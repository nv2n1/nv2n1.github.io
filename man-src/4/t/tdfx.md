---
title: "tdfx(4)"
name: "tdfx"
section: "4"
letter: "t"
url: "/docs/linux/man/4-tdfx/"
description: "tdfx – 3Dfx video driver"
---

<p>tdfx &#8211; 3Dfx video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;tdfx&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>tdfx </code> is an Xorg driver for 3Dfx video cards.</p>
<h2>Supported Hardware</h2>
<p>The <code>tdfx</code> driver supports Voodoo Banshee, Voodoo3, Voodoo4 and Voodoo5 cards.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;NoAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option &#34;SWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable software cursor. Default: software cursor is disable and a hardware cursor is used for configurations where the hardware cursor is available.</p>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable DRI support. By default, DRI is on.</p>
<dt><code>Option &#34;TexturedVideo&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This has XvImage support use the texture engine rather than the video overlay.</p>
<dt><code>Option &#34;VideoKey&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This sets the default pixel value for the YUV video overlay key. Default: undefined.</p>
<dt><code>Option &#34;UsePIO&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Force the use of Programmed IO instead of Memory Mapped IO. Default: off.</dl>
<p> The following additional <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;ShowCache&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable viewing offscreen cache memory. A development debug option. Default: off.</dl>
<h2>Files</h2>
<p>tdfx_drv.o</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: &#8230;</p>
