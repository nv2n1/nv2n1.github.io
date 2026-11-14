---
title: "struct_sock_common(9)"
name: "struct_sock_common"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_sock_common/"
---

struct_sock_common - minimal network layer representation of sockets

<h2>Synopsis</h2>

<pre><code>struct sock_common {
    union {
        unnamed_union
    };
};</code></pre>

<h2>Members</h2>

{unnamed_union}
<dl><dd>anonymous</dl>

<h2>Description</h2>

This is the minimal network layer representation of sockets, the header for struct sock and struct inet_timewait_sock.

<h2>Copyright</h2>


