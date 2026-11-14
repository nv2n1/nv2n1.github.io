---
title: "gtags-parser(1)"
name: "gtags-parser"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtags-parser/"
description: "gtags-parser – print cross reference list for gtags."
---

<h2>NAME</h2>
<p> gtags-parser &#8211; print cross reference list for gtags.</p>
<h2>SYNOPSIS</h2>
<p> <code>gtags-parser</code> [-bdenqrstvw] <i>file</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>Gtags-parser</code> print cross reference list for <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1) from the specified C, C++, yacc, java, PHP and Assembly source to standard output. Each line of output contains the object name, the line number which it appears, the file in which it is defined, and a line image separated by white-space. It&#8217;s same with the output of <code><a href="/docs/linux/man/1-ctags/">ctags</a></code>(1) with <code>-x</code> option. </p>
<p> Depending upon the options provided to <code>gtags-parser</code>, objects will consist of object definitions, object references and other symbols. </p>
<p> Files whose names end in &#8216;.c&#8217; or &#8216;.h&#8217; are assumed to be C source files. Files whose names end in &#8216;.c++&#8217; &#8216;.cc&#8217; &#8216;.cpp&#8217; &#8216;.cxx&#8217; &#8216;.hxx&#8217; &#8216;.hpp&#8217; &#8216;.C&#8217; &#8216;.H&#8217; are assumed to be C++ source files. Files whose names end in &#8216;.y&#8217; are assumed to be YACC source files. Files whose names end in &#8216;.java&#8217; are assumed to be Java source files. Files whose names end in &#8216;.php&#8217; &#8216;.php3&#8217; &#8216;.phtml&#8217; are assumed to be PHP source files. Files whose names end in &#8216;.s&#8217; or &#8216;.S&#8217; are assumed to be Assembly source files. Other files are searched for C style definitions. </p>
<p> Yacc files each have a special tag. <code>yyparse</code> is the start of the second section of the yacc file. </p>
<p> This command is the default parser of GLOBAL source code tag system.</p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>-b</code>, <code>&#8211;begin-block</code></p>
<dd> Force level 1 block to begin when reach the left brace at the first column. (C only)</p>
<dt><code>-e</code>, <code>&#8211;end-block</code></p>
<dd> Force level 1 block to end when reach the right brace at the first column. (C only)</p>
<dt><code>-n</code>, <code>&#8211;no-tags</code></p>
<dd> Suppress output of tags. It is useful to use with <code>-w</code> option.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Quiet mode.</p>
<dt><code>-r</code>, <code>&#8211;reference</code></p>
<dd> Locate object references instead of object definitions. &#8216;GTAGS&#8217; is needed at the current directory. (C, C++ and Java source only) By default, locate object definitions.</p>
<dt><code>-s</code>, <code>&#8211;symbol</code></p>
<dd> Collect symbols other than object definitions and references. By default, locate object definitions.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</p>
<dt><code>-w</code>, <code>&#8211;warning</code></p>
<dd> Print warning message.</p>
<dt><code>&#8211;langmap</code>=map</p>
<dd> Language mapping. Each comma-separated map consists of the language name, a colon, and a list of file extensions. Default mapping is &#8216;c:.c.h,yacc:.y,asm:.s.S,java:.java,cpp:.c++.cc.cpp.cxx.hxx.hpp.C.H,php:.php.php3.phtml&#8217;.</dl>
<p> The <code>-r</code> and <code>-s</code> options override each other; the last one specified determines the method used.</p>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>gtags-parser</code>:</p>
<dl>
<dt><code>GTAGSFORCECPP</code></p>
<dd> If this variable is set, each file whose suffix is &#8216;h&#8217; is treated as a C++ source file.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>Gtags-parser</code> exits with a non 0 value if an error occurred, 0 otherwise. Duplicate objects are not considered errors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-global/">global</a></code>(1), <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1), <code><a href="/docs/linux/man/1-htags/">htags</a></code>(1). </p>
<p> GNU GLOBAL source code tag system<br />
 (<a rel="nofollow" href="http://www.gnu.org/software/global/">http://www.gnu.org/software/global/</a>).</p>
<h2>BUG</h2>
<p> <code>Gtags-parser</code> relies on the input being well formed, and any syntactical errors will completely confuse it.</p>
<h2>AUTHOR</h2>
<p> Tama Communications Corporation.</p>
<h2>HISTORY</h2>
<p> The <code>gtags-parser</code>(gctags) command appeared in FreeBSD 2.2.2. </p>
<h2>Index</h2>
