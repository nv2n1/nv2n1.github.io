---

title: "neofetch(1)"
name: "neofetch"
section: "1"
letter: "n"
url: "/docs/linux/man/1-neofetch/"
description: "Neofetch – A fast, highly customizable system info script"
---

<p> <code>neofetch</code> <i>,func_name &#8211;option &quot;value&quot; &#8211;option &quot;value&quot;/</i></p>
<p> Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice. </p>
<p> NOTE: Every launch flag has a config option.</p>
<h2>OPTIONS</h2>
<h3>INFO:</h3>
<dl>
<dt>func_name</dt>
<dd> Specify a function name (second part of info() from config) to quickly display only that function&#8217;s information.</dd>
<dt>
</dt><dd> Example: neofetch uptime <code>&#8211;uptime_shorthand</code> tiny</dd>
<dt>
</dt><dd> Example: neofetch uptime disk wm memory</dd>
<dt>
</dt><dd> This can be used in bars and scripts like so:</dd>
<dt>
</dt><dd> memory=&quot;$(neofetch memory)&quot;; memory=&quot;${memory##*: }&quot;</dd>
<dt>
</dt><dd> For multiple outputs at once (each line of info in an array):</dd>
<dt>
</dt><dd> IFS=$&#8217;
&#8217; read <code>-d</code> &quot;&quot; <code>-ra</code> info &lt; &lt;(neofetch memory uptime wm)</dd>
<dt>
</dt><dd> info=(&quot;${info[@]##*: }&quot;)</dd>
<dt><code>&#8211;disable</code> infoname</dt>
<dd> Allows you to disable an info line from appearing in the output. &#8216;infoname&#8217; is the function name from the &#8216;print_info()&#8217; function inside the config file. For example: &#8216;info &quot;Memory&quot; memory&#8217; would be &#8216;&#8211;disable memory&#8217;</dd>
<dt>
</dt><dd> NOTE: You can supply multiple args. eg. &#8216;neofetch <code>&#8211;disable</code> cpu gpu&#8217;</dd>
<dt><code>&#8211;package_managers</code> on/off</dt>
<dd> Hide/Show Package Manager names . (on, tiny, off)</dd>
<dt><code>&#8211;os_arch</code> on/off</dt>
<dd> Hide/Show OS architecture.</dd>
<dt><code>&#8211;speed_type</code> type</dt>
<dd> Change the type of cpu speed to display. Possible values: current, min, max, bios, scaling_current, scaling_min, scaling_max</dd>
<dt>
</dt><dd> NOTE: This only supports Linux with cpufreq.</dd>
<dt><code>&#8211;speed_shorthand</code> on/off</dt>
<dd> Whether or not to show decimals in CPU speed.</dd>
<dt>NOTE: This flag is not supported in systems with CPU speed less than</dt>
<dd> 1 GHz.</dd>
<dt><code>&#8211;cpu_brand</code> on/off</dt>
<dd> Enable/Disable CPU brand in output.</dd>
<dt><code>&#8211;cpu_cores</code> type</dt>
<dd> Whether or not to display the number of CPU cores Possible values: logical, physical, off</dd>
<dt>
</dt><dd> NOTE: &#8216;physical&#8217; doesn&#8217;t work on BSD.</dd>
<dt><code>&#8211;cpu_speed</code> on/off</dt>
<dd> Hide/Show cpu speed.</dd>
<dt><code>&#8211;cpu_temp</code> C/F/off</dt>
<dd> Hide/Show cpu temperature.</dd>
<dt>
</dt><dd> NOTE: This only works on Linux and BSD.</dd>
<dt>NOTE: For FreeBSD and NetBSD-based systems, you need to enable</dt>
<dd> coretemp kernel module. This only supports newer Intel processors.</dd>
<dt><code>&#8211;distro_shorthand</code> on/off</dt>
<dd> Shorten the output of distro (on, tiny, off)</dd>
<dt>
</dt><dd> NOTE: This option won&#8217;t work in Windows (Cygwin)</dd>
<dt><code>&#8211;kernel_shorthand</code> on/off</dt>
<dd> Shorten the output of kernel</dd>
<dt>
</dt><dd> NOTE: This option won&#8217;t work in BSDs (except PacBSD and PC-BSD)</dd>
<dt><code>&#8211;uptime_shorthand</code> on/off</dt>
<dd> Shorten the output of uptime (on, tiny, off)</dd>
<dt><code>&#8211;refresh_rate</code> on/off</dt>
<dd> Whether to display the refresh rate of each monitor Unsupported on Windows</dd>
<dt><code>&#8211;gpu_brand</code> on/off</dt>
<dd> Enable/Disable GPU brand in output. (AMD/NVIDIA/Intel)</dd>
<dt><code>&#8211;gpu_type</code> type</dt>
<dd> Which GPU to display. (all, dedicated, integrated)</dd>
<dt>
</dt><dd> NOTE: This only supports Linux.</dd>
<dt><code>&#8211;de_version</code> on/off</dt>
<dd> Show/Hide Desktop Environment version</dd>
<dt><code>&#8211;gtk_shorthand</code> on/off</dt>
<dd> Shorten output of gtk theme/icons</dd>
<dt><code>&#8211;gtk2</code> on/off</dt>
<dd> Enable/Disable gtk2 theme/font/icons output</dd>
<dt><code>&#8211;gtk3</code> on/off</dt>
<dd> Enable/Disable gtk3 theme/font/icons output</dd>
<dt><code>&#8211;shell_path</code> on/off</dt>
<dd> Enable/Disable showing $SHELL path</dd>
<dt><code>&#8211;shell_version</code> on/off</dt>
<dd> Enable/Disable showing $SHELL version</dd>
<dt><code>&#8211;disk_show</code> value</dt>
<dd> Which disks to display. Possible values: &#8216;/&#8217;, &#8216;/dev/sdXX&#8217;, &#8216;/path/to/mount point&#8217;</dd>
<dt>
</dt><dd> NOTE: Multiple values can be given. (<code>&#8211;disk_show</code> &#8216;/&#8217; &#8216;/dev/sdc1&#8217;)</dd>
<dt><code>&#8211;disk_subtitle</code> type</dt>
<dd> What information to append to the Disk subtitle. Takes: name, mount, dir, none</dd>
<dt>
</dt><dd> &#8216;name&#8217; shows the disk&#8217;s name (sda1, sda2, etc)</dd>
<dt>
</dt><dd> &#8216;mount&#8217; shows the disk&#8217;s mount point (/, <i>,/mnt/Local/</i> Disk, etc)</dd>
<dt>
</dt><dd> &#8216;dir&#8217; shows the basename of the disks&#8217;s path. (/, Local Disk, etc)</dd>
<dt>
</dt><dd> &#8216;none&#8217; shows only &#8216;Disk&#8217; or the configured title.</dd>
<dt><code>&#8211;disk_percent</code> on/off</dt>
<dd> Hide/Show disk percent.</dd>
<dt><code>&#8211;ip_host</code> url</dt>
<dd> URL to query for public IP</dd>
<dt><code>&#8211;ip_timeout</code> int</dt>
<dd> Public IP timeout (in seconds).</dd>
<dt><code>&#8211;song_format</code> format</dt>
<dd> Print the song data in a specific format (see config file).</dd>
<dt><code>&#8211;song_shorthand</code> on/off</dt>
<dd> Print the Artist/Album/Title on separate lines.</dd>
<dt><code>&#8211;memory_percent</code> on/off</dt>
<dd> Display memory percentage.</dd>
<dt><code>&#8211;music_player</code> player-name</dt>
<dd> Manually specify a player to use. Available values are listed in the config file</dd></dl>
<h3>TEXT FORMATTING:</h3>
<dl>
<dt><code>&#8211;colors</code> x x x x x x</dt>
<dd> Changes the text colors in this order: title, @, underline, subtitle, colon, info</dd>
<dt><code>&#8211;underline</code> on/off</dt>
<dd> Enable/Disable the underline.</dd>
<dt><code>&#8211;underline_char</code> char</dt>
<dd> Character to use when underlining title</dd>
<dt><code>&#8211;bold</code> on/off</dt>
<dd> Enable/Disable bold text</dd>
<dt><code>&#8211;separator</code> string</dt>
<dd> Changes the default &#8216;:&#8217; separator to the specified string.</dd></dl>
<h3>COLOR BLOCKS:</h3>
<dl>
<dt><code>&#8211;color_blocks</code> on/off</dt>
<dd> Enable/Disable the color blocks</dd>
<dt><code>&#8211;col_offset</code> auto/num</dt>
<dd> Left-padding of color blocks</dd>
<dt><code>&#8211;block_width</code> num</dt>
<dd> Width of color blocks in spaces</dd>
<dt><code>&#8211;block_height</code> num</dt>
<dd> Height of color blocks in lines</dd>
<dt><code>&#8211;block_range</code> num num</dt>
<dd> Range of colors to print as blocks</dd></dl>
<h3>BARS:</h3>
<dl>
<dt><code>&#8211;bar_char</code> &#8216;elapsed char&#8217; &#8216;total char&#8217;</dt>
<dd> Characters to use when drawing bars.</dd>
<dt><code>&#8211;bar_border</code> on/off</dt>
<dd> Whether or not to surround the bar with &#8216;[]&#8217;</dd>
<dt><code>&#8211;bar_length</code> num</dt>
<dd> Length in spaces to make the bars.</dd>
<dt><code>&#8211;bar_colors</code> num num</dt>
<dd> Colors to make the bar. Set in this order: elapsed, total</dd>
<dt><code>&#8211;cpu_display</code> mode</dt>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</dd>
<dt><code>&#8211;memory_display</code> mode</dt>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</dd>
<dt><code>&#8211;battery_display</code> mode</dt>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</dd>
<dt><code>&#8211;disk_display</code> mode</dt>
<dd> Bar mode. Possible values: bar, infobar, barinfo, off</dd></dl>
<h3>IMAGE BACKEND:</h3>
<dl>
<dt><code>&#8211;backend</code> backend</dt>
<dd> Which image backend to use. Possible values: &#8216;ascii&#8217;, &#8216;caca&#8217;, &#8216;chafa&#8217;, &#8216;jp2a&#8217;, &#8216;iterm2&#8217;, &#8216;off&#8217;, &#8216;sixel&#8217;, &#8216;tycat&#8217;, &#8216;w3m&#8217;, &#8216;kitty&#8217;</dd>
<dt><code>&#8211;source</code> source</dt>
<dd> Which image or ascii file to use. Possible values: &#8216;auto&#8217;, &#8216;ascii&#8217;, &#8216;wallpaper&#8217;, &#8216;/path/to/img&#8217;, &#8216;/path/to/ascii&#8217;, &#8216;/path/to/dir/&#8217;, &#8216;command output&#8217; [ascii]</dd>
<dt><code>&#8211;ascii</code> source</dt>
<dd> Shortcut to use &#8216;ascii&#8217; backend.</dd>
<dt>
</dt><dd> NEW: neofetch <code>&#8211;ascii</code> &quot;$(fortune | cowsay <code>-W</code> 30)&quot;</dd>
<dt><code>&#8211;caca</code> source</dt>
<dd> Shortcut to use &#8216;caca&#8217; backend.</dd>
<dt><code>&#8211;chafa</code> source</dt>
<dd> Shortcut to use &#8216;chafa&#8217; backend.</dd>
<dt><code>&#8211;iterm2</code> source</dt>
<dd> Shortcut to use &#8216;iterm2&#8217; backend.</dd>
<dt><code>&#8211;jp2a</code> source</dt>
<dd> Shortcut to use &#8216;jp2a&#8217; backend.</dd>
<dt><code>&#8211;kitty</code> source</dt>
<dd> Shortcut to use &#8216;kitty&#8217; backend.</dd>
<dt><code>&#8211;pixterm</code> source</dt>
<dd> Shortcut to use &#8216;pixterm&#8217; backend.</dd>
<dt><code>&#8211;sixel</code> source</dt>
<dd> Shortcut to use &#8216;sixel&#8217; backend.</dd>
<dt><code>&#8211;termpix</code> source</dt>
<dd> Shortcut to use &#8216;termpix&#8217; backend.</dd>
<dt><code>&#8211;tycat</code> source</dt>
<dd> Shortcut to use &#8216;tycat&#8217; backend.</dd>
<dt><code>&#8211;w3m</code> source</dt>
<dd> Shortcut to use &#8216;w3m&#8217; backend.</dd>
<dt><code>&#8211;off</code></dt>
<dd> Shortcut to use &#8216;off&#8217; backend (Disable ascii art).</dd>
<dt>
</dt><dd> NOTE: &#8216;source; can be any of the following: &#8216;auto&#8217;, &#8216;ascii&#8217;, &#8216;wallpaper&#8217;, &#8216;/path/to/img&#8217;, &#8216;/path/to/ascii&#8217;, &#8216;/path/to/dir/&#8217;</dd></dl>
<h3>ASCII:</h3>
<dl>
<dt><code>&#8211;ascii_colors</code> x x x x x x</dt>
<dd> Colors to print the ascii art</dd>
<dt><code>&#8211;ascii_distro</code> distro</dt>
<dd> Which Distro&#8217;s ascii art to print</dd>
<dt>NOTE: AIX, Alpine, Anarchy, Android, Antergos, antiX, AOSC,</dt>
<dd> Apricity, ArcoLinux, ArchBox, ARCHlabs, ArchStrike, XFerience, ArchMerge, Arch, Artix, Arya, Bedrock, Bitrig, BlackArch, BLAG, BlankOn, BlueLight, bonsai, BSD, BunsenLabs, Calculate, Carbs, CentOS, Chakra, ChaletOS, Chapeau, Chrom, Cleanjaro, ClearOS, Clear_Linux, Clover, Condres, Container_Linux, CRUX, Cucumber, Debian, Deepin, DesaOS, Devuan, DracOS, DragonFly, Drauger, Elementary, EndeavourOS, Endless, EuroLinux, Exherbo, Fedora, Feren, FreeBSD, FreeMiNT, Frugalware, Funtoo, GalliumOS, Gentoo, Pentoo, gNewSense, GNU, GoboLinux, Grombyang, Guix, Haiku, Huayra, Hyperbola, janus, Kali, KaOS, KDE_neon, Kibojoe, Kogaion, Korora, KSLinux, Kubuntu, LEDE, LFS, Linux_Lite, LMDE, Lubuntu, Lunar, macos, Mageia, MagpieOS, Mandriva, Manjaro, Maui, Mer, Minix, LinuxMint, MX_Linux, Namib, Neptune, NetBSD, Netrunner, Nitrux, NixOS, Nurunner, NuTyX, OBRevenge, OpenBSD, OpenIndiana, OpenMandriva, OpenWrt, osmc, Oracle, PacBSD, Parabola, Pardus, Parrot, Parsix, TrueOS, PCLinuxOS, Peppermint, popos, Porteus, PostMarketOS, Proxmox, Puppy, PureOS, Qubes, Radix, Raspbian, Reborn_OS, Redstar, Redcore, Redhat, Refracted_Devuan, Regata, Rosa, sabotage, Sabayon, Sailfish, SalentOS, Scientific, Septor, SharkLinux, Siduction, Slackware, SliTaz, SmartOS, Solus, Source_Mage, Sparky, Star, SteamOS, SunOS, openSUSE_Leap, openSUSE_Tumbleweed, openSUSE, SwagArch, Tails, Trisquel, Ubuntu-Budgie, Ubuntu-GNOME, Ubuntu-MATE, Ubuntu-Studio, Ubuntu, Void, Obarun, windows10, Windows7, Xubuntu, Zorin, and IRIX have ascii logos</dd>
<dt>
</dt><dd> NOTE: Arch, Ubuntu, Redhat, and Dragonfly have &#8216;old&#8217; logo variants.</dd>
<dt>
</dt><dd> NOTE: Use &#8216;{distro name}_old&#8217; to use the old logos.</dd>
<dt>
</dt><dd> NOTE: Ubuntu has flavor variants.</dd>
<dt>NOTE: Change this to Lubuntu, Kubuntu, Xubuntu, Ubuntu-GNOME,</dt>
<dd> Ubuntu-Studio, Ubuntu-Mate or Ubuntu-Budgie to use the flavors.</dd>
<dt>NOTE: Arcolinux, Dragonfly, Fedora, Alpine, Arch, Ubuntu,</dt>
<dd> CRUX, Debian, Gentoo, FreeBSD, Mac, NixOS, OpenBSD, android, Antrix, CentOS, Cleanjaro, ElementaryOS, GUIX, Hyperbola, Manjaro, MXLinux, NetBSD, Parabola, POP_OS, PureOS, Slackware, SunOS, LinuxLite, OpenSUSE, Raspbian, postmarketOS, and Void have a smaller logo variant.</dd>
<dt>
</dt><dd> NOTE: Use &#8216;{distro name}_small&#8217; to use the small variants.</dd>
<dt><code>&#8211;ascii_bold</code> on/off</dt>
<dd> Whether or not to bold the ascii logo.</dd>
<dt><code>-L</code>, <code>&#8211;logo</code></dt>
<dd> Hide the info text and only show the ascii logo.</dd></dl>
<h3>IMAGE:</h3>
<dl>
<dt><code>&#8211;loop</code></dt>
<dd> Redraw the image constantly until Ctrl+C is used. This fixes issues in some terminals emulators when using image mode.</dd>
<dt><code>&#8211;size</code> 00px | <code>&#8211;size</code> 00%</dt>
<dd> How to size the image. Possible values: auto, 00px, 00%, none</dd>
<dt><code>&#8211;crop_mode</code> mode</dt>
<dd> Which crop mode to use Takes the values: normal, fit, fill</dd>
<dt><code>&#8211;crop_offset</code> value</dt>
<dd> Change the crop offset for normal mode. Possible values: northwest, north, northeast, west, center, east, southwest, south, southeast</dd>
<dt><code>&#8211;xoffset</code> px</dt>
<dd> How close the image will be to the left edge of the window. This only works with w3m.</dd>
<dt><code>&#8211;yoffset</code> px</dt>
<dd> How close the image will be to the top edge of the window. This only works with w3m.</dd>
<dt><code>&#8211;bg_color</code> color</dt>
<dd> Background color to display behind transparent image. This only works with w3m.</dd>
<dt><code>&#8211;gap</code> num</dt>
<dd> Gap between image and text.</dd>
<dt>NOTE: <code>&#8211;gap</code> can take a negative value which will move the text</dt>
<dd> closer to the left side.</dd>
<dt><code>&#8211;clean</code></dt>
<dd> Delete cached files and thumbnails.</dd></dl>
<h3>OTHER:</h3>
<dl>
<dt><code>&#8211;config</code> <i>,/path/to/config/</i></dt>
<dd> Specify a path to a custom config file</dd>
<dt><code>&#8211;config</code> none</dt>
<dd> Launch the script without a config file</dd>
<dt><code>&#8211;no_config</code></dt>
<dd> Don&#8217;t create the user config file.</dd>
<dt><code>&#8211;print_config</code></dt>
<dd> Print the default config file to stdout.</dd>
<dt><code>&#8211;stdout</code></dt>
<dd> Turn off all colors and disables any ASCII/image backend.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print this text and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show neofetch version</dd>
<dt><code>-v</code></dt>
<dd> Display error messages.</dd>
<dt><code>-vv</code></dt>
<dd> Display a verbose log for error reporting.</dd></dl>
<h3>DEVELOPER:</h3>
<dl>
<dt><code>&#8211;gen-man</code></dt>
<dd> Generate a manpage for Neofetch in your PWD. (Requires GNU help2man)</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/dylanaraps/neofetch/issues">https://github.com/dylanaraps/neofetch/issues</a> </p>
