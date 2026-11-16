---
title: "basic_db_auth(8)"
name: "basic_db_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_db_auth/"
---

<pre> basic_db_auth - Database auth helper for Squid</pre>
<h2>Synopsis</h2>
<pre> basic_db_auth [options]</pre>
<h2>Descriptoin</h2>
<p>This program verifies username &amp; password to a database</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;debug</code></dt>
<dd>Write debug info to stderr.</dd>
<dt><code>&#8211;dsn</code></dt>
<dd>Database <font SIZE="-1">DSN.</font> Default &#8220;DBI:mysql:database=squid&#8221;</dd>
<dt><code>&#8211;user</code></dt>
<dd>Database User</dd>
<dt><code>&#8211;password</code></dt>
<dd>Database password</dd>
<dt><code>&#8211;table</code></dt>
<dd>Database table. Default &#8220;passwd&#8221;.</dd>
<dt><code>&#8211;usercol</code></dt>
<dd>Username column. Default &#8220;user&#8221;.</dd>
<dt><code>&#8211;passwdcol</code></dt>
<dd>Password column. Default &#8220;password&#8221;.</dd>
<dt><code>&#8211;cond</code></dt>
<dd>Condition, defaults to enabled=1. Specify 1 or &quot;&quot; for no condition If you use &#8211;joomla flag, this condition will be changed to block=0</dd>
<dt><code>&#8211;plaintext</code></dt>
<dd>Database contains plain-text passwords</dd>
<dt><code>&#8211;md5</code></dt>
<dd>Database contains unsalted md5 passwords</dd>
<dt><code>&#8211;salt</code></dt>
<dd>Selects the correct salt to evaluate passwords</dd>
<dt><code>&#8211;persist</code></dt>
<dd>Keep a persistent database connection open between queries.</dd>
<dt><code>&#8211;joomla</code></dt>
<dd>Tells helper that user database is Joomla <font SIZE="-1">DB. </font> So their unusual salt hashing is understood.</dd></dl>
<h2>Author</h2>
<p>This program was written by <i>Henrik Nordstrom &lt;henrik [at] henriknordstrom.net</i>&gt; and <i>Luis Daniel Lucio Quiroz &lt;dlucio [at] okay.com.mx</i>&gt; </p>
<p> This manual was written by <i>Henrik Nordstrom &lt;henrik [at] henriknordstrom.net</i>&gt;</p>
<h2>Copyright</h2>
<pre> * Copyright (C) 1996-2016 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.</pre>
<p>Copyright (C) 2007 Henrik Nordstrom &lt;henrik [at] henriknordstrom.net&gt; Copyright (C) 2010 Luis Daniel Lucio Quiroz &lt;dlucio [at] okay.com.mx&gt; (Joomla support) This program is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License version 2, or (at youropinion) any later version.</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list &lt;squid-users [at] squid-cache.org</i>&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org</i>&gt; </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list &lt;squid-dev [at] squid-cache.org</i>&gt;</p>
<h2>See Also</h2>
<p>squid (8), <font SIZE="-1">GPL \fIs0(7), The Squid </font><font SIZE="-2">FAQ</font> wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a> The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
