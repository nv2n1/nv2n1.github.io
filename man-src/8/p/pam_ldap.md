---
title: "pam_ldap(8)"
name: "pam_ldap"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_ldap/"
description: "pam_ldap – PAM module for LDAP-based authentication"
---

<p>pam_ldap &#8211; PAM module for LDAP-based authentication</p>
<h2>Synopsis</h2>
<p><code>pam_ldap.so</code> [<i>&#8230;</i>]</p>
<h2>Description</h2>
<p>This is a PAM module that uses an LDAP server to verify user access rights and credentials.</p>
<h2>Options</h2>
<dl>
<dt><code>use_first_pass</code></p>
<dd>Specifies that the PAM module should use the first password provided in the authentication stack and not prompt the user for a password.</p>
<dt><code>try_first_pass</code></p>
<dd>Specifies that the PAM module should use the first password provided in the authentication stack and if that fails prompt the user for a password.</p>
<dt><code>nullok</code></p>
<dd>Specifying this option allows users to log in with a blank password. Normally logins without a password are denied.</p>
<dt><code>ignore_unknown_user</code></p>
<dd>Specifies that the PAM module should return PAM_IGNORE for users that are not present in the LDAP directory. This causes the PAM framework to ignore this module.</p>
<dt><code>ignore_authinfo_unavail</code></p>
<dd>Specifies that the PAM module should return PAM_IGNORE if it cannot contact the LDAP server. This causes the PAM framework to ignore this module.</p>
<dt><code>no_warn</code></p>
<dd>Specifies that warning messages should not be propagated to the PAM application.</p>
<dt><code>use_authtok</code></p>
<dd>This causes the PAM module to use the earlier provided password when changing the password. The module will not prompt the user for a new password (it is analogous to <code>use_first_pass</code>).</p>
<dt><code>debug</code></p>
<dd>This option causes the PAM module to log debugging information to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<dt><code>minimum_uid=</code><i>UID</i></p>
<dd>This option causes the PAM module to ignore the user if the user id is lower than the specified value. This can be used to bypass LDAP checks for system users (e.g. by setting it to 1000).</dl>
<h2>Module Services Provided</h2>
<p>All services are provided by this module but currently sessions changes are not implemented in the nslcd daemon.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/pam.conf</i></p>
<dd>the main PAM configuration file</p>
<dt><i>/etc/nslcd.conf</i></p>
<dd>The configuration file for the <code>nslcd</code> daemon (see <code><a href="/docs/linux/man/5-nslcd-conf/">nslcd.conf</a></code>(5))</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/8-nslcd/">nslcd</a></code>(8), <code><a href="/docs/linux/man/5-nslcd-conf/">nslcd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual was written by Arthur de Jong &lt;arthur [at] arthurdejong.org&gt;.</p>
