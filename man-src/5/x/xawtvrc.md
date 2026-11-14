---
title: "xawtvrc(5)"
name: "xawtvrc"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xawtvrc/"
description: "xawtvrc — TV apps config file"
---

<p>xawtvrc &#8212; TV apps config file</p>
<h2>Synopsis</h2>
<p>/etc/X11/xawtvrc<br />
 $HOME/.xawtv</p>
<h2>Description</h2>
<p><code>xawtvrc</code> is the config file originally used by xawtv only (that&#8217;s why the name xawtvrc). These days a number of other TV applications / utilities read it too to get configuration information from it. </p>
<p> Both a global (/etc/X11/xawtvrc) and personal ($HOME/.xawtv) config file are used by the applications. Settings in the personal config file will overwrite the global ones.</p>
<h3>Applications</h3>
<p>The following applications use these config files:</p>
<dl>
<dt><code>xawtv</code></p>
<dd>The classic X11 TV application.</p>
<dt><code>motv</code></p>
<dd>A better, motif-based GUI for xawtv &#8230;</p>
<dt><code>fbtv</code></p>
<dd>TV application for the linux framebuffer console.</p>
<dt><code>ttv</code></p>
<dd>aalib-based TV application for any terminal.</p>
<dt><code>v4lctl</code></p>
<dd>command line tool to control video4linux devices.</dl>
<h3>Create a config file</h3>
<p><code>xawtv</code> and <code>motv</code> both provide some functions to edit the channels and save the configuration. The save function will <code>not</code> preserve any comments you might have put into the config file throught &#8230; </p>
<p> You can also use your favorite text editor and modify the config file directly. </p>
<p> You can use the command line utility <code>scantv</code> to create a initial config file. scantv will automatically scan all channels for TV stations and write the ones it has found to the config file.</p>
<h2>Syntax</h2>
<p><code>xawtvrc</code> uses the same syntax like smb.conf: sections starting with [name], followed by lines with option = value pairs. </p>
<p> There are four special sections: [global], [launch], [eventmap] and [defaults]. All other sections describe a TV station each.</p>
<h3>TV station options.</h3>
<p>The following options are allowed for TV stations and the [defaults] section. The options from the [defaults] sections are used &#8212; as the name suggests &#8212; as defaults for all other channels. You can put everything which is common for all TV stations (like the TV norm which is used in your country) into the [defaults] section, so you don&#8217;t have to specify it for every single channel. </p>
<p> With a reasonable [defaults] section you usually only need to specify the channel for each TV station, like this: </p>
<pre>[ORB]
channel = 27</pre>
<p>The other options are:</p>
<dl>
<dt><code>fine = n</code></p>
<dd>finetuning (what left+right keys do within xawtv), default: 0</p>
<dt><code>norm = pal | ntsc | secam</code></p>
<dd>which TV norm, default is pal</p>
<dt><code>key = keysym</code></p>
<dd>Hotkey for the channel. All X11 keysyms allowed here. You can prefix a keysym with Modifier+, &quot;Ctrl+F&quot; for example.</p>
<dt><code>capture = off | overlay | grabdisplay</code></p>
<dd>capture mode: off, overlay (default, TV card =&gt; video, 0% cpu) or grabdisplay (TV card =&gt; main memory =&gt; X-Server =&gt; video, frame rate depends on load and picture size). Default is overlay. If it is not possible to use overlay for some reason (remote display, not supported by the hardware, whatever) the applications will automatically fallback to grabdisplay.</p>
<dt><code>input = Television | Composite1 | Composite2 | SVHS</code></p>
<dd>input source. The valid choices depend on the hardware driver, the values above are just examples. You can use &quot;v4lctl list&quot; to get a list of valid choices.</p>
<dt><code>color = n</code></p>
<dd>
<dt><code>bright = n</code></p>
<dd>
<dt><code>hue = n</code></p>
<dd>
<dt><code>contrast = n</code></p>
<dd>Valid range is 0-65535, default is 32768. Adding a percent symbol changes the range to 0-100, i.e. &quot;50%&quot; has the same effect like &quot;32768&quot;.</p>
<dt><code>audio = mono | stereo | lang1 | lang2</code></p>
<dd>Set the audio mode for the given channel.</p>
<dt><code>freq = n</code></p>
<dd>Specify the frequency for the given station (MHz, video carrier). You shouldn&#8217;t need this for normal operation, all your channels should be listed in the frequency table for your area (if not, mail me a patch). Maybe unless you live near the border and the foreign country uses another channel scheme.</p>
<dt><code>midi = note</code></p>
<dd>Use midi noteon event for &lt;note&gt; as hotkey for the channel.</p>
<dt><code>group = name</code></p>
<dd>Put the channel into the group &lt;name&gt;. motv uses that to create submenus per channel group.</dl>
<h3>Global options</h3>
<p>A number of not channel-related settings go to the &quot;[global]&quot; section:</p>
<dl>
<dt><code>fullscreen = width x height</code></p>
<dd>specify which video mode should be used for full-screen. Works with XFree only, and of course you need a valid modeline for this mode in your XF86Config file. You also have to enable the VidMode extension (option -vm, see above) to make this work.</p>
<dt><code>wm-off-by = [+-]x[+-]y</code></p>
<dd>Some WM&#8217;s handle static gravity incorrectly (I know mwm and kwm). This is somewhat boring with fullscreen mode. With this option you can correct this with a displacement for moving windows. For example, wm-off-by = -4-24 does the trick for kwm (the KDE1 window manager).</p>
<dt><code>freqtab = </code></p>
<dd>select a channel-to-freqency mapping. Options window-&gt;Frequency table (in xawtv) brings up a menu with all valid entries (and allows table-switching at runtime).</p>
<dt><code>pixsize = width x height</code></p>
<dd>size of the channel pixmaps (within Channels window). 0x0 disables this feature.</p>
<dt><code>pixcols = n</code></p>
<dd>number of columns the channel window should use. Defaults to 1.</p>
<dt><code>mixer = ctl | device:ctl</code></p>
<dd>This allows volume control using the sound card mixer. ctl is the mixer control, i.e. &quot;vol&quot; for the master volume. &quot;line1&quot; is a good candidate for the TV card. device is the mixer device (defaults to /dev/mixer in unspecified). Volume-control works with the keypad: + is up, &#8211; is down, Enter is mute.</p>
<dt><code>jpeg-quality = n</code></p>
<dd>set the quality for (M)JPEG images/frames. As usual the valid range for n is [0 .. 100] with 75 as default.</p>
<dt><code>keypad-ntsc = on | off</code></p>
<dd>Configure keypad mode. Default is off. When set to on, numbers typed on the keypad are interpreted as channel numbers (this is like NTSC TV sets work). Otherwise they are interpreted as programmed station, i.e. 1 is the first station from $HOME/.xawtv, &#8230;</p>
<dt><code>keypad-partial = on | off</code></p>
<dd>Another configuration of keypad mode. Default is on. When set to off, typing one digit on the keypad doesn&#8217;t change the station number when there are two-digit station numbers starting with that digit.</p>
<dt><code>osd = on | off</code></p>
<dd>Enable/disable the onscreen display in fullscreen mode. Default is on.</p>
<dt><code>osd-position = x , y</code></p>
<dd>Position the onscreen display, in pixels. Default is 30,20.</p>
<dt><code>use-wm-fullscreen = on | off</code></p>
<dd>Enter fullscreen mode by asking the window manager to handle that via _NET_WM_STATE_FULLSCREEN (if supported by the wm). Default is on.</p>
<dt><code>ratio = x:y</code></p>
<dd>Set a fixed aspect ratio for the TV image. Default is 4:3. Use 0:0 if you don&#8217;t want a fixed aspect ratio.</p>
<dt><code>mov-driver = files | raw | avi | mov</code></p>
<dd>
<dt><code>mov-video = ppm | pgm | jpeg | rgb | gray | 422 | 422p | rgb15 | rgb24 | mjpeg | jpeg | raw | mjpa | png</code></p>
<dd>
<dt><code>mov-fps = fps</code></p>
<dd>
<dt><code>mov-audio = mono8 | mono16 | stereo</code></p>
<dd>
<dt><code>mov-rate = rate</code></p>
<dd>Set defaults for movie recording. Not all possible combinations are valid choices. &quot;streamer -h&quot; will print a nice list.</p>
<dt><code>midi = port</code></p>
<dd>You can specify a ALSA port where xawtv should receive midi events from. If configured this way, you can program your midi keyboard keys as station hotkeys and use midi controller events to control settings like volume, bright etc. Check the [eventmap] description below for details.</p>
<dt><code>filter = name</code></p>
<dd>Enable the specified filter.</p>
<dt><code>alsa_latency = time_in_ms</code></p>
<dd>This can be used to specify the latency for the ALSA digital sound loopback which xawtv does. The default is 30ms if you&#8217;re getting sound dropouts on your system try increasing this setting.</dl>
<h3>The [launch] section</h3>
<p>You can start other programs from within xawtv. This is configured with entries in the &quot;[launch]&quot; section:</p>
<dl>
<dt><code>label = key, command line</code></p>
<dd>The specified hotkey will run the configured program. Calling the Action &quot;Launch(label)&quot; works too. If you want to play with the Xt translation tables, feel free to do so. But don&#8217;t complain if you broke something while doing so&#8230;</dl>
<h3>The [eventmap] section</h3>
<p>The eventmap simply has a number of &quot;event = action&quot; lines. &quot;action&quot; can be any command which xawtv understands (check the xawtv-remote man page for a list). &quot;event&quot; is some event generated by any input device xawtv listens to. An event might have some argument, the midi-ctrl events for example have one. If present the argument is appended to the action. </p>
<p> There are default mappings for lirc and joystick input events, so you don&#8217;t have to create an eventmap to use them. But if you don&#8217;t like the defaults you can change them easily. </p>
<p> Here is a list of valid events:</p>
<dl>
<dt><code>lirc-key-&lt;name&gt;</code></p>
<dd>The key &lt;name&gt; was pressed on the IR remote control.</p>
<dt><code>joy-button-&lt;n&gt;</code></p>
<dd>Joystick button &lt;n&gt; was pressed.</p>
<dt><code>joy-axis-&lt;left|right|up|down&gt;</code></p>
<dd>Joystick was moved into the given direction.</p>
<dt><code>midi-note-&lt;n&gt;</code></p>
<dd>noteon event for note &lt;n&gt; was received (i.e. you probably pressed some key on the midi keyboard).</p>
<dt><code>midi-ctrl-&lt;n&gt;</code></p>
<dd>midi controller message for control &lt;n&gt; was received. This event has an argument (the current value of the control).</p>
<dt><code>kbd-key-&lt;name&gt;</code></p>
<dd>Key &lt;name&gt; was pressed on the keyboard.</dl>
<h3>sample config file</h3>
<pre># this is a comment
# empty lines are ignored too
[global]
freqtab = europe-west
#mixer = line
jpeg-quality = 75
midi = 64:0
fullscreen = 768x576
# for /etc/XF86Config
# Modeline &quot;pal&quot; 50.00 768 832 856 1000 576 590 595 630 -hsync -vsync
[launch]
mixer = M, gtkaumix
AleVT = Ctrl+A, alevt
[eventmap]
midi-ctrl-7 = volume
kbd-key-h = msg &quot;hello world&quot;
[defaults]
input = television
norm = pal
[ZDF]
channel=33
key=F1
[ORB]
channel = 27
key = F2
# more stations follow here
[Camera]
input = Composite1
key = K</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-scantv/">scantv</a>(1), <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-motv/">motv</a>(1), <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1), <a href="/docs/linux/man/1-ttv/">ttv</a>(1), <a href="/docs/linux/man/1-v4lctl/">v4lctl</a>(1) </p>
