---
title: "inc(1)"
name: "inc"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inc/"
description: "inc – incorporate new mail"
---

<h2 class="name">NAME</h2>
<p> inc &#8211; incorporate new mail </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>inc</code> [<i>+folder</i>] [<code>-audit</code> <i>audit-file</i>] [<code>-noaudit</code>] [<code>-changecur</code> | <code>-nochangecur</code>] [<code>-form</code> <i>formfile</i>] [<code>-format</code> <i>string</i>] [<code>-file</code> <i>name</i>] [<code>-silent</code> | <code>-nosilent</code>] [<code>-truncate</code> | <code>-notruncate</code>] [<code>-width</code> <i>columns</i>] [<code>-host</code> <i>hostname</i>] [<code>-port</code> <i>portname/number</i>] [<code>-user</code> <i>username</i>] [<code>-pack</code> <i>file</i>] [<code>-nopack</code>] [<code>-proxy</code> <i>command</i>] [<code>-sasl</code> | <code>-nosasl</code>] [<code>-saslmech</code> <i>mechanism</i>] [<code>-snoop</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Inc</code></p>
<dd>incorporates mail from the user&#8217;s incoming mail drop into an <code>nmh</code> folder. If the mail drop is a file, it can be in <code>mbox</code> or <code>MMDF</code> format. If the mail drop is a directory it will considered to be a <code>Maildir</code> format mail drop. </p>
<p> You may specify which folder to use with <i>+folder</i>. If no folder is specified, then <code>inc</code> will use either the folder given by a (non-empty) &#8220;<i>Inbox</i>&#8221; entry in the user&#8217;s profile, or the folder named &#8220;<i>inbox</i>&#8221;. If the specified (or default) folder doesn&#8217;t exist, the user will be queried prior to its creation. </p>
<p> When the new messages are incorporated into the folder, they are assigned numbers starting with the next highest number for the folder. As the messages are processed, a <code>scan</code> listing of the new mail is produced. </p>
<p> If the user&#8217;s profile contains a &#8220;<i>Msg-Protect: nnn</i>&#8221; entry, it will be used as the protection on the newly created messages, otherwise the <code>nmh</code> default of 0600 will be used (on filesystems that support it). For all subsequent operations on these messages, this initially assigned protection will be preserved. </p>
<p> If the switch <code>-audit</code> <i>audit-file</i> is specified (usually as a default switch in the profile), then <code>inc</code> will append a header line and a line per message to the end of the specified audit-file with the format: </p>
<dl>
<dt>
<dd>
<pre>
&lt;&lt;inc&gt;&gt; date
&lt;scan line for first message&gt;
&lt;scan line for second message&gt;
&lt;etc.&gt;
</pre>
</dl>
<p> This is useful for keeping track of volume and source of incoming mail. Eventually, <code>repl</code>, <code>forw</code>, <code>comp</code>, and <code>dist</code> may also produce audits to this (or another) file, perhaps with &#8220;<i>Message-Id</i>&#8221; information to keep an exact correspondence history. &#8220;<i>Audit-file</i>&#8221; will be in the user&#8217;s nmh directory unless a full path is specified. </p>
<p> <code>Inc</code> will incorporate even improperly formatted messages into the user&#8217;s nmh folder, inserting a blank line prior to the offending component and printing a comment identifying the bad message. </p>
<p> In all cases, the user&#8217;s mail drop will be zeroed, unless the <code>-notruncate</code> switch is given. </p>
<p> If the profile entry &#8220;<i>Unseen-Sequence</i>&#8221; is present and non-empty, then <code>inc</code> will add each of the newly incorporated messages to each sequence named by the profile entry. <code>Inc</code> will not zero each sequence prior to adding messages. </p>
<p> The interpretation of the <code>-form</code> <i>formatfile</i>, <code>-format</code> <i>string</i>, and <code>-width</code> <i>columns</i> switches is the same as in <code>scan</code>. </p>
<p> By using the <code>-file</code> <i>name</i> switch, one can direct <code>inc</code> to incorporate messages from a file other than the user&#8217;s maildrop. Note that the name file will NOT be zeroed, unless the <code>-truncate</code> switch is given. </p>
<p> The <code>-file</code> switch does not support use of standard input. Instead, the <code>rcvstore</code> command can be used to incorporate mail from the standard input stream. </p>
<p> If the environment variable <code>$MAILDROP</code> is set, then <code>inc</code> uses it as the location of the user&#8217;s maildrop instead of the default (the <code>-file</code> <i>name</i> switch still overrides this, however). If this environment variable is not set, then <code>inc</code> will consult the profile entry &#8220;<i>MailDrop</i>&#8221; for this information. If the value found is not absolute, then it is interpreted relative to the user&#8217;s <code>nmh</code> directory. If the value is not found, then <code>inc</code> will look in the standard system location for the user&#8217;s maildrop. </p>
<p> The <code>-silent</code> switch directs <code>inc</code> to be quiet and not ask any questions at all. This is useful for putting <code>inc</code> in the background and going on to other things. </p>
<h3>Using POP</h3>
<p> <code>inc</code> will normally check local mail drops for mail, as covered above. But if the option &#8220;<i>pophost</i>&#8221; is set in &#8220;<i>mts.conf</i>&#8221;, or if the <code>-host</code> <i>hostname</i> switch is given, or if the <code>$MAILHOST</code> environment variable is set, then <code>inc</code> will query this POP service host for mail to incorporate. If <code>$MAILHOST</code> is set and <code>-host</code> is specified as well, the commandline switch will override the environment variable. The <code>-port</code> switch specifies the port name or number used to connect to the POP server. If unspecified the default is &#8220;pop3&#8221;. </p>
<p> To specify a username for authentication with the POP server, use the <code>-user</code> <i>username</i> switch. The credentials profile entry in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page describes the ways to supply a username and password. </p>
<p> If passed the <code>-proxy</code> <i>command</i> switch, <code>inc</code> will use the specified command to establish the connection to the POP server. The string <i>%h</i> in the command will be substituted by the hostname to connect to. </p>
<p> If <code>inc</code> uses POP, then the <code>-pack</code> <i>file</i> switch is considered. If given, then <code>inc</code> simply uses the POP to <code>packf</code> the user&#8217;s maildrop from the POP service host to the named file. This switch is provided for those users who prefer to use <code>msh</code> to read their maildrops. </p>
<p> For debugging purposes, you may give the switch <code>-snoop</code>, which will allow you to watch the POP transaction take place between you and the POP server. </p>
<p> If <code>nmh</code> has been compiled with SASL support, the <code>-sasl</code> switch will enable the use of SASL authentication. Depending on the SASL mechanism used, this may require an additional password prompt from the user (but the <i>netrc</i> file can be used to store this password, as described in the <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5) man page). The <code>-saslmech</code> switch can be used to select a particular SASL mechanism. </p>
<p> If SASL authentication is successful, <code>inc</code> will attempt to negotiate a security layer for session encryption. Encrypted traffic is labelled with `(encrypted)&#8217; and `(decrypted)&#8217; when viewing the POP transaction with the <code>-snoop</code> switch.</p>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</p>
<dt>/etc/nmh/mts.conf</p>
<dd> mts configuration file.</p>
<dt>/var/mail/$USER</p>
<dd> Location of the system mail drop.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory.</p>
<dt>Alternate-Mailboxes:</p>
<dd> To determine the user&#8217;s mailboxes.</p>
<dt>Inbox:</p>
<dd> To determine the inbox.</p>
<dt>Folder-Protect:</p>
<dd> To set mode when creating a new folder.</p>
<dt>Msg-Protect:</p>
<dd> To set mode when creating a new message and audit-file.</p>
<dt>Unseen-Sequence:</p>
<dd> To name sequences denoting unseen messages.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mhmail/">mhmail</a></i>(1), <i><a href="/docs/linux/man/1-scan/">scan</a></i>(1), <i><a href="/docs/linux/man/5-mh-mail/">mh-mail</a></i>(5), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5), <i><a href="/docs/linux/man/8-post/">post</a></i>(8), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>+folder</p>
<dd> defaulted by &#8220;Inbox&#8221; above.</p>
<dt>-noaudit</p>
<dd>
<dt>-changecur</p>
<dd>
<dt>-format</p>
<dd> As described above.</p>
<dt>-nosilent</p>
<dd>
<dt>-nosasl</p>
<dd>
<dt>-truncate</p>
<dd> If <code>-file</code> <i>name</i> not given, -notruncate otherwise.</p>
<dt>-width</p>
<dd> The width of the terminal.</p>
<dt>-nopack</p>
<dd></dl>
<h2>CONTEXT</h2>
<p> The folder into which messages are being incorporated will become the current folder. The first message incorporated will become the current message, unless the <code>-nochangecur</code> option is specified. This leaves the context ready for a <code>show</code> of the first new message. </p>
<h2>Index</h2>
