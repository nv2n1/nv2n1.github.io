---
title: "xdmx(1)"
name: "xdmx"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdmx/"
description: "Xdmx – Distributed Multi-head X server"
---

<p>Xdmx &#8211; Distributed Multi-head X server</p>
<h2>Synopsis</h2>
<p><code>Xdmx</code> [:display] [option &#8230;]</p>
<h2>Description</h2>
<p><i>Xdmx</i> is a proxy X server that uses one or more other X servers as its display devices. It provides multi-head X functionality for displays that might be located on different machines. <i>Xdmx</i> functions as a front-end X server that acts as a proxy to a set of back-end X servers. All of the visible rendering is passed to the back-end X servers. Clients connect to the <i>Xdmx</i> front-end, and everything appears as it would in a regular multi-head configuration. If Xinerama is enabled (e.g., with <code>+xinerama</code> on the command line), the clients see a single large screen. </p>
<p> <i>Xdmx</i> communicates to the back-end X servers using the standard X11 protocol, and standard and/or commonly available X server extensions.</p>
<h2>Options</h2>
<p>In addition to the normal X server options described in the <i><a href="/docs/linux/man/1-xserver/">Xserver</a>(1)</i> manual page, <i>Xdmx</i> accepts the following command line switches:</p>
<dl>
<dt><code>-display </code><i>display-name</i></p>
<dd>This specifies the name(s) of the back-end X server display(s) to connect to. This option may be specified multiple times to connect to more than one back-end display. The first is used as screen 0, the second as screen 1, etc. If this option is omitted, the <code>$DISPLAY</code> environment variable is used as the single back-end X server display. </p>
<dt><code>-xinput </code><i>input-source</i></p>
<dd>This specifies the source to use for XInput extension devices. The choices are the same as for <code>-input </code>, described below, except that core devices on backend servers cannot be treated as XInput extension devices. (Although extension devices on backend and console servers are supported as extension devices under <i>Xdmx</i>). </p>
<dt><code>-input </code><i>input-source</i></p>
<dd>This specifies the source to use for the core input devices. The choices are:</p>
<dl>
<dd>
<dl>
<dt><code>dummy</code></p>
<dd>A set of dummy core input drivers are used. These never generate any input events. </p>
<dt><code>local</code></p>
<dd>The raw keyboard and pointer from the local computer are used. A comma-separated list of driver names can be appended. For example, to select the example Linux keyboard and PS/2 mouse driver use: <code>-input local,kbd,ps2</code>. The following drivers have been implemented for Linux: kbd, ms (a two-button Microsoft mouse driver), ps2 (a PS/2 mouse driver), usb-mou (a USB mouse driver), usb-kbd (a USB keyboard driver), and usb-oth (a USB non-keyboard, non-mouse driver). Additional drivers may be implemented in the future. Appropriate defaults will be used if no comma-separated list is provided. </p>
<dt><i>display-name</i></p>
<dd>If the display-name is a back-end server, then core input events are taken from the server specified. Otherwise, a console window will be opened on the specified display. </p>
<p> If the <i>display-name</i> is followed by &quot;,xi&quot; then XInput extension devices on the display will be used as <i>Xdmx</i> XInput extension devices. If the <i>display-name</i> is followed by &quot;,noxi&quot; then XInput extension devices on the display will <code>not</code> be used as <i>Xdmx</i> XInput extension devices. Currently, the default is &quot;,xi&quot;. </p>
<p> If the <i>display-name</i> is followed by &quot;,console&quot; and the <i>display-name</i> refers to a display that is used as a backend display, then a console window will be opened on that display <code>and</code> that display will be treated as a backend display. Otherwise (or if &quot;,noconsole&quot; is used), the display will be treated purely as a backend or a console display, as described above. </p>
<p> If the <i>display-name</i> is followed by &quot;,windows&quot;, then outlines of the windows on the backend will be displayed inside the console window. Otherwise (or if &quot;,nowindows&quot; is used), the console window will not display the outlines of backend windows. (This option only applies to console input.) </p>
<p> If the <i>display-name</i> is followed by &quot;,xkb&quot;, then the next 1 to 3 comma-separated parameters will specify the keycodes, symbols, and geometry of the keyboard for this input device. For example, &quot;,xkb,xfree86,pc104&quot; will specify that the &quot;xfree86&quot; keycodes and the &quot;pc104&quot; symbols should be used to initialize the keyboard. For an SGI keyboard, &quot;,xkb,sgi/indy(pc102)&quot; might be useful. A list of keycodes, symbols, and geometries can be found in <i>/usr/share/X11/xkb</i>. Use of keycodes, symbols and geometries for XKB configuration is deprecated in favor of the rules, layout, model, variant and options settings available via the -param command line switch. If this option is not specified, the input device will be queried, perhaps using the XKEYBOARD extension.</dl>
</dl>
<dl>
<dd>If this option isn&#8217;t specified, the default input source is the first back-end server (the one used for screen 0). The console window shows the layout of the back-end display(s) and pointer movements and key presses within the console window will be used as core input devices. </p>
<p> Several special function keys are active, depending on the input source: </p>
<dl>
<dd><code>Ctrl-Alt-q</code> will terminate the <i>Xdmx</i> server in all modes. </p>
<p> <code>Ctrl-Alt-g</code> will toggle a server grab in console mode (a special cursor, currently a spider, is used to indicate an active server grab). </p>
<p> <code>Ctrl-Alt-f</code> will toggle fine-grain motion in console mode (a special cursor, currently a cross hair, is used to indicate this mode). If this mode is combined with a server grab, then the cursor will have 4 lines instead of only 2. </p>
<p> <code>Ctrl-Alt-F1</code> through <code>Ctrl-Alt-F12</code> will switch to another VC in local (raw) mode.</dl>
</dl>
<dt><code>-nomulticursor</code></p>
<dd>This option turns off support for displaying multiple cursors on overlapped back-end displays. This option is available for testing and benchmarking purposes. </p>
<dt><code>-fontpath</code></p>
<dd>This option sets the <i>Xdmx</i> server&#8217;s default font path. This option can be specified multiple times to accommodate multiple font paths. See the <code>FONT PATHS</code> section below for very important information regarding setting the default font path. </p>
<dt><code>-configfile </code><i>filename</i></p>
<dd>Specify the configuration file that should be read. Note that if the <code>-display</code> command-line option is used, then the configuration file will be ignored. </p>
<dt><code>-config </code><i>name</i></p>
<dd>Specify a configuration to use. The <i>name</i> will be the name following the <code>virtual</code> keyword in the configuration file. </p>
<dt><code>-stat </code><i>interval screens</i></p>
<dd>This option enables the display of performance statistics. The interval is in seconds. The screens is a count of the number of back-end screens for which data is printed each interval. Specifying 0 for screens will display data for all screens. </p>
<p> For each screen, the following information is printed: the screen number, an absolute count of the number of XSync() calls made (SyncCount), the rate of these calls during the previous interval (Sync/s), the average round-trip time (in microseconds) of the last 10 XSync() calls (avSync), the maximum round-trip time (in microseconds) of the last 10 XSync calls (mxSync), the average number of XSync() requests that were pending but not yet processed for each of the last 10 processed XSync() calls, the maximum number of XSync() requests that were pending but not yet processed for each of the last 10 processed XSync() calls, and a histogram showing the distribution of the times of all of the XSync() calls that were made during the previous interval. </p>
<p> (The length of the moving average and the number and value of histogram bins are configurable at compile time in the <code>dmxstat.h</code> header file.) </p>
<dt><code>-syncbatch </code><i>interval</i></p>
<dd>This option sets the <i>interval</i> in milliseconds for XSync() batching. An <i>interval</i> less than or equal to 0 will disable XSync() batching. The default <i>interval</i> is 100 ms. </p>
<dt><code>-nooffscreenopt</code></p>
<dd>This option disables the offscreen optimization. Since the lazy window creation optimization requires the offscreen optimization to be enabled, this option will also disable the lazy window creation optimization. </p>
<dt><code>-nowindowopt</code></p>
<dd>This option disables the lazy window creation optimization. </p>
<dt><code>-nosubdivprims</code></p>
<dd>This option disables the primitive subdivision optimization. </p>
<dt><code>-noxkb</code></p>
<dd>Disable use of the XKB extension for communication with the back end displays. (Combine with <code>-kb</code> to disable all use of XKB.) </p>
<dt><code>-depth </code><i>int</i></p>
<dd>This option sets the root window&#8217;s default depth. When choosing a default visual from those available on the back-end X server, the first visual with that matches the depth specified is used. </p>
<p> This option can be combined with the <code>-cc</code> option, which specifies the default color visual class, to force the use of a specific depth and color class for the root window. </p>
<dt><code>-norender</code></p>
<dd>This option disables the RENDER extension. </p>
<dt><code>-noglxproxy</code></p>
<dd>This option disables GLX proxy &#8212; the build-in GLX extension implementation that is DMX aware. </p>
<dt><code>-noglxswapgroup</code></p>
<dd>This option disables the swap group and swap barrier extensions in GLX proxy. </p>
<dt><code>-glxsyncswap</code></p>
<dd>This option enables synchronization after a swap buffers call by waiting until all X protocol has been processed. When a client issues a glXSwapBuffers request, Xdmx relays that request to each back-end X server, and those requests are buffered along with all other protocol requests. However, in systems that have large network buffers, this buffering can lead to the set of back-end X servers handling the swap buffers request asynchronously. With this option, an XSync() request is issued to each back-end X server after sending the swap buffers request. The XSync() requests will flush all buffered protocol (including the swap buffers requests) and wait until the back-end X servers have processed those requests before continuing. This option does not wait until all GL commands have been processed so there might be previously issued commands that are still being processed in the GL pipe when the XSync() request returns. See the <code>-glxfinishswap</code> option below if Xdmx should wait until the GL commands have been processed. </p>
<dt><code>-glxfinishswap</code></p>
<dd>This option enables synchronization after a swap buffers call by waiting until all GL commands have been completed. It is similar to the <code>-glxsyncswap</code> option above; however, instead of issuing an XSync(), it issues a glFinish() request to each back-end X server after sending the swap buffers requests. The glFinish() request will flush all buffered protocol requests, process both X and GL requests, and wait until all previously called GL commands are complete before returning. </p>
<dt><code>-ignorebadfontpaths</code></p>
<dd>This option ignores font paths that are not available on all back-end servers by removing the bad font path(s) from the default font path list. If no valid font paths are left after removing the bad paths, an error to that effect is printed in the log. </p>
<dt><code>-addremovescreens</code></p>
<dd>This option enables the dynamic addition and removal of screens, which is disabled by default. Note that GLXProxy and Render do not yet support dynamic addition and removal of screens, and must be disabled via the <code>-noglxproxy</code> and <code>-norender</code> command line options described above. </p>
<dt><code>-param</code></p>
<dd>This option specifies parameters on the command line. Currently, only parameters dealing with XKEYBOARD configuration are supported. These parameters apply only to the core keyboard. Parameter values are installation-dependent. Please see <i>/usr/share/X11/xkb</i> or a similar directory for complete information.</p>
<dl>
<dd>
<dl>
<dt><code>XkbRules</code></p>
<dd>Defaults to &quot;evdev&quot;. Other values may include &quot;sgi&quot; and &quot;sun&quot;. </p>
<dt><code>XkbModel</code></p>
<dd>Defaults to &quot;pc105&quot;. When used with &quot;base&quot; rules, other values may include &quot;pc102&quot;, &quot;pc104&quot;, &quot;microsoft&quot;, and many others. When used with &quot;sun&quot; rules, other values may include &quot;type4&quot; and &quot;type5&quot;. </p>
<dt><code>XkbLayout</code></p>
<dd>Defaults to &quot;us&quot;. Other country codes and &quot;dvorak&quot; are usually available. </p>
<dt><code>XkbVariant</code></p>
<dd>Defaults to &quot;&quot;. </p>
<dt><code>XkbOptions</code></p>
<dd>Defaults to &quot;&quot;.</dl>
</dl>
</dl>
<h2>Configuration File Grammar</h2>
<p>The following words and tokens are reserved:</p>
<dl>
<dd><code>virtual</code> <code>display</code> <code>wall</code> <code>option</code> <code>param</code> <code>{</code> <code>}</code> <code>;</code> <code>#</code></dl>
<p> Comments start with a <code>#</code> mark and extend to the end of the line. They may appear anywhere. If a configuration file is read into <code>xdmxconfig</code>, the comments in that file will be preserved, but will not be editable. </p>
<p> The grammar is as follows:</p>
<dl>
<dd>virtual-list ::= [ virtual-list ] | virtual </p>
<p> virtual ::= <code>virtual</code> [ name ] [ dim ] <code>{</code> dw-list <code>}</code> </p>
<p> dw-list ::= [ dw-list ] | dw </p>
<p> dw ::= display | wall | option </p>
<p> display ::= <code>display</code> name [ geometry ] [ / geometry ] [ origin ] <code>;</code> </p>
<p> wall ::= <code>wall</code> [ dim ] [ dim ] name-list <code>;</code> </p>
<p> option ::= <code>option</code> name-list <code>;</code> </p>
<p> param ::= <code>param</code> name-list <code>;</code> </p>
<p> param ::= <code>param {</code> param-list <code>}</code> </p>
<p> param-list ::= [ param-list ] | name-list <code>;</code> </p>
<p> name-list ::= [ name-list ] | name </p>
<p> name ::= string | double-quoted-string </p>
<p> dim ::= integer <code>x</code> integer </p>
<p> geometry ::= [ integer <code>x</code> integer ] [ signed-integer signed-integer ] </p>
<p> origin ::= <code>@</code> integer <code>x</code> integer</dl>
<p> The name following <code>virtual</code> is used as an identifier for the configuration, and may be passed to <code>Xdmx</code> using the <code>-config</code> command line option. The name of a display should be standard X display name, although no checking is performed (e.g., &quot;machine:0&quot;). </p>
<p> For names, double quotes are optional unless the name is reserved or contains spaces. </p>
<p> The first dimension following <code>wall</code> is the dimension for tiling (e.g., 2&#215;4 or 4&#215;4). The second dimension following <code>wall</code> is the dimension of each display in the wall (e.g., 1280&#215;1024). </p>
<p> The first geometry following <code>display</code> is the geometry of the screen window on the backend server. The second geometry, which is always preceeded by a slash, is the geometry of the root window. By default, the root window has the same geometry as the screen window. </p>
<p> The <code>option</code> line can be used to specify any command-line options (e.g., <code>-input</code>). (It cannot be used to specify the name of the front-end display.) The option line is processed once at server startup, just line command line options. This behavior may be unexpected.</p>
<h2>Configuration File Examples</h2>
<p>Two displays being used for a desktop may be specified in any of the following formats:</p>
<dl>
<dd>
<pre>virtual example0 {
 display d0:0 1280x1024 @0x0;
 display d1:0 1280x1024 @1280x0;
}
virtual example1 {
 display d0:0 1280x1024;
 display d1:0 @1280x0;
}
virtual example2 {
 display &quot;d0:0&quot;;
 display &quot;d1:0&quot; @1280x0;
}
virtual example3 { wall 2x1 d0:0 d1:0; }</pre>
</dl>
<p> A 4&#215;4 wall of 16 total displays could be specified as follows (if no tiling dimension is specified, an approximate square is used):</p>
<dl>
<dd>
<pre>virtual example4 {
 wall d0:0 d1:0 d2:0 d3:0
 d4:0 d5:0 d6:0 d7:0
 d8:0 d9:0 da:0 db:0
 dc:0 dd:0 de:0 df:0;
}</pre>
</dl>
<h2>Font Paths</h2>
<p>The font path used by the <i>Xdmx</i> front-end server will be propagated to each back-end server,which requires that each back-end server have access to the exact same font paths as the front-end server. This can be most easily handled by either using a font server (e.g., xfs) or by remotely mounting the font paths on each back-end server, and then setting the <i>Xdmx</i> server&#8217;s default font path with the -I &quot;-fontpath&quot; command line option described above. </p>
<p> For example, if you specify a font path with the following command line:</p>
<dl>
<dd>Xdmx :1 -display d0:0 -fontpath /usr/fonts/75dpi/ -fontpath /usr/fonts/Type1/ +xinerama</dl>
<p> Then, /usr/fonts/75dpi/ and /usr/fonts/Type1/ must be valid font paths on the <i>Xdmx</i> server and all back-end server, which is d0 in this example. </p>
<p> Font servers can also be specified with the <i>-fontpath</i> option. For example, let&#8217;s assume that a properly configured font server is running on host d0. Then, the following command line</p>
<dl>
<dd>Xdmx :1 -display d0:0 -display d1:0 -fontpath tcp/d0:7100 +xinerama</dl>
<p> will initialize the front-end <i>Xdmx</i> server and each of the back-end servers to use the font server on d0. </p>
<p> Some fonts might not be supported by either the front-end or the back-end servers. For example, let&#8217;s assume the front-end <i>Xdmx</i> server includes support Type1 fonts, but one of the back-end servers does not. Let&#8217;s also assume that the default font path for <i>Xdmx</i> includes Type1 fonts in its font path. Then, when <i>Xdmx</i> initializes the default font path to load the default font, the font path that includes Type1 fonts (along with the other default font paths that are used by the <i>Xdmx</i> server) is sent to the back-end server that cannot handle Type1 fonts. That back-end server then rejects the font path and sends an error back to the <i>Xdmx</i> server. <i>Xdmx</i> then prints an error message and exits because it failed to set the default font path and was unable load the default font. </p>
<p> To fix this error, the offending font path must be removed from the default font path by using a different <i>-fontpath</i> command line option. </p>
<p> The <i>-fontpath</i> option can also be added to the configuration file as described above.</p>
<h2>Command-Line Examples</h2>
<p>The back-end machines are d0 and d1, core input is from the pointer and keyboard attached to d0, clients will refer to :1 when opening windows:</p>
<dl>
<dd>Xdmx :1 -display d0:0 -display d1:0 +xinerama</dl>
<p> As above, except with core input from d1:</p>
<dl>
<dd>Xdmx :1 -display d0:0 -display d1:0 -input d1:0 +xinerama</dl>
<p> As above, except with core input from a console window on the local display:</p>
<dl>
<dd>Xdmx :1 -display d0:0 -display d1:0 -input :0 +xinerama</dl>
<p> As above, except with core input from the local keyboard and mouse:</p>
<dl>
<dd>Xdmx :1 -display d0:0 -display d1:0 -input local,kbd,ps2 +xinerama</dl>
<p> Note that local input can be used under Linux while another X session is running on :0 (assuming the user can access the Linux console tty and mouse devices): a new (blank) VC will be used for keyboard input on the local machine and the Ctrl-Alt-F* sequence will be available to change to another VC (possibly back to another X session running on the local machine). Using Ctrl-Alt-Backspace on the blank VC will terminate the Xdmx session and return to the original VC. </p>
<p> This example uses the configuration file shown in the previous section:</p>
<dl>
<dd>Xdmx :1 -input :0 +xinerama -configfile filename -config example2</dl>
<p> With this configuration file line:</p>
<dl>
<dd>option -input :0 +xinerama;</dl>
<p> the command line can be shortened to:</p>
<dl>
<dd>Xdmx :1 -configfile filename -config example2</dl>
<h2>Using The Usb Device Drivers</h2>
<p>The USB device drivers use the devices called <i>/dev/input/event0</i>, <i>/dev/input/event1</i>, etc. under Linux. These devices are driven using the <i>evdev</i> Linux kernel module, which is part of the hid suite. Please note that if you load the <i>mousedev</i> or <i>kbddev</i> Linux kernel modules, then USB devices will appear as core Linux input devices and you will not be able to select between using the device only as an <i>Xdmx</i> core device or an <i>Xdmx</i> XInput extension device. Further, you may be unable to unload the <i>mousedev</i> Linux kernel module if <i>XFree86</i> is configured to use <i>/dev/input/mice</i> as an input device (this is quite helpful for laptop users and is set up by default under some Linux distributions, but should be changed if USB devices are to be used with <i>Xdmx</i>). </p>
<p> The USB device drivers search through the Linux devices for the first mouse, keyboard, or non-mouse-non-keyboard Linux device and use that device.</p>
<h2>Keyboard Initialization</h2>
<p>If <i>Xdmx</i> was invoked with <i>-xkb</i> or was <code>not</code> compiled to use the XKEYBOARD extension, then a keyboard on a backend or console will be initialized using the map that the host X server provides. </p>
<p> If the XKEYBOARD extension is used for both <i>Xdmx</i> and the host X server for the keyboard (i.e., the backend or console X server), then the type of the keyboard will be obtained from the host X server and the keyboard under <i>Xdmx</i> will be initialized with that information. Otherwise, the default type of keyboard will be initialized. In both cases, the map from the host X server will <code>not</code> be used. This means that different initial behavior may be noted with and without XKEYBOARD. Consistent and expected results will be obtained by running XKEYBOARD on all servers and by avoiding the use of <i>xmodmap</i> on the backend or console X servers prior to starting <i>Xdmx</i>. </p>
<p> If <i>-xkbmap</i> is specified on the <i>Xdmx</i> command line, then that map will currently be used for all keyboards.</p>
<h2>Multiple Core Keyboards</h2>
<p>X was not designed to support multiple core keyboards. However, <i>Xdmx</i> provides some support for multiple core keyboards. Best results will be obtained if all of the keyboards are of the same type and are using the same keyboard map. Because the X server passes raw key code information to the X client, key symbols for keyboards with different key maps would be different if the key code for each keyboard was sent without translation to the client. Therefore, <i>Xdmx</i> will attempt to translate the key code from a core keyboard to the key code for the key with the same key symbol of the <code>first</code> core keyboard that was loaded. If the key symbol appears in both maps, the results will be expected. Otherwise, the second core keyboard will return a NoSymbol key symbol for some keys that would have been translated if it was the first core keyboard.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), <code><a href="/docs/linux/man/1-xdmxconfig/">xdmxconfig</a></code>(1), <code><a href="/docs/linux/man/1-vdltodmx/">vdltodmx</a></code>(1), <code><a href="/docs/linux/man/1-xfs/">xfs</a></code>(1), <code><a href="/docs/linux/man/1-xkbcomp/">xkbcomp</a></code>(1), <code><a href="/docs/linux/man/7-xkeyboard-config/">xkeyboard-config</a></code>(7)</p>
<h2>Authors</h2>
<p>Kevin E. Martin <i>&lt;kem [at] redhat.com&gt;,</i> David H. Dawes <i>&lt;dawes [at] xfree86.org&gt;,</i> and Rickard E. (Rik) Faith <i>&lt;faith [at] redhat.com&gt;</i>. </p>
<p> Portions of <i>Xdmx</i> are based on code from The XFree86 Project (<i><a rel="nofollow" href="http://www.xfree86.org">http://www.xfree86.org</a></i>) and X.Org (<i><a rel="nofollow" href="http://www.x.org">http://www.x.org</a></i>).</p>
