---
title: "msmtp(1)"
name: "msmtp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msmtp/"
description: "msmtp – An SMTP client"
---

<h2>NAME</h2>
<p> msmtp &#8211; An SMTP client</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>Sendmail mode (default):</p>
<dd> <code>msmtp</code> [option&#8230;] [&#8211;] recipient&#8230;<br />
 <code>msmtp</code> [option&#8230;] -t [&#8211;] [recipient&#8230;]</p>
<dt>Server information mode:</p>
<dd> <code>msmtp</code> [option&#8230;] &#8211;serverinfo</p>
<dt>Remote Message Queue Starting mode:</p>
<dd> <code>msmtp</code> [option&#8230;] &#8211;rmqs=<i>host</i>|<i>@domain</i>|<i>#queue</i></dl>
<h2>DESCRIPTION</h2>
<p> In the default sendmail mode, msmtp reads a mail from standard input and sends it to an SMTP server for delivery.<br />
 In server information mode, msmtp prints information about an SMTP server.<br />
 In Remote Message Queue Starting mode, msmtp sends a Remote Message Queue Starting request for a host, domain, or queue to an SMTP server.</p>
<h2>EXIT STATUS</h2>
<p> The standard sendmail exit status codes are used, as defined in sysexits.h.</p>
<h2>OPTIONS</h2>
<p> Options override configuration file settings.<br />
 They are compatible with sendmail where appropriate.</p>
<dl>
<dt><code>General options</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;version</p>
<dd> Print version information. This includes information about the library used for TLS/SSL support (if any), the library used for authentication, the authentication mechanisms supported by this library, and the default locations of the system and user configuration files.</p>
<dt>&#8211;help</p>
<dd> Print help.</p>
<dt>-P, &#8211;pretend</p>
<dd> Print the configuration settings that would be used, but do not take further action. An asterisk (`*&#8217;) will be printed instead of your password.</p>
<dt>-v, -d, &#8211;debug</p>
<dd> Print lots of debugging information, including the whole conversation with the SMTP server. Be careful with this option: the (potentially dangerous) output will not be sanitized, and your password may get printed in an easily decodable format!</dl>
</dl>
<dt><code>Changing the mode of operation</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>-S, &#8211;serverinfo</p>
<dd> Print information about the SMTP server and exit. This includes information about supported features (mail size limit, authentication, TLS, DSN, &#8230;) and about the TLS certificate (if TLS is active).</p>
<dt>&#8211;rmqs=(<i>host</i>|<i>@domain</i>|<i>#queue</i>)</p>
<dd> Send a Remote Message Queue Starting request for the given host, domain, or queue to the SMTP server and exit.</dl>
</dl>
<dt><code>Configuration options</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>-C, &#8211;file=<i>filename</i></p>
<dd> Use the given file instead of ~/.msmtprc as the user configuration file.</p>
<dt>-a, &#8211;account=<i>account_name</i></p>
<dd> Use the given account instead of the account named &quot;default&quot;. The settings of this account may be changed with command line options. This option cannot be used together with the <code>&#8211;host</code> option.</p>
<dt>&#8211;host=<i>hostname</i></p>
<dd> Use this SMTP server with settings from the command line; do not use any configuration file data. This option cannot be used together with the <code>&#8211;account</code> option.</p>
<dt>&#8211;port=<i>number</i></p>
<dd> Set the port number to connect to. See the <code>port</code> command below.</p>
<dt>&#8211;timeout=(<i>off</i>|<i>seconds</i>)</p>
<dd> Set a network timeout. See the <code>timeout</code> command below. For compatibility with older versions, &#8211;connect-timeout is accepted as an alias for this option.</p>
<dt>&#8211;protocol=(<i>smtp</i>|<i>lmtp</i>)</p>
<dd> Set the protocol to use. See the <code>protocol</code> command below.</p>
<dt>&#8211;auth[=(<i>on</i>|<i>off</i>|<i>method</i>)]</p>
<dd> Enable or disable authentication. You can optionally choose the method. See the <code>auth</code> command below.</p>
<dt>&#8211;user=<i>[username]</i></p>
<dd> Set or unset the user name for authentication. See the <code>user</code> command below.</p>
<dt>&#8211;passwordeval=[<i>eval</i>]</p>
<dd> Set your password for SMTP authentication to the output (stdout) of the execution of <i>eval</i>.</p>
<dt>&#8211;tls[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable TLS/SSL encryption. See the <code>tls</code> command below.</p>
<dt>&#8211;tls-starttls[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable STARTTLS for TLS encryption. See the <code>tls_starttls</code> command below.</p>
<dt>&#8211;tls-trust-file=[<i>file</i>]</p>
<dd> Set or unset a trust file for TLS encryption. See the <code>tls_trust_file</code> command below.</p>
<dt>&#8211;tls-crl-file=[<i>file</i>]</p>
<dd> Set or unset a certificate revocation list (CRL) file for TLS. See the <code>tls_crl_file</code> command below.</p>
<dt>&#8211;tls-fingerprint=[<i>fingerprint</i>]</p>
<dd> Set ot unset the fingerprint of a trusted TLS certificate. See the <code>tls_fingerprint</code> command below.</p>
<dt>&#8211;tls-key-file=[<i>file</i>]</p>
<dd> Set or unset a key file for TLS encryption. See the <code>tls_key_file</code> command below.</p>
<dt>&#8211;tls-cert-file=[<i>file</i>]</p>
<dd> Set or unset a cert file for TLS encryption. See the <code>tls_cert_file</code> command below.</p>
<dt>&#8211;tls-certcheck[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable server certificate checks for TLS encryption. See the <code>tls_certcheck</code> command below.</p>
<dt>&#8211;tls-force-sslv3[=(<i>on</i>|<i>off</i>)]</p>
<dd> Force TLS/SSL version SSLv3. See the <code>tls_force_sslv3</code> command below.</p>
<dt>&#8211;tls-min-dh-prime-bits=[<i>bits</i>]</p>
<dd> Set or unset minimum bit size of the Diffie-Hellman (DH) prime. See the <code>tls_min_dh_prime_bits</code> command below.</p>
<dt>&#8211;tls-priorities=[<i>priorities</i>]</p>
<dd> Set or unset TLS priorities. See the <code>tls_priorities</code> command below.</p>
<dt>&#8211;domain=[<i>string</i>]</p>
<dd> Set the argument of the SMTP EHLO (or LMTP LHLO) command. See the <code>domain</code> command below.</dl>
</dl>
<dt><code>Options specific to sendmail mode</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;auto-from[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable automatic envelope-from addresses. The default is off. See the <code>auto_from</code> command below.</p>
<dt>-f, &#8211;from=<i>address</p>
<dd> Set the envelope-from address. It is only used when auto_from</i> is off.<br />
 If no account was chosen yet (with <code>&#8211;account</code> or <code>&#8211;host</code>), this option will choose the first account that has the given envelope-from address (set with the <code>from</code> command). If no such account is found, &quot;default&quot; is used.</p>
<dt>&#8211;maildomain=[<i>domain</i>]</p>
<dd> Set the domain part for generated envelope-from addresses. It is only used when <i>auto_from</i> is on. See the <code>maildomain</code> command below.</p>
<dt>-N, &#8211;dsn-notify=(<i>off</i>|<i>cond</i>)</p>
<dd> Set or unset DSN notification conditions. See the <code>dsn_notify</code> command below.</p>
<dt>-R, &#8211;dsn-return=(<i>off</i>|<i>ret</i>)</p>
<dd> Set or unset the DSN notification amount. See the <code>dsn_return</code> command below. Note that <i>hdrs</i> is accepted as an alias for <i>headers</i> to be compatible with sendmail.</p>
<dt>&#8211;keepbcc[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable the preservation of the Bcc header. See the <code>keepbcc</code> command below.</p>
<dt>-X, &#8211;logfile=[<i>file</i>]</p>
<dd> Set or unset the log file. See the <code>logfile</code> command below.</p>
<dt>&#8211;syslog[=(<i>on</i>|<i>off</i>|<i>facility</i>)]</p>
<dd> Enable or disable syslog logging. See the <code>syslog</code> command below.</p>
<dt>-t, &#8211;read-recipients</p>
<dd> Read recipient addresses from the To, Cc, and Bcc headers of the mail in addition to the recipients given on the command line. If any Resent- headers are present, then the addresses from any Resent-To, Resent-Cc, and Resent-Bcc headers in the first block of Resent- headers are used instead.</p>
<dt>&#8211;read-envelope-from</p>
<dd> Read the envelope from address from the From header of the mail. Currently this header must be on a single line for this option to work correctly.</p>
<dt>&#8211;aliases=[<i>file</i>]</p>
<dd> Set or unset an aliases file. See the <code>aliases</code> command below.</p>
<dt>&#8212;</p>
<dd> This marks the end of options. All following arguments will be treated as recipient addresses, even if they start with a `-&#8216;.</dl>
</dl>
</dl>
<p> The following options are accepted but ignored for sendmail compatibility:<br />
 -B<i>type</i>, -bm, -F<i>name</i>, -G, -h<i>N</i>, -i, -L <i>tag</i>, -m, -n, -O <i>option=value</i>, -o<i>x</i> <i>value</i></p>
<h2>USAGE</h2>
<p> Normally, a system wide configuration file and/or a user configuration file contain information about which SMTP server to use (and how to use it), but almost all settings can also be configured on the command line. </p>
<p> Information about SMTP servers is organized in <i>accounts</i>. Each account describes one SMTP server: host name, authentication settings, TLS settings, and so on. Each configuration file can define multiple accounts. </p>
<p> In sendmail mode, an envelope-from address is necessary to send mail. This is the mail address that will be presented to the SMTP server as the originator of the mail. Envelope-from addresses can be generated automatically (when <i>auto_from</i> is enabled) or set explicitly with the <code>from</code> command or <code>&#8211;from</code> option. When <i>auto_from</i> is enabled, an envelope-from address of the form user [at] domain will be generated. The local part will be set to <code>USER</code> or, if that fails, to <code>LOGNAME</code> or, if that fails, to the login name of the current user. The domain part can be set with the <code>maildomain</code> command. If the maildomain is empty, the envelope-from address will only consist of the user name and not have a domain part. </p>
<p> The user can choose which account to use in one of three ways:</p>
<dl>
<dt>&#8211;account=<i>id</i></p>
<dd> Use the given account. Command line settings override configuration file settings.</p>
<dt>&#8211;host=<i>hostname</i></p>
<dd> Use only the settings from the command line; do not use any configuration file data.</p>
<dt>&#8211;from=<i>address</i> or &#8211;read-envelope-from</p>
<dd> Choose the first account from the system or user configuration file that has a matching envelope-from address as specified by a <code>from</code> command. This works only when neither <code>&#8211;account</code> nor <code>&#8211;host</code> is used.</dl>
<p> If none of the above options is used (or if no account has a matching <code>from</code> command), then the account &quot;default&quot; is used. </p>
<p> Skip to the EXAMPLES section for a quick start.</p>
<h2>CONFIGURATION FILES</h2>
<p> If it exists and is readable, a system wide configuration file SYSCONFDIR/msmtprc will be loaded, where SYSCONFDIR depends on your platform. Use <code>&#8211;version</code> to find out which directory is used.<br />
 If it exists and is readable, a user configuration file will be loaded (~/.msmtprc by default). Accounts defined in the user configuration file override accounts from the system configuration file. The user configuration file must have no more permissions than user read/write. Configuration data from either file can be changed by command line options. </p>
<p> A configuration file is a simple text file. Empty lines and comment lines (whose first non-blank character is `#&#8217;) are ignored.<br />
 Every other line must contain a command and may contain an argument to that command.<br />
 The argument may be enclosed in double quotes (&quot;), for example if its first or last character is a blank.<br />
 If the first character of a filename is the tilde (~), this tilde will be replaced by HOME. If a command accepts the argument <i>on</i>, it also accepts an empty argument and treats that as if it was <i>on</i>.<br />
 Commands form groups. Each group begins with the <code>account</code> command and defines the settings for one SMTP server. </p>
<p> Skip to the EXAMPLES section for a quick start. </p>
<p> Commands are as follows:</p>
<dl>
<dt>defaults</p>
<dd> Set defaults. The following configuration commands will set default values for all following account definitions in the current configuration file.</p>
<dt>account <i>name</i> [:<i>account</i>[,&#8230;]]</p>
<dd> Start a new account definition with the given name. The current default values are filled in.<br />
 If a colon and a list of previously defined accounts is given after the account name, the new account, with the filled in default values, will inherit all settings from the accounts in the list.</p>
<dt>host <i>hostname</i></p>
<dd> The SMTP server to send the mail to. The argument may be a host name or a network address. Every account definition must contain this command.</p>
<dt>port <i>number</i></p>
<dd> The port that the SMTP server listens on. The default port will be acquired from your operating system&#8217;s service database: for SMTP, the service is &quot;smtp&quot; (default port 25), unless TLS without STARTTLS is used, in which case it is &quot;smtps&quot; (465). For LMTP, it is &quot;lmtp&quot;.</p>
<dt>timeout (<i>off</i>|<i>seconds</i>)</p>
<dd> Set or unset a network timeout, in seconds. The argument <i>off</i> means that no timeout will be set, which means that the operating system default will be used.<br />
 For compatibility with older versions, <code>connect_timeout</code> is accepted as an alias for this command.</p>
<dt>protocol (<i>smtp</i>|<i>lmtp</i>)</p>
<dd> Set the protocol to use. Currently only SMTP and LMTP are supported. SMTP is the default. See the <code>port</code> command above for default ports.</p>
<dt>auto_from [(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable automatic envelope-from addresses. The default is off. When enabled, an envelope-from address of the form user [at] domain will be generated. The local part will be set to <code>USER</code> or, if that fails, to <code>LOGNAME</code> or, if that fails, to the login name of the current user. The domain part can be set with the <code>maildomain</code> command. If the maildomain is empty, the envelope-from address will only consist of the user name and not have a domain part. When auto_from is disabled, the envelope-from address must be set explicitly.</p>
<dt>from <i>envelope_from</i></p>
<dd> Set the envelope-from address. This address will only be used when <i>auto_from</i> is off.</p>
<dt>maildomain [<i>domain</i>]</p>
<dd> Set a domain part for the generation of an envelope-from address. This is only used when <i>auto_from</i> is on. The domain may be empty.</p>
<dt>auth [(<i>on</i>|<i>off</i>|<i>method</i>)]</p>
<dd> This command enables or disables SMTP authentication. You should not need to set the method yourself; with the argument <i>on</i>, msmtp will choose the best one available for you (see below).<br />
 You probably need to set a username (with <code>user</code>) and password (with <code>password</code>). If no password is set but one is needed during authentication, msmtp will try to find it in ~/.netrc. If that fails, it will try to find it in SYSCONFDIR/netrc (use <code>&#8211;version</code> to find out what SYSCONFDIR is on your platform). If that fails, it will try to get it from a system specific keyring (if available). If that fails but a controlling terminal is available, msmtp will prompt you for it.<br />
 Currently supported keyrings are the Gnome Keyring and the Mac OS X Keychain. The script <code>msmtp-gnome-tool.py</code> can be used to manage Gnome Keyring passwords for msmtp. To manage Mac OS X Keychain passwords, use the Keychain Access GUI application. The <i>account name</i> is same as the msmtp <code>user</code> argument. The <i>keychain item name</i> is <code>smtp://&lt;hostname&gt;</code> where <code>&lt;hostname&gt;</code> matches the msmtp <code>host</code> argument.<br />
 Available authentication methods are <i>plain</i>, <i>scram-sha-1</i>, <i>cram-md5</i>, <i>gssapi</i>, <i>external</i>, <i>digest-md5</i>, <i>login</i>, and <i>ntlm</i>. Note that one or more of these methods may be unavailable due to lack of support in the underlying authentication library. Use the <code>&#8211;version</code> option to find out which methods are supported.<br />
 The <i>plain</i> and <i>login</i> methods send your authentication data in cleartext over the net, and the <i>ntlm</i> method may be vulnerable to attacks. These methods should therefore only be used together with the <code>tls</code> command.<br />
 If you don&#8217;t choose the method yourself, msmtp chooses the best secure method that the SMTP server supports. Secure means that your authentication data will not be sent in cleartext (or in an easily decryptable form) over the net. For TLS encrypted connections, every authentication method is secure in this sense. If TLS is not active, only gssapi, scram-sha-1, and cram-md5 are secure in this sense.<br />
 The <i>external</i> is special: the actual authentication happens outside of the SMTP protocol, typically by sending a TLS client certificate (see the <code>tls_cert_file</code> command). The <i>external</i> method merely confirms that this authentication succeeded for the given user (or, if no user name is given, confirms that authentication succeeded). This authentication method is not chosen automatically; you have to request it manually.</p>
<dt>user [<i>username</i>]</p>
<dd> Set your user name for SMTP authentication. An empty argument unsets the user name. Authentication must be activated with the <code>auth</code> command.</p>
<dt>password [<i>secret</i>]</p>
<dd> Set your password for SMTP authentication. An empty argument unsets the password. Authentication must be activated with the <code>auth</code> command. If no password is set but one is needed during authentication, msmtp will try to find it. First, if <code>passwordeval</code> is set, it will evaluate that command. If <code>passwordeval</code> is not set, msmtp will try to find the password in ~/.netrc. If that fails, it will try to find it in SYSCONFDIR/netrc (use <code>&#8211;version</code> to find out what SYSCONFDIR is on your platform). If that fails, it will try to get it from a system specific keychain (if available). If that fails but a controlling terminal is available, msmtp will prompt you for it.</p>
<dt>passwordeval [<i>eval</i>]</p>
<dd> Set your password for SMTP authentication to the output (stdout) of the execution of <i>eval</i>.</p>
<dt>ntlmdomain [<i>domain</i>]</p>
<dd> Set a domain for the <i>ntlm</i> authentication method. The default is to use no domain (equivalent to an empty argument), but some servers seem to require one, even if it is an arbitrary string.</p>
<dt>tls [(<i>on</i>|<i>off</i>)]</p>
<dd> This command enables or disables TLS (also known as SSL) encrypted connections to the SMTP server. Not every server supports TLS.<br />
 With TLS/SSL, the connection with the SMTP server will be protected against eavesdroppers and man-in-the-middle attacks. To use TLS/SSL, it is required to either use the <code>tls_trust_file</code> command (highly recommended) or to disable <code>tls_certcheck</code>.</p>
<dt>tls_starttls [(<i>on</i>|<i>off</i>)]</p>
<dd> By default, TLS encryption is activated using the STARTTLS SMTP command. By disabling this, TLS encryption is immediately started instead (this is known as SMTP tunneled through TLS/SSL). The default port is set to 465 for this mode of operation.<br />
 For compatibility with older versions, <code>tls_nostarttls</code> is accepted as an alias for <code>tls_starttls off</code>.</p>
<dt>tls_trust_file [<i>file</i>]</p>
<dd> This command activates strict server certificate verification.<br />
 The filename must be the absolute path name of a file in PEM format containing one or more certificates of trusted Certification Authorities (CAs).<br />
 On Debian based systems, you can install the <code>ca-certificates</code> package and use the file <code>/etc/ssl/certs/ca-certificates.crt</code>.</p>
<dt>tls_crl_file [<i>file</i>]</p>
<dd> This command sets or unsets a certificate revocation list (CRL) file for TLS, to be used during strict server certificate verification as enabled by the <code>tls_trust_file</code> command. This allows the verification procedure to detect revoked certificates.</p>
<dt>tls_fingerprint [<i>fingerprint</i>]</p>
<dd> This command sets or unsets the fingerprint of a particular TLS certificate. This certificate will then be trusted, regardless of its contents. This can be used to trust broken certificates (e.g. with a non-matching hostname) or in situations where <code>tls_trust_file</code> cannot be used for some reason.<br />
 You can give either an SHA1 (recommended) or an MD5 fingerprint in the format 01:23:45:67:&#8230;<br />
 You can use <code>&#8211;serverinfo &#8211;tls &#8211;tls-certcheck=off</code> to get the peer certificate&#8217;s fingerprints.</p>
<dt>tls_key_file [<i>file</i>]</p>
<dd> This command (together with the <code>tls_cert_file</code> command) enables msmtp to send a client certificate to the SMTP server if requested. The file must contain the private key of a certificate in PEM format. An empty argument disables this feature.</p>
<dt>tls_cert_file [<i>file</i>]</p>
<dd> This command (together with the <code>tls_key_file</code> command) enables msmtp to send a client certificate to the SMTP server if requested. The file must contain a certificate in PEM format. An empty argument disables this feature.</p>
<dt>tls_certcheck [(<i>on</i>|<i>off</i>)]</p>
<dd> This command enables or disables checks for the server certificate.<br />
 <code>WARNING</code>: When the checks are disabled, TLS/SSL sessions will be vulnerable to man-in-the-middle attacks!<br />
 For compatibility with older versions, <code>tls_nocertcheck</code> is accepted as an alias for <code>tls_certcheck off</code>.</p>
<dt>tls_force_sslv3 [(<i>on</i>|<i>off</i>)]</p>
<dd> Force TLS/SSL version SSLv3. This might be needed to use SSL with some old and broken servers. Do not use this unless you have to.</p>
<dt>tls_min_dh_prime_bits [<i>bits</i>]</p>
<dd> Set or unset the minimum number of Diffie-Hellman (DH) prime bits that msmtp will accept for TLS sessions. The default is set by the TLS library and can be selected by using an empty argument to this command. Only lower the default (for example to 512 bits) if there is no other way to make TLS work with the remote server.</p>
<dt>tls_priorities [<i>priorities</i>]</p>
<dd> Set the priorities for TLS sessions. The default is set by the TLS library and can be selected by using an empty argument to this command. Currently this command only works with sufficiently recent GnuTLS releases. See the GnuTLS documentation of the <code>gnutls_priority_init</code> function for a description of the <i>priorities</i> string.</p>
<dt>dsn_notify (<i>off</i>|<i>condition</i>)</p>
<dd> This command sets the condition(s) under which the mail system should send DSN (Delivery Status Notification) messages. The argument <i>off</i> disables explicit DSN requests, which means the mail system decides when to send DSN messages. This is the default. The <i>condition</i> must be <i>never</i>, to never request notification, or a comma separated list (no spaces!) of one or more of the following: <i>failure</i>, to request notification on transmission failure, <i>delay</i>, to be notified of message delays, <i>success</i>, to be notified of successful transmission. The SMTP server must support the DSN extension.</p>
<dt>dsn_return (<i>off</i>|<i>amount</i>)</p>
<dd> This command controls how much of a mail should be returned in DSN (Delivery Status Notification) messages. The argument <i>off</i> disables explicit DSN requests, which means the mail system decides how much of a mail it returns in DSN messages. This is the default. The <i>amount</i> must be <i>headers</i>, to just return the message headers, or <i>full</i>, to return the full mail. The SMTP server must support the DSN extension.</p>
<dt>domain <i>argument</i></p>
<dd> Use this command to set the argument of the SMTP EHLO (or LMTP LHLO) command. The default is <i>localhost</i>, which is stupid but usually works. Try to change the default if mails get rejected due to anti-SPAM measures. Possible choices are the domain part of your mail address (provider.example for joe [at] provider.example) or the fully qualified domain name of your host (if available).</p>
<dt>keepbcc [(<i>on</i>|<i>off</i>)]</p>
<dd> This command controls whether to remove or keep the Bcc header when sending a mail. The default is to remove it.</p>
<dt>logfile [<i>file</i>]</p>
<dd> An empty argument disables logging (this is the default).<br />
 When logging is enabled by choosing a log file, msmtp will append one line to the log file for each mail it tries to send via the account that this log file was chosen for.<br />
 The line will include the following information: date and time, host name of the SMTP server, whether TLS was used, whether authentication was used, authentication user name (only if authentication is used), envelope-from address, recipient addresses, size of the mail as transferred to the server (only if the delivery succeeded), SMTP status code and SMTP error message (only in case of failure and only if available), error message (only in case of failure and only if available), exit code (from sysexits.h; EX_OK indicates success).<br />
 If the filename is a dash (-), msmtp prints the log line to the standard output.</p>
<dt>syslog [(<i>on</i>|<i>off</i>|<i>facility</i>)]</p>
<dd> Enable or disable syslog logging. The facility can be one of LOG_USER, LOG_MAIL, LOG_LOCAL0, &#8230;, LOG_LOCAL7. The default is LOG_USER.<br />
 Each time msmtp tries to send a mail via the account that contains this syslog command, it will log one entry to the syslog service with the chosen facility.<br />
 The line will include the following information: host name of the SMTP server, whether TLS was used, whether authentication was used, envelope-from address, recipient addresses, size of the mail as transferred to the server (only if the delivery succeeded), SMTP status code and SMTP error message (only in case of failure and only if available), error message (only in case of failure and only if available), exit code (from sysexits.h; EX_OK indicates success). </p>
<dt>aliases [<i>file</i>]</p>
<dd> Replace local recipients with addresses in the aliases file. The aliases file is a plain text file containing mappings between a local address and a list of domain addresses. A local address is defined as one without an `@&#8217; character and a domain address is one with an `@&#8217; character. The mappings are of the form: </p>
<p>&nbsp;<wbr>local: someone [at] example.com, person [at] domain.example<br />
 Multiple domain addresses are separated with commas. Comments start with `#&#8217; and continue to the end of the line.<br />
 The local address <i>default</i> has special significance and is matched if the local address is not found in the aliases file. If no <i>default</i> alias is found, then the local address is left as is.<br />
 An empty argument to the aliases command disables the replacement of local addresses. This is the default.
</dl>
<h2>EXAMPLES</h2>
<p> <code>Configuration file</code> </p>
<p> # Set default values for all following accounts.<br />
 defaults<br />
 tls on<br />
 tls_trust_file /etc/ssl/certs/ca-certificates.crt<br />
 logfile ~/.msmtp.log </p>
<p> # A freemail service<br />
 account freemail<br />
 host smtp.freemail.example<br />
 from joe_smith [at] freemail.example<br />
 auth on<br />
 user joe.smith<br />
 password secret </p>
<p> # A second mail address at the same freemail service<br />
 account freemail2 : freemail<br />
 from joey [at] freemail.example </p>
<p> # The SMTP server of the provider.<br />
 account provider<br />
 host mail.provider.example<br />
 from smithjoe [at] provider.example<br />
 auth on<br />
 user 123456789<br />
 passwordeval gpg -d ~/.msmtp.password.gpg </p>
<p> # Set a default account<br />
 account default : provider </p>
<p> <code>Using msmtp with Mutt</code> </p>
<p> Create a configuration file for msmtp and add the following lines to your Mutt configuration file:<br />
 <code>set sendmail=/path/to/msmtp</code><br />
 <code>set use_from=yes</code><br />
 <code>set realname=Your Name</code><br />
 <code>set from=you [at] example.com</code><br />
 <code>set envelope_from=yes</code><br />
 The envelope_from=yes option lets Mutt use the <code>-f</code> option of msmtp. Therefore msmtp chooses the first account that matches the from address you [at] example.com.<br />
 Alternatively, you can use the <code>-a</code> option:<br />
 <code>set sendmail=/path/to/msmtp -a my-account</code><br />
 Or set everything from the command line (but note that you cannot set a password this way):<br />
 <code>set sendmail=/path/to/msmtp &#8211;host=mailhub -f me [at] example.com &#8211;tls</code> <code>&#8211;tls-trust-file=trust.crt</code> </p>
<p> If you have multiple mail accounts in your msmtp configuration file and let Mutt use the <code>-f</code> option to choose the right one, you can easily switch accounts in Mutt with the following Mutt configuration lines:<br />
 <code>macro generic&nbsp;<wbr>&lt;esc&gt;1 :set from=you [at] example.com</code><br />
 <code>macro generic&nbsp;<wbr>&lt;esc&gt;2 :set from=you [at] your-employer.example</code><br />
 <code>macro generic&nbsp;<wbr>&lt;esc&gt;3 :set from=you [at] some-other-provider.example</code> </p>
<p> <code>Using msmtp with mail</code> </p>
<p> Define a default account, and put the following in your ~/.mailrc:<br />
 <code>set sendmail=/path/to/msmtp</code> </p>
<p> <code>Aliases file</code> </p>
<p> # Example aliases file </p>
<p> # Send root to Joe and Jane<br />
 root: joe_smith [at] example.com, jane_chang [at] example.com </p>
<p> # Send cron to Mark<br />
 cron: mark_jones [at] example.com </p>
<p> # Send everything else to admin<br />
 default: admin [at] domain.example </p>
<h2>FILES</h2>
<dl>
<dt>SYSCONFDIR/msmtprc</p>
<dd> System configuration file. Use <code>&#8211;version</code> to find out what SYSCONFDIR is on your platform.</p>
<dt>~/.msmtprc</p>
<dd> User configuration file.</p>
<dt>~/.netrc and SYSCONFDIR/netrc</p>
<dd> The netrc file contains login information. If a password is not found in the configuration file, msmtp will search it in ~/.netrc and SYSCONFDIR/netrc before prompting the user for it. The syntax of netrc files is described in <code><a href="/docs/linux/man/5-netrc/">netrc</a></code>(5) or <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1).</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>USER, LOGNAME</p>
<dd> These variables override the user&#8217;s login name when constructing an envelope-from address. LOGNAME is only used if USER is unset.</p>
<dt>TMPDIR</p>
<dd> Directory to create temporary files in. If this is unset, a system specific default directory is used.<br />
 A temporary file is only created when the <code>-t/&#8211;read-recipients</code> or <code>&#8211;read-envelope-from</code> option is used. The file is then used to buffer the headers of the mail (but not the body, so the file won&#8217;t get very large).</p>
<dt>EMAIL, SMTPSERVER</p>
<dd> These environment variables are used only if neither <code>&#8211;host</code> nor <code>&#8211;account</code> is used and there is no default account defined in the configuration files. In this case, the host name is taken from SMTPSERVER, and the envelope from address is taken from EMAIL, unless overridden by <code>&#8211;from</code> or <code>&#8211;read-envelope-from</code>. Currently SMTPSERVER must contain a plain host name (no URL), and EMAIL must contain a plain address (no names or additional information).</dl>
<h2>AUTHORS</h2>
<p> msmtp was written by Martin Lambers &lt;marlam [at] marlam.de&gt;.<br />
 Other authors are listed in the AUTHORS file in the source distribution.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/5-netrc/">netrc</a></code>(5) or <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1) </p>
<h2>Index</h2>
