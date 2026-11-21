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
<p> <code>scp</code> -words [-<code>12346BCpqrv</code> ] [-<code>c </code><i>cipher</i> ] [-<code>F </code><i>ssh_config</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>l </code><i>limit</i> ] [-<code>o </code><i>ssh_option</i> ] [-<code>P </code><i>port</i> ] [-<code>S </code><i>program</i> ] [[<i>user </i><code>@</code> ] <i>host1 </i><code>:</code> <i>file1</i> ] <i>&#8230;</i> [[<i>user </i><code>@</code> ] <i>host2 </i><code>:</code> <i>file2</i> ]</p>
<p> <code>scp</code> copies files between hosts on a network. It uses <a href="/docs/linux/man/1-ssh/">ssh</a>(1) for data transfer, and uses the same authentication and provides the same security as <a href="/docs/linux/man/1-ssh/">ssh</a>(1). Unlike <a href="/docs/linux/man/1-rcp/">rcp</a>(1), <code>scp</code> will ask for passwords or passphrases if they are needed for authentication. </p>
<p> File names may contain a user and host specification to indicate that the file is to be copied to/from that host. Local file names can be made explicit using absolute or relative pathnames to avoid <code>scp</code> treating file names containing `:&#8217; as host specifiers. Copies between two remote hosts are also permitted. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-1</code></dt>
<dd> Forces <code>scp</code> to use protocol 1.</dd>
<dt><code>-2</code></dt>
<dd> Forces <code>scp</code> to use protocol 2.</dd>
<dt><code>-3</code></dt>
<dd> Copies between two remote hosts are transferred through the local host. Without this option the data is copied directly between the two remote hosts. Note that this option disables the progress meter.</dd>
<dt><code>-4</code></dt>
<dd> Forces <code>scp</code> to use IPv4 addresses only.</dd>
<dt><code>-6</code></dt>
<dd> Forces <code>scp</code> to use IPv6 addresses only.</dd>
<dt><code>-B</code></dt>
<dd> Selects batch mode (prevents asking for passwords or passphrases).</dd>
<dt><code>-C</code></dt>
<dd> Compression enable. Passes the &#8211;<code>C</code> flag to <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to enable compression.</dd>
<dt><code>-c </code><i>cipher</i></dt>
<dd> Selects the cipher to use for encrypting the data transfer. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-F </code><i>ssh_config</i></dt>
<dd> Specifies an alternative per-user configuration file for <code>ssh</code> This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-i </code><i>identity_file</i></dt>
<dd> Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-l </code><i>limit</i></dt>
<dd> Limits the used bandwidth, specified in Kbit/s.</dd>
<dt><code>-o </code><i>ssh_option</i></dt>
<dd> Can be used to pass options to <code>ssh</code> in the format used in ssh_config5. This is useful for specifying options for which there is no separate <code>scp</code> command-line flag. For full details of the options listed below, and their possible values, see ssh_config5. </dd>
<dl>
<dt><code>AddressFamily</code></dt>
<dd>
</dd><dt><code>BatchMode</code></dt>
<dd>
</dd><dt><code>BindAddress</code></dt>
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
<dt><code>ChallengeResponseAuthentication</code></dt>
<dd>
</dd><dd>
</dd><dt><code>CheckHostIP</code></dt>
<dd>
</dd><dt><code>Cipher</code></dt>
<dd>
</dd><dt><code>Ciphers</code></dt>
<dd>
</dd><dt><code>Compression</code></dt>
<dd>
</dd><dt><code>CompressionLevel</code></dt>
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
</dd><dt><code>HostbasedAuthentication</code></dt>
<dd>
</dd><dt><code>HostKeyAlgorithms</code></dt>
<dd>
</dd><dt><code>HostKeyAlias</code></dt>
<dd>
</dd><dt><code>HostName</code></dt>
<dd>
</dd><dt><code>IdentityFile</code></dt>
<dd>
</dd><dt><code>IdentitiesOnly</code></dt>
<dd>
</dd><dt><code>IPQoS</code></dt>
<dd>
</dd><dt><code>KbdInteractiveAuthentication</code></dt>
<dd>
</dd><dt><code>KbdInteractiveDevices</code></dt>
<dd>
</dd><dt><code>KexAlgorithms</code></dt>
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
</dd><dt><code>Protocol</code></dt>
<dd>
</dd><dt><code>ProxyCommand</code></dt>
<dd>
</dd><dt><code>PubkeyAuthentication</code></dt>
<dd>
</dd><dt><code>RekeyLimit</code></dt>
<dd>
</dd><dt><code>RhostsRSAAuthentication</code></dt>
<dd>
</dd><dt><code>RSAAuthentication</code></dt>
<dd>
</dd><dt><code>SendEnv</code></dt>
<dd>
</dd><dt><code>ServerAliveInterval</code></dt>
<dd>
</dd><dt><code>ServerAliveCountMax</code></dt>
<dd>
</dd><dt><code>StrictHostKeyChecking</code></dt>
<dd>
</dd><dt><code>TCPKeepAlive</code></dt>
<dd>
</dd><dt><code>UsePrivilegedPort</code></dt>
<dd>
</dd><dt><code>User</code></dt>
<dd>
</dd><dt><code>UserKnownHostsFile</code></dt>
<dd>
</dd><dt><code>VerifyHostKeyDNS</code></dt>
<dd></dd></dl>
<dt><code>-P </code><i>port</i></dt>
<dd> Specifies the port to connect to on the remote host. Note that this option is written with a capital `P&#8217; because &#8211;<code>p</code> is already reserved for preserving the times and modes of the file in <a href="/docs/linux/man/1-rcp/">rcp</a>(1).</dd>
<dt><code>-p</code></dt>
<dd> Preserves modification times, access times, and modes from the original file.</dd>
<dt><code>-q</code></dt>
<dd> Quiet mode: disables the progress meter as well as warning and diagnostic messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-r</code></dt>
<dd> Recursively copy entire directories. Note that <code>scp</code> follows symbolic links encountered in the tree traversal.</dd>
<dt><code>-S </code><i>program</i></dt>
<dd> Name of <i>program</i> to use for the encrypted connection. The program must understand <a href="/docs/linux/man/1-ssh/">ssh</a>(1) options.</dd>
<dt><code>-v</code></dt>
<dd> Verbose mode. Causes <code>scp</code> and <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to print debugging messages about their progress. This is helpful in debugging connection, authentication, and configuration problems.</dd></dl>
<h2>EXIT STATUS</h2>
<p> Ex -std scp</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rcp/">rcp</a>(1), <a href="/docs/linux/man/1-sftp/">sftp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, ssh-keygen1, ssh_config5, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>HISTORY</h2>
<p> <code>scp</code> is based on the <a href="/docs/linux/man/1-rcp/">rcp</a>(1) program in BSD source code from the Regents of the University of California.</p>
<h2>AUTHORS</h2>
<p> An Timo Rinne Aq Mt tri [at] iki.fi An Tatu Ylonen Aq Mt ylo [at] cs.hut.fi </p>
