---
title: "lockfile-progs(1)"
name: "lockfile-progs"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lockfile-progs/"
description: "lockfile-progs – command-line programs to safely lock and unlock files and mailboxes (via liblockfile)."
---

<h2>NAME</h2>
<p> lockfile-progs &#8211; command-line programs to safely lock and unlock files and mailboxes (via liblockfile).</p>
<h2>SYNOPSIS</h2>
<pre><code>
mail - lock[--use - pid][--retry retry - count] mail - unlock mail - touchlock[--oneshot] lockfile - create[--use - pid][--retry retry - count][--lock - name] filename lockfile - remove[--lock - name] filename lockfile - touch[--oneshot][--lock - name] filename lockfile - check[--use - pid][--lock - name] filename
</code></pre>
<h2>DESCRIPTION</h2>
<p> Lockfile-progs provides a set a programs that can be used to lock and unlock mailboxes and files safely (via liblockfile): </p>
<pre>
<dl><dt><dd><code>mail-lock</code> - lock the current user's mailbox
<code>mail-unlock</code> - unlock the current user's mailbox
<code>mail-touchlock</code> - touch the lock on the current user's mailbox
<code>lockfile-create</code> - lock a given file
<code>lockfile-remove</code> - remove the lock on a given file
<code>lockfile-touch</code> - touch the lock on a given file
<code>lockfile-check</code> - check the lock on a given file
</dl>
</pre>
<p> By default, the <i>filename</i> argument refers to the name of the file to be locked, and the name of the lockfile will be <i>filename</i> .lock. However, if the &#8211;lock-name argument is specified, then <i>filename</i> will be taken as the name of the lockfile itself. </p>
<p> Each of the mail locking commands attempts to lock /var/spool/mail/&lt;user&gt;, where &lt;user&gt; is the name associated with the effective user ID, as determined by via <a href="/docs/linux/man/2-geteuid/">geteuid</a>(2). </p>
<p> Once a file is locked, the lock must be touched at least once every five minutes or the lock will be considered stale, and subsequent lock attempts will succeed. Also see the <code>&#8211;use-pid</code> option and the <code><a href="/docs/linux/man/3-lockfile_create/">lockfile_create</a></code>(3) manpage. </p>
<p> The <code>lockfile-check</code> command tests whether or not a valid lock already exists. </p>
<h2>OPTIONS</h2>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Suppress any output. Success or failure will only be indicated by the exit status.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Enable diagnostic output.</dl>
<p> <code>-l</code>, <code>&#8211;lock-name</code></p>
<dl>
<dt>
<dd> Do not append .lock to the <i>filename</i>. This option applies to <code>lockfile-create</code>, <code>lockfile-remove</code>, <code>lockfile-touch</code>, or <code>lockfile-check</code>.</dl>
<p> <code>-p</code>, <code>&#8211;use-pid</code></p>
<dl>
<dt>
<dd> Write the current process id (PID) to the lockfile whenever a lockfile is created, and use that pid when checking a lock&#8217;s validity. See the <code><a href="/docs/linux/man/3-lockfile_create/">lockfile_create</a></code>(3) manpage for more information. This option applies to <code>lockfile-create</code>, <code>lockfile-remove</code>, <code>lockfile-touch</code>, and <code>lockfile-check</code>.</dl>
<p> <code>-o</code>, <code>&#8211;oneshot</code></p>
<dl>
<dt>
<dd> Touch the lock and exit immediately. This option applies to <code>lockfile-touch</code> and <code>mail-touchlock</code>. When not provided, these commands will run forever, touching the lock once every minute until killed.</dl>
<p> <code>-r</code> <i>retry-count</i>, <code>&#8211;retry</code> <i>retry-count</i></p>
<dl>
<dt>
<dd> Try to lock <i>filename</i> <i>retry-count</i> times before giving up. Each attempt will be delayed a bit longer than the last (in 5 second increments) until reaching a maximum delay of one minute between retries. If <i>retry-count</i> is unspecified, the default is 9 which will give up after 180 seconds (3 minutes) if all 9 lock attempts fail. </p>
</dl>
<h2>EXAMPLES</h2>
<p> <code>Locking a file during a lengthy process:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>lockfile-create&nbsp;<wbr>/some/file<br />
&nbsp;<wbr>&nbsp;<wbr>lockfile-touch&nbsp;<wbr>/some/file&nbsp;<wbr>&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Save the PID of the lockfile-touch process<br />
&nbsp;<wbr>&nbsp;<wbr>BADGER=&quot;$!&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>do-something-important-with&nbsp;<wbr>/some/file<br />
&nbsp;<wbr>&nbsp;<wbr>kill&nbsp;<wbr>&quot;${BADGER}&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>lockfile-remove&nbsp;<wbr>/some/file </p>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> For <code>lockfile-check</code> this indicates that a valid lock exists, otherwise it just indicates successful program execution.</dl>
<p> <code>Not 0</code></p>
<dl>
<dt>
<dd> For <code>lockfile-check</code> a non-zero exit status indicates that the specified lock does not exist or is not valid. For other programs it indicates that some problem was encountered.</dl>
<h2>SEE ALSO</h2>
<pre>
<code><a href="//www.systutorials.com/docs/linux/man/3-maillock/">maillock</a></code>(3)
<code><a href="//www.systutorials.com/docs/linux/man/3-touchlock/">touchlock</a></code>(3)
<code><a href="//www.systutorials.com/docs/linux/man/3-mailunlock/">mailunlock</a></code>(3)
<code><a href="//www.systutorials.com/docs/linux/man/3-lockfile_create/">lockfile_create</a></code>(3)
<code><a href="//www.systutorials.com/docs/linux/man/3-lockfile_remove/">lockfile_remove</a></code>(3)
<code><a href="//www.systutorials.com/docs/linux/man/3-lockfile_touch/">lockfile_touch</a></code>(3)
<code><a href="//www.systutorials.com/docs/linux/man/3-lockfile_check/">lockfile_check</a></code>(3)
</pre>
<h2>AUTHOR</h2>
<p> Written by Rob Browning &lt;rlb [at] defaultvalue.org&gt; </p>
<h2>Index</h2>
