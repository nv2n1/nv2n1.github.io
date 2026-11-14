---
title: "gfs_jadd(8)"
name: "gfs_jadd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs_jadd/"
description: "gfs_jadd – Add journals to a GFS filesystem"
---

<p>gfs_jadd &#8211; Add journals to a GFS filesystem</p>
<h2>Synopsis</h2>
<p><code>gfs_jadd</code> [<i>OPTION</i>]&#8230; &lt;<i>DEVICE</i>|<i>MOINTPOINT</i>&gt;&#8230; </p>
<h2>Description</h2>
<p><i>gfs_jadd</i> is used to add journals to a GFS filesystem after the device upon which the filesystem resides has been grown. By running <i>gfs_jadd</i> on a GFS filesystem, you are filling in space between the current end of the filesystem and the end of the device upon which the filesystem resides. When this operation is complete, the journal index is updated so that machines mounting the filesystem at a later date will see the newly created journals in addition to the journals already there. Machines which are already running in the cluster are unaffected. <i>gfs_jadd</i> will not use space that has been formatted for filesystem data even if that space has never been populated with files. You may only run <i>gfs_jadd</i> on a mounted filesystem, addition of journals to unmounted filesystems is not supported. You only need to run <i>gfs_jadd</i> on one node in the cluster. All the other nodes will see the expansion has occurred when required. You must be superuser to execute <i>gfs_jadd</i>. The <i>gfs_jadd</i> tool tries to prevent you from corrupting your filesystem by checking as many of the likely problems as it can. When growing a filesystem, only the last step of updating the journal index affects the currently mounted filesystem and so failure part way through the expansion process should leave your filesystem in its original state. You can run <i>gfs_jadd</i> with the <i>-Tv</i> flags to get a display of the current state of a mounted GFS filesystem. This can be useful to do after the journal addition process to see if the changes have been successful. </p>
<h2>Options</h2>
<dl>
<dt><code>-j num</code></p>
<dd>The number of new journals to add. This defaults to 1.</p>
<dt><code>-J size</code></p>
<dd>The size of the new journals in megabytes. The defaults to 128MB (the minimum size allowed is 32MB). If you want to add journals of different sizes to the filesystem, you&#8217;ll need to run gfs_jadd once for each different size of journal. The size you specify here will be rounded down so that it is a multiple of the journal segment size which was specified at filesystem creation time.</p>
<dt><code>-h</code></p>
<dd>Help. Prints out a short usage message and exits.</p>
<dt><code>-q</code></p>
<dd>Quiet. Turns down the verbosity level.</p>
<dt><code>-T</code></p>
<dd>Test. Do all calculations, but do not write any data to the disk and do not add journals. This is used to discover what the tool would have done were it run without this flag. You probably want to turn the verbosity level up in order to gain most information from this option.</p>
<dt><code>-V</code></p>
<dd>Version. Print version information, then exit.</p>
<dt><code>-v</code></p>
<dd>Verbose. Turn up verbosity of messages. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mkfs-gfs/">mkfs.gfs</a>(8) <a href="/docs/linux/man/8-gfs_grow/">gfs_grow</a>(8) </p>
