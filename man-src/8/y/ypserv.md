---
title: "ypserv(8)"
name: "ypserv"
section: "8"
letter: "y"
url: "/docs/linux/man/8-ypserv/"
description: "ypserv – NIS Server"
---

<p>ypserv &#8211; NIS Server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/sbin/ypserv</code> [-d] [-p&nbsp;<wbr><i>port</i>] [-f|&#8211;foreground]</dl>
<h2>Description</h2>
<dd>The Network Information Service (NIS) provides a simple network lookup service consisting of databases and processes. The databases are <code>gdbm</code> files in a directory tree rooted at /var/yp. </p>
<p> The <code>ypserv</code> daemon is typically activated at system startup. <code>ypserv</code> runs only on NIS server machines with a complete NIS database. On other machines using the NIS services, you have to run <code>ypbind</code> as client or under Linux you could use the libc with NYS support. <code>ypbind</code> must run on every machine which has NIS client processes; <code>ypserv</code> may or may not be running on the same node, but must be running somewhere on the network. On startup <code>ypserv</code> parses the file /etc/ypserv.conf. It is also possible to pass <code>OPTIONS</code> to <code>ypserv</code> using the environment variable YPSERV_ARGS and this variable can be set in <code>/etc/sysconfig/network.</code></p>
<h2>Options</h2>
<p><code>-d</code>, <code>&#8211;debug</p>
<dl>
<dd>Causes the server to run in debugging mode. Normally, ypserv</code> reports only errors (access violations, dbm failures) using the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) facility. In debug mode, the server does not background itself and prints extra status messages to stderr for each request that it revceives.</dl>
<p> <code>-p</code>, <code>&#8211;port</code> <i>port</i></p>
<dl>
<dd><code>ypserv</code> will bind itself to this port. This makes it possible to have a router filter packets to the NIS ports, so that access to the NIS server from hosts on the Internet can be restricted.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Prints the version number</dl>
<p> <code>-f</code>, <code>&#8211;foreground</code></p>
<dl>
<dd>will not put itself into background.</dl>
<h2>Security</h2>
<p>In general, any remote user can issue an RPC to <code>ypserv</code> and retrieve the contents of your NIS maps, if he knows your domain name. To prevent such unauthorized transactions, <code>ypserv</code> supports a feature called <code>securenets</code> which can be used to restrict access to a given set of hosts. At startup <code>ypserv</code> will attempt to load the securenets information from a file called /var/yp/securenets . This file contains entries that consist of a netmask and a network pair separated by white spaces. Lines starting with &#8220;#&#8221; are considered to be comments. </p>
<p> A sample securenets file might look like this:</p>
<dl>
<dd>
<dl>
<dd>
<pre># allow connections from local host -- necessary
host 127.0.0.1
# same as 255.255.255.255 127.0.0.1
#
# allow connections from any host
# on the 131.234.223.0 network
255.255.255.0 131.234.223.0
# allow connections from any host
# between 131.234.214.0 and 131.234.215.255
255.255.254.0 131.234.214.0</pre>
</dl>
</dl>
<p> If <code>ypserv</code> receives a request from an address that fails to match a rule, the request will be ignored and a warning message will be logged. If the /var/yp/securenets file does not exist, <code>ypserv</code> will allow connections from any host. </p>
<p> In the /etc/ypserv.conf you could specify some access rules for special maps and hosts. But it is not very secure, it makes the life only a little bit harder for a potential hacker. If a mapname doesn&#8217;t match a rule, ypserv will look for the YP_SECURE key in the map. If it exists, ypserv will only allow requests on a reserved port. </p>
<p> For security reasons, ypserv will only accept ypproc_xfr requests for updating maps from the same master server as the old one. This means, you have to reinstall the slave servers if you change the master server for a map.</p>
<h2>Bugs</h2>
<p>Sending the signal <code>SIGHUP</code> to the server can lead to a deadlock or crash.</p>
<h2>Files</h2>
<p>/etc/ypserv.conf</p>
<dl>
<dd>configuration file.</dl>
<p> /var/yp/securenets</p>
<dl>
<dd>which hosts are allowed to contact <code>ypserv</code>.</dl>
<p> /etc/sysconfig/network</p>
<dl>
<dd>setting additional arguments to <code>ypserv</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-domainname/">domainname</a></code>(1), <code><a href="/docs/linux/man/1-ypcat/">ypcat</a></code>(1), <code><a href="/docs/linux/man/1-ypmatch/">ypmatch</a></code>(1), <code><a href="/docs/linux/man/5-ypserv-conf/">ypserv.conf</a></code>(5), <code><a href="/docs/linux/man/5-netgroup/">netgroup</a></code>(5), <code><a href="/docs/linux/man/8-makedbm/">makedbm</a></code>(8), <code><a href="/docs/linux/man/8-revnetgroup/">revnetgroup</a></code>(8), <code><a href="/docs/linux/man/8-ypinit/">ypinit</a></code>(8), <code><a href="/docs/linux/man/8-yppoll/">yppoll</a></code>(8), <code><a href="/docs/linux/man/8-yppush/">yppush</a></code>(8), <code><a href="/docs/linux/man/8-ypset/">ypset</a></code>(8), <code><a href="/docs/linux/man/8-ypwhich/">ypwhich</a></code>(8), <code><a href="/docs/linux/man/8-ypxfr/">ypxfr</a></code>(8), <code><a href="/docs/linux/man/8-rpc-ypxfrd/">rpc.ypxfrd</a></code>(8) </p>
<p> The Network Information Service (NIS) was formerly known as Sun Yellow Pages (YP). The functionality of the two remains the same; only the name has changed. The name Yellow Pages is a registered trademark in the United Kingdom of British Telecommunications plc, and may not be used without permission.</p>
<h2>Author</h2>
<p><code>ypserv</code> was written by Peter Eriksson &lt;pen [at] lysator.liu.se&gt;. Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt; added support for master/slave server and is the new Maintainer.</p>
