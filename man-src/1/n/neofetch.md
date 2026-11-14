---
title: "neofetch(1)"
name: "neofetch"
section: "1"
letter: "n"
url: "/docs/linux/man/1-neofetch/"
description: "Neofetch – A fast, highly customizable system info script"
---

<h2 class="name">NAME</h2>
<p> Neofetch &#8211; A fast, highly customizable system info script </p>
<h2>SYNOPSIS</h2>
<p> <code>neofetch</code> <i>,func_name &#8211;option &quot;value&quot; &#8211;option &quot;value&quot;/</i></p>
<h2>DESCRIPTION</h2>
<p> Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice. </p>
<p> NOTE: Every launch flag has a config option.</p>
<h2>OPTIONS</h2>
<h3>INFO:</h3>
<dl>
<dt>func_name</p>
<dd> Specify a function name (second part of info() from config) to quickly display only that function&#8217;s information.</p>
<dt>
<dd> Example: neofetch uptime <code>&#8211;uptime_shorthand</code> tiny</p>
<dt>
<dd> Example: neofetch uptime disk wm memory</p>
<dt>
<dd> This can be used in bars and scripts like so:</p>
<dt>
<dd> memory=&quot;$(neofetch memory)&quot;; memory=&quot;${memory##*: }&quot;</p>
<dt>
<dd> For multiple outputs at once (each line of info in an array):</p>
<dt>
<dd> IFS=$&#8217;
&#8217; read <code>-d</code> &quot;&quot; <code>-ra</code> info &lt; &lt;(neofetch memory uptime wm)</p>
<dt>
<dd> info=(&quot;${info[@]##*: }&quot;)</p>
<dt><code>&#8211;disable</code> infoname</p>
<dd> Allows you to disable an info line from appearing in the output. &#8216;infoname&#8217; is the function name from the &#8216;print_info()&#8217; function inside the config file. For example: &#8216;info &quot;Memory&quot; memory&#8217; would be &#8216;&#8211;disable memory&#8217;</p>
<dt>
<dd> NOTE: You can supply multiple args. eg. &#8216;neofetch <code>&#8211;disable</code> cpu gpu&#8217;</p>
<dt><code>&#8211;package_managers</code> on/off</p>
<dd> Hide/Show Package Manager names . (on, tiny, off)</p>
<dt><code>&#8211;os_arch</code> on/off</p>
<dd> Hide/Show OS architecture.</p>
<dt><code>&#8211;speed_type</code> type</p>
<dd> Change the type of cpu speed to display. Possible values: current, min, max, bios, scaling_current, scaling_min, scaling_max</p>
<dt>
<dd> NOTE: This only supports Linux with cpufreq.</p>
<dt><code>&#8211;speed_shorthand</code> on/off</p>
<dd> Whether or not to show decimals in CPU speed.</p>
<dt>NOTE: This flag is not supported in systems with CPU speed less than</p>
<dd> 1 GHz.</p>
<dt><code>&#8211;cpu_brand</code> on/off</p>
<dd> Enable/Disable CPU brand in output.</p>
<dt><code>&#8211;cpu_cores</code> type</p>
<dd> Whether or not to display the number of CPU cores Possible values: logical, physical, off</p>
<dt>
<dd> NOTE: &#8216;physical&#8217; doesn&#8217;t work on BSD.</p>
<dt><code>&#8211;cpu_speed</code> on/off</p>
<dd> Hide/Show cpu speed.</p>
<dt><code>&#8211;cpu_temp</code> C/F/off</p>
<dd> Hide/Show cpu temperature.</p>
<dt>
<dd> NOTE: This only works on Linux and BSD.</p>
<dt>NOTE: For FreeBSD and NetBSD-based systems, you need to enable</p>
<dd> coretemp kernel module. This only supports newer Intel processors.</p>
<dt><code>&#8211;distro_shorthand</code> on/off</p>
<dd> Shorten the output of distro (on, tiny, off)</p>
<dt>
<dd> NOTE: This option won&#8217;t work in Windows (Cygwin)</p>
<dt><code>&#8211;kernel_shorthand</code> on/off</p>
<dd> Shorten the output of kernel</p>
<dt>
<dd> NOTE: This option won&#8217;t work in BSDs (except PacBSD and PC-BSD)</p>
<dt><code>&#8211;uptime_shorthand</code> on/off</p>
<dd> Shorten the output of uptime (on, tiny, off)</p>
<dt><code>&#8211;refresh_rate</code> on/off</p>
<dd> Whether to display the refresh rate of each monitor Unsupported on Windows</p>
<dt><code>&#8211;gpu_brand</code> on/off</p>
<dd> Enable/Disable GPU brand in output. (AMD/NVIDIA/Intel)</p>
<dt><code>&#8211;gpu_type</code> type</p>
<dd> Which GPU to display. (all, dedicated, integrated)</p>
<dt>
<dd> NOTE: This only supports Linux.</p>
<dt><code>&#8211;de_version</code> on/off</p>
<dd> Show/Hide Desktop Environment version</p>
<dt><code>&#8211;gtk_shorthand</code> on/off</p>
<dd> Shorten output of gtk theme/icons</p>
<dt><code>&#8211;gtk2</code> on/off</p>
<dd> Enable/Disable gtk2 theme/font/icons output</p>
<dt><code>&#8211;gtk3</code> on/off</p>
<dd> Enable/Disable gtk3 theme/font/icons output</p>
<dt><code>&#8211;shell_path</code> on/off</p>
<dd> Enable/Disable showing $SHELL path</p>
<dt><code>&#8211;shell_version</code> on/off</p>
<dd> Enable/Disable showing $SHELL version</p>
<dt><code>&#8211;disk_show</code> value</p>
<dd> Which disks to display. Possible values: &#8216;/&#8217;, &#8216;/dev/sdXX&#8217;, &#8216;/path/to/mount point&#8217;</p>
<dt>
<dd> NOTE: Multiple values can be given. (<code>&#8211;disk_show</code> &#8216;/&#8217; &#8216;/dev/sdc1&#8217;)</p>
<dt><code>&#8211;disk_subtitle</code> type</p>
<dd> What information to append to the Disk subtitle. Takes: name, mount, dir, none</p>
<dt>
<dd> &#8216;name&#8217; shows the disk&#8217;s name (sda1, sda2, etc)</p>
<dt>
<dd> &#8216;mount&#8217; shows the disk&#8217;s mount point (/, <i>,/mnt/Local/</i> Disk, etc)</p>
<dt>
<dd> &#8216;dir&#8217; shows the basename of the disks&#8217;s path. (/, Local Disk, etc)</p>
<dt>
<dd> &#8216;none&#8217; shows only &#8216;Disk&#8217; or the configured title.</p>
<dt><code>&#8211;disk_percent</code> on/off</p>
<dd> Hide/Show disk percent.</p>
<dt><code>&#8211;ip_host</code> url</p>
<dd> URL to query for public IP</p>
<dt><code>&#8211;ip_timeout</code> int</p>
<dd> Public IP timeout (in seconds).</p>
<dt><code>&#8211;song_format</code> format</p>
<dd> Print the song data in a specific format (see config file).</p>
<dt><code>&#8211;song_shorthand</code> on/off</p>
<dd> Print the Artist/Album/Title on separate lines.</p>
<dt><code>&#8211;memory_percent</code> on/off</p>
<dd> Display memory percentage.</p>
<dt><code>&#8211;music_player</code> player-name</p>
<dd> Manually specify a player to use. Available values are listed in the config file</dl>
<h3>TEXT FORMATTING:</h3>
<dl>
<dt><code>&#8211;colors</code> x x x x x x</p>
<dd> Changes the text colors in this order: title, @, underline, subtitle, colon, info</p>
<dt><code>&#8211;underline</code> on/off</p>
<dd> Enable/Disable the underline.</p>
<dt><code>&#8211;underline_char</code> char</p>
<dd> Character to use when underlining title</p>
<dt><code>&#8211;bold</code> on/off</p>
<dd> Enable/Disable bold text</p>
<dt><code>&#8211;separator</code> string</p>
<dd> Changes the default &#8216;:&#8217; separator to the specified string.</dl>
<h3>COLOR BLOCKS:</h3>
<dl>
<dt><code>&#8211;color_blocks</code> on/off</p>
<dd> Enable/Disable the color blocks</p>
<dt><code>&#8211;col_offset</code> auto/num</p>
<dd> Left-padding of color blocks</p>
<dt><code>&#8211;block_width</code> num</p>
<dd> Width of color blocks in spaces</p>
<dt><code>&#8211;block_height</code> num</p>
<dd> Height of color blocks in lines</p>
<dt><code>&#8211;block_range</code> num num</p>
<dd> Range of colors to print as blocks</dl>
<h3>BARS:</h3>
<dl>
<dt><code>&#8211;bar_char</code> &#8216;elapsed char&#8217; &#8216;total char&#8217;</p>
<dd> Characters to use when drawing bars.</p>
<dt><code>&#8211;bar_border</code> on/off</p>
<dd> Whether or not to surround the bar with &#8216;[]&#8217;</p>
<dt><code>&#8211;bar_length</code> num</p>
<dd> Length in spaces to make the bars.</p>
<dt><code>&#8211;bar_colors</code> num num</p>
<dd> Colors to make the bar. Set in this order: elapsed, total</p>
<dt><code>&#8211;cpu_display</code> mode</p>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</p>
<dt><code>&#8211;memory_display</code> mode</p>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</p>
<dt><code>&#8211;battery_display</code> mode</p>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</p>
<dt><code>&#8211;disk_display</code> mode</p>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</dl>
<h3>IMAGE BACKEND:</h3>
<dl>
<dt><code>&#8211;backend</code> backend</p>
<dd> Which image backend to use. Possible values: &#8216;ascii&#8217;, &#8216;caca&#8217;, &#8216;chafa&#8217;, &#8216;jp2a&#8217;, &#8216;iterm2&#8217;, &#8216;off&#8217;, &#8216;sixel&#8217;, &#8216;tycat&#8217;, &#8216;w3m&#8217;, &#8216;kitty&#8217;</p>
<dt><code>&#8211;source</code> source</p>
<dd> Which image or ascii file to use. Possible values: &#8216;auto&#8217;, &#8216;ascii&#8217;, &#8216;wallpaper&#8217;, &#8216;/path/to/img&#8217;, &#8216;/path/to/ascii&#8217;, &#8216;/path/to/dir/&#8217;, &#8216;command output&#8217; [ascii]</p>
<dt><code>&#8211;ascii</code> source</p>
<dd> Shortcut to use &#8216;ascii&#8217; backend.</p>
<dt>
<dd> NEW: neofetch <code>&#8211;ascii</code> &quot;$(fortune | cowsay <code>-W</code> 30)&quot;</p>
<dt><code>&#8211;caca</code> source</p>
<dd> Shortcut to use &#8216;caca&#8217; backend.</p>
<dt><code>&#8211;chafa</code> source</p>
<dd> Shortcut to use &#8216;chafa&#8217; backend.</p>
<dt><code>&#8211;iterm2</code> source</p>
<dd> Shortcut to use &#8216;iterm2&#8217; backend.</p>
<dt><code>&#8211;jp2a</code> source</p>
<dd> Shortcut to use &#8216;jp2a&#8217; backend.</p>
<dt><code>&#8211;kitty</code> source</p>
<dd> Shortcut to use &#8216;kitty&#8217; backend.</p>
<dt><code>&#8211;pixterm</code> source</p>
<dd> Shortcut to use &#8216;pixterm&#8217; backend.</p>
<dt><code>&#8211;sixel</code> source</p>
<dd> Shortcut to use &#8216;sixel&#8217; backend.</p>
<dt><code>&#8211;termpix</code> source</p>
<dd> Shortcut to use &#8216;termpix&#8217; backend.</p>
<dt><code>&#8211;tycat</code> source</p>
<dd> Shortcut to use &#8216;tycat&#8217; backend.</p>
<dt><code>&#8211;w3m</code> source</p>
<dd> Shortcut to use &#8216;w3m&#8217; backend.</p>
<dt><code>&#8211;off</code></p>
<dd> Shortcut to use &#8216;off&#8217; backend (Disable ascii art).</p>
<dt>
<dd> NOTE: &#8216;source; can be any of the following: &#8216;auto&#8217;, &#8216;ascii&#8217;, &#8216;wallpaper&#8217;, &#8216;/path/to/img&#8217;, &#8216;/path/to/ascii&#8217;, &#8216;/path/to/dir/&#8217;</dl>
<h3>ASCII:</h3>
<dl>
<dt><code>&#8211;ascii_colors</code> x x x x x x</p>
<dd> Colors to print the ascii art</p>
<dt><code>&#8211;ascii_distro</code> distro</p>
<dd> Which Distro&#8217;s ascii art to print</p>
<dt>NOTE: AIX, Alpine, Anarchy, Android, Antergos, antiX, AOSC,</p>
<dd> Apricity, ArcoLinux, ArchBox, ARCHlabs, ArchStrike, XFerience, ArchMerge, Arch, Artix, Arya, Bedrock, Bitrig, BlackArch, BLAG, BlankOn, BlueLight, bonsai, BSD, BunsenLabs, Calculate, Carbs, CentOS, Chakra, ChaletOS, Chapeau, Chrom, Cleanjaro, ClearOS, Clear_Linux, Clover, Condres, Container_Linux, CRUX, Cucumber, Debian, Deepin, DesaOS, Devuan, DracOS, DragonFly, Drauger, Elementary, EndeavourOS, Endless, EuroLinux, Exherbo, Fedora, Feren, FreeBSD, FreeMiNT, Frugalware, Funtoo, GalliumOS, Gentoo, Pentoo, gNewSense, GNU, GoboLinux, Grombyang, Guix, Haiku, Huayra, Hyperbola, janus, Kali, KaOS, KDE_neon, Kibojoe, Kogaion, Korora, KSLinux, Kubuntu, LEDE, LFS, Linux_Lite, LMDE, Lubuntu, Lunar, macos, Mageia, MagpieOS, Mandriva, Manjaro, Maui, Mer, Minix, LinuxMint, MX_Linux, Namib, Neptune, NetBSD, Netrunner, Nitrux, NixOS, Nurunner, NuTyX, OBRevenge, OpenBSD, OpenIndiana, OpenMandriva, OpenWrt, osmc, Oracle, PacBSD, Parabola, Pardus, Parrot, Parsix, TrueOS, PCLinuxOS, Peppermint, popos, Porteus, PostMarketOS, Proxmox, Puppy, PureOS, Qubes, Radix, Raspbian, Reborn_OS, Redstar, Redcore, Redhat, Refracted_Devuan, Regata, Rosa, sabotage, Sabayon, Sailfish, SalentOS, Scientific, Septor, SharkLinux, Siduction, Slackware, SliTaz, SmartOS, Solus, Source_Mage, Sparky, Star, SteamOS, SunOS, openSUSE_Leap, openSUSE_Tumbleweed, openSUSE, SwagArch, Tails, Trisquel, Ubuntu-Budgie, Ubuntu-GNOME, Ubuntu-MATE, Ubuntu-Studio, Ubuntu, Void, Obarun, windows10, Windows7, Xubuntu, Zorin, and IRIX have ascii logos</p>
<dt>
<dd> NOTE: Arch, Ubuntu, Redhat, and Dragonfly have &#8216;old&#8217; logo variants.</p>
<dt>
<dd> NOTE: Use &#8216;{distro name}_old&#8217; to use the old logos.</p>
<dt>
<dd> NOTE: Ubuntu has flavor variants.</p>
<dt>NOTE: Change this to Lubuntu, Kubuntu, Xubuntu, Ubuntu-GNOME,</p>
<dd> Ubuntu-Studio, Ubuntu-Mate or Ubuntu-Budgie to use the flavors.</p>
<dt>NOTE: Arcolinux, Dragonfly, Fedora, Alpine, Arch, Ubuntu,</p>
<dd> CRUX, Debian, Gentoo, FreeBSD, Mac, NixOS, OpenBSD, android, Antrix, CentOS, Cleanjaro, ElementaryOS, GUIX, Hyperbola, Manjaro, MXLinux, NetBSD, Parabola, POP_OS, PureOS, Slackware, SunOS, LinuxLite, OpenSUSE, Raspbian, postmarketOS, and Void have a smaller logo variant.</p>
<dt>
<dd> NOTE: Use &#8216;{distro name}_small&#8217; to use the small variants.</p>
<dt><code>&#8211;ascii_bold</code> on/off</p>
<dd> Whether or not to bold the ascii logo.</p>
<dt><code>-L</code>, <code>&#8211;logo</code></p>
<dd> Hide the info text and only show the ascii logo.</dl>
<h3>IMAGE:</h3>
<dl>
<dt><code>&#8211;loop</code></p>
<dd> Redraw the image constantly until Ctrl+C is used. This fixes issues in some terminals emulators when using image mode.</p>
<dt><code>&#8211;size</code> 00px | <code>&#8211;size</code> 00%</p>
<dd> How to size the image. Possible values: auto, 00px, 00%, none</p>
<dt><code>&#8211;crop_mode</code> mode</p>
<dd> Which crop mode to use Takes the values: normal, fit, fill</p>
<dt><code>&#8211;crop_offset</code> value</p>
<dd> Change the crop offset for normal mode. Possible values: northwest, north, northeast, west, center, east, southwest, south, southeast</p>
<dt><code>&#8211;xoffset</code> px</p>
<dd> How close the image will be to the left edge of the window. This only works with w3m.</p>
<dt><code>&#8211;yoffset</code> px</p>
<dd> How close the image will be to the top edge of the window. This only works with w3m.</p>
<dt><code>&#8211;bg_color</code> color</p>
<dd> Background color to display behind transparent image. This only works with w3m.</p>
<dt><code>&#8211;gap</code> num</p>
<dd> Gap between image and text.</p>
<dt>NOTE: <code>&#8211;gap</code> can take a negative value which will move the text</p>
<dd> closer to the left side.</p>
<dt><code>&#8211;clean</code></p>
<dd> Delete cached files and thumbnails.</dl>
<h3>OTHER:</h3>
<dl>
<dt><code>&#8211;config</code> <i>,/path/to/config/</i></p>
<dd> Specify a path to a custom config file</p>
<dt><code>&#8211;config</code> none</p>
<dd> Launch the script without a config file</p>
<dt><code>&#8211;no_config</code></p>
<dd> Don&#8217;t create the user config file.</p>
<dt><code>&#8211;print_config</code></p>
<dd> Print the default config file to stdout.</p>
<dt><code>&#8211;stdout</code></p>
<dd> Turn off all colors and disables any ASCII/image backend.</p>
<dt><code>&#8211;help</code></p>
<dd> Print this text and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Show neofetch version</p>
<dt><code>-v</code></p>
<dd> Display error messages.</p>
<dt><code>-vv</code></p>
<dd> Display a verbose log for error reporting.</dl>
<h3>DEVELOPER:</h3>
<dl>
<dt><code>&#8211;gen-man</code></p>
<dd> Generate a manpage for Neofetch in your PWD. (Requires GNU help2man)</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/dylanaraps/neofetch/issues">https://github.com/dylanaraps/neofetch/issues</a> </p>
<h2>Index</h2>
