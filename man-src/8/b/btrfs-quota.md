---
title: "btrfs-quota(8)"
name: "btrfs-quota"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-quota/"
description: "btrfs-quota – control the global quota status of a btrfs filesystem"
---

<p>btrfs-quota &#8211; control the global quota status of a btrfs filesystem</p>
<h2>Synopsis</h2>
<p><code>btrfs quota</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p>The commands under <code>btrfs quota</code> are used to affect the global status of quotas of a btrfs filesystem. The quota groups (qgroups) are managed by the subcommand <code>btrfs <a href="/docs/linux/man/8-qgroup/">qgroup</a></code>(8). </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Qgroups are different than the traditional user quotas and designed to track shared and exclusive data per-subvolume. Please refer to the section <i>HIERARCHICAL QUOTA GROUP CONCEPTS</i> for a detailed description. </p>
</dl>
<h3>Performance Implications</h3>
<p>When quotas are activated, they affect all extent processing, which takes a performance hit. Activation of qgroups is not recommended unless the user intends to actually use them.</p>
<h3>Stability Status</h3>
<p>The qgroup implementation has turned out to be quite difficult as it affects the core of the filesystem operation. Qgroup users have hit various corner cases over time, such as incorrect accounting or system instability. The situation is gradually improving and issues found and fixed.</p>
<h2>Hierarchical Quota Group Concepts</h2>
<p>The concept of quota has a long-standing tradition in the Unix world. Ever since computers allow multiple users to work simultaneously in one filesystem, there is the need to prevent one user from using up the entire space. Every user should get his fair share of the available resources. </p>
<p> In case of files, the solution is quite straightforward. Each file has an <i>owner</i> recorded along with it, and it has a size. Traditional quota just restricts the total size of all files that are owned by a user. The concept is quite flexible: if a user hits his quota limit, the administrator can raise it on the fly. </p>
<p> On the other hand, the traditional approach has only a poor solution to restrict directories. At installation time, the harddisk can be partitioned so that every directory (eg. /usr, /var/, &#8230;) that needs a limit gets its own partition. The obvious problem is that those limits cannot be changed without a reinstallation. The btrfs subvolume feature builds a bridge. Subvolumes correspond in many ways to partitions, as every subvolume looks like its own filesystem. With subvolume quota, it is now possible to restrict each subvolume like a partition, but keep the flexibility of quota. The space for each subvolume can be expanded or restricted on the fly. </p>
<p> As subvolumes are the basis for snapshots, interesting questions arise as to how to account used space in the presence of snapshots. If you have a file shared between a subvolume and a snapshot, whom to account the file to? The creator? Both? What if the file gets modified in the snapshot, should only these changes be accounted to it? But wait, both the snapshot and the subvolume belong to the same user home. I just want to limit the total space used by both! But somebody else might not want to charge the snapshots to the users. </p>
<p> Btrfs subvolume quota solves these problems by introducing groups of subvolumes and let the user put limits on them. It is even possible to have groups of groups. In the following, we refer to them as <i>qgroups</i>. </p>
<p> Each qgroup primarily tracks two numbers, the amount of total referenced space and the amount of exclusively referenced space. </p>
<p> referenced</p>
<dl>
<dd>space is the amount of data that can be reached from any of the subvolumes contained in the qgroup, while</dl>
<p> exclusive</p>
<dl>
<dd>is the amount of data where all references to this data can be reached from within this qgroup.</dl>
<h3>Subvolume Quota Groups</h3>
<p>The basic notion of the Subvolume Quota feature is the quota group, short qgroup. Qgroups are notated as <i>level/id</i>, eg. the qgroup 3/2 is a qgroup of level 3. For level 0, the leading <i>0/</i> can be omitted. Qgroups of level 0 get created automatically when a subvolume/snapshot gets created. The ID of the qgroup corresponds to the ID of the subvolume, so 0/5 is the qgroup for the root subvolume. For the <code>btrfs qgroup</code> command, the path to the subvolume can also be used instead of <i>0/ID</i>. For all higher levels, the ID can be chosen freely. </p>
<p> Each qgroup can contain a set of lower level qgroups, thus creating a hierarchy of qgroups. Figure 1 shows an example qgroup tree. </p>
<dl>
<dd>
<pre> +---+
 |2/1|
 +---+
 / \
 +---+/ \+---+
 |1/1| |1/2|
 +---+ +---+
 / \ / \
 +---+/ \+---+/ \+---+
qgroups |0/1| |0/2| |0/3|
 +-+-+ +---+ +---+
 | / \ / \
 | / \ / \
 | / \ / \
extents 1 2 3 4</pre>
</dl>
<p> Figure1: Sample qgroup hierarchy </p>
<p> At the bottom, some extents are depicted showing which qgroups reference which extents. It is important to understand the notion of <i>referenced</i> vs <i>exclusive</i>. In the example, qgroup 0/2 references extents 2 and 3, while 1/2 references extents 2-4, 2/1 references all extents. </p>
<p> On the other hand, extent 1 is exclusive to 0/1, extent 2 is exclusive to 0/2, while extent 3 is neither exclusive to 0/2 nor to 0/3. But because both references can be reached from 1/2, extent 3 is exclusive to 1/2. All extents are exclusive to 2/1. </p>
<p> So exclusive does not mean there is no other way to reach the extent, but it does mean that if you delete all subvolumes contained in a qgroup, the extent will get deleted. </p>
<p> Exclusive of a qgroup conveys the useful information how much space will be freed in case all subvolumes of the qgroup get deleted. </p>
<p> All data extents are accounted this way. Metadata that belongs to a specific subvolume (i.e. its filesystem tree) is also accounted. Checksums and extent allocation information are not accounted. </p>
<p> In turn, the referenced count of a qgroup can be limited. All writes beyond this limit will lead to a <i>Quota Exceeded</i> error.</p>
<h3>Inheritance</h3>
<p>Things get a bit more complicated when new subvolumes or snapshots are created. The case of (empty) subvolumes is still quite easy. If a subvolume should be part of a qgroup, it has to be added to the qgroup at creation time. To add it at a later time, it would be necessary to at least rescan the full subvolume for a proper accounting. </p>
<p> Creation of a snapshot is the hard case. Obviously, the snapshot will reference the exact amount of space as its source, and both source and destination now have an exclusive count of 0 (the filesystem nodesize to be precise, as the roots of the trees are not shared). But what about qgroups of higher levels? If the qgroup contains both the source and the destination, nothing changes. If the qgroup contains only the source, it might lose some exclusive. </p>
<p> But how much? The tempting answer is, subtract all exclusive of the source from the qgroup, but that is wrong, or at least not enough. There could have been an extent that is referenced from the source and another subvolume from that qgroup. This extent would have been exclusive to the qgroup, but not to the source subvolume. With the creation of the snapshot, the qgroup would also lose this extent from its exclusive set. </p>
<p> So how can this problem be solved? In the instant the snapshot gets created, we already have to know the correct exclusive count. We need to have a second qgroup that contains all the subvolumes as the first qgroup, except the subvolume we want to snapshot. The moment we create the snapshot, the exclusive count from the second qgroup needs to be copied to the first qgroup, as it represents the correct value. The second qgroup is called a tracking qgroup. It is only there in case a snapshot is needed.</p>
<h3>Use Cases</h3>
<p>Below are some usecases that do not mean to be extensive. You can find your own way how to integrate qgroups. </p>
<p> <font SIZE="+1"> <code>SINGLE-USER MACHINE</code></p>
<dl>
<dd><code>Replacement for partitions</code> </p>
<p> The simplest use case is to use qgroups as simple replacement for partitions. Btrfs takes the disk as a whole, and /, /usr, /var, etc. are created as subvolumes. As each subvolume gets it own qgroup automatically, they can simply be restricted. No hierarchy is needed for that. </p>
<p> <code>Track usage of snapshots</code> </p>
<p> When a snapshot is taken, a qgroup for it will automatically be created with the correct values. <i>Referenced</i> will show how much is in it, possibly shared with other subvolumes. <i>Exclusive</i> will be the amount of space that gets freed when the subvolume is deleted.</dl>
<p> </font><font SIZE="+2"> <code>MULTI-USER MACHINE</code></p>
<dl>
<dd><code>Restricting homes</code> </p>
<p> When you have several users on a machine, with home directories probably under /home, you might want to restrict /home as a whole, while restricting every user to an individual limit as well. This is easily accomplished by creating a qgroup for /home , eg. 1/1, and assigning all user subvolumes to it. Restricting this qgroup will limit /home, while every user subvolume can get its own (lower) limit. </p>
<p> <code>Accounting snapshots to the user</code> </p>
<p> Let&#8217;s say the user is allowed to create snapshots via some mechanism. It would only be fair to account space used by the snapshots to the user. This does not mean the user doubles his usage as soon as he takes a snapshot. Of course, files that are present in his home and the snapshot should only be accounted once. This can be accomplished by creating a qgroup for each user, say <i>1/UID</i>. The user home and all snapshots are assigned to this qgroup. Limiting it will extend the limit to all snapshots, counting files only once. To limit /home as a whole, a higher level group 2/1 replacing 1/1 from the previous example is needed, with all user qgroups assigned to it. </p>
<p> <code>Do not account snapshots</code> </p>
<p> On the other hand, when the snapshots get created automatically, the user has no chance to control them, so the space used by them should not be accounted to him. This is already the case when creating snapshots in the example from the previous section. </p>
<p> <code>Snapshots for backup purposes</code> </p>
<p> This scenario is a mixture of the previous two. The user can create snapshots, but some snapshots for backup purposes are being created by the system. The user&#8217;s snapshots should be accounted to the user, not the system. The solution is similar to the one from section <i>Accounting snapshots to the user</i>, but do not assign system snapshots to user&#8217;s qgroup.</dl>
<p> </font></p>
<h2>Subcommand</h2>
<p><code>disable</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Disable subvolume quota support for a filesystem.</dl>
<p> <code>enable</code> <i>&lt;path&gt;</i></p>
<dl>
<dd>Enable subvolume quota support for a filesystem.</dl>
<p> <code>rescan</code> [-s] <i>&lt;path&gt;</i></p>
<dl>
<dd>Trash all qgroup numbers and scan the metadata again with the current config. </p>
<p> <code>Options</code> </p>
<p> -s</p>
<dl>
<dd>show status of a running rescan operation.</dl>
<p> -w</p>
<dl>
<dd>wait for rescan operation to finish(can be already in progress).</dl>
</dl>
<h2>Exit Status</h2>
<p><code>btrfs quota</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-subvolume/">btrfs-subvolume</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-qgroup/">btrfs-qgroup</a></code>(8) </p>
