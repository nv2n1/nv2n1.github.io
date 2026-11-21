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
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> An omitted EXPRESSION defaults to false. Otherwise, EXPRESSION is true or false and sets exit status. It is one of:</p>
<dl>
<dt>( EXPRESSION )</dt>
<dd> EXPRESSION is true</dd>
<dt>! EXPRESSION</dt>
<dd> EXPRESSION is false</dd>
<dt>EXPRESSION1 <code>-a</code> EXPRESSION2</dt>
<dd> both EXPRESSION1 and EXPRESSION2 are true</dd>
<dt>EXPRESSION1 <code>-o</code> EXPRESSION2</dt>
<dd> either EXPRESSION1 or EXPRESSION2 is true</dd>
<dt><code>-n</code> STRING</dt>
<dd> the length of STRING is nonzero</dd>
<dt>STRING</dt>
<dd> equivalent to <code>-n</code> STRING</dd>
<dt><code>-z</code> STRING</dt>
<dd> the length of STRING is zero</dd>
<dt>STRING1 = STRING2</dt>
<dd> the strings are equal</dd>
<dt>STRING1 != STRING2</dt>
<dd> the strings are not equal</dd>
<dt>INTEGER1 <code>-eq</code> INTEGER2</dt>
<dd> INTEGER1 is equal to INTEGER2</dd>
<dt>INTEGER1 <code>-ge</code> INTEGER2</dt>
<dd> INTEGER1 is greater than or equal to INTEGER2</dd>
<dt>INTEGER1 <code>-gt</code> INTEGER2</dt>
<dd> INTEGER1 is greater than INTEGER2</dd>
<dt>INTEGER1 <code>-le</code> INTEGER2</dt>
<dd> INTEGER1 is less than or equal to INTEGER2</dd>
<dt>INTEGER1 <code>-lt</code> INTEGER2</dt>
<dd> INTEGER1 is less than INTEGER2</dd>
<dt>INTEGER1 <code>-ne</code> INTEGER2</dt>
<dd> INTEGER1 is not equal to INTEGER2</dd>
<dt>FILE1 <code>-ef</code> FILE2</dt>
<dd> FILE1 and FILE2 have the same device and inode numbers</dd>
<dt>FILE1 <code>-nt</code> FILE2</dt>
<dd> FILE1 is newer (modification date) than FILE2</dd>
<dt>FILE1 <code>-ot</code> FILE2</dt>
<dd> FILE1 is older than FILE2</dd>
<dt><code>-b</code> FILE</dt>
<dd> FILE exists and is block special</dd>
<dt><code>-c</code> FILE</dt>
<dd> FILE exists and is character special</dd>
<dt><code>-d</code> FILE</dt>
<dd> FILE exists and is a directory</dd>
<dt><code>-e</code> FILE</dt>
<dd> FILE exists</dd>
<dt><code>-f</code> FILE</dt>
<dd> FILE exists and is a regular file</dd>
<dt><code>-g</code> FILE</dt>
<dd> FILE exists and is set-group-ID</dd>
<dt><code>-G</code> FILE</dt>
<dd> FILE exists and is owned by the effective group ID</dd>
<dt><code>-h</code> FILE</dt>
<dd> FILE exists and is a symbolic link (same as <code>-L</code>)</dd>
<dt><code>-k</code> FILE</dt>
<dd> FILE exists and has its sticky bit set</dd>
<dt><code>-L</code> FILE</dt>
<dd> FILE exists and is a symbolic link (same as <code>-h</code>)</dd>
<dt><code>-N</code> FILE</dt>
<dd> FILE exists and has been modified since it was last read</dd>
<dt><code>-O</code> FILE</dt>
<dd> FILE exists and is owned by the effective user ID</dd>
<dt><code>-p</code> FILE</dt>
<dd> FILE exists and is a named pipe</dd>
<dt><code>-r</code> FILE</dt>
<dd> FILE exists and read permission is granted</dd>
<dt><code>-s</code> FILE</dt>
<dd> FILE exists and has a size greater than zero</dd>
<dt><code>-S</code> FILE</dt>
<dd> FILE exists and is a socket</dd>
<dt><code>-t</code> FD</dt>
<dd> file descriptor FD is opened on a terminal</dd>
<dt><code>-u</code> FILE</dt>
<dd> FILE exists and its set-user-ID bit is set</dd>
<dt><code>-w</code> FILE</dt>
<dd> FILE exists and write permission is granted</dd>
<dt><code>-x</code> FILE</dt>
<dd> FILE exists and execute (or search) permission is granted</dd></dl>
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
