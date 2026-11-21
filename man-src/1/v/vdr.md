---
title: "vdr(1)"
name: "vdr"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdr/"
description: "vdr – the Video Disk Recorder"
---

<h2>NAME</h2>
<p> vdr &#8211; the Video Disk Recorder</p>
<h2>SYNOPSIS</h2>
<p> <code>vdr</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>vdr</code> implements a complete digital Set-Top Box and Video Recorder. It can work with signals received from satellites (DVB-S) as well as cable (DVB-C) and terrestrial (DVB-T) signals. </p>
<p> At least one DVB card is required to run <code>vdr</code>. With it you can watch live TV while recording one or more other broadcasts from the same transponder. It is also possible to start watching a recorded programme before the live broadcast has ended (<code>time shifting</code>). In order to record from different transponders simultaneously two or more DVB cards are necessary. By default <code>vdr</code> can support up to eight DVB cards. The primary DVB card (the one your TV set is connected to) can either be a &quot;full featured&quot; card, which means it contains an MPEG decoder and provides audio and video signal outputs, or you can use some third party plugin that implements software decoding of the MPEG data and displays it via the system&#8217;s graphics adapter. </p>
<p> <code>vdr</code> uses an On Screen Display (OSD) to display its menus. It can be controlled by the PC keyboard, the &quot;Linux Infrared Remote Control&quot; (LIRC), or any other means of remote control, implemented by a third party plugin. </p>
<p> Remote access is possible via the &quot;Simple Video Disk Recorder Protocol&quot; (SVDRP), which can be accessed on port 6419, for instance by <code>telnet</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>cmd</i><code>, &#8211;audio=</code><i>cmd</i></dt>
<dd> Send Dolby Digital audio to stdin of command <i>cmd</i>.</dd>
<dt><code>&#8211;cachedir=</code><i>dir</i></dt>
<dd> Save cache files in <i>dir</i> (default is to save them in the video directory).</dd>
<dt><code>-c&nbsp;<wbr></code><i>dir</i><code>, &#8211;config=</code><i>dir</i></dt>
<dd> Read config files from directory <i>dir</i> (default is to read them from /etc/vdr).</dd>
<dt><code>-d, &#8211;daemon</code></dt>
<dd> Run in daemon mode (implies &#8211;no-kbd).</dd>
<dt><code>-D&nbsp;<wbr></code><i>num</i><code>, &#8211;device=</code><i>num</i></dt>
<dd> Use only the given DVB device (<i>num</i> = 0, 1, 2&#8230;). There may be several <code>-D</code> options (by default all DVB devices will be used).</dd>
<dt><code>&#8211;dirnames=</code><i>path</i><code>[,</code><i>name</i><code>[,</code><i>enc</i><code>]]</code></dt>
<dd> Set the maximum directory path length to <i>path</i> (default is the maximum value allowed on the system). If <i>name</i> is also given, it defines the maximum directory name length (default is the maximum value allowed on the system). The optional <i>enc</i> can be 0 or 1, and controls whether special characters in directory names are encoded as hex values (default: 0). If <i>path</i> or <i>name</i> are left empty (as in &quot;,,1&quot; to only set <i>enc</i>), the defaults apply. The length of the video directory name and that of the actual recording directory is subtracted from <i>path</i>, to make sure the directory path will never become too long.</dd>
<dt><code>&#8211;edit=</code><i>rec</i></dt>
<dd> Edit the given recording. <i>rec</i> must be the full path name of an existing recording. The program will return immediately after editing the recording.</dd>
<dt><code>-E&nbsp;<wbr></code><i>file</i><code>, &#8211;epgfile=</code><i>file</i></dt>
<dd> Write the EPG data into the given <i>file</i> (default is <i>epg.data</i> in the cache directory). Use <code>-E-</code> to disable this. If <i>file</i> is a directory, the file <i>epg.data</i> will be created in that directory.</dd>
<dt><code>&#8211;filesize=</code><i>size</i></dt>
<dd> Limit video files to <i>size</i> bytes (default is 2000M). This option is only useful in conjunction with &#8211;edit, and must precede that option to have an effect. <i>size</i> is an integer number and may be followed by one of the letters K, M, G or T to abbreviate Kilo-, Mega-, Giga- or Terabyte, respectively. The given value is silently limited to the program&#8217;s internal minimum and maximum values.</dd>
<dt><code>&#8211;genindex=</code><i>rec</i></dt>
<dd> Generate the index file for the given recording. <i>rec</i> must be the full path name of an existing recording. The recording must be in TS format. If the recording already has an index file, it will be deleted before creating the new one. The program will return immediately after generating the index. Note that using this option while another instance of VDR is currently replaying the given recording, or if the recording has not been finished yet, may lead to unexpected results.</dd>
<dt><code>-g, &#8211;grab=</code><i>dir</i></dt>
<dd> Write images from the SVDRP command GRAB into the given directory <i>dir</i>. <i>dir</i> must be the full path name of an existing directory, without any &quot;..&quot;, double &#8216;/&#8217; or symlinks. By default, or if <code>-g-</code> is given, grabbing images to disk is disabled.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print a help message and exit.</dd>
<dt><code>-i&nbsp;<wbr></code><i>instance</i><code>, &#8211;instance=</code><i>instance</i></dt>
<dd> Use <i>instance</i> as the id of this VDR instance (default is 0). In an environment where several instances of VDR use the same video directory, this parameter can be set to a positive integer value that&#8217;s unique for each instance, so that they won&#8217;t interfere with each other in case they record exactly the same broadcast. The number given here will be part of the directory name in which the recordings will be stored.</dd>
<dt><code>-l&nbsp;<wbr></code><i>level</i><code>, &#8211;log=</code><i>level</i></dt>
<dd> Set logging to <i>level</i>. <code>0</code>&nbsp;<wbr>=&nbsp;<wbr>no logging, <code>1</code>&nbsp;<wbr>=&nbsp;<wbr>errors only, <code>2</code>&nbsp;<wbr>=&nbsp;<wbr>errors and info, <code>3</code>&nbsp;<wbr>=&nbsp;<wbr>errors, info and debug. The default logging level is <code>3</code>. If logging should be done to LOG_LOCAL<i>n</i> instead of LOG_USER, add &#8216;.n&#8217; to LEVEL, as in 3.7 (n=0..7).</dd>
<dt><code>-L&nbsp;<wbr></code><i>dir</i><code>, &#8211;lib=</code><i>dir</i></dt>
<dd> Search for plugins in directory <i>dir</i> (default is /usr/lib64/vdr). There can be several <code>-L</code> options with different <i>dir</i> values. Each of them will apply to the <code>-P</code> options following it.</dd>
<dt><code>&#8211;lirc[=</code><i>path</i><code>]</code></dt>
<dd> Use a LIRC remote control device. If <i>path</i> is omitted, vdr uses <i>/var/run/lirc/lircd</i>.</dd>
<dt><code>&#8211;localedir=</code><i>dir</i></dt>
<dd> Search for locale files in <i>dir</i> (default is ./locale).</dd>
<dt><code>-m, &#8211;mute</code></dt>
<dd> Mute audio of the primary DVB device at startup.</dd>
<dt><code>&#8211;no-kbd</code></dt>
<dd> Don&#8217;t use the keyboard as an input device.</dd>
<dt><code>-p&nbsp;<wbr></code><i>port</i><code>, &#8211;port=</code><i>port</i></dt>
<dd> Use <i>port</i> for SVDRP. A value of <code>0</code> turns off SVDRP. The default SVDRP port is <code>6419</code>. You need to edit the file <i>svdrphosts.conf</i> in order to enable access to the SVDRP port.</dd>
<dt><code>-P&nbsp;<wbr></code><i>options</i><code>, &#8211;plugin=</code><i>options</i></dt>
<dd> Load a plugin, defined by the given <i>options</i>. The first word in <i>options</i> must be the name of an existing <code>vdr</code> plugin, optionally followed by a blank separated list of command line options for that plugin. If <i>options</i> contains any blanks, you need to enclose it in quotes, like for example </dd>
<p> <code>vdr -P &quot;abc -a -b xyz&quot;</code> </p>
<p> which would load a plugin named <code>abc</code>, giving it the command line options <code>-a -b xyz</code>. If you want to load all available plugins (without any particular options) you can use </p>
<p> <code>vdr -P &quot;*&quot;</code> </p>
<p> (note the quotes around the asterisk to prevent wildcard expansion).</p>
<dt><code>-r&nbsp;<wbr></code><i>cmd</i><code>, &#8211;record=</code><i>cmd</i></dt>
<dd> Call <i>cmd</i> before and after a recording. See the file <i>INSTALL</i> for more information.</dd>
<dt><code>&#8211;resdir=</code><i>dir</i></dt>
<dd> Read resource files from <i>dir</i> (default is to read them from the config directory).</dd>
<dt><code>-s&nbsp;<wbr></code><i>cmd</i><code>, &#8211;shutdown=</code><i>cmd</i></dt>
<dd> Call <i>cmd</i> to shutdown the computer. See the file <i>INSTALL</i> for more information.</dd>
<dt><code>&#8211;split</code></dt>
<dd> Split edited files at the editing marks. This option is only useful in conjunction with &#8211;edit, and must precede that option to have an effect.</dd>
<dt><code>-t&nbsp;<wbr></code><i>tty</i><code>, &#8211;terminal=</code><i>tty</i></dt>
<dd> Set the controlling terminal.</dd>
<dt><code>-u&nbsp;<wbr></code><i>user</i><code>, &#8211;user=</code><i>user</i></dt>
<dd> Run as user <i>user</i> in case vdr was started as user &#8216;root&#8217;. Starting vdr as &#8216;root&#8217; is necessary if the system time shall be set from the transponder data, but for security reasons vdr can switch to a lesser privileged user id during normal operation.</dd>
<dt><code>&#8211;userdump</code></dt>
<dd> Allow coredumps if -u is given (only for debugging).</dd>
<dt><code>&#8211;vfat</code></dt>
<dd> For backwards compatibility (same as &#8211;dirnames= 250,40,1).</dd>
<dt><code>-v&nbsp;<wbr></code><i>dir</i><code>, &#8211;video=</code><i>dir</i></dt>
<dd> Use <i>dir</i> as video directory. The default is <i>/var/lib/vdr/video</i>.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Print version information and exit.</dd>
<dt><code>-w&nbsp;<wbr></code><i>sec</i><code>, &#8211;watchdog=</code><i>sec</i></dt>
<dd> Activate the watchdog timer with a timeout of <i>sec</i> seconds. A value of <code>0</code> (default) disables the watchdog.</dd></dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGINT, SIGTERM</code></dt>
<dd> Program exits with status 0.</dd>
<dt><code>SIGHUP</code></dt>
<dd> Program exits with status 1. This can be used to force a reload, for example if an update has been installed.</dd></dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> Successful program execution.</dd>
<dt><code>1</code></dt>
<dd> An error has been detected which requires the DVB driver and <code>vdr</code> to be reloaded.</dd>
<dt><code>2</code></dt>
<dd> An non-recoverable error has been detected, <code>vdr</code> has given up.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>channels.conf</i></dt>
<dd> Channel configuration.</dd>
<dt><i>timers.conf</i></dt>
<dd> Timer configuration.</dd>
<dt><i>setup.conf</i></dt>
<dd> User definable setup.</dd>
<dt><i>commands.conf</i></dt>
<dd> User definable commands (executed from the <code>Commands</code> menu).</dd>
<dt><i>svdrphosts.conf</i></dt>
<dd> SVDRP host configuration, defining which hosts or networks are given access to the SVDRP port.</dd>
<dt><i>marks</i></dt>
<dd> Contains the editing marks defined for a recording.</dd>
<dt><i>info</i></dt>
<dd> Contains a description of the recording.</dd>
<dt><i>resume</i></dt>
<dd> Contains the index into the recording where the last replay session left off.</dd>
<dt><i>index</i></dt>
<dd> Contains the file number, offset and type of each frame of the recording.</dd>
<dt><i>remote.conf</i></dt>
<dd> Contains the key assignments for the remote control.</dd>
<dt><i>keymacros.conf</i></dt>
<dd> Contains user defined remote control key macros.</dd>
<dt><i>00001.ts&nbsp;<wbr></i>&#8230;&nbsp;<wbr><i>65535.ts</i></dt>
<dd> The actual data files of a recording.</dd>
<dt><i>epg.data</i></dt>
<dd> Contains all current EPG data. Can be used for external processing and will also be read at program startup to have the full EPG data available immediately.</dd>
<dt><i>.update</i></dt>
<dd> If this file is present in the video directory, its last modification time will be used to trigger an update of the list of recordings in the &quot;Recordings&quot; menu.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-vdr/">vdr</a></code>(5),<code>svdrp(1)</code></p>
<h2>AUTHOR</h2>
<p> Written by Klaus Schmidinger, with contributions from many others. See the file <i>CONTRIBUTORS</i> in the <code>vdr</code> source distribution.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;vdr-bugs [at] tvdr.de&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Klaus Schmidinger. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
