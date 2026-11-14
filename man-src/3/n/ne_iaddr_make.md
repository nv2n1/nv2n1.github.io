---
title: "ne_iaddr_make(3)"
name: "ne_iaddr_make"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_iaddr_make/"
description: "ne_iaddr_make, ne_iaddr_cmp, ne_iaddr_print, ne_iaddr_typeof, ne_iaddr_parse, ne_iaddr_raw, ne_iaddr_reverse, ne_iaddr_free – functions to manipulate network addresses"
---

<p>ne_iaddr_make, ne_iaddr_cmp, ne_iaddr_print, ne_iaddr_typeof, ne_iaddr_parse, ne_iaddr_raw, ne_iaddr_reverse, ne_iaddr_free &#8211; functions to manipulate network addresses</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_socket.h&gt;

typedef enum {
    ne_iaddr_ipv4 = 0,
    ne_iaddr_ipv6
} ne_iaddr_type;

ne_inet_addr *ne_iaddr_make(ne_iaddr_type type, const unsigned char *raw);

int ne_iaddr_cmp(const ne_inet_addr *ia1, const ne_inet_addr *ia2);

char *ne_iaddr_print(const ne_inet_addr *ia, char *buffer, size_t bufsiz);

ne_iaddr_type ne_iaddr_typeof(const ne_inet_addr *ia);

ne_inet_addr *ne_iaddr_parse(const char *address, ne_iaddr_type type);

unsigned char *ne_iaddr_raw(const ne_inet_addr *ia, unsigned char *buffer);

int ne_iaddr_reverse(const ne_inet_addr *ia, char *buffer, size_t buflen);

void ne_iaddr_free(const ne_inet_addr *ia);</code></pre>
<h2>Description</h2>
<p><code>ne_iaddr_make</code></p>
<dd>creates an <code>ne_inet_addr</code> object from a raw binary network address; for instance the four bytes 0x7f 0x00 0x00 0x01 represent the IPv4 address 127.0.0.1. The object returned is suitable for passing to <code>ne_sock_connect</code>. A binary IPv4 address contains four bytes; a binary IPv6 address contains sixteen bytes; addresses passed must be in network byte order. </p>
<p> <code>ne_iaddr_cmp</code> compares two network address objects; returning zero only if they are identical. The objects need not have the same address type; if the addresses are not of the same type, the return value is guaranteed to be non-zero. </p>
<p> <code>ne_iaddr_print</code> prints a human-readable string representation of a network address into a buffer, for instance the string &quot;127.0.0.1&quot;. </p>
<p> <code>ne_iaddr_typeof</code> returns the type of the given network address object. </p>
<p> <code>ne_iaddr_parse</code> parses a string representation of a network address (such as &quot;127.0.0.1&quot; and creates a network address object to represent the parsed address. </p>
<p> <code>ne_iaddr_raw</code> writes the raw byte representation of a network address to the provided buffer. The bytes are written in network byte order; the buffer must be of suitable length for the type of address (4 bytes for an IPv4 address, 16 bytes for an IPv6 address). </p>
<p> <code>ne_iaddr_reverse</code> performs a reverse name lookup on the address object, writing the (first) hostname associated with the IP address to the provided buffer. If the hostname is longer than the buffer it will be silently truncated; on success the string written to the buffer is always NUL-terminated. </p>
<p> <code>ne_iaddr_free</code> releases the memory associated with a network address object.</p>
<h2>Return Value</h2>
<p><code>ne_iaddr_make</code> returns NULL if the address type passed is not supported (for instance on a platform which does not support IPv6). </p>
<p> <code>ne_iaddr_print</code> returns the <i>buffer</i> pointer, and never NULL. </p>
<p> <code>ne_iaddr_parse</code> returns a network address object on success, or NULL on failure to parse the <i>address</i> parameter. </p>
<p> <code>ne_iaddr_reverse</code> returns zero on success or non-zero if no hostname is associated with the address. </p>
<p> <code>ne_iaddr_raw</code> returns the <i>buffer</i> parameter, and never NULL.</p>
<h2>Examples</h2>
<p>The following example connects a socket to port 80 at the address 127.0.0.1. </p>
<pre><code>unsigned char addr[] = &quot;
