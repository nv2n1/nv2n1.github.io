---
title: "Setting Up Java Environment Variables on Linux"
date: 2018-03-24 08:22:40 +0000
layout: post
canonical: https://www.systutorials.com/how-to-set-up-the-java-environment-in-linux/
---

When you install a JDK on Linux, you need to configure environment variables so your shell uses the correct Java binary and build tools can locate the installation. If you have multiple Java versions installed, proper configuration becomes essential.

## Why Set Java Environment Variables

Setting `JAVA_HOME` and `PATH` ensures:

- Tools and applications can locate the Java installation
- The correct `java` and `javac` binaries execute from your shell
- Build tools (Maven, Gradle, Ant) find the right JDK
- IDEs and other Java applications can auto-detect your JDK

## Installation Methods

Your configuration approach depends on how you installed Java:

**Package manager (recommended for most users):**

``` bash
# Fedora/RHEL/CentOS
sudo dnf install java-21-openjdk java-21-openjdk-devel

# Ubuntu/Debian
sudo apt install openjdk-21-jdk

# Alpine
apk add openjdk21
```

Package-managed installations typically configure environment variables automatically. The system often places JDK files in `/usr/lib/jvm/`.

**Oracle JDK or other distributions:**

Manual tarball or RPM installations usually land in `/opt/java/` or `/usr/java/`. You’ll need to configure variables manually.

**Checking existing Java setup:**

``` bash
which java
java -version
echo $JAVA_HOME
ls -l /usr/lib/jvm/  # typical package manager location
```

On modern distributions with package-managed Java, check if the system already configured variables:

``` bash
cat /etc/profile.d/java.sh
```

## Using update-alternatives (Best Method for Multiple Versions)

The `update-alternatives` system is cleaner than manual PATH editing and survives system updates:

``` bash
# List currently registered alternatives
sudo update-alternatives --list java
sudo update-alternatives --list javac

# Register a new Java installation
sudo update-alternatives --install /usr/bin/java java /opt/java/jdk-21/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /opt/java/jdk-21/bin/javac 1

# Switch between versions interactively
sudo update-alternatives --config java
```

The number at the end (here `1`) is the priority — higher numbers take precedence when running `--auto`. This approach works across all POSIX-compliant systems and handles symlink management automatically.

## Manual Configuration (When Necessary)

If you’re not using package managers or `update-alternatives`, configure variables in `~/.bashrc` or `~/.zshrc`:

``` bash
export JAVA_HOME=/opt/java/jdk-21
export PATH=$JAVA_HOME/bin:$PATH
```

For system-wide configuration affecting all users, create `/etc/profile.d/java.sh`:

``` bash
sudo tee /etc/profile.d/java.sh > /dev/null <<'EOF'
export JAVA_HOME=/opt/java/jdk-21
export PATH=$JAVA_HOME/bin:$PATH
EOF

sudo chmod 644 /etc/profile.d/java.sh
```

To apply immediately without logging out:

``` bash
source /etc/profile.d/java.sh
```

**Avoid hardcoding version numbers.** Create a symlink to simplify future upgrades:

``` bash
sudo ln -s /opt/java/jdk-21 /opt/java/default
export JAVA_HOME=/opt/java/default
```

## CLASSPATH (Usually Not Required)

Modern Java doesn’t use `CLASSPATH` by default — the classpath is set by each application or build tool. Only set it if a legacy application explicitly requires it:

``` bash
export CLASSPATH=.:$JAVA_HOME/lib/*:$CLASSPATH
```

Most developers and tools manage classpath through build files (pom.xml, build.gradle), not environment variables.

## Verifying Your Configuration

After any changes, reload the shell and test:

``` bash
source ~/.bashrc
java -version
javac -version
echo $JAVA_HOME
```

Expected output for Java 21:

    openjdk version "21.0.2" 2024-01-16
    OpenJDK Runtime Environment (build 21.0.2+13-58)
    OpenJDK 64-Bit Server VM (build 21.0.2+13-58, mixed mode, sharing)

## Troubleshooting

**“command not found: java”**

Verify the path exists and is in PATH:

``` bash
ls -l $JAVA_HOME/bin/java
echo $PATH | tr ':' '\n' | grep java
```

**Wrong Java version executing**

The first `java` binary in PATH wins. Check the order:

``` bash
echo $PATH | tr ':' '\n'
which java
```

Remove conflicting paths from your shell rc file or use `update-alternatives --config java` to prioritize the correct version.

**Build tools can’t find the JDK**

Maven, Gradle, and other build tools check `JAVA_HOME` explicitly, separate from `PATH`. Always set it:

``` bash
export JAVA_HOME=/opt/java/default
mvn -version  # shows JAVA_HOME Maven detected
gradle --version  # shows JAVA_HOME Gradle detected
```

If these commands still report the wrong JDK, check for `MAVEN_JAVA_HOME` or `GRADLE_JAVA_HOME` environment variables that may override global settings.

**Finding where package managers installed Java**

``` bash
# Debian/Ubuntu
dpkg -L openjdk-21-jdk | grep bin/java | head -1

# RHEL/Fedora
rpm -ql java-21-openjdk | grep bin/java | head -1

# Generic method
find /usr -name java -type f 2>/dev/null
```

## Best Practices

- Use package managers when possible — they handle configuration and updates automatically
- Prefer `update-alternatives` for managing multiple JDK versions instead of manual PATH editing
- Set `JAVA_HOME` in shell rc files or system-wide, even if `java` is in PATH — build tools rely on it
- Use symlinks (like `/opt/java/default`) instead of hardcoding version numbers
- Run `java -version` and `javac -version` after any changes to confirm the correct version
- In containers or CI pipelines, set `JAVA_HOME` in Dockerfile or pipeline config, not relying on inherited shell config
