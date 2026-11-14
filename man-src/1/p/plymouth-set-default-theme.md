---
title: "plymouth-set-default-theme(1)"
name: "plymouth-set-default-theme"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plymouth-set-default-theme/"
description: "plymouth-set-default-theme – Set the plymouth theme"
---

<h2 class="name">NAME</h2>
<p> plymouth-set-default-theme &#8211; Set the plymouth theme </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>plymouth-set-default-theme </code><code>[OPTION&#8230;]</code><code>[THEME]</code></dl>
<h2>DESCRIPTION</h2>
<dd>When called with a <code>THEME</code> argument, the <code>plymouth-set-default-theme</code> command changes the preferred boot theme and also performs the necessary regeneration of the initial ramdisk (initrd) since plymouth is loaded from the boot loader from the initrd prior to the mounting of the root filesystem. </p>
<p> If <code>plymouth-set-default-theme</code> is invoked with no options or parameters, it shows the currently selected theme by default. This output is used by the helper scripts plymouth-generate-initrd and plymouth-update-initrd to set the proper theme in the initial ramdisk.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List available themes.</dl>
<p> <code>-r</code>, <code>&#8211;reset</code></p>
<dl>
<dt>
<dd> Reset to default theme.</dl>
<p> <code>-R</code>, <code>&#8211;rebuild-initrd</code></p>
<dl>
<dt>
<dd> Rebuild initrd (necessary after changing theme).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-grub/">grub</a></code>(8), <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8), <code><a href="/docs/linux/man/8-plymouthd/">plymouthd</a></code>(8), <code><a href="/docs/linux/man/1-plymouth/">plymouth</a></code>(1), m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/Plymouth">http://www.freedesktop.org/wiki/Software/Plymouth</a></code>m[] </p>
<h2>Index</h2>
