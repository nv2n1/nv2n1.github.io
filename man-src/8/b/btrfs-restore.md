---
title: "btrfs-restore(8)"
name: "btrfs-restore"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-restore/"
description: "btrfs-restore – try to restore files from a damaged btrfs filesystem image"
---

<p>btrfs-restore &#8211; try to restore files from a damaged btrfs filesystem image</p>
<h2>Synopsis</h2>
<p><code>btrfs restore</code> [options] <i>&lt;device&gt;</i> <i>&lt;path&gt;</i> | -l <i>&lt;device&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs restore</code> is used to try to salvage files from a damaged filesystem and restore them into <i>&lt;path&gt;</i> or just list the subvolume tree roots. The filesystem image is not modified. If the filesystem is damaged and cannot be repaired by the other tools (<code><a href="/docs/linux/man/8-btrfs-check/">btrfs-check</a></code>(8) or <code><a href="/docs/linux/man/8-btrfs-rescue/">btrfs-rescue</a></code>(8)), <code>btrfs restore</code> could be used to retrieve file data, as far as the metadata are readable. The checks done by restore are less strict and the process is usually able to get far enough to retrieve data from the whole filesystem. This comes at a cost that some data might be incomplete or from older versions if they&#8217;re available. There are several options to attempt restoration of various file metadata type. You can try a dry run first to see how well the process goes and use further options to extend the set of restored metadata. For images with damaged tree structures, there are several options to point the process to some spare copy.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 It is recommended to read the following btrfs wiki page if your data is not salvaged with default option: m[blue]<code><a rel="nofollow" href="https://btrfs.wiki.kernel.org/index.php/Restore">https://btrfs.wiki.kernel.org/index.php/Restore</a></code>m[] </p>
<h2>Options</h2>
<p>-s|&#8211;snapshots</p>
<dl>
<dd>get also snapshots that are skipped by default</dl>
<p> -x|&#8211;xattr</p>
<dl>
<dd>get extended attributes</dl>
<p> -m|&#8211;metadata</p>
<dl>
<dd>restore owner, mode and times for files and directories</dl>
<p> -S|&#8211;symlinks</p>
<dl>
<dd>restore symbolic links as well as normal files</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dd>be verbose and print what is being restored</dl>
<p> -i|&#8211;ignore-errors</p>
<dl>
<dd>ignore errors during restoration and continue</dl>
<p> -o|&#8211;overwrite</p>
<dl>
<dd>overwrite directories/files in <i>&lt;path&gt;</i>, eg. for repeated runs</dl>
<p> -t <i>&lt;bytenr&gt;</i></p>
<dl>
<dd>use <i>&lt;bytenr&gt;</i> to read the root tree</dl>
<p> -f <i>&lt;bytenr&gt;</i></p>
<dl>
<dd>only restore files that are under specified subvolume root pointed by <i>&lt;bytenr&gt;</i></dl>
<p> -u|&#8211;super <i>&lt;mirror&gt;</i></p>
<dl>
<dd>use given superblock mirror identified by <i>&lt;mirror&gt;</i>, it can be 0,1 or 2</dl>
<p> -r|&#8211;root <i>&lt;rootid&gt;</i></p>
<dl>
<dd>only restore files that are under a specified subvolume whose objectid is <i>&lt;rootid&gt;</i></dl>
<p> -d</p>
<dl>
<dd>find directory</dl>
<p> -l|&#8211;list-roots</p>
<dl>
<dd>list subvolume tree roots, can be used as argument for <i>-r</i></dl>
<p> -D|&#8211;dry-run</p>
<dl>
<dd>dry run (only list files that would be recovered)</dl>
<p> &#8211;path-regex <i>&lt;regex&gt;</i></p>
<dl>
<dd>restore only filenames matching a regular expression (<code><a href="/docs/linux/man/7-regex/">regex</a></code>(7)) with a mandatory format </p>
<p> <code>^/(|home(|/username(|/Desktop(|/.*))))$</code> </p>
<p> The format is not very comfortable and restores all files in the directories in the whole path, so this is not useful for restoring single file in a deep hierarchy.</dl>
<p> -c</p>
<dl>
<dd>ignore case (&#8211;path-regex only)</dl>
<h2>Exit Status</h2>
<p><code>btrfs restore</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-rescue/">btrfs-rescue</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-check/">btrfs-check</a></code>(8) </p>
