---
title: "Configuring Scala Compiler Options in sbt"
date: 2018-03-24 08:20:51 +0000
layout: post
canonical: https://www.systutorials.com/how-to-set-options-for-scala-in-sbt/
---

When the Scala compiler emits warnings like deprecation notices, you need to pass compiler flags to see the details. The solution is to configure `scalacOptions` in your sbt build.

## Session-Only Configuration

During an interactive sbt session, add options temporarily:

    set scalacOptions += "-deprecation"

This applies only to the current session and is lost after reload or exit.

## Permanent Configuration in build.sbt

For persistent configuration, add `scalacOptions` to your `build.sbt` file:

``` scala
scalacOptions += "-deprecation"
```

For multiple options, use a sequence:

``` scala
scalacOptions ++= Seq(
  "-deprecation",
  "-feature",
  "-unchecked",
  "-Ywarn-unused",
  "-Ywarn-dead-code"
)
```

## Common Scala Compiler Options

| Option | Purpose |
|----|----|
| `-deprecation` | Show details about deprecated API usage |
| `-feature` | Warn about advanced features requiring explicit imports |
| `-unchecked` | Show details about unchecked type erasure warnings |
| `-Ywarn-unused` | Warn about unused imports and local definitions |
| `-Ywarn-dead-code` | Warn about unreachable code |
| `-explain` | Explain errors and warnings in detail (Scala 3) |
| `-explain-types` | Provide detailed type mismatch explanations (Scala 3) |
| `-Xsource:3` | Enable Scala 3 migration warnings for forward compatibility |
| `-release 11` | Target a specific JVM version (Scala 3.3+) |

## Configuration by Build Scope

Apply different options to main code versus test code:

``` scala
scalacOptions ++= Seq("-deprecation", "-feature")

scalacOptions.in(Test) += "-Ywarn-unused:implicits"
```

This ensures tests don’t fail on warnings that are acceptable in production code.

## Scala Version-Specific Options

Some options only work with certain Scala versions. Use conditional logic based on the active Scala version:

``` scala
scalacOptions ++= {
  if (scalaVersion.value.startsWith("3")) {
    Seq("-explain", "-explain-types")
  } else {
    Seq("-Ywarn-unused", "-Ywarn-dead-code")
  }
}
```

## Verifying Your Settings

Display all current compiler options:

    show scalacOptions

This shows the merged result of all `scalacOptions` assignments in your build, including those inherited from plugins and configurations.

## Performance Trade-offs

Warning options like `-Ywarn-unused` and `-Ywarn-dead-code` add compilation overhead, especially in large projects with many files. For faster iteration during development, conditionally disable expensive checks:

``` scala
scalacOptions ++= {
  if (sys.env.contains("FAST_BUILD")) {
    Seq("-deprecation", "-feature")
  } else {
    Seq("-deprecation", "-feature", "-Ywarn-unused", "-Ywarn-dead-code")
  }
}
```

Then use `FAST_BUILD=1 sbt compile` for quick builds during active development.

## Suppressing Specific Warnings

Use the `@nowarn` annotation (available in Scala 2.13+ and Scala 3) to suppress warnings on individual definitions without disabling the option globally:

``` scala
@nowarn("cat=deprecation")
def oldMethod() = {
  // code that uses deprecated API
}
```

This is cleaner than disabling warnings in build configuration and documents intent at the point of use. You can also suppress specific warnings with patterns like `msg=match is not exhaustive`.

## Common Patterns for CI/CD

In continuous integration, enable all warnings strictly:

``` scala
scalacOptions ++= {
  if (sys.env.contains("CI")) {
    Seq("-deprecation", "-feature", "-unchecked", "-Ywarn-unused", "-Ywarn-dead-code")
  } else {
    Seq("-deprecation", "-feature")
  }
}
```

This catches issues in CI without slowing down local development builds.

## 2026 Best Practices and Advanced Techniques

For Configuring Scala Compiler Options in sbt, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
