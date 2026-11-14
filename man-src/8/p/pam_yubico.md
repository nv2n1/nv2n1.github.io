---
title: "pam_yubico(8)"
name: "pam_yubico"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_yubico/"
description: "pam_yubico – Module for YubiKey authentication"
---

<p>pam_yubico &#8211; Module for YubiKey authentication</p>
<h2>Synopsis</h2>
<p><code>pam_yubico</code> [&#8230;]</p>
<h2>Description</h2>
<p>The module is for authentication of YubiKeys, either with online validation of OTP, or offline validation with HMAC-SHA1 challenge-response.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Turns on debugging to STDOUT</dl>
<p> <code>mode=</code>[<i>client</i>|<i>challenge-response</i>]</p>
<dl>
<dd>Set the mode of operation, client for OTP validation and challenge-response for challenge-response validation, client is the default.</dl>
<p> <code>authfile</code>=<i>file</i></p>
<dl>
<dd>Set the location of the file that holds the mappings of Yubikey token IDs to user names. The format is username:first_public_id:second_public_id:&#8230; default location of the file is $HOME/.yubico/authorized_yubikeys.</dl>
<p> <code>id</code>=<i>id</i></p>
<dl>
<dd>Set to your client identity.</dl>
<p> <code>key</code>=<i>key</i></p>
<dl>
<dd>Set to your client key in base64 format. The client key is also known as API key, and provides integrity in the communication between the client (you) and the validation server. If you want to get one for use with the default YubiCloud service, please go to <a rel="nofollow" href="https://upgrade.yubico.com/getapikey/">https://upgrade.yubico.com/getapikey/</a></dl>
<p> <code>alwaysok</code></p>
<dl>
<dd>Set to enable all authentication attempts to succeed (aka presentation mode).</dl>
<p> <code>try_first_pass</code></p>
<dl>
<dd>Before prompting the user for their password, the module first tries the previous stacked module&acute;s password in case that satisfies this module as well.</dl>
<p> <code>use_first_pass</code></p>
<dl>
<dd>The argument use_first_pass forces the module to use a previous stacked modules password and will never prompt the user &#8211; if no password is available or the password is not appropriate, the user will be denied access.</dl>
<p> <code>urllist</code>=<i>list</i></p>
<dl>
<dd>List of URL templates to be used. This is set by calling ykclient_set_url_bases. The list should be in the format: <a rel="nofollow" href="https://api1.example.com/wsapi/2.0/verify;https://api2.example.com/wsapi/2.0/verify">https://api1.example.com/wsapi/2.0/verify;https://api2.example.com/wsapi/2.0/verify</a></dl>
<p> <code>url</code>=<i>url</i></p>
<dl>
<dd>This option should not be used, please use the urllist option instead. Set the URL template to use, this is set by calling ykclient_set_url_template. The URL should be set in the format <a rel="nofollow" href="https://api.example.com/wsapi/2.0/verify?id=%d">https://api.example.com/wsapi/2.0/verify?id=%d</a>&amp;otp=%s</dl>
<p> <code>capath</code>=<i>path</i></p>
<dl>
<dd>Specify the path where X509 certificates are stored. This is required if <i>https</i> or <i>ldaps</i> are used in <i>url</i> and <i>ldap_uri</i> respectively.</dl>
<p> <code>proxy</code>=<i>proxy</i></p>
<dl>
<dd>Specify a proxy to connect to the validation server. Valid schemes are socks4://, socks4a://, socks5:// or socks5h://. Socks5h asks the proxy to do the dns resolving. If no scheme or port is specified HTTP proxy port 1080 will be used. E.g. socks5h://user:pass [at] 10.10.0.1:1080</dl>
<p> <code>verbose_otp</code></p>
<dl>
<dd>This argument is used to show the OTP (One Time Password) when it is entered, i.e. to enable terminal echo of entered characters. You are advised to not use this, if you are using two factor authentication because that will display your password on the screen. This requires the service using the PAM module to display custom fields. This option can not be used with OpenSSH.</dl>
<p> <code>ldap_uri</code>=<i>uri</i></p>
<dl>
<dd>Specify the LDAP server URI (e.g. <a href="ldap://localhost">ldap://localhost</a>).</dl>
<p> <code>ldap_server</code>=<i>server</i></p>
<dl>
<dd>Specify the LDAP server host (default LDAP port is used). <code>Deprecated. Use </code><i>ldap_uri</i><code> instead.</code></dl>
<p> <code>ldapdn</code>=<i>dn</i></p>
<dl>
<dd>The dn where the users are stored (eg: ou=users,dc=domain,dc=com). If <i>ldap_filter</i> is used this is the base from which the subtree search will be performed.</dl>
<p> <code>user_attr</code>=<i>attr</i></p>
<dl>
<dd>The LDAP attribute used to store user names (eg:cn).</dl>
<p> <code>yubi_attr</code>=<i>attr</i></p>
<dl>
<dd>The LDAP attribute used to store the Yubikey id.</dl>
<p> <code>yubi_attr_prefix</code>=<i>prefix</i></p>
<dl>
<dd>The prefix of the LDAP attribute&#8217;s value, in case of a generic attribute, used to store several types of ids.</dl>
<p> <code>token_id_length</code>=<i>length</i></p>
<dl>
<dd>Length of ID prefixing the OTP (this is 12 if using the YubiCloud).</dl>
<p> <code>ldap_bind_user</code>=<i>user</i></p>
<dl>
<dd>The user to attempt a LDAP bind as.</dl>
<p> <code>ldap_bind_password</code>=<i>password</i></p>
<dl>
<dd>The password to use on LDAP bind.</dl>
<p> <code>ldap_filter</code>=<i>filter</i></p>
<dl>
<dd>An ldap filter to use for attempting to find the correct object in LDAP. In this string %u will be replaced with the username.</dl>
<p> <code>ldap_cacertfile</code>=<i>cacertfile</i></p>
<dl>
<dd>Ca certfile for the LDAP connection.</dl>
<p> <code>chalresp_path</code>=<i>path</i></p>
<dl>
<dd>Path of a system wide directory where challenge response files can be found for users. Default location is $HOME/.yubico/</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth sufficient pam_yubico.so id=16 debug</pre>
</dl>
<dl>
<dd>
<pre>auth required pam_yubico.so mode=challenge-response</pre>
</dl>
<dl>
<dd>
<pre>auth required pam_yubico.so id=16 ldap_uri=<a href="ldaps://ldap.example.com">ldaps://ldap.example.com</a> ldap_filter=(uid=%u) yubi_attr=yubiKeyId</pre>
</dl>
<h2>Files</h2>
<p><code>$HOME/.yubico/authorized_yubikeys</code></p>
<dl>
<dd>If <code>authfile</code> is not set this file is used for the mapping between YubiKey public id and in <i>client</i> mode.</dl>
<p> <code>$HOME/.yubico/challenge</code>, <code>$HOME/.yubico/challenge-</code><i>serial_number</i></p>
<dl>
<dd>If <code>chalresp_path</code> is not set these files are used to hold next challenge and expected response for the user in <i>challenge-response</i> mode. If <code>chalresp_path</code> is set the filename will be username instead of challenge.</dl>
<h2>Bugs</h2>
<p>Report yubico-pam bugs in the issue tracker: <a rel="nofollow" href="https://github.com/Yubico/yubico-pam/issues">https://github.com/Yubico/yubico-pam/issues</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ykpamcfg/">ykpamcfg</a></code>(1), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7) The yubico-pam home page: <a rel="nofollow" href="https://developers.yubico.com/yubico-pam/">https://developers.yubico.com/yubico-pam/</a> YubiKeys can be obtained from Yubico: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> </p>
