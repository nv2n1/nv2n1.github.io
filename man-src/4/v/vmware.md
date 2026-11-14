---
title: "vmware(4)"
name: "vmware"
section: "4"
letter: "v"
url: "/docs/linux/man/4-vmware/"
description: "vmware – VMware SVGA video driver"
---

<p>vmware &#8211; VMware SVGA video driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;vmware&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>vmware </code> is an Xorg driver for VMware virtual video cards.</p>
<h2>Modesetting, Xinerama And Randr12</h2>
<p>If the driver can connect to the &#34;vmwgfx&#34; kernel module on linux, it will attempt to use kernel modesetting and will then also use RandR12 for multiple output operation instead of Xinerama. The X server log or the &#34;xrandr&#34; application can be used to determine whether RandR12 or Xinerama is actually used.</p>
<h2>3D Acceleration</h2>
<p>If the driver can connect to the &#34;vmwgfx&#34; kernel module on linux, and the Virtual Machine is set up to use 3D acceleration, the driver will try to use Gallium3D XA to accelerate 3D operations. It will also by default enable DRI, the Direct Rendering Infrastructure, primarily for accelerated OpenGL. If 3D acceleration is available, the driver will in addition provide an additional XVideo adaptor for textured video. Gallium3D XA,ibxatracker.so&#34; and the accelerated OpenGL driver, &#34;vmwgfx_dri.so&#34; is provided by the mesa distribution.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The driver auto-detects the version of any virtual VMware SVGA adapter. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;HWCursor&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable the HW cursor. Default: off.</p>
<dt><code>Option &#34;Xinerama&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable Xinerama support. Default: xinerama is enabled if the hardware supports it.</p>
<dt><code>Option &#34;StaticXinerama&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Provide a static xinerama geometry that will be active at server startup and will not be overridden at runtime. The format is &quot;Width1xHeight1+Xoffset1+Yoffset1;Width2xHeight2+Xoffset2+Yoffset2&quot; and so on. Negative offsets are not supported. If the driver is using RandR12, this option should be used to place and enable outputs at driver startup time or else when VMware tools is not used for that purpose. Also please see option &#34;GuiLayout&#34;.</p>
<dt><code>Option &#34;GuiLayout&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>A synonym to option &#34;StaticXinerama&#34;, since the latter name is somewhat misleading when RandR12 is favoured before Xinerarma.</p>
<dt><code>Option &#34;AddDefaultMode&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Provide a default mode with a resolution identical to the resolution of the guest before the X server was started. The X server will thus try to start without changing resolution. Default: on.</p>
<dt><code>Option &#34;RenderAccel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Try to accelerate render operations if the operations are reading from previously accelerated contents (3D or video). This option is needed for 3D support. Default: on if 3D acceleration is supported. Otherwise off.</p>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable the Direct Rendering Infrastructure. Default: on if 3D acceleration is supported and &#34;RenderAccel&#34; is enabled. Otherwise off.</p>
<dt><code>Option &#34;DirectPresents&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Speed up OpenGL swapbuffers by skipping a copy operation. This provides some OpenGL swapbuffer speedups, but may cause performance degradation and rendering errors when 3D contents is read back for mixing with software rendered contents. Default: off.</p>
<dt><code>Option &#34;HwPresents&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This is a developer convenience option and should not be used by distros or normal users. When enabled, it copies software rendered contents to a 3D surface before presenting it, so that the visible screen is always present on a 3D surface. Default: off.</p>
<dt><code>Option &#34;RenderCheck&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This is a developer convenience option and should not be used by distros or normal users. When enabled, it tries to use 3D acceleration for all XRender operations where 3D acceleration is supported, resulting in a considerable slowdown due to the increased number of readbacks of accelerated contents from host to guest. This option is used to verify that the accelerated Xrender paths works correctly with the &quot;rendercheck&quot; application. Default: off.</p>
<dt></dl>
<h2>See Also</h2>
<dd><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrandr/">xrandr</a>(1)</p>
<h2>Authors</h2>
<p>Copyright (c) 1999-2007 VMware, Inc.</p>
