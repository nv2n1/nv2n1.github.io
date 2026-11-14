---
title: "xvshmputimage(3)"
name: "xvshmputimage"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvshmputimage/"
description: "XvPutImage, XvShmPutImage – display an XvImage"
---

<p>XvPutImage, XvShmPutImage &#8211; display an XvImage</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvPutImage (Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>,</code>
<code> Drawable </code><i>d</i><code>, GC </code><i>gc</i><code>, XvImage *</code><i>image</i><code>,</code>
<code> int </code><i>src_x</i><code>, int </code><i>src_y</i><code>,</code>
<code> unsigned int </code><i>src_w</i><code>, unsigned int </code><i>src_h</i><code>,</code>
<code> int </code><i>dest_x</i><code>, int </code><i>dest_y</i><code>,</code>
<code> unsigned int </code><i>dest_w</i><code>, unsigned int </code><i>dest_h</i><code>);</code>
<code>int XvShmPutImage (Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>,</code>
<code> Drawable </code><i>d</i><code>, GC </code><i>gc</i><code>, XvImage *</code><i>image</i><code>,</code>
<code> int </code><i>src_x</i><code>, int </code><i>src_y</i><code>,</code>
<code> unsigned int </code><i>src_w</i><code>, unsigned int </code><i>src_h</i><code>,</code>
<code> int </code><i>dest_x</i><code>, int </code><i>dest_y</i><code>,</code>
<code> unsigned int </code><i>dest_w</i><code>, unsigned int </code><i>dest_h</i><code>,</code>
<code> Bool </code><i>send_event</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>The port id of a port on an XvImage capable adaptor.</p>
<dt><i>d</p>
<dd>
<dt>gc</i></p>
<dd>the graphics context specifying the clip mask to use, if any.</p>
<dt><i>image</i></p>
<dd>A pointer to the XvImage to be displayed.</p>
<dt><i>src_?</i></p>
<dd>The portion of the XvImage to be displayed.</p>
<dt><i>dest_?</i></p>
<dd>The portion of the destination drawable to be filled by the image.</p>
<dt><i>send_event</i></p>
<dd>Indicates whether or not an XShmCompletionEvent should be sent. If sent, the event&#8217;s major_code and minor_code fields will indicate the Xv extension&#8217;s major code and XvShmPutImage&#8217;s minor code.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvputimage/">XvPutImage</a></code>(3) is similar to <code><a href="/docs/linux/man/3-xputimage/">XPutImage</a></code>(3). <code><a href="/docs/linux/man/3-xvshmputimage/">XvShmPutImage</a></code>(3) is similar to <code><a href="/docs/linux/man/3-xshmputimage/">XShmPutImage</a></code>(3). The library will allocate the XvImage structure and fill out all fields except for <i>data</i>. <i>Width</i> and <i>height</i> may be enlarged in some YUV formats. The size of the data buffer that needs to be allocated will be given in the <i>data_size</i> field in the XvImage. Image data is not allocated by this function. The client may pass a pointer to the preallocated memory as <i>data</i> or may allocate the memory and fill in the XvImage structure&#8217;s data field after the <i>data_size</i> field has been filled out by the server. The XvImage structure may be freed by <code><a href="/docs/linux/man/3-xfree/">XFree</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</p>
<dt>[XvBadAlloc]</p>
<dd>Generated if the X server was unable to allocate resources required to complete the operation.</p>
<dt>[BadMatch]</p>
<dd>Generated if incompatible arguments were supplied, such as a port that isn&#8217;t capable of displaying XvImages.</p>
<dt>[BadShmSegCode]</p>
<dd>Generated if an invalid shared memory segment is specified.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvlistimageformats/">XvListImageFormats</a></code>(3), <code><a href="/docs/linux/man/3-xvcreateimage/">XvCreateImage</a></code>(3), <code><a href="/docs/linux/man/3-xvshmcreateimage/">XvShmCreateImage</a></code>(3) <code><a href="/docs/linux/man/3-xputimage/">XPutImage</a></code>(3), <code><a href="/docs/linux/man/3-xshmputimage/">XShmPutImage</a></code>(3)</p>
