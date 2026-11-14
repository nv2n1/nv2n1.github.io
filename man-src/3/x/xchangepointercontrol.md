---
title: "xchangepointercontrol(3)"
name: "xchangepointercontrol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xchangepointercontrol/"
description: "XChangePointerControl, XGetPointerControl – control pointer"
---

<p>XChangePointerControl, XGetPointerControl &#8211; control pointer </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XChangePointerControl(Display *<i>display</i>, Bool <i>do_accel</i>, Bool <i>do_threshold</i>, int <i>accel_numerator</i>, int <i>accel_denominator</i>, int <i>threshold</i>);</p>
<dd>int XGetPointerControl(Display *<i>display</i>, int *<i>accel_numerator_return</i>, int *<i>accel_denominator_return</i>, int *<i>threshold_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>accel_denominator</i></p>
<dd>Specifies the denominator for the acceleration multiplier.</p>
<dt><i>accel_denominator_return</i></p>
<dd>Returns the denominator for the acceleration multiplier.</p>
<dt><i>accel_numerator</i></p>
<dd>Specifies the numerator for the acceleration multiplier.</p>
<dt><i>accel_numerator_return</i></p>
<dd>Returns the numerator for the acceleration multiplier.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>do_accel</i></p>
<dd>Specifies a Boolean value that controls whether the values for the accel_numerator or accel_denominator are used.</p>
<dt><i>do_threshold</i></p>
<dd>Specifies a Boolean value that controls whether the value for the threshold is used.</p>
<dt><i>threshold</i></p>
<dd>Specifies the acceleration threshold.</p>
<dt><i>threshold_return</i></p>
<dd>Returns the acceleration threshold.</dl>
<h2>Description</h2>
<p>The <code>XChangePointerControl</code> function defines how the pointing device moves. The acceleration, expressed as a fraction, is a multiplier for movement. For example, specifying 3/1 means the pointer moves three times as fast as normal. The fraction may be rounded arbitrarily by the X server. Acceleration only takes effect if the pointer moves more than threshold pixels at once and only applies to the amount beyond the value in the threshold argument. Setting a value to -1 restores the default. The values of the do_accel and do_threshold arguments must be <code>True</code> for the pointer values to be set, or the parameters are unchanged. Negative values (other than -1) generate a <code>BadValue</code> error, as does a zero value for the accel_denominator argument. </p>
<p> <code>XChangePointerControl</code> can generate a <code>BadValue</code> error. </p>
<p> The <code>XGetPointerControl</code> function returns the pointer&#8217;s current acceleration multiplier and acceleration threshold.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
