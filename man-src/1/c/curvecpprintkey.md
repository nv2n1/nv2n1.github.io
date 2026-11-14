---
title: "curvecpprintkey(1)"
name: "curvecpprintkey"
section: "1"
letter: "c"
url: "/docs/linux/man/1-curvecpprintkey/"
description: "CurveCP — Message-handling programs"
---

<h2>NAME</h2>
<p> CurveCP &#8212; Message-handling programs</p>
<h2>SYNOPSIS</h2>
<p> <code>curvecpmakekey</code> [<code>keydir</code>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>CurveCP</code> commands. </p>
<p> A traditional UNIX-style server such as ftpd handles just one network connection, reading input from stdin and writing output to stdout. A &quot;superserver&quot; such as inetd or tcpserver listens for network connections and starts a separate server process for each connection. </p>
<p> <code>curvecpprintkey</code> prints ascii version of binary keys needed for <code>curvecpclient</code> and <code>curvecpserver</code> and created using <code>curvecpmakekey</code> command before.</p>
<h2>OPTIONS</h2>
<p> How to use <code>curvecpprintkey</code>:</p>
<dl>
<dt><code>keydir</code></p>
<dd> a directory where <code>CurveCP</code> binary keys were created.</dl>
<h2>SEE ALSO</h2>
<p> curvecpserver (1), curvecpclient (1), curvecpmakekey (1), inetd (8), tcpserver (1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sergiusz Pawlowicz debian [at] pawlowicz.name for the <code>Debian</code> system (and may be used by others). The source of this page is a webpage <a rel="nofollow" href="http://curvecp.org/">http://curvecp.org/</a> . Permission is granted to copy, distribute and/or modify this document under public domain.<br />
&nbsp;<wbr> </p>
<p> This manual page was rewritten for the <code>Debian</code> distribution because the original program does not have a manual page. </p>
<h2>Index</h2>
