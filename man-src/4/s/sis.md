---
title: "sis(4)"
name: "sis"
section: "4"
letter: "s"
url: "/docs/linux/man/4-sis/"
description: "sis – SiS and XGI video driver"
---

<p>sis &#8211; SiS and XGI video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;sis&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>sis</code> is an Xorg driver for SiS (Silicon Integrated Systems) and XGI video chips. The driver is accelerated and provides support for colordepths of 8, 16 and 24 bpp. XVideo, Render and other extensions are supported as well.</p>
<h2>Supported Hardware</h2>
<p>The <code>sis</code> driver supports PCI, AGP and PCIe video cards based on the following chipsets: </p>
<p> <code>SiS5597/5598</code> <code>SiS530/620</code> <code>SiS6326/AGP/DVD</code> <code>SiS300/305</code> <code>SiS540</code> <code>SiS630/730</code> <code>SiS315/E/H/PRO</code> <code>SiS550/551/552</code> <code>SiS650/651/661/741</code> <code>SiS330 (Xabre)</code> <code>SiS760/761</code> <code>XGI Volari V3/V5/V8</code> <code>XGI Volari Z7</code> </p>
<p> In the following text, the following terms are used: </p>
<p> <code>old series</code> for SiS5597/5598, 530/620 and 6326/AGP/DVD </p>
<p> <code>300 series</code> for SiS300/305, 540 and 630/730 </p>
<p> <code>315/330/340 series</code> for SiS315, 55x, 330, 661/741/76x (plus M, FX, MX, GX variants thereof), 340 and all XGI chips.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> Detailed information on all supported options can be obtained at <a rel="nofollow" href="http://www.winischhofer.eu/linuxsisvga.shtml">http://www.winischhofer.eu/linuxsisvga.shtml</a> </p>
<p> This manpage only covers a subset of the supported options. </p>
<p> <i>1. For all supported chipsets</i> </p>
<p> The following driver <code>options</code> are supported on all chipsets:</p>
<dl>
<dt><code>Option &#34;NoAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable 2D acceleration. Default: acceleration is enabled.</p>
<dt><code>Option &#34;HWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable the HW cursor. Default: HWCursor is on.</p>
<dt><code>Option &#34;SWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>The opposite of HWCursor. Default: SWCursor is off.</p>
<dt><code>Option &#34;Rotate&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Rotate the display clockwise (&quot;CW&quot;) or counter-clockwise (&quot;CCW&quot;). This mode is unaccelerated. Using this option disables XVideo and the Resize and Rotate extension (RandR). Rotation and reflection (see below) are mutually exclusive. Default: no rotation.</p>
<dt><code>Option &#34;Reflect&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Reflect (mirror) the display horizontally (&quot;X&quot;), vertically (&quot;Y&quot;) or both (&quot;XY&quot;). This mode is unaccelerated. Using this option disables XVideo and the Resize and Rotate extension (RandR). Rotation (see above) and reflection are mutually exclusive. Default: no reflection.</p>
<dt><code>Option &#34;CRT1Gamma&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable gamma correction. (On the 300 and 315/330/340 series, this option only affects CRT1 output). Default: Gamma correction is enabled.</dl>
<p> <i>2. Old series specific information</i> </p>
<p> The driver will auto-detect the amount of video memory present for all these chips, but in the case of the 6326, it will limit the memory size to 4MB. This is because the 6326&#8217;s 2D engine can only address 4MB. The remaining memory seems to be intended for 3D texture data, since only the 3D engine can address RAM above 4MB. However, you can override this limitation using the <code>&#34;VideoRAM&#34;</code> option in the Device section if your board has more than 4MB and you need to use it. However, 2D acceleration, XVideo and the HWCursor will be disabled in this case. </p>
<p> For the 6326, the driver has two built-in modes for high resolutions which you should use instead of the default ones. These are named <code>&#34;SIS1280x1024-75&#34;</code> and <code>&#34;SIS1600x1200-60&#34;</code> and they will be added to the list of default modes. To use these modes, just place them in your Screen section. Example: </p>
<p> <code>Modes &#34;SIS1600x1200-60&#34; &#34;SIS1280x1024x75&#34; &#34;1024&#215;768&#34; &#8230;</code> </p>
<p> Of these modes, 1280&#215;1024 is only available at 8, 15 and 16bpp. 1600&#215;1200 is available at 8bpp only. </p>
<p> TV support for the 6326 </p>
<p> TV output is supported for the 6326. The driver will auto detect a connected TV and in this case add the following display modes to the list of available display modes: &quot;PAL800x600&quot;, &quot;PAL800x600U&quot;, &quot;PAL720x540&quot;, &quot;PAL640x480&quot;, &quot;NTSC640x480&quot;, &quot;NTSC640x480U&quot; and &quot;NTSC640x400&quot;. Use these modes like the hi-res modes described above. </p>
<p> The following driver <code>Options</code> are supported on the old series:</p>
<dl>
<dt><code>Option &#34;TurboQueue&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable TurboQueue mode. Default: off for SIS530/620, on for the others</p>
<dt><code>Option &#34;FastVram&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable FastVram mode. Enabling this sets the video RAM timing to one cycle per read operation instead of two cycles. Disabling this will set two cycles for read and write operations. Leaving this option out uses the default, which varies depending on the chipset.</p>
<dt><code>Option &#34;NoHostBus&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>(SiS5597/5598 only). Disable CPU-to-VGA host bus support. This speeds up CPU to video RAM transfers. Default: Host bus is enabled.</p>
<dt><code>Option &#34;NoXVideo&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable XV (XVideo) extension support. Default: XVideo is on.</p>
<dt><code>Option &#34;NoYV12&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable YV12 Xv support. This might me required due to hardware bugs in some chipsets. Disabling YV12 support forces Xv-aware applications to use YUV2 or XShm for video output. Default: YV12 support is on.</p>
<dt><code>Option &#34;TVStandard&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>(6326 only) Valid parameters are <code>PAL</code> or <code>NTSC.</code> The default is set by a jumper on the card.</p>
<dt><code>Option &#34;TVXPosOffset&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>(6326 only) This option allows tuning the horizontal position of the image for TV output. The range is from -16 to 16. Default: 0</p>
<dt><code>Option &#34;TVYPosOffset&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>(6326 only) This option allows tuning the vertical position of the image for TV output. The range is from -16 to 16. Default: 0</p>
<dt><code>Option &#34;SIS6326TVEnableYFilter&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>(6326 only) This option allows enabling/disabling the Y (chroma) filter for TV output.</p>
<dt><code>Option &#34;SIS6326TVAntiFlicker&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>(6326 only) This option allow enabling/disabling the anti flicker facility for TV output. Possible parameters are <code>OFF, LOW, MED, HIGH</code> or <code>ADAPTIVE.</code> By experience, <code>ADAPTIVE</code> yields the best results, hence it is the default.</dl>
<p> <i>2. 300 and 315/330/340 series specific information</i> </p>
<p> The 300 and 315/330/340 series, except the XGI Z7, feature two CRT controllers and very often come with a video bridge for controlling LCD and TV output. Hereinafter, the term <code>CRT1</code> refers to the VGA output of the chip, and <code>CRT2</code> refers to either LCD, TV or secondary VGA. Due to timing reasons, only one CRT2 output can be active at the same time. But this limitation does not apply to using CRT1 and CRT2 at the same time which makes it possible to run the driver in dual head mode. </p>
<p> The driver supports the following video bridges: </p>
<p> <code>SiS301</code> <code>SiS301B(-DH)</code> <code>SiS301C</code> <code>SiS301LV</code> <code>SiS302(E)LV</code> </p>
<p> Instead of a video bridge, some machines have a third party <code>LVDS</code> transmitter to control LCD panels, and/or a <code>Chrontel 7005</code> or <code>7019</code> for TV output. All these are supported as well. </p>
<p> About TV output </p>
<p> The driver fully supports standard (PAL, NTSC, PAL-N, PAL-M) S-video or composite output as well as high definition TV (HDTV) output via YPbPr plugs. For more information on HDTV, please consult the author&#8217;s website. </p>
<p> As regards S-video and CVBS output, the SiS301 and the Chrontel 7005 only support resolutions up to 800&#215;600. All others support resolutions up to 1024&#215;768. However, due to a hardware bug, Xvideo might be distorted on SiS video bridges if running NTSC or PAL-M at 1024&#215;768. </p>
<p> About XVideo support </p>
<p> XVideo is supported on all chipsets of both families (except the XGI Volari Z7 which lacks hardware support for video overlays). However, there are some differences in hardware features which cause limitations. The 300 series as well as the SiS55x, M650, 651, 661FX, M661FX, M661MX, 741, 741GX, M741, 76x, M76x support two video overlays. The SiS315/H/PRO, 650/740, 330, 340 and the XGI Volari V3, V5 and V8 chips support only one such overlay. On chips with two overlays, one overlay is used for CRT1, the other for CRT2. On the other chipsets, the option <code>&#34;XvOnCRT2&#34;</code> can be used to select the desired output device (CRT1 or CRT2). </p>
<p> About Merged Framebuffer support </p>
<p> Merged framebuffer mode is similar to dual head/Xinerama mode (for using two output devices of one card at the same time), but has a few advantages which make me recommend it strongly over Xinerama. Please see <a rel="nofollow" href="http://www.winischhofer.eu/linuxsisvga.shtml">http://www.winischhofer.eu/linuxsisvga.shtml</a> for detailed information. </p>
<p> About dual-head support </p>
<p> Dual head mode with or without Xinerama is fully supported, be it with one card driving two outputs, be it two cards. Note that colordepth 8 is not supported in dual head mode if run on one card with two outputs. </p>
<p> The following driver <code>Options</code> are supported on the 300 and 315/330/340 series:</p>
<dl>
<dt><code>Option &#34;NoXVideo&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable XV (XVideo) extension support. Default: XVideo is on.</p>
<dt><code>Option &#34;XvOnCRT2&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>On chipsets with only one video overlay, this option can used to bind the overlay to CRT1 ( if a monitor is detected and if this option is either unset or set to <code>false</code> ) or CRT2 ( if a CRT2 device is detected or forced, and if this option is set to <code>true</code> ). If either only CRT1 or CRT2 is detected, the driver decides automatically. In Merged Framebuffer mode, this option is ignored. Default: overlay is used on CRT1</p>
<dt><code>Option &#34;ForceCRT1&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Force CRT1 to be on of off. If a monitor is connected, it will be detected during server start. However, some old monitors are not detected correctly. In such cases, you may set this option to <code>on</code> in order to make the driver initialize CRT1 anyway. If this option is set to <code>off</code> , the driver will switch off CRT1. Default: auto-detect</p>
<dt><code>Option &#34;ForceCRT2Type&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Force display type to one of: <code>NONE</code> , <code>TV</code> , <code>SVIDEO</code> , <code>COMPOSITE</code> , <code>SVIDEO+COMPOSITE</code> , <code>SCART</code> , <code>LCD</code> , <code>VGA</code> ; <code>NONE</code> will disable CRT2. The SVIDEO, COMPOSITE, SVIDEO+COMPOSITE and SCART parameters are for SiS video bridges only and can be used to force the driver to use a specific TV output connector (if present). For further parameters, see the author&#8217;s website. Default: auto detect.</p>
<dt><code>Option &#34;CRT2Gamma&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable gamma correction for CRT2. Only supported for SiS video bridges. Default: Gamma correction for CRT2 is on.</p>
<dt><code>Option &#34;TVStandard&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Force the TV standard to either <code>PAL</code> or <code>NTSC.</code> On some machines with 630, 730 and the 315/330/340 series, <code>PALM</code> , <code>PALN</code> and <code>NTSCJ</code> are supported as well. Default: BIOS setting.</p>
<dt><code>Option &#34;TVXPosOffset&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option allows tuning the horizontal position of the image for TV output. The range is from -32 to 32. Not supported on the Chrontel 7019. Default: 0</p>
<dt><code>Option &#34;TVYPosOffset&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option allows tuning the vertical position of the image for TV output. The range is from -32 to 32. Not supported on the Chrontel 7019. Default: 0</p>
<dt><code>Option &#34;SISTVXScale&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option selects the horizontal zooming level for TV output. The range is from -16 to 16. Only supported on SiS video bridges. Default: 0</p>
<dt><code>Option &#34;SISTVYScale&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option selects the vertical zooming level for TV output in the following modes: 640&#215;480, 800&#215;600. On the 315/330/340 series, also 720&#215;480, 720&#215;576 and 768&#215;576. The range is from -4 to 3. Only supported on SiS video bridges. Default: 0</p>
<dt><code>Option &#34;CHTVOverscan&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>On machines with a Chrontel TV encoder, this can be used to force the TV mode to overscan or underscan. <code>on</code> means overscan, <code>off</code> means underscan. Default: BIOS setting.</p>
<dt><code>Option &#34;CHTVSuperOverscan&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>On machines with a Chrontel 7005 TV encoder, this option enables a super-overscan mode. This is only supported if the TV standard is PAL. Super overscan will produce an image on the TV which is larger than the viewable area.</dl>
<p> The driver supports many more options. Please see <a rel="nofollow" href="http://www.winischhofer.eu/linuxsisvga.shtml">http://www.winischhofer.eu/linuxsisvga.shtml</a> for more information. </p>
<p> <i>3. 300 series specific information</i> </p>
<p> DRI is supported on the 300 series only. On Linux, prior to kernel 2.6.3, DRI requires the kernel&#8217;s SiS framebuffer driver ( <code>sisfb</code> ). The SiS DRM kernel driver as well as the SiS DRI client driver are required in any case. </p>
<p> Sisfb, if installed and running, takes care of memory management for texture data. In order to prevent the X Server and sisfb from overwriting each other&#8217;s data, sisfb reserves an amount of video memory for the X driver. This amount can either be selected using sisfb&#8217;s mem parameter, or auto-selected depending on the amount of total video RAM available. </p>
<p> Sisfb can be used for memory management only, or as a complete framebuffer driver. If you start sisfb with a valid mode (ie you gain a graphical console), the X driver can communicate with sisfb and doesn&#8217;t require any manual configuration for finding out about the video memory it is allowed to use. </p>
<p> However, if you are running a 2.4 series Linux kernel and use sisfb for video memory management only, ie you started sisfb with mode=none and still have a text mode console, there is no communication between sisfb and the X driver. For this purpose, the</p>
<dl>
<dt><code>Option &#34;MaxXFBMem&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd></dl>
<p> exists. This option must be set to the same value as given to sisfb through its &quot;mem&quot; parameter, ie the amount of memory to use for X in kilobytes. </p>
<p> If you started sisfb without the mem argument, sisfb will reserve</p>
<dl>
<dt>12288KB if more than 16MB of total video RAM is available,</p>
<dd>
<dt>8192KB if between 12 and 16MB of video RAM is available,</p>
<dd>
<dt>4096KB in all other cases.</p>
<dd></dl>
<p> If you intend to use DRI on an integrated chipset (540, 630, 730), I recommend setting the total video memory in the BIOS setup utility to 64MB. </p>
<p> PLEASE NOTE: As of Linux 2.6.3 and under *BSD, sisfb is not required for memory management. Hence, this option is mandatory on such systems not running sisfb to decide how much memory X should reserve for DRI. If the option is omitted, DRI will have no memory assigned, and all DRI applications will quit with errors like &quot;failed to allocate Z-buffer&quot; or the like.</p>
<dl>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option allows enabling or disabling DRI. By default, DRI is on.</p>
<dt><code>Option &#34;AGPSize&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option allows selecting the amount of AGP memory to be used for DRI. The amount is to be specified in megabyte, the default is 8.</dl>
<h2>Known Bugs</h2>
<p>none.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
<p> <code><a rel="nofollow" href="http://www.winischhofer.eu/linuxsisvga.shtml">http://www.winischhofer.eu/linuxsisvga.shtml</a></code> for more information and updates</p>
<h2>Authors</h2>
<p>Author: Thomas Winischhofer. Formerly based on code by Alan Hourihane, Mike Chapman, Juanjo Santamarta, Mitani Hiroshi, David Thomas, Sung-Ching Lin, Ademar Reis.</p>
