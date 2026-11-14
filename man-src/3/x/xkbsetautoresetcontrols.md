---
title: "xkbsetautoresetcontrols(3)"
name: "xkbsetautoresetcontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetautoresetcontrols/"
description: "XkbSetAutoResetControls – Changes the current values of the AutoReset control attributes"
---

<p>XkbSetAutoResetControls &#8211; Changes the current values of the AutoReset control attributes </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetAutoResetControls</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>changes</i><code>,</code> <code>unsigned int *</code><i>auto_ctrls</i><code>,</code> <code>unsigned int *</code><i>auto_values</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; changes</i></p>
<dd>controls for which to change auto-reset values</p>
<dt><i>&#8211; auto_ctrls</i></p>
<dd>controls from changes that should auto reset</p>
<dt><i>&#8211; auto_values</i></p>
<dd>1 bit =&gt; auto-reset on</dl>
<h2>Description</h2>
<p><i>XkbSetAutoResetControls </i> changes the auto-reset status and associated auto-reset values for the controls selected by <i>changes. </i> For any control selected by <i>changes, </i> if the corresponding bit is set in <i>auto_ctrls, </i> the control is configured to auto-reset when the client exits. If the corresponding bit in <i>auto_values </i> is on, the control is turned on when the client exits; if zero, the control is turned off when the client exits. For any control selected by <i>changes, </i> if the corresponding bit is not set in <i>auto_ctrls, </i> the control is configured to not reset when the client exits. </p>
<p> For example: </p>
<pre>To leave the auto-reset controls for StickyKeys the way they are:
 ok = XkbSetAutoResetControls(dpy, 0, 0, 0);
 
To change the auto-reset controls so that StickyKeys are unaffected when the 
client exits:
 ok = XkbSetAutoResetControls(dpy, XkbStickyKeysMask, 0, 0);
 
To change the auto-reset controls so that StickyKeys are turned off when the 
client exits:
 ok = XkbSetAutoResetControls(dpy, XkbStickyKeysMask, XkbStickyKeysMask, 0);
 
To change the auto-reset controls so that StickyKeys are turned on when the 
client exits:
 ok = XkbSetAutoResetControls(dpy, XkbStickyKeysMask, XkbStickyKeysMask, 
XkbStickyKeysMask);</pre>
<p><i>XkbSetAutoResetControls </i> backfills <i>auto_ctrls </i> and <i>auto_values </i> with the auto-reset controls for this particular client. Note that all of the bits are valid in the returned values, not just the ones selected in the <i>changes </i> mask.</p>
