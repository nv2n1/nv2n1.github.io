---
title: "cgroupfs-mount(8)"
name: "cgroupfs-mount"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cgroupfs-mount/"
description: "cgroupfs-mount, cgroupfs-umount – set up cgroupfs mount hierarchies"
---

<p>cgroupfs-mount, cgroupfs-umount &#8211; set up cgroupfs mount hierarchies</p>
<h2>Synopsis</h2>
<p>Control groups are a kernel mechanism for tracking and imposing limits on resource usage on groups of tasks. These scripts mount and unmount the hierarchies for managing them. </p>
<p> <code>cgroupfs-mount</code> </p>
<p> <code>cgroupfs-umount</code></p>
<h2>Description</h2>
<p>The location for the mounts these scripts create is <i>/sys/fs/cgroup</i>, which is widely regarded as &quot;the place&quot; for these to be mounted (for example, <code>systemd</code> mounts them here as well).</p>
<h2>Return Value</h2>
<p>Zero for success or if it is determined that we can or should not mount, due to user entries in <i>/etc/fstab</i> or pre-existing mounts. Non-zero for explicit failures.</p>
<h2>CAVEATS &amp; DIAGNOSTICS</h2>
<p>It is critically important for the proper operation of these scripts that you do not manually include any cgroup mount points in <i>/etc/fstab</i>. After commenting out any extraneous cgroup entries in <i>/etc/fstab</i>, you should either reboot or manually <code>umount</code> them and then run <code>cgroupfs-mount</code> again.</p>
<h2>Restrictions</h2>
<p>These scripts intentionally do not do any cgroup management or classification of tasks into cgroups. They are also very intentionally light on configurability (to the point of non-existence) to keep the implementation simple and less error-prone.</p>
<h2>Authors</h2>
<p>Serge Hallyn and Tianon Gravi</p>
<h2>History</h2>
<p>This package was originally derived from the <code>cgroup-lite</code> package from Ubuntu.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
