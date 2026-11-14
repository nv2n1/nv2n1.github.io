---
title: "chktrust(1)"
name: "chktrust"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chktrust/"
description: "chktrust – Check the trust of a PE executable."
---

<h2>NAME</h2>
<p> chktrust &#8211; Check the trust of a PE executable.</p>
<h2>SYNOPSIS</h2>
<p> <code>chktrust [options] filename</code></p>
<h2>DESCRIPTION</h2>
<p> Verify if an PE executable (CLR assembly, Win32 EXE or DLL) has a valid Authenticode(r) signature that can be traced back to a trusted certificate authority (CA). This means that</p>
<dl>
<dt>(a) the signature is valid (i.e. file integrity) and,</p>
<dd>
<dt>(b) the code-signing certificate can be chained back to one of the</p>
<dd> certificates in the Trust store.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>-q, -quiet</i></p>
<dd> Quiet mode. Limited display on console.</p>
<dt><i>-v, -verbose</i></p>
<dd> Verbose mode. More details displayed on the console.</p>
<dt><i>-help, -h, -?, /?</i></p>
<dd> Display help about this tool.</dl>
<h2>KNOWN RESTRICTIONS</h2>
<p> chktrust cannot validate Authenticode signatures on CAB files.</p>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003 Motus Technologies. Copyright (C) 2004 Novell. Released under BSD license.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-signcode/">signcode</a>(1),</code><a href="/docs/linux/man/1-makecert/">makecert</a>(1),<code><a href="/docs/linux/man/1-certmgr/">certmgr</a>(1),</code><a href="/docs/linux/man/1-setreg/">setreg</a>(1) </p>
<h2>Index</h2>
