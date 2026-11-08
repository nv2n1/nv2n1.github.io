---
title: "Building a Secure Random Password Generator in Scala"
date: 2018-03-24 08:20:16 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/random-string-password-generator-in-scala/
---

When managing user accounts on a cluster or application, you’ll often need to generate temporary passwords programmatically. Here’s a practical approach using Scala’s built-in utilities.

## Basic implementation with scala.util.Random

For non-security-critical use cases, here’s a straightforward generator:

``` scala
def randomString(len: Int): String = {
  val rand = new scala.util.Random()
  val chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  (0 until len).map(_ => chars(rand.nextInt(chars.length))).mkString
}

// Usage
println(randomString(12))  // Example output: "aB3xKp9mN2Lq"
```

This pulls random characters from the alphanumeric set and concatenates them. You can easily modify the `chars` string to include or exclude specific character types—add special characters like `!@#$%` if your system requires them, or restrict to lowercase only if needed.

**Why not use nanoTime seeding?** The original example seeded with `System.nanoTime`, but `scala.util.Random()` already seeds itself adequately for non-cryptographic purposes. Don’t add custom seeding unless you have a specific reason.

## Secure password generation with SecureRandom

**Always use this for actual password generation.** Regular `Random` is not suitable for security-sensitive operations.

``` scala
import java.security.SecureRandom

object PasswordGenerator {
  private val secureRandom = SecureRandom.getInstanceStrong()
  private val charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

  def generate(length: Int): String = {
    (0 until length)
      .map(_ => charset(secureRandom.nextInt(charset.length)))
      .mkString
  }
}

// Usage
println(PasswordGenerator.generate(16))
```

This uses `SecureRandom.getInstanceStrong()`, which accesses the OS-level entropy source. On Linux, this typically reads from `/dev/urandom`. The performance overhead is negligible for password generation, which doesn’t happen at high frequency.

## Alternative: entropy-based generation

If you prefer a more compact approach that leverages higher entropy directly:

``` scala
import java.security.SecureRandom
import scala.math.BigInt

object PasswordGenerator {
  private val secureRandom = SecureRandom.getInstanceStrong()

  def generateFromEntropy(length: Int): String = {
    val entropy = new Array[Byte](length)
    secureRandom.nextBytes(entropy)
    BigInt(1, entropy)
      .toString(36)
      .takeRight(length)
      .padTo(length, '0')
  }
}
```

This generates raw random bytes and converts them to base-36 (alphanumeric). It’s slightly different from character-by-character selection—useful if you want maximum entropy density.

## Practical considerations

**Length:** For temporary passwords assigned to users who’ll change them immediately, 12–16 characters suffices. For system accounts or service tokens, use 24+ characters.

**Character restrictions:** Some systems don’t accept certain characters in passwords. If you need to exclude similar-looking characters (like `0` and `O`), filter them:

``` scala
private val charset = "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz"
```

**Logging:** Never log generated passwords in plain text. If you must log, hash them first or log only a checksum.

**Distribution:** If delivering passwords via email or log files, ensure the delivery mechanism is encrypted. Consider having users set their own passwords instead, using the generated string only as a temporary token.

Use `SecureRandom` for all security-related password generation. The tiny performance cost is irrelevant compared to the cryptographic assurance it provides.

## 2026 Best Practices and Advanced Techniques

For Building a Secure Random Password Generator in Scala, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
