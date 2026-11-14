---
title: "plink(1)"
name: "plink"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plink/"
description: "plink – PuTTY link, command line network connection tool"
---

<h2>NAME</h2>
<p> <code>plink</code> &#8211; PuTTY link, command line network connection tool</p>
<h2>SYNOPSIS</h2>
<pre><code>
plink &amp;nbsp;
[options] &amp; nbsp;
[user @] host &amp;nbsp;
[command]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>plink</code> is a network connection tool supporting several protocols.</p>
<h2>OPTIONS</h2>
<p> The command-line options supported by <code>plink</code> are:</p>
<dl>
<dt><code>-V</code></p>
<dd> Show version information and exit.</p>
<dt><code>-pgpfp</code></p>
<dd> Display the fingerprints of the PuTTY PGP Master Keys and exit, to aid in verifying new files released by the PuTTY team.</p>
<dt><code>-v</code></p>
<dd> Show verbose messages.</p>
<dt><code>-load</code> <i>session</i></p>
<dd> Load settings from saved session.</p>
<dt><code>-ssh</code></p>
<dd> Force use of SSH protocol (default).</p>
<dt><code>-telnet</code></p>
<dd> Force use of Telnet protocol.</p>
<dt><code>-rlogin</code></p>
<dd> Force use of rlogin protocol.</p>
<dt><code>-raw</code></p>
<dd> Force raw mode.</p>
<dt><code>-serial</code></p>
<dd> Force serial mode.</p>
<dt><code>-P</code> <i>port</i></p>
<dd> Connect to port <i>port</i>.</p>
<dt><code>-l</code> <i>user</i></p>
<dd> Set remote username to <i>user</i>.</p>
<dt><code>-m</code> <i>path</i></p>
<dd> Read remote command(s) from local file <i>path</i>.</p>
<dt><code>-batch</code></p>
<dd> Disable interactive prompts.</p>
<dt><code>-pw</code> <i>password</i></p>
<dd> Set remote password to <i>password</i>. <i>CAUTION:</i> this will likely make the password visible to other users of the local machine (via commands such as `<code>w</code>&#8216;).</p>
<dt><code>-L</code> <code>[</code><i>srcaddr</i><code>:]</code><i>srcport</i><code>:</code><i>desthost</i><code>:</code><i>destport</i></p>
<dd> Set up a local port forwarding: listen on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and forward any connections over the SSH connection to the destination address <i>desthost</i>:<i>destport</i>. Only works in SSH.</p>
<dt><code>-R</code> <code>[</code><i>srcaddr</i><code>:]</code><i>srcport</i><code>:</code><i>desthost</i><code>:</code><i>destport</i></p>
<dd> Set up a remote port forwarding: ask the SSH server to listen on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and to forward any connections back over the SSH connection where the client will pass them on to the destination address <i>desthost</i>:<i>destport</i>. Only works in SSH.</p>
<dt><code>-D</code> [<i>srcaddr</i>:]<i>srcport</i></p>
<dd> Set up dynamic port forwarding. The client listens on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and implements a SOCKS server. So you can point SOCKS-aware applications at this port and they will automatically use the SSH connection to tunnel all their connections. Only works in SSH.</p>
<dt><code>-X</code></p>
<dd> Enable X11 forwarding.</p>
<dt><code>-x</code></p>
<dd> Disable X11 forwarding (default).</p>
<dt><code>-A</code></p>
<dd> Enable agent forwarding.</p>
<dt><code>-a</code></p>
<dd> Disable agent forwarding (default).</p>
<dt><code>-t</code></p>
<dd> Enable pty allocation (default if a command is NOT specified).</p>
<dt><code>-T</code></p>
<dd> Disable pty allocation (default if a command is specified).</p>
<dt><code>-1</code></p>
<dd> Force use of SSH protocol version 1.</p>
<dt><code>-2</code></p>
<dd> Force use of SSH protocol version 2.</p>
<dt><code>-C</code></p>
<dd> Enable SSH compression.</p>
<dt><code>-i</code> <i>path</i></p>
<dd> Private key file for authentication.</p>
<dt><code>-s</code></p>
<dd> Remote command is SSH subsystem (SSH-2 only).</p>
<dt><code>-N</code></p>
<dd> Don&#8217;t start a remote command or shell at all (SSH-2 only).</p>
<dt><code>-sercfg</code> <i>configuration-string</i></p>
<dd> Specify the configuration parameters for the serial port, in <code>-serial</code> mode. <i>configuration-string</i> should be a comma-separated list of configuration parameters as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&bull;</code></p>
<dd> Any single digit from 5 to 9 sets the number of data bits.</p>
<dt><code>&bull;</code></p>
<dd> `<code>1</code>&#8216;, `<code>1.5</code>&#8216; or `<code>2</code>&#8216; sets the number of stop bits.</p>
<dt><code>&bull;</code></p>
<dd> Any other numeric string is interpreted as a baud rate.</p>
<dt><code>&bull;</code></p>
<dd> A single lower-case letter specifies the parity: `<code>n</code>&#8216; for none, `<code>o</code>&#8216; for odd, `<code>e</code>&#8216; for even, `<code>m</code>&#8216; for mark and `<code>s</code>&#8216; for space.</p>
<dt><code>&bull;</code></p>
<dd> A single upper-case letter specifies the flow control: `<code>N</code>&#8216; for none, `<code>X</code>&#8216; for XON/XOFF, `<code>R</code>&#8216; for RTS/CTS and `<code>D</code>&#8216; for DSR/DTR.</dl>
</dl>
</dl>
<h2>MORE INFORMATION</h2>
<p> For more information on plink, it&#8217;s probably best to go and look at the manual on the PuTTY web page: </p>
<p> <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">http://www.chiark.greenend.org.uk/~sgtatham/putty/</a></code></p>
<h2>BUGS</h2>
<p> This man page isn&#8217;t terribly complete. See the above web link for better documentation. </p>
<h2>Index</h2>
