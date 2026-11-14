---
title: "xkbgetautorepeatrate(3)"
name: "xkbgetautorepeatrate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetautorepeatrate/"
description: "XkbGetAutoRepeatRate – Gets the current attributes of the RepeatKeys control for a keyboard device"
---

<p>XkbGetAutoRepeatRate &#8211; Gets the current attributes of the RepeatKeys control for a keyboard device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbGetAutoRepeatRate</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int *</code><i>timeout_rtrn</i><code>,</code> <code>unsigned int *</code><i>interval_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>desired device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; timeout_rtrn</i></p>
<dd>backfilled with initial repeat delay, ms</p>
<dt><i>&#8211; interval_rtrn</i></p>
<dd>backfilled with subsequent repeat delay, ms</dl>
<h2>Description</h2>
<p>The core protocol allows only control over whether or not the entire keyboard or individual keys should auto-repeat when held down. RepeatKeys is a boolean control that extends this capability by adding control over the delay until a key begins to repeat and the rate at which it repeats. RepeatKeys is coupled with the core auto-repeat control: when RepeatKeys is enabled or disabled, the core auto-repeat is enabled or disabled and vice versa. </p>
<p> Auto-repeating keys are controlled by two attributes. The first, <i>timeout, </i> is the delay after the initial press of an auto-repeating key and the first generated repeat event. The second, <i>interval, </i> is the delay between all subsequent generated repeat events. As with all boolean controls, configuring the attributes that determine how the control operates does not automatically enable the control as a whole. </p>
<p> <i>XkbGetAutoRepeatRate </i> queries the server for the current values of the RepeatControls control attributes, backfills <i>timeout_rtrn </i> and <i>interval_rtrn </i> with them, and returns True. If a compatible version of the Xkb extension is not available in the server <i>XkbGetAutoRepeatRate </i> returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The XkbGetAutoRepeatRate function returns True if a compatible version of the Xkb extension is available in the server.</p>
<dt>False</p>
<dd>The XkbGetAutoRepeatRate function returns False if a compatible version of the Xkb extension is not available in the server. </p>
</dl>
