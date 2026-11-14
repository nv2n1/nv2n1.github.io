---
title: "pam_setquota(8)"
name: "pam_setquota"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_setquota/"
description: "pam_setquota – PAM module to set or modify disk quotas on session start"
---

<p>pam_setquota &#8211; PAM module to set or modify disk quotas on session start</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_setquota.so</code> [fs=<i>/home</i>] [overwrite=<i>0</i>] [debug=<i>0</i>] [startuid=<i>1000</i>] [enduid=<i>0</i>] [bsoftlimit=<i>19000</i>] [bhardlimit=<i>20000</i>] [isoftlimit=<i>3000</i>] [ihardlimit=<i>4000</i>]</dl>
<h2>Description</h2>
<dd>pam_setquota is a PAM module to set or modify a disk quota at session start </p>
<p> This makes quotas usable with central user databases, such as MySQL or LDAP.</p>
<h2>Options</h2>
<p><code>fs=</code><i>/home</i></p>
<dl>
<dd>The device file or mountpoint the policy applies to. Defaults to the filesystem containing the users home directory.</dl>
<p> <code>overwrite=</code><i>0</i></p>
<dl>
<dd>Overwrite an existing quota. Note: Enabling this will remove the ability for the admin to manually configure different quotas for users for a filesystem with <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8). (Defaults to 0)</dl>
<p> <code>debug=</code><i>0</i></p>
<dl>
<dd>Enable debugging. A value of 1 outputs the old and new quota on a device. A value of 2 also prints out the matched and found filesystems should <code>fs</code> be unset. (Defaults to 0)</dl>
<p> <code>startuid=</code><i>1000</i></p>
<dl>
<dd>Describe the start of the UID range the policy is applied to. (Defaults to UID_MIN from login.defs or the uidmin value defined at compile-time if UID_MIN is undefined)</dl>
<p> <code>enduid=</code><i>0</i></p>
<dl>
<dd>Describe the end of the UID range the policy is applied to. Setting <i>enduid=0</i> results in an open-ended UID range (i.e. all uids greater than <code>startuid</code> are included). (Defaults to 0)</dl>
<p> <code>bsoftlimit=</code><i>19000</i></p>
<dl>
<dd>Soft limit for disk quota blocks, as defined by <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2). Note: <code>bsoftlimit</code> and <code>bhardlimit</code> <i>must</i> be set at the same time!</dl>
<p> <code>bhardlimit=</code><i>20000</i></p>
<dl>
<dd>Hard limit for disk quota blocks, as defined by <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2). Note: <code>bsoftlimit</code> and <code>bhardlimit</code> <i>must</i> be set at the same time!</dl>
<p> <code>isoftlimit=</code><i>3000</i></p>
<dl>
<dd>Soft limit for inodes, as defined by <code> <a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2). Note: <code>isoftlimit</code> and <code>ihardlimit</code> <i>must</i> be set at the same time!</dl>
<p> <code>ihardlimit=</code><i>4000</i></p>
<dl>
<dd>Hard limit for inodes, as defined by <code> <a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2). Note: <code>isoftlimit</code> and <code>ihardlimit</code> <i>must</i> be set at the same time!</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The quota was set successfully.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>No action was taken because either the UID of the user was outside of the specifed range, a quota already existed and <code>overwrite=1</code> was not configured or no limits were configured at all.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The user was not found.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>/proc/mounts could not be opened. </p>
<p> The filesystem or device specified was not found. </p>
<p> The limits for the user could not be retrieved. See syslog for more information. </p>
<p> The limits for the user could not be set. See syslog for more information. </p>
<p> Either <code>isoftlimit</code>/<code>ihardlimit</code> or <code>bsoftlimit</code>/<code>bhardlimit</code> were not set at the same time.</dl>
<h2>Examples</h2>
<p>A single invocation of `pam_setquota` applies a specific policy to a UID range. Applying different policies to specific UID ranges is done by invoking pam_setquota more than once. The last matching entry defines the resulting quota.</p>
<dl>
<dd>
<pre> session required pam_setquota.so bsoftlimit=1000 bhardlimit=2000 isoftlimit=1000 ihardlimit=2000 startuid=1000 enduid=0 fs=/home
 session required pam_setquota.so bsoftlimit=19000 bhardlimit=20000 isoftlimit=3000 ihardlimit=4000 startuid=2001 enduid=3000 fs=/dev/sda1
 session required pam_setquota.so bsoftlimit=19000 bhardlimit=20000 isoftlimit=3000 ihardlimit=4000 startuid=3001 enduid=4000 fs=/dev/sda1 overwrite=1</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Author</h2>
<p>pam_setquota was originally written by Ruslan Savchenko &lt;savrus [at] mexmat.net&gt;. </p>
<p> Further modifications were made by Shane Tzen&lt;shane [at] ict.usc.edu&gt;, Sven Hartge &lt;sven [at] svenharte.de&gt; and Keller Fuchs &lt;kellerfuchs [at] hashbang.sh&gt;</p>
