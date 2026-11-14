---
title: "pam_unix(8)"
name: "pam_unix"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_unix/"
description: "pam_unix – Module for traditional password authentication"
---

<p>pam_unix &#8211; Module for traditional password authentication</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_unix.so</code> [&#8230;]</dl>
<h2>Description</h2>
<dd>This is the standard Unix authentication module. It uses standard calls from the system&#8217;s libraries to retrieve and set account information as well as authentication. Usually this is obtained from the /etc/passwd and the /etc/shadow file as well if shadow is enabled. </p>
<p> The account component performs the task of establishing the status of the user&#8217;s account and password based on the following <i>shadow</i> elements: expire, last_change, max_change, min_change, warn_change. In the case of the latter, it may offer advice to the user on changing their password or, through the <code>PAM_AUTHTOKEN_REQD</code> return, delay giving service to the user until they have established a new password. The entries listed above are documented in the <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5) manual page. Should the user&#8217;s record not contain one or more of these entries, the corresponding <i>shadow</i> check is not performed. </p>
<p> The authentication component performs the task of checking the users credentials (password). The default action of this module is to not permit the user access to a service if their official password is blank. </p>
<p> A helper binary, <code><a href="/docs/linux/man/8-unix_chkpwd/">unix_chkpwd</a></code>(8), is provided to check the user&#8217;s password when it is stored in a read protected database. This binary is very simple and will only check the password of the user invoking it. It is called transparently on behalf of the user by the authenticating component of this module. In this way it is possible for applications like <code><a href="/docs/linux/man/1-xlock/">xlock</a></code>(1) to work without being setuid-root. The module, by default, will temporarily turn off SIGCHLD handling for the duration of execution of the helper binary. This is generally the right thing to do, as many applications are not prepared to handle this signal from a child they didn&#8217;t know was <code>fork()</code>d. The <code>noreap</code> module argument can be used to suppress this temporary shielding and may be needed for use with certain applications. </p>
<p> The maximum length of a password supported by the pam_unix module via the helper binary is <i>PAM_MAX_RESP_SIZE</i> &#8211; currently 512 bytes. The rest of the password provided by the conversation function to the module will be ignored. </p>
<p> The password component of this module performs the task of updating the user&#8217;s password. The default encryption hash is taken from the <code>ENCRYPT_METHOD</code> variable from <i>/etc/login.defs</i> </p>
<p> The session component of this module logs when a user logins or leave the system. </p>
<p> Remaining arguments, supported by others functions of this module, are silently ignored. Other arguments are logged as errors through <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Turns on debugging via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>audit</code></p>
<dl>
<dd>A little more extreme than debug.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Turns off informational messages namely messages about session open and close via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>nullok</code></p>
<dl>
<dd>The default action of this module is to not permit the user access to a service if their official password is blank. The <code>nullok</code> argument overrides this default.</dl>
<p> <code>nullresetok</code></p>
<dl>
<dd>Allow users to authenticate with blank password if password reset is enforced even if <code>nullok</code> is not set. If password reset is not required and <code>nullok</code> is not set the authentication with blank password will be denied.</dl>
<p> <code>try_first_pass</code></p>
<dl>
<dd>Before prompting the user for their password, the module first tries the previous stacked module&#8217;s password in case that satisfies this module as well.</dl>
<p> <code>use_first_pass</code></p>
<dl>
<dd>The argument <code>use_first_pass</code> forces the module to use a previous stacked modules password and will never prompt the user &#8211; if no password is available or the password is not appropriate, the user will be denied access.</dl>
<p> <code>nodelay</code></p>
<dl>
<dd>This argument can be used to discourage the authentication component from requesting a delay should the authentication as a whole fail. The default action is for the module to request a delay-on-failure of the order of two second.</dl>
<p> <code>use_authtok</code></p>
<dl>
<dd>When password changing enforce the module to set the new password to the one provided by a previously stacked <code>password</code> module (this is used in the example of the stacking of the <code>pam_cracklib</code> module documented below).</dl>
<p> <code>authtok_type=</code><i>type</i></p>
<dl>
<dd>This argument can be used to modify the password prompt when changing passwords to include the type of the password. Empty by default.</dl>
<p> <code>nis</code></p>
<dl>
<dd>NIS RPC is used for setting new passwords.</dl>
<p> <code>remember=</code><i>n</i></p>
<dl>
<dd>The last <i>n</i> passwords for each user are saved in /etc/security/opasswd in order to force password change history and keep the user from alternating between the same password too frequently. The MD5 password hash algorithm is used for storing the old passwords. Instead of this option the <code>pam_pwhistory</code> module should be used.</dl>
<p> <code>shadow</code></p>
<dl>
<dd>Try to maintain a shadow based system.</dl>
<p> <code>md5</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the MD5 algorithm.</dl>
<p> <code>bigcrypt</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the DEC C2 algorithm.</dl>
<p> <code>sha256</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the SHA256 algorithm. The SHA256 algorithm must be supported by the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function.</dl>
<p> <code>sha512</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the SHA512 algorithm. The SHA512 algorithm must be supported by the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function.</dl>
<p> <code>blowfish</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the blowfish algorithm. The blowfish algorithm must be supported by the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function.</dl>
<p> <code>gost_yescrypt</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the gost-yescrypt algorithm. The gost-yescrypt algorithm must be supported by the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function.</dl>
<p> <code>yescrypt</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the yescrypt algorithm. The yescrypt algorithm must be supported by the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function.</dl>
<p> <code>rounds=</code><i>n</i></p>
<dl>
<dd>Set the optional number of rounds of the SHA256, SHA512, blowfish, gost-yescrypt, and yescrypt password hashing algorithms to <i>n</i>.</dl>
<p> <code>broken_shadow</code></p>
<dl>
<dd>Ignore errors reading shadow information for users in the account management module.</dl>
<p> <code>minlen=</code><i>n</i></p>
<dl>
<dd>Set a minimum password length of <i>n</i> characters. The default value is 6. The maximum for DES crypt-based passwords is 8 characters.</dl>
<p> <code>obscure</code></p>
<dl>
<dd>Enable some extra checks on password strength. These checks are based on the &quot;obscure&quot; checks in the original shadow package. The behavior is similar to the pam_cracklib module, but for non-dictionary-based checks. The following checks are implemented: </p>
<p> <code>Palindrome</code></p>
<dl>
<dd>Verifies that the new password is not a palindrome of (i.e., the reverse of) the previous one.</dl>
<p> <code>Case Change Only</code></p>
<dl>
<dd>Verifies that the new password isn&#8217;t the same as the old one with a change of case.</dl>
<p> <code>Similar</code></p>
<dl>
<dd>Verifies that the new password isn&#8217;t too much like the previous one.</dl>
<p> <code>Simple</code></p>
<dl>
<dd>Is the new password too simple? This is based on the length of the password and the number of different types of characters (alpha, numeric, etc.) used.</dl>
<p> <code>Rotated</code></p>
<dl>
<dd>Is the new password a rotated version of the old password? (E.g., &quot;billy&quot; and &quot;illyb&quot;)</dl>
</dl>
<p> <code>no_pass_expiry</code></p>
<dl>
<dd>When set ignore password expiration as defined by the <i>shadow</i> entry of the user. The option has an effect only in case <i>pam_unix</i> was not used for the authentication or it returned authentication failure meaning that other authentication source or method succeeded. The example can be public key authentication in <i>sshd</i>. The module will return <code>PAM_SUCCESS</code> instead of eventual <code>PAM_NEW_AUTHTOK_REQD</code> or <code>PAM_AUTHTOK_EXPIRED</code>.</dl>
<p> Invalid arguments are logged with <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_IGNORE</p>
<dl>
<dd>Ignore this module.</dl>
<h2>Examples</h2>
<p>An example usage for /etc/pam.d/login would be:</p>
<dl>
<dd>
<pre># Authenticate the user
auth required pam_unix.so
# Ensure users account and password are still active
account required pam_unix.so
# Change the user's password, but at first check the strength
# with <a href="//www.systutorials.com/docs/linux/man/8-pam_cracklib/">pam_cracklib</a>(8)
password required pam_cracklib.so retry=3 minlen=6 difok=3
password required pam_unix.so use_authtok nullok yescrypt
session required pam_unix.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_unix was written by various people.</p>
