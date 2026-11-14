---
title: "isync(1)"
name: "isync"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isync/"
description: "isync – synchronize IMAP4 and Maildir mailboxes"
---

<h2 class="name">NAME</h2>
<p> isync &#8211; synchronize IMAP4 and Maildir mailboxes </p>
<h2>SYNOPSIS</h2>
<p> <code>isync</code> [<i>options</i> &#8230;] {<i>mailbox</i> &#8230;|<i>-a</i>|<i>-l</i>}</p>
<h2>DESCRIPTION</h2>
<p> <code>isync</code> is a command line application which synchronizes local Maildir mailboxes with remote IMAP4 mailboxes, suitable for use in IMAP-disconnected mode. Multiple copies of the remote IMAP4 mailboxes can be maintained, and all flags are synchronized.<br />
 <code>isync</code> is only a wrapper binary around <code>mbsync</code> to simplify upgrades. It will automatically migrate the UID mapping from previous versions of <code>isync</code> (even before 0.8) to the new format, and transparently call <code>mbsync</code>. If you were using <code>isync</code> version 0.8 or 0.9.x you might want to use <code>mdconvert</code> to convert the mailboxes to the more efficient <code>native</code> UID storage scheme after migrating them.<br />
 <code>isync</code> is deprecated. Please use the <code>-w</code> option to permanently migrate the configuration and start using <code>mbsync</code> directly.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></p>
<dd> Read configuration from <i>file</i>. By default, the configuration is read from ~/.isyncrc if it exists.</p>
<dt><code>-1</code>, <code>&#8211;one-to-one</code></p>
<dd> Instead of using the mailbox specifications in ~/.isyncrc, isync will pick up all mailboxes from the local directory and remote folder and map them 1:1 onto each other according to their names.</p>
<dt><code>-I</code>, <code>&#8211;inbox</code> <i>mailbox</i></p>
<dd> Exception to the 1:1 mapping created by -1: the special IMAP mailbox <i>INBOX</i> is mapped to the local <i>mailbox</i> (relative to the maildir).</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> Synchronize all mailboxes (either specified in ~/.isyncrc or determined by the 1:1 mapping).</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Don&#8217;t synchronize anything, but list all mailboxes and exit.</p>
<dt><code>-L</code>, <code>&#8211;create-local</code></p>
<dd> Automatically create the local Maildir mailbox if it doesn&#8217;t already exist.</p>
<dt><code>-R</code>, <code>&#8211;create-remote</code></p>
<dd> Automatically create the remote IMAP mailbox if it doesn&#8217;t already exist.</p>
<dt><code>-C</code>, <code>&#8211;create</code></p>
<dd> Automatically create any mailboxes if they don&#8217;t already exist. This is simply a combination of -L and -R.</p>
<dt><code>-d</code>, <code>&#8211;delete</code></p>
<dd> Causes <code>isync</code> to propagate message deletions. By default, <i>dead</i> messages are <code>not</code> deleted.</p>
<dt><code>-e</code>, <code>&#8211;expunge</code></p>
<dd> Causes <code>isync</code> to permanently remove all messages marked for deletion. By default, <i>deleted</i> messages are <code>not</code> expunged.</p>
<dt><code>-f</code>, <code>&#8211;fast</code></p>
<dd> Only fetch new messages existing on the server into the local mailbox. Message deletions and flag changes will not be propagated.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Displays a summary of command line options</p>
<dt><code>-p</code>, <code>&#8211;port</code> <i>port</i></p>
<dd> Specifies the port on the IMAP server to connect to (default: 143 for imap, 993 for imaps)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress informational messages. If specified twice, suppress warning messages as well.</p>
<dt><code>-r</code>, <code>&#8211;remote</code> <i>box</i></p>
<dd> Specifies the name of the remote IMAP mailbox to synchronize with (Default: INBOX)</p>
<dt><code>-s</code>, <code>&#8211;host</code> [<code>imaps:</code>]<i>host</i></p>
<dd> Specifies the hostname of the IMAP server</p>
<dt><code>-u</code>, <code>&#8211;user</code> <i>user</i></p>
<dd> Specifies the login name to access the IMAP server (default: $USER)</p>
<dt><code>-P</code>, <code>&#8211;pass</code> <i>password</i></p>
<dd> Specifies the password to access the IMAP server (prompted for by default)</p>
<dt><code>-M</code>, <code>&#8211;maildir</code> <i>dir</i></p>
<dd> Specifies the location for your local mailboxes.</p>
<dt><code>-F</code>, <code>&#8211;folder</code> <i>folder</i>/</p>
<dd> Specifies the location for your remote mailboxes.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays <code>isync</code> version information.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Enables <i>verbose</i> mode, which displays the IMAP4 network traffic.</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> Enable printing of <i>debug</i> messages.</p>
<dt><code>-w</code>, <code>&#8211;write</code></p>
<dd> Don&#8217;t run <code>mbsync</code>, but instead write a permanent config file for it. The UID mappings of all configured mailboxes will be migrated. Note that most command line options that would affect an actual sync operation will be incorporated into the new config file as well; exceptions are &#8211;fast and &#8211;create[-remote|-local]. The name of the new config file is determined by replacing the last occurrence of &quot;isync&quot; with &quot;mbsync&quot;, or appending &quot;.mbsync&quot; if &quot;isync&quot; was not found.</p>
<dt><code>-W</code>, <code>&#8211;writeto</code> <i>file</i></p>
<dd> Like <code>-w</code>, but use the specified name for the new config file.</dl>
<h2>CONFIGURATION</h2>
<p> <code>isync</code> by default reads <i>~/.isyncrc</i> to load configuration data. Each non-empty line of the configuration file that does not start with a hash mark consists of a command. The following commands are understood:</p>
<dl>
<dt><code>Mailbox</code> <i>path</i></p>
<dd> Defines a local Maildir mailbox. All configuration commands following this line, up until the next <i>Mailbox</i> command, apply to this mailbox only.</p>
<dt><code>Host</code> [<code>imaps:</code>]<i>name</i></p>
<dd> Defines the DNS name or IP address of the IMAP server. If the hostname is prefixed with <code>imaps:</code> the connection is assumed to be a SSL connection to port 993 (though you can change this by placing a <code>Port</code> command <code>after</code> the <code>Host</code> command). Note that modern servers support SSL on the default port 143. <code>isync</code> will always attempt to use SSL if available.</p>
<dt><code>Port</code> <i>port</i></p>
<dd> Defines the TCP port number of the IMAP server (Default: 143 for imap, 993 for imaps)</p>
<dt><code>Box</code> <i>mailbox</i></p>
<dd> Defines the name of the remote IMAP mailbox associated with the local Maildir mailbox (Default: INBOX)</p>
<dt><code>User</code> <i>username</i></p>
<dd> Defines the login name on the IMAP server (Default: current user)</p>
<dt><code>Pass</code> <i>password</i></p>
<dd> Defines the password for <i>username</i> on the IMAP server. Note that this option is <code>NOT</code> required. If no password is specified in the configuration file, <code>isync</code> will prompt you for it.</p>
<dt><code>Alias</code> <i>string</i></p>
<dd> Defines an alias for the mailbox which can be used as a shortcut on the command line.</p>
<dt><code>CopyDeletedTo</code> <i>mailbox</i></p>
<dd> Specifies the remote IMAP mailbox to copy deleted messages to prior to expunging (Default: none).</p>
<dt><code>Delete</code> <i>yes</i>|<i>no</i></p>
<dd> Specifies whether message deletions are propagated. (Default: no). <code>NOTE:</code> The <i>-d</i> command line option overrides this setting when set to <i>no</i>.</p>
<dt><code>Expunge</code> <i>yes</i>|<i>no</i></p>
<dd> Specifies whether deleted messages are expunged. (Default: no). <code>NOTE:</code> The <i>-e</i> command line option overrides this setting when set to <i>no</i>.</p>
<dt><code>MailDir</code> <i>directory</i></p>
<dd> Specifies the location of your local mailboxes if a relative path is specified in a <i>Mailbox</i> command (Default: <i>~</i>). <code>NOTE:</code> This directive is allowed only in the <i>global</i> section (see below).</p>
<dt><code>Folder</code> <i>directory</i>/</p>
<dd> Specifies the location of your IMAP mailboxes specified in <i>Box</i> commands (Default: <i>&quot;&quot;</i>). <code>NOTE:</code> You <code>must</code> append the hierarchy delimiter (usually a slash) to this specification. <code>NOTE 2:</code> This directive is allowed only in the <i>global</i> section (see below).</p>
<dt><code>MaxMessages</code> <i>count</i></p>
<dd> Sets the number of messages <code>isync</code> should keep in the local copy of a mailbox. This is useful for mailboxes where you keep a complete archive on the server, but want to mirror only the last messages (for instance, for mailing lists). The messages that were the first to arrive in the mailbox (independently of the actual date of the message) will be deleted first. Messages that are flagged (marked as important) and unread messages will not be automatically deleted. If <i>count</i> is 0, the maximum number of messages is <code>unlimited</code>. (Default: 0)</p>
<dt><code>MaxSize</code> <i>bytes</i></p>
<dd> Messages larger than that many bytes will not be transferred over the wire. This is useful for weeding out messages with large attachments. If <i>bytes</i> is 0, the maximum file size is <code>unlimited</code>. (Default: 0)</p>
<dt><code>Tunnel</code> <i>command</i></p>
<dd> Specify a command to run to establish a connection rather than opening a TCP socket. This allows you to run an IMAP session over an SSH tunnel, for example.</p>
<dt><code>UseNamespace</code> <i>yes</i>|<i>no</i></p>
<dd> Selects whether the server&#8217;s first &quot;personal&quot; NAMESPACE should be prefixed to mailbox names. Disabling this makes sense for some broken IMAP servers. This option is meaningless if a <i>Folder</i> was specified. (Default: <i>yes</i>)</p>
<dt><code>RequireCRAM</code> <i>yes</i>|<i>no</i></p>
<dd> If set to <i>yes</i>, <code>isync</code> will abort the connection if no CRAM-MD5 authentication is possible. (Default: <i>no</i>)</p>
<dt><code>RequireSSL</code> <i>yes</i>|<i>no</i></p>
<dd> <code>isync</code> will abort the connection if a TLS/SSL session cannot be established with the IMAP server. (Default: <i>yes</i>)</p>
<dt><code>CertificateFile</code> <i>path</i></p>
<dd> File containing X.509 CA certificates used to verify server identities.</p>
<dt><code>UseSSLv2</code> <i>yes</i>|<i>no</i></p>
<dd> Should <code>isync</code> use SSLv2 for communication with the IMAP server over SSL? (Default: <i>no</i>)</p>
<dt><code>UseSSLv3</code> <i>yes</i>|<i>no</i></p>
<dd> Should <code>isync</code> use SSLv3 for communication with the IMAP server over SSL? (Default: <i>yes</i> if the imaps port is used, otherwise <i>no</i>)</p>
<dt><code>UseTLSv1</code> <i>yes</i>|<i>no</i></p>
<dd> Should <code>isync</code> use TLSv1 for communication with the IMAP server over SSL? (Default: <i>yes</i>)</p>
<dt><code>OneToOne</code></p>
<dd> <code>isync</code> will ignore any <i>Mailbox</i> specifications and instead pick up all mailboxes from the local <i>MailDir</i> and remote <i>Folder</i> and map them 1:1 onto each other according to their names. <code>NOTE:</code> This directive is allowed only in the <i>global</i> section (see below).</p>
<dt><code>Inbox</code> <i>mailbox</i></p>
<dd> Exception to the OneToOne mapping: the special IMAP mailbox <i>INBOX</i> is mapped to the local <i>mailbox</i> (relative to the <i>MailDir</i>). <code>NOTE:</code> This directive is only meaningful in the <i>global</i> section (see below).</dl>
<p> Configuration commands that appear prior to the first <code>Mailbox</code> command are considered to be <i>global</i> options which are used as defaults when those specific options are not specifically set for a defined Mailbox. For example, if you use the same login name for several IMAP servers, you can put a <code>User</code> command before the first <code>Mailbox</code> command, and then leave out the <code>User</code> command in the sections for each mailbox. <code>isync</code> will then use the global value by default.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.isyncrc</code></p>
<dd> Default configuration file</dl>
<h2>BUGS</h2>
<p> The configuration file takes precedence over command line options.<br />
 Use -c /dev/null to work around. </p>
<p> See the <code>INHERENT PROBLEMS</code> section in the <code>mbsync</code> man page, too.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mbsync/">mbsync</a>(1), <a href="/docs/linux/man/1-mdconvert/">mdconvert</a>(1), <a href="/docs/linux/man/1-mutt/">mutt</a>(1), <a href="/docs/linux/man/5-maildir/">maildir</a>(5) </p>
<p> Up to date information on <code>isync</code> can be found at <a rel="nofollow" href="http://isync.sf.net/">http://isync.sf.net/</a></p>
<h2>AUTHORS</h2>
<p> Originally written by Michael R. Elkins, currently maintained by Oswald Buddenhagen. </p>
<h2>Index</h2>
