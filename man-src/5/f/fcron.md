---
title: "fcron(5)"
name: "fcron"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fcron/"
description: "fcron.conf – configuration file for fcron and fcrontab"
---

<p>fcron.conf &#8211; configuration file for fcron and fcrontab</p>
<h2>Description</h2>
<h3>Abstract</h3>
<p>This page describes the syntax used for the configuration file of <code><a href="/docs/linux/man/1-fcrontab/">fcrontab</a></code>(1), <code><a href="/docs/linux/man/1-fcrondyn/">fcrondyn</a></code>(1) and <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8). Blank lines, line beginning by a hash sign (#) (which are considered comments), leading blanks and tabs are ignored. Each line in a <code>fcron.conf</code> file is of the form  name = value</dl>
<p> where the blanks around equal-sign (=) are ignored and optional. Trailing blanks are also ignored. The following names are recognized (default value in parentheses): &quot;VALID VARIABLES IN A FCRON.CONF FILE&quot;</p>
<dl>
<dt><code>fcrontabs=</code><i>directory</i><code> (</code><i>/usr/local/var/spool/fcron</i><code>)</code></p>
<dd><code>Fcron</code> spool directory.</p>
<dt><code>pidfile=</code><i>file-path</i><code> (</code><i>/usr/local/var/run/fcron.pid</i><code>)</code></p>
<dd>Location of <code>fcron</code> pid file (needed by <code>fcrontab</code> to work properly).</p>
<dt><code>fifofile=</code><i>file-path</i><code> (</code><i>/usr/local/var/run/fcron.fifo</i><code>)</code></p>
<dd>Location of <code>fcron</code> fifo file (needed by <code>fcrondyn</code> to communicate with <code>fcron</code>).</p>
<dt><code>fcronallow=</code><i>file-path</i><code> (</code><i>/usr/local/etc/fcron.allow</i><code>)</code></p>
<dd>Location of fcron.allow file.</p>
<dt><code>fcrondeny=</code><i>file-path</i><code> (</code><i>/usr/local/etc/fcron.deny</i><code>)</code></p>
<dd>Location of fcron.deny file.</p>
<dt><code>shell=</code><i>file-path</i><code> (</code><i>/bin/sh</i><code>)</code></p>
<dd>Location of default shell called by <code>fcron</code> when running a job. When <code>fcron</code> runs a job, <code>fcron</code> uses the value of <code>SHELL</code> from the fcrontab if any, otherwise it uses the value from <i>fcron.conf</i> if any, or in last resort the value from <i>/etc/passwd</i>.</p>
<dt><code>sendmail=</code><i>file-path</i><code> (</code><i>/usr/sbin/sendmail</i><code>)</code></p>
<dd>Location of mailer program called by <code>fcron</code> to send job output.</p>
<dt><code>editor=</code><i>file-path</i><code> (</code><i>/usr/bin/vi</i><code>)</code></p>
<dd>Location of default editor used when invoking &quot;fcrontab -e&quot;. File-paths and directories are complete and absolute (i.e. beginning by a &quot;/&quot;).</dl>
<p> To run several instances of <code>fcron</code> simultaneously on the same system, you must use a different configuration file for each instance. Each instance must have a different fcrontabs, pidfile and fifofile. Then, use <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8)&#8217;s command line option <i>-c</i> to select which config file (so which instance) you refer to.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/local/etc/fcron.conf</i></p>
<dd>Configuration file for <code>fcron</code>, <code>fcrontab</code> and <code>fcrondyn</code>: contains paths (spool dir, pid file) and default programs to use (editor, shell, etc). See <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5) for more details.</p>
<dt><i>/usr/local/etc/fcron.allow</i></p>
<dd>Users allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (one name per line, special name &quot;all&quot; acts for everyone)</p>
<dt><i>/usr/local/etc/fcron.deny</i></p>
<dd>Users who are not allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (same format as allow file)</p>
<dt><i>/usr/local/etc/pam.d/fcron</i><code> (or </code><i>/usr/local/etc/pam.conf</i><code>)</code></p>
<dd>PAM configuration file for <code>fcron</code>. Take a look at <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) for more details.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fcrontab/">fcrontab</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/1-fcrondyn/">fcrondyn</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8). </p>
<p> If you&#8217;re learning how to use fcron from scratch, I suggest that you read the HTML version of the documentation (if your are not reading it right now! :) ): the content is the same, but it is easier to navigate thanks to the hyperlinks.</p>
<h2>Author</h2>
<p>Thibault Godouet &lt;fcron [at] free.fr&gt;</p>
