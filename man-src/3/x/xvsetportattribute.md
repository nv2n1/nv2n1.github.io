---
title: "xvsetportattribute(3)"
name: "xvsetportattribute"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvsetportattribute/"
description: "XvSetPortAttribute – sets an attribute of a video port"
---

<p>XvSetPortAttribute &#8211; sets an attribute of a video port</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvSetPortAttribute(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>,</code>
<code> Atom </code><i>attribute</i><code>, int </code><i>value</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Specifies the port for which the attribute is to be used.</p>
<dt><i>attribute</i></p>
<dd>Identifies the port attribute to be set by this request. Can be one of the table entries under the column &quot;String,&quot; below.</p>
<dt><i>value</i></p>
<dd>Identifies the value to which <i>attribute</i> is to be set. Can be one of the table entries under the column &quot;Type,&quot; below.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3)<br />
&nbsp;<wbr>permits a client to set the port attribute to specified values. This request supports the following values: </p>
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
<p> The supplied encoding must be one of the encodings listed for the adaptor, otherwise an Encoding error results. </p>
<p> If the adaptor does not support the exact hue, saturation, brightness, and contrast levels supplied, the closest levels supported are assumed. Use <code><a href="/docs/linux/man/3-xvgetportattribute/">XvGetPortAttribute</a></code>(3) to query the resulting levels. </p>
<p> When an <code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3) request is processed, a <code><a href="/docs/linux/man/3-xvportnotify/">XvPortNotify</a></code>(3) event is generated for all clients that have requested notification of port changes using <code><a href="/docs/linux/man/3-xvselectportnotify/">XvSelectPortNotify</a></code>(3).</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</p>
<dt>[XvBadEncoding]</p>
<dd>Generated if an encoding is specified that does not exist.</p>
<dt>[BadMatch]</p>
<dd>Generated if the requested attribute atom does not specify an attribute supported by the adaptor.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvgetportattribute/">XvGetPortAttribute</a></code>(3), <code><a href="/docs/linux/man/3-xvqueryportattributes/">XvQueryPortAttributes</a></code>(3), <code><a href="/docs/linux/man/3-xvselectportnotify/">XvSelectPortNotify</a></code>(3), <code><a href="/docs/linux/man/3-xvportnotify/">XvPortNotify</a></code>(3)</p>
