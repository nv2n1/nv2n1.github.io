---

title: "id(1)"
name: "id"
section: "1"
letter: "i"
url: "/docs/linux/man/1-id/"
description: "id – print real and effective user and group IDs"
---

<p> id &#8211; print real and effective user and group IDs </p>
<h2>SYNOPSIS</h2>
<p> <code>id</code> [<i>,OPTION/</i>]&#8230; [<i>,USER/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print user and group information for each specified USER, or (when USER omitted) for the current user.</p>
<dl>
<dt><code>-a</code></dt>
<dd> ignore, for compatibility with other versions</dd>
<dt><code>-Z</code>, <code>&#8211;context</code></dt>
<dd> print only the security context of the process</dd>
<dt><code>-g</code>, <code>&#8211;group</code></dt>
<dd> print only the effective group ID</dd>
<dt><code>-G</code>, <code>&#8211;groups</code></dt>
<dd> print all group IDs</dd>
<dt><code>-n</code>, <code>&#8211;name</code></dt>
<dd> print a name instead of a number, for <code>-ugG</code></dd>
<dt><code>-r</code>, <code>&#8211;real</code></dt>
<dd> print the real ID instead of the effective ID, with <code>-ugG</code></dd>
<dt><code>-u</code>, <code>&#8211;user</code></dt>
<dd> print only the effective user ID</dd>
<dt><code>-z</code>, <code>&#8211;zero</code></dt>
<dd> delimit entries with NUL characters, not whitespace;</dd>
<dt>
</dt><dd> not permitted in default format</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> Without any OPTION, print some useful set of identified information.</p>
<h2>AUTHOR</h2>
<p> Written by Arnold Robbins and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br/>
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/id">https://www.gnu.org/software/coreutils/id</a>&gt;<br/>
 or available locally via: info &#8216;(coreutils) id invocation&#8217; </p>
