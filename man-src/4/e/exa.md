---
title: "exa(4)"
name: "exa"
section: "4"
letter: "e"
url: "/docs/linux/man/4-exa/"
description: "exa – new 2D acceleration architecture for X.Org"
---

<p>exa &#8211; new 2D acceleration architecture for X.Org</p>
<h2>Description</h2>
<p><code>EXA</code> provides a simple API for video drivers to implement for 2D acceleration. It is a module loaded by drivers, and is not intended to be loaded on its own. See your driver&#8217;s manual page for how to enable <code>EXA</code>. </p>
<p> The <code>EXA</code> architecture is designed to make accelerating the Render extension simple and efficient, and results in various performance tradeoffs compared to XAA. Some xorg.conf options are available for debugging performance issues or driver rendering problems. They are not intended for general use.</p>
<dl>
<dt><code>Option &#34;EXANoComposite&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disables acceleration of the Composite operation, which is at the heart of the Render extension. Not related to the Composite extension. Default: No.</p>
<dt><code>Option &#34;EXANoUploadToScreen&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disables acceleration of uploading pixmap data to the framebuffer. Default: No.</p>
<dt><code>Option &#34;EXANoDownloadFromScreen&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disables acceleration of downloading of pixmap data from the framebuffer. <code>NOTE:</code> Not usable with drivers which rely on DownloadFromScreen succeeding. Default: No.</p>
<dt><code>Option &#34;MigrationHeuristic&#34; &#34;</code><i>anystr</i><code>&#34;</code></p>
<dd>Chooses an alternate pixmap migration heuristic, for debugging purposes. The default is intended to be the best performing one for general use, though others may help with specific use cases. Available options include &#34;always&#34;, &#34;greedy&#34;, and &#34;smart&#34;. Default: always.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xorg/">Xorg</a></code>(1), <code><a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5).</code></p>
<h2>Authors</h2>
<p>Authors include: Keith Packard, Eric Anholt, Zack Rusin, and Michel D&auml;nzer</p>
