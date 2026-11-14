---
title: "ceph-rbdnamer(8)"
name: "ceph-rbdnamer"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ceph-rbdnamer/"
description: "ceph-rbdnamer – udev helper to name RBD devices"
---

<p>ceph-rbdnamer &#8211; udev helper to name RBD devices</p>
<h2>Synopsis</h2>
<pre><code>ceph-rbdnamer</code> <i>num</i></pre>
<h2>Description</h2>
<p><code>ceph-rbdnamer</code> prints the pool and image name for the given RBD devices to stdout. It is used by <i>udev</i> (using a rule like the one below) to set up a device symlink. </p>
<pre><code>KERNEL==&quot;rbd[0-9]*&quot;, PROGRAM=&quot;/usr/bin/ceph-rbdnamer %n&quot;, SYMLINK+=&quot;rbd/%c{1}/%c{2}&quot;</code></pre>
<h2>Availability</h2>
<p><code>ceph-rbdnamer</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rbd/">rbd</a></code>(8), <code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8)</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
