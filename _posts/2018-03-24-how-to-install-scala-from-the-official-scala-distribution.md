---
title: "Installing Scala from Official Sources"
date: 2018-03-24 08:16:53 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-scala-from-the-official-scala-distribution/
---

When your distro’s package repositories lag behind, installing Scala directly from the official release is straightforward. This approach works on any Linux system with Java already installed.

### Prerequisites

You’ll need a JDK installed. On most systems:

``` bash
# Debian/Ubuntu
apt install default-jdk

# RHEL/Fedora/CentOS
dnf install java-17-openjdk-devel

# Alpine
apk add openjdk17
```

Verify your Java installation:

``` bash
java -version
javac -version
```

### Download and install Scala

Download the latest Scala release from <a href="https://www.scala-lang.org/download/" rel="nofollow noopener" target="_blank">scala-lang.org/download</a>. The current stable version is Scala 3.x, though some projects still use 2.13.x for compatibility.

``` bash
# Download Scala 3.5.x (adjust version as needed)
wget https://github.com/lampepfl/dotty/releases/download/3.5.0/scala-3.5.0.tgz

# Extract to /opt
tar xzf scala-3.5.0.tgz
mv scala-3.5.0 /opt/scala
```

### Set up the PATH

For system-wide access, create a profile script:

``` bash
cat > /etc/profile.d/scala.sh << 'EOF'
export PATH="/opt/scala/bin:$PATH"
EOF
chmod 644 /etc/profile.d/scala.sh
```

Users can then source this on login, or add it to their shell configuration:

``` bash
echo 'export PATH="/opt/scala/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Verify installation:

``` bash
scala -version
scalac -version
```

### Version management with alternatives

If you need to support multiple Scala versions, use `update-alternatives` on Debian-based systems or maintain separate installations:

``` bash
update-alternatives --install /usr/local/bin/scala scala /opt/scala-3.5.0/bin/scala 100
update-alternatives --install /usr/local/bin/scalac scalac /opt/scala-3.5.0/bin/scalac 100
```

Switch versions with:

``` bash
update-alternatives --config scala
update-alternatives --config scalac
```

### Automated installation script

For repeated deployments, create a reusable installation script:

``` bash
#!/bin/bash
set -e

SCALA_VERSION=${1:-3.5.0}
INSTALL_DIR=/opt
SCALA_HOME="${INSTALL_DIR}/scala-${SCALA_VERSION}"

echo "Installing Scala ${SCALA_VERSION}..."

cd /tmp
wget -q "https://github.com/lampepfl/dotty/releases/download/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz"
tar xzf "scala-${SCALA_VERSION}.tgz"
mv "scala-${SCALA_VERSION}" "${SCALA_HOME}"

cat > /etc/profile.d/scala.sh << EOF
export PATH="${SCALA_HOME}/bin:\$PATH"
EOF

echo "Scala ${SCALA_VERSION} installed to ${SCALA_HOME}"
echo "Run: source /etc/profile.d/scala.sh"
```

Save as `install-scala.sh`, make it executable, and run:

``` bash
chmod +x install-scala.sh
./install-scala.sh 3.5.0
```

### Using SDKMAN (alternative approach)

For user-level installations without root access, SDKMAN is cleaner:

``` bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install scala 3.5.0
```

This handles PATH configuration automatically and supports easy version switching.

### Troubleshooting

If `scala` command isn’t found after installation, check that `/etc/profile.d/scala.sh` exists and is sourced. New shell sessions will load it automatically; existing sessions need `source /etc/profile.d/scala.sh`.

For development, pin your Scala version in build files (sbt, Maven, Gradle) rather than relying on system PATH, ensuring consistent builds across environments.

## Troubleshooting Common Issues

If you encounter problems during installation, check these common solutions:

- Ensure your system packages are up to date before installing new software
- Check for conflicting packages that might prevent installation
- Verify network connectivity if downloading packages from external repositories
- Review system logs in /var/log/ for detailed error messages

## Verification Steps

After installation, verify everything is working correctly by checking the installed version and running basic functionality tests. Most command-line tools respond to the –version or -v flag to display their version information.

## Keeping Your Installation Updated

Regularly update your system to receive security patches and bug fixes. On Fedora, use dnf update. On Ubuntu and Debian, use apt update followed by apt upgrade. For software installed via language-specific package managers like pip, npm, or gem, check their respective update commands.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.
