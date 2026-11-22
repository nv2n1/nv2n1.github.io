---

title: "vncserver(1)"
name: "vncserver"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vncserver/"
description: "vncserver – start or stop a VNC server"
---

<p> vncserver &#8211; start or stop a VNC server</p>
<h2>SYNOPSIS</h2>
<p> <code>vncserver</code> [:<i>display#</i>] [<code>-name</code> <i>desktop-name</i>] [<code>-geometry</code> <i>width</i>x<i>height</i>] [<code>-depth</code> <i>depth</i>] [<code>-pixelformat</code> <i>format</i>] [<code>-fp</code> <i>font-path</i>] [<code>-fg</code>] [<code>-autokill</code>] [<code>-noxstartup</code>] [<code>-xstartup</code> <i>script</i>] [<i>Xvnc-options&#8230;</i>]<br/>
 <code>vncserver -kill :</code><i>display#</i><br/>
 <code>vncserver -list</code></p>
<h2>DESCRIPTION</h2>
<p> <code>vncserver</code> is used to start a VNC (Virtual Network Computing) desktop. <code>vncserver</code> is a Perl script which simplifies the process of starting an Xvnc server. It runs Xvnc with appropriate options and starts a window manager on the VNC desktop. </p>
<p> <code>vncserver</code> can be run with no options at all. In this case it will choose the first available display number (usually :1), start Xvnc with that display number, and start the default window manager in the Xvnc session. You can also specify the display number, in which case vncserver will attempt to start Xvnc with that display number and exit if the display number is not available. For example: </p>
<dl>
<dt>
</dt><dd> vncserver :13</dd></dl>
<p> Editing the file $HOME/.vnc/xstartup allows you to change the applications run at startup (but note that this will not affect an existing VNC session.) </p>
<h2>OPTIONS</h2>
<p> You can get a list of options by passing <code>-h</code> as an option to vncserver. In addition to the options listed below, any unrecognised options will be passed to Xvnc &#8211; see the Xvnc man page, or &quot;Xvnc -help&quot;, for details. </p>
<dl>
<dt><code>-name </code><i>desktop-name</i></dt>
<dd> Each VNC desktop has a name which may be displayed by the viewer. The desktop name defaults to &quot;<i>host</i>:<i>display#</i> (<i>username</i>)&quot;, but you can change it with this option. The desktop name option is passed to the xstartup script via the $VNCDESKTOP environment variable, which allows you to run a different set of applications depending on the name of the desktop.</dd>
<dt><code>-geometry </code><i>width</i>x<i>height</i></dt>
<dd> Specify the size of the VNC desktop to be created. Default is 1024&#215;768.</dd>
<dt><code>-depth </code><i>depth</i></dt>
<dd> Specify the pixel depth (in bits) of the VNC desktop to be created. Default is 24. Other possible values are 8, 15 and 16 &#8211; anything else is likely to cause strange behaviour by applications.</dd>
<dt><code>-pixelformat </code><i>format</i></dt>
<dd> Specify pixel format for Xvnc to use (BGRnnn or RGBnnn). The default for depth 8 is BGR233 (meaning the most significant two bits represent blue, the next three green, and the least significant three represent red), the default for depth 16 is RGB565, and the default for depth 24 is RGB888.</dd>
<dt><code>-cc 3</code></dt>
<dd> As an alternative to the default TrueColor visual, this allows you to run an Xvnc server with a PseudoColor visual (i.e. one which uses a color map or palette), which can be useful for running some old X applications which only work on such a display. Values other than 3 (PseudoColor) and 4 (TrueColor) for the -cc option may result in strange behaviour, and PseudoColor desktops must have an 8-bit depth.</dd>
<dt><code>-kill :</code><i>display#</i></dt>
<dd> This kills a VNC desktop previously started with vncserver. It does this by killing the Xvnc process, whose process ID is stored in the file &quot;$HOME/.vnc/<i>host</i>:<i>display#</i>.pid&quot;. The <code>-kill</code> option ignores anything preceding the first colon (&quot;:&quot;) in the display argument. Thus, you can invoke &quot;vncserver -kill $DISPLAY&quot;, for example at the end of your xstartup file after a particular application exits.</dd>
<dt><code>-fp </code><i>font-path</i></dt>
<dd> If the vncserver script detects that the X Font Server (XFS) is running, it will attempt to start Xvnc and configure Xvnc to use XFS for font handling. Otherwise, if XFS is not running, the vncserver script will attempt to start Xvnc and allow Xvnc to use its own preferred method of font handling (which may be a hard-coded font path or, on more recent systems, a font catalog.) In any case, if Xvnc fails to start, the vncserver script will then attempt to determine an appropriate X font path for this system and start Xvnc using that font path. </dd>
<p> The <code>-fp</code> argument allows you to override the above fallback logic and specify a font path for Xvnc to use.</p>
<dt><code>-fg</code></dt>
<dd> Runs Xvnc as a foreground process. This has two effects: (1) The VNC server can be aborted with CTRL-C, and (2) the VNC server will exit as soon as the user logs out of the window manager in the VNC session. This may be necessary when launching TigerVNC from within certain grid computing environments.</dd>
<dt><code>-autokill</code></dt>
<dd> Automatically kill Xvnc whenever the xstartup script exits. In most cases, this has the effect of terminating Xvnc when the user logs out of the window manager.</dd>
<dt><code>-noxstartup</code></dt>
<dd> Do not run the %HOME/.vnc/xstartup script after launching Xvnc. This option allows you to manually start a window manager in your TigerVNC session.</dd>
<dt><code>-xstartup </code><i>script</i></dt>
<dd> Run a custom startup script, instead of %HOME/.vnc/xstartup, after launching Xvnc. This is useful to run full-screen applications.</dd>
<dt><code>-list</code></dt>
<dd> Lists all VNC desktops started by vncserver. </dd>
</dl>
<h2>FILES</h2>
<p> Several VNC-related files are found in the directory $HOME/.vnc:</p>
<dl>
<dt>$HOME/.vnc/xstartup</dt>
<dd> A shell script specifying X applications to be run when a VNC desktop is started. If this file does not exist, then vncserver will create a default xstartup script which attempts to launch your chosen window manager.</dd>
<dt>/etc/tigervnc/vncserver-config-defaults</dt>
<dd> The optional system-wide equivalent of $HOME/.vnc/config. If this file exists and defines options to be passed to Xvnc, they will be used as defaults for users. The user&#8217;s $HOME/.vnc/config overrides settings configured in this file. The overall configuration file load order is: this file, $HOME/.vnc/config, and then /etc/tigervnc/vncserver-config-mandatory. None are required to exist.</dd>
<dt>/etc/tigervnc/vncserver-config-mandatory</dt>
<dd> The optional system-wide equivalent of $HOME/.vnc/config. If this file exists and defines options to be passed to Xvnc, they will override any of the same options defined in a user&#8217;s $HOME/.vnc/config. This file offers a mechanism to establish some basic form of system-wide policy. WARNING! There is nothing stopping users from constructing their own vncserver-like script that calls Xvnc directly to bypass any options defined in /etc/tigervnc/vncserver-config-mandatory. Likewise, any CLI arguments passed to vncserver will override ANY config file setting of the same name. The overall configuration file load order is: /etc/tigervnc/vncserver-config-defaults, $HOME/.vnc/config, and then this file. None are required to exist.</dd>
<dt>$HOME/.vnc/config</dt>
<dd> An optional server config file wherein options to be passed to Xvnc are listed to avoid hard-coding them to the physical invocation. List options in this file one per line. For those requiring an argument, simply separate the option from the argument with an equal sign, for example: &quot;geometry=2000&#215;1200&quot; or &quot;securitytypes=vncauth,tlsvnc&quot;. Options without an argument are simply listed as a single word, for example: &quot;localhost&quot; or &quot;alwaysshared&quot;.</dd>
<dt>$HOME/.vnc/passwd</dt>
<dd> The VNC password file.</dd>
<dt>$HOME/.vnc/<i>host</i>:<i>display#</i>.log</dt>
<dd> The log file for Xvnc and applications started in xstartup.</dd>
<dt>$HOME/.vnc/<i>host</i>:<i>display#</i>.pid</dt>
<dd> Identifies the Xvnc process ID, used by the <code>-kill</code> option. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vncviewer/">vncviewer</a></code>(1), <code><a href="/docs/linux/man/1-vncpasswd/">vncpasswd</a></code>(1), <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1), <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1)<br/>
 <a rel="nofollow" href="http://www.tigervnc.org">http://www.tigervnc.org</a> </p>
<h2>AUTHOR</h2>
<p> Tristan Richardson, RealVNC Ltd., D. R. Commander and others. </p>
<p> VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&amp;T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite. </p>
