---
title: "ftpwho(1)"
name: "ftpwho"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftpwho/"
description: "ftpwho – show current process information for each FTP session"
---

<h2 class="name">NAME</h2>
<p> ftpwho &#8211; show current process information for each FTP session </p>
<h2>SYNOPSIS</h2>
<p> <code>ftpwho</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ftpwho</code> command shows process information for all active proftpd connections, and a count of all connected users off of each server. Proftpd sesssions spawned from inetd are counted separately from those created by a master proftpd <i>standalone</i> server.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h,&#8211;help</code></p>
<dd> Display a short usage description, including all available options.</p>
<dt><code>-f,&#8211;file</code><i> scoreboard-file</i></p>
<dd> Specify the full path to proftpd&#8217;s run-time scoreboard file (configured via the <code>ScoreboardFile</code> directive in <i>proftpd.conf</i> ). If proftpd&#8217;s default directory has been changed via this directive, <code>ftpwho</code> must either be recompiled, or this option must be used in order to find proftpd&#8217;s scoreboard.</p>
<dt><code>-o,&#8211;outform</code><i> format</i></p>
<dd> Specify an output format. Currently, two &quot;formats&quot; are supported: <code>compat</code> and <code>oneline</code>. The <code>compat</code> format is used for backward compatibility. The <code>oneline</code> format causes all of the fields for a session to be displayed on a single line, for ease of line-based searches (e.g. grep).</p>
<dt><code>-v,&#8211;verbose</code></p>
<dd> Reports additional information for each connection, such as the remote host and current working directory. <code>-S,&#8211;server</code><i> server-name</i> Specify the ServerName for a specific virtual host. If used, <i>ftpwho</i> will only show session information for the given virtual host.</dl>
<h2>FILES</h2>
<p> <code>/usr/bin/ftpwho</code><br />
 <code>/run/proftpd/proftpd.scoreboard</code></p>
<h2>AUTHORS</h2>
<p> ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-inetd/">inetd</a>(8),</code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),<code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code><a href="/docs/linux/man/1-ftpcount/">ftpcount</a>(1),<code><a href="/docs/linux/man/1-ftptop/">ftptop</a>(1),</code><a href="/docs/linux/man/8-ftpshut/">ftpshut</a>(8) </p>
<p> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> </p>
<p> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> </p>
<p> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
<h2>Index</h2>
