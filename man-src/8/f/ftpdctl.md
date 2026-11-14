---
title: "ftpdctl(8)"
name: "ftpdctl"
section: "8"
letter: "f"
url: "/docs/linux/man/8-ftpdctl/"
description: "ftpdctl – ProFTPD control program"
---

<p>ftpdctl &#8211; ProFTPD control program</p>
<h2>Synopsis</h2>
<p><code>ftpdctl</code> [ <code>-hv</code> ] [ <code>-s</code><i> Unix domain socket</i> ] <code>action</code><i> action-parameters</i></p>
<h2>Description</h2>
<p><code>ftpdctl</code> is the control program for the Professional File Transfer Protocol (FTP) server daemon. The control program is used to control the daemon while it is running, supporting actions like restarting or shutting down the daemon, disabling or enabling specific virtual servers, kicking FTP users, etc. </p>
<p> The specific <code>actions</code> available via <code>ftpdctl</code> depend on the modules compiled into <code>proftpd.</code> Check the modules documentation for more information on the specific <code>actions</code> supported by the modules.</p>
<h2>Options</h2>
<dl>
<dt><code>-h,&#8211;help</code></p>
<dd>Display a short usage description, including all available options.</p>
<dt><code>-s,&#8211;socket</code></p>
<dd>Specifies an alternate <code>path</code> to be used for communicating with <code>proftpd</code> rather than the default Unix domain socket. The default controls socket is <code>/var/run/proftpd/proftpd.sock</code></p>
<dt><code>-v,&#8211;verbose</code></p>
<dd>Display informational messages while communicating with the <code>proftpd</code> daemon.</p>
<dd></dl>
<h2>Authors</h2>
<p>ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),<code><a href="/docs/linux/man/1-ftpwho/">ftpwho</a>(1),</code><a href="/docs/linux/man/1-ftpcount/">ftpcount</a>(1),<code><a href="/docs/linux/man/8-ftpshut/">ftpshut</a>(8)</code> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
