---
title: "rlogin(1)"
name: "rlogin"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rlogin/"
description: "ssh – OpenSSH remote login client"
---

<h2 class="name">NAME</h2>
<p> <code>ssh</code> &#8211; OpenSSH remote login client </p>
<h2>SYNOPSIS</h2>
<p> <code>ssh</code> [-<code>46AaCfGgKkMNnqsTtVvXxYy </code>[-<code>B </code><i>bind_interface</i> ] ] [-<code>b </code><i>bind_address</i> ] [-<code>c </code><i>cipher_spec</i> ] [-<code>D </code>[<i>bind_address : </i><i>port</i> ] ] [-<code>E </code><i>log_file</i> ] [-<code>e </code><i>escape_char</i> ] [-<code>F </code><i>configfile</i> ] [-<code>I </code><i>pkcs11</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>J </code><i>destination</i> ] [-<code>L </code><i>address</i> ] [-<code>l </code><i>login_name</i> ] [-<code>m </code><i>mac_spec</i> ] [-<code>O </code><i>ctl_cmd</i> ] [-<code>o </code><i>option</i> ] [-<code>p </code><i>port</i> ] [-<code>Q </code><i>query_option</i> ] [-<code>R </code><i>address</i> ] [-<code>S </code><i>ctl_path</i> ] [-<code>W </code><i>host : </i><i>port</i> ] [-<code>w </code><i>local_tun </i>[: <i>remote_tun</i> ] ] <i>destination</i> [<i>command </i>[<i>argument &#8230;</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ssh</code> (SSH client) is a program for logging into a remote machine and for executing commands on a remote machine. It is intended to provide secure encrypted communications between two untrusted hosts over an insecure network. X11 connections, arbitrary TCP ports and UNIX sockets can also be forwarded over the secure channel. </p>
<p> <code>ssh</code> connects and logs into the specified <i>destination</i> which may be specified as either [user @ hostname] or a URI of the form <code>ssh:// </code>[user @ hostname [: port] ] The user must prove their identity to the remote machine using one of several methods (see below). </p>
<p> If a <i>command</i> is specified, it will be executed on the remote host instead of a login shell. A complete command line may be specified as <i>command</i> or it may have additional arguments. If supplied, the arguments will be appended to the command, separated by spaces, before it is sent to the server to be executed. </p>
<p> The options are as follows: </p>
<dl>
<dt><code>-4</code></p>
<dd> Forces <code>ssh</code> to use IPv4 addresses only. </p>
<dt><code>-6</code></p>
<dd> Forces <code>ssh</code> to use IPv6 addresses only. </p>
<dt><code>-A</code></p>
<dd> Enables forwarding of connections from an authentication agent such as ssh-agent1. This can also be specified on a per-host basis in a configuration file. </p>
<p> Agent forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the agent&#8217;s UNIX socket) can access the local agent through the forwarded connection. An attacker cannot obtain key material from the agent, however they can perform operations on the keys that enable them to authenticate using the identities loaded into the agent. A safer alternative may be to use a jump host (see &#8211;<code>J )</code> </p>
<dt><code>-a</code></p>
<dd> Disables forwarding of the authentication agent connection. </p>
<dt><code>-B </code><i>bind_interface</i></p>
<dd> Bind to the address of <i>bind_interface</i> before attempting to connect to the destination host. This is only useful on systems with more than one address. </p>
<dt><code>-b </code><i>bind_address</i></p>
<dd> Use <i>bind_address</i> on the local machine as the source address of the connection. Only useful on systems with more than one address. </p>
<dt><code>-C</code></p>
<dd> Requests compression of all data (including stdin, stdout, stderr, and data for forwarded X11, TCP and UNIX connections). The compression algorithm is the same used by <a href="/docs/linux/man/1-gzip/">gzip</a>(1). Compression is desirable on modem lines and other slow connections, but will only slow down things on fast networks. The default value can be set on a host-by-host basis in the configuration files; see the <code>Compression</code> option. </p>
<dt><code>-c </code><i>cipher_spec</i></p>
<dd> Selects the cipher specification for encrypting the session. <i>cipher_spec</i> is a comma-separated list of ciphers listed in order of preference. See the <code>Ciphers</code> keyword in ssh_config5 for more information. </p>
<dt><code>-D </code> [<i>bind_address : </i>] <i>port</i></p>
<dd>
<dd>Specifies a local &#8220;dynamic&#8221; application-level port forwarding. This works by allocating a socket to listen to <i>port</i> on the local side, optionally bound to the specified <i>bind_address</i> Whenever a connection is made to this port, the connection is forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine. Currently the SOCKS4 and SOCKS5 protocols are supported, and <code>ssh</code> will act as a SOCKS server. Only root can forward privileged ports. Dynamic port forwardings can also be specified in the configuration file. </p>
<p> IPv6 addresses can be specified by enclosing the address in square brackets. Only the superuser can forward privileged ports. By default, the local port is bound in accordance with the <code>GatewayPorts</code> setting. However, an explicit <i>bind_address</i> may be used to bind the connection to a specific address. The <i>bind_address</i> of &#8220;localhost&#8221; indicates that the listening port be bound for local use only, while an empty address or `*&#8217; indicates that the port should be available from all interfaces. </p>
<dt><code>-E </code><i>log_file</i></p>
<dd> Append debug logs to <i>log_file</i> instead of standard error. </p>
<dt><code>-e </code><i>escape_char</i></p>
<dd> Sets the escape character for sessions with a pty (default: `~&#8217; ) . The escape character is only recognized at the beginning of a line. The escape character followed by a dot (`.&#8217; ) closes the connection; followed by control-Z suspends the connection; and followed by itself sends the escape character once. Setting the character to &#8220;none&#8221; disables any escapes and makes the session fully transparent. </p>
<dt><code>-F </code><i>configfile</i></p>
<dd> Specifies an alternative per-user configuration file. If a configuration file is given on the command line, the system-wide configuration file (/etc/ssh/ssh_config ) will be ignored. The default for the per-user configuration file is ~/.ssh/config If set to &#8220;none&#8221; no configuration files will be read. </p>
<dt><code>-f</code></p>
<dd> Requests <code>ssh</code> to go to background just before command execution. This is useful if <code>ssh</code> is going to ask for passwords or passphrases, but the user wants it in the background. This implies &#8211;<code>n</code> The recommended way to start X11 programs at a remote site is with something like <code>ssh -f host xterm</code> </p>
<p> If the <code>ExitOnForwardFailure</code> configuration option is set to &#8220;yes&#8221; then a client started with &#8211;<code>f</code> will wait for all remote port forwards to be successfully established before placing itself in the background. Refer to the description of <code>ForkAfterAuthentication</code> in ssh_config5 for details. </p>
<dt><code>-G</code></p>
<dd> Causes <code>ssh</code> to print its configuration after evaluating <code>Host</code> and <code>Match</code> blocks and exit. </p>
<dt><code>-g</code></p>
<dd> Allows remote hosts to connect to local forwarded ports. If used on a multiplexed connection, then this option must be specified on the master process. </p>
<dt><code>-I </code><i>pkcs11</i></p>
<dd> Specify the PKCS#11 shared library <code>ssh</code> should use to communicate with a PKCS#11 token providing keys for user authentication. </p>
<dt><code>-i </code><i>identity_file</i></p>
<dd> Selects a file from which the identity (private key) for public key authentication is read. You can also specify a public key file to use the corresponding private key that is loaded in ssh-agent1 when the private key file is not present locally. The default is ~/.ssh/id_rsa ~/.ssh/id_ecdsa ~/.ssh/id_ecdsa_sk ~/.ssh/id_ed25519 ~/.ssh/id_ed25519_sk and ~/.ssh/id_dsa Identity files may also be specified on a per-host basis in the configuration file. It is possible to have multiple &#8211;<code>i</code> options (and multiple identities specified in configuration files). If no certificates have been explicitly specified by the <code>CertificateFile</code> directive, <code>ssh</code> will also try to load certificate information from the filename obtained by appending -cert.pub to identity filenames. </p>
<dt><code>-J </code><i>destination</i></p>
<dd> Connect to the target host by first making a <code>ssh</code> connection to the jump host described by <i>destination</i> and then establishing a TCP forwarding to the ultimate destination from there. Multiple jump hops may be specified separated by comma characters. This is a shortcut to specify a <code>ProxyJump</code> configuration directive. Note that configuration directives supplied on the command-line generally apply to the destination host and not any specified jump hosts. Use ~/.ssh/config to specify configuration for jump hosts. </p>
<dt><code>-K</code></p>
<dd> Enables GSSAPI-based authentication and forwarding (delegation) of GSSAPI credentials to the server. </p>
<dt><code>-k</code></p>
<dd> Disables forwarding (delegation) of GSSAPI credentials to the server. </p>
<dt><code>-L </code> [<i>bind_address : </i>] <i>port : host : hostport</i></p>
<dd>
<dt><code>-L </code> [<i>bind_address : </i>] <i>port : remote_socket</i></p>
<dd>
<dt><code>-L </code> <i>local_socket : host : hostport</i></p>
<dd>
<dt><code>-L </code> <i>local_socket : remote_socket</i></p>
<dd>
<dd>Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side. This works by allocating a socket to listen to either a TCP <i>port</i> on the local side, optionally bound to the specified <i>bind_address</i> or to a Unix socket. Whenever a connection is made to the local port or socket, the connection is forwarded over the secure channel, and a connection is made to either <i>host</i> port <i>hostport</i> or the Unix socket <i>remote_socket</i> from the remote machine. </p>
<p> Port forwardings can also be specified in the configuration file. Only the superuser can forward privileged ports. IPv6 addresses can be specified by enclosing the address in square brackets. </p>
<p> By default, the local port is bound in accordance with the <code>GatewayPorts</code> setting. However, an explicit <i>bind_address</i> may be used to bind the connection to a specific address. The <i>bind_address</i> of &#8220;localhost&#8221; indicates that the listening port be bound for local use only, while an empty address or `*&#8217; indicates that the port should be available from all interfaces. </p>
<dt><code>-l </code><i>login_name</i></p>
<dd> Specifies the user to log in as on the remote machine. This also may be specified on a per-host basis in the configuration file. </p>
<dt><code>-M</code></p>
<dd> Places the <code>ssh</code> client into &#8220;master&#8221; mode for connection sharing. Multiple &#8211;<code>M</code> options places <code>ssh</code> into &#8220;master&#8221; mode but with confirmation required using ssh-askpass1 before each operation that changes the multiplexing state (e.g. opening a new session). Refer to the description of <code>ControlMaster</code> in ssh_config5 for details. </p>
<dt><code>-m </code><i>mac_spec</i></p>
<dd> A comma-separated list of MAC (message authentication code) algorithms, specified in order of preference. See the <code>MACs </code>keyword for more information. </p>
<dt><code>-N</code></p>
<dd> Do not execute a remote command. This is useful for just forwarding ports. Refer to the description of <code>SessionType</code> in ssh_config5 for details. </p>
<dt><code>-n</code></p>
<dd> Redirects stdin from /dev/null (actually, prevents reading from stdin). This must be used when <code>ssh</code> is run in the background. A common trick is to use this to run X11 programs on a remote machine. For example, <code>ssh -n shadows.cs.hut.fi emacs</code> will start an emacs on shadows.cs.hut.fi, and the X11 connection will be automatically forwarded over an encrypted channel. The <code>ssh</code> program will be put in the background. (This does not work if <code>ssh</code> needs to ask for a password or passphrase; see also the &#8211;<code>f</code> option.) Refer to the description of <code>StdinNull</code> in ssh_config5 for details. </p>
<dt><code>-O </code><i>ctl_cmd</i></p>
<dd> Control an active connection multiplexing master process. When the &#8211;<code>O</code> option is specified, the <i>ctl_cmd</i> argument is interpreted and passed to the master process. Valid commands are: &#8220;check&#8221; (check that the master process is running), &#8220;forward&#8221; (request forwardings without command execution), &#8220;cancel&#8221; (cancel forwardings), &#8220;exit&#8221; (request the master to exit), and &#8220;stop&#8221; (request the master to stop accepting further multiplexing requests). </p>
<dt><code>-o </code><i>option</i></p>
<dd> Can be used to give options in the format used in the configuration file. This is useful for specifying options for which there is no separate command-line flag. For full details of the options listed below, and their possible values, see ssh_config5. </p>
<dl>
<dt><code>AddKeysToAgent</code></p>
<dd>
<dt><code>AddressFamily</code></p>
<dd>
<dt><code>BatchMode</code></p>
<dd>
<dt><code>BindAddress</code></p>
<dd>
<dt><code>CanonicalDomains</code></p>
<dd>
<dt><code>CanonicalizeFallbackLocal</code></p>
<dd>
<dt><code>CanonicalizeHostname</code></p>
<dd>
<dt><code>CanonicalizeMaxDots</code></p>
<dd>
<dt><code>CanonicalizePermittedCNAMEs </code></p>
<dt><code>CASignatureAlgorithms</code></p>
<dd>
<dd>
<dt><code>CertificateFile</code></p>
<dd>
<dt><code>CheckHostIP</code></p>
<dd>
<dt><code>Ciphers</code></p>
<dd>
<dt><code>ClearAllForwardings</code></p>
<dd>
<dt><code>Compression</code></p>
<dd>
<dt><code>ConnectionAttempts</code></p>
<dd>
<dt><code>ConnectTimeout</code></p>
<dd>
<dt><code>ControlMaster</code></p>
<dd>
<dt><code>ControlPath</code></p>
<dd>
<dt><code>ControlPersist</code></p>
<dd>
<dt><code>DynamicForward</code></p>
<dd>
<dt><code>EscapeChar</code></p>
<dd>
<dt><code>ExitOnForwardFailure</code></p>
<dd>
<dt><code>FingerprintHash</code></p>
<dd>
<dt><code>ForkAfterAuthentication</code></p>
<dd>
<dt><code>ForwardAgent</code></p>
<dd>
<dt><code>ForwardX11</code></p>
<dd>
<dt><code>ForwardX11Timeout</code></p>
<dd>
<dt><code>ForwardX11Trusted</code></p>
<dd>
<dt><code>GatewayPorts</code></p>
<dd>
<dt><code>GlobalKnownHostsFile</code></p>
<dd>
<dt><code>GSSAPIAuthentication</code></p>
<dd>
<dt><code>GSSAPIKeyExchange</code></p>
<dd>
<dt><code>GSSAPIClientIdentity</code></p>
<dd>
<dt><code>GSSAPIDelegateCredentials</code></p>
<dd>
<dt><code>GSSAPIKexAlgorithms</code></p>
<dd>
<dt><code>GSSAPIRenewalForcesRekey</code></p>
<dd>
<dt><code>GSSAPIServerIdentity</code></p>
<dd>
<dt><code>GSSAPITrustDns</code></p>
<dd>
<dt><code>HashKnownHosts</code></p>
<dd>
<dt><code>Host</code></p>
<dd>
<dt><code>HostbasedAcceptedAlgorithms</code></p>
<dd>
<dt><code>HostbasedAuthentication</code></p>
<dd>
<dt><code>HostKeyAlgorithms</code></p>
<dd>
<dt><code>HostKeyAlias</code></p>
<dd>
<dt><code>Hostname</code></p>
<dd>
<dt><code>IdentitiesOnly</code></p>
<dd>
<dt><code>IdentityAgent</code></p>
<dd>
<dt><code>IdentityFile</code></p>
<dd>
<dt><code>IPQoS</code></p>
<dd>
<dt><code>KbdInteractiveAuthentication</code></p>
<dd>
<dt><code>KbdInteractiveDevices</code></p>
<dd>
<dt><code>KexAlgorithms</code></p>
<dd>
<dt><code>KnownHostsCommand</code></p>
<dd>
<dt><code>LocalCommand</code></p>
<dd>
<dt><code>LocalForward</code></p>
<dd>
<dt><code>LogLevel</code></p>
<dd>
<dt><code>MACs </code></p>
<dt><code>Match</code></p>
<dd>
<dd>
<dt><code>NoHostAuthenticationForLocalhost</code></p>
<dd>
<dt><code>NumberOfPasswordPrompts</code></p>
<dd>
<dt><code>PasswordAuthentication</code></p>
<dd>
<dt><code>PermitLocalCommand</code></p>
<dd>
<dt><code>PermitRemoteOpen</code></p>
<dd>
<dt><code>PKCS11Provider</code></p>
<dd>
<dt><code>Port</code></p>
<dd>
<dt><code>PreferredAuthentications</code></p>
<dd>
<dt><code>ProxyCommand</code></p>
<dd>
<dt><code>ProxyJump</code></p>
<dd>
<dt><code>ProxyUseFdpass</code></p>
<dd>
<dt><code>PubkeyAcceptedAlgorithms</code></p>
<dd>
<dt><code>PubkeyAuthentication</code></p>
<dd>
<dt><code>RekeyLimit</code></p>
<dd>
<dt><code>RemoteCommand</code></p>
<dd>
<dt><code>RemoteForward</code></p>
<dd>
<dt><code>RequestTTY</code></p>
<dd>
<dt><code>SendEnv</code></p>
<dd>
<dt><code>ServerAliveInterval</code></p>
<dd>
<dt><code>ServerAliveCountMax</code></p>
<dd>
<dt><code>SessionType</code></p>
<dd>
<dt><code>SetEnv</code></p>
<dd>
<dt><code>StdinNull</code></p>
<dd>
<dt><code>StreamLocalBindMask</code></p>
<dd>
<dt><code>StreamLocalBindUnlink</code></p>
<dd>
<dt><code>StrictHostKeyChecking</code></p>
<dd>
<dt><code>TCPKeepAlive</code></p>
<dd>
<dt><code>Tunnel</code></p>
<dd>
<dt><code>TunnelDevice</code></p>
<dd>
<dt><code>UpdateHostKeys</code></p>
<dd>
<dt><code>User</code></p>
<dd>
<dt><code>UserKnownHostsFile</code></p>
<dd>
<dt><code>VerifyHostKeyDNS</code></p>
<dd>
<dt><code>VisualHostKey</code></p>
<dd>
<dt><code>XAuthLocation</code></p>
<dd></dl>
<dt><code>-p </code><i>port</i></p>
<dd> Port to connect to on the remote host. This can be specified on a per-host basis in the configuration file. </p>
<dt><code>-Q </code><i>query_option</i></p>
<dd> Queries for the algorithms supported by one of the following features: <i>cipher</i> (supported symmetric ciphers), <i>cipher-auth</i> (supported symmetric ciphers that support authenticated encryption), <i>help</i> (supported query terms for use with the &#8211;<code>Q</code> flag), <i>mac</i> (supported message integrity codes), <i>kex</i> (key exchange algorithms), <i>kex-gss</i> (GSSAPI key exchange algorithms), <i>key</i> (key types), <i>key-cert</i> (certificate key types), <i>key-plain</i> (non-certificate key types), <i>key-sig</i> (all key types and signature algorithms), <i>protocol-version</i> (supported SSH protocol versions), and <i>sig</i> (supported signature algorithms). Alternatively, any keyword from ssh_config5 or sshd_config5 that takes an algorithm list may be used as an alias for the corresponding query_option. </p>
<dt><code>-q</code></p>
<dd> Quiet mode. Causes most warning and diagnostic messages to be suppressed. </p>
<dt><code>-R </code> [<i>bind_address : </i>] <i>port : host : hostport</i></p>
<dd>
<dt><code>-R </code> [<i>bind_address : </i>] <i>port : local_socket</i></p>
<dd>
<dt><code>-R </code> <i>remote_socket : host : hostport</i></p>
<dd>
<dt><code>-R </code> <i>remote_socket : local_socket</i></p>
<dd>
<dt><code>-R </code> [<i>bind_address : </i>] <i>port</i></p>
<dd>
<dd>Specifies that connections to the given TCP port or Unix socket on the remote (server) host are to be forwarded to the local side. </p>
<p> This works by allocating a socket to listen to either a TCP <i>port</i> or to a Unix socket on the remote side. Whenever a connection is made to this port or Unix socket, the connection is forwarded over the secure channel, and a connection is made from the local machine to either an explicit destination specified by <i>host</i> port <i>hostport</i> or <i>local_socket</i> or, if no explicit destination was specified, <code>ssh</code> will act as a SOCKS 4/5 proxy and forward connections to the destinations requested by the remote SOCKS client. </p>
<p> Port forwardings can also be specified in the configuration file. Privileged ports can be forwarded only when logging in as root on the remote machine. IPv6 addresses can be specified by enclosing the address in square brackets. </p>
<p> By default, TCP listening sockets on the server will be bound to the loopback interface only. This may be overridden by specifying a <i>bind_address</i> An empty <i>bind_address</i> or the address `*&#8217; , indicates that the remote socket should listen on all interfaces. Specifying a remote <i>bind_address</i> will only succeed if the server&#8217;s <code>GatewayPorts</code> option is enabled (see sshd_config5). </p>
<p> If the <i>port</i> argument is `0&#8242; , the listen port will be dynamically allocated on the server and reported to the client at run time. When used together with <code>-O forward</code> the allocated port will be printed to the standard output. </p>
<dt><code>-S </code><i>ctl_path</i></p>
<dd> Specifies the location of a control socket for connection sharing, or the string &#8220;none&#8221; to disable connection sharing. Refer to the description of <code>ControlPath</code> and <code>ControlMaster</code> in ssh_config5 for details. </p>
<dt><code>-s</code></p>
<dd> May be used to request invocation of a subsystem on the remote system. Subsystems facilitate the use of SSH as a secure transport for other applications (e.g. <a href="/docs/linux/man/1-sftp/">sftp</a>(1)). The subsystem is specified as the remote command. Refer to the description of <code>SessionType</code> in ssh_config5 for details. </p>
<dt><code>-T</code></p>
<dd> Disable pseudo-terminal allocation. </p>
<dt><code>-t</code></p>
<dd> Force pseudo-terminal allocation. This can be used to execute arbitrary screen-based programs on a remote machine, which can be very useful, e.g. when implementing menu services. Multiple &#8211;<code>t</code> options force tty allocation, even if <code>ssh</code> has no local tty. </p>
<dt><code>-V</code></p>
<dd> Display the version number and exit. </p>
<dt><code>-v</code></p>
<dd> Verbose mode. Causes <code>ssh</code> to print debugging messages about its progress. This is helpful in debugging connection, authentication, and configuration problems. Multiple &#8211;<code>v</code> options increase the verbosity. The maximum is 3. </p>
<dt><code>-W </code><i>host : </i><i>port</i></p>
<dd> Requests that standard input and output on the client be forwarded to <i>host</i> on <i>port</i> over the secure channel. Implies &#8211;<code>N</code> &#8211;<code>T</code> <code>ExitOnForwardFailure</code> and <code>ClearAllForwardings</code> though these can be overridden in the configuration file or using &#8211;<code>o</code> command line options. </p>
<dt><code>-w </code> <i>local_tun </i>[: <i>remote_tun</i> ]</p>
<dd>
<dd>Requests tunnel device forwarding with the specified <a href="/docs/linux/man/4-tun/">tun</a>(4) devices between the client (<i>local_tun</i> ) and the server (<i>remote_tun</i> ) </p>
<p> The devices may be specified by numerical ID or the keyword &#8220;any&#8221; which uses the next available tunnel device. If <i>remote_tun</i> is not specified, it defaults to &#8220;any&#8221; See also the <code>Tunnel</code> and <code>TunnelDevice</code> directives in ssh_config5. </p>
<p> If the <code>Tunnel</code> directive is unset, it will be set to the default tunnel mode, which is &#8220;point-to-point&#8221; If a different <code>Tunnel</code> forwarding mode it desired, then it should be specified before &#8211;<code>w</code> </p>
<dt><code>-X</code></p>
<dd> Enables X11 forwarding. This can also be specified on a per-host basis in a configuration file. </p>
<p> X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user&#8217;s X authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring. </p>
<p> For this reason, X11 forwarding is subjected to X11 SECURITY extension restrictions by default. Refer to the <code>ssh</code> &#8211;<code>Y</code> option and the <code>ForwardX11Trusted</code> directive in ssh_config5 for more information. </p>
<p> (Debian-specific: X11 forwarding is not subjected to X11 SECURITY extension restrictions by default, because too many programs currently crash in this mode. Set the <code>ForwardX11Trusted</code> option to &#8220;no&#8221; to restore the upstream behaviour. This may change in future depending on client-side improvements.) </p>
<dt><code>-x</code></p>
<dd> Disables X11 forwarding. </p>
<dt><code>-Y</code></p>
<dd> Enables trusted X11 forwarding. Trusted X11 forwardings are not subjected to the X11 SECURITY extension controls. </p>
<p> (Debian-specific: In the default configuration, this option is equivalent to &#8211;<code>X</code> since <code>ForwardX11Trusted</code> defaults to &#8220;yes&#8221; as described above. Set the <code>ForwardX11Trusted</code> option to &#8220;no&#8221; to restore the upstream behaviour. This may change in future depending on client-side improvements.) </p>
<dt><code>-y</code></p>
<dd> Send log information using the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) system module. By default this information is sent to stderr.</dl>
<p> <code>ssh</code> may additionally obtain configuration data from a per-user configuration file and a system-wide configuration file. The file format and configuration options are described in ssh_config5.</p>
<h2>AUTHENTICATION</h2>
<p> The OpenSSH SSH client supports SSH protocol 2. </p>
<p> The methods available for authentication are: GSSAPI-based authentication, host-based authentication, public key authentication, keyboard-interactive authentication, and password authentication. Authentication methods are tried in the order specified above, though <code>PreferredAuthentications</code> can be used to change the default order. </p>
<p> Host-based authentication works as follows: If the machine the user logs in from is listed in /etc/hosts.equiv or /etc/ssh/shosts.equiv on the remote machine, the user is non-root and the user names are the same on both sides, or if the files ~/.rhosts or ~/.shosts exist in the user&#8217;s home directory on the remote machine and contain a line containing the name of the client machine and the name of the user on that machine, the user is considered for login. Additionally, the server <i>must</i> be able to verify the client&#8217;s host key (see the description of /etc/ssh/ssh_known_hosts and ~/.ssh/known_hosts below) for login to be permitted. This authentication method closes security holes due to IP spoofing, DNS spoofing, and routing spoofing. [Note to the administrator: /etc/hosts.equiv ~/.rhosts and the rlogin/rsh protocol in general, are inherently insecure and should be disabled if security is desired.] </p>
<p> Public key authentication works as follows: The scheme is based on public-key cryptography, using cryptosystems where encryption and decryption are done using separate keys, and it is unfeasible to derive the decryption key from the encryption key. The idea is that each user creates a public/private key pair for authentication purposes. The server knows the public key, and only the user knows the private key. <code>ssh</code> implements public key authentication protocol automatically, using one of the DSA, ECDSA, Ed25519 or RSA algorithms. The HISTORY section of <a href="/docs/linux/man/8-ssl/">ssl</a>(8) (on non-OpenBSD systems, see <a rel="nofollow" href="http://www.openbsd.org/cgi-bin/man.cgi?query=ssl">http://www.openbsd.org/cgi-bin/man.cgi?query=ssl</a>&amp;sektion=8#HISTORY) contains a brief discussion of the DSA and RSA algorithms. </p>
<p> The file ~/.ssh/authorized_keys lists the public keys that are permitted for logging in. When the user logs in, the <code>ssh</code> program tells the server which key pair it would like to use for authentication. The client proves that it has access to the private key and the server checks that the corresponding public key is authorized to accept the account. </p>
<p> The server may inform the client of errors that prevented public key authentication from succeeding after authentication completes using a different method. These may be viewed by increasing the <code>LogLevel</code> to <code>DEBUG</code> or higher (e.g. by using the &#8211;<code>v</code> flag). </p>
<p> The user creates their key pair by running ssh-keygen1. This stores the private key in ~/.ssh/id_dsa (DSA), ~/.ssh/id_ecdsa (ECDSA), ~/.ssh/id_ecdsa_sk (authenticator-hosted ECDSA), ~/.ssh/id_ed25519 (Ed25519), ~/.ssh/id_ed25519_sk (authenticator-hosted Ed25519), or ~/.ssh/id_rsa (RSA) and stores the public key in ~/.ssh/id_dsa.pub (DSA), ~/.ssh/id_ecdsa.pub (ECDSA), ~/.ssh/id_ecdsa_sk.pub (authenticator-hosted ECDSA), ~/.ssh/id_ed25519.pub (Ed25519), ~/.ssh/id_ed25519_sk.pub (authenticator-hosted Ed25519), or ~/.ssh/id_rsa.pub (RSA) in the user&#8217;s home directory. The user should then copy the public key to ~/.ssh/authorized_keys in their home directory on the remote machine. The authorized_keys file corresponds to the conventional ~/.rhosts file, and has one key per line, though the lines can be very long. After this, the user can log in without giving the password. </p>
<p> A variation on public key authentication is available in the form of certificate authentication: instead of a set of public/private keys, signed certificates are used. This has the advantage that a single trusted certification authority can be used in place of many public/private keys. See the CERTIFICATES section of ssh-keygen1 for more information. </p>
<p> The most convenient way to use public key or certificate authentication may be with an authentication agent. See ssh-agent1 and (optionally) the <code>AddKeysToAgent</code> directive in ssh_config5 for more information. </p>
<p> Keyboard-interactive authentication works as follows: The server sends an arbitrary Qq challenge text and prompts for a response, possibly multiple times. Examples of keyboard-interactive authentication include BSD Authentication (see login.conf5) and PAM (some non- Ox systems). </p>
<p> Finally, if other authentication methods fail, <code>ssh</code> prompts the user for a password. The password is sent to the remote host for checking; however, since all communications are encrypted, the password cannot be seen by someone listening on the network. </p>
<p> <code>ssh</code> automatically maintains and checks a database containing identification for all hosts it has ever been used with. Host keys are stored in ~/.ssh/known_hosts in the user&#8217;s home directory. Additionally, the file /etc/ssh/ssh_known_hosts is automatically checked for known hosts. Any new hosts are automatically added to the user&#8217;s file. If a host&#8217;s identification ever changes, <code>ssh</code> warns about this and disables password authentication to prevent server spoofing or man-in-the-middle attacks, which could otherwise be used to circumvent the encryption. The <code>StrictHostKeyChecking</code> option can be used to control logins to machines whose host key is not known or has changed. </p>
<p> When the user&#8217;s identity has been accepted by the server, the server either executes the given command in a non-interactive session or, if no command has been specified, logs into the machine and gives the user a normal shell as an interactive session. All communication with the remote command or shell will be automatically encrypted. </p>
<p> If an interactive session is requested <code>ssh</code> by default will only request a pseudo-terminal (pty) for interactive sessions when the client has one. The flags &#8211;<code>T</code> and &#8211;<code>t</code> can be used to override this behaviour. </p>
<p> If a pseudo-terminal has been allocated the user may use the escape characters noted below. </p>
<p> If no pseudo-terminal has been allocated, the session is transparent and can be used to reliably transfer binary data. On most systems, setting the escape character to &#8220;none&#8221; will also make the session transparent even if a tty is used. </p>
<p> The session terminates when the command or shell on the remote machine exits and all X11 and TCP connections have been closed.</p>
<h2>ESCAPE CHARACTERS</h2>
<p> When a pseudo-terminal has been requested, <code>ssh</code> supports a number of functions through the use of an escape character. </p>
<p> A single tilde character can be sent as <code>~~</code> or by following the tilde by a character other than those described below. The escape character must always follow a newline to be interpreted as special. The escape character can be changed in configuration files using the <code>EscapeChar</code> configuration directive or on the command line by the &#8211;<code>e</code> option. </p>
<p> The supported escapes (assuming the default `~&#8217; ) are:</p>
<dl>
<dt><code>~.</code></p>
<dd> Disconnect.</p>
<dt><code>~^Z</code></p>
<dd> Background <code>ssh.</code></p>
<dt><code>~#</code></p>
<dd> List forwarded connections.</p>
<dt><code>~&amp;</code></p>
<dd> Background <code>ssh</code> at logout when waiting for forwarded connection / X11 sessions to terminate.</p>
<dt><code>~?</code></p>
<dd> Display a list of escape characters.</p>
<dt><code>~B</code></p>
<dd> Send a BREAK to the remote system (only useful if the peer supports it).</p>
<dt><code>~C</code></p>
<dd> Open command line. Currently this allows the addition of port forwardings using the &#8211;<code>L</code> &#8211;<code>R</code> and &#8211;<code>D</code> options (see above). It also allows the cancellation of existing port-forwardings with &#8211;<code>KL </code>[<i>bind_address : port</i> ] for local, &#8211;<code>KR </code>[<i>bind_address : port</i> ] for remote and &#8211;<code>KD </code>[<i>bind_address : port</i> ] for dynamic port-forwardings. <code>! </code><i>command</i> allows the user to execute a local command if the <code>PermitLocalCommand</code> option is enabled in ssh_config5. Basic help is available, using the &#8211;<code>h</code> option.</p>
<dt><code>~R</code></p>
<dd> Request rekeying of the connection (only useful if the peer supports it).</p>
<dt><code>~V</code></p>
<dd> Decrease the verbosity (<code>LogLevel</code> ) when errors are being written to stderr.</p>
<dt><code>~v</code></p>
<dd> Increase the verbosity (<code>LogLevel</code> ) when errors are being written to stderr.</dl>
<h2>TCP FORWARDING</h2>
<p> Forwarding of arbitrary TCP connections over a secure channel can be specified either on the command line or in a configuration file. One possible application of TCP forwarding is a secure connection to a mail server; another is going through firewalls. </p>
<p> In the example below, we look at encrypting communication for an IRC client, even though the IRC server it connects to does not directly support encrypted communication. This works as follows: the user connects to the remote host using <code>ssh,</code> specifying the ports to be used to forward the connection. After that it is possible to start the program locally, and <code>ssh</code> will encrypt and forward the connection to the remote server. </p>
<p> The following example tunnels an IRC session from the client to an IRC server at &#8220;server.example.com&#8221; joining channel &#8220;#users&#8221; nickname &#8220;pinky&#8221; using the standard IRC port, 6667: </p>
<pre>
$ ssh -f -L 6667:localhost:6667 server.example.com sleep 10
$ irc -c '#users' pinky IRC/127.0.0.1
</pre>
<p> The &#8211;<code>f</code> option backgrounds <code>ssh</code> and the remote command &#8220;sleep 10&#8221; is specified to allow an amount of time (10 seconds, in the example) to start the program which is going to use the tunnel. If no connections are made within the time specified, <code>ssh</code> will exit.</p>
<h2>X11 FORWARDING</h2>
<p> If the <code>ForwardX11</code> variable is set to &#8220;yes&#8221; (or see the description of the &#8211;<code>X</code> &#8211;<code>x</code> and &#8211;<code>Y</code> options above) and the user is using X11 (the <code>DISPLAY</code> environment variable is set), the connection to the X11 display is automatically forwarded to the remote side in such a way that any X11 programs started from the shell (or command) will go through the encrypted channel, and the connection to the real X server will be made from the local machine. The user should not manually set <code>DISPLAY</code> Forwarding of X11 connections can be configured on the command line or in configuration files. </p>
<p> The <code>DISPLAY</code> value set by <code>ssh</code> will point to the server machine, but with a display number greater than zero. This is normal, and happens because <code>ssh</code> creates a &#8220;proxy&#8221; X server on the server machine for forwarding the connections over the encrypted channel. </p>
<p> <code>ssh</code> will also automatically set up Xauthority data on the server machine. For this purpose, it will generate a random authorization cookie, store it in Xauthority on the server, and verify that any forwarded connections carry this cookie and replace it by the real cookie when the connection is opened. The real authentication cookie is never sent to the server machine (and no cookies are sent in the plain). </p>
<p> If the <code>ForwardAgent</code> variable is set to &#8220;yes&#8221; (or see the description of the &#8211;<code>A</code> and &#8211;<code>a</code> options above) and the user is using an authentication agent, the connection to the agent is automatically forwarded to the remote side.</p>
<h2>VERIFYING HOST KEYS</h2>
<p> When connecting to a server for the first time, a fingerprint of the server&#8217;s public key is presented to the user (unless the option <code>StrictHostKeyChecking</code> has been disabled). Fingerprints can be determined using ssh-keygen1: </p>
<blockquote><p><tt>$ ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key</tt></p></blockquote>
<p> If the fingerprint is already known, it can be matched and the key can be accepted or rejected. If only legacy (MD5) fingerprints for the server are available, the ssh-keygen1 &#8211;<code>E</code> option may be used to downgrade the fingerprint algorithm to match. </p>
<p> Because of the difficulty of comparing host keys just by looking at fingerprint strings, there is also support to compare host keys visually, using <i>random art</i> By setting the <code>VisualHostKey</code> option to &#8220;yes&#8221; a small ASCII graphic gets displayed on every login to a server, no matter if the session itself is interactive or not. By learning the pattern a known server produces, a user can easily find out that the host key has changed when a completely different pattern is displayed. Because these patterns are not unambiguous however, a pattern that looks similar to the pattern remembered only gives a good probability that the host key is the same, not guaranteed proof. </p>
<p> To get a listing of the fingerprints along with their random art for all known hosts, the following command line can be used: </p>
<blockquote><p><tt>$ ssh-keygen -lv -f ~/.ssh/known_hosts</tt></p></blockquote>
<p> If the fingerprint is unknown, an alternative method of verification is available: SSH fingerprints verified by DNS. An additional resource record (RR), SSHFP, is added to a zonefile and the connecting client is able to match the fingerprint with that of the key presented. </p>
<p> In this example, we are connecting a client to a server, &#8220;host.example.com&#8221; The SSHFP resource records should first be added to the zonefile for host.example.com: </p>
<blockquote>
<pre>
$ ssh-keygen -r host.example.com.
</pre>
</blockquote>
<p> The output lines will have to be added to the zonefile. To check that the zone is answering fingerprint queries: </p>
<blockquote><p><tt>$ dig -t SSHFP host.example.com</tt></p></blockquote>
<p> Finally the client connects: </p>
<blockquote>
<pre>
$ ssh -o &quot;VerifyHostKeyDNS ask&quot; host.example.com
[...]
Matching host key fingerprint found in DNS.
Are you sure you want to continue connecting (yes/no)?
</pre>
</blockquote>
<p> See the <code>VerifyHostKeyDNS</code> option in ssh_config5 for more information.</p>
<h2>SSH-BASED VIRTUAL PRIVATE NETWORKS</h2>
<p> <code>ssh</code> contains support for Virtual Private Network (VPN) tunnelling using the <a href="/docs/linux/man/4-tun/">tun</a>(4) network pseudo-device, allowing two networks to be joined securely. The sshd_config5 configuration option <code>PermitTunnel</code> controls whether the server supports this, and at what level (layer 2 or 3 traffic). </p>
<p> The following example would connect client network 10.0.50.0/24 with remote network 10.0.99.0/24 using a point-to-point connection from 10.1.1.1 to 10.1.1.2, provided that the SSH server running on the gateway to the remote network, at 192.168.1.15, allows it. </p>
<p> On the client: </p>
<blockquote>
<pre>
# ssh -f -w 0:1 192.168.1.15 true
# ifconfig tun0 10.1.1.1 10.1.1.2 netmask 255.255.255.252
# route add 10.0.99.0/24 10.1.1.2
</pre>
</blockquote>
<p> On the server: </p>
<blockquote>
<pre>
# ifconfig tun1 10.1.1.2 10.1.1.1 netmask 255.255.255.252
# route add 10.0.50.0/24 10.1.1.1
</pre>
</blockquote>
<p> Client access may be more finely tuned via the /root/.ssh/authorized_keys file (see below) and the <code>PermitRootLogin</code> server option. The following entry would permit connections on <a href="/docs/linux/man/4-tun/">tun</a>(4) device 1 from user &#8220;jane&#8221; and on tun device 2 from user &#8220;john&#8221; if <code>PermitRootLogin</code> is set to &#8220;forced-commands-only&#8221; </p>
<pre>
tunnel=&quot;1&quot;,command=&quot;sh /etc/netstart tun1&quot; ssh-rsa ... jane
tunnel=&quot;2&quot;,command=&quot;sh /etc/netstart tun2&quot; ssh-rsa ... john
</pre>
<p> Since an SSH-based setup entails a fair amount of overhead, it may be more suited to temporary setups, such as for wireless VPNs. More permanent VPNs are better provided by tools such as <a href="/docs/linux/man/8-ipsecctl/">ipsecctl</a>(8) and <a href="/docs/linux/man/8-isakmpd/">isakmpd</a>(8).</p>
<h2>ENVIRONMENT</h2>
<p> <code>ssh</code> will normally set the following environment variables:</p>
<dl>
<dt><code>DISPLAY</code></p>
<dd> The <code>DISPLAY</code> variable indicates the location of the X11 server. It is automatically set by <code>ssh</code> to point to a value of the form &#8220;hostname:n&#8221; where &#8220;hostname&#8221; indicates the host where the shell runs, and `n&#8217; is an integer &#038;gt=; 1. <code>ssh</code> uses this special value to forward X11 connections over the secure channel. The user should normally not set <code>DISPLAY</code> explicitly, as that will render the X11 connection insecure (and will require the user to manually copy any required authorization cookies).</p>
<dt><code>HOME</code></p>
<dd> Set to the path of the user&#8217;s home directory.</p>
<dt><code>LOGNAME</code></p>
<dd> Synonym for <code>USER</code> set for compatibility with systems that use this variable.</p>
<dt><code>MAIL</code></p>
<dd> Set to the path of the user&#8217;s mailbox.</p>
<dt><code>PATH</code></p>
<dd> Set to the default <code>PATH</code> as specified when compiling <code>ssh.</code></p>
<dt><code>SSH_ASKPASS</code></p>
<dd> If <code>ssh</code> needs a passphrase, it will read the passphrase from the current terminal if it was run from a terminal. If <code>ssh</code> does not have a terminal associated with it but <code>DISPLAY</code> and <code>SSH_ASKPASS</code> are set, it will execute the program specified by <code>SSH_ASKPASS</code> and open an X11 window to read the passphrase. This is particularly useful when calling <code>ssh</code> from a .xsession or related script. (Note that on some machines it may be necessary to redirect the input from /dev/null to make this work.)</p>
<dt><code>SSH_ASKPASS_REQUIRE</code></p>
<dd> Allows further control over the use of an askpass program. If this variable is set to &#8220;never&#8221; then <code>ssh</code> will never attempt to use one. If it is set to &#8220;prefer&#8221; then <code>ssh</code> will prefer to use the askpass program instead of the TTY when requesting passwords. Finally, if the variable is set to &#8220;force&#8221; then the askpass program will be used for all passphrase input regardless of whether <code>DISPLAY</code> is set.</p>
<dt><code>SSH_AUTH_SOCK</code></p>
<dd> Identifies the path of a UNIX socket used to communicate with the agent.</p>
<dt><code>SSH_CONNECTION</code></p>
<dd> Identifies the client and server ends of the connection. The variable contains four space-separated values: client IP address, client port number, server IP address, and server port number.</p>
<dt><code>SSH_ORIGINAL_COMMAND</code></p>
<dd> This variable contains the original command line if a forced command is executed. It can be used to extract the original arguments.</p>
<dt><code>SSH_TTY</code></p>
<dd> This is set to the name of the tty (path to the device) associated with the current shell or command. If the current session has no tty, this variable is not set.</p>
<dt><code>SSH_TUNNEL</code></p>
<dd> Optionally set by <a href="/docs/linux/man/8-sshd/">sshd</a>(8) to contain the interface names assigned if tunnel forwarding was requested by the client.</p>
<dt><code>SSH_USER_AUTH</code></p>
<dd> Optionally set by <a href="/docs/linux/man/8-sshd/">sshd</a>(8), this variable may contain a pathname to a file that lists the authentication methods successfully used when the session was established, including any public keys that were used.</p>
<dt><code>TZ</code></p>
<dd> This variable is set to indicate the present time zone if it was set when the daemon was started (i.e. the daemon passes the value on to new connections).</p>
<dt><code>USER</code></p>
<dd> Set to the name of the user logging in.</dl>
<p> Additionally, <code>ssh</code> reads ~/.ssh/environment and adds lines of the format &#8220;VARNAME=value&#8221; to the environment if the file exists and users are allowed to change their environment. For more information, see the <code>PermitUserEnvironment</code> option in sshd_config5.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.rhosts </code></p>
<dd> This file is used for host-based authentication (see above). On some machines this file may need to be world-readable if the user&#8217;s home directory is on an NFS partition, because <a href="/docs/linux/man/8-sshd/">sshd</a>(8) reads it as root. Additionally, this file must be owned by the user, and must not have write permissions for anyone else. The recommended permission for most machines is read/write for the user, and not accessible by others. </p>
<dt><code>~/.shosts </code></p>
<dd> This file is used in exactly the same way as .rhosts but allows host-based authentication without permitting login with rlogin/rsh. </p>
<dt><code>~/.ssh/ </code></p>
<dd> This directory is the default location for all user-specific configuration and authentication information. There is no general requirement to keep the entire contents of this directory secret, but the recommended permissions are read/write/execute for the user, and not accessible by others. </p>
<dt><code>~/.ssh/authorized_keys </code></p>
<dd> Lists the public keys (DSA, ECDSA, Ed25519, RSA) that can be used for logging in as this user. The format of this file is described in the <a href="/docs/linux/man/8-sshd/">sshd</a>(8) manual page. This file is not highly sensitive, but the recommended permissions are read/write for the user, and not accessible by others. </p>
<dt><code>~/.ssh/config </code></p>
<dd> This is the per-user configuration file. The file format and configuration options are described in ssh_config5. Because of the potential for abuse, this file must have strict permissions: read/write for the user, and not writable by others. It may be group-writable provided that the group in question contains only the user. </p>
<dt><code>~/.ssh/environment </code></p>
<dd> Contains additional definitions for environment variables; see Sx ENVIRONMENT , above. </p>
<dt><code>~/.ssh/id_dsa </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa_sk </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519 </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519_sk </code></p>
<dd>
<dt><code>~/.ssh/id_rsa </code></p>
<dd> Contains the private key for authentication. These files contain sensitive data and should be readable by the user but not accessible by others (read/write/execute). <code>ssh</code> will simply ignore a private key file if it is accessible by others. It is possible to specify a passphrase when generating the key which will be used to encrypt the sensitive part of this file using AES-128. </p>
<dt><code>~/.ssh/id_dsa.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ecdsa_sk.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519.pub </code></p>
<dd>
<dt><code>~/.ssh/id_ed25519_sk.pub </code></p>
<dd>
<dt><code>~/.ssh/id_rsa.pub </code></p>
<dd> Contains the public key for authentication. These files are not sensitive and can (but need not) be readable by anyone. </p>
<dt><code>~/.ssh/known_hosts </code></p>
<dd> Contains a list of host keys for all hosts the user has logged into that are not already in the systemwide list of known host keys. See <a href="/docs/linux/man/8-sshd/">sshd</a>(8) for further details of the format of this file. </p>
<dt><code>~/.ssh/rc </code></p>
<dd> Commands in this file are executed by <code>ssh</code> when the user logs in, just before the user&#8217;s shell (or command) is started. See the <a href="/docs/linux/man/8-sshd/">sshd</a>(8) manual page for more information. </p>
<dt><code>/etc/hosts.equiv </code></p>
<dd> This file is for host-based authentication (see above). It should only be writable by root. </p>
<dt><code>/etc/ssh/shosts.equiv </code></p>
<dd> This file is used in exactly the same way as hosts.equiv but allows host-based authentication without permitting login with rlogin/rsh. </p>
<dt><code>/etc/ssh/ssh_config </code></p>
<dd> Systemwide configuration file. The file format and configuration options are described in ssh_config5. </p>
<dt><code>/etc/ssh/ssh_host_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_dsa_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ecdsa_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ed25519_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_rsa_key </code></p>
<dd> These files contain the private parts of the host keys and are used for host-based authentication. </p>
<dt><code>/etc/ssh/ssh_known_hosts </code></p>
<dd> Systemwide list of known host keys. This file should be prepared by the system administrator to contain the public host keys of all machines in the organization. It should be world-readable. See <a href="/docs/linux/man/8-sshd/">sshd</a>(8) for further details of the format of this file. </p>
<dt><code>/etc/ssh/sshrc </code></p>
<dd> Commands in this file are executed by <code>ssh</code> when the user logs in, just before the user&#8217;s shell (or command) is started. See the <a href="/docs/linux/man/8-sshd/">sshd</a>(8) manual page for more information.</dl>
<h2>EXIT STATUS</h2>
<p> <code>ssh</code> exits with the exit status of the remote command or with 255 if an error occurred.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-scp/">scp</a>(1), <a href="/docs/linux/man/1-sftp/">sftp</a>(1), ssh-add1, ssh-agent1, ssh-argv01, ssh-keygen1, ssh-keyscan1, <a href="/docs/linux/man/4-tun/">tun</a>(4), ssh_config5, ssh-keysign8, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>STANDARDS</h2>
<dl>
<dt>
<dd> S. Lehtinen C. Lonvick January 2006 <i>RFC 4250</i> <i>The Secure Shell (SSH) Protocol Assigned Numbers</i></dl>
<dl>
<dt>
<dd> T. Ylonen C. Lonvick January 2006 <i>RFC 4251</i> <i>The Secure Shell (SSH) Protocol Architecture</i></dl>
<dl>
<dt>
<dd> T. Ylonen C. Lonvick January 2006 <i>RFC 4252</i> <i>The Secure Shell (SSH) Authentication Protocol</i></dl>
<dl>
<dt>
<dd> T. Ylonen C. Lonvick January 2006 <i>RFC 4253</i> <i>The Secure Shell (SSH) Transport Layer Protocol</i></dl>
<dl>
<dt>
<dd> T. Ylonen C. Lonvick January 2006 <i>RFC 4254</i> <i>The Secure Shell (SSH) Connection Protocol</i></dl>
<dl>
<dt>
<dd> J. Schlyter W. Griffin January 2006 <i>RFC 4255</i> <i>Using DNS to Securely Publish Secure Shell (SSH) Key Fingerprints</i></dl>
<dl>
<dt>
<dd> F. Cusack M. Forssen January 2006 <i>RFC 4256</i> <i>Generic Message Exchange Authentication for the Secure Shell Protocol (SSH)</i></dl>
<dl>
<dt>
<dd> J. Galbraith P. Remaker January 2006 <i>RFC 4335</i> <i>The Secure Shell (SSH) Session Channel Break Extension</i></dl>
<dl>
<dt>
<dd> M. Bellare T. Kohno C. Namprempre January 2006 <i>RFC 4344</i> <i>The Secure Shell (SSH) Transport Layer Encryption Modes</i></dl>
<dl>
<dt>
<dd> B. Harris January 2006 <i>RFC 4345</i> <i>Improved Arcfour Modes for the Secure Shell (SSH) Transport Layer Protocol</i></dl>
<dl>
<dt>
<dd> M. Friedl N. Provos W. Simpson March 2006 <i>RFC 4419</i> <i>Diffie-Hellman Group Exchange for the Secure Shell (SSH) Transport Layer Protocol</i></dl>
<dl>
<dt>
<dd> J. Galbraith R. Thayer November 2006 <i>RFC 4716</i> <i>The Secure Shell (SSH) Public Key File Format</i></dl>
<dl>
<dt>
<dd> D. Stebila J. Green December 2009 <i>RFC 5656</i> <i>Elliptic Curve Algorithm Integration in the Secure Shell Transport Layer</i></dl>
<dl>
<dt>
<dd> A. Perrig D. Song 1999 International Workshop on Cryptographic Techniques and E-Commerce (CrypTEC &#8217;99) <i>Hash Visualization: a New Technique to improve Real-World Security</i></dl>
<h2>AUTHORS</h2>
<p> OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. </p>
<h2>Index</h2>
