---
title: "chcpu(8)"
name: "chcpu"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chcpu/"
description: "chcpu – configure CPUs"
---

<p>chcpu &#8211; configure CPUs</p>
<h2>Synopsis</h2>
<p><code>chcpu</code> <code>-c</code>|<code>-d</code>|<code>-e</code>|<code>-g</code> <i>cpu-list</i> </p>
<p> <code>chcpu</code> <code>-p</code> <i>mode</i> </p>
<p> <code>chcpu</code> <code>-r</code>|<code>-h</code>|<code>-V</code></p>
<h2>Description</h2>
<p><code>chcpu</code> can modify the state of CPUs. It can enable or disable CPUs, scan for new CPUs, change the CPU dispatching <i>mode</i> of the underlying hypervisor, and request CPUs from the hypervisor (configure) or return CPUs to the hypervisor (deconfigure). </p>
<p> Some options have a <i>cpu-list</i> argument. Use this argument to specify a comma-separated list of CPUs. The list can contain individual CPU addresses or ranges of addresses. For example, <code>0,5,7,9-11</code> makes the command applicable to the CPUs with the addresses 0, 5, 7, 9, 10, and 11.</p>
<h2>Options</h2>
<p><code>-c</code>, <code>&#8211;configure</code> <i>cpu-list</i></p>
<dl>
<dd>Configure the specified CPUs. Configuring a CPU means that the hypervisor takes a CPU from the CPU pool and assigns it to the virtual hardware on which your kernel runs.</dl>
<p> <code>-d</code>, <code>&#8211;disable</code> <i>cpu-list</i></p>
<dl>
<dd>Disable the specified CPUs. Disabling a CPU means that the kernel sets it offline.</dl>
<p> <code>-e</code>, <code>&#8211;enable</code> <i>cpu-list</i></p>
<dl>
<dd>Enable the specified CPUs. Enabling a CPU means that the kernel sets it online. A CPU must be configured, see <code>-c</code>, before it can be enabled.</dl>
<p> <code>-g</code>, <code>&#8211;deconfigure</code> <i>cpu-list</i></p>
<dl>
<dd>Deconfigure the specified CPUs. Deconfiguring a CPU means that the hypervisor removes the CPU from the virtual hardware on which the Linux instance runs and returns it to the CPU pool. A CPU must be offline, see <code>-d</code>, before it can be deconfigured.</dl>
<p> <code>-p</code>, <code>&#8211;dispatch</code> <i>mode</i></p>
<dl>
<dd>Set the CPU dispatching <i>mode</i> (polarization). This option has an effect only if your hardware architecture and hypervisor support CPU polarization. Available <i>modes</i> are: </p>
<p> <code>horizontal</code></p>
<dl>
<dd>The workload is spread across all available CPUs.</dl>
<p> <code>vertical</code></p>
<dl>
<dd>The workload is concentrated on few CPUs.</dl>
</dl>
<p> <code>-r</code>, <code>&#8211;rescan</code></p>
<dl>
<dd>Trigger a rescan of CPUs. After a rescan, the Linux kernel recognizes the new CPUs. Use this option on systems that do not automatically detect newly attached CPUs.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Exit Status</h2>
<p><code>chcpu</code> has the following exit status values: </p>
<p> <code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>1</code></p>
<dl>
<dd>failure</dl>
<p> <code>64</code></p>
<dl>
<dd>partial success</dl>
<h2>Authors</h2>
<h2>Copyright</h2>
<p>Copyright IBM Corp. 2011</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lscpu/">lscpu</a></code>(1)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>chcpu</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
