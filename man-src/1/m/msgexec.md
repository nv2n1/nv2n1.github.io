---
title: "msgexec(1)"
name: "msgexec"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgexec/"
description: "msgexec – process translations of message catalog"
---

<h2 class="name">NAME</h2>
<p> msgexec &#8211; process translations of message catalog </p>
<h2>SYNOPSIS</h2>
<p> <code>msgexec</code> [<i>OPTION</i>] <i>COMMAND </i>[<i>COMMAND-OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> Applies a command to all translations of a translation catalog. The COMMAND can be any program that reads a translation from standard input. It is invoked once for each translation. Its output becomes msgexec&#8217;s output. msgexec&#8217;s return code is the maximum return code across all invocations. </p>
<p> A special builtin command called &#8216;0&#8217; outputs the translation, followed by a null byte. The output of &quot;msgexec 0&quot; is suitable as input for &quot;xargs <code>-0</code>&quot;.</p>
<h3>Command input:</h3>
<dl>
<dt><code>&#8211;newline</code></p>
<dd> add newline at the end of input</dl>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<h3>Input file location:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>INPUTFILE</i></p>
<dd> input PO file</p>
<dt><code>-D</code>, <code>&#8211;directory</code>=<i>DIRECTORY</i></p>
<dd> add DIRECTORY to list for input files search</dl>
<p> If no input file is given or if it is -, standard input is read.</p>
<h3>Input file syntax:</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;properties-input</code></p>
<dd> input file is in Java .properties syntax</p>
<dt><code>&#8211;stringtable-input</code></p>
<dd> input file is in NeXTstep/GNUstep .strings syntax</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Bruno Haible.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnu-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>msgexec</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>msgexec</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info msgexec</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
