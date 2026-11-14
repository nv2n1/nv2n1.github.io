---
title: "ypinit(8)"
name: "ypinit"
section: "8"
letter: "y"
url: "/docs/linux/man/8-ypinit/"
description: "ypinit – NIS database install and build program"
---

<p>ypinit &#8211; NIS database install and build program</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/lib/yp/ypinit</code> [-m] [-s&nbsp;<wbr><i>master_name</i>]</dl>
<h2>Description</h2>
<p><code>ypinit</code></p>
<dd>builds the domain subdirectory of FC/var/ypF[] for the current default domain. After building the domain subdirectory, <code>ypinit</code> builds a complete set of administrative maps for your system and places them in this directory. The first map created by <code>ypinit -m</code> is the ypservers map. You should run it as root on the hosts, which should be the master ypserver.You should have only one master server per NIS domain. </p>
<p> All databases are built from scratch, either from information available to the program at runtime, or from the ASCII data base files in FC/etcF[]. These files are listed below under FILES. </p>
<p> An NIS database on a slave server is set up by copying an existing database from a running server. The <code>master_name</code> argument should be the hostname of an NIS server (either the master server for all the maps, or a server on which the data base is up-to-date and stable).</p>
<h2>Options</h2>
<p><code>-m</code></p>
<dl>
<dd>If the local host is the NIS master.</dl>
<p> <code>-s</code></p>
<dl>
<dd>Set up a slave server with the database from <i>master_name</i></dl>
<h2>Files</h2>
<p>FC/etc/passwdF[], FC/etc/groupF[], FC/etc/hostsF[], FC/etc/networksF[], FC/etc/servicesF[], FC/etc/protocolsF[], FC/etc/netgroupF[], FC/etc/rpcF[]</p>
<dl>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-makedbm/">makedbm</a></code>(8), <code><a href="/docs/linux/man/8-revnetgroup/">revnetgroup</a></code>(8), <code><a href="/docs/linux/man/8-yppush/">yppush</a></code>(8), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-ypxfr/">ypxfr</a></code>(8)</p>
<h2>Bugs</h2>
<p>There is no good error handling at the moment.</p>
<h2>Author</h2>
<p>Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;</p>
