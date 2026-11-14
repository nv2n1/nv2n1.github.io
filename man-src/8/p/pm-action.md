---
title: "pm-action(8)"
name: "pm-action"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pm-action/"
description: "pm-action – Suspend or Hibernate your computer"
---

<p>pm-action &#8211; Suspend or Hibernate your computer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pm-hibernate</code> [&#8211;help]</p>
<dt> <code>pm-suspend</code> [&#8211;quirk-*] [&#8211;help]</p>
<dt> <code>pm-suspend-hybrid</code> [&#8211;quirk-*] [&#8211;help]</dl>
<h2>Description</h2>
<dd>This manual page documents briefly the <code>pm-action</code>, <code>pm-hibernate</code>, <code>pm-suspend</code> and <code>pm-suspend-hybrid</code> commands. This manual page was originally written for the Debian(TM) distribution and has been adopted by the pm-utils project. </p>
<p> These commands can be used to put the machine in a sleep state. The precise way how this is done can be influenced by installing executables and configuration snippets. For some options external programs are needed. </p>
<p> These commands will usually be called by <code>UPower</code> or <code>hald</code> when triggered to do so by a program in a desktop session such as <code>gnome-power-manager</code>. Calling them from the command line is also possible, but it is not guaranteed that all programs in your desktop session keep working as expected. </p>
<p> <code>pm-suspend</code></p>
<dl>
<dd>During suspend most devices are shutdown, and system state is saved in RAM. The system still requires power in this state. Most modern systems require 3 to 5 seconds to enter and leave suspend, and most laptops can stay in suspend mode for 1 to 3 days before exhausting their battery.</dl>
<p> <code>pm-hibernate</code></p>
<dl>
<dd>During hibernate the system is fully powered off, and system state is saved to disk. The system does not require power, and can stay in hibernate mode indefinitely. Most modern systems require 15 to 45 seconds to enter and leave hibernate, and entering and leaving hibernate takes longer when you have more memory.</dl>
<p> <code>pm-suspend-hybrid</code></p>
<dl>
<dd>Hybrid-suspend is the process where the system does everything it needs to hibernate, but suspends instead of shutting down. This means that your computer can wake up quicker than for normal hibernation if you do not run out of power, and you can resume even if you run out of power. <a href="/docs/linux/man/8-s2both/">s2both</a>(8) is an hybrid-suspend implementation.</dl>
<h2>Options</h2>
<p>On some hardware putting the video card in the suspend state and recovering from it needs some special quirk handling. With the &#8211;quirk-* options of the <code>pm-suspend</code> and <code>pm-suspend-hybrid</code> commands you can select which quirks should be used. </p>
<p> If <code>pm-suspend</code>, <code>pm-hibernate</code>, or <code>pm-suspend-hybrid</code> are invoked without any commandline parameters, they will try to grab the correct quirks from the internal quirk database. </p>
<p> <code>&#8211;quirk-dpms-on</code></p>
<dl>
<dd>This option forces the video hardware to turn on the screen during resume. Most video adapters turn on the screen themselves, but if you get a blank screen on resume that can be turned back on by moving the mouse or typing then this option may be useful.</dl>
<p> <code>&#8211;quirk-dpms-suspend</code></p>
<dl>
<dd>This option forces the video hardware to turn off the screen when suspending. Most video adapters seem to do this correctly, but some do not, which wastes lots of power. If your screen is still on after successfully suspending you may need to use this option.</dl>
<p> <code>&#8211;quirk-none</code></p>
<dl>
<dd>This option disables quirks.</dl>
<p> <code>&#8211;quirk-radeon-off</code></p>
<dl>
<dd>This option forces Radeon hardware to turn off the display during suspend and turn it back on during resume. You only need to do this on some old ThinkPads of the &#8217;30 series (T30, X31, R32,&#8230; ) with Radeon video hardware.</dl>
<p> <code>&#8211;quirk-reset-brigthness</code></p>
<dl>
<dd>This option resets display brightness during resume (i.e. sets the brightness to 0 and returns it to the previous value).</dl>
<p> <code>&#8211;quirk-s3-bios</code></p>
<dl>
<dd>This option calls the video BIOS during S3 resume. Unfortunately, it is not always allowed to call the video BIOS at this point, so sometimes adding this option can actually break resume on some systems.</dl>
<p> <code>&#8211;quirk-s3-mode</code></p>
<dl>
<dd>This option initializes the video card into a VGA text mode, and then uses the BIOS to set the video mode. On some systems S3 BIOS only initializes the video BIOS to text mode, and so both S3 BIOS and S3 MODE are needed.</dl>
<p> <code>&#8211;quirk-vbe-post</code></p>
<dl>
<dd>This option will attempt to reinitialize the video card when resuming from suspend, using the same code the system BIOS uses at boot in order to initialize the video hardware. Not all video cards need this, and using this option on systems where it is not needed can cause a system to lock up when resuming.</dl>
<p> <code>&#8211;quirk-vbemode-restore</code></p>
<dl>
<dd>This option will save and restore the current VESA mode which may be necessary to avoid X screen corruption. Using this feature on Intel graphics hardware is probably a bad idea.</dl>
<p> <code>&#8211;quirk-vbestate-restore</code></p>
<dl>
<dd>This option saves and restores some low level hardware state which may be invalid after suspend.</dl>
<p> <code>&#8211;quirk-vga-mode-3</code></p>
<dl>
<dd>This option will try to force the video card into a standard text mode on resume.</dl>
<p> <code>&#8211;quirk-save-pci</code></p>
<dl>
<dd>Save the PCI config space for the VGA card.</dl>
<p> <code>&#8211;store-quirks-as-lkw</code></p>
<dl>
<dd>Save the quirks the video adaptor required by <code>pm-suspend</code> or <code>pm-suspend-hybrid</code> as an .quirkdb file that is specific to this system. The file will be saved in /etc/pm/last_known_working.quirkdb. This parameter will only save the actual quirks that were used to successfully suspend/resume a system, and will be specific to the exact configuration of that system, including the video hardware, video driver, and whether or not kernel modesetting was used.</dl>
<h2>Files</h2>
<p>/etc/pm/config.d</p>
<dl>
<dd>The files in this directory are evaluated in C sort order. These files can be provided by individual packages outside of pm-utils. If a global configuration variable is set, the value set to will be appended to the previous value. If any other variable is set, it will be ignored. The syntax is simply: VAR_NAME=value. See the CONFIGURATION VARIABLES section for valid variables defined by pm-utils. External packages can define others, see their respective documentation for more information.</dl>
<p> /etc/pm/sleep.d, /usr/lib/pm-utils/sleep.d</p>
<dl>
<dd>Programs in these directories (called hooks) are combined and executed in C sort order before suspend and hibernate with as argument &#8216;suspend&#8217; or &#8216;hibernate&#8217;. Afterwards they are called in reverse order with argument &#8216;resume&#8217; and &#8216;thaw&#8217; respectively. If both directories contain a similar named file, the one in /etc/pm/sleep.d will get preference. It is possible to disable a hook in the distribution directory by putting a non-executable file in /etc/pm/sleep.d, or by adding it to the HOOK_BLACKLIST configuration variable.</dl>
<p> /var/log/pm-suspend.log</p>
<dl>
<dd>The log file shows what was done on the last suspend/hibernate and resume/thaw.</dl>
<h2>Sleep Hook Ordering Convention</h2>
<p>00 &#8211; 49</p>
<dl>
<dd>User and most package supplied hooks. If a hook assumes that all of the usual services and userspace infrastructure is still running, it should be here.</dl>
<p> 50 &#8211; 74</p>
<dl>
<dd>Service handling hooks. Hooks that start or stop a service belong in this range. At or before 50, hooks can assume that all services are still enabled.</dl>
<p> 75 &#8211; 89</p>
<dl>
<dd>Module and non-core hardware handling. If a hook needs to load/unload a module, or if it needs to place non-video hardware that would otherwise break suspend or hibernate into a safe state, it belongs in this range. At or before 75, hooks can assume all modules are still loaded.</dl>
<p> 90 &#8211; 99</p>
<dl>
<dd>Reserved for critical suspend hooks.</dl>
<h2>Configuration Variables</h2>
<p>Configuration variables defined by pm-utils. These can be set in any file in /etc/pm/config.d/. </p>
<p> <code>SLEEP_MODULE [=kernel]</code></p>
<dl>
<dd>The default suspend backend to use. Valid values are: </p>
<p> <i>kernel</i></p>
<dl>
<dd>The built-in kernel suspend/resume support. Use this if nothing else is supported on your system. The kernel backend is always used if nothing else is available.</dl>
<p> <i>uswsusp</i></p>
<dl>
<dd>If your system has support for the userspace suspend programs (s2ram/s2disk/s2both), then use this.</dl>
<p> <i>tuxonice</i></p>
<dl>
<dd>If your system has support for tuxonice/suspend2, use this.</dl>
</dl>
<p> <code>HIBERNATE_RESUME_POST_VIDEO [=no]</code></p>
<dl>
<dd>If video should be posted after hibernate, just like after suspend. You should not normally need to set this.</dl>
<p> <code>SUSPEND_MODULES</code></p>
<dl>
<dd>Space separated list of modules to unload before suspend.</dl>
<p> <code>HOOK_BLACKLIST</code></p>
<dl>
<dd>Space separated list of hooks that should be disabled.</dl>
<p> <code>HIBERNATE_MODE</code></p>
<dl>
<dd>Default method to power down the system when hibernating. If not set, the system will use the kernel default as a default value. Check /sys/power/disk for valid values. The default value will be surrounded by [square brackets].</dl>
<p> <code>NEED_CLOCK_SYNC</code></p>
<dl>
<dd>If your system clock drifts across a suspend/resume or hibernate/thaw cycle, you should set this to true. This will cause pm-utils to synchronize the system clock whenever going through a sleep/wake cycle at the expense of making suspend/resume take longer.</dl>
<p> <code>PM_HIBERNATE_DELAY [=900]</code></p>
<dl>
<dd>If you are using kernel suspend/resume and invoke <code>pm-suspend-hybrid</code>, this environment variable controls how many seconds the system will wait after going into suspend before waking back up and hibernating. By default, this is set to 900 seconds (15 minutes).</dl>
<h2>Return Values</h2>
<p>Return values less than 128 mean that pm-action failed before trying to put the system in the requested power saving state. A return value of 128 means that pm-action tried to put the machine in the requested power state but failed. A return value greater than 128 means pm-action encountered an error and also failed to enter the requested power saving state.</p>
<h2>Debugging</h2>
<p>Debugging suspend/resume can be a tricky process, and is covered in more detail in /usr/share/doc/pm-utils/README.debugging.</p>
<h2>Bugs</h2>
<p>The upstream BTS can be found at m[blue]<code><a rel="nofollow" href="https://bugs.freedesktop.org/">https://bugs.freedesktop.org/</a></code>m[]. Select &#8216;pm-utils&#8217; as product.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-s2ram/">s2ram</a></code>(8), <code><a href="/docs/linux/man/8-s2disk/">s2disk</a></code>(8), <code><a href="/docs/linux/man/8-s2both/">s2both</a></code>(8), <code><a href="/docs/linux/man/1-pm-is-supported/">pm-is-supported</a></code>(1), <code><a href="/docs/linux/man/8-pm-powersave/">pm-powersave</a></code>(8), <code><a href="/docs/linux/man/8-vbetool/">vbetool</a></code>(8), <code><a href="/docs/linux/man/8-radeontool/">radeontool</a></code>(8)</p>
<h2>Author</h2>
<p><code>Tim Dijkstra</code> &lt;tim [at] famdijkstra.org&gt;</p>
<dl>
<dd>Manpage author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Tim Dijkstra </p>
<p> This manual page was originally written for the Debian(TM) system, and has been adopted by the pm-utils project. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or (at your option) any later version published by the Free Software Foundation.</p>
