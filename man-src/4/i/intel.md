---
title: "intel(4)"
name: "intel"
section: "4"
letter: "i"
url: "/docs/linux/man/4-intel/"
description: "intel – Intel integrated graphics chipsets"
---

<p>intel &#8211; Intel integrated graphics chipsets</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;intel&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>intel</code> is an Xorg driver for Intel integrated graphics chipsets. The driver supports depths 8, 15, 16 and 24. All visual types are supported in depth 8. For the i810/i815 other depths support the TrueColor and DirectColor visuals. For the i830M and later, only the TrueColor visual is supported for depths greater than 8. The driver supports hardware accelerated 3D via the Direct Rendering Infrastructure (DRI), but only in depth 16 for the i810/i815 and depths 16 and 24 for the 830M and later.</p>
<h2>Supported Hardware</h2>
<p><code>intel</code> supports the i810, i810-DC100, i810e, i815, i830M, 845G, 852GM, 855GM, 865G, 915G, 915GM, 945G, 945GM, 965G, 965Q, 946GZ, 965GM, 945GME, G33, Q33, Q35, G35, GM45, G45, Q45, G43, G41 chipsets, Pineview-M in Atom N400 series, Pineview-D in Atom D400/D500 series, Intel(R) HD Graphics, Intel(R) Iris(TM) Graphics, Intel(R) Iris(TM) Pro Graphics.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver. </p>
<p> The Intel 8xx and 9xx families of integrated graphics chipsets have a unified memory architecture meaning that system memory is used as video RAM. For the i810 and i815 family of chipsets, operating system support for allocating system memory is required in order to use this driver. For the 830M and later, this is required in order for the driver to use more video RAM than has been pre-allocated at boot time by the BIOS. This is usually achieved with an &quot;agpgart&quot; or &quot;agp&quot; kernel driver. Linux, FreeBSD, OpenBSD, NetBSD, and Solaris have such kernel drivers available. </p>
<p> By default, the i810/i815 will use 8 MB of system memory for graphics if AGP allocable memory is &lt; 128 MB, 16 MB if &lt; 192 MB or 24 MB if higher. Use the <code>VideoRam</code> option to change the default value. </p>
<p> For the 830M and later, the driver will automatically size its memory allocation according to the features it will support. Therefore, the <code>VideoRam</code> option, which in the past had been necessary to allow more than some small amount of memory to be allocated, is now ignored. </p>
<p> The following driver <code>Options</code> are supported</p>
<dl>
<dt><code>Option &#34;ColorKey&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This sets the default pixel value for the YUV video overlay key.</p>
<dd>Default: undefined.</p>
<dt><code>Option &#34;DRI&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Disable or enable DRI support. A driver name to use can be provided instead of simple boolean value, which will be passed to the GL implementation for it to load the appropriate backend. Alternatively the maximum level of DRI to enable (e.g. &quot;1&quot;, &quot;2&quot; or &quot;3&quot;) can be specified.</p>
<dd>Default: All levels of DRI are enabled for configurations where it is supported. </p>
</dl>
<p> The following driver <code>Options</code> are supported for the i810 and i815 chipsets:</p>
<dl>
<dt><code>Option &#34;CacheLines&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This allows the user to change the amount of graphics memory used for 2D acceleration and video when XAA acceleration is enabled. Decreasing this amount leaves more for 3D textures. Increasing it can improve 2D performance at the expense of 3D performance.</p>
<dd>Default: depends on the resolution, depth, and available video memory. The driver attempts to allocate space for at 3 screenfuls of pixmaps plus an HD-sized XV video. The default used for a specific configuration can be found by examining the Xorg log file.</p>
<dt><code>Option &#34;DDC&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable DDC support.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;Dac6Bit&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable 6-bits per RGB for 8-bit modes.</p>
<dd>Default: 8-bits per RGB for 8-bit modes.</p>
<dt><code>Option &#34;XvMCSurfaces&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option enables XvMC. The integer parameter specifies the number of surfaces to use. Valid values are 6 and 7.</p>
<dd>Default: XvMC is disabled.</p>
<dt><code>VideoRam </code><i>integer</i></p>
<dd>This option specifies the amount of system memory to use for graphics, in KB.</p>
<dd>The default is 8192 if AGP allocable memory is &lt; 128 MB, 16384 if &lt; 192 MB, 24576 if higher. DRI require at least a value of 16384. Higher values may give better 3D performance, at expense of available system memory.</p>
<dt><code>Option &#34;Accel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable acceleration.</p>
<dd>Default: acceleration is enabled. </p>
</dl>
<p> The following driver <code>Options</code> are supported for the 830M and later chipsets:</p>
<dl>
<dt><code>Option &#34;Accel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable or disable acceleration.</p>
<dd>Default: acceleration is enabled.</p>
<dt><code>Option &#34;Present&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable use of hardware counters and flow control for the Present extension.</p>
<dd>Default: Enabled</p>
<dt><code>Option &#34;AccelMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Select acceleration method. There are a couple of backends available for accelerating the DDX. &#34;UXA&#34; (Unified Acceleration Architecture) is the mature backend that was introduced to support the GEM driver model. It is in the process of being superseded by &#34;SNA&#34; (Sandybridge&#8217;s New Acceleration). Until that process is complete, the ability to choose which backend to use remains for backwards compatibility. In addition, there are a pair of sub-options to limit the acceleration for debugging use. Specify &#34;off&#34; or &#34;none&#34; to disable all acceleration, or &#34;blt&#34; to disable render acceleration and only use the BLT engine.</p>
<dd>Default: use SNA (render acceleration)</p>
<dt><code>Option &#34;TearFree&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable TearFree updates. This option forces X to perform all rendering to a backbuffer prior to updating the actual display. It requires an extra memory allocation the same size as a framebuffer, the occasional extra copy, and requires Damage tracking. Thus enabling TearFree requires more memory and is slower (reduced throughput) and introduces a small amount of output latency, but it should not impact input latency. However, the update to the screen is then performed synchronously with the vertical refresh of the display so that the entire update is completed before the display starts its refresh. That is only one frame is ever visible, preventing an unsightly tear between two visible and differing frames. Note that this replicates what the compositing manager should be doing, however TearFree will redirect the compositor updates (and those of fullscreen games) directly on to the scanout thus incurring no additional overhead in the composited case. Also note that not all compositing managers prevent tearing, and if the outputs are rotated, there will still be tearing without TearFree enabled.</p>
<dd>Default: TearFree is disabled.</p>
<dt><code>Option &#34;ReprobeOutputs&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disable or enable rediscovery of connected displays during server startup. As the kernel driver loads it scans for connected displays and configures a console spanning those outputs. When the X server starts, we then take the list of connected displays and framebuffer layout and use that for the initial configuration. Sometimes, not all displays are correctly detected by the kernel and so it is useful in a few circumstances for X to force the kernel to reprobe all displays when it starts. To make the X server recheck the status of connected displays, set the &#34;ReprobeOutputs&#34; option to true. Please do file a bug for any circumstances which require this workaround.</p>
<dd>Default: reprobing is disabled for a faster startup.</p>
<dt><code>Option &#34;VideoKey&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This is the same as the <code>&#34;ColorKey&#34;</code> option described above. It is provided for compatibility with most other drivers.</p>
<dt><code>Option &#34;XvPreferOverlay&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Make hardware overlay be the first XV adaptor. The overlay behaves incorrectly in the presence of compositing, but some prefer it due to it syncing to vblank in the absence of compositing. While most XV-using applications have options to select which XV adaptor to use, this option can be used to place the overlay first for applications which don&#8217;t have options for selecting adaptors.</p>
<dd>Default: Textured video adaptor is preferred.</p>
<dt><code>Option &#34;Backlight&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Override the probed backlight control interface. Sometimes the automatically selected backlight interface may not correspond to the correct, or simply most useful, interface available on the system. This allows you to override that choice by specifying the entry under /sys/class/backlight to use.</p>
<dd>Default: Automatic selection.</p>
<dt><code>Option &#34;CustomEDID&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Override the probed EDID on particular outputs. Sometimes the manufacturer supplied EDID is corrupt or lacking a few usable modes and supplying a corrected EDID may be easier than specifying every modeline. This option allows to pass the path to load an EDID from per output. The format is a comma separated string of output:path pairs, e.g. DP1:/path/to/dp1.edid,DP2:/path/to/dp2.edid</p>
<dd>Default: No override, use manufacturer supplied EDIDs.</p>
<dt><code>Option &#34;FallbackDebug&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable printing of debugging information on acceleration fallbacks to the server log.</p>
<dd>Default: Disabled</p>
<dt><code>Option &#34;DebugFlushBatches&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Flush the batch buffer after every single operation.</p>
<dd>Default: Disabled</p>
<dt><code>Option &#34;DebugFlushCaches&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Include an MI_FLUSH at the end of every batch buffer to force data to be flushed out of cache and into memory before the completion of the batch.</p>
<dd>Default: Disabled</p>
<dt><code>Option &#34;DebugWait&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Wait for the completion of every batch buffer before continuing, i.e. perform synchronous rendering.</p>
<dd>Default: Disabled</p>
<dt><code>Option &#34;HWRotation&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Override the use of native hardware rotation and force the use of software, but GPU accelerated where possible, rotation. On some platforms the hardware can scanout directly into a rotated output bypassing the intermediate rendering and extra allocations required for software implemented rotation (i.e. native rotation uses less resources, is quicker and uses less power). This allows you to disable the native rotation in case of errors.</p>
<dd>Default: Enabled (use hardware rotation)</p>
<dt><code>Option &#34;VSync&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls the use of commands to synchronise rendering with the vertical refresh of the display. Some rendering commands have the option to be performed in a &quot;tear-free&quot; fashion by stalling the GPU to wait for the display to be outside of the region to be updated. This slows down all rendering, and historically has been the source of many GPU hangs.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;PageFlip&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls the use of commands to flip the scanout address on a VBlank. This is used by glXSwapBuffers to efficiently perform the back-to-front exchange at the end of a frame without incurring the penalty of a copy, or stalling the render pipeline (the flip is performed asynchronrously to the render command stream by the display engine). However, it has historically been the source of many GPU hangs.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;SwapbuffersWait&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls the behavior of glXSwapBuffers and glXCopySubBufferMESA calls by GL applications. If enabled, the calls will avoid tearing by making sure the display scanline is outside of the area to be copied before the copy occurs. If disabled, no scanline synchronization is performed, meaning tearing will likely occur.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;TripleBuffer&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option enables the use of a third buffer for page-flipping. The third buffer allows applications to run at vrefresh rates even if they occasionally fail to swapbuffers on time. The effect of such missed swaps is the output jitters between 60fps and 30fps, and in the worst case appears frame-locked to 30fps. The disadvantage of triple buffering is that there is an extra frame of latency, due to the pre-rendered frame sitting in the swap queue, between input and any display update.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;Tiling&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls whether memory buffers for Pixmaps are allocated in tiled mode. In most cases (especially for complex rendering), tiling dramatically improves performance.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;LinearFramebuffer&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls whether the memory for the scanout (also known as the front or frame buffer) is allocated in linear memory. A tiled framebuffer is required for power conservation features, but for certain system configurations you may wish to override this and force a linear layout.</p>
<dd>Default: disabled</p>
<dt><code>Option &#34;RelaxedFencing&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls whether we attempt to allocate the minimal amount of memory required for the buffers. The reduction in working set has a substantial improvement on system performance. However, this has been demonstrate to be buggy on older hardware (845-865 and 915-945, but ok on PineView and later) so on those chipsets defaults to off.</p>
<dd>Default: Enabled for G33 (includes PineView), and later, class machines.</p>
<dt><code>Option &#34;XvMC&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable XvMC driver. Current support MPEG2 MC on 915/945 and G33 series. User should provide absolute path to libIntelXvMC.so in XvMCConfig file.</p>
<dd>Default: Disabled.</p>
<dt><code>Option &#34;Throttle&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls whether the driver periodically waits for pending drawing operations to complete. Throttling ensures that the GPU does not lag too far behind the CPU and thus noticeable delays in user responsible at the cost of throughput performance.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;HotPlug&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option controls whether the driver automatically notifies applications when monitors are connected or disconnected.</p>
<dd>Default: enabled.</p>
<dt><code>Option &#34;Virtualheads&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This option controls specifies the number of fake outputs to create in addition to the normal outputs detected on your hardware. These outputs cannot be assigned to the regular displays attached to the GPU, but do otherwise act as any other xrandr output and share a portion of the regular framebuffer. One use case for these extra heads is for extending your desktop onto a discrete GPU using the Bumblebee project. However, the recommendation here is to use PRIME instead to create a single Xserver that can addresses and coordinate between multiple GPUs.</p>
<dd>Default: 0</p>
<dt><code>Option &#34;ZaphodHeads&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>
<dd>Specify the randr output(s) to use with zaphod mode for a particular driver instance. If you set this option you must use it with all instances of the driver. By default, each head is assigned only one CRTC (which limits using multiple outputs with that head to cloned mode). CRTC can be manually assigned to individual heads by preceding the output names with a comma delimited list of pipe numbers followed by a colon. Note that different pipes may be limited in their functionality and some outputs may only work with different pipes.<br />
 For example: </p>
<dl>
<dd><code>Option &#34;ZaphodHeads&#34; &#34;LVDS1,VGA1&#34;</code> </p>
<p> will assign xrandr outputs LVDS1 and VGA1 to this instance of the driver.</dl>
<dl>
<dd><code>Option &#34;ZaphodHeads&#34; &#34;0,2:HDMI1,DP2&#34;</code> </p>
<p> will assign xrandr outputs HDMI1 and DP2 and CRTCs 0 and 2 to this instance of the driver.</dl>
</dl>
<h2>Output Configuration</h2>
<p>On 830M and better chipsets, the driver supports runtime configuration of detected outputs. You can use the <code>xrandr</code> tool to control outputs on the command line as follows: </p>
<dl>
<dd><code>xrandr &#8211;output</code> <i>output</i> <code>&#8211;set</code> <i>property value</i></dl>
<p> Note that you may need to quote property and value arguments that contain spaces. Each output listed below may have one or more properties associated with it (like a binary EDID block if one is found). Some outputs have unique properties which are described below. See the &quot;MULTIHEAD CONFIGURATIONS&quot; section below for additional information.</p>
<h3>Vga</h3>
<p>VGA output port (typically exposed via an HD15 connector).</p>
<h3>Lvds</h3>
<p>Low Voltage Differential Signalling output (typically a laptop LCD panel). Available properties: </p>
<dl>
<dt><code>BACKLIGHT &#8211; current backlight level (adjustable)</p>
<dd>By adjusting the BACKLIGHT property, the brightness on the LVDS output can be adjusted. In some cases, this property may be unavailable (for example if your platform uses an external microcontroller to control the backlight).</p>
<dt>scaling mode</code> &#8211; control LCD panel scaling mode</p>
<dd>When the currently selected display mode differs from the native panel resolution, various scaling options are available. These include</p>
<dl>
<dd>
<dl>
<dt><code>Center</code></p>
<dd>Simply center the image on-screen without scaling. This is the only scaling mode that guarantees a one-to-one correspondence between native and displayed pixels, but some portions of the panel may be unused (so-called &quot;letterboxing&quot;).</p>
<dt><code>Full aspect</code></p>
<dd>Scale the image as much as possible while preserving aspect ratio. Pixels may not be displayed one-to-one (there may be some blurriness). Some portions of the panel may be unused if the aspect ratio of the selected mode does not match that of the panel.</p>
<dt><code>Full</code></p>
<dd>Scale the image to the panel size without regard to aspect ratio. This is the only mode which guarantees that every pixel of the panel will be used. But the displayed image may be distorted by stretching either horizontally or vertically, and pixels may not be displayed one-to-one (there may be some blurriness).</dl>
</dl>
<p> The precise names of these options may differ depending on the kernel video driver, (but the functionality should be similar). See the output of <code>xrandr &#8211;prop</code> for a list of currently available scaling modes.</dl>
<h3>Tv</h3>
<p>Integrated TV output. Available properties include:</p>
<dl>
<dt><code>BOTTOM, RIGHT, TOP, LEFT</code> &#8211; margins</p>
<dd>Adjusting these properties allows you to control the placement of your TV output buffer on the screen. The options with the same name can also be set in xorg.conf with integer value.</p>
<dt><code>BRIGHTNESS</code> &#8211; TV brightness, range 0-255</p>
<dd>Adjust TV brightness, default value is 128.</p>
<dt><code>CONTRAST</code> &#8211; TV contrast, range 0-255</p>
<dd>Adjust TV contrast, default value is 1.0 in chipset specific format.</p>
<dt><code>SATURATION</code> &#8211; TV saturation, range 0-255</p>
<dd>Adjust TV saturation, default value is 1.0 in chipset specific format.</p>
<dt><code>HUE</code> &#8211; TV hue, range 0-255</p>
<dd>Adjust TV hue, default value is 0.</p>
<dt><code>TV_FORMAT</code> &#8211; output standard</p>
<dd>This property allows you to control the output standard used on your TV output port. You can select between NTSC-M, NTSC-443, NTSC-J, PAL-M, PAL-N, and PAL.</p>
<dt><code>TV_Connector</code> &#8211; connector type</p>
<dd>This config option should be added to xorg.conf TV monitor&#8217;s section, it allows you to force the TV output connector type, which bypass load detect and TV will always be taken as connected. You can select between S-Video, Composite and Component. </p>
</dl>
<h3>Tmds-1</h3>
<p>First DVI SDVO output</p>
<h3>Tmds-2</h3>
<p>Second DVI SDVO output</p>
<h3>Tmds-1, Tmds-2, Hdmi-1, Hdmi-2</h3>
<p>DVI/HDMI outputs. Available common properties include:</p>
<dl>
<dt><code>BROADCAST_RGB</code> &#8211; method used to set RGB color range</p>
<dd>Adjusting this property allows you to set RGB color range on each channel in order to match HDTV requirement(default 0 for full range). Setting 1 means RGB color range is 16-235, 0 means RGB color range is 0-255 on each channel. (Full range is 0-255, not 16-235) </p>
</dl>
<p> SDVO and DVO TV outputs are not supported by the driver at this time. </p>
<p> See <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for information on associating Monitor sections with these outputs for configuration. Associating Monitor sections with each output can be helpful if you need to ignore a specific output, for example, or statically configure an extended desktop monitor layout.</p>
<h2>Multihead Configurations</h2>
<p>The number of independent outputs is dictated by the number of CRTCs (in X parlance) a given chip supports. Most recent Intel chips have two CRTCs, meaning that two separate framebuffers can be displayed simultaneously, in an extended desktop configuration. If a chip supports more outputs than it has CRTCs (say local flat panel, VGA and TV in the case of many outputs), two of the outputs will have to be &quot;cloned&quot;, meaning that they display the same framebuffer contents (or one displays a subset of another&#8217;s framebuffer if the modes aren&#8217;t equal). </p>
<p> You can use the &quot;xrandr&quot; tool, or various desktop utilities, to change your output configuration at runtime. To statically configure your outputs, you can use the &quot;Monitor-&lt;type&gt;&quot; options along with additional monitor sections in your xorg.conf to create your screen topology. The example below puts the VGA output to the right of the builtin laptop screen, both running at 1024&#215;768. </p>
<pre><code>Section &#34;Monitor&#34;</code>
<code> Identifier &#34;Laptop FooBar Internal Display&#34;</code>
<code> Option &#34;Position&#34; &#34;0 0&#34;</code>
<code>EndSection</code>
<code>Section &#34;Monitor&#34;</code>
<code> Identifier &#34;Some Random CRT&#34;</code>
<code> Option &#34;Position&#34; &#34;1024 0&#34;</code>
<code> Option &#34;RightOf&#34; &#34;Laptop FoodBar Internal Display&#34;</code>
<code>EndSection</code>
<code>Section &#34;Device&#34;</code>
<code> Driver &#34;intel&#34;</code>
<code> Option &#34;monitor-LVDS&#34; &#34;Laptop FooBar Internal Display&#34;</code>
<code> Option &#34;monitor-VGA&#34; &#34;Some Random CRT&#34;</code>
<code>EndSection</code></pre>
<h2>Textured Video Attributes</h2>
<p>The driver supports the following X11 Xv attributes for Textured Video. You can use the &quot;xvattr&quot; tool to query/set those attributes at runtime.</p>
<h3>Xv_Sync_To_Vblank</h3>
<p>XV_SYNC_TO_VBLANK is used to control whether textured adapter synchronizes the screen update to the vblank to eliminate tearing. It is a Boolean attribute with values of 0 (never sync) or 1 (always sync). An historic value of -1 (sync for large windows only) will now be interpreted as 1, (since the current approach for sync is not costly even with small video windows).</p>
<h3>Xv_Brightness</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<h3>Xv_Contrast</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<h2>Reporting Bugs</h2>
<p>The xf86-video-intel driver is part of the X.Org and Freedesktop.org umbrella projects. Details on bug reporting can be found at <a rel="nofollow" href="https://01.org/linuxgraphics/documentation/how-report-bugs.">https://01.org/linuxgraphics/documentation/how-report-bugs.</a> Mailing lists are also commonly used to report experiences and ask questions about configuration and other topics. See lists.freedesktop.org for more information (the xorg [at] lists.freedesktop.org mailing list is the most appropriate place to ask X.Org and driver related questions).</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Keith Whitwell, and also Jonathan Bian, Matthew J Sottek, Jeff Hartmann, Mark Vojkovich, Alan Hourihane, H. J. Lu. 830M and 845G support reworked for XFree86 4.3 by David Dawes and Keith Whitwell. 852GM, 855GM, and 865G support added by David Dawes and Keith Whitwell. 915G, 915GM, 945G, 945GM, 965G, 965Q and 946GZ support added by Alan Hourihane and Keith Whitwell. Lid status support added by Alan Hourihane. Textured video support for 915G and later chips, RandR 1.2 and hardware modesetting added by Eric Anholt and Keith Packard. EXA and Render acceleration added by Wang Zhenyu. TV out support added by Zou Nan Hai and Keith Packard. 965GM, G33, Q33, and Q35 support added by Wang Zhenyu.</p>
