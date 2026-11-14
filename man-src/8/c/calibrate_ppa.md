---
title: "calibrate_ppa(8)"
name: "calibrate_ppa"
section: "8"
letter: "c"
url: "/docs/linux/man/8-calibrate_ppa/"
description: "calibrate_ppa – pnm2ppa calibration tool"
---

<p>calibrate_ppa &#8211; pnm2ppa calibration tool</p>
<h2>Synopsis</h2>
<p><code>calibrate_ppa </code> [options]</p>
<h2>Description</h2>
<p>Produces various PixMap (PPM) files used for calibrating pnm2ppa.</p>
<dl>
<dt>This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page.</p>
<dd></dl>
<h2>Note</h2>
<p>The size of a full-page PixMap is 100MB!!. These PixMaps should be piped directly to pnm2ppa, except in the case of the -g option, where the PixMap should be viewed or printed by other means.</p>
<h2>Options</h2>
<dl>
<dt><code>-g, &#8211;gamma</code></p>
<dd>produce gamma.ppm (10MB, used in color calibration).</p>
<dt><code>-h, &#8211;help</code></p>
<dd>displays this help text.</p>
<dt><code>-o &lt;outfile&gt;</code></p>
<dd>output to file &lt;outfile&gt;, &quot;-o -&quot; means stdout (default)</p>
<dt><code>-p &lt;n&gt;</code></p>
<dd>create test pattern number &lt;n&gt;</p>
<dt><code>&#8211;align</code></p>
<dd>pattern 0: align print heads. (default)</p>
<dt><code>&#8211;test</code></p>
<dd>pattern 1: test alignment.</p>
<dt><code>&#8211;clean</code></p>
<dd>pattern 2: clean print head.</p>
<dt><code>&#8211;center</code></p>
<dd>pattern 3: center paper.</p>
<dt><code>-s</code> &lt;paper&gt;</p>
<dd>default papersize (a4, legal, letter = us (default))</dl>
<h2>Author</h2>
<p>This manual page was written by Chad C. Walstrom &lt;chewie [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-pnm2ppa/">pnm2ppa</a></i>(1), <i><a href="/docs/linux/man/8-magicfilter/">magicfilter</a></i>(8), <i><a href="/docs/linux/man/8-apsfilter/">apsfilter</a></i>(8) </p>
