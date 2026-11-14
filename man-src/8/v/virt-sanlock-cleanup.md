---
title: "virt-sanlock-cleanup(8)"
name: "virt-sanlock-cleanup"
section: "8"
letter: "v"
url: "/docs/linux/man/8-virt-sanlock-cleanup/"
description: "virt-sanlock-cleanup – remove stale sanlock resource lease files"
---

<p>virt-sanlock-cleanup &#8211; remove stale sanlock resource lease files</p>
<h2>Synopsis</h2>
<p><code>virt-sanlock-cleanup</code></p>
<h2>Description</h2>
<p>This tool removes any resource lease files created by the sanlock lock manager plugin. The resource lease files only need to exist on disks when a guest using the resource is active. This script reclaims the disk space used by resources which are not currently active.</p>
<h2>Exit Status</h2>
<p>Upon successful processing of leases cleanup, an exit status of 0 will be set. Upon fatal error a non-zero status will be set.</p>
<h2>Author</h2>
<p>Daniel Berrange</p>
<h2>Bugs</h2>
<p>Report any bugs discovered to the libvirt community via the mailing list &lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt; or bug tracker &lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;. Alternatively report bugs to your software distributor / vendor.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2011, 2013 Red Hat, Inc.</p>
<h2>License</h2>
<p>virt-sanlock-cleanup is distributed under the terms of the <font SIZE="-1">GNU GPL</font> v2+. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), online instructions &lt;<a rel="nofollow" href="http://libvirt.org/locking.html">http://libvirt.org/locking.html</a>&gt; </p>
