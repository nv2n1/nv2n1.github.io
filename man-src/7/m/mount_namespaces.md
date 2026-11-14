---
title: "mount_namespaces(7)"
name: "mount_namespaces"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mount_namespaces/"
description: "mount_namespaces – overview of Linux mount namespaces"
---

<p>mount_namespaces &#8211; overview of Linux mount namespaces</p>
<h2>Description</h2>
<p>For an overview of namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7). </p>
<p> Mount namespaces provide isolation of the list of mount points seen by the processes in each namespace instance. Thus, the processes in each of the mount namespace instances will see distinct single-directory hierarchies. </p>
<p> The views provided by the <i>/proc/[pid]/mounts</i>, <i>/proc/[pid]/mountinfo</i>, and <i>/proc/[pid]/mountstats</i> files (all described in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)) correspond to the mount namespace in which the process with the PID <i>[pid]</i> resides. (All of the processes that reside in the same mount namespace will see the same view in these files.) </p>
<p> A new mount namespace is created using either <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWNS</code> flag. When a new mount namespace is created, its mount point list is initialized as follows:</p>
<dl>
<dt>*</p>
<dd>If the namespace is created using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), the mount point list of the child&#8217;s namespace is a copy of the mount point list in the parent&#8217;s namespace.</p>
<dt>*</p>
<dd>If the namespace is created using <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), the mount point list of the new namespace is a copy of the mount point list in the caller&#8217;s previous mount namespace.</dl>
<p> Subsequent modifications to the mount point list (<code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) and <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2)) in either mount namespace will not (by default) affect the mount point list seen in the other namespace (but see the following discussion of shared subtrees).</p>
<h3>Restrictions on mount namespaces</h3>
<p>Note the following points with respect to mount namespaces:</p>
<dl>
<dt>*</p>
<dd>Each mount namespace has an owner user namespace. As explained above, when a new mount namespace is created, its mount point list is initialized as a copy of the mount point list of another mount namespace. If the new namespace and the namespace from which the mount point list was copied are owned by different user namespaces, then the new mount namespace is considered <i>less privileged</i>.</p>
<dt>*</p>
<dd>When creating a less privileged mount namespace, shared mounts are reduced to slave mounts. (Shared and slave mounts are discussed below.) This ensures that mappings performed in less privileged mount namespaces will not propagate to more privileged mount namespaces.</p>
<dt>*</p>
<dd>Mounts that come as a single unit from a more privileged mount namespace are locked together and may not be separated in a less privileged mount namespace. (The <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) <code>CLONE_NEWNS</code> operation brings across all of the mounts from the original mount namespace as a single unit, and recursive mounts that propagate between mount namespaces propagate as a single unit.)</p>
<dt>*</p>
<dd>The <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) flags <code>MS_RDONLY</code>, <code>MS_NOSUID</code>, <code>MS_NOEXEC</code>, and the &quot;atime&quot; flags (<code>MS_NOATIME</code>, <code>MS_NODIRATIME</code>, <code>MS_RELATIME</code>) settings become locked when propagated from a more privileged to a less privileged mount namespace, and may not be changed in the less privileged mount namespace.</p>
<dt>*</p>
<dd>A file or directory that is a mount point in one namespace that is not a mount point in another namespace, may be renamed, unlinked, or removed (<code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2)) in the mount namespace in which it is not a mount point (subject to the usual permission checks). Consequently, the mount point is removed in the mount namespace where it was a mount point.</p>
<dd>Previously (before Linux 3.18), attempting to unlink, rename, or remove a file or directory that was a mount point in another mount namespace would result in the error <code>EBUSY</code>. That behavior had technical problems of enforcement (e.g., for NFS) and permitted denial-of-service attacks against more privileged users. (i.e., preventing individual files from being updated by bind mounting on top of them).</dl>
<h2>Shared Subtrees</h2>
<p>After the implementation of mount namespaces was completed, experience showed that the isolation that they provided was, in some cases, too great. For example, in order to make a newly loaded optical disk available in all mount namespaces, a mount operation was required in each namespace. For this use case, and others, the shared subtree feature was introduced in Linux 2.6.15. This feature allows for automatic, controlled propagation of mount and unmount <i>events</i> between namespaces (or, more precisely, between the members of a <i>peer group</i> that are propagating events to one another). </p>
<p> Each mount point is marked (via <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2)) as having one of the following <i>propagation types</i>:</p>
<dl>
<dt><code>MS_SHARED</code></p>
<dd>This mount point shares events with members of a peer group. Mount and unmount events immediately under this mount point will propagate to the other mount points that are members of the peer group. <i>Propagation</i> here means that the same mount or unmount will automatically occur under all of the other mount points in the peer group. Conversely, mount and unmount events that take place under peer mount points will propagate to this mount point.</p>
<dt><code>MS_PRIVATE</code></p>
<dd>This mount point is private; it does not have a peer group. Mount and unmount events do not propagate into or out of this mount point.</p>
<dt><code>MS_SLAVE</code></p>
<dd>Mount and unmount events propagate into this mount point from a (master) shared peer group. Mount and unmount events under this mount point do not propagate to any peer.</p>
<dd>Note that a mount point can be the slave of another peer group while at the same time sharing mount and unmount events with a peer group of which it is a member. (More precisely, one peer group can be the slave of another peer group.)</p>
<dt><code>MS_UNBINDABLE</code></p>
<dd>This is like a private mount, and in addition this mount can&#8217;t be bind mounted. Attempts to bind mount this mount (<code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) with the <code>MS_BIND</code> flag) will fail.</p>
<dd>When a recursive bind mount (<code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) with the <code>MS_BIND</code> and <code>MS_REC</code> flags) is performed on a directory subtree, any bind mounts within the subtree are automatically pruned (i.e., not replicated) when replicating that subtree to produce the target subtree.</dl>
<p> For a discussion of the propagation type assigned to a new mount, see NOTES. </p>
<p> The propagation type is a per-mount-point setting; some mount points may be marked as shared (with each shared mount point being a member of a distinct peer group), while others are private (or slaved or unbindable). </p>
<p> Note that a mount&#8217;s propagation type determines whether mounts and unmounts of mount points <i>immediately under</i> the mount point are propagated. Thus, the propagation type does not affect propagation of events for grandchildren and further removed descendant mount points. What happens if the mount point itself is unmounted is determined by the propagation type that is in effect for the <i>parent</i> of the mount point. </p>
<p> Members are added to a <i>peer group</i> when a mount point is marked as shared and either:</p>
<dl>
<dt>*</p>
<dd>the mount point is replicated during the creation of a new mount namespace; or</p>
<dt>*</p>
<dd>a new bind mount is created from the mount point.</dl>
<p> In both of these cases, the new mount point joins the peer group of which the existing mount point is a member. </p>
<p> A new peer group is also created when a child mount point is created under an existing mount point that is marked as shared. In this case, the new child mount point is also marked as shared and the resulting peer group consists of all the mount points that are replicated under the peers of parent mount. </p>
<p> A mount ceases to be a member of a peer group when either the mount is explicitly unmounted, or when the mount is implicitly unmounted because a mount namespace is removed (because it has no more member processes). </p>
<p> The propagation type of the mount points in a mount namespace can be discovered via the &quot;optional fields&quot; exposed in <i>/proc/[pid]/mountinfo</i>. (See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for details of this file.) The following tags can appear in the optional fields for a record in that file:</p>
<dl>
<dt><i>shared:X</i></p>
<dd>This mount point is shared in peer group <i>X</i>. Each peer group has a unique ID that is automatically generated by the kernel, and all mount points in the same peer group will show the same ID. (These IDs are assigned starting from the value 1, and may be recycled when a peer group ceases to have any members.)</p>
<dt><i>master:X</i></p>
<dd>This mount is a slave to shared peer group <i>X</i>.</p>
<dt><i>propagate_from:X</i> (since Linux 2.6.26)</p>
<dd>This mount is a slave and receives propagation from shared peer group <i>X</i>. This tag will always appear in conjunction with a <i>master:X</i> tag. Here, <i>X</i> is the closest dominant peer group under the process&#8217;s root directory. If <i>X</i> is the immediate master of the mount, or if there is no dominant peer group under the same root, then only the <i>master:X</i> field is present and not the <i>propagate_from:X</i> field. For further details, see below.</p>
<dt><i>unbindable</i></p>
<dd>This is an unbindable mount.</dl>
<p> If none of the above tags is present, then this is a private mount.</p>
<h3>MS_SHARED and MS_PRIVATE example</h3>
<p>Suppose that on a terminal in the initial mount namespace, we mark one mount point as shared and another as private, and then view the mounts in <i>/proc/self/mountinfo</i>: </p>
<p> sh1# <code>mount &#8211;make-shared /mntS</code> sh1# <code>mount &#8211;make-private /mntP</code> sh1# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 77 61 8:17 / /mntS rw,relatime shared:1 83 61 8:15 / /mntP rw,relatime </p>
<p> From the <i>/proc/self/mountinfo</i> output, we see that <i>/mntS</i> is a shared mount in peer group 1, and that <i>/mntP</i> has no optional tags, indicating that it is a private mount. The first two fields in each record in this file are the unique ID for this mount, and the mount ID of the parent mount. We can further inspect this file to see that the parent mount point of <i>/mntS</i> and <i>/mntP</i> is the root directory, <i>/</i>, which is mounted as private: </p>
<p> sh1# <code>cat /proc/self/mountinfo | awk &#8216;$1 == 61&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 61 0 8:2 / / rw,relatime </p>
<p> On a second terminal, we create a new mount namespace where we run a second shell and inspect the mounts: </p>
<p> $ <code>PS1=&#8217;sh2# &#8216; sudo unshare -m &#8211;propagation unchanged sh</code> sh2# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 222 145 8:17 / /mntS rw,relatime shared:1 225 145 8:15 / /mntP rw,relatime </p>
<p> The new mount namespace received a copy of the initial mount namespace&#8217;s mount points. These new mount points maintain the same propagation types, but have unique mount IDs. (The <i>&#8211;propagation unchanged</i> option prevents <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) from marking all mounts as private when creating a new mount namespace, which it does by default.) </p>
<p> In the second terminal, we then create submounts under each of <i>/mntS</i> and <i>/mntP</i> and inspect the set-up: </p>
<p> sh2# <code>mkdir /mntS/a</code> sh2# <code>mount /dev/sdb6 /mntS/a</code> sh2# <code>mkdir /mntP/b</code> sh2# <code>mount /dev/sdb7 /mntP/b</code> sh2# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 222 145 8:17 / /mntS rw,relatime shared:1 225 145 8:15 / /mntP rw,relatime 178 222 8:22 / /mntS/a rw,relatime shared:2 230 225 8:23 / /mntP/b rw,relatime </p>
<p> From the above, it can be seen that <i>/mntS/a</i> was created as shared (inheriting this setting from its parent mount) and <i>/mntP/b</i> was created as a private mount. </p>
<p> Returning to the first terminal and inspecting the set-up, we see that the new mount created under the shared mount point <i>/mntS</i> propagated to its peer mount (in the initial mount namespace), but the new mount created under the private mount point <i>/mntP</i> did not propagate: </p>
<p> sh1# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 77 61 8:17 / /mntS rw,relatime shared:1 83 61 8:15 / /mntP rw,relatime 179 77 8:22 / /mntS/a rw,relatime shared:2</p>
<h3>MS_SLAVE example</h3>
<p>Making a mount point a slave allows it to receive propagated mount and unmount events from a master shared peer group, while preventing it from propagating events to that master. This is useful if we want to (say) receive a mount event when an optical disk is mounted in the master shared peer group (in another mount namespace), but want to prevent mount and unmount events under the slave mount from having side effects in other namespaces. </p>
<p> We can demonstrate the effect of slaving by first marking two mount points as shared in the initial mount namespace: </p>
<p> sh1# <code>mount &#8211;make-shared /mntX</code> sh1# <code>mount &#8211;make-shared /mntY</code> sh1# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 132 83 8:23 / /mntX rw,relatime shared:1 133 83 8:22 / /mntY rw,relatime shared:2 </p>
<p> On a second terminal, we create a new mount namespace and inspect the mount points: </p>
<p> sh2# <code>unshare -m &#8211;propagation unchanged sh</code> sh2# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 168 167 8:23 / /mntX rw,relatime shared:1 169 167 8:22 / /mntY rw,relatime shared:2 </p>
<p> In the new mount namespace, we then mark one of the mount points as a slave: </p>
<p> sh2# <code>mount &#8211;make-slave /mntY</code> sh2# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 168 167 8:23 / /mntX rw,relatime shared:1 169 167 8:22 / /mntY rw,relatime master:2 </p>
<p> From the above output, we see that <i>/mntY</i> is now a slave mount that is receiving propagation events from the shared peer group with the ID 2. </p>
<p> Continuing in the new namespace, we create submounts under each of <i>/mntX</i> and <i>/mntY</i>: </p>
<p> sh2# <code>mkdir /mntX/a</code> sh2# <code>mount /dev/sda3 /mntX/a</code> sh2# <code>mkdir /mntY/b</code> sh2# <code>mount /dev/sda5 /mntY/b</code> </p>
<p> When we inspect the state of the mount points in the new mount namespace, we see that <i>/mntX/a</i> was created as a new shared mount (inheriting the &quot;shared&quot; setting from its parent mount) and <i>/mntY/b</i> was created as a private mount: </p>
<p> sh2# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 168 167 8:23 / /mntX rw,relatime shared:1 169 167 8:22 / /mntY rw,relatime master:2 173 168 8:3 / /mntX/a rw,relatime shared:3 175 169 8:5 / /mntY/b rw,relatime </p>
<p> Returning to the first terminal (in the initial mount namespace), we see that the mount <i>/mntX/a</i> propagated to the peer (the shared <i>/mntX</i>), but the mount <i>/mntY/b</i> was not propagated: </p>
<p> sh1# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 132 83 8:23 / /mntX rw,relatime shared:1 133 83 8:22 / /mntY rw,relatime shared:2 174 132 8:3 / /mntX/a rw,relatime shared:3 </p>
<p> Now we create a new mount point under <i>/mntY</i> in the first shell: </p>
<p> sh1# <code>mkdir /mntY/c</code> sh1# <code>mount /dev/sda1 /mntY/c</code> sh1# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 132 83 8:23 / /mntX rw,relatime shared:1 133 83 8:22 / /mntY rw,relatime shared:2 174 132 8:3 / /mntX/a rw,relatime shared:3 178 133 8:1 / /mntY/c rw,relatime shared:4 </p>
<p> When we examine the mount points in the second mount namespace, we see that in this case the new mount has been propagated to the slave mount point, and that the new mount is itself a slave mount (to peer group 4): </p>
<p> sh2# <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 168 167 8:23 / /mntX rw,relatime shared:1 169 167 8:22 / /mntY rw,relatime master:2 173 168 8:3 / /mntX/a rw,relatime shared:3 175 169 8:5 / /mntY/b rw,relatime 179 169 8:1 / /mntY/c rw,relatime master:4</p>
<h3>MS_UNBINDABLE example</h3>
<p>One of the primary purposes of unbindable mounts is to avoid the &quot;mount point explosion&quot; problem when repeatedly performing bind mounts of a higher-level subtree at a lower-level mount point. The problem is illustrated by the following shell session. </p>
<p> Suppose we have a system with the following mount points: </p>
<p> # <code>mount | awk &#8216;{print $1, $2, $3}&#8217;</code> /dev/sda1 on / /dev/sdb6 on /mntX /dev/sdb7 on /mntY </p>
<p> Suppose furthermore that we wish to recursively bind mount the root directory under several users&#8217; home directories. We do this for the first user, and inspect the mount points: </p>
<p> # <code>mount &#8211;rbind / /home/cecilia/</code> # <code>mount | awk &#8216;{print $1, $2, $3}&#8217;</code> /dev/sda1 on / /dev/sdb6 on /mntX /dev/sdb7 on /mntY /dev/sda1 on /home/cecilia /dev/sdb6 on /home/cecilia/mntX /dev/sdb7 on /home/cecilia/mntY </p>
<p> When we repeat this operation for the second user, we start to see the explosion problem: </p>
<p> # <code>mount &#8211;rbind / /home/henry</code> # <code>mount | awk &#8216;{print $1, $2, $3}&#8217;</code> /dev/sda1 on / /dev/sdb6 on /mntX /dev/sdb7 on /mntY /dev/sda1 on /home/cecilia /dev/sdb6 on /home/cecilia/mntX /dev/sdb7 on /home/cecilia/mntY /dev/sda1 on /home/henry /dev/sdb6 on /home/henry/mntX /dev/sdb7 on /home/henry/mntY /dev/sda1 on /home/henry/home/cecilia /dev/sdb6 on /home/henry/home/cecilia/mntX /dev/sdb7 on /home/henry/home/cecilia/mntY </p>
<p> Under <i>/home/henry</i>, we have not only recursively added the <i>/mntX</i> and <i>/mntY</i> mounts, but also the recursive mounts of those directories under <i>/home/cecilia</i> that were created in the previous step. Upon repeating the step for a third user, it becomes obvious that the explosion is exponential in nature: </p>
<p> # <code>mount &#8211;rbind / /home/otto</code> # <code>mount | awk &#8216;{print $1, $2, $3}&#8217;</code> /dev/sda1 on / /dev/sdb6 on /mntX /dev/sdb7 on /mntY /dev/sda1 on /home/cecilia /dev/sdb6 on /home/cecilia/mntX /dev/sdb7 on /home/cecilia/mntY /dev/sda1 on /home/henry /dev/sdb6 on /home/henry/mntX /dev/sdb7 on /home/henry/mntY /dev/sda1 on /home/henry/home/cecilia /dev/sdb6 on /home/henry/home/cecilia/mntX /dev/sdb7 on /home/henry/home/cecilia/mntY /dev/sda1 on /home/otto /dev/sdb6 on /home/otto/mntX /dev/sdb7 on /home/otto/mntY /dev/sda1 on /home/otto/home/cecilia /dev/sdb6 on /home/otto/home/cecilia/mntX /dev/sdb7 on /home/otto/home/cecilia/mntY /dev/sda1 on /home/otto/home/henry /dev/sdb6 on /home/otto/home/henry/mntX /dev/sdb7 on /home/otto/home/henry/mntY /dev/sda1 on /home/otto/home/henry/home/cecilia /dev/sdb6 on /home/otto/home/henry/home/cecilia/mntX /dev/sdb7 on /home/otto/home/henry/home/cecilia/mntY </p>
<p> The mount explosion problem in the above scenario can be avoided by making each of the new mounts unbindable. The effect of doing this is that recursive mounts of the root directory will not replicate the unbindable mounts. We make such a mount for the first user: </p>
<p> # <code>mount &#8211;rbind &#8211;make-unbindable / /home/cecilia</code> </p>
<p> Before going further, we show that unbindable mounts are indeed unbindable: </p>
<p> # <code>mkdir /mntZ</code> # <code>mount &#8211;bind /home/cecilia /mntZ</code> mount: wrong fs type, bad option, bad superblock on /home/cecilia,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;missing codepage or helper program, or other error </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;In some cases useful info is found in syslog &#8211; try<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dmesg | tail or so. </p>
<p> Now we create unbindable recursive bind mounts for the other two users: </p>
<p> # <code>mount &#8211;rbind &#8211;make-unbindable / /home/henry</code> # <code>mount &#8211;rbind &#8211;make-unbindable / /home/otto</code> </p>
<p> Upon examining the list of mount points, we see there has been no explosion of mount points, because the unbindable mounts were not replicated under each user&#8217;s directory: </p>
<p> # <code>mount | awk &#8216;{print $1, $2, $3}&#8217;</code> /dev/sda1 on / /dev/sdb6 on /mntX /dev/sdb7 on /mntY /dev/sda1 on /home/cecilia /dev/sdb6 on /home/cecilia/mntX /dev/sdb7 on /home/cecilia/mntY /dev/sda1 on /home/henry /dev/sdb6 on /home/henry/mntX /dev/sdb7 on /home/henry/mntY /dev/sda1 on /home/otto /dev/sdb6 on /home/otto/mntX /dev/sdb7 on /home/otto/mntY</p>
<h3>Propagation type transitions</h3>
<p>The following table shows the effect that applying a new propagation type (i.e., <i>mount &#8211;make-xxxx)</i> has on the existing propagation type of a mount point. The rows correspond to existing propagation types, and the columns are the new propagation settings. For reasons of space, &quot;private&quot; is abbreviated as &quot;priv&quot; and &quot;unbindable&quot; as &quot;unbind&quot;. </p>
<table>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td><code>make-shared&nbsp;<wbr>&nbsp;</code></td>
<td><code>make-slave&nbsp;<wbr>&nbsp;</code></td>
<td><code>make-priv&nbsp;<wbr>&nbsp;</code></td>
<td><code>make-unbind&nbsp;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>shared</code></td>
<td>shared</td>
<td>slave/priv [1]</td>
<td>priv</td>
<td>unbind
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>slave</code></td>
<td>slave+shared</td>
<td>slave [2]</td>
<td>priv</td>
<td>unbind
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>slave+shared</code></td>
<td>slave+shared</td>
<td>slave</td>
<td>priv</td>
<td>unbind
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>private</code></td>
<td>shared</td>
<td>priv [2]</td>
<td>priv</td>
<td>unbind
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>unbindable</code></td>
<td>shared</td>
<td>unbind [2]</td>
<td>priv</td>
<td>unbind
</td>
<td>
</td>
</tr>
</table>
<p> Note the following details to the table:</p>
<dl>
<dt>[1]</p>
<dd>If a shared mount is the only mount in its peer group, making it a slave automatically makes it private.</p>
<dt>[2]</p>
<dd>Slaving a nonshared mount has no effect on the mount.</dl>
<h3>Bind (MS_BIND) semantics</h3>
<p>Suppose that the following command is performed: </p>
<p> mount &#8211;bind A/a B/b </p>
<p> Here, <i>A</i> is the source mount point, <i>B</i> is the destination mount point, <i>a</i> is a subdirectory path under the mount point <i>A</i>, and <i>b</i> is a subdirectory path under the mount point <i>B</i>. The propagation type of the resulting mount, <i>B/b</i>, depends on the propagation types of the mount points <i>A</i> and <i>B</i>, and is summarized in the following table. </p>
<table>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td><code>&nbsp;</code></td>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td><code>source(A)&nbsp;<wbr>&nbsp;</code></td>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td><code>&nbsp;</code></td>
<td><code>shared&nbsp;<wbr>&nbsp;</code></td>
<td><code>private&nbsp;<wbr>&nbsp;</code></td>
<td><code>slave&nbsp;<wbr>&nbsp;</code></td>
<td><code>unbind</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>dest(B)</code></td>
<td><code>shared</code></td>
<td>shared</td>
<td>shared</td>
<td>slave+shared</td>
<td>invalid
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>nonshared</code></td>
<td>shared</td>
<td>private</td>
<td>slave</td>
<td>invalid
</td>
<td>
</td>
</tr>
</table>
<p> Note that a recursive bind of a subtree follows the same semantics as for a bind operation on each mount in the subtree. (Unbindable mounts are automatically pruned at the target mount point.) </p>
<p> For further details, see <i>Documentation/filesystems/sharedsubtree.txt</i> in the kernel source tree.</p>
<h3>Move (MS_MOVE) semantics</h3>
<p>Suppose that the following command is performed: </p>
<p> mount &#8211;move A B/b </p>
<p> Here, <i>A</i> is the source mount point, <i>B</i> is the destination mount point, and <i>b</i> is a subdirectory path under the mount point <i>B</i>. The propagation type of the resulting mount, <i>B/b</i>, depends on the propagation types of the mount points <i>A</i> and <i>B</i>, and is summarized in the following table. </p>
<table>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td><code>&nbsp;</code></td>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td><code>source(A)&nbsp;<wbr>&nbsp;</code></td>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>&nbsp;</code></td>
<td><code>&nbsp;</code></td>
<td><code>shared&nbsp;<wbr>&nbsp;</code></td>
<td><code>private&nbsp;<wbr>&nbsp;</code></td>
<td><code>slave&nbsp;<wbr>&nbsp;</code></td>
<td><code>unbind</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>dest(B)</code></td>
<td><code>shared</code></td>
<td>shared</td>
<td>shared</td>
<td>slave+shared</td>
<td>invalid
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>nonshared</code></td>
<td>shared</td>
<td>private</td>
<td>slave</td>
<td>unbindable
</td>
<td>
</td>
</tr>
</table>
<p> Note: moving a mount that resides under a shared mount is invalid. </p>
<p> For further details, see <i>Documentation/filesystems/sharedsubtree.txt</i> in the kernel source tree.</p>
<h3>Mount semantics</h3>
<p>Suppose that we use the following command to create a mount point: </p>
<p> mount device B/b </p>
<p> Here, <i>B</i> is the destination mount point, and <i>b</i> is a subdirectory path under the mount point <i>B</i>. The propagation type of the resulting mount, <i>B/b</i>, follows the same rules as for a bind mount, where the propagation type of the source mount is considered always to be private.</p>
<h3>Unmount semantics</h3>
<p>Suppose that we use the following command to tear down a mount point: </p>
<p> unmount A </p>
<p> Here, <i>A</i> is a mount point on <i>B/b</i>, where <i>B</i> is the parent mount and <i>b</i> is a subdirectory path under the mount point <i>B</i>. If <code>B</code> is shared, then all most-recently-mounted mounts at <i>b</i> on mounts that receive propagation from mount <i>B</i> and do not have submounts under them are unmounted.</p>
<h3>The /proc/[pid]/mountinfo propagate_from tag</h3>
<p>The <i>propagate_from:X</i> tag is shown in the optional fields of a <i>/proc/[pid]/mountinfo</i> record in cases where a process can&#8217;t see a slave&#8217;s immediate master (i.e., the pathname of the master is not reachable from the filesystem root directory) and so cannot determine the chain of propagation between the mounts it can see. </p>
<p> In the following example, we first create a two-link master-slave chain between the mounts <i>/mnt</i>, <i>/tmp/etc</i>, and <i>/mnt/tmp/etc</i>. Then the <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1) command is used to make the <i>/tmp/etc</i> mount point unreachable from the root directory, creating a situation where the master of <i>/mnt/tmp/etc</i> is not reachable from the (new) root directory of the process. </p>
<p> First, we bind mount the root directory onto <i>/mnt</i> and then bind mount <i>/proc</i> at <i>/mnt/proc</i> so that after the later <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1) the <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) filesystem remains visible at the correct location in the chroot-ed environment. </p>
<p> # <code>mkdir -p /mnt/proc</code> # <code>mount &#8211;bind / /mnt</code> # <code>mount &#8211;bind /proc /mnt/proc</code> </p>
<p> Next, we ensure that the <i>/mnt</i> mount is a shared mount in a new peer group (with no peers): </p>
<p> # <code>mount &#8211;make-private /mnt</code> # Isolate from any previous peer group # <code>mount &#8211;make-shared /mnt</code> # <code>cat /proc/self/mountinfo | grep &#8216;/mnt&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 239 61 8:2 / /mnt &#8230; shared:102 248 239 0:4 / /mnt/proc &#8230; shared:5 </p>
<p> Next, we bind mount <i>/mnt/etc</i> onto <i>/tmp/etc</i>: </p>
<p> # <code>mkdir -p /tmp/etc</code> # <code>mount &#8211;bind /mnt/etc /tmp/etc</code> # <code>cat /proc/self/mountinfo | egrep &#8216;/mnt|/tmp/&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 239 61 8:2 / /mnt &#8230; shared:102 248 239 0:4 / /mnt/proc &#8230; shared:5 267 40 8:2 /etc /tmp/etc &#8230; shared:102 </p>
<p> Initially, these two mount points are in the same peer group, but we then make the <i>/tmp/etc</i> a slave of <i>/mnt/etc</i>, and then make <i>/tmp/etc</i> shared as well, so that it can propagate events to the next slave in the chain: </p>
<p> # <code>mount &#8211;make-slave /tmp/etc</code> # <code>mount &#8211;make-shared /tmp/etc</code> # <code>cat /proc/self/mountinfo | egrep &#8216;/mnt|/tmp/&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 239 61 8:2 / /mnt &#8230; shared:102 248 239 0:4 / /mnt/proc &#8230; shared:5 267 40 8:2 /etc /tmp/etc &#8230; shared:105 master:102 </p>
<p> Then we bind mount <i>/tmp/etc</i> onto <i>/mnt/tmp/etc</i>. Again, the two mount points are initially in the same peer group, but we then make <i>/mnt/tmp/etc</i> a slave of <i>/tmp/etc</i>: </p>
<p> # <code>mkdir -p /mnt/tmp/etc</code> # <code>mount &#8211;bind /tmp/etc /mnt/tmp/etc</code> # <code>mount &#8211;make-slave /mnt/tmp/etc</code> # <code>cat /proc/self/mountinfo | egrep &#8216;/mnt|/tmp/&#8217; | sed &#8216;s/ &#8211; .*//&#8217;</code> 239 61 8:2 / /mnt &#8230; shared:102 248 239 0:4 / /mnt/proc &#8230; shared:5 267 40 8:2 /etc /tmp/etc &#8230; shared:105 master:102 273 239 8:2 /etc /mnt/tmp/etc &#8230; master:105 </p>
<p> From the above, we see that <i>/mnt</i> is the master of the slave <i>/tmp/etc</i>, which in turn is the master of the slave <i>/mnt/tmp/etc</i>. </p>
<p> We then <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1) to the <i>/mnt</i> directory, which renders the mount with ID 267 unreachable from the (new) root directory: </p>
<p> # <code>chroot /mnt</code> </p>
<p> When we examine the state of the mounts inside the chroot-ed environment, we see the following: </p>
<p> # <code>cat /proc/self/mountinfo | sed &#8216;s/ &#8211; .*//&#8217;</code> 239 61 8:2 / / &#8230; shared:102 248 239 0:4 / /proc &#8230; shared:5 273 239 8:2 /etc /tmp/etc &#8230; master:105 propagate_from:102 </p>
<p> Above, we see that the mount with ID 273 is a slave whose master is the peer group 105. The mount point for that master is unreachable, and so a <i>propagate_from</i> tag is displayed, indicating that the closest dominant peer group (i.e., the nearest reachable mount in the slave chain) is the peer group with the ID 102 (corresponding to the <i>/mnt</i> mount point before the <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1) was performed.</p>
<h2>Versions</h2>
<p>Mount namespaces first appeared in Linux 2.4.19.</p>
<h2>Conforming To</h2>
<p>Namespaces are a Linux-specific feature.</p>
<h2>Notes</h2>
<p>The propagation type assigned to a new mount point depends on the propagation type of the parent mount. If the mount point has a parent (i.e., it is a non-root mount point) and the propagation type of the parent is <code>MS_SHARED</code>, then the propagation type of the new mount is also <code>MS_SHARED</code>. Otherwise, the propagation type of the new mount is <code>MS_PRIVATE</code>. </p>
<p> Notwithstanding the fact that the default propagation type for new mount points is in many cases <code>MS_PRIVATE</code>, <code>MS_SHARED</code> is typically more useful. For this reason, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) automatically remounts all mount points as <code>MS_SHARED</code> on system startup. Thus, on most modern systems, the default propagation type is in practice <code>MS_SHARED</code>. </p>
<p> Since, when one uses <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) to create a mount namespace, the goal is commonly to provide full isolation of the mount points in the new namespace, <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) (since <i>util-linux</i> version 2.27) in turn reverses the step performed by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), by making all mount points private in the new namespace. That is, <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) performs the equivalent of the following in the new mount namespace: </p>
<p> mount &#8211;make-rprivate / </p>
<p> To prevent this, one can use the <i>&#8211;propagation unchanged</i> option to <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1). </p>
<p> An application that creates a new mount namespace directly using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) may desire to prevent propagation of mount events to other mount namespaces (as is done by <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1)). This can be done by changing the propagation type of mount points in the new namespace to either <code>MS_SLAVE</code> or <code>MS_PRIVATE</code>. using a call such as the following: </p>
<p> mount(NULL, &quot;/&quot;, MS_SLAVE | MS_REC, NULL); </p>
<p> For a discussion of propagation types when moving mounts (<code>MS_MOVE</code>) and creating bind mounts (<code>MS_BIND</code>), see <i>Documentation/filesystems/sharedsubtree.txt</i>.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-findmnt/">findmnt</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) </p>
<p> <i>Documentation/filesystems/sharedsubtree.txt</i> in the kernel source tree.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
