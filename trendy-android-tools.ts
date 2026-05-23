#!/usr/bin/env -S deno run --allow-net --allow-env
/**
 * Trendy Android Tools Fetcher
 * Scans r/Android for trending Android customization tools
 * Validates GitHub repos, fetches star counts, outputs JSON
 */

import { parse } from "https://deno.land/std@0.208.0/flags/mod.ts";

interface ToolResult {
  name: string;
  url: string;
  stars: number;
  description: string;
  mentions: number;
}

async function fetchTrendingTools(): Promise<ToolResult[]> {
  const subredditUrl =
    "https://www.reddit.com/r/Android/top.json?t=week&limit=100";

  const response = await fetch(subredditUrl, {
    headers: { "User-Agent": "TrendyAndroidToolsFetcher/1.0" },
  });

  const data = await response.json();
  const posts = data.data.children || [];

  const toolCounts: Map<string, { mentions: number; url: string }> = new Map();

  // Parse posts for GitHub URLs
  for (const post of posts) {
    const text = `${post.data.title} ${post.data.selftext}`.toLowerCase();
    const urls = text.match(/https:\/\/github\.com\/[\w\-]+\/[\w\-]+/gi) || [];

    for (const url of urls) {
      const normalized = url.toLowerCase();
      const existing = toolCounts.get(normalized) || {
        mentions: 0,
        url: normalized,
      };
      existing.mentions++;
      toolCounts.set(normalized, existing);
    }
  }

  // Fetch GitHub star counts
  const tools: ToolResult[] = [];
  const githubToken = Deno.env.get("GITHUB_TOKEN") || "";

  for (const [url, data] of toolCounts) {
    if (data.mentions < 2) continue; // Only tools mentioned 2+ times

    const [, owner, repo] = url.match(
      /github\.com\/([^/]+)\/([^/]+)/
    ) || ["", "", ""];
    if (!owner || !repo) continue;

    try {
      const repoData = await fetch(
        `https://api.github.com/repos/${owner}/${repo}`,
        {
          headers: githubToken
            ? { Authorization: `token ${githubToken}` }
            : {},
        }
      ).then((r) => r.json());

      tools.push({
        name: `${owner}/${repo}`,
        url,
        stars: repoData.stargazers_count || 0,
        description: repoData.description || "",
        mentions: data.mentions,
      });
    } catch (e) {
      // Skip broken repos
    }
  }

  return tools.sort((a, b) => b.stars - a.stars);
}

async function main() {
  const args = parse(Deno.args, { string: ["output"] });

  try {
    console.log("🔍 Fetching trending Android tools from r/Android...");
    const tools = await fetchTrendingTools();

    console.log(`✅ Found ${tools.length} trending tools\n`);
    console.table(tools);

    if (args.output) {
      await Deno.writeTextFile(args.output, JSON.stringify(tools, null, 2));
      console.log(`\n📝 Results saved to ${args.output}`);
    }
  } catch (error) {
    console.error("❌ Error:", error.message);
    Deno.exit(1);
  }
}

main();
