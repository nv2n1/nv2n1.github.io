---
title: "lockmail(1)"
name: "lockmail"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lockmail/"
description: "lockmail – create mail lock files"
---

<h2 class="name">NAME</h2>
<p> lockmail &#8211; create mail lock files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>lockmail</code> [-r] [-t&nbsp;<wbr><i>timeout</i>] {<i>lockfile</i>} {<i>program</i>} [argument&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>lockmail</code></p>
<dd>is a helper utility for working with mailbox files. Mailbox files must be locked to prevent other applications from modifying the mailbox at the same time. Different system use different locking conventions. <code>lockmail</code> uses two of the most common locking mechanisms in use, which should work reliably on most systems. </p>
<p> <i>lockfile</i> is the pathname to an existing mailbox file. By default, <code>lockmail</code> tries to lock the mailbox every five seconds (if the mailbox is already locked), and will give up after three minutes. After the mailbox is successfully locked, <code>lockmail</code> runs <i>program</i> as a child process, with any optional <i>argument</i>s. When <i>program</i> terminates, <code>lockmail</code> removes the mailbox lock, and terminates itself.</p>
<h2>OPTIONS</h2>
<p> -r</p>
<dl>
<dt>
<dd> If a regular lock fails, try a read-only lock. Use this option to lock mailbox files in a read-only directory.</dl>
<p> -t <i>timeout</i></p>
<dl>
<dt>
<dd> If the lock attempt fails, try again for up to <i>timeout</i> seconds. The actual timeout is rounded up to the next five second interval (a lock attempt is tried every five seconds).</dl>
<h2>DESCRIPTION</h2>
<p> This section briefly describes the locking mechanism used by <code>lockmail</code>. <code>lockmail</code> uses three different locking conventions in order to maximize compatibility with other mail software: C-Client folder locks, dot-locks, and file locks.</p>
<h3>C-Client folder locks</h3>
<p> Mail software based on the C-Client library creates lock files named /tmp/.<i>dddddd</i>.<i>iiiiii</i>. Here, <i>dddddd</i> and <i>iiiiii</i> are the device number and the inode number of the mailbox file (the <i>st_dev</i> and <i>st_ino</i> fields in the inode), in hexadecimal. If the process ID saved in the C-Client folder lock file is not valid, <code>lockmail</code> concludes that it&#8217;s a stale lock file, and will remove it. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> A race condition exists where a C-Client process is killed after it creates a lock file, but before saving its process ID in the lock file. The race window is very small, but it exists. The C-Client library does not appear to ever clear out the lock file. </p>
<p> <code>lockmail</code> attempts to resolve this race condition by deleting zero-length lock files that are at least five minutes old. </p>
</dl>
<h3>dot-locks</h3>
<p> <code>lockmail</code> also creates, and honors dot-lock files. Dot-lock files are first created as temporary files, then linked to <i>lockfile</i>.lock. The link operation fails if the dot-lock file already exists. <code>lockmail</code> uses an enhanced method of dot-locking, where its process ID, and the name of the server where <code>lockmail</code> is running is also saved in its dot-lock file. If the operation fails due to an existing dot-lock file that was created by another <code>lockmail</code> process on the same server, and the process ID no longer exists, this stale dot-lock file is removed immediately. In all other situations a dot-lock file older than five minutes is considered stale, and removed. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> A failure to create a dot-lock file is silently ignored if the reason for the failure is because <code>lockmail</code> does not have the write permission in the dot-lock file&#8217;s directory. The incoming mail spool directory (usually /var/mail) typically does not have global write permissions, so the attempt to create the dot-lock file in the spool directory will fail, and <code>lockmail</code> will be content with using file-locking only. </p>
</dl>
<h3>File locks</h3>
<p> The final locking mechanism <code>lockmail</code> uses is the operating system&#8217;s file locking facility. If <code>lockmail</code> fails to obtain all three locks, <code>lockmail</code> will sleep for five seconds and try again. The only exception is a failure to create a dot-lock because of no write access to the dot-lock file&#8217;s directory, which is ignored. If <code>lockmail</code> still fails to obtain all required locks in the amount of time specified by the <code>-t</code> option (or its default value), <code>lockmail</code> will terminate with the EX_TEMPFAIL exit code. </p>
<p> <code>lockmail</code> runs <i>program</i> after obtaining the last file lock, waits until <i>program</i> terminates, and releases all locks. <i>program</i> must terminate before any of the locks obtained by <code>lockmail</code> expire, and are considered stale. <code>lockmail</code> will then terminate with the same exit code as <i>program</i>.</p>
<h2>EXIT STATUS</h2>
<p> <code>lockmail</code> terminates with the same exit status as <i>program</i><code>lockmail</code> terminates with the EX_TEMPFAIL exit status if it was unable to obtain a lock, or if <i>program</i> was killed by a signal.</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)m[]<font SIZE="-2">[1]</font>, <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8).</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd> Author</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildrop.html</dl>
</dl>
<h2>Index</h2>
