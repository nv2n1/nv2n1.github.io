---
title: "rpc-ypxfrd(8)"
name: "rpc-ypxfrd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpc-ypxfrd/"
description: "rpc.ypxfrd – NIS map transfer server"
---

<p>rpc.ypxfrd &#8211; NIS map transfer server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/sbin/rpc.ypxfrd</code> [-d&nbsp;<wbr><i>path</i>] [-p&nbsp;<wbr><i>port</i>] [&#8211;debug] [-f|&#8211;foreground]</p>
<dt> <code>/usr/sbin/rpc.ypxfrd</code> &#8211;version</dl>
<h2>Description</h2>
<p><code>rpc.ypxfrd</code></p>
<dd>is used for speed up the transfer of very large NIS maps from a NIS master to the NIS slave server. If a NIS slave server receives a message that there is a new map, it will start <code>ypxfr</code> for transfering the new map. <code>ypxfr</code> will read the contents of a map from the master server using the <code>yp_all</code>() function. The <code>rpc.ypxfrd</code> server speeds up the transfer process by allowing NIS slave servers to simply copy the master servers map files rather than building their own from scratch. <code>rpc.ypxfrd</code> uses an RPC-based file transfer protocol. If the on-disk format of the database on both machines is not the same, <code>rpc.ypxfrd</code> will refuse to send the data and <code>ypxfr</code> will fallback to <code>yp_all</code>() and fetch every single entry alone. <code>rpc.ypxfrd</code> could be started by inetd. But since it starts very slowly, it should be started after <code>ypserv</code> from <code>/etc/init.d/ypxfrd</code>. It is possible to pass <code>OPTIONS</code> to <code>rpc.ypxfrd</code> using the environment variable YPXFRD_ARGS and this variable can be set in <code>/etc/sysconfig/network.</code> </p>
<h2>Options</h2>
<p><code>&#8211;debug</code></p>
<dl>
<dd>Causes the server to run in debugging mode. In debug mode, the server does not background itself and prints extra status messages to stderr for each request that it revceives.</dl>
<p> <code>-d</code> <i>path</i></p>
<dl>
<dd><code>rpc.ypxfrd</code> is using this directory instead of <i>/var/yp</i>.</dl>
<p> <code>-p</code> <i>port</i></p>
<dl>
<dd><code>rpc.ypxfrd</code> will bind itself to this port, which makes it possible to have a router filter packets to the NIS ports. This can restricted the access to the NIS server from hosts on the Internet.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Prints the version number</dl>
<p> <code>-f</code>, <code>&#8211;foreground</code></p>
<dl>
<dd>will not put itself into background.</dl>
<h2>Security</h2>
<p><code>rpc.ypxfrd</code> uses the same functions for checking a host as <code>ypserv</code>. At first, <code>rpc.ypxfrd</code> will check a request from an address with <i>/var/yp/securenets</i> or the tcp wrapper. If the host is allowed to connect to the server, <code>rpc.ypxfrd</code> will uses the rules from <i>/etc/ypserv.conf</i> to check the requested map. If a mapname doesn&#8217;t match a rule, <code>rpc.ypxfrd</code> will look for the YP_SECURE key in the map. If it exists, <code>rpc.ypxfrd</code> will only allow requests on a reserved port.</p>
<h2>Notes</h2>
<p>The FreeBSD <code>ypxfrd</code> protocol is not compatible with that used by SunOS. This is unfortunate but unavoidable: SUNs protocol is not freely available, and even if it were it would probably not be useful since the SunOS NIS v2 implementation uses the original ndbm package for its map databases whereas the other implementation uses GNU DBM or Berkeley DB. These packages uses vastly different file formats. Furthermore, ndbm and gdbm are byte-order and word width sensitive and not very smart about it, meaning that a gdbm or ndbm database created on a big endian or 64bit system cannot be read on a little endian or 32bit system. The FreeBSD <code>ypxfrd</code> protocol checks, if both, master and slave, uses the same database packages and, if necessary, the byte order of the system.</p>
<h2>Files</h2>
<p><i>/etc/ypserv.conf</i></p>
<dl>
<dd>Configuration file for options and access rights</dl>
<p> <i>/var/yp/securenets</i></p>
<dl>
<dd>Configuration file for access rights</dl>
<p> <i>/etc/sysconfig/network</i></p>
<dl>
<dd>Setting additional arguments to <code>rpc.ypxfrd</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-makedbm/">makedbm</a></code>(8), <code><a href="/docs/linux/man/8-yppush/">yppush</a></code>(8), <code><a href="/docs/linux/man/8-ypxfr/">ypxfr</a></code>(8)</p>
<h2>Author</h2>
<p>ypxfrd protocol and FreeBSD Implementation: Bill Paul &lt;wpaul [at] ctr.columbia.edu&gt; </p>
<p> Linux Implementation: Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;</p>
