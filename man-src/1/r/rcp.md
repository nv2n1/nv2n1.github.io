---
title: "rcp(1)"
name: "rcp"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcp/"
description: "scp – OpenSSH secure file copy"
---

<h2 class="name">NAME</h2>
<p> <code>scp</code> &#8211; OpenSSH secure file copy </p>
<h2>SYNOPSIS</h2>
<p> <code>scp</code> [-<code>346ABCOpqRrsTv </code>[-<code>c </code><i>cipher</i> ] ] [-<code>D </code><i>sftp_server_path</i> ] [-<code>F </code><i>ssh_config</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>J </code><i>destination</i> ] [-<code>l </code><i>limit</i> ] [-<code>o </code><i>ssh_option</i> ] [-<code>P </code><i>port</i> ] [-<code>S </code><i>program</i> ] <i>source &#8230; target</i></p>
<h2>DESCRIPTION</h2>
<p> <code>scp</code> copies files between hosts on a network. </p>
<p> It uses <a href="/docs/linux/man/1-ssh/">ssh</a>(1) for data transfer, and uses the same authentication and provides the same security as a login session. </p>
<p> <code>scp</code> will ask for passwords or passphrases if they are needed for authentication. </p>
<p> The <i>source</i> and <i>target</i> may be specified as a local pathname, a remote host with optional path in the form [user @ host : [path] ] or a URI in the form <code>scp:// </code>[user @ host [: port [/ path] ] ] Local file names can be made explicit using absolute or relative pathnames to avoid <code>scp</code> treating file names containing `:&#8217; as host specifiers. </p>
<p> When copying between two remote hosts, if the URI format is used, a <i>port</i> cannot be specified on the <i>target</i> if the &#8211;<code>R</code> option is used. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-3</code></p>
<dd> Copies between two remote hosts are transferred through the local host. Without this option the data is copied directly between the two remote hosts. Note that, when using the original SCP protocol (the default), this option selects batch mode for the second host as <code>scp</code> cannot ask for passwords or passphrases for both hosts. This mode is the default.</p>
<dt><code>-4</code></p>
<dd> Forces <code>scp</code> to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd> Forces <code>scp</code> to use IPv6 addresses only.</p>
<dt><code>-A</code></p>
<dd> Allows forwarding of ssh-agent1 to the remote system. The default is not to forward an authentication agent.</p>
<dt><code>-B</code></p>
<dd> Selects batch mode (prevents asking for passwords or passphrases).</p>
<dt><code>-C</code></p>
<dd> Compression enable. Passes the &#8211;<code>C</code> flag to <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to enable compression.</p>
<dt><code>-c </code><i>cipher</i></p>
<dd> Selects the cipher to use for encrypting the data transfer. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-D </code><i>sftp_server_path</i></p>
<dd> When using the SFTP protocol support via &#8211;<code>s</code> connect directly to a local SFTP server program rather than a remote one via <a href="/docs/linux/man/1-ssh/">ssh</a>(1). This option may be useful in debugging the client and server.</p>
<dt><code>-F </code><i>ssh_config</i></p>
<dd> Specifies an alternative per-user configuration file for <code>ssh</code> This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-i </code><i>identity_file</i></p>
<dd> Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-J </code><i>destination</i></p>
<dd> Connect to the target host by first making an <code>scp</code> connection to the jump host described by <i>destination</i> and then establishing a TCP forwarding to the ultimate destination from there. Multiple jump hops may be specified separated by comma characters. This is a shortcut to specify a <code>ProxyJump</code> configuration directive. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-l </code><i>limit</i></p>
<dd> Limits the used bandwidth, specified in Kbit/s.</p>
<dt><code>-O</code></p>
<dd> Use the original SCP protocol for file transfers instead of the SFTP protocol. Forcing the use of the SCP protocol may be necessary for servers that do not implement SFTP, for backwards-compatibility for particular filename wildcard patterns and for expanding paths with a `~&#8217; prefix for older SFTP servers. This mode is the default.</p>
<dt><code>-o </code><i>ssh_option</i></p>
<dd> Can be used to pass options to <code>ssh</code> in the format used in ssh_config5. This is useful for specifying options for which there is no separate <code>scp</code> command-line flag. For full details of the options listed below, and their possible values, see ssh_config5. </p>
<dl>
<dt><code>AddressFamily</code></p>
<dd>
<dt><code>BatchMode</code></p>
<dd>
<dt><code>BindAddress</code></p>
<dd>
<dt><code>BindInterface</code></p>
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
<dt><code>GlobalKnownHostsFile</code></p>
<dd>
<dt><code>GSSAPIAuthentication</code></p>
<dd>
<dt><code>GSSAPIDelegateCredentials</code></p>
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
<dt><code>LogLevel</code></p>
<dd>
<dt><code>MACs </code></p>
<dt><code>NoHostAuthenticationForLocalhost</code></p>
<dd>
<dd>
<dt><code>NumberOfPasswordPrompts</code></p>
<dd>
<dt><code>PasswordAuthentication</code></p>
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
<dt><code>PubkeyAcceptedAlgorithms</code></p>
<dd>
<dt><code>PubkeyAuthentication</code></p>
<dd>
<dt><code>RekeyLimit</code></p>
<dd>
<dt><code>SendEnv</code></p>
<dd>
<dt><code>ServerAliveInterval</code></p>
<dd>
<dt><code>ServerAliveCountMax</code></p>
<dd>
<dt><code>SetEnv</code></p>
<dd>
<dt><code>StrictHostKeyChecking</code></p>
<dd>
<dt><code>TCPKeepAlive</code></p>
<dd>
<dt><code>UpdateHostKeys</code></p>
<dd>
<dt><code>User</code></p>
<dd>
<dt><code>UserKnownHostsFile</code></p>
<dd>
<dt><code>VerifyHostKeyDNS</code></p>
<dd></dl>
<dt><code>-P </code><i>port</i></p>
<dd> Specifies the port to connect to on the remote host. Note that this option is written with a capital `P&#8217; because &#8211;<code>p</code> is already reserved for preserving the times and mode bits of the file.</p>
<dt><code>-p</code></p>
<dd> Preserves modification times, access times, and file mode bits from the source file.</p>
<dt><code>-q</code></p>
<dd> Quiet mode: disables the progress meter as well as warning and diagnostic messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-R</code></p>
<dd> Copies between two remote hosts are performed by connecting to the origin host and executing <code>scp</code> there. This requires that <code>scp</code> running on the origin host can authenticate to the destination host without requiring a password.</p>
<dt><code>-r</code></p>
<dd> Recursively copy entire directories. Note that <code>scp</code> follows symbolic links encountered in the tree traversal.</p>
<dt><code>-S </code><i>program</i></p>
<dd> Name of <i>program</i> to use for the encrypted connection. The program must understand <a href="/docs/linux/man/1-ssh/">ssh</a>(1) options.</p>
<dt><code>-s</code></p>
<dd> Use the SFTP protocol for transfers rather than the original scp protocol.</p>
<dt><code>-T</code></p>
<dd> Disable strict filename checking. By default when copying files from a remote host to a local directory <code>scp</code> checks that the received filenames match those requested on the command-line to prevent the remote end from sending unexpected or unwanted files. Because of differences in how various operating systems and shells interpret filename wildcards, these checks may cause wanted files to be rejected. This option disables these checks at the expense of fully trusting that the server will not send unexpected filenames.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Causes <code>scp</code> and <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to print debugging messages about their progress. This is helpful in debugging connection, authentication, and configuration problems.</dl>
<h2>EXIT STATUS</h2>
<p> Ex -std scp</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sftp/">sftp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, ssh-keygen1, ssh_config5, sftp-server8, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>HISTORY</h2>
<p> <code>scp</code> is based on the rcp program in BSD source code from the Regents of the University of California.</p>
<h2>AUTHORS</h2>
<p> An Timo Rinne Aq Mt tri [at] iki.fi An Tatu Ylonen Aq Mt ylo [at] cs.hut.fi</p>
<h2>CAVEATS</h2>
<p> The original SCP protocol (used by default) requires execution of the remote user&#8217;s shell to perform <a href="/docs/linux/man/3-glob/">glob</a>(3) pattern matching. This requires careful quoting of any characters that have special meaning to the remote shell, such as quote characters. </p>
<h2>Index</h2>
