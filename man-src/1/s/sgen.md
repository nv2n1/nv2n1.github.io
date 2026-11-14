---
title: "sgen(1)"
name: "sgen"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgen/"
description: "sgen – Mono XML Serializer GENerator"
---

<h2>NAME</h2>
<p> sgen &#8211; Mono XML Serializer GENerator</p>
<h2>SYNOPSIS</h2>
<p> <code>sgen [options]</code></p>
<h2>DESCRIPTION</h2>
<p> Generates pre-compilable custom XML serializer classes for specific types.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;assembly[:filename], -a</i></p>
<dd> Specifies the assembly filename to process.</p>
<dt><i>&#8211;type[:typefullname], -t</i></p>
<dd> Explicitly specifies the runtime type to process.</p>
<dt><i>&#8211;reference:[filename], -r</i></p>
<dd> Specifies an assembly filename, which is referenced by the target assembly and thus required to process it.</p>
<dt><i>&#8211;compiler:[options], -c</i></p>
<dd> Specifies compiler options.</p>
<dt><i>&#8211;proxytypes, -p</i></p>
<dd> (Not supported yet.)</p>
<dt><i>&#8211;debug, -d</i></p>
<dd> Indicates the compiler to generate debug information.</p>
<dt><i>&#8211;keep, -k</i></p>
<dd> Indicates the compiler to keep generated temporary source files.</p>
<dt><i>&#8211;force, -f</i></p>
<dd> Indicates the generator to force overwriting existing assembly.</p>
<dt><i>&#8211;out:[output-directory], -o</i></p>
<dd> Specifies the output directory for resulting files. By default, it is current directory.</p>
<dt><i>&#8211;nologo, -n</i></p>
<dd> Indicates to not print the logo for this tool.</p>
<dt><i>&#8211;silent, -s</i></p>
<dd> Indicates the tool to run silently.</p>
<dt><i>&#8211;verbose, -v</i></p>
<dd> Indicates the tool to be more verbose on its progress.</p>
<dt><i>&#8211;help, -?</i></p>
<dd> Display command line help.</dl>
<h2>FEATURES</h2>
<dl>
<dt>It generates a file which contains a set of classes for custom XML serialization. The resulting classes enable xml serialization faster since it does not have to generate serialization classes dynamically at run time.</p>
<dd></dl>
<p> Generated classes are supported only after 2.0 profile.</p>
<h2>AUTHOR</h2>
<p> Written by Lluis Sanchez Gual</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006 Novell.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xsd/">xsd</a>(1),<a href="/docs/linux/man/1-wsdl/">wsdl</a>(1),<a href="/docs/linux/man/1-genxs/">genxs</a>(1)</code> </p>
<h2>Index</h2>
