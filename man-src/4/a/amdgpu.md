---
title: "amdgpu(4)"
name: "amdgpu"
section: "4"
letter: "a"
url: "/docs/linux/man/4-amdgpu/"
description: "amdgpu – AMD RADEON GPU video driver"
---

<p>amdgpu &#8211; AMD RADEON GPU video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;amdgpu&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>amdgpu</code> is an Xorg driver for AMD RADEON-based video cards with the following features: </p>
<dl>
<dt>&bull;</p>
<dd>Support for 8-, 15-, 16-, 24- and 30-bit pixel depths;</p>
<dt>&bull;</p>
<dd>RandR support up to version 1.4;</p>
<dt>&bull;</p>
<dd>3D acceleration;</dl>
<h2>Supported Hardware</h2>
<p>The <code>amdgpu</code> driver supports SI and newer families&#8217; video cards.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;SWcursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Selects software cursor. The default is <code>off.</code></p>
<dt><code>Option &#34;Accel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enables or disables all hardware acceleration.<br />
 The default is <code>on.</code> </p>
<dt><code>Option &#34;ZaphodHeads&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the RandR output(s) to use with zaphod mode for a particular driver instance. If you use this option you must use this option for all instances of the driver.<br />
 For example: <code>Option &#34;ZaphodHeads&#34; &#34;LVDS,VGA-0&#34;</code> will assign xrandr outputs LVDS and VGA-0 to this instance of the driver.</p>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Define the maximum level of DRI to enable. Valid values are 2 for DRI2 or 3 for DRI3. The default is <code>3 for DRI3</code> if the Xorg version is &gt;= 1.18.3, otherwise <code>2 for DRI2.</code></p>
<dt><code>Option &#34;EnablePageFlip&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable DRI2 page flipping. The default is <code>on.</code></p>
<dt><code>Option &#34;TearFree&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Set the default value of the per-output &#8216;TearFree&#8217; property, which controls tearing prevention using the hardware page flipping mechanism. TearFree is on for any CRTC associated with one or more outputs with TearFree on. Two separate scanout buffers need to be allocated for each CRTC with TearFree on. If this option is set, the default value of the property is &#8216;on&#8217; or &#8216;off&#8217; accordingly. If this option isn&#8217;t set, the default value of the property is <code>auto,</code> which means that TearFree is on for rotated outputs, outputs with RandR transforms applied and for RandR 1.4 secondary outputs, otherwise off.</p>
<dt><code>Option &#34;VariableRefresh&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enables support for enabling variable refresh on the Screen&#8217;s CRTCs when an suitable application is flipping via the Present extension.<br />
 The default is <code>off.</code></p>
<dt><code>Option &#34;AsyncFlipSecondaries&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Use async flips for secondary video outputs on multi-display setups. If a screen has multiple displays attached and DRI3 page flipping is used, then only one of the displays will have its page flip synchronized to vblank for tear-free presentation. This is the display that is used for presentation timing and timestamping, usually the one covering the biggest pixel area of the screen. All other displays (&quot;Secondaries&quot;) will not synchronize their flips. This may cause some tearing on these displays, but it prevents a permanent or periodic slowdown or irritating judder of animations if not all video outputs are running synchronized with each other and with the same refresh rate. There is no perfect solution apart from perfectly synchronized outputs, but this option may give preferrable results if the displays in a multi-display setup mirror or clone each other. The default is <code>off.</code></p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Setting this option to <code>none</code> disables use of the glamor acceleration architecture. In that case, all 2D rendering is done by the CPU, but 3D and video hardware acceleration can still work. This is mainly useful for OpenGL driver bring-up.<br />
 The default is to use glamor. </p>
</dl>
<p> The following driver <code>Option</code> is supported for <code>glamor</code> :</p>
<dl>
<dt><code>Option &#34;ShadowPrimary&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option enables a so-called &quot;shadow primary&quot; buffer for fast CPU access to pixel data, and separate scanout buffers for each display controller (CRTC). This may improve performance for some 2D workloads, potentially at the expense of other (e.g. 3D, video) workloads. Note in particular that enabling this option currently disables page flipping. The default is <code>off.</code> </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<dl>
<dt> 1.</p>
<dd>Wiki page:</p>
<dl>
<dd><a rel="nofollow" href="https://www.x.org/wiki/radeon">https://www.x.org/wiki/radeon</a></dl>
<dt> 2.</p>
<dd>Overview about amdgpu development code:</p>
<dl>
<dd><a rel="nofollow" href="https://cgit.freedesktop.org/xorg/driver/xf86-video-amdgpu/">https://cgit.freedesktop.org/xorg/driver/xf86-video-amdgpu/</a></dl>
<dt> 3.</p>
<dd>Mailing list:</p>
<dl>
<dd><a rel="nofollow" href="https://lists.freedesktop.org/mailman/listinfo/amd-gfx">https://lists.freedesktop.org/mailman/listinfo/amd-gfx</a></dl>
<dt> 4.</p>
<dd>IRC channel:</p>
<dl>
<dd>#radeon on irc.freenode.net</dl>
<dt> 5.</p>
<dd>Query the bugtracker for amdgpu bugs:</p>
<dl>
<dd><a rel="nofollow" href="https://bugs.freedesktop.org/query.cgi?product=xorg">https://bugs.freedesktop.org/query.cgi?product=xorg</a>&amp;component=Driver/AMDgpu</dl>
<dt> 6.</p>
<dd>Submit bugs &amp; patches:</p>
<dl>
<dd><a rel="nofollow" href="https://bugs.freedesktop.org/enter_bug.cgi?product=xorg">https://bugs.freedesktop.org/enter_bug.cgi?product=xorg</a>&amp;component=Driver/AMDgpu</dl>
<h2>Authors</h2>
<pre>Authors include:
Michel D&auml;nzer <i>michel [at] daenzer.net</i>
Alex Deucher <i>alexdeucher [at] gmail.com</i></pre>
