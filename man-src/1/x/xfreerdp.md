---
title: "xfreerdp(1)"
name: "xfreerdp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfreerdp/"
description: "xfreerdp – FreeRDP X11 client"
---

<h2 class="name">NAME</h2>
<p> xfreerdp &#8211; FreeRDP X11 client </p>
<h2>SYNOPSIS</h2>
<p> <code>xfreerdp</code> [options] server[:port]</p>
<h2>DESCRIPTION</h2>
<p> <code>xfreerdp</code> is an X11 Remote Desktop Protocol (RDP) client which is part of the FreeRDP project. An RDP server is built-in to many editions of Windows. Alternative servers included xrdp and VRDP (VirtualBox).</p>
<h2>OPTIONS</h2>
<p> -0</p>
<dl>
<dt>
<dd> Attach to the admin console of the server.</dl>
<p> -a <i>bpp</i></p>
<dl>
<dt>
<dd> Sets the color depth for the connection to <i>bpp</i> bits per pixel. Valid values are 8, 15, 16, 24 and 32. The default value is the color depth of the FreeRDP-window.</dl>
<p> -c <i>dir</i></p>
<dl>
<dt>
<dd> Sets the working-dir to <i>dir</i>. This parameter is only used when an AlternateShell (-s <i>shell</i>) is requested. <i>dir</i> should contain the executable file specified in the AlternateShell.</dl>
<p> -D</p>
<dl>
<dt>
<dd> Removes the windows decorations.</dl>
<p> -d <i>domain</i></p>
<dl>
<dt>
<dd> Set the domain used in authentication to <i>domain</i>.</dl>
<p> -f</p>
<dl>
<dt>
<dd> start in full screen mode. This mode can always be en- and disabled using Ctrl-Alt-Enter.</dl>
<p> -T <i>text</i></p>
<dl>
<dt>
<dd> Sets the window title to <i>text</i>.</dl>
<p> -g <i>geometry</i></p>
<dl>
<dt>
<dd> Sets the size of the FreeRDP window (and of the remote desktop, when establishing a new connection). <i>geometry</i> can have one of the following forms: </p>
<p> <i>W</i>x<i>H</i></p>
<dl>
<dt>
<dd> in this case the resulting window will be of <i>W</i>x<i>H</i> pixels.</dl>
<p> <i>P</i>%</p>
<dl>
<dt>
<dd> in this case the resulting window will be <i>P</i>% of your screen.</dl>
<p> The special keyword <i>workarea</i></p>
<dl>
<dt>
<dd> in this case the resulting window will be of the same size as your workarea.</dl>
</dl>
<p> -h</p>
<dl>
<dt>
<dd> Print help.</dl>
<p> -k <i>id</i></p>
<dl>
<dt>
<dd> Sets the keyboard-layout-id to <i>id</i>.</dl>
<p> -K</p>
<dl>
<dt>
<dd> Do not interfere with window manager bindings (don&#8217;t grab keyboard).</dl>
<p> -n <i>hostname</i></p>
<dl>
<dt>
<dd> Set the reported client hostname to <i>hostname</i>. Default is to automatically detect the hostname.</dl>
<p> -o</p>
<dl>
<dt>
<dd> Play audio on the console instead of redirecting to the client.</dl>
<p> -p <i>password</i></p>
<dl>
<dt>
<dd> Password used in authentication.</dl>
<p> -s <i>shell</i></p>
<dl>
<dt>
<dd> Sets the startup-shell to <i>shell</i>. This parameter should contain a complete path to the alternate shell. If the alternete shell requires a different working directory use -c <i>dir</i>.</dl>
<p> -t <i>port</i></p>
<dl>
<dt>
<dd> Connect to <i>port</i>, instead of the default 3389.</dl>
<p> -u <i>username</i></p>
<dl>
<dt>
<dd> Username used in authentication.</dl>
<p> -x <i>flag</i></p>
<dl>
<dt>
<dd> Set the experience performance flags. <i>flag</i> can be one of: </p>
<p> m &#8211; (modem)</p>
<dl>
<dt>
<dd> Equivalent to 15.</dl>
<p> b &#8211; (broadband)</p>
<dl>
<dt>
<dd> Equivalent to 1.</dl>
<p> l &#8211; (lan)</p>
<dl>
<dt>
<dd> Equivalent to 0.</dl>
<p> <i>num</i></p>
<dl>
<dt>
<dd> A hexadecimal number that represents a bit-mask, were numbers mean the following <font SIZE="-2">[1]</font>: </p>
<p> 1</p>
<dl>
<dt>
<dd> Disable desktop wallpaper.</dl>
<p> 2</p>
<dl>
<dt>
<dd> Disable full-window drag (only the window outline is displayed when the window is moved).</dl>
<p> 4</p>
<dl>
<dt>
<dd> Disable menu animations.</dl>
<p> 8</p>
<dl>
<dt>
<dd> Disable user interface themes.</dl>
<p> 20</p>
<dl>
<dt>
<dd> Disable mouse cursor shadows.</dl>
<p> 40</p>
<dl>
<dt>
<dd> Disable cursor blinking.</dl>
<p> 80</p>
<dl>
<dt>
<dd> Enable font smoothing.</dl>
<p> 100</p>
<dl>
<dt>
<dd> Enable Desktop Composition.</dl>
</dl>
</dl>
<p> -X <i>xid</i></p>
<dl>
<dt>
<dd> embed xfreerdp into window with <i>xid</i>.</dl>
<p> -z</p>
<dl>
<dt>
<dd> Enable compression.</dl>
<p> &#8211;app</p>
<dl>
<dt>
<dd> initialize a RemoteApp connection. This implies -g workarea.</dl>
<p> &#8211;no-auth</p>
<dl>
<dt>
<dd> Skips authentication. This is useful e.g. for the current FreeRDP server that doesn&#8217;t yet support server-side authentication.</dl>
<p> &#8211;authonly</p>
<dl>
<dt>
<dd> Only authenticates. This is useful to test your credentials (username and password). Returns status code 0 if the client can connect. Requires a username, password and connection host at the command line.</dl>
<p> &#8211;no-bmp-cache</p>
<dl>
<dt>
<dd> Disable bitmap cache.</dl>
<p> &#8211;certificate-name <i>name</i></p>
<dl>
<dt>
<dd> use <i>name</i> for the logon certificate, instead of the server name</dl>
<p> &#8211;composition</p>
<dl>
<dt>
<dd> Enable composition (RDVH only, not to be confused with remote composition).</dl>
<p> &#8211;ext <i>extname</i></p>
<dl>
<dt>
<dd> load extension <i>extname</i></dl>
<p> &#8211;no-fastpath</p>
<dl>
<dt>
<dd> Disables fast-path. Use slow-path packets instead, which have larger headers. It might be good for debugging certain issues when you suspect it might be linked to the parsing of one of the two header types.</dl>
<p> &#8211;from-stdin</p>
<dl>
<dt>
<dd> Prompts for unspecified arguments -u username, -p password, -d domain and connection host. This is useful to hide arguments from ps. Also useful for scripts that will feed these arguments to the client via (what else?) stdin.</dl>
<p> &#8211;disable-full-window-drag</p>
<dl>
<dt>
<dd> Disable full window drag.</dl>
<p> &#8211;gdi <i>backend</i></p>
<dl>
<dt>
<dd> GDI (Graphics Device Interface) rendering backend. <i>backend</i> can be either sw (software) or hw (hardware).</dl>
<p> &#8211;help</p>
<dl>
<dt>
<dd> Print help.</dl>
<p> &#8211;ignore-certificate</p>
<dl>
<dt>
<dd> ignore verification of logon certificate.</dl>
<p> &#8211;kbd-list</p>
<dl>
<dt>
<dd> list all keyboard layout ids used by -k</dl>
<p> &#8211;disable-menu-animations</p>
<dl>
<dt>
<dd> Disable menu animations.</dl>
<p> &#8211;no-motion</p>
<dl>
<dt>
<dd> Don&#8217;t send mouse motion events.</dl>
<p> &#8211;no-nla</p>
<dl>
<dt>
<dd> Disable network level authentication.</dl>
<p> &#8211;nsc</p>
<dl>
<dt>
<dd> Enable NSCodec.</dl>
<p> &#8211;no-osb</p>
<dl>
<dt>
<dd> Disable off screen bitmaps.</dl>
<p> &#8211;plugin <i>pluginname</i></p>
<dl>
<dt>
<dd> Load <i>pluginname</i> </p>
<p> In Red Hat Enterprise Linux 6, the following plugins are available: </p>
<p> cliprdr</p>
<dl>
<dt>
<dd> Clipboard support</dl>
<p> drdynvc</p>
<dl>
<dt>
<dd> Used for multimedia redirection</dl>
<p> rdpsnd</p>
<dl>
<dt>
<dd> For audio output</dl>
<p> rail</p>
<dl>
<dt>
<dd> Remote Applications Integrated Locally</dl>
<p> rdpdbg</p>
<dl>
<dt>
<dd> Debugging Virtual Channel</dl>
<p> rdpdr</p>
<dl>
<dt>
<dd> File System Support</dl>
<p> As an example, </p>
<p> <code>xfreerdp</code> &#8211;plugin rdpsnd <i>server</i> </p>
<p> will enable audio output using the PulseAudio backend of the rdpsnd plugin. Please Note that Red Hat Enterprise Linux 6 does not include support for the ALSA backend of the rdpsnd plugin.</dl>
<p> &#8211;no-rdp</p>
<dl>
<dt>
<dd> Disable Standard RDP encryption.</dl>
<p> &#8211;rfx</p>
<dl>
<dt>
<dd> Enable RemoteFX.</dl>
<p> &#8211;rfx-mode</p>
<dl>
<dt>
<dd> RemoteFX operational flags. <i>flags</i> can be either v[ideo], i[mage]), default is video.</dl>
<p> &#8211;ntlm <i>version</i></p>
<dl>
<dt>
<dd> Force NTLM protocol version to be <i>version</i>, which can be one of 1 or 2.</dl>
<p> &#8211;sec <i>proto</i></p>
<dl>
<dt>
<dd> Force protocol security. <i>proto</i> can be one of rdp, tls or nla.</dl>
<p> &#8211;secure-checksum</p>
<dl>
<dt>
<dd> Use salted checksums with Standard RDP encryption.</dl>
<p> &#8211;disable-theming</p>
<dl>
<dt>
<dd> Disable theming.</dl>
<p> &#8211;no-tls</p>
<dl>
<dt>
<dd> Disable TLS encryption.</dl>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Print version information.</dl>
<p> &#8211;disable-wallpaper</p>
<dl>
<dt>
<dd> Disable wallpaper.</dl>
<h2>LINKS</h2>
<p> m[blue]<code><a rel="nofollow" href="http://www.freerdp.com/">http://www.freerdp.com/</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> The FreeRDP Team</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Taken from m[blue]<code>MS-RDPBCGR Section 2.2.1.11.1.1.1 &#8211; Extended Info Packet</code>m[]</p>
<dt> 2.</p>
<dd> MS-RDPBCGR Section 2.2.1.11.1.1.1 &#8211; Extended Info Packet</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://msdn.microsoft.com/en-us/library/cc240476%28v=prot.10%29.aspx">http://msdn.microsoft.com/en-us/library/cc240476%28v=prot.10%29.aspx</a></dl>
</dl>
<h2>Index</h2>
