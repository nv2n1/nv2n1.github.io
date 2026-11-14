---
title: "drmavailable(3)"
name: "drmavailable"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmavailable/"
description: "drmAvailable – determine whether a DRM kernel driver has been loaded"
---

<p>drmAvailable &#8211; determine whether a DRM kernel driver has been loaded </p>
<h2>Synopsis</h2>
<pre>#include &lt;xf86drm.h&gt;</pre>
<dl COMPACT>
<dt> <code>int drmAvailable(void);</code></dl>
<h2>Description</h2>
<p><code>drmAvailable</code></p>
<dd>allows the caller to determine whether a kernel DRM driver is loaded.</p>
<h2>Return Value</h2>
<p><code>drmAvailable</code> returns 1 if a DRM driver is currently loaded. Otherwise 0 is returned.</p>
<h2>Reporting Bugs</h2>
<p>Bugs in this function should be reported to <a rel="nofollow" href="http://bugs.freedesktop.org">http://bugs.freedesktop.org</a> under the &quot;Mesa&quot; product, with &quot;Other&quot; or &quot;libdrm&quot; as the component.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-drm/">drm</a></code>(7), <code><a href="/docs/linux/man/3-drmopen/">drmOpen</a></code>(3)</p>
