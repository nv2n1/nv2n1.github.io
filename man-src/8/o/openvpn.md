---
title: "openvpn(8)"
name: "openvpn"
section: "8"
letter: "o"
url: "/docs/linux/man/8-openvpn/"
description: "openvpn – Secure IP tunnel daemon"
---

<p>openvpn &#8211; Secure IP tunnel daemon</p>
<h2>Synopsis</h2>
<pre><code>openvpn</code> [ options ... ]
<code>openvpn</code> <code>--help</code></pre>
<h2>Introduction</h2>
<p>OpenVPN is an open source VPN daemon by James Yonan. Because OpenVPN tries to be a universal VPN tool offering a great deal of flexibility, there are a lot of options on this manual page. If you&#8217;re new to OpenVPN, you might want to skip ahead to the examples section where you will see how to construct simple VPNs on the command line without even needing a configuration file. </p>
<p> Also note that there&#8217;s more documentation and examples on the OpenVPN web site: <i><a rel="nofollow" href="https://openvpn.net/">https://openvpn.net/</a></i> </p>
<p> And if you would like to see a shorter version of this manual, see the openvpn usage message which can be obtained by running <code>openvpn</code> without any parameters.</p>
<h2>Description</h2>
<p>OpenVPN is a robust and highly flexible VPN daemon. OpenVPN supports SSL/TLS security, ethernet bridging, TCP or UDP tunnel transport through proxies or NAT, support for dynamic IP addresses and DHCP, scalability to hundreds or thousands of users, and portability to most major OS platforms. </p>
<p> OpenVPN is tightly bound to the OpenSSL library, and derives much of its crypto capabilities from it. </p>
<p> OpenVPN supports conventional encryption using a pre-shared secret key <code>(Static Key mode)</code> or public key security <code>(SSL/TLS mode)</code> using client &amp; server certificates. OpenVPN also supports non-encrypted TCP/UDP tunnels. </p>
<p> OpenVPN is designed to work with the <code>TUN/TAP</code> virtual networking interface that exists on most platforms. </p>
<p> Overall, OpenVPN aims to offer many of the key features of IPSec but with a relatively lightweight footprint.</p>
<h2>Options</h2>
<p>OpenVPN allows any option to be placed either on the command line or in a configuration file. Though all command line options are preceded by a double-leading-dash (&quot;&#8211;&quot;), this prefix can be removed when an option is placed in a configuration file.</p>
<h3>Generic Options</h3>
<p>This section covers generic options which are accessible regardless of which mode OpenVPN is configured as.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Show options.</p>
<dt><code>&#8211;auth-nocache</code></p>
<dd>Don&#8217;t cache <code>&#8211;askpass</code> or <code>&#8211;auth-user-pass</code> username/passwords in virtual memory. </p>
<p> If specified, this directive will cause OpenVPN to immediately forget username/password inputs after they are used. As a result, when OpenVPN needs a username/password, it will prompt for input from stdin, which may be multiple times during the duration of an OpenVPN session. </p>
<p> When using <code>&#8211;auth-nocache</code> in combination with a user/password file and <code>&#8211;chroot</code> or <code>&#8211;daemon</code>, make sure to use an absolute path. </p>
<p> This directive does not affect the <code>&#8211;http-proxy</code> username/password. It is always cached.</p>
<dt><code>&#8211;cd</code><i>&nbsp;dir</i></p>
<dd>Change directory to <code>dir</code> prior to reading any files such as configuration files, key files, scripts, etc. <code>dir</code> should be an absolute path, with a leading &quot;/&quot;, and without any references to the current directory such as <code>.</code> or <code>..</code>. </p>
<p> This option is useful when you are running OpenVPN in <code>&#8211;daemon</code> mode, and you want to consolidate all of your OpenVPN control files in one location.</p>
<dt><code>&#8211;chroot</code><i>&nbsp;dir</i></p>
<dd>Chroot to <code>dir</code> after initialization. <code>&#8211;chroot</code> essentially redefines <code>dir</code> as being the top level directory tree (/). OpenVPN will therefore be unable to access any files outside this tree. This can be desirable from a security standpoint. </p>
<p> Since the chroot operation is delayed until after initialization, most OpenVPN options that reference files will operate in a pre-chroot context. </p>
<p> In many cases, the <code>dir</code> parameter can point to an empty directory, however complications can result when scripts or restarts are executed after the chroot operation. </p>
<p> Note: The SSL library will probably need /dev/urandom to be available inside the chroot directory <code>dir</code>. This is because SSL libraries occasionally need to collect fresh random. Newer linux kernels and some BSDs implement a getrandom() or getentropy() syscall that removes the need for /dev/urandom to be available.</p>
<dt><code>&#8211;config</code><i>&nbsp;file</i></p>
<dd>Load additional config options from <code>file</code> where each line corresponds to one command line option, but with the leading &#8216;&#8211;&#8216; removed. </p>
<p> If <code>&#8211;config file</code> is the only option to the openvpn command, the <code>&#8211;config</code> can be removed, and the command can be given as <code>openvpn file</code> </p>
<p> Note that configuration files can be nested to a reasonable depth. </p>
<p> Double quotation or single quotation characters (&quot;&quot;, &#8221;) can be used to enclose single parameters containing whitespace, and &quot;#&quot; or &quot;;&quot; characters in the first column can be used to denote comments. </p>
<p> Note that OpenVPN 2.0 and higher performs backslash-based shell escaping for characters not in single quotations, so the following mappings should be observed: </p>
<pre>\ Maps to a single backslash character (\).
\&quot; Pass a literal doublequote character (&quot;), don't
 interpret it as enclosing a parameter.
\[SPACE] Pass a literal space or tab character, don't
 interpret it as a parameter delimiter.</pre>
<p>For example on Windows, use double backslashes to represent pathnames: </p>
<pre>secret &quot;c:\OpenVPN\secret.key&quot;</pre>
<p>For examples of configuration files, see <i><a rel="nofollow" href="https://openvpn.net/community-resources/how-to/">https://openvpn.net/community-resources/how-to/</a></i> </p>
<p> Here is an example configuration file: </p>
<pre>#
# Sample OpenVPN configuration file for
# using a pre-shared static key.
#
# '#' or ';' may be used to delimit comments.
# Use a dynamic tun device.
dev tun
# Our remote peer
remote mypeer.mydomain
# 10.1.0.1 is our local VPN endpoint
# 10.1.0.2 is our remote VPN endpoint
ifconfig 10.1.0.1 10.1.0.2
# Our pre-shared static key
secret static.key</pre>
<dt><code>&#8211;daemon</code><i>&nbsp;progname</i></p>
<dd>Become a daemon after all initialization functions are completed. This option will cause all message and error output to be sent to the syslog file (such as <code>/var/log/messages</code>), except for the output of scripts and ifconfig commands, which will go to <code>/dev/null</code> unless otherwise redirected. The syslog redirection occurs immediately at the point that <code>&#8211;daemon</code> is parsed on the command line even though the daemonization point occurs later. If one of the <code>&#8211;log</code> options is present, it will supersede syslog redirection. </p>
<p> The optional <code>progname</code> parameter will cause OpenVPN to report its program name to the system logger as <code>progname</code>. This can be useful in linking OpenVPN messages in the syslog file with specific tunnels. When unspecified, <code>progname</code> defaults to &quot;openvpn&quot;. </p>
<p> When OpenVPN is run with the <code>&#8211;daemon</code> option, it will try to delay daemonization until the majority of initialization functions which are capable of generating fatal errors are complete. This means that initialization scripts can test the return status of the openvpn command for a fairly reliable indication of whether the command has correctly initialized and entered the packet forwarding event loop. </p>
<p> In OpenVPN, the vast majority of errors which occur after initialization are non-fatal. </p>
<p> Note: as soon as OpenVPN has daemonized, it can not ask for usernames, passwords, or key pass phrases anymore. This has certain consequences, namely that using a password-protected private key will fail unless the <code>&#8211;askpass</code> option is used to tell OpenVPN to ask for the pass phrase (this requirement is new in v2.3.7, and is a consequence of calling daemon() before initializing the crypto layer). </p>
<p> Further, using <code>&#8211;daemon</code> together with <code>&#8211;auth-user-pass</code> (entered on console) and <code>&#8211;auth-nocache</code> will fail as soon as key renegotiation (and reauthentication) occurs.</p>
<dt><code>&#8211;disable-occ</code></p>
<dd>Don&#8217;t output a warning message if option inconsistencies are detected between peers. An example of an option inconsistency would be where one peer uses <code>&#8211;dev tun</code> while the other peer uses <code>&#8211;dev tap</code>. </p>
<p> Use of this option is discouraged, but is provided as a temporary fix in situations where a recent version of OpenVPN must connect to an old version.</p>
<dt><code>&#8211;engine</code><i>&nbsp;engine-name</i></p>
<dd>Enable OpenSSL hardware-based crypto engine functionality. </p>
<p> If <code>engine-name</code> is specified, use a specific crypto engine. Use the <code>&#8211;show-engines</code> standalone option to list the crypto engines which are supported by OpenSSL.</p>
<dt><code>&#8211;fast-io</code></p>
<dd>(Experimental) Optimize TUN/TAP/UDP I/O writes by avoiding a call to poll/epoll/select prior to the write operation. The purpose of such a call would normally be to block until the device or socket is ready to accept the write. Such blocking is unnecessary on some platforms which don&#8217;t support write blocking on UDP sockets or TUN/TAP devices. In such cases, one can optimize the event loop by avoiding the poll/epoll/select call, improving CPU efficiency by 5% to 10%. </p>
<p> This option can only be used on non-Windows systems, when <code>&#8211;proto udp</code> is specified, and when <code>&#8211;shaper</code> is NOT specified.</p>
<dt><code>&#8211;group</code><i>&nbsp;group</i></p>
<dd>Similar to the <code>&#8211;user</code> option, this option changes the group ID of the OpenVPN process to <code>group</code> after initialization.</p>
<dt><code>&#8211;ignore-unknown-option</code><i>&nbsp;args</i></p>
<dd>Valid syntax: </p>
<pre>ignore-unknown-options opt1 opt2 opt3 ... optN</pre>
<p>When one of options <code>opt1 &#8230; optN</code> is encountered in the configuration file the configuration file parsing does not fail if this OpenVPN version does not support the option. Multiple <code>&#8211;ignore-unknown-option</code> options can be given to support a larger number of options to ignore. </p>
<p> This option should be used with caution, as there are good security reasons for having OpenVPN fail if it detects problems in a config file. Having said that, there are valid reasons for wanting new software features to gracefully degrade when encountered by older software versions. </p>
<p> <code>&#8211;ignore-unknown-option</code> is available since OpenVPN 2.3.3.</p>
<dt><code>&#8211;iproute</code><i>&nbsp;cmd</i></p>
<dd>Set alternate command to execute instead of default <code>iproute2</code> command. May be used in order to execute OpenVPN in unprivileged environment.</p>
<dt><code>&#8211;keying-material-exporter</code><i>&nbsp;args</i></p>
<dd>Save Exported Keying Material [RFC5705] of len bytes (must be between 16 and 4095 bytes) using <code>label</code> in environment (<code>exported_keying_material</code>) for use by plugins in <code>OPENVPN_PLUGIN_TLS_FINAL</code> callback. </p>
<p> Valid syntax: </p>
<pre>keying-material-exporter label len</pre>
<p>Note that exporter <code>labels</code> have the potential to collide with existing PRF labels. In order to prevent this, labels <i>MUST</i> begin with <code>EXPORTER</code>.</p>
<dt><code>&#8211;mlock</code></p>
<dd>Disable paging by calling the POSIX mlockall function. Requires that OpenVPN be initially run as root (though OpenVPN can subsequently downgrade its UID using the <code>&#8211;user</code> option). </p>
<p> Using this option ensures that key material and tunnel data are never written to disk due to virtual memory paging operations which occur under most modern operating systems. It ensures that even if an attacker was able to crack the box running OpenVPN, he would not be able to scan the system swap file to recover previously used ephemeral keys, which are used for a period of time governed by the <code>&#8211;reneg</code> options (see below), then are discarded. </p>
<p> The downside of using <code>&#8211;mlock</code> is that it will reduce the amount of physical memory available to other applications. </p>
<p> The limit on how much memory can be locked and how that limit is enforced are OS-dependent. On Linux the default limit that an unprivileged process may lock (RLIMIT_MEMLOCK) is low, and if privileges are dropped later, future memory allocations will very likely fail. The limit can be increased using ulimit or systemd directives depending on how OpenVPN is started.</p>
<dt><code>&#8211;nice</code><i>&nbsp;n</i></p>
<dd>Change process priority after initialization (<code>n</code> greater than 0 is lower priority, <code>n</code> less than zero is higher priority).</p>
<dt><code>&#8211;persist-key</code></p>
<dd>Don&#8217;t re-read key files across <code>SIGUSR1</code> or <code>&#8211;ping-restart</code>. </p>
<p> This option can be combined with <code>&#8211;user nobody</code> to allow restarts triggered by the <code>SIGUSR1</code> signal. Normally if you drop root privileges in OpenVPN, the daemon cannot be restarted since it will now be unable to re-read protected key files. </p>
<p> This option solves the problem by persisting keys across <code>SIGUSR1</code> resets, so they don&#8217;t need to be re-read.</p>
<dt><code>&#8211;remap-usr1</code><i>&nbsp;signal</i></p>
<dd>Control whether internally or externally generated <code>SIGUSR1</code> signals are remapped to <code>SIGHUP</code> (restart without persisting state) or SIGTERM (exit). </p>
<p> <code>signal</code> can be set to <code>SIGHUP</code> or <code>SIGTERM</code>. By default, no remapping occurs.</p>
<dt><code>&#8211;script-security</code><i>&nbsp;level</i></p>
<dd>This directive offers policy-level control over OpenVPN&#8217;s usage of external programs and scripts. Lower <code>level</code> values are more restrictive, higher values are more permissive. Settings for <code>level</code>:</p>
<dt><code>0</code></p>
<dd>Strictly no calling of external programs.</p>
<dt><code>1</code></p>
<dd>(Default) Only call built-in executables such as ifconfig, ip, route, or netsh.</p>
<dt><code>2</code></p>
<dd>Allow calling of built-in executables and user-defined scripts.</p>
<dt><code>3</code></p>
<dd>Allow passwords to be passed to scripts via environmental variables (potentially unsafe). </p>
<p> OpenVPN releases before v2.3 also supported a <code>method</code> flag which indicated how OpenVPN should call external commands and scripts. This could be either <code>execve</code> or <code>system</code>. As of OpenVPN 2.3, this flag is no longer accepted. In most *nix environments the execve() approach has been used without any issues. </p>
<p> Some directives such as <code>&#8211;up</code> allow options to be passed to the external script. In these cases make sure the script name does not contain any spaces or the configuration parser will choke because it can&#8217;t determine where the script name ends and script options start. </p>
<p> To run scripts in Windows in earlier OpenVPN versions you needed to either add a full path to the script interpreter which can parse the script or use the <code>system</code> flag to run these scripts. As of OpenVPN 2.3 it is now a strict requirement to have full path to the script interpreter when running non-executables files. This is not needed for executable files, such as .exe, .com, .bat or .cmd files. For example, if you have a Visual Basic script, you must use this syntax now: </p>
<pre>--up 'C:\Windows\System32\wscript.exe C:\Program\ Files\OpenVPN\config\my-up-script.vbs'</pre>
<p>Please note the single quote marks and the escaping of the backslashes (\) and the space character. </p>
<p> The reason the support for the <code>system</code> flag was removed is due to the security implications with shell expansions when executing scripts via the <code>system()</code> call.</p>
<dt><code>&#8211;setcon</code><i>&nbsp;context</i></p>
<dd>Apply SELinux <code>context</code> after initialization. This essentially provides the ability to restrict OpenVPN&#8217;s rights to only network I/O operations, thanks to SELinux. This goes further than <code>&#8211;user</code> and <code>&#8211;chroot</code> in that those two, while being great security features, unfortunately do not protect against privilege escalation by exploitation of a vulnerable system call. You can of course combine all three, but please note that since setcon requires access to /proc you will have to provide it inside the chroot directory (e.g. with mount &#8211;bind). </p>
<p> Since the setcon operation is delayed until after initialization, OpenVPN can be restricted to just network-related system calls, whereas by applying the context before startup (such as the OpenVPN one provided in the SELinux Reference Policies) you will have to allow many things required only during initialization. </p>
<p> Like with chroot, complications can result when scripts or restarts are executed after the setcon operation, which is why you should really consider using the <code>&#8211;persist-key</code> and <code>&#8211;persist-tun</code> options.</p>
<dt><code>&#8211;status</code><i>&nbsp;args</i></p>
<dd>Write operational status to <code>file</code> every <code>n</code> seconds. </p>
<p> Valid syntaxes: </p>
<pre>status file
status file n</pre>
<p>Status can also be written to the syslog by sending a <code>SIGUSR2</code> signal. </p>
<p> With multi-client capability enabled on a server, the status file includes a list of clients and a routing table. The output format can be controlled by the <code>&#8211;status-version</code> option in that case. </p>
<p> For clients or instances running in point-to-point mode, it will contain the traffic statistics.</p>
<dt><code>&#8211;status-version</code><i>&nbsp;n</i></p>
<dd>Set the status file format version number to <code>n</code>. </p>
<p> This only affects the status file on servers with multi-client capability enabled. Valid status version values:</p>
<dt><code>1</code></p>
<dd>Traditional format (default). The client list contains the following fields comma-separated: Common Name, Real Address, Bytes Received, Bytes Sent, Connected Since.</p>
<dt><code>2</code></p>
<dd>A more reliable format for external processing. Compared to version <code>1</code>, the client list contains some additional fields: Virtual Address, Virtual IPv6 Address, Username, Client ID, Peer ID, Data Channel Cipher. Future versions may extend the number of fields.</p>
<dt><code>3</code></p>
<dd>Identical to <code>2</code>, but fields are tab-separated.</p>
<dt><code>&#8211;test-crypto</code></p>
<dd>Do a self-test of OpenVPN&#8217;s crypto options by encrypting and decrypting test packets using the data channel encryption options specified above. This option does not require a peer to function, and therefore can be specified without <code>&#8211;dev</code> or <code>&#8211;remote</code>. </p>
<p> The typical usage of <code>&#8211;test-crypto</code> would be something like this: </p>
<pre>openvpn --test-crypto --secret key</pre>
<p>or </p>
<pre>openvpn --test-crypto --secret key --verb 9</pre>
<p>This option is very useful to test OpenVPN after it has been ported to a new platform, or to isolate problems in the compiler, OpenSSL crypto library, or OpenVPN&#8217;s crypto code. Since it is a self-test mode, problems with encryption and authentication can be debugged independently of network and tunnel issues.</p>
<dt><code>&#8211;tmp-dir</code><i>&nbsp;dir</i></p>
<dd>Specify a directory <code>dir</code> for temporary files. This directory will be used by openvpn processes and script to communicate temporary data with openvpn main process. Note that the directory must be writable by the OpenVPN process after it has dropped it&#8217;s root privileges. </p>
<p> This directory will be used by in the following cases:</p>
<dt>&bull;</p>
<dd><code>&#8211;client-connect</code> scripts and <code>OPENVPN_PLUGIN_CLIENT_CONNECT</code> plug-in hook to dynamically generate client-specific configuration <code>client_connect_config_file</code> and return success/failure via <code>client_connect_deferred_file</code> when using deferred client connect method</p>
<dt>&bull;</p>
<dd><code>OPENVPN_PLUGIN_AUTH_USER_PASS_VERIFY</code> plug-in hooks returns success/failure via <code>auth_control_file</code> when using deferred auth method</p>
<dt>&bull;</p>
<dd><code>OPENVPN_PLUGIN_ENABLE_PF</code> plugin hook to pass filtering rules via <code>pf_file</code></p>
<dt><code>&#8211;use-prediction-resistance</code></p>
<dd>Enable prediction resistance on mbed TLS&#8217;s RNG. </p>
<p> Enabling prediction resistance causes the RNG to reseed in each call for random. Reseeding this often can quickly deplete the kernel entropy pool. </p>
<p> If you need this option, please consider running a daemon that adds entropy to the kernel pool.</p>
<dt><code>&#8211;user</code><i>&nbsp;user</i></p>
<dd>Change the user ID of the OpenVPN process to <code>user</code> after initialization, dropping privileges in the process. This option is useful to protect the system in the event that some hostile party was able to gain control of an OpenVPN session. Though OpenVPN&#8217;s security features make this unlikely, it is provided as a second line of defense. </p>
<p> By setting <code>user</code> to <code>nobody</code> or somebody similarly unprivileged, the hostile party would be limited in what damage they could cause. Of course once you take away privileges, you cannot return them to an OpenVPN session. This means, for example, that if you want to reset an OpenVPN daemon with a <code>SIGUSR1</code> signal (for example in response to a DHCP reset), you should make use of one or more of the <code>&#8211;persist</code> options to ensure that OpenVPN doesn&#8217;t need to execute any privileged operations in order to restart (such as re-reading key files or running <code>ifconfig</code> on the TUN device).</p>
<dt><code>&#8211;writepid</code><i>&nbsp;file</i></p>
<dd>Write OpenVPN&#8217;s main process ID to <code>file</code>.</dl>
<h3>Log options</h3>
<dl>
<dt><code>&#8211;echo</code><i>&nbsp;parms</i></p>
<dd>Echo <code>parms</code> to log output. </p>
<p> Designed to be used to send messages to a controlling application which is receiving the OpenVPN log output.</p>
<dt><code>&#8211;errors-to-stderr</code></p>
<dd>Output errors to stderr instead of stdout unless log output is redirected by one of the <code>&#8211;log</code> options.</p>
<dt><code>&#8211;log</code><i>&nbsp;file</i></p>
<dd>Output logging messages to <code>file</code>, including output to stdout/stderr which is generated by called scripts. If <code>file</code> already exists it will be truncated. This option takes effect immediately when it is parsed in the command line and will supersede syslog output if <code>&#8211;daemon</code> or <code>&#8211;inetd</code> is also specified. This option is persistent over the entire course of an OpenVPN instantiation and will not be reset by <code>SIGHUP</code>, <code>SIGUSR1</code>, or <code>&#8211;ping-restart</code>. </p>
<p> Note that on Windows, when OpenVPN is started as a service, logging occurs by default without the need to specify this option.</p>
<dt><code>&#8211;log-append</code><i>&nbsp;file</i></p>
<dd>Append logging messages to <code>file</code>. If <code>file</code> does not exist, it will be created. This option behaves exactly like <code>&#8211;log</code> except that it appends to rather than truncating the log file.</p>
<dt><code>&#8211;machine-readable-output</code></p>
<dd>Always write timestamps and message flags to log messages, even when they otherwise would not be prefixed. In particular, this applies to log messages sent to stdout.</p>
<dt><code>&#8211;mute</code><i>&nbsp;n</i></p>
<dd>Log at most <code>n</code> consecutive messages in the same category. This is useful to limit repetitive logging of similar message types.</p>
<dt><code>&#8211;mute-replay-warnings</code></p>
<dd>Silence the output of replay warnings, which are a common false alarm on WiFi networks. This option preserves the security of the replay protection code without the verbosity associated with warnings about duplicate packets.</p>
<dt><code>&#8211;suppress-timestamps</code></p>
<dd>Avoid writing timestamps to log messages, even when they otherwise would be prepended. In particular, this applies to log messages sent to stdout.</p>
<dt><code>&#8211;syslog</code><i>&nbsp;progname</i></p>
<dd>Direct log output to system logger, but do not become a daemon. See <code>&#8211;daemon</code> directive above for description of <code>progname</code> parameter.</p>
<dt><code>&#8211;verb</code><i>&nbsp;n</i></p>
<dd>Set output verbosity to <code>n</code> (default <code>1</code>). Each level shows all info from the previous levels. Level <code>3</code> is recommended if you want a good summary of what&#8217;s happening without being swamped by output.</p>
<dt><code>0</code></p>
<dd>No output except fatal errors.</p>
<dt><code>1</code> to <code>4</code></p>
<dd>Normal usage range.</p>
<dt><code>5</code></p>
<dd>Outputs <code>R</code> and <code>W</code> characters to the console for each packet read and write, uppercase is used for TCP/UDP packets and lowercase is used for TUN/TAP packets.</p>
<dt><code>6</code> to <code>11</code></p>
<dd>Debug info range (see <code>errlevel.h</code> in the source code for additional information on debug levels).</dl>
<h3>Protocol options</h3>
<p>Options in this section affect features available in the OpenVPN wire protocol. Many of these options also define the encryption options of the data channel in the OpenVPN wire protocol. These options must be configured in a compatible way between both the local and remote side.</p>
<dl>
<dt><code>&#8211;allow-compression</code><i>&nbsp;mode</i></p>
<dd>As described in the <code>&#8211;compress</code> option, compression is a potentially dangerous option. This option allows controlling the behaviour of OpenVPN when compression is used and allowed. </p>
<p> Valid syntaxes: </p>
<pre>allow-compression
allow-compression mode</pre>
<p>The <code>mode</code> argument can be one of the following values:</p>
<dt><code>asym</code> (default)</p>
<dd>OpenVPN will only <i>decompress downlink packets</i> but <i>not compress uplink packets</i>. This also allows migrating to disable compression when changing both server and client configurations to remove compression at the same time is not a feasible option.</p>
<dt><code>no</code></p>
<dd>OpenVPN will refuse any non-stub compression.</p>
<dt><code>yes</code></p>
<dd>OpenVPN will send and receive compressed packets.</p>
<dt><code>&#8211;auth</code><i>&nbsp;alg</i></p>
<dd>Authenticate data channel packets and (if enabled) <code>tls-auth</code> control channel packets with HMAC using message digest algorithm <code>alg</code>. (The default is <code>SHA1</code> ). HMAC is a commonly used message authentication algorithm (MAC) that uses a data string, a secure hash algorithm and a key to produce a digital signature. </p>
<p> The OpenVPN data channel protocol uses encrypt-then-mac (i.e. first encrypt a packet then HMAC the resulting ciphertext), which prevents padding oracle attacks. </p>
<p> If an AEAD cipher mode (e.g. GCM) is chosen then the specified <code>&#8211;auth</code> algorithm is ignored for the data channel and the authentication method of the AEAD cipher is used instead. Note that <code>alg</code> still specifies the digest used for <code>tls-auth</code>. </p>
<p> In static-key encryption mode, the HMAC key is included in the key file generated by <code>&#8211;genkey</code>. In TLS mode, the HMAC key is dynamically generated and shared between peers via the TLS control channel. If OpenVPN receives a packet with a bad HMAC it will drop the packet. HMAC usually adds 16 or 20 bytes per packet. Set <code>alg=none</code> to disable authentication. </p>
<p> For more information on HMAC see <i><a rel="nofollow" href="http://www.cs.ucsd.edu/users/mihir/papers/hmac.html">http://www.cs.ucsd.edu/users/mihir/papers/hmac.html</a></i></p>
<dt><code>&#8211;cipher</code><i>&nbsp;alg</i></p>
<dd>This option is deprecated for server-client mode. <code>&#8211;data-ciphers</code> or possibly <i>&#8211;data-ciphers-fallback`</i> should be used instead. </p>
<p> Encrypt data channel packets with cipher algorithm <code>alg</code>. </p>
<p> The default is <code>BF-CBC</code>, an abbreviation for Blowfish in Cipher Block Chaining mode. When cipher negotiation (NCP) is allowed, OpenVPN 2.4 and newer on both client and server side will automatically upgrade to <code>AES-256-GCM</code>. See <code>&#8211;data-ciphers</code> and <code>&#8211;ncp-disable</code> for more details on NCP. </p>
<p> Using <code>BF-CBC</code> is no longer recommended, because of its 64-bit block size. This small block size allows attacks based on collisions, as demonstrated by SWEET32. See <i><a rel="nofollow" href="https://community.openvpn.net/openvpn/wiki/SWEET32">https://community.openvpn.net/openvpn/wiki/SWEET32</a></i> for details. Due to this, support for <code>BF-CBC</code>, <code>DES</code>, <code>CAST5</code>, <code>IDEA</code> and <code>RC2</code> ciphers will be removed in OpenVPN 2.6. </p>
<p> To see other ciphers that are available with OpenVPN, use the <code>&#8211;show-ciphers</code> option. </p>
<p> Set <code>alg</code> to <code>none</code> to disable encryption.</p>
<dt><code>&#8211;compress</code><i>&nbsp;algorithm</i></p>
<dd><code>DEPRECATED</code> Enable a compression algorithm. Compression is generally not recommended. VPN tunnels which use compression are susceptible to the VORALCE attack vector. </p>
<p> The <code>algorithm</code> parameter may be <code>lzo</code>, <code>lz4</code>, <code>lz4-v2</code>, <code>stub</code>, <code>stub-v2</code> or empty. LZO and LZ4 are different compression algorithms, with LZ4 generally offering the best performance with least CPU usage. </p>
<p> The <code>lz4-v2</code> and <code>stub-v2</code> variants implement a better framing that does not add overhead when packets cannot be compressed. All other variants always add one extra framing byte compared to no compression framing. </p>
<p> If the <code>algorithm</code> parameter is <code>stub</code>, <code>stub-v2</code> or empty, compression will be turned off, but the packet framing for compression will still be enabled, allowing a different setting to be pushed later. Additionally, <code>stub</code> and <code>stub-v2</code> wil disable announcing <code>lzo</code> and <code>lz4</code> compression support via <i>IV_</i> variables to the server. </p>
<p> Note: the <code>stub</code> (or empty) option is NOT compatible with the older option <code>&#8211;comp-lzo no</code>. </p>
<p> <code>*Security Considerations*</code> </p>
<p> Compression and encryption is a tricky combination. If an attacker knows or is able to control (parts of) the plain-text of packets that contain secrets, the attacker might be able to extract the secret if compression is enabled. See e.g. the <i>CRIME</i> and <i>BREACH</i> attacks on TLS and <i>VORACLE</i> on VPNs which also leverage to break encryption. If you are not entirely sure that the above does not apply to your traffic, you are advised to <i>not</i> enable compression.</p>
<dt><code>&#8211;comp-lzo</code><i>&nbsp;mode</i></p>
<dd><code>DEPRECATED</code> Enable LZO compression algorithm. Compression is generally not recommended. VPN tunnels which uses compression are suspectible to the VORALCE attack vector. </p>
<p> Use LZO compression &#8212; may add up to 1 byte per packet for incompressible data. <code>mode</code> may be <code>yes</code>, <code>no</code>, or <code>adaptive</code> (default). </p>
<p> In a server mode setup, it is possible to selectively turn compression on or off for individual clients. </p>
<p> First, make sure the client-side config file enables selective compression by having at least one <code>&#8211;comp-lzo</code> directive, such as <code>&#8211;comp-lzo no</code>. This will turn off compression by default, but allow a future directive push from the server to dynamically change the <code>on</code>/<code>off</code>/<code>adaptive</code> setting. </p>
<p> Next in a <code>&#8211;client-config-dir</code> file, specify the compression setting for the client, for example: </p>
<pre>comp-lzo yes
push &quot;comp-lzo yes&quot;</pre>
<p>The first line sets the <code>comp-lzo</code> setting for the server side of the link, the second sets the client side.</p>
<dt><code>&#8211;comp-noadapt</code></p>
<dd><code>DEPRECATED</code> When used in conjunction with <code>&#8211;comp-lzo</code>, this option will disable OpenVPN&#8217;s adaptive compression algorithm. Normally, adaptive compression is enabled with <code>&#8211;comp-lzo</code>. </p>
<p> Adaptive compression tries to optimize the case where you have compression enabled, but you are sending predominantly incompressible (or pre-compressed) packets over the tunnel, such as an FTP or rsync transfer of a large, compressed file. With adaptive compression, OpenVPN will periodically sample the compression process to measure its efficiency. If the data being sent over the tunnel is already compressed, the compression efficiency will be very low, triggering openvpn to disable compression for a period of time until the next re-sample test.</p>
<dt><code>&#8211;key-direction</code></p>
<dd>Alternative way of specifying the optional direction parameter for the <code>&#8211;tls-auth</code> and <code>&#8211;secret</code> options. Useful when using inline files (See section on inline files).</p>
<dt><code>&#8211;keysize</code><i>&nbsp;n</i></p>
<dd><code>DEPRECATED</code> This option will be removed in OpenVPN 2.6. </p>
<p> Size of cipher key in bits (optional). If unspecified, defaults to cipher-specific default. The <code>&#8211;show-ciphers</code> option (see below) shows all available OpenSSL ciphers, their default key sizes, and whether the key size can be changed. Use care in changing a cipher&#8217;s default key size. Many ciphers have not been extensively cryptanalyzed with non-standard key lengths, and a larger key may offer no real guarantee of greater security, or may even reduce security.</p>
<dt><code>&#8211;data-ciphers</code><i>&nbsp;cipher-list</i></p>
<dd>Restrict the allowed ciphers to be negotiated to the ciphers in <code>cipher-list</code>. <code>cipher-list</code> is a colon-separated list of ciphers, and defaults to <code>AES-256-GCM:AES-128-GCM</code>. </p>
<p> For servers, the first cipher from <code>cipher-list</code> that is also supported by the client will be pushed to clients that support cipher negotiation. </p>
<p> Cipher negotiation is enabled in client-server mode only. I.e. if <code>&#8211;mode</code> is set to &#8216;server&#8217; (server-side, implied by setting <code>&#8211;server</code> ), or if <code>&#8211;pull</code> is specified (client-side, implied by setting &#8211;client). </p>
<p> If no common cipher is found during cipher negotiation, the connection is terminated. To support old clients/old servers that do not provide any cipher negotiation support see <code>&#8211;data-ciphers-fallback</code>. </p>
<p> Additionally, to allow for more smooth transition, if NCP is enabled, OpenVPN will inherit the cipher of the peer if that cipher is different from the local <code>&#8211;cipher</code> setting, but the peer cipher is one of the ciphers specified in <code>&#8211;data-ciphers</code>. E.g. a non-NCP client (&lt;=v2.3, or with &#8211;ncp-disabled set) connecting to a NCP server (v2.4+) with <code>&#8211;cipher BF-CBC</code> and <code>&#8211;data-ciphers AES-256-GCM:AES-256-CBC</code> set can either specify <code>&#8211;cipher BF-CBC</code> or <code>&#8211;cipher AES-256-CBC</code> and both will work. </p>
<p> Note for using NCP with an OpenVPN 2.4 peer: This list must include the <code>AES-256-GCM</code> and <code>AES-128-GCM</code> ciphers. </p>
<p> This list is restricted to be 127 chars long after conversion to OpenVPN ciphers. </p>
<p> This option was called <code>&#8211;ncp-ciphers</code> in OpenVPN 2.4 but has been renamed to <code>&#8211;data-ciphers</code> in OpenVPN 2.5 to more accurately reflect its meaning.</p>
<dt><code>&#8211;data-ciphers-fallback</code><i>&nbsp;alg</i></p>
<dd>Configure a cipher that is used to fall back to if we could not determine which cipher the peer is willing to use. </p>
<p> This option should only be needed to connect to peers that are running OpenVPN 2.3 and older version, and have been configured with <i>&#8211;enable-small</i> (typically used on routers or other embedded devices).</p>
<dt><code>&#8211;ncp-disable</code></p>
<dd><code>DEPRECATED</code> Disable &quot;Negotiable Crypto Parameters&quot;. This completely disables cipher negotiation.</p>
<dt><code>&#8211;secret</code><i>&nbsp;args</i></p>
<dd>Enable Static Key encryption mode (non-TLS). Use pre-shared secret <code>file</code> which was generated with <code>&#8211;genkey</code>. </p>
<p> Valid syntaxes: </p>
<pre>secret file
secret file direction</pre>
<p>The optional <code>direction</code> parameter enables the use of 4 distinct keys (HMAC-send, cipher-encrypt, HMAC-receive, cipher-decrypt), so that each data flow direction has a different set of HMAC and cipher keys. This has a number of desirable security properties including eliminating certain kinds of DoS and message replay attacks. </p>
<p> When the <code>direction</code> parameter is omitted, 2 keys are used bidirectionally, one for HMAC and the other for encryption/decryption. </p>
<p> The <code>direction</code> parameter should always be complementary on either side of the connection, i.e. one side should use <code>0</code> and the other should use <code>1</code>, or both sides should omit it altogether. </p>
<p> The <code>direction</code> parameter requires that <code>file</code> contains a 2048 bit key. While pre-1.5 versions of OpenVPN generate 1024 bit key files, any version of OpenVPN which supports the <code>direction</code> parameter, will also support 2048 bit key file generation using the <code>&#8211;genkey</code> option. </p>
<p> Static key encryption mode has certain advantages, the primary being ease of configuration. </p>
<p> There are no certificates or certificate authorities or complicated negotiation handshakes and protocols. The only requirement is that you have a pre-existing secure channel with your peer (such as <code>ssh</code>) to initially copy the key. This requirement, along with the fact that your key never changes unless you manually generate a new one, makes it somewhat less secure than TLS mode (see below). If an attacker manages to steal your key, everything that was ever encrypted with it is compromised. Contrast that to the perfect forward secrecy features of TLS mode (using Diffie Hellman key exchange), where even if an attacker was able to steal your private key, he would gain no information to help him decrypt past sessions. </p>
<p> Another advantageous aspect of Static Key encryption mode is that it is a handshake-free protocol without any distinguishing signature or feature (such as a header or protocol handshake sequence) that would mark the ciphertext packets as being generated by OpenVPN. Anyone eavesdropping on the wire would see nothing but random-looking data.</p>
<dt><code>&#8211;tran-window</code><i>&nbsp;n</i></p>
<dd>Transition window &#8212; our old key can live this many seconds after a new a key renegotiation begins (default <code>3600</code> seconds). This feature allows for a graceful transition from old to new key, and removes the key renegotiation sequence from the critical path of tunnel data forwarding.</dl>
<h3>Client Options</h3>
<p>The client options are used when connecting to an OpenVPN server configured to use <code>&#8211;server</code>, <code>&#8211;server-bridge</code>, or <code>&#8211;mode server</code> in its configuration.</p>
<dl>
<dt><code>&#8211;allow-pull-fqdn</code></p>
<dd>Allow client to pull DNS names from server (rather than being limited to IP address) for <code>&#8211;ifconfig</code>, <code>&#8211;route</code>, and <code>&#8211;route-gateway</code>.</p>
<dt><code>&#8211;allow-recursive-routing</code></p>
<dd>When this option is set, OpenVPN will not drop incoming tun packets with same destination as host.</p>
<dt><code>&#8211;auth-token</code><i>&nbsp;token</i></p>
<dd>This is not an option to be used directly in any configuration files, but rather push this option from a <code>&#8211;client-connect</code> script or a <code>&#8211;plugin</code> which hooks into the <code>OPENVPN_PLUGIN_CLIENT_CONNECT</code> or <code>OPENVPN_PLUGIN_CLIENT_CONNECT_V2</code> calls. This option provides a possibility to replace the clients password with an authentication token during the lifetime of the OpenVPN client. </p>
<p> Whenever the connection is renegotiated and the <code>&#8211;auth-user-pass-verify</code> script or <code>&#8211;plugin</code> making use of the <code>OPENVPN_PLUGIN_AUTH_USER_PASS_VERIFY</code> hook is triggered, it will pass over this token as the password instead of the password the user provided. The authentication token can only be reset by a full reconnect where the server can push new options to the client. The password the user entered is never preserved once an authentication token has been set. If the OpenVPN server side rejects the authentication token then the client will receive an <code>AUTH_FAILED</code> and disconnect. </p>
<p> The purpose of this is to enable two factor authentication methods, such as HOTP or TOTP, to be used without needing to retrieve a new OTP code each time the connection is renegotiated. Another use case is to cache authentication data on the client without needing to have the users password cached in memory during the life time of the session. </p>
<p> To make use of this feature, the <code>&#8211;client-connect</code> script or <code>&#8211;plugin</code> needs to put </p>
<pre>push &quot;auth-token UNIQUE_TOKEN_VALUE&quot;</pre>
<p>into the file/buffer for dynamic configuration data. This will then make the OpenVPN server to push this value to the client, which replaces the local password with the <code>UNIQUE_TOKEN_VALUE</code>. </p>
<p> Newer clients (2.4.7+) will fall back to the original password method after a failed auth. Older clients will keep using the token value and react according to <code>&#8211;auth-retry</code></p>
<dt><code>&#8211;auth-token-user</code><i>&nbsp;base64username</i></p>
<dd>Companion option to <code>&#8211;auth-token</code>. This options allows to override the username used by the client when reauthenticating with the <code>auth-token</code>. It also allows to use <code>&#8211;auth-token</code> in setups that normally do not use username and password. </p>
<p> The username has to be base64 encoded.</p>
<dt><code>&#8211;auth-user-pass</code></p>
<dd>Authenticate with server using username/password. </p>
<p> Valid syntaxes: </p>
<pre>auth-user-pass
auth-user-pass up</pre>
<p>If <code>up</code> is present, it must be a file containing username/password on 2 lines. If the password line is missing, OpenVPN will prompt for one. </p>
<p> If <code>up</code> is omitted, username/password will be prompted from the console. </p>
<p> The server configuration must specify an <code>&#8211;auth-user-pass-verify</code> script to verify the username/password provided by the client.</p>
<dt><code>&#8211;auth-retry</code><i>&nbsp;type</i></p>
<dd>Controls how OpenVPN responds to username/password verification errors such as the client-side response to an <code>AUTH_FAILED</code> message from the server or verification failure of the private key password. </p>
<p> Normally used to prevent auth errors from being fatal on the client side, and to permit username/password requeries in case of error. </p>
<p> An <code>AUTH_FAILED</code> message is generated by the server if the client fails <code>&#8211;auth-user-pass</code> authentication, or if the server-side <code>&#8211;client-connect</code> script returns an error status when the client tries to connect. </p>
<p> <code>type</code> can be one of:</p>
<dt><code>none</code></p>
<dd>Client will exit with a fatal error (this is the default).</p>
<dt><code>nointeract</code></p>
<dd>Client will retry the connection without requerying for an <code>&#8211;auth-user-pass</code> username/password. Use this option for unattended clients.</p>
<dt><code>interact</code></p>
<dd>Client will requery for an <code>&#8211;auth-user-pass</code> username/password and/or private key password before attempting a reconnection. </p>
<p> Note that while this option cannot be pushed, it can be controlled from the management interface.</p>
<dt><code>&#8211;client</code></p>
<dd>A helper directive designed to simplify the configuration of OpenVPN&#8217;s client mode. This directive is equivalent to: </p>
<pre>pull
tls-client</pre>
<dt><code>&#8211;client-nat</code><i>&nbsp;args</i></p>
<dd>This pushable client option sets up a stateless one-to-one NAT rule on packet addresses (not ports), and is useful in cases where routes or ifconfig settings pushed to the client would create an IP numbering conflict. </p>
<p> Examples: </p>
<pre>client-nat snat 192.168.0.0/255.255.0.0
client-nat dnat 10.64.0.0/255.255.0.0</pre>
<p><code>network/netmask</code> (for example <code>192.168.0.0/255.255.0.0</code>) defines the local view of a resource from the client perspective, while <code>alias/netmask</code> (for example <code>10.64.0.0/255.255.0.0</code>) defines the remote view from the server perspective. </p>
<p> Use <code>snat</code> (source NAT) for resources owned by the client and <code>dnat</code> (destination NAT) for remote resources. </p>
<p> Set <code>&#8211;verb 6</code> for debugging info showing the transformation of src/dest addresses in packets.</p>
<dt><code>&#8211;connect-retry</code><i>&nbsp;n</i></p>
<dd>Wait <code>n</code> seconds between connection attempts (default <code>5</code>). Repeated reconnection attempts are slowed down after 5 retries per remote by doubling the wait time after each unsuccessful attempt. An optional argument <code>max</code> specifies the maximum value of wait time in seconds at which it gets capped (default <code>300</code>).</p>
<dt><code>&#8211;connect-retry-max</code><i>&nbsp;n</i></p>
<dd><code>n</code> specifies the number of times each <code>&#8211;remote</code> or <code>&lt;connection&gt;</code> entry is tried. Specifying <code>n</code> as <code>1</code> would try each entry exactly once. A successful connection resets the counter. (default <i>unlimited</i>).</p>
<dt><code>&#8211;connect-timeout</code><i>&nbsp;n</i></p>
<dd>See <code>&#8211;server-poll-timeout</code>.</p>
<dt><code>&#8211;explicit-exit-notify</code><i>&nbsp;n</i></p>
<dd>In UDP client mode or point-to-point mode, send server/peer an exit notification if tunnel is restarted or OpenVPN process is exited. In client mode, on exit/restart, this option will tell the server to immediately close its client instance object rather than waiting for a timeout. </p>
<p> The <code>n</code> parameter (default <code>1</code> if not present) controls the maximum number of attempts that the client will try to resend the exit notification message. </p>
<p> In UDP server mode, send <code>RESTART</code> control channel command to connected clients. The <code>n</code> parameter (default <code>1</code> if not present) controls client behavior. With <code>n</code> = <code>1</code> client will attempt to reconnect to the same server, with <code>n</code> = <code>2</code> client will advance to the next server. </p>
<p> OpenVPN will not send any exit notifications unless this option is enabled.</p>
<dt><code>&#8211;inactive</code><i>&nbsp;args</i></p>
<dd>Causes OpenVPN to exit after <code>n</code> seconds of inactivity on the TUN/TAP device. The time length of inactivity is measured since the last incoming or outgoing tunnel packet. The default value is 0 seconds, which disables this feature. </p>
<p> Valid syntaxes: </p>
<pre>inactive n
inactive n bytes</pre>
<p>If the optional <code>bytes</code> parameter is included, exit if less than <code>bytes</code> of combined in/out traffic are produced on the tun/tap device in <code>n</code> seconds. </p>
<p> In any case, OpenVPN&#8217;s internal ping packets (which are just keepalives) and TLS control packets are not considered &quot;activity&quot;, nor are they counted as traffic, as they are used internally by OpenVPN and are not an indication of actual user activity.</p>
<dt><code>&#8211;proto-force</code><i>&nbsp;p</i></p>
<dd>When iterating through connection profiles, only consider profiles using protocol <code>p</code> (<code>tcp</code> | <code>udp</code>).</p>
<dt><code>&#8211;pull</code></p>
<dd>This option must be used on a client which is connecting to a multi-client server. It indicates to OpenVPN that it should accept options pushed by the server, provided they are part of the legal set of pushable options (note that the <code>&#8211;pull</code> option is implied by <code>&#8211;client</code> ). </p>
<p> In particular, <code>&#8211;pull</code> allows the server to push routes to the client, so you should not use <code>&#8211;pull</code> or <code>&#8211;client</code> in situations where you don&#8217;t trust the server to have control over the client&#8217;s routing table.</p>
<dt><code>&#8211;pull-filter</code><i>&nbsp;args</i></p>
<dd>Filter options on the client pushed by the server to the client. </p>
<p> Valid syntaxes: </p>
<pre>pull-filter accept text
pull-filter ignore text
pull-filter reject text</pre>
<p>Filter options received from the server if the option starts with <code>text</code>. The action flag <code>accept</code> allows the option, <code>ignore</code> removes it and <code>reject</code> flags an error and triggers a <code>SIGUSR1</code> restart. The filters may be specified multiple times, and each filter is applied in the order it is specified. The filtering of each option stops as soon as a match is found. Unmatched options are accepted by default. </p>
<p> Prefix comparison is used to match <code>text</code> against the received option so that </p>
<pre>pull-filter ignore &quot;route&quot;</pre>
<p>would remove all pushed options starting with <code>route</code> which would include, for example, <code>route-gateway</code>. Enclose <i>text</i> in quotes to embed spaces. </p>
<pre>pull-filter accept &quot;route 192.168.1.&quot;
pull-filter ignore &quot;route &quot;</pre>
<p>would remove all routes that do not start with <code>192.168.1</code>. </p>
<p> <i>Note</i> that <code>reject</code> may result in a repeated cycle of failure and reconnect, unless multiple remotes are specified and connection to the next remote succeeds. To silently ignore an option pushed by the server, use <code>ignore</code>.</p>
<dt><code>&#8211;push-peer-info</code></p>
<dd>Push additional information about the client to server. The following data is always pushed to the server:</p>
<dt><code>IV_VER=&lt;version&gt;</code></p>
<dd>The client OpenVPN version</p>
<dt><code>IV_PLAT=[linux|solaris|openbsd|mac|netbsd|freebsd|win]</code></p>
<dd>The client OS platform</p>
<dt><code>IV_LZO_STUB=1</code></p>
<dd>If client was built with LZO stub capability</p>
<dt><code>IV_LZ4=1</code></p>
<dd>If the client supports LZ4 compressions.</p>
<dt><code>IV_PROTO</code></p>
<dd>Details about protocol extensions that the peer supports. The variable is a bitfield and the bits are defined as follows (starting a bit 0 for the first (unused) bit:</p>
<dt>&bull;</p>
<dd>bit 1: The peer supports peer-id floating mechanism</p>
<dt>&bull;</p>
<dd>bit 2: The client expects a push-reply and the server may send this reply without waiting for a push-request first.</p>
<dt>&bull;</p>
<dd>bit 3: The client is capable of doing key derivation using RFC5705 key material exporter.</p>
<dt>&bull;</p>
<dd>bit 4: The client is capable of accepting additional arguments to the <i>AUTH_PENDING</i> message.</p>
<dt><code>IV_NCP=2</code></p>
<dd>Negotiable ciphers, client supports <code>&#8211;cipher</code> pushed by the server, a value of 2 or greater indicates client supports <i>AES-GCM-128</i> and <i>AES-GCM-256</i>.</p>
<dt><code>IV_CIPHERS=&lt;ncp-ciphers&gt;</code></p>
<dd>The client announces the list of supported ciphers configured with the <code>&#8211;data-ciphers</code> option to the server.</p>
<dt><code>IV_GUI_VER=&lt;gui_id&gt; &lt;version&gt;</code></p>
<dd>The UI version of a UI if one is running, for example <code>de.blinkt.openvpn 0.5.47</code> for the Android app.</p>
<dt><code>IV_SSO=[crtext,][openurl,][proxy_url]</code></p>
<dd>Additional authentication methods supported by the client. This may be set by the client UI/GUI using <code>&#8211;setenv</code> </p>
<p> When <code>&#8211;push-peer-info</code> is enabled the additional information consists of the following data:</p>
<dt><code>IV_HWADDR=&lt;string&gt;</code></p>
<dd>This is intended to be a unique and persistent ID of the client. The string value can be any readable ASCII string up to 64 bytes. OpenVPN 2.x and some other implementations use the MAC address of the client&#8217;s interface used to reach the default gateway. If this string is generated by the client, it should be consistent and preserved across independent session and preferably re-installations and upgrades.</p>
<dt><code>IV_SSL=&lt;version string&gt;</code></p>
<dd>The ssl version used by the client, e.g. <code>OpenSSL 1.0.2f 28 Jan 2016</code>.</p>
<dt><code>IV_PLAT_VER=x.y</code></p>
<dd>The version of the operating system, e.g. 6.1 for Windows 7.</p>
<dt><code>UV_&lt;name&gt;=&lt;value&gt;</code></p>
<dd>Client environment variables whose names start with <code>UV_</code></p>
<dt><code>&#8211;remote</code><i>&nbsp;args</i></p>
<dd>Remote host name or IP address, port and protocol. </p>
<p> Valid syntaxes: </p>
<pre>remote host
remote host port
remote host port proto</pre>
<p>The <code>port</code> and <code>proto</code> arguments are optional. The OpenVPN client will try to connect to a server at <code>host:port</code>. The <code>proto</code> argument indicates the protocol to use when connecting with the remote, and may be <code>tcp</code> or <code>udp</code>. To enforce IPv4 or IPv6 connections add a <code>4</code> or <code>6</code> suffix; like <code>udp4</code> / <code>udp6</code> / <code>tcp4</code> / <code>tcp6</code>. </p>
<p> On the client, multiple <code>&#8211;remote</code> options may be specified for redundancy, each referring to a different OpenVPN server, in the order specified by the list of <code>&#8211;remote</code> options. Specifying multiple <code>&#8211;remote</code> options for this purpose is a special case of the more general connection-profile feature. See the <code>&lt;connection&gt;</code> documentation below. </p>
<p> The client will move on to the next host in the list, in the event of connection failure. Note that at any given time, the OpenVPN client will at most be connected to one server. </p>
<p> Examples: </p>
<pre>remote server1.example.net
remote server1.example.net 1194
remote server2.example.net 1194 tcp</pre>
<dt><i>Note:</i></p>
<dd>Since UDP is connectionless, connection failure is defined by the <code>&#8211;ping</code> and <code>&#8211;ping-restart</code> options. </p>
<p> Also, if you use multiple <code>&#8211;remote</code> options, AND you are dropping root privileges on the client with <code>&#8211;user</code> and/or <code>&#8211;group</code> AND the client is running a non-Windows OS, if the client needs to switch to a different server, and that server pushes back different TUN/TAP or route settings, the client may lack the necessary privileges to close and reopen the TUN/TAP interface. This could cause the client to exit with a fatal error. </p>
<p> If <code>&#8211;remote</code> is unspecified, OpenVPN will listen for packets from any IP address, but will not act on those packets unless they pass all authentication tests. This requirement for authentication is binding on all potential peers, even those from known and supposedly trusted IP addresses (it is very easy to forge a source IP address on a UDP packet). </p>
<p> When used in TCP mode, <code>&#8211;remote</code> will act as a filter, rejecting connections from any host which does not match <code>host</code>. </p>
<p> If <code>host</code> is a DNS name which resolves to multiple IP addresses, OpenVPN will try them in the order that the system getaddrinfo() presents them, so priorization and DNS randomization is done by the system library. Unless an IP version is forced by the protocol specification (4/6 suffix), OpenVPN will try both IPv4 and IPv6 addresses, in the order getaddrinfo() returns them.</p>
<dt><code>&#8211;remote-random</code></p>
<dd>When multiple <code>&#8211;remote</code> address/ports are specified, or if connection profiles are being used, initially randomize the order of the list as a kind of basic load-balancing measure.</p>
<dt><code>&#8211;remote-random-hostname</code></p>
<dd>Prepend a random string (6 bytes, 12 hex characters) to hostname to prevent DNS caching. For example, &quot;foo.bar.gov&quot; would be modified to &quot;&lt;random-chars&gt;.foo.bar.gov&quot;.</p>
<dt><code>&#8211;resolv-retry</code><i>&nbsp;n</i></p>
<dd>If hostname resolve fails for <code>&#8211;remote</code>, retry resolve for <code>n</code> seconds before failing. </p>
<p> Set <code>n</code> to &quot;infinite&quot; to retry indefinitely. </p>
<p> By default, <code>&#8211;resolv-retry infinite</code> is enabled. You can disable by setting n=0.</p>
<dt><code>&#8211;single-session</code></p>
<dd>After initially connecting to a remote peer, disallow any new connections. Using this option means that a remote peer cannot connect, disconnect, and then reconnect. </p>
<p> If the daemon is reset by a signal or <code>&#8211;ping-restart</code>, it will allow one new connection. </p>
<p> <code>&#8211;single-session</code> can be used with <code>&#8211;ping-exit</code> or <code>&#8211;inactive</code> to create a single dynamic session that will exit when finished.</p>
<dt><code>&#8211;server-poll-timeout</code><i>&nbsp;n</i></p>
<dd>When connecting to a remote server do not wait for more than <code>n</code> seconds for a response before trying the next server. The default value is 120s. This timeout includes proxy and TCP connect timeouts.</p>
<dt><code>&#8211;static-challenge</code><i>&nbsp;args</i></p>
<dd>Enable static challenge/response protocol </p>
<p> Valid syntax: </p>
<pre>static-challenge text echo</pre>
<p>The <code>text</code> challenge text is presented to the user which describes what information is requested. The <code>echo</code> flag indicates if the user&#8217;s input should be echoed on the screen. Valid <code>echo</code> values are <code>0</code> or <code>1</code>. </p>
<p> See management-notes.txt in the OpenVPN distribution for a description of the OpenVPN challenge/response protocol.</p>
<dt><code>&#8211;show-proxy-settings</code></p>
<dd>Show sensed HTTP or SOCKS proxy settings. Currently, only Windows clients support this option.</p>
<dt><code>&#8211;http-proxy</code><i>&nbsp;args</i></p>
<dd>Connect to remote host through an HTTP proxy. This requires at least an address <code>server</code> and <code>port</code> argument. If HTTP Proxy-Authenticate is required, a file name to an <code>authfile</code> file containing a username and password on 2 lines can be given, or <code>stdin</code> to prompt from console. Its content can also be specified in the config file with the <code>&#8211;http-proxy-user-pass</code> option. (See section on inline files) </p>
<p> The last optional argument is an <code>auth-method</code> which should be one of <code>none</code>, <code>basic</code>, or <code>ntlm</code>. </p>
<p> HTTP Digest authentication is supported as well, but only via the <code>auto</code> or <code>auto-nct</code> flags (below). This must replace the <code>authfile</code> argument. </p>
<p> The <code>auto</code> flag causes OpenVPN to automatically determine the <code>auth-method</code> and query stdin or the management interface for username/password credentials, if required. This flag exists on OpenVPN 2.1 or higher. </p>
<p> The <code>auto-nct</code> flag (no clear-text auth) instructs OpenVPN to automatically determine the authentication method, but to reject weak authentication protocols such as HTTP Basic Authentication. </p>
<p> Examples: </p>
<pre>http-proxy proxy.example.net 3128
http-proxy proxy.example.net 3128 authfile.txt
http-proxy proxy.example.net 3128 stdin
http-proxy proxy.example.net 3128 auto basic
http-proxy proxy.example.net 3128 auto-nct ntlm</pre>
<dt><code>&#8211;http-proxy-option</code><i>&nbsp;args</i></p>
<dd>Set extended HTTP proxy options. Requires an option <code>type</code> as argument and an optional <code>parameter</code> to the type. Repeat to set multiple options.</p>
<dt><code>VERSION</code> <code>version</code></p>
<dd>Set HTTP version number to <code>version</code> (default <code>1.0</code>).</p>
<dt><code>AGENT</code> <code>user-agent</code></p>
<dd>Set HTTP &quot;User-Agent&quot; string to <code>user-agent</code>.</p>
<dt><code>CUSTOM-HEADER</code> <code>name</code> <code>content</code></p>
<dd>Adds the custom Header with <code>name</code> as name and <code>content</code> as the content of the custom HTTP header. </p>
<p> Examples: </p>
<pre>http-proxy-option VERSION 1.1
http-proxy-option AGENT OpenVPN/2.4
http-proxy-option X-Proxy-Flag some-flags</pre>
<dt><code>&#8211;socks-proxy</code><i>&nbsp;args</i></p>
<dd>Connect to remote host through a Socks5 proxy. A required <code>server</code> argument is needed. Optionally a <code>port</code> (default <code>1080</code>) and <code>authfile</code> can be given. The <code>authfile</code> is a file containing a username and password on 2 lines, or <code>stdin</code> can be used to prompt from console.</dl>
<h3>Server Options</h3>
<p>Starting with OpenVPN 2.0, a multi-client TCP/UDP server mode is supported, and can be enabled with the <code>&#8211;mode server</code> option. In server mode, OpenVPN will listen on a single port for incoming client connections. All client connections will be routed through a single tun or tap interface. This mode is designed for scalability and should be able to support hundreds or even thousands of clients on sufficiently fast hardware. SSL/TLS authentication must be used in this mode.</p>
<dl>
<dt><code>&#8211;auth-gen-token</code><i>&nbsp;args</i></p>
<dd>Returns an authentication token to successfully authenticated clients. </p>
<p> Valid syntax: </p>
<pre>auth-gen-token [lifetime] [external-auth]</pre>
<p>After successful user/password authentication, the OpenVPN server will with this option generate a temporary authentication token and push that to the client. On the following renegotiations, the OpenVPN client will pass this token instead of the users password. On the server side the server will do the token authentication internally and it will NOT do any additional authentications against configured external user/password authentication mechanisms. </p>
<p> The tokens implemented by this mechanism include an initial timestamp and a renew timestamp and are secured by HMAC. </p>
<p> The <code>lifetime</code> argument defines how long the generated token is valid. The lifetime is defined in seconds. If lifetime is not set or it is set to <code>0</code>, the token will never expire. </p>
<p> The token will expire either after the configured <code>lifetime</code> of the token is reached or after not being renewed for more than 2 * <code>reneg-sec</code> seconds. Clients will be sent renewed tokens on every TLS renogiation to keep the client&#8217;s token updated. This is done to invalidate a token if a client is disconnected for a sufficently long time, while at the same time permitting much longer token lifetimes for active clients. </p>
<p> This feature is useful for environments which are configured to use One Time Passwords (OTP) as part of the user/password authentications and that authentication mechanism does not implement any auth-token support. </p>
<p> When the <code>external-auth</code> keyword is present the normal authentication method will always be called even if auth-token succeeds. Normally other authentications method are skipped if auth-token verification suceeds or fails. </p>
<p> This option postpones this decision to the external authentication methods and checks the validity of the account and do other checks. </p>
<p> In this mode the environment will have a <code>session_id</code> variable that holds the session id from auth-gen-token. Also an environment variable <code>session_state</code> is present. This variable indicates whether the auth-token has succeeded or not. It can have the following values:</p>
<dt><code>Initial</code></p>
<dd>No token from client.</p>
<dt><code>Authenticated</code></p>
<dd>Token is valid and not expired.</p>
<dt><code>Expired</code></p>
<dd>Token is valid but has expired.</p>
<dt><code>Invalid</code></p>
<dd>Token is invalid (failed HMAC or wrong length)</p>
<dt><code>AuthenticatedEmptyUser</code> / <code>ExpiredEmptyUser</code></p>
<dd>The token is not valid with the username sent from the client but would be valid (or expired) if we assume an empty username was used instead. These two cases are a workaround for behaviour in OpenVPN 3. If this workaround is not needed these two cases should be handled in the same way as <code>Invalid</code>. </p>
<p> <code>Warning:</code> Use this feature only if you want your authentication method called on every verification. Since the external authentication is called it needs to also indicate a success or failure of the authentication. It is strongly recommended to return an authentication failure in the case of the Invalid/Expired auth-token with the external-auth option unless the client could authenticate in another acceptable way (e.g. client certificate), otherwise returning success will lead to authentication bypass (as does returning success on a wrong password from a script).</p>
<dt><code>&#8211;auth-gen-token-secret</code><i>&nbsp;file</i></p>
<dd>Specifies a file that holds a secret for the HMAC used in <code>&#8211;auth-gen-token</code> If <code>file</code> is not present OpenVPN will generate a random secret on startup. This file should be used if auth-token should validate after restarting a server or if client should be able to roam between multiple OpenVPN servers with their auth-token.</p>
<dt><code>&#8211;auth-user-pass-optional</code></p>
<dd>Allow connections by clients that do not specify a username/password. Normally, when <code>&#8211;auth-user-pass-verify</code> or <code>&#8211;management-client-auth</code> are specified (or an authentication plugin module), the OpenVPN server daemon will require connecting clients to specify a username and password. This option makes the submission of a username/password by clients optional, passing the responsibility to the user-defined authentication module/script to accept or deny the client based on other factors (such as the setting of X509 certificate fields). When this option is used, and a connecting client does not submit a username/password, the user-defined authentication module/script will see the username and password as being set to empty strings (&quot;&quot;). The authentication module/script MUST have logic to detect this condition and respond accordingly.</p>
<dt><code>&#8211;ccd-exclusive</code></p>
<dd>Require, as a condition of authentication, that a connecting client has a <code>&#8211;client-config-dir</code> file.</p>
<dt><code>&#8211;client-config-dir</code><i>&nbsp;dir</i></p>
<dd>Specify a directory <code>dir</code> for custom client config files. After a connecting client has been authenticated, OpenVPN will look in this directory for a file having the same name as the client&#8217;s X509 common name. If a matching file exists, it will be opened and parsed for client-specific configuration options. If no matching file is found, OpenVPN will instead try to open and parse a default file called &quot;DEFAULT&quot;, which may be provided but is not required. Note that the configuration files must be readable by the OpenVPN process after it has dropped it&#8217;s root privileges. </p>
<p> This file can specify a fixed IP address for a given client using <code>&#8211;ifconfig-push</code>, as well as fixed subnets owned by the client using <code>&#8211;iroute</code>. </p>
<p> One of the useful properties of this option is that it allows client configuration files to be conveniently created, edited, or removed while the server is live, without needing to restart the server. </p>
<p> The following options are legal in a client-specific context: <code>&#8211;push</code>, <code>&#8211;push-reset</code>, <code>&#8211;push-remove</code>, <code>&#8211;iroute</code>, <code>&#8211;ifconfig-push</code>, <code>&#8211;vlan-pvid</code> and <code>&#8211;config</code>.</p>
<dt><code>&#8211;client-to-client</code></p>
<dd>Because the OpenVPN server mode handles multiple clients through a single tun or tap interface, it is effectively a router. The <code>&#8211;client-to-client</code> flag tells OpenVPN to internally route client-to-client traffic rather than pushing all client-originating traffic to the TUN/TAP interface. </p>
<p> When this option is used, each client will &quot;see&quot; the other clients which are currently connected. Otherwise, each client will only see the server. Don&#8217;t use this option if you want to firewall tunnel traffic using custom, per-client rules.</p>
<dt><code>&#8211;disable</code></p>
<dd>Disable a particular client (based on the common name) from connecting. Don&#8217;t use this option to disable a client due to key or password compromise. Use a CRL (certificate revocation list) instead (see the <code>&#8211;crl-verify</code> option). </p>
<p> This option must be associated with a specific client instance, which means that it must be specified either in a client instance config file using <code>&#8211;client-config-dir</code> or dynamically generated using a <code>&#8211;client-connect</code> script.</p>
<dt><code>&#8211;connect-freq</code><i>&nbsp;args</i></p>
<dd>Allow a maximum of <code>n</code> new connections per <code>sec</code> seconds from clients. </p>
<p> Valid syntax: </p>
<pre>connect-freq n sec</pre>
<p>This is designed to contain DoS attacks which flood the server with connection requests using certificates which will ultimately fail to authenticate. </p>
<p> This is an imperfect solution however, because in a real DoS scenario, legitimate connections might also be refused. </p>
<p> For the best protection against DoS attacks in server mode, use <code>&#8211;proto udp</code> and either <code>&#8211;tls-auth</code> or <code>&#8211;tls-crypt</code>.</p>
<dt><code>&#8211;duplicate-cn</code></p>
<dd>Allow multiple clients with the same common name to concurrently connect. In the absence of this option, OpenVPN will disconnect a client instance upon connection of a new client having the same common name.</p>
<dt><code>&#8211;ifconfig-pool</code><i>&nbsp;args</i></p>
<dd>Set aside a pool of subnets to be dynamically allocated to connecting clients, similar to a DHCP server. </p>
<p> Valid syntax: </p>
<pre>ifconfig-pool start-IP end-IP [netmask]</pre>
<p>For tun-style tunnels, each client will be given a /30 subnet (for interoperability with Windows clients). For tap-style tunnels, individual addresses will be allocated, and the optional <code>netmask</code> parameter will also be pushed to clients.</p>
<dt><code>&#8211;ifconfig-ipv6-pool</code><i>&nbsp;args</i></p>
<dd>Specify an IPv6 address pool for dynamic assignment to clients. </p>
<p> Valid args: </p>
<pre>ifconfig-ipv6-pool ipv6addr/bits</pre>
<p>The pool starts at <code>ipv6addr</code> and matches the offset determined from the start of the IPv4 pool. If the host part of the given IPv6 address is <code>0</code>, the pool starts at <code>ipv6addr</code> +1.</p>
<dt><code>&#8211;ifconfig-pool-persist</code><i>&nbsp;args</i></p>
<dd>Persist/unpersist ifconfig-pool data to <code>file</code>, at <code>seconds</code> intervals (default <code>600</code>), as well as on program startup and shutdown. </p>
<p> Valid syntax: </p>
<pre>ifconfig-pool-persist file [seconds]</pre>
<p>The goal of this option is to provide a long-term association between clients (denoted by their common name) and the virtual IP address assigned to them from the ifconfig-pool. Maintaining a long-term association is good for clients because it allows them to effectively use the <code>&#8211;persist-tun</code> option. </p>
<p> <code>file</code> is a comma-delimited ASCII file, formatted as <code>&lt;Common-Name&gt;,&lt;IP-address&gt;</code>. </p>
<p> If <code>seconds</code> = <code>0</code>, <code>file</code> will be treated as read-only. This is useful if you would like to treat <code>file</code> as a configuration file. </p>
<p> Note that the entries in this file are treated by OpenVPN as <i>suggestions</i> only, based on past associations between a common name and IP address. They do not guarantee that the given common name will always receive the given IP address. If you want guaranteed assignment, use <code>&#8211;ifconfig-push</code></p>
<dt><code>&#8211;ifconfig-push</code><i>&nbsp;args</i></p>
<dd>Push virtual IP endpoints for client tunnel, overriding the <code>&#8211;ifconfig-pool</code> dynamic allocation. </p>
<p> Valid syntax: </p>
<pre>ifconfig-push local remote-netmask [alias]</pre>
<p>The parameters <code>local</code> and <code>remote-netmask</code> are set according to the <code>&#8211;ifconfig</code> directive which you want to execute on the client machine to configure the remote end of the tunnel. Note that the parameters <code>local</code> and <code>remote-netmask</code> are from the perspective of the client, not the server. They may be DNS names rather than IP addresses, in which case they will be resolved on the server at the time of client connection. </p>
<p> The optional <code>alias</code> parameter may be used in cases where NAT causes the client view of its local endpoint to differ from the server view. In this case <code>local/remote-netmask</code> will refer to the server view while <code>alias/remote-netmask</code> will refer to the client view. </p>
<p> This option must be associated with a specific client instance, which means that it must be specified either in a client instance config file using <code>&#8211;client-config-dir</code> or dynamically generated using a <code>&#8211;client-connect</code> script. </p>
<p> Remember also to include a <code>&#8211;route</code> directive in the main OpenVPN config file which encloses <code>local</code>, so that the kernel will know to route it to the server&#8217;s TUN/TAP interface. </p>
<p> OpenVPN&#8217;s internal client IP address selection algorithm works as follows:</p>
<dt>1.</p>
<dd>Use <code>&#8211;client-connect script</code> generated file for static IP (first choice).</p>
<dt>2.</p>
<dd>Use <code>&#8211;client-config-dir</code> file for static IP (next choice).</p>
<dt>3.</p>
<dd>Use <code>&#8211;ifconfig-pool</code> allocation for dynamic IP (last choice).</p>
<dt><code>&#8211;ifconfig-ipv6-push</code><i>&nbsp;args</i></p>
<dd>for <code>&#8211;client-config-dir</code> per-client static IPv6 interface configuration, see <code>&#8211;client-config-dir</code> and <code>&#8211;ifconfig-push</code> for more details. </p>
<p> Valid syntax: </p>
<pre>ifconfig-ipv6-push ipv6addr/bits ipv6remote</pre>
<dt><code>&#8211;inetd</code><i>&nbsp;args</i></p>
<dd>Valid syntaxes: </p>
<pre>inetd
inetd wait
inetd nowait
inetd wait progname</pre>
<p>Use this option when OpenVPN is being run from the inetd or <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) server. </p>
<p> The <code>wait</code> and <code>nowait</code> option must match what is specified in the inetd/xinetd config file. The <code>nowait</code> mode can only be used with <code>&#8211;proto tcp-server</code> The default is <code>wait</code>. The <code>nowait</code> mode can be used to instantiate the OpenVPN daemon as a classic TCP server, where client connection requests are serviced on a single port number. For additional information on this kind of configuration, see the OpenVPN FAQ: <i><a rel="nofollow" href="https://community.openvpn.net/openvpn/wiki/325-openvpn-as-a--forking-tcp-server-which-can-service-multiple-clients-over-a-single-tcp-port">https://community.openvpn.net/openvpn/wiki/325-openvpn-as-a&#8211;forking-tcp-server-which-can-service-multiple-clients-over-a-single-tcp-port</a></i> </p>
<p> This option precludes the use of <code>&#8211;daemon</code>, <code>&#8211;local</code> or <code>&#8211;remote</code>. Note that this option causes message and error output to be handled in the same way as the <code>&#8211;daemon</code> option. The optional <code>progname</code> parameter is also handled exactly as in <code>&#8211;daemon</code>. </p>
<p> Also note that in <code>wait</code> mode, each OpenVPN tunnel requires a separate TCP/UDP port and a separate inetd or xinetd entry. See the OpenVPN 1.x HOWTO for an example on using OpenVPN with xinetd: <i><a rel="nofollow" href="https://openvpn.net/community-resources/1xhowto/">https://openvpn.net/community-resources/1xhowto/</a></i></p>
<dt><code>&#8211;multihome</code></p>
<dd>Configure a multi-homed UDP server. This option needs to be used when a server has more than one IP address (e.g. multiple interfaces, or secondary IP addresses), and is not using <code>&#8211;local</code> to force binding to one specific address only. This option will add some extra lookups to the packet path to ensure that the UDP reply packets are always sent from the address that the client is talking to. This is not supported on all platforms, and it adds more processing, so it&#8217;s not enabled by default.</p>
<dt><i>Notes:</i></p>
<dd>
<dt>&bull;</p>
<dd>This option is only relevant for UDP servers.</p>
<dt>&bull;</p>
<dd>If you do an IPv6+IPv4 dual-stack bind on a Linux machine with multiple IPv4 address, connections to IPv4 addresses will not work right on kernels before 3.15, due to missing kernel support for the IPv4-mapped case (some distributions have ported this to earlier kernel versions, though).</p>
<dt><code>&#8211;iroute</code><i>&nbsp;args</i></p>
<dd>Generate an internal route to a specific client. The <code>netmask</code> parameter, if omitted, defaults to <code>255.255.255.255</code>. </p>
<p> Valid syntax: </p>
<pre>iroute network [netmask]</pre>
<p>This directive can be used to route a fixed subnet from the server to a particular client, regardless of where the client is connecting from. Remember that you must also add the route to the system routing table as well (such as by using the <code>&#8211;route</code> directive). The reason why two routes are needed is that the <code>&#8211;route</code> directive routes the packet from the kernel to OpenVPN. Once in OpenVPN, the <code>&#8211;iroute</code> directive routes to the specific client. </p>
<p> This option must be specified either in a client instance config file using <code>&#8211;client-config-dir</code> or dynamically generated using a <code>&#8211;client-connect</code> script. </p>
<p> The <code>&#8211;iroute</code> directive also has an important interaction with <code>&#8211;push &quot;route &#8230;&quot;</code>. <code>&#8211;iroute</code> essentially defines a subnet which is owned by a particular client (we will call this client <i>A</i>). If you would like other clients to be able to reach <i>A</i>&#8216;s subnet, you can use <code>&#8211;push &quot;route &#8230;&quot;</code> together with <code>&#8211;client-to-client</code> to effect this. In order for all clients to see <i>A</i>&#8216;s subnet, OpenVPN must push this route to all clients EXCEPT for <i>A</i>, since the subnet is already owned by <i>A</i>. OpenVPN accomplishes this by not not pushing a route to a client if it matches one of the client&#8217;s iroutes.</p>
<dt><code>&#8211;iroute-ipv6</code><i>&nbsp;args</i></p>
<dd>for <code>&#8211;client-config-dir</code> per-client static IPv6 route configuration, see <code>&#8211;iroute</code> for more details how to setup and use this, and how <code>&#8211;iroute</code> and <code>&#8211;route</code> interact. </p>
<p> Valid syntax: </p>
<pre>iroute-ipv6 ipv6addr/bits</pre>
<dt><code>&#8211;max-clients</code><i>&nbsp;n</i></p>
<dd>Limit server to a maximum of <code>n</code> concurrent clients.</p>
<dt><code>&#8211;max-routes-per-client</code><i>&nbsp;n</i></p>
<dd>Allow a maximum of <code>n</code> internal routes per client (default <code>256</code>). This is designed to help contain DoS attacks where an authenticated client floods the server with packets appearing to come from many unique MAC addresses, forcing the server to deplete virtual memory as its internal routing table expands. This directive can be used in a <code>&#8211;client-config-dir</code> file or auto-generated by a <code>&#8211;client-connect</code> script to override the global value for a particular client. </p>
<p> Note that this directive affects OpenVPN&#8217;s internal routing table, not the kernel routing table.</p>
<dt><code>&#8211;opt-verify</code></p>
<dd>Clients that connect with options that are incompatible with those of the server will be disconnected. </p>
<p> Options that will be compared for compatibility include <code>dev-type</code>, <code>link-mtu</code>, <code>tun-mtu</code>, <code>proto</code>, <code>ifconfig</code>, <code>comp-lzo</code>, <code>fragment</code>, <code>keydir</code>, <code>cipher</code>, <code>auth</code>, <code>keysize</code>, <code>secret</code>, <code>no-replay</code>, <code>tls-auth</code>, <code>key-method</code>, <code>tls-server</code> and <code>tls-client</code>. </p>
<p> This option requires that <code>&#8211;disable-occ</code> NOT be used.</p>
<dt><code>&#8211;port-share</code><i>&nbsp;args</i></p>
<dd>Share OpenVPN TCP with another service </p>
<p> Valid syntax: </p>
<pre>port-share host port [dir]</pre>
<p>When run in TCP server mode, share the OpenVPN port with another application, such as an HTTPS server. If OpenVPN senses a connection to its port which is using a non-OpenVPN protocol, it will proxy the connection to the server at <code>host</code>:<code>port</code>. Currently only designed to work with HTTP/HTTPS, though it would be theoretically possible to extend to other protocols such as ssh. </p>
<p> <code>dir</code> specifies an optional directory where a temporary file with name N containing content C will be dynamically generated for each proxy connection, where N is the source IP:port of the client connection and C is the source IP:port of the connection to the proxy receiver. This directory can be used as a dictionary by the proxy receiver to determine the origin of the connection. Each generated file will be automatically deleted when the proxied connection is torn down. </p>
<p> Not implemented on Windows.</p>
<dt><code>&#8211;push</code><i>&nbsp;option</i></p>
<dd>Push a config file option back to the client for remote execution. Note that <code>option</code> must be enclosed in double quotes (<code>&quot;&quot;</code>). The client must specify <code>&#8211;pull</code> in its config file. The set of options which can be pushed is limited by both feasibility and security. Some options such as those which would execute scripts are banned, since they would effectively allow a compromised server to execute arbitrary code on the client. Other options such as TLS or MTU parameters cannot be pushed because the client needs to know them before the connection to the server can be initiated. </p>
<p> This is a partial list of options which can currently be pushed: <code>&#8211;route</code>, <code>&#8211;route-gateway</code>, <code>&#8211;route-delay</code>, <code>&#8211;redirect-gateway</code>, <code>&#8211;ip-win32</code>, <code>&#8211;dhcp-option</code>, <code>&#8211;inactive</code>, <code>&#8211;ping</code>, <code>&#8211;ping-exit</code>, <code>&#8211;ping-restart</code>, <code>&#8211;setenv</code>, <code>&#8211;auth-token</code>, <code>&#8211;persist-key</code>, <code>&#8211;persist-tun</code>, <code>&#8211;echo</code>, <code>&#8211;comp-lzo</code>, <code>&#8211;socket-flags</code>, <code>&#8211;sndbuf</code>, <code>&#8211;rcvbuf</code></p>
<dt><code>&#8211;push-remove</code><i>&nbsp;opt</i></p>
<dd>Selectively remove all <code>&#8211;push</code> options matching &quot;opt&quot; from the option list for a client. <code>opt</code> is matched as a substring against the whole option string to-be-pushed to the client, so <code>&#8211;push-remove route</code> would remove all <code>&#8211;push route &#8230;</code> and <code>&#8211;push route-ipv6 &#8230;</code> statements, while <code>&#8211;push-remove &quot;route-ipv6 2001:&quot;</code> would only remove IPv6 routes for <code>2001:&#8230;</code> networks. </p>
<p> <code>&#8211;push-remove</code> can only be used in a client-specific context, like in a <code>&#8211;client-config-dir</code> file, or <code>&#8211;client-connect</code> script or plugin &#8212; similar to <code>&#8211;push-reset</code>, just more selective. </p>
<p> <i>NOTE</i>: to <i>change</i> an option, <code>&#8211;push-remove</code> can be used to first remove the old value, and then add a new <code>&#8211;push</code> option with the new value. </p>
<p> <i>NOTE 2</i>: due to implementation details, &#8216;ifconfig&#8217; and &#8216;ifconfig-ipv6&#8217; can only be removed with an exact match on the option ( <code>push-remove ifconfig</code>), no substring matching and no matching on the IPv4/IPv6 address argument is possible.</p>
<dt><code>&#8211;push-reset</code></p>
<dd>Don&#8217;t inherit the global push list for a specific client instance. Specify this option in a client-specific context such as with a <code>&#8211;client-config-dir</code> configuration file. This option will ignore <code>&#8211;push</code> options at the global config file level. </p>
<p> <i>NOTE</i>: <code>&#8211;push-reset</code> is very thorough: it will remove almost all options from the list of to-be-pushed options. In many cases, some of these options will need to be re-configured afterwards &#8211; specifically, <code>&#8211;topology subnet</code> and <code>&#8211;route-gateway</code> will get lost and this will break client configs in many cases. Thus, for most purposes, <code>&#8211;push-remove</code> is better suited to selectively remove push options for individual clients.</p>
<dt><code>&#8211;server</code><i>&nbsp;args</i></p>
<dd>A helper directive designed to simplify the configuration of OpenVPN&#8217;s server mode. This directive will set up an OpenVPN server which will allocate addresses to clients out of the given network/netmask. The server itself will take the <code>.1</code> address of the given network for use as the server-side endpoint of the local TUN/TAP interface. If the optional <code>nopool</code> flag is given, no dynamic IP address pool will prepared for VPN clients. </p>
<p> Valid syntax: </p>
<pre>server network netmask [nopool]</pre>
<p>For example, <code>&#8211;server 10.8.0.0 255.255.255.0</code> expands as follows: </p>
<pre>mode server
tls-server
push &quot;topology [topology]&quot;
if dev tun AND (topology == net30 OR topology == p2p):
 ifconfig 10.8.0.1 10.8.0.2
 if !nopool:
 ifconfig-pool 10.8.0.4 10.8.0.251
 route 10.8.0.0 255.255.255.0
 if client-to-client:
 push &quot;route 10.8.0.0 255.255.255.0&quot;
 else if topology == net30:
 push &quot;route 10.8.0.1&quot;
if dev tap OR (dev tun AND topology == subnet):
 ifconfig 10.8.0.1 255.255.255.0
 if !nopool:
 ifconfig-pool 10.8.0.2 10.8.0.253 255.255.255.0
 push &quot;route-gateway 10.8.0.1&quot;
 if route-gateway unset:
 route-gateway 10.8.0.2</pre>
<p>Don&#8217;t use <code>&#8211;server</code> if you are ethernet bridging. Use <code>&#8211;server-bridge</code> instead.</p>
<dt><code>&#8211;server-bridge</code><i>&nbsp;args</i></p>
<dd>A helper directive similar to <code>&#8211;server</code> which is designed to simplify the configuration of OpenVPN&#8217;s server mode in ethernet bridging configurations. </p>
<p> Valid syntaxes: </p>
<pre>server-bridge gateway netmask pool-start-IP pool-end-IP
server-bridge [nogw]</pre>
<p>If <code>&#8211;server-bridge</code> is used without any parameters, it will enable a DHCP-proxy mode, where connecting OpenVPN clients will receive an IP address for their TAP adapter from the DHCP server running on the OpenVPN server-side LAN. Note that only clients that support the binding of a DHCP client with the TAP adapter (such as Windows) can support this mode. The optional <code>nogw</code> flag (advanced) indicates that gateway information should not be pushed to the client. </p>
<p> To configure ethernet bridging, you must first use your OS&#8217;s bridging capability to bridge the TAP interface with the ethernet NIC interface. For example, on Linux this is done with the <code>brctl</code> tool, and with Windows XP it is done in the Network Connections Panel by selecting the ethernet and TAP adapters and right-clicking on &quot;Bridge Connections&quot;. </p>
<p> Next you you must manually set the IP/netmask on the bridge interface. The <code>gateway</code> and <code>netmask</code> parameters to <code>&#8211;server-bridge</code> can be set to either the IP/netmask of the bridge interface, or the IP/netmask of the default gateway/router on the bridged subnet. </p>
<p> Finally, set aside a IP range in the bridged subnet, denoted by <code>pool-start-IP</code> and <code>pool-end-IP</code>, for OpenVPN to allocate to connecting clients. </p>
<p> For example, <code>server-bridge 10.8.0.4 255.255.255.0 10.8.0.128 10.8.0.254</code> expands as follows: </p>
<pre>mode server
tls-server
ifconfig-pool 10.8.0.128 10.8.0.254 255.255.255.0
push &quot;route-gateway 10.8.0.4&quot;</pre>
<p>In another example, <code>&#8211;server-bridge</code> (without parameters) expands as follows: </p>
<pre>mode server
tls-server
push &quot;route-gateway dhcp&quot;</pre>
<p>Or <code>&#8211;server-bridge nogw</code> expands as follows: </p>
<pre>mode server
tls-server</pre>
<dt><code>&#8211;server-ipv6</code><i>&nbsp;args</i></p>
<dd>Convenience-function to enable a number of IPv6 related options at once, namely <code>&#8211;ifconfig-ipv6</code>, <code>&#8211;ifconfig-ipv6-pool</code> and <code>&#8211;push tun-ipv6</code>. </p>
<p> Valid syntax: </p>
<pre>server-ipv6 ipv6addr/bits</pre>
<p>Pushing of the <code>&#8211;tun-ipv6</code> directive is done for older clients which require an explicit <code>&#8211;tun-ipv6</code> in their configuration.</p>
<dt><code>&#8211;stale-routes-check</code><i>&nbsp;args</i></p>
<dd>Remove routes which haven&#8217;t had activity for <code>n</code> seconds (i.e. the ageing time). This check is run every <code>t</code> seconds (i.e. check interval). </p>
<p> Valid syntax: </p>
<pre>stale-routes-check n [t]</pre>
<p>If <code>t</code> is not present it defaults to <code>n</code>. </p>
<p> This option helps to keep the dynamic routing table small. See also <code>&#8211;max-routes-per-client</code></p>
<dt><code>&#8211;username-as-common-name</code></p>
<dd>Use the authenticated username as the common-name, rather than the common-name from the client certificate. Requires that some form of <code>&#8211;auth-user-pass</code> verification is in effect. As the replacement happens after <code>&#8211;auth-user-pass</code> verification, the verification script or plugin will still receive the common-name from the certificate. </p>
<p> The common_name environment variable passed to scripts and plugins invoked after authentication (e.g, client-connect script) and file names parsed in client-config directory will match the username.</p>
<dt><code>&#8211;verify-client-cert</code><i>&nbsp;mode</i></p>
<dd>Specify whether the client is required to supply a valid certificate. </p>
<p> Possible <code>mode</code> options are:</p>
<dt><code>none</code></p>
<dd>A client certificate is not required. the client needs to authenticate using username/password only. Be aware that using this directive is less secure than requiring certificates from all clients. </p>
<p> If you use this directive, the entire responsibility of authentication will rest on your <code>&#8211;auth-user-pass-verify</code> script, so keep in mind that bugs in your script could potentially compromise the security of your VPN. </p>
<p> <code>&#8211;verify-client-cert none</code> is functionally equivalent to <code>&#8211;client-cert-not-required</code>.</p>
<dt><code>optional</code></p>
<dd>A client may present a certificate but it is not required to do so. When using this directive, you should also use a <code>&#8211;auth-user-pass-verify</code> script to ensure that clients are authenticated using a certificate, a username and password, or possibly even both. </p>
<p> Again, the entire responsibility of authentication will rest on your <code>&#8211;auth-user-pass-verify</code> script, so keep in mind that bugs in your script could potentially compromise the security of your VPN.</p>
<dt><code>require</code></p>
<dd>This is the default option. A client is required to present a certificate, otherwise VPN access is refused. </p>
<p> If you don&#8217;t use this directive (or use <code>&#8211;verify-client-cert require</code>) but you also specify an <code>&#8211;auth-user-pass-verify</code> script, then OpenVPN will perform double authentication. The client certificate verification AND the <code>&#8211;auth-user-pass-verify</code> script will need to succeed in order for a client to be authenticated and accepted onto the VPN.</p>
<dt><code>&#8211;vlan-tagging</code></p>
<dd>Server-only option. Turns the OpenVPN server instance into a switch that understands VLAN-tagging, based on IEEE 802.1Q. </p>
<p> The server TAP device and each of the connecting clients is seen as a port of the switch. All client ports are in untagged mode and the server TAP device is VLAN-tagged, untagged or accepts both, depending on the <code>&#8211;vlan-accept</code> setting. </p>
<p> Ethernet frames with a prepended 802.1Q tag are called &quot;tagged&quot;. If the VLAN Identifier (VID) field in such a tag is non-zero, the frame is called &quot;VLAN-tagged&quot;. If the VID is zero, but the Priority Control Point (PCP) field is non-zero, the frame is called &quot;prio-tagged&quot;. If there is no 802.1Q tag, the frame is &quot;untagged&quot;. </p>
<p> Using the <code>&#8211;vlan-pvid v</code> option once per client (see &#8211;client-config-dir), each port can be associated with a certain VID. Packets can only be forwarded between ports having the same VID. Therefore, clients with differing VIDs are completely separated from one-another, even if <code>&#8211;client-to-client</code> is activated. </p>
<p> The packet filtering takes place in the OpenVPN server. Clients should not have any VLAN tagging configuration applied. </p>
<p> The <code>&#8211;vlan-tagging</code> option is off by default. While turned off, OpenVPN accepts any Ethernet frame and does not perform any special processing for VLAN-tagged packets. </p>
<p> This option can only be activated in <code>&#8211;dev tap mode</code>.</p>
<dt><code>&#8211;vlan-accept</code><i>&nbsp;args</i></p>
<dd>Configure the VLAN tagging policy for the server TAP device. </p>
<p> Valid syntax: </p>
<pre>vlan-accept all|tagged|untagged</pre>
<p>The following modes are available:</p>
<dt><code>tagged</code></p>
<dd>Admit only VLAN-tagged frames. Only VLAN-tagged packets are accepted, while untagged or priority-tagged packets are dropped when entering the server TAP device.</p>
<dt><code>untagged</code></p>
<dd>Admit only untagged and prio-tagged frames. VLAN-tagged packets are not accepted, while untagged or priority-tagged packets entering the server TAP device are tagged with the value configured for the global <code>&#8211;vlan-pvid</code> setting.</p>
<dt><code>all</code> (default)</p>
<dd>Admit all frames. All packets are admitted and then treated like untagged or tagged mode respectively.</p>
<dt><i>Note</i>:</p>
<dd>Some vendors refer to switch ports running in <code>tagged</code> mode as &quot;trunk ports&quot; and switch ports running in <code>untagged</code> mode as &quot;access ports&quot;. </p>
<p> Packets forwarded from clients to the server are VLAN-tagged with the originating client&#8217;s PVID, unless the VID matches the global <code>&#8211;vlan-pvid</code>, in which case the tag is removed. </p>
<p> If no <i>PVID</i> is configured for a given client (see &#8211;vlan-pvid) packets are tagged with 1 by default.</p>
<dt><code>&#8211;vlan-pvid</code><i>&nbsp;v</i></p>
<dd>Specifies which VLAN identifier a &quot;port&quot; is associated with. Only valid when <code>&#8211;vlan-tagging</code> is speficied. </p>
<p> In the client context, the setting specifies which VLAN ID a client is associated with. In the global context, the VLAN ID of the server TAP device is set. The latter only makes sense for <code>&#8211;vlan-accept untagged</code> and <code>&#8211;vlan-accept all</code> modes. </p>
<p> Valid values for <code>v</code> go from <code>1</code> through to <code>4094</code>. The global value defaults to <code>1</code>. If no <code>&#8211;vlan-pvid</code> is specified in the client context, the global value is inherited. </p>
<p> In some switch implementations, the <i>PVID</i> is also referred to as &quot;Native VLAN&quot;.</dl>
<h2>Encryption Options</h2>
<h3>SSL Library information</h3>
<dl>
<dt><code>&#8211;show-ciphers</code></p>
<dd>(Standalone) Show all cipher algorithms to use with the <code>&#8211;cipher</code> option.</p>
<dt><code>&#8211;show-digests</code></p>
<dd>(Standalone) Show all message digest algorithms to use with the <code>&#8211;auth</code> option.</p>
<dt><code>&#8211;show-tls</code></p>
<dd>(Standalone) Show all TLS ciphers supported by the crypto library. OpenVPN uses TLS to secure the control channel, over which the keys that are used to protect the actual VPN traffic are exchanged. The TLS ciphers will be sorted from highest preference (most secure) to lowest. </p>
<p> Be aware that whether a cipher suite in this list can actually work depends on the specific setup of both peers (e.g. both peers must support the cipher, and an ECDSA cipher suite will not work if you are using an RSA certificate, etc.).</p>
<dt><code>&#8211;show-engines</code></p>
<dd>(Standalone) Show currently available hardware-based crypto acceleration engines supported by the OpenSSL library.</p>
<dt><code>&#8211;show-groups</code></p>
<dd>(Standalone) Show all available elliptic curves/groups to use with the <code>&#8211;ecdh-curve</code> and <code>tls-groups</code> options.</dl>
<h3>Generating key material</h3>
<dl>
<dt><code>&#8211;genkey</code><i>&nbsp;args</i></p>
<dd>(Standalone) Generate a key to be used of the type keytype. if keyfile is left out or empty the key will be output on stdout. See the following sections for the different keytypes. </p>
<p> Valid syntax: </p>
<pre>--genkey keytype keyfile</pre>
<p>Valid keytype arguments are: </p>
<p> <code>secret</code> Standard OpenVPN shared secret keys </p>
<p> <code>tls-crypt</code> Alias for <code>secret</code> </p>
<p> <code>tls-auth</code> Alias for <code>secret</code> </p>
<p> <code>auth-token</code> Key used for <code>&#8211;auth-gen-token-key</code> </p>
<p> <code>tls-crypt-v2-server</code> TLS Crypt v2 server key </p>
<p> <code>tls-crypt-v2-client</code> TLS Crypt v2 client key </p>
<p> Examples: </p>
<pre>$ openvpn --genkey secret shared.key
$ openvpn --genkey tls-crypt shared.key
$ openvpn --genkey tls-auth shared.key
$ openvpn --genkey tls-crypt-v2-server v2crypt-server.key
$ openvpn --tls-crypt-v2 v2crypt-server.key --genkey tls-crypt-v2-client v2crypt-client-1.key</pre>
<dt>&bull;</p>
<dd>Generating <i>Shared Secret Keys</i> Generate a shared secret, for use with the <code>&#8211;secret</code>, <code>&#8211;tls-auth</code> or <code>&#8211;tls-crypt</code> options. </p>
<p> Syntax: </p>
<pre>$ openvpn --genkey secret|tls-crypt|tls-auth keyfile</pre>
<p>The key is saved in <code>keyfile</code>. All three variants (<code>&#8211;secret</code>, <code>tls-crypt</code> and <code>tls-auth</code>) generate the same type of key. The aliases are added for convenience. </p>
<p> If using this for <code>&#8211;secret</code>, this file must be shared with the peer over a pre-existing secure channel such as <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1).</p>
<dt>&bull;</p>
<dd>Generating <i>TLS Crypt v2 Server key</i> Generate a <code>&#8211;tls-crypt-v2</code> key to be used by an OpenVPN server. The key is stored in <code>keyfile</code>. </p>
<p> Syntax: </p>
<pre>--genkey tls-crypt-v2-server keyfile</pre>
<dt>&bull;</p>
<dd>Generating <i>TLS Crypt v2 Client key</i> Generate a &#8211;tls-crypt-v2 key to be used by OpenVPN clients. The key is stored in <code>keyfile</code>. </p>
<p> Syntax </p>
<pre>--genkey tls-crypt-v2-client keyfile [metadata]</pre>
<p>If supplied, include the supplied <code>metadata</code> in the wrapped client key. This metadata must be supplied in base64-encoded form. The metadata must be at most 735 bytes long (980 bytes in base64). </p>
<p> If no metadata is supplied, OpenVPN will use a 64-bit unix timestamp representing the current time in UTC, encoded in network order, as metadata for the generated key. </p>
<p> A tls-crypt-v2 client key is wrapped using a server key. To generate a client key, the user must therefore supply the server key using the <code>&#8211;tls-crypt-v2</code> option. </p>
<p> Servers can use <code>&#8211;tls-crypt-v2-verify</code> to specify a metadata verification command.</p>
<dt>&bull;</p>
<dd>Generate <i>Authentication Token key</i> Generate a new secret that can be used with <code>&#8211;auth-gen-token-secret</code> </p>
<p> Syntax: </p>
<pre>--genkey auth-token [keyfile]</pre>
<dt><i>Note:</i></p>
<dd>This file should be kept secret to the server as anyone that has access to this file will be able to generate auth tokens that the OpenVPN server will accept as valid.</dl>
<h3>Data Channel Renegotiation</h3>
<p>When running OpenVPN in client/server mode, the data channel will use a separate ephemeral encryption key which is rotated at regular intervals.</p>
<dl>
<dt><code>&#8211;reneg-bytes</code><i>&nbsp;n</i></p>
<dd>Renegotiate data channel key after <code>n</code> bytes sent or received (disabled by default with an exception, see below). OpenVPN allows the lifetime of a key to be expressed as a number of bytes encrypted/decrypted, a number of packets, or a number of seconds. A key renegotiation will be forced if any of these three criteria are met by either peer. </p>
<p> If using ciphers with cipher block sizes less than 128-bits, <code>&#8211;reneg-bytes</code> is set to 64MB by default, unless it is explicitly disabled by setting the value to <code>0</code>, but this is <code>HIGHLY DISCOURAGED</code> as this is designed to add some protection against the SWEET32 attack vector. For more information see the <code>&#8211;cipher</code> option.</p>
<dt><code>&#8211;reneg-pkts</code><i>&nbsp;n</i></p>
<dd>Renegotiate data channel key after <code>n</code> packets sent and received (disabled by default).</p>
<dt><code>&#8211;reneg-sec</code><i>&nbsp;args</i></p>
<dd>Renegotiate data channel key after at most <code>max</code> seconds (default <code>3600</code>) and at least <code>min</code> seconds (default is 90% of <code>max</code> for servers, and equal to <code>max</code> for clients). </p>
<pre>reneg-sec max [min]</pre>
<p>The effective <code>&#8211;reneg-sec</code> value used is per session pseudo-uniform-randomized between <code>min</code> and <code>max</code>. </p>
<p> With the default value of <code>3600</code> this results in an effective per session value in the range of <code>3240</code> .. <code>3600</code> seconds for servers, or just 3600 for clients. </p>
<p> When using dual-factor authentication, note that this default value may cause the end user to be challenged to reauthorize once per hour. </p>
<p> Also, keep in mind that this option can be used on both the client and server, and whichever uses the lower value will be the one to trigger the renegotiation. A common mistake is to set <code>&#8211;reneg-sec</code> to a higher value on either the client or server, while the other side of the connection is still using the default value of <code>3600</code> seconds, meaning that the renegotiation will still occur once per <code>3600</code> seconds. The solution is to increase &#8211;reneg-sec on both the client and server, or set it to <code>0</code> on one side of the connection (to disable), and to your chosen value on the other side.</dl>
<h3>TLS Mode Options</h3>
<p>TLS mode is the most powerful crypto mode of OpenVPN in both security and flexibility. TLS mode works by establishing control and data channels which are multiplexed over a single TCP/UDP port. OpenVPN initiates a TLS session over the control channel and uses it to exchange cipher and HMAC keys to protect the data channel. TLS mode uses a robust reliability layer over the UDP connection for all control channel communication, while the data channel, over which encrypted tunnel data passes, is forwarded without any mediation. The result is the best of both worlds: a fast data channel that forwards over UDP with only the overhead of encrypt, decrypt, and HMAC functions, and a control channel that provides all of the security features of TLS, including certificate-based authentication and Diffie Hellman forward secrecy. </p>
<p> To use TLS mode, each peer that runs OpenVPN should have its own local certificate/key pair (<code>&#8211;cert</code> and <code>&#8211;key</code>), signed by the root certificate which is specified in <code>&#8211;ca</code>. </p>
<p> When two OpenVPN peers connect, each presents its local certificate to the other. Each peer will then check that its partner peer presented a certificate which was signed by the master root certificate as specified in <code>&#8211;ca</code>. </p>
<p> If that check on both peers succeeds, then the TLS negotiation will succeed, both OpenVPN peers will exchange temporary session keys, and the tunnel will begin passing data. </p>
<p> The OpenVPN project provides a set of scripts for managing RSA certificates and keys: <i><a rel="nofollow" href="https://github.com/OpenVPN/easy-rsa">https://github.com/OpenVPN/easy-rsa</a></i></p>
<dl>
<dt><code>&#8211;askpass</code><i>&nbsp;file</i></p>
<dd>Get certificate password from console or <code>file</code> before we daemonize. </p>
<p> Valid syntaxes: </p>
<pre>askpass
askpass file</pre>
<p>For the extremely security conscious, it is possible to protect your private key with a password. Of course this means that every time the OpenVPN daemon is started you must be there to type the password. The <code>&#8211;askpass</code> option allows you to start OpenVPN from the command line. It will query you for a password before it daemonizes. To protect a private key with a password you should omit the <code>-nodes</code> option when you use the <code>openssl</code> command line tool to manage certificates and private keys. </p>
<p> If <code>file</code> is specified, read the password from the first line of <code>file</code>. Keep in mind that storing your password in a file to a certain extent invalidates the extra security provided by using an encrypted key.</p>
<dt><code>&#8211;ca</code><i>&nbsp;file</i></p>
<dd>Certificate authority (CA) file in .pem format, also referred to as the <i>root</i> certificate. This file can have multiple certificates in .pem format, concatenated together. You can construct your own certificate authority certificate and private key by using a command such as: </p>
<pre>openssl req -nodes -new -x509 -keyout ca.key -out ca.crt</pre>
<p>Then edit your openssl.cnf file and edit the <code>certificate</code> variable to point to your new root certificate <code>ca.crt</code>. </p>
<p> For testing purposes only, the OpenVPN distribution includes a sample CA certificate (ca.crt). Of course you should never use the test certificates and test keys distributed with OpenVPN in a production environment, since by virtue of the fact that they are distributed with OpenVPN, they are totally insecure.</p>
<dt><code>&#8211;capath</code><i>&nbsp;dir</i></p>
<dd>Directory containing trusted certificates (CAs and CRLs). Not available with mbed TLS. </p>
<p> CAs in the capath directory are expected to be named &lt;hash&gt;.&lt;n&gt;. CRLs are expected to be named &lt;hash&gt;.r&lt;n&gt;. See the <code>-CApath</code> option of <code>openssl verify</code>, and the <code>-hash</code> option of <code>openssl x509</code>, <code>openssl crl</code> and <code>X509_LOOKUP_hash_dir()</code>(3) for more information. </p>
<p> Similar to the <code>&#8211;crl-verify</code> option, CRLs are not mandatory &#8211; OpenVPN will log the usual warning in the logs if the relevant CRL is missing, but the connection will be allowed.</p>
<dt><code>&#8211;cert</code><i>&nbsp;file</i></p>
<dd>Local peer&#8217;s signed certificate in .pem format &#8212; must be signed by a certificate authority whose certificate is in <code>&#8211;ca file</code>. Each peer in an OpenVPN link running in TLS mode should have its own certificate and private key file. In addition, each certificate should have been signed by the key of a certificate authority whose public key resides in the <code>&#8211;ca</code> certificate authority file. You can easily make your own certificate authority (see above) or pay money to use a commercial service such as thawte.com (in which case you will be helping to finance the world&#8217;s second space tourist :). To generate a certificate, you can use a command such as: </p>
<pre>openssl req -nodes -new -keyout mycert.key -out mycert.csr</pre>
<p>If your certificate authority private key lives on another machine, copy the certificate signing request (mycert.csr) to this other machine (this can be done over an insecure channel such as email). Now sign the certificate with a command such as: </p>
<pre>openssl ca -out mycert.crt -in mycert.csr</pre>
<p>Now copy the certificate (mycert.crt) back to the peer which initially generated the .csr file (this can be over a public medium). Note that the <code>openssl ca</code> command reads the location of the certificate authority key from its configuration file such as <code>/usr/share/ssl/openssl.cnf</code> &#8212; note also that for certificate authority functions, you must set up the files <code>index.txt</code> (may be empty) and <code>serial</code> (initialize to <code>01</code>).</p>
<dt><code>&#8211;crl-verify</code><i>&nbsp;args</i></p>
<dd>Check peer certificate against a Certificate Revocation List. </p>
<p> Valid syntax: </p>
<pre>crl-verify file/directory flag</pre>
<p>Examples: </p>
<pre>crl-verify crl-file.pem
crl-verify /etc/openvpn/crls dir</pre>
<p>A CRL (certificate revocation list) is used when a particular key is compromised but when the overall PKI is still intact. </p>
<p> Suppose you had a PKI consisting of a CA, root certificate, and a number of client certificates. Suppose a laptop computer containing a client key and certificate was stolen. By adding the stolen certificate to the CRL file, you could reject any connection which attempts to use it, while preserving the overall integrity of the PKI. </p>
<p> The only time when it would be necessary to rebuild the entire PKI from scratch would be if the root certificate key itself was compromised. </p>
<p> The option is not mandatory &#8211; if the relevant CRL is missing, OpenVPN will log a warning in the logs &#8211; e.g. </p>
<pre>VERIFY WARNING: depth=0, unable to get certificate CRL</pre>
<p>but the connection will be allowed. If the optional <code>dir</code> flag is specified, enable a different mode where the <code>crl-verify</code> is pointed at a directory containing files named as revoked serial numbers (the files may be empty, the contents are never read). If a client requests a connection, where the client certificate serial number (decimal string) is the name of a file present in the directory, it will be rejected.</p>
<dt><i>Note:</i></p>
<dd>As the crl file (or directory) is read every time a peer connects, if you are dropping root privileges with <code>&#8211;user</code>, make sure that this user has sufficient privileges to read the file.</p>
<dt><code>&#8211;dh</code><i>&nbsp;file</i></p>
<dd>File containing Diffie Hellman parameters in .pem format (required for <code>&#8211;tls-server</code> only). </p>
<p> Set <code>file</code> to <code>none</code> to disable Diffie Hellman key exchange (and use ECDH only). Note that this requires peers to be using an SSL library that supports ECDH TLS cipher suites (e.g. OpenSSL 1.0.1+, or mbed TLS 2.0+). </p>
<p> Use <code>openssl dhparam -out dh2048.pem 2048</code> to generate 2048-bit DH parameters. Diffie Hellman parameters may be considered public.</p>
<dt><code>&#8211;ecdh-curve</code><i>&nbsp;name</i></p>
<dd>Specify the curve to use for elliptic curve Diffie Hellman. Available curves can be listed with <code>&#8211;show-curves</code>. The specified curve will only be used for ECDH TLS-ciphers. </p>
<p> This option is not supported in mbed TLS builds of OpenVPN.</p>
<dt><code>&#8211;extra-certs</code><i>&nbsp;file</i></p>
<dd>Specify a <code>file</code> containing one or more PEM certs (concatenated together) that complete the local certificate chain. </p>
<p> This option is useful for &quot;split&quot; CAs, where the CA for server certs is different than the CA for client certs. Putting certs in this file allows them to be used to complete the local certificate chain without trusting them to verify the peer-submitted certificate, as would be the case if the certs were placed in the <code>ca</code> file.</p>
<dt><code>&#8211;hand-window</code><i>&nbsp;n</i></p>
<dd>Handshake Window &#8212; the TLS-based key exchange must finalize within <code>n</code> seconds of handshake initiation by any peer (default <code>60</code> seconds). If the handshake fails we will attempt to reset our connection with our peer and try again. Even in the event of handshake failure we will still use our expiring key for up to <code>&#8211;tran-window</code> seconds to maintain continuity of transmission of tunnel data.</p>
<dt><code>&#8211;key</code><i>&nbsp;file</i></p>
<dd>Local peer&#8217;s private key in .pem format. Use the private key which was generated when you built your peer&#8217;s certificate (see <code>&#8211;cert file</code> above).</p>
<dt><code>&#8211;pkcs12</code><i>&nbsp;file</i></p>
<dd>Specify a PKCS #12 file containing local private key, local certificate, and root CA certificate. This option can be used instead of <code>&#8211;ca</code>, <code>&#8211;cert</code>, and <code>&#8211;key</code>. Not available with mbed TLS.</p>
<dt><code>&#8211;remote-cert-eku</code><i>&nbsp;oid</i></p>
<dd>Require that peer certificate was signed with an explicit <i>extended key usage</i>. </p>
<p> This is a useful security option for clients, to ensure that the host they connect to is a designated server. </p>
<p> The extended key usage should be encoded in <i>oid notation</i>, or <i>OpenSSL symbolic representation</i>.</p>
<dt><code>&#8211;remote-cert-ku</code><i>&nbsp;key-usage</i></p>
<dd>Require that peer certificate was signed with an explicit <code>key-usage</code>. </p>
<p> If present in the certificate, the <code>keyUsage</code> value is validated by the TLS library during the TLS handshake. Specifying this option without arguments requires this extension to be present (so the TLS library will verify it). </p>
<p> If <code>key-usage</code> is a list of usage bits, the <code>keyUsage</code> field must have <i>at least</i> the same bits set as the bits in <i>one of</i> the values supplied in the <code>key-usage</code> list. </p>
<p> The <code>key-usage</code> values in the list must be encoded in hex, e.g. </p>
<pre>remote-cert-ku a0</pre>
<dt><code>&#8211;remote-cert-tls</code><i>&nbsp;type</i></p>
<dd>Require that peer certificate was signed with an explicit <i>key usage</i> and <i>extended key usage</i> based on RFC3280 TLS rules. </p>
<p> Valid syntaxes: </p>
<pre>remote-cert-tls server
remote-cert-tls client</pre>
<p>This is a useful security option for clients, to ensure that the host they connect to is a designated server. Or the other way around; for a server to verify that only hosts with a client certificate can connect. </p>
<p> The <code>&#8211;remote-cert-tls client</code> option is equivalent to </p>
<pre>remote-cert-ku
remote-cert-eku &quot;TLS Web Client Authentication&quot;</pre>
<p>The <code>&#8211;remote-cert-tls server</code> option is equivalent to </p>
<pre>remote-cert-ku
remote-cert-eku &quot;TLS Web Server Authentication&quot;</pre>
<p>This is an important security precaution to protect against a man-in-the-middle attack where an authorized client attempts to connect to another client by impersonating the server. The attack is easily prevented by having clients verify the server certificate using any one of <code>&#8211;remote-cert-tls</code>, <code>&#8211;verify-x509-name</code>, or <code>&#8211;tls-verify</code>.</p>
<dt><code>&#8211;tls-auth</code><i>&nbsp;args</i></p>
<dd>Add an additional layer of HMAC authentication on top of the TLS control channel to mitigate DoS attacks and attacks on the TLS stack. </p>
<p> Valid syntaxes: </p>
<pre>tls-auth file
tls-auth file 0
tls-auth file 1</pre>
<p>In a nutshell, <code>&#8211;tls-auth</code> enables a kind of &quot;HMAC firewall&quot; on OpenVPN&#8217;s TCP/UDP port, where TLS control channel packets bearing an incorrect HMAC signature can be dropped immediately without response. </p>
<p> <code>file</code> (required) is a file in OpenVPN static key format which can be generated by <code>&#8211;genkey</code>. </p>
<p> Older versions (up to OpenVPN 2.3) supported a freeform passphrase file. This is no longer supported in newer versions (v2.4+). </p>
<p> See the <code>&#8211;secret</code> option for more information on the optional <code>direction</code> parameter. </p>
<p> <code>&#8211;tls-auth</code> is recommended when you are running OpenVPN in a mode where it is listening for packets from any IP address, such as when <code>&#8211;remote</code> is not specified, or <code>&#8211;remote</code> is specified with <code>&#8211;float</code>. </p>
<p> The rationale for this feature is as follows. TLS requires a multi-packet exchange before it is able to authenticate a peer. During this time before authentication, OpenVPN is allocating resources (memory and CPU) to this potential peer. The potential peer is also exposing many parts of OpenVPN and the OpenSSL library to the packets it is sending. Most successful network attacks today seek to either exploit bugs in programs (such as buffer overflow attacks) or force a program to consume so many resources that it becomes unusable. Of course the first line of defense is always to produce clean, well-audited code. OpenVPN has been written with buffer overflow attack prevention as a top priority. But as history has shown, many of the most widely used network applications have, from time to time, fallen to buffer overflow attacks. </p>
<p> So as a second line of defense, OpenVPN offers this special layer of authentication on top of the TLS control channel so that every packet on the control channel is authenticated by an HMAC signature and a unique ID for replay protection. This signature will also help protect against DoS (Denial of Service) attacks. An important rule of thumb in reducing vulnerability to DoS attacks is to minimize the amount of resources a potential, but as yet unauthenticated, client is able to consume. </p>
<p> <code>&#8211;tls-auth</code> does this by signing every TLS control channel packet with an HMAC signature, including packets which are sent before the TLS level has had a chance to authenticate the peer. The result is that packets without the correct signature can be dropped immediately upon reception, before they have a chance to consume additional system resources such as by initiating a TLS handshake. <code>&#8211;tls-auth</code> can be strengthened by adding the <code>&#8211;replay-persist</code> option which will keep OpenVPN&#8217;s replay protection state in a file so that it is not lost across restarts. </p>
<p> It should be emphasized that this feature is optional and that the key file used with <code>&#8211;tls-auth</code> gives a peer nothing more than the power to initiate a TLS handshake. It is not used to encrypt or authenticate any tunnel data. </p>
<p> Use <code>&#8211;tls-crypt</code> instead if you want to use the key file to not only authenticate, but also encrypt the TLS control channel.</p>
<dt><code>&#8211;tls-groups</code><i>&nbsp;list</i></p>
<dd>A list of allowable groups/curves in order of preference. </p>
<p> Set the allowed elliptic curves/groups for the TLS session. These groups are allowed to be used in signatures and key exchange. </p>
<p> mbedTLS currently allows all known curves per default. </p>
<p> OpenSSL 1.1+ restricts the list per default to </p>
<pre>&quot;X25519:secp256r1:X448:secp521r1:secp384r1&quot;.</pre>
<p>If you use certificates that use non-standard curves, you might need to add them here. If you do not force the ecdh curve by using <code>&#8211;ecdh-curve</code>, the groups for ecdh will also be picked from this list. </p>
<p> OpenVPN maps the curve name <i>secp256r1</i> to <i>prime256v1</i> to allow specifying the same tls-groups option for mbedTLS and OpenSSL. </p>
<p> Warning: this option not only affects elliptic curve certificates but also the key exchange in TLS 1.3 and using this option improperly will disable TLS 1.3.</p>
<dt><code>&#8211;tls-cert-profile</code><i>&nbsp;profile</i></p>
<dd>Set the allowed cryptographic algorithms for certificates according to <code>profile</code>. </p>
<p> The following profiles are supported:</p>
<dt><code>legacy</code> (default)</p>
<dd>SHA1 and newer, RSA 2048-bit+, any elliptic curve.</p>
<dt><code>preferred</code></p>
<dd>SHA2 and newer, RSA 2048-bit+, any elliptic curve.</p>
<dt><code>suiteb</code></p>
<dd>SHA256/SHA384, ECDSA with P-256 or P-384. </p>
<p> This option is only fully supported for mbed TLS builds. OpenSSL builds use the following approximation:</p>
<dt><code>legacy</code> (default)</p>
<dd>sets &quot;security level 1&quot;</p>
<dt><code>preferred</code></p>
<dd>sets &quot;security level 2&quot;</p>
<dt><code>suiteb</code></p>
<dd>sets &quot;security level 3&quot; and <code>&#8211;tls-cipher &quot;SUITEB128&quot;</code>. </p>
<p> OpenVPN will migrate to &#8216;preferred&#8217; as default in the future. Please ensure that your keys already comply.</p>
<dt><i>WARNING:</i> <code>&#8211;tls-ciphers</code>, <code>&#8211;tls-ciphersuites</code> and <code>tls-groups</code></p>
<dd>These options are expert features, which &#8211; if used correctly &#8211; can improve the security of your VPN connection. But it is also easy to unwittingly use them to carefully align a gun with your foot, or just break your connection. Use with care!</p>
<dt><code>&#8211;tls-cipher</code><i>&nbsp;l</i></p>
<dd>A list <code>l</code> of allowable TLS ciphers delimited by a colon (&quot;<code>:</code>&quot;). </p>
<p> These setting can be used to ensure that certain cipher suites are used (or not used) for the TLS connection. OpenVPN uses TLS to secure the control channel, over which the keys that are used to protect the actual VPN traffic are exchanged. </p>
<p> The supplied list of ciphers is (after potential OpenSSL/IANA name translation) simply supplied to the crypto library. Please see the OpenSSL and/or mbed TLS documentation for details on the cipher list interpretation. </p>
<p> For OpenSSL, the <code>&#8211;tls-cipher</code> is used for TLS 1.2 and below. </p>
<p> Use <code>&#8211;show-tls</code> to see a list of TLS ciphers supported by your crypto library. </p>
<p> The default for <code>&#8211;tls-cipher</code> is to use mbed TLS&#8217;s default cipher list when using mbed TLS or <code>DEFAULT:!EXP:!LOW:!MEDIUM:!kDH:!kECDH:!DSS:!PSK:!SRP:!kRSA</code> when using OpenSSL.</p>
<dt><code>&#8211;tls-ciphersuites</code><i>&nbsp;l</i></p>
<dd>Same as <code>&#8211;tls-cipher</code> but for TLS 1.3 and up. mbed TLS has no TLS 1.3 support yet and only the <code>&#8211;tls-cipher</code> setting is used. </p>
<p> The default for <i>&#8211;tls-ciphersuites</i> is to use the crypto library&#8217;s default.</p>
<dt><code>&#8211;tls-client</code></p>
<dd>Enable TLS and assume client role during TLS handshake.</p>
<dt><code>&#8211;tls-crypt</code><i>&nbsp;keyfile</i></p>
<dd>Encrypt and authenticate all control channel packets with the key from <code>keyfile</code>. (See <code>&#8211;tls-auth</code> for more background.) </p>
<p> Encrypting (and authenticating) control channel packets:</p>
<dt>&bull;</p>
<dd>provides more privacy by hiding the certificate used for the TLS connection,</p>
<dt>&bull;</p>
<dd>makes it harder to identify OpenVPN traffic as such,</p>
<dt>&bull;</p>
<dd>provides &quot;poor-man&#8217;s&quot; post-quantum security, against attackers who will never know the pre-shared key (i.e. no forward secrecy). </p>
<p> In contrast to <code>&#8211;tls-auth</code>, <code>&#8211;tls-crypt</code> does <i>not</i> require the user to set <code>&#8211;key-direction</code>. </p>
<p> <code>Security Considerations</code> </p>
<p> All peers use the same <code>&#8211;tls-crypt</code> pre-shared group key to authenticate and encrypt control channel messages. To ensure that IV collisions remain unlikely, this key should not be used to encrypt more than 2^48 client-to-server or 2^48 server-to-client control channel messages. A typical initial negotiation is about 10 packets in each direction. Assuming both initial negotiation and renegotiations are at most 2^16 (65536) packets (to be conservative), and (re)negotiations happen each minute for each user (24/7), this limits the tls-crypt key lifetime to 8171 years divided by the number of users. So a setup with 1000 users should rotate the key at least once each eight years. (And a setup with 8000 users each year.) </p>
<p> If IV collisions were to occur, this could result in the security of <code>&#8211;tls-crypt</code> degrading to the same security as using <code>&#8211;tls-auth</code>. That is, the control channel still benefits from the extra protection against active man-in-the-middle-attacks and DoS attacks, but may no longer offer extra privacy and post-quantum security on top of what TLS itself offers. </p>
<p> For large setups or setups where clients are not trusted, consider using <code>&#8211;tls-crypt-v2</code> instead. That uses per-client unique keys, and thereby improves the bounds to &#8216;rotate a client key at least once per 8000 years&#8217;.</p>
<dt><code>&#8211;tls-crypt-v2</code><i>&nbsp;keyfile</i></p>
<dd>Use client-specific tls-crypt keys. </p>
<p> For clients, <code>keyfile</code> is a client-specific tls-crypt key. Such a key can be generated using the <code>&#8211;genkey tls-crypt-v2-client</code> option. </p>
<p> For servers, <code>keyfile</code> is used to unwrap client-specific keys supplied by the client during connection setup. This key must be the same as the key used to generate the client-specific key (see <code>&#8211;genkey tls-crypt-v2-client</code>). </p>
<p> On servers, this option can be used together with the <code>&#8211;tls-auth</code> or <code>&#8211;tls-crypt</code> option. In that case, the server will detect whether the client is using client-specific keys, and automatically select the right mode.</p>
<dt><code>&#8211;tls-crypt-v2-verify</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> to verify the metadata of the client-specific tls-crypt-v2 key of a connecting client. This allows server administrators to reject client connections, before exposing the TLS stack (including the notoriously dangerous X.509 and ASN.1 stacks) to the connecting client. </p>
<p> OpenVPN supplies the following environment variables to the command:</p>
<dt>&bull;</p>
<dd><code>script_type</code> is set to <code>tls-crypt-v2-verify</code></p>
<dt>&bull;</p>
<dd><code>metadata_type</code> is set to <code>0</code> if the metadata was user supplied, or <code>1</code> if it&#8217;s a 64-bit unix timestamp representing the key creation time.</p>
<dt>&bull;</p>
<dd><code>metadata_file</code> contains the filename of a temporary file that contains the client metadata. </p>
<p> The command can reject the connection by exiting with a non-zero exit code.</p>
<dt><code>&#8211;tls-exit</code></p>
<dd>Exit on TLS negotiation failure.</p>
<dt><code>&#8211;tls-export-cert</code><i>&nbsp;directory</i></p>
<dd>Store the certificates the clients use upon connection to this directory. This will be done before <code>&#8211;tls-verify</code> is called. The certificates will use a temporary name and will be deleted when the tls-verify script returns. The file name used for the certificate is available via the <code>peer_cert</code> environment variable.</p>
<dt><code>&#8211;tls-server</code></p>
<dd>Enable TLS and assume server role during TLS handshake. Note that OpenVPN is designed as a peer-to-peer application. The designation of client or server is only for the purpose of negotiating the TLS control channel.</p>
<dt><code>&#8211;tls-timeout</code><i>&nbsp;n</i></p>
<dd>Packet retransmit timeout on TLS control channel if no acknowledgment from remote within <code>n</code> seconds (default <code>2</code>). When OpenVPN sends a control packet to its peer, it will expect to receive an acknowledgement within <code>n</code> seconds or it will retransmit the packet, subject to a TCP-like exponential backoff algorithm. This parameter only applies to control channel packets. Data channel packets (which carry encrypted tunnel data) are never acknowledged, sequenced, or retransmitted by OpenVPN because the higher level network protocols running on top of the tunnel such as TCP expect this role to be left to them.</p>
<dt><code>&#8211;tls-version-min</code><i>&nbsp;args</i></p>
<dd>Sets the minimum TLS version we will accept from the peer (default is &quot;1.0&quot;). </p>
<p> Valid syntax: </p>
<pre>tls-version-min version ['or-highest']</pre>
<p>Examples for version include <code>1.0</code>, <code>1.1</code>, or <code>1.2</code>. If <code>or-highest</code> is specified and version is not recognized, we will only accept the highest TLS version supported by the local SSL implementation.</p>
<dt><code>&#8211;tls-version-max</code><i>&nbsp;version</i></p>
<dd>Set the maximum TLS version we will use (default is the highest version supported). Examples for version include <code>1.0</code>, <code>1.1</code>, or <code>1.2</code>.</p>
<dt><code>&#8211;verify-hash</code><i>&nbsp;args</i></p>
<dd>Specify SHA1 or SHA256 fingerprint for level-1 cert. </p>
<p> Valid syntax: </p>
<pre>verify-hash hash [algo]</pre>
<p>The level-1 cert is the CA (or intermediate cert) that signs the leaf certificate, and is one removed from the leaf certificate in the direction of the root. When accepting a connection from a peer, the level-1 cert fingerprint must match <code>hash</code> or certificate verification will fail. Hash is specified as XX:XX:&#8230; For example: </p>
<pre>AD:B0:95:D8:09:C8:36:45:12:A9:89:C8:90:09:CB:13:72:A6:AD:16</pre>
<p>The <code>algo</code> flag can be either <code>SHA1</code> or <code>SHA256</code>. If not provided, it defaults to <code>SHA1</code>.</p>
<dt><code>&#8211;verify-x509-name</code><i>&nbsp;args</i></p>
<dd>Accept connections only if a host&#8217;s X.509 name is equal to <code>name.</code> The remote host must also pass all other tests of verification. </p>
<p> Valid syntax: </p>
<pre>verify-x509 name type</pre>
<p>Which X.509 name is compared to <code>name</code> depends on the setting of type. <code>type</code> can be <code>subject</code> to match the complete subject DN (default), <code>name</code> to match a subject RDN or <code>name-prefix</code> to match a subject RDN prefix. Which RDN is verified as name depends on the <code>&#8211;x509-username-field</code> option. But it defaults to the common name (CN), e.g. a certificate with a subject DN </p>
<pre>C=KG, ST=NA, L=Bishkek, CN=Server-1</pre>
<p>would be matched by: </p>
<pre>verify-x509-name 'C=KG, ST=NA, L=Bishkek, CN=Server-1'
verify-x509-name Server-1 name
verify-x509-name Server- name-prefix</pre>
<p>The last example is useful if you want a client to only accept connections to <code>Server-1</code>, <code>Server-2</code>, etc. </p>
<p> <code>&#8211;verify-x509-name</code> is a useful replacement for the <code>&#8211;tls-verify</code> option to verify the remote host, because <code>&#8211;verify-x509-name</code> works in a <code>&#8211;chroot</code> environment without any dependencies. </p>
<p> Using a name prefix is a useful alternative to managing a CRL (Certificate Revocation List) on the client, since it allows the client to refuse all certificates except for those associated with designated servers.</p>
<dt><i>NOTE:</i></p>
<dd>Test against a name prefix only when you are using OpenVPN with a custom CA certificate that is under your control. Never use this option with type <code>name-prefix</code> when your client certificates are signed by a third party, such as a commercial web CA.</p>
<dt><code>&#8211;x509-track</code><i>&nbsp;attribute</i></p>
<dd>Save peer X509 <code>attribute</code> value in environment for use by plugins and management interface. Prepend a <code>+</code> to <code>attribute</code> to save values from full cert chain. Values will be encoded as <code>X509_&lt;depth&gt;_&lt;attribute&gt;=&lt;value&gt;</code>. Multiple <code>&#8211;x509-track</code> options can be defined to track multiple attributes.</p>
<dt><code>&#8211;x509-username-field</code><i>&nbsp;args</i></p>
<dd>Field in the X.509 certificate subject to be used as the username (default <code>CN</code>). </p>
<p> Valid syntax: </p>
<pre>x509-username-field [ext:]fieldname</pre>
<p>Typically, this option is specified with <code>fieldname</code> as either of the following: </p>
<pre>x509-username-field emailAddress
x509-username-field ext:subjectAltName</pre>
<p>The first example uses the value of the <code>emailAddress</code> attribute in the certificate&#8217;s Subject field as the username. The second example uses the <code>ext:</code> prefix to signify that the X.509 extension <code>fieldname</code> <code>subjectAltName</code> be searched for an rfc822Name (email) field to be used as the username. In cases where there are multiple email addresses in <code>ext:fieldname</code>, the last occurrence is chosen. </p>
<p> When this option is used, the <code>&#8211;verify-x509-name</code> option will match against the chosen <code>fieldname</code> instead of the Common Name. </p>
<p> Only the <code>subjectAltName</code> and <code>issuerAltName</code> X.509 extensions are supported. </p>
<p> <code>Please note:</code> This option has a feature which will convert an all-lowercase <code>fieldname</code> to uppercase characters, e.g., <code>ou</code> -&gt; <code>OU</code>. A mixed-case <code>fieldname</code> or one having the <code>ext:</code> prefix will be left as-is. This automatic upcasing feature is deprecated and will be removed in a future release.</dl>
<h3>PKCS#11 / SmartCard options</h3>
<dl>
<dt><code>&#8211;pkcs11-cert-private</code><i>&nbsp;args</i></p>
<dd>Set if access to certificate object should be performed after login. Every provider has its own setting. </p>
<p> Valid syntaxes: </p>
<pre>pkcs11-cert-private 0
pkcs11-cert-private 1</pre>
<dt><code>&#8211;pkcs11-id</code><i>&nbsp;name</i></p>
<dd>Specify the serialized certificate id to be used. The id can be gotten by the standalone <code>&#8211;show-pkcs11-ids</code> option.</p>
<dt><code>&#8211;pkcs11-id-management</code></p>
<dd>Acquire PKCS#11 id from management interface. In this case a <code>NEED-STR &#8216;pkcs11-id-request&#8217;</code> real-time message will be triggered, application may use pkcs11-id-count command to retrieve available number of certificates, and pkcs11-id-get command to retrieve certificate id and certificate body.</p>
<dt><code>&#8211;pkcs11-pin-cache</code><i>&nbsp;seconds</i></p>
<dd>Specify how many seconds the PIN can be cached, the default is until the token is removed.</p>
<dt><code>&#8211;pkcs11-private-mode</code><i>&nbsp;mode</i></p>
<dd>Specify which method to use in order to perform private key operations. A different mode can be specified for each provider. Mode is encoded as hex number, and can be a mask one of the following: </p>
<p> <code>0</code> (default) Try to determine automatically. </p>
<p> <code>1</code> Use sign. </p>
<p> <code>2</code> Use sign recover. </p>
<p> <code>4</code> Use decrypt. </p>
<p> <code>8</code> Use unwrap.</p>
<dt><code>&#8211;pkcs11-protected-authentication</code><i>&nbsp;args</i></p>
<dd>Use PKCS#11 protected authentication path, useful for biometric and external keypad devices. Every provider has its own setting. </p>
<p> Valid syntaxes: </p>
<pre>pkcs11-protected-authentication 0
pkcs11-protected-authentication 1</pre>
<dt><code>&#8211;pkcs11-providers</code><i>&nbsp;provider</i></p>
<dd>Specify an RSA Security Inc. PKCS #11 Cryptographic Token Interface (Cryptoki) providers to load. This option can be used instead of <code>&#8211;cert</code>, <code>&#8211;key</code> and <code>&#8211;pkcs12</code>. </p>
<p> If p11-kit is present on the system, its <code>p11-kit-proxy.so</code> module will be loaded by default if either the <code>&#8211;pkcs11-id</code> or <code>&#8211;pkcs11-id-management</code> options are specified without <code>&#8211;pkcs11-provider</code> being given.</p>
<dt><code>&#8211;show-pkcs11-ids</code><i>&nbsp;args</i></p>
<dd>(Standalone) Show PKCS#11 token object list. </p>
<p> Valid syntax: </p>
<pre>show-pkcs11 [provider] [cert_private]</pre>
<p>Specify <code>cert_private</code> as <code>1</code> if certificates are stored as private objects. </p>
<p> If <i>p11-kit</i> is present on the system, the <code>provider</code> argument is optional; if omitted the default <code>p11-kit-proxy.so</code> module will be queried. </p>
<p> <code>&#8211;verb</code> option can be used BEFORE this option to produce debugging information.</dl>
<h2>Data Channel Cipher Negotiation</h2>
<p>OpenVPN 2.4 and higher have the capability to negotiate the data cipher that is used to encrypt data packets. This section describes the mechanism in more detail and the different backwards compatibility mechanism with older server and clients.</p>
<h3>OpenVPN 2.5 and higher behaviour</h3>
<p>When both client and server are at least running OpenVPN 2.5, that the order of the ciphers of the server&#8217;s <code>&#8211;data-ciphers</code> is used to pick the the data cipher. That means that the first cipher in that list that is also in the client&#8217;s <code>&#8211;data-ciphers</code> list is chosen. If no common cipher is found the client is rejected with a AUTH_FAILED message (as seen in client log): AUTH: Received control message: AUTH_FAILED,Data channel cipher negotiation failed (no shared cipher) </p>
<p> OpenVPN 2.5 will only allow the ciphers specified in <code>&#8211;data-ciphers</code>. To ensure backwards compatibility also if a cipher is specified using the <code>&#8211;cipher</code> option it is automatically added to this list. If both options are unset the default is <code>AES-256-GCM:AES-128-GCM</code>.</p>
<h3>OpenVPN 2.4 clients</h3>
<p>The negotiation support in OpenVPN 2.4 was the first iteration of the implementation and still had some quirks. Its main goal was &quot;upgrade to AES-256-GCM when possible&quot;. An OpenVPN 2.4 client that is built against a crypto library that supports AES in GCM mode and does not have <code>&#8211;ncp-disable</code> will always announce support for <i>AES-256-GCM</i> and <i>AES-128-GCM</i> to a server by sending <code>IV_NCP=2</code>. </p>
<p> This only causes a problem if <code>&#8211;ncp-ciphers</code> option has been changed from the default of <code>AES-256-GCM:AES-128-GCM</code> to a value that does not include these two ciphers. When a OpenVPN servers try to use <i>AES-256-GCM</i> or <i>AES-128-GCM</i> the connection will then fail. It is therefore recommended to always have the <i>AES-256-GCM</i> and <i>AES-128-GCM</i> ciphers to the <code>&#8211;ncp-ciphers</code> options to avoid this behaviour.</p>
<h3>OpenVPN 3 clients</h3>
<p>Clients based on the OpenVPN 3.x library (<i><a rel="nofollow" href="https://github.com/openvpn/openvpn3/">https://github.com/openvpn/openvpn3/</a></i>) do not have a configurable <code>&#8211;ncp-ciphers</code> or <code>&#8211;data-ciphers</code> option. Instead these clients will announce support for all their supported AEAD ciphers (<i>AES-256-GCM</i>, <i>AES-128-GCM</i> and in newer versions also <i>Chacha20-Poly1305</i>). </p>
<p> To support OpenVPN 3.x based clients at least one of these ciphers needs to be included in the server&#8217;s <code>&#8211;data-ciphers</code> option.</p>
<h3>OpenVPN 2.3 and older clients (and clients with <code>&#8211;ncp-disable</code>)</h3>
<p>When a client without cipher negotiation support connects to a server the cipher specified with the <code>&#8211;cipher</code> option in the client configuration must be included in the <code>&#8211;data-ciphers</code> option of the server to allow the client to connect. Otherwise the client will be sent the <code>AUTH_FAILED</code> message that indicates no shared cipher. </p>
<p> If the client is 2.3 or older and has been configured with the <code>&#8211;enable-small</code> <code>./configure</code> argument, using <code>data-ciphers-fallback cipher</code> in the server config file with the explicit cipher used by the client is necessary.</p>
<h3>OpenVPN 2.4 server</h3>
<p>When a client indicates support for <i>AES-128-GCM</i> and <i>AES-256-GCM</i> (with <code>IV_NCP=2</code>) an OpenVPN 2.4 server will send the first cipher of the <code>&#8211;ncp-ciphers</code> to the OpenVPN client regardless of what the cipher is. To emulate the behaviour of an OpenVPN 2.4 client as close as possible and have compatibility to a setup that depends on this quirk, adding <i>AES-128-GCM</i> and <i>AES-256-GCM</i> to the client&#8217;s <code>&#8211;data-ciphers</code> option is required. OpenVPN 2.5+ will only announce the <code>IV_NCP=2</code> flag if those ciphers are present.</p>
<h3>OpenVPN 2.3 and older servers (and servers with <code>&#8211;ncp-disable</code>)</h3>
<p>The cipher used by the server must be included in <code>&#8211;data-ciphers</code> to allow the client connecting to a server without cipher negotiation support. (For compatibility OpenVPN 2.5 will also accept the cipher set with <code>&#8211;cipher</code>) </p>
<p> If the server is 2.3 or older and has been configured with the <code>&#8211;enable-small</code> <code>./configure</code> argument, adding <code>data-ciphers-fallback cipher</code> to the client config with the explicit cipher used by the server is necessary.</p>
<h3>Blowfish in CBC mode (BF-CBC) deprecation</h3>
<p>The <code>&#8211;cipher</code> option defaulted to <code>BF-CBC</code> in OpenVPN 2.4 and older version. The default was never changed to ensure backwards compatibility. In OpenVPN 2.5 this behaviour has now been changed so that if the <code>&#8211;cipher</code> is not explicitly set it does not allow the weak <code>BF-CBC</code> cipher any more and needs to explicitly added as <code>&#8211;cipher BFC-CBC</code> or added to <code>&#8211;data-ciphers</code>. </p>
<p> We strongly recommend to switching away from BF-CBC to a more secure cipher as soon as possible instead.</p>
<h2>Network Configuration</h2>
<p>OpenVPN consists of two sides of network configuration. One side is the <i>link</i> between the local and remote side, the other side is the <i>virtual network adapter</i> (tun/tap device).</p>
<h3>Link Options</h3>
<p>This link options section covers options related to the connection between the local and the remote host.</p>
<dl>
<dt><code>&#8211;bind</code><i>&nbsp;keywords</i></p>
<dd>Bind to local address and port. This is the default unless any of <code>&#8211;proto tcp-client</code> , <code>&#8211;http-proxy</code> or <code>&#8211;socks-proxy</code> are used. </p>
<p> If the optional <code>ipv6only</code> keyword is present OpenVPN will bind only to IPv6 (as opposed to IPv6 and IPv4) when a IPv6 socket is opened.</p>
<dt><code>&#8211;float</code></p>
<dd>Allow remote peer to change its IP address and/or port number, such as due to DHCP (this is the default if <code>&#8211;remote</code> is not used). <code>&#8211;float</code> when specified with <code>&#8211;remote</code> allows an OpenVPN session to initially connect to a peer at a known address, however if packets arrive from a new address and pass all authentication tests, the new address will take control of the session. This is useful when you are connecting to a peer which holds a dynamic address such as a dial-in user or DHCP client. </p>
<p> Essentially, <code>&#8211;float</code> tells OpenVPN to accept authenticated packets from any address, not only the address which was specified in the <code>&#8211;remote</code> option.</p>
<dt><code>&#8211;fragment</code><i>&nbsp;max</i></p>
<dd>Enable internal datagram fragmentation so that no UDP datagrams are sent which are larger than <code>max</code> bytes. </p>
<p> The <code>max</code> parameter is interpreted in the same way as the <code>&#8211;link-mtu</code> parameter, i.e. the UDP packet size after encapsulation overhead has been added in, but not including the UDP header itself. </p>
<p> The <code>&#8211;fragment</code> option only makes sense when you are using the UDP protocol (<code>&#8211;proto udp</code>). </p>
<p> <code>&#8211;fragment</code> adds 4 bytes of overhead per datagram. </p>
<p> See the <code>&#8211;mssfix</code> option below for an important related option to <code>&#8211;fragment</code>. </p>
<p> It should also be noted that this option is not meant to replace UDP fragmentation at the IP stack level. It is only meant as a last resort when path MTU discovery is broken. Using this option is less efficient than fixing path MTU discovery for your IP link and using native IP fragmentation instead. </p>
<p> Having said that, there are circumstances where using OpenVPN&#8217;s internal fragmentation capability may be your only option, such as tunneling a UDP multicast stream which requires fragmentation.</p>
<dt><code>&#8211;keepalive</code><i>&nbsp;args</i></p>
<dd>A helper directive designed to simplify the expression of <code>&#8211;ping</code> and <code>&#8211;ping-restart</code>. </p>
<p> Valid syntax: </p>
<pre>keepalive interval timeout</pre>
<p>This option can be used on both client and server side, but it is enough to add this on the server side as it will push appropriate <code>&#8211;ping</code> and <code>&#8211;ping-restart</code> options to the client. If used on both server and client, the values pushed from server will override the client local values. </p>
<p> The <code>timeout</code> argument will be twice as long on the server side. This ensures that a timeout is detected on client side before the server side drops the connection. </p>
<p> For example, <code>&#8211;keepalive 10 60</code> expands as follows: </p>
<pre>if mode server:
 ping 10 # Argument: interval
 ping-restart 120 # Argument: timeout*2
 push &quot;ping 10&quot; # Argument: interval
 push &quot;ping-restart 60&quot; # Argument: timeout
else
 ping 10 # Argument: interval
 ping-restart 60 # Argument: timeout</pre>
<dt><code>&#8211;link-mtu</code><i>&nbsp;n</i></p>
<dd>Sets an upper bound on the size of UDP packets which are sent between OpenVPN peers. <i>It&#8217;s best not to set this parameter unless you know what you&#8217;re doing.</i></p>
<dt><code>&#8211;local</code><i>&nbsp;host</i></p>
<dd>Local host name or IP address for bind. If specified, OpenVPN will bind to this address only. If unspecified, OpenVPN will bind to all interfaces.</p>
<dt><code>&#8211;lport</code><i>&nbsp;port</i></p>
<dd>Set local TCP/UDP port number or name. Cannot be used together with <code>&#8211;nobind</code> option.</p>
<dt><code>&#8211;mark</code><i>&nbsp;value</i></p>
<dd>Mark encrypted packets being sent with value. The mark value can be matched in policy routing and packetfilter rules. This option is only supported in Linux and does nothing on other operating systems.</p>
<dt><code>&#8211;mode</code><i>&nbsp;m</i></p>
<dd>Set OpenVPN major mode. By default, OpenVPN runs in point-to-point mode (<code>p2p</code>). OpenVPN 2.0 introduces a new mode (<code>server</code>) which implements a multi-client server capability.</p>
<dt><code>&#8211;mssfix</code><i>&nbsp;max</i></p>
<dd>Announce to TCP sessions running over the tunnel that they should limit their send packet sizes such that after OpenVPN has encapsulated them, the resulting UDP packet size that OpenVPN sends to its peer will not exceed <code>max</code> bytes. The default value is <code>1450</code>. </p>
<p> The <code>max</code> parameter is interpreted in the same way as the <code>&#8211;link-mtu</code> parameter, i.e. the UDP packet size after encapsulation overhead has been added in, but not including the UDP header itself. Resulting packet would be at most 28 bytes larger for IPv4 and 48 bytes for IPv6 (20/40 bytes for IP header and 8 bytes for UDP header). Default value of 1450 allows IPv4 packets to be transmitted over a link with MTU 1473 or higher without IP level fragmentation. </p>
<p> The <code>&#8211;mssfix</code> option only makes sense when you are using the UDP protocol for OpenVPN peer-to-peer communication, i.e. <code>&#8211;proto udp</code>. </p>
<p> <code>&#8211;mssfix</code> and <code>&#8211;fragment</code> can be ideally used together, where <code>&#8211;mssfix</code> will try to keep TCP from needing packet fragmentation in the first place, and if big packets come through anyhow (from protocols other than TCP), <code>&#8211;fragment</code> will internally fragment them. </p>
<p> Both <code>&#8211;fragment</code> and <code>&#8211;mssfix</code> are designed to work around cases where Path MTU discovery is broken on the network path between OpenVPN peers. </p>
<p> The usual symptom of such a breakdown is an OpenVPN connection which successfully starts, but then stalls during active usage. </p>
<p> If <code>&#8211;fragment</code> and <code>&#8211;mssfix</code> are used together, <code>&#8211;mssfix</code> will take its default <code>max</code> parameter from the <code>&#8211;fragment max</code> option. </p>
<p> Therefore, one could lower the maximum UDP packet size to 1300 (a good first try for solving MTU-related connection problems) with the following options: </p>
<pre>--tun-mtu 1500 --fragment 1300 --mssfix</pre>
<dt><code>&#8211;mtu-disc</code><i>&nbsp;type</i></p>
<dd>Should we do Path MTU discovery on TCP/UDP channel? Only supported on OSes such as Linux that supports the necessary system call to set. </p>
<p> Valid types: </p>
<p> <code>no</code> Never send DF (Don&#8217;t Fragment) frames </p>
<p> <code>maybe</code> Use per-route hints </p>
<p> <code>yes</code> Always DF (Don&#8217;t Fragment)</p>
<dt><code>&#8211;mtu-test</code></p>
<dd>To empirically measure MTU on connection startup, add the <code>&#8211;mtu-test</code> option to your configuration. OpenVPN will send ping packets of various sizes to the remote peer and measure the largest packets which were successfully received. The <code>&#8211;mtu-test</code> process normally takes about 3 minutes to complete.</p>
<dt><code>&#8211;nobind</code></p>
<dd>Do not bind to local address and port. The IP stack will allocate a dynamic port for returning packets. Since the value of the dynamic port could not be known in advance by a peer, this option is only suitable for peers which will be initiating connections by using the &#8211;remote option.</p>
<dt><code>&#8211;passtos</code></p>
<dd>Set the TOS field of the tunnel packet to what the payload&#8217;s TOS is.</p>
<dt><code>&#8211;ping</code><i>&nbsp;n</i></p>
<dd>Ping remote over the TCP/UDP control channel if no packets have been sent for at least <code>n</code> seconds (specify <code>&#8211;ping</code> on both peers to cause ping packets to be sent in both directions since OpenVPN ping packets are not echoed like IP ping packets). When used in one of OpenVPN&#8217;s secure modes (where <code>&#8211;secret</code>, <code>&#8211;tls-server</code> or <code>&#8211;tls-client</code> is specified), the ping packet will be cryptographically secure. </p>
<p> This option has two intended uses:</p>
<dt>1.</p>
<dd>Compatibility with stateful firewalls. The periodic ping will ensure that a stateful firewall rule which allows OpenVPN UDP packets to pass will not time out.</p>
<dt>2.</p>
<dd>To provide a basis for the remote to test the existence of its peer using the <code>&#8211;ping-exit</code> option.</p>
<dt><code>&#8211;ping-exit</code><i>&nbsp;n</i></p>
<dd>Causes OpenVPN to exit after <code>n</code> seconds pass without reception of a ping or other packet from remote. This option can be combined with <code>&#8211;inactive</code>, <code>&#8211;ping</code> and <code>&#8211;ping-exit</code> to create a two-tiered inactivity disconnect. </p>
<p> For example, </p>
<pre>openvpn [options...] --inactive 3600 --ping 10 --ping-exit 60</pre>
<p>when used on both peers will cause OpenVPN to exit within 60 seconds if its peer disconnects, but will exit after one hour if no actual tunnel data is exchanged.</p>
<dt><code>&#8211;ping-restart</code><i>&nbsp;n</i></p>
<dd>Similar to <code>&#8211;ping-exit</code>, but trigger a <code>SIGUSR1</code> restart after <code>n</code> seconds pass without reception of a ping or other packet from remote. </p>
<p> This option is useful in cases where the remote peer has a dynamic IP address and a low-TTL DNS name is used to track the IP address using a service such as <i><a rel="nofollow" href="https://www.nsupdate.info/">https://www.nsupdate.info/</a></i> + a dynamic DNS client such as <code>ddclient</code>. </p>
<p> If the peer cannot be reached, a restart will be triggered, causing the hostname used with <code>&#8211;remote</code> to be re-resolved (if <code>&#8211;resolv-retry</code> is also specified). </p>
<p> In server mode, <code>&#8211;ping-restart</code>, <code>&#8211;inactive</code> or any other type of internally generated signal will always be applied to individual client instance objects, never to whole server itself. Note also in server mode that any internally generated signal which would normally cause a restart, will cause the deletion of the client instance object instead. </p>
<p> In client mode, the <code>&#8211;ping-restart</code> parameter is set to 120 seconds by default. This default will hold until the client pulls a replacement value from the server, based on the <code>&#8211;keepalive</code> setting in the server configuration. To disable the 120 second default, set <code>&#8211;ping-restart 0</code> on the client. </p>
<p> See the signals section below for more information on <code>SIGUSR1</code>. </p>
<p> Note that the behavior of <code>SIGUSR1</code> can be modified by the <code>&#8211;persist-tun</code>, <code>&#8211;persist-key</code>, <code>&#8211;persist-local-ip</code> and <code>&#8211;persist-remote-ip</code> options. </p>
<p> Also note that <code>&#8211;ping-exit</code> and <code>&#8211;ping-restart</code> are mutually exclusive and cannot be used together.</p>
<dt><code>&#8211;ping-timer-rem</code></p>
<dd>Run the <code>&#8211;ping-exit</code> / <code>&#8211;ping-restart</code> timer only if we have a remote address. Use this option if you are starting the daemon in listen mode (i.e. without an explicit <code>&#8211;remote</code> peer), and you don&#8217;t want to start clocking timeouts until a remote peer connects.</p>
<dt><code>&#8211;proto</code><i>&nbsp;p</i></p>
<dd>Use protocol <code>p</code> for communicating with remote host. <code>p</code> can be <code>udp</code>, <code>tcp-client</code>, or <code>tcp-server</code>. </p>
<p> The default protocol is <code>udp</code> when <code>&#8211;proto</code> is not specified. </p>
<p> For UDP operation, <code>&#8211;proto udp</code> should be specified on both peers. </p>
<p> For TCP operation, one peer must use <code>&#8211;proto tcp-server</code> and the other must use <code>&#8211;proto tcp-client</code>. A peer started with <code>tcp-server</code> will wait indefinitely for an incoming connection. A peer started with <code>tcp-client</code> will attempt to connect, and if that fails, will sleep for 5 seconds (adjustable via the <code>&#8211;connect-retry</code> option) and try again infinite or up to N retries (adjustable via the <code>&#8211;connect-retry-max</code> option). Both TCP client and server will simulate a SIGUSR1 restart signal if either side resets the connection. </p>
<p> OpenVPN is designed to operate optimally over UDP, but TCP capability is provided for situations where UDP cannot be used. In comparison with UDP, TCP will usually be somewhat less efficient and less robust when used over unreliable or congested networks. </p>
<p> This article outlines some of problems with tunneling IP over TCP: <i><a rel="nofollow" href="http://sites.inka.de/sites/bigred/devel/tcp-tcp.html">http://sites.inka.de/sites/bigred/devel/tcp-tcp.html</a></i> </p>
<p> There are certain cases, however, where using TCP may be advantageous from a security and robustness perspective, such as tunneling non-IP or application-level UDP protocols, or tunneling protocols which don&#8217;t possess a built-in reliability layer.</p>
<dt><code>&#8211;port</code><i>&nbsp;port</i></p>
<dd>TCP/UDP port number or port name for both local and remote (sets both <code>&#8211;lport</code> and <code>&#8211;rport</code> options to given port). The current default of 1194 represents the official IANA port number assignment for OpenVPN and has been used since version 2.0-beta17. Previous versions used port 5000 as the default.</p>
<dt><code>&#8211;rport</code><i>&nbsp;port</i></p>
<dd>Set TCP/UDP port number or name used by the <code>&#8211;remote</code> option. The port can also be set directly using the <code>&#8211;remote</code> option.</p>
<dt><code>&#8211;replay-window</code><i>&nbsp;args</i></p>
<dd>Modify the replay protection sliding-window size and time window. </p>
<p> Valid syntax: </p>
<pre>replay-window n [t]</pre>
<p>Use a replay protection sliding-window of size <code>n</code> and a time window of <code>t</code> seconds. </p>
<p> By default <code>n</code> is 64 (the IPSec default) and <code>t</code> is 15 seconds. </p>
<p> This option is only relevant in UDP mode, i.e. when either <code>&#8211;proto udp</code> is specified, or no <code>&#8211;proto</code> option is specified. </p>
<p> When OpenVPN tunnels IP packets over UDP, there is the possibility that packets might be dropped or delivered out of order. Because OpenVPN, like IPSec, is emulating the physical network layer, it will accept an out-of-order packet sequence, and will deliver such packets in the same order they were received to the TCP/IP protocol stack, provided they satisfy several constraints.</p>
<dt>a.</p>
<dd>The packet cannot be a replay (unless <code>&#8211;no-replay</code> is specified, which disables replay protection altogether).</p>
<dt>b.</p>
<dd>If a packet arrives out of order, it will only be accepted if the difference between its sequence number and the highest sequence number received so far is less than <code>n</code>.</p>
<dt>c.</p>
<dd>If a packet arrives out of order, it will only be accepted if it arrives no later than <code>t</code> seconds after any packet containing a higher sequence number. </p>
<p> If you are using a network link with a large pipeline (meaning that the product of bandwidth and latency is high), you may want to use a larger value for <code>n</code>. Satellite links in particular often require this. </p>
<p> If you run OpenVPN at <code>&#8211;verb 4</code>, you will see the message &quot;Replay-window backtrack occurred [x]&quot; every time the maximum sequence number backtrack seen thus far increases. This can be used to calibrate <code>n</code>. </p>
<p> There is some controversy on the appropriate method of handling packet reordering at the security layer. </p>
<p> Namely, to what extent should the security layer protect the encapsulated protocol from attacks which masquerade as the kinds of normal packet loss and reordering that occur over IP networks? </p>
<p> The IPSec and OpenVPN approach is to allow packet reordering within a certain fixed sequence number window. </p>
<p> OpenVPN adds to the IPSec model by limiting the window size in time as well as sequence space. </p>
<p> OpenVPN also adds TCP transport as an option (not offered by IPSec) in which case OpenVPN can adopt a very strict attitude towards message deletion and reordering: Don&#8217;t allow it. Since TCP guarantees reliability, any packet loss or reordering event can be assumed to be an attack. </p>
<p> In this sense, it could be argued that TCP tunnel transport is preferred when tunneling non-IP or UDP application protocols which might be vulnerable to a message deletion or reordering attack which falls within the normal operational parameters of IP networks. </p>
<p> So I would make the statement that one should never tunnel a non-IP protocol or UDP application protocol over UDP, if the protocol might be vulnerable to a message deletion or reordering attack that falls within the normal operating parameters of what is to be expected from the physical IP layer. The problem is easily fixed by simply using TCP as the VPN transport layer.</p>
<dt><code>&#8211;replay-persist</code><i>&nbsp;file</i></p>
<dd>Persist replay-protection state across sessions using <code>file</code> to save and reload the state. </p>
<p> This option will strengthen protection against replay attacks, especially when you are using OpenVPN in a dynamic context (such as with <code>&#8211;inetd</code>) when OpenVPN sessions are frequently started and stopped. </p>
<p> This option will keep a disk copy of the current replay protection state (i.e. the most recent packet timestamp and sequence number received from the remote peer), so that if an OpenVPN session is stopped and restarted, it will reject any replays of packets which were already received by the prior session. </p>
<p> This option only makes sense when replay protection is enabled (the default) and you are using either <code>&#8211;secret</code> (shared-secret key mode) or TLS mode with <code>&#8211;tls-auth</code>.</p>
<dt><code>&#8211;socket-flags</code><i>&nbsp;flags</i></p>
<dd>Apply the given flags to the OpenVPN transport socket. Currently, only <code>TCP_NODELAY</code> is supported. </p>
<p> The <code>TCP_NODELAY</code> socket flag is useful in TCP mode, and causes the kernel to send tunnel packets immediately over the TCP connection without trying to group several smaller packets into a larger packet. This can result in a considerably improvement in latency. </p>
<p> This option is pushable from server to client, and should be used on both client and server for maximum effect.</p>
<dt><code>&#8211;tcp-nodelay</code></p>
<dd>This macro sets the <code>TCP_NODELAY</code> socket flag on the server as well as pushes it to connecting clients. The <code>TCP_NODELAY</code> flag disables the Nagle algorithm on TCP sockets causing packets to be transmitted immediately with low latency, rather than waiting a short period of time in order to aggregate several packets into a larger containing packet. In VPN applications over TCP, <code>TCP_NODELAY</code> is generally a good latency optimization. </p>
<p> The macro expands as follows: </p>
<pre>if mode server:
 socket-flags TCP_NODELAY
 push &quot;socket-flags TCP_NODELAY&quot;</pre>
</dl>
<h3>Virtual Network Adapter (VPN interface)</h3>
<p>Options in this section relates to configuration of the virtual tun/tap network interface, including setting the VPN IP address and network routing.</p>
<dl>
<dt><code>&#8211;bind-dev</code><i>&nbsp;device</i></p>
<dd>(Linux only) Set <code>device</code> to bind the server socket to a <i>Virtual Routing and Forwarding</i> device</p>
<dt><code>&#8211;block-ipv6</code></p>
<dd>On the client, instead of sending IPv6 packets over the VPN tunnel, all IPv6 packets are answered with an ICMPv6 no route host message. On the server, all IPv6 packets from clients are answered with an ICMPv6 no route to host message. This options is intended for cases when IPv6 should be blocked and other options are not available. <code>&#8211;block-ipv6</code> will use the remote IPv6 as source address of the ICMPv6 packets if set, otherwise will use <code>fe80::7</code> as source address. </p>
<p> For this option to make sense you actually have to route traffic to the tun interface. The following example config block would send all IPv6 traffic to OpenVPN and answer all requests with no route to host, effectively blocking IPv6 (to avoid IPv6 connections from dual-stacked clients leaking around IPv4-only VPN services).</p>
<dt><code>Client config</code></p>
<dd>
<pre>--ifconfig-ipv6 fd15:53b6:dead::2/64 fd15:53b6:dead::1
--redirect-gateway ipv6
--block-ipv6</pre>
<dt><code>Server config</code></p>
<dd>Push a &quot;valid&quot; ipv6 config to the client and block on the server </p>
<pre>--push &quot;ifconfig-ipv6 fd15:53b6:dead::2/64 fd15:53b6:dead::1&quot;
--push &quot;redirect-gateway ipv6&quot;
--block-ipv6</pre>
<p>Note: this option does not influence traffic sent from the server towards the client (neither on the server nor on the client side). This is not seen as necessary, as such traffic can be most easily avoided by not configuring IPv6 on the server tun, or setting up a server-side firewall rule.</p>
<dt><code>&#8211;dev</code><i>&nbsp;device</i></p>
<dd>TUN/TAP virtual network device which can be <code>tunX</code>, <code>tapX</code>, <code>null</code> or an arbitrary name string (<code>X</code> can be omitted for a dynamic device.) </p>
<p> See examples section below for an example on setting up a TUN device. </p>
<p> You must use either tun devices on both ends of the connection or tap devices on both ends. You cannot mix them, as they represent different underlying network layers:</p>
<dt><code>tun</code></p>
<dd>devices encapsulate IPv4 or IPv6 (OSI Layer 3)</p>
<dt><code>tap</code></p>
<dd>devices encapsulate Ethernet 802.3 (OSI Layer 2). </p>
<p> Valid syntaxes: </p>
<pre>dev tun2
dev tap4
dev ovpn</pre>
<p>When the device name starts with <code>tun</code> or <code>tap</code>, the device type is extracted automatically. Otherwise the <code>&#8211;dev-type</code> option needs to be added as well.</p>
<dt><code>&#8211;dev-node</code><i>&nbsp;node</i></p>
<dd>Explicitly set the device node rather than using <code>/dev/net/tun</code>, <code>/dev/tun</code>, <code>/dev/tap</code>, etc. If OpenVPN cannot figure out whether <code>node</code> is a TUN or TAP device based on the name, you should also specify <code>&#8211;dev-type tun</code> or <code>&#8211;dev-type tap</code>. </p>
<p> Under Mac OS X this option can be used to specify the default tun implementation. Using <code>&#8211;dev-node utun</code> forces usage of the native Darwin tun kernel support. Use <code>&#8211;dev-node utunN</code> to select a specific utun instance. To force using the <code>tun.kext</code> (<code>/dev/tunX</code>) use <code>&#8211;dev-node tun</code>. When not specifying a <code>&#8211;dev-node</code> option openvpn will first try to open utun, and fall back to tun.kext. </p>
<p> On Windows systems, select the TAP-Win32 adapter which is named <code>node</code> in the Network Connections Control Panel or the raw GUID of the adapter enclosed by braces. The <code>&#8211;show-adapters</code> option under Windows can also be used to enumerate all available TAP-Win32 adapters and will show both the network connections control panel name and the GUID for each TAP-Win32 adapter.</p>
<dt><code>&#8211;dev-type</code><i>&nbsp;device-type</i></p>
<dd>Which device type are we using? <code>device-type</code> should be <code>tun</code> (OSI Layer 3) or <code>tap</code> (OSI Layer 2). Use this option only if the TUN/TAP device used with <code>&#8211;dev</code> does not begin with <code>tun</code> or <code>tap</code>.</p>
<dt><code>&#8211;dhcp-option</code><i>&nbsp;args</i></p>
<dd>Set additional network parameters on supported platforms. May be specified on the client or pushed from the server. On Windows these options are handled by the <code>tap-windows6</code> driver by default or directly by OpenVPN if dhcp is disabled or the <code>wintun</code> driver is in use. The <code>OpenVPN for Android</code> client also handles them internally. </p>
<p> On all other platforms these options are only saved in the client&#8217;s environment under the name <code>foreign_option_{n}</code> before the <code>&#8211;up</code> script is called. A plugin or an <code>&#8211;up</code> script must be used to pick up and interpret these as required. Many Linux distributions include such scripts and some third-party user interfaces such as tunnelblick also come with scripts that process these options. </p>
<p> Valid syntax: </p>
<pre>dhcp-options type [parm]</pre>
<dt><code>DOMAIN</code> <code>name</code></p>
<dd>Set Connection-specific DNS Suffix to <code>name</code>.</p>
<dt><code>ADAPTER_DOMAIN_SUFFIX</code> <code>name</code></p>
<dd>Alias to <code>DOMAIN</code>. This is a compatibility option, it should not be used in new deployments.</p>
<dt><code>DOMAIN-SEARCH</code> <code>name</code></p>
<dd>Add <code>name</code> to the domain search list. Repeat this option to add more entries. Up to 10 domains are supported.</p>
<dt><code>DNS</code> <code>address</code></p>
<dd>Set primary domain name server IPv4 or IPv6 address. Repeat this option to set secondary DNS server addresses. </p>
<p> Note: DNS IPv6 servers are currently set using netsh (the existing DHCP code can only do IPv4 DHCP, and that protocol only permits IPv4 addresses anywhere). The option will be put into the environment, so an <code>&#8211;up</code> script could act upon it if needed.</p>
<dt><code>WINS</code> <code>address</code></p>
<dd>Set primary WINS server address (NetBIOS over TCP/IP Name Server). Repeat this option to set secondary WINS server addresses.</p>
<dt><code>NBDD</code> <code>address</code></p>
<dd>Set primary NBDD server address (NetBIOS over TCP/IP Datagram Distribution Server). Repeat this option to set secondary NBDD server addresses.</p>
<dt><code>NTP</code> <code>address</code></p>
<dd>Set primary NTP server address (Network Time Protocol). Repeat this option to set secondary NTP server addresses.</p>
<dt><code>NBT</code> <code>type</code></p>
<dd>Set NetBIOS over TCP/IP Node type. Possible options:</p>
<dt><code>1</code></p>
<dd>b-node (broadcasts)</p>
<dt><code>2</code></p>
<dd>p-node (point-to-point name queries to a WINS server)</p>
<dt><code>4</code></p>
<dd>m-node (broadcast then query name server)</p>
<dt><code>8</code></p>
<dd>h-node (query name server, then broadcast).</p>
<dt><code>NBS</code> <code>scope-id</code></p>
<dd>Set NetBIOS over TCP/IP Scope. A NetBIOS Scope ID provides an extended naming service for the NetBIOS over TCP/IP (Known as NBT) module. The primary purpose of a NetBIOS scope ID is to isolate NetBIOS traffic on a single network to only those nodes with the same NetBIOS scope ID. The NetBIOS scope ID is a character string that is appended to the NetBIOS name. The NetBIOS scope ID on two hosts must match, or the two hosts will not be able to communicate. The NetBIOS Scope ID also allows computers to use the same computer name, as they have different scope IDs. The Scope ID becomes a part of the NetBIOS name, making the name unique. (This description of NetBIOS scopes courtesy of <i>NeonSurge [at] abyss.com</i>)</p>
<dt><code>DISABLE-NBT</code></p>
<dd>Disable Netbios-over-TCP/IP.</p>
<dt><code>&#8211;ifconfig</code><i>&nbsp;args</i></p>
<dd>Set TUN/TAP adapter parameters. It requires the <i>IP address</i> of the local VPN endpoint. For TUN devices in point-to-point mode, the next argument must be the VPN IP address of the remote VPN endpoint. For TAP devices, or TUN devices used with <code>&#8211;topology subnet</code>, the second argument is the subnet mask of the virtual network segment which is being created or connected to. </p>
<p> For TUN devices, which facilitate virtual point-to-point IP connections (when used in <code>&#8211;topology net30</code> or <code>p2p</code> mode), the proper usage of <code>&#8211;ifconfig</code> is to use two private IP addresses which are not a member of any existing subnet which is in use. The IP addresses may be consecutive and should have their order reversed on the remote peer. After the VPN is established, by pinging <code>rn</code>, you will be pinging across the VPN. </p>
<p> For TAP devices, which provide the ability to create virtual ethernet segments, or TUN devices in <code>&#8211;topology subnet</code> mode (which create virtual &quot;multipoint networks&quot;), <code>&#8211;ifconfig</code> is used to set an IP address and subnet mask just as a physical ethernet adapter would be similarly configured. If you are attempting to connect to a remote ethernet bridge, the IP address and subnet should be set to values which would be valid on the the bridged ethernet segment (note also that DHCP can be used for the same purpose). </p>
<p> This option, while primarily a proxy for the <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) command, is designed to simplify TUN/TAP tunnel configuration by providing a standard interface to the different ifconfig implementations on different platforms. </p>
<p> <code>&#8211;ifconfig</code> parameters which are IP addresses can also be specified as a DNS or /etc/hosts file resolvable name. </p>
<p> For TAP devices, <code>&#8211;ifconfig</code> should not be used if the TAP interface will be getting an IP address lease from a DHCP server. </p>
<p> Examples: </p>
<pre># tun device in net30/p2p mode
ifconfig 10.8.0.2 10.8.0.1
# tun/tap device in subnet mode
ifconfig 10.8.0.2 255.255.255.0</pre>
<dt><code>&#8211;ifconfig-ipv6</code><i>&nbsp;args</i></p>
<dd>Configure an IPv6 address on the <i>tun</i> device. </p>
<p> Valid syntax: </p>
<pre>ifconfig-ipv6 ipv6addr/bits [ipv6remote]</pre>
<p>The <code>ipv6addr/bits</code> argument is the IPv6 address to use. The second parameter is used as route target for <code>&#8211;route-ipv6</code> if no gateway is specified. </p>
<p> The <code>&#8211;topology</code> option has no influence with <code>&#8211;ifconfig-ipv6</code></p>
<dt><code>&#8211;ifconfig-noexec</code></p>
<dd>Don&#8217;t actually execute ifconfig/netsh commands, instead pass <code>&#8211;ifconfig</code> parameters to scripts using environmental variables.</p>
<dt><code>&#8211;ifconfig-nowarn</code></p>
<dd>Don&#8217;t output an options consistency check warning if the <code>&#8211;ifconfig</code> option on this side of the connection doesn&#8217;t match the remote side. This is useful when you want to retain the overall benefits of the options consistency check (also see <code>&#8211;disable-occ</code> option) while only disabling the ifconfig component of the check. </p>
<p> For example, if you have a configuration where the local host uses <code>&#8211;ifconfig</code> but the remote host does not, use <code>&#8211;ifconfig-nowarn</code> on the local host. </p>
<p> This option will also silence warnings about potential address conflicts which occasionally annoy more experienced users by triggering &quot;false positive&quot; warnings.</p>
<dt><code>&#8211;lladdr</code><i>&nbsp;address</i></p>
<dd>Specify the link layer address, more commonly known as the MAC address. Only applied to TAP devices.</p>
<dt><code>&#8211;persist-tun</code></p>
<dd>Don&#8217;t close and reopen TUN/TAP device or run up/down scripts across <code>SIGUSR1</code> or <code>&#8211;ping-restart</code> restarts. </p>
<p> <code>SIGUSR1</code> is a restart signal similar to <code>SIGHUP</code>, but which offers finer-grained control over reset options.</p>
<dt><code>&#8211;redirect-gateway</code><i>&nbsp;flags</i></p>
<dd>Automatically execute routing commands to cause all outgoing IP traffic to be redirected over the VPN. This is a client-side option. </p>
<p> This option performs three steps:</p>
<dt>1.</p>
<dd>Create a static route for the <code>&#8211;remote</code> address which forwards to the pre-existing default gateway. This is done so that <code>(3)</code> will not create a routing loop.</p>
<dt>2.</p>
<dd>Delete the default gateway route.</p>
<dt>3.</p>
<dd>Set the new default gateway to be the VPN endpoint address (derived either from <code>&#8211;route-gateway</code> or the second parameter to <code>&#8211;ifconfig</code> when <code>&#8211;dev tun</code> is specified). </p>
<p> When the tunnel is torn down, all of the above steps are reversed so that the original default route is restored. </p>
<p> Option flags:</p>
<dt><code>local</code></p>
<dd>Add the <code>local</code> flag if both OpenVPN peers are directly connected via a common subnet, such as with wireless. The <code>local</code> flag will cause step <code>(1)</code> above to be omitted.</p>
<dt><code>autolocal</code></p>
<dd>Try to automatically determine whether to enable <code>local</code> flag above.</p>
<dt><code>def1</code></p>
<dd>Use this flag to override the default gateway by using <code>0.0.0.0/1</code> and <code>128.0.0.0/1</code> rather than <code>0.0.0.0/0</code>. This has the benefit of overriding but not wiping out the original default gateway.</p>
<dt><code>bypass-dhcp</code></p>
<dd>Add a direct route to the DHCP server (if it is non-local) which bypasses the tunnel (Available on Windows clients, may not be available on non-Windows clients).</p>
<dt><code>bypass-dns</code></p>
<dd>Add a direct route to the DNS server(s) (if they are non-local) which bypasses the tunnel (Available on Windows clients, may not be available on non-Windows clients).</p>
<dt><code>block-local</code></p>
<dd>Block access to local LAN when the tunnel is active, except for the LAN gateway itself. This is accomplished by routing the local LAN (except for the LAN gateway address) into the tunnel.</p>
<dt><code>ipv6</code></p>
<dd>Redirect IPv6 routing into the tunnel. This works similar to the <code>def1</code> flag, that is, more specific IPv6 routes are added (<code>2000::/4</code>, <code>3000::/4</code>), covering the whole IPv6 unicast space.</p>
<dt><code>!ipv4</code></p>
<dd>Do not redirect IPv4 traffic &#8211; typically used in the flag pair <code>ipv6 !ipv4</code> to redirect IPv6-only.</p>
<dt><code>&#8211;redirect-private</code><i>&nbsp;flags</i></p>
<dd>Like <code>&#8211;redirect-gateway</code>, but omit actually changing the default gateway. Useful when pushing private subnets.</p>
<dt><code>&#8211;route</code><i>&nbsp;args</i></p>
<dd>Add route to routing table after connection is established. Multiple routes can be specified. Routes will be automatically torn down in reverse order prior to TUN/TAP device close. </p>
<p> Valid syntaxes: </p>
<pre>route network/IP
route network/IP netmask
route network/IP netmask gateway
route network/IP netmask gateway metric</pre>
<p>This option is intended as a convenience proxy for the <code><a href="/docs/linux/man/8-route/">route</a></code>(8) shell command, while at the same time providing portable semantics across OpenVPN&#8217;s platform space.</p>
<dt><code>netmask</code></p>
<dd>defaults to <code>255.255.255.255</code> when not given</p>
<dt><code>gateway</code></p>
<dd>default taken from <code>&#8211;route-gateway</code> or the second parameter to <code>&#8211;ifconfig</code> when <code>&#8211;dev tun</code> is specified.</p>
<dt><code>metric</code></p>
<dd>default taken from <code>&#8211;route-metric</code> if set, otherwise <code>0</code>. </p>
<p> The default can be specified by leaving an option blank or setting it to <code>default</code>. </p>
<p> The <code>network</code> and <code>gateway</code> parameters can also be specified as a DNS or <code>/etc/hosts</code> file resolvable name, or as one of three special keywords:</p>
<dt><code>vpn_gateway</code></p>
<dd>The remote VPN endpoint address (derived either from <code>&#8211;route-gateway</code> or the second parameter to <code>&#8211;ifconfig</code> when <code>&#8211;dev tun</code> is specified).</p>
<dt><code>net_gateway</code></p>
<dd>The pre-existing IP default gateway, read from the routing table (not supported on all OSes).</p>
<dt><code>remote_host</code></p>
<dd>The <code>&#8211;remote</code> address if OpenVPN is being run in client mode, and is undefined in server mode.</p>
<dt><code>&#8211;route-delay</code><i>&nbsp;args</i></p>
<dd>Valid syntaxes: </p>
<pre>route-delay
route-delay n
route-delay n m</pre>
<p>Delay <code>n</code> seconds (default <code>0</code>) after connection establishment, before adding routes. If <code>n</code> is <code>0</code>, routes will be added immediately upon connection establishment. If <code>&#8211;route-delay</code> is omitted, routes will be added immediately after TUN/TAP device open and <code>&#8211;up</code> script execution, before any <code>&#8211;user</code> or <code>&#8211;group</code> privilege downgrade (or <code>&#8211;chroot</code> execution.) </p>
<p> This option is designed to be useful in scenarios where DHCP is used to set tap adapter addresses. The delay will give the DHCP handshake time to complete before routes are added. </p>
<p> On Windows, <code>&#8211;route-delay</code> tries to be more intelligent by waiting <code>w</code> seconds (default <code>30</code> by default) for the TAP-Win32 adapter to come up before adding routes.</p>
<dt><code>&#8211;route-ipv6</code><i>&nbsp;args</i></p>
<dd>Setup IPv6 routing in the system to send the specified IPv6 network into OpenVPN&#8217;s <i>tun</i>. </p>
<p> Valid syntax: </p>
<pre>route-ipv6 ipv6addr/bits [gateway] [metric]</pre>
<p>The gateway parameter is only used for IPv6 routes across <i>tap</i> devices, and if missing, the <code>ipv6remote</code> field from <code>&#8211;ifconfig-ipv6</code> or <code>&#8211;route-ipv6-gateway</code> is used.</p>
<dt><code>&#8211;route-gateway</code><i>&nbsp;arg</i></p>
<dd>Specify a default <i>gateway</i> for use with <code>&#8211;route</code>. </p>
<p> If <code>dhcp</code> is specified as the parameter, the gateway address will be extracted from a DHCP negotiation with the OpenVPN server-side LAN. </p>
<p> Valid syntaxes: </p>
<pre>route-gateway gateway
route-gateway dhcp</pre>
<dt><code>&#8211;route-ipv6-gateway</code><i>&nbsp;gw</i></p>
<dd>Specify a default gateway <code>gw</code> for use with <code>&#8211;route-ipv6</code>.</p>
<dt><code>&#8211;route-metric</code><i>&nbsp;m</i></p>
<dd>Specify a default metric <code>m</code> for use with <code>&#8211;route</code>.</p>
<dt><code>&#8211;route-noexec</code></p>
<dd>Don&#8217;t add or remove routes automatically. Instead pass routes to <code>&#8211;route-up</code> script using environmental variables.</p>
<dt><code>&#8211;route-nopull</code></p>
<dd>When used with <code>&#8211;client</code> or <code>&#8211;pull</code>, accept options pushed by server EXCEPT for routes, block-outside-dns and dhcp options like DNS servers. </p>
<p> When used on the client, this option effectively bars the server from adding routes to the client&#8217;s routing table, however note that this option still allows the server to set the TCP/IP properties of the client&#8217;s TUN/TAP interface.</p>
<dt><code>&#8211;topology</code><i>&nbsp;mode</i></p>
<dd>Configure virtual addressing topology when running in <code>&#8211;dev tun</code> mode. This directive has no meaning in <code>&#8211;dev tap</code> mode, which always uses a <code>subnet</code> topology. </p>
<p> If you set this directive on the server, the <code>&#8211;server</code> and <code>&#8211;server-bridge</code> directives will automatically push your chosen topology setting to clients as well. This directive can also be manually pushed to clients. Like the <code>&#8211;dev</code> directive, this directive must always be compatible between client and server. </p>
<p> <code>mode</code> can be one of:</p>
<dt><code>net30</code></p>
<dd>Use a point-to-point topology, by allocating one /30 subnet per client. This is designed to allow point-to-point semantics when some or all of the connecting clients might be Windows systems. This is the default on OpenVPN 2.0.</p>
<dt><code>p2p</code></p>
<dd>Use a point-to-point topology where the remote endpoint of the client&#8217;s tun interface always points to the local endpoint of the server&#8217;s tun interface. This mode allocates a single IP address per connecting client. Only use when none of the connecting clients are Windows systems.</p>
<dt><code>subnet</code></p>
<dd>Use a subnet rather than a point-to-point topology by configuring the tun interface with a local IP address and subnet mask, similar to the topology used in <code>&#8211;dev tap</code> and ethernet bridging mode. This mode allocates a single IP address per connecting client and works on Windows as well. Only available when server and clients are OpenVPN 2.1 or higher, or OpenVPN 2.0.x which has been manually patched with the <code>&#8211;topology</code> directive code. When used on Windows, requires version 8.2 or higher of the TAP-Win32 driver. When used on *nix, requires that the tun driver supports an <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) command which sets a subnet instead of a remote endpoint IP address. </p>
<p> <i>Note:</i> Using <code>&#8211;topology subnet</code> changes the interpretation of the arguments of <code>&#8211;ifconfig</code> to mean &quot;address netmask&quot;, no longer &quot;local remote&quot;.</p>
<dt><code>&#8211;tun-mtu</code><i>&nbsp;n</i></p>
<dd>Take the TUN device MTU to be <code>n</code> and derive the link MTU from it (default <code>1500</code>). In most cases, you will probably want to leave this parameter set to its default value. </p>
<p> The MTU (Maximum Transmission Units) is the maximum datagram size in bytes that can be sent unfragmented over a particular network path. OpenVPN requires that packets on the control and data channels be sent unfragmented. </p>
<p> MTU problems often manifest themselves as connections which hang during periods of active usage. </p>
<p> It&#8217;s best to use the <code>&#8211;fragment</code> and/or <code>&#8211;mssfix</code> options to deal with MTU sizing issues.</p>
<dt><code>&#8211;tun-mtu-extra</code><i>&nbsp;n</i></p>
<dd>Assume that the TUN/TAP device might return as many as <code>n</code> bytes more than the <code>&#8211;tun-mtu</code> size on read. This parameter defaults to 0, which is sufficient for most TUN devices. TAP devices may introduce additional overhead in excess of the MTU size, and a setting of 32 is the default when TAP devices are used. This parameter only controls internal OpenVPN buffer sizing, so there is no transmission overhead associated with using a larger value.</dl>
<h3>TUN/TAP standalone operations</h3>
<p>These two standalone operations will require <code>&#8211;dev</code> and optionally <code>&#8211;user</code> and/or <code>&#8211;group</code>.</p>
<dl>
<dt><code>&#8211;mktun</code></p>
<dd>(Standalone) Create a persistent tunnel on platforms which support them such as Linux. Normally TUN/TAP tunnels exist only for the period of time that an application has them open. This option takes advantage of the TUN/TAP driver&#8217;s ability to build persistent tunnels that live through multiple instantiations of OpenVPN and die only when they are deleted or the machine is rebooted. </p>
<p> One of the advantages of persistent tunnels is that they eliminate the need for separate <code>&#8211;up</code> and <code>&#8211;down</code> scripts to run the appropriate <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) and <code><a href="/docs/linux/man/8-route/">route</a></code>(8) commands. These commands can be placed in the the same shell script which starts or terminates an OpenVPN session. </p>
<p> Another advantage is that open connections through the TUN/TAP-based tunnel will not be reset if the OpenVPN peer restarts. This can be useful to provide uninterrupted connectivity through the tunnel in the event of a DHCP reset of the peer&#8217;s public IP address (see the <code>&#8211;ipchange</code> option above). </p>
<p> One disadvantage of persistent tunnels is that it is harder to automatically configure their MTU value (see <code>&#8211;link-mtu</code> and <code>&#8211;tun-mtu</code> above). </p>
<p> On some platforms such as Windows, TAP-Win32 tunnels are persistent by default.</p>
<dt><code>&#8211;rmtun</code></p>
<dd>(Standalone) Remove a persistent tunnel.</dl>
<h3>Virtual Routing and Forwarding</h3>
<p>Options in this section relates to configuration of virtual routing and forwarding in combination with the underlying operating system. </p>
<p> As of today this is only supported on Linux, a kernel &gt;= 4.9 is recommended. </p>
<p> This could come in handy when for example the external network should be only used as a means to connect to some VPN endpoints and all regular traffic should only be routed through any tunnel(s). This could be achieved by setting up a VRF and configuring the interface connected to the external network to be part of the VRF. The examples below will cover this setup. </p>
<p> Another option would be to put the tun/tap interface into a VRF. This could be done by an up-script which uses the <code>ip link set</code> command shown below.</p>
<h3>VRF setup with iproute2</h3>
<p>Create VRF <code>vrf_external</code> and map it to routing table <code>1023</code> </p>
<pre>ip link add vrf_external type vrf table 1023</pre>
<p>Move <code>eth0</code> into <code>vrf_external</code> </p>
<pre>ip link set master vrf_external dev eth0</pre>
<p>Any prefixes configured on <code>eth0</code> will be moved from the :code`main` routing table into routing table <i>1023</i></p>
<h3>VRF setup with ifupdown</h3>
<p>For Debian based Distributions <code>ifupdown2</code> provides an almost drop-in replacement for <code>ifupdown</code> including VRFs and other features. A configuration for an interface <code>eth0</code> being part of VRF code:<i>vrf_external</i> could look like this: </p>
<pre>auto eth0
iface eth0
 address 192.0.2.42/24
 address 2001:db8:08:15::42/64
 gateway 192.0.2.1
 gateway 2001:db8:08:15::1
 vrf vrf_external
auto vrf_external
iface vrf_external
 vrf-table 1023</pre>
<h3>OpenVPN configuration</h3>
<p>The OpenVPN configuration needs to contain this line: </p>
<pre>bind-dev vrf_external</pre>
<h3>Further reading</h3>
<p>Wikipedia has nice page one VRFs: <i><a rel="nofollow" href="https://en.wikipedia.org/wiki/Virtual_routing_and_forwarding">https://en.wikipedia.org/wiki/Virtual_routing_and_forwarding</a></i> </p>
<p> This talk from the Network Track of FrOSCon 2018 provides an overview about advanced layer 2 and layer 3 features of Linux</p>
<dl>
<dt>&bull;</p>
<dd>Slides: <i><a rel="nofollow" href="https://www.slideshare.net/BarbarossaTM/l2l3-fr-fortgeschrittene-helle-und-dunkle-magie-im-linuxnetzwerkstack">https://www.slideshare.net/BarbarossaTM/l2l3-fr-fortgeschrittene-helle-und-dunkle-magie-im-linuxnetzwerkstack</a></i></p>
<dt>&bull;</p>
<dd>Video (german): <i><a rel="nofollow" href="https://media.ccc.de/v/froscon2018-2247-l2_l3_fur_fortgeschrittene_-_helle_und_dunkle_magie_im_linux-netzwerkstack">https://media.ccc.de/v/froscon2018-2247-l2_l3_fur_fortgeschrittene_-_helle_und_dunkle_magie_im_linux-netzwerkstack</a></i></dl>
<h2>Scripting Integration</h2>
<p>OpenVPN can execute external scripts in various phases of the lifetime of the OpenVPN process.</p>
<h3>Script Order of Execution</h3>
<dl>
<dt>1.</p>
<dd><code>&#8211;up</code> </p>
<p> Executed after TCP/UDP socket bind and TUN/TAP open.</p>
<dt>2.</p>
<dd><code>&#8211;tls-verify</code> </p>
<p> Executed when we have a still untrusted remote peer.</p>
<dt>3.</p>
<dd><code>&#8211;ipchange</code> </p>
<p> Executed after connection authentication, or remote IP address change.</p>
<dt>4.</p>
<dd><code>&#8211;client-connect</code> </p>
<p> Executed in <code>&#8211;mode server</code> mode immediately after client authentication.</p>
<dt>5.</p>
<dd><code>&#8211;route-up</code> </p>
<p> Executed after connection authentication, either immediately after, or some number of seconds after as defined by the <code>&#8211;route-delay</code> option.</p>
<dt>6.</p>
<dd><code>&#8211;route-pre-down</code> </p>
<p> Executed right before the routes are removed.</p>
<dt>7.</p>
<dd><code>&#8211;client-disconnect</code> </p>
<p> Executed in <code>&#8211;mode server</code> mode on client instance shutdown.</p>
<dt>8.</p>
<dd><code>&#8211;down</code> </p>
<p> Executed after TCP/UDP and TUN/TAP close.</p>
<dt>9.</p>
<dd><code>&#8211;learn-address</code> </p>
<p> Executed in <code>&#8211;mode server</code> mode whenever an IPv4 address/route or MAC address is added to OpenVPN&#8217;s internal routing table.</p>
<dt>10.</p>
<dd><code>&#8211;auth-user-pass-verify</code> </p>
<p> Executed in <code>&#8211;mode server</code> mode on new client connections, when the client is still untrusted.</dl>
<h3>Script Hooks</h3>
<dl>
<dt><code>&#8211;auth-user-pass-verify</code><i>&nbsp;args</i></p>
<dd>Require the client to provide a username/password (possibly in addition to a client certificate) for authentication. </p>
<p> Valid syntax: </p>
<pre>auth-user-pass-verify cmd method</pre>
<p>OpenVPN will run command <code>cmd</code> to validate the username/password provided by the client. </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> If <code>method</code> is set to <code>via-env</code>, OpenVPN will call <code>script</code> with the environmental variables <code>username</code> and <code>password</code> set to the username/password strings provided by the client. <i>Beware</i> that this method is insecure on some platforms which make the environment of a process publicly visible to other unprivileged processes. </p>
<p> If <code>method</code> is set to <code>via-file</code>, OpenVPN will write the username and password to the first two lines of a temporary file. The filename will be passed as an argument to <code>script</code>, and the file will be automatically deleted by OpenVPN after the script returns. The location of the temporary file is controlled by the <code>&#8211;tmp-dir</code> option, and will default to the current directory if unspecified. For security, consider setting <code>&#8211;tmp-dir</code> to a volatile storage medium such as <code>/dev/shm</code> (if available) to prevent the username/password file from touching the hard drive. </p>
<p> The script should examine the username and password, returning a success exit code (<code>0</code>) if the client&#8217;s authentication request is to be accepted, or a failure code (<code>1</code>) to reject the client. </p>
<p> This directive is designed to enable a plugin-style interface for extending OpenVPN&#8217;s authentication capabilities. </p>
<p> To protect against a client passing a maliciously formed username or password string, the username string must consist only of these characters: alphanumeric, underbar (&#8216;<code>_</code>&#8216;), dash (&#8216;<code>&#8211;</code>&#8216;), dot (&#8216;<code>.</code>&#8216;), or at (&#8216;<code>@</code>&#8216;). The password string can consist of any printable characters except for CR or LF. Any illegal characters in either the username or password string will be converted to underbar (&#8216;<code>_</code>&#8216;). </p>
<p> Care must be taken by any user-defined scripts to avoid creating a security vulnerability in the way that these strings are handled. Never use these strings in such a way that they might be escaped or evaluated by a shell interpreter. </p>
<p> For a sample script that performs PAM authentication, see <code>sample-scripts/auth-pam.pl</code> in the OpenVPN source distribution.</p>
<dt><code>&#8211;client-connect</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> on client connection. </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> The command is passed the common name and IP address of the just-authenticated client as environmental variables (see environmental variable section below). The command is also passed the pathname of a freshly created temporary file as the last argument (after any arguments specified in <code>cmd</code> ), to be used by the command to pass dynamically generated config file directives back to OpenVPN. </p>
<p> If the script wants to generate a dynamic config file to be applied on the server when the client connects, it should write it to the file named by the last argument. </p>
<p> See the <code>&#8211;client-config-dir</code> option below for options which can be legally used in a dynamically generated config file. </p>
<p> Note that the return value of <code>script</code> is significant. If <code>script</code> returns a non-zero error status, it will cause the client to be disconnected. </p>
<p> If a <code>&#8211;client-connect</code> wants to defer the generating of the configuration then the script needs to use the <code>client_connect_deferred_file</code> and <code>client_connect_config_file</code> environment variables, and write status accordingly into these files. See the <i>Environmental Variables</i> section for more details.</p>
<dt><code>&#8211;client-disconnect</code><i>&nbsp;cmd</i></p>
<dd>Like <code>&#8211;client-connect</code> but called on client instance shutdown. Will not be called unless the <code>&#8211;client-connect</code> script and plugins (if defined) were previously called on this instance with successful (0) status returns. </p>
<p> The exception to this rule is if the <code>&#8211;client-disconnect</code> command or plugins are cascaded, and at least one client-connect function succeeded, then ALL of the client-disconnect functions for scripts and plugins will be called on client instance object deletion, even in cases where some of the related client-connect functions returned an error status. </p>
<p> The <code>&#8211;client-disconnect</code> command is not passed any extra arguments (only those arguments specified in cmd, if any).</p>
<dt><code>&#8211;down</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> after TUN/TAP device close (post <code>&#8211;user</code> UID change and/or <code>&#8211;chroot</code> ). <code>cmd</code> consists of a path to script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> Called with the same parameters and environmental variables as the <code>&#8211;up</code> option above. </p>
<p> Note that if you reduce privileges by using <code>&#8211;user</code> and/or <code>&#8211;group</code>, your <code>&#8211;down</code> script will also run at reduced privilege.</p>
<dt><code>&#8211;down-pre</code></p>
<dd>Call <code>&#8211;down</code> cmd/script before, rather than after, TUN/TAP close.</p>
<dt><code>&#8211;ipchange</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> when our remote ip-address is initially authenticated or changes. </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> When <code>cmd</code> is executed two arguments are appended after any arguments specified in <code>cmd</code> , as follows: </p>
<pre>cmd ip address port number</pre>
<p>Don&#8217;t use <code>&#8211;ipchange</code> in <code>&#8211;mode server</code> mode. Use a <code>&#8211;client-connect</code> script instead. </p>
<p> See the <i>Environmental Variables</i> section below for additional parameters passed as environmental variables. </p>
<p> If you are running in a dynamic IP address environment where the IP addresses of either peer could change without notice, you can use this script, for example, to edit the <code>/etc/hosts</code> file with the current address of the peer. The script will be run every time the remote peer changes its IP address. </p>
<p> Similarly if <i>our</i> IP address changes due to DHCP, we should configure our IP address change script (see man page for <code><a href="/docs/linux/man/8-dhcpcd/">dhcpcd</a></code>(8)) to deliver a <code>SIGHUP</code> or <code>SIGUSR1</code> signal to OpenVPN. OpenVPN will then re-establish a connection with its most recently authenticated peer on its new IP address.</p>
<dt><code>&#8211;learn-address</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> to validate client virtual addresses or routes. </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> Three arguments will be appended to any arguments in <code>cmd</code> as follows:</p>
<dt><code>$1</code> &#8211; [operation]</p>
<dd><code>&quot;add&quot;</code>, <code>&quot;update&quot;</code>, or <code>&quot;delete&quot;</code> based on whether or not the address is being added to, modified, or deleted from OpenVPN&#8217;s internal routing table.</p>
<dt><code>$2</code> &#8211; [address]</p>
<dd>The address being learned or unlearned. This can be an IPv4 address such as <code>&quot;198.162.10.14&quot;</code>, an IPv4 subnet such as <code>&quot;198.162.10.0/24&quot;</code>, or an ethernet MAC address (when <code>&#8211;dev tap</code> is being used) such as <code>&quot;00:FF:01:02:03:04&quot;</code>.</p>
<dt><code>$3</code> &#8211; [common name]</p>
<dd>The common name on the certificate associated with the client linked to this address. Only present for <code>&quot;add&quot;</code> or <code>&quot;update&quot;</code> operations, not <code>&quot;delete&quot;</code>. </p>
<p> On <code>&quot;add&quot;</code> or <code>&quot;update&quot;</code> methods, if the script returns a failure code (non-zero), OpenVPN will reject the address and will not modify its internal routing table. </p>
<p> Normally, the <code>cmd</code> script will use the information provided above to set appropriate firewall entries on the VPN TUN/TAP interface. Since OpenVPN provides the association between virtual IP or MAC address and the client&#8217;s authenticated common name, it allows a user-defined script to configure firewall access policies with regard to the client&#8217;s high-level common name, rather than the low level client virtual addresses.</p>
<dt><code>&#8211;route-up</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> after routes are added, subject to <code>&#8211;route-delay</code>. </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> See the <i>Environmental Variables</i> section below for additional parameters passed as environmental variables.</p>
<dt><code>&#8211;route-pre-down</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> before routes are removed upon disconnection. </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> See the <i>Environmental Variables</i> section below for additional parameters passed as environmental variables.</p>
<dt><code>&#8211;setenv</code><i>&nbsp;args</i></p>
<dd>Set a custom environmental variable <code>name=value</code> to pass to script. </p>
<p> Valid syntaxes: </p>
<pre>setenv name value
setenv FORWARD_COMPATIBLE 1
setenv opt config_option</pre>
<p>By setting <code>FORWARD_COMPATIBLE</code> to <code>1</code>, the config file syntax checking is relaxed so that unknown directives will trigger a warning but not a fatal error, on the assumption that a given unknown directive might be valid in future OpenVPN versions. </p>
<p> This option should be used with caution, as there are good security reasons for having OpenVPN fail if it detects problems in a config file. Having said that, there are valid reasons for wanting new software features to gracefully degrade when encountered by older software versions. </p>
<p> It is also possible to tag a single directive so as not to trigger a fatal error if the directive isn&#8217;t recognized. To do this, prepend the following before the directive: <code>setenv opt</code> </p>
<p> Versions prior to OpenVPN 2.3.3 will always ignore options set with the <code>setenv opt</code> directive. </p>
<p> See also <code>&#8211;ignore-unknown-option</code></p>
<dt><code>&#8211;setenv-safe</code><i>&nbsp;args</i></p>
<dd>Set a custom environmental variable <code>OPENVPN_name</code> to <code>value</code> to pass to scripts. </p>
<p> Valid syntaxes: </p>
<pre>setenv-safe name value</pre>
<p>This directive is designed to be pushed by the server to clients, and the prepending of <code>OPENVPN_</code> to the environmental variable is a safety precaution to prevent a <code>LD_PRELOAD</code> style attack from a malicious or compromised server.</p>
<dt><code>&#8211;tls-verify</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> to verify the X509 name of a pending TLS connection that has otherwise passed all other tests of certification (except for revocation via <code>&#8211;crl-verify</code> directive; the revocation test occurs after the <code>&#8211;tls-verify</code> test). </p>
<p> <code>cmd</code> should return <code>0</code> to allow the TLS handshake to proceed, or <code>1</code> to fail. </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> When <code>cmd</code> is executed two arguments are appended after any arguments specified in <code>cmd</code>, as follows: </p>
<pre>cmd certificate_depth subject</pre>
<p>These arguments are, respectively, the current certificate depth and the X509 subject distinguished name (dn) of the peer. </p>
<p> This feature is useful if the peer you want to trust has a certificate which was signed by a certificate authority who also signed many other certificates, where you don&#8217;t necessarily want to trust all of them, but rather be selective about which peer certificate you will accept. This feature allows you to write a script which will test the X509 name on a certificate and decide whether or not it should be accepted. For a simple perl script which will test the common name field on the certificate, see the file <code>verify-cn</code> in the OpenVPN distribution. </p>
<p> See the <i>Environmental Variables</i> section below for additional parameters passed as environmental variables.</p>
<dt><code>&#8211;up</code><i>&nbsp;cmd</i></p>
<dd>Run command <code>cmd</code> after successful TUN/TAP device open (pre <code>&#8211;user</code> UID change). </p>
<p> <code>cmd</code> consists of a path to a script (or executable program), optionally followed by arguments. The path and arguments may be single- or double-quoted and/or escaped using a backslash, and should be separated by one or more spaces. </p>
<p> The up command is useful for specifying route commands which route IP traffic destined for private subnets which exist at the other end of the VPN connection into the tunnel. </p>
<p> For <code>&#8211;dev tun</code> execute as: </p>
<pre>cmd tun_dev tun_mtu link_mtu ifconfig_local_ip ifconfig_remote_ip [init | restart]</pre>
<p>For <code>&#8211;dev tap</code> execute as: </p>
<pre>cmd tap_dev tap_mtu link_mtu ifconfig_local_ip ifconfig_netmask [init | restart]</pre>
<p>See the <i>Environmental Variables</i> section below for additional parameters passed as environmental variables. </p>
<p> Note that if <code>cmd</code> includes arguments, all OpenVPN-generated arguments will be appended to them to build an argument list with which the executable will be called. </p>
<p> Typically, <code>cmd</code> will run a script to add routes to the tunnel. </p>
<p> Normally the up script is called after the TUN/TAP device is opened. In this context, the last command line parameter passed to the script will be <i>init.</i> If the <code>&#8211;up-restart</code> option is also used, the up script will be called for restarts as well. A restart is considered to be a partial reinitialization of OpenVPN where the TUN/TAP instance is preserved (the <code>&#8211;persist-tun</code> option will enable such preservation). A restart can be generated by a SIGUSR1 signal, a <code>&#8211;ping-restart</code> timeout, or a connection reset when the TCP protocol is enabled with the <code>&#8211;proto</code> option. If a restart occurs, and <code>&#8211;up-restart</code> has been specified, the up script will be called with <i>restart</i> as the last parameter.</p>
<dt><i>NOTE:</i></p>
<dd>On restart, OpenVPN will not pass the full set of environment variables to the script. Namely, everything related to routing and gateways will not be passed, as nothing needs to be done anyway &#8211; all the routing setup is already in place. Additionally, the up-restart script will run with the downgraded UID/GID settings (if configured). </p>
<p> The following standalone example shows how the <code>&#8211;up</code> script can be called in both an initialization and restart context. (<i>NOTE:</i> for security reasons, don&#8217;t run the following example unless UDP port 9999 is blocked by your firewall. Also, the example will run indefinitely, so you should abort with control-c). </p>
<pre>openvpn --dev tun --port 9999 --verb 4 --ping-restart 10 \
 --up 'echo up' --down 'echo down' --persist-tun \
 --up-restart</pre>
<p>Note that OpenVPN also provides the <code>&#8211;ifconfig</code> option to automatically ifconfig the TUN device, eliminating the need to define an <code>&#8211;up</code> script, unless you also want to configure routes in the <code>&#8211;up</code> script. </p>
<p> If <code>&#8211;ifconfig</code> is also specified, OpenVPN will pass the ifconfig local and remote endpoints on the command line to the <code>&#8211;up</code> script so that they can be used to configure routes such as: </p>
<pre>route add -net 10.0.0.0 netmask 255.255.255.0 gw $5</pre>
<dt><code>&#8211;up-delay</code></p>
<dd>Delay TUN/TAP open and possible <code>&#8211;up</code> script execution until after TCP/UDP connection establishment with peer. </p>
<p> In <code>&#8211;proto udp</code> mode, this option normally requires the use of <code>&#8211;ping</code> to allow connection initiation to be sensed in the absence of tunnel data, since UDP is a &quot;connectionless&quot; protocol. </p>
<p> On Windows, this option will delay the TAP-Win32 media state transitioning to &quot;connected&quot; until connection establishment, i.e. the receipt of the first authenticated packet from the peer.</p>
<dt><code>&#8211;up-restart</code></p>
<dd>Enable the <code>&#8211;up</code> and <code>&#8211;down</code> scripts to be called for restarts as well as initial program start. This option is described more fully above in the <code>&#8211;up</code> option documentation.</dl>
<h3>String Types and Remapping</h3>
<p>In certain cases, OpenVPN will perform remapping of characters in strings. Essentially, any characters outside the set of permitted characters for each string type will be converted to underbar (&#8216;_&#8217;).</p>
<dl>
<dt><i>Q: Why is string remapping necessary?</i></p>
<dd>It&#8217;s an important security feature to prevent the malicious coding of strings from untrusted sources to be passed as parameters to scripts, saved in the environment, used as a common name, translated to a filename, etc.</p>
<dt><i>Q: Can string remapping be disabled?</i></p>
<dd>Yes, by using the <code>&#8211;no-name-remapping</code> option, however this should be considered an advanced option. </p>
<p> Here is a brief rundown of OpenVPN&#8217;s current string types and the permitted character class for each string:</p>
<dt><i>X509 Names</i></p>
<dd>Alphanumeric, underbar (&#8216;_&#8217;), dash (&#8216;-&#8216;), dot (&#8216;.&#8217;), at (&#8216;@&#8217;), colon (&#8216;:&#8217;), slash (&#8216;/&#8217;), and equal (&#8216;=&#8217;). Alphanumeric is defined as a character which will cause the C library isalnum() function to return true.</p>
<dt><i>Common Names</i></p>
<dd>Alphanumeric, underbar (&#8216;_&#8217;), dash (&#8216;-&#8216;), dot (&#8216;.&#8217;), and at (&#8216;@&#8217;).</p>
<dt><i>&#8211;auth-user-pass username</i></p>
<dd>Same as Common Name, with one exception: starting with OpenVPN 2.0.1, the username is passed to the <code>OPENVPN_PLUGIN_AUTH_USER_PASS_VERIFY</code> plugin in its raw form, without string remapping.</p>
<dt><i>&#8211;auth-user-pass password</i></p>
<dd>Any &quot;printable&quot; character except CR or LF. Printable is defined to be a character which will cause the C library isprint() function to return true.</p>
<dt><i>&#8211;client-config-dir filename as derived from common name or`username</i></p>
<dd>Alphanumeric, underbar (&#8216;_&#8217;), dash (&#8216;-&#8216;), and dot (&#8216;.&#8217;) except for &quot;.&quot; or &quot;..&quot; as standalone strings. As of v2.0.1-rc6, the at (&#8216;@&#8217;) character has been added as well for compatibility with the common name character class.</p>
<dt><i>Environmental variable names</i></p>
<dd>Alphanumeric or underbar (&#8216;_&#8217;).</p>
<dt><i>Environmental variable values</i></p>
<dd>Any printable character. </p>
<p> For all cases, characters in a string which are not members of the legal character class for that string type will be remapped to underbar (&#8216;_&#8217;).</dl>
<h3>Environmental Variables</h3>
<p>Once set, a variable is persisted indefinitely until it is reset by a new value or a restart, </p>
<p> As of OpenVPN 2.0-beta12, in server mode, environmental variables set by OpenVPN are scoped according to the client objects they are associated with, so there should not be any issues with scripts having access to stale, previously set variables which refer to different client instances.</p>
<dl>
<dt><code>bytes_received</code></p>
<dd>Total number of bytes received from client during VPN session. Set prior to execution of the <code>&#8211;client-disconnect</code> script.</p>
<dt><code>bytes_sent</code></p>
<dd>Total number of bytes sent to client during VPN session. Set prior to execution of the <code>&#8211;client-disconnect</code> script.</p>
<dt><code>client_connect_config_file</code></p>
<dd>The path to the configuration file that should be written to by the <code>&#8211;client-connect</code> script (optional, if per-session configuration is desired). This is the same file name as passed via command line argument on the call to the <code>&#8211;client-connect</code> script.</p>
<dt><code>client_connect_deferred_file</code></p>
<dd>This file can be optionally written to in order to to communicate a status code of the <code>&#8211;client-connect</code> script or plgin. Only the first character in the file is relevant. It must be either <code>1</code> to indicate normal script execution, <code>0</code> indicates an error (in the same way that a non zero exit status does) or <code>2</code> to indicate that the script deferred returning the config file. </p>
<p> For deferred (background) handling, the script or plugin MUST write <code>2</code> to the file to indicate the deferral and then return with exit code <code>0</code> to signal <code>deferred handler started OK</code>. </p>
<p> A background process or similar must then take care of writing the configuration to the file indicated by the <code>client_connect_config_file</code> environment variable and when finished, write the a <code>1</code> to this file (or <code>0</code> in case of an error). </p>
<p> The absence of any character in the file when the script finishes executing is interpreted the same as <code>1</code>. This allows scripts that are not written to support the defer mechanism to be used unmodified.</p>
<dt><code>common_name</code></p>
<dd>The X509 common name of an authenticated client. Set prior to execution of <code>&#8211;client-connect</code>, <code>&#8211;client-disconnect</code> and <code>&#8211;auth-user-pass-verify</code> scripts.</p>
<dt><code>config</code></p>
<dd>Name of first <code>&#8211;config</code> file. Set on program initiation and reset on SIGHUP.</p>
<dt><code>daemon</code></p>
<dd>Set to &quot;1&quot; if the <code>&#8211;daemon</code> directive is specified, or &quot;0&quot; otherwise. Set on program initiation and reset on SIGHUP.</p>
<dt><code>daemon_log_redirect</code></p>
<dd>Set to &quot;1&quot; if the <code>&#8211;log</code> or <code>&#8211;log-append</code> directives are specified, or &quot;0&quot; otherwise. Set on program initiation and reset on SIGHUP.</p>
<dt><code>dev</code></p>
<dd>The actual name of the TUN/TAP device, including a unit number if it exists. Set prior to <code>&#8211;up</code> or <code>&#8211;down</code> script execution.</p>
<dt><code>dev_idx</code></p>
<dd>On Windows, the device index of the TUN/TAP adapter (to be used in netsh.exe calls which sometimes just do not work right with interface names). Set prior to <code>&#8211;up</code> or <code>&#8211;down</code> script execution.</p>
<dt><code>foreign_option_{n}</code></p>
<dd>An option pushed via <code>&#8211;push</code> to a client which does not natively support it, such as <code>&#8211;dhcp-option</code> on a non-Windows system, will be recorded to this environmental variable sequence prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_broadcast</code></p>
<dd>The broadcast address for the virtual ethernet segment which is derived from the <code>&#8211;ifconfig</code> option when <code>&#8211;dev tap</code> is used. Set prior to OpenVPN calling the <code>ifconfig</code> or <code>netsh</code> (windows version of ifconfig) commands which normally occurs prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_ipv6_local</code></p>
<dd>The local VPN endpoint IPv6 address specified in the <code>&#8211;ifconfig-ipv6</code> option (first parameter). Set prior to OpenVPN calling the <code>ifconfig</code> or code:<i>netsh</i> (windows version of ifconfig) commands which normally occurs prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_ipv6_netbits</code></p>
<dd>The prefix length of the IPv6 network on the VPN interface. Derived from the /nnn parameter of the IPv6 address in the <code>&#8211;ifconfig-ipv6</code> option (first parameter). Set prior to OpenVPN calling the <code>ifconfig</code> or <code>netsh</code> (windows version of ifconfig) commands which normally occurs prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_ipv6_remote</code></p>
<dd>The remote VPN endpoint IPv6 address specified in the <code>&#8211;ifconfig-ipv6</code> option (second parameter). Set prior to OpenVPN calling the <code>ifconfig</code> or <code>netsh</code> (windows version of ifconfig) commands which normally occurs prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_local</code></p>
<dd>The local VPN endpoint IP address specified in the <code>&#8211;ifconfig</code> option (first parameter). Set prior to OpenVPN calling the <code>ifconfig</code> or <code>netsh</code> (windows version of ifconfig) commands which normally occurs prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_remote</code></p>
<dd>The remote VPN endpoint IP address specified in the <code>&#8211;ifconfig</code> option (second parameter) when <code>&#8211;dev tun</code> is used. Set prior to OpenVPN calling the <code>ifconfig</code> or <code>netsh</code> (windows version of ifconfig) commands which normally occurs prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_netmask</code></p>
<dd>The subnet mask of the virtual ethernet segment that is specified as the second parameter to <code>&#8211;ifconfig</code> when <code>&#8211;dev tap</code> is being used. Set prior to OpenVPN calling the <code>ifconfig</code> or <code>netsh</code> (windows version of ifconfig) commands which normally occurs prior to <code>&#8211;up</code> script execution.</p>
<dt><code>ifconfig_pool_local_ip</code></p>
<dd>The local virtual IP address for the TUN/TAP tunnel taken from an <code>&#8211;ifconfig-push</code> directive if specified, or otherwise from the ifconfig pool (controlled by the <code>&#8211;ifconfig-pool</code> config file directive). Only set for <code>&#8211;dev tun</code> tunnels. This option is set on the server prior to execution of the <code>&#8211;client-connect</code> and <code>&#8211;client-disconnect</code> scripts.</p>
<dt><code>ifconfig_pool_netmask</code></p>
<dd>The virtual IP netmask for the TUN/TAP tunnel taken from an <code>&#8211;ifconfig-push</code> directive if specified, or otherwise from the ifconfig pool (controlled by the <code>&#8211;ifconfig-pool</code> config file directive). Only set for <code>&#8211;dev tap</code> tunnels. This option is set on the server prior to execution of the <code>&#8211;client-connect</code> and <code>&#8211;client-disconnect</code> scripts.</p>
<dt><code>ifconfig_pool_remote_ip</code></p>
<dd>The remote virtual IP address for the TUN/TAP tunnel taken from an <code>&#8211;ifconfig-push</code> directive if specified, or otherwise from the ifconfig pool (controlled by the <code>&#8211;ifconfig-pool</code> config file directive). This option is set on the server prior to execution of the <code>&#8211;client-connect</code> and <code>&#8211;client-disconnect</code> scripts.</p>
<dt><code>link_mtu</code></p>
<dd>The maximum packet size (not including the IP header) of tunnel data in UDP tunnel transport mode. Set prior to <code>&#8211;up</code> or <code>&#8211;down</code> script execution.</p>
<dt><code>local</code></p>
<dd>The <code>&#8211;local</code> parameter. Set on program initiation and reset on SIGHUP.</p>
<dt><code>local_port</code></p>
<dd>The local port number or name, specified by <code>&#8211;port</code> or <code>&#8211;lport</code>. Set on program initiation and reset on SIGHUP.</p>
<dt><code>password</code></p>
<dd>The password provided by a connecting client. Set prior to <code>&#8211;auth-user-pass-verify</code> script execution only when the <code>via-env</code> modifier is specified, and deleted from the environment after the script returns.</p>
<dt><code>proto</code></p>
<dd>The <code>&#8211;proto</code> parameter. Set on program initiation and reset on SIGHUP.</p>
<dt><code>remote_{n}</code></p>
<dd>The <code>&#8211;remote</code> parameter. Set on program initiation and reset on SIGHUP.</p>
<dt><code>remote_port_{n}</code></p>
<dd>The remote port number, specified by <code>&#8211;port</code> or <code>&#8211;rport</code>. Set on program initiation and reset on SIGHUP.</p>
<dt><code>route_net_gateway</code></p>
<dd>The pre-existing default IP gateway in the system routing table. Set prior to <code>&#8211;up</code> script execution.</p>
<dt><code>route_vpn_gateway</code></p>
<dd>The default gateway used by <code>&#8211;route</code> options, as specified in either the <code>&#8211;route-gateway</code> option or the second parameter to <code>&#8211;ifconfig</code> when <code>&#8211;dev tun</code> is specified. Set prior to <code>&#8211;up</code> script execution.</p>
<dt><code>route_{parm}_{n}</code></p>
<dd>A set of variables which define each route to be added, and are set prior to <code>&#8211;up</code> script execution. </p>
<p> <code>parm</code> will be one of <code>network</code>, <code>netmask&quot;</code>, <code>gateway</code>, or <code>metric</code>. </p>
<p> <code>n</code> is the OpenVPN route number, starting from 1. </p>
<p> If the network or gateway are resolvable DNS names, their IP address translations will be recorded rather than their names as denoted on the command line or configuration file.</p>
<dt><code>route_ipv6_{parm}_{n}</code></p>
<dd>A set of variables which define each IPv6 route to be added, and are set prior to <code>&#8211;up</code> script execution. </p>
<p> <code>parm</code> will be one of <code>network</code>, <code>gateway</code> or <code>metric</code>. <code>route_ipv6_network_{n}</code> contains <code>netmask</code> as <code>/nnn</code>, unlike IPv4 where it is passed in a separate environment variable. </p>
<p> <code>n</code> is the OpenVPN route number, starting from 1. </p>
<p> If the network or gateway are resolvable DNS names, their IP address translations will be recorded rather than their names as denoted on the command line or configuration file.</p>
<dt><code>peer_cert</code></p>
<dd>Temporary file name containing the client certificate upon connection. Useful in conjunction with <code>&#8211;tls-verify</code>.</p>
<dt><code>script_context</code></p>
<dd>Set to &quot;init&quot; or &quot;restart&quot; prior to up/down script execution. For more information, see documentation for <code>&#8211;up</code>.</p>
<dt><code>script_type</code></p>
<dd>Prior to execution of any script, this variable is set to the type of script being run. It can be one of the following: <code>up</code>, <code>down</code>, <code>ipchange</code>, <code>route-up</code>, <code>tls-verify</code>, <code>auth-user-pass-verify</code>, <code>client-connect</code>, <code>client-disconnect</code> or <code>learn-address</code>. Set prior to execution of any script.</p>
<dt><code>signal</code></p>
<dd>The reason for exit or restart. Can be one of <code>sigusr1</code>, <code>sighup</code>, <code>sigterm</code>, <code>sigint</code>, <code>inactive</code> (controlled by <code>&#8211;inactive</code> option), <code>ping-exit</code> (controlled by <code>&#8211;ping-exit</code> option), <code>ping-restart</code> (controlled by <code>&#8211;ping-restart</code> option), <code>connection-reset</code> (triggered on TCP connection reset), <code>error</code> or <code>unknown</code> (unknown signal). This variable is set just prior to down script execution.</p>
<dt><code>time_ascii</code></p>
<dd>Client connection timestamp, formatted as a human-readable time string. Set prior to execution of the <code>&#8211;client-connect</code> script.</p>
<dt><code>time_duration</code></p>
<dd>The duration (in seconds) of the client session which is now disconnecting. Set prior to execution of the <code>&#8211;client-disconnect</code> script.</p>
<dt><code>time_unix</code></p>
<dd>Client connection timestamp, formatted as a unix integer date/time value. Set prior to execution of the <code>&#8211;client-connect</code> script.</p>
<dt><code>tls_digest_{n}</code> / <code>tls_digest_sha256_{n}</code></p>
<dd>Contains the certificate SHA1 / SHA256 fingerprint, where <code>n</code> is the verification level. Only set for TLS connections. Set prior to execution of <code>&#8211;tls-verify</code> script.</p>
<dt><code>tls_id_{n}</code></p>
<dd>A series of certificate fields from the remote peer, where <code>n</code> is the verification level. Only set for TLS connections. Set prior to execution of <code>&#8211;tls-verify</code> script.</p>
<dt><code>tls_serial_{n}</code></p>
<dd>The serial number of the certificate from the remote peer, where <code>n</code> is the verification level. Only set for TLS connections. Set prior to execution of <code>&#8211;tls-verify</code> script. This is in the form of a decimal string like &quot;933971680&quot;, which is suitable for doing serial-based OCSP queries (with OpenSSL, do not prepend &quot;0x&quot; to the string) If something goes wrong while reading the value from the certificate it will be an empty string, so your code should check that. See the <code>contrib/OCSP_check/OCSP_check.sh</code> script for an example.</p>
<dt><code>tls_serial_hex_{n}</code></p>
<dd>Like <code>tls_serial_{n}</code>, but in hex form (e.g. <code>12:34:56:78:9A</code>).</p>
<dt><code>tun_mtu</code></p>
<dd>The MTU of the TUN/TAP device. Set prior to <code>&#8211;up</code> or <code>&#8211;down</code> script execution.</p>
<dt><code>trusted_ip</code> / <code>trusted_ip6</code>)</p>
<dd>Actual IP address of connecting client or peer which has been authenticated. Set prior to execution of <code>&#8211;ipchange</code>, <code>&#8211;client-connect</code> and <code>&#8211;client-disconnect</code> scripts. If using ipv6 endpoints (udp6, tcp6), <code>trusted_ip6</code> will be set instead.</p>
<dt><code>trusted_port</code></p>
<dd>Actual port number of connecting client or peer which has been authenticated. Set prior to execution of <code>&#8211;ipchange</code>, <code>&#8211;client-connect</code> and <code>&#8211;client-disconnect</code> scripts.</p>
<dt><code>untrusted_ip</code> / <code>untrusted_ip6</code></p>
<dd>Actual IP address of connecting client or peer which has not been authenticated yet. Sometimes used to <i>nmap</i> the connecting host in a <code>&#8211;tls-verify</code> script to ensure it is firewalled properly. Set prior to execution of <code>&#8211;tls-verify</code> and <code>&#8211;auth-user-pass-verify</code> scripts. If using ipv6 endpoints (udp6, tcp6), <code>untrusted_ip6</code> will be set instead.</p>
<dt><code>untrusted_port</code></p>
<dd>Actual port number of connecting client or peer which has not been authenticated yet. Set prior to execution of <code>&#8211;tls-verify</code> and <code>&#8211;auth-user-pass-verify</code> scripts.</p>
<dt><code>username</code></p>
<dd>The username provided by a connecting client. Set prior to <code>&#8211;auth-user-pass-verify</code> script execution only when the <code>via-env</code> modifier is specified.</p>
<dt><code>X509_{n}_{subject_field}</code></p>
<dd>An X509 subject field from the remote peer certificate, where <code>n</code> is the verification level. Only set for TLS connections. Set prior to execution of <code>&#8211;tls-verify</code> script. This variable is similar to <code>tls_id_{n}</code> except the component X509 subject fields are broken out, and no string remapping occurs on these field values (except for remapping of control characters to &quot;<code>_</code>&quot;). For example, the following variables would be set on the OpenVPN server using the sample client certificate in sample-keys (client.crt). Note that the verification level is 0 for the client certificate and 1 for the CA certificate. </p>
<pre>X509_0_emailAddress=me [at] myhost.mydomain
X509_0_CN=Test-Client
X509_0_O=OpenVPN-TEST
X509_0_ST=NA
X509_0_C=KG
X509_1_emailAddress=me [at] myhost.mydomain
X509_1_O=OpenVPN-TEST
X509_1_L=BISHKEK
X509_1_ST=NA
X509_1_C=KG</pre>
</dl>
<h3>Management Interface Options</h3>
<p>OpenVPN provides a feature rich socket based management interface for both server and client mode operations.</p>
<dl>
<dt><code>&#8211;management</code><i>&nbsp;args</i></p>
<dd>Enable a management server on a <code>socket-name</code> Unix socket on those platforms supporting it, or on a designated TCP port. </p>
<p> Valid syntaxes: </p>
<pre>management socket-name unix #
management socket-name unix pw-file # (recommended)
management IP port # (INSECURE)
management IP port pw-file #</pre>
<p><code>pw-file</code>, if specified, is a password file where the password must be on first line. Instead of a filename it can use the keyword stdin which will prompt the user for a password to use when OpenVPN is starting. </p>
<p> For unix sockets, the default behaviour is to create a unix domain socket that may be connected to by any process. Use the <code>&#8211;management-client-user</code> and <code>&#8211;management-client-group</code> directives to restrict access. </p>
<p> The management interface provides a special mode where the TCP management link can operate over the tunnel itself. To enable this mode, set IP to <code>tunnel</code>. Tunnel mode will cause the management interface to listen for a TCP connection on the local VPN address of the TUN/TAP interface. </p>
<p> <code>*BEWARE*</code> of enabling the management interface over TCP. In these cases you should <i>ALWAYS</i> make use of <code>pw-file</code> to password protect the management interface. Any user who can connect to this TCP <code>IP:port</code> will be able to manage and control (and interfere with) the OpenVPN process. It is also strongly recommended to set IP to 127.0.0.1 (localhost) to restrict accessibility of the management server to local clients. </p>
<p> While the management port is designed for programmatic control of OpenVPN by other applications, it is possible to telnet to the port, using a telnet client in &quot;raw&quot; mode. Once connected, type <code>help</code> for a list of commands. </p>
<p> For detailed documentation on the management interface, see the <i>management-notes.txt</i> file in the management folder of the OpenVPN source distribution.</p>
<dt><code>&#8211;management-client</code></p>
<dd>Management interface will connect as a TCP/unix domain client to <code>IP:port</code> specified by <code>&#8211;management</code> rather than listen as a TCP server or on a unix domain socket. </p>
<p> If the client connection fails to connect or is disconnected, a SIGTERM signal will be generated causing OpenVPN to quit.</p>
<dt><code>&#8211;management-client-auth</code></p>
<dd>Gives management interface client the responsibility to authenticate clients after their client certificate has been verified. See <code>management-notes.txt</code> in OpenVPN distribution for detailed notes.</p>
<dt><code>&#8211;management-client-group</code><i>&nbsp;g</i></p>
<dd>When the management interface is listening on a unix domain socket, only allow connections from group <code>g</code>.</p>
<dt><code>&#8211;management-client-pf</code></p>
<dd>Management interface clients must specify a packet filter file for each connecting client. See <code>management-notes.txt</code> in OpenVPN distribution for detailed notes.</p>
<dt><code>&#8211;management-client-user</code><i>&nbsp;u</i></p>
<dd>When the management interface is listening on a unix domain socket, only allow connections from user <code>u</code>.</p>
<dt><code>&#8211;management-external-cert</code><i>&nbsp;certificate-hint</i></p>
<dd>Allows usage for external certificate instead of <code>&#8211;cert</code> option (client-only). <code>certificate-hint</code> is an arbitrary string which is passed to a management interface client as an argument of <i>NEED-CERTIFICATE</i> notification. Requires <code>&#8211;management-external-key</code>.</p>
<dt><code>&#8211;management-external-key</code><i>&nbsp;args</i></p>
<dd>Allows usage for external private key file instead of <code>&#8211;key</code> option (client-only). </p>
<p> Valid syntaxes: </p>
<pre>management-external-key
management-external-key nopadding
management-external-key pkcs1
management-external-key nopadding pkcs1</pre>
<p>The optional parameters <code>nopadding</code> and <code>pkcs1</code> signal support for different padding algorithms. See <code>doc/mangement-notes.txt</code> for a complete description of this feature.</p>
<dt><code>&#8211;management-forget-disconnect</code></p>
<dd>Make OpenVPN forget passwords when management session disconnects. </p>
<p> This directive does not affect the <code>&#8211;http-proxy</code> username/password. It is always cached.</p>
<dt><code>&#8211;management-hold</code></p>
<dd>Start OpenVPN in a hibernating state, until a client of the management interface explicitly starts it with the <code>hold release</code> command.</p>
<dt><code>&#8211;management-log-cache</code><i>&nbsp;n</i></p>
<dd>Cache the most recent <code>n</code> lines of log file history for usage by the management channel.</p>
<dt><code>&#8211;management-query-passwords</code></p>
<dd>Query management channel for private key password and <code>&#8211;auth-user-pass</code> username/password. Only query the management channel for inputs which ordinarily would have been queried from the console.</p>
<dt><code>&#8211;management-query-proxy</code></p>
<dd>Query management channel for proxy server information for a specific <code>&#8211;remote</code> (client-only).</p>
<dt><code>&#8211;management-query-remote</code></p>
<dd>Allow management interface to override <code>&#8211;remote</code> directives (client-only).</p>
<dt><code>&#8211;management-signal</code></p>
<dd>Send SIGUSR1 signal to OpenVPN if management session disconnects. This is useful when you wish to disconnect an OpenVPN session on user logoff. For <code>&#8211;management-client</code> this option is not needed since a disconnect will always generate a <code>SIGTERM</code>.</p>
<dt><code>&#8211;management-up-down</code></p>
<dd>Report tunnel up/down events to management interface.</dl>
<h3>Plug-in Interface Options</h3>
<p>OpenVPN can be extended by loading external plug-in modules at runtime. These plug-ins must be prebuilt and adhere to the OpenVPN Plug-In API.</p>
<dl>
<dt><code>&#8211;plugin</code><i>&nbsp;args</i></p>
<dd>Loads an OpenVPN plug-in module. </p>
<p> Valid syntax: </p>
<pre>plugin module-name
plugin module-name &quot;arguments&quot;</pre>
<p>The <code>module-name</code> needs to be the first argument, indicating the plug-in to load. The second argument is an optional init string which will be passed directly to the plug-in. If the init consists of multiple arguments it must be enclosed in double-quotes (&quot;). Multiple plugin modules may be loaded into one OpenVPN process. </p>
<p> The <code>module-name</code> argument can be just a filename or a filename with a relative or absolute path. The format of the filename and path defines if the plug-in will be loaded from a default plug-in directory or outside this directory. </p>
<pre>--plugin path Effective directory used
===================== =============================
 myplug.so DEFAULT_DIR/myplug.so
 subdir/myplug.so DEFAULT_DIR/subdir/myplug.so
 ./subdir/myplug.so CWD/subdir/myplug.so
 /usr/lib/my/plug.so /usr/lib/my/plug.so</pre>
<p><code>DEFAULT_DIR</code> is replaced by the default plug-in directory, which is configured at the build time of OpenVPN. <code>CWD</code> is the current directory where OpenVPN was started or the directory OpenVPN have switched into via the <code>&#8211;cd</code> option before the <code>&#8211;plugin</code> option. </p>
<p> For more information and examples on how to build OpenVPN plug-in modules, see the README file in the <code>plugin</code> folder of the OpenVPN source distribution. </p>
<p> If you are using an RPM install of OpenVPN, see <code>/usr/share/openvpn/plugin</code>. The documentation is in <code>doc</code> and the actual plugin modules are in <code>lib</code>. </p>
<p> Multiple plugin modules can be cascaded, and modules can be used in tandem with scripts. The modules will be called by OpenVPN in the order that they are declared in the config file. If both a plugin and script are configured for the same callback, the script will be called last. If the return code of the module/script controls an authentication function (such as tls-verify, auth-user-pass-verify, or client-connect), then every module and script must return success (<code>0</code>) in order for the connection to be authenticated. </p>
<dt><code>WARNING</code>:</p>
<dd>Plug-ins may do deferred execution, meaning the plug-in will return the control back to the main OpenVPN process and provide the plug-in result later on via a different thread or process. OpenVPN does <code>NOT</code> support multiple authentication plug-ins <code>where more than one plugin</code> tries to do deferred authentication. If this behaviour is detected, OpenVPN will shut down upon first authentication.</dl>
<h3>Windows-Specific Options</h3>
<dl>
<dt><code>&#8211;allow-nonadmin</code><i>&nbsp;TAP-adapter</i></p>
<dd>(Standalone) Set <code>TAP-adapter</code> to allow access from non-administrative accounts. If <code>TAP-adapter</code> is omitted, all TAP adapters on the system will be configured to allow non-admin access. The non-admin access setting will only persist for the length of time that the TAP-Win32 device object and driver remain loaded, and will need to be re-enabled after a reboot, or if the driver is unloaded and reloaded. This directive can only be used by an administrator.</p>
<dt><code>&#8211;block-outside-dns</code></p>
<dd>Block DNS servers on other network adapters to prevent DNS leaks. This option prevents any application from accessing TCP or UDP port 53 except one inside the tunnel. It uses Windows Filtering Platform (WFP) and works on Windows Vista or later. </p>
<p> This option is considered unknown on non-Windows platforms and unsupported on Windows XP, resulting in fatal error. You may want to use <code>&#8211;setenv opt</code> or <code>&#8211;ignore-unknown-option</code> (not suitable for Windows XP) to ignore said error. Note that pushing unknown options from server does not trigger fatal errors.</p>
<dt><code>&#8211;cryptoapicert</code><i>&nbsp;select-string</i></p>
<dd><i>(Windows/OpenSSL Only)</i> Load the certificate and private key from the Windows Certificate System Store. </p>
<p> Use this option instead of <code>&#8211;cert</code> and <code>&#8211;key</code>. </p>
<p> This makes it possible to use any smart card, supported by Windows, but also any kind of certificate, residing in the Cert Store, where you have access to the private key. This option has been tested with a couple of different smart cards (GemSAFE, Cryptoflex, and Swedish Post Office eID) on the client side, and also an imported PKCS12 software certificate on the server side. </p>
<p> To select a certificate, based on a substring search in the certificate&#8217;s subject: </p>
<pre>cryptoapicert &quot;SUBJ:Peter Runestig&quot;</pre>
<p>To select a certificate, based on certificate&#8217;s thumbprint: </p>
<pre>cryptoapicert &quot;THUMB:f6 49 24 41 01 b4 ...&quot;</pre>
<p>The thumbprint hex string can easily be copy-and-pasted from the Windows Certificate Store GUI.</p>
<dt><code>&#8211;dhcp-release</code></p>
<dd>Ask Windows to release the TAP adapter lease on shutdown. This option has no effect now, as it is enabled by default starting with OpenVPN 2.4.1.</p>
<dt><code>&#8211;dhcp-renew</code></p>
<dd>Ask Windows to renew the TAP adapter lease on startup. This option is normally unnecessary, as Windows automatically triggers a DHCP renegotiation on the TAP adapter when it comes up, however if you set the TAP-Win32 adapter Media Status property to &quot;Always Connected&quot;, you may need this flag.</p>
<dt><code>&#8211;ip-win32</code><i>&nbsp;method</i></p>
<dd>When using <code>&#8211;ifconfig</code> on Windows, set the TAP-Win32 adapter IP address and netmask using <code>method</code>. Don&#8217;t use this option unless you are also using <code>&#8211;ifconfig</code>.</p>
<dt><code>manual</code></p>
<dd>Don&#8217;t set the IP address or netmask automatically. Instead output a message to the console telling the user to configure the adapter manually and indicating the IP/netmask which OpenVPN expects the adapter to be set to.</p>
<dt><code>dynamic [offset] [lease-time]</code></p>
<dd>Automatically set the IP address and netmask by replying to DHCP query messages generated by the kernel. This mode is probably the &quot;cleanest&quot; solution for setting the TCP/IP properties since it uses the well-known DHCP protocol. There are, however, two prerequisites for using this mode:</p>
<dt>1.</p>
<dd>The TCP/IP properties for the TAP-Win32 adapter must be set to &quot;Obtain an IP address automatically&quot;, and</p>
<dt>2.</p>
<dd>OpenVPN needs to claim an IP address in the subnet for use as the virtual DHCP server address. </p>
<p> By default in <code>&#8211;dev tap</code> mode, OpenVPN will take the normally unused first address in the subnet. For example, if your subnet is <code>192.168.4.0 netmask 255.255.255.0</code>, then OpenVPN will take the IP address <code>192.168.4.0</code> to use as the virtual DHCP server address. In <code>&#8211;dev tun</code> mode, OpenVPN will cause the DHCP server to masquerade as if it were coming from the remote endpoint. </p>
<p> The optional offset parameter is an integer which is &gt; <code>-256</code> and &lt; <code>256</code> and which defaults to 0. If offset is positive, the DHCP server will masquerade as the IP address at network address + offset. If offset is negative, the DHCP server will masquerade as the IP address at broadcast address + offset. </p>
<p> The Windows <code>ipconfig /all</code> command can be used to show what Windows thinks the DHCP server address is. OpenVPN will &quot;claim&quot; this address, so make sure to use a free address. Having said that, different OpenVPN instantiations, including different ends of the same connection, can share the same virtual DHCP server address. </p>
<p> The <code>lease-time</code> parameter controls the lease time of the DHCP assignment given to the TAP-Win32 adapter, and is denoted in seconds. Normally a very long lease time is preferred because it prevents routes involving the TAP-Win32 adapter from being lost when the system goes to sleep. The default lease time is one year.</p>
<dt><code>netsh</code></p>
<dd>Automatically set the IP address and netmask using the Windows command-line &quot;netsh&quot; command. This method appears to work correctly on Windows XP but not Windows 2000.</p>
<dt><code>ipapi</code></p>
<dd>Automatically set the IP address and netmask using the Windows IP Helper API. This approach does not have ideal semantics, though testing has indicated that it works okay in practice. If you use this option, it is best to leave the TCP/IP properties for the TAP-Win32 adapter in their default state, i.e. &quot;Obtain an IP address automatically.&quot;</p>
<dt><code>adaptive</code> (Default)</p>
<dd>Try <code>dynamic</code> method initially and fail over to <code>netsh</code> if the DHCP negotiation with the TAP-Win32 adapter does not succeed in 20 seconds. Such failures have been known to occur when certain third-party firewall packages installed on the client machine block the DHCP negotiation used by the TAP-Win32 adapter. Note that if the <code>netsh</code> failover occurs, the TAP-Win32 adapter TCP/IP properties will be reset from DHCP to static, and this will cause future OpenVPN startups using the <code>adaptive</code> mode to use <code>netsh</code> immediately, rather than trying <code>dynamic</code> first. </p>
<p> To &quot;unstick&quot; the <code>adaptive</code> mode from using <code>netsh</code>, run OpenVPN at least once using the <code>dynamic</code> mode to restore the TAP-Win32 adapter TCP/IP properties to a DHCP configuration.</p>
<dt><code>&#8211;pause-exit</code></p>
<dd>Put up a &quot;press any key to continue&quot; message on the console prior to OpenVPN program exit. This option is automatically used by the Windows explorer when OpenVPN is run on a configuration file using the right-click explorer menu.</p>
<dt><code>&#8211;register-dns</code></p>
<dd>Run <code>ipconfig /flushdns</code> and <code>ipconfig /registerdns</code> on connection initiation. This is known to kick Windows into recognizing pushed DNS servers.</p>
<dt><code>&#8211;route-method</code><i>&nbsp;m</i></p>
<dd>Which method <code>m</code> to use for adding routes on Windows?</p>
<dt><code>adaptive</code> (default)</p>
<dd>Try IP helper API first. If that fails, fall back to the route.exe shell command.</p>
<dt><code>ipapi</code></p>
<dd>Use IP helper API.</p>
<dt><code>exe</code></p>
<dd>Call the route.exe shell command.</p>
<dt><code>&#8211;service</code><i>&nbsp;args</i></p>
<dd>Should be used when OpenVPN is being automatically executed by another program in such a context that no interaction with the user via display or keyboard is possible. </p>
<p> Valid syntax: </p>
<pre>service exit-event [0|1]</pre>
<p>In general, end-users should never need to explicitly use this option, as it is automatically added by the OpenVPN service wrapper when a given OpenVPN configuration is being run as a service. </p>
<p> <code>exit-event</code> is the name of a Windows global event object, and OpenVPN will continuously monitor the state of this event object and exit when it becomes signaled. </p>
<p> The second parameter indicates the initial state of <code>exit-event</code> and normally defaults to 0. </p>
<p> Multiple OpenVPN processes can be simultaneously executed with the same <code>exit-event</code> parameter. In any case, the controlling process can signal <code>exit-event</code>, causing all such OpenVPN processes to exit. </p>
<p> When executing an OpenVPN process using the <code>&#8211;service</code> directive, OpenVPN will probably not have a console window to output status/error messages, therefore it is useful to use <code>&#8211;log</code> or <code>&#8211;log-append</code> to write these messages to a file.</p>
<dt><code>&#8211;show-adapters</code></p>
<dd>(Standalone) Show available TAP-Win32 adapters which can be selected using the <code>&#8211;dev-node</code> option. On non-Windows systems, the <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) command provides similar functionality.</p>
<dt><code>&#8211;show-net</code></p>
<dd>(Standalone) Show OpenVPN&#8217;s view of the system routing table and network adapter list.</p>
<dt><code>&#8211;show-net-up</code></p>
<dd>Output OpenVPN&#8217;s view of the system routing table and network adapter list to the syslog or log file after the TUN/TAP adapter has been brought up and any routes have been added.</p>
<dt><code>&#8211;show-valid-subnets</code></p>
<dd>(Standalone) Show valid subnets for <code>&#8211;dev tun</code> emulation. Since the TAP-Win32 driver exports an ethernet interface to Windows, and since TUN devices are point-to-point in nature, it is necessary for the TAP-Win32 driver to impose certain constraints on TUN endpoint address selection. </p>
<p> Namely, the point-to-point endpoints used in TUN device emulation must be the middle two addresses of a /30 subnet (netmask 255.255.255.252).</p>
<dt><code>&#8211;tap-sleep</code><i>&nbsp;n</i></p>
<dd>Cause OpenVPN to sleep for <code>n</code> seconds immediately after the TAP-Win32 adapter state is set to &quot;connected&quot;. </p>
<p> This option is intended to be used to troubleshoot problems with the <code>&#8211;ifconfig</code> and <code>&#8211;ip-win32</code> options, and is used to give the TAP-Win32 adapter time to come up before Windows IP Helper API operations are applied to it.</p>
<dt><code>&#8211;win-sys</code><i>&nbsp;path</i></p>
<dd>Set the Windows system directory pathname to use when looking for system executables such as <code>route.exe</code> and <code>netsh.exe</code>. By default, if this directive is not specified, OpenVPN will use the SystemRoot environment variable. </p>
<p> This option has changed behaviour since OpenVPN 2.3. Earlier you had to define <code>&#8211;win-sys env</code> to use the SystemRoot environment variable, otherwise it defaulted to <code>C:\WINDOWS</code>. It is not needed to use the <code>env</code> keyword any more, and it will just be ignored. A warning is logged when this is found in the configuration file.</p>
<dt><code>&#8211;windows-driver</code><i>&nbsp;drv</i></p>
<dd>Specifies which tun driver to use. Values are <code>tap-windows6</code> (default) and <code>wintun</code>. This is a Windows-only option. <code>wintun</code>&quot; requires <code>&#8211;dev tun</code> and the OpenVPN process to run elevated, or be invoked using the Interactive Service.</dl>
<h3>Standalone Debug Options</h3>
<dl>
<dt><code>&#8211;show-gateway</code><i>&nbsp;args</i></p>
<dd>(Standalone) Show current IPv4 and IPv6 default gateway and interface towards the gateway (if the protocol in question is enabled). </p>
<p> Valid syntax: </p>
<pre>--show-gateway
--show-gateway IPv6-target</pre>
<p>For IPv6 this queries the route towards ::/128, or the specified IPv6 target address if passed as argument. For IPv4 on Linux, Windows, MacOS and BSD it looks for a 0.0.0.0/0 route. If there are more specific routes, the result will not always be matching the route of the IPv4 packets to the VPN gateway.</dl>
<h3>Advanced Expert Options</h3>
<p>These are options only required when special tweaking is needed, often used when debugging or testing out special usage scenarios.</p>
<dl>
<dt><code>&#8211;hash-size</code><i>&nbsp;args</i></p>
<dd>Set the size of the real address hash table to <code>r</code> and the virtual address table to <code>v</code>. </p>
<p> Valid syntax: </p>
<pre>hash-size r v</pre>
<p>By default, both tables are sized at 256 buckets.</p>
<dt><code>&#8211;bcast-buffers</code><i>&nbsp;n</i></p>
<dd>Allocate <code>n</code> buffers for broadcast datagrams (default <code>256</code>).</p>
<dt><code>&#8211;persist-local-ip</code></p>
<dd>Preserve initially resolved local IP address and port number across <code>SIGUSR1</code> or <code>&#8211;ping-restart</code> restarts.</p>
<dt><code>&#8211;persist-remote-ip</code></p>
<dd>Preserve most recently authenticated remote IP address and port number across <code>SIGUSR1</code> or <code>&#8211;ping-restart</code> restarts.</p>
<dt><code>&#8211;prng</code><i>&nbsp;args</i></p>
<dd><i>(Advanced)</i> Change the PRNG (Pseudo-random number generator) parameters </p>
<p> Valid syntaxes: </p>
<pre>prng alg
prng alg nsl</pre>
<p>Changes the PRNG to use digest algorithm <code>alg</code> (default <code>sha1</code>), and set <code>nsl</code> (default <code>16</code>) to the size in bytes of the nonce secret length (between 16 and 64). </p>
<p> Set <code>alg</code> to <code>none</code> to disable the PRNG and use the OpenSSL RAND_bytes function instead for all of OpenVPN&#8217;s pseudo-random number needs.</p>
<dt><code>&#8211;rcvbuf</code><i>&nbsp;size</i></p>
<dd>Set the TCP/UDP socket receive buffer size. Defaults to operating system default.</p>
<dt><code>&#8211;shaper</code><i>&nbsp;n</i></p>
<dd>Limit bandwidth of outgoing tunnel data to <code>n</code> bytes per second on the TCP/UDP port. Note that this will only work if mode is set to <code>p2p</code>. If you want to limit the bandwidth in both directions, use this option on both peers. </p>
<p> OpenVPN uses the following algorithm to implement traffic shaping: Given a shaper rate of <code>n</code> bytes per second, after a datagram write of <code>b</code> bytes is queued on the TCP/UDP port, wait a minimum of <code>(b / n)</code> seconds before queuing the next write. </p>
<p> It should be noted that OpenVPN supports multiple tunnels between the same two peers, allowing you to construct full-speed and reduced bandwidth tunnels at the same time, routing low-priority data such as off-site backups over the reduced bandwidth tunnel, and other data over the full-speed tunnel. </p>
<p> Also note that for low bandwidth tunnels (under 1000 bytes per second), you should probably use lower MTU values as well (see above), otherwise the packet latency will grow so large as to trigger timeouts in the TLS layer and TCP connections running over the tunnel. </p>
<p> OpenVPN allows <code>n</code> to be between 100 bytes/sec and 100 Mbytes/sec.</p>
<dt><code>&#8211;sndbuf</code><i>&nbsp;size</i></p>
<dd>Set the TCP/UDP socket send buffer size. Defaults to operating system default.</p>
<dt><code>&#8211;tcp-queue-limit</code><i>&nbsp;n</i></p>
<dd>Maximum number of output packets queued before TCP (default <code>64</code>). </p>
<p> When OpenVPN is tunneling data from a TUN/TAP device to a remote client over a TCP connection, it is possible that the TUN/TAP device might produce data at a faster rate than the TCP connection can support. When the number of output packets queued before sending to the TCP socket reaches this limit for a given client connection, OpenVPN will start to drop outgoing packets directed at this client.</p>
<dt><code>&#8211;txqueuelen</code><i>&nbsp;n</i></p>
<dd><i>(Linux only)</i> Set the TX queue length on the TUN/TAP interface. Currently defaults to operating system default.</dl>
<h2>Unsupported Options</h2>
<p>Options listed in this section have been removed from OpenVPN and are no longer supported</p>
<dl>
<dt><code>&#8211;client-cert-not-required</code></p>
<dd>Removed in OpenVPN 2.5. This should be replaxed with <code>&#8211;verify-client-cert none</code>.</p>
<dt><code>&#8211;ifconfig-pool-linear</code></p>
<dd>Removed in OpenVPN 2.5. This should be replaced with <code>&#8211;topology p2p</code>.</p>
<dt><code>&#8211;key-method</code></p>
<dd>Removed in OpenVPN 2.5. This option should not be used, as using the old <code>key-method</code> weakens the VPN tunnel security. The old <code>key-method</code> was also only needed when the remote side was older than OpenVPN 2.0.</p>
<dt><code>&#8211;no-iv</code></p>
<dd>Removed in OpenVPN 2.5. This option should not be used as it weakens the VPN tunnel security. This has been a NOOP option since OpenVPN 2.4.</p>
<dt><code>&#8211;no-replay</code></p>
<dd>Removed in OpenVPN 2.5. This option should not be used as it weakens the VPN tunnel security.</p>
<dt><code>&#8211;ns-cert-type</code></p>
<dd>Removed in OpenVPN 2.5. The <code>nsCertType</code> field is no longer supported in recent SSL/TLS libraries. If your certificates does not include <i>key usage</i> and <i>extended key usage</i> fields, they must be upgraded and the <code>&#8211;remote-cert-tls</code> option should be used instead.</dl>
<h2>Connection Profiles</h2>
<p>Client configuration files may contain multiple remote servers which it will attempt to connect against. But there are some configuration options which are related to specific <code>&#8211;remote</code> options. For these use cases, connection profiles are the solution. </p>
<p> By enacpulating the <code>&#8211;remote</code> option and related options within <code>&lt;connection&gt;</code> and <code>&lt;/connection&gt;</code>, these options are handled as a group. </p>
<p> An OpenVPN client will try each connection profile sequentially until it achieves a successful connection. </p>
<p> <code>&#8211;remote-random</code> can be used to initially &quot;scramble&quot; the connection list. </p>
<p> Here is an example of connection profile usage: </p>
<pre>client
dev tun
&lt;connection&gt;
remote 198.19.34.56 1194 udp
&lt;/connection&gt;
&lt;connection&gt;
remote 198.19.34.56 443 tcp
&lt;/connection&gt;
&lt;connection&gt;
remote 198.19.34.56 443 tcp
http-proxy 192.168.0.8 8080
&lt;/connection&gt;
&lt;connection&gt;
remote 198.19.36.99 443 tcp
http-proxy 192.168.0.8 8080
&lt;/connection&gt;
persist-key
persist-tun
pkcs12 client.p12
remote-cert-tls server
verb 3</pre>
<p>First we try to connect to a server at 198.19.34.56:1194 using UDP. If that fails, we then try to connect to 198.19.34.56:443 using TCP. If that also fails, then try connecting through an HTTP proxy at 192.168.0.8:8080 to 198.19.34.56:443 using TCP. Finally, try to connect through the same proxy to a server at 198.19.36.99:443 using TCP. </p>
<p> The following OpenVPN options may be used inside of a <code>&lt;connection&gt;</code> block: </p>
<p> <code>bind</code>, <code>connect-retry</code>, <code>connect-retry-max</code>, <code>connect-timeout</code>, <code>explicit-exit-notify</code>, <code>float</code>, <code>fragment</code>, <code>http-proxy</code>, <code>http-proxy-option</code>, <code>key-direction</code>, <code>link-mtu</code>, <code>local</code>, <code>lport</code>, <code>mssfix</code>, <code>mtu-disc</code>, <code>nobind</code>, <code>port</code>, <code>proto</code>, <code>remote</code>, <code>rport</code>, <code>socks-proxy</code>, <code>tls-auth</code>, <code>tls-crypt</code>, <code>tun-mtu and</code>, <code>tun-mtu-extra</code>. </p>
<p> A defaulting mechanism exists for specifying options to apply to all <code>&lt;connection&gt;</code> profiles. If any of the above options (with the exception of <code>remote</code> ) appear outside of a <code>&lt;connection&gt;</code> block, but in a configuration file which has one or more <code>&lt;connection&gt;</code> blocks, the option setting will be used as a default for <code>&lt;connection&gt;</code> blocks which follow it in the configuration file. </p>
<p> For example, suppose the <code>nobind</code> option were placed in the sample configuration file above, near the top of the file, before the first <code>&lt;connection&gt;</code> block. The effect would be as if <code>nobind</code> were declared in all <code>&lt;connection&gt;</code> blocks below it.</p>
<h2>Inline File Support</h2>
<p>OpenVPN allows including files in the main configuration for the <code>&#8211;ca</code>, <code>&#8211;cert</code>, <code>&#8211;dh</code>, <code>&#8211;extra-certs</code>, <code>&#8211;key</code>, <code>&#8211;pkcs12</code>, <code>&#8211;secret</code>, <code>&#8211;crl-verify</code>, <code>&#8211;http-proxy-user-pass</code>, <code>&#8211;tls-auth</code>, <code>&#8211;auth-gen-token-secret</code>, <code>&#8211;tls-crypt</code> and <code>&#8211;tls-crypt-v2</code> options. </p>
<p> Each inline file started by the line <code>&lt;option&gt;</code> and ended by the line <code>&lt;/option&gt;</code> </p>
<p> Here is an example of an inline file usage </p>
<pre>&lt;cert&gt;
-----BEGIN CERTIFICATE-----
[...]
-----END CERTIFICATE-----
&lt;/cert&gt;</pre>
<p>When using the inline file feature with <code>&#8211;pkcs12</code> the inline file has to be base64 encoded. Encoding of a .p12 file into base64 can be done for example with OpenSSL by running <code>openssl base64 -in input.p12</code></p>
<h2>Signals</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd>Cause OpenVPN to close all TUN/TAP and network connections, restart, re-read the configuration file (if any), and reopen TUN/TAP and network connections.</p>
<dt><code>SIGUSR1</code></p>
<dd>Like <code>SIGHUP`</code>, except don&#8217;t re-read configuration file, and possibly don&#8217;t close and reopen TUN/TAP device, re-read key files, preserve local IP address/port, or preserve most recently authenticated remote IP address/port based on <code>&#8211;persist-tun</code>, <code>&#8211;persist-key</code>, <code>&#8211;persist-local-ip</code> and <code>&#8211;persist-remote-ip</code> options respectively (see above). </p>
<p> This signal may also be internally generated by a timeout condition, governed by the <code>&#8211;ping-restart</code> option. </p>
<p> This signal, when combined with <code>&#8211;persist-remote-ip</code>, may be sent when the underlying parameters of the host&#8217;s network interface change such as when the host is a DHCP client and is assigned a new IP address. See <code>&#8211;ipchange</code> for more information.</p>
<dt><code>SIGUSR2</code></p>
<dd>Causes OpenVPN to display its current statistics (to the syslog file if <code>&#8211;daemon</code> is used, or stdout otherwise).</p>
<dt><code>SIGINT</code>, <code>SIGTERM</code></p>
<dd>Causes OpenVPN to exit gracefully.</dl>
<h2>Faq</h2>
<p><i><a rel="nofollow" href="https://community.openvpn.net/openvpn/wiki/FAQ">https://community.openvpn.net/openvpn/wiki/FAQ</a></i></p>
<h2>Howto</h2>
<p>For a more comprehensive guide to setting up OpenVPN in a production setting, see the OpenVPN HOWTO at <i><a rel="nofollow" href="https://openvpn.net/community-resources/how-to/">https://openvpn.net/community-resources/how-to/</a></i></p>
<h2>Protocol</h2>
<p>For a description of OpenVPN&#8217;s underlying protocol, see <i><a rel="nofollow" href="https://openvpn.net/community-resources/openvpn-protocol/">https://openvpn.net/community-resources/openvpn-protocol/</a></i></p>
<h2>Web</h2>
<p>OpenVPN&#8217;s web site is at <i><a rel="nofollow" href="https://openvpn.net/">https://openvpn.net/</a></i> </p>
<p> Go here to download the latest version of OpenVPN, subscribe to the mailing lists, read the mailing list archives, or browse the SVN repository.</p>
<h2>Bugs</h2>
<p>Report all bugs to the OpenVPN team <i>info [at] openvpn.net</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-openvpn-examples/">openvpn-examples</a></code>(5), <code><a href="/docs/linux/man/8-dhcpcd/">dhcpcd</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1), <code><a href="/docs/linux/man/8-route/">route</a></code>(8), <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1) <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1)</p>
<h2>Notes</h2>
<p>This product includes software developed by the OpenSSL Project (<i><a rel="nofollow" href="https://www.openssl.org/">https://www.openssl.org/</a></i>) </p>
<p> For more information on the TLS protocol, see <i><a rel="nofollow" href="http://www.ietf.org/rfc/rfc2246.txt">http://www.ietf.org/rfc/rfc2246.txt</a></i> </p>
<p> For more information on the LZO real-time compression library see <i><a rel="nofollow" href="https://www.oberhumer.com/opensource/lzo/">https://www.oberhumer.com/opensource/lzo/</a></i></p>
<h2>Copyright</h2>
<p>Copyright (C) 2002-2020 OpenVPN Inc This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation.</p>
<h2>Authors</h2>
<p>James Yonan <i>james [at] openvpn.net</i></p>
