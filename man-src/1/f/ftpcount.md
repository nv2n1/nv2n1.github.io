---
title: "ftpcount(1)"
name: "ftpcount"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftpcount/"
description: "ftpcount – show current number of connections for each proftpd server configuration"
---

<h2 class="name">NAME</h2>
<p> ftpcount &#8211; show current number of connections for each proftpd server configuration </p>
<h2>SYNOPSIS</h2>
<p> <code>ftpcount</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ftpcount</code> command shows the current number of connections per server and virtualhost/anonymous configuration defined in the proftpd.conf file. Connections spawned by inetd are counted separately from those created by a master proftpd <i>standalone</i> server.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h,&#8211;help</code></p>
<dd> Display a short usage description, including all available options.</p>
<dt><code>-f,&#8211;file</code><i> scoreboard-file</i></p>
<dd> Specify the full path to proftpd&#8217;s run-time scoreboard file (configured via the <code>ScoreboardFile</code> directive in <i>proftpd.conf</i> ). If proftpd&#8217;s default directory has been changed via this directive, <code>ftpcount</code> must either be recompiled or this option must be used in order to find proftpd&#8217;s scoreboard.</p>
<dt><code>-S,&#8211;server</code><i> server-name</i></p>
<dd> Specify the ServerName for a specific virtual host. If used, <i>ftpcount</i> will only show the session count for the given virtual host.</dl>
<h2>FILES</h2>
<p> <code>/usr/bin/ftpcount</code><br />
 <code>/run/proftpd/proftpd.scoreboard</code></p>
<h2>AUTHORS</h2>
<p> ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-inetd/">inetd</a>(8),</code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),<code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code><a href="/docs/linux/man/1-ftpwho/">ftpwho</a>(1),<code><a href="/docs/linux/man/1-ftptop/">ftptop</a>(1),</code><a href="/docs/linux/man/8-ftpshut/">ftpshut</a>(8) </p>
<p> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> </p>
<p> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> </p>
<p> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
<h2>Index</h2>
