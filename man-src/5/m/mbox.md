---
title: "mbox(5)"
name: "mbox"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mbox/"
description: "mbox – Format for mail message storage."
---

<p>mbox &#8211; Format for mail message storage.</p>
<h2>Description</h2>
<p>This document describes the format traditionally used by Unix hosts to store mail messages locally. <code>mbox</code> files typically reside in the system&#8217;s mail spool, under various names in users&#8217; Mail directories, and under the name <code>mbox</code> in users&#8217; home directories. </p>
<p> An <code>mbox</code> is a text file containing an arbitrary number of e-mail messages. Each message consists of a postmark, followed by an e-mail message formatted according to <code>RFC822</code>, <code>RFC2822</code>. The file format is line-oriented. Lines are separated by line feed characters (ASCII 10). </p>
<p> A postmark line consists of the four characters &quot;From&quot;, followed by a space character, followed by the message&#8217;s envelope sender address, followed by whitespace, and followed by a time stamp. This line is often called From_ line. </p>
<p> The sender address is expected to be <code>addr-spec</code> as defined in <code>RFC2822</code> 3.4.1. The date is expected to be <code>date-time</code> as output by <code><a href="/docs/linux/man/3-asctime/">asctime</a>(3)</code>. For compatibility reasons with legacy software, two-digit years greater than or equal to 70 should be interpreted as the years 1970+, while two-digit years less than 70 should be interpreted as the years 2000-2069. Software reading files in this format should also be prepared to accept non-numeric timezone information such as &quot;CET DST&quot; for Central European Time, daylight saving time. </p>
<p> Example:</p>
<dl>
<dd>&gt;From example [at] example.com Fri Jun 23 02:56:55 2000</dl>
<p> In order to avoid misinterpretation of lines in message bodies which begin with the four characters &quot;From&quot;, followed by a space character, the mail delivery agent must quote any occurrence of &quot;From &quot; at the start of a body line. </p>
<p> There are two different quoting schemes, the first (<code>MBOXO</code>) only quotes plain &quot;From &quot; lines in the body by prepending a &#8216;&gt;&#8217; to the line; the second (<code>MBOXRD</code>) also quotes already quoted &quot;From &quot; lines by prepending a &#8216;&gt;&#8217; (i.e. &quot;&gt;From &quot;, &quot;&gt;&gt;From &quot;, &#8230;). The later has the advantage that lines like</p>
<dl>
<dd>&gt;From the command line you can use the &#8216;-p&#8217; option</dl>
<p> aren&#8217;t dequoted wrongly as a <code>MBOXRD</code>-MDA would turn the line into</p>
<dl>
<dd>&gt;&gt;From the command line you can use the &#8216;-p&#8217; option</dl>
<p> before storing it. Besides <code>MBOXO</code> and <code>MBOXRD</code> there is also <code>MBOXCL</code> which is <code>MBOXO</code> with a &quot;Content-Length:&quot;-field with the number of bytes in the message body; some MUAs (like <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1)) do automatically transform <code>MBOXO</code> mailboxes into <code>MBOXCL</code> ones when ever they write them back as <code>MBOXCL</code> can be read by any <code>MBOXO</code>-MUA without any problems. </p>
<p> If the modification-time (usually determined via <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)) of a nonempty <code>mbox</code> file is greater than the access-time the file has new mail. Many MUAs place a Status: header in each message to indicate which messages have already been read.</p>
<h2>Locking</h2>
<p>Since <code>mbox</code> files are frequently accessed by multiple programs in parallel, <code>mbox</code> files should generally not be accessed without locking. </p>
<p> Three different locking mechanisms (and combinations thereof) are in general use:</p>
<dl>
<dt>&bull;</p>
<dd><code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locking is mostly used on recent, POSIX-compliant systems. Use of this locking method is, in particular, advisable if <code>mbox</code> files are accessed through the Network File System (NFS), since it seems the only way to reliably invalidate NFS clients&#8217; caches.</p>
<dt>&bull;</p>
<dd><code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) locking is mostly used on BSD-based systems.</p>
<dt>&bull;</p>
<dd>Dotlocking is used on all kinds of systems. In order to lock an <code>mbox</code> file named <i>folder</i>, an application first creates a temporary file with a unique name in the directory in which the <i>folder</i> resides. The application then tries to use the <code><a href="/docs/linux/man/2-link/">link</a></code>(2) system call to create a hard link named <i>folder.lock</i> to the temporary file. The success of the <code><a href="/docs/linux/man/2-link/">link</a></code>(2) system call should be additionally verified using <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) calls. If the link has succeeded, the mail folder is considered dotlocked. The temporary file can then safely be unlinked.</p>
<dd>In order to release the lock, an application just unlinks the <i>folder.lock</i> file.</dl>
<p> If multiple methods are combined, implementors should make sure to use the non-blocking variants of the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) and <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) system calls in order to avoid deadlocks. </p>
<p> If multiple methods are combined, an <code>mbox</code> file must not be considered to have been successfully locked before all individual locks were obtained. When one of the individual locking methods fails, an application should release all locks it acquired successfully, and restart the entire locking procedure from the beginning, after a suitable delay. </p>
<p> The locking mechanism used on a particular system is a matter of local policy, and should be consistently used by all applications installed on the system which access <code>mbox</code> files. Failure to do so may result in loss of e-mail data, and in corrupted <code>mbox</code> files.</p>
<h2>Files</h2>
<p><i>/var/spool/mail/$LOGNAME</i></p>
<dl>
<dd><code>$LOGNAME</code>&#8216;s incoming mail folder.</dl>
<p> <i>$HOME/mbox</i></p>
<dl>
<dd>user&#8217;s archived mail messages, in his <code>$HOME</code> directory.</dl>
<p> <i>$HOME/Mail/</i></p>
<dl>
<dd>A directory in user&#8217;s <code>$HOME</code> directory which is commonly used to hold <code>mbox</code> format folders.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-asctime/">asctime</a></code>(3), <code><a href="/docs/linux/man/5-maildir/">maildir</a></code>(5), <code><a href="/docs/linux/man/5-mmdf/">mmdf</a></code>(5), <code>RFC822</code>, <code>RFC976</code>, <code>RFC2822</code></p>
<h2>Author</h2>
<p>Thomas Roessler &lt;roessler [at] does-not-exist.org&gt;, Urs Janssen &lt;urs [at] tin.org&gt;</p>
<h2>History</h2>
<p>The <code>mbox</code> format occurred in Version 6 AT&amp;T Unix.<br />
 A variant of this format was documented in <code>RFC976</code>.</p>
