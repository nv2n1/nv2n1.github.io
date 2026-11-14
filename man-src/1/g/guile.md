---
title: "guile(1)"
name: "guile"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guile/"
description: "guile – The GNU Project Extension Language"
---

<h2>NAME</h2>
<p> guile &#8211; The GNU Project Extension Language</p>
<h2>SYNOPSIS</h2>
<p> <code>guile</code> [<code>-L</code> <i>DIRECTORY</i>] [<code>-l</code> <i>FILE</i>] [<code>-e</code> <i>FUNCTION</i>] [<code>\</code>] [<code>-c</code> <i>EXPR</i>] [<code>-s</code> <i>SCRIPT</i>] [<code>&#8212;</code>] [<i>SCRIPT</i> [<i>ARGs for SCRIPT</i>]] </p>
<p> Only the most useful options are listed here; see below for the remainder.</p>
<h2>DESCRIPTION</h2>
<p> GNU Guile is an implementation of the Scheme programming language. It extends the R5RS and R6RS language standards, providing additional features necessary for real-world use. </p>
<p> Guile works well for interactive use, basic scripting, and extension of larger applications, as well as for stand-alone Scheme application development. </p>
<p> The <code>guile</code> executable itself provides a stand-alone interactive compiler and run-time for Scheme programs, both for interactive use and for executing Scheme scripts or programs. </p>
<p> This manual page provides only brief instruction in invoking <code>guile</code> from the command line. Please consult the Guile info documentation for more information, (type <code> info &quot;(guile)Invoking Guile&quot;</code> at a command prompt).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-L</code><i>&nbsp;<wbr>DIRECTORY</i></p>
<dd> Add <i>DIRECTORY</i> to the front of Guile&#8217;s module load path.</p>
<dt><code>-l</code><i>&nbsp;<wbr>FILE</i></p>
<dd> Load Scheme source code from <i>FILE</i>.</p>
<dt><code>-e</code><i>&nbsp;<wbr>FUNCTION</i></p>
<dd> After reading <i>SCRIPT</i>, apply <i>FUNCTION</i> to command-line arguments. Note that <i>FUNCTION</i> is evaluated, so, for example, <code>(@ (my-module) my-proc)</code> is valid here.</p>
<dt><code>\</code></p>
<dd> The &quot;meta switch&quot;, used to work around limitations in #! scripts. See &quot;The Meta Switch&quot; in the texinfo documentation for more details.</p>
<dt><code>&#8212;</code></p>
<dd> Stop argument processing, and start <code>guile</code> in interactive mode.</p>
<dt><code>-c</code><i>&nbsp;<wbr>EXPR</i></p>
<dd> Stop argument processing, and evaluate <i>EXPR</i> as a Scheme expression.</p>
<dt><code>-s</code><i>&nbsp;<wbr>SCRIPT-FILE</i></p>
<dd> Load Scheme source from <i>SCRIPT-FILE</i> and execute as a script. Note that in many cases it is not necessary to use <code>-s</code>; one may invoke <code>guile</code> simply as <code>guile</code> <i>SCRIPT-FILE ARG&#8230;</i></p>
<dt><code>-ds</code></p>
<dd> Carry out <code>-s </code><i>SCRIPT</i> at this point in the option sequence. Note that this argument must be used in conjunction with <code>-s</code>.</p>
<dt><code>&#8211;debug</code></p>
<dd> Start <code>guile</code> with the debugging VM. By default, debugging is on when <code>guile</code> is invoked interactively; it is off otherwise.</p>
<dt><code>&#8211;no-debug</code></p>
<dd> Start <code>guile</code> without the debugging VM, even if <code>guile</code> is being run interactively.</p>
<dt><code>&#8211;auto-compile</code></p>
<dd> Compile source files automatically (default behavior).</p>
<dt><code>&#8211;no-autocompile</code></p>
<dd> Disable automatic source file compilation.</p>
<dt><code>&#8211;listen</code>[=<i>P</i>]</p>
<dd> Listen on a port or socket for remote REPL connections. See the manual for more details.</p>
<dt><code>&#8211;use-srfi</code>=<i>N,M</i>&#8230;</p>
<dd> Load SRFI extensions <i>N</i>, <i>M</i>, etc. For example, <code> &#8211;use-srfi</code>=<i>8,13</i>.</p>
<dt><code>-x</code><i>&nbsp;<wbr>EXTENSION</i></p>
<dd> Add <i>EXTENSION</i> to the <code>guile</code> load extension list.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Describe command-line options and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display guile version and exit.</p>
<dt><code>-q</code></p>
<dd> In interactive mode, suppress loading the user&#8217;s initialization file, <i>~/.guile.</i></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GUILE_LOAD_PATH</code></p>
<dd> If $<code>GUILE_LOAD_PATH</code> is set before <code>guile</code> is started, its value is used to augment the path to search for Scheme files when loading. It should be a colon-separated list of directories, which will be prefixed to the default <code>%load-path.</code></p>
<dt><code>GUILE_LOAD_COMPILED_PATH</code></p>
<dd> If $<code>GUILE_LOAD_COMPILED_PATH</code> is set before <code>guile</code> is started, its value is used to augment the path to search for compiled Scheme files (.go files) when loading. It should be a colon-separated list of directories, which will be prefixed to the default <code>%load-compiled-path.</code></dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.guile</i></p>
<dd> A Guile script that is executed before any other processing occurs. For example, the following <i>.guile</i> activates guile&#8217;s readline interface: </p>
<dl>
<dt>
<dd> <code>(use-modules (ice-9 readline))</code></p>
<dl>
<dt>
<dd> <code>(activate-readline)</code></dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for Guile is maintained as a Texinfo manual. If the <code>info</code> and <code>guile</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info guile</code></dl>
<p> should give you access to the complete manual. </p>
<p> <a rel="nofollow" href="http://www.schemers.org">http://www.schemers.org</a> provides a general introduction to the Scheme language.</p>
<h2>REPORTING BUGS</h2>
<p> There is a mailing list, bug-guile [at] gnu.org, for reporting Guile bugs and fixes. But before reporting something as a bug, please try to be sure that it really is a bug, not a misunderstanding or a deliberate feature. We ask you to read the section &#8220;Reporting Bugs&#8221; in the Guile reference manual (or Info system) for hints on how and when to report bugs. Also, include the version number of the Guile you are running in every bug report that you send in. Bugs tend actually to get fixed if they can be isolated, so it is in your interest to report them in such a way that they can be easily reproduced.</p>
<h2>COPYING</h2>
<p> Copyright (C) 2010, 2011 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this document provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this document under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this document into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Free Software Foundation.</p>
<h2>AUTHORS</h2>
<p> Robert Merkel &lt;rgmerk [at] mira.net&gt; wrote this manpage. Rob Browning &lt;rlb [at] cs.utexas.edu&gt; has added to it. </p>
<p> <code>guile</code> is GNU software. Guile is originally based on Aubrey Jaffer&#8217;s SCM interpreter, and is the work of many individuals. </p>
<h2>Index</h2>
