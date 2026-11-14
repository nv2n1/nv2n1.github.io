---
title: "unbuffer(1)"
name: "unbuffer"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unbuffer/"
description: "unbuffer – unbuffer output"
---

<h2 class="name">NAME</h2>
<p> unbuffer &#8211; unbuffer output </p>
<h2>SYNOPSIS</h2>
<p> <code>unbuffer</code> <i>program</i> [ <i>args</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>unbuffer</code> disables the output buffering that occurs when program output is redirected from non-interactive programs. For example, suppose you are watching the output from a fifo by running it through od and then more. </p>
<pre>
        od -c /tmp/fifo | more
</pre>
<p> You will not see anything until a full page of output has been produced. </p>
<p> You can disable this automatic buffering as follows: </p>
<pre>
        unbuffer od -c /tmp/fifo | more
</pre>
<p> Normally, unbuffer does not read from stdin. This simplifies use of unbuffer in some situations. To use unbuffer in a pipeline, use the -p flag. Example: </p>
<pre>
        process1 | unbuffer -p process2 | process3
</pre>
<h2>CAVEATS</h2>
<p> unbuffer -p may appear to work incorrectly if a process feeding input to unbuffer exits. Consider: </p>
<pre>
        process1 | unbuffer -p process2 | process3
</pre>
<p> If process1 exits, process2 may not yet have finished. It is impossible for unbuffer to know long to wait for process2 and process2 may not ever finish, for example, if it is a filter. For expediency, unbuffer simply exits when it encounters an EOF from either its input or process2. </p>
<p> In order to have a version of unbuffer that worked in all situations, an oracle would be necessary. If you want an application-specific solution, workarounds or hand-coded Expect may be more suitable. For example, the following example shows how to allow grep to finish processing when the cat before it finishes first. Using cat to feed grep would never require unbuffer in real life. It is merely a placeholder for some imaginary process that may or may not finish. Similarly, the final cat at the end of the pipeline is also a placeholder for another process. </p>
<pre>
$ cat /tmp/abcdef.log | grep abc | cat
abcdef
xxxabc defxxx
$ cat /tmp/abcdef.log | unbuffer grep abc | cat
$ (cat /tmp/abcdef.log ; sleep 1) | unbuffer grep abc | cat
abcdef
xxxabc defxxx
$ 
</pre>
<h2>BUGS</h2>
<p> The man page is longer than the program. </p>
<h2>SEE ALSO</h2>
<p> <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<h2>Index</h2>
