---
title: "drmhandleevent(3)"
name: "drmhandleevent"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmhandleevent/"
description: "drmHandleEvent – read and process pending DRM events"
---

<p>drmHandleEvent &#8211; read and process pending DRM events </p>
<h2>Synopsis</h2>
<pre>#include &lt;xf86drm.h&gt;</pre>
<dl COMPACT>
<dt> <code>int drmHandleEvent(int&nbsp;<wbr></code><i>fd</i><code>, drmEventContextPtr&nbsp;<wbr></code><i>evctx</i><code>);</code></dl>
<h2>Description</h2>
<p><code>drmHandleEvent</code></p>
<dd>processes outstanding DRM events on the DRM file-descriptor passed as <i>fd</i>. This function should be called after the DRM file-descriptor has polled readable; it will read the events and use the passed-in <i>evctx</i> structure to call function pointers with the parameters noted below: </p>
<dl COMPACT>
<dd>
<pre>typedef struct _drmEventContext {
 int version;
 void (*vblank_handler) (int fd,
 unsigned int sequence,
 unsigned int tv_sec,
 unsigned int tv_usec,
 void *user_data)
 void (*page_flip_handler) (int fd,
 unsigned int sequence,
 unsigned int tv_sec,
 unsigned int tv_usec,
 void *user_data)
} drmEventContext, *drmEventContextPtr;</pre>
</dl>
<h2>Return Value</h2>
<p><code>drmHandleEvent</code> returns 0 on success, or if there is no data to read from the file-descriptor. Returns -1 if the read on the file-descriptor fails or returns less than a full event record.</p>
<h2>Reporting Bugs</h2>
<p>Bugs in this function should be reported to <a rel="nofollow" href="http://bugs.freedesktop.org">http://bugs.freedesktop.org</a> under the &quot;Mesa&quot; product, with &quot;Other&quot; or &quot;libdrm&quot; as the component.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-drm/">drm</a></code>(7), <code><a href="/docs/linux/man/7-drm-kms/">drm-kms</a></code>(7), <code><a href="/docs/linux/man/3-drmmodepageflip/">drmModePageFlip</a></code>(3), <code><a href="/docs/linux/man/3-drmwaitvblank/">drmWaitVBlank</a></code>(3)</p>
