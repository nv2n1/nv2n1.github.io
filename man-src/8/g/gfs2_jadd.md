---
title: "gfs2_jadd(8)"
name: "gfs2_jadd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs2_jadd/"
description: "gfs2_jadd – Add journals to a GFS2 filesystem"
---

<p>gfs2_jadd &#8211; Add journals to a GFS2 filesystem</p>
<h2>Synopsis</h2>
<p><code>gfs2_jadd</code> [<i>OPTION</i>]&#8230; &lt;<i>DEVICE</i>|<i>MOINTPOINT</i>&gt;&#8230; </p>
<h2>Description</h2>
<p><i>gfs2_jadd</i> is used to add journals (and a few other per-node files) to a GFS2 filesystem. When this operation is complete, the journal index is updated so that machines mounting the filesystem at a later date will see the newly created journals in addition to the journals already there. Machines which are already running in the cluster are unaffected. You may only run <i>gfs2_jadd</i> on a mounted filesystem, addition of journals to unmounted filesystems is not supported. You only need to run <i>gfs2_jadd</i> on one node in the cluster. All the other nodes will see the expansion has occurred when required. You must be superuser to execute <i>gfs2_jadd</i>. The <i>gfs2_jadd</i> tool tries to prevent you from corrupting your filesystem by checking as many of the likely problems as it can. When growing a filesystem, only the last step of updating the journal index affects the currently mounted filesystem and so failure part way through the expansion process should leave your filesystem in its original state. </p>
<h2>Options</h2>
<dl>
<dt><code>-c MegaBytes</code></dt>
<dd>Initial size of each journal&#8217;s quota change file</dd>
<dt><code>-D</code></dt>
<dd>Print out debugging information about the filesystem layout.</dd>
<dt><code>-h</code></dt>
<dd>Prints out a short usage message and exits.</dd>
<dt><code>-J size</code></dt>
<dd>The size of the new journals in megabytes. The defaults to 32MB (the minimum size allowed is 8MB). If you want to add journals of different sizes to the filesystem, you&#8217;ll need to run gfs2_jadd once for each different size of journal.</dd>
<dt><code>-j num</code></dt>
<dd>The number of new journals to add.</dd>
<dt><code>-q</code></dt>
<dd>Be quiet. Don&#8217;t print anything.</dd>
<dt><code>-V</code></dt>
<dd>Version. Print version information, then exit.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mkfs-gfs2/">mkfs.gfs2</a>(8) <a href="/docs/linux/man/8-gfs2_grow/">gfs2_grow</a>(8) </p>
