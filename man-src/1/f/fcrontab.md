---
title: "fcrontab(1)"
name: "fcrontab"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcrontab/"
description: "fcrontab – manipulate per-user fcrontab files"
---

<h2 class="name">NAME</h2>
<p> fcrontab &#8211; manipulate per-user fcrontab files </p>
<h2>SYNOPSIS</h2>
<p> <code>fcrontab</code> [ <code>-c </code><i>file</i> ] [ <code>-n</code> ] <i>file</i> [ <i>user</i> | <code>-u </code><i>user</i> ] </p>
<p> <code>fcrontab</code> [ <code>-c </code><i>file</i> ] [ <code>-n</code> ] { <code>-l</code> | <code>-r</code> | <code>-e</code> | <code>-z</code> } [ <i>user</i> | <code>-u </code><i>user</i> ] </p>
<p> <code>fcrontab</code> [ <code>-h</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>Fcrontab</code> is the program intended to install, edit, list and remove the tables used by <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8) daemon. As <code>fcron</code> internally uses a non-human readable format (this is needed because <code>fcron</code> saves more informations than the user gives, for example the time and date of next execution), the user cannot edit directly his <code>fcrontab</code> (the one used by <code>fcron</code>). </p>
<p> When a user installs a <code>fcrontab</code>, the source file is saved in the spool directory (<i>/usr/local/var/spool/fcron</i>) to allow future editions, and a formatted file is generated for the <code>fcron</code> daemon, which is signaled once about ten seconds before the next minute for all changes made previously. The daemon is not informed of the changes immediately but at most once a minute to keep ill disposed users from blocking the daemon by installing <code>fcrontab</code>s over and over (ie. denial of service attack). We will call &quot;<code>fcrontab</code>&quot; the source file of the <code>fcrontab</code> in the following. </p>
<p> A user can install a <code>fcrontab</code> if he is listed in the <i>/usr/local/etc/fcron.allow</i> and not (unless by the keyword all) listed in <i>/usr/local/etc/fcron.deny</i> (see section &quot;files&quot; below). If neither <i>fcron.allow</i> nor <i>fcron.deny</i> exist, all users are allowed. None of these files have to exist, but if they do, the deny file takes precedence. </p>
<p> The first form of the command is used to install a new <code>fcrontab</code> file, from any named file or from standard input if the pseudo-filename &quot;-&quot; is given, replacing the previous one (if any): each user can have only one <code>fcrontab</code>. </p>
<p> For instance, root can create a systemwide fcrontab file, say <i>/etc/fcrontab</i>, and run &quot;<code>fcrontab</code> <i>/etc/fcrontab</i>&quot; to install the new version after each change of the file. Or (s)he can create a new fcrontab running a simple &quot;<code>fcrontab</code>&quot;, and then maintain it using &quot;<code>fcrontab</code> <code>-e</code>&quot;. Same considerations apply to a non privileged user.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u </code><i>user</i></p>
<dd> Specify the user whose <code>fcrontab</code> will be managed, or &quot;systab&quot; for the system fcrontab. Should only be used by root. If not given, the <code>fcrontab</code> file of the user invoking <code>fcrontab</code> will be handled. It may be useful since the <code><a href="/docs/linux/man/8-su/">su</a></code>(8) command may confuse <code>fcrontab</code>. </p>
<dl>
<dt>
<dd> <code>Note:</code> the &#8216;<i>user</i>&#8216; in the synopsys is equivalent to a &#8216;<code>-u</code> <i>user</i>&#8216;.</dl>
<dt><code>-l</code></p>
<dd> List user&#8217;s current <code>fcrontab</code> to standard output.</p>
<dt><code>-e</code></p>
<dd> Edit user&#8217;s current <code>fcrontab</code> using either the editor specified by the environment variable <code>VISUAL</code>, or <code>EDITOR</code> if <code>VISUAL</code> is not set. If none or them are set, <code>/usr/bin/vi</code> will be used.</p>
<dt><code>-r</code></p>
<dd> Remove user&#8217;s <code>fcrontab</code>.</p>
<dt><code>-z</code></p>
<dd> Reinstall user&#8217;s <code>fcrontab</code> from its source code. All informations <code>fcron</code> may have kept in the binary <code>fcrontab</code> (such as the last execution time and date) will be forgotten (ie. lost).</p>
<dt><code>-n</code></p>
<dd> Ignore previous version. If this option is not given, <code>fcron</code> will try to keep as much information as possible between old and new version of the <code>fcrontab</code> (time and date of next execution, if job is in serial queue, etc) if the line hasn&#8217;t been modified (same fields, same shell command).</p>
<dt><code>-c </code><i>file</i></p>
<dd> Make <code>fcrontab</code> use config file <i>file</i> instead of default config file <i>/usr/local/etc/fcron.conf</i>. To interact with a running <code>fcron</code> process, <code>fcrontab</code> must use the same config file as the process. That way, several <code>fcron</code> processes can run simultaneously on an only system.</p>
<dt><code>-d</code></p>
<dd> Run in debug mode. In this mode, many informational messages will be output in order to check if anything went wrong.</p>
<dt><code>-h</code></p>
<dd> Display a brief description of the options.</p>
<dt><code>-V</code></p>
<dd> Display an informational message about <code>fcrontab</code>, including its version and the license under which it is distributed.</dl>
<h2>RETURN VALUES</h2>
<p> <code>Fcrontab</code> returns 0 on normal exit and 1 on error.</p>
<h2>CONFORMING TO</h2>
<p> Should be POSIX compliant.</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/local/etc/fcron.conf</i></p>
<dd> Configuration file for <code>fcron</code>, <code>fcrontab</code> and <code>fcrondyn</code>: contains paths (spool dir, pid file) and default programs to use (editor, shell, etc). See <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5) for more details.</p>
<dt><i>/usr/local/etc/fcron.allow</i></p>
<dd> Users allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (one name per line, special name &quot;all&quot; acts for everyone)</p>
<dt><i>/usr/local/etc/fcron.deny</i></p>
<dd> Users who are not allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (same format as allow file)</p>
<dt><i>/usr/local/etc/pam.d/fcron</i><code> (or </code><i>/usr/local/etc/pam.conf</i><code>)</code></p>
<dd> PAM configuration file for <code>fcron</code>. Take a look at <a href="/docs/linux/man/8-pam/">pam</a>(8) for more details.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fcrontab/">fcrontab</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/1-fcrondyn/">fcrondyn</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8). </p>
<p> If you&#8217;re learning how to use fcron from scratch, I suggest that you read the HTML version of the documentation (if your are not reading it right now! :) ): the content is the same, but it is easier to navigate thanks to the hyperlinks.</p>
<h2>AUTHOR</h2>
<p> Thibault Godouet &lt;fcron [at] free.fr&gt; </p>
<h2>Index</h2>
