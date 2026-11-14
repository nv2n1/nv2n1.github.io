---
title: "dvdrw-booktype(1)"
name: "dvdrw-booktype"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvdrw-booktype/"
description: "dvd+rw-booktype – format DVD+-RW/-RAM disk with a logical format"
---

<p>dvd+rw-booktype &#8211; format DVD+-RW/-RAM disk with a logical format</p>
<h2>Synopsis</h2>
<p><code>dvd+rw-booktype</code> [<code>-dvd-rom-spec | -dvd+rw-spec | -dvd+r-spec | -inq</code>] [<code>&nbsp;-media | -unit| -unit+rw | -unit+r</code>] <i>/dev/dvd</i> </p>
<h2>Description</h2>
<p>The <code>dvd+rw-booktype</code> command formats dvd disk in the specified dvd drive (e.g. <i>/dev/dvd</i>) with a specified logical format. <code>You can&#8217;t expect this utility to work with all recorders.</code> </p>
<h2>Options</h2>
<dl>
<dt><code>-dvd-rom</code></p>
<dd>This is useful for addressing <code>DVD-ROM compatibility,</code> or playability in legacy units. </p>
</dl>
<h2>See Also</h2>
<p>Most up-to-date information on dvd+rw-tools is available at <a rel="nofollow" href="http://fy.chalmers.se/~appro/linux/DVD+RW/.">http://fy.chalmers.se/~appro/linux/DVD+RW/.</a> </p>
<p> The manpage for <code><a href="/docs/linux/man/8-genisoimage/">genisoimage</a></code>(8), <code><a href="/docs/linux/man/1-growisofs/">growisofs</a></code>(1), <code>dvd+<a href="/docs/linux/man/1-rw-mediainfo/">rw-mediainfo</a></code>(1), <code>dvd+<a href="/docs/linux/man/1-rw-format/">rw-format</a></code>(1). </p>
<h2>Author</h2>
<p><code>dvd+rw-booktype</code> was written by Andy Polyakov &lt;appro [at] fy.chalmers.se&gt;. This manual page was written by Osamu Aoki &lt;osamu [at] debian.org&gt; for the Debian project.</p>
