---

title: "sftp(1)"
name: "sftp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sftp/"
description: "sftp – OpenSSH secure file transfer"
---

<p> <code>sftp</code> &#8211; OpenSSH secure file transfer </p>
<h2>SYNOPSIS</h2>
<p> <code>sftp</code> [-<code>46AaCfNpqrv</code> ] [-<code>B </code><i>buffer_size</i> ] [-<code>b </code><i>batchfile</i> ] [-<code>c </code><i>cipher</i> ] [-<code>D </code><i>sftp_server_path</i> ] [-<code>F </code><i>ssh_config</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>J </code><i>destination</i> ] [-<code>l </code><i>limit</i> ] [-<code>o </code><i>ssh_option</i> ] [-<code>P </code><i>port</i> ] [-<code>R </code><i>num_requests</i> ] [-<code>S </code><i>program</i> ] [-<code>s </code><i>subsystem | sftp_server</i> ] <i>destination</i></p>
<h2>DESCRIPTION</h2>
<p> <code>sftp</code> is a file transfer program, similar to <a href="/docs/linux/man/1-ftp/">ftp</a>(1), which performs all operations over an encrypted <a href="/docs/linux/man/1-ssh/">ssh</a>(1) transport. It may also use many features of ssh, such as public key authentication and compression. </p>
<p> The <i>destination</i> may be specified either as [user @ host [: path] ] or as a URI in the form <code>sftp:// </code>[user @ host [: port [/ path] ] ] </p>
<p> If the <i>destination</i> includes a <i>path</i> and it is not a directory, <code>sftp</code> will retrieve files automatically if a non-interactive authentication method is used; otherwise it will do so after successful interactive authentication. </p>
<p> If no <i>path</i> is specified, or if the <i>path</i> is a directory, <code>sftp</code> will log in to the specified <i>host</i> and enter interactive command mode, changing to the remote directory if one was specified. An optional trailing slash can be used to force the <i>path</i> to be interpreted as a directory. </p>
<p> Since the destination formats use colon characters to delimit host names from path names or port numbers, IPv6 addresses must be enclosed in square brackets to avoid ambiguity. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-4</code></dt>
<dd> Forces <code>sftp</code> to use IPv4 addresses only.</dd>
<dt><code>-6</code></dt>
<dd> Forces <code>sftp</code> to use IPv6 addresses only.</dd>
<dt><code>-A</code></dt>
<dd> Allows forwarding of ssh-agent1 to the remote system. The default is not to forward an authentication agent.</dd>
<dt><code>-a</code></dt>
<dd> Attempt to continue interrupted transfers rather than overwriting existing partial or complete copies of files. If the partial contents differ from those being transferred, then the resultant file is likely to be corrupt.</dd>
<dt><code>-B </code><i>buffer_size</i></dt>
<dd> Specify the size of the buffer that <code>sftp</code> uses when transferring files. Larger buffers require fewer round trips at the cost of higher memory consumption. The default is 32768 bytes.</dd>
<dt><code>-b </code><i>batchfile</i></dt>
<dd> Batch mode reads a series of commands from an input <i>batchfile</i> instead of <i>stdin</i> Since it lacks user interaction it should be used in conjunction with non-interactive authentication to obviate the need to enter a password at connection time (see <a href="/docs/linux/man/8-sshd/">sshd</a>(8) and ssh-keygen1 for details). </dd>
<p> A <i>batchfile</i> of `-&#8216; may be used to indicate standard input. <code>sftp</code> will abort if any of the following commands fail: <code>get , put , reget , reput , rename , ln</code> <code>rm , mkdir , chdir , ls</code> <code>lchdir , chmod , chown</code> <code>chgrp , lpwd , df , symlink</code> and <code>lmkdir</code> </p>
<p> Termination on error can be suppressed on a command by command basis by prefixing the command with a `-&#8216; character (for example, <code>-rm /tmp/blah* )</code> Echo of the command may be suppressed by prefixing the command with a `@&#8217; character. These two prefixes may be combined in any order, for example <code>-@ls /bsd</code></p>
<dt><code>-C</code></dt>
<dd> Enables compression (via ssh&#8217;s &#8211;<code>C</code> flag).</dd>
<dt><code>-c </code><i>cipher</i></dt>
<dd> Selects the cipher to use for encrypting the data transfers. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-D </code><i>sftp_server_path</i></dt>
<dd> Connect directly to a local sftp server (rather than via <a href="/docs/linux/man/1-ssh/">ssh</a>(1)). This option may be useful in debugging the client and server.</dd>
<dt><code>-F </code><i>ssh_config</i></dt>
<dd> Specifies an alternative per-user configuration file for <a href="/docs/linux/man/1-ssh/">ssh</a>(1). This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-f</code></dt>
<dd> Requests that files be flushed to disk immediately after transfer. When uploading files, this feature is only enabled if the server implements the &quot;fsync [at] openssh.com&quot; extension.</dd>
<dt><code>-i </code><i>identity_file</i></dt>
<dd> Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-J </code><i>destination</i></dt>
<dd> Connect to the target host by first making an <code>sftp</code> connection to the jump host described by <i>destination</i> and then establishing a TCP forwarding to the ultimate destination from there. Multiple jump hops may be specified separated by comma characters. This is a shortcut to specify a <code>ProxyJump</code> configuration directive. This option is directly passed to <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-l </code><i>limit</i></dt>
<dd> Limits the used bandwidth, specified in Kbit/s.</dd>
<dt><code>-N</code></dt>
<dd> Disables quiet mode, e.g. to override the implicit quiet mode set by the &#8211;<code>b</code> flag.</dd>
<dt><code>-o </code><i>ssh_option</i></dt>
<dd> Can be used to pass options to <code>ssh</code> in the format used in ssh_config5. This is useful for specifying options for which there is no separate <code>sftp</code> command-line flag. For example, to specify an alternate port use: <code>sftp -oPort=24</code> For full details of the options listed below, and their possible values, see ssh_config5. </dd>
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
<dd> Specifies the port to connect to on the remote host.</dd>
<dt><code>-p</code></dt>
<dd> Preserves modification times, access times, and modes from the original files transferred.</dd>
<dt><code>-q</code></dt>
<dd> Quiet mode: disables the progress meter as well as warning and diagnostic messages from <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</dd>
<dt><code>-R </code><i>num_requests</i></dt>
<dd> Specify how many requests may be outstanding at any one time. Increasing this may slightly improve file transfer speed but will increase memory usage. The default is 64 outstanding requests.</dd>
<dt><code>-r</code></dt>
<dd> Recursively copy entire directories when uploading and downloading. Note that <code>sftp</code> does not follow symbolic links encountered in the tree traversal.</dd>
<dt><code>-S </code><i>program</i></dt>
<dd> Name of the <i>program</i> to use for the encrypted connection. The program must understand <a href="/docs/linux/man/1-ssh/">ssh</a>(1) options.</dd>
<dt><code>-s </code><i>subsystem | sftp_server</i></dt>
<dd> Specifies the SSH2 subsystem or the path for an sftp server on the remote host. A path is useful when the remote <a href="/docs/linux/man/8-sshd/">sshd</a>(8) does not have an sftp subsystem configured.</dd>
<dt><code>-v</code></dt>
<dd> Raise logging level. This option is also passed to ssh.</dd></dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> Once in interactive mode, <code>sftp</code> understands a set of commands similar to those of <a href="/docs/linux/man/1-ftp/">ftp</a>(1). Commands are case insensitive. Pathnames that contain spaces must be enclosed in quotes. Any special characters contained within pathnames that are recognized by <a href="/docs/linux/man/3-glob/">glob</a>(3) must be escaped with backslashes (`\&#8217; )</p>
<dl>
<dt><code>bye</code></dt>
<dd> Quit <code>sftp</code></dd>
<dt><code>cd </code>[<i>path</i> ]</dt>
<dd> Change remote directory to <i>path</i> If <i>path</i> is not specified, then change directory to the one the session started in.</dd>
<dt><code> chgrp</code> [-<code>h</code> ] <i>grp</i> <i>path</i></dt>
<dd>
</dd><dd>Change group of file <i>path</i> to <i>grp</i> <i>path</i> may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) characters and may match multiple files. <i>grp</i> must be a numeric GID. </dd>
<p> If the &#8211;<code>h</code> flag is specified, then symlinks will not be followed. Note that this is only supported by servers that implement the &quot;lsetstat [at] openssh.com&quot; extension.</p>
<dt><code> chmod</code> [-<code>h</code> ] <i>mode</i> <i>path</i></dt>
<dd>
</dd><dd>Change permissions of file <i>path</i> to <i>mode</i> <i>path</i> may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) characters and may match multiple files. </dd>
<p> If the &#8211;<code>h</code> flag is specified, then symlinks will not be followed. Note that this is only supported by servers that implement the &quot;lsetstat [at] openssh.com&quot; extension.</p>
<dt><code> chown</code> [-<code>h</code> ] <i>own</i> <i>path</i></dt>
<dd>
</dd><dd>Change owner of file <i>path</i> to <i>own</i> <i>path</i> may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) characters and may match multiple files. <i>own</i> must be a numeric UID. </dd>
<p> If the &#8211;<code>h</code> flag is specified, then symlinks will not be followed. Note that this is only supported by servers that implement the &quot;lsetstat [at] openssh.com&quot; extension.</p>
<dt><code> df</code> [-<code>hi</code> ] [<i>path</i> ]</dt>
<dd>
</dd><dd>Display usage information for the filesystem holding the current directory (or <i>path</i> if specified). If the &#8211;<code>h</code> flag is specified, the capacity information will be displayed using &quot;human-readable&quot; suffixes. The &#8211;<code>i</code> flag requests display of inode information in addition to capacity information. This command is only supported on servers that implement the &#8220;statvfs [at] openssh.com&#8221; extension.</dd>
<dt><code>exit</code></dt>
<dd> Quit <code>sftp</code></dd>
<dt><code> get</code> [-<code>afpR</code> ] <i>remote-path</i> [<i>local-path</i> ]</dt>
<dd>
</dd><dd>Retrieve the <i>remote-path</i> and store it on the local machine. If the local path name is not specified, it is given the same name it has on the remote machine. <i>remote-path</i> may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) characters and may match multiple files. If it does and <i>local-path</i> is specified, then <i>local-path</i> must specify a directory. </dd>
<p> If the &#8211;<code>a</code> flag is specified, then attempt to resume partial transfers of existing files. Note that resumption assumes that any partial copy of the local file matches the remote copy. If the remote file contents differ from the partial local copy then the resultant file is likely to be corrupt. </p>
<p> If the &#8211;<code>f</code> flag is specified, then <a href="/docs/linux/man/2-fsync/">fsync</a>(2) will be called after the file transfer has completed to flush the file to disk. </p>
<p> If the &#8211;<code>p</code> flag is specified, then full file permissions and access times are copied too. </p>
<p> If the &#8211;<code>R</code> flag is specified then directories will be copied recursively. Note that <code>sftp</code> does not follow symbolic links when performing recursive transfers.</p>
<dt><code>help</code></dt>
<dd> Display help text.</dd>
<dt><code>lcd </code>[<i>path</i> ]</dt>
<dd> Change local directory to <i>path</i> If <i>path</i> is not specified, then change directory to the local user&#8217;s home directory.</dd>
<dt><code>lls </code>[<i>ls-options </i>[<i>path</i> ] ]</dt>
<dd> Display local directory listing of either <i>path</i> or current directory if <i>path</i> is not specified. <i>ls-options</i> may contain any flags supported by the local system&#8217;s <a href="/docs/linux/man/1-ls/">ls</a>(1) command. <i>path</i> may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) characters and may match multiple files.</dd>
<dt><code>lmkdir </code><i>path</i></dt>
<dd> Create local directory specified by <i>path</i></dd>
<dt><code> ln</code> [-<code>s</code> ] <i>oldpath</i> <i>newpath</i></dt>
<dd>
</dd><dd>Create a link from <i>oldpath</i> to <i>newpath</i> If the &#8211;<code>s</code> flag is specified the created link is a symbolic link, otherwise it is a hard link.</dd>
<dt><code>lpwd</code></dt>
<dd> Print local working directory.</dd>
<dt><code> ls</code> [-<code>1afhlnrSt </code>[<i>path</i> ] ]</dt>
<dd>
</dd><dd>Display a remote directory listing of either <i>path</i> or the current directory if <i>path</i> is not specified. <i>path</i> may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) characters and may match multiple files. </dd>
<p> The following flags are recognized and alter the behaviour of <code>ls</code> accordingly:</p>
<dl>
<dt><code>-1</code></dt>
<dd> Produce single columnar output.</dd>
<dt><code>-a</code></dt>
<dd> List files beginning with a dot (`.&#8217; )</dd>
<dt><code>-f</code></dt>
<dd> Do not sort the listing. The default sort order is lexicographical.</dd>
<dt><code>-h</code></dt>
<dd> When used with a long format option, use unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte, Petabyte, and Exabyte in order to reduce the number of digits to four or fewer using powers of 2 for sizes (K=1024, M=1048576, etc.).</dd>
<dt><code>-l</code></dt>
<dd> Display additional details including permissions and ownership information.</dd>
<dt><code>-n</code></dt>
<dd> Produce a long listing with user and group information presented numerically.</dd>
<dt><code>-r</code></dt>
<dd> Reverse the sort order of the listing.</dd>
<dt><code>-S</code></dt>
<dd> Sort the listing by file size.</dd>
<dt><code>-t</code></dt>
<dd> Sort the listing by last modification time.</dd></dl>
<dt><code>lumask </code><i>umask</i></dt>
<dd> Set local umask to <i>umask</i></dd>
<dt><code>mkdir </code><i>path</i></dt>
<dd> Create remote directory specified by <i>path</i></dd>
<dt><code>progress</code></dt>
<dd> Toggle display of progress meter.</dd>
<dt><code> put</code> [-<code>afpR</code> ] <i>local-path</i> [<i>remote-path</i> ]</dt>
<dd>
</dd><dd>Upload <i>local-path</i> and store it on the remote machine. If the remote path name is not specified, it is given the same name it has on the local machine. <i>local-path</i> may contain <a href="/docs/linux/man/7-glob/">glob</a>(7) characters and may match multiple files. If it does and <i>remote-path</i> is specified, then <i>remote-path</i> must specify a directory. </dd>
<p> If the &#8211;<code>a</code> flag is specified, then attempt to resume partial transfers of existing files. Note that resumption assumes that any partial copy of the remote file matches the local copy. If the local file contents differ from the remote local copy then the resultant file is likely to be corrupt. </p>
<p> If the &#8211;<code>f</code> flag is specified, then a request will be sent to the server to call <a href="/docs/linux/man/2-fsync/">fsync</a>(2) after the file has been transferred. Note that this is only supported by servers that implement the &quot;fsync [at] openssh.com&quot; extension. </p>
<p> If the &#8211;<code>p</code> flag is specified, then full file permissions and access times are copied too. </p>
<p> If the &#8211;<code>R</code> flag is specified then directories will be copied recursively. Note that <code>sftp</code> does not follow symbolic links when performing recursive transfers.</p>
<dt><code>pwd</code></dt>
<dd> Display remote working directory.</dd>
<dt><code>quit</code></dt>
<dd> Quit <code>sftp</code></dd>
<dt><code> reget</code> [-<code>fpR</code> ] <i>remote-path</i> [<i>local-path</i> ]</dt>
<dd>
</dd><dd>Resume download of <i>remote-path</i> Equivalent to <code>get</code> with the &#8211;<code>a</code> flag set.</dd>
<dt><code> reput</code> [-<code>fpR</code> ] <i>local-path</i> [<i>remote-path</i> ]</dt>
<dd>
</dd><dd>Resume upload of <i>local-path</i> Equivalent to <code>put</code> with the &#8211;<code>a</code> flag set.</dd>
<dt><code>rename </code><i>oldpath newpath</i></dt>
<dd> Rename remote file from <i>oldpath</i> to <i>newpath</i></dd>
<dt><code>rm </code><i>path</i></dt>
<dd> Delete remote file specified by <i>path</i></dd>
<dt><code>rmdir </code><i>path</i></dt>
<dd> Remove remote directory specified by <i>path</i></dd>
<dt><code>symlink </code><i>oldpath newpath</i></dt>
<dd> Create a symbolic link from <i>oldpath</i> to <i>newpath</i></dd>
<dt><code>version</code></dt>
<dd> Display the <code>sftp</code> protocol version.</dd>
<dt><code>! </code><i>command</i></dt>
<dd> Execute <i>command</i> in local shell.</dd>
<dt><code>!</code></dt>
<dd> Escape to local shell.</dd>
<dt><code>?</code></dt>
<dd> Synonym for help.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ftp/">ftp</a>(1), <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/1-scp/">scp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-keygen1, ssh_config5, <a href="/docs/linux/man/7-glob/">glob</a>(7), sftp-server8, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<dl>
<dt>
</dt><dd> T. Ylonen S. Lehtinen <i>&quot;SSH File Transfer Protocol&quot;</i> draft-ietf-secsh-filexfer-00.txt January 2001 work in progress material</dd></dl>
