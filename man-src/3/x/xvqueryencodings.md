---
title: "xvqueryencodings(3)"
name: "xvqueryencodings"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvqueryencodings/"
description: "XvQueryEncodings – return list of encodings for an adaptor"
---

<p>XvQueryEncodings &#8211; return list of encodings for an adaptor</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvQueryEncodings(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>,</code>
<code> unsigned int *</code><i>p_num_encodings</i><code>,</code>
<code> XvEncodingInfo **</code><i>pp_encoding_info</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Specifies the port whose adaptor is to be queried for its list of encodings.</p>
<dt><i>p_num_encodings</i></p>
<dd>A pointer to where the number of encodings supported by the adaptor is written.</p>
<dt><i>pp_encoding_info</i></p>
<dd>A pointer to where the list of returned encoding information is returned. XvEncodingInfo has the following structure: </p>
<p>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br />
XvEncodingID encoding_id;<br />
char&nbsp;<wbr>*name;<br />
unsigned long width;<br />
unsigned long height;<br />
XvRational rate;<br />
unsigned long num_encodings;<br />
&nbsp;<wbr>}&nbsp;<wbr>XvEncodingInfo; </p>
<dt><i>encoding_id</i></p>
<dd>Specifies the encoding-id of the encoding. The encoding-id is used to identify an encoding when a port&#8217;s encoding attribute is changed.</p>
<dt><i>name</i></p>
<dd>A pointer to a formatted string that identifies the encoding. The string has the format &quot;<i>timing</i>&#8211;<i>signaltype</i>&quot;. For example &quot;ntsc-composite&quot;.</p>
<dt><i>width,height</i></p>
<dd>The width and height, in pixels, of the decoded video image.</p>
<dt><i>rate</i></p>
<dd>The field rate of the decoded video.</dl>
<p> The XvRational structure is used to specify a fractional number. It has the following structure: </p>
<p>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br />
int numerator;<br />
int denominator;<br />
&nbsp;<wbr>}&nbsp;<wbr>XvRational; </p>
<p> The <i>numerator</i> and <i>denominator</i> fields specify the appropriate parts of a fractional number.</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3) returns encoding information about an adaptor. Each encoding is described by the XvEncodingInfo structure described above. The encodings are identified by an encoding-id, which can be used to set or get the encoding attribute of a port.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvfreeencodinginfo/">XvFreeEncodingInfo</a></code>(3)</p>
