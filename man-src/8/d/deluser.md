---
title: "deluser(8)"
name: "deluser"
section: "8"
letter: "d"
url: "/docs/linux/man/8-deluser/"
description: "deluser, delgroup – remove a user or group from the system"
---

<p>deluser, delgroup &#8211; remove a user or group from the system</p>
<h2>Synopsis</h2>
<p><code>deluser</code> [options] [&#8211;force] [&#8211;remove-home] [&#8211;remove-all-files] [&#8211;backup] [&#8211;backup-to DIR] user </p>
<p> <code>deluser</code> &#8211;group [options] group<br />
 <code>delgroup</code> [options] [&#8211;only-if-empty] group </p>
<p> <code>deluser</code> [options] user group</p>
<h3>Common Options</h3>
<p>[&#8211;quiet] [&#8211;system] [&#8211;help] [&#8211;version] [&#8211;conf FILE]</p>
<h2>Description</h2>
<p><code>deluser</code> and <code>delgroup</code> remove users and groups from the system according to command line options and configuration information in <i>/etc/deluser.conf</i> and <i>/etc/adduser.conf</i>. They are friendlier front ends to the <code>userdel</code> and <code>groupdel</code> programs, removing the home directory as option or even all files on the system owned by the user to be removed, running a custom script, and other features. <code>deluser</code> and <code>delgroup</code> can be run in one of three modes:</p>
<h3>Remove a normal user</h3>
<p>If called with one non-option argument and without the <code>&#8211;group</code> option, <code>deluser</code> will remove a normal user. </p>
<p> By default, <code>deluser</code> will remove the user without removing the home directory, the mail spool or any other files on the system owned by the user. Removing the home directory and mail spool can be achieved using the <code>&#8211;remove-home</code> option. </p>
<p> The <code>&#8211;remove-all-files</code> option removes all files on the system owned by the user. Note that if you activate both options <code>&#8211;remove-home</code> will have no effect because all files including the home directory and mail spool are already covered by the <code>&#8211;remove-all-files</code> option. </p>
<p> If you want to backup all files before deleting them you can activate the <code>&#8211;backup</code> option which will create a file username.tar(.gz|.bz2) in the directory specified by the <code>&#8211;backup-to</code> option (defaulting to the current working directory). Both the remove and backup options can also be activated for default in the configuration file /etc/deluser.conf. See <code><a href="/docs/linux/man/5-deluser-conf/">deluser.conf</a>(5)</code> for details. </p>
<p> If you want to remove the root account (uid 0), then use the <code>&#8211;force </code> parameter; this may prevent to remove the root user by accident. </p>
<p> If the file <code>/usr/local/sbin/deluser.local</code> exists, it will be executed after the user account has been removed in order to do any local cleanup. The arguments passed to <code>deluser.local</code> are:<br />
 username uid gid home-directory</p>
<h3>Remove a group</h3>
<p>If <code>deluser</code> is called with the <code>&#8211;group</code> option, or <code>delgroup</code> is called, a group will be removed. </p>
<p> Warning: The primary group of an existing user cannot be removed. </p>
<p> If the option <code>&#8211;only-if-empty</code> is given, the group won&#8217;t be removed if it has any members left.</p>
<h3>Remove a user from a specific group</h3>
<p>If called with two non-option arguments, <code>deluser</code> will remove a user from a specific group.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;conf FILE</code></p>
<dd>Use FILE instead of the default files <i>/etc/deluser.conf</i> and <i>/etc/adduser.conf</i></p>
<dt><code>&#8211;group</code></p>
<dd>Remove a group. This is the default action if the program is invoked as <i>delgroup</i>.</p>
<dt><code>&#8211;help</code></p>
<dd>Display brief instructions.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Suppress progress messages.</p>
<dt><code>&#8211;system</code></p>
<dd>Only delete if user/group is a system user/group. This avoids accidentally deleting non-system users/groups. Additionally, if the user does not exist, no error value is returned. This option is mainly for use in Debian package maintainer scripts.</p>
<dt><code>&#8211;only-if-empty </code></p>
<dd>Only remove if no members are left.</p>
<dt><code>&#8211;backup</code></p>
<dd>Backup all files contained in the userhome and the mailspool-file to a file named /$user.tar.bz2 or /$user.tar.gz.</p>
<dt><code>&#8211;backup-to</code></p>
<dd>Place the backup files not in / but in the directory specified by this parameter. This implicitly sets &#8211;backup also.</p>
<dt><code>&#8211;remove-home</code></p>
<dd>Remove the home directory of the user and its mailspool. If &#8211;backup is specified, the files are deleted after having performed the backup.</p>
<dt><code>&#8211;remove-all-files</code></p>
<dd>Remove all files from the system owned by this user. Note: &#8211;remove-home does not have an effect any more. If &#8211;backup is specified, the files are deleted after having performed the backup.</p>
<dt><code>&#8211;version</code></p>
<dd>Display version and copyright information.</dl>
<h2>Return Value</h2>
<dl>
<dt><code>0</code></p>
<dd>The action was successfully executed.</p>
<dt><code>1</code></p>
<dd>The user to delete was not a system account. No action was performed.</p>
<dt><code>2</code></p>
<dd>There is no such user. No action was performed.</p>
<dt><code>3</code></p>
<dd>There is no such group. No action was performed.</p>
<dt><code>4</code></p>
<dd>Internal error. No action was performed.</p>
<dt><code>5</code></p>
<dd>The group to delete is not empty. No action was performed.</p>
<dt><code>6</code></p>
<dd>The user does not belong to the specified group. No action was performed.</p>
<dt><code>7</code></p>
<dd>You cannot remove a user from its primary group. No action was performed.</p>
<dt><code>8</code></p>
<dd>The required perl-package &#8216;perl modules&#8217; is not installed. This package is required to perform the requested actions. No action was performed.</p>
<dt><code>9</code></p>
<dd>For removing the root account the parameter &quot;&#8211;force&quot; is required. No action was performed. </p>
<h2>Files</h2>
<p><i>/etc/deluser.conf</i> Default configuration file for deluser and delgroup</p>
<dl>
<dt><i>/usr/local/sbin/deluser.local</i></p>
<dd>Optional custom add-ons. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-adduser/">adduser</a></code>(8), <code><a href="/docs/linux/man/5-deluser-conf/">deluser.conf</a></code>(5), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8) </p>
<h2>Copyright</h2>
<p>Copyright (C) 2000 Roland Bauerschmidt. Modifications (C) 2004 Marc Haber and Joerg Hoh. This manpage and the deluser program are based on adduser which is:<br />
 Copyright (C) 1997, 1998, 1999 Guy Maor.<br />
 Copyright (C) 1995 Ted Hajek, with a great deal borrowed from the original Debian <code>adduser</code><br />
 Copyright (C) 1994 Ian Murdock. <code>deluser</code> is free software; see the GNU General Public Licence version 2 or later for copying conditions. There is <i>no</i> warranty.</p>
