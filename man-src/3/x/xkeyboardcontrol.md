---
title: "xkeyboardcontrol(3)"
name: "xkeyboardcontrol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkeyboardcontrol/"
description: "XChangeKeyboardControl, XGetKeyboardControl, XAutoRepeatOn, XAutoRepeatOff, XBell, XQueryKeymap, XKeyboardControl – manipulate keyboard settings and keyboard control structure"
---

<p>XChangeKeyboardControl, XGetKeyboardControl, XAutoRepeatOn, XAutoRepeatOff, XBell, XQueryKeymap, XKeyboardControl &#8211; manipulate keyboard settings and keyboard control structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XChangeKeyboardControl(Display *<i>display</i>, unsigned long <i>value_mask</i>, XKeyboardControl *<i>values</i>);</p>
<dd>int XGetKeyboardControl(Display *<i>display</i>, XKeyboardState *<i>values_return</i>);</p>
<dd>int XAutoRepeatOn(Display *<i>display</i>);</p>
<dd>int XAutoRepeatOff(Display *<i>display</i>);</p>
<dd>int XBell(Display *<i>display</i>, int <i>percent</i>);</p>
<dd>int XQueryKeymap(Display *<i>display</i>, char <i>keys_return</i>[32]);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>keys_return</i></p>
<dd>Returns an array of bytes that identifies which keys are pressed down. Each bit represents one key of the keyboard.</p>
<dt><i>percent</i></p>
<dd>Specifies the volume for the bell, which can range from -100 to 100 inclusive.</p>
<dt><i>value_mask</i></p>
<dd>Specifies which controls to change. This mask is the bitwise inclusive OR of the valid control mask bits.</p>
<dt><i>values</i></p>
<dd>Specifies one value for each bit set to 1 in the mask.</p>
<dt><i>values_return</i></p>
<dd>Returns the current keyboard controls in the specified <code>XKeyboardState</code> structure.</dl>
<h2>Description</h2>
<p>The <code>XChangeKeyboardControl</code> function controls the keyboard characteristics defined by the <code>XKeyboardControl</code> structure. The value_mask argument specifies which values are to be changed. </p>
<p> <code>XChangeKeyboardControl</code> can generate <code>BadMatch</code> and <code>BadValue</code> errors. </p>
<p> The <code>XGetKeyboardControl</code> function returns the current control values for the keyboard to the <code>XKeyboardState</code> structure. </p>
<p> The <code>XAutoRepeatOn</code> function turns on auto-repeat for the keyboard on the specified display. </p>
<p> The <code>XAutoRepeatOff</code> function turns off auto-repeat for the keyboard on the specified display. </p>
<p> The <code>XBell</code> function rings the bell on the keyboard on the specified display, if possible. The specified volume is relative to the base volume for the keyboard. If the value for the percent argument is not in the range -100 to 100 inclusive, a <code>BadValue</code> error results. The volume at which the bell rings when the percent argument is nonnegative is:</p>
<dl COMPACT>
<dd>base &#8211; [(base * percent) / 100] + percent</dl>
<p> The volume at which the bell rings when the percent argument is negative is:</p>
<dl COMPACT>
<dd>base + [(base * percent) / 100]</dl>
<p> To change the base volume of the bell, use <code>XChangeKeyboardControl</code>. </p>
<p> <code>XBell</code> can generate a <code>BadValue</code> error. </p>
<p> The <code>XQueryKeymap</code> function returns a bit vector for the logical state of the keyboard, where each bit set to 1 indicates that the corresponding key is currently pressed down. The vector is represented as 32 bytes. Byte N (from 0) contains the bits for keys 8N to 8N + 7 with the least significant bit in the byte representing key 8N. </p>
<p> Note that the logical state of a device (as seen by client applications) may lag the physical state if device event processing is frozen.</p>
<h2>Structures</h2>
<p>The <code>XKeyboardControl</code> structure contains: </p>
<p> /* Mask bits for ChangeKeyboardControl */ </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBKeyClickPercent</code> </td>
<td> (1L&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBBellPercent</code> </td>
<td> (1L&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBBellPitch</code> </td>
<td> (1L&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBBellDuration</code> </td>
<td> (1L&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBLed</code> </td>
<td> (1L&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBLedMode</code> </td>
<td> (1L&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBKey</code> </td>
<td> (1L&lt;&lt;6)
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>KBAutoRepeatMode</code> </td>
<td> (1L&lt;&lt;7)
</td>
</tr>
</table>
<p> /* Values */ </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int key_click_percent;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bell_percent;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bell_pitch;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bell_duration;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int led;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int led_mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;LedModeOn, LedModeOff&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int key;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int auto_repeat_mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;AutoRepeatModeOff, AutoRepeatModeOn,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;AutoRepeatModeDefault&nbsp;*/ } XKeyboardControl; </p>
<p> The key_click_percent member sets the volume for key clicks between 0 (off) and 100 (loud) inclusive, if possible. A setting of -1 restores the default. Other negative values generate a <code>BadValue</code> error. </p>
<p> The bell_percent sets the base volume for the bell between 0 (off) and 100 (loud) inclusive, if possible. A setting of -1 restores the default. Other negative values generate a <code>BadValue</code> error. The bell_pitch member sets the pitch (specified in Hz) of the bell, if possible. A setting of -1 restores the default. Other negative values generate a <code>BadValue</code> error. The bell_duration member sets the duration of the bell specified in milliseconds, if possible. A setting of -1 restores the default. Other negative values generate a <code>BadValue</code> error. </p>
<p> If both the led_mode and led members are specified, the state of that LED is changed, if possible. The led_mode member can be set to <code>LedModeOn</code> or <code>LedModeOff</code>. If only led_mode is specified, the state of all LEDs are changed, if possible. At most 32 LEDs numbered from one are supported. No standard interpretation of LEDs is defined. If led is specified without led_mode, a <code>BadMatch</code> error results. </p>
<p> If both the auto_repeat_mode and key members are specified, the auto_repeat_mode of that key is changed (according to <code>AutoRepeatModeOn</code>, <code>AutoRepeatModeOff</code>, or <code>AutoRepeatModeDefault</code>), if possible. If only auto_repeat_mode is specified, the global auto_repeat_mode for the entire keyboard is changed, if possible, and does not affect the per-key settings. If a key is specified without an auto_repeat_mode, a <code>BadMatch</code> error results. Each key has an individual mode of whether or not it should auto-repeat and a default setting for the mode. In addition, there is a global mode of whether auto-repeat should be enabled or not and a default setting for that mode. When global mode is <code>AutoRepeatModeOn</code>, keys should obey their individual auto-repeat modes. When global mode is <code>AutoRepeatModeOff</code>, no keys should auto-repeat. An auto-repeating key generates alternating <code>KeyPress</code> and <code>KeyRelease</code> events. When a key is used as a modifier, it is desirable for the key not to auto-repeat, regardless of its auto-repeat setting. </p>
<p> The <code>XKeyboardState</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int key_click_percent;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bell_percent;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int bell_pitch, bell_duration;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long led_mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int global_auto_repeat;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char auto_repeats[32]; } XKeyboardState; </p>
<p> For the LEDs, the least significant bit of led_mask corresponds to LED one, and each bit set to 1 in led_mask indicates an LED that is lit. The global_auto_repeat member can be set to <code>AutoRepeatModeOn</code> or <code>AutoRepeatModeOff</code>. The auto_repeats member is a bit vector. Each bit set to 1 indicates that auto-repeat is enabled for the corresponding key. The vector is represented as 32 bytes. Byte N (from 0) contains the bits for keys 8N to 8N + 7 with the least significant bit in the byte representing key 8N.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangekeyboardmapping/">XChangeKeyboardMapping</a>(3), <a href="/docs/linux/man/3-xkbchangeenabledcontrols/">XkbChangeEnabledControls</a>(3), <a href="/docs/linux/man/3-xkbbell/">XkbBell</a>(3), <a href="/docs/linux/man/3-xkbdevicebell/">XkbDeviceBell</a>(3), <a href="/docs/linux/man/3-xkbgetmap/">XkbGetMap</a>(3), <a href="/docs/linux/man/3-xsetpointermapping/">XSetPointerMapping</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
