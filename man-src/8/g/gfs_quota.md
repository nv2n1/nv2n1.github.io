---
title: "gfs_quota(8)"
name: "gfs_quota"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs_quota/"
description: "gfs_quota – Manipulate GFS disk quotas"
---

<p>gfs_quota &#8211; Manipulate GFS disk quotas</p>
<h2>Synopsis</h2>
<p><code>gfs_quota</code> &lt;list|sync|get|limit|warn|check|init&gt; [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>gfs_quota is used to examine and change quota values in a GFS filesystem. This command has a number of different actions. </p>
<h2>Actions</h2>
<dl>
<dt><code>list</code></p>
<dd>List the contents of the quota file. Only IDs that have a non-zero hard limit, warn limit, or value are printed.</p>
<dt><code>sync</code></p>
<dd>Sync any local quota changes to the quota file.</p>
<dt><code>get</code></p>
<dd>Get the current data for the ID specified by the -u or -g argument.</p>
<dt><code>limit</code></p>
<dd>Set the current hard limit for the ID specified by the -u or -g argument to the value specified by the -l argument on the specified filesystem. The filesystem won&#8217;t let the user or group use more than this much space. A value of zero here means that no limit is enforced.</p>
<dt><code>warn</code></p>
<dd>Set the current warn limit for the ID specified by the -u or -g argument to the value specified by the -l argument on the specified filesystem. The filesystem will start complaining to the user or group when more than this much space is used. A value of zero here means that the user won&#8217;t ever be warned.</p>
<dt><code>check</code></p>
<dd>Scan a filesystem and make sure that what&#8217;s out there on the disk matches what&#8217;s in the quota file. This is only accurate if the filesystem is idle when this is running. If there is a mismatch, it is printed to stdout. Note: GFS quotas are transactional and a quota check is <code>not</code> needed every time there is a system crash.</p>
<dt><code>init</code></p>
<dd>Scan a filesystem and initialize the quota file with the values obtained from the scan. The filesystem should be idle when this is run. You should only need to do this if you upgrade a pre-quota GFS filesystem (pre-GFS 5.1). </p>
</dl>
<h2>Options</h2>
<p><code>-b</code> The units for disk space are filesystem blocks.</p>
<dl>
<dt><code>-d</code></p>
<dd>Don&#8217;t include the space allocated to GFS&#8217; hidden files in what&#8217;s reported for the root UID and GID values. This is useful if you&#8217;re trying to get the numbers reported by gfs_quota to match up with the numbers reported by du.</p>
<dt><code>-f</code> <i>Directory</i></p>
<dd>Specifies which filesystem to perform the action on.</p>
<dt><code>-g</code> <i>GID</i></p>
<dd>Specifies the group ID for get, limit, or warn. It can be either the group name from the group file, or the GID number.</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-k</code></p>
<dd>The units for disk space are kilobytes.</p>
<dt><code>-l</code> <i>Size</i></p>
<dd>Specifies the new value for the limit or warn actions. The value is assumed to be in the units specified by the -m, -k, -s, -b arguments. The default is megabytes.</p>
<dt><code>-m</code></p>
<dd>The units for disk space are megabytes. This is the default.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t try to resolve UIDs and GIDs into user and group names.</p>
<dt><code>-s</code></p>
<dd>The units for disk space are sectors (512-byte blocks).</p>
<dt><code>-u</code> <i>UID</i></p>
<dd>Specifies the user ID for get, limit, or warn. It can be either the username from the password file, or the UID number.</p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit. </p>
</dl>
<h2>Example</h2>
<p>To set the hard limit for user &quot;nobody&quot; to 1048576 kilobytes on filesystem /gfs0 gfs_quota limit -l 1048576 -k -u nobody -f /gfs0 </p>
