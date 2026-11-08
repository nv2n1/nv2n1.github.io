---
title: "Managing Multiple Go Versions on Ubuntu"
date: 2020-04-07 09:21:32 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-go-1-13-x-on-ubuntu-18-04/
---

When you need a specific Go version on Ubuntu, the default package manager often lags behind. Production systems like Kubernetes, Hyperledger Fabric, and other projects frequently require versions newer than what’s available in standard repositories. This guide covers system-level installation that allows multiple versions to coexist.

## Remove existing Go installations

Start by cleaning up any existing Go packages to prevent conflicts:

``` bash
sudo apt remove 'golang-*'
```

Check for and remove any manually installed Go directories:

``` bash
sudo rm -rf /usr/local/go /usr/local/go-*
```

## Download and verify the Go release

Visit the <a href="https://go.dev/dl/" rel="nofollow noopener" target="_blank">official Go downloads page</a> to find your required version. For x86_64 Ubuntu systems, download the binary archive and its checksum file:

``` bash
wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz.sha256
```

Verify integrity before extracting:

``` bash
sha256sum -c go1.23.4.linux-amd64.tar.gz.sha256
```

The output should display `go1.23.4.linux-amd64.tar.gz: OK`.

For other architectures, adjust the filename accordingly:

- `linux-arm64` — ARM64 systems (common for Raspberry Pi 4+, Apple Silicon via native builds)
- `linux-armv6l` — older ARM boards (Raspberry Pi Zero, Pi 1/2)
- `linux-ppc64le` — PowerPC systems
- `linux-s390x` — IBM Z systems

## Extract and install

Extract the tarball to a temporary location and move it to a versioned directory in `/usr/local`:

``` bash
tar xf go1.23.4.linux-amd64.tar.gz -C /tmp
sudo mv /tmp/go /usr/local/go-1.23.4
```

Using a versioned directory name simplifies maintaining multiple Go installations side-by-side.

## Configure environment variables

Create `/etc/profile.d/Z99-golang.sh` with the following content:

``` bash
export GOROOT=/usr/local/go-1.23.4
export PATH=$GOROOT/bin:$PATH
```

The `Z99-` prefix ensures this script runs after other profile.d scripts, preventing PATH overrides.

Apply the changes immediately:

``` bash
source /etc/profile.d/Z99-golang.sh
```

For subsequent login sessions, the environment variables will be sourced automatically.

## Verify the installation

Check which Go binary is in your PATH:

``` bash
which go
```

Confirm the installed version:

``` bash
go version
```

Inspect the full environment:

``` bash
go env
```

Verify that `GOROOT` points to `/usr/local/go-1.23.4` and `GOBIN` is empty (defaults to `$GOPATH/bin`).

## Managing multiple Go versions

Install multiple versions by repeating the download and extraction steps with different version numbers:

``` bash
# Download and extract Go 1.22.0
wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
tar xf go1.22.0.linux-amd64.tar.gz -C /tmp
sudo mv /tmp/go /usr/local/go-1.22.0

# Download and extract Go 1.23.4
wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
tar xf go1.23.4.linux-amd64.tar.gz -C /tmp
sudo mv /tmp/go /usr/local/go-1.23.4
```

Create separate profile.d scripts for each version:

``` bash
echo 'export GOROOT=/usr/local/go-1.23.4; export PATH=$GOROOT/bin:$PATH' | sudo tee /etc/profile.d/Z99-go-1.23.4.sh
echo 'export GOROOT=/usr/local/go-1.22.0; export PATH=$GOROOT/bin:$PATH' | sudo tee /etc/profile.d/Z99-go-1.22.0.sh
```

To switch versions, update the active symlink:

``` bash
sudo ln -sf Z99-go-1.23.4.sh /etc/profile.d/Z99-golang.sh
source /etc/profile.d/Z99-golang.sh
go version
```

Alternatively, manually edit `/etc/profile.d/Z99-golang.sh` and source it again.

## Working with Go modules

Go 1.13+ uses module mode by default. Create a workspace structure:

``` bash
mkdir -p ~/go/projects
cd ~/go/projects
go mod init github.com/username/project
```

The `GOPATH` is less critical now, though `~/go` remains the default workspace. Go will create `go.mod` and `go.sum` files to manage dependencies.

For organization across multiple projects, use Go workspaces (1.18+):

``` bash
go work init
go work use ./project1 ./project2
```

This allows testing changes across multiple modules without publishing intermediate versions.

## Non-interactive shell environments

Cron jobs and systemd services don’t source `/etc/profile.d/` by default, so you need to configure them explicitly.

**For systemd services**, set environment variables in the unit file:

``` ini
[Service]
Environment="GOROOT=/usr/local/go-1.23.4"
Environment="PATH=/usr/local/go-1.23.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin"
```

**For cron jobs**, explicitly source the profile in your script:

``` bash
#!/bin/bash
source /etc/profile.d/Z99-golang.sh
go build ./...
```

## Troubleshooting

**Go still points to the old version**: Check your shell’s startup files. Bash reads `~/.bashrc` and zsh reads `~/.zshrc` — ensure no conflicting `PATH` definitions override `/etc/profile.d/`. Verify with:

``` bash
echo $PATH
which go
```

If you see an unexpected path, check shell RC files:

``` bash
grep -n "export GOROOT\|export PATH.*go" ~/.bashrc ~/.zshrc
```

**Permission errors during extraction**: Always extract to a temporary directory first, then move with `sudo`:

``` bash
tar xf go1.23.4.linux-amd64.tar.gz -C /tmp
sudo mv /tmp/go /usr/local/go-1.23.4
```

**Checksum verification fails**: Ensure you downloaded both the archive and checksum file in the same directory. Re-download if the file may be corrupted:

``` bash
rm -f go1.23.4.linux-amd64.tar.gz*
wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz.sha256
sha256sum -c go1.23.4.linux-amd64.tar.gz.sha256
```

**Runtime issues with CGO**: If you’re using cgo (C/C++ bindings), ensure you have the necessary build tools installed:

``` bash
sudo apt install build-essential pkg-config
```
