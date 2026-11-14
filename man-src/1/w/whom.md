---
title: "whom(1)"
name: "whom"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whom/"
description: "whom – report to whom a message would go"
---

<h2 class="name">NAME</h2>
<p> whom &#8211; report to whom a message would go </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>whom</code> [<code>-alias</code> <i>aliasfile</i>] [<code>-check</code> | <code>-nocheck</code>] [<code>-draftfolder</code> <i>+folder</i>] [<code>-draftmessage</code> <i>msg</i>] [<code>-nodraftfolder</code>] [<code>-mts</code> <i>smtp</i> | <i>sendmail/smtp</i> | <i>sendmail/pipe</i>] [<code>-server</code> <i>servername</i>] [<code>-port</code> <i>port-name/number</i>] [<code>-sasl</code>] [<code>-saslmech</code> <i>mechanism</i>] [<code>-snoop</code>] [<code>-user</code> <i>username</i>] [<code>-tls</code>] [<code>-notls</code>] [<i>file</i>] [<code>-draft</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Whom</code></p>
<dd>is used to expand the headers of a message into a set of addresses and optionally verify that those addresses are deliverable at that time (if <code>-check</code> is given). </p>
<p> The <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> switches invoke the <code>nmh</code> draft folder facility. This is an advanced (and highly useful) feature. Consult the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for more information. </p>
<p> The mail transport system default is provided in <i>/etc/nmh/mts.conf</i> but can be overriiden here with the <code>-mts</code> switch. </p>
<p> If nmh is using the SMTP MTA, the <code>-server</code> and the <code>-port</code> switches can be used to override the default mail server (defined by the <i>/etc/nmh/mts.conf</i> servers entry). The <code>-snoop</code> switch can be used to view the SMTP transaction. (Beware that the SMTP transaction may contain authentication information either in plaintext or easily decoded base64.) </p>
<p> If <code>nmh</code> has been compiled with SASL support, the <code>-sasl</code> switch will enable the use of SASL authentication with the SMTP MTA. Depending on the SASL mechanism used, this may require an additional password prompt from the user (but the <i>netrc</i> file can be used to store this password, as described in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page). The <code>-saslmech</code> switch can be used to select a particular SASL mechanism, and the <code>-user</code> switch can be used to select a authorization userid to provide to SASL other than the default. The credentials profile entry in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page describes the ways to supply a username and password. </p>
<p> If SASL authentication is successful, <code>nmh</code> will attempt to negotiate a security layer for session encryption. Encrypted data is labelled with `(encrypted)&#8217; and `(decrypted)&#8217; when viewing the SMTP transaction with the <code>-snoop</code> switch. The <code>-saslmaxssf</code> switch can be used to select the maximum value of the Security Strength Factor. This is an integer value and the exact meaning of this value depends on the underlying SASL mechanism. A value of 0 disables encryption. </p>
<p> If <code>nmh</code> has been compiled with TLS support, the <code>-tls</code> and <code>-notls</code> switches will require and disable the negotiation of TLS support when connecting to the SMTP MTA. Encrypted data is labelled with `(tls-encrypted)&#8217; and `(tls-decrypted)&#8217; when viewing the SMTP transction with the <code>-snoop</code> switch. </p>
<p> The files specified by the profile entry &#8220;Aliasfile:&#8221; and any additional alias files given by the <code>-alias</code> <i>aliasfile</i> switch will be read (more than one file, each preceded by <code>-alias</code>, can be named). See <i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5) for more information.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Draft-Folder:~^To find the default draft-folder
^Aliasfile:~^For a default alias file
^postproc:~^Program to post the message
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5), <i><a href="/docs/linux/man/8-post/">post</a></i>(8)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>file</code>' defaults to &lt;mh-dir&gt;/draft
`<code>-nocheck</code>'
`<code>-alias</code>' defaults to  /etc/nmh/MailAliases
</pre>
<h2>CONTEXT</h2>
<p> None</p>
<h2>BUGS</h2>
<p> With the <code>-check</code> option, <code>whom</code> makes no guarantees that the addresses listed as being ok are really deliverable, rather, an address being listed as ok means that at the time that <code>whom</code> was run the address was thought to be deliverable by the transport service. For local addresses, this is absolute; for network addresses, it means that the host is known; for uucp addresses, it (often) means that the <code>UUCP</code> network is available for use. </p>
<h2>Index</h2>
