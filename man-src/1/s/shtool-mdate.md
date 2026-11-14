---
title: "shtool-mdate(1)"
name: "shtool-mdate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-mdate/"
description: "shtool mdate – GNU shtool pretty-print last modification time"
---

<h2 class="name">NAME</h2>
<p> shtool mdate &#8211; GNU shtool pretty-print last modification time </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool mdate</code> [<code>-n</code>|<code>&#8211;newline</code>] [<code>-z</code>|<code>&#8211;zero</code>] [<code>-s</code>|<code>&#8211;shorten</code>] [<code>-d</code>|<code>&#8211;digits</code>] [<code>-f</code>|<code>&#8211;field-sep</code> <i>str</i>] [<code>-o</code>|<code>&#8211;order</code> <i>spec</i>] <i>path</i></p>
<h2>DESCRIPTION</h2>
<p> This command pretty-prints the last modification time of a given file or directory <i>path</i>, while still allowing one to specify the format of the date to display.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;newline</code></p>
<dd> By default, output is written to <i>stdout</i> followed by a &#8220;newline&#8221; (<font SIZE="-1">ASCII</font> character 0x0a). If option <code>-n</code> is used, this newline character is omitted.</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd> Pads numeric day and numeric month with a leading zero. Default is to have variable width.</p>
<dt><code>-s</code>, <code>&#8211;shorten</code></p>
<dd> Shortens the name of the month to a english three character abbreviation. Default is full english name. This option is silently ignored when combined with <code>-d</code>.</p>
<dt><code>-d</code>, <code>&#8211;digits</code></p>
<dd> Use digits for month. Default is to use a english name.</p>
<dt><code>-f</code>, <code>&#8211;field-sep</code> <i>str</i></p>
<dd> Field separator string between the day month year tripple. Default is a single space character.</p>
<dt><code>-o</code>, <code>&#8211;order</code> <i>spec</i></p>
<dd> Specifies order of the day month year elements within the tripple. Each element represented as a single character out of &#8220;<tt>&quot;d&quot;</tt>&#8221;, &#8220;<tt>&quot;m&quot;</tt>&#8221; and &#8220;<tt>&quot;y&quot;</tt>&#8221;. The default for <i>spec</i> is &#8220;<tt>&quot;dmy&quot;</tt>&#8221;.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool mdate -n /
 shtool mdate -f '/' -z -d -o ymd foo.txt
 shtool mdate -f '-' -s foo.txt
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>mdate</code> command was originally written by Ulrich Drepper in 1995 and revised by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for inclusion into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-date/">date</a></i>(1), <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1). </p>
<h2>Index</h2>
