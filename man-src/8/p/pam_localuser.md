---
title: "pam_localuser(8)"
name: "pam_localuser"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_localuser/"
description: "pam_localuser – require users to be listed in /etc/passwd"
---

<p>pam_localuser &#8211; require users to be listed in /etc/passwd</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_localuser.so</code> [debug] [file=<i>/path/passwd</i>]</dl>
<h2>Description</h2>
<dd>pam_localuser is a PAM module to help implementing site-wide login policies, where they typically include a subset of the network&#8217;s users and a few accounts that are local to a particular workstation. Using pam_localuser and pam_wheel or pam_listfile is an effective way to restrict access to either local users and/or a subset of the network&#8217;s users. </p>
<p> This could also be implemented using pam_listfile.so and a very short awk script invoked by cron, but it&#8217;s common enough to have been separated out.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>file=</code><i>/path/passwd</i></p>
<dl>
<dd>Use a file other than /etc/passwd.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The new localuser was set successfully.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>The conversation method supplied by the application failed to obtain the username.</dl>
<p> PAM_INCOMPLETE</p>
<dl>
<dd>The conversation method supplied by the application returned PAM_CONV_AGAIN.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>The user name is not valid or the passwd file is unavailable.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>The user is not listed in the passwd file.</dl>
<h2>Examples</h2>
<p>Add the following lines to /etc/pam.d/su to allow only local users or group wheel to use su.</p>
<dl>
<dd>
<pre>account sufficient pam_localuser.so
account required pam_wheel.so</pre>
</dl>
<h2>Files</h2>
<p>/etc/passwd</p>
<dl>
<dd>Local user account information.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_localuser was written by Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;.</p>
