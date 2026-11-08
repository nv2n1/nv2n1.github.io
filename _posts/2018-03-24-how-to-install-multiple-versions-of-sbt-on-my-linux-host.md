---
title: "Managing Multiple sbt Versions on Linux"
date: 2018-03-24 11:41:00 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-multiple-versions-of-sbt-on-my-linux-host/
---

When working with multiple Scala projects, you’ll often need different sbt versions. A project using sbt 1.9.x may not be compatible with sbt 0.13.x, and manually switching between system-wide installations becomes tedious and error-prone.

## Using sbt-extras for automatic version detection

The most reliable approach is <a href="https://github.com/paulp/sbt-extras" rel="nofollow noopener" target="_blank">sbt-extras</a>, a wrapper script that automatically detects and uses the correct sbt version for each project.

**Installation:**

``` bash
curl -s https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt > ~/bin/sbt
chmod +x ~/bin/sbt
```

Ensure `~/bin` is in your `$PATH` before `/usr/bin`.

**How it works:**

sbt-extras reads your project’s `build.properties` file (in the `project/` directory) to determine which version to use. If no version is specified, it defaults to the latest available.

Example output from different projects in the same session:

``` bash
$ cd my-project-v1
$ sbt about
[info] This is sbt 1.9.8
[info] The current project is built against Scala 3.3.1

$ cd ../legacy-project
$ sbt about
[info] This is sbt 0.13.18
[info] The current project is built against Scala 2.10.7
```

The script downloaded the appropriate version automatically without any manual intervention.

## Specifying sbt versions

To pin a specific sbt version in a project, create or edit `project/build.properties`:

```properties
sbt.version=1.9.8
```

You can also override the version temporarily from the command line:

``` bash
sbt -sbt-version 0.13.18 compile
```

## Manual version management with SDKMAN!

If you prefer more control or need to switch versions frequently across different terminal sessions, use <a href="https://sdkman.io/" rel="nofollow noopener" target="_blank">SDKMAN!</a>:

``` bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install sbt 1.9.8
sdk install sbt 0.13.18
```

Switch versions in the current shell:

``` bash
sdk use sbt 0.13.18
```

Set a default globally:

``` bash
sdk default sbt 1.9.8
```

## Troubleshooting version conflicts

If sbt-extras doesn’t detect the correct version, verify `project/build.properties` exists and contains valid syntax:

``` bash
cat project/build.properties
# Output: sbt.version=1.9.8
```

For projects without `build.properties`, sbt-extras falls back to its configured default. Check which version you’re using:

``` bash
sbt -version
```

If you have stale cached versions causing issues, clear the sbt cache:

``` bash
rm -rf ~/.sbt/boot
```

## Best practices

- Always commit `project/build.properties` to version control so team members use consistent versions
- Use sbt-extras by default—it’s the standard in the Scala ecosystem
- Document any version constraints in your project’s README
- Test locally with the exact version specified before pushing to CI/CD pipelines

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
