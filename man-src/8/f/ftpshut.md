---
title: "ftpshut(8)"
name: "ftpshut"
section: "8"
letter: "f"
url: "/docs/linux/man/8-ftpshut/"
description: "ftpshut – shut down all proftpd servers at a given time"
---

<p>ftpshut &#8211; shut down all proftpd servers at a given time</p>
<h2>Synopsis</h2>
<p><code>ftpshut</code> [ <code>-R</code> ] [ <code>-l</code><i> min </i> ] [ <code>-d</code><i> min </i> ] <i>time</i> [ <i>warning-message </i> ]</p>
<h2>Description</h2>
<p>The <code>ftpshut</code> command provides an automated shutdown procedure that a superuser can use to automagically disconnect current proftpd connections, and deny new connections. The command creates a control file as <code>/etc/shutmsg</code> to inform proftpd processes about an impending shutdown.</p>
<h2>Options</h2>
<dl>
<dt><code>time</code></p>
<dd>The time at which the ftp servers will be brought down. It may be the word `now&#8217;, indicating an immediate shutdown, or a future time in one of two formats: <i>+number </i> or <i>HHMM. </i> The first form brings the servers down in <i>number</i> minutes, while the second form indicates an exact time of day, using a 24-hour clock format.</p>
<dt><code>-R</code></p>
<dd>Instructs ftpshut to <i>remove</i> the /etc/shutmsg file, restoring proftpd to its normal service. If this option is used, this will be the only operation performed by <i>ftpshut</i></p>
<dt><code>-l min</code></p>
<dd>Specifies the number of minutes before shutdown that new ftp access will be disabled. If the -l option is not specified, a default of 10 minutes (or immediately, if less than 10 minutes remains until shutdown) is used.</p>
<dt><code>-d min</code></p>
<dd>Specifies the number of minutes before shutdown that existing ftp connections will be disconnected. If the -d option is not specified, a default of 5 minutes (or immediately, if less than 5 minutes remains until shutdown) is used.</p>
<dt><code>warning-message</code></p>
<dd>Optionally provide a message which will be sent to new connections (if denied) and existing connections (when disconnected). The message can contain the following magic cookies, which will be replaced as follows before being sent to new or existing connections:</p>
<dl>
<dd>
<dl>
<dt><code>%s</code></p>
<dd>time proftpd is being shut down</p>
<dt><code>%r</code></p>
<dd>time new connections will be denied</p>
<dt><code>%d</code></p>
<dd>time current connections will be dropped</p>
<dt><code>%C</code></p>
<dd>current working directory (where applicable)</p>
<dt><code>%L</code></p>
<dd>local host name (or virtualhost name)</p>
<dt><code>%R</code></p>
<dd>remote host name</p>
<dt><code>%T</code></p>
<dd>local time (format Thu Nov 15 17:12:42 1990)</p>
<dt><code>%U</code></p>
<dd>username given at login time</dl>
</dl>
</dl>
<h2>Caveats</h2>
<p>Proftpd servers can only be shutdown via ftpshut if a master daemon is running in <i>standalone </i> mode. Servers running in <i>inetd </i> mode will honor the shutdown message file created by ftpshut, however currently running servers may be <a href="/docs/linux/man/2-chroot/">chroot</a>(2)ed, and unable to read the shutdown message control file. </p>
<p> It is possible to set an absolute shutdown time which is <code>earlier </code> than the current time. If this is the case, proftpd will not shutdown until the indicated time on the following day.</p>
<h2>Files</h2>
<p><code>/usr/sbin/ftpshut</code><br />
 <code>/etc/shutmsg</code></p>
<h2>Authors</h2>
<p>ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-inetd/">inetd</a>(8),</code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),<code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8),</code><a href="/docs/linux/man/1-ftpwho/">ftpwho</a>(1),<code><a href="/docs/linux/man/1-ftpcount/">ftpcount</a>(1)</code> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
