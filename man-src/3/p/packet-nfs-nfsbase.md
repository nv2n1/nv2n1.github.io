---
title: "packet-nfs-nfsbase(3)"
name: "packet-nfs-nfsbase"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-nfs-nfsbase/"
description: "packet.nfs.nfsbase – NFS Base module"
---

<p>packet.nfs.nfsbase &#8211; NFS Base module</p>
<h2>Description</h2>
<p>Base class for an NFS object</p>
<h2>Classes</h2>
<h3>class CB_NULL(NFSbase)</h3>
<pre>NFS CB_NULL object</pre>
<h3>class NFSbase(packet.utils.RPCload)</h3>
<pre>NFS Base object
This should only be used as a base class for an NFS object
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code>
Informal string representation of object</pre>
<h3>class NULL(NFSbase)</h3>
<pre>NFS NULL object</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs4_const/">packet.nfs.nfs4_const</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
