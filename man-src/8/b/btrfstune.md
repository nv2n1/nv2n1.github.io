---
title: "btrfstune(8)"
name: "btrfstune"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfstune/"
description: "btrfstune – tune various filesystem parameters"
---

<p>btrfstune &#8211; tune various filesystem parameters</p>
<h2>Synopsis</h2>
<p><code>btrfstune</code> [options] <i>&lt;device&gt;</i> [<i>&lt;device&gt;</i>&#8230;]</p>
<h2>Description</h2>
<p><code>btrfstune</code> can be used to enable, disable, or set various filesystem parameters. The filesystem must be unmounted. </p>
<p> The common usecase is to enable features that were not enabled at mkfs time. Please make sure that you have kernel support for the features. You can find a complete list of features and kernel version of their introduction at m[blue]<code><a rel="nofollow" href="https://btrfs.wiki.kernel.org/index.php/Changelog#By_feature">https://btrfs.wiki.kernel.org/index.php/Changelog#By_feature</a></code>m[] . Also, the manual page <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) contains more details about the features. </p>
<p> Some of the features could be also enabled on a mounted filesystem by other means. Please refer to the <i>FILESYSTEM FEATURES</i> in <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5).</p>
<h2>Options</h2>
<p>-f</p>
<dl>
<dd>Allow dangerous changes, e.g. clear the seeding flag or change fsid. Make sure that you are aware of the dangers.</dl>
<p> -m</p>
<dl>
<dd>(since kernel: 5.0) </p>
<p> change fsid stored as <i>metadata_uuid</i> to a randomly generated UUID, see also <i>-U</i></dl>
<p> -M <i>&lt;UUID&gt;</i></p>
<dl>
<dd>(since kernel: 5.0) </p>
<p> change fsid stored as <i>metadata_uuid</i> to a given UUID, see also <i>-U</i> </p>
<p> The metadata_uuid is stored only in the superblock and is a backward incompatible change. The fsid in metadata blocks remains unchanged and is not overwritten, thus the whole operation is significantly faster than <i>-U</i>. </p>
<p> The new metadata_uuid can be used for mount by UUID and is also used to identify devices of a multi-device filesystem.</dl>
<p> -n</p>
<dl>
<dd>(since kernel: 3.14) </p>
<p> Enable no-holes feature (more efficient representation of file holes), enabled by mkfs feature <i>no-holes</i>.</dl>
<p> -r</p>
<dl>
<dd>(since kernel: 3.7) </p>
<p> Enable extended inode refs (hardlink limit per file in a directory is 65536), enabled by mkfs feature <i>extref</i>.</dl>
<p> -S <i>&lt;0|1&gt;</i></p>
<dl>
<dd>Enable seeding on a given device. Value 1 will enable seeding, 0 will disable it. </p>
<p> A seeding filesystem is forced to be mounted read-only. A new device can be added to the filesystem and will capture all writes keeping the seeding device intact. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Clearing the seeding flag on a device may be dangerous. If a previously-seeding device is changed, all filesystems that used that device will become unmountable. Setting the seeding flag back will not fix that. </p>
<p> A valid usecase is <i>seeding device as a base image</i>. Clear the seeding flag, update the filesystem and make it seeding again, provided that it&#8217;s OK to throw away all filesystems built on top of the previous base. </p>
</dl>
</dl>
<p> -u</p>
<dl>
<dd>Change fsid to a randomly generated UUID or continue previous fsid change operation in case it was interrupted.</dl>
<p> -U <i>&lt;UUID&gt;</i></p>
<dl>
<dd>Change fsid to <i>UUID</i> in all metadata blocks. </p>
<p> The <i>UUID</i> should be a 36 bytes string in <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) format <i>&quot;%08x-%04x-%04x-%04x-%012x&quot;</i>. If there is a previous unfinished fsid change, it will continue only if the <i>UUID</i> matches the unfinished one or if you use the option <i>-u</i>. </p>
<p> All metadata blocks are rewritten, this may take some time, but the final filesystem compatibility is unaffected, unlike <i>-M</i>. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Cancelling or interrupting a UUID change operation will make the filesystem temporarily unmountable. To fix it, rerun <i>btrfstune -u</i> and let it complete. </p>
</dl>
</dl>
<p> -x</p>
<dl>
<dd>(since kernel: 3.10) </p>
<p> Enable skinny metadata extent refs (more efficient representation of extents), enabled by mkfs feature <i>skinny-metadata</i>. </p>
<p> All newly created extents will use the new representation. To completely switch the entire filesystem, run a full balance of the metadata. Please refer to <code><a href="/docs/linux/man/8-btrfs-balance/">btrfs-balance</a></code>(8).</dl>
<h2>Exit Status</h2>
<p><code>btrfstune</code> returns 0 if no error happened, 1 otherwise.</p>
<h2>Compatibility Note</h2>
<p>This deprecated tool exists for historical reasons but is still in use today. Its functionality will be merged to the main tool, at which time <code>btrfstune</code> will be declared obsolete and scheduled for removal.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/8-btrfs-balance/">btrfs-balance</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>
