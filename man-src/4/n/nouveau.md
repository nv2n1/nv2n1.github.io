---
title: "nouveau(4)"
name: "nouveau"
section: "4"
letter: "n"
url: "/docs/linux/man/4-nouveau/"
description: "nouveau – NVIDIA video driver"
---

<p>nouveau &#8211; NVIDIA video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;nouveau&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>nouveau</code> is an Xorg driver for NVIDIA video cards. The driver supports 2D acceleration and provides support for the following framebuffer depths: (15,) 16 and 24. TrueColor visuals are supported for these depths. </p>
<h2>Supported Hardware</h2>
<p>The <code>nouveau</code> driver supports PCI, PCI-Express and AGP video cards based on the following NVIDIA chips:</p>
<dl>
<dt><code>RIVA TNT</code></p>
<dd>NV4</p>
<dt><code>RIVA TNT2</code></p>
<dd>NV5</p>
<dt><code>GeForce 256, QUADRO</code></p>
<dd>NV10</p>
<dt><code>GeForce2, QUADRO2</code></p>
<dd>NV11 &amp; NV15</p>
<dt><code>GeForce3, QUADRO DCC</code></p>
<dd>NV20</p>
<dt><code>nForce, nForce2</code></p>
<dd>NV1A, NV1F</p>
<dt><code>GeForce4, QUADRO4</code></p>
<dd>NV17, NV18, NV25, NV28</p>
<dt><code>GeForce FX, QUADRO FX</code></p>
<dd>NV30, NV31, NV34, NV35, NV36, NV37, NV38</p>
<dt><code>GeForce 6XXX</code></p>
<dd>NV40, NV41, NV43, NV44, NV45, C51, MCP61</p>
<dt><code>GeForce 7XXX</code></p>
<dd>G70, G71, G72, G73, MCP67, MCP68, MCP73</p>
<dt><code>GeForce 8XXX, 9XXX, 2XX, 3XX</code></p>
<dd>G80, G84, G86, G92, G94, G96, G98, G200, GT215, GT216, GT218, MCP77, MCP79, MCP89</p>
<dt><code>GeForce 4XX, 5XX</code></p>
<dd>GF100, GF104, GF106, GF108, GF110, GF114, GF116, GF117, GF119</p>
<dt><code>GeForce 6XX, 7XX</code></p>
<dd>GK104, GK106, GK107, GK110, GK208</p>
<dt><code>GeForce GTX 750</code></p>
<dd>GM107, GM108</p>
<dt><code>GeForce GTX 9XX</code></p>
<dd>GM200, GM204, GM206</p>
<dt><code>GeForce GTX 10XX</code></p>
<dd>GP102, GP104, GP106, GP107, GP108 </p>
</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the chipset type and the amount of video memory present for all chips. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;HWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable the HW cursor. Default: on.</p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the acceleration method. One of &#34;none&#34;, or &#34;exa&#34;. Default: exa.</p>
<dt><code>Option &#34;NoAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: off.</p>
<dt><code>Option &#34;WrappedFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable wfb, only affects nv50+. Useful for some legacy configurations where high rendering latency is perceived. Default: wfb is disabled.</p>
<dt><code>Option &#34;GLXVBlank&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Synchronize GLX clients to VBlank. Useful where tearing is a problem, harmful if the GPU isn&#8217;t fast enough to keep up with the monitor refresh rate. Default: on.</p>
<dt><code>Option &#34;ZaphodHeads&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the randr output(s) to use with zaphod mode for a particular driver instance. If you use this option you most use this option for all instances of the driver.<br />
 For example: <code>Option &#34;ZaphodHeads&#34; &#34;LVDS,VGA-0&#34;</code> will assign xrandr outputs LVDS and VGA-0 to this instance of the driver.</p>
<dt><code>Option &#34;PageFlip&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable DRI2 page flipping. Default: on.</p>
<dt><code>Option &#34;SwapLimit&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set maximum allowed number of pending OpenGL double-buffer swaps for a drawable before a client is blocked.<br />
 A value of 1 corresponds to double-buffering. A value of 2 corresponds to triple-buffering. Higher values may allow higher framerate, but also increase lag for interactive applications, e.g., games. Nouveau currently reliably supports a maximum value of 2 on XOrg 1.12+. A maximum setting of 2 on older x-servers is allowed, but it will break conformance with the OpenML OML_sync_control specification and will cause failure of software that relies on correct presentation timing behaviour as defined in that specification.<br />
 Default: 1.</p>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Define the maximum level of DRI to enable. Valid values are 2 or 3. exa acceleration will honor the maximum level if it is supported. Default: 2.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: David McKay, Jarno Paananen, Chas Inman, Dave Schmenk, Mark Vojkovich</p>
<h2>Copyright</h2>
<p>NOTICE TO USER: The source code is copyrighted under U.S. and international laws. Users and possessors of this source code are hereby granted a nonexclusive, royalty-free copyright license to use this code in individual and commercial software. </p>
<p> Any use of this source code must include, in the user documentation and internal comments to the code, notices to the end user as follows: </p>
<p> Copyright 1993-2003 NVIDIA, Corporation. All rights reserved. </p>
<p> NVIDIA, CORPORATION MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOURCE CODE FOR ANY PURPOSE. IT IS PROVIDED &quot;AS IS&quot; WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY KIND. NVIDIA, CORPORATION DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOURCE CODE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT SHALL NVIDIA, CORPORATION BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOURCE CODE. </p>
<p> U.S. Government End Users. This source code is a &quot;commercial item,&quot; as that term is defined at 48 C.F.R. 2.101 (OCT 1995), consisting of &quot;commercial computer software&quot; and &quot;commercial computer software documentation,&quot; as such terms are used in 48 C.F.R. 12.212 (SEPT 1995) and is provided to the U.S. Government only as a commercial end item. Consistent with 48 C.F.R. 12.212 and 48 C.F.R. 227.7202-1 through 227.7202-4 (JUNE 1995), all U.S. Government End Users acquire the source code with only those rights set forth herein.</p>
