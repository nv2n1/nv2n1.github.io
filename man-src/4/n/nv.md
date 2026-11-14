---
title: "nv(4)"
name: "nv"
section: "4"
letter: "n"
url: "/docs/linux/man/4-nv/"
description: "nv – NVIDIA video driver"
---

<p>nv &#8211; NVIDIA video driver</p>
<h2>Synopsis</h2>
<pre><code>Section N'34'DeviceN'34'</code>
<code> Identifier N'34'</code><i>devname</i><code>N'34'</code>
<code> Driver N'34'nvN'34'</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>nv </code> is an Xorg driver for NVIDIA video cards. The driver supports 2D acceleration and provides support for the following framebuffer depths: 8, 15, 16 (except Riva128) and 24. All visual types are supported for depth 8, TrueColor and DirectColor visuals are supported for the other depths with the exception of the Riva128 which only supports TrueColor in the higher depths. </p>
<h2>Supported Hardware</h2>
<p>The <code>nv</code> driver supports PCI, PCI-Express and AGP video cards based on the following NVIDIA chips:</p>
<dl>
<dt><code>RIVA 128</code></p>
<dd>NV3</p>
<dt><code>RIVA TNT</code></p>
<dd>NV4</p>
<dt><code>RIVA TNT2</code></p>
<dd>NV5</p>
<dt><code>GeForce 256, Quadro </code></p>
<dd>NV10</p>
<dt><code>GeForce2, Quadro2</code></p>
<dd>NV11 &amp; NV15</p>
<dt><code>GeForce3, Quadro DCC</code></p>
<dd>NV20</p>
<dt><code>nForce, nForce2</code></p>
<dd>NV1A, NV1F</p>
<dt><code>GeForce4, Quadro4</code></p>
<dd>NV17, NV18, NV25, NV28</p>
<dt><code>GeForce FX, Quadro FX</code></p>
<dd>NV30, NV31, NV34, NV35, NV36, NV37, NV38</p>
<dt><code>GeForce 6XXX</code></p>
<dd>NV40, NV41, NV43, NV44, NV45, C51</p>
<dt><code>GeForce 7XXX</code></p>
<dd>G70, G71, G72, G73</p>
<dt><code>GeForce 8XXX, GeForce 9XXX</code></p>
<dd>G80, G84, G86, G92, G94, G96, G98</p>
<dt><code>GeForce GTX</code></p>
<dd>GT200</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the chipset type and the amount of video memory present for all chips. </p>
<p> The following driver <code>Options</code> are supported for pre-G80 hardware:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;HWCursorN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable the HW cursor. Default: on.</p>
<dt><code>Option N&#8217;34&#8217;NoAccelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option N&#8217;34&#8217;UseFBDevN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable use of an OS-specific fb interface (and is not supported on all OSs). See <a href="/docs/linux/man/4-fbdevhw/">fbdevhw</a>(4) for further information. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;CrtcNumberN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>Many graphics cards with NVIDIA chips have two video outputs. The driver attempts to autodetect which one the monitor is connected to. In the case that autodetection picks the wrong one, this option may be used to force usage of a particular output. The options are &quot;0&quot; or &quot;1&quot;. Default: autodetected.</p>
<dt><code>Option N&#8217;34&#8217;DualheadN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enables simple VBE-based dual head mode. This sets the same resolution on both outputs and lays them out side-by-side. The screens will be panned together as one big metamode if the virtual desktop is larger than both screens combined.</p>
<dt><code>Option N&#8217;34&#8217;FlatPanelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>The driver usually can autodetect the presence of a digital flat panel. In the case that this fails, this option can be used to force the driver to treat the attached device as a digital flat panel. With this driver, a digital flat panel will work only if it was POSTed by the BIOS, that is, the computer must have booted to the panel. If you have a dual head card you may also need to set the option CrtcNumber described above. Default: autodetected.</p>
<dt><code>Option N&#8217;34&#8217;FPDitherN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Many digital flat panels (particularly ones on laptops) have only 6 bits per component color resolution. This option tells the driver to dither from 8 bits per component to 6 before the flat panel truncates it. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;FPScaleN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Supported only on GeForce4 and newer chips, this option tells to the driver to scale lower resolutions up to the flat panel&#8217;s native resolution. Default: on.</p>
<dt><code>Option N&#8217;34&#8217;RotateN&#8217;34&#8217; N&#8217;34&#8217;CWN&#8217;34&#8217;</code></p>
<dd>
<dt><code>Option N&#8217;34&#8217;RotateN&#8217;34&#8217; N&#8217;34&#8217;CCWN&#8217;34&#8217;</code></p>
<dd>Rotate the display clockwise or counterclockwise. This mode is unaccelerated. Default: no rotation. </p>
<p> Note: The Resize and Rotate extension will be disabled if the Rotate &quot;CW&quot; or Rotate &quot;CCW&quot; options are used.</p>
<dt><code>Option N&#8217;34&#8217;RotateN&#8217;34&#8217; N&#8217;34&#8217;RandRN&#8217;34&#8217;</code></p>
<dd>Enable rotation of the screen using the Resize and Rotate extension. This mode is unaccelerated. Default: no rotation support.</p>
<dt><code>Option N&#8217;34&#8217;ShadowFBN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. Default: off.</dl>
<p> The following driver <code>Options</code> are available for G80 and higher:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;HWCursorN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable the hardware cursor. Default: on.</p>
<dt><code>Option N&#8217;34&#8217;NoAccelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option N&#8217;34&#8217;AccelMethodN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>Choose acceleration architecture, either N&#8217;34&#8217;XAAN&#8217;34&#8217; or N&#8217;34&#8217;EXAN&#8217;34&#8217;. XAA is the old but stable architecture. EXA is newer and supports resizing the desktop larger than it started out with RandR 1.2. If you choose to use EXA, you might also consider setting <code>Option N&#8217;34&#8217;MigrationHeuristicN&#8217;34&#8217; N&#8217;34&#8217;greedyN&#8217;34&#8217;</code> to improve performance. Default: XAA.</p>
<dt><code>Option N&#8217;34&#8217;FPDitherN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Enable or disable flat panel dithering by default. Dithering can also be enabled or disabled using the RandR 1.2 N&#8217;34&#8217;ditherN&#8217;34&#8217; output property. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;AllowDualLinkModesN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Allow validation of dual-link DVI modes. Not all GPUs are configured at boot time to be able to handle dual-link modes, so they are disabled by default.</dl>
<p> The following RandR 1.2 properties are available for flat panels on G80 and higher GPUs:</p>
<dl>
<dt><code>dither</code></p>
<dd>Enable or disable flat panel dithering. Valid values: <code>0</code> (off), <code>1</code> (on).</p>
<dt><code>scale</code></p>
<dd>Control how the image is scaled to fit the flat panel. Note that some flat panels perform their own scaling, overriding this option. N&#8217;34&#8217;<code>off</code>N&#8217;34&#8217; is not valid for laptop flat panels (LVDS). Valid values: N&#8217;34&#8217;<code>off</code>N&#8217;34&#8217;, N&#8217;34&#8217;<code>aspect</code>N&#8217;34&#8217;, N&#8217;34&#8217;<code>fill</code>N&#8217;34&#8217;, and N&#8217;34&#8217;<code>center</code>N&#8217;34&#8217;. Default: N&#8217;34&#8217;<code>aspect</code>N&#8217;34&#8217;.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrandr/">xrandr</a>(1)</p>
<h2>Authors</h2>
<p>Authors include: David McKay, Jarno Paananen, Chas Inman, Dave Schmenk, Mark Vojkovich, Aaron Plattner</p>
<h2>Copyright</h2>
<p>Copyright (c) 2003 &#8211; 2008 NVIDIA, Corporation </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
