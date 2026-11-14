---
title: "in-identtestd(8)"
name: "in-identtestd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in-identtestd/"
description: "in.identtestd – a small daemon that can be used to test Ident servers"
---

<p>in.identtestd &#8211; a small daemon that can be used to test Ident servers</p>
<h2>Synopsis</h2>
<p>in.identtestd </p>
<h2>Description</h2>
<p><i>in.identtestd</i> is a small daemon (to be started from inetd) that does an ident lookup on you if you telnet into it. Can be used to verify that your Ident server is working correctly. The source code can be found in the <i>libident</i> source tarball, as <code>ident-tester.c</code>. </p>
<h2>Example</h2>
<p>A typical entry in /etc/inetd.conf would be: </p>
<pre>9999 stream tcp nowait root /usr/sbin/in.identtestd in.identtestd</pre>
<p>With the above entry in place and active, execute &quot;telnet hostname 9999&quot; from either this system, or another system. It should show something like: </p>
<pre>Trying hostname...
Connected to hostname.
Escape character is '^]'.
Welcome to the IDENT server tester, version 2.0
(Linked with libident 0.30)
Connecting to Ident server at 192.168.1.1...
Querying for lport 1109, fport 9999....
Reading response data...
Userid response is:
 Lport........ 1109
 Fport........ 9999
 Opsys........ UNIX
 Charset...... &lt;not specified&gt;
 Identifier... paul
Connection closed by foreign host.</pre>
<h2>Author</h2>
<p>Peter Eriksson &lt;pen [at] lysator.liu.se&gt;<br />
 Manpage written for Debian by Paul Slootman &lt;paul [at] debian.org&gt;.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/3-ident/">ident</a></i>(3), <i><a href="/docs/linux/man/8-identd/">identd</a></i>(8), <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8) </p>
