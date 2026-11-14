---
title: "pam_sss(8)"
name: "pam_sss"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_sss/"
description: "pam_sss – PAM module for SSSD"
---

<p>pam_sss &#8211; PAM module for SSSD</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_sss.so</code> [<i>quiet</i>] [<i>forward_pass</i>] [<i>use_first_pass</i>] [<i>use_authtok</i>] [<i>retry=N</i>] [<i>ignore_unknown_user</i>] [<i>ignore_authinfo_unavail</i>] [<i>domains=X</i>] [<i>allow_missing_name</i>] [<i>prompt_always</i>]</dl>
<h2>Description</h2>
<p><code>pam_sss.so</code></p>
<dd>is the PAM interface to the System Security Services daemon (SSSD). Errors and results are logged through <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code> with the LOG_AUTHPRIV facility.</p>
<h2>Options</h2>
<p><code>quiet</code></p>
<dl>
<dd>Suppress log messages for unknown users.</dl>
<p> <code>forward_pass</code></p>
<dl>
<dd>If <code>forward_pass</code> is set the entered password is put on the stack for other PAM modules to use.</dl>
<p> <code>use_first_pass</code></p>
<dl>
<dd>The argument use_first_pass forces the module to use a previous stacked modules password and will never prompt the user &#8211; if no password is available or the password is not appropriate, the user will be denied access.</dl>
<p> <code>use_authtok</code></p>
<dl>
<dd>When password changing enforce the module to set the new password to the one provided by a previously stacked password module.</dl>
<p> <code>retry=N</code></p>
<dl>
<dd>If specified the user is asked another N times for a password if authentication fails. Default is 0. </p>
<p> Please note that this option might not work as expected if the application calling PAM handles the user dialog on its own. A typical example is <code>sshd</code> with <code>PasswordAuthentication</code>.</dl>
<p> <code>ignore_unknown_user</code></p>
<dl>
<dd>If this option is specified and the user does not exist, the PAM module will return PAM_IGNORE. This causes the PAM framework to ignore this module.</dl>
<p> <code>ignore_authinfo_unavail</code></p>
<dl>
<dd>Specifies that the PAM module should return PAM_IGNORE if it cannot contact the SSSD daemon. This causes the PAM framework to ignore this module.</dl>
<p> <code>domains</code></p>
<dl>
<dd>Allows the administrator to restrict the domains a particular PAM service is allowed to authenticate against. The format is a comma-separated list of SSSD domain names, as specified in the sssd.conf file. </p>
<p> NOTE: Must be used in conjunction with the &#8220;pam_trusted_users&#8221; and &#8220;pam_public_domains&#8221; options. Please see the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page for more information on these two PAM responder options.</dl>
<p> <code>allow_missing_name</code></p>
<dl>
<dd>The main purpose of this option is to let SSSD determine the user name based on additional information, e.g. the certificate from a Smartcard. </p>
<p> The current use case are login managers which can monitor a Smartcard reader for card events. In case a Smartcard is inserted the login manager will call a PAM stack which includes a line like </p>
<dl>
<dd>
<pre>auth sufficient pam_sss.so allow_missing_name</pre>
</dl>
<p> In this case SSSD will try to determine the user name based on the content of the Smartcard, returns it to pam_sss which will finally put it on the PAM stack.</dl>
<p> <code>prompt_always</code></p>
<dl>
<dd>Always prompt the user for credentials. With this option credentials requested by other PAM modules, typically a password, will be ignored and pam_sss will prompt for credentials again. Based on the pre-auth reply by SSSD pam_sss might prompt for a password, a Smartcard PIN or other credentials.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Files</h2>
<p>If a password reset by root fails, because the corresponding SSSD provider does not support password resets, an individual message can be displayed. This message can e.g. contain instructions about how to reset a password. </p>
<p> The message is read from the file pam_sss_pw_reset_message.LOC where LOC stands for a locale string returned by <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3). If there is no matching file the content of pam_sss_pw_reset_message.txt is displayed. Root must be the owner of the files and only root may have read and write permissions while all other users must have only read permissions. </p>
<p> These files are searched in the directory /etc/sssd/customize/DOMAIN_NAME/. If no matching file is present a generic message is displayed.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
