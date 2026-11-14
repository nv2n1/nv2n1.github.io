---
title: "retrace-server-interact(1)"
name: "retrace-server-interact"
section: "1"
letter: "r"
url: "/docs/linux/man/1-retrace-server-interact/"
description: "retrace-server-interact – use Retrace server’s chroot for interactive debugging."
---

<h2 class="name">NAME</h2>
<p> retrace-server-interact &#8211; use Retrace server&#8217;s chroot for interactive debugging. </p>
<h2>SYNOPSIS</h2>
<p> <i>retrace-server-interact</i> [-h] [&#8211;priv] task_id action</p>
<h2>DESCRIPTION</h2>
<p> The tool makes Retrace server&#8217;s chroot available for interactive debugging. It enables user to jump into the chroot and execute the correct tool (gdb/crash), automatically loading all relevant files.</p>
<h2>ACTIONS</h2>
<p> shell</p>
<dl>
<dt>
<dd> Jump to a shell. Not available if mock chroot is not used. This is the case of vmcores from the same architecture as host system.</dl>
<p> gdb</p>
<dl>
<dt>
<dd> Run GDB, load executable and coredump and jump to prompt. Only available for binary crashes (coredumps).</dl>
<p> crash</p>
<dl>
<dt>
<dd> Run Crash, load vmcore and vmlinux and jump to prompt. Only available for kernel crashes (vmcores).</dl>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
<dd> Display help and exit.</dl>
<p> &#8211;priv</p>
<dl>
<dt>
<dd> Use the chroot as privileged user.</dl>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> &bull; Michal Toman &lt;m[blue]<code>_mtoman [at] redhat.com_</code>m[]<font SIZE="-2">[1]</font>&gt;</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> _mtoman [at] redhat.com_</p>
<dl>
<dt>
<dd> mailto:_mtoman [at] redhat.com_</dl>
</dl>
<h2>Index</h2>
