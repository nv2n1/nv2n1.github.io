---
title: "systemd-machine-id-setup(1)"
name: "systemd-machine-id-setup"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-machine-id-setup/"
description: "systemd-machine-id-setup – Initialize the machine ID in /etc/machine-id"
---

<h2 class="name">NAME</h2>
<p> systemd-machine-id-setup &#8211; Initialize the machine ID in /etc/machine-id </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-machine-id-setup</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-machine-id-setup</code></p>
<dd>may be used by system installer tools to initialize the machine ID stored in /etc/machine-id at install time, with a provisioned or randomly generated ID. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information about this file. </p>
<p> If the tool is invoked without the <code>&#8211;commit</code> switch, /etc/machine-id is initialized with a valid, new machined ID if it is missing or empty. The new machine ID will be acquired in the following fashion: </p>
<dl>
<dt>
<dd> 1. If a valid D-Bus machine ID is already configured for the system, the D-Bus machine ID is copied and used to initialize the machine ID in /etc/machine-id.</dl>
<dl>
<dt>
<dd> 2. If run inside a KVM virtual machine and a UUID is configured (via the <code>-uuid</code> option), this UUID is used to initialize the machine ID. The caller must ensure that the UUID passed is sufficiently unique and is different for every booted instance of the VM.</dl>
<dl>
<dt>
<dd> 3. Similarly, if run inside a Linux container environment and a UUID is configured for the container, this is used to initialize the machine ID. For details, see the documentation of the m[blue]<code>Container Interface</code>m[]<font SIZE="-2">[1]</font>.</dl>
<dl>
<dt>
<dd> 4. Otherwise, a new ID is randomly generated.</dl>
<p> The <code>&#8211;commit</code> switch may be used to commit a transient machined ID to disk, making it persistent. For details, see below. </p>
<p> Use <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) to initialize the machine ID on mounted (but not booted) system images.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;root=</code><i>path</i></p>
<dl>
<dt>
<dd> Takes a directory path as argument. All paths operated on will be prefixed with the given alternate <i>root</i> path, including the path for /etc/machine-id itself.</dl>
<p> <code>&#8211;image=</code><i>path</i></p>
<dl>
<dt>
<dd> Takes a path to a device node or regular file as argument. This is similar to <code>&#8211;root=</code> as described above, but operates on a disk image instead of a directory tree.</dl>
<p> <code>&#8211;commit</code></p>
<dl>
<dt>
<dd> Commit a transient machine ID to disk. This command may be used to convert a transient machine ID into a persistent one. A transient machine ID file is one that was bind mounted from a memory file system (usually &quot;tmpfs&quot;) to /etc/machine-id during the early phase of the boot process. This may happen because /etc/ is initially read-only and was missing a valid machine ID file at that point. </p>
<p> This command will execute no operation if /etc/machine-id is not mounted from a memory file system, or if /etc/ is read-only. The command will write the current transient machine ID to disk and unmount the /etc/machine-id mount point in a race-free manner to ensure that this file is always valid and accessible for other processes. </p>
<p> This command is primarily used by the <code><a href="/docs/linux/man/8-systemd-machine-id-commit-service/">systemd-machine-id-commit.service</a></code>(8) early boot service.</dl>
<p> <code>&#8211;print</code></p>
<dl>
<dt>
<dd> Print the machine ID generated or committed after the operation is complete.</dl>
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
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/8-systemd-machine-id-commit-service/">systemd-machine-id-commit.service</a></code>(8), <code><a href="/docs/linux/man/1-dbus-uuidgen/">dbus-uuidgen</a></code>(1), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Container Interface</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://systemd.io/CONTAINER_INTERFACE">https://systemd.io/CONTAINER_INTERFACE</a></dl>
</dl>
<h2>Index</h2>
