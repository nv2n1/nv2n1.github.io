---
title: "update-usbids(8)"
name: "update-usbids"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-usbids/"
description: "update-usbids – download new version of the USB ID list"
---

<p>update-usbids &#8211; download new version of the USB ID list</p>
<h2>Synopsis</h2>
<p><code>update-usbids</code> </p>
<h2>Description</h2>
<p><code>update-usbids</code> fetches the current version of the usb.ids file from the primary distribution site and installs it. This utility requires either wget or lynx to be installed. If gzip or bzip2 are available, it automatically downloads the compressed version of the list. </p>
<h2>Options</h2>
<dl>
<dt><code>-q</code></p>
<dd>Be quiet and do not report anything except errors. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/var/lib/usbutils/usb.ids.gz</code></p>
<dd>Here we install the new list. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lsusb/">lsusb</a>(8).</code> </p>
<h2>Author</h2>
<p>Thomas Sailer, &lt;sailer [at] ife.ee.ethz.ch&gt;.</p>
