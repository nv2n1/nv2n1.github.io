---
title: "tunegfs2(8)"
name: "tunegfs2"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tunegfs2/"
description: "tunegfs2 – View and manipulate gfs2 superblocks"
---

<p>tunegfs2 &#8211; View and manipulate gfs2 superblocks</p>
<h2>Synopsis</h2>
<p><code>tunegfs2</code> [<i>OPTIONS</i>] /dev/blockdevice </p>
<h2>Description</h2>
<p>tunegfs2 allows viewing and manipulating the values contained in a GFS or GFS2 superblock. It is able to modify the <i>UUID</i> (on GFS2 only), <i>label</i>, <i>lockproto</i> and <i>locktable</i>. The values in the GFS2 superblock are read only on mount. Any changes on a live filesystem will not take effect until the next time it is mounted. Making changes on a live filesystem is not recommended for this reason. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Prints out usage information for this command. </p>
<dt><code>-l</code></p>
<dd>List contents of the filesystem superblock. Includes the current values of the parameters that can be set by this program. </p>
<dt><code>-L</code> <i>&lt;label&gt;</i></p>
<dd>Change the filesystem label. Note that the GFS2 filesystem label is also the locktable name. </p>
<dt><code>-o</code> <i>[lockproto=&lt;proto&gt;]</i> <i>[locktable=&lt;table&gt;]</i></p>
<dd>Set mount options. Currently supported options include lockproto and locktable </p>
<dt><code>-U</code> <i>&lt;uuid&gt;</i></p>
<dd>Set the filesystem UUID </p>
<dt><code>-V</code></p>
<dd>Print out the information on the version of the tool. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-gfs2/">gfs2</a></code>(5) </p>
