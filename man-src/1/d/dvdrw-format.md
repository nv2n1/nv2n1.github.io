---
title: "dvdrw-format(1)"
name: "dvdrw-format"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvdrw-format/"
description: "dvd+rw-format – format DVD+-RW/-RAM disk"
---

<p>dvd+rw-format &#8211; format DVD+-RW/-RAM disk</p>
<h2>Synopsis</h2>
<p><code>dvd+rw-format</code> [<code>-force[=full]</code>] [<code>-lead-out | -blank[=full]</code>] [<code>-ssa[=none | default | max]</code>] <i>/dev/dvd</i> </p>
<h2>Description</h2>
<p>The <code>dvd+rw-format</code> command formats dvd disk in the specified dvd drive (e.g. <i>/dev/dvd</i>). </p>
<h2>Options</h2>
<dl>
<dt><code>-force[=full]</code></dt>
<dd>This forces to format dvd as new while wiping any existing data.</dd>
<dt><code>-blank[=full]</code></dt>
<dd>This blanks dvd while changing to sequential mode.</dd>
<dt><code>-lead-out</code></dt>
<dd>This relocates the lead-out next to outermost written sector as well as makes sure there is no virgin surface before it. Previously written data is not affected by this operation. Useful for addressing <code>DVD-ROM compatibility,</code> or playability of already recorded media in legacy units. </dd>
</dl>
<h2>See Also</h2>
<p>Most up-to-date information on dvd+rw-tools is available at <a rel="nofollow" href="http://fy.chalmers.se/~appro/linux/DVD+RW/.">http://fy.chalmers.se/~appro/linux/DVD+RW/.</a> </p>
<p> The manpage for <code>genisofs</code>(8), <code><a href="/docs/linux/man/1-growisofs/">growisofs</a></code>(1), <code>dvd+rw-mediainfo</code>(1), <code>dvd+rw-booktype</code>(1). </p>
<h2>Author</h2>
<p><code>dvd+rw-format</code> was written by Andy Polyakov &lt;appro [at] fy.chalmers.se&gt;. This manual page was written by Osamu Aoki &lt;osamu [at] debian.org&gt; for the Debian project.</p>
