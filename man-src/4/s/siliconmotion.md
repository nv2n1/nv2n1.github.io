---
title: "siliconmotion(4)"
name: "siliconmotion"
section: "4"
letter: "s"
url: "/docs/linux/man/4-siliconmotion/"
description: "siliconmotion – Silicon Motion video driver"
---

<p>siliconmotion &#8211; Silicon Motion video driver</p>
<h2>Synopsis</h2>
<p><code>Section &#34;Device&#34;</code><br />
 <code> Identifier &#34;</code><i>devname</i><code>&#34;</code><br />
 <code> Driver &#34;siliconmotion&#34;</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
 &nbsp;<wbr>&nbsp;<wbr>[ <code>Option</code> &quot;optionname&quot; [&quot;optionvalue&quot;]]<br />
 <code>EndSection</code></p>
<h2>Description</h2>
<p><code>siliconmotion </code> is an Xorg driver for Silicon Motion based video cards. The driver is fully accelerated, and provides support for the following framebuffer depths: 8, 16, and 24. All visual types are supported for depth 8, and TrueColor visuals are supported for the other depths.</p>
<h2>Supported Hardware</h2>
<p>The <code>siliconmotion</code> driver supports PCI and AGP video cards based on the following Silicon Motion chips:</p>
<dl>
<dt><code>Lynx</code></p>
<dd>SM910</p>
<dt><code>LynxE</code></p>
<dd>SM810</p>
<dt><code>Lynx3D</code></p>
<dd>SM820</p>
<dt><code>LynxEM</code></p>
<dd>SM710</p>
<dt><code>LynxEM+</code></p>
<dd>SM712</p>
<dt><code>Lynx3DM</code></p>
<dd>SM720</p>
<dt><code>Cougar3DR</code></p>
<dd>SM731</p>
<dt><code>MSOC</code></p>
<dd>SM501,SM502</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. All options names are case and white space insensitive when parsed by the server, for example, &quot;lynxe&quot; and &quot;LynxE&quot; are equivalent. </p>
<p> Multihead mode configuration is done through the RandR1.2 interface (see <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) and <a href="/docs/linux/man/1-xrandr/">xrandr</a>(1) for further information). Hardware accelerated screen rotation and framebuffer resizing are only supported with the <code>EXA</code> acceleration architecture (see the <code>AccelMethod</code> option below). </p>
<p> The driver auto-detects the chipset type, but the following <code>ChipSet</code> names may optionally be specified in the config file <code>&#34;Device&#34;</code> section, and will override the auto-detection: </p>
<dl>
<dd>&quot;lynx&quot;, &quot;lynxe&quot;, &quot;lynx3d&quot;, &quot;lynxem&quot;, &quot;lynxem+&quot;, &quot;lynx3dm&quot;, &quot;cougar3dr&quot;, &quot;msoc&quot;.</dl>
<p> The following Cursor <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;HWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable the HW cursor. Default: on.</p>
<dt><code>Option &#34;SWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Inverse of &quot;HWCursor&quot;. Default: off. </p>
</dl>
<p> The following display <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;VideoKey&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set the video color key. Default: a little off full blue.</p>
<dt><code>Option &#34;ByteSwap&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Turn on byte swapping for capturing using SMI demo board. Default: off.</p>
<dt><code>Option &#34;Interlaced&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Turn on interlaced video capturing. Default: off.</p>
<dt><code>Option &#34;UseBIOS&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Use the BIOS to set the modes. This is used for custom panel timings. Default: off for SM72x and SM5xx, otherwise on.</p>
<dt><code>Option &#34;Dualhead&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable dualhead mode. Currently not all chips are supported and hardware video overlay (XV) support may have some limitations. Default: off.</p>
<dt><code>Option &#34;PanelSize&#34; &#34;</code><i>width</i><code>x</code><i>height</i><code>&#34;</code></p>
<dd>Override LCD panel dimension autodetection.</p>
<dt><code>Option &#34;UseFBDev&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Don&#8217;t actually program the hardware mode registers, but leave it as set by the operating system. Only available on MSOC chips. Default: off.</p>
<dt><code>Option &#34;CSCVideo&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>CSC video uses color space conversion to render video directly to the framebuffer, without using an overlay. Only available on MSOC chips. Default: on.</dl>
<p> The following video memory <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;mclk&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Sets the memory clock. You must specify the units. For example <i>50Mhz</i> is the same as <i>50000Khz</i> or <i>50000000Hz</i>. On MSOC chips this is the main clock source for all functional blocks, such as the 2D engine, GPIO, Video Engine, and DMA Engine. This option is only used for debugging purposes on MSOC chips. Default: probe the memory clock value, and use it at server start.</p>
<dt><code>Option &#34;mxclk&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Sets the memory clock. You must specify the units. For example <i>50Mhz</i> is the same as <i>50000Khz</i> or <i>50000000Hz</i>. Clock source for the local SDRAM controller. This option is only available on MSOC chips and used only for debugging purposes. Default: probe the memory clock value, and use it at server start.</dl>
<p> The following acceleration and graphics engine <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;NoAccel&#34;</code></p>
<dd>Disable acceleration. Very useful for determining if the driver has problems with drawing and acceleration routines. This is the first option to try if your server runs but you see graphic corruption on the screen. Using it decreases performance, as it uses software emulation for drawing operations the video driver can accelerate with hardware. Default: acceleration is enabled.</p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Chooses between available acceleration architectures. Valid options are <code>XAA</code> and <code>EXA.</code> XAA is the traditional acceleration architecture and support for it is very stable. EXA is a newer acceleration architecture with better performance for the Render and Composite extensions, but the rendering code for it is newer and possibly unstable. The default is <code>XAA.</code> </p>
</dl>
<p> The following PCI bus <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;PciBurst&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>will enable PCI burst mode. This should work on all but a few broken PCI chipsets, and will increase performance. Default: on.</p>
<dt><code>Option &#34;PciRetry&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>will allow the driver to rely on PCI Retry to program the registers. <code>PciBurst</code> must be enabled for this to work. This will increase performance, especially for small fills/blits, because the driver does not have to poll the card before sending it commands to make sure it is ready. It should work on most recent PCI chipsets. Default: value of <i>PciBurst</i> option. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
<h2>Support</h2>
<p>For assistance with this driver, or Xorg in general, check the web site at <a rel="nofollow" href="http://www.x.org/.">http://www.x.org/.</a> If you find a problem with Xorg or have a question not answered in the FAQ please use our bug report form available on the web site or send mail to xorg [at] lists.freedesktop.org. When reporting problems with the driver send as much detail as possible, including chipset type, a server output log, and operating system specifics.</p>
<h2>Authors</h2>
<p>Kevin Brosius, Matt Grossman, Harald Koenig, Sebastien Marineau, Mark Vojkovich, Frido Garritsen, Corvin Zahn.</p>
