---
title: "Installing gfortran on CentOS 7"
date: 2018-03-24 11:54:13 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-install-gfortran-on-centos-7/
---

GFortran is the GNU Fortran compiler from the GCC toolchain. It’s essential for scientific computing, numerical simulations, and legacy Fortran code maintenance.

### Quick Install

On modern RHEL-based systems (RHEL 9+, Rocky Linux, AlmaLinux, CentOS Stream):

``` bash
sudo dnf install gcc-gfortran
```

On CentOS 7 (EOL since June 2024), the older yum package manager still works:

``` bash
sudo yum install gcc-gfortran
```

However, **CentOS 7 is no longer supported**. If you’re still running it, plan a migration to Rocky Linux or AlmaLinux — they provide binary compatibility and continued security updates.

### Verify Installation

After installation, confirm GFortran is working:

``` bash
gfortran --version
```

You should see output like:

    GNU Fortran (GCC) 12.3.1 20230816 (Red Hat 12.3.1-2)

### Compile a Simple Program

Test with a basic Fortran program:

``` fortran
program hello
  print *, 'Hello from Fortran'
end program hello
```

Save as `hello.f90`, then compile:

``` bash
gfortran -o hello hello.f90
./hello
```

### Installing Full Development Tools

For more comprehensive Fortran development, install the entire `gcc-toolset`:

``` bash
sudo dnf install gcc gcc-c++ gcc-gfortran make
```

On older systems, the “Development Tools” group provides these:

``` bash
sudo yum groupinstall "Development Tools"
```

### HPC Environments and Modern Workflows

For scientific computing with multiple compiler versions, MPI libraries, or BLAS/LAPACK dependencies, use a package manager designed for HPC:

**Spack** — manages complex dependency trees and multiple compiler toolchains:

``` bash
git clone https://github.com/spack/spack.git
cd spack
. share/spack/setup-env.sh
spack install gcc@13.2.0
spack install openmpi %gcc@13.2.0
```

**EasyBuild** — provides pre-configured recipes for scientific software:

``` bash
pip install easybuild
eb GCC-13.2.0.eb -r
eb OpenMPI-4.1.5-GCC-13.2.0.eb -r
```

Conda/Mamba is another lightweight option for isolated environments:

``` bash
mamba install -c conda-forge gfortran openmpi
```

### Troubleshooting

**Command not found:** GFortran isn’t in your PATH. Verify installation with `which gfortran`. If nothing returns, reinstall: `sudo dnf reinstall gcc-gfortran`.

**Version mismatch:** Multiple GCC versions may be installed. Use `update-alternatives` to switch:

``` bash
sudo update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-12 100
sudo update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-13 200
sudo update-alternatives --config gfortran
```

**Missing dependencies for compilation:** Some Fortran packages need BLAS/LAPACK. Install them with:

``` bash
sudo dnf install blas-devel lapack-devel
```

### Common Compilation Flags

When building Fortran code, you’ll often use:

- `-O2` or `-O3` — optimization levels
- `-Wall` — enable warnings
- `-g` — debug symbols
- `-fcheck=all` — runtime bounds checking
- `-fopenmp` — OpenMP parallelization support

Example:

``` bash
gfortran -O3 -Wall -fopenmp -o program program.f90
```

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
