---
title: "xscreensaver(1)"
name: "xscreensaver"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xscreensaver/"
description: "xscreensaver – extensible screen saver and screen locking framework"
---

<h2 class="name">NAME</h2>
<p> xscreensaver &#8211; extensible screen saver and screen locking framework </p>
<h2>SYNOPSIS</h2>
<p> <code>xscreensaver</code> [-display <i>host:display.screen</i>] [-verbose] [-no-splash] [-no-capture-stderr] [-log <i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xscreensaver</i> program waits until the keyboard and mouse have been idle for a period, and then runs a graphics demo chosen at random. It turns off as soon as there is any mouse or keyboard activity. </p>
<p> This program can lock your terminal in order to prevent others from using it, though its default mode of operation is merely to display pretty pictures on your screen when it is not in use. </p>
<p> It also provides configuration and control of your monitor&#8217;s power-saving features.</p>
<h2>GETTING STARTED</h2>
<p> For the impatient, try this: </p>
<pre>
xscreensaver &amp;
xscreensaver-demo
</pre>
<p> The <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) program pops up a dialog box that lets you configure the screen saver, and experiment with the various display modes. </p>
<p> <code>Note that xscreensaver has a client-server model:</code> the <i>xscreensaver</i> program is a daemon that runs in the background; it is controlled by the foreground <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) and <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1) programs.</p>
<h2>CONFIGURATION</h2>
<p> The easiest way to configure <i>xscreensaver</i> is to simply run the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) program, and change the settings through the GUI. The rest of this manual page describes lower level ways of changing settings. </p>
<p> I&#8217;ll repeat that because it&#8217;s important: </p>
<dl>
<dt>
<dd> The easy way to configure xscreensaver is to run the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) program. You shouldn&#8217;t need to know any of the stuff described in <i>this</i> manual unless you are trying to do something tricky, like customize xscreensaver for site-wide use or something.</dl>
<p> Options to <i>xscreensaver</i> are stored in one of two places: in a <i>.xscreensaver</i> file in your home directory; or in the X resource database. If the <i>.xscreensaver</i> file exists, it overrides any settings in the resource database. </p>
<p> The syntax of the <i>.xscreensaver</i> file is similar to that of the <i>.Xdefaults</i> file; for example, to set the <i>timeout</i> parameter in the <i>.xscreensaver</i> file, you would write the following: </p>
<pre>
timeout: 5
</pre>
<p> whereas, in the <i>.Xdefaults</i> file, you would write </p>
<pre>
xscreensaver.timeout: 5
</pre>
<p> If you change a setting in the <i>.xscreensaver</i> file while xscreensaver is already running, it will notice this, and reload the file. (The file will be reloaded the next time the screen saver needs to take some action, such as blanking or unblanking the screen, or picking a new graphics mode.) </p>
<p> If you change a setting in your X resource database, or if you want xscreensaver to notice your changes immediately instead of the next time it wakes up, then you will need to reload your <i>.Xdefaults</i> file, and then tell the running xscreensaver process to restart itself, like so: </p>
<pre>
xrdb &lt; ~/.Xdefaults
xscreensaver-command -restart
</pre>
<p> If you want to set the system-wide defaults, then make your edits to the xscreensaver app-defaults file, which should have been installed when xscreensaver itself was installed. The app-defaults file will usually be named /usr/lib/X11/app-defaults/XScreenSaver, but different systems might keep it in a different place (for example, /usr/openwin/lib/app-defaults/XScreenSaver on Solaris). </p>
<p> When settings are changed in the Preferences dialog box (see above) the current settings will be written to the <i>.xscreensaver</i> file. (The <i>.Xdefaults</i> file and the app-defaults file will never be written by xscreensaver itself.)</p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> <i>xscreensaver</i> also accepts a few command-line options, mostly for use when debugging: for normal operation, you should configure things via the <i>~/.xscreensaver</i> file.</p>
<dl>
<dt><code>-display </code><i>host:display.screen</i></p>
<dd> The X display to use. For displays with multiple screens, XScreenSaver will manage all screens on the display simultaniously.</p>
<dt><code>-verbose</code></p>
<dd> Same as setting the <i>verbose</i> resource to <i>true</i>: print diagnostics on stderr and on the xscreensaver window.</p>
<dt><code>-no-capture-stderr</code></p>
<dd> Do not redirect the stdout and stderr streams to the xscreensaver window itself. If xscreensaver is crashing, you might need to do this in order to see the error message.</p>
<dt><code>-log </code><i>filename</i></p>
<dd> This is exactly the same as redirecting stdout and stderr to the given file (for append). This is useful when reporting bugs.</dl>
<h2>HOW IT WORKS</h2>
<p> When it is time to activate the screensaver, a full-screen black window is created on each screen of the display. Each window is created in such a way that, to any subsequently-created programs, it will appear to be a &quot;virtual root&quot; window. Because of this, any program which draws on the root window (and which understands virtual roots) can be used as a screensaver. The various graphics demos are, in fact, just standalone programs that know how to draw on the provided window. </p>
<p> When the user becomes active again, the screensaver windows are unmapped, and the running subprocesses are killed by sending them <code>SIGTERM</code>. This is also how the subprocesses are killed when the screensaver decides that it&#8217;s time to run a different demo: the old one is killed and a new one is launched. </p>
<p> You can control a running screensaver process by using the <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1) program (which see).</p>
<h2>POWER MANAGEMENT</h2>
<p> Modern X servers contain support to power down the monitor after an idle period. If the monitor has powered down, then <i>xscreensaver</i> will notice this (after a few minutes), and will not waste CPU by drawing graphics demos on a black screen. An attempt will also be made to explicitly power the monitor back up as soon as user activity is detected. </p>
<p> The <i>~/.xscreensaver</i> file controls the configuration of your display&#8217;s power management settings: if you have used <code><a href="/docs/linux/man/1-xset/">xset</a></code>(1) to change your power management settings, then xscreensaver will override those changes with the values specified in <i>~/.xscreensaver</i> (or with its built-in defaults, if there is no <i>~/.xscreensaver</i> file yet). </p>
<p> To change your power management settings, run <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) and change the various timeouts through the user interface. Alternatively, you can edit the <i>~/.xscreensaver</i> file directly. </p>
<p> If the power management section is grayed out in the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) window, then that means that your X server does not support the XDPMS extension, and so control over the monitor&#8217;s power state is not available. </p>
<p> If you&#8217;re using a laptop, don&#8217;t be surprised if changing the DPMS settings has no effect: many laptops have monitor power-saving behavior built in at a very low level that is invisible to Unix and X. On such systems, you can typically adjust the power-saving delays only by changing settings in the BIOS in some hardware-specific way. </p>
<p> If DPMS seems not to be working with XFree86, make sure the &quot;DPMS&quot; option is set in your <i>/etc/X11/XF86Config</i> file. See the <code><a href="/docs/linux/man/5-xf86config/">XF86Config</a></code>(5) manual for details.</p>
<h2>USING GNOME OR UNITY</h2>
<p> For the better part of a decade, GNOME shipped xscreensaver as-is, and everything just worked out of the box. In 2005, however, they decided to re-invent the wheel and ship their own replacement for the <i>xscreensaver</i> daemon called &quot;<i>gnome-screensaver</i>&quot;, rather than improving xscreensaver and contributing their changes back. As a result, the &quot;<i>gnome-screensaver</i>&quot; program is insecure, bug-ridden, and missing many features of xscreensaver. You shouldn&#8217;t use it. </p>
<p> To replace gnome-screensaver with xscreensaver:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1: Fully uninstall the gnome-screensaver package.</code></p>
<dd>
<pre>
sudo apt-get remove gnome-screensaver
</pre>
<p> or possibly </p>
<pre>
sudo dpkg -P gnome-screensaver
</pre>
<dt><code>2: Launch xscreensaver at login.</code></p>
<dd> Select &quot;<i>Startup Applications</i>&quot; from the menu (or manually launch &quot;<i>gnome-session-properties</i>&quot;) and add &quot;<i>xscreensaver</i>&quot;. </p>
<p> Do this as your normal user account, not as root. (This should go without saying, because you should never, ever, ever be logged in to the graphical desktop as user &quot;root&quot;.)</p>
<dt><code>3: Make GNOME&#8217;s &quot;Lock Screen&quot; use xscreensaver.</code></p>
<dd>
<pre>
sudo ln -sf /usr/bin/xscreensaver-command \
            /usr/bin/gnome-screensaver-command
</pre>
<p> That doesn&#8217;t work under Unity, though. Apparently it has its own built-in screen locker which is not gnome-screensaver, and cannot be removed, and yet still manages to be bug-addled and insecure. Keep reinventing that wheel, guys! (If you have figured out how to replace Unity&#8217;s locking &quot;feature&quot; with xscreensaver, let me know.)</p>
<dt><code>4: Turn off Unity&#8217;s built-in blanking.</code></p>
<dd> Open &quot;<i>System Settings / Brightness &amp; Lock</i>&quot;;<br />
 Un-check &quot;<i>Start Automatically</i>&quot;;<br />
 Set <i>&quot;Turn screen off when inactive for&quot;</i> to <i>&quot;Never&quot;.</i></dl>
</dl>
<h2>USING KDE</h2>
<p> Like GNOME, KDE also decided to invent their own screen saver framework from scratch instead of simply using xscreensaver. To replace the KDE screen saver with xscreensaver, do the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1: Turn off KDE&#8217;s screen saver.</code></p>
<dd> Open the &quot;<i>Control Center</i>&quot; and select the &quot;<i>Appearance &amp; Themes / Screensaver</i>&quot; page. Un-check &quot;<i>Start Automatically</i>&quot;. </p>
<p> Or possibly: Open &quot;<i>System Settings</i>&quot; and select &quot;<i>Screen Locking</i>&quot;. Un-check &quot;<i>Lock Screen Automatically</i>&quot;.</p>
<dt><code>2: Find your Autostart directory.</code></p>
<dd> Open the &quot;<i>System Administration / Paths</i>&quot; page, and see what your &quot;Autostart path&quot; is set to: it will probably be something like <i>~/.kde/Autostart/</i> or <i>~/.config/autostart/</i> </p>
<p> If that doesn&#8217;t work, then try this: </p>
<p> Open &quot;<i>System Settings / Startup/Shutdown / Autostart</i>&quot;, and then add &quot;<i>/usr/bin/xscreensaver</i>&quot;. </p>
<p> If you are lucky, that will create a <i>xscreensaver.desktop&quot;</i> file for you in <i>~/.config/autostart/</i> or <i>~/.kde/Autostart/</i>.</p>
<dt><code>3: Make xscreensaver be an Autostart program.</code></p>
<dd> If it does not already exist, create a file in your autostart directory called <i>xscreensaver.desktop</i> that contains the following six lines: </p>
<pre>
[Desktop Entry]
Exec=xscreensaver
Name=XScreenSaver
Type=Application
StartupNotify=false
X-KDE-StartupNotify=false
</pre>
<dt><code>4: Make the various &quot;lock session&quot; buttons call xscreensaver.</code></p>
<dd> The file you want to replace next has moved around over the years. It might be called <i>/usr/libexec/kde4/kscreenlocker</i>, or it might be called &quot;<i>kdesktop_lock</i>&quot; or &quot;<i>krunner_lock</i>&quot; or &quot;<i>kscreenlocker_greet</i>&quot;, and it might be in <i>/usr/lib/kde4/libexec/</i> or in <i>/usr/kde/3.5/bin/</i> or even in <i>/usr/bin/</i>, depending on the distro and phase of the moon. Replace the contents of that file with these two lines: </p>
<pre>
#!/bin/sh
xscreensaver-command -lock
</pre>
<p> Make sure the file is executable (chmod a+x).</dl>
</dl>
<p> Now use xscreensaver normally, controlling it via the usual <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) and <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1) mechanisms.</p>
<h2>USING SYSTEMD</h2>
<p> If the above didn&#8217;t do it, and your system has <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), then give this a try:</p>
<dl>
<dt><code>1: Create a service.</code></p>
<dd> Create the file <i>~/.config/systemd/user/xscreensaver.service</i> containing: </p>
<pre><code>
[Unit] Description = XScreenSaver
    [Service] ExecStart = / usr / bin / xscreensaver[Install] WantedBy = default.target
</code></pre>
<dt><code>2. Enable it.</code></p>
<dd>
<pre>
systemctl --user enable xscreensaver
</pre>
<p> Then restart X11.</dl>
<h2>USING UPSTART</h2>
<p> If it&#8217;s still not working, but on your distro, that newfangled <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) nonsense has already fallen out of favor? Then maybe this will work: launch the <i>&quot;Startup Applications&quot;</i> applet, click <i>&quot;Add&quot;</i>, enter these lines, then restart X11: </p>
<pre>
Name: XScreenSaver
Command: xscreensaver
Comment: xscreensaver
</pre>
<h2>USING GDM</h2>
<p> You can run <i>xscreensaver</i> from your <code><a href="/docs/linux/man/1-gdm/">gdm</a></code>(1) session, so that the screensaver will run even when nobody is logged in on the console. To do this, run <code><a href="/docs/linux/man/1-gdmconfig/">gdmconfig</a></code>(1). </p>
<p> On the <i>General</i> page set the <i>Local Greeter</i> to <i>Standard Greeter</i>. </p>
<p> On the <i>Background</i> page, type the command <code>&quot;xscreensaver -nosplash&quot;</code> into the <i>Background Program</i> field. That will cause gdm to run xscreensaver while nobody is logged in, and kill it as soon as someone does log in. (The user will then be responsible for starting xscreensaver on their own, if they want.) </p>
<p> If that doesn&#8217;t work, you can edit the config file directly. Edit <i>/etc/X11/gdm/gdm.conf</i> to include: </p>
<pre>
Greeter=/usr/bin/gdmlogin
BackgroundProgram=xscreensaver -nosplash
RunBackgroundProgramAlways=true
</pre>
<p> In this situation, the <i>xscreensaver</i> process will probably be running as user <i>gdm</i> instead of <i>root</i>. You can configure the settings for this nobody-logged-in state (timeouts, DPMS, etc.) by editing the <i>~gdm/.xscreensaver</i> file. </p>
<p> It is safe to run <i>xscreensaver</i> as root (as <i>xdm</i> or <i>gdm</i> may do). If run as root, <i>xscreensaver</i> changes its effective user and group ids to something safe (like <i>&quot;nobody&quot;</i>) before connecting to the X server or launching user-specified programs. </p>
<p> An unfortunate side effect of this (important) security precaution is that it may conflict with cookie-based authentication. </p>
<p> If you get &quot;connection refused&quot; errors when running <i>xscreensaver</i> from <i>gdm</i>, then this probably means that you have <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1) or some other security mechanism turned on. For information on the X server&#8217;s access control mechanisms, see the man pages for <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-xsecurity/">Xsecurity</a></code>(1), <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1), and <code><a href="/docs/linux/man/1-xhost/">xhost</a></code>(1).</p>
<h2>BUGS</h2>
<p> Bugs? There are no bugs. Ok, well, maybe. If you find one, please let me know. <a rel="nofollow" href="https://www.jwz.org/xscreensaver/bugs.html">https://www.jwz.org/xscreensaver/bugs.html</a> explains how to construct the most useful bug reports. </p>
<dl>
<dt><code>Locking and root logins</code></p>
<dd> In order for it to be safe for xscreensaver to be launched by <i>xdm</i>, certain precautions had to be taken, among them that xscreensaver never runs as <i>root</i>. In particular, if it is launched as root (as <i>xdm</i> is likely to do), xscreensaver will disavow its privileges, and switch itself to a safe user id (such as <i>nobody</i>). </p>
<p> An implication of this is that if you log in as <i>root</i> on the console, xscreensaver will refuse to lock the screen (because it can&#8217;t tell the difference between <i>root</i> being logged in on the console, and a normal user being logged in on the console but xscreensaver having been launched by the <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1) <i>Xsetup</i> file). </p>
<p> The solution to this is simple: you shouldn&#8217;t be logging in on the console as <i>root</i> in the first place! (What, are you crazy or something?) </p>
<p> Proper Unix hygiene dictates that you should log in as yourself, and <code><a href="/docs/linux/man/1-su/">su</a></code>(1) to <i>root</i> as necessary. People who spend their day logged in as <i>root</i> are just begging for disaster.</p>
<dt><code>XAUTH and XDM</code></p>
<dd> For xscreensaver to work when launched by <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1) or <code><a href="/docs/linux/man/1-gdm/">gdm</a></code>(1), programs running on the local machine as user <i>&quot;nobody&quot;</i> must be able to connect to the X server. This means that if you want to run xscreensaver on the console while nobody is logged in, you may need to disable cookie-based access control (and allow all users who can log in to the local machine to connect to the display). </p>
<p> You should be sure that this is an acceptable thing to do in your environment before doing it. See the &quot;<i>Using GDM</i>&quot; section, above, for more details.</p>
<dt><code>Passwords</code></p>
<dd> If you get an error message at startup like &quot;couldn&#8217;t get password of <i>user</i>&quot; then this probably means that you&#8217;re on a system in which the <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) library routine can only be effectively used by root. If this is the case, then <i>xscreensaver</i> must be installed as setuid to root in order for locking to work. Care has been taken to make this a safe thing to do. </p>
<p> It also may mean that your system uses shadow passwords instead of the standard <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) interface; in that case, you may need to change some options with <i>configure</i> and recompile. </p>
<p> If you change your password after xscreensaver has been launched, it will continue using your old password to unlock the screen until xscreensaver is restarted. On some systems, it may accept <i>both</i> your old and new passwords. So, after you change your password, you&#8217;ll have to do </p>
<pre>
xscreensaver-command -restart
</pre>
<p> to make <i>xscreensaver</i> notice.</p>
<dt><code>PAM Passwords</code></p>
<dd> If your system uses PAM (Pluggable Authentication Modules), then in order for xscreensaver to use PAM properly, PAM must be told about xscreensaver. The xscreensaver installation process should update the PAM data (on Linux, by creating the file <i>/etc/pam.d/xscreensaver</i> for you, and on Solaris, by telling you what lines to add to the <i>/etc/pam.conf</i> file). </p>
<p> If the PAM configuration files do not know about xscreensaver, then you <i>might</i> be in a situation where xscreensaver will refuse to ever unlock the screen. </p>
<p> This is a design flaw in PAM (there is no way for a client to tell the difference between PAM responding &quot;I have never heard of your module&quot;, and responding, &quot;you typed the wrong password&quot;). As far as I can tell, there is no way for xscreensaver to automatically work around this, or detect the problem in advance, so if you have PAM, make sure it is configured correctly!</p>
<dt><code>Machine Load</code></p>
<dd> Although this program &quot;nices&quot; the subprocesses that it starts, graphics-intensive subprograms can still overload the machine by causing the X server process itself (which is not &quot;niced&quot;) to consume many cycles. Care has been taken in all the modules shipped with xscreensaver to sleep periodically, and not run full tilt, so as not to cause appreciable load. </p>
<p> However, if you are running the OpenGL-based screen savers on a machine that does not have a video card with 3D acceleration, they <i>will</i> make your machine slow, despite <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1). </p>
<p> Your options are: don&#8217;t use the OpenGL display modes; or, collect the spare change hidden under the cushions of your couch, and use it to buy a video card manufactured after 1998. (It doesn&#8217;t even need to be <i>fast</i> 3D hardware: the problem will be fixed if there is any 3D hardware <i>at all.</i>)</p>
<dt><code>Magic Backdoor Keystrokes</code></p>
<dd> The XFree86 X server and the Linux kernel both trap certain magic keystrokes before X11 client programs ever see them. If you care about keeping your screen locked, this is a big problem.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Ctrl+Alt+Backspace</code></p>
<dd> This keystroke kills the X server, and on some systems, leaves you at a text console. If the user launched X11 manually, that text console will still be logged in. To disable this keystroke globally and permanently, you need to set the <code>DontZap</code> flag in your <i>xorg.conf</i> or <i>XF86Config</i> or <i>XF86Config-4</i> file, depending which is in use on your system. See <code><a href="/docs/linux/man/5-xf86config/">XF86Config</a></code>(5) for details.</p>
<dt><code>Ctrl-Alt-F1, Ctrl-Alt-F2, etc.</code></p>
<dd> These keystrokes will switch to a different virtual console, while leaving the console that X11 is running on locked. If you left a shell logged in on another virtual console, it is unprotected. So don&#8217;t leave yourself logged in on other consoles. You can disable VT switching globally and permanently by setting <code>DontVTSwitch</code> in your <i>xorg.conf</i>, but that might make your system harder to use, since VT switching is an actual useful feature. </p>
<p> There is no way to disable VT switching only when the screen is locked. It&#8217;s all or nothing.</p>
<dt><code>Ctrl-Alt-KP_Multiply</code></p>
<dd> This keystroke kills any X11 app that holds a lock, so typing this will kill xscreensaver and unlock the screen. This so-called &quot;feature&quot; showed up in the X server in 2008, and as of 2011, some vendors are shipping it turned on by default. How nice. You can disable it by turning off <code>AllowClosedownGrabs</code> in <i>xorg.conf</i>.</p>
<dt><code>Alt-SysRq-F</code></p>
<dd> This is the Linux kernel &quot;OOM-killer&quot; keystroke. It shoots down random long-running programs of its choosing, and so might might target and kill xscreensaver, and there&#8217;s no way for xscreensaver to protect itself from that. You can disable it globally with: </p>
<pre>
echo 176 &gt; /proc/sys/kernel/sysrq
</pre>
</dl>
</dl>
<p> There&#8217;s little that I can do to make the screen locker be secure so long as the kernel and X11 developers are <i>actively</i> working against security like this. The strength of the lock on your front door doesn&#8217;t matter much so long as someone else in the house insists on leaving a key under the welcome mat.</p>
<dt><code>Dangerous Backdoor Server Extensions</code></p>
<dd> Many distros enable by default several X11 server extensions that can be used to bypass grabs, and thus snoop on you while you&#8217;re typing your password. These extensions are nominally for debugging and automation, but they are also security-circumventing keystroke loggers. If your server is configured to load the <code>RECORD, XTRAP</code> or <code>XTEST</code> extensions, you absolutely should disable those, 100% of the time. Look for them in <i>xorg.conf</i> or whatever it is called.</dl>
<h2>X RESOURCES</h2>
<p> These are the X resources use by the <i>xscreensaver</i> program. You probably won&#8217;t need to change these manually (that&#8217;s what the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) program is for).</p>
<dl>
<dt><code>timeout</code> (class <code>Time</code>)</p>
<dd> The screensaver will activate (blank the screen) after the keyboard and mouse have been idle for this many minutes. Default 10 minutes.</p>
<dt><code>cycle</code> (class <code>Time</code>)</p>
<dd> After the screensaver has been running for this many minutes, the currently running graphics-hack sub-process will be killed (with <code>SIGTERM</code>), and a new one started. If this is 0, then the graphics hack will never be changed: only one demo will run until the screensaver is deactivated by user activity. Default 10 minutes. </p>
<p> The running saver will be restarted every <i>cycle</i> minutes even when <i>mode</i> is <i>one</i>, since some savers tend to converge on a steady state.</p>
<dt><code>lock</code> (class <code>Boolean</code>)</p>
<dd> Enable locking: before the screensaver will turn off, it will require you to type the password of the logged-in user (really, the person who ran xscreensaver), or the root password. (<code>Note:</code> this doesn&#8217;t work if the screensaver is launched by <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1) because it can&#8217;t know the user-id of the logged-in user. See the &quot;<i>Using <a href="/docs/linux/man/1-xdm/">XDM</a>(1)</i>&quot; section, below.</p>
<dt><code>lockTimeout</code> (class <code>Time</code>)</p>
<dd> If locking is enabled, this controls the length of the &quot;grace period&quot; between when the screensaver activates, and when the screen becomes locked. For example, if this is 5, and <i>-timeout</i> is 10, then after 10 minutes, the screen would blank. If there was user activity at 12 minutes, no password would be required to un-blank the screen. But, if there was user activity at 15 minutes or later (that is, <i>-lock-timeout</i> minutes after activation) then a password would be required. The default is 0, meaning that if locking is enabled, then a password will be required as soon as the screen blanks.</p>
<dt><code>passwdTimeout</code> (class <code>Time</code>)</p>
<dd> If the screen is locked, then this is how many seconds the password dialog box should be left on the screen before giving up (default 30 seconds). This should not be too large: the X server is grabbed for the duration that the password dialog box is up (for security purposes) and leaving the server grabbed for too long can cause problems.</p>
<dt><code>dpmsEnabled</code> (class <code>Boolean</code>)</p>
<dd> Whether power management is enabled.</p>
<dt><code>dpmsStandby</code> (class <code>Time</code>)</p>
<dd> If power management is enabled, how long until the monitor goes solid black.</p>
<dt><code>dpmsSuspend</code> (class <code>Time</code>)</p>
<dd> If power management is enabled, how long until the monitor goes into power-saving mode.</p>
<dt><code>dpmsOff</code> (class <code>Time</code>)</p>
<dd> If power management is enabled, how long until the monitor powers down completely. Note that these settings will have no effect unless both the X server and the display hardware support power management; not all do. See the <i>Power Management</i> section, below, for more information.</p>
<dt><code>dpmsQuickOff</code> (class <code>Boolean</code>)</p>
<dd> If <i>mode</i> is <i>blank</i> and this is true, then the screen will be powered down immediately upon blanking, regardless of other power-management settings.</p>
<dt><code>visualID</code> (class <code>VisualID</code>)</p>
<dd> This is an historical artifacts left over from when 8-bit displays were still common. You should probably ignore this. </p>
<p> Specify which X visual to use by default. (Note carefully that this resource is called <code>visualID</code>, not merely <code>visual</code>; if you set the <code>visual</code> resource instead, things will malfunction in obscure ways for obscure reasons.) </p>
<p> Legal values for the <code>VisualID</code> resource are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default</code></p>
<dd> Use the screen&#8217;s default visual (the visual of the root window). This is the default.</p>
<dt><code>best</code></p>
<dd> Use the visual which supports the most colors. Note, however, that the visual with the most colors might be a TrueColor visual, which does not support colormap animation. Some programs have more interesting behavior when run on PseudoColor visuals than on TrueColor.</p>
<dt><code>mono</code></p>
<dd> Use a monochrome visual, if there is one.</p>
<dt><code>gray</code></p>
<dd> Use a grayscale or staticgray visual, if there is one and it has more than one plane (that is, it&#8217;s not monochrome).</p>
<dt><code>color</code></p>
<dd> Use the best of the color visuals, if there are any.</p>
<dt><code>GL</code></p>
<dd> Use the visual that is best for OpenGL programs. (OpenGL programs have somewhat different requirements than other X programs.)</p>
<dt><i>class</i></p>
<dd> where <i>class</i> is one of <code>StaticGray</code>, <code>StaticColor</code>, <code>TrueColor</code>, <code>GrayScale</code>, <code>PseudoColor</code>, or <code>DirectColor</code>. Selects the deepest visual of the given class.</p>
<dt><i>number</i></p>
<dd> where <i>number</i> (decimal or hex) is interpreted as a visual id number, as reported by the <code><a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a></code>(1) program; in this way you can have finer control over exactly which visual gets used, for example, to select a shallower one than would otherwise have been chosen. </p>
</dl>
</dl>
<dl>
<dt>
<dd> Note that this option specifies only the <i>default</i> visual that will be used: the visual used may be overridden on a program-by-program basis. See the description of the <code>programs</code> resource, below.</dl>
<dt><code>installColormap</code> (class <code>Boolean</code>)</p>
<dd> On PseudoColor (8-bit) displays, install a private colormap while the screensaver is active, so that the graphics hacks can get as many colors as possible. This is the default. (This only applies when the screen&#8217;s default visual is being used, since non-default visuals get their own colormaps automatically.) This can also be overridden on a per-hack basis: see the discussion of the <code>default-n</code> name in the section about the <code>programs</code> resource. </p>
<p> This does nothing if you have a TrueColor (16-bit or deeper) display. (Which, in this century, you do.)</p>
<dt><code>verbose</code> (class <code>Boolean</code>)</p>
<dd> Whether to print diagnostics. Default false.</p>
<dt><code>timestamp</code> (class <code>Boolean</code>)</p>
<dd> Whether to print the time of day along with any other diagnostic messages. Default true.</p>
<dt><code>splash</code> (class <code>Boolean</code>)</p>
<dd> Whether to display a splash screen at startup. Default true.</p>
<dt><code>splashDuration</code> (class <code>Time</code>)</p>
<dd> How long the splash screen should remain visible; default 5 seconds.</p>
<dt><code>helpURL</code> (class <code>URL</code>)</p>
<dd> The splash screen has a <i>Help</i> button on it. When you press it, it will display the web page indicated here in your web browser.</p>
<dt><code>loadURL</code> (class <code>LoadURL</code>)</p>
<dd> This is the shell command used to load a URL into your web browser. The default setting will load it into Mozilla/Netscape if it is already running, otherwise, will launch a new browser looking at the <i>helpURL</i>.</p>
<dt><code>demoCommand</code> (class <code>DemoCommand</code>)</p>
<dd> This is the shell command run when the <i>Demo</i> button on the splash window is pressed. It defaults to <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1).</p>
<dt><code>prefsCommand</code> (class <code>PrefsCommand</code>)</p>
<dd> This is the shell command run when the <i>Prefs</i> button on the splash window is pressed. It defaults to <i>xscreensaver-demo -prefs</i>.</p>
<dt><code>newLoginCommand</code> (class <code>NewLoginCommand</code>)</p>
<dd> If set, this is the shell command that is run when the &quot;New Login&quot; button is pressed on the unlock dialog box, in order to create a new desktop session without logging out the user who has locked the screen. Typically this will be some variant of <code><a href="/docs/linux/man/1-gdmflexiserver/">gdmflexiserver</a></code>(1), <code><a href="/docs/linux/man/1-kdmctl/">kdmctl</a></code>(1), <code><a href="/docs/linux/man/1-lxdm/">lxdm</a></code>(1) or <code><a href="/docs/linux/man/1-dm-tool/">dm-tool</a></code>(1).</p>
<dt><code>nice</code> (class <code>Nice</code>)</p>
<dd> The sub-processes created by <i>xscreensaver</i> will be &quot;niced&quot; to this level, so that they are given lower priority than other processes on the system, and don&#8217;t increase the load unnecessarily. The default is 10. (Higher numbers mean lower priority; see <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1) for details.)</p>
<dt><code>fade</code> (class <code>Boolean</code>)</p>
<dd> If this is true, then when the screensaver activates, the current contents of the screen will fade to black instead of simply winking out. This only works on certain systems. A fade will also be done when switching graphics hacks (when the <i>cycle</i> timer expires). Default: true.</p>
<dt><code>unfade</code> (class <code>Boolean</code>)</p>
<dd> If this is true, then when the screensaver deactivates, the original contents of the screen will fade in from black instead of appearing immediately. This only works on certain systems, and if <i>fade</i> is true as well. Default false.</p>
<dt><code>fadeSeconds</code> (class <code>Time</code>)</p>
<dd> If <i>fade</i> is true, this is how long the fade will be in seconds (default 3 seconds).</p>
<dt><code>fadeTicks</code> (class <code>Integer</code>)</p>
<dd> If <i>fade</i> is true, this is how many times a second the colormap will be changed to effect a fade. Higher numbers yield smoother fades, but may make the fades take longer than the specified <i>fadeSeconds</i> if your server isn&#8217;t fast enough to keep up. Default 20.</p>
<dt><code>captureStderr</code> (class <code>Boolean</code>)</p>
<dd> Whether <i>xscreensaver</i> should redirect its stdout and stderr streams to the window itself. Since its nature is to take over the screen, you would not normally see error messages generated by xscreensaver or the sub-programs it runs; this resource will cause the output of all relevant programs to be drawn on the screensaver window itself, as well as being written to the controlling terminal of the screensaver driver process. Default true.</p>
<dt><code>ignoreUninstalledPrograms</code> (class <code>Boolean</code>)</p>
<dd> There may be programs in the list that are not installed on the system, yet are marked as &quot;enabled&quot;. If this preference is true, then such programs will simply be ignored. If false, then a warning will be printed if an attempt is made to run the nonexistent program. Also, the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) program will suppress the non-existent programs from the list if this is true. Default: false.</p>
<dt><code>authWarningSlack</code> (class <code>Integer</code>)</p>
<dd> If <i>all</i> failed unlock attempts (incorrect password entered) were made within this period of time, the usual dialog that warns about such attempts after a successful login will be suppressed. The assumption is that incorrect passwords entered within a few seconds of a correct one are user error, rather than hostile action. Default 20 seconds.</p>
<dt><code>GetViewPortIsFullOfLies</code> (class <code>Boolean</code>)</p>
<dd> Set this to true if the xscreensaver window doesn&#8217;t cover the whole screen. This works around a longstanding XFree86 bug #421. See the xscreensaver FAQ for details.</p>
<dt><code>font</code> (class <code>Font</code>)</p>
<dd> The font used for the stdout/stderr text, if <code>captureStderr</code> is true. Default <code>*-medium-r-*-140-*-m-*</code> (a 14 point fixed-width font).</p>
<dt><code>mode</code> (class <code>Mode</code>)</p>
<dd> Controls the behavior of xscreensaver. Legal values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>random</code></p>
<dd> When blanking the screen, select a random display mode from among those that are enabled and applicable. This is the default.</p>
<dt><code>random-same</code></p>
<dd> Like <i>random</i>, but if there are multiple screens, each screen will run the <i>same</i> random display mode, instead of each screen running a different one.</p>
<dt><code>one</code></p>
<dd> When blanking the screen, only ever use one particular display mode (the one indicated by the <i>selected</i> setting).</p>
<dt><code>blank</code></p>
<dd> When blanking the screen, just go black: don&#8217;t run any graphics hacks.</p>
<dt><code>off</code></p>
<dd> Don&#8217;t ever blank the screen, and don&#8217;t ever allow the monitor to power down. </p>
</dl>
</dl>
<dt><code>selected</code> (class <code>Integer</code>)</p>
<dd> When <i>mode</i> is set to <i>one</i>, this is the one, indicated by its index in the <i>programs</i> list. You&#8217;re crazy if you count them and set this number by hand: let <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) do it for you!</p>
<dt><code>programs</code> (class <code>Programs</code>)</p>
<dd> The graphics hacks which <i>xscreensaver</i> runs when the user is idle. The value of this resource is a multi-line string, one <i>sh</i>-syntax command per line. Each line must contain exactly one command: no semicolons, no ampersands. </p>
<p> When the screensaver starts up, one of these is selected (according to the <code>mode</code> setting), and run. After the <i>cycle</i> period expires, it is killed, and another is selected and run. </p>
<p> If a line begins with a dash (-) then that particular program is disabled: it won&#8217;t be selected at random (though you can still select it explicitly using the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) program). </p>
<p> If all programs are disabled, then the screen will just be made blank, as when <i>mode</i> is set to <i>blank</i>. </p>
<p> To disable a program, you must mark it as disabled with a dash instead of removing it from the list. This is because the system-wide (app-defaults) and per-user (.xscreensaver) settings are merged together, and if a user just <i>deletes</i> an entry from their programs list, but that entry still exists in the system-wide list, then it will come back. However, if the user <i>disables</i> it, then their setting takes precedence. </p>
<p> If the display has multiple screens, then a different program will be run for each screen. (All screens are blanked and unblanked simultaneously.) </p>
<p> Note that you must escape the newlines; here is an example of how you might set this in your <i>~/.xscreensaver</i> file: </p>
<dl>
<dt>
<dd>
<pre>
programs:  \
       qix -root                          
\
       ico -r -faces -sleep 1 -obj ico    
\
       xdaliclock -builtin2 -root         
\
       xv -root -rmode 5 image.gif -quit  

</pre>
</dl>
<dl>
<dt>
<dd> Make sure your <code>$PATH</code> environment variable is set up correctly <i>before</i> xscreensaver is launched, or it won&#8217;t be able to find the programs listed in the <i>programs</i> resource. </p>
<p> To use a program as a screensaver, two things are required: that that program draw on the root window (or be able to be configured to draw on the root window); and that that program understand &quot;virtual root&quot; windows, as used by virtual window managers such as <code><a href="/docs/linux/man/1-tvtwm/">tvtwm</a></code>(1). (Generally, this is accomplished by just including the <i>&quot;vroot.h&quot;</i> header file in the program&#8217;s source.) </p>
<p> <code>Visuals:</code> </p>
<p> Because xscreensaver was created back when dinosaurs roamed the earth, it still contains support for some things you&#8217;ve probably never seen, such as 1-bit monochrome monitors, grayscale monitors, and monitors capable of displaying only 8-bit colormapped images. </p>
<p> If there are some programs that you want to run only when using a color display, and others that you want to run only when using a monochrome display, you can specify that like this: </p>
<pre>
       mono:   mono-program  -root        
\
       color:  color-program -root        
\
</pre>
</dl>
<dl>
<dt>
<dd> More generally, you can specify the kind of visual that should be used for the window on which the program will be drawing. For example, if one program works best if it has a colormap, but another works best if it has a 24-bit visual, both can be accommodated: </p>
<pre>
       PseudoColor: cmap-program  -root   
\
       TrueColor:   24bit-program -root   
\
</pre>
</dl>
<dl>
<dt>
<dd> In addition to the symbolic visual names described above (in the discussion of the <i>visualID</i> resource) one other visual name is supported in the <i>programs</i> list:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default-n</code></p>
<dd> This is like <code>default</code>, but also requests the use of the default colormap, instead of a private colormap. (That is, it behaves as if the <i>-no-install</i> command-line option was specified, but only for this particular hack.) This is provided because some third-party programs that draw on the root window (notably: <code><a href="/docs/linux/man/1-xv/">xv</a></code>(1), and <code><a href="/docs/linux/man/1-xearth/">xearth</a></code>(1)) make assumptions about the visual and colormap of the root window: assumptions which xscreensaver can violate. </p>
</dl>
</dl>
<p> If you specify a particular visual for a program, and that visual does not exist on the screen, then that program will not be chosen to run. This means that on displays with multiple screens of different depths, you can arrange for appropriate hacks to be run on each. For example, if one screen is color and the other is monochrome, hacks that look good in mono can be run on one, and hacks that only look good in color will show up on the other.</dl>
</dl>
<p> You shouldn&#8217;t ever need to change the following resources: </p>
<dl>
<dt><code>pointerPollTime</code> (class <code>Time</code>)</p>
<dd> When server extensions are not in use, this controls how frequently <i>xscreensaver</i> checks to see if the mouse position or buttons have changed. Default 5 seconds.</p>
<dt><code>pointerHysteresis</code> (class <code>Integer</code>)</p>
<dd> If the mouse moves less than this-many pixels in a second, ignore it (do not consider that to be &quot;activity&quot;). This is so that the screen doesn&#8217;t un-blank (or fail to blank) just because you bumped the desk. Default: 10 pixels.</p>
<dt><code>windowCreationTimeout</code> (class <code>Time</code>)</p>
<dd> When server extensions are not in use, this controls the delay between when windows are created and when <i>xscreensaver</i> selects events on them. Default 30 seconds.</p>
<dt><code>initialDelay</code> (class <code>Time</code>)</p>
<dd> When server extensions are not in use, <i>xscreensaver</i> will wait this many seconds before selecting events on existing windows, under the assumption that <i>xscreensaver</i> is started during your login procedure, and the window state may be in flux. Default 0. (This used to default to 30, but that was back in the days when slow machines and X terminals were more common&#8230;)</p>
<dt><code>procInterrupts</code> (class <code>Boolean</code>)</p>
<dd> This resource controls whether the <code>/proc/interrupts</code> file should be consulted to decide whether the user is idle. This is the default if <i>xscreensaver</i> has been compiled on a system which supports this mechanism (i.e., Linux systems). </p>
<p> The benefit to doing this is that <i>xscreensaver</i> can note that the user is active even when the X console is not the active one: if the user is typing in another virtual console, xscreensaver will notice that and will fail to activate. For example, if you&#8217;re playing Quake in VGA-mode, xscreensaver won&#8217;t wake up in the middle of your game and start competing for CPU. </p>
<p> The drawback to doing this is that perhaps you <i>really do</i> want idleness on the X console to cause the X display to lock, even if there is activity on other virtual consoles. If you want that, then set this option to False. (Or just lock the X console manually.) </p>
<p> The default value for this resource is True, on systems where it works.</p>
<dt><code>overlayStderr</code> (class <code>Boolean</code>)</p>
<dd> If <code>captureStderr</code> is True, and your server supports &quot;overlay&quot; visuals, then the text will be written into one of the higher layers instead of into the same layer as the running screenhack. Set this to False to disable that (though you shouldn&#8217;t need to).</p>
<dt><code>overlayTextForeground</code> (class <code>Foreground</code>)</p>
<dd> The foreground color used for the stdout/stderr text, if <code>captureStderr</code> is true. Default: Yellow.</p>
<dt><code>overlayTextBackground</code> (class <code>Background</code>)</p>
<dd> The background color used for the stdout/stderr text, if <code>captureStderr</code> is true. Default: Black.</p>
<dt><code>bourneShell</code> (class <code>BourneShell</code>)</p>
<dd> The pathname of the shell that <i>xscreensaver</i> uses to start subprocesses. This must be whatever your local variant of <code>/bin/sh</code> is: in particular, it must not be <code>csh</code>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number, and to inform the sub-programs of the screen on which to draw.</p>
<dt><code>XSCREENSAVER_WINDOW</code></p>
<dd> Passed to sub-programs to indicate the ID of the window on which they should draw. This is necessary on Xinerama/RANDR systems where multiple physical monitors share a single X11 &quot;Screen&quot;.</p>
<dt><code>PATH</code></p>
<dd> to find the sub-programs to run.</p>
<dt><code>HOME</code></p>
<dd> for the directory in which to read the <i>.xscreensaver</i> file.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>UPGRADES</h2>
<p> The latest version of xscreensaver, an online version of this manual, and a FAQ can always be found at <a rel="nofollow" href="https://www.jwz.org/xscreensaver/">https://www.jwz.org/xscreensaver/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-xsecurity/">Xsecurity</a></code>(1), <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1), <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code><a href="/docs/linux/man/1-gdm/">gdm</a></code>(1), <code><a href="/docs/linux/man/1-xhost/">xhost</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-gl-helper/">xscreensaver-gl-helper</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-getimage/">xscreensaver-getimage</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-text/">xscreensaver-text</a></code>(1).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1991-2018 by Jamie Zawinski. Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty.</p>
<h2>AUTHOR</h2>
<p> Jamie Zawinski &lt;jwz [at] jwz.org&gt;. Written in late 1991; version 1.0 posted to comp.sources.x on 17-Aug-1992. </p>
<p> Please let me know if you find any bugs or make any improvements. </p>
<p> And a huge thank you to the hundreds of people who have contributed, in large ways and small, to the xscreensaver collection over the past two decades! </p>
<h2>Index</h2>
