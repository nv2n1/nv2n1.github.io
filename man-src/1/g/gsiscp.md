---
title: "gsiscp(1)"
name: "gsiscp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsiscp/"
description: "scp – secure copy (remote file copy program)"
---

<h2>NAME</h2>
<p> <code>scp</code> &#8211; secure copy (remote file copy program)</p>
<h2>SYNOPSIS</h2>
<p> <code>scp</code> -words [-<code>12346BCpqrv</code> ] [-<code>c </code><i>cipher</i> ] [-<code>F </code><i>ssh_config</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>l </code><i>limit</i> ] [-<code>o </code><i>ssh_option</i> ] [-<code>P </code><i>port</i> ] [-<code>S </code><i>program</i> ] [[<i>user </i><code>@</code> ] <i>host1 </i><code>:</code> <i>file1</i> ] <i>&#8230;</i> [[<i>user </i><code>@</code> ] <i>host2 </i><code>:</code> <i>file2</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>scp</code> copies files between hosts on a network. It uses <a href="/docs/linux/man/1-ssh/">ssh</a>(1) for data transfer, and uses the same authentication and provides the same security as <a href="/docs/linux/man/1-ssh/">ssh</a>(1). Unlike <a href="/docs/linux/man/1-rcp/">rcp</a>(1), <code>scp</code> will ask for passwords or passphrases if they are needed for authentication. </p>
<p> File names may contain a user and host specification to indicate that the file is to be copied to/from that host. Local file names can be made explicit using absolute or relative pathnames to avoid <code>scp</code> treating file names containing `:&#8217; as host specifiers. Copies between two remote hosts are also permitted. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-1</code></p>
<dd> Forces <code>scp</code> to use protocol 1.</p>
<dt><code>-2</code></p>
<dd> Forces <code>scp</code> to use protocol 2.</p>
<dt><code>-3</code></p>
<dd> Copies between two remote hosts are transferred through the local host. Without this option the data is copied directly between the two remote hosts. Note that this option disables the progress meter.</p>
<dt><code>-4</code></p>
<dd> Forces <code>scp</code> to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd> Forces <code>scp</code> to use IPv6 addresses only.</p>
<dt><code>-B</code></p>
<dd> Selects batch mode (prevents asking for passwords or passphrases).</p>
<dt><code>-C</code></p>
<dd> Compression enable. Passes the &#8211;<code>C</code> flag to <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to enable compression.</p>
<dt><code>-c </code><i>cipher</i></p>
<dd> Selects the cipher to use for encrypting the data transfer. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-F </code><i>ssh_config</i></p>
<dd> Specifies an alternative per-user configuration file for <code>ssh</code> This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-i </code><i>identity_file</i></p>
<dd> Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-l </code><i>limit</i></p>
<dd> Limits the used bandwidth, specified in Kbit/s.</p>
<dt><code>-o </code><i>ssh_option</i></p>
<dd> Can be used to pass options to <code>ssh</code> in the format used in ssh_config5. This is useful for specifying options for which there is no separate <code>scp</code> command-line flag. For full details of the options listed below, and their possible values, see ssh_config5. </p>
<dl>
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
<dt><code>ChallengeResponseAuthentication</code></p>
<dd>
<dd>
<dt><code>CheckHostIP</code></p>
<dd>
<dt><code>Cipher</code></p>
<dd>
<dt><code>Ciphers</code></p>
<dd>
<dt><code>Compression</code></p>
<dd>
<dt><code>CompressionLevel</code></p>
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
<dt><code>HostbasedAuthentication</code></p>
<dd>
<dt><code>HostKeyAlgorithms</code></p>
<dd>
<dt><code>HostKeyAlias</code></p>
<dd>
<dt><code>HostName</code></p>
<dd>
<dt><code>IdentityFile</code></p>
<dd>
<dt><code>IdentitiesOnly</code></p>
<dd>
<dt><code>IPQoS</code></p>
<dd>
<dt><code>KbdInteractiveAuthentication</code></p>
<dd>
<dt><code>KbdInteractiveDevices</code></p>
<dd>
<dt><code>KexAlgorithms</code></p>
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
<dt><code>Protocol</code></p>
<dd>
<dt><code>ProxyCommand</code></p>
<dd>
<dt><code>PubkeyAuthentication</code></p>
<dd>
<dt><code>RekeyLimit</code></p>
<dd>
<dt><code>RhostsRSAAuthentication</code></p>
<dd>
<dt><code>RSAAuthentication</code></p>
<dd>
<dt><code>SendEnv</code></p>
<dd>
<dt><code>ServerAliveInterval</code></p>
<dd>
<dt><code>ServerAliveCountMax</code></p>
<dd>
<dt><code>StrictHostKeyChecking</code></p>
<dd>
<dt><code>TCPKeepAlive</code></p>
<dd>
<dt><code>UsePrivilegedPort</code></p>
<dd>
<dt><code>User</code></p>
<dd>
<dt><code>UserKnownHostsFile</code></p>
<dd>
<dt><code>VerifyHostKeyDNS</code></p>
<dd></dl>
<dt><code>-P </code><i>port</i></p>
<dd> Specifies the port to connect to on the remote host. Note that this option is written with a capital `P&#8217; because &#8211;<code>p</code> is already reserved for preserving the times and modes of the file in <a href="/docs/linux/man/1-rcp/">rcp</a>(1).</p>
<dt><code>-p</code></p>
<dd> Preserves modification times, access times, and modes from the original file.</p>
<dt><code>-q</code></p>
<dd> Quiet mode: disables the progress meter as well as warning and diagnostic messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-r</code></p>
<dd> Recursively copy entire directories. Note that <code>scp</code> follows symbolic links encountered in the tree traversal.</p>
<dt><code>-S </code><i>program</i></p>
<dd> Name of <i>program</i> to use for the encrypted connection. The program must understand <a href="/docs/linux/man/1-ssh/">ssh</a>(1) options.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Causes <code>scp</code> and <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to print debugging messages about their progress. This is helpful in debugging connection, authentication, and configuration problems.</dl>
<h2>EXIT STATUS</h2>
<p> Ex -std scp</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rcp/">rcp</a>(1), <a href="/docs/linux/man/1-sftp/">sftp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, ssh-keygen1, ssh_config5, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>HISTORY</h2>
<p> <code>scp</code> is based on the <a href="/docs/linux/man/1-rcp/">rcp</a>(1) program in BSD source code from the Regents of the University of California.</p>
<h2>AUTHORS</h2>
<p> An Timo Rinne Aq Mt tri [at] iki.fi An Tatu Ylonen Aq Mt ylo [at] cs.hut.fi </p>
<h2>Index</h2>
