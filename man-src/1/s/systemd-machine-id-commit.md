---
title: "systemd-machine-id-commit(1)"
name: "systemd-machine-id-commit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-machine-id-commit/"
description: "systemd-machine-id-commit – Commit transient machine ID to /etc/machine-id"
---

<h2 class="name">NAME</h2>
<p> systemd-machine-id-commit &#8211; Commit transient machine ID to /etc/machine-id </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-machine-id-commit</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-machine-id-commit</code></p>
<dd>may be used to write on disk any transient machine ID mounted as a temporary file system in /etc/machine-id at boot time. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information about this file. </p>
<p> This tool will execute no operation if /etc/machine-id doesn&#8217;t contain any valid machine ID, isn&#8217;t mounted as an independent temporary file system, of /etc is read-only. If those conditions are met, it will then write current machine ID to disk and unmount the transient /etc/machine-id file in a race-free manner to ensure that this file is always valid for other processes. </p>
<p> Note that the traditional way to initialize the machine ID in /etc/machine-id is to use <code>systemd-machine-id-setup</code> by system installer tools. You can also use <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) to initialize the machine ID on mounted (but not booted) system images.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;root=</code><i>root</i></p>
<dl>
<dt>
<dd> Takes a directory path as an argument. All paths will be prefixed with the given alternate <i>root</i> path, including config search paths.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-machine-id-commit-service/">systemd-machine-id-commit.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-machine-id-setup/">systemd-machine-id-setup</a></code>(1), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) </p>
<h2>Index</h2>
