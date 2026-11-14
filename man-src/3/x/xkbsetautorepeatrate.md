---
title: "xkbsetautorepeatrate(3)"
name: "xkbsetautorepeatrate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetautorepeatrate/"
description: "XkbSetAutoRepeatRate – Sets the attributes of the RepeatKeys control for a keyboard device"
---

<p>XkbSetAutoRepeatRate &#8211; Sets the attributes of the RepeatKeys control for a keyboard device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetAutoRepeatRate</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>timeout</i><code>,</code> <code>unsigned int </code><i>interval</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device to configure, or XkbUseCoreKbd</p>
<dt><i>&#8211; timeout</i></p>
<dd>initial delay, ms</p>
<dt><i>&#8211; interval</i></p>
<dd>delay between repeats, ms</dl>
<h2>Description</h2>
<p>The core protocol allows only control over whether or not the entire keyboard or individual keys should auto-repeat when held down. RepeatKeys is a boolean control that extends this capability by adding control over the delay until a key begins to repeat and the rate at which it repeats. RepeatKeys is coupled with the core auto-repeat control: when RepeatKeys is enabled or disabled, the core auto-repeat is enabled or disabled and vice versa. </p>
<p> Auto-repeating keys are controlled by two attributes. The first, <i>timeout, </i> is the delay after the initial press of an auto-repeating key and the first generated repeat event. The second, <i>interval, </i> is the delay between all subsequent generated repeat events. As with all boolean controls, configuring the attributes that determine how the control operates does not automatically enable the control as a whole. </p>
<p> <i>XkbSetAutoRepeatRate </i> sends a request to the X server to configure the AutoRepeat control attributes to the values specified in <i>timeout </i> and <i>interval.</i><br />
&nbsp; <i>XkbSetAutoRepeatRate </i> does not wait for a reply; it normally returns True. Specifying a zero value for either <i>timeout </i> or <i>interval </i> causes the server to generate a BadValue protocol error. If a compatible version of the Xkb extension is not available in the server, <i>XkbSetAutoRepeatRate </i> returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetAutoRepeatRate </i> function returns True normally.</p>
<dt>False</p>
<dd>The <i>XkbSetAutoRepeatRate </i> function returns False if a compatible version of the Xkb extension is not available in the server.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
