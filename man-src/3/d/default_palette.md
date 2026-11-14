---
title: "default_palette(3)"
name: "default_palette"
section: "3"
letter: "d"
url: "/docs/linux/man/3-default_palette/"
description: "default_palette – The default IBM BIOS palette. Allegro game programming library."
---

<h2>NAME</h2>
<p> default_palette &#8211; The default IBM BIOS palette. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern PALETTE default_palette;</code></p>
<h2>DESCRIPTION</h2>
<p> The default IBM BIOS palette. This will be automatically selected whenever you set a new graphics mode. The palette contains 16 basic colors plus many gradients between them. If you want to see the values, you can write a small Allegro program which saves a screenshot with this palette, or open the grabber tool provided with Allegro and create a new palette object, which will use this palette by default. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-black_palette/">black_palette</a></code>(3), <code><a href="/docs/linux/man/3-desktop_palette/">desktop_palette</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3) </p>
<h2>Index</h2>
