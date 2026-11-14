---
title: "igawk(1)"
name: "igawk"
section: "1"
letter: "i"
url: "/docs/linux/man/1-igawk/"
description: "igawk – gawk with include files"
---

<h2 class="name">NAME</h2>
<p> igawk &#8211; gawk with include files </p>
<h2>SYNOPSIS</h2>
<p> <code>igawk</code> [ all <i>gawk</i> options ] <code>-f</code> <i>program-file</i> [ <code>&#8212;</code> ] file &#8230;<br />
 <code>igawk</code> [ all <i>gawk</i> options ] [ <code>&#8212;</code> ] <i>program-text</i> file &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>Igawk</i> is a simple shell script that adds the ability to have &#8220;include files&#8221; to <i><a href="/docs/linux/man/1-gawk/">gawk</a></i>(1). </p>
<p> AWK programs for <i>igawk</i> are the same as for <i>gawk</i>, except that, in addition, you may have lines like</p>
<dl>
<dt>
<dd>
<p> <code> @include getopt.awk </code> </p>
</dl>
<p> in your program to include the file <code>getopt.awk</code> from either the current directory or one of the other directories in the search path.</p>
<h2>OPTIONS</h2>
<p> See <i><a href="/docs/linux/man/1-gawk/">gawk</a></i>(1) for a full description of the AWK language and the options that <i>gawk</i> supports.</p>
<h2>EXAMPLES</h2>
<pre><code>
cat &lt;&lt; EOF &gt; test.awk
             @include getopt.awk
                 BEGIN
{
    while (getopt(ARGC, ARGV, "am:q") != -1)
        ...
}
EOF
        igawk -
    f test.awk
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gawk/">gawk</a></i>(1) </p>
<p> <i>Effective AWK Programming</i>, Edition 1.0, published by the Free Software Foundation, 1995.</p>
<h2>AUTHOR</h2>
<p> Arnold Robbins (<code>arnold [at] skeeve.com</code>). </p>
<h2>Index</h2>
