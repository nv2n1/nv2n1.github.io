---

title: "quota(1)"
name: "quota"
section: "1"
letter: "q"
url: "/docs/linux/man/1-quota/"
description: "quota – display disk usage and limits"
---

<p> quota &#8211; display disk usage and limits</p>
<h2>SYNOPSIS</h2>
<p> <code>quota</code> [ <code>-F</code> <i>format-name</i> ] [ <code>-guqvswi</code> ] [ <code>-l</code>&nbsp;<wbr>| [ <code>-QAm</code> ]]<br />
 <code>quota</code> [ <code>-F</code> <i>format-name</i> ] [ <code>-qvswi</code> ] [ <code>-l</code>&nbsp;<wbr>| [ <code>-QAm</code> ]] <code>-u</code> <i>user</i>&#8230;<br />
 <code>quota</code> [ <code>-F</code> <i>format-name</i> ] [ <code>-qvswi</code> ] [ <code>-l</code>&nbsp;<wbr>| [ <code>-QAm</code> ]] <code>-g</code> <i>group</i>&#8230;<br />
 <code>quota</code> [ <code>-F</code> <i>format-name</i> ] [ <code>-qvswugQm</code> ] <code>-f</code> <i>filesystem</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>quota</code> displays users&#8217; disk usage and limits. By default only the user quotas are printed. </p>
<p> <code>quota</code> reports the quotas of all the filesystems listed in <code>/etc/mtab</code>. For filesystems that are NFS-mounted a call to the rpc.rquotad on the server machine is performed to get the information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F, &#8211;format=</code><i>format-name</i></dt>
<dd> Show quota for specified format (ie. don&#8217;t perform format autodetection). Possible format names are: <code>vfsold</code> Original quota format with 16-bit UIDs / GIDs, <code>vfsv0</code> Quota format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode usage and limits, <code>vfsv1</code> Quota format with 64-bit quota limits and usage, <code>rpc</code> (quota over NFS), <code>xfs</code> (quota on XFS filesystem)</dd>
<dt><code>-g, &#8211;group</code></dt>
<dd> Print group quotas for the group of which the user is a member. The optional <code>group</code> argument(s) restricts the display to the specified group(s).</dd>
<dt><code>-u, &#8211;user</code></dt>
<dd> flag is equivalent to the default.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> will display quotas on filesystems where no storage is allocated.</dd>
<dt><code>-s, &#8211;human-readable</code></dt>
<dd> option will make <code><a href="/docs/linux/man/1-quota/">quota</a></code>(1) try to choose units for showing limits, used space and used inodes.</dd>
<dt><code>&#8211;always-resolve</code></dt>
<dd> Always try to translate user / group name to uid / gid even if the name is composed of digits only.</dd>
<dt><code>-p, &#8211;raw-grace</code></dt>
<dd> When user is in grace period, report time in seconds since epoch when his grace time runs out (or has run out). Field is &#8216;0&#8217; when no grace time is in effect. This is especially useful when parsing output by a script.</dd>
<dt><code>-i, &#8211;no-autofs</code></dt>
<dd> ignore mountpoints mounted by automounter</dd>
<dt><code>-l, &#8211;local-only</code></dt>
<dd> report quotas only on local filesystems (ie. ignore NFS mounted filesystems).</dd>
<dt><code>-A, &#8211;all-nfs</code></dt>
<dd> report quotas for all NFS filesystems even if they report to be on the same device.</dd>
<dt><code>-f, &#8211;filesystem-list</code></dt>
<dd> report quotas only for filesystems specified on command line.</dd>
<dt><code>-m, &#8211;no-mixed-pathnames</code></dt>
<dd> Currently, pathnames of NFSv4 mountpoints are sent without leading slash in the path. <code>rpc.rquotad</code> uses this to recognize NFSv4 mounts and properly prepend pseudoroot of NFS filesystem to the path. If you specify this option, <code>quota</code> will always send paths with a leading slash. This can be useful for legacy reasons but be aware that quota over RPC will stop working if you are using new <code>rpc.rquotad</code>.</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Print a more terse message, containing only information on filesystems where usage is over quota.</dd>
<dt><code>-Q, &#8211;quiet-refuse</code></dt>
<dd> Do not print error message if connection to <code>rpc.rquotad</code> is refused (usually this happens when <code>rpc.rquotad</code> is not running on the server).</dd>
<dt><code>-w, &#8211;no-wrap</code></dt>
<dd> Do not wrap the line if the device name is too long. This can be useful when parsing the output of <code><a href="/docs/linux/man/1-quota/">quota</a></code>(1) by a script.</dd>
<dt><code>&#8211;show-mntpoint</code></dt>
<dd> Show also mount point as a filesystem identification.</dd>
<dt><code>&#8211;hide-device</code></dt>
<dd> Do not show device name in a filesystem identification.</dd></dl>
<p> Specifying both <code>-g</code> and <code>-u</code> displays both the user quotas and the group quotas (for the user). </p>
<p> Only the super-user may use the <code>-u</code> flag and the optional <code>user</code> argument to view the limits of other users. Non-super-users can use the the <code>-g</code> flag and optional <code>group</code> argument to view only the limits of groups of which they are members. </p>
<p> The <code>-q</code> flag takes precedence over the <code>-v</code> flag.</p>
<h2>DIAGNOSTICS</h2>
<p> If <code>quota</code> exits with a non-zero status, one or more filesystems are over quota.</p>
<h2>FILES</h2>
<dl>
<dt><code>aquota.user or aquota.group</code></dt>
<dd> quota file at the filesystem root (version 2 quota, non-XFS filesystems)</dd>
<dt><code>quota.user or quota.group</code></dt>
<dd> quota file at the filesystem root (version 1 quota, non-XFS filesystems)</dd>
<dt><code>/etc/mtab</code></dt>
<dd> default filesystems</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-quota_nld/">quota_nld</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8), <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8), <code><a href="/docs/linux/man/8-setquota/">setquota</a></code>(8) </p>
