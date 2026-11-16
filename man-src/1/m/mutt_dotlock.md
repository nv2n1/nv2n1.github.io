---
title: "mutt_dotlock(1)"
name: "mutt_dotlock"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mutt_dotlock/"
description: "mutt_dotlock – Lock mail spool files."
---

<h2 class="name">NAME</h2>
<p> mutt_dotlock &#8211; Lock mail spool files. </p>
<h2>SYNOPSIS</h2>
<p> <code>mutt_dotlock </code> [-t|-f|-u|-d] [-p] [-r <i>retries</i>] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mutt_dotlock</code> implements the traditional mail spool file locking method: To lock <i>file</i>, a file named <i>file</i>.lock is created. The program operates with group mail privileges if necessary.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-t</dt>
<dd> Just try. <code>mutt_dotlock</code> won&#8217;t actually lock a file, but inform the invoking process if it&#8217;s at all possible to lock <i>file</i>.</dd>
<dt>-f</dt>
<dd> Force the lock. If another process holds a lock on <i>file</i> longer than a certain amount of time, <code>mutt_dotlock</code> will break that lock by removing the lockfile.</dd>
<dt>-u</dt>
<dd> Unlock. <code>mutt_dotlock </code> will remove <i>file</i>.lock.</dd>
<dt>-d</dt>
<dd> Delete. <code>mutt_dotlock</code> will lock <i>file</i>, remove it if it has length 0, and afterwards remove <i>file</i>.lock.</dd>
<dt>-p</dt>
<dd> Use privileges. If given this option, <code>mutt_dotlock</code> will operate with group mail privileges when creating and deleting lock files.</dd>
<dt>-r <i>retries</i></dt>
<dd> This command line option tells <code>mutt_dotlock </code> to try locking <i>retries</i> times before giving up or (if invoked with the <code>-f</code> command line option) break a lock. The default value is 5. <code>mutt_dotlock</code> waits one second between successive locking attempts.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>file</i>.lock</dt>
<dd> The lock file <code>mutt_dotlock</code> generates.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2), <code><a href="/docs/linux/man/1-lockfile/">lockfile</a></code>(1), <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1)</p>
<h2>DIAGNOSTICS</h2>
<p> <code>mutt_dotlock</code> gives all diagnostics in its return values:</p>
<dl>
<dt><code>0 &#8211; DL_EX_OK</code></dt>
<dd> The program was successful.</dd>
<dt><code>1 &#8211; DL_EX_ERROR</code></dt>
<dd> An unspecified error such as bad command line parameters, lack of system memory and the like has occurred.</dd>
<dt><code>3 &#8211; DL_EX_EXIST</code></dt>
<dd> The user wants to lock a file which has been locked by another process already. If <code>mutt_dotlock</code> is invoked with the <code>-f </code> command line option, <code>mutt_dotlock</code> won&#8217;t generate this error, but break other processes&#8217; locks.</dd>
<dt><code>4 &#8211; DL_EX_NEED_RPIVS</code></dt>
<dd> This return value only occurs if <code>mutt_dotlock </code> has been invoked with the <code>-t</code> command line option. It means that <code>mutt_dotlock</code> will have to use its group mail privileges to lock <i>file</i>.</dd>
<dt><code>5 &#8211; DL_EX_IMPOSSIBLE</code></dt>
<dd> This return value only occurs if <code>mutt_dotlock</code> has been invoked with the <code>-t</code> command line option. It means that <code>mutt_dotlock </code> is unable to lock <i>file</i> even with group mail privileges.</dd></dl>
<h2>NOTES</h2>
<p> <code>mutt_dotlock</code> tries to implement an NFS-safe dotlocking method which was borrowed from <code>lockfile</code> (1). </p>
<p> If the user can&#8217;t open <i>file</i> for reading with his normal privileges, <code>mutt_dotlock </code> will return the <code>DL_EX_ERROR</code> exit value to avoid certain attacks against other users&#8217; spool files. The code carefully avoids race conditions when checking permissions; for details of all this see the comments in dotlock.c.</p>
<h2>HISTORY</h2>
<p> <code>mutt_dotlock</code> is part of the Mutt mail user agent package. It has been created to avoid running mutt with group mail privileges.</p>
<h2>AUTHOR</h2>
<p> Thomas Roessler &lt;roessler [at] does-not-exist.org&gt; </p>
<h2>Index</h2>
