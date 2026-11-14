---
title: "rdiff(1)"
name: "rdiff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdiff/"
description: "rdiff – compute and apply signature-based file differences"
---

<h2>NAME</h2>
<p> rdiff &#8211; compute and apply signature-based file differences</p>
<h2>SYNOPSYS</h2>
<pre><code>
rdiff[options] signature old - file signature - file rdiff[options] delta signature - file new - file delta - file rdiff[options] patch basis - file delta - file new - file
</code></pre>
<h2>USAGE</h2>
<p> You can use <code>rdiff</code> to update files, much like <code>rsync</code> does. However, unlike <code>rsync</code>, <code>rdiff</code> puts you in control. There are three steps to updating a file: <code>signature</code>, <code>delta</code>, and <code>patch</code>.</p>
<h2>DESCRIPTION</h2>
<p> In every case where a filename must be specified, &#8211; may be used instead to mean either standard input or standard output as appropriate. Be aware that if you do this, you&#8217;ll need to terminate your <i>options</i> with &#8212; or <code>rdiff</code> will think you are passing it an empty option.</p>
<h2>RETURN VALUE</h2>
<p> 0 for successful completion, 1 for environmental problems (file not found, invalid options, IO error, etc), 2 for a corrupt file and 3 for an internal error or unhandled situation in librsync or rdiff.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-librsync/">librsync</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Martin Pool &lt;mbp [at] sourcefrog.net&gt; </p>
<p> The original rsync algorithm was discovered by Andrew Tridgell. </p>
<p> rdiff development has been supported by Linuxcare, Inc and VA Linux Systems. </p>
<h2>Index</h2>
