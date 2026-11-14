---
title: "gsisshd(8)"
name: "gsisshd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gsisshd/"
description: "sshd – OpenSSH SSH daemon"
---

<p><code>sshd</code> &#8211; OpenSSH SSH daemon</p>
<h2>Synopsis</h2>
<p><code>sshd</code> -words [-<code>46DdeiqTt </code>[-<code>b </code><i>bits</i> ] ] [-<code>C </code><i>connection_spec</i> ] [-<code>c </code><i>host_certificate_file</i> ] [-<code>E </code><i>log_file</i> ] [-<code>f </code><i>config_file</i> ] [-<code>g </code><i>login_grace_time</i> ] [-<code>h </code><i>host_key_file</i> ] [-<code>k </code><i>key_gen_time</i> ] [-<code>o </code><i>option</i> ] [-<code>p </code><i>port</i> ] [-<code>u </code><i>len</i> ]</p>
<h2>Description</h2>
<p><code>sshd</code> (OpenSSH Daemon) is the daemon program for <a href="/docs/linux/man/1-ssh/">ssh</a>(1). Together these programs replace <a href="/docs/linux/man/1-rlogin/">rlogin</a>(1) and <a href="/docs/linux/man/1-rsh/">rsh</a>(1), and provide secure encrypted communications between two untrusted hosts over an insecure network. <code>sshd</code> listens for connections from clients. It is normally started at boot from /etc/rc It forks a new daemon for each incoming connection. The forked daemons handle key exchange, encryption, authentication, command execution, and data exchange. <code>sshd</code> can be configured using command-line options or a configuration file (by default sshd_config5); command-line options override values specified in the configuration file. <code>sshd</code> rereads its configuration file when it receives a hangup signal, <code>SIGHUP</code> by executing itself with the name and options it was started with, e.g. /usr/sbin/sshd The options are as follows:</p>
<dl>
<dt><code>-4</code></p>
<dd>Forces <code>sshd</code> to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd>Forces <code>sshd</code> to use IPv6 addresses only.</p>
<dt><code>-b </code><i>bits</i></p>
<dd>Specifies the number of bits in the ephemeral protocol version 1 server key (default 1024).</p>
<dt><code>-C </code><i>connection_spec</i></p>
<dd>Specify the connection parameters to use for the &#8211;<code>T</code> extended test mode. If provided, any <code>Match</code> directives in the configuration file that would apply to the specified user, host, and address will be set before the configuration is written to standard output. The connection parameters are supplied as keyword=value pairs. The keywords are &#8220;user&#8221; &#8220;host&#8221; &#8220;laddr&#8221; &#8220;lport&#8221; and &#8220;addr&#8221; All are required and may be supplied in any order, either with multiple &#8211;<code>C</code> options or as a comma-separated list.</p>
<dt><code>-c </code><i>host_certificate_file</i></p>
<dd>Specifies a path to a certificate file to identify <code>sshd</code> during key exchange. The certificate file must match a host key file specified using the &#8211;<code>h</code> option or the <code>HostKey</code> configuration directive.</p>
<dt><code>-D</code></p>
<dd>When this option is specified, <code>sshd</code> will not detach and does not become a daemon. This allows easy monitoring of <code>sshd</code></p>
<dt><code>-d</code></p>
<dd>Debug mode. The server sends verbose debug output to standard error, and does not put itself in the background. The server also will not fork and will only process one connection. This option is only intended for debugging for the server. Multiple &#8211;<code>d</code> options increase the debugging level. Maximum is 3.</p>
<dt><code>-E </code><i>log_file</i></p>
<dd>Append debug logs to <i>log_file</i> instead of the system log.</p>
<dt><code>-e</code></p>
<dd>Write debug logs to standard error instead of the system log.</p>
<dt><code>-f </code><i>config_file</i></p>
<dd>Specifies the name of the configuration file. The default is /etc/gsissh/sshd_config <code>sshd</code> refuses to start if there is no configuration file.</p>
<dt><code>-g </code><i>login_grace_time</i></p>
<dd>Gives the grace time for clients to authenticate themselves (default 120 seconds). If the client fails to authenticate the user within this many seconds, the server disconnects and exits. A value of zero indicates no limit.</p>
<dt><code>-h </code><i>host_key_file</i></p>
<dd>Specifies a file from which a host key is read. This option must be given if <code>sshd</code> is not run as root (as the normal host key files are normally not readable by anyone but root). The default is /etc/gsissh/ssh_host_key for protocol version 1, and /etc/gsissh/ssh_host_dsa_key /etc/gsissh/ssh_host_ecdsa_key /etc/gsissh/ssh_host_ed25519_key and /etc/gsissh/ssh_host_rsa_key for protocol version 2. It is possible to have multiple host key files for the different protocol versions and host key algorithms.</p>
<dt><code>-i</code></p>
<dd>Specifies that <code>sshd</code> is being run from <a href="/docs/linux/man/8-inetd/">inetd</a>(8). <code>sshd</code> is normally not run from inetd because it needs to generate the server key before it can respond to the client, and this may take tens of seconds. Clients would have to wait too long if the key was regenerated every time. However, with small key sizes (e.g. 512) using <code>sshd</code> from inetd may be feasible.</p>
<dt><code>-k </code><i>key_gen_time</i></p>
<dd>Specifies how often the ephemeral protocol version 1 server key is regenerated (default 3600 seconds, or one hour). The motivation for regenerating the key fairly often is that the key is not stored anywhere, and after about an hour it becomes impossible to recover the key for decrypting intercepted communications even if the machine is cracked into or physically seized. A value of zero indicates that the key will never be regenerated.</p>
<dt><code>-o </code><i>option</i></p>
<dd>Can be used to give options in the format used in the configuration file. This is useful for specifying options for which there is no separate command-line flag. For full details of the options, and their values, see sshd_config5.</p>
<dt><code>-p </code><i>port</i></p>
<dd>Specifies the port on which the server listens for connections (default 22). Multiple port options are permitted. Ports specified in the configuration file with the <code>Port</code> option are ignored when a command-line port is specified. Ports specified using the <code>ListenAddress</code> option override command-line ports.</p>
<dt><code>-q</code></p>
<dd>Quiet mode. Nothing is sent to the system log. Normally the beginning, authentication, and termination of each connection is logged.</p>
<dt><code>-T</code></p>
<dd>Extended test mode. Check the validity of the configuration file, output the effective configuration to stdout and then exit. Optionally, <code>Match</code> rules may be applied by specifying the connection parameters using one or more &#8211;<code>C</code> options.</p>
<dt><code>-t</code></p>
<dd>Test mode. Only check the validity of the configuration file and sanity of the keys. This is useful for updating <code>sshd</code> reliably as configuration options may change.</p>
<dt><code>-u </code><i>len</i></p>
<dd>This option is used to specify the size of the field in the <code>utmp</code> structure that holds the remote host name. If the resolved host name is longer than <i>len</i> the dotted decimal value will be used instead. This allows hosts with very long host names that overflow this field to still be uniquely identified. Specifying &#8211;<code>u0</code> indicates that only dotted decimal addresses should be put into the utmp file. &#8211;<code>u0</code> may also be used to prevent <code>sshd</code> from making DNS requests unless the authentication mechanism or configuration requires it. Authentication mechanisms that may require DNS include <code>RhostsRSAAuthentication</code> <code>HostbasedAuthentication</code> and using a <code>from=pattern-list</code> option in a key file. Configuration options that require DNS include using a USER [at] HOST pattern in <code>AllowUsers</code> or <code>DenyUsers</code></dl>
<h2>Authentication</h2>
<p>The OpenSSH SSH daemon supports SSH protocols 1 and 2. The default is to use protocol 2 only, though this can be changed via the <code>Protocol</code> option in sshd_config5. Protocol 2 supports DSA, ECDSA, ED25519 and RSA keys; protocol 1 only supports RSA keys. For both protocols, each host has a host-specific key, normally 2048 bits, used to identify the host. </p>
<p> Forward security for protocol 1 is provided through an additional server key, normally 768 bits, generated when the server starts. This key is normally regenerated every hour if it has been used, and is never stored on disk. Whenever a client connects, the daemon responds with its public host and server keys. The client compares the RSA host key against its own database to verify that it has not changed. The client then generates a 256-bit random number. It encrypts this random number using both the host key and the server key, and sends the encrypted number to the server. Both sides then use this random number as a session key which is used to encrypt all further communications in the session. The rest of the session is encrypted using a conventional cipher, currently Blowfish or 3DES, with 3DES being used by default. The client selects the encryption algorithm to use from those offered by the server. </p>
<p> For protocol 2, forward security is provided through a Diffie-Hellman key agreement. This key agreement results in a shared session key. The rest of the session is encrypted using a symmetric cipher, currently 128-bit AES, Blowfish, 3DES, CAST128, Arcfour, 192-bit AES, or 256-bit AES. The client selects the encryption algorithm to use from those offered by the server. Additionally, session integrity is provided through a cryptographic message authentication code (hmac-md5, hmac-sha1, umac-64, umac-128, hmac-ripemd160, hmac-sha2-256 or hmac-sha2-512). </p>
<p> Finally, the server and the client enter an authentication dialog. The client tries to authenticate itself using host-based authentication, public key authentication, GSSAPI authentication, challenge-response authentication, or password authentication. </p>
<p> Regardless of the authentication type, the account is checked to ensure that it is accessible. An account is not accessible if it is locked, listed in <code>DenyUsers</code> or its group is listed in <code>DenyGroups</code> . The definition of a locked account is system dependant. Some platforms have their own account database (eg AIX) and some modify the passwd field ( `*LK*&#8217; on Solaris and UnixWare, `*&#8217; on HP-UX, containing `Nologin&#8217; on Tru64, a leading `*LOCKED*&#8217; on FreeBSD and a leading `!&#8217; on most Linuxes). If there is a requirement to disable password authentication for the account while allowing still public-key, then the passwd field should be set to something other than these values (eg `NP&#8217; or `*NP*&#8217; ). </p>
<p> If the client successfully authenticates itself, a dialog for preparing the session is entered. At this time the client may request things like allocating a pseudo-tty, forwarding X11 connections, forwarding TCP connections, or forwarding the authentication agent connection over the secure channel. </p>
<p> After this, the client either requests a shell or execution of a command. The sides then enter session mode. In this mode, either side may send data at any time, and such data is forwarded to/from the shell or command on the server side, and the user terminal in the client side. </p>
<p> When the user program terminates and all forwarded X11 and other connections have been closed, the server sends command exit status to the client, and both sides exit.</p>
<h2>Login Process</h2>
<p>When a user successfully logs in, <code>sshd</code> does the following: </p>
<ol>
<li> If the login is on a tty, and no command has been specified, prints last login time and /etc/motd (unless prevented in the configuration file or by ~/.hushlogin see the Sx FILES section).
<li> If the login is on a tty, records login time.
<li> Checks /etc/nologin if it exists, prints contents and quits (unless root).
<li> Changes to run with normal user privileges.
<li> Sets up basic environment.
<li> Reads the file ~/.ssh/environment if it exists, and users are allowed to change their environment. See the <code>PermitUserEnvironment</code> option in sshd_config5.
<li> Changes to user&#8217;s home directory.
<li> If ~/.ssh/rc exists, runs it; else if /etc/gsissh/sshrc exists, runs it; otherwise runs xauth. The &#8220;rc&#8221; files are given the X11 authentication protocol and cookie in standard input. See Sx SSHRC , below.
<li> Runs user&#8217;s shell or command. </ol>
<h2>Sshrc</h2>
<p>If the file ~/.ssh/rc exists, <a href="/docs/linux/man/1-sh/">sh</a>(1) runs it after reading the environment files but before starting the user&#8217;s shell or command. It must not produce any output on stdout; stderr must be used instead. If X11 forwarding is in use, it will receive the &quot;proto cookie&quot; pair in its standard input (and <code>DISPLAY</code> in its environment). The script must call <a href="/docs/linux/man/1-xauth/">xauth</a>(1) because <code>sshd</code> will not run xauth automatically to add X11 cookies. </p>
<p> The primary purpose of this file is to run any initialization routines which may be needed before the user&#8217;s home directory becomes accessible; AFS is a particular example of such an environment. </p>
<p> This file will probably contain some initialization code followed by something similar to: </p>
<pre>if read proto cookie &amp;&amp; [ -n &quot;$DISPLAY&quot; ]; then
 if [ `echo $DISPLAY | cut -c1-10` = 'localhost:' ]; then
 # X11UseLocalhost=yes
 echo add unix:`echo $DISPLAY |
 cut -c11-` $proto $cookie
 else
 # X11UseLocalhost=no
 echo add $DISPLAY $proto $cookie
 fi | xauth -q -
fi</pre>
<p>If this file does not exist, /etc/gsissh/sshrc is run, and if that does not exist either, xauth is used to add the cookie.</p>
<h2>Authorized_Keys File Format</h2>
<p><code>AuthorizedKeysFile</code> specifies the files containing public keys for public key authentication; if none is specified, the default is ~/.ssh/authorized_keys and ~/.ssh/authorized_keys2 Each line of the file contains one key (empty lines and lines starting with a `#&#8217; are ignored as comments). Protocol 1 public keys consist of the following space-separated fields: options, bits, exponent, modulus, comment. Protocol 2 public key consist of: options, keytype, base64-encoded key, comment. The options field is optional; its presence is determined by whether the line starts with a number or not (the options field never starts with a number). The bits, exponent, modulus, and comment fields give the RSA key for protocol version 1; the comment field is not used for anything (but may be convenient for the user to identify the key). For protocol version 2 the keytype is &#8220;ecdsa-sha2-nistp256&#8221; &#8220;ecdsa-sha2-nistp384&#8221; &#8220;ecdsa-sha2-nistp521&#8221; &#8220;ssh-ed25519&#8221; &#8220;ssh-dss&#8221; or &#8220;ssh-rsa&#8221; </p>
<p> Note that lines in this file are usually several hundred bytes long (because of the size of the public key encoding) up to a limit of 8 kilobytes, which permits DSA keys up to 8 kilobits and RSA keys up to 16 kilobits. You don&#8217;t want to type them in; instead, copy the identity.pub id_dsa.pub id_ecdsa.pub id_ed25519.pub or the id_rsa.pub file and edit it. </p>
<p> <code>sshd</code> enforces a minimum RSA key modulus size for protocol 1 and protocol 2 keys of 768 bits. </p>
<p> The options (if present) consist of comma-separated option specifications. No spaces are permitted, except within double quotes. The following option specifications are supported (note that option keywords are case-insensitive):</p>
<dl>
<dt><code>cert-authority</code></p>
<dd>Specifies that the listed key is a certification authority (CA) that is trusted to validate signed certificates for user authentication. </p>
<p> Certificates may encode access restrictions similar to these key options. If both certificate restrictions and key options are present, the most restrictive union of the two is applied.</p>
<dt><code>command=command</code></p>
<dd>Specifies that the command is executed whenever this key is used for authentication. The command supplied by the user (if any) is ignored. The command is run on a pty if the client requests a pty; otherwise it is run without a tty. If an 8-bit clean channel is required, one must not request a pty or should specify <code>no-pty</code> A quote may be included in the command by quoting it with a backslash. This option might be useful to restrict certain public keys to perform just a specific operation. An example might be a key that permits remote backups but nothing else. Note that the client may specify TCP and/or X11 forwarding unless they are explicitly prohibited. The command originally supplied by the client is available in the <code>SSH_ORIGINAL_COMMAND</code> environment variable. Note that this option applies to shell, command or subsystem execution. Also note that this command may be superseded by either a sshd_config5 <code>ForceCommand</code> directive or a command embedded in a certificate.</p>
<dt><code>environment=NAME=value</code></p>
<dd>Specifies that the string is to be added to the environment when logging in using this key. Environment variables set this way override other default environment values. Multiple options of this type are permitted. Environment processing is disabled by default and is controlled via the <code>PermitUserEnvironment</code> option. This option is automatically disabled if <code>UseLogin</code> is enabled.</p>
<dt><code>from=pattern-list</code></p>
<dd>Specifies that in addition to public key authentication, either the canonical name of the remote host or its IP address must be present in the comma-separated list of patterns. See PATTERNS in ssh_config5 for more information on patterns. </p>
<p> In addition to the wildcard matching that may be applied to hostnames or addresses, a <code>from</code> stanza may match IP addresses using CIDR address/masklen notation. </p>
<p> The purpose of this option is to optionally increase security: public key authentication by itself does not trust the network or name servers or anything (but the key); however, if somebody somehow steals the key, the key permits an intruder to log in from anywhere in the world. This additional option makes using a stolen key more difficult (name servers and/or routers would have to be compromised in addition to just the key).</p>
<dt><code>no-agent-forwarding</code></p>
<dd>Forbids authentication agent forwarding when this key is used for authentication.</p>
<dt><code>no-port-forwarding</code></p>
<dd>Forbids TCP forwarding when this key is used for authentication. Any port forward requests by the client will return an error. This might be used, e.g. in connection with the <code>command</code> option.</p>
<dt><code>no-pty</code></p>
<dd>Prevents tty allocation (a request to allocate a pty will fail).</p>
<dt><code>no-user-rc</code></p>
<dd>Disables execution of ~/.ssh/rc</p>
<dt><code>no-X11-forwarding</code></p>
<dd>Forbids X11 forwarding when this key is used for authentication. Any X11 forward requests by the client will return an error.</p>
<dt><code>permitopen=host:port</code></p>
<dd>Limit local <code>&#8220;ssh -L&#8221;</code> port forwarding such that it may only connect to the specified host and port. IPv6 addresses can be specified by enclosing the address in square brackets. Multiple <code>permitopen</code> options may be applied separated by commas. No pattern matching is performed on the specified hostnames, they must be literal domains or addresses. A port specification of <code>*</code> matches any port.</p>
<dt><code>principals=principals</code></p>
<dd>On a <code>cert-authority</code> line, specifies allowed principals for certificate authentication as a comma-separated list. At least one name from the list must appear in the certificate&#8217;s list of principals for the certificate to be accepted. This option is ignored for keys that are not marked as trusted certificate signers using the <code>cert-authority</code> option.</p>
<dt><code>tunnel=n</code></p>
<dd>Force a <a href="/docs/linux/man/4-tun/">tun</a>(4) device on the server. Without this option, the next available device will be used if the client requests a tunnel.</dl>
<p> An example authorized_keys file: </p>
<pre># Comments allowed at start of line
ssh-rsa AAAAB3Nza...LiPk== user [at] example.net
from=&quot;*.sales.example.net,!pc.sales.example.net&quot; ssh-rsa
AAAAB2...19Q== john [at] example.net
command=&quot;dump /home&quot;,no-pty,no-port-forwarding ssh-dss
AAAAC3...51R== example.net
permitopen=&quot;192.0.2.1:80&quot;,permitopen=&quot;192.0.2.2:25&quot; ssh-dss
AAAAB5...21S==
tunnel=&quot;0&quot;,command=&quot;sh /etc/netstart tun0&quot; ssh-rsa AAAA...==
jane [at] example.net</pre>
<h2>Ssh_Known_Hosts File Format</h2>
<p>The /etc/gsissh/ssh_known_hosts and ~/.ssh/known_hosts files contain host public keys for all known hosts. The global file should be prepared by the administrator (optional), and the per-user file is maintained automatically: whenever the user connects from an unknown host, its key is added to the per-user file. </p>
<p> Each line in these files contains the following fields: markers (optional), hostnames, bits, exponent, modulus, comment. The fields are separated by spaces. </p>
<p> The marker is optional, but if it is present then it must be one of &#8220;@cert-authority&#8221; to indicate that the line contains a certification authority (CA) key, or &#8220;@revoked&#8221; to indicate that the key contained on the line is revoked and must not ever be accepted. Only one marker should be used on a key line. </p>
<p> Hostnames is a comma-separated list of patterns ( `*&#8217; and `?&#8217; act as wildcards); each pattern in turn is matched against the canonical host name (when authenticating a client) or against the user-supplied name (when authenticating a server). A pattern may also be preceded by `!&#8217; to indicate negation: if the host name matches a negated pattern, it is not accepted (by that line) even if it matched another pattern on the line. A hostname or address may optionally be enclosed within `[&#8216; and `]&#8217; brackets then followed by `:&#8217; and a non-standard port number. </p>
<p> Alternately, hostnames may be stored in a hashed form which hides host names and addresses should the file&#8217;s contents be disclosed. Hashed hostnames start with a `|&#8217; character. Only one hashed hostname may appear on a single line and none of the above negation or wildcard operators may be applied. </p>
<p> Bits, exponent, and modulus are taken directly from the RSA host key; they can be obtained, for example, from /etc/gsissh/ssh_host_key.pub The optional comment field continues to the end of the line, and is not used. </p>
<p> Lines starting with `#&#8217; and empty lines are ignored as comments. </p>
<p> When performing host authentication, authentication is accepted if any matching line has the proper key; either one that matches exactly or, if the server has presented a certificate for authentication, the key of the certification authority that signed the certificate. For a key to be trusted as a certification authority, it must use the &#8220;@cert-authority&#8221; marker described above. </p>
<p> The known hosts file also provides a facility to mark keys as revoked, for example when it is known that the associated private key has been stolen. Revoked keys are specified by including the &#8220;@revoked&#8221; marker at the beginning of the key line, and are never accepted for authentication or as certification authorities, but instead will produce a warning from <a href="/docs/linux/man/1-ssh/">ssh</a>(1) when they are encountered. </p>
<p> It is permissible (but not recommended) to have several lines or different host keys for the same names. This will inevitably happen when short forms of host names from different domains are put in the file. It is possible that the files contain conflicting information; authentication is accepted if valid information can be found from either file. </p>
<p> Note that the lines in these files are typically hundreds of characters long, and you definitely don&#8217;t want to type in the host keys by hand. Rather, generate them by a script, ssh-keyscan1 or by taking /etc/gsissh/ssh_host_key.pub and adding the host names at the front. ssh-keygen1 also offers some basic automated editing for ~/.ssh/known_hosts including removing hosts matching a host name and converting all host names to their hashed representations. </p>
<p> An example ssh_known_hosts file: </p>
<pre># Comments allowed at start of line
closenet,...,192.0.2.53 1024 37 159...93 closenet.example.net
cvs.example.net,192.0.2.10 ssh-rsa AAAA1234.....=
# A hashed hostname
|1|JfKTdBh7rNbXkVAQCRp4OQoPfmI=|USECr3SWf1JUPsms5AqfD5QfxkM= ssh-rsa
AAAA1234.....=
# A revoked key
@revoked * ssh-rsa AAAAB5W...
# A CA key, accepted for any host in *.mydomain.com or *.mydomain.org
@cert-authority *.mydomain.org,*.mydomain.com ssh-rsa AAAAB5W...</pre>
<h2>Environment</h2>
<p><code>sshd</code> will normally set the following environment variables:</p>
<dl>
<dt><code>GLOBUS_USAGE_OPTOUT</code></p>
<dd>Setting this environment variable to &quot;1&quot; will disable the reporting of usage metrics. Usage metrics can also be disabled using the <code>DisableUsageStats</code> setting in sshd_config5.</p>
<dt><code>GLOBUS_USAGE_TARGETS</code></p>
<dd>If <code>UsageStatsTargets</code> is not specified in sshd_config5, a comma-separated list of targets (without any tags specified) if specified in the environment variable <code>GLOBUS_USAGE_TARGETS</code> will be used.</p>
<dt><code>GRIDMAP</code></p>
<dd>Applies to GSI authentication/authorization. Specifies the location of the gridmapfile. If not specified, the gridmap file is assumed to be available at /etc/grid-security/grid-mapfile for services running as root and at HOME/.gridmap for services running as non-root where HOME is the home directory of the effective user from the password file entry.</p>
<dt><code>X509_CERT_DIR</code></p>
<dd>Used for GSI authentication. Specifies a non-standard location for the CA certificates directory.</p>
<dt><code>X509_USER_CERT</code></p>
<dd>Used for GSI authentication. Specifies a non-standard location for the certificate to be used for authentication to the client.</p>
<dt><code>X509_USER_KEY</code></p>
<dd>Used for GSI authentication. Specifies a non-standard location for the private key to be used for authentication to the client.</p>
<dt><code>X509_USER_PROXY</code></p>
<dd>Used for GSI authentication. Specifies a non-standard location for the proxy credential to be used for authentication to the client.</dl>
<h2>Files</h2>
<dl>
<dt><code>~/.hushlogin </code></p>
<dd>This file is used to suppress printing the last login time and /etc/motd if <code>PrintLastLog</code> and <code>PrintMotd</code> respectively, are enabled. It does not suppress printing of the banner specified by <code>Banner</code> </p>
<dt><code>~/.rhosts </code></p>
<dd>This file is used for host-based authentication (see <a href="/docs/linux/man/1-ssh/">ssh</a>(1) for more information). On some machines this file may need to be world-readable if the user&#8217;s home directory is on an NFS partition, because <code>sshd</code> reads it as root. Additionally, this file must be owned by the user, and must not have write permissions for anyone else. The recommended permission for most machines is read/write for the user, and not accessible by others. </p>
<dt><code>~/.shosts </code></p>
<dd>This file is used in exactly the same way as .rhosts but allows host-based authentication without permitting login with rlogin/rsh. </p>
<dt><code>~/.k5login </code></p>
<dd>
<dt><code>~/.k5users </code></p>
<dd>These files enforce GSSAPI/Kerberos authentication access control. Further details are described in <a href="/docs/linux/man/1-ksu/">ksu</a>(1). The location of the k5login file depends on the configuration option <code>k5login_directory</code> in the krb5.conf5. </p>
<dt><code>~/.ssh/ </code></p>
<dd>This directory is the default location for all user-specific configuration and authentication information. There is no general requirement to keep the entire contents of this directory secret, but the recommended permissions are read/write/execute for the user, and not accessible by others. </p>
<dt><code>~/.ssh/authorized_keys </code></p>
<dd>Lists the public keys (DSA, ECDSA, ED25519, RSA) that can be used for logging in as this user. The format of this file is described above. The content of the file is not highly sensitive, but the recommended permissions are read/write for the user, and not accessible by others. </p>
<p> If this file, the ~/.ssh directory, or the user&#8217;s home directory are writable by other users, then the file could be modified or replaced by unauthorized users. In this case, <code>sshd</code> will not allow it to be used unless the <code>StrictModes</code> option has been set to &#8220;no&#8221; </p>
<dt><code>~/.ssh/environment </code></p>
<dd>This file is read into the environment at login (if it exists). It can only contain empty lines, comment lines (that start with `#&#8217; ) , and assignment lines of the form name=value. The file should be writable only by the user; it need not be readable by anyone else. Environment processing is disabled by default and is controlled via the <code>PermitUserEnvironment</code> option. </p>
<dt><code>~/.ssh/known_hosts </code></p>
<dd>Contains a list of host keys for all hosts the user has logged into that are not already in the systemwide list of known host keys. The format of this file is described above. This file should be writable only by root/the owner and can, but need not be, world-readable. </p>
<dt><code>~/.ssh/rc </code></p>
<dd>Contains initialization routines to be run before the user&#8217;s home directory becomes accessible. This file should be writable only by the user, and need not be readable by anyone else. </p>
<dt><code>/etc/hosts.allow </code></p>
<dd>
<dt><code>/etc/hosts.deny </code></p>
<dd>Access controls that should be enforced by tcp-wrappers are defined here. Further details are described in hosts_access5. </p>
<dt><code>/etc/hosts.equiv </code></p>
<dd>This file is for host-based authentication (see <a href="/docs/linux/man/1-ssh/">ssh</a>(1)). It should only be writable by root. </p>
<dt><code>/etc/gsissh/moduli </code></p>
<dd>Contains Diffie-Hellman groups used for the &quot;Diffie-Hellman Group Exchange&quot;. The file format is described in <a href="/docs/linux/man/5-moduli/">moduli</a>(5). </p>
<dt><code>/etc/motd </code></p>
<dd>See <a href="/docs/linux/man/5-motd/">motd</a>(5). </p>
<dt><code>/etc/nologin </code></p>
<dd>If this file exists, <code>sshd</code> refuses to let anyone except root log in. The contents of the file are displayed to anyone trying to log in, and non-root connections are refused. The file should be world-readable. </p>
<dt><code>/etc/gsissh/shosts.equiv </code></p>
<dd>This file is used in exactly the same way as hosts.equiv but allows host-based authentication without permitting login with rlogin/rsh. </p>
<dt><code>/etc/gsissh/ssh_host_key </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_dsa_key </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ecdsa_key </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ed25519_key </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_rsa_key </code></p>
<dd>These files contain the private parts of the host keys. These files should only be owned by root, readable only by root, and not accessible to others. Note that <code>sshd</code> does not start if these files are group/world-accessible. </p>
<dt><code>/etc/gsissh/ssh_host_key.pub </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_dsa_key.pub </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ecdsa_key.pub </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_ed25519_key.pub </code></p>
<dd>
<dt><code>/etc/gsissh/ssh_host_rsa_key.pub </code></p>
<dd>These files contain the public parts of the host keys. These files should be world-readable but writable only by root. Their contents should match the respective private parts. These files are not really used for anything; they are provided for the convenience of the user so their contents can be copied to known hosts files. These files are created using ssh-keygen1. </p>
<dt><code>/etc/gsissh/ssh_known_hosts </code></p>
<dd>Systemwide list of known host keys. This file should be prepared by the system administrator to contain the public host keys of all machines in the organization. The format of this file is described above. This file should be writable only by root/the owner and should be world-readable. </p>
<dt><code>/etc/gsissh/sshd_config </code></p>
<dd>Contains configuration data for <code>sshd</code> The file format and configuration options are described in sshd_config5. </p>
<dt><code>/etc/gsissh/sshrc </code></p>
<dd>Similar to ~/.ssh/rc it can be used to specify machine-specific login-time initializations globally. This file should be writable only by root, and should be world-readable. </p>
<dt><code>/var/empty/gsisshd </code></p>
<dd><a href="/docs/linux/man/2-chroot/">chroot</a>(2) directory used by <code>sshd</code> during privilege separation in the pre-authentication phase. The directory should not contain any files and must be owned by root and not group or world-writable. </p>
<dt><code>/var/run/gsisshd.pid </code></p>
<dd>Contains the process ID of the <code>sshd</code> listening for connections (if there are several daemons running concurrently for different ports, this contains the process ID of the one started last). The content of this file is not sensitive; it can be world-readable.</dl>
<h2>Environment</h2>
<dl>
<dt><code>SSH_USE_STRONG_RNG </code></p>
<dd>The reseeding of the OpenSSL random generator is usually done from <code>/dev/urandom</code> If the <code>SSH_USE_STRONG_RNG</code> environment variable is set to value other than <code>0</code> the OpenSSL random generator is reseeded from <code>/dev/random</code> The number of bytes read is defined by the SSH_USE_STRONG_RNG value. Minimum is 14 bytes. This setting is not recommended on the computers without the hardware random generator because insufficient entropy causes the connection to be blocked until enough entropy is available.</dl>
<h2>Ipv6</h2>
<p>IPv6 address can be used everywhere where IPv4 address. In all entries must be the IPv6 address enclosed in square brackets. Note: The square brackets are metacharacters for the shell and must be escaped in shell.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-scp/">scp</a>(1), <a href="/docs/linux/man/1-sftp/">sftp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, ssh-keygen1, ssh-keyscan1, <a href="/docs/linux/man/2-chroot/">chroot</a>(2), hosts_access5, login.conf5, <a href="/docs/linux/man/5-moduli/">moduli</a>(5), sshd_config5, <a href="/docs/linux/man/8-inetd/">inetd</a>(8), sftp-server8</p>
<h2>Authors</h2>
<p>OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. Niels Provos and Markus Friedl contributed support for privilege separation.</p>
<h2>Caveats</h2>
<p>System security is not improved unless <code>rshd</code> <code>rlogind</code> and <code>rexecd</code> are disabled (thus completely disabling rlogin and rsh into the machine).</p>
