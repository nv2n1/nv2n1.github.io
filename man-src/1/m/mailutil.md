---
title: "mailutil(1)"
name: "mailutil"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mailutil/"
description: "mailutil – mail utility program"
---

<h2>NAME</h2>
<p> mailutil &#8211; mail utility program</p>
<h2>SYNTAX</h2>
<p> <code>mailutil command [switches] [arguments]</code> </p>
<p> All commands accept the -d, -v, and -u switches in addition to any command-specific switches. </p>
<p> <code>mailutil check [MAILBOX]</code> </p>
<p> <code>mailutil create MAILBOX</code> </p>
<p> <code>mailutil delete MAILBOX</code> </p>
<p> <code>mailutil rename SOURCE DESTINATION</code> </p>
<p> <code>mailutil copy [-rw] [-kw] [-ig] SOURCE DESTINATION</code> </p>
<p> <code>mailutil move [-rw] [-kw] [-ig] SOURCE DESTINATION</code> </p>
<p> <code>mailutil append [-rw] [-kw] [-ig] SOURCE DESTINATION</code> </p>
<p> <code>mailutil appenddelete [-rw] [-kw] [-ig] SOURCE DESTINATION</code> </p>
<p> <code>mailutil prune MAILBOX CRITERIA</code> </p>
<p> <code>mailutil transfer [-m mode] [-rw] [-kw] [-ig] SOURCE DESTINATION</code></p>
<h2>DESCRIPTION</h2>
<p> <code>mailutil</code> replaces the old chkmail, imapcopy, imapmove, imapxfer, mbxcopy, mbxcreat, and mbxcvt programs. </p>
<p> <code>mailutil check</code> determines whether new mail exists in the given mailbox (the default is INBOX). The number of new messages is defined as the number of messages that have &quot;Recent&quot; status set. If the mailbox contains no new messages, <code>mailutil check</code> will indicate that no new mail is present; otherwise, it will report the number of new messages. In either case, it will also indicate the canonical form of the name of the mailbox. </p>
<p> <code>mailutil create</code> creates a new <i>mailbox</i> with the given name. The mailbox name must not already exist. A mailbox can be created in a particular format by prefixing the name with <i>#driver.</i> followed by the format name and a <i>/</i> character. For example, the command </p>
<p>mailutil create&nbsp;<wbr>#driver.mbx/junkmail<br />
 will create a new mailbox named &quot;junkmail&quot; in mbx format. </p>
<p> <code>mailutil delete</code> deletes an existing <i>mailbox</i> with the given name. </p>
<p> <code>mailutil rename</code> renames an existing mailbox to a new name (which must not already exist). This only works if the old and new names are in the same mail store. A more general means to rename a mailbox is to do a <code>mailutil copy</code> of the old name to the new name, followed by a <code>mailutil delete</code> of the old name. </p>
<p> <code>mailutil copy</code> creates a new mailbox and copies messages from the old mailbox to the new mailbox. As in <code>mailutil create</code> a mailbox format can be specified with the new mailbox. For example, the command </p>
<p>mailutil copy INBOX&nbsp;<wbr>#driver.mbx/INBOX<br />
 will copy messages from your existing INBOX to an mbx-format INBOX. </p>
<p> <code>mailutil move</code> is similar to <code>mailutil copy</code> but in addition will also remove (delete and expunge) the messages from the old mailbox after copying them to the new mailbox. </p>
<p> <code>mailutil append</code> and <code>mailutil appenddelete</code> are similar to <code>mailutil copy</code> and <code>mailutil move</code> respectively except that they do not create the destination mailbox. </p>
<p> <code>mailutil prune</code> prunes the mailbox of messages which match certain criteria, which are in the form of IMAP2 (RFC 1176) SEARCH arguments. For example, the command. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>mailutil prune INBOX&nbsp;<wbr>&quot;before 1-jan-2004&quot;<br />
 will delete and expunge all messages written before January 1, 2004. </p>
<p> Note that mailutil implements pruning by deleting the matching messages, and then expunging the mailbox. Consequently, mailutil will also expunge any messages which were deleted at the time of the pruning. </p>
<p> <code>mailutil transfer</code> copies an entire hierarchy of mailboxes from the named source to the named destination. Mailboxes are created on the destination as needed. Any error in copying messages will cause the transfer to stop. </p>
<p> Normally, any error in creation will cause the transfer to stop. However, if <code>-m MODE</code> or <code>-merge MODE</code> is specified, a merging transfer is performed. The <code>MODE</code> argument indicats the type of merge: </p>
<p> <code>-m[erge] prompt</code> indicates that the user should be asked for an alternative name to create. If creating the new name fails, the user will be asked again. </p>
<p> <code>-m[erge] append</code> indicates that it&#8217;s alright to copy the messages into an existing mailbox with that name. If the mailbox does not exist, the user will be prompted for an alternative name. </p>
<p> <code>-m[erge] suffix=XXXX</code> where XXXX is any string, indicates that an alternative name should be built by appending the given suffix to the name. It that alternative name can&#8217;t be created, then the user will be prompted for an alternative name. </p>
<p> The source hierarchy consists of all mailboxes which start with the given source name. With the exception of a remote system specification (within &quot;{}&quot; braces), the source name is used as the name of the destination. The destination hierarchy is a prefix applied to any new names being created. For example, </p>
<p>mailutil transfer foo bar<br />
 will copy all mailboxes with names beginning with &quot;foo&quot; to names beginning with &quot;bar&quot; (hence &quot;foobar&quot; will be copied to &quot;barfoobar&quot;). Similarly, </p>
<p>mailutil transfer&nbsp;<wbr>&quot;{imap.foo.com}&quot;&nbsp;<wbr>&quot;{imap.bar.com}old/&quot;<br />
 will copy all mailboxes from the imap.foo.com IMAP server to equivalent names starting with &quot;old/&quot; on the imap.bar.com IMAP server.</p>
<h2>FLAGS</h2>
<p> The <code>-d</code> or <code>-debug</code> flag prints full debugging telemetry including protocol operations. </p>
<p> The <code>-v</code> or <code>-verbose</code> flag prints verbose (non-error) telemetry. </p>
<p> The <code>-u USERID</code> or <code>-user USERID</code> switch attempts to become the indicated user. This is for the benefit of system administrators who want to do mailutil operations on a userid that does not normally have shell access. </p>
<p> The <code>-rw</code> or <code>-rwcopy</code> flag causes the source mailbox to be open in readwrite mode rather than readonly mode. Normally, mailutil tries to use readonly mode to avoid altering any flags in the source mailbox, but some mailbox types, e.g. POP3, can&#8217;t be open in readonly mode. </p>
<p> The <code>-kw</code> or <code>-kwcopy</code> flag causes the keywords of the source mailbox to be created in the destination mailbox. Normally, mailutil does not create keywords in the destination mailbox so only those keywords that are already defined in the destination mailbox will be preserved. Note that some IMAP servers may automatically create keywords, so this flag may not be necessary. </p>
<p> The <code>-ig</code> or <code>-ignore</code> flag causes the keywords of the source mailbox to be ignored completely and no attempt is made to copy them to the destination mailbox. </p>
<p> The <code>-ig[nore]</code> and <code>-kw[copy]</code> flags are mutually exclusive.</p>
<h2>ARGUMENTS</h2>
<p> The arguments are standard c-client mailbox names. A variety of mailbox name formats and types of mailboxes are supported by c-client; examples of the most common forms of names are: </p>
<p> <i></p>
<dl>
<dt>Name</p>
<dd> </i> <i>Meaning</i></p>
<dt>INBOX</p>
<dd> primary incoming mail folder on the local system</p>
<dt>archive/tx-project</p>
<dd> mail folder named &quot;tx-project&quot; in &quot;archive&quot; subdirectory of local filesystem home directory</p>
<dt>{imapserver.foo.com}INBOX</p>
<dd> primary incoming mail folder on IMAP server system &quot;imapserver.foo.com&quot;</p>
<dt>{imapserver.foo.com}archive/tx-project</p>
<dd> mail folder named &quot;tx-project&quot; in &quot;archive&quot; subdirectory on IMAP server system &quot;imapserver.foo.com&quot;</p>
<dt>#news.comp.mail.misc</p>
<dd> newsgroup &quot;comp.mail.misc&quot; on local filesystem</p>
<dt>{newserver.foo.com/nntp}comp.mail.misc</p>
<dd> newsgroup &quot;comp.mail.misc&quot; on NNTP server system &quot;newserver.foo.com&quot;</p>
<dt>{popserver.foo.com/pop3}</p>
<dd> mail folder on POP3 server system &quot;popserver.foo.com&quot;</dl>
<p> See your system manager for more information about the types of mailboxes which are available on your system.</p>
<h2>RESTRICTIONS</h2>
<p> You must surround a <i>{host}mailbox</i> argument with quotation marks if you run <code>mailutil</code> from <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) or another shell for which braces have special meaning. </p>
<p> You must surround a <i>#driver.format/mailbox</i> argument with quotation marks if you run <code>mailutil</code> from a shell in which &quot;#&quot; is the comment character.</p>
<h2>AUTHOR</h2>
<p> Mark Crispin, MRC [at] Washington.EDU </p>
<h2>Index</h2>
