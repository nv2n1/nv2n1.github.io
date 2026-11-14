---
title: "xml2ag(1)"
name: "xml2ag"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2ag/"
description: "xml2ag – XML to AutoGen Definiton Converter"
---

<h2 class="name">NAME</h2>
<p> xml2ag &#8211; XML to AutoGen Definiton Converter </p>
<h2>SYNOPSIS</h2>
<p> <code>xml2ag</code> [<code>&#8211;</code><i>flag</i> [<i>value</i>]]&#8230; [<code>&#8212;</code><i>opt-name</i>[[=| ]<i>value</i>]]&#8230;[ &lt;def-file&gt; ] </p>
<p> This program will convert any arbitrary XML file into equivalent AutoGen definitions, and invoke AutoGen.</p>
<h2>DESCRIPTION</h2>
<p> The template will be derived from either:<br />
 * the <code>&#8211;override-tpl</code> command line option<br />
 * a top level XML attribute named, &quot;template&quot;<br />
 One or the other <code>must</code> be provided, or the program will exit with a failure message. </p>
<p> The &#8220;base-name&#8221; for the output will similarly be either:<br />
 * the <code>&#8211;base-name</code> command line option<br />
 * the base name of the .xml file</p>
<h2>OPTIONS</h2>
<h3>All other options are derived from autogen</h3>
<dl>
<dt><code>-O</code> <i>file</i>, <code>&#8211;output</code>=<i>file</i></p>
<dd> Output file in lieu of AutoGen processing. </p>
<p> By default, the output is handed to an AutoGen for processing. However, you may save the definitions to a file instead.</dl>
<h3>All other options</h3>
<p> These options are <i>mostly</i> just passed throug to <code>autogen</code>. The one exception is <code>&#8211;override-tpl</code> which replaces the default template in the output definitions. It does not get passed through on the command line.</p>
<dl>
<dt><code>-L</code> <i>dir</i>, <code>&#8211;templ-dirs</code>=<i>dir</i></p>
<dd> Search for templates in <i>DIR</i>. This option may appear an unlimited number of times. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-T</code> <i>tpl-file</i>, <code>&#8211;override-tpl</code>=<i>tpl-file</i></p>
<dd> Use <i>TPL-FILE</i> for the template. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-l</code> <i>tpl-file</i>, <code>&#8211;lib-template</code>=<i>tpl-file</i></p>
<dd> Load AutoGen macros from <i>TPL-FILE</i>. This option may appear an unlimited number of times. </p>
<p> Pass-through AutoGen argument </p>
<p> <code>NOTE: THIS OPTION IS DEPRECATED</code></p>
<dt><code>&#8211;definitions</code>=<i>file</i></p>
<dd> Read definitions from <i>FILE</i>. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;shell</code>=<i>shell</i></p>
<dd> name or path name of shell to use. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-m</code>, <code>&#8211;no-fmemopen</code></p>
<dd> Do not use in-mem streams. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;equate</code>=<i>char-list</i></p>
<dd> characters considered equivalent. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-b</code> <i>name</i>, <code>&#8211;base-name</code>=<i>name</i></p>
<dd> Specify <code>NAME</code> as the base name for output. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;source-time</code></p>
<dd> set mod times to latest source. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;writable,</code> <code>&#8211;not-writable</code></p>
<dd> Allow output files to be writable. The <i>not-writable</i> form will disable the option. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;loop-limit</code>=<i>lim</i></p>
<dd> Limit on increment loops. This option takes an integer number as its argument. The value of <i>lim</i> is constrained to being: </p>
<pre>
exactly -1, or
in the range  1 through 0x1000000
</pre>
<p> The default <i>lim</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>256 </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-t</code> <i>seconds</i>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> Limit server shell operations to <code>SECONDS</code>. This option takes an integer number as its argument. The value of <i>seconds</i> is constrained to being: </p>
<pre>
in the range  0 through 3600
</pre>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;trace</code>=<i>level</i></p>
<dd> tracing level of detail. This option takes a keyword as its argument. The argument sets an enumeration value that can be tested by comparing them against the option value macro. The available keywords are: </p>
<pre>
nothing       debug-message server-shell
templates     block-macros  expressions
everything
</pre>
<p> or their numeric equivalent. </p>
<p> The default <i>level</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>nothing </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;trace-out</code>=<i>file</i></p>
<dd> tracing output file or filter. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;show-defs</code></p>
<dd> Show the definition tree. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>&#8211;used-defines</code></p>
<dd> Show the definitions used. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-C</code>, <code>&#8211;core</code></p>
<dd> Leave a core dump on a failure exit. </p>
<p> Many systems default to a zero sized core limit. If the system has the sys/resource.h header and if this option is supplied, then in the failure exit path, autogen will attempt to set the soft core limit to whatever the hard core limit is. If that does not work, then an administrator must raise the hard core size limit.</p>
<dt><code>-s</code> <i>suffix</i>, <code>&#8211;skip-suffix</code>=<i>suffix</i></p>
<dd> Skip the file with this <i>SUFFIX</i>. This option may appear an unlimited number of times. This option must not appear in combination with any of the following options: select-suffix. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-o</code> <i>suffix</i>, <code>&#8211;select-suffix</code>=<i>suffix</i></p>
<dd> specify this output suffix. This option may appear an unlimited number of times. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-D</code> <i>value</i>, <code>&#8211;define</code>=<i>value</i></p>
<dd> name to add to definition list. This option may appear an unlimited number of times. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-U</code> <i>name-pat</i>, <code>&#8211;undefine</code>=<i>name-pat</i></p>
<dd> definition list removal pattern. This option may appear an unlimited number of times. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-M</code> <i>type</i>, <code>&#8211;make-dep</code>[<code>=</code><i>type</i>]</p>
<dd> emit make dependency file. This option may appear an unlimited number of times. </p>
<p> Pass-through AutoGen argument</p>
<dt><code>-?</code>,<code> &#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-!</code>,<code> &#8211;more-help</code></p>
<dd> Pass the extended usage information through a pager.</p>
<dt><code>-v</code> [{<i>v|c|n</i>}],<code> &#8211;version</code>[={<i>v|c|n</i>}]</p>
<dd> Output version of program and exit. The default mode is `v&#8217;, a simple version. The `c&#8217; mode will print copyright information and `n&#8217; will print the full copyright notice.</dl>
<h2>EXIT STATUS</h2>
<p> One of the following exit values will be returned:</p>
<dl>
<dt><code>0</code> (EXIT_SUCCESS)</p>
<dd> Successful program execution.</p>
<dt><code>1</code> (EXIT_FAILURE)</p>
<dd> The operation failed or the command syntax was not valid.</p>
<dt><code>70</code> (EX_SOFTWARE)</p>
<dd> libopts had an internal operational error. Please report it to autogen-users [at] lists.sourceforge.net. Thank you.</dl>
<h2>AUTHORS</h2>
<p> Bruce Korb</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1992-2013 Bruce Korb all rights reserved. This program is released under the terms of the GNU General Public License, version 3 or later.</p>
<h2>BUGS</h2>
<p> Please send bug reports to: autogen-users [at] lists.sourceforge.net</p>
<h2>NOTES</h2>
<p> This manual page was <i>AutoGen</i>-erated from the <code>xml2ag</code> option definitions. </p>
<h2>Index</h2>
