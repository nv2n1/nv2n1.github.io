---
title: "quotacheck(8)"
name: "quotacheck"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quotacheck/"
description: "quotacheck – scan a filesystem for disk usage, create, check and repair quota files"
---

<p>quotacheck &#8211; scan a filesystem for disk usage, create, check and repair quota files</p>
<h2>Synopsis</h2>
<p><code>quotacheck</code> [ <code>-gubcfinvdMmR</code> ] [ <code>-F</code> <i>quota-format</i> ] <code>-a</code> | <i>filesystem</i></p>
<h2>Description</h2>
<p><code>quotacheck</code> examines each filesystem, builds a table of current disk usage, and compares this table against that recorded in the disk quota file for the filesystem (this step is omitted if option <code>-c</code> is specified). If any inconsistencies are detected, both the quota file and the current system copy of the incorrect quotas are updated (the latter only occurs if an active filesystem is checked which is not advised). By default, only user quotas are checked. <code>quotacheck</code> expects each filesystem to be checked to have quota files named <i>[a]quota.user</i> and <i>[a]quota.group</i> located at the root of the associated filesystem. If a file is not present, <code>quotacheck</code> will create it. </p>
<p> If the quota file is corrupted, <code>quotacheck</code> tries to save as much data as possible. Rescuing data may need user intervention. With no additional options <code>quotacheck</code> will simply exit in such a situation. When in interactive mode (option <code>-i</code>) , the user is asked for advice. Advice can also be provided from command line (see option <code>-n</code>) , which is useful when <code>quotacheck</code> is run automatically (ie. from script) and failure is unacceptable. </p>
<p> <code>quotacheck</code> should be run each time the system boots and mounts non-valid filesystems. This is most likely to happen after a system crash. </p>
<p> It is strongly recommended to run <code>quotacheck</code> with quotas turned off for the filesystem. Otherwise, possible damage or loss to data in the quota files can result. It is also unwise to run <code>quotacheck</code> on a live filesystem as actual usage may change during the scan. To prevent this, <code>quotacheck</code> tries to remount the filesystem read-only before starting the scan. After the scan is done it remounts the filesystem read-write. You can disable this with option <code>-m</code>. You can also make <code>quotacheck</code> ignore the failure to remount the filesystem read-only with option <code>-M</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-b, &#8211;backup</code></p>
<dd>Forces <code>quotacheck</code> to make backups of the quota file before writing the new data.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd><code>quotacheck</code> reports its operation as it progresses. Normally it operates silently. If the option is specified twice, also the current directory is printed (note that printing can slow down the scan measurably).</p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Enable debugging mode. It will result in a lot of information which can be used in debugging the program. The output is very verbose and the scan will be slow.</p>
<dt><code>-u, &#8211;user</code></p>
<dd>Only user quotas listed in <i>/etc/mtab</i> or on the filesystems specified are to be checked. This is the default action.</p>
<dt><code>-g, &#8211;group</code></p>
<dd>Only group quotas listed in <i>/etc/mtab</i> or on the filesystems specified are to be checked.</p>
<dt><code>-c, &#8211;create-files</code></p>
<dd>Don&#8217;t read existing quota files. Just perform a new scan and save it to disk. <code>quotacheck</code> also skips scanning of old quota files when they are not found.</p>
<dt><code>-f, &#8211;force</code></p>
<dd>Forces checking and writing of new quota files on filesystems with quotas enabled. This is not recommended as the created quota files may be out of sync.</p>
<dt><code>-M, &#8211;try-remount</code></p>
<dd>This flag forces checking of filesystem in read-write mode if a remount fails. Do this only when you are sure no process will write to a filesystem while scanning.</p>
<dt><code>-m, &#8211;no-remount</code></p>
<dd>Don&#8217;t try to remount filesystem read-only. See comment with option <code>-M</code>.</p>
<dt><code>-i, &#8211;interactive</code></p>
<dd>Interactive mode. By default <code>quotacheck</code> exits when it finds an error. In interactive mode user is asked for input instead. See option <code>-n</code>.</p>
<dt><code>-n, &#8211;use-first-dquot</code></p>
<dd>If the quota files become corrupted, it is possible for duplicate entries for a single user or group ID to exist. Normally in this case, <code>quotacheck</code> exits or asks user for input. When this option is set, the first entry found is always used (this option works in interactive mode too).</p>
<dt><code>-F, &#8211;format=</code><i>format-name</i></p>
<dd>Check and fix quota files of specified format (ie. don&#8217;t perform format auto-detection). This is recommended as detection might not work well on corrupted quota files. Possible format names are: <code>vfsold</code> Original quota format with 16-bit UIDs / GIDs, <code>vfsv0</code> Quota format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode usage and limits, <code>vfsv1</code> Quota format with 64-bit quota limits and usage, <code>rpc</code> (quota over NFS), <code>xfs</code> (quota on XFS filesystem)</p>
<dt><code>-a, &#8211;all</code></p>
<dd>Check all mounted non-NFS filesystems in <code>/etc/mtab</code></p>
<dt><code>-R, &#8211;exclude-root</code></p>
<dd>When used together with the <code>-a</code> option, all filesystems except for the root filesystem are checked for quotas. </p>
</dl>
<h2>Note</h2>
<p><code>quotacheck</code> should only be run by super-user. Non-privileged users are presumably not allowed to read all the directories on the given filesystem.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8), <code><a href="/docs/linux/man/8-convertquota/">convertquota</a></code>(8), <code><a href="/docs/linux/man/8-setquota/">setquota</a></code>(8), <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-efsck/">efsck</a></code>(8), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-xfsck/">xfsck</a></code>(8) </p>
<h2>Files</h2>
<dl>
<dt><code>aquota.user or aquota.group</code></p>
<dd>located at filesystem root with quotas (version 2 quota, non-XFS filesystems)</p>
<dt><code>quota.user or quota.group</code></p>
<dd>located at filesystem root with quotas (version 1 quota, non-XFS filesystems)</p>
<dt><code>/etc/mtab</code></p>
<dd>names and locations of mounted filesystems</dl>
<h2>Author</h2>
<p>Jan Kara &lt;jack [at] suse.cz&gt;<br />
 Based on old <code>quotacheck</code> by:<br />
 Edvard Tuinder &lt;ed [at] elm.net&gt;<br />
 Marco van Wieringen &lt;mvw [at] planets.elm.net&gt;</p>
