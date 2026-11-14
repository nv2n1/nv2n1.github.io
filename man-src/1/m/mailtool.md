---
title: "mailtool(1)"
name: "mailtool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mailtool/"
description: "mailtool – Process mailboxes"
---

<h2 class="name">NAME</h2>
<p> mailtool &#8211; Process mailboxes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mailtool</code> [options&#8230;]</dl>
<h2>USAGE</h2>
<p> <code>mailtool</code></p>
<dd>is a diagnostic utility for handling various operations on mailboxes. <code>mailtool</code>&#8216;s main uses include: display the list of folders in a mailbox; displaying list of messages in a mailbox; and copying mailboxes. </p>
<p> The following mailboxes can be accessed by <code>mailtool</code>: </p>
<p> imap://<i>userid</i>@<i>server</i>[/options]</p>
<dl>
<dt>
<dd> An IMAP account. <code>mailtool</code> will prompt for the login password.</dl>
<p> imaps://<i>userid</i>@<i>server</i>[/options]</p>
<dl>
<dt>
<dd> An IMAP account accessed via an encrypted SSL connection.</dl>
<p> pop3://<i>userid</i>@<i>server</i>[/options]</p>
<dl>
<dt>
<dd> A POP3 account. <code>mailtool</code> will prompt for the login password.</dl>
<p> pop3s://<i>userid</i>@<i>server</i>[/options]</p>
<dl>
<dt>
<dd> A POP3 account accessed via an encrypted SSL connection.</dl>
<p> maildir:<i>path</i></p>
<dl>
<dt>
<dd> A local maildir mailbox. path specifies the maildir&#8217;s location relative to the home directory (NOT the current directory).</dl>
<p> mbox:<i>path</i></p>
<dl>
<dt>
<dd> Local mbox mail folders. path specifies the path to an mbox folder file, or a directory containing mbox folders, relative to the home directory (NOT the current directory).</dl>
<p> inbox:<i>path</i></p>
<dl>
<dt>
<dd> Local mbox mail folders, like &#8220;mbox:<i>path</i>&#8220;; additionally, the system spool mailbox is automatically copied to $HOME/Inbox, which is accessible as folder INBOX.</dl>
<p> The name of a remote IMAP or POP3 server may be followed by one or more options that control various settings of the IMAP or POP3 connection: </p>
<p> /cram</p>
<dl>
<dt>
<dd> Do not open the account unless the server supports secure password authentication. Secure password authentication verifies the account&#8217;s password using a challenge/response authentication mechanism (where the label &quot;cram&quot; comes from). The actual password is never actually transmitted to the server, and therefore cannot be intercepted while in transit over an untrusted network. </p>
<p> Secure password authentication is not supported by all servers. This option may not work with some servers. This option does not enable secure password authentication, it only mandates its use. If the server supports secure password authentication, it will be used even without the /cram option. Traditional userid/password authentication will be used only if the server does not implement secure password authentication. The /cram option makes secure password authentication mandatory. </p>
<p> The /cram option is marginally useful even with encrypted server connections. The secure password authentication never sends the explicit password to the server. Encryption makes it theoretically impossible to recover the password from an encrypted data connection; but with secure authentication the password is never sent over the connection in the first place (the password&#8217;s validity is certified by exchanging certain mathematical calculations between the server and the client). If the server is compromised, the compromised server will not receive the account password (unless the password is recovered from the server in other ways).</dl>
<p> /imap</p>
<dl>
<dt>
<dd> Do not use the SMAP if the server claims the availability of this experimental mail access protocol, and fall back to IMAP compatibility mode (this option is meaningful only with &#8220;imap://&#8221; and &#8220;imaps://&#8221; URLs).</dl>
<p> /notls</p>
<dl>
<dt>
<dd> Do not upgrade a plain connection to an encrypted one. This option is primarily used for testing and debugging purposes. Sometimes this option might be useful with servers that claim to offer encryption, but are unable to do so when taken up on their offer.</dl>
<p> /novalidate-cert</p>
<dl>
<dt>
<dd> Do not validate the server&#8217;s SSL certificate when using an encrypted connection. Normally the mail server&#8217;s SSL certificate must be validate when using an encrypted connection. The certificate&#8217;s name must match the server&#8217;s name, and the certificate must be signed by a trusted certificate authority. </p>
<p> The encrypted connection normally fails if the certificate cannot be validate. Validation requires that a list of trusted certificate authorities must be known and configured. It&#8217;s simply impossible to know which certificate authorities are valid without an explicit list of valid, known, trusted, certificate authorities. If a trusted authority list is not configured, no certificate can be validated. If the server&#8217;s certificate is a self-signed certificate (this is often used for testing purposes), or if it&#8217;s not signed by a known authority, the encrypted connection fails. </p>
<p> This /novalidate-cert option disables certificate validation. The encrypted connection will be established even if the server&#8217;s certificate would otherwise be rejected. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This option is applicable even when an encrypted IMAP or POP3 connection is not explicitly requested. Many mail servers are capable of automatically upgrading unencrypted connections to a fully-encrypted connection. If a mail server claims to be able to use encryption, then there&#8217;s no reason not to use it. The result is that all encryption certification requirements still apply even when encryption is not explicitly requested. </p>
</dl>
</dl>
<h3>Displaying mailbox contents</h3>
<dl>
<dt> <code>mailtool</code> -tree | -list <i>account</i></dl>
<p> -tree</p>
<dd>shows a hierarchical representation of mail folders in <i>account</i>. -list generates a simple folder listing, one folder name per line. -tree shows folder names, while -list shows the actual mail folder path in <i>account</i>. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -tree <a href="imap://jsmith@mail.example.com/novalidate-cert/cram">imap://jsmith@mail.example.com/novalidate-cert/cram</a>
</pre>
</dl>
<h3>Creating folders</h3>
<dl>
<dt> <code>mailtool</code> -create | -createdir <i>folder</i> <i>name</i> <i>account</i></dl>
<p> -create</p>
<dd>creates a new subfolder of <i>folder</i> in <i>account</i>. The new subfolder&#8217;s name is <i>name</i>. -createdir creates a new folder directory (a folder that contains other folders). </p>
<dl>
<dt>
<dd>
<pre>
mailtool -create INBOX.lists announcements maildir:Maildir
</pre>
</dl>
<p> This command creates a new folder &#8220;announcements&#8221; as a subfolders of &#8220;INBOX.lists&#8221; in the local maildir.</p>
<h3>Deleting folders</h3>
<dl>
<dt> <code>mailtool</code> -delete | -deletedir <i>folder</i> <i>account</i></dl>
<p> -delete</p>
<dd>deletes an existing <i>folder</i> in <i>account</i>. </p>
<p> -deletedir deletes a folder directory. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -delete INBOX.lists.announcements maildir:Maildir
</pre>
</dl>
<h3>Renaming folders</h3>
<dl>
<dt> <code>mailtool</code> -rename <i>oldfolder</i> <i>folder</i> <i>name</i> <i>account</i></dl>
<p> -renames</p>
<dd>renames an existing <i>oldfolder</i>. The folder is renamed as <i>name</i>, as a subfolder of <i>folder</i>. <i>folder</i> may be an empty string if the folder should be moved to the top level of <i>account</i>&#8216;s folder hierarchy. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -rename INBOX.lists.announcements INBOX.lists Announcements maildir:Maildir
</pre>
</dl>
<p> The folder &#8220;INBOX.lists.announcements&#8221; is renamed to &#8220;INBOX.lists.Announcements&#8221;. This slightly unusual way to rename folder allows folders to be relocated in the mail <i>account</i>&#8216;s folder hierarchy.</p>
<h3>Reading folder&#8217;s index</h3>
<dl>
<dt> <code>mailtool</code> -index <i>folder</i> <i>account</i></dl>
<p> -index</p>
<dd>downloads and prints a summary of all messages in <i>folder</i>, in <i>account</i>. The summary shows the sender&#8217;s and recipients&#8217; address, the message&#8217;s subject, and size. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -index INBOX <a href="imap://john@mail.example.com/novalidate-cert">imap://john@mail.example.com/novalidate-cert</a>
</pre>
</dl>
<h3>Removing a message from a folder</h3>
<dl>
<dt> <code>mailtool</code> -remove <i>folder</i> <i>n</i> <i>account</i></dl>
<p> -remove</p>
<dd>removes message #<i>n</i> (ranging from 1 to the number of messages in the folder) in <i>folder</i>, in <i>account</i>. The message numbers may be obtained by using -index. </p>
<p> <i>n</i> may be a comma-separated list of message numbers, in strictly numerically increasing order. -remove confirms the list of messages to remove and issues a &#8220;Ready:&#8221; prompt. Press ENTER to remove the messages. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -remove INBOX 28,31 <a href="imap://john@mail.example.com/novalidate-cert">imap://john@mail.example.com/novalidate-cert</a>
</pre>
</dl>
<h3>Filtering messages</h3>
<dl>
<dt> <code>mailtool</code> -filter <i>folder</i> <i>account</i></dl>
<p> -filter</p>
<dd>is a combination of -index and -remove. <i>folder</i>&#8216;s index is downloaded, and the summary of each message is shown, one message at a time. Each message&#8217;s summary is followed by a prompt: &#8220;Delete, Skip, or Exit&#8221;. Pressing D removes the message, S leaves the message unchanged, and E leaves the remaining messages unchanged. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -filter INBOX pop3://john [at] mail.example.com/novalidate-cert
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> -filter is not meant to be used with large folders. Unless messages are removed quickly, the connection to the server may be disconnected for inactivity. </p>
</dl>
<h3>Copying folders</h3>
<dl>
<dt> <code>mailtool</code> [-recurse] -tofolder <i>tofolder</i> -copyto <i>toaccount</i> -fromfolder <i>fromfolder</i> <i>fromaccount</i></dl>
<dd>This command copies an entire folder, fromfolder in fromaccount to a new folder, tofolder (which will be created, if necessary) in toaccount. Optionally, -recurse specifies that all subfolders of fromfolder should also be copied. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -tofolder INBOX -copyto maildir:Maildir \
    -fromfolder &quot;INBOX&quot; <a href="imap://mbox100@mail.example.com/novalidate-cert">imap://mbox100@mail.example.com/novalidate-cert</a>
mailtool -recurse -tofolder INBOX.converted_mail \
    -copyto maildir:Maildir -fromfolder &quot;mail&quot; \
        <a href="imap://mbox100@mail.example.com/novalidate-cert">imap://mbox100@mail.example.com/novalidate-cert</a>
</pre>
</dl>
<p> This example first copies the INBOX on the IMAP server to $HOME/Maildir, then copies subfolders of &#8220;mail&#8221; on the IMAP server to the &#8220;converted_mail&#8221; subfolder in the maildir. </p>
<dl>
<dt>
<dd>
<pre>
mailtool -tofolder INBOX -copyto maildir:Maildir \
   -fromfolder &quot;INBOX&quot; inbox:mail
mailtool -recurse -tofolder INBOX.converted_mail \
    -copyto maildir:Maildir -fromfolder &quot;&quot; mbox:mail
</pre>
</dl>
<p> This example first copies $HOME/Inbox (accessed as the INBOX folder in inbox:mail) to $HOME/Maildir, then copies mbox folders from $HOME/mail to the &#8220;converted_mail&#8221; subfolder in the maildir. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Mail accounts that contain hybrid folders (folders that contain both messages and subfolders) can only be copied to account types that also support hybrid folders: either local maildirs, or to remote servers that support hybrid folders. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cone/">cone</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd></dl>
<h2>Index</h2>
