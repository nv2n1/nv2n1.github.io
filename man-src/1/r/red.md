---
title: "red(1)"
name: "red"
section: "1"
letter: "r"
url: "/docs/linux/man/1-red/"
description: "ed – line-oriented text editor"
---

<h2 class="name">NAME</h2>
<p> ed &#8211; line-oriented text editor </p>
<h2>SYNOPSIS</h2>
<p> <code>ed</code> [<i>,options/</i>] [<i>,file/</i>]</p>
<h2>DESCRIPTION</h2>
<p> GNU ed is a line-oriented text editor. It is used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts. A restricted version of ed, red, can only edit files in the current directory and cannot execute shell commands. Ed is the &#8216;standard&#8217; text editor in the sense that it is the original editor for Unix, and thus widely available. For most purposes, however, it is superseded by full-screen editors such as GNU Emacs or GNU Moe.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-E</code>, <code>&#8211;extended-regexp</code></p>
<dd> use extended regular expressions</p>
<dt><code>-G</code>, <code>&#8211;traditional</code></p>
<dd> run in compatibility mode</p>
<dt><code>-l</code>, <code>&#8211;loose-exit-status</code></p>
<dd> exit with 0 status even if a command fails</p>
<dt><code>-p</code>, <code>&#8211;prompt</code>=<i>,STRING/</i></p>
<dd> use STRING as an interactive prompt</p>
<dt><code>-r</code>, <code>&#8211;restricted</code></p>
<dd> run in restricted mode</p>
<dt><code>-s</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> suppress diagnostics, byte counts and &#8216;!&#8217; prompt</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose; equivalent to the &#8216;H&#8217; command</p>
<dt><code>&#8211;strip-trailing-cr</code></p>
<dd> strip carriage returns at end of text lines</dl>
<p> Start edit by reading in &#8216;file&#8217; if given. If &#8216;file&#8217; begins with a &#8216;!&#8217;, read output of shell command. </p>
<p> Exit status: 0 for a normal exit, 1 for environmental problems (file not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or invalid input file, 3 for an internal consistency error (e.g., bug) which caused ed to panic.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-ed [at] gnu.org<br />
 Ed home page: <a rel="nofollow" href="http://www.gnu.org/software/ed/ed.html">http://www.gnu.org/software/ed/ed.html</a><br />
 General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp">http://www.gnu.org/gethelp</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1994 Andrew L. Moore.<br />
 Copyright &#169; 2022 Antonio Diaz Diaz. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>ed</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>ed</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info ed</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
