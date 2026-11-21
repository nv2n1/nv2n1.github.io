---
title: "runcon(1)"
name: "runcon"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runcon/"
description: "runcon – run command with specified security context"
---

<h2>SYNOPSIS</h2>
<p> <code>runcon</code> <i>,CONTEXT COMMAND /</i>[<i>,args/</i>]<br />
 <code>runcon</code> [ <i>,-c /</i>] [<i>,-u USER/</i>] [<i>,-r ROLE/</i>] [<i>,-t TYPE/</i>] [<i>,-l RANGE/</i>] <i>,COMMAND /</i>[<i>,args/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Run COMMAND with completely-specified CONTEXT, or with current or transitioned security context modified by one or more of LEVEL, ROLE, TYPE, and USER. </p>
<p> If none of <i>-c</i>, <i>-t</i>, <i>-u</i>, <i>-r</i>, or <i>-l</i>, is specified, the first argument is used as the complete context. Any additional arguments after <i>COMMAND</i> are interpreted as arguments to the command. </p>
<p> Note that only carefully-chosen contexts are likely to successfully run. </p>
<p> Run a program in a different SELinux security context. With neither CONTEXT nor COMMAND, print the current security context. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt>CONTEXT</dt>
<dd> Complete security context</dd>
<dt><code>-c</code>, <code>&#8211;compute</code></dt>
<dd> compute process transition context before modifying</dd>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>,TYPE/</i></dt>
<dd> type (for same role as parent)</dd>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>,USER/</i></dt>
<dd> user identity</dd>
<dt><code>-r</code>, <code>&#8211;role</code>=<i>,ROLE/</i></dt>
<dd> role</dd>
<dt><code>-l</code>, <code>&#8211;range</code>=<i>,RANGE/</i></dt>
<dd> levelrange</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Russell Coker.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/runcon">https://www.gnu.org/software/coreutils/runcon</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) runcon invocation&#8217; </p>
