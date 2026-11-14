---
title: "xvqueryadaptors(3)"
name: "xvqueryadaptors"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvqueryadaptors/"
description: "XvQueryAdaptors – return adaptor information for a screen"
---

<p>XvQueryAdaptors &#8211; return adaptor information for a screen</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvQueryAdaptors(Display *</code><i>dpy</i><code>, Window </code><i>window</i><code>,</code>
<code> unsigned int *</code><i>p_num_adaptors</i><code>,</code>
<code> XvAdaptorInfo **</code><i>pp_adaptor_info</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>window</i></p>
<dd>Specifies a window of the screen for which the adaptor information is desired.</p>
<dt><i>p_num_adaptors</i></p>
<dd>A pointer to where the number of adaptors for the specified screen is returned.</p>
<dt><i>pp_adaptor_info</i></p>
<dd>A pointer to where the list of returned adaptor information is returned.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3)<br />
&nbsp;<wbr>returns an video adaptor information for the screen of the specified drawable. The XvAdaptorInfo structure has the following organization: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br />
&nbsp;<wbr>XvPortID base_id;<br />
&nbsp;<wbr>unsigned long num_ports;<br />
&nbsp;<wbr>char type;<br />
&nbsp;<wbr>char&nbsp;<wbr>*name;<br />
&nbsp;<wbr>unsigned long num_formats;<br />
&nbsp;<wbr>XvFormat&nbsp;<wbr>*formats;<br />
&nbsp;<wbr>unsigned long num_adaptors;<br />
&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>XvAdaptorInfo; </p>
<dl COMPACT>
<dt><i>base_id</i></p>
<dd>The resource ID of the first adaptor port.</p>
<dt><i>num_ports</i></p>
<dd>The number of ports supported by the adaptor.</p>
<dt><i>type</i></p>
<dd>A bit mask with the value XvInputMask asserted if the adaptor supports video input, and value XvOutputMask asserted if the adaptor supports video output. In Xv protocol 2.2 and later, there are 3 new bits defined &#8211; XvVideoMask, XvStillMask and XvImageMask indicating that the adaptor is capable of video, still or image primitives respectively.</p>
<dt><i>name</i></p>
<dd>A vendor specific name that identifies the adaptor.</p>
<dt><i>num_formats</i></p>
<dd>The number of depth/visual id formats supported by the adaptor.</p>
<dt><i>formats</i></p>
<dd>A pointer to an array of XvFormat structures.</dl>
<p> The XvFormat structure has the following organization: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br />
&nbsp;<wbr>char depth;<br />
&nbsp;<wbr>unsigned long visual_id;<br />
&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>XvFormat; </p>
<dl COMPACT>
<dt><i>depth</i></p>
<dd>A drawable depth supported by the adaptor.</p>
<dt><i>visual_id</i></p>
<dd>A visual-id supported for the given depth by the adaptor.</dl>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[Drawable]</p>
<dd>Returned if the requested drawable does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvfreeadaptorinfo/">XvFreeAdaptorInfo</a></code>(3)</p>
