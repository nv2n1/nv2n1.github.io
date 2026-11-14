---
title: "s3virge(4)"
name: "s3virge"
section: "4"
letter: "s"
url: "/docs/linux/man/4-s3virge/"
description: "s3virge – S3 ViRGE video driver"
---

<p>s3virge &#8211; S3 ViRGE video driver</p>
<h2>Synopsis</h2>
<p><code>Section N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code><br />
 <code> Identifier N&#8217;34&#8217;</code><i>devname</i><code>N&#8217;34&#8217;</code><br />
 <code> Driver N&#8217;34&#8217;s3virgeN&#8217;34&#8217;</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
 &nbsp;<wbr>&nbsp;<wbr>[ <code>Option</code> &quot;optionname&quot; [&quot;optionvalue&quot;]]<br />
 <code>EndSection</code></p>
<h2>Description</h2>
<p><code>s3virge </code> is an Xorg driver for S3 based video cards. The driver is fully accelerated, and provides support for the following framebuffer depths: 8, 15, 16, and 24. All visual types are supported for depth 8, and TrueColor visuals are supported for the other depths. XVideo hardware up scaling is supported in depth 16 and 24 on the DX, GX, GX2, MX, MX+, and Trio3D/2X. Doublescan modes are supported and tested in depth 8 and 16 on DX, but disable XVideo. Doublescan modes on other chipsets are untested.</p>
<h2>Supported Hardware</h2>
<p>The <code>s3virge</code> driver supports PCI and AGP video cards based on the following S3 chips:</p>
<dl>
<dt><code>ViRGE</code></p>
<dd>86C325</p>
<dt><code>ViRGE VX</code></p>
<dd>86C988</p>
<dt><code>ViRGE DX</code></p>
<dd>86C375</p>
<dt><code>ViRGE GX</code></p>
<dd>86C385</p>
<dt><code>ViRGE GX2</code></p>
<dd>86C357</p>
<dt><code>ViRGE MX</code></p>
<dd>86C260</p>
<dt><code>ViRGE MX+</code></p>
<dd>86C280</p>
<dt><code>Trio 3D</code></p>
<dd>86C365</p>
<dt><code>Trio 3D/2X</code></p>
<dd>86C362, 86C368</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. All options names are case and white space insensitive when parsed by the server, for example, &quot;virge vx&quot; and &quot;VIRGEvx&quot; are equivalent. </p>
<p> The driver auto-detects the chipset type, but the following <code>ChipSet</code> names may optionally be specified in the config file <code>N&#8217;34&#8217;DeviceN&#8217;34&#8217;</code> section, and will override the auto-detection: </p>
<dl>
<dd>&quot;virge&quot;, &quot;86c325&quot;, &quot;virge vx&quot;, &quot;86c988&quot;, &quot;virge dx&quot;, &quot;86c375&quot;, &quot;virge gx&quot;, &quot;86c385&quot;, &quot;virge gx2&quot;, &quot;86c357&quot;, &quot;virge mx&quot;, &quot;86c260&quot;, &quot;virge mx+&quot;, &quot;86c280&quot;, &quot;trio 3d&quot;, &quot;86c365&quot;, &quot;trio 3d/2x&quot;, &quot;86c362&quot;, &quot;86c368&quot;.</dl>
<p> The following Cursor <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;HWCursorN&#8217;34&#8217; [N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;]</code></p>
<dd>Enable or disable the HW cursor. Default: on.</p>
<dt><code>Option N&#8217;34&#8217;SWCursorN&#8217;34&#8217; [N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;]</code></p>
<dd>Inverse of &quot;HWCursor&quot;. Default: off. </p>
</dl>
<p> The following display <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;ShadowFBN&#8217;34&#8217; [N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;]</code></p>
<dd>Use shadow framebuffer. Disables HW acceleration. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;RotateN&#8217;34&#8217; N&#8217;34&#8217;</code>cw<code> | </code>ccw<code>N&#8217;34&#8217;</code></p>
<dd>Rotate the screen CW &#8211; clockwise or CCW &#8211; counter clockwise. Disables HW Acceleration and HW Cursor, uses ShadowFB. Default: no rotation.</p>
<dt><code>Option N&#8217;34&#8217;XVideoN&#8217;34&#8217; [N&#8217;34&#8217;</code>boolean<code>N&#8217;34&#8217;]</code></p>
<dd>Disable XVideo support by using the off option. This changes FIFO settings which prevent screen noise for high-res modes. Default: on </p>
</dl>
<p> The following video memory <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;slow_edodramN&#8217;34&#8217;</code></p>
<dd>Switch the standard ViRGE to 2-cycle edo mode. Try this if you encounter pixel corruption on the ViRGE. Using this option will cause a large decrease in performance. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;fpm_vramN&#8217;34&#8217;</code></p>
<dd>Switch the ViRGE/VX to fast page mode vram mode. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;slow_dram </code>|<code> fast_dramN&#8217;34&#8217;</code></p>
<dd>Change Trio 3D and 3D/2X memory options. Default: Use BIOS defaults.</p>
<dt><code>Option N&#8217;34&#8217;early_ras_precharge </code>|<code> late_ras_prechargeN&#8217;34&#8217;</code></p>
<dd>adjust memory parameters. One of these will us the same settings as your video card defaults, and using neither in the config file does the same. Default: none.</p>
<dt><code>Option N&#8217;34&#8217;set_mclkN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>sets the memory clock, where <i>integer</i> is in kHz, and <i>integer</i> &lt;= 100000. Default: probe the memory clock value, and use it at server start.</p>
<dt><code>Option N&#8217;34&#8217;set_refclkN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>sets the ref clock for ViRGE MX, where <i>integer</i> is in kHz. Default: probe the memory clock value, and use it at server start. </p>
</dl>
<p> The following acceleration and graphics engine <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;NoAccelN&#8217;34&#8217;</code></p>
<dd>Disable acceleration. Very useful for determining if the driver has problems with drawing and acceleration routines. This is the first option to try if your server runs but you see graphic corruption on the screen. Using it decreases performance, as it uses software emulation for drawing operations the video driver can accelerate with hardware. Default: acceleration is enabled.</p>
<dt><code>Option N&#8217;34&#8217;UseFBN&#8217;34&#8217;</code></p>
<dd>There are two framebuffer rendering methods. fb and cfb. Both are available in the driver. fb is the newer and default method. To switch back to cfb use this option with no, off or other negative parameter. Default: on.</p>
<dt><code>Option N&#8217;34&#8217;fifo_aggressive </code>|<code> fifo_moderate </code>|<code> fifo_conservativeN&#8217;34&#8217;</code></p>
<dd>alter the settings for the threshold at which the pixel FIFO takes over the internal memory bus to refill itself. The smaller this threshold, the better the acceleration performance of the card. You may try the fastest setting (<code>fifo_aggressive</code>) and move down if you encounter pixel corruption. The optimal setting will probably depend on dot-clock and on color depth. Note that specifying any of these options will also alter other memory settings which may increase performance, so trying <code>fifo_conservative</code> will in most cases be a slight benefit (this uses the chip defaults). If pixel corruption or transient streaking is observed during drawing operations then removing any fifo options is recommended. Default: none. </p>
</dl>
<p> The following PCI bus <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;pci_burstN&#8217;34&#8217; [N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;]</code></p>
<dd>will enable PCI burst mode. This should work on all but a few broken PCI chipsets, and will increase performance. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;pci_retryN&#8217;34&#8217; [N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;]</code></p>
<dd>will allow the driver to rely on PCI Retry to program the ViRGE registers. <code>pci_burst</code> must be enabled for this to work. This will increase performance, especially for small fills/blits, because the driver does not have to poll the ViRGE before sending it commands to make sure it is ready. It should work on most recent PCI chipsets. Default: off.</dl>
<p> The following ViRGE MX LCD <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;lcd_centerN&#8217;34&#8217;</code></p>
<dd>
<dt><code>Option N&#8217;34&#8217;set_lcdclkN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>allows setting the clock for a ViRGE MX LCD display. <i>integer</i> is in Hz. Default: use probed value. </p>
</dl>
<p> The following additional <code>Options</code> are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;ShowCacheN&#8217;34&#8217; [N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;]</code></p>
<dd>Enable or disable viewing offscreen cache memory. A development debug option. Default: off.</p>
<dt><code>Option N&#8217;34&#8217;mx_cr3a_fixN&#8217;34&#8217; [N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;]</code></p>
<dd>Enable or disable a cr3a fix added for ViRGE MX. Default: on. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
<h2>Known Bugs</h2>
<p>The VideoRam generic driver parameter is presently ignored by the s3virge driver. On PPC this is reported to cause problems for 2M cards, because they may autodetect as 4M.</p>
<h2>Support</h2>
<p>For assistance with this driver, or XFree86 in general, check the XFree86 web site at <a rel="nofollow" href="http://www.xfree86.org.">http://www.xfree86.org.</a> A FAQ is available on the web site at <a rel="nofollow" href="http://www.xfree86.org/FAQ/.">http://www.xfree86.org/FAQ/.</a> If you find a problem with XFree86 or have a question not answered in the FAQ please use our bug report form available on the web site or send mail to XFree86 [at] XFree86.org. When reporting problems with the driver send as much detail as possible, including chipset type, a server output log, and operating system specifics.</p>
<h2>Authors</h2>
<p>Kevin Brosius, Matt Grossman, Harald Koenig, Sebastien Marineau, Mark Vojkovich.</p>
