---
title: "secutil(1)"
name: "secutil"
section: "1"
letter: "s"
url: "/docs/linux/man/1-secutil/"
description: "secutil – Extract X.509 certificates and strongnames from assemblies."
---

<h2>NAME</h2>
<p> secutil &#8211; Extract X.509 certificates and strongnames from assemblies.</p>
<h2>SYNOPSIS</h2>
<p> <code>secutil [options] filename</code></p>
<h2>DESCRIPTION</h2>
<p> Extract X.509 certificates and strongnames from assemblies in a format that can be easily re-used in source code (C# or VB.NET syntax).</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-s assembly, -strongname assembly</i></p>
<dd> Display strongname informations about the assembly.</p>
<dt><i>-x assembly, -x509certificate assembly</i></p>
<dd> Display the X509 Authenticode certificate for the assembly.</p>
<dt><i>-a, -array</i></p>
<dd> Display data in a decimal array (default).</p>
<dt><i>-v, -vbmode</i></p>
<dd> Display data in a VisualBasic friendly format.</p>
<dt><i>-c, -cmode</i></p>
<dd> Display data in a C/C++/C# friendly format (default).</p>
<dt><i>-help, -h, -?</i></p>
<dd> Display help about this tool.</dl>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002, 2003 Motus Technologies. Released under BSD license.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sn/">sn</a>(1),</code><a href="/docs/linux/man/1-signcode/">signcode</a>(1) </p>
<h2>Index</h2>
