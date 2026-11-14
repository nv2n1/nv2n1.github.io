---
title: "xorg-x11-fonts-update-dirs(1)"
name: "xorg-x11-fonts-update-dirs"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xorg-x11-fonts-update-dirs/"
description: "xorg-x11-fonts-update-dirs – update X11 font directories"
---

<h2>NAME</h2>
<p> xorg-x11-fonts-update-dirs &#8211; update X11 font directories</p>
<h2>SYNOPSIS</h2>
<p> <code>xorg-x11-fonts-update-dirs [&#8211;skip-fontscale] [&#8211;need-ttmkfdir] path</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>xorg-x11-fonts-*</code> rpm packages call <i>xorg-x11-fonts-update-dirs</i> during %post and %postun to update the X11 font indices. This script may change in incompatible ways without notice and you should not run this script manually or rely on it otherwise. To manually update the font indices invoke <code>mkfontscale</code> and <code>ttmkfdir </code> directly as required. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mkfontscale/">mkfontscale</a>(1) <a href="/docs/linux/man/1-ttmkfdir/">ttmkfdir</a>(1) </p>
<h2>Index</h2>
