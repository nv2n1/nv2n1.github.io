---
title: "xkbgetnamedindicator(3)"
name: "xkbgetnamedindicator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetnamedindicator/"
description: "XkbGetNamedIndicator – Look up the indicator map and other information for an indicator by name"
---

<p>XkbGetNamedIndicator &#8211; Look up the indicator map and other information for an indicator by name </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbGetNamedDeviceIndicator</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>dev_spec</i><code>,</code> <code>unsigned int </code><i>led_class</i><code>,</code> <code>unsigned int </code><i>led_id</i><code>,</code> <code>Atom </code><i>name</i><code>,</code> <code>int *</code><i>ndx_rtrn</i><code>,</code> <code>Bool *</code><i>state_rtrn</i><code>,</code> <code>XkbIndicatorMapPtr </code><i>map_rtrn</i><code>,</code> <code>Bool *</code><i>real_rtrn</i><code>);</code></p>
<dt> <code>Bool XkbGetNamedIndicator</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>Atom </code><i>name</i><code>,</code> <code>int *</code><i>ndx_rtrn</i><code>,</code> <code>Bool *</code><i>state_rtrn</i><code>,</code> <code>XkbIndicatorMapPtr </code><i>map_rtrn</i><code>,</code> <code>Bool *</code><i>real_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; dev_spec</i></p>
<dd>keyboard device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; led_class</i></p>
<dd>feedback class, or XkbDfltXIClass</p>
<dt><i>&#8211; led_id</i></p>
<dd>feedback ID, or XkbDfltXIId</p>
<dt><i>&#8211; name</i></p>
<dd>name of the indicator to be retrieved</p>
<dt><i>&#8211; ndx_rtrn</i></p>
<dd>backfilled with the index of the retrieved indicator</p>
<dt><i>&#8211; state_rtrn</i></p>
<dd>backfilled with the current state of the retrieved indicator</p>
<dt><i>&#8211; map_rtrn</i></p>
<dd>&nbsp;backfilled with the mapping for the retrieved indicator&nbsp;</p>
<dt><i>&#8211; real_rtrn</i></p>
<dd>backfilled with True if the named indicator is real (physical)</dl>
<h2>Description</h2>
<p>Xkb also allows applications to refer to indicators by name. Use <i>XkbGetNames </i> to get the indicator names. Using names eliminates the need for hard-coding bitmask values for particular keyboards. For example, instead of using vendor-specific constants such as WSKBLed_ScrollLock mask on Digital workstations or XLED_SCROLL_LOCK on Sun workstations, you can instead use <i>XkbGetNamedDeviceIndicator</i> to look up information on the indicator named &quot;Scroll Lock.&quot; </p>
<p> If the device specified by <i>device_spec </i> has an indicator named <i>name</i>, <i>XkbGetNamedDeviceIndicator</i> returns True and populates the rest of the parameters with information about the indicator. Otherwise, <i>XkbGetNamedDeviceIndicator</i> returns False. </p>
<p> The <i>ndx_rtrn </i> field returns the zero-based index of the named indicator. This index is the bit position to use in any function call that requires a mask of indicator bits, as well as the indicator&#8217;s index into the XkbIndicatorRec array of indicator maps. <i>state_rtrn </i> returns the current state of the named indicator (True = on, False = off). <i>map_rtrn </i> returns the indicator map for the named indicator. In addition, if the indicator is mapped to a physical LED, the <i>real_rtrn </i> parameter is set to True. </p>
<p> Each of the &quot; <i>_rtrn</i> &quot; arguments is optional; you can pass NULL for any unneeded &quot; <i>_rtrn</i> &quot; arguments. </p>
<p> <i>XkbGetNamedIndicator</i> is a convenience function that calls <i>XkbGetNamedDeviceIndicator</i> with a <i>device_spec</i> of <code>XkbUseCoreKbd</code>, a <i>led_class</i> of <code>XkbDfltXIClass</code>, and a <i>led_id</i> of <code>XkbDfltXIId</code>. It returns the return value from <i>XkbGetNamedDeviceIndicator</i>. </p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbGetNamedIndicator</i> and <i>XkbGetNamedDeviceIndicator</i> functions return True if the device specified by <i>device_spec </i> has an indicator named <i>name</i>.</p>
<dt>False</p>
<dd>The <i>XkbGetNamedIndicator</i> and <i>XkbGetNamedDeviceIndicator</i> functions return False if the device specified by <i>device_spec </i> does not have an indicator named <i>name</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetnames/">XkbGetNames</a></code>(3)</p>
