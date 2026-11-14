---
title: "btrfs-qgroup(8)"
name: "btrfs-qgroup"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-qgroup/"
description: "btrfs-qgroup – control the quota group of a btrfs filesystem"
---

<p>btrfs-qgroup &#8211; control the quota group of a btrfs filesystem</p>
<h2>Synopsis</h2>
<p><code>btrfs qgroup</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs qgroup</code> is used to control quota group (qgroup) of a btrfs filesystem.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 To use qgroup you need to enable quota first using <code>btrfs quota enable</code> command. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Qgroup is not stable yet and will impact performance in current mainline kernel (v4.14). </p>
<h2>Qgroup</h2>
<p>Quota groups or qgroup in btrfs make a tree hierarchy, the leaf qgroups are attached to subvolumes. The size limits are set per qgroup and apply when any limit is reached in tree that contains a given subvolume. </p>
<p> The limits are separated between shared and exclusive and reflect the extent ownership. For example a fresh snapshot shares almost all the blocks with the original subvolume, new writes to either subvolume will raise towards the exclusive limit. </p>
<p> The qgroup identifiers conform to <i>level/id</i> where level 0 is reserved to the qgroups associated with subvolumes. Such qgroups are created automatically. </p>
<p> The qgroup hierarchy is built by commands <code>create</code> and <code>assign</code>. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> If the qgroup of a subvolume is destroyed, quota about the subvolume will not be functional until qgroup <i>0/</i><i>&lt;subvolume id&gt;</i> is created again. </p>
</dl>
<h2>Subcommand</h2>
<p><code>assign</code> [options] <i>&lt;src&gt;</i> <i>&lt;dst&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>Assign qgroup <i>&lt;src&gt;</i> as the child qgroup of <i>&lt;dst&gt;</i> in the btrfs filesystem identified by <i>&lt;path&gt;</i>. </p>
<p> <code>Options</code> </p>
<p> &#8211;rescan</p>
<dl>
<dd>(default since: 4.19) Automatically schedule quota rescan if the new qgroup assignment would lead to quota inconsistency. See <i>QUOTA RESCAN</i> for more information.</dl>
<p> &#8211;no-rescan</p>
<dl>
<dd>Explicitly ask not to do a rescan, even if the assignment will make the quotas inconsistent. This may be useful for repeated calls where the rescan would add unnecessary overhead.</dl>
</dl>
<p> <code>create</code> <i>&lt;qgroupid&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>Create a subvolume quota group. </p>
<p> For the <i>0/</i><i>&lt;subvolume id&gt;</i> qgroup, a qgroup can be created even before the subvolume is created.</dl>
<p> <code>destroy</code> <i>&lt;qgroupid&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>Destroy a qgroup. </p>
<p> If a qgroup is not isolated, meaning it is a parent or child qgroup, then it can only be destroyed after the relationship is removed.</dl>
<p> <code>limit</code> [options] <i>&lt;size&gt;</i>|none [<i>&lt;qgroupid&gt;</i>] <i>&lt;path&gt;</i></p>
<dl>
<dd>Limit the size of a qgroup to <i>&lt;size&gt;</i> or no limit in the btrfs filesystem identified by <i>&lt;path&gt;</i>. </p>
<p> If <i>&lt;qgroupid&gt;</i> is not given, qgroup of the subvolume identified by <i>&lt;path&gt;</i> is used if possible. </p>
<p> <code>Options</code> </p>
<p> -c</p>
<dl>
<dd>limit amount of data after compression. This is the default, it is currently not possible to turn off this option.</dl>
<p> -e</p>
<dl>
<dd>limit space exclusively assigned to this qgroup.</dl>
</dl>
<p> <code>remove</code> <i>&lt;src&gt;</i> <i>&lt;dst&gt;</i> <i>&lt;path&gt;</i></p>
<dl>
<dd>Remove the relationship between child qgroup <i>&lt;src&gt;</i> and parent qgroup <i>&lt;dst&gt;</i> in the btrfs filesystem identified by <i>&lt;path&gt;</i>. </p>
<p> <code>Options</code> </p>
<p> The same as <code>assign</code> subcommand.</dl>
<p> <code>show</code> [options] <i>&lt;path&gt;</i></p>
<dl>
<dd>Show all qgroups in the btrfs filesystem identified by <i>&lt;path&gt;</i>. </p>
<p> <code>Options</code> </p>
<p> -p</p>
<dl>
<dd>print parent qgroup id.</dl>
<p> -c</p>
<dl>
<dd>print child qgroup id.</dl>
<p> -r</p>
<dl>
<dd>print limit of referenced size of qgroup.</dl>
<p> -e</p>
<dl>
<dd>print limit of exclusive size of qgroup.</dl>
<p> -F</p>
<dl>
<dd>list all qgroups which impact the given path(include ancestral qgroups)</dl>
<p> -f</p>
<dl>
<dd>list all qgroups which impact the given path(exclude ancestral qgroups)</dl>
<p> &#8211;raw</p>
<dl>
<dd>raw numbers in bytes, without the <i>B</i> suffix.</dl>
<p> &#8211;human-readable</p>
<dl>
<dd>print human friendly numbers, base 1024, this is the default</dl>
<p> &#8211;iec</p>
<dl>
<dd>select the 1024 base for the following options, according to the IEC standard.</dl>
<p> &#8211;si</p>
<dl>
<dd>select the 1000 base for the following options, according to the SI standard.</dl>
<p> &#8211;kbytes</p>
<dl>
<dd>show sizes in KiB, or kB with &#8211;si.</dl>
<p> &#8211;mbytes</p>
<dl>
<dd>show sizes in MiB, or MB with &#8211;si.</dl>
<p> &#8211;gbytes</p>
<dl>
<dd>show sizes in GiB, or GB with &#8211;si.</dl>
<p> &#8211;tbytes</p>
<dl>
<dd>show sizes in TiB, or TB with &#8211;si.</dl>
<p> &#8211;sort=[+/-]<i>&lt;attr&gt;</i>[,[+/-]<i>&lt;attr&gt;</i>]&#8230;</p>
<dl>
<dd>list qgroups in order of <i>&lt;attr&gt;</i>. </p>
<p> <i>&lt;attr&gt;</i> can be one or more of qgroupid,rfer,excl,max_rfer,max_excl. </p>
<p> Prefix &#8216;+&#8217; means ascending order and &#8216;-&#8216; means descending order of <i>&lt;attr&gt;</i>. If no prefix is given, use ascending order by default. </p>
<p> If multiple <i>&lt;attr&gt;</i>s is given, use comma to separate.</dl>
<p> &#8211;sync</p>
<dl>
<dd>To retrieve information after updating the state of qgroups, force sync of the filesystem identified by <i>&lt;path&gt;</i> before getting information.</dl>
</dl>
<h2>Quota Rescan</h2>
<p>The rescan reads all extent sharing metadata and updates the respective qgoups accordingly. </p>
<p> The information consists of bytes owned exclusively (<i>excl</i>) or shared/referred to (<i>rfer</i>). There&#8217;s no explicit information about which extents are shared or owned exclusively. This means when qgroup relationship changes, extent owners change and qgroup numbers are no longer consistent unless we do a full rescan. </p>
<p> However there are cases where we can avoid a full rescan, if a subvolume whose <i>rfer</i> number equals its <i>excl</i> number, which means all bytes are exclusively owned, then assigning/removing this subvolume only needs to add/subtract <i>rfer</i> number from its parent qgroup. This can speed up the rescan.</p>
<h2>Exit Status</h2>
<p><code>btrfs qgroup</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-subvolume/">btrfs-subvolume</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-quota/">btrfs-quota</a></code>(8), </p>
