---
title: "vboxmode(1)"
name: "vboxmode"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxmode/"
description: "vboxmode – detect format of isdn voice file"
---

<h2>NAME</h2>
<p> vboxmode &#8211; detect format of isdn voice file</p>
<h2>SYNOPSIS</h2>
<p> <code>vboxmode</code> <i>[OPTION] [OPTION] [&#8230;] FILENAME</i></p>
<h2>DESCRIPTION</h2>
<p> Vboxmode detects format of isdn voice files and au files (sun audio format).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Don&#8217;t print information about the file, only detect format and return an error code.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version of program.</dl>
<h2>RETURN CODE</h2>
<p> The format of the file is returned as an error code: </p>
<dl>
<dt><code>o</code></p>
<dd> for .au files a value between 128 and 150</p>
<dt><code>o</code></p>
<dd> for vbox files a value between 2 and 6</p>
<dt><code>o</code></p>
<dd> for unknown format or errors 255 </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autovbox/">autovbox</a>(1), <a href="/docs/linux/man/1-rmdtovbox/">rmdtovbox</a>(1), <a href="/docs/linux/man/1-vboxtoau/">vboxtoau</a>(1), <a href="/docs/linux/man/1-vboxcnvt/">vboxcnvt</a>(1), <a href="/docs/linux/man/5-vbox/">vbox</a>(5)</code> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux. </p>
<h2>Index</h2>
