---
title: "xkbsetnameddeviceindicator(3)"
name: "xkbsetnameddeviceindicator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetnameddeviceindicator/"
description: "XkbSetNamedIndicator – Names an indicator if it is not already named; toggles the state of the indicator; sets the indicator to a specified state and sets the indicator map for the indicator"
---

<p>XkbSetNamedIndicator &#8211; Names an indicator if it is not already named; toggles the state of the indicator; sets the indicator to a specified state and sets the indicator map for the indicator </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt>
</dt><dt> <code>Bool XkbSetNamedDeviceIndicator</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>led_class</i><code>,</code> <code>unsigned int </code><i>led_id</i><code>,</code> <code>Atom </code><i>name</i><code>,</code> <code>Bool </code><i>change_state</i><code>,</code> <code>Bool </code><i>state</i><code>,</code> <code>Bool </code><i>create_new</i><code>,</code> <code>XkbIndicatorMapPtr </code><i>map</i><code>);</code> <code>Bool XkbSetNamedIndicator</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>Atom </code><i>name</i><code>,</code> <code>Bool </code><i>change_state</i><code>,</code> <code>Bool </code><i>state</i><code>,</code> <code>Bool </code><i>create_new</i><code>,</code> <code>XkbIndicatorMapPtr </code><i>map</i><code>);</code><br/>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></dt>
<dd>
</dd><dd>connection to the X server</dd>
<dt><i>&#8211; device_spec</i></dt>
<dd>device ID, or XkbUseCoreKbd</dd>
<dt><i>&#8211; led_class</i></dt>
<dd>feedback class, or XkbDfltXIClass</dd>
<dt><i>&#8211; led_id</i></dt>
<dd>feedback ID, or XkbDfltXIId</dd>
<dt><i>&#8211; name</i></dt>
<dd>name of the indicator to change</dd>
<dt><i>&#8211; change_state</i></dt>
<dd>whether to change the indicator state or not</dd>
<dt><i>&#8211; state</i></dt>
<dd>desired new state for the indicator</dd>
<dt><i>&#8211; create_new</i></dt>
<dd>whether a new indicator with the specified name should be created when necessary</dd>
<dt><i>&#8211; map</i></dt>
<dd>new map for the indicator</dd></dl>
<h2>Description</h2>
<p>If a compatible version of the Xkb extension is not available in the server, <i>XkbSetNamedDeviceIndicator</i> returns False. Otherwise, it sends a request to the X server to change the indicator specified by <i>name </i> and returns True.<br/>
&nbsp; If <i>change_state </i> is True, <i>XkbSetNamedDeviceIndicator</i> tells the server to change the state of the named indicator to the value specified by <i>state</i>. If <i>change_state</i> is False, then <i>state</i> is not used. </p>
<p> If an indicator with the name specified by <i>name </i> does not already exist, the <i>create_new </i> parameter tells the server whether it should create a new named indicator. If <i>create_new </i> is True, the server finds the first indicator that doesn&#8217;t have a name and gives it the name specified by <i>name</i>. If the optional parameter, <i>map</i>, is not NULL, <i>XkbSetNamedDeviceIndicator</i> tells the server to change the indicator&#8217;s map to the values specified in <i>map</i>. </p>
<p> In addition, it can also generate XkbIndicatorStateNotify, XkbIndicatorMapNotify, and XkbNamesNotify events. </p>
<p> <i>XkbSetNamedIndicator</i> is a convenience function that calls <i>XkbSetNamedDeviceIndicator</i> with a <i>device_spec</i> of <code>XkbUseCoreKbd</code>, a <i>led_class</i> of <code>XkbDfltXIClass</code>, and a <i>led_id</i> of <code>XkbDfltXIId</code>. It returns the return value from <i>XkbSetNamedDeviceIndicator</i>.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</dt>
<dd>The <i>XkbSetNamedIndicator</i> and <i>XkbSetNamedDeviceIndicator</i> functions return True if a compatible version of the Xkb extension is available in the server.</dd>
<dt>False</dt>
<dd>The <i>XkbSetNamedIndicator</i> and <i>XkbSetNamedDeviceIndicator</i> functions return False if a compatible version of the Xkb extension is not available in the server.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAtom</code></dt>
<dd>A name is neither a valid Atom or None</dd>
<dt><code>BadImplementation</code></dt>
<dd>Invalid reply from server</dd>
<dt><code>BadKeyboard</code></dt>
<dd><i>device_spec</i> does not specify a device with indicators.</dd>
<dt><code>BadMatch</code></dt>
<dd><i>led_id</i> is not <code>DfltXIId</code> and does not specify a feedback of the class specified by <i>led_class</i> on the device specified by <i>device_spec</i>.</dd>
<dt><code>BadValue</code></dt>
<dd><i>led_class</i> does not specify <code>DfltXIClass</code>, <code>LedFeedbackClass</code>, or <code>KbdFeedbackClass</code>.</dd></dl>
<h2>See Also</h2>
<p><code>XkbIndicatorMapNotify</code>(3), <code>XkbIndicatorStateNotify</code>(3), <code>XkbNamesNotify</code>(3)</p>
