---
title: "Installing NS-2 and NS-3 on Fedora"
date: 2013-07-12 16:32:26 +0000
modified: 2026-04-12 16:56:04 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /install-ns-2-and-ns-3-on-fedora-linux/
---

ns (Network Simulator) is a discrete-event simulator used primarily for research and educational purposes in networking. The two major versions—ns-2 and ns-3—are substantially different in architecture and usage patterns. This guide covers installation on current Fedora systems.

## Installing ns-2 on Fedora

**Note:** ns-2 is legacy software and requires significant compatibility workarounds on modern systems. Consider ns-3 unless you need specific ns-2 functionality or existing scripts.

### Prerequisites

Install base development tools and X11 libraries:

``` bash
sudo dnf install gcc gcc-c++ make libX11-devel libXt-devel libXmu-devel
```

### Download and extract

``` bash
wget https://sourceforge.net/projects/nsnam/files/allinone/ns-allinone-2.34/ns-allinone-2.34.tar.gz/download -O ns-allinone-2.34.tar.gz
tar xf ns-allinone-2.34.tar.gz
cd ns-allinone-2.34
```

### Build and install

ns-2 requires compatibility with older compiler versions. Use the modern gcc with appropriate flags:

``` bash
CXX=g++ CC=gcc ./install
```

If you encounter build failures with modern gcc (likely), patch the code or use a container with an older compiler. Alternatively, consider using Docker with a compatible base image.

### Environment configuration

Add the following to your shell configuration file (`~/.bashrc` for bash, `~/.zshrc` for zsh):

``` bash
export NS_HOME=$HOME/ns-allinone-2.34
export PATH=$NS_HOME/bin:$NS_HOME/tcl8.4.18/unix:$NS_HOME/tk8.4.18/unix:$PATH
export LD_LIBRARY_PATH=$NS_HOME/otcl-1.13:$NS_HOME/ns-2.34/lib:/usr/local/lib:$LD_LIBRARY_PATH
export TCL_LIBRARY=$NS_HOME/tcl8.4.18/library
```

Reload your shell configuration:

``` bash
source ~/.bashrc
```

Verify installation:

``` bash
nam
ns
```

## Installing ns-3 on Fedora

ns-3 is the recommended choice for new projects. It features a cleaner C++ API and better maintainability.

### Prerequisites

Install required dependencies:

``` bash
sudo dnf install libxml2 libxml2-devel gcc gcc-c++ make automake autoconf \
  binutils openssh-clients openssl python3 python3-devel mercurial scons \
  flex bison tcpdump valgrind gdb sqlite-devel
```

For additional Python bindings support, also install:

``` bash
sudo dnf install python3-dev
```

### Download and extract

``` bash
mkdir -p ~/ns-workspace
cd ~/ns-workspace
wget https://www.nsnam.org/release/ns-allinone-3.42.tar.bz2
tar xjf ns-allinone-3.42.tar.bz2
cd ns-allinone-3.42
```

(Replace 3.42 with the latest stable version available)

### Build

``` bash
./build.py
```

This script downloads and configures ns-3 along with dependencies. Proceed to the ns-3 directory:

``` bash
cd ns-3.42
```

### Configure with Waf

Configure for optimized builds with examples enabled:

``` bash
./waf -d optimized configure --enable-examples
./waf
```

For development builds with debugging symbols:

``` bash
./waf configure
./waf
```

### Validate installation

Run an example simulation:

``` bash
./waf shell
cd build/optimized/examples
./udp/udp-echo
```

Inspect the generated pcap trace file:

``` bash
tcpdump -tt -r udp-echo-0-1.pcap
```

Or view with more detail:

``` bash
tcpdump -tt -r udp-echo-0-1.pcap -v
```

### Running Python scripts

ns-3 supports Python-based simulations. Create a simple test script:

``` python
#!/usr/bin/env python3
import sys
sys.path.insert(0, '/path/to/ns-3.42/build/optimized/bindings/python')

import ns.core as ns_core
import ns.network as ns_network
import ns.internet as ns_internet

def main():
    ns_core.LogComponentEnable("UdpEchoServerApplication", ns_core.LOG_LEVEL_INFO)
    ns_core.LogComponentEnable("UdpEchoClientApplication", ns_core.LOG_LEVEL_INFO)

    ns_core.Simulator.Stop(ns_core.Seconds(10.0))
    ns_core.Simulator.Run()
    ns_core.Simulator.Destroy()

if __name__ == "__main__":
    main()
```

Run it with:

``` bash
./waf shell python3 your_script.py
```

## Troubleshooting

**ns-2 compilation failures:** Modern gcc versions may reject ns-2’s code. Options include using `--std=gnu++98` flags or running ns-2 in a container based on Fedora 15 or CentOS 6.

**Missing modules in ns-3:** If examples don’t build, ensure all optional dependencies are installed. Check the configure output for warnings about missing features.

**Python bindings not found:** Ensure you’re running scripts with `./waf shell` to set up the correct library paths.

**Performance:** For large simulations, build with optimization flags and allocate sufficient RAM. Monitor with `htop` or `vmstat`.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Installing NS-2 and NS-3 on Fedora with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Installing NS-2 and NS-3 on Fedora. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
