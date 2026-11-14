---
title: "xsetwacom(1)"
name: "xsetwacom"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsetwacom/"
description: "xsetwacom – commandline utility to query and modify wacom driver settings."
---

<h2 class="name">NAME</h2>
<p> xsetwacom &#8211; commandline utility to query and modify wacom driver settings. </p>
<h2>SYNOPSIS</h2>
<p> xsetwacom [options] [command [arguments]] </p>
<h2>DESCRIPTION</h2>
<p> This program queries or changes properties on the devices loaded by the wacom driver. The modification of properties happens at runtime and is not persistent through X server restarts.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;display</code> display_name</p>
<dd> Connect to the X server specified in display_name; see <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints a short help.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Enable verbose output, useful for debugging.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version number and exit. </p>
</dl>
<h2>COMMANDS</h2>
<p> Allowed commands are <code>list,</code> <code>get,</code> and <code>set.</code> The command may be specified with or without one or two preceding dashes, i.e. <code>&#8211;list</code> is equivalent to <code>-list</code> and <code>list.</code> </p>
<h3>LIST COMMANDS</h3>
<dl>
<dt><code>list</code> devices</p>
<dd> List known devices. Only input devices managed by the wacom driver are listed.</p>
<dt><code>list</code> parameters</p>
<dd> List known parameters. List all parameters suitable for the <code>get</code> or the <code>set</code> command. Note that not all parameters are available on all device types.</p>
<dt><code>list</code> modifiers</p>
<dd> List the aliases for modifiers and other keys that can be used when setting button action mappings. </p>
</dl>
<h3>GET COMMANDS</h3>
<dl>
<dt><code>get</code> device_name parameter</p>
<dd> Get the current settings for the parameter on the given device. Note that not all parameters are available on all device types. The special parameter name &quot;all&quot; may be provided to display all current settings on the device.</p>
<dt>By default, options are printed on the commandline in the respective format.</p>
<dd> The output format may be altered with one of the following options:</p>
<dt><code>-s, &#8211;shell</code></p>
<dd> Display the output in shell format, i.e. as shell commands to xsetwacom to reproduce the same parameter.</p>
<dt><code>-x, &#8211;xconf</code></p>
<dd> Display the output in xorg.conf format, i.e. as option lines that may be added to the InputDevice section in the xorg.conf. </p>
</dl>
<h3>SET COMMANDS</h3>
<dl>
<dt><code>set</code> device_name parameter [value]</p>
<dd> Set the parameter value on the given device to the value provided. Note that not all parameters are writable, some are read-only and result in an error when trying to be modified. </p>
</dl>
<h2>PARAMETERS</h2>
<p> Not all parameters are available on all tools. Use the get command with the parameter or &quot;all&quot; parameter for specific input tool applicable parameters and current settings.</p>
<dl>
<dt><code>Area</code> x1 y1 x2 y2</p>
<dd> Set the tablet input area in device coordinates in the form top left x/y and bottom right x/y. Top left and bottom right are defined in the device&#8217;s native orientation, regardless of the actual rotation currently applied. Input outside of these coordinates will be clipped to the edges of the area defined. Default: 0 0 x2 y2; with x2 and y2 tablet specific.</p>
<dt><code>Button</code> button-number [mapping]</p>
<dd> Set a mapping for the specified button-number. Mappings take the form of either a single numeric button or an &#8216;action&#8217; to be performed. If no mapping is provided, the default mapping is restored. If button-number is mapped to 0, the Button event is ignored. </p>
<p> Numeric button mappings indicate what X11 button number the given button-number should correspond to. For example, a mapping of &quot;3&quot; means a press of the given button-number will produce a press of X11 button 3 (i.e. right click). </p>
<p> Action mappings allow button presses to perform many events. They take the form of a string of keywords and arguments. </p>
<p> The &quot;key&quot; keyword is followed by a list of key names. These can optionally be preceded by &quot;+&quot; for press and &quot;-&quot; for release. If +/- is not given, press-and-release is assumed, except for modifier keys which are left pressed. Key names can be X11 KeySyms or some aliases such as &#8216;shift&#8217; or &#8216;f1&#8217; (the full list can be seen with the <code>list modifiers</code> command). </p>
<p> To assign a key that is not in the modifiers list, use the KeySym in /usr/include/X11/keysymdef.h with the XK_ prefix removed or its actual value as is. For example, XK_BackSpace should be specified as &quot;BackSpace&quot;. &quot;0xff80&quot; can also be used to replace &quot;BackSpace&quot; since it&#8217;s the unique KeySym value of Backspace key. </p>
<p> Here is a combined example: &quot;key +a shift b shift -a 0xff0d&quot; converts the button into a series of keystrokes. In this example, &quot;press a, press shift, press and release b, release shift, release a, then press and release enter&quot;. &quot;key +a +shift b -shift -a 0xff0d&quot; does the same thing. </p>
<p> The &quot;button&quot; keyword is similar except that its arguments are X11 button numbers. </p>
<p> The &quot;modetoggle&quot; keyword is also recognized; it takes no arguments, and toggles the device mode between relative and absolute pointer tracking. </p>
<p> The &quot;pan&quot; keyword causes the driver to send scroll events while the pen is dragged. This makes it easy to scroll through lists and documents, pan around 2D canvases, and zoom in/out of 3D scenes (exact behavior depends on application interpretation of scrollwheel events). Dragging the pen up/down will send scrollwheel down/up events; dragging it left/right will send scrollwheel right/left events. </p>
<p> The events in the action mapping are sent when the physical button is pressed. If the action mapping leaves any buttons or keys pressed (such as a modifier key), they will be released when the physical button is released. </p>
<p> Multiple keywords may be present in one action if desired: for example &quot;key +ctrl button 5 key -ctrl&quot;. Each keyword takes all arguments until the next keyword. </p>
<p> A maximum of 256 presses and/or releases can be specified in an action mapping. </p>
<p> The driver can only simulate physical key events but not keysyms and xsetwacom translates the mapping sequence into such events. Thus, symbols on the same physical key will generate the same event. For example, &#8216;1&#8217; and &#8216;!&#8217; are on the same key on a US keyboard and thus have the same keycode). For access to keys on a higher shift level, the sequence should be entered as it would be typed on a physical keyboard. For example, a exclamation mark is entered by the sequence of &quot;key +shift 1 -shift&quot;.</p>
<dt><code>BindToSerial</code> [serial|0]</p>
<dd> Bind the device to the tool with the specified serial number. Once bound, the device will ignore events from other tools. A serial of 0 means the device is unbound and will react to any tool of the matching type. Default: 0</p>
<dt><code>MapToOutput</code> [output]</p>
<dd> Map the tablet&#8217;s input area to a given output (e.g. &quot;VGA1&quot;). Output names may either be the name of a head available through the XRandR extension, or an X11 geometry string of the form WIDTHxHEIGHT+X+Y. To switch to the next available output, the &quot;next&quot; keyword is also supported. This will cycle between the individual monitors connected to the system, and then the entire desktop. The mapping may be reset to the entire desktop at any time with the output name &quot;desktop&quot;. Users of the NVIDIA binary driver should use the output names &quot;HEAD-0&quot; and &quot;HEAD-1&quot; until the driver supports XRandR 1.2 or later. </p>
<p> The output mapping configuration is a onetime setting and does not track output reconfigurations; the command needs to be re-run whenever the output configuration changes. When used with tablet rotation, the tablet must be rotated before it is mapped to the new screen. This parameter is write-only and cannot be queried.</p>
<dt><code>Mode</code> Absolute|Relative</p>
<dd> Set the device mode as either Relative or Absolute. Relative means pointer tracking for the device will function like a mouse, whereas Absolute means the pointer corresponds to the device&#8217;s actual position on the tablet or tablet PC screen. Default: Absolute for stylus, eraser and tablet PC touch; Relative for cursor and tablet touch.</p>
<dt><code>PressureCurve</code> x1 y1 x2 y2</p>
<dd> A Bezier curve of third order, composed of two anchor points (0,0 and 100,100) and two user modifiable control points that define the curve&#8217;s shape. Raise the curve (x1&lt;y1 x2&lt;y2) to &quot;soften&quot; the feel and lower the curve (x1&gt;y1 x2&gt;y2) for a &quot;firmer&quot; feel. Sigmoid shaped curves are permitted (x1&gt;y1 x2&lt;y2 or x1&lt;y1 x2&gt;y2). Default: 0 0 100 100, a linear curve; range of 0 to 100 for all four values.</p>
<dt><code>RawSample</code> level</p>
<dd> Set the sample window size (a sliding average sampling window) for incoming input tool raw data points. Default: 4, range of 1 to 20.</p>
<dt><code>Rotate</code> none|half|cw|ccw</p>
<dd> Set the tablet to the given rotation:<br />
&nbsp;<wbr>&nbsp;none: the tablet is not rotated and uses its natural rotation<br />
&nbsp;<wbr>&nbsp;half: the tablet is rotated by 180 degrees&nbsp;(upside-down)<br />
&nbsp;<wbr>&nbsp;cw: the tablet is rotated 90 degrees clockwise<br />
&nbsp;<wbr>&nbsp;ccw: the tablet is rotated 90 degrees counter-clockwise </p>
<p> Rotation is a tablet-wide option: rotation of one tool affects all other tools associated with the same tablet. When the tablet is physically rotated, rotate any tool to the corresponding orientation. Default: none</p>
<dt><code>Suppress</code> level</p>
<dd> Set the delta (difference) cutoff level for further processing of incoming input tool coordinate values. For example a X or Y coordinate event will be sent only if the change between the current X or Y coordinate and the previous one is greater than the Suppress value. The same applies to pressure level (Z coordinate) and Tilt rotation values. With a current absolute wheel (AbsWheel) or Tilt value the delta between it and the previous value must be equal to or greater than the Suppress value in order to be sent on. Suppress is a tablet wide parameter. A specified delta level for one input tool is applied to all input tool coordinates. To disable suppression use a level of 0. Default: 2, range of 0 to 100.</p>
<dt><code>TabletDebugLevel</code> level</p>
<dd> Set the debug level for this tablet to the given level. This only affects code paths that are shared between several tools on the same physical tablet. A higher level means more fine-grained debug messages, a level of 0 turns debugging off for this tool. Requires the driver to be built with debugging enabled. See also ToolDebugLevel. Default: 0, range of 0 to 12.</p>
<dt><code>TabletPCButton</code> on|off</p>
<dd> If on, the stylus must be in contact with the screen for a stylus side button to work. If off, stylus buttons will work once the stylus is in proximity of the tablet (regardless of whether it is touching the screen). Default: on for Tablet PCs; off for all other models.</p>
<dt><code>ToolSerialPrevious</code></p>
<dd> Get the serial number of the tool that was last in proximity last. This serial number is updated whenever the tool goes out of proximity. If the current tool went out of proximity once, this serial number is the one of the current tool. This is a read-only parameter.</p>
<dt><code>Touch</code> on|off</p>
<dd> If on, touch events are reported to userland, i.e., system cursor moves when user touches the tablet. If off, touch events are ignored. Default: on for devices that support touch; off for all other models.</p>
<dt><code>HWTouchSwitchState</code> on|off</p>
<dd> If on, it means touch switch is turned off. That is, touch events are reported to userland. If off, touch switch is turned on, i.e., touch events are ignored. This is a read-only parameter. Initial touch switch state is retrieved from the kernel when X driver starts.</p>
<dt><code>CursorProximity</code> distance</p>
<dd> Set the distance at which a relative tool is treated as being out of proximity. Beyond this distance the cursor will stop responding to tool motion. The default value for pucks is 10 (Intuos Pro) or 42 (Intuos/Bamboo). The default value for pens is 30.</p>
<dt><code>Threshold</code> level</p>
<dd> Set the minimum pressure necessary to generate a Button event for the stylus tip, eraser, or touch. The pressure levels of all tablets are normalized to 2048 levels irregardless of the actual hardware supported levels. This parameter is independent of the PressureCurve parameter. Default: 27, range of 0 to 2047.</p>
<dt><code>ToolDebugLevel</code> level</p>
<dd> Set the debug level for this tool to the given level. This only affects code paths that are specific to a given tool. A higher level means more fine-grained debug messages, a level of 0 turns debugging off for this tool. Requires the driver to be built with debugging enabled. See also TabletDebugLevel. Default: 0, range of 0 to 12.</p>
<dt><code>PressureRecalibration</code> on|off</p>
<dd> If the initial pressure of a device is != 0 the driver recalibrates the pressure range. This is to account for worn out devices. The downside is that when the user hits the tablet very hard the initial pressure reading may be unequal to zero even for a perfectly good pen. If the consecutive pressure readings are not higher than the initial pressure by a threshold no button event will be generated. This option allows to disable the recalibration. Default: on</p>
<dt><code>PanScrollThreshold</code> distance</p>
<dd> This specifies the distance the pen must move (in tablet units) before a scroll event is generated when using the &quot;pan&quot; action. Smaller values will require less distance and be more sensitive. Larger values will require more distance and be less sensitive. Default: 1300 or 2600 depending on tablet resolution (corresponds to 13 mm of distance). </p>
</dl>
<h2>WAYLAND SUPPORT</h2>
<p> This tool provides access to the device properties implemented in the <code>xf86-input-wacom</code> X server input module. It does not work under a Wayland compositor as the input module is not active.</p>
<dl>
<dt>See <a rel="nofollow" href="https://github.com/linuxwacom/xf86-input-wacom/wiki/Wayland">https://github.com/linuxwacom/xf86-input-wacom/wiki/Wayland</a> for details.</p>
<dd>
</dl>
<h2>AUTHORS</h2>
<p> Peter Hutterer &lt;peter.hutterer [at] redhat.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/4-wacom/">wacom</a>(4), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
<p> More information is available at <a rel="nofollow" href="https://github.com/linuxwacom/xf86-input-wacom">https://github.com/linuxwacom/xf86-input-wacom</a> </p>
<h2>Index</h2>
