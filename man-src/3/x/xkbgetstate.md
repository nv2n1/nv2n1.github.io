---
title: "xkbgetstate(3)"
name: "xkbgetstate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetstate/"
description: "XkbGetState – Obtains the keyboard state"
---

<p>XkbGetState &#8211; Obtains the keyboard state </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetState</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>XkbStatePtr </code><i>state_return</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>state_return</i></p>
<dd>backfilled with Xkb state</dl>
<h2>Description</h2>
<p>The <i>XkbGetState </i> function queries the server for the current keyboard state, waits for a reply, and then backfills <i>state_return </i> with the results. </p>
<p> All group values are expressed as group indices in the range [0..3]. Modifiers and the compatibility modifier state values are expressed as the bitwise union of the core X11 modifier masks. The pointer button state is reported as in the core X11 protocol.</p>
