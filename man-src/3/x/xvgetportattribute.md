---
title: "xvgetportattribute(3)"
name: "xvgetportattribute"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvgetportattribute/"
description: "XvGetPortAttribute – return current port attribute value"
---

<p>XvGetPortAttribute &#8211; return current port attribute value</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvGetPortAttribute(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>,</code>
<code> Atom </code><i>attribute</i><code>, int </code><i>p_value</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Specifies the port, associated with the given display, for which the attribute values are to be returned.</p>
<dt><i>attribute</i></p>
<dd>An atom that identifies the attribute to be queried by this request. Control atoms are obtained using the XInternAtom request with a string from the following table.</p>
<dt><i>p_value</i></p>
<dd>Pointer to the location where the attribute value is written on return.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvgetportattribute/">XvGetPortAttribute</a></code>(3) returns the current value of the requested port attribute in the integer pointed to by <i>p_value</i>. The attribute is identified using an Atom that equates to the attribute name. The XInternAtom request can be used with one of the strings below to return a matching Atom. </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Attribute String</td>
<td>Type</td>
<td>Default
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&quot;XV_ENCODING&quot;</td>
<td>XvEncodingID</td>
<td>Server dependent
</td>
</tr>
<tr VALIGN=top>
<td>&quot;XV_HUE&quot;</td>
<td>[-1000&#8230;1000]</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>&quot;XV_SATURATION&quot;</td>
<td>[-1000&#8230;1000]</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>&quot;XV_BRIGHTNESS&quot;</td>
<td>[-1000&#8230;1000]</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>&quot;XV_CONTRAST&quot;</td>
<td>[-1000&#8230;1000]</td>
<td>0
</td>
</tr>
</table>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvgetportattribute/">XvGetPortAttribute</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvgetportattribute/">XvGetPortAttribute</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</p>
<dt>[BadMatch]</p>
<dd>Generated if the requested attribute atom does not specify an attribute supported by the adaptor.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3), <code><a href="/docs/linux/man/3-xvportnotify/">XvPortNotify</a></code>(3)</p>
