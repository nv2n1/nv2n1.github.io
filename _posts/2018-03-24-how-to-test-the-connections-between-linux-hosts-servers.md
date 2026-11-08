---
title: "Testing Network Connectivity Between Linux Servers"
date: 2018-03-24 07:43:06 +0000
layout: post
canonical: https://www.systutorials.com/how-to-test-the-connections-between-linux-hosts-servers/
---

When you need to verify that two Linux systems can communicate over a specific protocol and port, you have several solid options. Let’s cover the most practical approaches.

## Using nc (netcat)

The `nc` command remains a reliable choice for quick connectivity tests. It’s widely available and requires no special setup.

### TCP connection test

To listen on a specific TCP port on the destination host:

``` bash
nc -l 1048
```

From the source host, connect to it:

``` bash
nc 10.0.3.48 1048
```

Once connected, you can type text in either direction to verify bidirectional communication. Press Ctrl+C to close the connection.

### UDP connection test

For UDP, add the `-u` flag:

``` bash
# Server
nc -u -l 1048

# Client
nc -u 10.0.3.48 1048
```

### Listening on a specific interface

If the server has multiple interfaces, bind to a specific one:

``` bash
nc -l 10.0.3.48 1048
```

### Timeout for non-interactive testing

For scripted tests, add a timeout so nc doesn’t hang:

``` bash
nc -w 2 10.0.3.48 1048
```

The `-w 2` parameter sets a 2-second inactivity timeout.

## Using telnet

For TCP connections only, `telnet` provides instant feedback:

``` bash
telnet 10.0.3.48 1048
```

If the connection succeeds, you’ll see a blank prompt. If it fails, you’ll get a connection refused or timeout message immediately. Press Ctrl+\] then type `quit` to exit.

## Using /dev/tcp and /dev/udp

Bash has built-in TCP/UDP capabilities without external tools:

``` bash
# TCP test (connects and times out after 3 seconds)
timeout 3 bash -c 'cat < /dev/null > /dev/tcp/10.0.3.48/1048' && echo "Connected" || echo "Failed"

# UDP test
timeout 3 bash -c 'echo "test" > /dev/udp/10.0.3.48/1048' && echo "Sent" || echo "Failed"
```

This approach is useful when nc or telnet aren’t available.

## Finding listening ports

To check which ports have services listening on your current system:

``` bash
# Show all listening ports with process information
ss -tlnp

# Or with netstat (older systems)
netstat -tlnp
```

The flags mean:

- `t` – TCP sockets
- `l` – listening sockets only
- `n` – numeric output (IPs and ports, not names)
- `p` – include process name and PID
- `u` – UDP sockets (add this if you want UDP too)

For example, to see everything listening:

``` bash
ss -tlnup
```

## Checking specific ports on remote hosts

To quickly scan whether multiple ports are open on a remote host, use `nmap`:

``` bash
nmap -p 1048,3306,5432 10.0.3.48
```

For a range of ports:

``` bash
nmap -p 1000-2000 10.0.3.48
```

## Using curl for HTTP/HTTPS services

If you’re testing web service connectivity:

``` bash
# Test HTTP connectivity with response headers
curl -v http://10.0.3.48:8080

# Test HTTPS with certificate validation disabled (for testing only)
curl -v -k https://10.0.3.48:8443
```

## Firewall considerations

If connections fail, check your firewall rules. On the destination host:

``` bash
# Check if UFW is blocking the port
sudo ufw status

# Temporarily allow traffic for testing
sudo ufw allow 1048/tcp
sudo ufw allow 1048/udp

# Remove the rule afterward
sudo ufw delete allow 1048/tcp
```

For `firewalld`:

``` bash
# Add port temporarily
sudo firewall-cmd --add-port=1048/tcp --zone=public --temporary

# Check open ports
sudo firewall-cmd --list-ports
```

## Real-world testing workflow

1.  Ensure the service is actually listening: `ss -tlnp | grep 1048`
2.  Test locally on the destination: `nc -l 1048` and `nc localhost 1048` from another terminal
3.  Test from the source host to the destination: `nc 10.0.3.48 1048`
4.  If it fails, check firewall rules, routing, and SELinux policies
5.  Check application logs if the port is listening but communication fails

Choose the tool based on what’s available in your environment and what you need to verify. For quick one-off tests, nc or telnet work well. For automated testing or when standard tools are missing, the /dev/tcp approach is reliable. For comprehensive port scanning, nmap is the right choice.
