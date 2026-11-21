---
title: "mplayer(1)"
name: "mplayer"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mplayer/"
description: "mplayer – movie player mencoder – movie encoder"
---

<h2 class="name">NAME</h2>
<p> mplayer &#8211; movie player<br />
 mencoder &#8211; movie encoder </p>
<h2>SYNOPSIS</h2>
<p> <code>mplayer</code> [options] [file|URL|playlist|-]<br />
 <code>mplayer</code> [options] file1 [specific options] [file2] [specific options]<br />
 <code>mplayer</code> [options] {group of files and options} [group-specific options]<br />
 <code>mplayer</code> [br]://[title][/device] [options]<br />
 <code>mplayer</code> [dvd|dvdnav]://[title|[start_title]-end_title][/device] [options]<br />
 <code>mplayer</code> <a href="vcd://track[/device]">vcd://track[/device]</a><br />
 <code>mplayer</code> tv://[channel][/input_id] [options]<br />
 <code>mplayer</code> <a href="radio://[channel|frequency][/capture]">radio://[channel|frequency][/capture]</a> [options]<br />
 <code>mplayer</code> pvr:// [options]<br />
 <code>mplayer</code> <a href="dvb://[card_number@]channel">dvb://[card_number@]channel</a> [options]<br />
 <code>mplayer</code> mf://[filemask|@listfile] [-mf options] [options]<br />
 <code>mplayer</code> [cdda|cddb]://track[-endtrack][:speed][/device] [options]<br />
 <code>mplayer</code> <a href="cue://file[:track]">cue://file[:track]</a> [options]<br />
 <code>mplayer</code> [file|mms[t]|http|http_proxy|rt[s]p|ftp|udp|unsv|icyx|noicyx|smb]:// [user:pass@]URL[:port] [options]<br />
 <code>mplayer</code> <a href="sdp://file">sdp://file</a> [options]<br />
 <code>mplayer</code> <a href="mpst://host[:port]/URL">mpst://host[:port]/URL</a> [options]<br />
 <code>mplayer</code> <a href="tivo://host/[list|llist|fsid]">tivo://host/[list|llist|fsid]</a> [options]<br />
 <code>gmplayer</code> [options] [file|URL|playlist] [-skin skin]<br />
 <code>mencoder</code> [options] file [file|URL|-] [-o file | file://file | <a href="smb://[user:pass@]host/filepath]">smb://[user:pass@]host/filepath]</a><br />
 <code>mencoder</code> [options] file1 [specific options] [file2] [specific options]</p>
<h2>DESCRIPTION</h2>
<p> <code>mplayer</code> is a movie player for Linux (runs on many other platforms and CPU architectures, see the documentation). It plays most MPEG/VOB, AVI, ASF/WMA/WMV, RM, QT/MOV/MP4, Ogg/OGM, MKV, VIVO, FLI, NuppelVideo, yuv4mpeg, FILM and RoQ files, supported by many native and binary codecs. You can watch VCD, SVCD, DVD, Blu-ray, 3ivx, DivX 3/4/5, WMV and even H.264 movies, too. </p>
<p> MPlayer supports a wide range of video and audio output drivers. It works with X11, Xv, DGA, OpenGL, SVGAlib, fbdev, AAlib, libcaca, DirectFB, Quartz, Mac OS X CoreVideo, but you can also use GGI, SDL (and all their drivers), VESA (on every VESA-compatible card, even without X11), some low-level card-specific drivers (for Matrox, 3dfx and ATI) and some hardware MPEG decoder boards, such as the Siemens DVB, Hauppauge PVR (IVTV), DXR2 and DXR3/Hollywood+. Most of them support software or hardware scaling, so you can enjoy movies in fullscreen mode. </p>
<p> MPlayer has an onscreen display (OSD) for status information, nice big antialiased shaded subtitles and visual feedback for keyboard controls. European/ISO8859-1,2 (Hungarian, English, Czech, etc), Cyrillic and Korean fonts are supported along with 12 subtitle formats (MicroDVD, SubRip, OGM, SubViewer, Sami, VPlayer, RT, SSA, AQTitle, JACOsub, PJS and our own: MPsub) and DVD subtitles (SPU streams, VOBsub and Closed Captions). </p>
<p> <code>mencoder</code> (MPlayer&#8217;s Movie Encoder) is a simple movie encoder, designed to encode MPlayer-playable movies (see above) to other MPlayer-playable formats (see below). It encodes to MPEG-4 (DivX/Xvid), one of the libavcodec codecs and PCM/MP3/VBRMP3 audio in 1, 2 or 3 passes. Furthermore it has stream copying abilities, a powerful filter system (crop, expand, flip, postprocess, rotate, scale, noise, RGB/YUV conversion) and more. </p>
<p> <code>gmplayer</code> is MPlayer with a graphical user interface. Besides some own options (stored in gui.conf), it has the same options as MPlayer, however some MPlayer options will be stored in gui.conf so that they can be chosen independently from MPlayer. (See GUI CONFIGURATION FILE below.) </p>
<p> Usage examples to get you started quickly can be found at the end of this man page. </p>
<p> <code>Also see the HTML documentation!</code></p>
<h2>INTERACTIVE CONTROL</h2>
<p> MPlayer has a fully configurable, command-driven control layer which allows you to control MPlayer using keyboard, mouse, joystick or remote control (with LIRC). See the -input option for ways to customize it.</p>
<dl>
<dt><code>keyboard control</code></dt>
<dd>
</dd><dl>
<dl>
<dt>LEFT and RIGHT</dt>
<dd> Seek backward/forward 10 seconds.</dd>
<dt>UP and DOWN</dt>
<dd> Seek forward/backward 1 minute.</dd>
<dt>PGUP and PGDWN</dt>
<dd> Seek forward/backward 10 minutes.</dd>
<dt>[ and ]</dt>
<dd> Decrease/increase current playback speed by 10%.</dd>
<dt>{ and }</dt>
<dd> Halve/double current playback speed.</dd>
<dt>BACKSPACE</dt>
<dd> Reset playback speed to normal.</dd>
<dt>&lt; and &gt;</dt>
<dd> Go backward/forward in the playlist.</dd>
<dt>ENTER</dt>
<dd> Go forward in the playlist, even over the end.</dd>
<dt>HOME and END</dt>
<dd> next/previous playtree entry in the parent list</dd>
<dt>INS and DEL (ASX playlist only)</dt>
<dd> next/previous alternative source.</dd>
<dt>p / SPACE</dt>
<dd> Pause (pressing again unpauses).</dd>
<dt>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Step forward. Pressing once will pause movie, every consecutive press will play one frame and then go into pause mode again (any other key unpauses).</dd>
<dt>q / ESC</dt>
<dd> Stop playing and quit.</dd>
<dt>U&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Stop playing (and quit if -idle is not used).</dd>
<dt>+ and &#8211;</dt>
<dd> Adjust audio delay by +/- 0.1 seconds.</dd>
<dt>/ and *</dt>
<dd> Decrease/increase volume.</dd>
<dt>9 and 0</dt>
<dd> Decrease/increase volume.</dd>
<dt>( and )</dt>
<dd> Adjust audio balance in favor of left/right channel.</dd>
<dt>m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Mute sound.</dd>
<dt>_ (MPEG-TS, AVI and libavformat only)</dt>
<dd> Cycle through the available video tracks.</dd>
<dt># (DVD, Blu-ray, MPEG, Matroska, AVI and libavformat only)</dt>
<dd> Cycle through the available audio tracks.</dd>
<dt>TAB (MPEG-TS and libavformat only)</dt>
<dd> Cycle through the available programs.</dd>
<dt>f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Toggle fullscreen (also see -fs).</dd>
<dt>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Toggle stay-on-top (also see -ontop).</dd>
<dt>w and e</dt>
<dd> Decrease/increase pan-and-scan range.</dd>
<dt>o&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Toggle OSD states: none / seek / seek + timer / seek + timer + total time.</dd>
<dt>d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Toggle frame dropping states: none / skip display / skip decoding (see -framedrop and -hardframedrop).</dd>
<dt>v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Toggle subtitle visibility.</dd>
<dt>j and J</dt>
<dd> Cycle through the available subtitles.</dd>
<dt>y and g</dt>
<dd> Step forward/backward in the subtitle list.</dd>
<dt>F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Toggle displaying &quot;forced subtitles&quot;.</dd>
<dt>a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Toggle subtitle alignment: top / middle / bottom.</dd>
<dt>x and z</dt>
<dd> Adjust subtitle delay by +/- 0.1 seconds.</dd>
<dt>c (-capture only)</dt>
<dd> Start/stop capturing the primary stream.</dd>
<dt>r and t</dt>
<dd> Move subtitles up/down.</dd>
<dt>i (-edlout mode only)</dt>
<dd> Set start or end of an EDL skip and write it out to the given file.</dd>
<dt>s (-vf screenshot only)</dt>
<dd> Take a screenshot.</dd>
<dt>S (-vf screenshot only)</dt>
<dd> Start/stop taking screenshots.</dd>
<dt>I&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Show filename on the OSD.</dd>
<dt>P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Show progression bar, elapsed time and total duration on the OSD.</dd>
<dt>! and @</dt>
<dd> Seek to the beginning of the previous/next chapter.</dd>
<dt>D (-vo xvmc, -vo vdpau, -vf yadif, -vf kerndeint only)</dt>
<dd> Activate/deactivate deinterlacer.</dd>
<dt>A</dt>
<dd> Cycle through the available DVD angles.</dd></dl>
</dl>
</dl>
<dl>
<dt>
</dt><dd> (The following keys are valid only when using a hardware accelerated video output (xv, (x)vidix, (x)mga, etc), the software equalizer (-vf eq or -vf eq2) or hue filter (-vf hue).)</dd></dl>
<dl>
<dl>
<dt>1 and 2</dt>
<dd> Adjust contrast.</dd>
<dt>3 and 4</dt>
<dd> Adjust brightness.</dd>
<dt>5 and 6</dt>
<dd> Adjust hue.</dd>
<dt>7 and 8</dt>
<dd> Adjust saturation.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> (The following keys are valid only when using the quartz or corevideo video output driver.)</dd></dl>
<dl>
<dl>
<dt>command + 0</dt>
<dd> Resize movie window to half its original size.</dd>
<dt>command + 1</dt>
<dd> Resize movie window to its original size.</dd>
<dt>command + 2</dt>
<dd> Resize movie window to double its original size.</dd>
<dt>command + f</dt>
<dd> Toggle fullscreen (also see -fs).</dd>
<dt>command + [ and command + ]</dt>
<dd> Set movie window alpha.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> (The following keys are valid only when using the sdl video output driver.)</dd></dl>
<dl>
<dl>
<dt>c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Cycle through available fullscreen modes.</dd>
<dt>n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Restore original mode.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> (The following keys are valid if you have a keyboard with multimedia keys.)</dd></dl>
<dl>
<dl>
<dt>PAUSE</dt>
<dd> Pause.</dd>
<dt>STOP&nbsp;</dt>
<dd> Stop playing and quit.</dd>
<dt>PREVIOUS and NEXT</dt>
<dd> Seek backward/forward 1 minute.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> (The following keys are only valid if you compiled with TV or DVB input support and will take precedence over the keys defined above.)</dd></dl>
<dl>
<dl>
<dt>h and k</dt>
<dd> Select previous/next channel.</dd>
<dt>n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Change norm.</dd>
<dt>u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Change channel list.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> (The following keys are only valid if you compiled with dvdnav support: They are used to navigate the menus.)</dd></dl>
<dl>
<dl>
<dt>keypad 8</dt>
<dd> Select button up.</dd>
<dt>keypad 2</dt>
<dd> Select button down.</dd>
<dt>keypad 4</dt>
<dd> Select button left.</dd>
<dt>keypad 6</dt>
<dd> Select button right.</dd>
<dt>keypad 5</dt>
<dd> Return to main menu.</dd>
<dt>keypad 7</dt>
<dd> Return to nearest menu (the order of preference is: chapter-&gt;title-&gt;root).</dd>
<dt>keypad ENTER</dt>
<dd> Confirm choice.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> (The following keys are used for controlling TV teletext. The data may come from either an analog TV source or an MPEG transport stream.)</dd></dl>
<dl>
<dl>
<dt>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Switch teletext on/off.</dd>
<dt>Q and W</dt>
<dd> Go to next/prev teletext page.</dd></dl>
</dl>
<dl>
<dt><code>mouse control</code></dt>
<dd>
</dd><dl>
<dl>
<dt>button 3 and button 4</dt>
<dd> Seek backward/forward 1 minute.</dd>
<dt>button 5 and button 6</dt>
<dd> Decrease/increase volume.</dd></dl>
</dl>
<dt><code>joystick control</code></dt>
<dd>
</dd><dl>
<dl>
<dt>left and right</dt>
<dd> Seek backward/forward 10 seconds.</dd>
<dt>up and down</dt>
<dd> Seek forward/backward 1 minute.</dd>
<dt>button 1</dt>
<dd> Pause.</dd>
<dt>button 2</dt>
<dd> Toggle OSD states: none / seek / seek + timer / seek + timer + total time.</dd>
<dt>button 3 and button 4</dt>
<dd> Decrease/increase volume.</dd></dl>
</dl>
</dl>
<h2>USAGE</h2>
<p> Every &#8216;flag&#8217; option has a &#8216;noflag&#8217; counterpart, e.g. the opposite of the -fs option is -nofs. </p>
<p> If an option is marked as (XXX only), it will only work in combination with the XXX option or if XXX is compiled in. </p>
<p> <i>NOTE:</i> The suboption parser (used for example for -ao pcm suboptions) supports a special kind of string-escaping intended for use with external GUIs.<br />
 It has the following format:<br />
 %n%string_of_length_n<br />
 <i>EXAMPLES:</i><br />
 mplayer -ao pcm:file=%10%C:test.wav test.avi<br />
 Or in a script:<br />
 mplayer -ao pcm:file=%`expr length &quot;$NAME&quot;`%&quot;$NAME&quot; test.avi </p>
<h2>CONFIGURATION FILES</h2>
<p> You can put all of the options in configuration files which will be read every time MPlayer/MEncoder is run. The system-wide configuration file &#8216;mplayer.conf&#8217; is in your configuration directory (e.g. /etc/mplayer or /usr/local/etc/mplayer), the user specific one is &#8216;~/.mplayer/config&#8217;. The configuration file for MEncoder is &#8216;mencoder.conf&#8217; in your configuration directory (e.g. /etc/mplayer or /usr/local/etc/mplayer), the user specific one is &#8216;~/.mplayer/mencoder.conf&#8217;. User specific options override system-wide options (in case of <code>gmplayer</code>, gui.conf options override user specific options) and options given on the command line override all. The syntax of the configuration files is &#8216;option=&lt;value&gt;&#8217;, everything after a &#8216;#&#8217; is considered a comment. Options that work without values can be enabled by setting them to &#8216;yes&#8217; or &#8216;1&#8217; or &#8216;true&#8217; and disabled by setting them to &#8216;no&#8217; or &#8216;0&#8217; or &#8216;false&#8217;. Even suboptions can be specified in this way. </p>
<p> You can also write file-specific configuration files. If you wish to have a configuration file for a file called &#8216;movie.avi&#8217;, create a file named &#8216;movie.avi.conf&#8217; with the file-specific options in it and put it in ~/.mplayer/. You can also put the configuration file in the same directory as the file to be played, as long as you give the -use-filedir-conf option (either on the command line or in your global config file). If a file-specific configuration file is found in the same directory, no file-specific configuration is loaded from ~/.mplayer. In addition, the -use-filedir-conf option enables directory-specific configuration files. For this, MPlayer first tries to load a mplayer.conf from the same directory as the file played and then tries to load any file-specific configuration. </p>
<p> <i>EXAMPLE MPLAYER CONFIGURATION FILE:</i> </p>
<pre>
# Use Matrox driver by default.
vo=xmga
# I love practicing handstands while watching videos.
flip=yes
# Decode/encode multiple files from PNG,
# start with mf://filemask
mf=type=png:fps=25
# Eerie negative images are cool.
vf=eq2=1.0:-0.8
# OSD progress bar vertical alignment
progbar-align=50
</pre>
<p> <i>EXAMPLE MENCODER CONFIGURATION FILE:</i> </p>
<pre>
# Make MEncoder output to a default filename.
o=encoded.avi
# The next 4 lines allow mencoder tv:// to start capturing immediately.
oac=pcm=yes
ovc=lavc=yes
lavcopts=vcodec=mjpeg
tv=driver=v4l2:input=1:width=768:height=576:device=/dev/video0:audiorate=48000
# more complex default encoding option set
lavcopts=vcodec=mpeg4:autoaspect=1
lameopts=aq=2:vbr=4
ovc=lavc=1
oac=lavc=1
passlogfile=pass1stats.log
noautoexpand=1
subfont-autoscale=3
subfont-osd-scale=6
subfont-text-scale=4
subalign=2
subpos=96
spuaa=20
</pre>
<p> <i>GUI CONFIGURATION FILE</i> </p>
<p> GUI&#8217;s own options are (MPlayer option names in parentheses): ao_alsa_device (<code>alsa:device=</code>) (ALSA only), ao_alsa_mixer (<code>mixer</code>) (ALSA only), ao_alsa_mixer_channel (<code>mixer-channel</code>) (ALSA only), ao_esd_device (<code>esd:</code>) (ESD only), ao_extra_stereo (<code>af extrastereo</code>) (default: 1.0), ao_extra_stereo_coefficient (<code>af extrastereo=</code>), ao_oss_device (<code>oss:</code>) (OSS only), ao_oss_mixer (<code>mixer</code>) (OSS only), ao_oss_mixer_channel (<code>mixer-channel</code>) (OSS only), ao_sdl_subdriver (<code>sdl:</code>) (SDL only), ao_surround (unused), ao_volnorm (<code>af volnorm</code>), autosync (enable/disable), autosync_size (<code>autosync</code>), cache (enable/disable), cache_size (<code>cache</code>), enable_audio_equ (<code>af equalizer</code>), equ_band_00 &#8230; equ_band_59, (<code>af equalizer=</code>), equ_channel_1 &#8230; equ_channel_6 (<code>af channels=</code>), gui_main_pos_x, gui_main_pos_y, gui_save_pos (yes/no), gui_tv_digital (yes/no), gui_video_out_pos_x, gui_video_out_pos_y, load_fullscreen (yes/no), playbar (enable/disable), replay_gain (enable/disable), replay_gain_adjustment (-30..10), show_videowin (yes/no), vf_lavc (<code>vf lavc</code>) (DXR3 only), vf_pp (<code>vf pp</code>), vo_dxr3_device (unused) (DXR3 only). </p>
<p> MPlayer options stored in gui.conf (GUI option names, MPlayer option names in parentheses) are: a_afm (<code>afm</code>), ao_driver (<code>ao</code>), ass_bottom_margin (<code>ass-bottom-margin</code>) (ASS only), ass_enabled (<code>ass</code>) (ASS only), ass_top_margin (<code>ass-top-margin</code>) (ASS only), ass_use_margins (<code>ass-use-margins</code>) (ASS only), cdrom_device (<code>cdrom-device</code>), dvd_device (<code>dvd-device</code>), font_autoscale (<code>subfont-autoscale</code>) (FreeType only), font_blur (<code>subfont-blur</code>) (FreeType only), font_encoding (<code>subfont-encoding</code>), font_factor (<code>ffactor</code>), font_name (<code>font</code>), font_osd_scale (<code>subfont-osd-scale</code>) (FreeType only), font_outline (<code>subfont-outline</code>) (FreeType only), font_text_scale (<code>subfont-text-scale</code>) (FreeType only), gui_skin (<code>skin</code>), idle (<code>idle</code>), osd_level (<code>osdlevel</code>), playlist_support (<code>allow-dangerous-playlist-parsing</code>), softvol (<code>softvol</code>), stopxscreensaver (<code>stop-xscreensaver</code>), sub_auto_load (<code>autosub</code>), sub_cp (<code>subcp</code>) (iconv only), sub_overlap (<code>overlapsub</code>), sub_pos (<code>subpos</code>), sub_unicode (<code>unicode</code>), sub_utf8 (<code>utf8</code>), v_flip (<code>flip</code>), v_framedrop (<code>framedrop</code>), v_idx (<code>idx</code>), v_ni (<code>ni</code>), v_vfm (<code>vfm</code>), vf_autoq (<code>autoq</code>), vo_direct_render (<code>panscan</code>), vo_doublebuffering (<code>dr</code>), vo_driver (<code>vo</code>), vo_panscan (<code>double</code>).</p>
<h2>PROFILES</h2>
<p> To ease working with different configurations profiles can be defined in the configuration files. A profile starts with its name between square brackets, e.g. &#8216;[my-profile]&#8217;. All following options will be part of the profile. A description (shown by -profile help) can be defined with the profile-desc option. To end the profile, start another one or use the profile name &#8216;default&#8217; to continue with normal options. </p>
<p> <i>EXAMPLE MPLAYER PROFILE:</i> </p>
<pre><code>
[protocol.dvd] profile - desc = "profile for dvd:// streams" vf = pp = hb / vb / dr / al / fd alang = en
                                                                                                          [protocol.dvdnav] profile -
                                                                                                      desc = "profile for dvdnav:// streams" profile = protocol.dvd
                                                                                                                                                           mouse -
                                                                                                                                                       movements = yes
                                                                                                                                                           nocache = yes
                                                                                                                                                                         [extension.flv] profile -
                                                                                                                                                                     desc = "profile for .flv files" flip = yes
                                                                                                                                                                         [vo.pnm] outdir = / tmp
                                                                                                                                                                                                 [ao.alsa] device = spdif
</code></pre>
<p> <i>EXAMPLE MENCODER PROFILE:</i> </p>
<p>[mpeg4] profile &#8211; desc = &#8220;MPEG4 encoding&#8221; ovc = lacv = yes<br />
    lavcopts = vcodec = mpeg4 : vbitrate = 1200<br />
                                               [mpeg4 &#8211; hq] profile &#8211;<br />
                                           desc = &#8220;HQ MPEG4 encoding&#8221; profile = mpeg4<br />
                                               lavcopts = mbd = 2 : trell = yes : v4mv = yes</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-codecpath &lt;dir&gt;</code></dt>
<dd> Specify a directory for binary codecs.</dd>
<dt><code>-codecs-file &lt;filename&gt; (also see -afm, -ac, -vfm, -vc)</code></dt>
<dd> Override the standard search path and use the specified file instead of the builtin codecs.conf.</dd>
<dt><code>-include &lt;configuration file&gt; (also see -gui-include)</code></dt>
<dd> Specify configuration file to be parsed after the default ones.</dd>
<dt><code>-list-options</code></dt>
<dd> Prints all available options.</dd>
<dt><code>-msgcharset &lt;charset&gt;</code></dt>
<dd> Convert console messages to the specified character set (default: autodetect). Text will be in the encoding specified with the &#8211;charset configure option. Set this to &quot;noconv&quot; to disable conversion (for e.g. iconv problems).<br />
 <i>NOTE:</i> The option takes effect after command line parsing has finished. The MPLAYER_CHARSET environment variable can help you get rid of the first lines of garbled output.</dd>
<dt><code>-msgcolor</code></dt>
<dd> Enable colorful console output on terminals that support ANSI color.</dd>
<dt><code>-msglevel &lt;all=&lt;level&gt;:&lt;module&gt;=&lt;level&gt;:&#8230;&gt;</code></dt>
<dd> Control verbosity directly for each module. The &#8216;all&#8217; module changes the verbosity of all the modules not explicitly specified on the command line. See &#8216;-msglevel help&#8217; for a list of all modules.<br />
 <i>NOTE:</i> Some messages are printed before the command line is parsed and are therefore not affected by -msglevel. To control these messages you have to use the MPLAYER_VERBOSE environment variable, see its description below for details.<br />
 Available levels:</dd>
<dl>
<dl>
<dt>-1</dt>
<dd> complete silence</dd>
<dt> 0</dt>
<dd> fatal messages only</dd>
<dt> 1</dt>
<dd> error messages</dd>
<dt> 2</dt>
<dd> warning messages</dd>
<dt> 3</dt>
<dd> short hints</dd>
<dt> 4</dt>
<dd> informational messages</dd>
<dt> 5</dt>
<dd> status messages (default)</dd>
<dt> 6</dt>
<dd> verbose messages</dd>
<dt> 7</dt>
<dd> debug level 2</dd>
<dt> 8</dt>
<dd> debug level 3</dd>
<dt> 9</dt>
<dd> debug level 4</dd></dl>
</dl>
<dt><code>-msgmodule</code></dt>
<dd> Prepend module name in front of each console message.</dd>
<dt><code>-noconfig &lt;options&gt;</code></dt>
<dd> Do not parse selected configuration files.<br />
 <i>NOTE:</i> If -include or -use-filedir-conf options are specified at the command line, they will be honoured. </dd>
<p> Available options are:</p>
<dl>
<dl>
<dt>all&nbsp;<wbr>&nbsp;</dt>
<dd> all configuration files</dd>
<dt>gui (GUI only)</dt>
<dd> GUI configuration file</dd>
<dt>system</dt>
<dd> system configuration file</dd>
<dt>user&nbsp;</dt>
<dd> user configuration file</dd></dl>
</dl>
<dt><code>-quiet&nbsp;</code></dt>
<dd> Make console output less verbose; in particular, prevents the status line (i.e. A: 0.7 V: 0.6 A-V: 0.068 &#8230;) from being displayed. Particularly useful on slow terminals or broken ones which do not properly handle carriage return (i.e. 
).</dd>
<dt><code>-priority &lt;prio&gt; (Windows and OS/2 only)</code></dt>
<dd> Set process priority for MPlayer according to the predefined priorities available under Windows and OS/2. Possible values of &lt;prio&gt;:</dd>
<dl>
<dt>
</dt><dd> idle|belownormal|normal|abovenormal|high|realtime</dd></dl>
<dl>
<dt>
</dt><dd> <i>WARNING:</i> Using realtime priority can cause system lockup.</dd></dl>
<dt><code>-profile &lt;profile1,profile2,&#8230;&gt;</code></dt>
<dd> Use the given profile(s), -profile help displays a list of the defined profiles.</dd>
<dt><code>-really-quiet (also see -quiet)</code></dt>
<dd> Display even less output and status messages than with -quiet. Also suppresses the GUI error message boxes.</dd>
<dt><code>-show-profile &lt;profile&gt;</code></dt>
<dd> Show the description and content of a profile.</dd>
<dt><code>-use-filedir-conf</code></dt>
<dd> Look for a file-specific configuration file in the same directory as the file that is being played.<br />
 <i>WARNING:</i> May be dangerous if playing from untrusted media.</dd>
<dt><code>-v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Increment verbosity level, one level for each -v found on the command line.</dd></dl>
<h2>PLAYER OPTIONS (MPLAYER ONLY)</h2>
<dl>
<dt><code>-autoq &lt;quality&gt; (use with -vf [s]pp)</code></dt>
<dd> Dynamically changes the level of postprocessing depending on the available spare CPU time. The number you specify will be the maximum level used. Usually you can use some big number. You have to use -vf [s]pp without parameters in order for this to work.</dd>
<dt><code>-autosync &lt;factor&gt;</code></dt>
<dd> Gradually adjusts the A/V sync based on audio delay measurements. Specifying -autosync 0, the default, will cause frame timing to be based entirely on audio delay measurements. Specifying -autosync 1 will do the same, but will subtly change the A/V correction algorithm. An uneven video framerate in a movie which plays fine with -nosound can often be helped by setting this to an integer value greater than 1. The higher the value, the closer the timing will be to -nosound. Try -autosync 30 to smooth out problems with sound drivers which do not implement a perfect audio delay measurement. With this value, if large A/V sync offsets occur, they will only take about 1 or 2 seconds to settle out. This delay in reaction time to sudden A/V offsets should be the only side-effect of turning this option on, for all sound drivers.</dd>
<dt><code>-benchmark</code></dt>
<dd> Prints some statistics on CPU usage and dropped frames at the end of playback. Use in combination with -nosound and -vo null for benchmarking only the video codec.<br />
 <i>NOTE:</i> With this option MPlayer will also ignore frame duration when playing only video (you can think of that as infinite fps).</dd>
<dt><code>-colorkey &lt;number&gt;</code></dt>
<dd> Changes the colorkey to an RGB value of your choice. 0x000000 is black and 0xffffff is white. Only supported by the cvidix, fbdev, svga, vesa, winvidix, xmga, xvidix, xover, xv (see -vo xv:ck), xvmc (see -vo xv:ck) and directx video output drivers.</dd>
<dt><code>-nocolorkey</code></dt>
<dd> Disables colorkeying. Only supported by the cvidix, fbdev, svga, vesa, winvidix, xmga, xvidix, xover, xv (see -vo xv:ck), xvmc (see -vo xv:ck) and directx video output drivers.</dd>
<dt><code>-correct-pts (EXPERIMENTAL)</code></dt>
<dd> Switches MPlayer to an experimental mode where timestamps for video frames are calculated differently and video filters which add new frames or modify timestamps of existing ones are supported. The more accurate timestamps can be visible for example when playing subtitles timed to scene changes with the -ass option. Without -correct-pts the subtitle timing will typically be off by some frames. This option does not work correctly with some demuxers and codecs.</dd>
<dt><code>-crash-debug (DEBUG CODE)</code></dt>
<dd> Automatically attaches gdb upon crash or SIGTRAP. Support must be compiled in by configuring with &#8211;enable-crash-debug.</dd>
<dt><code>-doubleclick-time</code></dt>
<dd> Time in milliseconds to recognize two consecutive button presses as a double-click (default: 300). Set to 0 to let your windowing system decide what a double-click is (-vo directx only).<br />
 <i>NOTE:</i> You will get slightly different behaviour depending on whether you bind MOUSE_BTN0_DBL or MOUSE_BTN0-MOUSE_BTN0_DBL.</dd>
<dt><code>-edlout &lt;filename&gt;</code></dt>
<dd> Creates a new file and writes edit decision list (EDL) records to it. During playback, the user hits &#8216;i&#8217; to mark the start or end of a skip block. This provides a starting point from which the user can fine-tune EDL entries later. See <a rel="nofollow" href="http://www.mplayerhq.hu/DOCS/HTML/en/edl.html">http://www.mplayerhq.hu/DOCS/HTML/en/edl.html</a> for details.</dd>
<dt><code>-edl-backward-delay &lt;number&gt;</code></dt>
<dd> When using EDL during playback and jumping backwards it is possible to end up in the middle of an EDL record. In that case MPlayer will seek further backwards to the start position of the EDL record and then immediately skip the scene specified in the EDL record. To avoid this kind of behavior, MPlayer jumps to a fixed time interval before the start of the EDL record. This parameter allows you to specify that time interval in seconds (default: 2 seconds).</dd>
<dt><code>-edl-start-pts</code></dt>
<dd> Adjust positions in EDL records according to playing file&#8217;s start time. Some formats, especially MPEG TS usually start with non-zero PTS values and when producing EDL file with -edlout option, EDL records contain absolute values that are correct only for this particular file. If re-encoded into a different format, this EDL file no longer applies. Specifying -edl-start-pts will automatically adjust EDL positions according to start time: when producing EDL file, it will substract start time from every EDL record, when playing with EDL file, it will add file&#8217;s start time to every EDL position.</dd>
<dt><code>-noedl-start-pts</code></dt>
<dd> Disable adjusting EDL positions.</dd>
<dt><code>-enqueue (GUI only)</code></dt>
<dd> Enqueue files given on the command line in the playlist instead of playing them immediately.</dd>
<dt><code>-fixed-vo</code></dt>
<dd> Enforces a fixed video system for multiple files (one (un)initialization for all files). Therefore only one window will be opened for all files. Currently the following drivers are fixed-vo compliant: gl, gl_tiled, mga, svga, x11, xmga, xv, xvidix and dfbmga.</dd>
<dt><code>-framedrop (also see -hardframedrop, experimental without -nocorrect-pts)</code></dt>
<dd> Skip displaying some frames to maintain A/V sync on slow systems. Video filters are not applied to such frames. For B-frames even decoding is skipped completely.</dd>
<dt><code>-(no)gui</code></dt>
<dd> Enable or disable the GUI interface (default depends on binary name). Only works as the first argument on the command line. Does not work as a config-file option.</dd>
<dt><code>-gui-include &lt;GUI configuration file&gt; (also see -include) (GUI only)</code></dt>
<dd> Specify a GUI configuration file to be parsed after the default gui.conf.</dd>
<dt><code>-h, -help, &#8211;help</code></dt>
<dd> Show short summary of options.</dd>
<dt><code>-hardframedrop (experimental without -nocorrect-pts)</code></dt>
<dd> More intense frame dropping (breaks decoding). Leads to image distortion! Note that especially the libmpeg2 decoder may crash with this, so consider using &quot;-vc ffmpeg12,&quot;.</dd>
<dt><code>-heartbeat-cmd</code></dt>
<dd> Command that is executed every 30 seconds during playback via system() &#8211; i.e. using the shell. </dd>
<p> <i>NOTE:</i> MPlayer uses this command without any checking, it is your responsibility to ensure it does not cause security problems (e.g. make sure to use full paths if &quot;.&quot; is in your path like on Windows). It also only works when playing video (i.e. not with -novideo but works with -vo null). </p>
<p> This can be &quot;misused&quot; to disable screensavers that do not support the proper X API (also see -stop-xscreensaver). If you think this is too complicated, ask the author of the screensaver program to support the proper X APIs. </p>
<p> <i>EXAMPLE for xscreensaver:</i> mplayer -heartbeat-cmd &quot;xscreensaver-command -deactivate&quot; file </p>
<p> <i>EXAMPLE for GNOME screensaver:</i> mplayer -heartbeat-cmd &quot;gnome-screensaver-command -p&quot; file</p>
<dt><code>-heartbeat-interval</code></dt>
<dd> Specify how often the -heartbeat-cmd should be executed, in seconds between executions (default: 30.0).</dd>
<dt><code>-identify</code></dt>
<dd> Shorthand for -msglevel identify=4. Show file parameters in an easily parseable format. Also prints more detailed information about subtitle and audio track languages and IDs. In some cases you can get more information by using -msglevel identify=6. For example, for a DVD or Blu-ray it will list the chapters and time length of each title, as well as a disk ID. Combine this with -frames 0 to suppress all video output. The wrapper script TOOLS/midentify.sh suppresses the other MPlayer output and (hopefully) shellescapes the filenames.</dd>
<dt><code>-idle (also see -slave)</code></dt>
<dd> Makes MPlayer wait idly instead of quitting when there is no file to play. Mostly useful in slave mode where MPlayer can be controlled through input commands.<br />
 For <code>gmplayer</code> -idle is the default, -noidle will quit the GUI after all files have been played.</dd>
<dt><code>-input &lt;commands&gt;</code></dt>
<dd> This option can be used to configure certain parts of the input system. Paths are relative to ~/.mplayer/.<br />
 <i>NOTE:</i> Autorepeat is currently only supported by joysticks. </dd>
<p> Available commands are: </p>
<dl>
<dl>
<dt>conf=&lt;filename&gt;</dt>
<dd> Specify input configuration file other than the default ~/.mplayer/input.conf. ~/.mplayer/&lt;filename&gt; is assumed if no full path is given.</dd>
<dt>ar-dev=&lt;device&gt;</dt>
<dd> Device to be used for Apple IR Remote (default is autodetected, Linux only).</dd>
<dt>ar-delay</dt>
<dd> Delay in milliseconds before we start to autorepeat a key (0 to disable).</dd>
<dt>ar-rate</dt>
<dd> Number of key presses to generate per second on autorepeat.</dd>
<dt>(no)default-bindings</dt>
<dd> Use the key bindings that MPlayer ships with by default.</dd>
<dt>keylist</dt>
<dd> Prints all keys that can be bound to commands.</dd>
<dt>cmdlist</dt>
<dd> Prints all commands that can be bound to keys.</dd>
<dt>js-dev</dt>
<dd> Specifies the joystick device to use (default: /dev/input/js0).</dd>
<dt>file=&lt;filename&gt;</dt>
<dd> Read commands from the given file. Mostly useful with a FIFO.<br />
 <i>NOTE:</i> When the given file is a FIFO MPlayer opens both ends so you can do several &#8216;echo &quot;seek 10&quot; &gt; mp_pipe&#8217; and the pipe will stay valid.</dd></dl>
</dl>
<dt><code>-key-fifo-size &lt;2-65000&gt;</code></dt>
<dd> Specify the size of the FIFO that buffers key events (default: 7). A FIFO of size n can buffer (n-1) events. If it is too small some events may be lost. If it is too big, MPlayer may seem to hang while it processes the buffered events. To get the same behavior as before this option was introduced, set it to 2 for Linux or 1024 for Windows. For small value you should disable double-clicks by setting -doubleclick-time to 0 so they do not compete with regular events for buffer space.</dd>
<dt><code>-lircconf &lt;filename&gt; (LIRC only)</code></dt>
<dd> Specifies a configuration file for LIRC (default: ~/.lircrc).</dd>
<dt><code>-list-properties</code></dt>
<dd> Print a list of the available properties.</dd>
<dt><code>-loop &lt;number&gt;</code></dt>
<dd> Loops movie playback &lt;number&gt; times. 0 means forever. Use -loop 0 to automatically reconnect to live streaming URLs.</dd>
<dt><code>-menu (OSD menu only)</code></dt>
<dd> Turn on OSD menu support.</dd>
<dt><code>-menu-cfg &lt;filename&gt; (OSD menu only)</code></dt>
<dd> Use an alternative menu.conf.</dd>
<dt><code>-menu-chroot &lt;path&gt; (OSD menu only)</code></dt>
<dd> Chroot the file selection menu to a specific location. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-menu-chroot /home</dt>
<dd> Will restrict the file selection menu to /home and downward (i.e. no access to / will be possible, but /home/user_name will).</dd></dl>
</dl>
<dt><code>-menu-keepdir (OSD menu only)</code></dt>
<dd> File browser starts from the last known location instead of current directory.</dd>
<dt><code>-menu-root &lt;value&gt; (OSD menu only)</code></dt>
<dd> Specify the main menu.</dd>
<dt><code>-menu-startup (OSD menu only)</code></dt>
<dd> Display the main menu at MPlayer startup.</dd>
<dt><code>-mouse-movements</code></dt>
<dd> Permit MPlayer to receive pointer events reported by the video output driver. Necessary to select the buttons in DVD menus. Supported for X11-based VOs (x11, xv, xvmc, etc) and the gl, gl_tiled, direct3d and corevideo VOs.</dd>
<dt><code>-noar</code></dt>
<dd> Turns off AppleIR remote support.</dd>
<dt><code>-noconsolecontrols</code></dt>
<dd> Prevent MPlayer from reading key events from standard input. Useful when reading data from standard input. This is automatically enabled when &#8211; is found on the command line. There are situations where you have to set it manually, e.g. if you open /dev/stdin (or the equivalent on your system), use stdin in a playlist or intend to read from stdin later on via the loadfile or loadlist slave commands.</dd>
<dt><code>-nojoystick</code></dt>
<dd> Turns off joystick support.</dd>
<dt><code>-nolirc</code></dt>
<dd> Turns off LIRC support.</dd>
<dt><code>-nomouseinput</code></dt>
<dd> Disable mouse button press/release input (mozplayerxp&#8217;s context menu relies on this option).</dd>
<dt><code>-rtc (RTC only)</code></dt>
<dd> Turns on usage of the Linux RTC (realtime clock &#8211; /dev/rtc) as timing mechanism. This wakes up the process every 1/1024 seconds to check the current time. Useless with modern Linux kernels configured for desktop use as they already wake up the process with similar accuracy when using normal timed sleep.</dd>
<dt><code>-pausing &lt;0-3&gt; (MPlayer only)</code></dt>
<dd> Specifies the default pausing behaviour of commands, i.e. whether MPlayer will continue playback or stay paused after the command has finished. See DOCS/tech/slave.txt for further details.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> resume</dd>
<dt>1</dt>
<dd> pause (pausing)</dd>
<dt>2</dt>
<dd> keep the paused / playing status (pausing_keep)</dd>
<dt>3</dt>
<dd> toggle the paused / playing status (pausing_toggle)</dd>
<dt>4</dt>
<dd> pause without frame step (experimental) (pausing_keep_force)</dd></dl>
</dl>
<dt><code>-playing-msg &lt;string&gt;</code></dt>
<dd> Print out a string before starting playback. The following expansions are supported:</dd>
<dl>
<dl>
<dt>${NAME}</dt>
<dd> Expand to the value of the property NAME.</dd>
<dt>?(NAME:TEXT)</dt>
<dd> Expand TEXT only if the property NAME is available.</dd>
<dt>?(!NAME:TEXT)</dt>
<dd> Expand TEXT only if the property NAME is not available.</dd></dl>
</dl>
<dt><code>-playlist &lt;filename&gt;</code></dt>
<dd> Play files according to a playlist file (ASX, Winamp, SMIL, or one-file-per-line format).<br />
 <i>WARNING:</i> The way MPlayer parses and uses playlist files is not safe against maliciously constructed files. Such files may trigger harmful actions. This has been the case for all MPlayer versions, but unfortunately this fact was not well documented earlier, and some people have even misguidedly recommended use of -playlist with untrusted sources. Do NOT use -playlist with random internet sources or files you don&#8217;t trust!<br />
 <i>NOTE:</i> This option is considered an entry so options found after it will apply only to the elements of this playlist.<br />
 FIXME: This needs to be clarified and documented thoroughly.</dd>
<dt><code>-allow-dangerous-playlist-parsing</code></dt>
<dd> This enables parsing any file as a playlist if e.g. a server advertises a file as playlist. Only enable if you know all servers involved are trustworthy. MPlayer&#8217;s playlist code is not designed to handle malicious playlist files.</dd>
<dt><code>-rtc-device &lt;device&gt;</code></dt>
<dd> Use the specified device for RTC timing.</dd>
<dt><code>-shuffle</code></dt>
<dd> Play files in random order.</dd>
<dt><code>-skin &lt;name&gt; (GUI only)</code></dt>
<dd> Loads a skin from the directory given as parameter below the default skin directories, ~/.mplayer/skins/ and /usr/local/share/mplayer/skins/. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-skin fittyfene</dt>
<dd> Tries ~/.mplayer/skins/fittyfene and afterwards /usr/local/share/mplayer/skins/fittyfene.</dd></dl>
</dl>
<dt><code>-slave (also see -input)</code></dt>
<dd> Switches on slave mode, in which MPlayer works as a backend for other programs. Instead of intercepting keyboard events, MPlayer will read commands separated by a newline (
) from stdin.<br />
 <i>NOTE:</i> See -input cmdlist for a list of slave commands and DOCS/tech/slave.txt for their description. Also, this is not intended to disable other inputs, e.g. via the video window, use some other method like -input nodefault-bindings:conf=/dev/null for that.</dd>
<dt><code>-softsleep</code></dt>
<dd> Time frames by repeatedly checking the current time instead of asking the kernel to wake up MPlayer at the correct time. Useful if your kernel timing is imprecise and you cannot use the RTC either. Comes at the price of higher CPU consumption.</dd>
<dt><code>-sstep &lt;sec&gt;</code></dt>
<dd> Skip &lt;sec&gt; seconds after every frame. The normal framerate of the movie is kept, so playback is accelerated. Since MPlayer can only seek to the next keyframe this may be inexact.</dd>
<dt><code>-udp-ip &lt;ip&gt;</code></dt>
<dd> Sets the destination address for datagrams sent by the -udp-master. Setting it to a broadcast address allows multiple slaves having the same broadcast address to sync to the master (default: 127.0.0.1).</dd>
<dt><code>-udp-master</code></dt>
<dd> Send a datagram to -udp-ip on -udp-port just before playing each frame. The datagram indicates the master&#8217;s position in the file.</dd>
<dt><code>-udp-port &lt;port&gt;</code></dt>
<dd> Sets the destination port for datagrams sent by the -udp-master, and the port a -udp-slave listens on (default: 23867).</dd>
<dt><code>-udp-seek-threshold &lt;sec&gt;</code></dt>
<dd> When the master seeks, the slave has to decide whether to seek as well, or to catch up by decoding frames without pausing between frames. If the master is more than &lt;sec&gt; seconds away from the slave, the slave seeks. Otherwise, it &quot;runs&quot; to catch up or waits for the master. This should almost always be left at its default setting of 1 second.</dd>
<dt><code>-udp-slave</code></dt>
<dd> Listen on -udp-port and match the master&#8217;s position.</dd></dl>
<h2>DEMUXER/STREAM OPTIONS</h2>
<dl>
<dt><code>-a52drc &lt;level&gt;</code></dt>
<dd> Select the Dynamic Range Compression level for AC-3 audio streams. &lt;level&gt; is a float value ranging from 0 to 1, where 0 means no compression and 1 (which is the default) means full compression (make loud passages more silent and vice versa). Values up to 2 are also accepted, but are purely experimental. This option only shows an effect if the AC-3 stream contains the required range compression information.</dd>
<dt><code>-aid &lt;ID&gt; (also see -alang)</code></dt>
<dd> Select audio channel (MPEG: 0-31, AVI/OGM: 1-99, ASF/RM: 0-127, VOB(AC-3): 128-159, VOB(LPCM): 160-191, MPEG-TS 17-8190). MPlayer prints the available audio IDs when run in verbose (-v) mode. When playing an MPEG-TS stream, MPlayer/MEncoder will use the first program (if present) with the chosen audio stream.</dd>
<dt><code>-ausid &lt;ID&gt; (also see -alang)</code></dt>
<dd> Select audio substream channel. Currently the valid range is 0x55..0x75 and applies only to MPEG-TS when handled by the native demuxer (not by libavformat). The format type may not be correctly identified because of how this information (or lack thereof) is embedded in the stream, but it will demux correctly the audio streams when multiple substreams are present. MPlayer prints the available substream IDs when run with -identify.</dd>
<dt><code>-alang &lt;language code[,language code,&#8230;]&gt; (also see -aid)</code></dt>
<dd> Specify a priority list of audio languages to use. Different container formats employ different language codes. DVDs use ISO 639-1 two letter language codes, Matroska, MPEG-TS and NUT use ISO 639-2 three letter language codes while OGM uses a free-form identifier. MPlayer prints the available languages when run in verbose (-v) mode. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>mplayer <a href="dvd://1">dvd://1</a> -alang hu,en</dt>
<dd> Chooses the Hungarian language track on a DVD and falls back on English if Hungarian is not available.</dd>
<dt>mplayer -alang jpn example.mkv</dt>
<dd> Plays a Matroska file in Japanese.</dd></dl>
</dl>
<dt><code>-audio-demuxer &lt;[+]name&gt; (-audiofile only)</code></dt>
<dd> Force audio demuxer type for -audiofile. Use a &#8216;+&#8217; before the name to force it, this will skip some checks! Give the demuxer name as printed by -audio-demuxer help. For backward compatibility it also accepts the demuxer ID as defined in libmpdemux/demuxer.h. -audio-demuxer audio or -audio-demuxer 17 forces MP3.</dd>
<dt><code>-audiofile &lt;filename&gt;</code></dt>
<dd> Play audio from an external file (WAV, MP3 or Ogg Vorbis) while viewing a movie.</dd>
<dt><code>-audiofile-cache &lt;kBytes&gt;</code></dt>
<dd> Enables caching for the stream used by -audiofile, using the specified amount of memory.</dd>
<dt><code>-reuse-socket (udp:// only)</code></dt>
<dd> Allows a socket to be reused by other processes as soon as it is closed.</dd>
<dt><code>-bandwidth &lt;Bytes&gt; (network only)</code></dt>
<dd> Specify the maximum bandwidth for network streaming (for servers that are able to send content in different bitrates). Useful if you want to watch live streamed media behind a slow connection. With Real RTSP streaming, it is also used to set the maximum delivery bandwidth allowing faster cache filling and stream dumping.</dd>
<dt><code>-bluray-angle &lt;angle ID&gt; (Blu-ray only)</code></dt>
<dd> Some Blu-ray discs contain scenes that can be viewed from multiple angles. Here you can tell MPlayer which angles to use (default: 1).</dd>
<dt><code>-bluray-device &lt;path to disc&gt; (Blu-ray only)</code></dt>
<dd> Specify the Blu-ray disc location. Must be a directory with Blu-ray structure.</dd>
<dt><code>-cache &lt;kBytes&gt;</code></dt>
<dd> This option specifies how much memory (in kBytes) to use when precaching a file or URL. Especially useful on slow media.</dd>
<dt><code>-nocache</code></dt>
<dd> Turns off caching.</dd>
<dt><code>-cache-min &lt;percentage&gt;</code></dt>
<dd> Playback will start when the cache has been filled up to &lt;percentage&gt; of the total.</dd>
<dt><code>-cache-seek-min &lt;percentage&gt;</code></dt>
<dd> If a seek is to be made to a position within &lt;percentage&gt; of the cache size from the current position, MPlayer will wait for the cache to be filled to this position rather than performing a stream seek (default: 50).</dd>
<dt><code>-capture (MPlayer only)</code></dt>
<dd> Allows capturing the primary stream (not additional audio tracks or other kind of streams) into the file specified by -dumpfile or by default. If this option is given, capturing can be started and stopped by pressing the key bound to this function (see section INTERACTIVE CONTROL). Same as for -dumpstream, this will likely not produce usable results for anything else than MPEG streams. Note that, due to cache latencies, captured data may begin and end somewhat delayed compared to what you see displayed.</dd>
<dt><code>-cdda &lt;option1:option2&gt; (CDDA only)</code></dt>
<dd> This option can be used to tune the CD Audio reading feature of MPlayer. </dd>
<p> Available options are:</p>
<dl>
<dl>
<dt>speed=&lt;value&gt;</dt>
<dd> Set CD spin speed.</dd>
<dt>paranoia=&lt;0-2&gt;</dt>
<dd> Set paranoia level. Values other than 0 seem to break playback of anything but the first track.</dd>
<dl>
<dt>
</dt><dd> 0: disable checking (default)<br />
 1: overlap checking only<br />
 2: full data correction and verification</dd></dl>
<dt>generic-dev=&lt;value&gt;</dt>
<dd> Use specified generic SCSI device.</dd>
<dt>sector-size=&lt;value&gt;</dt>
<dd> Set atomic read size.</dd>
<dt>overlap=&lt;value&gt;</dt>
<dd> Force minimum overlap search during verification to &lt;value&gt; sectors.</dd>
<dt>toc-bias</dt>
<dd> Assume that the beginning offset of track 1 as reported in the TOC will be addressed as LBA 0. Some Toshiba drives need this for getting track boundaries correct.</dd>
<dt>toc-offset=&lt;value&gt;</dt>
<dd> Add &lt;value&gt; sectors to the values reported when addressing tracks. May be negative.</dd>
<dt>(no)skip</dt>
<dd> (Never) accept imperfect data reconstruction.</dd></dl>
</dl>
<dt><code>-cdrom-device &lt;path to device&gt;</code></dt>
<dd> Specify the CD-ROM device (default: /dev/cdrom).</dd>
<dt><code>-channels &lt;number&gt; (also see -af channels)</code></dt>
<dd> Request the number of playback channels (default: 2). MPlayer asks the decoder to decode the audio into as many channels as specified. Then it is up to the decoder to fulfill the requirement. This is usually only important when playing videos with AC-3 audio (like DVDs). In that case liba52 does the decoding by default and correctly downmixes the audio into the requested number of channels. To directly control the number of output channels independently of how many channels are decoded, use the channels filter.<br />
 <i>NOTE:</i> This option is honored by codecs (AC-3 only), filters (surround) and audio output drivers (OSS at least). </dd>
<p> Available options are: </p>
<dl>
<dl>
<dt>2</dt>
<dd> stereo</dd>
<dt>4</dt>
<dd> surround</dd>
<dt>6</dt>
<dd> full 5.1</dd>
<dt>8</dt>
<dd> full 7.1</dd></dl>
</dl>
<dt><code>-chapter &lt;chapter ID&gt;[-&lt;endchapter ID&gt;]</code></dt>
<dd> Specify which chapter to start playing at. Optionally specify which chapter to end playing at (default: 1).</dd>
<dt><code>-cookies (network only)</code></dt>
<dd> Send cookies when making HTTP requests.</dd>
<dt><code>-cookies-file &lt;filename&gt; (network only)</code></dt>
<dd> Read HTTP cookies from &lt;filename&gt; (default: ~/.mozilla/ and ~/.netscape/) and skip reading from default locations. The file is assumed to be in Netscape format.</dd>
<dt><code>-delay &lt;sec&gt;</code></dt>
<dd> audio delay in seconds (positive or negative float value)<br />
 Negative values delay the audio, and positive values delay the video. Note that this is the exact opposite of the -audio-delay MEncoder option.<br />
 <i>NOTE:</i> When used with MEncoder, this is not guaranteed to work correctly with -ovc copy; use -audio-delay instead.</dd>
<dt><code>-ignore-start</code></dt>
<dd> Ignore the specified starting time for streams in AVI files. In MPlayer, this nullifies stream delays in files encoded with the -audio-delay option. During encoding, this option prevents MEncoder from transferring original stream start times to the new file; the -audio-delay option is not affected. Note that MEncoder sometimes adjusts stream starting times automatically to compensate for anticipated decoding delays, so do not use this option for encoding without testing it first.</dd>
<dt><code>-demuxer &lt;[+]name&gt;</code></dt>
<dd> Force demuxer type. Use a &#8216;+&#8217; before the name to force it, this will skip some checks! Give the demuxer name as printed by -demuxer help. For backward compatibility it also accepts the demuxer ID as defined in libmpdemux/demuxer.h.</dd>
<dt><code>-dumpaudio (MPlayer only)</code></dt>
<dd> Dumps raw compressed audio stream to ./stream.dump (useful with MPEG/AC-3, in most other cases the resulting file will not be playable). If you give more than one of -dumpaudio, -dumpvideo, -dumpstream on the command line only the last one will work.</dd>
<dt><code>-dumpfile &lt;filename&gt; (MPlayer only)</code></dt>
<dd> Specify which file MPlayer should dump to. Should be used together with -dumpaudio / -dumpvideo / -dumpstream / -capture.</dd>
<dt><code>-dumpstream (MPlayer only)</code></dt>
<dd> Dumps the raw stream to ./stream.dump. Useful when ripping from DVD or network. If you give more than one of -dumpaudio, -dumpvideo, -dumpstream on the command line only the last one will work.</dd>
<dt><code>-dumpvideo (MPlayer only)</code></dt>
<dd> Dump raw compressed video stream to ./stream.dump (not very usable). If you give more than one of -dumpaudio, -dumpvideo, -dumpstream on the command line only the last one will work.</dd>
<dt><code>-dvbin &lt;options&gt; (DVB only)</code></dt>
<dd> Pass the following parameters to the DVB input module, in order to override the default ones: </dd>
<dl>
<dl>
<dt>card=&lt;1-4&gt;</dt>
<dd> Specifies using card number 1-4 (default: 1).</dd>
<dt>file=&lt;filename&gt;</dt>
<dd> Instructs MPlayer to read the channels list from &lt;filename&gt;. Default is ~/.mplayer/channels.conf.{sat,ter,cbl,atsc} (based on your card type) or ~/.mplayer/channels.conf as a last resort.</dd>
<dt>timeout=&lt;1-240&gt;</dt>
<dd> Maximum number of seconds to wait when trying to tune a frequency before giving up (default: 30).</dd></dl>
</dl>
<dt><code>-dvd-device &lt;path to device&gt; (DVD only)</code></dt>
<dd> Specify the DVD device or .iso filename (default: /dev/dvd). You can also specify a directory that contains files previously copied directly from a DVD (with e.g. vobcopy).</dd>
<dt><code>-dvd-speed &lt;factor or speed in KB/s&gt; (DVD only)</code></dt>
<dd> Try to limit DVD speed (default: 0, no change). DVD base speed is about 1350KB/s, so a 8x drive can read at speeds up to 10800KB/s. Slower speeds make the drive more quiet, for watching DVDs 2700KB/s should be quiet and fast enough. MPlayer resets the speed to the drive default value on close. Values less than 100 mean multiples of 1350KB/s, i.e. -dvd-speed 8 selects 10800KB/s.<br />
 <i>NOTE:</i> You need write access to the DVD device to change the speed.</dd>
<dt><code>-dvdangle &lt;angle ID&gt; (DVD only)</code></dt>
<dd> Some DVD discs contain scenes that can be viewed from multiple angles. Here you can tell MPlayer which angles to use (default: 1).</dd>
<dt><code>-edl &lt;filename&gt;</code></dt>
<dd> Enables edit decision list (EDL) actions during playback. Video will be skipped over and audio will be muted and unmuted according to the entries in the given file. See <a rel="nofollow" href="http://www.mplayerhq.hu/DOCS/HTML/en/edl.html">http://www.mplayerhq.hu/DOCS/HTML/en/edl.html</a> for details on how to use this.</dd>
<dt><code>-endpos &lt;[[hh:]mm:]ss[.ms]|size[b|kb|mb]&gt; (also see -ss and -sb)</code></dt>
<dd> Stop at given time or byte position.<br />
 <i>NOTE:</i> Byte position may not be accurate, as it can only stop at a frame boundary. When used in conjunction with -ss option, -endpos time will shift forward by seconds specified with -ss if not a byte position. In addition it may not work well or not at all when used with any of the -dump options. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-endpos 56</dt>
<dd> Stop at 56 seconds.</dd>
<dt>-endpos 01:10:00</dt>
<dd> Stop at 1 hour 10 minutes.</dd>
<dt>-ss 10 -endpos 56</dt>
<dd> Stop at 1 minute 6 seconds.</dd>
<dt>mplayer -endpos 100mb</dt>
<dd> Stop playback after reading 100MB of the input file.</dd>
<dt>mencoder -endpos 100mb</dt>
<dd> Encode only 100 MB.</dd></dl>
</dl>
<dt><code>-forceidx</code></dt>
<dd> Force index rebuilding. Useful for files with broken index (A/V desync, etc). This will enable seeking in files where seeking was not possible. You can fix the index permanently with MEncoder (see the documentation).<br />
 <i>NOTE:</i> This option only works if the underlying media supports seeking (i.e. not with stdin, pipe, etc).</dd>
<dt><code>-fps &lt;float value&gt;</code></dt>
<dd> Override video framerate. Useful if the original value is wrong or missing.</dd>
<dt><code>-frames &lt;number&gt;</code></dt>
<dd> Play/convert only first &lt;number&gt; frames, then quit.</dd>
<dt><code>-hr-mp3-seek (MP3 only)</code></dt>
<dd> Hi-res MP3 seeking. Enabled when playing from an external MP3 file, as we need to seek to the very exact position to keep A/V sync. Can be slow especially when seeking backwards since it has to rewind to the beginning to find an exact frame position.</dd>
<dt><code>-http-header-fields &lt;field1,field2&gt;</code></dt>
<dd> Set custom HTTP fields when accessing HTTP stream. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>
</dt><dd> mplayer -http-header-fields &#8216;Field1: value1&#8242;,&#8217;Field2: value2&#8217; <a rel="nofollow" href="http://localhost:1234">http://localhost:1234</a><br />
 Will generate HTTP request:</dd>
<dl>
<dt>
</dt><dd>
 GET / HTTP/1.0<br />
 Host: localhost:1234<br />
 User-Agent: MPlayer<br />
 Icy-MetaData: 1<br />
 Field1: value1<br />
 Field2: value2<br />
 Connection: close</dd></dl>
</dl>
</dl>
<dt><code>-idx (also see -forceidx)</code></dt>
<dd> Rebuilds index of files if no index was found, allowing seeking. Useful with broken/incomplete downloads, or badly created files.<br />
 <i>NOTE:</i> This option only works if the underlying media supports seeking (i.e. not with stdin, pipe, etc).</dd>
<dt><code>-noidx</code></dt>
<dd> Skip rebuilding index file. MEncoder skips writing the index with this option.</dd>
<dt><code>-ipv4-only-proxy (network only)</code></dt>
<dd> Skip the proxy for IPv6 addresses. It will still be used for IPv4 connections.</dd>
<dt><code>-loadidx &lt;index file&gt;</code></dt>
<dd> The file from which to read the video index data saved by -saveidx. This index will be used for seeking, overriding any index data contained in the AVI itself. MPlayer will not prevent you from loading an index file generated from a different AVI, but this is sure to cause unfavorable results.<br />
 <i>NOTE:</i> This option is obsolete now that MPlayer has OpenDML support.</dd>
<dt><code>-mc &lt;seconds/frame&gt;</code></dt>
<dd> maximum A-V sync correction per frame (in seconds)<br />
 -mc 0 should always be combined with -noskip for mencoder, otherwise it will almost certainly cause A-V desync.</dd>
<dt><code>-mf &lt;option1:option2:&#8230;&gt;</code></dt>
<dd> Used when decoding from multiple PNG or JPEG files. </dd>
<p> Available options are: </p>
<dl>
<dl>
<dt>w=&lt;value&gt;</dt>
<dd> input file width (default: autodetect)</dd>
<dt>h=&lt;value&gt;</dt>
<dd> input file height (default: autodetect)</dd>
<dt>fps=&lt;value&gt;</dt>
<dd> output fps (default: 25)</dd>
<dt>type=&lt;value&gt;</dt>
<dd> input file type (available: jpeg, png, tga, sgi)</dd></dl>
</dl>
<dt><code>-ni</code></dt>
<dd> Force treating files as non-interleaved. In particular forces usage of non-interleaved AVI parser (fixes playback of some bad AVI files). Can also help playing files that otherwise play audio and video alternating instead of at the same time. This can significantly increase memory usage, thus it would be preferable to fix interleaving of affected files.</dd>
<dt><code>-nobps (AVI only)</code></dt>
<dd> Do not use average byte/second value for A-V sync. Helps with some AVI files with broken header.</dd>
<dt><code>-noextbased</code></dt>
<dd> Disables extension-based demuxer selection. By default, when the file type (demuxer) cannot be detected reliably (the file has no header or it is not reliable enough), the filename extension is used to select the demuxer. Always falls back on content-based demuxer selection.</dd>
<dt><code>-passwd &lt;password&gt; (also see -user) (network only)</code></dt>
<dd> Specify password for HTTP authentication.</dd>
<dt><code>-prefer-ipv4 (network only)</code></dt>
<dd> Use IPv4 on network connections. Falls back on IPv6 automatically.</dd>
<dt><code>-prefer-ipv6 (IPv6 network only)</code></dt>
<dd> Use IPv6 on network connections. Falls back on IPv4 automatically.</dd>
<dt><code>-psprobe &lt;byte position&gt;</code></dt>
<dd> When playing an MPEG-PS or MPEG-PES streams, this option lets you specify how many bytes in the stream you want MPlayer to scan in order to identify the video codec used. This option is needed to play EVO or VDR files containing H.264 streams.</dd>
<dt><code>-pvr &lt;option1:option2:&#8230;&gt; (PVR only)</code></dt>
<dd> This option tunes various encoding properties of the PVR capture module. It has to be used with any hardware MPEG encoder based card supported by the V4L2 driver. The Hauppauge WinTV PVR-150/250/350/500 and all IVTV based cards are known as PVR capture cards. Be aware that only Linux 2.6.18 kernel and above is able to handle MPEG stream through V4L2 layer. For hardware capture of an MPEG stream and watching it with MPlayer/MEncoder, use &#8216;<a href="pvr://'">pvr://&#8217;</a> as a movie URL. </dd>
<p> Available options are:</p>
<dl>
<dl>
<dt>aspect=&lt;0-3&gt;</dt>
<dd> Specify input aspect ratio:</dd>
<dl>
<dt>
</dt><dd> 0: 1:1<br />
 1: 4:3 (default)<br />
 2: 16:9<br />
 3: 2.21:1</dd></dl>
<dt>arate=&lt;32000-48000&gt;</dt>
<dd> Specify encoding audio rate (default: 48000 Hz, available: 32000, 44100 and 48000 Hz).</dd>
<dt>alayer=&lt;1-5&gt;</dt>
<dd> Specify MPEG audio layer encoding (default: 2).</dd>
<dt>abitrate=&lt;32-448&gt;</dt>
<dd> Specify audio encoding bitrate in kbps (default: 384).</dd>
<dt>amode=&lt;value&gt;</dt>
<dd> Specify audio encoding mode. Available preset values are &#8216;stereo&#8217;, &#8216;joint_stereo&#8217;, &#8216;dual&#8217; and &#8216;mono&#8217; (default: stereo).</dd>
<dt>vbitrate=&lt;value&gt;</dt>
<dd> Specify average video bitrate encoding in Mbps (default: 6).</dd>
<dt>vmode=&lt;value&gt;</dt>
<dd> Specify video encoding mode:</dd>
<dl>
<dt>
</dt><dd> vbr: Variable BitRate (default)<br />
 cbr: Constant BitRate</dd></dl>
<dt>vpeak=&lt;value&gt;</dt>
<dd> Specify peak video bitrate encoding in Mbps (only useful for VBR encoding, default: 9.6).</dd>
<dt>fmt=&lt;value&gt;</dt>
<dd> Choose an MPEG format for encoding:</dd>
<dl>
<dt>
</dt><dd> ps: MPEG-2 Program Stream (default)<br />
 ts: MPEG-2 Transport Stream<br />
 mpeg1: MPEG-1 System Stream<br />
 vcd: Video CD compatible stream<br />
 svcd: Super Video CD compatible stream<br />
 dvd: DVD compatible stream</dd></dl>
</dl>
</dl>
<dt><code>-radio &lt;option1:option2:&#8230;&gt; (radio only)</code></dt>
<dd> These options set various parameters of the radio capture module. For listening to radio with MPlayer use &#8216;radio://&lt;frequency&gt;&#8217; (if channels option is not given) or &#8216;radio://&lt;channel_number&gt;&#8217; (if channels option is given) as a movie URL. You can see allowed frequency range by running MPlayer with &#8216;-v&#8217;. To start the grabbing subsystem, use &#8216;radio://&lt;frequency or channel&gt;/capture&#8217;. If the capture keyword is not given you can listen to radio using the line-in cable only. Using capture to listen is not recommended due to synchronization problems, which makes this process uncomfortable. </dd>
<p> Available options are:</p>
<dl>
<dl>
<dt>device=&lt;value&gt;</dt>
<dd> Radio device to use (default: /dev/radio0 for Linux and /dev/tuner0 for *BSD).</dd>
<dt>driver=&lt;value&gt;</dt>
<dd> Radio driver to use (default: v4l2 if available, otherwise v4l). Currently, v4l and v4l2 drivers are supported.</dd>
<dt>volume=&lt;0..100&gt;</dt>
<dd> sound volume for radio device (default 100)</dd>
<dt>freq_min=&lt;value&gt; (*BSD BT848 only)</dt>
<dd> minimum allowed frequency (default: 87.50)</dd>
<dt>freq_max=&lt;value&gt; (*BSD BT848 only)</dt>
<dd> maximum allowed frequency (default: 108.00)</dd>
<dt>channels=&lt;frequency&gt;-&lt;name&gt;,&lt;frequency&gt;-&lt;name&gt;,&#8230;</dt>
<dd> Set channel list. Use _ for spaces in names (or play with quoting ;-). The channel names will then be written using OSD and the slave commands radio_step_channel and radio_set_channel will be usable for a remote control (see LIRC). If given, number in movie URL will be treated as channel position in channel list.<br />
 <i>EXAMPLE:</i> <a href="radio://1,">radio://1,</a> <a href="radio://104.4,">radio://104.4,</a> radio_set_channel 1</dd>
<dt>adevice=&lt;value&gt; (radio capture only)</dt>
<dd> Name of device to capture sound from. Without such a name capture will be disabled, even if the capture keyword appears in the URL. For ALSA devices use it in the form hw=&lt;card&gt;.&lt;device&gt;. If the device name contains a &#8216;=&#8217;, the module will use ALSA to capture, otherwise OSS.</dd>
<dt>arate=&lt;value&gt; (radio capture only)</dt>
<dd> Rate in samples per second (default: 44100).<br />
 <i>NOTE:</i> When using audio capture set also -rawaudio rate=&lt;value&gt; option with the same value as arate. If you have problems with sound speed (runs too quickly), try to play with different rate values (e.g. 48000,44100,32000,&#8230;).</dd>
<dt>achannels=&lt;value&gt; (radio capture only)</dt>
<dd> Number of audio channels to capture.</dd></dl>
</dl>
<dt><code>-rawaudio &lt;option1:option2:&#8230;&gt;</code></dt>
<dd> This option lets you play raw audio files. You have to use -demuxer rawaudio as well. It may also be used to play audio CDs which are not 44kHz 16-bit stereo. For playing raw AC-3 streams use -rawaudio format=0x2000 -demuxer rawaudio. </dd>
<p> Available options are: </p>
<dl>
<dl>
<dt>channels=&lt;value&gt;</dt>
<dd> number of channels</dd>
<dt>rate=&lt;value&gt;</dt>
<dd> rate in samples per second</dd>
<dt>samplesize=&lt;value&gt;</dt>
<dd> sample size in bytes</dd>
<dt>bitrate=&lt;value&gt;</dt>
<dd> bitrate for rawaudio files</dd>
<dt>format=&lt;value&gt;</dt>
<dd> fourcc in hex</dd></dl>
</dl>
<dt><code>-rawvideo &lt;option1:option2:&#8230;&gt;</code></dt>
<dd> This option lets you play raw video files. You have to use -demuxer rawvideo as well. </dd>
<p> Available options are: </p>
<dl>
<dl>
<dt>fps=&lt;value&gt;</dt>
<dd> rate in frames per second (default: 25.0)</dd>
<dt>sqcif|qcif|cif|4cif|pal|ntsc</dt>
<dd> set standard image size</dd>
<dt>w=&lt;value&gt;</dt>
<dd> image width in pixels</dd>
<dt>h=&lt;value&gt;</dt>
<dd> image height in pixels</dd>
<dt>i420|yv12|yuy2|y8</dt>
<dd> set colorspace</dd>
<dt>format=&lt;value&gt;</dt>
<dd> colorspace (fourcc) in hex or string constant. Use -rawvideo format=help for a list of possible strings.</dd>
<dt>size=&lt;value&gt;</dt>
<dd> frame size in Bytes</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer foreman.qcif -demuxer rawvideo -rawvideo qcif</dt>
<dd> Play the famous &quot;foreman&quot; sample video.</dd>
<dt>mplayer sample-720&#215;576.yuv -demuxer rawvideo -rawvideo w=720:h=576</dt>
<dd> Play a raw YUV sample.</dd></dl>
</dl>
<dt><code>-referrer &lt;string&gt; (network only)</code></dt>
<dd> Specify a referrer path or URL for HTTP requests.</dd>
<dt><code>-rtsp-port</code></dt>
<dd> Used with &#8216;<a href="rtsp://'">rtsp://&#8217;</a> URLs to force the client&#8217;s port number. This option may be useful if you are behind a router and want to forward the RTSP stream from the server to a specific client.</dd>
<dt><code>-rtsp-destination</code></dt>
<dd> Used with &#8216;<a href="rtsp://'">rtsp://&#8217;</a> URLs to force the destination IP address to be bound. This option may be useful with some RTSP server which do not send RTP packets to the right interface. If the connection to the RTSP server fails, use -v to see which IP address MPlayer tries to bind to and try to force it to one assigned to your computer instead.</dd>
<dt><code>-rtsp-stream-over-tcp (LIVE555 and NEMESI only)</code></dt>
<dd> Used with &#8216;<a href="rtsp://'">rtsp://&#8217;</a> URLs to specify that the resulting incoming RTP and RTCP packets be streamed over TCP (using the same TCP connection as RTSP). This option may be useful if you have a broken internet connection that does not pass incoming UDP packets (see <a rel="nofollow" href="http://www.live555.com/mplayer/">http://www.live555.com/mplayer/</a>).</dd>
<dt><code>-rtsp-stream-over-http (LIVE555 only)</code></dt>
<dd> Used with &#8216;<a rel="nofollow" href="http://'">http://&#8217;</a> URLs to specify that the resulting incoming RTP and RTCP packets be streamed over HTTP.</dd>
<dt><code>-saveidx &lt;filename&gt;</code></dt>
<dd> Force index rebuilding and dump the index to &lt;filename&gt;. Currently this only works with AVI files.<br />
 <i>NOTE:</i> This option is obsolete now that MPlayer has OpenDML support.</dd>
<dt><code>-sb &lt;byte position&gt; (also see -ss)</code></dt>
<dd> Seek to byte position. Useful for playback from CD-ROM images or VOB files with junk at the beginning.</dd>
<dt><code>-speed &lt;0.01-100&gt;</code></dt>
<dd> Slow down or speed up playback by the factor given as parameter. Not guaranteed to work correctly with -oac copy. Add -af scaletempo to get past the 4x limit on playback.</dd>
<dt><code>-srate &lt;Hz&gt;</code></dt>
<dd> Select the output sample rate to be used (of course sound cards have limits on this). If the sample frequency selected is different from that of the current media, the resample or lavcresample audio filter will be inserted into the audio filter layer to compensate for the difference. The type of resampling can be controlled by the -af-adv option. The default is fast resampling that may cause distortion.</dd>
<dt><code>-ss &lt;time&gt; (also see -sb)</code></dt>
<dd> Seek to given time position. Use -ss nopts to disable seeking, -ss 0 has different behaviour. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-ss 56</dt>
<dd> Seeks to 56 seconds.</dd>
<dt>-ss 01:10:00</dt>
<dd> Seeks to 1 hour 10 min.</dd></dl>
</dl>
<dt><code>-tskeepbroken</code></dt>
<dd> Tells MPlayer not to discard TS packets reported as broken in the stream. Sometimes needed to play corrupted MPEG-TS files.</dd>
<dt><code>-tsprobe &lt;byte position&gt;</code></dt>
<dd> When playing an MPEG-TS stream, this option lets you specify how many bytes in the stream you want MPlayer to search for the desired audio and video IDs.</dd>
<dt><code>-tsprog &lt;1-65534&gt;</code></dt>
<dd> When playing an MPEG-TS stream, you can specify with this option which program (if present) you want to play. Can be used with -vid and -aid.</dd>
<dt><code>-tv &lt;option1:option2:&#8230;&gt; (TV/PVR only)</code></dt>
<dd> This option tunes various properties of the TV capture module. For watching TV with MPlayer, use &#8216;tv://&#8217; or &#8216;tv://&lt;channel_number&gt;&#8217; or even &#8216;tv://&lt;channel_name&gt; (see option channels for channel_name below) as a movie URL. You can also use &#8216;tv:///&lt;input_id&gt;&#8217; to start watching a movie from a composite or S-Video input (see option input for details). </dd>
<p> Available options are:</p>
<dl>
<dl>
<dt>noaudio</dt>
<dd> no sound</dd>
<dt>automute=&lt;0-255&gt; (v4l and v4l2 only)</dt>
<dd> If signal strength reported by device is less than this value, audio and video will be muted. In most cases automute=100 will be enough. Default is 0 (automute disabled).</dd>
<dt>driver=&lt;value&gt;</dt>
<dd> See -tv driver=help for a list of compiled-in TV input drivers. available: dummy, v4l, v4l2, bsdbt848 (default: autodetect)</dd>
<dt>device=&lt;value&gt;</dt>
<dd> Specify TV device (default: /dev/video0). <i>NOTE:</i> For the bsdbt848 driver you can provide both bktr and tuner device names separating them with a comma, tuner after bktr (e.g. -tv device=/dev/bktr1,/dev/tuner1).</dd>
<dt>input=&lt;value&gt;</dt>
<dd> Specify input (default: 0 (TV), see console output for available inputs).</dd>
<dt>freq=&lt;value&gt;</dt>
<dd> Specify the frequency to set the tuner to (e.g. 511.250). Not compatible with the channels parameter.</dd>
<dt>outfmt=&lt;value&gt;</dt>
<dd> Specify the output format of the tuner with a preset value supported by the V4L driver (yv12, rgb32, rgb24, rgb16, rgb15, uyvy, yuy2, i420) or an arbitrary format given as hex value. Try outfmt=help for a list of all available formats.</dd>
<dt>width=&lt;value&gt;</dt>
<dd> output window width</dd>
<dt>height=&lt;value&gt;</dt>
<dd> output window height</dd>
<dt>fps=&lt;value&gt;</dt>
<dd> framerate at which to capture video (frames per second)</dd>
<dt>buffersize=&lt;value&gt;</dt>
<dd> maximum size of the capture buffer in megabytes (default: dynamical)</dd>
<dt>norm=&lt;value&gt;</dt>
<dd> For bsdbt848 and v4l, PAL, SECAM, NTSC are available. For v4l2, see the console output for a list of all available norms, also see the normid option below.</dd>
<dt>normid=&lt;value&gt; (v4l2 only)</dt>
<dd> Sets the TV norm to the given numeric ID. The TV norm depends on the capture card. See the console output for a list of available TV norms.</dd>
<dt>channel=&lt;value&gt;</dt>
<dd> Set tuner to &lt;value&gt; channel.</dd>
<dt>chanlist=&lt;value&gt;</dt>
<dd> available: argentina, australia, china-bcast, europe-east, europe-west, france, ireland, italy, japan-bcast, japan-cable, newzealand, russia, southafrica, us-bcast, us-cable, us-cable-hrc</dd>
<dt>channels=&lt;chan&gt;-&lt;name&gt;[=&lt;norm&gt;],&lt;chan&gt;-&lt;name&gt;[=&lt;norm&gt;],&#8230;</dt>
<dd> Set names for channels. <i>NOTE:</i> If &lt;chan&gt; is an integer greater than 1000, it will be treated as frequency (in kHz) rather than channel name from frequency table.<br />
 Use _ for spaces in names (or play with quoting ;-). The channel names will then be written using OSD, and the slave commands tv_step_channel, tv_set_channel and tv_last_channel will be usable for a remote control (see LIRC). Not compatible with the frequency parameter.<br />
 <i>NOTE:</i> The channel number will then be the position in the &#8216;channels&#8217; list, beginning with 1.<br />
 <i>EXAMPLE:</i> tv://1, tv://TV1, tv_set_channel 1, tv_set_channel TV1</dd>
<dt>[brightness|contrast|hue|saturation]=&lt;-100-100&gt;</dt>
<dd> Set the image equalizer on the card.</dd>
<dt>audiorate=&lt;value&gt;</dt>
<dd> Set input audio sample rate.</dd>
<dt>forceaudio</dt>
<dd> Capture audio even if there are no audio sources reported by v4l.</dd>
<dt>alsa&nbsp;</dt>
<dd> Capture from ALSA.</dd>
<dt>amode=&lt;0-3&gt;</dt>
<dd> Choose an audio mode:</dd>
<dl>
<dt>
</dt><dd> 0: mono<br />
 1: stereo<br />
 2: language 1<br />
 3: language 2</dd></dl>
<dt>forcechan=&lt;1-2&gt;</dt>
<dd> By default, the count of recorded audio channels is determined automatically by querying the audio mode from the TV card. This option allows forcing stereo/mono recording regardless of the amode option and the values returned by v4l. This can be used for troubleshooting when the TV card is unable to report the current audio mode.</dd>
<dt>adevice=&lt;value&gt;</dt>
<dd> Set an audio device. &lt;value&gt; should be /dev/xxx for OSS and a hardware ID for ALSA. You must replace any &#8216;:&#8217; by a &#8216;.&#8217; in the hardware ID for ALSA.</dd>
<dt>audioid=&lt;value&gt;</dt>
<dd> Choose an audio output of the capture card, if it has more than one.</dd>
<dt>[volume|bass|treble|balance]=&lt;0-65535&gt; (v4l1)</dt>
<dd>
</dd><dt>[volume|bass|treble|balance]=&lt;0-100&gt; (v4l2)</dt>
<dd> These options set parameters of the mixer on the video capture card. They will have no effect, if your card does not have one. For v4l2 50 maps to the default value of the control, as reported by the driver.</dd>
<dt>gain=&lt;0-100&gt; (v4l2)</dt>
<dd> Set gain control for video devices (usually webcams) to the desired value and switch off automatic control. A value of 0 enables automatic control. If this option is omitted, gain control will not be modified.</dd>
<dt>immediatemode=&lt;bool&gt;</dt>
<dd> A value of 0 means capture and buffer audio and video together (default for MEncoder). A value of 1 (default for MPlayer) means to do video capture only and let the audio go through a loopback cable from the TV card to the sound card.</dd>
<dt>mjpeg</dt>
<dd> Use hardware MJPEG compression (if the card supports it). When using this option, you do not need to specify the width and height of the output window, because MPlayer will determine it automatically from the decimation value (see below).</dd>
<dt>decimation=&lt;1|2|4&gt;</dt>
<dd> choose the size of the picture that will be compressed by hardware MJPEG compression:</dd>
<dl>
<dt>
</dt><dd> 1: full size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;704&#215;576&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PAL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;704&#215;480&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NTSC<br />
 2: medium size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;352&#215;288&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PAL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;352&#215;240&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NTSC<br />
 4: small size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;176&#215;144&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PAL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;176&#215;120&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NTSC</dd></dl>
<dt>quality=&lt;0-100&gt;</dt>
<dd> Choose the quality of the JPEG compression (&lt; 60 recommended for full size).</dd>
<dt>tdevice=&lt;value&gt;</dt>
<dd> Specify TV teletext device (example: /dev/vbi0) (default: none).</dd>
<dt>tformat=&lt;format&gt;</dt>
<dd> Specify TV teletext display format (default: 0):</dd>
<dl>
<dt>
</dt><dd> 0: opaque<br />
 1: transparent<br />
 2: opaque with inverted colors<br />
 3: transparent with inverted colors</dd></dl>
<dt>tpage=&lt;100-899&gt;</dt>
<dd> Specify initial TV teletext page number (default: 100).</dd>
<dt>tlang=&lt;-1-127&gt;</dt>
<dd> Specify default teletext language code (default: 0), which will be used as primary language until a type 28 packet is received. Useful when the teletext system uses a non-latin character set, but language codes are not transmitted via teletext type 28 packets for some reason. To see a list of supported language codes set this option to -1.</dd>
<dt>hidden_video_renderer (dshow only)</dt>
<dd> Terminate stream with video renderer instead of Null renderer (default: off). Will help if video freezes but audio does not. <i>NOTE:</i> May not work with -vo directx and -vf crop combination.</dd>
<dt>hidden_vp_renderer (dshow only)</dt>
<dd> Terminate VideoPort pin stream with video renderer instead of removing it from the graph (default: off). Useful if your card has a VideoPort pin and video is choppy. <i>NOTE:</i> May not work with -vo directx and -vf crop combination.</dd>
<dt>system_clock (dshow only)</dt>
<dd> Use the system clock as sync source instead of the default graph clock (usually the clock from one of the live sources in graph).</dd>
<dt>normalize_audio_chunks (dshow only)</dt>
<dd> Create audio chunks with a time length equal to video frame time length (default: off). Some audio cards create audio chunks about 0.5s in size, resulting in choppy video when using immediatemode=0.</dd></dl>
</dl>
<dt><code>-tvscan &lt;option1:option2:&#8230;&gt; (TV and MPlayer only)</code></dt>
<dd> Tune the TV channel scanner. MPlayer will also print value for &quot;-tv channels=&quot; option, including existing and just found channels. </dd>
<p> Available suboptions are:</p>
<dl>
<dl>
<dt>autostart</dt>
<dd> Begin channel scanning immediately after startup (default: disabled).</dd>
<dt>period=&lt;0.1-2.0&gt;</dt>
<dd> Specify delay in seconds before switching to next channel (default: 0.5). Lower values will cause faster scanning, but can detect inactive TV channels as active.</dd>
<dt>threshold=&lt;1-100&gt;</dt>
<dd> Threshold value for the signal strength (in percent), as reported by the device (default: 50). A signal strength higher than this value will indicate that the currently scanning channel is active.</dd></dl>
</dl>
<dt><code>-user &lt;username&gt; (also see -passwd) (network only)</code></dt>
<dd> Specify username for HTTP authentication.</dd>
<dt><code>-user-agent &lt;string&gt;</code></dt>
<dd> Use &lt;string&gt; as user agent for HTTP streaming.</dd>
<dt><code>-vid &lt;ID&gt;</code></dt>
<dd> Select video channel (MPG: 0-15, ASF: 0-255, MPEG-TS: 17-8190). When playing an MPEG-TS stream, MPlayer/MEncoder will use the first program (if present) with the chosen video stream.</dd>
<dt><code>-vivo &lt;suboption&gt; (DEBUG CODE)</code></dt>
<dd> Force audio parameters for the VIVO demuxer (for debugging purposes). FIXME: Document this.</dd></dl>
<h2>OSD/SUBTITLE OPTIONS</h2>
<p> <i>NOTE:</i> Also see -vf expand.</p>
<dl>
<dt><code>-ass (FreeType only)</code></dt>
<dd> Turn on SSA/ASS subtitle rendering. With this option, libass will be used for SSA/ASS external subtitles and Matroska tracks. You may also want to use -embeddedfonts.<br />
 <i>NOTE:</i> Unlike normal OSD, libass uses fontconfig by default. To disable it, use -nofontconfig.</dd>
<dt><code>-ass-border-color &lt;value&gt;</code></dt>
<dd> Sets the border (outline) color for text subtitles. The color format is RRGGBBAA.</dd>
<dt><code>-ass-bottom-margin &lt;value&gt;</code></dt>
<dd> Adds a black band at the bottom of the frame. The SSA/ASS renderer can place subtitles there (with -ass-use-margins).</dd>
<dt><code>-ass-color &lt;value&gt;</code></dt>
<dd> Sets the color for text subtitles. The color format is RRGGBBAA.</dd>
<dt><code>-ass-font-scale &lt;value&gt;</code></dt>
<dd> Set the scale coefficient to be used for fonts in the SSA/ASS renderer.</dd>
<dt><code>-ass-force-style &lt;[Style.]Param=Value[,&#8230;]&gt;</code></dt>
<dd> Override some style or script info parameters. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -ass-force-style FontName=Arial,Default.Bold=1<br />
 -ass-force-style PlayResY=768</dd></dl>
<dt><code>-ass-hinting &lt;type&gt;</code></dt>
<dd> Set hinting type. &lt;type&gt; can be:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> no hinting</dd>
<dt>1</dt>
<dd> FreeType autohinter, light mode</dd>
<dt>2</dt>
<dd> FreeType autohinter, normal mode</dd>
<dt>3</dt>
<dd> font native hinter</dd>
<dt>0-3 + 4</dt>
<dd> The same, but hinting will only be performed if the OSD is rendered at screen resolution and will therefore not be scaled.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> The default value is 7 (use native hinter for unscaled OSD and no hinting otherwise).</dd></dl>
<dt><code>-ass-line-spacing &lt;value&gt;</code></dt>
<dd> Set line spacing value for SSA/ASS renderer.</dd>
<dt><code>-ass-styles &lt;filename&gt;</code></dt>
<dd> Load all SSA/ASS styles found in the specified file and use them for rendering text subtitles. The syntax of the file is exactly like the [V4 Styles] / [V4+ Styles] section of SSA/ASS.</dd>
<dt><code>-ass-top-margin &lt;value&gt;</code></dt>
<dd> Adds a black band at the top of the frame. The SSA/ASS renderer can place toptitles there (with -ass-use-margins).</dd>
<dt><code>-ass-use-margins</code></dt>
<dd> Enables placing toptitles and subtitles in black borders when they are available.</dd>
<dt><code>-dumpjacosub (MPlayer only)</code></dt>
<dd> Convert the given subtitle (specified with the -sub option) to the time-based JACOsub subtitle format. Creates a dumpsub.js file in the current directory.</dd>
<dt><code>-dumpmicrodvdsub (MPlayer only)</code></dt>
<dd> Convert the given subtitle (specified with the -sub option) to the MicroDVD subtitle format. Creates a dumpsub.sub file in the current directory.</dd>
<dt><code>-dumpmpsub (MPlayer only)</code></dt>
<dd> Convert the given subtitle (specified with the -sub option) to MPlayer&#8217;s subtitle format, MPsub. Creates a dump.mpsub file in the current directory.</dd>
<dt><code>-dumpsami (MPlayer only)</code></dt>
<dd> Convert the given subtitle (specified with the -sub option) to the time-based SAMI subtitle format. Creates a dumpsub.smi file in the current directory.</dd>
<dt><code>-dumpsrtsub (MPlayer only)</code></dt>
<dd> Convert the given subtitle (specified with the -sub option) to the time-based SubViewer (SRT) subtitle format. Creates a dumpsub.srt file in the current directory.<br />
 <i>NOTE:</i> Some broken hardware players choke on SRT subtitle files with Unix line endings. If you are unlucky enough to have such a box, pass your subtitle files through unix2dos or a similar program to replace Unix line endings with DOS/Windows line endings.</dd>
<dt><code>-dumpsub (MPlayer only) (BETA CODE)</code></dt>
<dd> Dumps the subtitle substream from VOB streams. Also see the -dump*sub and -vobsubout* options.</dd>
<dt><code>-embeddedfonts (FreeType only)</code></dt>
<dd> Enables extraction of Matroska embedded fonts (default: disabled). These fonts can be used for SSA/ASS subtitle rendering (-ass option). Font files are created in the ~/.mplayer/fonts directory.<br />
 <i>NOTE:</i> With FontConfig 2.4.2 or newer, embedded fonts are opened directly from memory, and this option is enabled by default.</dd>
<dt><code>-ffactor &lt;number&gt;</code></dt>
<dd> Resample the font alphamap. Can be:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> plain white fonts</dd>
<dt>0.75</dt>
<dd> very narrow black outline (default)</dd>
<dt>1</dt>
<dd> narrow black outline</dd>
<dt>10</dt>
<dd> bold black outline</dd></dl>
</dl>
<dt><code>-flip-hebrew (FriBiDi only)</code></dt>
<dd> Turns on flipping subtitles using FriBiDi.</dd>
<dt><code>-noflip-hebrew-commas</code></dt>
<dd> Change FriBiDi&#8217;s assumptions about the placements of commas in subtitles. Use this if commas in subtitles are shown at the start of a sentence instead of at the end.</dd>
<dt><code>-font &lt;path to font.desc file, path to font (FreeType), font pattern (Fontconfig)&gt;</code></dt>
<dd> Search for the OSD/subtitle fonts in an alternative directory (default for normal fonts: ~/.mplayer/font/font.desc, default for FreeType fonts: ~/.mplayer/subfont.ttf, default for Fontconfig: &quot;sans-serif&quot;).<br />
 <i>NOTE:</i> With FreeType, this option determines the path to the font file. With Fontconfig, this option determines the Fontconfig font pattern. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -font ~/.mplayer/arial-14/font.desc<br />
 -font ~/.mplayer/arialuni.ttf<br />
 -font &#8216;Bitstream Vera Sans&#8217;<br />
 -font &#8216;Bitstream Vera Sans:style=Bold&#8217;</dd></dl>
<dt><code>-fontconfig (fontconfig only)</code></dt>
<dd> Enables the usage of fontconfig managed fonts (default: autodetect).<br />
 <i>NOTE:</i> By default fontconfig is used for libass-rendered subtitles and not used for OSD. With -fontconfig it is used for both libass and OSD, with -nofontconfig it is not used at all, i.e. only then -font and -subfont will work with a given path to font.</dd>
<dt><code>-forcedsubsonly</code></dt>
<dd> Display only forced subtitles for the DVD subtitle stream selected by e.g. -slang.</dd>
<dt><code>-fribidi-charset &lt;charset name&gt; (FriBiDi only)</code></dt>
<dd> Specifies the character set that will be passed to FriBiDi when decoding non-UTF-8 subtitles (default: ISO8859-8).</dd>
<dt><code>-ifo &lt;VOBsub IFO file&gt;</code></dt>
<dd> Indicate the file that will be used to load palette and frame size for VOBsub subtitles.</dd>
<dt><code>-noautosub</code></dt>
<dd> Turns off automatic subtitle file loading. Note: VOBsub subtitles are not affected.</dd>
<dt><code>-osd-duration &lt;time&gt;</code></dt>
<dd> Set the duration of the OSD messages in ms (default: 1000).</dd>
<dt><code>-osd-fractions &lt;0-2&gt;</code></dt>
<dd> Set how fractions of seconds of the current timestamp are printed on the OSD:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Do not display fractions (default).</dd>
<dt>1</dt>
<dd> Show the first two decimals.</dd>
<dt>2</dt>
<dd> Show approximated frame count within current second. This frame count is not accurate but only an approximation. For variable fps, the approximation is known to be far off the correct frame count.</dd></dl>
</dl>
<dt><code>-osdlevel &lt;0-3&gt; (MPlayer only)</code></dt>
<dd> Specifies which mode the OSD should start in.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> subtitles only</dd>
<dt>1</dt>
<dd> volume + seek (default)</dd>
<dt>2</dt>
<dd> volume + seek + timer + percentage</dd>
<dt>3</dt>
<dd> volume + seek + timer + percentage + total time</dd></dl>
</dl>
<dt><code>-overlapsub</code></dt>
<dd> Allows the next subtitle to be displayed while the current one is still visible (default is to enable the support only for specific formats).</dd>
<dt><code>-progbar-align &lt;0-100&gt;</code></dt>
<dd> Specify the vertical alignment of the progress bar (0: top, 100: bottom, default is 50, i.e. centered).</dd>
<dt><code>-sid &lt;ID&gt; (also see -slang, -vobsubid)</code></dt>
<dd> Display the subtitle stream specified by &lt;ID&gt; (0-31). MPlayer prints the available subtitle IDs when run in verbose (-v) mode. If you cannot select one of the subtitles on a DVD, also try -vobsubid.</dd>
<dt><code>-nosub</code></dt>
<dd> Disables any otherwise auto-selected internal subtitles (as e.g. the Matroska/mkv demuxer supports). Use -noautosub to disable the loading of external subtitle files.</dd>
<dt><code>-slang &lt;language code[,language code,&#8230;]&gt; (also see -sid)</code></dt>
<dd> Specify a priority list of subtitle languages to use. Different container formats employ different language codes. DVDs use ISO 639-1 two letter language codes, Matroska uses ISO 639-2 three letter language codes while OGM uses a free-form identifier. MPlayer prints the available languages when run in verbose (-v) mode. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>mplayer <a href="dvd://1">dvd://1</a> -slang hu,en</dt>
<dd> Chooses the Hungarian subtitle track on a DVD and falls back on English if Hungarian is not available.</dd>
<dt>mplayer -slang jpn example.mkv</dt>
<dd> Plays a Matroska file with Japanese subtitles.</dd></dl>
</dl>
<dt><code>-spuaa &lt;mode&gt;</code></dt>
<dd> Antialiasing/scaling mode for DVD/VOBsub. A value of 16 may be added to &lt;mode&gt; in order to force scaling even when original and scaled frame size already match. This can be employed to e.g. smooth subtitles with gaussian blur. Available modes are:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> none (fastest, very ugly)</dd>
<dt>1</dt>
<dd> approximate (broken?)</dd>
<dt>2</dt>
<dd> full (slow)</dd>
<dt>3</dt>
<dd> bilinear (default, fast and not too bad)</dd>
<dt>4</dt>
<dd> uses swscaler gaussian blur (looks very good)</dd></dl>
</dl>
<dt><code>-spualign &lt;-1-2&gt;</code></dt>
<dd> Specify how SPU (DVD/VOBsub) subtitles should be aligned.</dd>
<dl>
<dl>
<dt>-1</dt>
<dd> original position</dd>
<dt> 0</dt>
<dd> Align at top (original behavior, default).</dd>
<dt> 1</dt>
<dd> Align at center.</dd>
<dt> 2</dt>
<dd> Align at bottom.</dd></dl>
</dl>
<dt><code>-spugauss &lt;0.0-3.0&gt;</code></dt>
<dd> Variance parameter of gaussian used by -spuaa 4. Higher means more blur (default: 1.0).</dd>
<dt><code>-sub &lt;subtitlefile1,subtitlefile2,&#8230;&gt;</code></dt>
<dd> Use/display these subtitle files. Only one file can be displayed at the same time.</dd>
<dt><code>-sub-bg-alpha &lt;0-255&gt;</code></dt>
<dd> Specify the alpha channel value for subtitles and OSD backgrounds. Big values mean more transparency. 0 means completely transparent.</dd>
<dt><code>-sub-bg-color &lt;0-255&gt;</code></dt>
<dd> Specify the color value for subtitles and OSD backgrounds. Currently subtitles are grayscale so this value is equivalent to the intensity of the color. 255 means white and 0 black.</dd>
<dt><code>-sub-demuxer &lt;[+]name&gt; (-subfile only) (BETA CODE)</code></dt>
<dd> Force subtitle demuxer type for -subfile. Use a &#8216;+&#8217; before the name to force it, this will skip some checks! Give the demuxer name as printed by -sub-demuxer help. For backward compatibility it also accepts the demuxer ID as defined in subreader.h.</dd>
<dt><code>-sub-fuzziness &lt;mode&gt;</code></dt>
<dd> Adjust matching fuzziness when searching for subtitles (does not apply to VOBsub):</dd>
<dl>
<dl>
<dt>0</dt>
<dd> exact match (default)</dd>
<dt>1</dt>
<dd> Load all subs containing movie name.</dd>
<dt>2</dt>
<dd> Load all subs in the current and -sub-paths directories.</dd></dl>
</dl>
<dt><code>-sub-no-text-pp</code></dt>
<dd> Disables any kind of text post processing done after loading the subtitles. Used for debug purposes.</dd>
<dt><code>-subalign &lt;0-2&gt;</code></dt>
<dd> Specify which edge of the subtitles should be aligned at the height given by -subpos.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Align subtitle top edge (original behavior).</dd>
<dt>1</dt>
<dd> Align subtitle center.</dd>
<dt>2</dt>
<dd> Align subtitle bottom edge (default).</dd></dl>
</dl>
<dt><code>-subcc &lt;1-8&gt;&nbsp;</code></dt>
<dd> Display DVD Closed Caption (CC) subtitles from the specified channel. Values 5 to 8 select a mode that can extract EIA-608 compatibility streams from EIA-708 data. These are <code>not</code> the VOB subtitles, these are special ASCII subtitles for the hearing impaired encoded in the VOB userdata stream on most region 1 DVDs. CC subtitles have not been spotted on DVDs from other regions so far.</dd>
<dt><code>-subcp &lt;codepage&gt; (iconv only)</code></dt>
<dd> If your system supports iconv(3), you can use this option to specify the subtitle codepage. It takes priority over both -utf8 and -unicode. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -subcp latin2<br />
 -subcp cp1250</dd></dl>
<dt><code>-subcp enca:&lt;language&gt;:&lt;fallback codepage&gt; (ENCA only)</code></dt>
<dd> You can specify your language using a two letter language code to make ENCA detect the codepage automatically. If unsure, enter anything and watch mplayer -v output for available languages. Use __ (two underscores) if your language is not supported. Fallback codepage specifies the codepage to use, when autodetection fails. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-subcp enca:cs:latin2</dt>
<dd> Guess the encoding, assuming the subtitles are Czech, fall back on latin 2, if the detection fails.</dd>
<dt>-subcp enca:pl:cp1250</dt>
<dd> Guess the encoding for Polish, fall back on cp1250.</dd>
<dt>-subcp enca:__:latin1</dt>
<dd> Generic detection (mostly unicode) with latin1 fallback.</dd></dl>
</dl>
<dt><code>-sub-paths &lt;path1,path2,&#8230;&gt;</code></dt>
<dd> Specify extra subtitle paths to track in the media directory. </dd>
<p> <i>EXAMPLE:</i> Assuming that /path/to/movie/movie.avi is played and -sub-paths sub,subtitles,/tmp/subs is specified, MPlayer searches for subtitle files in these directories:</p>
<dl>
<dt>
</dt><dd> /path/to/movie/<br />
 /path/to/movie/sub/<br />
 /path/to/movie/subtitles/<br />
 /tmp/subs/<br />
 ~/.mplayer/sub/</dd></dl>
<dt><code>-subdelay &lt;sec&gt;</code></dt>
<dd> Delays subtitles by &lt;sec&gt; seconds. Can be negative.</dd>
<dt><code>-subfile &lt;filename&gt; (BETA CODE)</code></dt>
<dd> Currently useless. Same as -audiofile, but for subtitle streams (OggDS?).</dd>
<dt><code>-subfont &lt;path to font (FreeType), font pattern (Fontconfig)&gt; (FreeType only)</code></dt>
<dd> Sets the subtitle font (see -font). If no -subfont is given, -font is used.</dd>
<dt><code>-subfont-autoscale &lt;0-3&gt; (FreeType only)</code></dt>
<dd> Sets the autoscale mode.<br />
 <i>NOTE:</i> 0 means that text scale and OSD scale are font heights in points. </dd>
<p> The mode can be: </p>
<dl>
<dl>
<dt>0</dt>
<dd> no autoscale</dd>
<dt>1</dt>
<dd> proportional to movie height</dd>
<dt>2</dt>
<dd> proportional to movie width</dd>
<dt>3</dt>
<dd> proportional to movie diagonal (default)</dd></dl>
</dl>
<dt><code>-subfont-blur &lt;0-8&gt; (FreeType only)</code></dt>
<dd> Sets the font blur radius (default: 2).</dd>
<dt><code>-subfont-encoding &lt;value&gt;</code></dt>
<dd> Sets the font encoding. When set to &#8216;unicode&#8217;, all the glyphs from the font file will be rendered and unicode will be used (default: unicode). (Without FreeType, setting any other value than &#8216;unicode&#8217; will disable unicode glyphs rendering for font.desc files. With FreeType and for other values than &#8216;unicode&#8217; your system has to support iconv(3) in order for this to work.)</dd>
<dt><code>-subfont-osd-scale &lt;0-100&gt; (FreeType only)</code></dt>
<dd> Sets the autoscale coefficient of the OSD elements (default: 6).</dd>
<dt><code>-subfont-outline &lt;0-8&gt; (FreeType only)</code></dt>
<dd> Sets the font outline thickness (default: 2).</dd>
<dt><code>-subfont-text-scale &lt;0-100&gt; (FreeType only)</code></dt>
<dd> Sets the subtitle text autoscale coefficient as percentage of the screen size (default: 5).</dd>
<dt><code>-subfps &lt;rate&gt;</code></dt>
<dd> Specify the framerate of the subtitle file (default: movie fps).<br />
 <i>NOTE:</i> &lt;rate&gt; &gt; movie fps speeds the subtitles up for frame-based subtitle files and slows them down for time-based ones.</dd>
<dt><code>-subpos &lt;0-150&gt; (useful with -vf expand)</code></dt>
<dd> Specify the position of subtitles on the screen. The value is the vertical position of the subtitle in % of the screen height. Values larger than 100 allow part of the subtitle to be cut off.</dd>
<dt><code>-subwidth &lt;10-100&gt;</code></dt>
<dd> Specify the maximum width of subtitles on the screen. Useful for TV-out. The value is the width of the subtitle in % of the screen width.</dd>
<dt><code>-noterm-osd</code></dt>
<dd> Disable the display of OSD messages on the console when no video output is available.</dd>
<dt><code>-term-osd-esc &lt;escape sequence&gt;</code></dt>
<dd> Specify the escape sequence to use before writing an OSD message on the console. The escape sequence should move the pointer to the beginning of the line used for the OSD and clear it (default: ^[[A
^[[K).</dd>
<dt><code>-unicode</code></dt>
<dd> Tells MPlayer to handle the subtitle file as unicode. (It will only take effect if neither -subcp nor -utf8 is given.)</dd>
<dt><code>-unrarexec &lt;path to unrar executable&gt; (not supported on MingW)</code></dt>
<dd> Specify the path to the unrar executable so MPlayer can use it to access rar-compressed VOBsub files (default: not set, so the feature is off). The path must include the executable&#8217;s filename, i.e. /usr/local/bin/unrar.</dd>
<dt><code>-utf8 &nbsp;<wbr>&nbsp;</code></dt>
<dd> Tells MPlayer to handle the subtitle file as UTF-8. (It will only take effect if -subcp isn&#8217;t given, and it takes priority over -unicode.)</dd>
<dt><code>-vobsub &lt;VOBsub file without extension&gt;</code></dt>
<dd> Specify a VOBsub file to use for subtitles. Has to be the full pathname without extension, i.e. without the &#8216;.idx&#8217;, &#8216;.ifo&#8217; or &#8216;.sub&#8217;.</dd>
<dt><code>-vobsubid &lt;0-31&gt;</code></dt>
<dd> Specify the VOBsub subtitle ID.</dd></dl>
<h2>AUDIO OUTPUT OPTIONS (MPLAYER ONLY)</h2>
<dl>
<dt><code>-abs &lt;value&gt; (-ao oss only) (OBSOLETE)</code></dt>
<dd> Override audio driver/card buffer size detection.</dd>
<dt><code>-format &lt;format&gt; (also see the format audio filter)</code></dt>
<dd> Select the sample format used for output from the audio filter layer to the sound card. The values that &lt;format&gt; can adopt are listed below in the description of the format audio filter.</dd>
<dt><code>-mixer &lt;device&gt;</code></dt>
<dd> Use a mixer device different from the default /dev/mixer. For ALSA this is the mixer name.</dd>
<dt><code>-mixer-channel &lt;mixer line&gt;[,mixer index] (-ao oss and -ao alsa only)</code></dt>
<dd> This option will tell MPlayer to use a different channel for controlling volume than the default PCM. Options for OSS include <code>vol, pcm, line.</code> For a complete list of options look for SOUND_DEVICE_NAMES in /usr/include/linux/soundcard.h. For ALSA you can use the names e.g. alsamixer displays, like <code>Master, Line, PCM.</code><br />
 <i>NOTE:</i> ALSA mixer channel names followed by a number must be specified in the &lt;name,number&gt; format, i.e. a channel labeled &#8216;PCM 1&#8217; in alsamixer must be converted to <code>PCM,1</code>.</dd>
<dt><code>-softvol</code></dt>
<dd> Force the use of the software mixer, instead of using the sound card mixer.</dd>
<dt><code>-softvol-max &lt;10.0-10000.0&gt;</code></dt>
<dd> Set the maximum amplification level in percent (default: 110). A value of 200 will allow you to adjust the volume up to a maximum of double the current level. With values below 100 the initial volume (which is 100%) will be above the maximum, which e.g. the OSD cannot display correctly.</dd>
<dt><code>-volstep &lt;0-100&gt;</code></dt>
<dd> Set the step size of mixer volume changes in percent of the whole range (default: 3).</dd>
<dt><code>-volume &lt;-1-100&gt; (also see -af volume)</code></dt>
<dd> Set the startup volume in the mixer, either hardware or software (if used with -softvol). A value of -1 (the default) will not change the volume.</dd></dl>
<h2>AUDIO OUTPUT DRIVERS (MPLAYER ONLY)</h2>
<p> Audio output drivers are interfaces to different audio output facilities. The syntax is:</p>
<dl>
<dt><code>-ao &lt;driver1[:suboption1[=value]:&#8230;],driver2,&#8230;[,]&gt;</code></dt>
<dd> Specify a priority list of audio output drivers to be used.</dd></dl>
<p> If the list has a trailing &#8216;,&#8217; MPlayer will fall back on drivers not contained in the list. Suboptions are optional and can mostly be omitted.<br />
 <i>NOTE:</i> See -ao help for a list of compiled-in audio output drivers. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-ao alsa,oss,</dt>
<dd> Try the ALSA driver, then the OSS driver, then others.</dd>
<dt>-ao alsa:noblock:device=hw=0.3</dt>
<dd> Sets noblock-mode and the device-name as first card, fourth device.</dd></dl>
</dl>
<p> Available audio output drivers are:</p>
<dl>
<dt><code>alsa&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> ALSA 0.9/1.x audio output driver</dd>
<dl>
<dl>
<dt>noblock</dt>
<dd> Sets noblock-mode.</dd>
<dt>device=&lt;device&gt;</dt>
<dd> Sets the device name. Replace any &#8216;,&#8217; with &#8216;.&#8217; and any &#8216;:&#8217; with &#8216;=&#8217; in the ALSA device name. For hwac3 output via S/PDIF, use an &quot;iec958&quot; or &quot;spdif&quot; device, unless you really know how to set it correctly.</dd></dl>
</dl>
<dt><code>oss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> OSS audio output driver</dd>
<dl>
<dl>
<dt>&lt;dsp-device&gt;</dt>
<dd> Sets the audio output device (default: /dev/dsp).</dd>
<dt>&lt;mixer-device&gt;</dt>
<dd> Sets the audio mixer device (default: /dev/mixer).</dd>
<dt>&lt;mixer-channel&gt;</dt>
<dd> Sets the audio mixer channel (default: pcm).</dd></dl>
</dl>
<dt><code>sdl (SDL only)</code></dt>
<dd> highly platform independent SDL (Simple Directmedia Layer) library audio output driver</dd>
<dl>
<dl>
<dt>&lt;driver&gt;</dt>
<dd> Explicitly choose the SDL audio driver to use (default: let SDL choose).</dd></dl>
</dl>
<dt><code>arts&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> audio output through the aRts daemon</dd>
<dt><code>esd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> audio output through the ESD daemon</dd>
<dl>
<dl>
<dt>&lt;server&gt;</dt>
<dd> Explicitly choose the ESD server to use (default: localhost).</dd></dl>
</dl>
<dt><code>jack&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> audio output through JACK (Jack Audio Connection Kit)</dd>
<dl>
<dl>
<dt>(no)connect</dt>
<dd> Automatically create connections to output ports (default: enabled). When enabled, the maximum number of output channels will be limited to the number of available output ports.</dd>
<dt>port=&lt;name&gt;</dt>
<dd> Connects to the ports with the given name (default: physical ports).</dd>
<dt>name=&lt;client</dt>
<dd> Client name that is passed to JACK (default: MPlayer [&lt;PID&gt;]). Useful if you want to have certain connections established automatically.</dd>
<dt>(no)estimate</dt>
<dd> Estimate the audio delay, supposed to make the video playback smoother (default: enabled).</dd>
<dt>(no)autostart</dt>
<dd> Automatically start jackd if necessary (default: disabled). Note that this seems unreliable and will spam stdout with server messages.</dd></dl>
</dl>
<dt><code>nas&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> audio output through NAS</dd>
<dt><code>coreaudio (Mac OS X only)</code></dt>
<dd> native Mac OS X audio output driver</dd>
<dl>
<dl>
<dt>device_id=&lt;id&gt;</dt>
<dd> ID of output device to use (0 = default device)</dd>
<dt>help</dt>
<dd> List all available output devices with their IDs.</dd></dl>
</dl>
<dt><code>openal&nbsp;</code></dt>
<dd> Experimental OpenAL audio output driver</dd>
<dt><code>pulse&nbsp;<wbr>&nbsp;</code></dt>
<dd> PulseAudio audio output driver</dd>
<dl>
<dl>
<dt>[&lt;host&gt;[:&lt;output sink&gt;[:broken_pause]]]</dt>
<dd> Specify the host and optionally output sink to use. An empty &lt;host&gt; string uses a local connection, &quot;localhost&quot; uses network transfer (most likely not what you want). You can also explicitly force the workaround for broken pause functionality (default: autodetected). To only enable that without specifying a host/sink the syntax is -ao pulse:::broken_pause</dd></dl>
</dl>
<dt><code>sgi (SGI only)</code></dt>
<dd> native SGI audio output driver</dd>
<dl>
<dl>
<dt>&lt;output device name&gt;</dt>
<dd> Explicitly choose the output device/interface to use (default: system-wide default). For example, &#8216;Analog Out&#8217; or &#8216;Digital Out&#8217;.</dd></dl>
</dl>
<dt><code>sun (Sun only)</code></dt>
<dd> native Sun audio output driver</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the audio device to use (default: /dev/audio).</dd></dl>
</dl>
<dt><code>win32 (Windows only)</code></dt>
<dd> native Windows waveout audio output driver</dd>
<dt><code>dsound (Windows only)</code></dt>
<dd> DirectX DirectSound audio output driver</dd>
<dl>
<dl>
<dt>device=&lt;devicenum&gt;</dt>
<dd> Sets the device number to use. Playing a file with -v will show a list of available devices.</dd></dl>
</dl>
<dt><code>kai (OS/2 only)</code></dt>
<dd> OS/2 KAI audio output driver</dd>
<dl>
<dl>
<dt>uniaud</dt>
<dd> Force UNIAUD mode.</dd>
<dt>dart</dt>
<dd> Force DART mode.</dd>
<dt>(no)share</dt>
<dd> Open audio in shareable or exclusive mode.</dd>
<dt>bufsize=&lt;size&gt;</dt>
<dd> Set buffer size to &lt;size&gt; in samples (default: 2048).</dd></dl>
</dl>
<dt><code>dart (OS/2 only)</code></dt>
<dd> OS/2 DART audio output driver</dd>
<dl>
<dl>
<dt>(no)share</dt>
<dd> Open DART in shareable or exclusive mode.</dd>
<dt>bufsize=&lt;size&gt;</dt>
<dd> Set buffer size to &lt;size&gt; in samples (default: 2048).</dd></dl>
</dl>
<dt><code>dxr2 (also see -dxr2) (DXR2 only)</code></dt>
<dd> Creative DXR2 specific output driver</dd>
<dt><code>ivtv (IVTV only)</code></dt>
<dd> IVTV specific MPEG audio output driver. Works with -ac hwmpa only.</dd>
<dt><code>v4l2 (requires Linux 2.6.22+ kernel)</code></dt>
<dd> Audio output driver for V4L2 cards with hardware MPEG decoder.</dd>
<dt><code>mpegpes (DVB only)</code></dt>
<dd> Audio output driver for DVB cards that writes the output to an MPEG-PES file if no DVB card is installed.</dd>
<dl>
<dl>
<dt>card=&lt;1-4&gt;</dt>
<dd> DVB card to use if more than one card is present. If not specified MPlayer will search the first usable card.</dd>
<dt>file=&lt;filename&gt;</dt>
<dd> output filename</dd></dl>
</dl>
<dt><code>null&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Produces no audio output but maintains video playback speed. Use -nosound for benchmarking.</dd>
<dt><code>pcm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> raw PCM/wave file writer audio output</dd>
<dl>
<dl>
<dt>(no)waveheader</dt>
<dd> Include or do not include the wave header (default: included). When not included, raw PCM will be generated.</dd>
<dt>file=&lt;filename&gt;</dt>
<dd> Write the sound to &lt;filename&gt; instead of the default audiodump.wav. If nowaveheader is specified, the default is audiodump.pcm.</dd>
<dt>fast&nbsp;</dt>
<dd> Try to dump faster than realtime. Make sure the output does not get truncated (usually with &quot;Too many video packets in buffer&quot; message). It is normal that you get a &quot;Your system is too SLOW to play this!&quot; message.</dd></dl>
</dl>
<dt><code>plugin&nbsp;<wbr>&nbsp;</code></dt>
<dd> plugin audio output driver</dd></dl>
<h2>VIDEO OUTPUT OPTIONS (MPLAYER ONLY)</h2>
<dl>
<dt><code>-adapter &lt;value&gt;</code></dt>
<dd> Set the graphics card that will receive the image. You can get a list of available cards when you run this option with -v. Currently only works with the directx video output driver.</dd>
<dt><code>-bpp &lt;depth&gt;</code></dt>
<dd> Override the autodetected color depth. Only supported by the fbdev, dga, svga, vesa video output drivers.</dd>
<dt><code>-border</code></dt>
<dd> Play movie with window border and decorations. Since this is on by default, use -noborder to disable the standard window decorations.</dd>
<dt><code>-brightness &lt;-100-100&gt;</code></dt>
<dd> Adjust the brightness of the video signal (default: 0). Not supported by all video output drivers.</dd>
<dt><code>-contrast &lt;-100-100&gt;</code></dt>
<dd> Adjust the contrast of the video signal (default: 0). Not supported by all video output drivers.</dd>
<dt><code>-display &lt;name&gt; (X11 only)</code></dt>
<dd> Specify the hostname and display number of the X server you want to display on. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -display xtest.localdomain:0</dd></dl>
<dt><code>-dr &nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Turns on direct rendering (not supported by all codecs and video outputs). This can result in significantly faster blitting on some systems, on most the difference will be minimal. In some cases, particularly with decoders specifying their buffer requirements badly, it can be vastly slower.<br />
 <i>WARNING:</i> May cause OSD/SUB corruption!</dd>
<dt><code>-dxr2 &lt;option1:option2:&#8230;&gt;</code></dt>
<dd> This option is used to control the dxr2 video output driver.</dd>
<dl>
<dl>
<dt>ar-mode=&lt;value&gt;</dt>
<dd> aspect ratio mode (0 = normal, 1 = pan-and-scan, 2 = letterbox (default))</dd>
<dt>iec958-encoded</dt>
<dd> Set iec958 output mode to encoded.</dd>
<dt>iec958-decoded</dt>
<dd> Set iec958 output mode to decoded (default).</dd>
<dt>macrovision=&lt;value&gt;</dt>
<dd> macrovision mode (0 = off (default), 1 = agc, 2 = agc 2 colorstripe, 3 = agc 4 colorstripe)</dd>
<dt>mute&nbsp;</dt>
<dd> mute sound output</dd>
<dt>unmute</dt>
<dd> unmute sound output</dd>
<dt>ucode=&lt;value&gt;</dt>
<dd> path to the microcode</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>TV output</i></dd></dl>
<dl>
<dl>
<dt>75ire</dt>
<dd> enable 7.5 IRE output mode</dd>
<dt>no75ire</dt>
<dd> disable 7.5 IRE output mode (default)</dd>
<dt>bw&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> b/w TV output</dd>
<dt>color</dt>
<dd> color TV output (default)</dd>
<dt>interlaced</dt>
<dd> interlaced TV output (default)</dd>
<dt>nointerlaced</dt>
<dd> disable interlaced TV output</dd>
<dt>norm=&lt;value&gt;</dt>
<dd> TV norm (ntsc (default), pal, pal60, palm, paln, palnc)</dd>
<dt>square-pixel</dt>
<dd> set pixel mode to square</dd>
<dt>ccir601-pixel</dt>
<dd> set pixel mode to ccir601</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>overlay</i></dd></dl>
<dl>
<dl>
<dt>cr-left=&lt;0-500&gt;</dt>
<dd> Set the left cropping value (default: 50).</dd>
<dt>cr-right=&lt;0-500&gt;</dt>
<dd> Set the right cropping value (default: 300).</dd>
<dt>cr-top=&lt;0-500&gt;</dt>
<dd> Set the top cropping value (default: 0).</dd>
<dt>cr-bottom=&lt;0-500&gt;</dt>
<dd> Set the bottom cropping value (default: 0).</dd>
<dt>ck-[r|g|b]=&lt;0-255&gt;</dt>
<dd> Set the r(ed), g(reen) or b(lue) gain of the overlay color-key.</dd>
<dt>ck-[r|g|b]min=&lt;0-255&gt;</dt>
<dd> minimum value for the respective color key</dd>
<dt>ck-[r|g|b]max=&lt;0-255&gt;</dt>
<dd> maximum value for the respective color key</dd>
<dt>ignore-cache</dt>
<dd> Ignore cached overlay settings.</dd>
<dt>update-cache</dt>
<dd> Update cached overlay settings.</dd>
<dt>ol-osd</dt>
<dd> Enable overlay onscreen display.</dd>
<dt>nool-osd</dt>
<dd> Disable overlay onscreen display (default).</dd>
<dt>ol[h|w|x|y]-cor=&lt;-20-20&gt;</dt>
<dd> Adjust the overlay size (h,w) and position (x,y) in case it does not match the window perfectly (default: 0).</dd>
<dt>overlay</dt>
<dd> Activate overlay (default).</dd>
<dt>nooverlay</dt>
<dd> Activate TV-out.</dd>
<dt>overlay-ratio=&lt;1-2500&gt;</dt>
<dd> Tune the overlay (default: 1000).</dd></dl>
</dl>
<dt><code>-fbmode &lt;modename&gt; (-vo fbdev only)</code></dt>
<dd> Change video mode to the one that is labeled as &lt;modename&gt; in /etc/fb.modes.<br />
 <i>NOTE:</i> VESA framebuffer does not support mode changing.</dd>
<dt><code>-fbmodeconfig &lt;filename&gt; (-vo fbdev only)</code></dt>
<dd> Override framebuffer mode configuration file (default: /etc/fb.modes).</dd>
<dt><code>-fs (also see -zoom)</code></dt>
<dd> Fullscreen playback (centers movie, and paints black bands around it). Not supported by all video output drivers.</dd>
<dt><code>-fsmode-dontuse &lt;0-31&gt; (OBSOLETE, use the -fs option)</code></dt>
<dd> Try this option if you still experience fullscreen problems.</dd>
<dt><code>-fstype &lt;type1,type2,&#8230;&gt; (X11 only)</code></dt>
<dd> Specify a priority list of fullscreen modes to be used. You can negate the modes by prefixing them with &#8216;-&#8216;. If you experience problems like the fullscreen window being covered by other windows try using a different order.<br />
 <i>NOTE:</i> See -fstype help for a full list of available modes. </dd>
<p> The available types are: </p>
<dl>
<dl>
<dt>above</dt>
<dd> Use the _NETWM_STATE_ABOVE hint if available.</dd>
<dt>below</dt>
<dd> Use the _NETWM_STATE_BELOW hint if available.</dd>
<dt>fullscreen</dt>
<dd> Use the _NETWM_STATE_FULLSCREEN hint if available.</dd>
<dt>layer</dt>
<dd> Use the _WIN_LAYER hint with the default layer.</dd>
<dt>layer=&lt;0&#8230;15&gt;</dt>
<dd> Use the _WIN_LAYER hint with the given layer number.</dd>
<dt>netwm</dt>
<dd> Force NETWM style.</dd>
<dt>none&nbsp;</dt>
<dd> Clear the list of modes; you can add modes to enable afterward.</dd>
<dt>stays_on_top</dt>
<dd> Use _NETWM_STATE_STAYS_ON_TOP hint if available.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>layer,stays_on_top,above,fullscreen</dt>
<dd> Default order, will be used as a fallback if incorrect or unsupported modes are specified.</dd>
<dt>-fullscreen</dt>
<dd> Fixes fullscreen switching on OpenBox 1.x.</dd></dl>
</dl>
<dt><code>-fs-border-left &lt;pixels&gt;</code></dt>
<dd>
</dd><dt><code>-fs-border-right &lt;pixels&gt;</code></dt>
<dd>
</dd><dt><code>-fs-border-top &lt;pixels&gt;</code></dt>
<dd>
</dd><dt><code>-fs-border-bottom &lt;pixels&gt;</code></dt>
<dd> Specify extra borders in full screen mode. The borders apply to all displayed elements: video, OSD and EOSD. The number of pixels is specified in terms of screen resolution. Currently only supported with by the gl video output driver.</dd>
<dt><code>-gamma &lt;-100-100&gt;</code></dt>
<dd> Adjust the gamma of the video signal (default: 0). Not supported by all video output drivers.</dd>
<dt><code>-geometry x[%][:y[%]] or [WxH][+-x+-y]</code></dt>
<dd> Adjust where the output is on the screen initially. The x and y specifications are in pixels measured from the top-left of the screen to the top-left of the image being displayed, however if a percentage sign is given after the argument it turns the value into a percentage of the screen size in that direction. It also supports the standard X11 -geometry option format, in which e.g. +10-50 means &quot;place 10 pixels from the left border and 50 pixels from the lower border&quot; and &quot;&#8211;20+-10&quot; means &quot;place 20 pixels beyond the right and 10 pixels beyond the top border&quot;. If an external window is specified using the -wid option, then the x and y coordinates are relative to the top-left corner of the window rather than the screen. The coordinates are relative to the screen given with -screen for the video output drivers that fully support -screen (direct3d, gl, gl_tiled, vdpau, x11, xv, xvmc, corevideo).<br />
 <i>NOTE:</i> This option is only supported by the x11, xmga, xv, xvmc, xvidix, gl, gl_tiled, direct3d, directx, fbdev, sdl, dfxfb and corevideo video output drivers. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>50:40</dt>
<dd> Places the window at x=50, y=40.</dd>
<dt>50%:50%</dt>
<dd> Places the window in the middle of the screen.</dd>
<dt>100%&nbsp;</dt>
<dd> Places the window at the middle of the right edge of the screen.</dd>
<dt>100%:100%</dt>
<dd> Places the window at the bottom right corner of the screen.</dd></dl>
</dl>
<dt><code>-gui-wid &lt;window ID&gt; (also see -wid) (GUI only)</code></dt>
<dd> This tells the GUI to also use an X11 window and stick itself to the bottom of the video, which is useful to embed a mini-GUI in a browser (with the MPlayer plugin for instance).</dd>
<dt><code>-hue &lt;-100-100&gt;</code></dt>
<dd> Adjust the hue of the video signal (default: 0). You can get a colored negative of the image with this option. Not supported by all video output drivers.</dd>
<dt><code>-monitor-dotclock &lt;range[,range,&#8230;]&gt; (-vo fbdev and vesa only)</code></dt>
<dd> Specify the dotclock or pixelclock range of the monitor.</dd>
<dt><code>-monitor-hfreq &lt;range[,range,&#8230;]&gt; (-vo fbdev and vesa only)</code></dt>
<dd> Specify the horizontal frequency range of the monitor.</dd>
<dt><code>-monitor-vfreq &lt;range[,range,&#8230;]&gt; (-vo fbdev and vesa only)</code></dt>
<dd> Specify the vertical frequency range of the monitor.</dd>
<dt><code>-monitoraspect &lt;ratio&gt; (also see -aspect)</code></dt>
<dd> Set the aspect ratio of your monitor or TV screen. A value of 0 disables a previous setting (e.g. in the config file). Overrides the -monitorpixelaspect setting if enabled. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -monitoraspect 4:3 or 1.3333<br />
 -monitoraspect 16:9 or 1.7777</dd></dl>
<dt><code>-monitorpixelaspect &lt;ratio&gt; (also see -aspect)</code></dt>
<dd> Set the aspect of a single pixel of your monitor or TV screen (default: 1). A value of 1 means square pixels (correct for (almost?) all LCDs).</dd>
<dt><code>-name (X11 only)</code></dt>
<dd> Set the window class name.</dd>
<dt><code>-nodouble</code></dt>
<dd> Disables double buffering, mostly for debugging purposes. Double buffering fixes flicker by storing two frames in memory, and displaying one while decoding another. It can affect OSD negatively, but often removes OSD flickering.</dd>
<dt><code>-nograbpointer</code></dt>
<dd> Do not grab the mouse pointer after a video mode change (-vm). Useful for multihead setups.</dd>
<dt><code>-nokeepaspect</code></dt>
<dd> Do not keep window aspect ratio when resizing windows. Only works with the x11, xv, xmga, xvidix, directx video output drivers. Furthermore under X11 your window manager has to honor window aspect hints.</dd>
<dt><code>-ontop&nbsp;</code></dt>
<dd> Makes the player window stay on top of other windows. Supported by video output drivers which use X11, except SDL, as well as directx, corevideo, quartz, ggi and gl_tiled.</dd>
<dt><code>-panscan &lt;0.0-1.0&gt;</code></dt>
<dd> Enables pan-and-scan functionality (cropping the sides of e.g. a 16:9 movie to make it fit a 4:3 display without black bands). The range controls how much of the image is cropped. Only works with the directx, xv, xmga, mga, gl, gl_tiled, quartz, corevideo and xvidix video output drivers.<br />
 <i>NOTE:</i> Values between -1 and 0 are allowed as well, but highly experimental and may crash or worse. Use at your own risk!</dd>
<dt><code>-panscanrange &lt;-19.0-99.0&gt; (experimental)</code></dt>
<dd> Change the range of the pan-and-scan functionality (default: 1). Positive values mean multiples of the default range. Negative numbers mean you can zoom in up to a factor of -panscanrange+1. E.g. -panscanrange -3 allows a zoom factor of up to 4. This feature is experimental.</dd>
<dt><code>-border-pos-x &lt;0.0-1.0&gt; (-vo gl,xv,xvmc,vdpau,direct3d only, default 0.5)</code></dt>
<dd> When black borders are added to adjust for aspect, this determines where they are placed. 0.0 places borders on the right, 1.0 on the left. Values outside the range 0.0 &#8211; 1.0 will add extra black borders on one side and remove part of the image on the other side.</dd>
<dt><code>-border-pos-y &lt;0.0-1.0&gt; (-vo gl,xv,xvmc,vdpau,direct3d only, default 0.5)</code></dt>
<dd> As -border-pos-x but for top/bottom borders. 0.0 places borders on the bottom, 1.0 on the top.</dd>
<dt><code>-monitor-orientation &lt;0-3&gt; (experimental)</code></dt>
<dd> Rotate display by 90, 180 or 270 degrees. Rotates also the OSD, not just the video image itself. Currently only supported by the gl video output driver. For all other video outputs -vf ass,expand=osd=1,rotate=n can be used, in the future this might even happen automatically.</dd>
<dt><code>-refreshrate &lt;Hz&gt;</code></dt>
<dd> Set the monitor refreshrate in Hz. Currently only supported by -vo directx combined with the -vm option.</dd>
<dt><code>-rootwin</code></dt>
<dd> Play movie in the root window (desktop background). Desktop background images may cover the movie window, though. Only works with the x11, xv, xmga, xvidix, quartz, corevideo and directx video output drivers.</dd>
<dt><code>-saturation &lt;-100-100&gt;</code></dt>
<dd> Adjust the saturation of the video signal (default: 0). You can get grayscale output with this option. Not supported by all video output drivers.</dd>
<dt><code>-screenh &lt;pixels&gt;</code></dt>
<dd> Specify the screen height for video output drivers which do not know the screen resolution like fbdev, x11 and TV-out.</dd>
<dt><code>-screenw &lt;pixels&gt;</code></dt>
<dd> Specify the screen width for video output drivers which do not know the screen resolution like fbdev, x11 and TV-out.</dd>
<dt><code>-(no)stop-xscreensaver (X11 only)</code></dt>
<dd> Turns off xscreensaver at startup and turns it on again on exit (default: enabled). If your screensaver supports neither the XSS nor XResetScreenSaver API please use -heartbeat-cmd instead.</dd>
<dt><code>-title (also see -use-filename-title)</code></dt>
<dd> Set the window title. Supported by X11-based video output drivers.</dd>
<dt><code>-use-filename-title (also see -title)</code></dt>
<dd> Set the window title using the media filename, when not set with -title. Supported by X11-based video output drivers.</dd>
<dt><code>-vm &nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Try to change to a different video mode. Supported by the dga, x11, xv, sdl and directx video output drivers. If used with the directx video output driver the -screenw, -screenh, -bpp and -refreshrate options can be used to set the new display mode.</dd>
<dt><code>-vsync &nbsp;<wbr>&nbsp;</code></dt>
<dd> Enables VBI for the vesa, dfbmga and svga video output drivers.</dd>
<dt><code>-wid &lt;window ID&gt; (also see -gui-wid) (X11, OpenGL and DirectX only)</code></dt>
<dd> This tells MPlayer to attach to an existing window. Useful to embed MPlayer in a browser (e.g. the plugger extension). This option fills the given window completely, thus aspect scaling, panscan, etc are no longer handled by MPlayer but must be managed by the application that created the window.</dd>
<dt><code>-screen &lt;-2-&#8230;&gt; (alias for -xineramascreen)</code></dt>
<dd> In Xinerama configurations (i.e. a single desktop that spans across multiple displays) this option tells MPlayer which screen to display the movie on. A value of -2 means fullscreen across the whole virtual display (in this case Xinerama information is completely ignored), -1 means fullscreen on the display the window currently is on. The initial position set via the -geometry option is relative to the specified screen. Will usually only work with &quot;-fstype -fullscreen&quot; or &quot;-fstype none&quot;. This option is not suitable to only set the startup screen (because it will always display on the given screen in fullscreen mode), -geometry is the best that is available for that purpose currently. Supported by at least the direct3d, gl, gl_tiled, x11, xv and corevideo video output drivers.</dd>
<dt><code>-zrbw (-vo zr only)</code></dt>
<dd> Display in black and white. For optimal performance, this can be combined with &#8216;-lavdopts gray&#8217;.</dd>
<dt><code>-zrcrop &lt;[width]x[height]+[x offset]+[y offset]&gt; (-vo zr only)</code></dt>
<dd> Select a part of the input image to display, multiple occurrences of this option switch on cinerama mode. In cinerama mode the movie is distributed over more than one TV (or beamer) to create a larger image. Options appearing after the n-th -zrcrop apply to the n-th MJPEG card, each card should at least have a -zrdev in addition to the -zrcrop. For examples, see the output of -zrhelp and the Zr section of the documentation.</dd>
<dt><code>-zrdev &lt;device&gt; (-vo zr only)</code></dt>
<dd> Specify the device special file that belongs to your MJPEG card, by default the zr video output driver takes the first v4l device it can find.</dd>
<dt><code>-zrfd (-vo zr only)</code></dt>
<dd> Force decimation: Decimation, as specified by -zrhdec and -zrvdec, only happens if the hardware scaler can stretch the image to its original size. Use this option to force decimation.</dd>
<dt><code>-zrhdec &lt;1|2|4&gt; (-vo zr only)</code></dt>
<dd> Horizontal decimation: Ask the driver to send only every 2nd or 4th line/pixel of the input image to the MJPEG card and use the scaler of the MJPEG card to stretch the image to its original size.</dd>
<dt><code>-zrhelp (-vo zr only)</code></dt>
<dd> Display a list of all -zr* options, their default values and a cinerama mode example.</dd>
<dt><code>-zrnorm &lt;norm&gt; (-vo zr only)</code></dt>
<dd> Specify the TV norm as PAL or NTSC (default: no change).</dd>
<dt><code>-zrquality &lt;1-20&gt; (-vo zr only)</code></dt>
<dd> A number from 1 (best) to 20 (worst) representing the JPEG encoding quality.</dd>
<dt><code>-zrvdec &lt;1|2|4&gt; (-vo zr only)</code></dt>
<dd> Vertical decimation: Ask the driver to send only every 2nd or 4th line/pixel of the input image to the MJPEG card and use the scaler of the MJPEG card to stretch the image to its original size.</dd>
<dt><code>-zrxdoff &lt;x display offset&gt; (-vo zr only)</code></dt>
<dd> If the movie is smaller than the TV screen, this option specifies the x offset from the upper-left corner of the TV screen (default: centered).</dd>
<dt><code>-zrydoff &lt;y display offset&gt; (-vo zr only)</code></dt>
<dd> If the movie is smaller than the TV screen, this option specifies the y offset from the upper-left corner of the TV screen (default: centered).</dd></dl>
<h2>VIDEO OUTPUT DRIVERS (MPLAYER ONLY)</h2>
<p> Video output drivers are interfaces to different video output facilities. The syntax is:</p>
<dl>
<dt><code>-vo &lt;driver1[:suboption1[=value]:&#8230;],driver2,&#8230;[,]&gt;</code></dt>
<dd> Specify a priority list of video output drivers to be used.</dd></dl>
<p> If the list has a trailing &#8216;,&#8217; MPlayer will fall back on drivers not contained in the list. Suboptions are optional and can mostly be omitted.<br />
 <i>NOTE:</i> See -vo help for a list of compiled-in video output drivers. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-vo xmga,xv,</dt>
<dd> Try the Matrox X11 driver, then the Xv driver, then others.</dd>
<dt>-vo directx:noaccel</dt>
<dd> Uses the DirectX driver with acceleration features turned off.</dd></dl>
</dl>
<p> Available video output drivers are:</p>
<dl>
<dt><code>xv (X11 only)</code></dt>
<dd> Uses the XVideo extension of XFree86 4.x to enable hardware accelerated playback. If you cannot use a hardware specific driver, this is probably the best option. For information about what colorkey is used and how it is drawn run MPlayer with -v option and look out for the lines tagged with [xv common] at the beginning.</dd>
<dl>
<dl>
<dt>adaptor=&lt;number&gt;</dt>
<dd> Select a specific XVideo adaptor (check xvinfo results).</dd>
<dt>port=&lt;number&gt;</dt>
<dd> Select a specific XVideo port.</dd>
<dt>ck=&lt;cur|use|set&gt;</dt>
<dd> Select the source from which the colorkey is taken (default: cur).</dd>
<dl>
<dl>
<dt>cur</dt>
<dd> The default takes the colorkey currently set in Xv.</dd>
<dt>use</dt>
<dd> Use but do not set the colorkey from MPlayer (use -colorkey option to change it).</dd>
<dt>set</dt>
<dd> Same as use but also sets the supplied colorkey.</dd></dl>
</dl>
<dt>ck-method=&lt;man|bg|auto&gt;</dt>
<dd> Sets the colorkey drawing method (default: man).</dd>
<dl>
<dl>
<dt>man</dt>
<dd> Draw the colorkey manually (reduces flicker in some cases).</dd>
<dt>bg</dt>
<dd> Set the colorkey as window background.</dd>
<dt>auto</dt>
<dd> Let Xv draw the colorkey.</dd></dl>
</dl>
</dl>
</dl>
<dt><code>x11 (X11 only)</code></dt>
<dd> Shared memory video output driver without hardware acceleration that works whenever X11 is present.</dd>
<dt><code>xover (X11 only)</code></dt>
<dd> Adds X11 support to all overlay based video output drivers. Currently only supported by tdfx_vid.</dd>
<dl>
<dl>
<dt>&lt;vo_driver&gt;</dt>
<dd> Select the driver to use as source to overlay on top of X11.</dd></dl>
</dl>
<dt><code>vdpau (with -vc ffmpeg12vdpau, ffwmv3vdpau, ffvc1vdpau, ffh264vdpau or ffodivxvdpau)</code></dt>
<dd> Video output that uses VDPAU to decode video via hardware. Also supports displaying of software-decoded video.</dd>
<dl>
<dl>
<dt>sharpen=&lt;-1-1&gt;</dt>
<dd> For positive values, apply a sharpening algorithm to the video, for negative values a blurring algorithm (default: 0).</dd>
<dt>denoise=&lt;0-1&gt;</dt>
<dd> Apply a noise reduction algorithm to the video (default: 0, no noise reduction).</dd>
<dt>deint=&lt;0-4&gt;</dt>
<dd> Select the deinterlacer (default: 0). All modes &gt; 0 respect -field-dominance.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> no deinterlacing</dd>
<dt>1</dt>
<dd> Show only first field, similar to -vf field.</dd>
<dt>2</dt>
<dd> Bob deinterlacing, similar to -vf tfields=1.</dd>
<dt>3</dt>
<dd> motion adaptive temporal deinterlacing May lead to A/V desync with slow video hardware and/or high resolution. This is the default if &quot;D&quot; is used to enable deinterlacing.</dd>
<dt>4</dt>
<dd> motion adaptive temporal deinterlacing with edge-guided spatial interpolation Needs fast video hardware.</dd></dl>
</dl>
<dt>chroma-deint</dt>
<dd> Makes temporal deinterlacers operate both on luma and chroma (default). Use nochroma-deint to solely use luma and speed up advanced deinterlacing. Useful with slow video memory.</dd>
<dt>pullup</dt>
<dd> Try to skip deinterlacing for progressive frames, useful for watching telecined content, needs fast video hardware for high resolutions. Only works with motion adaptive temporal deinterlacing.</dd>
<dt>colorspace</dt>
<dd> Select the color space for YUV to RGB conversion. In general BT.601 should be used for standard definition (SD) content and BT.709 for high definition (HD) content. Using incorrect color space results in slightly under or over saturated and shifted colors.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Guess the color space based on video resolution. Video with width &gt;= 1280 or height &gt; 576 is assumed to be HD and BT.709 color space will be used.</dd>
<dt>1</dt>
<dd> Use ITU-R BT.601 color space (default).</dd>
<dt>2</dt>
<dd> Use ITU-R BT.709 color space.</dd>
<dt>3</dt>
<dd> Use SMPTE-240M color space.</dd></dl>
</dl>
<dt>hqscaling</dt>
<dd>
</dd><dl>
<dl>
<dt>0</dt>
<dd> Use default VDPAU scaling (default).</dd>
<dt>1-9</dt>
<dd> Apply high quality VDPAU scaling (needs capable hardware).</dd></dl>
</dl>
<dt>force-mixer</dt>
<dd> Forces the use of the VDPAU mixer, which implements all above options (default). Use noforce-mixer to allow displaying BGRA colorspace. (Disables all above options and the hardware equalizer if image format BGRA is actually used.)</dd></dl>
</dl>
<dt><code>xvmc (X11 with FFmpeg MPEG-1/2 decoder only)</code></dt>
<dd> Video output driver that uses the XvMC (X Video Motion Compensation) extension of XFree86 4.x to speed up MPEG-1/2 and VCR2 decoding.</dd>
<dl>
<dl>
<dt>adaptor=&lt;number&gt;</dt>
<dd> Select a specific XVideo adaptor (check xvinfo results).</dd>
<dt>port=&lt;number&gt;</dt>
<dd> Select a specific XVideo port.</dd>
<dt>(no)benchmark</dt>
<dd> Disables image display. Necessary for proper benchmarking of drivers that change image buffers on monitor retrace only (nVidia). Default is not to disable image display (nobenchmark).</dd>
<dt>(no)bobdeint</dt>
<dd> Very simple deinterlacer. Might not look better than -vf tfields=1, but it is the only deinterlacer for xvmc (default: nobobdeint).</dd>
<dt>(no)queue</dt>
<dd> Queue frames for display to allow more parallel work of the video hardware. May add a small (not noticeable) constant A/V desync (default: noqueue).</dd>
<dt>(no)sleep</dt>
<dd> Use sleep function while waiting for rendering to finish (not recommended on Linux) (default: nosleep).</dd>
<dt>ck=cur|use|set</dt>
<dd> Same as -vo xv:ck (see -vo xv).</dd>
<dt>ck-method=man|bg|auto</dt>
<dd> Same as -vo xv:ck-method (see -vo xv).</dd></dl>
</dl>
<dt><code>dga (X11 only)</code></dt>
<dd> Play video through the XFree86 Direct Graphics Access extension. Considered obsolete.</dd>
<dt><code>sdl (SDL only, buggy/outdated)</code></dt>
<dd> Highly platform independent SDL (Simple Directmedia Layer) library video output driver. Since SDL uses its own X11 layer, MPlayer X11 options do not have any effect on SDL. Note that it has several minor bugs (-vm/-novm is mostly ignored, -fs behaves like -novm should, window is in top-left corner when returning from fullscreen, panscan is not supported, &#8230;).</dd>
<dl>
<dl>
<dt>driver=&lt;driver&gt;</dt>
<dd> Explicitly choose the SDL driver to use.</dd>
<dt>(no)forcexv</dt>
<dd> Use XVideo through the sdl video output driver (default: forcexv).</dd>
<dt>(no)hwaccel</dt>
<dd> Use hardware accelerated scaler (default: hwaccel).</dd></dl>
</dl>
<dt><code>vidix&nbsp;<wbr>&nbsp;</code></dt>
<dd> VIDIX (VIDeo Interface for *niX) is an interface to the video acceleration features of different graphics cards. Very fast video output driver on cards that support it.</dd>
<dl>
<dl>
<dt>&lt;subdevice&gt;</dt>
<dd> Explicitly choose the VIDIX subdevice driver to use. Available subdevice drivers are cyberblade, ivtv, mach64, mga_crtc2, mga, nvidia, pm2, pm3, radeon, rage128, s3, sh_veu, sis_vid and unichrome.</dd></dl>
</dl>
<dt><code>xvidix (X11 only)</code></dt>
<dd> X11 frontend for VIDIX</dd>
<dl>
<dl>
<dt>&lt;subdevice&gt;</dt>
<dd> same as vidix</dd></dl>
</dl>
<dt><code>cvidix&nbsp;</code></dt>
<dd> Generic and platform independent VIDIX frontend, can even run in a text console with nVidia cards.</dd>
<dl>
<dl>
<dt>&lt;subdevice&gt;</dt>
<dd> same as vidix</dd></dl>
</dl>
<dt><code>winvidix (Windows only)</code></dt>
<dd> Windows frontend for VIDIX</dd>
<dl>
<dl>
<dt>&lt;subdevice&gt;</dt>
<dd> same as vidix</dd></dl>
</dl>
<dt><code>direct3d (Windows only) (BETA CODE!)</code></dt>
<dd> Video output driver that uses the Direct3D interface (useful for Vista).</dd>
<dt><code>directx (Windows only)</code></dt>
<dd> Video output driver that uses the DirectX interface.</dd>
<dl>
<dl>
<dt>noaccel</dt>
<dd> Turns off hardware acceleration. Try this option if you have display problems.</dd></dl>
</dl>
<dt><code>kva (OS/2 only)</code></dt>
<dd> Video output driver that uses the libkva interface.</dd>
<dl>
<dl>
<dt>snap</dt>
<dd> Force SNAP mode.</dd>
<dt>wo</dt>
<dd> Force WarpOverlay! mode.</dd>
<dt>dive</dt>
<dd> Force DIVE mode.</dd>
<dt>(no)t23</dt>
<dd> Enable or disable workaround for T23 laptop (default: disabled). Try to enable this option if your video card supports upscaling only.</dd></dl>
</dl>
<dt><code>quartz (Mac OS X only)</code></dt>
<dd> Mac OS X Quartz video output driver. Under some circumstances, it might be more efficient to force a packed YUV output format, with e.g. -vf format=yuy2.</dd>
<dl>
<dl>
<dt>device_id=&lt;number&gt;</dt>
<dd> Choose the display device to use in fullscreen.</dd>
<dt>fs_res=&lt;width&gt;:&lt;height&gt;</dt>
<dd> Specify the fullscreen resolution (useful on slow systems).</dd></dl>
</dl>
<dt><code>corevideo (Mac OS X 10.4 or 10.3.9 with QuickTime 7)</code></dt>
<dd> Mac OS X CoreVideo video output driver</dd>
<dl>
<dl>
<dt>device_id=&lt;number&gt;</dt>
<dd> DEPRECATED, use -screen instead. Choose the display device to use for fullscreen or set it to -1 to always use the same screen the video window is on (default: -1 &#8211; auto).</dd>
<dt>shared_buffer</dt>
<dd> Write output to a shared memory buffer instead of displaying it and try to open an existing NSConnection for communication with a GUI.</dd>
<dt>buffer_name=&lt;name&gt;</dt>
<dd> Name of the shared buffer created with shm_open as well as the name of the NSConnection MPlayer will try to open (default: &quot;mplayerosx&quot;). Setting buffer_name implicitly enables shared_buffer.</dd></dl>
</dl>
<dt><code>fbdev (Linux only)</code></dt>
<dd> Uses the kernel framebuffer to play video.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the fbdev device name to use (e.g. /dev/fb0) or the name of the VIDIX subdevice if the device name starts with &#8216;vidix&#8217; (e.g. &#8216;vidixsis_vid&#8217; for the sis driver).</dd></dl>
</dl>
<dt><code>fbdev2 (Linux only)</code></dt>
<dd> Uses the kernel framebuffer to play video, alternative implementation.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the fbdev device name to use (default: /dev/fb0).</dd></dl>
</dl>
<dt><code>vesa&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Very general video output driver that should work on any VESA VBE 2.0 compatible card.</dd>
<dl>
<dl>
<dt>(no)dga</dt>
<dd> Turns DGA mode on or off (default: on).</dd>
<dt>neotv_pal</dt>
<dd> Activate the NeoMagic TV out and set it to PAL norm.</dd>
<dt>neotv_ntsc</dt>
<dd> Activate the NeoMagic TV out and set it to NTSC norm.</dd>
<dt>vidix</dt>
<dd> Use the VIDIX driver.</dd>
<dt>lvo:&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Activate the Linux Video Overlay on top of VESA mode.</dd></dl>
</dl>
<dt><code>svga&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Play video using the SVGA library.</dd>
<dl>
<dl>
<dt>&lt;video mode&gt;</dt>
<dd> Specify video mode to use. The mode can be given in a &lt;width&gt;x&lt;height&gt;x&lt;colors&gt; format, e.g. 640x480x16M or be a graphics mode number, e.g. 84.</dd>
<dt>bbosd</dt>
<dd> Draw OSD into black bands below the movie (slower).</dd>
<dt>native</dt>
<dd> Use only native drawing functions. This avoids direct rendering, OSD and hardware acceleration.</dd>
<dt>retrace</dt>
<dd> Force frame switch on vertical retrace. Usable only with -double. It has the same effect as the -vsync option.</dd>
<dt>sq&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Try to select a video mode with square pixels.</dd>
<dt>vidix</dt>
<dd> Use svga with VIDIX.</dd></dl>
</dl>
<dt><code>gl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> OpenGL video output driver, simple version. Video size must be smaller than the maximum texture size of your OpenGL implementation. Intended to work even with the most basic OpenGL implementations, but also makes use of newer extensions, which allow support for more colorspaces and direct rendering. For optimal speed try adding the options<br />
 -dr -noslices<br />
 The code performs very few checks, so if a feature does not work, this might be because it is not supported by your card/OpenGL implementation even if you do not get any error message. Use glxinfo or a similar tool to display the supported OpenGL extensions.</dd>
<dl>
<dl>
<dt>backend=&lt;n&gt;</dt>
<dd> Select the backend/OpenGL implementation to use (default: -1).</dd>
<dl>
<dt>
</dt><dd> -1: Autoselect<br />
 0: Win32/WGL<br />
 1: X11/GLX<br />
 2: SDL<br />
 3: X11/EGL (highly experimental)<br />
 4: OSX/Cocoa<br />
 5: Android (very bad hack, only for testing)</dd></dl>
<dt>(no)ati-hack</dt>
<dd> ATI drivers may give a corrupted image when PBOs are used (when using -dr or force-pbo). This option fixes this, at the expense of using a bit more memory.</dd>
<dt>(no)force-pbo</dt>
<dd> Always uses PBOs to transfer textures even if this involves an extra copy. Currently this gives a little extra speed with NVidia drivers and a lot more speed with ATI drivers. May need -noslices and the ati-hack suboption to work correctly.</dd>
<dt>(no)scaled-osd</dt>
<dd> Changes the way the OSD behaves when the size of the window changes (default: disabled). When enabled behaves more like the other video output drivers, which is better for fixed-size fonts. Disabled looks much better with FreeType fonts and uses the borders in fullscreen mode. Does not work correctly with ass subtitles (see -ass), you can instead render them without OpenGL support via -vf ass.</dd>
<dt>osdcolor=&lt;0xAARRGGBB&gt;</dt>
<dd> Color for OSD (default: 0x00ffffff, corresponds to non-transparent white).</dd>
<dt>rectangle=&lt;0,1,2&gt;</dt>
<dd> Select usage of rectangular textures which saves video RAM, but often is slower (default: 0).</dd>
<dl>
<dt>
</dt><dd> 0: Use power-of-two textures (default).<br />
 1: Use the GL_ARB_texture_rectangle extension.<br />
 2: Use the GL_ARB_texture_non_power_of_two extension. In some cases only supported in software and thus very slow.</dd></dl>
<dt>swapinterval=&lt;n&gt;</dt>
<dd> Minimum interval between two buffer swaps, counted in displayed frames (default: 1). 1 is equivalent to enabling VSYNC, 0 to disabling VSYNC. Values below 0 will leave it at the system default. This limits the framerate to (horizontal refresh rate / n). Requires GLX_SGI_swap_control support to work. With some (most/all?) implementations this only works in fullscreen mode.</dd>
<dt>ycbcr</dt>
<dd> Use the GL_APPLE_ycbcr_422 extension to convert YUV to RGB. Default is disabled if yuv= is specified, auto-detected otherwise. Note that this will enable a few special settings to get into a special driver fast-path.</dd>
<dt>yuv=&lt;n&gt;</dt>
<dd> Select the type of YUV to RGB conversion. The default is auto-detection deciding between values 0 and 2.</dd>
<dl>
<dt>
</dt><dd> 0: Use software conversion. Compatible with all OpenGL versions. Provides brightness, contrast and saturation control.<br />
 1: Use register combiners. This uses an nVidia-specific extension (GL_NV_register_combiners). At least three texture units are needed. Provides saturation and hue control. This method is fast but inexact.<br />
 2: Use a fragment program using the POW instruction. Needs the GL_ARB_fragment_program extension and at least three texture units. Provides brightness, contrast, saturation, hue and gamma control. Gamma can also be set independently for red, green and blue. Method 4 is usually faster.<br />
 3: Same as 2. They exist as distinct values for legacy reasons, MPlayer now inserts the extra instructions for gamma control on-demand.<br />
 4: Use a fragment program with additional lookup. Needs the GL_ARB_fragment_program extension and at least four texture units. Provides brightness, contrast, saturation, hue and gamma control. Gamma can also be set independently for red, green and blue.<br />
 5: Use ATI-specific method (for older cards). This uses an ATI-specific extension (GL_ATI_fragment_shader &#8211; not GL_ARB_fragment_shader!). At least three texture units are needed. Provides saturation and hue control. This method is fast but inexact.<br />
 6: Use a 3D texture to do conversion via lookup. Needs the GL_ARB_fragment_program extension and at least four texture units. Extremely slow (software emulation) on some (all?) ATI cards since it uses a texture with border pixels. Provides brightness, contrast, saturation, hue and gamma control. Gamma can also be set independently for red, green and blue. Speed depends more on GPU memory bandwidth than other methods.</dd></dl>
<dt>colorspace</dt>
<dd> Select the color space for YUV to RGB conversion.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Use the formula used normally by MPlayer (default).</dd>
<dt>1</dt>
<dd> Use ITU-R BT.601 color space.</dd>
<dt>2</dt>
<dd> Use ITU-R BT.709 color space.</dd>
<dt>3</dt>
<dd> Use SMPTE-240M color space.</dd></dl>
</dl>
<dt>levelconv=&lt;n&gt;</dt>
<dd> Select the brightness level conversion to use for the YUV to RGB conversion</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Convert TV to PC levels (default).</dd>
<dt>1</dt>
<dd> Convert PC to TV levels.</dd>
<dt>2</dt>
<dd> Do not do any conversion.</dd></dl>
</dl>
<dt>lscale=&lt;n&gt;</dt>
<dd> Select the scaling function to use for luminance scaling. Only valid for yuv modes 2, 3, 4 and 6.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Use simple linear filtering (default).</dd>
<dt>1</dt>
<dd> Use bicubic B-spline filtering (better quality). Needs one additional texture unit. Older cards will not be able to handle this for chroma at least in fullscreen mode.</dd>
<dt>2</dt>
<dd> Use cubic filtering in horizontal, linear filtering in vertical direction. Works on a few more cards than method 1.</dd>
<dt>3</dt>
<dd> Same as 1 but does not use a lookup texture. Might be faster on some cards.</dd>
<dt>4</dt>
<dd> Use experimental unsharp masking with 3&#215;3 support and a default strength of 0.5 (see filter-strength).</dd>
<dt>5</dt>
<dd> Use experimental unsharp masking with 5&#215;5 support and a default strength of 0.5 (see filter-strength).</dd>
<dt>64</dt>
<dd> Use nearest-neighbor scaling.</dd></dl>
</dl>
<dt>cscale=&lt;n&gt;</dt>
<dd> Select the scaling function to use for chrominance scaling. For details see lscale.</dd>
<dt>filter-strength=&lt;value&gt;</dt>
<dd> Set the effect strength for the lscale/cscale filters that support it.</dd>
<dt>noise-strength=&lt;value&gt;</dt>
<dd> Set how much noise to add. 0 to disable (default), 1.0 for level suitable for dithering to 6 bit.</dd>
<dt>stereo=&lt;value&gt;</dt>
<dd> Select a method for stereo display. You may have to use -aspect to fix the aspect value. Add 32 to swap left and right side. Experimental, do not expect too much from it.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> normal 2D display</dd>
<dt>1</dt>
<dd> Convert side by side input to full-color red-cyan stereo.</dd>
<dt>2</dt>
<dd> Convert side by side input to full-color green-magenta stereo.</dd>
<dt>3</dt>
<dd> Convert side by side input to quadbuffered stereo. Only supported by very few OpenGL cards.</dd>
<dt>4</dt>
<dd> Mix left and right in a pixel pattern. Pattern is given by stipple option.</dd></dl>
</dl>
<dt>stipple=&lt;bit</dt>
<dd> Lowest 16 bit give the 4&#215;4 pattern to use (default: 0x0f0f). Examples to try: 0x0f0f, 0xf0f0: horizontal lines; 0xaaaa, 0x5555: vertical lines; 0xa5a5, 0x5a5a: checkerboard pattern</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> The following options are only useful if writing your own fragment programs.</dd></dl>
<dl>
<dl>
<dt>customprog=&lt;filename&gt;</dt>
<dd> Load a custom fragment program from &lt;filename&gt;. See TOOLS/edgedect.fp for an example.</dd>
<dt>customtex=&lt;filename&gt;</dt>
<dd> Load a custom &quot;gamma ramp&quot; texture from &lt;filename&gt;. This can be used in combination with yuv=4 or with the customprog option.</dd>
<dt>(no)customtlin</dt>
<dd> If enabled (default) use GL_LINEAR interpolation, otherwise use GL_NEAREST for customtex texture.</dd>
<dt>(no)customtrect</dt>
<dd> If enabled, use texture_rectangle for customtex texture. Default is disabled.</dd>
<dt>(no)mipmapgen</dt>
<dd> If enabled, mipmaps for the video are automatically generated. This should be useful together with the customprog and the TXB instruction to implement blur filters with a large radius. For most OpenGL implementations this is very slow for any non-RGB formats. Default is disabled.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Normally there is no reason to use the following options, they mostly exist for testing purposes.</dd></dl>
<dl>
<dl>
<dt>(no)glfinish</dt>
<dd> Call glFinish() before swapping buffers. Slower but in some cases more correct output (default: disabled).</dd>
<dt>(no)manyfmts</dt>
<dd> Enables support for more (RGB and BGR) color formats (default: enabled). Needs OpenGL version &gt;= 1.2.</dd>
<dt>slice-height=&lt;0-&#8230;&gt;</dt>
<dd> Number of lines copied to texture in one piece (default: 0). 0 for whole image.<br />
 <i>NOTE:</i> If YUV colorspace is used (see yuv suboption), special rules apply:</dd>
<dl>
<dt>
</dt><dd> If the decoder uses slice rendering (see -noslices), this setting has no effect, the size of the slices as provided by the decoder is used.<br />
 If the decoder does not use slice rendering, the default is 16.</dd></dl>
<dt>(no)osd</dt>
<dd> Enable or disable support for OSD rendering via OpenGL (default: enabled). This option is for testing; to disable the OSD use -osdlevel 0 instead.</dd>
<dt>(no)aspect</dt>
<dd> Enable or disable aspect scaling and pan-and-scan support (default: enabled). Disabling might increase speed.</dd></dl>
</dl>
<dt><code>gl_tiled</code></dt>
<dd> Variant of the OpenGL video output driver. Supports videos larger than the maximum texture size but lacks many of the advanced features and optimizations of the gl driver and is unlikely to be extended further.</dd>
<dl>
<dl>
<dt>(no)glfinish</dt>
<dd> same as gl (default: enabled)</dd>
<dt>yuv=&lt;n&gt;</dt>
<dd> Select the type of YUV to RGB conversion. If set to anything except 0 OSD will be disabled and brightness, contrast and gamma setting is only available via the global X server settings. Apart from this the values have the same meaning as for -vo gl.</dd></dl>
</dl>
<dt><code>matrixview</code></dt>
<dd> OpenGL-based renderer creating a Matrix-like running-text effect.</dd>
<dl>
<dl>
<dt>cols=&lt;n&gt;</dt>
<dd> Number of text columns to display. Very low values (&lt; 16) will probably fail due to scaler limitations. Values not divisible by 16 may cause issues as well.</dd>
<dt>rows=&lt;n&gt;</dt>
<dd> Number of text rows to display. Very low values (&lt; 16) will probably fail due to scaler limitations. Values not divisible by 16 may cause issues as well.</dd></dl>
</dl>
<dt><code>null&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Produces no video output. Useful for benchmarking.</dd>
<dt><code>aa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> ASCII art video output driver that works on a text console.<br />
 <i>NOTE:</i> The driver does not handle -aspect correctly.<br />
 <i>HINT:</i> You probably have to specify -monitorpixelaspect. Try &#8216;mplayer -vo aa -monitorpixelaspect 0.5&#8217;.</dd>
<dt><code>caca&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Color ASCII art video output driver that works on a text console.</dd>
<dt><code>bl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Video playback using the Blinkenlights UDP protocol. This driver is highly hardware specific.</dd>
<dl>
<dl>
<dt>&lt;subdevice&gt;</dt>
<dd> Explicitly choose the Blinkenlights subdevice driver to use. It is something like arcade:host=localhost:2323 or hdl:file=name1,file=name2. You must specify a subdevice.</dd></dl>
</dl>
<dt><code>ggi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> GGI graphics system video output driver</dd>
<dl>
<dl>
<dt>&lt;driver&gt;</dt>
<dd> Explicitly choose the GGI driver to use. Replace any &#8216;,&#8217; that would appear in the driver string by a &#8216;.&#8217;.</dd></dl>
</dl>
<dt><code>directfb</code></dt>
<dd> Play video using the DirectFB library.</dd>
<dl>
<dl>
<dt>(no)input</dt>
<dd> Use the DirectFB instead of the MPlayer keyboard code (default: enabled).</dd>
<dt>buffermode=single|double|triple</dt>
<dd> Double and triple buffering give best results if you want to avoid tearing issues. Triple buffering is more efficient than double buffering as it does not block MPlayer while waiting for the vertical retrace. Single buffering should be avoided (default: single).</dd>
<dt>fieldparity=top|bottom</dt>
<dd> Control the output order for interlaced frames (default: disabled). Valid values are top = top fields first, bottom = bottom fields first. This option does not have any effect on progressive film material like most MPEG movies are. You need to enable this option if you have tearing issues or unsmooth motions watching interlaced film material.</dd>
<dt>layer=N</dt>
<dd> Will force layer with ID N for playback (default: -1 &#8211; auto).</dd>
<dt>dfbopts=&lt;list&gt;</dt>
<dd> Specify a parameter list for DirectFB.</dd></dl>
</dl>
<dt><code>dfbmga&nbsp;</code></dt>
<dd> Matrox G400/G450/G550 specific video output driver that uses the DirectFB library to make use of special hardware features. Enables CRTC2 (second head), displaying video independently of the first head.</dd>
<dl>
<dl>
<dt>(no)input</dt>
<dd> same as directfb (default: disabled)</dd>
<dt>buffermode=single|double|triple</dt>
<dd> same as directfb (default: triple)</dd>
<dt>fieldparity=top|bottom</dt>
<dd> same as directfb</dd>
<dt>(no)bes</dt>
<dd> Enable the use of the Matrox BES (backend scaler) (default: disabled). Gives very good results concerning speed and output quality as interpolated picture processing is done in hardware. Works only on the primary head.</dd>
<dt>(no)spic</dt>
<dd> Make use of the Matrox sub picture layer to display the OSD (default: enabled).</dd>
<dt>(no)crtc2</dt>
<dd> Turn on TV-out on the second head (default: enabled). The output quality is amazing as it is a full interlaced picture with proper sync to every odd/even field.</dd>
<dt>tvnorm=pal|ntsc|auto</dt>
<dd> Will set the TV norm of the Matrox card without the need for modifying /etc/directfbrc (default: disabled). Valid norms are pal = PAL, ntsc = NTSC. Special norm is auto (auto-adjust using PAL/NTSC) because it decides which norm to use by looking at the framerate of the movie.</dd></dl>
</dl>
<dt><code>mga (Linux only)</code></dt>
<dd> Matrox specific video output driver that makes use of the YUV back end scaler on Gxxx cards through a kernel module. If you have a Matrox card, this is the fastest option.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the Matrox device name to use (default: /dev/mga_vid).</dd></dl>
</dl>
<dt><code>xmga (Linux, X11 only)</code></dt>
<dd> The mga video output driver, running in an X11 window.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the Matrox device name to use (default: /dev/mga_vid).</dd></dl>
</dl>
<dt><code>s3fb (Linux only) (also see -dr)</code></dt>
<dd> S3 Virge specific video output driver. This driver supports the card&#8217;s YUV conversion and scaling, double buffering and direct rendering features. Use -vf format=yuy2 to get hardware-accelerated YUY2 rendering, which is much faster than YV12 on this card.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the fbdev device name to use (default: /dev/fb0).</dd></dl>
</dl>
<dt><code>wii (Linux only)</code></dt>
<dd> Nintendo Wii/GameCube specific video output driver.</dd>
<dt><code>3dfx (Linux only)</code></dt>
<dd> 3dfx-specific video output driver that directly uses the hardware on top of X11. Only 16 bpp are supported.</dd>
<dt><code>tdfxfb (Linux only)</code></dt>
<dd> This driver employs the tdfxfb framebuffer driver to play movies with YUV acceleration on 3dfx cards.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the fbdev device name to use (default: /dev/fb0).</dd></dl>
</dl>
<dt><code>tdfx_vid (Linux only)</code></dt>
<dd> 3dfx-specific video output driver that works in combination with the tdfx_vid kernel module.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the device name to use (default: /dev/tdfx_vid).</dd></dl>
</dl>
<dt><code>dxr2 (also see -dxr2) (DXR2 only)</code></dt>
<dd> Creative DXR2 specific video output driver.</dd>
<dl>
<dl>
<dt>&lt;vo_driver&gt;</dt>
<dd> Output video subdriver to use as overlay (x11, xv).</dd></dl>
</dl>
<dt><code>dxr3 (DXR3 only)</code></dt>
<dd> Sigma Designs em8300 MPEG decoder chip (Creative DXR3, Sigma Designs Hollywood Plus) specific video output driver. Also see the lavc video filter.</dd>
<dl>
<dl>
<dt>overlay</dt>
<dd> Activates the overlay instead of TV-out.</dd>
<dt>prebuf</dt>
<dd> Turns on prebuffering.</dd>
<dt>sync&nbsp;</dt>
<dd> Will turn on the new sync-engine.</dd>
<dt>norm=&lt;norm&gt;</dt>
<dd> Specifies the TV norm.</dd>
<dl>
<dt>
</dt><dd> 0: Does not change current norm (default).<br />
 1: Auto-adjust using PAL/NTSC.<br />
 2: Auto-adjust using PAL/PAL-60.<br />
 3: PAL<br />
 4: PAL-60<br />
 5: NTSC</dd></dl>
<dt>&lt;0-3&gt;</dt>
<dd> Specifies the device number to use if you have more than one em8300 card.</dd></dl>
</dl>
<dt><code>ivtv (IVTV only)</code></dt>
<dd> Conexant CX23415 (iCompression iTVC15) or Conexant CX23416 (iCompression iTVC16) MPEG decoder chip (Hauppauge WinTV PVR-150/250/350/500) specific video output driver for TV-out. Also see the lavc video filter.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the MPEG decoder device name to use (default: /dev/video16).</dd>
<dt>&lt;output&gt;</dt>
<dd> Explicitly choose the TV-out output to be used for the video signal.</dd></dl>
</dl>
<dt><code>v4l2 (requires Linux 2.6.22+ kernel)</code></dt>
<dd> Video output driver for V4L2 compliant cards with built-in hardware MPEG decoder. Also see the lavc video filter.</dd>
<dl>
<dl>
<dt>&lt;device&gt;</dt>
<dd> Explicitly choose the MPEG decoder device name to use (default: /dev/video16).</dd>
<dt>&lt;output&gt;</dt>
<dd> Explicitly choose the TV-out output to be used for the video signal.</dd></dl>
</dl>
<dt><code>mpegpes (DVB only)</code></dt>
<dd> Video output driver for DVB cards that writes the output to an MPEG-PES file if no DVB card is installed.</dd>
<dl>
<dl>
<dt>card=&lt;1-4&gt;</dt>
<dd> Specifies the device number to use if you have more than one DVB output card (V3 API only, such as 1.x.y series drivers). If not specified MPlayer will search the first usable card.</dd>
<dt>&lt;filename&gt;</dt>
<dd> output filename (default: ./grab.mpg)</dd></dl>
</dl>
<dt><code>zr (also see -zr* and -zrhelp)</code></dt>
<dd> Video output driver for a number of MJPEG capture/playback cards.</dd>
<dt><code>zr2 (also see the zrmjpeg video filter)</code></dt>
<dd> Video output driver for a number of MJPEG capture/playback cards, second generation.</dd>
<dl>
<dl>
<dt>dev=&lt;device&gt;</dt>
<dd> Specifies the video device to use.</dd>
<dt>norm=&lt;PAL|NTSC|SECAM|auto&gt;</dt>
<dd> Specifies the video norm to use (default: auto).</dd>
<dt>(no)prebuf</dt>
<dd> (De)Activate prebuffering, not yet supported.</dd></dl>
</dl>
<dt><code>md5sum&nbsp;</code></dt>
<dd> Calculate MD5 sums of each frame and write them to a file. Supports RGB24 and YV12 colorspaces. Useful for debugging.</dd>
<dl>
<dl>
<dt>outfile=&lt;value&gt;</dt>
<dd> Specify the output filename (default: ./md5sums).</dd></dl>
</dl>
<dt><code>yuv4mpeg</code></dt>
<dd> Transforms the video stream into a sequence of uncompressed YUV 4:2:0 images and stores it in a file (default: ./stream.yuv). The format is the same as the one employed by mjpegtools, so this is useful if you want to process the video with the mjpegtools suite. It supports the YV12 format. If your source file has a different format and is interlaced, make sure to use -vf scale=::1 to ensure the conversion uses interlaced mode. You can combine it with the -fixed-vo option to concatenate files with the same dimensions and fps value.</dd>
<dl>
<dl>
<dt>interlaced</dt>
<dd> Write the output as interlaced frames, top field first.</dd>
<dt>interlaced_bf</dt>
<dd> Write the output as interlaced frames, bottom field first.</dd>
<dt>file=&lt;filename&gt;</dt>
<dd> Write the output to &lt;filename&gt; instead of the default stream.yuv.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>NOTE:</i> If you do not specify any option the output is progressive (i.e. not interlaced).</dd></dl>
<dt><code>gif89a&nbsp;</code></dt>
<dd> Output each frame into a single animated GIF file in the current directory. It supports only RGB format with 24 bpp and the output is converted to 256 colors.</dd>
<dl>
<dl>
<dt>&lt;fps&gt;</dt>
<dd> Float value to specify framerate (default: 5.0).</dd>
<dt>&lt;output&gt;</dt>
<dd> Specify the output filename (default: ./out.gif).</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>NOTE:</i> You must specify the framerate before the filename or the framerate will be part of the filename. </p>
<p> <i>EXAMPLE:</i></dd></dl>
<dl>
<dt>
</dt><dd> mplayer video.nut -vo gif89a:fps=15:output=test.gif</dd></dl>
<dt><code>jpeg&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Output each frame into a JPEG file in the current directory. Each file takes the frame number padded with leading zeros as name.</dd>
<dl>
<dl>
<dt>[no]progressive</dt>
<dd> Specify standard or progressive JPEG (default: noprogressive).</dd>
<dt>[no]baseline</dt>
<dd> Specify use of baseline or not (default: baseline).</dd>
<dt>optimize=&lt;0-100&gt;</dt>
<dd> optimization factor (default: 100)</dd>
<dt>smooth=&lt;0-100&gt;</dt>
<dd> smooth factor (default: 0)</dd>
<dt>quality=&lt;0-100&gt;</dt>
<dd> quality factor (default: 75)</dd>
<dt>outdir=&lt;dirname&gt;</dt>
<dd> Specify the directory to save the JPEG files to (default: ./).</dd>
<dt>subdirs=&lt;prefix&gt;</dt>
<dd> Create numbered subdirectories with the specified prefix to save the files in instead of the current directory.</dd>
<dt>maxfiles=&lt;value&gt; (subdirs only)</dt>
<dd> Maximum number of files to be saved per subdirectory. Must be equal to or larger than 1 (default: 1000).</dd></dl>
</dl>
<dt><code>pnm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Output each frame into a PNM file in the current directory. Each file takes the frame number padded with leading zeros as name. It supports PPM, PGM and PGMYUV files in both raw and ASCII mode. Also see <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/5-ppm/">ppm</a>(5) and <a href="/docs/linux/man/5-pgm/">pgm</a>(5).</dd>
<dl>
<dl>
<dt>ppm&nbsp;<wbr>&nbsp;</dt>
<dd> Write PPM files (default).</dd>
<dt>pgm&nbsp;<wbr>&nbsp;</dt>
<dd> Write PGM files.</dd>
<dt>pgmyuv</dt>
<dd> Write PGMYUV files. PGMYUV is like PGM, but it also contains the U and V plane, appended at the bottom of the picture.</dd>
<dt>raw&nbsp;<wbr>&nbsp;</dt>
<dd> Write PNM files in raw mode (default).</dd>
<dt>ascii</dt>
<dd> Write PNM files in ASCII mode.</dd>
<dt>outdir=&lt;dirname&gt;</dt>
<dd> Specify the directory to save the PNM files to (default: ./).</dd>
<dt>subdirs=&lt;prefix&gt;</dt>
<dd> Create numbered subdirectories with the specified prefix to save the files in instead of the current directory.</dd>
<dt>maxfiles=&lt;value&gt; (subdirs only)</dt>
<dd> Maximum number of files to be saved per subdirectory. Must be equal to or larger than 1 (default: 1000).</dd></dl>
</dl>
<dt><code>png&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Output each frame into a PNG file in the current directory. Each file takes the frame number padded with leading zeros as name. 24bpp RGB and BGR formats are supported.</dd>
<dl>
<dl>
<dt>z=&lt;0-9&gt;</dt>
<dd> Specifies the compression level. 0 is no compression, 9 is maximum compression.</dd>
<dt>outdir=&lt;dirname&gt;</dt>
<dd> Specify the directory to save the PNG files to (default: ./).</dd>
<dt>prefix=&lt;prefix&gt;</dt>
<dd> Specify the prefix to be used for the PNG filenames (default: no prefix).</dd>
<dt>alpha</dt>
<dd> Create PNG files with an alpha channel. Note that MPlayer in general does not support alpha, so this will only be useful in some rare cases.</dd></dl>
</dl>
<dt><code>mng&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Output video into an animated MNG file using 24 bpp RGB images with lossless compression.</dd>
<dl>
<dl>
<dt>output=&lt;filename&gt;</dt>
<dd> Specify the output filename (default: out.mng).</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>EXAMPLE:</i></dd></dl>
<dl>
<dt>
</dt><dd> mplayer video.mkv -vo mng:output=test.mng</dd></dl>
<dt><code>tga&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Output each frame into a Targa file in the current directory. Each file takes the frame number padded with leading zeros as name. The purpose of this video output driver is to have a simple lossless image writer to use without any external library. It supports the BGR[A] color format, with 15, 24 and 32 bpp. You can force a particular format with the format video filter. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> mplayer video.nut -vf format=bgr15 -vo tga</dd></dl>
</dl>
<h2>DECODING/FILTERING OPTIONS</h2>
<dl>
<dt><code>-ac &lt;[-|+]codec1,[-|+]codec2,&#8230;[,]&gt;</code></dt>
<dd> Specify a priority list of audio codecs to be used, according to their codec name in codecs.conf. Use a &#8216;-&#8216; before the codec name to omit it. Use a &#8216;+&#8217; before the codec name to force it, this will likely crash! If the list has a trailing &#8216;,&#8217; MPlayer will fall back on codecs not contained in the list.<br />
 <i>NOTE:</i> See -ac help for a full list of available codecs. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-ac mp3acm</dt>
<dd> Force the l3codeca.acm MP3 codec.</dd>
<dt>-ac mad,</dt>
<dd> Try libmad first, then fall back on others.</dd>
<dt>-ac hwac3,a52,</dt>
<dd> Try hardware AC-3 passthrough, software AC-3, then others.</dd>
<dt>-ac hwdts,</dt>
<dd> Try hardware DTS passthrough, then fall back on others.</dd>
<dt>-ac -ffmp3,</dt>
<dd> Skip FFmpeg&#8217;s MP3 decoder.</dd></dl>
</dl>
<dt><code>-af-adv &lt;force=(0-7):list=(filters)&gt; (also see -af)</code></dt>
<dd> Specify advanced audio filter options:</dd>
<dl>
<dl>
<dt>force=&lt;0-7&gt;</dt>
<dd> Forces the insertion of audio filters to one of the following:</dd>
<dl>
<dt>
</dt><dd> 0: Use completely automatic filter insertion (currently identical to 1).<br />
 1: Optimize for accuracy (default).<br />
 2: Optimize for speed. <i>Warning:</i> Some features in the audio filters may silently fail, and the sound quality may drop.<br />
 3: Use no automatic insertion of filters and no optimization. <i>Warning:</i> It may be possible to crash MPlayer using this setting.<br />
 4: Use automatic insertion of filters according to 0 above, but use floating point processing when possible.<br />
 5: Use automatic insertion of filters according to 1 above, but use floating point processing when possible.<br />
 6: Use automatic insertion of filters according to 2 above, but use floating point processing when possible.<br />
 7: Use no automatic insertion of filters according to 3 above, and use floating point processing when possible.</dd></dl>
<dt>list=&lt;filters&gt;</dt>
<dd> Same as -af.</dd></dl>
</dl>
<dt><code>-afm &lt;driver1,driver2,&#8230;&gt;</code></dt>
<dd> Specify a priority list of audio codec families to be used, according to their codec name in codecs.conf. Falls back on the default codecs if none of the given codec families work.<br />
 <i>NOTE:</i> See -afm help for a full list of available codec families. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-afm ffmpeg</dt>
<dd> Try FFmpeg&#8217;s libavcodec codecs first.</dd>
<dt>-afm acm,dshow</dt>
<dd> Try Win32 codecs first.</dd></dl>
</dl>
<dt><code>-aspect &lt;ratio&gt; (also see -zoom)</code></dt>
<dd> Override movie aspect ratio, in case aspect information is incorrect or missing in the file being played. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -aspect 4:3 or -aspect 1.3333<br />
 -aspect 16:9 or -aspect 1.7777</dd></dl>
<dt><code>-noaspect</code></dt>
<dd> Disable automatic movie aspect ratio compensation.</dd>
<dt><code>-field-dominance &lt;-1-1&gt;</code></dt>
<dd> Set first field for interlaced content. Useful for deinterlacers that double the framerate: -vf tfields=1, -vf yadif=1, -vo vdpau:deint and -vo xvmc:bobdeint.</dd>
<dl>
<dl>
<dt>-1</dt>
<dd> auto (default): If the decoder does not export the appropriate information, it falls back to 0 (top field first).</dd>
<dt>0</dt>
<dd> top field first</dd>
<dt>1</dt>
<dd> bottom field first</dd></dl>
</dl>
<dt><code>-flip &nbsp;</code></dt>
<dd> Flip image upside-down.</dd>
<dt><code>-lavdopts &lt;option1:option2:&#8230;&gt; (DEBUG CODE)</code></dt>
<dd> Specify libavcodec decoding parameters. Separate multiple options with a colon. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -lavdopts gray:skiploopfilter=all:skipframe=nonref</dd></dl>
<dl>
<dt>
</dt><dd> Available options are:</dd></dl>
<dl>
<dl>
<dt>bitexact</dt>
<dd> Only use bit-exact algorithms in all decoding steps (for codec testing).</dd>
<dt>bug=&lt;value&gt;</dt>
<dd> Manually work around encoder bugs.</dd>
<dl>
<dt>
</dt><dd> 0: nothing<br />
 1: autodetect bugs (default)<br />
 2 (msmpeg4v3): some old lavc generated msmpeg4v3 files (no autodetection)<br />
 4 (mpeg4): Xvid interlacing bug (autodetected if fourcc==XVIX)<br />
 8 (mpeg4): UMP4 (autodetected if fourcc==UMP4)<br />
 16 (mpeg4): padding bug (autodetected)<br />
 32 (mpeg4): illegal vlc bug (autodetected per fourcc)<br />
 64 (mpeg4): Xvid and DivX qpel bug (autodetected per fourcc/version)<br />
 128 (mpeg4): old standard qpel (autodetected per fourcc/version)<br />
 256 (mpeg4): another qpel bug (autodetected per fourcc/version)<br />
 512 (mpeg4): direct-qpel-blocksize bug (autodetected per fourcc/version)<br />
 1024 (mpeg4): edge padding bug (autodetected per fourcc/version)</dd></dl>
<dt>debug=&lt;value&gt;</dt>
<dd> Display debugging information.</dd>
<dl>
<dt>
</dt><dd>
 0: disabled<br />
 1: picture info<br />
 2: rate control<br />
 4: bitstream<br />
 8: macroblock (MB) type<br />
 16: per-block quantization parameter (QP)<br />
 32: motion vector<br />
 0x0040: motion vector visualization (use -noslices)<br />
 0x0080: macroblock (MB) skip<br />
 0x0100: startcode<br />
 0x0200: PTS<br />
 0x0400: error resilience<br />
 0x0800: memory management control operations (H.264)<br />
 0x1000: bugs<br />
 0x2000: Visualize quantization parameter (QP), lower QP are tinted greener.<br />
 0x4000: Visualize block types.</dd></dl>
<dt>ec=&lt;value&gt;</dt>
<dd> Set error concealment strategy.</dd>
<dl>
<dt>
</dt><dd> 1: Use strong deblock filter for damaged MBs.<br />
 2: iterative motion vector (MV) search (slow)<br />
 3: all (default)</dd></dl>
<dt>er=&lt;value&gt;</dt>
<dd> Set error resilience strategy.</dd>
<dl>
<dt>
</dt><dd>
 0: disabled<br />
 1: careful (Should work with broken encoders.)<br />
 2: normal (default) (Works with compliant encoders.)<br />
 3: aggressive (More checks, but might cause problems even for valid bitstreams.)<br />
 4: very aggressive</dd></dl>
<dt>fast (MPEG-2, MPEG-4, and H.264 only)</dt>
<dd> Enable optimizations which do not comply to the specification and might potentially cause problems, like simpler dequantization, simpler motion compensation, assuming use of the default quantization matrix, assuming YUV 4:2:0 and skipping a few checks to detect damaged bitstreams.</dd>
<dt>gray&nbsp;</dt>
<dd> grayscale only decoding (a bit faster than with color)</dd>
<dt>idct=&lt;0-99&gt; (see -lavcopts)</dt>
<dd> For best decoding quality use the same IDCT algorithm for decoding and encoding. This may come at a price in accuracy, though.</dd>
<dt>lowres=&lt;number&gt;[,&lt;w&gt;]</dt>
<dd> Decode at lower resolutions. Low resolution decoding is not supported by all codecs, and it will often result in ugly artifacts. This is not a bug, but a side effect of not decoding at full resolution.</dd>
<dl>
<dt>
</dt><dd>
 0: disabled<br />
 1: 1/2 resolution<br />
 2: 1/4 resolution<br />
 3: 1/8 resolution</dd></dl>
<dl>
<dt>
</dt><dd> If &lt;w&gt; is specified lowres decoding will be used only if the width of the video is major than or equal to &lt;w&gt;.</dd></dl>
<p> <code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code> Pass AVOptions to libavcodec decoder. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some options may conflict with MEncoder options. </p>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>o=debug=pict</dt>
<dd></dd></dl>
</dl>
<dt>sb=&lt;number&gt; (MPEG-2 only)</dt>
<dd> Skip the given number of macroblock rows at the bottom.</dd>
<dt>st=&lt;number&gt; (MPEG-2 only)</dt>
<dd> Skip the given number of macroblock rows at the top.</dd>
<dt>skiploopfilter=&lt;skipvalue&gt; (H.264 only)</dt>
<dd> Skips the loop filter (AKA deblocking) during H.264 decoding. Since the filtered frame is supposed to be used as reference for decoding dependent frames this has a worse effect on quality than not doing deblocking on e.g. MPEG-2 video. But at least for high bitrate HDTV this provides a big speedup with no visible quality loss. </dd>
<p> &lt;skipvalue&gt; can be either one of the following:</p>
<dl>
<dt>
</dt><dd>
 none: Never skip.<br />
 default: Skip useless processing steps (e.g. 0 size packets in AVI).<br />
 nonref: Skip frames that are not referenced (i.e. not used for decoding other frames, the error cannot &quot;build up&quot;).<br />
 bidir: Skip B-Frames.<br />
 nonkey: Skip all frames except keyframes.<br />
 all: Skip all frames.</dd></dl>
<dt>skipidct=&lt;skipvalue&gt; (MPEG-1/2 only)</dt>
<dd> Skips the IDCT step. This degrades quality a lot of in almost all cases (see skiploopfilter for available skip values).</dd>
<dt>skipframe=&lt;skipvalue&gt;</dt>
<dd> Skips decoding of frames completely. Big speedup, but jerky motion and sometimes bad artifacts (see skiploopfilter for available skip values).</dd>
<dt>threads=&lt;1-8&gt; (MPEG-1/2 and H.264 only)</dt>
<dd> number of threads to use for decoding (default: 1)</dd>
<dt>vismv=&lt;value&gt;</dt>
<dd> Visualize motion vectors.</dd>
<dl>
<dt>
</dt><dd>
 0: disabled<br />
 1: Visualize forward predicted MVs of P-frames.<br />
 2: Visualize forward predicted MVs of B-frames.<br />
 4: Visualize backward predicted MVs of B-frames.</dd></dl>
<dt>vstats</dt>
<dd> Prints some statistics and stores them in ./vstats_*.log.</dd>
<dt>wait_keyframe</dt>
<dd> Wait for a keyframe before displaying anything. Avoids broken frames at startup or after seeking with some formats.</dd></dl>
</dl>
<dt><code>-noslices</code></dt>
<dd> Disable drawing video by 16-pixel height slices/bands, instead draws the whole frame in a single run. May be faster or slower, depending on video card and available cache. It has effect only with libmpeg2 and libavcodec codecs.</dd>
<dt><code>-nosound</code></dt>
<dd> Do not play/encode sound. Useful for benchmarking.</dd>
<dt><code>-novideo</code></dt>
<dd> Do not play/encode video. In many cases this will not work, use -vc null -vo null instead.</dd>
<dt><code>-pp &lt;quality&gt; (also see -vf pp)</code></dt>
<dd> Set the DLL postprocess level. This option is no longer usable with -vf pp. It only works with Win32 DirectShow DLLs with internal postprocessing routines. The valid range of -pp values varies by codec, it is mostly 0-6, where 0=disable, 6=slowest/best.</dd>
<dt><code>-pphelp (also see -vf pp)</code></dt>
<dd> Show a summary about the available postprocess filters and their usage.</dd>
<dt><code>-ssf &lt;mode&gt;</code></dt>
<dd> Specifies software scaler parameters. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
</dt><dd> -vf scale -ssf lgb=3.0</dd></dl>
<dl>
<dl>
<dt>lgb=&lt;0-100&gt;</dt>
<dd> gaussian blur filter (luma)</dd>
<dt>cgb=&lt;0-100&gt;</dt>
<dd> gaussian blur filter (chroma)</dd>
<dt>ls=&lt;-100-100&gt;</dt>
<dd> sharpen filter (luma)</dd>
<dt>cs=&lt;-100-100&gt;</dt>
<dd> sharpen filter (chroma)</dd>
<dt>chs=&lt;h&gt;</dt>
<dd> chroma horizontal shifting</dd>
<dt>cvs=&lt;v&gt;</dt>
<dd> chroma vertical shifting</dd></dl>
</dl>
<dt><code>-stereo &lt;mode&gt;</code></dt>
<dd> Select type of MP2/MP3 stereo output.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> stereo</dd>
<dt>1</dt>
<dd> left channel</dd>
<dt>2</dt>
<dd> right channel</dd></dl>
</dl>
<dt><code>-sws &lt;software scaler type&gt; (also see -vf scale and -zoom)</code></dt>
<dd> Specify the software scaler algorithm to be used with the -zoom option. This affects video output drivers which lack hardware acceleration, e.g. x11. </dd>
<p> Available types are: </p>
<dl>
<dl>
<dt>0</dt>
<dd> fast bilinear</dd>
<dt>1</dt>
<dd> bilinear</dd>
<dt>2</dt>
<dd> bicubic (good quality) (default)</dd>
<dt>3</dt>
<dd> experimental</dd>
<dt>4</dt>
<dd> nearest neighbor (bad quality)</dd>
<dt>5</dt>
<dd> area</dd>
<dt>6</dt>
<dd> luma bicubic / chroma bilinear</dd>
<dt>7</dt>
<dd> gauss</dd>
<dt>8</dt>
<dd> sincR</dd>
<dt>9</dt>
<dd> lanczos</dd>
<dt>10</dt>
<dd> natural bicubic spline</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>NOTE:</i> Some -sws options are tunable. The description of the scale video filter has further information.</dd></dl>
<dt><code>-vc &lt;[-|+]codec1,[-|+]codec2,&#8230;[,]&gt;</code></dt>
<dd> Specify a priority list of video codecs to be used, according to their codec name in codecs.conf. Use a &#8216;-&#8216; before the codec name to omit it. Use a &#8216;+&#8217; before the codec name to force it, this will likely crash! If the list has a trailing &#8216;,&#8217; MPlayer will fall back on codecs not contained in the list.<br />
 <i>NOTE:</i> See -vc help for a full list of available codecs. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-vc divx</dt>
<dd> Force Win32/VfW DivX codec, no fallback.</dd>
<dt>-vc -divxds,-divx,</dt>
<dd> Skip Win32 DivX codecs.</dd>
<dt>-vc ffmpeg12,mpeg12,</dt>
<dd> Try libavcodec&#8217;s MPEG-1/2 codec, then libmpeg2, then others.</dd></dl>
</dl>
<dt><code>-vfm &lt;driver1,driver2,&#8230;&gt;</code></dt>
<dd> Specify a priority list of video codec families to be used, according to their names in codecs.conf. Falls back on the default codecs if none of the given codec families work.<br />
 <i>NOTE:</i> See -vfm help for a full list of available codec families. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-vfm ffmpeg,dshow,vfw</dt>
<dd> Try the libavcodec, then Directshow, then VfW codecs and fall back on others, if they do not work.</dd>
<dt>-vfm xanim</dt>
<dd> Try XAnim codecs first.</dd></dl>
</dl>
<dt><code>-x &lt;x&gt; (also see -zoom) (MPlayer only)</code></dt>
<dd> Scale image to width &lt;x&gt; (if software/hardware scaling is available). Disables aspect calculations.</dd>
<dt><code>-xvidopts &lt;option1:option2:&#8230;&gt;</code></dt>
<dd> Specify additional parameters when decoding with Xvid.<br />
 <i>NOTE:</i> Since libavcodec is faster than Xvid you might want to use the libavcodec postprocessing filter (-vf pp) and decoder (-vfm ffmpeg) instead. </dd>
<p> Xvid&#8217;s internal postprocessing filters:</p>
<dl>
<dl>
<dt>deblock-chroma (also see -vf pp)</dt>
<dd> chroma deblock filter</dd>
<dt>deblock-luma (also see -vf pp)</dt>
<dd> luma deblock filter</dd>
<dt>dering-luma (also see -vf pp)</dt>
<dd> luma deringing filter</dd>
<dt>dering-chroma (also see -vf pp)</dt>
<dd> chroma deringing filter</dd>
<dt>filmeffect (also see -vf noise)</dt>
<dd> Adds artificial film grain to the video. May increase perceived quality, while lowering true quality.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> rendering methods:</dd></dl>
<dl>
<dl>
<dt>dr2&nbsp;<wbr>&nbsp;</dt>
<dd> Activate direct rendering method 2.</dd>
<dt>nodr2</dt>
<dd> Deactivate direct rendering method 2.</dd></dl>
</dl>
<dt><code>-xy &lt;value&gt; (also see -zoom)</code></dt>
<dd>
</dd><dl>
<dl>
<dt>value&lt;=8</dt>
<dd> Scale image by factor &lt;value&gt;.</dd>
<dt>value&gt;8</dt>
<dd> Set width to value and calculate height to keep correct aspect ratio.</dd></dl>
</dl>
<dt><code>-y &lt;y&gt; (also see -zoom) (MPlayer only)</code></dt>
<dd> Scale image to height &lt;y&gt; (if software/hardware scaling is available). Disables aspect calculations.</dd>
<dt><code>-zoom&nbsp;<wbr>&nbsp;</code></dt>
<dd> Allow software scaling, where available. This will allow scaling with output drivers (like x11, fbdev) that do not support hardware scaling where MPlayer disables scaling by default for performance reasons.</dd></dl>
<h2>AUDIO FILTERS</h2>
<p> Audio filters allow you to modify the audio stream and its properties. The syntax is:</p>
<dl>
<dt><code>-af &lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></dt>
<dd> Setup a chain of audio filters.</dd></dl>
<p> <i>NOTE:</i> To get a full list of available audio filters, see -af help. </p>
<p> Audio filters are managed in lists. There are a few commands to manage the filter list.</p>
<dl>
<dt><code>-af-add &lt;filter1[,filter2,&#8230;]&gt;</code></dt>
<dd> Appends the filters given as arguments to the filter list.</dd>
<dt><code>-af-pre &lt;filter1[,filter2,&#8230;]&gt;</code></dt>
<dd> Prepends the filters given as arguments to the filter list.</dd>
<dt><code>-af-del &lt;index1[,index2,&#8230;]&gt;</code></dt>
<dd> Deletes the filters at the given indexes. Index numbers start at 0, negative numbers address the end of the list (-1 is the last).</dd>
<dt><code>-af-clr</code></dt>
<dd> Completely empties the filter list.</dd></dl>
<p> Available filters are:</p>
<dl>
<dt><code>resample[=srate[:sloppy[:type]]]</code></dt>
<dd> Changes the sample rate of the audio stream. Can be used if you have a fixed frequency sound card or if you are stuck with an old sound card that is only capable of max 44.1kHz. This filter is automatically enabled if necessary. It only supports 16-bit integer and float in native-endian format as input.<br />
 <i>NOTE:</i> With MEncoder, you need to also use -srate &lt;srate&gt;.</dd>
<dl>
<dl>
<dt>&lt;srate&gt;</dt>
<dd> output sample frequency in Hz. The valid range for this parameter is 8000 to 192000. If the input and output sample frequency are the same or if this parameter is omitted the filter is automatically unloaded. A high sample frequency normally improves the audio quality, especially when used in combination with other filters.</dd>
<dt>&lt;sloppy&gt;</dt>
<dd> Allow (1) or disallow (0) the output frequency to differ slightly from the frequency given by &lt;srate&gt; (default: 1). Can be used if the startup of the playback is extremely slow.</dd>
<dt>&lt;type&gt;</dt>
<dd> Select which resampling method to use.</dd>
<dl>
<dt>
</dt><dd> 0: linear interpolation (fast, poor quality especially when upsampling)<br />
 1: polyphase filterbank and integer processing<br />
 2: polyphase filterbank and floating point processing (slow, best quality)</dd></dl>
</dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af resample=44100:0:0</dt>
<dd> would set the output frequency of the resample filter to 44100Hz using exact output frequency scaling and linear interpolation.</dd></dl>
</dl>
<dt><code>lavcresample[=srate[:length[:linear[:count[:cutoff]]]]]</code></dt>
<dd> Changes the sample rate of the audio stream to an integer &lt;srate&gt; in Hz. It only supports the 16-bit native-endian format.<br />
 <i>NOTE:</i> With MEncoder, you need to also use -srate &lt;srate&gt;.</dd>
<dl>
<dl>
<dt>&lt;srate&gt;</dt>
<dd> the output sample rate</dd>
<dt>&lt;length&gt;</dt>
<dd> length of the filter with respect to the lower sampling rate (default: 16)</dd>
<dt>&lt;linear&gt;</dt>
<dd> if 1 then filters will be linearly interpolated between polyphase entries</dd>
<dt>&lt;count&gt;</dt>
<dd> log2 of the number of polyphase entries (&#8230;, 10-&gt;1024, 11-&gt;2048, 12-&gt;4096, &#8230;) (default: 10-&gt;1024)</dd>
<dt>&lt;cutoff&gt;</dt>
<dd> cutoff frequency (0.0-1.0), default set depending upon filter length</dd></dl>
</dl>
<dt><code>lavcac3enc[=tospdif[:bitrate[:minchn]]]</code></dt>
<dd> Encode multi-channel audio to AC-3 at runtime using libavcodec. Supports 16-bit native-endian input format, maximum 6 channels. The output is big-endian when outputting a raw AC-3 stream, native-endian when outputting to S/PDIF. The output sample rate of this filter is same with the input sample rate. When input sample rate is 48kHz, 44.1kHz, or 32kHz, this filter directly use it. Otherwise a resampling filter is auto-inserted before this filter to make the input and output sample rate be 48kHz. You need to specify &#8216;-channels N&#8217; to make the decoder decode audio into N-channel, then the filter can encode the N-channel input to AC-3. </dd>
<dl>
<dl>
<dt>&lt;tospdif&gt;</dt>
<dd> Output raw AC-3 stream if zero or not set, output to S/PDIF for passthrough when &lt;tospdif&gt; is set non-zero.</dd>
<dt>&lt;bitrate&gt;</dt>
<dd> The bitrate to encode the AC-3 stream. Set it to either 384 or 384000 to get 384kbits. Valid values: 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;320, 384, 448, 512, 576, 640 Default bitrate is based on the input channel number: 1ch: 96, 2ch: 192, 3ch: 224, 4ch: 384, 5ch: 448, 6ch: 448</dd>
<dt>&lt;minchn&gt;</dt>
<dd> If the input channel number is less than &lt;minchn&gt;, the filter will detach itself (default: 5).</dd></dl>
</dl>
<dt><code>sweep[=speed]</code></dt>
<dd> Produces a sine sweep.</dd>
<dl>
<dl>
<dt>&lt;0.0-1.0&gt;</dt>
<dd> Sine function delta, use very low values to hear the sweep.</dd></dl>
</dl>
<dt><code>sinesuppress[=freq:decay]</code></dt>
<dd> Remove a sine at the specified frequency. Useful to get rid of the 50/60Hz noise on low quality audio equipment. It probably only works on mono input.</dd>
<dl>
<dl>
<dt>&lt;freq&gt;</dt>
<dd> The frequency of the sine which should be removed (in Hz) (default: 50)</dd>
<dt>&lt;decay&gt;</dt>
<dd> Controls the adaptivity (a larger value will make the filter adapt to amplitude and phase changes quicker, a smaller value will make the adaptation slower) (default: 0.0001). Reasonable values are around 0.001.</dd></dl>
</dl>
<dt><code>bs2b[=option1:option2:&#8230;]</code></dt>
<dd> Bauer stereophonic to binaural transformation using libbs2b. Improves the headphone listening experience by making the sound similar to that from loudspeakers, allowing each ear to hear both channels and taking into account the distance difference and the head shadowing effect. It is applicable only to 2 channel audio.</dd>
<dl>
<dl>
<dt>fcut=&lt;300-1000&gt;</dt>
<dd> Set cut frequency in Hz.</dd>
<dt>feed=&lt;10-150&gt;</dt>
<dd> Set feed level for low frequencies in 0.1*dB.</dd>
<dt>profile=&lt;value&gt;</dt>
<dd> Several profiles are available for convenience:</dd>
<dl>
<dl>
<dt>default</dt>
<dd> will be used if nothing else was specified (fcut=700, feed=45)</dd>
<dt>cmoy&nbsp;</dt>
<dd> Chu Moy circuit implementation (fcut=700, feed=60)</dd>
<dt>jmeier</dt>
<dd> Jan Meier circuit implementation (fcut=650, feed=95)</dd></dl>
</dl>
</dl>
</dl>
<dl>
<dt>
</dt><dd> If fcut or feed options are specified together with a profile, they will be applied on top of the selected profile.</dd></dl>
<dt><code>hrtf[=flag]</code></dt>
<dd> Head-related transfer function: Converts multichannel audio to 2 channel output for headphones, preserving the spatiality of the sound. </dd>
<dl>
<dl>
<dt>Flag Meaning</dt>
<dd>
</dd><dt>m matrix decoding of the rear channel</dt>
<dd>
</dd><dt>s 2-channel matrix decoding</dt>
<dd>
</dd><dt>0 no matrix decoding (default)</dt>
<dd></dd></dl>
</dl>
<dt><code>equalizer=[g1:g2:g3:&#8230;:g10]</code></dt>
<dd> 10 octave band graphic equalizer, implemented using 10 IIR band pass filters. This means that it works regardless of what type of audio is being played back. The center frequencies for the 10 bands are: </dd>
<dl>
<dl>
<dt>No. frequency</dt>
<dd>
</dd><dt>0 31.25 Hz</dt>
<dd>
</dd><dt>1 62.50 Hz</dt>
<dd>
</dd><dt>2 125.00 Hz</dt>
<dd>
</dd><dt>3 250.00 Hz</dt>
<dd>
</dd><dt>4 500.00 Hz</dt>
<dd>
</dd><dt>5 1.00 kHz</dt>
<dd>
</dd><dt>6 2.00 kHz</dt>
<dd>
</dd><dt>7 4.00 kHz</dt>
<dd>
</dd><dt>8 8.00 kHz</dt>
<dd>
</dd><dt>9 16.00 kHz</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd> If the sample rate of the sound being played is lower than the center frequency for a frequency band, then that band will be disabled. A known bug with this filter is that the characteristics for the uppermost band are not completely symmetric if the sample rate is close to the center frequency of that band. This problem can be worked around by upsampling the sound using the resample filter before it reaches this filter.</dd></dl>
<dl>
<dl>
<dt>&lt;g1&gt;:&lt;g2&gt;:&lt;g3&gt;:&#8230;:&lt;g10&gt;</dt>
<dd> floating point numbers representing the gain in dB for each frequency band (-12-12)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af equalizer=11:11:10:5:0:-12:0:5:12:12 media.avi</dt>
<dd> Would amplify the sound in the upper and lower frequency region while canceling it almost completely around 1kHz.</dd></dl>
</dl>
<dt><code>channels=nch[:nr:from1:to1:from2:to2:from3:to3:&#8230;]</code></dt>
<dd> Can be used for adding, removing, routing and copying audio channels. If only &lt;nch&gt; is given the default routing is used, it works as follows: If the number of output channels is bigger than the number of input channels empty channels are inserted (except mixing from mono to stereo, then the mono channel is repeated in both of the output channels). If the number of output channels is smaller than the number of input channels the exceeding channels are truncated.</dd>
<dl>
<dl>
<dt>&lt;nch&gt;</dt>
<dd> number of output channels (1-8)</dd>
<dt>&lt;nr&gt;&nbsp;</dt>
<dd> number of routes (1-8)</dd>
<dt>&lt;from1:to1:from2:to2:from3:to3:&#8230;&gt;</dt>
<dd> Pairs of numbers between 0 and 7 that define where to route each channel.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af channels=4:4:0:1:1:0:2:2:3:3 media.avi</dt>
<dd> Would change the number of channels to 4 and set up 4 routes that swap channel 0 and channel 1 and leave channel 2 and 3 intact. Observe that if media containing two channels was played back, channels 2 and 3 would contain silence but 0 and 1 would still be swapped.</dd>
<dt>mplayer -af channels=6:4:0:0:0:1:0:2:0:3 media.avi</dt>
<dd> Would change the number of channels to 6 and set up 4 routes that copy channel 0 to channels 0 to 3. Channel 4 and 5 will contain silence.</dd></dl>
</dl>
<dt><code>format[=format] (also see -format)</code></dt>
<dd> Convert between different sample formats. Automatically enabled when needed by the sound card or another filter.</dd>
<dl>
<dl>
<dt>&lt;format&gt;</dt>
<dd> Sets the desired format. The general form is &#8216;sbe&#8217;, where &#8216;s&#8217; denotes the sign (either &#8216;s&#8217; for signed or &#8216;u&#8217; for unsigned), &#8216;b&#8217; denotes the number of bits per sample (16, 24 or 32) and &#8216;e&#8217; denotes the endianness (&#8216;le&#8217; means little-endian, &#8216;be&#8217; big-endian and &#8216;ne&#8217; the endianness of the computer MPlayer is running on). Valid values (amongst others) are: &#8216;s16le&#8217;, &#8216;u32be&#8217; and &#8216;u24ne&#8217;. Exceptions to this rule that are also valid format specifiers: u8, s8, floatle, floatbe, floatne, mulaw, alaw, mpeg2, ac3 and imaadpcm.</dd></dl>
</dl>
<dt><code>volume[=v[:sc]]</code></dt>
<dd> Implements software volume control. Use this filter with caution since it can reduce the signal to noise ratio of the sound. In most cases it is best to set the level for the PCM sound to max, leave this filter out and control the output level to your speakers with the master volume control of the mixer. In case your sound card has a digital PCM mixer instead of an analog one, and you hear distortion, use the MASTER mixer instead. If there is an external amplifier connected to the computer (this is almost always the case), the noise level can be minimized by adjusting the master level and the volume knob on the amplifier until the hissing noise in the background is gone.<br />
 This filter has a second feature: It measures the overall maximum sound level and prints out that level when MPlayer exits. This volume estimate can be used for setting the sound level in MEncoder such that the maximum dynamic range is utilized. This feature currently only works with floating-point data, use e.g. -af-adv force=5, or use -af stats.<br />
 <i>NOTE:</i> This filter is not reentrant and can therefore only be enabled once for every audio stream.</dd>
<dl>
<dl>
<dt>&lt;v&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> Sets the desired gain in dB for all channels in the stream from -200dB to +60dB, where -200dB mutes the sound completely and +60dB equals a gain of 1000 (default: 0).</dd>
<dt>&lt;sc&gt;&nbsp;</dt>
<dd> Turns soft clipping on (1) or off (0). Soft-clipping can make the sound more smooth if very high volume levels are used. Enable this option if the dynamic range of the loudspeakers is very low.<br />
 <i>WARNING:</i> This feature creates distortion and should be considered a last resort.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af volume=10.1:0 media.avi</dt>
<dd> Would amplify the sound by 10.1dB and hard-clip if the sound level is too high.</dd></dl>
</dl>
<dt><code>pan=n[:L00:L01:L02:&#8230;L10:L11:L12:&#8230;Ln0:Ln1:Ln2:&#8230;]</code></dt>
<dd> Mixes channels arbitrarily. Basically a combination of the volume and the channels filter that can be used to down-mix many channels to only a few, e.g. stereo to mono or vary the &quot;width&quot; of the center speaker in a surround sound system. This filter is hard to use, and will require some tinkering before the desired result is obtained. The number of options for this filter depends on the number of output channels. An example how to downmix a six-channel file to two channels with this filter can be found in the examples section near the end.</dd>
<dl>
<dl>
<dt>&lt;n&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> number of output channels (1-8)</dd>
<dt>&lt;Lij&gt;</dt>
<dd> How much of input channel i is mixed into output channel j (0-1). So in principle you first have n numbers saying what to do with the first input channel, then n numbers that act on the second input channel etc. If you do not specify any numbers for some input channels, 0 is assumed.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af pan=1:0.5:0.5 media.avi</dt>
<dd> Would down-mix from stereo to mono.</dd>
<dt>mplayer -af pan=3:1:0:0.5:0:1:0.5 media.avi</dt>
<dd> Would give 3 channel output leaving channels 0 and 1 intact, and mix channels 0 and 1 into output channel 2 (which could be sent to a subwoofer for example).</dd></dl>
</dl>
<dt><code>sub[=fc:ch]</code></dt>
<dd> Adds a subwoofer channel to the audio stream. The audio data used for creating the subwoofer channel is an average of the sound in channel 0 and channel 1. The resulting sound is then low-pass filtered by a 4th order Butterworth filter with a default cutoff frequency of 60Hz and added to a separate channel in the audio stream.<br />
 <i>Warning:</i> Disable this filter when you are playing DVDs with Dolby Digital 5.1 sound, otherwise this filter will disrupt the sound to the subwoofer.</dd>
<dl>
<dl>
<dt>&lt;fc&gt;&nbsp;</dt>
<dd> cutoff frequency in Hz for the low-pass filter (20Hz to 300Hz) (default: 60Hz) For the best result try setting the cutoff frequency as low as possible. This will improve the stereo or surround sound experience.</dd>
<dt>&lt;ch&gt;&nbsp;</dt>
<dd> Determines the channel number in which to insert the sub-channel audio. Channel number can be between 0 and 7 (default: 5). Observe that the number of channels will automatically be increased to &lt;ch&gt; if necessary.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af sub=100:4 -channels 5 media.avi</dt>
<dd> Would add a sub-woofer channel with a cutoff frequency of 100Hz to output channel 4.</dd></dl>
</dl>
<dt><code>center&nbsp;</code></dt>
<dd> Creates a center channel from the front channels. May currently be low quality as it does not implement a high-pass filter for proper extraction yet, but averages and halves the channels instead.</dd>
<dl>
<dl>
<dt>&lt;ch&gt;&nbsp;</dt>
<dd> Determines the channel number in which to insert the center channel. Channel number can be between 0 and 7 (default: 5). Observe that the number of channels will automatically be increased to &lt;ch&gt; if necessary.</dd></dl>
</dl>
<dt><code>surround[=delay]</code></dt>
<dd> Decoder for matrix encoded surround sound like Dolby Surround. Many files with 2 channel audio actually contain matrixed surround sound. Requires a sound card supporting at least 4 channels.</dd>
<dl>
<dl>
<dt>&lt;delay&gt;</dt>
<dd> delay time in ms for the rear speakers (0 to 1000) (default: 20) This delay should be set as follows: If d1 is the distance from the listening position to the front speakers and d2 is the distance from the listening position to the rear speakers, then the delay should be set to 15ms if d1 &lt;= d2 and to 15 + 5*(d1-d2) if d1 &gt; d2.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af surround=15 -channels 4 media.avi</dt>
<dd> Would add surround sound decoding with 15ms delay for the sound to the rear speakers.</dd></dl>
</dl>
<dt><code>delay[=ch1:ch2:&#8230;]</code></dt>
<dd> Delays the sound to the loudspeakers such that the sound from the different channels arrives at the listening position simultaneously. It is only useful if you have more than 2 loudspeakers.</dd>
<dl>
<dl>
<dt>ch1,ch2,&#8230;</dt>
<dd> The delay in ms that should be imposed on each channel (floating point number between 0 and 1000).</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> To calculate the required delay for the different channels do as follows:</dd>
<dl>
<dt>1.</dt>
<dd> Measure the distance to the loudspeakers in meters in relation to your listening position, giving you the distances s1 to s5 (for a 5.1 system). There is no point in compensating for the subwoofer (you will not hear the difference anyway).</dd>
<dt>2.</dt>
<dd> Subtract the distances s1 to s5 from the maximum distance, i.e. s[i] = max(s) &#8211; s[i]; i = 1&#8230;5.</dd>
<dt>3.</dt>
<dd> Calculate the required delays in ms as d[i] = 1000*s[i]/342; i = 1&#8230;5.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af delay=10.5:10.5:0:0:7:0 media.avi</dt>
<dd> Would delay front left and right by 10.5ms, the two rear channels and the sub by 0ms and the center channel by 7ms.</dd></dl>
</dl>
<dt><code>export[=mmapped_file[:nsamples]]</code></dt>
<dd> Exports the incoming signal to other processes using memory mapping (mmap()). Memory mapped areas contain a header: </dd>
<pre><code>
int nch                        /*number of channels*/
    int size                   /*buffer size*/
    unsigned long long counter /*Used to keep sync, updated every
                                 time new data is exported.*/
</code></pre>
<p> The rest is payload (non-interleaved) 16 bit data.</p>
<dl>
<dl>
<dt>&lt;mmapped_file&gt;</dt>
<dd> file to map data to (default: ~/.mplayer/mplayer-af_export)</dd>
<dt>&lt;nsamples&gt;</dt>
<dd> number of samples per channel (default: 512)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af export=/tmp/mplayer-af_export:1024 media.avi</dt>
<dd> Would export 1024 samples per channel to &#8216;/tmp/mplayer-af_export&#8217;.</dd></dl>
</dl>
<dt><code>extrastereo[=mul]</code></dt>
<dd> (Linearly) increases the difference between left and right channels which adds some sort of &quot;live&quot; effect to playback.</dd>
<dl>
<dl>
<dt>&lt;mul&gt;</dt>
<dd> Sets the difference coefficient (default: 2.5). 0.0 means mono sound (average of both channels), with 1.0 sound will be unchanged, with -1.0 left and right channels will be swapped.</dd></dl>
</dl>
<dt><code>volnorm[=method:target]</code></dt>
<dd> Maximizes the volume without distorting the sound.</dd>
<dl>
<dl>
<dt>&lt;method&gt;</dt>
<dd> Sets the used method.</dd>
<dl>
<dt>
</dt><dd> 1: Use a single sample to smooth the variations via the standard weighted mean over past samples (default).<br />
 2: Use several samples to smooth the variations via the standard weighted mean over past samples.</dd></dl>
<dt>&lt;target&gt;</dt>
<dd> Sets the target amplitude as a fraction of the maximum for the sample type (default: 0.25).</dd></dl>
</dl>
<dt><code>ladspa=file:label[:controls&#8230;]</code></dt>
<dd> Load a LADSPA (Linux Audio Developer&#8217;s Simple Plugin API) plugin. This filter is reentrant, so multiple LADSPA plugins can be used at once.</dd>
<dl>
<dl>
<dt>&lt;file&gt;</dt>
<dd> Specifies the LADSPA plugin library file. If LADSPA_PATH is set, it searches for the specified file. If it is not set, you must supply a fully specified pathname.</dd>
<dt>&lt;label&gt;</dt>
<dd> Specifies the filter within the library. Some libraries contain only one filter, but others contain many of them. Entering &#8216;help&#8217; here, will list all available filters within the specified library, which eliminates the use of &#8216;listplugins&#8217; from the LADSPA SDK.</dd>
<dt>&lt;controls&gt;</dt>
<dd> Controls are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). In verbose mode (add -v to the MPlayer command line), all available controls and their valid ranges are printed. This eliminates the use of &#8216;analyseplugin&#8217; from the LADSPA SDK.</dd></dl>
</dl>
<dt><code>comp&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Compressor/expander filter usable for microphone input. Prevents artifacts on very loud sound and raises the volume on very low sound. This filter is untested, maybe even unusable.</dd>
<dt><code>gate&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Noise gate filter similar to the comp audio filter. This filter is untested, maybe even unusable.</dd>
<dt><code>karaoke</code></dt>
<dd> Simple voice removal filter exploiting the fact that voice is usually recorded with mono gear and later &#8216;center&#8217; mixed onto the final audio stream. Beware that this filter will turn your signal into mono. Works well for 2 channel tracks; do not bother trying it on anything but 2 channel stereo.</dd>
<dt><code>scaletempo[=option1:option2:&#8230;]</code></dt>
<dd> Scales audio tempo without altering pitch, optionally synced to playback speed (default).<br />
 This works by playing &#8216;stride&#8217; ms of audio at normal speed then consuming &#8216;stride*scale&#8217; ms of input audio. It pieces the strides together by blending &#8216;overlap&#8217;% of stride with audio following the previous stride. It optionally performs a short statistical analysis on the next &#8216;search&#8217; ms of audio to determine the best overlap position.</dd>
<dl>
<dl>
<dt>scale=&lt;amount&gt;</dt>
<dd> Nominal amount to scale tempo. Scales this amount in addition to speed. (default: 1.0)</dd>
<dt>stride=&lt;amount&gt;</dt>
<dd> Length in milliseconds to output each stride. Too high of value will cause noticeable skips at high scale amounts and an echo at low scale amounts. Very low values will alter pitch. Increasing improves performance. (default: 60)</dd>
<dt>overlap=&lt;percent&gt;</dt>
<dd> Percentage of stride to overlap. Decreasing improves performance. (default: .20)</dd>
<dt>search=&lt;amount&gt;</dt>
<dd> Length in milliseconds to search for best overlap position. Decreasing improves performance greatly. On slow systems, you will probably want to set this very low. (default: 14)</dd>
<dt>speed=&lt;tempo|pitch|both|none&gt;</dt>
<dd> Set response to speed change.</dd>
<dl>
<dl>
<dt>tempo</dt>
<dd> Scale tempo in sync with speed (default).</dd>
<dt>pitch</dt>
<dd> Reverses effect of filter. Scales pitch without altering tempo. Add &#8216;[ speed_mult 0.9438743126816935&#8217; and &#8216;] speed_mult 1.059463094352953&#8217; to your input.conf to step by musical semi-tones. <i>WARNING:</i> Loses sync with video.</dd>
<dt>both</dt>
<dd> Scale both tempo and pitch.</dd>
<dt>none</dt>
<dd> Ignore speed changes.</dd></dl>
</dl>
</dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>mplayer -af scaletempo -speed 1.2 media.ogg</dt>
<dd> Would playback media at 1.2x normal speed, with audio at normal pitch. Changing playback speed, would change audio tempo to match.</dd>
<dt>mplayer -af scaletempo=scale=1.2:speed=none -speed 1.2 media.ogg</dt>
<dd> Would playback media at 1.2x normal speed, with audio at normal pitch, but changing playback speed has no effect on audio tempo.</dd>
<dt>mplayer -af scaletempo=stride=30:overlap=.50:search=10 media.ogg</dt>
<dd> Would tweak the quality and performace parameters.</dd>
<dt>mplayer -af format=floatne,scaletempo media.ogg</dt>
<dd> Would make scaletempo use float code. Maybe faster on some platforms.</dd>
<dt>mplayer -af scaletempo=scale=1.2:speed=pitch audio.ogg</dt>
<dd> Would playback audio file at 1.2x normal speed, with audio at normal pitch. Changing playback speed, would change pitch, leaving audio tempo at 1.2x.</dd></dl>
</dl>
<dt><code>stats&nbsp;<wbr>&nbsp;</code></dt>
<dd> Collects and prints statistics about the audio stream, especially the volume. These statistics are especially intended to help adjusting the volume while avoiding clipping. The volumes are printed in dB and compatible with the volume audio filter, they are always rounded towards -0dB. </dd>
<p> The &#8216;n_samples&#8217; field is the total number of samples seen by the filter. The &#8216;mean_volume&#8217; field is the root mean square. The &#8216;max_volume&#8217; field is exactly what it says. The &#8216;histogram_Xdb&#8217; fields count how many samples were at -XdB, for X just below max_volume. </p>
<p> For example, if max_volume is -7dB and histogram_7dB is 19, &#8216;volume=7&#8217; will not cause clipping and &#8216;volume=8&#8217; will cause clipping on exactly 19 samples.</dl>
<h2>VIDEO FILTERS</h2>
<p> Video filters allow you to modify the video stream and its properties. The syntax is:</p>
<dl>
<dt><code>-vf &lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></dt>
<dd> Setup a chain of video filters.</dd></dl>
<p> Many parameters are optional and set to default values if omitted. To explicitly use a default value set a parameter to &#8216;-1&#8217;. Parameters w:h means width x height in pixels, x:y means x;y position counted from the upper left corner of the bigger image.<br />
 <i>NOTE:</i> To get a full list of available video filters, see -vf help. </p>
<p> Video filters are managed in lists. There are a few commands to manage the filter list.</p>
<dl>
<dt><code>-vf-add &lt;filter1[,filter2,&#8230;]&gt;</code></dt>
<dd> Appends the filters given as arguments to the filter list.</dd>
<dt><code>-vf-pre &lt;filter1[,filter2,&#8230;]&gt;</code></dt>
<dd> Prepends the filters given as arguments to the filter list.</dd>
<dt><code>-vf-del &lt;index1[,index2,&#8230;]&gt;</code></dt>
<dd> Deletes the filters at the given indexes. Index numbers start at 0, negative numbers address the end of the list (-1 is the last).</dd>
<dt><code>-vf-clr</code></dt>
<dd> Completely empties the filter list.</dd></dl>
<p> With filters that support it, you can access parameters by their name.</p>
<dl>
<dt><code>-vf &lt;filter&gt;=help</code></dt>
<dd> Prints the parameter names and parameter value ranges for a particular filter.</dd>
<dt><code>-vf &lt;filter=named_parameter1=value1[:named_parameter2=value2:&#8230;]&gt;</code></dt>
<dd> Sets a named parameter to the given value. Use on and off or yes and no to set flag parameters.</dd></dl>
<p> Available filters are:</p>
<dl>
<dt><code>crop[=w:h:x:y]</code></dt>
<dd> Crops the given part of the image and discards the rest. Useful to remove black bands from widescreen movies.</dd>
<dl>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</dt>
<dd> Cropped width and height, defaults to original width and height.</dd>
<dt>&lt;x&gt;,&lt;y&gt;</dt>
<dd> Position of the cropped picture, defaults to center.</dd></dl>
</dl>
<dt><code>cropdetect[=limit:round[:reset]]</code></dt>
<dd> Calculates necessary cropping parameters and prints the recommended parameters to stdout.</dd>
<dl>
<dl>
<dt>&lt;limit&gt;</dt>
<dd> Threshold, which can be optionally specified from nothing (0) to everything (255) (default: 24). </dd>
<dt>&lt;round&gt;</dt>
<dd> Value which the width/height should be divisible by (default: 16). The offset is automatically adjusted to center the video. Use 2 to get only even dimensions (needed for 4:2:2 video). 16 is best when encoding to most video codecs. </dd>
<dt>&lt;reset&gt;</dt>
<dd> Counter that determines after how many frames cropdetect will reset the previously detected largest video area and start over to detect the current optimal crop area (default: 0). This can be useful when channel logos distort the video area. 0 indicates never reset and return the largest area encountered during playback.</dd></dl>
</dl>
<dt><code>rectangle[=w:h:x:y]</code></dt>
<dd> Draws a rectangle of the requested width and height at the specified coordinates over the image and prints current rectangle parameters to the console. This can be used to find optimal cropping parameters. If you bind the input.conf directive &#8216;change_rectangle&#8217; to keystrokes, you can move and resize the rectangle on the fly.</dd>
<dl>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</dt>
<dd> width and height (default: -1, maximum possible width where boundaries are still visible.)</dd>
<dt>&lt;x&gt;,&lt;y&gt;</dt>
<dd> top left corner position (default: -1, uppermost leftmost)</dd></dl>
</dl>
<dt><code>expand[=w:h:x:y:o:a:r]</code></dt>
<dd> Expands (not scales) movie resolution to the given value and places the unscaled original at coordinates x, y. Can be used for placing subtitles/OSD in the resulting black bands.</dd>
<dl>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</dt>
<dd> Expanded width,height (default: original width,height). Negative values for w and h are treated as offsets to the original size. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>expand=0:-50:0:0</dt>
<dd> Adds a 50 pixel border to the bottom of the picture.</dd></dl>
</dl>
<dt>&lt;x&gt;,&lt;y&gt;</dt>
<dd> position of original image on the expanded image (default: center)</dd>
<dt>&lt;o&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> OSD/subtitle rendering</dd>
<dl>
<dt>
</dt><dd> 0: disable (default)<br />
 1: enable</dd></dl>
<dt>&lt;a&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> Expands to fit an aspect instead of a resolution (default: 0). </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>expand=800:::::4/3</dt>
<dd> Expands to 800&#215;600, unless the source is higher resolution, in which case it expands to fill a 4/3 aspect.</dd></dl>
</dl>
<dt>&lt;r&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> Rounds up to make both width and height divisible by &lt;r&gt; (default: 1).</dd></dl>
</dl>
<dt><code>flip (also see -flip)</code></dt>
<dd> Flips the image upside down.</dd>
<dt><code>mirror&nbsp;</code></dt>
<dd> Mirrors the image on the Y axis.</dd>
<dt><code>rotate[=&lt;0-7&gt;]</code></dt>
<dd> Rotates the image by 90 degrees and optionally flips it. For values between 4-7 rotation is only done if the movie geometry is portrait and not landscape.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Rotate by 90 degrees clockwise and flip (default).</dd>
<dt>1</dt>
<dd> Rotate by 90 degrees clockwise.</dd>
<dt>2</dt>
<dd> Rotate by 90 degrees counterclockwise.</dd>
<dt>3</dt>
<dd> Rotate by 90 degrees counterclockwise and flip.</dd></dl>
</dl>
<dt><code>scale[=w:h[:interlaced[:chr_drop[:par[:par2[:presize[:noup[:arnd]]]]]]]]</code></dt>
<dd> Scales the image with the software scaler (slow) and performs a YUV&lt;-&gt;RGB colorspace conversion (also see -sws).</dd>
<dl>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</dt>
<dd> scaled width/height (default: original width/height)<br />
 <i>NOTE:</i> If -zoom is used, and underlying filters (including libvo) are incapable of scaling, it defaults to d_width/d_height!</dd>
<dl>
<dt>
</dt><dd>
&nbsp;0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;scaled d_width/d_height<br />
 -1: original width/height<br />
 -2: Calculate w/h using the other dimension and the prescaled aspect ratio.<br />
 -3: Calculate w/h using the other dimension and the original aspect ratio.<br />
 -(n+8): Like -n above, but rounding the dimension to the closest multiple of 16.</dd></dl>
<dt>&lt;interlaced&gt;</dt>
<dd> Toggle interlaced scaling.</dd>
<dl>
<dt>
</dt><dd> 0: off (default)<br />
 1: on</dd></dl>
<dt>&lt;chr_drop&gt;</dt>
<dd> chroma skipping</dd>
<dl>
<dt>
</dt><dd> 0: Use all available input lines for chroma.<br />
 1: Use only every 2. input line for chroma.<br />
 2: Use only every 4. input line for chroma.<br />
 3: Use only every 8. input line for chroma.</dd></dl>
<dt>&lt;par&gt;[:&lt;par2&gt;] (also see -sws)</dt>
<dd> Set some scaling parameters depending on the type of scaler selected with -sws.</dd>
<dl>
<dt>
</dt><dd> -sws 2 (bicubic): B (blurring) and C (ringing)<br />
 0.00:0.60 default<br />
 0.00:0.75 VirtualDub&#8217;s &quot;precise bicubic&quot;<br />
 0.00:0.50 Catmull-Rom spline<br />
 0.33:0.33 Mitchell-Netravali spline<br />
 1.00:0.00 cubic B-spline<br />
 -sws 7 (gaussian): sharpness (0 (soft) &#8211; 100 (sharp))<br />
 -sws 9 (lanczos): filter length (1-10)</dd></dl>
<dt>&lt;presize&gt;</dt>
<dd> Scale to preset sizes.</dd>
<dl>
<dt>
</dt><dd> qntsc: 352&#215;240 (NTSC quarter screen)<br />
 qpal: 352&#215;288 (PAL quarter screen)<br />
 ntsc: 720&#215;480 (standard NTSC)<br />
 pal: 720&#215;576 (standard PAL)<br />
 sntsc: 640&#215;480 (square pixel NTSC)<br />
 spal: 768&#215;576 (square pixel PAL)</dd></dl>
<dt>&lt;noup&gt;</dt>
<dd> Disallow upscaling past the original dimensions.</dd>
<dl>
<dt>
</dt><dd> 0: Allow upscaling (default).<br />
 1: Disallow upscaling if one dimension exceeds its original value.<br />
 2: Disallow upscaling if both dimensions exceed their original values.</dd></dl>
<dt>&lt;arnd&gt;</dt>
<dd> Accurate rounding for the vertical scaler, which may be faster or slower than the default rounding.</dd>
<dl>
<dt>
</dt><dd> 0: Disable accurate rounding (default).<br />
 1: Enable accurate rounding.</dd></dl>
</dl>
</dl>
<dt><code>dsize[=aspect|w:h:aspect-method:r]</code></dt>
<dd> Changes the intended display size/aspect at an arbitrary point in the filter chain. Aspect can be given as a fraction (4/3) or floating point number (1.33). Alternatively, you may specify the exact display width and height desired. Note that this filter does <code>not</code> do any scaling itself; it just affects what later scalers (software or hardware) will do when auto-scaling to correct aspect.</dd>
<dl>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</dt>
<dd> New display width and height. Can also be these special values:</dd>
<dl>
<dt>
</dt><dd>
&nbsp;0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;original display width and height<br />
 -1: original video width and height (default)<br />
 -2: Calculate w/h using the other dimension and the original display aspect ratio.<br />
 -3: Calculate w/h using the other dimension and the original video aspect ratio.</dd></dl>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>dsize=800:-2</dt>
<dd> Specifies a display resolution of 800&#215;600 for a 4/3 aspect video, or 800&#215;450 for a 16/9 aspect video.</dd></dl>
</dl>
<dt>&lt;aspect-method&gt;</dt>
<dd> Modifies width and height according to original aspect ratios.</dd>
<dl>
<dt>
</dt><dd> -1: Ignore original aspect ratio (default). </dd>
<p>&nbsp;0: Keep display aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as maximum resolution. </p>
<p>&nbsp;1: Keep display aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as minimum resolution. </p>
<p>&nbsp;2: Keep video aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as maximum resolution. </p>
<p>&nbsp;3: Keep video aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as minimum resolution.</dl>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>dsize=800:600:0</dt>
<dd> Specifies a display resolution of at most 800&#215;600, or smaller, in order to keep aspect.</dd></dl>
</dl>
<dt>&lt;r&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> Rounds up to make both width and height divisible by &lt;r&gt; (default: 1).</dd></dl>
</dl>
<dt><code>yvu9&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Forces software YVU9 to YV12 colorspace conversion. Deprecated in favor of the software scaler.</dd>
<dt><code>yuvcsp&nbsp;</code></dt>
<dd> Clamps YUV color values to the CCIR 601 range without doing real conversion.</dd>
<dt><code>palette</code></dt>
<dd> RGB/BGR 8 -&gt; 15/16/24/32bpp colorspace conversion using palette.</dd>
<dt><code>format[=fourcc[:outfourcc]]</code></dt>
<dd> Restricts the colorspace for the next filter without doing any conversion. Use together with the scale filter for a real conversion.<br />
 <i>NOTE:</i> For a list of available formats see format=fmt=help.</dd>
<dl>
<dl>
<dt>&lt;fourcc&gt;</dt>
<dd> format name like rgb15, bgr24, yv12, etc (default: yuy2)</dd>
<dt>&lt;outfourcc&gt;</dt>
<dd> Format name that should be substituted for the output. If this is not 100% compatible with the &lt;fourcc&gt; value it will crash.<br />
 Valid examples:<br />
 format=rgb24:bgr24 format=yuyv:yuy2<br />
 Invalid examples (will crash):<br />
 format=rgb24:yv12</dd></dl>
</dl>
<dt><code>noformat[=fourcc]</code></dt>
<dd> Restricts the colorspace for the next filter without doing any conversion. Unlike the format filter, this will allow any colorspace <code>except</code> the one you specify.<br />
 <i>NOTE:</i> For a list of available formats see noformat=fmt=help.</dd>
<dl>
<dl>
<dt>&lt;fourcc&gt;</dt>
<dd> format name like rgb15, bgr24, yv12, etc (default: yv12)</dd></dl>
</dl>
<dt><code>pp[=filter1[:option1[:option2&#8230;]]/[-]filter2&#8230;] (also see -pphelp)</code></dt>
<dd> Enables the specified chain of postprocessing subfilters. Subfilters must be separated by &#8216;/&#8217; and can be disabled by prepending a &#8216;-&#8216;. Each subfilter and some options have a short and a long name that can be used interchangeably, i.e. dr/dering are the same. All subfilters share common options to determine their scope:</dd>
<dl>
<dl>
<dt>a/autoq</dt>
<dd> Automatically switch the subfilter off if the CPU is too slow.</dd>
<dt>c/chrom</dt>
<dd> Do chrominance filtering, too (default).</dd>
<dt>y/nochrom</dt>
<dd> Do luminance filtering only (no chrominance).</dd>
<dt>n/noluma</dt>
<dd> Do chrominance filtering only (no luminance).</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
 <i>NOTE:</i> -pphelp shows a list of available subfilters. </dd>
<p> Available subfilters are</dl>
<dl>
<dl>
<dt>hb/hdeblock[:difference[:flatness]]</dt>
<dd> horizontal deblocking filter</dd>
<dl>
<dt>
</dt><dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dd></dl>
<dt>vb/vdeblock[:difference[:flatness]]</dt>
<dd> vertical deblocking filter</dd>
<dl>
<dt>
</dt><dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dd></dl>
<dt>ha/hadeblock[:difference[:flatness]]</dt>
<dd> accurate horizontal deblocking filter</dd>
<dl>
<dt>
</dt><dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dd></dl>
<dt>va/vadeblock[:difference[:flatness]]</dt>
<dd> accurate vertical deblocking filter</dd>
<dl>
<dt>
</dt><dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dd></dl>
<p> The horizontal and vertical deblocking filters share the difference and flatness values so you cannot set different horizontal and vertical thresholds. </p>
<dt>h1/x1hdeblock</dt>
<dd> experimental horizontal deblocking filter</dd>
<dt>v1/x1vdeblock</dt>
<dd> experimental vertical deblocking filter</dd>
<dt>dr/dering</dt>
<dd> deringing filter</dd>
<dt>tn/tmpnoise[:threshold1[:threshold2[:threshold3]]]</dt>
<dd> temporal noise reducer</dd>
<dl>
<dt>
</dt><dd> &lt;threshold1&gt;: larger -&gt; stronger filtering<br />
 &lt;threshold2&gt;: larger -&gt; stronger filtering<br />
 &lt;threshold3&gt;: larger -&gt; stronger filtering</dd></dl>
<dt>al/autolevels[:f/fullyrange]</dt>
<dd> automatic brightness / contrast correction</dd>
<dl>
<dt>
</dt><dd> f/fullyrange: Stretch luminance to (0-255).</dd></dl>
<dt>lb/linblenddeint</dt>
<dd> Linear blend deinterlacing filter that deinterlaces the given block by filtering all lines with a (1 2 1) filter.</dd>
<dt>li/linipoldeint</dt>
<dd> Linear interpolating deinterlacing filter that deinterlaces the given block by linearly interpolating every second line.</dd>
<dt>ci/cubicipoldeint</dt>
<dd> Cubic interpolating deinterlacing filter deinterlaces the given block by cubically interpolating every second line.</dd>
<dt>md/mediandeint</dt>
<dd> Median deinterlacing filter that deinterlaces the given block by applying a median filter to every second line.</dd>
<dt>fd/ffmpegdeint</dt>
<dd> FFmpeg deinterlacing filter that deinterlaces the given block by filtering every second line with a (-1 4 2 4 -1) filter.</dd>
<dt>l5/lowpass5</dt>
<dd> Vertically applied FIR lowpass deinterlacing filter that deinterlaces the given block by filtering all lines with a (-1 2 6 2 -1) filter.</dd>
<dt>fq/forceQuant[:quantizer]</dt>
<dd> Overrides the quantizer table from the input with the constant quantizer you specify.</dd>
<dl>
<dt>
</dt><dd> &lt;quantizer&gt;: quantizer to use</dd></dl>
<dt>de/default</dt>
<dd> default pp filter combination (hb:a,vb:a,dr:a)</dd>
<dt>fa/fast</dt>
<dd> fast pp filter combination (h1:a,v1:a,dr:a)</dd>
<dt>ac&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> high quality pp filter combination (ha:a:128:7,va:a,dr:a)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>-vf pp=hb/vb/dr/al</dt>
<dd> horizontal and vertical deblocking, deringing and automatic brightness/contrast</dd>
<dt>-vf pp=de/-al</dt>
<dd> default filters without brightness/contrast correction</dd>
<dt>-vf pp=default/tmpnoise:1:2:3</dt>
<dd> Enable default filters &amp; temporal denoiser.</dd>
<dt>-vf pp=hb:y/vb:a</dt>
<dd> Horizontal deblocking on luminance only, and switch vertical deblocking on or off automatically depending on available CPU time.</dd></dl>
</dl>
<dt><code>spp[=quality[:qp[:mode]]]</code></dt>
<dd> Simple postprocessing filter that compresses and decompresses the image at several (or &#8211; in the case of quality level 6 &#8211; all) shifts and averages the results.</dd>
<dl>
<dl>
<dt>&lt;quality&gt;</dt>
<dd> 0-6 (default: 3)</dd>
<dt>&lt;qp&gt;&nbsp;</dt>
<dd> Force quantization parameter (default: 0, use QP from video).</dd>
<dt>&lt;mode&gt;</dt>
<dd> 0: hard thresholding (default)<br />
 1: soft thresholding (better deringing, but blurrier)<br />
 4: like 0, but also use B-frames&#8217; QP (may cause flicker)<br />
 5: like 1, but also use B-frames&#8217; QP (may cause flicker)</dd></dl>
</dl>
<dt><code>uspp[=quality[:qp]]</code></dt>
<dd> Ultra simple &amp; slow postprocessing filter that compresses and decompresses the image at several (or &#8211; in the case of quality level 8 &#8211; all) shifts and averages the results. The way this differs from the behavior of spp is that uspp actually encodes &amp; decodes each case with libavcodec Snow, whereas spp uses a simplified intra only 8&#215;8 DCT similar to MJPEG.</dd>
<dl>
<dl>
<dt>&lt;quality&gt;</dt>
<dd> 0-8 (default: 3)</dd>
<dt>&lt;qp&gt;&nbsp;</dt>
<dd> Force quantization parameter (default: 0, use QP from video).</dd></dl>
</dl>
<dt><code>fspp[=quality[:qp[:strength[:bframes]]]]</code></dt>
<dd> faster version of the simple postprocessing filter</dd>
<dl>
<dl>
<dt>&lt;quality&gt;</dt>
<dd> 4-5 (equivalent to spp; default: 4)</dd>
<dt>&lt;qp&gt;&nbsp;</dt>
<dd> Force quantization parameter (default: 0, use QP from video).</dd>
<dt>&lt;-15-32&gt;</dt>
<dd> Filter strength, lower values mean more details but also more artifacts, while higher values make the image smoother but also blurrier (default: 0 &#8211; PSNR optimal).</dd>
<dt>&lt;bframes&gt;</dt>
<dd> 0: do not use QP from B-frames (default)<br />
 1: use QP from B-frames too (may cause flicker)</dd></dl>
</dl>
<dt><code>pp7[=qp[:mode]]</code></dt>
<dd> Variant of the spp filter, similar to spp=6 with 7 point DCT where only the center sample is used after IDCT.</dd>
<dl>
<dl>
<dt>&lt;qp&gt;&nbsp;</dt>
<dd> Force quantization parameter (default: 0, use QP from video).</dd>
<dt>&lt;mode&gt;</dt>
<dd> 0: hard thresholding<br />
 1: soft thresholding (better deringing, but blurrier)<br />
 2: medium thresholding (default, good results)</dd></dl>
</dl>
<dt><code>qp=equation</code></dt>
<dd> quantization parameter (QP) change filter</dd>
<dl>
<dl>
<dt>&lt;equation&gt;</dt>
<dd> some equation like &quot;2+2*sin(PI*qp)&quot;</dd></dl>
</dl>
<dt><code>geq=equation</code></dt>
<dd> generic equation change filter</dd>
<dl>
<dl>
<dt>&lt;equation&gt;</dt>
<dd> Some equation, e.g. &#8216;p(W-X\,Y)&#8217; to flip the image horizontally. You can use whitespace to make the equation more readable. There are a couple of constants that can be used in the equation:</dd>
<dl>
<dt>
</dt><dd> PI: the number pi<br />
 E: the number e<br />
 X / Y: the coordinates of the current sample<br />
 W / H: width and height of the image<br />
 SW / SH: width/height scale depending on the currently filtered plane, e.g. 1,1 and 0.5,0.5 for YUV 4:2:0.<br />
 p(x,y): returns the value of the pixel at location x/y of the current plane.</dd></dl>
</dl>
</dl>
<dt><code>test&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Generate various test patterns.</dd>
<dt><code>rgbtest[=width:height]</code></dt>
<dd> Generate an RGB test pattern useful for detecting RGB vs BGR issues. You should see a red, green and blue stripe from top to bottom.</dd>
<dl>
<dl>
<dt>&lt;width&gt;</dt>
<dd> Desired width of generated image (default: 0). 0 means width of input image. </dd>
<dt>&lt;height&gt;</dt>
<dd> Desired height of generated image (default: 0). 0 means height of input image.</dd></dl>
</dl>
<dt><code>lavc[=quality:fps]</code></dt>
<dd> Fast software YV12 to MPEG-1 conversion with libavcodec for use with DVB/DXR3/IVTV/V4L2.</dd>
<dl>
<dl>
<dt>&lt;quality&gt;</dt>
<dd> 1-31: fixed qscale<br />
 32-: fixed bitrate in kbits</dd>
<dt>&lt;fps&gt;</dt>
<dd> force output fps (float value) (default: 0, autodetect based on height)</dd></dl>
</dl>
<dt><code>dvbscale[=aspect]</code></dt>
<dd> Set up optimal scaling for DVB cards, scaling the x axis in hardware and calculating the y axis scaling in software to keep aspect. Only useful together with expand and scale.</dd>
<dl>
<dl>
<dt>&lt;aspect&gt;</dt>
<dd> Control aspect ratio, calculate as DVB_HEIGHT*ASPECTRATIO (default: 576*4/3=768), set it to 576*(16/9)=1024 for a 16:9 TV.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>-vf dvbscale,scale=-1:0,expand=-1:576:-1:-1:1,lavc</dt>
<dd> FIXME: Explain what this does.</dd></dl>
</dl>
<dt><code>noise[=luma[u][t|a][h][p]:chroma[u][t|a][h][p]]</code></dt>
<dd> Adds noise.</dd>
<dl>
<dl>
<dt>&lt;0-100&gt;</dt>
<dd> luma noise</dd>
<dt>&lt;0-100&gt;</dt>
<dd> chroma noise</dd>
<dt>u</dt>
<dd> uniform noise (gaussian otherwise)</dd>
<dt>t</dt>
<dd> temporal noise (noise pattern changes between frames)</dd>
<dt>a</dt>
<dd> averaged temporal noise (smoother, but a lot slower)</dd>
<dt>h</dt>
<dd> high quality (slightly better looking, slightly slower)</dd>
<dt>p</dt>
<dd> mix random noise with a (semi)regular pattern</dd></dl>
</dl>
<dt><code>denoise3d[=luma_spatial:chroma_spatial:luma_tmp:chroma_tmp]</code></dt>
<dd> This filter aims to reduce image noise producing smooth images and making still images really still (This should enhance compressibility.).</dd>
<dl>
<dl>
<dt>&lt;luma_spatial&gt;</dt>
<dd> spatial luma strength (default: 4)</dd>
<dt>&lt;chroma_spatial&gt;</dt>
<dd> spatial chroma strength (default: 3)</dd>
<dt>&lt;luma_tmp&gt;</dt>
<dd> luma temporal strength (default: 6)</dd>
<dt>&lt;chroma_tmp&gt;</dt>
<dd> chroma temporal strength (default: luma_tmp*chroma_spatial/luma_spatial)</dd></dl>
</dl>
<dt><code>hqdn3d[=luma_spatial:chroma_spatial:luma_tmp:chroma_tmp]</code></dt>
<dd> High precision/quality version of the denoise3d filter. Parameters and usage are the same.</dd>
<dt><code>ow[=depth[:luma_strength[:chroma_strength]]]</code></dt>
<dd> Overcomplete Wavelet denoiser.</dd>
<dl>
<dl>
<dt>&lt;depth&gt;</dt>
<dd> Larger depth values will denoise lower frequency components more, but slow down filtering (default: 8).</dd>
<dt>&lt;luma_strength&gt;</dt>
<dd> luma strength (default: 1.0)</dd>
<dt>&lt;chroma_strength&gt;</dt>
<dd> chroma strength (default: 1.0)</dd></dl>
</dl>
<dt><code>eq[=brightness:contrast] (OBSOLETE)</code></dt>
<dd> Software equalizer with interactive controls just like the hardware equalizer, for cards/drivers that do not support brightness and contrast controls in hardware. Might also be useful with MEncoder, either for fixing poorly captured movies, or for slightly reducing contrast to mask artifacts and get by with lower bitrates.</dd>
<dl>
<dl>
<dt>&lt;-100-100&gt;</dt>
<dd> initial brightness</dd>
<dt>&lt;-100-100&gt;</dt>
<dd> initial contrast</dd></dl>
</dl>
<dt><code>eq2[=gamma:contrast:brightness:saturation:rg:gg:bg:weight]</code></dt>
<dd> Alternative software equalizer that uses lookup tables (very slow), allowing gamma correction in addition to simple brightness and contrast adjustment. Note that it uses the same MMX optimized code as -vf eq if all gamma values are 1.0. The parameters are given as floating point values.</dd>
<dl>
<dl>
<dt>&lt;0.1-10&gt;</dt>
<dd> initial gamma value (default: 1.0)</dd>
<dt>&lt;-2-2&gt;</dt>
<dd> initial contrast, where negative values result in a negative image (default: 1.0)</dd>
<dt>&lt;-1-1&gt;</dt>
<dd> initial brightness (default: 0.0)</dd>
<dt>&lt;0-3&gt;</dt>
<dd> initial saturation (default: 1.0)</dd>
<dt>&lt;0.1-10&gt;</dt>
<dd> gamma value for the red component (default: 1.0)</dd>
<dt>&lt;0.1-10&gt;</dt>
<dd> gamma value for the green component (default: 1.0)</dd>
<dt>&lt;0.1-10&gt;</dt>
<dd> gamma value for the blue component (default: 1.0)</dd>
<dt>&lt;0-1&gt;</dt>
<dd> The weight parameter can be used to reduce the effect of a high gamma value on bright image areas, e.g. keep them from getting overamplified and just plain white. A value of 0.0 turns the gamma correction all the way down while 1.0 leaves it at its full strength (default: 1.0).</dd></dl>
</dl>
<dt><code>hue[=hue:saturation]</code></dt>
<dd> Software equalizer with interactive controls just like the hardware equalizer, for cards/drivers that do not support hue and saturation controls in hardware.</dd>
<dl>
<dl>
<dt>&lt;-180-180&gt;</dt>
<dd> initial hue (default: 0.0)</dd>
<dt>&lt;-100-100&gt;</dt>
<dd> initial saturation, where negative values result in a negative chroma (default: 1.0)</dd></dl>
</dl>
<dt><code>halfpack[=f]</code></dt>
<dd> Convert planar YUV 4:2:0 to half-height packed 4:2:2, downsampling luma but keeping all chroma samples. Useful for output to low-resolution display devices when hardware downscaling is poor quality or is not available. Can also be used as a primitive luma-only deinterlacer with very low CPU usage.</dd>
<dl>
<dl>
<dt>&lt;f&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> By default, halfpack averages pairs of lines when downsampling. Any value different from 0 or 1 gives the default (averaging) behavior.</dd>
<dl>
<dt>
</dt><dd> 0: Only use even lines when downsampling.<br />
 1: Only use odd lines when downsampling.</dd></dl>
</dl>
</dl>
<dt><code>ilpack[=mode]</code></dt>
<dd> When interlaced video is stored in YUV 4:2:0 formats, chroma interlacing does not line up properly due to vertical downsampling of the chroma channels. This filter packs the planar 4:2:0 data into YUY2 (4:2:2) format with the chroma lines in their proper locations, so that in any given scanline, the luma and chroma data both come from the same field.</dd>
<dl>
<dl>
<dt>&lt;mode&gt;</dt>
<dd> Select the sampling mode.</dd>
<dl>
<dt>
</dt><dd> 0: nearest-neighbor sampling, fast but incorrect<br />
 1: linear interpolation (default)</dd></dl>
</dl>
</dl>
<dt><code>harddup</code></dt>
<dd> Only useful with MEncoder. If harddup is used when encoding, it will force duplicate frames to be encoded in the output. This uses slightly more space, but is necessary for output to MPEG files or if you plan to demux and remux the video stream after encoding. Should be placed at or near the end of the filter chain unless you have a good reason to do otherwise.</dd>
<dt><code>softskip</code></dt>
<dd> Only useful with MEncoder. Softskip moves the frame skipping (dropping) step of encoding from before the filter chain to some point during the filter chain. This allows filters which need to see all frames (inverse telecine, temporal denoising, etc.) to function properly. Should be placed after the filters which need to see all frames and before any subsequent filters that are CPU-intensive.</dd>
<dt><code>decimate[=max:hi:lo:frac]</code></dt>
<dd> Drops frames that do not differ greatly from the previous frame in order to reduce framerate. The main use of this filter is for very-low-bitrate encoding (e.g. streaming over dialup modem), but it could in theory be used for fixing movies that were inverse-telecined incorrectly.</dd>
<dl>
<dl>
<dt>&lt;max&gt;</dt>
<dd> Sets the maximum number of consecutive frames which can be dropped (if positive), or the minimum interval between dropped frames (if negative).</dd>
<dt>&lt;hi&gt;,&lt;lo&gt;,&lt;frac&gt;</dt>
<dd> A frame is a candidate for dropping if no 8&#215;8 region differs by more than a threshold of &lt;hi&gt;, and if not more than &lt;frac&gt; portion (1 meaning the whole image) differs by more than a threshold of &lt;lo&gt;. Values of &lt;hi&gt; and &lt;lo&gt; are for 8&#215;8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block.</dd></dl>
</dl>
<dt><code>dint[=sense:level]</code></dt>
<dd> The drop-deinterlace (dint) filter detects and drops the first from a set of interlaced video frames.</dd>
<dl>
<dl>
<dt>&lt;0.0-1.0&gt;</dt>
<dd> relative difference between neighboring pixels (default: 0.1)</dd>
<dt>&lt;0.0-1.0&gt;</dt>
<dd> What part of the image has to be detected as interlaced to drop the frame (default: 0.15).</dd></dl>
</dl>
<dt><code>lavcdeint (OBSOLETE)</code></dt>
<dd> FFmpeg deinterlacing filter, same as -vf pp=fd</dd>
<dt><code>lavfi=filtergraph</code></dt>
<dd> FFmpeg libavfilter wrapper. <i>filtergraph</i> defines a whole libavfilter graph with one input and one output. See <a rel="nofollow" href="http://www.ffmpeg.org/libavfilter.html#SEC4">http://www.ffmpeg.org/libavfilter.html#SEC4</a> for details. </dd>
<p> As a special case, if <i>filtergraph</i> is <code>$</code><i>word</i> then the value of the <i>word</i> environment variable is used; this is necessary if commas are present in the graph description, as mplayer uses them as a delimiter between filters. </p>
<p> <i>NOTE:</i> This filter is considered experimental, it may interact strangely with other filters. </p>
<p> <i>EXAMPLE:</i><br />
 overlay=&quot;movie=$small_video, scale=160:120 [ca]; [in] [ca] overlay=16:8&quot; mplayer -vf lavfi=&#8217;$overlay&#8217; $big_video</p>
<dt><code>kerndeint[=thresh[:map[:order[:sharp[:twoway]]]]]</code></dt>
<dd> Donald Graft&#8217;s adaptive kernel deinterlacer. Deinterlaces parts of a video if a configurable threshold is exceeded.</dd>
<dl>
<dl>
<dt>&lt;0-255&gt;</dt>
<dd> threshold (default: 10)</dd>
<dt>&lt;map&gt;</dt>
<dd>
</dd><dl>
<dt>
</dt><dd> 0: Ignore pixels exceeding the threshold (default).<br />
 1: Paint pixels exceeding the threshold white.</dd></dl>
<dt>&lt;order&gt;</dt>
<dd>
</dd><dl>
<dt>
</dt><dd> 0: Leave fields alone (default).<br />
 1: Swap fields.</dd></dl>
<dt>&lt;sharp&gt;</dt>
<dd>
</dd><dl>
<dt>
</dt><dd> 0: Disable additional sharpening (default).<br />
 1: Enable additional sharpening.</dd></dl>
<dt>&lt;twoway&gt;</dt>
<dd>
</dd><dl>
<dt>
</dt><dd> 0: Disable twoway sharpening (default).<br />
 1: Enable twoway sharpening.</dd></dl>
</dl>
</dl>
<dt><code>unsharp[=l|cWxH:amount[:l|cWxH:amount]]</code></dt>
<dd> unsharp mask / gaussian blur</dd>
<dl>
<dl>
<dt>l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Apply effect on luma component.</dd>
<dt>c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Apply effect on chroma components.</dd>
<dt>&lt;width&gt;x&lt;height&gt;</dt>
<dd> width and height of the matrix, odd sized in both directions (min = 3&#215;3, max = 13&#215;11 or 11&#215;13, usually something between 3&#215;3 and 7&#215;7)</dd>
<dt>amount</dt>
<dd> Relative amount of sharpness/blur to add to the image (a sane range should be -1.5-1.5).</dd>
<dl>
<dt>
</dt><dd> &lt;0: blur<br />
 &gt;0: sharpen</dd></dl>
</dl>
</dl>
<dt><code>swapuv&nbsp;</code></dt>
<dd> Swap U &amp; V plane.</dd>
<dt><code>il[=d|i][s][:[d|i][s]]</code></dt>
<dd> (De)interleaves lines. The goal of this filter is to add the ability to process interlaced images pre-field without deinterlacing them. You can filter your interlaced DVD and play it on a TV without breaking the interlacing. While deinterlacing (with the postprocessing filter) removes interlacing permanently (by smoothing, averaging, etc) deinterleaving splits the frame into 2 fields (so called half pictures), so you can process (filter) them independently and then re-interleave them.</dd>
<dl>
<dl>
<dt>d</dt>
<dd> deinterleave (placing one above the other)</dd>
<dt>i</dt>
<dd> interleave</dd>
<dt>s</dt>
<dd> swap fields (exchange even &amp; odd lines)</dd></dl>
</dl>
<dt><code>fil[=i|d]</code></dt>
<dd> (De)interleaves lines. This filter is very similar to the il filter but much faster, the main disadvantage is that it does not always work. Especially if combined with other filters it may produce randomly messed up images, so be happy if it works but do not complain if it does not for your combination of filters.</dd>
<dl>
<dl>
<dt>d</dt>
<dd> Deinterleave fields, placing them side by side.</dd>
<dt>i</dt>
<dd> Interleave fields again (reversing the effect of fil=d).</dd></dl>
</dl>
<dt><code>field[=n]</code></dt>
<dd> Extracts a single field from an interlaced image using stride arithmetic to avoid wasting CPU time. The optional argument n specifies whether to extract the even or the odd field (depending on whether n is even or odd).</dd>
<dt><code>detc[=var1=value1:var2=value2:&#8230;]</code></dt>
<dd> Attempts to reverse the &#8216;telecine&#8217; process to recover a clean, non-interlaced stream at film framerate. This was the first and most primitive inverse telecine filter to be added to MPlayer/MEncoder. It works by latching onto the telecine 3:2 pattern and following it as long as possible. This makes it suitable for perfectly-telecined material, even in the presence of a fair degree of noise, but it will fail in the presence of complex post-telecine edits. Development on this filter is no longer taking place, as ivtc, pullup, and filmdint are better for most applications. The following arguments (see syntax above) may be used to control detc&#8217;s behavior:</dd>
<dl>
<dl>
<dt>&lt;dr&gt;&nbsp;</dt>
<dd> Set the frame dropping mode.</dd>
<dl>
<dt>
</dt><dd> 0: Do not drop frames to maintain fixed output framerate (default).<br />
 1: Always drop a frame when there have been no drops or telecine merges in the past 5 frames.<br />
 2: Always maintain exact 5:4 input to output frame ratio.<br />
 <i>NOTE:</i> Use mode 1 or 2 with MEncoder.</dd></dl>
<dt>&lt;am&gt;&nbsp;</dt>
<dd> Analysis mode.</dd>
<dl>
<dt>
</dt><dd> 0: Fixed pattern with initial frame number specified by &lt;fr&gt;.<br />
 1: aggressive search for telecine pattern (default)</dd></dl>
<dt>&lt;fr&gt;&nbsp;</dt>
<dd> Set initial frame number in sequence. 0-2 are the three clean progressive frames; 3 and 4 are the two interlaced frames. The default, -1, means &#8216;not in telecine sequence&#8217;. The number specified here is the type for the imaginary previous frame before the movie starts.</dd>
<dt>&lt;t0&gt;, &lt;t1&gt;, &lt;t2&gt;, &lt;t3&gt;</dt>
<dd> Threshold values to be used in certain modes.</dd></dl>
</dl>
<dt><code>ivtc[=1]</code></dt>
<dd> Experimental &#8216;stateless&#8217; inverse telecine filter. Rather than trying to lock on to a pattern like the detc filter does, ivtc makes its decisions independently for each frame. This will give much better results for material that has undergone heavy editing after telecine was applied, but as a result it is not as forgiving of noisy input, for example TV capture. The optional parameter (ivtc=1) corresponds to the dr=1 option for the detc filter, and should be used with MEncoder but not with MPlayer. As with detc, you must specify the correct output framerate (-ofps 24000/1001) when using MEncoder. Further development on ivtc has stopped, as the pullup and filmdint filters appear to be much more accurate.</dd>
<dt><code>pullup[=jl:jr:jt:jb:sb:mp]</code></dt>
<dd> Third-generation pulldown reversal (inverse telecine) filter, capable of handling mixed hard-telecine, 24000/1001 fps progressive, and 30000/1001 fps progressive content. The pullup filter is designed to be much more robust than detc or ivtc, by taking advantage of future context in making its decisions. Like ivtc, pullup is stateless in the sense that it does not lock onto a pattern to follow, but it instead looks forward to the following fields in order to identify matches and rebuild progressive frames. It is still under development, but believed to be quite accurate.</dd>
<dl>
<dl>
<dt>jl, jr, jt, and jb</dt>
<dd> These options set the amount of &quot;junk&quot; to ignore at the left, right, top, and bottom of the image, respectively. Left/right are in units of 8 pixels, while top/bottom are in units of 2 lines. The default is 8 pixels on each side. </dd>
<dt>sb (strict breaks)</dt>
<dd> Setting this option to 1 will reduce the chances of pullup generating an occasional mismatched frame, but it may also cause an excessive number of frames to be dropped during high motion sequences. Conversely, setting it to -1 will make pullup match fields more easily. This may help processing of video where there is slight blurring between the fields, but may also cause there to be interlaced frames in the output. </dd>
<dt>mp (metric plane)</dt>
<dd> This option may be set to 1 or 2 to use a chroma plane instead of the luma plane for doing pullup&#8217;s computations. This may improve accuracy on very clean source material, but more likely will decrease accuracy, especially if there is chroma noise (rainbow effect) or any grayscale video. The main purpose of setting mp to a chroma plane is to reduce CPU load and make pullup usable in realtime on slow machines.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>NOTE:</i> Always follow pullup with the softskip filter when encoding to ensure that pullup is able to see each frame. Failure to do so will lead to incorrect output and will usually crash, due to design limitations in the codec/filter layer.</dd></dl>
<dt><code>filmdint[=options]</code></dt>
<dd> Inverse telecine filter, similar to the pullup filter above. It is designed to handle any pulldown pattern, including mixed soft and hard telecine and limited support for movies that are slowed down or sped up from their original framerate for TV. Only the luma plane is used to find the frame breaks. If a field has no match, it is deinterlaced with simple linear approximation. If the source is MPEG-2, this must be the first filter to allow access to the field-flags set by the MPEG-2 decoder. Depending on the source MPEG, you may be fine ignoring this advice, as long as you do not see lots of &quot;Bottom-first field&quot; warnings. With no options it does normal inverse telecine, and should be used together with mencoder -fps 30000/1001 -ofps 24000/1001. When this filter is used with MPlayer, it will result in an uneven framerate during playback, but it is still generally better than using pp=lb or no deinterlacing at all. Multiple options can be specified separated by /.</dd>
<dl>
<dl>
<dt>crop=&lt;w&gt;:&lt;h&gt;:&lt;x&gt;:&lt;y&gt;</dt>
<dd> Just like the crop filter, but faster, and works on mixed hard and soft telecined content as well as when y is not a multiple of 4. If x or y would require cropping fractional pixels from the chroma planes, the crop area is extended. This usually means that x and y must be even.</dd>
<dt>io=&lt;ifps&gt;:&lt;ofps&gt;</dt>
<dd> For each ifps input frames the filter will output ofps frames. The ratio of ifps/ofps should match the -fps/-ofps ratio. This could be used to filter movies that are broadcast on TV at a frame rate different from their original framerate.</dd>
<dt>luma_only=&lt;n&gt;</dt>
<dd> If n is nonzero, the chroma plane is copied unchanged. This is useful for YV12 sampled TV, which discards one of the chroma fields.</dd>
<dt>mmx2=&lt;n&gt;</dt>
<dd> On x86, if n=1, use MMX2 optimized functions, if n=2, use 3DNow! optimized functions, otherwise, use plain C. If this option is not specified, MMX2 and 3DNow! are auto-detected, use this option to override auto-detection.</dd>
<dt>fast=&lt;n&gt;</dt>
<dd> The larger n will speed up the filter at the expense of accuracy. The default value is n=3. If n is odd, a frame immediately following a frame marked with the REPEAT_FIRST_FIELD MPEG flag is assumed to be progressive, thus filter will not spend any time on soft-telecined MPEG-2 content. This is the only effect of this flag if MMX2 or 3DNow! is available. Without MMX2 and 3DNow, if n=0 or 1, the same calculations will be used as with n=2 or 3. If n=2 or 3, the number of luma levels used to find the frame breaks is reduced from 256 to 128, which results in a faster filter without losing much accuracy. If n=4 or 5, a faster, but much less accurate metric will be used to find the frame breaks, which is more likely to misdetect high vertical detail as interlaced content.</dd>
<dt>verbose=&lt;n&gt;</dt>
<dd> If n is nonzero, print the detailed metrics for each frame. Useful for debugging.</dd>
<dt>dint_thres=&lt;n&gt;</dt>
<dd> Deinterlace threshold. Used during de-interlacing of unmatched frames. Larger value means less deinterlacing, use n=256 to completely turn off deinterlacing. Default is n=8.</dd>
<dt>comb_thres=&lt;n&gt;</dt>
<dd> Threshold for comparing a top and bottom fields. Defaults to 128.</dd>
<dt>diff_thres=&lt;n&gt;</dt>
<dd> Threshold to detect temporal change of a field. Default is 128.</dd>
<dt>sad_thres=&lt;n&gt;</dt>
<dd> Sum of Absolute Difference threshold, default is 64.</dd></dl>
</dl>
<dt><code>softpulldown</code></dt>
<dd> This filter works only correct with MEncoder and acts on the MPEG-2 flags used for soft 3:2 pulldown (soft telecine). If you want to use the ivtc or detc filter on movies that are partly soft telecined, inserting this filter before them should make them more reliable.</dd>
<dt><code>divtc[=options]</code></dt>
<dd> Inverse telecine for deinterlaced video. If 3:2-pulldown telecined video has lost one of the fields or is deinterlaced using a method that keeps one field and interpolates the other, the result is a juddering video that has every fourth frame duplicated. This filter is intended to find and drop those duplicates and restore the original film framerate. When using this filter, you must specify -ofps that is 4/5 of the fps of the input file and place the softskip later in the filter chain to make sure that divtc sees all the frames. Two different modes are available: One pass mode is the default and is straightforward to use, but has the disadvantage that any changes in the telecine phase (lost frames or bad edits) cause momentary judder until the filter can resync again. Two pass mode avoids this by analyzing the whole video beforehand so it will have forward knowledge about the phase changes and can resync at the exact spot. These passes do <code>not</code> correspond to pass one and two of the encoding process. You must run an extra pass using divtc pass one before the actual encoding throwing the resulting video away. Use -nosound -ovc raw -o /dev/null to avoid wasting CPU power for this pass. You may add something like crop=2:2:0:0 after divtc to speed things up even more. Then use divtc pass two for the actual encoding. If you use multiple encoder passes, use divtc pass two for all of them. The options are:</dd>
<dl>
<dl>
<dt>pass=1|2</dt>
<dd> Use two pass mode.</dd>
<dt>file=&lt;filename&gt;</dt>
<dd> Set the two pass log filename (default: &quot;framediff.log&quot;).</dd>
<dt>threshold=&lt;value&gt;</dt>
<dd> Set the minimum strength the telecine pattern must have for the filter to believe in it (default: 0.5). This is used to avoid recognizing false pattern from the parts of the video that are very dark or very still.</dd>
<dt>window=&lt;numframes&gt;</dt>
<dd> Set the number of past frames to look at when searching for pattern (default: 30). Longer window improves the reliability of the pattern search, but shorter window improves the reaction time to the changes in the telecine phase. This only affects the one pass mode. The two pass mode currently uses fixed window that extends to both future and past.</dd>
<dt>phase=0|1|2|3|4</dt>
<dd> Sets the initial telecine phase for one pass mode (default: 0). The two pass mode can see the future, so it is able to use the correct phase from the beginning, but one pass mode can only guess. It catches the correct phase when it finds it, but this option can be used to fix the possible juddering at the beginning. The first pass of the two pass mode also uses this, so if you save the output from the first pass, you get constant phase result.</dd>
<dt>deghost=&lt;value&gt;</dt>
<dd> Set the deghosting threshold (0-255 for one pass mode, -255-255 for two pass mode, default 0). If nonzero, deghosting mode is used. This is for video that has been deinterlaced by blending the fields together instead of dropping one of the fields. Deghosting amplifies any compression artifacts in the blended frames, so the parameter value is used as a threshold to exclude those pixels from deghosting that differ from the previous frame less than specified value. If two pass mode is used, then negative value can be used to make the filter analyze the whole video in the beginning of pass-2 to determine whether it needs deghosting or not and then select either zero or the absolute value of the parameter. Specify this option for pass-2, it makes no difference on pass-1.</dd></dl>
</dl>
<dt><code>phase[=t|b|p|a|u|T|B|A|U][:v]</code></dt>
<dd> Delay interlaced video by one field time so that the field order changes. The intended use is to fix PAL movies that have been captured with the opposite field order to the film-to-video transfer. The options are:</dd>
<dl>
<dl>
<dt>t</dt>
<dd> Capture field order top-first, transfer bottom-first. Filter will delay the bottom field.</dd>
<dt>b</dt>
<dd> Capture bottom-first, transfer top-first. Filter will delay the top field.</dd>
<dt>p</dt>
<dd> Capture and transfer with the same field order. This mode only exists for the documentation of the other options to refer to, but if you actually select it, the filter will faithfully do nothing ;-)</dd>
<dt>a</dt>
<dd> Capture field order determined automatically by field flags, transfer opposite. Filter selects among t and b modes on a frame by frame basis using field flags. If no field information is available, then this works just like u.</dd>
<dt>u</dt>
<dd> Capture unknown or varying, transfer opposite. Filter selects among t and b on a frame by frame basis by analyzing the images and selecting the alternative that produces best match between the fields.</dd>
<dt>T</dt>
<dd> Capture top-first, transfer unknown or varying. Filter selects among t and p using image analysis.</dd>
<dt>B</dt>
<dd> Capture bottom-first, transfer unknown or varying. Filter selects among b and p using image analysis.</dd>
<dt>A</dt>
<dd> Capture determined by field flags, transfer unknown or varying. Filter selects among t, b and p using field flags and image analysis. If no field information is available, then this works just like U. This is the default mode.</dd>
<dt>U</dt>
<dd> Both capture and transfer unknown or varying. Filter selects among t, b and p using image analysis only.</dd>
<dt>v</dt>
<dd> Verbose operation. Prints the selected mode for each frame and the average squared difference between fields for t, b, and p alternatives.</dd></dl>
</dl>
<dt><code>telecine[=start]</code></dt>
<dd> Apply 3:2 &#8216;telecine&#8217; process to increase framerate by 20%. This most likely will not work correctly with MPlayer, but it can be used with &#8216;mencoder -fps 30000/1001 -ofps 30000/1001 -vf telecine&#8217;. Both fps options are essential! (A/V sync will break if they are wrong.) The optional start parameter tells the filter where in the telecine pattern to start (0-3).</dd>
<dt><code>tinterlace[=mode]</code></dt>
<dd> Temporal field interlacing &#8211; merge pairs of frames into an interlaced frame, halving the framerate. Even frames are moved into the upper field, odd frames to the lower field. This can be used to fully reverse the effect of the tfields filter (in mode 0). Available modes are:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Move odd frames into the upper field, even into the lower field, generating a full-height frame at half framerate.</dd>
<dt>1</dt>
<dd> Only output odd frames, even frames are dropped; height unchanged.</dd>
<dt>2</dt>
<dd> Only output even frames, odd frames are dropped; height unchanged.</dd>
<dt>3</dt>
<dd> Expand each frame to full height, but pad alternate lines with black; framerate unchanged.</dd>
<dt>4</dt>
<dd> Interleave even lines from even frames with odd lines from odd frames. Height unchanged at half framerate.</dd></dl>
</dl>
<dt><code>tfields[=mode[:field_dominance]]</code></dt>
<dd> Temporal field separation &#8211; split fields into frames, doubling the output framerate. Like the telecine filter, tfields might not work completely right unless used with MEncoder and both -fps and -ofps set to the desired (double) framerate!</dd>
<dl>
<dl>
<dt>&lt;mode&gt;</dt>
<dd> 0: Leave fields unchanged (will jump/flicker).<br />
 1: Interpolate missing lines. (The algorithm used might not be so good.)<br />
 2: Translate fields by 1/4 pixel with linear interpolation (no jump).<br />
 4: Translate fields by 1/4 pixel with 4tap filter (higher quality) (default).</dd>
<dt>&lt;field_dominance&gt;&nbsp;(DEPRECATED)</dt>
<dd> -1: auto (default) Only works if the decoder exports the appropriate information and no other filters which discard that information come before tfields in the filter chain, otherwise it falls back to 0 (top field first).<br />
 0: top field first<br />
 1: bottom field first<br />
 <i>NOTE:</i> This option will possibly be removed in a future version. Use -field-dominance instead.</dd></dl>
</dl>
<dt><code>yadif=[mode[:field_dominance]]</code></dt>
<dd> Yet another deinterlacing filter</dd>
<dl>
<dl>
<dt>&lt;mode&gt;</dt>
<dd> 0: Output 1 frame for each frame.<br />
 1: Output 1 frame for each field.<br />
 2: Like 0 but skips spatial interlacing check.<br />
 3: Like 1 but skips spatial interlacing check.</dd>
<dt>&lt;field_dominance&gt;&nbsp;(DEPRECATED)</dt>
<dd> Operates like tfields.<br />
 <i>NOTE:</i> This option will possibly be removed in a future version. Use -field-dominance instead.</dd></dl>
</dl>
<dt><code>mcdeint=[mode[:parity[:qp]]]</code></dt>
<dd> Motion compensating deinterlacer. It needs one field per frame as input and must thus be used together with tfields=1 or yadif=1/3 or equivalent.</dd>
<dl>
<dl>
<dt>&lt;mode&gt;</dt>
<dd> 0: fast<br />
 1: medium<br />
 2: slow, iterative motion estimation<br />
 3: extra slow, like 2 plus multiple reference frames</dd>
<dt>&lt;parity&gt;</dt>
<dd> 0 or 1 selects which field to use (note: no autodetection yet!).</dd>
<dt>&lt;qp&gt;&nbsp;</dt>
<dd> Higher values should result in a smoother motion vector field but less optimal individual vectors.</dd></dl>
</dl>
<dt><code>boxblur=radius:power[:radius:power]</code></dt>
<dd> box blur</dd>
<dl>
<dl>
<dt>&lt;radius&gt;</dt>
<dd> blur filter strength</dd>
<dt>&lt;power&gt;</dt>
<dd> number of filter applications</dd></dl>
</dl>
<dt><code>sab=radius:pf:colorDiff[:radius:pf:colorDiff]</code></dt>
<dd> shape adaptive blur</dd>
<dl>
<dl>
<dt>&lt;radius&gt;</dt>
<dd> blur filter strength (~0.1-4.0) (slower if larger)</dd>
<dt>&lt;pf&gt;&nbsp;</dt>
<dd> prefilter strength (~0.1-2.0)</dd>
<dt>&lt;colorDiff&gt;</dt>
<dd> maximum difference between pixels to still be considered (~0.1-100.0)</dd></dl>
</dl>
<dt><code>smartblur=radius:strength:threshold[:radius:strength:threshold]</code></dt>
<dd> smart blur</dd>
<dl>
<dl>
<dt>&lt;radius&gt;</dt>
<dd> blur filter strength (~0.1-5.0) (slower if larger)</dd>
<dt>&lt;strength&gt;</dt>
<dd> blur (0.0-1.0) or sharpen (-1.0-0.0)</dd>
<dt>&lt;threshold&gt;</dt>
<dd> filter all (0), filter flat areas (0-30) or filter edges (-30-0)</dd></dl>
</dl>
<dt><code>perspective=x0:y0:x1:y1:x2:y2:x3:y3:t</code></dt>
<dd> Correct the perspective of movies not filmed perpendicular to the screen.</dd>
<dl>
<dl>
<dt>&lt;x0&gt;,&lt;y0&gt;,&#8230;</dt>
<dd> coordinates of the top left, top right, bottom left, bottom right corners</dd>
<dt>&lt;t&gt;&nbsp;<wbr>&nbsp;</dt>
<dd> linear (0) or cubic resampling (1)</dd></dl>
</dl>
<dt><code>2xsai&nbsp;<wbr>&nbsp;</code></dt>
<dd> Scale and smooth the image with the 2x scale and interpolate algorithm.</dd>
<dt><code>1bpp&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> 1bpp bitmap to YUV/BGR 8/15/16/32 conversion</dd>
<dt><code>down3dright[=lines]</code></dt>
<dd> Reposition and resize stereoscopic images. Extracts both stereo fields and places them side by side, resizing them to maintain the original movie aspect.</dd>
<dl>
<dl>
<dt>&lt;lines&gt;</dt>
<dd> number of lines to select from the middle of the image (default: 12)</dd></dl>
</dl>
<dt><code>bmovl=hidden:opaque:fifo</code></dt>
<dd> The bitmap overlay filter reads bitmaps from a FIFO and displays them on top of the movie, allowing some transformations on the image. Also see TOOLS/bmovl-test.c for a small bmovl test program.</dd>
<dl>
<dl>
<dt>&lt;hidden&gt;</dt>
<dd> Set the default value of the &#8216;hidden&#8217; flag (0=visible, 1=hidden).</dd>
<dt>&lt;opaque&gt;</dt>
<dd> Set the default value of the &#8216;opaque&#8217; flag (0=transparent, 1=opaque).</dd>
<dt>&lt;fifo&gt;</dt>
<dd> path/filename for the FIFO (named pipe connecting &#8216;mplayer -vf bmovl&#8217; to the controlling application)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> FIFO commands are:</dd></dl>
<dl>
<dl>
<dt>RGBA32 width height xpos ypos alpha clear</dt>
<dd> followed by width*height*4 Bytes of raw RGBA32 data.</dd>
<dt>ABGR32 width height xpos ypos alpha clear</dt>
<dd> followed by width*height*4 Bytes of raw ABGR32 data.</dd>
<dt>RGB24 width height xpos ypos alpha clear</dt>
<dd> followed by width*height*3 Bytes of raw RGB24 data.</dd>
<dt>BGR24 width height xpos ypos alpha clear</dt>
<dd> followed by width*height*3 Bytes of raw BGR24 data.</dd>
<dt>ALPHA width height xpos ypos alpha</dt>
<dd> Change alpha transparency of the specified area.</dd>
<dt>CLEAR width height xpos ypos</dt>
<dd> Clear area.</dd>
<dt>OPAQUE</dt>
<dd> Disable all alpha transparency. Send &quot;ALPHA 0 0 0 0 0&quot; to enable it again.</dd>
<dt>HIDE&nbsp;</dt>
<dd> Hide bitmap.</dd>
<dt>SHOW&nbsp;</dt>
<dd> Show bitmap.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Arguments are:</dd></dl>
<dl>
<dl>
<dt>&lt;width&gt;, &lt;height&gt;</dt>
<dd> image/area size</dd>
<dt>&lt;xpos&gt;, &lt;ypos&gt;</dt>
<dd> Start blitting at position x/y.</dd>
<dt>&lt;alpha&gt;</dt>
<dd> Set alpha difference. If you set this to -255 you can then send a sequence of ALPHA-commands to set the area to -225, -200, -175 etc for a nice fade-in-effect! ;)</dd>
<dl>
<dt>
</dt><dd> 0: same as original<br />
 255: Make everything opaque.<br />
 -255: Make everything transparent.</dd></dl>
<dt>&lt;clear&gt;</dt>
<dd> Clear the framebuffer before blitting.</dd>
<dl>
<dt>
</dt><dd> 0: The image will just be blitted on top of the old one, so you do not need to send 1.8MB of RGBA32 data every time a small part of the screen is updated.<br />
 1: clear</dd></dl>
</dl>
</dl>
<dt><code>framestep=I|[i]step</code></dt>
<dd> Renders only every nth frame or every intra frame (keyframe). </dd>
<p> If you call the filter with I (uppercase) as the parameter, then <code>only</code> keyframes are rendered. For DVDs it generally means one in every 15/12 frames (IBBPBBPBBPBBPBB), for AVI it means every scene change or every keyint value (see -lavcopts keyint= value if you use MEncoder to encode the video). </p>
<p> When a keyframe is found, an &#8216;I!&#8217; string followed by a newline character is printed, leaving the current line of MPlayer/MEncoder output on the screen, because it contains the time (in seconds) and frame number of the keyframe (You can use this information to split the AVI.). </p>
<p> If you call the filter with a numeric parameter &#8216;step&#8217; then only one in every &#8216;step&#8217; frames is rendered. </p>
<p> If you put an &#8216;i&#8217; (lowercase) before the number then an &#8216;I!&#8217; is printed (like the I parameter). </p>
<p> If you give only the i then nothing is done to the frames, only I! is printed.</p>
<dt><code>tile=xtiles:ytiles:output:start:delta</code></dt>
<dd> Tile a series of images into a single, bigger image. If you omit a parameter or use a value less than 0, then the default value is used. You can also stop when you are satisfied (&#8230; -vf tile=10:5 &#8230;). It is probably a good idea to put the scale filter before the tile :-) </dd>
<p> The parameters are: </p>
<dl>
<dl>
<dt>&lt;xtiles&gt;</dt>
<dd> number of tiles on the x axis (default: 5)</dd>
<dt>&lt;ytiles&gt;</dt>
<dd> number of tiles on the y axis (default: 5)</dd>
<dt>&lt;output&gt;</dt>
<dd> Render the tile when &#8216;output&#8217; number of frames are reached, where &#8216;output&#8217; should be a number less than xtile * ytile. Missing tiles are left blank. You could, for example, write an 8 * 7 tile every 50 frames to have one image every 2 seconds @ 25 fps.</dd>
<dt>&lt;start&gt;</dt>
<dd> outer border thickness in pixels (default: 2)</dd>
<dt>&lt;delta&gt;</dt>
<dd> inner border thickness in pixels (default: 4)</dd></dl>
</dl>
<dt><code>delogo[=x:y:w:h:t]</code></dt>
<dd> Suppresses a TV station logo by a simple interpolation of the surrounding pixels. Just set a rectangle covering the logo and watch it disappear (and sometimes something even uglier appear &#8211; your mileage may vary).</dd>
<dl>
<dl>
<dt>&lt;x&gt;,&lt;y&gt;</dt>
<dd> top left corner of the logo</dd>
<dt>&lt;w&gt;,&lt;h&gt;</dt>
<dd> width and height of the cleared rectangle</dd>
<dt>&lt;t&gt;</dt>
<dd> Thickness of the fuzzy edge of the rectangle (added to w and h). When set to -1, a green rectangle is drawn on the screen to simplify finding the right x,y,w,h parameters.</dd>
<dt>file=&lt;file&gt;</dt>
<dd> You can specify a text file to load the coordinates from. Each line must have a timestamp (in seconds, and in ascending order) and the &quot;x:y:w:h:t&quot; coordinates (t can be omitted).</dd></dl>
</dl>
<dt><code>remove-logo=/path/to/logo_bitmap_file_name.pgm</code></dt>
<dd> Suppresses a TV station logo, using a PGM or PPM image file to determine which pixels comprise the logo. The width and height of the image file must match those of the video stream being processed. Uses the filter image and a circular blur algorithm to remove the logo.</dd>
<dl>
<dl>
<dt>/path/to/logo_bitmap_file_name.pgm</dt>
<dd> [path] + filename of the filter image.</dd></dl>
</dl>
<dt><code>zrmjpeg[=options]</code></dt>
<dd> Software YV12 to MJPEG encoder for use with the zr2 video output device.</dd>
<dl>
<dl>
<dt>maxheight=&lt;h&gt;|maxwidth=&lt;w&gt;</dt>
<dd> These options set the maximum width and height the zr card can handle (the MPlayer filter layer currently cannot query those).</dd>
<dt>{dc10+,dc10,buz,lml33}-{PAL|NTSC}</dt>
<dd> Use these options to set maxwidth and maxheight automatically to the values known for card/mode combo. For example, valid options are: dc10-PAL and buz-NTSC (default: dc10+PAL)</dd>
<dt>color|bw</dt>
<dd> Select color or black and white encoding. Black and white encoding is faster. Color is the default.</dd>
<dt>hdec={1,2,4}</dt>
<dd> Horizontal decimation 1, 2 or 4.</dd>
<dt>vdec={1,2,4}</dt>
<dd> Vertical decimation 1, 2 or 4.</dd>
<dt>quality=1-20</dt>
<dd> Set JPEG compression quality [BEST] 1 &#8211; 20 [VERY BAD].</dd>
<dt>fd|nofd</dt>
<dd> By default, decimation is only performed if the Zoran hardware can upscale the resulting MJPEG images to the original size. The option fd instructs the filter to always perform the requested decimation (ugly).</dd></dl>
</dl>
<dt><code>screenshot=prefix</code></dt>
<dd> Allows acquiring screenshots of the movie using slave mode commands that can be bound to keypresses. See the slave mode documentation and the INTERACTIVE CONTROL section for details. By default files named &#8216;shotNNNN.png&#8217; will be saved in the working directory, using the first available number &#8211; no files will be overwritten. Specify a prefix to change the name or location, e.g. -vf screenshot=shots/now will save the files in the directory shots with nowNNNN.png as name. The filter has no overhead when not used and accepts an arbitrary colorspace, so it is safe to add it to the configuration file. Make sure that the screenshot filter is added after all other filters whose effect you want to record on the saved image. E.g. it should be the last filter if you want to have an exact screenshot of what you see on the monitor.</dd>
<dt><code>ass&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Moves SSA/ASS subtitle rendering to an arbitrary point in the filter chain. Only useful with the -ass option. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-vf ass,screenshot</dt>
<dd> Moves SSA/ASS rendering before the screenshot filter. Screenshots taken this way will contain subtitles.</dd></dl>
</dl>
<dt><code>blackframe[=amount:threshold]</code></dt>
<dd> Detect frames that are (almost) completely black. Can be useful to detect chapter transitions or commercials. Output lines consist of the frame number of the detected frame, the percentage of blackness, the frame type and the frame number of the last encountered keyframe.</dd>
<dl>
<dl>
<dt>&lt;amount&gt;</dt>
<dd> Percentage of the pixels that have to be below the threshold (default: 98).</dd>
<dt>&lt;threshold&gt;</dt>
<dd> Threshold below which a pixel value is considered black (default: 32).</dd></dl>
</dl>
<dt><code>stereo3d[=in:out]</code></dt>
<dd> Stereo3d converts between different stereoscopic image formats.</dd>
<dl>
<dl>
<dt>&lt;in&gt;</dt>
<dd> Stereoscopic image format of input. Possible values:</dd>
<dl>
<dt>
</dt><dd> <code>sbsl or side_by_side_left_first</code></dd>
<dl>
<dt>
</dt><dd> side by side parallel (left eye left, right eye right)</dd></dl>
<p> <code>sbsr or side_by_side_right_first</code></p>
<dl>
<dt>
</dt><dd> side by side crosseye (right eye left, left eye right)</dd></dl>
<p> <code>sbs2l or side_by_side_half_width_left_first</code></p>
<dl>
<dt>
</dt><dd> side by side with half width resolution (left eye left, right eye right)</dd></dl>
<p> <code>sbs2r or side_by_side_half_width_right_first</code></p>
<dl>
<dt>
</dt><dd> side by side with half width resolution (right eye left, left eye right)</dd></dl>
<p> <code>abl or above_below_left_first</code></p>
<dl>
<dt>
</dt><dd> above-below (left eye above, right eye below)</dd></dl>
<p> <code>abl or above_below_right_first</code></p>
<dl>
<dt>
</dt><dd> above-below (right eye above, left eye below)</dd></dl>
<p> <code>ab2l or above_below_half_height_left_first</code></p>
<dl>
<dt>
</dt><dd> above-below with half height resolution (left eye above, right eye below)</dd></dl>
<p> <code>ab2r or above_below_half_height_right_first</code></p>
<dl>
<dt>
</dt><dd> above-below with half height resolution (right eye above, left eye below)</dd></dl>
</dl>
<dt>&lt;out&gt;</dt>
<dd> Stereoscopic image format of output. Possible values are all the input formats as well as:</dd>
<dl>
<dt>
</dt><dd> <code>arcg or anaglyph_red_cyan_gray</code></dd>
<dl>
<dt>
</dt><dd> anaglyph red/cyan gray (red filter on left eye, cyan filter on right eye)</dd></dl>
<p> <code>arch or anaglyph_red_cyan_half_color</code></p>
<dl>
<dt>
</dt><dd> anaglyph red/cyan half colored (red filter on left eye, cyan filter on right eye)</dd></dl>
<p> <code>arcc or anaglyph_red_cyan_color</code></p>
<dl>
<dt>
</dt><dd> anaglyph red/cyan color (red filter on left eye, cyan filter on right eye)</dd></dl>
<p> <code>arcd or anaglyph_red_cyan_dubois</code></p>
<dl>
<dt>
</dt><dd> anaglyph red/cyan color optimized with the least squares projection of dubois (red filter on left eye, cyan filter on right eye)</dd></dl>
<p> <code>agmg or anaglyph_green_magenta_gray</code></p>
<dl>
<dt>
</dt><dd> anaglyph green/magenta gray (green filter on left eye, magenta filter on right eye)</dd></dl>
<p> <code>agmh or anaglyph_green_magenta_half_color</code></p>
<dl>
<dt>
</dt><dd> anaglyph green/magenta half colored (green filter on left eye, magenta filter on right eye)</dd></dl>
<p> <code>agmc or anaglyph_green_magenta_color</code></p>
<dl>
<dt>
</dt><dd> anaglyph green/magenta colored (green filter on left eye, magenta filter on right eye)</dd></dl>
<p> <code>aybg or anaglyph_yellow_blue_gray</code></p>
<dl>
<dt>
</dt><dd> anaglyph yellow/blue gray (yellow filter on left eye, blue filter on right eye)</dd></dl>
<p> <code>aybh or anaglyph_yellow_blue_half_color</code></p>
<dl>
<dt>
</dt><dd> anaglyph yellow/blue half colored (yellow filter on left eye, blue filter on right eye)</dd></dl>
<p> <code>aybc or anaglyph_yellow_blue_color</code></p>
<dl>
<dt>
</dt><dd> anaglyph yellow/blue colored (yellow filter on left eye, blue filter on right eye)</dd></dl>
<p> <code>irl or interleave_rows_left_first</code></p>
<dl>
<dt>
</dt><dd> Interleaved rows (left eye has top row, right eye starts on next row)</dd></dl>
<p> <code>irr or interleave_rows_right_first</code></p>
<dl>
<dt>
</dt><dd> Interleaved rows (right eye has top row, left eye starts on next row)</dd></dl>
<p> <code>ml or mono_left</code></p>
<dl>
<dt>
</dt><dd> mono output (left eye only)</dd></dl>
<p> <code>mr or mono_right</code></p>
<dl>
<dt>
</dt><dd> mono output (right eye only)</dd></dl>
</dl>
<p> <i>NOTE:</i> To use either of the interleaved-rows output formats to display full-screen on a row-interleaved 3D display, you will need to scale the video to the correct height first using the &quot;scale&quot; filter, if it is not already the right height. Typically, that is 1080 rows (so use e.g. &quot;-vf scale=1440:1080,stereo3d=sbsl:irl&quot; for a 720p side-by-side encoded movie).</dl>
</dl>
<dt><code>gradfun[=strength[:radius]]</code></dt>
<dd> Fix the banding artifacts that are sometimes introduced into nearly flat regions by truncation to 8bit colordepth. Interpolates the gradients that should go where the bands are, and dithers them. </dd>
<p> This filter is designed for playback only. Do not use it prior to lossy compression, because compression tends to lose the dither and bring back the bands.</p>
<dl>
<dl>
<dt>&lt;strength&gt;</dt>
<dd> Maximum amount by which the filter will change any one pixel. Also the threshold for detecting nearly flat regions (default: 1.2).</dd>
<dt>&lt;radius&gt;</dt>
<dd> Neighborhood to fit the gradient to. Larger radius makes for smoother gradients, but also prevents the filter from modifying pixels near detailed regions (default: 16).</dd></dl>
</dl>
<dt><code>fixpts[=options]</code></dt>
<dd> Fixes the presentation timestamps (PTS) of the frames. By default, the PTS passed to the next filter is dropped, but the following options can change that:</dd>
<dl>
<dl>
<dt>print</dt>
<dd> Print the incoming PTS.</dd>
<dt>fps=&lt;fps&gt;</dt>
<dd> Specify a frame per second value.</dd>
<dt>start=&lt;pts&gt;</dt>
<dd> Specify an initial value for the PTS.</dd>
<dt>autostart=&lt;n&gt;</dt>
<dd> Uses the <i>n</i>th incoming PTS as the initial PTS. All previous PTS are kept, so setting a huge value or -1 keeps the PTS intact.</dd>
<dt>autofps=&lt;n&gt;</dt>
<dd> Uses the <i>n</i>th incoming PTS after the end of autostart to determine the framerate.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>-vf fixpts=fps=24000/1001,ass,fixpts</dt>
<dd> Generates a new sequence of PTS, uses it for ASS subtitles, then drops it. Generating a new sequence is useful when the timestamps are reset during the program; this is frequent on DVDs. Dropping it may be necessary to avoid confusing encoders.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>NOTE:</i> Using this filter together with any sort of seeking (including -ss and EDLs) may make demons fly out of your nose.</dd></dl>
</dl>
<h2>GENERAL ENCODING OPTIONS (MENCODER ONLY)</h2>
<dl>
<dt><code>-audio-delay &lt;any floating-point number&gt;</code></dt>
<dd> Delays either audio or video by setting a delay field in the header (default: 0.0). This does not delay either stream while encoding, but the player will see the delay field and compensate accordingly. Positive values delay the audio, and negative values delay the video. Note that this is the exact opposite of the -delay option. For example, if a video plays correctly with -delay 0.2, you can fix the video with MEncoder by using -audio-delay -0.2. </dd>
<p> Currently, this option only works with the default muxer (-of avi). If you are using a different muxer, then you must use -delay instead.</p>
<dt><code>-audio-density &lt;1-50&gt;</code></dt>
<dd> Number of audio chunks per second (default is 2 for 0.5s long audio chunks).<br />
 <i>NOTE:</i> CBR only, VBR ignores this as it puts each packet in a new chunk.</dd>
<dt><code>-audio-preload &lt;0.0-2.0&gt;</code></dt>
<dd> Sets up the audio buffering time interval (default: 0.5s).</dd>
<dt><code>-fafmttag &lt;format&gt;</code></dt>
<dd> Can be used to override the audio format tag of the output file. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-fafmttag 0x55</dt>
<dd> Will have the output file contain 0x55 (mp3) as audio format tag.</dd></dl>
</dl>
<dt><code>-ffourcc &lt;fourcc&gt;</code></dt>
<dd> Can be used to override the video fourcc of the output file. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-ffourcc div3</dt>
<dd> Will have the output file contain &#8216;div3&#8217; as video fourcc.</dd></dl>
</dl>
<dt><code>-force-avi-aspect &lt;0.2-3.0&gt;</code></dt>
<dd> Override the aspect stored in the AVI OpenDML vprp header. This can be used to change the aspect ratio with &#8216;-ovc copy&#8217;.</dd>
<dt><code>-frameno-file &lt;filename&gt; (DEPRECATED)</code></dt>
<dd> Specify the name of the audio file with framenumber mappings created in the first (audio only) pass of a special three pass encoding mode.<br />
 <i>NOTE:</i> Using this mode will most likely give you A-V desync. Do not use it. It is kept for backwards compatibility only and will possibly be removed in a future version.</dd>
<dt><code>-hr-edl-seek</code></dt>
<dd> Use a more precise, but much slower method for skipping areas. Areas marked for skipping are not seeked over, instead all frames are decoded, but only the necessary frames are encoded. This allows starting at non-keyframe boundaries.<br />
 <i>NOTE:</i> Not guaranteed to work right with &#8216;-ovc copy&#8217;.</dd>
<dt><code>-info &lt;option1:option2:&#8230;&gt; (AVI only)</code></dt>
<dd> Specify the info header of the resulting AVI file. </dd>
<p> Available options are:</p>
<dl>
<dl>
<dt>help&nbsp;</dt>
<dd> Show this description.</dd>
<dt>name=&lt;value&gt;</dt>
<dd> title of the work</dd>
<dt>artist=&lt;value&gt;</dt>
<dd> artist or author of the work</dd>
<dt>genre=&lt;value&gt;</dt>
<dd> original work category</dd>
<dt>subject=&lt;value&gt;</dt>
<dd> contents of the work</dd>
<dt>copyright=&lt;value&gt;</dt>
<dd> copyright information</dd>
<dt>srcform=&lt;value&gt;</dt>
<dd> original format of the digitized material</dd>
<dt>comment=&lt;value&gt;</dt>
<dd> general comments about the work</dd></dl>
</dl>
<dt><code>-noautoexpand</code></dt>
<dd> Do not automatically insert the expand filter into the MEncoder filter chain. Useful to control at which point of the filter chain subtitles are rendered when hardcoding subtitles onto a movie.</dd>
<dt><code>-noencodedups</code></dt>
<dd> Do not attempt to encode duplicate frames in duplicate; always output zero-byte frames to indicate duplicates. Zero-byte frames will be written anyway unless a filter or encoder capable of doing duplicate encoding is loaded. Currently the only such filter is harddup.</dd>
<dt><code>-noodml (-of avi only)</code></dt>
<dd> Do not write OpenDML index for AVI files &gt;1GB.</dd>
<dt><code>-noskip</code></dt>
<dd> Do not skip frames.</dd>
<dt><code>-o &lt;filename&gt;</code></dt>
<dd> Outputs to the given filename.<br />
 If you want a default output filename, you can put this option in the MEncoder config file.</dd>
<dt><code>-oac &lt;codec name&gt;</code></dt>
<dd> Encode with the given audio codec (no default set).<br />
 <i>NOTE:</i> Use -oac help to get a list of available audio codecs. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-oac copy</dt>
<dd> no encoding, just streamcopy</dd>
<dt>-oac pcm</dt>
<dd> Encode to uncompressed PCM.</dd>
<dt>-oac mp3lame</dt>
<dd> Encode to MP3 (using LAME).</dd>
<dt>-oac lavc</dt>
<dd> Encode with a libavcodec codec.</dd></dl>
</dl>
<dt><code>-of &lt;format&gt; (BETA CODE!)</code></dt>
<dd> Encode to the specified container format (default: AVI).<br />
 <i>NOTE:</i> Use -of help to get a list of available container formats. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-of avi</dt>
<dd> Encode to AVI.</dd>
<dt>-of mpeg</dt>
<dd> Encode to MPEG (also see -mpegopts).</dd>
<dt>-of lavf</dt>
<dd> Encode with libavformat muxers (also see -lavfopts).</dd>
<dt>-of rawvideo</dt>
<dd> raw video stream (no muxing &#8211; one video stream only)</dd>
<dt>-of rawaudio</dt>
<dd> raw audio stream (no muxing &#8211; one audio stream only)</dd></dl>
</dl>
<dt><code>-ofps &lt;fps&gt;</code></dt>
<dd> Specify a frames per second (fps) value for the output file, which can be different from that of the source material. Must be set for variable fps (ASF, some MOV) and progressive (30000/1001 fps telecined MPEG) files.</dd>
<dt><code>-ovc &lt;codec name&gt;</code></dt>
<dd> Encode with the given video codec (no default set).<br />
 <i>NOTE:</i> Use -ovc help to get a list of available video codecs. </dd>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>-ovc copy</dt>
<dd> no encoding, just streamcopy</dd>
<dt>-ovc raw</dt>
<dd> Encode to an arbitrary uncompressed format (use &#8216;-vf format&#8217; to select).</dd>
<dt>-ovc lavc</dt>
<dd> Encode with a libavcodec codec.</dd></dl>
</dl>
<dt><code>-passlogfile &lt;filename&gt;</code></dt>
<dd> Dump first pass information to &lt;filename&gt; instead of the default divx2pass.log in two pass encoding mode.</dd>
<dt><code>-skiplimit &lt;value&gt;</code></dt>
<dd> Specify the maximum number of frames that may be skipped after encoding one frame (-noskiplimit for unlimited).</dd>
<dt><code>-vobsubout &lt;basename&gt;</code></dt>
<dd> Specify the basename for the output .idx and .sub files. This turns off subtitle rendering in the encoded movie and diverts it to VOBsub subtitle files.</dd>
<dt><code>-vobsuboutid &lt;langid&gt;</code></dt>
<dd> Specify the language two letter code for the subtitles. This overrides what is read from the DVD or the .ifo file.</dd>
<dt><code>-vobsuboutindex &lt;index&gt;</code></dt>
<dd> Specify the index of the subtitles in the output files (default: 0).</dd>
<dt><code>-force-key-frames &lt;time&gt;,&lt;time&gt;,&#8230;</code></dt>
<dd> Force key frames at the specified timestamps, more precisely at the first frame after each specified time. </dd>
<p> This option can be used to ensure that a seek point is present at a chapter mark or any other designated place in the output file. </p>
<p> The timestamps must be specified in ascending order. </p>
<p> Since MEncoder does not send timestamps along the filter chain, you probably need to use the fixpts filter for this option to work. </p>
<p> Not all codecs support forced key frames. Currently, support is only implemented for the following encoders: lavc, x264, xvid.</dl>
<h2>CODEC SPECIFIC ENCODING OPTIONS (MENCODER ONLY)</h2>
<p> You can specify codec specific encoding parameters using the following syntax:</p>
<dl>
<dt><code>-&lt;codec&gt;opts &lt;option1[=value1]:option2[=value2]:&#8230;&gt;</code></dt>
<dd></dd></dl>
<p> Where &lt;codec&gt; may be: lavc, xvidenc, mp3lame, toolame, twolame, nuv, xvfw, faac, x264enc, mpeg, lavf.</p>
<h3>mp3lame (-lameopts)</h3>
<dl>
<dt><code>help&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> get help</dd>
<dt><code>vbr=&lt;0-4&gt;</code></dt>
<dd> variable bitrate method</dd>
<dl>
<dl>
<dt>0</dt>
<dd> cbr</dd>
<dt>1</dt>
<dd> mt</dd>
<dt>2</dt>
<dd> rh (default)</dd>
<dt>3</dt>
<dd> abr</dd>
<dt>4</dt>
<dd> mtrh</dd></dl>
</dl>
<dt><code>abr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> average bitrate</dd>
<dt><code>cbr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> constant bitrate Also forces CBR mode encoding on subsequent ABR presets modes.</dd>
<dt><code>br=&lt;0-1024&gt;</code></dt>
<dd> bitrate in kbps (CBR and ABR only)</dd>
<dt><code>q=&lt;0-9&gt;</code></dt>
<dd> quality (0 &#8211; highest, 9 &#8211; lowest) (VBR only)</dd>
<dt><code>aq=&lt;0-9&gt;</code></dt>
<dd> algorithmic quality (0 &#8211; best/slowest, 9 &#8211; worst/fastest)</dd>
<dt><code>ratio=&lt;1-100&gt;</code></dt>
<dd> compression ratio</dd>
<dt><code>vol=&lt;0-10&gt;</code></dt>
<dd> audio input gain</dd>
<dt><code>mode=&lt;0-3&gt;</code></dt>
<dd> (default: auto)</dd>
<dl>
<dl>
<dt>0</dt>
<dd> stereo</dd>
<dt>1</dt>
<dd> joint-stereo</dd>
<dt>2</dt>
<dd> dualchannel</dd>
<dt>3</dt>
<dd> mono</dd></dl>
</dl>
<dt><code>padding=&lt;0-2&gt;</code></dt>
<dd>
</dd><dl>
<dl>
<dt>0</dt>
<dd> none</dd>
<dt>1</dt>
<dd> all</dd>
<dt>2</dt>
<dd> adjust</dd></dl>
</dl>
<dt><code>fast&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Switch on faster encoding on subsequent VBR presets modes. This results in slightly lower quality and higher bitrates.</dd>
<dt><code>highpassfreq=&lt;freq&gt;</code></dt>
<dd> Set a highpass filtering frequency in Hz. Frequencies below the specified one will be cut off. A value of -1 will disable filtering, a value of 0 will let LAME choose values automatically.</dd>
<dt><code>lowpassfreq=&lt;freq&gt;</code></dt>
<dd> Set a lowpass filtering frequency in Hz. Frequencies above the specified one will be cut off. A value of -1 will disable filtering, a value of 0 will let LAME choose values automatically.</dd>
<dt><code>preset=&lt;value&gt;</code></dt>
<dd> preset values</dd>
<dl>
<dl>
<dt>help&nbsp;</dt>
<dd> Print additional options and information about presets settings.</dd>
<dt>medium</dt>
<dd> VBR encoding, good quality, 150-180 kbps bitrate range</dd>
<dt>standard</dt>
<dd> VBR encoding, high quality, 170-210 kbps bitrate range</dd>
<dt>extreme</dt>
<dd> VBR encoding, very high quality, 200-240 kbps bitrate range</dd>
<dt>insane</dt>
<dd> CBR encoding, highest preset quality, 320 kbps bitrate</dd>
<dt>&lt;8-320&gt;</dt>
<dd> ABR encoding at average given kbps bitrate</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLES:</i></dd></dl>
<dl>
<dl>
<dt>fast:preset=standard</dt>
<dd> suitable for most people and most music types and already quite high quality</dd>
<dt>cbr:preset=192</dt>
<dd> Encode with ABR presets at a 192 kbps forced constant bitrate.</dd>
<dt>preset=172</dt>
<dd> Encode with ABR presets at a 172 kbps average bitrate.</dd>
<dt>preset=extreme</dt>
<dd> for people with extremely good hearing and similar equipment</dd></dl>
</dl>
</dl>
<h3>toolame and twolame (-toolameopts and -twolameopts respectively)</h3>
<dl>
<dt><code>br=&lt;32-384&gt;</code></dt>
<dd> In CBR mode this parameter indicates the bitrate in kbps, when in VBR mode it is the minimum bitrate allowed per frame. VBR mode will not work with a value below 112.</dd>
<dt><code>vbr=&lt;-50-50&gt; (VBR only)</code></dt>
<dd> variability range; if negative the encoder shifts the average bitrate towards the lower limit, if positive towards the higher. When set to 0 CBR is used (default).</dd>
<dt><code>maxvbr=&lt;32-384&gt; (VBR only)</code></dt>
<dd> maximum bitrate allowed per frame, in kbps</dd>
<dt><code>mode=&lt;stereo | jstereo | mono | dual&gt;</code></dt>
<dd> (default: mono for 1-channel audio, stereo otherwise)</dd>
<dt><code>psy=&lt;-1-4&gt;</code></dt>
<dd> psychoacoustic model (default: 2)</dd>
<dt><code>errprot=&lt;0 | 1&gt;</code></dt>
<dd> Include error protection.</dd>
<dt><code>debug=&lt;0-10&gt;</code></dt>
<dd> debug level</dd></dl>
<h3>faac (-faacopts)</h3>
<dl>
<dt><code>br=&lt;bitrate&gt;</code></dt>
<dd> average bitrate in kbps (mutually exclusive with quality)</dd>
<dt><code>quality=&lt;1-1000&gt;</code></dt>
<dd> quality mode, the higher the better (mutually exclusive with br)</dd>
<dt><code>object=&lt;1-4&gt;</code></dt>
<dd> object type complexity</dd>
<dl>
<dl>
<dt>1</dt>
<dd> MAIN (default)</dd>
<dt>2</dt>
<dd> LOW</dd>
<dt>3</dt>
<dd> SSR</dd>
<dt>4</dt>
<dd> LTP (extremely slow)</dd></dl>
</dl>
<dt><code>mpeg=&lt;2|4&gt;</code></dt>
<dd> MPEG version (default: 4)</dd>
<dt><code>tns&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Enables temporal noise shaping.</dd>
<dt><code>cutoff=&lt;0-sampling_rate/2&gt;</code></dt>
<dd> cutoff frequency (default: sampling_rate/2)</dd>
<dt><code>raw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Stores the bitstream as raw payload with extradata in the container header (default: 0, corresponds to ADTS). Do not set this flag if not explicitly required or you will not be able to remux the audio stream later on.</dd></dl>
<h3>lavc (-lavcopts)</h3>
<p> Many libavcodec (lavc for short) options are tersely documented. Read the source for full details. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>vcodec=msmpeg4:vbitrate=1800:vhq:keyint=250</dt>
<dd></dd></dl>
</dl>
<dl>
<dt><code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></dt>
<dd> Pass AVOptions to libavcodec encoder. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some AVOptions may conflict with MEncoder options. </dd>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>o=bt=100k</dt>
<dd></dd></dl>
</dl>
<dt><code>acodec=&lt;value&gt;</code></dt>
<dd> audio codec (default: mp2)</dd>
<dl>
<dl>
<dt>ac3&nbsp;<wbr>&nbsp;</dt>
<dd> Dolby Digital (AC-3)</dd>
<dt>adpcm_*</dt>
<dd> Adaptive PCM formats &#8211; see the HTML documentation for details.</dd>
<dt>flac&nbsp;</dt>
<dd> Free Lossless Audio Codec (FLAC)</dd>
<dt>g726&nbsp;</dt>
<dd> G.726 ADPCM</dd>
<dt>libfaac</dt>
<dd> Advanced Audio Coding (AAC) &#8211; using FAAC</dd>
<dt>libmp3lame</dt>
<dd> MPEG-1 audio layer 3 (MP3) &#8211; using LAME</dd>
<dt>mp2&nbsp;<wbr>&nbsp;</dt>
<dd> MPEG-1 audio layer 2 (MP2)</dd>
<dt>pcm_*</dt>
<dd> PCM formats &#8211; see the HTML documentation for details.</dd>
<dt>roq_dpcm</dt>
<dd> Id Software RoQ DPCM</dd>
<dt>sonic</dt>
<dd> experimental simple lossy codec</dd>
<dt>sonicls</dt>
<dd> experimental simple lossless codec</dd>
<dt>vorbis</dt>
<dd> Vorbis</dd>
<dt>wmav1</dt>
<dd> Windows Media Audio v1</dd>
<dt>wmav2</dt>
<dd> Windows Media Audio v2</dd></dl>
</dl>
<dt><code>abitrate=&lt;value&gt;</code></dt>
<dd> audio bitrate in kbps (default: 224)</dd>
<dt><code>atag=&lt;value&gt;</code></dt>
<dd> Use the specified Windows audio format tag (e.g. atag=0x55).</dd>
<dt><code>bit_exact</code></dt>
<dd> Use only bit exact algorithms (except (I)DCT). Additionally bit_exact disables several optimizations and thus should only be used for regression tests, which need binary identical files even if the encoder version changes. This also suppresses the user_data header in MPEG-4 streams. Do not use this option unless you know exactly what you are doing.</dd>
<dt><code>threads=&lt;1-8&gt;</code></dt>
<dd> Maximum number of threads to use (default: 1). May have a slight negative effect on motion estimation.</dd>
<dt><code>vcodec=&lt;value&gt;</code></dt>
<dd> Employ the specified codec (default: mpeg4).</dd>
<dl>
<dl>
<dt>asv1&nbsp;</dt>
<dd> ASUS Video v1</dd>
<dt>asv2&nbsp;</dt>
<dd> ASUS Video v2</dd>
<dt>dvvideo</dt>
<dd> Sony Digital Video</dd>
<dt>ffv1&nbsp;</dt>
<dd> FFmpeg&#8217;s lossless video codec</dd>
<dt>ffvhuff</dt>
<dd> nonstandard 20% smaller HuffYUV using YV12</dd>
<dt>flv&nbsp;<wbr>&nbsp;</dt>
<dd> Sorenson H.263 used in Flash Video</dd>
<dt>h261&nbsp;</dt>
<dd> H.261</dd>
<dt>h263&nbsp;</dt>
<dd> H.263</dd>
<dt>h263p</dt>
<dd> H.263+</dd>
<dt>huffyuv</dt>
<dd> HuffYUV</dd>
<dt>libtheora</dt>
<dd> Theora</dd>
<dt>libx264</dt>
<dd> x264 H.264/AVC MPEG-4 Part 10</dd>
<dt>libxvid</dt>
<dd> Xvid MPEG-4 Part 2 (ASP)</dd>
<dt>ljpeg</dt>
<dd> Lossless JPEG</dd>
<dt>mjpeg</dt>
<dd> Motion JPEG</dd>
<dt>mpeg1video</dt>
<dd> MPEG-1 video</dd>
<dt>mpeg2video</dt>
<dd> MPEG-2 video</dd>
<dt>mpeg4</dt>
<dd> MPEG-4 (DivX 4/5)</dd>
<dt>msmpeg4</dt>
<dd> DivX 3</dd>
<dt>msmpeg4v2</dt>
<dd> MS MPEG4v2</dd>
<dt>roqvideo</dt>
<dd> ID Software RoQ Video</dd>
<dt>rv10&nbsp;</dt>
<dd> an old RealVideo codec</dd>
<dt>snow (also see: vstrict)</dt>
<dd> FFmpeg&#8217;s experimental wavelet-based codec</dd>
<dt>svq1&nbsp;</dt>
<dd> Apple Sorenson Video 1</dd>
<dt>wmv1&nbsp;</dt>
<dd> Windows Media Video, version 1 (AKA WMV7)</dd>
<dt>wmv2&nbsp;</dt>
<dd> Windows Media Video, version 2 (AKA WMV8)</dd></dl>
</dl>
<dt><code>vqmin=&lt;1-31&gt;</code></dt>
<dd> minimum quantizer</dd>
<dl>
<dl>
<dt>1</dt>
<dd> Not recommended (much larger file, little quality difference and weird side effects: msmpeg4, h263 will be very low quality, ratecontrol will be confused resulting in lower quality and some decoders will not be able to decode it).</dd>
<dt>2</dt>
<dd> Recommended for normal mpeg4/mpeg1video encoding (default).</dd>
<dt>3</dt>
<dd> Recommended for h263(p)/msmpeg4. The reason for preferring 3 over 2 is that 2 could lead to overflows. (This will be fixed for h263(p) by changing the quantizer per MB in the future, msmpeg4 cannot be fixed as it does not support that.)</dd></dl>
</dl>
<dt><code>lmin=&lt;0.01-255.0&gt;</code></dt>
<dd> Minimum frame-level Lagrange multiplier for ratecontrol (default: 2.0). Lavc will rarely use quantizers below the value of lmin. Lowering lmin will make lavc more likely to choose lower quantizers for some frames, but not lower than the value of vqmin. Likewise, raising lmin will make lavc less likely to choose low quantizers, even if vqmin would have allowed them. You probably want to set lmin approximately equal to vqmin. When adaptive quantization is in use, changing lmin/lmax may have less of an effect; see mblmin/mblmax.</dd>
<dt><code>lmax=&lt;0.01-255.0&gt;</code></dt>
<dd> maximum Lagrange multiplier for ratecontrol (default: 31.0)</dd>
<dt><code>mblmin=&lt;0.01-255.0&gt;</code></dt>
<dd> Minimum macroblock-level Lagrange multiplier for ratecontrol (default:2.0). This parameter affects adaptive quantization options like qprd, lumi_mask, etc..</dd>
<dt><code>mblmax=&lt;0.01-255.0&gt;</code></dt>
<dd> Maximum macroblock-level Lagrange multiplier for ratecontrol (default: 31.0).</dd>
<dt><code>vqscale=&lt;0-31&gt;</code></dt>
<dd> Constant quantizer / constant quality encoding (selects fixed quantizer mode). A lower value means better quality but larger files (default: -1). In case of snow codec, value 0 means lossless encoding. Since the other codecs do not support this, vqscale=0 will have an undefined effect. 1 is not recommended (see vqmin for details).</dd>
<dt><code>vqmax=&lt;1-31&gt;</code></dt>
<dd> Maximum quantizer, 10-31 should be a sane range (default: 31).</dd>
<dt><code>vqdiff=&lt;1-31&gt;</code></dt>
<dd> maximum quantizer difference between consecutive I- or P-frames (default: 3)</dd>
<dt><code>vmax_b_frames=&lt;0-4&gt;</code></dt>
<dd> maximum number of B-frames between non-B-frames:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> no B-frames (default)</dd>
<dt>0-2</dt>
<dd> sane range for MPEG-4</dd></dl>
</dl>
<dt><code>vme=&lt;0-5&gt;</code></dt>
<dd> motion estimation method. Available methods are:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> none (very low quality)</dd>
<dt>1</dt>
<dd> full (slow, currently unmaintained and disabled)</dd>
<dt>2</dt>
<dd> log (low quality, currently unmaintained and disabled)</dd>
<dt>3</dt>
<dd> phods (low quality, currently unmaintained and disabled)</dd>
<dt>4</dt>
<dd> EPZS: size=1 diamond, size can be adjusted with the *dia options (default)</dd>
<dt>5</dt>
<dd> X1 (experimental, currently aliased to EPZS)</dd>
<dt>8</dt>
<dd> iter (iterative overlapped block, only used in snow)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
 <i>NOTE:</i> 0-3 currently ignores the amount of bits spent, so quality may be low.</dd></dl>
<dt><code>me_range=&lt;0-9999&gt;</code></dt>
<dd> motion estimation search range (default: 0 (unlimited))</dd>
<dt><code>mbd=&lt;0-2&gt; (also see *cmp, qpel)</code></dt>
<dd> Macroblock decision algorithm (high quality mode), encode each macro block in all modes and choose the best. This is slow but results in better quality and file size. When mbd is set to 1 or 2, the value of mbcmp is ignored when comparing macroblocks (the mbcmp value is still used in other places though, in particular the motion search algorithms). If any comparison setting (precmp, subcmp, cmp, or mbcmp) is nonzero, however, a slower but better half-pel motion search will be used, regardless of what mbd is set to. If qpel is set, quarter-pel motion search will be used regardless.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Use comparison function given by mbcmp (default).</dd>
<dt>1</dt>
<dd> Select the MB mode which needs the fewest bits (=vhq).</dd>
<dt>2</dt>
<dd> Select the MB mode which has the best rate distortion.</dd></dl>
</dl>
<dt><code>vhq&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Same as mbd=1, kept for compatibility reasons.</dd>
<dt><code>v4mv&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Allow 4 motion vectors per macroblock (slightly better quality). Works better if used with mbd&gt;0.</dd>
<dt><code>obmc&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> overlapped block motion compensation (H.263+)</dd>
<dt><code>loop&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> loop filter (H.263+) note, this is broken</dd>
<dt><code>keyint=&lt;0-300&gt;</code></dt>
<dd> maximum interval between keyframes in frames (default: 250 or one keyframe every ten seconds in a 25fps movie. This is the recommended default for MPEG-4). Most codecs require regular keyframes in order to limit the accumulation of mismatch error. Keyframes are also needed for seeking, as seeking is only possible to a keyframe &#8211; but keyframes need more space than other frames, so larger numbers here mean slightly smaller files but less precise seeking. 0 is equivalent to 1, which makes every frame a keyframe. Values &gt;300 are not recommended as the quality might be bad depending upon decoder, encoder and luck. It is common for MPEG-1/2 to use values &lt;=30.</dd>
<dt><code>sc_threshold=&lt;-1000000000-1000000000&gt;</code></dt>
<dd> Threshold for scene change detection. A keyframe is inserted by libavcodec when it detects a scene change. You can specify the sensitivity of the detection with this option. -1000000000 means there is a scene change detected at every frame, 1000000000 means no scene changes are detected (default: 0).</dd>
<dt><code>sc_factor=&lt;any positive integer&gt;</code></dt>
<dd> Causes frames with higher quantizers to be more likely to trigger a scene change detection and make libavcodec use an I-frame (default: 1). 1-16 is a sane range. Values between 2 and 6 may yield increasing PSNR (up to approximately 0.04 dB) and better placement of I-frames in high-motion scenes. Higher values than 6 may give very slightly better PSNR (approximately 0.01 dB more than sc_factor=6), but noticably worse visual quality.</dd>
<dt><code>vb_strategy=&lt;0-2&gt; (pass one only)</code></dt>
<dd> strategy to choose between I/P/B-frames:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Always use the maximum number of B-frames (default).</dd>
<dt>1</dt>
<dd> Avoid B-frames in high motion scenes. See the b_sensitivity option to tune this strategy.</dd>
<dt>2</dt>
<dd> Places B-frames more or less optimally to yield maximum quality (slower). You may want to reduce the speed impact of this option by tuning the option brd_scale.</dd></dl>
</dl>
<dt><code>b_sensitivity=&lt;any integer greater than 0&gt;</code></dt>
<dd> Adjusts how sensitively vb_strategy=1 detects motion and avoids using B-frames (default: 40). Lower sensitivities will result in more B-frames. Using more B-frames usually improves PSNR, but too many B-frames can hurt quality in high-motion scenes. Unless there is an extremely high amount of motion, b_sensitivity can safely be lowered below the default; 10 is a reasonable value in most cases.</dd>
<dt><code>brd_scale=&lt;0-10&gt;</code></dt>
<dd> Downscales frames for dynamic B-frame decision (default: 0). Each time brd_scale is increased by one, the frame dimensions are divided by two, which improves speed by a factor of four. Both dimensions of the fully downscaled frame must be even numbers, so brd_scale=1 requires the original dimensions to be multiples of four, brd_scale=2 requires multiples of eight, etc. In other words, the dimensions of the original frame must both be divisible by 2^(brd_scale+1) with no remainder.</dd>
<dt><code>bidir_refine=&lt;0-4&gt;</code></dt>
<dd> Refine the two motion vectors used in bidirectional macroblocks, rather than re-using vectors from the forward and backward searches. This option has no effect without B-frames.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Disabled (default).</dd>
<dt>1-4</dt>
<dd> Use a wider search (larger values are slower).</dd></dl>
</dl>
<dt><code>vpass=&lt;1-3&gt;</code></dt>
<dd> Activates internal two (or more) pass mode, only specify if you wish to use two (or more) pass encoding.</dd>
<dl>
<dl>
<dt>1</dt>
<dd> first pass (also see turbo)</dd>
<dt>2</dt>
<dd> second pass</dd>
<dt>3</dt>
<dd> Nth pass (second and subsequent passes of N-pass encoding)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Here is how it works, and how to use it:<br />
 The first pass (vpass=1) writes the statistics file. You might want to deactivate some CPU-hungry options, like &quot;turbo&quot; mode does.<br />
 In two pass mode, the second pass (vpass=2) reads the statistics file and bases ratecontrol decisions on it.<br />
 In N-pass mode, the second pass (vpass=3, that is not a typo) does both: It first reads the statistics, then overwrites them. You might want to backup divx2pass.log before doing this if there is any possibility that you will have to cancel MEncoder. You can use all encoding options, except very CPU-hungry options like &quot;qns&quot;.<br />
 You can run this same pass over and over to refine the encode. Each subsequent pass will use the statistics from the previous pass to improve. The final pass can include any CPU-hungry encoding options.<br />
 If you want a 2 pass encode, use first vpass=1, and then vpass=2.<br />
 If you want a 3 or more pass encode, use vpass=1 for the first pass and then vpass=3 and then vpass=3 again and again until you are satisfied with the encode.</dd></dl>
<dl>
<dt>
</dt><dd> huffyuv:</dd></dl>
<dl>
<dl>
<dt>pass 1</dt>
<dd> Saves statistics.</dd>
<dt>pass 2</dt>
<dd> Encodes with an optimal Huffman table based upon statistics from the first pass.</dd></dl>
</dl>
<dt><code>turbo (two pass only)</code></dt>
<dd> Dramatically speeds up pass one using faster algorithms and disabling CPU-intensive options. This will probably reduce global PSNR a little bit (around 0.01dB) and change individual frame type and PSNR a little bit more (up to 0.03dB).</dd>
<dt><code>aspect=&lt;x/y&gt;</code></dt>
<dd> Store movie aspect internally, just like with MPEG files. Much nicer than rescaling, because quality is not decreased. Only MPlayer will play these files correctly, other players will display them with wrong aspect. The aspect parameter can be given as a ratio or a floating point number. </dd>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>aspect=16/9 or aspect=1.78</dt>
<dd></dd></dl>
</dl>
<dt><code>autoaspect</code></dt>
<dd> Same as the aspect option, but automatically computes aspect, taking into account all the adjustments (crop/expand/scale/etc.) made in the filter chain. Does not incur a performance penalty, so you can safely leave it always on.</dd>
<dt><code>vbitrate=&lt;value&gt;</code></dt>
<dd> Specify bitrate (default: 800).<br />
 <i>WARNING:</i> 1kbit = 1000 bits</dd>
<dl>
<dl>
<dt>4-16000</dt>
<dd> (in kbit)</dd>
<dt>16001-24000000</dt>
<dd> (in bit)</dd></dl>
</dl>
<dt><code>vratetol=&lt;value&gt;</code></dt>
<dd> approximated file size tolerance in kbit. 1000-100000 is a sane range. (warning: 1kbit = 1000 bits) (default: 8000)<br />
 <i>NOTE:</i> vratetol should not be too large during the second pass or there might be problems if vrc_(min|max)rate is used.</dd>
<dt><code>vrc_maxrate=&lt;value&gt;</code></dt>
<dd> maximum bitrate in kbit/sec (default: 0, unlimited)</dd>
<dt><code>vrc_minrate=&lt;value&gt;</code></dt>
<dd> minimum bitrate in kbit/sec (default: 0, unlimited)</dd>
<dt><code>vrc_buf_size=&lt;value&gt;</code></dt>
<dd> buffer size in kbit For MPEG-1/2 this also sets the vbv buffer size, use 327 for VCD, 917 for SVCD and 1835 for DVD.</dd>
<dt><code>vrc_buf_aggressivity</code></dt>
<dd> currently useless</dd>
<dt><code>vrc_strategy</code></dt>
<dd> Ratecontrol method. Note that some of the ratecontrol-affecting options will have no effect if vrc_strategy is not set to 0.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Use internal lavc ratecontrol (default).</dd>
<dt>1</dt>
<dd> Use Xvid ratecontrol (experimental; requires MEncoder to be compiled with support for Xvid 1.1 or higher).</dd></dl>
</dl>
<dt><code>vb_qfactor=&lt;-31.0-31.0&gt;</code></dt>
<dd> quantizer factor between B- and non-B-frames (default: 1.25)</dd>
<dt><code>vi_qfactor=&lt;-31.0-31.0&gt;</code></dt>
<dd> quantizer factor between I- and non-I-frames (default: 0.8)</dd>
<dt><code>vb_qoffset=&lt;-31.0-31.0&gt;</code></dt>
<dd> quantizer offset between B- and non-B-frames (default: 1.25)</dd>
<dt><code>vi_qoffset=&lt;-31.0-31.0&gt;</code></dt>
<dd> (default: 0.0)<br />
 if v{b|i}_qfactor &gt; 0<br />
 I/B-frame quantizer = P-frame quantizer * v{b|i}_qfactor + v{b|i}_qoffset<br />
 else<br />
 do normal ratecontrol (do not lock to next P-frame quantizer) and set q= -q * v{b|i}_qfactor + v{b|i}_qoffset<br />
 <i>HINT:</i> To do constant quantizer encoding with different quantizers for I/P- and B-frames you can use: lmin= &lt;ip_quant&gt;:lmax= &lt;ip_quant&gt;:vb_qfactor= &lt;b_quant/ip_quant&gt;.</dd>
<dt><code>vqblur=&lt;0.0-1.0&gt; (pass one)</code></dt>
<dd> Quantizer blur (default: 0.5), larger values will average the quantizer more over time (slower change).</dd>
<dl>
<dl>
<dt>0.0</dt>
<dd> Quantizer blur disabled.</dd>
<dt>1.0</dt>
<dd> Average the quantizer over all previous frames.</dd></dl>
</dl>
<dt><code>vqblur=&lt;0.0-99.0&gt; (pass two)</code></dt>
<dd> Quantizer gaussian blur (default: 0.5), larger values will average the quantizer more over time (slower change).</dd>
<dt><code>vqcomp=&lt;0.0-1.0&gt;</code></dt>
<dd> Quantizer compression, vrc_eq depends upon this (default: 0.5). <i>NOTE:</i> Perceptual quality will be optimal somewhere in between the range&#8217;s extremes.</dd>
<dt><code>vrc_eq=&lt;equation&gt;</code></dt>
<dd> main ratecontrol equation</dd>
<dl>
<dl>
<dt>1+(tex/avgTex-1)*qComp</dt>
<dd> approximately the equation of the old ratecontrol code</dd>
<dt>tex^qComp</dt>
<dd> with qcomp 0.5 or something like that (default)</dd></dl>
</dl>
</dl>
<dl>
<dt>
</dt><dd> infix operators:</dd></dl>
<dl>
<dl>
<dt>+,-,*,/,^</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd> variables:</dd></dl>
<dl>
<dl>
<dt>tex&nbsp;<wbr>&nbsp;</dt>
<dd> texture complexity</dd>
<dt>iTex,pTex</dt>
<dd> intra, non-intra texture complexity</dd>
<dt>avgTex</dt>
<dd> average texture complexity</dd>
<dt>avgIITex</dt>
<dd> average intra texture complexity in I-frames</dd>
<dt>avgPITex</dt>
<dd> average intra texture complexity in P-frames</dd>
<dt>avgPPTex</dt>
<dd> average non-intra texture complexity in P-frames</dd>
<dt>avgBPTex</dt>
<dd> average non-intra texture complexity in B-frames</dd>
<dt>mv&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> bits used for motion vectors</dd>
<dt>fCode</dt>
<dd> maximum length of motion vector in log2 scale</dd>
<dt>iCount</dt>
<dd> number of intra macroblocks / number of macroblocks</dd>
<dt>var&nbsp;<wbr>&nbsp;</dt>
<dd> spatial complexity</dd>
<dt>mcVar</dt>
<dd> temporal complexity</dd>
<dt>qComp</dt>
<dd> qcomp from the command line</dd>
<dt>isI, isP, isB</dt>
<dd> Is 1 if picture type is I/P/B else 0.</dd>
<dt>Pi,E&nbsp;</dt>
<dd> See your favorite math book.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> functions:</dd></dl>
<dl>
<dl>
<dt>max(a,b),min(a,b)</dt>
<dd> maximum / minimum</dd>
<dt>gt(a,b)</dt>
<dd> is 1 if a&gt;b, 0 otherwise</dd>
<dt>lt(a,b)</dt>
<dd> is 1 if a&lt;b, 0 otherwise</dd>
<dt>eq(a,b)</dt>
<dd> is 1 if a==b, 0 otherwise</dd>
<dt>sin, cos, tan, sinh, cosh, tanh, exp, log, abs</dt>
<dd></dd></dl>
</dl>
<dl>
<dt><code>vrc_override=&lt;options&gt;</code></dt>
<dd> User specified quality for specific parts (ending, credits, &#8230;). The options are &lt;start-frame&gt;, &lt;end-frame&gt;, &lt;quality&gt;[/&lt;start-frame&gt;, &lt;end-frame&gt;, &lt;quality&gt;[/&#8230;]]:</dd>
<dl>
<dl>
<dt>quality (2-31)</dt>
<dd> quantizer</dd>
<dt>quality (-500-0)</dt>
<dd> quality correction in %</dd></dl>
</dl>
<dt><code>vrc_init_cplx=&lt;0-1000&gt;</code></dt>
<dd> initial complexity (pass 1)</dd>
<dt><code>vrc_init_occupancy=&lt;0.0-1.0&gt;</code></dt>
<dd> initial buffer occupancy, as a fraction of vrc_buf_size (default: 0.9)</dd>
<dt><code>vqsquish=&lt;0|1&gt;</code></dt>
<dd> Specify how to keep the quantizer between qmin and qmax.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Use clipping.</dd>
<dt>1</dt>
<dd> Use a nice differentiable function (default).</dd></dl>
</dl>
<dt><code>vlelim=&lt;-1000-1000&gt;</code></dt>
<dd> Sets single coefficient elimination threshold for luminance. Negative values will also consider the DC coefficient (should be at least -4 or lower for encoding at quant=1):</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled (default)</dd>
<dt>-4</dt>
<dd> JVT recommendation</dd></dl>
</dl>
<dt><code>vcelim=&lt;-1000-1000&gt;</code></dt>
<dd> Sets single coefficient elimination threshold for chrominance. Negative values will also consider the DC coefficient (should be at least -4 or lower for encoding at quant=1):</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled (default)</dd>
<dt>7</dt>
<dd> JVT recommendation</dd></dl>
</dl>
<dt><code>vstrict=&lt;-2|-1|0|1&gt;</code></dt>
<dd> strict standard compliance</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled</dd>
<dt>1</dt>
<dd> Only recommended if you want to feed the output into the MPEG-4 reference decoder.</dd>
<dt>-1</dt>
<dd> Allow libavcodec specific extensions (default).</dd>
<dt>-2</dt>
<dd> Enables experimental codecs and features which may not be playable with future MPlayer versions (snow).</dd></dl>
</dl>
<dt><code>vdpart&nbsp;</code></dt>
<dd> Data partitioning. Adds 2 Bytes per video packet, improves error-resistance when transferring over unreliable channels (e.g. streaming over the internet). Each video packet will be encoded in 3 separate partitions:</dd>
<dl>
<dl>
<dt>1. MVs</dt>
<dd> movement</dd>
<dt>2. DC coefficients</dt>
<dd> low res picture</dd>
<dt>3. AC coefficients</dt>
<dd> details</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> MV &amp; DC are most important, losing them looks far worse than losing the AC and the 1. &amp; 2. partition. (MV &amp; DC) are far smaller than the 3. partition (AC) meaning that errors will hit the AC partition much more often than the MV &amp; DC partitions. Thus, the picture will look better with partitioning than without, as without partitioning an error will trash AC/DC/MV equally.</dd></dl>
<dt><code>vpsize=&lt;0-10000&gt; (also see vdpart)</code></dt>
<dd> Video packet size, improves error-resistance.</dd>
<dl>
<dl>
<dt>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> disabled (default)</dd>
<dt>100-1000</dt>
<dd> good choice</dd></dl>
</dl>
<dt><code>ss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> slice structured mode for H.263+</dd>
<dt><code>gray&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> grayscale only encoding (faster)</dd>
<dt><code>vfdct=&lt;0-10&gt;</code></dt>
<dd> DCT algorithm</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Automatically select a good one (default).</dd>
<dt>1</dt>
<dd> fast integer</dd>
<dt>2</dt>
<dd> accurate integer</dd>
<dt>3</dt>
<dd> MMX</dd>
<dt>4</dt>
<dd> mlib</dd>
<dt>5</dt>
<dd> AltiVec</dd>
<dt>6</dt>
<dd> floating point AAN</dd></dl>
</dl>
<dt><code>idct=&lt;0-99&gt;</code></dt>
<dd> IDCT algorithm<br />
 <i>NOTE:</i> To the best of our knowledge all these IDCTs do pass the IEEE1180 tests.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Automatically select a good one (default).</dd>
<dt>1</dt>
<dd> JPEG reference integer</dd>
<dt>2</dt>
<dd> simple</dd>
<dt>3</dt>
<dd> simplemmx</dd>
<dt>4</dt>
<dd> libmpeg2mmx (inaccurate, do not use for encoding with keyint &gt;100)</dd>
<dt>5</dt>
<dd> ps2</dd>
<dt>6</dt>
<dd> mlib</dd>
<dt>7</dt>
<dd> arm</dd>
<dt>8</dt>
<dd> AltiVec</dd>
<dt>9</dt>
<dd> sh4</dd>
<dt>10</dt>
<dd> simplearm</dd>
<dt>11</dt>
<dd> H.264</dd>
<dt>12</dt>
<dd> VP3</dd>
<dt>13</dt>
<dd> IPP</dd>
<dt>14</dt>
<dd> xvidmmx</dd>
<dt>15</dt>
<dd> CAVS</dd>
<dt>16</dt>
<dd> simplearmv5te</dd>
<dt>17</dt>
<dd> simplearmv6</dd></dl>
</dl>
<dt><code>lumi_mask=&lt;0.0-1.0&gt;</code></dt>
<dd> Luminance masking is a &#8216;psychosensory&#8217; setting that is supposed to make use of the fact that the human eye tends to notice fewer details in very bright parts of the picture. Luminance masking compresses bright areas stronger than medium ones, so it will save bits that can be spent again on other frames, raising overall subjective quality, while possibly reducing PSNR.<br />
 <i>WARNING:</i> Be careful, overly large values can cause disastrous things.<br />
 <i>WARNING:</i> Large values might look good on some monitors but may look horrible on other monitors.</dd>
<dl>
<dl>
<dt>0.0&nbsp;<wbr>&nbsp;</dt>
<dd> disabled (default)</dd>
<dt>0.0-0.3</dt>
<dd> sane range</dd></dl>
</dl>
<dt><code>dark_mask=&lt;0.0-1.0&gt;</code></dt>
<dd> Darkness masking is a &#8216;psychosensory&#8217; setting that is supposed to make use of the fact that the human eye tends to notice fewer details in very dark parts of the picture. Darkness masking compresses dark areas stronger than medium ones, so it will save bits that can be spent again on other frames, raising overall subjective quality, while possibly reducing PSNR.<br />
 <i>WARNING:</i> Be careful, overly large values can cause disastrous things.<br />
 <i>WARNING:</i> Large values might look good on some monitors but may look horrible on other monitors / TV / TFT.</dd>
<dl>
<dl>
<dt>0.0&nbsp;<wbr>&nbsp;</dt>
<dd> disabled (default)</dd>
<dt>0.0-0.3</dt>
<dd> sane range</dd></dl>
</dl>
<dt><code>tcplx_mask=&lt;0.0-1.0&gt;</code></dt>
<dd> Temporal complexity masking (default: 0.0 (disabled)). Imagine a scene with a bird flying across the whole scene; tcplx_mask will raise the quantizers of the bird&#8217;s macroblocks (thus decreasing their quality), as the human eye usually does not have time to see all the bird&#8217;s details. Be warned that if the masked object stops (e.g. the bird lands) it is likely to look horrible for a short period of time, until the encoder figures out that the object is not moving and needs refined blocks. The saved bits will be spent on other parts of the video, which may increase subjective quality, provided that tcplx_mask is carefully chosen.</dd>
<dt><code>scplx_mask=&lt;0.0-1.0&gt;</code></dt>
<dd> Spatial complexity masking. Larger values help against blockiness, if no deblocking filter is used for decoding, which is maybe not a good idea.<br />
 Imagine a scene with grass (which usually has great spatial complexity), a blue sky and a house; scplx_mask will raise the quantizers of the grass&#8217; macroblocks, thus decreasing its quality, in order to spend more bits on the sky and the house.<br />
 <i>HINT:</i> Crop any black borders completely as they will reduce the quality of the macroblocks (also applies without scplx_mask).</dd>
<dl>
<dl>
<dt>0.0&nbsp;<wbr>&nbsp;</dt>
<dd> disabled (default)</dd>
<dt>0.0-0.5</dt>
<dd> sane range</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>NOTE:</i> This setting does not have the same effect as using a custom matrix that would compress high frequencies harder, as scplx_mask will reduce the quality of P blocks even if only DC is changing. The result of scplx_mask will probably not look as good.</dd></dl>
<dt><code>p_mask=&lt;0.0-1.0&gt; (also see vi_qfactor)</code></dt>
<dd> Reduces the quality of inter blocks. This is equivalent to increasing the quality of intra blocks, because the same average bitrate will be distributed by the rate controller to the whole video sequence (default: 0.0 (disabled)). p_mask=1.0 doubles the bits allocated to each intra block.</dd>
<dt><code>border_mask=&lt;0.0-1.0&gt;</code></dt>
<dd> border-processing for MPEG-style encoders. Border processing increases the quantizer for macroblocks which are less than 1/5th of the frame width/height away from the frame border, since they are often visually less important.</dd>
<dt><code>naq&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Normalize adaptive quantization (experimental). When using adaptive quantization (*_mask), the average per-MB quantizer may no longer match the requested frame-level quantizer. Naq will attempt to adjust the per-MB quantizers to maintain the proper average.</dd>
<dt><code>ildct&nbsp;<wbr>&nbsp;</code></dt>
<dd> Use interlaced DCT.</dd>
<dt><code>ilme&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Use interlaced motion estimation (mutually exclusive with qpel).</dd>
<dt><code>alt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Use alternative scantable.</dd>
<dt><code>top=&lt;-1-1&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd>
</dd><dl>
<dl>
<dt>-1</dt>
<dd> automatic</dd>
<dt>0</dt>
<dd> bottom field first</dd>
<dt>1</dt>
<dd> top field first</dd></dl>
</dl>
<dt><code>format=&lt;value&gt;</code></dt>
<dd>
</dd><dl>
<dl>
<dt>YV12&nbsp;</dt>
<dd> default</dd>
<dt>444P&nbsp;</dt>
<dd> for ffv1</dd>
<dt>422P&nbsp;</dt>
<dd> for HuffYUV, lossless JPEG, dv and ffv1</dd>
<dt>411P&nbsp;</dt>
<dd> for lossless JPEG, dv and ffv1</dd>
<dt>YVU9&nbsp;</dt>
<dd> for lossless JPEG, ffv1 and svq1</dd>
<dt>BGR32</dt>
<dd> for lossless JPEG and ffv1</dd></dl>
</dl>
<dt><code>pred&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> (for HuffYUV)</dd>
<dl>
<dl>
<dt>0</dt>
<dd> left prediction</dd>
<dt>1</dt>
<dd> plane/gradient prediction</dd>
<dt>2</dt>
<dd> median prediction</dd></dl>
</dl>
<dt><code>pred&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> (for lossless JPEG)</dd>
<dl>
<dl>
<dt>0</dt>
<dd> left prediction</dd>
<dt>1</dt>
<dd> top prediction</dd>
<dt>2</dt>
<dd> topleft prediction</dd>
<dt>3</dt>
<dd> plane/gradient prediction</dd>
<dt>6</dt>
<dd> mean prediction</dd></dl>
</dl>
<dt><code>coder&nbsp;<wbr>&nbsp;</code></dt>
<dd> (for ffv1)</dd>
<dl>
<dl>
<dt>0</dt>
<dd> vlc coding (Golomb-Rice)</dd>
<dt>1</dt>
<dd> arithmetic coding (CABAC)</dd></dl>
</dl>
<dt><code>context</code></dt>
<dd> (for ffv1)</dd>
<dl>
<dl>
<dt>0</dt>
<dd> small context model</dd>
<dt>1</dt>
<dd> large context model</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> (for ffvhuff)</dd></dl>
<dl>
<dl>
<dt>0</dt>
<dd> predetermined Huffman tables (builtin or two pass)</dd>
<dt>1</dt>
<dd> adaptive Huffman tables</dd></dl>
</dl>
<dt><code>qpel&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Use quarter pel motion compensation (mutually exclusive with ilme).<br />
 <i>HINT:</i> This seems only useful for high bitrate encodings.</dd>
<dt><code>mbcmp=&lt;0-2000&gt;</code></dt>
<dd> Sets the comparison function for the macroblock decision, has only an effect if mbd=0. This is also used for some motion search functions, in which case it has an effect regardless of mbd setting.</dd>
<dl>
<dl>
<dt>0 (SAD)</dt>
<dd> sum of absolute differences, fast (default)</dd>
<dt>1 (SSE)</dt>
<dd> sum of squared errors</dd>
<dt>2 (SATD)</dt>
<dd> sum of absolute Hadamard transformed differences</dd>
<dt>3 (DCT)</dt>
<dd> sum of absolute DCT transformed differences</dd>
<dt>4 (PSNR)</dt>
<dd> sum of squared quantization errors (avoid, low quality)</dd>
<dt>5 (BIT)</dt>
<dd> number of bits needed for the block</dd>
<dt>6 (RD)</dt>
<dd> rate distortion optimal, slow</dd>
<dt>7 (ZERO)</dt>
<dd> 0</dd>
<dt>8 (VSAD)</dt>
<dd> sum of absolute vertical differences</dd>
<dt>9 (VSSE)</dt>
<dd> sum of squared vertical differences</dd>
<dt>10 (NSSE)</dt>
<dd> noise preserving sum of squared differences</dd>
<dt>11 (W53)</dt>
<dd> 5/3 wavelet, only used in snow</dd>
<dt>12 (W97)</dt>
<dd> 9/7 wavelet, only used in snow</dd>
<dt>+256&nbsp;</dt>
<dd> Also use chroma, currently does not work (correctly) with B-frames.</dd></dl>
</dl>
<dt><code>ildctcmp=&lt;0-2000&gt;</code></dt>
<dd> Sets the comparison function for interlaced DCT decision (see mbcmp for available comparison functions).</dd>
<dt><code>precmp=&lt;0-2000&gt;</code></dt>
<dd> Sets the comparison function for motion estimation pre pass (see mbcmp for available comparison functions) (default: 0).</dd>
<dt><code>cmp=&lt;0-2000&gt;</code></dt>
<dd> Sets the comparison function for full pel motion estimation (see mbcmp for available comparison functions) (default: 0).</dd>
<dt><code>subcmp=&lt;0-2000&gt;</code></dt>
<dd> Sets the comparison function for sub pel motion estimation (see mbcmp for available comparison functions) (default: 0).</dd>
<dt><code>skipcmp=&lt;0-2000&gt;</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>nssew=&lt;0-1000000&gt;</code></dt>
<dd> This setting controls NSSE weight, where larger weights will result in more noise. 0 NSSE is identical to SSE You may find this useful if you prefer to keep some noise in your encoded video rather than filtering it away before encoding (default: 8).</dd>
<dt><code>predia=&lt;-99-6&gt;</code></dt>
<dd> diamond type and size for motion estimation pre-pass</dd>
<dt><code>dia=&lt;-99-6&gt;</code></dt>
<dd> Diamond type &amp; size for motion estimation. Motion search is an iterative process. Using a small diamond does not limit the search to finding only small motion vectors. It is just somewhat more likely to stop before finding the very best motion vector, especially when noise is involved. Bigger diamonds allow a wider search for the best motion vector, thus are slower but result in better quality.<br />
 Big normal diamonds are better quality than shape-adaptive diamonds.<br />
 Shape-adaptive diamonds are a good tradeoff between speed and quality.<br />
 <i>NOTE:</i> The sizes of the normal diamonds and shape adaptive ones do not have the same meaning.</dd>
<dl>
<dl>
<dt>-3</dt>
<dd> shape adaptive (fast) diamond with size 3</dd>
<dt>-2</dt>
<dd> shape adaptive (fast) diamond with size 2</dd>
<dt>-1</dt>
<dd> uneven multi-hexagon search (slow)</dd>
<dt>1</dt>
<dd> normal size=1 diamond (default) =EPZS type diamond </dd>
<pre>
      0
     000
      0
</pre>
<dt>2</dt>
<dd> normal size=2 diamond </dd>
<pre>
      0
     000
    00000
     000
      0
</pre>
</dl>
</dl>
<dt><code>trell&nbsp;<wbr>&nbsp;</code></dt>
<dd> Trellis searched quantization. This will find the optimal encoding for each 8&#215;8 block. Trellis searched quantization is quite simply an optimal quantization in the PSNR versus bitrate sense (Assuming that there would be no rounding errors introduced by the IDCT, which is obviously not the case.). It simply finds a block for the minimum of error and lambda*bits.</dd>
<dl>
<dl>
<dt>lambda</dt>
<dd> quantization parameter (QP) dependent constant</dd>
<dt>bits&nbsp;</dt>
<dd> amount of bits needed to encode the block</dd>
<dt>error</dt>
<dd> sum of squared errors of the quantization</dd></dl>
</dl>
<dt><code>cbp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Rate distorted optimal coded block pattern. Will select the coded block pattern which minimizes distortion + lambda*rate. This can only be used together with trellis quantization.</dd>
<dt><code>mv0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Try to encode each MB with MV=&lt;0,0&gt; and choose the better one. This has no effect if mbd=0.</dd>
<dt><code>mv0_threshold=&lt;any non-negative integer&gt;</code></dt>
<dd> When surrounding motion vectors are &lt;0,0&gt; and the motion estimation score of the current block is less than mv0_threshold, &lt;0,0&gt; is used for the motion vector and further motion estimation is skipped (default: 256). Lowering mv0_threshold to 0 can give a slight (0.01dB) PSNR increase and possibly make the encoded video look slightly better; raising mv0_threshold past 320 results in diminished PSNR and visual quality. Higher values speed up encoding very slightly (usually less than 1%, depending on the other options used).<br />
 <i>NOTE:</i> This option does not require mv0 to be enabled.</dd>
<dt><code>qprd (mbd=2 only)</code></dt>
<dd> rate distorted optimal quantization parameter (QP) for the given lambda of each macroblock</dd>
<dt><code>last_pred=&lt;0-99&gt;</code></dt>
<dd> amount of motion predictors from the previous frame</dd>
<dl>
<dl>
<dt>0</dt>
<dd> (default)</dd>
<dt>a</dt>
<dd> Will use 2a+1 x 2a+1 macroblock square of motion vector predictors from the previous frame.</dd></dl>
</dl>
<dt><code>preme=&lt;0-2&gt;</code></dt>
<dd> motion estimation pre-pass</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled</dd>
<dt>1</dt>
<dd> only after I-frames (default)</dd>
<dt>2</dt>
<dd> always</dd></dl>
</dl>
<dt><code>subq=&lt;1-8&gt;</code></dt>
<dd> subpel refinement quality (for qpel) (default: 8 (high quality))<br />
 <i>NOTE:</i> This has a significant effect on speed.</dd>
<dt><code>refs=&lt;1-8&gt;</code></dt>
<dd> number of reference frames to consider for motion compensation (Snow only) (default: 1)</dd>
<dt><code>psnr&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> print the PSNR (peak signal to noise ratio) for the whole video after encoding and store the per frame PSNR in a file with a name like &#8216;psnr_hhmmss.log&#8217;. Returned values are in dB (decibel), the higher the better.</dd>
<dt><code>mpeg_quant</code></dt>
<dd> Use MPEG quantizers instead of H.263.</dd>
<dt><code>aic&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Enable AC prediction for MPEG-4 or advanced intra prediction for H.263+. This will improve quality very slightly (around 0.02 dB PSNR) and slow down encoding very slightly (about 1%).<br />
 <i>NOTE:</i> vqmin should be 8 or larger for H.263+ AIC.</dd>
<dt><code>aiv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> alternative inter vlc for H.263+</dd>
<dt><code>umv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> unlimited MVs (H.263+ only) Allows encoding of arbitrarily long MVs.</dd>
<dt><code>ibias=&lt;-256-256&gt;</code></dt>
<dd> intra quantizer bias (256 equals 1.0, MPEG style quantizer default: 96, H.263 style quantizer default: 0)<br />
 <i>NOTE:</i> The H.263 MMX quantizer cannot handle positive biases (set vfdct=1 or 2), the MPEG MMX quantizer cannot handle negative biases (set vfdct=1 or 2).</dd>
<dt><code>pbias=&lt;-256-256&gt;</code></dt>
<dd> inter quantizer bias (256 equals 1.0, MPEG style quantizer default: 0, H.263 style quantizer default: -64)<br />
 <i>NOTE:</i> The H.263 MMX quantizer cannot handle positive biases (set vfdct=1 or 2), the MPEG MMX quantizer cannot handle negative biases (set vfdct=1 or 2).<br />
 <i>HINT:</i> A more positive bias (-32 &#8211; -16 instead of -64) seems to improve the PSNR.</dd>
<dt><code>nr=&lt;0-100000&gt;</code></dt>
<dd> Noise reduction, 0 means disabled. 0-600 is a useful range for typical content, but you may want to turn it up a bit more for very noisy content (default: 0). Given its small impact on speed, you might want to prefer to use this over filtering noise away with video filters like denoise3d or hqdn3d.</dd>
<dt><code>qns=&lt;0-3&gt;</code></dt>
<dd> Quantizer noise shaping. Rather than choosing quantization to most closely match the source video in the PSNR sense, it chooses quantization such that noise (usually ringing) will be masked by similar-frequency content in the image. Larger values are slower but may not result in better quality. This can and should be used together with trellis quantization, in which case the trellis quantization (optimal for constant weight) will be used as startpoint for the iterative search.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled (default)</dd>
<dt>1</dt>
<dd> Only lower the absolute value of coefficients.</dd>
<dt>2</dt>
<dd> Only change coefficients before the last non-zero coefficient + 1.</dd>
<dt>3</dt>
<dd> Try all.</dd></dl>
</dl>
<dt><code>inter_matrix=&lt;comma separated matrix&gt;</code></dt>
<dd> Use custom inter matrix. It needs a comma separated string of 64 integers.</dd>
<dt><code>intra_matrix=&lt;comma separated matrix&gt;</code></dt>
<dd> Use custom intra matrix. It needs a comma separated string of 64 integers.</dd>
<dt><code>vqmod_amp</code></dt>
<dd> experimental quantizer modulation</dd>
<dt><code>vqmod_freq</code></dt>
<dd> experimental quantizer modulation</dd>
<dt><code>dc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> intra DC precision in bits (default: 8). If you specify vcodec=mpeg2video this value can be 8, 9, 10 or 11.</dd>
<dt><code>cgop (also see sc_threshold)</code></dt>
<dd> Close all GOPs. Currently it only works if scene change detection is disabled (sc_threshold=1000000000).</dd>
<dt><code>gmc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Enable Global Motion Compensation.</dd>
<dt><code>(no)lowdelay</code></dt>
<dd> Sets the low delay flag for MPEG-1/2 (disables B-frames).</dd>
<dt><code>vglobal=&lt;0-3&gt;</code></dt>
<dd> Control writing global video headers.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Codec decides where to write global headers (default).</dd>
<dt>1</dt>
<dd> Write global headers only in extradata (needed for .mp4/MOV/NUT).</dd>
<dt>2</dt>
<dd> Write global headers only in front of keyframes.</dd>
<dt>3</dt>
<dd> Combine 1 and 2.</dd></dl>
</dl>
<dt><code>aglobal=&lt;0-3&gt;</code></dt>
<dd> Same as vglobal for audio headers.</dd>
<dt><code>level=&lt;value&gt;</code></dt>
<dd> Set CodecContext Level. Use 31 or 41 to play video on a Playstation 3.</dd>
<dt><code>skip_exp=&lt;0-1000000&gt;</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>skip_factor=&lt;0-1000000&gt;</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>skip_threshold=&lt;0-1000000&gt;</code></dt>
<dd> FIXME: Document this.</dd></dl>
<h3>nuv (-nuvopts)</h3>
<p> Nuppel video is based on RTJPEG and LZO. By default frames are first encoded with RTJPEG and then compressed with LZO, but it is possible to disable either or both of the two passes. As a result, you can in fact output raw i420, LZO compressed i420, RTJPEG, or the default LZO compressed RTJPEG.<br />
 <i>NOTE:</i> The nuvrec documentation contains some advice and examples about the settings to use for the most common TV encodings.</p>
<dl>
<dt><code>c=&lt;0-20&gt;</code></dt>
<dd> chrominance threshold (default: 1)</dd>
<dt><code>l=&lt;0-20&gt;</code></dt>
<dd> luminance threshold (default: 1)</dd>
<dt><code>lzo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Enable LZO compression (default).</dd>
<dt><code>nolzo&nbsp;<wbr>&nbsp;</code></dt>
<dd> Disable LZO compression.</dd>
<dt><code>q=&lt;3-255&gt;</code></dt>
<dd> quality level (default: 255)</dd>
<dt><code>raw &nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Disable RTJPEG encoding.</dd>
<dt><code>rtjpeg&nbsp;</code></dt>
<dd> Enable RTJPEG encoding (default).</dd></dl>
<h3>xvidenc (-xvidencopts)</h3>
<p> There are three modes available: constant bitrate (CBR), fixed quantizer and two pass.</p>
<dl>
<dt><code>pass=&lt;1|2&gt;</code></dt>
<dd> Specify the pass in two pass mode.</dd>
<dt><code>turbo (two pass only)</code></dt>
<dd> Dramatically speeds up pass one using faster algorithms and disabling CPU-intensive options. This will probably reduce global PSNR a little bit and change individual frame type and PSNR a little bit more.</dd>
<dt><code>bitrate=&lt;value&gt; (CBR or two pass mode)</code></dt>
<dd> Sets the bitrate to be used in kbits/second if &lt;16000 or in bits/second if &gt;16000. If &lt;value&gt; is negative, Xvid will use its absolute value as the target size (in kBytes) of the video and compute the associated bitrate automagically (default: 687 kbits/s).</dd>
<dt><code>fixed_quant=&lt;1-31&gt;</code></dt>
<dd> Switch to fixed quantizer mode and specify the quantizer to be used.</dd>
<dt><code>zones=&lt;zone0&gt;[/&lt;zone1&gt;[/&#8230;]] (CBR or two pass mode)</code></dt>
<dd> User specified quality for specific parts (ending, credits, &#8230;). Each zone is &lt;start-frame&gt;,&lt;mode&gt;,&lt;value&gt; where &lt;mode&gt; may be</dd>
<dl>
<dl>
<dt>q</dt>
<dd> Constant quantizer override, where value=&lt;2.0-31.0&gt; represents the quantizer value.</dd>
<dt>w</dt>
<dd> Ratecontrol weight override, where value=&lt;0.01-2.00&gt; represents the quality correction in %.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>zones=90000,q,20</dt>
<dd> Encodes all frames starting with frame 90000 at constant quantizer 20.</dd>
<dt>zones=0,w,0.1/10001,w,1.0/90000,q,20</dt>
<dd> Encode frames 0-10000 at 10% bitrate, encode frames 90000 up to the end at constant quantizer 20. Note that the second zone is needed to delimit the first zone, as without it everything up until frame 89999 would be encoded at 10% bitrate.</dd></dl>
</dl>
<dt><code>me_quality=&lt;0-6&gt;</code></dt>
<dd> This option controls the motion estimation subsystem. The higher the value, the more precise the estimation should be (default: 6). The more precise the motion estimation is, the more bits can be saved. Precision is gained at the expense of CPU time so decrease this setting if you need realtime encoding.</dd>
<dt><code>(no)qpel</code></dt>
<dd> MPEG-4 uses a half pixel precision for its motion search by default. The standard proposes a mode where encoders are allowed to use quarter pixel precision. This option usually results in a sharper image. Unfortunately it has a great impact on bitrate and sometimes the higher bitrate use will prevent it from giving a better image quality at a fixed bitrate. It is better to test with and without this option and see whether it is worth activating.</dd>
<dt><code>(no)gmc</code></dt>
<dd> Enable Global Motion Compensation, which makes Xvid generate special frames (GMC-frames) which are well suited for Pan/Zoom/Rotating images. Whether or not the use of this option will save bits is highly dependent on the source material.</dd>
<dt><code>(no)trellis</code></dt>
<dd> Trellis Quantization is a kind of adaptive quantization method that saves bits by modifying quantized coefficients to make them more compressible by the entropy encoder. Its impact on quality is good, and if VHQ uses too much CPU for you, this setting can be a good alternative to save a few bits (and gain quality at fixed bitrate) at a lesser cost than with VHQ (default: on).</dd>
<dt><code>(no)cartoon</code></dt>
<dd> Activate this if your encoded sequence is an anime/cartoon. It modifies some Xvid internal thresholds so Xvid takes better decisions on frame types and motion vectors for flat looking cartoons.</dd>
<dt><code>(no)chroma_me</code></dt>
<dd> The usual motion estimation algorithm uses only the luminance information to find the best motion vector. However for some video material, using the chroma planes can help find better vectors. This setting toggles the use of chroma planes for motion estimation (default: on).</dd>
<dt><code>(no)chroma_opt</code></dt>
<dd> Enable a chroma optimizer prefilter. It will do some extra magic on color information to minimize the stepped-stairs effect on edges. It will improve quality at the cost of encoding speed. It reduces PSNR by nature, as the mathematical deviation to the original picture will get bigger, but the subjective image quality will raise. Since it works with color information, you might want to turn it off when encoding in grayscale.</dd>
<dt><code>(no)hq_ac</code></dt>
<dd> Activates high-quality prediction of AC coefficients for intra frames from neighbor blocks (default: on).</dd>
<dt><code>vhq=&lt;0-4&gt;</code></dt>
<dd> The motion search algorithm is based on a search in the usual color domain and tries to find a motion vector that minimizes the difference between the reference frame and the encoded frame. With this setting activated, Xvid will also use the frequency domain (DCT) to search for a motion vector that minimizes not only the spatial difference but also the encoding length of the block. Fastest to slowest:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> off</dd>
<dt>1</dt>
<dd> mode decision (inter/intra MB) (default)</dd>
<dt>2</dt>
<dd> limited search</dd>
<dt>3</dt>
<dd> medium search</dd>
<dt>4</dt>
<dd> wide search</dd></dl>
</dl>
<dt><code>(no)lumi_mask</code></dt>
<dd> Adaptive quantization allows the macroblock quantizers to vary inside each frame. This is a &#8216;psychosensory&#8217; setting that is supposed to make use of the fact that the human eye tends to notice fewer details in very bright and very dark parts of the picture. It compresses those areas more strongly than medium ones, which will save bits that can be spent again on other frames, raising overall subjective quality and possibly reducing PSNR.</dd>
<dt><code>(no)grayscale</code></dt>
<dd> Make Xvid discard chroma planes so the encoded video is grayscale only. Note that this does not speed up encoding, it just prevents chroma data from being written in the last stage of encoding.</dd>
<dt><code>(no)interlacing</code></dt>
<dd> Encode the fields of interlaced video material. Turn this option on for interlaced content.<br />
 <i>NOTE:</i> Should you rescale the video, you would need an interlace-aware resizer, which you can activate with -vf scale=&lt;width&gt;:&lt;height&gt;:1.</dd>
<dt><code>min_iquant=&lt;0-31&gt;</code></dt>
<dd> minimum I-frame quantizer (default: 2)</dd>
<dt><code>max_iquant=&lt;0-31&gt;</code></dt>
<dd> maximum I-frame quantizer (default: 31)</dd>
<dt><code>min_pquant=&lt;0-31&gt;</code></dt>
<dd> minimum P-frame quantizer (default: 2)</dd>
<dt><code>max_pquant=&lt;0-31&gt;</code></dt>
<dd> maximum P-frame quantizer (default: 31)</dd>
<dt><code>min_bquant=&lt;0-31&gt;</code></dt>
<dd> minimum B-frame quantizer (default: 2)</dd>
<dt><code>max_bquant=&lt;0-31&gt;</code></dt>
<dd> maximum B-frame quantizer (default: 31)</dd>
<dt><code>min_key_interval=&lt;value&gt; (two pass only)</code></dt>
<dd> minimum interval between keyframes (default: 0)</dd>
<dt><code>max_key_interval=&lt;value&gt;</code></dt>
<dd> maximum interval between keyframes (default: 10*fps)</dd>
<dt><code>quant_type=&lt;h263|mpeg&gt;</code></dt>
<dd> Sets the type of quantizer to use. For high bitrates, you will find that MPEG quantization preserves more detail. For low bitrates, the smoothing of H.263 will give you less block noise. When using custom matrices, MPEG quantization <code>must</code> be used.</dd>
<dt><code>quant_intra_matrix=&lt;filename&gt;</code></dt>
<dd> Load a custom intra matrix file. You can build such a file with xvid4conf&#8217;s matrix editor.</dd>
<dt><code>quant_inter_matrix=&lt;filename&gt;</code></dt>
<dd> Load a custom inter matrix file. You can build such a file with xvid4conf&#8217;s matrix editor.</dd>
<dt><code>keyframe_boost=&lt;0-1000&gt; (two pass mode only)</code></dt>
<dd> Shift some bits from the pool for other frame types to intra frames, thus improving keyframe quality. This amount is an extra percentage, so a value of 10 will give your keyframes 10% more bits than normal (default: 0).</dd>
<dt><code>kfthreshold=&lt;value&gt; (two pass mode only)</code></dt>
<dd> Works together with kfreduction. Determines the minimum distance below which you consider that two frames are considered consecutive and treated differently according to kfreduction (default: 10).</dd>
<dt><code>kfreduction=&lt;0-100&gt; (two pass mode only)</code></dt>
<dd> The above two settings can be used to adjust the size of keyframes that you consider too close to the first (in a row). kfthreshold sets the range in which keyframes are reduced, and kfreduction determines the bitrate reduction they get. The last I-frame will get treated normally (default: 30).</dd>
<dt><code>max_bframes=&lt;0-4&gt;</code></dt>
<dd> Maximum number of B-frames to put between I/P-frames (default: 2).</dd>
<dt><code>bquant_ratio=&lt;0-1000&gt;</code></dt>
<dd> quantizer ratio between B- and non-B-frames, 150=1.50 (default: 150)</dd>
<dt><code>bquant_offset=&lt;-1000-1000&gt;</code></dt>
<dd> quantizer offset between B- and non-B-frames, 100=1.00 (default: 100)</dd>
<dt><code>bf_threshold=&lt;-255-255&gt;</code></dt>
<dd> This setting allows you to specify what priority to place on the use of B-frames. The higher the value, the higher the probability of B-frames being used (default: 0). Do not forget that B-frames usually have a higher quantizer, and therefore aggressive production of B-frames may cause worse visual quality.</dd>
<dt><code>(no)closed_gop</code></dt>
<dd> This option tells Xvid to close every GOP (Group Of Pictures bounded by two I-frames), which makes GOPs independent from each other. This just implies that the last frame of the GOP is either a P-frame or a N-frame but not a B-frame. It is usually a good idea to turn this option on (default: on).</dd>
<dt><code>(no)packed</code></dt>
<dd> This option is meant to solve frame-order issues when encoding to container formats like AVI that cannot cope with out-of-order frames. In practice, most decoders (both software and hardware) are able to deal with frame-order themselves, and may get confused when this option is turned on, so you can safely leave if off, unless you really know what you are doing.<br />
 <i>WARNING:</i> This will generate an illegal bitstream, and will not be decodable by ISO-MPEG-4 decoders except DivX/libavcodec/Xvid.<br />
 <i>WARNING:</i> This will also store a fake DivX version in the file so the bug autodetection of some decoders might be confused.</dd>
<dt><code>frame_drop_ratio=&lt;0-100&gt; (max_bframes=0 only)</code></dt>
<dd> This setting allows the creation of variable framerate video streams. The value of the setting specifies a threshold under which, if the difference of the following frame to the previous frame is below or equal to this threshold, a frame gets not coded (a so called n-vop is placed in the stream). On playback, when reaching an n-vop the previous frame will be displayed.<br />
 <i>WARNING:</i> Playing with this setting may result in a jerky video, so use it at your own risks!</dd>
<dt><code>rc_reaction_delay_factor=&lt;value&gt;</code></dt>
<dd> This parameter controls the number of frames the CBR rate controller will wait before reacting to bitrate changes and compensating for them to obtain a constant bitrate over an averaging range of frames.</dd>
<dt><code>rc_averaging_period=&lt;value&gt;</code></dt>
<dd> Real CBR is hard to achieve. Depending on the video material, bitrate can be variable, and hard to predict. Therefore Xvid uses an averaging period for which it guarantees a given amount of bits (minus a small variation). This settings expresses the &quot;number of frames&quot; for which Xvid averages bitrate and tries to achieve CBR.</dd>
<dt><code>rc_buffer=&lt;value&gt;</code></dt>
<dd> size of the rate control buffer</dd>
<dt><code>curve_compression_high=&lt;0-100&gt;</code></dt>
<dd> This setting allows Xvid to take a certain percentage of bits away from high bitrate scenes and give them back to the bit reservoir. You could also use this if you have a clip with so many bits allocated to high-bitrate scenes that the low(er)-bitrate scenes start to look bad (default: 0).</dd>
<dt><code>curve_compression_low=&lt;0-100&gt;</code></dt>
<dd> This setting allows Xvid to give a certain percentage of extra bits to the low bitrate scenes, taking a few bits from the entire clip. This might come in handy if you have a few low-bitrate scenes that are still blocky (default: 0).</dd>
<dt><code>overflow_control_strength=&lt;0-100&gt;</code></dt>
<dd> During pass one of two pass encoding, a scaled bitrate curve is computed. The difference between that expected curve and the result obtained during encoding is called overflow. Obviously, the two pass rate controller tries to compensate for that overflow, distributing it over the next frames. This setting controls how much of the overflow is distributed every time there is a new frame. Low values allow lazy overflow control, big rate bursts are compensated for more slowly (could lead to lack of precision for small clips). Higher values will make changes in bit redistribution more abrupt, possibly too abrupt if you set it too high, creating artifacts (default: 5).<br />
 <i>NOTE:</i> This setting impacts quality a lot, play with it carefully!</dd>
<dt><code>max_overflow_improvement=&lt;0-100&gt;</code></dt>
<dd> During the frame bit allocation, overflow control may increase the frame size. This parameter specifies the maximum percentage by which the overflow control is allowed to increase the frame size, compared to the ideal curve allocation (default: 5).</dd>
<dt><code>max_overflow_degradation=&lt;0-100&gt;</code></dt>
<dd> During the frame bit allocation, overflow control may decrease the frame size. This parameter specifies the maximum percentage by which the overflow control is allowed to decrease the frame size, compared to the ideal curve allocation (default: 5).</dd>
<dt><code>container_frame_overhead=&lt;0&#8230;&gt;</code></dt>
<dd> Specifies a frame average overhead per frame, in bytes. Most of the time users express their target bitrate for video w/o taking care of the video container overhead. This small but (mostly) constant overhead can cause the target file size to be exceeded. Xvid allows users to set the amount of overhead per frame the container generates (give only an average per frame). 0 has a special meaning, it lets Xvid use its own default values (default: 24 &#8211; AVI average overhead).</dd>
<dt><code>profile=&lt;profile_name&gt;</code></dt>
<dd> Restricts options and VBV (peak bitrate over a short period) according to the Simple, Advanced Simple and DivX profiles. The resulting videos should be playable on standalone players adhering to these profile specifications.</dd>
<dl>
<dl>
<dt>unrestricted</dt>
<dd> no restrictions (default)</dd>
<dt>sp0&nbsp;<wbr>&nbsp;</dt>
<dd> simple profile at level 0</dd>
<dt>sp1&nbsp;<wbr>&nbsp;</dt>
<dd> simple profile at level 1</dd>
<dt>sp2&nbsp;<wbr>&nbsp;</dt>
<dd> simple profile at level 2</dd>
<dt>sp3&nbsp;<wbr>&nbsp;</dt>
<dd> simple profile at level 3</dd>
<dt>sp4a&nbsp;<wbr>&nbsp;</dt>
<dd> simple profile at level 4a</dd>
<dt>sp5&nbsp;<wbr>&nbsp;</dt>
<dd> simple profile at level 5</dd>
<dt>sp6&nbsp;<wbr>&nbsp;</dt>
<dd> simple profile at level 6</dd>
<dt>asp0&nbsp;</dt>
<dd> advanced simple profile at level 0</dd>
<dt>asp1&nbsp;</dt>
<dd> advanced simple profile at level 1</dd>
<dt>asp2&nbsp;</dt>
<dd> advanced simple profile at level 2</dd>
<dt>asp3&nbsp;</dt>
<dd> advanced simple profile at level 3</dd>
<dt>asp4&nbsp;</dt>
<dd> advanced simple profile at level 4</dd>
<dt>asp5&nbsp;</dt>
<dd> advanced simple profile at level 5</dd>
<dt>dxnhandheld</dt>
<dd> DXN handheld profile</dd>
<dt>dxnportntsc</dt>
<dd> DXN portable NTSC profile</dd>
<dt>dxnportpal</dt>
<dd> DXN portable PAL profile</dd>
<dt>dxnhtntsc</dt>
<dd> DXN home theater NTSC profile</dd>
<dt>dxnhtpal</dt>
<dd> DXN home theater PAL profile</dd>
<dt>dxnhdtv</dt>
<dd> DXN HDTV profile</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>NOTE:</i> These profiles should be used in conjunction with an appropriate -ffourcc. Generally DX50 is applicable, as some players do not recognize Xvid but most recognize DivX.</dd></dl>
<dt><code>par=&lt;mode&gt;</code></dt>
<dd> Specifies the Pixel Aspect Ratio mode (not to be confused with DAR, the Display Aspect Ratio). PAR is the ratio of the width and height of a single pixel. So both are related like this: DAR = PAR * (width/height).<br />
 MPEG-4 defines 5 pixel aspect ratios and one extended one, giving the opportunity to specify a specific pixel aspect ratio. 5 standard modes can be specified:</dd>
<dl>
<dl>
<dt>vga11</dt>
<dd> It is the usual PAR for PC content. Pixels are a square unit.</dd>
<dt>pal43</dt>
<dd> PAL standard 4:3 PAR. Pixels are rectangles.</dd>
<dt>pal169</dt>
<dd> same as above</dd>
<dt>ntsc43</dt>
<dd> same as above</dd>
<dt>ntsc169</dt>
<dd> same as above (Do not forget to give the exact ratio.)</dd>
<dt>ext&nbsp;<wbr>&nbsp;</dt>
<dd> Allows you to specify your own pixel aspect ratio with par_width and par_height.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>NOTE:</i> In general, setting aspect and autoaspect options is enough.</dd></dl>
<dt><code>par_width=&lt;1-255&gt; (par=ext only)</code></dt>
<dd> Specifies the width of the custom pixel aspect ratio.</dd>
<dt><code>par_height=&lt;1-255&gt; (par=ext only)</code></dt>
<dd> Specifies the height of the custom pixel aspect ratio.</dd>
<dt><code>aspect=&lt;x/y | f (float value)&gt;</code></dt>
<dd> Store movie aspect internally, just like MPEG files. Much nicer solution than rescaling, because quality is not decreased. MPlayer and a few others players will play these files correctly, others will display them with the wrong aspect. The aspect parameter can be given as a ratio or a floating point number.</dd>
<dt><code>(no)autoaspect</code></dt>
<dd> Same as the aspect option, but automatically computes aspect, taking into account all the adjustments (crop/expand/scale/etc.) made in the filter chain.</dd>
<dt><code>psnr&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Print the PSNR (peak signal to noise ratio) for the whole video after encoding and store the per frame PSNR in a file with a name like &#8216;psnr_hhmmss.log&#8217; in the current directory. Returned values are in dB (decibel), the higher the better.</dd>
<dt><code>debug&nbsp;<wbr>&nbsp;</code></dt>
<dd> Save per-frame statistics in ./xvid.dbg. (This is not the two pass control file.)</dd></dl>
<p> The following options are only available in Xvid 1.1.x and later.</p>
<dl>
<dt><code>bvhq=&lt;0|1&gt;</code></dt>
<dd> This setting allows vector candidates for B-frames to be used for the encoding chosen using a rate distortion optimized operator, which is what is done for P-frames by the vhq option. This produces nicer-looking B-frames while incurring almost no performance penalty (default: 1).</dd>
<dt><code>vbv_bufsize=&lt;0&#8230;&gt; (two pass mode only)</code></dt>
<dd> Specify the video buffering verifier (VBV) buffer size in bits (default: 0 &#8211; VBV check disabled). VBV allows restricting peak bitrate to make the video play properly on hardware players. For example, the Home profile uses vbv_bufsize=3145728. If you set vbv_bufsize you should set also vbv_maxrate. Note that there is no vbv_peakrate because Xvid does not actually use it for bitrate controlling; the other VBV options are enough to restrict the peak bitrate.</dd>
<dt><code>vbv_initial=&lt;0&#8230;vbv_bufsize&gt; (two pass mode only)</code></dt>
<dd> Specify the initial fill of the VBV buffer in bits (default: 75% of vbv_bufsize). The default is probably what you want.</dd>
<dt><code>vbv_maxrate=&lt;0&#8230;&gt; (two pass mode only)</code></dt>
<dd> Specify the maximum processing rate in bits/s (default: 0). For example, the Home profile uses vbv_maxrate=4854000.</dd></dl>
<p> The following option is only available in Xvid 1.2.x and later.</p>
<dl>
<dt><code>threads=&lt;0-n&gt;</code></dt>
<dd> Create n threads to run the motion estimation (default: 0). The maximum number of threads that can be used is the picture height divided by 16.</dd></dl>
<h3>x264enc (-x264encopts)</h3>
<dl>
<dt><code>bitrate=&lt;value&gt;</code></dt>
<dd> Sets the average bitrate to be used in kbits/second (default: off). Since local bitrate may vary, this average may be inaccurate for very short videos (see ratetol). Constant bitrate can be achieved by combining this with vbv_maxrate, at significant reduction in quality.</dd>
<dt><code>qp=&lt;0-51&gt;</code></dt>
<dd> This selects the quantizer to use for P-frames. I- and B-frames are offset from this value by ip_factor and pb_factor, respectively. 20-40 is a useful range. Lower values result in better fidelity, but higher bitrates. 0 is lossless. Note that quantization in H.264 works differently from MPEG-1/2/4: H.264&#8217;s quantization parameter (QP) is on a logarithmic scale. The mapping is approximately H264QP = 12 + 6*log2(MPEGQP). For example, MPEG at QP=2 is equivalent to H.264 at QP=18. Generally, this option should be avoided and crf should be used instead as crf will yield better visual results for the same size.</dd>
<dt><code>crf=&lt;1.0-50.0&gt;</code></dt>
<dd> Enables constant quality mode, and selects the quality. The scale is similar to QP. Like the bitrate-based modes, this allows each frame to use a different QP based on the frame&#8217;s complexity. This option should generally be used instead of qp.</dd>
<dt><code>crf_max=&lt;float&gt;</code></dt>
<dd> With CRF and VBV, limit RF to this value (may cause VBV underflows!).</dd>
<dt><code>pass=&lt;1-3&gt;</code></dt>
<dd> Enable 2 or 3-pass mode. It is recommended to always encode in 2 or 3-pass mode as it leads to a better bit distribution and improves overall quality.</dd>
<dl>
<dl>
<dt>1</dt>
<dd> first pass</dd>
<dt>2</dt>
<dd> second pass (of two pass encoding)</dd>
<dt>3</dt>
<dd> Nth pass (second and third passes of three pass encoding)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Here is how it works, and how to use it:<br />
 The first pass (pass=1) collects statistics on the video and writes them to a file. You might want to deactivate some CPU-hungry options, apart from the ones that are on by default.<br />
 In two pass mode, the second pass (pass=2) reads the statistics file and bases ratecontrol decisions on it.<br />
 In three pass mode, the second pass (pass=3, that is not a typo) does both: It first reads the statistics, then overwrites them. You can use all encoding options, except very CPU-hungry options.<br />
 The third pass (pass=3) is the same as the second pass, except that it has the second pass&#8217; statistics to work from. You can use all encoding options, including CPU-hungry ones.<br />
 The first pass may use either average bitrate or constant quantizer. ABR is recommended, since it does not require guessing a quantizer. Subsequent passes are ABR, and must specify bitrate.</dd></dl>
<dt><code>profile=&lt;name&gt;</code></dt>
<dd> Constrain options to be compatible with an H.264 profile.</dd>
<dl>
<dl>
<dt>baseline</dt>
<dd> no8x8dct bframes=0 nocabac cqm=flat weightp=0 nointerlaced qp&gt;0</dd>
<dt>main</dt>
<dd> no8x8dct cqm=flat qp&gt;0</dd>
<dt>high</dt>
<dd> qp&gt;0 (default)</dd></dl>
</dl>
<dt><code>preset=&lt;name&gt;</code></dt>
<dd> Use a preset to select encoding settings.</dd>
<dl>
<dl>
<dt>ultrafast</dt>
<dd> no8x8dct aq_mode=0 b_adapt=0 bframes=0 nodeblock nombtree me=dia nomixed_refs partitions=none ref=1 scenecut=0 subq=0 trellis=0 noweight_b weightp=0</dd>
<dt>superfast</dt>
<dd> nombtree me=dia nomixed_refs partitions=i8x8,i4x4 ref=1 subq=1 trellis=0 weightp=0</dd>
<dt>veryfast</dt>
<dd> nombtree nomixed_refs ref=1 subq=2 trellis=0 weightp=0</dd>
<dt>faster</dt>
<dd> nomixed_refs rc_lookahead=20 ref=5 subq=4 weightp=1</dd>
<dt>fast</dt>
<dd> rc_lookahead=30 ref=2 subq=6</dd>
<dt>medium</dt>
<dd> Default settings apply.</dd>
<dt>slow</dt>
<dd> b_adapt=2 direct=auto me=umh rc_lookahead=50 ref=5 subq=8</dd>
<dt>slower</dt>
<dd> b_adapt=2 direct=auto me=umh partitions=all rc_lookahead=60 ref=8 subq=9 trellis=2</dd>
<dt>veryslow</dt>
<dd> b_adapt=2 b_frames=8 direct=auto me=umh me_range=24 partitions=all ref=16 subq=10 trellis=2 rc_lookahead=60</dd>
<dt>placebo</dt>
<dd> bframes=16 b_adapt=2 direct=auto nofast_pskip me=tesa me_range=24 partitions=all rc_lookahead=60 ref=16 subq=10 trellis=2</dd></dl>
</dl>
<dt><code>tune=&lt;name,[name,&#8230;]&gt;</code></dt>
<dd> Tune the settings for a particular type of source or situation. All tuned settings are overridden by explicit user-settings. Multiple tunings are separated by commas, but only one psy tuning can be used at a time.</dd>
<dl>
<dl>
<dt>film (psy tuning)</dt>
<dd> deblock=-1,-1 psy-rd=&lt;unset&gt;,0.15</dd>
<dt>animation (psy tuning)</dt>
<dd> b_frames={+2} deblock=1,1 psy-rd=0.4:&lt;unset&gt; aq_strength=0.6 ref={double if &gt;1 else 1}</dd>
<dt>grain (psy tuning)</dt>
<dd> aq_strength=0.5 nodct_decimate deadzone_inter=6 deadzone_intra=6 deblock=-2,-2 ipratio=1.1 pbratio=1.1 psy-rd=&lt;unset&gt;,0.25 qcomp=0.8</dd>
<dt>stillimage (psy tuning)</dt>
<dd> aq_strength=1.2 deblock=-3,-3 psy-rd=2.0,0.7</dd>
<dt>psnr (psy tuning)</dt>
<dd> aq_mode=0 nopsy</dd>
<dt>ssim (psy tuning)</dt>
<dd> aq_mode=2 nopsy</dd>
<dt>fastdecode</dt>
<dd> nocabac nodeblock noweight_b weightp=0</dd>
<dt>zerolatency</dt>
<dd> bframes=0 force_cfr rc_lookahead=0 sync_lookahead=0 sliced_threads</dd></dl>
</dl>
<dt><code>slow_firstpass</code></dt>
<dd> Disables the following faster options with pass=1: no_8x8dct me=dia partitions=none ref=1 subq={2 if &gt;2 else unchanged} trellis=0 fast_pskip. These settings significantly improve encoding speed while having little or no impact on the quality of the final pass.<br />
 This option is implied with preset=placebo.</dd>
<dt><code>keyint=&lt;value&gt;</code></dt>
<dd> Sets maximum interval between IDR-frames (default: 250). Larger values save bits, thus improve quality, at the cost of seeking precision. Unlike MPEG-1/2/4, H.264 does not suffer from DCT drift with large values of keyint.</dd>
<dt><code>keyint_min=&lt;1-keyint/2&gt;</code></dt>
<dd> Sets minimum interval between IDR-frames (default: auto). If scenecuts appear within this interval, they are still encoded as I-frames, but do not start a new GOP. In H.264, I-frames do not necessarily bound a closed GOP because it is allowable for a P-frame to be predicted from more frames than just the one frame before it (also see frameref). Therefore, I-frames are not necessarily seekable. IDR-frames restrict subsequent P-frames from referring to any frame prior to the IDR-frame.</dd>
<dt><code>scenecut=&lt;-1-100&gt;</code></dt>
<dd> Controls how aggressively to insert extra I-frames (default: 40). With small values of scenecut, the codec often has to force an I-frame when it would exceed keyint. Good values of scenecut may find a better location for the I-frame. Large values use more I-frames than necessary, thus wasting bits. -1 disables scene-cut detection, so I-frames are inserted only once every other keyint frames, even if a scene-cut occurs earlier. This is not recommended and wastes bitrate as scenecuts encoded as P-frames are just as big as I-frames, but do not reset the &quot;keyint counter&quot;.</dd>
<dt><code>(no)intra_refresh</code></dt>
<dd> Periodic intra block refresh instead of keyframes (default: disabled). This option disables IDR-frames, and, instead, uses a moving vertical bar of intra-coded blocks. This reduces compression efficiency but benefits low-latency streaming and resilience to packet loss.</dd>
<dt><code>frameref=&lt;1-16&gt;</code></dt>
<dd> Number of previous frames used as predictors in B- and P-frames (default: 3). This is effective in anime, but in live-action material the improvements usually drop off very rapidly above 6 or so reference frames. This has no effect on decoding speed, but does increase the memory needed for decoding. Some decoders can only handle a maximum of 15 reference frames.</dd>
<dt><code>bframes=&lt;0-16&gt;</code></dt>
<dd> maximum number of consecutive B-frames between I- and P-frames (default: 3)</dd>
<dt><code>(no)b_adapt</code></dt>
<dd> Automatically decides when to use B-frames and how many, up to the maximum specified above (default: on). If this option is disabled, then the maximum number of B-frames is used.</dd>
<dt><code>b_bias=&lt;-100-100&gt;</code></dt>
<dd> Controls the decision performed by b_adapt. A higher b_bias produces more B-frames (default: 0).</dd>
<dt><code>b_pyramid=&lt;normal|strict|none&gt;</code></dt>
<dd> Allows B-frames to be used as references for predicting other frames. For example, consider 3 consecutive B-frames: I0 B1 B2 B3 P4. Without this option, B-frames follow the same pattern as MPEG-[124]. So they are coded in the order I0 P4 B1 B2 B3, and all the B-frames are predicted from I0 and P4. With this option, they are coded as I0 P4 B2 B1 B3. B2 is the same as above, but B1 is predicted from I0 and B2, and B3 is predicted from B2 and P4. This usually results in slightly improved compression, at almost no speed cost. However, this is an experimental option: it is not fully tuned and may not always help. Requires bframes &gt;= 2. Disadvantage: increases decoding delay to 2 frames.</dd>
<dl>
<dl>
<dt>normal</dt>
<dd> Allow B-frames as references as described above (not Blu-ray compatible).</dd>
<dt>strict</dt>
<dd> Disallow P-frames referencing B-frames. Gives worse compression, but is required for Blu-ray compatibility.</dd>
<dt>none&nbsp;</dt>
<dd> Disable using B-frames as references.</dd></dl>
</dl>
<dt><code>(no)open_gop</code></dt>
<dd> Use recovery points to close GOPs; only available with bframes.</dd>
<dt><code>(no)bluray_compat</code></dt>
<dd> Enable compatibility hacks for Blu-Ray support.</dd>
<dt><code>(no)fake_interlaced</code></dt>
<dd> Flag stream as interlaced but encode progressive. Makes it posssible to encode 25p and 30p Blu-Ray streams. Ignored in interlaced mode.</dd>
<dt><code>frame_packing=&lt;0-5&gt;</code></dt>
<dd> Define frame arrangement for stereoscopic videos.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Checkerboard &#8211; pixels are alternately from L and R.</dd>
<dt>1</dt>
<dd> Column alternation &#8211; L and R are interlaced by column.</dd>
<dt>2</dt>
<dd> Row alternation &#8211; L and R are interlaced by row.</dd>
<dt>3</dt>
<dd> Side by side &#8211; L is on the left, R is on the right.</dd>
<dt>4</dt>
<dd> Top-bottom &#8211; L is on top, R is on the bottom.</dd>
<dt>5</dt>
<dd> Frame alternation &#8211; one view per frame.</dd></dl>
</dl>
<dt><code>(no)deblock</code></dt>
<dd> Use deblocking filter (default: on). As it takes very little time compared to its quality gain, it is not recommended to disable it.</dd>
<dt><code>deblock=&lt;-6-6&gt;,&lt;-6-6&gt;</code></dt>
<dd> The first parameter is AlphaC0 (default: 0). This adjusts thresholds for the H.264 in-loop deblocking filter. First, this parameter adjusts the maximum amount of change that the filter is allowed to cause on any one pixel. Secondly, this parameter affects the threshold for difference across the edge being filtered. A positive value reduces blocking artifacts more, but will also smear details.<br />
 The second parameter is Beta (default: 0). This affects the detail threshold. Very detailed blocks are not filtered, since the smoothing caused by the filter would be more noticeable than the original blocking.<br />
 The default behavior of the filter almost always achieves optimal quality, so it is best to either leave it alone, or make only small adjustments. However, if your source material already has some blocking or noise which you would like to remove, it may be a good idea to turn it up a little bit.</dd>
<dt><code>(no)cabac</code></dt>
<dd> Use CABAC (Context-Adaptive Binary Arithmetic Coding) (default: on). Slightly slows down encoding and decoding, but should save 10-15% bitrate. Unless you are looking for decoding speed, you should not disable it.</dd>
<dt><code>qp_min=&lt;1-51&gt; (ABR or two pass)</code></dt>
<dd> Minimum quantizer, 10-30 seems to be a useful range (default: 10).</dd>
<dt><code>qp_max=&lt;1-51&gt; (ABR or two pass)</code></dt>
<dd> maximum quantizer (default: 51)</dd>
<dt><code>qp_step=&lt;1-50&gt; (ABR or two pass)</code></dt>
<dd> maximum value by which the quantizer may be incremented/decremented between frames (default: 4)</dd>
<dt><code>(no)mbtree</code></dt>
<dd> Enable macroblock tree ratecontrol (default: enabled). Use a large lookahead to track temporal propagation of data and weight quality accordingly. In multi-pass mode, this writes to a separate stats file named &lt;passlogfile&gt;.mbtree.</dd>
<dt><code>rc_lookahead=&lt;0-250&gt;</code></dt>
<dd> Adjust the mbtree lookahead distance (default: 40). Larger values will be slower and cause x264 to consume more memory, but can yield higher quality.</dd>
<dt><code>ratetol=&lt;0.1-100.0&gt; (ABR or two pass)</code></dt>
<dd> allowed variance in average bitrate (no particular units) (default: 1.0)</dd>
<dt><code>vbv_maxrate=&lt;value&gt; (ABR or two pass)</code></dt>
<dd> maximum local bitrate, in kbits/second (default: disabled)</dd>
<dt><code>vbv_bufsize=&lt;value&gt; (ABR or two pass)</code></dt>
<dd> averaging period for vbv_maxrate, in kbits (default: none, must be specified if vbv_maxrate is enabled)</dd>
<dt><code>vbv_init=&lt;0.0-1.0&gt; (ABR or two pass)</code></dt>
<dd> initial buffer occupancy, as a fraction of vbv_bufsize (default: 0.9)</dd>
<dt><code>ip_factor=&lt;value&gt;</code></dt>
<dd> quantizer factor between I- and P-frames (default: 1.4)</dd>
<dt><code>pb_factor=&lt;value&gt;</code></dt>
<dd> quantizer factor between P- and B-frames (default: 1.3)</dd>
<dt><code>qcomp=&lt;0-1&gt; (ABR or two pass)</code></dt>
<dd> quantizer compression (default: 0.6). A lower value makes the bitrate more constant, while a higher value makes the quantization parameter more constant.</dd>
<dt><code>cplx_blur=&lt;0-999&gt; (two pass only)</code></dt>
<dd> Temporal blur of the estimated frame complexity, before curve compression (default: 20). Lower values allow the quantizer value to jump around more, higher values force it to vary more smoothly. cplx_blur ensures that each I-frame has quality comparable to the following P-frames, and ensures that alternating high and low complexity frames (e.g. low fps animation) do not waste bits on fluctuating quantizer.</dd>
<dt><code>qblur=&lt;0-99&gt; (two pass only)</code></dt>
<dd> Temporal blur of the quantization parameter, after curve compression (default: 0.5). Lower values allow the quantizer value to jump around more, higher values force it to vary more smoothly.</dd>
<dt><code>zones=&lt;zone0&gt;[/&lt;zone1&gt;[/&#8230;]]</code></dt>
<dd> User specified quality for specific parts (ending, credits, &#8230;). Each zone is &lt;start-frame&gt;,&lt;end-frame&gt;,&lt;option&gt; where option may be</dd>
<dl>
<dl>
<dt>q=&lt;0-51&gt;</dt>
<dd> quantizer</dd>
<dt>b=&lt;0.01-100.0&gt;</dt>
<dd> bitrate multiplier</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>NOTE:</i> The quantizer option is not strictly enforced. It affects only the planning stage of ratecontrol, and is still subject to overflow compensation and qp_min/qp_max.</dd></dl>
<dt><code>direct_pred=&lt;name&gt;</code></dt>
<dd> Determines the type of motion prediction used for direct macroblocks in B-frames.</dd>
<dl>
<dl>
<dt>none</dt>
<dd> Direct macroblocks are not used.</dd>
<dt>spatial</dt>
<dd> Motion vectors are extrapolated from neighboring blocks. (default)</dd>
<dt>temporal</dt>
<dd> Motion vectors are extrapolated from the following P-frame.</dd>
<dt>auto</dt>
<dd> The codec selects between spatial and temporal for each frame.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Spatial and temporal are approximately the same speed and PSNR, the choice between them depends on the video content. Auto is slightly better, but slower. Auto is most effective when combined with multipass. direct_pred=none is both slower and lower quality.</dd></dl>
<dt><code>weightp</code></dt>
<dd> Weighted P-frame prediction mode (default: 2).</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled (fastest)</dd>
<dt>1</dt>
<dd> weighted refs (better quality)</dd>
<dt>2</dt>
<dd> weighted refs + duplicates (best)</dd></dl>
</dl>
<dt><code>(no)weight_b</code></dt>
<dd> Use weighted prediction in B-frames. Without this option, bidirectionally predicted macroblocks give equal weight to each reference frame. With this option, the weights are determined by the temporal position of the B-frame relative to the references. Requires bframes &gt; 1.</dd>
<dt><code>partitions=&lt;list&gt;</code></dt>
<dd> Enable some optional macroblock types (default: p8x8,b8x8,i8x8,i4x4).</dd>
<dl>
<dl>
<dt>p8x8</dt>
<dd> Enable types p16x8, p8x16, p8x8.</dd>
<dt>p4x4</dt>
<dd> Enable types p8x4, p4x8, p4x4. p4x4 is recommended only with subq &gt;= 5, and only at low resolutions.</dd>
<dt>b8x8</dt>
<dd> Enable types b16x8, b8x16, b8x8.</dd>
<dt>i8x8</dt>
<dd> Enable type i8x8. i8x8 has no effect unless 8x8dct is enabled.</dd>
<dt>i4x4</dt>
<dd> Enable type i4x4.</dd>
<dt>all</dt>
<dd> Enable all of the above types.</dd>
<dt>none</dt>
<dd> Disable all of the above types.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> Regardless of this option, macroblock types p16x16, b16x16, and i16x16 are always enabled.<br />
 The idea is to find the type and size that best describe a certain area of the picture. For example, a global pan is better represented by 16&#215;16 blocks, while small moving objects are better represented by smaller blocks.</dd></dl>
<dt><code>(no)8x8dct</code></dt>
<dd> Adaptive spatial transform size: allows macroblocks to choose between 4&#215;4 and 8&#215;8 DCT. Also allows the i8x8 macroblock type. Without this option, only 4&#215;4 DCT is used.</dd>
<dt><code>me=&lt;name&gt;</code></dt>
<dd> Select fullpixel motion estimation algorithm.</dd>
<dl>
<dl>
<dt>dia</dt>
<dd> diamond search, radius 1 (fast)</dd>
<dt>hex</dt>
<dd> hexagon search, radius 2 (default)</dd>
<dt>umh</dt>
<dd> uneven multi-hexagon search (slow)</dd>
<dt>esa</dt>
<dd> exhaustive search (very slow, and no better than umh)</dd></dl>
</dl>
<dt><code>me_range=&lt;4-64&gt;</code></dt>
<dd> radius of exhaustive or multi-hexagon motion search (default: 16)</dd>
<dt><code>subq=&lt;0-11&gt;</code></dt>
<dd> Adjust subpel refinement quality. This parameter controls quality versus speed tradeoffs involved in the motion estimation decision process. subq=5 can compress up to 10% better than subq=1.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Runs fullpixel precision motion estimation on all candidate macroblock types. Then selects the best type with SAD metric (faster than subq=1, not recommended unless you&#8217;re looking for ultra-fast encoding).</dd>
<dt>1</dt>
<dd> Does as 0, then refines the motion of that type to fast quarterpixel precision (fast).</dd>
<dt>2</dt>
<dd> Runs halfpixel precision motion estimation on all candidate macroblock types. Then selects the best type with SATD metric. Then refines the motion of that type to fast quarterpixel precision.</dd>
<dt>3</dt>
<dd> As 2, but uses a slower quarterpixel refinement.</dd>
<dt>4</dt>
<dd> Runs fast quarterpixel precision motion estimation on all candidate macroblock types. Then selects the best type with SATD metric. Then finishes the quarterpixel refinement for that type.</dd>
<dt>5</dt>
<dd> Runs best quality quarterpixel precision motion estimation on all candidate macroblock types, before selecting the best type. Also refines the two motion vectors used in bidirectional macroblocks with SATD metric, rather than reusing vectors from the forward and backward searches.</dd>
<dt>6</dt>
<dd> Enables rate-distortion optimization of macroblock types in I- and P-frames.</dd>
<dt>7</dt>
<dd> Enables rate-distortion optimization of macroblock types in all frames (default).</dd>
<dt>8</dt>
<dd> Enables rate-distortion optimization of motion vectors and intra prediction modes in I- and P-frames.</dd>
<dt>9</dt>
<dd> Enables rate-distortion optimization of motion vectors and intra prediction modes in all frames.</dd>
<dt>10</dt>
<dd> QP-RD; requires trellis=2 and aq_mode=1 or higher (best).</dd>
<dt>11</dt>
<dd> Full RD; disable all early terminations.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> In the above, &quot;all candidates&quot; does not exactly mean all enabled types: 4&#215;4, 4&#215;8, 8&#215;4 are tried only if 8&#215;8 is better than 16&#215;16.</dd></dl>
<dt><code>(no)chroma_me</code></dt>
<dd> Takes into account chroma information during subpixel motion search (default: enabled). Requires subq&gt;=5.</dd>
<dt><code>(no)mixed_refs</code></dt>
<dd> Allows each 8&#215;8 or 16&#215;8 motion partition to independently select a reference frame. Without this option, a whole macroblock must use the same reference. Requires frameref&gt;1.</dd>
<dt><code>trellis=&lt;0-2&gt; (cabac only)</code></dt>
<dd> rate-distortion optimal quantization</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled</dd>
<dt>1</dt>
<dd> enabled only for the final encode (default)</dd>
<dt>2</dt>
<dd> enabled during all mode decisions (slow, requires subq&gt;=6)</dd></dl>
</dl>
<dt><code>psy-rd=rd[,trell]</code></dt>
<dd> Sets the strength of the psychovisual optimization.</dd>
<dl>
<dl>
<dt>rd=&lt;0.0-10.0&gt;</dt>
<dd> psy optimization strength (requires subq&gt;=6) (default: 1.0)</dd>
<dt>trell=&lt;0.0-10.0&gt;</dt>
<dd> trellis (requires trellis, experimental) (default: 0.0)</dd></dl>
</dl>
<dt><code>(no)psy</code></dt>
<dd> Enable psychovisual optimizations that hurt PSNR and SSIM but ought to look better (default: enabled).</dd>
<dt><code>deadzone_inter=&lt;0-32&gt;</code></dt>
<dd> Set the size of the inter luma quantization deadzone for non-trellis quantization (default: 21). Lower values help to preserve fine details and film grain (typically useful for high bitrate/quality encode), while higher values help filter out these details to save bits that can be spent again on other macroblocks and frames (typically useful for bitrate-starved encodes). It is recommended that you start by tweaking deadzone_intra before changing this parameter.</dd>
<dt><code>deadzone_intra=&lt;0-32&gt;</code></dt>
<dd> Set the size of the intra luma quantization deadzone for non-trellis quantization (default: 11). This option has the same effect as deadzone_inter except that it affects intra frames. It is recommended that you start by tweaking this parameter before changing deadzone_inter.</dd>
<dt><code>(no)fast_pskip</code></dt>
<dd> Performs early skip detection in P-frames (default: enabled). This usually improves speed at no cost, but it can sometimes produce artifacts in areas with no details, like sky.</dd>
<dt><code>(no)dct_decimate</code></dt>
<dd> Eliminate dct blocks in P-frames containing only a small single coefficient (default: enabled). This will remove some details, so it will save bits that can be spent again on other frames, hopefully raising overall subjective quality. If you are compressing non-anime content with a high target bitrate, you may want to disable this to preserve as much detail as possible.</dd>
<dt><code>nr=&lt;0-100000&gt;</code></dt>
<dd> Noise reduction, 0 means disabled. 100-1000 is a useful range for typical content, but you may want to turn it up a bit more for very noisy content (default: 0). Given its small impact on speed, you might want to prefer to use this over filtering noise away with video filters like denoise3d or hqdn3d.</dd>
<dt><code>chroma_qp_offset=&lt;-12-12&gt;</code></dt>
<dd> Use a different quantizer for chroma as compared to luma. Useful values are in the range &lt;-2-2&gt; (default: 0).</dd>
<dt><code>aq_mode=&lt;0-2&gt;</code></dt>
<dd> Defines how adaptive quantization (AQ) distributes bits:</dd>
<dl>
<dl>
<dt>0</dt>
<dd> disabled</dd>
<dt>1</dt>
<dd> Avoid moving bits between frames.</dd>
<dt>2</dt>
<dd> Move bits between frames (by default).</dd></dl>
</dl>
<dt><code>aq_strength=&lt;positive float value&gt;</code></dt>
<dd> Controls how much adaptive quantization (AQ) reduces blocking and blurring in flat and textured areas (default: 1.0). A value of 0.5 will lead to weak AQ and less details, when a value of 1.5 will lead to strong AQ and more details.</dd>
<dt><code>cqm=&lt;flat|jvt|&lt;filename&gt;&gt;</code></dt>
<dd> Either uses a predefined custom quantization matrix or loads a JM format matrix file.</dd>
<dl>
<dl>
<dt>flat&nbsp;</dt>
<dd> Use the predefined flat 16 matrix (default).</dd>
<dt>jvt&nbsp;<wbr>&nbsp;</dt>
<dd> Use the predefined JVT matrix.</dd>
<dt>&lt;filename&gt;</dt>
<dd> Use the provided JM format matrix file.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> <i>NOTE:</i> Windows CMD.EXE users may experience problems with parsing the command line if they attempt to use all the CQM lists. This is due to a command line length limitation. In this case it is recommended the lists be put into a JM format CQM file and loaded as specified above.</dd></dl>
<dt><code>cqm4iy=&lt;list&gt; (also see cqm)</code></dt>
<dd> Custom 4&#215;4 intra luminance matrix, given as a list of 16 comma separated values in the 1-255 range.</dd>
<dt><code>cqm4ic=&lt;list&gt; (also see cqm)</code></dt>
<dd> Custom 4&#215;4 intra chrominance matrix, given as a list of 16 comma separated values in the 1-255 range.</dd>
<dt><code>cqm4py=&lt;list&gt; (also see cqm)</code></dt>
<dd> Custom 4&#215;4 inter luminance matrix, given as a list of 16 comma separated values in the 1-255 range.</dd>
<dt><code>cqm4pc=&lt;list&gt; (also see cqm)</code></dt>
<dd> Custom 4&#215;4 inter chrominance matrix, given as a list of 16 comma separated values in the 1-255 range.</dd>
<dt><code>cqm8iy=&lt;list&gt; (also see cqm)</code></dt>
<dd> Custom 8&#215;8 intra luminance matrix, given as a list of 64 comma separated values in the 1-255 range.</dd>
<dt><code>cqm8py=&lt;list&gt; (also see cqm)</code></dt>
<dd> Custom 8&#215;8 inter luminance matrix, given as a list of 64 comma separated values in the 1-255 range.</dd>
<dt><code>level_idc=&lt;10-51&gt;</code></dt>
<dd> Set the bitstream&#8217;s level as defined by annex A of the H.264 standard (default: 51 &#8211; level 5.1). This is used for telling the decoder what capabilities it needs to support. Use this parameter only if you know what it means, and you have a need to set it.</dd>
<dt><code>(no)cpu_independent</code></dt>
<dd> Ensure exact reproducibility across different CPUs instead of chosing different algorithms when available/better (default:enabled).</dd>
<dt><code>threads=&lt;0-16&gt;</code></dt>
<dd> Spawn threads to encode in parallel on multiple CPUs (default: 0). This has a slight penalty to compression quality. 0 or &#8216;auto&#8217; tells x264 to detect how many CPUs you have and pick an appropriate number of threads.</dd>
<dt><code>(no)sliced_threads</code></dt>
<dd> Use slice-based threading (default: disabled). Unlike normal threading, this option adds no encoding latency, but is slightly slower and less effective at compression.</dd>
<dt><code>slice_max_size=&lt;0 or positive integer&gt;</code></dt>
<dd> Maximum slice size in bytes (default: 0). A value of zero disables the maximum.</dd>
<dt><code>slice_max_mbs=&lt;0 or positive integer&gt;</code></dt>
<dd> Maximum slice size in number of macroblocks (default: 0). A value of zero disables the maximum.</dd>
<dt><code>slices=&lt;0 or positive integer&gt;</code></dt>
<dd> Maximum number of slices per frame (default: 0). A value of zero disables the maximum.</dd>
<dt><code>sync_lookahead=&lt;0-250&gt;</code></dt>
<dd> Adjusts the size of the threaded lookahead buffer (default: 0). 0 or &#8216;auto&#8217; tells x264 to automatically determine buffer size.</dd>
<dt><code>(no)deterministic</code></dt>
<dd> Use only deterministic optimizations with multithreaded encoding (default: enabled).</dd>
<dt><code>(no)global_header</code></dt>
<dd> Causes SPS and PPS to appear only once, at the beginning of the bitstream (default: disabled). Some players, such as the Sony PSP, require the use of this option. The default behavior causes SPS and PPS to repeat prior to each IDR frame.</dd>
<dt><code>(no)tff</code></dt>
<dd> Enable interlaced mode, top field first (default: disabled)</dd>
<dt><code>(no)bff</code></dt>
<dd> Enable interlaced mode, bottom field first (default: disabled)</dd>
<dt><code>nal_hrd=&lt;none|vbr|cbr&gt;</code></dt>
<dd> Signal HRD information (requires vbv_bufsize) (default: none).</dd>
<dt><code>(no)pic_struct</code></dt>
<dd> Force pic_struct in Picture Timing SEI (default: disabled).</dd>
<dt><code>(no)constrained_intra</code></dt>
<dd> Enable constrained intra prediction (default: disabled). This significantly reduces compression, but is required for the base layer of SVC encodes.</dd>
<dt><code>output_csp=&lt;i420|i422|i444|rgb&gt;</code></dt>
<dd> Specify output colorspace (default: i420).</dd>
<dt><code>(no)aud</code></dt>
<dd> Write access unit delimeters to the stream (default: disabled). Enable this only if your target container format requires access unit delimiters.</dd>
<dt><code>overscan=&lt;undef|show|crop&gt;</code></dt>
<dd> Include VUI overscan information in the stream (default: disabled). See doc/vui.txt in the x264 source code for more information.</dd>
<dt><code>videoformat=&lt;component|pal|ntsc|secam|mac|undef&gt;</code></dt>
<dd> Include VUI video format information in the stream (default: disabled). This is a purely informative setting for describing the original source. See doc/vui.txt in the x264 source code for more information.</dd>
<dt><code>(no)fullrange</code></dt>
<dd> Include VUI full range information in the stream (default: disabled). Use this option if your source video is not range limited. See doc/vui.txt in the x264 source code for more information.</dd>
<dt><code>colorprim=&lt;bt709|bt470m|bt470bg|smpte170m|smpte240m|film|undef&gt;</code></dt>
<dd> Include color primaries information (default: disabled). This can be used for color correction. See doc/vui.txt in the x264 source code for more information.</dd>
<dt><code>transfer=&lt;bt709|bt470m|bt470bg|linear|log100|log316|smpte170m|smpte240m&gt;</code></dt>
<dd> Include VUI transfer characteristics information in the stream (default: disabled). This can be used for color correction. See doc/vui.txt in the x264 source code for more information.</dd>
<dt><code>colormatrix=&lt;bt709|fcc|bt470bg|smpte170m|smpte240m|GBR|YCgCo&gt;</code></dt>
<dd> Include VUI matrix coefficients in the stream (default: disabled). This can be used for color correction. See doc/vui.txt in the x264 source code for more information.</dd>
<dt><code>chromaloc=&lt;0-5&gt;</code></dt>
<dd> Include VUI chroma sample location information in the stream (default: disabled). Use this option to ensure alignment of the chroma and luma planes after color space conversions. See doc/vui.txt in the x264 source code for more information.</dd>
<dt><code>log=&lt;-1-3&gt;</code></dt>
<dd> Adjust the amount of logging info printed to the screen.</dd>
<dl>
<dl>
<dt>-1</dt>
<dd> none</dd>
<dt> 0</dt>
<dd> Print errors only.</dd>
<dt> 1</dt>
<dd> warnings</dd>
<dt> 2</dt>
<dd> PSNR and other analysis statistics when the encode finishes (default)</dd>
<dt> 3</dt>
<dd> PSNR, QP, frametype, size, and other statistics for every frame</dd></dl>
</dl>
<dt><code>(no)psnr</code></dt>
<dd> Print signal-to-noise ratio statistics.<br />
 <i>NOTE:</i> The &#8216;Y&#8217;, &#8216;U&#8217;, &#8216;V&#8217;, and &#8216;Avg&#8217; PSNR fields in the summary are not mathematically sound (they are simply the average of per-frame PSNRs). They are kept only for comparison to the JM reference codec. For all other purposes, please use either the &#8216;Global&#8217; PSNR, or the per-frame PSNRs printed by log=3.</dd>
<dt><code>(no)ssim</code></dt>
<dd> Print the Structural Similarity Metric results. This is an alternative to PSNR, and may be better correlated with the perceived quality of the compressed video.</dd>
<dt><code>(no)visualize</code></dt>
<dd> Enable x264 visualizations during encoding. If the x264 on your system supports it, a new window will be opened during the encoding process, in which x264 will attempt to present an overview of how each frame gets encoded. Each block type on the visualized movie will be colored as follows:</dd>
<dt><code>dump_yuv=&lt;file name&gt;</code></dt>
<dd> Dump YUV frames to the specified file. For debugging use.</dd>
<dl>
<dl>
<dt>red/pink</dt>
<dd> intra block</dd>
<dt>blue&nbsp;</dt>
<dd> inter block</dd>
<dt>green</dt>
<dd> skip block</dd>
<dt>yellow</dt>
<dd> B-block</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> This feature can be considered experimental and subject to change. In particular, it depends on x264 being compiled with visualizations enabled. Note that as of writing this, x264 pauses after encoding and visualizing each frame, waiting for the user to press a key, at which point the next frame will be encoded.</dd></dl>
</dl>
<h3>xvfw (-xvfwopts)</h3>
<p> Encoding with Video for Windows codecs is mostly obsolete unless you wish to encode to some obscure fringe codec.</p>
<dl>
<dt><code>codec=&lt;name&gt;</code></dt>
<dd> The name of the binary codec file with which to encode.</dd>
<dt><code>compdata=&lt;file&gt;</code></dt>
<dd> The name of the codec settings file (like firstpass.mcf) created by vfw2menc.</dd></dl>
<h3>MPEG muxer (-mpegopts)</h3>
<p> The MPEG muxer can generate 5 types of streams, each of which has reasonable default parameters that the user can override. Generally, when generating MPEG files, it is advisable to disable MEncoder&#8217;s frame-skip code (see -noskip, -mc as well as the harddup and softskip video filters). </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dl>
<dt>format=mpeg2:tsaf:vbitrate=8000</dt>
<dd></dd></dl>
</dl>
<dl>
<dt><code>format=&lt;mpeg1 | mpeg2 | xvcd | xsvcd | dvd | pes1 | pes2&gt;</code></dt>
<dd> stream format (default: mpeg2). pes1 and pes2 are very broken formats (no pack header and no padding), but VDR uses them; do not choose them unless you know exactly what you are doing.</dd>
<dt><code>size=&lt;up to 65535&gt;</code></dt>
<dd> Pack size in bytes, do not change unless you know exactly what you are doing (default: 2048).</dd>
<dt><code>muxrate=&lt;int&gt;</code></dt>
<dd> Nominal muxrate in kbit/s used in the pack headers (default: 1800 kb/s). Will be updated as necessary in the case of &#8216;format=mpeg1&#8217; or &#8216;mpeg2&#8217;.</dd>
<dt><code>tsaf&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> Sets timestamps on all frames, if possible; recommended when format=dvd. If dvdauthor complains with a message like &quot;..audio sector out of range&#8230;&quot;, you probably did not enable this option.</dd>
<dt><code>interleaving2</code></dt>
<dd> Uses a better algorithm to interleave audio and video packets, based on the principle that the muxer will always try to fill the stream with the largest percentage of free space.</dd>
<dt><code>vdelay=&lt;1-32760&gt;</code></dt>
<dd> Initial video delay time, in milliseconds (default: 0), use it if you want to delay video with respect to audio. It doesn&#8217;t work with :drop.</dd>
<dt><code>adelay=&lt;1-32760&gt;</code></dt>
<dd> Initial audio delay time, in milliseconds (default: 0), use it if you want to delay audio with respect to video.</dd>
<dt><code>drop&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></dt>
<dd> When used with vdelay the muxer drops the part of audio that was anticipated.</dd>
<dt><code>vwidth, vheight=&lt;1-4095&gt;</code></dt>
<dd> Set the video width and height when video is MPEG-1/2.</dd>
<dt><code>vpswidth, vpsheight=&lt;1-4095&gt;</code></dt>
<dd> Set pan and scan video width and height when video is MPEG-2.</dd>
<dt><code>vaspect=&lt;1 | 4/3 | 16/9 | 221/100&gt;</code></dt>
<dd> Sets the display aspect ratio for MPEG-2 video. Do not use it on MPEG-1 or the resulting aspect ratio will be completely wrong.</dd>
<dt><code>vbitrate=&lt;int&gt;</code></dt>
<dd> Sets the video bitrate in kbit/s for MPEG-1/2 video.</dd>
<dt><code>vframerate=&lt;24000/1001 | 24 | 25 | 30000/1001 | 30 | 50 | 60000/1001 | 60 &gt;</code></dt>
<dd> Sets the framerate for MPEG-1/2 video. This option will be ignored if used with the telecine option.</dd>
<dt><code>telecine</code></dt>
<dd> Enables 3:2 pulldown soft telecine mode: The muxer will make the video stream look like it was encoded at 30000/1001 fps. It only works with MPEG-2 video when the output framerate is 24000/1001 fps, convert it with -ofps if necessary. Any other framerate is incompatible with this option.</dd>
<dt><code>film2pal</code></dt>
<dd> Enables FILM to PAL and NTSC to PAL soft telecine mode: The muxer will make the video stream look like it was encoded at 25 fps. It only works with MPEG-2 video when the output framerate is 24000/1001 fps, convert it with -ofps if necessary. Any other framerate is incompatible with this option.</dd>
<dt><code>tele_src and tele_dest</code></dt>
<dd> Enables arbitrary telecining using Donand Graft&#8217;s DGPulldown code. You need to specify the original and the desired framerate; the muxer will make the video stream look like it was encoded at the desired framerate. It only works with MPEG-2 video when the input framerate is smaller than the output framerate and the framerate increase is &lt;= 1.5. </dd>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>tele_src=25,tele_dest=30000/1001</dt>
<dd> PAL to NTSC telecining</dd></dl>
</dl>
<dt><code>vbuf_size=&lt;40-1194&gt;</code></dt>
<dd> Sets the size of the video decoder&#8217;s buffer, expressed in kilobytes. Specify it only if the bitrate of the video stream is too high for the chosen format and if you know perfectly well what you are doing. A too high value may lead to an unplayable movie, depending on the player&#8217;s capabilities. When muxing HDTV video a value of 400 should suffice.</dd>
<dt><code>abuf_size=&lt;4-64&gt;</code></dt>
<dd> Sets the size of the audio decoder&#8217;s buffer, expressed in kilobytes. The same principle as for vbuf_size applies.</dd></dl>
<h3>FFmpeg libavformat demuxers (-lavfdopts)</h3>
<dl>
<dt><code>analyzeduration=&lt;value&gt;</code></dt>
<dd> Maximum length in seconds to analyze the stream properties.</dd>
<dt><code>format=&lt;value&gt;</code></dt>
<dd> Force a specific libavformat demuxer.</dd>
<dt><code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></dt>
<dd> Pass AVOptions to libavformat demuxer. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some options may conflict with MPlayer/MEncoder options. </dd>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>o=ignidx</dt>
<dd></dd></dl>
</dl>
<dt><code>probesize=&lt;value&gt;</code></dt>
<dd> Maximum amount of data to probe during the detection phase. In the case of MPEG-TS this value identifies the maximum number of TS packets to scan.</dd>
<dt><code>cryptokey=&lt;hexstring&gt;</code></dt>
<dd> Encryption key the demuxer should use. This is the raw binary data of the key converted to a hexadecimal string.</dd></dl>
<h3>FFmpeg libavformat muxers (-lavfopts) (also see -of lavf)</h3>
<dl>
<dt><code>delay=&lt;value&gt;</code></dt>
<dd> Currently only meaningful for MPEG[12]: Maximum allowed distance, in seconds, between the reference timer of the output stream (SCR) and the decoding timestamp (DTS) for any stream present (demux to decode delay). Default is 0.7 (as mandated by the standards defined by MPEG). Higher values require larger buffers and must not be used.</dd>
<dt><code>format=&lt;container_format&gt;</code></dt>
<dd> Override which container format to mux into (default: autodetect from output file extension).</dd>
<dl>
<dl>
<dt>mpg&nbsp;<wbr>&nbsp;</dt>
<dd> MPEG-1 systems and MPEG-2 PS</dd>
<dt>asf&nbsp;<wbr>&nbsp;</dt>
<dd> Advanced Streaming Format</dd>
<dt>avi&nbsp;<wbr>&nbsp;</dt>
<dd> Audio Video Interleave file</dd>
<dt>wav&nbsp;<wbr>&nbsp;</dt>
<dd> Waveform Audio</dd>
<dt>swf&nbsp;<wbr>&nbsp;</dt>
<dd> Macromedia Flash</dd>
<dt>flv&nbsp;<wbr>&nbsp;</dt>
<dd> Macromedia Flash video files</dd>
<dt>rm&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> RealAudio and RealVideo</dd>
<dt>au&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> SUN AU format</dd>
<dt>nut&nbsp;<wbr>&nbsp;</dt>
<dd> NUT open container format (experimental)</dd>
<dt>mov&nbsp;<wbr>&nbsp;</dt>
<dd> QuickTime</dd>
<dt>mp4&nbsp;<wbr>&nbsp;</dt>
<dd> MPEG-4 format</dd>
<dt>ipod&nbsp;</dt>
<dd> MPEG-4 format with extra header flags required by Apple iPod firmware</dd>
<dt>dv&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Sony Digital Video container</dd>
<dt>matroska&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt>
<dd> Matroska</dd></dl>
</dl>
<dt><code>muxrate=&lt;rate&gt;</code></dt>
<dd> Nominal bitrate of the multiplex, in bits per second; currently it is meaningful only for MPEG[12]. Sometimes raising it is necessary in order to avoid &quot;buffer underflows&quot;.</dd>
<dt><code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></dt>
<dd> Pass AVOptions to libavformat muxer. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some options may conflict with MEncoder options. </dd>
<dl>
<dt>
</dt><dd> <i>EXAMPLE:</i></dd></dl>
<dl>
<dl>
<dt>o=packetsize=100</dt>
<dd></dd></dl>
</dl>
<dt><code>packetsize=&lt;size&gt;</code></dt>
<dd> Size, expressed in bytes, of the unitary packet for the chosen format. When muxing to MPEG[12] implementations the default values are: 2324 for [S]VCD, 2048 for all others formats.</dd>
<dt><code>preload=&lt;distance&gt;</code></dt>
<dd> Currently only meaningful for MPEG[12]: Initial distance, in seconds, between the reference timer of the output stream (SCR) and the decoding timestamp (DTS) for any stream present (demux to decode delay).</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> There are a number of environment variables that can be used to control the behavior of MPlayer and MEncoder.</p>
<dl>
<dt><code>MPLAYER_CHARSET (also see -msgcharset)</code></dt>
<dd> Convert console messages to the specified charset (default: autodetect). A value of &quot;noconv&quot; means no conversion.</dd>
<dt><code>MPLAYER_HOME</code></dt>
<dd> Directory where MPlayer looks for user settings.</dd>
<dt><code>MPLAYER_VERBOSE (also see -v and -msglevel)</code></dt>
<dd> Set the initial verbosity level across all message modules (default: 0). The resulting verbosity corresponds to that of -msglevel 5 plus the value of MPLAYER_VERBOSE.</dd></dl>
<h3>libaf:</h3>
<dl>
<dt><code>LADSPA_PATH</code></dt>
<dd> If LADSPA_PATH is set, it searches for the specified file. If it is not set, you must supply a fully specified pathname. FIXME: This is also mentioned in the ladspa section.</dd></dl>
<h3>libdvdcss:</h3>
<dl>
<dt><code>DVDCSS_CACHE</code></dt>
<dd> Specify a directory in which to store title key values. This will speed up descrambling of DVDs which are in the cache. The DVDCSS_CACHE directory is created if it does not exist, and a subdirectory is created named after the DVD&#8217;s title or manufacturing date. If DVDCSS_CACHE is not set or is empty, libdvdcss will use the default value which is &quot;${HOME}/.dvdcss/&quot; under Unix and &quot;C:\Documents and Settings\$USER\Application Data\dvdcss\&quot; under Win32. The special value &quot;off&quot; disables caching.</dd>
<dt><code>DVDCSS_METHOD</code></dt>
<dd> Sets the authentication and decryption method that libdvdcss will use to read scrambled discs. Can be one of title, key or disc.</dd>
<dl>
<dl>
<dt>key&nbsp;<wbr>&nbsp;</dt>
<dd> is the default method. libdvdcss will use a set of calculated player keys to try and get the disc key. This can fail if the drive does not recognize any of the player keys.</dd>
<dt>disc&nbsp;</dt>
<dd> is a fallback method when key has failed. Instead of using player keys, libdvdcss will crack the disc key using a brute force algorithm. This process is CPU intensive and requires 64 MB of memory to store temporary data.</dd>
<dt>title</dt>
<dd> is the fallback when all other methods have failed. It does not rely on a key exchange with the DVD drive, but rather uses a crypto attack to guess the title key. On rare cases this may fail because there is not enough encrypted data on the disc to perform a statistical attack, but in the other hand it is the only way to decrypt a DVD stored on a hard disc, or a DVD with the wrong region on an RPC2 drive.</dd></dl>
</dl>
<dt><code>DVDCSS_RAW_DEVICE</code></dt>
<dd> Specify the raw device to use. Exact usage will depend on your operating system, the Linux utility to set up raw devices is <a href="/docs/linux/man/8-raw/">raw</a>(8) for instance. Please note that on most operating systems, using a raw device requires highly aligned buffers: Linux requires a 2048 bytes alignment (which is the size of a DVD sector).</dd>
<dt><code>DVDCSS_VERBOSE</code></dt>
<dd> Sets the libdvdcss verbosity level.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Outputs no messages at all.</dd>
<dt>1</dt>
<dd> Outputs error messages to stderr.</dd>
<dt>2</dt>
<dd> Outputs error messages and debug messages to stderr.</dd></dl>
</dl>
<dt><code>DVDREAD_NOKEYS</code></dt>
<dd> Skip retrieving all keys on startup. Currently disabled.</dd>
<dt><code>HOME</code></dt>
<dd> FIXME: Document this.</dd></dl>
<h3>libao2:</h3>
<dl>
<dt><code>AO_SUN_DISABLE_SAMPLE_TIMING</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>AUDIODEV</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>AUDIOSERVER</code></dt>
<dd> Specifies the Network Audio System server to which the nas audio output driver should connect and the transport that should be used. If unset DISPLAY is used instead. The transport can be one of tcp and unix. Syntax is tcp/&lt;somehost&gt;:&lt;someport&gt;, &lt;somehost&gt;:&lt;instancenumber&gt; or [unix]:&lt;instancenumber&gt;. The NAS base port is 8000 and &lt;instancenumber&gt; is added to that. </dd>
<dl>
<dt>
</dt><dd> <i>EXAMPLES:</i></dd></dl>
<dl>
<dl>
<dt>AUDIOSERVER=somehost:0</dt>
<dd> Connect to NAS server on somehost using default port and transport.</dd>
<dt>AUDIOSERVER=tcp/somehost:8000</dt>
<dd> Connect to NAS server on somehost listening on TCP port 8000.</dd>
<dt>AUDIOSERVER=(unix)?:0</dt>
<dd> Connect to NAS server instance 0 on localhost using unix domain sockets.</dd></dl>
</dl>
<dt><code>DISPLAY</code></dt>
<dd> FIXME: Document this.</dd></dl>
<h3>vidix:</h3>
<dl>
<dt><code>VIDIX_CRT</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>VIDIXIVTVALPHA</code></dt>
<dd> Set this to &#8216;disable&#8217; in order to stop the VIDIX driver from controlling alphablending settings. You can then manipulate it yourself with &#8216;ivtvfbctl&#8217;.</dd></dl>
<h3>osdep:</h3>
<dl>
<dt><code>TERM</code></dt>
<dd> FIXME: Document this.</dd></dl>
<h3>libvo:</h3>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>FRAMEBUFFER</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>HOME</code></dt>
<dd> FIXME: Document this.</dd></dl>
<h3>libmpdemux:</h3>
<dl>
<dt><code>HOME</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>HOMEPATH</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>http_proxy</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>LOGNAME</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>USERPROFILE</code></dt>
<dd> FIXME: Document this.</dd></dl>
<h3>GUI:</h3>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> The name of the display to which the GUI should connect.</dd>
<dt><code>HOME</code></dt>
<dd> The home directory of the current user.</dd></dl>
<h3>libavformat:</h3>
<dl>
<dt><code>AUDIO_FLIP_LEFT</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>BKTR_DEV</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>BKTR_FORMAT</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>BKTR_FREQUENCY</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>http_proxy</code></dt>
<dd> FIXME: Document this.</dd>
<dt><code>no_proxy</code></dt>
<dd> FIXME: Document this.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>/usr/local/etc/mplayer/mplayer.conf</dt>
<dd> MPlayer system-wide settings</dd>
<dt>/usr/local/etc/mplayer/mencoder.conf</dt>
<dd> MEncoder system-wide settings</dd>
<dt>~/.mplayer/config</dt>
<dd> MPlayer user settings</dd>
<dt>~/.mplayer/mencoder.conf</dt>
<dd> MEncoder user settings</dd>
<dt>~/.mplayer/input.conf</dt>
<dd> input bindings (see &#8216;-input keylist&#8217; for the full list)</dd>
<dt>~/.mplayer/gui.conf</dt>
<dd> GUI configuration file</dd>
<dt>~/.mplayer/gui.gain</dt>
<dd> for audio files not containing ReplayGain data, add a line with replay gain and filename separated by a space character, e.g. </dd>
<p> +1.50 /home/me/music/Song.mp3</p>
<dt>~/.mplayer/gui.history</dt>
<dd> GUI directory history</dd>
<dt>~/.mplayer/gui.pl</dt>
<dd> GUI playlist</dd>
<dt>~/.mplayer/gui.url</dt>
<dd> GUI URL list</dd>
<dt>~/.mplayer/font/</dt>
<dd> font directory (There must be a font.desc file and files with .RAW extension.)</dd>
<dt>~/.mplayer/DVDkeys/</dt>
<dd> cached CSS keys</dd></dl>
<h2>EXAMPLES OF MPLAYER USAGE</h2>
<p> <code>Quickstart Blu-ray playing:</code> </p>
<pre>
mplayer br:////path/to/disc
mplayer br:// -bluray-device /path/to/disc
</pre>
<p> <code>Quickstart DVD playing:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a>
</pre>
<p> <code>Play in Japanese with English subtitles:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a> -alang ja -slang en
</pre>
<p> <code>Play only chapters 5, 6, 7:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a> -chapter 5-7
</pre>
<p> <code>Play only titles 5, 6, 7:</code> </p>
<pre>
mplayer <a href="dvd://5-7">dvd://5-7</a>
</pre>
<p> <code>Play a multiangle DVD:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a> -dvdangle 2
</pre>
<p> <code>Play from a different DVD device:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a> -dvd-device /dev/dvd2
</pre>
<p> <code>Play DVD video from a directory with VOB files:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a> -dvd-device /path/to/directory/
</pre>
<p> <code>Copy a DVD title to hard disk, saving to file title1.vob:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a> -dumpstream -dumpfile title1.vob
</pre>
<p> <code>Play a DVD with dvdnav from path /dev/sr1:</code> </p>
<pre>
mplayer <a href="dvdnav:////dev/sr1">dvdnav:////dev/sr1</a>
</pre>
<p> <code>Stream from HTTP:</code> </p>
<pre>
mplayer <a rel="nofollow" href="http://mplayer.hq/example.avi">http://mplayer.hq/example.avi</a>
</pre>
<p> <code>Stream using RTSP:</code> </p>
<pre>
mplayer <a href="rtsp://server.example.com/streamName">rtsp://server.example.com/streamName</a>
</pre>
<p> <code>Convert subtitles to MPsub format:</code> </p>
<pre>
mplayer dummy.avi -sub source.sub -dumpmpsub
</pre>
<p> <code>Convert subtitles to MPsub format without watching the movie:</code> </p>
<pre>
mplayer /dev/zero -rawvideo pal:fps=xx -demuxer rawvideo -vc null -vo null -noframedrop -benchmark -sub source.sub -dumpmpsub
</pre>
<p> <code>input from standard V4L:</code> </p>
<pre>
mplayer tv:// -tv driver=v4l:width=640:height=480:outfmt=i420 -vc rawi420 -vo xv
</pre>
<p> <code>Playback on Zoran cards (old style, deprecated):</code> </p>
<pre>
mplayer -vo zr -vf scale=352:288 file.avi
</pre>
<p> <code>Playback on Zoran cards (new style):</code> </p>
<pre>
mplayer -vo zr2 -vf scale=352:288,zrmjpeg file.avi
</pre>
<p> <code>Play DTS-CD with passthrough:</code> </p>
<pre>
mplayer -ac hwdts -rawaudio format=0x2001 -cdrom-device /dev/cdrom cdda://
</pre>
<p> You can also use -afm hwac3 instead of -ac hwdts. Adjust &#8216;/dev/cdrom&#8217; to match the CD-ROM device on your system. If your external receiver supports decoding raw DTS streams, you can directly play it via cdda:// without setting format, hwac3 or hwdts. </p>
<p> <code>Play a 6-channel AAC file with only two speakers:</code> </p>
<pre>
mplayer -rawaudio format=0xff -demuxer rawaudio -af pan=2:.32:.32:.39:.06:.06:.39:.17:-.17:-.17:.17:.33:.33 adts_he-aac160_51.aac
</pre>
<p> You might want to play a bit with the pan values (e.g multiply with a value) to increase volume or avoid clipping. </p>
<p> <code>checkerboard invert with geq filter:</code> </p>
<pre>
mplayer -vf geq='128+(p(X\,Y)-128)*(0.5-gt(mod(X/SW\,128)\,64))*(0.5-gt(mod(Y/SH\,128)\,64))*4'
</pre>
<h2>EXAMPLES OF MENCODER USAGE</h2>
<p> <code>Encode DVD title #2, only selected chapters:</code> </p>
<pre>
mencoder <a href="dvd://2">dvd://2</a> -chapter 10-15 -o title2.avi -oac copy -ovc lavc -lavcopts vcodec=mpeg4
</pre>
<p> <code>Encode DVD title #2, resizing to 640&#215;480:</code> </p>
<pre>
mencoder <a href="dvd://2">dvd://2</a> -vf scale=640:480 -o title2.avi -oac copy -ovc lavc -lavcopts vcodec=mpeg4
</pre>
<p> <code>Encode DVD title #2, resizing to 512xHHH (keep aspect ratio):</code> </p>
<pre>
mencoder <a href="dvd://2">dvd://2</a> -vf scale -zoom -xy 512 -o title2.avi -oac copy -ovc lavc -lavcopts vcodec=mpeg4
</pre>
<p> <code>The same, but with bitrate set to 1800kbit and optimized macroblocks:</code> </p>
<pre>
mencoder <a href="dvd://2">dvd://2</a> -o title2.avi -oac copy -ovc lavc -lavcopts vcodec=mpeg4:mbd=1:vbitrate=1800
</pre>
<p> <code>The same, but with MJPEG compression:</code> </p>
<pre>
mencoder <a href="dvd://2">dvd://2</a> -o title2.avi -oac copy -ovc lavc -lavcopts vcodec=mjpeg:mbd=1:vbitrate=1800
</pre>
<p> <code>Encode all *.jpg files in the current directory:</code> </p>
<pre>
mencoder &quot;mf://*.jpg&quot; -mf fps=25 -o output.avi -ovc lavc -lavcopts vcodec=mpeg4
</pre>
<p> <code>Encode from a tuner (specify a format with -vf format):</code> </p>
<pre>
mencoder -tv driver=v4l:width=640:height=480 tv:// -o tv.avi -ovc raw
</pre>
<p> <code>Encode from a pipe:</code> </p>
<pre>
rar p test-SVCD.rar | mencoder -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=800 -ofps 24 -
</pre>
<h2>BUGS</h2>
<p> Don&#8217;t panic. If you find one, report it to us, but please make sure you have read all of the documentation first. Also look out for smileys. :) Many bugs are the result of incorrect setup or parameter usage. The bug reporting section of the documentation (<a rel="nofollow" href="http://www.mplayerhq.hu/DOCS/HTML/en/bugreports.html)">http://www.mplayerhq.hu/DOCS/HTML/en/bugreports.html)</a> explains how to create useful bug reports.</p>
<h2>AUTHORS</h2>
<p> MPlayer was initially written by Arpad Gereoffy. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> MPlayer is (C) 2000-2019 The MPlayer Team </p>
<p> This man page was written mainly by Gabucino, Jonas Jermann and Diego Biurrun. It is maintained by Diego Biurrun. Please send mails about it to the MPlayer-DOCS mailing list. Translation specific mails belong on the MPlayer-translations mailing list. </p>
