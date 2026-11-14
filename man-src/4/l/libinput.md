---
title: "libinput(4)"
name: "libinput"
section: "4"
letter: "l"
url: "/docs/linux/man/4-libinput/"
description: "libinput – libinput-based X.Org input driver"
---

<p>libinput &#8211; libinput-based X.Org input driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;libinput&#34;</code>
<code> Option &#34;Device&#34; &#34;</code><i>devpath</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Note</h2>
<p>This is the man page for the X input driver. If you are looking for the library documentation, go to <code><a rel="nofollow" href="http://wayland.freedesktop.org/libinput/doc/">http://wayland.freedesktop.org/libinput/doc/</a></code></p>
<h2>Description</h2>
<p><code>libinput</code> is an Xorg input driver based on libinput. It therefore supports all input devices that libinput can handle, including most mice, keyboards, tablets and touchscreens. It is recommended that <code>libinput</code> devices are configured through the <code>InputClass</code> directive (refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5)) instead of manual per-device configuration. Devices configured in the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) are not hot-plug capable. </p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;AccelProfile&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Sets the pointer acceleration profile to the given profile. Permitted values are <code>adaptive,</code> <code>flat.</code> Not all devices support this option or all profiles. If a profile is unsupported, the default profile for this device is used. For a description on the profiles and their behavior, see the libinput documentation.</p>
<dt><code>Option &#34;AccelSpeed&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Sets the pointer acceleration speed within the range [-1, 1]</p>
<dt><code>Option &#34;ButtonMapping&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Sets the logical button mapping for this device, see <a href="/docs/linux/man/3-xsetpointermapping/">XSetPointerMapping</a>(3). The string must be a space-separated list of button mappings in the order of the logical buttons on the device, starting with button 1. The default mapping is &quot;1 2 3 &#8230; 32&quot;. A mapping of 0 deactivates the button. Multiple buttons can have the same mapping. Invalid mapping strings are discarded and the default mapping is used for all buttons. Buttons not specified in the user&#8217;s mapping use the default mapping. See section <code>BUTTON MAPPING</code> for more details.</p>
<dt><code>Option &#34;CalibrationMatrix&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>A string of 9 space-separated floating point numbers, in the order &#34;a b c d e f g h i&#34;. Sets the calibration matrix to the 3&#215;3 matrix where the first row is (abc), the second row is (def) and the third row is (ghi).</p>
<dt><code>Option &#34;ClickMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Enables a click method. Permitted values are <code>none,</code> <code>buttonareas,</code> <code>clickfinger.</code> Not all devices support all methods, if an option is unsupported, the default click method for this device is used.</p>
<dt><code>Option &#34;DisableWhileTyping&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Indicates if the touchpad should be disabled while typing on the keyboard (this does not apply to modifier keys such as Ctrl or Alt).</p>
<dt><code>Option &#34;Device&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specifies the device through which the device can be accessed. This will generally be of the form &#34;/dev/input/eventX&#34;, where X is some integer. When using <code>InputClass</code> directives, this option is set by the server. The mapping from device node to hardware is system-dependent. Property: &quot;Device Node&quot; (read-only).</p>
<dt><code>Option &#34;DragLockButtons&#34; &#34;</code><i>L1 B1 L2 B2 &#8230;</i><code>&#34;</code></p>
<dd>Sets &quot;drag lock buttons&quot; that simulate a button logically down even when it has been physically released. To logically release a locked button, a second click of the same button is required.</p>
<dd>If the option is a single button number, that button acts as the &quot;meta&quot; locking button for the next button number. See section <code>BUTTON DRAG LOCK</code> for details.</p>
<dd>If the option is a list of button number pairs, the first number of each number pair is the lock button, the second number the logical button number to be locked. See section <code>BUTTON DRAG LOCK</code> for details.</p>
<dd>For both meta and button pair configuration, the button numbers are device button numbers, i.e. the <code>ButtonMapping</code> applies after drag lock.</p>
<dt><code>Option &#34;HighResolutionWheelScrolling&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Disables high-resolution wheel scroll events, enabled by default. When enabled, the driver forwards only high-resolution wheel scroll events from libinput. When disabled, the driver forwards legacy wheel scroll events instead.</p>
<dt><code>Option &#34;HorizontalScrolling&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Disables horizontal scrolling. When disabled, this driver will discard any horizontal scroll events from libinput. Note that this does not disable horizontal scrolling, it merely discards the horizontal axis from any scroll events.</p>
<dt><code>Option &#34;LeftHanded&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Enables left-handed button orientation, i.e. swapping left and right buttons.</p>
<dt><code>Option &#34;MiddleEmulation&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Enables middle button emulation. When enabled, pressing the left and right buttons simultaneously produces a middle mouse button click.</p>
<dt><code>Option &#34;NaturalScrolling&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Enables or disables natural scrolling behavior.</p>
<dt><code>Option &#34;RotationAngle&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Sets the rotation angle of the device to the given angle, in degrees clockwise. The angle must be between 0.0 (inclusive) and 360.0 (exclusive).</p>
<dt><code>Option &#34;ScrollButton&#34; &#34;</code><i>int</i><code>&#34;</code></p>
<dd>Designates a button as scroll button. If the <code>ScrollMethod</code> is <code>button</code> and the button is logically down, x/y axis movement is converted into scroll events.</p>
<dt><code>Option &#34;ScrollButtonLock&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Enables or disables the scroll button lock. If enabled, the <code>ScrollButton</code> is considered logically down after the first click and remains down until the second click of that button. If disabled (the default), the <code>ScrollButton</code> button is considered logically down while held down and up once physically released.</p>
<dt><code>Option &#34;ScrollMethod&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Enables a scroll method. Permitted values are <code>none,</code> <code>twofinger,</code> <code>edge,</code> <code>button.</code> Not all devices support all options, if an option is unsupported, the default scroll option for this device is used.</p>
<dt><code>Option &#34;ScrollPixelDistance&#34; &#34;</code><i>int</i><code>&#34;</code></p>
<dd>Sets the movement distance, in &quot;pixels&quot;, required to trigger one logical wheel click. This option only applies to the scroll methods <code>twofinger,</code> <code>edge,</code> <code>button.</code> See section <code>SCROLL PIXEL DISTANCE</code> for more details.</p>
<dt><code>Option &#34;SendEventsMode&#34; &#34;</code><i>(disabled|enabled|disabled-on-external-mouse)</i><code>&#34;</code></p>
<dd>Sets the send events mode to disabled, enabled, or &quot;disable when an external mouse is connected&quot;.</p>
<dt><code>Option &#34;TabletToolPressureCurve&#34; &#34;</code><i>x0/y0 x1/y1 x2/y2 x3/y3</i><code>&#34;</code></p>
<dd>Set the pressure curve for a tablet stylus to the bezier formed by the four points. The respective x/y coordinate must be in the [0.0, 1.0] range. For more information see section <code>TABLET STYLUS PRESSURE CURVE.</code></p>
<dt><code>Option &#34;TabletToolAreaRatio&#34; &#34;</code><i>w:h</i><code>&#34;</code></p>
<dd>Sets the area ratio for a tablet tool. The area always starts at the origin (0/0) and expands to the largest available area with the specified aspect ratio. Events outside this area are cropped to the area. The special value &quot;default&quot; is used for the default mapping (i.e. the device-native mapping). For more information see section <code>TABLET TOOL AREA RATIO.</code></p>
<dt><code>Option &#34;Tapping&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Enables or disables tap-to-click behavior.</p>
<dt><code>Option &#34;TappingButtonMap&#34; &#34;</code><i>(lrm|lmr)</i><code>&#34;</code></p>
<dd>Set the button mapping for 1/2/3-finger taps to left/right/middle or left/middle/right, respectively.</p>
<dt><code>Option &#34;TappingDrag&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Enables or disables drag during tapping behavior (&quot;tap-and-drag&quot;). When enabled, a tap followed by a finger held down causes a single button down only, all motions of that finger thus translate into dragging motion. Tap-and-drag requires option <code>Tapping</code> to be enabled.</p>
<dt><code>Option &#34;TappingDragLock&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>Enables or disables drag lock during tapping behavior. When enabled, a finger up during tap-and-drag will not immediately release the button. If the finger is set down again within the timeout, the dragging process continues.</dl>
<p> For all options, the options are only parsed if the device supports that configuration option. For all options, the default value is the one used by libinput. On configuration failure, the default value is applied.</p>
<h2>Supported Properties</h2>
<p><code>libinput</code> exports runtime-configurable options as properties. If a property listed below is not available, the matching configuration option is not available on the device. This however does not imply that the feature is not available on the device. The following properties are provided by the <code>libinput</code> driver.</p>
<dl>
<dt><code>libinput Accel Profiles Available</code></p>
<dd>2 boolean values (8 bit, 0 or 1), in order &quot;adaptive&quot;, &quot;flat&quot;. Indicates which acceleration profiles are available on this device.</p>
<dt><code>libinput Accel Profile Enabled</code></p>
<dd>2 boolean values (8 bit, 0 or 1), in order &quot;adaptive&quot;, &quot;flat&quot;. Indicates which acceleration profile is currently enabled on this device.</p>
<dt><code>libinput Accel Speed</code></p>
<dd>1 32-bit float value, defines the pointer speed. Value range -1, 1</p>
<dt><code>libinput Button Scrolling Button</code></p>
<dd>1 32-bit value. Sets the button number to use for button scrolling. This setting is independent of the scroll method, to enable button scrolling the method must be set to button-scrolling and a valid button must be set.</p>
<dt><code>libinput Button Scrolling Button Lock Enabled</code></p>
<dd>1 boolean value. If true, the scroll button lock is enabled. This setting is independent of the scroll method or the scroll button, to enable button scrolling the method must be set to button-scrolling and a valid button must be set.</p>
<dt><code>libinput Calibration Matrix</code></p>
<dd>9 32-bit float values, representing a 3&#215;3 calibration matrix, order is row 1, row 2, row 3</p>
<dt><code>libinput Click Methods Available</code></p>
<dd>2 boolean values (8 bit, 0 or 1), in order &quot;buttonareas&quot;, &quot;clickfinger&quot;. Indicates which click methods are available on this device.</p>
<dt><code>libinput Click Methods Enabled</code></p>
<dd>2 boolean values (8 bit, 0 or 1), in order &quot;buttonareas&quot;, &quot;clickfinger&quot;. Indicates which click methods are enabled on this device.</p>
<dt><code>libinput Drag Lock Buttons</code></p>
<dd>Either one 8-bit value specifying the meta drag lock button, or a list of button pairs. See section <code>BUTTON DRAG LOCK</code> for details.</p>
<dt><code>libinput High Resolution Wheel Scroll Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). Indicates whether high-resolution wheel scroll events are enabled or not.</p>
<dt><code>libinput Horizontal Scroll Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). Indicates whether horizontal scrolling events are enabled or not.</p>
<dt><code>libinput Left Handed Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). Indicates if left-handed mode is enabled or disabled.</p>
<dt><code>libinput Middle Emulation Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). Indicates if middle emulation is enabled or disabled.</p>
<dt><code>libinput Natural Scrolling Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). 1 enables natural scrolling</p>
<dt><code>libinput Rotation Angle</code></p>
<dd>1 32-bit float value [0.0 to 360.0). Sets the rotation angle of the device, clockwise of its natural neutral position.</p>
<dt><code>libinput Scroll Methods Available</code></p>
<dd>3 boolean values (8 bit, 0 or 1), in order &quot;two-finger&quot;, &quot;edge&quot;, &quot;button&quot;. Indicates which scroll methods are available on this device.</p>
<dt><code>libinput Scroll Method Enabled</code></p>
<dd>3 boolean values (8 bit, 0 or 1), in order &quot;two-finger&quot;, &quot;edge&quot;, &quot;button&quot;. Indicates which scroll method is currently enabled on this device.</p>
<dt><code>libinput Scroll Pixel Distance</code></p>
<dd>1 32-bit value (nonzero, with additional implementation-defined range checks). Changes the movement distance required to trigger one logical wheel click.</p>
<dt><code>libinput Send Events Modes Available</code></p>
<dd>2 boolean values (8 bit, 0 or 1), in order &quot;disabled&quot; and &quot;disabled-on-external-mouse&quot;. Indicates which send-event modes are available on this device.</p>
<dt><code>libinput Send Events Mode Enabled</code></p>
<dd>2 boolean values (8 bit, 0 or 1), in order &quot;disabled&quot; and &quot;disabled-on-external-mouse&quot;. Indicates which send-event modes is currently enabled on this device.</p>
<dt><code>libinput Tablet Tool Pressurecurve</code></p>
<dd>4 32-bit float values [0.0 to 1.0]. See section <code>TABLET TOOL PRESSURE CURVE</code></p>
<dt><code>libinput Tablet Tool Area Ratio</code></p>
<dd>2 32-bit values, corresponding to width and height. Special value 0, 0 resets to the default ratio. See section <code>TABLET TOOL AREA RATIO</code> for more information.</p>
<dt><code>libinput Tapping Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). 1 enables tapping</p>
<dt><code>libinput Tapping Button Mapping Enabled</code></p>
<dd>2 boolean value (8 bit, 0 or 1), in order &quot;lrm&quot; and &quot;lmr&quot;. Indicates which button mapping is currently enabled on this device.</p>
<dt><code>libinput Tapping Drag Lock Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). 1 enables drag lock during tapping</p>
<dt><code>libinput Disable While Typing Enabled</code></p>
<dd>1 boolean value (8 bit, 0 or 1). Indicates if disable while typing is enabled or disabled.</dl>
<p> Most properties have a <code>libinput &lt;property name&gt; Default</code> equivalent that indicates the default value for this setting on this device.</p>
<h2>Button Mapping</h2>
<p>X clients receive events with logical button numbers, where 1, 2, 3 are usually interpreted as left, middle, right and logical buttons 4, 5, 6, 7 are usually interpreted as scroll up, down, left, right. The fourth and fifth physical buttons on a device will thus send logical buttons 8 and 9. The <code>ButtonMapping</code> option adjusts the logical button mapping, it does not affect how a physical button is mapped to a logical button. </p>
<p> Traditionally, a device was set to left-handed button mode by applying a button mapping of <code>&#34;3 2 1 &#8230;&#34;</code> On systems using the <code>libinput</code> Xorg input driver it is recommended to use the <code>LeftHanded</code> option instead. </p>
<p> The <code>libinput</code> Xorg input driver does not use the button mapping after setup. Use <a href="/docs/linux/man/3-xsetpointermapping/">XSetPointerMapping</a>(3) to modify the button mapping at runtime.</p>
<h2>Button Drag Lock</h2>
<p>Button drag lock holds a button logically down even when the button itself has been physically released since. Button drag lock comes in two modes. </p>
<p> If in &quot;meta&quot; mode, a meta button click activates drag lock for the next button press of any other button. A button click in the future will keep that button held logically down until a subsequent click of that same button. The meta button events themselves are discarded. A separate meta button click is required each time a drag lock should be activated for a button in the future. </p>
<p> If in &quot;pairs&quot; mode, each button can be assigned a target locking button. On button click, the target lock button is held logically down until the next click of the same button. The button events themselves are discarded and only the target button events are sent.</p>
<dl>
<dt>This feature is provided by this driver, not by libinput.</p>
<dd></dl>
<h2>Tablet Tool Pressurecurve</h2>
<p>The pressure curve affects how stylus pressure is reported. By default, the hardware pressure is reported as-is. By setting a pressure curve, the feel of the stylus can be adjusted to be more like e.g. a pencil or a brush. </p>
<p> The pressure curve is a cubic Bezier curve, drawn within a normalized range of 0.0 to 1.0 between the four points provided. This normalized range is applied to the tablet&#8217;s pressure input so that the highest pressure maps to 1.0. The points must have increasing x coordinates, if x0 is larger than 0.0 all pressure values lower than x0 are equivalent to y0. If x3 is less than 1.0, all pressure values higher than x3 are equivalent to y3. </p>
<p> The input for a linear curve (default) is &quot;0.0/0.0 0.0/0.0 1.0/1.0 1.0/1.0&quot;; a slightly depressed curve (firmer) might be &quot;0.0/0.0 0.05/0.0 1.0/0.95 1.0/1.0&quot;; a slightly raised curve (softer) might be &quot;0.0/0.0 0.0/0.05 0.95/1.0 1.0/1.0&quot;.</p>
<dl>
<dt>This feature is provided by this driver, not by libinput.</p>
<dd></dl>
<h2>Tablet Tool Area Ratio</h2>
<p>By default, a tablet tool can access the whole sensor area and the tablet area is mapped to the available screen area. For external tablets like the Wacom Intuos series, the height:width ratio of the tablet may be different to that of the monitor, causing the skew of input data. </p>
<p> To avoid this skew of input data, an area ratio may be set to match the ratio of the screen device. For example, a ratio of 4:3 will reduce the available area of the tablet to the largest available area with a ratio of 4:3. Events within this area will scale to the tablet&#8217;s announced axis range, the area ratio is thus transparent to the X server. Any events outside this area will send events equal to the maximum value of that axis. The area always starts at the device&#8217;s origin in it&#8217;s current rotation, i.e. it takes left-handed-ness into account.</p>
<dl>
<dt>This feature is provided by this driver, not by libinput.</p>
<dd></dl>
<h2>Scroll Pixel Distance</h2>
<p>The X server does not support per-pixel scrolling but it does support smooth scrolling. All scroll events however are based around a logical unit of scrolling (traditionally corresponding to a wheel click). It is thus not possible to scroll by 10 pixels, but it is possible for a driver to scroll by 1/10th of a logical wheel click. </p>
<p> libinput provides scroll data in pixels. The <code>ScrollPixelDistance</code> option defines the amount of movement equivalent to one wheel click. For example, a value of 50 means the user has to move a finger by 50 pixels to generate one logical click event and each pixel is 1/50th of a wheel click.</p>
<h2>Bugs</h2>
<p>This driver does not work with <code>Option &#34;Device&#34;</code> set to an event node in <i>/dev/input/by-id</i> and <i>/dev/input/by-path</i>. This can be usually be worked by using <code>Section &#34;InputClass&#34;</code> with an appropriate <code>Match*</code> statement in the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5). </p>
<h2>Authors</h2>
<p>Peter Hutterer</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
