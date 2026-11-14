---
title: "pam_extrausers(8)"
name: "pam_extrausers"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_extrausers/"
description: "pam_extrausers – Module for libnss-extrausers authentication"
---

<p>pam_extrausers &#8211; Module for libnss-extrausers authentication</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_extrausers.so</code> [&#8230;]</dl>
<h2>Description</h2>
<dd>This is similar to the standard Unix authentication module pam_unix. But instead of using /etc/passwd and /etc/shadow, it uses /var/lib/extrausers/passwd and /var/lib/extrausers/shadow. </p>
<p> The account component performs the task of establishing the status of the user&#8217;s account and password based on the following <i>shadow</i> elements: expire, last_change, max_change, min_change, warn_change. In the case of the latter, it may offer advice to the user on changing their password or, through the <code>PAM_AUTHTOKEN_REQD</code> return, delay giving service to the user until they have established a new password. The entries listed above are documented in the <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5) manual page. Should the user&#8217;s record not contain one or more of these entries, the corresponding <i>shadow</i> check is not performed. </p>
<p> The authentication component performs the task of checking the users credentials (password). The default action of this module is to not permit the user access to a service if their official password is blank. </p>
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
<p> <code>nullok</code></p>
<dl>
<dd>The default action of this module is to not permit the user access to a service if their official password is blank. The <code>nullok</code> argument overrides this default and allows any user with a blank password to access the service.</dl>
<p> <code>nullok_secure</code></p>
<dl>
<dd>The default action of this module is to not permit the user access to a service if their official password is blank. The <code>nullok_secure</code> argument overrides this default and allows any user with a blank password to access the service as long as the value of PAM_TTY is set to one of the values found in /etc/securetty.</dl>
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
<p> <code>not_set_pass</code></p>
<dl>
<dd>This argument is used to inform the module that it is not to pay attention to/make available the old or new passwords from/to other (stacked) password modules.</dl>
<p> <code>nis</code></p>
<dl>
<dd>NIS RPC is used for setting new passwords.</dl>
<p> <code>remember=</code><i>n</i></p>
<dl>
<dd>The last <i>n</i> passwords for each user are saved in /etc/security/opasswd in order to force password change history and keep the user from alternating between the same password too frequently. Instead of this option the <code>pam_pwhistory</code> module should be used.</dl>
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
<dd>When a user changes their password next, encrypt it with the SHA256 algorithm. If the SHA256 algorithm is not known to the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function, fall back to MD5.</dl>
<p> <code>sha512</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the SHA512 algorithm. If the SHA512 algorithm is not known to the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function, fall back to MD5.</dl>
<p> <code>blowfish</code></p>
<dl>
<dd>When a user changes their password next, encrypt it with the blowfish algorithm. If the blowfish algorithm is not known to the <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) function, fall back to MD5.</dl>
<p> <code>rounds=</code><i>n</i></p>
<dl>
<dd>Set the optional number of rounds of the SHA256, SHA512 and blowfish password hashing algorithms to <i>n</i>.</dl>
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
<p> Invalid arguments are logged with <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_IGNORE</p>
<dl>
<dd>Ignore this module.</dl>
<h2>Examples</h2>
<p>An example usage for /etc/pam.d/common-password would be: </p>
<pre><code>password[success = 2 default = ignore] pam_extrausers.so obscure sha512
    password[success = 1 default = ignore] pam_unix.so obscure sha512
#here's the fallback if no module succeeds
        password requisite pam_deny.so
#prime the stack with a positive return value if there isn't one already;
#this avoids us returning an error just because nothing sets a success code
#since the modules above will each just jump around
            password required pam_permit.so
#and here are more per - package modules(the &quot;Additional&quot; block)
                password optional pam_gnome_keyring.so
                    password optional pam_ecryptfs.so
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_extrausers was written by various people.</p>
