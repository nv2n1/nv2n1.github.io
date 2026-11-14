---
title: "msgchk(1)"
name: "msgchk"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msgchk/"
description: "msgchk – check for messages"
---

<h2 class="name">NAME</h2>
<p> msgchk &#8211; check for messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>msgchk</code> [<code>-date</code> | <code>-nodate</code>] [<code>-notify</code></p>
<dd>all/mail/nomail ] [<code>-nonotify</code> all/mail/nomail ] [<code>-host</code> <i>hostname</i>] [<code>-user</code> <i>username</i>] [<code>-sasl</code>] [<code>-saslmech</code> <i>mechanism</i>] [<code>-snoop</code>] [<i>users</i> &#8230; ] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> The <code>msgchk</code> program checks all known mail drops for mail waiting for you. For those drops which have mail for you, <code>msgchk</code> will indicate if it believes that you have seen the mail in question before. </p>
<p> The <code>-notify</code> <i>type</i> switch indicates under what circumstances <code>msgchk</code> should produce a message. The default is <code>-notify</code> <i>all</i> which says that <code>msgchk</code> should always report the status of the users maildrop. Other values for `type&#8217; include `mail&#8217; which says that <code>msgchk</code> should report the status of waiting mail; and, `nomail&#8217; which says that <code>msgchk</code> should report the status of empty maildrops. The <code>-nonotify</code> <i>type</i> switch has the inverted sense, so <code>-nonotify</code> <i>all</i> directs <code>msgchk</code> to never report the status of maildrops. This is useful if the user wishes to check <code>msgchk</code>&#8216;s exit status. A non-zero exit status indicates that mail was <code>not</code> waiting for at least one of the indicated users. </p>
<p> If <code>msgchk</code> produces output, then the <code>-date</code> switch directs <code>msgchk</code> to print out the last date mail was read, if this can be determined.</p>
<h3>Using POP</h3>
<p> <code>msgchk</code> will normally check all the local mail drops, but if the option &#8220;pophost:&#8221; is set in the mts configuration file &#8220;mts.conf&#8221;, or if the <code>-host</code> <i>hostname</i> switch is given, <code>msgchk</code> will query this POP service host as to the status of mail waiting. </p>
<p> To specify a username for authentication with the POP server, use the <code>-user</code> <i>username</i> switch. The credentials profile entry in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page describes the ways to supply a username and password. </p>
<p> For debugging purposes, there is also a switch <code>-snoop</code>, which will allow you to watch the POP transaction take place between you and the POP server. </p>
<p> If <code>nmh</code> has been compiled with SASL support, the <code>-sasl</code> switch will enable the use of SASL authentication. Depending on the SASL mechanism used, this may require an additional password prompt from the user (but the <i>netrc</i> file can be used to store this password, as described in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page). The <code>-saslmech</code> switch can be used to select a particular SASL mechanism. </p>
<p> If SASL authentication is successful, <code>inc</code> will attempt to negotiate a security layer for session encryption. Encrypted traffic is labelled with `(encrypted)&#8217; and `(decrypted)&#8217; when viewing the POP transaction with the <code>-snoop</code> switch.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
^/etc/nmh/mts.conf~^nmh mts configuration file
^/var/mail/$USER~^Location of mail drop
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
None
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1), <i><a href="/docs/linux/man/5-mh-mail/">mh-mail</a></i>(5)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>user</code>' defaults to the current user
`<code>-date</code>'
`<code>-notify all</code>'
</pre>
<h2>CONTEXT</h2>
<p> None </p>
<h2>Index</h2>
