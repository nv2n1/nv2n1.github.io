---
title: "byobu(1)"
name: "byobu"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu/"
description: "byobu – wrapper script for seeding a user’s byobu configuration and launching a text based window manager (either screen or tmux)"
---

<h2>NAME</h2>
<p> byobu &#8211; wrapper script for seeding a user&#8217;s byobu configuration and launching a text based window manager (either screen or tmux) </p>
<h2>SYNOPSIS</h2>
<p> <code>byobu</code> [screen options] </p>
<p> <code>byobu-screen</code> [screen options] </p>
<p> <code>byobu-tmux</code> [tmux options] </p>
<p> Options to <code>byobu</code> are simply passed through <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1) or <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1). </p>
<h2>DESCRIPTION</h2>
<p> <code>byobu</code> is a script that launches a text based window manager (either <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1) or <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1)) in the byobu configuration. This enables the display of system information and status notifications within two lines at the bottom of the screen session. It also enables multiple tabbed terminal sessions, accessible through simple keystrokes. </p>
<p> <code>byobu</code> currently defaults to using <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1) (if present) as the backend, however, this can be overridden with the <code><a href="/docs/linux/man/1-byobu-select-backend/">byobu-select-backend</a></code>(1) utility. </p>
<p> Note that BYOBU_CONFIG_DIR=<i>$XDG_CONFIG_HOME/byobu</i> if defined, and <i>$HOME/.byobu</i> otherwise. </p>
<h2>BACKGROUND COLORS</h2>
<p> The background colors of the <code>byobu</code> status lines can be adjusted by editing the files <i>$HOME/.byobu/color</i> (for <code>byobu-screen</code>) and <i>$HOME/.byobu/color.tmux</i> (for <code>byobu-tmux</code>). The command <code>Ctrl-Shift-F5</code> will change the background to a randomly selected color when running in <code>byobu-tmux</code> mode. Simply remove those files to return to the default color configuration. </p>
<h2>STATUS NOTIFICATIONS</h2>
<p> <code>byobu</code> supports a number of unique and interesting status notifications across the lowest two lines in the screen. Each status notification item is independently configurable, enabled and disabled by the configuration utility. The guide below helps identify each status item (in alphabetical order): </p>
<p> <code>apport</code> &#8211; symbol displayed if there are pending crash reports; {!} symbol displayed on the lower bar toward the left, in black on an orange background </p>
<p> <code>arch</code> &#8211; system architecture; displayed on the lower bar toward the left, in the default text color on the default background color </p>
<p> <code>battery</code> &#8211; battery information; display on the lower bar toward the right; &#8211; indicates discharging, + indicates charging, = indicates fully charged; when charging or discharging, the current battery capacity as a percentage is displayed; the colours green, yellow, and red are used to give further indication of the battery&#8217;s charge state; you may override the detected battery by setting BATTERY=/proc/acpi/battery/BAT0 in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>cpu_count</code> &#8211; the number of cpu&#8217;s or cores on the system; displayed in the lower bar toward the right in the default text color on the default background, followed by a trailing &#8216;x&#8217; </p>
<p> <code>cpu_freq</code> &#8211; the current frequency of the cpu in GHz; displayed in the lower bar toward the right in white text on a light blue background </p>
<p> <code>cpu_temp</code> &#8211; the cpu temperature in Celsius (default) or Fahrenheit, configure TEMP=F or TEMP=C in <i>$BYOBU_CONFIG_DIR/statusrc</i>; displayed in the lower bar toward the right in yellow text on a black background; you may override the detected cpu temperature device by setting MONITORED_TEMP=/proc/acpi/whatever in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>custom</code> &#8211; user defined custom scripts; must be executable programs of any kind in <i>$BYOBU_CONFIG_DIR/bin</i>; must be named N_NAME, where N is the frequency in seconds to refresh the status indicator, and NAME is the name of the script; N should not be less than 5 seconds; the script should echo a small amount of text to standard out, standard error is discarded; the indicator will be displayed in the lower panel, in default colors, unless you manually specify the colors in your script&#8217;s output; BEWARE, cpu-intensive custom scripts may impact your overall system performance and could upset your system administrator! In fact, you can easily copy and modify <code>any</code> status script usually found in <i>/usr/lib/byobu/*</i> to your local <i>$HOME/.byobu/</i> directory.<br />
&nbsp;<wbr>&nbsp;<wbr>Example:&nbsp;<wbr><i>$BYOBU_CONFIG_DIR/bin/1000_uname</i><br />
&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>printf&nbsp;<wbr>&quot;{=&nbsp;<wbr>bw}%s{-}&quot;&nbsp;<wbr>&quot;$(uname -r)&quot; </p>
<p> <code>date</code> &#8211; the system date in YYYY-MM-DD format, or you can set this to any valid <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) you like in <i>$BYOBU_CONFIG_DIR/datetime</i>; displayed in the lower on the far right in the default text color on the default background </p>
<p> <code>disk</code> &#8211; total disk space available and total used on / directory; displayed in the lower bar on the far right in white text on a light purple background; override the default directory by specifying an alternate mount point with MONITORED_DISK=/wherever in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>disk_io</code> &#8211; instantaneous read/write througput in kB/s or MB/s over the last 3 seconds; displayed in the lower bar toward the right in white text on a light purple background with a leading &#8216;&lt;&#8216; sign indicating &#8216;read speed&#8217; and &#8216;&gt;&#8217; sign indicating &#8216;write speed&#8217;; override the default monitored disk by specifying an alternate device with MONITORED_DISK=/dev/sdb, and override the default DISK_IO_THRESHOLD=50 (kB/s) in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>distro</code> &#8211; OS/distribution name of the release running on the current system as reported by <code><a href="/docs/linux/man/1-lsb_release/">lsb_release</a>(1)</code> or <i>/etc/issue</i>; displayed in the lower bar in bold black text toward the left on a grey background; you may override the detected release with DISTRO=Whatever in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>ec2_cost</code> &#8211; an estimation of the cost of the current boot of the system in terms of the Amazon EC2 billing model; displayed in the lower bar toward the right in green text on a black background; the monetary units are US Dollars &#8216;$&#8217;; this plugin only works when an AWS-compatible metadata server is available at <i><a rel="nofollow" href="http://169.254.169.254">http://169.254.169.254</a></i> </p>
<p> <code>entropy</code> &#8211; a count of the system&#8217;s current entropy in bytes; displayed in the lower bar toward the right in yellow text on a dark grey background; there is a leading &#8216;e&#8217; to indicate &#8216;entropy&#8217; </p>
<p> <code>raid</code> &#8211; note very prominently if there is a RAID failure detected, in red blinking text on a white background; the term &#8216;RAID&#8217; notes that there is something wrong with the RAID, and if there is a rebuild/resync in progress, the percent complete is also shown </p>
<p> <code>rcs_cost</code> &#8211; an estimation of the cost of the current boot of the system in terms of the Rackspace Cloud Server billing model; displayed in the lower bar toward the right in green text on a black background; there is a leading &#8216;~&#8217; to indicate that this is an estimation, and the monetary units are US Dollars &#8216;$&#8217; </p>
<p> <code>fan_speed</code> &#8211; cpu or system fan speed as reported by lm-sensors; displayed in the lower bar toward the right in black text on a grey background; there is a trailing &#8216;rpm&#8217; for units; you may override the detected fan by setting FAN=/sys/path/to/your/fan1_input in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>hostname</code> &#8211; the hostname of the system; displayed in the upper bar on the far right in bold black text on a grey background; there is a leading &#8216;@&#8217; symbol if the username status is also enabled </p>
<p> <code>ip_address</code> &#8211; the IPv4 address of the system in dotted decimal form; displayed in the upper bar on the far right in bold black text on a grey background; you can override and display your IPv6 address by setting &#8216;IPV6=1&#8217;, and you can show your external ip address by setting &#8216;IP_EXTERNAL=1&#8217; in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>ip_address4</code> &#8211; the IPv4 address of the system in dotted decimal form; displayed in the upper bar on the far right in bold black text on a grey background; you can show your external ip address by setting &#8216;IP_EXTERNAL=1&#8217; in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>ip_address6</code> &#8211; the IPv6 address of the system; displayed in the upper bar on the far right in bold black text on a grey background; you can show your external ip address by setting &#8216;IP_EXTERNAL=1&#8217; in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>load_average</code> &#8211; the system load average over the last 1 minute; displayed in the lower bar toward the right in black text on a yellow background </p>
<p> <code>logo</code> &#8211; an approximation of the current operating system&#8217;s logo; displayed in the lower bar on the far left; you may customize this logo by setting a chosen logo in <i>$BYOBU_CONFIG_DIR/logo</i>, or you may override this with LOGO=:-D in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>mail</code> &#8211; system mail for the current user; the letter &#8216;[M]&#8217; is displayed in the lower bar toward the left in black text on a grey background </p>
<p> <code>memory</code> &#8211; total memory available and used percentage in the system; displayed in the lower bar toward the right in white text on a green background </p>
<p> <code>menu</code> &#8211; a simple indicator directing new users to use the F9 keybinding to access the byobu menu </p>
<p> <code>network</code> &#8211; instantaneous upload/download bandwidth in [GMk]bps over the last 3 seconds; nothing is displayed if traffic is 0; displayed in the lower bar toward the left in white text on a purple background with a leading &#8216;^&#8217; sign indicating &#8216;up&#8217; and &#8216;v&#8217; sign indicating &#8216;down&#8217;; override the default interface by specifying an alternate interface with MONITORED_NETWORK=eth1, and override the default units (bits) with NETWORK_UNITS=bytes, and override the default NETWORK_THRESHOLD=20 (kbps) in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>notify_osd</code> &#8211; Send on-screen notification messages to screen&#8217;s notification buffer </p>
<p> <code>processes</code> &#8211; total number of processes running on the system; displayed in the lower bar in white text on a dark yellow background with a trailing &#8216;&amp;&#8217; indicating &#8216;background processes&#8217; </p>
<p> <code>reboot_required</code> &#8211; symbol present if a reboot is required following a system update; displayed in the lower bar white text on a blue background by the symbol &#8216;(R)&#8217;; additionally, reboot_required will print &#8216;&lt;F5&gt;&#8217; in white text on a blue background, if Byobu requires you to reload your profile to affect some changes; it will also detect if your system is currently in <code><a href="/docs/linux/man/8-powernap/">powernap</a></code>(8) state and if so print &#8216;.zZ&#8217;. </p>
<p> <code>release</code> &#8211; OS/distribution name of the release running on the current system as reported by <code><a href="/docs/linux/man/1-lsb_release/">lsb_release</a>(1)</code> or <i>/etc/issue</i>; displayed in the lower bar in bold black text toward the left on a grey background; you may override the detected release with RELEASE=Whatever in <i>$BYOBU_CONFIG_DIR/statusrc</i>; you may also abbreviate the release string to N characters by setting RELEASE_ABBREVIATED=N in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<p> <code>services</code> &#8211; users can configure a list of services to monitor, define the SERVICES variable in <i>$BYOBU_CONFIG_DIR/statusrc</i>, a whitespace separated of services, each service should include the init name of the service, then a pipe, and then an abbreviated name or symbol to display when running (e.g. SERVICES=&quot;ssh|ssh apache2|http&quot;); displayed in the lower bar toward the center in cyan on a white background </p>
<p> <code>session</code> &#8211; byobu session name (only supported in <code><a href="/docs/linux/man/1-byobu-tmux/">byobu-tmux</a></code>(1)); displayed in the lower bar on the left in underlined black text on a white background </p>
<p> <code>swap</code> &#8211; total swap space and total used as a percentage of the total available; displayed in the lower bar toward the right in white text on a light green background with a trailing &#8216;%&#8217; sign </p>
<p> <code>time</code> &#8211; the system time in HH:MM:SS format (by default), or you can set this to any valid <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) you like in <i>$BYOBU_CONFIG_DIR/datetime</i>; displayed in the lower bar on the far right in the default text and default background colors </p>
<p> <code>time_binary</code> &#8211; only for the hard core geek, the local system time in binary; requires UTF-8 support in a VERY recent version of GNU Screen; displayed in the lower bar on the far right in the default text and background colors </p>
<p> <code>time_utc</code> &#8211; the UTC system time in HH:MM format; displayed in the lower bar on the far right in dark text on a light background </p>
<p> <code>updates_available</code> &#8211; the number of updates available on the system; displayed in the lower bar toward the right in white text on a red background with a trailing &#8216;!&#8217; sign; if any updates are marked &#8216;security updates&#8217;, then there will be a total of two trailing exclamation points, &#8216;!!&#8217; </p>
<p> <code>uptime</code> &#8211; the total system uptime since last boot; displayed in the lower bar toward the right in blue text on a grey background </p>
<p> <code>users</code> &#8211; the number of remote users logged into the system via sshd, empty if 0 users; displayed in the lower bar toward the right in red text on a grey background with a trailing &#8216;#&#8217; sign; set USERS_DISTINCT=1 to instead count the number of distinct users logged into the system (rather than open ssh sessions) </p>
<p> <code>whoami</code> &#8211; the name of the user who owns the screen session; displayed in the upper bar toward the far right in bold black text on a grey background </p>
<p> <code>wifi_quality</code> &#8211; the connection rate and signal quality of the wifi connection; displayed in the lower bar toward the right in black text on a cyan background; the connection rate is in &#8216;Mb/s&#8217; and the signal quality is as a percentage with a trailing &#8216;%&#8217;; override the default interface by specifying an alternate interface with MONITORED_NETWORK=wlan0 in <i>$BYOBU_CONFIG_DIR/statusrc</i> </p>
<h2>SESSIONS</h2>
<p> Byobu name screen sessions &quot;byobu&quot;, if unspecified. To hide sessions from <code><a href="/docs/linux/man/1-byobu-select-session/">byobu-select-session</a></code>(1), prepend a &quot;.&quot; to the beginning of the session name, like: </p>
<p>&nbsp;<wbr>byobu -S .hidden </p>
<h2>WINDOWS</h2>
<p> Each open window in the screen session is displayed in the upper bar toward the far left. These are numbered, and include indicators as to activity in the window (see &quot;activity&quot; in <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1) for symbol definitions). The current active window is highlighted by inverting the background/text from the rest of the window bar. </p>
<p> Users can create a list of windows to launch at startup in <i>$BYOBU_CONFIG_DIR/windows</i>. This file is the same syntax as <i>~/.screenrc</i>, each line specifying a window using the &quot;screen&quot; command, as described in <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1). </p>
<p> User can also launch Byobu with unique window sets. Users can store these as <i>$BYOBU_CONFIG_DIR/windows.[NAME]</i>, and launch Byobu with the environment variable <code>BYOBU_WINDOWS</code>. </p>
<p> For example:<br />
&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>cat&nbsp;<wbr>$BYOBU_CONFIG_DIR/windows.ssh_sessions<br />
&nbsp;<wbr>&nbsp;<wbr>screen -t localhost bash<br />
&nbsp;<wbr>&nbsp;<wbr>screen -t aussie ssh root [at] aussie<br />
&nbsp;<wbr>&nbsp;<wbr>screen -t beagle ssh root [at] beagle<br />
&nbsp;<wbr>&nbsp;<wbr>screen -t collie ssh root [at] collie<br />
&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>BYOBU_WINDOWS=ssh_sessions byobu </p>
<h2>UNITS OF MEASURE</h2>
<p> byobu uses binary for capacity measurements of KB, MB, GB, and TB. This means multiples of 1024 rather than multiples of 1000, in accordance with JEDEC Standard 100B.01 for disk and memory capacity measurements. See:<br />
&nbsp;<wbr>*&nbsp;<wbr><a rel="nofollow" href="http://en.wikipedia.org/wiki/JEDEC_memory_standards">http://en.wikipedia.org/wiki/JEDEC_memory_standards</a> </p>
<p> byobu uses decimal for measurements of network data transfer, meaning multiple of 1000, rather than 1024. See:<br />
&nbsp;<wbr>*&nbsp;<wbr><a rel="nofollow" href="http://en.wikipedia.org/wiki/Data_rate_units">http://en.wikipedia.org/wiki/Data_rate_units</a> </p>
<h2>KEYBINDINGS</h2>
<p> byobu keybindings can be user defined in /usr/share/byobu/keybindings/ (or within .screenrc if byobu-export was used). The common key bindings are: </p>
<p> <code>F2</code> &#8211; Create a new window </p>
<p> <code>F3</code> &#8211; Move to previous window </p>
<p> <code>F4</code> &#8211; Move to next window </p>
<p> <code>F5</code> &#8211; Reload profile </p>
<p> <code>F6</code> &#8211; Detach from this session </p>
<p> <code>F7</code> &#8211; Enter copy/scrollback mode </p>
<p> <code>F8</code> &#8211; Re-title a window </p>
<p> <code>F9</code> &#8211; Configuration Menu </p>
<p> <code>F12</code> &#8211; Lock this terminal </p>
<p> <code>shift-F2</code> &#8211; Split the screen horizontally </p>
<p> <code>ctrl-F2</code> &#8211; Split the screen vertically </p>
<p> <code>shift-F3</code> &#8211; Shift the focus to the previous split region </p>
<p> <code>shift-F4</code> &#8211; Shift the focus to the next split region </p>
<p> <code>shift-F5</code> &#8211; Join all splits </p>
<p> <code>ctrl-F6</code> &#8211; Remove this split </p>
<p> <code>ctrl-F5</code> &#8211; Reconnect GPG and SSH sockets </p>
<p> <code>shift-F6</code> &#8211; Detach, but do not logout </p>
<p> <code>alt-pgup</code> &#8211; Enter scrollback mode </p>
<p> <code>alt-pgdn</code> &#8211; Enter scrollback mode </p>
<p> <code>Ctrl-a $</code> &#8211; show detailed status </p>
<p> <code>Ctrl-a R</code> &#8211; Reload profile </p>
<p> <code>Ctrl-a !</code> &#8211; Toggle key bindings on and off </p>
<p> <code>Ctrl-a k</code> &#8211; Kill the current window </p>
<p> <code>Ctrl-a ~</code> &#8211; Save the current window&#8217;s scrollback buffer </p>
<h2>SCROLLBACK, COPY, PASTE MODES</h2>
<p> Each window in Byobu has up to 10,000 lines of scrollback history, which you can enter and navigate using the <code>alt-pgup</code> and <code>alt-pgdn</code> keys. Exit this scrollback mode by hitting <code>enter</code>. You can also easily copy and paste text from scrollback mode. To do so, enter scrollback using <code>alt-pgup</code> or <code>alt-pgdn</code>, press the <code>spacebar</code> to start highlighting text, use <code>up/down/left/right/pgup/pgdn</code> to select the text, and press <code>enter</code> to copy the text. You can then paste the text using <code>alt-insert</code> or <code>ctrl-a-]</code>. </p>
<h2>BUGS</h2>
<p> For Byobu colors to work properly, older versions of GNU Screen require a 1-line patch to adjust MAX_WINMSG_REND in screen.c. The change is in GNU Screen&#8217;s upstream source control system as of 2010-01-26, but GNU Screen has not released a new upstream version in several years. You can disable colors entirely by setting MONOCHROME=1 in <i>$BYOBU_CONFIG_DIR/statusrc</i>. For more information, see:<br />
&nbsp;<wbr>*&nbsp;<wbr><a rel="nofollow" href="http://savannah.gnu.org/bugs/?22146">http://savannah.gnu.org/bugs/?22146</a> </p>
<p> PuTTY users have reported that the F2, F3, and F4 shortcut keys are not working properly. PuTTY sends the same escape sequences as the linux console for F1-F4 by default. You can fix this problem in the PuTTY config, Terminal -&gt; Keyboard -&gt; Function keys: Xterm R6. See: <i><a rel="nofollow" href="http://www.mail-archive.com/screen-users@gnu.org/msg01525.html">http://www.mail-archive.com/screen-users@gnu.org/msg01525.html</a></i> </p>
<p> PuTTY users should configure enable UTF-8 characters in order to fix status refresh issues. You can fix this problem in the PuTTY configuration, Window -&gt; Translation: select UTF-8. </p>
<p> Apple Mac OSX terminal users have reported &#8216;flashing text&#8217;. You can fix this in the advanced settings of the terminal application, with &#8216;Declare Terminal As: xterm-color&#8217;. </p>
<p> Apple Mac keyboard users may need to specify a vt100 terminal by adding this to your OSX profile, in order to get Byobu&#8217;s function keys and colors to work:<br />
&nbsp;<wbr>&nbsp;<wbr>alias ssh=&#8217;TERM=vt100 ssh&#8217; </p>
<p> Users of a non-UTF-8 locale (such as cs_CZ charset ISO-8859-2), may need to add &quot;defutf8 off&quot; to <i>~/.screenrc</i>, if some characters are rendering as &quot;?&quot;. </p>
<p> Users who customize their PS1 prompt need to put this setting in <i>~/.bashrc</i>, rather than <i>~/.profile</i>, in order for it to work correctly with Byobu. </p>
<p> If you run <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1) under <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8), you <code>must</code> use the -H option, such that the user&#8217;s $HOME directory environment variable is set properly. Otherwise, <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1) will create a bunch of directories in the $SUDO_USER&#8217;s $HOME, but will be owned by root. To prevent this from happening, <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1) will simply refuse to run if $USER does not own $HOME. </p>
<p> Byobu requires a suitable <code><a href="/docs/linux/man/3-ulimit/">ulimit</a></code>(3) values to run. If you get an error at startup saying, &#8216;pipe: too many open files&#8217;, then check your ulimit -a values, as your &quot;open files&quot; or &quot;max user processes&quot; are too low. In this case, you will probably need to run simple <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1) </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-screen/">screen</a></code>(1), <code><a href="/docs/linux/man/1-byobu-config/">byobu-config</a></code>(1), <code><a href="/docs/linux/man/1-byobu-export/">byobu-export</a></code>(1), <code><a href="/docs/linux/man/1-byobu-status/">byobu-status</a></code>(1), <code><a href="/docs/linux/man/1-byobu-status-detail/">byobu-status-detail</a>(1), <a href="/docs/linux/man/1-byobu-enable/">byobu-enable</a>(1), <a href="/docs/linux/man/1-byobu-launch/">byobu-launch</a>(1), <a href="/docs/linux/man/1-byobu-select-backend/">byobu-select-backend</a></code>(1), <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1)</p>
<dd>
<dt><i><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the utility were written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
