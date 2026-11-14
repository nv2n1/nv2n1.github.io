---
title: "lastlog(8)"
name: "lastlog"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lastlog/"
description: "lastlog – reports the most recent login of all users or of a given user"
---

<p>lastlog &#8211; reports the most recent login of all users or of a given user</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>lastlog</code> [<i>options</i>]</dl>
<h2>Description</h2>
<p><code>lastlog</code></p>
<dd>formats and prints the contents of the last login log /var/log/lastlog file. The <i>login-name</i>, <i>port</i>, and <i>last login time</i> will be printed. The default (no flags) causes lastlog entries to be printed, sorted by their order in /etc/passwd.</p>
<h2>Options</h2>
<p>The options which apply to the <code>lastlog</code> command are: </p>
<p> <code>-b</code>, <code>&#8211;before</code>&nbsp;<i>DAYS</i></p>
<dl>
<dd>Print only lastlog records older than <i>DAYS</i>.</dl>
<p> <code>-C</code>, <code>&#8211;clear</code></p>
<dl>
<dd>Clear lastlog record of a user. This option can be used only together with <code>-u</code> (<code>&#8211;user</code>)).</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-S</code>, <code>&#8211;set</code></p>
<dl>
<dd>Set lastlog record of a user to the current time. This option can be used only together with <code>-u</code> (<code>&#8211;user</code>)).</dl>
<p> <code>-t</code>, <code>&#8211;time</code>&nbsp;<i>DAYS</i></p>
<dl>
<dd>Print the lastlog records more recent than <i>DAYS</i>.</dl>
<p> <code>-u</code>, <code>&#8211;user</code>&nbsp;<i>LOGIN</i>|<i>RANGE</i></p>
<dl>
<dd>Print the lastlog record of the specified user(s). </p>
<p> The users can be specified by a login name, a numerical user ID, or a <i>RANGE</i> of users. This <i>RANGE</i> of users can be specified with a min and max values (<i>UID_MIN-UID_MAX</i>), a max value (<i>-UID_MAX</i>), or a min value (<i>UID_MIN-</i>).</dl>
<p> If the user has never logged in the message <i>** Never logged in**</i> will be displayed instead of the port and time. </p>
<p> Only the entries for the current users of the system will be displayed. Other entries may exist for users that were deleted previously.</p>
<h2>Note</h2>
<p>The lastlog file is a database which contains info on the last login of each user. You should not rotate it. It is a sparse file, so its size on the disk is usually much smaller than the one shown by &quot;<code>ls -l</code>&quot; (which can indicate a really big file if you have in passwd users with a high UID). You can display its real size with &quot;<code>ls -s</code>&quot;.</p>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>LASTLOG_UID_MAX</code> (number)</p>
<dl>
<dd>Highest user ID number for which the lastlog entries should be updated. As higher user IDs are usually tracked by remote user identity and authentication services there is no need to create a huge sparse lastlog file for them. </p>
<p> No <code>LASTLOG_UID_MAX</code> option present in the configuration means that there is no user ID limit for writing lastlog entries.</dl>
<h2>Files</h2>
<p>/var/log/lastlog</p>
<dl>
<dd>Database times of previous user logins.</dl>
<h2>Caveats</h2>
<p>Large gaps in UID numbers will cause the lastlog program to run longer with no output to the screen (i.e. if in lastlog database there is no entries for users with UID between 170 and 800 lastlog will appear to hang as it processes entries with UIDs 171-799).</p>
