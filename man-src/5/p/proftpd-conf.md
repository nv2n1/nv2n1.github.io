---
title: "proftpd-conf(5)"
name: "proftpd-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-proftpd-conf/"
description: "proftpd.conf – ProFTPD server configuration file"
---

<p>proftpd.conf &#8211; ProFTPD server configuration file</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8)</code> daemon reads its configuration file, typically stored in one of the following locations: </p>
<p> <i>/etc/proftpd.conf</i><br />
 <i>/etc/proftpd/proftpd.conf</i><br />
 <i>/usr/local/etc/proftpd.conf</i></p>
<dl>
<dt>or passed to proftpd with the -c command-line option.</p>
<dd></dl>
<p> The <code>proftpd.conf</code> configuration file contains <i>directives</i> , one per line. Lines starting with # and empty lines are comments and are ignored. Directives are case-insensitive, whereas values are case-sensitive. Values may be enclosed in double-quotes (&quot;) if they contain spaces. </p>
<p> The possible directives and their descriptions are described online at <code><a rel="nofollow" href="http://www.proftpd.org/docs/directives/linked/by-name.html">http://www.proftpd.org/docs/directives/linked/by-name.html</a></code></p>
<h2>Files</h2>
<p><code>/usr/sbin/proftpd</code><br />
 <code>/etc/proftpd.conf</code></p>
<h2>Authors</h2>
<p>ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8)</code> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
