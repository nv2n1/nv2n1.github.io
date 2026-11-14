---
title: "sshd_config(5)"
name: "sshd_config"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sshd_config/"
description: "sshd_config – OpenSSH daemon configuration file"
---

<p><code>sshd_config</code> &#8211; OpenSSH daemon configuration file</p>
<h2>Description</h2>
<p><a href="/docs/linux/man/8-sshd/">sshd</a>(8) reads configuration data from /etc/ssh/sshd_config (or the file specified with &#8211;<code>f</code> on the command line). The file contains keyword-argument pairs, one per line. For each keyword, the first obtained value will be used. Lines starting with `#&#8217; and empty lines are interpreted as comments. Arguments may optionally be enclosed in double quotes () in order to represent arguments containing spaces. Note that the Debian <code>openssh-server</code> package sets several options as standard in /etc/ssh/sshd_config which are not the default in <a href="/docs/linux/man/8-sshd/">sshd</a>(8):  </p>
<li> <code>Include /etc/ssh/sshd_config.d/*.conf</code>
<li> <code>KbdInteractiveAuthentication no</code>
<li> <code>X11Forwarding yes</code>
<li> <code>PrintMotd no</code>
<li> <code>AcceptEnv LANG LC_*</code>
<li> <code>Subsystem sftp /usr/lib/openssh/sftp-server</code>
<li> <code>UsePAM yes</code> </ul>
<p> /etc/ssh/sshd_config.d/*.conf files are included at the start of the configuration file, so options set there will override those in /etc/ssh/sshd_config. The possible keywords and their meanings are as follows (note that keywords are case-insensitive and arguments are case-sensitive):</p>
<dl>
<dt><code>AcceptEnv</code></p>
<dd>Specifies what environment variables sent by the client will be copied into the session&#8217;s <a href="/docs/linux/man/7-environ/">environ</a>(7). See <code>SendEnv</code> and <code>SetEnv</code> in ssh_config5 for how to configure the client. The <code>TERM</code> environment variable is always accepted whenever the client requests a pseudo-terminal as it is required by the protocol. Variables are specified by name, which may contain the wildcard characters `*&#8217; and `?&#8217; Multiple environment variables may be separated by whitespace or spread across multiple <code>AcceptEnv</code> directives. Be warned that some environment variables could be used to bypass restricted user environments. For this reason, care should be taken in the use of this directive. The default is not to accept any environment variables.</p>
<dt><code>AddressFamily</code></p>
<dd>Specifies which address family should be used by <a href="/docs/linux/man/8-sshd/">sshd</a>(8). Valid arguments are <code>any</code> (the default), <code>inet</code> (use IPv4 only), or <code>inet6</code> (use IPv6 only).</p>
<dt><code>AllowAgentForwarding</code></p>
<dd>Specifies whether ssh-agent1 forwarding is permitted. The default is <code>yes</code> Note that disabling agent forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.</p>
<dt><code>AllowGroups</code></p>
<dd>This keyword can be followed by a list of group name patterns, separated by spaces. If specified, login is allowed only for users whose primary group or supplementary group list matches one of the patterns. Only group names are valid; a numerical group ID is not recognized. By default, login is allowed for all groups. The allow/deny groups directives are processed in the following order: <code>DenyGroups</code> <code>AllowGroups</code> See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>AllowStreamLocalForwarding</code></p>
<dd>Specifies whether StreamLocal (Unix-domain socket) forwarding is permitted. The available options are <code>yes</code> (the default) or <code>all</code> to allow StreamLocal forwarding, <code>no</code> to prevent all StreamLocal forwarding, <code>local</code> to allow local (from the perspective of <a href="/docs/linux/man/1-ssh/">ssh</a>(1)) forwarding only or <code>remote</code> to allow remote forwarding only. Note that disabling StreamLocal forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.</p>
<dt><code>AllowTcpForwarding</code></p>
<dd>Specifies whether TCP forwarding is permitted. The available options are <code>yes</code> (the default) or <code>all</code> to allow TCP forwarding, <code>no</code> to prevent all TCP forwarding, <code>local</code> to allow local (from the perspective of <a href="/docs/linux/man/1-ssh/">ssh</a>(1)) forwarding only or <code>remote</code> to allow remote forwarding only. Note that disabling TCP forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.</p>
<dt><code>AllowUsers</code></p>
<dd>This keyword can be followed by a list of user name patterns, separated by spaces. If specified, login is allowed only for user names that match one of the patterns. Only user names are valid; a numerical user ID is not recognized. By default, login is allowed for all users. If the pattern takes the form USER [at] HOST then USER and HOST are separately checked, restricting logins to particular users from particular hosts. HOST criteria may additionally contain addresses to match in CIDR address/masklen format. The allow/deny users directives are processed in the following order: <code>DenyUsers</code> <code>AllowUsers</code> See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>AuthenticationMethods</code></p>
<dd>Specifies the authentication methods that must be successfully completed for a user to be granted access. This option must be followed by one or more lists of comma-separated authentication method names, or by the single string <code>any</code> to indicate the default behaviour of accepting any single authentication method. If the default is overridden, then successful authentication requires completion of every method in at least one of these lists. For example, Qq publickey,password publickey,keyboard-interactive would require the user to complete public key authentication, followed by either password or keyboard interactive authentication. Only methods that are next in one or more lists are offered at each stage, so for this example it would not be possible to attempt password or keyboard-interactive authentication before public key. For keyboard interactive authentication it is also possible to restrict authentication to a specific device by appending a colon followed by the device identifier <code>bsdauth</code> or <code>pam</code> depending on the server configuration. For example, Qq keyboard-interactive:bsdauth would restrict keyboard interactive authentication to the <code>bsdauth</code> device. If the publickey method is listed more than once, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) verifies that keys that have been used successfully are not reused for subsequent authentications. For example, Qq publickey,publickey requires successful authentication using two different public keys. Note that each authentication method listed should also be explicitly enabled in the configuration. The available authentication methods are: Qq gssapi-with-mic , Qq hostbased , Qq keyboard-interactive , Qq none (used for access to password-less accounts when <code>PermitEmptyPasswords</code> is enabled), Qq password and Qq publickey .</p>
<dt><code>AuthorizedKeysCommand</code></p>
<dd>Specifies a program to be used to look up the user&#8217;s public keys. The program must be owned by root, not writable by group or others and specified by an absolute path. Arguments to <code>AuthorizedKeysCommand</code> accept the tokens described in the Sx TOKENS section. If no arguments are specified then the username of the target user is used. The program should produce on standard output zero or more lines of authorized_keys output (see Sx AUTHORIZED_KEYS in <a href="/docs/linux/man/8-sshd/">sshd</a>(8)). <code>AuthorizedKeysCommand</code> is tried after the usual <code>AuthorizedKeysFile</code> files and will not be executed if a matching key is found there. By default, no <code>AuthorizedKeysCommand</code> is run.</p>
<dt><code>AuthorizedKeysCommandUser</code></p>
<dd>Specifies the user under whose account the <code>AuthorizedKeysCommand</code> is run. It is recommended to use a dedicated user that has no other role on the host than running authorized keys commands. If <code>AuthorizedKeysCommand</code> is specified but <code>AuthorizedKeysCommandUser</code> is not, then <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will refuse to start.</p>
<dt><code>AuthorizedKeysFile</code></p>
<dd>Specifies the file that contains the public keys used for user authentication. The format is described in the AUTHORIZED_KEYS FILE FORMAT section of <a href="/docs/linux/man/8-sshd/">sshd</a>(8). Arguments to <code>AuthorizedKeysFile</code> accept the tokens described in the Sx TOKENS section. After expansion, <code>AuthorizedKeysFile</code> is taken to be an absolute path or one relative to the user&#8217;s home directory. Multiple files may be listed, separated by whitespace. Alternately this option may be set to <code>none</code> to skip checking for user keys in files. The default is Qq .ssh/authorized_keys .ssh/authorized_keys2 .</p>
<dt><code>AuthorizedPrincipalsCommand</code></p>
<dd>Specifies a program to be used to generate the list of allowed certificate principals as per <code>AuthorizedPrincipalsFile</code> The program must be owned by root, not writable by group or others and specified by an absolute path. Arguments to <code>AuthorizedPrincipalsCommand</code> accept the tokens described in the Sx TOKENS section. If no arguments are specified then the username of the target user is used. The program should produce on standard output zero or more lines of <code>AuthorizedPrincipalsFile</code> output. If either <code>AuthorizedPrincipalsCommand</code> or <code>AuthorizedPrincipalsFile</code> is specified, then certificates offered by the client for authentication must contain a principal that is listed. By default, no <code>AuthorizedPrincipalsCommand</code> is run.</p>
<dt><code>AuthorizedPrincipalsCommandUser</code></p>
<dd>Specifies the user under whose account the <code>AuthorizedPrincipalsCommand</code> is run. It is recommended to use a dedicated user that has no other role on the host than running authorized principals commands. If <code>AuthorizedPrincipalsCommand</code> is specified but <code>AuthorizedPrincipalsCommandUser</code> is not, then <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will refuse to start.</p>
<dt><code>AuthorizedPrincipalsFile</code></p>
<dd>Specifies a file that lists principal names that are accepted for certificate authentication. When using certificates signed by a key listed in <code>TrustedUserCAKeys</code> this file lists names, one of which must appear in the certificate for it to be accepted for authentication. Names are listed one per line preceded by key options (as described in Sx AUTHORIZED_KEYS FILE FORMAT in <a href="/docs/linux/man/8-sshd/">sshd</a>(8)). Empty lines and comments starting with `#&#8217; are ignored. Arguments to <code>AuthorizedPrincipalsFile</code> accept the tokens described in the Sx TOKENS section. After expansion, <code>AuthorizedPrincipalsFile</code> is taken to be an absolute path or one relative to the user&#8217;s home directory. The default is <code>none</code> i.e. not to use a principals file &#8211; in this case, the username of the user must appear in a certificate&#8217;s principals list for it to be accepted. Note that <code>AuthorizedPrincipalsFile</code> is only used when authentication proceeds using a CA listed in <code>TrustedUserCAKeys</code> and is not consulted for certification authorities trusted via ~/.ssh/authorized_keys though the <code>principals=</code> key option offers a similar facility (see <a href="/docs/linux/man/8-sshd/">sshd</a>(8) for details).</p>
<dt><code>Banner</code></p>
<dd>The contents of the specified file are sent to the remote user before authentication is allowed. If the argument is <code>none</code> then no banner is displayed. By default, no banner is displayed.</p>
<dt><code>CASignatureAlgorithms</code></p>
<dd>Specifies which algorithms are allowed for signing of certificates by certificate authorities (CAs). The default is: </p>
<blockquote>
<pre>ssh-ed25519,ecdsa-sha2-nistp256,
ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519 [at] openssh.com,
sk-ecdsa-sha2-nistp256 [at] openssh.com,
rsa-sha2-512,rsa-sha2-256</pre>
</blockquote>
<p> If the specified list begins with a `+&#8217; character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. Certificates signed using other algorithms will not be accepted for public key or host-based authentication.</p>
<dt><code>ChrootDirectory</code></p>
<dd>Specifies the pathname of a directory to <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to after authentication. At session startup <a href="/docs/linux/man/8-sshd/">sshd</a>(8) checks that all components of the pathname are root-owned directories which are not writable by any other user or group. After the chroot, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) changes the working directory to the user&#8217;s home directory. Arguments to <code>ChrootDirectory</code> accept the tokens described in the Sx TOKENS section. The <code>ChrootDirectory</code> must contain the necessary files and directories to support the user&#8217;s session. For an interactive session this requires at least a shell, typically <a href="/docs/linux/man/1-sh/">sh</a>(1), and basic /dev nodes such as <a href="/docs/linux/man/4-null/">null</a>(4), <a href="/docs/linux/man/4-zero/">zero</a>(4), <a href="/docs/linux/man/4-stdin/">stdin</a>(4), <a href="/docs/linux/man/4-stdout/">stdout</a>(4), <a href="/docs/linux/man/4-stderr/">stderr</a>(4), and <a href="/docs/linux/man/4-tty/">tty</a>(4) devices. For file transfer sessions using SFTP no additional configuration of the environment is necessary if the in-process sftp-server is used, though sessions which use logging may require /dev/log inside the chroot directory on some operating systems (see sftp-server8 for details). For safety, it is very important that the directory hierarchy be prevented from modification by other processes on the system (especially those outside the jail). Misconfiguration can lead to unsafe environments which <a href="/docs/linux/man/8-sshd/">sshd</a>(8) cannot detect. The default is <code>none</code> indicating not to <a href="/docs/linux/man/2-chroot/">chroot</a>(2).</p>
<dt><code>Ciphers</code></p>
<dd>Specifies the ciphers allowed. Multiple ciphers must be comma-separated. If the specified list begins with a `+&#8217; character, then the specified ciphers will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified ciphers (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified ciphers will be placed at the head of the default set. The supported ciphers are: </p>
<dt><code>3des-cbc</code></p>
<dd>
<dt><code>aes128-cbc</code></p>
<dd>
<dt><code>aes192-cbc</code></p>
<dd>
<dt><code>aes256-cbc</code></p>
<dd>
<dt><code>aes128-ctr</code></p>
<dd>
<dt><code>aes192-ctr</code></p>
<dd>
<dt><code>aes256-ctr</code></p>
<dd>
<dt><code>aes128-gcm [at] openssh.com</code></p>
<dd>
<dt><code>aes256-gcm [at] openssh.com</code></p>
<dd>
<dt><code>chacha20-poly1305 [at] openssh.com</code></p>
<dd></dl>
<p> The default is: </p>
<blockquote>
<pre>chacha20-poly1305 [at] openssh.com,
aes128-ctr,aes192-ctr,aes256-ctr,
aes128-gcm [at] openssh.com,aes256-gcm [at] openssh.com</pre>
</blockquote>
<p> The list of available ciphers may also be obtained using Qq ssh -Q cipher .</p>
<dt><code>ClientAliveCountMax</code></p>
<dd>Sets the number of client alive messages which may be sent without <a href="/docs/linux/man/8-sshd/">sshd</a>(8) receiving any messages back from the client. If this threshold is reached while client alive messages are being sent, sshd will disconnect the client, terminating the session. It is important to note that the use of client alive messages is very different from <code>TCPKeepAlive</code> The client alive messages are sent through the encrypted channel and therefore will not be spoofable. The TCP keepalive option enabled by <code>TCPKeepAlive</code> is spoofable. The client alive mechanism is valuable when the client or server depend on knowing when a connection has become unresponsive. The default value is 3. If <code>ClientAliveInterval</code> is set to 15, and <code>ClientAliveCountMax</code> is left at the default, unresponsive SSH clients will be disconnected after approximately 45 seconds. Setting a zero <code>ClientAliveCountMax</code> disables connection termination.</p>
<dt><code>ClientAliveInterval</code></p>
<dd>Sets a timeout interval in seconds after which if no data has been received from the client, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will send a message through the encrypted channel to request a response from the client. The default is 0, indicating that these messages will not be sent to the client.</p>
<dt><code>Compression</code></p>
<dd>Specifies whether compression is enabled after the user has authenticated successfully. The argument must be <code>yes</code> <code>delayed</code> (a legacy synonym for <code>yes</code> or <code>no</code> The default is <code>yes</code></p>
<dt><code>DebianBanner</code></p>
<dd>Specifies whether the distribution-specified extra version suffix is included during initial protocol handshake. The default is <code>yes</code></p>
<dt><code>DenyGroups</code></p>
<dd>This keyword can be followed by a list of group name patterns, separated by spaces. Login is disallowed for users whose primary group or supplementary group list matches one of the patterns. Only group names are valid; a numerical group ID is not recognized. By default, login is allowed for all groups. The allow/deny groups directives are processed in the following order: <code>DenyGroups</code> <code>AllowGroups</code> See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>DenyUsers</code></p>
<dd>This keyword can be followed by a list of user name patterns, separated by spaces. Login is disallowed for user names that match one of the patterns. Only user names are valid; a numerical user ID is not recognized. By default, login is allowed for all users. If the pattern takes the form USER [at] HOST then USER and HOST are separately checked, restricting logins to particular users from particular hosts. HOST criteria may additionally contain addresses to match in CIDR address/masklen format. The allow/deny users directives are processed in the following order: <code>DenyUsers</code> <code>AllowUsers</code> See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>DisableForwarding</code></p>
<dd>Disables all forwarding features, including X11, ssh-agent1, TCP and StreamLocal. This option overrides all other forwarding-related options and may simplify restricted configurations.</p>
<dt><code>ExposeAuthInfo</code></p>
<dd>Writes a temporary file containing a list of authentication methods and public credentials (e.g. keys) used to authenticate the user. The location of the file is exposed to the user session through the <code>SSH_USER_AUTH</code> environment variable. The default is <code>no</code></p>
<dt><code>FingerprintHash</code></p>
<dd>Specifies the hash algorithm used when logging key fingerprints. Valid options are: <code>md5</code> and <code>sha256</code> The default is <code>sha256</code></p>
<dt><code>ForceCommand</code></p>
<dd>Forces the execution of the command specified by <code>ForceCommand</code> ignoring any command supplied by the client and ~/.ssh/rc if present. The command is invoked by using the user&#8217;s login shell with the -c option. This applies to shell, command, or subsystem execution. It is most useful inside a <code>Match</code> block. The command originally supplied by the client is available in the <code>SSH_ORIGINAL_COMMAND</code> environment variable. Specifying a command of <code>internal-sftp</code> will force the use of an in-process SFTP server that requires no support files when used with <code>ChrootDirectory</code> The default is <code>none</code></p>
<dt><code>GatewayPorts</code></p>
<dd>Specifies whether remote hosts are allowed to connect to ports forwarded for the client. By default, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) binds remote port forwardings to the loopback address. This prevents other remote hosts from connecting to forwarded ports. <code>GatewayPorts</code> can be used to specify that sshd should allow remote port forwardings to bind to non-loopback addresses, thus allowing other hosts to connect. The argument may be <code>no</code> to force remote port forwardings to be available to the local host only, <code>yes</code> to force remote port forwardings to bind to the wildcard address, or <code>clientspecified</code> to allow the client to select the address to which the forwarding is bound. The default is <code>no</code></p>
<dt><code>GSSAPIAuthentication</code></p>
<dd>Specifies whether user authentication based on GSSAPI is allowed. The default is <code>no</code></p>
<dt><code>GSSAPICleanupCredentials</code></p>
<dd>Specifies whether to automatically destroy the user&#8217;s credentials cache on logout. The default is <code>yes</code></p>
<dt><code>GSSAPIKeyExchange</code></p>
<dd>Specifies whether key exchange based on GSSAPI is allowed. GSSAPI key exchange doesn&#8217;t rely on ssh keys to verify host identity. The default is <code>no</code></p>
<dt><code>GSSAPIStrictAcceptorCheck</code></p>
<dd>Determines whether to be strict about the identity of the GSSAPI acceptor a client authenticates against. If set to <code>yes</code> then the client must authenticate against the host service on the current hostname. If set to <code>no</code> then the client may authenticate against any service key stored in the machine&#8217;s default store. This facility is provided to assist with operation on multi homed machines. The default is <code>yes</code></p>
<dt><code>GSSAPIStoreCredentialsOnRekey</code></p>
<dd>Controls whether the user&#8217;s GSSAPI credentials should be updated following a successful connection rekeying. This option can be used to accepted renewed or updated credentials from a compatible client. The default is &#8220;no&#8221; For this to work <code>GSSAPIKeyExchange</code> needs to be enabled in the server and also used by the client.</p>
<dt><code>GSSAPIKexAlgorithms</code></p>
<dd>The list of key exchange algorithms that are accepted by GSSAPI key exchange. Possible values are </p>
<pre>gss-gex-sha1-,
gss-group1-sha1-,
gss-group14-sha1-,
gss-group14-sha256-,
gss-group16-sha512-,
gss-nistp256-sha256-,
gss-curve25519-sha256-</pre>
<p>The default is &#8220;gss-group14-sha256-,gss-group16-sha512-,gss-nistp256-sha256-,gss-curve25519-sha256-,gss-gex-sha1-,gss-group14-sha1-&#8221; This option only applies to connections using GSSAPI.</p>
<dt><code>HostbasedAcceptedAlgorithms</code></p>
<dd>Specifies the signature algorithms that will be accepted for hostbased authentication as a list of comma-separated patterns. Alternately if the specified list begins with a `+&#8217; character, then the specified signature algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified signature algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified signature algorithms will be placed at the head of the default set. The default for this option is: </p>
<pre>ssh-ed25519-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp256-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp384-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp521-cert-v01 [at] openssh.com,
sk-ssh-ed25519-cert-v01 [at] openssh.com,
sk-ecdsa-sha2-nistp256-cert-v01 [at] openssh.com,
rsa-sha2-512-cert-v01 [at] openssh.com,
rsa-sha2-256-cert-v01 [at] openssh.com,
ssh-ed25519,
ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519 [at] openssh.com,
sk-ecdsa-sha2-nistp256 [at] openssh.com,
rsa-sha2-512,rsa-sha2-256</pre>
<p>The list of available signature algorithms may also be obtained using Qq ssh -Q HostbasedAcceptedAlgorithms . This was formerly named HostbasedAcceptedKeyTypes.</p>
<dt><code>HostbasedAuthentication</code></p>
<dd>Specifies whether rhosts or /etc/hosts.equiv authentication together with successful public key client host authentication is allowed (host-based authentication). The default is <code>no</code></p>
<dt><code>HostbasedUsesNameFromPacketOnly</code></p>
<dd>Specifies whether or not the server will attempt to perform a reverse name lookup when matching the name in the ~/.shosts ~/.rhosts and /etc/hosts.equiv files during <code>HostbasedAuthentication</code> A setting of <code>yes</code> means that <a href="/docs/linux/man/8-sshd/">sshd</a>(8) uses the name supplied by the client rather than attempting to resolve the name from the TCP connection itself. The default is <code>no</code></p>
<dt><code>HostCertificate</code></p>
<dd>Specifies a file containing a public host certificate. The certificate&#8217;s public key must match a private host key already specified by <code>HostKey</code> The default behaviour of <a href="/docs/linux/man/8-sshd/">sshd</a>(8) is not to load any certificates.</p>
<dt><code>HostKey</code></p>
<dd>Specifies a file containing a private host key used by SSH. The defaults are /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_ed25519_key and /etc/ssh/ssh_host_rsa_key Note that <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will refuse to use a file if it is group/world-accessible and that the <code>HostKeyAlgorithms</code> option restricts which of the keys are actually used by <a href="/docs/linux/man/8-sshd/">sshd</a>(8). It is possible to have multiple host key files. It is also possible to specify public host key files instead. In this case operations on the private key will be delegated to an ssh-agent1.</p>
<dt><code>HostKeyAgent</code></p>
<dd>Identifies the UNIX-domain socket used to communicate with an agent that has access to the private host keys. If the string Qq SSH_AUTH_SOCK is specified, the location of the socket will be read from the <code>SSH_AUTH_SOCK</code> environment variable.</p>
<dt><code>HostKeyAlgorithms</code></p>
<dd>Specifies the host key signature algorithms that the server offers. The default for this option is: </p>
<pre>ssh-ed25519-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp256-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp384-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp521-cert-v01 [at] openssh.com,
sk-ssh-ed25519-cert-v01 [at] openssh.com,
sk-ecdsa-sha2-nistp256-cert-v01 [at] openssh.com,
rsa-sha2-512-cert-v01 [at] openssh.com,
rsa-sha2-256-cert-v01 [at] openssh.com,
ssh-ed25519,
ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519 [at] openssh.com,
sk-ecdsa-sha2-nistp256 [at] openssh.com,
rsa-sha2-512,rsa-sha2-256</pre>
<p>The list of available signature algorithms may also be obtained using Qq ssh -Q HostKeyAlgorithms .</p>
<dt><code>IgnoreRhosts</code></p>
<dd>Specifies whether to ignore per-user .rhosts and .shosts files during <code>HostbasedAuthentication</code> The system-wide /etc/hosts.equiv and /etc/ssh/shosts.equiv are still used regardless of this setting. Accepted values are <code>yes</code> (the default) to ignore all per-user files, <code>shosts-only</code> to allow the use of .shosts but to ignore .rhosts or <code>no</code> to allow both .shosts and rhosts</p>
<dt><code>IgnoreUserKnownHosts</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should ignore the user&#8217;s ~/.ssh/known_hosts during <code>HostbasedAuthentication</code> and use only the system-wide known hosts file /etc/ssh/known_hosts The default is &#8220;no&#8221;</p>
<dt><code>Include</code></p>
<dd>Include the specified configuration file(s). Multiple pathnames may be specified and each pathname may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) wildcards that will be expanded and processed in lexical order. Files without absolute paths are assumed to be in /etc/ssh An <code>Include</code> directive may appear inside a <code>Match</code> block to perform conditional inclusion.</p>
<dt><code>IPQoS</code></p>
<dd>Specifies the IPv4 type-of-service or DSCP class for the connection. Accepted values are <code>af11</code> <code>af12</code> <code>af13</code> <code>af21</code> <code>af22</code> <code>af23</code> <code>af31</code> <code>af32</code> <code>af33</code> <code>af41</code> <code>af42</code> <code>af43</code> <code>cs0</code> <code>cs1</code> <code>cs2</code> <code>cs3</code> <code>cs4</code> <code>cs5</code> <code>cs6</code> <code>cs7</code> <code>ef</code> <code>le</code> <code>lowdelay</code> <code>throughput</code> <code>reliability</code> a numeric value, or <code>none</code> to use the operating system default. This option may take one or two arguments, separated by whitespace. If one argument is specified, it is used as the packet class unconditionally. If two values are specified, the first is automatically selected for interactive sessions and the second for non-interactive sessions. The default is <code>lowdelay</code> for interactive sessions and <code>throughput</code> for non-interactive sessions.</p>
<dt><code>KbdInteractiveAuthentication</code></p>
<dd>Specifies whether to allow keyboard-interactive authentication. The default is <code>yes</code> The argument to this keyword must be <code>yes</code> or <code>no</code> <code>ChallengeResponseAuthentication</code> is a deprecated alias for this.</p>
<dt><code>KerberosAuthentication</code></p>
<dd>Specifies whether the password provided by the user for <code>PasswordAuthentication</code> will be validated through the Kerberos KDC. To use this option, the server needs a Kerberos servtab which allows the verification of the KDC&#8217;s identity. The default is <code>no</code></p>
<dt><code>KerberosGetAFSToken</code></p>
<dd>If AFS is active and the user has a Kerberos 5 TGT, attempt to acquire an AFS token before accessing the user&#8217;s home directory. The default is <code>no</code></p>
<dt><code>KerberosOrLocalPasswd</code></p>
<dd>If password authentication through Kerberos fails then the password will be validated via any additional local mechanism such as /etc/passwd The default is <code>yes</code></p>
<dt><code>KerberosTicketCleanup</code></p>
<dd>Specifies whether to automatically destroy the user&#8217;s ticket cache file on logout. The default is <code>yes</code></p>
<dt><code>KexAlgorithms</code></p>
<dd>Specifies the available KEX (Key Exchange) algorithms. Multiple algorithms must be comma-separated. Alternately if the specified list begins with a `+&#8217; character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified algorithms will be placed at the head of the default set. The supported algorithms are: </p>
<dt><code>curve25519-sha256</code></p>
<dd>
<dt><code>curve25519-sha256 [at] libssh.org</code></p>
<dd>
<dt><code>diffie-hellman-group1-sha1</code></p>
<dd>
<dt><code>diffie-hellman-group14-sha1</code></p>
<dd>
<dt><code>diffie-hellman-group14-sha256</code></p>
<dd>
<dt><code>diffie-hellman-group16-sha512</code></p>
<dd>
<dt><code>diffie-hellman-group18-sha512</code></p>
<dd>
<dt><code>diffie-hellman-group-exchange-sha1</code></p>
<dd>
<dt><code>diffie-hellman-group-exchange-sha256</code></p>
<dd>
<dt><code>ecdh-sha2-nistp256</code></p>
<dd>
<dt><code>ecdh-sha2-nistp384</code></p>
<dd>
<dt><code>ecdh-sha2-nistp521</code></p>
<dd>
<dt><code>sntrup761x25519-sha512 [at] openssh.com</code></p>
<dd></dl>
<p> The default is: </p>
<blockquote>
<pre>curve25519-sha256,curve25519-sha256 [at] libssh.org,
ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,
sntrup761x25519-sha512 [at] openssh.com,
diffie-hellman-group-exchange-sha256,
diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,
diffie-hellman-group14-sha256</pre>
</blockquote>
<p> The list of available key exchange algorithms may also be obtained using Qq ssh -Q KexAlgorithms .</p>
<dt><code>ListenAddress</code></p>
<dd>Specifies the local addresses <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should listen on. The following forms may be used: </p>
<dt><code>ListenAddress</code></p>
<dd><i>hostname | address</i></p>
<dt><code>ListenAddress</code></p>
<dd><i>hostname : port</i></p>
<dt><code>ListenAddress</code></p>
<dd><i>IPv4_address : port</i></p>
<dt><code>ListenAddress</code></p>
<dd>[<i>hostname | address : port</i> ]</dl>
<p> If <i>port</i> is not specified, sshd will listen on the address and all <code>Port</code> options specified. The default is to listen on all local addresses. Multiple <code>ListenAddress</code> options are permitted.</p>
<dt><code>LoginGraceTime</code></p>
<dd>The server disconnects after this time if the user has not successfully logged in. If the value is 0, there is no time limit. The default is 120 seconds.</p>
<dt><code>LogLevel</code></p>
<dd>Gives the verbosity level that is used when logging messages from <a href="/docs/linux/man/8-sshd/">sshd</a>(8). The possible values are: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, and DEBUG3. The default is INFO. DEBUG and DEBUG1 are equivalent. DEBUG2 and DEBUG3 each specify higher levels of debugging output. Logging with a DEBUG level violates the privacy of users and is not recommended.</p>
<dt><code>LogVerbose</code></p>
<dd>Specify one or more overrides to LogLevel. An override consists of a pattern lists that matches the source file, function and line number to force detailed logging for. For example, an override pattern of: </p>
<blockquote>
<pre>kex.c:*:1000,*:kex_exchange_identification():*,packet.c:*</pre>
</blockquote>
<p> would enable detailed logging for line 1000 of kex.c everything in the Fn kex_exchange_identification function, and all code in the packet.c file. This option is intended for debugging and no overrides are enabled by default.</p>
<dt><code>MACs </code>Specifies the available MAC (message authentication code) algorithms.</p>
<dd>The MAC algorithm is used for data integrity protection. Multiple algorithms must be comma-separated. If the specified list begins with a `+&#8217; character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified algorithms will be placed at the head of the default set. The algorithms that contain Qq -etm calculate the MAC after encryption (encrypt-then-mac). These are considered safer and their use recommended. The supported MACs are: </p>
<dt><code>hmac-md5</code></p>
<dd>
<dt><code>hmac-md5-96</code></p>
<dd>
<dt><code>hmac-sha1</code></p>
<dd>
<dt><code>hmac-sha1-96</code></p>
<dd>
<dt><code>hmac-sha2-256</code></p>
<dd>
<dt><code>hmac-sha2-512</code></p>
<dd>
<dt><code>umac-64 [at] openssh.com</code></p>
<dd>
<dt><code>umac-128 [at] openssh.com</code></p>
<dd>
<dt><code>hmac-md5-etm [at] openssh.com</code></p>
<dd>
<dt><code>hmac-md5-96-etm [at] openssh.com</code></p>
<dd>
<dt><code>hmac-sha1-etm [at] openssh.com</code></p>
<dd>
<dt><code>hmac-sha1-96-etm [at] openssh.com</code></p>
<dd>
<dt><code>hmac-sha2-256-etm [at] openssh.com</code></p>
<dd>
<dt><code>hmac-sha2-512-etm [at] openssh.com</code></p>
<dd>
<dt><code>umac-64-etm [at] openssh.com</code></p>
<dd>
<dt><code>umac-128-etm [at] openssh.com</code></p>
<dd></dl>
<p> The default is: </p>
<blockquote>
<pre>umac-64-etm [at] openssh.com,umac-128-etm [at] openssh.com,
hmac-sha2-256-etm [at] openssh.com,hmac-sha2-512-etm [at] openssh.com,
hmac-sha1-etm [at] openssh.com,
umac-64 [at] openssh.com,umac-128 [at] openssh.com,
hmac-sha2-256,hmac-sha2-512,hmac-sha1</pre>
</blockquote>
<p> The list of available MAC algorithms may also be obtained using Qq ssh -Q mac .</p>
<dt><code>Match</code></p>
<dd>Introduces a conditional block. If all of the criteria on the <code>Match</code> line are satisfied, the keywords on the following lines override those set in the global section of the config file, until either another <code>Match</code> line or the end of the file. If a keyword appears in multiple <code>Match</code> blocks that are satisfied, only the first instance of the keyword is applied. The arguments to <code>Match</code> are one or more criteria-pattern pairs or the single token <code>All</code> which matches all criteria. The available criteria are <code>User</code> <code>Group</code> <code>Host</code> <code>LocalAddress</code> <code>LocalPort</code> and <code>Address</code> The match patterns may consist of single entries or comma-separated lists and may use the wildcard and negation operators described in the Sx PATTERNS section of ssh_config5. The patterns in an <code>Address</code> criteria may additionally contain addresses to match in CIDR address/masklen format, such as 192.0.2.0/24 or 2001:db8::/32. Note that the mask length provided must be consistent with the address &#8211; it is an error to specify a mask length that is too long for the address or one with bits set in this host portion of the address. For example, 192.0.2.0/33 and 192.0.2.0/8, respectively. Only a subset of keywords may be used on the lines following a <code>Match</code> keyword. Available keywords are <code>AcceptEnv</code> <code>AllowAgentForwarding</code> <code>AllowGroups</code> <code>AllowStreamLocalForwarding</code> <code>AllowTcpForwarding</code> <code>AllowUsers</code> <code>AuthenticationMethods</code> <code>AuthorizedKeysCommand</code> <code>AuthorizedKeysCommandUser</code> <code>AuthorizedKeysFile</code> <code>AuthorizedPrincipalsCommand</code> <code>AuthorizedPrincipalsCommandUser</code> <code>AuthorizedPrincipalsFile</code> <code>Banner</code> <code>CASignatureAlgorithms</code> <code>ChrootDirectory</code> <code>ClientAliveCountMax</code> <code>ClientAliveInterval</code> <code>DenyGroups</code> <code>DenyUsers</code> <code>DisableForwarding</code> <code>ExposeAuthInfo</code> <code>ForceCommand</code> <code>GatewayPorts</code> <code>GSSAPIAuthentication</code> <code>HostbasedAcceptedAlgorithms</code> <code>HostbasedAuthentication</code> <code>HostbasedUsesNameFromPacketOnly</code> <code>IgnoreRhosts</code> <code>Include</code> <code>IPQoS</code> <code>KbdInteractiveAuthentication</code> <code>KerberosAuthentication</code> <code>LogLevel</code> <code>MaxAuthTries</code> <code>MaxSessions</code> <code>PasswordAuthentication</code> <code>PermitEmptyPasswords</code> <code>PermitListen</code> <code>PermitOpen</code> <code>PermitRootLogin</code> <code>PermitTTY</code> <code>PermitTunnel</code> <code>PermitUserRC</code> <code>PubkeyAcceptedAlgorithms</code> <code>PubkeyAuthentication</code> <code>PubkeyAuthOptions</code> <code>RekeyLimit</code> <code>RevokedKeys</code> <code>SetEnv</code> <code>StreamLocalBindMask</code> <code>StreamLocalBindUnlink</code> <code>TrustedUserCAKeys</code> <code>X11DisplayOffset</code> <code>X11Forwarding</code> and <code>X11UseLocalhost</code></p>
<dt><code>MaxAuthTries</code></p>
<dd>Specifies the maximum number of authentication attempts permitted per connection. Once the number of failures reaches half this value, additional failures are logged. The default is 6.</p>
<dt><code>MaxSessions</code></p>
<dd>Specifies the maximum number of open shell, login or subsystem (e.g. sftp) sessions permitted per network connection. Multiple sessions may be established by clients that support connection multiplexing. Setting <code>MaxSessions</code> to 1 will effectively disable session multiplexing, whereas setting it to 0 will prevent all shell, login and subsystem sessions while still permitting forwarding. The default is 10.</p>
<dt><code>MaxStartups</code></p>
<dd>Specifies the maximum number of concurrent unauthenticated connections to the SSH daemon. Additional connections will be dropped until authentication succeeds or the <code>LoginGraceTime</code> expires for a connection. The default is 10:30:100. Alternatively, random early drop can be enabled by specifying the three colon separated values start:rate:full (e.g. &quot;10:30:60&quot;). <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will refuse connection attempts with a probability of rate/100 (30%) if there are currently start (10) unauthenticated connections. The probability increases linearly and all connection attempts are refused if the number of unauthenticated connections reaches full (60).</p>
<dt><code>ModuliFile</code></p>
<dd>Specifies the <a href="/docs/linux/man/5-moduli/">moduli</a>(5) file that contains the Diffie-Hellman groups used for the &#8220;diffie-hellman-group-exchange-sha1&#8221; and &#8220;diffie-hellman-group-exchange-sha256&#8221; key exchange methods. The default is /etc/ssh/moduli</p>
<dt><code>PasswordAuthentication</code></p>
<dd>Specifies whether password authentication is allowed. The default is <code>yes</code></p>
<dt><code>PermitEmptyPasswords</code></p>
<dd>When password authentication is allowed, it specifies whether the server allows login to accounts with empty password strings. The default is <code>no</code></p>
<dt><code>PermitListen</code></p>
<dd>Specifies the addresses/ports on which a remote TCP port forwarding may listen. The listen specification must be one of the following forms: </p>
<dt><code>PermitListen</code></p>
<dd><i>port</i></p>
<dt><code>PermitListen</code></p>
<dd><i>host : port</i></dl>
<p> Multiple permissions may be specified by separating them with whitespace. An argument of <code>any</code> can be used to remove all restrictions and permit any listen requests. An argument of <code>none</code> can be used to prohibit all listen requests. The host name may contain wildcards as described in the PATTERNS section in ssh_config5. The wildcard `*&#8217; can also be used in place of a port number to allow all ports. By default all port forwarding listen requests are permitted. Note that the <code>GatewayPorts</code> option may further restrict which addresses may be listened on. Note also that <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will request a listen host of &#8220;localhost&#8221; if no listen host was specifically requested, and this name is treated differently to explicit localhost addresses of &#8220;127.0.0.1&#8221; and &#8220;::1&#8221;</p>
<dt><code>PermitOpen</code></p>
<dd>Specifies the destinations to which TCP port forwarding is permitted. The forwarding specification must be one of the following forms: </p>
<dt><code>PermitOpen</code></p>
<dd><i>host : port</i></p>
<dt><code>PermitOpen</code></p>
<dd><i>IPv4_addr : port</i></p>
<dt><code>PermitOpen</code></p>
<dd><i>[ IPv6_addr ] : port</i></dl>
<p> Multiple forwards may be specified by separating them with whitespace. An argument of <code>any</code> can be used to remove all restrictions and permit any forwarding requests. An argument of <code>none</code> can be used to prohibit all forwarding requests. The wildcard `*&#8217; can be used for host or port to allow all hosts or ports respectively. Otherwise, no pattern matching or address lookups are performed on supplied names. By default all port forwarding requests are permitted.</p>
<dt><code>PermitRootLogin</code></p>
<dd>Specifies whether root can log in using <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The argument must be <code>yes</code> <code>prohibit-password</code> <code>forced-commands-only</code> or <code>no</code> The default is <code>prohibit-password</code> If this option is set to <code>prohibit-password</code> (or its deprecated alias, <code>without-password )</code> password and keyboard-interactive authentication are disabled for root. If this option is set to <code>forced-commands-only</code> root login with public key authentication will be allowed, but only if the <i>command</i> option has been specified (which may be useful for taking remote backups even if root login is normally not allowed). All other authentication methods are disabled for root. If this option is set to <code>no</code> root is not allowed to log in.</p>
<dt><code>PermitTTY</code></p>
<dd>Specifies whether <a href="/docs/linux/man/4-pty/">pty</a>(4) allocation is permitted. The default is <code>yes</code></p>
<dt><code>PermitTunnel</code></p>
<dd>Specifies whether <a href="/docs/linux/man/4-tun/">tun</a>(4) device forwarding is allowed. The argument must be <code>yes</code> <code>point-to-point</code> (layer 3), <code>ethernet</code> (layer 2), or <code>no</code> Specifying <code>yes</code> permits both <code>point-to-point</code> and <code>ethernet</code> The default is <code>no</code> Independent of this setting, the permissions of the selected <a href="/docs/linux/man/4-tun/">tun</a>(4) device must allow access to the user.</p>
<dt><code>PermitUserEnvironment</code></p>
<dd>Specifies whether ~/.ssh/environment and <code>environment=</code> options in ~/.ssh/authorized_keys are processed by <a href="/docs/linux/man/8-sshd/">sshd</a>(8). Valid options are <code>yes</code> <code>no</code> or a pattern-list specifying which environment variable names to accept (for example Qq LANG,LC_* ) . The default is <code>no</code> Enabling environment processing may enable users to bypass access restrictions in some configurations using mechanisms such as <code>LD_PRELOAD</code></p>
<dt><code>PermitUserRC</code></p>
<dd>Specifies whether any ~/.ssh/rc file is executed. The default is <code>yes</code></p>
<dt><code>PerSourceMaxStartups</code></p>
<dd>Specifies the number of unauthenticated connections allowed from a given source address, or &#8220;none&#8221; if there is no limit. This limit is applied in addition to <code>MaxStartups</code> whichever is lower. The default is <code>none</code></p>
<dt><code>PerSourceNetBlockSize</code></p>
<dd>Specifies the number of bits of source address that are grouped together for the purposes of applying PerSourceMaxStartups limits. Values for IPv4 and optionally IPv6 may be specified, separated by a colon. The default is <code>32:128</code> which means each address is considered individually.</p>
<dt><code>PidFile</code></p>
<dd>Specifies the file that contains the process ID of the SSH daemon, or <code>none</code> to not write one. The default is /run/sshd.pid</p>
<dt><code>Port</code></p>
<dd>Specifies the port number that <a href="/docs/linux/man/8-sshd/">sshd</a>(8) listens on. The default is 22. Multiple options of this type are permitted. See also <code>ListenAddress</code></p>
<dt><code>PrintLastLog</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should print the date and time of the last user login when a user logs in interactively. The default is <code>yes</code></p>
<dt><code>PrintMotd</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should print /etc/motd when a user logs in interactively. (On some systems it is also printed by the shell, /etc/profile or equivalent.) The default is <code>yes</code></p>
<dt><code>PubkeyAcceptedAlgorithms</code></p>
<dd>Specifies the signature algorithms that will be accepted for public key authentication as a list of comma-separated patterns. Alternately if the specified list begins with a `+&#8217; character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified algorithms will be placed at the head of the default set. The default for this option is: </p>
<pre>ssh-ed25519-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp256-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp384-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp521-cert-v01 [at] openssh.com,
sk-ssh-ed25519-cert-v01 [at] openssh.com,
sk-ecdsa-sha2-nistp256-cert-v01 [at] openssh.com,
rsa-sha2-512-cert-v01 [at] openssh.com,
rsa-sha2-256-cert-v01 [at] openssh.com,
ssh-ed25519,
ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519 [at] openssh.com,
sk-ecdsa-sha2-nistp256 [at] openssh.com,
rsa-sha2-512,rsa-sha2-256</pre>
<p>The list of available signature algorithms may also be obtained using Qq ssh -Q PubkeyAcceptedAlgorithms .</p>
<dt><code>PubkeyAuthOptions</code></p>
<dd>Sets one or more public key authentication options. The supported keywords are: <code>none</code> (the default; indicating no additional options are enabled), <code>touch-required</code> and <code>verify-required</code> The <code>touch-required</code> option causes public key authentication using a FIDO authenticator algorithm (i.e. <code>ecdsa-sk</code> or <code>ed25519-sk</code> to always require the signature to attest that a physically present user explicitly confirmed the authentication (usually by touching the authenticator). By default, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) requires user presence unless overridden with an authorized_keys option. The <code>touch-required</code> flag disables this override. The <code>verify-required</code> option requires a FIDO key signature attest that the user was verified, e.g. via a PIN. Neither the <code>touch-required</code> or <code>verify-required</code> options have any effect for other, non-FIDO, public key types.</p>
<dt><code>PubkeyAuthentication</code></p>
<dd>Specifies whether public key authentication is allowed. The default is <code>yes</code></p>
<dt><code>RekeyLimit</code></p>
<dd>Specifies the maximum amount of data that may be transmitted before the session key is renegotiated, optionally followed by a maximum amount of time that may pass before the session key is renegotiated. The first argument is specified in bytes and may have a suffix of `K&#8217; `M&#8217; or `G&#8217; to indicate Kilobytes, Megabytes, or Gigabytes, respectively. The default is between `1G&#8217; and `4G&#8217; depending on the cipher. The optional second value is specified in seconds and may use any of the units documented in the Sx TIME FORMATS section. The default value for <code>RekeyLimit</code> is <code>default none</code> which means that rekeying is performed after the cipher&#8217;s default amount of data has been sent or received and no time based rekeying is done.</p>
<dt><code>RevokedKeys</code></p>
<dd>Specifies revoked public keys file, or <code>none</code> to not use one. Keys listed in this file will be refused for public key authentication. Note that if this file is not readable, then public key authentication will be refused for all users. Keys may be specified as a text file, listing one public key per line, or as an OpenSSH Key Revocation List (KRL) as generated by ssh-keygen1. For more information on KRLs, see the KEY REVOCATION LISTS section in ssh-keygen1.</p>
<dt><code>SecurityKeyProvider</code></p>
<dd>Specifies a path to a library that will be used when loading FIDO authenticator-hosted keys, overriding the default of using the built-in USB HID support.</p>
<dt><code>SetEnv</code></p>
<dd>Specifies one or more environment variables to set in child sessions started by <a href="/docs/linux/man/8-sshd/">sshd</a>(8) as &#8220;NAME=VALUE&#8221; The environment value may be quoted (e.g. if it contains whitespace characters). Environment variables set by <code>SetEnv</code> override the default environment and any variables specified by the user via <code>AcceptEnv</code> or <code>PermitUserEnvironment</code></p>
<dt><code>StreamLocalBindMask</code></p>
<dd>Sets the octal file creation mode mask (umask) used when creating a Unix-domain socket file for local or remote port forwarding. This option is only used for port forwarding to a Unix-domain socket file. The default value is 0177, which creates a Unix-domain socket file that is readable and writable only by the owner. Note that not all operating systems honor the file mode on Unix-domain socket files.</p>
<dt><code>StreamLocalBindUnlink</code></p>
<dd>Specifies whether to remove an existing Unix-domain socket file for local or remote port forwarding before creating a new one. If the socket file already exists and <code>StreamLocalBindUnlink</code> is not enabled, <code>sshd</code> will be unable to forward the port to the Unix-domain socket file. This option is only used for port forwarding to a Unix-domain socket file. The argument must be <code>yes</code> or <code>no</code> The default is <code>no</code></p>
<dt><code>StrictModes</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should check file modes and ownership of the user&#8217;s files and home directory before accepting login. This is normally desirable because novices sometimes accidentally leave their directory or files world-writable. The default is <code>yes</code> Note that this does not apply to <code>ChrootDirectory</code> whose permissions and ownership are checked unconditionally.</p>
<dt><code>Subsystem</code></p>
<dd>Configures an external subsystem (e.g. file transfer daemon). Arguments should be a subsystem name and a command (with optional arguments) to execute upon subsystem request. The command <code>sftp-server</code> implements the SFTP file transfer subsystem. Alternately the name <code>internal-sftp</code> implements an in-process SFTP server. This may simplify configurations using <code>ChrootDirectory</code> to force a different filesystem root on clients. By default no subsystems are defined.</p>
<dt><code>SyslogFacility</code></p>
<dd>Gives the facility code that is used when logging messages from <a href="/docs/linux/man/8-sshd/">sshd</a>(8). The possible values are: DAEMON, USER, AUTH, LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7. The default is AUTH.</p>
<dt><code>TCPKeepAlive</code></p>
<dd>Specifies whether the system should send TCP keepalive messages to the other side. If they are sent, death of the connection or crash of one of the machines will be properly noticed. However, this means that connections will die if the route is down temporarily, and some people find it annoying. On the other hand, if TCP keepalives are not sent, sessions may hang indefinitely on the server, leaving Qq ghost users and consuming server resources. The default is <code>yes</code> (to send TCP keepalive messages), and the server will notice if the network goes down or the client host crashes. This avoids infinitely hanging sessions. To disable TCP keepalive messages, the value should be set to <code>no</code> This option was formerly called <code>KeepAlive</code></p>
<dt><code>TrustedUserCAKeys</code></p>
<dd>Specifies a file containing public keys of certificate authorities that are trusted to sign user certificates for authentication, or <code>none</code> to not use one. Keys are listed one per line; empty lines and comments starting with `#&#8217; are allowed. If a certificate is presented for authentication and has its signing CA key listed in this file, then it may be used for authentication for any user listed in the certificate&#8217;s principals list. Note that certificates that lack a list of principals will not be permitted for authentication using <code>TrustedUserCAKeys</code> For more details on certificates, see the CERTIFICATES section in ssh-keygen1.</p>
<dt><code>UseDNS</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should look up the remote host name, and to check that the resolved host name for the remote IP address maps back to the very same IP address. If this option is set to <code>no</code> (the default) then only addresses and not host names may be used in ~/.ssh/authorized_keys <code>from</code> and <code>sshd_config</code> <code>Match</code> <code>Host</code> directives.</p>
<dt><code>UsePAM</code></p>
<dd>Enables the Pluggable Authentication Module interface. If set to <code>yes</code> this will enable PAM authentication using <code>KbdInteractiveAuthentication</code> and <code>PasswordAuthentication</code> in addition to PAM account and session module processing for all authentication types. Because PAM keyboard-interactive authentication usually serves an equivalent role to password authentication, you should disable either <code>PasswordAuthentication</code> or <code>KbdInteractiveAuthentication</code> If <code>UsePAM</code> is enabled, you will not be able to run <a href="/docs/linux/man/8-sshd/">sshd</a>(8) as a non-root user. The default is <code>no</code></p>
<dt><code>VersionAddendum</code></p>
<dd>Optionally specifies additional text to append to the SSH protocol banner sent by the server upon connection. The default is <code>none</code></p>
<dt><code>X11DisplayOffset</code></p>
<dd>Specifies the first display number available for <a href="/docs/linux/man/8-sshd/">sshd</a>(8)Ns&#8217;s X11 forwarding. This prevents sshd from interfering with real X11 servers. The default is 10.</p>
<dt><code>X11Forwarding</code></p>
<dd>Specifies whether X11 forwarding is permitted. The argument must be <code>yes</code> or <code>no</code> The default is <code>no</code> When X11 forwarding is enabled, there may be additional exposure to the server and to client displays if the <a href="/docs/linux/man/8-sshd/">sshd</a>(8) proxy display is configured to listen on the wildcard address (see <code>X11UseLocalhost )</code> though this is not the default. Additionally, the authentication spoofing and authentication data verification and substitution occur on the client side. The security risk of using X11 forwarding is that the client&#8217;s X11 display server may be exposed to attack when the SSH client requests forwarding (see the warnings for <code>ForwardX11</code> in ssh_config5). A system administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a <code>no</code> setting. Note that disabling X11 forwarding does not prevent users from forwarding X11 traffic, as users can always install their own forwarders.</p>
<dt><code>X11UseLocalhost</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should bind the X11 forwarding server to the loopback address or to the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the <code>DISPLAY</code> environment variable to <code>localhost</code> This prevents remote hosts from connecting to the proxy display. However, some older X11 clients may not function with this configuration. <code>X11UseLocalhost</code> may be set to <code>no</code> to specify that the forwarding server should be bound to the wildcard address. The argument must be <code>yes</code> or <code>no</code> The default is <code>yes</code></p>
<dt><code>XAuthLocation</code></p>
<dd>Specifies the full pathname of the <a href="/docs/linux/man/1-xauth/">xauth</a>(1) program, or <code>none</code> to not use one. The default is /usr/bin/xauth</dl>
<h2>Time Formats</h2>
<p><a href="/docs/linux/man/8-sshd/">sshd</a>(8) command-line arguments and configuration file options that specify time may be expressed using a sequence of the form: <i>time </i>[<i>qualifier</i> ] where <i>time</i> is a positive integer value and <i>qualifier</i> is one of the following: </p>
<dl>
<dt><code>Aq </code><code>none</code></p>
<dd>seconds</p>
<dt><code>s | S</code></p>
<dd>seconds</p>
<dt><code>m | M</code></p>
<dd>minutes</p>
<dt><code>h | H</code></p>
<dd>hours</p>
<dt><code>d | D</code></p>
<dd>days</p>
<dt><code>w | W</code></p>
<dd>weeks</dl>
<p> Each member of the sequence is added together to calculate the total time value. </p>
<p> Time format examples: </p>
<dl>
<dt><code>600</code></p>
<dd>600 seconds (10 minutes)</p>
<dt><code>10m</code></p>
<dd>10 minutes</p>
<dt><code>1h30m</code></p>
<dd>1 hour 30 minutes (90 minutes)</dl>
<h2>Tokens</h2>
<p>Arguments to some keywords can make use of tokens, which are expanded at runtime: </p>
<dl>
<dt><code>%%</code></p>
<dd>A literal `%&#8217;</p>
<dt><code>%F</code></p>
<dd>The fingerprint of the CA key.</p>
<dt><code>%f</code></p>
<dd>The fingerprint of the key or certificate.</p>
<dt><code>%h</code></p>
<dd>The home directory of the user.</p>
<dt><code>%i</code></p>
<dd>The key ID in the certificate.</p>
<dt><code>%K</code></p>
<dd>The base64-encoded CA key.</p>
<dt><code>%k</code></p>
<dd>The base64-encoded key or certificate for authentication.</p>
<dt><code>%s</code></p>
<dd>The serial number of the certificate.</p>
<dt><code>%T</code></p>
<dd>The type of the CA key.</p>
<dt><code>%t</code></p>
<dd>The key or certificate type.</p>
<dt><code>%U</code></p>
<dd>The numeric user ID of the target user.</p>
<dt><code>%u</code></p>
<dd>The username.</dl>
<p> <code>AuthorizedKeysCommand</code> accepts the tokens %%, %f, %h, %k, %t, %U, and %u. </p>
<p> <code>AuthorizedKeysFile</code> accepts the tokens %%, %h, %U, and %u. </p>
<p> <code>AuthorizedPrincipalsCommand</code> accepts the tokens %%, %F, %f, %h, %i, %K, %k, %s, %T, %t, %U, and %u. </p>
<p> <code>AuthorizedPrincipalsFile</code> accepts the tokens %%, %h, %U, and %u. </p>
<p> <code>ChrootDirectory</code> accepts the tokens %%, %h, %U, and %u.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/ssh/sshd_config </code></p>
<dd>Contains configuration data for <a href="/docs/linux/man/8-sshd/">sshd</a>(8). This file should be writable by root only, but it is recommended (though not necessary) that it be world-readable.</dl>
<h2>See Also</h2>
<p>sftp-server8, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>Authors</h2>
<p>An -nosplit OpenSSH is a derivative of the original and free ssh 1.2.12 release by An Tatu Ylonen . An Aaron Campbell , Bob Beck , Markus Friedl , Niels Provos , An Theo de Raadt and An Dug Song removed many bugs, re-added newer features and created OpenSSH. An Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. An Niels Provos and An Markus Friedl contributed support for privilege separation.</p>
