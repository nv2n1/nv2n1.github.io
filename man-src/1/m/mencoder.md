---
title: "mencoder(1)"
name: "mencoder"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mencoder/"
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
 <code>gmplayer</code> [options] [-skin skin]<br />
 <code>mencoder</code> [options] file [file|URL|-] [-o file | file://file | <a href="smb://[user:pass@]host/filepath]">smb://[user:pass@]host/filepath]</a><br />
 <code>mencoder</code> [options] file1 [specific options] [file2] [specific options]</p>
<h2>DESCRIPTION</h2>
<p> <code>mplayer</code> is a movie player for Linux (runs on many other platforms and CPU architectures, see the documentation). It plays most MPEG/:VOB, AVI, ASF/:WMA/:WMV, RM, QT/:MOV/:MP4, Ogg/:OGM, MKV, VIVO, FLI, NuppelVideo, yuv4mpeg, FILM and RoQ files, supported by many native and binary codecs. You can watch VCD, SVCD, DVD, Blu-ray, 3ivx, DivX 3/4/5, WMV and even H.264 movies, too. </p>
<p> MPlayer supports a wide range of video and audio output drivers. It works with X11, Xv, DGA, OpenGL, SVGAlib, fbdev, AAlib, libcaca, DirectFB, Quartz, Mac OS X CoreVideo, but you can also use GGI, SDL (and all their drivers), VESA (on every VESA-compatible card, even without X11), some low-level card-specific drivers (for Matrox, 3dfx and ATI) and some hardware MPEG decoder boards, such as the Siemens DVB, Hauppauge PVR (IVTV), DXR2 and DXR3/:Hollywood+. Most of them support software or hardware scaling, so you can enjoy movies in fullscreen mode. </p>
<p> MPlayer has an onscreen display (OSD) for status information, nice big antialiased shaded subtitles and visual feedback for keyboard controls. European/:ISO8859-1,2 (Hungarian, English, Czech, etc), Cyrillic and Korean fonts are supported along with 12 subtitle formats (MicroDVD, SubRip, OGM, SubViewer, Sami, VPlayer, RT, SSA, AQTitle, JACOsub, PJS and our own: MPsub) and DVD subtitles (SPU streams, VOBsub and Closed Captions). </p>
<p> <code>mencoder</code> (MPlayer&#8217;s Movie Encoder) is a simple movie encoder, designed to encode MPlayer-playable movies (see above) to other MPlayer-playable formats (see below). It encodes to MPEG-4 (DivX/Xvid), one of the libavcodec codecs and PCM/:MP3/:VBRMP3 audio in 1, 2 or 3 passes. Furthermore it has stream copying abilities, a powerful filter system (crop, expand, flip, postprocess, rotate, scale, noise, RGB/:YUV conversion) and more. </p>
<p> <code>gmplayer</code> is MPlayer with a graphical user interface. Besides some own options (stored in gui.conf), it has the same options as MPlayer, however some MPlayer options will be stored in gui.conf so that they can be chosen independently from MPlayer. (See GUI CONFIGURATION FILE below.) </p>
<p> Usage examples to get you started quickly can be found at the end of this man page. </p>
<p> <code>Also see the HTML documentation!</code></p>
<h2>INTERACTIVE CONTROL</h2>
<p> MPlayer has a fully configurable, command-driven control layer which allows you to control MPlayer using keyboard, mouse, joystick or remote control (with LIRC). See the -input option for ways to customize it.</p>
<dl>
<dt><code>keyboard control</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>LEFT and RIGHT</p>
<dd> Seek backward/:forward 10 seconds.</p>
<dt>UP and DOWN</p>
<dd> Seek forward/:backward 1 minute.</p>
<dt>PGUP and PGDWN</p>
<dd> Seek forward/:backward 10 minutes.</p>
<dt>[ and ]</p>
<dd> Decrease/increase current playback speed by 10%.</p>
<dt>{ and }</p>
<dd> Halve/double current playback speed.</p>
<dt>BACKSPACE</p>
<dd> Reset playback speed to normal.</p>
<dt>&lt; and &gt;</p>
<dd> Go backward/:forward in the playlist.</p>
<dt>ENTER</p>
<dd> Go forward in the playlist, even over the end.</p>
<dt>HOME and END</p>
<dd> next/:previous playtree entry in the parent list</p>
<dt>INS and DEL (ASX playlist only)</p>
<dd> next/:previous alternative source.</p>
<dt>p / SPACE</p>
<dd> Pause (pressing again unpauses).</p>
<dt>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Step forward. Pressing once will pause movie, every consecutive press will play one frame and then go into pause mode again (any other key unpauses).</p>
<dt>q / ESC</p>
<dd> Stop playing and quit.</p>
<dt>U&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Stop playing (and quit if -idle is not used).</p>
<dt>+ and &#8211;</p>
<dd> Adjust audio delay by +/- 0.1 seconds.</p>
<dt>/ and *</p>
<dd> Decrease/:increase volume.</p>
<dt>9 and 0</p>
<dd> Decrease/:increase volume.</p>
<dt>( and )</p>
<dd> Adjust audio balance in favor of left/:right channel.</p>
<dt>m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Mute sound.</p>
<dt>_ (MPEG-TS, AVI and libavformat only)</p>
<dd> Cycle through the available video tracks.</p>
<dt># (DVD, Blu-ray, MPEG, Matroska, AVI and libavformat only)</p>
<dd> Cycle through the available audio tracks.</p>
<dt>TAB (MPEG-TS and libavformat only)</p>
<dd> Cycle through the available programs.</p>
<dt>f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Toggle fullscreen (also see -fs).</p>
<dt>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Toggle stay-on-top (also see -ontop).</p>
<dt>w and e</p>
<dd> Decrease/:increase pan-and-scan range.</p>
<dt>o&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Toggle OSD states: none / seek / seek + timer / seek + timer + total time.</p>
<dt>d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Toggle frame dropping states: none / skip display / skip decoding (see -framedrop and -hardframedrop).</p>
<dt>v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Toggle subtitle visibility.</p>
<dt>j and J</p>
<dd> Cycle through the available subtitles.</p>
<dt>y and g</p>
<dd> Step forward/backward in the subtitle list.</p>
<dt>F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Toggle displaying &quot;forced subtitles&quot;.</p>
<dt>a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Toggle subtitle alignment: top / middle / bottom.</p>
<dt>x and z</p>
<dd> Adjust subtitle delay by +/- 0.1 seconds.</p>
<dt>c (-capture only)</p>
<dd> Start/stop capturing the primary stream.</p>
<dt>r and t</p>
<dd> Move subtitles up/down.</p>
<dt>i (-edlout mode only)</p>
<dd> Set start or end of an EDL skip and write it out to the given file.</p>
<dt>s (-vf screenshot only)</p>
<dd> Take a screenshot.</p>
<dt>S (-vf screenshot only)</p>
<dd> Start/stop taking screenshots.</p>
<dt>I&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Show filename on the OSD.</p>
<dt>P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Show progression bar, elapsed time and total duration on the OSD.</p>
<dt>! and @</p>
<dd> Seek to the beginning of the previous/next chapter.</p>
<dt>D (-vo xvmc, -vo vdpau, -vf yadif, -vf kerndeint only)</p>
<dd> Activate/deactivate deinterlacer.</p>
<dt>A</p>
<dd> Cycle through the available DVD angles.</dl>
</dl>
</dl>
<dl>
<dt>
<dd> (The following keys are valid only when using a hardware accelerated video output (xv, (x)vidix, (x)mga, etc), the software equalizer (-vf eq or -vf eq2) or hue filter (-vf hue).)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>1 and 2</p>
<dd> Adjust contrast.</p>
<dt>3 and 4</p>
<dd> Adjust brightness.</p>
<dt>5 and 6</p>
<dd> Adjust hue.</p>
<dt>7 and 8</p>
<dd> Adjust saturation.</dl>
</dl>
<dl>
<dt>
<dd> (The following keys are valid only when using the quartz or corevideo video output driver.)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>command + 0</p>
<dd> Resize movie window to half its original size.</p>
<dt>command + 1</p>
<dd> Resize movie window to its original size.</p>
<dt>command + 2</p>
<dd> Resize movie window to double its original size.</p>
<dt>command + f</p>
<dd> Toggle fullscreen (also see -fs).</p>
<dt>command + [ and command + ]</p>
<dd> Set movie window alpha.</dl>
</dl>
<dl>
<dt>
<dd> (The following keys are valid only when using the sdl video output driver.)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Cycle through available fullscreen modes.</p>
<dt>n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Restore original mode.</dl>
</dl>
<dl>
<dt>
<dd> (The following keys are valid if you have a keyboard with multimedia keys.)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>PAUSE</p>
<dd> Pause.</p>
<dt>STOP&nbsp;</p>
<dd> Stop playing and quit.</p>
<dt>PREVIOUS and NEXT</p>
<dd> Seek backward/:forward 1 minute.</dl>
</dl>
<dl>
<dt>
<dd> (The following keys are only valid if you compiled with TV or DVB input support and will take precedence over the keys defined above.)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>h and k</p>
<dd> Select previous/:next channel.</p>
<dt>n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Change norm.</p>
<dt>u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Change channel list.</dl>
</dl>
<dl>
<dt>
<dd> (The following keys are only valid if you compiled with dvdnav support: They are used to navigate the menus.)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>keypad 8</p>
<dd> Select button up.</p>
<dt>keypad 2</p>
<dd> Select button down.</p>
<dt>keypad 4</p>
<dd> Select button left.</p>
<dt>keypad 6</p>
<dd> Select button right.</p>
<dt>keypad 5</p>
<dd> Return to main menu.</p>
<dt>keypad 7</p>
<dd> Return to nearest menu (the order of preference is: chapter-&gt;title-&gt;root).</p>
<dt>keypad ENTER</p>
<dd> Confirm choice.</dl>
</dl>
<dl>
<dt>
<dd> (The following keys are used for controlling TV teletext. The data may come from either an analog TV source or an MPEG transport stream.)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Switch teletext on/:off.</p>
<dt>Q and W</p>
<dd> Go to next/:prev teletext page.</dl>
</dl>
<dl>
<dt><code>mouse control</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>button 3 and button 4</p>
<dd> Seek backward/:forward 1 minute.</p>
<dt>button 5 and button 6</p>
<dd> Decrease/:increase volume.</dl>
</dl>
<dt><code>joystick control</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>left and right</p>
<dd> Seek backward/:forward 10 seconds.</p>
<dt>up and down</p>
<dd> Seek forward/:backward 1 minute.</p>
<dt>button 1</p>
<dd> Pause.</p>
<dt>button 2</p>
<dd> Toggle OSD states: none / seek / seek + timer / seek + timer + total time.</p>
<dt>button 3 and button 4</p>
<dd> Decrease/:increase volume.</dl>
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
<p> You can put all of the options in configuration files which will be read every time MPlayer/MEncoder is run. The system-wide configuration file &#8216;mplayer.conf&#8217; is in your configuration directory (e.g. /etc/:mplayer or /usr/:local/:etc/:mplayer), the user specific one is &#8216;~/:.mplayer/:config&#8217;. The configuration file for MEncoder is &#8216;mencoder.conf&#8217; in your configuration directory (e.g. /etc/:mplayer or /usr/:local/:etc/:mplayer), the user specific one is &#8216;~/:.mplayer/:mencoder.conf&#8217;. User specific options override system-wide options (in case of <code>gmplayer</code>, gui.conf options override user specific options) and options given on the command line override all. The syntax of the configuration files is &#8216;option=&lt;value&gt;&#8217;, everything after a &#8216;#&#8217; is considered a comment. Options that work without values can be enabled by setting them to &#8216;yes&#8217; or &#8216;1&#8217; or &#8216;true&#8217; and disabled by setting them to &#8216;no&#8217; or &#8216;0&#8217; or &#8216;false&#8217;. Even suboptions can be specified in this way. </p>
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
<p> GUI&#8217;s own options are (MPlayer option names in parentheses): ao_alsa_device (<code>alsa:device=</code>) (ALSA only), ao_alsa_mixer (<code>mixer</code>) (ALSA only), ao_alsa_mixer_channel (<code>mixer-channel</code>) (ALSA only), ao_esd_device (<code>esd:</code>) (ESD only), ao_extra_stereo (<code>af extrastereo</code>) (default: 1.0), ao_extra_stereo_coefficient (<code>af extrastereo=</code>), ao_oss_device (<code>oss:</code>) (OSS only), ao_oss_mixer (<code>mixer</code>) (OSS only), ao_oss_mixer_channel (<code>mixer-channel</code>) (OSS only), ao_sdl_subdriver (<code>sdl:</code>) (SDL only), ao_surround (unused), ao_volnorm (<code>af volnorm</code>), autosync (enable/disable), autosync_size (<code>autosync</code>), cache (enable/disable), cache_size (<code>cache</code>), enable_audio_equ (<code>af equalizer</code>), equ_band_00 &#8230; equ_band_59, (<code>af equalizer=</code>), equ_channel_1 &#8230; equ_channel_6 (<code>af channels=</code>), gui_main_pos_x, gui_main_pos_y, gui_save_pos (yes/no), gui_tv_digital (yes/no), gui_video_out_pos_x, gui_video_out_pos_y, load_fullscreen (yes/no), playbar (enable/disable), show_videowin (yes/no), vf_lavc (<code>vf lavc</code>) (DXR3 only), vf_pp (<code>vf pp</code>), vo_dxr3_device (unused) (DXR3 only). </p>
<p> MPlayer options stored in gui.conf (GUI option names, MPlayer option names in parentheses) are: a_afm (<code>afm</code>), ao_driver (<code>ao</code>), ass_bottom_margin (<code>ass-bottom-margin</code>) (ASS only), ass_enabled (<code>ass</code>) (ASS only), ass_top_margin (<code>ass-top-margin</code>) (ASS only), ass_use_margins (<code>ass-use-margins</code>) (ASS only), cdrom_device (<code>cdrom-device</code>), dvd_device (<code>dvd-device</code>), font_autoscale (<code>subfont-autoscale</code>) (FreeType only), font_blur (<code>subfont-blur</code>) (FreeType only), font_encoding (<code>subfont-encoding</code>), font_factor (<code>ffactor</code>), font_name (<code>font</code>), font_osd_scale (<code>subfont-osd-scale</code>) (FreeType only), font_outline (<code>subfont-outline</code>) (FreeType only), font_text_scale (<code>subfont-text-scale</code>) (FreeType only), gui_skin (<code>skin</code>), idle (<code>idle</code>), osd_level (<code>osdlevel</code>), softvol (<code>softvol</code>), stopxscreensaver (<code>stop-xscreensaver</code>), sub_auto_load (<code>autosub</code>), sub_cp (<code>subcp</code>) (iconv only), sub_overlap (<code>overlapsub</code>), sub_pos (<code>subpos</code>), sub_unicode (<code>unicode</code>), sub_utf8 (<code>utf8</code>), v_flip (<code>flip</code>), v_framedrop (<code>framedrop</code>), v_idx (<code>idx</code>), v_ni (<code>ni</code>), v_vfm (<code>vfm</code>), vf_autoq (<code>autoq</code>), vo_direct_render (<code>panscan</code>), vo_doublebuffering (<code>dr</code>), vo_driver (<code>vo</code>), vo_panscan (<code>double</code>).</p>
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
<dt><code>-codecpath &lt;dir&gt;</code></p>
<dd> Specify a directory for binary codecs.</p>
<dt><code>-codecs-file &lt;filename&gt; (also see -afm, -ac, -vfm, -vc)</code></p>
<dd> Override the standard search path and use the specified file instead of the builtin codecs.conf.</p>
<dt><code>-include &lt;configuration file&gt; (also see -gui-include)</code></p>
<dd> Specify configuration file to be parsed after the default ones.</p>
<dt><code>-list-options</code></p>
<dd> Prints all available options.</p>
<dt><code>-msgcharset &lt;charset&gt;</code></p>
<dd> Convert console messages to the specified character set (default: autodetect). Text will be in the encoding specified with the &#8211;charset configure option. Set this to &quot;noconv&quot; to disable conversion (for e.g. iconv problems).<br />
 <i>NOTE:</i> The option takes effect after command line parsing has finished. The MPLAYER_CHARSET environment variable can help you get rid of the first lines of garbled output.</p>
<dt><code>-msgcolor</code></p>
<dd> Enable colorful console output on terminals that support ANSI color.</p>
<dt><code>-msglevel &lt;all=&lt;level&gt;:&lt;module&gt;=&lt;level&gt;:&#8230;&gt;</code></p>
<dd> Control verbosity directly for each module. The &#8216;all&#8217; module changes the verbosity of all the modules not explicitly specified on the command line. See &#8216;-msglevel help&#8217; for a list of all modules.<br />
 <i>NOTE:</i> Some messages are printed before the command line is parsed and are therefore not affected by -msglevel. To control these messages you have to use the MPLAYER_VERBOSE environment variable, see its description below for details.<br />
 Available levels:</p>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> complete silence</p>
<dt> 0</p>
<dd> fatal messages only</p>
<dt> 1</p>
<dd> error messages</p>
<dt> 2</p>
<dd> warning messages</p>
<dt> 3</p>
<dd> short hints</p>
<dt> 4</p>
<dd> informational messages</p>
<dt> 5</p>
<dd> status messages (default)</p>
<dt> 6</p>
<dd> verbose messages</p>
<dt> 7</p>
<dd> debug level 2</p>
<dt> 8</p>
<dd> debug level 3</p>
<dt> 9</p>
<dd> debug level 4</dl>
</dl>
<dt><code>-msgmodule</code></p>
<dd> Prepend module name in front of each console message.</p>
<dt><code>-noconfig &lt;options&gt;</code></p>
<dd> Do not parse selected configuration files.<br />
 <i>NOTE:</i> If -include or -use-filedir-conf options are specified at the command line, they will be honoured. </p>
<p> Available options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>all&nbsp;<wbr>&nbsp;</p>
<dd> all configuration files</p>
<dt>gui (GUI only)</p>
<dd> GUI configuration file</p>
<dt>system</p>
<dd> system configuration file</p>
<dt>user&nbsp;</p>
<dd> user configuration file</dl>
</dl>
<dt><code>-quiet&nbsp;</code></p>
<dd> Make console output less verbose; in particular, prevents the status line (i.e. A: 0.7 V: 0.6 A-V: 0.068 &#8230;) from being displayed. Particularly useful on slow terminals or broken ones which do not properly handle carriage return (i.e. ).</p>
<dt><code>-priority &lt;prio&gt; (Windows and OS/2 only)</code></p>
<dd> Set process priority for MPlayer according to the predefined priorities available under Windows and OS/2. Possible values of &lt;prio&gt;:</p>
<dl>
<dt>
<dd> idle|belownormal|normal|abovenormal|high|realtime</dl>
<dl>
<dt>
<dd> <i>WARNING:</i> Using realtime priority can cause system lockup.</dl>
<dt><code>-profile &lt;profile1,profile2,&#8230;&gt;</code></p>
<dd> Use the given profile(s), -profile help displays a list of the defined profiles.</p>
<dt><code>-really-quiet (also see -quiet)</code></p>
<dd> Display even less output and status messages than with -quiet. Also suppresses the GUI error message boxes.</p>
<dt><code>-show-profile &lt;profile&gt;</code></p>
<dd> Show the description and content of a profile.</p>
<dt><code>-use-filedir-conf</code></p>
<dd> Look for a file-specific configuration file in the same directory as the file that is being played.<br />
 <i>WARNING:</i> May be dangerous if playing from untrusted media.</p>
<dt><code>-v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Increment verbosity level, one level for each -v found on the command line.</dl>
<h2>PLAYER OPTIONS (MPLAYER ONLY)</h2>
<dl>
<dt><code>-autoq &lt;quality&gt; (use with -vf [s]pp)</code></p>
<dd> Dynamically changes the level of postprocessing depending on the available spare CPU time. The number you specify will be the maximum level used. Usually you can use some big number. You have to use -vf [s]pp without parameters in order for this to work.</p>
<dt><code>-autosync &lt;factor&gt;</code></p>
<dd> Gradually adjusts the A/V sync based on audio delay measurements. Specifying -autosync 0, the default, will cause frame timing to be based entirely on audio delay measurements. Specifying -autosync 1 will do the same, but will subtly change the A/V correction algorithm. An uneven video framerate in a movie which plays fine with -nosound can often be helped by setting this to an integer value greater than 1. The higher the value, the closer the timing will be to -nosound. Try -autosync 30 to smooth out problems with sound drivers which do not implement a perfect audio delay measurement. With this value, if large A/V sync offsets occur, they will only take about 1 or 2 seconds to settle out. This delay in reaction time to sudden A/V offsets should be the only side-effect of turning this option on, for all sound drivers.</p>
<dt><code>-benchmark</code></p>
<dd> Prints some statistics on CPU usage and dropped frames at the end of playback. Use in combination with -nosound and -vo null for benchmarking only the video codec.<br />
 <i>NOTE:</i> With this option MPlayer will also ignore frame duration when playing only video (you can think of that as infinite fps).</p>
<dt><code>-colorkey &lt;number&gt;</code></p>
<dd> Changes the colorkey to an RGB value of your choice. 0x000000 is black and 0xffffff is white. Only supported by the cvidix, fbdev, svga, vesa, winvidix, xmga, xvidix, xover, xv (see -vo xv:ck), xvmc (see -vo xv:ck) and directx video output drivers.</p>
<dt><code>-nocolorkey</code></p>
<dd> Disables colorkeying. Only supported by the cvidix, fbdev, svga, vesa, winvidix, xmga, xvidix, xover, xv (see -vo xv:ck), xvmc (see -vo xv:ck) and directx video output drivers.</p>
<dt><code>-correct-pts (EXPERIMENTAL)</code></p>
<dd> Switches MPlayer to an experimental mode where timestamps for video frames are calculated differently and video filters which add new frames or modify timestamps of existing ones are supported. The more accurate timestamps can be visible for example when playing subtitles timed to scene changes with the -ass option. Without -correct-pts the subtitle timing will typically be off by some frames. This option does not work correctly with some demuxers and codecs.</p>
<dt><code>-crash-debug (DEBUG CODE)</code></p>
<dd> Automatically attaches gdb upon crash or SIGTRAP. Support must be compiled in by configuring with &#8211;enable-crash-debug.</p>
<dt><code>-doubleclick-time</code></p>
<dd> Time in milliseconds to recognize two consecutive button presses as a double-click (default: 300). Set to 0 to let your windowing system decide what a double-click is (-vo directx only).<br />
 <i>NOTE:</i> You will get slightly different behaviour depending on whether you bind MOUSE_BTN0_DBL or MOUSE_BTN0-MOUSE_BTN0_DBL.</p>
<dt><code>-edlout &lt;filename&gt;</code></p>
<dd> Creates a new file and writes edit decision list (EDL) records to it. During playback, the user hits &#8216;i&#8217; to mark the start or end of a skip block. This provides a starting point from which the user can fine-tune EDL entries later. See <a rel="nofollow" href="http://www.mplayerhq.hu/:DOCS/:HTML/:en/:edl.html">http://www.mplayerhq.hu/:DOCS/:HTML/:en/:edl.html</a> for details.</p>
<dt><code>-edl-backward-delay &lt;number&gt;</code></p>
<dd> When using EDL during playback and jumping backwards it is possible to end up in the middle of an EDL record. In that case MPlayer will seek further backwards to the start position of the EDL record and then immediately skip the scene specified in the EDL record. To avoid this kind of behavior, MPlayer jumps to a fixed time interval before the start of the EDL record. This parameter allows you to specify that time interval in seconds (default: 2 seconds).</p>
<dt><code>-edl-start-pts</code></p>
<dd> Adjust positions in EDL records according to playing file&#8217;s start time. Some formats, especially MPEG TS usually start with non-zero PTS values and when producing EDL file with -edlout option, EDL records contain absolute values that are correct only for this particular file. If re-encoded into a different format, this EDL file no longer applies. Specifying -edl-start-pts will automatically adjust EDL positions according to start time: when producing EDL file, it will substract start time from every EDL record, when playing with EDL file, it will add file&#8217;s start time to every EDL position.</p>
<dt><code>-noedl-start-pts</code></p>
<dd> Disable adjusting EDL positions.</p>
<dt><code>-enqueue (GUI only)</code></p>
<dd> Enqueue files given on the command line in the playlist instead of playing them immediately.</p>
<dt><code>-fixed-vo</code></p>
<dd> Enforces a fixed video system for multiple files (one (un)initialization for all files). Therefore only one window will be opened for all files. Currently the following drivers are fixed-vo compliant: gl, gl_tiled, mga, svga, x11, xmga, xv, xvidix and dfbmga.</p>
<dt><code>-framedrop (also see -hardframedrop, experimental without -nocorrect-pts)</code></p>
<dd> Skip displaying some frames to maintain A/V sync on slow systems. Video filters are not applied to such frames. For B-frames even decoding is skipped completely.</p>
<dt><code>-(no)gui</code></p>
<dd> Enable or disable the GUI interface (default depends on binary name). Only works as the first argument on the command line. Does not work as a config-file option.</p>
<dt><code>-gui-include &lt;GUI configuration file&gt; (also see -include) (GUI only)</code></p>
<dd> Specify a GUI configuration file to be parsed after the default gui.conf.</p>
<dt><code>-h, -help, &#8211;help</code></p>
<dd> Show short summary of options.</p>
<dt><code>-hardframedrop (experimental without -nocorrect-pts)</code></p>
<dd> More intense frame dropping (breaks decoding). Leads to image distortion! Note that especially the libmpeg2 decoder may crash with this, so consider using &quot;-vc ffmpeg12,&quot;.</p>
<dt><code>-heartbeat-cmd</code></p>
<dd> Command that is executed every 30 seconds during playback via system() &#8211; i.e. using the shell. </p>
<p> <i>NOTE:</i> MPlayer uses this command without any checking, it is your responsibility to ensure it does not cause security problems (e.g. make sure to use full paths if &quot;.&quot; is in your path like on Windows). It also only works when playing video (i.e. not with -novideo but works with -vo null). </p>
<p> This can be &quot;misused&quot; to disable screensavers that do not support the proper X API (also see -stop-xscreensaver). If you think this is too complicated, ask the author of the screensaver program to support the proper X APIs. </p>
<p> <i>EXAMPLE for xscreensaver:</i> mplayer -heartbeat-cmd &quot;xscreensaver-command -deactivate&quot; file </p>
<p> <i>EXAMPLE for GNOME screensaver:</i> mplayer -heartbeat-cmd &quot;gnome-screensaver-command -p&quot; file</p>
<dt><code>-heartbeat-interval</code></p>
<dd> Specify how often the -heartbeat-cmd should be executed, in seconds between executions (default: 30.0).</p>
<dt><code>-identify</code></p>
<dd> Shorthand for -msglevel identify=4. Show file parameters in an easily parseable format. Also prints more detailed information about subtitle and audio track languages and IDs. In some cases you can get more information by using -msglevel identify=6. For example, for a DVD or Blu-ray it will list the chapters and time length of each title, as well as a disk ID. Combine this with -frames 0 to suppress all video output. The wrapper script TOOLS/:midentify.sh suppresses the other MPlayer output and (hopefully) shellescapes the filenames.</p>
<dt><code>-idle (also see -slave)</code></p>
<dd> Makes MPlayer wait idly instead of quitting when there is no file to play. Mostly useful in slave mode where MPlayer can be controlled through input commands.<br />
 For <code>gmplayer</code> -idle is the default, -noidle will quit the GUI after all files have been played.</p>
<dt><code>-input &lt;commands&gt;</code></p>
<dd> This option can be used to configure certain parts of the input system. Paths are relative to ~/.mplayer/.<br />
 <i>NOTE:</i> Autorepeat is currently only supported by joysticks. </p>
<p> Available commands are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>conf=&lt;filename&gt;</p>
<dd> Specify input configuration file other than the default ~/:.mplayer/:input.conf. ~/:.mplayer/:&lt;filename&gt; is assumed if no full path is given.</p>
<dt>ar-dev=&lt;device&gt;</p>
<dd> Device to be used for Apple IR Remote (default is autodetected, Linux only).</p>
<dt>ar-delay</p>
<dd> Delay in milliseconds before we start to autorepeat a key (0 to disable).</p>
<dt>ar-rate</p>
<dd> Number of key presses to generate per second on autorepeat.</p>
<dt>(no)default-bindings</p>
<dd> Use the key bindings that MPlayer ships with by default.</p>
<dt>keylist</p>
<dd> Prints all keys that can be bound to commands.</p>
<dt>cmdlist</p>
<dd> Prints all commands that can be bound to keys.</p>
<dt>js-dev</p>
<dd> Specifies the joystick device to use (default: /dev/:input/:js0).</p>
<dt>file=&lt;filename&gt;</p>
<dd> Read commands from the given file. Mostly useful with a FIFO.<br />
 <i>NOTE:</i> When the given file is a FIFO MPlayer opens both ends so you can do several &#8216;echo &quot;seek 10&quot; &gt; mp_pipe&#8217; and the pipe will stay valid.</dl>
</dl>
<dt><code>-key-fifo-size &lt;2-65000&gt;</code></p>
<dd> Specify the size of the FIFO that buffers key events (default: 7). A FIFO of size n can buffer (n-1) events. If it is too small some events may be lost. If it is too big, MPlayer may seem to hang while it processes the buffered events. To get the same behavior as before this option was introduced, set it to 2 for Linux or 1024 for Windows. For small value you should disable double-clicks by setting -doubleclick-time to 0 so they do not compete with regular events for buffer space.</p>
<dt><code>-lircconf &lt;filename&gt; (LIRC only)</code></p>
<dd> Specifies a configuration file for LIRC (default: ~/.lircrc).</p>
<dt><code>-list-properties</code></p>
<dd> Print a list of the available properties.</p>
<dt><code>-loop &lt;number&gt;</code></p>
<dd> Loops movie playback &lt;number&gt; times. 0 means forever.</p>
<dt><code>-menu (OSD menu only)</code></p>
<dd> Turn on OSD menu support.</p>
<dt><code>-menu-cfg &lt;filename&gt; (OSD menu only)</code></p>
<dd> Use an alternative menu.conf.</p>
<dt><code>-menu-chroot &lt;path&gt; (OSD menu only)</code></p>
<dd> Chroot the file selection menu to a specific location. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-menu-chroot /home</p>
<dd> Will restrict the file selection menu to /:home and downward (i.e. no access to / will be possible, but /home/user_name will).</dl>
</dl>
<dt><code>-menu-keepdir (OSD menu only)</code></p>
<dd> File browser starts from the last known location instead of current directory.</p>
<dt><code>-menu-root &lt;value&gt; (OSD menu only)</code></p>
<dd> Specify the main menu.</p>
<dt><code>-menu-startup (OSD menu only)</code></p>
<dd> Display the main menu at MPlayer startup.</p>
<dt><code>-mouse-movements</code></p>
<dd> Permit MPlayer to receive pointer events reported by the video output driver. Necessary to select the buttons in DVD menus. Supported for X11-based VOs (x11, xv, xvmc, etc) and the gl, gl_tiled, direct3d and corevideo VOs.</p>
<dt><code>-noar</code></p>
<dd> Turns off AppleIR remote support.</p>
<dt><code>-noconsolecontrols</code></p>
<dd> Prevent MPlayer from reading key events from standard input. Useful when reading data from standard input. This is automatically enabled when &#8211; is found on the command line. There are situations where you have to set it manually, e.g. if you open /dev/:stdin (or the equivalent on your system), use stdin in a playlist or intend to read from stdin later on via the loadfile or loadlist slave commands.</p>
<dt><code>-nojoystick</code></p>
<dd> Turns off joystick support.</p>
<dt><code>-nolirc</code></p>
<dd> Turns off LIRC support.</p>
<dt><code>-nomouseinput</code></p>
<dd> Disable mouse button press/:release input (mozplayerxp&#8217;s context menu relies on this option).</p>
<dt><code>-rtc (RTC only)</code></p>
<dd> Turns on usage of the Linux RTC (realtime clock &#8211; /dev/:rtc) as timing mechanism. This wakes up the process every 1/1024 seconds to check the current time. Useless with modern Linux kernels configured for desktop use as they already wake up the process with similar accuracy when using normal timed sleep.</p>
<dt><code>-pausing &lt;0-3&gt; (MPlayer only)</code></p>
<dd> Specifies the default pausing behaviour of commands, i.e. whether MPlayer will continue playback or stay paused after the command has finished. See DOCS/tech/slave.txt for further details.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> resume</p>
<dt>1</p>
<dd> pause (pausing)</p>
<dt>2</p>
<dd> keep the paused / playing status (pausing_keep)</p>
<dt>3</p>
<dd> toggle the paused / playing status (pausing_toggle)</p>
<dt>4</p>
<dd> pause without frame step (experimental) (pausing_keep_force)</dl>
</dl>
<dt><code>-playing-msg &lt;string&gt;</code></p>
<dd> Print out a string before starting playback. The following expansions are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>${NAME}</p>
<dd> Expand to the value of the property NAME.</p>
<dt>?(NAME:TEXT)</p>
<dd> Expand TEXT only if the property NAME is available.</p>
<dt>?(!NAME:TEXT)</p>
<dd> Expand TEXT only if the property NAME is not available.</dl>
</dl>
<dt><code>-playlist &lt;filename&gt;</code></p>
<dd> Play files according to a playlist file (ASX, Winamp, SMIL, or one-file-per-line format).<br />
 <i>WARNING:</i> The way MPlayer parses and uses playlist files is not safe against maliciously constructed files. Such files may trigger harmful actions. This has been the case for all MPlayer versions, but unfortunately this fact was not well documented earlier, and some people have even misguidedly recommended use of -playlist with untrusted sources. Do NOT use -playlist with random internet sources or files you don&#8217;t trust!<br />
 <i>NOTE:</i> This option is considered an entry so options found after it will apply only to the elements of this playlist.<br />
 FIXME: This needs to be clarified and documented thoroughly.</p>
<dt><code>-allow-dangerous-playlist-parsing</code></p>
<dd> This enables parsing any file as a playlist if e.g. a server advertises a file as playlist. Only enable if you know all servers involved are trustworthy. MPlayer&#8217;s playlist code is not designed to handle malicious playlist files.</p>
<dt><code>-rtc-device &lt;device&gt;</code></p>
<dd> Use the specified device for RTC timing.</p>
<dt><code>-shuffle</code></p>
<dd> Play files in random order.</p>
<dt><code>-skin &lt;name&gt; (GUI only)</code></p>
<dd> Loads a skin from the directory given as parameter below the default skin directories, ~/.mplayer/:skins/ and /usr/:local/:share/:mplayer/:skins/:. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-skin fittyfene</p>
<dd> Tries ~/.mplayer/:skins/:fittyfene and afterwards /usr/:local/:share/:mplayer/:skins/:fittyfene.</dl>
</dl>
<dt><code>-slave (also see -input)</code></p>
<dd> Switches on slave mode, in which MPlayer works as a backend for other programs. Instead of intercepting keyboard events, MPlayer will read commands separated by a newline (
) from stdin.<br />
 <i>NOTE:</i> See -input cmdlist for a list of slave commands and DOCS/tech/slave.txt for their description. Also, this is not intended to disable other inputs, e.g. via the video window, use some other method like -input nodefault-bindings:conf=/dev/null for that.</p>
<dt><code>-softsleep</code></p>
<dd> Time frames by repeatedly checking the current time instead of asking the kernel to wake up MPlayer at the correct time. Useful if your kernel timing is imprecise and you cannot use the RTC either. Comes at the price of higher CPU consumption.</p>
<dt><code>-sstep &lt;sec&gt;</code></p>
<dd> Skip &lt;sec&gt; seconds after every frame. The normal framerate of the movie is kept, so playback is accelerated. Since MPlayer can only seek to the next keyframe this may be inexact.</p>
<dt><code>-udp-ip &lt;ip&gt;</code></p>
<dd> Sets the destination address for datagrams sent by the -udp-master. Setting it to a broadcast address allows multiple slaves having the same broadcast address to sync to the master (default: 127.0.0.1).</p>
<dt><code>-udp-master</code></p>
<dd> Send a datagram to -udp-ip on -udp-port just before playing each frame. The datagram indicates the master&#8217;s position in the file.</p>
<dt><code>-udp-port &lt;port&gt;</code></p>
<dd> Sets the destination port for datagrams sent by the -udp-master, and the port a -udp-slave listens on (default: 23867).</p>
<dt><code>-udp-seek-threshold &lt;sec&gt;</code></p>
<dd> When the master seeks, the slave has to decide whether to seek as well, or to catch up by decoding frames without pausing between frames. If the master is more than &lt;sec&gt; seconds away from the slave, the slave seeks. Otherwise, it &quot;runs&quot; to catch up or waits for the master. This should almost always be left at its default setting of 1 second.</p>
<dt><code>-udp-slave</code></p>
<dd> Listen on -udp-port and match the master&#8217;s position.</dl>
<h2>DEMUXER/STREAM OPTIONS</h2>
<dl>
<dt><code>-a52drc &lt;level&gt;</code></p>
<dd> Select the Dynamic Range Compression level for AC-3 audio streams. &lt;level&gt; is a float value ranging from 0 to 1, where 0 means no compression and 1 (which is the default) means full compression (make loud passages more silent and vice versa). Values up to 2 are also accepted, but are purely experimental. This option only shows an effect if the AC-3 stream contains the required range compression information.</p>
<dt><code>-aid &lt;ID&gt; (also see -alang)</code></p>
<dd> Select audio channel (MPEG: 0-31, AVI/:OGM: 1-99, ASF/:RM: 0-127, VOB(AC-3): 128-159, VOB(LPCM): 160-191, MPEG-TS 17-8190). MPlayer prints the available audio IDs when run in verbose (-v) mode. When playing an MPEG-TS stream, MPlayer/:MEncoder will use the first program (if present) with the chosen audio stream.</p>
<dt><code>-ausid &lt;ID&gt; (also see -alang)</code></p>
<dd> Select audio substream channel. Currently the valid range is 0x55..0x75 and applies only to MPEG-TS when handled by the native demuxer (not by libavformat). The format type may not be correctly identified because of how this information (or lack thereof) is embedded in the stream, but it will demux correctly the audio streams when multiple substreams are present. MPlayer prints the available substream IDs when run with -identify.</p>
<dt><code>-alang &lt;language code[,language code,&#8230;]&gt; (also see -aid)</code></p>
<dd> Specify a priority list of audio languages to use. Different container formats employ different language codes. DVDs use ISO 639-1 two letter language codes, Matroska, MPEG-TS and NUT use ISO 639-2 three letter language codes while OGM uses a free-form identifier. MPlayer prints the available languages when run in verbose (-v) mode. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer <a href="dvd://1">dvd://1</a> -alang hu,en</p>
<dd> Chooses the Hungarian language track on a DVD and falls back on English if Hungarian is not available.</p>
<dt>mplayer -alang jpn example.mkv</p>
<dd> Plays a Matroska file in Japanese.</dl>
</dl>
<dt><code>-audio-demuxer &lt;[+]name&gt; (-audiofile only)</code></p>
<dd> Force audio demuxer type for -audiofile. Use a &#8216;+&#8217; before the name to force it, this will skip some checks! Give the demuxer name as printed by -audio-demuxer help. For backward compatibility it also accepts the demuxer ID as defined in libmpdemux/:demuxer.h. -audio-demuxer audio or -audio-demuxer 17 forces MP3.</p>
<dt><code>-audiofile &lt;filename&gt;</code></p>
<dd> Play audio from an external file (WAV, MP3 or Ogg Vorbis) while viewing a movie.</p>
<dt><code>-audiofile-cache &lt;kBytes&gt;</code></p>
<dd> Enables caching for the stream used by -audiofile, using the specified amount of memory.</p>
<dt><code>-reuse-socket (udp:// only)</code></p>
<dd> Allows a socket to be reused by other processes as soon as it is closed.</p>
<dt><code>-bandwidth &lt;Bytes&gt; (network only)</code></p>
<dd> Specify the maximum bandwidth for network streaming (for servers that are able to send content in different bitrates). Useful if you want to watch live streamed media behind a slow connection. With Real RTSP streaming, it is also used to set the maximum delivery bandwidth allowing faster cache filling and stream dumping.</p>
<dt><code>-bluray-angle &lt;angle ID&gt; (Blu-ray only)</code></p>
<dd> Some Blu-ray discs contain scenes that can be viewed from multiple angles. Here you can tell MPlayer which angles to use (default: 1).</p>
<dt><code>-bluray-device &lt;path to disc&gt; (Blu-ray only)</code></p>
<dd> Specify the Blu-ray disc location. Must be a directory with Blu-ray structure.</p>
<dt><code>-cache &lt;kBytes&gt;</code></p>
<dd> This option specifies how much memory (in kBytes) to use when precaching a file or URL. Especially useful on slow media.</p>
<dt><code>-nocache</code></p>
<dd> Turns off caching.</p>
<dt><code>-cache-min &lt;percentage&gt;</code></p>
<dd> Playback will start when the cache has been filled up to &lt;percentage&gt; of the total.</p>
<dt><code>-cache-seek-min &lt;percentage&gt;</code></p>
<dd> If a seek is to be made to a position within &lt;percentage&gt; of the cache size from the current position, MPlayer will wait for the cache to be filled to this position rather than performing a stream seek (default: 50).</p>
<dt><code>-capture (MPlayer only)</code></p>
<dd> Allows capturing the primary stream (not additional audio tracks or other kind of streams) into the file specified by -dumpfile or by default. If this option is given, capturing can be started and stopped by pressing the key bound to this function (see section INTERACTIVE CONTROL). Same as for -dumpstream, this will likely not produce usable results for anything else than MPEG streams. Note that, due to cache latencies, captured data may begin and end somewhat delayed compared to what you see displayed.</p>
<dt><code>-cdda &lt;option1:option2&gt; (CDDA only)</code></p>
<dd> This option can be used to tune the CD Audio reading feature of MPlayer. </p>
<p> Available options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>speed=&lt;value&gt;</p>
<dd> Set CD spin speed.</p>
<dt>paranoia=&lt;0-2&gt;</p>
<dd> Set paranoia level. Values other than 0 seem to break playback of anything but the first track.</p>
<dl>
<dt>
<dd> 0: disable checking (default)<br />
 1: overlap checking only<br />
 2: full data correction and verification</dl>
<dt>generic-dev=&lt;value&gt;</p>
<dd> Use specified generic SCSI device.</p>
<dt>sector-size=&lt;value&gt;</p>
<dd> Set atomic read size.</p>
<dt>overlap=&lt;value&gt;</p>
<dd> Force minimum overlap search during verification to &lt;value&gt; sectors.</p>
<dt>toc-bias</p>
<dd> Assume that the beginning offset of track 1 as reported in the TOC will be addressed as LBA 0. Some Toshiba drives need this for getting track boundaries correct.</p>
<dt>toc-offset=&lt;value&gt;</p>
<dd> Add &lt;value&gt; sectors to the values reported when addressing tracks. May be negative.</p>
<dt>(no)skip</p>
<dd> (Never) accept imperfect data reconstruction.</dl>
</dl>
<dt><code>-cdrom-device &lt;path to device&gt;</code></p>
<dd> Specify the CD-ROM device (default: /dev/:cdrom).</p>
<dt><code>-channels &lt;number&gt; (also see -af channels)</code></p>
<dd> Request the number of playback channels (default: 2). MPlayer asks the decoder to decode the audio into as many channels as specified. Then it is up to the decoder to fulfill the requirement. This is usually only important when playing videos with AC-3 audio (like DVDs). In that case liba52 does the decoding by default and correctly downmixes the audio into the requested number of channels. To directly control the number of output channels independently of how many channels are decoded, use the channels filter.<br />
 <i>NOTE:</i> This option is honored by codecs (AC-3 only), filters (surround) and audio output drivers (OSS at least). </p>
<p> Available options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>2</p>
<dd> stereo</p>
<dt>4</p>
<dd> surround</p>
<dt>6</p>
<dd> full 5.1</p>
<dt>8</p>
<dd> full 7.1</dl>
</dl>
<dt><code>-chapter &lt;chapter ID&gt;[-&lt;endchapter ID&gt;]</code></p>
<dd> Specify which chapter to start playing at. Optionally specify which chapter to end playing at (default: 1).</p>
<dt><code>-cookies (network only)</code></p>
<dd> Send cookies when making HTTP requests.</p>
<dt><code>-cookies-file &lt;filename&gt; (network only)</code></p>
<dd> Read HTTP cookies from &lt;filename&gt; (default: ~/.mozilla/ and ~/.netscape/) and skip reading from default locations. The file is assumed to be in Netscape format.</p>
<dt><code>-delay &lt;sec&gt;</code></p>
<dd> audio delay in seconds (positive or negative float value)<br />
 Negative values delay the audio, and positive values delay the video. Note that this is the exact opposite of the -audio-delay MEncoder option.<br />
 <i>NOTE:</i> When used with MEncoder, this is not guaranteed to work correctly with -ovc copy; use -audio-delay instead.</p>
<dt><code>-ignore-start</code></p>
<dd> Ignore the specified starting time for streams in AVI files. In MPlayer, this nullifies stream delays in files encoded with the -audio-delay option. During encoding, this option prevents MEncoder from transferring original stream start times to the new file; the -audio-delay option is not affected. Note that MEncoder sometimes adjusts stream starting times automatically to compensate for anticipated decoding delays, so do not use this option for encoding without testing it first.</p>
<dt><code>-demuxer &lt;[+]name&gt;</code></p>
<dd> Force demuxer type. Use a &#8216;+&#8217; before the name to force it, this will skip some checks! Give the demuxer name as printed by -demuxer help. For backward compatibility it also accepts the demuxer ID as defined in libmpdemux/:demuxer.h.</p>
<dt><code>-dumpaudio (MPlayer only)</code></p>
<dd> Dumps raw compressed audio stream to ./stream.dump (useful with MPEG/:AC-3, in most other cases the resulting file will not be playable). If you give more than one of -dumpaudio, -dumpvideo, -dumpstream on the command line only the last one will work.</p>
<dt><code>-dumpfile &lt;filename&gt; (MPlayer only)</code></p>
<dd> Specify which file MPlayer should dump to. Should be used together with -dumpaudio / -dumpvideo / -dumpstream / -capture.</p>
<dt><code>-dumpstream (MPlayer only)</code></p>
<dd> Dumps the raw stream to ./stream.dump. Useful when ripping from DVD or network. If you give more than one of -dumpaudio, -dumpvideo, -dumpstream on the command line only the last one will work.</p>
<dt><code>-dumpvideo (MPlayer only)</code></p>
<dd> Dump raw compressed video stream to ./stream.dump (not very usable). If you give more than one of -dumpaudio, -dumpvideo, -dumpstream on the command line only the last one will work.</p>
<dt><code>-dvbin &lt;options&gt; (DVB only)</code></p>
<dd> Pass the following parameters to the DVB input module, in order to override the default ones: </p>
<dl>
<dt>
<dd>
<dl>
<dt>card=&lt;1-4&gt;</p>
<dd> Specifies using card number 1-4 (default: 1).</p>
<dt>file=&lt;filename&gt;</p>
<dd> Instructs MPlayer to read the channels list from &lt;filename&gt;. Default is ~/.mplayer/:channels.conf.{sat,ter,cbl,atsc} (based on your card type) or ~/.mplayer/:channels.conf as a last resort.</p>
<dt>timeout=&lt;1-240&gt;</p>
<dd> Maximum number of seconds to wait when trying to tune a frequency before giving up (default: 30).</dl>
</dl>
<dt><code>-dvd-device &lt;path to device&gt; (DVD only)</code></p>
<dd> Specify the DVD device or .iso filename (default: /dev/:dvd). You can also specify a directory that contains files previously copied directly from a DVD (with e.g. vobcopy).</p>
<dt><code>-dvd-speed &lt;factor or speed in KB/s&gt; (DVD only)</code></p>
<dd> Try to limit DVD speed (default: 0, no change). DVD base speed is about 1350KB/s, so a 8x drive can read at speeds up to 10800KB/s. Slower speeds make the drive more quiet, for watching DVDs 2700KB/s should be quiet and fast enough. MPlayer resets the speed to the drive default value on close. Values less than 100 mean multiples of 1350KB/s, i.e. -dvd-speed 8 selects 10800KB/s.<br />
 <i>NOTE:</i> You need write access to the DVD device to change the speed.</p>
<dt><code>-dvdangle &lt;angle ID&gt; (DVD only)</code></p>
<dd> Some DVD discs contain scenes that can be viewed from multiple angles. Here you can tell MPlayer which angles to use (default: 1).</p>
<dt><code>-edl &lt;filename&gt;</code></p>
<dd> Enables edit decision list (EDL) actions during playback. Video will be skipped over and audio will be muted and unmuted according to the entries in the given file. See <a rel="nofollow" href="http://www.mplayerhq.hu/:DOCS/:HTML/:en/:edl.html">http://www.mplayerhq.hu/:DOCS/:HTML/:en/:edl.html</a> for details on how to use this.</p>
<dt><code>-endpos &lt;[[hh:]mm:]ss[.ms]|size[b|kb|mb]&gt; (also see -ss and -sb)</code></p>
<dd> Stop at given time or byte position.<br />
 <i>NOTE:</i> Byte position may not be accurate, as it can only stop at a frame boundary. When used in conjunction with -ss option, -endpos time will shift forward by seconds specified with -ss if not a byte position. In addition it may not work well or not at all when used with any of the -dump options. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-endpos 56</p>
<dd> Stop at 56 seconds.</p>
<dt>-endpos 01:10:00</p>
<dd> Stop at 1 hour 10 minutes.</p>
<dt>-ss 10 -endpos 56</p>
<dd> Stop at 1 minute 6 seconds.</p>
<dt>mplayer -endpos 100mb</p>
<dd> Stop playback after reading 100MB of the input file.</p>
<dt>mencoder -endpos 100mb</p>
<dd> Encode only 100 MB.</dl>
</dl>
<dt><code>-forceidx</code></p>
<dd> Force index rebuilding. Useful for files with broken index (A/V desync, etc). This will enable seeking in files where seeking was not possible. You can fix the index permanently with MEncoder (see the documentation).<br />
 <i>NOTE:</i> This option only works if the underlying media supports seeking (i.e. not with stdin, pipe, etc).</p>
<dt><code>-fps &lt;float value&gt;</code></p>
<dd> Override video framerate. Useful if the original value is wrong or missing.</p>
<dt><code>-frames &lt;number&gt;</code></p>
<dd> Play/:convert only first &lt;number&gt; frames, then quit.</p>
<dt><code>-hr-mp3-seek (MP3 only)</code></p>
<dd> Hi-res MP3 seeking. Enabled when playing from an external MP3 file, as we need to seek to the very exact position to keep A/V sync. Can be slow especially when seeking backwards since it has to rewind to the beginning to find an exact frame position.</p>
<dt><code>-http-header-fields &lt;field1,field2&gt;</code></p>
<dd> Set custom HTTP fields when accessing HTTP stream. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> mplayer -http-header-fields &#8216;Field1: value1&#8242;,&#8217;Field2: value2&#8217; <a rel="nofollow" href="http://localhost:1234">http://localhost:1234</a><br />
 Will generate HTTP request:</p>
<dl>
<dt>
<dd>
 GET / HTTP/1.0<br />
 Host: localhost:1234<br />
 User-Agent: MPlayer<br />
 Icy-MetaData: 1<br />
 Field1: value1<br />
 Field2: value2<br />
 Connection: close</dl>
</dl>
</dl>
<dt><code>-idx (also see -forceidx)</code></p>
<dd> Rebuilds index of files if no index was found, allowing seeking. Useful with broken/:incomplete downloads, or badly created files.<br />
 <i>NOTE:</i> This option only works if the underlying media supports seeking (i.e. not with stdin, pipe, etc).</p>
<dt><code>-noidx</code></p>
<dd> Skip rebuilding index file. MEncoder skips writing the index with this option.</p>
<dt><code>-ipv4-only-proxy (network only)</code></p>
<dd> Skip the proxy for IPv6 addresses. It will still be used for IPv4 connections.</p>
<dt><code>-loadidx &lt;index file&gt;</code></p>
<dd> The file from which to read the video index data saved by -saveidx. This index will be used for seeking, overriding any index data contained in the AVI itself. MPlayer will not prevent you from loading an index file generated from a different AVI, but this is sure to cause unfavorable results.<br />
 <i>NOTE:</i> This option is obsolete now that MPlayer has OpenDML support.</p>
<dt><code>-mc &lt;seconds/frame&gt;</code></p>
<dd> maximum A-V sync correction per frame (in seconds)<br />
 -mc 0 should always be combined with -noskip for mencoder, otherwise it will almost certainly cause A-V desync.</p>
<dt><code>-mf &lt;option1:option2:&#8230;&gt;</code></p>
<dd> Used when decoding from multiple PNG or JPEG files. </p>
<p> Available options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>w=&lt;value&gt;</p>
<dd> input file width (default: autodetect)</p>
<dt>h=&lt;value&gt;</p>
<dd> input file height (default: autodetect)</p>
<dt>fps=&lt;value&gt;</p>
<dd> output fps (default: 25)</p>
<dt>type=&lt;value&gt;</p>
<dd> input file type (available: jpeg, png, tga, sgi)</dl>
</dl>
<dt><code>-ni</code></p>
<dd> Force treating files as non-interleaved. In particular forces usage of non-interleaved AVI parser (fixes playback of some bad AVI files). Can also help playing files that otherwise play audio and video alternating instead of at the same time.</p>
<dt><code>-nobps (AVI only)</code></p>
<dd> Do not use average byte/:second value for A-V sync. Helps with some AVI files with broken header.</p>
<dt><code>-noextbased</code></p>
<dd> Disables extension-based demuxer selection. By default, when the file type (demuxer) cannot be detected reliably (the file has no header or it is not reliable enough), the filename extension is used to select the demuxer. Always falls back on content-based demuxer selection.</p>
<dt><code>-passwd &lt;password&gt; (also see -user) (network only)</code></p>
<dd> Specify password for HTTP authentication.</p>
<dt><code>-prefer-ipv4 (network only)</code></p>
<dd> Use IPv4 on network connections. Falls back on IPv6 automatically.</p>
<dt><code>-prefer-ipv6 (IPv6 network only)</code></p>
<dd> Use IPv6 on network connections. Falls back on IPv4 automatically.</p>
<dt><code>-psprobe &lt;byte position&gt;</code></p>
<dd> When playing an MPEG-PS or MPEG-PES streams, this option lets you specify how many bytes in the stream you want MPlayer to scan in order to identify the video codec used. This option is needed to play EVO or VDR files containing H.264 streams.</p>
<dt><code>-pvr &lt;option1:option2:&#8230;&gt; (PVR only)</code></p>
<dd> This option tunes various encoding properties of the PVR capture module. It has to be used with any hardware MPEG encoder based card supported by the V4L2 driver. The Hauppauge WinTV PVR-150/250/350/500 and all IVTV based cards are known as PVR capture cards. Be aware that only Linux 2.6.18 kernel and above is able to handle MPEG stream through V4L2 layer. For hardware capture of an MPEG stream and watching it with MPlayer/MEncoder, use &#8216;<a href="pvr://'">pvr://&#8217;</a> as a movie URL. </p>
<p> Available options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>aspect=&lt;0-3&gt;</p>
<dd> Specify input aspect ratio:</p>
<dl>
<dt>
<dd> 0: 1:1<br />
 1: 4:3 (default)<br />
 2: 16:9<br />
 3: 2.21:1</dl>
<dt>arate=&lt;32000-48000&gt;</p>
<dd> Specify encoding audio rate (default: 48000 Hz, available: 32000, 44100 and 48000 Hz).</p>
<dt>alayer=&lt;1-3&gt;</p>
<dd> Specify MPEG audio layer encoding (default: 2).</p>
<dt>abitrate=&lt;32-448&gt;</p>
<dd> Specify audio encoding bitrate in kbps (default: 384).</p>
<dt>amode=&lt;value&gt;</p>
<dd> Specify audio encoding mode. Available preset values are &#8216;stereo&#8217;, &#8216;joint_stereo&#8217;, &#8216;dual&#8217; and &#8216;mono&#8217; (default: stereo).</p>
<dt>vbitrate=&lt;value&gt;</p>
<dd> Specify average video bitrate encoding in Mbps (default: 6).</p>
<dt>vmode=&lt;value&gt;</p>
<dd> Specify video encoding mode:</p>
<dl>
<dt>
<dd> vbr: Variable BitRate (default)<br />
 cbr: Constant BitRate</dl>
<dt>vpeak=&lt;value&gt;</p>
<dd> Specify peak video bitrate encoding in Mbps (only useful for VBR encoding, default: 9.6).</p>
<dt>fmt=&lt;value&gt;</p>
<dd> Choose an MPEG format for encoding:</p>
<dl>
<dt>
<dd> ps: MPEG-2 Program Stream (default)<br />
 ts: MPEG-2 Transport Stream<br />
 mpeg1: MPEG-1 System Stream<br />
 vcd: Video CD compatible stream<br />
 svcd: Super Video CD compatible stream<br />
 dvd: DVD compatible stream</dl>
</dl>
</dl>
<dt><code>-radio &lt;option1:option2:&#8230;&gt; (radio only)</code></p>
<dd> These options set various parameters of the radio capture module. For listening to radio with MPlayer use &#8216;radio://&lt;frequency&gt;&#8217; (if channels option is not given) or &#8216;radio://&lt;channel_number&gt;&#8217; (if channels option is given) as a movie URL. You can see allowed frequency range by running MPlayer with &#8216;-v&#8217;. To start the grabbing subsystem, use &#8216;radio://&lt;frequency or channel&gt;/capture&#8217;. If the capture keyword is not given you can listen to radio using the line-in cable only. Using capture to listen is not recommended due to synchronization problems, which makes this process uncomfortable. </p>
<p> Available options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>device=&lt;value&gt;</p>
<dd> Radio device to use (default: /dev/radio0 for Linux and /dev/tuner0 for *BSD).</p>
<dt>driver=&lt;value&gt;</p>
<dd> Radio driver to use (default: v4l2 if available, otherwise v4l). Currently, v4l and v4l2 drivers are supported.</p>
<dt>volume=&lt;0..100&gt;</p>
<dd> sound volume for radio device (default 100)</p>
<dt>freq_min=&lt;value&gt; (*BSD BT848 only)</p>
<dd> minimum allowed frequency (default: 87.50)</p>
<dt>freq_max=&lt;value&gt; (*BSD BT848 only)</p>
<dd> maximum allowed frequency (default: 108.00)</p>
<dt>channels=&lt;frequency&gt;-&lt;name&gt;,&lt;frequency&gt;-&lt;name&gt;,&#8230;</p>
<dd> Set channel list. Use _ for spaces in names (or play with quoting ;-). The channel names will then be written using OSD and the slave commands radio_step_channel and radio_set_channel will be usable for a remote control (see LIRC). If given, number in movie URL will be treated as channel position in channel list.<br />
 <i>EXAMPLE:</i> <a href="radio://1,">radio://1,</a> <a href="radio://104.4,">radio://104.4,</a> radio_set_channel 1</p>
<dt>adevice=&lt;value&gt; (radio capture only)</p>
<dd> Name of device to capture sound from. Without such a name capture will be disabled, even if the capture keyword appears in the URL. For ALSA devices use it in the form hw=&lt;card&gt;.&lt;device&gt;. If the device name contains a &#8216;=&#8217;, the module will use ALSA to capture, otherwise OSS.</p>
<dt>arate=&lt;value&gt; (radio capture only)</p>
<dd> Rate in samples per second (default: 44100).<br />
 <i>NOTE:</i> When using audio capture set also -rawaudio rate=&lt;value&gt; option with the same value as arate. If you have problems with sound speed (runs too quickly), try to play with different rate values (e.g. 48000,44100,32000,&#8230;).</p>
<dt>achannels=&lt;value&gt; (radio capture only)</p>
<dd> Number of audio channels to capture.</dl>
</dl>
<dt><code>-rawaudio &lt;option1:option2:&#8230;&gt;</code></p>
<dd> This option lets you play raw audio files. You have to use -demuxer rawaudio as well. It may also be used to play audio CDs which are not 44kHz 16-bit stereo. For playing raw AC-3 streams use -rawaudio format=0x2000 -demuxer rawaudio. </p>
<p> Available options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>channels=&lt;value&gt;</p>
<dd> number of channels</p>
<dt>rate=&lt;value&gt;</p>
<dd> rate in samples per second</p>
<dt>samplesize=&lt;value&gt;</p>
<dd> sample size in bytes</p>
<dt>bitrate=&lt;value&gt;</p>
<dd> bitrate for rawaudio files</p>
<dt>format=&lt;value&gt;</p>
<dd> fourcc in hex</dl>
</dl>
<dt><code>-rawvideo &lt;option1:option2:&#8230;&gt;</code></p>
<dd> This option lets you play raw video files. You have to use -demuxer rawvideo as well. </p>
<p> Available options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>fps=&lt;value&gt;</p>
<dd> rate in frames per second (default: 25.0)</p>
<dt>sqcif|qcif|cif|4cif|pal|ntsc</p>
<dd> set standard image size</p>
<dt>w=&lt;value&gt;</p>
<dd> image width in pixels</p>
<dt>h=&lt;value&gt;</p>
<dd> image height in pixels</p>
<dt>i420|yv12|yuy2|y8</p>
<dd> set colorspace</p>
<dt>format=&lt;value&gt;</p>
<dd> colorspace (fourcc) in hex or string constant. Use -rawvideo format=help for a list of possible strings.</p>
<dt>size=&lt;value&gt;</p>
<dd> frame size in Bytes</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer foreman.qcif -demuxer rawvideo -rawvideo qcif</p>
<dd> Play the famous &quot;foreman&quot; sample video.</p>
<dt>mplayer sample-720&#215;576.yuv -demuxer rawvideo -rawvideo w=720:h=576</p>
<dd> Play a raw YUV sample.</dl>
</dl>
<dt><code>-referrer &lt;string&gt; (network only)</code></p>
<dd> Specify a referrer path or URL for HTTP requests.</p>
<dt><code>-rtsp-port</code></p>
<dd> Used with &#8216;<a href="rtsp://'">rtsp://&#8217;</a> URLs to force the client&#8217;s port number. This option may be useful if you are behind a router and want to forward the RTSP stream from the server to a specific client.</p>
<dt><code>-rtsp-destination</code></p>
<dd> Used with &#8216;<a href="rtsp://'">rtsp://&#8217;</a> URLs to force the destination IP address to be bound. This option may be useful with some RTSP server which do not send RTP packets to the right interface. If the connection to the RTSP server fails, use -v to see which IP address MPlayer tries to bind to and try to force it to one assigned to your computer instead.</p>
<dt><code>-rtsp-stream-over-tcp (LIVE555 and NEMESI only)</code></p>
<dd> Used with &#8216;<a href="rtsp://'">rtsp://&#8217;</a> URLs to specify that the resulting incoming RTP and RTCP packets be streamed over TCP (using the same TCP connection as RTSP). This option may be useful if you have a broken internet connection that does not pass incoming UDP packets (see <a rel="nofollow" href="http://www.live555.com/:mplayer/">http://www.live555.com/:mplayer/</a>).</p>
<dt><code>-rtsp-stream-over-http (LIVE555 only)</code></p>
<dd> Used with &#8216;<a rel="nofollow" href="http://'">http://&#8217;</a> URLs to specify that the resulting incoming RTP and RTCP packets be streamed over HTTP.</p>
<dt><code>-saveidx &lt;filename&gt;</code></p>
<dd> Force index rebuilding and dump the index to &lt;filename&gt;. Currently this only works with AVI files.<br />
 <i>NOTE:</i> This option is obsolete now that MPlayer has OpenDML support.</p>
<dt><code>-sb &lt;byte position&gt; (also see -ss)</code></p>
<dd> Seek to byte position. Useful for playback from CD-ROM images or VOB files with junk at the beginning.</p>
<dt><code>-speed &lt;0.01-100&gt;</code></p>
<dd> Slow down or speed up playback by the factor given as parameter. Not guaranteed to work correctly with -oac copy. Add -af scaletempo to get past the 4x limit on playback.</p>
<dt><code>-srate &lt;Hz&gt;</code></p>
<dd> Select the output sample rate to be used (of course sound cards have limits on this). If the sample frequency selected is different from that of the current media, the resample or lavcresample audio filter will be inserted into the audio filter layer to compensate for the difference. The type of resampling can be controlled by the -af-adv option. The default is fast resampling that may cause distortion.</p>
<dt><code>-ss &lt;time&gt; (also see -sb)</code></p>
<dd> Seek to given time position. Use -ss nopts to disable seeking, -ss 0 has different behaviour. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-ss 56</p>
<dd> Seeks to 56 seconds.</p>
<dt>-ss 01:10:00</p>
<dd> Seeks to 1 hour 10 min.</dl>
</dl>
<dt><code>-tskeepbroken</code></p>
<dd> Tells MPlayer not to discard TS packets reported as broken in the stream. Sometimes needed to play corrupted MPEG-TS files.</p>
<dt><code>-tsprobe &lt;byte position&gt;</code></p>
<dd> When playing an MPEG-TS stream, this option lets you specify how many bytes in the stream you want MPlayer to search for the desired audio and video IDs.</p>
<dt><code>-tsprog &lt;1-65534&gt;</code></p>
<dd> When playing an MPEG-TS stream, you can specify with this option which program (if present) you want to play. Can be used with -vid and -aid.</p>
<dt><code>-tv &lt;option1:option2:&#8230;&gt; (TV/:PVR only)</code></p>
<dd> This option tunes various properties of the TV capture module. For watching TV with MPlayer, use &#8216;tv://&#8217; or &#8216;tv://&lt;channel_number&gt;&#8217; or even &#8216;tv://&lt;channel_name&gt; (see option channels for channel_name below) as a movie URL. You can also use &#8216;tv:///&lt;input_id&gt;&#8217; to start watching a movie from a composite or S-Video input (see option input for details). </p>
<p> Available options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>noaudio</p>
<dd> no sound</p>
<dt>automute=&lt;0-255&gt; (v4l and v4l2 only)</p>
<dd> If signal strength reported by device is less than this value, audio and video will be muted. In most cases automute=100 will be enough. Default is 0 (automute disabled).</p>
<dt>driver=&lt;value&gt;</p>
<dd> See -tv driver=help for a list of compiled-in TV input drivers. available: dummy, v4l, v4l2, bsdbt848 (default: autodetect)</p>
<dt>device=&lt;value&gt;</p>
<dd> Specify TV device (default: /dev/:video0). <i>NOTE:</i> For the bsdbt848 driver you can provide both bktr and tuner device names separating them with a comma, tuner after bktr (e.g. -tv device=/dev/bktr1,/dev/tuner1).</p>
<dt>input=&lt;value&gt;</p>
<dd> Specify input (default: 0 (TV), see console output for available inputs).</p>
<dt>freq=&lt;value&gt;</p>
<dd> Specify the frequency to set the tuner to (e.g. 511.250). Not compatible with the channels parameter.</p>
<dt>outfmt=&lt;value&gt;</p>
<dd> Specify the output format of the tuner with a preset value supported by the V4L driver (yv12, rgb32, rgb24, rgb16, rgb15, uyvy, yuy2, i420) or an arbitrary format given as hex value. Try outfmt=help for a list of all available formats.</p>
<dt>width=&lt;value&gt;</p>
<dd> output window width</p>
<dt>height=&lt;value&gt;</p>
<dd> output window height</p>
<dt>fps=&lt;value&gt;</p>
<dd> framerate at which to capture video (frames per second)</p>
<dt>buffersize=&lt;value&gt;</p>
<dd> maximum size of the capture buffer in megabytes (default: dynamical)</p>
<dt>norm=&lt;value&gt;</p>
<dd> For bsdbt848 and v4l, PAL, SECAM, NTSC are available. For v4l2, see the console output for a list of all available norms, also see the normid option below.</p>
<dt>normid=&lt;value&gt; (v4l2 only)</p>
<dd> Sets the TV norm to the given numeric ID. The TV norm depends on the capture card. See the console output for a list of available TV norms.</p>
<dt>channel=&lt;value&gt;</p>
<dd> Set tuner to &lt;value&gt; channel.</p>
<dt>chanlist=&lt;value&gt;</p>
<dd> available: argentina, australia, china-bcast, europe-east, europe-west, france, ireland, italy, japan-bcast, japan-cable, newzealand, russia, southafrica, us-bcast, us-cable, us-cable-hrc</p>
<dt>channels=&lt;chan&gt;-&lt;name&gt;[=&lt;norm&gt;],&lt;chan&gt;-&lt;name&gt;[=&lt;norm&gt;],&#8230;</p>
<dd> Set names for channels. <i>NOTE:</i> If &lt;chan&gt; is an integer greater than 1000, it will be treated as frequency (in kHz) rather than channel name from frequency table.<br />
 Use _ for spaces in names (or play with quoting ;-). The channel names will then be written using OSD, and the slave commands tv_step_channel, tv_set_channel and tv_last_channel will be usable for a remote control (see LIRC). Not compatible with the frequency parameter.<br />
 <i>NOTE:</i> The channel number will then be the position in the &#8216;channels&#8217; list, beginning with 1.<br />
 <i>EXAMPLE:</i> tv://1, tv://TV1, tv_set_channel 1, tv_set_channel TV1</p>
<dt>[brightness|contrast|hue|saturation]=&lt;-100-100&gt;</p>
<dd> Set the image equalizer on the card.</p>
<dt>audiorate=&lt;value&gt;</p>
<dd> Set input audio sample rate.</p>
<dt>forceaudio</p>
<dd> Capture audio even if there are no audio sources reported by v4l.</p>
<dt>alsa&nbsp;</p>
<dd> Capture from ALSA.</p>
<dt>amode=&lt;0-3&gt;</p>
<dd> Choose an audio mode:</p>
<dl>
<dt>
<dd> 0: mono<br />
 1: stereo<br />
 2: language 1<br />
 3: language 2</dl>
<dt>forcechan=&lt;1-2&gt;</p>
<dd> By default, the count of recorded audio channels is determined automatically by querying the audio mode from the TV card. This option allows forcing stereo/:mono recording regardless of the amode option and the values returned by v4l. This can be used for troubleshooting when the TV card is unable to report the current audio mode.</p>
<dt>adevice=&lt;value&gt;</p>
<dd> Set an audio device. &lt;value&gt; should be /dev/:xxx for OSS and a hardware ID for ALSA. You must replace any &#8216;:&#8217; by a &#8216;.&#8217; in the hardware ID for ALSA.</p>
<dt>audioid=&lt;value&gt;</p>
<dd> Choose an audio output of the capture card, if it has more than one.</p>
<dt>[volume|bass|treble|balance]=&lt;0-65535&gt; (v4l1)</p>
<dd>
<dt>[volume|bass|treble|balance]=&lt;0-100&gt; (v4l2)</p>
<dd> These options set parameters of the mixer on the video capture card. They will have no effect, if your card does not have one. For v4l2 50 maps to the default value of the control, as reported by the driver.</p>
<dt>gain=&lt;0-100&gt; (v4l2)</p>
<dd> Set gain control for video devices (usually webcams) to the desired value and switch off automatic control. A value of 0 enables automatic control. If this option is omitted, gain control will not be modified.</p>
<dt>immediatemode=&lt;bool&gt;</p>
<dd> A value of 0 means capture and buffer audio and video together (default for MEncoder). A value of 1 (default for MPlayer) means to do video capture only and let the audio go through a loopback cable from the TV card to the sound card.</p>
<dt>mjpeg</p>
<dd> Use hardware MJPEG compression (if the card supports it). When using this option, you do not need to specify the width and height of the output window, because MPlayer will determine it automatically from the decimation value (see below).</p>
<dt>decimation=&lt;1|2|4&gt;</p>
<dd> choose the size of the picture that will be compressed by hardware MJPEG compression:</p>
<dl>
<dt>
<dd> 1: full size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;704&#215;576&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PAL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;704&#215;480&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NTSC<br />
 2: medium size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;352&#215;288&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PAL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;352&#215;240&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NTSC<br />
 4: small size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;176&#215;144&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PAL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;176&#215;120&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NTSC</dl>
<dt>quality=&lt;0-100&gt;</p>
<dd> Choose the quality of the JPEG compression (&lt; 60 recommended for full size).</p>
<dt>tdevice=&lt;value&gt;</p>
<dd> Specify TV teletext device (example: /dev/:vbi0) (default: none).</p>
<dt>tformat=&lt;format&gt;</p>
<dd> Specify TV teletext display format (default: 0):</p>
<dl>
<dt>
<dd> 0: opaque<br />
 1: transparent<br />
 2: opaque with inverted colors<br />
 3: transparent with inverted colors</dl>
<dt>tpage=&lt;100-899&gt;</p>
<dd> Specify initial TV teletext page number (default: 100).</p>
<dt>tlang=&lt;-1-127&gt;</p>
<dd> Specify default teletext language code (default: 0), which will be used as primary language until a type 28 packet is received. Useful when the teletext system uses a non-latin character set, but language codes are not transmitted via teletext type 28 packets for some reason. To see a list of supported language codes set this option to -1.</p>
<dt>hidden_video_renderer (dshow only)</p>
<dd> Terminate stream with video renderer instead of Null renderer (default: off). Will help if video freezes but audio does not. <i>NOTE:</i> May not work with -vo directx and -vf crop combination.</p>
<dt>hidden_vp_renderer (dshow only)</p>
<dd> Terminate VideoPort pin stream with video renderer instead of removing it from the graph (default: off). Useful if your card has a VideoPort pin and video is choppy. <i>NOTE:</i> May not work with -vo directx and -vf crop combination.</p>
<dt>system_clock (dshow only)</p>
<dd> Use the system clock as sync source instead of the default graph clock (usually the clock from one of the live sources in graph).</p>
<dt>normalize_audio_chunks (dshow only)</p>
<dd> Create audio chunks with a time length equal to video frame time length (default: off). Some audio cards create audio chunks about 0.5s in size, resulting in choppy video when using immediatemode=0.</dl>
</dl>
<dt><code>-tvscan &lt;option1:option2:&#8230;&gt; (TV and MPlayer only)</code></p>
<dd> Tune the TV channel scanner. MPlayer will also print value for &quot;-tv channels=&quot; option, including existing and just found channels. </p>
<p> Available suboptions are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>autostart</p>
<dd> Begin channel scanning immediately after startup (default: disabled).</p>
<dt>period=&lt;0.1-2.0&gt;</p>
<dd> Specify delay in seconds before switching to next channel (default: 0.5). Lower values will cause faster scanning, but can detect inactive TV channels as active.</p>
<dt>threshold=&lt;1-100&gt;</p>
<dd> Threshold value for the signal strength (in percent), as reported by the device (default: 50). A signal strength higher than this value will indicate that the currently scanning channel is active.</dl>
</dl>
<dt><code>-user &lt;username&gt; (also see -passwd) (network only)</code></p>
<dd> Specify username for HTTP authentication.</p>
<dt><code>-user-agent &lt;string&gt;</code></p>
<dd> Use &lt;string&gt; as user agent for HTTP streaming.</p>
<dt><code>-vid &lt;ID&gt;</code></p>
<dd> Select video channel (MPG: 0-15, ASF: 0-255, MPEG-TS: 17-8190). When playing an MPEG-TS stream, MPlayer/:MEncoder will use the first program (if present) with the chosen video stream.</p>
<dt><code>-vivo &lt;suboption&gt; (DEBUG CODE)</code></p>
<dd> Force audio parameters for the VIVO demuxer (for debugging purposes). FIXME: Document this.</dl>
<h2>OSD/SUBTITLE OPTIONS</h2>
<p> <i>NOTE:</i> Also see -vf expand.</p>
<dl>
<dt><code>-ass (FreeType only)</code></p>
<dd> Turn on SSA/ASS subtitle rendering. With this option, libass will be used for SSA/ASS external subtitles and Matroska tracks. You may also want to use -embeddedfonts.<br />
 <i>NOTE:</i> Unlike normal OSD, libass uses fontconfig by default. To disable it, use -nofontconfig.</p>
<dt><code>-ass-border-color &lt;value&gt;</code></p>
<dd> Sets the border (outline) color for text subtitles. The color format is RRGGBBAA.</p>
<dt><code>-ass-bottom-margin &lt;value&gt;</code></p>
<dd> Adds a black band at the bottom of the frame. The SSA/ASS renderer can place subtitles there (with -ass-use-margins).</p>
<dt><code>-ass-color &lt;value&gt;</code></p>
<dd> Sets the color for text subtitles. The color format is RRGGBBAA.</p>
<dt><code>-ass-font-scale &lt;value&gt;</code></p>
<dd> Set the scale coefficient to be used for fonts in the SSA/ASS renderer.</p>
<dt><code>-ass-force-style &lt;[Style.]Param=Value[,&#8230;]&gt;</code></p>
<dd> Override some style or script info parameters. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -ass-force-style FontName=Arial,Default.Bold=1<br />
 -ass-force-style PlayResY=768</dl>
<dt><code>-ass-hinting &lt;type&gt;</code></p>
<dd> Set hinting type. &lt;type&gt; can be:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> no hinting</p>
<dt>1</p>
<dd> FreeType autohinter, light mode</p>
<dt>2</p>
<dd> FreeType autohinter, normal mode</p>
<dt>3</p>
<dd> font native hinter</p>
<dt>0-3 + 4</p>
<dd> The same, but hinting will only be performed if the OSD is rendered at screen resolution and will therefore not be scaled.</dl>
</dl>
<dl>
<dt>
<dd> The default value is 7 (use native hinter for unscaled OSD and no hinting otherwise).</dl>
<dt><code>-ass-line-spacing &lt;value&gt;</code></p>
<dd> Set line spacing value for SSA/ASS renderer.</p>
<dt><code>-ass-styles &lt;filename&gt;</code></p>
<dd> Load all SSA/ASS styles found in the specified file and use them for rendering text subtitles. The syntax of the file is exactly like the [V4 Styles] / [V4+ Styles] section of SSA/ASS.</p>
<dt><code>-ass-top-margin &lt;value&gt;</code></p>
<dd> Adds a black band at the top of the frame. The SSA/ASS renderer can place toptitles there (with -ass-use-margins).</p>
<dt><code>-ass-use-margins</code></p>
<dd> Enables placing toptitles and subtitles in black borders when they are available.</p>
<dt><code>-dumpjacosub (MPlayer only)</code></p>
<dd> Convert the given subtitle (specified with the -sub option) to the time-based JACOsub subtitle format. Creates a dumpsub.js file in the current directory.</p>
<dt><code>-dumpmicrodvdsub (MPlayer only)</code></p>
<dd> Convert the given subtitle (specified with the -sub option) to the MicroDVD subtitle format. Creates a dumpsub.sub file in the current directory.</p>
<dt><code>-dumpmpsub (MPlayer only)</code></p>
<dd> Convert the given subtitle (specified with the -sub option) to MPlayer&#8217;s subtitle format, MPsub. Creates a dump.mpsub file in the current directory.</p>
<dt><code>-dumpsami (MPlayer only)</code></p>
<dd> Convert the given subtitle (specified with the -sub option) to the time-based SAMI subtitle format. Creates a dumpsub.smi file in the current directory.</p>
<dt><code>-dumpsrtsub (MPlayer only)</code></p>
<dd> Convert the given subtitle (specified with the -sub option) to the time-based SubViewer (SRT) subtitle format. Creates a dumpsub.srt file in the current directory.<br />
 <i>NOTE:</i> Some broken hardware players choke on SRT subtitle files with Unix line endings. If you are unlucky enough to have such a box, pass your subtitle files through unix2dos or a similar program to replace Unix line endings with DOS/Windows line endings.</p>
<dt><code>-dumpsub (MPlayer only) (BETA CODE)</code></p>
<dd> Dumps the subtitle substream from VOB streams. Also see the -dump*sub and -vobsubout* options.</p>
<dt><code>-embeddedfonts (FreeType only)</code></p>
<dd> Enables extraction of Matroska embedded fonts (default: disabled). These fonts can be used for SSA/ASS subtitle rendering (-ass option). Font files are created in the ~/.mplayer/:fonts directory.<br />
 <i>NOTE:</i> With FontConfig 2.4.2 or newer, embedded fonts are opened directly from memory, and this option is enabled by default.</p>
<dt><code>-ffactor &lt;number&gt;</code></p>
<dd> Resample the font alphamap. Can be:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> plain white fonts</p>
<dt>0.75</p>
<dd> very narrow black outline (default)</p>
<dt>1</p>
<dd> narrow black outline</p>
<dt>10</p>
<dd> bold black outline</dl>
</dl>
<dt><code>-flip-hebrew (FriBiDi only)</code></p>
<dd> Turns on flipping subtitles using FriBiDi.</p>
<dt><code>-noflip-hebrew-commas</code></p>
<dd> Change FriBiDi&#8217;s assumptions about the placements of commas in subtitles. Use this if commas in subtitles are shown at the start of a sentence instead of at the end.</p>
<dt><code>-font &lt;path to font.desc file, path to font (FreeType), font pattern (Fontconfig)&gt;</code></p>
<dd> Search for the OSD/:subtitle fonts in an alternative directory (default for normal fonts: ~/:.mplayer/:font/:font.desc, default for FreeType fonts: ~/.mplayer/:subfont.ttf, default for Fontconfig: &quot;sans-serif&quot;).<br />
 <i>NOTE:</i> With FreeType, this option determines the path to the font file. With Fontconfig, this option determines the Fontconfig font pattern. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -font ~/:.mplayer/:arial-14/:font.desc<br />
 -font ~/:.mplayer/:arialuni.ttf<br />
 -font &#8216;Bitstream Vera Sans&#8217;<br />
 -font &#8216;Bitstream Vera Sans:style=Bold&#8217;</dl>
<dt><code>-fontconfig (fontconfig only)</code></p>
<dd> Enables the usage of fontconfig managed fonts (default: autodetect).<br />
 <i>NOTE:</i> By default fontconfig is used for libass-rendered subtitles and not used for OSD. With -fontconfig it is used for both libass and OSD, with -nofontconfig it is not used at all, i.e. only then -font and -subfont will work with a given path to font.</p>
<dt><code>-forcedsubsonly</code></p>
<dd> Display only forced subtitles for the DVD subtitle stream selected by e.g. -slang.</p>
<dt><code>-fribidi-charset &lt;charset name&gt; (FriBiDi only)</code></p>
<dd> Specifies the character set that will be passed to FriBiDi when decoding non-UTF-8 subtitles (default: ISO8859-8).</p>
<dt><code>-ifo &lt;VOBsub IFO file&gt;</code></p>
<dd> Indicate the file that will be used to load palette and frame size for VOBsub subtitles.</p>
<dt><code>-noautosub</code></p>
<dd> Turns off automatic subtitle file loading.</p>
<dt><code>-osd-duration &lt;time&gt;</code></p>
<dd> Set the duration of the OSD messages in ms (default: 1000).</p>
<dt><code>-osd-fractions &lt;0-2&gt;</code></p>
<dd> Set how fractions of seconds of the current timestamp are printed on the OSD:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Do not display fractions (default).</p>
<dt>1</p>
<dd> Show the first two decimals.</p>
<dt>2</p>
<dd> Show approximated frame count within current second. This frame count is not accurate but only an approximation. For variable fps, the approximation is known to be far off the correct frame count.</dl>
</dl>
<dt><code>-osdlevel &lt;0-3&gt; (MPlayer only)</code></p>
<dd> Specifies which mode the OSD should start in.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> subtitles only</p>
<dt>1</p>
<dd> volume + seek (default)</p>
<dt>2</p>
<dd> volume + seek + timer + percentage</p>
<dt>3</p>
<dd> volume + seek + timer + percentage + total time</dl>
</dl>
<dt><code>-overlapsub</code></p>
<dd> Allows the next subtitle to be displayed while the current one is still visible (default is to enable the support only for specific formats).</p>
<dt><code>-progbar-align &lt;0-100&gt;</code></p>
<dd> Specify the vertical alignment of the progress bar (0: top, 100: bottom, default is 50, i.e. centered).</p>
<dt><code>-sid &lt;ID&gt; (also see -slang, -vobsubid)</code></p>
<dd> Display the subtitle stream specified by &lt;ID&gt; (0-31). MPlayer prints the available subtitle IDs when run in verbose (-v) mode. If you cannot select one of the subtitles on a DVD, also try -vobsubid.</p>
<dt><code>-nosub</code></p>
<dd> Disables any otherwise auto-selected internal subtitles (as e.g. the Matroska/mkv demuxer supports). Use -noautosub to disable the loading of external subtitle files.</p>
<dt><code>-slang &lt;language code[,language code,&#8230;]&gt; (also see -sid)</code></p>
<dd> Specify a priority list of subtitle languages to use. Different container formats employ different language codes. DVDs use ISO 639-1 two letter language codes, Matroska uses ISO 639-2 three letter language codes while OGM uses a free-form identifier. MPlayer prints the available languages when run in verbose (-v) mode. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer <a href="dvd://1">dvd://1</a> -slang hu,en</p>
<dd> Chooses the Hungarian subtitle track on a DVD and falls back on English if Hungarian is not available.</p>
<dt>mplayer -slang jpn example.mkv</p>
<dd> Plays a Matroska file with Japanese subtitles.</dl>
</dl>
<dt><code>-spuaa &lt;mode&gt;</code></p>
<dd> Antialiasing/:scaling mode for DVD/:VOBsub. A value of 16 may be added to &lt;mode&gt; in order to force scaling even when original and scaled frame size already match. This can be employed to e.g. smooth subtitles with gaussian blur. Available modes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> none (fastest, very ugly)</p>
<dt>1</p>
<dd> approximate (broken?)</p>
<dt>2</p>
<dd> full (slow)</p>
<dt>3</p>
<dd> bilinear (default, fast and not too bad)</p>
<dt>4</p>
<dd> uses swscaler gaussian blur (looks very good)</dl>
</dl>
<dt><code>-spualign &lt;-1-2&gt;</code></p>
<dd> Specify how SPU (DVD/:VOBsub) subtitles should be aligned.</p>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> original position</p>
<dt> 0</p>
<dd> Align at top (original behavior, default).</p>
<dt> 1</p>
<dd> Align at center.</p>
<dt> 2</p>
<dd> Align at bottom.</dl>
</dl>
<dt><code>-spugauss &lt;0.0-3.0&gt;</code></p>
<dd> Variance parameter of gaussian used by -spuaa 4. Higher means more blur (default: 1.0).</p>
<dt><code>-sub &lt;subtitlefile1,subtitlefile2,&#8230;&gt;</code></p>
<dd> Use/:display these subtitle files. Only one file can be displayed at the same time.</p>
<dt><code>-sub-bg-alpha &lt;0-255&gt;</code></p>
<dd> Specify the alpha channel value for subtitles and OSD backgrounds. Big values mean more transparency. 0 means completely transparent.</p>
<dt><code>-sub-bg-color &lt;0-255&gt;</code></p>
<dd> Specify the color value for subtitles and OSD backgrounds. Currently subtitles are grayscale so this value is equivalent to the intensity of the color. 255 means white and 0 black.</p>
<dt><code>-sub-demuxer &lt;[+]name&gt; (-subfile only) (BETA CODE)</code></p>
<dd> Force subtitle demuxer type for -subfile. Use a &#8216;+&#8217; before the name to force it, this will skip some checks! Give the demuxer name as printed by -sub-demuxer help. For backward compatibility it also accepts the demuxer ID as defined in subreader.h.</p>
<dt><code>-sub-fuzziness &lt;mode&gt;</code></p>
<dd> Adjust matching fuzziness when searching for subtitles:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> exact match (default)</p>
<dt>1</p>
<dd> Load all subs containing movie name.</p>
<dt>2</p>
<dd> Load all subs in the current and -sub-paths directories.</dl>
</dl>
<dt><code>-sub-no-text-pp</code></p>
<dd> Disables any kind of text post processing done after loading the subtitles. Used for debug purposes.</p>
<dt><code>-subalign &lt;0-2&gt;</code></p>
<dd> Specify which edge of the subtitles should be aligned at the height given by -subpos.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Align subtitle top edge (original behavior).</p>
<dt>1</p>
<dd> Align subtitle center.</p>
<dt>2</p>
<dd> Align subtitle bottom edge (default).</dl>
</dl>
<dt><code>-subcc &lt;1-8&gt;&nbsp;</code></p>
<dd> Display DVD Closed Caption (CC) subtitles from the specified channel. Values 5 to 8 select a mode that can extract EIA-608 compatibility streams from EIA-708 data. These are <code>not</code> the VOB subtitles, these are special ASCII subtitles for the hearing impaired encoded in the VOB userdata stream on most region 1 DVDs. CC subtitles have not been spotted on DVDs from other regions so far.</p>
<dt><code>-subcp &lt;codepage&gt; (iconv only)</code></p>
<dd> If your system supports <a href="/docs/linux/man/3-iconv/">iconv</a>(3), you can use this option to specify the subtitle codepage. It takes priority over both -utf8 and -unicode. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -subcp latin2<br />
 -subcp cp1250</dl>
<dt><code>-subcp enca:&lt;language&gt;:&lt;fallback codepage&gt; (ENCA only)</code></p>
<dd> You can specify your language using a two letter language code to make ENCA detect the codepage automatically. If unsure, enter anything and watch mplayer -v output for available languages. Fallback codepage specifies the codepage to use, when autodetection fails. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-subcp enca:cs:latin2</p>
<dd> Guess the encoding, assuming the subtitles are Czech, fall back on latin 2, if the detection fails.</p>
<dt>-subcp enca:pl:cp1250</p>
<dd> Guess the encoding for Polish, fall back on cp1250.</dl>
</dl>
<dt><code>-sub-paths &lt;path1,path2,&#8230;&gt;</code></p>
<dd> Specify extra subtitle paths to track in the media directory. </p>
<p> <i>EXAMPLE:</i> Assuming that /path/:to/:movie/:movie.avi is played and -sub-paths sub,subtitles,/tmp/subs is specified, MPlayer searches for subtitle files in these directories:</p>
<dl>
<dt>
<dd> /path/:to/:movie/<br />
 /path/:to/:movie/:sub/<br />
 /path/:to/:movie/:subtitles/<br />
 /tmp/:subs/<br />
 ~/.mplayer/:sub/</dl>
<dt><code>-subdelay &lt;sec&gt;</code></p>
<dd> Delays subtitles by &lt;sec&gt; seconds. Can be negative.</p>
<dt><code>-subfile &lt;filename&gt; (BETA CODE)</code></p>
<dd> Currently useless. Same as -audiofile, but for subtitle streams (OggDS?).</p>
<dt><code>-subfont &lt;path to font (FreeType), font pattern (Fontconfig)&gt; (FreeType only)</code></p>
<dd> Sets the subtitle font (see -font). If no -subfont is given, -font is used.</p>
<dt><code>-subfont-autoscale &lt;0-3&gt; (FreeType only)</code></p>
<dd> Sets the autoscale mode.<br />
 <i>NOTE:</i> 0 means that text scale and OSD scale are font heights in points. </p>
<p> The mode can be: </p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> no autoscale</p>
<dt>1</p>
<dd> proportional to movie height</p>
<dt>2</p>
<dd> proportional to movie width</p>
<dt>3</p>
<dd> proportional to movie diagonal (default)</dl>
</dl>
<dt><code>-subfont-blur &lt;0-8&gt; (FreeType only)</code></p>
<dd> Sets the font blur radius (default: 2).</p>
<dt><code>-subfont-encoding &lt;value&gt;</code></p>
<dd> Sets the font encoding. When set to &#8216;unicode&#8217;, all the glyphs from the font file will be rendered and unicode will be used (default: unicode). (Without FreeType, setting any other value than &#8216;unicode&#8217; will disable unicode glyphs rendering for font.desc files. With FreeType and for other values than &#8216;unicode&#8217; your system has to support <a href="/docs/linux/man/3-iconv/">iconv</a>(3) in order for this to work.)</p>
<dt><code>-subfont-osd-scale &lt;0-100&gt; (FreeType only)</code></p>
<dd> Sets the autoscale coefficient of the OSD elements (default: 6).</p>
<dt><code>-subfont-outline &lt;0-8&gt; (FreeType only)</code></p>
<dd> Sets the font outline thickness (default: 2).</p>
<dt><code>-subfont-text-scale &lt;0-100&gt; (FreeType only)</code></p>
<dd> Sets the subtitle text autoscale coefficient as percentage of the screen size (default: 5).</p>
<dt><code>-subfps &lt;rate&gt;</code></p>
<dd> Specify the framerate of the subtitle file (default: movie fps).<br />
 <i>NOTE:</i> &lt;rate&gt; &gt; movie fps speeds the subtitles up for frame-based subtitle files and slows them down for time-based ones.</p>
<dt><code>-subpos &lt;0-150&gt; (useful with -vf expand)</code></p>
<dd> Specify the position of subtitles on the screen. The value is the vertical position of the subtitle in % of the screen height. Values larger than 100 allow part of the subtitle to be cut off.</p>
<dt><code>-subwidth &lt;10-100&gt;</code></p>
<dd> Specify the maximum width of subtitles on the screen. Useful for TV-out. The value is the width of the subtitle in % of the screen width.</p>
<dt><code>-noterm-osd</code></p>
<dd> Disable the display of OSD messages on the console when no video output is available.</p>
<dt><code>-term-osd-esc &lt;escape sequence&gt;</code></p>
<dd> Specify the escape sequence to use before writing an OSD message on the console. The escape sequence should move the pointer to the beginning of the line used for the OSD and clear it (default: ^[[A^[[K).</p>
<dt><code>-unicode</code></p>
<dd> Tells MPlayer to handle the subtitle file as unicode. (It will only take effect if neither -subcp nor -utf8 is given.)</p>
<dt><code>-unrarexec &lt;path to unrar executable&gt; (not supported on MingW)</code></p>
<dd> Specify the path to the unrar executable so MPlayer can use it to access rar-compressed VOBsub files (default: not set, so the feature is off). The path must include the executable&#8217;s filename, i.e. /usr/local/bin/unrar.</p>
<dt><code>-utf8 &nbsp;<wbr>&nbsp;</code></p>
<dd> Tells MPlayer to handle the subtitle file as UTF-8. (It will only take effect if -subcp isn&#8217;t given, and it takes priority over -unicode.)</p>
<dt><code>-vobsub &lt;VOBsub file without extension&gt;</code></p>
<dd> Specify a VOBsub file to use for subtitles. Has to be the full pathname without extension, i.e. without the &#8216;.idx&#8217;, &#8216;.ifo&#8217; or &#8216;.sub&#8217;.</p>
<dt><code>-vobsubid &lt;0-31&gt;</code></p>
<dd> Specify the VOBsub subtitle ID.</dl>
<h2>AUDIO OUTPUT OPTIONS (MPLAYER ONLY)</h2>
<dl>
<dt><code>-abs &lt;value&gt; (-ao oss only) (OBSOLETE)</code></p>
<dd> Override audio driver/:card buffer size detection.</p>
<dt><code>-format &lt;format&gt; (also see the format audio filter)</code></p>
<dd> Select the sample format used for output from the audio filter layer to the sound card. The values that &lt;format&gt; can adopt are listed below in the description of the format audio filter.</p>
<dt><code>-mixer &lt;device&gt;</code></p>
<dd> Use a mixer device different from the default /dev/:mixer. For ALSA this is the mixer name.</p>
<dt><code>-mixer-channel &lt;mixer line&gt;[,mixer index] (-ao oss and -ao alsa only)</code></p>
<dd> This option will tell MPlayer to use a different channel for controlling volume than the default PCM. Options for OSS include <code>vol, pcm, line.</code> For a complete list of options look for SOUND_DEVICE_NAMES in /usr/:include/:linux/:soundcard.h. For ALSA you can use the names e.g. alsamixer displays, like <code>Master, Line, PCM.</code><br />
 <i>NOTE:</i> ALSA mixer channel names followed by a number must be specified in the &lt;name,number&gt; format, i.e. a channel labeled &#8216;PCM 1&#8217; in alsamixer must be converted to <code>PCM,1</code>.</p>
<dt><code>-softvol</code></p>
<dd> Force the use of the software mixer, instead of using the sound card mixer.</p>
<dt><code>-softvol-max &lt;10.0-10000.0&gt;</code></p>
<dd> Set the maximum amplification level in percent (default: 110). A value of 200 will allow you to adjust the volume up to a maximum of double the current level. With values below 100 the initial volume (which is 100%) will be above the maximum, which e.g. the OSD cannot display correctly.</p>
<dt><code>-volstep &lt;0-100&gt;</code></p>
<dd> Set the step size of mixer volume changes in percent of the whole range (default: 3).</p>
<dt><code>-volume &lt;-1-100&gt; (also see -af volume)</code></p>
<dd> Set the startup volume in the mixer, either hardware or software (if used with -softvol). A value of -1 (the default) will not change the volume.</dl>
<h2>AUDIO OUTPUT DRIVERS (MPLAYER ONLY)</h2>
<p> Audio output drivers are interfaces to different audio output facilities. The syntax is:</p>
<dl>
<dt><code>-ao &lt;driver1[:suboption1[=value]:&#8230;],driver2,&#8230;[,]&gt;</code></p>
<dd> Specify a priority list of audio output drivers to be used.</dl>
<p> If the list has a trailing &#8216;,&#8217; MPlayer will fall back on drivers not contained in the list. Suboptions are optional and can mostly be omitted.<br />
 <i>NOTE:</i> See -ao help for a list of compiled-in audio output drivers. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-ao alsa,oss,</p>
<dd> Try the ALSA driver, then the OSS driver, then others.</p>
<dt>-ao alsa:noblock:device=hw=0.3</p>
<dd> Sets noblock-mode and the device-name as first card, fourth device.</dl>
</dl>
<p> Available audio output drivers are:</p>
<dl>
<dt><code>alsa&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> ALSA 0.9/1.x audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>noblock</p>
<dd> Sets noblock-mode.</p>
<dt>device=&lt;device&gt;</p>
<dd> Sets the device name. Replace any &#8216;,&#8217; with &#8216;.&#8217; and any &#8216;:&#8217; with &#8216;=&#8217; in the ALSA device name. For hwac3 output via S/PDIF, use an &quot;iec958&quot; or &quot;spdif&quot; device, unless you really know how to set it correctly.</dl>
</dl>
<dt><code>oss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> OSS audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;dsp-device&gt;</p>
<dd> Sets the audio output device (default: /dev/:dsp).</p>
<dt>&lt;mixer-device&gt;</p>
<dd> Sets the audio mixer device (default: /dev/:mixer).</p>
<dt>&lt;mixer-channel&gt;</p>
<dd> Sets the audio mixer channel (default: pcm).</dl>
</dl>
<dt><code>sdl (SDL only)</code></p>
<dd> highly platform independent SDL (Simple Directmedia Layer) library audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;driver&gt;</p>
<dd> Explicitly choose the SDL audio driver to use (default: let SDL choose).</dl>
</dl>
<dt><code>arts&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> audio output through the aRts daemon</p>
<dt><code>esd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> audio output through the ESD daemon</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;server&gt;</p>
<dd> Explicitly choose the ESD server to use (default: localhost).</dl>
</dl>
<dt><code>jack&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> audio output through JACK (Jack Audio Connection Kit)</p>
<dl>
<dt>
<dd>
<dl>
<dt>(no)connect</p>
<dd> Automatically create connections to output ports (default: enabled). When enabled, the maximum number of output channels will be limited to the number of available output ports.</p>
<dt>port=&lt;name&gt;</p>
<dd> Connects to the ports with the given name (default: physical ports).</p>
<dt>name=&lt;client</p>
<dd> Client name that is passed to JACK (default: MPlayer [&lt;PID&gt;]). Useful if you want to have certain connections established automatically.</p>
<dt>(no)estimate</p>
<dd> Estimate the audio delay, supposed to make the video playback smoother (default: enabled).</p>
<dt>(no)autostart</p>
<dd> Automatically start jackd if necessary (default: disabled). Note that this seems unreliable and will spam stdout with server messages.</dl>
</dl>
<dt><code>nas&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> audio output through NAS</p>
<dt><code>coreaudio (Mac OS X only)</code></p>
<dd> native Mac OS X audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>device_id=&lt;id&gt;</p>
<dd> ID of output device to use (0 = default device)</p>
<dt>help</p>
<dd> List all available output devices with their IDs.</dl>
</dl>
<dt><code>openal&nbsp;</code></p>
<dd> Experimental OpenAL audio output driver</p>
<dt><code>pulse&nbsp;<wbr>&nbsp;</code></p>
<dd> PulseAudio audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>[&lt;host&gt;[:&lt;output sink&gt;[:broken_pause]]]</p>
<dd> Specify the host and optionally output sink to use. An empty &lt;host&gt; string uses a local connection, &quot;localhost&quot; uses network transfer (most likely not what you want). You can also explicitly force the workaround for broken pause functionality (default: autodetected). To only enable that without specifying a host/sink the syntax is -ao pulse:::broken_pause</dl>
</dl>
<dt><code>sgi (SGI only)</code></p>
<dd> native SGI audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;output device name&gt;</p>
<dd> Explicitly choose the output device/:interface to use (default: system-wide default). For example, &#8216;Analog Out&#8217; or &#8216;Digital Out&#8217;.</dl>
</dl>
<dt><code>sun (Sun only)</code></p>
<dd> native Sun audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the audio device to use (default: /dev/:audio).</dl>
</dl>
<dt><code>win32 (Windows only)</code></p>
<dd> native Windows waveout audio output driver</p>
<dt><code>dsound (Windows only)</code></p>
<dd> DirectX DirectSound audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>device=&lt;devicenum&gt;</p>
<dd> Sets the device number to use. Playing a file with -v will show a list of available devices.</dl>
</dl>
<dt><code>kai (OS/2 only)</code></p>
<dd> OS/2 KAI audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>uniaud</p>
<dd> Force UNIAUD mode.</p>
<dt>dart</p>
<dd> Force DART mode.</p>
<dt>(no)share</p>
<dd> Open audio in shareable or exclusive mode.</p>
<dt>bufsize=&lt;size&gt;</p>
<dd> Set buffer size to &lt;size&gt; in samples (default: 2048).</dl>
</dl>
<dt><code>dart (OS/2 only)</code></p>
<dd> OS/2 DART audio output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>(no)share</p>
<dd> Open DART in shareable or exclusive mode.</p>
<dt>bufsize=&lt;size&gt;</p>
<dd> Set buffer size to &lt;size&gt; in samples (default: 2048).</dl>
</dl>
<dt><code>dxr2 (also see -dxr2) (DXR2 only)</code></p>
<dd> Creative DXR2 specific output driver</p>
<dt><code>ivtv (IVTV only)</code></p>
<dd> IVTV specific MPEG audio output driver. Works with -ac hwmpa only.</p>
<dt><code>v4l2 (requires Linux 2.6.22+ kernel)</code></p>
<dd> Audio output driver for V4L2 cards with hardware MPEG decoder.</p>
<dt><code>mpegpes (DVB only)</code></p>
<dd> Audio output driver for DVB cards that writes the output to an MPEG-PES file if no DVB card is installed.</p>
<dl>
<dt>
<dd>
<dl>
<dt>card=&lt;1-4&gt;</p>
<dd> DVB card to use if more than one card is present. If not specified MPlayer will search the first usable card.</p>
<dt>file=&lt;filename&gt;</p>
<dd> output filename</dl>
</dl>
<dt><code>null&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Produces no audio output but maintains video playback speed. Use -nosound for benchmarking.</p>
<dt><code>pcm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> raw PCM/wave file writer audio output</p>
<dl>
<dt>
<dd>
<dl>
<dt>(no)waveheader</p>
<dd> Include or do not include the wave header (default: included). When not included, raw PCM will be generated.</p>
<dt>file=&lt;filename&gt;</p>
<dd> Write the sound to &lt;filename&gt; instead of the default audiodump.wav. If nowaveheader is specified, the default is audiodump.pcm.</p>
<dt>fast&nbsp;</p>
<dd> Try to dump faster than realtime. Make sure the output does not get truncated (usually with &quot;Too many video packets in buffer&quot; message). It is normal that you get a &quot;Your system is too SLOW to play this!&quot; message.</dl>
</dl>
<dt><code>plugin&nbsp;<wbr>&nbsp;</code></p>
<dd> plugin audio output driver</dl>
<h2>VIDEO OUTPUT OPTIONS (MPLAYER ONLY)</h2>
<dl>
<dt><code>-adapter &lt;value&gt;</code></p>
<dd> Set the graphics card that will receive the image. You can get a list of available cards when you run this option with -v. Currently only works with the directx video output driver.</p>
<dt><code>-bpp &lt;depth&gt;</code></p>
<dd> Override the autodetected color depth. Only supported by the fbdev, dga, svga, vesa video output drivers.</p>
<dt><code>-border</code></p>
<dd> Play movie with window border and decorations. Since this is on by default, use -noborder to disable the standard window decorations.</p>
<dt><code>-brightness &lt;-100-100&gt;</code></p>
<dd> Adjust the brightness of the video signal (default: 0). Not supported by all video output drivers.</p>
<dt><code>-contrast &lt;-100-100&gt;</code></p>
<dd> Adjust the contrast of the video signal (default: 0). Not supported by all video output drivers.</p>
<dt><code>-display &lt;name&gt; (X11 only)</code></p>
<dd> Specify the hostname and display number of the X server you want to display on. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -display xtest.localdomain:0</dl>
<dt><code>-dr &nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Turns on direct rendering (not supported by all codecs and video outputs). This can result in significantly faster blitting on some systems, on most the difference will be minimal. In some cases, particularly with decoders specifying their buffer requirements badly, it can be vastly slower.<br />
 <i>WARNING:</i> May cause OSD/SUB corruption!</p>
<dt><code>-dxr2 &lt;option1:option2:&#8230;&gt;</code></p>
<dd> This option is used to control the dxr2 video output driver.</p>
<dl>
<dt>
<dd>
<dl>
<dt>ar-mode=&lt;value&gt;</p>
<dd> aspect ratio mode (0 = normal, 1 = pan-and-scan, 2 = letterbox (default))</p>
<dt>iec958-encoded</p>
<dd> Set iec958 output mode to encoded.</p>
<dt>iec958-decoded</p>
<dd> Set iec958 output mode to decoded (default).</p>
<dt>macrovision=&lt;value&gt;</p>
<dd> macrovision mode (0 = off (default), 1 = agc, 2 = agc 2 colorstripe, 3 = agc 4 colorstripe)</p>
<dt>mute&nbsp;</p>
<dd> mute sound output</p>
<dt>unmute</p>
<dd> unmute sound output</p>
<dt>ucode=&lt;value&gt;</p>
<dd> path to the microcode</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>TV output</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>75ire</p>
<dd> enable 7.5 IRE output mode</p>
<dt>no75ire</p>
<dd> disable 7.5 IRE output mode (default)</p>
<dt>bw&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> b/w TV output</p>
<dt>color</p>
<dd> color TV output (default)</p>
<dt>interlaced</p>
<dd> interlaced TV output (default)</p>
<dt>nointerlaced</p>
<dd> disable interlaced TV output</p>
<dt>norm=&lt;value&gt;</p>
<dd> TV norm (ntsc (default), pal, pal60, palm, paln, palnc)</p>
<dt>square-pixel</p>
<dd> set pixel mode to square</p>
<dt>ccir601-pixel</p>
<dd> set pixel mode to ccir601</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>overlay</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>cr-left=&lt;0-500&gt;</p>
<dd> Set the left cropping value (default: 50).</p>
<dt>cr-right=&lt;0-500&gt;</p>
<dd> Set the right cropping value (default: 300).</p>
<dt>cr-top=&lt;0-500&gt;</p>
<dd> Set the top cropping value (default: 0).</p>
<dt>cr-bottom=&lt;0-500&gt;</p>
<dd> Set the bottom cropping value (default: 0).</p>
<dt>ck-[r|g|b]=&lt;0-255&gt;</p>
<dd> Set the r(ed), g(reen) or b(lue) gain of the overlay color-key.</p>
<dt>ck-[r|g|b]min=&lt;0-255&gt;</p>
<dd> minimum value for the respective color key</p>
<dt>ck-[r|g|b]max=&lt;0-255&gt;</p>
<dd> maximum value for the respective color key</p>
<dt>ignore-cache</p>
<dd> Ignore cached overlay settings.</p>
<dt>update-cache</p>
<dd> Update cached overlay settings.</p>
<dt>ol-osd</p>
<dd> Enable overlay onscreen display.</p>
<dt>nool-osd</p>
<dd> Disable overlay onscreen display (default).</p>
<dt>ol[h|w|x|y]-cor=&lt;-20-20&gt;</p>
<dd> Adjust the overlay size (h,w) and position (x,y) in case it does not match the window perfectly (default: 0).</p>
<dt>overlay</p>
<dd> Activate overlay (default).</p>
<dt>nooverlay</p>
<dd> Activate TV-out.</p>
<dt>overlay-ratio=&lt;1-2500&gt;</p>
<dd> Tune the overlay (default: 1000).</dl>
</dl>
<dt><code>-fbmode &lt;modename&gt; (-vo fbdev only)</code></p>
<dd> Change video mode to the one that is labeled as &lt;modename&gt; in /etc/:fb.modes.<br />
 <i>NOTE:</i> VESA framebuffer does not support mode changing.</p>
<dt><code>-fbmodeconfig &lt;filename&gt; (-vo fbdev only)</code></p>
<dd> Override framebuffer mode configuration file (default: /etc/:fb.modes).</p>
<dt><code>-fs (also see -zoom)</code></p>
<dd> Fullscreen playback (centers movie, and paints black bands around it). Not supported by all video output drivers.</p>
<dt><code>-fsmode-dontuse &lt;0-31&gt; (OBSOLETE, use the -fs option)</code></p>
<dd> Try this option if you still experience fullscreen problems.</p>
<dt><code>-fstype &lt;type1,type2,&#8230;&gt; (X11 only)</code></p>
<dd> Specify a priority list of fullscreen modes to be used. You can negate the modes by prefixing them with &#8216;-&#8216;. If you experience problems like the fullscreen window being covered by other windows try using a different order.<br />
 <i>NOTE:</i> See -fstype help for a full list of available modes. </p>
<p> The available types are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>above</p>
<dd> Use the _NETWM_STATE_ABOVE hint if available.</p>
<dt>below</p>
<dd> Use the _NETWM_STATE_BELOW hint if available.</p>
<dt>fullscreen</p>
<dd> Use the _NETWM_STATE_FULLSCREEN hint if available.</p>
<dt>layer</p>
<dd> Use the _WIN_LAYER hint with the default layer.</p>
<dt>layer=&lt;0&#8230;15&gt;</p>
<dd> Use the _WIN_LAYER hint with the given layer number.</p>
<dt>netwm</p>
<dd> Force NETWM style.</p>
<dt>none&nbsp;</p>
<dd> Clear the list of modes; you can add modes to enable afterward.</p>
<dt>stays_on_top</p>
<dd> Use _NETWM_STATE_STAYS_ON_TOP hint if available.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>layer,stays_on_top,above,fullscreen</p>
<dd> Default order, will be used as a fallback if incorrect or unsupported modes are specified.</p>
<dt>-fullscreen</p>
<dd> Fixes fullscreen switching on OpenBox 1.x.</dl>
</dl>
<dt><code>-fs-border-left &lt;pixels&gt;</code></p>
<dd>
<dt><code>-fs-border-right &lt;pixels&gt;</code></p>
<dd>
<dt><code>-fs-border-top &lt;pixels&gt;</code></p>
<dd>
<dt><code>-fs-border-bottom &lt;pixels&gt;</code></p>
<dd> Specify extra borders in full screen mode. The borders apply to all displayed elements: video, OSD and EOSD. The number of pixels is specified in terms of screen resolution. Currently only supported with by the gl video output driver.</p>
<dt><code>-gamma &lt;-100-100&gt;</code></p>
<dd> Adjust the gamma of the video signal (default: 0). Not supported by all video output drivers.</p>
<dt><code>-geometry x[%][:y[%]] or [WxH][+-x+-y]</code></p>
<dd> Adjust where the output is on the screen initially. The x and y specifications are in pixels measured from the top-left of the screen to the top-left of the image being displayed, however if a percentage sign is given after the argument it turns the value into a percentage of the screen size in that direction. It also supports the standard X11 -geometry option format, in which e.g. +10-50 means &quot;place 10 pixels from the left border and 50 pixels from the lower border&quot; and &quot;&#8211;20+-10&quot; means &quot;place 20 pixels beyond the right and 10 pixels beyond the top border&quot;. If an external window is specified using the -wid option, then the x and y coordinates are relative to the top-left corner of the window rather than the screen. The coordinates are relative to the screen given with -screen for the video output drivers that fully support -screen (direct3d, gl, gl_tiled, vdpau, x11, xv, xvmc, corevideo).<br />
 <i>NOTE:</i> This option is only supported by the x11, xmga, xv, xvmc, xvidix, gl, gl_tiled, direct3d, directx, fbdev, sdl, dfxfb and corevideo video output drivers. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>50:40</p>
<dd> Places the window at x=50, y=40.</p>
<dt>50%:50%</p>
<dd> Places the window in the middle of the screen.</p>
<dt>100%&nbsp;</p>
<dd> Places the window at the middle of the right edge of the screen.</p>
<dt>100%:100%</p>
<dd> Places the window at the bottom right corner of the screen.</dl>
</dl>
<dt><code>-gui-wid &lt;window ID&gt; (also see -wid) (GUI only)</code></p>
<dd> This tells the GUI to also use an X11 window and stick itself to the bottom of the video, which is useful to embed a mini-GUI in a browser (with the MPlayer plugin for instance).</p>
<dt><code>-hue &lt;-100-100&gt;</code></p>
<dd> Adjust the hue of the video signal (default: 0). You can get a colored negative of the image with this option. Not supported by all video output drivers.</p>
<dt><code>-monitor-dotclock &lt;range[,range,&#8230;]&gt; (-vo fbdev and vesa only)</code></p>
<dd> Specify the dotclock or pixelclock range of the monitor.</p>
<dt><code>-monitor-hfreq &lt;range[,range,&#8230;]&gt; (-vo fbdev and vesa only)</code></p>
<dd> Specify the horizontal frequency range of the monitor.</p>
<dt><code>-monitor-vfreq &lt;range[,range,&#8230;]&gt; (-vo fbdev and vesa only)</code></p>
<dd> Specify the vertical frequency range of the monitor.</p>
<dt><code>-monitoraspect &lt;ratio&gt; (also see -aspect)</code></p>
<dd> Set the aspect ratio of your monitor or TV screen. A value of 0 disables a previous setting (e.g. in the config file). Overrides the -monitorpixelaspect setting if enabled. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -monitoraspect 4:3 or 1.3333<br />
 -monitoraspect 16:9 or 1.7777</dl>
<dt><code>-monitorpixelaspect &lt;ratio&gt; (also see -aspect)</code></p>
<dd> Set the aspect of a single pixel of your monitor or TV screen (default: 1). A value of 1 means square pixels (correct for (almost?) all LCDs).</p>
<dt><code>-name (X11 only)</code></p>
<dd> Set the window class name.</p>
<dt><code>-nodouble</code></p>
<dd> Disables double buffering, mostly for debugging purposes. Double buffering fixes flicker by storing two frames in memory, and displaying one while decoding another. It can affect OSD negatively, but often removes OSD flickering.</p>
<dt><code>-nograbpointer</code></p>
<dd> Do not grab the mouse pointer after a video mode change (-vm). Useful for multihead setups.</p>
<dt><code>-nokeepaspect</code></p>
<dd> Do not keep window aspect ratio when resizing windows. Only works with the x11, xv, xmga, xvidix, directx video output drivers. Furthermore under X11 your window manager has to honor window aspect hints.</p>
<dt><code>-ontop&nbsp;</code></p>
<dd> Makes the player window stay on top of other windows. Supported by video output drivers which use X11, except SDL, as well as directx, corevideo, quartz, ggi and gl_tiled.</p>
<dt><code>-panscan &lt;0.0-1.0&gt;</code></p>
<dd> Enables pan-and-scan functionality (cropping the sides of e.g. a 16:9 movie to make it fit a 4:3 display without black bands). The range controls how much of the image is cropped. Only works with the directx, xv, xmga, mga, gl, gl_tiled, quartz, corevideo and xvidix video output drivers.<br />
 <i>NOTE:</i> Values between -1 and 0 are allowed as well, but highly experimental and may crash or worse. Use at your own risk!</p>
<dt><code>-panscanrange &lt;-19.0-99.0&gt; (experimental)</code></p>
<dd> Change the range of the pan-and-scan functionality (default: 1). Positive values mean multiples of the default range. Negative numbers mean you can zoom in up to a factor of -panscanrange+1. E.g. -panscanrange -3 allows a zoom factor of up to 4. This feature is experimental.</p>
<dt><code>-border-pos-x &lt;0.0-1.0&gt; (-vo gl,xv,xvmc,vdpau,direct3d only, default 0.5)</code></p>
<dd> When black borders are added to adjust for aspect, this determines where they are placed. 0.0 places borders on the right, 1.0 on the left. Values outside the range 0.0 &#8211; 1.0 will add extra black borders on one side and remove part of the image on the other side.</p>
<dt><code>-border-pos-y &lt;0.0-1.0&gt; (-vo gl,xv,xvmc,vdpau,direct3d only, default 0.5)</code></p>
<dd> As -border-pos-x but for top/bottom borders. 0.0 places borders on the bottom, 1.0 on the top.</p>
<dt><code>-monitor-orientation &lt;0-3&gt; (experimental)</code></p>
<dd> Rotate display by 90, 180 or 270 degrees. Rotates also the OSD, not just the video image itself. Currently only supported by the gl video output driver. For all other video outputs -vf ass,expand=osd=1,rotate=n can be used, in the future this might even happen automatically.</p>
<dt><code>-refreshrate &lt;Hz&gt;</code></p>
<dd> Set the monitor refreshrate in Hz. Currently only supported by -vo directx combined with the -vm option.</p>
<dt><code>-rootwin</code></p>
<dd> Play movie in the root window (desktop background). Desktop background images may cover the movie window, though. Only works with the x11, xv, xmga, xvidix, quartz, corevideo and directx video output drivers.</p>
<dt><code>-saturation &lt;-100-100&gt;</code></p>
<dd> Adjust the saturation of the video signal (default: 0). You can get grayscale output with this option. Not supported by all video output drivers.</p>
<dt><code>-screenh &lt;pixels&gt;</code></p>
<dd> Specify the screen height for video output drivers which do not know the screen resolution like fbdev, x11 and TV-out.</p>
<dt><code>-screenw &lt;pixels&gt;</code></p>
<dd> Specify the screen width for video output drivers which do not know the screen resolution like fbdev, x11 and TV-out.</p>
<dt><code>-(no)stop-xscreensaver (X11 only)</code></p>
<dd> Turns off xscreensaver at startup and turns it on again on exit (default: enabled). If your screensaver supports neither the XSS nor XResetScreenSaver API please use -heartbeat-cmd instead.</p>
<dt><code>-title (also see -use-filename-title)</code></p>
<dd> Set the window title. Supported by X11-based video output drivers.</p>
<dt><code>-use-filename-title (also see -title)</code></p>
<dd> Set the window title using the media filename, when not set with -title. Supported by X11-based video output drivers.</p>
<dt><code>-vm &nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Try to change to a different video mode. Supported by the dga, x11, xv, sdl and directx video output drivers. If used with the directx video output driver the -screenw, -screenh, -bpp and -refreshrate options can be used to set the new display mode.</p>
<dt><code>-vsync &nbsp;<wbr>&nbsp;</code></p>
<dd> Enables VBI for the vesa, dfbmga and svga video output drivers.</p>
<dt><code>-wid &lt;window ID&gt; (also see -gui-wid) (X11, OpenGL and DirectX only)</code></p>
<dd> This tells MPlayer to attach to an existing window. Useful to embed MPlayer in a browser (e.g. the plugger extension). This option fills the given window completely, thus aspect scaling, panscan, etc are no longer handled by MPlayer but must be managed by the application that created the window.</p>
<dt><code>-screen &lt;-2-&#8230;&gt; (alias for -xineramascreen)</code></p>
<dd> In Xinerama configurations (i.e. a single desktop that spans across multiple displays) this option tells MPlayer which screen to display the movie on. A value of -2 means fullscreen across the whole virtual display (in this case Xinerama information is completely ignored), -1 means fullscreen on the display the window currently is on. The initial position set via the -geometry option is relative to the specified screen. Will usually only work with &quot;-fstype -fullscreen&quot; or &quot;-fstype none&quot;. This option is not suitable to only set the startup screen (because it will always display on the given screen in fullscreen mode), -geometry is the best that is available for that purpose currently. Supported by at least the direct3d, gl, gl_tiled, x11, xv and corevideo video output drivers.</p>
<dt><code>-zrbw (-vo zr only)</code></p>
<dd> Display in black and white. For optimal performance, this can be combined with &#8216;-lavdopts gray&#8217;.</p>
<dt><code>-zrcrop &lt;[width]x[height]+[x offset]+[y offset]&gt; (-vo zr only)</code></p>
<dd> Select a part of the input image to display, multiple occurrences of this option switch on cinerama mode. In cinerama mode the movie is distributed over more than one TV (or beamer) to create a larger image. Options appearing after the n-th -zrcrop apply to the n-th MJPEG card, each card should at least have a -zrdev in addition to the -zrcrop. For examples, see the output of -zrhelp and the Zr section of the documentation.</p>
<dt><code>-zrdev &lt;device&gt; (-vo zr only)</code></p>
<dd> Specify the device special file that belongs to your MJPEG card, by default the zr video output driver takes the first v4l device it can find.</p>
<dt><code>-zrfd (-vo zr only)</code></p>
<dd> Force decimation: Decimation, as specified by -zrhdec and -zrvdec, only happens if the hardware scaler can stretch the image to its original size. Use this option to force decimation.</p>
<dt><code>-zrhdec &lt;1|2|4&gt; (-vo zr only)</code></p>
<dd> Horizontal decimation: Ask the driver to send only every 2nd or 4th line/:pixel of the input image to the MJPEG card and use the scaler of the MJPEG card to stretch the image to its original size.</p>
<dt><code>-zrhelp (-vo zr only)</code></p>
<dd> Display a list of all -zr* options, their default values and a cinerama mode example.</p>
<dt><code>-zrnorm &lt;norm&gt; (-vo zr only)</code></p>
<dd> Specify the TV norm as PAL or NTSC (default: no change).</p>
<dt><code>-zrquality &lt;1-20&gt; (-vo zr only)</code></p>
<dd> A number from 1 (best) to 20 (worst) representing the JPEG encoding quality.</p>
<dt><code>-zrvdec &lt;1|2|4&gt; (-vo zr only)</code></p>
<dd> Vertical decimation: Ask the driver to send only every 2nd or 4th line/:pixel of the input image to the MJPEG card and use the scaler of the MJPEG card to stretch the image to its original size.</p>
<dt><code>-zrxdoff &lt;x display offset&gt; (-vo zr only)</code></p>
<dd> If the movie is smaller than the TV screen, this option specifies the x offset from the upper-left corner of the TV screen (default: centered).</p>
<dt><code>-zrydoff &lt;y display offset&gt; (-vo zr only)</code></p>
<dd> If the movie is smaller than the TV screen, this option specifies the y offset from the upper-left corner of the TV screen (default: centered).</dl>
<h2>VIDEO OUTPUT DRIVERS (MPLAYER ONLY)</h2>
<p> Video output drivers are interfaces to different video output facilities. The syntax is:</p>
<dl>
<dt><code>-vo &lt;driver1[:suboption1[=value]:&#8230;],driver2,&#8230;[,]&gt;</code></p>
<dd> Specify a priority list of video output drivers to be used.</dl>
<p> If the list has a trailing &#8216;,&#8217; MPlayer will fall back on drivers not contained in the list. Suboptions are optional and can mostly be omitted.<br />
 <i>NOTE:</i> See -vo help for a list of compiled-in video output drivers. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-vo xmga,xv,</p>
<dd> Try the Matrox X11 driver, then the Xv driver, then others.</p>
<dt>-vo directx:noaccel</p>
<dd> Uses the DirectX driver with acceleration features turned off.</dl>
</dl>
<p> Available video output drivers are:</p>
<dl>
<dt><code>xv (X11 only)</code></p>
<dd> Uses the XVideo extension of XFree86 4.x to enable hardware accelerated playback. If you cannot use a hardware specific driver, this is probably the best option. For information about what colorkey is used and how it is drawn run MPlayer with -v option and look out for the lines tagged with [xv common] at the beginning.</p>
<dl>
<dt>
<dd>
<dl>
<dt>adaptor=&lt;number&gt;</p>
<dd> Select a specific XVideo adaptor (check xvinfo results).</p>
<dt>port=&lt;number&gt;</p>
<dd> Select a specific XVideo port.</p>
<dt>ck=&lt;cur|use|set&gt;</p>
<dd> Select the source from which the colorkey is taken (default: cur).</p>
<dl>
<dt>
<dd>
<dl>
<dt>cur</p>
<dd> The default takes the colorkey currently set in Xv.</p>
<dt>use</p>
<dd> Use but do not set the colorkey from MPlayer (use -colorkey option to change it).</p>
<dt>set</p>
<dd> Same as use but also sets the supplied colorkey.</dl>
</dl>
<dt>ck-method=&lt;man|bg|auto&gt;</p>
<dd> Sets the colorkey drawing method (default: man).</p>
<dl>
<dt>
<dd>
<dl>
<dt>man</p>
<dd> Draw the colorkey manually (reduces flicker in some cases).</p>
<dt>bg</p>
<dd> Set the colorkey as window background.</p>
<dt>auto</p>
<dd> Let Xv draw the colorkey.</dl>
</dl>
</dl>
</dl>
<dt><code>x11 (X11 only)</code></p>
<dd> Shared memory video output driver without hardware acceleration that works whenever X11 is present.</p>
<dt><code>xover (X11 only)</code></p>
<dd> Adds X11 support to all overlay based video output drivers. Currently only supported by tdfx_vid.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;vo_driver&gt;</p>
<dd> Select the driver to use as source to overlay on top of X11.</dl>
</dl>
<dt><code>vdpau (with -vc ffmpeg12vdpau, ffwmv3vdpau, ffvc1vdpau, ffh264vdpau or ffodivxvdpau)</code></p>
<dd> Video output that uses VDPAU to decode video via hardware. Also supports displaying of software-decoded video.</p>
<dl>
<dt>
<dd>
<dl>
<dt>sharpen=&lt;-1-1&gt;</p>
<dd> For positive values, apply a sharpening algorithm to the video, for negative values a blurring algorithm (default: 0).</p>
<dt>denoise=&lt;0-1&gt;</p>
<dd> Apply a noise reduction algorithm to the video (default: 0, no noise reduction).</p>
<dt>deint=&lt;0-4&gt;</p>
<dd> Select the deinterlacer (default: 0). All modes &gt; 0 respect -field-dominance.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> no deinterlacing</p>
<dt>1</p>
<dd> Show only first field, similar to -vf field.</p>
<dt>2</p>
<dd> Bob deinterlacing, similar to -vf tfields=1.</p>
<dt>3</p>
<dd> motion adaptive temporal deinterlacing May lead to A/V desync with slow video hardware and/or high resolution. This is the default if &quot;D&quot; is used to enable deinterlacing.</p>
<dt>4</p>
<dd> motion adaptive temporal deinterlacing with edge-guided spatial interpolation Needs fast video hardware.</dl>
</dl>
<dt>chroma-deint</p>
<dd> Makes temporal deinterlacers operate both on luma and chroma (default). Use nochroma-deint to solely use luma and speed up advanced deinterlacing. Useful with slow video memory.</p>
<dt>pullup</p>
<dd> Try to skip deinterlacing for progressive frames, useful for watching telecined content, needs fast video hardware for high resolutions. Only works with motion adaptive temporal deinterlacing.</p>
<dt>colorspace</p>
<dd> Select the color space for YUV to RGB conversion. In general BT.601 should be used for standard definition (SD) content and BT.709 for high definition (HD) content. Using incorrect color space results in slightly under or over saturated and shifted colors.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Guess the color space based on video resolution. Video with width &gt;= 1280 or height &gt; 576 is assumed to be HD and BT.709 color space will be used.</p>
<dt>1</p>
<dd> Use ITU-R BT.601 color space (default).</p>
<dt>2</p>
<dd> Use ITU-R BT.709 color space.</p>
<dt>3</p>
<dd> Use SMPTE-240M color space.</dl>
</dl>
<dt>hqscaling</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Use default VDPAU scaling (default).</p>
<dt>1-9</p>
<dd> Apply high quality VDPAU scaling (needs capable hardware).</dl>
</dl>
<dt>force-mixer</p>
<dd> Forces the use of the VDPAU mixer, which implements all above options (default). Use noforce-mixer to allow displaying BGRA colorspace. (Disables all above options and the hardware equalizer if image format BGRA is actually used.)</dl>
</dl>
<dt><code>xvmc (X11 with FFmpeg MPEG-1/2 decoder only)</code></p>
<dd> Video output driver that uses the XvMC (X Video Motion Compensation) extension of XFree86 4.x to speed up MPEG-1/2 and VCR2 decoding.</p>
<dl>
<dt>
<dd>
<dl>
<dt>adaptor=&lt;number&gt;</p>
<dd> Select a specific XVideo adaptor (check xvinfo results).</p>
<dt>port=&lt;number&gt;</p>
<dd> Select a specific XVideo port.</p>
<dt>(no)benchmark</p>
<dd> Disables image display. Necessary for proper benchmarking of drivers that change image buffers on monitor retrace only (nVidia). Default is not to disable image display (nobenchmark).</p>
<dt>(no)bobdeint</p>
<dd> Very simple deinterlacer. Might not look better than -vf tfields=1, but it is the only deinterlacer for xvmc (default: nobobdeint).</p>
<dt>(no)queue</p>
<dd> Queue frames for display to allow more parallel work of the video hardware. May add a small (not noticeable) constant A/V desync (default: noqueue).</p>
<dt>(no)sleep</p>
<dd> Use sleep function while waiting for rendering to finish (not recommended on Linux) (default: nosleep).</p>
<dt>ck=cur|use|set</p>
<dd> Same as -vo xv:ck (see -vo xv).</p>
<dt>ck-method=man|bg|auto</p>
<dd> Same as -vo xv:ck-method (see -vo xv).</dl>
</dl>
<dt><code>dga (X11 only)</code></p>
<dd> Play video through the XFree86 Direct Graphics Access extension. Considered obsolete.</p>
<dt><code>sdl (SDL only, buggy/outdated)</code></p>
<dd> Highly platform independent SDL (Simple Directmedia Layer) library video output driver. Since SDL uses its own X11 layer, MPlayer X11 options do not have any effect on SDL. Note that it has several minor bugs (-vm/-novm is mostly ignored, -fs behaves like -novm should, window is in top-left corner when returning from fullscreen, panscan is not supported, &#8230;).</p>
<dl>
<dt>
<dd>
<dl>
<dt>driver=&lt;driver&gt;</p>
<dd> Explicitly choose the SDL driver to use.</p>
<dt>(no)forcexv</p>
<dd> Use XVideo through the sdl video output driver (default: forcexv).</p>
<dt>(no)hwaccel</p>
<dd> Use hardware accelerated scaler (default: hwaccel).</dl>
</dl>
<dt><code>vidix&nbsp;<wbr>&nbsp;</code></p>
<dd> VIDIX (VIDeo Interface for *niX) is an interface to the video acceleration features of different graphics cards. Very fast video output driver on cards that support it.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;subdevice&gt;</p>
<dd> Explicitly choose the VIDIX subdevice driver to use. Available subdevice drivers are cyberblade, ivtv, mach64, mga_crtc2, mga, nvidia, pm2, pm3, radeon, rage128, s3, sh_veu, sis_vid and unichrome.</dl>
</dl>
<dt><code>xvidix (X11 only)</code></p>
<dd> X11 frontend for VIDIX</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;subdevice&gt;</p>
<dd> same as vidix</dl>
</dl>
<dt><code>cvidix&nbsp;</code></p>
<dd> Generic and platform independent VIDIX frontend, can even run in a text console with nVidia cards.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;subdevice&gt;</p>
<dd> same as vidix</dl>
</dl>
<dt><code>winvidix (Windows only)</code></p>
<dd> Windows frontend for VIDIX</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;subdevice&gt;</p>
<dd> same as vidix</dl>
</dl>
<dt><code>direct3d (Windows only) (BETA CODE!)</code></p>
<dd> Video output driver that uses the Direct3D interface (useful for Vista).</p>
<dt><code>directx (Windows only)</code></p>
<dd> Video output driver that uses the DirectX interface.</p>
<dl>
<dt>
<dd>
<dl>
<dt>noaccel</p>
<dd> Turns off hardware acceleration. Try this option if you have display problems.</dl>
</dl>
<dt><code>kva (OS/2 only)</code></p>
<dd> Video output driver that uses the libkva interface.</p>
<dl>
<dt>
<dd>
<dl>
<dt>snap</p>
<dd> Force SNAP mode.</p>
<dt>wo</p>
<dd> Force WarpOverlay! mode.</p>
<dt>dive</p>
<dd> Force DIVE mode.</p>
<dt>(no)t23</p>
<dd> Enable or disable workaround for T23 laptop (default: disabled). Try to enable this option if your video card supports upscaling only.</dl>
</dl>
<dt><code>quartz (Mac OS X only)</code></p>
<dd> Mac OS X Quartz video output driver. Under some circumstances, it might be more efficient to force a packed YUV output format, with e.g. -vf format=yuy2.</p>
<dl>
<dt>
<dd>
<dl>
<dt>device_id=&lt;number&gt;</p>
<dd> Choose the display device to use in fullscreen.</p>
<dt>fs_res=&lt;width&gt;:&lt;height&gt;</p>
<dd> Specify the fullscreen resolution (useful on slow systems).</dl>
</dl>
<dt><code>corevideo (Mac OS X 10.4 or 10.3.9 with QuickTime 7)</code></p>
<dd> Mac OS X CoreVideo video output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>device_id=&lt;number&gt;</p>
<dd> DEPRECATED, use -screen instead. Choose the display device to use for fullscreen or set it to -1 to always use the same screen the video window is on (default: -1 &#8211; auto).</p>
<dt>shared_buffer</p>
<dd> Write output to a shared memory buffer instead of displaying it and try to open an existing NSConnection for communication with a GUI.</p>
<dt>buffer_name=&lt;name&gt;</p>
<dd> Name of the shared buffer created with shm_open as well as the name of the NSConnection MPlayer will try to open (default: &quot;mplayerosx&quot;). Setting buffer_name implicitly enables shared_buffer.</dl>
</dl>
<dt><code>fbdev (Linux only)</code></p>
<dd> Uses the kernel framebuffer to play video.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the fbdev device name to use (e.g. /dev/:fb0) or the name of the VIDIX subdevice if the device name starts with &#8216;vidix&#8217; (e.g. &#8216;vidixsis_vid&#8217; for the sis driver).</dl>
</dl>
<dt><code>fbdev2 (Linux only)</code></p>
<dd> Uses the kernel framebuffer to play video, alternative implementation.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the fbdev device name to use (default: /dev/:fb0).</dl>
</dl>
<dt><code>vesa&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Very general video output driver that should work on any VESA VBE 2.0 compatible card.</p>
<dl>
<dt>
<dd>
<dl>
<dt>(no)dga</p>
<dd> Turns DGA mode on or off (default: on).</p>
<dt>neotv_pal</p>
<dd> Activate the NeoMagic TV out and set it to PAL norm.</p>
<dt>neotv_ntsc</p>
<dd> Activate the NeoMagic TV out and set it to NTSC norm.</p>
<dt>vidix</p>
<dd> Use the VIDIX driver.</p>
<dt>lvo:&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Activate the Linux Video Overlay on top of VESA mode.</dl>
</dl>
<dt><code>svga&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Play video using the SVGA library.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;video mode&gt;</p>
<dd> Specify video mode to use. The mode can be given in a &lt;width&gt;x&lt;height&gt;x&lt;colors&gt; format, e.g. 640x480x16M or be a graphics mode number, e.g. 84.</p>
<dt>bbosd</p>
<dd> Draw OSD into black bands below the movie (slower).</p>
<dt>native</p>
<dd> Use only native drawing functions. This avoids direct rendering, OSD and hardware acceleration.</p>
<dt>retrace</p>
<dd> Force frame switch on vertical retrace. Usable only with -double. It has the same effect as the -vsync option.</p>
<dt>sq&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Try to select a video mode with square pixels.</p>
<dt>vidix</p>
<dd> Use svga with VIDIX.</dl>
</dl>
<dt><code>gl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> OpenGL video output driver, simple version. Video size must be smaller than the maximum texture size of your OpenGL implementation. Intended to work even with the most basic OpenGL implementations, but also makes use of newer extensions, which allow support for more colorspaces and direct rendering. For optimal speed try adding the options<br />
 -dr -noslices<br />
 The code performs very few checks, so if a feature does not work, this might be because it is not supported by your card/OpenGL implementation even if you do not get any error message. Use glxinfo or a similar tool to display the supported OpenGL extensions.</p>
<dl>
<dt>
<dd>
<dl>
<dt>backend=&lt;n&gt;</p>
<dd> Select the backend/OpenGL implementation to use (default: -1).</p>
<dl>
<dt>
<dd> -1: Autoselect<br />
 0: Win32/WGL<br />
 1: X11/GLX<br />
 2: SDL<br />
 3: X11/EGL (highly experimental)<br />
 4: OSX/Cocoa<br />
 5: Android (very bad hack, only for testing)</dl>
<dt>(no)ati-hack</p>
<dd> ATI drivers may give a corrupted image when PBOs are used (when using -dr or force-pbo). This option fixes this, at the expense of using a bit more memory.</p>
<dt>(no)force-pbo</p>
<dd> Always uses PBOs to transfer textures even if this involves an extra copy. Currently this gives a little extra speed with NVidia drivers and a lot more speed with ATI drivers. May need -noslices and the ati-hack suboption to work correctly.</p>
<dt>(no)scaled-osd</p>
<dd> Changes the way the OSD behaves when the size of the window changes (default: disabled). When enabled behaves more like the other video output drivers, which is better for fixed-size fonts. Disabled looks much better with FreeType fonts and uses the borders in fullscreen mode. Does not work correctly with ass subtitles (see -ass), you can instead render them without OpenGL support via -vf ass.</p>
<dt>osdcolor=&lt;0xAARRGGBB&gt;</p>
<dd> Color for OSD (default: 0x00ffffff, corresponds to non-transparent white).</p>
<dt>rectangle=&lt;0,1,2&gt;</p>
<dd> Select usage of rectangular textures which saves video RAM, but often is slower (default: 0).</p>
<dl>
<dt>
<dd> 0: Use power-of-two textures (default).<br />
 1: Use the GL_ARB_texture_rectangle extension.<br />
 2: Use the GL_ARB_texture_non_power_of_two extension. In some cases only supported in software and thus very slow.</dl>
<dt>swapinterval=&lt;n&gt;</p>
<dd> Minimum interval between two buffer swaps, counted in displayed frames (default: 1). 1 is equivalent to enabling VSYNC, 0 to disabling VSYNC. Values below 0 will leave it at the system default. This limits the framerate to (horizontal refresh rate / n). Requires GLX_SGI_swap_control support to work. With some (most/all?) implementations this only works in fullscreen mode.</p>
<dt>ycbcr</p>
<dd> Use the GL_APPLE_ycbcr_422 extension to convert YUV to RGB. Default is disabled if yuv= is specified, auto-detected otherwise. Note that this will enable a few special settings to get into a special driver fast-path.</p>
<dt>yuv=&lt;n&gt;</p>
<dd> Select the type of YUV to RGB conversion. The default is auto-detection deciding between values 0 and 2.</p>
<dl>
<dt>
<dd> 0: Use software conversion. Compatible with all OpenGL versions. Provides brightness, contrast and saturation control.<br />
 1: Use register combiners. This uses an nVidia-specific extension (GL_NV_register_combiners). At least three texture units are needed. Provides saturation and hue control. This method is fast but inexact.<br />
 2: Use a fragment program using the POW instruction. Needs the GL_ARB_fragment_program extension and at least three texture units. Provides brightness, contrast, saturation, hue and gamma control. Gamma can also be set independently for red, green and blue. Method 4 is usually faster.<br />
 3: Same as 2. They exist as distinct values for legacy reasons, MPlayer now inserts the extra instructions for gamma control on-demand.<br />
 4: Use a fragment program with additional lookup. Needs the GL_ARB_fragment_program extension and at least four texture units. Provides brightness, contrast, saturation, hue and gamma control. Gamma can also be set independently for red, green and blue.<br />
 5: Use ATI-specific method (for older cards). This uses an ATI-specific extension (GL_ATI_fragment_shader &#8211; not GL_ARB_fragment_shader!). At least three texture units are needed. Provides saturation and hue control. This method is fast but inexact.<br />
 6: Use a 3D texture to do conversion via lookup. Needs the GL_ARB_fragment_program extension and at least four texture units. Extremely slow (software emulation) on some (all?) ATI cards since it uses a texture with border pixels. Provides brightness, contrast, saturation, hue and gamma control. Gamma can also be set independently for red, green and blue. Speed depends more on GPU memory bandwidth than other methods.</dl>
<dt>colorspace</p>
<dd> Select the color space for YUV to RGB conversion.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Use the formula used normally by MPlayer (default).</p>
<dt>1</p>
<dd> Use ITU-R BT.601 color space.</p>
<dt>2</p>
<dd> Use ITU-R BT.709 color space.</p>
<dt>3</p>
<dd> Use SMPTE-240M color space.</dl>
</dl>
<dt>levelconv=&lt;n&gt;</p>
<dd> Select the brightness level conversion to use for the YUV to RGB conversion</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Convert TV to PC levels (default).</p>
<dt>1</p>
<dd> Convert PC to TV levels.</p>
<dt>2</p>
<dd> Do not do any conversion.</dl>
</dl>
<dt>lscale=&lt;n&gt;</p>
<dd> Select the scaling function to use for luminance scaling. Only valid for yuv modes 2, 3, 4 and 6.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Use simple linear filtering (default).</p>
<dt>1</p>
<dd> Use bicubic B-spline filtering (better quality). Needs one additional texture unit. Older cards will not be able to handle this for chroma at least in fullscreen mode.</p>
<dt>2</p>
<dd> Use cubic filtering in horizontal, linear filtering in vertical direction. Works on a few more cards than method 1.</p>
<dt>3</p>
<dd> Same as 1 but does not use a lookup texture. Might be faster on some cards.</p>
<dt>4</p>
<dd> Use experimental unsharp masking with 3&#215;3 support and a default strength of 0.5 (see filter-strength).</p>
<dt>5</p>
<dd> Use experimental unsharp masking with 5&#215;5 support and a default strength of 0.5 (see filter-strength).</p>
<dt>64</p>
<dd> Use nearest-neighbor scaling.</dl>
</dl>
<dt>cscale=&lt;n&gt;</p>
<dd> Select the scaling function to use for chrominance scaling. For details see lscale.</p>
<dt>filter-strength=&lt;value&gt;</p>
<dd> Set the effect strength for the lscale/cscale filters that support it.</p>
<dt>noise-strength=&lt;value&gt;</p>
<dd> Set how much noise to add. 0 to disable (default), 1.0 for level suitable for dithering to 6 bit.</p>
<dt>stereo=&lt;value&gt;</p>
<dd> Select a method for stereo display. You may have to use -aspect to fix the aspect value. Add 32 to swap left and right side. Experimental, do not expect too much from it.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> normal 2D display</p>
<dt>1</p>
<dd> Convert side by side input to full-color red-cyan stereo.</p>
<dt>2</p>
<dd> Convert side by side input to full-color green-magenta stereo.</p>
<dt>3</p>
<dd> Convert side by side input to quadbuffered stereo. Only supported by very few OpenGL cards.</p>
<dt>4</p>
<dd> Mix left and right in a pixel pattern. Pattern is given by stipple option.</dl>
</dl>
<dt>stipple=&lt;bit</p>
<dd> Lowest 16 bit give the 4&#215;4 pattern to use (default: 0x0f0f). Examples to try: 0x0f0f, 0xf0f0: horizontal lines; 0xaaaa, 0x5555: vertical lines; 0xa5a5, 0x5a5a: checkerboard pattern</dl>
</dl>
<dl>
<dt>
<dd> The following options are only useful if writing your own fragment programs.</dl>
<dl>
<dt>
<dd>
<dl>
<dt>customprog=&lt;filename&gt;</p>
<dd> Load a custom fragment program from &lt;filename&gt;. See TOOLS/edgedect.fp for an example.</p>
<dt>customtex=&lt;filename&gt;</p>
<dd> Load a custom &quot;gamma ramp&quot; texture from &lt;filename&gt;. This can be used in combination with yuv=4 or with the customprog option.</p>
<dt>(no)customtlin</p>
<dd> If enabled (default) use GL_LINEAR interpolation, otherwise use GL_NEAREST for customtex texture.</p>
<dt>(no)customtrect</p>
<dd> If enabled, use texture_rectangle for customtex texture. Default is disabled.</p>
<dt>(no)mipmapgen</p>
<dd> If enabled, mipmaps for the video are automatically generated. This should be useful together with the customprog and the TXB instruction to implement blur filters with a large radius. For most OpenGL implementations this is very slow for any non-RGB formats. Default is disabled.</dl>
</dl>
<dl>
<dt>
<dd> Normally there is no reason to use the following options, they mostly exist for testing purposes.</dl>
<dl>
<dt>
<dd>
<dl>
<dt>(no)glfinish</p>
<dd> Call glFinish() before swapping buffers. Slower but in some cases more correct output (default: disabled).</p>
<dt>(no)manyfmts</p>
<dd> Enables support for more (RGB and BGR) color formats (default: enabled). Needs OpenGL version &gt;= 1.2.</p>
<dt>slice-height=&lt;0-&#8230;&gt;</p>
<dd> Number of lines copied to texture in one piece (default: 0). 0 for whole image.<br />
 <i>NOTE:</i> If YUV colorspace is used (see yuv suboption), special rules apply:</p>
<dl>
<dt>
<dd> If the decoder uses slice rendering (see -noslices), this setting has no effect, the size of the slices as provided by the decoder is used.<br />
 If the decoder does not use slice rendering, the default is 16.</dl>
<dt>(no)osd</p>
<dd> Enable or disable support for OSD rendering via OpenGL (default: enabled). This option is for testing; to disable the OSD use -osdlevel 0 instead.</p>
<dt>(no)aspect</p>
<dd> Enable or disable aspect scaling and pan-and-scan support (default: enabled). Disabling might increase speed.</dl>
</dl>
<dt><code>gl_tiled</code></p>
<dd> Variant of the OpenGL video output driver. Supports videos larger than the maximum texture size but lacks many of the advanced features and optimizations of the gl driver and is unlikely to be extended further.</p>
<dl>
<dt>
<dd>
<dl>
<dt>(no)glfinish</p>
<dd> same as gl (default: enabled)</p>
<dt>yuv=&lt;n&gt;</p>
<dd> Select the type of YUV to RGB conversion. If set to anything except 0 OSD will be disabled and brightness, contrast and gamma setting is only available via the global X server settings. Apart from this the values have the same meaning as for -vo gl.</dl>
</dl>
<dt><code>matrixview</code></p>
<dd> OpenGL-based renderer creating a Matrix-like running-text effect.</p>
<dl>
<dt>
<dd>
<dl>
<dt>cols=&lt;n&gt;</p>
<dd> Number of text columns to display. Very low values (&lt; 16) will probably fail due to scaler limitations. Values not divisible by 16 may cause issues as well.</p>
<dt>rows=&lt;n&gt;</p>
<dd> Number of text rows to display. Very low values (&lt; 16) will probably fail due to scaler limitations. Values not divisible by 16 may cause issues as well.</dl>
</dl>
<dt><code>null&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Produces no video output. Useful for benchmarking.</p>
<dt><code>aa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> ASCII art video output driver that works on a text console.<br />
 <i>NOTE:</i> The driver does not handle -aspect correctly.<br />
 <i>HINT:</i> You probably have to specify -monitorpixelaspect. Try &#8216;mplayer -vo aa -monitorpixelaspect 0.5&#8217;.</p>
<dt><code>caca&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Color ASCII art video output driver that works on a text console.</p>
<dt><code>bl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Video playback using the Blinkenlights UDP protocol. This driver is highly hardware specific.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;subdevice&gt;</p>
<dd> Explicitly choose the Blinkenlights subdevice driver to use. It is something like arcade:host=localhost:2323 or hdl:file=name1,file=name2. You must specify a subdevice.</dl>
</dl>
<dt><code>ggi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> GGI graphics system video output driver</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;driver&gt;</p>
<dd> Explicitly choose the GGI driver to use. Replace any &#8216;,&#8217; that would appear in the driver string by a &#8216;.&#8217;.</dl>
</dl>
<dt><code>directfb</code></p>
<dd> Play video using the DirectFB library.</p>
<dl>
<dt>
<dd>
<dl>
<dt>(no)input</p>
<dd> Use the DirectFB instead of the MPlayer keyboard code (default: enabled).</p>
<dt>buffermode=single|double|triple</p>
<dd> Double and triple buffering give best results if you want to avoid tearing issues. Triple buffering is more efficient than double buffering as it does not block MPlayer while waiting for the vertical retrace. Single buffering should be avoided (default: single).</p>
<dt>fieldparity=top|bottom</p>
<dd> Control the output order for interlaced frames (default: disabled). Valid values are top = top fields first, bottom = bottom fields first. This option does not have any effect on progressive film material like most MPEG movies are. You need to enable this option if you have tearing issues or unsmooth motions watching interlaced film material.</p>
<dt>layer=N</p>
<dd> Will force layer with ID N for playback (default: -1 &#8211; auto).</p>
<dt>dfbopts=&lt;list&gt;</p>
<dd> Specify a parameter list for DirectFB.</dl>
</dl>
<dt><code>dfbmga&nbsp;</code></p>
<dd> Matrox G400/:G450/:G550 specific video output driver that uses the DirectFB library to make use of special hardware features. Enables CRTC2 (second head), displaying video independently of the first head.</p>
<dl>
<dt>
<dd>
<dl>
<dt>(no)input</p>
<dd> same as directfb (default: disabled)</p>
<dt>buffermode=single|double|triple</p>
<dd> same as directfb (default: triple)</p>
<dt>fieldparity=top|bottom</p>
<dd> same as directfb</p>
<dt>(no)bes</p>
<dd> Enable the use of the Matrox BES (backend scaler) (default: disabled). Gives very good results concerning speed and output quality as interpolated picture processing is done in hardware. Works only on the primary head.</p>
<dt>(no)spic</p>
<dd> Make use of the Matrox sub picture layer to display the OSD (default: enabled).</p>
<dt>(no)crtc2</p>
<dd> Turn on TV-out on the second head (default: enabled). The output quality is amazing as it is a full interlaced picture with proper sync to every odd/:even field.</p>
<dt>tvnorm=pal|ntsc|auto</p>
<dd> Will set the TV norm of the Matrox card without the need for modifying /etc/:directfbrc (default: disabled). Valid norms are pal = PAL, ntsc = NTSC. Special norm is auto (auto-adjust using PAL/:NTSC) because it decides which norm to use by looking at the framerate of the movie.</dl>
</dl>
<dt><code>mga (Linux only)</code></p>
<dd> Matrox specific video output driver that makes use of the YUV back end scaler on Gxxx cards through a kernel module. If you have a Matrox card, this is the fastest option.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the Matrox device name to use (default: /dev/:mga_vid).</dl>
</dl>
<dt><code>xmga (Linux, X11 only)</code></p>
<dd> The mga video output driver, running in an X11 window.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the Matrox device name to use (default: /dev/:mga_vid).</dl>
</dl>
<dt><code>s3fb (Linux only) (also see -dr)</code></p>
<dd> S3 Virge specific video output driver. This driver supports the card&#8217;s YUV conversion and scaling, double buffering and direct rendering features. Use -vf format=yuy2 to get hardware-accelerated YUY2 rendering, which is much faster than YV12 on this card.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the fbdev device name to use (default: /dev/:fb0).</dl>
</dl>
<dt><code>wii (Linux only)</code></p>
<dd> Nintendo Wii/GameCube specific video output driver.</p>
<dt><code>3dfx (Linux only)</code></p>
<dd> 3dfx-specific video output driver that directly uses the hardware on top of X11. Only 16 bpp are supported.</p>
<dt><code>tdfxfb (Linux only)</code></p>
<dd> This driver employs the tdfxfb framebuffer driver to play movies with YUV acceleration on 3dfx cards.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the fbdev device name to use (default: /dev/:fb0).</dl>
</dl>
<dt><code>tdfx_vid (Linux only)</code></p>
<dd> 3dfx-specific video output driver that works in combination with the tdfx_vid kernel module.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the device name to use (default: /dev/:tdfx_vid).</dl>
</dl>
<dt><code>dxr2 (also see -dxr2) (DXR2 only)</code></p>
<dd> Creative DXR2 specific video output driver.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;vo_driver&gt;</p>
<dd> Output video subdriver to use as overlay (x11, xv).</dl>
</dl>
<dt><code>dxr3 (DXR3 only)</code></p>
<dd> Sigma Designs em8300 MPEG decoder chip (Creative DXR3, Sigma Designs Hollywood Plus) specific video output driver. Also see the lavc video filter.</p>
<dl>
<dt>
<dd>
<dl>
<dt>overlay</p>
<dd> Activates the overlay instead of TV-out.</p>
<dt>prebuf</p>
<dd> Turns on prebuffering.</p>
<dt>sync&nbsp;</p>
<dd> Will turn on the new sync-engine.</p>
<dt>norm=&lt;norm&gt;</p>
<dd> Specifies the TV norm.</p>
<dl>
<dt>
<dd> 0: Does not change current norm (default).<br />
 1: Auto-adjust using PAL/:NTSC.<br />
 2: Auto-adjust using PAL/:PAL-60.<br />
 3: PAL<br />
 4: PAL-60<br />
 5: NTSC</dl>
<dt>&lt;0-3&gt;</p>
<dd> Specifies the device number to use if you have more than one em8300 card.</dl>
</dl>
<dt><code>ivtv (IVTV only)</code></p>
<dd> Conexant CX23415 (iCompression iTVC15) or Conexant CX23416 (iCompression iTVC16) MPEG decoder chip (Hauppauge WinTV PVR-150/250/350/500) specific video output driver for TV-out. Also see the lavc video filter.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the MPEG decoder device name to use (default: /dev/video16).</p>
<dt>&lt;output&gt;</p>
<dd> Explicitly choose the TV-out output to be used for the video signal.</dl>
</dl>
<dt><code>v4l2 (requires Linux 2.6.22+ kernel)</code></p>
<dd> Video output driver for V4L2 compliant cards with built-in hardware MPEG decoder. Also see the lavc video filter.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;device&gt;</p>
<dd> Explicitly choose the MPEG decoder device name to use (default: /dev/video16).</p>
<dt>&lt;output&gt;</p>
<dd> Explicitly choose the TV-out output to be used for the video signal.</dl>
</dl>
<dt><code>mpegpes (DVB only)</code></p>
<dd> Video output driver for DVB cards that writes the output to an MPEG-PES file if no DVB card is installed.</p>
<dl>
<dt>
<dd>
<dl>
<dt>card=&lt;1-4&gt;</p>
<dd> Specifies the device number to use if you have more than one DVB output card (V3 API only, such as 1.x.y series drivers). If not specified MPlayer will search the first usable card.</p>
<dt>&lt;filename&gt;</p>
<dd> output filename (default: ./grab.mpg)</dl>
</dl>
<dt><code>zr (also see -zr* and -zrhelp)</code></p>
<dd> Video output driver for a number of MJPEG capture/:playback cards.</p>
<dt><code>zr2 (also see the zrmjpeg video filter)</code></p>
<dd> Video output driver for a number of MJPEG capture/:playback cards, second generation.</p>
<dl>
<dt>
<dd>
<dl>
<dt>dev=&lt;device&gt;</p>
<dd> Specifies the video device to use.</p>
<dt>norm=&lt;PAL|NTSC|SECAM|auto&gt;</p>
<dd> Specifies the video norm to use (default: auto).</p>
<dt>(no)prebuf</p>
<dd> (De)Activate prebuffering, not yet supported.</dl>
</dl>
<dt><code>md5sum&nbsp;</code></p>
<dd> Calculate MD5 sums of each frame and write them to a file. Supports RGB24 and YV12 colorspaces. Useful for debugging.</p>
<dl>
<dt>
<dd>
<dl>
<dt>outfile=&lt;value&gt;</p>
<dd> Specify the output filename (default: ./md5sums).</dl>
</dl>
<dt><code>yuv4mpeg</code></p>
<dd> Transforms the video stream into a sequence of uncompressed YUV 4:2:0 images and stores it in a file (default: ./stream.yuv). The format is the same as the one employed by mjpegtools, so this is useful if you want to process the video with the mjpegtools suite. It supports the YV12 format. If your source file has a different format and is interlaced, make sure to use -vf scale=::1 to ensure the conversion uses interlaced mode. You can combine it with the -fixed-vo option to concatenate files with the same dimensions and fps value.</p>
<dl>
<dt>
<dd>
<dl>
<dt>interlaced</p>
<dd> Write the output as interlaced frames, top field first.</p>
<dt>interlaced_bf</p>
<dd> Write the output as interlaced frames, bottom field first.</p>
<dt>file=&lt;filename&gt;</p>
<dd> Write the output to &lt;filename&gt; instead of the default stream.yuv.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>NOTE:</i> If you do not specify any option the output is progressive (i.e. not interlaced).</dl>
<dt><code>gif89a&nbsp;</code></p>
<dd> Output each frame into a single animated GIF file in the current directory. It supports only RGB format with 24 bpp and the output is converted to 256 colors.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;fps&gt;</p>
<dd> Float value to specify framerate (default: 5.0).</p>
<dt>&lt;output&gt;</p>
<dd> Specify the output filename (default: ./out.gif).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>NOTE:</i> You must specify the framerate before the filename or the framerate will be part of the filename. </p>
<p> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd> mplayer video.nut -vo gif89a:fps=15:output=test.gif</dl>
<dt><code>jpeg&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Output each frame into a JPEG file in the current directory. Each file takes the frame number padded with leading zeros as name.</p>
<dl>
<dt>
<dd>
<dl>
<dt>[no]progressive</p>
<dd> Specify standard or progressive JPEG (default: noprogressive).</p>
<dt>[no]baseline</p>
<dd> Specify use of baseline or not (default: baseline).</p>
<dt>optimize=&lt;0-100&gt;</p>
<dd> optimization factor (default: 100)</p>
<dt>smooth=&lt;0-100&gt;</p>
<dd> smooth factor (default: 0)</p>
<dt>quality=&lt;0-100&gt;</p>
<dd> quality factor (default: 75)</p>
<dt>outdir=&lt;dirname&gt;</p>
<dd> Specify the directory to save the JPEG files to (default: ./).</p>
<dt>subdirs=&lt;prefix&gt;</p>
<dd> Create numbered subdirectories with the specified prefix to save the files in instead of the current directory.</p>
<dt>maxfiles=&lt;value&gt; (subdirs only)</p>
<dd> Maximum number of files to be saved per subdirectory. Must be equal to or larger than 1 (default: 1000).</dl>
</dl>
<dt><code>pnm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Output each frame into a PNM file in the current directory. Each file takes the frame number padded with leading zeros as name. It supports PPM, PGM and PGMYUV files in both raw and ASCII mode. Also see <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/5-ppm/">ppm</a>(5) and <a href="/docs/linux/man/5-pgm/">pgm</a>(5).</p>
<dl>
<dt>
<dd>
<dl>
<dt>ppm&nbsp;<wbr>&nbsp;</p>
<dd> Write PPM files (default).</p>
<dt>pgm&nbsp;<wbr>&nbsp;</p>
<dd> Write PGM files.</p>
<dt>pgmyuv</p>
<dd> Write PGMYUV files. PGMYUV is like PGM, but it also contains the U and V plane, appended at the bottom of the picture.</p>
<dt>raw&nbsp;<wbr>&nbsp;</p>
<dd> Write PNM files in raw mode (default).</p>
<dt>ascii</p>
<dd> Write PNM files in ASCII mode.</p>
<dt>outdir=&lt;dirname&gt;</p>
<dd> Specify the directory to save the PNM files to (default: ./).</p>
<dt>subdirs=&lt;prefix&gt;</p>
<dd> Create numbered subdirectories with the specified prefix to save the files in instead of the current directory.</p>
<dt>maxfiles=&lt;value&gt; (subdirs only)</p>
<dd> Maximum number of files to be saved per subdirectory. Must be equal to or larger than 1 (default: 1000).</dl>
</dl>
<dt><code>png&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Output each frame into a PNG file in the current directory. Each file takes the frame number padded with leading zeros as name. 24bpp RGB and BGR formats are supported.</p>
<dl>
<dt>
<dd>
<dl>
<dt>z=&lt;0-9&gt;</p>
<dd> Specifies the compression level. 0 is no compression, 9 is maximum compression.</p>
<dt>outdir=&lt;dirname&gt;</p>
<dd> Specify the directory to save the PNG files to (default: ./).</p>
<dt>prefix=&lt;prefix&gt;</p>
<dd> Specify the prefix to be used for the PNG filenames (default: no prefix).</p>
<dt>alpha</p>
<dd> Create PNG files with an alpha channel. Note that MPlayer in general does not support alpha, so this will only be useful in some rare cases.</dl>
</dl>
<dt><code>mng&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Output video into an animated MNG file using 24 bpp RGB images with lossless compression.</p>
<dl>
<dt>
<dd>
<dl>
<dt>output=&lt;filename&gt;</p>
<dd> Specify the output filename (default: out.mng).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd> mplayer video.mkv -vo mng:output=test.mng</dl>
<dt><code>tga&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Output each frame into a Targa file in the current directory. Each file takes the frame number padded with leading zeros as name. The purpose of this video output driver is to have a simple lossless image writer to use without any external library. It supports the BGR[A] color format, with 15, 24 and 32 bpp. You can force a particular format with the format video filter. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> mplayer video.nut -vf format=bgr15 -vo tga</dl>
</dl>
<h2>DECODING/FILTERING OPTIONS</h2>
<dl>
<dt><code>-ac &lt;[-|+]codec1,[-|+]codec2,&#8230;[,]&gt;</code></p>
<dd> Specify a priority list of audio codecs to be used, according to their codec name in codecs.conf. Use a &#8216;-&#8216; before the codec name to omit it. Use a &#8216;+&#8217; before the codec name to force it, this will likely crash! If the list has a trailing &#8216;,&#8217; MPlayer will fall back on codecs not contained in the list.<br />
 <i>NOTE:</i> See -ac help for a full list of available codecs. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-ac mp3acm</p>
<dd> Force the l3codeca.acm MP3 codec.</p>
<dt>-ac mad,</p>
<dd> Try libmad first, then fall back on others.</p>
<dt>-ac hwac3,a52,</p>
<dd> Try hardware AC-3 passthrough, software AC-3, then others.</p>
<dt>-ac hwdts,</p>
<dd> Try hardware DTS passthrough, then fall back on others.</p>
<dt>-ac -ffmp3,</p>
<dd> Skip FFmpeg&#8217;s MP3 decoder.</dl>
</dl>
<dt><code>-af-adv &lt;force=(0-7):list=(filters)&gt; (also see -af)</code></p>
<dd> Specify advanced audio filter options:</p>
<dl>
<dt>
<dd>
<dl>
<dt>force=&lt;0-7&gt;</p>
<dd> Forces the insertion of audio filters to one of the following:</p>
<dl>
<dt>
<dd> 0: Use completely automatic filter insertion (currently identical to 1).<br />
 1: Optimize for accuracy (default).<br />
 2: Optimize for speed. <i>Warning:</i> Some features in the audio filters may silently fail, and the sound quality may drop.<br />
 3: Use no automatic insertion of filters and no optimization. <i>Warning:</i> It may be possible to crash MPlayer using this setting.<br />
 4: Use automatic insertion of filters according to 0 above, but use floating point processing when possible.<br />
 5: Use automatic insertion of filters according to 1 above, but use floating point processing when possible.<br />
 6: Use automatic insertion of filters according to 2 above, but use floating point processing when possible.<br />
 7: Use no automatic insertion of filters according to 3 above, and use floating point processing when possible.</dl>
<dt>list=&lt;filters&gt;</p>
<dd> Same as -af.</dl>
</dl>
<dt><code>-afm &lt;driver1,driver2,&#8230;&gt;</code></p>
<dd> Specify a priority list of audio codec families to be used, according to their codec name in codecs.conf. Falls back on the default codecs if none of the given codec families work.<br />
 <i>NOTE:</i> See -afm help for a full list of available codec families. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-afm ffmpeg</p>
<dd> Try FFmpeg&#8217;s libavcodec codecs first.</p>
<dt>-afm acm,dshow</p>
<dd> Try Win32 codecs first.</dl>
</dl>
<dt><code>-aspect &lt;ratio&gt; (also see -zoom)</code></p>
<dd> Override movie aspect ratio, in case aspect information is incorrect or missing in the file being played. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -aspect 4:3 or -aspect 1.3333<br />
 -aspect 16:9 or -aspect 1.7777</dl>
<dt><code>-noaspect</code></p>
<dd> Disable automatic movie aspect ratio compensation.</p>
<dt><code>-field-dominance &lt;-1-1&gt;</code></p>
<dd> Set first field for interlaced content. Useful for deinterlacers that double the framerate: -vf tfields=1, -vf yadif=1, -vo vdpau:deint and -vo xvmc:bobdeint.</p>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> auto (default): If the decoder does not export the appropriate information, it falls back to 0 (top field first).</p>
<dt>0</p>
<dd> top field first</p>
<dt>1</p>
<dd> bottom field first</dl>
</dl>
<dt><code>-flip &nbsp;</code></p>
<dd> Flip image upside-down.</p>
<dt><code>-lavdopts &lt;option1:option2:&#8230;&gt; (DEBUG CODE)</code></p>
<dd> Specify libavcodec decoding parameters. Separate multiple options with a colon. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -lavdopts gray:skiploopfilter=all:skipframe=nonref</dl>
<dl>
<dt>
<dd> Available options are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>bitexact</p>
<dd> Only use bit-exact algorithms in all decoding steps (for codec testing).</p>
<dt>bug=&lt;value&gt;</p>
<dd> Manually work around encoder bugs.</p>
<dl>
<dt>
<dd> 0: nothing<br />
 1: autodetect bugs (default)<br />
 2 (msmpeg4v3): some old lavc generated msmpeg4v3 files (no autodetection)<br />
 4 (mpeg4): Xvid interlacing bug (autodetected if fourcc==XVIX)<br />
 8 (mpeg4): UMP4 (autodetected if fourcc==UMP4)<br />
 16 (mpeg4): padding bug (autodetected)<br />
 32 (mpeg4): illegal vlc bug (autodetected per fourcc)<br />
 64 (mpeg4): Xvid and DivX qpel bug (autodetected per fourcc/:version)<br />
 128 (mpeg4): old standard qpel (autodetected per fourcc/:version)<br />
 256 (mpeg4): another qpel bug (autodetected per fourcc/:version)<br />
 512 (mpeg4): direct-qpel-blocksize bug (autodetected per fourcc/:version)<br />
 1024 (mpeg4): edge padding bug (autodetected per fourcc/:version)</dl>
<dt>debug=&lt;value&gt;</p>
<dd> Display debugging information.</p>
<dl>
<dt>
<dd>
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
 0x4000: Visualize block types.</dl>
<dt>ec=&lt;value&gt;</p>
<dd> Set error concealment strategy.</p>
<dl>
<dt>
<dd> 1: Use strong deblock filter for damaged MBs.<br />
 2: iterative motion vector (MV) search (slow)<br />
 3: all (default)</dl>
<dt>er=&lt;value&gt;</p>
<dd> Set error resilience strategy.</p>
<dl>
<dt>
<dd>
 0: disabled<br />
 1: careful (Should work with broken encoders.)<br />
 2: normal (default) (Works with compliant encoders.)<br />
 3: aggressive (More checks, but might cause problems even for valid bitstreams.)<br />
 4: very aggressive</dl>
<dt>fast (MPEG-2, MPEG-4, and H.264 only)</p>
<dd> Enable optimizations which do not comply to the specification and might potentially cause problems, like simpler dequantization, simpler motion compensation, assuming use of the default quantization matrix, assuming YUV 4:2:0 and skipping a few checks to detect damaged bitstreams.</p>
<dt>gray&nbsp;</p>
<dd> grayscale only decoding (a bit faster than with color)</p>
<dt>idct=&lt;0-99&gt; (see -lavcopts)</p>
<dd> For best decoding quality use the same IDCT algorithm for decoding and encoding. This may come at a price in accuracy, though.</p>
<dt>lowres=&lt;number&gt;[,&lt;w&gt;]</p>
<dd> Decode at lower resolutions. Low resolution decoding is not supported by all codecs, and it will often result in ugly artifacts. This is not a bug, but a side effect of not decoding at full resolution.</p>
<dl>
<dt>
<dd>
 0: disabled<br />
 1: 1/2 resolution<br />
 2: 1/4 resolution<br />
 3: 1/8 resolution</dl>
<dl>
<dt>
<dd> If &lt;w&gt; is specified lowres decoding will be used only if the width of the video is major than or equal to &lt;w&gt;.</dl>
<p> <code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code> Pass AVOptions to libavcodec decoder. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some options may conflict with MEncoder options. </p>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>o=debug=pict</p>
<dd></dl>
</dl>
<dt>sb=&lt;number&gt; (MPEG-2 only)</p>
<dd> Skip the given number of macroblock rows at the bottom.</p>
<dt>st=&lt;number&gt; (MPEG-2 only)</p>
<dd> Skip the given number of macroblock rows at the top.</p>
<dt>skiploopfilter=&lt;skipvalue&gt; (H.264 only)</p>
<dd> Skips the loop filter (AKA deblocking) during H.264 decoding. Since the filtered frame is supposed to be used as reference for decoding dependent frames this has a worse effect on quality than not doing deblocking on e.g. MPEG-2 video. But at least for high bitrate HDTV this provides a big speedup with no visible quality loss. </p>
<p> &lt;skipvalue&gt; can be either one of the following:</p>
<dl>
<dt>
<dd>
 none: Never skip.<br />
 default: Skip useless processing steps (e.g. 0 size packets in AVI).<br />
 nonref: Skip frames that are not referenced (i.e. not used for decoding other frames, the error cannot &quot;build up&quot;).<br />
 bidir: Skip B-Frames.<br />
 nonkey: Skip all frames except keyframes.<br />
 all: Skip all frames.</dl>
<dt>skipidct=&lt;skipvalue&gt; (MPEG-1/2 only)</p>
<dd> Skips the IDCT step. This degrades quality a lot of in almost all cases (see skiploopfilter for available skip values).</p>
<dt>skipframe=&lt;skipvalue&gt;</p>
<dd> Skips decoding of frames completely. Big speedup, but jerky motion and sometimes bad artifacts (see skiploopfilter for available skip values).</p>
<dt>threads=&lt;1-8&gt; (MPEG-1/2 and H.264 only)</p>
<dd> number of threads to use for decoding (default: 1)</p>
<dt>vismv=&lt;value&gt;</p>
<dd> Visualize motion vectors.</p>
<dl>
<dt>
<dd>
 0: disabled<br />
 1: Visualize forward predicted MVs of P-frames.<br />
 2: Visualize forward predicted MVs of B-frames.<br />
 4: Visualize backward predicted MVs of B-frames.</dl>
<dt>vstats</p>
<dd> Prints some statistics and stores them in ./vstats_*.log.</p>
<dt>wait_keyframe</p>
<dd> Wait for a keyframe before displaying anything. Avoids broken frames at startup or after seeking with some formats.</dl>
</dl>
<dt><code>-noslices</code></p>
<dd> Disable drawing video by 16-pixel height slices/:bands, instead draws the whole frame in a single run. May be faster or slower, depending on video card and available cache. It has effect only with libmpeg2 and libavcodec codecs.</p>
<dt><code>-nosound</code></p>
<dd> Do not play/:encode sound. Useful for benchmarking.</p>
<dt><code>-novideo</code></p>
<dd> Do not play/:encode video. In many cases this will not work, use -vc null -vo null instead.</p>
<dt><code>-pp &lt;quality&gt; (also see -vf pp)</code></p>
<dd> Set the DLL postprocess level. This option is no longer usable with -vf pp. It only works with Win32 DirectShow DLLs with internal postprocessing routines. The valid range of -pp values varies by codec, it is mostly 0-6, where 0=disable, 6=slowest/:best.</p>
<dt><code>-pphelp (also see -vf pp)</code></p>
<dd> Show a summary about the available postprocess filters and their usage.</p>
<dt><code>-ssf &lt;mode&gt;</code></p>
<dd> Specifies software scaler parameters. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd> -vf scale -ssf lgb=3.0</dl>
<dl>
<dt>
<dd>
<dl>
<dt>lgb=&lt;0-100&gt;</p>
<dd> gaussian blur filter (luma)</p>
<dt>cgb=&lt;0-100&gt;</p>
<dd> gaussian blur filter (chroma)</p>
<dt>ls=&lt;-100-100&gt;</p>
<dd> sharpen filter (luma)</p>
<dt>cs=&lt;-100-100&gt;</p>
<dd> sharpen filter (chroma)</p>
<dt>chs=&lt;h&gt;</p>
<dd> chroma horizontal shifting</p>
<dt>cvs=&lt;v&gt;</p>
<dd> chroma vertical shifting</dl>
</dl>
<dt><code>-stereo &lt;mode&gt;</code></p>
<dd> Select type of MP2/:MP3 stereo output.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> stereo</p>
<dt>1</p>
<dd> left channel</p>
<dt>2</p>
<dd> right channel</dl>
</dl>
<dt><code>-sws &lt;software scaler type&gt; (also see -vf scale and -zoom)</code></p>
<dd> Specify the software scaler algorithm to be used with the -zoom option. This affects video output drivers which lack hardware acceleration, e.g. x11. </p>
<p> Available types are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> fast bilinear</p>
<dt>1</p>
<dd> bilinear</p>
<dt>2</p>
<dd> bicubic (good quality) (default)</p>
<dt>3</p>
<dd> experimental</p>
<dt>4</p>
<dd> nearest neighbor (bad quality)</p>
<dt>5</p>
<dd> area</p>
<dt>6</p>
<dd> luma bicubic / chroma bilinear</p>
<dt>7</p>
<dd> gauss</p>
<dt>8</p>
<dd> sincR</p>
<dt>9</p>
<dd> lanczos</p>
<dt>10</p>
<dd> natural bicubic spline</dl>
</dl>
<dl>
<dt>
<dd> <i>NOTE:</i> Some -sws options are tunable. The description of the scale video filter has further information.</dl>
<dt><code>-vc &lt;[-|+]codec1,[-|+]codec2,&#8230;[,]&gt;</code></p>
<dd> Specify a priority list of video codecs to be used, according to their codec name in codecs.conf. Use a &#8216;-&#8216; before the codec name to omit it. Use a &#8216;+&#8217; before the codec name to force it, this will likely crash! If the list has a trailing &#8216;,&#8217; MPlayer will fall back on codecs not contained in the list.<br />
 <i>NOTE:</i> See -vc help for a full list of available codecs. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-vc divx</p>
<dd> Force Win32/:VfW DivX codec, no fallback.</p>
<dt>-vc -divxds,-divx,</p>
<dd> Skip Win32 DivX codecs.</p>
<dt>-vc ffmpeg12,mpeg12,</p>
<dd> Try libavcodec&#8217;s MPEG-1/2 codec, then libmpeg2, then others.</dl>
</dl>
<dt><code>-vfm &lt;driver1,driver2,&#8230;&gt;</code></p>
<dd> Specify a priority list of video codec families to be used, according to their names in codecs.conf. Falls back on the default codecs if none of the given codec families work.<br />
 <i>NOTE:</i> See -vfm help for a full list of available codec families. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-vfm ffmpeg,dshow,vfw</p>
<dd> Try the libavcodec, then Directshow, then VfW codecs and fall back on others, if they do not work.</p>
<dt>-vfm xanim</p>
<dd> Try XAnim codecs first.</dl>
</dl>
<dt><code>-x &lt;x&gt; (also see -zoom) (MPlayer only)</code></p>
<dd> Scale image to width &lt;x&gt; (if software/:hardware scaling is available). Disables aspect calculations.</p>
<dt><code>-xvidopts &lt;option1:option2:&#8230;&gt;</code></p>
<dd> Specify additional parameters when decoding with Xvid.<br />
 <i>NOTE:</i> Since libavcodec is faster than Xvid you might want to use the libavcodec postprocessing filter (-vf pp) and decoder (-vfm ffmpeg) instead. </p>
<p> Xvid&#8217;s internal postprocessing filters:</p>
<dl>
<dt>
<dd>
<dl>
<dt>deblock-chroma (also see -vf pp)</p>
<dd> chroma deblock filter</p>
<dt>deblock-luma (also see -vf pp)</p>
<dd> luma deblock filter</p>
<dt>dering-luma (also see -vf pp)</p>
<dd> luma deringing filter</p>
<dt>dering-chroma (also see -vf pp)</p>
<dd> chroma deringing filter</p>
<dt>filmeffect (also see -vf noise)</p>
<dd> Adds artificial film grain to the video. May increase perceived quality, while lowering true quality.</dl>
</dl>
<dl>
<dt>
<dd> rendering methods:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>dr2&nbsp;<wbr>&nbsp;</p>
<dd> Activate direct rendering method 2.</p>
<dt>nodr2</p>
<dd> Deactivate direct rendering method 2.</dl>
</dl>
<dt><code>-xy &lt;value&gt; (also see -zoom)</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>value&lt;=8</p>
<dd> Scale image by factor &lt;value&gt;.</p>
<dt>value&gt;8</p>
<dd> Set width to value and calculate height to keep correct aspect ratio.</dl>
</dl>
<dt><code>-y &lt;y&gt; (also see -zoom) (MPlayer only)</code></p>
<dd> Scale image to height &lt;y&gt; (if software/:hardware scaling is available). Disables aspect calculations.</p>
<dt><code>-zoom&nbsp;<wbr>&nbsp;</code></p>
<dd> Allow software scaling, where available. This will allow scaling with output drivers (like x11, fbdev) that do not support hardware scaling where MPlayer disables scaling by default for performance reasons.</dl>
<h2>AUDIO FILTERS</h2>
<p> Audio filters allow you to modify the audio stream and its properties. The syntax is:</p>
<dl>
<dt><code>-af &lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></p>
<dd> Setup a chain of audio filters.</dl>
<p> <i>NOTE:</i> To get a full list of available audio filters, see -af help. </p>
<p> Audio filters are managed in lists. There are a few commands to manage the filter list.</p>
<dl>
<dt><code>-af-add &lt;filter1[,filter2,&#8230;]&gt;</code></p>
<dd> Appends the filters given as arguments to the filter list.</p>
<dt><code>-af-pre &lt;filter1[,filter2,&#8230;]&gt;</code></p>
<dd> Prepends the filters given as arguments to the filter list.</p>
<dt><code>-af-del &lt;index1[,index2,&#8230;]&gt;</code></p>
<dd> Deletes the filters at the given indexes. Index numbers start at 0, negative numbers address the end of the list (-1 is the last).</p>
<dt><code>-af-clr</code></p>
<dd> Completely empties the filter list.</dl>
<p> Available filters are:</p>
<dl>
<dt><code>resample[=srate[:sloppy[:type]]]</code></p>
<dd> Changes the sample rate of the audio stream. Can be used if you have a fixed frequency sound card or if you are stuck with an old sound card that is only capable of max 44.1kHz. This filter is automatically enabled if necessary. It only supports 16-bit integer and float in native-endian format as input.<br />
 <i>NOTE:</i> With MEncoder, you need to also use -srate &lt;srate&gt;.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;srate&gt;</p>
<dd> output sample frequency in Hz. The valid range for this parameter is 8000 to 192000. If the input and output sample frequency are the same or if this parameter is omitted the filter is automatically unloaded. A high sample frequency normally improves the audio quality, especially when used in combination with other filters.</p>
<dt>&lt;sloppy&gt;</p>
<dd> Allow (1) or disallow (0) the output frequency to differ slightly from the frequency given by &lt;srate&gt; (default: 1). Can be used if the startup of the playback is extremely slow.</p>
<dt>&lt;type&gt;</p>
<dd> Select which resampling method to use.</p>
<dl>
<dt>
<dd> 0: linear interpolation (fast, poor quality especially when upsampling)<br />
 1: polyphase filterbank and integer processing<br />
 2: polyphase filterbank and floating point processing (slow, best quality)</dl>
</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af resample=44100:0:0</p>
<dd> would set the output frequency of the resample filter to 44100Hz using exact output frequency scaling and linear interpolation.</dl>
</dl>
<dt><code>lavcresample[=srate[:length[:linear[:count[:cutoff]]]]]</code></p>
<dd> Changes the sample rate of the audio stream to an integer &lt;srate&gt; in Hz. It only supports the 16-bit native-endian format.<br />
 <i>NOTE:</i> With MEncoder, you need to also use -srate &lt;srate&gt;.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;srate&gt;</p>
<dd> the output sample rate</p>
<dt>&lt;length&gt;</p>
<dd> length of the filter with respect to the lower sampling rate (default: 16)</p>
<dt>&lt;linear&gt;</p>
<dd> if 1 then filters will be linearly interpolated between polyphase entries</p>
<dt>&lt;count&gt;</p>
<dd> log2 of the number of polyphase entries (&#8230;, 10-&gt;1024, 11-&gt;2048, 12-&gt;4096, &#8230;) (default: 10-&gt;1024)</p>
<dt>&lt;cutoff&gt;</p>
<dd> cutoff frequency (0.0-1.0), default set depending upon filter length</dl>
</dl>
<dt><code>lavcac3enc[=tospdif[:bitrate[:minchn]]]</code></p>
<dd> Encode multi-channel audio to AC-3 at runtime using libavcodec. Supports 16-bit native-endian input format, maximum 6 channels. The output is big-endian when outputting a raw AC-3 stream, native-endian when outputting to S/PDIF. The output sample rate of this filter is same with the input sample rate. When input sample rate is 48kHz, 44.1kHz, or 32kHz, this filter directly use it. Otherwise a resampling filter is auto-inserted before this filter to make the input and output sample rate be 48kHz. You need to specify &#8216;-channels N&#8217; to make the decoder decode audio into N-channel, then the filter can encode the N-channel input to AC-3. </p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;tospdif&gt;</p>
<dd> Output raw AC-3 stream if zero or not set, output to S/PDIF for passthrough when &lt;tospdif&gt; is set non-zero.</p>
<dt>&lt;bitrate&gt;</p>
<dd> The bitrate to encode the AC-3 stream. Set it to either 384 or 384000 to get 384kbits. Valid values: 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;320, 384, 448, 512, 576, 640 Default bitrate is based on the input channel number: 1ch: 96, 2ch: 192, 3ch: 224, 4ch: 384, 5ch: 448, 6ch: 448</p>
<dt>&lt;minchn&gt;</p>
<dd> If the input channel number is less than &lt;minchn&gt;, the filter will detach itself (default: 5).</dl>
</dl>
<dt><code>sweep[=speed]</code></p>
<dd> Produces a sine sweep.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;0.0-1.0&gt;</p>
<dd> Sine function delta, use very low values to hear the sweep.</dl>
</dl>
<dt><code>sinesuppress[=freq:decay]</code></p>
<dd> Remove a sine at the specified frequency. Useful to get rid of the 50/60Hz noise on low quality audio equipment. It probably only works on mono input.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;freq&gt;</p>
<dd> The frequency of the sine which should be removed (in Hz) (default: 50)</p>
<dt>&lt;decay&gt;</p>
<dd> Controls the adaptivity (a larger value will make the filter adapt to amplitude and phase changes quicker, a smaller value will make the adaptation slower) (default: 0.0001). Reasonable values are around 0.001.</dl>
</dl>
<dt><code>bs2b[=option1:option2:&#8230;]</code></p>
<dd> Bauer stereophonic to binaural transformation using libbs2b. Improves the headphone listening experience by making the sound similar to that from loudspeakers, allowing each ear to hear both channels and taking into account the distance difference and the head shadowing effect. It is applicable only to 2 channel audio.</p>
<dl>
<dt>
<dd>
<dl>
<dt>fcut=&lt;300-1000&gt;</p>
<dd> Set cut frequency in Hz.</p>
<dt>feed=&lt;10-150&gt;</p>
<dd> Set feed level for low frequencies in 0.1*dB.</p>
<dt>profile=&lt;value&gt;</p>
<dd> Several profiles are available for convenience:</p>
<dl>
<dt>
<dd>
<dl>
<dt>default</p>
<dd> will be used if nothing else was specified (fcut=700, feed=45)</p>
<dt>cmoy&nbsp;</p>
<dd> Chu Moy circuit implementation (fcut=700, feed=60)</p>
<dt>jmeier</p>
<dd> Jan Meier circuit implementation (fcut=650, feed=95)</dl>
</dl>
</dl>
</dl>
<dl>
<dt>
<dd> If fcut or feed options are specified together with a profile, they will be applied on top of the selected profile.</dl>
<dt><code>hrtf[=flag]</code></p>
<dd> Head-related transfer function: Converts multichannel audio to 2 channel output for headphones, preserving the spatiality of the sound. </p>
<dl>
<dt>
<dd>
<dl>
<dt>Flag Meaning</p>
<dd>
<dt>m matrix decoding of the rear channel</p>
<dd>
<dt>s 2-channel matrix decoding</p>
<dd>
<dt>0 no matrix decoding (default)</p>
<dd></dl>
</dl>
<dt><code>equalizer=[g1:g2:g3:&#8230;:g10]</code></p>
<dd> 10 octave band graphic equalizer, implemented using 10 IIR band pass filters. This means that it works regardless of what type of audio is being played back. The center frequencies for the 10 bands are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>No. frequency</p>
<dd>
<dt>0 31.25 Hz</p>
<dd>
<dt>1 62.50 Hz</p>
<dd>
<dt>2 125.00 Hz</p>
<dd>
<dt>3 250.00 Hz</p>
<dd>
<dt>4 500.00 Hz</p>
<dd>
<dt>5 1.00 kHz</p>
<dd>
<dt>6 2.00 kHz</p>
<dd>
<dt>7 4.00 kHz</p>
<dd>
<dt>8 8.00 kHz</p>
<dd>
<dt>9 16.00 kHz</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd> If the sample rate of the sound being played is lower than the center frequency for a frequency band, then that band will be disabled. A known bug with this filter is that the characteristics for the uppermost band are not completely symmetric if the sample rate is close to the center frequency of that band. This problem can be worked around by upsampling the sound using the resample filter before it reaches this filter.</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;g1&gt;:&lt;g2&gt;:&lt;g3&gt;:&#8230;:&lt;g10&gt;</p>
<dd> floating point numbers representing the gain in dB for each frequency band (-12-12)</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af equalizer=11:11:10:5:0:-12:0:5:12:12 media.avi</p>
<dd> Would amplify the sound in the upper and lower frequency region while canceling it almost completely around 1kHz.</dl>
</dl>
<dt><code>channels=nch[:nr:from1:to1:from2:to2:from3:to3:&#8230;]</code></p>
<dd> Can be used for adding, removing, routing and copying audio channels. If only &lt;nch&gt; is given the default routing is used, it works as follows: If the number of output channels is bigger than the number of input channels empty channels are inserted (except mixing from mono to stereo, then the mono channel is repeated in both of the output channels). If the number of output channels is smaller than the number of input channels the exceeding channels are truncated.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;nch&gt;</p>
<dd> number of output channels (1-8)</p>
<dt>&lt;nr&gt;&nbsp;</p>
<dd> number of routes (1-8)</p>
<dt>&lt;from1:to1:from2:to2:from3:to3:&#8230;&gt;</p>
<dd> Pairs of numbers between 0 and 7 that define where to route each channel.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af channels=4:4:0:1:1:0:2:2:3:3 media.avi</p>
<dd> Would change the number of channels to 4 and set up 4 routes that swap channel 0 and channel 1 and leave channel 2 and 3 intact. Observe that if media containing two channels was played back, channels 2 and 3 would contain silence but 0 and 1 would still be swapped.</p>
<dt>mplayer -af channels=6:4:0:0:0:1:0:2:0:3 media.avi</p>
<dd> Would change the number of channels to 6 and set up 4 routes that copy channel 0 to channels 0 to 3. Channel 4 and 5 will contain silence.</dl>
</dl>
<dt><code>format[=format] (also see -format)</code></p>
<dd> Convert between different sample formats. Automatically enabled when needed by the sound card or another filter.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;format&gt;</p>
<dd> Sets the desired format. The general form is &#8216;sbe&#8217;, where &#8216;s&#8217; denotes the sign (either &#8216;s&#8217; for signed or &#8216;u&#8217; for unsigned), &#8216;b&#8217; denotes the number of bits per sample (16, 24 or 32) and &#8216;e&#8217; denotes the endianness (&#8216;le&#8217; means little-endian, &#8216;be&#8217; big-endian and &#8216;ne&#8217; the endianness of the computer MPlayer is running on). Valid values (amongst others) are: &#8216;s16le&#8217;, &#8216;u32be&#8217; and &#8216;u24ne&#8217;. Exceptions to this rule that are also valid format specifiers: u8, s8, floatle, floatbe, floatne, mulaw, alaw, mpeg2, ac3 and imaadpcm.</dl>
</dl>
<dt><code>volume[=v[:sc]]</code></p>
<dd> Implements software volume control. Use this filter with caution since it can reduce the signal to noise ratio of the sound. In most cases it is best to set the level for the PCM sound to max, leave this filter out and control the output level to your speakers with the master volume control of the mixer. In case your sound card has a digital PCM mixer instead of an analog one, and you hear distortion, use the MASTER mixer instead. If there is an external amplifier connected to the computer (this is almost always the case), the noise level can be minimized by adjusting the master level and the volume knob on the amplifier until the hissing noise in the background is gone.<br />
 This filter has a second feature: It measures the overall maximum sound level and prints out that level when MPlayer exits. This volume estimate can be used for setting the sound level in MEncoder such that the maximum dynamic range is utilized. This feature currently only works with floating-point data, use e.g. -af-adv force=5, or use -af stats.<br />
 <i>NOTE:</i> This filter is not reentrant and can therefore only be enabled once for every audio stream.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;v&gt;&nbsp;<wbr>&nbsp;</p>
<dd> Sets the desired gain in dB for all channels in the stream from -200dB to +60dB, where -200dB mutes the sound completely and +60dB equals a gain of 1000 (default: 0).</p>
<dt>&lt;sc&gt;&nbsp;</p>
<dd> Turns soft clipping on (1) or off (0). Soft-clipping can make the sound more smooth if very high volume levels are used. Enable this option if the dynamic range of the loudspeakers is very low.<br />
 <i>WARNING:</i> This feature creates distortion and should be considered a last resort.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af volume=10.1:0 media.avi</p>
<dd> Would amplify the sound by 10.1dB and hard-clip if the sound level is too high.</dl>
</dl>
<dt><code>pan=n[:L00:L01:L02:&#8230;L10:L11:L12:&#8230;Ln0:Ln1:Ln2:&#8230;]</code></p>
<dd> Mixes channels arbitrarily. Basically a combination of the volume and the channels filter that can be used to down-mix many channels to only a few, e.g. stereo to mono or vary the &quot;width&quot; of the center speaker in a surround sound system. This filter is hard to use, and will require some tinkering before the desired result is obtained. The number of options for this filter depends on the number of output channels. An example how to downmix a six-channel file to two channels with this filter can be found in the examples section near the end.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;n&gt;&nbsp;<wbr>&nbsp;</p>
<dd> number of output channels (1-8)</p>
<dt>&lt;Lij&gt;</p>
<dd> How much of input channel i is mixed into output channel j (0-1). So in principle you first have n numbers saying what to do with the first input channel, then n numbers that act on the second input channel etc. If you do not specify any numbers for some input channels, 0 is assumed.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af pan=1:0.5:0.5 media.avi</p>
<dd> Would down-mix from stereo to mono.</p>
<dt>mplayer -af pan=3:1:0:0.5:0:1:0.5 media.avi</p>
<dd> Would give 3 channel output leaving channels 0 and 1 intact, and mix channels 0 and 1 into output channel 2 (which could be sent to a subwoofer for example).</dl>
</dl>
<dt><code>sub[=fc:ch]</code></p>
<dd> Adds a subwoofer channel to the audio stream. The audio data used for creating the subwoofer channel is an average of the sound in channel 0 and channel 1. The resulting sound is then low-pass filtered by a 4th order Butterworth filter with a default cutoff frequency of 60Hz and added to a separate channel in the audio stream.<br />
 <i>Warning:</i> Disable this filter when you are playing DVDs with Dolby Digital 5.1 sound, otherwise this filter will disrupt the sound to the subwoofer.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;fc&gt;&nbsp;</p>
<dd> cutoff frequency in Hz for the low-pass filter (20Hz to 300Hz) (default: 60Hz) For the best result try setting the cutoff frequency as low as possible. This will improve the stereo or surround sound experience.</p>
<dt>&lt;ch&gt;&nbsp;</p>
<dd> Determines the channel number in which to insert the sub-channel audio. Channel number can be between 0 and 7 (default: 5). Observe that the number of channels will automatically be increased to &lt;ch&gt; if necessary.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af sub=100:4 -channels 5 media.avi</p>
<dd> Would add a sub-woofer channel with a cutoff frequency of 100Hz to output channel 4.</dl>
</dl>
<dt><code>center&nbsp;</code></p>
<dd> Creates a center channel from the front channels. May currently be low quality as it does not implement a high-pass filter for proper extraction yet, but averages and halves the channels instead.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;ch&gt;&nbsp;</p>
<dd> Determines the channel number in which to insert the center channel. Channel number can be between 0 and 7 (default: 5). Observe that the number of channels will automatically be increased to &lt;ch&gt; if necessary.</dl>
</dl>
<dt><code>surround[=delay]</code></p>
<dd> Decoder for matrix encoded surround sound like Dolby Surround. Many files with 2 channel audio actually contain matrixed surround sound. Requires a sound card supporting at least 4 channels.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;delay&gt;</p>
<dd> delay time in ms for the rear speakers (0 to 1000) (default: 20) This delay should be set as follows: If d1 is the distance from the listening position to the front speakers and d2 is the distance from the listening position to the rear speakers, then the delay should be set to 15ms if d1 &lt;= d2 and to 15 + 5*(d1-d2) if d1 &gt; d2.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af surround=15 -channels 4 media.avi</p>
<dd> Would add surround sound decoding with 15ms delay for the sound to the rear speakers.</dl>
</dl>
<dt><code>delay[=ch1:ch2:&#8230;]</code></p>
<dd> Delays the sound to the loudspeakers such that the sound from the different channels arrives at the listening position simultaneously. It is only useful if you have more than 2 loudspeakers.</p>
<dl>
<dt>
<dd>
<dl>
<dt>ch1,ch2,&#8230;</p>
<dd> The delay in ms that should be imposed on each channel (floating point number between 0 and 1000).</dl>
</dl>
<dl>
<dt>
<dd> To calculate the required delay for the different channels do as follows:</p>
<dl>
<dt>1.</p>
<dd> Measure the distance to the loudspeakers in meters in relation to your listening position, giving you the distances s1 to s5 (for a 5.1 system). There is no point in compensating for the subwoofer (you will not hear the difference anyway).</p>
<dt>2.</p>
<dd> Subtract the distances s1 to s5 from the maximum distance, i.e. s[i] = max(s) &#8211; s[i]; i = 1&#8230;5.</p>
<dt>3.</p>
<dd> Calculate the required delays in ms as d[i] = 1000*s[i]/342; i = 1&#8230;5.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af delay=10.5:10.5:0:0:7:0 media.avi</p>
<dd> Would delay front left and right by 10.5ms, the two rear channels and the sub by 0ms and the center channel by 7ms.</dl>
</dl>
<dt><code>export[=mmapped_file[:nsamples]]</code></p>
<dd> Exports the incoming signal to other processes using memory mapping (mmap()). Memory mapped areas contain a header: </p>
<pre><code>
int nch                        /*number of channels*/
    int size                   /*buffer size*/
    unsigned long long counter /*Used to keep sync, updated every
                                 time new data is exported.*/
</code></pre>
<p> The rest is payload (non-interleaved) 16 bit data.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;mmapped_file&gt;</p>
<dd> file to map data to (default: ~/.mplayer/:mplayer-af_export)</p>
<dt>&lt;nsamples&gt;</p>
<dd> number of samples per channel (default: 512)</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af export=/tmp/mplayer-af_export:1024 media.avi</p>
<dd> Would export 1024 samples per channel to &#8216;/tmp/mplayer-af_export&#8217;.</dl>
</dl>
<dt><code>extrastereo[=mul]</code></p>
<dd> (Linearly) increases the difference between left and right channels which adds some sort of &quot;live&quot; effect to playback.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;mul&gt;</p>
<dd> Sets the difference coefficient (default: 2.5). 0.0 means mono sound (average of both channels), with 1.0 sound will be unchanged, with -1.0 left and right channels will be swapped.</dl>
</dl>
<dt><code>volnorm[=method:target]</code></p>
<dd> Maximizes the volume without distorting the sound.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;method&gt;</p>
<dd> Sets the used method.</p>
<dl>
<dt>
<dd> 1: Use a single sample to smooth the variations via the standard weighted mean over past samples (default).<br />
 2: Use several samples to smooth the variations via the standard weighted mean over past samples.</dl>
<dt>&lt;target&gt;</p>
<dd> Sets the target amplitude as a fraction of the maximum for the sample type (default: 0.25).</dl>
</dl>
<dt><code>ladspa=file:label[:controls&#8230;]</code></p>
<dd> Load a LADSPA (Linux Audio Developer&#8217;s Simple Plugin API) plugin. This filter is reentrant, so multiple LADSPA plugins can be used at once.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;file&gt;</p>
<dd> Specifies the LADSPA plugin library file. If LADSPA_PATH is set, it searches for the specified file. If it is not set, you must supply a fully specified pathname.</p>
<dt>&lt;label&gt;</p>
<dd> Specifies the filter within the library. Some libraries contain only one filter, but others contain many of them. Entering &#8216;help&#8217; here, will list all available filters within the specified library, which eliminates the use of &#8216;listplugins&#8217; from the LADSPA SDK.</p>
<dt>&lt;controls&gt;</p>
<dd> Controls are zero or more floating point values that determine the behavior of the loaded plugin (for example delay, threshold or gain). In verbose mode (add -v to the MPlayer command line), all available controls and their valid ranges are printed. This eliminates the use of &#8216;analyseplugin&#8217; from the LADSPA SDK.</dl>
</dl>
<dt><code>comp&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Compressor/expander filter usable for microphone input. Prevents artifacts on very loud sound and raises the volume on very low sound. This filter is untested, maybe even unusable.</p>
<dt><code>gate&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Noise gate filter similar to the comp audio filter. This filter is untested, maybe even unusable.</p>
<dt><code>karaoke</code></p>
<dd> Simple voice removal filter exploiting the fact that voice is usually recorded with mono gear and later &#8216;center&#8217; mixed onto the final audio stream. Beware that this filter will turn your signal into mono. Works well for 2 channel tracks; do not bother trying it on anything but 2 channel stereo.</p>
<dt><code>scaletempo[=option1:option2:&#8230;]</code></p>
<dd> Scales audio tempo without altering pitch, optionally synced to playback speed (default).<br />
 This works by playing &#8216;stride&#8217; ms of audio at normal speed then consuming &#8216;stride*scale&#8217; ms of input audio. It pieces the strides together by blending &#8216;overlap&#8217;% of stride with audio following the previous stride. It optionally performs a short statistical analysis on the next &#8216;search&#8217; ms of audio to determine the best overlap position.</p>
<dl>
<dt>
<dd>
<dl>
<dt>scale=&lt;amount&gt;</p>
<dd> Nominal amount to scale tempo. Scales this amount in addition to speed. (default: 1.0)</p>
<dt>stride=&lt;amount&gt;</p>
<dd> Length in milliseconds to output each stride. Too high of value will cause noticeable skips at high scale amounts and an echo at low scale amounts. Very low values will alter pitch. Increasing improves performance. (default: 60)</p>
<dt>overlap=&lt;percent&gt;</p>
<dd> Percentage of stride to overlap. Decreasing improves performance. (default: .20)</p>
<dt>search=&lt;amount&gt;</p>
<dd> Length in milliseconds to search for best overlap position. Decreasing improves performance greatly. On slow systems, you will probably want to set this very low. (default: 14)</p>
<dt>speed=&lt;tempo|pitch|both|none&gt;</p>
<dd> Set response to speed change.</p>
<dl>
<dt>
<dd>
<dl>
<dt>tempo</p>
<dd> Scale tempo in sync with speed (default).</p>
<dt>pitch</p>
<dd> Reverses effect of filter. Scales pitch without altering tempo. Add &#8216;[ speed_mult 0.9438743126816935&#8217; and &#8216;] speed_mult 1.059463094352953&#8217; to your input.conf to step by musical semi-tones. <i>WARNING:</i> Loses sync with video.</p>
<dt>both</p>
<dd> Scale both tempo and pitch.</p>
<dt>none</p>
<dd> Ignore speed changes.</dl>
</dl>
</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>mplayer -af scaletempo -speed 1.2 media.ogg</p>
<dd> Would playback media at 1.2x normal speed, with audio at normal pitch. Changing playback speed, would change audio tempo to match.</p>
<dt>mplayer -af scaletempo=scale=1.2:speed=none -speed 1.2 media.ogg</p>
<dd> Would playback media at 1.2x normal speed, with audio at normal pitch, but changing playback speed has no effect on audio tempo.</p>
<dt>mplayer -af scaletempo=stride=30:overlap=.50:search=10 media.ogg</p>
<dd> Would tweak the quality and performace parameters.</p>
<dt>mplayer -af format=floatne,scaletempo media.ogg</p>
<dd> Would make scaletempo use float code. Maybe faster on some platforms.</p>
<dt>mplayer -af scaletempo=scale=1.2:speed=pitch audio.ogg</p>
<dd> Would playback audio file at 1.2x normal speed, with audio at normal pitch. Changing playback speed, would change pitch, leaving audio tempo at 1.2x.</dl>
</dl>
<dt><code>stats&nbsp;<wbr>&nbsp;</code></p>
<dd> Collects and prints statistics about the audio stream, especially the volume. These statistics are especially intended to help adjusting the volume while avoiding clipping. The volumes are printed in dB and compatible with the volume audio filter, they are always rounded towards -0dB. </p>
<p> The &#8216;n_samples&#8217; field is the total number of samples seen by the filter. The &#8216;mean_volume&#8217; field is the root mean square. The &#8216;max_volume&#8217; field is exactly what it says. The &#8216;histogram_Xdb&#8217; fields count how many samples were at -XdB, for X just below max_volume. </p>
<p> For example, if max_volume is -7dB and histogram_7dB is 19, &#8216;volume=7&#8217; will not cause clipping and &#8216;volume=8&#8217; will cause clipping on exactly 19 samples.</dl>
<h2>VIDEO FILTERS</h2>
<p> Video filters allow you to modify the video stream and its properties. The syntax is:</p>
<dl>
<dt><code>-vf &lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></p>
<dd> Setup a chain of video filters.</dl>
<p> Many parameters are optional and set to default values if omitted. To explicitly use a default value set a parameter to &#8216;-1&#8217;. Parameters w:h means width x height in pixels, x:y means x;y position counted from the upper left corner of the bigger image.<br />
 <i>NOTE:</i> To get a full list of available video filters, see -vf help. </p>
<p> Video filters are managed in lists. There are a few commands to manage the filter list.</p>
<dl>
<dt><code>-vf-add &lt;filter1[,filter2,&#8230;]&gt;</code></p>
<dd> Appends the filters given as arguments to the filter list.</p>
<dt><code>-vf-pre &lt;filter1[,filter2,&#8230;]&gt;</code></p>
<dd> Prepends the filters given as arguments to the filter list.</p>
<dt><code>-vf-del &lt;index1[,index2,&#8230;]&gt;</code></p>
<dd> Deletes the filters at the given indexes. Index numbers start at 0, negative numbers address the end of the list (-1 is the last).</p>
<dt><code>-vf-clr</code></p>
<dd> Completely empties the filter list.</dl>
<p> With filters that support it, you can access parameters by their name.</p>
<dl>
<dt><code>-vf &lt;filter&gt;=help</code></p>
<dd> Prints the parameter names and parameter value ranges for a particular filter.</p>
<dt><code>-vf &lt;filter=named_parameter1=value1[:named_parameter2=value2:&#8230;]&gt;</code></p>
<dd> Sets a named parameter to the given value. Use on and off or yes and no to set flag parameters.</dl>
<p> Available filters are:</p>
<dl>
<dt><code>crop[=w:h:x:y]</code></p>
<dd> Crops the given part of the image and discards the rest. Useful to remove black bands from widescreen movies.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</p>
<dd> Cropped width and height, defaults to original width and height.</p>
<dt>&lt;x&gt;,&lt;y&gt;</p>
<dd> Position of the cropped picture, defaults to center.</dl>
</dl>
<dt><code>cropdetect[=limit:round[:reset]]</code></p>
<dd> Calculates necessary cropping parameters and prints the recommended parameters to stdout.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;limit&gt;</p>
<dd> Threshold, which can be optionally specified from nothing (0) to everything (255) (default: 24). </p>
<dt>&lt;round&gt;</p>
<dd> Value which the width/:height should be divisible by (default: 16). The offset is automatically adjusted to center the video. Use 2 to get only even dimensions (needed for 4:2:2 video). 16 is best when encoding to most video codecs. </p>
<dt>&lt;reset&gt;</p>
<dd> Counter that determines after how many frames cropdetect will reset the previously detected largest video area and start over to detect the current optimal crop area (default: 0). This can be useful when channel logos distort the video area. 0 indicates never reset and return the largest area encountered during playback.</dl>
</dl>
<dt><code>rectangle[=w:h:x:y]</code></p>
<dd> Draws a rectangle of the requested width and height at the specified coordinates over the image and prints current rectangle parameters to the console. This can be used to find optimal cropping parameters. If you bind the input.conf directive &#8216;change_rectangle&#8217; to keystrokes, you can move and resize the rectangle on the fly.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</p>
<dd> width and height (default: -1, maximum possible width where boundaries are still visible.)</p>
<dt>&lt;x&gt;,&lt;y&gt;</p>
<dd> top left corner position (default: -1, uppermost leftmost)</dl>
</dl>
<dt><code>expand[=w:h:x:y:o:a:r]</code></p>
<dd> Expands (not scales) movie resolution to the given value and places the unscaled original at coordinates x, y. Can be used for placing subtitles/:OSD in the resulting black bands.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</p>
<dd> Expanded width,height (default: original width,height). Negative values for w and h are treated as offsets to the original size. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>expand=0:-50:0:0</p>
<dd> Adds a 50 pixel border to the bottom of the picture.</dl>
</dl>
<dt>&lt;x&gt;,&lt;y&gt;</p>
<dd> position of original image on the expanded image (default: center)</p>
<dt>&lt;o&gt;&nbsp;<wbr>&nbsp;</p>
<dd> OSD/:subtitle rendering</p>
<dl>
<dt>
<dd> 0: disable (default)<br />
 1: enable</dl>
<dt>&lt;a&gt;&nbsp;<wbr>&nbsp;</p>
<dd> Expands to fit an aspect instead of a resolution (default: 0). </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>expand=800:::::4/3</p>
<dd> Expands to 800&#215;600, unless the source is higher resolution, in which case it expands to fill a 4/3 aspect.</dl>
</dl>
<dt>&lt;r&gt;&nbsp;<wbr>&nbsp;</p>
<dd> Rounds up to make both width and height divisible by &lt;r&gt; (default: 1).</dl>
</dl>
<dt><code>flip (also see -flip)</code></p>
<dd> Flips the image upside down.</p>
<dt><code>mirror&nbsp;</code></p>
<dd> Mirrors the image on the Y axis.</p>
<dt><code>rotate[=&lt;0-7&gt;]</code></p>
<dd> Rotates the image by 90 degrees and optionally flips it. For values between 4-7 rotation is only done if the movie geometry is portrait and not landscape.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Rotate by 90 degrees clockwise and flip (default).</p>
<dt>1</p>
<dd> Rotate by 90 degrees clockwise.</p>
<dt>2</p>
<dd> Rotate by 90 degrees counterclockwise.</p>
<dt>3</p>
<dd> Rotate by 90 degrees counterclockwise and flip.</dl>
</dl>
<dt><code>scale[=w:h[:interlaced[:chr_drop[:par[:par2[:presize[:noup[:arnd]]]]]]]]</code></p>
<dd> Scales the image with the software scaler (slow) and performs a YUV&lt;-&gt;RGB colorspace conversion (also see -sws).</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</p>
<dd> scaled width/:height (default: original width/:height)<br />
 <i>NOTE:</i> If -zoom is used, and underlying filters (including libvo) are incapable of scaling, it defaults to d_width/:d_height!</p>
<dl>
<dt>
<dd>
&nbsp;0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;scaled d_width/:d_height<br />
 -1: original width/:height<br />
 -2: Calculate w/h using the other dimension and the prescaled aspect ratio.<br />
 -3: Calculate w/h using the other dimension and the original aspect ratio.<br />
 -(n+8): Like -n above, but rounding the dimension to the closest multiple of 16.</dl>
<dt>&lt;interlaced&gt;</p>
<dd> Toggle interlaced scaling.</p>
<dl>
<dt>
<dd> 0: off (default)<br />
 1: on</dl>
<dt>&lt;chr_drop&gt;</p>
<dd> chroma skipping</p>
<dl>
<dt>
<dd> 0: Use all available input lines for chroma.<br />
 1: Use only every 2. input line for chroma.<br />
 2: Use only every 4. input line for chroma.<br />
 3: Use only every 8. input line for chroma.</dl>
<dt>&lt;par&gt;[:&lt;par2&gt;] (also see -sws)</p>
<dd> Set some scaling parameters depending on the type of scaler selected with -sws.</p>
<dl>
<dt>
<dd> -sws 2 (bicubic): B (blurring) and C (ringing)<br />
 0.00:0.60 default<br />
 0.00:0.75 VirtualDub&#8217;s &quot;precise bicubic&quot;<br />
 0.00:0.50 Catmull-Rom spline<br />
 0.33:0.33 Mitchell-Netravali spline<br />
 1.00:0.00 cubic B-spline<br />
 -sws 7 (gaussian): sharpness (0 (soft) &#8211; 100 (sharp))<br />
 -sws 9 (lanczos): filter length (1-10)</dl>
<dt>&lt;presize&gt;</p>
<dd> Scale to preset sizes.</p>
<dl>
<dt>
<dd> qntsc: 352&#215;240 (NTSC quarter screen)<br />
 qpal: 352&#215;288 (PAL quarter screen)<br />
 ntsc: 720&#215;480 (standard NTSC)<br />
 pal: 720&#215;576 (standard PAL)<br />
 sntsc: 640&#215;480 (square pixel NTSC)<br />
 spal: 768&#215;576 (square pixel PAL)</dl>
<dt>&lt;noup&gt;</p>
<dd> Disallow upscaling past the original dimensions.</p>
<dl>
<dt>
<dd> 0: Allow upscaling (default).<br />
 1: Disallow upscaling if one dimension exceeds its original value.<br />
 2: Disallow upscaling if both dimensions exceed their original values.</dl>
<dt>&lt;arnd&gt;</p>
<dd> Accurate rounding for the vertical scaler, which may be faster or slower than the default rounding.</p>
<dl>
<dt>
<dd> 0: Disable accurate rounding (default).<br />
 1: Enable accurate rounding.</dl>
</dl>
</dl>
<dt><code>dsize[=aspect|w:h:aspect-method:r]</code></p>
<dd> Changes the intended display size/:aspect at an arbitrary point in the filter chain. Aspect can be given as a fraction (4/3) or floating point number (1.33). Alternatively, you may specify the exact display width and height desired. Note that this filter does <code>not</code> do any scaling itself; it just affects what later scalers (software or hardware) will do when auto-scaling to correct aspect.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;w&gt;,&lt;h&gt;</p>
<dd> New display width and height. Can also be these special values:</p>
<dl>
<dt>
<dd>
&nbsp;0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;original display width and height<br />
 -1: original video width and height (default)<br />
 -2: Calculate w/h using the other dimension and the original display aspect ratio.<br />
 -3: Calculate w/h using the other dimension and the original video aspect ratio.</dl>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>dsize=800:-2</p>
<dd> Specifies a display resolution of 800&#215;600 for a 4/3 aspect video, or 800&#215;450 for a 16/9 aspect video.</dl>
</dl>
<dt>&lt;aspect-method&gt;</p>
<dd> Modifies width and height according to original aspect ratios.</p>
<dl>
<dt>
<dd> -1: Ignore original aspect ratio (default). </p>
<p>&nbsp;0: Keep display aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as maximum resolution. </p>
<p>&nbsp;1: Keep display aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as minimum resolution. </p>
<p>&nbsp;2: Keep video aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as maximum resolution. </p>
<p>&nbsp;3: Keep video aspect ratio by using&nbsp;&lt;w&gt;&nbsp;and&nbsp;&lt;h&gt;&nbsp;as minimum resolution.</dl>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>dsize=800:600:0</p>
<dd> Specifies a display resolution of at most 800&#215;600, or smaller, in order to keep aspect.</dl>
</dl>
<dt>&lt;r&gt;&nbsp;<wbr>&nbsp;</p>
<dd> Rounds up to make both width and height divisible by &lt;r&gt; (default: 1).</dl>
</dl>
<dt><code>yvu9&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Forces software YVU9 to YV12 colorspace conversion. Deprecated in favor of the software scaler.</p>
<dt><code>yuvcsp&nbsp;</code></p>
<dd> Clamps YUV color values to the CCIR 601 range without doing real conversion.</p>
<dt><code>palette</code></p>
<dd> RGB/BGR 8 -&gt; 15/16/24/32bpp colorspace conversion using palette.</p>
<dt><code>format[=fourcc[:outfourcc]]</code></p>
<dd> Restricts the colorspace for the next filter without doing any conversion. Use together with the scale filter for a real conversion.<br />
 <i>NOTE:</i> For a list of available formats see format=fmt=help.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;fourcc&gt;</p>
<dd> format name like rgb15, bgr24, yv12, etc (default: yuy2)</p>
<dt>&lt;outfourcc&gt;</p>
<dd> Format name that should be substituted for the output. If this is not 100% compatible with the &lt;fourcc&gt; value it will crash.<br />
 Valid examples:<br />
 format=rgb24:bgr24 format=yuyv:yuy2<br />
 Invalid examples (will crash):<br />
 format=rgb24:yv12</dl>
</dl>
<dt><code>noformat[=fourcc]</code></p>
<dd> Restricts the colorspace for the next filter without doing any conversion. Unlike the format filter, this will allow any colorspace <code>except</code> the one you specify.<br />
 <i>NOTE:</i> For a list of available formats see noformat=fmt=help.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;fourcc&gt;</p>
<dd> format name like rgb15, bgr24, yv12, etc (default: yv12)</dl>
</dl>
<dt><code>pp[=filter1[:option1[:option2&#8230;]]/[-]filter2&#8230;] (also see -pphelp)</code></p>
<dd> Enables the specified chain of postprocessing subfilters. Subfilters must be separated by &#8216;/&#8217; and can be disabled by prepending a &#8216;-&#8216;. Each subfilter and some options have a short and a long name that can be used interchangeably, i.e. dr/dering are the same. All subfilters share common options to determine their scope:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a/autoq</p>
<dd> Automatically switch the subfilter off if the CPU is too slow.</p>
<dt>c/chrom</p>
<dd> Do chrominance filtering, too (default).</p>
<dt>y/nochrom</p>
<dd> Do luminance filtering only (no chrominance).</p>
<dt>n/noluma</p>
<dd> Do chrominance filtering only (no luminance).</dl>
</dl>
<dl>
<dt>
<dd>
 <i>NOTE:</i> -pphelp shows a list of available subfilters. </p>
<p> Available subfilters are</dl>
<dl>
<dt>
<dd>
<dl>
<dt>hb/hdeblock[:difference[:flatness]]</p>
<dd> horizontal deblocking filter</p>
<dl>
<dt>
<dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dl>
<dt>vb/vdeblock[:difference[:flatness]]</p>
<dd> vertical deblocking filter</p>
<dl>
<dt>
<dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dl>
<dt>ha/hadeblock[:difference[:flatness]]</p>
<dd> accurate horizontal deblocking filter</p>
<dl>
<dt>
<dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dl>
<dt>va/vadeblock[:difference[:flatness]]</p>
<dd> accurate vertical deblocking filter</p>
<dl>
<dt>
<dd> &lt;difference&gt;: Difference factor where higher values mean more deblocking (default: 32).<br />
 &lt;flatness&gt;: Flatness threshold where lower values mean more deblocking (default: 39).</dl>
<p> The horizontal and vertical deblocking filters share the difference and flatness values so you cannot set different horizontal and vertical thresholds. </p>
<dt>h1/x1hdeblock</p>
<dd> experimental horizontal deblocking filter</p>
<dt>v1/x1vdeblock</p>
<dd> experimental vertical deblocking filter</p>
<dt>dr/dering</p>
<dd> deringing filter</p>
<dt>tn/tmpnoise[:threshold1[:threshold2[:threshold3]]]</p>
<dd> temporal noise reducer</p>
<dl>
<dt>
<dd> &lt;threshold1&gt;: larger -&gt; stronger filtering<br />
 &lt;threshold2&gt;: larger -&gt; stronger filtering<br />
 &lt;threshold3&gt;: larger -&gt; stronger filtering</dl>
<dt>al/autolevels[:f/fullyrange]</p>
<dd> automatic brightness / contrast correction</p>
<dl>
<dt>
<dd> f/fullyrange: Stretch luminance to (0-255).</dl>
<dt>lb/linblenddeint</p>
<dd> Linear blend deinterlacing filter that deinterlaces the given block by filtering all lines with a (1 2 1) filter.</p>
<dt>li/linipoldeint</p>
<dd> Linear interpolating deinterlacing filter that deinterlaces the given block by linearly interpolating every second line.</p>
<dt>ci/cubicipoldeint</p>
<dd> Cubic interpolating deinterlacing filter deinterlaces the given block by cubically interpolating every second line.</p>
<dt>md/mediandeint</p>
<dd> Median deinterlacing filter that deinterlaces the given block by applying a median filter to every second line.</p>
<dt>fd/ffmpegdeint</p>
<dd> FFmpeg deinterlacing filter that deinterlaces the given block by filtering every second line with a (-1 4 2 4 -1) filter.</p>
<dt>l5/lowpass5</p>
<dd> Vertically applied FIR lowpass deinterlacing filter that deinterlaces the given block by filtering all lines with a (-1 2 6 2 -1) filter.</p>
<dt>fq/forceQuant[:quantizer]</p>
<dd> Overrides the quantizer table from the input with the constant quantizer you specify.</p>
<dl>
<dt>
<dd> &lt;quantizer&gt;: quantizer to use</dl>
<dt>de/default</p>
<dd> default pp filter combination (hb:a,vb:a,dr:a)</p>
<dt>fa/fast</p>
<dd> fast pp filter combination (h1:a,v1:a,dr:a)</p>
<dt>ac&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> high quality pp filter combination (ha:a:128:7,va:a,dr:a)</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>-vf pp=hb/vb/dr/al</p>
<dd> horizontal and vertical deblocking, deringing and automatic brightness/:contrast</p>
<dt>-vf pp=de/-al</p>
<dd> default filters without brightness/:contrast correction</p>
<dt>-vf pp=default/tmpnoise:1:2:3</p>
<dd> Enable default filters &amp; temporal denoiser.</p>
<dt>-vf pp=hb:y/vb:a</p>
<dd> Horizontal deblocking on luminance only, and switch vertical deblocking on or off automatically depending on available CPU time.</dl>
</dl>
<dt><code>spp[=quality[:qp[:mode]]]</code></p>
<dd> Simple postprocessing filter that compresses and decompresses the image at several (or &#8211; in the case of quality level 6 &#8211; all) shifts and averages the results.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;quality&gt;</p>
<dd> 0-6 (default: 3)</p>
<dt>&lt;qp&gt;&nbsp;</p>
<dd> Force quantization parameter (default: 0, use QP from video).</p>
<dt>&lt;mode&gt;</p>
<dd> 0: hard thresholding (default)<br />
 1: soft thresholding (better deringing, but blurrier)<br />
 4: like 0, but also use B-frames&#8217; QP (may cause flicker)<br />
 5: like 1, but also use B-frames&#8217; QP (may cause flicker)</dl>
</dl>
<dt><code>uspp[=quality[:qp]]</code></p>
<dd> Ultra simple &amp; slow postprocessing filter that compresses and decompresses the image at several (or &#8211; in the case of quality level 8 &#8211; all) shifts and averages the results. The way this differs from the behavior of spp is that uspp actually encodes &amp; decodes each case with libavcodec Snow, whereas spp uses a simplified intra only 8&#215;8 DCT similar to MJPEG.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;quality&gt;</p>
<dd> 0-8 (default: 3)</p>
<dt>&lt;qp&gt;&nbsp;</p>
<dd> Force quantization parameter (default: 0, use QP from video).</dl>
</dl>
<dt><code>fspp[=quality[:qp[:strength[:bframes]]]]</code></p>
<dd> faster version of the simple postprocessing filter</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;quality&gt;</p>
<dd> 4-5 (equivalent to spp; default: 4)</p>
<dt>&lt;qp&gt;&nbsp;</p>
<dd> Force quantization parameter (default: 0, use QP from video).</p>
<dt>&lt;-15-32&gt;</p>
<dd> Filter strength, lower values mean more details but also more artifacts, while higher values make the image smoother but also blurrier (default: 0 &#8211; PSNR optimal).</p>
<dt>&lt;bframes&gt;</p>
<dd> 0: do not use QP from B-frames (default)<br />
 1: use QP from B-frames too (may cause flicker)</dl>
</dl>
<dt><code>pp7[=qp[:mode]]</code></p>
<dd> Variant of the spp filter, similar to spp=6 with 7 point DCT where only the center sample is used after IDCT.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;qp&gt;&nbsp;</p>
<dd> Force quantization parameter (default: 0, use QP from video).</p>
<dt>&lt;mode&gt;</p>
<dd> 0: hard thresholding<br />
 1: soft thresholding (better deringing, but blurrier)<br />
 2: medium thresholding (default, good results)</dl>
</dl>
<dt><code>qp=equation</code></p>
<dd> quantization parameter (QP) change filter</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;equation&gt;</p>
<dd> some equation like &quot;2+2*sin(PI*qp)&quot;</dl>
</dl>
<dt><code>geq=equation</code></p>
<dd> generic equation change filter</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;equation&gt;</p>
<dd> Some equation, e.g. &#8216;p(W-X\,Y)&#8217; to flip the image horizontally. You can use whitespace to make the equation more readable. There are a couple of constants that can be used in the equation:</p>
<dl>
<dt>
<dd> PI: the number pi<br />
 E: the number e<br />
 X / Y: the coordinates of the current sample<br />
 W / H: width and height of the image<br />
 SW / SH: width/height scale depending on the currently filtered plane, e.g. 1,1 and 0.5,0.5 for YUV 4:2:0.<br />
 p(x,y): returns the value of the pixel at location x/y of the current plane.</dl>
</dl>
</dl>
<dt><code>test&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Generate various test patterns.</p>
<dt><code>rgbtest[=width:height]</code></p>
<dd> Generate an RGB test pattern useful for detecting RGB vs BGR issues. You should see a red, green and blue stripe from top to bottom.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;width&gt;</p>
<dd> Desired width of generated image (default: 0). 0 means width of input image. </p>
<dt>&lt;height&gt;</p>
<dd> Desired height of generated image (default: 0). 0 means height of input image.</dl>
</dl>
<dt><code>lavc[=quality:fps]</code></p>
<dd> Fast software YV12 to MPEG-1 conversion with libavcodec for use with DVB/:DXR3/:IVTV/:V4L2.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;quality&gt;</p>
<dd> 1-31: fixed qscale<br />
 32-: fixed bitrate in kbits</p>
<dt>&lt;fps&gt;</p>
<dd> force output fps (float value) (default: 0, autodetect based on height)</dl>
</dl>
<dt><code>dvbscale[=aspect]</code></p>
<dd> Set up optimal scaling for DVB cards, scaling the x axis in hardware and calculating the y axis scaling in software to keep aspect. Only useful together with expand and scale.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;aspect&gt;</p>
<dd> Control aspect ratio, calculate as DVB_HEIGHT*ASPECTRATIO (default: 576*4/3=768), set it to 576*(16/9)=1024 for a 16:9 TV.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>-vf dvbscale,scale=-1:0,expand=-1:576:-1:-1:1,lavc</p>
<dd> FIXME: Explain what this does.</dl>
</dl>
<dt><code>noise[=luma[u][t|a][h][p]:chroma[u][t|a][h][p]]</code></p>
<dd> Adds noise.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;0-100&gt;</p>
<dd> luma noise</p>
<dt>&lt;0-100&gt;</p>
<dd> chroma noise</p>
<dt>u</p>
<dd> uniform noise (gaussian otherwise)</p>
<dt>t</p>
<dd> temporal noise (noise pattern changes between frames)</p>
<dt>a</p>
<dd> averaged temporal noise (smoother, but a lot slower)</p>
<dt>h</p>
<dd> high quality (slightly better looking, slightly slower)</p>
<dt>p</p>
<dd> mix random noise with a (semi)regular pattern</dl>
</dl>
<dt><code>denoise3d[=luma_spatial:chroma_spatial:luma_tmp:chroma_tmp]</code></p>
<dd> This filter aims to reduce image noise producing smooth images and making still images really still (This should enhance compressibility.).</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;luma_spatial&gt;</p>
<dd> spatial luma strength (default: 4)</p>
<dt>&lt;chroma_spatial&gt;</p>
<dd> spatial chroma strength (default: 3)</p>
<dt>&lt;luma_tmp&gt;</p>
<dd> luma temporal strength (default: 6)</p>
<dt>&lt;chroma_tmp&gt;</p>
<dd> chroma temporal strength (default: luma_tmp*chroma_spatial/luma_spatial)</dl>
</dl>
<dt><code>hqdn3d[=luma_spatial:chroma_spatial:luma_tmp:chroma_tmp]</code></p>
<dd> High precision/:quality version of the denoise3d filter. Parameters and usage are the same.</p>
<dt><code>ow[=depth[:luma_strength[:chroma_strength]]]</code></p>
<dd> Overcomplete Wavelet denoiser.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;depth&gt;</p>
<dd> Larger depth values will denoise lower frequency components more, but slow down filtering (default: 8).</p>
<dt>&lt;luma_strength&gt;</p>
<dd> luma strength (default: 1.0)</p>
<dt>&lt;chroma_strength&gt;</p>
<dd> chroma strength (default: 1.0)</dl>
</dl>
<dt><code>eq[=brightness:contrast] (OBSOLETE)</code></p>
<dd> Software equalizer with interactive controls just like the hardware equalizer, for cards/:drivers that do not support brightness and contrast controls in hardware. Might also be useful with MEncoder, either for fixing poorly captured movies, or for slightly reducing contrast to mask artifacts and get by with lower bitrates.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;-100-100&gt;</p>
<dd> initial brightness</p>
<dt>&lt;-100-100&gt;</p>
<dd> initial contrast</dl>
</dl>
<dt><code>eq2[=gamma:contrast:brightness:saturation:rg:gg:bg:weight]</code></p>
<dd> Alternative software equalizer that uses lookup tables (very slow), allowing gamma correction in addition to simple brightness and contrast adjustment. Note that it uses the same MMX optimized code as -vf eq if all gamma values are 1.0. The parameters are given as floating point values.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;0.1-10&gt;</p>
<dd> initial gamma value (default: 1.0)</p>
<dt>&lt;-2-2&gt;</p>
<dd> initial contrast, where negative values result in a negative image (default: 1.0)</p>
<dt>&lt;-1-1&gt;</p>
<dd> initial brightness (default: 0.0)</p>
<dt>&lt;0-3&gt;</p>
<dd> initial saturation (default: 1.0)</p>
<dt>&lt;0.1-10&gt;</p>
<dd> gamma value for the red component (default: 1.0)</p>
<dt>&lt;0.1-10&gt;</p>
<dd> gamma value for the green component (default: 1.0)</p>
<dt>&lt;0.1-10&gt;</p>
<dd> gamma value for the blue component (default: 1.0)</p>
<dt>&lt;0-1&gt;</p>
<dd> The weight parameter can be used to reduce the effect of a high gamma value on bright image areas, e.g. keep them from getting overamplified and just plain white. A value of 0.0 turns the gamma correction all the way down while 1.0 leaves it at its full strength (default: 1.0).</dl>
</dl>
<dt><code>hue[=hue:saturation]</code></p>
<dd> Software equalizer with interactive controls just like the hardware equalizer, for cards/:drivers that do not support hue and saturation controls in hardware.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;-180-180&gt;</p>
<dd> initial hue (default: 0.0)</p>
<dt>&lt;-100-100&gt;</p>
<dd> initial saturation, where negative values result in a negative chroma (default: 1.0)</dl>
</dl>
<dt><code>halfpack[=f]</code></p>
<dd> Convert planar YUV 4:2:0 to half-height packed 4:2:2, downsampling luma but keeping all chroma samples. Useful for output to low-resolution display devices when hardware downscaling is poor quality or is not available. Can also be used as a primitive luma-only deinterlacer with very low CPU usage.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;f&gt;&nbsp;<wbr>&nbsp;</p>
<dd> By default, halfpack averages pairs of lines when downsampling. Any value different from 0 or 1 gives the default (averaging) behavior.</p>
<dl>
<dt>
<dd> 0: Only use even lines when downsampling.<br />
 1: Only use odd lines when downsampling.</dl>
</dl>
</dl>
<dt><code>ilpack[=mode]</code></p>
<dd> When interlaced video is stored in YUV 4:2:0 formats, chroma interlacing does not line up properly due to vertical downsampling of the chroma channels. This filter packs the planar 4:2:0 data into YUY2 (4:2:2) format with the chroma lines in their proper locations, so that in any given scanline, the luma and chroma data both come from the same field.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;mode&gt;</p>
<dd> Select the sampling mode.</p>
<dl>
<dt>
<dd> 0: nearest-neighbor sampling, fast but incorrect<br />
 1: linear interpolation (default)</dl>
</dl>
</dl>
<dt><code>harddup</code></p>
<dd> Only useful with MEncoder. If harddup is used when encoding, it will force duplicate frames to be encoded in the output. This uses slightly more space, but is necessary for output to MPEG files or if you plan to demux and remux the video stream after encoding. Should be placed at or near the end of the filter chain unless you have a good reason to do otherwise.</p>
<dt><code>softskip</code></p>
<dd> Only useful with MEncoder. Softskip moves the frame skipping (dropping) step of encoding from before the filter chain to some point during the filter chain. This allows filters which need to see all frames (inverse telecine, temporal denoising, etc.) to function properly. Should be placed after the filters which need to see all frames and before any subsequent filters that are CPU-intensive.</p>
<dt><code>decimate[=max:hi:lo:frac]</code></p>
<dd> Drops frames that do not differ greatly from the previous frame in order to reduce framerate. The main use of this filter is for very-low-bitrate encoding (e.g. streaming over dialup modem), but it could in theory be used for fixing movies that were inverse-telecined incorrectly.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;max&gt;</p>
<dd> Sets the maximum number of consecutive frames which can be dropped (if positive), or the minimum interval between dropped frames (if negative).</p>
<dt>&lt;hi&gt;,&lt;lo&gt;,&lt;frac&gt;</p>
<dd> A frame is a candidate for dropping if no 8&#215;8 region differs by more than a threshold of &lt;hi&gt;, and if not more than &lt;frac&gt; portion (1 meaning the whole image) differs by more than a threshold of &lt;lo&gt;. Values of &lt;hi&gt; and &lt;lo&gt; are for 8&#215;8 pixel blocks and represent actual pixel value differences, so a threshold of 64 corresponds to 1 unit of difference for each pixel, or the same spread out differently over the block.</dl>
</dl>
<dt><code>dint[=sense:level]</code></p>
<dd> The drop-deinterlace (dint) filter detects and drops the first from a set of interlaced video frames.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;0.0-1.0&gt;</p>
<dd> relative difference between neighboring pixels (default: 0.1)</p>
<dt>&lt;0.0-1.0&gt;</p>
<dd> What part of the image has to be detected as interlaced to drop the frame (default: 0.15).</dl>
</dl>
<dt><code>lavcdeint (OBSOLETE)</code></p>
<dd> FFmpeg deinterlacing filter, same as -vf pp=fd</p>
<dt><code>lavfi=filtergraph</code></p>
<dd> FFmpeg libavfilter wrapper. <i>filtergraph</i> defines a whole libavfilter graph with one input and one output. See <a rel="nofollow" href="http://www.ffmpeg.org/:libavfilter.html#SEC4">http://www.ffmpeg.org/:libavfilter.html#SEC4</a> for details. </p>
<p> As a special case, if <i>filtergraph</i> is <code>$</code><i>word</i> then the value of the <i>word</i> environment variable is used; this is necessary if commas are present in the graph description, as mplayer uses them as a delimiter between filters. </p>
<p> <i>NOTE:</i> This filter is considered experimental, it may interact strangely with other filters. </p>
<p> <i>EXAMPLE:</i><br />
 overlay=&quot;movie=$small_video, scale=160:120 [ca]; [in] [ca] overlay=16:8&quot; mplayer -vf lavfi=&#8217;$overlay&#8217; $big_video</p>
<dt><code>kerndeint[=thresh[:map[:order[:sharp[:twoway]]]]]</code></p>
<dd> Donald Graft&#8217;s adaptive kernel deinterlacer. Deinterlaces parts of a video if a configurable threshold is exceeded.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;0-255&gt;</p>
<dd> threshold (default: 10)</p>
<dt>&lt;map&gt;</p>
<dd>
<dl>
<dt>
<dd> 0: Ignore pixels exceeding the threshold (default).<br />
 1: Paint pixels exceeding the threshold white.</dl>
<dt>&lt;order&gt;</p>
<dd>
<dl>
<dt>
<dd> 0: Leave fields alone (default).<br />
 1: Swap fields.</dl>
<dt>&lt;sharp&gt;</p>
<dd>
<dl>
<dt>
<dd> 0: Disable additional sharpening (default).<br />
 1: Enable additional sharpening.</dl>
<dt>&lt;twoway&gt;</p>
<dd>
<dl>
<dt>
<dd> 0: Disable twoway sharpening (default).<br />
 1: Enable twoway sharpening.</dl>
</dl>
</dl>
<dt><code>unsharp[=l|cWxH:amount[:l|cWxH:amount]]</code></p>
<dd> unsharp mask / gaussian blur</p>
<dl>
<dt>
<dd>
<dl>
<dt>l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Apply effect on luma component.</p>
<dt>c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Apply effect on chroma components.</p>
<dt>&lt;width&gt;x&lt;height&gt;</p>
<dd> width and height of the matrix, odd sized in both directions (min = 3&#215;3, max = 13&#215;11 or 11&#215;13, usually something between 3&#215;3 and 7&#215;7)</p>
<dt>amount</p>
<dd> Relative amount of sharpness/:blur to add to the image (a sane range should be -1.5-1.5).</p>
<dl>
<dt>
<dd> &lt;0: blur<br />
 &gt;0: sharpen</dl>
</dl>
</dl>
<dt><code>swapuv&nbsp;</code></p>
<dd> Swap U &amp; V plane.</p>
<dt><code>il[=d|i][s][:[d|i][s]]</code></p>
<dd> (De)interleaves lines. The goal of this filter is to add the ability to process interlaced images pre-field without deinterlacing them. You can filter your interlaced DVD and play it on a TV without breaking the interlacing. While deinterlacing (with the postprocessing filter) removes interlacing permanently (by smoothing, averaging, etc) deinterleaving splits the frame into 2 fields (so called half pictures), so you can process (filter) them independently and then re-interleave them.</p>
<dl>
<dt>
<dd>
<dl>
<dt>d</p>
<dd> deinterleave (placing one above the other)</p>
<dt>i</p>
<dd> interleave</p>
<dt>s</p>
<dd> swap fields (exchange even &amp; odd lines)</dl>
</dl>
<dt><code>fil[=i|d]</code></p>
<dd> (De)interleaves lines. This filter is very similar to the il filter but much faster, the main disadvantage is that it does not always work. Especially if combined with other filters it may produce randomly messed up images, so be happy if it works but do not complain if it does not for your combination of filters.</p>
<dl>
<dt>
<dd>
<dl>
<dt>d</p>
<dd> Deinterleave fields, placing them side by side.</p>
<dt>i</p>
<dd> Interleave fields again (reversing the effect of fil=d).</dl>
</dl>
<dt><code>field[=n]</code></p>
<dd> Extracts a single field from an interlaced image using stride arithmetic to avoid wasting CPU time. The optional argument n specifies whether to extract the even or the odd field (depending on whether n is even or odd).</p>
<dt><code>detc[=var1=value1:var2=value2:&#8230;]</code></p>
<dd> Attempts to reverse the &#8216;telecine&#8217; process to recover a clean, non-interlaced stream at film framerate. This was the first and most primitive inverse telecine filter to be added to MPlayer/:MEncoder. It works by latching onto the telecine 3:2 pattern and following it as long as possible. This makes it suitable for perfectly-telecined material, even in the presence of a fair degree of noise, but it will fail in the presence of complex post-telecine edits. Development on this filter is no longer taking place, as ivtc, pullup, and filmdint are better for most applications. The following arguments (see syntax above) may be used to control detc&#8217;s behavior:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;dr&gt;&nbsp;</p>
<dd> Set the frame dropping mode.</p>
<dl>
<dt>
<dd> 0: Do not drop frames to maintain fixed output framerate (default).<br />
 1: Always drop a frame when there have been no drops or telecine merges in the past 5 frames.<br />
 2: Always maintain exact 5:4 input to output frame ratio.<br />
 <i>NOTE:</i> Use mode 1 or 2 with MEncoder.</dl>
<dt>&lt;am&gt;&nbsp;</p>
<dd> Analysis mode.</p>
<dl>
<dt>
<dd> 0: Fixed pattern with initial frame number specified by &lt;fr&gt;.<br />
 1: aggressive search for telecine pattern (default)</dl>
<dt>&lt;fr&gt;&nbsp;</p>
<dd> Set initial frame number in sequence. 0-2 are the three clean progressive frames; 3 and 4 are the two interlaced frames. The default, -1, means &#8216;not in telecine sequence&#8217;. The number specified here is the type for the imaginary previous frame before the movie starts.</p>
<dt>&lt;t0&gt;, &lt;t1&gt;, &lt;t2&gt;, &lt;t3&gt;</p>
<dd> Threshold values to be used in certain modes.</dl>
</dl>
<dt><code>ivtc[=1]</code></p>
<dd> Experimental &#8216;stateless&#8217; inverse telecine filter. Rather than trying to lock on to a pattern like the detc filter does, ivtc makes its decisions independently for each frame. This will give much better results for material that has undergone heavy editing after telecine was applied, but as a result it is not as forgiving of noisy input, for example TV capture. The optional parameter (ivtc=1) corresponds to the dr=1 option for the detc filter, and should be used with MEncoder but not with MPlayer. As with detc, you must specify the correct output framerate (-ofps 24000/1001) when using MEncoder. Further development on ivtc has stopped, as the pullup and filmdint filters appear to be much more accurate.</p>
<dt><code>pullup[=jl:jr:jt:jb:sb:mp]</code></p>
<dd> Third-generation pulldown reversal (inverse telecine) filter, capable of handling mixed hard-telecine, 24000/1001 fps progressive, and 30000/1001 fps progressive content. The pullup filter is designed to be much more robust than detc or ivtc, by taking advantage of future context in making its decisions. Like ivtc, pullup is stateless in the sense that it does not lock onto a pattern to follow, but it instead looks forward to the following fields in order to identify matches and rebuild progressive frames. It is still under development, but believed to be quite accurate.</p>
<dl>
<dt>
<dd>
<dl>
<dt>jl, jr, jt, and jb</p>
<dd> These options set the amount of &quot;junk&quot; to ignore at the left, right, top, and bottom of the image, respectively. Left/:right are in units of 8 pixels, while top/:bottom are in units of 2 lines. The default is 8 pixels on each side. </p>
<dt>sb (strict breaks)</p>
<dd> Setting this option to 1 will reduce the chances of pullup generating an occasional mismatched frame, but it may also cause an excessive number of frames to be dropped during high motion sequences. Conversely, setting it to -1 will make pullup match fields more easily. This may help processing of video where there is slight blurring between the fields, but may also cause there to be interlaced frames in the output. </p>
<dt>mp (metric plane)</p>
<dd> This option may be set to 1 or 2 to use a chroma plane instead of the luma plane for doing pullup&#8217;s computations. This may improve accuracy on very clean source material, but more likely will decrease accuracy, especially if there is chroma noise (rainbow effect) or any grayscale video. The main purpose of setting mp to a chroma plane is to reduce CPU load and make pullup usable in realtime on slow machines.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>NOTE:</i> Always follow pullup with the softskip filter when encoding to ensure that pullup is able to see each frame. Failure to do so will lead to incorrect output and will usually crash, due to design limitations in the codec/:filter layer.</dl>
<dt><code>filmdint[=options]</code></p>
<dd> Inverse telecine filter, similar to the pullup filter above. It is designed to handle any pulldown pattern, including mixed soft and hard telecine and limited support for movies that are slowed down or sped up from their original framerate for TV. Only the luma plane is used to find the frame breaks. If a field has no match, it is deinterlaced with simple linear approximation. If the source is MPEG-2, this must be the first filter to allow access to the field-flags set by the MPEG-2 decoder. Depending on the source MPEG, you may be fine ignoring this advice, as long as you do not see lots of &quot;Bottom-first field&quot; warnings. With no options it does normal inverse telecine, and should be used together with mencoder -fps 30000/1001 -ofps 24000/1001. When this filter is used with MPlayer, it will result in an uneven framerate during playback, but it is still generally better than using pp=lb or no deinterlacing at all. Multiple options can be specified separated by /.</p>
<dl>
<dt>
<dd>
<dl>
<dt>crop=&lt;w&gt;:&lt;h&gt;:&lt;x&gt;:&lt;y&gt;</p>
<dd> Just like the crop filter, but faster, and works on mixed hard and soft telecined content as well as when y is not a multiple of 4. If x or y would require cropping fractional pixels from the chroma planes, the crop area is extended. This usually means that x and y must be even.</p>
<dt>io=&lt;ifps&gt;:&lt;ofps&gt;</p>
<dd> For each ifps input frames the filter will output ofps frames. The ratio of ifps/:ofps should match the -fps/-ofps ratio. This could be used to filter movies that are broadcast on TV at a frame rate different from their original framerate.</p>
<dt>luma_only=&lt;n&gt;</p>
<dd> If n is nonzero, the chroma plane is copied unchanged. This is useful for YV12 sampled TV, which discards one of the chroma fields.</p>
<dt>mmx2=&lt;n&gt;</p>
<dd> On x86, if n=1, use MMX2 optimized functions, if n=2, use 3DNow! optimized functions, otherwise, use plain C. If this option is not specified, MMX2 and 3DNow! are auto-detected, use this option to override auto-detection.</p>
<dt>fast=&lt;n&gt;</p>
<dd> The larger n will speed up the filter at the expense of accuracy. The default value is n=3. If n is odd, a frame immediately following a frame marked with the REPEAT_FIRST_FIELD MPEG flag is assumed to be progressive, thus filter will not spend any time on soft-telecined MPEG-2 content. This is the only effect of this flag if MMX2 or 3DNow! is available. Without MMX2 and 3DNow, if n=0 or 1, the same calculations will be used as with n=2 or 3. If n=2 or 3, the number of luma levels used to find the frame breaks is reduced from 256 to 128, which results in a faster filter without losing much accuracy. If n=4 or 5, a faster, but much less accurate metric will be used to find the frame breaks, which is more likely to misdetect high vertical detail as interlaced content.</p>
<dt>verbose=&lt;n&gt;</p>
<dd> If n is nonzero, print the detailed metrics for each frame. Useful for debugging.</p>
<dt>dint_thres=&lt;n&gt;</p>
<dd> Deinterlace threshold. Used during de-interlacing of unmatched frames. Larger value means less deinterlacing, use n=256 to completely turn off deinterlacing. Default is n=8.</p>
<dt>comb_thres=&lt;n&gt;</p>
<dd> Threshold for comparing a top and bottom fields. Defaults to 128.</p>
<dt>diff_thres=&lt;n&gt;</p>
<dd> Threshold to detect temporal change of a field. Default is 128.</p>
<dt>sad_thres=&lt;n&gt;</p>
<dd> Sum of Absolute Difference threshold, default is 64.</dl>
</dl>
<dt><code>softpulldown</code></p>
<dd> This filter works only correct with MEncoder and acts on the MPEG-2 flags used for soft 3:2 pulldown (soft telecine). If you want to use the ivtc or detc filter on movies that are partly soft telecined, inserting this filter before them should make them more reliable.</p>
<dt><code>divtc[=options]</code></p>
<dd> Inverse telecine for deinterlaced video. If 3:2-pulldown telecined video has lost one of the fields or is deinterlaced using a method that keeps one field and interpolates the other, the result is a juddering video that has every fourth frame duplicated. This filter is intended to find and drop those duplicates and restore the original film framerate. When using this filter, you must specify -ofps that is 4/5 of the fps of the input file and place the softskip later in the filter chain to make sure that divtc sees all the frames. Two different modes are available: One pass mode is the default and is straightforward to use, but has the disadvantage that any changes in the telecine phase (lost frames or bad edits) cause momentary judder until the filter can resync again. Two pass mode avoids this by analyzing the whole video beforehand so it will have forward knowledge about the phase changes and can resync at the exact spot. These passes do <code>not</code> correspond to pass one and two of the encoding process. You must run an extra pass using divtc pass one before the actual encoding throwing the resulting video away. Use -nosound -ovc raw -o /dev/null to avoid wasting CPU power for this pass. You may add something like crop=2:2:0:0 after divtc to speed things up even more. Then use divtc pass two for the actual encoding. If you use multiple encoder passes, use divtc pass two for all of them. The options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>pass=1|2</p>
<dd> Use two pass mode.</p>
<dt>file=&lt;filename&gt;</p>
<dd> Set the two pass log filename (default: &quot;framediff.log&quot;).</p>
<dt>threshold=&lt;value&gt;</p>
<dd> Set the minimum strength the telecine pattern must have for the filter to believe in it (default: 0.5). This is used to avoid recognizing false pattern from the parts of the video that are very dark or very still.</p>
<dt>window=&lt;numframes&gt;</p>
<dd> Set the number of past frames to look at when searching for pattern (default: 30). Longer window improves the reliability of the pattern search, but shorter window improves the reaction time to the changes in the telecine phase. This only affects the one pass mode. The two pass mode currently uses fixed window that extends to both future and past.</p>
<dt>phase=0|1|2|3|4</p>
<dd> Sets the initial telecine phase for one pass mode (default: 0). The two pass mode can see the future, so it is able to use the correct phase from the beginning, but one pass mode can only guess. It catches the correct phase when it finds it, but this option can be used to fix the possible juddering at the beginning. The first pass of the two pass mode also uses this, so if you save the output from the first pass, you get constant phase result.</p>
<dt>deghost=&lt;value&gt;</p>
<dd> Set the deghosting threshold (0-255 for one pass mode, -255-255 for two pass mode, default 0). If nonzero, deghosting mode is used. This is for video that has been deinterlaced by blending the fields together instead of dropping one of the fields. Deghosting amplifies any compression artifacts in the blended frames, so the parameter value is used as a threshold to exclude those pixels from deghosting that differ from the previous frame less than specified value. If two pass mode is used, then negative value can be used to make the filter analyze the whole video in the beginning of pass-2 to determine whether it needs deghosting or not and then select either zero or the absolute value of the parameter. Specify this option for pass-2, it makes no difference on pass-1.</dl>
</dl>
<dt><code>phase[=t|b|p|a|u|T|B|A|U][:v]</code></p>
<dd> Delay interlaced video by one field time so that the field order changes. The intended use is to fix PAL movies that have been captured with the opposite field order to the film-to-video transfer. The options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>t</p>
<dd> Capture field order top-first, transfer bottom-first. Filter will delay the bottom field.</p>
<dt>b</p>
<dd> Capture bottom-first, transfer top-first. Filter will delay the top field.</p>
<dt>p</p>
<dd> Capture and transfer with the same field order. This mode only exists for the documentation of the other options to refer to, but if you actually select it, the filter will faithfully do nothing ;-)</p>
<dt>a</p>
<dd> Capture field order determined automatically by field flags, transfer opposite. Filter selects among t and b modes on a frame by frame basis using field flags. If no field information is available, then this works just like u.</p>
<dt>u</p>
<dd> Capture unknown or varying, transfer opposite. Filter selects among t and b on a frame by frame basis by analyzing the images and selecting the alternative that produces best match between the fields.</p>
<dt>T</p>
<dd> Capture top-first, transfer unknown or varying. Filter selects among t and p using image analysis.</p>
<dt>B</p>
<dd> Capture bottom-first, transfer unknown or varying. Filter selects among b and p using image analysis.</p>
<dt>A</p>
<dd> Capture determined by field flags, transfer unknown or varying. Filter selects among t, b and p using field flags and image analysis. If no field information is available, then this works just like U. This is the default mode.</p>
<dt>U</p>
<dd> Both capture and transfer unknown or varying. Filter selects among t, b and p using image analysis only.</p>
<dt>v</p>
<dd> Verbose operation. Prints the selected mode for each frame and the average squared difference between fields for t, b, and p alternatives.</dl>
</dl>
<dt><code>telecine[=start]</code></p>
<dd> Apply 3:2 &#8216;telecine&#8217; process to increase framerate by 20%. This most likely will not work correctly with MPlayer, but it can be used with &#8216;mencoder -fps 30000/1001 -ofps 30000/1001 -vf telecine&#8217;. Both fps options are essential! (A/V sync will break if they are wrong.) The optional start parameter tells the filter where in the telecine pattern to start (0-3).</p>
<dt><code>tinterlace[=mode]</code></p>
<dd> Temporal field interlacing &#8211; merge pairs of frames into an interlaced frame, halving the framerate. Even frames are moved into the upper field, odd frames to the lower field. This can be used to fully reverse the effect of the tfields filter (in mode 0). Available modes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Move odd frames into the upper field, even into the lower field, generating a full-height frame at half framerate.</p>
<dt>1</p>
<dd> Only output odd frames, even frames are dropped; height unchanged.</p>
<dt>2</p>
<dd> Only output even frames, odd frames are dropped; height unchanged.</p>
<dt>3</p>
<dd> Expand each frame to full height, but pad alternate lines with black; framerate unchanged.</p>
<dt>4</p>
<dd> Interleave even lines from even frames with odd lines from odd frames. Height unchanged at half framerate.</dl>
</dl>
<dt><code>tfields[=mode[:field_dominance]]</code></p>
<dd> Temporal field separation &#8211; split fields into frames, doubling the output framerate. Like the telecine filter, tfields might not work completely right unless used with MEncoder and both -fps and -ofps set to the desired (double) framerate!</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;mode&gt;</p>
<dd> 0: Leave fields unchanged (will jump/:flicker).<br />
 1: Interpolate missing lines. (The algorithm used might not be so good.)<br />
 2: Translate fields by 1/4 pixel with linear interpolation (no jump).<br />
 4: Translate fields by 1/4 pixel with 4tap filter (higher quality) (default).</p>
<dt>&lt;field_dominance&gt;&nbsp;(DEPRECATED)</p>
<dd> -1: auto (default) Only works if the decoder exports the appropriate information and no other filters which discard that information come before tfields in the filter chain, otherwise it falls back to 0 (top field first).<br />
 0: top field first<br />
 1: bottom field first<br />
 <i>NOTE:</i> This option will possibly be removed in a future version. Use -field-dominance instead.</dl>
</dl>
<dt><code>yadif=[mode[:field_dominance]]</code></p>
<dd> Yet another deinterlacing filter</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;mode&gt;</p>
<dd> 0: Output 1 frame for each frame.<br />
 1: Output 1 frame for each field.<br />
 2: Like 0 but skips spatial interlacing check.<br />
 3: Like 1 but skips spatial interlacing check.</p>
<dt>&lt;field_dominance&gt;&nbsp;(DEPRECATED)</p>
<dd> Operates like tfields.<br />
 <i>NOTE:</i> This option will possibly be removed in a future version. Use -field-dominance instead.</dl>
</dl>
<dt><code>mcdeint=[mode[:parity[:qp]]]</code></p>
<dd> Motion compensating deinterlacer. It needs one field per frame as input and must thus be used together with tfields=1 or yadif=1/3 or equivalent.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;mode&gt;</p>
<dd> 0: fast<br />
 1: medium<br />
 2: slow, iterative motion estimation<br />
 3: extra slow, like 2 plus multiple reference frames</p>
<dt>&lt;parity&gt;</p>
<dd> 0 or 1 selects which field to use (note: no autodetection yet!).</p>
<dt>&lt;qp&gt;&nbsp;</p>
<dd> Higher values should result in a smoother motion vector field but less optimal individual vectors.</dl>
</dl>
<dt><code>boxblur=radius:power[:radius:power]</code></p>
<dd> box blur</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;radius&gt;</p>
<dd> blur filter strength</p>
<dt>&lt;power&gt;</p>
<dd> number of filter applications</dl>
</dl>
<dt><code>sab=radius:pf:colorDiff[:radius:pf:colorDiff]</code></p>
<dd> shape adaptive blur</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;radius&gt;</p>
<dd> blur filter strength (~0.1-4.0) (slower if larger)</p>
<dt>&lt;pf&gt;&nbsp;</p>
<dd> prefilter strength (~0.1-2.0)</p>
<dt>&lt;colorDiff&gt;</p>
<dd> maximum difference between pixels to still be considered (~0.1-100.0)</dl>
</dl>
<dt><code>smartblur=radius:strength:threshold[:radius:strength:threshold]</code></p>
<dd> smart blur</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;radius&gt;</p>
<dd> blur filter strength (~0.1-5.0) (slower if larger)</p>
<dt>&lt;strength&gt;</p>
<dd> blur (0.0-1.0) or sharpen (-1.0-0.0)</p>
<dt>&lt;threshold&gt;</p>
<dd> filter all (0), filter flat areas (0-30) or filter edges (-30-0)</dl>
</dl>
<dt><code>perspective=x0:y0:x1:y1:x2:y2:x3:y3:t</code></p>
<dd> Correct the perspective of movies not filmed perpendicular to the screen.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;x0&gt;,&lt;y0&gt;,&#8230;</p>
<dd> coordinates of the top left, top right, bottom left, bottom right corners</p>
<dt>&lt;t&gt;&nbsp;<wbr>&nbsp;</p>
<dd> linear (0) or cubic resampling (1)</dl>
</dl>
<dt><code>2xsai&nbsp;<wbr>&nbsp;</code></p>
<dd> Scale and smooth the image with the 2x scale and interpolate algorithm.</p>
<dt><code>1bpp&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> 1bpp bitmap to YUV/:BGR 8/:15/:16/:32 conversion</p>
<dt><code>down3dright[=lines]</code></p>
<dd> Reposition and resize stereoscopic images. Extracts both stereo fields and places them side by side, resizing them to maintain the original movie aspect.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;lines&gt;</p>
<dd> number of lines to select from the middle of the image (default: 12)</dl>
</dl>
<dt><code>bmovl=hidden:opaque:fifo</code></p>
<dd> The bitmap overlay filter reads bitmaps from a FIFO and displays them on top of the movie, allowing some transformations on the image. Also see TOOLS/bmovl-test.c for a small bmovl test program.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;hidden&gt;</p>
<dd> Set the default value of the &#8216;hidden&#8217; flag (0=visible, 1=hidden).</p>
<dt>&lt;opaque&gt;</p>
<dd> Set the default value of the &#8216;opaque&#8217; flag (0=transparent, 1=opaque).</p>
<dt>&lt;fifo&gt;</p>
<dd> path/:filename for the FIFO (named pipe connecting &#8216;mplayer -vf bmovl&#8217; to the controlling application)</dl>
</dl>
<dl>
<dt>
<dd> FIFO commands are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>RGBA32 width height xpos ypos alpha clear</p>
<dd> followed by width*height*4 Bytes of raw RGBA32 data.</p>
<dt>ABGR32 width height xpos ypos alpha clear</p>
<dd> followed by width*height*4 Bytes of raw ABGR32 data.</p>
<dt>RGB24 width height xpos ypos alpha clear</p>
<dd> followed by width*height*3 Bytes of raw RGB24 data.</p>
<dt>BGR24 width height xpos ypos alpha clear</p>
<dd> followed by width*height*3 Bytes of raw BGR24 data.</p>
<dt>ALPHA width height xpos ypos alpha</p>
<dd> Change alpha transparency of the specified area.</p>
<dt>CLEAR width height xpos ypos</p>
<dd> Clear area.</p>
<dt>OPAQUE</p>
<dd> Disable all alpha transparency. Send &quot;ALPHA 0 0 0 0 0&quot; to enable it again.</p>
<dt>HIDE&nbsp;</p>
<dd> Hide bitmap.</p>
<dt>SHOW&nbsp;</p>
<dd> Show bitmap.</dl>
</dl>
<dl>
<dt>
<dd> Arguments are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;width&gt;, &lt;height&gt;</p>
<dd> image/area size</p>
<dt>&lt;xpos&gt;, &lt;ypos&gt;</p>
<dd> Start blitting at position x/y.</p>
<dt>&lt;alpha&gt;</p>
<dd> Set alpha difference. If you set this to -255 you can then send a sequence of ALPHA-commands to set the area to -225, -200, -175 etc for a nice fade-in-effect! ;)</p>
<dl>
<dt>
<dd> 0: same as original<br />
 255: Make everything opaque.<br />
 -255: Make everything transparent.</dl>
<dt>&lt;clear&gt;</p>
<dd> Clear the framebuffer before blitting.</p>
<dl>
<dt>
<dd> 0: The image will just be blitted on top of the old one, so you do not need to send 1.8MB of RGBA32 data every time a small part of the screen is updated.<br />
 1: clear</dl>
</dl>
</dl>
<dt><code>framestep=I|[i]step</code></p>
<dd> Renders only every nth frame or every intra frame (keyframe). </p>
<p> If you call the filter with I (uppercase) as the parameter, then <code>only</code> keyframes are rendered. For DVDs it generally means one in every 15/12 frames (IBBPBBPBBPBBPBB), for AVI it means every scene change or every keyint value (see -lavcopts keyint= value if you use MEncoder to encode the video). </p>
<p> When a keyframe is found, an &#8216;I!&#8217; string followed by a newline character is printed, leaving the current line of MPlayer/:MEncoder output on the screen, because it contains the time (in seconds) and frame number of the keyframe (You can use this information to split the AVI.). </p>
<p> If you call the filter with a numeric parameter &#8216;step&#8217; then only one in every &#8216;step&#8217; frames is rendered. </p>
<p> If you put an &#8216;i&#8217; (lowercase) before the number then an &#8216;I!&#8217; is printed (like the I parameter). </p>
<p> If you give only the i then nothing is done to the frames, only I! is printed.</p>
<dt><code>tile=xtiles:ytiles:output:start:delta</code></p>
<dd> Tile a series of images into a single, bigger image. If you omit a parameter or use a value less than 0, then the default value is used. You can also stop when you are satisfied (&#8230; -vf tile=10:5 &#8230;). It is probably a good idea to put the scale filter before the tile :-) </p>
<p> The parameters are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;xtiles&gt;</p>
<dd> number of tiles on the x axis (default: 5)</p>
<dt>&lt;ytiles&gt;</p>
<dd> number of tiles on the y axis (default: 5)</p>
<dt>&lt;output&gt;</p>
<dd> Render the tile when &#8216;output&#8217; number of frames are reached, where &#8216;output&#8217; should be a number less than xtile * ytile. Missing tiles are left blank. You could, for example, write an 8 * 7 tile every 50 frames to have one image every 2 seconds @ 25 fps.</p>
<dt>&lt;start&gt;</p>
<dd> outer border thickness in pixels (default: 2)</p>
<dt>&lt;delta&gt;</p>
<dd> inner border thickness in pixels (default: 4)</dl>
</dl>
<dt><code>delogo[=x:y:w:h:t]</code></p>
<dd> Suppresses a TV station logo by a simple interpolation of the surrounding pixels. Just set a rectangle covering the logo and watch it disappear (and sometimes something even uglier appear &#8211; your mileage may vary).</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;x&gt;,&lt;y&gt;</p>
<dd> top left corner of the logo</p>
<dt>&lt;w&gt;,&lt;h&gt;</p>
<dd> width and height of the cleared rectangle</p>
<dt>&lt;t&gt;</p>
<dd> Thickness of the fuzzy edge of the rectangle (added to w and h). When set to -1, a green rectangle is drawn on the screen to simplify finding the right x,y,w,h parameters.</p>
<dt>file=&lt;file&gt;</p>
<dd> You can specify a text file to load the coordinates from. Each line must have a timestamp (in seconds, and in ascending order) and the &quot;x:y:w:h:t&quot; coordinates (t can be omitted).</dl>
</dl>
<dt><code>remove-logo=/path/to/logo_bitmap_file_name.pgm</code></p>
<dd> Suppresses a TV station logo, using a PGM or PPM image file to determine which pixels comprise the logo. The width and height of the image file must match those of the video stream being processed. Uses the filter image and a circular blur algorithm to remove the logo.</p>
<dl>
<dt>
<dd>
<dl>
<dt>/path/to/logo_bitmap_file_name.pgm</p>
<dd> [path] + filename of the filter image.</dl>
</dl>
<dt><code>zrmjpeg[=options]</code></p>
<dd> Software YV12 to MJPEG encoder for use with the zr2 video output device.</p>
<dl>
<dt>
<dd>
<dl>
<dt>maxheight=&lt;h&gt;|maxwidth=&lt;w&gt;</p>
<dd> These options set the maximum width and height the zr card can handle (the MPlayer filter layer currently cannot query those).</p>
<dt>{dc10+,dc10,buz,lml33}-{PAL|NTSC}</p>
<dd> Use these options to set maxwidth and maxheight automatically to the values known for card/:mode combo. For example, valid options are: dc10-PAL and buz-NTSC (default: dc10+PAL)</p>
<dt>color|bw</p>
<dd> Select color or black and white encoding. Black and white encoding is faster. Color is the default.</p>
<dt>hdec={1,2,4}</p>
<dd> Horizontal decimation 1, 2 or 4.</p>
<dt>vdec={1,2,4}</p>
<dd> Vertical decimation 1, 2 or 4.</p>
<dt>quality=1-20</p>
<dd> Set JPEG compression quality [BEST] 1 &#8211; 20 [VERY BAD].</p>
<dt>fd|nofd</p>
<dd> By default, decimation is only performed if the Zoran hardware can upscale the resulting MJPEG images to the original size. The option fd instructs the filter to always perform the requested decimation (ugly).</dl>
</dl>
<dt><code>screenshot=prefix</code></p>
<dd> Allows acquiring screenshots of the movie using slave mode commands that can be bound to keypresses. See the slave mode documentation and the INTERACTIVE CONTROL section for details. By default files named &#8216;shotNNNN.png&#8217; will be saved in the working directory, using the first available number &#8211; no files will be overwritten. Specify a prefix to change the name or location, e.g. -vf screenshot=shots/now will save the files in the directory shots with nowNNNN.png as name. The filter has no overhead when not used and accepts an arbitrary colorspace, so it is safe to add it to the configuration file. Make sure that the screenshot filter is added after all other filters whose effect you want to record on the saved image. E.g. it should be the last filter if you want to have an exact screenshot of what you see on the monitor.</p>
<dt><code>ass&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Moves SSA/ASS subtitle rendering to an arbitrary point in the filter chain. Only useful with the -ass option. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-vf ass,screenshot</p>
<dd> Moves SSA/ASS rendering before the screenshot filter. Screenshots taken this way will contain subtitles.</dl>
</dl>
<dt><code>blackframe[=amount:threshold]</code></p>
<dd> Detect frames that are (almost) completely black. Can be useful to detect chapter transitions or commercials. Output lines consist of the frame number of the detected frame, the percentage of blackness, the frame type and the frame number of the last encountered keyframe.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;amount&gt;</p>
<dd> Percentage of the pixels that have to be below the threshold (default: 98).</p>
<dt>&lt;threshold&gt;</p>
<dd> Threshold below which a pixel value is considered black (default: 32).</dl>
</dl>
<dt><code>stereo3d[=in:out]</code></p>
<dd> Stereo3d converts between different stereoscopic image formats.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;in&gt;</p>
<dd> Stereoscopic image format of input. Possible values:</p>
<dl>
<dt>
<dd> <code>sbsl or side_by_side_left_first</code></p>
<dl>
<dt>
<dd> side by side parallel (left eye left, right eye right)</dl>
<p> <code>sbsr or side_by_side_right_first</code></p>
<dl>
<dt>
<dd> side by side crosseye (right eye left, left eye right)</dl>
<p> <code>sbs2l or side_by_side_half_width_left_first</code></p>
<dl>
<dt>
<dd> side by side with half width resolution (left eye left, right eye right)</dl>
<p> <code>sbs2r or side_by_side_half_width_right_first</code></p>
<dl>
<dt>
<dd> side by side with half width resolution (right eye left, left eye right)</dl>
<p> <code>abl or above_below_left_first</code></p>
<dl>
<dt>
<dd> above-below (left eye above, right eye below)</dl>
<p> <code>abl or above_below_right_first</code></p>
<dl>
<dt>
<dd> above-below (right eye above, left eye below)</dl>
<p> <code>ab2l or above_below_half_height_left_first</code></p>
<dl>
<dt>
<dd> above-below with half height resolution (left eye above, right eye below)</dl>
<p> <code>ab2r or above_below_half_height_right_first</code></p>
<dl>
<dt>
<dd> above-below with half height resolution (right eye above, left eye below)</dl>
</dl>
<dt>&lt;out&gt;</p>
<dd> Stereoscopic image format of output. Possible values are all the input formats as well as:</p>
<dl>
<dt>
<dd> <code>arcg or anaglyph_red_cyan_gray</code></p>
<dl>
<dt>
<dd> anaglyph red/cyan gray (red filter on left eye, cyan filter on right eye)</dl>
<p> <code>arch or anaglyph_red_cyan_half_color</code></p>
<dl>
<dt>
<dd> anaglyph red/cyan half colored (red filter on left eye, cyan filter on right eye)</dl>
<p> <code>arcc or anaglyph_red_cyan_color</code></p>
<dl>
<dt>
<dd> anaglyph red/cyan color (red filter on left eye, cyan filter on right eye)</dl>
<p> <code>arcd or anaglyph_red_cyan_dubois</code></p>
<dl>
<dt>
<dd> anaglyph red/cyan color optimized with the least squares projection of dubois (red filter on left eye, cyan filter on right eye)</dl>
<p> <code>agmg or anaglyph_green_magenta_gray</code></p>
<dl>
<dt>
<dd> anaglyph green/magenta gray (green filter on left eye, magenta filter on right eye)</dl>
<p> <code>agmh or anaglyph_green_magenta_half_color</code></p>
<dl>
<dt>
<dd> anaglyph green/magenta half colored (green filter on left eye, magenta filter on right eye)</dl>
<p> <code>agmc or anaglyph_green_magenta_color</code></p>
<dl>
<dt>
<dd> anaglyph green/magenta colored (green filter on left eye, magenta filter on right eye)</dl>
<p> <code>aybg or anaglyph_yellow_blue_gray</code></p>
<dl>
<dt>
<dd> anaglyph yellow/blue gray (yellow filter on left eye, blue filter on right eye)</dl>
<p> <code>aybh or anaglyph_yellow_blue_half_color</code></p>
<dl>
<dt>
<dd> anaglyph yellow/blue half colored (yellow filter on left eye, blue filter on right eye)</dl>
<p> <code>aybc or anaglyph_yellow_blue_color</code></p>
<dl>
<dt>
<dd> anaglyph yellow/blue colored (yellow filter on left eye, blue filter on right eye)</dl>
<p> <code>irl or interleave_rows_left_first</code></p>
<dl>
<dt>
<dd> Interleaved rows (left eye has top row, right eye starts on next row)</dl>
<p> <code>irr or interleave_rows_right_first</code></p>
<dl>
<dt>
<dd> Interleaved rows (right eye has top row, left eye starts on next row)</dl>
<p> <code>ml or mono_left</code></p>
<dl>
<dt>
<dd> mono output (left eye only)</dl>
<p> <code>mr or mono_right</code></p>
<dl>
<dt>
<dd> mono output (right eye only)</dl>
</dl>
<p> <i>NOTE:</i> To use either of the interleaved-rows output formats to display full-screen on a row-interleaved 3D display, you will need to scale the video to the correct height first using the &quot;scale&quot; filter, if it is not already the right height. Typically, that is 1080 rows (so use e.g. &quot;-vf scale=1440:1080,stereo3d=sbsl:irl&quot; for a 720p side-by-side encoded movie).</dl>
</dl>
<dt><code>gradfun[=strength[:radius]]</code></p>
<dd> Fix the banding artifacts that are sometimes introduced into nearly flat regions by truncation to 8bit colordepth. Interpolates the gradients that should go where the bands are, and dithers them. </p>
<p> This filter is designed for playback only. Do not use it prior to lossy compression, because compression tends to lose the dither and bring back the bands.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;strength&gt;</p>
<dd> Maximum amount by which the filter will change any one pixel. Also the threshold for detecting nearly flat regions (default: 1.2).</p>
<dt>&lt;radius&gt;</p>
<dd> Neighborhood to fit the gradient to. Larger radius makes for smoother gradients, but also prevents the filter from modifying pixels near detailed regions (default: 16).</dl>
</dl>
<dt><code>fixpts[=options]</code></p>
<dd> Fixes the presentation timestamps (PTS) of the frames. By default, the PTS passed to the next filter is dropped, but the following options can change that:</p>
<dl>
<dt>
<dd>
<dl>
<dt>print</p>
<dd> Print the incoming PTS.</p>
<dt>fps=&lt;fps&gt;</p>
<dd> Specify a frame per second value.</p>
<dt>start=&lt;pts&gt;</p>
<dd> Specify an initial value for the PTS.</p>
<dt>autostart=&lt;n&gt;</p>
<dd> Uses the <i>n</i>th incoming PTS as the initial PTS. All previous PTS are kept, so setting a huge value or -1 keeps the PTS intact.</p>
<dt>autofps=&lt;n&gt;</p>
<dd> Uses the <i>n</i>th incoming PTS after the end of autostart to determine the framerate.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>-vf fixpts=fps=24000/1001,ass,fixpts</p>
<dd> Generates a new sequence of PTS, uses it for ASS subtitles, then drops it. Generating a new sequence is useful when the timestamps are reset during the program; this is frequent on DVDs. Dropping it may be necessary to avoid confusing encoders.</dl>
</dl>
<dl>
<dt>
<dd> <i>NOTE:</i> Using this filter together with any sort of seeking (including -ss and EDLs) may make demons fly out of your nose.</dl>
</dl>
<h2>GENERAL ENCODING OPTIONS (MENCODER ONLY)</h2>
<dl>
<dt><code>-audio-delay &lt;any floating-point number&gt;</code></p>
<dd> Delays either audio or video by setting a delay field in the header (default: 0.0). This does not delay either stream while encoding, but the player will see the delay field and compensate accordingly. Positive values delay the audio, and negative values delay the video. Note that this is the exact opposite of the -delay option. For example, if a video plays correctly with -delay 0.2, you can fix the video with MEncoder by using -audio-delay -0.2. </p>
<p> Currently, this option only works with the default muxer (-of avi). If you are using a different muxer, then you must use -delay instead.</p>
<dt><code>-audio-density &lt;1-50&gt;</code></p>
<dd> Number of audio chunks per second (default is 2 for 0.5s long audio chunks).<br />
 <i>NOTE:</i> CBR only, VBR ignores this as it puts each packet in a new chunk.</p>
<dt><code>-audio-preload &lt;0.0-2.0&gt;</code></p>
<dd> Sets up the audio buffering time interval (default: 0.5s).</p>
<dt><code>-fafmttag &lt;format&gt;</code></p>
<dd> Can be used to override the audio format tag of the output file. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-fafmttag 0x55</p>
<dd> Will have the output file contain 0x55 (mp3) as audio format tag.</dl>
</dl>
<dt><code>-ffourcc &lt;fourcc&gt;</code></p>
<dd> Can be used to override the video fourcc of the output file. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-ffourcc div3</p>
<dd> Will have the output file contain &#8216;div3&#8217; as video fourcc.</dl>
</dl>
<dt><code>-force-avi-aspect &lt;0.2-3.0&gt;</code></p>
<dd> Override the aspect stored in the AVI OpenDML vprp header. This can be used to change the aspect ratio with &#8216;-ovc copy&#8217;.</p>
<dt><code>-frameno-file &lt;filename&gt; (DEPRECATED)</code></p>
<dd> Specify the name of the audio file with framenumber mappings created in the first (audio only) pass of a special three pass encoding mode.<br />
 <i>NOTE:</i> Using this mode will most likely give you A-V desync. Do not use it. It is kept for backwards compatibility only and will possibly be removed in a future version.</p>
<dt><code>-hr-edl-seek</code></p>
<dd> Use a more precise, but much slower method for skipping areas. Areas marked for skipping are not seeked over, instead all frames are decoded, but only the necessary frames are encoded. This allows starting at non-keyframe boundaries.<br />
 <i>NOTE:</i> Not guaranteed to work right with &#8216;-ovc copy&#8217;.</p>
<dt><code>-info &lt;option1:option2:&#8230;&gt; (AVI only)</code></p>
<dd> Specify the info header of the resulting AVI file. </p>
<p> Available options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>help&nbsp;</p>
<dd> Show this description.</p>
<dt>name=&lt;value&gt;</p>
<dd> title of the work</p>
<dt>artist=&lt;value&gt;</p>
<dd> artist or author of the work</p>
<dt>genre=&lt;value&gt;</p>
<dd> original work category</p>
<dt>subject=&lt;value&gt;</p>
<dd> contents of the work</p>
<dt>copyright=&lt;value&gt;</p>
<dd> copyright information</p>
<dt>srcform=&lt;value&gt;</p>
<dd> original format of the digitized material</p>
<dt>comment=&lt;value&gt;</p>
<dd> general comments about the work</dl>
</dl>
<dt><code>-noautoexpand</code></p>
<dd> Do not automatically insert the expand filter into the MEncoder filter chain. Useful to control at which point of the filter chain subtitles are rendered when hardcoding subtitles onto a movie.</p>
<dt><code>-noencodedups</code></p>
<dd> Do not attempt to encode duplicate frames in duplicate; always output zero-byte frames to indicate duplicates. Zero-byte frames will be written anyway unless a filter or encoder capable of doing duplicate encoding is loaded. Currently the only such filter is harddup.</p>
<dt><code>-noodml (-of avi only)</code></p>
<dd> Do not write OpenDML index for AVI files &gt;1GB.</p>
<dt><code>-noskip</code></p>
<dd> Do not skip frames.</p>
<dt><code>-o &lt;filename&gt;</code></p>
<dd> Outputs to the given filename.<br />
 If you want a default output filename, you can put this option in the MEncoder config file.</p>
<dt><code>-oac &lt;codec name&gt;</code></p>
<dd> Encode with the given audio codec (no default set).<br />
 <i>NOTE:</i> Use -oac help to get a list of available audio codecs. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-oac copy</p>
<dd> no encoding, just streamcopy</p>
<dt>-oac pcm</p>
<dd> Encode to uncompressed PCM.</p>
<dt>-oac mp3lame</p>
<dd> Encode to MP3 (using LAME).</p>
<dt>-oac lavc</p>
<dd> Encode with a libavcodec codec.</dl>
</dl>
<dt><code>-of &lt;format&gt; (BETA CODE!)</code></p>
<dd> Encode to the specified container format (default: AVI).<br />
 <i>NOTE:</i> Use -of help to get a list of available container formats. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-of avi</p>
<dd> Encode to AVI.</p>
<dt>-of mpeg</p>
<dd> Encode to MPEG (also see -mpegopts).</p>
<dt>-of lavf</p>
<dd> Encode with libavformat muxers (also see -lavfopts).</p>
<dt>-of rawvideo</p>
<dd> raw video stream (no muxing &#8211; one video stream only)</p>
<dt>-of rawaudio</p>
<dd> raw audio stream (no muxing &#8211; one audio stream only)</dl>
</dl>
<dt><code>-ofps &lt;fps&gt;</code></p>
<dd> Specify a frames per second (fps) value for the output file, which can be different from that of the source material. Must be set for variable fps (ASF, some MOV) and progressive (30000/1001 fps telecined MPEG) files.</p>
<dt><code>-ovc &lt;codec name&gt;</code></p>
<dd> Encode with the given video codec (no default set).<br />
 <i>NOTE:</i> Use -ovc help to get a list of available video codecs. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>-ovc copy</p>
<dd> no encoding, just streamcopy</p>
<dt>-ovc raw</p>
<dd> Encode to an arbitrary uncompressed format (use &#8216;-vf format&#8217; to select).</p>
<dt>-ovc lavc</p>
<dd> Encode with a libavcodec codec.</dl>
</dl>
<dt><code>-passlogfile &lt;filename&gt;</code></p>
<dd> Dump first pass information to &lt;filename&gt; instead of the default divx2pass.log in two pass encoding mode.</p>
<dt><code>-skiplimit &lt;value&gt;</code></p>
<dd> Specify the maximum number of frames that may be skipped after encoding one frame (-noskiplimit for unlimited).</p>
<dt><code>-vobsubout &lt;basename&gt;</code></p>
<dd> Specify the basename for the output .idx and .sub files. This turns off subtitle rendering in the encoded movie and diverts it to VOBsub subtitle files.</p>
<dt><code>-vobsuboutid &lt;langid&gt;</code></p>
<dd> Specify the language two letter code for the subtitles. This overrides what is read from the DVD or the .ifo file.</p>
<dt><code>-vobsuboutindex &lt;index&gt;</code></p>
<dd> Specify the index of the subtitles in the output files (default: 0).</p>
<dt><code>-force-key-frames &lt;time&gt;,&lt;time&gt;,&#8230;</code></p>
<dd> Force key frames at the specified timestamps, more precisely at the first frame after each specified time. </p>
<p> This option can be used to ensure that a seek point is present at a chapter mark or any other designated place in the output file. </p>
<p> The timestamps must be specified in ascending order. </p>
<p> Since MEncoder does not send timestamps along the filter chain, you probably need to use the fixpts filter for this option to work. </p>
<p> Not all codecs support forced key frames. Currently, support is only implemented for the following encoders: lavc, x264, xvid.</dl>
<h2>CODEC SPECIFIC ENCODING OPTIONS (MENCODER ONLY)</h2>
<p> You can specify codec specific encoding parameters using the following syntax:</p>
<dl>
<dt><code>-&lt;codec&gt;opts &lt;option1[=value1]:option2[=value2]:&#8230;&gt;</code></p>
<dd></dl>
<p> Where &lt;codec&gt; may be: lavc, xvidenc, mp3lame, toolame, twolame, nuv, xvfw, faac, x264enc, mpeg, lavf.</p>
<h3>mp3lame (-lameopts)</h3>
<dl>
<dt><code>help&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> get help</p>
<dt><code>vbr=&lt;0-4&gt;</code></p>
<dd> variable bitrate method</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> cbr</p>
<dt>1</p>
<dd> mt</p>
<dt>2</p>
<dd> rh (default)</p>
<dt>3</p>
<dd> abr</p>
<dt>4</p>
<dd> mtrh</dl>
</dl>
<dt><code>abr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> average bitrate</p>
<dt><code>cbr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> constant bitrate Also forces CBR mode encoding on subsequent ABR presets modes.</p>
<dt><code>br=&lt;0-1024&gt;</code></p>
<dd> bitrate in kbps (CBR and ABR only)</p>
<dt><code>q=&lt;0-9&gt;</code></p>
<dd> quality (0 &#8211; highest, 9 &#8211; lowest) (VBR only)</p>
<dt><code>aq=&lt;0-9&gt;</code></p>
<dd> algorithmic quality (0 &#8211; best/slowest, 9 &#8211; worst/fastest)</p>
<dt><code>ratio=&lt;1-100&gt;</code></p>
<dd> compression ratio</p>
<dt><code>vol=&lt;0-10&gt;</code></p>
<dd> audio input gain</p>
<dt><code>mode=&lt;0-3&gt;</code></p>
<dd> (default: auto)</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> stereo</p>
<dt>1</p>
<dd> joint-stereo</p>
<dt>2</p>
<dd> dualchannel</p>
<dt>3</p>
<dd> mono</dl>
</dl>
<dt><code>padding=&lt;0-2&gt;</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> none</p>
<dt>1</p>
<dd> all</p>
<dt>2</p>
<dd> adjust</dl>
</dl>
<dt><code>fast&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Switch on faster encoding on subsequent VBR presets modes. This results in slightly lower quality and higher bitrates.</p>
<dt><code>highpassfreq=&lt;freq&gt;</code></p>
<dd> Set a highpass filtering frequency in Hz. Frequencies below the specified one will be cut off. A value of -1 will disable filtering, a value of 0 will let LAME choose values automatically.</p>
<dt><code>lowpassfreq=&lt;freq&gt;</code></p>
<dd> Set a lowpass filtering frequency in Hz. Frequencies above the specified one will be cut off. A value of -1 will disable filtering, a value of 0 will let LAME choose values automatically.</p>
<dt><code>preset=&lt;value&gt;</code></p>
<dd> preset values</p>
<dl>
<dt>
<dd>
<dl>
<dt>help&nbsp;</p>
<dd> Print additional options and information about presets settings.</p>
<dt>medium</p>
<dd> VBR encoding, good quality, 150-180 kbps bitrate range</p>
<dt>standard</p>
<dd> VBR encoding, high quality, 170-210 kbps bitrate range</p>
<dt>extreme</p>
<dd> VBR encoding, very high quality, 200-240 kbps bitrate range</p>
<dt>insane</p>
<dd> CBR encoding, highest preset quality, 320 kbps bitrate</p>
<dt>&lt;8-320&gt;</p>
<dd> ABR encoding at average given kbps bitrate</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLES:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>fast:preset=standard</p>
<dd> suitable for most people and most music types and already quite high quality</p>
<dt>cbr:preset=192</p>
<dd> Encode with ABR presets at a 192 kbps forced constant bitrate.</p>
<dt>preset=172</p>
<dd> Encode with ABR presets at a 172 kbps average bitrate.</p>
<dt>preset=extreme</p>
<dd> for people with extremely good hearing and similar equipment</dl>
</dl>
</dl>
<h3>toolame and twolame (-toolameopts and -twolameopts respectively)</h3>
<dl>
<dt><code>br=&lt;32-384&gt;</code></p>
<dd> In CBR mode this parameter indicates the bitrate in kbps, when in VBR mode it is the minimum bitrate allowed per frame. VBR mode will not work with a value below 112.</p>
<dt><code>vbr=&lt;-50-50&gt; (VBR only)</code></p>
<dd> variability range; if negative the encoder shifts the average bitrate towards the lower limit, if positive towards the higher. When set to 0 CBR is used (default).</p>
<dt><code>maxvbr=&lt;32-384&gt; (VBR only)</code></p>
<dd> maximum bitrate allowed per frame, in kbps</p>
<dt><code>mode=&lt;stereo | jstereo | mono | dual&gt;</code></p>
<dd> (default: mono for 1-channel audio, stereo otherwise)</p>
<dt><code>psy=&lt;-1-4&gt;</code></p>
<dd> psychoacoustic model (default: 2)</p>
<dt><code>errprot=&lt;0 | 1&gt;</code></p>
<dd> Include error protection.</p>
<dt><code>debug=&lt;0-10&gt;</code></p>
<dd> debug level</dl>
<h3>faac (-faacopts)</h3>
<dl>
<dt><code>br=&lt;bitrate&gt;</code></p>
<dd> average bitrate in kbps (mutually exclusive with quality)</p>
<dt><code>quality=&lt;1-1000&gt;</code></p>
<dd> quality mode, the higher the better (mutually exclusive with br)</p>
<dt><code>object=&lt;1-4&gt;</code></p>
<dd> object type complexity</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> MAIN (default)</p>
<dt>2</p>
<dd> LOW</p>
<dt>3</p>
<dd> SSR</p>
<dt>4</p>
<dd> LTP (extremely slow)</dl>
</dl>
<dt><code>mpeg=&lt;2|4&gt;</code></p>
<dd> MPEG version (default: 4)</p>
<dt><code>tns&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Enables temporal noise shaping.</p>
<dt><code>cutoff=&lt;0-sampling_rate/2&gt;</code></p>
<dd> cutoff frequency (default: sampling_rate/2)</p>
<dt><code>raw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Stores the bitstream as raw payload with extradata in the container header (default: 0, corresponds to ADTS). Do not set this flag if not explicitly required or you will not be able to remux the audio stream later on.</dl>
<h3>lavc (-lavcopts)</h3>
<p> Many libavcodec (lavc for short) options are tersely documented. Read the source for full details. </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>vcodec=msmpeg4:vbitrate=1800:vhq:keyint=250</p>
<dd></dl>
</dl>
<dl>
<dt><code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></p>
<dd> Pass AVOptions to libavcodec encoder. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some AVOptions may conflict with MEncoder options. </p>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>o=bt=100k</p>
<dd></dl>
</dl>
<dt><code>acodec=&lt;value&gt;</code></p>
<dd> audio codec (default: mp2)</p>
<dl>
<dt>
<dd>
<dl>
<dt>ac3&nbsp;<wbr>&nbsp;</p>
<dd> Dolby Digital (AC-3)</p>
<dt>adpcm_*</p>
<dd> Adaptive PCM formats &#8211; see the HTML documentation for details.</p>
<dt>flac&nbsp;</p>
<dd> Free Lossless Audio Codec (FLAC)</p>
<dt>g726&nbsp;</p>
<dd> G.726 ADPCM</p>
<dt>libfaac</p>
<dd> Advanced Audio Coding (AAC) &#8211; using FAAC</p>
<dt>libmp3lame</p>
<dd> MPEG-1 audio layer 3 (MP3) &#8211; using LAME</p>
<dt>mp2&nbsp;<wbr>&nbsp;</p>
<dd> MPEG-1 audio layer 2 (MP2)</p>
<dt>pcm_*</p>
<dd> PCM formats &#8211; see the HTML documentation for details.</p>
<dt>roq_dpcm</p>
<dd> Id Software RoQ DPCM</p>
<dt>sonic</p>
<dd> experimental simple lossy codec</p>
<dt>sonicls</p>
<dd> experimental simple lossless codec</p>
<dt>vorbis</p>
<dd> Vorbis</p>
<dt>wmav1</p>
<dd> Windows Media Audio v1</p>
<dt>wmav2</p>
<dd> Windows Media Audio v2</dl>
</dl>
<dt><code>abitrate=&lt;value&gt;</code></p>
<dd> audio bitrate in kbps (default: 224)</p>
<dt><code>atag=&lt;value&gt;</code></p>
<dd> Use the specified Windows audio format tag (e.g. atag=0x55).</p>
<dt><code>bit_exact</code></p>
<dd> Use only bit exact algorithms (except (I)DCT). Additionally bit_exact disables several optimizations and thus should only be used for regression tests, which need binary identical files even if the encoder version changes. This also suppresses the user_data header in MPEG-4 streams. Do not use this option unless you know exactly what you are doing.</p>
<dt><code>threads=&lt;1-8&gt;</code></p>
<dd> Maximum number of threads to use (default: 1). May have a slight negative effect on motion estimation.</p>
<dt><code>vcodec=&lt;value&gt;</code></p>
<dd> Employ the specified codec (default: mpeg4).</p>
<dl>
<dt>
<dd>
<dl>
<dt>asv1&nbsp;</p>
<dd> ASUS Video v1</p>
<dt>asv2&nbsp;</p>
<dd> ASUS Video v2</p>
<dt>dvvideo</p>
<dd> Sony Digital Video</p>
<dt>ffv1&nbsp;</p>
<dd> FFmpeg&#8217;s lossless video codec</p>
<dt>ffvhuff</p>
<dd> nonstandard 20% smaller HuffYUV using YV12</p>
<dt>flv&nbsp;<wbr>&nbsp;</p>
<dd> Sorenson H.263 used in Flash Video</p>
<dt>h261&nbsp;</p>
<dd> H.261</p>
<dt>h263&nbsp;</p>
<dd> H.263</p>
<dt>h263p</p>
<dd> H.263+</p>
<dt>huffyuv</p>
<dd> HuffYUV</p>
<dt>libtheora</p>
<dd> Theora</p>
<dt>libx264</p>
<dd> x264 H.264/AVC MPEG-4 Part 10</p>
<dt>libxvid</p>
<dd> Xvid MPEG-4 Part 2 (ASP)</p>
<dt>ljpeg</p>
<dd> Lossless JPEG</p>
<dt>mjpeg</p>
<dd> Motion JPEG</p>
<dt>mpeg1video</p>
<dd> MPEG-1 video</p>
<dt>mpeg2video</p>
<dd> MPEG-2 video</p>
<dt>mpeg4</p>
<dd> MPEG-4 (DivX 4/5)</p>
<dt>msmpeg4</p>
<dd> DivX 3</p>
<dt>msmpeg4v2</p>
<dd> MS MPEG4v2</p>
<dt>roqvideo</p>
<dd> ID Software RoQ Video</p>
<dt>rv10&nbsp;</p>
<dd> an old RealVideo codec</p>
<dt>snow (also see: vstrict)</p>
<dd> FFmpeg&#8217;s experimental wavelet-based codec</p>
<dt>svq1&nbsp;</p>
<dd> Apple Sorenson Video 1</p>
<dt>wmv1&nbsp;</p>
<dd> Windows Media Video, version 1 (AKA WMV7)</p>
<dt>wmv2&nbsp;</p>
<dd> Windows Media Video, version 2 (AKA WMV8)</dl>
</dl>
<dt><code>vqmin=&lt;1-31&gt;</code></p>
<dd> minimum quantizer</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> Not recommended (much larger file, little quality difference and weird side effects: msmpeg4, h263 will be very low quality, ratecontrol will be confused resulting in lower quality and some decoders will not be able to decode it).</p>
<dt>2</p>
<dd> Recommended for normal mpeg4/:mpeg1video encoding (default).</p>
<dt>3</p>
<dd> Recommended for h263(p)/:msmpeg4. The reason for preferring 3 over 2 is that 2 could lead to overflows. (This will be fixed for h263(p) by changing the quantizer per MB in the future, msmpeg4 cannot be fixed as it does not support that.)</dl>
</dl>
<dt><code>lmin=&lt;0.01-255.0&gt;</code></p>
<dd> Minimum frame-level Lagrange multiplier for ratecontrol (default: 2.0). Lavc will rarely use quantizers below the value of lmin. Lowering lmin will make lavc more likely to choose lower quantizers for some frames, but not lower than the value of vqmin. Likewise, raising lmin will make lavc less likely to choose low quantizers, even if vqmin would have allowed them. You probably want to set lmin approximately equal to vqmin. When adaptive quantization is in use, changing lmin/lmax may have less of an effect; see mblmin/mblmax.</p>
<dt><code>lmax=&lt;0.01-255.0&gt;</code></p>
<dd> maximum Lagrange multiplier for ratecontrol (default: 31.0)</p>
<dt><code>mblmin=&lt;0.01-255.0&gt;</code></p>
<dd> Minimum macroblock-level Lagrange multiplier for ratecontrol (default:2.0). This parameter affects adaptive quantization options like qprd, lumi_mask, etc..</p>
<dt><code>mblmax=&lt;0.01-255.0&gt;</code></p>
<dd> Maximum macroblock-level Lagrange multiplier for ratecontrol (default: 31.0).</p>
<dt><code>vqscale=&lt;0-31&gt;</code></p>
<dd> Constant quantizer /: constant quality encoding (selects fixed quantizer mode). A lower value means better quality but larger files (default: -1). In case of snow codec, value 0 means lossless encoding. Since the other codecs do not support this, vqscale=0 will have an undefined effect. 1 is not recommended (see vqmin for details).</p>
<dt><code>vqmax=&lt;1-31&gt;</code></p>
<dd> Maximum quantizer, 10-31 should be a sane range (default: 31).</p>
<dt><code>vqdiff=&lt;1-31&gt;</code></p>
<dd> maximum quantizer difference between consecutive I- or P-frames (default: 3)</p>
<dt><code>vmax_b_frames=&lt;0-4&gt;</code></p>
<dd> maximum number of B-frames between non-B-frames:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> no B-frames (default)</p>
<dt>0-2</p>
<dd> sane range for MPEG-4</dl>
</dl>
<dt><code>vme=&lt;0-5&gt;</code></p>
<dd> motion estimation method. Available methods are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> none (very low quality)</p>
<dt>1</p>
<dd> full (slow, currently unmaintained and disabled)</p>
<dt>2</p>
<dd> log (low quality, currently unmaintained and disabled)</p>
<dt>3</p>
<dd> phods (low quality, currently unmaintained and disabled)</p>
<dt>4</p>
<dd> EPZS: size=1 diamond, size can be adjusted with the *dia options (default)</p>
<dt>5</p>
<dd> X1 (experimental, currently aliased to EPZS)</p>
<dt>8</p>
<dd> iter (iterative overlapped block, only used in snow)</dl>
</dl>
<dl>
<dt>
<dd>
 <i>NOTE:</i> 0-3 currently ignores the amount of bits spent, so quality may be low.</dl>
<dt><code>me_range=&lt;0-9999&gt;</code></p>
<dd> motion estimation search range (default: 0 (unlimited))</p>
<dt><code>mbd=&lt;0-2&gt; (also see *cmp, qpel)</code></p>
<dd> Macroblock decision algorithm (high quality mode), encode each macro block in all modes and choose the best. This is slow but results in better quality and file size. When mbd is set to 1 or 2, the value of mbcmp is ignored when comparing macroblocks (the mbcmp value is still used in other places though, in particular the motion search algorithms). If any comparison setting (precmp, subcmp, cmp, or mbcmp) is nonzero, however, a slower but better half-pel motion search will be used, regardless of what mbd is set to. If qpel is set, quarter-pel motion search will be used regardless.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Use comparison function given by mbcmp (default).</p>
<dt>1</p>
<dd> Select the MB mode which needs the fewest bits (=vhq).</p>
<dt>2</p>
<dd> Select the MB mode which has the best rate distortion.</dl>
</dl>
<dt><code>vhq&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Same as mbd=1, kept for compatibility reasons.</p>
<dt><code>v4mv&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Allow 4 motion vectors per macroblock (slightly better quality). Works better if used with mbd&gt;0.</p>
<dt><code>obmc&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> overlapped block motion compensation (H.263+)</p>
<dt><code>loop&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> loop filter (H.263+) note, this is broken</p>
<dt><code>keyint=&lt;0-300&gt;</code></p>
<dd> maximum interval between keyframes in frames (default: 250 or one keyframe every ten seconds in a 25fps movie. This is the recommended default for MPEG-4). Most codecs require regular keyframes in order to limit the accumulation of mismatch error. Keyframes are also needed for seeking, as seeking is only possible to a keyframe &#8211; but keyframes need more space than other frames, so larger numbers here mean slightly smaller files but less precise seeking. 0 is equivalent to 1, which makes every frame a keyframe. Values &gt;300 are not recommended as the quality might be bad depending upon decoder, encoder and luck. It is common for MPEG-1/2 to use values &lt;=30.</p>
<dt><code>sc_threshold=&lt;-1000000000-1000000000&gt;</code></p>
<dd> Threshold for scene change detection. A keyframe is inserted by libavcodec when it detects a scene change. You can specify the sensitivity of the detection with this option. -1000000000 means there is a scene change detected at every frame, 1000000000 means no scene changes are detected (default: 0).</p>
<dt><code>sc_factor=&lt;any positive integer&gt;</code></p>
<dd> Causes frames with higher quantizers to be more likely to trigger a scene change detection and make libavcodec use an I-frame (default: 1). 1-16 is a sane range. Values between 2 and 6 may yield increasing PSNR (up to approximately 0.04 dB) and better placement of I-frames in high-motion scenes. Higher values than 6 may give very slightly better PSNR (approximately 0.01 dB more than sc_factor=6), but noticably worse visual quality.</p>
<dt><code>vb_strategy=&lt;0-2&gt; (pass one only)</code></p>
<dd> strategy to choose between I/P/B-frames:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Always use the maximum number of B-frames (default).</p>
<dt>1</p>
<dd> Avoid B-frames in high motion scenes. See the b_sensitivity option to tune this strategy.</p>
<dt>2</p>
<dd> Places B-frames more or less optimally to yield maximum quality (slower). You may want to reduce the speed impact of this option by tuning the option brd_scale.</dl>
</dl>
<dt><code>b_sensitivity=&lt;any integer greater than 0&gt;</code></p>
<dd> Adjusts how sensitively vb_strategy=1 detects motion and avoids using B-frames (default: 40). Lower sensitivities will result in more B-frames. Using more B-frames usually improves PSNR, but too many B-frames can hurt quality in high-motion scenes. Unless there is an extremely high amount of motion, b_sensitivity can safely be lowered below the default; 10 is a reasonable value in most cases.</p>
<dt><code>brd_scale=&lt;0-10&gt;</code></p>
<dd> Downscales frames for dynamic B-frame decision (default: 0). Each time brd_scale is increased by one, the frame dimensions are divided by two, which improves speed by a factor of four. Both dimensions of the fully downscaled frame must be even numbers, so brd_scale=1 requires the original dimensions to be multiples of four, brd_scale=2 requires multiples of eight, etc. In other words, the dimensions of the original frame must both be divisible by 2^(brd_scale+1) with no remainder.</p>
<dt><code>bidir_refine=&lt;0-4&gt;</code></p>
<dd> Refine the two motion vectors used in bidirectional macroblocks, rather than re-using vectors from the forward and backward searches. This option has no effect without B-frames.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Disabled (default).</p>
<dt>1-4</p>
<dd> Use a wider search (larger values are slower).</dl>
</dl>
<dt><code>vpass=&lt;1-3&gt;</code></p>
<dd> Activates internal two (or more) pass mode, only specify if you wish to use two (or more) pass encoding.</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> first pass (also see turbo)</p>
<dt>2</p>
<dd> second pass</p>
<dt>3</p>
<dd> Nth pass (second and subsequent passes of N-pass encoding)</dl>
</dl>
<dl>
<dt>
<dd> Here is how it works, and how to use it:<br />
 The first pass (vpass=1) writes the statistics file. You might want to deactivate some CPU-hungry options, like &quot;turbo&quot; mode does.<br />
 In two pass mode, the second pass (vpass=2) reads the statistics file and bases ratecontrol decisions on it.<br />
 In N-pass mode, the second pass (vpass=3, that is not a typo) does both: It first reads the statistics, then overwrites them. You might want to backup divx2pass.log before doing this if there is any possibility that you will have to cancel MEncoder. You can use all encoding options, except very CPU-hungry options like &quot;qns&quot;.<br />
 You can run this same pass over and over to refine the encode. Each subsequent pass will use the statistics from the previous pass to improve. The final pass can include any CPU-hungry encoding options.<br />
 If you want a 2 pass encode, use first vpass=1, and then vpass=2.<br />
 If you want a 3 or more pass encode, use vpass=1 for the first pass and then vpass=3 and then vpass=3 again and again until you are satisfied with the encode.</dl>
<dl>
<dt>
<dd> huffyuv:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>pass 1</p>
<dd> Saves statistics.</p>
<dt>pass 2</p>
<dd> Encodes with an optimal Huffman table based upon statistics from the first pass.</dl>
</dl>
<dt><code>turbo (two pass only)</code></p>
<dd> Dramatically speeds up pass one using faster algorithms and disabling CPU-intensive options. This will probably reduce global PSNR a little bit (around 0.01dB) and change individual frame type and PSNR a little bit more (up to 0.03dB).</p>
<dt><code>aspect=&lt;x/y&gt;</code></p>
<dd> Store movie aspect internally, just like with MPEG files. Much nicer than rescaling, because quality is not decreased. Only MPlayer will play these files correctly, other players will display them with wrong aspect. The aspect parameter can be given as a ratio or a floating point number. </p>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>aspect=16/9 or aspect=1.78</p>
<dd></dl>
</dl>
<dt><code>autoaspect</code></p>
<dd> Same as the aspect option, but automatically computes aspect, taking into account all the adjustments (crop/:expand/:scale/:etc.) made in the filter chain. Does not incur a performance penalty, so you can safely leave it always on.</p>
<dt><code>vbitrate=&lt;value&gt;</code></p>
<dd> Specify bitrate (default: 800).<br />
 <i>WARNING:</i> 1kbit = 1000 bits</p>
<dl>
<dt>
<dd>
<dl>
<dt>4-16000</p>
<dd> (in kbit)</p>
<dt>16001-24000000</p>
<dd> (in bit)</dl>
</dl>
<dt><code>vratetol=&lt;value&gt;</code></p>
<dd> approximated file size tolerance in kbit. 1000-100000 is a sane range. (warning: 1kbit = 1000 bits) (default: 8000)<br />
 <i>NOTE:</i> vratetol should not be too large during the second pass or there might be problems if vrc_(min|max)rate is used.</p>
<dt><code>vrc_maxrate=&lt;value&gt;</code></p>
<dd> maximum bitrate in kbit/:sec (default: 0, unlimited)</p>
<dt><code>vrc_minrate=&lt;value&gt;</code></p>
<dd> minimum bitrate in kbit/:sec (default: 0, unlimited)</p>
<dt><code>vrc_buf_size=&lt;value&gt;</code></p>
<dd> buffer size in kbit For MPEG-1/2 this also sets the vbv buffer size, use 327 for VCD, 917 for SVCD and 1835 for DVD.</p>
<dt><code>vrc_buf_aggressivity</code></p>
<dd> currently useless</p>
<dt><code>vrc_strategy</code></p>
<dd> Ratecontrol method. Note that some of the ratecontrol-affecting options will have no effect if vrc_strategy is not set to 0.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Use internal lavc ratecontrol (default).</p>
<dt>1</p>
<dd> Use Xvid ratecontrol (experimental; requires MEncoder to be compiled with support for Xvid 1.1 or higher).</dl>
</dl>
<dt><code>vb_qfactor=&lt;-31.0-31.0&gt;</code></p>
<dd> quantizer factor between B- and non-B-frames (default: 1.25)</p>
<dt><code>vi_qfactor=&lt;-31.0-31.0&gt;</code></p>
<dd> quantizer factor between I- and non-I-frames (default: 0.8)</p>
<dt><code>vb_qoffset=&lt;-31.0-31.0&gt;</code></p>
<dd> quantizer offset between B- and non-B-frames (default: 1.25)</p>
<dt><code>vi_qoffset=&lt;-31.0-31.0&gt;</code></p>
<dd> (default: 0.0)<br />
 if v{b|i}_qfactor &gt; 0<br />
 I/B-frame quantizer = P-frame quantizer * v{b|i}_qfactor + v{b|i}_qoffset<br />
 else<br />
 do normal ratecontrol (do not lock to next P-frame quantizer) and set q= -q * v{b|i}_qfactor + v{b|i}_qoffset<br />
 <i>HINT:</i> To do constant quantizer encoding with different quantizers for I/P- and B-frames you can use: lmin= &lt;ip_quant&gt;:lmax= &lt;ip_quant&gt;:vb_qfactor= &lt;b_quant/:ip_quant&gt;.</p>
<dt><code>vqblur=&lt;0.0-1.0&gt; (pass one)</code></p>
<dd> Quantizer blur (default: 0.5), larger values will average the quantizer more over time (slower change).</p>
<dl>
<dt>
<dd>
<dl>
<dt>0.0</p>
<dd> Quantizer blur disabled.</p>
<dt>1.0</p>
<dd> Average the quantizer over all previous frames.</dl>
</dl>
<dt><code>vqblur=&lt;0.0-99.0&gt; (pass two)</code></p>
<dd> Quantizer gaussian blur (default: 0.5), larger values will average the quantizer more over time (slower change).</p>
<dt><code>vqcomp=&lt;0.0-1.0&gt;</code></p>
<dd> Quantizer compression, vrc_eq depends upon this (default: 0.5). <i>NOTE:</i> Perceptual quality will be optimal somewhere in between the range&#8217;s extremes.</p>
<dt><code>vrc_eq=&lt;equation&gt;</code></p>
<dd> main ratecontrol equation</p>
<dl>
<dt>
<dd>
<dl>
<dt>1+(tex/:avgTex-1)*qComp</p>
<dd> approximately the equation of the old ratecontrol code</p>
<dt>tex^qComp</p>
<dd> with qcomp 0.5 or something like that (default)</dl>
</dl>
</dl>
<dl>
<dt>
<dd> infix operators:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>+,-,*,/,^</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd> variables:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>tex&nbsp;<wbr>&nbsp;</p>
<dd> texture complexity</p>
<dt>iTex,pTex</p>
<dd> intra, non-intra texture complexity</p>
<dt>avgTex</p>
<dd> average texture complexity</p>
<dt>avgIITex</p>
<dd> average intra texture complexity in I-frames</p>
<dt>avgPITex</p>
<dd> average intra texture complexity in P-frames</p>
<dt>avgPPTex</p>
<dd> average non-intra texture complexity in P-frames</p>
<dt>avgBPTex</p>
<dd> average non-intra texture complexity in B-frames</p>
<dt>mv&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> bits used for motion vectors</p>
<dt>fCode</p>
<dd> maximum length of motion vector in log2 scale</p>
<dt>iCount</p>
<dd> number of intra macroblocks / number of macroblocks</p>
<dt>var&nbsp;<wbr>&nbsp;</p>
<dd> spatial complexity</p>
<dt>mcVar</p>
<dd> temporal complexity</p>
<dt>qComp</p>
<dd> qcomp from the command line</p>
<dt>isI, isP, isB</p>
<dd> Is 1 if picture type is I/P/B else 0.</p>
<dt>Pi,E&nbsp;</p>
<dd> See your favorite math book.</dl>
</dl>
<dl>
<dt>
<dd> functions:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>max(a,b),min(a,b)</p>
<dd> maximum / minimum</p>
<dt>gt(a,b)</p>
<dd> is 1 if a&gt;b, 0 otherwise</p>
<dt>lt(a,b)</p>
<dd> is 1 if a&lt;b, 0 otherwise</p>
<dt>eq(a,b)</p>
<dd> is 1 if a==b, 0 otherwise</p>
<dt>sin, cos, tan, sinh, cosh, tanh, exp, log, abs</p>
<dd></dl>
</dl>
<dl>
<dt><code>vrc_override=&lt;options&gt;</code></p>
<dd> User specified quality for specific parts (ending, credits, &#8230;). The options are &lt;start-frame&gt;, &lt;end-frame&gt;, &lt;quality&gt;[/&lt;start-frame&gt;, &lt;end-frame&gt;, &lt;quality&gt;[/&#8230;]]:</p>
<dl>
<dt>
<dd>
<dl>
<dt>quality (2-31)</p>
<dd> quantizer</p>
<dt>quality (-500-0)</p>
<dd> quality correction in %</dl>
</dl>
<dt><code>vrc_init_cplx=&lt;0-1000&gt;</code></p>
<dd> initial complexity (pass 1)</p>
<dt><code>vrc_init_occupancy=&lt;0.0-1.0&gt;</code></p>
<dd> initial buffer occupancy, as a fraction of vrc_buf_size (default: 0.9)</p>
<dt><code>vqsquish=&lt;0|1&gt;</code></p>
<dd> Specify how to keep the quantizer between qmin and qmax.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Use clipping.</p>
<dt>1</p>
<dd> Use a nice differentiable function (default).</dl>
</dl>
<dt><code>vlelim=&lt;-1000-1000&gt;</code></p>
<dd> Sets single coefficient elimination threshold for luminance. Negative values will also consider the DC coefficient (should be at least -4 or lower for encoding at quant=1):</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled (default)</p>
<dt>-4</p>
<dd> JVT recommendation</dl>
</dl>
<dt><code>vcelim=&lt;-1000-1000&gt;</code></p>
<dd> Sets single coefficient elimination threshold for chrominance. Negative values will also consider the DC coefficient (should be at least -4 or lower for encoding at quant=1):</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled (default)</p>
<dt>7</p>
<dd> JVT recommendation</dl>
</dl>
<dt><code>vstrict=&lt;-2|-1|0|1&gt;</code></p>
<dd> strict standard compliance</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled</p>
<dt>1</p>
<dd> Only recommended if you want to feed the output into the MPEG-4 reference decoder.</p>
<dt>-1</p>
<dd> Allow libavcodec specific extensions (default).</p>
<dt>-2</p>
<dd> Enables experimental codecs and features which may not be playable with future MPlayer versions (snow).</dl>
</dl>
<dt><code>vdpart&nbsp;</code></p>
<dd> Data partitioning. Adds 2 Bytes per video packet, improves error-resistance when transferring over unreliable channels (e.g. streaming over the internet). Each video packet will be encoded in 3 separate partitions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1. MVs</p>
<dd> movement</p>
<dt>2. DC coefficients</p>
<dd> low res picture</p>
<dt>3. AC coefficients</p>
<dd> details</dl>
</dl>
<dl>
<dt>
<dd> MV &amp; DC are most important, losing them looks far worse than losing the AC and the 1. &amp; 2. partition. (MV &amp; DC) are far smaller than the 3. partition (AC) meaning that errors will hit the AC partition much more often than the MV &amp; DC partitions. Thus, the picture will look better with partitioning than without, as without partitioning an error will trash AC/:DC/:MV equally.</dl>
<dt><code>vpsize=&lt;0-10000&gt; (also see vdpart)</code></p>
<dd> Video packet size, improves error-resistance.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> disabled (default)</p>
<dt>100-1000</p>
<dd> good choice</dl>
</dl>
<dt><code>ss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> slice structured mode for H.263+</p>
<dt><code>gray&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> grayscale only encoding (faster)</p>
<dt><code>vfdct=&lt;0-10&gt;</code></p>
<dd> DCT algorithm</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Automatically select a good one (default).</p>
<dt>1</p>
<dd> fast integer</p>
<dt>2</p>
<dd> accurate integer</p>
<dt>3</p>
<dd> MMX</p>
<dt>4</p>
<dd> mlib</p>
<dt>5</p>
<dd> AltiVec</p>
<dt>6</p>
<dd> floating point AAN</dl>
</dl>
<dt><code>idct=&lt;0-99&gt;</code></p>
<dd> IDCT algorithm<br />
 <i>NOTE:</i> To the best of our knowledge all these IDCTs do pass the IEEE1180 tests.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Automatically select a good one (default).</p>
<dt>1</p>
<dd> JPEG reference integer</p>
<dt>2</p>
<dd> simple</p>
<dt>3</p>
<dd> simplemmx</p>
<dt>4</p>
<dd> libmpeg2mmx (inaccurate, do not use for encoding with keyint &gt;100)</p>
<dt>5</p>
<dd> ps2</p>
<dt>6</p>
<dd> mlib</p>
<dt>7</p>
<dd> arm</p>
<dt>8</p>
<dd> AltiVec</p>
<dt>9</p>
<dd> sh4</p>
<dt>10</p>
<dd> simplearm</p>
<dt>11</p>
<dd> H.264</p>
<dt>12</p>
<dd> VP3</p>
<dt>13</p>
<dd> IPP</p>
<dt>14</p>
<dd> xvidmmx</p>
<dt>15</p>
<dd> CAVS</p>
<dt>16</p>
<dd> simplearmv5te</p>
<dt>17</p>
<dd> simplearmv6</dl>
</dl>
<dt><code>lumi_mask=&lt;0.0-1.0&gt;</code></p>
<dd> Luminance masking is a &#8216;psychosensory&#8217; setting that is supposed to make use of the fact that the human eye tends to notice fewer details in very bright parts of the picture. Luminance masking compresses bright areas stronger than medium ones, so it will save bits that can be spent again on other frames, raising overall subjective quality, while possibly reducing PSNR.<br />
 <i>WARNING:</i> Be careful, overly large values can cause disastrous things.<br />
 <i>WARNING:</i> Large values might look good on some monitors but may look horrible on other monitors.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0.0&nbsp;<wbr>&nbsp;</p>
<dd> disabled (default)</p>
<dt>0.0-0.3</p>
<dd> sane range</dl>
</dl>
<dt><code>dark_mask=&lt;0.0-1.0&gt;</code></p>
<dd> Darkness masking is a &#8216;psychosensory&#8217; setting that is supposed to make use of the fact that the human eye tends to notice fewer details in very dark parts of the picture. Darkness masking compresses dark areas stronger than medium ones, so it will save bits that can be spent again on other frames, raising overall subjective quality, while possibly reducing PSNR.<br />
 <i>WARNING:</i> Be careful, overly large values can cause disastrous things.<br />
 <i>WARNING:</i> Large values might look good on some monitors but may look horrible on other monitors / TV / TFT.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0.0&nbsp;<wbr>&nbsp;</p>
<dd> disabled (default)</p>
<dt>0.0-0.3</p>
<dd> sane range</dl>
</dl>
<dt><code>tcplx_mask=&lt;0.0-1.0&gt;</code></p>
<dd> Temporal complexity masking (default: 0.0 (disabled)). Imagine a scene with a bird flying across the whole scene; tcplx_mask will raise the quantizers of the bird&#8217;s macroblocks (thus decreasing their quality), as the human eye usually does not have time to see all the bird&#8217;s details. Be warned that if the masked object stops (e.g. the bird lands) it is likely to look horrible for a short period of time, until the encoder figures out that the object is not moving and needs refined blocks. The saved bits will be spent on other parts of the video, which may increase subjective quality, provided that tcplx_mask is carefully chosen.</p>
<dt><code>scplx_mask=&lt;0.0-1.0&gt;</code></p>
<dd> Spatial complexity masking. Larger values help against blockiness, if no deblocking filter is used for decoding, which is maybe not a good idea.<br />
 Imagine a scene with grass (which usually has great spatial complexity), a blue sky and a house; scplx_mask will raise the quantizers of the grass&#8217; macroblocks, thus decreasing its quality, in order to spend more bits on the sky and the house.<br />
 <i>HINT:</i> Crop any black borders completely as they will reduce the quality of the macroblocks (also applies without scplx_mask).</p>
<dl>
<dt>
<dd>
<dl>
<dt>0.0&nbsp;<wbr>&nbsp;</p>
<dd> disabled (default)</p>
<dt>0.0-0.5</p>
<dd> sane range</dl>
</dl>
<dl>
<dt>
<dd> <i>NOTE:</i> This setting does not have the same effect as using a custom matrix that would compress high frequencies harder, as scplx_mask will reduce the quality of P blocks even if only DC is changing. The result of scplx_mask will probably not look as good.</dl>
<dt><code>p_mask=&lt;0.0-1.0&gt; (also see vi_qfactor)</code></p>
<dd> Reduces the quality of inter blocks. This is equivalent to increasing the quality of intra blocks, because the same average bitrate will be distributed by the rate controller to the whole video sequence (default: 0.0 (disabled)). p_mask=1.0 doubles the bits allocated to each intra block.</p>
<dt><code>border_mask=&lt;0.0-1.0&gt;</code></p>
<dd> border-processing for MPEG-style encoders. Border processing increases the quantizer for macroblocks which are less than 1/5th of the frame width/height away from the frame border, since they are often visually less important.</p>
<dt><code>naq&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Normalize adaptive quantization (experimental). When using adaptive quantization (*_mask), the average per-MB quantizer may no longer match the requested frame-level quantizer. Naq will attempt to adjust the per-MB quantizers to maintain the proper average.</p>
<dt><code>ildct&nbsp;<wbr>&nbsp;</code></p>
<dd> Use interlaced DCT.</p>
<dt><code>ilme&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Use interlaced motion estimation (mutually exclusive with qpel).</p>
<dt><code>alt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Use alternative scantable.</p>
<dt><code>top=&lt;-1-1&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> automatic</p>
<dt>0</p>
<dd> bottom field first</p>
<dt>1</p>
<dd> top field first</dl>
</dl>
<dt><code>format=&lt;value&gt;</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>YV12&nbsp;</p>
<dd> default</p>
<dt>444P&nbsp;</p>
<dd> for ffv1</p>
<dt>422P&nbsp;</p>
<dd> for HuffYUV, lossless JPEG, dv and ffv1</p>
<dt>411P&nbsp;</p>
<dd> for lossless JPEG, dv and ffv1</p>
<dt>YVU9&nbsp;</p>
<dd> for lossless JPEG, ffv1 and svq1</p>
<dt>BGR32</p>
<dd> for lossless JPEG and ffv1</dl>
</dl>
<dt><code>pred&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> (for HuffYUV)</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> left prediction</p>
<dt>1</p>
<dd> plane/:gradient prediction</p>
<dt>2</p>
<dd> median prediction</dl>
</dl>
<dt><code>pred&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> (for lossless JPEG)</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> left prediction</p>
<dt>1</p>
<dd> top prediction</p>
<dt>2</p>
<dd> topleft prediction</p>
<dt>3</p>
<dd> plane/:gradient prediction</p>
<dt>6</p>
<dd> mean prediction</dl>
</dl>
<dt><code>coder&nbsp;<wbr>&nbsp;</code></p>
<dd> (for ffv1)</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> vlc coding (Golomb-Rice)</p>
<dt>1</p>
<dd> arithmetic coding (CABAC)</dl>
</dl>
<dt><code>context</code></p>
<dd> (for ffv1)</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> small context model</p>
<dt>1</p>
<dd> large context model</dl>
</dl>
<dl>
<dt>
<dd> (for ffvhuff)</dl>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> predetermined Huffman tables (builtin or two pass)</p>
<dt>1</p>
<dd> adaptive Huffman tables</dl>
</dl>
<dt><code>qpel&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Use quarter pel motion compensation (mutually exclusive with ilme).<br />
 <i>HINT:</i> This seems only useful for high bitrate encodings.</p>
<dt><code>mbcmp=&lt;0-2000&gt;</code></p>
<dd> Sets the comparison function for the macroblock decision, has only an effect if mbd=0. This is also used for some motion search functions, in which case it has an effect regardless of mbd setting.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0 (SAD)</p>
<dd> sum of absolute differences, fast (default)</p>
<dt>1 (SSE)</p>
<dd> sum of squared errors</p>
<dt>2 (SATD)</p>
<dd> sum of absolute Hadamard transformed differences</p>
<dt>3 (DCT)</p>
<dd> sum of absolute DCT transformed differences</p>
<dt>4 (PSNR)</p>
<dd> sum of squared quantization errors (avoid, low quality)</p>
<dt>5 (BIT)</p>
<dd> number of bits needed for the block</p>
<dt>6 (RD)</p>
<dd> rate distortion optimal, slow</p>
<dt>7 (ZERO)</p>
<dd> 0</p>
<dt>8 (VSAD)</p>
<dd> sum of absolute vertical differences</p>
<dt>9 (VSSE)</p>
<dd> sum of squared vertical differences</p>
<dt>10 (NSSE)</p>
<dd> noise preserving sum of squared differences</p>
<dt>11 (W53)</p>
<dd> 5/3 wavelet, only used in snow</p>
<dt>12 (W97)</p>
<dd> 9/7 wavelet, only used in snow</p>
<dt>+256&nbsp;</p>
<dd> Also use chroma, currently does not work (correctly) with B-frames.</dl>
</dl>
<dt><code>ildctcmp=&lt;0-2000&gt;</code></p>
<dd> Sets the comparison function for interlaced DCT decision (see mbcmp for available comparison functions).</p>
<dt><code>precmp=&lt;0-2000&gt;</code></p>
<dd> Sets the comparison function for motion estimation pre pass (see mbcmp for available comparison functions) (default: 0).</p>
<dt><code>cmp=&lt;0-2000&gt;</code></p>
<dd> Sets the comparison function for full pel motion estimation (see mbcmp for available comparison functions) (default: 0).</p>
<dt><code>subcmp=&lt;0-2000&gt;</code></p>
<dd> Sets the comparison function for sub pel motion estimation (see mbcmp for available comparison functions) (default: 0).</p>
<dt><code>skipcmp=&lt;0-2000&gt;</code></p>
<dd> FIXME: Document this.</p>
<dt><code>nssew=&lt;0-1000000&gt;</code></p>
<dd> This setting controls NSSE weight, where larger weights will result in more noise. 0 NSSE is identical to SSE You may find this useful if you prefer to keep some noise in your encoded video rather than filtering it away before encoding (default: 8).</p>
<dt><code>predia=&lt;-99-6&gt;</code></p>
<dd> diamond type and size for motion estimation pre-pass</p>
<dt><code>dia=&lt;-99-6&gt;</code></p>
<dd> Diamond type &amp; size for motion estimation. Motion search is an iterative process. Using a small diamond does not limit the search to finding only small motion vectors. It is just somewhat more likely to stop before finding the very best motion vector, especially when noise is involved. Bigger diamonds allow a wider search for the best motion vector, thus are slower but result in better quality.<br />
 Big normal diamonds are better quality than shape-adaptive diamonds.<br />
 Shape-adaptive diamonds are a good tradeoff between speed and quality.<br />
 <i>NOTE:</i> The sizes of the normal diamonds and shape adaptive ones do not have the same meaning.</p>
<dl>
<dt>
<dd>
<dl>
<dt>-3</p>
<dd> shape adaptive (fast) diamond with size 3</p>
<dt>-2</p>
<dd> shape adaptive (fast) diamond with size 2</p>
<dt>-1</p>
<dd> uneven multi-hexagon search (slow)</p>
<dt>1</p>
<dd> normal size=1 diamond (default) =EPZS type diamond </p>
<pre>
      0
     000
      0
</pre>
<dt>2</p>
<dd> normal size=2 diamond </p>
<pre>
      0
     000
    00000
     000
      0
</pre>
</dl>
</dl>
<dt><code>trell&nbsp;<wbr>&nbsp;</code></p>
<dd> Trellis searched quantization. This will find the optimal encoding for each 8&#215;8 block. Trellis searched quantization is quite simply an optimal quantization in the PSNR versus bitrate sense (Assuming that there would be no rounding errors introduced by the IDCT, which is obviously not the case.). It simply finds a block for the minimum of error and lambda*bits.</p>
<dl>
<dt>
<dd>
<dl>
<dt>lambda</p>
<dd> quantization parameter (QP) dependent constant</p>
<dt>bits&nbsp;</p>
<dd> amount of bits needed to encode the block</p>
<dt>error</p>
<dd> sum of squared errors of the quantization</dl>
</dl>
<dt><code>cbp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Rate distorted optimal coded block pattern. Will select the coded block pattern which minimizes distortion + lambda*rate. This can only be used together with trellis quantization.</p>
<dt><code>mv0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Try to encode each MB with MV=&lt;0,0&gt; and choose the better one. This has no effect if mbd=0.</p>
<dt><code>mv0_threshold=&lt;any non-negative integer&gt;</code></p>
<dd> When surrounding motion vectors are &lt;0,0&gt; and the motion estimation score of the current block is less than mv0_threshold, &lt;0,0&gt; is used for the motion vector and further motion estimation is skipped (default: 256). Lowering mv0_threshold to 0 can give a slight (0.01dB) PSNR increase and possibly make the encoded video look slightly better; raising mv0_threshold past 320 results in diminished PSNR and visual quality. Higher values speed up encoding very slightly (usually less than 1%, depending on the other options used).<br />
 <i>NOTE:</i> This option does not require mv0 to be enabled.</p>
<dt><code>qprd (mbd=2 only)</code></p>
<dd> rate distorted optimal quantization parameter (QP) for the given lambda of each macroblock</p>
<dt><code>last_pred=&lt;0-99&gt;</code></p>
<dd> amount of motion predictors from the previous frame</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> (default)</p>
<dt>a</p>
<dd> Will use 2a+1 x 2a+1 macroblock square of motion vector predictors from the previous frame.</dl>
</dl>
<dt><code>preme=&lt;0-2&gt;</code></p>
<dd> motion estimation pre-pass</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled</p>
<dt>1</p>
<dd> only after I-frames (default)</p>
<dt>2</p>
<dd> always</dl>
</dl>
<dt><code>subq=&lt;1-8&gt;</code></p>
<dd> subpel refinement quality (for qpel) (default: 8 (high quality))<br />
 <i>NOTE:</i> This has a significant effect on speed.</p>
<dt><code>refs=&lt;1-8&gt;</code></p>
<dd> number of reference frames to consider for motion compensation (Snow only) (default: 1)</p>
<dt><code>psnr&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> print the PSNR (peak signal to noise ratio) for the whole video after encoding and store the per frame PSNR in a file with a name like &#8216;psnr_hhmmss.log&#8217;. Returned values are in dB (decibel), the higher the better.</p>
<dt><code>mpeg_quant</code></p>
<dd> Use MPEG quantizers instead of H.263.</p>
<dt><code>aic&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Enable AC prediction for MPEG-4 or advanced intra prediction for H.263+. This will improve quality very slightly (around 0.02 dB PSNR) and slow down encoding very slightly (about 1%).<br />
 <i>NOTE:</i> vqmin should be 8 or larger for H.263+ AIC.</p>
<dt><code>aiv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> alternative inter vlc for H.263+</p>
<dt><code>umv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> unlimited MVs (H.263+ only) Allows encoding of arbitrarily long MVs.</p>
<dt><code>ibias=&lt;-256-256&gt;</code></p>
<dd> intra quantizer bias (256 equals 1.0, MPEG style quantizer default: 96, H.263 style quantizer default: 0)<br />
 <i>NOTE:</i> The H.263 MMX quantizer cannot handle positive biases (set vfdct=1 or 2), the MPEG MMX quantizer cannot handle negative biases (set vfdct=1 or 2).</p>
<dt><code>pbias=&lt;-256-256&gt;</code></p>
<dd> inter quantizer bias (256 equals 1.0, MPEG style quantizer default: 0, H.263 style quantizer default: -64)<br />
 <i>NOTE:</i> The H.263 MMX quantizer cannot handle positive biases (set vfdct=1 or 2), the MPEG MMX quantizer cannot handle negative biases (set vfdct=1 or 2).<br />
 <i>HINT:</i> A more positive bias (-32 &#8211; -16 instead of -64) seems to improve the PSNR.</p>
<dt><code>nr=&lt;0-100000&gt;</code></p>
<dd> Noise reduction, 0 means disabled. 0-600 is a useful range for typical content, but you may want to turn it up a bit more for very noisy content (default: 0). Given its small impact on speed, you might want to prefer to use this over filtering noise away with video filters like denoise3d or hqdn3d.</p>
<dt><code>qns=&lt;0-3&gt;</code></p>
<dd> Quantizer noise shaping. Rather than choosing quantization to most closely match the source video in the PSNR sense, it chooses quantization such that noise (usually ringing) will be masked by similar-frequency content in the image. Larger values are slower but may not result in better quality. This can and should be used together with trellis quantization, in which case the trellis quantization (optimal for constant weight) will be used as startpoint for the iterative search.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled (default)</p>
<dt>1</p>
<dd> Only lower the absolute value of coefficients.</p>
<dt>2</p>
<dd> Only change coefficients before the last non-zero coefficient + 1.</p>
<dt>3</p>
<dd> Try all.</dl>
</dl>
<dt><code>inter_matrix=&lt;comma separated matrix&gt;</code></p>
<dd> Use custom inter matrix. It needs a comma separated string of 64 integers.</p>
<dt><code>intra_matrix=&lt;comma separated matrix&gt;</code></p>
<dd> Use custom intra matrix. It needs a comma separated string of 64 integers.</p>
<dt><code>vqmod_amp</code></p>
<dd> experimental quantizer modulation</p>
<dt><code>vqmod_freq</code></p>
<dd> experimental quantizer modulation</p>
<dt><code>dc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> intra DC precision in bits (default: 8). If you specify vcodec=mpeg2video this value can be 8, 9, 10 or 11.</p>
<dt><code>cgop (also see sc_threshold)</code></p>
<dd> Close all GOPs. Currently it only works if scene change detection is disabled (sc_threshold=1000000000).</p>
<dt><code>gmc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Enable Global Motion Compensation.</p>
<dt><code>(no)lowdelay</code></p>
<dd> Sets the low delay flag for MPEG-1/2 (disables B-frames).</p>
<dt><code>vglobal=&lt;0-3&gt;</code></p>
<dd> Control writing global video headers.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Codec decides where to write global headers (default).</p>
<dt>1</p>
<dd> Write global headers only in extradata (needed for .mp4/MOV/NUT).</p>
<dt>2</p>
<dd> Write global headers only in front of keyframes.</p>
<dt>3</p>
<dd> Combine 1 and 2.</dl>
</dl>
<dt><code>aglobal=&lt;0-3&gt;</code></p>
<dd> Same as vglobal for audio headers.</p>
<dt><code>level=&lt;value&gt;</code></p>
<dd> Set CodecContext Level. Use 31 or 41 to play video on a Playstation 3.</p>
<dt><code>skip_exp=&lt;0-1000000&gt;</code></p>
<dd> FIXME: Document this.</p>
<dt><code>skip_factor=&lt;0-1000000&gt;</code></p>
<dd> FIXME: Document this.</p>
<dt><code>skip_threshold=&lt;0-1000000&gt;</code></p>
<dd> FIXME: Document this.</dl>
<h3>nuv (-nuvopts)</h3>
<p> Nuppel video is based on RTJPEG and LZO. By default frames are first encoded with RTJPEG and then compressed with LZO, but it is possible to disable either or both of the two passes. As a result, you can in fact output raw i420, LZO compressed i420, RTJPEG, or the default LZO compressed RTJPEG.<br />
 <i>NOTE:</i> The nuvrec documentation contains some advice and examples about the settings to use for the most common TV encodings.</p>
<dl>
<dt><code>c=&lt;0-20&gt;</code></p>
<dd> chrominance threshold (default: 1)</p>
<dt><code>l=&lt;0-20&gt;</code></p>
<dd> luminance threshold (default: 1)</p>
<dt><code>lzo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Enable LZO compression (default).</p>
<dt><code>nolzo&nbsp;<wbr>&nbsp;</code></p>
<dd> Disable LZO compression.</p>
<dt><code>q=&lt;3-255&gt;</code></p>
<dd> quality level (default: 255)</p>
<dt><code>raw &nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Disable RTJPEG encoding.</p>
<dt><code>rtjpeg&nbsp;</code></p>
<dd> Enable RTJPEG encoding (default).</dl>
<h3>xvidenc (-xvidencopts)</h3>
<p> There are three modes available: constant bitrate (CBR), fixed quantizer and two pass.</p>
<dl>
<dt><code>pass=&lt;1|2&gt;</code></p>
<dd> Specify the pass in two pass mode.</p>
<dt><code>turbo (two pass only)</code></p>
<dd> Dramatically speeds up pass one using faster algorithms and disabling CPU-intensive options. This will probably reduce global PSNR a little bit and change individual frame type and PSNR a little bit more.</p>
<dt><code>bitrate=&lt;value&gt; (CBR or two pass mode)</code></p>
<dd> Sets the bitrate to be used in kbits/:second if &lt;16000 or in bits/:second if &gt;16000. If &lt;value&gt; is negative, Xvid will use its absolute value as the target size (in kBytes) of the video and compute the associated bitrate automagically (default: 687 kbits/s).</p>
<dt><code>fixed_quant=&lt;1-31&gt;</code></p>
<dd> Switch to fixed quantizer mode and specify the quantizer to be used.</p>
<dt><code>zones=&lt;zone0&gt;[/&lt;zone1&gt;[/&#8230;]] (CBR or two pass mode)</code></p>
<dd> User specified quality for specific parts (ending, credits, &#8230;). Each zone is &lt;start-frame&gt;,&lt;mode&gt;,&lt;value&gt; where &lt;mode&gt; may be</p>
<dl>
<dt>
<dd>
<dl>
<dt>q</p>
<dd> Constant quantizer override, where value=&lt;2.0-31.0&gt; represents the quantizer value.</p>
<dt>w</p>
<dd> Ratecontrol weight override, where value=&lt;0.01-2.00&gt; represents the quality correction in %.</dl>
</dl>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>zones=90000,q,20</p>
<dd> Encodes all frames starting with frame 90000 at constant quantizer 20.</p>
<dt>zones=0,w,0.1/10001,w,1.0/90000,q,20</p>
<dd> Encode frames 0-10000 at 10% bitrate, encode frames 90000 up to the end at constant quantizer 20. Note that the second zone is needed to delimit the first zone, as without it everything up until frame 89999 would be encoded at 10% bitrate.</dl>
</dl>
<dt><code>me_quality=&lt;0-6&gt;</code></p>
<dd> This option controls the motion estimation subsystem. The higher the value, the more precise the estimation should be (default: 6). The more precise the motion estimation is, the more bits can be saved. Precision is gained at the expense of CPU time so decrease this setting if you need realtime encoding.</p>
<dt><code>(no)qpel</code></p>
<dd> MPEG-4 uses a half pixel precision for its motion search by default. The standard proposes a mode where encoders are allowed to use quarter pixel precision. This option usually results in a sharper image. Unfortunately it has a great impact on bitrate and sometimes the higher bitrate use will prevent it from giving a better image quality at a fixed bitrate. It is better to test with and without this option and see whether it is worth activating.</p>
<dt><code>(no)gmc</code></p>
<dd> Enable Global Motion Compensation, which makes Xvid generate special frames (GMC-frames) which are well suited for Pan/:Zoom/:Rotating images. Whether or not the use of this option will save bits is highly dependent on the source material.</p>
<dt><code>(no)trellis</code></p>
<dd> Trellis Quantization is a kind of adaptive quantization method that saves bits by modifying quantized coefficients to make them more compressible by the entropy encoder. Its impact on quality is good, and if VHQ uses too much CPU for you, this setting can be a good alternative to save a few bits (and gain quality at fixed bitrate) at a lesser cost than with VHQ (default: on).</p>
<dt><code>(no)cartoon</code></p>
<dd> Activate this if your encoded sequence is an anime/:cartoon. It modifies some Xvid internal thresholds so Xvid takes better decisions on frame types and motion vectors for flat looking cartoons.</p>
<dt><code>(no)chroma_me</code></p>
<dd> The usual motion estimation algorithm uses only the luminance information to find the best motion vector. However for some video material, using the chroma planes can help find better vectors. This setting toggles the use of chroma planes for motion estimation (default: on).</p>
<dt><code>(no)chroma_opt</code></p>
<dd> Enable a chroma optimizer prefilter. It will do some extra magic on color information to minimize the stepped-stairs effect on edges. It will improve quality at the cost of encoding speed. It reduces PSNR by nature, as the mathematical deviation to the original picture will get bigger, but the subjective image quality will raise. Since it works with color information, you might want to turn it off when encoding in grayscale.</p>
<dt><code>(no)hq_ac</code></p>
<dd> Activates high-quality prediction of AC coefficients for intra frames from neighbor blocks (default: on).</p>
<dt><code>vhq=&lt;0-4&gt;</code></p>
<dd> The motion search algorithm is based on a search in the usual color domain and tries to find a motion vector that minimizes the difference between the reference frame and the encoded frame. With this setting activated, Xvid will also use the frequency domain (DCT) to search for a motion vector that minimizes not only the spatial difference but also the encoding length of the block. Fastest to slowest:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> off</p>
<dt>1</p>
<dd> mode decision (inter/:intra MB) (default)</p>
<dt>2</p>
<dd> limited search</p>
<dt>3</p>
<dd> medium search</p>
<dt>4</p>
<dd> wide search</dl>
</dl>
<dt><code>(no)lumi_mask</code></p>
<dd> Adaptive quantization allows the macroblock quantizers to vary inside each frame. This is a &#8216;psychosensory&#8217; setting that is supposed to make use of the fact that the human eye tends to notice fewer details in very bright and very dark parts of the picture. It compresses those areas more strongly than medium ones, which will save bits that can be spent again on other frames, raising overall subjective quality and possibly reducing PSNR.</p>
<dt><code>(no)grayscale</code></p>
<dd> Make Xvid discard chroma planes so the encoded video is grayscale only. Note that this does not speed up encoding, it just prevents chroma data from being written in the last stage of encoding.</p>
<dt><code>(no)interlacing</code></p>
<dd> Encode the fields of interlaced video material. Turn this option on for interlaced content.<br />
 <i>NOTE:</i> Should you rescale the video, you would need an interlace-aware resizer, which you can activate with -vf scale=&lt;width&gt;:&lt;height&gt;:1.</p>
<dt><code>min_iquant=&lt;0-31&gt;</code></p>
<dd> minimum I-frame quantizer (default: 2)</p>
<dt><code>max_iquant=&lt;0-31&gt;</code></p>
<dd> maximum I-frame quantizer (default: 31)</p>
<dt><code>min_pquant=&lt;0-31&gt;</code></p>
<dd> minimum P-frame quantizer (default: 2)</p>
<dt><code>max_pquant=&lt;0-31&gt;</code></p>
<dd> maximum P-frame quantizer (default: 31)</p>
<dt><code>min_bquant=&lt;0-31&gt;</code></p>
<dd> minimum B-frame quantizer (default: 2)</p>
<dt><code>max_bquant=&lt;0-31&gt;</code></p>
<dd> maximum B-frame quantizer (default: 31)</p>
<dt><code>min_key_interval=&lt;value&gt; (two pass only)</code></p>
<dd> minimum interval between keyframes (default: 0)</p>
<dt><code>max_key_interval=&lt;value&gt;</code></p>
<dd> maximum interval between keyframes (default: 10*fps)</p>
<dt><code>quant_type=&lt;h263|mpeg&gt;</code></p>
<dd> Sets the type of quantizer to use. For high bitrates, you will find that MPEG quantization preserves more detail. For low bitrates, the smoothing of H.263 will give you less block noise. When using custom matrices, MPEG quantization <code>must</code> be used.</p>
<dt><code>quant_intra_matrix=&lt;filename&gt;</code></p>
<dd> Load a custom intra matrix file. You can build such a file with xvid4conf&#8217;s matrix editor.</p>
<dt><code>quant_inter_matrix=&lt;filename&gt;</code></p>
<dd> Load a custom inter matrix file. You can build such a file with xvid4conf&#8217;s matrix editor.</p>
<dt><code>keyframe_boost=&lt;0-1000&gt; (two pass mode only)</code></p>
<dd> Shift some bits from the pool for other frame types to intra frames, thus improving keyframe quality. This amount is an extra percentage, so a value of 10 will give your keyframes 10% more bits than normal (default: 0).</p>
<dt><code>kfthreshold=&lt;value&gt; (two pass mode only)</code></p>
<dd> Works together with kfreduction. Determines the minimum distance below which you consider that two frames are considered consecutive and treated differently according to kfreduction (default: 10).</p>
<dt><code>kfreduction=&lt;0-100&gt; (two pass mode only)</code></p>
<dd> The above two settings can be used to adjust the size of keyframes that you consider too close to the first (in a row). kfthreshold sets the range in which keyframes are reduced, and kfreduction determines the bitrate reduction they get. The last I-frame will get treated normally (default: 30).</p>
<dt><code>max_bframes=&lt;0-4&gt;</code></p>
<dd> Maximum number of B-frames to put between I/P-frames (default: 2).</p>
<dt><code>bquant_ratio=&lt;0-1000&gt;</code></p>
<dd> quantizer ratio between B- and non-B-frames, 150=1.50 (default: 150)</p>
<dt><code>bquant_offset=&lt;-1000-1000&gt;</code></p>
<dd> quantizer offset between B- and non-B-frames, 100=1.00 (default: 100)</p>
<dt><code>bf_threshold=&lt;-255-255&gt;</code></p>
<dd> This setting allows you to specify what priority to place on the use of B-frames. The higher the value, the higher the probability of B-frames being used (default: 0). Do not forget that B-frames usually have a higher quantizer, and therefore aggressive production of B-frames may cause worse visual quality.</p>
<dt><code>(no)closed_gop</code></p>
<dd> This option tells Xvid to close every GOP (Group Of Pictures bounded by two I-frames), which makes GOPs independent from each other. This just implies that the last frame of the GOP is either a P-frame or a N-frame but not a B-frame. It is usually a good idea to turn this option on (default: on).</p>
<dt><code>(no)packed</code></p>
<dd> This option is meant to solve frame-order issues when encoding to container formats like AVI that cannot cope with out-of-order frames. In practice, most decoders (both software and hardware) are able to deal with frame-order themselves, and may get confused when this option is turned on, so you can safely leave if off, unless you really know what you are doing.<br />
 <i>WARNING:</i> This will generate an illegal bitstream, and will not be decodable by ISO-MPEG-4 decoders except DivX/:libavcodec/:Xvid.<br />
 <i>WARNING:</i> This will also store a fake DivX version in the file so the bug autodetection of some decoders might be confused.</p>
<dt><code>frame_drop_ratio=&lt;0-100&gt; (max_bframes=0 only)</code></p>
<dd> This setting allows the creation of variable framerate video streams. The value of the setting specifies a threshold under which, if the difference of the following frame to the previous frame is below or equal to this threshold, a frame gets not coded (a so called n-vop is placed in the stream). On playback, when reaching an n-vop the previous frame will be displayed.<br />
 <i>WARNING:</i> Playing with this setting may result in a jerky video, so use it at your own risks!</p>
<dt><code>rc_reaction_delay_factor=&lt;value&gt;</code></p>
<dd> This parameter controls the number of frames the CBR rate controller will wait before reacting to bitrate changes and compensating for them to obtain a constant bitrate over an averaging range of frames.</p>
<dt><code>rc_averaging_period=&lt;value&gt;</code></p>
<dd> Real CBR is hard to achieve. Depending on the video material, bitrate can be variable, and hard to predict. Therefore Xvid uses an averaging period for which it guarantees a given amount of bits (minus a small variation). This settings expresses the &quot;number of frames&quot; for which Xvid averages bitrate and tries to achieve CBR.</p>
<dt><code>rc_buffer=&lt;value&gt;</code></p>
<dd> size of the rate control buffer</p>
<dt><code>curve_compression_high=&lt;0-100&gt;</code></p>
<dd> This setting allows Xvid to take a certain percentage of bits away from high bitrate scenes and give them back to the bit reservoir. You could also use this if you have a clip with so many bits allocated to high-bitrate scenes that the low(er)-bitrate scenes start to look bad (default: 0).</p>
<dt><code>curve_compression_low=&lt;0-100&gt;</code></p>
<dd> This setting allows Xvid to give a certain percentage of extra bits to the low bitrate scenes, taking a few bits from the entire clip. This might come in handy if you have a few low-bitrate scenes that are still blocky (default: 0).</p>
<dt><code>overflow_control_strength=&lt;0-100&gt;</code></p>
<dd> During pass one of two pass encoding, a scaled bitrate curve is computed. The difference between that expected curve and the result obtained during encoding is called overflow. Obviously, the two pass rate controller tries to compensate for that overflow, distributing it over the next frames. This setting controls how much of the overflow is distributed every time there is a new frame. Low values allow lazy overflow control, big rate bursts are compensated for more slowly (could lead to lack of precision for small clips). Higher values will make changes in bit redistribution more abrupt, possibly too abrupt if you set it too high, creating artifacts (default: 5).<br />
 <i>NOTE:</i> This setting impacts quality a lot, play with it carefully!</p>
<dt><code>max_overflow_improvement=&lt;0-100&gt;</code></p>
<dd> During the frame bit allocation, overflow control may increase the frame size. This parameter specifies the maximum percentage by which the overflow control is allowed to increase the frame size, compared to the ideal curve allocation (default: 5).</p>
<dt><code>max_overflow_degradation=&lt;0-100&gt;</code></p>
<dd> During the frame bit allocation, overflow control may decrease the frame size. This parameter specifies the maximum percentage by which the overflow control is allowed to decrease the frame size, compared to the ideal curve allocation (default: 5).</p>
<dt><code>container_frame_overhead=&lt;0&#8230;&gt;</code></p>
<dd> Specifies a frame average overhead per frame, in bytes. Most of the time users express their target bitrate for video w/o taking care of the video container overhead. This small but (mostly) constant overhead can cause the target file size to be exceeded. Xvid allows users to set the amount of overhead per frame the container generates (give only an average per frame). 0 has a special meaning, it lets Xvid use its own default values (default: 24 &#8211; AVI average overhead).</p>
<dt><code>profile=&lt;profile_name&gt;</code></p>
<dd> Restricts options and VBV (peak bitrate over a short period) according to the Simple, Advanced Simple and DivX profiles. The resulting videos should be playable on standalone players adhering to these profile specifications.</p>
<dl>
<dt>
<dd>
<dl>
<dt>unrestricted</p>
<dd> no restrictions (default)</p>
<dt>sp0&nbsp;<wbr>&nbsp;</p>
<dd> simple profile at level 0</p>
<dt>sp1&nbsp;<wbr>&nbsp;</p>
<dd> simple profile at level 1</p>
<dt>sp2&nbsp;<wbr>&nbsp;</p>
<dd> simple profile at level 2</p>
<dt>sp3&nbsp;<wbr>&nbsp;</p>
<dd> simple profile at level 3</p>
<dt>sp4a&nbsp;<wbr>&nbsp;</p>
<dd> simple profile at level 4a</p>
<dt>sp5&nbsp;<wbr>&nbsp;</p>
<dd> simple profile at level 5</p>
<dt>sp6&nbsp;<wbr>&nbsp;</p>
<dd> simple profile at level 6</p>
<dt>asp0&nbsp;</p>
<dd> advanced simple profile at level 0</p>
<dt>asp1&nbsp;</p>
<dd> advanced simple profile at level 1</p>
<dt>asp2&nbsp;</p>
<dd> advanced simple profile at level 2</p>
<dt>asp3&nbsp;</p>
<dd> advanced simple profile at level 3</p>
<dt>asp4&nbsp;</p>
<dd> advanced simple profile at level 4</p>
<dt>asp5&nbsp;</p>
<dd> advanced simple profile at level 5</p>
<dt>dxnhandheld</p>
<dd> DXN handheld profile</p>
<dt>dxnportntsc</p>
<dd> DXN portable NTSC profile</p>
<dt>dxnportpal</p>
<dd> DXN portable PAL profile</p>
<dt>dxnhtntsc</p>
<dd> DXN home theater NTSC profile</p>
<dt>dxnhtpal</p>
<dd> DXN home theater PAL profile</p>
<dt>dxnhdtv</p>
<dd> DXN HDTV profile</dl>
</dl>
<dl>
<dt>
<dd> <i>NOTE:</i> These profiles should be used in conjunction with an appropriate -ffourcc. Generally DX50 is applicable, as some players do not recognize Xvid but most recognize DivX.</dl>
<dt><code>par=&lt;mode&gt;</code></p>
<dd> Specifies the Pixel Aspect Ratio mode (not to be confused with DAR, the Display Aspect Ratio). PAR is the ratio of the width and height of a single pixel. So both are related like this: DAR = PAR * (width/height).<br />
 MPEG-4 defines 5 pixel aspect ratios and one extended one, giving the opportunity to specify a specific pixel aspect ratio. 5 standard modes can be specified:</p>
<dl>
<dt>
<dd>
<dl>
<dt>vga11</p>
<dd> It is the usual PAR for PC content. Pixels are a square unit.</p>
<dt>pal43</p>
<dd> PAL standard 4:3 PAR. Pixels are rectangles.</p>
<dt>pal169</p>
<dd> same as above</p>
<dt>ntsc43</p>
<dd> same as above</p>
<dt>ntsc169</p>
<dd> same as above (Do not forget to give the exact ratio.)</p>
<dt>ext&nbsp;<wbr>&nbsp;</p>
<dd> Allows you to specify your own pixel aspect ratio with par_width and par_height.</dl>
</dl>
<dl>
<dt>
<dd> <i>NOTE:</i> In general, setting aspect and autoaspect options is enough.</dl>
<dt><code>par_width=&lt;1-255&gt; (par=ext only)</code></p>
<dd> Specifies the width of the custom pixel aspect ratio.</p>
<dt><code>par_height=&lt;1-255&gt; (par=ext only)</code></p>
<dd> Specifies the height of the custom pixel aspect ratio.</p>
<dt><code>aspect=&lt;x/y | f (float value)&gt;</code></p>
<dd> Store movie aspect internally, just like MPEG files. Much nicer solution than rescaling, because quality is not decreased. MPlayer and a few others players will play these files correctly, others will display them with the wrong aspect. The aspect parameter can be given as a ratio or a floating point number.</p>
<dt><code>(no)autoaspect</code></p>
<dd> Same as the aspect option, but automatically computes aspect, taking into account all the adjustments (crop/:expand/:scale/:etc.) made in the filter chain.</p>
<dt><code>psnr&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Print the PSNR (peak signal to noise ratio) for the whole video after encoding and store the per frame PSNR in a file with a name like &#8216;psnr_hhmmss.log&#8217; in the current directory. Returned values are in dB (decibel), the higher the better.</p>
<dt><code>debug&nbsp;<wbr>&nbsp;</code></p>
<dd> Save per-frame statistics in ./xvid.dbg. (This is not the two pass control file.)</dl>
<p> The following options are only available in Xvid 1.1.x and later.</p>
<dl>
<dt><code>bvhq=&lt;0|1&gt;</code></p>
<dd> This setting allows vector candidates for B-frames to be used for the encoding chosen using a rate distortion optimized operator, which is what is done for P-frames by the vhq option. This produces nicer-looking B-frames while incurring almost no performance penalty (default: 1).</p>
<dt><code>vbv_bufsize=&lt;0&#8230;&gt; (two pass mode only)</code></p>
<dd> Specify the video buffering verifier (VBV) buffer size in bits (default: 0 &#8211; VBV check disabled). VBV allows restricting peak bitrate to make the video play properly on hardware players. For example, the Home profile uses vbv_bufsize=3145728. If you set vbv_bufsize you should set also vbv_maxrate. Note that there is no vbv_peakrate because Xvid does not actually use it for bitrate controlling; the other VBV options are enough to restrict the peak bitrate.</p>
<dt><code>vbv_initial=&lt;0&#8230;vbv_bufsize&gt; (two pass mode only)</code></p>
<dd> Specify the initial fill of the VBV buffer in bits (default: 75% of vbv_bufsize). The default is probably what you want.</p>
<dt><code>vbv_maxrate=&lt;0&#8230;&gt; (two pass mode only)</code></p>
<dd> Specify the maximum processing rate in bits/s (default: 0). For example, the Home profile uses vbv_maxrate=4854000.</dl>
<p> The following option is only available in Xvid 1.2.x and later.</p>
<dl>
<dt><code>threads=&lt;0-n&gt;</code></p>
<dd> Create n threads to run the motion estimation (default: 0). The maximum number of threads that can be used is the picture height divided by 16.</dl>
<h3>x264enc (-x264encopts)</h3>
<dl>
<dt><code>bitrate=&lt;value&gt;</code></p>
<dd> Sets the average bitrate to be used in kbits/:second (default: off). Since local bitrate may vary, this average may be inaccurate for very short videos (see ratetol). Constant bitrate can be achieved by combining this with vbv_maxrate, at significant reduction in quality.</p>
<dt><code>qp=&lt;0-51&gt;</code></p>
<dd> This selects the quantizer to use for P-frames. I- and B-frames are offset from this value by ip_factor and pb_factor, respectively. 20-40 is a useful range. Lower values result in better fidelity, but higher bitrates. 0 is lossless. Note that quantization in H.264 works differently from MPEG-1/2/4: H.264&#8217;s quantization parameter (QP) is on a logarithmic scale. The mapping is approximately H264QP = 12 + 6*log2(MPEGQP). For example, MPEG at QP=2 is equivalent to H.264 at QP=18. Generally, this option should be avoided and crf should be used instead as crf will yield better visual results for the same size.</p>
<dt><code>crf=&lt;1.0-50.0&gt;</code></p>
<dd> Enables constant quality mode, and selects the quality. The scale is similar to QP. Like the bitrate-based modes, this allows each frame to use a different QP based on the frame&#8217;s complexity. This option should generally be used instead of qp.</p>
<dt><code>crf_max=&lt;float&gt;</code></p>
<dd> With CRF and VBV, limit RF to this value (may cause VBV underflows!).</p>
<dt><code>pass=&lt;1-3&gt;</code></p>
<dd> Enable 2 or 3-pass mode. It is recommended to always encode in 2 or 3-pass mode as it leads to a better bit distribution and improves overall quality.</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> first pass</p>
<dt>2</p>
<dd> second pass (of two pass encoding)</p>
<dt>3</p>
<dd> Nth pass (second and third passes of three pass encoding)</dl>
</dl>
<dl>
<dt>
<dd> Here is how it works, and how to use it:<br />
 The first pass (pass=1) collects statistics on the video and writes them to a file. You might want to deactivate some CPU-hungry options, apart from the ones that are on by default.<br />
 In two pass mode, the second pass (pass=2) reads the statistics file and bases ratecontrol decisions on it.<br />
 In three pass mode, the second pass (pass=3, that is not a typo) does both: It first reads the statistics, then overwrites them. You can use all encoding options, except very CPU-hungry options.<br />
 The third pass (pass=3) is the same as the second pass, except that it has the second pass&#8217; statistics to work from. You can use all encoding options, including CPU-hungry ones.<br />
 The first pass may use either average bitrate or constant quantizer. ABR is recommended, since it does not require guessing a quantizer. Subsequent passes are ABR, and must specify bitrate.</dl>
<dt><code>profile=&lt;name&gt;</code></p>
<dd> Constrain options to be compatible with an H.264 profile.</p>
<dl>
<dt>
<dd>
<dl>
<dt>baseline</p>
<dd> no8x8dct bframes=0 nocabac cqm=flat weightp=0 nointerlaced qp&gt;0</p>
<dt>main</p>
<dd> no8x8dct cqm=flat qp&gt;0</p>
<dt>high</p>
<dd> qp&gt;0 (default)</dl>
</dl>
<dt><code>preset=&lt;name&gt;</code></p>
<dd> Use a preset to select encoding settings.</p>
<dl>
<dt>
<dd>
<dl>
<dt>ultrafast</p>
<dd> no8x8dct aq_mode=0 b_adapt=0 bframes=0 nodeblock nombtree me=dia nomixed_refs partitions=none ref=1 scenecut=0 subq=0 trellis=0 noweight_b weightp=0</p>
<dt>superfast</p>
<dd> nombtree me=dia nomixed_refs partitions=i8x8,i4x4 ref=1 subq=1 trellis=0 weightp=0</p>
<dt>veryfast</p>
<dd> nombtree nomixed_refs ref=1 subq=2 trellis=0 weightp=0</p>
<dt>faster</p>
<dd> nomixed_refs rc_lookahead=20 ref=5 subq=4 weightp=1</p>
<dt>fast</p>
<dd> rc_lookahead=30 ref=2 subq=6</p>
<dt>medium</p>
<dd> Default settings apply.</p>
<dt>slow</p>
<dd> b_adapt=2 direct=auto me=umh rc_lookahead=50 ref=5 subq=8</p>
<dt>slower</p>
<dd> b_adapt=2 direct=auto me=umh partitions=all rc_lookahead=60 ref=8 subq=9 trellis=2</p>
<dt>veryslow</p>
<dd> b_adapt=2 b_frames=8 direct=auto me=umh me_range=24 partitions=all ref=16 subq=10 trellis=2 rc_lookahead=60</p>
<dt>placebo</p>
<dd> bframes=16 b_adapt=2 direct=auto nofast_pskip me=tesa me_range=24 partitions=all rc_lookahead=60 ref=16 subq=10 trellis=2</dl>
</dl>
<dt><code>tune=&lt;name,[name,&#8230;]&gt;</code></p>
<dd> Tune the settings for a particular type of source or situation. All tuned settings are overridden by explicit user-settings. Multiple tunings are separated by commas, but only one psy tuning can be used at a time.</p>
<dl>
<dt>
<dd>
<dl>
<dt>film (psy tuning)</p>
<dd> deblock=-1,-1 psy-rd=&lt;unset&gt;,0.15</p>
<dt>animation (psy tuning)</p>
<dd> b_frames={+2} deblock=1,1 psy-rd=0.4:&lt;unset&gt; aq_strength=0.6 ref={double if &gt;1 else 1}</p>
<dt>grain (psy tuning)</p>
<dd> aq_strength=0.5 nodct_decimate deadzone_inter=6 deadzone_intra=6 deblock=-2,-2 ipratio=1.1 pbratio=1.1 psy-rd=&lt;unset&gt;,0.25 qcomp=0.8</p>
<dt>stillimage (psy tuning)</p>
<dd> aq_strength=1.2 deblock=-3,-3 psy-rd=2.0,0.7</p>
<dt>psnr (psy tuning)</p>
<dd> aq_mode=0 nopsy</p>
<dt>ssim (psy tuning)</p>
<dd> aq_mode=2 nopsy</p>
<dt>fastdecode</p>
<dd> nocabac nodeblock noweight_b weightp=0</p>
<dt>zerolatency</p>
<dd> bframes=0 force_cfr rc_lookahead=0 sync_lookahead=0 sliced_threads</dl>
</dl>
<dt><code>slow_firstpass</code></p>
<dd> Disables the following faster options with pass=1: no_8x8dct me=dia partitions=none ref=1 subq={2 if &gt;2 else unchanged} trellis=0 fast_pskip. These settings significantly improve encoding speed while having little or no impact on the quality of the final pass.<br />
 This option is implied with preset=placebo.</p>
<dt><code>keyint=&lt;value&gt;</code></p>
<dd> Sets maximum interval between IDR-frames (default: 250). Larger values save bits, thus improve quality, at the cost of seeking precision. Unlike MPEG-1/2/4, H.264 does not suffer from DCT drift with large values of keyint.</p>
<dt><code>keyint_min=&lt;1-keyint/2&gt;</code></p>
<dd> Sets minimum interval between IDR-frames (default: auto). If scenecuts appear within this interval, they are still encoded as I-frames, but do not start a new GOP. In H.264, I-frames do not necessarily bound a closed GOP because it is allowable for a P-frame to be predicted from more frames than just the one frame before it (also see frameref). Therefore, I-frames are not necessarily seekable. IDR-frames restrict subsequent P-frames from referring to any frame prior to the IDR-frame.</p>
<dt><code>scenecut=&lt;-1-100&gt;</code></p>
<dd> Controls how aggressively to insert extra I-frames (default: 40). With small values of scenecut, the codec often has to force an I-frame when it would exceed keyint. Good values of scenecut may find a better location for the I-frame. Large values use more I-frames than necessary, thus wasting bits. -1 disables scene-cut detection, so I-frames are inserted only once every other keyint frames, even if a scene-cut occurs earlier. This is not recommended and wastes bitrate as scenecuts encoded as P-frames are just as big as I-frames, but do not reset the &quot;keyint counter&quot;.</p>
<dt><code>(no)intra_refresh</code></p>
<dd> Periodic intra block refresh instead of keyframes (default: disabled). This option disables IDR-frames, and, instead, uses a moving vertical bar of intra-coded blocks. This reduces compression efficiency but benefits low-latency streaming and resilience to packet loss.</p>
<dt><code>frameref=&lt;1-16&gt;</code></p>
<dd> Number of previous frames used as predictors in B- and P-frames (default: 3). This is effective in anime, but in live-action material the improvements usually drop off very rapidly above 6 or so reference frames. This has no effect on decoding speed, but does increase the memory needed for decoding. Some decoders can only handle a maximum of 15 reference frames.</p>
<dt><code>bframes=&lt;0-16&gt;</code></p>
<dd> maximum number of consecutive B-frames between I- and P-frames (default: 3)</p>
<dt><code>(no)b_adapt</code></p>
<dd> Automatically decides when to use B-frames and how many, up to the maximum specified above (default: on). If this option is disabled, then the maximum number of B-frames is used.</p>
<dt><code>b_bias=&lt;-100-100&gt;</code></p>
<dd> Controls the decision performed by b_adapt. A higher b_bias produces more B-frames (default: 0).</p>
<dt><code>b_pyramid=&lt;normal|strict|none&gt;</code></p>
<dd> Allows B-frames to be used as references for predicting other frames. For example, consider 3 consecutive B-frames: I0 B1 B2 B3 P4. Without this option, B-frames follow the same pattern as MPEG-[124]. So they are coded in the order I0 P4 B1 B2 B3, and all the B-frames are predicted from I0 and P4. With this option, they are coded as I0 P4 B2 B1 B3. B2 is the same as above, but B1 is predicted from I0 and B2, and B3 is predicted from B2 and P4. This usually results in slightly improved compression, at almost no speed cost. However, this is an experimental option: it is not fully tuned and may not always help. Requires bframes &gt;= 2. Disadvantage: increases decoding delay to 2 frames.</p>
<dl>
<dt>
<dd>
<dl>
<dt>normal</p>
<dd> Allow B-frames as references as described above (not Blu-ray compatible).</p>
<dt>strict</p>
<dd> Disallow P-frames referencing B-frames. Gives worse compression, but is required for Blu-ray compatibility.</p>
<dt>none&nbsp;</p>
<dd> Disable using B-frames as references.</dl>
</dl>
<dt><code>(no)open_gop</code></p>
<dd> Use recovery points to close GOPs; only available with bframes.</p>
<dt><code>(no)bluray_compat</code></p>
<dd> Enable compatibility hacks for Blu-Ray support.</p>
<dt><code>(no)fake_interlaced</code></p>
<dd> Flag stream as interlaced but encode progressive. Makes it posssible to encode 25p and 30p Blu-Ray streams. Ignored in interlaced mode.</p>
<dt><code>frame_packing=&lt;0-5&gt;</code></p>
<dd> Define frame arrangement for stereoscopic videos.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Checkerboard &#8211; pixels are alternately from L and R.</p>
<dt>1</p>
<dd> Column alternation &#8211; L and R are interlaced by column.</p>
<dt>2</p>
<dd> Row alternation &#8211; L and R are interlaced by row.</p>
<dt>3</p>
<dd> Side by side &#8211; L is on the left, R is on the right.</p>
<dt>4</p>
<dd> Top-bottom &#8211; L is on top, R is on the bottom.</p>
<dt>5</p>
<dd> Frame alternation &#8211; one view per frame.</dl>
</dl>
<dt><code>(no)deblock</code></p>
<dd> Use deblocking filter (default: on). As it takes very little time compared to its quality gain, it is not recommended to disable it.</p>
<dt><code>deblock=&lt;-6-6&gt;,&lt;-6-6&gt;</code></p>
<dd> The first parameter is AlphaC0 (default: 0). This adjusts thresholds for the H.264 in-loop deblocking filter. First, this parameter adjusts the maximum amount of change that the filter is allowed to cause on any one pixel. Secondly, this parameter affects the threshold for difference across the edge being filtered. A positive value reduces blocking artifacts more, but will also smear details.<br />
 The second parameter is Beta (default: 0). This affects the detail threshold. Very detailed blocks are not filtered, since the smoothing caused by the filter would be more noticeable than the original blocking.<br />
 The default behavior of the filter almost always achieves optimal quality, so it is best to either leave it alone, or make only small adjustments. However, if your source material already has some blocking or noise which you would like to remove, it may be a good idea to turn it up a little bit.</p>
<dt><code>(no)cabac</code></p>
<dd> Use CABAC (Context-Adaptive Binary Arithmetic Coding) (default: on). Slightly slows down encoding and decoding, but should save 10-15% bitrate. Unless you are looking for decoding speed, you should not disable it.</p>
<dt><code>qp_min=&lt;1-51&gt; (ABR or two pass)</code></p>
<dd> Minimum quantizer, 10-30 seems to be a useful range (default: 10).</p>
<dt><code>qp_max=&lt;1-51&gt; (ABR or two pass)</code></p>
<dd> maximum quantizer (default: 51)</p>
<dt><code>qp_step=&lt;1-50&gt; (ABR or two pass)</code></p>
<dd> maximum value by which the quantizer may be incremented/decremented between frames (default: 4)</p>
<dt><code>(no)mbtree</code></p>
<dd> Enable macroblock tree ratecontrol (default: enabled). Use a large lookahead to track temporal propagation of data and weight quality accordingly. In multi-pass mode, this writes to a separate stats file named &lt;passlogfile&gt;.mbtree.</p>
<dt><code>rc_lookahead=&lt;0-250&gt;</code></p>
<dd> Adjust the mbtree lookahead distance (default: 40). Larger values will be slower and cause x264 to consume more memory, but can yield higher quality.</p>
<dt><code>ratetol=&lt;0.1-100.0&gt; (ABR or two pass)</code></p>
<dd> allowed variance in average bitrate (no particular units) (default: 1.0)</p>
<dt><code>vbv_maxrate=&lt;value&gt; (ABR or two pass)</code></p>
<dd> maximum local bitrate, in kbits/:second (default: disabled)</p>
<dt><code>vbv_bufsize=&lt;value&gt; (ABR or two pass)</code></p>
<dd> averaging period for vbv_maxrate, in kbits (default: none, must be specified if vbv_maxrate is enabled)</p>
<dt><code>vbv_init=&lt;0.0-1.0&gt; (ABR or two pass)</code></p>
<dd> initial buffer occupancy, as a fraction of vbv_bufsize (default: 0.9)</p>
<dt><code>ip_factor=&lt;value&gt;</code></p>
<dd> quantizer factor between I- and P-frames (default: 1.4)</p>
<dt><code>pb_factor=&lt;value&gt;</code></p>
<dd> quantizer factor between P- and B-frames (default: 1.3)</p>
<dt><code>qcomp=&lt;0-1&gt; (ABR or two pass)</code></p>
<dd> quantizer compression (default: 0.6). A lower value makes the bitrate more constant, while a higher value makes the quantization parameter more constant.</p>
<dt><code>cplx_blur=&lt;0-999&gt; (two pass only)</code></p>
<dd> Temporal blur of the estimated frame complexity, before curve compression (default: 20). Lower values allow the quantizer value to jump around more, higher values force it to vary more smoothly. cplx_blur ensures that each I-frame has quality comparable to the following P-frames, and ensures that alternating high and low complexity frames (e.g. low fps animation) do not waste bits on fluctuating quantizer.</p>
<dt><code>qblur=&lt;0-99&gt; (two pass only)</code></p>
<dd> Temporal blur of the quantization parameter, after curve compression (default: 0.5). Lower values allow the quantizer value to jump around more, higher values force it to vary more smoothly.</p>
<dt><code>zones=&lt;zone0&gt;[/&lt;zone1&gt;[/&#8230;]]</code></p>
<dd> User specified quality for specific parts (ending, credits, &#8230;). Each zone is &lt;start-frame&gt;,&lt;end-frame&gt;,&lt;option&gt; where option may be</p>
<dl>
<dt>
<dd>
<dl>
<dt>q=&lt;0-51&gt;</p>
<dd> quantizer</p>
<dt>b=&lt;0.01-100.0&gt;</p>
<dd> bitrate multiplier</dl>
</dl>
<dl>
<dt>
<dd> <i>NOTE:</i> The quantizer option is not strictly enforced. It affects only the planning stage of ratecontrol, and is still subject to overflow compensation and qp_min/qp_max.</dl>
<dt><code>direct_pred=&lt;name&gt;</code></p>
<dd> Determines the type of motion prediction used for direct macroblocks in B-frames.</p>
<dl>
<dt>
<dd>
<dl>
<dt>none</p>
<dd> Direct macroblocks are not used.</p>
<dt>spatial</p>
<dd> Motion vectors are extrapolated from neighboring blocks. (default)</p>
<dt>temporal</p>
<dd> Motion vectors are extrapolated from the following P-frame.</p>
<dt>auto</p>
<dd> The codec selects between spatial and temporal for each frame.</dl>
</dl>
<dl>
<dt>
<dd> Spatial and temporal are approximately the same speed and PSNR, the choice between them depends on the video content. Auto is slightly better, but slower. Auto is most effective when combined with multipass. direct_pred=none is both slower and lower quality.</dl>
<dt><code>weightp</code></p>
<dd> Weighted P-frame prediction mode (default: 2).</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled (fastest)</p>
<dt>1</p>
<dd> weighted refs (better quality)</p>
<dt>2</p>
<dd> weighted refs + duplicates (best)</dl>
</dl>
<dt><code>(no)weight_b</code></p>
<dd> Use weighted prediction in B-frames. Without this option, bidirectionally predicted macroblocks give equal weight to each reference frame. With this option, the weights are determined by the temporal position of the B-frame relative to the references. Requires bframes &gt; 1.</p>
<dt><code>partitions=&lt;list&gt;</code></p>
<dd> Enable some optional macroblock types (default: p8x8,b8x8,i8x8,i4x4).</p>
<dl>
<dt>
<dd>
<dl>
<dt>p8x8</p>
<dd> Enable types p16x8, p8x16, p8x8.</p>
<dt>p4x4</p>
<dd> Enable types p8x4, p4x8, p4x4. p4x4 is recommended only with subq &gt;= 5, and only at low resolutions.</p>
<dt>b8x8</p>
<dd> Enable types b16x8, b8x16, b8x8.</p>
<dt>i8x8</p>
<dd> Enable type i8x8. i8x8 has no effect unless 8x8dct is enabled.</p>
<dt>i4x4</p>
<dd> Enable type i4x4.</p>
<dt>all</p>
<dd> Enable all of the above types.</p>
<dt>none</p>
<dd> Disable all of the above types.</dl>
</dl>
<dl>
<dt>
<dd> Regardless of this option, macroblock types p16x16, b16x16, and i16x16 are always enabled.<br />
 The idea is to find the type and size that best describe a certain area of the picture. For example, a global pan is better represented by 16&#215;16 blocks, while small moving objects are better represented by smaller blocks.</dl>
<dt><code>(no)8x8dct</code></p>
<dd> Adaptive spatial transform size: allows macroblocks to choose between 4&#215;4 and 8&#215;8 DCT. Also allows the i8x8 macroblock type. Without this option, only 4&#215;4 DCT is used.</p>
<dt><code>me=&lt;name&gt;</code></p>
<dd> Select fullpixel motion estimation algorithm.</p>
<dl>
<dt>
<dd>
<dl>
<dt>dia</p>
<dd> diamond search, radius 1 (fast)</p>
<dt>hex</p>
<dd> hexagon search, radius 2 (default)</p>
<dt>umh</p>
<dd> uneven multi-hexagon search (slow)</p>
<dt>esa</p>
<dd> exhaustive search (very slow, and no better than umh)</dl>
</dl>
<dt><code>me_range=&lt;4-64&gt;</code></p>
<dd> radius of exhaustive or multi-hexagon motion search (default: 16)</p>
<dt><code>subq=&lt;0-11&gt;</code></p>
<dd> Adjust subpel refinement quality. This parameter controls quality versus speed tradeoffs involved in the motion estimation decision process. subq=5 can compress up to 10% better than subq=1.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Runs fullpixel precision motion estimation on all candidate macroblock types. Then selects the best type with SAD metric (faster than subq=1, not recommended unless you&#8217;re looking for ultra-fast encoding).</p>
<dt>1</p>
<dd> Does as 0, then refines the motion of that type to fast quarterpixel precision (fast).</p>
<dt>2</p>
<dd> Runs halfpixel precision motion estimation on all candidate macroblock types. Then selects the best type with SATD metric. Then refines the motion of that type to fast quarterpixel precision.</p>
<dt>3</p>
<dd> As 2, but uses a slower quarterpixel refinement.</p>
<dt>4</p>
<dd> Runs fast quarterpixel precision motion estimation on all candidate macroblock types. Then selects the best type with SATD metric. Then finishes the quarterpixel refinement for that type.</p>
<dt>5</p>
<dd> Runs best quality quarterpixel precision motion estimation on all candidate macroblock types, before selecting the best type. Also refines the two motion vectors used in bidirectional macroblocks with SATD metric, rather than reusing vectors from the forward and backward searches.</p>
<dt>6</p>
<dd> Enables rate-distortion optimization of macroblock types in I- and P-frames.</p>
<dt>7</p>
<dd> Enables rate-distortion optimization of macroblock types in all frames (default).</p>
<dt>8</p>
<dd> Enables rate-distortion optimization of motion vectors and intra prediction modes in I- and P-frames.</p>
<dt>9</p>
<dd> Enables rate-distortion optimization of motion vectors and intra prediction modes in all frames.</p>
<dt>10</p>
<dd> QP-RD; requires trellis=2 and aq_mode=1 or higher (best).</p>
<dt>11</p>
<dd> Full RD; disable all early terminations.</dl>
</dl>
<dl>
<dt>
<dd> In the above, &quot;all candidates&quot; does not exactly mean all enabled types: 4&#215;4, 4&#215;8, 8&#215;4 are tried only if 8&#215;8 is better than 16&#215;16.</dl>
<dt><code>(no)chroma_me</code></p>
<dd> Takes into account chroma information during subpixel motion search (default: enabled). Requires subq&gt;=5.</p>
<dt><code>(no)mixed_refs</code></p>
<dd> Allows each 8&#215;8 or 16&#215;8 motion partition to independently select a reference frame. Without this option, a whole macroblock must use the same reference. Requires frameref&gt;1.</p>
<dt><code>trellis=&lt;0-2&gt; (cabac only)</code></p>
<dd> rate-distortion optimal quantization</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled</p>
<dt>1</p>
<dd> enabled only for the final encode (default)</p>
<dt>2</p>
<dd> enabled during all mode decisions (slow, requires subq&gt;=6)</dl>
</dl>
<dt><code>psy-rd=rd[,trell]</code></p>
<dd> Sets the strength of the psychovisual optimization.</p>
<dl>
<dt>
<dd>
<dl>
<dt>rd=&lt;0.0-10.0&gt;</p>
<dd> psy optimization strength (requires subq&gt;=6) (default: 1.0)</p>
<dt>trell=&lt;0.0-10.0&gt;</p>
<dd> trellis (requires trellis, experimental) (default: 0.0)</dl>
</dl>
<dt><code>(no)psy</code></p>
<dd> Enable psychovisual optimizations that hurt PSNR and SSIM but ought to look better (default: enabled).</p>
<dt><code>deadzone_inter=&lt;0-32&gt;</code></p>
<dd> Set the size of the inter luma quantization deadzone for non-trellis quantization (default: 21). Lower values help to preserve fine details and film grain (typically useful for high bitrate/quality encode), while higher values help filter out these details to save bits that can be spent again on other macroblocks and frames (typically useful for bitrate-starved encodes). It is recommended that you start by tweaking deadzone_intra before changing this parameter.</p>
<dt><code>deadzone_intra=&lt;0-32&gt;</code></p>
<dd> Set the size of the intra luma quantization deadzone for non-trellis quantization (default: 11). This option has the same effect as deadzone_inter except that it affects intra frames. It is recommended that you start by tweaking this parameter before changing deadzone_inter.</p>
<dt><code>(no)fast_pskip</code></p>
<dd> Performs early skip detection in P-frames (default: enabled). This usually improves speed at no cost, but it can sometimes produce artifacts in areas with no details, like sky.</p>
<dt><code>(no)dct_decimate</code></p>
<dd> Eliminate dct blocks in P-frames containing only a small single coefficient (default: enabled). This will remove some details, so it will save bits that can be spent again on other frames, hopefully raising overall subjective quality. If you are compressing non-anime content with a high target bitrate, you may want to disable this to preserve as much detail as possible.</p>
<dt><code>nr=&lt;0-100000&gt;</code></p>
<dd> Noise reduction, 0 means disabled. 100-1000 is a useful range for typical content, but you may want to turn it up a bit more for very noisy content (default: 0). Given its small impact on speed, you might want to prefer to use this over filtering noise away with video filters like denoise3d or hqdn3d.</p>
<dt><code>chroma_qp_offset=&lt;-12-12&gt;</code></p>
<dd> Use a different quantizer for chroma as compared to luma. Useful values are in the range &lt;-2-2&gt; (default: 0).</p>
<dt><code>aq_mode=&lt;0-2&gt;</code></p>
<dd> Defines how adaptive quantization (AQ) distributes bits:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disabled</p>
<dt>1</p>
<dd> Avoid moving bits between frames.</p>
<dt>2</p>
<dd> Move bits between frames (by default).</dl>
</dl>
<dt><code>aq_strength=&lt;positive float value&gt;</code></p>
<dd> Controls how much adaptive quantization (AQ) reduces blocking and blurring in flat and textured areas (default: 1.0). A value of 0.5 will lead to weak AQ and less details, when a value of 1.5 will lead to strong AQ and more details.</p>
<dt><code>cqm=&lt;flat|jvt|&lt;filename&gt;&gt;</code></p>
<dd> Either uses a predefined custom quantization matrix or loads a JM format matrix file.</p>
<dl>
<dt>
<dd>
<dl>
<dt>flat&nbsp;</p>
<dd> Use the predefined flat 16 matrix (default).</p>
<dt>jvt&nbsp;<wbr>&nbsp;</p>
<dd> Use the predefined JVT matrix.</p>
<dt>&lt;filename&gt;</p>
<dd> Use the provided JM format matrix file.</dl>
</dl>
<dl>
<dt>
<dd> <i>NOTE:</i> Windows CMD.EXE users may experience problems with parsing the command line if they attempt to use all the CQM lists. This is due to a command line length limitation. In this case it is recommended the lists be put into a JM format CQM file and loaded as specified above.</dl>
<dt><code>cqm4iy=&lt;list&gt; (also see cqm)</code></p>
<dd> Custom 4&#215;4 intra luminance matrix, given as a list of 16 comma separated values in the 1-255 range.</p>
<dt><code>cqm4ic=&lt;list&gt; (also see cqm)</code></p>
<dd> Custom 4&#215;4 intra chrominance matrix, given as a list of 16 comma separated values in the 1-255 range.</p>
<dt><code>cqm4py=&lt;list&gt; (also see cqm)</code></p>
<dd> Custom 4&#215;4 inter luminance matrix, given as a list of 16 comma separated values in the 1-255 range.</p>
<dt><code>cqm4pc=&lt;list&gt; (also see cqm)</code></p>
<dd> Custom 4&#215;4 inter chrominance matrix, given as a list of 16 comma separated values in the 1-255 range.</p>
<dt><code>cqm8iy=&lt;list&gt; (also see cqm)</code></p>
<dd> Custom 8&#215;8 intra luminance matrix, given as a list of 64 comma separated values in the 1-255 range.</p>
<dt><code>cqm8py=&lt;list&gt; (also see cqm)</code></p>
<dd> Custom 8&#215;8 inter luminance matrix, given as a list of 64 comma separated values in the 1-255 range.</p>
<dt><code>level_idc=&lt;10-51&gt;</code></p>
<dd> Set the bitstream&#8217;s level as defined by annex A of the H.264 standard (default: 51 &#8211; level 5.1). This is used for telling the decoder what capabilities it needs to support. Use this parameter only if you know what it means, and you have a need to set it.</p>
<dt><code>(no)cpu_independent</code></p>
<dd> Ensure exact reproducibility across different CPUs instead of chosing different algorithms when available/better (default:enabled).</p>
<dt><code>threads=&lt;0-16&gt;</code></p>
<dd> Spawn threads to encode in parallel on multiple CPUs (default: 0). This has a slight penalty to compression quality. 0 or &#8216;auto&#8217; tells x264 to detect how many CPUs you have and pick an appropriate number of threads.</p>
<dt><code>(no)sliced_threads</code></p>
<dd> Use slice-based threading (default: disabled). Unlike normal threading, this option adds no encoding latency, but is slightly slower and less effective at compression.</p>
<dt><code>slice_max_size=&lt;0 or positive integer&gt;</code></p>
<dd> Maximum slice size in bytes (default: 0). A value of zero disables the maximum.</p>
<dt><code>slice_max_mbs=&lt;0 or positive integer&gt;</code></p>
<dd> Maximum slice size in number of macroblocks (default: 0). A value of zero disables the maximum.</p>
<dt><code>slices=&lt;0 or positive integer&gt;</code></p>
<dd> Maximum number of slices per frame (default: 0). A value of zero disables the maximum.</p>
<dt><code>sync_lookahead=&lt;0-250&gt;</code></p>
<dd> Adjusts the size of the threaded lookahead buffer (default: 0). 0 or &#8216;auto&#8217; tells x264 to automatically determine buffer size.</p>
<dt><code>(no)deterministic</code></p>
<dd> Use only deterministic optimizations with multithreaded encoding (default: enabled).</p>
<dt><code>(no)global_header</code></p>
<dd> Causes SPS and PPS to appear only once, at the beginning of the bitstream (default: disabled). Some players, such as the Sony PSP, require the use of this option. The default behavior causes SPS and PPS to repeat prior to each IDR frame.</p>
<dt><code>(no)tff</code></p>
<dd> Enable interlaced mode, top field first (default: disabled)</p>
<dt><code>(no)bff</code></p>
<dd> Enable interlaced mode, bottom field first (default: disabled)</p>
<dt><code>nal_hrd=&lt;none|vbr|cbr&gt;</code></p>
<dd> Signal HRD information (requires vbv_bufsize) (default: none).</p>
<dt><code>(no)pic_struct</code></p>
<dd> Force pic_struct in Picture Timing SEI (default: disabled).</p>
<dt><code>(no)constrained_intra</code></p>
<dd> Enable constrained intra prediction (default: disabled). This significantly reduces compression, but is required for the base layer of SVC encodes.</p>
<dt><code>output_csp=&lt;i420|i422|i444|rgb&gt;</code></p>
<dd> Specify output colorspace (default: i420).</p>
<dt><code>(no)aud</code></p>
<dd> Write access unit delimeters to the stream (default: disabled). Enable this only if your target container format requires access unit delimiters.</p>
<dt><code>overscan=&lt;undef|show|crop&gt;</code></p>
<dd> Include VUI overscan information in the stream (default: disabled). See doc/vui.txt in the x264 source code for more information.</p>
<dt><code>videoformat=&lt;component|pal|ntsc|secam|mac|undef&gt;</code></p>
<dd> Include VUI video format information in the stream (default: disabled). This is a purely informative setting for describing the original source. See doc/vui.txt in the x264 source code for more information.</p>
<dt><code>(no)fullrange</code></p>
<dd> Include VUI full range information in the stream (default: disabled). Use this option if your source video is not range limited. See doc/vui.txt in the x264 source code for more information.</p>
<dt><code>colorprim=&lt;bt709|bt470m|bt470bg|smpte170m|smpte240m|film|undef&gt;</code></p>
<dd> Include color primaries information (default: disabled). This can be used for color correction. See doc/vui.txt in the x264 source code for more information.</p>
<dt><code>transfer=&lt;bt709|bt470m|bt470bg|linear|log100|log316|smpte170m|smpte240m&gt;</code></p>
<dd> Include VUI transfer characteristics information in the stream (default: disabled). This can be used for color correction. See doc/vui.txt in the x264 source code for more information.</p>
<dt><code>colormatrix=&lt;bt709|fcc|bt470bg|smpte170m|smpte240m|GBR|YCgCo&gt;</code></p>
<dd> Include VUI matrix coefficients in the stream (default: disabled). This can be used for color correction. See doc/vui.txt in the x264 source code for more information.</p>
<dt><code>chromaloc=&lt;0-5&gt;</code></p>
<dd> Include VUI chroma sample location information in the stream (default: disabled). Use this option to ensure alignment of the chroma and luma planes after color space conversions. See doc/vui.txt in the x264 source code for more information.</p>
<dt><code>log=&lt;-1-3&gt;</code></p>
<dd> Adjust the amount of logging info printed to the screen.</p>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> none</p>
<dt> 0</p>
<dd> Print errors only.</p>
<dt> 1</p>
<dd> warnings</p>
<dt> 2</p>
<dd> PSNR and other analysis statistics when the encode finishes (default)</p>
<dt> 3</p>
<dd> PSNR, QP, frametype, size, and other statistics for every frame</dl>
</dl>
<dt><code>(no)psnr</code></p>
<dd> Print signal-to-noise ratio statistics.<br />
 <i>NOTE:</i> The &#8216;Y&#8217;, &#8216;U&#8217;, &#8216;V&#8217;, and &#8216;Avg&#8217; PSNR fields in the summary are not mathematically sound (they are simply the average of per-frame PSNRs). They are kept only for comparison to the JM reference codec. For all other purposes, please use either the &#8216;Global&#8217; PSNR, or the per-frame PSNRs printed by log=3.</p>
<dt><code>(no)ssim</code></p>
<dd> Print the Structural Similarity Metric results. This is an alternative to PSNR, and may be better correlated with the perceived quality of the compressed video.</p>
<dt><code>(no)visualize</code></p>
<dd> Enable x264 visualizations during encoding. If the x264 on your system supports it, a new window will be opened during the encoding process, in which x264 will attempt to present an overview of how each frame gets encoded. Each block type on the visualized movie will be colored as follows:</p>
<dt><code>dump_yuv=&lt;file name&gt;</code></p>
<dd> Dump YUV frames to the specified file. For debugging use.</p>
<dl>
<dt>
<dd>
<dl>
<dt>red/pink</p>
<dd> intra block</p>
<dt>blue&nbsp;</p>
<dd> inter block</p>
<dt>green</p>
<dd> skip block</p>
<dt>yellow</p>
<dd> B-block</dl>
</dl>
<dl>
<dt>
<dd> This feature can be considered experimental and subject to change. In particular, it depends on x264 being compiled with visualizations enabled. Note that as of writing this, x264 pauses after encoding and visualizing each frame, waiting for the user to press a key, at which point the next frame will be encoded.</dl>
</dl>
<h3>xvfw (-xvfwopts)</h3>
<p> Encoding with Video for Windows codecs is mostly obsolete unless you wish to encode to some obscure fringe codec.</p>
<dl>
<dt><code>codec=&lt;name&gt;</code></p>
<dd> The name of the binary codec file with which to encode.</p>
<dt><code>compdata=&lt;file&gt;</code></p>
<dd> The name of the codec settings file (like firstpass.mcf) created by vfw2menc.</dl>
<h3>MPEG muxer (-mpegopts)</h3>
<p> The MPEG muxer can generate 5 types of streams, each of which has reasonable default parameters that the user can override. Generally, when generating MPEG files, it is advisable to disable MEncoder&#8217;s frame-skip code (see -noskip, -mc as well as the harddup and softskip video filters). </p>
<p> <i>EXAMPLE:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt>format=mpeg2:tsaf:vbitrate=8000</p>
<dd></dl>
</dl>
<dl>
<dt><code>format=&lt;mpeg1 | mpeg2 | xvcd | xsvcd | dvd | pes1 | pes2&gt;</code></p>
<dd> stream format (default: mpeg2). pes1 and pes2 are very broken formats (no pack header and no padding), but VDR uses them; do not choose them unless you know exactly what you are doing.</p>
<dt><code>size=&lt;up to 65535&gt;</code></p>
<dd> Pack size in bytes, do not change unless you know exactly what you are doing (default: 2048).</p>
<dt><code>muxrate=&lt;int&gt;</code></p>
<dd> Nominal muxrate in kbit/s used in the pack headers (default: 1800 kb/s). Will be updated as necessary in the case of &#8216;format=mpeg1&#8217; or &#8216;mpeg2&#8217;.</p>
<dt><code>tsaf&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> Sets timestamps on all frames, if possible; recommended when format=dvd. If dvdauthor complains with a message like &quot;..audio sector out of range&#8230;&quot;, you probably did not enable this option.</p>
<dt><code>interleaving2</code></p>
<dd> Uses a better algorithm to interleave audio and video packets, based on the principle that the muxer will always try to fill the stream with the largest percentage of free space.</p>
<dt><code>vdelay=&lt;1-32760&gt;</code></p>
<dd> Initial video delay time, in milliseconds (default: 0), use it if you want to delay video with respect to audio. It doesn&#8217;t work with :drop.</p>
<dt><code>adelay=&lt;1-32760&gt;</code></p>
<dd> Initial audio delay time, in milliseconds (default: 0), use it if you want to delay audio with respect to video.</p>
<dt><code>drop&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code></p>
<dd> When used with vdelay the muxer drops the part of audio that was anticipated.</p>
<dt><code>vwidth, vheight=&lt;1-4095&gt;</code></p>
<dd> Set the video width and height when video is MPEG-1/2.</p>
<dt><code>vpswidth, vpsheight=&lt;1-4095&gt;</code></p>
<dd> Set pan and scan video width and height when video is MPEG-2.</p>
<dt><code>vaspect=&lt;1 | 4/3 | 16/9 | 221/100&gt;</code></p>
<dd> Sets the display aspect ratio for MPEG-2 video. Do not use it on MPEG-1 or the resulting aspect ratio will be completely wrong.</p>
<dt><code>vbitrate=&lt;int&gt;</code></p>
<dd> Sets the video bitrate in kbit/s for MPEG-1/2 video.</p>
<dt><code>vframerate=&lt;24000/1001 | 24 | 25 | 30000/1001 | 30 | 50 | 60000/1001 | 60 &gt;</code></p>
<dd> Sets the framerate for MPEG-1/2 video. This option will be ignored if used with the telecine option.</p>
<dt><code>telecine</code></p>
<dd> Enables 3:2 pulldown soft telecine mode: The muxer will make the video stream look like it was encoded at 30000/1001 fps. It only works with MPEG-2 video when the output framerate is 24000/1001 fps, convert it with -ofps if necessary. Any other framerate is incompatible with this option.</p>
<dt><code>film2pal</code></p>
<dd> Enables FILM to PAL and NTSC to PAL soft telecine mode: The muxer will make the video stream look like it was encoded at 25 fps. It only works with MPEG-2 video when the output framerate is 24000/1001 fps, convert it with -ofps if necessary. Any other framerate is incompatible with this option.</p>
<dt><code>tele_src and tele_dest</code></p>
<dd> Enables arbitrary telecining using Donand Graft&#8217;s DGPulldown code. You need to specify the original and the desired framerate; the muxer will make the video stream look like it was encoded at the desired framerate. It only works with MPEG-2 video when the input framerate is smaller than the output framerate and the framerate increase is &lt;= 1.5. </p>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>tele_src=25,tele_dest=30000/1001</p>
<dd> PAL to NTSC telecining</dl>
</dl>
<dt><code>vbuf_size=&lt;40-1194&gt;</code></p>
<dd> Sets the size of the video decoder&#8217;s buffer, expressed in kilobytes. Specify it only if the bitrate of the video stream is too high for the chosen format and if you know perfectly well what you are doing. A too high value may lead to an unplayable movie, depending on the player&#8217;s capabilities. When muxing HDTV video a value of 400 should suffice.</p>
<dt><code>abuf_size=&lt;4-64&gt;</code></p>
<dd> Sets the size of the audio decoder&#8217;s buffer, expressed in kilobytes. The same principle as for vbuf_size applies.</dl>
<h3>FFmpeg libavformat demuxers (-lavfdopts)</h3>
<dl>
<dt><code>analyzeduration=&lt;value&gt;</code></p>
<dd> Maximum length in seconds to analyze the stream properties.</p>
<dt><code>format=&lt;value&gt;</code></p>
<dd> Force a specific libavformat demuxer.</p>
<dt><code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></p>
<dd> Pass AVOptions to libavformat demuxer. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some options may conflict with MPlayer/MEncoder options. </p>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>o=ignidx</p>
<dd></dl>
</dl>
<dt><code>probesize=&lt;value&gt;</code></p>
<dd> Maximum amount of data to probe during the detection phase. In the case of MPEG-TS this value identifies the maximum number of TS packets to scan.</p>
<dt><code>cryptokey=&lt;hexstring&gt;</code></p>
<dd> Encryption key the demuxer should use. This is the raw binary data of the key converted to a hexadecimal string.</dl>
<h3>FFmpeg libavformat muxers (-lavfopts) (also see -of lavf)</h3>
<dl>
<dt><code>delay=&lt;value&gt;</code></p>
<dd> Currently only meaningful for MPEG[12]: Maximum allowed distance, in seconds, between the reference timer of the output stream (SCR) and the decoding timestamp (DTS) for any stream present (demux to decode delay). Default is 0.7 (as mandated by the standards defined by MPEG). Higher values require larger buffers and must not be used.</p>
<dt><code>format=&lt;container_format&gt;</code></p>
<dd> Override which container format to mux into (default: autodetect from output file extension).</p>
<dl>
<dt>
<dd>
<dl>
<dt>mpg&nbsp;<wbr>&nbsp;</p>
<dd> MPEG-1 systems and MPEG-2 PS</p>
<dt>asf&nbsp;<wbr>&nbsp;</p>
<dd> Advanced Streaming Format</p>
<dt>avi&nbsp;<wbr>&nbsp;</p>
<dd> Audio Video Interleave file</p>
<dt>wav&nbsp;<wbr>&nbsp;</p>
<dd> Waveform Audio</p>
<dt>swf&nbsp;<wbr>&nbsp;</p>
<dd> Macromedia Flash</p>
<dt>flv&nbsp;<wbr>&nbsp;</p>
<dd> Macromedia Flash video files</p>
<dt>rm&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> RealAudio and RealVideo</p>
<dt>au&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> SUN AU format</p>
<dt>nut&nbsp;<wbr>&nbsp;</p>
<dd> NUT open container format (experimental)</p>
<dt>mov&nbsp;<wbr>&nbsp;</p>
<dd> QuickTime</p>
<dt>mp4&nbsp;<wbr>&nbsp;</p>
<dd> MPEG-4 format</p>
<dt>ipod&nbsp;</p>
<dd> MPEG-4 format with extra header flags required by Apple iPod firmware</p>
<dt>dv&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Sony Digital Video container</p>
<dt>matroska&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dd> Matroska</dl>
</dl>
<dt><code>muxrate=&lt;rate&gt;</code></p>
<dd> Nominal bitrate of the multiplex, in bits per second; currently it is meaningful only for MPEG[12]. Sometimes raising it is necessary in order to avoid &quot;buffer underflows&quot;.</p>
<dt><code>o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></p>
<dd> Pass AVOptions to libavformat muxer. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some options may conflict with MEncoder options. </p>
<dl>
<dt>
<dd> <i>EXAMPLE:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>o=packetsize=100</p>
<dd></dl>
</dl>
<dt><code>packetsize=&lt;size&gt;</code></p>
<dd> Size, expressed in bytes, of the unitary packet for the chosen format. When muxing to MPEG[12] implementations the default values are: 2324 for [S]VCD, 2048 for all others formats.</p>
<dt><code>preload=&lt;distance&gt;</code></p>
<dd> Currently only meaningful for MPEG[12]: Initial distance, in seconds, between the reference timer of the output stream (SCR) and the decoding timestamp (DTS) for any stream present (demux to decode delay).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> There are a number of environment variables that can be used to control the behavior of MPlayer and MEncoder.</p>
<dl>
<dt><code>MPLAYER_CHARSET (also see -msgcharset)</code></p>
<dd> Convert console messages to the specified charset (default: autodetect). A value of &quot;noconv&quot; means no conversion.</p>
<dt><code>MPLAYER_HOME</code></p>
<dd> Directory where MPlayer looks for user settings.</p>
<dt><code>MPLAYER_VERBOSE (also see -v and -msglevel)</code></p>
<dd> Set the initial verbosity level across all message modules (default: 0). The resulting verbosity corresponds to that of -msglevel 5 plus the value of MPLAYER_VERBOSE.</dl>
<h3>libaf:</h3>
<dl>
<dt><code>LADSPA_PATH</code></p>
<dd> If LADSPA_PATH is set, it searches for the specified file. If it is not set, you must supply a fully specified pathname. FIXME: This is also mentioned in the ladspa section.</dl>
<h3>libdvdcss:</h3>
<dl>
<dt><code>DVDCSS_CACHE</code></p>
<dd> Specify a directory in which to store title key values. This will speed up descrambling of DVDs which are in the cache. The DVDCSS_CACHE directory is created if it does not exist, and a subdirectory is created named after the DVD&#8217;s title or manufacturing date. If DVDCSS_CACHE is not set or is empty, libdvdcss will use the default value which is &quot;${HOME}/.dvdcss/&quot; under Unix and &quot;C:\Documents and Settings\$USER\Application Data\dvdcss\&quot; under Win32. The special value &quot;off&quot; disables caching.</p>
<dt><code>DVDCSS_METHOD</code></p>
<dd> Sets the authentication and decryption method that libdvdcss will use to read scrambled discs. Can be one of title, key or disc.</p>
<dl>
<dt>
<dd>
<dl>
<dt>key&nbsp;<wbr>&nbsp;</p>
<dd> is the default method. libdvdcss will use a set of calculated player keys to try and get the disc key. This can fail if the drive does not recognize any of the player keys.</p>
<dt>disc&nbsp;</p>
<dd> is a fallback method when key has failed. Instead of using player keys, libdvdcss will crack the disc key using a brute force algorithm. This process is CPU intensive and requires 64 MB of memory to store temporary data.</p>
<dt>title</p>
<dd> is the fallback when all other methods have failed. It does not rely on a key exchange with the DVD drive, but rather uses a crypto attack to guess the title key. On rare cases this may fail because there is not enough encrypted data on the disc to perform a statistical attack, but in the other hand it is the only way to decrypt a DVD stored on a hard disc, or a DVD with the wrong region on an RPC2 drive.</dl>
</dl>
<dt><code>DVDCSS_RAW_DEVICE</code></p>
<dd> Specify the raw device to use. Exact usage will depend on your operating system, the Linux utility to set up raw devices is <a href="/docs/linux/man/8-raw/">raw</a>(8) for instance. Please note that on most operating systems, using a raw device requires highly aligned buffers: Linux requires a 2048 bytes alignment (which is the size of a DVD sector).</p>
<dt><code>DVDCSS_VERBOSE</code></p>
<dd> Sets the libdvdcss verbosity level.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Outputs no messages at all.</p>
<dt>1</p>
<dd> Outputs error messages to stderr.</p>
<dt>2</p>
<dd> Outputs error messages and debug messages to stderr.</dl>
</dl>
<dt><code>DVDREAD_NOKEYS</code></p>
<dd> Skip retrieving all keys on startup. Currently disabled.</p>
<dt><code>HOME</code></p>
<dd> FIXME: Document this.</dl>
<h3>libao2:</h3>
<dl>
<dt><code>AO_SUN_DISABLE_SAMPLE_TIMING</code></p>
<dd> FIXME: Document this.</p>
<dt><code>AUDIODEV</code></p>
<dd> FIXME: Document this.</p>
<dt><code>AUDIOSERVER</code></p>
<dd> Specifies the Network Audio System server to which the nas audio output driver should connect and the transport that should be used. If unset DISPLAY is used instead. The transport can be one of tcp and unix. Syntax is tcp/&lt;somehost&gt;:&lt;someport&gt;, &lt;somehost&gt;:&lt;instancenumber&gt; or [unix]:&lt;instancenumber&gt;. The NAS base port is 8000 and &lt;instancenumber&gt; is added to that. </p>
<dl>
<dt>
<dd> <i>EXAMPLES:</i></dl>
<dl>
<dt>
<dd>
<dl>
<dt>AUDIOSERVER=somehost:0</p>
<dd> Connect to NAS server on somehost using default port and transport.</p>
<dt>AUDIOSERVER=tcp/somehost:8000</p>
<dd> Connect to NAS server on somehost listening on TCP port 8000.</p>
<dt>AUDIOSERVER=(unix)?:0</p>
<dd> Connect to NAS server instance 0 on localhost using unix domain sockets.</dl>
</dl>
<dt><code>DISPLAY</code></p>
<dd> FIXME: Document this.</dl>
<h3>vidix:</h3>
<dl>
<dt><code>VIDIX_CRT</code></p>
<dd> FIXME: Document this.</p>
<dt><code>VIDIXIVTVALPHA</code></p>
<dd> Set this to &#8216;disable&#8217; in order to stop the VIDIX driver from controlling alphablending settings. You can then manipulate it yourself with &#8216;ivtvfbctl&#8217;.</dl>
<h3>osdep:</h3>
<dl>
<dt><code>TERM</code></p>
<dd> FIXME: Document this.</dl>
<h3>libvo:</h3>
<dl>
<dt><code>DISPLAY</code></p>
<dd> FIXME: Document this.</p>
<dt><code>FRAMEBUFFER</code></p>
<dd> FIXME: Document this.</p>
<dt><code>HOME</code></p>
<dd> FIXME: Document this.</dl>
<h3>libmpdemux:</h3>
<dl>
<dt><code>HOME</code></p>
<dd> FIXME: Document this.</p>
<dt><code>HOMEPATH</code></p>
<dd> FIXME: Document this.</p>
<dt><code>http_proxy</code></p>
<dd> FIXME: Document this.</p>
<dt><code>LOGNAME</code></p>
<dd> FIXME: Document this.</p>
<dt><code>USERPROFILE</code></p>
<dd> FIXME: Document this.</dl>
<h3>GUI:</h3>
<dl>
<dt><code>DISPLAY</code></p>
<dd> The name of the display to which the GUI should connect.</p>
<dt><code>HOME</code></p>
<dd> The home directory of the current user.</dl>
<h3>libavformat:</h3>
<dl>
<dt><code>AUDIO_FLIP_LEFT</code></p>
<dd> FIXME: Document this.</p>
<dt><code>BKTR_DEV</code></p>
<dd> FIXME: Document this.</p>
<dt><code>BKTR_FORMAT</code></p>
<dd> FIXME: Document this.</p>
<dt><code>BKTR_FREQUENCY</code></p>
<dd> FIXME: Document this.</p>
<dt><code>http_proxy</code></p>
<dd> FIXME: Document this.</p>
<dt><code>no_proxy</code></p>
<dd> FIXME: Document this.</dl>
<h2>FILES</h2>
<dl>
<dt>/usr/:local/:etc/:mplayer/:mplayer.conf</p>
<dd> MPlayer system-wide settings</p>
<dt>/usr/:local/:etc/:mplayer/:mencoder.conf</p>
<dd> MEncoder system-wide settings</p>
<dt>~/.mplayer/:config</p>
<dd> MPlayer user settings</p>
<dt>~/.mplayer/:mencoder.conf</p>
<dd> MEncoder user settings</p>
<dt>~/.mplayer/:input.conf</p>
<dd> input bindings (see &#8216;-input keylist&#8217; for the full list)</p>
<dt>~/.mplayer/:gui.conf</p>
<dd> GUI configuration file</p>
<dt>~/.mplayer/:gui.history</p>
<dd> GUI directory history</p>
<dt>~/.mplayer/:gui.pl</p>
<dd> GUI playlist</p>
<dt>~/.mplayer/:gui.url</p>
<dd> GUI URL list</p>
<dt>~/.mplayer/:font/</p>
<dd> font directory (There must be a font.desc file and files with .RAW extension.)</p>
<dt>~/.mplayer/:DVDkeys/</p>
<dd> cached CSS keys</dl>
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
mplayer <a href="dvd://1">dvd://1</a> -dvd-device /dev/:dvd2
</pre>
<p> <code>Play DVD video from a directory with VOB files:</code> </p>
<pre>
mplayer <a href="dvd://1">dvd://1</a> -dvd-device /path/:to/:directory/
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
mplayer /dev/:zero -rawvideo pal:fps=xx -demuxer rawvideo -vc null -vo null -noframedrop -benchmark -sub source.sub -dumpmpsub
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
<p> Don&#8217;t panic. If you find one, report it to us, but please make sure you have read all of the documentation first. Also look out for smileys. :) Many bugs are the result of incorrect setup or parameter usage. The bug reporting section of the documentation (<a rel="nofollow" href="http://www.mplayerhq.hu/:DOCS/:HTML/:en/:bugreports.html)">http://www.mplayerhq.hu/:DOCS/:HTML/:en/:bugreports.html)</a> explains how to create useful bug reports.</p>
<h2>AUTHORS</h2>
<p> MPlayer was initially written by Arpad Gereoffy. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> MPlayer is (C) 2000-2016 The MPlayer Team </p>
<p> This man page was written mainly by Gabucino, Jonas Jermann and Diego Biurrun. It is maintained by Diego Biurrun. Please send mails about it to the MPlayer-DOCS mailing list. Translation specific mails belong on the MPlayer-translations mailing list. </p>
<h2>Index</h2>
