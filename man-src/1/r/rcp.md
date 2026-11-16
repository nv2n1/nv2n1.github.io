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
<dt><code>-3</code></dt>
<dd> Copies between two remote hosts are transferred through the local host. Without this option the data is copied directly between the two remote hosts. Note that, when using the original SCP protocol (the default), this option selects batch mode for the second host as <code>scp</code> cannot ask for passwords or passphrases for both hosts. This mode is the default.</dd>
<dt><code>-4</code></dt>
<dd> Forces <code>scp</code> to use IPv4 addresses only.</dd>
<dt><code>-6</code></dt>
<dd> Forces <code>scp</code> to use IPv6 addresses only.</dd>
<dt><code>-A</code></dt>
<dd> Allows forwarding of ssh-agent1 to the remote system. The default is not to forward an authentication agent.</dd>
<dt><code>-B</code></dt>
<dd> Selects batch mode (prevents asking for passwords or passphrases).</dd>
<dt><code>-C</code></dt>
<dd> Compression enable. Passes the &#8211;<code>C</code> flag to <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to enable compression.</dd>
<dt><code>-c </code><i>cipher</i></dt>
<dd> Selects the cipher to use for encrypting the data transfer. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-D </code><i>sftp_server_path</i></dt>
<dd> When using the SFTP protocol support via &#8211;<code>s</code> connect directly to a local SFTP server program rather than a remote one via <a href="/docs/linux/man/1-ssh/">ssh</a>(1). This option may be useful in debugging the client and server.</dd>
<dt><code>-F </code><i>ssh_config</i></dt>
<dd> Specifies an alternative per-user configuration file for <code>ssh</code> This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-i </code><i>identity_file</i></dt>
<dd> Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-J </code><i>destination</i></dt>
<dd> Connect to the target host by first making an <code>scp</code> connection to the jump host described by <i>destination</i> and then establishing a TCP forwarding to the ultimate destination from there. Multiple jump hops may be specified separated by comma characters. This is a shortcut to specify a <code>ProxyJump</code> configuration directive. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-l </code><i>limit</i></dt>
<dd> Limits the used bandwidth, specified in Kbit/s.</dd>
<dt><code>-O</code></dt>
<dd> Use the original SCP protocol for file transfers instead of the SFTP protocol. Forcing the use of the SCP protocol may be necessary for servers that do not implement SFTP, for backwards-compatibility for particular filename wildcard patterns and for expanding paths with a `~&#8217; prefix for older SFTP servers. This mode is the default.</dd>
<dt><code>-o </code><i>ssh_option</i></dt>
<dd> Can be used to pass options to <code>ssh</code> in the format used in ssh_config5. This is useful for specifying options for which there is no separate <code>scp</code> command-line flag. For full details of the options listed below, and their possible values, see ssh_config5. </dd>
<dl>
<dt><code>AddressFamily</code></dt>
<dd>
</dd><dt><code>BatchMode</code></dt>
<dd>
</dd><dt><code>BindAddress</code></dt>
<dd>
</dd><dt><code>BindInterface</code></dt>
<dd>
</dd><dt><code>CanonicalDomains</code></dt>
<dd>
</dd><dt><code>CanonicalizeFallbackLocal</code></dt>
<dd>
</dd><dt><code>CanonicalizeHostname</code></dt>
<dd>
</dd><dt><code>CanonicalizeMaxDots</code></dt>
<dd>
</dd><dt><code>CanonicalizePermittedCNAMEs </code></dt>
<dt><code>CASignatureAlgorithms</code></dt>
<dd>
</dd><dd>
</dd><dt><code>CertificateFile</code></dt>
<dd>
</dd><dt><code>CheckHostIP</code></dt>
<dd>
</dd><dt><code>Ciphers</code></dt>
<dd>
</dd><dt><code>Compression</code></dt>
<dd>
</dd><dt><code>ConnectionAttempts</code></dt>
<dd>
</dd><dt><code>ConnectTimeout</code></dt>
<dd>
</dd><dt><code>ControlMaster</code></dt>
<dd>
</dd><dt><code>ControlPath</code></dt>
<dd>
</dd><dt><code>ControlPersist</code></dt>
<dd>
</dd><dt><code>GlobalKnownHostsFile</code></dt>
<dd>
</dd><dt><code>GSSAPIAuthentication</code></dt>
<dd>
</dd><dt><code>GSSAPIDelegateCredentials</code></dt>
<dd>
</dd><dt><code>HashKnownHosts</code></dt>
<dd>
</dd><dt><code>Host</code></dt>
<dd>
</dd><dt><code>HostbasedAcceptedAlgorithms</code></dt>
<dd>
</dd><dt><code>HostbasedAuthentication</code></dt>
<dd>
</dd><dt><code>HostKeyAlgorithms</code></dt>
<dd>
</dd><dt><code>HostKeyAlias</code></dt>
<dd>
</dd><dt><code>Hostname</code></dt>
<dd>
</dd><dt><code>IdentitiesOnly</code></dt>
<dd>
</dd><dt><code>IdentityAgent</code></dt>
<dd>
</dd><dt><code>IdentityFile</code></dt>
<dd>
</dd><dt><code>IPQoS</code></dt>
<dd>
</dd><dt><code>KbdInteractiveAuthentication</code></dt>
<dd>
</dd><dt><code>KbdInteractiveDevices</code></dt>
<dd>
</dd><dt><code>KexAlgorithms</code></dt>
<dd>
</dd><dt><code>KnownHostsCommand</code></dt>
<dd>
</dd><dt><code>LogLevel</code></dt>
<dd>
</dd><dt><code>MACs </code></dt>
<dt><code>NoHostAuthenticationForLocalhost</code></dt>
<dd>
</dd><dd>
</dd><dt><code>NumberOfPasswordPrompts</code></dt>
<dd>
</dd><dt><code>PasswordAuthentication</code></dt>
<dd>
</dd><dt><code>PKCS11Provider</code></dt>
<dd>
</dd><dt><code>Port</code></dt>
<dd>
</dd><dt><code>PreferredAuthentications</code></dt>
<dd>
</dd><dt><code>ProxyCommand</code></dt>
<dd>
</dd><dt><code>ProxyJump</code></dt>
<dd>
</dd><dt><code>PubkeyAcceptedAlgorithms</code></dt>
<dd>
</dd><dt><code>PubkeyAuthentication</code></dt>
<dd>
</dd><dt><code>RekeyLimit</code></dt>
<dd>
</dd><dt><code>SendEnv</code></dt>
<dd>
</dd><dt><code>ServerAliveInterval</code></dt>
<dd>
</dd><dt><code>ServerAliveCountMax</code></dt>
<dd>
</dd><dt><code>SetEnv</code></dt>
<dd>
</dd><dt><code>StrictHostKeyChecking</code></dt>
<dd>
</dd><dt><code>TCPKeepAlive</code></dt>
<dd>
</dd><dt><code>UpdateHostKeys</code></dt>
<dd>
</dd><dt><code>User</code></dt>
<dd>
</dd><dt><code>UserKnownHostsFile</code></dt>
<dd>
</dd><dt><code>VerifyHostKeyDNS</code></dt>
<dd></dd></dl>
<dt><code>-P </code><i>port</i></dt>
<dd> Specifies the port to connect to on the remote host. Note that this option is written with a capital `P&#8217; because &#8211;<code>p</code> is already reserved for preserving the times and mode bits of the file.</dd>
<dt><code>-p</code></dt>
<dd> Preserves modification times, access times, and file mode bits from the source file.</dd>
<dt><code>-q</code></dt>
<dd> Quiet mode: disables the progress meter as well as warning and diagnostic messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-R</code></dt>
<dd> Copies between two remote hosts are performed by connecting to the origin host and executing <code>scp</code> there. This requires that <code>scp</code> running on the origin host can authenticate to the destination host without requiring a password.</dd>
<dt><code>-r</code></dt>
<dd> Recursively copy entire directories. Note that <code>scp</code> follows symbolic links encountered in the tree traversal.</dd>
<dt><code>-S </code><i>program</i></dt>
<dd> Name of <i>program</i> to use for the encrypted connection. The program must understand <a href="/docs/linux/man/1-ssh/">ssh</a>(1) options.</dd>
<dt><code>-s</code></dt>
<dd> Use the SFTP protocol for transfers rather than the original scp protocol.</dd>
<dt><code>-T</code></dt>
<dd> Disable strict filename checking. By default when copying files from a remote host to a local directory <code>scp</code> checks that the received filenames match those requested on the command-line to prevent the remote end from sending unexpected or unwanted files. Because of differences in how various operating systems and shells interpret filename wildcards, these checks may cause wanted files to be rejected. This option disables these checks at the expense of fully trusting that the server will not send unexpected filenames.</dd>
<dt><code>-v</code></dt>
<dd> Verbose mode. Causes <code>scp</code> and <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to print debugging messages about their progress. This is helpful in debugging connection, authentication, and configuration problems.</dd></dl>
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
