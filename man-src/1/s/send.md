---
title: "send(1)"
name: "send"
section: "1"
letter: "s"
url: "/docs/linux/man/1-send/"
description: "send – send a message"
---

<h2>NAME</h2>
<p> send &#8211; send a message</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>send</code> [<code>-alias</code> <i>aliasfile</i>] [<code>-draft</code>] [<code>-draftfolder</code> <i>+folder</i>] [<code>-draftmessage</code> <i>msg</i>] [<code>-nodraftfolder</code>] [<code>-filter</code> <i>filterfile</i>] [<code>-nofilter</code>] [<code>-format</code> | <code>-noformat</code>] [<code>-forward</code> | <code>-noforward</code>] [<code>-mime</code> | <code>-nomime</code>] [<code>-msgid</code> | <code>-nomsgid</code>] [<code>-messageid</code> <i>localname</i> | <i>random</i>] [<code>-push</code> | <code>-nopush</code>] [<code>-split</code> <i>seconds</i>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-watch</code> | <code>-nowatch</code>] [<code>-mts</code> <i>smtp</i> | <i>sendmail/smtp</i> | <i>sendmail/pipe</i>] [<code>-server</code> <i>servername</i>] [<code>-port</code> <i>port-name/number</i>] [<code>-sasl</code>] [<code>-nosasl</code>] [<code>-saslmaxssf</code> <i>ssf</i>] [<code>-saslmech</code> <i>mechanism</i>] [<code>-snoop</code>] [<code>-user</code> <i>username</i>] [<code>-tls</code>] [<code>-initialtls</code>] [<code>-notls</code>] [<code>-width</code> <i>columns</i>] [<code>file</code> &#8230;] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Send</code></p>
<dd>will cause each of the specified files to be delivered to each of the destinations in the &#8220;To:&#8221;, &#8220;cc:&#8221;, &#8220;Bcc:&#8221;, &#8220;Dcc:&#8221;, and &#8220;Fcc:&#8221; fields of the message. If <code>send</code> is re-distributing a message, as invoked from <code>dist</code>, then the corresponding &#8220;Resent-xxx&#8221; fields are examined instead. </p>
<p> By default, <code>send</code> uses the program <code>post</code> to do the actual delivery of the messages, although this can be changed by defining the <i>postproc</i> profile component. Most of the features attributed to <code>send</code> are actually performed by <code>post</code>. </p>
<p> Before <code>send</code> gives the message to <code>post</code> for delivery, the message is processed by <code>mhbuild</code> to perform any necessary MIME encoding of the outgoing message. This can be changed by the <i>buildmimeproc</i> profile component. <code>mhbuild</code> is invoked with the <code>-auto</code> switch, so <code>mhbuild</code> directives are not processed by default. See <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1) for more information. </p>
<p> <code>mhbuild</code> will scan the message draft for a header named <i>Attach</i>. The draft is converted to a MIME message if one or more matches are found. This conversion occurs before all other processing. The <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1) man page describes the user interface for managing MIME attachments via this mechanism. </p>
<p> The first part of the MIME message is the draft body if that body contains any non-blank characters. The body of each <i>Attach</i> header field is interpreted as a file name, and each file named is included as a separate part in the MIME message. </p>
<p> Determination of the content MIME type inserted into the Content-Type header for each part depends on how the <code>nmh</code> installation was configured. If a program, such as <code>file</code> with a <code>&#8211;mime</code> or <code>-i</code> option, was found that can specify the type of a file as a MIME type string, then that will be used. To determine if your <code>nmh</code> was so configured, run <code>mhparam mimetypeproc</code> and see if a non-empty string is displayed. </p>
<p> If your <code>nmh</code> was not configured with a program to specify a file type as a MIME string, then a different method is used to determine the content-type string. For file names with dot suffixes, the profile is scanned for a <i>mhshow-suffix-</i> entry for that suffix. The content-type for the part is taken from that profile entry if a match is found. If a match is not found in the user profile, the mhn.defaults profile is scanned next. If no match is found or the file does not have a dot suffix, the content-type is text/plain if the file contains only ASCII characters or application/octet-stream if it contains characters outside of the ASCII range. See <i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1) for more details and example syntax. </p>
<p> Each attached MIME part contains a &#8220;Content-Description&#8221; header that includes the filename, and adds a &#8220;Content-Disposition&#8221; header. Here is an example of MIME part headers for an attachment: </p>
<pre>
Content-Type: text/plain; name=&quot;VERSION&quot;; charset=&quot;us-ascii&quot;
Content-Description: VERSION
Content-Disposition: attachment; filename=&quot;VERSION&quot;
</pre>
<p> If <code>-push</code> is specified, <code>send</code> will detach itself from the user&#8217;s terminal and perform its actions in the background. If <code>push</code>&#8216;d and the draft can&#8217;t be sent, then an error message will be sent (using the mailproc) back to the user. If <code>-forward</code> is given, then a copy of the draft will be attached to this failure notice. Using <code>-push</code> differs from putting <code>send</code> in the background because the output is trapped and analyzed by <code>nmh</code>. </p>
<p> If <code>-verbose</code> is specified, <code>send</code> will indicate the interactions occurring with the transport system, prior to actual delivery. If <code>-watch</code> is specified <code>send</code> will monitor the delivery of local and network mail. Hence, by specifying both switches, a large detail of information can be gathered about each step of the message&#8217;s entry into the transport system. </p>
<p> The <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> switches invoke the <code>nmh</code> draft folder facility. This is an advanced (and highly useful) feature. Consult the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for more information. </p>
<p> If <code>-split</code> is specified, <code>send</code> will split the draft into one or more partial messages prior to sending. This makes use of the MIME features in <code>nmh</code>. Note however that if <code>send</code> is invoked under <code>dist</code>, then this switch is ignored &#8212; it makes no sense to redistribute a message in this fashion. Sometimes you want <code>send</code> to pause after posting a partial message. This is usually the case when you are running <code>sendmail</code> and expect to generate a lot of partial messages. The argument to <code>-split</code> tells it how long to pause between postings. </p>
<p> <code>Send</code> with no <i>file</i> argument will query whether the draft is the intended file, whereas <code>-draft</code> will suppress this question. Once the transport system has successfully accepted custody of the message, the file will be renamed with a site-dependent prefix (usually a comma), which allows it to be retrieved until the next draft message is sent. If there are errors in the formatting of the message, <code>send</code> will abort with a (hopefully) helpful error message. </p>
<p> If a &#8220;Bcc:&#8221; field is encountered, its addresses will be used for delivery, and the &#8220;Bcc:&#8221; field will be removed from the message sent to sighted recipients. The blind recipients will receive an entirely new message with a minimal set of headers. Included in the body of the message will be a copy of the message sent to the sighted recipients. </p>
<p> If a &#8220;Dcc:&#8221; field is encountered and the <code>sendmail/pipe</code> mail transport method is not in use, its addresses will be used for delivery, and the &#8220;Dcc:&#8221; field will be removed from the message. The blind recipients will receive the same message sent to the sighted recipients. *WARNING* Recipients listed in the &#8220;Dcc:&#8221; field receive no explicit indication that they have received a &#8220;blind copy&#8221;. This can cause blind recipients to inadvertently reply to all of the sighted recipients of the original message, revealing that they received a blind copy. On the other hand, since a normal reply to a message sent via a &#8220;Bcc:&#8221; field will generate a reply only to the sender of the original message, it takes extra effort in most mailers to reply to the included message, and so would usually only be done deliberately, rather than by accident. </p>
<p> If <code>-filter</code> <i>filterfile</i> is specified, then this copy is filtered (re-formatted) by <code>mhl</code> prior to being sent to the blind recipients. Alternately, if you specify the <code>-mime</code> switch, then <code>send</code> will use the MIME rules for encapsulation. </p>
<p> Prior to sending the message, the &#8220;Date: now&#8221; field will be appended to the headers in the message. If <code>-msgid</code> is specified, then a &#8220;Message-ID:&#8221; field will also be added to the message. </p>
<p> The <code>-messageid</code> switch selects the style used for the part appearing after the @ in &#8220;Message-ID:&#8221;, &#8220;Resent-Message-ID:&#8221;, and &#8220;Content-ID:&#8221; header fields. The two acceptable options are <code>localname</code> (which is the default), and <code>random</code>. With <code>localname</code>, the local hostname is used. With <code>random</code>, a random sequence of characters is used instead. Note that the <code>-msgid</code> switch must be enabled for this switch to have any effect. </p>
<p> If <code>send</code> is re-distributing a message (when invoked by <code>dist</code>), then &#8220;Resent-&#8221; will be prepended to each of these fields: &#8220;From:&#8221;, &#8220;Date:&#8221;, and &#8220;Message-ID:&#8221;. </p>
<p> A &#8220;From:&#8221; field is required for all outgoing messages. Multiple addresses are permitted in the &#8220;From:&#8221; field, but a &#8220;Sender:&#8221; field is required in this case. Otherwise a &#8220;Sender:&#8221; field is optional. </p>
<p> If a message with multiple &#8220;From:&#8221; addresses does <code>NOT</code> include a &#8220;Sender:&#8221; field but does include an &#8220;Envelope-From:&#8221; field, the &#8220;Envelope-From:&#8221; field will be used to construct a &#8220;Sender:&#8221; field. </p>
<p> When using SMTP for mail submission, the envelope-from used for the SMTP transaction is derived from the &#8220;Envelope-From:&#8221; field. If no &#8220;Envelope-From:&#8221; field is present, the &#8220;Sender:&#8221; field is used. If neither the &#8220;Envelope-From:&#8221; nor the &#8220;Sender:&#8221; field is present, the &#8220;From:&#8221; field is used. When &#8220;Envelope-From:&#8221; appears in a message it will be removed from the final outgoing message. </p>
<p> By using the <code>-format</code> switch, each of the entries in the &#8220;To:&#8221; and &#8220;cc:&#8221; fields will be replaced with &#8220;standard&#8221; format entries. This standard format is designed to be usable by all of the message handlers on the various systems around the Internet. If <code>-noformat</code> is given, then headers are output exactly as they appear in the message draft. </p>
<p> If an &#8220;Fcc: folder&#8221; is encountered, the message will be copied to the specified folder for the sender in the format in which it will appear to any non-Bcc receivers of the message. That is, it will have the appended fields and field reformatting. The &#8220;Fcc:&#8221; fields will be removed from all outgoing copies of the message. </p>
<p> By using the <code>-width</code> <i>columns</i> switch, the user can direct <code>send</code> as to how long it should make header lines containing addresses. </p>
<p> The mail transport system default is provided in <i>/etc/nmh/mts.conf</i> but can be overriiden here with the <code>-mts</code> switch. </p>
<p> If nmh is using the SMTP MTA, the <code>-server</code> and the <code>-port</code> switches can be used to override the default mail server (defined by the <i>/etc/nmh/mts.conf</i> servers entry). The <code>-snoop</code> switch can be used to view the SMTP transaction. (Beware that the SMTP transaction may contain authentication information either in plaintext or easily decoded base64.) </p>
<p> If <code>nmh</code> has been compiled with SASL support, the <code>-sasl</code> and <code>-nosasl</code> switches will enable and disable the use of SASL authentication with the SMTP MTA. Depending on the SASL mechanism used, this may require an additional password prompt from the user (but the <i>netrc</i> file can be used to store this password, as described in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page). The <code>-saslmech</code> switch can be used to select a particular SASL mechanism, and the <code>-user</code> switch can be used to select a authorization userid to provide to SASL other than the default. The credentials profile entry in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page describes the ways to supply a username and password. </p>
<p> If SASL authentication is successful, <code>nmh</code> will attempt to negotiate a security layer for session encryption. Encrypted data is labelled with `(encrypted)&#8217; and `(decrypted)&#8217; when viewing the SMTP transaction with the <code>-snoop</code> switch. The <code>-saslmaxssf</code> switch can be used to select the maximum value of the Security Strength Factor. This is an integer value and the exact meaning of this value depends on the underlying SASL mechanism. A value of 0 disables encryption. </p>
<p> If <code>nmh</code> has been compiled with TLS support, the <code>-tls</code> and <code>-initialtls</code> switches will require the negotiation of TLS when connecting to the SMTP MTA. The <code>-tls</code> switch will negotiate TLS as part of the normal SMTP protocol using the STARTTLS command. The <code>-initialtls</code> will negotiate TLS immediately after the connection has taken place, before any SMTP commands are sent or received. Encrypted data is labelled with `(tls-encrypted)&#8217; and `(tls-decrypted)&#8217; when viewing the SMTP transction with the <code>-snoop</code> switch. The <code>-notls</code> switch will disable all attempts to negotiate TLS. </p>
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
^Signature:~^To determine the user's mail signature
^mailproc:~^Program to post failure notices
^postproc:~^Program to post the message
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1), <i><a href="/docs/linux/man/1-dist/">dist</a></i>(1), <i><a href="/docs/linux/man/1-file/">file</a></i>(1), <i><a href="/docs/linux/man/1-forw/">forw</a></i>(1), <i><a href="/docs/linux/man/1-mhparam/">mhparam</a></i>(1), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1), <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1), <i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5), <i><a href="/docs/linux/man/5-mh-tailor/">mh-tailor</a></i>(5), <i><a href="/docs/linux/man/8-post/">post</a></i>(8)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>file</code>' defaults to &lt;mh-dir&gt;/draft
`<code>-alias</code>' defaults to /etc/nmh/MailAliases
`<code>-nodraftfolder</code>'
`<code>-nofilter</code>'
`<code>-format</code>'
`<code>-forward</code>'
`<code>-nomime</code>'
`<code>-nomsgid</code>'
`<code>-messageid localname</code>'
`<code>-nopush</code>'
`<code>-noverbose</code>'
`<code>-nowatch</code>'
`<code>-width 72</code>'
</pre>
<h2>CONTEXT</h2>
<p> None</p>
<h2>BUGS</h2>
<p> Under some configurations, it is not possible to monitor the mail delivery transaction; <code>-watch</code> is a no-op on those systems. </p>
<p> Using <code>-split</code> <i>0</i> doesn&#8217;t work correctly. </p>
<h2>Index</h2>
