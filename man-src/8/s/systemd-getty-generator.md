---
title: "systemd-getty-generator(8)"
name: "systemd-getty-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-getty-generator/"
description: "systemd-getty-generator – Generator for enabling getty instances on the console"
---

<p>systemd-getty-generator &#8211; Generator for enabling getty instances on the console</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-getty-generator</p>
<h2>Description</h2>
<p>systemd-getty-generator is a generator that automatically instantiates serial-getty [at] .service on the kernel console(s), if they can function as ttys and are not provided by the virtual console subsystem. It will also instantiate serial-getty [at] .service instances for virtualizer consoles, if execution in a virtualized environment is detected. If execution in a container environment is detected, it will instead enable console-getty.service for /dev/console, and container-getty [at] .service instances for additional container pseudo TTYs as requested by the container manager (see m[blue]<code>Container Interface</code>m[]<font SIZE="-2">[1]</font>). This should ensure that the user is shown a login prompt at the right place, regardless of which environment the system is started in. For example, it is sufficient to redirect the kernel console with a kernel command line argument such as <i>console=</i> to get both kernel messages and a getty prompt on a serial TTY. See m[blue]<code>kernel-parameters.txt</code>m[]<font SIZE="-2">[2]</font> for more information on the <i>console=</i> kernel parameter. </p>
<p> systemd-getty-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7). </p>
<p> Further information about configuration of gettys can be found in m[blue]<code>systemd for Administrators, Part XVI: Gettys on Serial Consoles (and Elsewhere)</code>m[]<font SIZE="-2">[3]</font>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Container<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Interface</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/CONTAINER_INTERFACE">https://systemd.io/CONTAINER_INTERFACE</a></dl>
<dt> 2.</p>
<dd>kernel-parameters.txt</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/admin-guide/kernel-parameters.txt">https://www.kernel.org/doc/Documentation/admin-guide/kernel-parameters.txt</a></dl>
<dt> 3.</p>
<dd>systemd for Administrators, Part XVI: Gettys on Serial Consoles (and Elsewhere)</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/serial-console.html">http://0pointer.de/blog/projects/serial-console.html</a></dl>
