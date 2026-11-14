---
title: "sane-kvs40xx(5)"
name: "sane-kvs40xx"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-kvs40xx/"
description: "sane-kvs40xx – SANE backend for Panasonic KV-S40xxC USB/SCSI ADF scanners."
---

<p>sane-kvs40xx &#8211; SANE backend for Panasonic KV-S40xxC USB/SCSI ADF scanners.</p>
<h2>Description</h2>
<p>The <code>sane-kvs40xx</code> library implements a SANE (Scanner Access Now Easy) backend which provides access to the Panasonic KV-S40xxC and KV-S70xxC scanners. </p>
<h2>Known Issues</h2>
<p>This document was written by the SANE project, which has no information regarding the capabilities or reliability of the backend. All information contained here is suspect. </p>
<p> The backend uses pthreads directly, and so requires pthreads to be enabled.</p>
<h2>Credits</h2>
<p>The backend was written by Panasonic Russia Ltd. </p>
<p> The backend was ported to sane-backends 1.0.23 and downgraded to C89 by m. allan noah.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Author</h2>
<p>m. allan noah: &lt;<i>kitno455 a t gmail d o t com</i>&gt;</p>
