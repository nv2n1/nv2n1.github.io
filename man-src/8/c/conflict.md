---
title: "conflict(8)"
name: "conflict"
section: "8"
letter: "c"
url: "/docs/linux/man/8-conflict/"
description: "conflict – search for alias/password conflicts"
---

<p>conflict &#8211; search for alias/password conflicts</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/libexec/nmh/conflict</code> [<code>-search</code> <i>directory</i>] [<code>-mail</code> <i>name</i>] [<code>-version</code>] [<code>-help</code>] [<i>aliasfiles</i> &#8230;]</dl>
<h2>Description</h2>
<p><code>Conflict is deprecated and will be removed from the next nmh release.</code> </p>
<p> <code>Conflict</code></p>
<dd>is a program that checks to see if the interface between <code>nmh</code> and the transport system is in good shape </p>
<p> <code>Conflict</code> also checks for maildrops in /var/mail which do not belong to a valid user. It assumes that no user name will start with `.&#8217;, and thus ignores files in /var/mail which begin with `.&#8217;. It also checks for entries in the <i><a href="/docs/linux/man/5-group/">group</a></i>(5) file which do not belong to a valid user, and for users who do not have a valid group number. In addition duplicate users and groups are noted. </p>
<p> If the <code>-mail</code> <i>name</i> switch is used, then the results will be sent to the specified <i>name</i>. Otherwise, the results are sent to the standard output. </p>
<p> The <code>-search</code> <i>directory</i> switch can be used to search directories other than /var/mail and to report anomalies in those directories. The <code>-search</code> <i>directory</i> switch can appear more than one time in an invocation to <code>conflict</code>. </p>
<p> <code>Conflict</code> should be run under <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8), or whenever system accounting takes place.</p>
<h2>Files</h2>
<pre>^/etc/nmh/mts.conf~^nmh mts configuration file
^/etc/passwd~^List of users
^/etc/group~^List of groups
^/usr/bin/mhmail~^Program to send mail
^/var/mail/~^Directory of mail drop</pre>
<h2>Profile Components</h2>
<p>None</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5)</p>
<h2>Defaults</h2>
<pre>`<code>aliasfiles</code>' defaults to /etc/nmh/MailAliases</pre>
<h2>Context</h2>
<p>None</p>
