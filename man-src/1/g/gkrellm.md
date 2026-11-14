---
title: "gkrellm(1)"
name: "gkrellm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gkrellm/"
description: "gkrellm – The GNU Krell Monitors"
---

<h2 class="name">NAME</h2>
<p> gkrellm &#8211; The GNU Krell Monitors</p>
<h2>SYNOPSIS</h2>
<p> <code>gkrellm</code> [ <code>&#8211;help</code> ] [ <code>-t</code> | <code>&#8211;theme</code> dir ] [ <code>-g</code> | <code>&#8211;geometry</code> +x+y ] [ <code>-wm</code> ] [ <code>-w</code> | <code>&#8211;withdrawn</code> ] [ <code>-c</code> | <code>&#8211;config</code> suffix ] [ <code>-nc</code> ] [ <code>-f</code> | <code>&#8211;force-host-config</code> ] [ <code>-demo</code> ] [ <code>-p</code> | <code>&#8211;plugin</code> plugin.so ] [ <code>-s</code> | <code>&#8211;server</code> hostname ] [ <code>-P</code> | <code>&#8211;port</code> server_port ] [ <code>-l</code> | <code>&#8211;logfile</code> path ] </p>
<h2>DESCRIPTION</h2>
<p> With a single process, <code>gkrellm</code> manages multiple stacked monitors and supports applying themes to match the monitors appearance to your window manager, Gtk, or any other theme. </p>
<h3>FEATURES</h3>
<dl>
<dt>&bull;</p>
<dd> SMP CPU, Disk, Proc, and active net interface monitors with LEDs.</p>
<dt>&bull;</p>
<dd> Internet monitor that displays current and charts historical port hits.</p>
<dt>&bull;</p>
<dd> Memory and swap space usage meters and a system uptime monitor.</p>
<dt>&bull;</p>
<dd> File system meters show capacity/free space and can mount/umount.</p>
<dt>&bull;</p>
<dd> A mbox/maildir/MH/POP3/IMAP mail monitor which can launch a mail reader or remote mail fetch program.</p>
<dt>&bull;</p>
<dd> Clock/calendar and hostname display.</p>
<dt>&bull;</p>
<dd> Laptop Battery monitor.</p>
<dt>&bull;</p>
<dd> CPU/motherboard temperature/fan/voltages display with warnings and alarms. Linux requires a sensor configured sysfs, lm_sensors modules or a running mbmon daemon. FreeBSD can also read the mbmon daemon. Windows requires MBM.</p>
<dt>&bull;</p>
<dd> Disk temperatures if there&#8217;s a running hddtemp daemon.</p>
<dt>&bull;</p>
<dd> Multiple monitors managed by a single process to reduce system load.</p>
<dt>&bull;</p>
<dd> A timer button that can execute PPP or ISDN logon/logoff scripts.</p>
<dt>&bull;</p>
<dd> Charts are autoscaling with configurable grid line resolution, or</p>
<dt>&bull;</p>
<dd> can be set to a fixed scale mode.</p>
<dt>&bull;</p>
<dd> Separate colors for &quot;in&quot; and &quot;out&quot; data. The in color is used for CPU user time, disk read, forks, and net receive data. The out color is used for CPU sys time, disk write, load, and net transmit data.</p>
<dt>&bull;</p>
<dd> Commands can be configured to run when monitor labels are clicked.</p>
<dt>&bull;</p>
<dd> Data can be collected from a <code>gkrellmd</code> server running on a remote machine.</p>
<dt>&bull;</p>
<dd> <code>gkrellm</code> is plugin capable so special interest monitors can be created.</p>
<dt>&bull;</p>
<dd> Many themes are available. </p>
</dl>
<h3>USER INTERFACE</h3>
<p> <code></p>
<dl>
<dt>&bull; Top frame</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 1</i></p>
<dd> Press and drag to move <code>gkrellm</code> window.</p>
<dt><i>Btn 3</i></p>
<dd> Popup main menu.</dl>
</dl>
<p> <code></p>
<dt>&bull; Side frames</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 2</i></p>
<dd> Slide <code>gkrellm</code> window shut (Btn1 if -m2 option).</p>
<dt><i>Btn 3</i></p>
<dd> Popup main menu.</dl>
</dl>
<p> <code></p>
<dt>&bull; All charts</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 1</i></p>
<dd> Toggle draw of extra info on the chart.</p>
<dt><i>Btn 3</i></p>
<dd> Brings up a chart configuration window.</dl>
</dl>
<p> <code></p>
<dt>&bull; Inet charts</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 2</i></p>
<dd> Toggle between port hits per minute and hour.</dl>
</dl>
<p> <code></p>
<dt>&bull; Most panels</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 3</i></p>
<dd> Opens the configuration window directly to a monitor&#8217;s configuration page.</dl>
</dl>
<p> <code></p>
<dt>&bull; File System meter panels</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 1,2</i></p>
<dd> Toggle display of label and fs capacity scrolling display. The mount button runs mount/umount commands. If ejectable, left click the eject button to open tray, right click to close.</dl>
</dl>
<p> <code></p>
<dt>&bull; Mem and Swap meter panels</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 1,2</i></p>
<dd> Toggle display of label and memory or swap capacity scrolling display.</dl>
</dl>
<p> <code></p>
<dt>&bull; Mailbox monitor message count button</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 1</i></p>
<dd> Launch a mail reader program. If options permit, also stop animations and reset remote message counts.</p>
<dt><i>Btn 2</i></p>
<dd> Toggle mail check mute mode which inhibits the sound notify program, and optionally inhibits all mail checking.</dl>
</dl>
<p> <code></p>
<dt>&bull; Mailbox monitor envelope decal</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 1</i></p>
<dd> Force a mail check regardless of mute or timeout state.</dl>
</dl>
<p> <code></p>
<dt>&bull; Battery monitor panel</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>Btn 1</i></p>
<dd> On the charging state decal toggles battery minutes left, percent level, and charge rate display.</p>
<dt><i>Btn 2</i></p>
<dd> Anywhere on the panel also toggles the display.</dl>
</dl>
<p> <code></p>
<dt>&bull; Keyboard shortcuts</p>
<dd> </code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>F1</i></p>
<dd> popup the user config window.</p>
<dt><i>F2</i></p>
<dd> popup the main menu.</p>
<dt><i>Page_Up</i></p>
<dd> previous theme or theme alternative.</p>
<dt><i>Page_Down</i></p>
<dd> next theme or theme alternative.</p>
<dt><i>&lt;Ctl&gt;Page_Up</i></p>
<dd> previous theme, skipping any theme alternatives.</p>
<dt><i>&lt;Ctl&gt;Page_Down</i></p>
<dd> next theme, skipping any theme alternatives.</dl>
</dl>
</dl>
<p> If a command has been configured to be launched for a monitor, then a button will appear when the mouse enters the panel of that monitor. Clicking the button will launch the command. </p>
<p> A right button mouse click on the side or top frames of the <code>gkrellm</code> window will pop up a user configuration window where you can configure all the builtin and plugin monitors. Chart appearance may be configured by right clicking on a chart, and right clicking on many panels will open the configuration window directly to the corresponding monitor&#8217;s configuration page. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Displays this manual page.</p>
<dt><code>-t, &#8211;theme dir</code></p>
<dd> <code>gkrellm</code> will load all theme image files it finds in <i>dir</i> and parse the <i>gkrellmrc</i> file if one exists. This option overrides the loading of the last theme you configured to be loaded in the Themes configuration window. Theme changes are not saved when <code>gkrellm</code> is run with this option.</p>
<dt><code>-g, &#8211;geometry +x+y</code></p>
<dd> Makes <code>gkrellm</code> move to an <i>(x,y)</i> position on the screen at startup. Standard X window geometry position (not size) formats are parsed, ie +x+y -x+y +x-y -x-y. Except, negative geometry positions are not recognized (ie +-x&#8211;y ).</p>
<dt><code>-wm</code></p>
<dd> Forces <code>gkrellm</code> to start up with window manager decorations. The default is no decorations because there are themed borders.</p>
<dt><code>-w, &#8211;withdrawn</code></p>
<dd> <code>gkrellm</code> starts up in withdrawn mode so it can go into the Blackbox slit (and maybe WindowMaker dock).</p>
<dt><code>-c, &#8211;config suffix</code></p>
<dd> Use alternate config files generated by appending <i>suffix</i> to config file names. This overrides any previous host config which may have been setup with the below option.</p>
<dt><code>-f, &#8211;force-host-config</code></p>
<dd> If <code>gkrellm</code> is run once with this option and then the configuration or theme is changed, the config files that are written will have a <i>-hostname</i> appended to them. Subsequent runs will detect the <i>user-config-hostname</i> and <i>gkrellm_theme.cfg-hostname</i> files and use them instead of the normal configuration files (unless the <code>&#8211;config</code> option is specified). This is a convenience for allowing remote <code>gkrellm</code> independent config files in a shared home directory, and for the hostname to show up in the X title for window management. This option has no effect in client mode.</p>
<dt><code>-s, &#8211;server hostname</code></p>
<dd> Run in client mode by connecting to and collecting data from a <code>gkrellmd</code> server on <i>hostname</i></p>
<dt><code>-P, &#8211;port server_port</code></p>
<dd> Use <i>server_port</i> for the <code>gkrellmd</code> server connection.</p>
<dt><code>-l, &#8211;logfile path</code></p>
<dd> Enable sending error and debugging messages to a log file.</p>
<dt><code>-nc</code></p>
<dd> No config mode. The config menu is blocked so no config changes can be made. Useful in certain environments, or maybe for running on a <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1) login screen or during a screensaver mode?</p>
<dt><code>-demo</code></p>
<dd> Force enabling of many monitors so themers can see everything. All config saving is inhibited.</p>
<dt><code>-p, &#8211;plugin plugin.so</code></p>
<dd> For plugin development, load the command line specified plugin so you can avoid repeated install steps in the development cycle. </p>
</dl>
<h2>BUILTIN MONITORS</h2>
<h3>Charts</h3>
<p> The default for most charts is to automatically adjust the number of grid lines drawn and the resolution per grid so drawn data will be nicely visible. You may change this to fixed grids of 1-5 and/or fixed grid resolutions in the chart configuration windows. However, some combination of the auto scaling modes may give best results. </p>
<p> Auto grid resolution has the following behavior. </p>
<p> <code>Auto mode sticks at peak value</code> is not set:</p>
<dl>
<dt>
<dd> 1) If using auto number of grids, set the resolution per grid and the number of grids to optimize the visibility of data drawn on the chart. Try to keep the number of grids between 1 and 7.</p>
<dt>
<dd> 2) If using a fixed number of grids, set the resolution per grid to the smallest value that draws data without clipping.</dl>
<p> <code>Auto mode sticks at peak value</code> is set:</p>
<dl>
<dt>
<dd> 1) If using auto number of grids, set the resolution per grid such that drawing the peak value encountered would require at least 5 grids.</p>
<dt>
<dd> 2) If using a fixed number of grids, set the resolution per grid such that the peak value encountered could be drawn without clipping. This means the resolution per grid never decreases.</dl>
<p> All resolution per grid values are constrained to a set of values in either a 1, 2, 5 sequence or a 1, 1.5, 2, 3, 5, 7 sequence. If you set <code>Auto mode sticks at peak value</code> a manual <code>Auto mode recalibrate</code> may occasionally be required if the chart data has a wide dynamic range. </p>
<h3>CPU Monitor</h3>
<p> Data is plotted as a percentage. In auto number of grids mode, resolution is a fixed 20% per grid. In fixed number of grids mode, grid resolution is 100% divided by the number of grids. </p>
<h3>Proc Monitor</h3>
<p> The krell shows process forks with a full scale value of 10 forks. The chart has a resolution of 10 forks/sec per grid in auto number of grids mode and 50 forks/second maximum on the chart in fixed number of grids mode. The process load resolution per grid is best left at 1.0 for auto number of grids, but can be set as high as 5 if you configure the chart to have only 1 or 2 fixed grids. </p>
<h3>Net Monitor</h3>
<p> <code>gkrellm</code> is designed to display a chart for net interfaces which are up, which means they are listed in the routing table (however, it is possible in some cases to monitor unrouted interfaces). One net interface may be linked to a timer button which can be used to connect and disconnect from an ISP. </p>
<p> The timer button shows an off, standby, or on state by a distinctive (color or shape) icon.</p>
<dl>
<dt>ppp</p>
<dd> Standby state is while the modem phone line is locked while ppp is connecting, and the on state is the ppp link connected. The phone line lock is determined by the existence of the modem lock file <i>/var/lock/LCK..modem,</i> which assumes pppd is using <i>/dev/modem.</i> However, if your pppd setup does not use <i>/dev/modem,</i> then you can configure an alternative with:</dl>
<dl>
<dt>
<dd>
<pre>
ln  -s  /var/lock/LCK..ttySx   ~/.gkrellm2/LCK..modem
</pre>
</dl>
<dl>
<dt>
<dd> where ttySx is the tty device your modem does use. The ppp on state is detected by the existence of <i>/var/run/pppX.pid</i> and the time stamp of this file is the base for the on line time.</p>
<dt>ippp</p>
<dd> The timer button standby state is not applicable to ISDN interfaces that are always routed. The on state is ISDN on line while the ippp interface is routed. The on line timer is reset at transitions from ISDN hangup state to on line state.</dl>
<p> For both ppp and ippp timer button links, the panel area of the interface is always shown and the chart appears when the interface is routed with the phone link connected or on line. </p>
<p> If the timer button is not linked to a net interface, then it can be used as a push on / push off timer </p>
<p> Net monitors can have a label so that the interface can be associated with the identity of the other end of the connection. This is useful if you have several net connections or run multiple remote <code>gkrellm</code> programs. It can be easier to keep track of who is connected to who. </p>
<h3>Mem and Swap Monitor</h3>
<p> Here you are reading a ratio of total used to total available. The amount of memory used indicated by the memory monitor is actually a calculated &quot;used&quot; memory. If you enter the &quot;free&quot; command, you will see that most of your memory is almost always used because the kernel uses large amounts for buffers and cache. Since the kernel can free a lot of this memory as user process demand for memory goes up, a more realistic reading of memory in use is obtained by subtracting the buffers and cached memory from the kernel reported used. This is shown in the free command output in the &quot;-/+ buffers/cache&quot; line where a calculated used amount has buffers and cached memory subtracted from the kernel reported used memory, and a calculated free amount has the buffers and cached memory added in. </p>
<p> While the memory meter always shows the calculated &quot;used&quot; memory, the raw memory values total, shared, buffered, and cached may be optionally displayed in the memory panel by entering an appropriate format display string in the config. </p>
<p> Units: All memory values have units of binary megabytes (MiB). Memory sizes have historically been reported in these units because memory arrays on silicon have always increased in size by multiples of 2. Add an address line to a memory chip and you double or quadruple (a multiplexed address) the memory size. A binary megabyte is 2^20 or 1048576. Contrast this with units for other stats such as disk capacities or net transfer rates where the proper units are decimal megabytes or kilobytes. Disk drive capacities do not increase by powers of 2 and manufacturers do not use binary units when reporting their sizes. However, some of you may prefer to see a binary disk drive capacity reported, so it is available as an option. </p>
<h3>Internet Monitor</h3>
<p> Displays TCP port connections and records historical port hits on a minute or hourly chart. Middle button click on an inet chart to toggle between the minute and hourly displays. There is a strip below the minute or hour charts where marks are drawn for port hits in second intervals. Each inet krell also shows port hits with a full scale range of 5 hits. The left button toggle of extra info displays current port connections. </p>
<p> For each internet monitor you can specify two labeled datasets with one or two ports for each dataset. There are two ports because some internet ports are related and you might want to group them &#8211; for example, the standard HTTP port is 80, but there is also a www web caching service on port 8080. So it makes sense to have a HTTP monitor which combines data from both ports. A possible common configuration would be to create one inet monitor that monitors HTTP hits plotted in one color and FTP hits in another. To do this, setup in the Internet configuration tab: </p>
<dl>
<dt>
<dd>
<pre>
HTTP  80 8080    FTP  21
</pre>
</dl>
<p> Or you could create separate monitors for HTTP and FTP. Other monitors might be SMTP on port 25 or NNTP on port 119. </p>
<p> If you check the &quot;Port0 &#8211; Port1 is a range&quot; button, then all of the ports between the two entries will be monitored. Clicking the small button on the Inet panels will pop up a window listing the currently connected port numbers and the host that is connected to it. </p>
<p> <code>gkrellm</code> samples TCP port activity once per second, so it is possible for port hits lasting less than a second to be missed. </p>
<h3>File System Monitor</h3>
<p> File system mount points can be selected to be monitored with a meter that shows the ratio of blocks used to total blocks available. Mounting commands can be enabled for mount points in one of two ways: </p>
<p> If a mount point is in your <i>/etc/fstab</i> and you have mount permission then <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) and <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) commands can be enabled and executed for that mount point simply by checking the &quot;Enable /etc/fstab mounting&quot; option. Mount table entries in <i>/etc/fstab</i> must have the &quot;user&quot; or &quot;owner&quot; option set to grant this permission unless <code>gkrellm</code> is run as root. For example, if you run <code>gkrellm</code> as a normal user and you want to be able to mount your floppy, your <i>/etc/fstab</i> could have either of: </p>
<dl>
<dt>
<dd>
<pre>
/dev/fd0 /mnt/floppy  ext2 user,noauto,rw,exec  0  0
/dev/fd0 /mnt/floppy  ext2 user,defaults  0  0
</pre>
</dl>
<p> If <code>gkrellm</code> is run as root or if you have <code><a href="/docs/linux/man/1-sudo/">sudo</a></code>(1) permission to run the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) commands, then a custom mount command can be entered into the &quot;mount command&quot; entry box. A <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command must also be entered if you choose this method. Example mount and umount entries using sudo: </p>
<dl>
<dt>
<dd>
<pre>
sudo /bin/mount -t msdos /dev/fd0 /mnt/A
sudo /bin/umount /mnt/A
</pre>
</dl>
<p> Notes: the mount point specified in a custom mount command (/mnt/A in this example) must be the same as entered in the &quot;Mount Point&quot; entry. Also, you should have the NOPASSWD option set in <i>/etc/sudoers</i> for this. </p>
<p> File system monitors can be created as primary (always visible) or secondary which can be hidden and then shown when they are of interest. For example, you might make primary file system monitors for root, home, or user so they will be always visible, but make secondary monitors for less frequently used mount points such as floppy, zip, backup partitions, foreign file system types, etc. Secondary FS monitors can also be configured to always be visible if they are mounted by checking the &quot;Show if mounted&quot; option. Using this feature you can show the secondary group, mount a file system, and have that FS monitor remain visible even when the secondary group is hidden. A standard cdrom mount will show as 100% full but a monitor for it could be created with mounting enabled just to have the mount/umount convenience. </p>
<p> When the &quot;Ejectable&quot; option is selected for a file system, an eject button will appear when the mouse enters the file system panel. If you are not using /etc/fstab mounting, a device file to eject will also need to be entered. Systems may have varying levels of support for this feature ranging from none or basic using an ioctl() to full support using an eject command to eject all its supported devices. Linux and NetBSD use the &quot;eject&quot; command while FreeBSD uses the &quot;cdcontrol&quot; command, so be sure these commands are installed. Most eject commands will also support closing a CDROM tray. If they do, you will be able to access this function by right clicking the eject button. </p>
<h3>Mail Monitor</h3>
<p> Checks your mailboxes for unread mail. A mail reading program (MUA) can be executed with a left mouse click on the mail monitor panel button, and a mail notify (play a sound) program such as esdplay or artsplay can be executed whenever the new mail count increases. The mail panel envelope decal may also be clicked to force an immediate mail check at any time. </p>
<p> <code>gkrellm</code> is capable of checking mail from local mailbox types mbox, MH, and maildir, and from remote mailbox types POP3 and IMAP. </p>
<p> POP3 and IMAP checking can use non-standard port numbers and password authentication protocols APOP (for POP3 only) or CRAM-MD5. If supported by the mail server, emote checking may be done over an SSL connection if the &quot;Use SSL&quot; option is selected. </p>
<p> Before internal POP3 and IMAP checking was added, an external mail fetch/check program could be set up to be executed periodically to download or check remote POP3 or IMAP mail. This method is still available and must be used if you want <code>gkrellm</code> to be able to download remote mail to local mailboxes because the builtin checking functions cannot download. </p>
<h3>Battery Monitor</h3>
<p> This meter will be available if a battery exists and will show battery percentage life remaining. A decal indicates if AC line is connected or if the battery is in use. If the data is available, time remaining may be displayed as well as the percentage battery level. If the time remaining is not available or is inaccurate, the Estimate Time option may be selected to display a battery time to run or time to charge which is calculated based on the current battery percent level, user supplied typical battery times, and a default linear extrapolation model. For charging, an exponential charge model may be selected. </p>
<p> A battery low level warning and alarm alert may be set. If battery time is not available from the OS and the estimate time mode is not set, the alert units will be battery percent level. Otherwise the alert units will be battery time left in minutes. If OS battery time is not available and the estimate time mode is set when the alert is created, the alert will have units of time left in minutes and the alert will automatically be destroyed if the estimate time option is subsequently turned off. </p>
<p> If the OS reports multiple batteries, the alert will be a master alert which is duplicated for each battery. </p>
<h3>CPU/Motherboard Sensors &#8211; Temperature, Voltages, and Fan RPM</h3>
<p> <code>Linux:</code><br />
 Sensor monitoring on Linux requires that either lm_sensors modules are installed in your running kernel, that you run a kernel &gt;= 2.6 with sysfs sensors configured, or, for i386 architectures, that you have the mbmon daemon running when <code>gkrellm</code> is started (as long as mbmon supports reporting sensor values for your motherboard). </p>
<p> For lm_sensors to be used, <code>gkrellm</code> must be compiled with libsensors support. It will be if the libsensors development package is installed when <code>gkrellm</code> is compiled. Using libsensors is the preferred interface on Linux since it is the only interface that will be up to date on supporting correct voltage scaling factors and offsets for recent sensor chips. </p>
<p> If the mbmon daemon is used, it must be started before <code>gkrellm</code> like so: </p>
<dl>
<dt>
<dd>
<pre>
mbmon -r -P port-number
</pre>
</dl>
<p> where the given &quot;port-number&quot; must be configured to match in the <code>gkrellm</code> Sensors-&gt;Options config. If you have mbmon installed from a distribution package, you can probably easily set up for mbmon to be started at boot. With Debian, for example, you would edit the file /etc/default/mbmon to set: </p>
<dl>
<dt>
<dd>
<pre>
START_MBMON=1
</pre>
</dl>
<p> and you would need to set in the <code>gkrellm</code> Sensors-&gt;Option config the mbmon port to be &quot;411&quot; to match the default in the /etc/default/mbmon file. </p>
<p> Sensor temperatures can also be read from /proc/acpi/thermal_zone, /proc/acpi/thermal, /proc/acpi/ibm, the PowerMac Windfarm /sysfs interface, and PowerMac PMU /sysfs based sensors. </p>
<p> When using lm_sensors, libsensors will be used if available, but if libsensors is not linked into the program, the sensor data will be read directly from the /sysfs or /proc file systems. If running a newer Linux kernel sensor module not yet supported by libsensors and libsensors is linked, there will also be an automatic fallback to using /sysfs as long as libsensors doesn&#8217;t detect any sensors. But if it does detect some sensors which does not include the new sensors you need, you can force getting /sysfs sensor data either by running: </p>
<dl>
<dt>
<dd>
<pre>
gkrellm --without-libsensors
</pre>
</dl>
<p> or by rebuilding with: </p>
<dl>
<dt>
<dd>
<pre>
make without-libsensors=yes
</pre>
</dl>
<p> Disk temperatures may also be monitored if you have the hddtemp daemon running when <code>gkrellm</code> is started. <code>gkrellm</code> uses the default hddtemp port of 7634. Like mbmon, hddtemp is best started in a boot script to guarantee it will be running when <code>gkrellm</code> is started. </p>
<p> NVIDIA graphics card GPU temperatures may also be monitored if the nvidia-settings command is installed and your Nvidia card supports the temperature reporting. If nvidia-settings is not installed or does not report temperatures for your card, an option for using the nvclock program will appear in the Sensors config. Nvclock use is not automatically enabled as is nvidia-settings because nvclock can add seconds of <code>gkrellm</code> startup time when used on a NVIDIA GPU chipset it does not support. GKrellM must be restarted to recognize changes for the nvclock option. </p>
<p> <code>Windows:</code><br />
 Requires a MBM install: <i><a rel="nofollow" href="http://mbm.livewiredev.com/.">http://mbm.livewiredev.com/.</a></i> </p>
<p> <code>FreeBSD:</code><br />
 Builtin sensor reporting is available for some sensor chips. FreeBSD systems can also read sensor data from the mbmon daemon as described in the Linux section above. </p>
<p> <code>NetBSD:</code><br />
 Builtin sensor reporting is available for some sensor chips. NetBSD uses the <a href="/docs/linux/man/4-envsys/">envsys</a>(4) interface and sensors reading is automatically enabled if you have either a <a href="/docs/linux/man/4-lm/">lm</a>(4) or <a href="/docs/linux/man/4-viaenv/">viaenv</a>(4) chip configured in your kernel. </p>
<p> <code>General Setup:</code><br />
 Temperature and fan sensor displays may be optionally located on the CPU or Proc panels to save some vertical space while voltages are always displayed on their own panel. If you set up to monitor both a temperature and a fan on a single CPU or Proc panel, they can be displayed optionally as an alternating single display or as separate displays. If separate, the fan display will replace the panel label. The configuration for this is under the CPU and Proc config pages. </p>
<p> If not using libsensors, in the Setup page for the Sensors config enter any correction factors and offsets for each of the sensors you are monitoring (see below and lm_sensor documentation). For Linux, default values are automatically provided for many sensor chips. </p>
<p> But if using libsenors, it is not possible to enter correction factors and offsets on the Sensors config page because libsensors configuration is done in the /etc/sensors.conf file. To get sensor debug output and to find out the sensor data source, run: </p>
<dl>
<dt>
<dd>
<pre>
gkrellm -d 0x80
</pre>
</dl>
<pre>
Note for NetBSD users:
</pre>
<dl>
<dt>
<dd> The current implementation of the sensor reading under NetBSD opens /dev/sysmon and never closes it. Since that device does not support concurrent accesses, you won&#8217;t be able to run other apps such as <a href="/docs/linux/man/8-envstat/">envstat</a>(8) while GKrellM is running. This might change if this happens to be an issue. </p>
<p> The reasons for this choice are a) efficiency (though it might be possible to open/close /dev/sysmon each time a reading is needed without major performance issue) and b) as of October 2001, there&#8217;s a bug in the <a href="/docs/linux/man/4-envsys/">envsys</a>(4) driver which sometimes causes deadlocks when processes try to access simultaneously /dev/sysmon (see NetBSD PR#14368). A (quick and dirty) workaround for this is to monopolize the driver :)</dl>
<h3>CPU/Motherboard Temperatures</h3>
<p> Most modern motherboards will not require setting temperature correction factors and offsets other than the defaults. However, for lm_sensors it is necessary to have a correct &quot;set sensor&quot; line in <i>/etc/sensors.conf</i> if the temperature sensor type is other than the default thermistor. If using Linux sysfs sensors, this sensor type would be set by writing to a sysfs file. For example, you might at boot set a sysfs temperature sensor type with: </p>
<dl>
<dt>
<dd>
<pre>
echo &quot;2&quot; &gt; /sys/bus/i2c/devices/0-0290/sensor2
</pre>
</dl>
<p> On the other hand, some older motherboards may need temperature calibration by setting a correction factor and offset for each temperature sensor because of factors such as variations in physical thermistor contact with the CPU. Unfortunately, this calibration may not be practical or physically possible because it requires that somehow you can get a real CPU temperature reading. So, the calibration discussion which follows should probably be considered an academic exercise that might give you some good (or bad) ideas. If you have a recent motherboard, skip the following. </p>
<p> Anyway, to do this calibration, take two real CPU temperature readings corresponding to two sensor reported readings. To get the real readings, you can trust that your motherboard manufacturer has done this calibration and is reporting accurate temperatures in the bios, or you can put a temperature probe directly on your CPU case (and this is where things get impractical). </p>
<p> Here is a hypothetical CPU calibration procedure. Make sure <code>gkrellm</code> is configured with default factors of 1.0 and offsets of 0 and is reporting temperatures in centigrade: </p>
<dl>
<dt>1 &bull;</p>
<dd> Power on the machine and read a real temperature T1 from the bios or a temperature probe. If reading from the bios, proceed with booting the OS. Now record a sensor temperature S1 as reported by <code>gkrellm.</code></p>
<dt>2 &bull;</p>
<dd> Change the room temperature environment (turn off your AC or change computer fan exhaust speed). Now repeat step 1, this time recording a real temperature T2 and <code>gkrellm</code> reported sensor temperature S2.</p>
<dt>3 &bull;</p>
<dd> Now you can calculate the correction factor and offset you need to enter into the Sensor configuration tab:</dl>
<dl>
<dt>
<dd>
<pre><code>
From : s - S1 t - T1-- -- -- = -- -- --S2 - S1 T2 - T1 T2 - T1 S2 *T1 - S1 *T2 t = s *-- -- -- -+-- -- -- -- -- -- -S2 - S1 S2 - S1 So : T2 - T1 S2 *T1 - S1 *T2 factor = -- -- -- -offset = -- -- -- -- -- -- -S2 - S1 S2 - S1
</code></pre>
</dl>
<h3>Voltage Sensor Corrections</h3>
<p> You need to read this section only if you think the default voltage correction factors and offsets are incorrect. For Linux and lm_sensors and sysfs sensors<br />
&nbsp;<wbr>this would be if <code>gkrellm</code> does not know about your particular sensor chip. For MBM with Windows, the default values should be correct. </p>
<p> Motherboard voltage measurements are made by a variety of sensor chips which are capable of measuring a small positive voltage. GKrellM can display these voltage values and can apply a correction factor, offset, and for the negative voltages of some chips (lm80), a level shifting reference voltage to the displayed voltage. There are four cases to consider: </p>
<dl>
<dt>1 &bull;</p>
<dd> Low valued positive voltages may be directly connected to the input pins of the sensor chip and therefore need no correction. For these, the correction factor should be 1.0 and the offset should be 0.</p>
<dt>2 &bull;</p>
<dd> Higher valued positive voltages will be connected to the input pins of the sensor chip through a 2 resistor attenuation circuit. For these, the correction factor will be a ratio of the resistor values and the offset will be 0.</p>
<dt>3 &bull;</p>
<dd> Negative voltages will be connected to the input pins of the sensor through a 2 resistor attenuation circuit with one of the resistors connected to a positive voltage to effect a voltage level shift. For these (lm80), the correction factor and offset will be ratios of the resistor values, and a reference voltage must be used.</p>
<dt>4 &bull;</p>
<dd> Some sensor chips (w83782, lm78) are designed to handle negative inputs without requiring an input resistor connected to a voltage reference. For these, there will be a correction factor and a possible offset.</dl>
<dl>
<dt>
<dd>
For cases 2 and 3, the sensor chip input network looks like : Vs o&#8211; &#8212; /\/\/ &#8212; -o&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; -o Vin R1 |<br />
                       o&#8211; /\/\/ &#8211;o Vref R2
</dl>
<dl>
<dt>where,</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><i>Vs</i></p>
<dd> is the motherboard voltage under measurement</p>
<dt><i>Vin</i></p>
<dd> is the voltage at the input pin of the sensor chip and therefore is the voltage reading that will need correction.</p>
<dt><i>Vref</i></p>
<dd> is a level shifting voltage reference. For case 2, Vref is ground or zero. For case 3, Vref will be one of the positive motherboard voltages.</dl>
</dl>
</dl>
<p> The problem then is to compute correction factors and offsets as a function of R1 and R2 so that GKrellM can display a computed motherboard voltage Vs as a function of a measured voltage Vin. </p>
<p> Since sensor chip input pins are high impedance, current into the pins may be assumed to be zero. In that case, the current through R1 equals current through R2, and we have: </p>
<dl>
<dt>
<dd>
<pre>
    (Vs - Vin)/R1 = (Vin - Vref)/R2
Solving for Vs as a function of Vin:
    Vs = Vin * (1 + R1/R2)  -  (R1/R2) * Vref
So, the correction factor is:  1 + R1/R2
    the correction offset is:  - (R1/R2)
    Vref is specified in the config separately from
    the offset (for chips that need it).
</pre>
</dl>
<p> Fortunately there seems to be a standard set of resistor values used for the various sensor chips which are documented in the lm_sensor documentation. The GKrellM sensor corrections are similar to the compute lines you find with lm_sensors, with the difference that lm_sensors has an expression evaluator which does not require that compute lines be simplified to the single factor and offset required by GKrellM. But you can easily calculate the factor and offset. For example, this lm_sensor compute line for a case 2 voltage: </p>
<dl>
<dt>
<dd>
<pre>
    compute in3 ((6.8/10)+1)*@ ,  @/((6.8/10)+1)
</pre>
</dl>
<p> yields a correction factor of ((6.8/10)+1) = 1.68 and an offset of zero. </p>
<p> Note that the second compute line expression is not relevant in GKrellM because there is never any need to invert the voltage reading calculation. Also, the compute line &#8216;@&#8217; symbol represents the Vin voltage. </p>
<p> A more complicated compute line for a case 3 voltage: </p>
<dl>
<dt>
<dd>
<pre>
    compute in5 (160/35.7)*(@ - in0) + @, ...
can be rewritten:
    compute in5 (1 + 160/35.7)*@ - (160/35.7)*in0, ...
so the correction factor is  (1 + 160/35.7) = 5.48
and the correction offset is -(160/35.7) = -4.48
and the voltage reference Vref is in0
</pre>
</dl>
<p> Here is a table of correction factors and offsets based on some typical compute line entries from /etc/sensors.conf: </p>
<dl>
<dt>
<dd>
<pre><code>
Compute line Factor Offset Vref-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -lm80 in0(24 / 14.7 + 1) * @2.633 0 -
    in2(22.1 / 30 + 1) * @1.737 0 -
    in3(2.8 / 1.9) * @1.474 0 -
    in4(160 / 30.1 + 1) * @6.316 0 -
    in5(160 / 35.7) * (@-in0) + @5.482 - 4.482 in0 in6(36 / 16.2) * (@-in0) + @3.222 - 2.222 in0 LM78 in3((6.8 / 10) + 1) * @1.68 0 -
    in4((28 / 10) + 1) * @3.8 0 -
    in5 - (210 / 60.4) * @-3.477 0 -
    in6 - (90.9 / 60.4) * @-1.505 0 -
    w83782 in5(5.14 * @) - 14.91 5.14 - 14.91 -
    in6(3.14 * @) - 7.71 3.14 - 7.71 -
</code></pre>
</dl>
<h3>Command launching</h3>
<p> Many monitors can be set up to launch a command when you click on the monitor label. When a command is configured for a monitor, its label is converted into a button which becomes visible when the mouse enters the panel or meter area of the label. If the command is a console command (doesn&#8217;t have a graphical user interface), then the command must be run in a terminal window such as xterm, eterm, or Gnome terminal. For example running the &quot;top&quot; command would take:</p>
<dl>
<dt>xterm -e top</p>
<dd></dl>
<p> You can use the command launching feature to run commands related to monitoring functions, or you may use it to have a convenient launch for any command. Since <code>gkrellm</code> is usually made sticky, you can have easy access to several frequently used commands from any desktop. This is intended to be a convenience and a way to maximize utilization of screen real estate and not a replacement for more full featured command launching from desktops such as Gnome or KDE or others. Some launch ideas for some monitors could be:</p>
<dl>
<dt><i>calendar:</i></p>
<dd> gnomecal, evolution, or ical</p>
<dt><i>CPU:</i></p>
<dd> xterm -e top or gps or gtop</p>
<dt><i>inet:</i></p>
<dd> gftp or xterm -e ftpwho</p>
<dt><i>net:</i></p>
<dd> mozilla, galeon, skipstone, or xterm -e slrn -C-</dl>
<p> And so on&#8230; Tooltips can be set up for these commands. </p>
<h3>Alerts</h3>
<p> Most monitors can have alerts configured to give warnings and alarms for data readings which range outside of configurable limits. Where useful, a delay of the alert trigger can be configured. A warning or alarm consists of an attention grabbing decal appearing and an optional command being executed. For most monitors the command may contain the same substitution variables which are available for display in the chart or panel label format strings and are documented on configuration Info pages. Additionally, the hostname may be embedded in the command with the $H substitution variable. </p>
<p> If you have festival installed, either a warn or alarm command could be configured to speak something. For example a CPU temperature alert warn command could just speak the current temperature with: </p>
<pre>
    sh -c &quot;echo warning C P U is at $s degrees | esddsp festival --tts&quot;
</pre>
<p> Assuming you have esd running. </p>
<h2>THEMES</h2>
<p> A theme is a directory containing image files and a <i>gkrellmrc</i> configuration file. The theme directory may be installed in several locations: </p>
<dl>
<dt>
<dd>
<pre>
~/.gkrellm2/themes
/usr/local/share/gkrellm2/themes
/usr/share/gkrellm2/themes
</pre>
</dl>
<p> For compatibility with Gtk themes, a <code>gkrellm</code> theme may also be installed as: </p>
<dl>
<dt>
<dd>
<pre>
~/.themes/THEME_NAME/gkrellm2
/usr/share/themes/THEME_NAME/gkrellm2
</pre>
</dl>
<p> Finally, a theme you simply want to check out can be untarred anywhere and used by running: </p>
<dl>
<dt>
<dd>
<pre>
gkrellm -t path_to_theme
</pre>
</dl>
<p> If you are interested in writing a theme, go to the Themes page at <i><a rel="nofollow" href="http://www.gkrellm.net">http://www.gkrellm.net</a></i> and there you will find a Theme making reference. </p>
<h2>PLUGINS</h2>
<p> <code>gkrellm</code> tries to load all plugins (shared object files ending in .so) it finds in your plugin directory <i>~/.gkrellm2/plugins.</i> The directories <i>/usr/local/lib64/gkrellm2/plugins</i> and <i>/usr/lib64/gkrellm2/plugins</i> are also searched for plugins to install. </p>
<p> Some plugins may be available only as source files and they will have to be compiled before installation. There should be instructions for doing this with each plugin that comes in source form. </p>
<p> If you are interested in writing a plugin, go to the Plugins page at <i><a rel="nofollow" href="http://www.gkrellm.net">http://www.gkrellm.net</a></i> and there you will find a Plugin programmers reference. </p>
<h2>CLIENT/SERVER</h2>
<p> When a local <code>gkrellm</code> runs in client mode and connects to a remote <code>gkrellmd</code> server all builtin monitors collect their data from the server. However, the client <code>gkrellm</code> process is running on the local machine, so any enabled plugins will run in the local context (Flynn is an exception to this since it derives its data from the builtin CPU monitor). Also, any command launching will run commands on the local machine. </p>
<h2>FILES</h2>
<dl>
<dt><i>~/.gkrellm2</i></p>
<dd> User gkrellm directory where are located configuration files, user&#8217;s plugins and user&#8217;s themes.</p>
<dt><i>~/.gkrellm2/plugins</i></p>
<dd> User plugin directory.</p>
<dt><i>/usr/lib64/gkrellm2/plugins</i></p>
<dd> System wide plugin directory.</p>
<dt><i>/usr/local/lib64/gkrellm2/plugins</i></p>
<dd> Local plugin directory.</p>
<dt><i>~/.gkrellm2/themes</i></p>
<dd> User theme directory.</p>
<dt><i>~/.themes/THEME_NAME/gkrellm2</i></p>
<dd> User theme packaged as part of a user Gtk theme.</p>
<dt><i>/usr/share/gkrellm2/themes</i></p>
<dd> System wide theme directory.</p>
<dt><i>/usr/local/share/gkrellm2/themes</i></p>
<dd> Local theme directory.</p>
<dt><i>/usr/share/themes/THEME_NAME/gkrellm2</i></p>
<dd> System wide theme packaged as part of a system wide Gtk theme. </p>
</dl>
<h2>AUTHORS</h2>
<p> This manual page was written by Bill Wilson &lt;billw [at] gkrellm.net&gt;. <a rel="nofollow" href="http://www.gkrellm.net/">http://www.gkrellm.net/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/1-sudo/">sudo</a></code>(1), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) </p>
<h2>Index</h2>
