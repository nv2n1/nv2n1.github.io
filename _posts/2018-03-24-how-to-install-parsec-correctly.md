---
title: "How to Install PARSEC: A Step-by-Step Guide"
date: 2018-03-24 11:50:48 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-parsec-correctly/
---

PARSEC is a widely-used CPU-bound benchmark suite containing real applications and complex third-party library dependencies. The installation can be challenging due to these external requirements, but following this guide will get you up and running.

### Prerequisites

Before starting, install the required build tools and libraries:

``` bash
sudo apt-get update
sudo apt-get install build-essential pkg-config gettext autoconf automake libtool
```

On Fedora/RHEL-based systems:

``` bash
sudo dnf install gcc gcc-c++ pkg-config gettext autoconf automake libtool
```

### Downloading PARSEC

Download PARSEC 3.0 from the official repository:

``` bash
wget http://parsec.cs.princeton.edu/download/3.0/parsec-3.0.tar.gz
tar -xzf parsec-3.0.tar.gz
cd parsec-3.0
```

### Configuration and Build

Before building, you need to establish your environment. PARSEC provides build configurations for different compilers and threading models. Initialize the environment:

``` bash
source env.sh
```

The common build configurations are:

- `gcc-pthreads` — GCC with POSIX threads
- `gcc-openmp` — GCC with OpenMP
- `gcc` — GCC with sequential execution

### Building Benchmarks

To build all benchmarks:

``` bash
parsecmgmt -a build -c gcc-pthreads
```

If you encounter errors during the build, they typically fall into two categories:

**Missing build configurations for specific kernels:**

Some benchmarks like `freqmine` are implemented with OpenMP rather than pthread support. If you get an error like:

    [PARSEC] Error: Cannot find local build configuration 'gcc-pthreads.bldconf' for package parsec.freqmine

Build that specific benchmark with the appropriate configuration:

``` bash
parsecmgmt -a build -p freqmine -c gcc-openmp
```

**SSL/TLS library issues:**

Older benchmark components may fail due to modern OpenSSL restrictions. If you encounter SSL-related build failures, you can disable documentation generation by modifying the build configuration or removing problematic targets from Makefiles.

### Running Benchmarks

After a successful build, run benchmarks in test mode first:

``` bash
parsecmgmt -a run -c gcc-pthreads -i test -p freqmine
```

For full benchmark runs (these take significantly longer):

``` bash
parsecmgmt -a run -c gcc-pthreads -i native
```

### Troubleshooting

**Build failures on modern systems:** PARSEC 3.0 was released in 2012 and may have compatibility issues with current toolchains. You may need to:

- Update compiler flags in build configuration files
- Patch outdated dependency sources
- Use container-based installation for reproducibility

**Missing or outdated dependencies:** Ensure all required libraries are installed before starting. The build system should report missing dependencies clearly.

**Architecture mismatches:** PARSEC supports both 32-bit and 64-bit builds. Verify your intended architecture matches your system and available libraries.

### Validation

Verify installation success by checking the run output directory:

``` bash
ls -la results/
```

Each benchmark run produces results in timestamped directories containing execution logs and performance metrics.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
