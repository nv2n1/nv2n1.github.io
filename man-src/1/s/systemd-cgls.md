---
title: "systemd-cgls(1)"
name: "systemd-cgls"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-cgls/"
description: "systemd-cgls – Recursively show control group contents"
---

<h2 class="name">NAME</h2>
<p> systemd-cgls &#8211; Recursively show control group contents </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-cgls</code> [OPTIONS&#8230;] [CGROUP&#8230;]</p>
<dt> <code>systemd-cgls</code> [OPTIONS&#8230;] <code>&#8211;unit</code>|<code>&#8211;user-unit</code> [UNIT&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-cgls</code></p>
<dd>recursively shows the contents of the selected Linux control group hierarchy in a tree. If arguments are specified, shows all member processes of the specified control groups plus all their subgroups and their members. The control groups may either be specified by their full file paths or are assumed in the systemd control group hierarchy. If no argument is specified and the current working directory is beneath the control group mount point /sys/fs/cgroup/, shows the contents of the control group the working directory refers to. Otherwise, the full systemd control group hierarchy is shown. </p>
<p> By default, empty control groups are not shown.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Do not hide empty control groups in the output.</dl>
<p> <code>-l</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize process tree members.</dl>
<p> <code>-u</code>, <code>&#8211;unit</code></p>
<dl>
<dt>
<dd> Show cgroup subtrees for the specified units.</dl>
<p> <code>&#8211;user-unit</code></p>
<dl>
<dt>
<dd> Show cgroup subtrees for the specified user units.</dl>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> Include kernel threads in output.</dl>
<p> <code>-M </code><i>MACHINE</i>, <code>&#8211;machine=</code><i>MACHINE</i></p>
<dl>
<dt>
<dd> Limit control groups shown to the part corresponding to the container <i>MACHINE</i>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-systemd-cgtop/">systemd-cgtop</a></code>(1), <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) </p>
<h2>Index</h2>
