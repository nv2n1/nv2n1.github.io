---
title: "enum_sock_type(9)"
name: "enum_sock_type"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_sock_type/"
---

enum_sock_type - Socket types

<h2>Synopsis</h2>

<pre>enum sock_type {
 SOCK_STREAM,
 SOCK_DGRAM,
 SOCK_RAW,
 SOCK_RDM,
 SOCK_SEQPACKET,
 SOCK_DCCP,
 SOCK_PACKET
}; </pre>

<h2>Constants</h2>

SOCK_STREAM
<dl><dd>stream (connection) socket</dl>
 

 SOCK_DGRAM
<dl><dd>datagram (conn.less) socket</dl>
 

 SOCK_RAW
<dl><dd>raw socket</dl>
 

 SOCK_RDM
<dl><dd>reliably-delivered message</dl>
 

 SOCK_SEQPACKET
<dl><dd>sequential packet socket</dl>
 

 SOCK_DCCP
<dl><dd>Datagram Congestion Control Protocol socket</dl>
 

 SOCK_PACKET
<dl><dd>linux specific way of getting packets at the dev level. For writing rarp and other similar things on the user level.</dl>

<h2>Description</h2>

When adding some new socket type please grep ARCH_HAS_SOCKET_TYPE include/asm-* /socket.h, at least MIPS overrides this enum for binary compat reasons.

<h2>Copyright</h2>


