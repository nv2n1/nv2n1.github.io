---
title: "edquota(8)"
name: "edquota"
section: "8"
letter: "e"
url: "/docs/linux/man/8-edquota/"
description: "edquota – edit user quotas"
---

<p>edquota &#8211; edit user quotas</p>
<h2>Synopsis</h2>
<p><code>edquota</code> [ <code>-p</code> <i>protoname</i> ] [ <code>-u</code>&nbsp;<wbr>| <code>-g</code> ] [ <code>-rm</code> ] [ <code>-F</code> <i>format-name</i> ] [ <code>-f</code> <i>filesystem</i> ] <i>username</i>&#8230; </p>
<p> <code>edquota</code> [ <code>-u</code>&nbsp;<wbr>| <code>-g</code> ] [ <code>-F</code> <i>format-name</i> ] [ <code>-f</code> <i>filesystem</i> ] <code>-t</code> </p>
<p> <code>edquota</code> [ <code>-u</code>&nbsp;<wbr>| <code>-g</code> ] [ <code>-F</code> <i>format-name</i> ] [ <code>-f</code> <i>filesystem</i> ] <code>-T</code> <i>username</i>&nbsp;<wbr>| <i>groupname</i>&#8230;</p>
<h2>Description</h2>
<p><code>edquota</code> is a quota editor. One or more users or groups may be specified on the command line. If a number is given in the place of user/group name it is treated as an UID/GID. For each user or group a temporary file is created with an <font SIZE="-1">ASCII</font> representation of the current disk quotas for that user or group and an editor is then invoked on the file. The quotas may then be modified, new quotas added, etc. Setting a quota to zero indicates that no quota should be imposed. </p>
<p> Block usage and limits are reported and interpereted as multiples of kibibyte (1024 bytes) blocks by default. Symbols K, M, G, and T can be appended to numeric value to express kibibytes, mebibytes, gibibytes, and tebibytes. </p>
<p> Inode usage and limits are interpreted literally. Symbols k, m, g, and t can be appended to numeric value to express multiples of 10^3, 10^6, 10^9, and 10^12 inodes. </p>
<p> Users are permitted to exceed their soft limits for a grace period that may be specified per filesystem. Once the grace period has expired, the soft limit is enforced as a hard limit. </p>
<p> The current usage information in the file is for informational purposes; only the hard and soft limits can be changed. </p>
<p> Upon leaving the editor, <code>edquota</code> reads the temporary file and modifies the binary quota files to reflect the changes made. </p>
<p> The editor invoked is <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) unless either the <font SIZE="-1"><code>EDITOR</code></font> or the <font SIZE="-1"><code>VISUAL</code></font> environment variable specifies otherwise. </p>
<p> Only the super-user may edit quotas.</p>
<h2>Options</h2>
<dl>
<dt><code>-r, &#8211;remote</code></p>
<dd>Edit also non-local quota use rpc.rquotad on remote server to set quota. This option is available only if quota tools were compiled with enabled support for setting quotas over RPC. The <code>-n</code> option is equivalent, and is maintained for backward compatibility.</p>
<dt><code>-m, &#8211;no-mixed-pathnames</code></p>
<dd>Currently, pathnames of NFSv4 mountpoints are sent without leading slash in the path. <code>rpc.rquotad</code> uses this to recognize NFSv4 mounts and properly prepend pseudoroot of NFS filesystem to the path. If you specify this option, <code>edquota</code> will always send paths with a leading slash. This can be useful for legacy reasons but be aware that quota over RPC will stop working if you are using new <code>rpc.rquotad</code>.</p>
<dt><code>-u, &#8211;user</code></p>
<dd>Edit the user quota. This is the default.</p>
<dt><code>-g, &#8211;group</code></p>
<dd>Edit the group quota.</p>
<dt><code>-p, &#8211;prototype=</code><i>protoname</i></p>
<dd>Duplicate the quotas of the prototypical user specified for each user specified. This is the normal mechanism used to initialize quotas for groups of users.</p>
<dt><code>&#8211;always-resolve</code></p>
<dd>Always try to translate user / group name to uid / gid even if the name is composed of digits only.</p>
<dt><code>-F, &#8211;format=</code><i>format-name</i></p>
<dd>Edit quota for specified format (ie. don&#8217;t perform format autodetection). Possible format names are: <code>vfsold</code> Original quota format with 16-bit UIDs / GIDs, <code>vfsv0</code> Quota format with 32-bit UIDs / GIDs, 64-bit space usage, 32-bit inode usage and limits, <code>vfsv1</code> Quota format with 64-bit quota limits and usage, <code>rpc</code> (quota over NFS), <code>xfs</code> (quota on XFS filesystem)</p>
<dt><code>-f, &#8211;filesystem </code><i>filesystem</i></p>
<dd>Perform specified operations only for given filesystem (default is to perform operations for all filesystems with quota).</p>
<dt><code>-t, &#8211;edit-period</code></p>
<dd>Edit the soft time limits for each filesystem. In old quota format if the time limits are zero, the default time limits in <code>&lt;linux/quota.h&gt;</code> are used. In new quota format time limits must be specified (there is no default value set in kernel). Time units of &#8216;seconds&#8217;, &#8216;minutes&#8217;, &#8216;hours&#8217;, and &#8216;days&#8217; are understood. Time limits are printed in the greatest possible time unit such that the value is greater than or equal to one.</p>
<dt><code>-T, &#8211;edit-times</code></p>
<dd>Edit time for the user/group when softlimit is enforced. Possible values are &#8216;unset&#8217; or number and unit. Units are the same as in <code>-t</code> option.</dl>
<h2>Files</h2>
<dl>
<dt><code>aquota.user</code> or <code>aquota.group</code></p>
<dd>quota file at the filesystem root (version 2 quota, non-XFS filesystems)</p>
<dt><code>quota.user</code> or <code>quota.group</code></p>
<dd>quota file at the filesystem root (version 1 quota, non-XFS filesystems)</p>
<dt><code>/etc/mtab</code></p>
<dd>mounted filesystems table</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8), <code><a href="/docs/linux/man/8-setquota/">setquota</a></code>(8) </p>
