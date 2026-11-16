---
title: "x0vncserver(1)"
name: "x0vncserver"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x0vncserver/"
description: "x0vncserver – TigerVNC Server for X displays"
---

<h2>NAME</h2>
<p> x0vncserver &#8211; TigerVNC Server for X displays</p>
<h2>SYNOPSIS</h2>
<p> <code>x0vncserver</code> [<i>options</i>]<br />
 <code>x0vncserver -version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>x0vncserver</code> is a TigerVNC Server which makes any X display remotely accessible via VNC, TigerVNC or compatible viewers. Unlike <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1), it does not create a virtual display. Instead, it just shares an existing X server (typically, that one connected to the physical screen). </p>
<p> XDamage will be used if the existing X server supports it. Otherwise <code>x0vncserver</code> will fall back to polling the screen for changes. </p>
<h2>OPTIONS</h2>
<p> <code>x0vncserver</code> interprets the command line as a list of parameters with optional values. Running <code>x0vncserver -h</code> will show a list of all valid parameters with short descriptions. All parameters are optional, but normally you would have to use the <code>PasswordFile</code> parameter (see its description below). </p>
<p> There are several forms of specifying parameters in the command line (here we use `<i>SomeParameter</i>&#8216; as an example parameter name): </p>
<dl>
<dt><code>&#8211;</code><i>SomeParameter</i></dt>
<dd> Enable the parameter, turn the feature on. This form can be used with parameters that simply enable or disable some feature.</dd>
<dt><code>&#8211;</code><i>SomeParameter</i>=0</dt>
<dd> Disable the parameter, turn the feature off.</dd>
<dt><code>&#8211;</code><i>SomeParameter</i>=<i>value</i></dt>
<dd> Assign the specified <i>value</i> to the parameter. The leading dash can be omitted, or it can be doubled if desired (like in GNU-style long options).</dd></dl>
<p> Parameter names are case-insensitive, their order in the command line can be arbitrary. </p>
<h2>PARAMETERS</h2>
<dl>
<dt><code>display</code></dt>
<dd> The X display name. If not specified, it defaults to the value of the DISPLAY environment variable.</dd>
<dt><code>rfbport</code></dt>
<dd> TCP port to listen for incoming VNC connections (RFB protocol). The default port is 5900.</dd>
<dt><code>Log</code></dt>
<dd> Specifies which log output should be directed to which target logger, and the level of output to log. Format is <i>log</i>:<i>target</i>:<i>level</i>. Default is <code>*:stderr:30</code> (log everything to stderr, set log level to 30). Log level should be a value between 0 and 100, higher levels produce more output.</dd>
<dt><code>HostsFile</code></dt>
<dd> This parameter allows to specify a file name with IP access control rules. The file should include one rule per line, and the rule format is one of the following: +<i>address</i>/<i>prefix</i> (accept connections from the specified address group), &#8211;<i>address</i>/<i>prefix</i> (reject connections) or ?<i>address</i>/<i>prefix</i> (query the local user). The first rule matching the IP address determines the action to be performed. Rules that include only an action sign (+, &#8211; or ?) will match any IP address. <i>Prefix</i> is optional and is specified as a number of bits (e.g. /24). Default is to accept connections from any IP address.</dd>
<dt><code>SecurityTypes</code></dt>
<dd> Specify which security scheme to use for incoming connections. Valid values are a comma separated list of <code>None</code>, <code>VncAuth</code>, <code>Plain</code>, <code>TLSNone</code>, <code>TLSVnc</code>, <code>TLSPlain</code>, <code>X509None</code>, <code>X509Vnc</code> and <code>X509Plain</code>. Default is <code>VncAuth,TLSVnc</code>.</dd>
<dt><code>rfbauth, PasswordFile</code></dt>
<dd> Password file for VNC authentication. There is no default, you should specify the password file explicitly. Password file should be created with the <code><a href="/docs/linux/man/1-vncpasswd/">vncpasswd</a></code>(1) utility.</dd>
<dt><code>Password</code></dt>
<dd> Obfuscated binary encoding of the password which clients must supply to access the server. Using this parameter is insecure, use <code>PasswordFile</code> parameter instead.</dd>
<dt><code>PlainUsers</code></dt>
<dd> A comma separated list of user names that are allowed to authenticate via any of the &quot;Plain&quot; security types (Plain, TLSPlain, etc.). Specify <code>*</code> to allow any user to authenticate using this security type. Default is to deny all users.</dd>
<dt><code>pam_service, PAMService</code></dt>
<dd> PAM service name to use when authentication users using any of the &quot;Plain&quot; security types. Default is <code>vnc</code>.</dd>
<dt><code>X509Cert</code></dt>
<dd> Path to a X509 certificate in PEM format to be used for all X509 based security types (X509None, X509Vnc, etc.).</dd>
<dt><code>X509Key</code></dt>
<dd> Private key counter part to the certificate given in <code>X509Cert</code>. Must also be in PEM format.</dd>
<dt><code>BlacklistThreshold</code></dt>
<dd> The number of unauthenticated connection attempts allowed from any individual host before that host is black-listed. Default is 5.</dd>
<dt><code>BlacklistTimeout</code></dt>
<dd> The initial timeout applied when a host is first black-listed. The host cannot re-attempt a connection until the timeout expires. Default is 10.</dd>
<dt><code>QueryConnect</code></dt>
<dd> Prompt the local user to accept or reject incoming connections. Default is off.</dd>
<dt><code>QueryConnectTimeout</code></dt>
<dd> Number of seconds to show the Accept Connection dialog before rejecting the connection. Default is 10.</dd>
<dt><code>AlwaysShared</code></dt>
<dd> Always treat incoming connections as shared, regardless of the client-specified setting. Default is off.</dd>
<dt><code>NeverShared</code></dt>
<dd> Never treat incoming connections as shared, regardless of the client-specified setting. Default is off.</dd>
<dt><code>DisconnectClients</code></dt>
<dd> Disconnect existing clients if an incoming connection is non-shared. If combined with <code>NeverShared</code> then new connections will be refused while there is a client active. Default is on.</dd>
<dt><code>AcceptKeyEvents</code></dt>
<dd> Accept key press and release events from clients. Default is on.</dd>
<dt><code>AcceptPointerEvents</code></dt>
<dd> Accept pointer events from clients. Default is on.</dd>
<dt><code>RemapKeys</code></dt>
<dd> Comma-separated list of incoming keysyms to remap. Mappings are expressed as two hex values, prefixed by <code>0x</code>, and separated by <code>-&gt;</code> (`dash&#8217; and `greater than&#8217; characters).</dd>
<dt><code>Protocol3.3</code></dt>
<dd> Always use RFB protocol version 3.3 for backwards compatibility with badly-behaved clients. Default is off.</dd>
<dt><code>Geometry</code></dt>
<dd> This option specifies the screen area that will be shown to VNC clients. The format is <i>width</i>x<i>height</i>+<i>xoffset</i>+<i>yoffset</i> , where `+&#8217; signs can be replaced with `-&#8216; signs to specify offsets from the right and/or from the bottom of the screen. Offsets are optional, +0+0 is assumed by default (top left corner). If the argument is empty, full screen is shown to VNC clients (this is the default).</dd>
<dt><code>MaxProcessorUsage</code></dt>
<dd> Maximum percentage of CPU time to be consumed when polling the screen. Default is 35.</dd>
<dt><code>PollingCycle</code></dt>
<dd> Milliseconds per one polling cycle. Actual interval may be dynamically adjusted to satisfy <code>MaxProcessorUsage</code> setting. Default is 30.</dd>
<dt><code>DeferUpdate</code></dt>
<dd> x0vncserver uses a &quot;deferred update&quot; mechanism which enhances performance in many cases. After any change to the framebuffer, x0vncserver waits for this number of milliseconds (default 1) before sending an update to any waiting clients. This means that more changes tend to get coalesced together in a single update. Setting it to 0 results in the same behaviour as earlier versions of x0vncserver, where the first change to the framebuffer causes an immediate update to any waiting clients.</dd>
<dt><code>AlwaysSetDeferUpdateTimer</code></dt>
<dd> Keep delaying sending the screen update to the client(s) each time the screen is updated. Otherwise the delay is from the first update. Default is off.</dd>
<dt><code>CompareFB</code></dt>
<dd> Perform pixel comparison on framebuffer to reduce unnecessary updates. Can be either <code>0</code> (off), <code>1</code> (always) or <code>2</code> (auto). Default is <code>2</code>.</dd>
<dt><code>UseSHM</code></dt>
<dd> Use MIT-SHM extension if available. Using that extension accelerates reading the screen. Default is on.</dd>
<dt><code>OverlayMode</code></dt>
<dd> Use overlay mode in IRIX or Solaris (does not have effect in other systems). This enables system-specific access to complete full-color version of the screen (the default X visual often provides 256 colors). Also, in overlay mode, <code>x0vncserver</code> can show correct mouse cursor. Default is on.</dd>
<dt><code>ZlibLevel</code></dt>
<dd> Zlib compression level for ZRLE encoding (it does not affect Tight encoding). Acceptable values are between 0 and 9. Default is to use the standard compression level provided by the <code><a href="/docs/linux/man/3-zlib/">zlib</a></code>(3) compression library.</dd>
<dt><code>ImprovedHextile</code></dt>
<dd> Use improved compression algorithm for Hextile encoding which achieves better compression ratios by the cost of using slightly more CPU time. Default is on.</dd>
<dt><code>IdleTimeout</code></dt>
<dd> The number of seconds after which an idle VNC connection will be dropped (zero means no timeout). Default is 0.</dd>
<dt><code>MaxDisconnectionTime</code></dt>
<dd> Terminate when no client has been connected for <i>N</i> seconds. Default is 0.</dd>
<dt><code>MaxConnectionTime</code></dt>
<dd> Terminate when a client has been connected for <i>N</i> seconds. Default is 0.</dd>
<dt><code>MaxIdleTime</code></dt>
<dd> Terminate after <i>N</i> seconds of user inactivity. Default is 0.</dd>
<dt><code>ClientWaitTimeMillis</code></dt>
<dd> The number of milliseconds to wait for a client which is no longer responding. Default is 20000.</dd>
<dt><code>AcceptCutText</code></dt>
<dd> <code>SendCutText</code> <code>MaxCutText</code> Currently unused. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1), <code><a href="/docs/linux/man/1-vncpasswd/">vncpasswd</a></code>(1),<br />
 <a rel="nofollow" href="http://www.tigervnc.org/">http://www.tigervnc.org/</a> </p>
<h2>AUTHOR</h2>
<p> Constantin Kaplinsky and others. </p>
<p> VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&amp;T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite. </p>
<h2>Index</h2>
