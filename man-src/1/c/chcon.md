---
title: "chcon(1)"
name: "chcon"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chcon/"
description: "chcon – change file security context"
---

<h2>SYNOPSIS</h2>
<p> <code>chcon</code> [<i>,OPTION/</i>]&#8230; <i>,CONTEXT FILE/</i>&#8230;<br />
 <code>chcon</code> [<i>,OPTION/</i>]&#8230; [<i>,-u USER/</i>] [<i>,-r ROLE/</i>] [<i>,-l RANGE/</i>] [<i>,-t TYPE/</i>] <i>,FILE/</i>&#8230;<br />
 <code>chcon</code> [<i>,OPTION/</i>]&#8230; <i>,&#8211;reference=RFILE FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Change the SELinux security context of each FILE to CONTEXT. With <code>&#8211;reference</code>, change the security context of each FILE to that of RFILE. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;dereference</code></dt>
<dd> affect the referent of each symbolic link (this is the default), rather than the symbolic link itself</dd>
<dt><code>-h</code>, <code>&#8211;no-dereference</code></dt>
<dd> affect symbolic links instead of any referenced file</dd>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>,USER/</i></dt>
<dd> set user USER in the target security context</dd>
<dt><code>-r</code>, <code>&#8211;role</code>=<i>,ROLE/</i></dt>
<dd> set role ROLE in the target security context</dd>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>,TYPE/</i></dt>
<dd> set type TYPE in the target security context</dd>
<dt><code>-l</code>, <code>&#8211;range</code>=<i>,RANGE/</i></dt>
<dd> set range RANGE in the target security context</dd>
<dt><code>&#8211;no-preserve-root</code></dt>
<dd> do not treat &#8216;/&#8217; specially (the default)</dd>
<dt><code>&#8211;preserve-root</code></dt>
<dd> fail to operate recursively on &#8216;/&#8217;</dd>
<dt><code>&#8211;reference</code>=<i>,RFILE/</i></dt>
<dd> use RFILE&#8217;s security context rather than specifying a CONTEXT value</dd>
<dt><code>-R</code>, <code>&#8211;recursive</code></dt>
<dd> operate on files and directories recursively</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> output a diagnostic for every file processed</dd></dl>
<p> The following options modify how a hierarchy is traversed when the <code>-R</code> option is also specified. If more than one is specified, only the final one takes effect.</p>
<dl>
<dt><code>-H</code></dt>
<dd> if a command line argument is a symbolic link to a directory, traverse it</dd>
<dt><code>-L</code></dt>
<dd> traverse every symbolic link to a directory encountered</dd>
<dt><code>-P</code></dt>
<dd> do not traverse any symbolic links (default)</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Russell Coker and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/chcon">https://www.gnu.org/software/coreutils/chcon</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) chcon invocation&#8217; </p>
