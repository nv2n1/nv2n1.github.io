---
title: "xmdestroypixmap(3)"
name: "xmdestroypixmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdestroypixmap/"
description: "XmDestroyPixmap — A pixmap caching function that removes a pixmap from the pixmap cache"
---

<p><code>XmDestroyPixmap</code> &#8212; A pixmap caching function that removes a pixmap from the pixmap cache</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmDestroyPixmap</code>(
<code>Screen * screen</code>,
<code>Pixmap pixmap</code>);</pre>
<h2>Description</h2>
<p><code>XmDestroyPixmap</code> removes pixmaps that are no longer used. Pixmaps are completely freed only when there is no further reference to them.</p>
<dl COMPACT>
<dt><i>screen</i></p>
<dd>Specifies the display screen for which the pixmap was requested</p>
<dt><i>pixmap</i></p>
<dd>Specifies the pixmap to be destroyed</dl>
<h2>Return</h2>
<p>Returns True when successful; returns False if there is no matching screen and pixmap in the pixmap cache.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xminstallimage/">XmInstallImage</a></code>(3), <code><a href="/docs/linux/man/3-xmuninstallimage/">XmUninstallImage</a></code>(3), and <code><a href="/docs/linux/man/3-xmgetpixmap/">XmGetPixmap</a></code>(3).</p>
