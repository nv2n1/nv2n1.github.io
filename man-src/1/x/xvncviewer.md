---
title: "xvncviewer(1)"
name: "xvncviewer"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvncviewer/"
description: "vncviewer – VNC viewer for X"
---

<h2 class="name">NAME</h2>
<p> vncviewer &#8211; VNC viewer for X </p>
<h2>SYNOPSIS</h2>
<p> <code>vncviewer</code> [<i>options</i>] [<i>host</i>][:<i>display#</i>]<br />
 <code>vncviewer</code> [<i>options</i>] <code>-listen</code> [<i>port</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>vncviewer</code> is a viewer (client) for Virtual Network Computing. This manual page documents version 4 for the X window system. </p>
<p> If you run the viewer with no arguments it will prompt you for a VNC server to connect to. Alternatively, specify the VNC server as an argument, e.g.: </p>
<dl>
<dt>
<dd> vncviewer snoopy:2</dl>
<p> where &#8216;snoopy&#8217; is the name of the machine, and &#8216;2&#8217; is the display number of the VNC server on that machine. Either the machine name or display number can be omitted. So for example &quot;:1&quot; means display number 1 on the same machine, and &quot;snoopy&quot; means &quot;snoopy:0&quot; i.e. display 0 on machine &quot;snoopy&quot;. </p>
<p> If the VNC server is successfully contacted, you will be prompted for a password to authenticate you. If the password is correct, a window will appear showing the desktop of the VNC server. </p>
<h2>AUTOMATIC PROTOCOL SELECTION</h2>
<p> The viewer tests the speed of the connection to the server and chooses the encoding and pixel format (colour level) appropriately. This makes it much easier to use than previous versions where the user had to specify arcane command line arguments. </p>
<p> The viewer normally starts out assuming the link is slow, using a low colour level and using the encoding with the best compression. If it turns out that the link is fast enough it switches to full-colour mode and will use an encoding which compresses less but is faster to generate, thus improving the interactive feel. Automatic selection can be turned off by setting the <code>AutoSelect</code> parameter to false, or from the options dialog. </p>
<h2>POPUP MENU</h2>
<p> The viewer has a popup menu containing entries which perform various actions. It is usually brought up by pressing F8, but this can be configured with the MenuKey parameter. Actions which the popup menu can perform include:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> switching in and out of full-screen mode</p>
<dt>*</p>
<dd> quitting the viewer</p>
<dt>*</p>
<dd> generating key events, e.g. sending ctrl-alt-del</p>
<dt>*</p>
<dd> accessing the options dialog and various other dialogs</dl>
</dl>
<p> By default, key presses in the popup menu get sent to the VNC server and dismiss the popup. So to get an F8 through to the VNC server simply press it twice. </p>
<h2>FULL SCREEN MODE</h2>
<p> A full-screen mode is supported. This is particularly useful when connecting to a remote screen which is the same size as your local one. If the remote screen is bigger, you can scroll by bumping the mouse against the edge of the screen. </p>
<p> Unfortunately this mode doesn&#8217;t work completely with all window managers, since it breaks the X window management conventions. </p>
<h2>OPTIONS (PARAMETERS)</h2>
<p> You can get a list of parameters by giving <code>-h</code> as a command-line option to vncviewer. Parameters can be turned on with &#8211;<i>param</i> or off with &#8211;<i>param</i>=0. Parameters which take a value can be specified as &#8211;<i>param</i> <i>value</i>. Other valid forms are <i>param</i><code>=</code><i>value</i> &#8211;<i>param</i>=<i>value</i> &#8212;<i>param</i>=<i>value</i>. Parameter names are case-insensitive. </p>
<p> Many of the parameters can also be set graphically via the options dialog box. This can be accessed from the popup menu or from the &quot;Connection details&quot; dialog box. </p>
<dl>
<dt><code>-display </code><i>Xdisplay</i></p>
<dd> Specifies the X display on which the VNC viewer window should appear. </p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> Standard X position and sizing specification. </p>
<dt><code>-listen </code><i>[port]</i></p>
<dd> Causes vncviewer to listen on the given port (default 5500) for reverse connections from a VNC server. WinVNC supports reverse connections initiated using the &#8216;Add New Client&#8217; menu option or the &#8216;-connect&#8217; command-line option. Xvnc supports reverse connections with a helper program called <code>vncconfig.</code> </p>
<dt><code>-XDialog</code></p>
<dd> Popup an X dialog when asking for server, username and password. Default is to not popup when vncviewer is start from command line. </p>
<dt><code>-passwd </code><i>password-file</i></p>
<dd> If you are on a filesystem which gives you access to the password file used by the server, you can specify it here to avoid typing it in. It will usually be &quot;~/.vnc/passwd&quot;. </p>
<dt><code>-Shared</code></p>
<dd> When you make a connection to a VNC server, all other existing connections are normally closed. This option requests that they be left open, allowing you to share the desktop with someone already using it. </p>
<dt><code>-ViewOnly</code></p>
<dd> Specifies that no keyboard or mouse events should be sent to the server. Useful if you want to view a desktop without interfering; often needs to be combined with <code>-Shared.</code> </p>
<dt><code>-FullScreen</code></p>
<dd> Start in full-screen mode. </p>
<dt><code>-AutoSelect</code></p>
<dd> Use automatic selection of encoding and pixel format (default is on). Normally the viewer tests the speed of the connection to the server and chooses the encoding and pixel format appropriately. Turn it off with <code>-AutoSelect=0</code>. </p>
<dt><code>-FullColour, -FullColor</code></p>
<dd> Tells the VNC server to send full-colour pixels in the best format for this display. By default a low colour mode is used until AutoSelect decides the link is fast enough. However if the server&#8217;s native pixel format is colourmapped (as opposed to truecolour) then the server&#8217;s format is used by default. </p>
<dt><code>-LowColourLevel </code><i>level</i></p>
<dd> Selects the reduced colour level to use on slow links. <i>level</i> can range from 0 to 2, 0 meaning 8 colours, 1 meaning 64 colours (the default), 2 meaning 256 colours. </p>
<dt><code>-PreferredEncoding </code><i>encoding</i></p>
<dd> This option specifies the preferred encoding to use from one of &quot;ZRLE&quot;, &quot;hextile&quot; or &quot;raw&quot;. </p>
<dt><code>-UseLocalCursor</code></p>
<dd> Render the mouse cursor locally if the server supports it (default is on). This can make the interactive performance feel much better over slow links. </p>
<dt><code>-WMDecorationWidth </code><i>w</i>, -WMDecorationHeight <i>h</i></p>
<dd> The total width and height taken up by window manager decorations. This is used to calculate the maximum size of the VNC viewer window. Default is width 6, height 24. </p>
<dt><code>-log </code><i>logname</i>:<i>dest</i>:<i>level</i></p>
<dd> Configures the debug log settings. <i>dest</i> can currently be <code>stderr</code> or <code>stdout</code>, and <i>level</i> is between 0 and 100, 100 meaning most verbose output. <i>logname</i> is usually <code>*</code> meaning all, but you can target a specific source file if you know the name of its &quot;LogWriter&quot;. Default is <code>*:stderr:30</code>. </p>
<dt><code>-MenuKey </code><i>keysym-name</i></p>
<dd> This option specifies the key which brings up the popup menu. The key is specified as an X11 keysym name (these can be obtained by removing the XK_ prefix from the entries in &quot;/usr/include/X11/keysymdef.h&quot;). Default is F8. </p>
<dt><code>-via</code> <i>gateway</i></p>
<dd> Automatically create encrypted TCP tunnel to the <i>gateway</i> machine before connection, connect to the <i>host</i> through that tunnel (TightVNC-specific). By default, this option invokes SSH local port forwarding, assuming that SSH client binary can be accessed as /usr/bin/ssh. Note that when using the <code>-via</code> option, the host machine name should be specified as known to the gateway machine, e.g. &quot;localhost&quot; denotes the <i>gateway</i>, not the machine where vncviewer was launched. The environment variable <i>VNC_VIA_CMD</i> can override the default tunnel command of <code>/usr/bin/ssh -f -L&nbsp;&quot;$L&quot;:&quot;$H&quot;:&quot;$R&quot;&nbsp;&quot;$G&quot;&nbsp;sleep 20</code>. The tunnel command is executed with the environment variables <i>L</i>, <i>H</i>, <i>R</i>, and <i>G</i> taken the values of the local port number, the remote host, the port number on the remote host, and the gateway machine respectively. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1), <code><a href="/docs/linux/man/1-vncpasswd/">vncpasswd</a></code>(1), <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1), <code><a href="/docs/linux/man/1-vncserver/">vncserver</a></code>(1)<br />
 <a rel="nofollow" href="http://www.realvnc.com">http://www.realvnc.com</a> </p>
<h2>AUTHOR</h2>
<p> Tristan Richardson, RealVNC Ltd. </p>
<p> VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&amp;T Laboratories Cambridge. It is now being maintained by RealVNC Ltd. See <a rel="nofollow" href="http://www.realvnc.com">http://www.realvnc.com</a> for details. </p>
<h2>Index</h2>
