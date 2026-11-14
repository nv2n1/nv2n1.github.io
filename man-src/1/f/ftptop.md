---
title: "ftptop(1)"
name: "ftptop"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftptop/"
description: "ftptop – display running status on proftpd server connections"
---

<h2 class="name">NAME</h2>
<p> ftptop &#8211; display running status on proftpd server connections </p>
<h2>SYNOPSIS</h2>
<p> <code>ftptop</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ftptop</code> command displays the current status of FTP sessions in a continuously updating <i>top</i> like format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Filter the display to show sessions that are authenticating.</p>
<dt><code>-a</code></p>
<dd> Filter the display to hide sessions that are authenticating.</p>
<dt><code>-D</code></p>
<dd> Filter the display to show sessions that are downloading.</p>
<dt><code>-S</code></p>
<dd> Specify the ServerName for a specific virtual host. If used, <i>ftptop</i> will only show sessions for the given virtual host.</p>
<dt><code>-d</code></p>
<dd> Specify the delay, in seconds, between display refreshes. The default is 2 seconds. Only values between 0 and 15 seconds are accepted.</p>
<dt><code>-f</code></p>
<dd> Specify the full path to proftpd&#8217;s run-time scoreboard file (configured via the <code>ScoreboardFile</code> directive in proftpd.conf). If proftpd&#8217;s default directory has been changed via this directive, <i>ftptop</i> must either be recompiled or this option must be used in order to find proftpd&#8217;s scoreboard. <code>-h</code> Display a short usage description, including all available options.</p>
<dt><code>-I</code></p>
<dd> Filter the display to show sessions that are idle.</p>
<dt><code>-i</code></p>
<dd> Filter the display to hide sessions that are idle.</p>
<dt><code>-U</code></p>
<dd> Filter the display to show sessions that are uploading.</p>
<dt><code>-V</code></p>
<dd> Print out the version of <i>ftptop</i> and quit.</dl>
<p> While <i>ftptop</i> is running, hit the &#8216;q&#8217; key to quit. The &#8216;t&#8217; key toggles between display modes. Currently there are two display modes: <code>normal</code> and <code>transfer speed</code> modes.</p>
<h2>FILES</h2>
<p> <code>/usr/bin/ftptop</code><br />
 <code>/run/proftpd/proftpd.scoreboard</code></p>
<h2>AUTHORS</h2>
<p> ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-inetd/">inetd</a>(8),</code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),<code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code><a href="/docs/linux/man/1-ftpwho/">ftpwho</a>(1),<code><a href="/docs/linux/man/1-ftptop/">ftptop</a>(1),</code><a href="/docs/linux/man/8-ftpshut/">ftpshut</a>(8) </p>
<p> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> </p>
<p> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> </p>
<p> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
<h2>Index</h2>
