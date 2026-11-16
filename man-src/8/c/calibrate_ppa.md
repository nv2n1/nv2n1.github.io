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
<dt>This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page.</dt>
<dd></dd></dl>
<h2>Note</h2>
<p>The size of a full-page PixMap is 100MB!!. These PixMaps should be piped directly to pnm2ppa, except in the case of the -g option, where the PixMap should be viewed or printed by other means.</p>
<h2>Options</h2>
<dl>
<dt><code>-g, &#8211;gamma</code></dt>
<dd>produce gamma.ppm (10MB, used in color calibration).</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>displays this help text.</dd>
<dt><code>-o &lt;outfile&gt;</code></dt>
<dd>output to file &lt;outfile&gt;, &quot;-o -&quot; means stdout (default)</dd>
<dt><code>-p &lt;n&gt;</code></dt>
<dd>create test pattern number &lt;n&gt;</dd>
<dt><code>&#8211;align</code></dt>
<dd>pattern 0: align print heads. (default)</dd>
<dt><code>&#8211;test</code></dt>
<dd>pattern 1: test alignment.</dd>
<dt><code>&#8211;clean</code></dt>
<dd>pattern 2: clean print head.</dd>
<dt><code>&#8211;center</code></dt>
<dd>pattern 3: center paper.</dd>
<dt><code>-s</code> &lt;paper&gt;</dt>
<dd>default papersize (a4, legal, letter = us (default))</dd></dl>
<h2>Author</h2>
<p>This manual page was written by Chad C. Walstrom &lt;chewie [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-pnm2ppa/">pnm2ppa</a></i>(1), <i>magicfilter</i>(8), <i>apsfilter</i>(8) </p>
