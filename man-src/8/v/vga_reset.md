---
title: "vga_reset(8)"
name: "vga_reset"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vga_reset/"
description: "vga_reset – reset video graphic board"
---

<p>vga_reset &#8211; reset video graphic board</p>
<h2>Synopsis</h2>
<p><code>vga_reset</code></p>
<h2>Description</h2>
<p>Call real mode c000:0003, which should be the video card&#8217;s initialization routine. Should work in some cases when mode3 fails to restore text mode.</p>
<h2>Bugs</h2>
<p>Using this program is unsafe, and might (depending on the bios) result in a video card in a state that requires a hard reset to restore to normal, or even a hung computer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mode3/">mode3</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Guillem Jover &lt;guillem [at] debian.org&gt;.</p>
