---
title: "exportfs(8)"
name: "exportfs"
section: "8"
letter: "e"
url: "/docs/linux/man/8-exportfs/"
description: "exportfs – maintain table of exported NFS file systems"
---

<p>exportfs &#8211; maintain table of exported NFS file systems</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/exportfs [-avi] [-o </code><i>options,..</i><code>] [</code><i>client:/path</i><code> ..]</code><br />
 <code>/usr/sbin/exportfs -r [-v]</code><br />
 <code>/usr/sbin/exportfs [-av] -u [</code><i>client:/path</i><code> ..]</code><br />
 <code>/usr/sbin/exportfs [-v]</code><br />
 <code>/usr/sbin/exportfs -f</code><br />
 <code>/usr/sbin/exportfs -s</code></p>
<h2>Description</h2>
<p>An NFS server maintains a table of local physical file systems that are accessible to NFS clients. Each file system in this table is referred to as an <i>exported file system</i>, or <i>export</i>, for short. </p>
<p> The <code>exportfs</code> command maintains the current table of exports for the NFS server. The master export table is kept in a file named <i>/var/lib/nfs/etab</i>. This file is read by <code>rpc.mountd</code> when a client sends an NFS MOUNT request. </p>
<p> Normally the master export table is initialized with the contents of <i>/etc/exports</i> and files under <i>/etc/exports.d</i> by invoking <code>exportfs -a</code>. However, a system administrator can choose to add or delete exports without modifying <i>/etc/exports</i> or files under <i>/etc/exports.d</i> by using the <code>exportfs</code> command. </p>
<p> <code>exportfs</code> and its partner program <code>rpc.mountd</code> work in one of two modes: a legacy mode which applies to 2.4 and earlier versions of the Linux kernel, and a new mode which applies to 2.6 and later versions, providing the <code>nfsd</code> virtual filesystem has been mounted at <i>/proc/fs/nfsd</i> or <i>/proc/fs/nfs</i>. On 2.6 kernels, if this filesystem is not mounted, the legacy mode is used. </p>
<p> In the new mode, <code>exportfs</code> does not give any information to the kernel, but provides it only to <code>rpc.mountd</code> through the <i>/var/lib/nfs/etab</i> file. <code>rpc.mountd</code> then manages kernel requests for information about exports, as needed. </p>
<p> In the legacy mode, exports which identify a specific host, rather than a subnet or netgroup, are entered directly into the kernel&#8217;s export table, as well as being written to <i>/var/lib/nfs/etab</i>. Further, exports listed in <i>/var/lib/nfs/rmtab</i> which match a non host-specific export request will cause an appropriate export entry for the host given in <i>rmtab</i> to be added to the kernel&#8217;s export table.</p>
<h2>Options</h2>
<dl>
<dt><code>-d kind or &#8211;debug kind</code></p>
<dd>Turn on debugging. Valid kinds are: all, auth, call, general and parse. Debugging can also be turned on by setting <code>debug=</code> in the <code>[exportfs]</code> section of <i>/etc/nfs.conf</i>. </p>
<dt><code>-a</code></p>
<dd>Export or unexport all directories.</p>
<dt><code>-o </code><i>options,&#8230;</i></p>
<dd>Specify a list of export options in the same manner as in <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5).</p>
<dt><code>-i</code></p>
<dd>Ignore the <i>/etc/exports</i> file and files under <i>/etc/exports.d</i> directory. Only default options and options given on the command line are used.</p>
<dt><code>-r</code></p>
<dd>Reexport all directories, synchronizing <i>/var/lib/nfs/etab</i> with <i>/etc/exports</i> and files under <i>/etc/exports.d</i>. This option removes entries in <i>/var/lib/nfs/etab</i> which have been deleted from <i>/etc/exports</i> or files under <i>/etc/exports.d</i>, and removes any entries from the kernel export table which are no longer valid.</p>
<dt><code>-u</code></p>
<dd>Unexport one or more directories.</p>
<dt><code>-f</code></p>
<dd>If <i>/proc/fs/nfsd</i> or <i>/proc/fs/nfs</i> is mounted, flush everything out of the kernel&#8217;s export table. Fresh entries for active clients are added to the kernel&#8217;s export table by <code>rpc.mountd</code> when they make their next NFS mount request.</p>
<dt><code>-v</code></p>
<dd>Be verbose. When exporting or unexporting, show what&#8217;s going on. When displaying the current export list, also display the list of export options.</p>
<dt><code>-s</code></p>
<dd>Display the current export list suitable for /etc/exports.</dl>
<h2>Discussion</h2>
<h3>Exporting Directories</h3>
<p>The first synopsis shows how to invoke <code>exportfs</code> when adding new entries to the export table. When using <code>exportfs -a</code>, all exports listed in <i>/etc/exports</i> and files under <i>/etc/exports.d</i> are added to <i>/var/lib/nfs/etab</i>. The kernel&#8217;s export table is also updated as needed. </p>
<p> The <i>host:/path</i> argument specifies a local directory to export, along with the client or clients who are permitted to access it. See <code><a href="/docs/linux/man/5-exports/">exports</a>(5)</code> for a description of supported options and access list formats. </p>
<p> IPv6 presentation addresses contain colons, which are already used to separate the &quot;host&quot; and &quot;path&quot; command line arguments. When specifying a client using a raw IPv6 address, enclose the address in square brackets. For IPv6 network addresses, place the prefix just after the closing bracket. </p>
<p> To export a directory to the world, simply specify <i>:/path</i>. </p>
<p> The export options for a particular host/directory pair derive from several sources. The default export options are <code>sync,ro,root_squash,wdelay</code>. These can be overridden by entries in <i>/etc/exports</i> or files under <i>/etc/exports.d</i>. </p>
<p> A system administrator may override options from these sources using the <code>-o</code> command-line option on <code>exportfs</code>. This option takes a comma-separated list of options in the same fashion as one would specify them in <i>/etc/exports</i>. In this way <code>exportfs</code> can be used to modify the export options of an already exported directory.</p>
<h3>Unexporting Directories</h3>
<p>The third synopsis shows how to unexport a currently exported directory. When using <code>exportfs -ua</code>, all entries listed in <i>/var/lib/nfs/etab</i> are removed from the kernel export tables, and the file is cleared. This effectively shuts down all NFS activity. </p>
<p> To remove an export, specify a <i>host:/path</i> pair. This deletes the specified entry from <i>/var/lib/nfs/etab</i> and removes the corresponding kernel entry (if any).</p>
<h3>Dumping the Export Table</h3>
<p>Invoking <code>exportfs</code> without options shows the current list of exported file systems. Adding the <code>-v</code> option causes <code>exportfs</code> to display the export options for each export.</p>
<h2>Examples</h2>
<p>The following adds all directories listed in <i>/etc/exports</i> and files under <i>/etc/exports.d</i> to <i>/var/lib/nfs/etab</i> and pushes the resulting export entries into the kernel: </p>
<pre><code># exportfs -a</code></pre>
<p>To export the <i>/usr/tmp</i> directory to host <code>django</code>, allowing insecure file locking requests from clients: </p>
<pre><code># exportfs -o insecure_locks django:/usr/tmp</code></pre>
<p>To unexport the <i>/usr/tmp</i> directory: </p>
<pre><code># exportfs -u django:/usr/tmp</code></pre>
<p>To unexport all exports listed in <i>/etc/exports</i> and files under <i>/etc/exports.d</i>: </p>
<pre><code># exportfs -au</code></pre>
<p>To export the <i>/usr/tmp</i> directory to IPv6 link-local clients: </p>
<pre><code># exportfs [fe80::]/64:/usr/tmp</code></pre>
<h2>Usage Notes</h2>
<p>Exporting to IP networks or DNS and NIS domains does not enable clients from these groups to access NFS immediately. Rather, these sorts of exports are hints to <code><a href="/docs/linux/man/8-rpc-mountd/">rpc.mountd</a></code>(8) to grant any mount requests from these clients. This is usually not a problem, because any existing mounts are preserved in <i>rmtab</i> across reboots. </p>
<p> When unexporting a network or domain entry, any current exports to members of this group will be checked against the remaining valid exports and if they themselves are no longer valid they will be removed.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/exports</i></p>
<dd>input file listing exports, export options, and access control lists</p>
<dt><i>/etc/exports.d</i></p>
<dd>directory where extra input files are stored. <code>Note:</code> only files that end with <i>.exports</i> are used.</p>
<dt><i>/var/lib/nfs/etab</i></p>
<dd>master table of exports</p>
<dt><i>/var/lib/nfs/rmtab</i></p>
<dd>table of clients accessing server&#8217;s exports</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-exports/">exports</a></code>(5), <code><a href="/docs/linux/man/5-nfs-conf/">nfs.conf</a></code>(5), <code><a href="/docs/linux/man/8-rpc-mountd/">rpc.mountd</a></code>(8), <code><a href="/docs/linux/man/5-netgroup/">netgroup</a></code>(5)</p>
<h2>Authors</h2>
<p>Olaf Kirch &lt;okir [at] monad.swb.de&gt;<br />
 Neil Brown &lt;neilb [at] cse.unsw.edu.au&gt;</p>
