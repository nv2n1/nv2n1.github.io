---
title: "setsysfont(8)"
name: "setsysfont"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setsysfont/"
description: "setsysfont – set console font according to /etc/sysconfig/i18n."
---

<p>setsysfont &#8211; set console font according to /etc/sysconfig/i18n.</p>
<h2>Synopsis</h2>
<p><code>setsysfont</code></p>
<h2>Description</h2>
<p><code>setsysfont</code> sets the console font for current virtual terminal. The font setting is read from /etc/sysconfig/i18n.</p>
<h2>Notes</h2>
<p><code>setsysfont</code> should not need to be called in normal practice, as the font is set on boot. </p>
<h2>Files</h2>
<dl>
<dt><code>/etc/sysconfig/i18n</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code>/usr/share/doc/initscripts-*/sysconfig.txt,</code> <code><a href="/docs/linux/man/1-unicode_start/">unicode_start</a></code>(1), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/1-consoletype/">consoletype</a></code>(1) </p>
