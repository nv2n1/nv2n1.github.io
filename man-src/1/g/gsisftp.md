---
title: "gsisftp(1)"
name: "gsisftp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsisftp/"
description: "sftp – secure file transfer program"
---

<h2>NAME</h2>
<p> <code>sftp</code> &#8211; secure file transfer program</p>
<h2>SYNOPSIS</h2>
<p> <code>sftp</code> -words [-<code>1246aCfpqrv</code> ] [-<code>B </code><i>buffer_size</i> ] [-<code>b </code><i>batchfile</i> ] [-<code>c </code><i>cipher</i> ] [-<code>D </code><i>sftp_server_path</i> ] [-<code>F </code><i>ssh_config</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>l </code><i>limit</i> ] [-<code>o </code><i>ssh_option</i> ] [-<code>P </code><i>port</i> ] [-<code>R </code><i>num_requests</i> ] [-<code>S </code><i>program</i> ] [-<code>s </code><i>subsystem | sftp_server</i> ] <i>host</i><br />
<code>sftp</code> [<i>user </i><code>@ </code><i>host </i>[: <i>file &#8230;</i> ] ]<br />
<code>sftp</code> [<i>user </i><code>@ </code><i>host </i>[: <i>dir </i>[<i>file &#8230;</i> ] ] ]<br />
<code>sftp</code> &#8211;<code>b </code><i>batchfile</i> [<i>user </i><code>@ </code><i>host</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>sftp</code> is an interactive file transfer program, similar to <a href="/docs/linux/man/1-ftp/">ftp</a>(1), which performs all operations over an encrypted <a href="/docs/linux/man/1-ssh/">ssh</a>(1) transport. It may also use many features of ssh, such as public key authentication and compression. <code>sftp</code> connects and logs into the specified <i>host</i> then enters an interactive command mode. </p>
<p> The second usage format will retrieve files automatically if a non-interactive authentication method is used; otherwise it will do so after successful interactive authentication. </p>
<p> The third usage format allows <code>sftp</code> to start in a remote directory. </p>
<p> The final usage format allows for automated sessions using the &#8211;<code>b</code> option. In such cases, it is necessary to configure non-interactive authentication to obviate the need to enter a password at connection time (see <a href="/docs/linux/man/8-sshd/">sshd</a>(8) and ssh-keygen1 for details). </p>
<p> Since some usage formats use colon characters to delimit host names from path names, IPv6 addresses must be enclosed in square brackets to avoid ambiguity. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-1</code></p>
<dd> Specify the use of protocol version 1.</p>
<dt><code>-2</code></p>
<dd> Specify the use of protocol version 2.</p>
<dt><code>-4</code></p>
<dd> Forces <code>sftp</code> to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd> Forces <code>sftp</code> to use IPv6 addresses only.</p>
<dt><code>-a</code></p>
<dd> Attempt to continue interrupted downloads rather than overwriting existing partial or complete copies of files. If the remote file contents differ from the partial local copy then the resultant file is likely to be corrupt.</p>
<dt><code>-B </code><i>buffer_size</i></p>
<dd> Specify the size of the buffer that <code>sftp</code> uses when transferring files. Larger buffers require fewer round trips at the cost of higher memory consumption. The default is 32768 bytes.</p>
<dt><code>-b </code><i>batchfile</i></p>
<dd> Batch mode reads a series of commands from an input <i>batchfile</i> instead of <i>stdin</i> Since it lacks user interaction it should be used in conjunction with non-interactive authentication. A <i>batchfile</i> of `-&#8216; may be used to indicate standard input. <code>sftp</code> will abort if any of the following commands fail: <code>get , put , reget , rename , ln</code> <code>rm , mkdir , chdir , ls</code> <code>lchdir , chmod , chown</code> <code>chgrp , lpwd , df , symlink</code> and <code>lmkdir</code> Termination on error can be suppressed on a command by command basis by prefixing the command with a `-&#8216; character (for example, <code>-rm /tmp/blah* )</code></p>
<dt><code>-C</code></p>
<dd> Enables compression (via ssh&#8217;s &#8211;<code>C</code> flag).</p>
<dt><code>-c </code><i>cipher</i></p>
<dd> Selects the cipher to use for encrypting the data transfers. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-D </code><i>sftp_server_path</i></p>
<dd> Connect directly to a local sftp server (rather than via <a href="/docs/linux/man/1-ssh/">ssh</a>(1)). This option may be useful in debugging the client and server.</p>
<dt><code>-F </code><i>ssh_config</i></p>
<dd> Specifies an alternative per-user configuration file for <a href="/docs/linux/man/1-ssh/">ssh</a>(1). This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-f</code></p>
<dd> Requests that files be flushed to disk immediately after transfer. When uploading files, this feature is only enabled if the server implements the &quot;fsync [at] openssh.com&quot; extension.</p>
<dt><code>-i </code><i>identity_file</i></p>
<dd> Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-l </code><i>limit</i></p>
<dd> Limits the used bandwidth, specified in Kbit/s.</p>
<dt><code>-o </code><i>ssh_option</i></p>
<dd> Can be used to pass options to <code>ssh</code> in the format used in ssh_config5. This is useful for specifying options for which there is no separate <code>sftp</code> command-line flag. For example, to specify an alternate port use: <code>sftp -oPort=24</code> For full details of the options listed below, and their possible values, see ssh_config5. </p>
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
<dd> Specifies the port to connect to on the remote host.</p>
<dt><code>-p</code></p>
<dd> Preserves modification times, access times, and modes from the original files transferred.</p>
<dt><code>-q</code></p>
<dd> Quiet mode: disables the progress meter as well as warning and diagnostic messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<dt><code>-R </code><i>num_requests</i></p>
<dd> Specify how many requests may be outstanding at any one time. Increasing this may slightly improve file transfer speed but will increase memory usage. The default is 64 outstanding requests.</p>
<dt><code>-r</code></p>
<dd> Recursively copy entire directories when uploading and downloading. Note that <code>sftp</code> does not follow symbolic links encountered in the tree traversal.</p>
<dt><code>-S </code><i>program</i></p>
<dd> Name of the <i>program</i> to use for the encrypted connection. The program must understand <a href="/docs/linux/man/1-ssh/">ssh</a>(1) options.</p>
<dt><code>-s </code><i>subsystem | sftp_server</i></p>
<dd> Specifies the SSH2 subsystem or the path for an sftp server on the remote host. A path is useful for using <code>sftp</code> over protocol version 1, or when the remote <a href="/docs/linux/man/8-sshd/">sshd</a>(8) does not have an sftp subsystem configured.</p>
<dt><code>-v</code></p>
<dd> Raise logging level. This option is also passed to ssh.</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> Once in interactive mode, <code>sftp</code> understands a set of commands similar to those of <a href="/docs/linux/man/1-ftp/">ftp</a>(1). Commands are case insensitive. Pathnames that contain spaces must be enclosed in quotes. Any special characters contained within pathnames that are recognized by <a href="/docs/linux/man/3-glob/">glob</a>(3) must be escaped with backslashes (`\&#8217; )</p>
<dl>
<dt><code>bye</code></p>
<dd> Quit <code>sftp</code></p>
<dt><code>cd </code><i>path</i></p>
<dd> Change remote directory to <i>path</i></p>
<dt><code>chgrp </code><i>grp path</i></p>
<dd> Change group of file <i>path</i> to <i>grp</i> <i>path</i> may contain <a href="/docs/linux/man/3-glob/">glob</a>(3) characters and may match multiple files. <i>grp</i> must be a numeric GID.</p>
<dt><code>chmod </code><i>mode path</i></p>
<dd> Change permissions of file <i>path</i> to <i>mode</i> <i>path</i> may contain <a href="/docs/linux/man/3-glob/">glob</a>(3) characters and may match multiple files.</p>
<dt><code>chown </code><i>own path</i></p>
<dd> Change owner of file <i>path</i> to <i>own</i> <i>path</i> may contain <a href="/docs/linux/man/3-glob/">glob</a>(3) characters and may match multiple files. <i>own</i> must be a numeric UID.</p>
<dt><code> df</code> [-<code>hi</code> ] [<i>path</i> ]</p>
<dd>
<dd>Display usage information for the filesystem holding the current directory (or <i>path</i> if specified). If the &#8211;<code>h</code> flag is specified, the capacity information will be displayed using &quot;human-readable&quot; suffixes. The &#8211;<code>i</code> flag requests display of inode information in addition to capacity information. This command is only supported on servers that implement the &#8220;statvfs [at] openssh.com&#8221; extension.</p>
<dt><code>exit</code></p>
<dd> Quit <code>sftp</code></p>
<dt><code> get</code> [-<code>afPpr</code> ] <i>remote-path</i> [<i>local-path</i> ]</p>
<dd>
<dd>Retrieve the <i>remote-path</i> and store it on the local machine. If the local path name is not specified, it is given the same name it has on the remote machine. <i>remote-path</i> may contain <a href="/docs/linux/man/3-glob/">glob</a>(3) characters and may match multiple files. If it does and <i>local-path</i> is specified, then <i>local-path</i> must specify a directory. </p>
<p> If the &#8211;<code>a</code> flag is specified, then attempt to resume partial transfers of existing files. Note that resumption assumes that any partial copy of the local file matches the remote copy. If the remote file contents differ from the partial local copy then the resultant file is likely to be corrupt. </p>
<p> If the &#8211;<code>f</code> flag is specified, then <a href="/docs/linux/man/2-fsync/">fsync</a>(2) will be called after the file transfer has completed to flush the file to disk. </p>
<p> If either the &#8211;<code>P</code> or &#8211;<code>p</code> flag is specified, then full file permissions and access times are copied too. </p>
<p> If the &#8211;<code>r</code> flag is specified then directories will be copied recursively. Note that <code>sftp</code> does not follow symbolic links when performing recursive transfers.</p>
<dt><code>help</code></p>
<dd> Display help text.</p>
<dt><code>lcd </code><i>path</i></p>
<dd> Change local directory to <i>path</i></p>
<dt><code>lls </code>[<i>ls-options </i>[<i>path</i> ] ]</p>
<dd> Display local directory listing of either <i>path</i> or current directory if <i>path</i> is not specified. <i>ls-options</i> may contain any flags supported by the local system&#8217;s <a href="/docs/linux/man/1-ls/">ls</a>(1) command. <i>path</i> may contain <a href="/docs/linux/man/3-glob/">glob</a>(3) characters and may match multiple files.</p>
<dt><code>lmkdir </code><i>path</i></p>
<dd> Create local directory specified by <i>path</i></p>
<dt><code> ln</code> [-<code>s</code> ] <i>oldpath</i> <i>newpath</i></p>
<dd>
<dd>Create a link from <i>oldpath</i> to <i>newpath</i> If the &#8211;<code>s</code> flag is specified the created link is a symbolic link, otherwise it is a hard link.</p>
<dt><code>lpwd</code></p>
<dd> Print local working directory.</p>
<dt><code> ls</code> [-<code>1afhlnrSt </code>[<i>path</i> ] ]</p>
<dd>
<dd>Display a remote directory listing of either <i>path</i> or the current directory if <i>path</i> is not specified. <i>path</i> may contain <a href="/docs/linux/man/3-glob/">glob</a>(3) characters and may match multiple files. </p>
<p> The following flags are recognized and alter the behaviour of <code>ls</code> accordingly:</p>
<dl>
<dt><code>-1</code></p>
<dd> Produce single columnar output.</p>
<dt><code>-a</code></p>
<dd> List files beginning with a dot (`.&#8217; )</p>
<dt><code>-f</code></p>
<dd> Do not sort the listing. The default sort order is lexicographical.</p>
<dt><code>-h</code></p>
<dd> When used with a long format option, use unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte, Petabyte, and Exabyte in order to reduce the number of digits to four or fewer using powers of 2 for sizes (K=1024, M=1048576, etc.).</p>
<dt><code>-l</code></p>
<dd> Display additional details including permissions and ownership information.</p>
<dt><code>-n</code></p>
<dd> Produce a long listing with user and group information presented numerically.</p>
<dt><code>-r</code></p>
<dd> Reverse the sort order of the listing.</p>
<dt><code>-S</code></p>
<dd> Sort the listing by file size.</p>
<dt><code>-t</code></p>
<dd> Sort the listing by last modification time.</dl>
<dt><code>lumask </code><i>umask</i></p>
<dd> Set local umask to <i>umask</i></p>
<dt><code>mkdir </code><i>path</i></p>
<dd> Create remote directory specified by <i>path</i></p>
<dt><code>progress</code></p>
<dd> Toggle display of progress meter.</p>
<dt><code> put</code> [-<code>fPpr</code> ] <i>local-path</i> [<i>remote-path</i> ]</p>
<dd>
<dd>Upload <i>local-path</i> and store it on the remote machine. If the remote path name is not specified, it is given the same name it has on the local machine. <i>local-path</i> may contain <a href="/docs/linux/man/3-glob/">glob</a>(3) characters and may match multiple files. If it does and <i>remote-path</i> is specified, then <i>remote-path</i> must specify a directory. </p>
<p> If the &#8211;<code>f</code> flag is specified, then a request will be sent to the server to call <a href="/docs/linux/man/2-fsync/">fsync</a>(2) after the file has been transferred. Note that this is only supported by servers that implement the &quot;fsync [at] openssh.com&quot; extension. </p>
<p> If either the &#8211;<code>P</code> or &#8211;<code>p</code> flag is specified, then full file permissions and access times are copied too. </p>
<p> If the &#8211;<code>r</code> flag is specified then directories will be copied recursively. Note that <code>sftp</code> does not follow symbolic links when performing recursive transfers.</p>
<dt><code>pwd</code></p>
<dd> Display remote working directory.</p>
<dt><code>quit</code></p>
<dd> Quit <code>sftp</code></p>
<dt><code> reget</code> [-<code>Ppr</code> ] <i>remote-path</i> [<i>local-path</i> ]</p>
<dd>
<dd>Resume download of <i>remote-path</i> Equivalent to <code>get</code> with the &#8211;<code>a</code> flag set.</p>
<dt><code>rename </code><i>oldpath newpath</i></p>
<dd> Rename remote file from <i>oldpath</i> to <i>newpath</i></p>
<dt><code>rm </code><i>path</i></p>
<dd> Delete remote file specified by <i>path</i></p>
<dt><code>rmdir </code><i>path</i></p>
<dd> Remove remote directory specified by <i>path</i></p>
<dt><code>symlink </code><i>oldpath newpath</i></p>
<dd> Create a symbolic link from <i>oldpath</i> to <i>newpath</i></p>
<dt><code>version</code></p>
<dd> Display the <code>sftp</code> protocol version.</p>
<dt><code>! </code><i>command</i></p>
<dd> Execute <i>command</i> in local shell.</p>
<dt><code>!</code></p>
<dd> Escape to local shell.</p>
<dt><code>?</code></p>
<dd> Synonym for help.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ftp/">ftp</a>(1), <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/1-scp/">scp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-keygen1, <a href="/docs/linux/man/3-glob/">glob</a>(3), ssh_config5, sftp-server8, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<dl>
<dt>
<dd> T. Ylonen S. Lehtinen <i>&quot;SSH File Transfer Protocol&quot;</i> draft-ietf-secsh-filexfer-00.txt January 2001 work in progress material</dl>
<h2>Index</h2>
