---
title: "ipsec_ikeping(8)"
name: "ipsec_ikeping"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_ikeping/"
description: "ipsec_ikeping – send/receive ISAKMP/IKE echo requests/replies"
---

<p>ipsec_ikeping &#8211; send/receive ISAKMP/IKE echo requests/replies</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>ikeping</i> [&#8211;listen] [&#8211;verbose] [&#8211;wait&nbsp;<wbr><i>time</i>] [&#8211;exchangenum&nbsp;<wbr><i>num</i>] [&#8211;ikeport&nbsp;<wbr><i>localport</i>] [&#8211;ikeaddress&nbsp;<wbr><i>address</i>] [&#8211;inet] [&#8211;inet6] <i>destaddr</i> [<i>/dstport</i>&#8230;]</dl>
<h2>Description</h2>
<p><i>Ikeping</i></p>
<dd>sends and receives ISAKMP/IKE echo request and echo reply packets. These packets are intended for diagnostics purposes, in a manner similar to <code><a href="/docs/linux/man/8-ping/">ping</a></code>(8) does for ICMP echo request/reply packets. </p>
<p> At the time of this writing, the ISAKMP echo request/reply exchange is still an internet-draft (draft-richardson-ipsec-ikeping-00), and is therefore completely non-standard. The Libreswan IKE daemon pluto does implement this draft, so ikeping can be used to test connectivity to an libreswan ipsec server. </p>
<p> <i>Ikeping</i> will bind to the local address given by <code>&#8211;ikeaddress</code> and the port number given by <code>&#8211;ikeport</code> defaulting to the wildcard address and the ISAKMP port 500. An ISAKMP exchange of type 244 (a private use number) is sent to each of the address/ports listed on the command line. The exchange number may be overridden by the <code>&#8211;exchangenum</code> option. </p>
<p> <i>Ikeping</i> then listens for replies, printing them as they are received. Replies are of exchange type 245 or the specified exchange number plus 1. <i>Ikeping</i> will keep listening until it either receives as many echo responses as it sent, or until the timeout period (5 seconds) has been reached. Receipt of a packet will reset the timer. The <code>&#8211;wait</code> option can be used to specify a different timeout period. </p>
<p> If the <code>&#8211;listen</code> option is given, then <i>ikeping</i> will not send any packets. Instead, it will listen for them and reply to each request received. </p>
<p> If the <code>&#8211;natt</code> option is given, then <i>ikeping</i> will set the socket to permit UDP encapsulated ESP packets. This is only useful in listen mode.</p>
<h2>Files</h2>
<p>no external files</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ping/">ping</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Michael Richardson.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
