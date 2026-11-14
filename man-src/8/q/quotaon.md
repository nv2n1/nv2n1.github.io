---
title: "quotaon(8)"
name: "quotaon"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quotaon/"
description: "quotaon, quotaoff – turn filesystem quotas on and off"
---

<p>quotaon, quotaoff &#8211; turn filesystem quotas on and off</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/quotaon</code> [ <code>-vugfp</code> ] [ <code>-F</code> <i>format-name</i> ] <i>filesystem</i>&#8230;<br />
 <code>/usr/sbin/quotaon</code> [ <code>-avugfp</code> ] [ <code>-F</code> <i>format-name</i> ] </p>
<p> <code>/usr/sbin/quotaoff</code> [ <code>-vugp</code> ] [ <code>-x</code> <i>state</i> ] <i>filesystem</i>&#8230;<br />
 <code>/usr/sbin/quotaoff</code> [ <code>-avugp</code> ]</p>
<h2>Description</h2>
<h3>quotaon</h3>
<p><code>quotaon</code> announces to the system that disk quotas should be enabled on one or more filesystems. The filesystem quota files must be present in the root directory of the specified filesystem and be named either <i>aquota.user</i> (for version 2 user quota), <i>quota.user</i> (for version 1 user quota), <i>aquota.group</i> (for version 2 group quota), or <i>quota.group</i> (for version 1 group quota). </p>
<p> XFS filesystems are a special case &#8211; XFS considers quota information as filesystem metadata and uses journaling to provide a higher level guarantee of consistency. There are two components to the XFS disk quota system: accounting and limit enforcement. XFS filesystems require that quota accounting be turned on at mount time. It is possible to enable and disable limit enforcement on an XFS filesystem after quota accounting is already turned on. The default is to turn on both accounting and enforcement. </p>
<p> The XFS quota implementation does not maintain quota information in user-visible files, but rather stores this information internally.</p>
<h3>quotaoff</h3>
<p><code>quotaoff</code> announces to the system that the specified filesystems should have any disk quotas turned off.</p>
<h2>Options</h2>
<h3>quotaon</h3>
<dl>
<dt><code>-F, &#8211;format=</code><i>format-name</i></p>
<dd>Report quota for specified format (ie. don&#8217;t perform format autodetection). Possible format names are: <code>vfsold</code> Original quota format with 16-bit UIDs / GIDs, <code>vfsv0</code> Quota format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode usage and limits, <code>vfsv1</code> Quota format with 64-bit quota limits and usage, <code>xfs</code> (quota on XFS filesystem)</p>
<dt><code>-a, &#8211;all</code></p>
<dd>All automatically mounted (no <code>noauto</code> option) non-NFS filesystems in <code>/etc/fstab</code> with quotas will have their quotas turned on. This is normally used at boot time to enable quotas.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Display a message for each filesystem where quotas are turned on.</p>
<dt><code>-u, &#8211;user</code></p>
<dd>Manipulate user quotas. This is the default.</p>
<dt><code>-g, &#8211;group</code></p>
<dd>Manipulate group quotas.</p>
<dt><code>-p, &#8211;print-state</code></p>
<dd>Instead of turning quotas on just print state of quotas (ie. whether. quota is on or off)</p>
<dt><code>-x, &#8211;xfs-command enforce</code></p>
<dd>Switch on limit enforcement for XFS filesystems. This is the default action for any XFS filesystem. This option is only applicable to XFS, and is silently ignored for other filesystem types.</p>
<dt><code>-f, &#8211;off</code></p>
<dd>Make <code>quotaon</code> behave like being called as <code>quotaoff</code>.</dl>
<h3>quotaoff</h3>
<dl>
<dt><code>-F, &#8211;format=</code><i>format-name</i></p>
<dd>Report quota for specified format (ie. don&#8217;t perform format autodetection). Possible format names are: <code>vfsold</code> (version 1 quota), <code>vfsv0</code> (version 2 quota), <code>xfs</code> (quota on XFS filesystem)</p>
<dt><code>-a, &#8211;all</code></p>
<dd>Force all filesystems in <code>/etc/fstab</code> to have their quotas disabled.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Display a message for each filesystem affected.</p>
<dt><code>-u, &#8211;user</code></p>
<dd>Manipulate user quotas. This is the default.</p>
<dt><code>-g, &#8211;group</code></p>
<dd>Manipulate group quotas.</p>
<dt><code>-p, &#8211;print-state</code></p>
<dd>Instead of turning quotas off just print state of quotas (ie. whether. quota is on or off)</p>
<dt><code>-x, &#8211;xfs-command delete</code></p>
<dd>Free up the space used to hold quota information (maintained internally) within XFS. This option is only applicable to XFS, and is silently ignored for other filesystem types. It can only be used on a filesystem with quota previously turned off.</p>
<dt><code>-x, &#8211;xfs-command enforce</code></p>
<dd>Switch off limit enforcement for XFS filesystems (perform quota accounting only). This is the default action for any XFS filesystem. This option is only applicable to XFS, and is silently ignored for other filesystem types.</p>
<dt><code>-x, &#8211;xfs-command account</code></p>
<dd>This option can be used to disable quota accounting. It is not possible to enable quota accounting by quota tools. Use <i><a href="/docs/linux/man/8-mount/">mount</a></i>(8) for that. This option is only applicable to XFS filesystems, and is silently ignored for other filesystem types.</dl>
<h2>Notes On Xfs Filesystems</h2>
<p>To enable quotas on an XFS filesystem, use <i><a href="/docs/linux/man/8-mount/">mount</a></i>(8) or <code>/etc/fstab</code> quota option to enable both accounting and limit enforcement. <code>quotaon</code> utility cannot be used for this purpose. </p>
<p> Turning on quotas on an XFS root filesystem requires the quota mount options be passed into the kernel at boot time through the Linux <code>rootflags</code> boot option. </p>
<p> To turn off quota limit enforcement on any XFS filesystem, first make sure that quota accounting and enforcement are both turned on using <code>repquota -v</code> <i>filesystem</i>. Then, use <code>quotaoff -v</code> <i>filesystem</i> to disable limit enforcement. This may be done while the filesystem is mounted. </p>
<p> Turning on quota limit enforcement on an XFS filesystem is achieved using <code>quotaon -v</code> <i>filesystem</i>. This may be done while the filesystem is mounted.</p>
<h2>Files</h2>
<dl>
<dt><code>aquota.user or aquota.group</code></p>
<dd>quota file at the filesystem root (version 2 quota, non-XFS filesystems)</p>
<dt><code>quota.user or quota.group</code></p>
<dd>quota file at the filesystem root (version 1 quota, non-XFS filesystems)</p>
<dt><code>/etc/fstab</code></p>
<dd>default filesystems</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-quota_nld/">quota_nld</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8), <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8) </p>
