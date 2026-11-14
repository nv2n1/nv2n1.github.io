---
title: "evdev(4)"
name: "evdev"
section: "4"
letter: "e"
url: "/docs/linux/man/4-evdev/"
description: "evdev – Generic Linux input driver"
---

<p>evdev &#8211; Generic Linux input driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;evdev&#34;</code>
<code> Option &#34;Device&#34; &#34;</code><i>devpath</i><code>&#34;</code>
<code> Option &#34;Emulate3Buttons&#34; &#34;</code><i>True</i><code>&#34;</code>
<code> Option &#34;Emulate3Timeout&#34; &#34;</code><i>50</i><code>&#34;</code>
<code> Option &#34;GrabDevice&#34; &#34;</code><i>False</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>evdev </code> is an Xorg input driver for Linux&#8217;s generic event devices. It therefore supports all input devices that the kernel knows about, including most mice, keyboards, tablets and touchscreens. <code>evdev</code> is the default driver on the major Linux distributions. The <code>evdev</code> driver can serve as both a pointer and a keyboard input device. Multiple input devices are supported by multiple instances of this driver, with one InputDevice section of your xorg.conf for each input device that will use this driver. It is recommended that <code>evdev</code> devices are configured through the <code>InputClass</code> directive (refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5)) instead of manual per-device configuration. Devices configured in the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) are not hot-plug capable. </p>
<h2>Supported Hardware</h2>
<p>In general, any input device that the kernel has a driver for can be accessed through the <code>evdev</code> driver. See the Linux kernel documentation for a complete list.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;ButtonMapping&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Sets the button mapping for this device. The mapping is a space-separated list of button mappings that correspond in order to the physical buttons on the device (i.e. the first number is the mapping for button 1, etc.). The default mapping is &quot;1 2 3 &#8230; 32&quot;. A mapping of 0 deactivates the button. Multiple buttons can have the same mapping. For example, a left-handed mouse with deactivated scroll-wheel would use a mapping of &quot;3 2 1 0 0&quot;. Invalid mappings are ignored and the default mapping is used. Buttons not specified in the user&#8217;s mapping use the default mapping.</p>
<dt><code>Option &#34;Device&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specifies the device through which the device can be accessed. This will generally be of the form &#34;/dev/input/eventX&#34;, where X is some integer. The mapping from device node to hardware is system-dependent. Property: &quot;Device Node&quot; (read-only).</p>
<dt><code>Option &#34;DragLockButtons&#34; &#34;</code><i>L1 B2 L3 B4</i><code>&#34;</code></p>
<dd>Sets &#34;drag lock buttons&#34; that simulate holding a button down, so that low dexterity people do not have to hold a button down at the same time they move a mouse cursor. Button numbers occur in pairs, with the lock button number occurring first, followed by the button number that is the target of the lock button. Property: &quot;Evdev Drag Lock Buttons&quot;.</p>
<dt><code>Option &#34;DragLockButtons&#34; &#34;</code><i>M1</i><code>&#34;</code></p>
<dd>Sets a &#34;master drag lock button&#34; that acts as a &#34;Meta Key&#34; indicating that the next button pressed is to be &#34;drag locked&#34;. Property: &quot;Evdev Drag Lock Buttons&quot;.</p>
<dt>
<dt><code>Option &#34;Emulate3Buttons&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>
<dd>Enable/disable the emulation of the third (middle) mouse button for mice which only have two physical buttons. The third button is emulated by pressing both buttons simultaneously. Default: off. Property: &quot;Evdev Middle Button Emulation&quot;.</p>
<dt><code>Option &#34;Emulate3Timeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Sets the timeout (in milliseconds) that the driver waits before deciding if two buttons where pressed &quot;simultaneously&quot; when 3 button emulation is enabled. Default: 50. Property: &quot;Evdev Middle Button Timeout&quot;.</p>
<dt><code>Option &#34;Emulate3Button&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies the physical button number to be emitted if middle button emulation is triggered. Default: 2. Property: &quot;Evdev Middle Button Button&quot;.</p>
<dt><code>Option &#34;EmulateWheel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable/disable &quot;wheel&quot; emulation. Wheel emulation means emulating button press/release events when the mouse is moved while a specific real button is pressed. Wheel button events (typically buttons 4 and 5) are usually used for scrolling. Wheel emulation is useful for getting wheel-like behaviour with trackballs. It can also be useful for mice with 4 or more buttons but no wheel. See the description of the <code>EmulateWheelButton</code>, <code>EmulateWheelInertia</code>, <code>EmulateWheelTimeout</code>, <code>XAxisMapping</code>, and <code>YAxisMapping</code> options. Default: off. Property &quot;Evdev Wheel Emulation&quot;.</p>
<dt><code>Option &#34;EmulateWheelButton&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies which button must be held down to enable wheel emulation mode. While this button is down, X and/or Y pointer movement will generate button press/release events as specified for the <code>XAxisMapping</code> and <code>YAxisMapping</code> settings. If the button is 0 and <code>EmulateWheel</code> is on, any motion of the device is converted into wheel events. Default: 4. Property: &quot;Evdev Wheel Emulation Button&quot;.</p>
<dt><code>Option &#34;EmulateWheelInertia&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies how far (in pixels) the pointer must move to generate button press/release events in wheel emulation mode. Default: 10. Property: &quot;Evdev Wheel Emulation Inertia&quot;.</p>
<dd>This value must be set for any device does not resemble a standard mouse. Specifically, on absolute devices such as tablets the value should be set to a reasonable fraction of the expected movement to avoid excess scroll events.</p>
<dd><code>WARNING:</code> the name &#34;inertia&#34; is a misnomer. This option defines the distance required to generate one scroll event similar to the <code>VertScrollDelta</code> and <code>HorizScrollDelta</code> options. It does not enable inertia in the physical sense, scrolling stops immediately once the movement has stopped.</p>
<dt><code>Option &#34;EmulateWheelTimeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies the time in milliseconds the <code>EmulateWheelButton</code> must be pressed before wheel emulation is started. If the <code>EmulateWheelButton</code> is released before this timeout, the original button press/release event is sent. Default: 200. Property: &quot;Evdev Wheel Emulation Timeout&quot;.</p>
<dt><code>Option &#34;EmulateThirdButton&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable third button emulation. Third button emulation emits a right button event (by default) by pressing and holding the first button. The first button must be held down for the configured timeout and must not move more than the configured threshold for the emulation to activate. Otherwise, the first button event is posted as normal. Default: off. Property: &quot;Evdev Third Button Emulation&quot;.</p>
<dt><code>Option &#34;EmulateThirdButtonTimeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies the timeout in milliseconds between the initial button press and the generation of the emulated button event. Default: 1000. Property: &quot;Evdev Third Button Emulation Timeout&quot;.</p>
<dt><code>Option &#34;EmulateThirdButtonButton&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies the physical button number to be emitted if third button emulation is triggered. Default: 3. Property: &quot;Evdev Third Button Button&quot;.</p>
<dt><code>Option &#34;EmulateThirdButtonMoveThreshold&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies the maximum move fuzz in device coordinates for third button emulation. If the device moves by more than this threshold before the third button emulation is triggered, the emulation is cancelled and a first button event is generated as normal. Default: 20. Property: &quot;Evdev Third Button Emulation Threshold&quot;.</p>
<dt><code>Option &#34;GrabDevice&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Force a grab on the event device. Doing so will ensure that no other driver can initialise the same device and it will also stop the device from sending events to /dev/kbd or /dev/input/mice. Events from this device will not be sent to virtual devices (e.g. rfkill or the Macintosh mouse button emulation). Default: disabled.</p>
<dt><code>Option &#34;InvertX&#34; &#34;</code><i>Bool</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;InvertY&#34; &#34;</code><i>Bool</i><code>&#34;</code></p>
<dd>Invert the given axis. Default: off. Property: &quot;Evdev Axis Inversion&quot;.</p>
<dt><code>Option &#34;IgnoreRelativeAxes&#34; &#34;</code><i>Bool</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;IgnoreAbsoluteAxes&#34; &#34;</code><i>Bool</i><code>&#34;</code></p>
<dd>Ignore the specified type of axis. Default: unset. The X server cannot deal with devices that have both relative and absolute axes. Evdev tries to guess wich axes to ignore given the device type and disables absolute axes for mice and relative axes for tablets, touchscreens and touchpad. These options allow to forcibly disable an axis type. Mouse wheel axes are exempt and will work even if relative axes are ignored. No property, this configuration must be set in the configuration.<br />
 If either option is set to False, the driver will not ignore the specified axes regardless of the presence of other axes. This may trigger buggy behavior and events from this axis are always forwarded. Users are discouraged from setting this option.</p>
<dt><code>Option &#34;Calibration&#34; &#34;</code><i>min-x max-x min-y max-y</i><code>&#34;</code></p>
<dd>Calibrates the X and Y axes for devices that need to scale to a different coordinate system than reported to the X server. This feature is required for devices that need to scale to a different coordinate system than originally reported by the kernel (e.g. touchscreens). The scaling to the custom coordinate system is done in-driver and the X server is unaware of the transformation. Property: &quot;Evdev Axis Calibration&quot;.</p>
<dt><code>Option &#34;Mode&#34; &#34;Relative&#34;</code>|&#34;Absolute&#34;</p>
<dd>Sets the mode of the device if device has absolute axes. The default value for touchpads is relative, for other absolute. This option has no effect on devices without absolute axes.</p>
<dt><code>Option &#34;SwapAxes&#34; &#34;</code><i>Bool</i><code>&#34;</code></p>
<dd>Swap x/y axes. Default: off. Property: &quot;Evdev Axes Swap&quot;.</p>
<dt><code>Option &#34;XAxisMapping&#34; &#34;</code><i>N1 N2</i><code>&#34;</code></p>
<dd>Specifies which buttons are mapped to motion in the X direction in wheel emulation mode. Button number <i>N1</i> is mapped to the negative X axis motion and button number <i>N2</i> is mapped to the positive X axis motion. Default: no mapping. Property: &quot;Evdev Wheel Emulation Axes&quot;.</p>
<dt><code>Option &#34;YAxisMapping&#34; &#34;</code><i>N1 N2</i><code>&#34;</code></p>
<dd>Specifies which buttons are mapped to motion in the Y direction in wheel emulation mode. Button number <i>N1</i> is mapped to the negative Y axis motion and button number <i>N2</i> is mapped to the positive Y axis motion. Default: &quot;4 5&quot;. Property: &quot;Evdev Wheel Emulation Axes&quot;.</p>
<dt><code>Option &#34;TypeName&#34; &#34;type&#34;</code></p>
<dd>Specify the X Input 1.x type (see <a href="/docs/linux/man/3-xlistinputdevices/">XListInputDevices</a>(3)). There is rarely a need to use this option, evdev will guess the device type based on the device&#8217;s capabilities. This option is provided for devices that need quirks.</p>
<dt><code>Option &#34;VertScrollDelta&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The amount of motion considered one unit of scrolling vertically. Default: &quot;1&quot;. Property: &quot;Evdev Scrolling Distance&quot;.</p>
<dt><code>Option &#34;HorizScrollDelta&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The amount of motion considered one unit of scrolling horizontally. Default: &quot;1&quot;. Property: &quot;Evdev Scrolling Distance&quot;.</p>
<dt><code>Option &#34;DialDelta&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The amount of motion considered one unit of turning the dial. Default: &quot;1&quot;. Property: &quot;Evdev Scrolling Distance&quot;.</p>
<dt><code>Option &#34;Resolution&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Sets the resolution of the device in dots per inch. The resolution is used to scale relative motion events from mouse devices to 1000 DPI resolution. This can be used to make high resolution mice less sensitive without turning off acceleration. If set to 0 no scaling will be performed. Default: &quot;0&quot;. </p>
</dl>
<h2>Supported Properties</h2>
<p>The following properties are provided by the <code>evdev</code> driver.</p>
<dl>
<dt><code>Evdev Axis Calibration</code></p>
<dd>4 32-bit values, order min-x, max-x, min-y, max-y or 0 values to disable in-driver axis calibration.</p>
<dt><code>Evdev Axis Inversion</code></p>
<dd>2 boolean values (8 bit, 0 or 1), order X, Y. 1 inverts the axis.</p>
<dt><code>Evdev Axes Swap</code></p>
<dd>1 boolean value (8 bit, 0 or 1). 1 swaps x/y axes.</p>
<dt><code>Evdev Drag Lock Buttons</code></p>
<dd>8-bit. Either 1 value or pairs of values. Value range 0-32, 0 disables a value.</p>
<dt><code>Evdev Middle Button Emulation</code></p>
<dd>1 boolean value (8 bit, 0 or 1).</p>
<dt><code>Evdev Middle Button Timeout</code></p>
<dd>1 16-bit positive value.</p>
<dt><code>Evdev Middle Button Button</code></p>
<dd>1 8-bit value, allowed range 0-32, 0 disables the button.</p>
<dt><code>Evdev Wheel Emulation</code></p>
<dd>1 boolean value (8 bit, 0 or 1).</p>
<dt><code>Evdev Wheel Emulation Axes</code></p>
<dd>4 8-bit values, order X up, X down, Y up, Y down. 0 disables a value.</p>
<dt><code>Evdev Wheel Emulation Button</code></p>
<dd>1 8-bit value, allowed range 0-32, 0 disables the button.</p>
<dt><code>Evdev Wheel Emulation Inertia</code></p>
<dd>1 16-bit positive value.</p>
<dt><code>Evdev Wheel Emulation Timeout</code></p>
<dd>1 16-bit positive value.</p>
<dt><code>Evdev Scrolling Distance</code></p>
<dd>3 32-bit values: vertical, horizontal and dial. </p>
</dl>
<h2>Authors</h2>
<p>Kristian Høgsberg, Peter Hutterer</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7) </p>
