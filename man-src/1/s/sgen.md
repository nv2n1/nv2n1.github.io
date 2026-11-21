---

title: "sgen(1)"
name: "sgen"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgen/"
description: "sgen – Mono XML Serializer GENerator"
---

<p> sgen &#8211; Mono XML Serializer GENerator</p>
<h2>SYNOPSIS</h2>
<p> <code>sgen [options]</code></p>
<h2>DESCRIPTION</h2>
<p> Generates pre-compilable custom XML serializer classes for specific types.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;assembly[:filename], -a</i></dt>
<dd> Specifies the assembly filename to process.</dd>
<dt><i>&#8211;type[:typefullname], -t</i></dt>
<dd> Explicitly specifies the runtime type to process.</dd>
<dt><i>&#8211;reference:[filename], -r</i></dt>
<dd> Specifies an assembly filename, which is referenced by the target assembly and thus required to process it.</dd>
<dt><i>&#8211;compiler:[options], -c</i></dt>
<dd> Specifies compiler options.</dd>
<dt><i>&#8211;proxytypes, -p</i></dt>
<dd> (Not supported yet.)</dd>
<dt><i>&#8211;debug, -d</i></dt>
<dd> Indicates the compiler to generate debug information.</dd>
<dt><i>&#8211;keep, -k</i></dt>
<dd> Indicates the compiler to keep generated temporary source files.</dd>
<dt><i>&#8211;force, -f</i></dt>
<dd> Indicates the generator to force overwriting existing assembly.</dd>
<dt><i>&#8211;out:[output-directory], -o</i></dt>
<dd> Specifies the output directory for resulting files. By default, it is current directory.</dd>
<dt><i>&#8211;nologo, -n</i></dt>
<dd> Indicates to not print the logo for this tool.</dd>
<dt><i>&#8211;silent, -s</i></dt>
<dd> Indicates the tool to run silently.</dd>
<dt><i>&#8211;verbose, -v</i></dt>
<dd> Indicates the tool to be more verbose on its progress.</dd>
<dt><i>&#8211;help, -?</i></dt>
<dd> Display command line help.</dd></dl>
<h2>FEATURES</h2>
<dl>
<dt>It generates a file which contains a set of classes for custom XML serialization. The resulting classes enable xml serialization faster since it does not have to generate serialization classes dynamically at run time.</dt>
<dd></dd></dl>
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
