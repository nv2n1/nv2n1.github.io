---
title: "synaptics(4)"
name: "synaptics"
section: "4"
letter: "s"
url: "/docs/linux/man/4-synaptics/"
description: "synaptics – touchpad input driver"
---

<p>synaptics &#8211; touchpad input driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>devname</i><code>&#34;</code>
<code> Driver &#34;synaptics&#34;</code>
<code> Option &#34;Device&#34; &#34;</code><i>devpath</i><code>&#34;</code>
<code> Option &#34;Path&#34; &#34;</code><i>path</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>synaptics</code> is an Xorg input driver for touchpads. Even though touchpads can be handled by the normal evdev or mouse drivers, this driver allows more advanced features of the touchpad to become available. Some benefits would be:</p>
<dl>
<dt>&bull;</p>
<dd>Movement with adjustable, non-linear acceleration and speed.</p>
<dt>&bull;</p>
<dd>Button events through short touching of the touchpad.</p>
<dt>&bull;</p>
<dd>Double-Button events through double short touching of the touchpad.</p>
<dt>&bull;</p>
<dd>Dragging through short touching and holding down the finger on the touchpad (tap-and-drag gesture).</p>
<dt>&bull;</p>
<dd>Middle and right button events on the upper and lower corner of the touchpad.</p>
<dt>&bull;</p>
<dd>Vertical scrolling (button four and five events) through moving the finger on the right side of the touchpad.</p>
<dt>&bull;</p>
<dd>The up/down button sends button four/five events.</p>
<dt>&bull;</p>
<dd>Horizontal scrolling (button six and seven events) through moving the finger on the lower side of the touchpad.</p>
<dt>&bull;</p>
<dd>The multi-buttons send button four/five events for vertical scrolling and button six/seven events for horizontal scrolling.</p>
<dt>&bull;</p>
<dd>Adjustable finger detection.</p>
<dt>&bull;</p>
<dd>Multifinger taps: two finger for right button and three finger for middle button events. (Needs hardware support. Not all models implement this feature.)</p>
<dt>&bull;</p>
<dd>Pressure-dependent motion speed.</dl>
<p> Note that depending on the touchpad firmware, some of these features might be available even without using the synaptics driver. Note also that some functions are not available on all touchpad models, because they need support from the touchpad hardware/firmware. (Multifinger taps for example.) The name &quot;synaptics&quot; is historical and the driver still provides the synaptics protocol parsing code. Under Linux however, the hardware-specifics are handled by the kernel and this driver will work for any touchpad that has a working kernel driver. If your device is recognized as &#34;PS/2 Mouse&#34; or similar, the kernel driver does not support your device and this driver will only provide limited functionality. </p>
<h2>Configuration Options</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;Device&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>This option specifies the device file in your &#34;/dev&#34; directory which will be used to access the physical device. Normally you should use something like &#34;/dev/input/eventX&#34;, where X is some integer.</p>
<dt><code>Option &#34;Protocol&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specifies which kernel driver will be used by this driver. This is the list of supported drivers and their default use scenarios. </p>
<table>
<tr VALIGN=top>
<td>auto-dev</td>
<td>automatic, default (recommend)
</td>
</tr>
<tr VALIGN=top>
<td>event</td>
<td>Linux 2.6 kernel events
</td>
</tr>
<tr VALIGN=top>
<td>psaux</td>
<td>raw device access (Linux 2.4)
</td>
</tr>
<tr VALIGN=top>
<td>psm</td>
<td>FreeBSD psm driver
</td>
</tr>
</table>
<dt><code>Option &#34;LeftEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>X coordinate for left edge. Property: &quot;Synaptics Edges&quot;</p>
<dt><code>Option &#34;RightEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>X coordinate for right edge. Property: &quot;Synaptics Edges&quot;</p>
<dt><code>Option &#34;TopEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Y coordinate for top edge. Property: &quot;Synaptics Edges&quot;</p>
<dt><code>Option &#34;BottomEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Y coordinate for bottom edge. Property: &quot;Synaptics Edges&quot;</p>
<dt><code>Option &#34;FingerLow&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>When finger pressure drops below this value, the driver counts it as a release. Property: &quot;Synaptics Finger&quot;</p>
<dt><code>Option &#34;FingerHigh&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>When finger pressure goes above this value, the driver counts it as a touch. Property: &quot;Synaptics Finger&quot;</p>
<dt><code>Option &#34;MaxTapTime&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Maximum time (in milliseconds) for detecting a tap. Property: &quot;Synaptics Tap Durations&quot;</p>
<dt><code>Option &#34;MaxTapMove&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Maximum movement of the finger for detecting a tap. Property: &quot;Synaptics Tap Move&quot;</p>
<dt><code>Option &#34;MaxDoubleTapTime&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Maximum time (in milliseconds) for detecting a double tap. Property: &quot;Synaptics Tap Durations&quot;</p>
<dt><code>Option &#34;ClickTime&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The duration of the mouse click generated by tapping. Property: &quot;Synaptics Tap Durations&quot;</p>
<dt><code>Option &#34;ClickPad&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Whether the device is a click pad. See <code>ClickPad support</code> for more details. Property: &quot;Synaptics ClickPad&quot;</p>
<dt><code>Option &#34;VertEdgeScroll&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable vertical scrolling when dragging along the right edge. Property: &quot;Synaptics Edge Scrolling&quot;</p>
<dt><code>Option &#34;HorizEdgeScroll&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable horizontal scrolling when dragging along the bottom edge. Property: &quot;Synaptics Edge Scrolling&quot;</p>
<dt><code>Option &#34;CornerCoasting&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable edge scrolling to continue while the finger stays in an edge corner. Property: &quot;Synaptics Edge Scrolling&quot;</p>
<dt><code>Option &#34;VertTwoFingerScroll&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable vertical scrolling when dragging with two fingers anywhere on the touchpad. Property: &quot;Synaptics Two-Finger Scrolling&quot;</p>
<dt><code>Option &#34;HorizTwoFingerScroll&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable horizontal scrolling when dragging with two fingers anywhere on the touchpad. Property: &quot;Synaptics Two-Finger Scrolling&quot;</p>
<dt><code>Option &#34;VertScrollDelta&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Move distance of the finger for a scroll event. Property: &quot;Synaptics Scrolling Distance&quot;</p>
<dt><code>Option &#34;HorizScrollDelta&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Move distance of the finger for a scroll event. Property: &quot;Synaptics Scrolling Distance&quot;</p>
<dt><code>Option &#34;MinSpeed&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Minimum speed factor. Property: &quot;Synaptics Move Speed&quot;</p>
<dt><code>Option &#34;MaxSpeed&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Maximum speed factor. Property: &quot;Synaptics Move Speed&quot;</p>
<dt><code>Option &#34;AccelFactor&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Acceleration factor for normal pointer movements. Property: &quot;Synaptics Move Speed&quot;</p>
<dt><code>Option &#34;PressureMotionMinZ&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Finger pressure at which minimum pressure motion factor is applied. Property: &quot;Synaptics Pressure Motion&quot;</p>
<dt><code>Option &#34;PressureMotionMaxZ&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Finger pressure at which maximum pressure motion factor is applied. Property: &quot;Synaptics Pressure Motion&quot;</p>
<dt><code>Option &#34;PressureMotionMinFactor&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Lowest setting for pressure motion factor. Property: &quot;Synaptics Pressure Motion Factor&quot;</p>
<dt><code>Option &#34;PressureMotionMaxFactor&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Greatest setting for pressure motion factor. Property: &quot;Synaptics Pressure Motion Factor&quot;</p>
<dt><code>Option &#34;HorizHysteresis&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The minimum horizontal HW distance required to generate motion events. Can be specified as a percentage. Increase if noise motion is a problem for you. Zero is disabled. Default: 0.5 percent of the diagonal or (in case of evdev) the appropriate &quot;fuzz&quot; as advertised by the device.</p>
<dt><code>Option &#34;VertHysteresis&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The minimum vertical HW distance required to generate motion events. See <code>HorizHysteresis</code>.</p>
<dt><code>Option &#34;UpDownScrolling&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If on, the up/down buttons generate button 4/5 events. If off, the up button generates a double click and the down button generates a button 2 event. This option is only available for touchpads with physical scroll buttons. Property: &quot;Synaptics Button Scrolling&quot;</p>
<dt><code>Option &#34;LeftRightScrolling&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If on, the left/right buttons generate button 6/7 events. If off, the left/right buttons both generate button 2 events. This option is only available for touchpads with physical scroll buttons. Property: &quot;Synaptics Button Scrolling&quot;</p>
<dt><code>Option &#34;UpDownScrollRepeat&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If on, and the up/down buttons are used for scrolling (<code>UpDownScrolling</code>), these buttons will send auto-repeating 4/5 events, with the delay between repeats determined by <code>ScrollButtonRepeat</code>. This option is only available for touchpads with physical scroll buttons. Property: &quot;Synaptics Button Scrolling Repeat&quot;</p>
<dt><code>Option &#34;LeftRightScrollRepeat&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If on, and the left/right buttons are used for scrolling (<code>LeftRightScrolling</code>), these buttons will send auto-repeating 6/7 events, with the delay between repeats determined by <code>ScrollButtonRepeat</code>. This option is only available for touchpads with physical scroll buttons. Property: &quot;Synaptics Button Scrolling Repeat&quot;</p>
<dt><code>Option &#34;ScrollButtonRepeat&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>The number of milliseconds between repeats of button events 4-7 from the up/down/left/right scroll buttons. This option is only available for touchpads with physical scroll buttons. Property: &quot;Synaptics Button Scrolling Time&quot;</p>
<dt><code>Option &#34;EmulateMidButtonTime&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Maximum time (in milliseconds) for middle button emulation. Property: &quot;Synaptics Middle Button Timeout&quot;</p>
<dt><code>Option &#34;EmulateTwoFingerMinZ&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>For touchpads not capable of detecting multiple fingers but are capable of detecting finger pressure and width, this sets the Z pressure threshold. When both Z pressure and W width thresholds are crossed, a two finger press will be emulated. This defaults to a value that disables emulation on touchpads with real two-finger detection and defaults to a value that enables emulation on remaining touchpads that support pressure and width support. Property: &quot;Synaptics Two-Finger Pressure&quot;</p>
<dt><code>Option &#34;EmulateTwoFingerMinW&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>For touchpads not capable of detecting multiple fingers but are capable of detecting finger width and pressure, this sets the W width threshold. When both W width and Z pressure thresholds are crossed, a two finger press will be emulated. This feature works best with (<code>PalmDetect</code>) off. Property: &quot;Synaptics Two-Finger Width&quot;</p>
<dt><code>Option &#34;TouchpadOff&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Switch off the touchpad. Valid values are: </p>
<table>
<tr VALIGN=top>
<td>0</td>
<td>Touchpad is enabled
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Touchpad is switched off (physical clicks still work)
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Only tapping and scrolling is switched off
</td>
</tr>
</table>
<p> When the touchpad is switched off, button events caused by a physical button press are still interpreted. On a ClickPad, this includes software-emulated middle and right buttons as defined by the SoftButtonAreas setting.</p>
<dt>Property: &quot;Synaptics Off&quot;</p>
<dd>
<dt><code>Option &#34;LockedDrags&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If off, a tap-and-drag gesture ends when you release the finger. If on, the gesture is active until you tap a second time, or until LockedDragTimeout expires. Property: &quot;Synaptics Locked Drags&quot;</p>
<dt><code>Option &#34;LockedDragTimeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>This parameter specifies how long it takes (in milliseconds) for the LockedDrags mode to be automatically turned off after the finger is released from the touchpad. Property: &quot;Synaptics Locked Drags Timeout&quot;</p>
<dt><code>Option &#34;RTCornerButton&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported on a right top corner tap. Set to 0 to disable. Property: &quot;Synaptics Tap Action&quot;</p>
<dt><code>Option &#34;RBCornerButton&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported on a right bottom corner tap. Set to 0 to disable. Property: &quot;Synaptics Tap Action&quot;</p>
<dt><code>Option &#34;LTCornerButton&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported on a left top corner tap. Set to 0 to disable. Property: &quot;Synaptics Tap Action&quot;</p>
<dt><code>Option &#34;LBCornerButton&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported on a left bottom corner tap. Set to 0 to disable. Property: &quot;Synaptics Tap Action&quot;</p>
<dt><code>Option &#34;TapButton1&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported on a non-corner one-finger tap. Set to 0 to disable. Property: &quot;Synaptics Tap Action&quot;</p>
<dt><code>Option &#34;TapButton2&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported on a non-corner two-finger tap. Set to 0 to disable. Property: &quot;Synaptics Tap Action&quot;</p>
<dt><code>Option &#34;TapButton3&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported on a non-corner three-finger tap. Set to 0 to disable. Property: &quot;Synaptics Tap Action&quot;</p>
<dt><code>Option &#34;ClickFinger1&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported when left-clicking with one finger. Set to 0 to disable. Property: &quot;Synaptics Click Action&quot;</p>
<dt><code>Option &#34;ClickFinger2&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported when left-clicking with two fingers. Set to 0 to disable. Property: &quot;Synaptics Click Action&quot;</p>
<dt><code>Option &#34;ClickFinger3&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Which mouse button is reported when left-clicking with three fingers. Set to 0 to disable. Property: &quot;Synaptics Click Action&quot;</p>
<dt><code>Option &#34;CircularScrolling&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If on, circular scrolling is used. Property: &quot;Synaptics Circular Scrolling&quot;</p>
<dt><code>Option &#34;CircScrollDelta&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Move angle (radians) of finger to generate a scroll event. Property: &quot;Synaptics Circular Scrolling Distance&quot;</p>
<dt><code>Option &#34;CircScrollTrigger&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Trigger region on the touchpad to start circular scrolling </p>
<table>
<tr VALIGN=top>
<td>0</td>
<td>All Edges
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Top Edge
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Top Right Corner
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>Right Edge
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>Bottom Right Corner
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>Bottom Edge
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>Bottom Left Corner
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>Left Edge
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>Top Left Corner
</td>
</tr>
</table>
<p> Property: &quot;Synaptics Circular Scrolling Trigger&quot;</p>
<dt><code>Option &#34;CircularPad&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Instead of being a rectangle, the edge is the ellipse enclosed by the Left/Right/Top/BottomEdge parameters. For circular touchpads. Property: &quot;Synaptics Circular Pad&quot;</p>
<dt><code>Option &#34;PalmDetect&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If palm detection should be enabled. Note that this also requires hardware/firmware support from the touchpad. Property: &quot;Synaptics Palm Detection&quot;</p>
<dt><code>Option &#34;PalmMinWidth&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Minimum finger width at which touch is considered a palm. Property: &quot;Synaptics Palm Dimensions&quot;</p>
<dt><code>Option &#34;PalmMinZ&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Minimum finger pressure at which touch is considered a palm. Property: &quot;Synaptics Palm Dimensions&quot;</p>
<dt><code>Option &#34;CoastingSpeed&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Your finger needs to produce this many scrolls per second in order to start coasting. The default is 20 which should prevent you from starting coasting unintentionally. 0 disables coasting. Property: &quot;Synaptics Coasting Speed&quot;</p>
<dt><code>Option &#34;CoastingFriction&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Number of scrolls/second² to decrease the coasting speed. Default is 50. Property: &quot;Synaptics Coasting Speed&quot;</p>
<dt><code>Option &#34;SingleTapTimeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Timeout after a tap to recognize it as a single tap. Property: &quot;Synaptics Tap Durations&quot;</p>
<dt><code>Option &#34;GrabEventDevice&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If GrabEventDevice is true, the driver will grab the event device for exclusive use when using the linux 2.6 event protocol. When using other protocols, this option has no effect. Grabbing the event device means that no other user space or kernel space program sees the touchpad events. This is desirable if the X config file includes /dev/input/mice as an input device, but is undesirable if you want to monitor the device from user space. When changing this parameter with the synclient program, the change will not take effect until the synaptics driver is disabled and reenabled. This can be achieved by switching to a text console and then switching back to X.</p>
<dt><code>Option &#34;TapAndDragGesture&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Switch on/off the tap-and-drag gesture. This gesture is an alternative way of dragging. It is performed by tapping (touching and releasing the finger), then touching again and moving the finger on the touchpad. The gesture is enabled by default and can be disabled by setting the TapAndDragGesture option to false. Property: &quot;Synaptics Gestures&quot;</p>
<dt><code>Option &#174;esolutionDetect&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Allow or prevent the synaptics driver from reporting the size of the touchpad to the X server. The X server normally uses this information to scale movements so that touchpad movement corresponds visually to mouse cursor movements on the screen. However, in some rare cases where the touchpad height/width ratio is significantly different from the laptop, it can cause the mouse cursor to skip pixels in the X or Y axis. This option allows disabling this scaling behavior, which can provide smoother mouse movement in such cases. Property: &quot;Synaptics Resolution Detect&quot;</p>
<dt><code>Option &#34;VertResolution&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Resolution of X coordinates in units/millimeter. The value is used together with HorizResolution to compensate unequal vertical and horizontal sensitivity. Setting VertResolution and HorizResolution equal values means no compensation. Default value is read from the touchpad or set to 1 if value could not be read. Property: &quot;Synaptics Pad Resolution&quot;</p>
<dt><code>Option &#34;HorizResolution&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Resolution of Y coordinates in units/millimeter. The value is used together with VertResolution to compensate unequal vertical and horizontal sensitivity. Setting VertResolution and HorizResolution equal values means no compensation. Default value is read from the touchpad or set to 1 if value could not be read. Property: &quot;Synaptics Pad Resolution&quot;</p>
<dt><code>Option &#34;AreaLeftEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Ignore movements, scrolling and tapping which start left of this edge. The option is disabled by default and can be enabled by setting the AreaLeftEdge option to any integer value other than zero. If supported by the server (version 1.9 and later), the edge may be specified in percent of the total width of the touchpad. Property: &quot;Synaptics Area&quot;</p>
<dt><code>Option &#34;AreaRightEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Ignore movements, scrolling and tapping which start right of this edge. The option is disabled by default and can be enabled by setting the AreaRightEdge option to any integer value other than zero. If supported by the server (version 1.9 and later), the edge may be specified in percent of the total width of the touchpad. Property: &quot;Synaptics Area&quot;</p>
<dt><code>Option &#34;AreaTopEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Ignore movements, scrolling and tapping which start above this edge. The option is disabled by default and can be enabled by setting the AreaTopEdge option to any integer value other than zero. If supported by the server (version 1.9 and later), the edge may be specified in percent of the total height of the touchpad. Property: &quot;Synaptics Area&quot;</p>
<dt><code>Option &#34;AreaBottomEdge&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Ignore movements, scrolling and tapping which start below this edge. The option is disabled by default and can be enabled by setting the AreaBottomEdge option to any integer value other than zero. If supported by the server (version 1.9 and later), the edge may be specified in percent of the total height of the touchpad. Property: &quot;Synaptics Area&quot;</p>
<dt><code>Option &#34;SoftButtonAreas&#34; &#34;</code><i>RBL RBR RBT RBB MBL MBR MBT MBB</i><code>&#34;</code></p>
<dd>This option is only available on ClickPad devices. Enable soft button click area support on ClickPad devices. The first four parameters are the left, right, top, bottom edge of the right button, respectively, the second four parameters are the left, right, top, bottom edge of the middle button, respectively. Any of the values may be given as percentage of the touchpad width or height, whichever applies. If any edge is set to 0 (not 0%), the button is assumed to extend to infinity in the given direction. Setting all values to 0 (not 0%) disables soft button areas. Button areas may not overlap, however it is permitted for two buttons to share an edge value. Property: &quot;Synaptics Soft Button Areas&quot;</p>
<dt><code>Option &#34;HasSecondarySoftButtons&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option is only available on ClickPad devices. Enable the secondary software button area support. The exact area must be set in option &#34;SecondarySoftButtonAreas&#34;. See <code>ClickPad support</code> for more details.</p>
<dt><code>Option &#34;SecondarySoftButtonAreas&#34; &#34;</code><i>RBL RBR RBT RBB MBL MBR MBT MBB</i><code>&#34;</code></p>
<dd>This option is only available on ClickPad devices and only if <code>Option &#34;HasSecondarySoftButtons&#34;</code> is enabled. Define the secondary soft button click areas on ClickPad devices (usually on top of the device). For the allowed values for this option, see <code>Option &#34;SoftButtonAreas&#34;.</code> Primary and secondary soft button areas must not overlap each other. If they do, the behavior of the driver is undefined. Property: &quot;Synaptics Secondary Soft Button Areas&quot;. This property is only initialized if <code>Option &#34;HasSecondarySoftButtons&#34; </code> is enabled and this option is set in the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5). </p>
</dl>
<h2>Configuration Details</h2>
<h3>Area handling</h3>
<p>The LeftEdge, RightEdge, TopEdge and BottomEdge parameters are used to define the edge and corner areas of the touchpad. The parameters split the touchpad area in 9 pieces, like this: </p>
<table>
<tr VALIGN=top>
<td></td>
<td>LeftEdge</td>
<td COLSPAN=2>RightEdge</td>
<td></td>
</tr>
<tr VALIGN=top>
<td></td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1</td>
<td ALIGN=center>2</td>
<td ALIGN=center>3</td>
<td></td>
</tr>
<tr VALIGN=top>
<td></td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td></td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>5</td>
<td ALIGN=center>6</td>
<td></td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td></td>
</tr>
<tr VALIGN=top>
<td></td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>7</td>
<td ALIGN=center>8</td>
<td ALIGN=center>9</td>
<td></td>
</tr>
<tr VALIGN=top>
<td></td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>Physical left edge</td>
<td></td>
<td>Physical right edge</td>
<td></td>
</tr>
</table>
<p> Coordinates to the left of LeftEdge are part of the left edge (areas 1, 4 and 7), coordinates to the left of LeftEdge and above TopEdge (area 1) are part of the upper left corner, etc. </p>
<p> A good way to find appropriate edge parameters is to use <a href="/docs/linux/man/1-evtest/">evtest</a>(1) on the device to see the x/y coordinates corresponding to different positions on the touchpad. </p>
<p> The perceived physical edges may be adjusted with the AreaLeftEdge, AreaRightEdge, AreaTopEdge, and AreaBottomEdge options. If these values are set to something other than the physical edges, input that starts in the space between the area edge and the respective physical edge is ignored. Note that this reduces the available space on the touchpad to start motions in.</p>
<h3>Tapping</h3>
<p>A tap event happens when the finger is touched and released in a time interval shorter than MaxTapTime, and the touch and release coordinates are less than MaxTapMove units apart. A &quot;touch&quot; event happens when the Z value goes above FingerHigh, and an &quot;untouch&quot; event happens when the Z value goes below FingerLow. </p>
<p> The MaxDoubleTapTime parameter has the same function as the MaxTapTime parameter, but for the second, third, etc tap in a tap sequence. If you can&#8217;t perform double clicks fast enough (for example, xmms depends on fast double clicks), try reducing this parameter. If you can&#8217;t get word selection to work in xterm (ie button down, button up, button down, move mouse), try increasing this parameter. </p>
<p> The ClickTime parameter controls the delay between the button down and button up X events generated in response to a tap event. A too long value can cause undesirable autorepeat in scroll bars and a too small value means that visual feedback from the gui application you are interacting with is harder to see.</p>
<h3>Acceleration</h3>
<p>The MinSpeed, MaxSpeed and AccelFactor parameters control the pointer motion speed. The speed value defines the scaling between touchpad coordinates and screen coordinates. When moving the finger very slowly, the MinSpeed value is used, when moving very fast the MaxSpeed value is used. When moving the finger at moderate speed, you get a pointer motion speed somewhere between MinSpeed and MaxSpeed. If you don&#8217;t want any acceleration, set MinSpeed and MaxSpeed to the same value. </p>
<p> The MinSpeed, MaxSpeed and AccelFactor parameters don&#8217;t have any effect on scrolling speed. Scrolling speed is determined solely from the VertScrollDelta and HorizScrollDelta parameters. To invert the direction of vertical or horizontal scrolling, set VertScrollDelta or HorizScrollDelta to a negative value. </p>
<p> Acceleration is mostly handled outside the driver, thus the driver will translate MinSpeed into constant deceleration and adapt MaxSpeed at startup time. This ensures you can user the other acceleration profiles, albeit without pressure motion. However the numbers at runtime will likely be different from any options you may have set.</p>
<h3>Pressure motion</h3>
<p>When pressure motion is activated, the cursor motion speed depends on the pressure exerted on the touchpad (the more pressure exerted on the touchpad, the faster the pointer). More precisely the speed is first calculated according to MinSpeed, MaxSpeed and AccelFactor, and then is multiplied by a sensitivity factor. </p>
<p> The sensitivity factor can be adjusted using the PressureMotion parameters. If the pressure is below PressureMotionMinZ, PressureMotionMinFactor is used, and if the pressure is greater than PressureMotionMaxZ, PressureMotionMaxFactor is used. For a pressure value between PressureMotionMinZ and PressureMotionMaxZ, the factor is increased linearly.</p>
<h3>Middle button emulation</h3>
<p>Since most synaptics touchpad models don&#8217;t have a button that corresponds to the middle button on a mouse, the driver can emulate middle mouse button events. If you press both the left and right mouse buttons at almost the same time (no more than EmulateMidButtonTime milliseconds apart) the driver generates a middle mouse button event.</p>
<h3>Circular scrolling</h3>
<p>Circular scrolling acts like a scrolling wheel on the touchpad. Scrolling is engaged when a drag starts in the given CircScrollTrigger region, which can be all edges, a particular side, or a particular corner. Once scrolling is engaged, moving your finger in clockwise circles around the center of the touchpad will generate scroll down events and counter clockwise motion will generate scroll up events. Lifting your finger will disengage circular scrolling. Use tight circles near the center of the pad for fast scrolling and large circles for better control. When used together with vertical scrolling, hitting the upper or lower right corner will seamlessly switch over from vertical to circular scrolling.</p>
<h3>Coasting</h3>
<p>Coasting is enabled by setting the CoastingSpeed parameter to a non-zero value. Coasting comes in two flavors: conventional (finger off) coasting, and corner (finger on) coasting. </p>
<p> Conventional coasting is enabled when coasting is enabled, and CornerCoasting is set to false. When conventional coasting is enabled, horizontal/vertical scrolling can continue after the finger is released from the lower/right edge of the touchpad. The driver computes the scrolling speed corresponding to the finger speed immediately before the finger leaves the touchpad. If this scrolling speed is larger than the CoastingSpeed parameter (measured in scroll events per second), the scrolling will continue with the same speed in the same direction until the finger touches the touchpad again. </p>
<p> Corner coasting is enabled when coasting is enabled, and CornerCoasting is set to true. When corner coasting is enabled, edge scrolling can continue as long as the finger stays in a corner. Coasting begins when the finger enters the corner, and continues until the finger leaves the corner. CornerCoasting takes precedence over the seamless switch from edge scrolling to circular scrolling. That is, if CornerCoasting is active, scrolling will stop, and circular scrolling will not start, when the finger leaves the corner.</p>
<h3>Noise cancellation</h3>
<p>The synaptics has a built-in noise cancellation based on hysteresis. This means that incoming coordinates actually shift a box of predefined dimensions such that it covers the incoming coordinate, and only the boxes own center is used as input. Obviously, the smaller the box the better, but the likelyhood of noise motion coming through also increases.</p>
<h3>ClickPad support</h3>
<p>A click pad device has button(s) integrated into the touchpad surface. The user must press downward on the touchpad in order to generated a button press. ClickPad support is enabled if the option <code>ClickPad</code> is set or the property is set at runtime. On some platforms, this option will be set automatically if the kernel detects a matching device. On Linux, the device must have the INPUT_PROP_BUTTONPAD property set. </p>
<p> ClickPads do not support middle mouse button emulation. If enabling ClickPad support at runime, the user must also set the middle mouse button timeout to 0. If auto-detected, middle mouse button emulation is disabled by the driver. </p>
<p> ClickPads provide software emulated buttons through <code>Option &#34;SoftButtonAreas&#34;.</code> These buttons enable areas on the touchpad to perform as right or middle mouse button. When the user performs a click within a defined soft button area, a right or middle click is performed. </p>
<p> Some laptops, most notably the Lenovo T440, T540 and x240 series, provide a pointing stick without physical buttons. On those laptops, the top of the touchpad acts as software-emulated button area. This area can be enabled with <code>Option &#34;HasSecondarySoftButtons&#34;</code> and configured with <code>Option &#34;SecondarySoftButtonAreas&#34;.</code> On some platforms, this option will be set automatically if the kernel detects a matching device. On Linux, the device must have the INPUT_PROP_TOPBUTTONPAD property set.</p>
<h2>Device Properties</h2>
<p>Synaptics 1.0 and higher support input device properties if the driver is running on X server 1.6 or higher. The synclient tool shipped with synaptics version 1.1 uses input device properties by default. Properties supported:</p>
<dl>
<dt><code>Synaptics Edges</code></p>
<dd>32 bit, 4 values, left, right, top, bottom. </p>
<dt><code>Synaptics Finger</code></p>
<dd>32 bit, 3 values, low, high, press. </p>
<dt><code>Synaptics Tap Time</code></p>
<dd>32 bit. </p>
<dt><code>Synaptics Tap Move</code></p>
<dd>32 bit. </p>
<dt><code>Synaptics Tap Durations</code></p>
<dd>32 bit, 3 values, single touch timeout, max tapping time for double taps, duration of a single click. </p>
<dt><code>Synaptics ClickPad</code></p>
<dd>8 bit (Bool). </p>
<dt><code>Synaptics Middle Button Timeout</code></p>
<dd>32 bit. </p>
<dt><code>Synaptics Two-Finger Pressure</code></p>
<dd>32 bit. </p>
<dt><code>Synaptics Two-Finger Width</code></p>
<dd>32 bit. </p>
<dt><code>Synaptics Scrolling Distance</code></p>
<dd>32 bit, 2 values, vert, horiz. </p>
<dt><code>Synaptics Edge Scrolling</code></p>
<dd>8 bit (BOOL), 3 values, vertical, horizontal, corner. </p>
<dt><code>Synaptics Two-Finger Scrolling</code></p>
<dd>8 bit (BOOL), 2 values, vertical, horizontal. </p>
<dt><code>Synaptics Move Speed</code></p>
<dd>FLOAT, 4 values, min, max, accel, &lt;deprecated&gt; </p>
<dt><code>Synaptics Button Scrolling</code></p>
<dd>8 bit (BOOL), 2 values, updown, leftright. </p>
<dt><code>Synaptics Button Scrolling Repeat</code></p>
<dd>8 bit (BOOL), 2 values, updown, leftright. </p>
<dt><code>Synaptics Button Scrolling Time</code></p>
<dd>32 bit. </p>
<dt><code>Synaptics Off</code></p>
<dd>8 bit, valid values (0, 1, 2). </p>
<dt><code>Synaptics Locked Drags</code></p>
<dd>8 bit (BOOL). </p>
<dt><code>Synaptics Locked Drags Timeout</code></p>
<dd>32 bit. </p>
<dt><code>Synaptics Tap Action</code></p>
<dd>8 bit, up to MAX_TAP values (see synaptics.h), 0 disables an element. order: RT, RB, LT, LB, F1, F2, F3. </p>
<dt><code>Synaptics Click Action</code></p>
<dd>8 bit, up to MAX_CLICK values (see synaptics.h), 0 disables an element. order: Finger 1, 2, 3. </p>
<dt><code>Synaptics Circular Scrolling</code></p>
<dd>8 bit (BOOL). </p>
<dt><code>Synaptics Circular Scrolling Distance</code></p>
<dd>FLOAT. </p>
<dt><code>Synaptics Circular Scrolling Trigger</code></p>
<dd>8 bit, valid values 0..8 (inclusive) order: any edge, top, top + right, right, right + bottom, bottom, bottom + left, left, left + top. </p>
<dt><code>Synaptics Circular Pad</code></p>
<dd>8 bit (BOOL). </p>
<dt><code>Synaptics Palm Detection</code></p>
<dd>8 bit (BOOL). </p>
<dt><code>Synaptics Palm Dimensions</code></p>
<dd>32 bit, 2 values, width, z. </p>
<dt><code>Synaptics Coasting Speed</code></p>
<dd>FLOAT, 2 values, speed, friction. </p>
<dt><code>Synaptics Pressure Motion</code></p>
<dd>32 bit, 2 values, min, max. </p>
<dt><code>Synaptics Pressure Motion Factor</code></p>
<dd>FLOAT, 2 values, min, max. </p>
<dt><code>Synaptics Resolution Detect</code></p>
<dd>8 bit (BOOL). </p>
<dt><code>Synaptics Grab Event Device</code></p>
<dd>8 bit (BOOL). </p>
<dt><code>Synaptics Gestures</code></p>
<dd>8 bit (BOOL), 1 value, tap-and-drag. </p>
<dt><code>Synaptics Area</code></p>
<dd>The AreaLeftEdge, AreaRightEdge, AreaTopEdge and AreaBottomEdge parameters are used to define the edges of the active area of the touchpad. All movements, scrolling and tapping which take place outside of this area will be ignored. This property is disabled by default. </p>
<p> 32 bit, 4 values, left, right, top, bottom. 0 disables an element. </p>
<dt><code>Synaptics Soft Button Areas</code></p>
<dd>This property is only available on ClickPad devices. The Right and middle soft button areas are used to support right and middle click actions on a ClickPad device. Providing 0 for all values of a given button disables the button area. </p>
<p> 32 bit, 8 values, RBL, RBR, RBT, RBB, MBL, MBR, MBT, MBB. </p>
<dt><code>Synaptics Capabilities</code></p>
<dd>This read-only property expresses the physical capability of the touchpad, most notably whether the touchpad hardware supports multi-finger tapping and scrolling. </p>
<p> 8 bit (BOOL), 7 values (read-only), has left button, has middle button, has right button, two-finger detection, three-finger detection, pressure detection, and finger/palm width detection. </p>
<dt><code>Synaptics Pad Resolution</code></p>
<dd>32 bit unsigned, 2 values (read-only), vertical, horizontal in units/millimeter. </p>
</dl>
<h2>Notes</h2>
<p>Configuration through <i>InputClass</i> sections is recommended in X servers 1.8 and later. See <a href="/docs/linux/man/5-xorg-conf-d/">xorg.conf.d</a>(5) for more details. An example xorg.conf.d snippet is provided in <i>${sourcecode}/conf/70-synaptics.conf</i> Configuration through hal fdi files is recommended in X servers 1.5, 1.6 and 1.7. An example hal policy file is provided in <i>${sourcecode}/conf/11-x11-synaptics.fdi</i> If either of <code>Protocol &#34;</code><i>auto-dev</i><code>&#34;</code> (default) or <code>Protocol &#34;</code><i>event</i><code>&#34;</code> is used, the driver initializes defaults based on the capabilities reported by the kernel driver. Acceleration, edges and resolution are based on the dimensions reported by the kernel. If the kernel reports multi-finger detection, two-finger vertical scrolling is enabled, horizontal two-finger scrolling is disabled and edge scrolling is disabled. If no multi-finger capabilities are reported, edge scrolling is enabled for both horizontal and vertical scrolling. Tapping is disabled by default for touchpads with one or more physical buttons. To enable it you need to map tap actions to buttons. See the &quot;TapButton1&quot;, &quot;TapButton2&quot; and &quot;TapButton3&quot; options. Button mapping for physical buttons is handled in the server. If the device is switched to left-handed (an in-server mapping of physical buttons 1, 2, 3 to the logical buttons 3, 2, 1, respectively), both physical and TapButtons are affected. To counteract this, the TapButtons need to be set up in reverse order (TapButton1=3, TapButton2=1). </p>
<h2>Removed Options</h2>
<p>The following options are no longer part of the driver configuration:</p>
<dl>
<dt><code>Option &#34;Repeater&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;HistorySize&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;SpecialScrollAreaRight&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;GuestMouseOff&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;SHMConfig&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;FingerPress&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;TrackstickSpeed&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;EdgeMotionMinZ&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;EdgeMotionMaxZ&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;EdgeMotionMinSpeed&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;EdgeMotionMaxSpeed&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;EdgeMotionUseAlways&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>
<dd></dl>
<h2>Authors</h2>
<p>Peter Osterlund &lt;petero2 [at] telia.com&gt; and many others.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-synclient/">synclient</a>(1), <a href="/docs/linux/man/1-syndaemon/">syndaemon</a>(1) </p>
