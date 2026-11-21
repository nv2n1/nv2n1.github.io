---

title: "secutil(1)"
name: "secutil"
section: "1"
letter: "s"
url: "/docs/linux/man/1-secutil/"
description: "secutil – Extract X.509 certificates and strongnames from assemblies."
---

<p> secutil &#8211; Extract X.509 certificates and strongnames from assemblies.</p>
<h2>SYNOPSIS</h2>
<p> <code>secutil [options] filename</code></p>
<h2>DESCRIPTION</h2>
<p> Extract X.509 certificates and strongnames from assemblies in a format that can be easily re-used in source code (C# or VB.NET syntax).</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-s assembly, -strongname assembly</i></dt>
<dd> Display strongname informations about the assembly.</dd>
<dt><i>-x assembly, -x509certificate assembly</i></dt>
<dd> Display the X509 Authenticode certificate for the assembly.</dd>
<dt><i>-a, -array</i></dt>
<dd> Display data in a decimal array (default).</dd>
<dt><i>-v, -vbmode</i></dt>
<dd> Display data in a VisualBasic friendly format.</dd>
<dt><i>-c, -cmode</i></dt>
<dd> Display data in a C/C++/C# friendly format (default).</dd>
<dt><i>-help, -h, -?</i></dt>
<dd> Display help about this tool.</dd></dl>
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
