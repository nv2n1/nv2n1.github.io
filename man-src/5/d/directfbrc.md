---
title: "directfbrc(5)"
name: "directfbrc"
section: "5"
letter: "d"
url: "/docs/linux/man/5-directfbrc/"
description: "directfbrc – DirectFB configuration file"
---

<p>directfbrc &#8211; DirectFB configuration file </p>
<h2>Description</h2>
<p>The <code>directfbrc</code> file is a configuration file read by all DirectFB applications on startup. There are two of these: a system-wide one stored in <i>/etc/directfbrc</i> and a per-user <i></i><code>$HOME</code>/.directfbrc which may override system settings. Further customization is available per executable (basename of argv[0]): <i>/etc/directfbrc.$0</i> and a per-user <i></i><code>$HOME</code>/.directfbrc.$0 After config files, the environment variable DFBARGS is parsed. The same parameters that can be used in the <code>directfbrc</code> file can be passed via this variable or on the command-line by prefixing them with <code>&#8211;dfb:</code> separated each with a comma. </p>
<h2>Syntax</h2>
<p>The <code>directfbrc</code> file contains one parameter per line. Comments are introduced by a hash sign (#), and continue until the end of the line. Blank lines are ignored. </p>
<p> Most parameters are switches that turn certain features on or off. These switches have a no- variant that disables the feature. This man-page describes the positive variant and will also note which setting is the compiled-in default.</p>
<h2>Parameters</h2>
<p>The following parameters may be specified in the <code>directfbrc</code> file: </p>
<dl>
<dt><code>system=&lt;system&gt;</code></dt>
<dd>Specifies the graphics system to use. The default is to use the Linux frame buffer (fbdev) but you can also run DirectFB applications on SDL (sdl). Other systems might be added in the future. </dd>
<dt><code>fbdev=&lt;device&gt;</code></dt>
<dd>Opens the given frame buffer device instead of /dev/fb0. </dd>
<dt><code>busid=&lt;id&gt;</code></dt>
<dd>Specify the bus location of the card. The option is only used if DirectFB doesn&#8217;t have sysfs support and if unspecified 1:0:0 will be assumed. Use this option if the driver fails to detect (or incorrectly detects) your card. </dd>
<dt><code>mode=&lt;width&gt;x&lt;height&gt;</code></dt>
<dd>Sets the default screen resolution. If unspecified DirectFB will use the first mode from <i>/etc/fb.modes</i> Some frame buffer devices (namely vesafb) don&#8217;t support mode switches and can only be used in the resolution that is set on boot time. </dd>
<dt><code>scaled=&lt;width&gt;x&lt;height&gt;</code></dt>
<dd>Scale the window to this size for &#8216;force-windowed&#8217; apps. </dd>
<dt><code>depth=&lt;pixeldepth&gt;</code></dt>
<dd>Sets the default pixel depth in bits per pixel. If unspecified DirectFB will use the depth specified in the first mode from <i>/etc/fb.modes</i> DirectFB supports color depths of 8, 15, 16, 24 and 32. Which values are available depends on the frame buffer device you are using. Some frame buffer devices (namely vesafb) don&#8217;t support mode switches at all and can only be used in the pixel depth that is set at boot time. </dd>
<dt><code>pixelformat=&lt;pixelformat&gt;</code></dt>
<dd>Sets the default pixel format. This is similar to the depth parameter described above but allows more fine-grained control. Possible values for pixelformat are LUT8, RGB332, RGB16, RGB24 and RGB32. Some drivers may also support the more exotic pixel formats A8, ALUT44, ARGB, ARGB1555, I420, UYVY, YUY2 and YV12. </dd>
<dt><code>session=&lt;num&gt;</code></dt>
<dd>Selects the multi application world which is joined or created. Starting with zero, negative values force creation of a new world using the lowest unused session number. This will override the environment variable &quot;DIRECTFB_SESSION&quot;. </dd>
<dt><code>force-slave</code></dt>
<dd>Always enter as a slave, waiting for the master, if not there. </dd>
<dt><code>remote=&lt;host&gt;[:&lt;session&gt;]</code></dt>
<dd>Select the remote session to connect to. </dd>
<dt><code>tmpfs=&lt;directory&gt;</code></dt>
<dd>Uses the given directory (tmpfs mount point) for creation of the shared memory file in multi application mode. This option is only useful if the automatic detection fails or if non-tmpfs storage is desired. </dd>
<dt><code>shmfile-group=&lt;groupname&gt;</code></dt>
<dd>Group that owns shared memory files. </dd>
<dt><code>memcpy=&lt;method&gt;</code></dt>
<dd>With this option the probing of memcpy() routines can be skipped, saving a lot of startup time. Pass &quot;help&quot; for a list of possible values. </dd>
<dt><code>primary-layer=&lt;id&gt;</code></dt>
<dd>Selects which layer is the &quot;primary layer&quot;, default is the first. Check &#8216;dfbinfo&#8217; for a list of layers supported by your hardware. </dd>
<dt><code>primary-only</code></dt>
<dd>Tell application only about the primary layer. </dd>
<dt><code>quiet</code></dt>
<dd>Suppresses console output from DirectFB. Only error messages will be displayed. </dd>
<dt><code>[no-]banner</code></dt>
<dd>Enables the output of the DirectFB banner at startup. This is on by default. </dd>
<dt><code>[no-]debug</code></dt>
<dd>Enables debug output. This is on by default but you won&#8217;t see any debug output unless you compiled DirectFB with debugging support. </dd>
<dt><code>[no-]debugmem</code></dt>
<dd>Enable memory allocation tracking. </dd>
<dt><code>[no-]debugshm</code></dt>
<dd>Enable shared memory allocation tracking. </dd>
<dt><code>[no-]trace</code></dt>
<dd>Enable stack trace support. This is on by default but you won&#8217;t see any trcae output unless you compiled DirectFB with trace support. </dd>
<dt><code>log-file=&lt;name&gt;</code></dt>
<dd>Write all messages to the specified file. </dd>
<dt><code>log-udp=&lt;host&gt;:&lt;port&gt;</code></dt>
<dd>Send all messages via UDP to the specified host and port. </dd>
<dt><code>fatal-level=&lt;level&gt;</code></dt>
<dd>Abort on NONE, ASSERT (default) or ASSUME (incl. assert) </dd>
<dt><code>force-windowed</code></dt>
<dd>Forces the primary surface to be a window. This allows to run applications that were written to do full-screen access in a window. </dd>
<dt><code>force-desktop</code></dt>
<dd>Forces the primary surface to be the background surface of the desktop. </dd>
<dt><code>[no-]hardware</code></dt>
<dd>Turns hardware acceleration on. By default hardware acceleration is auto-detected. If you disable hardware acceleration, the driver for your graphics card will still be loaded and used to access additional display layers (if there are any), but all graphics operations will be performed by the software renderer. </dd>
<dt><code>[no-]software</code></dt>
<dd>This option allows to disable software fallbacks. </dd>
<dt><code>[no-]dma</code></dt>
<dd>Turns DMA acceleration on, if supported by the driver. By default DMA acceleration is off. </dd>
<dt><code>[no-]sync</code></dt>
<dd>Flushes all disk buffers before initializing DirectFB. This can be useful if you working with experimental device drivers and expect crashes. The default is not to sync. </dd>
<dt><code>[no-]mmx</code></dt>
<dd>The no-mmx options allows to disable the use of MMX routines even if support for MMX was detected. By default MMX is used if is available and support for MMX was compiled in. </dd>
<dt><code>[no-]agp[=mode]</code></dt>
<dd>Turns AGP memory support on. The option enables DirectFB using the AGP memory to extend the amount of video memory available. You can specify the AGP mode to use (e.g. 1, 2, 4, 8 or 0 to disable agp). By default AGP memory support is off. </dd>
<dt><code>[no-]thrifty-surface-buffers</code></dt>
<dd>Free sysmem instance on xfer to video memory. </dd>
<dt><code>font-format=&lt;format&gt;</code></dt>
<dd>Specify the font format to use. Possible values are A1, A8, ARGB, ARGB1555, ARGB2554, ARGB4444, AiRGB. The default font format is A8 because it is the only format that ensures high quality, fast rendering and low memory consumption at the same time. Use this option only if your fonts looks strange or if font rendering is too slow. </dd>
<dt><code>[no-]sighandler</code></dt>
<dd>By default DirectFB installs a signal handler for a number of signals that cause an application to exit. This signal handler tries to deinitialize the DirectFB engine before quitting the application. Use this option to enable/disable this feature. </dd>
<dt><code>dont-catch=&lt;num&gt;[[,&lt;num&gt;]&#8230;]</code></dt>
<dd>As described with the <code>sighandler</code> option, DirectFB installs a signal handler for a number of signals. By using this option you may specify a list of signals that shouldn&#8217;t be handled this way. </dd>
<dt><code>[no-]deinit-check</code></dt>
<dd>By default DirectFB checks if the application has released all allocated resources on exit. If it didn&#8217;t, it will clean up after the application. This option allows to switch this feature on or off. </dd>
<dt><code>block-all-signals</code></dt>
<dd>This option activates blocking of all signals, useful for DirectFB daemons (a DirectFB master application that does nothing except being the master). </dd>
<dt><code>[no-]vt-switch</code></dt>
<dd>By default DirectFB allocates a new virtual terminal and switches to it. </dd>
<dt><code>vt-num=&lt;num&gt;</code></dt>
<dd>Use given VT instead of current/new one. </dd>
<dt><code>[no-]vt-switching</code></dt>
<dd>Allow to switch virtual terminals using &lt;Ctrl&gt;+&lt;Alt&gt;+&lt;F?&gt;. This is an experimental feature that is usually disabled; use at your own risk. </dd>
<dt><code>[no-]graphics-vt</code></dt>
<dd>Puts the virtual terminal into graphics mode. This has the advantage that kernel messages won&#8217;t show up on your screen while the DirectFB application is running. </dd>
<dt><code>[no-]vt</code></dt>
<dd>Use VT handling code at all? </dd>
<dt><code>mouse-source=&lt;device&gt;</code></dt>
<dd>Specify the serial mouse device. </dd>
<dt><code>[no-]mouse-gpm-source</code></dt>
<dd>Enables using GPM as mouse input repeater. </dd>
<dt><code>[no-]motion-compression</code></dt>
<dd>Usually DirectFB compresses mouse motion events. This means that subsequent mouse motions are delivered to the application as a single mouse motion event. This leads to a more responsive but less exact mouse handling. </dd>
<dt><code>mouse-protocol=&lt;protocol&gt;</code></dt>
<dd>Specifies the mouse protocol to use. The following protocols are supported: </dd>
<p> <code>MS</code> Two button mouse using the Microsoft mouse protocol. </p>
<p> <code>MS3</code> Three button mouse using an extended Microsoft mouse protocol. </p>
<p> <code>MouseMan</code> Three button mouse using a different extension to the Microsoft mouse protocol introduced by Logitech. </p>
<p> <code>MouseSystems</code> The most commonly used protocol for three button mice. </p>
<p> <code>PS/2</code> Two/three button mice of the PS/2 series. </p>
<p> <code>IMPS/2</code> Two/three button USB mice with scrolling wheel using the Microsoft Intellimouse protocol. </p>
<p> The different protocols for serial mice are described in more detail in <a href="/docs/linux/man/4-mouse/">mouse</a>(4). </p>
<dt><code>[no-]lefty</code></dt>
<dd>Swaps left and right mouse buttons. Useful for left-handers. </dd>
<dt><code>[no-]capslock-meta</code></dt>
<dd>Map the CapsLock key to Meta. Useful for users of the builtin WM without a Meta key on the keyboard (e.g. Window key). </dd>
<dt><code>linux-input-ir-only</code></dt>
<dd>Ignore all non-IR Linux Input devices. </dd>
<dt><code>[no-]linux-input-grab</code></dt>
<dd>Grab Linux Input devices. When a device is grabbed only DirectFB will receive events from it. The default is to not grab. </dd>
<dt><code>[no-]cursor</code></dt>
<dd>By default DirectFB shows a mouse cursor when an application makes use of windows. This option allows to switch the cursor off permanently. Applications cannot enable it explicitly. </dd>
<dt><code>wm=&lt;wm&gt;</code></dt>
<dd>Specify the window manager to use. </dd>
<dt><code>bg-none</code></dt>
<dd>Completely disables background handling. Doesn&#8217;t make much sense since the mouse and moving windows will leave ugly traces on the background. </dd>
<dt><code>bg-color=AARRGGBB</code></dt>
<dd>Controls the color of the background. The color is specified in hexadecimal notation. The alpha value defaults to full opacity and may be omitted. For example to choose a bright magenta background, you&#8217;d use bg-color=FF00FF. </dd>
<dt><code>bg-image=&lt;filename&gt;</code></dt>
<dd>Fills the background with the given image from file. The image is stretched to fit to the screen dimensions. </dd>
<dt><code>bg-tile=&lt;filename&gt;</code></dt>
<dd>Like <code>bg-image</code> but tiles the image to fit to the screen dimensions instead of stretching it. </dd>
<dt><code>[no-]translucent-windows</code></dt>
<dd>By default DirectFB windows may be translucent. If you disable this feature, windows are forced to be either fully opaque or fully transparent. This is useful if your graphics card doesn&#8217;t support alpha-transparent blits. </dd>
<dt><code>[no-]decorations</code></dt>
<dd>Enables window decorations if supported by the window manager. </dd>
<dt><code>videoram-limit=&lt;amount&gt;</code></dt>
<dd>Limits the amount of Video RAM used by DirectFB. The amount of Video RAM is specified in Kilobytes. </dd>
<dt><code>agpmem-limit=&lt;amount&gt;</code></dt>
<dd>Limits the amount if AGP memory used by DirectFB. The amount of AGP memory is specified in Kilobytes. </dd>
<dt><code>screenshot-dir=&lt;directory&gt;</code></dt>
<dd>If specified DirectFB will dump the screen contents in PPM format into this directory when the &lt;Print&gt; key gets pressed. </dd>
<dt><code>disable-module=&lt;modulename&gt;</code></dt>
<dd>Suppress loading of this module. The module name is the filename without the <code>libdirectfb_</code> prefix and without extension (for example <code>keyboard</code> to disable loading of the keyboard input module). </dd>
<dt><code>[no-]matrox-sgram</code></dt>
<dd>Some older Matrox G400 cards have SGRAM and a number of graphics operations are considerably faster on these cards if this feature is enabled. Don&#8217;t try to enable it if your card doesn&#8217;t have SGRAM! Otherwise you&#8217;d have to reboot. </dd>
<dt><code>[no-]matrox-crtc2</code></dt>
<dd>If you have a dual head G400/G450/G550 you can use this option to enable additional layers using the second head. </dd>
<dt><code>matrox-tv-standard=[pal|ntsc]</code></dt>
<dd>Controls the signal produced by the TV output of Matrox cards. </dd>
<dt><code>matrox-cable-type=(composite|scart-rgb|scart-composite)</code></dt>
<dd>Matrox cable type (default=composite). </dd>
<dt><code>h3600-device=&lt;device&gt;</code></dt>
<dd>Use this device for the H3600 TS driver. </dd>
<dt><code>mut-device=&lt;device&gt;</code></dt>
<dd>Use this device for the MuTouch driver. </dd>
<dt><code>penmount-device=&lt;device&gt;</code></dt>
<dd>Use this device for the PenMount driver. </dd>
<dt><code>linux-input-devices=&lt;device&gt;[[,&lt;device&gt;]&#8230;]</code></dt>
<dd>Use these devices for the Linux Input driver. </dd>
<dt><code>tslib-devices=&lt;device&gt;[[,&lt;device&gt;]&#8230;]</code></dt>
<dd>Use these devices for the tslib driver. </dd>
<dt><code>unichrome-revision=&lt;revision&gt;</code></dt>
<dd>Override the hardware revision number used by the Unichrome driver. </dd>
<dt><code>i8xx_overlay_pipe_b</code></dt>
<dd>Redirect videolayer to pixelpipe B. </dd>
<dt><code>window-surface-policy=&lt;policy&gt;</code></dt>
<dd>Allows to control where window surfaces are stored. Supported values for &lt;policy&gt; are: </dd>
<p> <code>auto</code> DirectFB decides depending on hardware capabilities. This is the default. </p>
<p> <code>videohigh</code> Swapping system/video with high priority. </p>
<p> <code>videolow</code> Swapping system/video with low priority. </p>
<p> <code>systemonly</code> Window surfaces are stored in system memory. </p>
<p> <code>videoonly</code> Window surfaces are stored in video memory. </p>
<dt><code>desktop-buffer-mode=&lt;mode&gt;</code></dt>
<dd>Allows to control the desktop buffer mode. Whenever a window is moved, opened, closed, resized or its contents change DirectFB recomposites the window stack at the affected region. This is done by blitting the windows together that are visible within that region. Opaque windows are blitted directly while translucent windows are blitted using alpha blending or color keying. If there&#8217;s a back buffer the recomposition is not visible since only the final result is copied into the front buffer. Without a back buffer each step of the recomposition is visible. This causes noticeable flicker unless all windows are opaque. </dd>
<p> Supported values for &lt;mode&gt; are: </p>
<p> <code>auto</code> DirectFB decides depending on hardware capabilities. This is the default. DirectFB chooses a back buffer in video memory if the hardware supports simple blitting (copying from back to front buffer). If there&#8217;s no acceleration at all the back buffer is allocated in system memory since that gives much better performance for alpha blended recomposition in software and avoids reading from the video memory when the result is copied to the front buffer. </p>
<p> <code>backsystem</code> The back buffer is allocated in system memory. This is the recommend choice if your hardware supports simple blitting but no alpha blending and you are going to have many alpha blended windows. </p>
<p> <code>backvideo</code> Front and back buffer are allocated in video memory. It&#8217;s not required to set this mode explicitly because the &#8216;auto&#8217; mode chooses it if blits are accelerated. Without accelerated blits this mode is not recommended. </p>
<p> <code>triple</code> Like backvideo except the surface is triple buffered. </p>
<p> <code>frontonly</code> There is no back buffer. This is the best choice if you are using opaque windows only and don&#8217;t use any color keying. </p>
<p> <code>windows</code> Special mode with window buffers directly displayed. This mode requires special hardware support. </p>
<dt><code>vsync-after</code></dt>
<dd>Wait for the vertical retrace after flipping. The default is to wait before doing the flip. </dd>
<dt><code>vsync-none</code></dt>
<dd>Disables polling for vertical retrace. </dd>
</dl>
<h2>Examples</h2>
<p>Here are some examples that demonstrates how the parameters described above are passed to DirectFB application on the command-line.</p>
<dl>
<dt><code>df_neo &#8211;dfb:no-hardware</code></dt>
<dd>Starts df_neo without hardware acceleration.</dd>
<dt><code>df_neo &#8211;dfb:help</code></dt>
<dd>Lists the DirectFB options that can be passed to df_neo. </dd>
<h2>Other Info</h2>
<p>The canonical place to find informations about DirectFB is at <a rel="nofollow" href="http://www.directfb.org/.">http://www.directfb.org/.</a> Here you can find the FAQ, tutorials, mailing list archives, the CVS tree and can download the latest version of the DirectFB library as well as a number of applications.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/directfbrc</i></dt>
<dd>system-wide DirectFB configuration file</dd>
<dt><i>$HOME/.directfbrc</i></dt>
<dd>per-user DirectFB configuration file</dd>
<dt><i>/etc/fb.modes</i></dt>
<dd>frame buffer modes file </dd>
</dl>
<h2>See Also</h2>
<p><code>fb.modes</code>(5), <code><a href="/docs/linux/man/8-fbset/">fbset</a></code>(8), <code><a href="/docs/linux/man/4-mouse/">mouse</a></code>(4), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
</dl>