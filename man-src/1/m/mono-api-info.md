---
title: "mono-api-info(1)"
name: "mono-api-info"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mono-api-info/"
description: "mono-api-info – Expose IL structure of CLR assemblies as XML."
---

<h2>NAME</h2>
<p> mono-api-info &#8211; Expose IL structure of CLR assemblies as XML.</p>
<h2>SYNOPSIS</h2>
<p> <code>mono-api-info [&#8211;abi] assembly1.dll assembly2.exe &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> Expose the structure of your CLR assemblies by examining their IL and giving XML output. </p>
<p> By default this tool gives information about just the public API of the assemblies to scan. So it&#8217;s good for comparing API compatibility between versions of libraries.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;abi</i></p>
<dd> Show the ABI instead of the API, that is, non-static fields (even the non-public ones) that are not marked as [NonSerialized()].</dl>
<h2>AUTHOR</h2>
<p> Written by Andrés G. Aragoneses</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 LindenLab. Released under BSD license.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a>(1)</code> </p>
<h2>Index</h2>
