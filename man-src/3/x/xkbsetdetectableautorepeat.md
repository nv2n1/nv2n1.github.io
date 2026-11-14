---
title: "xkbsetdetectableautorepeat(3)"
name: "xkbsetdetectableautorepeat"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetdetectableautorepeat/"
description: "XkbSetDetectableAutorepeat – Sets DetectableAutorepeat"
---

<p>XkbSetDetectableAutorepeat &#8211; Sets DetectableAutorepeat</p>
<h2>Syntax</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetDetectableAutorepeat</code> <code>(Display *</code><i>display</i><code>,</code> <code>Bool </code><i>detectable</i><code>,</code> <code>Bool *</code><i>supported_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; detectable</i></p>
<dd>True =&gt; set DetectableAutorepeat</p>
<dt><i>&#8211; supported_rtrn</i></p>
<dd>backfilled True if DetectableAutorepeat supported</dl>
<h2>Description</h2>
<p>Auto-repeat is the generation of multiple key events by a keyboard when the user presses a key and holds it down. Keyboard hardware and device-dependent X server software often implement auto-repeat by generating multiple KeyPress events with no intervening KeyRelease event. The standard behavior of the X server is to generate a KeyRelease event for every KeyPress event. If the keyboard hardware and device-dependent software of the X server implement auto-repeat by generating multiple KeyPress events, the device-independent part of the X server by default synthetically generates a KeyRelease event after each KeyPress event. This provides predictable behavior for X clients, but does not allow those clients to detect the fact that a key is auto-repeating. </p>
<p> Xkb allows clients to request <i>detectable auto-repeat. </i> If a client requests and the server supports DetectableAutorepeat, Xkb generates KeyRelease events only when the key is physically released. If DetectableAutorepeat is not supported or has not been requested, the server synthesizes a KeyRelease event for each repeating KeyPress event it generates. </p>
<p> DetectableAutorepeat, unlike other controls, is not contained in the XkbControlsRec structure, nor can it be enabled or disabled via the EnabledControls control. Instead, query and set DetectableAutorepeat using <i>XkbGetDetectableAutorepeat </i> and <i>XkbSetDetectableAutorepeat.</i> </p>
<p> DetectableAutorepeat is a condition that applies to all keyboard devices for a client&#8217;s connection to a given X server; it cannot be selectively set for some devices and not for others. For this reason, none of the Xkb library functions involving DetectableAutorepeat involve a device specifier. </p>
<p> This request affects all keyboard activity for the requesting client only; other clients still see the expected nondetectable auto-repeat behavior, unless they have requested otherwise. </p>
<p> <i>XkbSetDetectableAutorepeat </i> sends a request to the server to set DetectableAutorepeat on for the current client if <i>detectable </i> is True, and off if <i>detectable </i> is False; it then waits for a reply. If <i>supported_rtrn </i> is not NULL, <i>XkbSetDetectableAutorepeat </i> backfills <i>supported_rtrn </i> with True if the server supports DetectableAutorepeat, and False if it does not. <i>XkbSetDetectableAutorepeat </i> returns the current state of DetectableAutorepeat for the requesting client: True if DetectableAutorepeat is set, and False otherwise.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetDetectableAutorepeat </i> function returns True if DetectableAutorepeat is set.</p>
<dt>False</p>
<dd>The <i>XkbSetDetectableAutorepeat </i> function returns False if DetectableAutorepeat is not set. </p>
</dl>
