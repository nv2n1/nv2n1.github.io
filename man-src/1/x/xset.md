---
title: "xset(1)"
name: "xset"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xset/"
description: "xset – user preference utility for X"
---

<h2 class="name">NAME</h2>
<p> xset &#8211; user preference utility for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xset</code> [-display <i>display</i>]<br />
 [-b] [b {on|off}] [b [<i>volume</i> [<i>pitch</i> [<i>duration</i>]]]]<br />
 [-bc] [bc]<br />
 [-c] [c {on|off}] [c [<i>volume</i>]]<br />
 [+dpms] [-dpms]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[dpms <i>standby</i> [<i> suspend</i> [<i> off</i>]]]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[dpms force {standby|suspend|off|on}]</p>
<p> [fp=<i>pathlist</i>] [-fp=<i>pathlist</i>] [+fp=<i>pathlist</i>] [fp-<i>pathlist</i>] [fp+<i>pathlist</i>]<br />
 [fp default] [fp rehash]<br />
 [-led [<i>integer</i>|named <i>indicator</i>]] [led [<i>integer</i>|named <i>indicator</i>]]<br />
 [led {on|off}]<br />
 [mouse [<i>accel_mult</i>[/<i>accel_div</i>] [<i>threshold</i>]]] [mouse default]<br />
 [p <i>pixel</i> <i>color</i>]<br />
 [-r [keycode]] [r [keycode]] [r {on|off}] [r rate <i>delay</i> [<i>rate</i>]]<br />
 [s [<i>length</i> [<i>period</i>]]] [s {blank|noblank}] [s {expose|noexpose}] [s {on|off}] [s default] [s activate] [s reset]<br />
 [q]<br />
 [-version]</p>
<h2>DESCRIPTION</h2>
<p> This program is used to set various user preference options of the display.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This option specifies the server to use; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<dl>
<dt><code>b</code></p>
<dd> The <code>b</code> option controls bell volume, pitch and duration. This option accepts up to three numerical parameters, a preceding dash(-), or a &#8216;on/off&#8217; flag. If no parameters are given, or the &#8216;on&#8217; flag is used, the system defaults will be used. If the dash or &#8216;off&#8217; are given, the bell will be turned off. If only one numerical parameter is given, the bell volume will be set to that value, as a percentage of its maximum. Likewise, the second numerical parameter specifies the bell pitch, in hertz, and the third numerical parameter specifies the duration in milliseconds. Note that not all hardware can vary the bell characteristics. The X server will set the characteristics of the bell as closely as it can to the user&#8217;s specifications.</dl>
<dl>
<dt><code>bc</code></p>
<dd> The <code>bc</code> option controls <i>bug compatibility</i> mode in the server, if possible; a preceding dash(-) disables the mode, otherwise the mode is enabled. Various pre-R4 clients pass illegal values in some protocol requests, and pre-R4 servers did not correctly generate errors in these cases. Such clients, when run against an R4 server, will terminate abnormally or otherwise fail to operate correctly. Bug compatibility mode explicitly reintroduces certain bugs into the X server, so that many such clients can still be run. This mode should be used with care; new application development should be done with this mode disabled. The server must support the MIT-SUNDRY-NONSTANDARD protocol extension in order for this option to work.</p>
<dt><code>c</code></p>
<dd> The <code>c</code> option controls key click. This option can take an optional value, a preceding dash(-), or an &#8216;on/off&#8217; flag. If no parameter or the &#8216;on&#8217; flag is given, the system defaults will be used. If the dash or &#8216;off&#8217; flag is used, keyclick will be disabled. If a value from 0 to 100 is given, it is used to indicate volume, as a percentage of the maximum. The X server will set the volume to the nearest value that the hardware can support.</dl>
<dl>
<dt><code>-dpms</code></p>
<dd> The <code>-dpms</code> option disables DPMS (Energy Star) features.</p>
<dt><code>+dpms</code></p>
<dd> The <code>+dpms</code> option enables DPMS (Energy Star) features.</p>
<dt><code>dpms </code><i>flags&#8230;</i></p>
<dd> The <code>dpms</code> option allows the DPMS (Energy Star) parameters to be set. The option can take up to three numerical values, or the `force&#8217; flag followed by a DPMS state. The `force&#8217; flags forces the server to immediately switch to the DPMS state specified. The DPMS state can be one of `standby&#8217;, `suspend&#8217;, `off&#8217;, or `on&#8217;. When numerical values are given, they set the inactivity period (in units of seconds) before the three modes are activated. The first value given is for the `standby&#8217; mode, the second is for the `suspend&#8217; mode, and the third is for the `off&#8217; mode. Setting these values implicitly enables the DPMS features. A value of zero disables a particular mode.</p>
<dt><code>fp= </code><i>path,&#8230;</i></p>
<dd> The <code>fp=</code> sets the font path to the entries given in the path argument. The entries are interpreted by the server, not by the client. Typically they are directory names or font server names, but the interpretation is server-dependent.</p>
<dt><code>fp default</code></p>
<dd> The <code>default</code> argument causes the font path to be reset to the server&#8217;s default.</p>
<dt><code>fp rehash</code></p>
<dd> The <code>rehash</code> argument resets the font path to its current value, causing the server to reread the font databases in the current font path. This is generally only used when adding new fonts to a font directory (after running <i>mkfontdir</i> to recreate the font database).</dl>
<dl>
<dt><code>-fp </code>or fp-</p>
<dd> The <code>-fp</code> and <code>fp-</code> options remove elements from the current font path. They must be followed by a comma-separated list of entries.</dl>
<dl>
<dt><code>+fp </code>or fp+</p>
<dd> This <code>+fp</code> and <code>fp+</code> options prepend and append elements to the current font path, respectively. They must be followed by a comma-separated list of entries.</dl>
<dl>
<dt><code>led</code></p>
<dd> The <code>led</code> option controls the keyboard LEDs. This controls the turning on or off of one or all of the LEDs. It accepts an optional integer, a preceding dash(-) or an &#8216;on/off&#8217; flag. If no parameter or the &#8216;on&#8217; flag is given, all LEDs are turned on. If a preceding dash or the flag &#8216;off&#8217; is given, all LEDs are turned off. If a value between 1 and 32 is given, that LED will be turned on or off depending on the existence of a preceding dash. &#8220;xset led 3&#8221; would turn led #3 on. &#8220;xset -led 3&#8221; would turn it off. The particular LED values may refer to different LEDs on different hardware. If the X server supports the XKEYBOARD (XKB) extension, leds may be referenced by the XKB indicator name by specifying the `named&#8217; keyword and the indicator name. For example, to turn on the Scroll Lock LED:</p>
<dt>
<dd> xset led named &quot;Scroll Lock&quot;</dl>
<dl>
<dt><code>mouse</code></p>
<dd> The <code>m</code> option controls the mouse parameters; it may be abbreviated to &#8216;m&#8217;. Of course, it applies to most pointing devices, not just mice. The parameters for the pointing device are `acceleration&#8217; and `threshold&#8217;. The acceleration can be specified as an integer, or as a simple fraction. Threshold is just an integer. The setting is applied to all connected pointing devices. <a href="/docs/linux/man/1-xinput/">xinput</a>(1) should be used if you need device-specific settings.</dl>
<p> By default the pointer (the on-screen representation of the pointing device) will go `acceleration&#8217; times as fast when the device travels more than `threshold&#8217; mickeys (i.e. would-be pixels) in 10 ms, including a small transition range. This way, the pointing device can be used for precise alignment when it is moved slowly, yet it can be set to travel across the screen in a flick of the wrist when desired. One or both parameters for the <code>m</code> option can be omitted, but if only one is given, it will be interpreted as the acceleration. If no parameters or the flag &#8216;default&#8217; is used, the system defaults will be set. </p>
<p> If the `threshold&#8217; parameter is provided and 0, the `acceleration&#8217; parameter will be used in the exponent of a more natural and continuous formula, giving precise control for slow motion but big reach for fast motion, and a progressive transition for motions in between. Recommended `acceleration&#8217; value in this case is 3/2 to 3, but not limited to that range. </p>
<p> In the X.org X Server 1.6 and above, the behaviour described so far is linked to the default profile. There are other profiles (i.e. functions determining pointer acceleration from device velocity) and additional settings, so the above description may not apply to non-default cases. In the X.org Server 1.7, these are available as input device properties (see xinput). </p>
<dl>
<dt><code>p</code></p>
<dd> The <code>p</code> option controls pixel color values. The parameters are the color map entry number in decimal, and a color specification. The root background colors may be changed on some servers by altering the entries for BlackPixel and WhitePixel. Although these are often 0 and 1, they need not be. Also, a server may choose to allocate those colors privately, in which case an error will be generated. The map entry must not be a read-only color, or an error will result.</dl>
<dl>
<dt><code>r</code></p>
<dd> The <code>r</code> option controls the autorepeat. Invoking with &quot;<code>-r</code>&quot;, or &quot;<code>r off</code>&quot;, will disable autorepeat, whereas &quot;<code>r</code>&quot;, or &quot;<code>r on</code>&quot; will enable autorepeat. Following the &quot;<code>-r</code>&quot; or &quot;<code>r</code>&quot; option with an integer keycode between 0 and 255 will disable or enable autorepeat on that key respectively, but only if it makes sense for the particular keycode. Keycodes below 8 are not typically valid for this command. Example: &quot;<code>xset -r 10</code>&quot; will disable autorepeat for the &quot;1&quot; key on the top row of an IBM PC keyboard. </p>
<p> If the server supports the XFree86-Misc extension, or the XKB extension, then a parameter of &#8216;rate&#8217; is accepted and should be followed by zero, one or two numeric values. The first specifies the delay before autorepeat starts and the second specifies the repeat rate. In the case that the server supports the XKB extension, the delay is the number of milliseconds before autorepeat starts, and the rate is the number of repeats per second. If the rate or delay is not given, it will be set to the default value.</dl>
<dl>
<dt><code>s</code></p>
<dd> The <code>s</code> option lets you set the screen saver parameters. This option accepts up to two numerical parameters, a &#8216;blank/noblank&#8217; flag, an &#8216;expose/noexpose&#8217; flag, an &#8216;on/off&#8217; flag, an &#8216;activate/reset&#8217; flag, or the &#8216;default&#8217; flag. If no parameters or the &#8216;default&#8217; flag is used, the system will be set to its default screen saver characteristics. The &#8216;on/off&#8217; flags simply turn the screen saver functions on or off. The &#8216;activate&#8217; flag forces activation of screen saver even if the screen saver had been turned off. The &#8216;reset&#8217; flag forces deactivation of screen saver if it is active. The &#8216;blank&#8217; flag sets the preference to blank the video (if the hardware can do so) rather than display a background pattern, while &#8216;noblank&#8217; sets the preference to display a pattern rather than blank the video. The &#8216;expose&#8217; flag sets the preference to allow window exposures (the server can freely discard window contents), while &#8216;noexpose&#8217; sets the preference to disable screen saver unless the server can regenerate the screens without causing exposure events. The length and period parameters for the screen saver function determines how long the server must be inactive for screen saving to activate, and the period to change the background pattern to avoid burn in. The arguments are specified in seconds. If only one numerical parameter is given, it will be used for the length.</dl>
<dl>
<dt><code>q</code></p>
<dd> The <code>q</code> option gives you information on the current settings.</dl>
<dl>
<dt><code>-version</code></p>
<dd> The <code>-version</code> option prints the program version and exits without doing anything else.</dl>
<p> These settings will be reset to default values when you log out. </p>
<p> Note that not all X implementations are guaranteed to honor all of these options.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-xmodmap/">xmodmap</a>(1), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/1-xsetroot/">xsetroot</a>(1), <a href="/docs/linux/man/1-xinput/">xinput</a>(1)</p>
<h2>AUTHOR</h2>
<p> Bob Scheifler, MIT Laboratory for Computer Science<br />
 David Krikorian, MIT Project Athena (X11 version)<br />
 XFree86-Misc support added by David Dawes and Joe Moss<br />
 Manpage updates added by Mike A. Harris &lt;mharris [at] redhat.com&gt; </p>
<h2>Index</h2>
