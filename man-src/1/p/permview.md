---
title: "permview(1)"
name: "permview"
section: "1"
letter: "p"
url: "/docs/linux/man/1-permview/"
description: "permview – Viewer for declarative security permission sets inside assemblies."
---

<h2>NAME</h2>
<p> permview &#8211; Viewer for declarative security permission sets inside assemblies.</p>
<h2>SYNOPSIS</h2>
<p> <code>permview [options] assembly</code></p>
<h2>DESCRIPTION</h2>
<p> This tools allow to list the declarative security attributes present in an assembly. The security attributes are either found on the assembly level, on the classes and the methods. This tool is useful to diagnose why an assembly won&#8217;t load or why some class/method throws SecurityException.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-output filename</i></p>
<dd> Output all declarative security attributes related informations into the specified file.</p>
<dt><i>-xml | &#8211;xml | /XML</i></p>
<dd> Output all declarative security attributes in an XML format.</p>
<dt><i>-decl | &#8211;decl | /DECL</i></p>
<dd> Show declarative security attributes on classes and methods. The default, without the <code>-decl</code> option, is to show only the assembly level permission sets.</p>
<dt><i>-? | /? | -h[elp] | /h[elp]</i></p>
<dd> Display help informations about the permview tool. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><i>permview mscorlib.dll</i></p>
<dd> This will show the minimum, optional and refused permissions sets (i.e. the assembly level security actions) that are compiled inside the mscorlib assembly.</p>
<dt><i>permview -decl permview.exe</i></p>
<dd> This will show all (assembly, class or method level) declarative security attributes present in the permview.exe assembly. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2004-2005 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
