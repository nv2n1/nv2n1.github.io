---
title: "rendercheck(1)"
name: "rendercheck"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rendercheck/"
description: "rendercheck – simple tests of the X Render extension."
---

<h2 class="name">NAME</h2>
<p> rendercheck &#8211; simple tests of the X Render extension. </p>
<h2>SYNOPSIS</h2>
<pre><code>
rendercheck[-d | --display display][-i | --iter][--sync][-t | --tests test1, test2, test3, ...][-o | --ops op1, op2, op3, ...]
           [-v | --verbose][--minimalrendering]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>rendercheck</code> is a set of simple tests of the X Render extension. It is designed for authors of Render implementations in X Servers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d|&#8211;display display</code></p>
<dd> Specifies the display to test against.</p>
<dt><code>-i|&#8211;iter iterations</code></p>
<dd> Specifies the number of times to repeat each operation before sampling results. Some X Servers may behave differently (hardware vs software rendering paths) depending on the previous operations done, so this may be used to influence the server&#8217;s choices.</p>
<dt><code>&#8211;sync</code></p>
<dd> Enables synchronous xlib operation, for debugging.</p>
<dt><code>-t|&#8211;tests test1,test2,test3&#8230;</code></p>
<dd> Enables only a specific subset of the possible tests. Test names include fill, dcoords, scoords, mcoords, tscoords, tmcoords, blend, composite, cacomposite, gradients, repeat, triangles, and bug7366. Names must be separated by commas and have no spaces.</p>
<dt><code>-f|&#8211;formats format1,format2,format3&#8230;</code></p>
<dd> Enables only a specific subset of the possible formats. Only formats listed in the server-supported format list are available. Names must be separated by commas and have no spaces.</p>
<dt><code>-o|&#8211;ops</code></p>
<dd> Enables only a specific subset of the Render operators.</p>
<dt><code>-v|&#8211;verbose</code></p>
<dd> Enables verbose printing of information on tests run, and successes and failures.</p>
<dt><code>&#8211;minimalrendering</code></p>
<dd> Disables copying of offscreen destinations to the window, which is on by default to provide the user with visual feedback.</dl>
<h2>BUGS</h2>
<p> Several limitations are documented in the TODO file accompanying the source. Please report any further bugs you find to <a rel="nofollow" href="http://bugs.freedesktop.org/.">http://bugs.freedesktop.org/.</a></p>
<h2>AUTHORS</h2>
<p> Eric Anholt, with help from Keith Packard. </p>
<h2>Index</h2>
