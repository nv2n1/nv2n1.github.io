---
title: "fixmount(8)"
name: "fixmount"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fixmount/"
description: "fixmount – fix remote mount entries"
---

<p>fixmount &#8211; fix remote mount entries</p>
<h2>Synopsis</h2>
<p><code>fixmount</code> [ <code>-adervq</code> ] [ <code>-h</code> <i>name</i> ] <i>host</i> &#8230;</p>
<h2>Description</h2>
<p> <code>fixmount</code> is a variant of <code><a href="/docs/linux/man/8-showmount/">showmount</a></code>(8) that can delete bogus mount entries in remote <code><a href="/docs/linux/man/8-mountd/">mountd</a></code>(8) daemons. The actions specified by the options are performed for each <i>host</i> in turn.</p>
<h2>Options</h2>
<dl>
<dt><code>-a -d -e</code></p>
<dd>These options work as in <code><a href="/docs/linux/man/8-showmount/">showmount</a></code>(8) except that only entries pertaining to the local host are printed.</p>
<dt><code>-r</code></p>
<dd>Removes those remote mount entries on <i>host</i> that do not correspond to current mounts, i.e., which are left-over from a crash or are the result of improper mount protocol. The actuality of mounts is verified using the entries in <code>/etc/mtab</code>.</p>
<dt><code>-v</code></p>
<dd>Verify remote mounts. Similar to <code>-r</code> except that only a notification message is printed for each bogus entry found. The remote mount table is not changed.</p>
<dt><code>-A</code></p>
<dd>Issues a command to the remote mountd declaring that ALL of its filesystems have been unmounted. This should be used with caution, as it removes all remote mount entries pertaining to the local system, whether or not any filesystems are still mounted locally.</p>
<dt><code>-q</code></p>
<dd>Be quiet. Suppresses error messages due to timeouts and &quot;Program not registered&quot;, i.e., due to remote hosts not supporting RPC or not running mountd.</p>
<dt><code>-h</code><i>&nbsp;<wbr>name</i></p>
<dd>Pretend the local hostname is <i>name</i>. This is useful after the local hostname has been changed and rmtab entries using the old name remain on a remote machine. Unfortunately, most mountd&#8217;s won&#8217;t be able to successfully handle removal of such entries, so this option is useful in combination with <code>-v</code> only.<br />
 This option also saves time as comparisons of remotely recorded and local hostnames by address are avoided.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/mtab</code></p>
<dd>List of current mounts.</p>
<dt><code>/etc/rmtab</code></p>
<dd>Backup file for remote mount entries on NFS server.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-showmount/">showmount</a></code>(8), <code><a href="/docs/linux/man/5-mtab/">mtab</a></code>(5), <code><a href="/docs/linux/man/5-rmtab/">rmtab</a></code>(5), <code><a href="//www.systutorials.com/docs/linux/man/8C-mountd/">mountd</a></code>(8C). </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<p> <i>Amd &#8211; The 4.4 BSD Automounter</i></p>
<h2>Bugs</h2>
<p>No attempt is made to verify the information in <code>/etc/mtab</code> itself. </p>
<p> Since swap file mounts are not recorded in <code>/etc/mtab</code>, a heuristic specific to SunOS is used to determine whether such a mount is actual (replacing the string &quot;swap&quot; with &quot;root&quot; and verifying the resulting path). </p>
<p> Symbolic links on the server will cause the path in the remote entry to differ from the one in <code>/etc/mtab</code>. To catch those cases, a filesystem is also deemed mounted if its <i>local</i> mount point is identical to the remote entry. I.e., on a SunOS diskless client, <code>server:/export/share/sunos.4.1.1</code> is actually <code>/usr/share</code>. Since the local mount point is <code>/usr/share</code> as well this will be handled correctly. </p>
<p> There is no way to clear a stale entry in a remote mountd after the local hostname (or whatever reverse name resolution returns for it) has been changed. To take care of these cases, the remote /etc/rmtab file has to be edited and mountd restarted. </p>
<p> The RPC timeouts for mountd calls can only be changed by recompiling. The defaults are 2 seconds for client handle creation and 5 seconds for RPC calls.</p>
<h2>Authors</h2>
<p>Andreas Stolcke &lt;stolcke [at] icsi.berkeley.edu&gt;. </p>
<p> Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>
