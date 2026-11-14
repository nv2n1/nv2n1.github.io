---
title: "xkbgetindicatorstate(3)"
name: "xkbgetindicatorstate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetindicatorstate/"
description: "XkbGetIndicatorState – Obtains the current state of the keyboard indicators"
---

<p>XkbGetIndicatorState &#8211; Obtains the current state of the keyboard indicators </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetIndicatorState</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>state_return</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; state_return</i></p>
<dd>backfilled with a mask of the indicator state</dl>
<h2>Description</h2>
<p>Xkb allows applications to obtain information about indicators using two different methods. The first method, which is similar to the core X implementation, uses a mask to specify the indicators. The second method, which is more suitable for applications concerned with interoperability, uses indicator names. The correspondence between the indicator name and the bit position in masks is as follows: one of the parameters returned from <i>XkbGetNamedIndicators </i> is an index that is the bit position to use in any function call that requires a mask of indicator bits, as well as the indicator&#8217;s index into the XkbIndicatorRec array of indicator maps. </p>
<p> <i>XkbGetIndicatorState </i> queries the <i>display </i> for the state of the indicators on the device specified by the <i>device_spec. </i> For each indicator that is &quot;turned on&quot; on the device, the associated bit is set in <i>state_return. </i> If a compatible version of the Xkb extension is not available in the server, <i>XkbGetIndicatorState</i> returns a BadMatch error. Otherwise, it sends the request to the X server, places the state of the indicators into <i>state_return, </i> and returns Success. Thus the value reported by <i>XkbGetIndicatorState </i> is identical to the value reported by the core protocol.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetnamedindicators/">XkbGetNamedIndicators</a></code>(3)</p>
