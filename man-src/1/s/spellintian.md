---
title: "spellintian(1)"
name: "spellintian"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spellintian/"
description: "spellintian – simple spellchecker based on Lintian’s data files"
---

<h2 class="name">NAME</h2>
<p> spellintian &#8211; simple spellchecker based on Lintian&#8217;s data files </p>
<h2>SYNOPSIS</h2>
<p> <code>spellintian</code> [<code>&#8211;picky</code>] [<i>text-file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>spellintian</code> command parses one or more text files for spelling mistakes. It uses the same spellcheck algorithm and data set as <code>lintian</code>. </p>
<p> If no file is specified on the command line, this command expects its input on stdin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;picky</code></p>
<dd> Also use the &#8220;picky&#8221; data set on top of the regular spelling data set. The &#8220;picky&#8221; data set also includes a lot of capitalization related rules (like spelling &#8220;Debian&#8221; with an uppercase &#8220;D&#8221;). </p>
<p> Note however that these checks can have false positives. As an example, consider the following those uses of Python &#8220;the python binary&#8221; (e.g. /usr/bin/python) and &#8220;the Python language&#8221;. The <code>&#8211;picky</code> option will unconditionally flag the use of &#8220;python&#8221; in the first case as bad despite being correct.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print a version banner and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Niels Thykier &lt;niels [at] thykier.net&gt; (wrote the manpage) </p>
<p> Jakub Wilk &lt;jwilk [at] jwilk.net&gt; (wrote the program) </p>
<h2>Index</h2>
