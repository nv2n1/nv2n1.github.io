---
title: "irdadump(8)"
name: "irdadump"
section: "8"
letter: "i"
url: "/docs/linux/man/8-irdadump/"
description: "irdadump – monitors the IrDA traffic on one or more links."
---

<p>irdadump &#8211; monitors the IrDA traffic on one or more links.</p>
<h2>Synopsis</h2>
<p><code>irdadump</code> [ <i>-b</i> ] [ <i>-c n</i> ] [ <i>-d</i> ] [ <i>-x</i> ] [ <i>-s n</i> ] [ <i>-t</i> ] [ <i>-l</i> ] [ <i>-v</i> ] [ <i>-i device</i> ] </p>
<h2>Options</h2>
<p><code>-b</code> dump bytes in columns </p>
<p> <code>-c n</code> set snapcols for byte printing with -b option </p>
<p> <code>-d</code> prints the time difference between the current and the previous frame </p>
<p> <code>-x</code> dump frame (bytes and ascii) </p>
<p> <code>-s n</code> set snaplen for -b and -x option </p>
<p> <code>-t</code> force TTP decoding of unknown connections </p>
<p> <code>-l</code> set line buffering on output file </p>
<p> <code>-v</code> verbose </p>
<p> <code>-i device</code> interface</p>
<h2>Description</h2>
<p><code>irdadump</code> is a tool for monitoring the IrDA traffic on one or more links. Just write &quot;make&quot; to compile the program. When you run the program, you should be able to see the IrDA traffic (if any). </p>
<p> One advantage of implementing IrDA device drivers as network device drivers is that you should be able to attach sniffers to the device (or actually the packet type). That way, it is possible to use a really handy utility called <code>irdadump</code> (instead of <code>tcpdump</code>). This will make debugging MUCH easier. Linux-2.2 implements the BPF (Berkeley Packet Filter), so its possible to filter out exactly the frames you want to see. You may use <code>hostname</code> to separate different machines names. Or <code>grep</code> to filter the output, too. </p>
<p> <code>irdadump</code> must be run as root or installed setuid root, as it requires root privileges.</p>
<h2>Examples</h2>
<p>The output should look something like this: </p>
<pre>/ # ./irdadump 
20:11:45.412199 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=0
20:11:45.492137 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=1
20:11:45.572137 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=2
20:11:45.652208 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=3
20:11:45.732137 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=4
20:11:45.812137 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=5
20:11:45.892175 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=255 Linux
20:11:45.902362 xid:rsp 0xf7be8388 &lt; 0x0015c23b S=6 s=5 ACTiSYS IR100M
20:11:48.412197 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=0
20:11:48.492656 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=1
20:11:48.572177 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=2
20:11:48.652169 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=3
20:11:48.732177 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=4
20:11:48.812153 xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=5
20:11:48.822371 xid:rsp 0xf7be8388 &lt; 0x0015c23b S=6 s=4 ACTiSYS IR100M
15 packets received by filter</pre>
<p>Turning on the &quot;-d&quot; option will make irdadump print the time difference between the current and the previous frame: </p>
<pre>/ # ./irdadump -d
20:11:18.412475 (0982.06 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=0
20:11:18.492345 (0079.87 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=1
20:11:18.572376 (0080.03 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=2
20:11:18.652979 (0080.60 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=3
20:11:18.732354 (0079.38 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=4
20:11:18.755093 (0022.74 ms) xid:rsp 0xf7be8388 &lt; 0x0015c23b S=6 s=3 ACTiSYS IR100M
20:11:18.812350 (0057.26 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=5
20:11:18.892518 (0080.17 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=255 Linux
20:11:21.412486 (2519.97 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=0
20:11:21.492395 (0079.91 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=1
20:11:21.572368 (0079.97 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=2
20:11:21.652405 (0080.04 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=3
20:11:21.732458 (0080.05 ms) xid:cmd 0x0015c23b &gt; 0xffffffff S=6 s=4</pre>
<p><code>irdadump</code> must be run as root or installed setuid root, as it requires root privileges. </p>
<p> <code>irdadump -d -x -s 256</code> will check the contents of the frames. This should tell us if the frames have malformed content, or if the irda stack is doing something wrong.</p>
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
