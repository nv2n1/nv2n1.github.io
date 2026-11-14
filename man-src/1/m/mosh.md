---
title: "mosh(1)"
name: "mosh"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mosh/"
description: "mosh – mobile shell with roaming and intelligent local echo"
---

<h2 class="name">NAME</h2>
<p> mosh &#8211; mobile shell with roaming and intelligent local echo </p>
<h2>SYNOPSIS</h2>
<p> <code>mosh</code> [<i>options</i>] [&#8211;] [user@]host [command&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>mosh</code> (mobile shell) is a remote terminal application that supports intermittent connectivity, allows roaming, and provides speculative local echo and line editing of user keystrokes. </p>
<p> Compared with <code>ssh</code>, <code>mosh</code> is more robust &#8212; its connections stay up across sleeps and changes in the client&#8217;s IP address &#8212; and more responsive, because the protocol is tolerant of packet loss and the client can echo most keystrokes immediately, without waiting for a network round-trip. </p>
<p> <code>mosh</code> uses <code>ssh</code> to establish a connection to the remote host and authenticate with existing means (e.g., public-key authentication or a password). <code>mosh</code> executes the unprivileged <code>mosh-server</code> helper program on the server, then closes the SSH connection and starts the <code>mosh-client</code>, which establishes a long-lived datagram connection over UDP. </p>
<p> To improve responsiveness, <code>mosh</code> runs a predictive model of the server&#8217;s behavior in the background, trying to guess the effect of each keystroke on the screen. It makes predictions for normal typing, backspace, and the left- and right-arrow keys. When it is confident, <code>mosh</code> displays the predictions without waiting for the server. The predictive model must prove itself anew on each row of the terminal and after each control character, so <code>mosh</code> avoids echoing passwords or non-echoing editor commands. </p>
<p> By default, <code>mosh</code> shows its predictions only on high-latency connections and to smooth out network glitches. (On longer-latency links, the predicted cells are underlined until confirmed by the server.) Occasional echo mistakes are corrected within a network round-trip and do not cause lasting effect. </p>
<p> <code>mosh</code> does not support X forwarding or the non-interactive uses of SSH, including port forwarding or sshfs. <code>mosh</code> works through typical client-side network address translators but requires UDP to pass between client and server. By default, <code>mosh</code> uses the ports between 60000 and 61000, but allows the user to request a particular UDP port instead. </p>
<p> Currently, <code>mosh</code> has limited support for IPv6, dual-stack networks, and servers with multiple addresses. At session start, it will select a single IPv4 or IPv6 server address to connect to for the lifetime of the session. </p>
<p> <code>mosh</code> will do its best to arrange a UTF-8 character set locale on the client and server. The client must have locale-related environment variables that specify UTF-8. <code>mosh</code> will pass these client variables to the <code>mosh-server</code> on its command line, but in most cases they will not need to be used. <code>mosh-server</code> first attempts to use its own locale-related environment variables, which come from the system default configuration (sometimes /etc/default/locale) or from having been passed over the SSH connection. But if these variables don&#8217;t call for the use of UTF-8, <code>mosh-server</code> will apply the locale-related environment variables from the client and try again. </p>
<h2>OPTIONS</h2>
<p> Options named <code> &#8211;experimental-*</code> are subject to change or removal in future versions of Mosh; their design or function is not yet final. </p>
<dl>
<dt><i>command</i></p>
<dd> Command to run on remote host. By default, <code>mosh</code> executes a login shell. </p>
<dt><code>&#8211;client=</code><i>PATH</i></p>
<dd> path to client helper on local machine (default: &quot;mosh-client&quot;) </p>
<dt><code>&#8211;server=</code><i>COMMAND</i></p>
<dd> command to run server helper on remote machine (default: &quot;mosh-server&quot;) </p>
<p> The server helper is unprivileged and can be installed in the user&#8217;s home directory. </p>
<p> This option can be used to set environment variables for the server by using the <code><a href="/docs/linux/man/1-env/">env</a></code>(1) command to wrap the actual server command. See <code><a href="/docs/linux/man/1-mosh-server/">mosh-server</a></code>(1) for available environment variables. </p>
<dt><code>&#8211;ssh=</code><i>COMMAND</i></p>
<dd> OpenSSH command to remotely execute mosh-server on remote machine (default: &quot;ssh&quot;) </p>
<p> An alternate ssh port can be specified with, <i>e.g.</i>, &#8211;ssh=&quot;ssh -p 2222&quot;. </p>
<dt><code>&#8211;predict=</code><i>WHEN</i></p>
<dd> Controls use of speculative local echo. WHEN defaults to `adaptive&#8217; (show predictions on slower links and to smooth out network glitches) and can also be `always` or `never&#8217;. </p>
<p> The MOSH_PREDICTION_DISPLAY environment variable controls this setting permanently and can adopt the same three values. </p>
<p> Even on `always&#8217;, <code>mosh</code> will only show predictions when it is confident. This generally means a previous prediction on the same row of the terminal has been confirmed by the server, without any intervening control character keystrokes. </p>
<dt><code>-a</code></p>
<dd> Synonym for &#8211;predict=always </p>
<dt><code>-n</code></p>
<dd> Synonym for &#8211;predict=never </p>
<dt><code>&#8211;family=inet</code></p>
<dd> Only use IPv4 for the SSH connection and Mosh session. </p>
<dt><code>&#8211;family=inet6</code></p>
<dd> Only use IPv6 for the SSH connection and Mosh session. This and the following modes require Perl&#8217;s IO::Socket::IP or IO::Socket::INET6 modules. </p>
<dt><code>&#8211;family=auto</code></p>
<dd> Autodetect IPv4 or IPv6 for hosts that only have addresses in a single family. Hosts with both IPv4 and IPv6 addresses will raise an error, and require re-invocation of <code>mosh</code> with another <code>&#8211;family</code> option. </p>
<dt><code>&#8211;family=all</code></p>
<dd> Choose an address from all available IPv4 or IPv6 address, even for dual-stack hosts. This is the most convenient option, but requires dual-stack connectivity, and Mosh 1.2.5 or later on the server, when roaming with dual-stack servers. </p>
<dt><code>&#8211;family=prefer-inet</code></p>
<dd> Similar to <code>&#8211;family=all</code>, but attempt connects to the IPv4 addresses first. This is the default. </p>
<dt><code>&#8211;family=prefer-inet6</code></p>
<dd> Similar to <code>&#8211;family=all</code>, but attempt connects to the IPv6 addresses first. </p>
<dt><code>-4</code></p>
<dd> Synonym for &#8211;family=inet </p>
<dt><code>-6</code></p>
<dd> Synonym for &#8211;family=inet6 </p>
<dt><code>-p </code><i>PORT</i>[:<i>PORT2</i>], &#8211;port=<i>PORT</i>[:<i>PORT2</i>]</p>
<dd> Use a particular server-side UDP port or port range, for example, if this is the only port that is forwarded through a firewall to the server. Otherwise, <code>mosh</code> will choose a port between 60000 and 61000. </p>
<dt><code>&#8211;bind-server={ssh|any|</code><i>IP</i>}</p>
<dd> Control the IP address that the <code>mosh-server</code> binds to. </p>
<p> The default is `ssh&#8217;, in which case the server will reply from the IP address that the SSH connection came from (as found in the <code>SSH_CONNECTION</code> environment variable). This is useful for multihomed servers. </p>
<p> With &#8211;bind-server=any, the server will reply on the default interface and will not bind to a particular IP address. This can be useful if the connection is made through <code>sslh</code> or another tool that makes the SSH connection appear to come from localhost. </p>
<p> With &#8211;bind-server=<i>IP</i>, the server will attempt to bind to the specified IP address. </p>
<dt><code>&#8211;no-init</code></p>
<dd> Do not send the <code>smcup</code> initialization string and <code>rmcup</code> deinitialization string to the client&#8217;s terminal. On many terminals this disables alternate screen mode. </p>
<dt><code>&#8211;local</code></p>
<dd> Invoke <code>mosh-server</code> locally, without using <code>ssh</code>. This option requires the <code>host</code> argument to be a local, numeric IPv4/IPv6 address. This option is useful for testing. </p>
<dt><code>&#8211;experimental-remote-ip={proxy|local|remote}</code></p>
<dd> Select the method used to discover the IP address that the <code>mosh-client</code> connects to. </p>
<p> The default is <code>proxy</code>, which uses SSH&#8217;s <code>&#8211;ssh-proxy-command</code> option to generate and report the exact address that <code>ssh</code> uses to connect to the remote host. This option is generally the most compatible with hosts and other options configured in <code>ssh</code> configuration files. However, this may not work for some configurations, or for environments where a <code>ssh</code> bastion host forwards to a remote machine. It only works with <code>OpenSSH</code>. </p>
<p> With <code>remote</code>, the server&#8217;s <code>SSH_CONNECTION</code> environment variable will be used. This is useful for environments where <code>ssh</code> forwarding is used, or the <code>&#8211;ssh-proxy-command</code> option is used for other purposes. </p>
<p> With <code>local</code>, Mosh resolves the hostname given on its command line, and uses that address for both <code>ssh</code> and Mosh connections. This option ignores any configuration in <code>ssh_config</code> for the same hostname. </p>
</dl>
<h2>ESCAPE SEQUENCES</h2>
<p> The default escape character used by Mosh is ASCII RS (decimal 30). This is typically typed as <code>Ctrl-^</code> or <code>Ctrl-Shift-6</code>, on US English keyboards. Users of non-English keyboards may find it difficult or impossible to type the default escape character, and may need to change the escape character. See the description of MOSH_ESCAPE_KEY, below. In this description, the configured escape character is represented as <code>Esc</code>. </p>
<p> There are two slightly different modes for escape sequences, depending whether the escape character is printable or not. </p>
<p> If the escape character is a printable character, it must be prefixed with a newline, similar to <code>OpenSSH</code>. To send the escape character itself, type it twice. If the escape character is set to <code>~</code>, <code>mosh</code> will behave much like <code>OpenSSH</code>. </p>
<p> If the escape character is a non-printable control character, no prefix is used and the escape character is recognized at any time. To send the escape character itself, type the escape character, then its corresponding ASCII character (for <code>Ctrl-^</code> you would type <code>^</code>, for <code>Ctrl-B</code> you would type <code>B</code>). </p>
<p> The escape sequence to shut down the connection is <code>Esc .</code>. The sequence <code>Esc Ctrl-Z</code> suspends the client. Any other sequence passes both characters through to the server. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> These variables are not actually interpreted by <code><a href="/docs/linux/man/1-mosh/">mosh</a></code>(1) itself, but are passed through to <code><a href="/docs/linux/man/1-mosh-server/">mosh-server</a></code>(1). They are described here for ease of use. </p>
<dl>
<dt><code>MOSH_ESCAPE_KEY</code></p>
<dd> When set, this configures the escape character used for local commands. The escape character may be set to any ASCII character in the range 1-127. The variable must be set with a single literal ASCII character. Control characters are set with the actual ASCII control character, not with a printable representation such as &quot;^B&quot;. </p>
<dt><code>MOSH_PREDICTION_DISPLAY</code></p>
<dd> Controls local echo as described above. The command-line flag overrides this variable. </p>
<dt><code>MOSH_TITLE_NOPREFIX</code></p>
<dd> When set, inhibits prepending &quot;[mosh]&quot; to window title. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mosh-client/">mosh-client</a></code>(1), <code><a href="/docs/linux/man/1-mosh-server/">mosh-server</a></code>(1). </p>
<p> Project home page: <i><a rel="nofollow" href="http://mosh.mit.edu">http://mosh.mit.edu</a></i> </p>
<h2>AUTHOR</h2>
<p> mosh was written by Keith Winstein &lt;mosh-devel [at] mit.edu&gt;.</p>
<h2>BUGS</h2>
<p> Please report bugs to <i>mosh-devel [at] mit.edu</i>. Users may also subscribe to the <i>mosh-users [at] mit.edu</i> mailing list, at<br />
 <i><a rel="nofollow" href="http://mailman.mit.edu/mailman/listinfo/mosh-users">http://mailman.mit.edu/mailman/listinfo/mosh-users</a></i> </p>
<h2>Index</h2>
