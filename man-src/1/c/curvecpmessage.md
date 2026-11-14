---
title: "curvecpmessage(1)"
name: "curvecpmessage"
section: "1"
letter: "c"
url: "/docs/linux/man/1-curvecpmessage/"
description: "CurveCP — Message-handling programs"
---

<h2>NAME</h2>
<p> CurveCP &#8212; Message-handling programs</p>
<h2>SYNOPSIS</h2>
<p> <code>curvecpmessage</code> [<code>-q </code><i>(optional)</i>] [<code>-Q </code><i>(optional)</i>] [<code>-v </code><i>(optional)</i>] [<code>-c </code><i>(optional)</i>] [<code>-C </code><i>(optional)</i>] [<code>-s </code><i>(optional)</i>] [prog]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>CurveCP</code> commands. </p>
<p> A traditional UNIX-style server such as ftpd handles just one network connection, reading input from stdin and writing output to stdout. A &quot;superserver&quot; such as inetd or tcpserver listens for network connections and starts a separate server process for each connection. </p>
<p> The <code>CurveCP</code> command-line tools have an extra level of modularity. The <code>curvecpserver</code> superserver listens for network connections. For each connection, <code>curvecpserver</code> starts the <code>curvecpmessage</code> message handler; <code>curvecpmessage</code> then starts a server such as ftpd. Then ftpd sends a stream of data to <code>curvecpmessage</code>, which in turn sends messages to <code>curvecpserver</code>, which encrypts and authenticates the messages and sends them inside network packets. At the same time <code>curvecpclient</code> receives network packets, verifies and decrypts messages inside the packets, and passes the messages to <code>curvecpmessage</code>; <code>curvecpmessage</code> sends a stream of data to ftpd. The same curvecpmessage tool is also used by <code>curvecpclient</code>. </p>
<p> <code>curvecpserver</code> and <code>curvecpclient</code> can use programs other than <code>curvecpmessage</code>. Those programs can directly generate messages in the CurveCP message format without talking to separate tools such as ftpd; or they can support a completely different protocol that reuses CurveCP&#8217;s cryptographic layer but transmits different kinds of messages.</p>
<h2>OPTIONS</h2>
<p> How to use <code>curvecpmessage</code>:</p>
<dl>
<dt><code>-q</code> <code>optional</code></p>
<dd> no error messages</p>
<dt><code>-Q</code> <code>optional</code></p>
<dd> print error messages (default)</p>
<dt><code>-v</code> <code>optional</code></p>
<dd> print extra information</p>
<dt><code>-c</code> <code>optional</code></p>
<dd> program is a client; server starts first</p>
<dt><code>-C</code> <code>optional</code></p>
<dd> program is a client that starts first</p>
<dt><code>-s</code> <code>optional</code></p>
<dd> program is a server (default)</p>
<dt><code>prog</code></p>
<dd> run this server</dl>
<h2>SEE ALSO</h2>
<p> curvecpserver (1), curvecpclient (1), inetd (8), tcpserver (1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sergiusz Pawlowicz debian [at] pawlowicz.name for the <code>Debian</code> system (and may be used by others). The source of this page is a webpage <a rel="nofollow" href="http://curvecp.org/messageapi.html">http://curvecp.org/messageapi.html</a> . Permission is granted to copy, distribute and/or modify this document under public domain.<br />
&nbsp;<wbr> </p>
<p> This manual page was rewritten for the <code>Debian</code> distribution because the original program does not have a manual page. </p>
<h2>Index</h2>
