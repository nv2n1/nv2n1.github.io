---
title: "maildir(5)"
name: "maildir"
section: "5"
letter: "m"
url: "/docs/linux/man/5-maildir/"
description: "maildir – E-mail directory"
---

<p>maildir &#8211; E-mail directory</p>
<h2>Synopsis</h2>
<p>$HOME/Maildir</p>
<h2>Description</h2>
<p>A &#8220;Maildir&#8221; is a structured directory that holds E-mail messages. Maildirs were first implemented by the Qmail mail server. Qmail&#8217;s maildirs were a simple data structure, nothing more than a single collection of E-mail messages. The Courier mail server builds upon Qmail&#8217;s maildirs to provide extended functionality, such as folders and quotas. This document describes the Courier mail server&#8217;s extended maildirs, without explicitly identifying The Courier mail server-specific extensions. See <code><a href="/docs/linux/man/5-maildir/">maildir</a></code>(5) in Qmail&#8217;s documentation for the original definition of maildirs. </p>
<p> Traditionally, E-mail folders were saved as plain text files, called &#8220;mboxes&#8221;. Mboxes have known limitations. Only one application can use an mbox at the same time. Locking is required in order to allow simultaneous concurrent access by different applications. Locking is often problematic, and not very reliable in network-based filesystem requirements. Some network-based filesystems don&#8217;t offer any reliable locking mechanism at all. Furthermore, even bulletproof locking won&#8217;t prevent occasional mbox corruption. A process can be killed or terminated in the middle of updating an mbox. This will likely result in corruption, and a loss of most messages in the mbox. </p>
<p> Maildirs allow multiple concurrent access by different applications. Maildirs do not require locking. Multiple applications can update a maildir at the same time, without stepping on each other&#8217;s feet.</p>
<h3>Maildir contents</h3>
<p>A &#8220;maildir&#8221; is a directory that&#8217;s created by m[blue]<code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)m[]<font SIZE="-2">[1]</font>. Naturally, maildirs should not have any group or world permissions, unless you want other people to read your mail. A maildir contains three subdirectories: tmp, new, and cur. These three subdirectories comprise the primary folder, where new mail is delivered by the system. </p>
<p> Folders are additional subdirectories in the maildir whose names begin with a period: such as .Drafts or .Sent. Each folder itself contains the same three subdirectories, tmp, new, and cur, and an additional zero-length file named maildirfolder, whose purpose is to inform any mail delivery agent that it&#8217;s really delivering to a folder, and that the mail delivery agent should look in the parent directory for any maildir-related information. </p>
<p> Folders are not physically nested. A folder subdirectory, such as .Sent does not itself contain any subfolders. The main maildir contains a single, flat list of subfolders. These folders are logically nested, and periods serve to separate folder hierarchies. For example, .Sent.2002 is considered to be a subfolder called &#8220;2002&#8221; which is a subfolder of &#8220;Sent&#8221;. </p>
<p> <font SIZE="+1"> <code>Folder name encoding</code></p>
<dl>
<dd>Folder names can contain any Unicode character, except for control characters. US-ASCII characters, U+0x0020 &#8211; U+0x007F, except for the period, forward-slash, and ampersand characters (U+0x002E, U+0x002F, and U+0x0026) represent themselves. The ampersand is represent by the two character sequence &#8220;&amp;-&#8220;. The period, forward slash, and non US-ASCII Unicode characters are represented using the UTF-7 character set, and encoded with a modified form of base64-encoding. </p>
<p> The &#8220;&amp;&#8221; character starts the modified base64-encoded sequence; the sequence is terminated by the &#8220;-&#8221; character. The sequence of 16-bit Unicode characters is written in big-endian order, and encoded using the base64-encoding method described in section 5.2 of m[blue]<code>RFC 1521</code>m[]</font><font SIZE="-1">[2]</font><font SIZE="+1">, with the following modifications: </p>
<dl>
<dd>&bull; The &#8220;=&#8221; padding character is omitted. When decoding, an incomplete 16-bit character is discarded.</dl>
<dl>
<dd>&bull; The comma character, &#8220;,&#8221; is used in place of the &#8220;/&#8221; character in the base64 alphabet.</dl>
<p> For example, the word &#8220;Resume&#8221; with both &quot;e&quot;s being the e-acute character, U+0x00e9, is encoded as &#8220;R&amp;AOk-sum&amp;AOk-&#8221; (so a folder of that name would be a maildir subdirectory called &#8220;.R&amp;AOk-sum&amp;AOk-&#8220;).</dl>
<p> </font><font SIZE="+2"> <code>Other maildir contents</code></p>
<dl>
<dd>Software that uses maildirs may also create additional files besides the tmp, new, and cur subdirectories &#8212; in the main maildir or a subfolder &#8212; for its own purposes.</dl>
<p> </font></p>
<h3>Messages</h3>
<p>E-mail messages are stored in separate, individual files, one E-mail message per file. The tmp subdirectory temporarily stores E-mail messages that are in the process of being delivered to this maildir. tmp may also store other kinds of temporary files, as long as they are created in the same way that message files are created in tmp. The new subdirectory stores messages that have been delivered to this maildir, but have not yet been seen by any mail application. The cur subdirectory stores messages that have already been seen by mail applications.</p>
<h3>Adding new mail to maildirs</h3>
<p>The following process delivers a new message to the maildir: </p>
<p> A new unique filename is created using one of two possible forms: &#8220;time.MusecPpid.host&#8221;, or &#8220;time.MusecPpid_unique.host&#8221;. &#8220;time&#8221; and &#8220;usec&#8221; is the current system time, obtained from <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2). &#8220;pid&#8221; is the process number of the process that is delivering this message to the maildir. &#8220;host&#8221; is the name of the machine where the mail is being delivered. In the event that the same process creates multiple messages, a suffix unique to each message is appended to the process id; preferrably an underscore, followed by an increasing counter. This applies whether messages created by a process are all added to the same, or different, maildirs. This protocol allows multiple processes running on multiple machines on the same network to simultaneously create new messages without stomping on each other. </p>
<p> The filename created in the previous step is checked for existence by executing the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call. If <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) results in ANYTHING OTHER than the system error ENOENT, the process must sleep for two seconds, then go back and create another unique filename. This is an extra step to insure that each new message has a completely unique filename. </p>
<p> Other applications that wish to use tmp for temporary storage should observe the same protocol (but see READING MAIL FROM MAILDIRS below, because old files in tmp will be eventually deleted). </p>
<p> If the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call returned ENOENT, the process may proceed to create the file in the tmp subdirectory, and save the entire message in the new file. The message saved MUST NOT have the &#8220;From_&#8221; header that is used to mboxes. The message also MUST NOT have any &#8220;From_&#8221; lines in the contents of the message prefixed by the &#8220;&gt;&#8221; character. </p>
<p> When saving the message, the number of bytes returned by the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) system call must be checked, in order to make sure that the complete message has been written out. </p>
<p> After the message is saved, the file descriptor is <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2)-ed. The file&#8217;s device number, inode number, and the its byte size, are saved. The file is closed and is then immediately moved/renamed into the new subdirectory. The name of the file in new should be &#8220;time.MusecPpidVdevIino.host,S=<i>cnt</i>&#8220;, or &#8220;time.MusecPpidVdevIino_unique.host,S=<i>cnt</i>&#8220;. &#8220;dev&#8221; is the message&#8217;s device number, &#8220;ino&#8221; is the message&#8217;s inode number (from the previous <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2) call); and &#8220;cnt&#8221; is the message&#8217;s size, in bytes. </p>
<p> The &#8220;,S=<i>cnt</i>&#8221; part optimizes the m[blue]<code>Courier</code>m[]<font SIZE="-2">[3]</font> mail server&#8217;s maildir quota enhancement; it allows the size of all the mail stored in the maildir to be added up without issuing the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call for each individual message (this can be quite a performance drain with certain network filesystems).</p>
<h3>Reading Mail From Maildirs</h3>
<p>Applications that read mail from maildirs should do it in the following order: </p>
<p> When opening a maildir or a maildir folder, read the tmp subdirectory and delete any files in there that are at least 36 hours old. </p>
<p> Look for new messages in the new subdirectory. Rename <i>new/filename</i>, as <i>cur/filename:2,info</i>. Here, <i>info</i> represents the state of the message, and it consists of zero or more boolean flags chosen from the following: &#8220;D&#8221; &#8211; this is a &#8216;draft&#8217; message, &#8220;R&#8221; &#8211; this message has been replied to, &#8220;S&#8221; &#8211; this message has been viewed (seen), &#8220;T&#8221; &#8211; this message has been marked to be deleted (trashed), but is not yet removed (messages are removed from maildirs simply by deleting their file), &#8220;F&#8221; &#8211; this message has been marked by the user, for some purpose. These flags must be stored in alphabetical order. New messages contain only the :2, suffix, with no flags, indicating that the messages were not seen, replied, marked, or deleted. </p>
<p> Maildirs may have maximum size quotas defined, but these quotas are purely voluntary. If you need to implement mandatory quotas, you should use any quota facilities provided by the underlying filesystem that is used to store the maildirs. The maildir quota enhancement is designed to be used in certain situations where filesystem-based quotas cannot be used for some reason. The implementation is designed to avoid the use of any locking. As such, at certain times the calculated quota may be imprecise, and certain anomalous situations may result in the maildir actually going over the stated quota. One such situation would be when applications create messages without updating the quota estimate for the maildir. Eventually it will be precisely recalculated, but wherever possible new messages should be created in compliance with the voluntary quota protocol. </p>
<p> The voluntary quota protocol involves some additional procedures that must be followed when creating or deleting messages within a given maildir or its subfolders. The m[blue]<code><a href="/docs/linux/man/8-deliverquota/">deliverquota</a></code>(8)m[]<font SIZE="-2">[4]</font> command is a tiny application that delivers a single message to a maildir using the voluntary quota protocol, and hopefully it can be used as a measure of last resort. Alternatively, applications can use the libmaildir.a library to handle all the low-level dirty details for them. The voluntary quota enhancement is described in the m[blue]<code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)m[]<font SIZE="-2">[5]</font> man page.</p>
<h3>Maildir Quotas</h3>
<p>This is a voluntary mechanism for enforcing &quot;loose&quot; quotas on the maximum sizes of maildirs. This mechanism is enforced in software, and not by the operating system. Therefore it is only effective as long as the maildirs themselves are not directly accessible by their users, since this mechanism is trivially disabled. </p>
<p> If possible, operating system-enforced quotas are preferrable. Where operating system quota enforcement is not available, or not possible, this voluntary quota enforcement mechanism might be an acceptable compromise. Since it&#8217;s enforced in software, all software that modifies or accesses the maildirs is required to voluntary obey and enforce a quota. The voluntary quota implementation is flexible enough to allow non quota-aware applications to also access the maildirs, without any drastic consequences. There will be some non-drastic consequences, though. Of course, non quota-aware applications will not enforce any defined quotas. Furthermore, this voluntary maildir quota mechanism works by estimating the current size of the maildir, with periodic exact recalculation. Obviously non quota-aware maildir applications will not update the maildir size estimation, so the estimate will be thrown off for some period of time, until the next recalculation. </p>
<p> This voluntary quota mechanism is designed to be a reasonable compromise between effectiveness, and performance. The entire purpose of using maildir-based mail storage is to avoid any kind of locking, and to permit parallel access to mail by multiple applications. In order to compute the exact size of a maildir, the maildir must be locked somehow to prevent any modifications while its contents are added up. Obviously something like that defeats the original purpose of using maildirs, therefore the voluntary quota mechanism does not use locking, and that&#8217;s why the current recorded maildir size is always considered to be an estimate. Regular size recalculations will compensate for any occasional race conditions that result in the estimate to be thrown off. </p>
<p> A quota for an existing maildir is installed by running maildirmake with the -q option, and naming an existing maildir. The -q option takes a parameter, <i>quota</i>, which is a comma-separated list of quota specifications. A quota specification consists of a number followed by either &#8216;S&#8217;, indicating the maximum message size in bytes, or &#8216;C&#8217;, maximum number of messages. For example: </p>
<dl>
<dd>
<pre><code>maildirmake -q 5000000S,1000C ./Maildir</code></pre>
</dl>
<p> This sets the quota to 5,000,000 bytes or 1000 messages, whichever comes first. </p>
<dl>
<dd>
<pre><code>maildirmake -q 1000000S ./Maildir</code></pre>
</dl>
<p> This sets the quota to 1,000,000 bytes, without limiting the number of messages. </p>
<p> A quota of an existing maildir can be changed by rerunning the <code>maildirmake</code> command with a new -q option. To delete a quota entirely, delete the <i>Maildir</i>/maildirsize file.</p>
<h2>See Also</h2>
<p>m[blue]<code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)m[]<font SIZE="-2">[1]</font>.</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><code><a href="/docs/linux/man/1-maildirmake/">maildirmake</a></code>(1)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/maildirmake.html</dl>
<dt> 2.</p>
<dd>RFC 1521</p>
<dl>
<dd><a rel="nofollow" href="http://www.rfc-editor.org/rfc/rfc1521.txt">http://www.rfc-editor.org/rfc/rfc1521.txt</a></dl>
<dt> 3.</p>
<dd>Courier</p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org">http://www.courier-mta.org</a></dl>
<dt> 4.</p>
<dd><code><a href="/docs/linux/man/8-deliverquota/">deliverquota</a></code>(8)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/deliverquota.html</dl>
<dt> 5.</p>
<dd><code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)</p>
<dl>
<dd>[set $man.base.url.for.relative.links]/maildirquota.html</dl>
