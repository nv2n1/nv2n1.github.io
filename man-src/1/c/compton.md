---
title: "compton(1)"
name: "compton"
section: "1"
letter: "c"
url: "/docs/linux/man/1-compton/"
description: "compton – a compositor for X11"
---

<h2 class="name">NAME</h2>
<p> compton &#8211; a compositor for X11 </p>
<h2>SYNOPSIS</h2>
<p> <code>compton</code> [<i>OPTIONS</i>]</p>
<h2>WARNING</h2>
<p> This man page may be less up-to-date than the usage text in compton (compton -h).</p>
<h2>DESCRIPTION</h2>
<p> compton is a compositor based on Dana Jansens&#8217; version of xcompmgr (which itself was written by Keith Packard). It includes some improvements over the original xcompmgr, like window frame opacity and inactive window transparency.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Get the usage text embedded in program code, which may be more up-to-date than this man page.</dl>
<p> <code>-d</code> <i>DISPLAY</i></p>
<dl>
<dt>
<dd> Display to be managed.</dl>
<p> <code>-r</code> <i>RADIUS</i></p>
<dl>
<dt>
<dd> The blur radius for shadows, in pixels. (defaults to 12)</dl>
<p> <code>-o</code> <i>OPACITY</i></p>
<dl>
<dt>
<dd> The opacity of shadows. (0.0 &#8211; 1.0, defaults to 0.75)</dl>
<p> <code>-l</code> <i>OFFSET</i></p>
<dl>
<dt>
<dd> The left offset for shadows, in pixels. (defaults to -15)</dl>
<p> <code>-t</code> <i>OFFSET</i></p>
<dl>
<dt>
<dd> The top offset for shadows, in pixels. (defaults to -15)</dl>
<p> <code>-I</code> <i>OPACITY_STEP</i></p>
<dl>
<dt>
<dd> Opacity change between steps while fading in. (0.01 &#8211; 1.0, defaults to 0.028)</dl>
<p> <code>-O</code> <i>OPACITY_STEP</i></p>
<dl>
<dt>
<dd> Opacity change between steps while fading out. (0.01 &#8211; 1.0, defaults to 0.03)</dl>
<p> <code>-D</code> <i>MILLISECONDS</i></p>
<dl>
<dt>
<dd> The time between steps in fade step, in milliseconds. (&gt; 0, defaults to 10)</dl>
<p> <code>-m</code> <i>OPACITY</i></p>
<dl>
<dt>
<dd> Default opacity for dropdown menus and popup menus. (0.0 &#8211; 1.0, defaults to 1.0)</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Enabled client-side shadows on windows. Note desktop windows (windows with <i>_NET_WM_WINDOW_TYPE_DESKTOP</i>) never get shadow.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> Avoid drawing shadows on dock/panel windows.</dl>
<p> <code>-z</code></p>
<dl>
<dt>
<dd> Zero the part of the shadow&#8217;s mask behind the window. Note this may not work properly on ARGB windows with fully transparent areas.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Fade windows in/out when opening/closing and when opacity changes, unless <code>&#8211;no-fading-openclose</code> is used.</dl>
<p> <code>-F</code></p>
<dl>
<dt>
<dd> Equals <code>-f</code>. Deprecated.</dl>
<p> <code>-i</code> <i>OPACITY</i></p>
<dl>
<dt>
<dd> Opacity of inactive windows. (0.1 &#8211; 1.0, disabled by default)</dl>
<p> <code>-e</code> <i>OPACITY</i></p>
<dl>
<dt>
<dd> Opacity of window titlebars and borders. (0.1 &#8211; 1.0, disabled by default)</dl>
<p> <code>-G</code></p>
<dl>
<dt>
<dd> Don&#8217;t draw shadows on drag-and-drop windows.</dl>
<p> <code>-b</code></p>
<dl>
<dt>
<dd> Daemonize process. Fork to background after initialization.</dl>
<p> <code>-S</code></p>
<dl>
<dt>
<dd> Enable synchronous X operation (for debugging).</dl>
<p> <code>&#8211;config</code> <i>PATH</i></p>
<dl>
<dt>
<dd> Look for configuration file at the path. See <code>CONFIGURATION FILES</code> section below for where compton looks for a configuration file by default.</dl>
<p> <code>&#8211;shadow-red</code> <i>VALUE</i></p>
<dl>
<dt>
<dd> Red color value of shadow (0.0 &#8211; 1.0, defaults to 0).</dl>
<p> <code>&#8211;shadow-green</code> <i>VALUE</i></p>
<dl>
<dt>
<dd> Green color value of shadow (0.0 &#8211; 1.0, defaults to 0).</dl>
<p> <code>&#8211;shadow-blue</code> <i>VALUE</i></p>
<dl>
<dt>
<dd> Blue color value of shadow (0.0 &#8211; 1.0, defaults to 0).</dl>
<p> <code>&#8211;inactive-opacity-override</code></p>
<dl>
<dt>
<dd> Let inactive opacity set by <code>-i</code> overrides the windows&#8217; <i>_NET_WM_OPACITY</i> values.</dl>
<p> <code>&#8211;active-opacity</code> <i>OPACITY</i></p>
<dl>
<dt>
<dd> Default opacity for active windows. (0.0 &#8211; 1.0)</dl>
<p> <code>&#8211;inactive-dim</code> <i>VALUE</i></p>
<dl>
<dt>
<dd> Dim inactive windows. (0.0 &#8211; 1.0, defaults to 0.0)</dl>
<p> <code>&#8211;mark-wmwin-focused</code></p>
<dl>
<dt>
<dd> Try to detect WM windows (a non-override-redirect window with no child that has WM_STATE) and mark them as active.</dl>
<p> <code>&#8211;mark-ovredir-focused</code></p>
<dl>
<dt>
<dd> Mark override-redirect windows that doesn&#8217;t have a child window with WM_STATE focused.</dl>
<p> <code>&#8211;no-fading-openclose</code></p>
<dl>
<dt>
<dd> Do not fade on window open/close.</dl>
<p> <code>&#8211;shadow-ignore-shaped</code></p>
<dl>
<dt>
<dd> Do not paint shadows on shaped windows. Note shaped windows here means windows setting its shape through X Shape extension. Those using ARGB background is beyond our control.</dl>
<p> <code>&#8211;detect-rounded-corners</code></p>
<dl>
<dt>
<dd> Try to detect windows with rounded corners and don&#8217;t consider them shaped windows. The accuracy is not very high, unfortunately.</dl>
<p> <code>&#8211;detect-client-opacity</code></p>
<dl>
<dt>
<dd> Detect <i>_NET_WM_OPACITY</i> on client windows, useful for window managers not passing <i>_NET_WM_OPACITY</i> of client windows to frame windows.</dl>
<p> <code>&#8211;refresh-rate</code> <i>REFRESH_RATE</i></p>
<dl>
<dt>
<dd> Specify refresh rate of the screen. If not specified or 0, compton will try detecting this with X RandR extension.</dl>
<p> <code>&#8211;vsync</code> <i>VSYNC_METHOD</i></p>
<dl>
<dt>
<dd> Set VSync method. VSync methods currently available: </p>
<dl>
<dt>
<dd> &bull; <i>none</i>: No VSync</dl>
<dl>
<dt>
<dd> &bull; <i>drm</i>: VSync with <i>DRM_IOCTL_WAIT_VBLANK</i>. May only work on some drivers.</dl>
<dl>
<dt>
<dd> &bull; <i>opengl</i>: Try to VSync with <i>SGI_video_sync</i> OpenGL extension. Only work on some drivers.</dl>
<dl>
<dt>
<dd> &bull; <i>opengl-oml</i>: Try to VSync with <i>OML_sync_control</i> OpenGL extension. Only work on some drivers.</dl>
<dl>
<dt>
<dd> &bull; <i>opengl-swc</i>: Try to VSync with <i>SGI_swap_control</i> OpenGL extension. Only work on some drivers. Works only with GLX backend. Known to be most effective on many drivers. Does not actually control paint timing, only buffer swap is affected, so it doesn&#8217;t have the effect of <code>&#8211;sw-opti</code> unlike other methods. Experimental.</dl>
<dl>
<dt>
<dd> &bull; <i>opengl-mswc</i>: Try to VSync with <i>MESA_swap_control</i> OpenGL extension. Basically the same as <i>opengl-swc</i> above, except the extension we use.</dl>
<p> (Note some VSync methods may not be enabled at compile time.)</dl>
<p> <code>&#8211;vsync-aggressive</code></p>
<dl>
<dt>
<dd> Attempt to send painting request before VBlank and do XFlush() during VBlank. Reported to work pretty terribly. This switch may be lifted out at any moment.</dl>
<p> <code>&#8211;alpha-step</code> <i>VALUE</i></p>
<dl>
<dt>
<dd> X Render backend: Step for pregenerating alpha pictures. (0.01 &#8211; 1.0, defaults to 0.03)</dl>
<p> <code>&#8211;dbe</code></p>
<dl>
<dt>
<dd> Enable DBE painting mode, intended to use with VSync to (hopefully) eliminate tearing. Reported to have no effect, though.</dl>
<p> <code>&#8211;paint-on-overlay</code></p>
<dl>
<dt>
<dd> Painting on X Composite overlay window instead of on root window.</dl>
<p> <code>&#8211;sw-opti</code></p>
<dl>
<dt>
<dd> Limit compton to repaint at most once every 1 / <i>refresh_rate</i> second to boost performance. This should not be used with <code>&#8211;vsync</code> drm/opengl/opengl-oml as they essentially does <code>&#8211;sw-opti</code>&#8216;s job already, unless you wish to specify a lower refresh rate than the actual value.</dl>
<p> <code>&#8211;use-ewmh-active-win</code></p>
<dl>
<dt>
<dd> Use EWMH <i>_NET_ACTIVE_WINDOW</i> to determine currently focused window, rather than listening to <i>FocusIn</i>/<i>FocusOut</i> event. Might have more accuracy, provided that the WM supports it.</dl>
<p> <code>&#8211;respect-prop-shadow</code></p>
<dl>
<dt>
<dd> Respect <i>_COMPTON_SHADOW</i>. This a prototype-level feature, which you must not rely on.</dl>
<p> <code>&#8211;unredir-if-possible</code></p>
<dl>
<dt>
<dd> Unredirect all windows if a full-screen opaque window is detected, to maximize performance for full-screen windows. Known to cause flickering when redirecting/unredirecting windows. <code>&#8211;paint-on-overlay</code> may make the flickering less obvious.</dl>
<p> <code>&#8211;shadow-exclude</code> <i>CONDITION</i></p>
<dl>
<dt>
<dd> Specify a list of conditions of windows that should have no shadow.</dl>
<p> <code>&#8211;fade-exclude</code> <i>CONDITION</i></p>
<dl>
<dt>
<dd> Specify a list of conditions of windows that should not be faded.</dl>
<p> <code>&#8211;focus-exclude</code> <i>CONDITION</i></p>
<dl>
<dt>
<dd> Specify a list of conditions of windows that should always be considered focused.</dl>
<p> <code>&#8211;inactive-dim-fixed</code></p>
<dl>
<dt>
<dd> Use fixed inactive dim value, instead of adjusting according to window opacity.</dl>
<p> <code>&#8211;detect-transient</code></p>
<dl>
<dt>
<dd> Use <i>WM_TRANSIENT_FOR</i> to group windows, and consider windows in the same group focused at the same time.</dl>
<p> <code>&#8211;detect-client-leader</code></p>
<dl>
<dt>
<dd> Use <i>WM_CLIENT_LEADER</i> to group windows, and consider windows in the same group focused at the same time. <i>WM_TRANSIENT_FOR</i> has higher priority if <code>&#8211;detect-transient</code> is enabled, too.</dl>
<p> <code>&#8211;blur-background</code></p>
<dl>
<dt>
<dd> Blur background of semi-transparent / ARGB windows. Bad in performance, with driver-dependent behavior. The name of the switch may change without prior notifications.</dl>
<p> <code>&#8211;blur-background-frame</code></p>
<dl>
<dt>
<dd> Blur background of windows when the window frame is not opaque. Implies <code>&#8211;blur-background</code>. Bad in performance, with driver-dependent behavior. The name may change.</dl>
<p> <code>&#8211;blur-background-fixed</code></p>
<dl>
<dt>
<dd> Use fixed blur strength rather than adjusting according to window opacity.</dl>
<p> <code>&#8211;blur-kern</code> <i>MATRIX</i></p>
<dl>
<dt>
<dd> Specify the blur convolution kernel, with the following format: </p>
<dl>
<dt>
<dd>
<pre>
WIDTH,HEIGHT,ELE1,ELE2,ELE3,ELE4,ELE5...
</pre>
</dl>
<p> The element in the center must not be included, it will be forever 1.0 or changing based on opacity, depending on whether you have &#8211;blur-background-fixed. Yet the automatic adjustment of blur factor may not work well with a custom blur kernel. </p>
<p> A 7&#215;7 Guassian blur kernel (sigma = 0.84089642) looks like: </p>
<dl>
<dt>
<dd>
<pre>
--blur-kern '7,7,0.000003,0.000102,0.000849,0.001723,0.000849,0.000102,0.000003,0.000102,0.003494,0.029143,0.059106,0.029143,0.003494,0.000102,0.000849,0.029143,0.243117,0.493069,0.243117,0.029143,0.000849,0.001723,0.059106,0.493069,0.493069,0.059106,0.001723,0.000849,0.029143,0.243117,0.493069,0.243117,0.029143,0.000849,0.000102,0.003494,0.029143,0.059106,0.029143,0.003494,0.000102,0.000003,0.000102,0.000849,0.001723,0.000849,0.000102,0.000003'
</pre>
</dl>
<p> May also be one of the predefined kernels: 3x3box (default), 5x5box, 7x7box, 3x3gaussian, 5x5gaussian, 7x7gaussian, 9x9gaussian, 11x11gaussian. All Guassian kernels are generated with sigma = 0.84089642 . You may use the accompanied compton-convgen.py to generate blur kernels.</dl>
<p> <code>&#8211;blur-background-exclude</code> <i>CONDITION</i></p>
<dl>
<dt>
<dd> Exclude conditions for background blur.</dl>
<p> <code>&#8211;resize-damage</code> <i>INTEGER</i></p>
<dl>
<dt>
<dd> Resize damaged region by a specific number of pixels. A positive value enlarges it while a negative one shrinks it. If the value is positive, those additional pixels will not be actually painted to screen, only used in blur calculation, and such. (Due to technical limitations, with <code>&#8211;dbe</code> or <code>&#8211;glx-swap-method</code>, those pixels will still be incorrectly painted to screen.) Primarily used to fix the line corruption issues of blur, in which case you should use the blur radius value here (e.g. with a 3&#215;3 kernel, you should use <code>&#8211;resize-damage</code> 1, with a 5&#215;5 one you use <code>&#8211;resize-damage</code> 2, and so on). May or may not work with &#8211;glx-no-stencil. Shrinking doesn&#8217;t function correctly.</dl>
<p> <code>&#8211;invert-color-include</code> <i>CONDITION</i></p>
<dl>
<dt>
<dd> Specify a list of conditions of windows that should be painted with inverted color. Resource-hogging, and is not well tested.</dl>
<p> <code>&#8211;opacity-rule</code> <i>OPACITY</i>:&#8217;CONDITION&#8217;</p>
<dl>
<dt>
<dd> Specify a list of opacity rules, in the format PERCENT:PATTERN, like 50:name *= &quot;Firefox&quot;. compton-trans is recommended over this. Note we do not distinguish 100% and unset, and we don&#8217;t make any guarantee about possible conflicts with other programs that set <i>_NET_WM_WINDOW_OPACITY</i> on frame or client windows.</dl>
<p> <code>&#8211;shadow-exclude-reg</code> <i>GEOMETRY</i></p>
<dl>
<dt>
<dd> Specify a X geometry that describes the region in which shadow should not be painted in, such as a dock window region. Use &#8211;shadow-exclude-reg x10+0-0, for example, if the 10 pixels on the bottom of the screen should not have shadows painted on.</dl>
<p> <code>&#8211;backend</code> <i>BACKEND</i></p>
<dl>
<dt>
<dd> Specify the backend to use: xrender or glx. GLX (OpenGL) backend generally has much superior performance as far as you have a graphic card/chip and driver.</dl>
<p> <code>&#8211;glx-no-stencil</code></p>
<dl>
<dt>
<dd> GLX backend: Avoid using stencil buffer, useful if you don&#8217;t have a stencil buffer. Might cause incorrect opacity when rendering transparent content (but never practically happened) and may not work with <code>&#8211;blur-background</code>. My tests show a 15% performance boost. Recommended.</dl>
<p> <code>&#8211;glx-copy-from-front</code></p>
<dl>
<dt>
<dd> GLX backend: Copy unmodified regions from front buffer instead of redrawing them all. My tests with nvidia-drivers show a 10% decrease in performance when the whole screen is modified, but a 20% increase when only 1/4 is. My tests on nouveau show terrible slowdown. Useful with &#8211;glx-swap-method, as well.</dl>
<p> <code>&#8211;glx-use-copysubbuffermesa</code></p>
<dl>
<dt>
<dd> GLX backend: Use <i>MESA_copy_sub_buffer</i> to do partial screen update. My tests on nouveau shows a 200% performance boost when only 1/4 of the screen is updated. May break VSync and is not available on some drivers. Overrides <code>&#8211;glx-copy-from-front</code>.</dl>
<p> <code>&#8211;glx-no-rebind-pixmap</code></p>
<dl>
<dt>
<dd> GLX backend: Avoid rebinding pixmap on window damage. Probably could improve performance on rapid window content changes, but is known to break things on some drivers (LLVMpipe). Recommended if it works.</dl>
<p> <code>&#8211;glx-swap-method</code> undefined/exchange/copy/3/4/5/6/buffer-age</p>
<dl>
<dt>
<dd> GLX backend: GLX buffer swap method we assume. Could be undefined (0), copy (1), exchange (2), 3-6, or buffer-age (-1). undefined is the slowest and the safest, and the default value. copy is fastest, but may fail on some drivers, 2-6 are gradually slower but safer (6 is still faster than 0). Usually, double buffer means 2, triple buffer means 3. buffer-age means auto-detect using <i>GLX_EXT_buffer_age</i>, supported by some drivers. Useless with <code>&#8211;glx-use-copysubbuffermesa</code>. Partially breaks &#8211;resize-damage. Defaults to undefined.</dl>
<p> <code>&#8211;glx-use-gpushader4</code></p>
<dl>
<dt>
<dd> GLX backend: Use <i>GL_EXT_gpu_shader4</i> for some optimization on blur GLSL code. My tests on GTX 670 show no noticeable effect.</dl>
<p> <code>&#8211;dbus</code></p>
<dl>
<dt>
<dd> Enable remote control via D-Bus. See the <code>D-BUS API</code> section below for more details.</dl>
<p> <code>&#8211;benchmark</code> <i>CYCLES</i></p>
<dl>
<dt>
<dd> Benchmark mode. Repeatedly paint until reaching the specified cycles.</dl>
<p> <code>&#8211;benchmark-wid</code> <i>WINDOW_ID</i></p>
<dl>
<dt>
<dd> Specify window ID to repaint in benchmark mode. If omitted or is 0, the whole screen is repainted.</dl>
<h2>FORMAT OF CONDITIONS</h2>
<p> Some options accept a condition string to match certain windows. A condition string is formed by one or more conditions, joined by logical operators. </p>
<p> A condition with &quot;exists&quot; operator looks like this: </p>
<dl>
<dt>
<dd>
<pre>
&lt;NEGATION&gt; &lt;TARGET&gt; &lt;CLIENT/FRAME&gt; [&lt;INDEX&gt;] : &lt;FORMAT&gt; &lt;TYPE&gt;
</pre>
</dl>
<p> With equals operator it looks like: </p>
<dl>
<dt>
<dd>
<pre>
&lt;NEGATION&gt; &lt;TARGET&gt; &lt;CLIENT/FRAME&gt; [&lt;INDEX&gt;] : &lt;FORMAT&gt; &lt;TYPE&gt; &lt;NEGATION&gt; &lt;OP QUALIFIER&gt; &lt;MATCH TYPE&gt; = &lt;PATTERN&gt;
</pre>
</dl>
<p> With greater-than/less-than operators it looks like: </p>
<dl>
<dt>
<dd>
<pre>
&lt;NEGATION&gt; &lt;TARGET&gt; &lt;CLIENT/FRAME&gt; [&lt;INDEX&gt;] : &lt;FORMAT&gt; &lt;TYPE&gt; &lt;NEGATION&gt; &lt;OPERATOR&gt; &lt;PATTERN&gt;
</pre>
</dl>
<p> <i>NEGATION</i> (optional) is one or more exclamation marks; </p>
<p> <i>TARGET</i> is either a predefined target name, or the name of a window property to match. Supported predefined targets are id, x, y, x2 (x + widthb), y2, width, height, widthb (width + 2 * border), heightb, override_redirect, argb (whether the window has an ARGB visual), focused, wmwin (whether the window looks like a WM window, i.e. has no child window with WM_STATE and is not override-redirected), client (ID of client window), window_type (window type in string), leader (ID of window leader), name, class_g (= WM_CLASS[1]), class_i (= WM_CLASS[0]), and role. </p>
<p> <i>CLIENT/FRAME</i> is a single @ if the window attribute should be be looked up on client window, nothing if on frame window; </p>
<p> <i>INDEX</i> (optional) is the index number of the property to look up. For example, [2] means look at the third value in the property. Do not specify it for predefined targets. </p>
<p> <i>FORMAT</i> (optional) specifies the format of the property, 8, 16, or 32. On absence we use format X reports. Do not specify it for predefined or string targets. </p>
<p> <i>TYPE</i> is a single character representing the type of the property to match for: c for <i>CARDINAL</i>, a for <i>ATOM</i>, w for <i>WINDOW</i>, d for <i>DRAWABLE</i>, s for <i>STRING</i> (and any other string types, such as <i>UTF8_STRING</i>). Do not specify it for predefined targets. </p>
<p> <i>OP QUALIFIER</i> (optional), applicable only for equals operator, could be ? (ignore-case). </p>
<p> <i>MATCH TYPE</i> (optional), applicable only for equals operator, could be nothing (exact match), * (match anywhere), ^ (match from start), % (wildcard), or ~ (PCRE regular expression). </p>
<p> <i>OPERATOR</i> is one of = (equals), &lt;, &gt;, &lt;=, =&gt;, or nothing (exists). Exists operator checks whether a property exists on a window (but for predefined targets, exists means != 0 then). </p>
<p> <i>PATTERN</i> is either an integer or a string enclosed by single or double quotes. Python-3-style escape sequences and raw string are supported in the string format. </p>
<p> Supported logical operators are &amp;&amp; (and) and || (or). &amp;&amp; has higher precedence than ||, left-to-right associativity. Use parentheses to change precedence. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre><code>
#If the window is focused
focused
    focused = 1
#If the window is not override - redirected
    !override_redirect
        override_redirect = false override_redirect != true override_redirect != 1
#If the window is a menu
                            window_type *= "menu" _NET_WM_WINDOW_TYPE @ : a *= "MENU"
#If the window name contains "Firefox", ignore case
                                                                                   name *
                                                                                   ? = "Firefox" _NET_WM_NAME @
                                                                               : s *? = "Firefox"
#If the window name ends with "Firefox"
                                                                                      name %= "*Firefox" name ~ = "Firefox$"
#If the window has a property _COMPTON_SHADOW with value 0, type CARDINAL,
#format 32, value 0, on its frame window
                                                                                      _COMPTON_SHADOW
                                                                                    : 32c = 0
#If the third value of _NET_FRAME_EXTENTS is less than 20, or there's no
#_NET_FRAME_EXTENTS property on client window
                                                                                                _NET_FRAME_EXTENTS @[ 2 ] : 32c &lt; 20 ||
                                                                                            !_NET_FRAME_EXTENTS @ : 32c
#The pattern here will be parsed as "dd4"
                                                                                            name = "dd\o64"
#The pattern here will be parsed as "ddd"
                                                                                      name = r "dd\o64"
</code></pre>
</dl>
<h2>LEGACY FORMAT OF CONDITIONS</h2>
<p> This is the old condition format we once used. Support of this format might be removed in the future. </p>
<dl>
<dt>
<dd>
<pre>
condition = TARGET:TYPE[FLAGS]:PATTERN
</pre>
</dl>
<p> <i>TARGET</i> is one of &quot;n&quot; (window name), &quot;i&quot; (window class instance), &quot;g&quot; (window general class), and &quot;r&quot; (window role). </p>
<p> <i>TYPE</i> is one of &quot;e&quot; (exact match), &quot;a&quot; (match anywhere), &quot;s&quot; (match from start), &quot;w&quot; (wildcard), and &quot;p&quot; (PCRE regular expressions, if compiled with the support). </p>
<p> <i>FLAGS</i> could be a series of flags. Currently the only defined flag is &quot;i&quot; (ignore case). </p>
<p> <i>PATTERN</i> is the actual pattern string.</p>
<h2>CONFIGURATION FILES</h2>
<p> compton could read from a configuration file if libconfig support is compiled in. If <code>&#8211;config</code> is not used, compton will seek for a configuration file in $XDG_CONFIG_HOME/compton.conf (~/.config/compton.conf, usually), then ~/.compton.conf, then compton.conf under $XDG_DATA_DIRS (often /etc/xdg/compton.conf). </p>
<p> compton uses general libconfig configurtion file format. A sample configuration file is available as compton.sample.conf in the source tree. Most commandline switches each could be replaced with an option in configuration file, thus documented above. Window-type-specific settings are exposed only in configuration file and has the following format: </p>
<dl>
<dt>
<dd>
<pre><code>
wintypes:
{
    WINDOW_TYPE = { fade = BOOL;
    shadow = BOOL;
    opacity = FLOAT;
    focus = BOOL;
};
}
;
</code></pre>
</dl>
<p> <i>WINDOW_TYPE</i> is one of the 15 window types defined in EWMH standard: &quot;unknown&quot;, &quot;desktop&quot;, &quot;dock&quot;, &quot;toolbar&quot;, &quot;menu&quot;, &quot;utility&quot;, &quot;splash&quot;, &quot;dialog&quot;, &quot;normal&quot;, &quot;dropdown_menu&quot;, &quot;popup_menu&quot;, &quot;tooltip&quot;, &quot;notify&quot;, &quot;combo&quot;, and &quot;dnd&quot;. &quot;fade&quot; and &quot;shadow&quot; controls window-type-specific shadow and fade settings. &quot;opacity&quot; controls default opacity of the window type. &quot;focus&quot; controls whether the window of this type is to be always considered focused. (By default, all window types except &quot;normal&quot; and &quot;dialog&quot; has this on.)</p>
<h2>SIGNALS</h2>
<dl>
<dt>
<dd> &bull; compton reinitializes itself upon receiving SIGUSR1.</dl>
<h2>D-BUS API</h2>
<p> It&#8217;s possible to control compton via D-Bus messages, by running compton with <code>&#8211;dbus</code> and send messages to com.github.chjj.compton.&lt;DISPLAY&gt;. &lt;DISPLAY&gt; is the display used by compton, with all non-alphanumeric characters transformed to underscores. For DISPLAY=:0.0 you should use com.github.chjj.compton._0_0, for example. </p>
<p> The D-Bus methods and signals are not yet stable, thus undocumented right now.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Disable configuration file parsing: </p>
<dl>
<dt>
<dd>
<pre>
$ compton --config /dev/null
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Run compton with client-side shadow and fading, disable shadow on dock windows and drag-and-drop windows: </p>
<dl>
<dt>
<dd>
<pre>
$ compton -cCGf
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Same thing as above, plus making inactive windows 80% transparent, making frame 80% transparent, don&#8217;t fade on window open/close, enable software optimization, and fork to background: </p>
<dl>
<dt>
<dd>
<pre>
$ compton -bcCGf -i 0.8 -e 0.8 --no-fading-openclose --sw-opti
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Draw white shadows: </p>
<dl>
<dt>
<dd>
<pre>
$ compton -c --shadow-red 1 --shadow-green 1 --shadow-blue 1
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Avoid drawing shadows on wbar window: </p>
<dl>
<dt>
<dd>
<pre>
$ compton -c --shadow-exclude 'class_g = &quot;wbar&quot;'
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Enable OpenGL SGI_swap_control VSync with GLX backend: </p>
<dl>
<dt>
<dd>
<pre>
$ compton --backend glx --vsync opengl-swc
</pre>
</dl>
</dl>
<h2>BUGS</h2>
<p> Please report any you find to <a rel="nofollow" href="https://github.com/chjj/compton">https://github.com/chjj/compton</a> .</p>
<h2>AUTHORS</h2>
<p> xcompmgr, originally written by Keith Packard, with contributions from Matthew Allum, Eric Anholt, Dan Doel, Thomas Luebking, Matthew Hawn, Ely Levy, Phil Blundell, and Carl Worth. Compton by Christopher Jeffrey, based on Dana Jansens&#8217; original work, with contributions from Richard Grenville.</p>
<h2>RESOURCES</h2>
<p> Homepage: <a rel="nofollow" href="https://github.com/chjj/compton">https://github.com/chjj/compton</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xcompmgr/">xcompmgr</a></code>(1), <code><a href="/docs/linux/man/1-compton-trans/">compton-trans</a></code>(1) </p>
<h2>Index</h2>
