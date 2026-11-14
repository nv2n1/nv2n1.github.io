---
title: "xresqueryclients(3)"
name: "xresqueryclients"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xresqueryclients/"
description: "XRes – X-Resource extension client library"
---

<p>XRes &#8211; X-Resource extension client library</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/XRes.h&gt;</code> </p>
<pre>typedef struct {
 XID resource_base;
 XID resource_mask;
} XResClient;
typedef struct {
 Atom resource_type;
 unsigned int count;
} XResType;</pre>
<dl COMPACT>
<dd>Bool XResQueryExtension(Display *<i>dpy</i>, int *<i>event_base_return</i>, int *<i>error_base_return</i>);</p>
<dd>Status XResQueryVersion(Display *<i>dpy</i>, int *<i>major_version_return</i>, int *<i>minor_version_return</i>);</p>
<dd>Status XResQueryClients(Display *<i>dpy</i>, int *<i>num_clients</i>, XResClient **<i>clients</i>);</p>
<dd>Status XResQueryClientResources(Display *<i>dpy</i>, XID <i>xid</i>, int *<i>num_types</i>, XResType **<i>types</i>);</p>
<dd>Status XResQueryClientPixmapBytes(Display *<i>dpy</i>, XID <i>xid</i>, unsigned long *<i>bytes</i>);</dl>
<h2>Description</h2>
<p><code>X-Resource</code> is an extension that allows a client to query the X server about its usage of various resources. It should not be confused with the X resource database access functions. </p>
<p> <code>XResQueryExtension</code> returns <code>True</code> if the <i>XRes</i> extension is available on the given display. A client must call <code>XResQueryExtension</code> before calling any other XRes function in order to negotiate a compatible protocol version; otherwise the client will get undefined behavior (XRes may or may not work). </p>
<p> <code>XResQueryVersion</code> returns <code>True</code> if the request succeeded; the values of the major and minor protocol versions supported by the server are returned in <i>major_version_return</i> and <i>minor_version_return .</i> </p>
<p> <code>XResQueryClients</code> fills a list of clients of the given display. For each client it returns in the <i>XResClient</i> structure a mask and a base value of the resources used by these clients. Returns <code>True</code> on success or <code>False</code> on failure. </p>
<p> <code>XResQueryClientResources</code> fills a list of XResType structures, indicating for each resource type allocated by the client its name (as an Atom) and the number of resources of this type allocated. Returns <code>True</code> on success or <code>False</code> on failure. </p>
<p> <code>XResQueryClientPixmapBytes</code> gives, for resources of type <i>PIXMAP</i> the total number of bytes allocated in the X server by the given client. Returns <code>True</code> on success or <code>False</code> on failure.</p>
<h2>Errors</h2>
<p><code>XResQueryClientResources</code> and <code>XResQueryClientPixmapBytes</code> will return <i>BadValue</i> if passed an illegal client identifier.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Author</h2>
<p>Mark Vojkovich, originally for The XFree86 Project Inc.</p>
<h2>Stability</h2>
<p>This API is considered as experimental. The XRes library major revision may be incremented whenever incompatible changes are done to the API without notice. Use with care.</p>
