---
title: "dspam_dump(1)"
name: "dspam_dump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam_dump/"
description: "dspam_dump – produce a dump of a user’s metadata"
---

<h2 class="name">NAME</h2>
<p> dspam_dump &#8211; produce a dump of a user&#8217;s metadata</p>
<h2>SYNOPSIS</h2>
<p> <code>dspam_dump</code> [<code>&#8211;profile</code>=PROFILE] [<code>-d</code><br />
&nbsp;<wbr>sqlite_drv] <code>username</code> [<code>token</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>dspam_dump</code> dumps a user&#8217;s metadata dictionary to stdout. This can be used to view the entire contents of a user&#8217;s dictionary, or used in combination with grep to view a subset of data. The output provides the token&#8217;s stored value (in CRC64 format), the number of spam and nonspam hits, and the token&#8217;s computed probability. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&nbsp;<wbr>&#8211;profile=</code><i>PROFILE</i></p>
<dd> Specify a storage profile from dspam.conf. The storage profile selected will be used for all database connectivity. See dspam.conf for more information. </p>
<dt><code>&nbsp;<wbr>username</code><i></i></p>
<dd> The username of the user to dump. Only trusted users (or root) can use this program for the usernames different from the current one.<br />
&nbsp;<wbr></p>
<dt><code>&nbsp;<wbr>token</code><i></i></p>
<dd>
 The text string of the token to search for and dump. If no token is specified, all tokens will be dumped to stdout. </p>
</dl>
<h2>EXAMPLES</h2>
<p> <code>dspam_dump user Subject*Viagra</code> </p>
<p> Dumps the token Subject*Viagra, which represents the word Viagra in the Subject header, for the user specified. </p>
<h2>EXIT VALUE</h2>
<dl>
<dt><code>0</code></p>
<dd> Operation was successful.</p>
<dt><code>other</code></p>
<dd> Operation resulted in an error. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 DSPAM Project<br />
 All rights reserved. </p>
<p> For more information, see <a rel="nofollow" href="http://dspam.sourceforge.net.">http://dspam.sourceforge.net.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_stats/">dspam_stats</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
<h2>Index</h2>
