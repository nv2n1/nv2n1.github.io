---
title: "pam_mkhomedir(8)"
name: "pam_mkhomedir"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_mkhomedir/"
description: "pam_mkhomedir – PAM module to create users home directory"
---

<p>pam_mkhomedir &#8211; PAM module to create users home directory</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_mkhomedir.so</code> [silent] [debug] [umask=<i>mode</i>] [skel=<i>skeldir</i>]</dl>
<h2>Description</h2>
<dd>The pam_mkhomedir PAM module will create a users home directory if it does not exist when the session begins. This allows users to be present in central database (such as NIS, kerberos or LDAP) without using a distributed file system or pre-creating a large number of directories. The skeleton directory (usually /etc/skel/) is used to copy default files and also sets a umask for the creation. </p>
<p> The new users home directory will not be removed after logout of the user.</p>
<h2>Options</h2>
<p><code>silent</code></p>
<dl>
<dd>Don&#8217;t print informative messages.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Turns on debugging via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>umask=</code><i>mask</i></p>
<dl>
<dd>The user file-creation mask is set to <i>mask</i>. The default value of mask is 0022.</dl>
<p> <code>skel=</code><i>/path/to/skel/directory</i></p>
<dl>
<dd>Indicate an alternative skel directory to override the default /etc/skel.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Not enough permissions to create the new directory or read the skel directory.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known to the underlying authentication module.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Environment variables were set.</dl>
<h2>Files</h2>
<p>/etc/skel</p>
<dl>
<dd>Default skel directory</dl>
<h2>Examples</h2>
<p>A sample /etc/pam.d/login file:</p>
<dl>
<dd>
<pre> auth requisite pam_securetty.so
 auth sufficient pam_ldap.so
 auth required pam_unix.so
 auth required pam_nologin.so
 account sufficient pam_ldap.so
 account required pam_unix.so
 password required pam_unix.so
 session required pam_mkhomedir.so skel=/etc/skel/ umask=0022
 session required pam_unix.so
 session optional pam_lastlog.so
 session optional pam_mail.so standard</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7).</p>
<h2>Author</h2>
<p>pam_mkhomedir was written by Jason Gunthorpe &lt;jgg [at] debian.org&gt;.</p>
