---
title: "irdaping(8)"
name: "irdaping"
section: "8"
letter: "i"
url: "/docs/linux/man/8-irdaping/"
description: "irdaping – sends IrDA test frames"
---

<p>irdaping &#8211; sends IrDA test frames</p>
<h2>Synopsis</h2>
<p><code>irdaping</code> [ <i>daddr</i> ] [ <i>-s framesize</i> ] </p>
<h2>Options</h2>
<p><code>daddr</code> &#8230; </p>
<p> <code>-s framesize</code> &#8230;</p>
<h2>Description</h2>
<p>This is a program similar to <code><a href="/docs/linux/man/8-ping/">ping</a>(8)</code>. It sends IrDA test frames (added some userdata which contains the frame number and the time the frame was sent). You can change the size of the frame by using the <code>-s</code> option. To get <code>daddr</code> you may use <code>irdadump</code>. </p>
<p> <code>irdaping</code> must be run as root or installed setuid root, as it requires root privileges.</p>
<h2>Examples</h2>
<p><code>irdaping &lt;daddr&gt; [-s &lt;framesize&gt;]</code> </p>
<p> You may use an <code>alias</code>, which does not use any parameter <code>alias irping=&quot;irdaping \`grep daddr /proc/net/irda/discovery|sed s/.*<a href="daddr://\`">daddr://\`</a>&quot;</code> It works fine when there is only one discovered client.</p>
<h2>Diagnostics</h2>
<p>N.N.</p>
<h2>Bugs</h2>
<p>N.N.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-irattach/">irattach</a>(8), <a href="/docs/linux/man/8-irdaping/">irdaping</a>(8), <a href="/docs/linux/man/8-irdadump/">irdadump</a>(8), <a href="/docs/linux/man/8-findchip/">findchip</a>(8), <a href="/docs/linux/man/8-irpsion5/">irpsion5</a>(8), <a href="/docs/linux/man/8-modprobe/">modprobe</a>(8) </p>
<p> Linux/IrDA Project <a rel="nofollow" href="http://irda.sourceforge.net">http://irda.sourceforge.net</a> -*- Linux/IrDA-Tutorial <a rel="nofollow" href="http://www.hpl.hp.com/personal/Jean_Tourrilhes/IrDA/index.html">http://www.hpl.hp.com/personal/Jean_Tourrilhes/IrDA/index.html</a> -*- Infrared-HOWTO <a rel="nofollow" href="http://tuxmobil.org/howtos.html">http://tuxmobil.org/howtos.html</a></p>
<h2>Author</h2>
<p>This manual page is written by Werner Heuser &lt;wehe [at] tuxmobil.org&gt;. It is based on the READMEs from <code>irda-utils</code> by the Linux/IrDA Project and the Linux/IrDA-Tutorial.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2001 Werner Heuser </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License (GFDL), Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
