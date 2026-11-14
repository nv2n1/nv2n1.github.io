---
title: "mbsync(1)"
name: "mbsync"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mbsync/"
description: "mbsync – synchronize IMAP4 and Maildir mailboxes"
---

<h2 class="name">NAME</h2>
<p> mbsync &#8211; synchronize IMAP4 and Maildir mailboxes </p>
<h2>SYNOPSIS</h2>
<p> <code>mbsync</code> [<i>options</i> &#8230;] &#123;&#123;<i>channel</i>[<code>:</code><i>box</i>[{<code>,</code>|<code>
</code>}&#8230;]]|<i>group</i>} &#8230;|<code>-a</code>}</p>
<h2>DESCRIPTION</h2>
<p> <code>mbsync</code> is a command line application which synchronizes mailboxes; currently Maildir and IMAP4 mailboxes are supported. New messages, message deletions and flag changes can be propagated both ways; the operation set can be selected in a fine-grained manner.<br />
 Synchronization is based on unique message identifiers (UIDs), so no identification conflicts can occur (as opposed to some other mail synchronizers). OTOH, <code>mbsync</code> is susceptible to UID validity changes (that <i>should</i> never happen, but see &quot;Compatibility&quot; in the README). Synchronization state is kept in one local text file per mailbox pair; multiple replicas of a mailbox can be maintained.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></p>
<dd> Read configuration from <i>file</i>. By default, the configuration is read from ~/.mbsyncrc.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> Select all configured channels. Any channel/group specifications on the command line are ignored.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Don&#8217;t synchronize anything, but list all mailboxes in the selected channels and exit.</p>
<dt><code>-C</code>[<code>m</code>][<code>s</code>], <code>&#8211;create</code>[<code>-master</code>|<code>-slave</code>]</p>
<dd> Override any <code>Create</code> options from the config file. See below.</p>
<dt><code>-R</code>[<code>m</code>][<code>s</code>], <code>&#8211;remove</code>[<code>-master</code>|<code>-slave</code>]</p>
<dd> Override any <code>Remove</code> options from the config file. See below.</p>
<dt><code>-X</code>[<code>m</code>][<code>s</code>], <code>&#8211;expunge</code>[<code>-master</code>|<code>-slave</code>]</p>
<dd> Override any <code>Expunge</code> options from the config file. See below.</p>
<dt>{<code>-n</code>|<code>-N</code>|<code>-d</code>|<code>-f</code>|<code>-0</code>|<code>-F</code>},<br />
&nbsp;<wbr>{<code>&#8211;new</code>|<code>&#8211;renew</code>|<code>&#8211;delete</code>|<code>&#8211;flags</code>|<code>&#8211;noop</code>|<code>&#8211;full</code>}</p>
<dd>
<dt>{<code>-L</code>|<code>-H</code>}[<code>n</code>][<code>N</code>][<code>d</code>][<code>f</code>],<br />
&nbsp;<wbr>{<code>&#8211;pull</code>|<code>&#8211;push</code>}[<code>-new</code>|<code>-renew</code>|<code>-delete</code>|<code>-flags</code>]</p>
<dd> Override any <code>Sync</code> options from the config file. See below.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a summary of command line options.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Enable <i>verbose</i> mode, which displays what is currently happening.</p>
<dt><code>-D</code>[<code>C</code>][<code>m</code>][<code>M</code>][<code>n</code>|<code>N</code>][<code>s</code>]],<br />
&nbsp;<wbr><code>&#8211;debug</code>[<code>-crash</code>|<code>-maildir</code>|<code>-main</code>|<code>-net</code>|<code>-net-all</code>|<code>-sync</code>]</p>
<dd> Enable debugging categories: <code>C</code>, <code>crash</code> &#8211; use built-in crash handler<br />
 <code>m</code>, <code>maildir</code> &#8211; print maildir debug info<br />
 <code>M</code>, <code>main</code> &#8211; print main debug info<br />
 <code>n</code>, <code>net</code> &#8211; print network traffic (protocol only)<br />
 <code>N</code>, <code>net-all</code> &#8211; print network traffic (including payloads)<br />
 <code>s</code>, <code>sync</code> &#8211; print synchronization debug info All categories except <code>crash</code> implictly enable <i>verbose</i> mode. Without category specification, all categories except net-all are enabled.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress progress counters (this is implicit if stdout is no TTY, or any debugging categories are enabled) and notices. If specified twice, suppress warning messages as well.</dl>
<h2>CONFIGURATION</h2>
<p> The configuration file is mandatory; <code>mbsync</code> will not run without it. Lines starting with a hash mark (<code>#</code>) are comments and are ignored entirely. Configuration items are keywords followed by one or more arguments; arguments containing spaces must be enclosed in double quotes (<code>&quot;</code>), and literal double quotes and backslashes (<code>\</code>) must be backslash-escaped. All keywords (including those used as arguments) are case-insensitive. Bash-like home directory expansion using the tilde (<code>~</code>) is supported in all options which represent local paths. There are a few global options, the rest applies to particular sections. Sections are started by a section keyword and are terminated by an empty line or end of file. Every section defines an object with an identifier unique within that object class. </p>
<p> There are two basic object classes: Stores and Channels. A Store defines a collection of mailboxes; basically a folder, either local or remote. A Channel connects two Stores, describing the way the two are synchronized.<br />
 There are two auxiliary object classes: Accounts and Groups. An Account describes the connection part of remote Stores, so a server connection can be shared between multiple Stores. A Group aggregates multiple Channels to save typing on the command line. </p>
<p> File system locations (in particular, <code>Path</code> and <code>Inbox</code>) use the Store&#8217;s internal path separators, which may be slashes, periods, etc., or even combinations thereof.<br />
 Mailbox names, OTOH, always use canonical path separators, which are Unix-like forward slashes.</p>
<h3>All Stores</h3>
<p> These options can be used in all supported Store types.<br />
 In this context, the term &quot;remote&quot; describes the second Store within a Channel, and not necessarily a remote server.<br />
 The special mailbox <code>INBOX</code> exists in every Store; its physical location in the file system is Store type specific.</p>
<dl>
<dt><code>Path</code> <i>path</i></p>
<dd> The location of the Store in the (server&#8217;s) file system. If this is no absolute path, the reference point is Store type specific. This string is prepended to the mailbox names addressed in this Store, but is not considered part of them; this is important for <code>Patterns</code> in the Channels section. Note that you <code>must</code> append a slash if you want to specify an entire directory. (Default: none)</p>
<dt><code>MaxSize</code> <i>size</i>[<code>k</code>|<code>m</code>][<code>b</code>]</p>
<dd> Messages larger than that will not be propagated into this Store. This is useful for weeding out messages with large attachments. <code>K</code> and <code>M</code> can be appended to the size to specify KiBytes resp. MeBytes instead of bytes. <code>B</code> is accepted but superfluous. If <i>size</i> is 0, the maximum message size is <code>unlimited</code>. (Default: <i>0</i>)</p>
<dt><code>MapInbox</code> <i>mailbox</i></p>
<dd> Create a virtual mailbox (relative to <code>Path</code>) which aliases the <code>INBOX</code>. Makes sense in conjunction with <code>Patterns</code> in the Channels section, though with a Maildir slave, you probably want to place <code>Inbox</code> under <code>Path</code> instead. This virtual mailbox does not support subfolders.</p>
<dt><code>Flatten</code> <i>delim</i></p>
<dd> Flatten the hierarchy within this Store by substituting the canonical hierarchy delimiter <code>/</code> with <i>delim</i>. This can be useful when the MUA used to access the Store provides suboptimal handling of hierarchical mailboxes, as is the case with <code>Mutt</code>. A common choice for the delimiter is <code>.</code>.<br />
 Note that flattened sub-folders of the <code>INBOX</code> always end up under <code>Path</code>, including the &quot;INBOX<i>delim</i>&quot; prefix.</p>
<dt><code>Trash</code> <i>mailbox</i></p>
<dd> Specifies a mailbox (relative to <code>Path</code>) to copy deleted messages to prior to expunging. See <code>RECOMMENDATIONS</code> and <code>INHERENT PROBLEMS</code> below. (Default: none)</p>
<dt><code>TrashNewOnly</code> <i>yes</i>|<i>no</i></p>
<dd> When trashing, copy only not yet propagated messages. This makes sense if the remote Store has a <code>Trash</code> as well (with <code>TrashNewOnly</code> <i>no</i>). (Default: <i>no</i>)</p>
<dt><code>TrashRemoteNew</code> <i>yes</i>|<i>no</i></p>
<dd> When expunging the remote Store, copy not yet propagated messages to this Store&#8217;s <code>Trash</code>. When using this, the remote Store does not need an own <code>Trash</code> at all, yet all messages are archived. (Default: <i>no</i>)</dl>
<h3>Maildir Stores</h3>
<p> The reference point for relative <code>Path</code>s is the current working directory. </p>
<p> As <code>mbsync</code> needs UIDs, but no standardized UID storage scheme exists for Maildir, <code>mbsync</code> supports two schemes, each with its pros and cons.<br />
 The <code>native</code> scheme is stolen from the latest Maildir patches to <code>c-client</code> and is therefore compatible with <code>pine</code>. The UID validity is stored in a file named .uidvalidity; the UIDs are encoded in the file names of the messages.<br />
 The <code>alternative</code> scheme is based on the UID mapping used by <code>isync</code> versions 0.8 and 0.9.x. The invariant parts of the file names of the messages are used as keys into a Berkeley database named .isyncuidmap.db, which holds the UID validity as well.<br />
 The <code>native</code> scheme is faster, more space efficient, endianness independent and &quot;human readable&quot;, but will be disrupted if a message is copied from another mailbox without getting a new file name; this would result in duplicated UIDs sooner or later, which in turn results in a UID validity change, making synchronization fail. The <code>alternative</code> scheme would fail if a MUA changed a message&#8217;s file name in a part <code>mbsync</code> considers invariant; this would be interpreted as a message deletion and a new message, resulting in unnecessary traffic.<br />
 <code>Mutt</code> is known to work fine with both schemes.<br />
 Use <code>mdconvert</code> to convert mailboxes from one scheme to the other.</p>
<dl>
<dt><code>MaildirStore</code> <i>name</i></p>
<dd> Define the Maildir Store <i>name</i>, opening a section for its parameters.</p>
<dt><code>AltMap</code> <i>yes</i>|<i>no</i></p>
<dd> Use the <code>alternative</code> UID storage scheme for mailboxes in this Store. This does not affect mailboxes that do already have a UID storage scheme; use <code>mdconvert</code> to change it. (Default: <i>no</i>)</p>
<dt><code>Inbox</code> <i>path</i></p>
<dd> The location of the <code>INBOX</code>. This is <i>not</i> relative to <code>Path</code>, but it is allowed to place the <code>INBOX</code> inside the <code>Path</code>. (Default: <i>~/Maildir</i>)</p>
<dt><code>InfoDelimiter</code> <i>delim</i></p>
<dd> The character used to delimit the info field from a message&#8217;s basename. The Maildir standard defines this to be the colon, but this is incompatible with DOS/Windows file systems. (Default: the value of <code>FieldDelimiter</code>)</dl>
<h3>IMAP4 Accounts</h3>
<dl>
<dt><code>IMAPAccount</code> <i>name</i></p>
<dd> Define the IMAP4 Account <i>name</i>, opening a section for its parameters.</p>
<dt><code>Host</code> <i>host</i></p>
<dd> Specify the DNS name or IP address of the IMAP server.<br />
 If <code>Tunnel</code> is used, this setting is needed only if <code>SSLType</code> is not <i>None</i> and <code>CertificateFile</code> is not used, in which case the host name is used for certificate subject verification.</p>
<dt><code>Port</code> <i>port</i></p>
<dd> Specify the TCP port number of the IMAP server. (Default: 143 for IMAP, 993 for IMAPS)<br />
 If <code>Tunnel</code> is used, this setting is ignored.</p>
<dt><code>User</code> <i>username</i></p>
<dd> Specify the login name on the IMAP server.</p>
<dt><code>Pass</code> <i>password</i></p>
<dd> Specify the password for <i>username</i> on the IMAP server. Note that this option is <code>NOT</code> required. If neither a password nor a password command is specified in the configuration file, <code>mbsync</code> will prompt you for a password.</p>
<dt><code>PassCmd</code> [<code>+</code>]<i>command</i></p>
<dd> Specify a shell command to obtain a password rather than specifying a password directly. This allows you to use password files and agents. The command must produce exactly one line on stdout; the trailing newline is optional. Prepend <code>+</code> to the command to indicate that it produces TTY output (e.g., a decryption password prompt); failure to do so will merely produce messier output.</p>
<dt><code>Tunnel</code> <i>command</i></p>
<dd> Specify a command to run to establish a connection rather than opening a TCP socket. This allows you to run an IMAP session over an SSH tunnel, for example.</p>
<dt><code>AuthMechs</code> <i>type</i> &#8230;</p>
<dd> The list of acceptable authentication mechanisms. In addition to the mechanisms listed in the SASL registry (link below), the legacy IMAP <code>LOGIN</code> mechanism is known. The wildcard <code>*</code> represents all mechanisms that are deemed secure enough for the current <code>SSLType</code> setting. The actually used mechanism is the most secure choice from the intersection of this list, the list supplied by the server, and the installed SASL modules. (Default: <code>*</code>)</p>
<dt><code>SSLType</code> {<i>None</i>|<i>STARTTLS</i>|<i>IMAPS</i>}</p>
<dd> Select the connection security/encryption method:<br />
 <i>None</i> &#8211; no security. This is the default when <code>Tunnel</code> is set, as tunnels are usually secure.<br />
 <i>STARTTLS</i> &#8211; security is established via the STARTTLS extension after connecting the regular IMAP port 143. Most servers support this, so it is the default (unless a tunnel is used).<br />
 <i>IMAPS</i> &#8211; security is established by starting SSL/TLS negotiation right after connecting the secure IMAP port 993.</p>
<dt><code>SSLVersions</code> [<i>SSLv2</i>] [<i>SSLv3</i>] [<i>TLSv1</i>] [<i>TLSv1.1</i>] [<i>TLSv1.2</i>]</p>
<dd> Select the acceptable SSL/TLS versions. Use of SSLv2 is strongly discouraged for security reasons, but might be the only option on some very old servers. Generally, the newest TLS version is recommended, but as this confuses some servers, <code>TLSv1</code> is the default.</p>
<dt><code>SystemCertificates</code> <i>yes</i>|<i>no</i></p>
<dd> Whether the system&#8217;s default root cerificate store should be loaded. (Default: <i>yes</i>)</p>
<dt><code>CertificateFile</code> <i>path</i></p>
<dd> File containing additional X.509 certificates used to verify server identities. Directly matched peer certificates are always trusted, regardless of validity.<br />
 Note that the system&#8217;s default certificate store is always used (unless <code>SystemCertificates</code> is disabled) and should not be specified here.</p>
<dt><code>PipelineDepth</code> <i>depth</i></p>
<dd> Maximum number of IMAP commands which can be simultaneously in flight. Setting this to <i>1</i> disables pipelining. This is mostly a debugging only option. (Default: <i>unlimited</i>)</dl>
<h3>IMAP Stores</h3>
<p> The reference point for relative <code>Path</code>s is whatever the server likes it to be; probably the user&#8217;s $HOME or $HOME/Mail on that server. The location of <code>INBOX</code> is up to the server as well and is usually irrelevant.</p>
<dl>
<dt><code>IMAPStore</code> <i>name</i></p>
<dd> Define the IMAP4 Store <i>name</i>, opening a section for its parameters.</p>
<dt><code>Account</code> <i>account</i></p>
<dd> Specify which IMAP4 Account to use. Instead of defining an Account and referencing it here, it is also possible to specify all the Account options directly in the Store&#8217;s section &#8211; this makes sense if an Account is used for one Store only anyway.</p>
<dt><code>UseNamespace</code> <i>yes</i>|<i>no</i></p>
<dd> Selects whether the server&#8217;s first &quot;personal&quot; NAMESPACE should be prefixed to mailbox names. Disabling this makes sense for some broken IMAP servers. This option is meaningless if a <code>Path</code> was specified. (Default: <i>yes</i>)</p>
<dt><code>PathDelimiter</code> <i>delim</i></p>
<dd> Specify the server&#8217;s hierarchy delimiter. (Default: taken from the server&#8217;s first &quot;personal&quot; NAMESPACE)<br />
 Do <code>NOT</code> abuse this to re-interpret the hierarchy. Use <code>Flatten</code> instead.</dl>
<h3>Channels</h3>
<dl>
<dt><code>Channel</code> <i>name</i></p>
<dd> Define the Channel <i>name</i>, opening a section for its parameters.</p>
<dt>{<code>Master</code>|<code>Slave</code>} <code>:</code><i>store</i><code>:</code>[<i>mailbox</i>]</p>
<dd> Specify the Master resp. Slave Store to be connected by this Channel. If <code>Patterns</code> are specified, <i>mailbox</i> is interpreted as a prefix which is not matched against the patterns, and which is not affected by mailbox list overrides. Otherwise, if <i>mailbox</i> is omitted, <code>INBOX</code> is assumed.</p>
<dt><code>Pattern</code>[<code>s</code>] [<code>!</code>]<i>pattern</i> &#8230;</p>
<dd> Instead of synchronizing only one mailbox pair, synchronize all mailboxes that match the <i>pattern</i>(s). The mailbox names are the same on both Master and Slave. Patterns are IMAP4 patterns, i.e., <code>*</code> matches anything and <code>%</code> matches anything up to the next hierarchy delimiter. Prepending <code>!</code> to a pattern makes it an exclusion. Multiple patterns can be specified (either by supplying multiple arguments or by using <code>Pattern</code> multiple times); later matches take precedence.<br />
 Note that <code>INBOX</code> is not matched by wildcards, unless it lives under <code>Path</code>.<br />
 The mailbox list selected by <code>Patterns</code> can be overridden by a mailbox list in a channel reference (a <code>Group</code> specification or the command line).<br />
 Example: &quot;<code>Patterns</code>&nbsp;<wbr><i>%&nbsp;<wbr>!Trash</i>&quot;</p>
<dt><code>MaxSize</code> <i>size</i>[<code>k</code>|<code>m</code>][<code>b</code>]</p>
<dd> Analogous to the homonymous option in the Stores section, but applies equally to Master and Slave. Note that this actually modifies the Stores, so take care not to provide conflicting settings if you use the Stores in multiple Channels.</p>
<dt><code>MaxMessages</code> <i>count</i></p>
<dd> Sets the maximum number of messages to keep in each Slave mailbox. This is useful for mailboxes where you keep a complete archive on the server, but want to mirror only the last messages (for instance, for mailing lists). The messages that were the first to arrive in the mailbox (independently of the actual date of the message) will be deleted first. Messages that are flagged (marked as important) and (by default) unread messages will not be automatically deleted. If <i>count</i> is 0, the maximum number of messages is <code>unlimited</code> (Default: <i>0</i>).</p>
<dt><code>ExpireUnread</code> <i>yes</i>|<i>no</i></p>
<dd> Selects whether unread messages should be affected by <code>MaxMessages</code>. Normally, unread messages are considered important and thus never expired. This ensures that you never miss new messages even after an extended absence. However, if your archive contains large amounts of unread messages by design, treating them as important would practically defeat <code>MaxMessages</code>. In this case you need to enable this option. (Default: <i>no</i>).</p>
<dt><code>Sync</code> {<i>None</i>|[<i>Pull</i>] [<i>Push</i>] [<i>New</i>] [<i>ReNew</i>] [<i>Delete</i>] [<i>Flags</i>]|<i>All</i>}</p>
<dd> Select the synchronization operation(s) to perform:<br />
 <i>Pull</i> &#8211; propagate changes from Master to Slave.<br />
 <i>Push</i> &#8211; propagate changes from Slave to Master.<br />
 <i>New</i> &#8211; propagate newly appeared messages.<br />
 <i>ReNew</i> &#8211; previously refused messages are re-evaluated for propagation. Useful after flagging affected messages in the source Store or enlarging MaxSize in the destination Store.<br />
 <i>Delete</i> &#8211; propagate message deletions. This applies only to messages that are actually gone, i.e., were expunged. The affected messages in the remote Store are marked as deleted only, i.e., they won&#8217;t be really deleted until that Store is expunged.<br />
 <i>Flags</i> &#8211; propagate flag changes. Note that Deleted/Trashed is a flag as well; this is particularly interesting if you use <code>mutt</code> with the maildir_trash option.<br />
 <i>All</i> (<code>&#8211;full</code> on the command line) &#8211; all of the above. This is the global default.<br />
 <i>None</i> (<code>&#8211;noop</code> on the command line) &#8211; don&#8217;t propagate anything. Useful if you want to expunge only.</p>
<dt>
<dd> <i>Pull</i> and <i>Push</i> are direction flags, while <i>New</i>, <i>ReNew</i>, <i>Delete</i> and <i>Flags</i> are type flags. The two flag classes make up a two-dimensional matrix (a table). Its cells are the individual actions to perform. There are two styles of asserting the cells:<br />
 In the first style, the flags select entire rows/colums in the matrix. Only the cells which are selected both horizontally and vertically are asserted. Specifying no flags from a class is like specifying all flags from this class. For example, &quot;<code>Sync</code>&nbsp;<wbr><i>Pull</i>&nbsp;<wbr><i>New</i>&nbsp;<wbr><i>Flags</i>&quot; will propagate new messages and flag changes from the Master to the Slave, &quot;<code>Sync</code>&nbsp;<wbr><i>New</i>&nbsp;<wbr><i>Delete</i>&quot; will propagate message arrivals and deletions both ways, and &quot;<code>Sync</code>&nbsp;<wbr><i>Push</i>&quot; will propagate all changes from the Slave to the Master.<br />
 In the second style, direction flags are concatenated with type flags; every compound flag immediately asserts a cell in the matrix. In addition to at least one compound flag, the individual flags can be used as well, but as opposed to the first style, they immediately assert all cells in their respective row/column. For example, &quot;<code>Sync</code>&nbsp;<wbr><i>PullNew</i>&nbsp;<wbr><i>PullDelete</i>&nbsp;<wbr><i>Push</i>&quot; will propagate message arrivals and deletions from the Master to the Slave and any changes from the Slave to the Master. Note that it is not allowed to assert a cell in two ways, e.g. &quot;<code>Sync</code>&nbsp;<wbr><i>PullNew</i>&nbsp;<wbr><i>Pull</i>&quot; and &quot;<code>Sync</code>&nbsp;<wbr><i>PullNew</i>&nbsp;<wbr><i>Delete</i>&nbsp;<wbr><i>Push</i>&quot; induce error messages.</p>
<dt><code>Create</code> {<i>None</i>|<i>Master</i>|<i>Slave</i>|<i>Both</i>}</p>
<dd> Automatically create missing mailboxes [on the Master/Slave]. Otherwise print an error message and skip that mailbox pair if a mailbox and the corresponding sync state does not exist. (Global default: <i>None</i>)</p>
<dt><code>Remove</code> {<i>None</i>|<i>Master</i>|<i>Slave</i>|<i>Both</i>}</p>
<dd> Propagate mailbox deletions [to the Master/Slave]. Otherwise print an error message and skip that mailbox pair if a mailbox does not exist but the corresponding sync state does.<br />
 For MailDir mailboxes it is sufficient to delete the cur/ subdirectory to mark them as deleted. This ensures compatibility with <code>SyncState *</code>.<br />
 Note that for safety, non-empty mailboxes are never deleted.<br />
 (Global default: <i>None</i>)</p>
<dt><code>Expunge</code> {<i>None</i>|<i>Master</i>|<i>Slave</i>|<i>Both</i>}</p>
<dd> Permanently remove all messages [on the Master/Slave] marked for deletion. See <code>RECOMMENDATIONS</code> below. (Global default: <i>None</i>)</p>
<dt><code>CopyArrivalDate</code> {<i>yes</i>|<i>no</i>}</p>
<dd> Selects whether their arrival time should be propagated together with the messages. Enabling this makes sense in order to keep the time stamp based message sorting intact. Note that IMAP does not guarantee that the time stamp (termed <code>internal date</code>) is actually the arrival time, but it is usually close enough. (Default: <i>no</i>)</dl>
<p> <code>Sync</code>, <code>Create</code>, <code>Remove</code>, <code>Expunge</code>, <code>MaxMessages</code>, and <code>CopyArrivalDate</code> can be used before any section for a global effect. The global settings are overridden by Channel-specific options, which in turn are overridden by command line switches.</p>
<dl>
<dt><code>SyncState</code> {<code>*</code>|<i>path</i>}</p>
<dd> Set the location of this Channel&#8217;s synchronization state files. <code>*</code> means that the state should be saved in a file named .mbsyncstate in the Slave mailbox itself; this has the advantage that you needn&#8217;t to care for the state file if you delete the mailbox, but it works only with Maildir mailboxes, obviously. Otherwise this is interpreted as a string to prepend to the Slave mailbox name to make up a complete path.<br />
 This option can be used outside any section for a global effect. In this case the appended string is made up according to the pattern <code>:</code><i>master</i><code>:</code><i>master-box</i><code>_:</code><i>slave</i><code>:</code><i>slave-box</i> (see also <code>FieldDelimiter</code> below).<br />
 (Global default: <i>~/.mbsync/</i>).</dl>
<h3>Groups</h3>
<dl>
<dt><code>Group</code> <i>name</i> [<i>channel</i>[<code>:</code><i>box</i>[<code>,</code>&#8230;]]] &#8230;</p>
<dd> Define the Group <i>name</i>, opening a section for its parameters. Note that even though Groups have an own namespace, they will &quot;hide&quot; Channels with the same name on the command line.<br />
 One or more Channels can be specified on the same line.<br />
 If you supply one or more <i>box</i>es to a <i>channel</i>, they will be used instead of what is specified in the Channel&#8217;s Patterns. The same can be done on the command line, except that there newlines can be used as mailbox name separators as well.</p>
<dt><code>Channel</code>[<code>s</code>] <i>channel</i>[<code>:</code><i>box</i>[<code>,</code>&#8230;]] &#8230;</p>
<dd> Add the specified channels to the group. This option can be specified multiple times within a Group.</dl>
<h3>Global Options</h3>
<dl>
<dt><code>FSync</code> <i>yes</i>|<i>no</i></p>
<dd>
 Selects whether <code>mbsync</code> performs forced flushing, which determines the level of data safety after system crashes and power outages. Disabling it is reasonably safe for file systems which are mounted with data=ordered mode. Enabling it is a wise choice for file systems mounted with data=writeback, in particular modern systems like ext4, btrfs and xfs. The performance impact on older file systems may be disproportionate. (Default: <i>yes</i>)</p>
<dt><code>FieldDelimiter</code> <i>delim</i></p>
<dd> The character to use to delimit fields in the string appended to a global <code>SyncState</code>. <code>mbsync</code> prefers to use the colon, but this is incompatible with DOS/Windows file systems. This option is meaningless for <code>SyncState</code> if the latter is <code>*</code>, obviously. However, it also determines the default of <code>InfoDelimiter</code>. (Global default: <i>;</i> on Windows, <i>:</i> everywhere else)</p>
<dt><code>BufferLimit</code> <i>size</i>[<code>k</code>|<code>m</code>][<code>b</code>]</p>
<dd> The per-Channel, per-direction instantaneous memory usage above which <code>mbsync</code> will refrain from using more memory. Note that this is no absolute limit, as even a single message can consume more memory than this. (Default: <i>10M</i>)</dl>
<h2>CONSOLE OUTPUT</h2>
<p> If <code>mbsync</code>&#8216;s output is connected to a console, it will print progress counters by default. The output will look like this: </p>
<p> C: 1/2 B: 3/4 M: +13/13 *23/42 #0/0 S: +0/7 *0/0 #0/0 </p>
<p> This represents the cumulative progress over channels, boxes, and messages affected on master and slave, respectively. The message counts represent added messages, messages with updated flags, and trashed messages, respectively. No attempt is made to calculate the totals in advance, so they grow over time as more information is gathered.</p>
<h2>RECOMMENDATIONS</h2>
<p> Make sure your IMAP server does not auto-expunge deleted messages &#8211; it is slow, and semantically somewhat questionable. Specifically, Gmail needs to be configured not to do it. </p>
<p> By default, <code>mbsync</code> will not delete any messages &#8211; deletions are propagated by marking the messages as deleted on the remote store. Once you have verified that your setup works, you will typically want to set <code>Expunge</code> to <code>Both</code>, so that deletions become effective. </p>
<p> <code>mbsync</code>&#8216;s built-in trash functionality relies on <code>mbsync</code> doing the expunging of deleted messages. This is the case when it propagates deletions of previously propagated messages, and the trash is on the target store (typically your IMAP server).<br />
 However, when you intend <code>mbsync</code> to trash messages which were not propagated yet, the MUA must mark the messages as deleted without expunging them (e.g., <code>Mutt</code>&#8216;s <code>maildir_trash</code> option). Note that most messages are propagated a long time before they are deleted, so this is a corner case you probably do not want to optimize for. This also implies that the <code>TrashNewOnly</code> and <code>TrashRemoteNew</code> options are typically not very useful. </p>
<p> If your server supports auto-trashing (as Gmail does), it is probably a good idea to rely on that instead of <code>mbsync</code>&#8216;s trash functionality. If you do that, and intend to synchronize the trash like other mailboxes, you should not use <code>mbsync</code>&#8216;s <code>Trash</code> option at all.</p>
<h2>INHERENT PROBLEMS</h2>
<p> Changes done after <code>mbsync</code> has retrieved the message list will not be synchronised until the next time <code>mbsync</code> is invoked. </p>
<p> Using <code>Trash</code> on IMAP Stores without the UIDPLUS extension (notably, M$ Exchange up to at least 2010) bears a race condition: messages will be lost if they are marked as deleted after the message list was retrieved but before the mailbox is expunged. There is no risk as long as the IMAP mailbox is accessed by only one client (including <code>mbsync</code>) at a time.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.mbsyncrc</code></p>
<dd> Default configuration file</p>
<dt><code>~/.mbsync/</code></p>
<dd> Directory containing synchronization state files</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mdconvert/">mdconvert</a>(1), <a href="/docs/linux/man/1-isync/">isync</a>(1), <a href="/docs/linux/man/1-mutt/">mutt</a>(1), <a href="/docs/linux/man/5-maildir/">maildir</a>(5) </p>
<p> Up to date information on <code>mbsync</code> can be found at <a rel="nofollow" href="http://isync.sf.net/">http://isync.sf.net/</a> </p>
<p> SASL mechanisms are listed at <a rel="nofollow" href="http://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml">http://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml</a></p>
<h2>AUTHORS</h2>
<p> Originally written by Michael R. Elkins, rewritten and currently maintained by Oswald Buddenhagen, contributions by Theodore Y. Ts&#8217;o. </p>
<h2>Index</h2>
