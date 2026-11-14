---
title: "setquota(8)"
name: "setquota"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setquota/"
description: "setquota – set disk quotas"
---

<p>setquota &#8211; set disk quotas</p>
<h2>Synopsis</h2>
<p><code>setquota</code> [ <code>-rm</code> ] [ <code>-u</code> | <code>-g</code> ] [ <code>-F</code> <i>quotaformat</i> ] <i>name</i> <i>block-softlimit</i> <i>block-hardlimit</i> <i>inode-softlimit</i> <i>inode-hardlimit</i> <code>-a</code> | <i>filesystem&#8230;</i> </p>
<p> <code>setquota</code> [ <code>-rm</code> ] [ <code>-u</code> | <code>-g</code> ] [ <code>-F</code> <i>quotaformat</i> ] [ <code>-p</code> <i>protoname </i> ] <i>name</i> <code>-a</code> | <i>filesystem&#8230;</i> </p>
<p> <code>setquota</code> <code>-b</code> [ <code>-rm</code> ] [ <code>-u</code> | <code>-g</code> ] [ <code>-F</code> <i>quotaformat</i> ] <code>-a</code> | <i>filesystem&#8230;</i> </p>
<p> <code>setquota</code> <code>-t</code> [ <code>-u</code> | <code>-g</code> ] [ <code>-F</code> <i>quotaformat</i> ] <i>block-grace</i> <i>inode-grace</i> <code>-a</code> | <i>filesystem&#8230;</i> </p>
<p> <code>setquota</code> <code>-T</code> [ <code>-u</code> | <code>-g</code> ] [ <code>-F</code> <i>quotaformat</i> ] <i>name</i> <i>block-grace</i> <i>inode-grace</i> <code>-a</code> | <i>filesystem&#8230;</i></p>
<h2>Description</h2>
<p><code>setquota</code> is a command line quota editor. The filesystem, user/group name and new quotas for this filesystem can be specified on the command line. Note that if a number is given in the place of a user/group name it is treated as an UID/GID.</p>
<dl>
<dt><code>-r, &#8211;remote</code></p>
<dd>Edit also remote quota use rpc.rquotad on remote server to set quota. This option is available only if quota tools were compiled with enabled support for setting quotas over RPC.</p>
<dt><code>-m, &#8211;no-mixed-pathnames</code></p>
<dd>Currently, pathnames of NFSv4 mountpoints are sent without leading slash in the path. <code>rpc.rquotad</code> uses this to recognize NFSv4 mounts and properly prepend pseudoroot of NFS filesystem to the path. If you specify this option, <code>setquota</code> will always send paths with a leading slash. This can be useful for legacy reasons but be aware that quota over RPC will stop working if you are using new <code>rpc.rquotad</code>.</p>
<dt><code>-F, &#8211;format=</code><i>quotaformat</i></p>
<dd>Perform setting for specified format (ie. don&#8217;t perform format autodetection). Possible format names are: <code>vfsold</code> Original quota format with 16-bit UIDs / GIDs, <code>vfsv0</code> Quota format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode usage and limits, <code>vfsv1</code> Quota format with 64-bit quota limits and usage, <code>rpc</code> (quota over NFS), <code>xfs</code> (quota on XFS filesystem)</p>
<dt><code>-u, &#8211;user</code></p>
<dd>Set user quotas for named user. This is the default.</p>
<dt><code>-g, &#8211;group</code></p>
<dd>Set group quotas for named group.</p>
<dt><code>-p, &#8211;prototype=</code><i>protoname</i></p>
<dd>Use quota settings of user or group <i>protoname</i> to set the quota for the named user or group.</p>
<dt><code>&#8211;always-resolve</code></p>
<dd>Always try to translate user / group name to uid / gid even if the name is composed of digits only.</p>
<dt><code>-b, &#8211;batch</code></p>
<dd>Read information to set from stdin (input format is <i>name block-softlimit block-hardlimit inode-softlimit inode-hardlimit</i> ). Empty lines and lines starting with # are ignored.</p>
<dt><code>-c, &#8211;continue-batch</code></p>
<dd>If parsing of an input line in batch mode fails, continue with processing the next line.</p>
<dt><code>-t, &#8211;edit-period</code></p>
<dd>Set grace times for users/groups. Times <code>block-grace</code> and <code>inode-grace</code> are specified in seconds.</p>
<dt><code>-T, &#8211;edit-times</code></p>
<dd>Alter times for individual user/group when softlimit is enforced. Times <code>block-grace</code> and <code>inode-grace</code> are specified in seconds or can be string &#8216;unset&#8217;.</p>
<dt><code>-a, &#8211;all</code></p>
<dd>Go through all filesystems with quota in <code>/etc/mtab</code> and perform setting.</dl>
<p> <i>block-softlimit</i> and <i>block-hardlimit</i> are interpreted as multiples of kibibyte (1024 bytes) blocks by default. Symbols K, M, G, and T can be appended to numeric value to express kibibytes, mebibytes, gibibytes, and tebibytes. </p>
<p> <i>inode-softlimit</i> and <i>inode-hardlimit</i> are interpreted literally. Symbols k, m, g, and t can be appended to numeric value to express multiples of 10^3, 10^6, 10^9, and 10^12 inodes. </p>
<p> To disable a quota, set the corresponding parameter to 0. To change quotas for several filesystems, invoke once for each filesystem. </p>
<p> Only the super-user may edit quotas.</p>
<h2>Files</h2>
<dl>
<dt><code>aquota.user or aquota.group</code></p>
<dd>quota file at the filesystem root (version 2 quota, non-XFS filesystems)</p>
<dt><code>quota.user or quota.group</code></p>
<dd>quota file at the filesystem root (version 1 quota, non-XFS filesystems)</p>
<dt><code>/etc/mtab</code></p>
<dd>mounted filesystem table</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8), <code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8) </p>
