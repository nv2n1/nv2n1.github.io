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
</dt><dd> Attach to the admin console of the server.</dd></dl>
<p> -a <i>bpp</i></p>
<dl>
<dt>
</dt><dd> Sets the color depth for the connection to <i>bpp</i> bits per pixel. Valid values are 8, 15, 16, 24 and 32. The default value is the color depth of the FreeRDP-window.</dd></dl>
<p> -c <i>dir</i></p>
<dl>
<dt>
</dt><dd> Sets the working-dir to <i>dir</i>. This parameter is only used when an AlternateShell (-s <i>shell</i>) is requested. <i>dir</i> should contain the executable file specified in the AlternateShell.</dd></dl>
<p> -D</p>
<dl>
<dt>
</dt><dd> Removes the windows decorations.</dd></dl>
<p> -d <i>domain</i></p>
<dl>
<dt>
</dt><dd> Set the domain used in authentication to <i>domain</i>.</dd></dl>
<p> -f</p>
<dl>
<dt>
</dt><dd> start in full screen mode. This mode can always be en- and disabled using Ctrl-Alt-Enter.</dd></dl>
<p> -T <i>text</i></p>
<dl>
<dt>
</dt><dd> Sets the window title to <i>text</i>.</dd></dl>
<p> -g <i>geometry</i></p>
<dl>
<dt>
</dt><dd> Sets the size of the FreeRDP window (and of the remote desktop, when establishing a new connection). <i>geometry</i> can have one of the following forms: </dd>
<p> <i>W</i>x<i>H</i></p>
<dl>
<dt>
</dt><dd> in this case the resulting window will be of <i>W</i>x<i>H</i> pixels.</dd></dl>
<p> <i>P</i>%</p>
<dl>
<dt>
</dt><dd> in this case the resulting window will be <i>P</i>% of your screen.</dd></dl>
<p> The special keyword <i>workarea</i></p>
<dl>
<dt>
</dt><dd> in this case the resulting window will be of the same size as your workarea.</dd></dl>
</dl>
<p> -h</p>
<dl>
<dt>
</dt><dd> Print help.</dd></dl>
<p> -k <i>id</i></p>
<dl>
<dt>
</dt><dd> Sets the keyboard-layout-id to <i>id</i>.</dd></dl>
<p> -K</p>
<dl>
<dt>
</dt><dd> Do not interfere with window manager bindings (don&#8217;t grab keyboard).</dd></dl>
<p> -n <i>hostname</i></p>
<dl>
<dt>
</dt><dd> Set the reported client hostname to <i>hostname</i>. Default is to automatically detect the hostname.</dd></dl>
<p> -o</p>
<dl>
<dt>
</dt><dd> Play audio on the console instead of redirecting to the client.</dd></dl>
<p> -p <i>password</i></p>
<dl>
<dt>
</dt><dd> Password used in authentication.</dd></dl>
<p> -s <i>shell</i></p>
<dl>
<dt>
</dt><dd> Sets the startup-shell to <i>shell</i>. This parameter should contain a complete path to the alternate shell. If the alternete shell requires a different working directory use -c <i>dir</i>.</dd></dl>
<p> -t <i>port</i></p>
<dl>
<dt>
</dt><dd> Connect to <i>port</i>, instead of the default 3389.</dd></dl>
<p> -u <i>username</i></p>
<dl>
<dt>
</dt><dd> Username used in authentication.</dd></dl>
<p> -x <i>flag</i></p>
<dl>
<dt>
</dt><dd> Set the experience performance flags. <i>flag</i> can be one of: </dd>
<p> m &#8211; (modem)</p>
<dl>
<dt>
</dt><dd> Equivalent to 15.</dd></dl>
<p> b &#8211; (broadband)</p>
<dl>
<dt>
</dt><dd> Equivalent to 1.</dd></dl>
<p> l &#8211; (lan)</p>
<dl>
<dt>
</dt><dd> Equivalent to 0.</dd></dl>
<p> <i>num</i></p>
<dl>
<dt>
</dt><dd> A hexadecimal number that represents a bit-mask, were numbers mean the following <font SIZE="-2">[1]</font>: </dd>
<p> 1</p>
<dl>
<dt>
</dt><dd> Disable desktop wallpaper.</dd></dl>
<p> 2</p>
<dl>
<dt>
</dt><dd> Disable full-window drag (only the window outline is displayed when the window is moved).</dd></dl>
<p> 4</p>
<dl>
<dt>
</dt><dd> Disable menu animations.</dd></dl>
<p> 8</p>
<dl>
<dt>
</dt><dd> Disable user interface themes.</dd></dl>
<p> 20</p>
<dl>
<dt>
</dt><dd> Disable mouse cursor shadows.</dd></dl>
<p> 40</p>
<dl>
<dt>
</dt><dd> Disable cursor blinking.</dd></dl>
<p> 80</p>
<dl>
<dt>
</dt><dd> Enable font smoothing.</dd></dl>
<p> 100</p>
<dl>
<dt>
</dt><dd> Enable Desktop Composition.</dd></dl>
</dl>
</dl>
<p> -X <i>xid</i></p>
<dl>
<dt>
</dt><dd> embed xfreerdp into window with <i>xid</i>.</dd></dl>
<p> -z</p>
<dl>
<dt>
</dt><dd> Enable compression.</dd></dl>
<p> &#8211;app</p>
<dl>
<dt>
</dt><dd> initialize a RemoteApp connection. This implies -g workarea.</dd></dl>
<p> &#8211;no-auth</p>
<dl>
<dt>
</dt><dd> Skips authentication. This is useful e.g. for the current FreeRDP server that doesn&#8217;t yet support server-side authentication.</dd></dl>
<p> &#8211;authonly</p>
<dl>
<dt>
</dt><dd> Only authenticates. This is useful to test your credentials (username and password). Returns status code 0 if the client can connect. Requires a username, password and connection host at the command line.</dd></dl>
<p> &#8211;no-bmp-cache</p>
<dl>
<dt>
</dt><dd> Disable bitmap cache.</dd></dl>
<p> &#8211;certificate-name <i>name</i></p>
<dl>
<dt>
</dt><dd> use <i>name</i> for the logon certificate, instead of the server name</dd></dl>
<p> &#8211;composition</p>
<dl>
<dt>
</dt><dd> Enable composition (RDVH only, not to be confused with remote composition).</dd></dl>
<p> &#8211;ext <i>extname</i></p>
<dl>
<dt>
</dt><dd> load extension <i>extname</i></dd></dl>
<p> &#8211;no-fastpath</p>
<dl>
<dt>
</dt><dd> Disables fast-path. Use slow-path packets instead, which have larger headers. It might be good for debugging certain issues when you suspect it might be linked to the parsing of one of the two header types.</dd></dl>
<p> &#8211;from-stdin</p>
<dl>
<dt>
</dt><dd> Prompts for unspecified arguments -u username, -p password, -d domain and connection host. This is useful to hide arguments from ps. Also useful for scripts that will feed these arguments to the client via (what else?) stdin.</dd></dl>
<p> &#8211;disable-full-window-drag</p>
<dl>
<dt>
</dt><dd> Disable full window drag.</dd></dl>
<p> &#8211;gdi <i>backend</i></p>
<dl>
<dt>
</dt><dd> GDI (Graphics Device Interface) rendering backend. <i>backend</i> can be either sw (software) or hw (hardware).</dd></dl>
<p> &#8211;help</p>
<dl>
<dt>
</dt><dd> Print help.</dd></dl>
<p> &#8211;ignore-certificate</p>
<dl>
<dt>
</dt><dd> ignore verification of logon certificate.</dd></dl>
<p> &#8211;kbd-list</p>
<dl>
<dt>
</dt><dd> list all keyboard layout ids used by -k</dd></dl>
<p> &#8211;disable-menu-animations</p>
<dl>
<dt>
</dt><dd> Disable menu animations.</dd></dl>
<p> &#8211;no-motion</p>
<dl>
<dt>
</dt><dd> Don&#8217;t send mouse motion events.</dd></dl>
<p> &#8211;no-nla</p>
<dl>
<dt>
</dt><dd> Disable network level authentication.</dd></dl>
<p> &#8211;nsc</p>
<dl>
<dt>
</dt><dd> Enable NSCodec.</dd></dl>
<p> &#8211;no-osb</p>
<dl>
<dt>
</dt><dd> Disable off screen bitmaps.</dd></dl>
<p> &#8211;plugin <i>pluginname</i></p>
<dl>
<dt>
</dt><dd> Load <i>pluginname</i> </dd>
<p> In Red Hat Enterprise Linux 6, the following plugins are available: </p>
<p> cliprdr</p>
<dl>
<dt>
</dt><dd> Clipboard support</dd></dl>
<p> drdynvc</p>
<dl>
<dt>
</dt><dd> Used for multimedia redirection</dd></dl>
<p> rdpsnd</p>
<dl>
<dt>
</dt><dd> For audio output</dd></dl>
<p> rail</p>
<dl>
<dt>
</dt><dd> Remote Applications Integrated Locally</dd></dl>
<p> rdpdbg</p>
<dl>
<dt>
</dt><dd> Debugging Virtual Channel</dd></dl>
<p> rdpdr</p>
<dl>
<dt>
</dt><dd> File System Support</dd></dl>
<p> As an example, </p>
<p> <code>xfreerdp</code> &#8211;plugin rdpsnd <i>server</i> </p>
<p> will enable audio output using the PulseAudio backend of the rdpsnd plugin. Please Note that Red Hat Enterprise Linux 6 does not include support for the ALSA backend of the rdpsnd plugin.</dl>
<p> &#8211;no-rdp</p>
<dl>
<dt>
</dt><dd> Disable Standard RDP encryption.</dd></dl>
<p> &#8211;rfx</p>
<dl>
<dt>
</dt><dd> Enable RemoteFX.</dd></dl>
<p> &#8211;rfx-mode</p>
<dl>
<dt>
</dt><dd> RemoteFX operational flags. <i>flags</i> can be either v[ideo], i[mage]), default is video.</dd></dl>
<p> &#8211;ntlm <i>version</i></p>
<dl>
<dt>
</dt><dd> Force NTLM protocol version to be <i>version</i>, which can be one of 1 or 2.</dd></dl>
<p> &#8211;sec <i>proto</i></p>
<dl>
<dt>
</dt><dd> Force protocol security. <i>proto</i> can be one of rdp, tls or nla.</dd></dl>
<p> &#8211;secure-checksum</p>
<dl>
<dt>
</dt><dd> Use salted checksums with Standard RDP encryption.</dd></dl>
<p> &#8211;disable-theming</p>
<dl>
<dt>
</dt><dd> Disable theming.</dd></dl>
<p> &#8211;no-tls</p>
<dl>
<dt>
</dt><dd> Disable TLS encryption.</dd></dl>
<p> &#8211;version</p>
<dl>
<dt>
</dt><dd> Print version information.</dd></dl>
<p> &#8211;disable-wallpaper</p>
<dl>
<dt>
</dt><dd> Disable wallpaper.</dd></dl>
<h2>LINKS</h2>
<p> m[blue]<code><a rel="nofollow" href="http://www.freerdp.com/">http://www.freerdp.com/</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> The FreeRDP Team</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> Taken from m[blue]<code>MS-RDPBCGR Section 2.2.1.11.1.1.1 &#8211; Extended Info Packet</code>m[]</dd>
<dt> 2.</dt>
<dd> MS-RDPBCGR Section 2.2.1.11.1.1.1 &#8211; Extended Info Packet</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://msdn.microsoft.com/en-us/library/cc240476%28v=prot.10%29.aspx">http://msdn.microsoft.com/en-us/library/cc240476%28v=prot.10%29.aspx</a></dd></dl>
</dl>
