---
title: "irpsion5(8)"
name: "irpsion5"
section: "8"
letter: "i"
url: "/docs/linux/man/8-irpsion5/"
description: "irpsion5 – IrDA connectivity to a Psion V PDA"
---

<p>irpsion5 &#8211; IrDA connectivity to a Psion V PDA</p>
<h2>Synopsis</h2>
<p><code>irpsion5</code> [ <i>-s file</i> ] [ <i>-r</i> ] [ <i>-b</i> ] [ <i>-v</i> ] [ <i>-q</i> ] [ <i>-S ms</i> ] [ <i>-D n</i> ] </p>
<h2>Options</h2>
<p><code>-s file</code> send file to the Psion </p>
<p> <code>-r</code> receive a file from the Psion </p>
<p> <code>-b</code> receive multiple files (batch mode) </p>
<p> <code>-v</code> verbose mode, progress indication </p>
<p> <code>-q</code> quiet mode, no progress indication </p>
<p> <code>-S ms</code> set discovery slot timeout, standard 80ms, default 120ms </p>
<p> <code>-D n</code> debug level</p>
<h2>Description</h2>
<p>N.N. </p>
<p> <code>irpsion5</code> must be run as root or installed setuid root, as it requires root privileges.</p>
<h2>Examples</h2>
<p>N.N.</p>
<h2>Diagnostics</h2>
<p>Error: unknown switch %s </p>
<p> Call without args for usage: %s</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-irattach/">irattach</a>(8), <a href="/docs/linux/man/8-irdaping/">irdaping</a>(8), <a href="/docs/linux/man/8-irdadump/">irdadump</a>(8), <a href="/docs/linux/man/8-findchip/">findchip</a>(8), <a href="/docs/linux/man/8-irpsion5/">irpsion5</a>(8), <a href="/docs/linux/man/8-modprobe/">modprobe</a>(8) </p>
<p> Linux/IrDA Project <a rel="nofollow" href="http://irda.sourceforge.net">http://irda.sourceforge.net</a> -*- Linux/IrDA-Tutorial <a rel="nofollow" href="http://www.hpl.hp.com/personal/Jean_Tourrilhes/IrDA/index.html">http://www.hpl.hp.com/personal/Jean_Tourrilhes/IrDA/index.html</a> -*- Infrared-HOWTO <a rel="nofollow" href="http://tuxmobil.org/howtos.html">http://tuxmobil.org/howtos.html</a></p>
<h2>Author</h2>
<p>This manual page is written by Werner Heuser &lt;wehe [at] tuxmobil.org&gt;. It is based on the READMEs from <code>irda-utils</code> by the Linux/IrDA Project and the Linux/IrDA-Tutorial.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2001 Werner Heuser </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License (GFDL), Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
