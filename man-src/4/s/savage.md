---
title: "savage(4)"
name: "savage"
section: "4"
letter: "s"
url: "/docs/linux/man/4-savage/"
description: "savage – S3 Savage video driver"
---

<p>savage &#8211; S3 Savage video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;savage&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>savage </code> is an Xorg driver for the S3 Savage family video accelerator chips. 2D, 3D, and Xv acceleration is supported on all chips except the Savage2000 (2D only). Dualhead operation is supported on MX, IX, and SuperSavage chips. The <code>savage</code> driver supports PCI and AGP boards with the following chips:</p>
<dl>
<dt><code>Savage3D</code></p>
<dd>(8a20 and 8a21) (2D, 3D)</p>
<dt><code>Savage4</code></p>
<dd>(8a22) (2D, 3D)</p>
<dt><code>Savage2000</code></p>
<dd>(9102) (2D only)</p>
<dt><code>Savage/MX</code></p>
<dd>(8c10 and 8c11) (2D, 3D, Dualhead)</p>
<dt><code>Savage/IX</code></p>
<dd>(8c12 and 8c13) (2D, 3D, Dualhead)</p>
<dt><code>SuperSavage/MX</code></p>
<dd>(8c22, 8c24, and 8c26) (2D, 3D, Dualhead)</p>
<dt><code>SuperSavage/IX</code></p>
<dd>(8c2a, 8c2b, 8c2c, 8c2d, 8c2e, and 8c2f) (2D, 3D, Dualhead)</p>
<dt><code>ProSavage PM133</code></p>
<dd>(8a25) (2D, 3D)</p>
<dt><code>ProSavage KM133</code></p>
<dd>(8a26) (2D, 3D)</p>
<dt><code>Twister (ProSavage PN133)</code></p>
<dd>(8d01) (2D, 3D)</p>
<dt><code>TwisterK (ProSavage KN133)</code></p>
<dd>(8d02) (2D, 3D)</p>
<dt><code>ProSavage DDR</code></p>
<dd>(8d03) (2D, 3D)</p>
<dt><code>ProSavage DDR-K</code></p>
<dd>(8d04) (2D, 3D)</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;HWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;SWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>These two options interact to specify hardware or software cursor. If the SWCursor option is specified, any HWCursor setting is ignored. Thus, either &#34;HWCursor off&#34; or &#34;SWCursor on&#34; will force the use of the software cursor. On Savage/MX and Savage/IX chips which are connected to LCDs, a software cursor will be forced, because the Savage hardware cursor does not correctly track the automatic panel expansion feature. Default: hardware cursor.</p>
<dt><code>Option &#34;NoAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable acceleration. Default: acceleration is enabled.</p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Chooses between available acceleration architectures. Valid options are <code>XAA</code> and <code>EXA.</code> XAA is the traditional acceleration architecture and support for it is very stable. EXA is a newer acceleration architecture with better performance for the Render and Composite extensions, but the rendering code for it is newer and possibly unstable. The default is <code>XAA.</code></p>
<dt><code>Option &#34;Rotate&#34; &#34;CW&#34;</code></p>
<dd>
<dt><code>Option &#34;Rotate&#34; &#34;CCW&#34;</code></p>
<dd>Rotate the desktop 90 degrees clockwise or counterclockwise. This option forces the ShadowFB option on, and disables acceleration and the RandR extension. Default: no rotation.</p>
<dt><code>Option &#34;ShadowFB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the shadow framebuffer layer. This option disables acceleration. Default: off.</p>
<dt><code>Option &#34;LCDClock&#34; &#34;</code><i>frequency</i><code>&#34;</code></p>
<dd>Override the maximum dot clock. Some LCD panels produce incorrect results if they are driven at too fast of a frequency. If UseBIOS is on, the BIOS will usually restrict the clock to the correct range. If not, it might be necessary to override it here. The <code>frequency</code> parameter may be specified as an integer in Hz (135750000), or with standard suffixes like &quot;k&quot;, &quot;kHz&quot;, &quot;M&quot;, or &quot;MHz&quot; (as in 135.75MHz).</p>
<dt><code>Option &#34;CrtOnly&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option disables output to the LCD and enables output to the CRT port only. It is useful on laptops if you only want to use the CRT port or to force the CRT output only on desktop cards that use mobile chips. Default: auto-detect active outputs</p>
<dt><code>Option &#34;UseBIOS&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable use of the video BIOS to change modes. Ordinarily, the <code>savage </code> driver tries to use the video BIOS to do mode switches. This generally produces the best results with the mobile chips (/MX and /IX), since the BIOS knows how to handle the critical but unusual timing requirements of the various LCD panels supported by the chip. To do this, the driver searches through the BIOS mode list, looking for the mode which most closely matches the xorg.conf mode line. Some purists find this scheme objectionable. If you would rather have the <code>savage</code> driver use your mode line timing exactly, turn off the UseBios option. <code>Note:</code> Use of the BIOS is required for dualhead operation. Default: on (use the BIOS).</p>
<dt><code>Option &#34;IgnoreEDID&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Do not use EDID data for mode validation, but DDC is still used for monitor detection. This is different from NoDDC option.<br />
 The default value is <code>off.</code></p>
<dt><code>Option &#34;ShadowStatus&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enables the use of a shadow status register. There is a chip bug in the Savage graphics engine that can cause a bus lock when reading the engine status register under heavy load, such as when scrolling text or dragging windows. The bug affects about 4% of all Savage users without DRI and a large fraction of users with DRI. If your system hangs regularly while scrolling text or dragging windows, try turning this option on. This uses an alternate method of reading the engine status which is slightly more expensive, but avoids the problem. When DRI is enabled then the default is &#34;on&#34; (use shadow status), otherwise the default is &#34;off&#34; (use normal status register).</p>
<dt><code>Option &#34;DisableCOB&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disables the COB (Command Overflow Buffer) on savage4 and newer chips. There is supposedly a HW cache coherency problem on certain savage4 and newer chips that renders the COB useless. If you are having problems with 2D acceleration you can disable the COB, however you will lose some performance. 3D acceleration requires the COB to work. This option only applies to Savage4 and newer chips. Default: &#34;off&#34; (use COB).</p>
<dt><code>Option &#34;BCIforXv&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Use the BCI to copy and reformat Xv pixel data. Using the BCI for Xv causes graphics artifacts on some chips. This option only applies to Savage4 and prosavage/twister chips. On some combinations of chipsets and video players, BCI formatting might actually be slower than software formatting (&#34;AGPforXv&#34; might help in this case). BCI formatting can only be used on video data with a width that is a multiple of 16 pixels (which is the vast majority of videos). Other widths are handled through software formatting. Default: on for prosavage and twister (use BCI for Xv); off for savage4 (do not use the BCI for Xv).</p>
<dt><code>Option &#34;AGPforXv&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Instructs the BCI Xv pixel formatter to use AGP memory as a scratch buffer. Ordinarily the BCI formatter uses a an area in framebuffer memory to hold YV12 planar data to be converted for display. This requires a somewhat expensive upload of YV12 data to framebuffer memory. The &#34;AGPforXv&#34; option causes the BCI formatter to place the YV12 data in AGP memory instead, which can be uploaded faster than the framebuffer. Use of this option cuts upload overhead by 25% according to benchmarks. This option also smooths out most of the shearing present when using BCI for pixel conversion. Currently this option is <code>experimental</code> and is disabled by default. Video width restrictions that apply to &#34;BCIforXv&#34; also apply here. Only valid when &#34;DRI&#34; and &#34;BCIforXv&#34; are both active, and only on AGP chipsets. Default: &#34;off&#34;.<br />
 If &#34;AccelMethod&#34; is set to &#34;EXA&#34; and &#34;AGPforXv&#34; is enabled, then the driver will also attempt to reuse the AGP scratch buffer for UploadToScreen acceleration.</p>
<dt><code>Option &#34;AGPMode&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set AGP data transfer rate. (used only when DRI is enabled)<br />
 1 &#8212; x1 (default)<br />
 2 &#8212; x2<br />
 4 &#8212; x4<br />
 others &#8212; invalid</p>
<dt><code>Option &#34;AGPSize&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The amount of AGP memory that will allocated for DMA and textures in MB. Valid sizes are 4, 8, 16, 32, 64, 128 and 256. The default is 16MB.</p>
<dt><code>Option &#34;DmaMode&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>This option influences in which way DMA (direct memory access) is used by the kernel and 3D drivers.<br />
 Any &#8212; Try command DMA first, then vertex DMA (default)<br />
 Command &#8212; Only use command DMA or don&#8217;t use DMA at all<br />
 Vertex &#8212; Only use vertex DMA or don&#8217;t use DMA at all<br />
 None &#8212; Disable DMA<br />
 Command and vertex DMA cannot be enabled at the same time. Which DMA mode is actually used in the end also depends on the DRM version (only &gt;= 2.4.0 supports command DMA) and the hardware (Savage3D/MX/IX doesn&#8217;t support command DMA).</p>
<dt><code>Option &#34;DmaType&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>The type of memory that will be used by the 3D driver for DMA (direct memory access).<br />
 PCI &#8212; PCI memory (default on PCI cards)<br />
 AGP &#8212; AGP memory (default on AGP cards)<br />
 &#34;AGP&#34; only works if you have an AGP card.</p>
<dt><code>Option &#34;BusType&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>The bus type that will be used to access the graphics card.<br />
 PCI &#8212; PCI bus (default)<br />
 AGP &#8212; AGP bus<br />
 &#34;AGP&#34; only works if you have an AGP card. If you choose &#34;PCI&#34; on an AGP card the AGP bus speed is not set and no AGP aperture is allocated. This implies <code>DmaType</code> &#34;PCI&#34;.</p>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable DRI support. This option allows you to enable or disable the DRI. Default: &#34;on&#34; (enable DRI).</dl>
<h2>Files</h2>
<p>savage_drv.o</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include Tim Roberts (timr [at] probo.com) and Ani Joshi (ajoshi [at] unixbox.com) for this version, and Tim Roberts and S. Marineau for the original driver from which this was derived.</p>
