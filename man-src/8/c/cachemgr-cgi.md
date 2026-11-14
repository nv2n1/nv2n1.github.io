---
title: "cachemgr-cgi(8)"
name: "cachemgr-cgi"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cachemgr-cgi/"
description: "cachemgr.cgi – Squid HTTP proxy manager CGI web interface"
---

<p>cachemgr.cgi &#8211; Squid HTTP proxy manager CGI web interface</p>
<h2>Synopsis</h2>
<p><code><a rel="nofollow" href="http://your.server/cgi-bin/cachemgr.cgi">http://your.server/cgi-bin/cachemgr.cgi</a></code></p>
<h2>Description</h2>
<p>The cache manager ( <code>cachemgr.cgi</code> ) is a CGI utility for displaying statistics about the Squid HTTP proxy process as it runs. The cache manager is a convenient way to manage the cache and view statistics without logging into the server.</p>
<h2>Configuration</h2>
<p>Configuration examples for many common web servers can be found in the Squid FAQ wiki. <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a> </p>
<p> <i>./cachemgr.conf</i><br />
 <i>/etc/squid/cachemgr.conf</i></p>
<dl>
<dd>The access configuration file defining which Squid servers may be managed via this <code>cachemgr.cgi</code> program. Each line specifies a <code>server</code>:<code>port</code> followed by an optional description </p>
<p> The server name may contain shell wildcard characters such as *, [] etc. A quick selection dropdown menu is automatically constructed from the simple server names. </p>
<p> Specifying :port is optional. If not specified then the default proxy port is assumed. :* or :any matches any port on the target server.</dl>
<h2>Security</h2>
<p><code>cachemgr.cgi</code> calls the requested server on the requested port using HTTP and returns a formatted version of the response. To avoid abuse it is recommended to configure your web server to restrict access to the <code>cachemgr.cgi</code> program.</p>
<h2>Author</h2>
<p>Derived from Harvest. Further developed by numerous individuals from the internet community. Development is led by Duane Wessels of the National Laboratory for Applied Network Research and funded by the National Science Foundation.</p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details.</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/1-squidclient/">squidclient</a></code>(1) </p>
