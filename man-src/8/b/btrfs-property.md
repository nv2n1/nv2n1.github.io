---
title: "btrfs-property(8)"
name: "btrfs-property"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-property/"
description: "btrfs-property – get/set/list properties for given filesystem object"
---

<p>btrfs-property &#8211; get/set/list properties for given filesystem object</p>
<h2>Synopsis</h2>
<p><code>btrfs property</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs property</code> is used to get/set/list property for given filesystem object. The object can be an inode (file or directory), subvolume or the whole filesystem. See the description of <code>get</code> subcommand for more information about both btrfs object and property. </p>
<p> <code>btrfs property</code> provides an unified and user-friendly method to tune different btrfs properties instead of using the traditional method like <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) or <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1).</p>
<h2>Subcommand</h2>
<p><code>get</code> [-t <i>&lt;type&gt;</i>] <i>&lt;object&gt;</i> [<i>&lt;name&gt;</i>]</p>
<dl>
<dd>get property from a btrfs <i>&lt;object&gt;</i> of given <i>&lt;type&gt;</i> </p>
<p> A btrfs object, which is set by <i>&lt;object&gt;</i>, can be a btrfs filesystem itself, a btrfs subvolume, an inode (file or directory) inside btrfs, or a device on which a btrfs exists. </p>
<p> The option <i>-t</i> can be used to explicitly specify what type of object you meant. This is only needed when a property could be set for more then one object type. </p>
<p> Possible types are <i>s[ubvol]</i>, <i>f[ilesystem]</i>, <i>i[node]</i> and <i>d[evice]</i>, where the first lettes is a shortcut. </p>
<p> Set the name of property by <i>name</i>. If no <i>name</i> is specified, all properties for the given object are printed. <i>name</i> is one of the following: </p>
<p> ro</p>
<dl>
<dd>read-only flag of subvolume: true or false</dl>
<p> label</p>
<dl>
<dd>label of the filesystem. For an unmounted filesystem, provide a path to a block device as object. For a mounted filesystem, specify a mount point.</dl>
<p> compression</p>
<dl>
<dd>compression algorithm set for an inode, possible values: <i>lzo</i>, <i>zlib</i>, <i>zstd</i>. To disable compression use &quot;&quot; (empty string), <i>no</i> or <i>none</i>.</dl>
</dl>
<p> <code>list</code> [-t <i>&lt;type&gt;</i>] <i>&lt;object&gt;</i></p>
<dl>
<dd>Lists available properties with their descriptions for the given object. </p>
<p> See the description of <code>get</code> subcommand for the meaning of each option.</dl>
<p> <code>set</code> [-t <i>&lt;type&gt;</i>] <i>&lt;object&gt;</i> <i>&lt;name&gt;</i> <i>&lt;value&gt;</i></p>
<dl>
<dd>Sets a property on a btrfs object. </p>
<p> See the description of <code>get</code> subcommand for the meaning of each option.</dl>
<h2>Exit Status</h2>
<p><code>btrfs property</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1), <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) </p>
