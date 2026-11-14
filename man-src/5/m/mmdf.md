---
title: "mmdf(5)"
name: "mmdf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mmdf/"
description: "MMDF – Multi-channel Memorandum Distribution Facility mailbox format"
---

<p>MMDF &#8211; Multi-channel Memorandum Distribution Facility mailbox format</p>
<h2>Description</h2>
<p>This document describes the <code>MMDF</code> mailbox format used by some MTAs and MUAs (i.e. <code><a href="/docs/linux/man/1-scomail/">scomail</a></code>(1)) to store mail messages locally. </p>
<p> An <code>MMDF</code> mailbox is a text file containing an arbitrary number of e-mail messages. Each message consists of a postmark, followed by an e-mail message formatted according to <code>RFC822</code> / <code>RFC2822</code>, followed by a postmark. The file format is line-oriented. Lines are separated by line feed characters (ASCII 10). A postmark line consists of the four characters &quot;^A^A^A^A&quot; (Control-A; ASCII 1).</p>
<dl>
<dt>Example of a <code>MMDF</code> mailbox holding two mails:</p>
<dd>
<dl>
<dd>
<pre>^A^A^A^A
<br>
From: example [at] example.com
<br>
To: example [at] example.org
<br>
Subject: test
<br>
<br>
&gt;From what I learned about the MMDF-format:
<br>
<br>
^A^A^A^A
<br>
^A^A^A^A
<br>
From: example [at] example.com
<br>
To: example [at] example.org
<br>
Subject: test 2
<br>
<br>
bar
<br>
^A^A^A^A</pre>
</dl>
</dl>
<p> In contrast to most other single file mailbox formats like MBOXO and MBOXRD (see <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5)) there is no need to quote/dequote &quot;From &quot;-lines in <code>MMDF</code> mailboxes as such lines have no special meaning in this format. </p>
<p> If the modification-time (usually determined via <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)) of a nonempty mailbox file is greater than the access-time the file has new mail. Many MUAs place a Status: header in each message to indicate which messages have already been read.</p>
<h2>Locking</h2>
<p>Since <code>MMDF</code> files are frequently accessed by multiple programs in parallel, <code>MMDF</code> files should generally not be accessed without locking. </p>
<p> Three different locking mechanisms (and combinations thereof) are in general use:</p>
<dl>
<dt>&bull;</p>
<dd><code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locking is mostly used on recent, POSIX-compliant systems. Use of this locking method is, in particular, advisable if <code>MMDF</code> files are accessed through the Network File System (NFS), since it seems the only way to reliably invalidate NFS clients&#8217; caches.</p>
<dt>&bull;</p>
<dd><code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) locking is mostly used on BSD-based systems.</p>
<dt>&bull;</p>
<dd>Dotlocking is used on all kinds of systems. In order to lock an <code>MMDF</code> file named <i>folder</i>, an application first creates a temporary file with a unique name in the directory in which the <i>folder</i> resides. The application then tries to use the <code><a href="/docs/linux/man/2-link/">link</a></code>(2) system call to create a hard link named <i>folder.lock</i> to the temporary file. The success of the <code><a href="/docs/linux/man/2-link/">link</a></code>(2) system call should be additionally verified using <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) calls. If the link has succeeded, the mail folder is considered dotlocked. The temporary file can then safely be unlinked.</p>
<dd>In order to release the lock, an application just unlinks the <i>folder.lock</i> file.</dl>
<p> If multiple methods are combined, implementors should make sure to use the non-blocking variants of the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) and <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) system calls in order to avoid deadlocks. </p>
<p> If multiple methods are combined, an <code>MMDF</code> file must not be considered to have been successfully locked before all individual locks were obtained. When one of the individual locking methods fails, an application should release all locks it acquired successfully, and restart the entire locking procedure from the beginning, after a suitable delay. </p>
<p> The locking mechanism used on a particular system is a matter of local policy, and should be consistently used by all applications installed on the system which access <code>MMDF</code> files. Failure to do so may result in loss of e-mail data, and in corrupted <code>MMDF</code> files.</p>
<h2>Conforming To</h2>
<p><code>MMDF</code> is not part of any currently supported standard.</p>
<h2>History</h2>
<p><code>MMDF</code> was developed at the University of Delaware by Dave Crocker.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-scomail/">scomail</a></code>(1), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5), <code>RFC822</code>, <code>RFC2822</code> </p>
<h2>Author</h2>
<p>Urs Janssen &lt;urs [at] tin.org&gt;</p>
