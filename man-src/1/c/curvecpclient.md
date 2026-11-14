---
title: "curvecpclient(1)"
name: "curvecpclient"
section: "1"
letter: "c"
url: "/docs/linux/man/1-curvecpclient/"
description: "CurveCP — Message-handling programs"
---

<h2>NAME</h2>
<p> CurveCP &#8212; Message-handling programs</p>
<h2>SYNOPSIS</h2>
<p> <code>curvecpclient</code> [<code>-q </code><i>(optional)</i>] [<code>-Q </code><i>(optional)</i>] [<code>-v </code><i>(optional)</i>] [<code>-c keydir</code><i>(optional)</i>] [sname] [pk] [ip] [port] [ext] [prog]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>CurveCP</code> commands. </p>
<p> A traditional UNIX-style server such as ftpd handles just one network connection, reading input from stdin and writing output to stdout. A &quot;superserver&quot; such as inetd or tcpserver listens for network connections and starts a separate server process for each connection. </p>
<p> The <code>CurveCP</code> command-line tools have an extra level of modularity. The <code>curvecpserver</code> superserver listens for network connections. For each connection, <code>curvecpserver</code> starts the <code>curvecpmessage</code> message handler; <code>curvecpmessage</code> then starts a server such as ftpd. Then ftpd sends a stream of data to <code>curvecpmessage</code>, which in turn sends messages to <code>curvecpserver</code>, which encrypts and authenticates the messages and sends them inside network packets. At the same time <code>curvecpclient</code> receives network packets, verifies and decrypts messages inside the packets, and passes the messages to <code>curvecpmessage</code>; <code>curvecpmessage</code> sends a stream of data to ftpd. The same curvecpmessage tool is also used by <code>curvecpclient</code>. </p>
<p> <code>curvecpserver</code> and <code>curvecpclient</code> can use programs other than <code>curvecpmessage</code>. Those programs can directly generate messages in the CurveCP message format without talking to separate tools such as ftpd; or they can support a completely different protocol that reuses CurveCP&#8217;s cryptographic layer but transmits different kinds of messages. </p>
<p> This page explains what programmers have to do to write <code>curvecpmessage</code> replacements that talk to <code>curvecpserver</code> and <code>curvecpclient.</code></p>
<h2>Incoming messagess</h2>
<p> File descriptor 8 is a pipe. Read from this pipe a length byte n, between 1 and 68, and a 16*n-byte message. Repeat. The pipe is set to non-blocking mode; be prepared for EAGAIN and EWOULDBLOCK, even in the middle of a message. </p>
<p> This pipe reading must always be active. The <code>curvecpclient</code> and <code>curvecpserver</code> programs assume that every message is read immediately. If you can&#8217;t handle a message immediately, read it and put it onto a queue. If you don&#8217;t have queue space, throw the message away; this shouldn&#8217;t cause trouble, since you have to be able to handle missing messages in any case.</p>
<h2>Outgoing messagess</h2>
<p> File descriptor 9 is a pipe. Write to this pipe a length byte n, between 1 and 68, and a 16*n-byte message. Repeat. The pipe is set to non-blocking mode; be prepared for EAGAIN and EWOULDBLOCK, even in the middle of a message. </p>
<p> As a client, do not use length bytes above 40 until a message has arrived from the server. (The messages inside CurveCP Initiate packets are limited to 640 bytes.) </p>
<p> The CurveCP server does not start until it has received a message from the client. Furthermore, the CurveCP server must receive this message within 60 seconds of the client starting up. (The CurveCP Initiate packet is valid for only 60 seconds after the corresponding CurveCP Cookie packet.) This does not mean that the client must start sending messages immediately, but it does mean that waiting for more than a second to send a message is a bad idea.</p>
<h2>OPTIONS</h2>
<p> How to use <code>curvecpclient</code>:</p>
<dl>
<dt><code>-q</code> <code>optional</code></p>
<dd> no error messages</p>
<dt><code>-Q</code> <code>optional</code></p>
<dd> print error messages (default)</p>
<dt><code>-v</code> <code>optional</code></p>
<dd> print extra information</p>
<dt><code>-c keydir</code> <code>optional</code></p>
<dd> use this public-key directory</p>
<dt><code>sname</code></p>
<dd> server&#8217;s name</p>
<dt><code>pk</code></p>
<dd> server&#8217;s public key</p>
<dt><code>ip</code></p>
<dd> server&#8217;s IP address</p>
<dt><code>port</code></p>
<dd> server&#8217;s UDP port</p>
<dt><code>ext</code></p>
<dd> server&#8217;s extension</p>
<dt><code>prog</code></p>
<dd> run this client</dl>
<h2>SEE ALSO</h2>
<p> curvecpserver (1), curvecpmessage (1), inetd (8), tcpserver (1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sergiusz Pawlowicz debian [at] pawlowicz.name for the <code>Debian</code> system (and may be used by others). The source of this page is a webpage <a rel="nofollow" href="http://curvecp.org/messageapi.html">http://curvecp.org/messageapi.html</a> . Permission is granted to copy, distribute and/or modify this document under public domain.<br />
&nbsp;<wbr> </p>
<p> This manual page was rewritten for the <code>Debian</code> distribution because the original program does not have a manual page. </p>
<h2>Index</h2>
