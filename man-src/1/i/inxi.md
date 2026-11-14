---
title: "inxi(1)"
name: "inxi"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inxi/"
description: "inxi – Command line system information script for console and IRC"
---

<h2 class="name">NAME</h2>
<p> inxi &#8211; Command line system information script for console and IRC </p>
<h2>SYNOPSIS</h2>
<p> <code>inxi</code> </p>
<p> <code>inxi</code> [<code>-AbBCdDfFGhiIlmMnNopPrRsSuUVwzZ</code>] </p>
<p> <code>inxi</code> [<code>-c NUMBER</code>] [<code>-t</code> [<code>c</code>|<code>m</code>|<code>cm</code>|<code>mc</code>][<code>NUMBER</code>]] [<code>-v NUMBER</code>] [<code>-W LOCATION</code>] [<code>&#8211;weather-unit</code> {<code>m</code>|<code>i</code>|<code>mi</code>|<code>im</code>}] [<code>-y WIDTH</code>] <code>inxi</code> [<code>&#8211;memory-modules</code>] [<code>&#8211;memory-short</code>] [<code>&#8211;recommends</code>] [<code>&#8211;slots</code>] [<code>&#8211;usb</code>] </p>
<p> <code>inxi [-x</code>|<code>-xx</code>|<code>-xxx</code>|<code>-a</code>|<code>&#8211;admin</code>] <code>-OPTION(s)</code> </p>
<p> All options have long form variants &#8211; see below for these and more advanced options. </p>
<h2>DESCRIPTION</h2>
<p> <code>inxi</code> is a command line system information script built for console and IRC. It is also used a debugging tool for forum technical support to quickly ascertain users&#8217; system configurations and hardware. inxi shows system hardware, CPU, drivers, Xorg, Desktop, Kernel, gcc version(s), Processes, RAM usage, and a wide variety of other useful information. </p>
<p> <code>inxi</code> output varies depending on whether it is being used on CLI or IRC, with some default filters and color options applied only for IRC use. Script colors can be turned off if desired with <code>-c 0</code>, or changed using the <code>-c</code> color options listed in the STANDARD OPTIONS section below. </p>
<h2>PRIVACY AND SECURITY</h2>
<p> In order to maintain basic privacy and security, inxi used on IRC automatically filters out your network device MAC address, WAN and LAN IP, your <code>/home</code> username directory in partitions, and a few other items. </p>
<p> Because inxi is often used on forums for support, you can also trigger this filtering with the <code>-z</code> option (<code>-Fz</code>, for example). To override the IRC filter, you can use the <code>-Z</code> option. This can be useful in debugging network connection issues online in a private chat, for example. </p>
<h2>USING OPTIONS</h2>
<p> Options can be combined if they do not conflict. You can either group the letters together or separate them. </p>
<p> Letters with numbers can have no gap or a gap at your discretion, except when using <code> -t</code>. </p>
<p> For example: <code>inxi</code> <code>-AG</code> or <code>inxi -A -G</code> or <code>inxi -c10</code> </p>
<p> Note that all the short form options have long form equivalents, which are listed below. However, usually the short form is used in examples in order to keep things simple. </p>
<h2>STANDARD OPTIONS</h2>
<dl>
<dt><code>-A</code>,<code> &#8211;audio</code></p>
<dd> Show Audio/sound card(s) information, including card driver.</p>
<dt><code>-b</code>,<code> &#8211;basic</code></p>
<dd> Show basic output, short form. Same as: <code>inxi -v 2</code></p>
<dt><code>-B</code>,<code> &#8211;battery</code></p>
<dd> Show system battery (<code>ID-x</code>) data, charge, condition, plus extra information (if battery present). Uses <code>/sys</code> or, for BSDs without systctl battery data, <code>dmidecode</code>. <code>dmidecode</code> does not have very much information, and none about current battery state/charge/voltage. Supports multiple batteries when using <code>/sys</code> data. </p>
<p> Note that for <code>charge</code>, the output shows the current charge, as well as its value as a percentage of the available capacity, which can be less than the original design capacity. In the following example, the actual current available capacity of the battery is <code>22.2 Wh</code>. </p>
<p> <code>charge: 20.1 Wh 95.4%</code> </p>
<p> The <code>condition</code> item shows the remaining available capacity / original design capacity, and then this figure as a percentage of original capacity available in the battery. </p>
<p> <code>condition: 22.2/36.4 Wh (61%)</code> </p>
<p> With <code>-x</code> shows attached <code>Device-x</code> information (mouse, keyboard, etc.) if they are battery powered. </p>
<dt><code>-c</code>,<code> &#8211;color</code> [<code>0</code>&#8211;<code>42</code>]</p>
<dd> Set color scheme. If no scheme number is supplied, 0 is assumed. </p>
<dt><code>-c </code>[<code>94</code>&#8211;<code>99</code>]</p>
<dd>
<p> These color selectors run a color selector option prior to inxi starting which lets you set the config file value for the selection. </p>
<p> NOTE: All configuration file set color values are removed when output is piped or redirected. You must use the explicit runtime <code>-c &lt;color number&gt;</code> option if you want color codes to be present in the piped/redirected output. </p>
<p> Color selectors for each type display (NOTE: IRC and global only show safe color set):</p>
<dt><code>-c 94</code></p>
<dd> &#8211; Console, out of X.</p>
<dt><code>-c 95</code></p>
<dd> &#8211; Terminal, running in X &#8211; like xTerm.</p>
<dt><code>-c 96</code></p>
<dd> &#8211; GUI IRC, running in X &#8211; like XChat, Quassel, Konversation etc.</p>
<dt><code>-c 97</code></p>
<dd> &#8211; Console IRC running in X &#8211; like irssi in xTerm.</p>
<dt><code>-c 98</code></p>
<dd> &#8211; Console IRC not in X.</p>
<dt><code>-c 99</code></p>
<dd> &#8211; Global &#8211; Overrides/removes all settings. </p>
<p> Setting a specific color type removes the global color selection.</p>
<dt><code>-C</code>,<code> &#8211;cpu</code></p>
<dd> Show full CPU output, including per CPU clock speed and CPU max speed (if available). If max speed data present, shows <code>(max)</code> in short output formats (<code>inxi</code>, <code>inxi -b</code>) if actual CPU speed matches max CPU speed. If max CPU speed does not match actual CPU speed, shows both actual and max speed information. See <code>-x</code> for more options. </p>
<p> For certain CPUs (some ARM, and AMD Zen family) shows CPU die count. </p>
<p> The details for each CPU include a technical description e.g. <code>type: MT MCP</code> </p>
<p> * <code>MT</code> &#8211; Multi/Hyper Threaded CPU, more than 1 thread per core (previously <code>HT</code>). </p>
<p> * <code>MCM</code> &#8211; Multi Chip Model (more than 1 die per CPU). </p>
<p> * <code>MCP</code> &#8211; Multi Core Processor (more than 1 core per CPU). </p>
<p> * <code>SMP</code> &#8211; Symmetric Multi Processing (more than 1 physical CPU). </p>
<p> * <code>UP</code> &#8211; Uni (single core) Processor. </p>
<dt><code>-d</code>,<code> &#8211;disk-full</code>,<code>&#8211;optical</code></p>
<dd> Show optical drive data as well as <code>-D</code> hard drive data. With <code>-x</code>, adds a feature line to the output. Also shows floppy disks if present. Note that there is no current way to get any information about the floppy device that I am aware of, so it will simply show the floppy ID without any extra data. <code>-xx</code> adds a few more features.</p>
<dt><code>-D</code>,<code> &#8211;disk</code></p>
<dd> Show Hard Disk info. Shows total disk space and used percentage. The disk used percentage includes space used by swap partition(s), since those are not usable for data storage. Note that with RAID disks, the percentage will be wrong since the total is computed from the disk sizes, but used is computed from mounted partition used percentages. This small defect may get corrected in the future. Also, unmounted partitions are not counted in disk use percentages since inxi has no access to the used amount. </p>
<p> Also shows per disk information: Disk ID, type (if present), vendor (if detected), model, and size. See <code>Extra Data Options</code> (<code>-x</code> options) and <code>Admin Extra Data Options</code> (<code>&#8211;admin</code> options) for many more features.</p>
<dt><code>-f</code>,<code> &#8211;flags</code></p>
<dd> Show all CPU flags used, not just the short list. Not shown with <code>-F</code> in order to avoid spamming. ARM CPUs: show <code>features</code> items.</p>
<dt><code>-F</code>,<code> &#8211;full</code></p>
<dd> Show Full output for inxi. Includes all Upper Case line letters except <code>-W</code>, plus <code>-s</code> and <code>-n</code>. Does not show extra verbose options such as <code>-d -f -i -l -m -o -p -r -t -u -x</code> unless you use those arguments in the command, e.g.: <code>inxi -Frmxx</code></p>
<dt><code>-G</code>,<code> &#8211;graphics</code></p>
<dd> Show Graphic card(s) information, including details of card and card driver, display protocol (if available), display server (vendor and version number), e.g.: </p>
<p> <code>Display: x11 server: Xorg 1.15.1</code> </p>
<p> If protocol is not detected, shows: </p>
<p> <code>Display: server: Xorg 1.15.1</code> </p>
<p> Also shows screen resolution(s), OpenGL renderer, OpenGL core profile version/OpenGL version. </p>
<p> Compositor information will show if detected using <code>-xx</code> option.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> The help menu. Features dynamic sizing to fit into terminal window. Set script global <code>COLS_MAX_CONSOLE</code> if you want a different default value, or use <code>-y &lt;width&gt;</code> to temporarily override the defaults or actual window width.</p>
<dt><code>-i</code>,<code> &#8211;ip</code></p>
<dd> Show WAN IP address and local interfaces (latter requires <code>ifconfig</code> or <code>ip</code> network tool), as well as network output from <code>-n</code>. Not shown with <code>-F</code> for user security reasons. You shouldn&#8217;t paste your local/WAN IP. Shows both IPv4 and IPv6 link IP addresses. </p>
<dt><code>-I</code>,<code> &#8211;info</code></p>
<dd> Show Information: processes, uptime, memory, IRC client (or shell type if run in shell, not IRC), inxi version. See <code>-x</code> and <code>-xx</code> for extra information (init type/version, runlevel). </p>
<p> Note: if <code>-m</code> is used or triggered, the memory item will show in the main Memory: report of <code>-m</code>, not in <code>Info:</code>. </p>
<p> Rasberry Pi only: uses <code>vcgencmd get_mem gpu</code> to get gpu RAM amount, if user is in video group and <code>vcgencmd</code> is installed. Uses this result to increase the <code>Memory:</code> amount and <code>used:</code> amounts.</p>
<dt><code>-l</code>,<code> &#8211;label</code></p>
<dd> Show partition labels. Default: main partitions <code>-P</code>. For full <code>-p</code> output, use: <code>-pl</code>.</p>
<dt><code>-m</code>,<code> &#8211;memory</code></p>
<dd> Memory (RAM) data. Does not display with <code>-b</code> or <code>-F</code> unless you use <code>-m</code> explicitly. Ordered by system board physical system memory array(s) (<code>Array-[number]</code>), and individual memory devices (<code>Device-[number]</code>). Physical memory array data shows array capacity, number of devices supported, and Error Correction information. Devices shows locator data (highly variable in syntax), size, speed, type (eg: <code>type: DDR3</code>). </p>
<p> Note: <code>-m</code> uses <code>dmidecode</code>, which must be run as root (or start <code>inxi</code> with <code>sudo</code>), unless you figure out how to set up sudo to permit dmidecode to read <code>/dev/mem</code> as user. <code>speed</code> and <code>bus width</code> will not show if <code>No Module Installed</code> is found in <code>size</code>. </p>
<p> Note: If <code>-m</code> is triggered RAM total/used report will appear in this section, not in <code>-I</code> or <code>-tm</code> items. </p>
<p> Because <code>dmidecode</code> data is extremely unreliable, inxi will try to make best guesses. If you see <code>(check)</code> after the capacity number, you should check it with the specifications. <code>(est)</code> is slightly more reliable, but you should still check the real specifications before buying RAM. Unfortunately there is nothing <code>inxi</code> can do to get truly reliable data about the system RAM; maybe one day the kernel devs will put this data into <code>/sys</code>, and make it real data, taken from the actual system, not dmi data. For most people, the data will be right, but a significant percentage of users will have either a wrong max module size, if present, or max capacity. </p>
<p> See <code>&#8211;memory-modules</code> and <code>&#8211;memory-short</code> if you want a shorter report.</p>
<dt><code>&#8211;memory-modules</code></p>
<dd> Memory (RAM) data. Show only RAM arrays and modules in Memory report. Skip empty slots. See <code>-m</code>.</p>
<dt><code>&#8211;memory-short</code></p>
<dd> Memory (RAM) data. Show a one line RAM report in Memory, e.g. <code>Report: arrays: 1 slots: 4 modules: 2 type: DDR4</code> See <code>-m</code>.</p>
<dt><code>-M</code>,<code> &#8211;machine</code></p>
<dd> Show machine data. Device, Motherboard, BIOS, and if present, System Builder (Like Lenovo). Older systems/kernels without the required <code>/sys</code> data can use <code>dmidecode</code> instead, run as root. If using <code>dmidecode</code>, may also show BIOS/UEFI revision as well as version. <code>&#8211;dmidecode</code> forces use of <code>dmidecode</code> data instead of <code>/sys</code>. Will also attempt to show if the system was booted by BIOS, UEFI, or UEFI [Legacy], the latter being legacy BIOS boot mode in a system board using UEFI. </p>
<p> Device information requires either <code>/sys</code> or <code>dmidecode</code>. Note that &#8216;other-vm?&#8217; is a type that means it&#8217;s usually a VM, but inxi failed to detect which type, or positively confirm which VM it is. Primary VM identification is via systemd-detect-virt but fallback tests that should also support some BSDs are used. Less commonly used or harder to detect VMs may not be correctly detected. If you get an incorrect output, post an issue and we&#8217;ll get it fixed if possible. </p>
<p> Due to unreliable vendor data, device type will show: desktop, laptop, notebook, server, blade, plus some obscure stuff that inxi is unlikely to ever run on.</p>
<dt><code>-n</code>,<code> &#8211;network-advanced</code></p>
<dd> Show Advanced Network card information in addition to that produced by <code>-N</code>. Shows interface, speed, MAC ID, state, etc.</p>
<dt><code>-N</code>,<code> &#8211;network</code></p>
<dd> Show Network card(s) information, including card driver. With <code>-x</code>, shows PCI BusID, Port number.</p>
<dt><code>-o</code>,<code> &#8211;unmounted</code></p>
<dd> Show unmounted partition information (includes UUID and LABEL if available). Shows file system type if you have <code>lsblk</code> installed (Linux only). For BSD/GNU Linux: shows file system type if <code>file</code> is installed, and if you are root or if you have added to <code>/etc/sudoers</code> (sudo v. 1.7 or newer): </p>
<p> <code>&lt;username&gt; ALL = NOPASSWD: /usr/bin/file (sample)</code> </p>
<p> Does not show components (partitions that create the md-raid array) of md-raid arrays.</p>
<dt><code>-p</code>,<code> &#8211;partitions-full</code></p>
<dd> Show full Partition information (<code>-P</code> plus all other detected mounted partitions).</p>
<dt><code>-P</code>,<code> &#8211;partitions</code></p>
<dd> Show basic Partition information. Shows, if detected: <code>/ /boot /home /opt /tmp /usr /usr/home /var /var/tmp /var/log</code>. Use <code>-p</code> to see all mounted partitions.</p>
<dt><code>-r</code>,<code> &#8211;repos</code></p>
<dd> Show distro repository data. Currently supported repo types: </p>
<p> <code>APK</code> (Alpine Linux + derived versions) </p>
<p> <code>APT</code> (Debian, Ubuntu + derived versions, as well as RPM based APT distros like PCLinuxOS or Alt-Linux) </p>
<p> <code>CARDS</code> (NuTyX + derived versions) </p>
<p> <code>EOPKG</code> (Solus) </p>
<p> <code>PACMAN</code> (Arch Linux, KaOS + derived versions) </p>
<p> <code>PACMAN-G2</code> (Frugalware + derived versions) </p>
<p> <code>PISI</code> (Pardus + derived versions) </p>
<p> <code>PORTAGE</code> (Gentoo, Sabayon + derived versions) </p>
<p> <code>PORTS</code> (OpenBSD, FreeBSD, NetBSD + derived OS types) </p>
<p> <code>SLACKPKG</code> (Slackware + derived versions) </p>
<p> <code>TCE</code> (TinyCore) </p>
<p> <code>URPMQ</code> (Mandriva, Mageia + derived versions) </p>
<p> <code>XBPS</code> (Void) </p>
<p> <code>YUM/ZYPP</code> (Fedora, Red Hat, Suse + derived versions) </p>
<p> More will be added as distro data is collected. If yours is missing please show us how to get this information and we&#8217;ll try to add it.</p>
<dt><code>-R</code>,<code> &#8211;raid</code></p>
<dd> Show RAID data. Shows RAID devices, states, levels and components, and extra data with <code>-x</code> / <code>-xx</code>. </p>
<p> md-raid: If device is resyncing, also shows resync progress line. </p>
<p> Note: Only md-raid and ZFS are currently supported. Other software RAID types could be added, but only if users supply all data required, and if the software RAID actually can be made to give the required output. </p>
<p> If hardware RAID is detected, shows basic information. Due to complexity of adding hardware RAID device disk / RAID reports, those will only be added if there is demand, and reasonable reporting tools. </p>
<dt><code>&#8211;recommends</code></p>
<dd> Checks inxi application dependencies and recommends, as well as directories, then shows what package(s) you need to install to add support for each feature.</p>
<dt><code>-s</code>,<code> &#8211;sensors</code></p>
<dd> Show output from sensors if sensors installed/configured: Motherboard/CPU/GPU temperatures; detected fan speeds. GPU temperature when available. Nvidia shows screen number for multiple screens. IPMI sensors are also used (root required) if present.</p>
<dt><code>&#8211;slots</code></p>
<dd> Show PCI slots with type, speed, and status information.</p>
<dt><code>-S</code>,<code> &#8211;system</code></p>
<dd> Show System information: host name, kernel, desktop environment (if in X), distro. With <code>-xx</code> show dm &#8211; or startx &#8211; (only shows if present and running if out of X), and if in X, with <code>-xxx</code> show more desktop info, e.g. taskbar or panel.</p>
<dt><code>-t</code>,<code> &#8211;processes</code></p>
<dd> [<code>c</code>|<code>m</code>|<code>cm</code>|<code>mc NUMBER</code>] Show processes. If no arguments, defaults to <code>cm</code>. If followed by a number, shows that number of processes for each type (default: <code>5</code>; if in IRC, max: <code>5</code>) </p>
<p> Make sure that there is no space between letters and numbers (e.g. write as <code>-t cm10</code>).</p>
<dt><code>-t c</code></p>
<dd> &#8211; CPU only. With <code>-x</code>, also shows memory for that process on same line.</p>
<dt><code>-t m</code></p>
<dd> &#8211; memory only. With <code>-x</code>, also shows CPU for that process on same line. If the -I line is not triggered, will also show the system RAM used/total information.</p>
<dt><code>-t cm</code></p>
<dd> &#8211; CPU+memory. With <code>-x</code>, shows also CPU or memory for that process on same line. </p>
<dt><code>&#8211;usb</code></p>
<dd> Show USB data for attached Hubs and Devices. Hubs also show number of ports. Be aware that a port is not always external, some may be internal, and either used or unused (for example, a motherboard USB header connector that is not used). </p>
<p> Hubs and Devices are listed in order of BusID. </p>
<p> BusID is generally in this format: BusID-port[.port][.port]:DeviceID </p>
<p> Device ID is a number created by the kernel, and has no necessary ordering or sequence connection, but can be used to match this output to lsusb values, which generally shows BusID / DeviceID (except for tree view, which shows ports). </p>
<p> Examples: <code>Device-3: 4-3.2.1:2</code> or <code>Hub: 4-0:1</code> </p>
<p> The <code>rev: 2.0</code> item refers to the USB revision number, like <code>1.0</code> or <code>3.1</code>. </p>
<dt><code>-u</code>,<code> &#8211;uuid</code></p>
<dd> Show partition UUIDs. Default: main partitions <code>-P</code>. For full <code>-p</code> output, use: <code>-pu</code>.</p>
<dt><code>-U</code>,<code> &#8211;update</code></p>
<dd> Note &#8211; Maintainer may have disabled this function. </p>
<p> If inxi <code>-h</code> has no listing for <code>-U</code> then it&#8217;s disabled. </p>
<p> Auto-update script. Note: if you installed as root, you must be root to update, otherwise user is fine. Also installs / updates this man page to: <code>/usr/local/share/man/man1</code> (if <code>/usr/local/share/man/</code> exists AND there is no inxi man page in <code>/usr/share/man/man1</code>, otherwise it goes to <code>/usr/share/man/man1</code>). This requires that you be root to write to that directory. See <code>&#8211;man</code> or <code>&#8211;no-man</code> to force or disable man install. </p>
<dt><code>-V</code>,<code> &#8211;version</code></p>
<dd> inxi version information. Prints information then exits.</p>
<dt><code>-v</code>,<code> &#8211;verbosity</code></p>
<dd> Script verbosity levels. If no verbosity level number is given, 0 is assumed. Should not be used with <code>-b</code> or <code>-F</code>. </p>
<p> Supported levels: <code>0-8</code> Examples :<code> inxi -v 4 </code> or <code> inxi -v4</code></p>
<dt><code>-v 0</code></p>
<dd> &#8211; Short output, same as: <code>inxi</code></p>
<dt><code>-v 1</code></p>
<dd> &#8211; Basic verbose, <code>-S</code> + basic CPU (cores, type, clock speed, and min/max speeds, if available) + <code>-G</code> + basic Disk + <code>-I</code>.</p>
<dt><code>-v 2</code></p>
<dd> &#8211; Adds networking card (<code>-N</code>), Machine (<code>-M</code>) data, Battery (<code>-B</code>) (if available). Same as: <code>inxi -b</code></p>
<dt><code>-v 3</code></p>
<dd> &#8211; Adds advanced CPU (<code>-C</code>) and network (<code>-n</code>) data; triggers <code>-x</code> advanced data option.</p>
<dt><code>-v 4</code></p>
<dd> &#8211; Adds partition size/used data (<code>-P</code>) for (if present): <code>/ /home /var/ /boot</code>. Shows full disk data (<code>-D</code>)</p>
<dt><code>-v 5</code></p>
<dd> &#8211; Adds audio card (<code>-A</code>), memory/RAM (<code>-m</code>), sensors (<code>-s</code>), partition label (<code>-l</code>), UUID (<code>-u</code>), and short form of optical drives.</p>
<dt><code>-v 6</code></p>
<dd> &#8211; Adds full mounted partition data (<code>-p</code>), unmounted partition data (<code>-o</code>), optical drive data (<code>-d</code>), USB (<code>&#8211;usb</code>); triggers <code>-xx</code> extra data option.</p>
<dt><code>-v 7</code></p>
<dd> &#8211; Adds network IP data (<code>-i</code>); triggers <code>-xxx</code></p>
<dt><code>-v 8</code></p>
<dd> &#8211; All system data available. Adds Repos (<code>-r</code>), PCI slots (<code>&#8211;slots</code>), processes (<code>-tcm</code>), admin (<code>&#8211;admin</code>). Useful for testing output and to see what data you can get from your system.</p>
<dt><code>-w</code>,<code> &#8211;weather</code></p>
<dd> Adds weather line. To get weather for an alternate location, use <code>-W [location]</code>. See also <code>-x</code>, <code>-xx</code>, <code>-xxx</code> options. Please note that your distribution&#8217;s maintainer may chose to disable this feature. </p>
<p> DO NOT USE THIS FEATURE FOR AUTOMATED WEATHER UPDATES! You will be blocked from any further access. This feature is not meant for widget type weather monitoring, or Conky type use. It is meant to get weather when you need to see it, for example, on a remote server.</p>
<dt><code>-W</code>, <code>&#8211;weather-location &lt;location_string&gt;</code></p>
<dd> Get weather/time for an alternate location. Accepts postal/zip code[, country], city,state pair, or latitude,longitude. Note: city/country/state names must not contain spaces. Replace spaces with &#8216;<code>+</code>&#8216; sign. Don&#8217;t place spaces around any commas. Postal code is not reliable except for North America and maybe the UK. Try postal codes with and without country code added. Note that City,State applies only to USA, otherwise it&#8217;s City,Country. If country name (english) does not work, try 2 character country code (e.g. Spain: es; Great Britain: gb). </p>
<p> See <i><a rel="nofollow" href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2</a></i> for current 2 letter country codes. </p>
<p> Use only ASCII letters in city/state/country names. </p>
<p> Examples: <code>-W 95623,us</code> OR <code>-W Boston,MA</code> OR <code>-W 45.5234,-122.6762</code> OR <code>-W new+york,ny</code> OR <code>-W bodo,norway</code>. </p>
<p> DO NOT USE THIS FEATURE FOR AUTOMATED WEATHER UPDATES! Use of automated queries, will result in your access being blocked. If you try to work around the ban, you will be permanently banned from this service.</p>
<dt><code>&#8211;weather-source</code>, <code>&#8211;ws &lt;unit&gt;</code></p>
<dd> [<code>1-9</code>] Switches weather data source. Possible values are <code>1-9</code>. <code>1-4</code> will generally be active, and <code>5-9</code> may or may not be active, so check. <code>1</code> may not support city / country names with spaces (even if you use the <code>+</code> sign instead of space). <code>2</code> offers pretty good data, but may not have all small city names for <code>-W</code>. </p>
<p> Please note that the data sources are not static per value, and can change any time, or be removed, so always test to verify which source is being used for each value if that is important to you. Data sources may be added or removed on occasions, so try each one and see which you prefer. If you get unsupported source message, it means that number has not been implemented.</p>
<dt><code>&#8211;weather-unit &lt;unit&gt;</code></p>
<dd> [<code>m</code>|<code>i</code>|<code>mi</code>|<code>im</code>] Sets weather units to metric (<code>m</code>), imperial (<code>i</code>), metric (imperial) (<code>mi</code>, default), imperial (metric) (<code>im</code>). If metric or imperial not found,sets to default value, or <code>N/A</code>.</p>
<dt><code>-y</code>,<code> &#8211;width &lt;integer&gt;</code></p>
<dd> This is an absolute width override which sets the output line width max. Overrides <code>COLS_MAX_IRC</code> / <code>COLS_MAX_CONSOLE</code> globals, or the actual widths of the terminal. <code>80</code> is the minimum width supported. <code>-1</code> removes width limits. Example: <code>inxi -Fxx -y 130</code></p>
<dt><code>-z</code>,<code> &#8211;filter</code></p>
<dd> Adds security filters for IP addresses, serial numbers, MAC, location (<code>-w</code>), and user home directory name. Removes Host:. On by default for IRC clients.</p>
<dt><code>-Z</code>,<code> &#8211;filter-override</code></p>
<dd> Absolute override for output filters. Useful for debugging networking issues in IRC for example.</dl>
<h2>EXTRA DATA OPTIONS</h2>
<p> These options can be triggered by one or more <code>-x</code>. Alternatively, the <code>-v</code> options trigger them in the following way: <code>-v 3</code> adds <code>-x</code>; <code>-v 6</code> adds <code>-xx</code>; <code>-v 7</code> adds <code>-xxx</code> </p>
<p> These extra data triggers can be useful for getting more in-depth data on various options. They can be added to any long form option list, e.g.: <code>-bxx</code> or <code>-Sxxx</code> </p>
<p> There are 3 extra data levels: </p>
<p> <code>-x</code>, <code>-xx</code>, <code>-xxx</code> </p>
<p> OR </p>
<p> <code>&#8211;extra 1</code>, <code>&#8211;extra 2</code>, <code>&#8211;extra 3</code> </p>
<p> The following details show which lines / items display extra information for each extra data level.</p>
<dl>
<dt><code>-x -A</code></p>
<dd> &#8211; Adds (if available and/or relevant) <code>vendor:</code> item, which shows specific vendor [product] information. </p>
<p> &#8211; Adds version/port(s)/driver version (if available) for each Audio device. </p>
<p> &#8211; Adds PCI Bus ID/USB ID number of each Audio device.</p>
<dt><code>-x -B</code></p>
<dd> &#8211; Adds vendor/model, battery status (if battery present). </p>
<p> &#8211; Adds attached battery powered peripherals (<code>Device-[number]:</code>) if detected (keyboard, mouse, etc.).</p>
<dt><code>-x -C</code></p>
<dd> &#8211; Adds bogomips on CPU (if available) </p>
<p> &#8211; Adds CPU Flags (short list). Use <code>-f</code> to see full flag/feature list. </p>
<p> &#8211; Adds CPU microarchitecture + revision (e.g. Sandy Bridge, K8, ARMv8, P6, etc.). Only shows data if detected. Newer microarchitectures will have to be added as they appear, and require the CPU family ID and model ID. </p>
<p> Examples: <code>arch: Sandy Bridge rev: 2</code>, <code>arch: K8 rev.F+ rev: 2</code></p>
<dt><code>-x -d</code></p>
<dd> &#8211; Adds more items to <code>Features</code> line of optical drive; dds rev version to optical drive.</p>
<dt><code>-x -D</code></p>
<dd> &#8211; Adds HDD temperature with disk data if you have hddtemp installed, if you are root or if you have added to <code>/etc/sudoers</code> (sudo v. 1.7 or newer): </p>
<p> <code>&lt;username&gt; ALL = NOPASSWD: /usr/sbin/hddtemp (sample)</code></p>
<dt><code>-x -G</code></p>
<dd> &#8211; Adds (if available and/or relevant) <code>vendor:</code> item, which shows specific vendor [product] information. </p>
<p> &#8211; Adds direct rendering status. </p>
<p> &#8211; Adds (for single GPU, nvidia driver) screen number that GPU is running on. </p>
<p> &#8211; Adds PCI Bus ID/USB ID number of each Graphics card.</p>
<dt><code>-x -i</code></p>
<dd> &#8211; Adds IP v6 additional scope data, like Global, Site, Temporary for each interface. </p>
<p> Note that there is no way I am aware of to filter out the deprecated IP v6 scope site/global temporary addresses from the output of <code>ifconfig</code>. The <code>ip</code> tool shows that clearly. </p>
<p> <code>ip-v6-temporary</code> &#8211; (<code>ip</code> tool only), scope global temporary. Scope global temporary deprecated is not shown </p>
<p> <code>ip-v6-global</code> &#8211; scope global (<code>ifconfig</code> will show this for all types, global, global temporary, and global temporary deprecated, <code>ip</code> shows it only for global) </p>
<p> <code>ip-v6-link</code> &#8211; scope link (<code>ip</code>/<code>ifconfig</code>) &#8211; default for <code>-i</code>. </p>
<p> <code>ip-v6-site</code> &#8211; scope site (<code>ip</code>/<code>ifconfig</code>). This has been deprecated in IPv6, but still exists. <code>ifconfig</code> may show multiple site values, as with global temporary, and global temporary deprecated. </p>
<p> <code>ip-v6-unknown</code> &#8211; unknown scope </p>
<dt><code>-x -I</code></p>
<dd> &#8211; Adds current init system (and init rc in some cases, like OpenRC). With <code>-xx</code>, shows init/rc version number, if available. </p>
<p> &#8211; Adds default system gcc. With <code>-xx</code>, also show other installed gcc versions. </p>
<p> &#8211; Adds current runlevel (not available with all init systems). </p>
<p> &#8211; If in shell (i.e. not in IRC client), adds shell version number, if available.</p>
<dt><code>-x -m</code>, <code>&#8211;memory-modules</code></p>
<dd> &#8211; If present, adds maximum memory module/device size in the Array line. Only some systems will have this data available. Shows estimate if it can generate one. </p>
<p> &#8211; Adds device type in the Device line.</p>
<dt><code>-x -N</code></p>
<dd> &#8211; Adds (if available and/or relevant) <code>vendor:</code> item, which shows specific vendor [product] information. </p>
<p> &#8211; Adds version/port(s)/driver version (if available) for each Network card; </p>
<p> &#8211; Adds PCI Bus ID/USB ID number of each Network card.</p>
<dt><code>-x -R</code></p>
<dd> &#8211; md-raid: Adds second RAID Info line with extra data: blocks, chunk size, bitmap (if present). Resync line, shows blocks synced/total blocks. </p>
<p> &#8211; Hardware RAID: Adds driver version, bus ID.</p>
<dt><code>-x -s</code></p>
<dd> &#8211; Adds basic voltages: 12v, 5v, 3.3v, vbat (<code>ipmi</code>, <code>lm-sensors</code> if present).</p>
<dt><code>-x -S</code></p>
<dd> &#8211; Adds Kernel gcc version. </p>
<p> &#8211; Adds to <code>Distro:</code> <code>base:</code> if detected. System base will only be seen on a subset of distributions. The distro must be both derived from a parent distro (e.g. Mint from Ubuntu), and explicitly added to the supported distributions for this feature. Due to the complexity of distribution identification, these will only be added as relatively solid methods are found for each distribution system base detection.</p>
<dt><code>-x -t</code></p>
<dd> &#8211; Adds memory use output to CPU (<code>-xt c</code>), and CPU use to memory (<code>-xt m</code>).</p>
<dt><code>-x &#8211;usb</code></p>
<dd> &#8211; For Devices, adds driver(s).</p>
<dt><code>-x -w</code>,<code> -W</code></p>
<dd> &#8211; Adds humidity and barometric pressure. </p>
<p> &#8211; Adds wind speed and direction.</p>
<dt><code>-xx -A</code></p>
<dd> &#8211; Adds vendor:product ID for each Audio device.</p>
<dt><code>-xx -B</code></p>
<dd> &#8211; Adds serial number, voltage (if available). Note that <code>volts</code> shows the data (if available) as the voltage now / minimum design voltage.</p>
<dt><code>-xx -C</code></p>
<dd> &#8211; Adds <code>L1 cache:</code> and <code>L3 cache:</code> if either are available. Requires dmidecode and sudo/root.</p>
<dt><code>-xx -D</code></p>
<dd> &#8211; Adds disk serial number. </p>
<p> &#8211; Adds disk speed (if available). This is the theoretical top speed of the device as reported. This speed may be restricted by system board limits, eg. a SATA 3 drive on a SATA 2 board may report SATA 2 speeds, but this is not completely consistent, sometimes a SATA 3 device on a SATA 2 board reports its design speed. </p>
<p> NVMe drives: adds lanes, and (per direction) speed is calculated with lane speed * lanes * PCIe overhead. PCIe 1 and 2 have data rates of GT/s * .8 = Gb/s (10 bits required to transfer 8 bits of data). PCIe 3 and greater transfer data at a rate of GT/s * 128/130 * lanes = Gb/s (130 bits required to transfer 128 bits of data). </p>
<p> For a PCIe 3 NVMe drive, with speed of <code>8 GT/s</code> and <code>4</code> lanes (<code>8GT/s * 128/130 * 4 = 31.6 Gb/s</code>): </p>
<p> <code>speed: 31.6 Gb/s lanes: 4</code></p>
<dt><code>-xx -G</code></p>
<dd> &#8211; Adds vendor:product ID of each Graphics card. </p>
<p> &#8211; Adds compositor, if found (experimental). </p>
<p> &#8211; For free drivers, adds OpenGL compatibility version number if available. For nonfree drivers, the core version and compatibility versions are usually the same. Example: </p>
<p> <code>v: 3.3 Mesa 11.2.0 compat-v: 3.0</code> </p>
<p> &#8211; If available, shows <code>alternate:</code> Xorg drivers. This means a driver on the default list of drivers Xorg automatically checks for the card, but which is not installed. For example, if you have <code>nouveau</code> driver, <code>nvidia</code> would show as alternate if it was not installed. Note that <code>alternate:</code> does NOT mean you should have it, it&#8217;s just one of the drivers Xorg checks to see if is present and loaded when checking the card. This can let you know there are other driver options. Note that if you have explicitly set the driver in <code>xorg.conf</code>, Xorg will not create this automatic check driver list. </p>
<dt><code>-xx -I</code></p>
<dd> &#8211; Adds init type version number (and rc if present). </p>
<p> &#8211; Adds other detected installed gcc versions (if present). </p>
<p> &#8211; Adds system default runlevel, if detected. Supports Systemd/Upstart/SysVinit type defaults. </p>
<p> &#8211; Adds parent program (or tty) that started shell, if not IRC client.</p>
<dt><code>-xx -m</code>, <code>&#8211;memory-modules</code></p>
<dd> &#8211; Adds memory device Manufacturer. </p>
<p> &#8211; Adds memory device Part Number (<code>part-no:</code>). Useful for ordering new or replacement memory sticks etc. Part numbers are unique, particularly if you use the word <code>memory</code> in the search as well. With <code>-xxx</code>, also shows serial number. </p>
<p> &#8211; Adds single/double bank memory, if data is found. Note, this may not be 100% right all of the time since it depends on the order that data is found in <code>dmidecode</code> output for <code>type 6</code> and <code>type 17</code>.</p>
<dt><code>-xx -M</code></p>
<dd> &#8211; Adds chassis information, if data is available. Also shows BIOS ROM size if using <code>dmidecode</code>.</p>
<dt><code>-xx -N</code></p>
<dd> &#8211; Adds vendor:product ID for each Network card.</p>
<dt><code>-xx -R</code></p>
<dd> &#8211; md-raid: Adds superblock (if present) and algorithm. If resync, shows progress bar. </p>
<p> &#8211; Hardware RAID: Adds Chip vendor:product ID.</p>
<dt><code>-xx -s</code></p>
<dd> &#8211; Adds DIMM/SOC voltages, if present (<code>ipmi</code> only).</p>
<dt><code>-xx -S</code></p>
<dd> &#8211; Adds display manager (<code>dm</code>) type, if present. If none, shows N/A. Supports most known display managers, including gdm, gdm3, idm, kdm, lightdm, lxdm, mdm, nodm, sddm, slim, tint, wdm, and xdm. </p>
<p> &#8211; Adds, if run in X, window manager type (<code>wm</code>), if available. Not all window managers are supported. Some desktops support using more than one window manager, so this can be useful to see what window manager is actually running. If none found, shows nothing. Uses a less accurate fallback tool <code>wmctrl</code> if <code>ps</code> tests fail to find data. </p>
<p> &#8211; Adds desktop toolkit (<code>tk</code>), if available (Xfce/KDE/Trinity).</p>
<dt><code>-xx &#8211;slots</code></p>
<dd> &#8211; Adds slot length.</p>
<dt><code>-xx &#8211;usb</code></p>
<dd> &#8211; Adds vendor:chip id.</p>
<dt><code>-xx -w</code>,<code> -W</code></p>
<dd> &#8211; Adds wind chill, heat index, and dew point, if available. </p>
<p> &#8211; Adds cloud cover, rain, snow, or precipitation (amount in previous hour to observation time), if available.</p>
<dt><code>-xxx -A</code></p>
<dd> &#8211; Adds, if present, serial number.</p>
<dt><code>-xxx -B</code></p>
<dd> &#8211; Adds battery chemistry (e.g. <code>Li-ion</code>), cycles (NOTE: there appears to be a problem with the Linux kernel obtaining the cycle count, so this almost always shows <code>0</code>. There&#8217;s nothing that can be done about this glitch, the data is simply not available as of 2018-04-03), location (only available from <code>dmidecode</code> derived output). </p>
<p> &#8211; Adds attached device <code>rechargeable: [yes|no]</code> information.</p>
<dt><code>-xxx -C</code></p>
<dd> &#8211; Adds <code>boost: [enabled|disabled]</code> if detected, aka <code>turbo</code>. Not all CPUs have this feature.</p>
<dt><code>-xxx -D</code></p>
<dd> &#8211; Adds disk firmware revision number (if available). </p>
<p> &#8211; Adds disk partition scheme (in most cases), e.g. <code>scheme: GPT</code>. Currently not able to detect all schemes, but handles the most common, e.g. <code>GPT</code> or <code>MBR</code>. </p>
<p> &#8211; Adds disk rotation speed (in some but not all cases), e.g. <code>rotation: 7200 rpm</code>. Only appears if detected (SSD drives do not have rotation speeds, for example). If none found, nothing shows. Not all disks report this speed, so even if they are spinnning, no data will show.</p>
<dt><code>-xxx -G</code></p>
<dd> &#8211; Adds (if available) <code>compositor:</code> version <code>v:</code>.</p>
<dt><code>-xxx -I</code></p>
<dd> &#8211; For <code>Shell:</code> adds <code>(su|sudo|login)</code> to shell name if present. </p>
<p> &#8211; For <code>running in:</code> adds <code>(SSH)</code> to parent, if present. SSH detection uses the <code>who am i</code> test.</p>
<dt><code>-xxx -m</code>, <code>&#8211;memory-modules</code></p>
<dd> &#8211; Adds memory bus width: primary bus width, and if present, total width. e.g. <code>bus width: 64 bit (total: 72 bits)</code>. Note that total / data widths are mixed up sometimes in dmidecode output, so inxi will take the larger value as the total if present. If no total width data is found, then inxi will not show that item. </p>
<p> &#8211; Adds device Type Detail, e.g. <code>detail: DDR3 (Synchronous)</code>. </p>
<p> &#8211; Adds, if present, memory module voltage. Only some systems will have this data available. </p>
<p> &#8211; Adds device serial number.</p>
<dt><code>-xxx -N</code></p>
<dd> &#8211; Adds, if present, serial number.</p>
<dt><code>-xxx -R</code></p>
<dd> &#8211; md-raid: Adds system mdraid support types (kernel support, read ahead, RAID events) </p>
<p> &#8211; zfs-raid: Adds portion allocated (used) by RAID array/device. </p>
<p> &#8211; Hardware RAID: Adds rev, ports, and (if available and/or relevant) <code>vendor:</code> item, which shows specific vendor [product] information.</p>
<dt><code>-xxx -S</code></p>
<dd> &#8211; Adds, if in X, or with <code>&#8211;display</code>, bar/dock/panel/tray items (<code>info</code>). If none found, shows nothing. Supports desktop items like gnome-panel, lxpanel, xfce4-panel, lxqt-panel, tint2, cairo-dock, trayer, and many others. </p>
<p> &#8211; Adds (if present), window manager (<code>wm</code>) version number. </p>
<p> &#8211; Adds (if present), display manager (<code>dm</code>) version number.</p>
<dt><code>-xxx &#8211;usb</code></p>
<dd> &#8211; Adds, if present, serial number for non hub devices. </p>
<p> &#8211; Adds <code>interfaces:</code> for non hub devices. </p>
<p> &#8211; Adds, if available, USB speed in <code>Mbits/s</code> or <code>Gbits/s</code>.</p>
<dt><code>-xxx -w</code>,<code> -W</code></p>
<dd> &#8211; Adds location (city state country), observation altitude (if available), weather observation time (if available), sunset/sunrise (if available). </p>
</dl>
<h2>ADMIN EXTRA DATA OPTIONS</h2>
<p> These options are triggered with <code>&#8211;admin</code> or <code>-a</code>. Admin options are advanced output options, and are more technical, and mostly of interest to system administrators or other machine admins. </p>
<p> The <code>&#8211;admin</code> option sets <code>-xxx</code>, and only has to be used once. It will trigger the following features: </p>
<dl>
<dt><code>-a -C</code></p>
<dd> &#8211; Adds CPU family, model-id, and stepping (replaces <code>rev</code> of <code>-Cx</code>). Format is <code>hexadecimal (decimal)</code> if greater than 9, otherwise <code>hexadecimal</code>. </p>
<p> &#8211; Adds CPU microcode. Format is <code>hexadecimal</code>. </p>
<p> &#8211; Adds CPU Vulnerabilities (bugs) as known by your current kernel. Lists by <code>Type: &#8230; (status|mitigation): &#8230;.</code> for systems that support this feature (Linux kernel 4.14 or newer, or patched older kernels). </p>
<dt><code>-a -d</code>,<code>-a -D</code></p>
<dd> &#8211; Adds logical and physical block size in bytes. </p>
<p> Using <code>smartctl</code> (requires sudo/root privileges). </p>
<p> &#8211; Adds device model family, like <code>Caviar Black</code>, if available. </p>
<p> &#8211; Adds SATA type (eg 1.0, 2.6, 3.0) if a SATA device. </p>
<p> &#8211; Adds SMART report line: status, enabled/disabled, health, powered on, cycles, and some error cases if out of range values. Note that for Pre-fail items, it will show the VALUE and THRESHOLD numbers. It will also fall back for unknown attributes that are or have been failing and print out the Attribute name, value, threshold, and failing message. This way even for unhandled Attribute names, you should get a solid report for full failure cases. Other cases may show if inxi believes that the item may be approaching failure. This is a guess so make sure to check the drive and smartctl full output to verify before taking any further action. </p>
<p> &#8211; Adds, for USB or other external drives, actual model name/serial if available, and different from enclosure model/serial, and corrects block sizes if necessary. Adds in drive temperature for some drives as well, and other useful data. </p>
<dt><code>-a -p</code>,<code>-a -P</code></p>
<dd> &#8211; Adds raw partition size, including file system overhead, partition table, e.g. </p>
<p> <code>raw size: 60.00 GiB</code>. </p>
<p> &#8211; Adds percent of raw size available to <code>size:</code> item, e.g. </p>
<p> <code>size: 58.81 GiB (98.01%)</code>. </p>
<p> Note that <code>used: 16.44 GiB (34.3%)</code> percent refers to the available size, not the raw size. </p>
<p> &#8211; Adds partition filesystem block size if found (requires root and blockdev). </p>
<p> &#8211; For swap, adds swappiness and vfs cache pressure, and a message to indicate if it is the default value or not (Linux only, and only if available). If not, shows default value as well, e.g. </p>
<p> <code>swappiness: 60 (default) cache pressure: 90 (default 100)</code>. </p>
<dt><code>-a -S</code></p>
<dd> &#8211; Adds kernel boot parameters to <code>Kernel</code> section (if detected). Support varies by OS type. </p>
</dl>
<h2>ADVANCED OPTIONS</h2>
<dl>
<dt><code>&#8211;alt 40</code></p>
<dd> Bypass <code>Perl</code> as a downloader option. Priority is: Perl (HTTP::Tiny), Curl, Wget, Fetch, (OpenBSD only) ftp. </p>
<dt><code>&#8211;alt 41</code></p>
<dd> Bypass <code>Curl</code> as a downloader option. Priority is: Perl (HTTP::Tiny), Curl, Wget, Fetch, (OpenBSD only) ftp. </p>
<dt><code>&#8211;alt 42</code></p>
<dd> Bypass <code>Fetch</code> as a downloader option. Priority is: Perl (HTTP::Tiny), Curl, Wget, Fetch, (OpenBSD only) ftp. </p>
<dt><code>&#8211;alt 43</code></p>
<dd> Bypass <code>Wget</code> as a downloader option. Priority is: Perl (HTTP::Tiny), Curl, Wget, Fetch, OpenBSD only: ftp </p>
<dt><code>&#8211;alt 44</code></p>
<dd> Bypass <code>Curl</code>, <code>Fetch</code>, and <code>Wget</code> as downloader options. This basically forces the downloader selection to use <code>Perl 5.x</code> <code>HTTP::Tiny</code>, which is generally slower than <code>Curl</code> or <code>Wget</code> but it may help bypass issues with downloading. </p>
<dt><code>&#8211;display [:&lt;integer&gt;]</code></p>
<dd> Will try to get display data out of X (does not usually work as root user). Default gets display info from display <code>:0</code>. If you use the format <code>&#8211;display :1</code> then it would get it from display <code>1</code> instead, or any display you specify. </p>
<p> Note that in some cases, <code>&#8211;display</code> will cause inxi to hang endlessly when running the option in console with Intel graphics. The situation regarding other free drivers such as nouveau/ATI is currently unknown. It may be that this is a bug with the Intel graphics driver &#8211; more information is required. </p>
<p> You can test this easily by running the following command out of X/display server: <code>glxinfo -display :0</code> </p>
<p> If it hangs, <code>&#8211;display</code> will not work. </p>
<dt><code>&#8211;dmidecode</code></p>
<dd> Force use of <code>dmidecode</code>. This will override <code>/sys</code> data in some lines, e.g. <code>-M</code> or <code>-B</code>. </p>
<dt><code>&#8211;downloader [curl|fetch|perl|wget]</code></p>
<dd> Force inxi to use Curl, Fetch, Perl, or Wget for downloads. </p>
<dt><code>&#8211;host</code></p>
<dd> Turns on hostname in System line. Overrides inxi config file value (if set): </p>
<p> <code>SHOW_HOST=&#8217;false&#8217;</code> &#8211; Same as: <code>SHOW_HOST=&#8217;true&#8217;</code> </p>
<p> This is an absolute override, the host will always show no matter what other switches you use. </p>
<dt><code>&#8211;indent-min [integer]</code></p>
<dd> Overrides default indent minimum value. This is the value that makes inxi change from wrapped line starters [like <code>Info</code>] to non wrapped. If less than <code>80</code>, no wrapping will occur. Overrides internal default value and user configuration value: </p>
<p> <code>INDENT_MIN=85</code> </p>
<dt><code>&#8211;limit [-1 &#8211; x]</code></p>
<dd> Raise or lower max output limit of IP addresses for <code>-i</code>. <code>-1</code> removes limit. </p>
<dt><code>&#8211;man</code></p>
<dd> Updates / installs man page with <code>-U</code> if <code>pinxi</code> or using <code>-U 3</code> dev branch. (Only active if <code>-U</code> is is not disabled by maintainers). </p>
<dt><code>&#8211;no-host</code></p>
<dd> Turns off hostname in System line. This is default when using <code>-z</code>, for anonymizing inxi output for posting on forums or IRC. Overrides configuration value (if set): </p>
<p> <code>SHOW_HOST=&#8217;true&#8217;</code> &#8211; Same as: <code>SHOW_HOST=&#8217;false&#8217;</code> </p>
<p> This is an absolute override, the host will not show no matter what other switches you use. </p>
<dt><code>&#8211;no-man</code></p>
<dd> Disables man page install with <code>-U</code> for master and active development branches. (Only active if <code>-U</code> is is not disabled by maintainers). </p>
<dt><code>&#8211;no-ssl</code></p>
<dd> Skip SSL certificate checks for all downloader actions (<code>-U</code>, <code>-w</code>, <code>-W</code>, <code>-i</code>). Use if your system does not have current SSL certificate lists, or if you have problems making a connection for any reason. Works with <code>Wget</code>, <code>Curl</code>, and <code>Fetch</code> only. </p>
<dt><code>&#8211;no-sudo</code></p>
<dd> Skips the use of sudo to run certain internal features (like <code>hddtemp</code>, <code>file</code>) with sudo. Not related to running inxi itself with sudo or super user. Some systems will register errors which will then trigger admin emails in such cases, so if you want to disable regular user use of sudo (which requires configuration to setup anyway for these options) just use this option, or <code>NO_SUDO</code> configuration item. </p>
<dt><code>&#8211;output [json|screen|xml]</code></p>
<dd> Change data output type. Requires &#8211;output-file if not <code>screen</code>. </p>
<dt><code>&#8211;output-file [full path to output file|print]</code></p>
<dd> The given directory path must exist. The directory path given must exist, The <code>print</code> options prints to stdout. Required for non-screen <code>&#8211;output</code> formats (json|xml). </p>
<dt><code>&#8211;partition-sort [dev-base|fs|id|label|percent-used|size|uuid|used]</code></p>
<dd> Change default sort order of partition output. Corresponds to <code>PARTITION_SORT</code> configuration item. These are the available sort options: </p>
<p> <code>dev-base</code> &#8211; <code>/dev</code> partition identifier, like <code>/dev/sda1</code>. Note that it&#8217;s an alphabetic sort, so <code>sda12</code> is before <code>sda2</code>. </p>
<p> <code>fs</code> &#8211; Partition filesystem. Note that sorts will be somewhat random if all filesystems are the same. </p>
<p> <code>id</code> &#8211; Mount point of partition (default). </p>
<p> <code>label</code> &#8211; Label of partition. If partitions have no labels, sort will be random. </p>
<p> <code>percent-used</code> &#8211; Percentage of partition size used. </p>
<p> <code>size</code> &#8211; KiB size of partition. </p>
<p> <code>uuid</code> &#8211; UUID of the partition. </p>
<p> <code>used</code> &#8211; KiB used of partition. </p>
<dt><code>&#8211;pm-type [package manager name]</code></p>
<dd> For distro package maintainers only, and only for non apt, rpm, or pacman based systems. To be used to test replacement package lists for recommends for that package manager. </p>
<dt><code>&#8211;sleep [0-x.x]</code></p>
<dd> Usually in decimals. Change CPU sleep time for <code>-C</code> (current: <code>&nbsp;.35</code>). Sleep is used to let the system catch up and show a more accurate CPU use. Example: </p>
<p> <code>inxi -Cxxx &#8211;sleep 0.15</code> </p>
<p> Overrides default internal value and user configuration value: </p>
<p> <code>CPU_SLEEP=0.25</code> </p>
<dt><code>&#8211;tty</code></p>
<dd> Forces internal IRC flag to off. Used in unhandled cases where the program running inxi may not be seen as a shell/tty, but it is not an IRC client. Put <code>&#8211;tty</code> first in option list to avoid unexpected errors. If you want a specific output width, use the <code>&#8211;width</code> option. If you want normal color codes in the output, use the <code>-c [color ID]</code> flag. </p>
<p> The sign you need to use this is extra numbers before the key/value pairs of the output of your program. These are IRC, not TTY, color codes. Please post a github issue if you find you need to use <code>&#8211;tty</code> (including the full <code>-Ixxx</code> line) so we can figure out how to add your program to the list of whitelisted programs. </p>
<p> You can see what inxi believed started it in the <code>-Ixxx</code> line, <code>Shell:</code> or <code>Client:</code> item. Please let us know what that result was so we can add it to the parent start program whitelist. </p>
<dt><code>&#8211;usb-sys</code></p>
<dd> Forces the USB data generator to use <code>/sys</code> as data source instead of <code>lsusb</code>. </p>
<dt><code>&#8211;usb-tool</code></p>
<dd> Forces the USB data generator to use <code>lsusb</code> as data source. Overrides <code>USB_SYS</code> in user configuration file(s). </p>
<dt><code>&#8211;wan-ip-url [URL]</code></p>
<dd> Force <code>-i</code> to use supplied URL as WAN IP source. Overrides dig or default IP source urls. URL must start with http[s] or ftp. </p>
<p> The IP address from the URL must be the last item on the last (non-empty) line of the page content source code. </p>
<p> Same as configuration value (example): </p>
<p> <code>WAN_IP_URL=&#8217;<a rel="nofollow" href="https://mysite.com/ip.php'">https://mysite.com/ip.php&#8217;</a></code> </p>
<dt><code>&#8211;wm</code></p>
<dd> Force <code>System</code> item <code>wm</code> to use <code>wmctrl</code> as data source, override default <code>ps</code> source. </p>
</dl>
<h2>DEBUGGING OPTIONS</h2>
<dl>
<dt><code>&#8211;dbg 1</code></p>
<dd> &#8211; Debug downloader failures. Turns off silent/quiet mode for curl, wget, and fetch. Shows more downloader action information. Shows some more information for Perl downloader. </p>
<dt><code>&#8211;debug [1-3]</code></p>
<dd> &#8211; On screen debugger output. Output varies depending on current needs Usually nothing changes. </p>
<dt><code>&#8211;debug 10</code></p>
<dd> &#8211; Basic logging. Check <code>$XDG_DATA_HOME/inxi/inxi.log</code> or <code>$HOME/.local/share/inxi/inxi.log</code> or <code>$HOME/.inxi/inxi.log</code>. </p>
<dt><code>&#8211;debug 11</code></p>
<dd> &#8211; Full file/system info logging. </p>
<dt><code>&#8211;debug 20</code></p>
<dd> Creates a tar.gz file of system data and collects the inxi output in a file. </p>
<p> * tree traversal data file(s) read from <code>/proc</code> and <code>/sys</code>, and other system data. </p>
<p> * xorg conf and log data, xrandr, xprop, xdpyinfo, glxinfo etc. </p>
<p> * data from dev, disks, partitions, etc. </p>
<dt><code>&#8211;debug 21</code></p>
<dd> Automatically uploads debugger data tar.gz file to <i><a href="ftp://ftp.techpatterns.com">ftp.techpatterns.com</a></i>, then removes the debug data directory, but leaves the debug tar.gz file. See <code>&#8211;ftp</code> for uploading to alternate locations. </p>
<dt><code>&#8211;debug 22</code></p>
<dd> Automatically uploads debugger data tar.gz file to <i><a href="ftp://ftp.techpatterns.com">ftp.techpatterns.com</a></i>, then removes the debug data directory and the tar.gz file. See <code>&#8211;ftp</code> for uploading to alternate locations. </p>
<dt><code>&#8211;ftp [<a href="ftp://ftp.yoursite.com">ftp.yoursite.com</a>/incoming]</code></p>
<dd> For alternate ftp upload locations: Example: </p>
<p> <code>inxi &#8211;ftp </code><i><a href="ftp://ftp.yourserver.com">ftp.yourserver.com</a>/incoming</i><code> &#8211;debug 21</code> </p>
</dl>
<h2>DEBUGGING OPTIONS TO DEBUG DEBUGGER FAILURES</h2>
<p> Only used the following in conjunction with <code>&#8211;debug 2[012]</code>, and only use if you experienced a failure or hang, or were instructed to do so. </p>
<dl>
<dt><code>&#8211;debug-proc</code></p>
<dd> Force debugger to parse <code>/proc</code> directory data when run as root. Normally this is disabled due to unpredictable data in /proc tree. </p>
<dt><code>&#8211;debug-proc-print</code></p>
<dd> Use this to locate file that /proc debugger hangs on. </p>
<dt><code>&#8211;debug-no-exit</code></p>
<dd> Skip exit on error when running debugger. </p>
<dt><code>&#8211;debug-no-proc</code></p>
<dd> Skip /proc debugging in case of a hang. </p>
<dt><code>&#8211;debug-no-sys</code></p>
<dd> Skip /sys debugging in case of a hang. </p>
<dt><code>&#8211;debug-sys</code></p>
<dd> Force PowerPC debugger parsing of /sys as sudo/root. </p>
<dt><code>&#8211;debug-sys-print</code></p>
<dd> Use this to locate file that /sys debugger hangs on. </p>
</dl>
<h2>SUPPORTED IRC CLIENTS</h2>
<p> BitchX, Gaim/Pidgin, ircII, Irssi, Konversation, Kopete, KSirc, KVIrc, Weechat, and Xchat. Plus any others that are capable of displaying either built-in or external script output. </p>
<h2>RUNNING IN IRC CLIENT</h2>
<p> To trigger inxi output in your IRC client, pick the appropriate method from the list below:</p>
<dl>
<dt><code>Hexchat, XChat, Irssi</code></p>
<dd> (and many other IRC clients) <code>/exec -o inxi </code>[<code>options</code>] If you don&#8217;t include the <code>-o</code>, only you will see the output on your local IRC client.</p>
<dt><code>Konversation</code></p>
<dd> <code>/cmd inxi</code> [<code>options</code>] </p>
<p> To run inxi in Konversation as a native script if your distribution or inxi package hasn&#8217;t already done this for you, create this symbolic link: </p>
<p> KDE 4: <code>ln -s /usr/local/bin/inxi /usr/share/kde4/apps/konversation/scripts/inxi</code> </p>
<p> KDE 5: <code>ln -s /usr/local/bin/inxi /usr/share/konversation/scripts/inxi</code> </p>
<p> If inxi is somewhere else, change the path <code>/usr/local/bin</code> to wherever it is located. </p>
<p> If you are using KDE/QT 5, then you may also need to add the following to get the Konversation /inxi command to work: </p>
<p> <code>ln -s /usr/share/konversation /usr/share/apps/</code> </p>
<p> Then you can start inxi directly, like this: </p>
<p> <code>/inxi</code> [<code>options</code>]</p>
<dt><code>WeeChat</code></p>
<dd> <code>NEW: /exec -o inxi</code> [<code>options</code>] </p>
<p> <code>OLD: /shell -o inxi</code> [<code>options</code>] </p>
<p> Newer (2014 and later) WeeChats work pretty much the same now as other console IRC clients, with <code>/exec -o inxi </code>[<code>options</code>]. Newer WeeChats have dropped the <code>-curses</code> part of their program name, i.e.: <code>weechat</code> instead of <code>weechat-curses</code>. </p>
</dl>
<h2>CONFIGURATION FILE</h2>
<p> inxi will read its configuration/initialization files in the following order: </p>
<p> <code>/etc/inxi.conf</code> contains the default configurations. These can be overridden by user configurations found in one of the following locations (inxi will store its config file using the following precedence: if <code>$XDG_CONFIG_HOME</code> is not empty, it will go there, else if <code>$HOME/.conf/inxi.conf</code> exists, it will go there, and as a last default, the legacy location is used), i.e.: </p>
<p> <code>$XDG_CONFIG_HOME/inxi.conf</code> &gt; <code>$HOME/.conf/inxi.conf</code> &gt; <code>$HOME/.inxi/inxi.conf</code> </p>
<h2>CONFIGURATION OPTIONS</h2>
<p> See the documentation page for more complete information on how to set these up, and for a complete list of options: </p>
<p> <i><a rel="nofollow" href="https://smxi.org/docs/inxi-configuration.htm">https://smxi.org/docs/inxi-configuration.htm</a></i></p>
<dl>
<dt><code>Basic Options</code></p>
<dd> Here&#8217;s a brief overview of the basic options you are likely to want to use: </p>
<p> <code>COLS_MAX_CONSOLE</code> The max display column width on terminal. </p>
<p> <code>COLS_MAX_IRC</code> The max display column width on IRC clients. </p>
<p> <code>COLS_MAX_NO_DISPLAY</code> The max display column width in console, out of GUI desktop. </p>
<p> <code>CPU_SLEEP</code> Decimal value <code>0</code> or more. Default is usually around <code>0.35</code> seconds. Time that inxi will &#8216;sleep&#8217; before getting CPU speed data, so that it reflects actual system state. </p>
<p> <code>DOWNLOADER</code> Sets default inxi downloader: curl, fetch, ftp, perl, wget. See <code>&#8211;recommends</code> output for more information on downloaders and Perl downloaders. </p>
<p> <code>FILTER_STRING</code> Default <code>&lt;filter&gt;</code>. Any string you prefer to see instead for filtered values. </p>
<p> <code>INDENT_MIN</code> The point where the line starter wrapping to its own line happens. Overrides default. See <code>&#8211;indent-min</code>. If <code>80</code> or less, wrap will never happen. </p>
<p> <code>LIMIT</code> Overrides default of <code>10</code> IP addresses per IF. This is only of interest to sys admins running servers with many IP addresses. </p>
<p> <code>NO_SUDO</code> Set to <code>1</code> or <code>true</code> to disable internal use of <code>sudo</code>. </p>
<p> <code>PARTITION_SORT</code> Overrides default partition output sort. See <code>&#8211;partition-sort</code> for options. </p>
<p> <code>PS_COUNT</code> The default number of items showing per <code>-t</code> type, <code>m</code> or <code>c</code>. Default is 5. </p>
<p> <code>SENSORS_CPU_NO</code> In cases of ambiguous temp1/temp2 (inxi can&#8217;t figure out which is the CPU), forces sensors to use either value 1 or 2 as CPU temperature. See the above configuration page on smxi.org for full info. </p>
<p> <code>SEP2_CONSOLE</code> Replaces default key / value separator of &#8216;<code>:</code>&#8216;. </p>
<p> <code>USB_SYS</code> Forces all USB data to use <code>/sys</code> instead of <code>lsusb</code>. </p>
<p> <code>WAN_IP_URL</code> Forces <code>-i</code> to use supplied URL, and to not use dig (dig is generally much faster). URL must begin with http or ftp. Note that if you use this, the downloader set tests will run each time you start inxi whether a downloader feature is going to be used or not. </p>
<p> The IP address from the URL must be the last item on the last (non-empty) line of the URL&#8217;s page content source code. </p>
<p> Same as <code>&#8211;wan-ip-url [URL]</code> </p>
<p> <code>WEATHER_SOURCE</code> Values: [<code>0-9</code>]. Same as <code>&#8211;weather-source</code>. Values 4-9 are not currently supported, but this can change at any time. </p>
<p> <code>WEATHER_UNIT</code> Values: [<code>c</code>|<code>f</code>|<code>cf</code>|<code>fc</code>]. Same as <code>&#8211;weather-unit</code>. </p>
<dt><code>Color Options</code></p>
<dd> It&#8217;s best to use the <code>-c [94-99]</code> color selector tool to set the following values because it will correctly update the configuration file and remove any invalid or conflicting items, but if you prefer to create your own configuration files, here are the options. All take the integer value from the options available in <code>-c 94-99</code>. </p>
<p> NOTE: All default and configuration file set color values are removed when output is piped or redirected. You must use the explicit <code>-c &lt;color number&gt;</code> option if you want colors to be present in the piped/redirected output (creating a PDF for example). </p>
<p> <code>CONSOLE_COLOR_SCHEME</code> The color scheme for console output (not in X/Wayland). </p>
<p> <code>GLOBAL_COLOR_SCHEME</code> Overrides all other color schemes. </p>
<p> <code>IRC_COLOR_SCHEME</code> Desktop X/Wayland IRC CLI color scheme. </p>
<p> <code>IRC_CONS_COLOR_SCHEME</code> Out of X/Wayland, IRC CLI color scheme. </p>
<p> <code>IRC_X_TERM_COLOR_SCHEME</code> In X/Wayland IRC client terminal color scheme. </p>
<p> <code>VIRT_TERM_COLOR_SCHEME</code> Color scheme for virtual terminal output (in X/Wayland). </p>
</dl>
<h2>BUGS</h2>
<p> Please report bugs using the following resources. </p>
<p> You may be asked to run the inxi debugger tool (see <code>&#8211;debug 21/22</code>), which will upload a data dump of system files for use in debugging inxi. These data dumps are very important since they provide us with all the real system data inxi uses to parse out its report.</p>
<dl>
<dt><code>Issue Report</code></p>
<dd> File an issue report: <i><a rel="nofollow" href="https://github.com/smxi/inxi/issues">https://github.com/smxi/inxi/issues</a></i></p>
<dt><code>Developer Forums</code></p>
<dd> Post on inxi developer forums: <i><a rel="nofollow" href="https://techpatterns.com/forums/forum-32.html">https://techpatterns.com/forums/forum-32.html</a></i></p>
<dt><code>IRC irc.oftc.net#smxi</code></p>
<dd> You can also visit <i>irc.oftc.net</i> channel:<i> #smxi</i> to post issues. </p>
</dl>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="https://github.com/smxi/inxi">https://github.com/smxi/inxi</a></i> </p>
<p> <i><a rel="nofollow" href="https://smxi.org/docs/inxi.htm">https://smxi.org/docs/inxi.htm</a></i> </p>
<h2>AUTHOR AND CONTRIBUTORS TO CODE</h2>
<p> <code>inxi</code> is a fork of <code>locsmif</code>&#8216;s very clever <code>infobash</code> script. </p>
<p> Original infobash author and copyright holder: Copyright (C) 2005-2007 Michiel de Boer aka locsmif </p>
<p> inxi version: Copyright (C) 2008-18 Harald Hope </p>
<p> This man page was originally created by Gordon Spencer (aka aus9) and is maintained by Harald Hope (aka h2 or TechAdmin). </p>
<p> Initial CPU logic, konversation version logic, occasional maintenance fixes, and the initial xiin.py tool for /sys parsing (obsolete, but still very much appreciated for all the valuable debugger data it helped generate): Scott Rogers </p>
<p> Further fixes (listed as known): </p>
<p> Horst Tritremmel &lt;hjt at sidux.com&gt; </p>
<p> Steven Barrett (aka: damentz) &#8211; USB audio patch; swap percent used patch. </p>
<p> Jarett.Stevens &#8211; <code>dmidecode -M</code> patch for older systems with no <code>/sys</code>. </p>
<h2>SPECIAL THANKS TO THE FOLLOWING</h2>
<p> The nice people at irc.oftc.net channels #linux-smokers-club and #smxi, who all really have to be considered to be co-developers because of their non-stop enthusiasm and willingness to provide real-time testing and debugging of inxi development. </p>
<p> Siduction forum members, who have helped get some features working by providing a large number of datasets that have revealed possible variations, particularly for the RAM <code>-m</code> option. </p>
<p> AntiX users and admins, who have helped greatly with testing and debugging, particularly for the 3.0.0 release. </p>
<p> ArcherSeven (Max), Brett Bohnenkamper (aka KittyKatt), and Iotaka, who always manage to find the weirdest or most extreme hardware and setups that help make inxi much more robust. </p>
<p> For the vastly underrated skill of output error/glitch catching, Pete Haddow. His patience and focus in going through inxi repeatedly to find errors and inconsistencies is much appreciated. </p>
<p> All the inxi package maintainers, distro support people, forum moderators, and in particular, sys admins with their particular issues, which almost always help make inxi better, and any others who contribute ideas, suggestions, and patches. </p>
<p> Without a wide range of diverse Linux kernel-based Free Desktop systems to test on, we could never have gotten inxi to be as reliable and solid as it&#8217;s turning out to be. </p>
<p> And of course, a big thanks to locsmif, who figured out a lot of the core methods, logic, and tricks originally used in inxi Gawk/Bash. </p>
<h2>Index</h2>
