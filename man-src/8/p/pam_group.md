---
title: "pam_group(8)"
name: "pam_group"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_group/"
description: "pam_group – PAM module for group access"
---

<p>pam_group &#8211; PAM module for group access</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_group.so</code></dl>
<h2>Description</h2>
<dd>The pam_group PAM module does not authenticate the user, but instead it grants group memberships (in the credential setting phase of the authentication module) to the user. Such memberships are based on the service they are applying for. </p>
<p> By default rules for group memberships are taken from config file /etc/security/group.conf. </p>
<p> This module&#8217;s usefulness relies on the file-systems accessible to the user. The point being that once granted the membership of a group, the user may attempt to create a <code>setgid</code> binary with a restricted group ownership. Later, when the user is not given membership to this group, they can recover group membership with the precompiled binary. The reason that the file-systems that the user has access to are so significant, is the fact that when a system is mounted <i>nosuid</i> the user is unable to create or execute such a binary file. For this module to provide any level of security, all file-systems that the user has write access to should be mounted <i>nosuid</i>. </p>
<p> The pam_group module functions in parallel with the /etc/group file. If the user is granted any groups based on the behavior of this module, they are granted <i>in addition</i> to those entries /etc/group (or equivalent).</p>
<h2>Options</h2>
<p>This module does not recognise any options.</p>
<h2>Module Types Provided</h2>
<p>Only the <code>auth</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>group membership was granted.</dl>
<p> PAM_ABORT</p>
<dl>
<dd>Not all relevant data could be gotten.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CRED_ERR</p>
<dl>
<dd>Group membership was not granted.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd><code>pam_sm_authenticate</code> was called which does nothing.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The user is not known to the system.</dl>
<h2>Files</h2>
<p>/etc/security/group.conf</p>
<dl>
<dd>Default configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-group-conf/">group.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7).</p>
<h2>Authors</h2>
<p>pam_group was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
