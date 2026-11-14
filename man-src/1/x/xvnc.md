---
title: "xvnc(1)"
name: "xvnc"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvnc/"
description: "Xvnc – the X VNC server"
---

<p>Xvnc &#8211; the X VNC server</p>
<h2>Synopsis</h2>
<p><code>Xvnc</code> [<i>options</i>] :<i>display#</i></p>
<h2>Description</h2>
<p><code>Xvnc</code> is the X VNC (Virtual Network Computing) server. It is based on a standard X server, but it has a &quot;virtual&quot; screen rather than a physical one. X applications display themselves on it as if it were a normal X display, but they can only be accessed via a VNC viewer &#8211; see <code><a href="/docs/linux/man/1-vncviewer/">vncviewer</a></code>(1). </p>
<p> So Xvnc is really two servers in one. To the applications it is an X server, and to the remote VNC users it is a VNC server. By convention we have arranged that the VNC server display number will be the same as the X server display number, which means you can use eg. snoopy:2 to refer to display 2 on machine &quot;snoopy&quot; in both the X world and the VNC world. </p>
<p> The best way of starting <code>Xvnc</code> is via the <code>vncserver</code> script. This sets up the environment appropriately and runs some X applications to get you going. See the manual page for <code><a href="/docs/linux/man/1-vncserver/">vncserver</a></code>(1) for more information. </p>
<h2>Options</h2>
<p><code>Xvnc</code> takes lots of options &#8211; running <code>Xvnc -help</code> gives a list. Many of these are standard X server options, which are described in the <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1) manual page. In addition to options which can only be set via the command-line, there are also &quot;parameters&quot; which can be set both via the command-line and through the <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1) program. </p>
<dl>
<dt><code>-geometry </code><i>width</i>x<i>height</i></p>
<dd>Specify the size of the desktop to be created. Default is 1024&#215;768.</p>
<dt><code>-depth </code><i>depth</i></p>
<dd>Specify the pixel depth in bits of the desktop to be created. Default is 24, other possible values are 8, 15, and 16 &#8211; anything else is likely to cause strange behaviour by applications.</p>
<dt><code>-pixelformat </code><i>format</i></p>
<dd>Specify pixel format for server to use (BGRnnn or RGBnnn). The default for depth 8 is BGR233 (meaning the most significant two bits represent blue, the next three green, and the least significant three represent red), the default for depth 16 is RGB565 and for depth 24 is RGB888.</p>
<dt><code>-interface </code><i>IP address</i></p>
<dd>Listen on interface. By default Xvnc listens on all available interfaces.</p>
<dt><code>-inetd </code></p>
<dd>This significantly changes Xvnc&#8217;s behaviour so that it can be launched from inetd. See the section below on usage with inetd.</p>
<dt><code>-help</code></p>
<dd>List all the options and parameters </p>
</dl>
<h2>Parameters</h2>
<p>VNC parameters can be set both via the command-line and through the <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1) program, and with a VNC-enabled Xorg server via Options entries in the xorg.conf file. </p>
<p> Parameters can be turned on with &#8211;<i>param</i> or off with &#8211;<i>param</i>=0. Parameters which take a value can be specified as &#8211;<i>param</i> <i>value</i>. Other valid forms are <i>param</i><code>=</code><i>value</i> &#8211;<i>param</i>=<i>value</i> &#8212;<i>param</i>=<i>value</i>. Parameter names are case-insensitive. </p>
<dl>
<dt><code>-desktop </code><i>desktop-name</i></p>
<dd>Each desktop has a name which may be displayed by the viewer. It defaults to &quot;x11&quot;.</p>
<dt><code>-rfbport </code><i>port</i></p>
<dd>Specifies the TCP port on which Xvnc listens for connections from viewers (the protocol used in VNC is called RFB &#8211; &quot;remote framebuffer&quot;). The default is 5900 plus the display number.</p>
<dt><code>-rfbwait </code><i>time</i>, -ClientWaitTimeMillis <i>time</i></p>
<dd>Time in milliseconds to wait for a viewer which is blocking Xvnc. This is necessary because Xvnc is single-threaded and sometimes blocks until the viewer has finished sending or receiving a message &#8211; note that this does not mean an update will be aborted after this time. Default is 20000 (20 seconds).</p>
<dt><code>-httpd </code><i>directory</i></p>
<dd>Run a mini-HTTP server which serves files from the given directory. Normally the directory will contain the classes for the Java viewer. In addition, files with a .vnc extension will have certain substitutions made so that a single installation of the Java VNC viewer can be served by separate instances of Xvnc.</p>
<dt><code>-httpPort </code><i>port</i></p>
<dd>Specifies the port on which the mini-HTTP server runs. Default is 5800 plus the display number.</p>
<dt><code>-rfbauth </code><i>passwd-file</i>, -PasswordFile <i>passwd-file</i></p>
<dd>Specifies the file containing the password used to authenticate viewers. The file is accessed each time a connection comes in, so it can be changed on the fly via <code><a href="/docs/linux/man/1-vncpasswd/">vncpasswd</a></code>(1).</p>
<dt><code>-DeferUpdate </code><i>time</i></p>
<dd>Xvnc uses a &quot;deferred update&quot; mechanism which enhances performance in many cases. After any change to the framebuffer, Xvnc waits for this number of milliseconds (default 1) before sending an update to any waiting clients. This means that more changes tend to get coalesced together in a single update. Setting it to 0 results in the same behaviour as earlier versions of Xvnc, where the first change to the framebuffer causes an immediate update to any waiting clients.</p>
<dt><code>-AlwaysSetDeferUpdateTimer</code></p>
<dd>Keep delaying sending the screen update to the client(s) each time the screen is updated. Otherwise the delay is from the first update. Default is off.</p>
<dt><code>-AcceptCutText</code></p>
<dd>Accept clipboard updates from clients (default is on).</p>
<dt><code>-MaxCutText </code><i>bytes</i></p>
<dd>The maximum size of a clipboard update that will be accepted from a client. Default is <code>262144</code>.</p>
<dt><code>-SendCutText</code></p>
<dd>Send clipboard changes to clients (default is on).</p>
<dt><code>-SendPrimary</code></p>
<dd>Send the primary selection and cut buffer to the server as well as the clipboard selection. Default is on.</p>
<dt><code>-AcceptPointerEvents</code></p>
<dd>Accept pointer press and release events from clients (default is on).</p>
<dt><code>-AcceptKeyEvents</code></p>
<dd>Accept key press and release events from clients (default is on).</p>
<dt><code>-DisconnectClients</code></p>
<dd>Disconnect existing clients if an incoming connection is non-shared (default is on). If <code>DisconnectClients</code> is false, then a new non-shared connection will be refused while there is a client active. When combined with <code>NeverShared</code> this means only one client is allowed at a time.</p>
<dt><code>-NeverShared</code></p>
<dd>Never treat incoming connections as shared, regardless of the client-specified setting (default is off).</p>
<dt><code>-AlwaysShared</code></p>
<dd>Always treat incoming connections as shared, regardless of the client-specified setting (default is off).</p>
<dt><code>-Protocol3.3</code></p>
<dd>Always use protocol version 3.3 for backwards compatibility with badly-behaved clients (default is off).</p>
<dt><code>-CompareFB</code></p>
<dd>Perform pixel comparison on framebuffer to reduce unnecessary updates (default is on).</p>
<dt><code>-ZlibLevel</code></p>
<dd>Zlib compression level for ZRLE encoding (it does not affect Tight encoding). Acceptable values are between 0 and 9. Default is to use the standard compression level provided by the <code><a href="/docs/linux/man/3-zlib/">zlib</a></code>(3) compression library.</p>
<dt><code>-ImprovedHextile</code></p>
<dd>Use improved compression algorithm for Hextile encoding which achieves better compression ratios by the cost of using slightly more CPU time. Default is on.</p>
<dt><code>-SecurityTypes </code><i>sec-types</i></p>
<dd>Specify which security scheme to use for incoming connections. Valid values are a comma separated list of <code>None</code>, <code>VncAuth</code>, <code>Plain</code>, <code>TLSNone</code>, <code>TLSVnc</code>, <code>TLSPlain</code>, <code>X509None</code>, <code>X509Vnc</code> and <code>X509Plain</code>. Default is <code>VncAuth,TLSVnc</code>.</p>
<dt><code>-Password </code><i>password</i></p>
<dd>Obfuscated binary encoding of the password which clients must supply to access the server. Using this parameter is insecure, use <code>PasswordFile</code> parameter instead.</p>
<dt><code>-PlainUsers </code><i>user-list</i></p>
<dd>A comma separated list of user names that are allowed to authenticate via any of the &quot;Plain&quot; security types (Plain, TLSPlain, etc.). Specify <code>*</code> to allow any user to authenticate using this security type. Default is to deny all users.</p>
<dt><code>-pam_service </code><i>name</i>, -PAMService <i>name</i></p>
<dd>PAM service name to use when authentication users using any of the &quot;Plain&quot; security types. Default is <code>vnc</code>.</p>
<dt><code>-X509Cert </code><i>path</i></p>
<dd>Path to a X509 certificate in PEM format to be used for all X509 based security types (X509None, X509Vnc, etc.).</p>
<dt><code>-X509Key </code><i>path</i></p>
<dd>Private key counter part to the certificate given in <code>X509Cert</code>. Must also be in PEM format.</p>
<dt><code>-BlacklistThreshold </code><i>count</i></p>
<dd>The number of unauthenticated connection attempts allowed from any individual host before that host is black-listed. Default is 5.</p>
<dt><code>-BlacklistTimeout </code><i>seconds</i></p>
<dd>The initial timeout applied when a host is first black-listed. The host cannot re-attempt a connection until the timeout expires. Default is 10.</p>
<dt><code>-IdleTimeout </code><i>seconds</i></p>
<dd>The number of seconds after which an idle VNC connection will be dropped (default is 0, which means that idle connections will never be dropped).</p>
<dt><code>-MaxDisconnectionTime </code><i>seconds</i></p>
<dd>Terminate when no client has been connected for <i>N</i> seconds. Default is 0.</p>
<dt><code>-MaxConnectionTime </code><i>seconds</i></p>
<dd>Terminate when a client has been connected for <i>N</i> seconds. Default is 0.</p>
<dt><code>-MaxIdleTime </code><i>seconds</i></p>
<dd>Terminate after <i>N</i> seconds of user inactivity. Default is 0.</p>
<dt><code>-QueryConnect</code></p>
<dd>Prompts the user of the desktop to explicitly accept or reject incoming connections. This is most useful when using the vnc.so module or <code><a href="/docs/linux/man/1-x0vncserver/">x0vncserver</a></code>(1) program to access an existing X desktop via VNC. </p>
<p> The <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1) program must be running on the desktop in order for QueryConnect to be supported by the <code><a href="/docs/linux/man/1-vnc-so/">vnc.so</a></code>(1) module or <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1) program. The <code><a href="/docs/linux/man/1-x0vncserver/">x0vncserver</a></code>(1) program does not require <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1) to be running.</p>
<dt><code>-QueryConnectTimeout </code><i>seconds</i></p>
<dd>Number of seconds to show the Accept Connection dialog before rejecting the connection. Default is <code>10</code>.</p>
<dt><code>-localhost</code></p>
<dd>Only allow connections from the same machine. Useful if you use SSH and want to stop non-SSH connections from any other hosts.</p>
<dt><code>-Log </code><i>logname</i>:<i>dest</i>:<i>level</i></p>
<dd>Configures the debug log settings. <i>dest</i> can currently be <code>stderr</code>, <code>stdout</code> or <code>syslog</code>, and <i>level</i> is between 0 and 100, 100 meaning most verbose output. <i>logname</i> is usually <code>*</code> meaning all, but you can target a specific source file if you know the name of its &quot;LogWriter&quot;. Default is <code>*:stderr:30</code>.</p>
<dt><code>-RemapKeys </code><i>mapping</i></p>
<dd>Sets up a keyboard mapping. <i>mapping</i> is a comma-separated string of character mappings, each of the form <i>char</i>-&gt;<i>char</i>, or <i>char</i>&lt;&gt;<i>char</i>, where <i>char</i> is a hexadecimal keysym. For example, to exchange the &quot; and @ symbols you would specify the following:</p>
<dd>RemapKeys=0x22&lt;&gt;0x40</p>
<dt><code>-AvoidShiftNumLock</code></p>
<dd>Key affected by NumLock often require a fake Shift to be inserted in order for the correct symbol to be generated. Turning on this option avoids these extra fake Shift events but may result in a slightly different symbol (e.g. a Return instead of a keypad Enter).</p>
<dt><code>-AllowOverride</code></p>
<dd>Comma separated list of parameters that can be modified using VNC extension. Parameters can be modified for example using <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1) program from inside a running session. </p>
<p> Allowing override of parameters such as <code>PAMService</code> or <code>PasswordFile</code> can negatively impact security if Xvnc runs under different user than the programs allowed to override the parameters. </p>
<p> When <code>NoClipboard</code> parameter is set, allowing override of <code>SendCutText</code> and <code>AcceptCutText</code> has no effect. </p>
<p> Default is <code>desktop,AcceptPointerEvents,SendCutText,AcceptCutText,SendPrimary,SetPrimary</code>. </p>
</dl>
<h2>Usage With Inetd</h2>
<p>By configuring the <code><a href="/docs/linux/man/1-inetd/">inetd</a></code>(1) service appropriately, Xvnc can be launched on demand when a connection comes in, rather than having to be started manually. When given the <code>-inetd</code> option, instead of listening for TCP connections on a given port it uses its standard input and standard output. There are two modes controlled by the wait/nowait entry in the inetd.conf file. </p>
<p> In the nowait mode, Xvnc uses its standard input and output directly as the connection to a viewer. It never has a listening socket, so cannot accept further connections from viewers (it can however connect out to listening viewers by use of the vncconfig program). Further viewer connections to the same TCP port result in inetd spawning off a new Xvnc to deal with each connection. When the connection to the viewer dies, the Xvnc and any associated X clients die. This behaviour is most useful when combined with the XDMCP options -query and -once. An typical example in inetd.conf might be (all on one line): </p>
<p> 5950 stream tcp nowait nobody /usr/local/bin/Xvnc Xvnc -inetd -query localhost -once securitytypes=none </p>
<p> In this example a viewer connection to :50 will result in a new Xvnc for that connection which should display the standard XDM login screen on that machine. Because the user needs to login via XDM, it is usually OK to accept connections without a VNC password in this case. </p>
<p> In the wait mode, when the first connection comes in, inetd gives the listening socket to Xvnc. This means that for a given TCP port, there is only ever one Xvnc at a time. Further viewer connections to the same port are accepted by the same Xvnc in the normal way. Even when the original connection is broken, the Xvnc will continue to run. If this is used with the XDMCP options -query and -once, the Xvnc and associated X clients will die when the user logs out of the X session in the normal way. It is important to use a VNC password in this case. A typical entry in inetd.conf might be: </p>
<p> 5951 stream tcp wait james /usr/local/bin/Xvnc Xvnc -inetd -query localhost -once passwordFile=/home/james/.vnc/passwd </p>
<p> In fact typically, you would have one entry for each user who uses VNC regularly, each of whom has their own dedicated TCP port which they use. In this example, when user &quot;james&quot; connects to :51, he enters his VNC password, then gets the XDM login screen where he logs in in the normal way. However, unlike the previous example, if he disconnects, the session remains persistent, and when he reconnects he will get the same session back again. When he logs out of the X session, the Xvnc will die, but of course a new one will be created automatically the next time he connects. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1), <code><a href="/docs/linux/man/1-vncpasswd/">vncpasswd</a></code>(1), <code><a href="/docs/linux/man/1-vncserver/">vncserver</a></code>(1), <code><a href="/docs/linux/man/1-vncviewer/">vncviewer</a></code>(1), <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), <code><a href="/docs/linux/man/1-inetd/">inetd</a></code>(1)<br />
 <a rel="nofollow" href="http://www.tigervnc.org">http://www.tigervnc.org</a> </p>
<h2>Author</h2>
<p>Tristan Richardson, RealVNC Ltd. and others. </p>
<p> VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&amp;T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite.</p>
