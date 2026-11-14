---
title: "gfs2_grow(8)"
name: "gfs2_grow"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs2_grow/"
description: "gfs2_grow – Expand a GFS2 filesystem"
---

<p>gfs2_grow &#8211; Expand a GFS2 filesystem</p>
<h2>Synopsis</h2>
<p><code>gfs2_grow</code> [<i>OPTION</i>]&#8230; &lt;<i>DEVICE</i>|<i>MOUNTPOINT</i>&gt;&#8230; </p>
<h2>Description</h2>
<p>gfs2_grow is used to expand a GFS2 filesystem after the device upon which the filesystem resides has also been expanded. By running gfs2_grow on a GFS2 filesystem, you are requesting that any spare space between the current end of the filesystem and the end of the device is filled with a newly initialized GFS2 filesystem extension. When this operation is complete, the resource group index for the filesystem is updated so that all nodes in the cluster can use the extra storage space that has been added. </p>
<p> You may only run gfs2_grow on a mounted filesystem; expansion of unmounted filesystems is not supported. You only need to run gfs2_grow on one node in the cluster. All the other nodes will see the expansion has occurred and automatically start to use the newly available space. </p>
<p> You must be superuser to execute <code>gfs2_grow</code>. The gfs2_grow tool tries to prevent you from corrupting your filesystem by checking as many of the likely problems as it can. When expanding a filesystem, only the last step of updating the resource index affects the currently mounted filesystem and so failure part way through the expansion process should leave your filesystem in its original unexpanded state. </p>
<p> You can run gfs2_grow with the <code>-T</code> flag to get a display of the current state of a mounted GFS2 filesystem. </p>
<p> The gfs2_grow tool uses the resource group (RG) size that was originally calculated when mkfs.gfs2 was done. This allows tools like fsck.gfs2 to better ensure the integrity of the file system. Since the new free space often does not lie on even boundaries based on that RG size, there may be some unused space on the device after gfs2_grow is run.</p>
<h2>Options</h2>
<dl>
<dt><code>-D</code></p>
<dd>Print out debugging information about the filesystem layout.</p>
<dt><code>-h</code></p>
<dd>Prints out a short usage message and exits.</p>
<dt><code>-q</code></p>
<dd>Be quiet. Don&#8217;t print anything.</p>
<dt><code>-T</code></p>
<dd>Test. Do all calculations, but do not write any data to the disk and do not expand the filesystem. This is used to discover what the tool would have done were it run without this flag.</p>
<dt><code>-V</code></p>
<dd>Version. Print out version information, then exit. </p>
</dl>
<h2>Bugs</h2>
<p>There is no way to shrink a GFS2 filesystem. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mkfs-gfs2/">mkfs.gfs2</a>(8) <a href="/docs/linux/man/8-gfs2_jadd/">gfs2_jadd</a>(8) </p>
