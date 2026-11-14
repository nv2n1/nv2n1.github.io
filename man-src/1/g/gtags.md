---
title: "gtags(1)"
name: "gtags"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtags/"
description: "gtags – create tag files for global."
---

<h2>NAME</h2>
<p> gtags &#8211; create tag files for global.</p>
<h2>SYNOPSIS</h2>
<p> <code>gtags</code> [-ciIOqvw][-f <i>file</i>][-n <i>number</i>][<i>dbpath</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Gtags</code> recursively collect the source files under the current directory, pickup symbols and write the cross-reference data into tag files (&#8216;GTAGS&#8217;, &#8216;GRTAGS&#8217;, &#8216;GSYMS&#8217; and &#8216;GPATH&#8217;). You should execute this command at the root of the source tree. </p>
<p> C, C++, yacc, java, PHP and Assembly source files are supported. Files whose names end in &#8216;.c&#8217; or &#8216;.h&#8217; are assumed to be C source files. Files whose names end in &#8216;.c++&#8217; &#8216;.cc&#8217; &#8216;.cpp&#8217; &#8216;.cxx&#8217; &#8216;.hxx&#8217; &#8216;.hpp&#8217; &#8216;.C&#8217; &#8216;.H&#8217; are assumed to be C++ source files. Files whose names end in &#8216;.y&#8217; are assumed to be YACC source files. Files whose names end in &#8216;.java&#8217; are assumed to be Java source files. Files whose names end in &#8216;.php&#8217; &#8216;.php3&#8217; &#8216;.phtml&#8217; are assumed to be PHP source files. Files whose names end in &#8216;.s&#8217; or &#8216;.S&#8217; are assumed to be Assembly source files. Other files are assumed to be text files.</p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>-c</code>, <code>&#8211;compact</code></p>
<dd> Make GTAGS in compact format. This option does not influence GRTAGS and GSYMS, because they are always made in compact format.</p>
<dt><code>&#8211;config</code>[=<i>name</i>]</p>
<dd> Show the value of config variable <i>name</i>. If <i>name</i> is not specified then show whole of config entry.</p>
<dt><code>-f</code>, <code>&#8211;file</code> <i>file</i></p>
<dd> Read from <i>file</i> a list of file names which should be considered as the candidate of source files. By default, all files under the current directory are considered as the candidate. If <i>file</i> is &#8216;-&#8216;, read from standard input. File names must be separated by newline.</p>
<dt><code>&#8211;gtagsconf</code> <i>file</i></p>
<dd> Load user&#8217;s configuration from <i>file</i>.</p>
<dt><code>&#8211;gtagslabel</code> <i>label</i></p>
<dd> <i>label</i> is used as the label of configuration file. The default is default.</p>
<dt><code>-I</code>, <code>&#8211;idutils</code></p>
<dd> Make index files for <code><a href="/docs/linux/man/1-idutils/">idutils</a></code>(1) too.</p>
<dt><code>-i</code>, <code>&#8211;incremental</code></p>
<dd> Update tag files incrementally. You had better use <code><a href="/docs/linux/man/1-global/">global</a></code>(1) with the -u option.</p>
<dt><code>-n</code>, <code>&#8211;max-args</code> <i>number</i></p>
<dd> Maximum number of arguments for <code><a href="/docs/linux/man/1-gtags-parser/">gtags-parser</a></code>(1). By default, gtags invokes <code>gtags-parser</code> with arguments as many as possible to decrease the frequency of invoking.</p>
<dt><code>-O</code>, <code>&#8211;objdir</code></p>
<dd> Use objdir as dbpath. If &#8216;$MAKEOBJDIRPREFIX&#8217; directory exists, <code>gtags</code> creates &#8216;$MAKEOBJDIRPREFIX/&lt;current directory&gt;&#8217; directory and makes tag files in it. If <i>dbpath</i> is specified, this options is ignored.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Quiet mode.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</p>
<dt><code>-w</code>, <code>&#8211;warning</code></p>
<dd> Print warning messages.</p>
<dt><i>dbpath</i></p>
<dd> The directory in which tag files are generated. The default is the current directory. It is useful when your source directory is on a read only device like CDROM.</dl>
<h2>EXAMPLES</h2>
<pre>
        $ ls -F
        Makefile      src/    lib/
        $ gtags -v
        $ global -x main
        main              10 src/main.c  main (argc, argv) {
</pre>
<h2>FILES</h2>
<dl>
<dt>&#8216;GTAGS&#8217;</p>
<dd> Tag file for object definitions.</p>
<dt>&#8216;GRTAGS&#8217;</p>
<dd> Tag file for object references.</p>
<dt>&#8216;GSYMS&#8217;</p>
<dd> Tag file for other symbols.</p>
<dt>&#8216;GPATH&#8217;</p>
<dd> Tag file for path of source files.</p>
<dt>&#8216;/etc/gtags.conf&#8217;, &#8216;$HOME/.globalrc&#8217;</p>
<dd> Configuration file.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>gtags</code>:</p>
<dl>
<dt><code>GTAGSCONF</code></p>
<dd> If this variable is set, its value is used as the configuration file. The default is &#8216;$HOME/.globalrc&#8217;.</p>
<dt><code>GTAGSLABEL</code></p>
<dd> If this variable is set, its value is used as the label of configuration file. The default is default.</p>
<dt><code>GTAGSCACHE</code></p>
<dd> If this variable is set, its value is used as the size of B-tree cache. The default is 50000000 (bytes).</p>
<dt><code>GTAGSFORCECPP</code></p>
<dd> If this variable is set, each file whose suffix is &#8216;h&#8217; is treated as a C++ source file.</p>
<dt><code>MAKEOBJDIRPREFIX</code></p>
<dd> If this variable is set, &#8216;$MAKEOBJDIRPREFIX&#8217; is used as an object prefix directory. The default is &#8216;/usr/obj&#8217;.</dl>
<h2>CONFIGURATION</h2>
<p> The following configuration variables affect the execution of <code>gtags</code>. You can see the default value for each variable with the <code>&#8211;config</code> option.</p>
<dl>
<dt>GTAGS(string)</p>
<dd> If this variable is set, its value is used as the command line of the parser for GTAGS. The default is &#8216;gtags-parser %s&#8217;.</p>
<dt>GRTAGS(string)</p>
<dd> If this variable is set, its value is used as the command line of the parser for GRTAGS. The default is &#8216;gtags-parser -r %s&#8217;.</p>
<dt>GSYMS(string)</p>
<dd> If this variable is set, its value is used as the command line of the parser for GSYMS. The default is &#8216;gtags-parser -s %s&#8217;.</p>
<dt>icase_path(boolean)</p>
<dd> Ignore case distinctions in the path. Suffixes check are affected by this capability.</p>
<dt>langmap(comma separated list)</p>
<dd> Language mapping. Each comma-separated map consists of the language name, a colon, and a list of file extensions. Default mapping is &#8216;c:.c.h,yacc:.y,asm:.s.S,java:.java,cpp:.c++.cc.cpp.cxx.hxx.hpp.C.H,php:.php.php3.phtml&#8217;.</p>
<dt>skip(comma separated list)</p>
<dd> <code>Gtags</code> skips files which are listed in this list. As a special exception, <code>gtags</code> collect values from multiple skip variables. If the value ends with &#8216;/&#8217;, it assumed as a directory and <code>gtags</code> skips all files under it. If the value start with &#8216;/&#8217;, it assumed relative path from the root of source directory.</p>
<dt>suffixes(comma separated list)</p>
<dd> Suffixes of target source file. As a special exception, <code>gtags</code> collect values from multiple suffixes variables. This variable is obsoleted. If the langmap variable is defined <code>gtags</code> no longer refers this.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>Gtags</code> exits with a non 0 value if an error occurred, 0 otherwise.</p>
<h2>MESSAGE FORMAT</h2>
<p> Verbose message has important level. The most important level is 0, the second is 1 and so on. All the message has level numbers leading blanks.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtags-parser/">gtags-parser</a></code>(1), <code><a href="/docs/linux/man/1-global/">global</a></code>(1), <code><a href="/docs/linux/man/1-htags/">htags</a></code>(1). </p>
<p> GNU GLOBAL source code tag system<br />
 (<a rel="nofollow" href="http://www.gnu.org/software/global/">http://www.gnu.org/software/global/</a>).</p>
<h2>BUG</h2>
<p> &#8216;GTAGS&#8217;, &#8216;GRTAGS&#8217; and &#8216;GSYMS&#8217; are very large. In advance of using this command, check the space of your disk. </p>
<p> Assembly support is far from complete. It extracts only ENTRY() and ALTENTRY() from source file. Probably valid only for FreeBSD and Linux kernel source. </p>
<p> There is no concurrency control about tag files.</p>
<h2>AUTHOR</h2>
<p> Tama Communications Corporation.</p>
<h2>HISTORY</h2>
<p> The <code>gtags</code> command appeared in FreeBSD 2.2.2. </p>
<h2>Index</h2>
