---
title: "xmuninstallimage(3)"
name: "xmuninstallimage"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmuninstallimage/"
description: "XmUninstallImage — A pixmap caching function that removes an image from the image cache"
---

<p><code>XmUninstallImage</code> &#8212; A pixmap caching function that removes an image from the image cache</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmUninstallImage</code>(
<code>XImage * image</code>);</pre>
<h2>Description</h2>
<p><code>XmUninstallImage</code> removes an image from the image cache.</p>
<dl COMPACT>
<dt><i>image</i></p>
<dd>Points to the image structure given to the XmInstallImage() routine</dl>
<h2>Return</h2>
<p>Returns True when successful; returns False if the <i>image</i> is NULL, or if it cannot be found to be uninstalled.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xminstallimage/">XmInstallImage</a></code>(3), <code><a href="/docs/linux/man/3-xmgetpixmap/">XmGetPixmap</a></code>(3), and <code><a href="/docs/linux/man/3-xmdestroypixmap/">XmDestroyPixmap</a></code>(3).</p>
