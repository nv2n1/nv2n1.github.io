---
title: "post(8)"
name: "post"
section: "8"
letter: "p"
url: "/docs/linux/man/8-post/"
description: "post – deliver a message"
---

<p>post &#8211; deliver a message</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/libexec/nmh/post </code> [<code>-alias</code> <i>aliasfile</i>] [<code>-filter</code> <i>filterfile</i>] [<code>-nofilter</code>] [<code>-format</code> | <code>-noformat</code>] [<code>-mime</code> | <code>-nomime</code>] [<code>-msgid</code> | <code>-nomsgid</code>] [<code>-messageid</code> <i>localname</i> | <i>random</i>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-watch</code> | <code>-nowatch</code>] [<code>-width</code> <i>columns</i>] [<code>-mts</code> <i>smtp</i> | <i>sendmail/smtp</i> | <i>sendmail/pipe</i>] [<code>-server</code> <i>servername</i>] [<code>-port</code> <i>portname/number</i>] [<code>-sasl</code>] [<code>-nosasl</code>] [<code>-saslmaxssf</code> <i>ssf</i>] [<code>-saslmech</code> <i>mechanism</i>] [<code>-user</code> <i>username</i>] [<code>-tls</code>] [<code>-initialtls</code>] [<code>-notls</code>] <i>file</i> [<code>-version</code>] [<code>-help</code>]</dl>
<h2>Description</h2>
<p><code>Post</code></p>
<dd>is the default program called by <code>send</code> to deliver the message in <i>file</i> to local and remote users. In fact, most of the features attributed to <code>send</code> in its manual page are performed by <code>post</code>, with <code>send</code> acting as a relatively simple preprocessor. Thus, it is <code>post</code> which parses the various header fields, appends a &#8220;Date:&#8221; line, and interacts with the mail transport system. <code>Post</code> will not normally be called directly by the user. </p>
<p> <code>Post</code> searches the &#8220;To:&#8221;, &#8220;cc:&#8221;, &#8220;Bcc:&#8221;, &#8220;Fcc:&#8221;, and &#8220;Resent-xxx:&#8221; header lines of the specified message for destination addresses, checks these addresses for validity, and formats them so as to conform to ARPAnet Internet Message Format protocol, unless the <code>-noformat</code> flag is set. This will normally cause &#8220;@<i>local-site</i>&#8221; to be appended to each local destination address, as well as any local return addresses. The <code>-width</code> <i>columns</i> switch can be used to indicate the preferred length of the header components that contain addresses. </p>
<p> If a &#8220;Bcc:&#8221; field is encountered, its addresses will be used for delivery, and the &#8220;Bcc:&#8221; field will be removed from the message sent to sighted recipients. The blind recipients will receive an entirely new message with a minimal set of headers. Included in the body of the message will be a copy of the message sent to the sighted recipients. If <code>-filter</code> <i>filterfile</i> is specified, then this copy is filtered (re-formatted) by <code>mhl</code> prior to being sent to the blind recipients. Alternately, if the <code>-mime</code> switch is given, then <code>post</code> will use the MIME rules for encapsulation. </p>
<p> The <code>-alias</code> <i>aliasfile</i> switch can be used to specify a file that post should take aliases from. More than one file can be specified, each being preceded with <code>-alias</code>. In any event, the primary alias file is read first. </p>
<p> The <code>-msgid</code> switch indicates that a &#8220;Message-ID:&#8221; or &#8220;Resent-Message-ID:&#8221; field should be added to the header. </p>
<p> The <code>-messageid</code> switch selects the style used for the part appearing after the @ in &#8220;Message-ID:&#8221;, &#8220;Resent-Message-ID:&#8221;, and &#8220;Content-ID:&#8221; header fields. The two acceptable options are <code>localname</code> (which is the default), and <code>random</code>. With <code>localname</code>, the local hostname is used. With <code>random</code>, a random sequence of characters is used instead. Note that the <code>-msgid</code> switch must be enabled for this switch to have any effect. </p>
<p> The <code>-verbose</code> switch indicates that the user should be informed of each step of the posting/filing process. </p>
<p> The <code>-watch</code> switch indicates that the user would like to watch the transport system&#8217;s handling of the message (e.g., local and &#8220;fast&#8221; delivery). </p>
<p> Under normal circumstances, <code>post</code> uses the &#8220;From:&#8221; line in the message draft as the identity of the originating mailbox. A &#8220;From:&#8221; line is required in all message draft. By default the message composition utilities such as <code>comp</code>, <code>repl</code> and <code>mhmail</code> will automatically place a &#8220;From:&#8221; line in the message draft. There are two ways to override this behavior, however. Note that they apply equally to &#8220;Resent-From:&#8221; lines in messages sent with <code>dist</code>. </p>
<p> The first way is to supply a &#8220;Sender:&#8221; line. The value of this field will be used as the originating mailbox identity when submitting the message to the mail transport system. If multiple addresses are given in the &#8220;From:&#8221; line, a &#8220;Sender:&#8221; line is <code>required</code>. If an &#8220;Envelope-From:&#8221; line is supplied when multiple addresses are given in the &#8220;From:&#8221; line, a &#8220;Sender:&#8221; header will be generated using the value of the &#8220;Envelope-From:&#8221; line, <code>if</code> the &#8220;Envelope-From:&#8221; line is not blank. </p>
<p> The second way is to supply a &#8220;Envelope-From:&#8221; line. The value of this field will be used as the originating mailbox identity when submitting the message to the mail transport system. This will override both the value of the &#8220;From:&#8221; line and a &#8220;Sender:&#8221; line (if one is supplied). The &#8220;Envelope-From:&#8221; line is allowed to have a blank value; if the value is blank, then the mail transport system will be instructed to not send any bounces in response to the message. Not all mail transport systems support this feature. </p>
<p> The mail transport system default is provided in <i>/etc/nmh/mts.conf</i> but can be overriiden here with the <code>-mts</code> switch. </p>
<p> If nmh is using the SMTP MTA, the <code>-server</code> and the <code>-port</code> switches can be used to override the default mail server (defined by the servers entry in <i>/etc/nmh/mts.conf</i> ). </p>
<p> If <code>nmh</code> has been compiled with SASL support, the <code>-sasl</code> and <code>-nosasl</code> switches will enable and disable the use of SASL authentication with the SMTP MTA. Depending on the SASL mechanism used, this may require an additional password prompt from the user (but the <i>netrc</i> file can be used to store this password, as described in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page). The <code>-saslmech</code> switch can be used to select a particular SASL mechanism, and the <code>-user</code> switch can be used to select a authorization userid to provide to SASL other than the default. The credentials profile entry in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page describes the ways to supply a username and password. </p>
<p> If SASL authentication is successful, <code>nmh</code> will attempt to negotiate a security layer for session encryption. Encrypted data is labelled with `(sasl-encrypted)&#8217; and `(sasl-decrypted)&#8217; when viewing the SMTP transaction with the <code>-snoop</code> switch. The <code>-saslmaxssf</code> switch can be used to select the maximum value of the Security Strength Factor. This is an integer value and the exact meaning of this value depends on the underlying SASL mechanism. A value of 0 disables encryption. </p>
<p> If <code>nmh</code> has been compiled with TLS support, the <code>-tls</code> and <code>-initialtls</code> switches will require the negotiation of TLS when connecting to the SMTP MTA. The <code>-tls</code> switch will negotiate TLS as part of the normal SMTP protocol using the STARTTLS command. The <code>-initialtls</code> will negotiate TLS immediately after the connection has taken place, before any SMTP commands are sent or received. Encrypted data is labelled with `(tls-encrypted)&#8217; and `(tls-decrypted)&#8217; when viewing the SMTP transction with the <code>-snoop</code> switch. The <code>-notls</code> switch will disable all attempts to negotiate TLS.</p>
<h2>Files</h2>
<pre>^/etc/nmh/mts.conf~^nmh mts configuration file
^/etc/nmh/MailAliases~^global nmh alias file
^/usr/bin/refile~^Program to process Fcc:s
^/usr/libexec/nmh/mhl~^Program to process Bcc:s</pre>
<h2>Profile Components</h2>
<p><code>post</code> does <code>NOT</code> consult the user&#8217;s <i>.mh_profile</i></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-mhmail/">mhmail</a></i>(1), <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/5-mh-mail/">mh-mail</a></i>(5), <i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5), <i><a href="/docs/linux/man/5-mh-tailor/">mh-tailor</a></i>(5) </p>
<p> <i>Standard for the Format of ARPA Internet Text Messages</i> (RFC 822)</p>
<h2>Defaults</h2>
<pre>`<code>-alias</code>' defaults to /etc/nmh/MailAliases
`<code>-format</code>'
`<code>-nomime</code>'
`<code>-nomsgid</code>'
`<code>-messageid localname</code>'
`<code>-noverbose</code>'
`<code>-nowatch</code>'
`<code>-width 72</code>'
`<code>-nofilter</code>'</pre>
<h2>Context</h2>
<p>None</p>
<h2>Bugs</h2>
<p>&#8220;Reply-To:&#8221; fields are allowed to have groups in them according to the RFC 822 specification, but <code>post</code> won&#8217;t let you use them. </p>
