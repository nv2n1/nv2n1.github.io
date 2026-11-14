---
title: "conky(1)"
name: "conky"
section: "1"
letter: "c"
url: "/docs/linux/man/1-conky/"
description: "conky – A system monitor for X originally based on the torsmo code, but more kickass. It just keeps on given’er. Yeah."
---

<h2>NAME</h2>
<p> conky &#8211; A system monitor for X originally based on the torsmo code, but more kickass. It just keeps on given&#8217;er. Yeah.</p>
<h2>SYNOPSIS</h2>
<p> <code>conky</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Conky is a system monitor for X originally based on torsmo. Since its inception, Conky has changed significantly from its predecessor, while maintaining simplicity and configurability. Conky can display just about anything, either on your root desktop or in its own window. Not only does Conky have many built-in objects, it can also display just about any piece of information by using scripts and other external programs. </p>
<p> Conky has more than 250 built in objects, including support for a plethora of OS stats (uname, uptime, CPU usage, mem usage, disk usage, &quot;top&quot; like process stats, and network monitoring, just to name a few), built in IMAP and POP3 support, built in support for many popular music players (MPD, XMMS2, BMPx, Audacious), and much much more. Conky can display this info either as text, or using simple progress bars and graph widgets, with different fonts and colours. </p>
<p> We are always looking for help, whether its reporting bugs, writing patches, or writing docs. Please use the facilities at SourceForge to make bug reports, feature requests, and submit patches, or stop by #conky on irc.freenode.net if you have questions or want to contribute. </p>
<p> Thanks for your interest in Conky.</p>
<h2>COMPILING</h2>
<p> For users compiling from source on a binary distro, make sure you have the X development libraries installed (Unless you provide configure with &quot;&#8211;disable-x11&quot;). This should be a package along the lines of &quot;libx11-dev&quot; or &quot;xorg-x11-dev&quot; for X11 libs, and similar &quot;-dev&quot; format for the other libs required (depending on your configure options). You should be able to see which extra packages you need to install by reading errors that you get from &#8216;./configure&#8217;. You can enable/disable stuff by giving options to configure, but be careful with disabling. For example: with &#8211;disable-math you won&#8217;t get errors but logarithmic graphs will be normal graphs and gauges will miss their line. </p>
<p> Conky has (for some time) been available in the repositories of most popular distributions. Here are some installation instructions for a few: </p>
<p> Gentoo users &#8212; Conky is in Gentoo&#8217;s Portage&#8230; simply use &quot;emerge app-admin/conky&quot; for installation. </p>
<p> Debian, etc. users &#8212; Conky should be in your repositories, and can be installed by doing &quot;aptitude install conky&quot;. </p>
<p> Example to compile and run Conky with all optional components (note that some configure options may differ for your system):</p>
<dl>
<dt><code>sh autogen.sh</code> <code># Only required if building from the git repo</code></p>
<dd>
<dt><code>./configure</code> <code>&#8211;prefix=/usr &#8211;mandir=/usr/share/man &#8211;infodir=/usr/share/info &#8211;datadir=/usr/share &#8211;sysconfdir=/etc &#8211;localstatedir=/var/lib &#8211;disable-own-window &#8211;enable-audacious[=yes|no|legacy] &#8211;enable-bmpx &#8211;disable-hddtemp &#8211;disable-mpd &#8211;enable-xmms2 &#8211;disable-portmon &#8211;disable-network &#8211;enable-debug &#8211;disable-x11 &#8211;disable-double-buffer &#8211;disable-xdamage &#8211;disable-xft</code></p>
<dd>
<dt><code>make</code></p>
<dd>
<dt><code>make install</code> <code># Optional</code></p>
<dd>
<dt><code>src/conky</code></p>
<dd></dl>
<p> Conky has been tested to be compatible with C99 C, however it has not been tested with anything other than gcc, and is not guaranteed to work with other compilers. </p>
<h2>YOU SHOULD KNOW</h2>
<p> Conky is generally very good on resources. That said, the more you try to make Conky do, the more resources it is going to consume. </p>
<p> An easy way to force Conky to reload your ~/.conkyrc: &quot;killall -SIGUSR1 conky&quot;. Saves you the trouble of having to kill and then restart. You can now also do the same with SIGHUP.</p>
<h2>OPTIONS</h2>
<p> Command line options override configurations defined in configuration file.</p>
<dl>
<dt><code>-v | -V | &#8211;version</code></p>
<dd> Prints version and exits </p>
<dt><code>-q | &#8211;quiet</code></p>
<dd> Run Conky in &#8216;quiet mode&#8217; (ie. no output) </p>
<dt><code>-D | &#8211;debug</code></p>
<dd> Increase debugging output, ie. -DD for more debugging </p>
<dt><code>-a | &#8211;alignment=</code> <code>ALIGNMENT</code></p>
<dd> Text alignment on screen, {top,bottom,middle}_{left,right,middle} or none. Can also be abbreviated with first chars of position, ie. tr for top_right. </p>
<dt><code>-b | &#8211;double-buffer</code></p>
<dd> Use double buffering (eliminates &quot;flicker&quot;) </p>
<dt><code>-c | &#8211;config=</code> <code>FILE</code></p>
<dd> Config file to load instead of $HOME/.conkyrc </p>
<dt><code>-C | &#8211;print-config</code></p>
<dd> Print builtin default config to stdout. See also the section EXAMPLES for more information. </p>
<dt><code>-d | &#8211;daemonize</code></p>
<dd> Daemonize Conky, aka fork to background </p>
<dt><code>-f | &#8211;font=</code> <code>FONT</code></p>
<dd> Font to use </p>
<dt><code>-h | &#8211;help</code></p>
<dd> Prints command line help and exits </p>
<dt><code>-o | &#8211;own-window</code></p>
<dd> Create own window to draw </p>
<dt><code>-t | &#8211;text=</code> <code>TEXT</code></p>
<dd> Text to render, remember single quotes, like -t &#8216; $uptime &#8216; </p>
<dt><code>-p | &#8211;pause=</code> <code>SECONDS</code></p>
<dd> Time to pause before actually starting Conky </p>
<dt><code>-u | &#8211;interval=</code> <code>SECONDS</code></p>
<dd> Update interval </p>
<dt><code>-w | &#8211;window-id=</code> <code>WIN_ID</code></p>
<dd> Window id to draw </p>
<dt><code>-X | &#8211;display=</code> <code>DISPLAY</code></p>
<dd> X11 display to use </p>
<dt><code>-x</code> <code>X_COORDINATE</code></p>
<dd> X position </p>
<dt><code>-y</code> <code>Y_COORDINATE</code></p>
<dd> Y position </p>
<dt><code>-i</code> <code>COUNT</code></p>
<dd> Number of times to update Conky (and quit) </p>
</dl>
<h2>CONFIGURATION SETTINGS</h2>
<p> Default configuration file location is $HOME/.conkyrc or ${sysconfdir}/conky/conky.conf. On most systems, sysconfdir is /etc, and you can find the sample config file there (/etc/conky/conky.conf). </p>
<p> You might want to copy it to $HOME/.conkyrc and then start modifying it. Other configs can be found at <a rel="nofollow" href="http://conky.sf.net/">http://conky.sf.net/</a></p>
<dl>
<dt><code>TEXT</code></p>
<dd> After this begins text to be formatted on screen. Backslash (\) escapes newlines in the text section. This can be useful for cleaning up config files where conky is used to pipe input to dzen2. </p>
<dt><code>alignment</code></p>
<dd> Aligned position on screen, may be top_left, top_right, top_middle, bottom_left, bottom_right, bottom_middle, middle_left, middle_middle, middle_right, or none (also can be abreviated as tl, tr, tm, bl, br, bm, ml, mm, mr). See also gap_x and gap_y. </p>
<dt><code>append_file</code></p>
<dd> Append the file given as argument. </p>
<dt><code>background</code></p>
<dd> Boolean value, if true, Conky will be forked to background when started. </p>
<dt><code>border_inner_margin</code></p>
<dd> Inner border margin in pixels (the margin between the border and text). </p>
<dt><code>border_outer_margin</code></p>
<dd> Outer border margin in pixels (the margin between the border and the edge of the window). </p>
<dt><code>border_width</code></p>
<dd> Border width in pixels. </p>
<dt><code>colorN</code></p>
<dd> Predefine a color for use inside TEXT segments. Substitute N by a digit between 0 and 9, inclusively. When specifying the color value in hex, omit the leading hash (#). </p>
<dt><code>cpu_avg_samples</code></p>
<dd> The number of samples to average for CPU monitoring. </p>
<dt><code>default_bar_size</code></p>
<dd> Specify a default width and height for bars. Example: &#8216;default_bar_size 0 6&#8217;. This is particularly useful for execbar and execibar as they do not take size arguments. </p>
<dt><code>default_color</code></p>
<dd> Default color and border color </p>
<dt><code>default_gauge_size</code></p>
<dd> Specify a default width and height for gauges. Example: &#8216;default_gauge_size 25 25&#8217;. This is particularly useful for execgauge and execigauge as they do not take size arguments </p>
<dt><code>default_graph_size</code></p>
<dd> Specify a default width and height for graphs. Example: &#8216;default_graph_size 0 25&#8217;. This is particularly useful for execgraph and execigraph as they do not take size arguments </p>
<dt><code>default_outline_color</code></p>
<dd> Default outline color </p>
<dt><code>default_shade_color</code></p>
<dd> Default shading color and border&#8217;s shading color </p>
<dt><code>disable_auto_reload</code></p>
<dd> Enable to disable the inotify-based auto config reload feature. </p>
<dt><code>diskio_avg_samples</code></p>
<dd> The number of samples to average for disk I/O monitoring. </p>
<dt><code>display</code></p>
<dd> Specify an X display to connect to. </p>
<dt><code>double_buffer</code></p>
<dd> Use the Xdbe extension? (eliminates flicker) It is highly recommended to use own window with this one so double buffer won&#8217;t be so big. </p>
<dt><code>draw_borders</code></p>
<dd> Draw borders around text? </p>
<dt><code>draw_graph_borders</code></p>
<dd> Draw borders around graphs? </p>
<dt><code>draw_outline</code></p>
<dd> Draw outlines? </p>
<dt><code>draw_shades</code></p>
<dd> Draw shades? </p>
<dt><code>extra_newline</code></p>
<dd> Put an extra newline at the end when writing to stdout, useful for writing to awesome&#8217;s wiboxes. </p>
<dt><code>font</code></p>
<dd> Font name in X, xfontsel can be used to get a nice font </p>
<dt><code>format_human_readable</code></p>
<dd> If enabled, values which are in bytes will be printed in human readable format (i.e., KiB, MiB, etc). If disabled, the number of bytes is printed instead. </p>
<dt><code>gap_x</code></p>
<dd> Gap, in pixels, between right or left border of screen, same as passing -x at command line, e.g. gap_x 10. For other position related stuff, see &#8216;alignment&#8217;. </p>
<dt><code>gap_y</code></p>
<dd> Gap, in pixels, between top or bottom border of screen, same as passing -y at command line, e.g. gap_y 10. For other position related stuff, see &#8216;alignment&#8217;. </p>
<dt><code>hddtemp_host</code></p>
<dd> Hostname to connect to for hddtemp objects. Defaults to &quot;127.0.0.1&quot;. </p>
<dt><code>hddtemp_port</code></p>
<dd> Port to use for hddtemp connections. Defaults to 7634. </p>
<dt><code>if_up_strictness</code></p>
<dd> How strict should if_up be when testing an interface for being up? The value is one of up, link or address, to check for the interface being solely up, being up and having link or being up, having link and an assigned IP address. </p>
<dt><code>imap</code></p>
<dd> Default global IMAP server. Arguments are: &quot;host user pass [-i interval (in seconds)] [-f &#8216;folder&#8217;] [-p port] [-e &#8216;command&#8217;] [-r retries]&quot;. Default port is 143, default folder is &#8216;INBOX&#8217;, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as &#8216;*&#8217;, you will be prompted to enter the password when Conky starts. </p>
<dt><code>imlib_cache_flush_interval</code></p>
<dd> Interval (in seconds) to flush Imlib2 cache. </p>
<dt><code>imlib_cache_size</code></p>
<dd> Imlib2 image cache size, in bytes. Defaults to 4MiB. Increase this value if you use $image lots. Set to 0 to disable the image cache. </p>
<dt><code>imlib_image_alpha</code></p>
<dd> Boolean, use transparency for images? Enabled by default. If own_window_visual_argb is enabled, images appear transparent; disable this option to make images appear opaque. </p>
<dt><code>lua_draw_hook_post</code> <code>function_name [function arguments]</code></p>
<dd> This function, if defined, will be called by Conky through each iteration after drawing to the window. Requires X support. Takes any number of optional arguments. Use this hook for drawing things on top of what Conky draws. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>lua_draw_hook_pre</code> <code>function_name [function arguments]</code></p>
<dd> This function, if defined, will be called by Conky through each iteration before drawing to the window. Requires X support. Takes any number of optional arguments. Use this hook for drawing things on top of what Conky draws. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>lua_load</code></p>
<dd> Loads the Lua scripts separated by spaces. </p>
<dt><code>lua_shutdown_hook</code> <code>function_name [function arguments]</code></p>
<dd> This function, if defined, will be called by Conky at shutdown or when the configuration is reloaded. Use this hook to clean up after yourself, such as freeing memory which has been allocated by external libraries via Lua. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>lua_startup_hook</code> <code>function_name [function arguments]</code></p>
<dd> This function, if defined, will be called by Conky at startup or when the configuration is reloaded. Use this hook to initialize values, or for any run-once applications. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>mail_spool</code></p>
<dd> Mail spool for mail checking </p>
<dt><code>max_port_monitor_connections</code></p>
<dd> Allow each port monitor to track at most this many connections (if 0 or not set, default is 256) </p>
<dt><code>max_specials</code></p>
<dd> Maximum number of special things, e.g. fonts, offsets, aligns, etc. (default is 512) </p>
<dt><code>max_text_width</code> <code>width</code></p>
<dd> When a line in the output contains &#8216;width&#8217; chars and the end isn&#8217;t reached, the next char will start on a new line. If you want to make sure that lines don&#8217;t get broken, set &#8216;width&#8217; to 0 </p>
<dt><code>max_user_text</code> <code>bytes</code></p>
<dd> Maximum size of user text buffer, i.e. layout below TEXT line in config file (default is 16384 bytes) </p>
<dt><code>maximum_width</code> <code>pixels</code></p>
<dd> Maximum width of window </p>
<dt><code>minimum_size</code> <code>width (height)</code></p>
<dd> Minimum size of window </p>
<dt><code>mpd_host</code></p>
<dd> Host of MPD server </p>
<dt><code>mpd_password</code></p>
<dd> MPD server password </p>
<dt><code>mpd_port</code></p>
<dd> Port of MPD server </p>
<dt><code>music_player_interval</code></p>
<dd> Music player thread update interval (defaults to Conky&#8217;s update interval) </p>
<dt><code>net_avg_samples</code></p>
<dd> The number of samples to average for net data </p>
<dt><code>no_buffers</code></p>
<dd> Subtract (file system) buffers from used memory? </p>
<dt><code>nvidia_display</code></p>
<dd> The display that the nvidia variable will use (defaults to the value of the display variable) </p>
<dt><code>out_to_console</code></p>
<dd> Print text to stdout. </p>
<dt><code>out_to_ncurses</code></p>
<dd> Print text in the console, but use ncurses so that conky can print the text of a new update over the old text. (In the future this will provide more useful things) </p>
<dt><code>out_to_stderr</code></p>
<dd> Print text to stderr. </p>
<dt><code>out_to_x</code></p>
<dd> When set to no, there will be no output in X (useful when you also use things like out_to_console). If you set it to no, make sure that it&#8217;s placed before all other X-related setting (take the first line of your configfile to be sure). Default value is yes </p>
<dt><code>override_utf8_locale</code></p>
<dd> Force UTF8? requires XFT </p>
<dt><code>overwrite_file</code></p>
<dd> Overwrite the file given as argument. </p>
<dt><code>own_window</code></p>
<dd> Boolean, create own window to draw? </p>
<dt><code>own_window_class</code></p>
<dd> Manually set the WM_CLASS name. Defaults to &quot;Conky&quot;. </p>
<dt><code>own_window_colour</code> <code>colour</code></p>
<dd> If own_window_transparent no, set a specified background colour (defaults to black). Takes either a hex value (e.g. ffffff, note the lack of &#8216;#&#8217;) or a valid RGB name (see /usr/lib/X11/rgb.txt) </p>
<dt><code>own_window_hints</code> <code>undecorated,below,above,sticky,skip_taskbar,skip_pager</code></p>
<dd> If own_window is yes, you may use these window manager hints to affect the way Conky displays. Notes: Use own_window_type desktop as another way to implement many of these hints implicitly. If you use own_window_type override, window manager hints have no meaning and are ignored. </p>
<dt><code>own_window_title</code></p>
<dd> Manually set the window name. Defaults to &quot;&lt;hostname&gt; &#8211; conky&quot;. </p>
<dt><code>own_window_argb_visual</code></p>
<dd> Boolean, use ARGB visual? ARGB can be used for real transparency, note that a composite manager is required for real transparency. This option will not work as desired (in most cases) in conjunction with &#8216;own_window_type override&#8217;. </p>
<dt><code>own_window_argb_value</code></p>
<dd> When ARGB visuals are enabled, this use this to modify the alpha value used. Valid range is 0-255, where 0 is 0% opacity, and 255 is 100% opacity. </p>
<dt><code>own_window_transparent</code></p>
<dd> Boolean, set transparency? If ARGB visual is enabled, sets background opacity to 0%. </p>
<dt><code>own_window_type</code></p>
<dd> if own_window is yes, you may specify type normal, desktop, dock, panel or override (default: normal). Desktop windows are special windows that have no window decorations; are always visible on your desktop; do not appear in your pager or taskbar; and are sticky across all workspaces. Panel windows reserve space along a desktop edge, just like panels and taskbars, preventing maximized windows from overlapping them. The edge is chosen based on the alignment option. Override windows are not under the control of the window manager. Hints are ignored. This type of window can be useful for certain situations. </p>
<dt><code>pad_percents</code></p>
<dd> Pad percentages to this many decimals (0 = no padding) </p>
<dt><code>pop3</code></p>
<dd> Default global POP3 server. Arguments are: &quot;host user pass [-i interval (in seconds)] [-p port] [-e &#8216;command&#8217;] [-r retries]&quot;. Default port is 110, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as &#8216;*&#8217;, you will be prompted to enter the password when Conky starts. </p>
<dt><code>short_units</code></p>
<dd> Shortens units to a single character (kiB-&gt;k, GiB-&gt;G, etc.). Default is off. </p>
<dt><code>show_graph_range</code></p>
<dd> Shows the time range covered by a graph. </p>
<dt><code>show_graph_scale</code></p>
<dd> Shows the maximum value in scaled graphs. </p>
<dt><code>stippled_borders</code></p>
<dd> Border stippling (dashing) in pixels </p>
<dt><code>temperature_unit</code></p>
<dd> Desired output unit of all objects displaying a temperature. Parameters are either &quot;fahrenheit&quot; or &quot;celsius&quot;. The default unit is degree Celsius. </p>
<dt><code>templateN</code></p>
<dd> Define a template for later use inside TEXT segments. Substitute N by a digit between 0 and 9, inclusively. The value of the variable is being inserted into the stuff below TEXT at the corresponding position, but before some substitutions are applied: </p>
<p> &#8216;
&#8217; -&gt; newline<br />
 &#8216;\&#8217; -&gt; backslash<br />
 &#8216;\ &#8216; -&gt; space<br />
 &#8216;\N&#8217; -&gt; template argument N </p>
<dt><code>text_buffer_size</code> <code>bytes</code></p>
<dd> Size of the standard text buffer (default is 256 bytes). This buffer is used for intermediary text, such as individual lines, output from $exec vars, and various other variables. Increasing the size of this buffer can drastically reduce Conky&#8217;s performance, but will allow for more text display per variable. The size of this buffer cannot be smaller than the default value of 256 bytes. </p>
<dt><code>times_in_seconds</code></p>
<dd> If true, variables that output times output a number that represents seconds. This doesn&#8217;t affect $time, $tztime and $utime </p>
<dt><code>top_cpu_separate</code></p>
<dd> If true, cpu in top will show usage of one processor&#8217;s power. If false, cpu in top will show the usage of all processors&#8217; power combined. </p>
<dt><code>top_name_width</code></p>
<dd> Width for $top name value (defaults to 15 characters). </p>
<dt><code>total_run_times</code></p>
<dd> Total number of times for Conky to update before quitting. Zero makes Conky run forever </p>
<dt><code>update_interval</code> <code>seconds</code></p>
<dd> Update interval </p>
<dt><code>update_interval_on_battery</code> <code>seconds</code></p>
<dd> Update interval when running on batterypower </p>
<dt><code>uppercase</code></p>
<dd> Boolean value, if true, text is rendered in upper case </p>
<dt><code>use_spacer</code></p>
<dd> Adds spaces around certain objects to stop them from moving other things around. Arguments are left, right, and none (default). The old true/false values are deprecated and default to right/none respectively. Note that this only helps if you are using a mono font, such as Bitstream Vera Sans Mono. </p>
<dt><code>use_xft</code></p>
<dd> Use Xft (anti-aliased font and stuff) </p>
<dt><code>xftalpha</code></p>
<dd> Alpha of Xft font. Must be a value at or between 1 and 0. </p>
<dt><code>xftfont</code></p>
<dd> Xft font to use. </p>
</dl>
<h2>OBJECTS/VARIABLES</h2>
<p> Colours are parsed using XParsecolor(), there might be a list of them: /usr/share/X11/rgb.txt. Colour can be also in #rrggbb format (hex). </p>
<p> Some objects may create threads, and sometimes these threads will not be destroyed until Conky terminates. There is no way to destroy or clean up threads while Conky is running. For example, if you use an MPD variable, the MPD thread will keep running until Conky dies. Some threaded objects will use one of the parameters as a &#8216;key&#8217;, so that you only have 1 relevant thread running (for example, the $curl, $rss and $weather objects launch one thread per URI).</p>
<dl>
<dt><code>acpiacadapter</code> <code>(adapter)</code></p>
<dd> ACPI ac adapter state. On linux, the adapter option specifies the subfolder of /sys/class/power_supply containing the state information (tries &quot;AC&quot; and &quot;ADP1&quot; if there is no argument given). Non-linux systems ignore it. </p>
<dt><code>acpifan</code></p>
<dd> ACPI fan state </p>
<dt><code>acpitemp</code></p>
<dd> ACPI temperature in C. </p>
<dt><code>addr</code> <code>(interface)</code></p>
<dd> IP address for an interface, or &quot;No Address&quot; if no address is assigned. </p>
<dt><code>addrs</code> <code>(interface)</code></p>
<dd> IP addresses for an interface (if one &#8211; works like addr). Linux only. </p>
<dt><code>adt746xcpu</code></p>
<dd> CPU temperature from therm_adt746x </p>
<dt><code>adt746xfan</code></p>
<dd> Fan speed from therm_adt746x </p>
<dt><code>alignc</code> <code>(num)</code></p>
<dd> Align text to centre </p>
<dt><code>alignr</code> <code>(num)</code></p>
<dd> Right-justify text, with space of N </p>
<dt><code>apcupsd</code> <code>host</code> <code>port</code></p>
<dd> Sets up the connection to apcupsd daemon. Prints nothing, defaults to localhost:3551 </p>
<dt><code>apcupsd_cable</code></p>
<dd> Prints the UPS connection type. </p>
<dt><code>apcupsd_charge</code></p>
<dd> Current battery capacity in percent. </p>
<dt><code>apcupsd_lastxfer</code></p>
<dd> Reason for last transfer from line to battery. </p>
<dt><code>apcupsd_linev</code></p>
<dd> Nominal input voltage. </p>
<dt><code>apcupsd_load</code></p>
<dd> Current load in percent. </p>
<dt><code>apcupsd_loadbar</code></p>
<dd> Bar showing current load. </p>
<dt><code>apcupsd_loadgauge</code> <code>(height),(width)</code></p>
<dd> Gauge that shows current load. </p>
<dt><code>apcupsd_loadgraph</code> <code>(height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> History graph of current load. </p>
<dt><code>apcupsd_model</code></p>
<dd> Prints the model of the UPS. </p>
<dt><code>apcupsd_name</code></p>
<dd> Prints the UPS user-defined name. </p>
<dt><code>apcupsd_status</code></p>
<dd> Prints current status (on-line, on-battery). </p>
<dt><code>apcupsd_temp</code></p>
<dd> Current internal temperature. </p>
<dt><code>apcupsd_timeleft</code></p>
<dd> Time left to run on battery. </p>
<dt><code>apcupsd_upsmode</code></p>
<dd> Prints the UPS mode (e.g. standalone). </p>
<dt><code>apm_adapter</code></p>
<dd> Display APM AC adapter status (FreeBSD only) </p>
<dt><code>apm_battery_life</code></p>
<dd> Display APM battery life in percent (FreeBSD only) </p>
<dt><code>apm_battery_time</code></p>
<dd> Display remaining APM battery life in hh:mm:ss or &quot;unknown&quot; if AC adapterstatus is on-line or charging (FreeBSD only) </p>
<dt><code>audacious_bar</code> <code>(height),(width)</code></p>
<dd> Progress bar </p>
<dt><code>audacious_bitrate</code></p>
<dd> Bitrate of current tune </p>
<dt><code>audacious_channels</code></p>
<dd> Number of audio channels of current tune </p>
<dt><code>audacious_filename</code></p>
<dd> Full path and filename of current tune </p>
<dt><code>audacious_frequency</code></p>
<dd> Sampling frequency of current tune </p>
<dt><code>audacious_length</code></p>
<dd> Total length of current tune as MM:SS </p>
<dt><code>audacious_length_seconds</code></p>
<dd> Total length of current tune in seconds </p>
<dt><code>audacious_main_volume</code></p>
<dd> The current volume fetched from Audacious </p>
<dt><code>audacious_playlist_length</code></p>
<dd> Number of tunes in playlist </p>
<dt><code>audacious_playlist_position</code></p>
<dd> Playlist position of current tune </p>
<dt><code>audacious_position</code></p>
<dd> Position of current tune (MM:SS) </p>
<dt><code>audacious_position_seconds</code></p>
<dd> Position of current tune in seconds </p>
<dt><code>audacious_status</code></p>
<dd> Player status (Playing/Paused/Stopped/Not running) </p>
<dt><code>audacious_title</code> <code>(max length)</code></p>
<dd> Title of current tune with optional maximum length specifier </p>
<dt><code>battery</code> <code>(num)</code></p>
<dd> Battery status and remaining percentage capacity of ACPI or APM battery. ACPI battery number can be given as argument (default is BAT0). </p>
<dt><code>battery_bar</code> <code>(height),(width) (num)</code></p>
<dd> Battery percentage remaining of ACPI battery in a bar. ACPI battery number can be given as argument (default is BAT0). </p>
<dt><code>battery_percent</code> <code>(num)</code></p>
<dd> Battery percentage remaining for ACPI battery. ACPI battery number can be given as argument (default is BAT0). </p>
<dt><code>battery_short</code> <code>(num)</code></p>
<dd> Battery status and remaining percentage capacity of ACPI or APM battery. ACPI battery number can be given as argument (default is BAT0). This mode display a short status, which means that C is displayed instead of charging, D for discharging, F for full, N for not present, E for empty and U for unknown. </p>
<dt><code>battery_time</code> <code>(num)</code></p>
<dd> Battery charge/discharge time remaining of ACPI battery. ACPI battery number can be given as argument (default is BAT0). </p>
<dt><code>blink</code> <code>text_and_other_conky_vars</code></p>
<dd> Let &#8216;text_and_other_conky_vars&#8217; blink on and off. </p>
<dt><code>bmpx_album</code></p>
<dd> Album in current BMPx track </p>
<dt><code>bmpx_artist</code></p>
<dd> Artist in current BMPx track </p>
<dt><code>bmpx_bitrate</code></p>
<dd> Bitrate of the current BMPx track </p>
<dt><code>bmpx_title</code></p>
<dd> Title of the current BMPx track </p>
<dt><code>bmpx_track</code></p>
<dd> Track number of the current BMPx track </p>
<dt><code>bmpx_uri</code></p>
<dd> URI of the current BMPx track </p>
<dt><code>buffers</code></p>
<dd> Amount of memory buffered </p>
<dt><code>cached</code></p>
<dd> Amount of memory cached </p>
<dt><code>cat</code> <code>file</code></p>
<dd> Reads a file and displays the contents in conky. This is useful if you have an independent process generating output that you want to include in conky. </p>
<dt><code>catp</code> <code>file</code></p>
<dd> Reads a file and displays the contents in conky. This is useful if you have an independent process generating output that you want to include in conky. This differs from $cat in that it parses the contents of the file, so you can insert things like ${color red}hi!${color} in your file and have it correctly parsed by Conky. </p>
<dt><code>cmdline_to_pid</code> <code>string</code></p>
<dd> PID of the first process that has string in it&#8217;s commandline </p>
<dt><code>color</code> <code>(color)</code></p>
<dd> Change drawing color to &#8216;color&#8217; which is a name of a color or a hexcode preceded with # (for example #0A1B2C ). If you use ncurses only the following colors are supported: red,green,yellow,blue,magenta,cyan,black,white. </p>
<dt><code>colorN</code></p>
<dd> Change drawing color to colorN configuration option, where N is a digit between 0 and 9, inclusively. </p>
<dt><code>combine</code> <code>var1 var2</code></p>
<dd> Places the lines of var2 to the right of the lines of var1 separated by the chars that are put between var1 and var2. For example: ${combine ${head /proc/cpuinfo 2} &#8211; ${head /proc/meminfo 1}} gives as output &quot;cpuinfo_line1 &#8211; meminfo_line1&quot; on line 1 and &quot;cpuinfo_line2 -&quot; on line 2. $combine vars can also be nested to place more vars next to each other. </p>
<dt><code>conky_build_arch</code></p>
<dd> CPU architecture Conky was built for </p>
<dt><code>conky_build_date</code></p>
<dd> Date Conky was built </p>
<dt><code>conky_version</code></p>
<dd> Conky version </p>
<dt><code>cpu</code> <code>(cpuN)</code></p>
<dd> CPU usage in percents. For SMP machines, the CPU number can be provided as an argument. ${cpu cpu0} is the total usage, and ${cpu cpuX} (X &gt;= 1) are individual CPUs. </p>
<dt><code>cpubar</code> <code>(cpuN) (height),(width)</code></p>
<dd> Bar that shows CPU usage, height is bar&#8217;s height in pixels. See $cpu for more info on SMP. </p>
<dt><code>cpugauge</code> <code>(cpuN) (height),(width)</code></p>
<dd> Elliptical gauge that shows CPU usage, height and width are gauge&#8217;s vertical and horizontal axis respectively. See $cpu for more info on SMP. </p>
<dt><code>cpugraph</code> <code>(cpuN) (height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> CPU usage graph, with optional colours in hex, minus the #. See $cpu for more info on SMP. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>curl</code> <code>url (interval_in_minutes)</code></p>
<dd> Download data from URI using Curl at the specified interval. The interval may be a floating point value greater than 0, otherwise defaults to 15 minutes. Most useful when used in conjunction with Lua and the Lua API. This object is threaded, and once a thread is created it can&#8217;t be explicitly destroyed. One thread will run for each URI specified. You can use any protocol that Curl supports.</p>
<dt><code>desktop</code></p>
<dd> Number of the desktop on which conky is running or the message &quot;Not running in X&quot; if this is the case. </p>
<dt><code>desktop_name</code></p>
<dd> Name of the desktop on which conky is running or the message &quot;Not running in X&quot; if this is the case. </p>
<dt><code>desktop_number</code></p>
<dd> Number of desktops or the message &quot;Not running in X&quot; if this is the case. </p>
<dt><code>disk_protect</code> <code>device</code></p>
<dd> Disk protection status, if supported (needs kernel-patch). Prints either &quot;frozen&quot; or &quot;free &quot; (note the padding). </p>
<dt><code>diskio</code> <code>(device)</code></p>
<dd> Displays current disk IO. Device is optional, and takes the form of sda for /dev/sda. Individual partitions are allowed. </p>
<dt><code>diskio_read</code> <code>(device)</code></p>
<dd> Displays current disk IO for reads. Device as in diskio. </p>
<dt><code>diskio_write</code> <code>(device)</code></p>
<dd> Displays current disk IO for writes. Device as in diskio. </p>
<dt><code>diskiograph</code> <code>(device) (height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Disk IO graph, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>diskiograph_read</code> <code>(device) (height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Disk IO graph for reads, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Device as in diskio. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>diskiograph_write</code> <code>(device) (height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Disk IO graph for writes, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Device as in diskio. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>downspeed</code> <code>(net)</code></p>
<dd> Download speed in suitable IEC units </p>
<dt><code>downspeedf</code> <code>(net)</code></p>
<dd> Download speed in KiB with one decimal </p>
<dt><code>downspeedgraph</code> <code>(netdev) (height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Download speed graph, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>draft_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails marked as draft in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>else</code></p>
<dd> Text to show if any of the above are not true </p>
<dt><code>endif</code></p>
<dd> Ends an $if block. </p>
<dt><code>entropy_avail</code></p>
<dd> Current entropy available for crypto freaks </p>
<dt><code>entropy_bar</code> <code>(height),(width)</code></p>
<dd> Normalized bar of available entropy for crypto freaks </p>
<dt><code>entropy_perc</code></p>
<dd> Percentage of entropy available in comparison to the poolsize </p>
<dt><code>entropy_poolsize</code></p>
<dd> Total size of system entropy pool for crypto freaks </p>
<dt><code>eval</code> <code>string</code></p>
<dd> Evaluates given string according to the rules of TEXT interpretation, i.e. parsing any contained text object specifications into their output, any occuring &#8216;$$&#8217; into a single &#8216;$&#8217; and so on. The output is then being parsed again. </p>
<dt><code>eve</code> <code>api_userid api_key character_id</code></p>
<dd> Fetches your currently training skill from the Eve Online API servers (<a rel="nofollow" href="http://www.eve-online.com/)">http://www.eve-online.com/)</a> and displays the skill along with the remaining training time. </p>
<dt><code>exec</code> <code>command</code></p>
<dd> Executes a shell command and displays the output in conky. warning: this takes a lot more resources than other variables. I&#8217;d recommend coding wanted behaviour in C and posting a patch. </p>
<dt><code>execbar</code> <code>command</code></p>
<dd> Same as exec, except if the first value return is a value between 0-100, it will use that number for a bar. The size for bars can be controlled via the default_bar_size config setting. </p>
<dt><code>execgauge</code> <code>command</code></p>
<dd> Same as exec, except if the first value returned is a value between 0-100, it will use that number for a gauge. The size for gauges can be controlled via the default_gauge_size config setting. </p>
<dt><code>execgraph</code> <code>(-t) (-l) command</code></p>
<dd> Same as execbar, but graphs values. Uses a logaritmic scale when the log option (-l switch) is given (to see small numbers). Values still have to be between 0 and 100. The size for graphs can be controlled via the default_graph_size config setting. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). If -t or -l is your first argument, you may need to preceed it by a space (&#8216; &#8216;). </p>
<dt><code>execi</code> <code>interval command</code></p>
<dd> Same as exec but with specific interval. Interval can&#8217;t be less than update_interval in configuration. See also $texeci </p>
<dt><code>execibar</code> <code>interval command</code></p>
<dd> Same as execbar, except with an interval </p>
<dt><code>execigauge</code> <code>interval command</code></p>
<dd> Same as execgauge, but takes an interval arg and gauges values. </p>
<dt><code>execigraph</code> <code>interval (-t) (-l) command</code></p>
<dd> Same as execgraph, but takes an interval arg and graphs values. If -t or -l is your first argument, you may need to preceed it by a space (&#8216; &#8216;). </p>
<dt><code>execp</code> <code>command</code></p>
<dd> Executes a shell command and displays the output in conky. warning: this takes a lot more resources than other variables. I&#8217;d recommend coding wanted behaviour in C and posting a patch. This differs from $exec in that it parses the output of the command, so you can insert things like ${color red}hi!${color} in your script and have it correctly parsed by Conky. Caveats: Conky parses and evaluates the output of $execp every time Conky loops, and then destroys all the objects. If you try to use anything like $execi within an $execp statement, it will functionally run at the same interval that the $execp statement runs, as it is created and destroyed at every interval. </p>
<dt><code>execpi</code> <code>interval command</code></p>
<dd> Same as execp but with specific interval. Interval can&#8217;t be less than update_interval in configuration. Note that the output from the $execpi command is still parsed and evaluated at every interval. </p>
<dt><code>flagged_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails marked as flagged in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>font</code> <code>(font)</code></p>
<dd> Specify a different font. This new font will apply to the current line and everything following. You can use a $font with no arguments to change back to the default font (much like with $color) </p>
<dt><code>format_time</code> <code>seconds format</code></p>
<dd> Format time given in seconds. This var only works when the times_in_seconds configuration setting is on. Format is a string that should start and end with a &quot;-char. The &quot;-chars are not part of the output, \w,\d,\h,\m,\s,\(,\) and \ are replaced by weeks,days,hours,minutes,seconds,(,) and \. If you leave out a unit, it&#8217;s value will be expressed in the highest unite lower then the one left out. Text between ()-chars will not be visible if a replaced unit in this text is 0. If seconds is a decimal number then you can see the numbers behind the point by using \S followed by a number that specifies the amount of digits behind the point that you want to see (maximum 9). You can also place a &#8216;x&#8217; behind \S so you have all digits behind the point and no trailing zero&#8217;s. (also maximum 9) </p>
<dt><code>forwarded_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails marked as forwarded in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>freq</code> <code>(n)</code></p>
<dd> Returns CPU #n&#8217;s frequency in MHz. CPUs are counted from 1. If omitted, the parameter defaults to 1. </p>
<dt><code>freq_g</code> <code>(n)</code></p>
<dd> Returns CPU #n&#8217;s frequency in GHz. CPUs are counted from 1. If omitted, the parameter defaults to 1. </p>
<dt><code>fs_bar</code> <code>(height),(width) fs</code></p>
<dd> Bar that shows how much space is used on a file system. height is the height in pixels. fs is any file on that file system. </p>
<dt><code>fs_bar_free</code> <code>(height),(width) fs</code></p>
<dd> Bar that shows how much space is free on a file system. height is the height in pixels. fs is any file on that file system. </p>
<dt><code>fs_free</code> <code>(fs)</code></p>
<dd> Free space on a file system available for users. </p>
<dt><code>fs_free_perc</code> <code>(fs)</code></p>
<dd> Free percentage of space on a file system available for users. </p>
<dt><code>fs_size</code> <code>(fs)</code></p>
<dd> File system size. </p>
<dt><code>fs_type</code> <code>(fs)</code></p>
<dd> File system type. </p>
<dt><code>fs_used</code> <code>(fs)</code></p>
<dd> File system used space. </p>
<dt><code>fs_used_perc</code> <code>(fs)</code></p>
<dd> Percent of file system used space. </p>
<dt><code>goto</code> <code>x</code></p>
<dd> The next element will be printed at position &#8216;x&#8217;. </p>
<dt><code>gw_iface</code></p>
<dd> Displays the default route&#8217;s interface or &quot;multiple&quot;/&quot;none&quot; accordingly. </p>
<dt><code>gw_ip</code></p>
<dd> Displays the default gateway&#8217;s IP or &quot;multiple&quot;/&quot;none&quot; accordingly. </p>
<dt><code>hddtemp</code> <code>(dev)</code></p>
<dd> Displays temperature of a selected hard disk drive as reported by the hddtemp daemon. Use hddtemp_host and hddtemp_port to specify a host and port for all hddtemp objects. If no dev parameter is given, the first disk returned by the hddtemp daemon is used. </p>
<dt><code>head</code> <code>logfile lines (next_check)</code></p>
<dd> Displays first N lines of supplied text file. The file is checked every &#8216;next_check&#8217; update. If next_check is not supplied, Conky defaults to 2. Max of 30 lines can be displayed, or until the text buffer is filled. </p>
<dt><code>hr</code> <code>(height)</code></p>
<dd> Horizontal line, height is the height in pixels </p>
<dt><code>hwmon</code> <code>(dev) type n (factor offset)</code></p>
<dd> Hwmon sensor from sysfs (Linux 2.6). Parameter dev may be omitted if you have only one hwmon device. Parameter type is either &#8216;in&#8217; or &#8216;vol&#8217; meaning voltage; &#8216;fan&#8217; meaning fan; &#8216;temp&#8217; meaning temperature. Parameter n is number of the sensor. See /sys/class/hwmon/ on your local computer. The optional arguments &#8216;factor&#8217; and &#8216;offset&#8217; allow precalculation of the raw input, which is being modified as follows: &#8216;input = input * factor + offset&#8217;. Note that they have to be given as decimal values (i.e. contain at least one decimal place). </p>
<dt><code>i2c</code> <code>(dev) type n (factor offset)</code></p>
<dd> I2C sensor from sysfs (Linux 2.6). Parameter dev may be omitted if you have only one I2C device. Parameter type is either &#8216;in&#8217; or &#8216;vol&#8217; meaning voltage; &#8216;fan&#8217; meaning fan; &#8216;temp&#8217; meaning temperature. Parameter n is number of the sensor. See /sys/bus/i2c/devices/ on your local computer. The optional arguments &#8216;factor&#8217; and &#8216;offset&#8217; allow precalculation of the raw input, which is being modified as follows: &#8216;input = input * factor + offset&#8217;. Note that they have to be given as decimal values (i.e. contain at least one decimal place). </p>
<dt><code>i8k_ac_status</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays whether ac power is on, as listed in /proc/i8k (translated to human-readable). Beware that this is by default not enabled by i8k itself. </p>
<dt><code>i8k_bios</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the bios version as listed in /proc/i8k. </p>
<dt><code>i8k_buttons_status</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the volume buttons status as listed in /proc/i8k. </p>
<dt><code>i8k_cpu_temp</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the cpu temperature in Celsius, as reported by /proc/i8k. </p>
<dt><code>i8k_left_fan_rpm</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the left fan&#8217;s rate of rotation, in revolutions per minute as listed in /proc/i8k. Beware, some laptops i8k reports these fans in reverse order. </p>
<dt><code>i8k_left_fan_status</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the left fan status as listed in /proc/i8k (translated to human-readable). Beware, some laptops i8k reports these fans in reverse order. </p>
<dt><code>i8k_right_fan_rpm</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the right fan&#8217;s rate of rotation, in revolutions per minute as listed in /proc/i8k. Beware, some laptops i8k reports these fans in reverse order. </p>
<dt><code>i8k_right_fan_status</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the right fan status as listed in /proc/i8k (translated to human-readable). Beware, some laptops i8k reports these fans in reverse order. </p>
<dt><code>i8k_serial</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays your laptop serial number as listed in /proc/i8k. </p>
<dt><code>i8k_version</code></p>
<dd> If running the i8k kernel driver for Inspiron laptops, displays the version formatting of /proc/i8k. </p>
<dt><code>ibm_brightness</code></p>
<dd> If running the IBM ACPI, displays the brigtness of the laptops&#8217;s LCD (0-7). </p>
<dt><code>ibm_fan</code></p>
<dd> If running the IBM ACPI, displays the fan speed. </p>
<dt><code>ibm_temps</code> <code>N</code></p>
<dd> If running the IBM ACPI, displays the temperatures from the IBM temperature sensors (N=0..7) Sensor 0 is on the CPU, 3 is on the GPU. </p>
<dt><code>ibm_volume</code></p>
<dd> If running the IBM ACPI, displays the &quot;master&quot; volume, controlled by the volume keys (0-14). </p>
<dt><code>iconv_start</code> <code>codeset_from codeset_to</code></p>
<dd> Convert text from one codeset to another using GNU iconv. Needs to be stopped with iconv_stop. </p>
<dt><code>iconv_stop</code></p>
<dd> Stop iconv codeset conversion. </p>
<dt><code>if_empty</code> <code>(var)</code></p>
<dd> if conky variable VAR is empty, display everything between $if_empty and the matching $endif </p>
<dt><code>if_existing</code> <code>file (string)</code></p>
<dd> if FILE exists, display everything between if_existing and the matching $endif. The optional second parameter checks for FILE containing the specified string and prints everything between $if_existing and the matching $endif. </p>
<dt><code>if_gw</code></p>
<dd> if there is at least one default gateway, display everything between $if_gw and the matching $endif </p>
<dt><code>if_match</code> <code>expression</code></p>
<dd> Evaluates the given boolean expression, printing everything between $if_match and the matching $endif depending on whether the evaluation returns true or not. Valid expressions consist of a left side, an operator and a right side. Left and right sides are being parsed for contained text objects before evaluation. Recognised left and right side types are: </p>
<p> <code>double</code>Argument consists of only digits and a single dot.<br />
 <code>long</code>Argument consists of only digits.<br />
 <code>string</code>Argument is enclosed in quotation marks (&quot;) </p>
<p> Valid operands are: &#8216;&gt;&#8217;, &#8216;&lt;&#8216;, &#8216;&gt;=&#8217;, &#8216;&lt;=&#8217;, &#8216;==&#8217;, &#8216;!=&#8217;. </p>
<dt><code>if_mixer_mute</code> <code>(mixer)</code></p>
<dd> If mixer exists, display everything between $if_mixer_mute and the matching $endif. If no mixer is specified, &quot;Vol&quot; is used. </p>
<dt><code>if_mounted</code> <code>(mountpoint)</code></p>
<dd> if MOUNTPOINT is mounted, display everything between $if_mounted and the matching $endif </p>
<dt><code>if_mpd_playing</code></p>
<dd> if mpd is playing or paused, display everything between $if_mpd_playing and the matching $endif </p>
<dt><code>if_running</code> <code>(process)</code></p>
<dd> if PROCESS is running, display everything $if_running and the matching $endif. This uses the &#8220;pidof&#8221; command, so the -x switch is also supported. </p>
<dt><code>if_smapi_bat_installed</code> <code>(INDEX)</code></p>
<dd> when using smapi, if the battery with index INDEX is installed, display everything between $if_smapi_bat_installed and the matching $endif </p>
<dt><code>if_up</code> <code>(interface)</code></p>
<dd> if INTERFACE exists and is up, display everything between $if_up and the matching $endif </p>
<dt><code>if_updatenr</code> <code>(updatenr)</code></p>
<dd> If it&#8217;s the UPDATENR-th time that conky updates, display everything between $if_updatenr and the matching $endif. The counter resets when the highest UPDATENR is reached. Example : &quot;{$if_updatenr 1}foo$endif{$if_updatenr 2}bar$endif{$if_updatenr 4}$endif&quot; shows foo 25% of the time followed by bar 25% of the time followed by nothing the other half of the time. </p>
<dt><code>if_xmms2_connected</code></p>
<dd> Display everything between $if_xmms2_connected and the matching $endif if xmms2 is running. </p>
<dt><code>image</code> <code>&lt;path to image&gt; (-p x,y) (-s WxH) (-n) (-f interval)</code></p>
<dd> Renders an image from the path specified using Imlib2. Takes 4 optional arguments: a position, a size, a no-cache switch, and a cache flush interval. Changing the x,y position will move the position of the image, and changing the WxH will scale the image. If you specify the no-cache flag (-n), the image will not be cached. Alternately, you can specify the -f int switch to specify a cache flust interval for a particular image. Example: ${image /home/brenden/cheeseburger.jpg -p 20,20 -s 200&#215;200} will render &#8216;cheeseburger.jpg&#8217; at (20,20) scaled to 200&#215;200 pixels. Conky does not make any attempt to adjust the position (or any other formatting) of images, they are just rendered as per the arguments passed. The only reason $image is part of the TEXT section, is to allow for runtime modifications, through $execp $lua_parse, or some other method. </p>
<dt><code>imap_messages</code> <code>(args)</code></p>
<dd> Displays the number of messages in your global IMAP inbox by default. You can define individual IMAP inboxes separately by passing arguments to this object. Arguments are: &quot;host user pass [-i interval (in seconds)] [-f &#8216;folder&#8217;] [-p port] [-e &#8216;command&#8217;] [-r retries]&quot;. Default port is 143, default folder is &#8216;INBOX&#8217;, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as &#8216;*&#8217;, you will be prompted to enter the password when Conky starts. </p>
<dt><code>imap_unseen</code> <code>(args)</code></p>
<dd> Displays the number of unseen messages in your global IMAP inbox by default. You can define individual IMAP inboxes separately by passing arguments to this object. Arguments are: &quot;host user pass [-i interval (in seconds)] [-f &#8216;folder&#8217;] [-p port] [-e &#8216;command&#8217;] [-r retries]&quot;. Default port is 143, default folder is &#8216;INBOX&#8217;, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as &#8216;*&#8217;, you will be prompted to enter the password when Conky starts. </p>
<dt><code>include</code> <code>path</code></p>
<dd> Loads the configfile at path, places the configsettings behind the configsettings in the orginal config and places the vars where the includevar stood.</p>
<dt><code>ioscheduler</code> <code>disk</code></p>
<dd> Prints the current ioscheduler used for the given disk name (i.e. e.g. &quot;hda&quot; or &quot;sdb&quot;) </p>
<dt><code>kernel</code></p>
<dd> Kernel version </p>
<dt><code>laptop_mode</code></p>
<dd> The value of /proc/sys/vm/laptop_mode </p>
<dt><code>lines</code> <code>textfile</code></p>
<dd> Displays the number of lines in the given file </p>
<dt><code>loadavg</code> <code>(1|2|3)</code></p>
<dd> System load average, 1 is for past 1 minute, 2 for past 5 minutes and 3 for past 15 minutes. Without argument, prints all three values separated by whitespace. </p>
<dt><code>loadgraph</code> <code>(height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Load1 average graph, similar to xload, with optional colours in hex, minus the #. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>lua</code> <code>function_name (function parameters)</code></p>
<dd> Executes a Lua function with given parameters, then prints the returned string. See also &#8216;lua_load&#8217; on how to load scripts. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you put you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>lua_bar</code> <code>(height, width) function_name (function parameters)</code></p>
<dd> Executes a Lua function with given parameters and draws a bar. Expects result value to be an integer between 0 and 100. See also &#8216;lua_load&#8217; on how to load scripts. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you put you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>lua_gauge</code> <code>(height, width) function_name (function parameters)</code></p>
<dd> Executes a Lua function with given parameters and draws a gauge. Expects result value to be an integer between 0 and 100. See also &#8216;lua_load&#8217; on how to load scripts. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you put you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>lua_graph</code> <code>function_name (height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Executes a Lua function with and draws a graph. Expects result value to be any number, and by default will scale to show the full range. See also &#8216;lua_load&#8217; on how to load scripts. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you put you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>lua_parse</code> <code>function_name (function parameters)</code></p>
<dd> Executes a Lua function with given parameters as per $lua, then parses and prints the result value as per the syntax for Conky&#8217;s TEXT section. See also &#8216;lua_load&#8217; on how to load scripts. Conky puts &#8216;conky_&#8217; in front of function_name to prevent accidental calls to the wrong function unless you put you place &#8216;conky_&#8217; in front of it yourself. </p>
<dt><code>machine</code></p>
<dd> Machine, i686 for example </p>
<dt><code>mails</code> <code>(mailbox)</code> <code>(interval)</code></p>
<dd> Mail count in the specified mailbox or your mail spool if not. Both mbox and maildir type mailboxes are supported. You can use a program like fetchmail to get mails from some server using your favourite protocol. See also new_mails. </p>
<dt><code>mboxscan</code> <code>(-n number of messages to print) (-fw from width) (-sw subject width) mbox</code></p>
<dd> Print a summary of recent messages in an mbox format mailbox. mbox parameter is the filename of the mailbox (can be encapsulated using &#8216;&quot;&#8217;, ie. ${mboxscan -n 10 &quot;/home/brenden/some box&quot;} </p>
<dt><code>mem</code></p>
<dd> Amount of memory in use </p>
<dt><code>membar</code> <code>(height),(width)</code></p>
<dd> Bar that shows amount of memory in use </p>
<dt><code>memeasyfree</code></p>
<dd> Amount of free memory including the memory that is very easily freed (buffers/cache) </p>
<dt><code>memfree</code></p>
<dd> Amount of free memory </p>
<dt><code>memgauge</code> <code>(height),(width)</code></p>
<dd> Gauge that shows amount of memory in use (see cpugauge) </p>
<dt><code>memgraph</code> <code>(height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Memory usage graph. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>memmax</code></p>
<dd> Total amount of memory </p>
<dt><code>memperc</code></p>
<dd> Percentage of memory in use </p>
<dt><code>mixer</code> <code>(device)</code></p>
<dd> Prints the mixer value as reported by the OS. On Linux, this variable uses the OSS emulation, so you need the proper kernel module loaded. Default mixer is &quot;Vol&quot;, but you can specify one of the available OSS controls: &quot;Vol&quot;, &quot;Bass&quot;, &quot;Trebl&quot;, &quot;Synth&quot;, &quot;Pcm&quot;, &quot;Spkr&quot;, &quot;Line&quot;, &quot;Mic&quot;, &quot;CD&quot;, &quot;Mix&quot;, &quot;Pcm2 &quot;, &quot;Rec&quot;, &quot;IGain&quot;, &quot;OGain&quot;, &quot;Line1&quot;, &quot;Line2&quot;, &quot;Line3&quot;, &quot;Digital1&quot;, &quot;Digital2&quot;, &quot;Digital3&quot;, &quot;PhoneIn&quot;, &quot;PhoneOut&quot;, &quot;Video&quot;, &quot;Radio&quot; and &quot;Monitor&quot;. </p>
<dt><code>mixerbar</code> <code>(device)</code></p>
<dd> Displays mixer value in a bar as reported by the OS. See docs for $mixer for details on arguments. </p>
<dt><code>mixerl</code> <code>(device)</code></p>
<dd> Prints the left channel mixer value as reported by the OS. See docs for $mixer for details on arguments. </p>
<dt><code>mixerlbar</code> <code>(device)</code></p>
<dd> Displays the left channel mixer value in a bar as reported by the OS. See docs for $mixer for details on arguments. </p>
<dt><code>mixerr</code> <code>(device)</code></p>
<dd> Prints the right channel mixer value as reported by the OS. See docs for $mixer for details on arguments. </p>
<dt><code>mixerrbar</code> <code>(device)</code></p>
<dd> Displays the right channel mixer value in a bar as reported by the OS. See docs for $mixer for details on arguments. </p>
<dt><code>moc_album</code></p>
<dd> Album of the current MOC song </p>
<dt><code>moc_artist</code></p>
<dd> Artist of the current MOC song </p>
<dt><code>moc_bitrate</code></p>
<dd> Bitrate in the current MOC song </p>
<dt><code>moc_curtime</code></p>
<dd> Current time of the current MOC song </p>
<dt><code>moc_file</code></p>
<dd> File name of the current MOC song </p>
<dt><code>moc_rate</code></p>
<dd> Rate of the current MOC song </p>
<dt><code>moc_song</code></p>
<dd> The current song name being played in MOC. </p>
<dt><code>moc_state</code></p>
<dd> Current state of MOC; playing, stopped etc. </p>
<dt><code>moc_timeleft</code></p>
<dd> Time left in the current MOC song </p>
<dt><code>moc_title</code></p>
<dd> Title of the current MOC song </p>
<dt><code>moc_totaltime</code></p>
<dd> Total length of the current MOC song </p>
<dt><code>monitor</code></p>
<dd> Number of the monitor on which conky is running or the message &quot;Not running in X&quot; if this is the case. </p>
<dt><code>monitor_number</code></p>
<dd> Number of monitors or the message &quot;Not running in X&quot; if this is the case. </p>
<dt><code>mpd_album</code></p>
<dd> Album in current MPD song </p>
<dt><code>mpd_artist</code></p>
<dd> Artist in current MPD song must be enabled at compile </p>
<dt><code>mpd_bar</code> <code>(height),(width)</code></p>
<dd> Bar of mpd&#8217;s progress </p>
<dt><code>mpd_bitrate</code></p>
<dd> Bitrate of current song </p>
<dt><code>mpd_date</code></p>
<dd> Date of current song </p>
<dt><code>mpd_elapsed</code></p>
<dd> Song&#8217;s elapsed time </p>
<dt><code>mpd_file</code></p>
<dd> Prints the file name of the current MPD song </p>
<dt><code>mpd_length</code></p>
<dd> Song&#8217;s length </p>
<dt><code>mpd_name</code></p>
<dd> Prints the MPD name field </p>
<dt><code>mpd_percent</code></p>
<dd> Percent of song&#8217;s progress </p>
<dt><code>mpd_random</code></p>
<dd> Random status (On/Off) </p>
<dt><code>mpd_repeat</code></p>
<dd> Repeat status (On/Off) </p>
<dt><code>mpd_smart</code> <code>(max length)</code></p>
<dd> Prints the song name in either the form &quot;artist &#8211; title&quot; or file name, depending on whats available </p>
<dt><code>mpd_status</code></p>
<dd> Playing, stopped, et cetera. </p>
<dt><code>mpd_title</code> <code>(max length)</code></p>
<dd> Title of current MPD song </p>
<dt><code>mpd_track</code></p>
<dd> Prints the MPD track field </p>
<dt><code>mpd_vol</code></p>
<dd> MPD&#8217;s volume </p>
<dt><code>nameserver</code> <code>(index)</code></p>
<dd> Print a nameserver from /etc/resolv.conf. Index starts at and defaults to 0. </p>
<dt><code>new_mails</code> <code>(mailbox)</code> <code>(interval)</code></p>
<dd> Unread mail count in the specified mailbox or mail spool if not. Both mbox and maildir type mailboxes are supported. </p>
<dt><code>nodename</code></p>
<dd> Hostname </p>
<dt><code>nodename_short</code></p>
<dd> Short hostname (same as &#8216;hostname -s&#8217; shell command). </p>
<dt><code>nvidia</code> <code>threshold</code> <code>temp</code> <code>ambient</code> <code>gpufreq</code> <code>memfreq</code> <code>imagequality</code></p>
<dd> Nvidia graficcard support for the XNVCtrl library. Each option can be shortened to the least significant part. Temperatures are printed as float, all other values as integer. </p>
<p> <code>threshold</code> <code>The thresholdtemperature at which the gpu slows down</code><br />
 <code>temp</code> <code>Gives the gpu current temperature</code><br />
 <code>ambient</code> <code>Gives current air temperature near GPU case</code><br />
 <code>gpufreq</code> <code>Gives the current gpu frequency</code><br />
 <code>memfreq</code> <code>Gives the current mem frequency</code><br />
 <code>imagequality</code> <code>Which imagequality should be chosen by OpenGL applications</code> </p>
<dt><code>offset</code> <code>(pixels)</code></p>
<dd> Move text over by N pixels. See also $voffset. </p>
<dt><code>outlinecolor</code> <code>(color)</code></p>
<dd> Change outline color </p>
<dt><code>pb_battery</code> <code>item</code></p>
<dd> If running on Apple powerbook/ibook, display information on battery status. The item parameter specifies, what information to display. Exactly one item must be specified. Valid items are: </p>
<p> <code>status</code> <code>Display if battery is fully charged, charging, discharging or absent (running on AC)</code><br />
 <code>percent</code> <code>Display charge of battery in percent, if charging or discharging. Nothing will be displayed, if battery is fully charged or absent.</code><br />
 <code>time</code> <code>Display the time remaining until the battery will be fully charged or discharged at current rate. Nothing is displayed, if battery is absent or if it&#8217;s present but fully charged and not discharging.</code> </p>
<dt><code>pid_chroot</code> <code>pid</code></p>
<dd> Directory used as rootdirectory by the process (this will be &quot;/&quot; unless the process did a chroot syscall) </p>
<dt><code>pid_cmdline</code> <code>pid</code></p>
<dd> Command line this process was invoked with </p>
<dt><code>pid_cwd</code> <code>pid</code></p>
<dd> Current working directory of the process </p>
<dt><code>pid_environ</code> <code>pid varname</code></p>
<dd> Contents of a environment-var of the process </p>
<dt><code>pid_environ_list</code> <code>pid</code></p>
<dd> List of environment-vars that the process can see </p>
<dt><code>pid_exe</code> <code>pid</code></p>
<dd> Path to executed command that started the process </p>
<dt><code>pid_nice</code> <code>pid</code></p>
<dd> The nice value of the process </p>
<dt><code>pid_openfiles</code> <code>pid</code></p>
<dd> List of files that the process has open </p>
<dt><code>pid_parent</code> <code>pid</code></p>
<dd> The pid of the parent of the process </p>
<dt><code>pid_priority</code> <code>pid</code></p>
<dd> The priority of the process (see &#8216;priority&#8217; in &quot;man 5 proc&quot;) </p>
<dt><code>pid_read</code> <code>pid</code></p>
<dd> Total number of bytes read by the process </p>
<dt><code>pid_state</code> <code>pid</code></p>
<dd> State of the process </p>
<dt><code>pid_state_short</code> <code>pid</code></p>
<dd> One of the chars in &quot;RSDZTW&quot; representing the state of the process where R is running, S is sleeping in an interruptible wait, D is waiting in uninterruptible disk sleep, Z is zombie, T is traced or stopped (on a signal), and W is paging </p>
<dt><code>pid_stderr</code> <code>pid</code></p>
<dd> Filedescriptor binded to the STDERR of the process </p>
<dt><code>pid_stdin</code> <code>pid</code></p>
<dd> Filedescriptor binded to the STDIN of the process </p>
<dt><code>pid_stdout</code> <code>pid</code></p>
<dd> Filedescriptor binded to the STDOUT of the process </p>
<dt><code>pid_threads</code> <code>pid</code></p>
<dd> Number of threads in process containing this thread </p>
<dt><code>pid_thread_list</code> <code>pid</code></p>
<dd> List with pid&#8217;s from threads from this process </p>
<dt><code>pid_time_kernelmode</code> <code>pid</code></p>
<dd> Amount of time that the process has been scheduled in kernel mode in seconds </p>
<dt><code>pid_time_usermode</code> <code>pid</code></p>
<dd> Amount of time that the process has been scheduled in user mode in seconds </p>
<dt><code>pid_time</code> <code>pid</code></p>
<dd> Sum of $pid_time_kernelmode and $pid_time_usermode </p>
<dt><code>pid_uid</code> <code>pid</code></p>
<dd> The real uid of the process </p>
<dt><code>pid_euid</code> <code>pid</code></p>
<dd> The effective uid of the process </p>
<dt><code>pid_suid</code> <code>pid</code></p>
<dd> The saved set uid of the process </p>
<dt><code>pid_fsuid</code> <code>pid</code></p>
<dd> The file system uid of the process </p>
<dt><code>pid_gid</code> <code>pid</code></p>
<dd> The real gid of the process </p>
<dt><code>pid_egid</code> <code>pid</code></p>
<dd> The effective gid of the process </p>
<dt><code>pid_sgid</code> <code>pid</code></p>
<dd> The saved set gid of the process </p>
<dt><code>pid_fsgid</code> <code>pid</code></p>
<dd> The file system gid of the process </p>
<dt><code>pid_vmpeak</code> <code>pid</code></p>
<dd> Peak virtual memory size of the process </p>
<dt><code>pid_vmsize</code> <code>pid</code></p>
<dd> Virtual memory size of the process </p>
<dt><code>pid_vmlck</code> <code>pid</code></p>
<dd> Locked memory size of the process </p>
<dt><code>pid_vmhwm</code> <code>pid</code></p>
<dd> Peak resident set size (&quot;high water mark&quot;) of the process </p>
<dt><code>pid_vmrss</code> <code>pid</code></p>
<dd> Resident set size of the process </p>
<dt><code>pid_vmdata</code> <code>pid</code></p>
<dd> Data segment size of the process </p>
<dt><code>pid_vmstk</code> <code>pid</code></p>
<dd> Stack segment size of the process </p>
<dt><code>pid_vmexe</code> <code>pid</code></p>
<dd> Text segment size of the process </p>
<dt><code>pid_vmlib</code> <code>pid</code></p>
<dd> Shared library code size of the process </p>
<dt><code>pid_vmpte</code> <code>pid</code></p>
<dd> Page table entries size of the process </p>
<dt><code>pid_write</code> <code>pid</code></p>
<dd> Total number of bytes written by the process </p>
<dt><code>platform</code> <code>(dev) type n (factor offset)</code></p>
<dd> Platform sensor from sysfs (Linux 2.6). Parameter dev may be omitted if you have only one platform device. Platform type is either &#8216;in&#8217; or &#8216;vol&#8217; meaning voltage; &#8216;fan&#8217; meaning fan; &#8216;temp&#8217; meaning temperature. Parameter n is number of the sensor. See /sys/bus/platform/devices/ on your local computer. The optional arguments &#8216;factor&#8217; and &#8216;offset&#8217; allow precalculation of the raw input, which is being modified as follows: &#8216;input = input * factor + offset&#8217;. Note that they have to be given as decimal values (i.e. contain at least one decimal place). </p>
<dt><code>pop3_unseen</code> <code>(args)</code></p>
<dd> Displays the number of unseen messages in your global POP3 inbox by default. You can define individual POP3 inboxes separately by passing arguments to this object. Arguments are: &quot;host user pass [-i interval (in seconds)] [-p port] [-e &#8216;command&#8217;] [-r retries]&quot;. Default port is 110, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as &#8216;*&#8217;, you will be prompted to enter the password when Conky starts. </p>
<dt><code>pop3_used</code> <code>(args)</code></p>
<dd> Displays the amount of space (in MiB, 2^20) used in your global POP3 inbox by default. You can define individual POP3 inboxes separately by passing arguments to this object. Arguments are: &quot;host user pass [-i interval (in seconds)] [-p port] [-e &#8216;command&#8217;] [-r retries]&quot;. Default port is 110, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as &#8216;*&#8217;, you will be prompted to enter the password when Conky starts. </p>
<dt><code>pre_exec</code> <code>shell command</code></p>
<dd> Executes a shell command one time before conky displays anything and puts output as text. </p>
<dt><code>processes</code></p>
<dd> Total processes (sleeping and running) </p>
<dt><code>read_tcp</code> <code>(host) port</code></p>
<dd> Connects to a tcp port on a host (default is localhost), reads every char available at the moment and shows them. </p>
<dt><code>replied_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails marked as replied in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>rss</code> <code>uri interval_in_minutes action (num_par (spaces_in_front))</code></p>
<dd> Download and parse RSS feeds. The interval may be a floating point value greater than 0, otherwise defaults to 15 minutes. Action may be one of the following: feed_title, item_title (with num par), item_desc (with num par) and item_titles (when using this action and spaces_in_front is given conky places that many spaces in front of each item). This object is threaded, and once a thread is created it can&#8217;t be explicitly destroyed. One thread will run for each URI specified. You can use any protocol that Curl supports.</p>
<dt><code>running_processes</code></p>
<dd> Running processes (not sleeping), requires Linux 2.6 </p>
<dt><code>running_threads</code></p>
<dd> Number of running (runnable) threads. Linux only. </p>
<dt><code>scroll</code> <code>length (step) text</code></p>
<dd> Scroll &#8216;text&#8217; by &#8216;step&#8217; characters showing &#8216;length&#8217; number of characters at the same time. The text may also contain variables. &#8216;step&#8217; is optional and defaults to 1 if not set. If a var creates output on multiple lines then the lines are placed behind each other separated with a &#8216;|&#8217;-sign. If you change the textcolor inside $scroll it will automatically have it&#8217;s old value back at the end of $scroll. The end and the start of text will be separated by &#8216;length&#8217; number of spaces. </p>
<dt><code>seen_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails marked as seen in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>shadecolor</code> <code>(color)</code></p>
<dd> Change shading color </p>
<dt><code>smapi</code> <code>(ARGS)</code></p>
<dd> when using smapi, display contents of the /sys/devices/platform/smapi directory. ARGS are either &#8216;(FILENAME)&#8217; or &#8216;bat (INDEX) (FILENAME)&#8217; to display the corresponding files&#8217; content. This is a very raw method of accessing the smapi values. When available, better use one of the smapi_* variables instead. </p>
<dt><code>smapi_bat_bar</code> <code>(INDEX),(height),(width)</code></p>
<dd> when using smapi, display the remaining capacity of the battery with index INDEX as a bar. </p>
<dt><code>smapi_bat_perc</code> <code>(INDEX)</code></p>
<dd> when using smapi, display the remaining capacity in percent of the battery with index INDEX. This is a separate variable because it supports the &#8216;use_spacer&#8217; configuration option. </p>
<dt><code>smapi_bat_power</code> <code>INDEX</code></p>
<dd> when using smapi, display the current power of the battery with index INDEX in watt. This is a separate variable because the original read out value is being converted from mW. The sign of the output reflects charging (positive) or discharging (negative) state. </p>
<dt><code>smapi_bat_temp</code> <code>INDEX</code></p>
<dd> when using smapi, display the current temperature of the battery with index INDEX in degree Celsius. This is a separate variable because the original read out value is being converted from milli degree Celsius. </p>
<dt><code>sony_fanspeed</code></p>
<dd> Displays the Sony VAIO fanspeed information if sony-laptop kernel support is enabled. Linux only. </p>
<dt><code>stippled_hr</code> <code>(space)</code></p>
<dd> Stippled (dashed) horizontal line </p>
<dt><code>swap</code></p>
<dd> Amount of swap in use </p>
<dt><code>swapbar</code> <code>(height),(width)</code></p>
<dd> Bar that shows amount of swap in use </p>
<dt><code>swapfree</code></p>
<dd> Amount of free swap </p>
<dt><code>swapmax</code></p>
<dd> Total amount of swap </p>
<dt><code>swapperc</code></p>
<dd> Percentage of swap in use </p>
<dt><code>sysname</code></p>
<dd> System name, Linux for example </p>
<dt><code>tab</code> <code>(width, (start))</code></p>
<dd> Puts a tab of the specified width, starting from column &#8216;start&#8217;. The unit is pixels for both arguments. </p>
<dt><code>tail</code> <code>logfile lines (next_check)</code></p>
<dd> Displays last N lines of supplied text file. The file is checked every &#8216;next_check&#8217; update. If next_check is not supplied, Conky defaults to 2. Max of 30 lines can be displayed, or until the text buffer is filled. </p>
<dt><code>tcp_portmon</code> <code>port_begin port_end item (index)</code></p>
<dd> TCP port (both IPv6 and IPv4) monitor for specified local ports. Port numbers must be in the range 1 to 65535. Valid items are: </p>
<p> <code>count</code> <code>Total number of connections in the range</code><br />
 <code>rip</code> <code>Remote ip address</code><br />
 <code>rhost</code> <code>Remote host name</code><br />
 <code>rport</code> <code>Remote port number</code><br />
 <code>rservice</code> <code>Remote service name from /etc/services</code><br />
 <code>lip</code> <code>Local ip address</code><br />
 <code>lhost</code> <code>Local host name</code><br />
 <code>lport</code> <code>Local port number</code><br />
 <code>lservice</code> <code>Local service name from /etc/services</code> </p>
<p> The connection index provides you with access to each connection in the port monitor. The monitor will return information for index values from 0 to n-1 connections. Values higher than n-1 are simply ignored. For the &quot;count&quot; item, the connection index must be omitted. It is required for all other items. </p>
<p> Examples: </p>
<p> <code>${tcp_portmon 6881 6999 count}</code> <code>Displays the number of connections in the bittorrent port range</code><br />
 <code>${tcp_portmon 22 22 rip 0}</code> <code>Displays the remote host ip of the first sshd connection</code><br />
 <code>${tcp_portmon 22 22 rip 9}</code> <code>Displays the remote host ip of the tenth sshd connection</code><br />
 <code>${tcp_portmon 1 1024 rhost 0}</code> <code>Displays the remote host name of the first connection on a privileged port</code><br />
 <code>${tcp_portmon 1 1024 rport 4}</code> <code>Displays the remote host port of the fifth connection on a privileged port</code><br />
 <code>${tcp_portmon 1 65535 lservice 14}</code> <code>Displays the local service name of the fifteenth connection in the range of all ports</code> </p>
<p> Note that port monitor variables which share the same port range actually refer to the same monitor, so many references to a single port range for different items and different indexes all use the same monitor internally. In other words, the program avoids creating redundant monitors.</p>
<dt><code>templateN</code> <code>(arg1)</code> <code>(arg2)</code> <code>(arg3 &#8230;)</code></p>
<dd> Evaluate the content of the templateN configuration variable (where N is a value between 0 and 9, inclusively), applying substitutions as described in the documentation of the corresponding configuration variable. The number of arguments is optional, but must match the highest referred index in the template. You can use the same special sequences in each argument as the ones valid for a template definition, e.g. to allow an argument to contain a whitespace. Also simple nesting of templates is possible this way. </p>
<p> Here are some examples of template definitions: </p>
<p> template0 $\1\2<br />
 template1 \1: ${fs_used \2} / ${fs_size \2}<br />
 template2 \1 \2 </p>
<p> The following list shows sample usage of the templates defined above, with the equivalent syntax when not using any template at all: </p>
<table>
<tr VALIGN=top>
<td> using template </td>
<td> same without template
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> ${template1 root /} </td>
<td> root: ${fs_free /} / ${fs_size /}
</td>
</tr>
<tr VALIGN=top>
<td> ${template1 ${template2\ disk\ root} /} </td>
<td> disk root: ${fs_free /} / ${fs_size /}
</td>
</tr>
</table>
<dt><code>texeci</code> <code>interval command</code></p>
<dd> Runs a command at an interval inside a thread and displays the output. Same as $execi, except the command is run inside a thread. Use this if you have a slow script to keep Conky updating. You should make the interval slightly longer then the time it takes your script to execute. For example, if you have a script that take 5 seconds to execute, you should make the interval at least 6 seconds. See also $execi. This object will clean up the thread when it is destroyed, so it can safely be used in a nested fashion, though it may not produce the desired behaviour if used this way. </p>
<dt><code>threads</code></p>
<dd> Total threads </p>
<dt><code>time</code> <code>(format)</code></p>
<dd> Local time, see man strftime to get more information about format </p>
<dt><code>to_bytes</code> <code>size</code></p>
<dd> If &#8216;size&#8217; is a number followed by a size-unit (kilobyte,mb,GiB,&#8230;) then it converts the size to bytes and shows it without unit, otherwise it just shows &#8216;size&#8217;. </p>
<dt><code>top</code> <code>type num</code></p>
<dd> This takes arguments in the form:top (name) (number) Basically, processes are ranked from highest to lowest in terms of cpu usage, which is what (num) represents. The types are: &quot;name&quot;, &quot;pid&quot;, &quot;cpu&quot;, &quot;mem&quot;, &quot;mem_res&quot;, &quot;mem_vsize&quot;, &quot;time&quot;, &quot;uid&quot;, &quot;user&quot;, &quot;io_perc&quot;, &quot;io_read&quot; and &quot;io_write&quot;. There can be a max of 10 processes listed. </p>
<dt><code>top_io</code> <code>type num</code></p>
<dd> Same as top, except sorted by the amount of I/O the process has done during the update interval </p>
<dt><code>top_mem</code> <code>type num</code></p>
<dd> Same as top, except sorted by mem usage instead of cpu </p>
<dt><code>top_time</code> <code>type num</code></p>
<dd> Same as top, except sorted by total CPU time instead of current CPU usage </p>
<dt><code>totaldown</code> <code>(net)</code></p>
<dd> Total download, overflows at 4 GB on Linux with 32-bit arch and there doesn&#8217;t seem to be a way to know how many times it has already done that before conky has started. </p>
<dt><code>totalup</code> <code>(net)</code></p>
<dd> Total upload, this one too, may overflow </p>
<dt><code>trashed_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails marked as trashed in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>tztime</code> <code>(timezone (format))</code></p>
<dd> Local time for specified timezone, see man strftime to get more information about format. The timezone argument is specified in similar fashion as TZ environment variable. For hints, look in /usr/share/zoneinfo. e.g. US/Pacific, Europe/Zurich, etc. </p>
<dt><code>gid_name</code> <code>gid</code></p>
<dd> Name of group with this gid </p>
<dt><code>uid_name</code> <code>uid</code></p>
<dd> Username of user with this uid </p>
<dt><code>unflagged_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails not marked as flagged in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>unforwarded_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails not marked as forwarded in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>unreplied_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of mails not marked as replied in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>unseen_mails</code> <code>(maildir)</code> <code>(interval)</code></p>
<dd> Number of new or unseen mails in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. </p>
<dt><code>updates</code> <code>Number of updates</code></p>
<dd> for debugging </p>
<dt><code>upspeed</code> <code>(net)</code></p>
<dd> Upload speed in suitable IEC units </p>
<dt><code>upspeedf</code> <code>(net)</code></p>
<dd> Upload speed in KiB with one decimal </p>
<dt><code>upspeedgraph</code> <code>(netdev) (height),(width) (gradient colour 1) (gradient colour 2) (scale) (-t) (-l)</code></p>
<dd> Upload speed graph, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch &#8216;-t&#8217; to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). </p>
<dt><code>uptime</code></p>
<dd> Uptime </p>
<dt><code>uptime_short</code></p>
<dd> Uptime in a shorter format </p>
<dt><code>user_names</code></p>
<dd> Lists the names of the users logged in </p>
<dt><code>user_number</code></p>
<dd> Number of users logged in </p>
<dt><code>user_terms</code></p>
<dd> Lists the consoles in use </p>
<dt><code>user_times</code></p>
<dd> Lists how long users have been logged in for </p>
<dt><code>user_time</code> <code>console</code></p>
<dd> Lists how long the user for the given console has been logged in for </p>
<dt><code>utime</code> <code>(format)</code></p>
<dd> Display time in UTC (universal coordinate time). </p>
<dt><code>voffset</code> <code>(pixels)</code></p>
<dd> Change vertical offset by N pixels. Negative values will cause text to overlap. See also $offset. </p>
<dt><code>voltage_mv</code> <code>(n)</code></p>
<dd> Returns CPU #n&#8217;s voltage in mV. CPUs are counted from 1. If omitted, the parameter defaults to 1. </p>
<dt><code>voltage_v</code> <code>(n)</code></p>
<dd> Returns CPU #n&#8217;s voltage in V. CPUs are counted from 1. If omitted, the parameter defaults to 1. </p>
<dt><code>weather</code> <code>URI locID data_type (interval_in_minutes)</code></p>
<dd> Download, parse and display METAR data. </p>
<p> For the &#8216;URI&#8217;, there are two possibilities: </p>
<p> <a rel="nofollow" href="http://weather.noaa.gov/pub/data/observations/metar/stations/">http://weather.noaa.gov/pub/data/observations/metar/stations/</a><br />
 <a rel="nofollow" href="http://xoap.weather.com/weather/local/">http://xoap.weather.com/weather/local/</a> </p>
<p> The first one is free to use but the second requires you to register and obtain your partner ID and license key. These two must be written, separated by a space, into a file called .xoaprc which needs to be placed into your home directory. </p>
<p> &#8216;locID&#8217; must be a valid location identifier for the required uri. For the NOAA site this must be a valid ICAO (see for instance <a rel="nofollow" href="https://pilotweb.nas.faa.gov/qryhtml/icao/">https://pilotweb.nas.faa.gov/qryhtml/icao/</a>). For the weather.com site this must be a valid location ID (see for instance <a rel="nofollow" href="http://aspnetresources.com/tools/locid.aspx">http://aspnetresources.com/tools/locid.aspx</a>). </p>
<p> &#8216;data_type&#8217; must be one of the following: </p>
<p> <code>last_update</code> The date and time stamp of the data. The result depends on the URI used. For the NOAA site it is date (yyyy/mm/dd) and UTC time. For the weather.com one it is date ([m]m/[d]d/yy) and Local Time of the station.<br />
 <code>temperature</code> </p>
<p> Air temperature (you can use the &#8216;temperature_unit&#8217; config setting to change units)<br />
 <code>cloud_cover</code> </p>
<p> The highest cloud cover status<br />
 <code>pressure</code> </p>
<p> Air pressure in millibar<br />
 <code>wind_speed</code> </p>
<p> Wind speed in km/h<br />
 <code>wind_dir</code> </p>
<p> Wind direction<br />
 <code>wind_dir_DEG</code> </p>
<p> Compass wind direction<br />
 <code>humidity</code> </p>
<p> Relative humidity in %<br />
 <code>weather</code> </p>
<p> Any relevant weather event (rain, snow, etc.). This is not used if you are querying the weather.com site since this data is aggregated into the cloud_cover one<br />
 <code>icon</code> </p>
<p> Weather icon (only for <a rel="nofollow" href="http://www.weather.com">www.weather.com</a>). Can be used together with the icon kit provided upon registering to their service. </p>
<p> &#8216;delay_in_minutes&#8217; (optional, default 30) cannot be less than 30 minutes. </p>
<p> This object is threaded, and once a thread is created it can&#8217;t be explicitly destroyed. One thread will run for each URI specified. </p>
<p> Note that these variables are still EXPERIMENTAL and can be subject to many future changes.</p>
<dt><code>weather_forecast</code> <code>URI locID day data_type (interval_in_minutes)</code></p>
<dd> Download, parse and display weather forecast data for a given day (daytime only). </p>
<p> For the &#8216;URI&#8217;, for the time being only <a rel="nofollow" href="http://xoap.weather.com/weather/local/">http://xoap.weather.com/weather/local/</a> is supported. See &#8216;weather&#8217; above for details of usage </p>
<p> &#8216;locID&#8217;, see &#8216;weather&#8217; above. </p>
<p> &#8216;day&#8217; is a number from 0 (today) to 4 (3 days after tomorrow). </p>
<p> &#8216;data_type&#8217; must be one of the following: </p>
<p> <code>day</code> <code>Day of the week</code><br />
 <code>date</code> <code>Date, in the form MMM DD (ie. Jul 14)</code><br />
 <code>low</code> <code>Minimun temperature (you can use the &#8216;temperature_unit&#8217; config setting to change units)</code><br />
 <code>hi</code> <code>Maximum temperature (you can use the &#8216;temperature_unit&#8217; config setting to change units)</code><br />
 <code>icon</code> <code>Weather icon. Can be used together with the icon kit provided upon registering to the weather.com service</code><br />
 <code>forecast</code> <code>Weather forecast (sunny, rainy, etc.)</code><br />
 <code>wind_speed</code> <code>Wind speed in km/h</code><br />
 <code>wind_dir</code> <code>Wind direction</code><br />
 <code>wind_dir_DEG</code> <code>Compass wind direction</code><br />
 <code>humidity</code> <code>Relative humidity in %</code><br />
 <code>precipitation</code> <code>Probability of having a precipitation (in %)</code> </p>
<p> &#8216;delay_in_minutes&#8217; (optional, default 210) cannot be lower than 210 min. </p>
<p> This object is threaded, and once a thread is created it can&#8217;t be explicitly destroyed. One thread will run for each URI specified. You can use any protocol that Curl supports. </p>
<p> Note that these variables are still EXPERIMENTAL and can be subject to many future changes.</p>
<dt><code>wireless_ap</code> <code>(net)</code></p>
<dd> Wireless access point MAC address (Linux only) </p>
<dt><code>wireless_bitrate</code> <code>(net)</code></p>
<dd> Wireless bitrate (ie 11 Mb/s) (Linux only) </p>
<dt><code>wireless_essid</code> <code>(net)</code></p>
<dd> Wireless access point ESSID (Linux only) </p>
<dt><code>wireless_link_bar</code> <code>(height),(width) (net)</code></p>
<dd> Wireless link quality bar (Linux only) </p>
<dt><code>wireless_link_qual</code> <code>(net)</code></p>
<dd> Wireless link quality (Linux only) </p>
<dt><code>wireless_link_qual_max</code> <code>(net)</code></p>
<dd> Wireless link quality maximum value (Linux only) </p>
<dt><code>wireless_link_qual_perc</code> <code>(net)</code></p>
<dd> Wireless link quality in percents (Linux only) </p>
<dt><code>wireless_mode</code> <code>(net)</code></p>
<dd> Wireless mode (Managed/Ad-Hoc/Master) (Linux only) </p>
<dt><code>words</code> <code>textfile</code></p>
<dd> Displays the number of words in the given file </p>
<dt><code>xmms2_album</code></p>
<dd> Album in current XMMS2 song </p>
<dt><code>xmms2_artist</code></p>
<dd> Artist in current XMMS2 song </p>
<dt><code>xmms2_bar</code> <code>(height),(width)</code></p>
<dd> Bar of XMMS2&#8217;s progress </p>
<dt><code>xmms2_bitrate</code></p>
<dd> Bitrate of current song </p>
<dt><code>xmms2_comment</code></p>
<dd> Comment in current XMMS2 song </p>
<dt><code>xmms2_date</code></p>
<dd> Returns song&#8217;s date. </p>
<dt><code>xmms2_duration</code></p>
<dd> Duration of current song </p>
<dt><code>xmms2_elapsed</code></p>
<dd> Song&#8217;s elapsed time </p>
<dt><code>xmms2_genre</code></p>
<dd> Genre in current XMMS2 song </p>
<dt><code>xmms2_id</code></p>
<dd> XMMS2 id of current song </p>
<dt><code>xmms2_percent</code></p>
<dd> Percent of song&#8217;s progress </p>
<dt><code>xmms2_playlist</code></p>
<dd> Returns the XMMS2 playlist. </p>
<dt><code>xmms2_size</code></p>
<dd> Size of current song </p>
<dt><code>xmms2_smart</code></p>
<dd> Prints the song name in either the form &quot;artist &#8211; title&quot; or file name, depending on whats available </p>
<dt><code>xmms2_status</code></p>
<dd> XMMS2 status (Playing, Paused, Stopped, or Disconnected) </p>
<dt><code>xmms2_timesplayed</code></p>
<dd> Number of times a song was played (presumably). </p>
<dt><code>xmms2_title</code></p>
<dd> Title in current XMMS2 song </p>
<dt><code>xmms2_tracknr</code></p>
<dd> Track number in current XMMS2 song </p>
<dt><code>xmms2_url</code></p>
<dd> Full path to current song </p>
<dt><code>if_jack_active</code></p>
<dd> If JACK is active display everything between the $if_jack_active and the matching $endif. </p>
<dt><code>jack_cpu_load</code></p>
<dd> Prints the current CPU load as estimated by JACK. </p>
<dt><code>jack_buffer_size</code></p>
<dd> Shows the current JACK buffer size. </p>
<dt><code>jack_sampler_rate</code></p>
<dd> Shows the current JACK sample rate. </p>
<dt><code>jack_xruns</code></p>
<dd> Shows a count of xruns (buffer over/under runs) that have ocurred. </p>
<dt><code>if_jack_rolling</code></p>
<dd> If the JACK transport mechanism is rolling, display everything between the $if_jack_rolling and the matching $endif. </p>
<dt><code>jack_frame</code></p>
<dd> Shows the frame number in the JACK transport timeline. </p>
<dt><code>jack_hour</code></p>
<dd> Shows the frame number as hours. </p>
<dt><code>jack_min</code></p>
<dd> Shows the frame number as minutes within the hour. </p>
<dt><code>jack_sec</code></p>
<dd> Shows the frame number as seconds within the minute. </p>
<dt><code>if_jack_bbt</code></p>
<dd> If JACK transport is keeping BBT (bars/beats/ticks) information then display everything between $if_jack_bbt and the corresponding $endif. </p>
<dt><code>jack_beat_type</code></p>
<dd> Shows the beat type of the time signature the JACK transport mechanism is using. </p>
<dt><code>jack_beats_per_bar</code></p>
<dd> Shows the number of beats per bar the JACK transport mechanism is using. </p>
<dt><code>jack_bpm</code></p>
<dd> Shows the beats per minute the JACK transport mechanism is using. </p>
<dt><code>jack_bar</code></p>
<dd> The bar position JACK transport is currently located. </p>
<dt><code>jack_beat</code></p>
<dd> The beat within the bar JACK transport is currently located. </p>
<dt><code>jack_tick</code></p>
<dd> The tick within the beat JACK transport is currently located. </p>
</dl>
<h2>LUA API</h2>
<p> Conky features a Lua Programming API, and also ships with Lua bindings for some useful libraries. Conky defines certain global functions and variables which can be accessed from Lua code running in Conky. </p>
<p> To use Lua Conky, you first need to make sure you have a version of Conky with Lua support enabled (&#8220;conky -v&#8221; will report this). Scripts must first be loaded using the lua_load configuration option. You then call functions in Lua via Conky&#8217;s $lua, $lua_read, and Lua hooks. </p>
<p> Be careful when creating threaded objects through the Lua API. You could wind up with a whole bunch of threads running if a thread is created with each iteration. </p>
<p> At this time, the Lua API should not be considered stable and may change drastically from one release to another as it matures. </p>
<p> NOTE: In order to accommodate certain features in the cairo library&#8217;s API, Conky will export a few additional functions for the creation of certain structures. These are documented below.</p>
<dl>
<dt><code>conky_parse(string)</code> <code>function</code></p>
<dd> This function takes a string that is evaluated as per Conky&#8217;s TEXT section, and then returns a string with the result.</p>
<dt><code>conky_set_update_interval(number)</code> <code>function</code></p>
<dd> Sets Conky&#8217;s update interval (in seconds) to &#8216;number&#8217;.</p>
<dt><code>conky_window</code> <code>table</code></p>
<dd> This table contains some information about Conky&#8217;s window. The following table describes the values contained: </p>
<p> <code>drawable</code> <code>Window&#8217;s drawable (Xlib Drawable), requires Lua extras enabled at compile time.</code><br />
 <code>visual</code> <code>Window&#8217;s visual (Xlib Visual), requires Lua extras enabled at compile time.</code><br />
 <code>display</code> <code>Window&#8217;s display (Xlib Display), requires Lua extras enabled at compile time.</code><br />
 <code>width</code> <code>Window width (in pixels).</code><br />
 <code>height</code> <code>Window height (in pixels).</code><br />
 <code>border_inner_margin</code> <code>Window&#8217;s inner border margin (in pixels).</code><br />
 <code>border_outer_margin</code> <code>Window&#8217;s outer border margin (in pixels).</code><br />
 <code>border_width</code> <code>Window&#8217;s border width (in pixels).</code><br />
 <code>text_start_x</code> <code>The x component of the starting coordinate of text drawing.</code><br />
 <code>text_start_y</code> <code>The y component of the starting coordinate of text drawing.</code><br />
 <code>text_width</code> <code>The width of the text drawing region.</code><br />
 <code>text_height</code> <code>The height of the text drawing region.</code> </p>
<p> NOTE: This table is only defined when X support is enabled.</p>
<dt><code>conky_info</code> <code>table</code></p>
<dd> This table contains some information about Conky&#8217;s internal data. The following table describes the values contained: </p>
<p> <code>update_interval</code> <code>Conky&#8217;s update interval (in seconds).</code><br />
 <code>uptime</code> <code>System uptime, in seconds.</code></p>
<dt><code>conky_build_info</code> <code>string</code></p>
<dd> A string containing the build info for this particular instance of Conky, including the version, build date, and architecture.</p>
<dt><code>conky_build_date</code> <code>string</code></p>
<dd> A string containing the build date for this particular instance of Conky.</p>
<dt><code>conky_build_arch</code> <code>string</code></p>
<dd> A string containing the build architecture for this particular instance of Conky.</p>
<dt><code>conky_version</code> <code>string</code></p>
<dd> A string containing the version of the current instance of Conky.</p>
<dt><code>conky_config</code> <code>string</code></p>
<dd> A string containing the path of the current Conky configuration file.</p>
<dt><code>cairo_text_extents_t:create()</code> <code>function</code></p>
<dd> Call this function to return a new cairo_text_extents_t structure. A creation function for this structure is not provided by the cairo API. After calling this, you should use tolua.takeownership() on the return value to ensure ownership is passed properly.</p>
<dt><code>cairo_font_extents_t:create()</code> <code>function</code></p>
<dd> Call this function to return a new cairo_font_extents_t structure. A creation function for this structure is not provided by the cairo API. After calling this, you should use tolua.takeownership() on the return value to ensure ownership is passed properly.</p>
<dt><code>cairo_matrix_t:create()</code> <code>function</code></p>
<dd> Call this function to return a new cairo_matrix_t structure. A creation function for this structure is not provided by the cairo API. After calling this, you should use tolua.takeownership() on the return value to ensure ownership is passed properly.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>conky <code>-t &#8216;${time %D %H:%M}&#8217; -o -u 30</code></p>
<dd> Start Conky in its own window with date and clock as text and 30 sec update interval.</p>
<dt>conky <code>-a top_left -x 5 -y 500 -d</code></p>
<dd> Start Conky to background at coordinates (5, 500).</p>
<dt>conky <code>-C &gt; ~/.conkyrc</code></p>
<dd> Do not start Conky, but have it output the builtin default config file to ~/.conkyrc for later customising.</dl>
<h2>FILES</h2>
<dl>
<dt><i>${sysconfdir}/conky/conky.conf</i></p>
<dd> Default system-wide configuration file. The value of ${sysconfdir} depends on the compile-time options (most likely /etc).</p>
<dt><i>~/.conkyrc</i></p>
<dd> Default personal configuration file.</dl>
<h2>BUGS</h2>
<p> Drawing to root or some other desktop window directly doesn&#8217;t work with all window managers. Especially doesn&#8217;t work well with Gnome and it has been reported that it doesn&#8217;t work with KDE either. Nautilus can be disabled from drawing to desktop with program gconf-editor. Uncheck show_desktop in /apps/nautilus/preferences/. There is -w switch in Conky to set some specific window id. You might find xwininfo -tree useful to find the window to draw to. You can also use -o argument which makes Conky to create its own window. If you do try running Conky in its own window, be sure to read up on the own_window_type settings and experiment.</p>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="http://conky.sourceforge.net/">http://conky.sourceforge.net/</a>&gt; </p>
<p> &lt;<a rel="nofollow" href="http://www.sourceforge.net/projects/conky">http://www.sourceforge.net/projects/conky</a>&gt; </p>
<p> &lt;<a rel="nofollow" href="http://wiki.conky.be">http://wiki.conky.be</a>&gt; </p>
<p> #conky on irc.freenode.net</p>
<h2>COPYING</h2>
<p> Copyright (c) 2005-2012 Brenden Matthews, Philip Kovacs, et. al. Any original torsmo code is licensed under the BSD license (see LICENSE.BSD for a copy). All code written since the fork of torsmo is licensed under the GPL (see LICENSE.GPL for a copy), except where noted differently (such as in portmon code, timed thread code, and audacious code which are LGPL, and prss which is an MIT-style license).</p>
<h2>AUTHORS</h2>
<p> The Conky dev team (see AUTHORS for a full list of contributors). </p>
<h2>Index</h2>
