---
title: "putty(1)"
name: "putty"
section: "1"
letter: "p"
url: "/docs/linux/man/1-putty/"
description: "putty – GUI SSH, Telnet and Rlogin client for X"
---

<h2>NAME</h2>
<p> <code>putty</code> &#8211; GUI SSH, Telnet and Rlogin client for X</p>
<h2>SYNOPSIS</h2>
<pre><code>
putty &amp;nbsp;
[&amp;nbsp; options &amp; nbsp;] &amp; nbsp;
[&amp;nbsp; host &amp; nbsp;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>putty</code> is a graphical SSH, Telnet and Rlogin client for X. It is a direct port of the Windows SSH client of the same name.</p>
<h2>OPTIONS</h2>
<p> The command-line options supported by <code>putty</code> are:</p>
<dl>
<dt><code>&#8211;display</code> <i>display-name</i></p>
<dd> Specify the X display on which to open <code>putty</code>. (Note this option has a double minus sign, even though none of the others do. This is because this option is supplied automatically by GTK. Sorry.)</p>
<dt><code>-fn</code> <i>font-name</i></p>
<dd> Specify the font to use for normal text displayed in the terminal.</p>
<dt><code>-fb</code> <i>font-name</i></p>
<dd> Specify the font to use for bold text displayed in the terminal. If the <code>BoldAsColour</code> resource is set to 1 (the default), bold text will be displayed in different colours instead of a different font, so this option will be ignored. If <code>BoldAsColour</code> is set to 0 or 2 and you do not specify a bold font, <code>putty</code> will overprint the normal font to make it look bolder.</p>
<dt><code>-fw</code> <i>font-name</i></p>
<dd> Specify the font to use for double-width characters (typically Chinese, Japanese and Korean text) displayed in the terminal.</p>
<dt><code>-fwb</code> <i>font-name</i></p>
<dd> Specify the font to use for bold double-width characters (typically Chinese, Japanese and Korean text). Like <code>-fb</code>, this will be ignored unless the <code>BoldAsColour</code> resource is set to 0 or 2.</p>
<dt><code>-geometry</code> <i>geometry</i></p>
<dd> Specify the size of the terminal, in rows and columns of text. See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for more information on the syntax of geometry specifications.</p>
<dt><code>-sl</code> <i>lines</i></p>
<dd> Specify the number of lines of scrollback to save off the top of the terminal.</p>
<dt><code>-fg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for normal text.</p>
<dt><code>-bg</code> <i>colour</i></p>
<dd> Specify the background colour to use for normal text.</p>
<dt><code>-bfg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for bold text, if the <code>BoldAsColour</code> resource is set to 1 (the default) or 2.</p>
<dt><code>-bbg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for bold reverse-video text, if the <code>BoldAsColour</code> resource is set to 1 (the default) or 2. (This colour is best thought of as the bold version of the background colour; so it only appears when text is displayed <i>in</i> the background colour.)</p>
<dt><code>-cfg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for text covered by the cursor.</p>
<dt><code>-cbg</code> <i>colour</i></p>
<dd> Specify the background colour to use for text covered by the cursor. In other words, this is the main colour of the cursor.</p>
<dt><code>-title</code> <i>title</i></p>
<dd> Specify the initial title of the terminal window. (This can be changed under control of the server.)</p>
<dt><code>-sb-</code> or <code>+sb</code></p>
<dd> Tells <code>putty</code> not to display a scroll bar.</p>
<dt><code>-sb</code></p>
<dd> Tells <code>putty</code> to display a scroll bar: this is the opposite of <code>-sb-</code>. This is the default option: you will probably only need to specify it explicitly if you have changed the default using the <code>ScrollBar</code> resource.</p>
<dt><code>-log</code> <i>filename</i></p>
<dd> This option makes <code>putty</code> log all the terminal output to a file as well as displaying it in the terminal.</p>
<dt><code>-cs</code> <i>charset</i></p>
<dd> This option specifies the character set in which <code>putty</code> should assume the session is operating. This character set will be used to interpret all the data received from the session, and all input you type or paste into <code>putty</code> will be converted into this character set before being sent to the session.</p>
<dl>
<dt>
<dd>
<p> Any character set name which is valid in a MIME header (and supported by <code>putty</code>) should be valid here (examples are `<code>ISO-8859-1</code>&#8216;, `<code>windows-1252</code>&#8216; or `<code>UTF-8</code>&#8216;). Also, any character encoding which is valid in an X logical font description should be valid (`<code>ibm-cp437</code>&#8216;, for example). </p>
<p> <code>putty</code>&#8216;s default behaviour is to use the same character encoding as its primary font. If you supply a Unicode (<code>iso10646-1</code>) font, it will default to the UTF-8 character set. </p>
<p> Character set names are case-insensitive.</dl>
<dt><code>-nethack</code></p>
<dd> Tells <code>putty</code> to enable NetHack keypad mode, in which the numeric keypad generates the NetHack <code>hjklyubn</code> direction keys. This enables you to play NetHack with the numeric keypad without having to use the NetHack <code>number_pad</code> option (which requires you to press `<code>n</code>&#8216; before any repeat count). So you can move with the numeric keypad, and enter repeat counts with the normal number keys.</p>
<dt><code>-help</code>, <code>&#8211;help</code></p>
<dd> Display a message summarizing the available options.</p>
<dt><code>-pgpfp</code></p>
<dd> Display the fingerprints of the PuTTY PGP Master Keys, to aid in verifying new files released by the PuTTY team.</p>
<dt><code>-load</code> <i>session</i></p>
<dd> Load a saved session by name. This allows you to run a saved session straight from the command line without having to go through the configuration box first.</p>
<dt><code>-ssh</code>, <code>-telnet</code>, <code>-rlogin</code>, <code>-raw</code>, <code>-serial</code></p>
<dd> Select the protocol <code>putty</code> will use to make the connection.</p>
<dt><code>-l</code> <i>username</i></p>
<dd> Specify the username to use when logging in to the server.</p>
<dt><code>-L</code> <code>[</code><i>srcaddr</i><code>:]</code><i>srcport</i><code>:</code><i>desthost</i><code>:</code><i>destport</i></p>
<dd> Set up a local port forwarding: listen on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and forward any connections over the SSH connection to the destination address <i>desthost</i>:<i>destport</i>. Only works in SSH.</p>
<dt><code>-R</code> <code>[</code><i>srcaddr</i><code>:]</code><i>srcport</i><code>:</code><i>desthost</i><code>:</code><i>destport</i></p>
<dd> Set up a remote port forwarding: ask the SSH server to listen on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and to forward any connections back over the SSH connection where the client will pass them on to the destination address <i>desthost</i>:<i>destport</i>. Only works in SSH.</p>
<dt><code>-D</code> [<i>srcaddr</i>:]<i>srcport</i></p>
<dd> Set up dynamic port forwarding. The client listens on <i>srcport</i> (or <i>srcaddr</i>:<i>srcport</i> if specified), and implements a SOCKS server. So you can point SOCKS-aware applications at this port and they will automatically use the SSH connection to tunnel all their connections. Only works in SSH.</p>
<dt><code>-P</code> <i>port</i></p>
<dd> Specify the port to connect to the server on.</p>
<dt><code>-A</code>, <code>-a</code></p>
<dd> Enable (<code>-A</code>) or disable (<code>-a</code>) SSH agent forwarding. Currently this only works with OpenSSH and SSH-1.</p>
<dt><code>-X</code>, <code>-x</code></p>
<dd> Enable (<code>-X</code>) or disable (<code>-x</code>) X11 forwarding.</p>
<dt><code>-T</code>, <code>-t</code></p>
<dd> Enable (<code>-t</code>) or disable (<code>-T</code>) the allocation of a pseudo-terminal at the server end.</p>
<dt><code>-C</code></p>
<dd> Enable zlib-style compression on the connection.</p>
<dt><code>-1</code>, <code>-2</code></p>
<dd> Select SSH protocol version 1 or 2.</p>
<dt><code>-i</code> <i>keyfile</i></p>
<dd> Specify a private key file to use for authentication. For SSH-2 keys, this key file must be in PuTTY&#8217;s format, not OpenSSH&#8217;s or anyone else&#8217;s.</p>
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
<h2>SAVED SESSIONS</h2>
<p> Saved sessions are stored in a <code>.putty/sessions</code> subdirectory in your home directory.</p>
<h2>MORE INFORMATION</h2>
<p> For more information on PuTTY, it&#8217;s probably best to go and look at the manual on the web page: </p>
<p> <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">http://www.chiark.greenend.org.uk/~sgtatham/putty/</a></code></p>
<h2>BUGS</h2>
<p> This man page isn&#8217;t terribly complete. </p>
<h2>Index</h2>
