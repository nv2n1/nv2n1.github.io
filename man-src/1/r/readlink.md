---
title: "readlink(1)"
name: "readlink"
section: "1"
letter: "r"
url: "/docs/linux/man/1-readlink/"
description: "readlink – print resolved symbolic links or canonical file names"
---

<h2 class="name">NAME</h2>
<p> readlink &#8211; print resolved symbolic links or canonical file names </p>
<h2>SYNOPSIS</h2>
<p> <code>readlink</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Note <a href="/docs/linux/man/1-realpath/">realpath</a>(1) is the preferred command to use for canonicalization functionality. </p>
<p> Print value of a symbolic link or canonical file name</p>
<dl>
<dt><code>-f</code>, <code>&#8211;canonicalize</code></p>
<dd> canonicalize by following every symlink in every component of the given name recursively; all but the last component must exist</p>
<dt><code>-e</code>, <code>&#8211;canonicalize-existing</code></p>
<dd> canonicalize by following every symlink in every component of the given name recursively, all components must exist</p>
<dt><code>-m</code>, <code>&#8211;canonicalize-missing</code></p>
<dd> canonicalize by following every symlink in every component of the given name recursively, without requirements on components existence</p>
<dt><code>-n</code>, <code>&#8211;no-newline</code></p>
<dd> do not output the trailing delimiter</p>
<dt> <code>-q</code>, <code>&#8211;quiet</code></p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd>
<dd>suppress most error messages (on by default)</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> report error messages</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd> end each output line with NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Dmitry V. Levin.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-readlink/">readlink</a>(2), <a href="/docs/linux/man/1-realpath/">realpath</a>(1), <a href="/docs/linux/man/3-realpath/">realpath</a>(3) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/readlink">https://www.gnu.org/software/coreutils/readlink</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) readlink invocation&#8217; </p>
<h2>Index</h2>
