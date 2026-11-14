---
title: "mpop(1)"
name: "mpop"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpop/"
description: "mpop – A POP3 client"
---

<h2>NAME</h2>
<p> mpop &#8211; A POP3 client</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>Mail retrieval mode (default):</p>
<dd> <code>mpop</code> [option&#8230;] [&#8211;] [account&#8230;]<br />
 <code>mpop</code> &#8211;host=host [option&#8230;]</p>
<dt>Server information mode:</p>
<dd> <code>mpop</code> [option&#8230;] &#8211;serverinfo [account&#8230;]<br />
 <code>mpop</code> &#8211;host=host [option&#8230;] &#8211;serverinfo</dl>
<h2>DESCRIPTION</h2>
<p> In mail retrieval mode of operation, mpop retrieves mails from one or more POP3 mailboxes, optionally does some filtering, and delivers them through a mail delivery agent (MDA), to a maildir folder, or to an mbox file. Mails that were successfully delivered before will not be retrieved a second time, even if errors occur or mpop is terminated in the middle of a session.<br />
 In server information mode, mpop prints information about one or more POP3 servers.<br />
 If no account names are given on the command line, one named <i>default</i> will be used.<br />
 The best way to start is probably to have a look at the EXAMPLES section.</p>
<h2>EXIT STATUS</h2>
<p> The standard sendmail exit codes are used, as defined in sysexits.h.</p>
<h2>OPTIONS</h2>
<p> Options override configuration file settings, for every used account.</p>
<dl>
<dt><code>General Options</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;version</p>
<dd> Print version information, including information about the libraries used.</p>
<dt>&#8211;help</p>
<dd> Print help.</p>
<dt>-P, &#8211;pretend</p>
<dd> Print the configuration settings that would be used, but do not take further action. An asterisk (`*&#8217;) will be printed instead of your password.</p>
<dt>-d, &#8211;debug</p>
<dd> Print lots of debugging information, including the whole conversation with the server. Be careful with this option: the (potentially dangerous) output will not be sanitized, and your password may get printed in an easily decodable format!<br />
 This option implies &#8211;half-quiet, because the progress output would interfere with the debugging output.</dl>
</dl>
<dt><code>Changing the mode of operation</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>-S, &#8211;serverinfo</p>
<dd> Print information about the POP3 server(s) and exit. This includes information about supported features (pipelining, authentication methods, TOP command, &#8230;), about parameters (time for which mails will not be deleted, minimum time between logins, &#8230;), and about the TLS certificate (if TLS is active).</dl>
</dl>
<dt><code>Configuration options</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>-C, &#8211;file=<i>conffile</i></p>
<dd> Use the given file instead of ~/.mpoprc as configuration file.</p>
<dt>&#8211;host=<i>hostname</i></p>
<dd> Use this server with settings from the command line; do not use any configuration file data. This option disables loading of the configuration file. You cannot use both this option and account names on the command line.</p>
<dt>&#8211;port=<i>number</i></p>
<dd> Set the port number to connect to. See the <code>port</code> command.</p>
<dt>&#8211;timeout=(<i>off</i>|<i>seconds</i>)</p>
<dd> Set a network timeout. See the <code>timeout</code> command.</p>
<dt>&#8211;pipelining=(<i>auto</i>|<i>on</i>|<i>off)</p>
<dd> Enable or disable POP3 pipelining. See the </i><code>pipelining</code> command.</p>
<dt>&#8211;proxy-host=[<i>IP</i>|<i>hostname</i>]</p>
<dd> Set or unset a SOCKS proxy to use. See the <code>proxy_host</code> command.</p>
<dt>&#8211;proxy-port=[<i>number</i>]</p>
<dd> Set or unset a port number for the proxy host. See the <code>proxy_port</code> command.</p>
<dt>&#8211;received-header[=(<i>on</i>|<i>off)]</p>
<dd> Enable or disable the Received header. See the </i><code>received_header</code> command.</p>
<dt>&#8211;auth[=(<i>on</i>|<i>method</i>)]</p>
<dd> Set the authentication method to automatic (with &quot;on&quot;) or manually choose an authentication method. See the <code>auth</code> command.</p>
<dt>&#8211;user=[<i>username</i>]</p>
<dd> Set or unset the user name for authentication. See the <code>user</code> command.</p>
<dt>&#8211;passwordeval=[<i>eval</i>]</p>
<dd> Evaluate password for authentication. See the <code>passwordeval</code> command.</p>
<dt>&#8211;tls[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable TLS/SSL. See the <code>tls</code> command.</p>
<dt>&#8211;tls-starttls[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable STARTTLS for TLS. See the <code>tls_starttls</code> command.</p>
<dt>&#8211;tls-trust-file=[<i>file</i>]</p>
<dd> Set or unset a trust file for TLS. See the <code>tls_trust_file</code> command.</p>
<dt>&#8211;tls-crl-file=[<i>file</i>]</p>
<dd> Set or unset a certificate revocation list (CRL) file for TLS. See the <code>tls_crl_file</code> command.</p>
<dt>&#8211;tls-fingerprint=[<i>fingerprint</i>]</p>
<dd> Set ot unset the fingerprint of a trusted TLS certificate. See the <code>tls_fingerprint</code> command.</p>
<dt>&#8211;tls-key-file=[<i>file</i>]</p>
<dd> Set or unset a key file for TLS. See the <code>tls_key_file</code> command.</p>
<dt>&#8211;tls-cert-file=[<i>file</i>]</p>
<dd> Set or unset a cert file for TLS. See the <code>tls_cert_file</code> command.</p>
<dt>&#8211;tls-certcheck[=(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable server certificate checks for TLS. See the <code>tls_certcheck</code> command.</p>
<dt>&#8211;tls-min-dh-prime-bits=[<i>bits</i>]</p>
<dd> Set or unset minimum bit size of the Diffie-Hellmann (DH) prime. See the <code>tls_min_dh_prime_bits</code> command.</p>
<dt>&#8211;tls-priorities=[<i>priorities</i>]</p>
<dd> Set or unset TLS priorities. See the <code>tls_priorities</code> command.</dl>
</dl>
<dt><code>Options specific to mail retrieval mode</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>-q, &#8211;quiet</p>
<dd> Do not print status or progress information.</p>
<dt>-Q, &#8211;half-quiet</p>
<dd> Print status but not progress information.</p>
<dt>-a, &#8211;all-accounts</p>
<dd> Query all accounts in the configuration file.</p>
<dt>-A, &#8211;auth-only</p>
<dd> Authenticate only; do not retrieve mail. Useful for SMTP-after-POP.</p>
<dt>-s, &#8211;status-only</p>
<dd> Print number and size of mails in each account only; do not retrieve mail.</p>
<dt>-n, &#8211;only-new[=(<i>on</i>|<i>off</i>)]</p>
<dd> Process only new messages. See the <code>only_new</code> command.</p>
<dt>-k, &#8211;keep[=(<i>on</i>|<i>off</i>)]</p>
<dd> Do not delete mails from POP3 servers, regardless of other options or settings. See the <code>keep</code> command.</p>
<dt>&#8211;killsize=(<i>off</i>|<i>size</i>)</p>
<dd> Set or unset kill size. See the <code>killsize</code> command.</p>
<dt>&#8211;skipsize=(<i>off</i>|<i>size</i>)</p>
<dd> Set or unset skip size. See the <code>skipsize</code> command.</p>
<dt>&#8211;filter=[<i>program</i>]</p>
<dd> Set a filter which will decide whether to retrieve, skip, or delete each mail by investigating the mail&#8217;s headers. See the <code>filter</code> command.</p>
<dt>&#8211;delivery=<i>method</i>,<i>method_arguments&#8230;</i></p>
<dd> How to deliver messages received from this account. See the <code>delivery</code> command. Note that a comma is used instead of a blank to separate the method from its arguments.</p>
<dt>&#8211;uidls-file=<i>filename</i></p>
<dd> File to store UIDLs in. See the <code>uidls_file</code> command.</dl>
</dl>
</dl>
<h2>USAGE</h2>
<p> The default configuration file is ~/.mpoprc. Settings in this file can be changed by command line options.<br />
 A configuration file is a simple text file. Empty lines and comment lines (first non-blank character is &#8216;#&#8217;) are ignored. Every other line must contain a command and may contain an argument to that command. The argument may be enclosed in double quotes (&quot;).<br />
 If a file name starts with the tilde (~), this tilde will be replaced by $HOME.<br />
 If a command accepts the argument <i>on</i>, it also accepts an empty argument and treats that as if it was <i>on</i>.<br />
 Commands are organized in accounts. Each account starts with the <i>account</i> command and defines the settings for one POP3 account. </p>
<p> Commands are as follows:</p>
<dl>
<dt>defaults</p>
<dd> Set defaults. The following configuration commands will set default values for all following account definitions.</p>
<dt>account <i>name</i> [:<i>account</i>[,&#8230;]]</p>
<dd> Start a new account definition with the given name. The current default values are filled in.<br />
 If a colon and a list of previously defined accounts is given after the account name, the new account, with the filled in default values, will inherit all settings from the accounts in the list.</p>
<dt>host <i>hostname</i></p>
<dd> The POP3 server to retrieve mails from. The argument may be a host name or a network address. Every account definition must contain this command.</p>
<dt>port <i>number</i></p>
<dd> The port that the POP3 server listens on. The default is 110 (&quot;pop3&quot;), unless TLS without STARTTLS is used, in which case it is 995 (&quot;pop3s&quot;).</p>
<dt>timeout (<i>off</i>|<i>seconds</i>)</p>
<dd> Set or unset a network timeout, in seconds. The default is 180 seconds. The argument <i>off</i> means that no timeout will be set, which means that the operating system default will be used.</p>
<dt>pipelining (<i>auto</i>|<i>on</i>|<i>off</i>)</p>
<dd> Enable or disable POP3 pipelining. You should never need to change the default setting, which is <i>auto</i>: mpop enables pipelining for POP3 servers that advertise this capability, and disables it for all other servers. Pipelining can speed up a POP3 session substantially.</p>
<dt>proxy_host [<i>IP|hostname</i>]</p>
<dd> Use a SOCKS proxy. All network traffic will go through this proxy host, including DNS queries, except for a DNS query that might be necessary to resolve the proxy host name itself (this can be avoided by using an IP address as proxy host name). An empty <i>hostname</i> argument disables proxy usage. The supported SOCKS protocol version is 5. If you want to use this with Tor, see also &quot;Using mpop with Tor&quot; below.</p>
<dt>proxy_port [<i>number</i>]</p>
<dd> Set the port number for the proxy host. An empty <i>number</i> argument resets this to the default port, which is 1080 (&quot;socks&quot;).</p>
<dt>auth [(<i>on</i>|<i>method</i>)]</p>
<dd> Choose an authentication method. The default argument <i>on</i> chooses a method automatically.<br />
 Usually a user name and a password are used for authentication. The user name is specified in the configuration file with the <code>user</code> command. There are five different methods to specify the password:<br />
 1. Add the password to the system key ring. Currently supported key rings are the Gnome key ring and the Mac OS X Keychain. For the Gnome key ring, use the command secret-tool (part of Gnome&#8217;s libsecret) to store passwords: secret-tool store &#8211;label=mpop host pop.freemail.example service pop3 user joe.smith. On Mac OS X, use the Keychain Access GUI application. The account name is same as the user name. The keychain item name is pop3://&lt;hostname&gt; where &lt;hostname&gt; matches the host argument.<br />
 2. Store the password in an encrypted files, and use <code>passwordeval</code> to specify a command to decrypt that file, e.g. using GnuPG. See EXAMPLES.<br />
 3. Store the password in the configuration file using the <code>password</code> command. (Usually it is not considered a good idea to store passwords in plain text files. If you do it anyway, you must make sure that the file can only be read by yourself.)<br />
 4. Store the password in ~/.netrc. This method is probably obsolete.<br />
 5. Type the password into the terminal when it is required.<br />
 It is recommended to use method 1 or 2.<br />
 Multiple authentication methods exist. Most servers support only some of them. Historically, sophisticated methods were developed to protect passwords from being sent unencrypted to the server, but nowadays everybody needs TLS anyway, so the simple methods suffice since the whole session is protected. A suitable authentication method is chosen automatically, and when TLS is disabled for some reason, only methods that avoid sending clear text passwords are considered.<br />
 The following user / password methods are supported: <i>user</i> (a simple plain text method supported by all servers), <i>plain</i> (another simple plain text method, with base64 encoding, supported by almost all servers), <i>scram-sha-1</i> (a method that avoids clear-text passwords), <i>cram-md5</i> (an obsolete method that avoids clear-text passwords), <i>apop</i> (an obsolete method that avoids clear-text passwords, but is vulnerable to man-in-the-middle attacks), <i>digest-md5</i> (an overcomplicated obsolete method that avoids clear-text passwords, but is not considered secure anymore), <i>login</i> (a non-standard clear-text method similar to but worse than the plain method), <i>ntlm</i> (an obscure non-standard method that is now considered broken; it sometimes requires a special domain parameter passed via <code>ntlmdomain</code>).<br />
 There are currently two authentication methods that are not based on user / password information and have to be chosen manually: <i>external</i> (the authentication happens outside of the protocol, typically by sending a TLS client certificate, and the method merely confirms that this authentication succeeded), and <i>gssapi</i> (the Kerberos framework takes care of secure authentication, only a user name is required).<br />
 It depends on the underlying authentication library and its version whether a particular method is supported or not. Use <code>&#8211;version</code> to find out which methods are supported.</p>
<dt>user <i>login</i></p>
<dd> Set the user name for authentication. An empty argument unsets the user name.</p>
<dt>password <i>secret</i></p>
<dd> Set the password for authentication. An empty argument unsets the password. Consider using the <code>passwordeval</code> command or a key ring instead of this command, to avoid storing plain text passwords in the configuration file.</p>
<dt>passwordeval [<i>eval</i>]</p>
<dd> Set the password for authentication to the output (stdout) of the command <i>eval</i>. This can be used e.g. to decrypt password files on the fly or to query key rings, and thus to avoid storing plain text passwords.</p>
<dt>ntlmdomain [<i>domain</i>]</p>
<dd> Set a domain for the <code>ntlm</code> authentication method. This is obsolete.</p>
<dt>tls [(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable TLS (also known as SSL) for secured connections. You also need <code>tls_trust_file</code> or <code>tls_fingerprint</code>, and for some servers you may need to disable <code>tls_starttls</code>.<br />
 Transport Layer Security (TLS) &quot;&#8230; provides communications privacy over the Internet. The protocol allows client/server applications to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery&quot; (quote from RFC2246).<br />
 A server can use TLS in one of two modes: via a STARTTLS command (the session starts with the normal protocol initialization, and TLS is then started using the protocol&#8217;s STARTTLS command), or immediately (TLS is initialized before the normal protocol initialization; this requires a separate port). The first mode is the default, but you can switch to the second mode by disabling <code>tls_starttls</code>.<br />
 When TLS is started, the server sends a certificate to identify itself. To verify the server identity, a client program is expected to check that the certificate is formally correct and that it was issued by a Certificate Authority (CA) that the user trusts. (There can also be certificate chains with intermediate CAs.)<br />
 The list of trusted CAs is specified using the <code>tls_trust_file</code> command. Usually there is some system-wide default file available, e.g. /etc/ssl/certs/ca-certificates.crt on Debian-based systems, but you can also choose to select the trusted CAs yourself.<br />
 One practical problem with this approach is that the client program should also check if the server certificate has been revoked for some reason, using a Certificate Revocation List (CRL). A CRL file can be specified using the <code>tls_crl_file</code> command, but getting the relevant CRL files and keeping them up to date is not straightforward. You are basically on your own.<br />
 A much more serious and fundamental problem is is that you need to trust CAs. Like any other organization, a CA can be incompetent, malicious, subverted by bad people, or forced by government agencies to compromise end users without telling them. All of these things happened and continue to happen worldwide. The idea to have central organizations that have to be trusted for your communication to be secure is fundamentally broken.<br />
 Instead of putting trust in a CA, you can choose to trust only a single certificate for the server you want to connect to. For that purpose, specify the certificate fingerprint with <code>tls_fingerprint</code>. This makes sure that no man-in-the-middle can fake the identity of the server by presenting you a fraudulent certificate issued by some CA that happens to be in your trust list. However, you have to update the fingerprint whenever the server certificate changes, and you have to make sure that the change is legitimate each time, e.g. when the old certificate expired. This is inconvenient, but it&#8217;s the price to pay.<br />
 Information about a server certificate can be obtained with <i>&#8211;serverinfo &#8211;tls &#8211;tls-certcheck=off</i>. This includes the issuer CA of the certificate (so you can trust that CA via <code>tls_trust_file</code>), and the fingerprint of the certificate (so you can trust that particular certificate via <code>tls_fingerprint</code>).<br />
 TLS also allows the server to verify the identity of the client. For this purpose, the client has to present a certificate issued by a CA that the server trusts. To present that certificate, the client also needs the matching key file. You can set the certificate and key files using <code>tls_cert_file</code> and <code>tls_key_file</code>. This mechanism can also be used to authenticate users, so that traditional user / password authentication is not necessary anymore. See the <i>external</i> mechanism in <code>auth</code>.</p>
<dt>tls_starttls [(<i>on</i>|<i>off</i>)]</p>
<dd> Choose the TLS variant: start TLS from within the session (<i>on</i>, default), or tunnel the session through TLS (<i>off</i>).</p>
<dt>tls_trust_file <i>file</i></p>
<dd> Activate server certificate verification using a list of truted Certification Authorities (CAs). The file must be in PEM format. Some systems provide a system-wide default file, e.g. /etc/ssl/certs/ca-certificates.crt on Debian-based systems with the ca-certificates package. An empty argument disables this. You should also use <code>tls_crl_file</code>.</p>
<dt>tls_crl_file [<i>file</i>]</p>
<dd> Set a certificate revocation list (CRL) file for TLS, to check for revoked certificates. An empty argument disables this.</p>
<dt>tls_fingerprint [<i>fingerprint</i>]</p>
<dd> Set the fingerprint of a single certificate to accept for TLS. This certificate will be trusted regardless of its contents. The fingerprint should be of type SHA256, but can for backwards compatibility also be of type SHA1 or MD5 (please avoid this). The format should be 01:23:45:67:&#8230;. Use <i>&#8211;serverinfo &#8211;tls &#8211;tls-certcheck=off &#8211;tls-fingerprint=</i> to get the server certificate fingerprint.</p>
<dt>tls_key_file <i>file</i></p>
<dd> Send a client certificate to the server (use this together with <code>tls_cert_file}</code>). The file must contain the private key of a certificate in PEM format. An empty argument disables this feature.</p>
<dt>tls_cert_file <i>file</i></p>
<dd> Send a client certificate to the server (use this together with <code>tls_key_file</code>). The file must contain a certificate in PEM format. An empty argument disables this feature.</p>
<dt>tls_certcheck [(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable checks of the server certificate. WARNING: When the checks are disabled, TLS sessions will be vulnerable to man-in-the-middle attacks!</p>
<dt>tls_min_dh_prime_bits [<i>bits</i>]</p>
<dd> Set or unset the minimum number of Diffie-Hellman (DH) prime bits that mpop will accept for TLS sessions. The default is set by the TLS library and can be selected by using an empty argument to this command. Only lower the default (for example to 512 bits) if there is no other way to make TLS work with the remote server.</p>
<dt>tls_priorities [<i>priorities</i>]</p>
<dd> Set the priorities for TLS sessions. The default is set by the TLS library and can be selected by using an empty argument to this command. See the GnuTLS documentation of the <i>gnutls_priority_init</i> function for a description of the priorities string.</p>
<dt>delivery <i>method</i> <i>method_arguments&#8230;</i></p>
<dd> How to deliver messages received from this account.</p>
<dl>
<dt>
<dd>
<dl>
<dt>delivery mda <i>command</i></p>
<dd> Deliver the mails through a mail delivery agent (MDA).<br />
 All occurences of %F in the command will be replaced with the envelope from address of the current message (or MAILER-DAEMON if none is found). Note that this address is guaranteed to contain only letters a-z and A-Z, digits 0-9, and any of &quot;.@_-+/&quot;, even though that is only a subset of what is theoretically allowed in a mail address. Other characters, including those interpreted by the shell, are replaced with &quot;_&quot;. Nevertheless, you should put %F into single quotes: &#8216;%F&#8217;.<br />
 Use &quot;delivery mda /usr/bin/procmail -f &#8216;%F&#8217; -d $USER&quot; for the procmail MDA.<br />
 Use &quot;delivery mda /usr/sbin/sendmail -oi -oem -f &#8216;%F&#8217; &#8212; $USER&quot; to let your MTA handle the mail.<br />
 Use &quot;delivery mda /usr/local/bin/msmtp &#8211;host=localhost &#8211;from=&#8217;%F&#8217; &#8212; $USER@`hostname`.`dnsdomainname`&quot; to pass the mail to your MTA via SMTP. (This is what fetchmail does by default.)</p>
<dt>delivery maildir <i>directory</i></p>
<dd> Deliver the mails to the given maildir directory. The directory must exist and it must have the maildir subdirectories <i>cur</i>, <i>new</i>, and <i>tmp</i>; mpop will not create directories. This delivery type only works on file systems that support hard links.</p>
<dt>delivery mbox <i>mbox-file</i></p>
<dd> Deliver the mails to the given file in mbox format. The file will be locked with <code><a href="/docs/linux/man/2-fcntl/">fcntl</a>(2)</code>. mpop uses the MBOXRD mbox format variant; see the documentation of the mbox format.</p>
<dt>delivery exchange <i>directory</i></p>
<dd> Deliver the mails to the given Exchange pickup directory. The directory must exist.</dl>
<p> If the delivery method needs to parse the mail headers for an envelope from address (the mda method if the command contains %F, and the mbox method), then it needs to create a temporary file to store the mail headers (but not the body) in. See $TMPDIR in the FILES / ENVIRONMENT section.</dl>
<dt>uidls_file <i>filename</i></p>
<dd> The file to store UIDLs in. These are needed to identify new messages. %U in the filename will be replaced by the username of the current account. %H in the filename will be replaced by the hostname of the current account. If the filename contains directories that do not exist, mpop will create them. mpop locks this file for exclusive access when accessing the associated POP3 account.<br />
 The default value is &quot;~/.mpop_uidls/%U_at_%H&quot;. You can also use a single UIDLS file for multiple accounts, but then you cannot poll more than one of these accounts at the same time.</p>
<dt>only_new [(<i>on</i>|<i>off</i>)]</p>
<dd> By default, mpop processes only new messages (new messages are those that were not already successfully retrieved in an earlier session). If this option is turned off, mpop will process all messages.</p>
<dt>keep [(<i>on</i>|<i>off</i>)]</p>
<dd> Keep all mails on the POP3 server, never delete them. The default behaviour is to delete mails that have been successfully retrieved or filtered by kill filters.</p>
<dt>killsize (<i>off</i>|<i>size</i>)</p>
<dd> Mails larger than the given size will be deleted (unless the <code>keep</code> command is used, in which case they will just be skipped). The size argument must be zero or greater. If it is followed by a `k&#8217; or an `m&#8217;, the size is measured in kibibytes/mebibytes instead of bytes. Note that some POP3 servers report slightly incorrect sizes for mails; see <code>NOTES</code> below.<br />
 When <code>killsize</code> is set to 0 and <code>keep</code> is set to on, then all mails are marked as retrieved, but no mail gets deleted from the server. This can be used to synchronize the UID list on the client to the UID list on the server.</p>
<dt>skipsize (<i>off</i>|<i>size</i>)</p>
<dd> Mails larger than the given size will be skipped (not downloaded). The size argument must be zero or greater. If it is followed by a `k&#8217; or an `m&#8217;, the size is measured in kibibytes/mebibytes instead of bytes. Note that some POP3 servers report slightly incorrect sizes for mails; see <code>NOTES</code> below.</p>
<dt>filter [<i>command</i>]</p>
<dd> Set a filter which will decide whether to retrieve, skip, or delete each mail by investigating the mail&#8217;s headers. The POP3 server must support the POP3 TOP command for this to work; see option <code>&#8211;serverinfo</code> above. An empty argument disables filtering.<br />
 All occurences of %F in the command will be replaced with the envelope from address of the current message (or MAILER-DAEMON if none is found). Note that this address is guaranteed to contain only letters a-z and A-Z, digits 0-9, and any of &quot;.@_-+/&quot;, even though that is only a subset of what is theoretically allowed in a mail address. Other characters, including those interpreted by the shell, are replaced with &quot;_&quot;. Nevertheless, you should put %F into single quotes: &#8216;%F&#8217;.<br />
 All occurences of %S in the command will be replaced with the size of the current mail as reported by the POP3 server.<br />
 The mail headers (plus the blank line separating the headers from the body) will be piped to the command. Based on the return code, mpop decides what to do with the mail:<br />
 0: proceed normally; no special action<br />
 1: delete the mail; do not retrieve it<br />
 2: skip the mail; do not retrieve it<br />
 Return codes greater than or equal to 3 mean that an error occured. The sysexits.h error codes may be used to give information about the kind of the error, but this is not necessary.</p>
<dt>received_header [(<i>on</i>|<i>off</i>)]</p>
<dd> Enable or disable adding a Received header. By default, mpop prepends a Received header to the mail during delivery. This is required by the RFCs if the mail is subsequently further delivered e.g. via SMTP.</dl>
<h2>FILTERING</h2>
<p> There are three filtering commands available. They will be executed in the following order:<br />
 <code>killsize</code><br />
 <code>skipsize</code><br />
 <code>filter</code><br />
 If a filtering command applies to a mail, the remaining filters will not be executed.</p>
<h2>EXAMPLES</h2>
<p> <code>Configuration file</code> </p>
<p> # Example for a user configuration file ~/.mpoprc<br />
 #<br />
 # This file focusses on TLS, authentication, and the mail delivery method.<br />
 # Features not used here include mail filtering, timeouts, SOCKS proxies,<br />
 # TLS parameters, and more. </p>
<p> # Set default values for all following accounts.<br />
 defaults </p>
<p> # Always use TLS.<br />
 tls on </p>
<p> # Set a list of trusted CAs for TLS. You can use a system-wide default file,<br />
 # as in this example, or download the root certificate of your CA and use that.<br />
 tls_trust_file /etc/ssl/certs/ca-certificates.crt </p>
<p> # Additionally, you should use the tls_crl_file command to check for revoked<br />
 # certificates, but unfortunately getting revocation lists and keeping them<br />
 # up to date is not straightforward.<br />
 #tls_crl_file ~/.tls-crls </p>
<p> # Deliver mail to an MBOX mail file:<br />
 delivery mbox ~/Mail/inbox<br />
 # Deliver mail to a maildir folder:<br />
 #delivery maildir ~/Mail/incoming<br />
 # Deliver mail via procmail:<br />
 #delivery mda &quot;/usr/bin/procmail -f &#8216;%F&#8217; -d $USER&quot;<br />
 # Deliver mail via the local SMTP server:<br />
 #delivery mda &quot;/usr/bin/msmtp &#8211;host=localhost &#8211;from=&#8217;%F&#8217; &#8212; $USER&quot;<br />
 # Deliver mail to an Exchange pickup directory:<br />
 #delivery exchange c:xchange\pickup </p>
<p> # A freemail service<br />
 account freemail </p>
<p> # Host name of the POP3 server<br />
 host pop.freemail.example </p>
<p> # As an alternative to tls_trust_file/tls_crl_file, you can use tls_fingerprint<br />
 # to pin a single certificate. You have to update the fingerprint when the<br />
 # server certificate changes, but an attacker cannot trick you into accepting<br />
 # a fraudulent certificate. Get the fingerprint with<br />
 # $ mpop &#8211;serverinfo &#8211;tls &#8211;tls-certcheck=off &#8211;host=pop.freemail.example<br />
 tls_fingerprint 00::11::22::33::44::55::66::77::88::99::AA::BB::CC::DD::EE::FF::00::11::22::33 </p>
<p> # Authentication. The password is given using one of five methods, see below.<br />
 user joe.smith </p>
<p> # Password method 1: Add the password to the system keyring, and let mpop get<br />
 # it automatically. To set the keyring password using Gnome&#8217;s libsecret:<br />
 # $ secret-tool store &#8211;label=mpop \<br />
 # host pop.freemail.example \<br />
 # service pop3 \<br />
 # user joe.smith </p>
<p> # Password method 2: Store the password in an encrypted file, and tell mpop<br />
 # which command to use to decrypt it. This is usually used with GnuPG, as in<br />
 # this example. Usually gpg-agent will ask once for the decryption password.<br />
 passwordeval gpg2 &#8211;no-tty -q -d ~/.mpop-password.gpg </p>
<p> # Password method 3: Store the password directly in this file. Usually it is not<br />
 # a good idea to store passwords in plain text files. If you do it anyway, at<br />
 # least make sure that this file can only be read by yourself.<br />
 #password secret123 </p>
<p> # Password method 4: Store the password in ~/.netrc. This method is probably not<br />
 # relevant anymore. </p>
<p> # Password method 5: Do not specify a password. Mpop will then prompt you for<br />
 # it. This means you need to be able to type into a terminal when mpop runs. </p>
<p> # A second mail box at the same freemail service<br />
 account freemail2 : freemail<br />
 user joey </p>
<p> # The POP3 server of your ISP<br />
 account isp<br />
 host mail.isp.example<br />
 auth on<br />
 user 12345<br />
 # Your ISP runs SpamAssassin, so test each mail for the &quot;X-Spam-Status: Yes&quot;<br />
 # header, and delete all mails with this header before downloading them.<br />
 filter<tt>&nbsp;<wbr></tt>if [ &quot;`grep &quot;^X-Spam-Status: Yes&quot;`&quot; ]; then exit 1; else exit 0; fi</p>
<p> # Set a default account<br />
 account default : freemail </p>
<p> <code>Filtering with SpamAssassin</code> </p>
<p> The command <code>filter&nbsp;<wbr>/path/to/spamc -c &gt; /dev/null</code> will delete all mails that SpamAssassin thinks are spam. Since no message body is passed to SpamAssassin, you should disable all body-specific tests in the SpamAssassin configuration file; for example set <code>use_bayes 0.</code> </p>
<p> If your mail provider runs SpamAssassin for you, you just have to check for the result. The following script can do that when used as an mpop filter:<br />
 #!/bin/sh<br />
 if [ &quot;`grep &quot;^X-Spam-Status: Yes&quot;`&quot; ]; then </p>
<p>&nbsp;<wbr>exit 1&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>kill this message<br />
 else </p>
<p>&nbsp;<wbr>exit 0&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>proceed normally<br />
 fi<br />
 Since the filter command is passed to a shell, you can also use this directly:<br />
 <code>filter if [&nbsp;<wbr>`grep&nbsp;<wbr>^X-Spam-Status: Yes` ]; then exit 1; else exit 0; fi</code> </p>
<p> <code>Using mpop with Tor</code> </p>
<p> Use the following settings:<br />
 <code>proxy_host 127.0.0.1</code><br />
 <code>proxy_port 9050</code><br />
 <code>tls on</code><br />
 Use an IP address as proxy host name, so that mpop does not leak a DNS query when resolving it.<br />
 TLS is required to prevent exit hosts from reading your POP3 session. You also need <code>tls_trust_file</code> or <code>tls_fingerprint</code> to check the server identity. </p>
<h2>FILES</h2>
<dl>
<dt>~/.mpoprc</p>
<dd> Default configuration file.</p>
<dt>~/.mpop_uidls</p>
<dd> Default directory to store UIDLs files in.</p>
<dt>~/.netrc and SYSCONFDIR/netrc</p>
<dd> The netrc file contains login information. Before prompting for a password, msmtp will search it in ~/.netrc and SYSCONFDIR/netrc.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>$USER, $LOGNAME</p>
<dd> These variables override the user&#8217;s login name. $LOGNAME is only used if $USER is unset. The user&#8217;s login name is used for Received headers.</p>
<dt>$TMPDIR</p>
<dd> Directory to create temporary files in. If this is unset, a system specific default directory is used.</dl>
<h2>AUTHOR</h2>
<p> mpop was written by Martin Lambers &lt;marlam [at] marlam.de&gt;<br />
 Other authors are listed in the AUTHORS file in the source distribution.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1), <code><a href="/docs/linux/man/1-spamassassin/">spamassassin</a></code>(1), <code><a href="/docs/linux/man/5-netrc/">netrc</a></code>(5) or <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1), <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) </p>
<h2>Index</h2>
