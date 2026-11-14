---
title: "xorg(1)"
name: "xorg"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xorg/"
description: "Xorg – X11R7 X server"
---

<p>Xorg &#8211; X11R7 X server </p>
<h2>Synopsis</h2>
<p><code>Xorg</code> [<code>:</code><i>display</i>] [<i>option</i> <i>&#8230;</i>]</p>
<h2>Description</h2>
<p><code>Xorg</code> is a full featured X server that was originally designed for UNIX and UNIX-like operating systems running on Intel x86 hardware. It now runs on a wider range of hardware and OS platforms. </p>
<p> This work was derived by the X.Org Foundation from the XFree86 Project&#8217;s <i>XFree86 4.4rc2</i> release. The XFree86 release was originally derived from <i>X386 1.2</i> by Thomas Roell which was contributed to X11R5 by Snitily Graphics Consulting Service.</p>
<h2>Platforms</h2>
<p><code>Xorg</code> operates under a wide range of operating systems and hardware platforms. The Intel x86 (IA32) architecture is the most widely supported hardware platform. Other hardware platforms include Compaq Alpha, Intel IA64, AMD64, SPARC and PowerPC. The most widely supported operating systems are the free/OpenSource UNIX-like systems such as Linux, FreeBSD, NetBSD, OpenBSD, and Solaris. Commercial UNIX operating systems such as UnixWare are also supported. Other supported operating systems include GNU Hurd. Mac OS X is supported with the <a href="/docs/linux/man/1-xquartz/">Xquartz</a>(1) X server. Win32/Cygwin is supported with the <a href="/docs/linux/man/1-xwin/">XWin</a>(1) X server. </p>
<h2>Network Connections</h2>
<p><code>Xorg</code> supports connections made using the following reliable byte-streams:</p>
<dl>
<dt><i>Local</i></p>
<dd>On most platforms, the &quot;Local&quot; connection type is a UNIX-domain socket. On some System V platforms, the &quot;local&quot; connection types also include STREAMS pipes, named pipes, and some other mechanisms. See the &quot;LOCAL CONNECTIONS&quot; section of <a href="/docs/linux/man/7-x/">X</a>(7) for details.</p>
<dt><i>TCP/IP</i></p>
<dd><code>Xorg</code> listens on port 6000+<i>n</i>, where <i>n</i> is the display number. This connection type is usually disabled by default, but may be enabled with the <code>-listen</code> option (see the <a href="/docs/linux/man/1-xserver/">Xserver</a>(1) man page for details).</dl>
<h2>Options</h2>
<p><code>Xorg</code> supports several mechanisms for supplying/obtaining configuration and run-time parameters: command line options, environment variables, the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) configuration files, auto-detection, and fallback defaults. When the same information is supplied in more than one way, the highest precedence mechanism is used. The list of mechanisms is ordered from highest precedence to lowest. Note that not all parameters can be supplied via all methods. The available command line options and environment variables (and some defaults) are described here and in the <a href="/docs/linux/man/1-xserver/">Xserver</a>(1) manual page. Most configuration file parameters, with their defaults, are described in the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) manual page. Driver and module specific configuration parameters are described in the relevant driver or module manual page. </p>
<p> In addition to the normal server options described in the <a href="/docs/linux/man/1-xserver/">Xserver</a>(1) manual page, <code>Xorg</code> accepts the following command line switches:</p>
<dl>
<dt><code>vt</code><i>XX</i></p>
<dd><i>XX</i> specifies the Virtual Terminal device number which <code>Xorg</code> will use. Without this option, <code>Xorg</code> will pick the first available Virtual Terminal that it can locate. This option applies only to platforms that have virtual terminal support, such as Linux, BSD, OpenSolaris, SVR3, and SVR4.</p>
<dt><code>-allowMouseOpenFail</code></p>
<dd>Allow the server to start up even if the mouse device can&#8217;t be opened or initialised. This is equivalent to the <code>AllowMouseOpenFail</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option.</p>
<dt><code>-allowNonLocalXvidtune</code></p>
<dd>Make the VidMode extension available to remote clients. This allows the xvidtune client to connect from another host. This is equivalent to the <code>AllowNonLocalXvidtune</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option. By default non-local connections are not allowed.</p>
<dt><code>-bgamma</code><i> value</i></p>
<dd>Set the blue gamma correction. <i>value</i> must be between 0.1 and 10. The default is 1.0. Not all drivers support this. See also the <code>-gamma</code>, <code>-rgamma</code>, and <code>-ggamma</code> options.</p>
<dt><code>-bpp</code><i> n</i></p>
<dd>No longer supported. Use <code>-depth</code> to set the color depth, and use <code>-fbbpp</code> if you really need to force a non-default framebuffer (hardware) pixel format.</p>
<dt><code>-config</code><i> file</i></p>
<dd>Read the server configuration from <i>file</i>. This option will work for any file when the server is run as root (i.e, with real-uid 0), or for files relative to a directory in the config search path for all other users.</p>
<dt><code>-configdir</code><i> directory</i></p>
<dd>Read the server configuration files from <i>directory</i>. This option will work for any directory when the server is run as root (i.e, with real-uid 0), or for directories relative to a directory in the config directory search path for all other users.</p>
<dt><code>-configure</code></p>
<dd>When this option is specified, the <code>Xorg</code> server loads all video driver modules, probes for available hardware, and writes out an initial <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file based on what was detected. This option currently has some problems on some platforms, but in most cases it is a good way to bootstrap the configuration process. This option is only available when the server is run as root (i.e, with real-uid 0).</p>
<dt><code>-crt /dev/tty</code><i>XX</i></p>
<dd>SCO only. This is the same as the <code>vt</code> option, and is provided for compatibility with the native SCO X server.</p>
<dt><code>-depth</code><i> n</i></p>
<dd>Sets the default color depth. Legal values are 1, 4, 8, 15, 16, and 24. Not all drivers support all values.</p>
<dt><code>-disableVidMode</code></p>
<dd>Disable the parts of the VidMode extension (used by the xvidtune client) that can be used to change the video modes. This is equivalent to the <code>DisableVidModeExtension</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option.</p>
<dt><code>-fbbpp </code><i>n</i></p>
<dd>Sets the number of framebuffer bits per pixel. You should only set this if you&#8217;re sure it&#8217;s necessary; normally the server can deduce the correct value from <code>-depth</code> above. Useful if you want to run a depth 24 configuration with a 24 bpp framebuffer rather than the (possibly default) 32 bpp framebuffer (or vice versa). Legal values are 1, 8, 16, 24, 32. Not all drivers support all values.</p>
<dt><code>-gamma</code><i> value</i></p>
<dd>Set the gamma correction. <i>value</i> must be between 0.1 and 10. The default is 1.0. This value is applied equally to the R, G and B values. Those values can be set independently with the <code>-rgamma</code>, <code>-bgamma</code>, and <code>-ggamma</code> options. Not all drivers support this.</p>
<dt><code>-ggamma</code><i> value</i></p>
<dd>Set the green gamma correction. <i>value</i> must be between 0.1 and 10. The default is 1.0. Not all drivers support this. See also the <code>-gamma</code>, <code>-rgamma</code>, and <code>-bgamma</code> options.</p>
<dt><code>-ignoreABI</code></p>
<dd>The <code>Xorg</code> server checks the ABI revision levels of each module that it loads. It will normally refuse to load modules with ABI revisions that are newer than the server&#8217;s. This is because such modules might use interfaces that the server does not have. When this option is specified, mismatches like this are downgraded from fatal errors to warnings. This option should be used with care.</p>
<dt><code>-isolateDevice </code><i>bus-id</i></p>
<dd>Restrict device resets to the device at <i>bus-id</i>. The <i>bus-id</i> string has the form <i>bustype</i><code>:</code><i>bus</i><code>:</code><i>device</i><code>:</code><i>function</i> (e.g., &#8216;PCI:1:0:0&#8217;). At present, only isolation of PCI devices is supported; i.e., this option is ignored if <i>bustype</i> is anything other than &#8216;PCI&#8217;.</p>
<dt><code>-keeptty</code></p>
<dd>Prevent the server from detaching its initial controlling terminal. If you want to use systemd-logind integration you must specify this option. Not all platforms support (or can use) this option.</p>
<dt><code>-keyboard</code><i> keyboard-name</i></p>
<dd>Use the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file <code>InputDevice</code> section called <i>keyboard-name</i> as the core keyboard. This option is ignored when the <code>Layout</code> section specifies a core keyboard. In the absence of both a Layout section and this option, the first relevant <code>InputDevice</code> section is used for the core keyboard.</p>
<dt><code>-layout</code><i> layout-name</i></p>
<dd>Use the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file <code>Layout</code> section called <i>layout-name</i>. By default the first <code>Layout</code> section is used.</p>
<dt><code>-logfile</code><i> filename</i></p>
<dd>Use the file called <i>filename</i> as the <code>Xorg</code> server log file. The default log file when running as root is <code>/var/log/Xorg.</code><i>n</i><code>.log</code> and for non root it is <code>$XDG_DATA_HOME/xorg/Xorg.</code><i>n</i><code>.log</code> where <i>n</i> is the display number of the <code>Xorg</code> server. The default may be in a different directory on some platforms. This option is only available when the server is run as root (i.e, with real-uid 0).</p>
<dt><code>-logverbose</code> [<i>n</i>]</p>
<dd>Sets the verbosity level for information printed to the <code>Xorg</code> server log file. If the <i>n</i> value isn&#8217;t supplied, each occurrence of this option increments the log file verbosity level. When the <i>n</i> value is supplied, the log file verbosity level is set to that value. The default log file verbosity level is 3.</p>
<dt><code>-modulepath</code><i> searchpath</i></p>
<dd>Set the module search path to <i>searchpath</i>. <i>searchpath</i> is a comma separated list of directories to search for <code>Xorg</code> server modules. This option is only available when the server is run as root (i.e, with real-uid 0).</p>
<dt><code>-noautoBindGPU</code></p>
<dd>Disable automatically setting secondary GPUs up as output sinks and offload sources. This is equivalent to setting the <code>AutoBindGPU</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option. To <code>false.</code></p>
<dt><code>-nosilk</code></p>
<dd>Disable Silken Mouse support.</p>
<dt><code>-novtswitch</code></p>
<dd>Disable the automatic switching on X server reset and shutdown to the VT that was active when the server started, if supported by the OS.</p>
<dt><code>-pointer</code><i> pointer-name</i></p>
<dd>Use the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file <code>InputDevice</code> section called <i>pointer-name</i> as the core pointer. This option is ignored when the <code>Layout</code> section specifies a core pointer. In the absence of both a Layout section and this option, the first relevant <code>InputDevice</code> section is used for the core pointer.</p>
<dt><code>-quiet</code></p>
<dd>Suppress most informational messages at startup. The verbosity level is set to zero.</p>
<dt><code>-rgamma</code><i> value</i></p>
<dd>Set the red gamma correction. <i>value</i> must be between 0.1 and 10. The default is 1.0. Not all drivers support this. See also the <code>-gamma</code>, <code>-bgamma</code>, and <code>-ggamma</code> options.</p>
<dt><code>-sharevts</code></p>
<dd>Share virtual terminals with another X server, if supported by the OS.</p>
<dt><code>-screen</code><i> screen-name</i></p>
<dd>Use the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file <code>Screen</code> section called <i>screen-name</i>. By default the screens referenced by the default <code>Layout</code> section are used, or the first <code>Screen</code> section when there are no <code>Layout</code> sections.</p>
<dt><code>-showconfig</code></p>
<dd>This is the same as the <code>-version</code> option, and is included for compatibility reasons. It may be removed in a future release, so the <code>-version</code> option should be used instead.</p>
<dt><code>-showDefaultModulePath</code></p>
<dd>Print out the default module path the server was compiled with.</p>
<dt><code>-showDefaultLibPath</code></p>
<dd>Print out the path libraries should be installed to.</p>
<dt><code>-showopts</code></p>
<dd>For each driver module installed, print out the list of options and their argument types.</p>
<dt><code>-weight</code><i> nnn</i></p>
<dd>Set RGB weighting at 16 bpp. The default is 565. This applies only to those drivers which support 16 bpp.</p>
<dt><code>-verbose</code> [<i>n</i>]</p>
<dd>Sets the verbosity level for information printed on stderr. If the <i>n</i> value isn&#8217;t supplied, each occurrence of this option increments the verbosity level. When the <i>n</i> value is supplied, the verbosity level is set to that value. The default verbosity level is 0.</p>
<dt><code>-version</code></p>
<dd>Print out the server version, patchlevel, release date, the operating system/platform it was built on, and whether it includes module loader support.</dl>
<h2>Keyboard</h2>
<p>The <code>Xorg</code> server is normally configured to recognize various special combinations of key presses that instruct the server to perform some action, rather than just sending the key press event to a client application. These actions depend on the XKB keymap loaded by a particular keyboard device and may or may not be available on a given configuration. </p>
<p> The following key combinations are commonly part of the default XKEYBOARD keymap.</p>
<dl>
<dt><code>Ctrl+Alt+Backspace</code></p>
<dd>Immediately kills the server &#8212; no questions asked. It can be disabled by setting the <code>DontZap</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option to a TRUE value.</dl>
<dl>
<dd>It should be noted that zapping is triggered by the <code>Terminate_Server</code> action in the keyboard map. This action is not part of the default keymaps but can be enabled with the XKB option <code>&#34;terminate:ctrl_alt_bksp&#34;.</code></dl>
<dl>
<dt><code>Ctrl+Alt+Keypad-Plus</code></p>
<dd>Change video mode to next one specified in the configuration file. This can be disabled with the <code>DontZoom</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option.</p>
<dt><code>Ctrl+Alt+Keypad-Minus</code></p>
<dd>Change video mode to previous one specified in the configuration file. This can be disabled with the <code>DontZoom</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option.</p>
<dt><code>Ctrl+Alt+F1&#8230;F12</code></p>
<dd>For systems with virtual terminal support, these keystroke combinations are used to switch to virtual terminals 1 through 12, respectively. This can be disabled with the <code>DontVTSwitch</code> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) file option.</dl>
<h2>Configuration</h2>
<p><code>Xorg</code> typically uses a configuration file called <code>xorg.conf</code> and configuration files with the suffix <i>.conf</i> in a directory called <code>xorg.conf.d</code> for its initial setup. Refer to the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) manual page for information about the format of this file. </p>
<p> <code>Xorg</code> has a mechanism for automatically generating a built-in configuration at run-time when no <code>xorg.conf</code> file or <code>xorg.conf.d</code> files are present. The current version of this automatic configuration mechanism works in two ways. </p>
<p> The first is via enhancements that have made many components of the <code>xorg.conf</code> file optional. This means that information that can be probed or reasonably deduced doesn&#8217;t need to be specified explicitly, greatly reducing the amount of built-in configuration information that needs to be generated at run-time. </p>
<p> The second is to have &quot;safe&quot; fallbacks for most configuration information. This maximises the likelihood that the <code>Xorg</code> server will start up in some usable configuration even when information about the specific hardware is not available. </p>
<p> The automatic configuration support for Xorg is work in progress. It is currently aimed at the most popular hardware and software platforms supported by Xorg. Enhancements are planned for future releases.</p>
<h2>Files</h2>
<p>The <code>Xorg</code> server config files can be found in a range of locations. These are documented fully in the <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) manual page. The most commonly used locations are shown here.</p>
<dl>
<dt><code>/etc/X11/xorg.conf</code></p>
<dd>Server configuration file.</p>
<dt><code>/etc/X11/xorg.conf-4</code></p>
<dd>Server configuration file.</p>
<dt><code>/etc/xorg.conf</code></p>
<dd>Server configuration file.</p>
<dt><code>/usr/etc/xorg.conf</code></p>
<dd>Server configuration file.</p>
<dt><code>/usr/lib/X11/xorg.conf</code></p>
<dd>Server configuration file.</p>
<dt><code>/etc/X11/xorg.conf.d</code></p>
<dd>Server configuration directory.</p>
<dt><code>/etc/X11/xorg.conf.d-4</code></p>
<dd>Server configuration directory.</p>
<dt><code>/etc/xorg.conf.d</code></p>
<dd>Server configuration directory.</p>
<dt><code>/usr/etc/xorg.conf.d</code></p>
<dd>Server configuration directory.</p>
<dt><code>/usr/lib/X11/xorg.conf.d</code></p>
<dd>Server configuration directory.</p>
<dt><code>/var/log/Xorg.</code><i>n</i><code>.log</code></p>
<dd>Server log file for display <i>n</i>.</p>
<dt><code>/usr/bin/*</code></p>
<dd>Client binaries.</p>
<dt><code>/usr/include/*</code></p>
<dd>Header files.</p>
<dt><code>/usr/lib/*</code></p>
<dd>Libraries.</p>
<dt><code>/usr/share/fonts/X11/*</code></p>
<dd>Fonts.</p>
<dt><code>/usr/share/X11/XErrorDB</code></p>
<dd>Client error message database.</p>
<dt><code>/usr/lib/X11/app-defaults/*</code></p>
<dd>Client resource specifications.</p>
<dt><code>/usr/share/man/man?/*</code></p>
<dd>Manual pages.</p>
<dt><code>/etc/X</code><i>n</i><code>.hosts</code></p>
<dd>Initial access control list for display <i>n</i>.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-xdm/">xdm</a>(1), <a href="/docs/linux/man/1-xinit/">xinit</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xvidtune/">xvidtune</a>(1), xkeyboard-config (7), <a href="/docs/linux/man/4-apm/">apm</a>(4), <a href="/docs/linux/man/4-ati/">ati</a>(4), <a href="/docs/linux/man/4-chips/">chips</a>(4), <a href="/docs/linux/man/4-cirrus/">cirrus</a>(4), <a href="/docs/linux/man/4-cyrix/">cyrix</a>(4), <a href="/docs/linux/man/4-fbdev/">fbdev</a>(4), <a href="/docs/linux/man/4-glide/">glide</a>(4), <a href="/docs/linux/man/4-glint/">glint</a>(4), <a href="/docs/linux/man/4-i128/">i128</a>(4), <a href="/docs/linux/man/4-i740/">i740</a>(4), <a href="/docs/linux/man/4-imstt/">imstt</a>(4), <a href="/docs/linux/man/4-intel/">intel</a>(4), <a href="/docs/linux/man/4-mga/">mga</a>(4), <a href="/docs/linux/man/4-neomagic/">neomagic</a>(4), <a href="/docs/linux/man/4-nsc/">nsc</a>(4), <a href="/docs/linux/man/4-nv/">nv</a>(4), openchrome (4), <a href="/docs/linux/man/4-r128/">r128</a>(4), <a href="/docs/linux/man/4-rendition/">rendition</a>(4), <a href="/docs/linux/man/4-s3virge/">s3virge</a>(4), <a href="/docs/linux/man/4-siliconmotion/">siliconmotion</a>(4), <a href="/docs/linux/man/4-sis/">sis</a>(4), <a href="/docs/linux/man/4-sunbw2/">sunbw2</a>(4), <a href="/docs/linux/man/4-suncg14/">suncg14</a>(4), <a href="/docs/linux/man/4-suncg3/">suncg3</a>(4), <a href="/docs/linux/man/4-suncg6/">suncg6</a>(4), <a href="/docs/linux/man/4-sunffb/">sunffb</a>(4), <a href="/docs/linux/man/4-sunleo/">sunleo</a>(4), <a href="/docs/linux/man/4-suntcx/">suntcx</a>(4), <a href="/docs/linux/man/4-tdfx/">tdfx</a>(4), <a href="/docs/linux/man/4-tga/">tga</a>(4), <a href="/docs/linux/man/4-trident/">trident</a>(4), <a href="/docs/linux/man/4-tseng/">tseng</a>(4), <a href="/docs/linux/man/4-v4l/">v4l</a>(4), <a href="/docs/linux/man/4-vesa/">vesa</a>(4), <a href="/docs/linux/man/4-vmware/">vmware</a>(4),<br />
 Web site <i>&lt;<a rel="nofollow" href="https://www.x.org">https://www.x.org</a>&gt;</i>. </p>
<h2>Authors</h2>
<p>Xorg has many contributors world wide. The names of most of them can be found in the documentation, ChangeLog files in the source tree, and in the actual source code. </p>
<p> Xorg was originally based on XFree86 4.4rc2. That was originally based on <i>X386 1.2</i> by Thomas Roell, which was contributed to the then X Consortium&#8217;s X11R5 distribution by SGCS. </p>
<p> Xorg is released by the X.Org Foundation. </p>
<p> The project that became XFree86 was originally founded in 1992 by David Dawes, Glenn Lai, Jim Tsillas and David Wexelblat. </p>
<p> XFree86 was later integrated in the then X Consortium&#8217;s X11R6 release by a group of dedicated XFree86 developers, including the following: </p>
<dl>
<dd>
<pre>Stuart Anderson <i>anderson [at] metrolink.com</i>
Doug Anson <i>danson [at] lgc.com</i>
Gertjan Akkerman <i>akkerman [at] dutiba.twi.tudelft.nl</i>
Mike Bernson <i>mike [at] mbsun.mlb.org</i>
Robin Cutshaw <i>robin [at] XFree86.org</i>
David Dawes <i>dawes [at] XFree86.org</i>
Marc Evans <i>marc [at] XFree86.org</i>
Pascal Haible <i>haible [at] izfm.uni-stuttgart.de</i>
Matthieu Herrb <i>Matthieu.Herrb [at] laas.fr</i>
Dirk Hohndel <i>hohndel [at] XFree86.org</i>
David Holland <i>davidh [at] use.com</i>
Alan Hourihane <i>alanh [at] fairlite.demon.co.uk</i>
Jeffrey Hsu <i>hsu [at] soda.berkeley.edu</i>
Glenn Lai <i>glenn [at] cs.utexas.edu</i>
Ted Lemon <i>mellon [at] ncd.com</i>
Rich Murphey <i>rich [at] XFree86.org</i>
Hans Nasten <i>nasten [at] everyware.se</i>
Mark Snitily <i>mark [at] sgcs.com</i>
Randy Terbush <i>randyt [at] cse.unl.edu</i>
Jon Tombs <i>tombs [at] XFree86.org</i>
Kees Verstoep <i>versto [at] cs.vu.nl</i>
Paul Vixie <i>paul [at] vix.com</i>
Mark Weaver <i>Mark_Weaver [at] brown.edu</i>
David Wexelblat <i>dwex [at] XFree86.org</i>
Philip Wheatley <i>Philip.Wheatley [at] ColumbiaSC.NCR.COM</i>
Thomas Wolfram <i>wolf [at] prz.tu-berlin.de</i>
Orest Zborowski <i>orestz [at] eskimo.com</i></pre>
</dl>
<p> Xorg source is available from the FTP server <i>&lt;<a href="ftp://ftp.x.org/">ftp://ftp.x.org/</a>&gt;</i>, and from the X.Org server <i>&lt;<a rel="nofollow" href="https://gitlab.freedesktop.org/xorg/">https://gitlab.freedesktop.org/xorg/</a>&gt;</i>. Documentation and other information can be found from the X.Org web site <i>&lt;<a rel="nofollow" href="https://www.x.org/">https://www.x.org/</a>&gt;</i>. </p>
<h2>Legal</h2>
<p><code>Xorg</code> is copyright software, provided under licenses that permit modification and redistribution in source and binary form without fee. <code>Xorg is copyright by numerous authors and</code> contributors from around the world. Licensing information can be found at <i>&lt;<a rel="nofollow" href="https://www.x.org">https://www.x.org</a>&gt;</i>. Refer to the source code for specific copyright notices. </p>
<p> <code>XFree86(TM)</code> is a trademark of The XFree86 Project, Inc. </p>
<p> <code>X11(TM)</code> and <code>X Window System(TM)</code> are trademarks of The Open Group.</p>
