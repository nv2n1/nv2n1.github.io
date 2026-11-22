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
<dt><i>dpy</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>window</i></dt>
<dd>Specifies a window of the screen for which the adaptor information is desired.</dd>
<dt><i>p_num_adaptors</i></dt>
<dd>A pointer to where the number of adaptors for the specified screen is returned.</dd>
<dt><i>pp_adaptor_info</i></dt>
<dd>A pointer to where the list of returned adaptor information is returned.</dd></dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3)<br/>
&nbsp;<wbr>returns an video adaptor information for the screen of the specified drawable. The XvAdaptorInfo structure has the following organization: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br/>
&nbsp;<wbr>XvPortID base_id;<br/>
&nbsp;<wbr>unsigned long num_ports;<br/>
&nbsp;<wbr>char type;<br/>
&nbsp;<wbr>char&nbsp;<wbr>*name;<br/>
&nbsp;<wbr>unsigned long num_formats;<br/>
&nbsp;<wbr>XvFormat&nbsp;<wbr>*formats;<br/>
&nbsp;<wbr>unsigned long num_adaptors;<br/>
&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>XvAdaptorInfo; </p>
<dl COMPACT>
<dt><i>base_id</i></dt>
<dd>The resource ID of the first adaptor port.</dd>
<dt><i>num_ports</i></dt>
<dd>The number of ports supported by the adaptor.</dd>
<dt><i>type</i></dt>
<dd>A bit mask with the value XvInputMask asserted if the adaptor supports video input, and value XvOutputMask asserted if the adaptor supports video output. In Xv protocol 2.2 and later, there are 3 new bits defined &#8211; XvVideoMask, XvStillMask and XvImageMask indicating that the adaptor is capable of video, still or image primitives respectively.</dd>
<dt><i>name</i></dt>
<dd>A vendor specific name that identifies the adaptor.</dd>
<dt><i>num_formats</i></dt>
<dd>The number of depth/visual id formats supported by the adaptor.</dd>
<dt><i>formats</i></dt>
<dd>A pointer to an array of XvFormat structures.</dd></dl>
<p> The XvFormat structure has the following organization: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>typedef struct&nbsp;<wbr>{<br/>
&nbsp;<wbr>char depth;<br/>
&nbsp;<wbr>unsigned long visual_id;<br/>
&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>XvFormat; </p>
<dl COMPACT>
<dt><i>depth</i></dt>
<dd>A drawable depth supported by the adaptor.</dd>
<dt><i>visual_id</i></dt>
<dd>A visual-id supported for the given depth by the adaptor.</dd></dl>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3) completed successfully.</dd>
<dt>[XvBadExtension]</dt>
<dd>Returned if the Xv extension is unavailable.</dd>
<dt>[XvBadAlloc]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3) failed to allocate memory to process the request.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[Drawable]</dt>
<dd>Returned if the requested drawable does not exist.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvfreeadaptorinfo/">XvFreeAdaptorInfo</a></code>(3)</p>
