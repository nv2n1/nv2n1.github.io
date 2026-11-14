---
title: "postlock(1)"
name: "postlock"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postlock/"
description: "postlock – lock mail folder and execute command"
---

<h2 class="name">NAME</h2>
<p> postlock &#8211; lock mail folder and execute command </p>
<h2>SYNOPSIS</h2>
<p> <code>postlock</code> [<code>-c </code><i>config_dir</i>] [<code>-l </code><i>lock_style</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-v</code>]&nbsp;<i>file command&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postlock/">postlock</a></code>(1) command locks <i>file</i> for exclusive access, and executes <i>command</i>. The locking method is compatible with the Postfix UNIX-style local delivery agent. </p>
<p> Options:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd> Read the <code>main.cf</code> configuration file in the named directory instead of the default configuration directory.</p>
<dt><code>-l </code><i>lock_style</i></p>
<dd> Override the locking method specified via the <code>mailbox_delivery_lock</code> configuration parameter (see below).</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<p> Arguments:</p>
<dl>
<dt><i>file</i></p>
<dd> A mailbox file. The user should have read/write permission.</p>
<dt><i>command&#8230;</i></p>
<dd> The command to execute while <i>file</i> is locked for exclusive access. The command is executed directly, i.e. without interpretation by a shell command interpreter.</dl>
<h2>DIAGNOSTICS</h2>
<p> The result status is 75 (EX_TEMPFAIL) when <code><a href="/docs/linux/man/1-postlock/">postlock</a></code>(1) could not perform the requested operation. Otherwise, the exit status is the exit status from the command.</p>
<h2>BUGS</h2>
<p> With remote file systems, the ability to acquire a lock does not necessarily eliminate access conflicts. Avoid file access by processes running on different machines.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> Directory with Postfix configuration files.</p>
<dt><code>MAIL_VERBOSE</code></p>
<dd> Enable verbose logging for debugging purposes.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>LOCKING CONTROLS</h2>
<dl>
<dt><code>deliver_lock_attempts (20)</code></p>
<dd> The maximal number of attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>deliver_lock_delay (1s)</code></p>
<dd> The time between attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>stale_lock_time (500s)</code></p>
<dd> The time after which a stale exclusive mailbox lockfile is removed.</p>
<dt><code>mailbox_delivery_lock (see &#8216;postconf -d&#8217; output)</code></p>
<dd> How to lock a UNIX-style <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mailbox before attempting delivery.</dl>
<h2>RESOURCE AND RATE CONTROLS</h2>
<dl>
<dt><code>fork_attempts (5)</code></p>
<dd> The maximal number of attempts to fork() a child process.</p>
<dt><code>fork_delay (1s)</code></p>
<dd> The delay between attempts to fork() a child process.</dl>
<h2>MISCELLANEOUS CONTROLS</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
