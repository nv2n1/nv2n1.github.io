---
title: "console-perms(5)"
name: "console-perms"
section: "5"
letter: "c"
url: "/docs/linux/man/5-console-perms/"
description: "console.perms – permissions control file for users at the system console"
---

<p>console.perms &#8211; permissions control file for users at the system console</p>
<h2>Description</h2>
<p>/etc/security/console.perms and .perms files in the /etc/security/console.perms.d directory determine the permissions that will be given to priviledged users of the console at login time, and the permissions to which to revert when the users log out. They are read by the pam_console_apply helper executable. </p>
<p> The format is: </p>
<p> &lt;<code>class</code>&gt;=<code>space-separated list of words</code> </p>
<p> <code>login-regexp</code><i>|</i>&lt;<code>login-class</code>&gt; <code>perm dev-glob</code><i>|</i>&lt;<code>dev-class</code>&gt; \<br />
 <code>revert-mode revert-owner</code><i>[</i>.revert-group<i>]</i> </p>
<p> The <code>revert-mode</code>, <code>revert-owner</code>, and revert-group fields are optional, and default to <code>0600</code>, <code>root</code>, and <code>root</code>, respectively. </p>
<p> The words in a class definition are evaluated as globs if they refer to files, but as regular expressions if they apply to a console definition. Do not mix them. </p>
<p> Any line can be broken and continued on the next line by using a \ character as the last character on the line. </p>
<p> The <code>login-class</code> class and the <code>login-regexp</code> word are evaluated as regular expressions. The <code>dev-class</code> and the <code>dev-glob</code> word are evaluated as shell-style globs. If a name given corresponds to a directory, and if it is a mount point listed in <i>/etc/fstab</i>, the device node associated with the filesystem mounted at that point will be substituted in its place. </p>
<p> Classes are denoted by being contained in &lt; angle bracket &gt; characters; a lack of &lt; angle brackets &gt; indicates that the string is to be taken literally as a <code>login-regexp</code> or a <code>dev-glob</code>, depending on its input position.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_console/">pam_console</a></code>(8)<br />
 <code><a href="/docs/linux/man/8-pam_console_apply/">pam_console_apply</a></code>(8)<br />
 <code><a href="/docs/linux/man/5-console-apps/">console.apps</a></code>(5)</p>
<h2>Author</h2>
<p>Michael K. Johnson &lt;johnsonm [at] redhat.com&gt;</p>
