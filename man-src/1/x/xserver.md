---
title: "xserver(1)"
name: "xserver"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xserver/"
description: "Xserver – X Window System display server"
---

<p>Xserver &#8211; X Window System display server </p>
<h2>Synopsis</h2>
<p><code>X</code> [option &#8230;]</p>
<h2>Description</h2>
<p><i>X</i> is the generic name for the X Window System display server. It is frequently a link or a copy of the appropriate server binary for driving the most frequently used server on a given machine.</p>
<h2>Starting The Server</h2>
<p>The X server is usually started from the X Display Manager program <i><a href="/docs/linux/man/1-xdm/">xdm</a></i>(1) or a similar display manager program. This utility is run from the system boot files and takes care of keeping the server running, prompting for usernames and passwords, and starting up the user sessions. </p>
<p> Installations that run more than one window system may need to use the <i><a href="/docs/linux/man/1-xinit/">xinit</a></i>(1) utility instead of a display manager. However, <i>xinit</i> is to be considered a tool for building startup scripts and is not intended for use by end users. Site administrators are <code>strongly</code> urged to use a display manager, or build other interfaces for novice users. </p>
<p> The X server may also be started directly by the user, though this method is usually reserved for testing and is not recommended for normal operation. On some platforms, the user must have special permission to start the X server, often because access to certain devices (e.g. <i>/dev/mouse</i>) is restricted. Where applicable, the X server notifies systemd when it is ready to process requests. </p>
<p> When the X server starts up, it typically takes over the display. If you are running on a workstation whose console is the display, you may not be able to log into the console while the server is running.</p>
<h2>Options</h2>
<p>Many X servers have device-specific command line options. See the manual pages for the individual servers for more details; a list of server-specific manual pages is provided in the SEE ALSO section below. </p>
<p> All of the X servers accept the command line options described below. Some X servers may have alternative ways of providing the parameters described here, but the values provided via the command line options should override values specified via other mechanisms.</p>
<dl>
<dt><code>:</code><i>displaynumber</i></p>
<dd>The X server runs as the given <i>displaynumber</i>, which by default is 0. If multiple X servers are to run simultaneously on a host, each must have a unique display number. See the DISPLAY NAMES section of the <i><a href="/docs/linux/man/7-x/">X</a></i>(7) manual page to learn how to specify which display number clients should try to use.</p>
<dt><code>-a </code><i>number</i></p>
<dd>sets pointer acceleration (i.e. the ratio of how much is reported to how much the user actually moved the pointer).</p>
<dt><code>-ac</code></p>
<dd>disables host-based access control mechanisms. Enables access by any host, and permits any host to modify the access control list. Use with extreme caution. This option exists primarily for running test suites remotely.</p>
<dt><code>-audit </code><i>level</i></p>
<dd>sets the audit trail level. The default level is 1, meaning only connection rejections are reported. Level 2 additionally reports all successful connections and disconnects. Level 4 enables messages from the SECURITY extension, if present, including generation and revocation of authorizations and violations of the security policy. Level 0 turns off the audit trail. Audit lines are sent as standard error output.</p>
<dt><code>-auth </code><i>authorization-file</i></p>
<dd>specifies a file which contains a collection of authorization records used to authenticate access. See also the <i><a href="/docs/linux/man/1-xdm/">xdm</a></i>(1) and <i><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></i>(7) manual pages.</p>
<dt><code>-background none</code></p>
<dd>Asks the driver not to clear the background on startup, if the driver supports that. May be useful for smooth transition with eg. fbdev driver. For security reasons this is not the default as the screen contents might show a previous user session.</p>
<dt><code>-br</code></p>
<dd>sets the default root window to solid black instead of the standard root weave pattern. This is the default unless -retro or -wr is specified.</p>
<dt><code>-bs</code></p>
<dd>disables backing store support on all screens.</p>
<dt><code>-c</code></p>
<dd>turns off key-click.</p>
<dt><code>c </code><i>volume</i></p>
<dd>sets key-click volume (allowable range: 0-100).</p>
<dt><code>-cc </code><i>class</i></p>
<dd>sets the visual class for the root window of color screens. The class numbers are as specified in the X protocol. Not obeyed by all servers.</p>
<dt><code>-core</code></p>
<dd>causes the server to generate a core dump on fatal errors.</p>
<dt><code>-displayfd </code><i>fd</i></p>
<dd>specifies a file descriptor in the launching process. Rather than specify a display number, the X server will attempt to listen on successively higher display numbers, and upon finding a free one, will write the display number back on this file descriptor as a newline-terminated string. The -pn option is ignored when using -displayfd.</p>
<dt><code>-deferglyphs </code><i>whichfonts</i></p>
<dd>specifies the types of fonts for which the server should attempt to use deferred glyph loading. <i>whichfonts</i> can be all (all fonts), none (no fonts), or 16 (16 bit fonts only).</p>
<dt><code>-dpi </code><i>resolution</i></p>
<dd>sets the resolution for all screens, in dots per inch. To be used when the server cannot determine the screen size(s) from the hardware.</p>
<dt><code>dpms</code></p>
<dd>enables DPMS (display power management services), where supported. The default state is platform and configuration specific.</p>
<dt><code>-dpms</code></p>
<dd>disables DPMS (display power management services). The default state is platform and configuration specific.</p>
<dt><code>-extension</code><i>extensionName</i></p>
<dd>disables named extension. If an unknown extension name is specified, a list of accepted extension names is printed.</p>
<dt><code>+extension</code><i>extensionName</i></p>
<dd>enables named extension. If an unknown extension name is specified, a list of accepted extension names is printed.</p>
<dt><code>-f </code><i>volume</i></p>
<dd>sets beep (bell) volume (allowable range: 0-100).</p>
<dt><code>-fakescreenfps </code>ps</p>
<dd>sets fake presenter screen default fps (allowable range: 1-600).</p>
<dt><code>-fp </code><i>fontPath</i></p>
<dd>sets the search path for fonts. This path is a comma separated list of directories which the X server searches for font databases. See the FONTS section of this manual page for more information and the default list.</p>
<dt><code>-help</code></p>
<dd>prints a usage message.</p>
<dt><code>-I</code></p>
<dd>causes all remaining command line arguments to be ignored.</p>
<dt><code>-iglx</code></p>
<dd>Prohibit creating indirect GLX contexts. Indirect GLX is of limited use, since it lacks support for many modern OpenGL features and extensions; it&#8217;s slower than direct contexts; and it opens a large attack surface for protocol parsing errors. This is the default unless +iglx is specified.</p>
<dt><code>+iglx</code></p>
<dd>Allow creating indirect GLX contexts.</p>
<dt><code>-maxbigreqsize </code><i>size</i></p>
<dd>sets the maximum big request to <i>size</i> MB.</p>
<dt><code>-nocursor</code></p>
<dd>disable the display of the pointer cursor.</p>
<dt><code>-nolisten </code><i>trans-type</i></p>
<dd>disables a transport type. For example, TCP/IP connections can be disabled with <code>-nolisten tcp</code>. This option may be issued multiple times to disable listening to different transport types. Supported transport types are platform dependent, but commonly include: </p>
<table>
<tr VALIGN=top>
<td>tcp TCP over IPv4 or IPv6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>inet TCP over IPv4 only</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>inet6 TCP over IPv6 only</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>unix UNIX Domain Sockets</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>local Platform preferred local connection method</td>
<td>
</td>
</tr>
</table>
<dt><code>-listen </code><i>trans-type</i></p>
<dd>enables a transport type. For example, TCP/IP connections can be enabled with <code>-listen tcp</code>. This option may be issued multiple times to enable listening to different transport types.</p>
<dt><code>-noreset</code></p>
<dd>prevents a server reset when the last client connection is closed. This overrides a previous <code>-terminate</code> command line option.</p>
<dt><code>-p </code><i>minutes</i></p>
<dd>sets screen-saver pattern cycle time in minutes.</p>
<dt><code>-pn</code></p>
<dd>permits the server to continue running if it fails to establish all of its well-known sockets (connection points for clients), but establishes at least one. This option is set by default.</p>
<dt><code>-nopn</code></p>
<dd>causes the server to exit if it fails to establish all of its well-known sockets (connection points for clients).</p>
<dt><code>-r</code></p>
<dd>turns off auto-repeat.</p>
<dt><code>r</code></p>
<dd>turns on auto-repeat.</p>
<dt><code>-retro</code></p>
<dd>starts the server with the classic stipple and cursor visible. The default is to start with a black root window, and to suppress display of the cursor until the first time an application calls XDefineCursor(). For kdrive servers, this implies -zap.</p>
<dt><code>-s </code><i>minutes</i></p>
<dd>sets screen-saver timeout time in minutes.</p>
<dt><code>-su</code></p>
<dd>disables save under support on all screens.</p>
<dt><code>-seat </code><i>seat</i></p>
<dd>seat to run on. Takes a string identifying a seat in a platform specific syntax. On platforms which support this feature this may be used to limit the server to expose only a specific subset of devices connected to the system.</p>
<dt><code>-t </code><i>number</i></p>
<dd>sets pointer acceleration threshold in pixels (i.e. after how many pixels pointer acceleration should take effect).</p>
<dt><code>-terminate </code><i>[delay]</i></p>
<dd>causes the server to terminate at server reset, instead of continuing to run. This overrides a previous <code>-noreset</code> command line option. If a delay in seconds is specified, the server waits for at least the delay. At the end of this grace period if no client is connected, the server terminates immediately.</p>
<dt><code>-tst</code></p>
<dd>disables all testing extensions (e.g., XTEST, XTrap, XTestExtension1, RECORD).</p>
<dt><code>tty</code><i>xx</i></p>
<dd>ignored, for servers started the ancient way (from init).</p>
<dt><code>v</code></p>
<dd>sets video-off screen-saver preference.</p>
<dt><code>-v</code></p>
<dd>sets video-on screen-saver preference.</p>
<dt><code>-wr</code></p>
<dd>sets the default root window to solid white instead of the standard root weave pattern.</p>
<dt><code>-x </code><i>extension</i></p>
<dd>loads the specified extension at init. This is a no-op for most implementations.</p>
<dt><code>[+-]xinerama</code></p>
<dd>enables(+) or disables(-) the XINERAMA extension. The default state is platform and configuration specific.</dl>
<h2>Server Dependent Options</h2>
<p>Some X servers accept the following options:</p>
<dl>
<dt><code>-ld </code><i>kilobytes</i></p>
<dd>sets the data space limit of the server to the specified number of kilobytes. A value of zero makes the data size as large as possible. The default value of -1 leaves the data space limit unchanged.</p>
<dt><code>-lf </code><i>files</i></p>
<dd>sets the number-of-open-files limit of the server to the specified number. A value of zero makes the limit as large as possible. The default value of -1 leaves the limit unchanged.</p>
<dt><code>-ls </code><i>kilobytes</i></p>
<dd>sets the stack space limit of the server to the specified number of kilobytes. A value of zero makes the stack size as large as possible. The default value of -1 leaves the stack space limit unchanged.</p>
<dt><code>-maxclients</code></p>
<dd><code>64</code>|<code>128</code>|<code>256</code>|<code>512</code> Set the maximum number of clients allowed to connect to the X server. Acceptable values are 64, 128, 256 or 512.</p>
<dt><code>-render</code></p>
<dd><code>default</code>|<code>mono</code>|<code>gray</code>|<code>color</code> sets the color allocation policy that will be used by the render extension.</p>
<dl>
<dd>
<dl>
<dt><i>default</i></p>
<dd>selects the default policy defined for the display depth of the X server.</p>
<dt><i>mono</i></p>
<dd>don&#8217;t use any color cell.</p>
<dt><i>gray</i></p>
<dd>use a gray map of 13 color cells for the X render extension.</p>
<dt><i>color</i></p>
<dd>use a color cube of at most 4*4*4 colors (that is 64 color cells).</dl>
</dl>
<dt><code>-dumbSched</code></p>
<dd>disables smart scheduling on platforms that support the smart scheduler.</p>
<dt><code>-schedInterval </code><i>interval</i></p>
<dd>sets the smart scheduler&#8217;s scheduling interval to <i>interval</i> milliseconds.</dl>
<h2>Xdmcp Options</h2>
<p>X servers that support XDMCP have the following options. See the <i>X Display Manager Control Protocol</i> specification for more information.</p>
<dl>
<dt><code>-query </code><i>hostname</i></p>
<dd>enables XDMCP and sends Query packets to the specified <i>hostname</i>.</p>
<dt><code>-broadcast</code></p>
<dd>enable XDMCP and broadcasts BroadcastQuery packets to the network. The first responding display manager will be chosen for the session.</p>
<dt><code>-multicast [</code><i>address</i> [<i>hop count</i>]]</p>
<dd>Enable XDMCP and multicast BroadcastQuery packets to the network. The first responding display manager is chosen for the session. If an address is specified, the multicast is sent to that address. If no address is specified, the multicast is sent to the default XDMCP IPv6 multicast group. If a hop count is specified, it is used as the maximum hop count for the multicast. If no hop count is specified, the multicast is set to a maximum of 1 hop, to prevent the multicast from being routed beyond the local network.</p>
<dt><code>-indirect </code><i>hostname</i></p>
<dd>enables XDMCP and send IndirectQuery packets to the specified <i>hostname</i>.</p>
<dt><code>-port </code><i>port-number</i></p>
<dd>uses the specified <i>port-number</i> for XDMCP packets, instead of the default. This option must be specified before any -query, -broadcast, -multicast, or -indirect options.</p>
<dt><code>-from </code><i>local-address</i></p>
<dd>specifies the local address to connect from (useful if the connecting host has multiple network interfaces). The <i>local-address</i> may be expressed in any form acceptable to the host platform&#8217;s <i><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></i>(3) implementation.</p>
<dt><code>-once</code></p>
<dd>causes the server to terminate (rather than reset) when the XDMCP session ends.</p>
<dt><code>-class </code><i>display-class</i></p>
<dd>XDMCP has an additional display qualifier used in resource lookup for display-specific options. This option sets that value, by default it is &quot;MIT-unspecified&quot; (not a very useful value).</p>
<dt><code>-cookie </code><i>xdm-auth-bits</i></p>
<dd>When testing XDM-AUTHENTICATION-1, a private key is shared between the server and the manager. This option sets the value of that private data (not that it is very private, being on the command line!).</p>
<dt><code>-displayID </code><i>display-id</i></p>
<dd>Yet another XDMCP specific value, this one allows the display manager to identify each display so that it can locate the shared key.</dl>
<h2>Xkeyboard Options</h2>
<p>X servers that support the XKEYBOARD (a.k.a. &#34;XKB&#34;) extension accept the following options. All layout files specified on the command line must be located in the XKB base directory or a subdirectory, and specified as the relative path from the XKB base directory. The default XKB base directory is <i>/usr/lib/X11/xkb</i>.</p>
<dl>
<dt><code>[+-]accessx</code> [ <i>timeout</i> [ <i>timeout_mask</i> [ <i>feedback</i> [ <i>options_mask</i> ] ] ] ]</p>
<dd>enables(+) or disables(-) AccessX key sequences.</p>
<dt><code>-xkbdir </code><i>directory</i></p>
<dd>base directory for keyboard layout files. This option is not available for setuid X servers (i.e., when the X server&#8217;s real and effective uids are different).</p>
<dt><code>-ardelay </code><i>milliseconds</i></p>
<dd>sets the autorepeat delay (length of time in milliseconds that a key must be depressed before autorepeat starts).</p>
<dt><code>-arinterval </code><i>milliseconds</i></p>
<dd>sets the autorepeat interval (length of time in milliseconds that should elapse between autorepeat-generated keystrokes).</p>
<dt><code>-xkbmap </code><i>filename</i></p>
<dd>loads keyboard description in <i>filename</i> on server startup.</dl>
<h2>Network Connections</h2>
<p>The X server supports client connections via a platform-dependent subset of the following transport types: TCP/IP, Unix Domain sockets, and several varieties of SVR4 local connections. See the DISPLAY NAMES section of the <i><a href="/docs/linux/man/7-x/">X</a></i>(7) manual page to learn how to specify which transport type clients should try to use.</p>
<h2>Granting Access</h2>
<p>The X server implements a platform-dependent subset of the following authorization protocols: MIT-MAGIC-COOKIE-1, XDM-AUTHORIZATION-1, XDM-AUTHORIZATION-2, SUN-DES-1, and MIT-KERBEROS-5. See the <i><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></i>(7) manual page for information on the operation of these protocols. </p>
<p> Authorization data required by the above protocols is passed to the server in a private file named with the <code>-auth</code> command line option. Each time the server is about to accept the first connection after a reset (or when the server is starting), it reads this file. If this file contains any authorization records, the local host is not automatically allowed access to the server, and only clients which send one of the authorization records contained in the file in the connection setup information will be allowed access. See the <i>Xau</i> manual page for a description of the binary format of this file. See <i><a href="/docs/linux/man/1-xauth/">xauth</a></i>(1) for maintenance of this file, and distribution of its contents to remote hosts. </p>
<p> The X server also uses a host-based access control list for deciding whether or not to accept connections from clients on a particular machine. If no other authorization mechanism is being used, this list initially consists of the host on which the server is running as well as any machines listed in the file <i>/etc/X</i><code>n</code><i>.hosts</i>, where <code>n</code> is the display number of the server. Each line of the file should contain either an Internet hostname (e.g. expo.lcs.mit.edu) or a complete name in the format <i>family</i>:<i>name</i> as described in the <i><a href="/docs/linux/man/1-xhost/">xhost</a></i>(1) manual page. There should be no leading or trailing spaces on any lines. For example: </p>
<pre>joesworkstation
corporate.company.com
inet:bigcpu
local:</pre>
<p>Users can add or remove hosts from this list and enable or disable access control using the <i>xhost</i> command from the same machine as the server. </p>
<p> If the X FireWall Proxy (<i>xfwp</i>) is being used without a sitepolicy, host-based authorization must be turned on for clients to be able to connect to the X server via the <i>xfwp</i>. If <i>xfwp</i> is run without a configuration file and thus no sitepolicy is defined, if <i>xfwp</i> is using an X server where xhost + has been run to turn off host-based authorization checks, when a client tries to connect to this X server via <i>xfwp</i>, the X server will deny the connection. See <i><a href="/docs/linux/man/1-xfwp/">xfwp</a></i>(1) for more information about this proxy. </p>
<p> The X protocol intrinsically does not have any notion of window operation permissions or place any restrictions on what a client can do; if a program can connect to a display, it has full run of the screen. X servers that support the SECURITY extension fare better because clients can be designated untrusted via the authorization they use to connect; see the <i><a href="/docs/linux/man/1-xauth/">xauth</a></i>(1) manual page for details. Restrictions are imposed on untrusted clients that curtail the mischief they can do. See the SECURITY extension specification for a complete list of these restrictions. </p>
<p> Sites that have better authentication and authorization systems might wish to make use of the hooks in the libraries and the server to provide additional security models.</p>
<h2>Signals</h2>
<p>The X server attaches special meaning to the following signals:</p>
<dl>
<dt><i>SIGHUP</i></p>
<dd>This signal causes the server to close all existing connections, free all resources, and restore all defaults. It is sent by the display manager whenever the main user&#8217;s main application (usually an <i>xterm</i> or window manager) exits to force the server to clean up and prepare for the next user.</p>
<dt><i>SIGTERM</i></p>
<dd>This signal causes the server to exit cleanly.</p>
<dt><i>SIGUSR1</i></p>
<dd>This signal is used quite differently from either of the above. When the server starts, it checks to see if it has inherited SIGUSR1 as SIG_IGN instead of the usual SIG_DFL. In this case, the server sends a SIGUSR1 to its parent process after it has set up the various connection schemes. <i>Xdm</i> uses this feature to recognize when connecting to the server is possible.</dl>
<h2>Fonts</h2>
<p>The X server can obtain fonts from directories and/or from font servers. The list of directories and font servers the X server uses when trying to open a font is controlled by the <i>font path</i>. </p>
<p> The default font path is /usr/share/fonts/X11/misc,/usr/share/fonts/X11/cyrillic,/usr/share/fonts/X11/100dpi/:unscaled,/usr/share/fonts/X11/75dpi/:unscaled,/usr/share/fonts/X11/Type1,/usr/share/fonts/X11/100dpi,/usr/share/fonts/X11/75dpi,built-ins . </p>
<p> A special kind of directory can be specified using the <code>catalogue</code>: prefix. Directories specified this way can contain symlinks pointing to the real font directories. See the FONTPATH.D section for details. </p>
<p> The font path can be set with the <code>-fp</code> option or by <i><a href="/docs/linux/man/1-xset/">xset</a></i>(1) after the server has started.</p>
<h2>Fontpath.D</h2>
<p>You can specify a special kind of font path in the form <code>catalogue:&lt;dir&gt;</code>. The directory specified after the catalogue: prefix will be scanned for symlinks and each symlink destination will be added as a local fontfile FPE. </p>
<p> The symlink can be suffixed by attributes such as &#8216;<code>unscaled</code>&#8216;, which will be passed through to the underlying fontfile FPE. The only exception is the newly introduced &#8216;<code>pri</code>&#8216; attribute, which will be used for ordering the font paths specified by the symlinks. </p>
<p> An example configuration: </p>
<pre> 75dpi:unscaled:pri=20 -&gt; /usr/share/X11/fonts/75dpi
 ghostscript:pri=60 -&gt; /usr/share/fonts/default/ghostscript
 misc:unscaled:pri=10 -&gt; /usr/share/X11/fonts/misc
 type1:pri=40 -&gt; /usr/share/X11/fonts/Type1
 type1:pri=50 -&gt; /usr/share/fonts/default/Type1</pre>
<p>This will add /usr/share/X11/fonts/misc as the first FPE with the attribute &#39;unscaled&#8217;, second FPE will be /usr/share/X11/fonts/75dpi, also with the attribute &#8216;unscaled&#8217; etc. This is functionally equivalent to setting the following font path: </p>
<pre> /usr/share/X11/fonts/misc:unscaled,
 /usr/share/X11/fonts/75dpi:unscaled,
 /usr/share/X11/fonts/Type1,
 /usr/share/fonts/default/Type1,
 /usr/share/fonts/default/ghostscript</pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/X</i><code>n</code>.hosts</p>
<dd>Initial access control list for display number <code>n</code></p>
<dt><i>/usr/share/fonts/X11/misc</i>,<i>/usr/share/fonts/X11/75dpi</i>,<i>/usr/share/fonts/X11/100dpi</i></p>
<dd>Bitmap font directories</p>
<dt><i>/usr/share/fonts/X11/TTF</i>,<i>/usr/share/fonts/X11/Type1</i></p>
<dd>Outline font directories</p>
<dt><i>/tmp/.X11-unix/X</i><code>n</code></p>
<dd>Unix domain socket for display number <code>n</code></p>
<dt><i>/usr/adm/X</i><code>n</code>msgs</p>
<dd>Error log file for display number <code>n</code> if run from <i><a href="/docs/linux/man/8-init/">init</a></i>(8)</p>
<dt><i>/usr/lib/X11/xdm/xdm-errors</i></p>
<dd>Default error log file if the server is run from <i><a href="/docs/linux/man/1-xdm/">xdm</a></i>(1)</dl>
<h2>See Also</h2>
<p>General information: <i><a href="/docs/linux/man/7-x/">X</a></i>(7) </p>
<p> Protocols: <i>X Window System Protocol,</i> <i>The X Font Service Protocol,</i> <i>X Display Manager Control Protocol</i> </p>
<p> Fonts: <i><a href="/docs/linux/man/1-bdftopcf/">bdftopcf</a></i>(1), <i><a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a></i>(1), <i><a href="/docs/linux/man/1-mkfontscale/">mkfontscale</a></i>(1), <i><a href="/docs/linux/man/1-xfs/">xfs</a></i>(1), <i><a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a></i>(1), <i><a href="/docs/linux/man/1-xfontsel/">xfontsel</a></i>(1), <i><a href="/docs/linux/man/1-xfd/">xfd</a></i>(1), <i>X Logical Font Description Conventions</i> </p>
<p> Keyboards: <i><a href="/docs/linux/man/7-xkeyboard-config/">xkeyboard-config</a></i>(7) </p>
<p> Security: <i><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></i>(7), <i><a href="/docs/linux/man/1-xauth/">xauth</a></i>(1), <i><a href="/docs/linux/man/1-xau/">Xau</a></i>(1), <i><a href="/docs/linux/man/1-xdm/">xdm</a></i>(1), <i><a href="/docs/linux/man/1-xhost/">xhost</a></i>(1), <i><a href="/docs/linux/man/1-xfwp/">xfwp</a></i>(1), <i>Security Extension Specification</i> </p>
<p> Starting the server: <i><a href="/docs/linux/man/1-startx/">startx</a></i>(1), <i><a href="/docs/linux/man/1-xdm/">xdm</a></i>(1), <i><a href="/docs/linux/man/1-xinit/">xinit</a></i>(1) </p>
<p> Controlling the server once started: <i><a href="/docs/linux/man/1-xset/">xset</a></i>(1), <i><a href="/docs/linux/man/1-xsetroot/">xsetroot</a></i>(1), <i><a href="/docs/linux/man/1-xhost/">xhost</a></i>(1), <i><a href="/docs/linux/man/1-xinput/">xinput</a></i>(1), <i><a href="/docs/linux/man/1-xrandr/">xrandr</a></i>(1) </p>
<p> Server-specific man pages: <i><a href="/docs/linux/man/1-xorg/">Xorg</a></i>(1), <i><a href="/docs/linux/man/1-xephyr/">Xephyr</a></i>(1), <i><a href="/docs/linux/man/1-xnest/">Xnest</a></i>(1), <i><a href="/docs/linux/man/1-xvfb/">Xvfb</a></i>(1), <i><a href="/docs/linux/man/1-xquartz/">Xquartz</a></i>(1), <i><a href="/docs/linux/man/1-xwin/">XWin</a></i>(1). </p>
<p> Server internal documentation: <i>Definition of the Porting Layer for the X v11 Sample Server</i></p>
<h2>Authors</h2>
<p>The sample server was originally written by Susan Angebranndt, Raymond Drewry, Philip Karlton, and Todd Newman, from Digital Equipment Corporation, with support from a large cast. It has since been extensively rewritten by Keith Packard and Bob Scheifler, from MIT. Dave Wiggins took over post-R5 and made substantial improvements.</p>
