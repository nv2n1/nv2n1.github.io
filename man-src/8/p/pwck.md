---
title: "pwck(8)"
name: "pwck"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pwck/"
description: "pwck – verify integrity of password files"
---

<p>pwck &#8211; verify integrity of password files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pwck</code> [options] [<i>passwd</i>&nbsp;[&nbsp;<i>shadow</i>&nbsp;]]</dl>
<h2>Description</h2>
<dd>The <code>pwck</code> command verifies the integrity of the users and authentication information. It checks that all entries in /etc/passwd and /etc/shadow have the proper format and contain valid data. The user is prompted to delete entries that are improperly formatted or which have other uncorrectable errors. </p>
<p> Checks are made to verify that each entry has: </p>
<dl>
<dd>&bull; the correct number of fields</dl>
<dl>
<dd>&bull; a unique and valid user name</dl>
<dl>
<dd>&bull; a valid user and group identifier</dl>
<dl>
<dd>&bull; a valid primary group</dl>
<dl>
<dd>&bull; a valid home directory</dl>
<dl>
<dd>&bull; a valid login shell</dl>
<p> shadow checks are enabled when a second file parameter is specified or when /etc/shadow exists on the system. </p>
<p> These checks are the following: </p>
<dl>
<dd>&bull; every passwd entry has a matching shadow entry, and every shadow entry has a matching passwd entry</dl>
<dl>
<dd>&bull; passwords are specified in the shadowed file</dl>
<dl>
<dd>&bull; shadow entries have the correct number of fields</dl>
<dl>
<dd>&bull; shadow entries are unique in shadow</dl>
<dl>
<dd>&bull; the last password changes are not in the future</dl>
<p> The checks for correct number of fields and unique user name are fatal. If the entry has the wrong number of fields, the user will be prompted to delete the entire line. If the user does not answer affirmatively, all further checks are bypassed. An entry with a duplicated user name is prompted for deletion, but the remaining checks will still be made. All other errors are warning and the user is encouraged to run the <code>usermod</code> command to correct the error. </p>
<p> The commands which operate on the /etc/passwd file are not able to alter corrupted or duplicated entries. <code>pwck</code> should be used in those circumstances to remove the offending entry.</p>
<h2>Options</h2>
<p>The <code>-r</code> and <code>-s</code> options cannot be combined. </p>
<p> The options which apply to the <code>pwck</code> command are: </p>
<p> <code>&#8211;badname</code>&nbsp;</p>
<dl>
<dd>Allow names that do not conform to standards.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Report errors only. The warnings which do not require any action from the user won&#8217;t be displayed.</dl>
<p> <code>-r</code>, <code>&#8211;read-only</code></p>
<dl>
<dd>Execute the <code>pwck</code> command in read-only mode.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-s</code>, <code>&#8211;sort</code></p>
<dl>
<dd>Sort entries in /etc/passwd and /etc/shadow by UID.</dl>
<p> By default, <code>pwck</code> operates on the files /etc/passwd and /etc/shadow. The user may select alternate files with the <i>passwd</i> and <i>shadow</i> parameters.</p>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>PASS_MAX_DAYS</code> (number)</p>
<dl>
<dd>The maximum number of days a password may be used. If the password is older than this, a password change will be forced. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_MIN_DAYS</code> (number)</p>
<dl>
<dd>The minimum number of days allowed between password changes. Any password changes attempted sooner than this will be rejected. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_WARN_AGE</code> (number)</p>
<dl>
<dd>The number of days warning given before a password expires. A zero means warning is given only upon the day of expiration, a negative value means no warning is given. If not specified, no warning will be provided.</dl>
<h2>Files</h2>
<p>/etc/group</p>
<dl>
<dd>Group account information.</dl>
<p> /etc/passwd</p>
<dl>
<dd>User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dd>Secure user account information.</dl>
<h2>Exit Values</h2>
<p>The <code>pwck</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dd>success</dl>
<p> <i>1</i></p>
<dl>
<dd>invalid command syntax</dl>
<p> <i>2</i></p>
<dl>
<dd>one or more bad password entries</dl>
<p> <i>3</i></p>
<dl>
<dd>can&#8217;t open password files</dl>
<p> <i>4</i></p>
<dl>
<dd>can&#8217;t lock password files</dl>
<p> <i>5</i></p>
<dl>
<dd>can&#8217;t update password files</dl>
<p> <i>6</i></p>
<dl>
<dd>can&#8217;t sort password files</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/8-grpck/">grpck</a></code>(8), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
