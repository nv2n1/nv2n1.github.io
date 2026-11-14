---
title: "radeon(4)"
name: "radeon"
section: "4"
letter: "r"
url: "/docs/linux/man/4-radeon/"
description: "radeon – ATI/AMD RADEON video driver"
---

<p>radeon &#8211; ATI/AMD RADEON video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;radeon&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>radeon</code> is an Xorg driver for ATI/AMD RADEON-based video cards with the following features: </p>
<dl>
<dt>&bull;</p>
<dd>Full support for 8-, 15-, 16- and 24-bit pixel depths, and for 30-bit depth on Linux 3.16 and later;</p>
<dt>&bull;</p>
<dd>RandR 1.2 and RandR 1.3 support;</p>
<dt>&bull;</p>
<dd>Full EXA 2D acceleration;</p>
<dt>&bull;</p>
<dd>Textured XVideo acceleration including anti-tearing support (Bicubic filtering only available on R/RV3xx, R/RV/RS4xx, R/RV5xx, and RS6xx/RS740);</p>
<dt>&bull;</p>
<dd>3D acceleration;</dl>
<h2>Supported Hardware</h2>
<p>The <code>radeon</code> driver supports PCI, AGP, and PCIe video cards based on the following ATI/AMD chips (note: list is non-exhaustive): </p>
<dl>
<dt><code>R100</code></p>
<dd>Radeon 7200</p>
<dt><code>RV100</code></p>
<dd>Radeon 7000(VE), M6, RN50/ES1000</p>
<dt><code>RS100</code></p>
<dd>Radeon IGP320(M)</p>
<dt><code>RV200</code></p>
<dd>Radeon 7500, M7, FireGL 7800</p>
<dt><code>RS200</code></p>
<dd>Radeon IGP330(M)/IGP340(M)</p>
<dt><code>RS250</code></p>
<dd>Radeon Mobility 7000 IGP</p>
<dt><code>R200</code></p>
<dd>Radeon 8500, 9100, FireGL 8800/8700</p>
<dt><code>RV250</code></p>
<dd>Radeon 9000PRO/9000, M9</p>
<dt><code>RV280</code></p>
<dd>Radeon 9200PRO/9200/9200SE/9250, M9+</p>
<dt><code>RS300</code></p>
<dd>Radeon 9100 IGP</p>
<dt><code>RS350</code></p>
<dd>Radeon 9200 IGP</p>
<dt><code>RS400/RS480</code></p>
<dd>Radeon XPRESS 200(M)/1100 IGP</p>
<dt><code>R300</code></p>
<dd>Radeon 9700PRO/9700/9500PRO/9500/9600TX, FireGL X1/Z1</p>
<dt><code>R350</code></p>
<dd>Radeon 9800PRO/9800SE/9800, FireGL X2</p>
<dt><code>R360</code></p>
<dd>Radeon 9800XT</p>
<dt><code>RV350</code></p>
<dd>Radeon 9600PRO/9600SE/9600/9550, M10/M11, FireGL T2</p>
<dt><code>RV360</code></p>
<dd>Radeon 9600XT</p>
<dt><code>RV370</code></p>
<dd>Radeon X300, M22</p>
<dt><code>RV380</code></p>
<dd>Radeon X600, M24</p>
<dt><code>RV410</code></p>
<dd>Radeon X700, M26 PCIe</p>
<dt><code>R420</code></p>
<dd>Radeon X800 AGP</p>
<dt><code>R423/R430</code></p>
<dd>Radeon X800, M28 PCIe</p>
<dt><code>R480/R481</code></p>
<dd>Radeon X850 PCIe/AGP</p>
<dt><code>RV505/RV515/RV516/RV550</code></p>
<dd>Radeon X1300/X1400/X1500/X1550/X2300</p>
<dt><code>R520</code></p>
<dd>Radeon X1800</p>
<dt><code>RV530/RV560</code></p>
<dd>Radeon X1600/X1650/X1700</p>
<dt><code>RV570/R580</code></p>
<dd>Radeon X1900/X1950</p>
<dt><code>RS600/RS690/RS740</code></p>
<dd>Radeon X1200/X1250/X2100</p>
<dt><code>R600</code></p>
<dd>Radeon HD 2900</p>
<dt><code>RV610/RV630</code></p>
<dd>Radeon HD 2400/2600/2700/4200/4225/4250</p>
<dt><code>RV620/RV635</code></p>
<dd>Radeon HD 3410/3430/3450/3470/3650/3670</p>
<dt><code>RV670</code></p>
<dd>Radeon HD 3690/3850/3870</p>
<dt><code>RS780/RS880</code></p>
<dd>Radeon HD 3100/3200/3300/4100/4200/4250/4290</p>
<dt><code>RV710/RV730</code></p>
<dd>Radeon HD 4330/4350/4550/4650/4670/5145/5165/530v/545v/560v/565v</p>
<dt><code>RV740/RV770/RV790</code></p>
<dd>Radeon HD 4770/4730/4830/4850/4860/4870/4890</p>
<dt><code>CEDAR</code></p>
<dd>Radeon HD 5430/5450/6330/6350/6370</p>
<dt><code>REDWOOD</code></p>
<dd>Radeon HD 5550/5570/5650/5670/5730/5750/5770/6530/6550/6570</p>
<dt><code>JUNIPER</code></p>
<dd>Radeon HD 5750/5770/5830/5850/5870/6750/6770/6830/6850/6870</p>
<dt><code>CYPRESS</code></p>
<dd>Radeon HD 5830/5850/5870</p>
<dt><code>HEMLOCK</code></p>
<dd>Radeon HD 5970</p>
<dt><code>PALM</code></p>
<dd>Radeon HD 6310/6250</p>
<dt><code>SUMO/SUMO2</code></p>
<dd>Radeon HD 6370/6380/6410/6480/6520/6530/6550/6620</p>
<dt><code>BARTS</code></p>
<dd>Radeon HD 6790/6850/6870/6950/6970/6990</p>
<dt><code>TURKS</code></p>
<dd>Radeon HD 6570/6630/6650/6670/6730/6750/6770</p>
<dt><code>CAICOS</code></p>
<dd>Radeon HD 6430/6450/6470/6490</p>
<dt><code>CAYMAN</code></p>
<dd>Radeon HD 6950/6970/6990</p>
<dt><code>ARUBA</code></p>
<dd>Radeon HD 7000 series</p>
<dt><code>TAHITI</code></p>
<dd>Radeon HD 7900 series</p>
<dt><code>PITCAIRN</code></p>
<dd>Radeon HD 7800 series</p>
<dt><code>VERDE</code></p>
<dd>Radeon HD 7700 series</p>
<dt><code>OLAND</code></p>
<dd>Radeon HD 8000 series</p>
<dt><code>HAINAN</code></p>
<dd>Radeon HD 8000 series</p>
<dt><code>BONAIRE</code></p>
<dd>Radeon HD 7790 series</p>
<dt><code>KAVERI</code></p>
<dd>KAVERI APUs</p>
<dt><code>KABINI</code></p>
<dd>KABINI APUs</p>
<dt><code>HAWAII</code></p>
<dd>Radeon R9 series</p>
<dt><code>MULLINS</code></p>
<dd>MULLINS APUs</dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;SWcursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Selects software cursor. The default is <code>off.</code></p>
<dt><code>Option &#34;Accel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enables or disables all hardware acceleration.<br />
 The default is <code>on.</code></p>
<dt><code>Option &#34;ZaphodHeads&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the RandR output(s) to use with zaphod mode for a particular driver instance. If you use this option you must use this option for all instances of the driver.<br />
 For example: <code>Option &#34;ZaphodHeads&#34; &#34;LVDS,VGA-0&#34;</code> will assign xrandr outputs LVDS and VGA-0 to this instance of the driver.</p>
<dt><code>Option &#34;ColorTiling&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>The framebuffer can be addressed either in linear or tiled mode. Tiled mode can provide significant performance benefits with 3D applications. Tiling will be disabled if the drm module is too old or if the current display configuration does not support it. On R600+ this enables 1D tiling mode.<br />
 The default value is <code>on</code> for R/RV3XX, R/RV4XX, R/RV5XX, RS6XX, RS740, R/RV6XX, R/RV7XX, RS780, RS880, EVERGREEN, CAYMAN, ARUBA, Southern Islands, and Sea Islands and <code>off</code> for R/RV/RS1XX, R/RV/RS2XX, RS3XX, and RS690/RS780/RS880 when fast fb feature is enabled.</p>
<dt><code>Option &#34;ColorTiling2D&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>The framebuffer can be addressed either in linear, 1D, or 2D tiled modes. 2D tiled mode can provide significant performance benefits over 1D tiling with 3D applications. Tiling will be disabled if the drm module is too old or if the current display configuration does not support it. KMS ColorTiling2D is only supported on R600 and newer chips and requires Mesa 9.0 or newer for R6xx-ARUBA, Mesa 9.2 or newer for Southern Islands, and Mesa 10.1 or newer for Sea Islands.<br />
 The default value is <code>on</code> for R/RV6XX, R/RV7XX, RS780, RS880, EVERGREEN, CAYMAN, ARUBA, Southern Islands, and Sea Islands.</p>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Define the maximum level of DRI to enable. Valid values are 2 for DRI2 or 3 for DRI3. The default is <code>3 for DRI3</code> if the Xorg version is &gt;= 1.18.3 and glamor is enabled, otherwise <code>2 for DRI2. Note:</code> DRI3 may not work correctly in all cases with EXA, enable at your own risk.</p>
<dt><code>Option &#34;EnablePageFlip&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable DRI2 page flipping. The default is <code>on.</code> Pageflipping is supported on all radeon hardware.</p>
<dt><code>Option &#34;TearFree&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Set the default value of the per-output &#8216;TearFree&#8217; property, which controls tearing prevention using the hardware page flipping mechanism. TearFree is on for any CRTC associated with one or more outputs with TearFree on. Two separate scanout buffers need to be allocated for each CRTC with TearFree on. If this option is set, the default value of the property is &#8216;on&#8217; or &#8216;off&#8217; accordingly. If this option isn&#8217;t set, the default value of the property is <code>auto,</code> which means that TearFree is on for rotated outputs, outputs with RandR transforms applied and for RandR 1.4 secondary outputs, otherwise off.</p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Chooses between available acceleration architectures. Valid values are <code>EXA</code> (for pre-TAHITI GPUs) and <code>glamor</code> (for R300 or higher). The default is <code>glamor</code> with R600 or newer (with Xorg &gt;= 1.18.3, otherwise with TAHITI or newer), otherwise <code>EXA.</code> </p>
</dl>
<p> The following driver <code>Options</code> are supported for <code>glamor</code> :</p>
<dl>
<dt><code>Option &#34;ShadowPrimary&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option enables a so-called &quot;shadow primary&quot; buffer for fast CPU access to pixel data, and separate scanout buffers for each display controller (CRTC). This may improve performance for some 2D workloads, potentially at the expense of other (e.g. 3D, video) workloads. Note in particular that enabling this option currently disables page flipping. The default is <code>off.</code> </p>
</dl>
<p> The following driver <code>Options</code> are supported for <code>EXA</code> :</p>
<dl>
<dt><code>Option &#34;EXAVSync&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option attempts to avoid tearing by stalling the engine until the display controller has passed the destination region. It reduces tearing at the cost of performance and has been known to cause instability on some chips. The default is <code>off.</code></p>
<dt><code>Option &#34;EXAPixmaps&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Under KMS, to avoid thrashing pixmaps in/out of VRAM on low memory cards, we use a heuristic based on VRAM amount to determine whether to allow EXA to use VRAM for non-essential pixmaps. This option allows us to override the heuristic. The default is <code>on</code> with &gt; 32MB VRAM, off with &lt; 32MB or when fast fb feature is enabled for RS690/RS780/RS880.</p>
<dt><code>Option &#34;SwapbuffersWait&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls the behavior of glXSwapBuffers and glXCopySubBufferMESA calls by GL applications. If enabled, the calls will avoid tearing by making sure the display scanline is outside of the area to be copied before the copy occurs. If disabled, no scanline synchronization is performed, meaning tearing will likely occur. Note that when enabled, this option can adversely affect the framerate of applications that render frames at less than refresh rate.</p>
<dd>The default value is <code>on.</code> </p>
</dl>
<h2>Textured Video Attributes</h2>
<p>The driver supports the following X11 Xv attributes for Textured Video. You can use the &quot;xvattr&quot; tool to query/set those attributes at runtime. </p>
<dl>
<dt><code>XV_VSYNC</code></p>
<dd>XV_VSYNC is used to control whether textured adapter synchronizes the screen update to the monitor vertical refresh to eliminate tearing. It has two values: &#8216;off'(0) and &#8216;on'(1). The default is <code>&#8216;on'(1).</code> </p>
<dt><code>XV_CRTC</code></p>
<dd>XV_CRTC is used to control which display controller (crtc) the textured adapter synchronizes the screen update with when XV_VSYNC is enabled. The default, &#8216;auto'(-1), will sync to the display controller that more of the video is on; when this is ambiguous, the display controller associated with the RandR primary output is preferred. This attribute is useful for things like clone mode where the user can best decide which display should be synced. The default is <code>&#8216;auto'(-1).</code> </p>
<dt><code>XV_BICUBIC</code></p>
<dd>XV_BICUBIC is used to control whether textured adapter should apply a bicubic filter to smooth the output. It has three values: &#8216;off'(0), &#8216;on'(1) and &#8216;auto'(2). &#8216;off&#8217; means never apply the filter, &#8216;on&#8217; means always apply the filter and &#8216;auto&#8217; means apply the filter only if the X and Y sizes are scaled to more than double to avoid blurred output. Bicubic filtering is not currently compatible with other Xv attributes like hue, contrast, and brightness, and must be disabled to use those attributes. The default is <code>&#8216;off'(0).</code> </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<dl>
<dt> 1.</p>
<dd>Wiki page:</p>
<dl>
<dd><a rel="nofollow" href="https://www.x.org/wiki/radeon">https://www.x.org/wiki/radeon</a></dl>
<dt> 2.</p>
<dd>Overview about radeon development code:</p>
<dl>
<dd><a rel="nofollow" href="https://cgit.freedesktop.org/xorg/driver/xf86-video-ati/">https://cgit.freedesktop.org/xorg/driver/xf86-video-ati/</a></dl>
<dt> 3.</p>
<dd>Mailing list:</p>
<dl>
<dd><a rel="nofollow" href="https://lists.freedesktop.org/mailman/listinfo/amd-gfx">https://lists.freedesktop.org/mailman/listinfo/amd-gfx</a></dl>
<dt> 4.</p>
<dd>IRC channel:</p>
<dl>
<dd>#radeon on irc.freenode.net</dl>
<dt> 5.</p>
<dd>Query the bugtracker for radeon bugs:</p>
<dl>
<dd><a rel="nofollow" href="https://bugs.freedesktop.org/query.cgi?product=xorg">https://bugs.freedesktop.org/query.cgi?product=xorg</a>&amp;component=Driver/Radeon</dl>
<dt> 6.</p>
<dd>Submit bugs &amp; patches:</p>
<dl>
<dd><a rel="nofollow" href="https://bugs.freedesktop.org/enter_bug.cgi?product=xorg">https://bugs.freedesktop.org/enter_bug.cgi?product=xorg</a>&amp;component=Driver/Radeon</dl>
<h2>Authors</h2>
<pre>Authors include:
Rickard E. (Rik) Faith <i>faith [at] precisioninsight.com</i>
Kevin E. Martin <i>kem [at] freedesktop.org</i>
Alan Hourihane <i>alanh [at] fairlite.demon.co.uk</i>
Marc Aurele La France <i>tsi [at] xfree86.org</i>
Benjamin Herrenschmidt <i>benh [at] kernel.crashing.org</i>
Michel D&auml;nzer <i>michel [at] daenzer.net</i>
Alex Deucher <i>alexdeucher [at] gmail.com</i>
Bogdan D. <i>bogdand [at] users.sourceforge.net</i>
Eric Anholt <i>eric [at] anholt.net</i></pre>
