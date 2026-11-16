---
title: "xvcreateimage(3)"
name: "xvcreateimage"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvcreateimage/"
description: "XvCreateImage, XvShmCreateImage – create an XvImage"
---

<p>XvCreateImage, XvShmCreateImage &#8211; create an XvImage</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>XvImage * XvCreateImage (Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>,</code>
<code> int </code><i>id</i><code>, char *</code><i>data</i><code>,</code>
<code> int </code><i>width</i><code>, int </code><i>height</i><code>);</code>
<code>XvImage * XvShmCreateImage (Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>,</code>
<code> int </code><i>id</i><code>, char *</code><i>data</i><code>,</code>
<code> int </code><i>width</i><code>, int </code><i>height</i><code>,</code>
<code> XShmSegmentInfo *</code><i>shminfo</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>port</i></dt>
<dd>Specifies the port the XvImage will be used with.</dd>
<dt><i>id</i></dt>
<dd>Specifies the format of the image to be created by the XvImageFormatValues id.</dd>
<dt><i>data</i></dt>
<dd>Specifies the image data.</dd>
<dt><i>width</i>, <i>height</i></dt>
<dd>Specifies the desired width and height of the image.</dd></dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvcreateimage/">XvCreateImage</a></code>(3) is similar to <code><a href="/docs/linux/man/3-xcreateimage/">XCreateImage</a></code>(3). <code><a href="/docs/linux/man/3-xvshmcreateimage/">XvShmCreateImage</a></code>(3) is similar to <code><a href="/docs/linux/man/3-xshmcreateimage/">XShmCreateImage</a></code>(3). The library will allocate the XvImage structure and fill out all fields except for <i>data</i>. <i>Width</i> and <i>height</i> may be enlarged in some YUV formats. The size of the data buffer that needs to be allocated will be given in the <i>data_size</i> field in the XvImage. Image data is not allocated by this function. The client may pass a pointer to the preallocated memory as <i>data</i> or may allocate the memory and fill in the XvImage structure&#8217;s data field after the <i>data_size</i> field has been filled out by the server. The XvImage structure may be freed by <code><a href="/docs/linux/man/3-xfree/">XFree</a></code>(3). Shared memory segments are attached/detached with <code><a href="/docs/linux/man/3-xshmattach/">XShmAttach</a></code>(3)/<code><a href="/docs/linux/man/3-xshmdetach/">XShmDetach</a></code>(3).</p>
<h2>Return Values</h2>
<p>XvImage has the following structure: </p>
<p> typedef struct {<br />
int id;<br />
int width, height;<br />
int data_size;<br />
int num_planes;<br />
int&nbsp;<wbr>*pitches;<br />
int&nbsp;<wbr>*offsets;<br />
char&nbsp;<wbr>*data;<br />
XPointer obdata; } XvImage; </p>
<dl COMPACT>
<dt><i>id</i></dt>
<dd>A descriptor for the format from the XvImageFormatValues structure returned by <code><a href="/docs/linux/man/3-xvlistimageformats/">XvListImageFormats</a></code>(3).</dd>
<dt><i>width, height</i></dt>
<dd>The width and height of the image in pixels.</dd>
<dt><i>data_size</i></dt>
<dd>The size of the data buffer in bytes.</dd>
<dt><i>num_planes</i></dt>
<dd>The number of image planes.</dd>
<dt><i>pitches</i></dt>
<dd>An array of size <i>num_planes</i> indicating the scanline pitch in bytes. Each plane may have a different pitch.</dd>
<dt><i>offsets</i></dt>
<dd>An array of size <i>num_planes</i> indicating the byte offset from <i>data</i> to the start of each plane.</dd>
<dt><i>data</i></dt>
<dd>A pointer to the start of the data buffer.</dd>
<dt><i>obdata</i></dt>
<dd>A private field for holding SHM info. This field will be set up by the client libraries so the programmer will generally need not be concerned with this field.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</dt>
<dd>Generated if the requested port does not exist.</dd>
<dt>[XvBadAlloc]</dt>
<dd>Generated if the X server was unable to allocate resources required to complete the operation.</dd>
<dt>[BadMatch]</dt>
<dd>Generated if incompatible arguments were supplied, such as a port that isn&#8217;t capable of displaying XvImages.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvlistimageformats/">XvListImageFormats</a></code>(3), <code><a href="/docs/linux/man/3-xcreateimage/">XCreateImage</a></code>(3), <code><a href="/docs/linux/man/3-xshmcreateimage/">XShmCreateImage</a></code>(3), <code><a href="/docs/linux/man/3-xshmattach/">XShmAttach</a></code>(3), <code><a href="/docs/linux/man/3-xshmdetach/">XShmDetach</a></code>(3).</p>
