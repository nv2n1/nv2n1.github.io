---
title: "msgfmt(1)"
name: "msgfmt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgfmt/"
description: "msgfmt – compile message catalog to binary format"
---

<h2 class="name">NAME</h2>
<p> msgfmt &#8211; compile message catalog to binary format </p>
<h2>SYNOPSIS</h2>
<p> <code>msgfmt</code> [<i>OPTION</i>] <i>filename.po </i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Generate binary message catalog from textual translation description. </p>
<p> Mandatory arguments to long options are mandatory for short options too. Similarly for optional arguments.</p>
<h3>Input file location:</h3>
<dl>
<dt>filename.po &#8230;</p>
<dd> input files</p>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></p>
<dd> add DIRECTORY to list for input files search</dl>
<p> If input file is -, standard input is read.</p>
<h3>Operation mode:</h3>
<dl>
<dt><code>-j</code>, <code>&#8211;java</code></p>
<dd> Java mode: generate a Java ResourceBundle class</p>
<dt><code>&#8211;java2</code></p>
<dd> like <code>&#8211;java</code>, and assume Java2 (JDK 1.2 or higher)</p>
<dt><code>&#8211;csharp</code></p>
<dd> C# mode: generate a .NET .dll file</p>
<dt><code>&#8211;csharp-resources</code></p>
<dd> C# resources mode: generate a .NET .resources file</p>
<dt><code>&#8211;tcl</code></p>
<dd> Tcl mode: generate a tcl/msgcat .msg file</p>
<dt><code>&#8211;qt</code></p>
<dd> Qt mode: generate a Qt .qm file</p>
<dt><code>&#8211;desktop</code></p>
<dd> Desktop Entry mode: generate a .desktop file</p>
<dt><code>&#8211;xml</code></p>
<dd> XML mode: generate XML file</dl>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified file</p>
<dt><code>&#8211;strict</code></p>
<dd> enable strict Uniforum mode</dl>
<p> If output file is -, output is written to standard output.</p>
<h3>Output file location in Java mode:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>RESOURCE</i></p>
<dd> resource name</p>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></p>
<dd> locale name, either language or language_COUNTRY</p>
<dt><code>&#8211;source</code></p>
<dd> produce a .java file, instead of a .class file</p>
<dt><code>-d</code> DIRECTORY</p>
<dd> base directory of classes directory hierarchy</dl>
<p> The class name is determined by appending the locale name to the resource name, separated with an underscore. The <code>-d</code> option is mandatory. The class is written under the specified directory.</p>
<h3>Output file location in C# mode:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>RESOURCE</i></p>
<dd> resource name</p>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></p>
<dd> locale name, either language or language_COUNTRY</p>
<dt><code>-d</code> DIRECTORY</p>
<dd> base directory for locale dependent .dll files</dl>
<p> The <code>-l</code> and <code>-d</code> options are mandatory. The .dll file is written in a subdirectory of the specified directory whose name depends on the locale.</p>
<h3>Output file location in Tcl mode:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></p>
<dd> locale name, either language or language_COUNTRY</p>
<dt><code>-d</code> DIRECTORY</p>
<dd> base directory of .msg message catalogs</dl>
<p> The <code>-l</code> and <code>-d</code> options are mandatory. The .msg file is written in the specified directory.</p>
<h3>Desktop Entry mode options:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></p>
<dd> locale name, either language or language_COUNTRY</p>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified file</p>
<dt><code>&#8211;template</code>=<i>TEMPLATE</i></p>
<dd> a .desktop file used as a template</p>
<dt><code>-d</code> DIRECTORY</p>
<dd> base directory of .po files</p>
<dt><code>-kWORD</code>, <code>&#8211;keyword</code>=<i>WORD</i></p>
<dd> look for WORD as an additional keyword</p>
<dt><code>-k</code>, <code>&#8211;keyword</code></p>
<dd> do not to use default keywords</dl>
<p> The <code>-l</code>, <code>-o</code>, and <code>&#8211;template</code> options are mandatory. If <code>-D</code> is specified, input files are read from the directory instead of the command line arguments.</p>
<h3>XML mode options:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></p>
<dd> locale name, either language or language_COUNTRY</p>
<dt><code>-L</code>, <code>&#8211;language</code>=<i>NAME</i></p>
<dd> recognise the specified XML language</p>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></p>
<dd> write output to specified file</p>
<dt><code>&#8211;template</code>=<i>TEMPLATE</i></p>
<dd> an XML file used as a template</p>
<dt><code>-d</code> DIRECTORY</p>
<dd> base directory of .po files</dl>
<p> The <code>-l</code>, <code>-o</code>, and <code>&#8211;template</code> options are mandatory. If <code>-D</code> is specified, input files are read from the directory instead of the command line arguments.</p>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></p>
<dd> input files are in Java .properties syntax</p>
<dt><code>&#8211;stringtable-input</code></p>
<dd> input files are in NeXTstep/GNUstep .strings syntax</dl>
<h3>Input file interpretation:</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> perform all the checks implied by <code>&#8211;check-format</code>, <code>&#8211;check-header</code>, <code>&#8211;check-domain</code></p>
<dt><code>&#8211;check-format</code></p>
<dd> check language dependent format strings</p>
<dt><code>&#8211;check-header</code></p>
<dd> verify presence and contents of the header entry</p>
<dt><code>&#8211;check-domain</code></p>
<dd> check for conflicts between domain directives and the <code>&#8211;output-file</code> option</p>
<dt><code>-C</code>, <code>&#8211;check-compatibility</code></p>
<dd> check that GNU msgfmt behaves like X/Open msgfmt</p>
<dt><code>&#8211;check-accelerators</code>[=<i>CHAR</i>]</p>
<dd> check presence of keyboard accelerators for menu items</p>
<dt><code>-f</code>, <code>&#8211;use-fuzzy</code></p>
<dd> use fuzzy entries in output</dl>
<h3>Output details:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;alignment</code>=<i>NUMBER</i></p>
<dd> align strings to NUMBER bytes (default: 1)</p>
<dt><code>&#8211;endianness</code>=<i>BYTEORDER</i></p>
<dd> write out 32-bit numbers in the given byte order (big or little, default depends on platform)</p>
<dt><code>&#8211;no-hash</code></p>
<dd> binary file will not include the hash table</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>&#8211;statistics</code></p>
<dd> print statistics about translations</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> increase verbosity level</dl>
<h2>AUTHOR</h2>
<p> Written by Ulrich Drepper.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-1998, 2000-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>msgfmt</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgfmt</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info msgfmt</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
