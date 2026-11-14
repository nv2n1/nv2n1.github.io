---
title: "amzfs-snapshot(8)"
name: "amzfs-snapshot"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amzfs-snapshot/"
description: "amzfs-snapshot – Amanda script to create zfs snapshot"
---

<p>amzfs-snapshot &#8211; Amanda script to create zfs snapshot</p>
<h2>Description</h2>
<p>amzfs-snapshot is an Amanda script implementing the Script API. It should not be run by users directly. It create a zfs snapshot of the filesystem where the path specified is mounted. </p>
<p> PRE-DLE-* create a snapshot and the POST-DLE-* destroy the snapshot, *-DLE-AMCHECK, *-DLE-ESTIMATE and *-DLE-BACKUP must be set to be executed on the client: </p>
<pre> execute-on pre-dle-amcheck, post-dle-amcheck, pre-dle-estimate, post-dle-estimate, pre-dle-backup, post-dle-backup
 execute-where client</pre>
<p>The PRE_DLE_* script output a DIRECTORY property telling where the directory is located in the snapshot. The application must be able to use the DIRECTORY property, amgtar can do it. </p>
<p> The script is run as the amanda user, it must have the priviledge to create and destroy snapshot: </p>
<pre> zfs allow -ldu AMANDA_USER mount,snapshot,destroy FILESYSTEM</pre>
<p>Some system doesn&#8217;t have &quot;zfs allow&quot;, but you can give the Amanda backup user the rights to manipulate ZFS filesystems by using the following command: </p>
<pre>usermod -P &quot;ZFS File System Management,ZFS Storage Management&quot; AMANDA_USER</pre>
<p>This will require that your run zfs under pfexec, set the PFEXEC property to YES. </p>
<p> The format of the DLE must be one of: </p>
<pre>Desciption Example
---------- -------
Mountpoint /data
Arbitrary mounted dir /data/interesting_dir
ZFS pool name datapool
ZFS filesystem datapool/database
ZFS logical volume datapool/dbvol</pre>
<p>The filesystem must be mounted.</p>
<h2>Properties</h2>
<p>This section lists the properties that control amzfs-snapshot&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-scripts/">amanda-scripts</a></code>(7) for information on the Script API, script configuration. </p>
<p> DF-PATH</p>
<dl>
<dd>Path to the &#8216;df&#8217; binary, search in $PATH by default.</dl>
<p> ZFS-PATH</p>
<dl>
<dd>Path to the &#8216;zfs&#8217; binary, search in $PATH by default.</dl>
<p> PFEXEC-PATH</p>
<dl>
<dd>Path to the &#8216;pfexec&#8217; binary, search in $PATH by default.</dl>
<p> PFEXEC</p>
<dl>
<dd>If &quot;NO&quot; (the default), pfexec is not used, if set to &quot;YES&quot; then pfexec is used.</dl>
<h2>Example</h2>
<p>In this example, a dumptype is defined to use amzfs-snapshot script to create a snapshot and use amgtar to backup the snapshot. </p>
<pre> define script-tool amzfs_snapshot {
 comment &quot;backup of zfs snapshot&quot;
 plugin &quot;amzfs-snapshot&quot;
 execute-on pre-dle-amcheck, post-dle-amcheck, pre-dle-estimate, post-dle-estimate, pre-dle-backup, post-dle-backup
 execute-where client
 #property &quot;DF-PATH&quot; &quot;/usr/sbin/df&quot;
 #property &quot;ZFS-PATH&quot; &quot;/usr/sbin/zfs&quot;
 #property &quot;PFEXEC-PATH&quot; &quot;/usr/sbin/pfexec&quot;
 #property &quot;PFEXEC&quot; &quot;NO&quot;
 }
 define dumptype user-zfs-amgtar {
 dt_amgtar
 script &quot;amzfs_snapshot&quot;
 }</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-scripts/">amanda-scripts</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
