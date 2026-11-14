---
title: "pure-mrtginfo(8)"
name: "pure-mrtginfo"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-mrtginfo/"
description: "pure-mrtginfo – provide an MRTG-graphable user count for ftpd"
---

<p>pure-mrtginfo &#8211; provide an MRTG-graphable user count for ftpd </p>
<h2>Synopsis</h2>
<p><code>pure-mrtginfo [server port]</code> </p>
<h2>Description</h2>
<p><code>Pure-Mrtginfo</code> counts the number of clients currently connected to <code><a href="/docs/linux/man/8-ftpd/">ftpd</a></code>(8) and output the format in a format graphable by MRTG. </p>
<h2>Options</h2>
<p><code>server port</code> : defaults to 21.</p>
<h2>Files</h2>
<dl>
<dt><i>/proc/net/tcp</i></p>
<dd>is used to count the connectiont to port 21.</p>
<dt><i>/proc/sys/kernel/hostname</i></p>
<dd>is used to get the fully qualified hostname.</p>
<dt><i>/proc/uptime</i></p>
<dd>is used to get the uptime. </p>
</dl>
<h2>Mrtg</h2>
<p>MRTG is a really nice package for graphing router traffic. Mrtg can also graph other information is available via SNMP or by running a program such as <code>pure-mrtginfo</code>. The author of this program uses it to graph CPU load, /var usage etc., and naturally the number of users connected to his FTP servers. See </p>
<pre><a rel="nofollow" href="http://oss.oetiker.ch/mrtg/">http://oss.oetiker.ch/mrtg/</a></pre>
<p>for more information about MRTG.</p>
<h2>Bugs</h2>
<p>This program only works on GNU/Linux systems yet. </p>
<h2>Home Page</h2>
<p><a rel="nofollow" href="http://www.pureftpd.org/">http://www.pureftpd.org/</a></p>
<h2>Author And License</h2>
<p>Written by Arnt Gulbrandsen &lt;agulbra [at] troll.no&gt; and copyright 1995-2002 Troll Tech AS, Waldemar Thranes gate 98B, N-0175 Oslo, Norway, fax +47 22806380. </p>
<p> Pure-FTPd (C)opyleft 2001-2015 by Frank DENIS &lt;j at pureftpd dot org&gt; and the Pure-FTPd team. </p>
<p> Use, modification and distribution is allowed without limitation, warranty, or liability of any kind.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959</code>, <code>RFC 2228,</code> <code>RFC 2389</code> and <code>RFC 2428</code>. </p>
