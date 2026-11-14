---
title: "xvqueryportattributes(3)"
name: "xvqueryportattributes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvqueryportattributes/"
description: "XvQueryPortAttributes – return list of attributes of a video port"
---

<p>XvQueryPortAttributes &#8211; return list of attributes of a video port</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>XvAttribute* XvQueryPortAttributes(Display *</code><i>dpy</i><code>,</code>
<code> XvPortID </code><i>port</i><code>, int *</code><i>p_num_attributes</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Specifies the port whose adaptor is to be queried for its list of attributes.</p>
<dt><i>p_num_attributes</i></p>
<dd>A pointer to where the number of attributes returned in the array is written.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvqueryportattributes/">XvQueryPortAttributes</a></code>(3)<code>returns</code>the<code>number</code>of<code>attributes</code> and an array of XvAttributes valid for the given port. The array may be freed with <code><a href="/docs/linux/man/3-xfree/">XFree</a></code>(3).</p>
<h2>Return Values</h2>
<p>XvAttribute has the following structure: </p>
<p>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br />
int flags;<br />
int min_value;<br />
int max_value;<br />
char&nbsp;<wbr>*name;<br />
&nbsp;<wbr>}&nbsp;<wbr>XvAttribute; </p>
<dl COMPACT>
<dt><i>flags</i></p>
<dd>May be XvGettable or XvSettable or both OR&#8217;d together indicating the particular attribute is readable, writeable or readable and writeable.</p>
<dt><i>min_value</i></p>
<dd>The minimum attribute values which are valid for the driver.</p>
<dt><i></p>
<dd>The maximum attribute values which are valid for the driver.</p>
<dt>name</i></p>
<dd>A string describing the name of the attribute that may be used to retrieve the Atom for the particular attribute.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvgetportattribute/">XvGetPortAttribute</a></code>(3), <code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3)</p>
