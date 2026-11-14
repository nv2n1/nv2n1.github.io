---
title: "inxi(8)"
name: "inxi"
section: "8"
letter: "i"
url: "/docs/linux/man/8-inxi/"
description: "inxi – Info script for console and IRC."
---

<p>inxi &#8211; Info script for console and IRC. </p>
<h2>Synopsis</h2>
<p><code>inxi</code> <code>inxi </code>[<code>-AbCdDfFGhHiIlMnNopPrsSu</code>] [<code>-c NUMBER</code>] [<code>-v NUMBER</code>] <code>inxi </code>[<code>-t </code>(<code>c</code> or<code> m</code> or<code> cm</code> or<code> cm NUMBER</code>)] [<code>-x LETTER</code>(<code>s</code>)] [<code>-xx LETTER</code>] <code>inxi </code>[<code>&#8211;help</code>] [<code>&#8211;recommends</code>] [<code>&#8211;version</code>] [<code>-@ NUMBER</code>] </p>
<h2>Description</h2>
<p><code>inxi</code> forum posts as well &#8211; for the same reason. It is is a fork of locsmif&#8217;s largely unmaintained yet very clever, infobash script. inxi is co-developed, a group project, primarily with trash80 on the programming side. But the nice people at irc.oftc.net channel #linux-smokers-club all really have to be considered to be co-developers because of their non-stop enthusiasm and willingness to provide real time testing and debugging of inxi development. Without a wide range of diverse Linux kernel based Free Desktop systems to test on, we could never have gotten inxi to be as reliable and solid as it&#8217;s turning out to be. And of course, locsmif, who figured out a lot of the core methods, logic, and tricks used in inxi, has to be considered as a primary author as well, even if inxi has been officially forked from his infobash script. </p>
<h2>Notes For All Users For The Options Section</h2>
<p>Options can be combined if they do not conflict. Either group the letters together or separate them. </p>
<p> Letters with numbers can have no gap or a gap at your discretion unless using <code> -t </p>
<p> eg </code><i>inxi -AG </i>or<i> inxi -A -G </i>or<i> inxi -c10</i></p>
<h2>Options</h2>
<dl>
<dt><code>-A </code></p>
<dd>Show Audio/sound card information.</p>
<dt><code>-b </code></p>
<dd>Shows basic output, short form (previously -d). Same as: inxi -v 2</p>
<dt><code>-c </code>[<code>0</code>&#8211;<code>32</code>]</p>
<dd>Available color schemes. Scheme number is required.<br />
&nbsp;<wbr>&nbsp;<wbr> Supported color schemes: 0-32. </p>
<dt><code>-c </code>[<code>94</code>&#8211;<code>99</code>]</p>
<dd>Color selectors run a color selector option prior to inxi starting which lets you set the config file value for the selection. </p>
<p> Color selectors for each type display </p>
<p> (NOTE: irc and global only show safe color set):</p>
<dt><code> -c 94 </code> Console, out of X</p>
<dd>
<dt><code> -c 95 </code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Terminal, running in X &#8211; like xTerm</p>
<dd>
<dt><code> -c 96 </code> Gui IRC, running in X &#8211; like Xchat, Quassel,</p>
<dd>Konversation etc.</p>
<dt><code> -c 97 </code><tt>&nbsp;<wbr></tt>Console IRC running in X &#8211; like irssi in xTerm</p>
<dd>
<dt><code> -c 98 </code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Console IRC not in X</p>
<dd>
<dt><code> -c 99 </code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Global &#8211; Overrides/removes all settings.</p>
<dd>Setting specific removes global. </p>
<dt><code>-C </code></p>
<dd>Show full CPU output, including per CPU clockspeed.</p>
<dt><code>-d </code></p>
<dd>Shows optical drive data. Same as -Dd. With -x, adds features line to output. -xx adds a few more features.</p>
<dt><code>-D </code></p>
<dd>Show full hard Disk info, not only model, ie: /dev/sda ST380817AS 80.0GB.</p>
<dt><code>-f </code></p>
<dd>Show all cpu flags used, not just the short list. Not shown with -F to avoid spamming.</p>
<dt><code>-F </code></p>
<dd>Show Full output for inxi. Includes all Upper Case line letters, plus -s and -n. Does not show extra verbose options like -x -d -f -u -l -o -p -t -r unless you use that argument.</p>
<dt><code>-G </code></p>
<dd>Show Graphic card information (card, x type, resolution, glx renderer, version).</p>
<dt><code>-h </code></p>
<dd>This help menu.</p>
<dt><code>&#8211;help </code></p>
<dd>Same as -h</p>
<dt><code>-H </code></p>
<dd>This help menu, plus developer options. Do not use dev options in normal operation!</p>
<dt><code>-i </code></p>
<dd>Show Wan IP address, and shows local interfaces (requires ifconfig network tool). Same as -Nni. Not shown with -F for user security reasons, you shouldn&#8217;t paste your local/wan IP.</p>
<dt><code>-I </code></p>
<dd>Show Information: processes, uptime, memory, irc client, inxi version.</p>
<dt><code>-l </code></p>
<dd>Show partition labels. Default: short partition -P. For full -p output, use: -pl (or -plu).</p>
<dt><code>-M </code></p>
<dd>Show machine data. Motherboard, Bios, and if present, System Builder (Like Lenovo). Older systems/kernels without the required /sys data can use dmidecode instead, run as root.</p>
<dt><code>-n </code></p>
<dd>Show Advanced Network card information. Same as -Nn. Shows interface, speed, mac id, state, etc.</p>
<dt><code>-N </code></p>
<dd>Show Network card information. With -x, shows PCI BusID, Port number.</p>
<dt><code>-o </code></p>
<dd>Show unmounted partition information (includes UUID and LABEL if available). Shows file system type if you have file installed, if you are root OR if you have added to /etc/sudoers (sudo v. 1.7 or newer): &lt;username&gt; ALL = NOPASSWD: /usr/bin/file (sample)</p>
<dt><code>-p </code></p>
<dd>Show full partition information (-P plus all other detected partitions).</p>
<dt><code>-P </code></p>
<dd>Show Partition information (shows what -v 4 would show, but without extra data). Shows, if detected: / /boot /home /tmp /usr /var. Use -p to see all mounted partitions.</p>
<dt><code>-r </code></p>
<dd>Show distro repository data. Currently supported repo types: APT (Debian, Ubuntu + derived versions) </p>
<p> PACMAN (Arch Linux + derived versions) </p>
<p> PISI (Pardus + derived versions) </p>
<p> YUM. (Fedora, Redhat, maybe Suse + derived versions) </p>
<p> (as distro data is collected more will be added. If your&#8217;s is missing please show us how to get this information and we&#8217;ll try to add it.)</p>
<dt><code>-R</code></p>
<dd>Show RAID data. Shows RAID devices, states, levels, and components, and extra data with -x/-xx. If device is resyncing, shows resync progress line as well.</p>
<dt><code>&#8211;recommends </code></p>
<dd>Checks inxi application dependencies + recommends, and directories, then shows what package(s) you need to install to add support for that feature.</p>
<dt><code>-s</code></p>
<dd>Show sensors output (if sensors installed/configured): mobo/cpu/gpu temp; detected fan speeds. Gpu temp only for Fglrx/Nvidia drivers. Nvidia shows screen number for &gt; 1 screens.</p>
<dt><code>-S </code></p>
<dd>Show System information: host name, kernel, desktop environment (if in X), distro</p>
<dt><code>-t </code>[<code>c</code> or<code> m</code> or<code> cm</code> or<code> cm NUMBER</code>]- Show processes.</p>
<dd>
<dt><code>-t c </code></p>
<dd>cpu</p>
<dt><code>-t m </code></p>
<dd>memory</p>
<dt><code>-t cm c </code>cpu+memory.</p>
<dd>If followed by numbers <code>1</code>&#8211;<code>20 </code>, shows that number of processes for each type (default: 5; if in irc, max: 5) </p>
<p> Make sure to have <i>no space </i></p>
<dt><code>-u </code></p>
<dd>Show partition UUIDs. Default: short partition -P. For full -p output, use: -pu (or -plu).</p>
<dt><code>-U </code></p>
<dd>Auto-update script. Note: if you installed as root, you must be root to update, otherwise user is fine.</p>
<dt><code>-V </code></p>
<dd>inxi version information. Prints information then exits.</p>
<dt><code>&#8211;version </code></p>
<dd>same as -V</p>
<dt><code>-v<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code></p>
<dd>Script verbosity levels. Verbosity level number is required. Should not be used with -b or -F. </p>
<p> Supported levels: 0-7 Examples :<i> inxi -v 4 </i> or <i> inxi -v4</p>
<dt></i><code>-v 0 </code></p>
<dd>&#8211; Short output, same as: inxi</p>
<dt><code>-v 1 </code></p>
<dd>&#8211; Basic verbose, -S + basic CPU + -G + basic Disk + -I.</p>
<dt><code>-v 2 </code></p>
<dd>&#8211; Adds networking card (-N), Machine (-M) data, and shows basic hard disk data (names only). Same as: inxi -b</p>
<dt><code>-v 3 </code></p>
<dd>&#8211; Adds advanced CPU (-C), network (-n) data, and switches on -x advanced data option.</p>
<dt><code>-v 4 </code></p>
<dd>&#8211; Adds partition size/filled data (-P) for (if present):/, /home, /var/, /boot Shows full disk data (-D)</p>
<dt><code>-v 5 </code></p>
<dd>&#8211; Adds audio card (-A); sensors (-s), partition label (-l) and UUID (-u), short form of optical drives.</p>
<dt><code>-v 6 </code></p>
<dd>&#8211; Adds full partition data (-p), unmounted partition data (-o), optical drive data (-d).</p>
<dt><code>-v 7 </code></p>
<dd>&#8211; Adds network IP data (-i); triggers -xx.</p>
<dt><code>-x </code></p>
<dd>Show extra data (only works with verbose or line output, not short form):</p>
<dt><code>-x -C </code></p>
<dd>&#8211; bogomips on Cpu</p>
<dt><code>-x -d</code></p>
<dd>&#8211; Adds items to features line of optical drive; adds rev version to optical drive.</p>
<dt><code>-x -D</code></p>
<dd>&#8211; Hdd temp with disk data if you have hddtemp installed, if you are root OR if you have added to /etc/sudoers (sudo v. 1.7 or newer): </p>
<p> &lt;username&gt; ALL = NOPASSWD: /usr/sbin/hddtemp (sample)</p>
<dt><code>-x -G </code></p>
<dd>&#8211; Direct rendering status for Graphics (in X).</p>
<dt><code>-x -G </code></p>
<dd>&#8211; (for single gpu, nvidia driver) screen number gpu is running on.</p>
<dt><code>-x -i </code></p>
<dd>&#8211; Show IPv6 as well for LAN interface (IF) devices.</p>
<dt><code>-x -I</code></p>
<dd>&#8211; Show system GCC, default. With -xx, also show other installed GCC versions.</p>
<dt><code>-x -N -A </code>&#8211; Adds version/port(s)/driver version (if available) for Network/Audio;</p>
<dd>
<dt><code>-x -N -A -G </code>&#8211; Network, audio, graphics, shows PCI Bus ID/Usb ID number of card</p>
<dd>
<dt><code>-x -R </code></p>
<dd>&#8211; Shows component raid id. Adds second RAID Info line: raid level; report on drives (like 5/5); blocks; chunk size; bitmap (if present). Resync line, shows blocks synced/total blocks.</p>
<dt><code>-x -S </code></p>
<dd>&#8211; Desktop toolkit if avaliable (GNOME/XFCE/KDE only); Kernel gcc version</p>
<dt><code>-x -t </code></p>
<dd>&#8211; Adds memory use output to cpu (-xt c), and cpu use to memory (-xt m).</p>
<dt><code>-xx</code></p>
<dd>Show extra, extra data (only works with verbose or line output, not short form):</p>
<dt><code>-xx -D </code></p>
<dd>&#8211; Adds disk serial number</p>
<dt><code>-xx -I </code></p>
<dd>&#8211; Adds other detected installed gcc versions to primary gcc output (if present).</p>
<dt><code>-xx -M </code></p>
<dd>&#8211; Adds chassis information, if any data for that is available.</p>
<dt><code>-xx -R</code></p>
<dd>&#8211; Adds superblock (if present); algorythm, U data. Adds system info line (kernel support, read ahead, raid events). Adds if present, unused device line. If device is resyncing, shows resync progress line as well</p>
<dt><code>-xx -@ &lt;11-14&gt;</code></p>
<dd>&#8211; Automatically uploads debugger data tar.gz file to <a href="ftp://ftp.techpatterns.com">ftp.techpatterns.com</a>.</p>
<dt><code>-z </code></p>
<dd>Adds security filters for IP addresses, Mac, and user home directory name. Default on for irc clients.</p>
<dt><code>-Z </code></p>
<dd>Absolute override for output filters. Useful for debugging networking issues in irc for example.</p>
<dd></dl>
<h2>Debugging Options</h2>
<dl>
<dt><code>-% </code></p>
<dd>Overrides defective or corrupted data.</p>
<dt><code>-@ </code></p>
<dd>Triggers debugger output. Requires debugging level 1-14 (8-10 &#8211; logging of data). Less than 8 just triggers inxi debugger output on screen.</p>
<dt><code>-@ </code>[<code>1</code>&#8211;<code>7</code>]</p>
<dd>&#8211; On screen debugger output</p>
<dt><code>-@ 8 </code></p>
<dd>&#8211; Basic logging. Check <i> /home/yourname/.inxi/inxi*.log</p>
<dt></i><code>-@ 9 </code></p>
<dd>&#8211; Full file/sys info logging</p>
<dt><code>-@ 10 </code></p>
<dd>&#8211; Color logging.</p>
<dt><code>-@ &lt;11-14&gt;</code></p>
<dd>The following create a tar.gz file of system data, plus collecting the inxi output to file: To automatically upload debugger data tar.gz file to <a href="ftp://ftp.techpatterns.com">ftp.techpatterns.com</a>: inxi -xx@ &lt;11-14&gt; For alternate ftp upload locations: Example: </p>
<p> <i>inxi -! <a href="ftp://ftp.yourserver.com">ftp.yourserver.com</a>/incoming -xx@ 14</i> </p>
<dt><code>-@ 11 </code></p>
<dd>&#8211; With data file of xiin read of /sys</p>
<dt><code>-@ 12 </code></p>
<dd>&#8211; With xorg conf and log data, xrandr, xprop, xdpyinfo, glxinfo etc.</p>
<dt><code>-@ 13 </code></p>
<dd>&#8211; With data from dev, disks, partitions, etc., plus xiin data file.</p>
<dt><code>-@ 14 </code></p>
<dd>&#8211; Everything, full data collection </p>
</dl>
<h2>Supported Irc Clients</h2>
<dl>
<dt>BitchX Gaim/Pidgin ircII Irssi Konversation Kopete KSirc KVIrc Weechat Xchat</p>
<dd></dl>
<h2>Initialization File</h2>
<dl>
<dt>inxi will read the following configuration/initialization files in the following order:</p>
<dd>
<dt>/etc/inxi.conf</p>
<dd>
<dt>$HOME/.inxi/inxi.conf</p>
<dd>
<dt>See wiki pages for more information on how to set these up:</p>
<dd>
<dt><i><a rel="nofollow" href="http://code.google.com/p/inxi/wiki/script_configuration_files">http://code.google.com/p/inxi/wiki/script_configuration_files</a> </i></p>
<dd></dl>
<h2>Bugs</h2>
<p>Please report bugs using the following resources: </p>
<p> inxi wiki, file an issue report: <i><a rel="nofollow" href="http://code.google.com/p/inxi/issues/list">http://code.google.com/p/inxi/issues/list</a> </i> </p>
<p> post on inxi developer forums: <i><a rel="nofollow" href="http://techpatterns.com/forums/forum-32.html">http://techpatterns.com/forums/forum-32.html</a> </i> </p>
<p> You can also visit <i>irc.oftc.net channel: #smxi </i> to post issues. </p>
<p> You may be asked to run the inxi debugger tool which will upload a data dump of all system files for use in debugging inxi. These data dumps are very important since they provide us with all the real system data inxi uses to parse out its report.</p>
<h2>HOMEPAGE: <a rel="nofollow" href="http://code.google.com/p/inxi">http://code.google.com/p/inxi</a></h2>
<p></i></p>
<h2></h2>
<h2>Author And Contributors To Code</h2>
<p>Original infobash author and copyright holder: Copyright (C) 2005-2007 Michiel de Boer a.k.a. locsmif </p>
<p> inxi version: Copyright (C) 2008-12 Scott Rogers &amp; Harald Hope </p>
<p> Further fixes (listed as known): Horst Tritremmel &lt;hjt at sidux.com&gt; </p>
<p> Steven Barrett (aka: damentz) &#8211; usb audio patch; swap percent used patch </p>
<p> Man page creator with help from Harald, aus9</p>
