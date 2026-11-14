---
title: "virt-manager(1)"
name: "virt-manager"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-manager/"
description: "virt-manager – display the virtual machine desktop management tool"
---

<h2 class="name">NAME</h2>
<p> virt-manager &#8211; display the virtual machine desktop management tool </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-manager</code> [<font SIZE="-1">OPTIONS</font>]</p>
<h2>DESCRIPTION</h2>
<p> <code>virt-manager</code> is a desktop tool for managing virtual machines. It provides the ability to control the lifecycle of existing machines (bootup/shutdown,pause/resume,suspend/restore), provision new virtual machines and various types of store, manage virtual networks, access the graphical console of virtual machines, and view performance statistics, all done locally or remotely.</p>
<h2>OPTIONS</h2>
<p> The following options are accepted when running <tt>&quot;virt-manager&quot;</tt>:</p>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Display command line help summary</p>
<dt><code>&#8211;version</code></p>
<dd> Show virt-manager&#8217;s version number and exit</p>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code>=URI</p>
<dd> Specify the hypervisor connection <tt>&quot;URI&quot;</tt></p>
<dt><code>&#8211;debug</code></p>
<dd> List debugging output to the console (normally this is only logged in ~/.cache/virt-manager/virt-manager.log). This function implies &#8211;no-fork.</p>
<dt><code>&#8211;no-fork</code></p>
<dd> Don&#8217;t fork <tt>&quot;virt-manager&quot;</tt> off into the background: run it blocking the current terminal. Useful for seeing possible errors dumped to stdout/stderr.</p>
<dt><code>&#8211;no-conn-autostart</code></p>
<dd> Don&#8217;t autostart any libvirt connections when launching <tt>&quot;virt-manager&quot;</tt>.</p>
<dt><code>&#8211;show-DIALOG-WINDOW</code></p>
<dd> Display the corresponding <tt>&quot;DIALOG-WINDOW&quot;</tt> when launching <tt>&quot;virt-manager&quot;</tt>. This function implies &#8211;no-conn-autostart and the manager window will not be shown at startup in this case. </p>
<p> The following <tt>&quot;DIALOG-WINDOW&quot;</tt> options are currently available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;show-domain-creator</code></p>
<dd> Display the wizard for creating new virtual machines</p>
<dt><code>&#8211;show-domain-editor</code> NAME|ID|UUID</p>
<dd> Display the dialog for editing properties of the virtual machine with unique <font SIZE="-1">ID</font> matching either the domain name, <font SIZE="-1">ID,</font> or <font SIZE="-1">UUID</font></p>
<dt><code>&#8211;show-domain-performance</code> NAME|ID|UUID</p>
<dd> Display the dialog for monitoring performance of the virtual machine with unique <font SIZE="-1">ID</font> matching either the domain name, <font SIZE="-1">ID,</font> or <font SIZE="-1">UUID</font></p>
<dt><code>&#8211;show-domain-console</code> NAME|ID|UUID</p>
<dd> Display the virtual console of the virtual machine with unique <font SIZE="-1">ID</font> matching either the domain name, <font SIZE="-1">ID,</font> or <font SIZE="-1">UUID</font></p>
<dt><code>&#8211;show-host-summary</code></p>
<dd> Display the main window summarizing performance for all virtual machines on the host.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;spice-disable-auto-usbredir</code></p>
<dd> Auto <font SIZE="-1">USB</font> redirection is supported by default. This option switches off it.</dl>
<p> Standard <font SIZE="-1">GTK</font> options like &#8211;g-fatal-warnings are also accepted.</p>
<h2>BUGS</h2>
<p> Please see &lt;<a rel="nofollow" href="http://virt-manager.org/bugs/">http://virt-manager.org/bugs/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) Red Hat, Inc, and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-virsh/">virsh</a>(1)</tt>, <tt>&quot;<a href="/docs/linux/man/1-virt-viewer/">virt-viewer</a>(1)&quot;</tt>, the project website <tt>&quot;<a rel="nofollow" href="http://virt-manager.org">http://virt-manager.org</a>&quot;</tt> </p>
<h2>Index</h2>
