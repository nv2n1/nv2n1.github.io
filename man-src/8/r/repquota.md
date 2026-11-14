---
title: "repquota(8)"
name: "repquota"
section: "8"
letter: "r"
url: "/docs/linux/man/8-repquota/"
description: "repquota – summarize quotas for a filesystem"
---

<p>repquota &#8211; summarize quotas for a filesystem</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/repquota</code> [ <code>-vspiug</code> ] [ <code>-c</code> | <code>-C</code> ] [ <code>-t</code> | <code>-n</code> ] [ <code>-F</code> <i>format-name</i> ] <i>filesystem</i>&#8230; </p>
<p> <code>/usr/sbin/repquota</code> [ <code>-avtpsiug</code> ] [ <code>-c</code> | <code>-C</code> ] [ <code>-t</code> | <code>-n</code> ] [ <code>-F</code> <i>format-name</i> ]</p>
<h2>Description</h2>
<p> <code>repquota</code> prints a summary of the disc usage and quotas for the specified file systems. For each user the current number of files and amount of space (in kilobytes) is printed, along with any quota limits set with <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8) or <code><a href="/docs/linux/man/8-setquota/">setquota</a></code>(8). In the second column repquota prints two characters marking which limits are exceeded. If user is over his space softlimit or reaches his space hardlimit in case softlimit is unset, the first character is &#8216;+&#8217;. Otherwise the character printed is &#8216;-&#8216;. The second character denotes the state of inode usage analogously. <code>repquota</code> has to translate ids of all users/groups to names (unless option <code>-n</code> was specified) so it may take a while to print all the information. To make translating as fast as possible <code>repquota</code> tries to detect (by reading <code>/etc/nsswitch.conf</code>) whether entries are stored in standard plain text file or in a database and either translates chunks of 1024 names or each name individually. You can override this autodetection by <code>-c</code> or <code>-C</code> options.</p>
<h2>Options</h2>
<dl>
<dt><code>-a, &#8211;all</code></p>
<dd>Report on all filesystems indicated in <code>/etc/mtab</code> to be read-write with quotas.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Report all quotas, even if there is no usage. Be also more verbose about quotafile information.</p>
<dt><code>-c, &#8211;cache</code></p>
<dd>Cache entries to report and translate uids/gids to names in big chunks by scanning all users (default). This is good (fast) behaviour when using /etc/passwd file.</p>
<dt><code>-C, &#8211;no-cache</code></p>
<dd>Translate individual entries. This is faster when you have users stored in database.</p>
<dt><code>-t, &#8211;truncate-names</code></p>
<dd>Truncate user/group names longer than 9 characters. This results in nicer output when there are such names.</p>
<dt><code>-n, &#8211;no-names</code></p>
<dd>Don&#8217;t resolve UIDs/GIDs to names. This can speedup printing a lot.</p>
<dt><code>-s, &#8211;human-readable</code></p>
<dd>Try to report used space, number of used inodes and limits in more appropriate units than the default ones.</p>
<dt><code>-p, &#8211;raw-grace</code></p>
<dd>When user is in grace period, report time in seconds since epoch when his grace time runs out (or has run out). Field is &#8216;0&#8217; when no grace time is in effect. This is especially useful when parsing output by a script.</p>
<dt><code>-i, &#8211;no-autofs</code></p>
<dd>Ignore mountpoints mounted by automounter.</p>
<dt><code>-F, &#8211;format=</code><i>format-name</i></p>
<dd>Report quota for specified format (ie. don&#8217;t perform format autodetection). Possible format names are: <code>vfsold</code> Original quota format with 16-bit UIDs / GIDs, <code>vfsv0</code> Quota format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode usage and limits, <code>vfsv1</code> Quota format with 64-bit quota limits and usage, <code>xfs</code> (quota on XFS filesystem)</p>
<dt><code>-g, &#8211;group</code></p>
<dd>Report quotas for groups.</p>
<dt><code>-u, &#8211;user</code></p>
<dd>Report quotas for users. This is the default.</dl>
<p> Only the super-user may view quotas which are not their own.</p>
<h2>Files</h2>
<dl>
<dt><code>aquota.user</code> or <code>aquota.group</code></p>
<dd>quota file at the filesystem root (version 2 quota, non-XFS filesystems)</p>
<dt><code>quota.user</code> or <code>quota.group</code></p>
<dd>quota file at the filesystem root (version 1 quota, non-XFS filesystems)</p>
<dt><code>/etc/mtab</code></p>
<dd>default filesystems</p>
<dt><code>/etc/passwd</code></p>
<dd>default set of users</p>
<dt><code>/etc/group</code></p>
<dd>default set of groups</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-quota_nld/">quota_nld</a></code>(8), <code><a href="/docs/linux/man/8-setquota/">setquota</a></code>(8), <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8) </p>
