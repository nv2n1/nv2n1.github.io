---
title: "annotate-output(1)"
name: "annotate-output"
section: "1"
letter: "a"
url: "/docs/linux/man/1-annotate-output/"
description: "annotate-output – annotate program output with time and stream"
---

<h2>NAME</h2>
<p> annotate-output &#8211; annotate program output with time and stream</p>
<h2>SYNOPSIS</h2>
<p> <code>annotate-output</code> [<i>options</i>] <i>program</i> [<i>args</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>annotate-output</code> will execute the specified program, while prepending every line with the current time and O for stdout and E for stderr. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>+FORMAT</code></p>
<dd> Controls the timestamp format, as per <code><a href="/docs/linux/man/1-date/">date</a></code>(1). Defaults to &quot;%H:%M:%S&quot;.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a help message and exit successfully. </p>
</dl>
<h2>EXAMPLE</h2>
<pre>
$ annotate-output make
21:41:21 I: Started make
21:41:21 O: gcc -Wall program.c
21:43:18 E: program.c: Couldn't compile, and took me ages to find out
21:43:19 E: collect2: ld returned 1 exit status
21:43:19 E: make: *** [all] Error 1
21:43:19 I: Finished with exitcode 2
</pre>
<h2>BUGS</h2>
<p> Since stdout and stderr are processed in parallel, it can happen that some lines received on stdout will show up before later-printed stderr lines (and vice-versa). </p>
<p> This is unfortunately very hard to fix with the current annotation strategy. A fix would involve switching to PTRACE&#8217;ing the process. Giving nice a (much) higher priority over the executed program could however cause this behaviour to show up less frequently. </p>
<p> The program does not work as well when the output is not linewise. In particular, when an interactive program asks for input, the question might not be shown until after you have answered it. This will give the impression that the annotated program has hung, while it has not. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1) </p>
<h2>SUPPORT</h2>
<p> This program is community-supported (meaning: you&#8217;ll need to fix it yourself). Patches are however appreciated, as is any feedback (positive or negative). </p>
<h2>AUTHOR</h2>
<p> <code>annotate-output</code> was written by Jeroen van Wolffelaar &lt;jeroen [at] wolffelaar.nl&gt; This manpage comes under the same copyright as annotate-output itself, read /usr/bin/annotate-output (or wherever you install it) for the details. </p>
<h2>Index</h2>
