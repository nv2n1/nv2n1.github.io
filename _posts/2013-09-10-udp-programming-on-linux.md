---
title: "UDP Socket Programming in C: Building Practical Applications"
date: 2013-09-10 10:24:25 +0000
layout: post
canonical: https://www.systutorials.com/udp-programming-on-linux/
---

UDP (User Datagram Protocol) defined in RFC 768 provides a lightweight alternative to TCP. Unlike TCP’s stream-oriented approach, UDP delivers discrete packets — each `recvfrom()` or `recvmsg()` call returns one complete datagram. The tradeoff is real: you gain speed and lower overhead, but lose automatic reliability guarantees. Your application must handle packet loss, reordering, and out-of-order delivery.

## Basic UDP Socket Implementation

### Socket Creation and Binding

Here’s a working UDP server that binds to a port and receives datagrams:

``` c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    addr.sin_port = htons(5353);

    if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("bind");
        close(sock);
        return 1;
    }

    char buffer[256];
    struct sockaddr_in client;
    socklen_t client_len = sizeof(client);

    ssize_t n = recvfrom(sock, buffer, sizeof(buffer) - 1, 0,
                         (struct sockaddr *)&client, &client_len);
    if (n > 0) {
        buffer[n] = '\0';
        printf("Received from %s:%d: %s\n", 
               inet_ntoa(client.sin_addr), 
               ntohs(client.sin_port), 
               buffer);

        sendto(sock, "ACK", 3, 0,
               (struct sockaddr *)&client, client_len);
    }

    close(sock);
    return 0;
}
```

### Key Differences from TCP

- **No connection phase**: You don’t call `listen()` or `accept()`. Bind directly, then start receiving with `recvfrom()`.
- **Per-packet I/O**: Each datagram is independent and self-contained. Use `recvfrom()` on servers or `recv()` on connected sockets.
- **Size limits**: UDP packets have a practical maximum around 65,507 bytes (accounting for headers). Anything larger gets fragmented or dropped by the network layer.
- **No ordering**: Packets can arrive out of sequence or not at all. Your application must handle this if order matters.

## Handling Real-World Constraints

### Receive Timeouts

Set a receive timeout to avoid blocking indefinitely:

``` c
struct timeval tv;
tv.tv_sec = 2;
tv.tv_usec = 0;
setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
```

After the timeout expires, `recvfrom()` returns -1 with `errno` set to `EAGAIN` or `EWOULDBLOCK`. Check this to implement retry logic or move on.

### Packet Loss and Fragmentation

UDP doesn’t retransmit lost packets automatically. If you need reliability:

- Implement application-level acknowledgments: send an ACK back when data arrives.
- Use retransmission timers on the sender side.
- Keep datagrams small — under 512 bytes for maximum compatibility, under 1,472 bytes on typical Ethernet — to avoid IP-layer fragmentation.

Fragmentation at the IP layer increases packet loss risk significantly. Prefer many small packets over one large one.

### Socket Reuse and Multi-Recipient Scenarios

For broadcast or when restarting a server quickly, enable socket reuse:

``` c
int opt = 1;
setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
```

For multicast scenarios where multiple processes bind to the same port:

``` c
setsockopt(sock, SOL_SOCKET, SO_REUSEPORT, &opt, sizeof(opt));
```

## Using recvmsg() and sendmsg() for Advanced Control

When you need to handle multiple buffers, ancillary data, or gather/scatter I/O, use `recvmsg()` and `sendmsg()`:

``` c
struct iovec iov[2];
iov[0].iov_base = buffer1;
iov[0].iov_len = 128;
iov[1].iov_base = buffer2;
iov[1].iov_len = 128;

struct msghdr msg;
memset(&msg, 0, sizeof(msg));
msg.msg_iov = iov;
msg.msg_iovlen = 2;
msg.msg_name = (struct sockaddr *)&client;
msg.msg_namelen = sizeof(client);

ssize_t n = recvmsg(sock, &msg, 0);
if (n > 0) {
    printf("Received %zd bytes across %d iovecs\n", n, msg.msg_iovlen);
}
```

This approach is useful for protocol implementations where you need to separate headers from payload or collect data from multiple buffers.

## IPv6 Support

Modern applications should support IPv6 alongside IPv4. Use `AF_INET6` with `struct sockaddr_in6`:

``` c
struct sockaddr_in6 addr6;
memset(&addr6, 0, sizeof(addr6));
addr6.sin6_family = AF_INET6;
addr6.sin6_addr = in6addr_any;
addr6.sin6_port = htons(5353);

int sock = socket(AF_INET6, SOCK_DGRAM, 0);
bind(sock, (struct sockaddr *)&addr6, sizeof(addr6));
```

To support both IPv4 and IPv6 on the same port, you can:

- Bind two separate sockets (one IPv4, one IPv6) and use `select()` or `poll()` to multiplex them.
- Use dual-stack sockets by ensuring `IPV6_V6ONLY` is disabled (often the default).

## Testing and Debugging

### netcat

Send a test datagram to your server:

``` bash
echo "test message" | nc -u localhost 5353
```

### socat

More powerful testing with socat:

``` bash
socat - UDP4-DATAGRAM:127.0.0.1:5353
```

### tcpdump

Monitor UDP traffic on a specific port:

``` bash
tcpdump -i lo -nn udp port 5353
```

### strace

Trace system calls to see socket operations:

``` bash
strace -e trace=network ./your_udp_program
```

## When to Use Alternatives

UDP is the right choice for low-latency, connectionless communication. However, consider alternatives if:

- **You need reliability**: Use TCP or implement a custom ACK/retransmission layer in your application.
- **You need congestion control**: TCP handles this automatically; QUIC libraries like `quiche` or `quinn` add it to UDP.
- **You need connection state and ordered delivery**: SCTP with `SOCK_SEQPACKET` offers message boundaries with reliability.
- **Bulk transfers are critical**: TCP’s flow control and congestion algorithms are battle-tested for large volumes.

Most applications should default to TCP. Use UDP only when you have concrete latency constraints, multicast requirements, or connection overhead is a measurable problem.
