---
title: "pmvarrun(8)"
name: "pmvarrun"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pmvarrun/"
description: "pmvarrun – updates /var/run/pam_mount/user"
---

<p>pmvarrun &#8211; updates /var/run/pam_mount/<i>user</i></p>
<h2>Syntax</h2>
<p><code>pmvarrun</code> <code>-u</code> <i>user</i> [<i>options</i>]</p>
<h2>Description</h2>
<p>A separate program is needed so that /var/run/pam_mount/<i>user</i> may be created with a pam_mount-specific security context (otherwise SELinux policy will conflict with gdm, which also creates file in /var/run). </p>
<p> pmvarrun is flexible and can run in a number of different security setups:</p>
<h3>root-root</h3>
<p>When pmvarrun is invoked as root, /var/run/pam_mount&#8217;s permission settings can be as strict as needed; usually (0755,root,root) is a good pick as it gives users the debug control over their refcount. Refcount files are given their respective owners (chowned to the user who logs in).</p>
<h3>user-user</h3>
<p>When invoked as the user who logs in, /var/run/pam_mount needs appropriate permissions to create a file, which means the write bit must be set. It is also highly suggested to set the sticky bit in this case, so other users do not tamper with your refcount.</p>
<h3>root-user</h3>
<p>Some programs or login helpers incorrectly call the PAM stack in a way that the login phase is done as root and the logout phase as a normal user. Nevertheless, pmvarrun supports this, and the same permissions as in root-root can be used. While the user may not be able to unlink his file from /var/run/pam_mount, it will be truncated to indicate the same state.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd>Display help.</p>
<dt><code>&#8211;user</code> <i>user</i>, <code>-u</code> <i>user</i></p>
<dd>User to handle, must be a valid username.</p>
<dt><code>&#8211;operation</code> <i>number</i>, <code>-o</code> <i>number</i></p>
<dd>Increase volume count by <i>number</i>.</p>
<dt><code>-d</code></p>
<dd>Turn on debugging.</dl>
<h2>Files</h2>
<p><code>/var/run/pam_mount/</code><i>user</i></p>
<h2>Author</h2>
<p>This manpage was originally written by Bastian Kleineidam &lt;calvin [at] debian.org&gt; for the Debian distribution of libpam-mount but may be used by others. </p>
<p> See /usr/share/doc/packages/pam_mount/AUTHORS for the list of original authors of pam_mount.</p>
