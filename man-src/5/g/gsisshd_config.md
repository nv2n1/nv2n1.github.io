---
title: "gsisshd_config(5)"
name: "gsisshd_config"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gsisshd_config/"
description: "sshd_config – OpenSSH SSH daemon configuration file"
---

<p><code>sshd_config</code> &#8211; OpenSSH SSH daemon configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/gsissh/sshd_config</code></p>
<h2>Description</h2>
<p><a href="/docs/linux/man/8-sshd/">sshd</a>(8) reads configuration data from /etc/gsissh/sshd_config (or the file specified with &#8211;<code>f</code> on the command line). The file contains keyword-argument pairs, one per line. Lines starting with `#&#8217; and empty lines are interpreted as comments. Arguments may optionally be enclosed in double quotes () in order to represent arguments containing spaces. The possible keywords and their meanings are as follows (note that keywords are case-insensitive and arguments are case-sensitive):</p>
<dl>
<dt><code>AcceptEnv</code></p>
<dd>Specifies what environment variables sent by the client will be copied into the session&#8217;s <a href="/docs/linux/man/7-environ/">environ</a>(7). See <code>SendEnv</code> in ssh_config5 for how to configure the client. Note that environment passing is only supported for protocol 2, and that the <code>TERM</code> environment variable is always sent whenever the client requests a pseudo-terminal as it is required by the protocol. Variables are specified by name, which may contain the wildcard characters `*&#8217; and `?&#8217; Multiple environment variables may be separated by whitespace or spread across multiple <code>AcceptEnv</code> directives. Be warned that some environment variables could be used to bypass restricted user environments. For this reason, care should be taken in the use of this directive. The default is not to accept any environment variables.</p>
<dt><code>AddressFamily</code></p>
<dd>Specifies which address family should be used by <a href="/docs/linux/man/8-sshd/">sshd</a>(8). Valid arguments are &#8220;any&#8221; &#8220;inet&#8221; (use IPv4 only), or &#8220;inet6&#8221; (use IPv6 only). The default is &#8220;any&#8221;</p>
<dt><code>AllowAgentForwarding</code></p>
<dd>Specifies whether ssh-agent1 forwarding is permitted. The default is &#8220;yes&#8221; Note that disabling agent forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.</p>
<dt><code>AllowGroups</code></p>
<dd>This keyword can be followed by a list of group name patterns, separated by spaces. If specified, login is allowed only for users whose primary group or supplementary group list matches one of the patterns. Only group names are valid; a numerical group ID is not recognized. By default, login is allowed for all groups. The allow/deny directives are processed in the following order: <code>DenyUsers</code> <code>AllowUsers</code> <code>DenyGroups</code> and finally <code>AllowGroups</code> All of the specified user and group tests must succeed, before user is allowed to log in. See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>AllowTcpForwarding</code></p>
<dd>Specifies whether TCP forwarding is permitted. The available options are &#8220;yes&#8221; or &#8220;all&#8221; to allow TCP forwarding, &#8220;no&#8221; to prevent all TCP forwarding, &#8220;local&#8221; to allow local (from the perspective of <a href="/docs/linux/man/1-ssh/">ssh</a>(1)) forwarding only or &#8220;remote&#8221; to allow remote forwarding only. The default is &#8220;yes&#8221; Note that disabling TCP forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.</p>
<dt><code>AllowUsers</code></p>
<dd>This keyword can be followed by a list of user name patterns, separated by spaces. If specified, login is allowed only for user names that match one of the patterns. Only user names are valid; a numerical user ID is not recognized. By default, login is allowed for all users. If the pattern takes the form USER [at] HOST then USER and HOST are separately checked, restricting logins to particular users from particular hosts. The allow/deny directives are processed in the following order: <code>DenyUsers</code> <code>AllowUsers</code> <code>DenyGroups</code> and finally <code>AllowGroups</code> All of the specified user and group tests must succeed, before user is allowed to log in. See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>AuthenticationMethods</code></p>
<dd>Specifies the authentication methods that must be successfully completed for a user to be granted access. This option must be followed by one or more comma-separated lists of authentication method names, or by the single string &#8220;any&#8221; to indicate the default behaviour of accepting any single authentication method. if the default is overridden, then successful authentication requires completion of every method in at least one of these lists. For example, an argument of &#8220;publickey,password publickey,keyboard-interactive&#8221; would require the user to complete public key authentication, followed by either password or keyboard interactive authentication. Only methods that are next in one or more lists are offered at each stage, so for this example, it would not be possible to attempt password or keyboard-interactive authentication before public key. For keyboard interactive authentication it is also possible to restrict authentication to a specific device by appending a colon followed by the device identifier &#8220;bsdauth&#8221; &#8220;pam&#8221; or &#8220;skey&#8221; depending on the server configuration. For example, &#8220;keyboard-interactive:bsdauth&#8221; would restrict keyboard interactive authentication to the &#8220;bsdauth&#8221; device. This option is only available for SSH protocol 2 and will yield a fatal error if enabled if protocol 1 is also enabled. Note that each authentication method listed should also be explicitly enabled in the configuration. The default &#8220;any&#8221; is not to require multiple authentication; successful completion of a single authentication method is sufficient.</p>
<dt><code>AuthorizedKeysCommand</code></p>
<dd>Specifies a program to be used to look up the user&#8217;s public keys. The program must be owned by root and not writable by group or others. It will be invoked with a single argument of the username being authenticated, and should produce on standard output zero or more lines of authorized_keys output (see AUTHORIZED_KEYS in <a href="/docs/linux/man/8-sshd/">sshd</a>(8)). If a key supplied by AuthorizedKeysCommand does not successfully authenticate and authorize the user then public key authentication continues using the usual <code>AuthorizedKeysFile</code> files. By default, no AuthorizedKeysCommand is run.</p>
<dt><code>AuthorizedKeysCommandUser</code></p>
<dd>Specifies the user under whose account the AuthorizedKeysCommand is run. It is recommended to use a dedicated user that has no other role on the host than running authorized keys commands.</p>
<dt><code>AuthorizedKeysFile</code></p>
<dd>Specifies the file that contains the public keys that can be used for user authentication. The format is described in the AUTHORIZED_KEYS FILE FORMAT section of <a href="/docs/linux/man/8-sshd/">sshd</a>(8). <code>AuthorizedKeysFile</code> may contain tokens of the form %T which are substituted during connection setup. The following tokens are defined: %% is replaced by a literal &#8216;%&#8217;, %h is replaced by the home directory of the user being authenticated, and %u is replaced by the username of that user. After expansion, <code>AuthorizedKeysFile</code> is taken to be an absolute path or one relative to the user&#8217;s home directory. Multiple files may be listed, separated by whitespace. The default is &#8220;.ssh/authorized_keys .ssh/authorized_keys2&#8221;</p>
<dt><code>AuthorizedPrincipalsFile</code></p>
<dd>Specifies a file that lists principal names that are accepted for certificate authentication. When using certificates signed by a key listed in <code>TrustedUserCAKeys</code> this file lists names, one of which must appear in the certificate for it to be accepted for authentication. Names are listed one per line preceded by key options (as described in AUTHORIZED_KEYS FILE FORMAT in <a href="/docs/linux/man/8-sshd/">sshd</a>(8)). Empty lines and comments starting with `#&#8217; are ignored. <code>AuthorizedPrincipalsFile</code> may contain tokens of the form %T which are substituted during connection setup. The following tokens are defined: %% is replaced by a literal &#8216;%&#8217;, %h is replaced by the home directory of the user being authenticated, and %u is replaced by the username of that user. After expansion, <code>AuthorizedPrincipalsFile</code> is taken to be an absolute path or one relative to the user&#8217;s home directory. The default is &#8220;none&#8221; i.e. not to use a principals file &#8211; in this case, the username of the user must appear in a certificate&#8217;s principals list for it to be accepted. Note that <code>AuthorizedPrincipalsFile</code> is only used when authentication proceeds using a CA listed in <code>TrustedUserCAKeys</code> and is not consulted for certification authorities trusted via ~/.ssh/authorized_keys though the <code>principals=</code> key option offers a similar facility (see <a href="/docs/linux/man/8-sshd/">sshd</a>(8) for details).</p>
<dt><code>Banner</code></p>
<dd>The contents of the specified file are sent to the remote user before authentication is allowed. If the argument is &#8220;none&#8221; then no banner is displayed. This option is only available for protocol version 2. By default, no banner is displayed.</p>
<dt><code>ChallengeResponseAuthentication</code></p>
<dd>Specifies whether challenge-response authentication is allowed (e.g. via PAM or though authentication styles supported in login.conf5) The default is &#8220;yes&#8221;</p>
<dt><code>ChrootDirectory</code></p>
<dd>Specifies the pathname of a directory to <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to after authentication. All components of the pathname must be root-owned directories that are not writable by any other user or group. After the chroot, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) changes the working directory to the user&#8217;s home directory. The pathname may contain the following tokens that are expanded at runtime once the connecting user has been authenticated: %% is replaced by a literal &#8216;%&#8217;, %h is replaced by the home directory of the user being authenticated, and %u is replaced by the username of that user. The <code>ChrootDirectory</code> must contain the necessary files and directories to support the user&#8217;s session. For an interactive session this requires at least a shell, typically <a href="/docs/linux/man/1-sh/">sh</a>(1), and basic /dev nodes such as <a href="/docs/linux/man/4-null/">null</a>(4), <a href="/docs/linux/man/4-zero/">zero</a>(4), <a href="/docs/linux/man/4-stdin/">stdin</a>(4), <a href="/docs/linux/man/4-stdout/">stdout</a>(4), <a href="/docs/linux/man/4-stderr/">stderr</a>(4), <a href="/docs/linux/man/4-arandom/">arandom</a>(4) and <a href="/docs/linux/man/4-tty/">tty</a>(4) devices. For file transfer sessions using &#8220;sftp&#8221; no additional configuration of the environment is necessary if the in-process sftp server is used, though sessions which use logging do require /dev/log inside the chroot directory (see sftp-server8 for details). The default is not to <a href="/docs/linux/man/2-chroot/">chroot</a>(2).</p>
<dt><code>Ciphers</code></p>
<dd>Specifies the ciphers allowed for protocol version 2. Multiple ciphers must be comma-separated. The supported ciphers are: &#8220;3des-cbc&#8221; &#8220;aes128-cbc&#8221; &#8220;aes192-cbc&#8221; &#8220;aes256-cbc&#8221; &#8220;aes128-ctr&#8221; &#8220;aes192-ctr&#8221; &#8220;aes256-ctr&#8221; &#8220;aes128-gcm [at] openssh.com&#8221; &#8220;aes256-gcm [at] openssh.com&#8221; &#8220;arcfour128&#8221; &#8220;arcfour256&#8221; &#8220;arcfour&#8221; &#8220;blowfish-cbc&#8221; &#8220;cast128-cbc&#8221; and &#8220;chacha20-poly1305 [at] openssh.com&#8221; The default is: </p>
<pre>aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,
aes128-gcm [at] openssh.com,aes256-gcm [at] openssh.com,
chacha20-poly1305 [at] openssh.com,
aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,aes192-cbc,
aes256-cbc,arcfour</pre>
<p>The list of available ciphers may also be obtained using the &#8211;<code>Q</code> option of <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>ClientAliveCountMax</code></p>
<dd>Sets the number of client alive messages (see below) which may be sent without <a href="/docs/linux/man/8-sshd/">sshd</a>(8) receiving any messages back from the client. If this threshold is reached while client alive messages are being sent, sshd will disconnect the client, terminating the session. It is important to note that the use of client alive messages is very different from <code>TCPKeepAlive</code> (below). The client alive messages are sent through the encrypted channel and therefore will not be spoofable. The TCP keepalive option enabled by <code>TCPKeepAlive</code> is spoofable. The client alive mechanism is valuable when the client or server depend on knowing when a connection has become inactive. The default value is 3. If <code>ClientAliveInterval</code> (see below) is set to 15, and <code>ClientAliveCountMax</code> is left at the default, unresponsive SSH clients will be disconnected after approximately 45 seconds. This option applies to protocol version 2 only.</p>
<dt><code>ClientAliveInterval</code></p>
<dd>Sets a timeout interval in seconds after which if no data has been received from the client, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will send a message through the encrypted channel to request a response from the client. The default is 0, indicating that these messages will not be sent to the client. This option applies to protocol version 2 only.</p>
<dt><code>Compression</code></p>
<dd>Specifies whether compression is allowed, or delayed until the user has authenticated successfully. The argument must be &#8220;yes&#8221; &#8220;delayed&#8221; or &#8220;no&#8221; The default is &#8220;delayed&#8221;</p>
<dt><code>DenyGroups</code></p>
<dd>This keyword can be followed by a list of group name patterns, separated by spaces. Login is disallowed for users whose primary group or supplementary group list matches one of the patterns. Only group names are valid; a numerical group ID is not recognized. By default, login is allowed for all groups. The allow/deny directives are processed in the following order: <code>DenyUsers</code> <code>AllowUsers</code> <code>DenyGroups</code> and finally <code>AllowGroups</code> All of the specified user and group tests must succeed, before user is allowed to log in. See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>DenyUsers</code></p>
<dd>This keyword can be followed by a list of user name patterns, separated by spaces. Login is disallowed for user names that match one of the patterns. Only user names are valid; a numerical user ID is not recognized. By default, login is allowed for all users. If the pattern takes the form USER [at] HOST then USER and HOST are separately checked, restricting logins to particular users from particular hosts. The allow/deny directives are processed in the following order: <code>DenyUsers</code> <code>AllowUsers</code> <code>DenyGroups</code> and finally <code>AllowGroups</code> All of the specified user and group tests must succeed, before user is allowed to log in. See PATTERNS in ssh_config5 for more information on patterns.</p>
<dt><code>DisableUsageStats</code></p>
<dd>This keyword can be followed by &quot;yes&quot; to disable reporting of usage metrics. Or it can be set to &quot;no&quot; to enable reporting of usage metrics. Setting the <code>GLOBUS_USAGE_OPTOUT</code> environment variable to &quot;1&quot; will also disable the reporting of usage metrics. Disabling reporting of usage metrics will cause the <code>UsageStatsTargets</code> setting to be ignored.</p>
<dt><code>ExposeAuthenticationMethods</code></p>
<dd>When using SSH2, this option controls the exposure of the list of successful authentication methods to PAM during the authentication and to the shell environment via the <code>SSH_USER_AUTH</code> variable. See the description of this variable for more details. Valid options are: &#8220;never&#8221; (Do not expose successful authentication methods), &#8220;pam-only&#8221; (Only expose them to PAM during authentication, not afterwards), &#8220;pam-and-env&#8221; (Expose them to PAM and keep them in the shell environment). The default is &#8220;never&#8221;</p>
<dt><code>ForceCommand</code></p>
<dd>Forces the execution of the command specified by <code>ForceCommand</code> ignoring any command supplied by the client and ~/.ssh/rc if present. The command is invoked by using the user&#8217;s login shell with the -c option. This applies to shell, command, or subsystem execution. It is most useful inside a <code>Match</code> block. The command originally supplied by the client is available in the <code>SSH_ORIGINAL_COMMAND</code> environment variable. Specifying a command of &#8220;internal-sftp&#8221; will force the use of an in-process sftp server that requires no support files when used with <code>ChrootDirectory</code></p>
<dt><code>GatewayPorts</code></p>
<dd>Specifies whether remote hosts are allowed to connect to ports forwarded for the client. By default, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) binds remote port forwardings to the loopback address. This prevents other remote hosts from connecting to forwarded ports. <code>GatewayPorts</code> can be used to specify that sshd should allow remote port forwardings to bind to non-loopback addresses, thus allowing other hosts to connect. The argument may be &#8220;no&#8221; to force remote port forwardings to be available to the local host only, &#8220;yes&#8221; to force remote port forwardings to bind to the wildcard address, or &#8220;clientspecified&#8221; to allow the client to select the address to which the forwarding is bound. The default is &#8220;no&#8221;</p>
<dt><code>GSSAPIAuthentication</code></p>
<dd>Specifies whether user authentication based on GSSAPI is allowed. The default is &#8220;yes&#8221; Note that this option applies to protocol version 2 only.</p>
<dt><code>GSSAPIDelegateCredentials</code></p>
<dd>Specifies whether delegated credentials are stored in the user&#8217;s environment. The default is &#8220;yes&#8221;</p>
<dt><code>GSSAPIKeyExchange</code></p>
<dd>Specifies whether key exchange based on GSSAPI is allowed. GSSAPI key exchange doesn&#8217;t rely on ssh keys to verify host identity. The default is &#8220;yes&#8221; Note that this option applies to protocol version 2 only.</p>
<dt><code>GSSAPICleanupCredentials</code></p>
<dd>Specifies whether to automatically destroy the user&#8217;s credentials cache on logout. The default is &#8220;yes&#8221; Note that this option applies to protocol version 2 only.</p>
<dt><code>GSSAPICredentialsPath</code></p>
<dd>If specified, the delegated GSSAPI credential is stored in the given path, overwriting any existing credentials. Paths can be specified with syntax similar to the AuthorizedKeysFile option (i.e., accepting %h and %u tokens). When using this option, setting &#8216;GssapiCleanupCredentials no&#8217; is recommended, so logging out of one session doesn&#8217;t remove the credentials in use by another session of the same user. Currently only implemented for the GSI mechanism.</p>
<dt><code>GSIAllowLimitedProxy</code></p>
<dd>Specifies whether to accept limited proxy credentials for authentication. The default is &#8220;no&#8221;</p>
<dt><code>GSSAPIEnablek5users</code></p>
<dd>Specifies whether to look at .k5users file for GSSAPI authentication access control. Further details are described in <a href="/docs/linux/man/1-ksu/">ksu</a>(1). The default is &#8220;no&#8221;</p>
<dt><code>GSSAPIStrictAcceptorCheck</code></p>
<dd>Determines whether to be strict about the identity of the GSSAPI acceptor a client authenticates against. If &#8220;yes&#8221; then the client must authenticate against the host service on the current hostname. If &#8220;no&#8221; then the client may authenticate against any service key stored in the machine&#8217;s default store. This facility is provided to assist with operation on multi homed machines. The default is &#8220;yes&#8221; Note that this option applies only to protocol version 2 GSSAPI connections, and setting it to &#8220;no&#8221; may only work with recent Kerberos GSSAPI libraries.</p>
<dt><code>GSSAPIStoreCredentialsOnRekey</code></p>
<dd>Controls whether the user&#8217;s GSSAPI credentials should be updated following a successful connection rekeying. This option can be used to accepted renewed or updated credentials from a compatible client. The default is &#8220;no&#8221;</p>
<dt><code>GSSAPIKexAlgorithms</code></p>
<dd>The list of key exchange algorithms that are accepted by GSSAPI key exchange. Possible values are </p>
<pre>gss-gex-sha1-,
gss-group1-sha1-,
gss-group14-sha1-</pre>
<p>The default is &#8220;gss-gex-sha1-,gss-group1-sha1-,gss-group14-sha1-&#8221; This option only applies to protocol version 2 connections using GSSAPI.</p>
<dt><code>HostbasedAuthentication</code></p>
<dd>Specifies whether rhosts or /etc/hosts.equiv authentication together with successful public key client host authentication is allowed (host-based authentication). This option is similar to <code>RhostsRSAAuthentication</code> and applies to protocol version 2 only. The default is &#8220;no&#8221;</p>
<dt><code>HostbasedUsesNameFromPacketOnly</code></p>
<dd>Specifies whether or not the server will attempt to perform a reverse name lookup when matching the name in the ~/.shosts ~/.rhosts and /etc/hosts.equiv files during <code>HostbasedAuthentication</code> A setting of &#8220;yes&#8221; means that <a href="/docs/linux/man/8-sshd/">sshd</a>(8) uses the name supplied by the client rather than attempting to resolve the name from the TCP connection itself. The default is &#8220;no&#8221;</p>
<dt><code>HostCertificate</code></p>
<dd>Specifies a file containing a public host certificate. The certificate&#8217;s public key must match a private host key already specified by <code>HostKey</code> The default behaviour of <a href="/docs/linux/man/8-sshd/">sshd</a>(8) is not to load any certificates.</p>
<dt><code>HostKey</code></p>
<dd>Specifies a file containing a private host key used by SSH. The default is /etc/gsissh/ssh_host_key for protocol version 1, and /etc/gsissh/ssh_host_dsa_key /etc/gsissh/ssh_host_ecdsa_key /etc/gsissh/ssh_host_ed25519_key and /etc/gsissh/ssh_host_rsa_key for protocol version 2. Note that <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will refuse to use a file if it is group/world-accessible. It is possible to have multiple host key files. &#8220;rsa1&#8221; keys are used for version 1 and &#8220;dsa&#8221; &#8220;ecdsa&#8221; &#8220;ed25519&#8221; or &#8220;rsa&#8221; are used for version 2 of the SSH protocol. It is also possible to specify public host key files instead. In this case operations on the private key will be delegated to an ssh-agent1.</p>
<dt><code>HostKeyAgent</code></p>
<dd>Identifies the UNIX-domain socket used to communicate with an agent that has access to the private host keys. If &#8220;SSH_AUTH_SOCK&#8221; is specified, the location of the socket will be read from the <code>SSH_AUTH_SOCK</code> environment variable.</p>
<dt><code>IgnoreRhosts</code></p>
<dd>Specifies that .rhosts and .shosts files will not be used in <code>RhostsRSAAuthentication</code> or <code>HostbasedAuthentication</code> /etc/hosts.equiv and /etc/gsissh/shosts.equiv are still used. The default is &#8220;yes&#8221;</p>
<dt><code>IgnoreUserKnownHosts</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should ignore the user&#8217;s ~/.ssh/known_hosts during <code>RhostsRSAAuthentication</code> or <code>HostbasedAuthentication</code> The default is &#8220;no&#8221;</p>
<dt><code>IPQoS</code></p>
<dd>Specifies the IPv4 type-of-service or DSCP class for the connection. Accepted values are &#8220;af11&#8221; &#8220;af12&#8221; &#8220;af13&#8221; &#8220;af21&#8221; &#8220;af22&#8221; &#8220;af23&#8221; &#8220;af31&#8221; &#8220;af32&#8221; &#8220;af33&#8221; &#8220;af41&#8221; &#8220;af42&#8221; &#8220;af43&#8221; &#8220;cs0&#8221; &#8220;cs1&#8221; &#8220;cs2&#8221; &#8220;cs3&#8221; &#8220;cs4&#8221; &#8220;cs5&#8221; &#8220;cs6&#8221; &#8220;cs7&#8221; &#8220;ef&#8221; &#8220;lowdelay&#8221; &#8220;throughput&#8221; &#8220;reliability&#8221; or a numeric value. This option may take one or two arguments, separated by whitespace. If one argument is specified, it is used as the packet class unconditionally. If two values are specified, the first is automatically selected for interactive sessions and the second for non-interactive sessions. The default is &#8220;lowdelay&#8221; for interactive sessions and &#8220;throughput&#8221; for non-interactive sessions.</p>
<dt><code>KbdInteractiveAuthentication</code></p>
<dd>Specifies whether to allow keyboard-interactive authentication. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; The default is to use whatever value <code>ChallengeResponseAuthentication</code> is set to (by default &#8220;yes )&#8221;</p>
<dt><code>KerberosAuthentication</code></p>
<dd>Specifies whether the password provided by the user for <code>PasswordAuthentication</code> will be validated through the Kerberos KDC. To use this option, the server needs a Kerberos servtab which allows the verification of the KDC&#8217;s identity. The default is &#8220;no&#8221;</p>
<dt><code>KerberosGetAFSToken</code></p>
<dd>If AFS is active and the user has a Kerberos 5 TGT, attempt to acquire an AFS token before accessing the user&#8217;s home directory. The default is &#8220;no&#8221;</p>
<dt><code>KerberosOrLocalPasswd</code></p>
<dd>If password authentication through Kerberos fails then the password will be validated via any additional local mechanism such as /etc/passwd The default is &#8220;yes&#8221;</p>
<dt><code>KerberosTicketCleanup</code></p>
<dd>Specifies whether to automatically destroy the user&#8217;s ticket cache file on logout. The default is &#8220;yes&#8221;</p>
<dt><code>KerberosUseKuserok</code></p>
<dd>Specifies whether to look at .k5login file for user&#8217;s aliases. The default is &#8220;yes&#8221;</p>
<dt><code>KexAlgorithms</code></p>
<dd>Specifies the available KEX (Key Exchange) algorithms. Multiple algorithms must be comma-separated. The default is </p>
<blockquote>
<pre>curve25519-sha256 [at] libssh.org,
ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,
diffie-hellman-group-exchange-sha256,
diffie-hellman-group-exchange-sha1,
diffie-hellman-group14-sha1,
diffie-hellman-group1-sha1</pre>
</blockquote>
<dt><code>KeyRegenerationInterval</code></p>
<dd>In protocol version 1, the ephemeral server key is automatically regenerated after this many seconds (if it has been used). The purpose of regeneration is to prevent decrypting captured sessions by later breaking into the machine and stealing the keys. The key is never stored anywhere. If the value is 0, the key is never regenerated. The default is 3600 (seconds).</p>
<dt><code>ListenAddress</code></p>
<dd>Specifies the local addresses <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should listen on. The following forms may be used: </p>
<dt><code>ListenAddress</code></p>
<dd><i>host </i><code>| </code><i>IPv4_addr </i><code>| </code><i>IPv6_addr</i></p>
<dt><code>ListenAddress</code></p>
<dd><i>host </i><code>| </code><i>IPv4_addr </i><code>: </code><i>port</i></p>
<dt><code>ListenAddress</code></p>
<dd>[<i>host </i><code>| </code><i>IPv6_addr : port</i> ]</dl>
<p> If <i>port</i> is not specified, sshd will listen on the address and all prior <code>Port</code> options specified. The default is to listen on all local addresses. Multiple <code>ListenAddress</code> options are permitted. Additionally, any <code>Port</code> options must precede this option for non-port qualified addresses.</p>
<dt><code>LoginGraceTime</code></p>
<dd>The server disconnects after this time if the user has not successfully logged in. If the value is 0, there is no time limit. The default is 120 seconds.</p>
<dt><code>LogLevel</code></p>
<dd>Gives the verbosity level that is used when logging messages from <a href="/docs/linux/man/8-sshd/">sshd</a>(8). The possible values are: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, and DEBUG3. The default is INFO. DEBUG and DEBUG1 are equivalent. DEBUG2 and DEBUG3 each specify higher levels of debugging output. Logging with a DEBUG level violates the privacy of users and is not recommended.</p>
<dt><code>MACs </code>Specifies the available MAC (message authentication code) algorithms.</p>
<dd>The MAC algorithm is used in protocol version 2 for data integrity protection. Multiple algorithms must be comma-separated. The algorithms that contain &#8220;-etm&#8221; calculate the MAC after encryption (encrypt-then-mac). These are considered safer and their use recommended. The default is: </p>
<blockquote>
<pre>hmac-md5-etm [at] openssh.com,hmac-sha1-etm [at] openssh.com,
umac-64-etm [at] openssh.com,umac-128-etm [at] openssh.com,
hmac-sha2-256-etm [at] openssh.com,hmac-sha2-512-etm [at] openssh.com,
hmac-ripemd160-etm [at] openssh.com,hmac-sha1-96-etm [at] openssh.com,
hmac-md5-96-etm [at] openssh.com,
hmac-md5,hmac-sha1,umac-64 [at] openssh.com,umac-128 [at] openssh.com,
hmac-sha2-256,hmac-sha2-512,hmac-ripemd160,
hmac-sha1-96,hmac-md5-96</pre>
</blockquote>
<dt><code>Match</code></p>
<dd>Introduces a conditional block. If all of the criteria on the <code>Match</code> line are satisfied, the keywords on the following lines override those set in the global section of the config file, until either another <code>Match</code> line or the end of the file. If a keyword appears in multiple <code>Match</code> blocks that are satisified, only the first instance of the keyword is applied. The arguments to <code>Match</code> are one or more criteria-pattern pairs or the single token <code>All</code> which matches all criteria. The available criteria are <code>User</code> <code>Group</code> <code>Host</code> <code>LocalAddress</code> <code>LocalPort</code> and <code>Address</code> The match patterns may consist of single entries or comma-separated lists and may use the wildcard and negation operators described in the PATTERNS section of ssh_config5. The patterns in an <code>Address</code> criteria may additionally contain addresses to match in CIDR address/masklen format, e.g. &#8220;192.0.2.0/24&#8221; or &#8220;3ffe:ffff::/32&#8221; Note that the mask length provided must be consistent with the address &#8211; it is an error to specify a mask length that is too long for the address or one with bits set in this host portion of the address. For example, &#8220;192.0.2.0/33&#8221; and &#8220;192.0.2.0/8&#8221; respectively. Only a subset of keywords may be used on the lines following a <code>Match</code> keyword. Available keywords are <code>AcceptEnv</code> <code>AllowAgentForwarding</code> <code>AllowGroups</code> <code>AllowTcpForwarding</code> <code>AllowUsers</code> <code>AuthenticationMethods</code> <code>AuthorizedKeysCommand</code> <code>AuthorizedKeysCommandUser</code> <code>AuthorizedKeysFile</code> <code>AuthorizedPrincipalsFile</code> <code>Banner</code> <code>ChrootDirectory</code> <code>DenyGroups</code> <code>DenyUsers</code> <code>ForceCommand</code> <code>GatewayPorts</code> <code>GSSAPIAuthentication</code> <code>HostbasedAuthentication</code> <code>HostbasedUsesNameFromPacketOnly</code> <code>KbdInteractiveAuthentication</code> <code>KerberosAuthentication</code> <code>KerberosUseKuserok</code> <code>MaxAuthTries</code> <code>MaxSessions</code> <code>PasswordAuthentication</code> <code>PermitEmptyPasswords</code> <code>PermitOpen</code> <code>PermitRootLogin</code> <code>PermitTTY</code> <code>PermitTunnel</code> <code>PubkeyAuthentication</code> <code>RekeyLimit</code> <code>RhostsRSAAuthentication</code> <code>RSAAuthentication</code> <code>X11DisplayOffset</code> <code>X11MaxDisplays</code> <code>X11Forwarding</code> and <code>X11UseLocalHost</code></p>
<dt><code>MaxAuthTries</code></p>
<dd>Specifies the maximum number of authentication attempts permitted per connection. Once the number of failures reaches half this value, additional failures are logged. The default is 6.</p>
<dt><code>MaxSessions</code></p>
<dd>Specifies the maximum number of open sessions permitted per network connection. The default is 10.</p>
<dt><code>MaxStartups</code></p>
<dd>Specifies the maximum number of concurrent unauthenticated connections to the SSH daemon. Additional connections will be dropped until authentication succeeds or the <code>LoginGraceTime</code> expires for a connection. The default is 10:30:100. Alternatively, random early drop can be enabled by specifying the three colon separated values &#8220;start:rate:full&#8221; (e.g. &quot;10:30:60&quot;). <a href="/docs/linux/man/8-sshd/">sshd</a>(8) will refuse connection attempts with a probability of &#8220;rate/100&#8221; (30%) if there are currently &#8220;start&#8221; (10) unauthenticated connections. The probability increases linearly and all connection attempts are refused if the number of unauthenticated connections reaches &#8220;full&#8221; (60).</p>
<dt><code>PasswordAuthentication</code></p>
<dd>Specifies whether password authentication is allowed. The default is &#8220;yes&#8221;</p>
<dt><code>PermitEmptyPasswords</code></p>
<dd>When password authentication is allowed, it specifies whether the server allows login to accounts with empty password strings. The default is &#8220;no&#8221;</p>
<dt><code>PermitOpen</code></p>
<dd>Specifies the destinations to which TCP port forwarding is permitted. The forwarding specification must be one of the following forms: </p>
<dt><code>PermitOpen</code></p>
<dd><i>host : port</i></p>
<dt><code>PermitOpen</code></p>
<dd><i>IPv4_addr : port</i></p>
<dt><code>PermitOpen</code></p>
<dd><i>[ IPv6_addr ] : port</i></dl>
<p> Multiple forwards may be specified by separating them with whitespace. An argument of &#8220;any&#8221; can be used to remove all restrictions and permit any forwarding requests. An argument of &#8220;none&#8221; can be used to prohibit all forwarding requests. Wildcard &#8220;*&#8221; can be used for host or port to allow all hosts or all ports respectively. By default all port forwarding requests are permitted.</p>
<dt><code>PermitRootLogin</code></p>
<dd>Specifies whether root can log in using <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The argument must be &#8220;yes&#8221; &#8220;without-password&#8221; &#8220;forced-commands-only&#8221; or &#8220;no&#8221; The default is &#8220;yes&#8221; If this option is set to &#8220;without-password&#8221; password authentication is disabled for root. If this option is set to &#8220;forced-commands-only&#8221; root login with public key authentication will be allowed, but only if the <i>command</i> option has been specified (which may be useful for taking remote backups even if root login is normally not allowed). All other authentication methods are disabled for root. If this option is set to &#8220;no&#8221; root is not allowed to log in.</p>
<dt><code>PermitTunnel</code></p>
<dd>Specifies whether <a href="/docs/linux/man/4-tun/">tun</a>(4) device forwarding is allowed. The argument must be &#8220;yes&#8221; &#8220;point-to-point&#8221; (layer 3), &#8220;ethernet&#8221; (layer 2), or &#8220;no&#8221; Specifying &#8220;yes&#8221; permits both &#8220;point-to-point&#8221; and &#8220;ethernet&#8221; The default is &#8220;no&#8221;</p>
<dt><code>PermitTTY</code></p>
<dd>Specifies whether <a href="/docs/linux/man/4-pty/">pty</a>(4) allocation is permitted. The default is &#8220;yes&#8221;</p>
<dt><code>PermitUserEnvironment</code></p>
<dd>Specifies whether ~/.ssh/environment and <code>environment=</code> options in ~/.ssh/authorized_keys are processed by <a href="/docs/linux/man/8-sshd/">sshd</a>(8). The default is &#8220;no&#8221; Enabling environment processing may enable users to bypass access restrictions in some configurations using mechanisms such as <code>LD_PRELOAD</code></p>
<dt><code>PidFile</code></p>
<dd>Specifies the file that contains the process ID of the SSH daemon. The default is /var/run/gsisshd.pid</p>
<dt><code>Port</code></p>
<dd>Specifies the port number that <a href="/docs/linux/man/8-sshd/">sshd</a>(8) listens on. The default is 22. Multiple options of this type are permitted. See also <code>ListenAddress</code></p>
<dt><code>PrintLastLog</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should print the date and time of the last user login when a user logs in interactively. The default is &#8220;yes&#8221;</p>
<dt><code>PrintMotd</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should print /etc/motd when a user logs in interactively. (On some systems it is also printed by the shell, /etc/profile or equivalent.) The default is &#8220;yes&#8221;</p>
<dt><code>Protocol</code></p>
<dd>Specifies the protocol versions <a href="/docs/linux/man/8-sshd/">sshd</a>(8) supports. The possible values are `1&#8242; and `2&#8242; Multiple versions must be comma-separated. The default is `2&#8242; Note that the order of the protocol list does not indicate preference, because the client selects among multiple protocol versions offered by the server. Specifying &#8220;2,1&#8221; is identical to &#8220;1,2&#8221;</p>
<dt><code>PubkeyAuthentication</code></p>
<dd>Specifies whether public key authentication is allowed. The default is &#8220;yes&#8221; Note that this option applies to protocol version 2 only.</p>
<dt><code>RekeyLimit</code></p>
<dd>Specifies the maximum amount of data that may be transmitted before the session key is renegotiated, optionally followed a maximum amount of time that may pass before the session key is renegotiated. The first argument is specified in bytes and may have a suffix of `K&#8217; `M&#8217; or `G&#8217; to indicate Kilobytes, Megabytes, or Gigabytes, respectively. The default is between `1G&#8217; and `4G&#8217; depending on the cipher. The optional second value is specified in seconds and may use any of the units documented in the Sx TIME FORMATS section. The default value for <code>RekeyLimit</code> is &#8220;default none&#8221; which means that rekeying is performed after the cipher&#8217;s default amount of data has been sent or received and no time based rekeying is done. This option applies to protocol version 2 only.</p>
<dt><code>RevokedKeys</code></p>
<dd>Specifies revoked public keys. Keys listed in this file will be refused for public key authentication. Note that if this file is not readable, then public key authentication will be refused for all users. Keys may be specified as a text file, listing one public key per line, or as an OpenSSH Key Revocation List (KRL) as generated by ssh-keygen1. For more information on KRLs, see the KEY REVOCATION LISTS section in ssh-keygen1.</p>
<dt><code>RhostsRSAAuthentication</code></p>
<dd>Specifies whether rhosts or /etc/hosts.equiv authentication together with successful RSA host authentication is allowed. The default is &#8220;no&#8221; This option applies to protocol version 1 only.</p>
<dt><code>RSAAuthentication</code></p>
<dd>Specifies whether pure RSA authentication is allowed. The default is &#8220;yes&#8221; This option applies to protocol version 1 only.</p>
<dt><code>ServerKeyBits</code></p>
<dd>Defines the number of bits in the ephemeral protocol version 1 server key. The minimum value is 512, and the default is 1024.</p>
<dt><code>ShowPatchLevel </code></p>
<dd>Specifies whether <code>sshd </code> will display the patch level of the binary in the identification string. The patch level is set at compile-time. The default is &#8220;no . &#8221; This option applies to protocol version 1 only.</p>
<dt><code>StrictModes</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should check file modes and ownership of the user&#8217;s files and home directory before accepting login. This is normally desirable because novices sometimes accidentally leave their directory or files world-writable. The default is &#8220;yes&#8221; Note that this does not apply to <code>ChrootDirectory</code> whose permissions and ownership are checked unconditionally.</p>
<dt><code>Subsystem</code></p>
<dd>Configures an external subsystem (e.g. file transfer daemon). Arguments should be a subsystem name and a command (with optional arguments) to execute upon subsystem request. The command sftp-server8 implements the &#8220;sftp&#8221; file transfer subsystem. Alternately the name &#8220;internal-sftp&#8221; implements an in-process &#8220;sftp&#8221; server. This may simplify configurations using <code>ChrootDirectory</code> to force a different filesystem root on clients. By default no subsystems are defined. Note that this option applies to protocol version 2 only.</p>
<dt><code>SyslogFacility</code></p>
<dd>Gives the facility code that is used when logging messages from <a href="/docs/linux/man/8-sshd/">sshd</a>(8). The possible values are: DAEMON, USER, AUTH, AUTHPRIV, LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7. The default is AUTH.</p>
<dt><code>TCPKeepAlive</code></p>
<dd>Specifies whether the system should send TCP keepalive messages to the other side. If they are sent, death of the connection or crash of one of the machines will be properly noticed. However, this means that connections will die if the route is down temporarily, and some people find it annoying. On the other hand, if TCP keepalives are not sent, sessions may hang indefinitely on the server, leaving &#8220;ghost&#8221; users and consuming server resources. The default is &#8220;yes&#8221; (to send TCP keepalive messages), and the server will notice if the network goes down or the client host crashes. This avoids infinitely hanging sessions. To disable TCP keepalive messages, the value should be set to &#8220;no&#8221;</p>
<dt><code>TrustedUserCAKeys</code></p>
<dd>Specifies a file containing public keys of certificate authorities that are trusted to sign user certificates for authentication. Keys are listed one per line; empty lines and comments starting with `#&#8217; are allowed. If a certificate is presented for authentication and has its signing CA key listed in this file, then it may be used for authentication for any user listed in the certificate&#8217;s principals list. Note that certificates that lack a list of principals will not be permitted for authentication using <code>TrustedUserCAKeys</code> For more details on certificates, see the CERTIFICATES section in ssh-keygen1.</p>
<dt><code>UsageStatsTargets</code></p>
<dd>This option can be used to specify the target collector hosts to which usage metrics should be reported. This setting will be ignored if <code>DisableUsageStats</code> is enabled. Multiple targets can be specified separated by comma(s), but no space(s). Each target specification is of the format host:port[!tags]. Tags control what data elements are reported. The following list specifies the tags for the corresponding data elements. </p>
<dt><code>V</code></p>
<dd>&#8211; OpenSSH version, reported by default.</p>
<dt><code>v</code></p>
<dd>&#8211; SSL version, reported by default.</p>
<dt><code>M</code></p>
<dd>&#8211; User authentication method used such as &quot;gssapi-keyex&quot;, &quot;gssapi-with-mic&quot;, etc. Reported by default.</p>
<dt><code>m</code></p>
<dd>&#8211; User authentication mechanism used such as &quot;GSI&quot;, &quot;Kerberos&quot;, etc. Reported by default.</p>
<dt><code>I</code></p>
<dd>&#8211; Client IP address. Not reported by default.</p>
<dt><code>u</code></p>
<dd>&#8211; User name. Not reported by default.</p>
<dt><code>U</code></p>
<dd>&#8211; User DN. Not reported by default. In addition to the above selected information, the following data are reported to ALL the specified/default target collectors. There&#8217;s no way to exclude these from being reported other than by disabling the reporting of usage metrics altogether:</p>
<dt><code>Component code</code></p>
<dd>&#8211; 12 for GSI OpenSSH</p>
<dt><code>Component Data Format version</code></p>
<dd>&#8211; 0 currently</p>
<dt><code>IP Address</code></p>
<dd>&#8211; IP address of reporting server</p>
<dt><code>Timestamp</code></p>
<dd>
<dt><code>Hostname</code></p>
<dd>&#8211; Host name of reporting server If no tags are specified in a host spec, or the special string &#8220;default&#8221; is specified, the tags &#8220;VvMm are assumed. A site could choose to allow a &#8221; different set of data to be reported by specifying a different tag set. The last 3 tags &#8220;I&#8221; &#8220;u&#8221; and &#8220;U&#8221; above are more meant for a local collector that a site might like to deploy since they could be construed as private information. The special string &#8220;all&#8221; denotes all tags.</dl>
<p> By default, Usage Metrics reporting is sent to &#8220;usage-stats.cilogon.org:4810&#8221; This can be made explicit by specifying &#8220;default&#8221; (all by itself) for the target specification as in: </p>
<dt><code>UsageStatsTargets</code></p>
<dd>default</dl>
<p> If <code>UsageStatsTargets</code> is not specified, a comma-separated list of targets (without any tags specified) if specified in the environment variable <code>GLOBUS_USAGE_TARGETS</code> will be used.</p>
<dt><code>UseDNS</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should look up the remote host name and check that the resolved host name for the remote IP address maps back to the very same IP address. The default is &#8220;yes&#8221;</p>
<dt><code>UseLogin</code></p>
<dd>Specifies whether <a href="/docs/linux/man/1-login/">login</a>(1) is used for interactive login sessions. The default is &#8220;no&#8221; Note that <a href="/docs/linux/man/1-login/">login</a>(1) is never used for remote command execution. Note also, that if this is enabled, <code>X11Forwarding</code> will be disabled because <a href="/docs/linux/man/1-login/">login</a>(1) does not know how to handle <a href="/docs/linux/man/1-xauth/">xauth</a>(1) cookies. If <code>UsePrivilegeSeparation</code> is specified, it will be disabled after authentication.</p>
<dt><code>UsePAM</code></p>
<dd>Enables the Pluggable Authentication Module interface. If set to &#8220;yes&#8221; this will enable PAM authentication using <code>ChallengeResponseAuthentication</code> and <code>PasswordAuthentication</code> in addition to PAM account and session module processing for all authentication types. Because PAM challenge-response authentication usually serves an equivalent role to password authentication, you should disable either <code>PasswordAuthentication</code> or <code>ChallengeResponseAuthentication.</code> If <code>UsePAM</code> is enabled, you will not be able to run <a href="/docs/linux/man/8-sshd/">sshd</a>(8) as a non-root user. The default is &#8220;no&#8221;</p>
<dt><code>PermitPAMUserChange</code></p>
<dd>If set to &#8220;yes&#8221; this will enable PAM authentication to change the name of the user being authenticated. The default is &#8220;no&#8221;</p>
<dt><code>UsePrivilegeSeparation</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) separates privileges by creating an unprivileged child process to deal with incoming network traffic. After successful authentication, another process will be created that has the privilege of the authenticated user. The goal of privilege separation is to prevent privilege escalation by containing any corruption within the unprivileged processes. The default is &#8220;yes&#8221; If <code>UsePrivilegeSeparation</code> is set to &#8220;sandbox&#8221; then the pre-authentication unprivileged process is subject to additional restrictions.</p>
<dt><code>VersionAddendum</code></p>
<dd>Optionally specifies additional text to append to the SSH protocol banner sent by the server upon connection. The default is &#8220;none&#8221;</p>
<dt><code>X11DisplayOffset</code></p>
<dd>Specifies the first display number available for <a href="/docs/linux/man/8-sshd/">sshd</a>(8)Ns&#8217;s X11 forwarding. This prevents sshd from interfering with real X11 servers. The default is 10.</p>
<dt><code>X11MaxDisplays</code></p>
<dd>Specifies the maximum number of displays available for <a href="/docs/linux/man/8-sshd/">sshd</a>(8)Ns&#8217;s X11 forwarding. This prevents sshd from exhausting local ports. The default is 1000.</p>
<dt><code>X11Forwarding</code></p>
<dd>Specifies whether X11 forwarding is permitted. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221; When X11 forwarding is enabled, there may be additional exposure to the server and to client displays if the <a href="/docs/linux/man/8-sshd/">sshd</a>(8) proxy display is configured to listen on the wildcard address (see <code>X11UseLocalhost</code> below), though this is not the default. Additionally, the authentication spoofing and authentication data verification and substitution occur on the client side. The security risk of using X11 forwarding is that the client&#8217;s X11 display server may be exposed to attack when the SSH client requests forwarding (see the warnings for <code>ForwardX11</code> in ssh_config5). A system administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a &#8220;no&#8221; setting. Note that disabling X11 forwarding does not prevent users from forwarding X11 traffic, as users can always install their own forwarders. X11 forwarding is automatically disabled if <code>UseLogin</code> is enabled.</p>
<dt><code>X11UseLocalhost</code></p>
<dd>Specifies whether <a href="/docs/linux/man/8-sshd/">sshd</a>(8) should bind the X11 forwarding server to the loopback address or to the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the <code>DISPLAY</code> environment variable to &#8220;localhost&#8221; This prevents remote hosts from connecting to the proxy display. However, some older X11 clients may not function with this configuration. <code>X11UseLocalhost</code> may be set to &#8220;no&#8221; to specify that the forwarding server should be bound to the wildcard address. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;yes&#8221;</p>
<dt><code>XAuthLocation</code></p>
<dd>Specifies the full pathname of the <a href="/docs/linux/man/1-xauth/">xauth</a>(1) program. The default is /usr/bin/xauth</dl>
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
<h2>Files</h2>
<dl>
<dt><code>/etc/gsissh/sshd_config </code></p>
<dd>Contains configuration data for <a href="/docs/linux/man/8-sshd/">sshd</a>(8). This file should be writable by root only, but it is recommended (though not necessary) that it be world-readable.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>Authors</h2>
<p>OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. Niels Provos and Markus Friedl contributed support for privilege separation.</p>
