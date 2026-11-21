---
title: "mkafmmap(1)"
name: "mkafmmap"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkafmmap/"
description: "mkafmmap – creates font map for AFM files"
---

<h2>SYNOPSIS</h2>
<p> <code>mkafmmap</code> [<i>options</i>]<i> files</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>mkafmmap</code> command will generate a font map file reading all the AFM files given in the command line. By default it will write the map to a file named <code>font.map</code>, a different filename can be specified with the <code>&#8211;output-file</code> options. Using &#8216;<code>&#8211;</code>&#8216; will make the program write the map to <code>stdout</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show version of program.</dd>
<dt><code>-p, &#8211;output-file=NAME</code></dt>
<dd> Print output to file NAME.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-enscript/">enscript</a></code>(1), <code><a href="/docs/linux/man/1-states/">states</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Lucas Wall &lt;kthulhu [at] usa.net&gt;, for the Debian project (but may be used by others). </p>
