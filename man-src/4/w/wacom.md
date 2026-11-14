---
title: "wacom(4)"
name: "wacom"
section: "4"
letter: "w"
url: "/docs/linux/man/4-wacom/"
description: "wacom – Wacom input driver"
---

<p>wacom &#8211; Wacom input driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>idevname</i><code>&#34;</code>
<code> Driver &#34;wacom&#34;</code>
<code> Option &#34;Device&#34; &#34;</code><i>devpath</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>wacom</code> is an X input driver for Wacom devices. </p>
<p> The <code>wacom</code> driver functions as a pointer input device.</p>
<h2>Supported Hardware</h2>
<p>This driver supports the Wacom IV and Wacom V protocols. Serial tablets only need this driver. USB tablet support is available on some Linux platforms and requires the wacom kernel driver being loaded before this driver starts. </p>
<p> Please check <a rel="nofollow" href="https://github.com/linuxwacom">https://github.com/linuxwacom</a> for latest updates of Wacom X and kernel drivers.</p>
<h2>Driver-Internal Device Hotplugging</h2>
<p>When input device hotplugging in the X server is enabled and no <code>InputDevice</code> section exists for a compatible tablet device and an <code>InputClass</code> section (see <a href="//www.systutorials.com/docs/linux/man/5x-xorg.conf.d/">xorg.conf.d</a>(5x)) assigns this driver for the device, the <code>wacom</code> driver creates multiple X devices for each a physical device, one X device for each available tool. The list of tools is hardware-dependent. See <code>Option Type</code> as outlined in the <code>CONFIGURATION DETAILS</code> section. </p>
<p> These tool-specific devices are referred to as parent device and dependent device. The parent device is the one presented by the system and the one that causes the X server to load the <code>wacom</code> driver. This parent device then causes the automatic addition of several dependent devices. If the parent device is unplugged or otherwise removed, the dependent devices will be automatically removed as well. </p>
<p> Dependent devices may be assigned tool-specific options through additional <code>InputClass</code> sections. We recommend that a <code>MatchDriver wacom</code> line is used in these sections in addition to the user-specific pattern. </p>
<p> Match directives are applied by the X server before the driver is selected. The type name of the parent device is appended by the driver. It is not possible to use a <code>MatchProduct</code> directive to match against this appended type name.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="//www.systutorials.com/docs/linux/man/5x-xorg.conf/">xorg.conf</a>(5x) or <a href="//www.systutorials.com/docs/linux/man/5x-xorg.conf.d/">xorg.conf.d</a>(5x) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> Multiple instances of the Wacom devices can cohabit. Each device supports the following entries:</p>
<dl>
<dd>
<dl>
<dt><code>Option </code><i>Type</i> <i>stylus|eraser|cursor|pad|touch</i></p>
<dd>sets the type of tool the device represents. This option is mandatory. The core options, such as &quot;SendCoreEvents&quot; or &quot;AlwaysCore&quot;, are unnecessary in Gimp if you don&#8217;t need to move system cursor outside of Gimp drawing area. &quot;pad&quot; is for Intuos 3 or Cintiq 21UX tablet ExpressKeys/menu strips, and Graphire 4 or Bamboo tablet buttons, wheel, and/or ring. It is required for Intuos3, CintiqV5, Graphire 4, and Bamboo if you want to use keystroke features. &quot;pad&quot; is reported as a second tool in the driver. &quot;touch&quot; is for the tablet with touch support. Right now only a few Tablet PCs have this feature.</p>
<dt><code>Option </code><i>Device</i> <i>path</i></p>
<dd>sets the path to the special file which represents serial line where the tablet is plugged. You have to specify it for each subsection with the same value if you want to have multiple devices with the same tablet. This option is mandatory.</p>
<dt><code>Option </code><i>Suppress</i> <i>number</i></p>
<dd>sets the position increment under which not to transmit coordinates. This entry must be specified only in the first Wacom subsection if you have multiple devices for one tablet. If you don&#8217;t specify this entry, the default value, which is 2, will be used. To disable suppression, the entry should be specified as 0. When suppress is defined, an event will be sent only when at least one of the following conditions is met: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the change between the current X coordinate and the previous one is greater than suppress; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the change between the current Y coordinate and the previous one is greater than suppress; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the change between the current pressure and the previous one is greater than suppress; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the change between the&nbsp;<wbr>&nbsp;current degree of rotation and the previous one of the transducer is greater than suppress; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the change between the current absolute wheel value and the previous one is equal to or greater than suppress; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the change between the current tilt value and the previous one is equal to or greater than suppress (if tilt is supported); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;relative wheel value has changed; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;button value has changed; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proximity has changed.</p>
<dt><code>Option </code><i>Mode</i> <i>Relative|Absolute</i></p>
<dd>sets the mode of the device. The default value for stylus, pad and eraser is Absolute; cursor is Relative; touch defaults to Relative for tablets with touch pads and Absolute for touch screens.</p>
<dt><code>Option </code><i>TopX</i> <i>number</i></p>
<dd>X coordinate of the top corner of the active zone. Default to 0.</p>
<dt><code>Option </code><i>TopY</i> <i>number</i></p>
<dd>Y coordinate of the top corner of the active zone. Default to 0.</p>
<dt><code>Option </code><i>BottomX</i> <i>number</i></p>
<dd>X coordinate of the bottom corner of the active zone. Default to width of the tablet.</p>
<dt><code>Option </code><i>BottomY</i> <i>number</i></p>
<dd>Y coordinate of the bottom corner of the active zone. Default to height of the tablet.</p>
<dt><code>Option </code><i>ButtonsOnly</i> <i>on|off</i></p>
<dd>disables the device&#8217;s motion events. Default to off.</p>
<dt><code>Option </code><i>ButtonM</i> <i>AC</i></p>
<dd>reports an action AC when button M is pressed, where M is one of the device supported button numbers, it can be 1 to 32. Wacom uses a driver-internal button mapping, where any physical button appears to the X server as the button specified by the ButtonM mapping. Hence, if two physical buttons have the same ButtonM mapping, the server will think they are the same physical button. The default action reported to the X server is mouse button M click. Because X uses buttons 4, 5, 6, and 7 as the four scrolling directions, physical buttons 4 and higher are mapped to 8 and higher by default. Only simple button presses can be configured here; for more complex actions, use <a href="/docs/linux/man/1-xsetwacom/">xsetwacom</a>(1). To ignore the button click, i.e., to not report any button click event to the X server, use &quot;0&quot; or &quot;button 0&quot;.</p>
<dt><code>Option </code><i>TPCButton</i> <i>on|off</i></p>
<dd>enables the stylus buttons as Tablet PC buttons. If enabled, the stylus reports button events only when its tip is pressed. If any button is down, pressing the tip reports a button event for the button. Otherwise if no button is down, the tip reports as usual. Default to &quot;on&quot; for Tablet PCs; &quot;off&quot; for all other models. Only available on the stylus tool.</p>
<dt><code>Option </code><i>Touch</i> <i>on|off</i></p>
<dd>enables touch events for touch devices, i.e., system cursor moves when user touches the tablet. Default to &quot;on&quot; for devices that support touch; &quot;off&quot; for all other models.</p>
<dt><code>Option </code><i>Rotate</i> <i>CW|CCW|HALF|NONE</i></p>
<dd>rotates the tablet orientation counterclockwise (CCW) or clockwise (CW) or 180 degrees (HALF). If you have specific tablet mappings, i.e. TopX/Y or BottomX/Y were set, the mapping will be applied before rotation. Rotation must be applied to the parent device (usually the stylus), rotation settings on in-driver hotplugged devices (see <code>DRIVER-INTERNAL DEVICE HOTPLUGGING</code> ) will be ignored. The default is &quot;NONE&quot;.</p>
<dt><code>Option </code><i>PressCurve</i> <i>x1,y1,x2,y2</i></p>
<dd>sets pressure curve by control points x1, y1, x2, and y2. Their values are in range from 0..100. The pressure curve is interpreted as Bezier curve with 4 control points, the first and the last control point being fixed on the coordinates 0/0 and 100/100, respectively. The middle control points are adjustible by this setting and thus define the shape of the curve. The input for linear curve (default) is &quot;0,0,100,100&quot;; slightly depressed curve (firmer) might be &quot;5,0,100,95&quot;; slightly raised curve (softer) might be &quot;0,5,95,100&quot;. The pressure curve is only applicable to devices of type stylus or eraser, other devices do not honor this setting.</p>
<dt><code>Option </code><i>Pressure2K</i> <i>bool</i></p>
<dd>reduces the pressure range to the range of 0 to 2048 for backwards compatibility with applications that have this range hardcoded. See section <code>BUGS.</code> This option should not be used unless the user runs one or more applications that rely on a hardcoded pressure range.</p>
<dt><code>Option </code><i>DebugLevel</i> <i>number</i></p>
<dd>sets the level of debugging info for tool-specific messages. There are 12 levels, specified by the integers between 1 and 12. All debug messages with a level less than or equal to the &quot;number&quot; will be logged into the Xorg log file. This option is only available if the driver was built with debugging support.</p>
<dt><code>Option </code><i>CommonDBG</i> <i>number</i></p>
<dd>sets the level of debugging info for common (i.e. not tool-specific) code paths on the tablet. There are 12 levels, specified by the integers between 1 and 12. All debug messages with a level less than or equal to the &quot;number&quot; will be logged into the Xorg log file. This option is only available if the driver was built with debugging support.</p>
<dt><code>Option </code><i>GrabDevice</i> <i>bool</i></p>
<dd>sets whether the underlying event device will be grabbed by the driver to prevent the data from leaking to /dev/input/mice. When enabled, while the X server is running, no other programs will be able to read the event stream. Default: &quot;false&quot;.</p>
<dt><code>Option </code><i>CursorProx</i> <i>number</i></p>
<dd>sets the distance at which a relative tool is treated as being out of proximity. Beyond this distance the cursor will stop responding to tool motion. The default value for pucks is 10 (Intuos Pro) or 42 (Intuos/Bamboo). The default value for pens is 30.</p>
<dt><code>Option </code><i>RawSample</i> <i>number</i></p>
<dd>Set the sample window size (a sliding average sampling window) for incoming input tool raw data points. Default: 4, range of 1 to 20.</p>
<dt><code>Option </code><i>Serial</i> <i>number</i></p>
<dd>sets the serial number associated with the physical device. This allows to have multiple devices of the same type (i.e. multiple pens). This option is only available on wacom V devices (Intuos series and Cintiq 21U). To see which serial number belongs to a device, you need to run the utility program, xsetwacom, which comes with linuxwacom package.</p>
<dt><code>Option </code><i>ToolSerials</i> <i>number[,type[,label]][;&#8230;]</i></p>
<dd>sets the list of serial numbered devices that need to be hotplugged for a physical device. The &#8216;type&#8217; option may be any of &quot;pen&quot;, &quot;airbrush&quot;, &quot;artpen&quot;, or &quot;cursor&quot;. This option is only available on wacom V devices which are capable of reporting a serial number. To see if a connected device is supported, or to identify which serial number belongs to a device, you need to run the utility program, xsetwacom, that comes with this driver. In layman&#8217;s terms, this option will add additional X devices for this specific tool&#8217;s tip (and eraser, if applicable). This is useful for programs like gimp (which remembers tools based on the X device) to recall additional drawing tool selections for an airbrush+eraser, art pen, extra pen, etc.</p>
<dt><code>Option </code><i>Threshold</i> <i>number</i></p>
<dd>sets the pressure threshold used to generate a button 1 events of stylus. The threshold applies to the normalised pressure range of [0..2048]. The default is 27.</p>
<dt><code>Option </code><i>Gesture</i> <i>bool</i></p>
<dd>Enable or disable multi-finger in-driver gesture support on the device. Default: off unless the tablet supports multi-touch. Note that disabling this option may allow the desktop environment to detect multi-finger gestures instead.</p>
<dt><code>Option </code><i>ZoomDistance</i> <i>number</i></p>
<dd>If <code>Option </code><i>Gesture</i> is enabled, this option specifies the minimum movement distance before a zoom gesture is recognized.</p>
<dt><code>Option </code><i>ScrollDistance</i> <i>number</i></p>
<dd>If <code>Option </code><i>Gesture</i> is enabled, this option specifies the minimum movement distance before a scroll gesture is recognized.</p>
<dt><code>Option </code><i>TapTime</i> <i>number</i></p>
<dd>If <code>Option </code><i>Gesture</i> is enabled, this option determines the maximum time of a touch event to be recognized as tap. A press and release event shorter than <code>TapTime</code> generates button press and release events. Presses longer than <code>TapTime</code> do not generate button events, only motion events.</p>
<dt><code>Option </code><i>PressureRecalibration</i> <i>bool</i></p>
<dd>Allows to disable pressure recalibration. Default: true. If the initial pressure of a device is != 0 the driver recalibrates the pressure range. This is to account for worn out devices. The downside is that when the user hits the tablet very hard the initial pressure reading may be unequal to zero even for a perfectly good pen. If the consecutive pressure readings are not higher than the initial pressure by a threshold no button event will be generated. This option allows to disable the recalibration.</p>
<dt><code>Option </code><i>PanScrollThreshold</i> <i>number</i></p>
<dd>Specifies the distance the pen must move (in tablet units) before a scroll event is generated when using the &quot;pan&quot; action. Smaller values will require less distance and be more sensitive. Larger values will require more distance and be less sensitive. Default: 1300 or 2600 depending on tablet resolution (corresponds to 13 mm of distance).</dl>
</dl>
<h2>Touch Gestures</h2>
<h3>Single finger (1FG)</h3>
<p><code>Left click:</code> tap, actual click happens after TapTime period elapses. </p>
<p> <code>Left click drag:</code> tap to select, quickly (within TapTime period) touch selection again. Then drag. Available on touchpads, e.g. BambooPT, not touchscreens.</p>
<h3>Two finger (2FG)</h3>
<p><code>Right click:</code> one finger down + tap second finger </p>
<p> <code>Vertical scroll:</code> two fingers side by side (in any orientation) moving vertically with constant separation initiates a vertical scroll. By driver default a gesture up results in a scroll down event (the document moves up) and a gesture down results in a scroll up event (moving the document down). </p>
<p> <code>Horizontal scroll:</code> two fingers side by side held at a constant distance moving horizontally initiates a horizontal scroll. A gesture to the left results in a scroll right event (the document moves left) and a gesture right results in a scroll left event (moving the document right). </p>
<p> <code>Zoom in:</code> two separated fingers side by side, bring together i.e. pinch. </p>
<p> <code>Zoom out:</code> two fingers side by side, spread. Not all applications support zoom.</p>
<h2>Bugs</h2>
<h3>Pressure range increase leads to unexpected behavior</h3>
<p>In version 0.34, the driver&#8217;s pressure range increased from 2048 steps to 65536 steps. The pressure axis range is advertised through the X Input Protocol but some applications have the previous pressure range hardcoded and cannot handle pressure values above 2048. This is an application bug but for backwards-compatibility with such applications, this driver provides the <code>Pressure2K</code> option to reduce the range to 2048 steps. Note that this setting applies to the device. Once applied, all applications will see the reduced pressure range. It is not possible to provide this setting on a per-application basis.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/5-xorg-conf-d/">xorg.conf.d</a>(5), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
<p> More information is available at <a rel="nofollow" href="https://github.com/linuxwacom/xf86-input-wacom">https://github.com/linuxwacom/xf86-input-wacom</a></p>
<h2>Authors</h2>
<p>Peter Hutterer &lt;peter.hutterer [at] who-t.net&gt;, Ping Cheng &lt;pingc [at] wacom.com&gt;, Frederic Lepied &lt;lepied [at] xfree86.org&gt;, John E. Joganic &lt;jej [at] j-arkadia.com&gt;, Magnus Vigerlöf &lt;Magnus.Vigerlof [at] ipbo.se&gt;</p>
