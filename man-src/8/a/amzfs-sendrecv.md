---
title: "amzfs-sendrecv(8)"
name: "amzfs-sendrecv"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amzfs-sendrecv/"
description: "amzfs-sendrecv – Amanda script to create zfs sendrecv"
---

<p>amzfs-sendrecv &#8211; Amanda script to create zfs sendrecv</p>
<h2>Description</h2>
<p>amzfs-sendrecv is an Amanda application implementing the Application API. It should not be run by users directly. It create a zfs snapshot of the filesystem and backup the snapshot with &#8216;zfs send&#8217;. Snapshot are kept after the backup is done, this increase the disk space use on the client but it is neccesary to be able do to incremental backup. If you want only full backup, you can disable this feature by setting the KEEP-SNAPSHOT property to &#8216;NO&#8217;. Only the restoration of the complete backup is allowed, it is impossible to restore a single file. </p>
<p> The application is run as the amanda user, it must have many zfs priviledge: </p>
<pre> zfs allow -ldu AMANDA_USER mount,create,rename,snapshot,destroy,send,receive FILESYSTEM</pre>
<p>Some system doesn&#8217;t have &quot;zfs allow&quot;, but you can give the Amanda backup user the rights to manipulate ZFS filesystems by using the following command: </p>
<pre>usermod -P &quot;ZFS File System Management,ZFS Storage Management&quot; AMANDA_USER</pre>
<p>This will require that your run zfs under pfexec, set the PFEXEC property to YES. </p>
<p> The format of the <code>diskdevice</code> in the disklist (DLE) must be one of: </p>
<pre>Desciption Example
---------- -------
Mountpoint /data
ZFS pool name datapool
ZFS filesystem datapool/database
ZFS logical volume datapool/dbvol</pre>
<p>The filesystem doesn&#8217;t need to be mounted.</p>
<h2>Properties</h2>
<p>This section lists the properties that control amzfs-sendrecv&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) for information on the Application API, application configuration. </p>
<p> DF-PATH</p>
<dl>
<dd>Path to the &#8216;df&#8217; binary, search in $PATH by default.</dl>
<p> KEEP-SNAPSHOT</p>
<dl>
<dd>If &quot;YES&quot; (the default), snapshot are kept after the backup, if set to &quot;NO&quot; then snapshot are no kept and incremental backup will fail.</dl>
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
<p>In this example, a dumptype is defined to use amzfs-sendrecv application to backup a zfs filesystem. </p>
<pre> define application-tool amzfs_sendrecv {
 comment &quot;amzfs-sendrecv&quot;
 plugin &quot;amzfs-sendrecv&quot;
 #property &quot;DF-PATH&quot; &quot;/usr/sbin/df&quot;
 #property &quot;KEEP-SNAPSHOT&quot; &quot;YES&quot;
 #property &quot;ZFS-PATH&quot; &quot;/usr/sbin/zfs&quot;
 #property &quot;PFEXEC-PATH&quot; &quot;/usr/sbin/pfexec&quot;
 #property &quot;PFEXEC&quot; &quot;NO&quot;
 }
 define dumptype user-zfs-sendrecv {
 program &quot;APPLICATION&quot;
 application &quot;amzfs_sendrecv&quot;
 }</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
