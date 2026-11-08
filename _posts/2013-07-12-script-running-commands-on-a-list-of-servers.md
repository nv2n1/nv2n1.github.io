---
title: "Running Commands Across Multiple Servers with Bash and Ansible"
date: 2013-07-12 16:32:35 +0000
modified: 2026-04-11 16:41:36 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /script-running-commands-on-a-list-of-servers/
---

Running the same command across dozens of servers is a routine task in infrastructure work. Whether you’re checking disk usage, deploying updates, or gathering system metrics, doing this manually wastes time and introduces errors. The straightforward approach: iterate through a list of hosts and execute commands via SSH on each one.

## Basic Shell Loop Approach

The simplest method uses a bash loop with SSH:

``` bash
#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <hostfile> <command>"
    echo "Example: $0 hosts.txt 'df -h'"
    exit 1
fi

hostfile="$1"
cmd="$2"

if [[ ! -f "$hostfile" ]]; then
    echo "Error: Host file '$hostfile' not found"
    exit 1
fi

while IFS= read -r host || [[ -n "$host" ]]; do
    # Skip empty lines and comments
    [[ -z "$host" || "$host" =~ ^[[:space:]]*# ]] && continue

    echo "=== $host ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=accept-new "$host" "$cmd"
    echo ""
done < "$hostfile"
```

Save this as `batch-cmd.sh` and make it executable:

``` bash
chmod +x batch-cmd.sh
```

Usage examples:

``` bash
./batch-cmd.sh hosts.txt "uname -a"
./batch-cmd.sh hosts.txt "systemctl status nginx"
./batch-cmd.sh hosts.txt "free -h"
```

Your `hosts.txt` file should contain one hostname or IP per line:

    192.168.1.10
    192.168.1.11
    app-server-01
    db-server-01

Comments and blank lines are automatically skipped.

## Setting Up Passwordless SSH

This script assumes passwordless SSH to each host. Use Ed25519 keys (modern, fast, and secure):

``` bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
ssh-copy-id -i ~/.ssh/id_ed25519 user@hostname
```

For specific SSH keys or non-standard ports, modify the SSH command:

``` bash
ssh -i ~/.ssh/custom_key -p 2222 -o ConnectTimeout=5 "$host" "$cmd"
```

## Handling Complex Commands

Commands with pipes, redirects, or multiple statements need proper quoting so they’re sent as a single string to the remote shell:

``` bash
./batch-cmd.sh hosts.txt "ps aux | grep nginx"
./batch-cmd.sh hosts.txt "tail -n 20 /var/log/syslog | grep error"
./batch-cmd.sh hosts.txt "df -h / && free -h"
./batch-cmd.sh hosts.txt "journalctl -u nginx -n 50 --no-pager"
```

For commands requiring elevated privileges, configure passwordless sudo on remote hosts or include sudo in the command:

``` bash
./batch-cmd.sh hosts.txt "sudo systemctl restart nginx"
./batch-cmd.sh hosts.txt "sudo apt update && apt list --upgradable"
```

## Parallel Execution with GNU Parallel

Serial execution slows you down with large deployments. Use `gnu-parallel` to run commands concurrently:

``` bash
#!/bin/bash

hostfile="$1"
cmd="$2"
jobs=${3:-4}

cat "$hostfile" | grep -v '^\s*#' | grep -v '^\s*$' | \
    parallel -j "$jobs" "ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=accept-new {} '$cmd'"
```

This runs 4 commands concurrently (adjust `-j` as needed). For 20 servers, serial execution might take 100 seconds; parallel execution with `-j 5` could finish in 20 seconds.

Install gnu-parallel:

``` bash
# Ubuntu/Debian
sudo apt install parallel

# RHEL/CentOS/Fedora
sudo dnf install parallel

# macOS
brew install parallel
```

## Error Handling and Tracking Failed Hosts

Capture exit codes and identify which hosts failed:

``` bash
#!/bin/bash

hostfile="$1"
cmd="$2"
failed=()
successful=()

while IFS= read -r host || [[ -n "$host" ]]; do
    [[ -z "$host" || "$host" =~ ^[[:space:]]*# ]] && continue

    echo "=== $host ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=accept-new "$host" "$cmd"

    if [[ $? -eq 0 ]]; then
        successful+=("$host")
    else
        failed+=("$host")
    fi
done < "$hostfile"

echo ""
echo "Successful: ${#successful[@]} hosts"
echo "Failed: ${#failed[@]} hosts"

if [[ ${#failed[@]} -gt 0 ]]; then
    echo "Failed hosts: ${failed[*]}"
    exit 1
fi
```

## Parallel Execution with Job Logging

Combine parallelism with error tracking and output capture:

``` bash
#!/bin/bash

hostfile="$1"
cmd="$2"
jobs=${3:-4}
tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT

cat "$hostfile" | grep -v '^\s*#' | grep -v '^\s*$' | \
    parallel -j "$jobs" --joblog "$tmpdir/joblog" \
    "ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=accept-new {} '$cmd' > $tmpdir/{}.out 2>&1"

echo "Results saved to $tmpdir/"
echo ""
echo "Failed hosts:"
cat "$tmpdir/joblog" | awk 'NR>1 && $7!=0 {print $2}'
```

Each host’s output is saved to `$tmpdir/hostname.out` for later review.

## SSH Options for Reliable Automation

Combine these SSH options to handle automation safely:

``` bash
ssh \
    -q \
    -o ConnectTimeout=5 \
    -o StrictHostKeyChecking=accept-new \
    -o BatchMode=yes \
    -o UserKnownHostsFile=/dev/null \
    "$host" "$cmd"
```

Option breakdown:

- `ConnectTimeout=5`: Fail fast if a host is unreachable
- `StrictHostKeyChecking=accept-new`: Add new hosts to `known_hosts` automatically (requires OpenSSH 7.6+)
- `BatchMode=yes`: Disable interactive authentication; fail immediately if key authentication doesn’t work
- `-q`: Suppress SSH banners and non-error output
- `UserKnownHostsFile=/dev/null`: Skip `known_hosts` checking (use cautiously in trusted environments)

## SSH Connection Pooling

For frequent commands on the same hosts, enable SSH ControlMaster to reuse connections:

``` bash
ssh -o ControlMaster=auto -o ControlPath=~/.ssh/control-%h-%p-%r -o ConnectTimeout=5 "$host" "$cmd"
```

Add this to `~/.ssh/config` to make it permanent:

    Host *
        ControlMaster auto
        ControlPath ~/.ssh/control-%h-%p-%r
        ControlPersist 600

This reduces connection overhead significantly when running multiple commands per host.

## When to Use Ansible Instead

For anything beyond simple ad-hoc commands, use Ansible. It’s better for:

- Complex multi-step deployments
- Conditional logic and templating
- Idempotent operations
- Role-based configuration management
- Large inventories (100+ hosts)

Basic Ansible examples:

``` bash
ansible all -i hosts.txt -a "df -h"
ansible all -i hosts.txt -m shell -a "systemctl status nginx"
ansible webservers -i hosts.txt -m apt -a "name=nginx state=latest"
```

Ansible handles parallelism, error handling, variable substitution, and complex workflows out of the box. Shell scripts excel for quick one-off commands; Ansible is better for anything you’ll run repeatedly or in production environments.

## Choosing Your Approach

For dozens of servers running a single command once: a shell loop is fast to write and understand. For frequent operations or complex workflows: invest in Ansible. For one-time commands on a small number of hosts: a simple loop is perfectly adequate. Parallel execution becomes worthwhile once you exceed 10-15 hosts.
