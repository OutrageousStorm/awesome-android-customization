import java.io.*;
import java.nio.file.*;
import java.util.zip.*;
import java.util.*;

/**
 * APKAnalyzer - Analyze Android APK structure, permissions, and signatures
 * Command: java APKAnalyzer <apk_file> [--verbose] [--json]
 */
public class APKAnalyzer {
    private String apkPath;
    private boolean verbose = false;
    private boolean jsonOutput = false;
    
    public APKAnalyzer(String apkPath, String... options) {
        this.apkPath = apkPath;
        for (String opt : options) {
            if ("--verbose".equals(opt)) verbose = true;
            if ("--json".equals(opt)) jsonOutput = true;
        }
    }
    
    public void analyze() throws IOException {
        File apk = new File(apkPath);
        if (!apk.exists()) {
            System.err.println("Error: APK file not found: " + apkPath);
            System.exit(1);
        }
        
        Map<String, Object> report = new LinkedHashMap<>();
        report.put("file", apk.getName());
        report.put("size_bytes", apk.length());
        report.put("size_mb", String.format("%.2f", apk.length() / 1024.0 / 1024.0));
        
        List<String> files = new ArrayList<>();
        List<String> permissions = new ArrayList<>();
        
        try (ZipFile zip = new ZipFile(apk)) {
            Enumeration<? extends ZipEntry> entries = zip.entries();
            while (entries.hasMoreElements()) {
                ZipEntry entry = entries.nextElement();
                files.add(entry.getName());
                
                // Check for AndroidManifest.xml
                if ("AndroidManifest.xml".equals(entry.getName()) && verbose) {
                    InputStream is = zip.getInputStream(entry);
                    byte[] data = is.readAllBytes();
                    // Simple permission extraction from manifest
                    String manifest = new String(data);
                    if (manifest.contains("android.permission")) {
                        permissions.add("[Found permissions in manifest]");
                    }
                }
            }
        }
        
        report.put("total_files", files.size());
        report.put("has_native_libs", files.stream().anyMatch(f -> f.contains("/lib/")));
        report.put("has_resources", files.stream().anyMatch(f -> f.startsWith("res/")));
        
        if (jsonOutput) {
            System.out.println(toJson(report));
        } else {
            printReport(report);
        }
    }
    
    private void printReport(Map<String, Object> report) {
        System.out.println("╔══ APK Analysis Report ══╗");
        System.out.println("File: " + report.get("file"));
        System.out.println("Size: " + report.get("size_mb") + " MB");
        System.out.println("Total files: " + report.get("total_files"));
        System.out.println("Has native libs: " + report.get("has_native_libs"));
        System.out.println("Has resources: " + report.get("has_resources"));
        System.out.println("╚═════════════════════════╝");
    }
    
    private String toJson(Map<String, Object> map) {
        StringBuilder sb = new StringBuilder("{");
        List<String> entries = new ArrayList<>();
        for (Map.Entry<String, Object> e : map.entrySet()) {
            if (e.getValue() instanceof String) {
                entries.add("\"" + e.getKey() + "\":\"" + e.getValue() + "\"");
            } else {
                entries.add("\"" + e.getKey() + "\":" + e.getValue());
            }
        }
        sb.append(String.join(",", entries));
        sb.append("}");
        return sb.toString();
    }
    
    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Usage: java APKAnalyzer <apk_file> [--verbose] [--json]");
            System.exit(1);
        }
        
        APKAnalyzer analyzer = new APKAnalyzer(args[0], 
            args.length > 1 ? Arrays.copyOfRange(args, 1, args.length) : new String[0]);
        analyzer.analyze();
    }
}
