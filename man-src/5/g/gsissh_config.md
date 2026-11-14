---
title: "gsissh_config(5)"
name: "gsissh_config"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gsissh_config/"
description: "ssh_config – OpenSSH SSH client configuration files"
---

<p><code>ssh_config</code> &#8211; OpenSSH SSH client configuration files</p>
<h2>Synopsis</h2>
<p><code>~/.ssh/config</code><br />
<code>/etc/gsissh/ssh_config</code></p>
<h2>Description</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1) obtains configuration data from the following sources in the following order:  </p>
<li> command-line options
<li> user&#8217;s configuration file (~/.ssh/config )
<li> GSSAPI configuration file (~/.ssh/config.gssapi )
<li> Kerberos configuration file (~/.ssh/config.krb )
<li> system-wide configuration file (/etc/gsissh/ssh_config ) </ol>
<p> For each parameter, the first obtained value will be used. The configuration files contain sections separated by &#8220;Host&#8221; specifications, and that section is only applied for hosts that match one of the patterns given in the specification. The matched host name is the one given on the command line. Since the first obtained value for each parameter is used, more host-specific declarations should be given near the beginning of the file, and general defaults at the end. The configuration file has the following format: Empty lines and lines starting with `#&#8217; are comments. Otherwise a line is of the format &#8220;keyword arguments&#8221; Configuration options may be separated by whitespace or optional whitespace and exactly one `=&#8217; ; the latter format is useful to avoid the need to quote whitespace when specifying configuration options using the <code>ssh</code> <code>scp</code> and <code>sftp</code> &#8211;<code>o</code> option. Arguments may optionally be enclosed in double quotes () in order to represent arguments containing spaces. The possible keywords and their meanings are as follows (note that keywords are case-insensitive and arguments are case-sensitive):</p>
<dl>
<dt><code>Host</code></p>
<dd>Restricts the following declarations (up to the next <code>Host</code> or <code>Match</code> keyword) to be only for those hosts that match one of the patterns given after the keyword. If more than one pattern is provided, they should be separated by whitespace. A single `*&#8217; as a pattern can be used to provide global defaults for all hosts. The host is the <i>hostname</i> argument given on the command line (i.e. the name is not converted to a canonicalized host name before matching). A pattern entry may be negated by prefixing it with an exclamation mark (`!&#8217; ) If a negated entry is matched, then the <code>Host</code> entry is ignored, regardless of whether any other patterns on the line match. Negated matches are therefore useful to provide exceptions for wildcard matches. See Sx PATTERNS for more information on patterns.</p>
<dt><code>Match</code></p>
<dd>Restricts the following declarations (up to the next <code>Host</code> or <code>Match</code> keyword) to be used only when the conditions following the <code>Match</code> keyword are satisfied. Match conditions are specified using one or more keyword/criteria pairs or the single token <code>all</code> which matches all criteria. The available keywords are: <code>exec</code> <code>host</code> <code>originalhost</code> <code>user</code> and <code>localuser</code> The <code>exec</code> keyword executes the specified command under the user&#8217;s shell. If the command returns a zero exit status then the condition is considered true. Commands containing whitespace characters must be quoted. The following character sequences in the command will be expanded prior to execution: `%L&#8217; will be substituted by the first component of the local host name, `%l&#8217; will be substituted by the local host name (including any domain name), `%h&#8217; will be substituted by the target host name, `%n&#8217; will be substituted by the original target host name specified on the command-line, `%p&#8217; the destination port, `%r&#8217; by the remote login username, and `%u&#8217; by the username of the user running <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The other keywords&#8217; criteria must be single entries or comma-separated lists and may use the wildcard and negation operators described in the Sx PATTERNS section. The criteria for the <code>host</code> keyword are matched against the target hostname, after any substitution by the <code>Hostname</code> option. The <code>originalhost</code> keyword matches against the hostname as it was specified on the command-line. The <code>user</code> keyword matches against the target username on the remote host. The <code>localuser</code> keyword matches against the name of the local user running <a href="/docs/linux/man/1-ssh/">ssh</a>(1) (this keyword may be useful in system-wide <code>~/.ssh/config</code> files).</p>
<dt><code>AddressFamily</code></p>
<dd>Specifies which address family to use when connecting. Valid arguments are &#8220;any&#8221; &#8220;inet&#8221; (use IPv4 only), or &#8220;inet6&#8221; (use IPv6 only).</p>
<dt><code>BatchMode</code></p>
<dd>If set to &#8220;yes&#8221; passphrase/password querying will be disabled. This option is useful in scripts and other batch jobs where no user is present to supply the password. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221;</p>
<dt><code>BindAddress</code></p>
<dd>Use the specified address on the local machine as the source address of the connection. Only useful on systems with more than one address. Note that this option does not work if <code>UsePrivilegedPort</code> is set to &#8220;yes&#8221;</p>
<dt><code>CanonicalDomains</code></p>
<dd>When <code>CanonicalizeHostname</code> is enabled, this option specifies the list of domain suffixes in which to search for the specified destination host.</p>
<dt><code>CanonicalizeFallbackLocal</code></p>
<dd>Specifies whether to fail with an error when hostname canonicalization fails. The default, &#8220;yes&#8221; will attempt to look up the unqualified hostname using the system resolver&#8217;s search rules. A value of &#8220;no&#8221; will cause <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to fail instantly if <code>CanonicalizeHostname</code> is enabled and the target hostname cannot be found in any of the domains specified by <code>CanonicalDomains</code></p>
<dt><code>CanonicalizeHostname</code></p>
<dd>Controls whether explicit hostname canonicalization is performed. The default, &#8220;no&#8221; is not to perform any name rewriting and let the system resolver handle all hostname lookups. If set to &#8220;yes&#8221; then, for connections that do not use a <code>ProxyCommand</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will attempt to canonicalize the hostname specified on the command line using the <code>CanonicalDomains</code> suffixes and <code>CanonicalizePermittedCNAMEs </code>rules. If <code>CanonicalizeHostname</code> is set to &#8220;always&#8221; then canonicalization is applied to proxied connections too. If this option is enabled and canonicalisation results in the target hostname changing, then the configuration files are processed again using the new target name to pick up any new configuration in matching <code>Host</code> stanzas.</p>
<dt><code>CanonicalizeMaxDots</code></p>
<dd>Specifies the maximum number of dot characters in a hostname before canonicalization is disabled. The default, &#8220;1&#8221; allows a single dot (i.e. hostname.subdomain).</p>
<dt><code>CanonicalizePermittedCNAMEs </code>Specifies rules to determine whether CNAMEs should be followed when</p>
<dd>canonicalizing hostnames. The rules consist of one or more arguments of <i>source_domain_list : </i><i>target_domain_list</i> where <i>source_domain_list</i> is a pattern-list of domains that may follow CNAMEs in canonicalization, and <i>target_domain_list</i> is a pattern-list of domains that they may resolve to. For example, &#8220;*.a.example.com:*.b.example.com,*.c.example.com&#8221; will allow hostnames matching &#8220;*.a.example.com&#8221; to be canonicalized to names in the &#8220;*.b.example.com&#8221; or &#8220;*.c.example.com&#8221; domains.</p>
<dt><code>ChallengeResponseAuthentication</code></p>
<dd>Specifies whether to use challenge-response authentication. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;yes&#8221;</p>
<dt><code>CheckHostIP</code></p>
<dd>If this flag is set to &#8220;yes&#8221; <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will additionally check the host IP address in the known_hosts file. This allows ssh to detect if a host key changed due to DNS spoofing. If the option is set to &#8220;no&#8221; the check will not be executed. The default is &#8220;yes&#8221;</p>
<dt><code>Cipher</code></p>
<dd>Specifies the cipher to use for encrypting the session in protocol version 1. Currently, &#8220;blowfish&#8221; &#8220;3des&#8221; and &#8220;des&#8221; are supported. <i>des</i> is only supported in the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) client for interoperability with legacy protocol 1 implementations that do not support the <i>3des</i> cipher. Its use is strongly discouraged due to cryptographic weaknesses. The default is &#8220;3des&#8221;</p>
<dt><code>Ciphers</code></p>
<dd>Specifies the ciphers allowed for protocol version 2 in order of preference. Multiple ciphers must be comma-separated. The supported ciphers are: &#8220;3des-cbc&#8221; &#8220;aes128-cbc&#8221; &#8220;aes192-cbc&#8221; &#8220;aes256-cbc&#8221; &#8220;aes128-ctr&#8221; &#8220;aes192-ctr&#8221; &#8220;aes256-ctr&#8221; &#8220;aes128-gcm [at] openssh.com&#8221; &#8220;aes256-gcm [at] openssh.com&#8221; &#8220;arcfour128&#8221; &#8220;arcfour256&#8221; &#8220;arcfour&#8221; &#8220;blowfish-cbc&#8221; &#8220;cast128-cbc&#8221; and &#8220;chacha20-poly1305 [at] openssh.com&#8221; The default is: </p>
<pre>aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,
aes128-gcm [at] openssh.com,aes256-gcm [at] openssh.com,
chacha20-poly1305 [at] openssh.com,
aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,aes192-cbc,
aes256-cbc,arcfour</pre>
<p>The list of available ciphers may also be obtained using the &#8211;<code>Q</code> option of <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>ClearAllForwardings</code></p>
<dd>Specifies that all local, remote, and dynamic port forwardings specified in the configuration files or on the command line be cleared. This option is primarily useful when used from the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) command line to clear port forwardings set in configuration files, and is automatically set by <a href="/docs/linux/man/1-scp/">scp</a>(1) and <a href="/docs/linux/man/1-sftp/">sftp</a>(1). The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221;</p>
<dt><code>Compression</code></p>
<dd>Specifies whether to use compression. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221;</p>
<dt><code>CompressionLevel</code></p>
<dd>Specifies the compression level to use if compression is enabled. The argument must be an integer from 1 (fast) to 9 (slow, best). The default level is 6, which is good for most applications. The meaning of the values is the same as in <a href="/docs/linux/man/1-gzip/">gzip</a>(1). Note that this option applies to protocol version 1 only.</p>
<dt><code>ConnectionAttempts</code></p>
<dd>Specifies the number of tries (one per second) to make before exiting. The argument must be an integer. This may be useful in scripts if the connection sometimes fails. The default is 1.</p>
<dt><code>ConnectTimeout</code></p>
<dd>Specifies the timeout (in seconds) used when connecting to the SSH server, instead of using the default system TCP timeout. This value is used only when the target is down or really unreachable, not when it refuses the connection.</p>
<dt><code>ControlMaster</code></p>
<dd>Enables the sharing of multiple sessions over a single network connection. When set to &#8220;yes&#8221; <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will listen for connections on a control socket specified using the <code>ControlPath</code> argument. Additional sessions can connect to this socket using the same <code>ControlPath</code> with <code>ControlMaster</code> set to &#8220;no&#8221; (the default). These sessions will try to reuse the master instance&#8217;s network connection rather than initiating new ones, but will fall back to connecting normally if the control socket does not exist, or is not listening. Setting this to &#8220;ask&#8221; will cause ssh to listen for control connections, but require confirmation using the <code>SSH_ASKPASS</code> program before they are accepted (see ssh-add1 for details). If the <code>ControlPath</code> cannot be opened, ssh will continue without connecting to a master instance. X11 and ssh-agent1 forwarding is supported over these multiplexed connections, however the display and agent forwarded will be the one belonging to the master connection i.e. it is not possible to forward multiple displays or agents. Two additional options allow for opportunistic multiplexing: try to use a master connection but fall back to creating a new one if one does not already exist. These options are: &#8220;auto&#8221; and &#8220;autoask&#8221; The latter requires confirmation like the &#8220;ask&#8221; option.</p>
<dt><code>ControlPath</code></p>
<dd>Specify the path to the control socket used for connection sharing as described in the <code>ControlMaster</code> section above or the string &#8220;none&#8221; to disable connection sharing. In the path, `%L&#8217; will be substituted by the first component of the local host name, `%l&#8217; will be substituted by the local host name (including any domain name), `%h&#8217; will be substituted by the target host name, `%n&#8217; will be substituted by the original target host name specified on the command line, `%p&#8217; the destination port, `%r&#8217; by the remote login username, and `%u&#8217; by the username of the user running <a href="/docs/linux/man/1-ssh/">ssh</a>(1). It is recommended that any <code>ControlPath</code> used for opportunistic connection sharing include at least %h, %p, and %r. This ensures that shared connections are uniquely identified.</p>
<dt><code>ControlPersist</code></p>
<dd>When used in conjunction with <code>ControlMaster</code> specifies that the master connection should remain open in the background (waiting for future client connections) after the initial client connection has been closed. If set to &#8220;no&#8221; then the master connection will not be placed into the background, and will close as soon as the initial client connection is closed. If set to &#8220;yes&#8221; then the master connection will remain in the background indefinitely (until killed or closed via a mechanism such as the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) &#8220;-<code>O exit</code> &#8221; option). If set to a time in seconds, or a time in any of the formats documented in sshd_config5, then the backgrounded master connection will automatically terminate after it has remained idle (with no client connections) for the specified time.</p>
<dt><code>DynamicForward</code></p>
<dd>Specifies that a TCP port on the local machine be forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine. The argument must be [<i>bind_address : port</i> ] IPv6 addresses can be specified by enclosing addresses in square brackets. By default, the local port is bound in accordance with the <code>GatewayPorts</code> setting. However, an explicit <i>bind_address</i> may be used to bind the connection to a specific address. The <i>bind_address</i> of &#8220;localhost&#8221; indicates that the listening port be bound for local use only, while an empty address or `*&#8217; indicates that the port should be available from all interfaces. Currently the SOCKS4 and SOCKS5 protocols are supported, and <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will act as a SOCKS server. Multiple forwardings may be specified, and additional forwardings can be given on the command line. Only the superuser can forward privileged ports.</p>
<dt><code>EnableSSHKeysign</code></p>
<dd>Setting this option to &#8220;yes&#8221; in the global client configuration file /etc/gsissh/ssh_config enables the use of the helper program ssh-keysign8 during <code>HostbasedAuthentication</code> The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221; This option should be placed in the non-hostspecific section. See ssh-keysign8 for more information.</p>
<dt><code>EscapeChar</code></p>
<dd>Sets the escape character (default: `~&#8217; ) . The escape character can also be set on the command line. The argument should be a single character, `^&#8217; followed by a letter, or &#8220;none&#8221; to disable the escape character entirely (making the connection transparent for binary data).</p>
<dt><code>ExitOnForwardFailure</code></p>
<dd>Specifies whether <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should terminate the connection if it cannot set up all requested dynamic, tunnel, local, and remote port forwardings. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221;</p>
<dt><code>ForwardAgent</code></p>
<dd>Specifies whether the connection to the authentication agent (if any) will be forwarded to the remote machine. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221; Agent forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the agent&#8217;s Unix-domain socket) can access the local agent through the forwarded connection. An attacker cannot obtain key material from the agent, however they can perform operations on the keys that enable them to authenticate using the identities loaded into the agent.</p>
<dt><code>ForwardX11</code></p>
<dd>Specifies whether X11 connections will be automatically redirected over the secure channel and <code>DISPLAY</code> set. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221; X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user&#8217;s X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the <code>ForwardX11Trusted</code> option is also enabled.</p>
<dt><code>ForwardX11Timeout</code></p>
<dd>Specify a timeout for untrusted X11 forwarding using the format described in the TIME FORMATS section of sshd_config5. X11 connections received by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) after this time will be refused. The default is to disable untrusted X11 forwarding after twenty minutes has elapsed.</p>
<dt><code>ForwardX11Trusted</code></p>
<dd>If this option is set to &#8220;yes&#8221; remote X11 clients will have full access to the original X11 display. If this option is set to &#8220;no&#8221; remote X11 clients will be considered untrusted and prevented from stealing or tampering with data belonging to trusted X11 clients. Furthermore, the <a href="/docs/linux/man/1-xauth/">xauth</a>(1) token used for the session will be set to expire after 20 minutes. Remote clients will be refused access after this time. The default is &#8220;no&#8221; See the X11 SECURITY extension specification for full details on the restrictions imposed on untrusted clients.</p>
<dt><code>GatewayPorts</code></p>
<dd>Specifies whether remote hosts are allowed to connect to local forwarded ports. By default, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) binds local port forwardings to the loopback address. This prevents other remote hosts from connecting to forwarded ports. <code>GatewayPorts</code> can be used to specify that ssh should bind local port forwardings to the wildcard address, thus allowing remote hosts to connect to forwarded ports. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221;</p>
<dt><code>GlobalKnownHostsFile</code></p>
<dd>Specifies one or more files to use for the global host key database, separated by whitespace. The default is /etc/gsissh/ssh_known_hosts /etc/gsissh/ssh_known_hosts2</p>
<dt><code>GSSAPIAuthentication</code></p>
<dd>Specifies whether user authentication based on GSSAPI is allowed. The default is &#8220;yes&#8221; Note that this option applies to protocol version 2 only.</p>
<dt><code>GSSAPIKeyExchange</code></p>
<dd>Specifies whether key exchange based on GSSAPI may be used. When using GSSAPI key exchange the server need not have a host key. The default is &#8220;yes&#8221; Note that this option applies to protocol version 2 only.</p>
<dt><code>GSSAPIClientIdentity</code></p>
<dd>If set, specifies the GSSAPI client identity that ssh should use when connecting to the server. The default is unset, which means that the default identity will be used.</p>
<dt><code>GSSAPIServerIdentity</code></p>
<dd>If set, specifies the GSSAPI server identity that ssh should expect when connecting to the server. The default is unset, which means that the expected GSSAPI server identity will be determined from the target hostname.</p>
<dt><code>GSSAPIDelegateCredentials</code></p>
<dd>Forward (delegate) credentials to the server. The default is &#8220;yes&#8221; Note that this option applies to protocol version 2 connections using GSSAPI.</p>
<dt><code>GSSAPIRenewalForcesRekey</code></p>
<dd>If set to &#8220;yes&#8221; then renewal of the client&#8217;s GSSAPI credentials will force the rekeying of the ssh connection. With a compatible server, this can delegate the renewed credentials to a session on the server. The default is &#8220;no&#8221;</p>
<dt><code>GSSAPITrustDns</code></p>
<dd>Set to &#8220;yes to indicate that the DNS is trusted to securely canonicalize&#8221; the name of the host being connected to. If &#8220;no, the hostname entered on the&#8221; command line will be passed untouched to the GSSAPI library. The default is &#8220;yes&#8221; This option only applies to protocol version 2 connections using GSSAPI.</p>
<dt><code>GSSAPIKexAlgorithms</code></p>
<dd>The list of key exchange algorithms that are offered for GSSAPI key exchange. Possible values are </p>
<pre>gss-gex-sha1-,
gss-group1-sha1-,
gss-group14-sha1-</pre>
<p>The default is &#8220;gss-gex-sha1-,gss-group1-sha1-,gss-group14-sha1-&#8221; This option only applies to protocol version 2 connections using GSSAPI.</p>
<dt><code>HashKnownHosts</code></p>
<dd>Indicates that <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should hash host names and addresses when they are added to ~/.ssh/known_hosts These hashed names may be used normally by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) and <a href="/docs/linux/man/8-sshd/">sshd</a>(8), but they do not reveal identifying information should the file&#8217;s contents be disclosed. The default is &#8220;no&#8221; Note that existing names and addresses in known hosts files will not be converted automatically, but may be manually hashed using ssh-keygen1.</p>
<dt><code>HostbasedAuthentication</code></p>
<dd>Specifies whether to try rhosts based authentication with public key authentication. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221; This option applies to protocol version 2 only and is similar to <code>RhostsRSAAuthentication</code></p>
<dt><code>HostKeyAlgorithms</code></p>
<dd>Specifies the protocol version 2 host key algorithms that the client wants to use in order of preference. The default for this option is: </p>
<pre>ecdsa-sha2-nistp256-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp384-cert-v01 [at] openssh.com,
ecdsa-sha2-nistp521-cert-v01 [at] openssh.com,
ssh-ed25519-cert-v01 [at] openssh.com,
ssh-rsa-cert-v01 [at] openssh.com,ssh-dss-cert-v01 [at] openssh.com,
ssh-rsa-cert-v00 [at] openssh.com,ssh-dss-cert-v00 [at] openssh.com,
ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
ssh-ed25519,ssh-rsa,ssh-dss</pre>
<p>If hostkeys are known for the destination host then this default is modified to prefer their algorithms.</p>
<dt><code>HostKeyAlias</code></p>
<dd>Specifies an alias that should be used instead of the real host name when looking up or saving the host key in the host key database files. This option is useful for tunneling SSH connections or for multiple servers running on a single host.</p>
<dt><code>HostName</code></p>
<dd>Specifies the real host name to log into. This can be used to specify nicknames or abbreviations for hosts. If the hostname contains the character sequence `%h&#8217; , then this will be replaced with the host name specified on the command line (this is useful for manipulating unqualified names). The default is the name given on the command line. Numeric IP addresses are also permitted (both on the command line and in <code>HostName</code> specifications).</p>
<dt><code>IdentitiesOnly</code></p>
<dd>Specifies that <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should only use the authentication identity files configured in the <code>~/.ssh/config</code> files, even if ssh-agent1 or a <code>PKCS11Provider</code> offers more identities. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; This option is intended for situations where ssh-agent offers many different identities. The default is &#8220;no&#8221;</p>
<dt><code>IdentityFile</code></p>
<dd>Specifies a file from which the user&#8217;s DSA, ECDSA, ED25519 or RSA authentication identity is read. The default is ~/.ssh/identity for protocol version 1, and ~/.ssh/id_dsa ~/.ssh/id_ecdsa ~/.ssh/id_ed25519 and ~/.ssh/id_rsa for protocol version 2. Additionally, any identities represented by the authentication agent will be used for authentication unless <code>IdentitiesOnly</code> is set. <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will try to load certificate information from the filename obtained by appending -cert.pub to the path of a specified <code>IdentityFile</code> The file name may use the tilde syntax to refer to a user&#8217;s home directory or one of the following escape characters: `%d&#8217; (local user&#8217;s home directory), `%u&#8217; (local user name), `%l&#8217; (local host name), `%h&#8217; (remote host name) or `%r&#8217; (remote user name). It is possible to have multiple identity files specified in configuration files; all these identities will be tried in sequence. Multiple <code>IdentityFile</code> directives will add to the list of identities tried (this behaviour differs from that of other configuration directives). <code>IdentityFile</code> may be used in conjunction with <code>IdentitiesOnly</code> to select which identities in an agent are offered during authentication.</p>
<dt><code>IgnoreUnknown</code></p>
<dd>Specifies a pattern-list of unknown options to be ignored if they are encountered in configuration parsing. This may be used to suppress errors if <code>~/.ssh/config</code> contains options that are unrecognised by <a href="/docs/linux/man/1-ssh/">ssh</a>(1). It is recommended that <code>IgnoreUnknown</code> be listed early in the configuration file as it will not be applied to unknown options that appear before it.</p>
<dt><code>IPQoS</code></p>
<dd>Specifies the IPv4 type-of-service or DSCP class for connections. Accepted values are &#8220;af11&#8221; &#8220;af12&#8221; &#8220;af13&#8221; &#8220;af21&#8221; &#8220;af22&#8221; &#8220;af23&#8221; &#8220;af31&#8221; &#8220;af32&#8221; &#8220;af33&#8221; &#8220;af41&#8221; &#8220;af42&#8221; &#8220;af43&#8221; &#8220;cs0&#8221; &#8220;cs1&#8221; &#8220;cs2&#8221; &#8220;cs3&#8221; &#8220;cs4&#8221; &#8220;cs5&#8221; &#8220;cs6&#8221; &#8220;cs7&#8221; &#8220;ef&#8221; &#8220;lowdelay&#8221; &#8220;throughput&#8221; &#8220;reliability&#8221; or a numeric value. This option may take one or two arguments, separated by whitespace. If one argument is specified, it is used as the packet class unconditionally. If two values are specified, the first is automatically selected for interactive sessions and the second for non-interactive sessions. The default is &#8220;lowdelay&#8221; for interactive sessions and &#8220;throughput&#8221; for non-interactive sessions.</p>
<dt><code>KbdInteractiveAuthentication</code></p>
<dd>Specifies whether to use keyboard-interactive authentication. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;yes&#8221;</p>
<dt><code>KbdInteractiveDevices</code></p>
<dd>Specifies the list of methods to use in keyboard-interactive authentication. Multiple method names must be comma-separated. The default is to use the server specified list. The methods available vary depending on what the server supports. For an OpenSSH server, it may be zero or more of: &#8220;bsdauth&#8221; &#8220;pam&#8221; and &#8220;skey&#8221;</p>
<dt><code>KexAlgorithms</code></p>
<dd>Specifies the available KEX (Key Exchange) algorithms. Multiple algorithms must be comma-separated. The default is: </p>
<blockquote>
<pre>curve25519-sha256 [at] libssh.org,
ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,
diffie-hellman-group-exchange-sha256,
diffie-hellman-group-exchange-sha1,
diffie-hellman-group14-sha1,
diffie-hellman-group1-sha1</pre>
</blockquote>
<dt><code>LocalCommand</code></p>
<dd>Specifies a command to execute on the local machine after successfully connecting to the server. The command string extends to the end of the line, and is executed with the user&#8217;s shell. The following escape character substitutions will be performed: `%d&#8217; (local user&#8217;s home directory), `%h&#8217; (remote host name), `%l&#8217; (local host name), `%n&#8217; (host name as provided on the command line), `%p&#8217; (remote port), `%r&#8217; (remote user name) or `%u&#8217; (local user name). The command is run synchronously and does not have access to the session of the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) that spawned it. It should not be used for interactive commands. This directive is ignored unless <code>PermitLocalCommand</code> has been enabled.</p>
<dt><code>LocalForward</code></p>
<dd>Specifies that a TCP port on the local machine be forwarded over the secure channel to the specified host and port from the remote machine. The first argument must be [<i>bind_address : port</i> ] and the second argument must be <i>host : </i><i>hostport</i> IPv6 addresses can be specified by enclosing addresses in square brackets. Multiple forwardings may be specified, and additional forwardings can be given on the command line. Only the superuser can forward privileged ports. By default, the local port is bound in accordance with the <code>GatewayPorts</code> setting. However, an explicit <i>bind_address</i> may be used to bind the connection to a specific address. The <i>bind_address</i> of &#8220;localhost&#8221; indicates that the listening port be bound for local use only, while an empty address or `*&#8217; indicates that the port should be available from all interfaces.</p>
<dt><code>LogLevel</code></p>
<dd>Gives the verbosity level that is used when logging messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The possible values are: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, and DEBUG3. The default is INFO. DEBUG and DEBUG1 are equivalent. DEBUG2 and DEBUG3 each specify higher levels of verbose output.</p>
<dt><code>MACs </code>Specifies the MAC (message authentication code) algorithms</p>
<dd>in order of preference. The MAC algorithm is used in protocol version 2 for data integrity protection. Multiple algorithms must be comma-separated. The algorithms that contain &#8220;-etm&#8221; calculate the MAC after encryption (encrypt-then-mac). These are considered safer and their use recommended. The default is: </p>
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
<dt><code>NoHostAuthenticationForLocalhost</code></p>
<dd>This option can be used if the home directory is shared across machines. In this case localhost will refer to a different machine on each of the machines and the user will get many warnings about changed host keys. However, this option disables host authentication for localhost. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; The default is to check the host key for localhost.</p>
<dt><code>NumberOfPasswordPrompts</code></p>
<dd>Specifies the number of password prompts before giving up. The argument to this keyword must be an integer. The default is 3.</p>
<dt><code>PasswordAuthentication</code></p>
<dd>Specifies whether to use password authentication. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;yes&#8221;</p>
<dt><code>PermitLocalCommand</code></p>
<dd>Allow local command execution via the <code>LocalCommand</code> option or using the <code>! </code><i>command</i> escape sequence in <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221;</p>
<dt><code>PKCS11Provider</code></p>
<dd>Specifies which PKCS#11 provider to use. The argument to this keyword is the PKCS#11 shared library <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should use to communicate with a PKCS#11 token providing the user&#8217;s private RSA key.</p>
<dt><code>Port</code></p>
<dd>Specifies the port number to connect on the remote host. The default is 22.</p>
<dt><code>PreferredAuthentications</code></p>
<dd>Specifies the order in which the client should try protocol 2 authentication methods. This allows a client to prefer one method (e.g. <code>keyboard-interactive</code> over another method (e.g. <code>password )</code> The default is: </p>
<blockquote>
<pre>gssapi-with-mic,hostbased,publickey,
keyboard-interactive,password</pre>
</blockquote>
<dt><code>Protocol</code></p>
<dd>Specifies the protocol versions <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should support in order of preference. The possible values are `1&#8242; and `2&#8242; Multiple versions must be comma-separated. When this option is set to &#8220;2,1&#8221; <code>ssh</code> will try version 2 and fall back to version 1 if version 2 is not available. The default is `2&#8242;</p>
<dt><code>ProxyCommand</code></p>
<dd>Specifies the command to use to connect to the server. The command string extends to the end of the line, and is executed with the user&#8217;s shell. In the command string, any occurrence of `%h&#8217; will be substituted by the host name to connect, `%p&#8217; by the port, and `%r&#8217; by the remote user name. The command can be basically anything, and should read from its standard input and write to its standard output. It should eventually connect an <a href="/docs/linux/man/8-sshd/">sshd</a>(8) server running on some machine, or execute <code>sshd -i</code> somewhere. Host key management will be done using the HostName of the host being connected (defaulting to the name typed by the user). Setting the command to &#8220;none&#8221; disables this option entirely. Note that <code>CheckHostIP</code> is not available for connects with a proxy command. This directive is useful in conjunction with <a href="/docs/linux/man/1-nc/">nc</a>(1) and its proxy support. For example, the following directive would connect via an HTTP proxy at 192.0.2.0: </p>
<pre>ProxyCommand /usr/bin/nc -X connect -x 192.0.2.0:8080 %h %p</pre>
<dt><code>ProxyUseFdpass</code></p>
<dd>Specifies that <code>ProxyCommand</code> will pass a connected file descriptor back to <a href="/docs/linux/man/1-ssh/">ssh</a>(1) instead of continuing to execute and pass data. The default is &#8220;no&#8221;</p>
<dt><code>PubkeyAuthentication</code></p>
<dd>Specifies whether to try public key authentication. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;yes&#8221; This option applies to protocol version 2 only.</p>
<dt><code>RekeyLimit</code></p>
<dd>Specifies the maximum amount of data that may be transmitted before the session key is renegotiated, optionally followed a maximum amount of time that may pass before the session key is renegotiated. The first argument is specified in bytes and may have a suffix of `K&#8217; `M&#8217; or `G&#8217; to indicate Kilobytes, Megabytes, or Gigabytes, respectively. The default is between `1G&#8217; and `4G&#8217; depending on the cipher. The optional second value is specified in seconds and may use any of the units documented in the TIME FORMATS section of sshd_config5. The default value for <code>RekeyLimit</code> is &#8220;default none&#8221; which means that rekeying is performed after the cipher&#8217;s default amount of data has been sent or received and no time based rekeying is done. This option applies to protocol version 2 only.</p>
<dt><code>RemoteForward</code></p>
<dd>Specifies that a TCP port on the remote machine be forwarded over the secure channel to the specified host and port from the local machine. The first argument must be [<i>bind_address : port</i> ] and the second argument must be <i>host : </i><i>hostport</i> IPv6 addresses can be specified by enclosing addresses in square brackets. Multiple forwardings may be specified, and additional forwardings can be given on the command line. Privileged ports can be forwarded only when logging in as root on the remote machine. If the <i>port</i> argument is `0&#8242; , the listen port will be dynamically allocated on the server and reported to the client at run time. If the <i>bind_address</i> is not specified, the default is to only bind to loopback addresses. If the <i>bind_address</i> is `*&#8217; or an empty string, then the forwarding is requested to listen on all interfaces. Specifying a remote <i>bind_address</i> will only succeed if the server&#8217;s <code>GatewayPorts</code> option is enabled (see sshd_config5).</p>
<dt><code>RequestTTY</code></p>
<dd>Specifies whether to request a pseudo-tty for the session. The argument may be one of: &#8220;no&#8221; (never request a TTY), &#8220;yes&#8221; (always request a TTY when standard input is a TTY), &#8220;force&#8221; (always request a TTY) or &#8220;auto&#8221; (request a TTY when opening a login session). This option mirrors the &#8211;<code>t</code> and &#8211;<code>T</code> flags for <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>RhostsRSAAuthentication</code></p>
<dd>Specifies whether to try rhosts based authentication with RSA host authentication. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221; This option applies to protocol version 1 only and requires <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to be setuid root.</p>
<dt><code>RSAAuthentication</code></p>
<dd>Specifies whether to try RSA authentication. The argument to this keyword must be &#8220;yes&#8221; or &#8220;no&#8221; RSA authentication will only be attempted if the identity file exists, or an authentication agent is running. The default is &#8220;yes&#8221; Note that this option applies to protocol version 1 only.</p>
<dt><code>SendEnv</code></p>
<dd>Specifies what variables from the local <a href="/docs/linux/man/7-environ/">environ</a>(7) should be sent to the server. Note that environment passing is only supported for protocol 2. The server must also support it, and the server must be configured to accept these environment variables. Note that the <code>TERM</code> environment variable is always sent whenever a pseudo-terminal is requested as it is required by the protocol. Refer to <code>AcceptEnv</code> in sshd_config5 for how to configure the server. Variables are specified by name, which may contain wildcard characters. Multiple environment variables may be separated by whitespace or spread across multiple <code>SendEnv</code> directives. The default is not to send any environment variables. See Sx PATTERNS for more information on patterns.</p>
<dt><code>ServerAliveCountMax</code></p>
<dd>Sets the number of server alive messages (see below) which may be sent without <a href="/docs/linux/man/1-ssh/">ssh</a>(1) receiving any messages back from the server. If this threshold is reached while server alive messages are being sent, ssh will disconnect from the server, terminating the session. It is important to note that the use of server alive messages is very different from <code>TCPKeepAlive</code> (below). The server alive messages are sent through the encrypted channel and therefore will not be spoofable. The TCP keepalive option enabled by <code>TCPKeepAlive</code> is spoofable. The server alive mechanism is valuable when the client or server depend on knowing when a connection has become inactive. The default value is 3. If, for example, <code>ServerAliveInterval</code> (see below) is set to 15 and <code>ServerAliveCountMax</code> is left at the default, if the server becomes unresponsive, ssh will disconnect after approximately 45 seconds. This option applies to protocol version 2 only.</p>
<dt><code>ServerAliveInterval</code></p>
<dd>Sets a timeout interval in seconds after which if no data has been received from the server, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will send a message through the encrypted channel to request a response from the server. The default is 0, indicating that these messages will not be sent to the server. This option applies to protocol version 2 only.</p>
<dt><code>StrictHostKeyChecking</code></p>
<dd>If this flag is set to &#8220;yes&#8221; <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will never automatically add host keys to the ~/.ssh/known_hosts file, and refuses to connect to hosts whose host key has changed. This provides maximum protection against trojan horse attacks, though it can be annoying when the /etc/gsissh/ssh_known_hosts file is poorly maintained or when connections to new hosts are frequently made. This option forces the user to manually add all new hosts. If this flag is set to &#8220;no&#8221; ssh will automatically add new host keys to the user known hosts files. If this flag is set to &#8220;ask&#8221; new host keys will be added to the user known host files only after the user has confirmed that is what they really want to do, and ssh will refuse to connect to hosts whose host key has changed. The host keys of known hosts will be verified automatically in all cases. The argument must be &#8220;yes&#8221; &#8220;no&#8221; or &#8220;ask&#8221; The default is &#8220;ask&#8221;</p>
<dt><code>TCPKeepAlive</code></p>
<dd>Specifies whether the system should send TCP keepalive messages to the other side. If they are sent, death of the connection or crash of one of the machines will be properly noticed. However, this means that connections will die if the route is down temporarily, and some people find it annoying. The default is &#8220;yes&#8221; (to send TCP keepalive messages), and the client will notice if the network goes down or the remote host dies. This is important in scripts, and many users want it too. To disable TCP keepalive messages, the value should be set to &#8220;no&#8221;</p>
<dt><code>Tunnel</code></p>
<dd>Request <a href="/docs/linux/man/4-tun/">tun</a>(4) device forwarding between the client and the server. The argument must be &#8220;yes&#8221; &#8220;point-to-point&#8221; (layer 3), &#8220;ethernet&#8221; (layer 2), or &#8220;no&#8221; Specifying &#8220;yes&#8221; requests the default tunnel mode, which is &#8220;point-to-point&#8221; The default is &#8220;no&#8221;</p>
<dt><code>TunnelDevice</code></p>
<dd>Specifies the <a href="/docs/linux/man/4-tun/">tun</a>(4) devices to open on the client (<i>local_tun</i> ) and the server (<i>remote_tun</i> ) The argument must be <i>local_tun </i>[: <i>remote_tun</i> ] The devices may be specified by numerical ID or the keyword &#8220;any&#8221; which uses the next available tunnel device. If <i>remote_tun</i> is not specified, it defaults to &#8220;any&#8221; The default is &#8220;any:any&#8221;</p>
<dt><code>UsePrivilegedPort</code></p>
<dd>Specifies whether to use a privileged port for outgoing connections. The argument must be &#8220;yes&#8221; or &#8220;no&#8221; The default is &#8220;no&#8221; If set to &#8220;yes&#8221; <a href="/docs/linux/man/1-ssh/">ssh</a>(1) must be setuid root. Note that this option must be set to &#8220;yes&#8221; for <code>RhostsRSAAuthentication</code> with older servers.</p>
<dt><code>User</code></p>
<dd>Specifies the user to log in as. This can be useful when a different user name is used on different machines. This saves the trouble of having to remember to give the user name on the command line.</p>
<dt><code>UserKnownHostsFile</code></p>
<dd>Specifies one or more files to use for the user host key database, separated by whitespace. The default is ~/.ssh/known_hosts ~/.ssh/known_hosts2</p>
<dt><code>VerifyHostKeyDNS</code></p>
<dd>Specifies whether to verify the remote key using DNS and SSHFP resource records. If this option is set to &#8220;yes&#8221; the client will implicitly trust keys that match a secure fingerprint from DNS. Insecure fingerprints will be handled as if this option was set to &#8220;ask&#8221; If this option is set to &#8220;ask&#8221; information on fingerprint match will be displayed, but the user will still need to confirm new host keys according to the <code>StrictHostKeyChecking</code> option. The argument must be &#8220;yes&#8221; &#8220;no&#8221; or &#8220;ask&#8221; The default is &#8220;no&#8221; Note that this option applies to protocol version 2 only. See also VERIFYING HOST KEYS in <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>VisualHostKey</code></p>
<dd>If this flag is set to &#8220;yes&#8221; an ASCII art representation of the remote host key fingerprint is printed in addition to the hex fingerprint string at login and for unknown host keys. If this flag is set to &#8220;no&#8221; no fingerprint strings are printed at login and only the hex fingerprint string will be printed for unknown host keys. The default is &#8220;no&#8221;</p>
<dt><code>XAuthLocation</code></p>
<dd>Specifies the full pathname of the <a href="/docs/linux/man/1-xauth/">xauth</a>(1) program. The default is /usr/bin/xauth</dl>
<h2>Patterns</h2>
<p>A <i>pattern</i> consists of zero or more non-whitespace characters, `*&#8217; (a wildcard that matches zero or more characters), or `?&#8217; (a wildcard that matches exactly one character). For example, to specify a set of declarations for any host in the &#8220;.co.uk&#8221; set of domains, the following pattern could be used: </p>
<blockquote><p><tt>Host *.co.uk</tt></p></blockquote>
<p> The following pattern would match any host in the 192.168.0.[0-9] network range: </p>
<blockquote><p><tt>Host 192.168.0.?</tt></p></blockquote>
<p> A <i>pattern-list</i> is a comma-separated list of patterns. Patterns within pattern-lists may be negated by preceding them with an exclamation mark (`!&#8217; ) For example, to allow a key to be used from anywhere within an organization except from the &#8220;dialup&#8221; pool, the following entry (in authorized_keys) could be used: </p>
<blockquote><p><tt>from=&quot;!*.dialup.example.com,*.example.com&quot;</tt></p></blockquote>
<h2>Files</h2>
<dl>
<dt><code>~/.ssh/config </code></p>
<dd>This is the per-user configuration file. The format of this file is described above. This file is used by the SSH client. Because of the potential for abuse, this file must have strict permissions: read/write for the user, and not accessible by others.</p>
<dt><code>/etc/gsissh/ssh_config </code></p>
<dd>Systemwide configuration file. This file provides defaults for those values that are not specified in the user&#8217;s configuration file, and for those users who do not have a configuration file. This file must be world-readable.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</p>
<h2>Authors</h2>
<p>OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0.</p>
