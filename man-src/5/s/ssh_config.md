---
title: "ssh_config(5)"
name: "ssh_config"
section: "5"
letter: "s"
url: "/docs/linux/man/5-ssh_config/"
description: "ssh_config – OpenSSH client configuration file"
---

<p><code>ssh_config</code> &#8211; OpenSSH client configuration file</p>
<h2>Description</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1) obtains configuration data from the following sources in the following order:  </p>
<li> command-line options
<li> user&#8217;s configuration file (~/.ssh/config )
<li> system-wide configuration file (/etc/ssh/ssh_config ) </ol>
<p> For each parameter, the first obtained value will be used. The configuration files contain sections separated by <code>Host</code> specifications, and that section is only applied for hosts that match one of the patterns given in the specification. The matched host name is usually the one given on the command line (see the <code>CanonicalizeHostname</code> option for exceptions). Since the first obtained value for each parameter is used, more host-specific declarations should be given near the beginning of the file, and general defaults at the end. Note that the Debian <code>openssh-client</code> package sets several options as standard in /etc/ssh/ssh_config which are not the default in <a href="/docs/linux/man/1-ssh/">ssh</a>(1):  </p>
<li> <code>Include /etc/ssh/ssh_config.d/*.conf</code>
<li> <code>SendEnv LANG LC_*</code>
<li> <code>HashKnownHosts yes</code>
<li> <code>GSSAPIAuthentication yes</code> </ul>
<p> /etc/ssh/ssh_config.d/*.conf files are included at the start of the system-wide configuration file, so options set there will override those in /etc/ssh/ssh_config. The file contains keyword-argument pairs, one per line. Lines starting with `#&#8217; and empty lines are interpreted as comments. Arguments may optionally be enclosed in double quotes () in order to represent arguments containing spaces. Configuration options may be separated by whitespace or optional whitespace and exactly one `=&#8217; ; the latter format is useful to avoid the need to quote whitespace when specifying configuration options using the <code>ssh</code> <code>scp</code> and <code>sftp</code> &#8211;<code>o</code> option. The possible keywords and their meanings are as follows (note that keywords are case-insensitive and arguments are case-sensitive):</p>
<dl>
<dt><code>Host</code></p>
<dd>Restricts the following declarations (up to the next <code>Host</code> or <code>Match</code> keyword) to be only for those hosts that match one of the patterns given after the keyword. If more than one pattern is provided, they should be separated by whitespace. A single `*&#8217; as a pattern can be used to provide global defaults for all hosts. The host is usually the <i>hostname</i> argument given on the command line (see the <code>CanonicalizeHostname</code> keyword for exceptions). A pattern entry may be negated by prefixing it with an exclamation mark (`!&#8217; ) If a negated entry is matched, then the <code>Host</code> entry is ignored, regardless of whether any other patterns on the line match. Negated matches are therefore useful to provide exceptions for wildcard matches. See Sx PATTERNS for more information on patterns.</p>
<dt><code>Match</code></p>
<dd>Restricts the following declarations (up to the next <code>Host</code> or <code>Match</code> keyword) to be used only when the conditions following the <code>Match</code> keyword are satisfied. Match conditions are specified using one or more criteria or the single token <code>all</code> which always matches. The available criteria keywords are: <code>canonical</code> <code>final</code> <code>exec</code> <code>host</code> <code>originalhost</code> <code>user</code> and <code>localuser</code> The <code>all</code> criteria must appear alone or immediately after <code>canonical</code> or <code>final</code> Other criteria may be combined arbitrarily. All criteria but <code>all</code> <code>canonical</code> and <code>final</code> require an argument. Criteria may be negated by prepending an exclamation mark (`!&#8217; ) The <code>canonical</code> keyword matches only when the configuration file is being re-parsed after hostname canonicalization (see the <code>CanonicalizeHostname</code> option). This may be useful to specify conditions that work with canonical host names only. The <code>final</code> keyword requests that the configuration be re-parsed (regardless of whether <code>CanonicalizeHostname</code> is enabled), and matches only during this final pass. If <code>CanonicalizeHostname</code> is enabled, then <code>canonical</code> and <code>final</code> match during the same pass. The <code>exec</code> keyword executes the specified command under the user&#8217;s shell. If the command returns a zero exit status then the condition is considered true. Commands containing whitespace characters must be quoted. Arguments to <code>exec</code> accept the tokens described in the Sx TOKENS section. The other keywords&#8217; criteria must be single entries or comma-separated lists and may use the wildcard and negation operators described in the Sx PATTERNS section. The criteria for the <code>host</code> keyword are matched against the target hostname, after any substitution by the <code>Hostname</code> or <code>CanonicalizeHostname</code> options. The <code>originalhost</code> keyword matches against the hostname as it was specified on the command-line. The <code>user</code> keyword matches against the target username on the remote host. The <code>localuser</code> keyword matches against the name of the local user running <a href="/docs/linux/man/1-ssh/">ssh</a>(1) (this keyword may be useful in system-wide <code>ssh_config</code> files).</p>
<dt><code>AddKeysToAgent</code></p>
<dd>Specifies whether keys should be automatically added to a running ssh-agent1. If this option is set to <code>yes</code> and a key is loaded from a file, the key and its passphrase are added to the agent with the default lifetime, as if by ssh-add1. If this option is set to <code>ask</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will require confirmation using the <code>SSH_ASKPASS</code> program before adding a key (see ssh-add1 for details). If this option is set to <code>confirm</code> each use of the key must be confirmed, as if the &#8211;<code>c</code> option was specified to ssh-add1. If this option is set to <code>no</code> no keys are added to the agent. Alternately, this option may be specified as a time interval using the format described in the Sx TIME FORMATS section of sshd_config5 to specify the key&#8217;s lifetime in ssh-agent1, after which it will automatically be removed. The argument must be <code>no</code> (the default), <code>yes</code> <code>confirm</code> (optionally followed by a time interval), <code>ask</code> or a time interval.</p>
<dt><code>AddressFamily</code></p>
<dd>Specifies which address family to use when connecting. Valid arguments are <code>any</code> (the default), <code>inet</code> (use IPv4 only), or <code>inet6</code> (use IPv6 only).</p>
<dt><code>BatchMode</code></p>
<dd>If set to <code>yes</code> user interaction such as password prompts and host key confirmation requests will be disabled. In addition, the <code>ServerAliveInterval</code> option will be set to 300 seconds by default (Debian-specific). This option is useful in scripts and other batch jobs where no user is present to interact with <a href="/docs/linux/man/1-ssh/">ssh</a>(1), and where it is desirable to detect a broken network swiftly. The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>BindAddress</code></p>
<dd>Use the specified address on the local machine as the source address of the connection. Only useful on systems with more than one address.</p>
<dt><code>BindInterface</code></p>
<dd>Use the address of the specified interface on the local machine as the source address of the connection.</p>
<dt><code>CanonicalDomains</code></p>
<dd>When <code>CanonicalizeHostname</code> is enabled, this option specifies the list of domain suffixes in which to search for the specified destination host.</p>
<dt><code>CanonicalizeFallbackLocal</code></p>
<dd>Specifies whether to fail with an error when hostname canonicalization fails. The default, <code>yes</code> will attempt to look up the unqualified hostname using the system resolver&#8217;s search rules. A value of <code>no</code> will cause <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to fail instantly if <code>CanonicalizeHostname</code> is enabled and the target hostname cannot be found in any of the domains specified by <code>CanonicalDomains</code></p>
<dt><code>CanonicalizeHostname</code></p>
<dd>Controls whether explicit hostname canonicalization is performed. The default, <code>no</code> is not to perform any name rewriting and let the system resolver handle all hostname lookups. If set to <code>yes</code> then, for connections that do not use a <code>ProxyCommand</code> or <code>ProxyJump</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will attempt to canonicalize the hostname specified on the command line using the <code>CanonicalDomains</code> suffixes and <code>CanonicalizePermittedCNAMEs </code>rules. If <code>CanonicalizeHostname</code> is set to <code>always</code> then canonicalization is applied to proxied connections too. If this option is enabled, then the configuration files are processed again using the new target name to pick up any new configuration in matching <code>Host</code> and <code>Match</code> stanzas. A value of <code>none</code> disables the use of a <code>ProxyJump</code> host.</p>
<dt><code>CanonicalizeMaxDots</code></p>
<dd>Specifies the maximum number of dot characters in a hostname before canonicalization is disabled. The default, 1, allows a single dot (i.e. hostname.subdomain).</p>
<dt><code>CanonicalizePermittedCNAMEs </code>Specifies rules to determine whether CNAMEs should be followed when</p>
<dd>canonicalizing hostnames. The rules consist of one or more arguments of <i>source_domain_list : </i><i>target_domain_list</i> where <i>source_domain_list</i> is a pattern-list of domains that may follow CNAMEs in canonicalization, and <i>target_domain_list</i> is a pattern-list of domains that they may resolve to. For example, Qq *.a.example.com:*.b.example.com,*.c.example.com will allow hostnames matching Qq *.a.example.com to be canonicalized to names in the Qq *.b.example.com or Qq *.c.example.com domains. A single argument of Qq none causes no CNAMEs to be considered for canonicalization. This is the default behaviour.</p>
<dt><code>CASignatureAlgorithms</code></p>
<dd>Specifies which algorithms are allowed for signing of certificates by certificate authorities (CAs). The default is: </p>
<blockquote>
<pre>ssh-ed25519,ecdsa-sha2-nistp256,
ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,
sk-ssh-ed25519 [at] openssh.com,
sk-ecdsa-sha2-nistp256 [at] openssh.com,
rsa-sha2-512,rsa-sha2-256</pre>
</blockquote>
<p> If the specified list begins with a `+&#8217; character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will not accept host certificates signed using algorithms other than those specified.</p>
<dt><code>CertificateFile</code></p>
<dd>Specifies a file from which the user&#8217;s certificate is read. A corresponding private key must be provided separately in order to use this certificate either from an <code>IdentityFile</code> directive or &#8211;<code>i</code> flag to <a href="/docs/linux/man/1-ssh/">ssh</a>(1), via ssh-agent1, or via a <code>PKCS11Provider</code> or <code>SecurityKeyProvider</code> Arguments to <code>CertificateFile</code> may use the tilde syntax to refer to a user&#8217;s home directory, the tokens described in the Sx TOKENS section and environment variables as described in the Sx ENVIRONMENT VARIABLES section. It is possible to have multiple certificate files specified in configuration files; these certificates will be tried in sequence. Multiple <code>CertificateFile</code> directives will add to the list of certificates used for authentication.</p>
<dt><code>CheckHostIP</code></p>
<dd>If set to <code>yes</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will additionally check the host IP address in the known_hosts file. This allows it to detect if a host key changed due to DNS spoofing and will add addresses of destination hosts to ~/.ssh/known_hosts in the process, regardless of the setting of <code>StrictHostKeyChecking</code> If the option is set to <code>no</code> (the default), the check will not be executed.</p>
<dt><code>Ciphers</code></p>
<dd>Specifies the ciphers allowed and their order of preference. Multiple ciphers must be comma-separated. If the specified list begins with a `+&#8217; character, then the specified ciphers will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified ciphers (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified ciphers will be placed at the head of the default set. The supported ciphers are: </p>
<blockquote>
<pre>3des-cbc
aes128-cbc
aes192-cbc
aes256-cbc
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm [at] openssh.com
aes256-gcm [at] openssh.com
chacha20-poly1305 [at] openssh.com</pre>
</blockquote>
<p> The default is: </p>
<blockquote>
<pre>chacha20-poly1305 [at] openssh.com,
aes128-ctr,aes192-ctr,aes256-ctr,
aes128-gcm [at] openssh.com,aes256-gcm [at] openssh.com</pre>
</blockquote>
<p> The list of available ciphers may also be obtained using Qq ssh -Q cipher .</p>
<dt><code>ClearAllForwardings</code></p>
<dd>Specifies that all local, remote, and dynamic port forwardings specified in the configuration files or on the command line be cleared. This option is primarily useful when used from the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) command line to clear port forwardings set in configuration files, and is automatically set by <a href="/docs/linux/man/1-scp/">scp</a>(1) and <a href="/docs/linux/man/1-sftp/">sftp</a>(1). The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>Compression</code></p>
<dd>Specifies whether to use compression. The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>ConnectionAttempts</code></p>
<dd>Specifies the number of tries (one per second) to make before exiting. The argument must be an integer. This may be useful in scripts if the connection sometimes fails. The default is 1.</p>
<dt><code>ConnectTimeout</code></p>
<dd>Specifies the timeout (in seconds) used when connecting to the SSH server, instead of using the default system TCP timeout. This timeout is applied both to establishing the connection and to performing the initial SSH protocol handshake and key exchange.</p>
<dt><code>ControlMaster</code></p>
<dd>Enables the sharing of multiple sessions over a single network connection. When set to <code>yes</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will listen for connections on a control socket specified using the <code>ControlPath</code> argument. Additional sessions can connect to this socket using the same <code>ControlPath</code> with <code>ControlMaster</code> set to <code>no</code> (the default). These sessions will try to reuse the master instance&#8217;s network connection rather than initiating new ones, but will fall back to connecting normally if the control socket does not exist, or is not listening. Setting this to <code>ask</code> will cause <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to listen for control connections, but require confirmation using ssh-askpass1. If the <code>ControlPath</code> cannot be opened, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will continue without connecting to a master instance. X11 and ssh-agent1 forwarding is supported over these multiplexed connections, however the display and agent forwarded will be the one belonging to the master connection i.e. it is not possible to forward multiple displays or agents. Two additional options allow for opportunistic multiplexing: try to use a master connection but fall back to creating a new one if one does not already exist. These options are: <code>auto</code> and <code>autoask</code> The latter requires confirmation like the <code>ask</code> option.</p>
<dt><code>ControlPath</code></p>
<dd>Specify the path to the control socket used for connection sharing as described in the <code>ControlMaster</code> section above or the string <code>none</code> to disable connection sharing. Arguments to <code>ControlPath</code> may use the tilde syntax to refer to a user&#8217;s home directory, the tokens described in the Sx TOKENS section and environment variables as described in the Sx ENVIRONMENT VARIABLES section. It is recommended that any <code>ControlPath</code> used for opportunistic connection sharing include at least %h, %p, and %r (or alternatively %C) and be placed in a directory that is not writable by other users. This ensures that shared connections are uniquely identified.</p>
<dt><code>ControlPersist</code></p>
<dd>When used in conjunction with <code>ControlMaster</code> specifies that the master connection should remain open in the background (waiting for future client connections) after the initial client connection has been closed. If set to <code>no</code> (the default), then the master connection will not be placed into the background, and will close as soon as the initial client connection is closed. If set to <code>yes</code> or 0, then the master connection will remain in the background indefinitely (until killed or closed via a mechanism such as the Qq ssh -O exit ) . If set to a time in seconds, or a time in any of the formats documented in sshd_config5, then the backgrounded master connection will automatically terminate after it has remained idle (with no client connections) for the specified time.</p>
<dt><code>DynamicForward</code></p>
<dd>Specifies that a TCP port on the local machine be forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine. The argument must be [<i>bind_address : port</i> ] IPv6 addresses can be specified by enclosing addresses in square brackets. By default, the local port is bound in accordance with the <code>GatewayPorts</code> setting. However, an explicit <i>bind_address</i> may be used to bind the connection to a specific address. The <i>bind_address</i> of <code>localhost</code> indicates that the listening port be bound for local use only, while an empty address or `*&#8217; indicates that the port should be available from all interfaces. Currently the SOCKS4 and SOCKS5 protocols are supported, and <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will act as a SOCKS server. Multiple forwardings may be specified, and additional forwardings can be given on the command line. Only the superuser can forward privileged ports.</p>
<dt><code>EnableSSHKeysign</code></p>
<dd>Setting this option to <code>yes</code> in the global client configuration file /etc/ssh/ssh_config enables the use of the helper program ssh-keysign8 during <code>HostbasedAuthentication</code> The argument must be <code>yes</code> or <code>no</code> (the default). This option should be placed in the non-hostspecific section. See ssh-keysign8 for more information.</p>
<dt><code>EscapeChar</code></p>
<dd>Sets the escape character (default: `~&#8217; ) . The escape character can also be set on the command line. The argument should be a single character, `^&#8217; followed by a letter, or <code>none</code> to disable the escape character entirely (making the connection transparent for binary data).</p>
<dt><code>ExitOnForwardFailure</code></p>
<dd>Specifies whether <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should terminate the connection if it cannot set up all requested dynamic, tunnel, local, and remote port forwardings, (e.g. if either end is unable to bind and listen on a specified port). Note that <code>ExitOnForwardFailure</code> does not apply to connections made over port forwardings and will not, for example, cause <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to exit if TCP connections to the ultimate forwarding destination fail. The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>FingerprintHash</code></p>
<dd>Specifies the hash algorithm used when displaying key fingerprints. Valid options are: <code>md5</code> and <code>sha256</code> (the default).</p>
<dt><code>ForkAfterAuthentication</code></p>
<dd>Requests <code>ssh</code> to go to background just before command execution. This is useful if <code>ssh</code> is going to ask for passwords or passphrases, but the user wants it in the background. This implies the <code>StdinNull</code> configuration option being set to &#8220;yes&#8221; The recommended way to start X11 programs at a remote site is with something like <code>ssh -f host xterm</code> which is the same as <code>ssh host xterm</code> if the <code>ForkAfterAuthentication</code> configuration option is set to &#8220;yes&#8221; If the <code>ExitOnForwardFailure</code> configuration option is set to &#8220;yes&#8221; then a client started with the <code>ForkAfterAuthentication</code> configuration option being set to &#8220;yes&#8221; will wait for all remote port forwards to be successfully established before placing itself in the background. The argument to this keyword must be <code>yes</code> (same as the &#8211;<code>f</code> option) or <code>no</code> (the default).</p>
<dt><code>ForwardAgent</code></p>
<dd>Specifies whether the connection to the authentication agent (if any) will be forwarded to the remote machine. The argument may be <code>yes</code> <code>no</code> (the default), an explicit path to an agent socket or the name of an environment variable (beginning with `$&#8217; in which to find the path. Agent forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the agent&#8217;s Unix-domain socket) can access the local agent through the forwarded connection. An attacker cannot obtain key material from the agent, however they can perform operations on the keys that enable them to authenticate using the identities loaded into the agent.</p>
<dt><code>ForwardX11</code></p>
<dd>Specifies whether X11 connections will be automatically redirected over the secure channel and <code>DISPLAY</code> set. The argument must be <code>yes</code> or <code>no</code> (the default). X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user&#8217;s X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the <code>ForwardX11Trusted</code> option is also enabled.</p>
<dt><code>ForwardX11Timeout</code></p>
<dd>Specify a timeout for untrusted X11 forwarding using the format described in the Sx TIME FORMATS section of sshd_config5. X11 connections received by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) after this time will be refused. Setting <code>ForwardX11Timeout</code> to zero will disable the timeout and permit X11 forwarding for the life of the connection. The default is to disable untrusted X11 forwarding after twenty minutes has elapsed.</p>
<dt><code>ForwardX11Trusted</code></p>
<dd>If this option is set to <code>yes</code> (the Debian-specific default), remote X11 clients will have full access to the original X11 display. If this option is set to <code>no</code> (the upstream default), remote X11 clients will be considered untrusted and prevented from stealing or tampering with data belonging to trusted X11 clients. Furthermore, the <a href="/docs/linux/man/1-xauth/">xauth</a>(1) token used for the session will be set to expire after 20 minutes. Remote clients will be refused access after this time. See the X11 SECURITY extension specification for full details on the restrictions imposed on untrusted clients.</p>
<dt><code>GatewayPorts</code></p>
<dd>Specifies whether remote hosts are allowed to connect to local forwarded ports. By default, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) binds local port forwardings to the loopback address. This prevents other remote hosts from connecting to forwarded ports. <code>GatewayPorts</code> can be used to specify that ssh should bind local port forwardings to the wildcard address, thus allowing remote hosts to connect to forwarded ports. The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>GlobalKnownHostsFile</code></p>
<dd>Specifies one or more files to use for the global host key database, separated by whitespace. The default is /etc/ssh/ssh_known_hosts /etc/ssh/ssh_known_hosts2</p>
<dt><code>GSSAPIAuthentication</code></p>
<dd>Specifies whether user authentication based on GSSAPI is allowed. The default is <code>no</code></p>
<dt><code>GSSAPIClientIdentity</code></p>
<dd>If set, specifies the GSSAPI client identity that ssh should use when connecting to the server. The default is unset, which means that the default identity will be used.</p>
<dt><code>GSSAPIDelegateCredentials</code></p>
<dd>Forward (delegate) credentials to the server. The default is <code>no</code></p>
<dt><code>GSSAPIKeyExchange</code></p>
<dd>Specifies whether key exchange based on GSSAPI may be used. When using GSSAPI key exchange the server need not have a host key. The default is &#8220;no&#8221;</p>
<dt><code>GSSAPIRenewalForcesRekey</code></p>
<dd>If set to &#8220;yes&#8221; then renewal of the client&#8217;s GSSAPI credentials will force the rekeying of the ssh connection. With a compatible server, this will delegate the renewed credentials to a session on the server. Checks are made to ensure that credentials are only propagated when the new credentials match the old ones on the originating client and where the receiving server still has the old set in its cache. The default is &#8220;no&#8221; For this to work <code>GSSAPIKeyExchange</code> needs to be enabled in the server and also used by the client.</p>
<dt><code>GSSAPIServerIdentity</code></p>
<dd>If set, specifies the GSSAPI server identity that ssh should expect when connecting to the server. The default is unset, which means that the expected GSSAPI server identity will be determined from the target hostname.</p>
<dt><code>GSSAPITrustDns</code></p>
<dd>Set to &#8220;yes&#8221; to indicate that the DNS is trusted to securely canonicalize the name of the host being connected to. If &#8220;no&#8221; the hostname entered on the command line will be passed untouched to the GSSAPI library. The default is &#8220;no&#8221;</p>
<dt><code>GSSAPIKexAlgorithms</code></p>
<dd>The list of key exchange algorithms that are offered for GSSAPI key exchange. Possible values are </p>
<pre>gss-gex-sha1-,
gss-group1-sha1-,
gss-group14-sha1-,
gss-group14-sha256-,
gss-group16-sha512-,
gss-nistp256-sha256-,
gss-curve25519-sha256-</pre>
<p>The default is &#8220;gss-group14-sha256-,gss-group16-sha512-,gss-nistp256-sha256-,gss-curve25519-sha256-,gss-gex-sha1-,gss-group14-sha1-&#8221; This option only applies to connections using GSSAPI.</p>
<dt><code>HashKnownHosts</code></p>
<dd>Indicates that <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should hash host names and addresses when they are added to ~/.ssh/known_hosts These hashed names may be used normally by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) and <a href="/docs/linux/man/8-sshd/">sshd</a>(8), but they do not visually reveal identifying information if the file&#8217;s contents are disclosed. The default is <code>no</code> Note that existing names and addresses in known hosts files will not be converted automatically, but may be manually hashed using ssh-keygen1. Use of this option may break facilities such as tab-completion that rely on being able to read unhashed host names from ~/.ssh/known_hosts</p>
<dt><code>HostbasedAcceptedAlgorithms</code></p>
<dd>Specifies the signature algorithms that will be used for hostbased authentication as a comma-separated list of patterns. Alternately if the specified list begins with a `+&#8217; character, then the specified signature algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified signature algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified signature algorithms will be placed at the head of the default set. The default for this option is: </p>
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
<p>The &#8211;<code>Q</code> option of <a href="/docs/linux/man/1-ssh/">ssh</a>(1) may be used to list supported signature algorithms. This was formerly named HostbasedKeyTypes.</p>
<dt><code>HostbasedAuthentication</code></p>
<dd>Specifies whether to try rhosts based authentication with public key authentication. The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>HostKeyAlgorithms</code></p>
<dd>Specifies the host key signature algorithms that the client wants to use in order of preference. Alternately if the specified list begins with a `+&#8217; character, then the specified signature algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified signature algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified signature algorithms will be placed at the head of the default set. The default for this option is: </p>
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
sk-ecdsa-sha2-nistp256 [at] openssh.com,
sk-ssh-ed25519 [at] openssh.com,
rsa-sha2-512,rsa-sha2-256</pre>
<p>If hostkeys are known for the destination host then this default is modified to prefer their algorithms. The list of available signature algorithms may also be obtained using Qq ssh -Q HostKeyAlgorithms .</p>
<dt><code>HostKeyAlias</code></p>
<dd>Specifies an alias that should be used instead of the real host name when looking up or saving the host key in the host key database files and when validating host certificates. This option is useful for tunneling SSH connections or for multiple servers running on a single host.</p>
<dt><code>Hostname</code></p>
<dd>Specifies the real host name to log into. This can be used to specify nicknames or abbreviations for hosts. Arguments to <code>Hostname</code> accept the tokens described in the Sx TOKENS section. Numeric IP addresses are also permitted (both on the command line and in <code>Hostname</code> specifications). The default is the name given on the command line.</p>
<dt><code>IdentitiesOnly</code></p>
<dd>Specifies that <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should only use the configured authentication identity and certificate files (either the default files, or those explicitly configured in the <code>ssh_config</code> files or passed on the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) command-line), even if ssh-agent1 or a <code>PKCS11Provider</code> or <code>SecurityKeyProvider</code> offers more identities. The argument to this keyword must be <code>yes</code> or <code>no</code> (the default). This option is intended for situations where ssh-agent offers many different identities.</p>
<dt><code>IdentityAgent</code></p>
<dd>Specifies the UNIX socket used to communicate with the authentication agent. This option overrides the <code>SSH_AUTH_SOCK</code> environment variable and can be used to select a specific agent. Setting the socket name to <code>none</code> disables the use of an authentication agent. If the string Qq SSH_AUTH_SOCK is specified, the location of the socket will be read from the <code>SSH_AUTH_SOCK</code> environment variable. Otherwise if the specified value begins with a `$&#8217; character, then it will be treated as an environment variable containing the location of the socket. Arguments to <code>IdentityAgent</code> may use the tilde syntax to refer to a user&#8217;s home directory, the tokens described in the Sx TOKENS section and environment variables as described in the Sx ENVIRONMENT VARIABLES section.</p>
<dt><code>IdentityFile</code></p>
<dd>Specifies a file from which the user&#8217;s DSA, ECDSA, authenticator-hosted ECDSA, Ed25519, authenticator-hosted Ed25519 or RSA authentication identity is read. The default is ~/.ssh/id_rsa ~/.ssh/id_ecdsa ~/.ssh/id_ecdsa_sk ~/.ssh/id_ed25519 ~/.ssh/id_ed25519_sk and ~/.ssh/id_dsa Additionally, any identities represented by the authentication agent will be used for authentication unless <code>IdentitiesOnly</code> is set. If no certificates have been explicitly specified by <code>CertificateFile</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will try to load certificate information from the filename obtained by appending -cert.pub to the path of a specified <code>IdentityFile</code> Arguments to <code>IdentityFile</code> may use the tilde syntax to refer to a user&#8217;s home directory or the tokens described in the Sx TOKENS section. It is possible to have multiple identity files specified in configuration files; all these identities will be tried in sequence. Multiple <code>IdentityFile</code> directives will add to the list of identities tried (this behaviour differs from that of other configuration directives). <code>IdentityFile</code> may be used in conjunction with <code>IdentitiesOnly</code> to select which identities in an agent are offered during authentication. <code>IdentityFile</code> may also be used in conjunction with <code>CertificateFile</code> in order to provide any certificate also needed for authentication with the identity.</p>
<dt><code>IgnoreUnknown</code></p>
<dd>Specifies a pattern-list of unknown options to be ignored if they are encountered in configuration parsing. This may be used to suppress errors if <code>ssh_config</code> contains options that are unrecognised by <a href="/docs/linux/man/1-ssh/">ssh</a>(1). It is recommended that <code>IgnoreUnknown</code> be listed early in the configuration file as it will not be applied to unknown options that appear before it.</p>
<dt><code>Include</code></p>
<dd>Include the specified configuration file(s). Multiple pathnames may be specified and each pathname may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) wildcards and, for user configurations, shell-like `~&#8217; references to user home directories. Wildcards will be expanded and processed in lexical order. Files without absolute paths are assumed to be in ~/.ssh if included in a user configuration file or /etc/ssh if included from the system configuration file. <code>Include</code> directive may appear inside a <code>Match</code> or <code>Host</code> block to perform conditional inclusion.</p>
<dt><code>IPQoS</code></p>
<dd>Specifies the IPv4 type-of-service or DSCP class for connections. Accepted values are <code>af11</code> <code>af12</code> <code>af13</code> <code>af21</code> <code>af22</code> <code>af23</code> <code>af31</code> <code>af32</code> <code>af33</code> <code>af41</code> <code>af42</code> <code>af43</code> <code>cs0</code> <code>cs1</code> <code>cs2</code> <code>cs3</code> <code>cs4</code> <code>cs5</code> <code>cs6</code> <code>cs7</code> <code>ef</code> <code>le</code> <code>lowdelay</code> <code>throughput</code> <code>reliability</code> a numeric value, or <code>none</code> to use the operating system default. This option may take one or two arguments, separated by whitespace. If one argument is specified, it is used as the packet class unconditionally. If two values are specified, the first is automatically selected for interactive sessions and the second for non-interactive sessions. The default is <code>lowdelay</code> for interactive sessions and <code>throughput</code> for non-interactive sessions.</p>
<dt><code>KbdInteractiveAuthentication</code></p>
<dd>Specifies whether to use keyboard-interactive authentication. The argument to this keyword must be <code>yes</code> (the default) or <code>no</code> <code>ChallengeResponseAuthentication</code> is a deprecated alias for this.</p>
<dt><code>KbdInteractiveDevices</code></p>
<dd>Specifies the list of methods to use in keyboard-interactive authentication. Multiple method names must be comma-separated. The default is to use the server specified list. The methods available vary depending on what the server supports. For an OpenSSH server, it may be zero or more of: <code>bsdauth</code> and <code>pam</code></p>
<dt><code>KexAlgorithms</code></p>
<dd>Specifies the available KEX (Key Exchange) algorithms. Multiple algorithms must be comma-separated. If the specified list begins with a `+&#8217; character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified algorithms will be placed at the head of the default set. The default is: </p>
<blockquote>
<pre>curve25519-sha256,curve25519-sha256 [at] libssh.org,
ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,
sntrup761x25519-sha512 [at] openssh.com,
diffie-hellman-group-exchange-sha256,
diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,
diffie-hellman-group14-sha256</pre>
</blockquote>
<p> The list of available key exchange algorithms may also be obtained using Qq ssh -Q kex .</p>
<dt><code>KnownHostsCommand</code></p>
<dd>Specifies a command to use to obtain a list of host keys, in addition to those listed in <code>UserKnownHostsFile</code> and <code>GlobalKnownHostsFile</code> This command is executed after the files have been read. It may write host key lines to standard output in identical format to the usual files (described in the Sx VERIFYING HOST KEYS section in <a href="/docs/linux/man/1-ssh/">ssh</a>(1)). Arguments to <code>KnownHostsCommand</code> accept the tokens described in the Sx TOKENS section. The command may be invoked multiple times per connection: once when preparing the preference list of host key algorithms to use, again to obtain the host key for the requested host name and, if <code>CheckHostIP</code> is enabled, one more time to obtain the host key matching the server&#8217;s address. If the command exits abnormally or returns a non-zero exit status then the connection is terminated.</p>
<dt><code>LocalCommand</code></p>
<dd>Specifies a command to execute on the local machine after successfully connecting to the server. The command string extends to the end of the line, and is executed with the user&#8217;s shell. Arguments to <code>LocalCommand</code> accept the tokens described in the Sx TOKENS section. The command is run synchronously and does not have access to the session of the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) that spawned it. It should not be used for interactive commands. This directive is ignored unless <code>PermitLocalCommand</code> has been enabled.</p>
<dt><code>LocalForward</code></p>
<dd>Specifies that a TCP port on the local machine be forwarded over the secure channel to the specified host and port from the remote machine. The first argument specifies the listener and may be [<i>bind_address : port</i> ] or a Unix domain socket path. The second argument is the destination and may be <i>host : </i><i>hostport</i> or a Unix domain socket path if the remote host supports it. IPv6 addresses can be specified by enclosing addresses in square brackets. Multiple forwardings may be specified, and additional forwardings can be given on the command line. Only the superuser can forward privileged ports. By default, the local port is bound in accordance with the <code>GatewayPorts</code> setting. However, an explicit <i>bind_address</i> may be used to bind the connection to a specific address. The <i>bind_address</i> of <code>localhost</code> indicates that the listening port be bound for local use only, while an empty address or `*&#8217; indicates that the port should be available from all interfaces. Unix domain socket paths may use the tokens described in the Sx TOKENS section and environment variables as described in the Sx ENVIRONMENT VARIABLES section.</p>
<dt><code>LogLevel</code></p>
<dd>Gives the verbosity level that is used when logging messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The possible values are: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, and DEBUG3. The default is INFO. DEBUG and DEBUG1 are equivalent. DEBUG2 and DEBUG3 each specify higher levels of verbose output.</p>
<dt><code>LogVerbose</code></p>
<dd>Specify one or more overrides to LogLevel. An override consists of a pattern lists that matches the source file, function and line number to force detailed logging for. For example, an override pattern of: </p>
<blockquote>
<pre>kex.c:*:1000,*:kex_exchange_identification():*,packet.c:*</pre>
</blockquote>
<p> would enable detailed logging for line 1000 of kex.c everything in the Fn kex_exchange_identification function, and all code in the packet.c file. This option is intended for debugging and no overrides are enabled by default.</p>
<dt><code>MACs </code>Specifies the MAC (message authentication code) algorithms</p>
<dd>in order of preference. The MAC algorithm is used for data integrity protection. Multiple algorithms must be comma-separated. If the specified list begins with a `+&#8217; character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified algorithms will be placed at the head of the default set. The algorithms that contain Qq -etm calculate the MAC after encryption (encrypt-then-mac). These are considered safer and their use recommended. The default is: </p>
<blockquote>
<pre>umac-64-etm [at] openssh.com,umac-128-etm [at] openssh.com,
hmac-sha2-256-etm [at] openssh.com,hmac-sha2-512-etm [at] openssh.com,
hmac-sha1-etm [at] openssh.com,
umac-64 [at] openssh.com,umac-128 [at] openssh.com,
hmac-sha2-256,hmac-sha2-512,hmac-sha1</pre>
</blockquote>
<p> The list of available MAC algorithms may also be obtained using Qq ssh -Q mac .</p>
<dt><code>NoHostAuthenticationForLocalhost</code></p>
<dd>Disable host authentication for localhost (loopback addresses). The argument to this keyword must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>NumberOfPasswordPrompts</code></p>
<dd>Specifies the number of password prompts before giving up. The argument to this keyword must be an integer. The default is 3.</p>
<dt><code>PasswordAuthentication</code></p>
<dd>Specifies whether to use password authentication. The argument to this keyword must be <code>yes</code> (the default) or <code>no</code></p>
<dt><code>PermitLocalCommand</code></p>
<dd>Allow local command execution via the <code>LocalCommand</code> option or using the <code>! </code><i>command</i> escape sequence in <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>PermitRemoteOpen</code></p>
<dd>Specifies the destinations to which remote TCP port forwarding is permitted when <code>RemoteForward</code> is used as a SOCKS proxy. The forwarding specification must be one of the following forms: </p>
<dt><code>PermitRemoteOpen</code></p>
<dd><i>host : port</i></p>
<dt><code>PermitRemoteOpen</code></p>
<dd><i>IPv4_addr : port</i></p>
<dt><code>PermitRemoteOpen</code></p>
<dd><i>[ IPv6_addr ] : port</i></dl>
<p> Multiple forwards may be specified by separating them with whitespace. An argument of <code>any</code> can be used to remove all restrictions and permit any forwarding requests. An argument of <code>none</code> can be used to prohibit all forwarding requests. The wildcard `*&#8217; can be used for host or port to allow all hosts or ports respectively. Otherwise, no pattern matching or address lookups are performed on supplied names.</p>
<dt><code>PKCS11Provider</code></p>
<dd>Specifies which PKCS#11 provider to use or <code>none</code> to indicate that no provider should be used (the default). The argument to this keyword is a path to the PKCS#11 shared library <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should use to communicate with a PKCS#11 token providing keys for user authentication.</p>
<dt><code>Port</code></p>
<dd>Specifies the port number to connect on the remote host. The default is 22.</p>
<dt><code>PreferredAuthentications</code></p>
<dd>Specifies the order in which the client should try authentication methods. This allows a client to prefer one method (e.g. <code>keyboard-interactive</code> over another method (e.g. <code>password )</code> The default is: </p>
<blockquote>
<pre>gssapi-with-mic,hostbased,publickey,
keyboard-interactive,password</pre>
</blockquote>
<dt><code>ProxyCommand</code></p>
<dd>Specifies the command to use to connect to the server. The command string extends to the end of the line, and is executed using the user&#8217;s shell `exec&#8217; directive to avoid a lingering shell process. Arguments to <code>ProxyCommand</code> accept the tokens described in the Sx TOKENS section. The command can be basically anything, and should read from its standard input and write to its standard output. It should eventually connect an <a href="/docs/linux/man/8-sshd/">sshd</a>(8) server running on some machine, or execute <code>sshd -i</code> somewhere. Host key management will be done using the <code>Hostname</code> of the host being connected (defaulting to the name typed by the user). Setting the command to <code>none</code> disables this option entirely. Note that <code>CheckHostIP</code> is not available for connects with a proxy command. This directive is useful in conjunction with <a href="/docs/linux/man/1-nc/">nc</a>(1) and its proxy support. For example, the following directive would connect via an HTTP proxy at 192.0.2.0: </p>
<pre>ProxyCommand /usr/bin/nc -X connect -x 192.0.2.0:8080 %h %p</pre>
<dt><code>ProxyJump</code></p>
<dd>Specifies one or more jump proxies as either [<i>user </i><code>@</code> ] <i>host</i> [: <i>port</i> ] or an ssh URI . Multiple proxies may be separated by comma characters and will be visited sequentially. Setting this option will cause <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to connect to the target host by first making a <a href="/docs/linux/man/1-ssh/">ssh</a>(1) connection to the specified <code>ProxyJump</code> host and then establishing a TCP forwarding to the ultimate target from there. Setting the host to <code>none</code> disables this option entirely. Note that this option will compete with the <code>ProxyCommand</code> option &#8211; whichever is specified first will prevent later instances of the other from taking effect. Note also that the configuration for the destination host (either supplied via the command-line or the configuration file) is not generally applied to jump hosts. ~/.ssh/config should be used if specific configuration is required for jump hosts.</p>
<dt><code>ProxyUseFdpass</code></p>
<dd>Specifies that <code>ProxyCommand</code> will pass a connected file descriptor back to <a href="/docs/linux/man/1-ssh/">ssh</a>(1) instead of continuing to execute and pass data. The default is <code>no</code></p>
<dt><code>PubkeyAcceptedAlgorithms</code></p>
<dd>Specifies the signature algorithms that will be used for public key authentication as a comma-separated list of patterns. If the specified list begins with a `+&#8217; character, then the algorithms after it will be appended to the default instead of replacing it. If the specified list begins with a `-&#8216; character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a `^&#8217; character, then the specified algorithms will be placed at the head of the default set. The default for this option is: </p>
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
<dt><code>PubkeyAuthentication</code></p>
<dd>Specifies whether to try public key authentication. The argument to this keyword must be <code>yes</code> (the default), <code>no</code> <code>unbound</code> or <code>host-bound</code> The final two options enable public key authentication while respectively disabling or enabling the OpenSSH host-bound authentication protocol extension required for restricted ssh-agent1 forwarding.</p>
<dt><code>RekeyLimit</code></p>
<dd>Specifies the maximum amount of data that may be transmitted before the session key is renegotiated, optionally followed by a maximum amount of time that may pass before the session key is renegotiated. The first argument is specified in bytes and may have a suffix of `K&#8217; `M&#8217; or `G&#8217; to indicate Kilobytes, Megabytes, or Gigabytes, respectively. The default is between `1G&#8217; and `4G&#8217; depending on the cipher. The optional second value is specified in seconds and may use any of the units documented in the TIME FORMATS section of sshd_config5. The default value for <code>RekeyLimit</code> is <code>default none</code> which means that rekeying is performed after the cipher&#8217;s default amount of data has been sent or received and no time based rekeying is done.</p>
<dt><code>RemoteCommand</code></p>
<dd>Specifies a command to execute on the remote machine after successfully connecting to the server. The command string extends to the end of the line, and is executed with the user&#8217;s shell. Arguments to <code>RemoteCommand</code> accept the tokens described in the Sx TOKENS section.</p>
<dt><code>RemoteForward</code></p>
<dd>Specifies that a TCP port on the remote machine be forwarded over the secure channel. The remote port may either be forwarded to a specified host and port from the local machine, or may act as a SOCKS 4/5 proxy that allows a remote client to connect to arbitrary destinations from the local machine. The first argument is the listening specification and may be [<i>bind_address : port</i> ] or, if the remote host supports it, a Unix domain socket path. If forwarding to a specific destination then the second argument must be <i>host : </i><i>hostport</i> or a Unix domain socket path, otherwise if no destination argument is specified then the remote forwarding will be established as a SOCKS proxy. When acting as a SOCKS proxy the destination of the connection can be restricted by <code>PermitRemoteOpen</code> IPv6 addresses can be specified by enclosing addresses in square brackets. Multiple forwardings may be specified, and additional forwardings can be given on the command line. Privileged ports can be forwarded only when logging in as root on the remote machine. Unix domain socket paths may use the tokens described in the Sx TOKENS section and environment variables as described in the Sx ENVIRONMENT VARIABLES section. If the <i>port</i> argument is 0, the listen port will be dynamically allocated on the server and reported to the client at run time. If the <i>bind_address</i> is not specified, the default is to only bind to loopback addresses. If the <i>bind_address</i> is `*&#8217; or an empty string, then the forwarding is requested to listen on all interfaces. Specifying a remote <i>bind_address</i> will only succeed if the server&#8217;s <code>GatewayPorts</code> option is enabled (see sshd_config5).</p>
<dt><code>RequestTTY</code></p>
<dd>Specifies whether to request a pseudo-tty for the session. The argument may be one of: <code>no</code> (never request a TTY), <code>yes</code> (always request a TTY when standard input is a TTY), <code>force</code> (always request a TTY) or <code>auto</code> (request a TTY when opening a login session). This option mirrors the &#8211;<code>t</code> and &#8211;<code>T</code> flags for <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>RevokedHostKeys</code></p>
<dd>Specifies revoked host public keys. Keys listed in this file will be refused for host authentication. Note that if this file does not exist or is not readable, then host authentication will be refused for all hosts. Keys may be specified as a text file, listing one public key per line, or as an OpenSSH Key Revocation List (KRL) as generated by ssh-keygen1. For more information on KRLs, see the KEY REVOCATION LISTS section in ssh-keygen1.</p>
<dt><code>SecurityKeyProvider</code></p>
<dd>Specifies a path to a library that will be used when loading any FIDO authenticator-hosted keys, overriding the default of using the built-in USB HID support. If the specified value begins with a `$&#8217; character, then it will be treated as an environment variable containing the path to the library.</p>
<dt><code>SendEnv</code></p>
<dd>Specifies what variables from the local <a href="/docs/linux/man/7-environ/">environ</a>(7) should be sent to the server. The server must also support it, and the server must be configured to accept these environment variables. Note that the <code>TERM</code> environment variable is always sent whenever a pseudo-terminal is requested as it is required by the protocol. Refer to <code>AcceptEnv</code> in sshd_config5 for how to configure the server. Variables are specified by name, which may contain wildcard characters. Multiple environment variables may be separated by whitespace or spread across multiple <code>SendEnv</code> directives. See Sx PATTERNS for more information on patterns. It is possible to clear previously set <code>SendEnv</code> variable names by prefixing patterns with &#8211; The default is not to send any environment variables.</p>
<dt><code>ServerAliveCountMax</code></p>
<dd>Sets the number of server alive messages (see below) which may be sent without <a href="/docs/linux/man/1-ssh/">ssh</a>(1) receiving any messages back from the server. If this threshold is reached while server alive messages are being sent, ssh will disconnect from the server, terminating the session. It is important to note that the use of server alive messages is very different from <code>TCPKeepAlive</code> (below). The server alive messages are sent through the encrypted channel and therefore will not be spoofable. The TCP keepalive option enabled by <code>TCPKeepAlive</code> is spoofable. The server alive mechanism is valuable when the client or server depend on knowing when a connection has become unresponsive. The default value is 3. If, for example, <code>ServerAliveInterval</code> (see below) is set to 15 and <code>ServerAliveCountMax</code> is left at the default, if the server becomes unresponsive, ssh will disconnect after approximately 45 seconds.</p>
<dt><code>ServerAliveInterval</code></p>
<dd>Sets a timeout interval in seconds after which if no data has been received from the server, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will send a message through the encrypted channel to request a response from the server. The default is 0, indicating that these messages will not be sent to the server, or 300 if the <code>BatchMode</code> option is set (Debian-specific). <code>ProtocolKeepAlives</code> and <code>SetupTimeOut</code> are Debian-specific compatibility aliases for this option.</p>
<dt><code>SessionType</code></p>
<dd>May be used to either request invocation of a subsystem on the remote system, or to prevent the execution of a remote command at all. The latter is useful for just forwarding ports. The argument to this keyword must be <code>none</code> (same as the &#8211;<code>N</code> option), <code>subsystem</code> (same as the &#8211;<code>s</code> option) or <code>default</code> (shell or command execution).</p>
<dt><code>SetEnv</code></p>
<dd>Directly specify one or more environment variables and their contents to be sent to the server. Similarly to <code>SendEnv</code> with the exception of the <code>TERM</code> variable, the server must be prepared to accept the environment variable.</p>
<dt><code>StdinNull</code></p>
<dd>Redirects stdin from /dev/null (actually, prevents reading from stdin). Either this or the equivalent &#8211;<code>n</code> option must be used when <code>ssh</code> is run in the background. The argument to this keyword must be <code>yes</code> (same as the &#8211;<code>n</code> option) or <code>no</code> (the default).</p>
<dt><code>StreamLocalBindMask</code></p>
<dd>Sets the octal file creation mode mask (umask) used when creating a Unix-domain socket file for local or remote port forwarding. This option is only used for port forwarding to a Unix-domain socket file. The default value is 0177, which creates a Unix-domain socket file that is readable and writable only by the owner. Note that not all operating systems honor the file mode on Unix-domain socket files.</p>
<dt><code>StreamLocalBindUnlink</code></p>
<dd>Specifies whether to remove an existing Unix-domain socket file for local or remote port forwarding before creating a new one. If the socket file already exists and <code>StreamLocalBindUnlink</code> is not enabled, <code>ssh</code> will be unable to forward the port to the Unix-domain socket file. This option is only used for port forwarding to a Unix-domain socket file. The argument must be <code>yes</code> or <code>no</code> (the default).</p>
<dt><code>StrictHostKeyChecking</code></p>
<dd>If this flag is set to <code>yes</code> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will never automatically add host keys to the ~/.ssh/known_hosts file, and refuses to connect to hosts whose host key has changed. This provides maximum protection against man-in-the-middle (MITM) attacks, though it can be annoying when the /etc/ssh/ssh_known_hosts file is poorly maintained or when connections to new hosts are frequently made. This option forces the user to manually add all new hosts. If this flag is set to <code>accept-new</code> then ssh will automatically add new host keys to the user&#8217;s known_hosts file, but will not permit connections to hosts with changed host keys. If this flag is set to <code>no</code> or <code>off</code> ssh will automatically add new host keys to the user known hosts files and allow connections to hosts with changed hostkeys to proceed, subject to some restrictions. If this flag is set to <code>ask</code> (the default), new host keys will be added to the user known host files only after the user has confirmed that is what they really want to do, and ssh will refuse to connect to hosts whose host key has changed. The host keys of known hosts will be verified automatically in all cases.</p>
<dt><code>SyslogFacility</code></p>
<dd>Gives the facility code that is used when logging messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1). The possible values are: DAEMON, USER, AUTH, LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7. The default is USER.</p>
<dt><code>TCPKeepAlive</code></p>
<dd>Specifies whether the system should send TCP keepalive messages to the other side. If they are sent, death of the connection or crash of one of the machines will be properly noticed. This option only uses TCP keepalives (as opposed to using ssh level keepalives), so takes a long time to notice when the connection dies. As such, you probably want the <code>ServerAliveInterval</code> option as well. However, this means that connections will die if the route is down temporarily, and some people find it annoying. The default is <code>yes</code> (to send TCP keepalive messages), and the client will notice if the network goes down or the remote host dies. This is important in scripts, and many users want it too. To disable TCP keepalive messages, the value should be set to <code>no</code> See also <code>ServerAliveInterval</code> for protocol-level keepalives.</p>
<dt><code>Tunnel</code></p>
<dd>Request <a href="/docs/linux/man/4-tun/">tun</a>(4) device forwarding between the client and the server. The argument must be <code>yes</code> <code>point-to-point</code> (layer 3), <code>ethernet</code> (layer 2), or <code>no</code> (the default). Specifying <code>yes</code> requests the default tunnel mode, which is <code>point-to-point</code></p>
<dt><code>TunnelDevice</code></p>
<dd>Specifies the <a href="/docs/linux/man/4-tun/">tun</a>(4) devices to open on the client (<i>local_tun</i> ) and the server (<i>remote_tun</i> ) The argument must be <i>local_tun </i>[: <i>remote_tun</i> ] The devices may be specified by numerical ID or the keyword <code>any</code> which uses the next available tunnel device. If <i>remote_tun</i> is not specified, it defaults to <code>any</code> The default is <code>any:any</code></p>
<dt><code>UpdateHostKeys</code></p>
<dd>Specifies whether <a href="/docs/linux/man/1-ssh/">ssh</a>(1) should accept notifications of additional hostkeys from the server sent after authentication has completed and add them to <code>UserKnownHostsFile</code> The argument must be <code>yes</code> <code>no</code> or <code>ask</code> This option allows learning alternate hostkeys for a server and supports graceful key rotation by allowing a server to send replacement public keys before old ones are removed. Additional hostkeys are only accepted if the key used to authenticate the host was already trusted or explicitly accepted by the user, the host was authenticated via <code>UserKnownHostsFile</code> (i.e. not <code>GlobalKnownHostsFile</code> and the host was authenticated using a plain key and not a certificate. <code>UpdateHostKeys</code> is enabled by default if the user has not overridden the default <code>UserKnownHostsFile</code> setting and has not enabled <code>VerifyHostKeyDNS</code> otherwise <code>UpdateHostKeys</code> will be set to <code>no</code> If <code>UpdateHostKeys</code> is set to <code>ask</code> then the user is asked to confirm the modifications to the known_hosts file. Confirmation is currently incompatible with <code>ControlPersist</code> and will be disabled if it is enabled. Presently, only <a href="/docs/linux/man/8-sshd/">sshd</a>(8) from OpenSSH 6.8 and greater support the Qq hostkeys [at] openssh.com protocol extension used to inform the client of all the server&#8217;s hostkeys.</p>
<dt><code>User</code></p>
<dd>Specifies the user to log in as. This can be useful when a different user name is used on different machines. This saves the trouble of having to remember to give the user name on the command line.</p>
<dt><code>UserKnownHostsFile</code></p>
<dd>Specifies one or more files to use for the user host key database, separated by whitespace. Each filename may use tilde notation to refer to the user&#8217;s home directory, the tokens described in the Sx TOKENS section and environment variables as described in the Sx ENVIRONMENT VARIABLES section. The default is ~/.ssh/known_hosts ~/.ssh/known_hosts2</p>
<dt><code>VerifyHostKeyDNS</code></p>
<dd>Specifies whether to verify the remote key using DNS and SSHFP resource records. If this option is set to <code>yes</code> the client will implicitly trust keys that match a secure fingerprint from DNS. Insecure fingerprints will be handled as if this option was set to <code>ask</code> If this option is set to <code>ask</code> information on fingerprint match will be displayed, but the user will still need to confirm new host keys according to the <code>StrictHostKeyChecking</code> option. The default is <code>no</code> See also Sx VERIFYING HOST KEYS in <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>VisualHostKey</code></p>
<dd>If this flag is set to <code>yes</code> an ASCII art representation of the remote host key fingerprint is printed in addition to the fingerprint string at login and for unknown host keys. If this flag is set to <code>no</code> (the default), no fingerprint strings are printed at login and only the fingerprint string will be printed for unknown host keys.</p>
<dt><code>XAuthLocation</code></p>
<dd>Specifies the full pathname of the <a href="/docs/linux/man/1-xauth/">xauth</a>(1) program. The default is /usr/bin/xauth</dl>
<h2>Patterns</h2>
<p>A <i>pattern</i> consists of zero or more non-whitespace characters, `*&#8217; (a wildcard that matches zero or more characters), or `?&#8217; (a wildcard that matches exactly one character). For example, to specify a set of declarations for any host in the Qq .co.uk set of domains, the following pattern could be used: </p>
<blockquote><p><tt>Host *.co.uk</tt></p></blockquote>
<p> The following pattern would match any host in the 192.168.0.[0-9] network range: </p>
<blockquote><p><tt>Host 192.168.0.?</tt></p></blockquote>
<p> A <i>pattern-list</i> is a comma-separated list of patterns. Patterns within pattern-lists may be negated by preceding them with an exclamation mark (`!&#8217; ) For example, to allow a key to be used from anywhere within an organization except from the Qq dialup pool, the following entry (in authorized_keys) could be used: </p>
<blockquote><p><tt>from=&quot;!*.dialup.example.com,*.example.com&quot;</tt></p></blockquote>
<p> Note that a negated match will never produce a positive result by itself. For example, attempting to match Qq host3 against the following pattern-list will fail: </p>
<blockquote><p><tt>from=&quot;!host1,!host2&quot;</tt></p></blockquote>
<p> The solution here is to include a term that will yield a positive match, such as a wildcard: </p>
<blockquote><p><tt>from=&quot;!host1,!host2,*&quot;</tt></p></blockquote>
<h2>Tokens</h2>
<p>Arguments to some keywords can make use of tokens, which are expanded at runtime: </p>
<dl>
<dt><code>%%</code></p>
<dd>A literal `%&#8217;</p>
<dt><code>%C</code></p>
<dd>Hash of %l%h%p%r.</p>
<dt><code>%d</code></p>
<dd>Local user&#8217;s home directory.</p>
<dt><code>%f</code></p>
<dd>The fingerprint of the server&#8217;s host key.</p>
<dt><code>%H</code></p>
<dd>The known_hosts hostname or address that is being searched for.</p>
<dt><code>%h</code></p>
<dd>The remote hostname.</p>
<dt><code>%I</code></p>
<dd>A string describing the reason for a <code>KnownHostsCommand</code> execution: either <code>ADDRESS</code> when looking up a host by address (only when <code>CheckHostIP</code> is enabled), <code>HOSTNAME</code> when searching by hostname, or <code>ORDER</code> when preparing the host key algorithm preference list to use for the destination host.</p>
<dt><code>%i</code></p>
<dd>The local user ID.</p>
<dt><code>%K</code></p>
<dd>The base64 encoded host key.</p>
<dt><code>%k</code></p>
<dd>The host key alias if specified, otherwise the original remote hostname given on the command line.</p>
<dt><code>%L</code></p>
<dd>The local hostname.</p>
<dt><code>%l</code></p>
<dd>The local hostname, including the domain name.</p>
<dt><code>%n</code></p>
<dd>The original remote hostname, as given on the command line.</p>
<dt><code>%p</code></p>
<dd>The remote port.</p>
<dt><code>%r</code></p>
<dd>The remote username.</p>
<dt><code>%T</code></p>
<dd>The local <a href="/docs/linux/man/4-tun/">tun</a>(4) or <a href="/docs/linux/man/4-tap/">tap</a>(4) network interface assigned if tunnel forwarding was requested, or Qq NONE otherwise.</p>
<dt><code>%t</code></p>
<dd>The type of the server host key, e.g. <code>ssh-ed25519</code></p>
<dt><code>%u</code></p>
<dd>The local username.</dl>
<p> <code>CertificateFile</code> <code>ControlPath</code> <code>IdentityAgent</code> <code>IdentityFile</code> <code>KnownHostsCommand</code> <code>LocalForward</code> <code>Match exec</code> <code>RemoteCommand</code> <code>RemoteForward</code> and <code>UserKnownHostsFile</code> accept the tokens %%, %C, %d, %h, %i, %k, %L, %l, %n, %p, %r, and %u. </p>
<p> <code>KnownHostsCommand</code> additionally accepts the tokens %f, %H, %I, %K and %t. </p>
<p> <code>Hostname</code> accepts the tokens %% and %h. </p>
<p> <code>LocalCommand</code> accepts all tokens. </p>
<p> <code>ProxyCommand</code> accepts the tokens %%, %h, %n, %p, and %r.</p>
<h2>Environment Variables</h2>
<p>Arguments to some keywords can be expanded at runtime from environment variables on the client by enclosing them in <code>${}</code> for example <code>${HOME}/.ssh</code> would refer to the user&#8217;s .ssh directory. If a specified environment variable does not exist then an error will be returned and the setting for that keyword will be ignored. </p>
<p> The keywords <code>CertificateFile</code> <code>ControlPath</code> <code>IdentityAgent</code> <code>IdentityFile</code> <code>KnownHostsCommand</code> and <code>UserKnownHostsFile</code> support environment variables. The keywords <code>LocalForward</code> and <code>RemoteForward</code> support environment variables only for Unix domain socket paths.</p>
<h2>Files</h2>
<dl>
<dt><code>~/.ssh/config </code></p>
<dd>This is the per-user configuration file. The format of this file is described above. This file is used by the SSH client. Because of the potential for abuse, this file must have strict permissions: read/write for the user, and not writable by others. It may be group-writable provided that the group in question contains only the user.</p>
<dt><code>/etc/ssh/ssh_config </code></p>
<dd>Systemwide configuration file. This file provides defaults for those values that are not specified in the user&#8217;s configuration file, and for those users who do not have a configuration file. This file must be world-readable.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</p>
<h2>Authors</h2>
<p>An -nosplit OpenSSH is a derivative of the original and free ssh 1.2.12 release by An Tatu Ylonen . An Aaron Campbell , Bob Beck , Markus Friedl , An Niels Provos , Theo de Raadt and An Dug Song removed many bugs, re-added newer features and created OpenSSH. An Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0.</p>
