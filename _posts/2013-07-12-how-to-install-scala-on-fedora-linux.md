---
title: "Installing Scala on Linux"
date: 2013-07-12 16:32:34 +0000
author: "Eric Ma"
layout: post
categories: [linux-system-configuration]
canonical: /how-to-install-scala-on-fedora-linux/
---

Scala runs on the Java Virtual Machine, so you’ll need Java 11 or later installed first. Check your current version:

``` bash
java -version
```

If you don’t have Java installed, install it through your distribution’s package manager or use a tool like SDKMAN.

### Installing via SDKMAN (Recommended)

SDKMAN is the most reliable way to manage Scala and other JVM tools. Install SDKMAN first if you haven’t:

``` bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
```

Then install Scala:

``` bash
sdk install scala
```

This installs the latest stable version. To install a specific version:

``` bash
sdk install scala 3.3.1
```

List available versions:

``` bash
sdk list scala
```

Switch between installed versions:

``` bash
sdk use scala 3.3.1
```

### Installing from Official Distribution

Download the latest Scala release from <a href="https://www.scala-lang.org/download/" rel="nofollow noopener" target="_blank">scala-lang.org</a>:

``` bash
cd ~/Downloads
wget https://github.com/scala/scala/releases/download/v3.3.1/scala-3.3.1.tgz
tar -xzf scala-3.3.1.tgz
sudo mv scala-3.3.1 /opt/scala
```

Add Scala to your PATH by editing `~/.bashrc` or `~/.zshrc`:

``` bash
export PATH="/opt/scala/bin:$PATH"
```

Reload your shell:

``` bash
source ~/.bashrc
```

Verify the installation:

``` bash
scala -version
```

### Installing via Package Manager

Most distributions now carry reasonably current Scala packages:

**Fedora/RHEL:**

``` bash
sudo dnf install scala
```

**Debian/Ubuntu:**

``` bash
sudo apt install scala
```

**Arch:**

``` bash
sudo pacman -S scala
```

Check what version your distro offers before installing this way — sometimes it lags behind the latest releases. If you need a newer version, use SDKMAN or the official distribution method.

### Verification and Basic Usage

Verify installation worked:

``` bash
scala -version
scala --version
```

Launch the interactive REPL:

``` bash
scala
```

You’ll see the Scala prompt. Try a simple command:

``` scala
scala> println("Hello, Scala")
Hello, Scala
```

Exit with `Ctrl+D` or `:quit`.

Create a simple Scala file to test compilation:

``` bash
cat > HelloScala.scala << 'EOF'
object HelloScala {
  def main(args: Array[String]): Unit = {
    println("Hello from Scala!")
  }
}
EOF
```

Compile it:

``` bash
scalac HelloScala.scala
```

Run it:

``` bash
scala HelloScala
```

### Troubleshooting

If `scala` command isn’t found after installation, verify the PATH is set correctly:

``` bash
echo $PATH
which scala
```

Ensure the directory containing the `scala` binary is in your PATH. If using the official distribution, double-check the `/opt/scala/bin` symlink exists:

``` bash
ls -la /opt/scala/bin/scala
```

If you’re behind a corporate proxy, configure it for SDKMAN:

``` bash
export SDKMAN_CURL_CONNECT_TIMEOUT=15
export SDKMAN_CURL_TIMEOUT=120
```

For build tools like sbt (Scala Build Tool), install it separately:

``` bash
sdk install sbt
```

Or via package manager:

``` bash
sudo dnf install sbt        # Fedora
sudo apt install sbt        # Debian/Ubuntu
```

SDKMAN remains the cleanest approach for development since it isolates versions per-user and doesn’t require sudo.

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
