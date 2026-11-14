---
title: "lsinitrd(1)"
name: "lsinitrd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsinitrd/"
description: "lsinitrd – tool to show the contents of an initramfs image"
---

<h2 class="name">NAME</h2>
<p> lsinitrd &#8211; tool to show the contents of an initramfs image </p>
<h2>SYNOPSIS</h2>
<p> <code>lsinitrd</code> [<i>OPTION&#8230;</i>] [&lt;image&gt; [&lt;filename&gt; [&lt;filename&gt; [&#8230;] ]]] </p>
<p> <code>lsinitrd</code> [<i>OPTION&#8230;</i>] -k &lt;kernel-version&gt;</p>
<h2>DESCRIPTION</h2>
<p> lsinitrd shows the contents of an initramfs image. if &lt;image&gt; is omitted, then lsinitrd uses the default image <i>/boot/&lt;machine-id&gt;/&lt;kernel-version&gt;/initrd</i> or <i>/boot/initramfs-&lt;kernel-version&gt;.img</i>.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> print a help message and exit.</dl>
<p> <code>-s, &#8211;size</code></p>
<dl>
<dt>
<dd> sort the contents of the initramfs by size.</dl>
<p> <code>-f, &#8211;file</code>&nbsp;<wbr><i>&lt;filename&gt;</i></p>
<dl>
<dt>
<dd> print the contents of &lt;filename&gt;.</dl>
<p> <code>-k, &#8211;kver</code>&nbsp;<wbr><i>&lt;kernel version&gt;</i></p>
<dl>
<dt>
<dd> inspect the initramfs of &lt;kernel version&gt;.</dl>
<h2>AVAILABILITY</h2>
<p> The lsinitrd command is part of the dracut package and is available from m[blue]<code><a rel="nofollow" href="https://dracut.wiki.kernel.org">https://dracut.wiki.kernel.org</a></code>m[]</p>
<h2>AUTHORS</h2>
<p> Harald Hoyer </p>
<p> Amerigo Wang </p>
<p> Nikoli</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>
<h2>Index</h2>
