---
title: "btrfs-subvolume(8)"
name: "btrfs-subvolume"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-subvolume/"
description: "btrfs-subvolume – manage btrfs subvolumes"
---

<p>btrfs-subvolume &#8211; manage btrfs subvolumes</p>
<h2>Synopsis</h2>
<p><code>btrfs subvolume</code> <i>&lt;subcommand&gt;</i> [<i>&lt;args&gt;</i>]</p>
<h2>Description</h2>
<p><code>btrfs subvolume</code> is used to create/delete/list/show btrfs subvolumes and snapshots.</p>
<h2>Subvolume And Snapshot</h2>
<p>A subvolume is a part of filesystem with its own independent file/directory hierarchy. Subvolumes can share file extents. A snapshot is also subvolume, but with a given initial content of the original subvolume. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> A subvolume in btrfs is not like an LVM logical volume, which is block-level snapshot while btrfs subvolumes are file extent-based. </p>
</dl>
<p> A subvolume looks like a normal directory, with some additional operations described below. Subvolumes can be renamed or moved, nesting subvolumes is not restricted but has some implications regarding snapshotting. </p>
<p> A subvolume in btrfs can be accessed in two ways: </p>
<dl>
<dd>&bull; like any other directory that is accessible to the user</dl>
<dl>
<dd>&bull; like a separately mounted filesystem (options <i>subvol</i> or <i>subvolid</i>)</dl>
<p> In the latter case the parent directory is not visible and accessible. This is similar to a bind mount, and in fact the subvolume mount does exactly that. </p>
<p> A freshly created filesystem is also a subvolume, called <i>top-level</i>, internally has an id 5. This subvolume cannot be removed or replaced by another subvolume. This is also the subvolume that will be mounted by default, unless the default subvolume has been changed (see subcommand <i>set-default</i>). </p>
<p> A snapshot is a subvolume like any other, with given initial content. By default, snapshots are created read-write. File modifications in a snapshot do not affect the files in the original subvolume.</p>
<h2>Subcommand</h2>
<p><code>create</code> [-i <i>&lt;qgroupid&gt;</i>] [&lt;dest&gt;/]<i>&lt;name&gt;</i></p>
<dl>
<dd>Create a subvolume <i>&lt;name&gt;</i> in <i>&lt;dest&gt;</i>. </p>
<p> If <i>&lt;dest&gt;</i> is not given, subvolume <i>&lt;name&gt;</i> will be created in the current directory. </p>
<p> <code>Options</code> </p>
<p> -i <i>&lt;qgroupid&gt;</i></p>
<dl>
<dd>Add the newly created subvolume to a qgroup. This option can be given multiple times.</dl>
</dl>
<p> <code>delete</code> [options] <i>&lt;subvolume&gt;</i> [<i>&lt;subvolume&gt;</i>&#8230;]</p>
<dl>
<dd>Delete the subvolume(s) from the filesystem. </p>
<p> If <i>&lt;subvolume&gt;</i> is not a subvolume, btrfs returns an error but continues if there are more arguments to process. </p>
<p> The corresponding directory is removed instantly but the data blocks are removed later in the background. The command returns immediately. See <code>btrfs subvolume sync</code> how to wait until the subvolume gets completely removed. </p>
<p> The deletion does not involve full transaction commit by default due to performance reasons. As a consequence, the subvolume may appear again after a crash. Use one of the <i>&#8211;commit</i> options to wait until the operation is safely stored on the device. </p>
<p> <code>Options</code> </p>
<p> -c|&#8211;commit-after</p>
<dl>
<dd>wait for transaction commit at the end of the operation.</dl>
<p> -C|&#8211;commit-each</p>
<dl>
<dd>wait for transaction commit after deleting each subvolume.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dd>verbose output of operations.</dl>
</dl>
<p> <code>find-new</code> <i>&lt;subvolume&gt;</i> <i>&lt;last_gen&gt;</i></p>
<dl>
<dd>List the recently modified files in a subvolume, after <i>&lt;last_gen&gt;</i> generation.</dl>
<p> <code>get-default</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Get the default subvolume of the filesystem <i>&lt;path&gt;</i>. </p>
<p> The output format is similar to <code>subvolume list</code> command.</dl>
<p> <code>list</code> [options] [-G [+|-]<i>&lt;value&gt;</i>] [-C [+|-]<i>&lt;value&gt;</i>] [&#8211;sort=rootid,gen,ogen,path] <i>&lt;path&gt;</i></p>
<dl>
<dd>List the subvolumes present in the filesystem <i>&lt;path&gt;</i>. </p>
<p> For every subvolume the following information is shown by default: </p>
<p> ID <i>&lt;ID&gt;</i> gen <i>&lt;generation&gt;</i> top level <i>&lt;ID&gt;</i> path <i>&lt;path&gt;</i> </p>
<p> where ID is subvolume&#8217;s id, gen is an internal counter which is updated every transaction, top level is the same as parent subvolume&#8217;s id, and path is the relative path of the subvolume to the top level subvolume. The subvolume&#8217;s ID may be used by the subvolume set-default command, or at mount time via the subvolid= option. </p>
<p> <code>Options</code> </p>
<p> Path filtering</p>
<dl>
<dd>-o</p>
<dl>
<dd>print only subvolumes below specified <i>&lt;path&gt;</i>.</dl>
<p> -a</p>
<dl>
<dd>print all the subvolumes in the filesystem and distinguish between absolute and relative path with respect to the given <i>&lt;path&gt;</i>.</dl>
</dl>
<p> Field selection</p>
<dl>
<dd>-p</p>
<dl>
<dd>print the parent ID (<i>parent</i> here means the subvolume which contains this subvolume).</dl>
<p> -c</p>
<dl>
<dd>print the ogeneration of the subvolume, aliases: ogen or origin generation.</dl>
<p> -g</p>
<dl>
<dd>print the generation of the subvolume (default).</dl>
<p> -u</p>
<dl>
<dd>print the UUID of the subvolume.</dl>
<p> -q</p>
<dl>
<dd>print the parent UUID of the subvolume (<i>parent</i> here means subvolume of which this subvolume is a snapshot).</dl>
<p> -R</p>
<dl>
<dd>print the UUID of the sent subvolume, where the subvolume is the result of a receive operation.</dl>
</dl>
<p> Type filtering</p>
<dl>
<dd>-s</p>
<dl>
<dd>only snapshot subvolumes in the filesystem will be listed.</dl>
<p> -r</p>
<dl>
<dd>only readonly subvolumes in the filesystem will be listed.</dl>
<p> -d</p>
<dl>
<dd>list deleted subvolumes that are not yet cleaned.</dl>
</dl>
<p> Other</p>
<dl>
<dd>-t</p>
<dl>
<dd>print the result as a table.</dl>
</dl>
<p> Sorting</p>
<dl>
<dd>By default the subvolumes will be sorted by subvolume ID ascending. </p>
<p> -G [+|-]<i>&lt;value&gt;</i></p>
<dl>
<dd>list subvolumes in the filesystem that its generation is &gt;=, &lt; or = value. &#8216;+&#8217; means &gt;= value, &#8216;-&#8216; means &lt;= value, If there is neither &#8216;+&#8217; nor &#8216;-&#8216;, it means = value.</dl>
<p> -C [+|-]<i>&lt;value&gt;</i></p>
<dl>
<dd>list subvolumes in the filesystem that its ogeneration is &gt;=, &lt;= or = value. The usage is the same to <i>-G</i> option.</dl>
<p> &#8211;sort=rootid,gen,ogen,path</p>
<dl>
<dd>list subvolumes in order by specified items. you can add &#8216;+&#8217; or &#8216;-&#8216; in front of each items, &#8216;+&#8217; means ascending, &#8216;-&#8216; means descending. The default is ascending. </p>
<p> for &#8211;sort you can combine some items together by &#8216;,&#8217;, just like &#8211;sort=+ogen,-gen,path,rootid.</dl>
</dl>
</dl>
<p> <code>set-default</code> [<i>&lt;subvolume&gt;</i>|<i>&lt;id&gt;</i> <i>&lt;path&gt;</i>]</p>
<dl>
<dd>Set the default subvolume for the (mounted) filesystem. </p>
<p> Set the default subvolume for the (mounted) filesystem at <i>&lt;path&gt;</i>. This will hide the top-level subvolume (i.e. the one mounted with <i>subvol=/</i> or <i>subvolid=5</i>). Takes action on next mount. </p>
<p> There are two ways how to specify the subvolume, by <i>&lt;id&gt;</i> or by the <i>&lt;subvolume&gt;</i> path. The id can be obtained from <code>btrfs subvolume list</code>, <code>btrfs subvolume show</code> or <code>btrfs inspect-internal rootid</code>.</dl>
<p> <code>show</code> [options] <i>&lt;path&gt;</i></p>
<dl>
<dd>Show more information about subvolume <i>&lt;path&gt;</i> regarding UUIDs, times, generations, flags and related snapshots. </p>
<dl>
<dd>
<pre>/mnt/btrfs/subvolume
 Name: subvolume
 UUID: 5e076a14-4e42-254d-ac8e-55bebea982d1
 Parent UUID: -
 Received UUID: -
 Creation time: 2018-01-01 12:34:56 +0000
 Subvolume ID: 79
 Generation: 2844
 Gen at creation: 2844
 Parent ID: 5
 Top level ID: 5
 Flags: -
 Snapshot(s):</pre>
</dl>
<p> <code>Options</code> </p>
<p> -r|&#8211;rootid</p>
<dl>
<dd>rootid of the subvolume.</dl>
<p> -u|&#8211;uuid</p>
<dl>
<dd>UUID of the subvolume.</dl>
</dl>
<p> <code>snapshot</code> [-r|-i <i>&lt;qgroupid&gt;</i>] <i>&lt;source&gt;</i> <i>&lt;dest&gt;</i>|[&lt;dest&gt;/]<i>&lt;name&gt;</i></p>
<dl>
<dd>Create a snapshot of the subvolume <i>&lt;source&gt;</i> with the name <i>&lt;name&gt;</i> in the <i>&lt;dest&gt;</i> directory. </p>
<p> If only <i>&lt;dest&gt;</i> is given, the subvolume will be named the basename of <i>&lt;source&gt;</i>. If <i>&lt;source&gt;</i> is not a subvolume, btrfs returns an error. </p>
<p> <code>Options</code> </p>
<p> -r</p>
<dl>
<dd>Make the new snapshot read only.</dl>
<p> -i <i>&lt;qgroupid&gt;</i></p>
<dl>
<dd>Add the newly created subvolume to a qgroup. This option can be given multiple times.</dl>
</dl>
<p> <code>sync</code> <i>&lt;path&gt;</i> [subvolid&#8230;]</p>
<dl>
<dd>Wait until given subvolume(s) are completely removed from the filesystem after deletion. If no subvolume id is given, wait until all current deletion requests are completed, but do not wait for subvolumes deleted in the meantime. </p>
<p> <code>Options</code> </p>
<p> -s <i>&lt;N&gt;</i></p>
<dl>
<dd>sleep N seconds between checks (default: 1)</dl>
</dl>
<h2>Exit Status</h2>
<p><code>btrfs subvolume</code> returns a zero exit status if it succeeds. A non-zero value is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-quota/">btrfs-quota</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-qgroup/">btrfs-qgroup</a></code>(8), </p>
