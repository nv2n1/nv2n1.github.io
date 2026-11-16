---
title: "gfs2_quota(8)"
name: "gfs2_quota"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs2_quota/"
description: "gfs2_quota – Manipulate GFS2 disk quotas"
---

<p>gfs2_quota &#8211; Manipulate GFS2 disk quotas</p>
<h2>Synopsis</h2>
<p><code>gfs2_quota</code> &lt;list|sync|get|limit|warn|check|init|reset&gt; [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>gfs2_quota is used to examine and change quota values in a GFS2 filesystem. This command has a number of different actions. GFS2 introduced a new linked list format for the quotas in the quota file. This list format allows for faster <code>list</code>, <code>check</code> and <code>init</code> operations. Older GFS2 quota files may be migrated to this newer format using the <code>gfs2_quota reset</code> command. </p>
<h2>Actions</h2>
<dl>
<dt><code>list</code></dt>
<dd>List the contents of the quota file. Only IDs that have a non-zero hard limit, warn limit, or value are printed.</dd>
<dt><code>sync</code></dt>
<dd>Sync any local quota changes to the quota file.</dd>
<dt><code>get</code></dt>
<dd>Get the current data for the ID specified by the -u or -g argument.</dd>
<dt><code>limit</code></dt>
<dd>Set the current hard limit for the ID specified by the -u or -g argument to the value specified by the -l argument on the specified filesystem. The filesystem won&#8217;t let the user or group use more than this much space. A value of zero here means that no limit is enforced.</dd>
<dt><code>warn</code></dt>
<dd>Set the current warn limit for the ID specified by the -u or -g argument to the value specified by the -l argument on the specified filesystem. The filesystem will start complaining to the user or group when more than this much space is used. A value of zero here means that the user won&#8217;t ever be warned.</dd>
<dt><code>check</code></dt>
<dd>Scan a filesystem and make sure that what&#8217;s out there on the disk matches what&#8217;s in the quota file. This is only accurate if the filesystem is idle when this is running. If there is a mismatch, it is printed to stdout. Note: GFS2 quotas are transactional and a quota check is <code>not</code> needed every time there is a system crash.</dd>
<dt><code>init</code></dt>
<dd>Scan a filesystem and initialize the quota file with the values obtained from the scan. The filesystem should be idle when this is run. You should only need to do this if you upgrade a pre-quota GFS2 filesystem (pre-GFS2 5.1).</dd>
<dt><code>reset</code></dt>
<dd>The <code>reset</code> operation will truncate the quota file and all quota information (values, limits, warnings) will be lost. All quota limits and warnings will have to be reassigned after this operation. </dd>
</dl>
<h2>Options</h2>
<p><code>-b</code> The units for disk space are filesystem blocks.</p>
<dl>
<dt><code>-f</code> <i>Directory</i></dt>
<dd>Specifies which filesystem to perform the action on.</dd>
<dt><code>-g</code> <i>GID</i></dt>
<dd>Specifies the group ID for get, limit, or warn. It can be either the group name from the group file, or the GID number.</dd>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-k</code></dt>
<dd>The units for disk space are kilobytes.</dd>
<dt><code>-l</code> <i>Size</i></dt>
<dd>Specifies the new value for the limit or warn actions. The value is assumed to be in the units specified by the -m, -k, -s, -b arguments. The default is megabytes.</dd>
<dt><code>-m</code></dt>
<dd>The units for disk space are megabytes. This is the default.</dd>
<dt><code>-n</code></dt>
<dd>Don&#8217;t try to resolve UIDs and GIDs into user and group names.</dd>
<dt><code>-s</code></dt>
<dd>The units for disk space are sectors (512-byte blocks).</dd>
<dt><code>-u</code> <i>UID</i></dt>
<dd>Specifies the user ID for get, limit, or warn. It can be either the username from the password file, or the UID number.</dd>
<dt><code>-V</code></dt>
<dd>Print program version information, then exit. </dd>
</dl>
<h2>Example</h2>
<p>To set the hard limit for user &quot;nobody&quot; to 1048576 kilobytes on filesystem /gfs20 gfs2_quota limit -l 1048576 -k -u nobody -f /gfs20 </p>
