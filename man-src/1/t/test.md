---
title: "test(1)"
name: "test"
section: "1"
letter: "t"
url: "/docs/linux/man/1-test/"
description: "test – check file types and compare values"
---

<h2 class="name">NAME</h2>
<p> test &#8211; check file types and compare values </p>
<h2>SYNOPSIS</h2>
<p> <code>test</code> <i>EXPRESSION</i><br />
 <code>test</code><br />
 <code>[</code> <i>EXPRESSION</i> <code>]</code><br />
 <code>[ ]</code><br />
 <code>[</code> <i>OPTION</i></p>
<h2>DESCRIPTION</h2>
<p> Exit with the status determined by EXPRESSION.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> An omitted EXPRESSION defaults to false. Otherwise, EXPRESSION is true or false and sets exit status. It is one of:</p>
<dl>
<dt>( EXPRESSION )</p>
<dd> EXPRESSION is true</p>
<dt>! EXPRESSION</p>
<dd> EXPRESSION is false</p>
<dt>EXPRESSION1 <code>-a</code> EXPRESSION2</p>
<dd> both EXPRESSION1 and EXPRESSION2 are true</p>
<dt>EXPRESSION1 <code>-o</code> EXPRESSION2</p>
<dd> either EXPRESSION1 or EXPRESSION2 is true</p>
<dt><code>-n</code> STRING</p>
<dd> the length of STRING is nonzero</p>
<dt>STRING</p>
<dd> equivalent to <code>-n</code> STRING</p>
<dt><code>-z</code> STRING</p>
<dd> the length of STRING is zero</p>
<dt>STRING1 = STRING2</p>
<dd> the strings are equal</p>
<dt>STRING1 != STRING2</p>
<dd> the strings are not equal</p>
<dt>INTEGER1 <code>-eq</code> INTEGER2</p>
<dd> INTEGER1 is equal to INTEGER2</p>
<dt>INTEGER1 <code>-ge</code> INTEGER2</p>
<dd> INTEGER1 is greater than or equal to INTEGER2</p>
<dt>INTEGER1 <code>-gt</code> INTEGER2</p>
<dd> INTEGER1 is greater than INTEGER2</p>
<dt>INTEGER1 <code>-le</code> INTEGER2</p>
<dd> INTEGER1 is less than or equal to INTEGER2</p>
<dt>INTEGER1 <code>-lt</code> INTEGER2</p>
<dd> INTEGER1 is less than INTEGER2</p>
<dt>INTEGER1 <code>-ne</code> INTEGER2</p>
<dd> INTEGER1 is not equal to INTEGER2</p>
<dt>FILE1 <code>-ef</code> FILE2</p>
<dd> FILE1 and FILE2 have the same device and inode numbers</p>
<dt>FILE1 <code>-nt</code> FILE2</p>
<dd> FILE1 is newer (modification date) than FILE2</p>
<dt>FILE1 <code>-ot</code> FILE2</p>
<dd> FILE1 is older than FILE2</p>
<dt><code>-b</code> FILE</p>
<dd> FILE exists and is block special</p>
<dt><code>-c</code> FILE</p>
<dd> FILE exists and is character special</p>
<dt><code>-d</code> FILE</p>
<dd> FILE exists and is a directory</p>
<dt><code>-e</code> FILE</p>
<dd> FILE exists</p>
<dt><code>-f</code> FILE</p>
<dd> FILE exists and is a regular file</p>
<dt><code>-g</code> FILE</p>
<dd> FILE exists and is set-group-ID</p>
<dt><code>-G</code> FILE</p>
<dd> FILE exists and is owned by the effective group ID</p>
<dt><code>-h</code> FILE</p>
<dd> FILE exists and is a symbolic link (same as <code>-L</code>)</p>
<dt><code>-k</code> FILE</p>
<dd> FILE exists and has its sticky bit set</p>
<dt><code>-L</code> FILE</p>
<dd> FILE exists and is a symbolic link (same as <code>-h</code>)</p>
<dt><code>-N</code> FILE</p>
<dd> FILE exists and has been modified since it was last read</p>
<dt><code>-O</code> FILE</p>
<dd> FILE exists and is owned by the effective user ID</p>
<dt><code>-p</code> FILE</p>
<dd> FILE exists and is a named pipe</p>
<dt><code>-r</code> FILE</p>
<dd> FILE exists and read permission is granted</p>
<dt><code>-s</code> FILE</p>
<dd> FILE exists and has a size greater than zero</p>
<dt><code>-S</code> FILE</p>
<dd> FILE exists and is a socket</p>
<dt><code>-t</code> FD</p>
<dd> file descriptor FD is opened on a terminal</p>
<dt><code>-u</code> FILE</p>
<dd> FILE exists and its set-user-ID bit is set</p>
<dt><code>-w</code> FILE</p>
<dd> FILE exists and write permission is granted</p>
<dt><code>-x</code> FILE</p>
<dd> FILE exists and execute (or search) permission is granted</dl>
<p> Except for <code>-h</code> and <code>-L</code>, all FILE-related tests dereference symbolic links. Beware that parentheses need to be escaped (e.g., by backslashes) for shells. INTEGER may also be <code>-l</code> STRING, which evaluates to the length of STRING. </p>
<p> NOTE: Binary <code>-a</code> and <code>-o</code> are inherently ambiguous. Use &#8216;test EXPR1 &amp;&amp; test EXPR2&#8217; or &#8216;test EXPR1 || test EXPR2&#8217; instead. </p>
<p> NOTE: [ honors the <code>&#8211;help</code> and <code>&#8211;version</code> options, but test does not. test treats each of those as it treats any other nonempty STRING. </p>
<p> NOTE: your shell may have its own version of test and/or [, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.</p>
<h2>AUTHOR</h2>
<p> Written by Kevin Braunsdorf and Matthew Bradburn.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/[">https://www.gnu.org/software/coreutils/[</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) test invocation&#8217; </p>
<h2>Index</h2>
