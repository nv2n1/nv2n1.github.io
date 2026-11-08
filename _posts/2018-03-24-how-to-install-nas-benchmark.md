---
title: "Setting Up NAS Benchmarking Tools"
date: 2018-03-24 11:50:48 +0000
author: "Weiwei Jia"
layout: post
categories: [code-optimization]
canonical: /how-to-install-nas-benchmark/
---

The NAS Parallel Benchmarks (NPB) remain a standard tool for evaluating HPC system performance, though landscape has shifted toward additional metrics like HPCG and memory bandwidth tests. This guide covers installation and basic usage.

## Prerequisites

Before installing NPB, you’ll need:

- **Fortran compiler** — gfortran is the standard choice on most systems
- **MPI implementation** — OpenMPI or Intel MPI (MPICH works but is less common in modern clusters)
- **Make** — standard build tools
- **Python 3** — some build scripts and utilities require it

Install on Ubuntu/Debian:

``` bash
sudo apt update
sudo apt install gfortran libopenmpi-dev openmpi-bin make
```

On RHEL/CentOS/Fedora:

``` bash
sudo dnf install gcc-gfortran openmpi openmpi-devel make
```

## Download and Extract

Download the latest NPB source from the official NASA repository:

``` bash
cd /opt
sudo wget https://www.nas.nasa.gov/assets/npb/NPB3.4.2.tar.gz
sudo tar xzf NPB3.4.2.tar.gz
sudo chown -R $USER:$USER NPB3.4.2
cd NPB3.4.2
```

## Build Configuration

The NPB suite uses a makefile-based build system. First, configure your compiler settings:

``` bash
cd NPB3.4.2
cp config/make.def.template config/make.def
```

Edit `config/make.def` and ensure these lines match your environment:

``` makefile
MPIF77 = mpif77
MPIF90 = mpif90
MPICC  = mpicc
FFLAGS = -O3 -march=native
F90FLAGS = -O3 -march=native
CFLAGS = -O3 -march=native
```

For Intel-based systems with ifort, modify accordingly:

``` makefile
MPIF77 = mpiifort
MPIF90 = mpiifort
FFLAGS = -O3 -xHost
```

## Build the Suite

Compile all benchmarks:

``` bash
make suite
```

This builds the standard benchmarks. Optionally build specific classes:

``` bash
make suite SUITE=BT NPROCS=4 CLASS=A
```

Build options:

- **NPROCS** — number of MPI processes (must be a perfect square for most benchmarks)
- **CLASS** — problem size (S, W, A, B, C, D, E, F in increasing size)
- **SUITE** — specific benchmark (BT, CG, EP, FT, IS, LU, MG, SP, UA)

Compiled binaries end up in `bin/` directory.

## Running Benchmarks

Execute a single benchmark with MPI:

``` bash
mpirun -np 4 ./bin/bt.A.4
```

The output shows execution time and performance metrics (Mflops).

For systematic testing across multiple problem sizes:

``` bash
for class in A B C; do
  for nprocs in 4 8 16; do
    echo "Running BT class $class with $nprocs processes"
    mpirun -np $nprocs ./bin/bt.$class.$nprocs
  done
done
```

## Container Deployment

Modern HPC clusters increasingly run benchmarks inside containers for reproducibility. Build a Singularity/Apptainer image:

``` bash
cat > npb.def << 'EOF'
Bootstrap: docker
From: ubuntu:24.04

%post
    apt-get update
    apt-get install -y gfortran libopenmpi-dev openmpi-bin make wget
    cd /opt
    wget https://www.nas.nasa.gov/assets/npb/NPB3.4.2.tar.gz
    tar xzf NPB3.4.2.tar.gz
    cd NPB3.4.2
    cp config/make.def.template config/make.def
    make suite

%environment
    export PATH=/opt/NPB3.4.2/bin:$PATH

%runscript
    exec "$@"
EOF

apptainer build npb.sif npb.def
apptainer exec npb.sif mpirun -np 4 bt.A.4
```

## Complementary Benchmarks

NPB remains useful for comparative analysis, but consider pairing it with:

- **HPCG** — tests sustained performance on modern hardware
- **Stream** — memory bandwidth benchmark (single-node focus)
- **OSU Micro-benchmarks** — latency and bandwidth for MPI operations
- **Linpack/LINPACK** — for Top500 comparisons (largely obsolete)

Install Stream for quick memory bandwidth testing:

``` bash
wget https://www.cs.virginia.edu/stream/stream.c
gcc -O2 -fopenmp stream.c -o stream
./stream
```

## Troubleshooting

**“mpif77: command not found”** — Ensure MPI is in PATH:

``` bash
export PATH=$PATH:/usr/lib64/openmpi/bin
```

**Compilation errors with gfortran** — Add `-ffixed-form` flag if needed for older Fortran code:

``` bash
echo "FFLAGS = -O3 -ffixed-form" >> config/make.def
```

**Performance inconsistencies** — Disable CPU frequency scaling during benchmarks:

``` bash
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

NPB benchmarks typically complete in seconds to minutes depending on problem class and system size, providing baseline performance metrics suitable for cluster validation and HPC system procurement evaluation.
