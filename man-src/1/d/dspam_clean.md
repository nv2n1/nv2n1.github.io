---
title: "dspam_clean(1)"
name: "dspam_clean"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dspam_clean/"
description: "dspam_clean – perform periodic maintenance of metadata"
---

<h2 class="name">NAME</h2>
<p> dspam_clean &#8211; perform periodic maintenance of metadata</p>
<h2>SYNOPSIS</h2>
<p> <code>dspam_clean</code> [<code>&#8211;profile</code>=PROFILE] [<i>-s[signature_life]</i>] [<i>-p[probability_life]</i>] [<i>-u[sl,hcl,shl,ihl]</i>] [<i>user1 user2 &#8230; userN</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>dspam_clean</code> is used to perform periodic housecleaning on DSPAM&#8217;s metadata dictionary by deleting old or useless data. </p>
<p> <code>dspam_clean</code> has no effect if you use the &quot;hash&quot; storage driver. In that case, you should use the tools <code>cssclean</code> and <code>csscompress</code> (which do not currently have manual pages). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&nbsp;<wbr>&#8211;profile=</code><i>PROFILE</i></p>
<dd> Specify a storage profile from dspam.conf. The storage profile selected will be used for all database connectivity. See dspam.conf for more information. </p>
<dt><code>-s</code></p>
<dd> Performs stale signature purging. If a value is specified, the default value of 14 days will be overridden. Specifying an age of 0 will delete all signatures from the user(s) processed. </p>
<dt><code>-p</code></p>
<dd> Deletes all tokens from the target user(s) database whose probability is between 0.35 and 0.65 (fairly neutral, useless data). If a value is specified, the default life of 30 days will be overridden. It&#8217;s a good idea to use this flag once with a life of 0 days for users after a significant amount of corpus training. </p>
<dt><code>-u</code></p>
<dd> Deletes all unused tokens from a user&#8217;s dataset. Four different life values are used: </p>
<p> <code>sl</code> Stale tokens which have not been used for a long period of time </p>
<p> <code>hcl</code> Tokens with a total hit count below 5 (which will be assigned a hapaxial value by DSPAM) </p>
<p> <code>shl</code> Tokens witha single spam hit </p>
<p> <code>ihl</code> Tokens with a single innocent hit </p>
<p> Ages may be overridden by specifying a format string, such as -u30,15,10,10 where each number represents the respective life. Specifying a life of zero will delete all unused tokens in the category. </p>
<dt><code>&nbsp;<wbr>user1 user2 &#8230; userN</code></p>
<dd> Specify the username(s) to perform the selected maintenance operations on. If no username is specified, all users are processed. </p>
</dl>
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
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_stats/">dspam_stats</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
<h2>Index</h2>
