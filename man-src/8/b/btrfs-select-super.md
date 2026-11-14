---
title: "btrfs-select-super(8)"
name: "btrfs-select-super"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-select-super/"
description: "btrfs-select-super – overwrite primary superblock with a backup copy"
---

<p>btrfs-select-super &#8211; overwrite primary superblock with a backup copy</p>
<h2>Synopsis</h2>
<p><code>btrfs-select-super</code> -s number <i>&lt;device&gt;</i></p>
<h2>Description</h2>
<p>Destructively overwrite all copies of the superblock with a specified copy. This helps in certain cases, for example when write barriers were disabled during a power failure and not all superblocks were written, or if the primary superblock is damaged, eg. accidentally overwritten. The filesystem specified by <i>device</i> must not be mounted.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 <code>Prior to overwriting the primary superblock, please make sure that the backup copies are valid!</code>  To dump a superblock use the <code>btrfs inspect-internal dump-super</code> command. Then run the check (in the non-repair mode) using the command <code>btrfs check -s</code> where <i>-s</i> specifies the superblock copy to use. Superblock copies exist in the following offsets on the device:</p>
<dl>
<dd>&bull; primary: <i>64KiB</i> (65536)</dl>
<dl>
<dd>&bull; 1st copy: <i>64MiB</i> (67108864)</dl>
<dl>
<dd>&bull; 2nd copy: <i>256GiB</i> (274877906944)</dl>
<p> A superblock size is <i>4KiB</i> (4096).</p>
<h2>Options</h2>
<p>-s|&#8211;super <i>&lt;superblock&gt;</i></p>
<dl>
<dd>use &#8216;superblock&#8217;th superblock copy, valid values are 0 1 or 2 if the respective superblock offset is within the device size</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-btrfs-inspect-internal/">btrfs-inspect-internal</a></code>(8), <code>btrfsck <a href="/docs/linux/man/8-check/">check</a></code>(8) </p>
