---
title: "ftpscrub(8)"
name: "ftpscrub"
section: "8"
letter: "f"
url: "/docs/linux/man/8-ftpscrub/"
description: "ftpscrub – scrub the proftpd scoreboard file of stale entries"
---

<p>ftpscrub &#8211; scrub the proftpd scoreboard file of stale entries</p>
<h2>Synopsis</h2>
<p><code>ftpscrub</code></p>
<h2>Description</h2>
<p>The <code>ftpscrub</code> command provides a way to scrub the scoreboard file on demand, at times which suit the site best. This should be run periodically on sites which run proftpd in <i>inetd</i> mode.</p>
<h2>Options</h2>
<dl>
<dt><code>-h,&#8211;help</code></p>
<dd>Display a short usage description, including all available options.</p>
<dt><code>-f,&#8211;file</code><i> scoreboard-file</i></p>
<dd>Specify the full path to proftpd&#8217;s run-time scoreboard file (configured via the <code>ScoreboardFile</code> directive in <i>proftpd.conf</i> ). If proftpd&#8217;s default directory has been changed via this directive, <code>ftpscrub</code> must either be recompiled, or this option must be used in order to find proftpd&#8217;s scoreboard.</p>
<dt><code>-v,&#8211;verbose</code></p>
<dd>Reports additional information while scrubbing the scoreboard.</dl>
<h2>Files</h2>
<p><code>/usr/sbin/ftpscrub</code><br />
 <code>/run/proftpd/proftpd.scoreboard</code></p>
<h2>Authors</h2>
<p>ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-inetd/">inetd</a>(8),</code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),<code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code><a href="/docs/linux/man/1-ftpwho/">ftpwho</a>(1),<code><a href="/docs/linux/man/1-ftpcount/">ftpcount</a>(1)</code> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
