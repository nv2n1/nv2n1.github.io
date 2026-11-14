---
title: "pam_matrix(8)"
name: "pam_matrix"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_matrix/"
description: "pam_matrix – A PAM test module to retrieve module-specific PAM items"
---

<p>pam_matrix &#8211; A PAM test module to retrieve module-specific PAM items</p>
<h2>Synopsis</h2>
<p>pam_matrix.so [&#8230;]</p>
<h2>Description</h2>
<p>Testing PAM application often requires to set up an authentication backend with as little effort as possible. The <code>pam_matrix</code> module allows to authenticate against a key-value text file, provided by an option or with an environment variable.</p>
<h2>Important</h2>
<p>pam_matrix is a <code>test tool</code>. It should be considered completely insecure and never used outside test environments! As you&#8217;ll see when reading description of the options and actions, many of them don&#8217;t make any sense in the real world and were added just to make tests possible.</p>
<h2>Password Database</h2>
<p>The pam_matrix module authenticates user against a plain-text CSV file. The format of the file is as follows: </p>
<dl>
<dd>
<pre>username:password:allowed_service</pre>
</dl>
<p> Example: User bob allowed to authenticate with the service sshd </p>
<dl>
<dd>
<pre>bob:secret:sshd</pre>
</dl>
<h2>Options</h2>
<dl>
<dd>&bull; <code>passdb=/path/to/file</code> &#8211; the patch to the password database. If the database is not provided with this module option, pam_matrix.so reads the PAM_MATRIX_PASSWD environment variable and tries to load the file from there. If that fails as well, PAM_AUTHINFO_UNAVAIL is returned.</dl>
<dl>
<dd>&bull; <code>echo</code> &#8211; if this option is provided, pam_matrix.so will ask for password using PAM_PROMPT_ECHO_ON, that is, the password will be echoed back to user. This option was added to make it possible to test conversation functions better.</dl>
<dl>
<dd>&bull; <code>verbose</code> &#8211; if this option is provided, pam_matrix.so will display a PAM_TEXT_INFO message when authentication succeeds and a PAM_ERROR_MSG when authentication fails. This option was added to make it possible to test conversation functions better.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are supported. </p>
<p> The <code>auth</code> module searches for the user in the passdb file and compares the provided password with the one in the passdb file. </p>
<p> The <code>password</code> module is able to update the password in the passdb file. </p>
<p> The <code>access</code> module compares the service name the PAM conversation was invoked with the allowed service for the user as set in the passdb file. </p>
<p> The <code>session</code> module sets the HOMEDIR PAM environment variable to &quot;/home/%u&quot; where %u stands for the user who opens the session. The variable is unset on session close.</p>
<h2>Example</h2>
<dl>
<dd>
<pre>auth required pam_matrix.so passdb=/tmp/passdb verbose
account required pam_matrix.so passdb=/tmp/passdb verbose
password required pam_matrix.so passdb=/tmp/passdb verbose
session required pam_matrix.so passdb=/tmp/passdb verbose</pre>
</dl>
