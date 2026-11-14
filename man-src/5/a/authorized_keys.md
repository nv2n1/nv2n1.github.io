---
title: "authorized_keys(5)"
name: "authorized_keys"
section: "5"
letter: "a"
url: "/docs/linux/man/5-authorized_keys/"
description: "sshd – OpenSSH daemon"
---

<p><code>sshd</code> &#8211; OpenSSH daemon</p>
<h2>Synopsis</h2>
<p><code>sshd</code> [-<code>46DdeiqTt </code>[-<code>C </code><i>connection_spec</i> ] ] [-<code>c </code><i>host_certificate_file</i> ] [-<code>E </code><i>log_file</i> ] [-<code>f </code><i>config_file</i> ] [-<code>g </code><i>login_grace_time</i> ] [-<code>h </code><i>host_key_file</i> ] [-<code>o </code><i>option</i> ] [-<code>p </code><i>port</i> ] [-<code>u </code><i>len</i> ]</p>
<h2>Description</h2>
<p><code>sshd</code> (OpenSSH Daemon) is the daemon program for <a href="/docs/linux/man/1-ssh/">ssh</a>(1). It provides secure encrypted communications between two untrusted hosts over an insecure network. <code>sshd</code> listens for connections from clients. It is normally started at boot from /etc/init.d/ssh It forks a new daemon for each incoming connection. The forked daemons handle key exchange, encryption, authentication, command execution, and data exchange. <code>sshd</code> can be configured using command-line options or a configuration file (by default sshd_config5); command-line options override values specified in the configuration file. <code>sshd</code> rereads its configuration file when it receives a hangup signal, <code>SIGHUP</code> by executing itself with the name and options it was started with, e.g. /usr/sbin/sshd The options are as follows:</p>
<dl>
<dt><code>-4</code></p>
<dd>Forces <code>sshd</code> to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd>Forces <code>sshd</code> to use IPv6 addresses only.</p>
<dt><code>-C </code><i>connection_spec</i></p>
<dd>Specify the connection parameters to use for the &#8211;<code>T</code> extended test mode. If provided, any <code>Match</code> directives in the configuration file that would apply are applied before the configuration is written to standard output. The connection parameters are supplied as keyword=value pairs and may be supplied in any order, either with multiple &#8211;<code>C</code> options or as a comma-separated list. The keywords are &#8220;addr&#8221; &#8220;user&#8221; &#8220;host&#8221; &#8220;laddr&#8221; &#8220;lport&#8221; and &#8220;rdomain&#8221; and correspond to source address, user, resolved source host name, local address, local port number and routing domain respectively.</p>
<dt><code>-c </code><i>host_certificate_file</i></p>
<dd>Specifies a path to a certificate file to identify <code>sshd</code> during key exchange. The certificate file must match a host key file specified using the &#8211;<code>h</code> option or the <code>HostKey</code> configuration directive.</p>
<dt><code>-D</code></p>
<dd>When this option is specified, <code>sshd</code> will not detach and does not become a daemon. This allows easy monitoring of <code>sshd</code></p>
<dt><code>-d</code></p>
<dd>Debug mode. The server sends verbose debug output to standard error, and does not put itself in the background. The server also will not <a href="/docs/linux/man/2-fork/">fork</a>(2) and will only process one connection. This option is only intended for debugging for the server. Multiple &#8211;<code>d</code> options increase the debugging level. Maximum is 3.</p>
<dt><code>-E </code><i>log_file</i></p>
<dd>Append debug logs to <i>log_file</i> instead of the system log.</p>
<dt><code>-e</code></p>
<dd>Write debug logs to standard error instead of the system log.</p>
<dt><code>-f </code><i>config_file</i></p>
<dd>Specifies the name of the configuration file. The default is /etc/ssh/sshd_config <code>sshd</code> refuses to start if there is no configuration file.</p>
<dt><code>-g </code><i>login_grace_time</i></p>
<dd>Gives the grace time for clients to authenticate themselves (default 120 seconds). If the client fails to authenticate the user within this many seconds, the server disconnects and exits. A value of zero indicates no limit.</p>
<dt><code>-h </code><i>host_key_file</i></p>
<dd>Specifies a file from which a host key is read. This option must be given if <code>sshd</code> is not run as root (as the normal host key files are normally not readable by anyone but root). The default is /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_ed25519_key and /etc/ssh/ssh_host_rsa_key It is possible to have multiple host key files for the different host key algorithms.</p>
<dt><code>-i</code></p>
<dd>Specifies that <code>sshd</code> is being run from <a href="/docs/linux/man/8-inetd/">inetd</a>(8).</p>
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
<dd>This option is used to specify the size of the field in the <code>utmp</code> structure that holds the remote host name. If the resolved host name is longer than <i>len</i> the dotted decimal value will be used instead. This allows hosts with very long host names that overflow this field to still be uniquely identified. Specifying &#8211;<code>u0</code> indicates that only dotted decimal addresses should be put into the utmp file. &#8211;<code>u0</code> may also be used to prevent <code>sshd</code> from making DNS requests unless the authentication mechanism or configuration requires it. Authentication mechanisms that may require DNS include <code>HostbasedAuthentication</code> and using a <code>from=pattern-list</code> option in a key file. Configuration options that require DNS include using a USER [at] HOST pattern in <code>AllowUsers</code> or <code>DenyUsers</code></dl>
<h2>Authentication</h2>
<p>The OpenSSH SSH daemon supports SSH protocol 2 only. Each host has a host-specific key, used to identify the host. Whenever a client connects, the daemon responds with its public host key. The client compares the host key against its own database to verify that it has not changed. Forward secrecy is provided through a Diffie-Hellman key agreement. This key agreement results in a shared session key. The rest of the session is encrypted using a symmetric cipher. The client selects the encryption algorithm to use from those offered by the server. Additionally, session integrity is provided through a cryptographic message authentication code (MAC). </p>
<p> Finally, the server and the client enter an authentication dialog. The client tries to authenticate itself using host-based authentication, public key authentication, challenge-response authentication, or password authentication. </p>
<p> Regardless of the authentication type, the account is checked to ensure that it is accessible. An account is not accessible if it is locked, listed in <code>DenyUsers</code> or its group is listed in <code>DenyGroups</code> . The definition of a locked account is system dependent. Some platforms have their own account database (eg AIX) and some modify the passwd field ( `*LK*&#8217; on Solaris and UnixWare, `*&#8217; on HP-UX, containing `Nologin&#8217; on Tru64, a leading `*LOCKED*&#8217; on FreeBSD and a leading `!&#8217; on most Linuxes). If there is a requirement to disable password authentication for the account while allowing still public-key, then the passwd field should be set to something other than these values (eg `NP&#8217; or `*NP*&#8217; ). </p>
<p> If the client successfully authenticates itself, a dialog for preparing the session is entered. At this time the client may request things like allocating a pseudo-tty, forwarding X11 connections, forwarding TCP connections, or forwarding the authentication agent connection over the secure channel. </p>
<p> After this, the client either requests an interactive shell or execution or a non-interactive command, which <code>sshd</code> will execute via the user&#8217;s shell using its &#8211;<code>c</code> option. The sides then enter session mode. In this mode, either side may send data at any time, and such data is forwarded to/from the shell or command on the server side, and the user terminal in the client side. </p>
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
<li> If ~/.ssh/rc exists and the sshd_config5 <code>PermitUserRC</code> option is set, runs it; else if /etc/ssh/sshrc exists, runs it; otherwise runs <a href="/docs/linux/man/1-xauth/">xauth</a>(1). The &#8220;rc&#8221; files are given the X11 authentication protocol and cookie in standard input. See Sx SSHRC , below.
<li> Runs user&#8217;s shell or command. All commands are run under the user&#8217;s login shell as specified in the system password database. </ol>
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
<p>If this file does not exist, /etc/ssh/sshrc is run, and if that does not exist either, xauth is used to add the cookie.</p>
<h2>Authorized_Keys File Format</h2>
<p><code>AuthorizedKeysFile</code> specifies the files containing public keys for public key authentication; if this option is not specified, the default is ~/.ssh/authorized_keys and ~/.ssh/authorized_keys2 Each line of the file contains one key (empty lines and lines starting with a `#&#8217; are ignored as comments). Public keys consist of the following space-separated fields: options, keytype, base64-encoded key, comment. The options field is optional. The supported key types are: </p>
<dl>
<dt><code>sk-ecdsa-sha2-nistp256 [at] openssh.com</code></p>
<dd>
<dt><code>ecdsa-sha2-nistp256</code></p>
<dd>
<dt><code>ecdsa-sha2-nistp384</code></p>
<dd>
<dt><code>ecdsa-sha2-nistp521</code></p>
<dd>
<dt><code>sk-ssh-ed25519 [at] openssh.com</code></p>
<dd>
<dt><code>ssh-ed25519</code></p>
<dd>
<dt><code>ssh-dss</code></p>
<dd>
<dt><code>ssh-rsa</code></p>
<dd></dl>
<p> The comment field is not used for anything (but may be convenient for the user to identify the key). </p>
<p> Note that lines in this file can be several hundred bytes long (because of the size of the public key encoding) up to a limit of 8 kilobytes, which permits RSA keys up to 16 kilobits. You don&#8217;t want to type them in; instead, copy the id_dsa.pub id_ecdsa.pub id_ecdsa_sk.pub id_ed25519.pub id_ed25519_sk.pub or the id_rsa.pub file and edit it. </p>
<p> <code>sshd</code> enforces a minimum RSA key modulus size of 1024 bits. </p>
<p> The options (if present) consist of comma-separated option specifications. No spaces are permitted, except within double quotes. The following option specifications are supported (note that option keywords are case-insensitive):</p>
<dl>
<dt><code>agent-forwarding</code></p>
<dd>Enable authentication agent forwarding previously disabled by the <code>restrict</code> option.</p>
<dt><code>cert-authority</code></p>
<dd>Specifies that the listed key is a certification authority (CA) that is trusted to validate signed certificates for user authentication. </p>
<p> Certificates may encode access restrictions similar to these key options. If both certificate restrictions and key options are present, the most restrictive union of the two is applied.</p>
<dt><code>command=command</code></p>
<dd>Specifies that the command is executed whenever this key is used for authentication. The command supplied by the user (if any) is ignored. The command is run on a pty if the client requests a pty; otherwise it is run without a tty. If an 8-bit clean channel is required, one must not request a pty or should specify <code>no-pty</code> A quote may be included in the command by quoting it with a backslash. </p>
<p> This option might be useful to restrict certain public keys to perform just a specific operation. An example might be a key that permits remote backups but nothing else. Note that the client may specify TCP and/or X11 forwarding unless they are explicitly prohibited, e.g. using the <code>restrict</code> key option. </p>
<p> The command originally supplied by the client is available in the <code>SSH_ORIGINAL_COMMAND</code> environment variable. Note that this option applies to shell, command or subsystem execution. Also note that this command may be superseded by a sshd_config5 <code>ForceCommand</code> directive. </p>
<p> If a command is specified and a forced-command is embedded in a certificate used for authentication, then the certificate will be accepted only if the two commands are identical.</p>
<dt><code>environment=NAME=value</code></p>
<dd>Specifies that the string is to be added to the environment when logging in using this key. Environment variables set this way override other default environment values. Multiple options of this type are permitted. Environment processing is disabled by default and is controlled via the <code>PermitUserEnvironment</code> option.</p>
<dt><code>expiry-time=timespec</code></p>
<dd>Specifies a time after which the key will not be accepted. The time may be specified as a YYYYMMDD date or a YYYYMMDDHHMM[SS] time in the system time-zone.</p>
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
<dt><code>permitlisten=[host:]port</code></p>
<dd>Limit remote port forwarding with the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) &#8211;<code>R</code> option such that it may only listen on the specified host (optional) and port. IPv6 addresses can be specified by enclosing the address in square brackets. Multiple <code>permitlisten</code> options may be applied separated by commas. Hostnames may include wildcards as described in the PATTERNS section in ssh_config5. A port specification of <code>*</code> matches any port. Note that the setting of <code>GatewayPorts</code> may further restrict listen addresses. Note that <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will send a hostname of &#8220;localhost&#8221; if a listen host was not specified when the forwarding was requested, and that this name is treated differently to the explicit localhost addresses &#8220;127.0.0.1&#8221; and &#8220;::1&#8221;</p>
<dt><code>permitopen=host:port</code></p>
<dd>Limit local port forwarding with the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) &#8211;<code>L</code> option such that it may only connect to the specified host and port. IPv6 addresses can be specified by enclosing the address in square brackets. Multiple <code>permitopen</code> options may be applied separated by commas. No pattern matching or name lookup is performed on the specified hostnames, they must be literal host names and/or addresses. A port specification of <code>*</code> matches any port.</p>
<dt><code>port-forwarding</code></p>
<dd>Enable port forwarding previously disabled by the <code>restrict</code> option.</p>
<dt><code>principals=principals</code></p>
<dd>On a <code>cert-authority</code> line, specifies allowed principals for certificate authentication as a comma-separated list. At least one name from the list must appear in the certificate&#8217;s list of principals for the certificate to be accepted. This option is ignored for keys that are not marked as trusted certificate signers using the <code>cert-authority</code> option.</p>
<dt><code>pty</code></p>
<dd>Permits tty allocation previously disabled by the <code>restrict</code> option.</p>
<dt><code>no-touch-required</code></p>
<dd>Do not require demonstration of user presence for signatures made using this key. This option only makes sense for the FIDO authenticator algorithms <code>ecdsa-sk</code> and <code>ed25519-sk</code></p>
<dt><code>verify-required</code></p>
<dd>Require that signatures made using this key attest that they verified the user, e.g. via a PIN. This option only makes sense for the FIDO authenticator algorithms <code>ecdsa-sk</code> and <code>ed25519-sk</code></p>
<dt><code>restrict</code></p>
<dd>Enable all restrictions, i.e. disable port, agent and X11 forwarding, as well as disabling PTY allocation and execution of ~/.ssh/rc If any future restriction capabilities are added to authorized_keys files they will be included in this set.</p>
<dt><code>tunnel=n</code></p>
<dd>Force a <a href="/docs/linux/man/4-tun/">tun</a>(4) device on the server. Without this option, the next available device will be used if the client requests a tunnel.</p>
<dt><code>user-rc</code></p>
<dd>Enables execution of ~/.ssh/rc previously disabled by the <code>restrict</code> option.</p>
<dt><code>X11-forwarding</code></p>
<dd>Permits X11 forwarding previously disabled by the <code>restrict</code> option.</dl>
<p> An example authorized_keys file: </p>
<pre># Comments are allowed at start of line. Blank lines are allowed.
# Plain key, no restrictions
ssh-rsa ...
# Forced command, disable PTY and all forwarding
restrict,command=&quot;dump /home&quot; ssh-rsa ...
# Restriction of ssh -L forwarding destinations
permitopen=&quot;192.0.2.1:80&quot;,permitopen=&quot;192.0.2.2:25&quot; ssh-rsa ...
# Restriction of ssh -R forwarding listeners
permitlisten=&quot;localhost:8080&quot;,permitlisten=&quot;[::1]:22000&quot; ssh-rsa ...
# Configuration for tunnel forwarding
tunnel=&quot;0&quot;,command=&quot;sh /etc/netstart tun0&quot; ssh-rsa ...
# Override of restriction to allow PTY allocation
restrict,pty,command=&quot;nethack&quot; ssh-rsa ...
# Allow FIDO key without requiring touch
no-touch-required sk-ecdsa-sha2-nistp256 [at] openssh.com ...
# Require user-verification (e.g. PIN or biometric) for FIDO key
verify-required sk-ecdsa-sha2-nistp256 [at] openssh.com ...
# Trust CA key, allow touch-less FIDO if requested in certificate
cert-authority,no-touch-required,principals=&quot;user_a&quot; ssh-rsa ...</pre>
<h2>Ssh_Known_Hosts File Format</h2>
<p>The /etc/ssh/ssh_known_hosts and ~/.ssh/known_hosts files contain host public keys for all known hosts. The global file should be prepared by the administrator (optional), and the per-user file is maintained automatically: whenever the user connects to an unknown host, its key is added to the per-user file. </p>
<p> Each line in these files contains the following fields: marker (optional), hostnames, keytype, base64-encoded key, comment. The fields are separated by spaces. </p>
<p> The marker is optional, but if it is present then it must be one of &#8220;@cert-authority&#8221; to indicate that the line contains a certification authority (CA) key, or &#8220;@revoked&#8221; to indicate that the key contained on the line is revoked and must not ever be accepted. Only one marker should be used on a key line. </p>
<p> Hostnames is a comma-separated list of patterns ( `*&#8217; and `?&#8217; act as wildcards); each pattern in turn is matched against the host name. When <code>sshd</code> is authenticating a client, such as when using <code>HostbasedAuthentication</code> this will be the canonical client host name. When <a href="/docs/linux/man/1-ssh/">ssh</a>(1) is authenticating a server, this will be the host name given by the user, the value of the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) <code>HostkeyAlias</code> if it was specified, or the canonical server hostname if the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) <code>CanonicalizeHostname</code> option was used. </p>
<p> A pattern may also be preceded by `!&#8217; to indicate negation: if the host name matches a negated pattern, it is not accepted (by that line) even if it matched another pattern on the line. A hostname or address may optionally be enclosed within `[&#8216; and `]&#8217; brackets then followed by `:&#8217; and a non-standard port number. </p>
<p> Alternately, hostnames may be stored in a hashed form which hides host names and addresses should the file&#8217;s contents be disclosed. Hashed hostnames start with a `|&#8217; character. Only one hashed hostname may appear on a single line and none of the above negation or wildcard operators may be applied. </p>
<p> The keytype and base64-encoded key are taken directly from the host key; they can be obtained, for example, from /etc/ssh/ssh_host_rsa_key.pub The optional comment field continues to the end of the line, and is not used. </p>
<p> Lines starting with `#&#8217; and empty lines are ignored as comments. </p>
<p> When performing host authentication, authentication is accepted if any matching line has the proper key; either one that matches exactly or, if the server has presented a certificate for authentication, the key of the certification authority that signed the certificate. For a key to be trusted as a certification authority, it must use the &#8220;@cert-authority&#8221; marker described above. </p>
<p> The known hosts file also provides a facility to mark keys as revoked, for example when it is known that the associated private key has been stolen. Revoked keys are specified by including the &#8220;@revoked&#8221; marker at the beginning of the key line, and are never accepted for authentication or as certification authorities, but instead will produce a warning from <a href="/docs/linux/man/1-ssh/">ssh</a>(1) when they are encountered. </p>
<p> It is permissible (but not recommended) to have several lines or different host keys for the same names. This will inevitably happen when short forms of host names from different domains are put in the file. It is possible that the files contain conflicting information; authentication is accepted if valid information can be found from either file. </p>
<p> Note that the lines in these files are typically hundreds of characters long, and you definitely don&#8217;t want to type in the host keys by hand. Rather, generate them by a script, ssh-keyscan1 or by taking, for example, /etc/ssh/ssh_host_rsa_key.pub and adding the host names at the front. ssh-keygen1 also offers some basic automated editing for ~/.ssh/known_hosts including removing hosts matching a host name and converting all host names to their hashed representations. </p>
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
<h2>Files</h2>
<dl>
<dt><code>~/.hushlogin </code></p>
<dd>This file is used to suppress printing the last login time and /etc/motd if <code>PrintLastLog</code> and <code>PrintMotd</code> respectively, are enabled. It does not suppress printing of the banner specified by <code>Banner</code> </p>
<dt><code>~/.rhosts </code></p>
<dd>This file is used for host-based authentication (see <a href="/docs/linux/man/1-ssh/">ssh</a>(1) for more information). On some machines this file may need to be world-readable if the user&#8217;s home directory is on an NFS partition, because <code>sshd</code> reads it as root. Additionally, this file must be owned by the user, and must not have write permissions for anyone else. The recommended permission for most machines is read/write for the user, and not accessible by others. </p>
<dt><code>~/.shosts </code></p>
<dd>This file is used in exactly the same way as .rhosts but allows host-based authentication without permitting login with rlogin/rsh. </p>
<dt><code>~/.ssh/ </code></p>
<dd>This directory is the default location for all user-specific configuration and authentication information. There is no general requirement to keep the entire contents of this directory secret, but the recommended permissions are read/write/execute for the user, and not accessible by others. </p>
<dt><code>~/.ssh/authorized_keys </code></p>
<dd>Lists the public keys (DSA, ECDSA, Ed25519, RSA) that can be used for logging in as this user. The format of this file is described above. The content of the file is not highly sensitive, but the recommended permissions are read/write for the user, and not accessible by others. </p>
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
<dt><code>/etc/ssh/moduli </code></p>
<dd>Contains Diffie-Hellman groups used for the &quot;Diffie-Hellman Group Exchange&quot; key exchange method. The file format is described in <a href="/docs/linux/man/5-moduli/">moduli</a>(5). If no usable groups are found in this file then fixed internal groups will be used. </p>
<dt><code>/etc/motd </code></p>
<dd>See <a href="/docs/linux/man/5-motd/">motd</a>(5). </p>
<dt><code>/etc/nologin </code></p>
<dd>If this file exists, <code>sshd</code> refuses to let anyone except root log in. The contents of the file are displayed to anyone trying to log in, and non-root connections are refused. The file should be world-readable. </p>
<dt><code>/etc/ssh/shosts.equiv </code></p>
<dd>This file is used in exactly the same way as hosts.equiv but allows host-based authentication without permitting login with rlogin/rsh. </p>
<dt><code>/etc/ssh/ssh_host_ecdsa_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ed25519_key </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_rsa_key </code></p>
<dd>These files contain the private parts of the host keys. These files should only be owned by root, readable only by root, and not accessible to others. Note that <code>sshd</code> does not start if these files are group/world-accessible. </p>
<dt><code>/etc/ssh/ssh_host_ecdsa_key.pub </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_ed25519_key.pub </code></p>
<dd>
<dt><code>/etc/ssh/ssh_host_rsa_key.pub </code></p>
<dd>These files contain the public parts of the host keys. These files should be world-readable but writable only by root. Their contents should match the respective private parts. These files are not really used for anything; they are provided for the convenience of the user so their contents can be copied to known hosts files. These files are created using ssh-keygen1. </p>
<dt><code>/etc/ssh/ssh_known_hosts </code></p>
<dd>Systemwide list of known host keys. This file should be prepared by the system administrator to contain the public host keys of all machines in the organization. The format of this file is described above. This file should be writable only by root/the owner and should be world-readable. </p>
<dt><code>/etc/ssh/sshd_config </code></p>
<dd>Contains configuration data for <code>sshd</code> The file format and configuration options are described in sshd_config5. </p>
<dt><code>/etc/ssh/sshrc </code></p>
<dd>Similar to ~/.ssh/rc it can be used to specify machine-specific login-time initializations globally. This file should be writable only by root, and should be world-readable. </p>
<dt><code>/run/sshd </code></p>
<dd><a href="/docs/linux/man/2-chroot/">chroot</a>(2) directory used by <code>sshd</code> during privilege separation in the pre-authentication phase. The directory should not contain any files and must be owned by root and not group or world-writable. </p>
<dt><code>/run/sshd.pid </code></p>
<dd>Contains the process ID of the <code>sshd</code> listening for connections (if there are several daemons running concurrently for different ports, this contains the process ID of the one started last). The content of this file is not sensitive; it can be world-readable.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-scp/">scp</a>(1), <a href="/docs/linux/man/1-sftp/">sftp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, ssh-keygen1, ssh-keyscan1, <a href="/docs/linux/man/2-chroot/">chroot</a>(2), hosts_access5, <a href="/docs/linux/man/5-moduli/">moduli</a>(5), sshd_config5, <a href="/docs/linux/man/8-inetd/">inetd</a>(8), sftp-server8</p>
<h2>Authors</h2>
<p>OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. Niels Provos and Markus Friedl contributed support for privilege separation.</p>
