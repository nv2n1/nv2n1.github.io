---
title: "warnquota(8)"
name: "warnquota"
section: "8"
letter: "w"
url: "/docs/linux/man/8-warnquota/"
description: "warnquota – send mail to users over quota"
---

<p>warnquota &#8211; send mail to users over quota</p>
<h2>Synopsis</h2>
<p><code>warnquota</code> [ <code>-ugsid</code> ] [ <code>-F</code> <i>quotaformat</i> ] [ <code>-q</code> <i>quotatab</i> ] [ <code>-c</code> <i>configfile</i> ] [ <code>-a</code> <i>adminsfile</i> ] [ <i>filesystem</i>&#8230; ]</p>
<h2>Description</h2>
<p><code>warnquota</code> checks the disk quota for specified local filesystems (or for each local filesystem if none specified) and mails a warning message to those users who have reached their softlimit. It is typically run via <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8).</p>
<dl>
<dt><code>-F, &#8211;format=</code><i>quotaformat</i></dt>
<dd>Perform setting for specified format (ie. don&#8217;t perform format autodetection). Possible format names are: <code>vfsold</code> Original quota format with 16-bit UIDs / GIDs, <code>vfsv0</code> Quota format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode usage and limits, <code>vfsv1</code> Quota format with 64-bit quota limits and usage, <code>xfs</code> Quota on XFS filesystem.</dd>
<dt><code>-q, &#8211;quota-tab=</code><i>quotatab</i></dt>
<dd>Use <i>quotatab</i> instead of <i>/etc/quotatab</i> as file with device description strings (see <code><a href="/docs/linux/man/5-quotatab/">quotatab</a></code>(5) for syntax).</dd>
<dt><code>-c, &#8211;config=</code><i>configfile</i></dt>
<dd>Use <i>configfile</i> instead of <i>/etc/warnquota.conf</i> as configuration file (see <code><a href="/docs/linux/man/5-warnquota-conf/">warnquota.conf</a></code>(5) for syntax).</dd>
<dt><code>-a, &#8211;admins-file=</code><i>adminsfile</i></dt>
<dd>Use <i>adminsfile</i> instead of <i>/etc/quotagrpadmins</i> as a file with administrators of the groups (see <code><a href="/docs/linux/man/5-quotagrpadmins/">quotagrpadmins</a></code>(5) for syntax).</dd>
<dt><code>-u, &#8211;user</code></dt>
<dd>check whether users are not exceeding quotas (default).</dd>
<dt><code>-g, &#8211;group</code></dt>
<dd>check whether groups are not exceeding quotas. If group is exceeding quota a mail is sent to the user specified in /etc/quotagrpadmins.</dd>
<dt><code>-s, &#8211;human-readable</code></dt>
<dd>Try to report used space, number of used inodes and limits in more appropriate units than the default ones.</dd>
<dt><code>-i, &#8211;no-autofs</code></dt>
<dd>ignore mountpoints mounted by automounter.</dd>
<dt><code>-d, &#8211;no-details</code></dt>
<dd>do not attach quota report in email.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>aquota.user</code></dt>
<dd>quota file at the filesystem root (version 2 quota, non-XFS filesystems)</dd>
<dt><code>quota.user</code></dt>
<dd>quota file at the filesystem root (version 1 quota, non-XFS filesystems)</dd>
<dt><code>/etc/warnquota.conf</code></dt>
<dd>configuration file</dd>
<dt><code>/etc/quotatab</code></dt>
<dd>device description</dd>
<dt><code>/etc/quotagrpadmins</code></dt>
<dd>administrators of the groups</dd>
<dt><code>/etc/mtab</code></dt>
<dd>default filesystems</dd>
<dt><code>/etc/passwd</code></dt>
<dd>default set of users</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/5-quotatab/">quotatab</a></code>(5), <code><a href="/docs/linux/man/5-quotagrpadmins/">quotagrpadmins</a></code>(5), <code><a href="/docs/linux/man/5-warnquota-conf/">warnquota.conf</a></code>(5), <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8), <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8).</p>
<h2>Authors</h2>
<p><code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8) was written by Marco van Wieringen &lt;mvw [at] planets.elm.net&gt;, modifications by Jan Kara &lt;jack [at] suse.cz&gt;. This reference page written by Heiko Schlittermann &lt;heiko [at] lotte.sax.de&gt;, modifications by Jan Kara</p>
