---
title: "initng(8)"
name: "initng"
section: "8"
letter: "i"
url: "/docs/linux/man/8-initng/"
description: "initng – a full replacement of the old and in many ways depricated sysvinit"
---

<p>initng &#8211; a full replacement of the old and in many ways depricated sysvinit</p>
<h2>Synopsis</h2>
<p><code>initng</code></p>
<h2>Description</h2>
<p><code>Initng</code> is a full replacement of the old and in many ways deprecated sysvinit tool. It is designed with speed in mind, doing as much as possible asynchronously. In other words: It will boot your unix-system much faster, and give you more control and statistics over your system. </p>
<p> The basic premise is that startup commands can be launched as soon as their dependencies are met. This limits the effect of bottlenecks like I/O operations; while one program is performing I/O, another can be utilizing the processor. Initng tracks the individual service dependencies in its configuration files. </p>
<p> It is designed to use a minimum of system resources and to boot your system quickly and safely. </p>
<p> <i>lilo</i> users need to add the line &#8216;<i>append=&quot;init=/sbin/initng&quot;</i>&#8216; in their <i>/etc/lilo.conf</i>, <i>grub</i> users can just append &#8216;<i>init=/sbin/initng</i>&#8216; to their &quot;kernel image options&quot; line in <i>/boot/grub/menu.lst</i>.</p>
<h2>Options</h2>
<p>Initng is the first process the kernel starts. It has no parameters. It will start the services defined in /etc/initng.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ngc/">ngc</a>(8),</code> <code><a href="/docs/linux/man/8-ngdc/">ngdc</a>(8),</code> <code><a href="/docs/linux/man/8-ng-update/">ng-update</a>(8),</code> <code><a href="/docs/linux/man/8-gen_system_runlevel/">gen_system_runlevel</a>(8),</code> <code><a href="/docs/linux/man/8-install_service/">install_service</a>(8),</code> <code><a href="/docs/linux/man/8-system_off/">system_off</a>(8).</code></p>
<h2>Author</h2>
<p>initng was written by Jimmy Wennlund &lt;jimmy.wennlund [at] gmail.com&gt; and can be found at <a rel="nofollow" href="http://www.initng.org/.">http://www.initng.org/.</a> </p>
<p> This manual page was written by Armin Berres &lt;a.berres [at] web.de&gt; based on the readme file written by Patrick Boehnke.</p>
