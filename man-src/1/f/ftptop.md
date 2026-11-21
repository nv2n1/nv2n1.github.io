---
title: "ftptop(1)"
name: "ftptop"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftptop/"
description: "ftptop – display running status on proftpd server connections"
---

<h2>SYNOPSIS</h2>
<p> <code>ftptop</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ftptop</code> command displays the current status of FTP sessions in a continuously updating <i>top</i> like format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></dt>
<dd> Filter the display to show sessions that are authenticating.</dd>
<dt><code>-a</code></dt>
<dd> Filter the display to hide sessions that are authenticating.</dd>
<dt><code>-D</code></dt>
<dd> Filter the display to show sessions that are downloading.</dd>
<dt><code>-S</code></dt>
<dd> Specify the ServerName for a specific virtual host. If used, <i>ftptop</i> will only show sessions for the given virtual host.</dd>
<dt><code>-d</code></dt>
<dd> Specify the delay, in seconds, between display refreshes. The default is 2 seconds. Only values between 0 and 15 seconds are accepted.</dd>
<dt><code>-f</code></dt>
<dd> Specify the full path to proftpd&#8217;s run-time scoreboard file (configured via the <code>ScoreboardFile</code> directive in proftpd.conf). If proftpd&#8217;s default directory has been changed via this directive, <i>ftptop</i> must either be recompiled or this option must be used in order to find proftpd&#8217;s scoreboard. <code>-h</code> Display a short usage description, including all available options.</dd>
<dt><code>-I</code></dt>
<dd> Filter the display to show sessions that are idle.</dd>
<dt><code>-i</code></dt>
<dd> Filter the display to hide sessions that are idle.</dd>
<dt><code>-U</code></dt>
<dd> Filter the display to show sessions that are uploading.</dd>
<dt><code>-V</code></dt>
<dd> Print out the version of <i>ftptop</i> and quit.</dd></dl>
<p> While <i>ftptop</i> is running, hit the &#8216;q&#8217; key to quit. The &#8216;t&#8217; key toggles between display modes. Currently there are two display modes: <code>normal</code> and <code>transfer speed</code> modes.</p>
<h2>FILES</h2>
<p> <code>/usr/bin/ftptop</code><br />
 <code>/run/proftpd/proftpd.scoreboard</code></p>
<h2>AUTHORS</h2>
<p> ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>SEE ALSO</h2>
<p> <code>inetd(8),</code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),<code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code><a href="/docs/linux/man/1-ftpwho/">ftpwho</a>(1),<code><a href="/docs/linux/man/1-ftptop/">ftptop</a>(1),</code><a href="/docs/linux/man/8-ftpshut/">ftpshut</a>(8) </p>
<p> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> </p>
<p> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> </p>
<p> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
