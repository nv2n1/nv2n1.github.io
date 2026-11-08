---
title: "Installing Java Runtime Environment on Linux x86-64"
date: 2018-03-24 08:18:42 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-jre-for-chrome-on-linux-x86-64/
---

Java Runtime Environment (JRE) is required to run Java applications on Linux. On x86-64 systems, you have several installation options ranging from open-source to Oracle’s commercial builds.

## Install OpenJDK (Recommended)

OpenJDK is the open-source implementation and is available in all major Linux distributions:

```wp-block-code
# Fedora / RHEL / Rocky Linux
sudo dnf install java-17-openjdk

# Ubuntu / Debian
sudo apt install default-jre

# For a specific version
sudo dnf install java-11-openjdk    # Fedora
sudo apt install openjdk-11-jre     # Ubuntu
```

Verify the installation:

```wp-block-code
java -version
```

## Multiple Java Versions

You can install multiple JRE/JDK versions and switch between them:

```wp-block-code
# Install multiple versions
sudo dnf install java-11-openjdk java-17-openjdk java-21-openjdk

# List installed versions
alternatives --list | grep java

# Switch the default Java version
sudo alternatives --config java
```

On Ubuntu/Debian:

```wp-block-code
sudo update-alternatives --config java
```

Select the version you want from the menu. The change takes effect immediately.

## Setting JAVA_HOME

Many Java applications require the `JAVA_HOME` environment variable. Find your Java installation path:

```wp-block-code
# Find the Java home directory
readlink -f $(which java) | sed 's:/bin/java::'
```

Set it in your shell configuration:

```wp-block-code
# Add to ~/.bashrc or ~/.profile
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export PATH=$JAVA_HOME/bin:$PATH
```

For system-wide configuration, add to `/etc/profile.d/java.sh`:

```wp-block-code
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk' | sudo tee /etc/profile.d/java.sh
source /etc/profile.d/java.sh
```

## Install Oracle JRE

Oracle’s JRE requires manual download and installation:

```wp-block-code
# Download from Oracle's website
# https://www.oracle.com/java/technologies/downloads/

# Extract and install
tar -xzf jre-17_linux-x64_bin.tar.gz
sudo mv jre-17.* /usr/local/java/

# Add to alternatives
sudo alternatives --install /usr/bin/java java /usr/local/java/jre-17.*/bin/java 1
```

Note: Oracle JRE has different licensing terms than OpenJDK. For most use cases, OpenJDK is functionally equivalent and doesn’t require a commercial license.

## Verify JRE vs JDK

JRE only runs Java applications. JDK (Java Development Kit) includes the compiler and development tools. Check what you have:

```wp-block-code
# Check if JDK is installed
javac -version

# If "command not found", you have JRE only
# If it shows a version, you have JDK (which includes JRE)
```

Install the JDK if you need to compile Java code:

```wp-block-code
sudo dnf install java-17-openjdk-devel    # Fedora
sudo apt install openjdk-17-jdk           # Ubuntu
```

## Testing Your JRE Installation

Create a simple test program:

```wp-block-code
// Test.java
public class Test {
    public static void main(String[] args) {
        System.out.println("Java is working! Version: " +
            System.getProperty("java.version"));
        System.out.println("JRE home: " +
            System.getProperty("java.home"));
    }
}
```

```wp-block-code
# Compile (requires JDK)
javac Test.java

# Run (JRE is sufficient)
java Test
```

## Quick Reference

- `sudo dnf install java-17-openjdk` — Install JRE on Fedora
- `sudo apt install default-jre` — Install JRE on Ubuntu
- `java -version` — Verify installation
- `alternatives --config java` — Switch Java versions
- `JAVA_HOME=/usr/lib/jvm/java-17-openjdk` — Set Java home

## Container-Based Java Runtime

For isolated Java environments, use Docker or Podman:

```wp-block-code
# Run a Java application in a container
podman run --rm -v $(pwd):/app:Z eclipse-temurin:17-jre java -jar /app/myapp.jar

# Build a custom image
FROM eclipse-temurin:17-jre
COPY myapp.jar /app/myapp.jar
ENTRYPOINT ["java", "-jar", "/app/myapp.jar"]
```

Popular container JRE images:

- `eclipse-temurin:17-jre` — Adoptium Eclipse Temurin (recommended)
- `amazoncorretto:17` — Amazon Corretto
- `azul/zulu-openjdk:17-jre` — Azul Zulu

These images are regularly updated with security patches and are smaller than full JDK images.

## JRE Security Configuration

For security-sensitive deployments, configure the JRE’s security policies:

```wp-block-code
# Edit Java security policy
sudo nano $JAVA_HOME/conf/security/java.security

# Key settings:
# securerandom.source=file:/dev/urandom  (or /dev/random for stronger entropy)
# jdk.tls.disabledAlgorithms=SSLv3, TLSv1, TLSv1.1  (disable weak protocols)
# jdk.jar.disabledAlgorithms=MD2, MD5, RSA keySize < 1024  (disable weak signatures)
```

Check the JRE's crypto strength:

```wp-block-code
java -XX:+PrintFlagsFinal -version 2>&1 | grep -i crypto
```
