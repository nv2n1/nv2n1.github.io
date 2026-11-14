---
title: "password-auth-ac(5)"
name: "password-auth-ac"
section: "5"
letter: "p"
url: "/docs/linux/man/5-password-auth-ac/"
description: "system-auth-ac, password-auth-ac, smartcard-auth-ac, fingerprint-auth-ac, postlogin-ac – Common configuration files for PAMified services written by authconfig(8)"
---

<p>system-auth-ac, password-auth-ac, smartcard-auth-ac, fingerprint-auth-ac, postlogin-ac &#8211; Common configuration files for PAMified services written by <a href="/docs/linux/man/8-authconfig/">authconfig</a>(8) </p>
<h2>Synopsis</h2>
<p><code>/etc/pam.d/system-auth-ac</code> </p>
<h2>Description</h2>
<p>The purpose of this configuration file is to provide common configuration file for all applications and service daemons calling PAM library. The <code>system-auth</code> configuration file is included from all individual service configuration files with the help of the <code>include</code> directive. When <a href="/docs/linux/man/8-authconfig/">authconfig</a>(8) writes the system PAM configuration file it replaces the default <code>system-auth</code> file with a symlink pointing to <code>system-auth-ac</code> and writes the configuration to this file. The symlink is not changed on subsequent configuration changes even if it points elsewhere. This allows system administrators to override the configuration written by authconfig. The authconfig now writes the authentication modules also into additional PAM configuration files <code>/etc/pam.d/password-auth-ac</code>, <code>/etc/pam.d/smartcard-auth-ac</code>, and <code>/etc/pam.d/fingerprint-auth-ac</code>. These configuration files contain only modules which perform authentication with the respective kinds of authentication tokens. For example <code>/etc/pam.d/smartcard-auth[-ac]</code> will not contain <code>pam_unix</code> and <code>pam_ldap</code> modules and <code>/etc/pam.d/password-auth[-ac]</code> will not contain <code>pam_pkcs11</code> and <code>pam_fprintd</code> modules. The file <code>/etc/pam.d/postlogin-ac</code> contains common services to be invoked after login. An example can be a module that encrypts an user&#8217;s filesystem or user&#8217;s keyring and is decrypted by his password. The PAM configuration files of services which are accessed by remote connections such as sshd or ftpd now include the <code>/etc/pam.d/password-auth</code> configuration file instead of <code>/etc/pam.d/system-auth</code>. </p>
<h2>Example</h2>
<p>Configure system to use pam_tally2 for configuration of maximum number of failed logins. Also call pam_access to verify if access is allowed. Make <code>system-auth</code> symlink point to system-auth-local which contains: </p>
<pre><code>auth            requisite       pam_access.so

auth            requisite       pam_tally2.so deny=3 lock_time=30 \

unlock_time=3600

auth            include         system-auth-ac

account         required        pam_tally2.so

account         include         system-auth-ac

password        include         system-auth-ac

session         include         system-auth-ac

</code></pre>
<h2>Bugs</h2>
<p>None known. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-authconfig/">authconfig</a>(8), <a href="/docs/linux/man/8-authconfig-gtk/">authconfig-gtk</a>(8), <a href="/docs/linux/man/8-pam/">pam</a>(8), <a href="/docs/linux/man/5-system-auth/">system-auth</a>(5) </p>
