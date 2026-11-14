---
title: "pam_pwhistory(8)"
name: "pam_pwhistory"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_pwhistory/"
description: "pam_pwhistory – PAM module to remember last passwords"
---

<p>pam_pwhistory &#8211; PAM module to remember last passwords</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_pwhistory.so</code> [debug] [use_authtok] [enforce_for_root] [remember=<i>N</i>] [retry=<i>N</i>] [authtok_type=<i>STRING</i>]</dl>
<h2>Description</h2>
<dd>This module saves the last passwords for each user in order to force password change history and keep the user from alternating between the same password too frequently. </p>
<p> This module does not work together with kerberos. In general, it does not make much sense to use this module in conjunction with NIS or LDAP, since the old passwords are stored on the local machine and are not available on another machine for password history checking.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Turns on debugging via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>use_authtok</code></p>
<dl>
<dd>When password changing enforce the module to use the new password provided by a previously stacked <code>password</code> module (this is used in the example of the stacking of the <code>pam_cracklib</code> module documented below).</dl>
<p> <code>enforce_for_root</code></p>
<dl>
<dd>If this option is set, the check is enforced for root, too.</dl>
<p> <code>remember=</code><i>N</i></p>
<dl>
<dd>The last <i>N</i> passwords for each user are saved in /etc/security/opasswd. The default is <i>10</i>. Value of <i>0</i> makes the module to keep the existing contents of the opasswd file unchanged.</dl>
<p> <code>retry=</code><i>N</i></p>
<dl>
<dd>Prompt user at most <i>N</i> times before returning with error. The default is <i>1</i>.</dl>
<p> <code>authtok_type=</code><i>STRING</i></p>
<dl>
<dd>See <code><a href="/docs/linux/man/3-pam_get_authtok/">pam_get_authtok</a></code>(3) for more details.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>password</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTHTOK_ERR</p>
<dl>
<dd>No new password was entered, the user aborted password change or new password couldn&#8217;t be set.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>Password history was disabled.</dl>
<p> PAM_MAXTRIES</p>
<dl>
<dd>Password was rejected too often.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User is not known to system.</dl>
<h2>Examples</h2>
<p>An example password section would be:</p>
<dl>
<dd>
<pre>#%PAM-1.0
password required pam_pwhistory.so
password required pam_unix.so use_authtok</pre>
</dl>
<p> In combination with <code>pam_cracklib</code>:</p>
<dl>
<dd>
<pre>#%PAM-1.0
password required pam_cracklib.so retry=3
password required pam_pwhistory.so use_authtok
password required pam_unix.so use_authtok</pre>
</dl>
<h2>Files</h2>
<p>/etc/security/opasswd</p>
<dl>
<dd>File with password history</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7) <code><a href="/docs/linux/man/3-pam_get_authtok/">pam_get_authtok</a></code>(3)</p>
<h2>Author</h2>
<p>pam_pwhistory was written by Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;</p>
