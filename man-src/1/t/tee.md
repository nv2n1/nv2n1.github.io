---
title: "tee(1)"
name: "tee"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tee/"
description: "tee – read from standard input and write to standard output and files"
---

<h2 class="name">NAME</h2>
<p> tee &#8211; read from standard input and write to standard output and files </p>
<h2>SYNOPSIS</h2>
<p> <code>tee</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Copy standard input to each FILE, and also to standard output.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;append</code></p>
<dd> append to the given FILEs, do not overwrite</p>
<dt><code>-i</code>, <code>&#8211;ignore-interrupts</code></p>
<dd> ignore interrupt signals</p>
<dt><code>-p</code></p>
<dd> diagnose errors writing to non pipes</p>
<dt><code>&#8211;output-error</code>[=<i>,MODE/</i>]</p>
<dd> set behavior on write error. See MODE below</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h3>MODE determines behavior with write errors on the outputs:</h3>
<dl>
<dt>&#8216;warn&#8217;</p>
<dd> diagnose errors writing to any output</p>
<dt>&#8216;warn-nopipe&#8217;</p>
<dd> diagnose errors writing to any output not a pipe</p>
<dt>&#8216;exit&#8217;</p>
<dd> exit on error writing to any output</p>
<dt>&#8216;exit-nopipe&#8217;</p>
<dd> exit on error writing to any output not a pipe</dl>
<p> The default MODE for the <code>-p</code> option is &#8216;warn-nopipe&#8217;. The default operation when <code>&#8211;output-error</code> is not specified, is to exit immediately on error writing to a pipe, and diagnose errors writing to non pipe outputs.</p>
<h2>AUTHOR</h2>
<p> Written by Mike Parker, Richard M. Stallman, and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/tee">https://www.gnu.org/software/coreutils/tee</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) tee invocation&#8217; </p>
<h2>Index</h2>
