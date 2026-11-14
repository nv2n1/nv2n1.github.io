---
title: "fvwmevent(1)"
name: "fvwmevent"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmevent/"
description: "FvwmEvent – the fvwm event module"
---

<p><i>FvwmEvent</i> &#8211; the fvwm event module </p>
<h2>Synopsis</h2>
<p><i>FvwmEvent</i> is a more versatile replacement for <i>FvwmAudio</i>. It can in general be used to hook any <i>fvwm</i> function or program to any window manager event. E.g: Delete unwanted Netscape Pop ups or application error pop ups as they appear, play sounds, log events to a file and the like. Be creative, you&#8217;ll find a use for it. </p>
<p> <i>FvwmEvent</i> is spawned by <i>fvwm</i>, so no command line invocation will work. From within the <i>.fvwm2rc</i> file, <i>FvwmEvent</i> is spawned as follows: </p>
<pre>Module FvwmEvent</pre>
<p>or from within an <i>fvwm</i> pop-up menu: </p>
<pre>DestroyMenu Module-Popup
AddToMenu Module-Popup &quot;Modules&quot; Title
+ &quot;Event&quot; Module FvwmEvent
+ &quot;Auto&quot; Module FvwmAuto 200
+ &quot;Buttons&quot; Module FvwmButtons
+ &quot;Console&quot; Module FvwmConsole
+ &quot;Ident&quot; Module FvwmIdent
+ &quot;Banner&quot; Module FvwmBanner
+ &quot;Pager&quot; Module FvwmPager 0 3</pre>
<h2>Description</h2>
<p>The <i>FvwmEvent</i> module communicates with the <i>fvwm</i> window manager to bind <i>actions</i> to window manager <i>events</i>. Different actions may be assigned to distinct window manager events. </p>
<p> <i>FvwmEvent</i> can be used to bind sound files to events like <i>FvwmAudio</i> (RiP) did. It can be used for logging event traces to a log file, while debugging <i>fvwm</i>. </p>
<p> <i>FvwmEvent</i> can also have builtin support for the rplay library. (heritage of FvwmAudio) </p>
<h2>Invocation</h2>
<p>The invocation method was shown in the synopsis section. No command line invocation is possible. <i>FvwmEvent</i> must be invoked by the <i>fvwm</i> window manager. <i>FvwmEvent</i> accepts a single argument: </p>
<dl>
<dt>-audio</p>
<dd>Enables FvwmAudio compatibility mode. </p>
<dt>alias</p>
<dd>Makes FvwmEvent use <i>alias</i> as its name. This affects which lines from the user&#8217;s configuration file are used. </p>
<p> Invoking FvwmEvent as <i>FvwmAudio</i> (either by using an alias or creating a symlink) enables FvwmAudio compatibility mode. </p>
</dl>
<h2>Configuration Options</h2>
<p><i>FvwmEvent</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>), and looks for certain configuration options: </p>
<dl>
<dt>*FvwmEvent: Cmd <i>command</i></p>
<dd>This determines the <i>fvwm</i> function that is to be called with the event parameters. You might want to do one of the following (details below): </p>
<pre> # play sounds
 *FvwmEvent: Cmd <i>builtin-rplay</i>
 # execute distinct fvwm functions
 *FvwmEvent: Cmd
 # execute distinct external programs
 *FvwmEvent: Cmd exec</pre>
<p>This version of <i>FvwmEvent</i> has builtin <i>rplay</i> support which does not need to invoke an external audio player to play sounds. The rplay support is enabled when <i>FvwmEvent</i> is compiled with <i>HAVE_RPLAY</i> defined and when <i>FvwmEvent: Cmd</i> is set to <i>builtin-rplay</i>. See remarks below if <i>FvwmEvent</i> is invoked in FvwmAudio compatibility mode. </p>
<p> For example: </p>
<pre> *FvwmEvent: Cmd <i>builtin-rplay</i>
 *FvwmEvent: add_window drip.au</pre>
<p>rplay can be obtained via anonymous ftp at </p>
<pre> &lt;URL:<a href="ftp://ftp.sdsu.edu/pub/rplay">ftp://ftp.sdsu.edu/pub/rplay</a>&gt; or
 &lt;URL:<a href="ftp://ftp.x.org/contrib/Event/audio/rplay">ftp://ftp.x.org/contrib/Event/audio/rplay</a>&gt;</pre>
<p><i>FvwmEvent</i> also has support for any other external program. e.g: the rsynth &#8216;say&#8217; command: </p>
<pre> *FvwmEvent: Cmd &quot;Exec /rsynth/say&quot;
 *FvwmEvent: destroy_window &quot;window closed&quot;</pre>
<p>You can also use <i>fvwm</i>&#8216;s builtin <i>Echo</i> command as <i>FvwmEvent: Cmd</i> to obtain debug output for <i>fvwm</i> events quietly. I used this setup to debug FvwmAuto: </p>
<pre> *FvwmEvent: Cmd <i>Echo</i>
 *FvwmEvent: focus_change &quot;focus change&quot;
 *FvwmEvent: raise_window &quot;raise window&quot;</pre>
<p>You can even call different shell commands for each event just by setting </p>
<pre> *FvwmEvent: Cmd exec
 *FvwmEvent: add_window 'killname &quot;APPL ERROR&quot;'</pre>
<dt>*FvwmEvent: PassId</p>
<dd>Specifies that the event action will have an ID parameter added to the end of the command line. Most events will have the windowID of the window that the event refers to, new_desk will have the new desk number. The windowID is a hexadecimal string preceded by 0x, desk numbers are decimal. </p>
<dt>*FvwmEvent: <i>window-manager-event action-or-filename</i></p>
<dd>Binds particular actions to window manager events. </p>
<p> e.g. for audio-events: </p>
<pre> *FvwmEvent: startup TaDa.au
 *FvwmEvent: shutdown Elvis_Left.au
 *FvwmEvent: unknown doh.au
 *FvwmEvent: new_page beam_trek.au
 *FvwmEvent: new_desk beam_trek.au
 *FvwmEvent: old_add_window drip.au
 *FvwmEvent: raise_window swoosh.au
 *FvwmEvent: lower_window swoosh.au
 *FvwmEvent: old_configure_window hammer.au
 *FvwmEvent: focus_change boing.au
 *FvwmEvent: enter_window boing.au
 *FvwmEvent: leave_window boing.au
 *FvwmEvent: destroy_window explosion.au
 *FvwmEvent: iconify ploop.au
 *FvwmEvent: deiconify ploop.au
 *FvwmEvent: window_name huh.au
 *FvwmEvent: icon_name beep.au
 *FvwmEvent: visible_icon_name beep.au
 *FvwmEvent: res_class beep.au
 *FvwmEvent: res_name beep.au
 *FvwmEvent: end_windowlist twang.au
 *FvwmEvent: icon_location beep.au
 *FvwmEvent: map beep.au
 *FvwmEvent: error beep.au
 *FvwmEvent: config_info beep.au
 *FvwmEvent: end_config_info beep.au
 *FvwmEvent: icon_file beep.au
 *FvwmEvent: default_icon beep.au
 *FvwmEvent: string plapper.au
 *FvwmEvent: mini_icon beep.au
 *FvwmEvent: windowshade beep.au
 *FvwmEvent: dewindowshade beep.au
 *FvwmEvent: visible_name beep.au
 *FvwmEvent: sendconfig beep.au
 *FvwmEvent: restack beep.au
 *FvwmEvent: add_window beep.au
 *FvwmEvent: configure_window beep.au
 *FvwmEvent: visible_icon_name beep.au
 *FvwmEvent: enter_window beep.au
 *FvwmEvent: leave_window beep.au
 *FvwmEvent: property_change beep.au</pre>
<p>The window related event handlers are executed within a window context. Previously PassId was used for this purpose, but now using PassId is not needed. </p>
<p> Note: The enter_window event is generated when the pointer enters a window. With the -passid option, that window&#8217;s id is passed to fvwm. An enter_window event is generated too when the pointer leaves a window and moves into the root window. In this case, the id passed is 0. </p>
<p> Note: When the shutdown event arrives, FvwmEvent may be killed before it can trigger the associated action. </p>
<p> Provided <i>fvwm</i> supports it (not yet), there&#8217;s an additional event to replace all <i>fvwm</i> beeps with a sound: </p>
<pre> *FvwmEvent: beep beep.au</pre>
<dt>*FvwmEvent: Delay <i>5</i></p>
<dd>Specifies that an event-action will only be executed if it occurs at least 5 seconds after the previous event. Events that occur during the delay period are ignored. This option is useful if you don&#8217;t want several sounds playing at the same time. The default delay is 0 which disables the Event delay. </p>
<dt>*FvwmEvent: StartDelay <i>delay</i></p>
<dd>Specifies that an event-action will only be executed if it occurs at least <i>delay</i> seconds after the startup event. Events that occur during the delay period are ignored. This option is useful when <i>fvwm</i> starts and restarts using an audio player. The default delay is 0. </p>
</dl>
<h2>Rplay Options</h2>
<p>The following options are only valid with builtin rplay support. i.e: when <i>FvwmEvent</i> was compiled with <i>HAVE_RPLAY</i> defined. They are used only if <i>FvwmEvent: Cmd</i> is set to <i>builtin-rplay</i>. </p>
<dl>
<dt>*FvwmEvent: RplayHost <i>hostname</i></p>
<dd>Specifies what host the rplay sounds will play on. The <i>hostname</i> can also be an environment variable such as $HOSTDISPLAY. </p>
<dt>*FvwmEvent: RplayPriority <i>0</i></p>
<dd>Specifies what priority will be assigned to the rplay sounds when they are played. </p>
<dt>*FvwmEvent: RplayVolume <i>127</i></p>
<dd>Specifies what volume will be assigned to the sounds when they are played. </p>
</dl>
<h2>FvwmAudio Compatibility Mode</h2>
<p>When invoked in FvwmAudio compatibility mode (see above), FvwmEvent accepts the following options to provide backwards compatibility for FvwmAudio: </p>
<dl>
<dt>*FvwmEvent: PlayCmd <i>command</i></p>
<dd>This is equivalent to using *FvwmEvent: Cmd to Exec commands. This determines the independent audio player program that will actually play the sounds. If the play command is set to <i>builtin-rplay</i> then the builtin rplay support will be used. </p>
<dt>*FvwmAudio: Dir <i>directory</i></p>
<dd>Specifies the directory to look for the audio files. This option is ignored when rplay is used. </p>
</dl>
<h2>Bugs</h2>
<p>It&#8217;s REALLY noisy when <i>fvwm</i> starts and restarts using an audio player. You can use FvwmEvent: StartDelay to fix this problem. </p>
<h2>Copyrights</h2>
<p>This module has evolved of <i>FvwmAudio</i>, which in term is heavily based on a similar Fvwm module called <i>FvwmSound</i> by Mark Boyns. <i>FvwmAudio</i> simply took Mark&#8217;s original program and extended it to make it generic enough to work with any audio player. Due to different requests to do specific things on specific events, <i>FvwmEvent</i> took this one step further and now calls any <i>fvwm</i> function, or builtin-rplay. If <i>fvwm</i>&#8216;s Exec function is used, any external program can be called with any parameter. </p>
<p> The concept for interfacing this module to the Window Manager, is original work by Robert Nation. </p>
<p> Copyright 1998 Albrecht Kadlec. Copyright 1994, Mark Boyns and Mark Scott. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use and modify this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>Authors</h2>
<pre>1994 FvwmSound Mark Boyns (<i>boyns [at] sdsu.edu</i>)
1994 FvwmAudio Mark Scott (<i>mscott [at] mcd.mot.com</i>)
1996 FvwmAudio Albrecht Kadlec
1998 FvwmEvent Albrecht Kadlec (<i>albrecht [at] auto.tuwien.ac.at</i>)</pre>
