---
title: "xrandr(1)"
name: "xrandr"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrandr/"
description: "xrandr – primitive command line interface to RandR extension"
---

<h2 class="name">NAME</h2>
<p> xrandr &#8211; primitive command line interface to RandR extension </p>
<h2>SYNOPSIS</h2>
<p> <code>xrandr</code> [&#8211;help] [&#8211;display <i>display</i>] [-q] [-v] [&#8211;verbose] [&#8211;dryrun] [&#8211;screen <i>snum</i>] [&#8211;q1] [&#8211;q12] [&#8211;current] [&#8211;noprimary] [&#8211;panning <i>width</i>x<i>height</i>[+<i>x</i>+<i>y</i>[/<i>track_width</i>x<i>track_height</i>+<i>track_x</i>+<i>track_y</i>[/<i>border_left</i>/<i>border_top</i>/<i>border_right</i>/<i>border_bottom</i>]]]] [&#8211;scale <i>x</i>[x<i>y</i>]] [&#8211;scale-from <i>w</i>x<i>h</i>] [&#8211;transform <i>a</i>,<i>b</i>,<i>c</i>,<i>d</i>,<i>e</i>,<i>f</i>,<i>g</i>,<i>h</i>,<i>i</i>] [&#8211;primary] [&#8211;prop] [&#8211;fb <i>width</i>x<i>height</i>] [&#8211;fbmm <i>width</i>x<i>height</i>] [&#8211;dpi <i>dpi</i>] [&#8211;dpi <i>from-output</i>] [&#8211;newmode <i>name</i> <i>mode</i>] [&#8211;rmmode <i>name</i>] [&#8211;addmode <i>output</i> <i>name</i>] [&#8211;delmode <i>output</i> <i>name</i>] [&#8211;output <i>output</i>] [&#8211;auto] [&#8211;mode <i>mode</i>] [&#8211;preferred] [&#8211;pos <i>x</i>x<i>y</i>] [&#8211;rate <i>rate</i>] [&#8211;reflect <i>reflection</i>] [&#8211;rotate <i>orientation</i>] [&#8211;left-of <i>output</i>] [&#8211;right-of <i>output</i>] [&#8211;above <i>output</i>] [&#8211;below <i>output</i>] [&#8211;same-as <i>output</i>] [&#8211;set <i>property</i> <i>value</i>] [&#8211;off] [&#8211;crtc <i>crtc</i>] [&#8211;gamma <i>red</i>[:<i>green</i>:<i>blue</i>]] [&#8211;brightness <i>brightness</i>] [-o <i>orientation</i>] [-s <i>size</i>] [-r <i>rate</i>] [-x] [-y] [&#8211;listproviders] [&#8211;setprovideroutputsource <i>provider</i> <i>source</i>] [&#8211;setprovideroffloadsink <i>provider</i> <i>sink</i>] [&#8211;listmonitors] [&#8211;listactivemonitors] [&#8211;setmonitor <i>name</i> <i>geometry</i> <i>outputs</i>] [&#8211;delmonitor <i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xrandr</i> is used to set the size, orientation and/or reflection of the outputs for a screen. It can also set the screen size. </p>
<p> If invoked without any option, it will dump the state of the outputs, showing the existing modes for each of them, with a &#8216;+&#8217; after the preferred modes and a &#8216;*&#8217; after the current mode. </p>
<p> There are a few global options. Other options modify the last output that is specified in earlier parameters in the command line. Multiple outputs may be modified at the same time by passing multiple &#8211;output options followed immediately by their corresponding modifying options.</p>
<dl>
<dt>&#8211;help</p>
<dd> Print out a summary of the usage and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Print out the RandR version reported by the X server and exit.</p>
<dt>&#8211;verbose</p>
<dd> Causes xrandr to be more verbose. When used with -q (or without other options), xrandr will display more information about the server state. Please note that the gamma and brightness informations are only approximations of the complete color profile stored in the server. When used along with options that reconfigure the system, progress will be reported while executing the configuration changes.</p>
<dt>-q, &#8211;query</p>
<dd> When this option is present, or when no configuration changes are requested, xrandr will display the current state of the system.</p>
<dt>&#8211;dryrun</p>
<dd> Performs all the actions specified except that no changes are made.</p>
<dt>&#8211;nograb</p>
<dd> Apply the modifications without grabbing the screen. It avoids to block other applications during the update but it might also cause some applications that detect screen resize to receive old values.</p>
<dt>-d, &#8211;display <i>name</i></p>
<dd> This option selects the X display to use. Note this refers to the X screen abstraction, not the monitor (or output).</p>
<dt>&#8211;screen <i>snum</i></p>
<dd> This option selects which screen to manipulate. Note this refers to the X screen abstraction, not the monitor (or output).</p>
<dt>&#8211;q1</p>
<dd> Forces the usage of the RandR version 1.1 protocol, even if a higher version is available.</p>
<dt>&#8211;q12</p>
<dd> Forces the usage of the RandR version 1.2 protocol, even if the display does not report it as supported or a higher version is available.</dl>
<h2>RandR version 1.5 options</h2>
<p> Options for RandR 1.5 are used as a superset of the options for RandR 1.4. </p>
<dl>
<dt>&#8211;listmonitors</p>
<dd> Report information about all defined monitors.</p>
<dt>&#8211;listactivemonitors</p>
<dd> Report information about currently active monitors.</p>
<dt>&#8211;setmonitor <i>name</i> <i>geometry</i> <i>outputs</i>}</p>
<dd> Define a new monitor with the given geometry and associated to the given outputs. The output list is either the keyword <code>none</code> or a comma-separated list of outputs. The geometry is either the keyword <code>auto</code>, in which case the monitor will automatically track the geometry of the associated outputs, or a manual specification in the form <i>w</i>/<i>mmw</i>x<i>h</i>/<i>mmh</i>+<i>x</i>+<i>y</i> where w, h, x, y are in pixels and mmw, mmh are the physical dimensions of the monitor.</p>
<dt>&#8211;delmonitor <i>name</i></p>
<dd> Delete the given user-defined monitor.</dl>
<h2>RandR version 1.4 options</h2>
<p> Options for RandR 1.4 are used as a superset of the options for RandR 1.3.</p>
<dl>
<dt>&#8211;listproviders</p>
<dd> Report information about the providers available.</p>
<dt>&#8211;setprovideroutputsource <i>provider</i> <i>source</i></p>
<dd> Set <i>source</i> as the source of display output images for <i>provider</i>. This is only possible if <i>source</i> and <i>provider</i> have the <code>Source Output</code> and <code>Sink Output</code> capabilities, respectively. If <i>source</i> is <code>0x0</code>, then <i>provider</i> is disconnected from its current output source.</p>
<dt>&#8211;setprovideroffloadsink <i>provider</i> <i>sink</i></p>
<dd> Set <i>provider</i> as a render offload device for <i>sink</i>. This is only possible if <i>provider</i> and <i>sink</i> have the <code>Source Offload</code> and <code>Sink Offload</code> capabilities, respectively. If <i>sink</i> is <code>0x0</code>, then <i>provider</i> is disconnected from its current render offload sink.</dl>
<h2>RandR version 1.3 options</h2>
<p> Options for RandR 1.3 are used as a superset of the options for RandR 1.2. </p>
<dl>
<dt>&#8211;current</p>
<dd> Return the current screen configuration, without polling for hardware changes.</p>
<dt>&#8211;noprimary</p>
<dd> Don&#8217;t define a primary output.</dl>
<p> <code>Per-output options</code></p>
<dl>
<dt>&#8211;panning <i>width</i>x<i>height</i>[+<i>x</i>+<i>y</i>[/<i>track_width</i>x<i>track_height</i>+<i>track_x</i>+<i>track_y</i>[/<i>border_left</i>/<i>border_top</i>/<i>border_right</i>/<i>border_bottom</i>]]]</p>
<dd> This option sets the panning parameters. As soon as panning is enabled, the CRTC position can change with every pointer move. The first four parameters specify the total panning area, the next four the pointer tracking area (which defaults to the same area). The last four parameters specify the border and default to 0. A width or height set to zero disables panning on the according axis. You typically have to set the screen size with <i>&#8211;fb</i> simultaneously.</p>
<dt>&#8211;transform <i>a</i>,<i>b</i>,<i>c</i>,<i>d</i>,<i>e</i>,<i>f</i>,<i>g</i>,<i>h</i>,<i>i</i></p>
<dd> Specifies a transformation matrix to apply on the output. A bilinear filter is selected automatically unless the &#8211;filter parameter is also specified. The mathematical form corresponds to:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> a b c<br />
 d e f<br />
 g h i</dl>
<p> The transformation is based on homogeneous coordinates. The matrix multiplied by the coordinate vector of a pixel of the output gives the transformed coordinate vector of a pixel in the graphic buffer. More precisely, the vector (x y) of the output pixel is extended to 3 values (x y w), with 1 as the w coordinate and multiplied against the matrix. The final device coordinates of the pixel are then calculated with the so-called homogenic division by the transformed w coordinate. In other words, the device coordinates (x&#8217; y&#8217;) of the transformed pixel are:</p>
<dl>
<dt>
<dd> x&#8217; = (ax + by + c) / w&#8217; and<br />
 y&#8217; = (dx + ey + f) / w&#8217; ,<br />
 with w&#8217; = (gx + hy + i) .</dl>
<p> Typically, <i>a</i> and <i>e</i> corresponds to the scaling on the X and Y axes, <i>c</i> and <i>f</i> corresponds to the translation on those axes, and <i>g</i>, <i>h</i>, and <i>i</i> are respectively 0, 0 and 1. The matrix can also be used to express more complex transformations such as keystone correction, or rotation. For a rotation of an angle T, this formula can be used:</p>
<dl>
<dt>
<dd> cos T -sin T 0<br />
 sin T cos T 0 </p>
<p>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1</dl>
<p> As a special argument, instead of passing a matrix, one can pass the string <i>none</i>, in which case the default values are used (a unit matrix without filter).</dl>
<dt>&#8211;filter <i>filtermode</i></p>
<dd> Chooses the scaling filter method to be applied when the screen is scaled or transformed. Can be either &#8216;bilinear&#8217; or &#8216;nearest&#8217;.</p>
<dt>&#8211;scale <i>x</i>[x<i>y</i>]</p>
<dd> Changes the dimensions of the output picture. If the <i>y</i> value is omitted, the <i>x</i> value will be used for both dimensions. Values larger than 1 lead to a compressed screen (screen dimension bigger than the dimension of the output mode), and values less than 1 lead to a zoom in on the output. This option is actually a shortcut version of the <i>&#8211;transform</i> option.</p>
<dt>&#8211;scale-from <i>w</i>x<i>h</i></p>
<dd> Specifies the size in pixels of the area of the framebuffer to be displayed on this output. This option is actually a shortcut version of the <i>&#8211;transform</i> option.</p>
<dt>&#8211;primary</p>
<dd> Set the output as primary. It will be sorted first in Xinerama and RANDR geometry requests.</dl>
<h2>RandR version 1.2 options</h2>
<p> These options are only available for X server supporting RandR version 1.2 or newer.</p>
<dl>
<dt>&#8211;prop, &#8211;properties</p>
<dd> This option causes xrandr to display the contents of properties for each output. &#8211;verbose also enables &#8211;prop.</p>
<dt>&#8211;fb <i>width</i>x<i>height</i></p>
<dd> Reconfigures the screen to the specified size. All configured monitors must fit within this size. When this option is not provided, xrandr computes the smallest screen size that will hold the set of configured outputs; this option provides a way to override that behaviour.</p>
<dt>&#8211;fbmm <i>width</i>x<i>height</i></p>
<dd> Sets the value reported as physical size of the X screen as a whole (union of all configured monitors). In configurations with multiple monitors with different DPIs, the value has no physical meaning, but it may be used by some legacy clients which do not support RandR version 1.2 to compute a reference font scaling. Normally, xrandr resets the reported physical size values to keep the DPI constant. This overrides that computation. Default DPI value is 96.</p>
<dt>&#8211;dpi <i>dpi</i></p>
<dd>
<dt>&#8211;dpi <i>from-output</i></p>
<dd> This also sets the value reported as physical size of the X screen as a whole (union of all configured monitors). In configurations with multiple monitors with different DPIs, the value has no physical meaning, but it may be used by some legacy clients which do not support RandR version 1.2 to compute a reference font scaling. This option uses either the specified DPI value, or the DPI of the given output, to compute an appropriate physical size using whatever pixel size will be set. Typical values are the default (96 DPI), the DPI of the only monitor in single-monitor configurations, or the DPI of the primary monitor in multi-monitor configurations.</p>
<dt>&#8211;newmode <i>name</i> <i>mode</i></p>
<dd> New modelines can be added to the server and then associated with outputs. This option does the former. The <i>mode</i> is specified using the ModeLine syntax for xorg.conf: clock hdisp hsyncstart hsyncend htotal vdisp vsyncstart vsyncend vtotal <i>flags</i>. <i>flags</i> can be zero or more of +HSync, -HSync, +VSync, -VSync, Interlace, DoubleScan, CSync, +CSync, -CSync. Several tools permit to compute the usual modeline from a height, width, and refresh rate, for instance you can use <code>cvt</code>.</p>
<dt>&#8211;rmmode <i>name</i></p>
<dd> This removes a mode from the server if it is otherwise unused.</p>
<dt>&#8211;addmode <i>output</i> <i>name</i></p>
<dd> Add a mode to the set of valid modes for an output.</p>
<dt>&#8211;delmode <i>output</i> <i>name</i></p>
<dd> Remove a mode from the set of valid modes for an output.</dl>
<p> <code>Per-output options</code></p>
<dl>
<dt>&#8211;output <i>output</i></p>
<dd> Selects an output to reconfigure. Use either the name of the output or the XID.</p>
<dt>&#8211;auto</p>
<dd> For connected but disabled outputs, this will enable them using their first preferred mode (or, something close to 96dpi if they have no preferred mode). For disconnected but enabled outputs, this will disable them.</p>
<dt>&#8211;mode <i>mode</i></p>
<dd> This selects a mode. Use either the name or the XID for <i>mode</i></p>
<dt>&#8211;preferred</p>
<dd> This selects the same mode as &#8211;auto, but it doesn&#8217;t automatically enable or disable the output.</p>
<dt>&#8211;pos <i>x</i>x<i>y</i></p>
<dd> Position the output within the screen using pixel coordinates. In case reflection or rotation is applied, the translation is applied after the effects.</p>
<dt>&#8211;rate <i>rate</i></p>
<dd> This marks a preference for refresh rates close to the specified value, when multiple modes have the same name, this will select the one with the nearest refresh rate.</p>
<dt>&#8211;reflect <i>reflection</i></p>
<dd> Reflection can be one of &#8216;normal&#8217; &#8216;x&#8217;, &#8216;y&#8217; or &#8216;xy&#8217;. This causes the output contents to be reflected across the specified axes.</p>
<dt>&#8211;rotate <i>rotation</i></p>
<dd> Rotation can be one of &#8216;normal&#8217;, &#8216;left&#8217;, &#8216;right&#8217; or &#8216;inverted&#8217;. This causes the output contents to be rotated in the specified direction. &#8216;right&#8217; specifies a clockwise rotation of the picture and &#8216;left&#8217; specifies a counter-clockwise rotation.</p>
<dt>&#8211;left-of, &#8211;right-of, &#8211;above, &#8211;below, &#8211;same-as <i>another-output</i></p>
<dd> Use one of these options to position the output relative to the position of another output. This allows convenient tiling of outputs within the screen. The position is always computed relative to the new position of the other output, so it is not valid to say &#8211;output a &#8211;left-of b &#8211;output b &#8211;left-of a.</p>
<dt>&#8211;set <i>property</i> <i>value</i></p>
<dd> Sets an output property. Integer properties may be specified as a valid (see &#8211;prop) comma-separated list of decimal or hexadecimal (with a leading 0x) values. Atom properties may be set to any of the valid atoms (see &#8211;prop). String properties may be set to any value.</p>
<dt>&#8211;off</p>
<dd> Disables the output.</p>
<dt>&#8211;crtc <i>crtc</i></p>
<dd> Uses the specified crtc (either as an index in the list of CRTCs or XID). In normal usage, this option is not required as xrandr tries to make sensible choices about which crtc to use with each output. When that fails for some reason, this option can override the normal selection.</p>
<dt>&#8211;gamma <i>red</i>[:<i>green</i>:<i>blue</i>]</p>
<dd> Set the specified floating point values as gamma correction on the crtc currently attached to this output. If green and blue are not specified, the red value will be used for all three components. Note that you cannot get two different values for cloned outputs (i.e.: which share the same crtc) and that switching an output to another crtc doesn&#8217;t change the crtc gamma corrections at all.</p>
<dt>&#8211;brightness <i>brightness</i></p>
<dd> Multiply the gamma values on the crtc currently attached to the output to specified floating value. Useful for overly bright or overly dim outputs. However, this is a software only modification, if your hardware has support to actually change the brightness, you will probably prefer to use <code>xbacklight</code>.</dl>
<h2>RandR version 1.1 options</h2>
<p> These options are available for X servers supporting RandR version 1.1 or older. They are still valid for newer X servers, but they don&#8217;t interact sensibly with version 1.2 options on the same command line.</p>
<dl>
<dt>-s, &#8211;size <i>size-index</i> or &#8211;size <i>width</i>x<i>height</i></p>
<dd> This sets the screen size, either matching by size or using the index into the list of available sizes.</p>
<dt>-r, &#8211;rate, &#8211;refresh <i>rate</i></p>
<dd> This sets the refresh rate closest to the specified value.</p>
<dt>-o, &#8211;orientation <i>rotation</i></p>
<dd> This specifies the orientation of the screen, and can be one of normal, inverted, left or right.</p>
<dt>-x</p>
<dd> Reflect across the X axis.</p>
<dt>-y</p>
<dd> Reflect across the Y axis.</dl>
<h2>EXAMPLES</h2>
<p> Sets an output called LVDS to its preferred mode, and on its right put an output called VGA to preferred mode of a screen which has been physically rotated clockwise:</p>
<dl>
<dt>
<dd> xrandr &#8211;output LVDS &#8211;auto &#8211;rotate normal &#8211;pos 0x0 &#8211;output VGA &#8211;auto &#8211;rotate left &#8211;right-of LVDS</dl>
<p> Forces to use a 1024&#215;768 mode on an output called VGA:</p>
<dl>
<dt>
<dd> xrandr &#8211;newmode &quot;1024&#215;768&quot; 63.50 1024 1072 1176 1328 768 771 775 798 -hsync +vsync<br />
 xrandr &#8211;addmode VGA 1024&#215;768<br />
 xrandr &#8211;output VGA &#8211;mode 1024&#215;768</dl>
<p> Enables panning on a 1600&#215;768 desktop while displaying 1024&#215;768 mode on an output called VGA:</p>
<dl>
<dt>
<dd> xrandr &#8211;fb 1600&#215;768 &#8211;output VGA &#8211;mode 1024&#215;768 &#8211;panning 1600&#215;0</dl>
<p> Have one small 1280&#215;800 LVDS screen showing a small version of a huge 3200&#215;2000 desktop, and have a big VGA screen display the surrounding of the mouse at normal size.</p>
<dl>
<dt>
<dd> xrandr &#8211;fb 3200&#215;2000 &#8211;output LVDS &#8211;scale 2.5&#215;2.5 &#8211;output VGA &#8211;pos 0x0 &#8211;panning 3200&#215;2000+0+0/3200&#215;2000+0+0/64/64/64/64</dl>
<p> Displays the VGA output in trapezoid shape so that it is keystone corrected when the projector is slightly above the screen:</p>
<dl>
<dt>
<dd> xrandr &#8211;fb 1024&#215;768 &#8211;output VGA &#8211;transform 1.24,0.16,-124,0,1.24,0,0,0.000316,1</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-xrandr/">Xrandr</a>(3), <a href="/docs/linux/man/1-cvt/">cvt</a>(1), <a href="/docs/linux/man/1-xkeystone/">xkeystone</a>(1), <a href="/docs/linux/man/1-xbacklight/">xbacklight</a>(1)</p>
<h2>AUTHORS</h2>
<p> Keith Packard, Open Source Technology Center, Intel Corporation. and Jim Gettys, Cambridge Research Laboratory, HP Labs, HP. </p>
<h2>Index</h2>
