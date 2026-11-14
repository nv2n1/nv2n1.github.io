---
title: "heimdal-ftpd(8)"
name: "heimdal-ftpd"
section: "8"
letter: "h"
url: "/docs/linux/man/8-heimdal-ftpd/"
description: "ftpd – Internet File Transfer Protocol server"
---

<p><code>ftpd</code> &#8211; Internet File Transfer Protocol server</p>
<h2>Synopsis</h2>
<p>[-<code>a </code><i>authmode</i> ] [-<code>dilvU</code> ] [-<code>g </code><i>umask</i> ] [-<code>p </code><i>port</i> ] [-<code>T </code><i>maxtimeout</i> ] [-<code>t </code><i>timeout</i> ] [-<code>-gss-bindings</code> ] [-<code>I | &#8211;no-insecure-oob</code> ] [-<code>u </code><i>default umask</i> ] [-<code>B | &#8211;builtin-ls</code> ] [-<code>-good-chars= </code><i>string</i> ]</p>
<h2>Description</h2>
<p><code>Ftpd</code> is the Internet File Transfer Protocol server process. The server uses the <code>TCP</code> protocol and listens at the port specified in the &#8220;ftp&#8221; service specification; see <a href="/docs/linux/man/5-services/">services</a>(5). Available options:</p>
<dl>
<dt><code>-a</code></p>
<dd>Select the level of authentication required. Kerberised login can not be turned off. The default is to only allow kerberised login. Other possibilities can be turned on by giving a string of comma separated flags as argument to &#8211;<code>a</code> Recognised flags are:</p>
<dl>
<dt><i>plain</i></p>
<dd>Allow logging in with plaintext password. The password can be <a href="/docs/linux/man/n-a/">a</a>(n) OTP or an ordinary password.</p>
<dt><i>otp</i></p>
<dd>Same as <i>plain</i> but only OTP is allowed.</p>
<dt><i>ftp</i></p>
<dd>Allow anonymous login.</dl>
<p> The following combination modes exists for backwards compatibility:</p>
<dl>
<dt><i>none</i></p>
<dd>Same as <i>plain,ftp</i></p>
<dt><i>safe</i></p>
<dd>Same as <i>ftp</i></p>
<dt><i>user</i></p>
<dd>Ignored.</dl>
<dt><code>-d</code></p>
<dd>Debugging information is written to the syslog using LOG_FTP.</p>
<dt><code>-g</code></p>
<dd>Anonymous users will get a umask of <i>umask</i></p>
<dt><code>&#8211;gss-bindings</code></p>
<dd>require the peer to use GSS-API bindings (ie make sure IP addresses match).</p>
<dt><code>-i</code></p>
<dd>Open a socket and wait for a connection. This is mainly used for debugging when ftpd isn&#8217;t started by inetd.</p>
<dt><code>-l</code></p>
<dd>Each successful and failed <a href="/docs/linux/man/1-ftp/">ftp</a>(1) session is logged using syslog with a facility of LOG_FTP. If this option is specified twice, the retrieve (get), store (put), append, delete, make directory, remove directory and rename operations and their filename arguments are also logged.</p>
<dt><code>-p</code></p>
<dd>Use <i>port</i> (a service name or number) instead of the default <i>ftp/tcp</i></p>
<dt><code>-T</code></p>
<dd>A client may also request a different timeout period; the maximum period allowed may be set to <i>timeout</i> seconds with the &#8211;<code>T</code> option. The default limit is 2 hours.</p>
<dt><code>-t</code></p>
<dd>The inactivity timeout period is set to <i>timeout</i> seconds (the default is 15 minutes).</p>
<dt><code>-u</code></p>
<dd>Set the initial umask to something else than the default 027.</p>
<dt><code>-U</code></p>
<dd>In previous versions of <code>ftpd</code> when a passive mode client requested a data connection to the server, the server would use data ports in the range 1024..4999. Now, by default, if the system supports the IP_PORTRANGE socket option, the server will use data ports in the range 49152..65535. Specifying this option will revert to the old behavior.</p>
<dt><code>-v</code></p>
<dd>Verbose mode.</p>
<dt> &#8211;<code>B</code> &#8211;<code>-builtin-ls</code></p>
<dd>
<dd>use built-in ls to list files</p>
<dt> &#8211;<code>-good-chars= </code><i>string</i></p>
<dd>
<dd>allowed anonymous upload filename chars</p>
<dt> &#8211;<code>I</code> &#8211;<code>-no-insecure-oob</code></p>
<dd>
<dd>don&#8217;t allow insecure out of band. Heimdal ftp clients before 0.6.3 doesn&#8217;t support secure oob, so turning on this option makes them no longer work.</dl>
<p> The file /etc/nologin can be used to disable ftp access. If the file exists, displays it and exits. If the file /etc/ftpwelcome exists, prints it before issuing the &#8220;ready&#8221; message. If the file /etc/motd exists, prints it after a successful login. The ftp server currently supports the following ftp requests. The case of the requests is ignored.</p>
<dl>
<dt><code>Request Ta </code>Description</p>
<dd>
<dt><code>ABOR Ta </code>abort previous command</p>
<dd>
<dt><code>ACCT Ta </code>specify account (ignored)</p>
<dd>
<dt><code>ALLO Ta </code>allocate storage (vacuously)</p>
<dd>
<dt><code>APPE Ta </code>append to a file</p>
<dd>
<dt><code>CDUP Ta </code>change to parent of current working directory</p>
<dd>
<dt><code>CWD Ta </code>change working directory</p>
<dd>
<dt><code>DELE Ta </code>delete a file</p>
<dd>
<dt><code>HELP Ta </code>give help information</p>
<dd>
<dt><code>LIST Ta </code>give list files in a directory (&#8220;<code>ls -lgA</code> &#8221; )</p>
<dd>
<dt><code>MKD Ta </code>make a directory</p>
<dd>
<dt><code>MDTM Ta </code>show last modification time of file</p>
<dd>
<dt><code>MODE Ta </code>specify data transfer <i>mode</i></p>
<dd>
<dt><code>NLST Ta </code>give name list of files in directory</p>
<dd>
<dt><code>NOOP Ta </code>do nothing</p>
<dd>
<dt><code>PASS Ta </code>specify password</p>
<dd>
<dt><code>PASV Ta </code>prepare for server-to-server transfer</p>
<dd>
<dt><code>PORT Ta </code>specify data connection port</p>
<dd>
<dt><code>PWD Ta </code>print the current working directory</p>
<dd>
<dt><code>QUIT Ta </code>terminate session</p>
<dd>
<dt><code>REST Ta </code>restart incomplete transfer</p>
<dd>
<dt><code>RETR Ta </code>retrieve a file</p>
<dd>
<dt><code>RMD Ta </code>remove a directory</p>
<dd>
<dt><code>RNFR Ta </code>specify rename-from file name</p>
<dd>
<dt><code>RNTO Ta </code>specify rename-to file name</p>
<dd>
<dt><code>SITE Ta </code>non-standard commands (see next section)</p>
<dd>
<dt><code>SIZE Ta </code>return size of file</p>
<dd>
<dt><code>STAT Ta </code>return status of server</p>
<dd>
<dt><code>STOR Ta </code>store a file</p>
<dd>
<dt><code>STOU Ta </code>store a file with a unique name</p>
<dd>
<dt><code>STRU Ta </code>specify data transfer <i>structure</i></p>
<dd>
<dt><code>SYST Ta </code>show operating system type of server system</p>
<dd>
<dt><code>TYPE Ta </code>specify data transfer <i>type</i></p>
<dd>
<dt><code>USER Ta </code>specify user name</p>
<dd>
<dt><code>XCUP Ta </code>change to parent of current working directory (deprecated)</p>
<dd>
<dt><code>XCWD Ta </code>change working directory (deprecated)</p>
<dd>
<dt><code>XMKD Ta </code>make a directory (deprecated)</p>
<dd>
<dt><code>XPWD Ta </code>print the current working directory (deprecated)</p>
<dd>
<dt><code>XRMD Ta </code>remove a directory (deprecated)</p>
<dd></dl>
<p> The following commands are specified by RFC2228.</p>
<dl>
<dt><code>AUTH Ta </code>authentication/security mechanism</p>
<dd>
<dt><code>ADAT Ta </code>authentication/security data</p>
<dd>
<dt><code>PROT Ta </code>data channel protection level</p>
<dd>
<dt><code>PBSZ Ta </code>protection buffer size</p>
<dd>
<dt><code>MIC Ta </code>integrity protected command</p>
<dd>
<dt><code>CONF Ta </code>confidentiality protected command</p>
<dd>
<dt><code>ENC Ta </code>privacy protected command</p>
<dd>
<dt><code>CCC Ta </code>clear command channel</p>
<dd></dl>
<p> The following non-standard or <code>UNIX</code> specific commands are supported by the SITE request. </p>
<dt><code>UMASK Ta </code>change umask, (e.g.</p>
<dd><code>SITE UMASK 002</code></p>
<dt><code>IDLE Ta </code>set idle-timer, (e.g.</p>
<dd><code>SITE IDLE 60</code></p>
<dt><code>CHMOD Ta </code>change mode of a file (e.g.</p>
<dd><code>SITE CHMOD 755 filename</code></p>
<dt><code>FIND Ta </code>quickly find a specific file with GNU</p>
<dd><a href="/docs/linux/man/1-locate/">locate</a>(1).</p>
<dt><code>HELP Ta </code>give help information.</p>
<dd></dl>
<p> The following Kerberos related site commands are understood.</p>
<dl>
<dt><code>KAUTH Ta </code>obtain remote tickets.</p>
<dd>
<dt><code>KLIST Ta </code>show remote tickets</p>
<dd></dl>
<p> The remaining ftp requests specified in Internet RFC 959 are recognized, but not implemented. MDTM and SIZE are not specified in RFC 959, but will appear in the next updated FTP RFC. The ftp server will abort an active file transfer only when the ABOR command is preceded by a Telnet &quot;Interrupt Process&quot; (IP) signal and a Telnet &quot;Synch&quot; signal in the command Telnet stream, as described in Internet RFC 959. If a STAT command is received during a data transfer, preceded by a Telnet IP and Synch, transfer status will be returned. <code>Ftpd</code> interprets file names according to the &#8220;globbing&#8221; conventions used by <a href="/docs/linux/man/1-csh/">csh</a>(1). This allows users to use the metacharacters &#8220;<code>*?[]{}~</code> &#8221; <code>Ftpd</code> authenticates users according to these rules.  </p>
<li> If Kerberos authentication is used, the user must pass valid tickets and the principal must be allowed to login as the remote user.
<li> The login name must be in the password data base, and not have a null password (if Kerberos is used the password field is not checked). In this case a password must be provided by the client before any file operations may be performed. If the user has an OTP key, the response from a successful USER command will include an OTP challenge. The client may choose to respond with a PASS command giving either a standard password or an OTP one-time password. The server will automatically determine which type of password it has been given and attempt to authenticate accordingly. See <a href="/docs/linux/man/1-otp/">otp</a>(1) for more information on OTP authentication.
<li> The login name must not appear in the file /etc/ftpusers
<li> The user must have a standard shell returned by <a href="/docs/linux/man/3-getusershell/">getusershell</a>(3).
<li> If the user name appears in the file /etc/ftpchroot the session&#8217;s root will be changed to the user&#8217;s login directory by <a href="/docs/linux/man/2-chroot/">chroot</a>(2) as for an &#8220;anonymous&#8221; or &#8220;ftp&#8221; account (see next item). However, the user must still supply a password. This feature is intended as a compromise between a fully anonymous account and a fully privileged account. The account should also be set up as for an anonymous account.
<li> If the user name is &#8220;anonymous&#8221; or &#8220;ftp&#8221; an anonymous ftp account must be present in the password file (user &#8220;ftp )&#8221; In this case the user is allowed to log in by specifying any password (by convention an email address for the user should be used as the password). </ol>
<p> In the last case, <code>ftpd</code> takes special measures to restrict the client&#8217;s access privileges. The server performs a <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to the home directory of the &#8220;ftp&#8221; user. In order that system security is not breached, it is recommended that the &#8220;ftp&#8221; subtree be constructed with care, consider following these guidelines for anonymous ftp. In general all files should be owned by &#8220;root&#8221; and have non-write permissions (644 or 755 depending on the kind of file). No files should be owned or writable by &#8220;ftp&#8221; (possibly with exception for the ~ftp/incoming as specified below).</p>
<dl>
<dt><code>~ftp </code></p>
<dd>The &#8220;ftp&#8221; homedirectory should be owned by root.</p>
<dt><code>~ftp/bin </code></p>
<dd>The directory for external programs (such as <a href="/docs/linux/man/1-ls/">ls</a>(1)). These programs must either be statically linked, or you must setup an environment for dynamic linking when running chrooted. These programs will be used if present:</p>
<dl>
<dt><code>ls</code></p>
<dd>Used when listing files.</p>
<dt><code>compress</code></p>
<dd>When retrieving a filename that ends in .Z and that file isn&#8217;t present, will try to find the filename without .Z and compress it on the fly.</p>
<dt><code>gzip</code></p>
<dd>Same as compress, just with files ending in .gz</p>
<dt><code>gtar</code></p>
<dd>Enables retrieval of whole directories as files ending in .tar Can also be combined with compression. You must use GNU Tar (or some other that supports the &#8211;<code>z</code> and &#8211;<code>Z</code> flags).</p>
<dt><code>locate</code></p>
<dd>Will enable &#8220;fast find&#8221; with the <code>SITE FIND</code> command. You must also create a locatedb file in ~ftp/etc</dl>
<dt><code>~ftp/etc </code></p>
<dd>If you put copies of the <a href="/docs/linux/man/5-passwd/">passwd</a>(5) and <a href="/docs/linux/man/5-group/">group</a>(5) files here, ls will be able to produce owner names rather than numbers. Remember to remove any passwords from these files. The file motd if present, will be printed after a successful login.</p>
<dt><code>~ftp/dev </code></p>
<dd>Put a copy of /dev/null7 here.</p>
<dt><code>~ftp/pub </code></p>
<dd>Traditional place to put whatever you want to make public.</dl>
<p> If you want guests to be able to upload files, create a ~ftp/incoming directory owned by &#8220;root&#8221; and group &#8220;ftp&#8221; with mode 730 (make sure &#8220;ftp&#8221; is member of group &#8220;ftp )&#8221; The following restrictions apply to anonymous users: </p>
<ul>
<li> Directories created will have mode 700.
<li> Uploaded files will be created with an umask of 777, if not changed with the &#8211;<code>g</code> option.
<li> These command are not accessible: <code>DELE , RMD , RNTO , RNFR</code> <code>SITE UMASK</code> and <code>SITE CHMOD</code>
<li> Filenames must start with an alpha-numeric character, and consist of alpha-numeric characters or any of the following: <code>+</code> (plus), <code>&#8211;</code> (minus), <code>=</code> (equal), <code>_</code> (underscore), <code>.</code> (period), and <code>,</code> (comma). </ul>
<h2>Files</h2>
<dl>
<dt><code>/etc/ftpusers </code></p>
<dd>Access list for users.</p>
<dt><code>/etc/ftpchroot </code></p>
<dd>List of normal users who should be chroot&#8217;d.</p>
<dt><code>/etc/ftpwelcome </code></p>
<dd>Welcome notice.</p>
<dt><code>/etc/motd </code></p>
<dd>Welcome notice after login.</p>
<dt><code>/etc/nologin </code></p>
<dd>Displayed and access refused.</p>
<dt><code>~/.klogin </code></p>
<dd>Login access for Kerberos.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ftp/">ftp</a>(1), <a href="/docs/linux/man/1-otp/">otp</a>(1), <a href="/docs/linux/man/3-getusershell/">getusershell</a>(3), <a href="/docs/linux/man/5-ftpusers/">ftpusers</a>(5), <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)</p>
<h2>Standards</h2>
<dl>
<dt><code>RFC 959</code></p>
<dd>FTP PROTOCOL SPECIFICATION</p>
<dt><code>RFC 1938</code></p>
<dd>OTP Specification</p>
<dt><code>RFC 2228</code></p>
<dd>FTP Security Extensions.</dl>
<h2>Bugs</h2>
<p>The server must run as the super-user to create sockets with privileged port numbers. It maintains an effective user id of the logged in user, reverting to the super-user only when binding addresses to sockets. The possible security holes have been extensively scrutinized, but are possibly incomplete.</p>
<h2>History</h2>
<p>The command appeared in BSD 4.2</p>
