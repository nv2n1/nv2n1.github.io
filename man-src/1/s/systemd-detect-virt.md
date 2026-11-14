---
title: "systemd-detect-virt(1)"
name: "systemd-detect-virt"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-detect-virt/"
description: "systemd-detect-virt – Detect execution in a virtualized environment"
---

<h2 class="name">NAME</h2>
<p> systemd-detect-virt &#8211; Detect execution in a virtualized environment </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-detect-virt</code> [OPTIONS&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-detect-virt</code></p>
<dd>detects execution in a virtualized environment. It identifies the virtualization technology and can distinguish full machine virtualization from container virtualization. systemd-detect-virt exits with a return value of 0 (success) if a virtualization technology is detected, and non-zero (error) otherwise. By default, any type of virtualization is detected, and the options <code>&#8211;container</code> and <code>&#8211;vm</code> can be used to limit what types of virtualization are detected. </p>
<p> When executed without <code>&#8211;quiet</code> will print a short identifier for the detected virtualization technology. The following technologies are currently identified: </p>
<p> <code>Table 1. Known virtualization technologies (both VM, i.e. full hardware virtualization, and container, i.e. shared kernel virtualization)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Type </code></td>
<td><code> ID </code></td>
<td><code> Product </code>
</td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2> VM </td>
<td> <i>qemu</i> </td>
<td> QEMU software virtualization, without KVM
</td>
</tr>
<tr VALIGN=top>
<td> <i>kvm</i> </td>
<td> Linux KVM kernel virtual machine, in combination with QEMU. Not used for other virtualizers using the KVM interfaces, such as Oracle VirtualBox or Amazon EC2 Nitro, see below. </td>
</tr>
<tr VALIGN=top>
<td> <i>amazon</i> </td>
<td> Amazon EC2 Nitro using Linux KVM </td>
</tr>
<tr VALIGN=top>
<td> <i>zvm</i> </td>
<td> s390 z/VM </td>
</tr>
<tr VALIGN=top>
<td> <i>vmware</i> </td>
<td> VMware Workstation or Server, and related products </td>
</tr>
<tr VALIGN=top>
<td> <i>microsoft</i> </td>
<td> Hyper-V, also known as Viridian or Windows Server Virtualization </td>
</tr>
<tr VALIGN=top>
<td> <i>oracle</i> </td>
<td> Oracle VM VirtualBox (historically marketed by innotek and Sun Microsystems), for legacy and KVM hypervisor </td>
</tr>
<tr VALIGN=top>
<td> <i>powervm</i> </td>
<td> IBM PowerVM hypervisor &#8212; comes as firmware with some IBM POWER servers </td>
</tr>
<tr VALIGN=top>
<td> <i>xen</i> </td>
<td> Xen hypervisor (only domU, not dom0) </td>
</tr>
<tr VALIGN=top>
<td> <i>bochs</i> </td>
<td> Bochs Emulator </td>
</tr>
<tr VALIGN=top>
<td> <i>uml</i> </td>
<td> User-mode Linux </td>
</tr>
<tr VALIGN=top>
<td> <i>parallels</i> </td>
<td> Parallels Desktop, Parallels Server </td>
</tr>
<tr VALIGN=top>
<td> <i>bhyve</i> </td>
<td> bhyve, FreeBSD hypervisor </td>
</tr>
<tr VALIGN=top>
<td> <i>qnx</i> </td>
<td> QNX hypervisor </td>
</tr>
<tr VALIGN=top>
<td> <i>acrn</i> </td>
<td> m[blue]<code>ACRN hypervisor</code>m[]<font SIZE="-2">[1]</font> </td>
<td> &nbsp;
</td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2> Container </td>
<td> <i>openvz</i> </td>
<td> OpenVZ/Virtuozzo
</td>
</tr>
<tr VALIGN=top>
<td> <i>lxc</i> </td>
<td> Linux container implementation by LXC </td>
</tr>
<tr VALIGN=top>
<td> <i>lxc-libvirt</i> </td>
<td> Linux container implementation by libvirt </td>
</tr>
<tr VALIGN=top>
<td> <i>systemd-nspawn</i> </td>
<td> systemd&#8217;s minimal container implementation, see <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) </td>
</tr>
<tr VALIGN=top>
<td> <i>docker</i> </td>
<td> Docker container manager </td>
</tr>
<tr VALIGN=top>
<td> <i>podman</i> </td>
<td> m[blue]<code>Podman</code>m[]<font SIZE="-2">[2]</font> container manager </td>
</tr>
<tr VALIGN=top>
<td> <i>rkt</i> </td>
<td> rkt app container runtime </td>
</tr>
<tr VALIGN=top>
<td> <i>wsl</i> </td>
<td> m[blue]<code>Windows Subsystem for Linux</code>m[]<font SIZE="-2">[3]</font> </td>
</tr>
<tr VALIGN=top>
<td> <i>proot</i> </td>
<td> m[blue]<code>proot</code>m[]<font SIZE="-2">[4]</font> userspace chroot/bind mount emulation </td>
</tr>
<tr VALIGN=top>
<td> <i>pouch</i> </td>
<td> m[blue]<code>Pouch</code>m[]<font SIZE="-2">[5]</font> Container Engine </td>
</tr>
</table>
<p> If multiple virtualization solutions are used, only the &quot;innermost&quot; is detected and identified. That means if both machine and container virtualization are used in conjunction, only the latter will be identified (unless <code>&#8211;vm</code> is passed). </p>
<p> Windows Subsystem for Linux is not a Linux container, but an environment for running Linux userspace applications on top of the Windows kernel using a Linux-compatible interface. WSL is categorized as a container for practical purposes. Multiple WSL environments share the same kernel and services should generally behave like when being run in a container.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-c</code>, <code>&#8211;container</code></p>
<dl>
<dt>
<dd> Only detects container virtualization (i.e. shared kernel virtualization).</dl>
<p> <code>-v</code>, <code>&#8211;vm</code></p>
<dl>
<dt>
<dd> Only detects hardware virtualization.</dl>
<p> <code>-r</code>, <code>&#8211;chroot</code></p>
<dl>
<dt>
<dd> Detect whether invoked in a <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) environment. In this mode, no output is written, but the return value indicates whether the process was invoked in a <code>chroot()</code> environment or not.</dl>
<p> <code>&#8211;private-users</code></p>
<dl>
<dt>
<dd> Detect whether invoked in a user namespace. In this mode, no output is written, but the return value indicates whether the process was invoked inside of a user namespace or not. See <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7) for more information.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Suppress output of the virtualization technology identifier.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Output all currently known and detectable container and VM environments.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> If a virtualization technology is detected, 0 is returned, a non-zero code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1), <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> ACRN hypervisor</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://projectacrn.org">https://projectacrn.org</a></dl>
<dt> 2.</p>
<dd> Podman</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://podman.io">https://podman.io</a></dl>
<dt> 3.</p>
<dd> Windows Subsystem for Linux</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://docs.microsoft.com/en-us/windows/wsl/about">https://docs.microsoft.com/en-us/windows/wsl/about</a></dl>
<dt> 4.</p>
<dd> proot</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://proot-me.github.io/">https://proot-me.github.io/</a></dl>
<dt> 5.</p>
<dd> Pouch</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/alibaba/pouch">https://github.com/alibaba/pouch</a></dl>
</dl>
<h2>Index</h2>
