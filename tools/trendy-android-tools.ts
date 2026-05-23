import Deno from "https://deno.land/std@0.152.0/encoding/base64.ts";

/**
 * Trendy Android Tools Validator
 * Fetch trending Android tools from community sources and validate them
 * Purpose: Keep awesome-android-customization updated with real trending tools
 */

interface Tool {
  name: string;
  url: string;
  description: string;
  stars?: number;
  trending?: boolean;
}

const SUBREDDIT_URL = "https://api.reddit.com/r/Android/top?t=week&limit=25";
const GITHUB_API = "https://api.github.com";

async function fetchRedditTrending(): Promise<Tool[]> {
  try {
    const response = await fetch(SUBREDDIT_URL, {
      headers: { "User-Agent": "trendy-android-tools/1.0" },
    });
    const data = await response.json();

    const tools: Tool[] = [];
    for (const post of data.data.children) {
      const title = post.data.title;
      if (
        title.includes("tool") ||
        title.includes("app") ||
        title.includes("guide")
      ) {
        tools.push({
          name: title.substring(0, 60),
          url: post.data.url,
          description: post.data.selftext.substring(0, 100),
          trending: true,
        });
      }
    }
    return tools;
  } catch (error) {
    console.error("Reddit fetch failed:", error);
    return [];
  }
}

async function validateTool(tool: Tool): Promise<boolean> {
  try {
    const response = await fetch(tool.url, { method: "HEAD" });
    return response.status < 400;
  } catch {
    return false;
  }
}

async function getGitHubStars(toolName: string): Promise<number> {
  try {
    const response = await fetch(
      `${GITHUB_API}/search/repositories?q=${toolName}&sort=stars&order=desc&per_page=1`,
      {
        headers: {
          Authorization: `token ${Deno.env.get("GITHUB_ACCESS_TOKEN")}`,
        },
      }
    );
    const data = await response.json();
    return data.items?.[0]?.stargazers_count || 0;
  } catch {
    return 0;
  }
}

async function main() {
  console.log("🔍 Fetching trending Android tools...");

  const tools = await fetchRedditTrending();
  console.log(`Found ${tools.length} trending tool mentions`);

  const validated: Tool[] = [];
  for (const tool of tools) {
    const isValid = await validateTool(tool);
    if (isValid) {
      const stars = await getGitHubStars(tool.name);
      tool.stars = stars;
      validated.push(tool);
      console.log(
        `✅ ${tool.name} (${stars} ⭐) — Valid & trending on Reddit`
      );
    }
  }

  console.log(
    `\n📊 Validated ${validated.length} active tools for curated list`
  );
  console.log("💡 Top 3 trending:\n");

  validated.sort((a, b) => (b.stars || 0) - (a.stars || 0));
  validated.slice(0, 3).forEach((tool) => {
    console.log(`- **${tool.name}** (${tool.stars} ⭐)`);
    console.log(`  ${tool.description}\n`);
  });

  return validated;
}

main();
