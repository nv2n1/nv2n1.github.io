---

title: "msgfmt(1)"
name: "msgfmt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgfmt/"
description: "msgfmt – compile message catalog to binary format"
---

<p> <code>msgfmt</code> [<i>OPTION</i>] <i>filename.po </i>&#8230;</p>
<p> Generate binary message catalog from textual translation description. </p>
<p> Mandatory arguments to long options are mandatory for short options too. Similarly for optional arguments.</p>
<h3>Input file location:</h3>
<dl>
<dt>filename.po &#8230;</dt>
<dd> input files</dd>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></dt>
<dd> add DIRECTORY to list for input files search</dd></dl>
<p> If input file is -, standard input is read.</p>
<h3>Operation mode:</h3>
<dl>
<dt><code>-j</code>, <code>&#8211;java</code></dt>
<dd> Java mode: generate a Java ResourceBundle class</dd>
<dt><code>&#8211;java2</code></dt>
<dd> like <code>&#8211;java</code>, and assume Java2 (JDK 1.2 or higher)</dd>
<dt><code>&#8211;csharp</code></dt>
<dd> C# mode: generate a .NET .dll file</dd>
<dt><code>&#8211;csharp-resources</code></dt>
<dd> C# resources mode: generate a .NET .resources file</dd>
<dt><code>&#8211;tcl</code></dt>
<dd> Tcl mode: generate a tcl/msgcat .msg file</dd>
<dt><code>&#8211;qt</code></dt>
<dd> Qt mode: generate a Qt .qm file</dd>
<dt><code>&#8211;desktop</code></dt>
<dd> Desktop Entry mode: generate a .desktop file</dd>
<dt><code>&#8211;xml</code></dt>
<dd> XML mode: generate XML file</dd></dl>
<h3>Output file location:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified file</dd>
<dt><code>&#8211;strict</code></dt>
<dd> enable strict Uniforum mode</dd></dl>
<p> If output file is -, output is written to standard output.</p>
<h3>Output file location in Java mode:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>RESOURCE</i></dt>
<dd> resource name</dd>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd>
<dt><code>&#8211;source</code></dt>
<dd> produce a .java file, instead of a .class file</dd>
<dt><code>-d</code> DIRECTORY</dt>
<dd> base directory of classes directory hierarchy</dd></dl>
<p> The class name is determined by appending the locale name to the resource name, separated with an underscore. The <code>-d</code> option is mandatory. The class is written under the specified directory.</p>
<h3>Output file location in C# mode:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>RESOURCE</i></dt>
<dd> resource name</dd>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd>
<dt><code>-d</code> DIRECTORY</dt>
<dd> base directory for locale dependent .dll files</dd></dl>
<p> The <code>-l</code> and <code>-d</code> options are mandatory. The .dll file is written in a subdirectory of the specified directory whose name depends on the locale.</p>
<h3>Output file location in Tcl mode:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd>
<dt><code>-d</code> DIRECTORY</dt>
<dd> base directory of .msg message catalogs</dd></dl>
<p> The <code>-l</code> and <code>-d</code> options are mandatory. The .msg file is written in the specified directory.</p>
<h3>Desktop Entry mode options:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified file</dd>
<dt><code>&#8211;template</code>=<i>TEMPLATE</i></dt>
<dd> a .desktop file used as a template</dd>
<dt><code>-d</code> DIRECTORY</dt>
<dd> base directory of .po files</dd>
<dt><code>-kWORD</code>, <code>&#8211;keyword</code>=<i>WORD</i></dt>
<dd> look for WORD as an additional keyword</dd>
<dt><code>-k</code>, <code>&#8211;keyword</code></dt>
<dd> do not to use default keywords</dd></dl>
<p> The <code>-l</code>, <code>-o</code>, and <code>&#8211;template</code> options are mandatory. If <code>-D</code> is specified, input files are read from the directory instead of the command line arguments.</p>
<h3>XML mode options:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;locale</code>=<i>LOCALE</i></dt>
<dd> locale name, either language or language_COUNTRY</dd>
<dt><code>-L</code>, <code>&#8211;language</code>=<i>NAME</i></dt>
<dd> recognise the specified XML language</dd>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>FILE</i></dt>
<dd> write output to specified file</dd>
<dt><code>&#8211;template</code>=<i>TEMPLATE</i></dt>
<dd> an XML file used as a template</dd>
<dt><code>-d</code> DIRECTORY</dt>
<dd> base directory of .po files</dd></dl>
<p> The <code>-l</code>, <code>-o</code>, and <code>&#8211;template</code> options are mandatory. If <code>-D</code> is specified, input files are read from the directory instead of the command line arguments.</p>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></dt>
<dd> input files are in Java .properties syntax</dd>
<dt><code>&#8211;stringtable-input</code></dt>
<dd> input files are in NeXTstep/GNUstep .strings syntax</dd></dl>
<h3>Input file interpretation:</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;check</code></dt>
<dd> perform all the checks implied by <code>&#8211;check-format</code>, <code>&#8211;check-header</code>, <code>&#8211;check-domain</code></dd>
<dt><code>&#8211;check-format</code></dt>
<dd> check language dependent format strings</dd>
<dt><code>&#8211;check-header</code></dt>
<dd> verify presence and contents of the header entry</dd>
<dt><code>&#8211;check-domain</code></dt>
<dd> check for conflicts between domain directives and the <code>&#8211;output-file</code> option</dd>
<dt><code>-C</code>, <code>&#8211;check-compatibility</code></dt>
<dd> check that GNU msgfmt behaves like X/Open msgfmt</dd>
<dt><code>&#8211;check-accelerators</code>[=<i>CHAR</i>]</dt>
<dd> check presence of keyboard accelerators for menu items</dd>
<dt><code>-f</code>, <code>&#8211;use-fuzzy</code></dt>
<dd> use fuzzy entries in output</dd></dl>
<h3>Output details:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;alignment</code>=<i>NUMBER</i></dt>
<dd> align strings to NUMBER bytes (default: 1)</dd>
<dt><code>&#8211;endianness</code>=<i>BYTEORDER</i></dt>
<dd> write out 32-bit numbers in the given byte order (big or little, default depends on platform)</dd>
<dt><code>&#8211;no-hash</code></dt>
<dd> binary file will not include the hash table</dd></dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>&#8211;statistics</code></dt>
<dd> print statistics about translations</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> increase verbosity level</dd></dl>
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
</dt><dd> <code>info msgfmt</code></dd></dl>
<p> should give you access to the complete manual. </p>
