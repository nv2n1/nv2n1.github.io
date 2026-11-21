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
<dt><code>-V</code></dt>
<dd> Show version information and exit.</dd>
<dt><code>-pgpfp</code></dt>
<dd> Display the fingerprints of the PuTTY PGP Master Keys and exit, to aid in verifying new files released by the PuTTY team.</dd>
<dt><code>-v</code></dt>
<dd> Show verbose messages.</dd>
<dt><code>-load</code> <i>session</i></dt>
<dd> Load settings from saved session.</dd>
<dt><code>-ssh</code></dt>
<dd> Force use of SSH protocol (default).</dd>
<dt><code>-telnet</code></dt>
<dd> Force use of Telnet protocol.</dd>
<dt><code>-rlogin</code></dt>
<dd> Force use of rlogin protocol.</dd>
<dt><code>-raw</code></dt>
<dd> Force raw mode.</dd>
<dt><code>-serial</code></dt>
<dd> Force serial mode.</dd>
<dt><code>-P</code> <i>port</i></dt>
<dd> Connect to port <i>port</i>.</dd>
<dt><code>-l</code> <i>user</i></dt>
<dd> Set remote username to <i>user</i>.</dd>
<dt><code>-m</code> <i>path</i></dt>
<dd> Read remote command(s) from local file <i>path</i>.</dd>
<dt><code>-batch</code></dt>
<dd> Disable interactive prompts.</dd>
<dt><code>-pw</code> <i>password</i></dt>
<dd> Set remote password to <i>password</i>. <i>CAUTION:</i> this will likely make the password visible to other users of the local machine (via commands such as `<code>w</code>&#8216;).</dd>
<dt><code>-L</code> <code>[</code><i>srcaddr</i><code>:]</code><i>srcport</i><code>:</code><i>desthost</i><code>:</code><i>destport</i></dt>
<dd> Set up a local port forwarding: listen on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and forward any connections over the SSH connection to the destination address <i>desthost</i>:<i>destport</i>. Only works in SSH.</dd>
<dt><code>-R</code> <code>[</code><i>srcaddr</i><code>:]</code><i>srcport</i><code>:</code><i>desthost</i><code>:</code><i>destport</i></dt>
<dd> Set up a remote port forwarding: ask the SSH server to listen on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and to forward any connections back over the SSH connection where the client will pass them on to the destination address <i>desthost</i>:<i>destport</i>. Only works in SSH.</dd>
<dt><code>-D</code> [<i>srcaddr</i>:]<i>srcport</i></dt>
<dd> Set up dynamic port forwarding. The client listens on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and implements a SOCKS server. So you can point SOCKS-aware applications at this port and they will automatically use the SSH connection to tunnel all their connections. Only works in SSH.</dd>
<dt><code>-X</code></dt>
<dd> Enable X11 forwarding.</dd>
<dt><code>-x</code></dt>
<dd> Disable X11 forwarding (default).</dd>
<dt><code>-A</code></dt>
<dd> Enable agent forwarding.</dd>
<dt><code>-a</code></dt>
<dd> Disable agent forwarding (default).</dd>
<dt><code>-t</code></dt>
<dd> Enable pty allocation (default if a command is NOT specified).</dd>
<dt><code>-T</code></dt>
<dd> Disable pty allocation (default if a command is specified).</dd>
<dt><code>-1</code></dt>
<dd> Force use of SSH protocol version 1.</dd>
<dt><code>-2</code></dt>
<dd> Force use of SSH protocol version 2.</dd>
<dt><code>-C</code></dt>
<dd> Enable SSH compression.</dd>
<dt><code>-i</code> <i>path</i></dt>
<dd> Private key file for authentication.</dd>
<dt><code>-s</code></dt>
<dd> Remote command is SSH subsystem (SSH-2 only).</dd>
<dt><code>-N</code></dt>
<dd> Don&#8217;t start a remote command or shell at all (SSH-2 only).</dd>
<dt><code>-sercfg</code> <i>configuration-string</i></dt>
<dd> Specify the configuration parameters for the serial port, in <code>-serial</code> mode. <i>configuration-string</i> should be a comma-separated list of configuration parameters as follows:</dd>
<dl>
<dl>
<dt><code>&bull;</code></dt>
<dd> Any single digit from 5 to 9 sets the number of data bits.</dd>
<dt><code>&bull;</code></dt>
<dd> `<code>1</code>&#8216;, `<code>1.5</code>&#8216; or `<code>2</code>&#8216; sets the number of stop bits.</dd>
<dt><code>&bull;</code></dt>
<dd> Any other numeric string is interpreted as a baud rate.</dd>
<dt><code>&bull;</code></dt>
<dd> A single lower-case letter specifies the parity: `<code>n</code>&#8216; for none, `<code>o</code>&#8216; for odd, `<code>e</code>&#8216; for even, `<code>m</code>&#8216; for mark and `<code>s</code>&#8216; for space.</dd>
<dt><code>&bull;</code></dt>
<dd> A single upper-case letter specifies the flow control: `<code>N</code>&#8216; for none, `<code>X</code>&#8216; for XON/XOFF, `<code>R</code>&#8216; for RTS/CTS and `<code>D</code>&#8216; for DSR/DTR.</dd></dl>
</dl>
</dl>
<h2>MORE INFORMATION</h2>
<p> For more information on plink, it&#8217;s probably best to go and look at the manual on the PuTTY web page: </p>
<p> <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">http://www.chiark.greenend.org.uk/~sgtatham/putty/</a></code></p>
<h2>BUGS</h2>
<p> This man page isn&#8217;t terribly complete. See the above web link for better documentation. </p>
