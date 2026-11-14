---
title: "ext_session_acl(8)"
name: "ext_session_acl"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ext_session_acl/"
description: "ext_session_acl – Squid session tracking external acl helper."
---

<p>ext_session_acl &#8211; Squid session tracking external acl helper. </p>
<p> Version 1.2</p>
<h2>Synopsis</h2>
<p><code>ext_session_acl</code> <code>[-t</code> timeout <code>] [-b</code> database <code>] [-a]</code></p>
<h2>Description</h2>
<p><code>ext_session_acl</code> maintains a concept of sessions by monitoring requests and timing out sessions. The timeout is based either on idle use ( <code>-t</code> ) or a fixed period of time ( <code>-T</code> ). The former is suitable for displaying terms and conditions to a user; the latter is suitable for the display of advertisments or other notices (both as a splash page &#8211; see config examples in the wiki online). The session helper can also be used to force users to re-authenticate if the <code>%LOGIN </code> and <code>-a</code> are both used.</p>
<h2>Options</h2>
<dl>
<dt><code>-t timeout</code></p>
<dd>Idle timeout for any session. The default if not specified (set to 3600 seconds).</p>
<dt><code>-T timeout</code></p>
<dd>Fixed timeout for any session. This will end the session after the timeout regardless of a user&#8217;s activity. If used with <code>active</code> mode, this will terminate the user&#8217;s session after <code>timeout</code> , after which another <code>LOGIN</code> will be required. <code>LOGOUT</code> will reset the session and timeout.</p>
<dt><code>-b path</code></p>
<dd><code>Path</code> to persistent database. If a file is specified then that single file is used as the database. If a path is specified, a Berkeley DB database environment is created within the directory. The advantage of the latter is better database support between multiple instances of the session helper. Using multiple instances of the session helper with a single database file will cause synchronisation problems between processes. If this option is not specified the session details will be kept in memory only and all sessions will reset each time Squid restarts its helpers (Squid restart or rotation of logs).</p>
<dt><code>-a</code></p>
<dd>Active mode. In this mode sessions are started by evaluating an acl with the argument <code>LOGIN</code> , or terminated by the argument <code>LOGOUT .</code> Without this flag the helper automatically starts the session after the first request.</dl>
<h2>Configuration</h2>
<p>The <code>ext_session_acl</code> helper is a concurrent helper; therefore, the concurrency= option <code>must</code> be specified in the configuration. </p>
<p> Passive session configuration example using the default automatic mode</p>
<dl>
<dd><code>external_acl_type session ttl=300 negative_ttl=0 children=1 concurrency=200 %LOGIN /usr/local/squid/libexec/ext_session_acl</code><br />
 <code>acl session external session</code><br />
 <code>http_access deny !session</code><br />
 <code>deny_info <a rel="nofollow" href="http://your.server.example.com/bannerpage?url=%s">http://your.server.example.com/bannerpage?url=%s</a> session</code></dl>
<p> Then set up <code><a rel="nofollow" href="http://your.server.example.com/bannerpage">http://your.server.example.com/bannerpage</a> </code> to display a session startup page and then redirect the user back to the requested URL given in the url query parameter.</p>
<h2>Author</h2>
<p>This program and documentation was written by <i>Henrik Nordstrom &lt;henrik [at] henriknordstrom.net&gt;</i> <i>Andrew Beverley &lt;andy [at] andybev.com&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> This program and documentation is copyright to the authors named above. </p>
<p> Distributed under the GNU General Public License (GNU GPL) version 2 or later (GPLv2+).</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
