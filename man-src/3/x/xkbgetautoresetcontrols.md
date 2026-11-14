---
title: "xkbgetautoresetcontrols(3)"
name: "xkbgetautoresetcontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetautoresetcontrols/"
description: "XkbGetAutoResetControls – Gets the current values of the auto-reset controls"
---

<p>XkbGetAutoResetControls &#8211; Gets the current values of the auto-reset controls </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbGetAutoResetControls</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int *</code><i>auto_ctrls</i><code>,</code> <code>unsigned int *</code><i>auto_values</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>&nbsp;connection to X server</p>
<dt><i>&#8211; auto_ctrls</i></p>
<dd>&nbsp;specifies which bits in auto_values are relevant</p>
<dt><i>&#8211; auto_values</i></p>
<dd>
<dd>1 bit =&gt; corresponding control has auto-reset on</dl>
<h2>Description</h2>
<p>You can configure the boolean controls to automatically be enabled or disabled when a program exits. This capability is controlled via two masks maintained in the X server on a per-client basis. There is no client-side Xkb data structure corresponding to these masks. Whenever the client exits for any reason, any boolean controls specified in the <i>auto-reset mask </i> are set to the corresponding value from the <i>auto-reset values </i> mask. This makes it possible for clients to &quot;clean up after themselves&quot; automatically, even if abnormally terminated. The bits used in the masks correspond to the EnabledControls control bits. </p>
<p> For example, a client that replaces the keyboard bell with some other audible cue might want to turn off the AudibleBell control to prevent the server from also generating a sound and avoid cacophony. If the client were to exit without resetting the AudibleBell control, the user would be left without any feedback at all. Setting AudibleBell in both the auto-reset mask and auto-reset values guarantees that the audible bell will be turned back on when the client exits. </p>
<p> <i>XkbGetAutoResetControls </i> backfills <i>auto_ctrls </i> and <i>auto_values </i> with the AutoReset control attributes for this particular client. It returns True if successful, and False otherwise.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbGetAutoResetControls </i> function returns True when it successfully backfills <i>auto_ctrls </i> and <i>auto_values </i> with the AutoReset control attributes for this particular client.</p>
<dt>False</p>
<dd>The <i>XkbGetAutoResetControls </i> function returns False when it does not successfully backfill <i>auto_ctrls </i> and <i>auto_values </i> with the AutoReset control attributes for this particular client. </p>
</dl>
