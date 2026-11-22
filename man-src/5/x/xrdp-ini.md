---
title: "xrdp-ini(5)"
name: "xrdp-ini"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xrdp-ini/"
description: "xrdp.ini – Configuration file for xrdp(8)"
---

<p><code>xrdp.ini</code> &#8211; Configuration file for <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) </p>
<h2>Description</h2>
<p>This is the man page for <code>xrdp.ini</code>, <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) configuration file. It is composed by a number of sections, each one composed by a section name, enclosed by square brackets, followed by a list of <i>&lt;parameter&gt;</i>=<i>&lt;value&gt;</i> lines. <code>xrdp.ini</code> supports the following sections:</p>
<dl>
<dt><code>[Globals]</code> &#8211; sets some global configuration settings for <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8).</dt>
<dd>
</dd><dt><code>[Logging]</code> &#8211; logging subsystem parameters</dt>
<dd>
</dd><dt><code>[Channels]</code> &#8211; channel subsystem parameters</dt>
<dd> All options and values (except for file names and paths) are case insensitive, and are described in detail below. </dd>
<h2>Globals</h2>
<p>The options to be specified in the <code>[Globals]</code> section are the following: </p>
<dl>
<dt><code>address</code>=<i>ip address</i></dt>
<dd>Specify xrdp listening address. If not specified, defaults to 0.0.0.0 (all interfaces). </dd>
<dt><code>autorun</code>=<i>session_name</i></dt>
<dd>Section name for automatic login. If set and the client supplies valid username and password, the user will be logged in automatically using the connection specified by <i>session_name</i>. </dd>
<p> If <i>session_name</i> is empty, the <code>LOGIN DOMAIN</code> from the client with be used to select the section. If no domain name is supplied, the first suitable section will be used for automatic login. </p>
<dt><code>bitmap_cache</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> this option enables bitmap caching in <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8). </dd>
<dt><code>bitmap_compression</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> this option enables bitmap compression in <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8). </dd>
<dt><code>bulk_compression</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> this option enables compression of bulk data in <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8). </dd>
<dt><code>certificate</code>=<i>/path/to/certificate</i></dt>
<dd>
</dd><dt><code>key_file</code>=<i>/path/to/private_key</i></dt>
<dd>Set location of TLS certificate and private key. They must be written in PEM format. If not specified, defaults to <code>${XRDP_CFG_DIR}/cert.pem</code>, <code>${XRDP_CFG_DIR}/key.pem</code>. </dd>
<p> This parameter is effective only if <code>security_layer</code> is set to <code>tls</code> or <code>negotiate</code>. </p>
<dt><code>channel_code</code>=<i>[true|false]</i></dt>
<dd>If set to <code>0</code>, <code>false</code> or <code>no</code> this option disables all channels <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8). See section <code>CHANNELS</code> below for more fine grained options. </dd>
<dt><code>crypt_level</code>=<i>[low|medium|high|fips]</i></dt>
<dd>Regulate encryption level of Standard RDP Security. This parameter is effective only if <code>security_layer</code> is set to <code>rdp</code> or <code>negotiate</code>. </dd>
<p> Encryption in Standard RDP Security is controlled by two settings: <i>Encryption Level</i> and <i>Encryption Method</i>. The only supported <i>Encryption Method</i> are <code>40BIT_ENCRYPTION</code> and <code>128BIT_ENCRYPTION</code>. <code>56BIT_ENCRYPTION</code> is not supported. This option controls the <i>Encryption Level</i>:</p>
<dl>
<dd>
</dd><dl>
<dt><code>low</code></dt>
<dd>All data sent from the client to the server is protected by encryption based on the maximum key strength supported by the client. <i>This is the only level that the traffic sent by the server to client is not encrypted.</i></dd>
<dt><code>medium</code></dt>
<dd>All data sent between the client and the server is protected by encryption based on the maximum key strength supported by the client (client compatible).</dd>
<dt><code>high</code></dt>
<dd>All data sent between the client and the server is protected by encryption based on the server&#8217;s maximum key strength (sever compatible).</dd>
<dt><code>fips</code></dt>
<dd>All data sent between the client and server is protected using Federal Information Processing Standard 140-1 validated encryption methods. <i>This level is required for Windows clients (mstsc.exe) if the client&#8217;s group policy</i> <i>enforces FIPS-compliance mode.</i></dd></dl>
</dl>
<dt><code>disableSSLv3</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, <code>xrdp</code> will not accept SSLv3 connections. If not specified, defaults to <code>false</code>. This parameter is effective only if <code>security_layer</code> is set to <code>tls</code> or <code>negotiate</code>. </dd>
<dt><code>fork</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> for each incoming connection <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) forks a sub-process instead of using threads. </dd>
<dt><code>hidelogwindow</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, <code>xrdp</code> will not show a window for log messages. If not specified, defaults to <code>false</code>. </dd>
<dt><code>max_bpp</code>=<i>[8|15|16|24|32]</i></dt>
<dd>Limit the color depth by specifying the maximum number of bits per pixel. If not specified or set to <code>0</code>, unlimited. </dd>
<dt><code>pamerrortxt</code>=<i>error_text</i></dt>
<dd>Specify text passed to PAM when authentication failed. The maximum length is <code>256</code>. </dd>
<dt><code>port</code>=<i>port</i></dt>
<dd>Specify TCP port to listen on for incoming connections. The default for RDP is <code>3389</code>. </dd>
<dt><code>require_credentials</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, <code>xrdp</code> requires clients to include username and password initial connection phase. In other words, xrdp doesn&#8217;t allow clients to show login screen if set to true. If not specified, defaults to <code>false</code>. </dd>
<dt><code>security_layer</code>=<i>[tls|rdp|negotiate]</i></dt>
<dd>Regulate security methods. If not specified, defaults to <code>negotiate</code>.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>tls</code></dt>
<dd>Enhanced RDP Security is used. All security operations (encryption, decryption, data integrity verification, and server authentication) are implemented by TLS. </dd>
<dt><code>rdp</code></dt>
<dd>Standard RDP Security, which is not safe from man-in-the-middle attack, is used. The encryption level of Standard RDP Security is controlled by <code>crypt_level</code>. </dd>
<dt><code>negotiate</code></dt>
<dd>Negotiate these security methods with clients.</dd></dl>
</dl>
<dt><code>tcp_keepalive</code>=<i>[true|false]</i></dt>
<dd>Regulate if the listening socket uses socket option <code>SO_KEEPALIVE</code>. If set to <code>1</code>, <code>true</code> or <code>yes</code> and the network connection disappears without closing messages, the connection will be closed. </dd>
<dt><code>tcp_nodelay</code>=<i>[true|false]</i></dt>
<dd>Regulate if the listening socket uses socket option <code>TCP_NODELAY</code>. If set to <code>1</code>, <code>true</code> or <code>yes</code>, no buffering will be performed in the TCP stack. </dd>
<dt><code>tcp_send_buffer_bytes</code>=<i>buffer_size</i></dt>
<dd>
</dd><dt><code>tcp_recv_buffer_bytes</code>=<i>buffer_size</i></dt>
<dd>Specify send/recv buffer sizes in bytes. The default value depends on operating system. </dd>
<dt><code>tls_ciphers</code>=<i>cipher_suite</i></dt>
<dd>Specifies TLS cipher suite. The format of this parameter is equivalent to which <code>openssl</code>(1) ciphers subcommand accepts. </dd>
<p> (ex. $ openssl ciphers &#8216;HIGH:!ADH:!SHA1&#8217;) </p>
<p> This parameter is effective only if <code>security_layer</code> is set to <code>tls</code> or <code>negotiate</code>. </p>
<dt><code>use_fastpath</code>=<i>[input|output|both|none]</i></dt>
<dd>If not specified, defaults to <code>none</code>. </dd>
<dt><code>black</code>=<i>000000</i></dt>
<dd>
</dd><dt><code>grey</code>=<i>c0c0c0</i></dt>
<dd>
</dd><dt><code>dark_grey</code>=<i>808080</i></dt>
<dd>
</dd><dt><code>blue</code>=<i>0000ff</i></dt>
<dd>
</dd><dt><code>dark_blue</code>=<i>00007f</i></dt>
<dd>
</dd><dt><code>white</code>=<i>ffffff</i></dt>
<dd>
</dd><dt><code>red</code>=<i>ff0000</i></dt>
<dd>
</dd><dt><code>green</code>=<i>00ff00</i></dt>
<dd>
</dd><dt><code>background</code>=<i>000000</i></dt>
<dd>These options override the colors used internally by <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) to draw the login and log windows. Colors are defined using a hexadecimal (hex) notation for the combination of Red, Green, and Blue color values (RGB). The lowest value that can be given to one of the light sources is 0 (hex 00). The highest value is 255 (hex FF). </dd>
</dl>
<h2>Logging</h2>
<p>The following parameters can be used in the <code>[Logging]</code> section: </p>
<dl>
<dt><code>LogFile</code>=<i>${SESMAN_LOG_DIR}/sesman.log</i></dt>
<dd>This options contains the path to logfile. It can be either absolute or relative, and the default is <i>${SESMAN_LOG_DIR}/sesman.log</i> </dd>
<dt><code>LogLevel</code>=<i>level</i></dt>
<dd>This option can have one of the following values: </dd>
<p> <code>CORE</code> or <code>0</code> &#8211; Log only core messages. these messages are _always_ logged, regardless the logging level selected. </p>
<p> <code>ERROR</code> or <code>1</code> &#8211; Log only error messages </p>
<p> <code>WARNING</code>, <code>WARN</code> or <code>2</code> &#8211; Logs warnings and error messages </p>
<p> <code>INFO</code> or <code>3</code> &#8211; Logs errors, warnings and informational messages </p>
<p> <code>DEBUG</code> or <code>4</code> &#8211; Log everything. If <code>sesman</code> is compiled in debug mode, this options will output many more low-level message, useful for developers </p>
<dt><code>EnableSyslog</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> this option enables logging to syslog. Otherwise syslog is disabled. </dd>
<dt><code>SyslogLevel</code>=<i>level</i></dt>
<dd>This option sets the logging level for syslog. It can have the same values of <code>LogLevel</code>. If <code>SyslogLevel</code> is greater than <code>LogLevel</code>, its value is lowered to that of <code>LogLevel</code>. </dd>
</dl>
<h2>Channels</h2>
<p>The Remote Desktop Protocol supports several channels, which are used to transfer additional data like sound, clipboard data and others. Channel names not listed here will be blocked by <code>xrdp</code>. Not all channels are supported in all cases, so setting a value to <i>true</i> is a prerequisite, but does not force its use.<br/>
 Channels can also be enabled or disabled on a per connection basis by prefixing each setting with <code>channel.</code> in the channel section. </p>
<dl>
<dt><code>rdpdr</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> using the RDP channel for device redirection is allowed. </dd>
<dt><code>rdpsnd</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> using the RDP channel for sound is allowed. </dd>
<dt><code>drdynvc</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> using the RDP channel to initiate additional dynamic virtual channels is allowed. </dd>
<dt><code>cliprdr</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> using the RDP channel for clipboard redirection is allowed. </dd>
<dt><code>rail</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> using the RDP channel for remote applications integrated locally (RAIL) is allowed. </dd>
<dt><code>xrdpvr</code>=<i>[true|false]</i></dt>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code> using the RDP channel for XRDP Video streaming is allowed. </dd>
</dl>
<h2>Connections</h2>
<p>A connection section is made of a section name, enclosed in square brackets, and the following entries: </p>
<dl>
<dt><code>name</code>=<i>&lt;session name&gt;</i></dt>
<dd>The name displayed in <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) login window&#8217;s combo box. </dd>
<dt><code>lib</code>=<i>../vnc/libvnc.so</i></dt>
<dd>Sets the library to be used with this connection. </dd>
<dt><code>username</code>=<i>&lt;username&gt;</i>|<i>ask</i></dt>
<dd>Specifies the username used for authenticating in the connection. If set to <i>ask</i>, user name should be provided in the login window. </dd>
<dt><code>password</code>=<i>&lt;password&gt;</i>|<i>ask</i></dt>
<dd>Specifies the password used for authenticating in the connection. If set to <i>ask</i>, password should be provided in the login window. </dd>
<dt><code>ip</code>=<i>127.0.0.1</i></dt>
<dd>Specifies the ip address of the host to connect to. </dd>
<dt><code>port</code>=<i>&lt;number&gt;</i>|<i>-1</i></dt>
<dd>Specifies the port number to connect to. If set to <i>-1</i>, the default port for the specified library is used. </dd>
<dt><code>xserverbpp</code>=<i>&lt;number&gt;</i></dt>
<dd>Specifies color depth of the backend X server. The default is the color depth of the client. Only Xvnc and X11rdp use that setting. Xorg runs at <i>24</i> bpp. </dd>
<dt><code>code</code>=<i>&lt;number&gt;</i>|<i>0</i></dt>
<dd>Specifies the session type. The default, <i>0</i>, is Xvnc, <i>10</i> is X11rdp, and <i>20</i> is Xorg with xorgxrdp modules. </dd>
</dl>
<h2>Examples</h2>
<p>This is an example <code>xrdp.ini</code>: </p>
<pre>[Globals]
bitmap_cache=true
bitmap_compression=true
[vnc1]
name=sesman
lib=../vnc/libvnc.so
username=ask
password=ask
ip=127.0.0.1
port=-1</pre>
<h2>Files</h2>
<p>${XRDP_CFG_DIR}/xrdp.ini</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8), <code>sesman</code>(8), <code>sesrun</code>(8), <code><a href="/docs/linux/man/5-sesman-ini/">sesman.ini</a></code>(5) for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
</dl>