---
title: "dotlockfile(1)"
name: "dotlockfile"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dotlockfile/"
description: "dotlockfile – Utility to manage lockfiles"
---

<h2>NAME</h2>
<p> dotlockfile &#8211; Utility to manage lockfiles</p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/bin/dotlockfile</code> [<code>-p</code>] [<code>-c</code>] [<code>-m</code>] [<code>-l|-u|-t</code>] [<code>-r</code> <i>retries</i>] [<code>lockfile]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Dotlockfile</code> is a command line utility to safely create, test and remove lockfiles. Lockfiles are created in an NFS-safe way. <code>Dotlockfile</code> can can also be used to lock and unlock mailboxes even if the mailspool directory is only writable by group mail. </p>
<p> The name <code>dotlockfile</code> comes from the way mailboxes are locked for updates on a lot of UNIX systems. A lockfile is created with the same filename as the mailbox but with the string &quot;<i>.lock</i>&quot; appended. </p>
<p> The names <code>dotlock</code> and <code>lockfile</code> were already taken &#8211; hence the name <code>dotlockfile</code> <i>:)</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code></p>
<dd> Create a lockfile. This is the default.</p>
<dt><code>-u</code></p>
<dd> Remove a lockfile.</p>
<dt><code>-c</code></p>
<dd> Check for the existence of a <code>valid</code> lockfile.</p>
<dt><code>-t</code></p>
<dd> Touch an existing lockfile (update the timestamp).</p>
<dt><code>-p</code></p>
<dd> Write the <i>process-id</i> of the calling process into the lockfile. Also when testing for an existing lockfile, check the contents for a process-id to find out if the lockfile is still valid.</p>
<dt><code>-r retries</code></p>
<dd> The number of times <code>dotlockfile</code> retries to acquire the lock if it failed the first time before giving up. The initial sleep after failing to acquire the lock is 5 seconds. After each next try, a sleep of 5 seconds <i>extra</i> occurs up to a maximum sleep of 60 seconds between tries. The default number of retries is 5.</p>
<dt><code>-m</code></p>
<dd> Lock or unlock the current users mailbox. The path to the mailbox is the default system mailspool directory (usually <i>/var/mail</i>) with the username as gotten from <i>getpwuid()</i> appended. If the environment variable <i>$MAIL</i> is set, that is used instead. Then the string <i>&quot;.lock&quot;</i> is appended to get the name of the actual lockfile.</p>
<dt>lockfile</p>
<dd> The lockfile to be created/removed, unless the <code>-m</code> option is in effect. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> Zero on success, and non-zero on failure. For the <code>-c</code> option, sucess means that a valid lockfile is already present. When locking (the default, or the <code>-l</code> option) <code>dotlockfile</code> returns the same values as the library function <i><a href="/docs/linux/man/3-lockfile_create/">lockfile_create</a></i>(3). Unlocking a non-existant lockfile is not an error. </p>
<h2>NOTES</h2>
<p> The lockfile is created exactly as named on the command line. The extension <i>.lock</i> is <i>not</i> automatically added. </p>
<p> This utility is a lot like the <i><a href="/docs/linux/man/1-lockfile/">lockfile</a></i>(1) utility included with <i>procmail</i>, and the <i><a href="/docs/linux/man/1-mutt_dotlock/">mutt_dotlock</a></i>(1) utility included with <i>mutt</i>. However the command-line arguments differ, and so does the return status. It is believed that <i>dotlockfile</i> is the most flexible implementation, since it automatically detects when it needs to use priviliges to lock a mailbox, and does it safely. </p>
<p> The above mentioned <i><a href="/docs/linux/man/3-lockfile_create/">lockfile_create</a></i>(3) manpage is present in the <i>liblockfile-dev</i> package. </p>
<h2>BUGS</h2>
<p> None known. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-lockfile_create/">lockfile_create</a>(3), <a href="/docs/linux/man/3-maillock/">maillock</a>(3) </p>
<h2>AUTHOR</h2>
<p> Miquel van Smoorenburg, miquels [at] cistron.nl </p>
<h2>Index</h2>
