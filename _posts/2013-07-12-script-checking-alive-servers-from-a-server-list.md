---
title: "Bash Script for Monitoring Server Uptime"
date: 2013-07-12 16:32:35 +0000
layout: post
canonical: https://www.systutorials.com/script-checking-alive-servers-from-a-server-list/
---

When managing multiple servers, you need reliable ways to verify which hosts are reachable. While orchestration tools like Kubernetes and Ansible handle monitoring at scale, a lightweight Bash script works well for quick spot checks, operational tasks, or smaller deployments.

## Basic ICMP Reachability Check

The simplest approach uses `ping` to test ICMP reachability:

``` bash
ping -W 1 -c 1 "$host" &>/dev/null && echo "up" || echo "down"
```

Breaking down the options:

- `-W 1`: timeout after 1 second
- `-c 1`: send only 1 packet
- `&>/dev/null`: suppress all output
- `&& echo "up" || echo "down"`: use the exit status to determine output

This approach is cleaner than parsing `ping` output, which varies across different systems (Linux, macOS, BSD).

## Sequential Server Check Script

Here’s a production-ready script that processes a host list sequentially:

``` bash
#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "usage: $0 <server-list-file>"
    echo "Each server hostname/IP on a separate line"
    exit 1
fi

if [[ ! -f "$1" ]]; then
    echo "Error: file '$1' not found"
    exit 1
fi

alive_count=0
dead_count=0

while IFS= read -r host || [[ -n "$host" ]]; do
    # Skip empty lines and comments
    [[ -z "$host" || "$host" =~ ^# ]] && continue

    if ping -W 1 -c 1 "$host" &>/dev/null; then
        echo "✓ $host is alive"
        ((alive_count++))
    else
        echo "✗ $host is down"
        ((dead_count++))
    fi
done < "$1"

echo ""
echo "Summary: $alive_count alive, $dead_count down"
```

Save as `check-alive-servers.sh` and make it executable:

``` bash
chmod +x check-alive-servers.sh
```

Create a server list file with one host per line:

    192.168.1.10
    web01.example.com
    db-server
    10.0.0.5
    # commented-out host
    legacy.internal

Run the script:

``` bash
./check-alive-servers.sh server-list.txt
```

Output:

    ✓ 192.168.1.10 is alive
    ✓ web01.example.com is alive
    ✗ db-server is down
    ✓ 10.0.0.5 is alive
    ✓ legacy.internal is alive

    Summary: 4 alive, 1 down

## Parallel Checking for Large Inventories

Sequential pings become slow with large server lists. Use background jobs with controlled concurrency:

``` bash
#!/bin/bash

HOST_FILE="$1"
MAX_JOBS=10
TEMP_DIR=$(mktemp -d)
RESULTS_FILE="$TEMP_DIR/results"

if [[ ! -f "$HOST_FILE" ]]; then
    echo "Error: file '$HOST_FILE' not found"
    exit 1
fi

check_host() {
    local host="$1"
    if ping -W 1 -c 1 "$host" &>/dev/null; then
        echo "✓ $host" >> "$RESULTS_FILE"
    else
        echo "✗ $host" >> "$RESULTS_FILE"
    fi
}

while IFS= read -r host || [[ -n "$host" ]]; do
    [[ -z "$host" || "$host" =~ ^# ]] && continue

    # Wait if we hit the job limit
    while (( $(jobs -r -p | wc -l) >= MAX_JOBS )); do
        sleep 0.05
    done

    check_host "$host" &
done < "$HOST_FILE"

wait

sort "$RESULTS_FILE"
rm -rf "$TEMP_DIR"
```

This version runs up to 10 pings concurrently, dramatically reducing total runtime. The temporary file preserves results across concurrent execution.

Adjust `MAX_JOBS` based on your system’s resources. Values between 10–50 work well for most deployments; higher concurrency can exhaust file descriptors or overwhelm slower network links.

## TCP Port Checks as an Alternative

Some networks block ICMP traffic, making hosts appear unreachable even when they’re running. Test TCP connectivity to a specific port instead:

``` bash
check_tcp() {
    local host="$1"
    local port="${2:-22}"

    if timeout 1 bash -c "echo >/dev/tcp/$host/$port" 2>/dev/null; then
        echo "✓ $host:$port open"
    else
        echo "✗ $host:$port unreachable"
    fi
}

check_tcp web01.example.com 443
check_tcp db-server 5432
check_tcp app-server 8080
```

Common ports to check:

- `22`: SSH
- `80`: HTTP
- `443`: HTTPS
- `3306`: MySQL
- `5432`: PostgreSQL
- `6379`: Redis
- `27017`: MongoDB

This method is more reliable in restrictive network environments where firewalls drop ICMP packets.

## Export Results as JSON

For integration with monitoring systems or log aggregation, export results as JSON:

``` bash
#!/bin/bash

HOST_FILE="$1"

check_host() {
    local host="$1"
    local status="down"

    if ping -W 1 -c 1 "$host" &>/dev/null; then
        status="up"
    fi

    printf '{"host":"%s","status":"%s","timestamp":"%s"}\n' \
        "$host" "$status" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}

while IFS= read -r host || [[ -n "$host" ]]; do
    [[ -z "$host" || "$host" =~ ^# ]] && continue
    check_host "$host"
done < "$HOST_FILE"
```

Pipe results to `jq` for filtering:

``` bash
./check-alive-servers.sh servers.txt | jq 'select(.status=="down")'
```

Or save to a file for later analysis:

``` bash
./check-alive-servers.sh servers.txt > server-status.jsonl
```

## DNS Resolution and Error Handling

The script relies on your system’s DNS resolver via `/etc/resolv.conf`. In air-gapped environments or when custom DNS is required, validate DNS resolution first:

``` bash
resolve_host() {
    local host="$1"
    if getent hosts "$host" &>/dev/null; then
        return 0
    else
        echo "✗ $host (DNS resolution failed)"
        return 1
    fi
}
```

For scripts running in containers or chroot environments, verify `/etc/resolv.conf` is properly mounted or populated. Test with:

``` bash
cat /etc/resolv.conf
nslookup example.com
```

## Performance Characteristics

- **Sequential mode**: ~1 second per host (with 1-second timeout)
- **Parallel mode (10 jobs)**: ~0.1–0.2 seconds per host
- **TCP mode**: Often faster than ICMP on networks with firewall delays

For inventories exceeding 1000 hosts or when you need continuous monitoring, use dedicated monitoring systems like Prometheus with `node_exporter`, Icinga2, or Zabbix. For ad-hoc operational tasks and smaller deployments, these scripts are lightweight, portable, and require no external dependencies.
