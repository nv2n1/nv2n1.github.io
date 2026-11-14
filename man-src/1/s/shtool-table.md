---
title: "shtool-table(1)"
name: "shtool-table"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-table/"
description: "shtool table – GNU shtool pretty-print a field-separated list"
---

<h2 class="name">NAME</h2>
<p> shtool table &#8211; GNU shtool pretty-print a field-separated list </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool table</code> [<code>-F</code>|<code>&#8211;field-sep</code> <i>sep</i>] [<code>-w</code>|<code>&#8211;width</code> <i>width</i>] [<code>-c</code>|<code>&#8211;columns</code> <i>cols</i>] [<code>-s</code>|<code>&#8211;strip</code> <i>strip</i>] <i>str</i><code>sep</code><i>str</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This pretty-prints a list of strings as a table.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-F</code>, <code>&#8211;field-sep</code> <i>sep</i></p>
<dd> Separate columns using <i>sep</i>. Default is <tt>&quot;:&quot;</tt>.</p>
<dt><code>-w</code>, <code>&#8211;width</code> <i>width</i></p>
<dd> Width of each column. Default is 15 characters.</p>
<dt><code>-c</code>, <code>&#8211;columns</code> <i>cols</i></p>
<dd> Number of columns. Default is <tt>3</tt>.</p>
<dt><code>-s</code>, <code>&#8211;strip</code> <i>strip</i></p>
<dd> Strip off any characters past <i>strip</i>. Default is <tt>79</tt>.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool table -F , -w 5 -c 4 &quot;1,2,3,4,5,6,7,8,9,10,11,12&quot;
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>table</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1999 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-tr/">tr</a></i>(1), <i><a href="/docs/linux/man/1-fmt/">fmt</a></i>(1), <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i><a href="/docs/linux/man/1-awk/">awk</a></i>(1), <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1). </p>
<h2>Index</h2>
