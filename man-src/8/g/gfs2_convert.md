---
title: "gfs2_convert(8)"
name: "gfs2_convert"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs2_convert/"
description: "gfs2_convert – Convert a GFS1 filesystem to GFS2"
---

<p>gfs2_convert &#8211; Convert a GFS1 filesystem to GFS2</p>
<h2>Synopsis</h2>
<p><code>gfs2_convert</code> [<i>OPTION</i>]&#8230; <i>DEVICE</i> </p>
<h2>Description</h2>
<p>gfs2_convert is used to convert a filesystem from GFS1 to GFS2. It is required that the GFS1 filesystem be checked and fixed for errors using <code>fsck.gfs2</code> and that the filesystem be backed up before attempting to convert it. The convert process is irreversible and any error encountered during the conversion can result in the abrupt termination of the program and consequently an unusable filesystem. See <code>NOTES</code> section below for more information. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd>Help. </dd>
<p> This prints out the proper command line usage syntax.</p>
<dt><code>-q</code></dt>
<dd>Quiet. Print less information while running.</dd>
<dt><code>-n</code></dt>
<dd>No to all questions.</dd>
<dt><code>-V</code></dt>
<dd>Print program Version information only. </dd>
<p> Print out the current version name.</p>
<dt><code>-v</code></dt>
<dd>Verbose operation. </dd>
<p> Print more information while running.</p>
<dt><code>-y</code></dt>
<dd>Yes to all questions. </dd>
<p> By specifying this option, gfs2_convert will not prompt before making changes. </p>
</dl>
<h2>Example</h2>
<dl>
<dt>gfs2_convert /dev/vg0/lvol0</dt>
<dd>This will convert the Global File System on the block device &quot;/dev/vg0/lvol0&quot; to gfs2 format. </dd>
<h2>Notes</h2>
<p>If gfs2_convert is interrupted for some reason other than a conversion failure, DO NOT run <code>gfs2_fsck</code> on this partially converted filesystem. When this occurs, reissue the gfs2_convert command on the partially converted filesystem to complete the conversion process. The GFS2 filesystem does not support Context-Dependent Path Names (CDPNs). gfs2_convert identifies such CDPNs and replaces them with empty directories with the same name. The administrator can use bind mounts on these directories to get the same effect as CDPNs. When converting full or nearly full filesystems, it is possible that there won&#8217;t be enough space available to fit all the GFS2 filesystem data structures. In such cases, the size of all the journals is reduced uniformly such that everything fits in the available space. </p>
</dl>