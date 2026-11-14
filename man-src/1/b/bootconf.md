---
title: "bootconf(1)"
name: "bootconf"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bootconf/"
description: "bootconf – bootconf"
---

<h2 class="name">NAME</h2>
<p> bootconf &#8211; bootconf </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bootconf</code> [options&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>bootconf</code></p>
<dd>is a small utility that provides a convenient way to set or inspect some common Linux kernel boot options. <code>bootconf</code> updates the <code>GRUB</code> configuration file (<i>/boot/grub/grub.conf</i> in most cases). The changes will take effect, naturally, at the next reboot. </p>
<p> The following parameters may be specified: </p>
<p> -titles</p>
<dl>
<dt>
<dd> This parameter must be specified by itself, alone. <code>bootconf</code> displays a formatted list of available boot partitions and kernels.</dl>
<p> default=<i>n</i></p>
<dl>
<dt>
<dd> The default boot kernel or partition is lqnrq, where lqnrq is the boot partition number from the list produced by the <i>-titles</i> parameter.</dl>
<p> quiet or quiet=1</p>
<dl>
<dt>
<dd> Suppress most diagnostic messages when the Linux kernel initializes.</dl>
<p> noquiet or quiet=0</p>
<dl>
<dt>
<dd> Display diagnostic messages when the Linux kernel initializes.</dl>
<p> gui or gui=1</p>
<dl>
<dt>
<dd> Show the status of the system boot process graphically (the lqrhgbrq boot option).</dl>
<p> nogui or gui=0</p>
<dl>
<dt>
<dd> Show the status of the system boot process as text.</dl>
<p> vesa=<i>mode</i></p>
<dl>
<dt>
<dd> Use a VESA framebuffer for the system display (see below).</dl>
<p> novesa</p>
<dl>
<dt>
<dd> Do not use the VESA framebuffer for the system display.</dl>
<p> Running <code>bootconf</code> without specifying any parameters displays the current settings. Run <code>bootconf</code> from X to show a small window where the individual settings can be adjusted graphically. </p>
<p> The current settings are parsed from the first kernel listed in GRUB&#8217;s configuration file, but new settings are saved for every configured kernel.</p>
<h3>VESA framebuffer</h3>
<p> Many modern video cards are capable of providing a standard, vendor-independent access mechanism to the display memory. Linux can use this framebuffer for the system console, as opposed to the traditional text display. </p>
<p> The lqvesa=<i>mode</i>rq option configures the Linux kernel to set the video card framebuffer to <i>mode</i>. The possible values for <i>mode</i> are: </p>
<p> 640x480x8 640x480x15 640x480x16 640x480x24 800x600x8 800x600x15 800x600x16 800x600x24 1024x768x8 1024x768x15 1024x768x16 1024x768x24 1280x1024x8 1280x1024x15 1280x1024x16 1280x1024x24 1600x1200x8 1600x1200x15 1600x1200x16 1600x1200x24 </p>
<p> Note </p>
<p> Your video card may not support all of the above video modes. Check your video card&#8217;s documentation. If you select an invalid video mode, the Linux kernel may not be able to boot. When that happens, press E to edit the kernel command line, in GRUB, remove the lqvga=NNNrq parameter, press Enter then B to boot without the framebuffer.</p>
<h2>SEE ALSO</h2>
<p> <i>Framebuffer HOWTO</i>[1] </p>
<p> <i>Latest release of bootconf</i>[2]</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Framebuffer HOWTO</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://tldp.org/HOWTO/Framebuffer-HOWTO.html">http://tldp.org/HOWTO/Framebuffer-HOWTO.html</a></dl>
<dt> 2.</p>
<dd> Latest release of bootconf</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/bootconf/download/">http://www.courier-mta.org/bootconf/download/</a></dl>
</dl>
<h2>Index</h2>
