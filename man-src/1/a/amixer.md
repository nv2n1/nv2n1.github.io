---
title: "amixer(1)"
name: "amixer"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amixer/"
description: "amixer – command-line mixer for ALSA soundcard driver"
---

<h2 class="name">NAME</h2>
<p> amixer &#8211; command-line mixer for ALSA soundcard driver </p>
<h2>SYNOPSIS</h2>
<p> <code>amixer</code> [<i>-option</i>] [<i>cmd</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>amixer</code> allows command-line control of the mixer for the ALSA soundcard driver. <code>amixer</code> supports multiple soundcards. </p>
<p> <code>amixer</code> with no arguments will display the current mixer settings for the default soundcard and device. This is a good way to see a list of the simple mixer controls you can use. </p>
<h2>COMMANDS</h2>
<dl>
<dt><i>help</i></p>
<dd> Shows syntax. </p>
<dt><i>info</i></p>
<dd> Shows the information about a mixer device. </p>
<dt><i>scontrols</i></p>
<dd> Shows a complete list of simple mixer controls. </p>
<dt><i>scontents</i></p>
<dd> Shows a complete list of simple mixer controls with their contents. </p>
<dt><i>set</i> or <i>sset</i> &lt;<i>SCONTROL</i>&gt; &lt;<i>PARAMETER</i>&gt; &#8230;</p>
<dd> Sets the simple mixer control contents. The parameter can be the volume either as a percentage from 0% to 100% with <i>%</i> suffix, a dB gain with <i>dB</i> suffix (like -12.5dB), or an exact hardware value. The dB gain can be used only for the mixer elements with available dB information. When plus(+) or minus(-) letter is appended after volume value, the volume is incremented or decremented from the current value, respectively. </p>
<p> The parameters <i>cap, nocap, mute, unmute, toggle</i> are used to change capture (recording) and muting for the group specified. </p>
<p> The optional modifiers can be put as extra parameters before the value to specify the stream direction or channels to apply. The modifiers <i>playback</i> and <i>capture</i> specify the stream, and the modifiers <i>front, frontleft, frontright, frontcenter, center, rear, rearright, rearleft, woofer</i> are used to specify channels to be changed. </p>
<p> A simple mixer control must be specified. Only one device can be controlled at a time. </p>
<dt><i>get</i> or <i>sget</i> &lt;<i>SCONTROL</i>&gt;</p>
<dd> Shows the simple mixer control contents. </p>
<p> A simple mixer control must be specified. Only one device can be controlled at a time. </p>
<dt><i>controls</i></p>
<dd> Shows a complete list of card controls. </p>
<dt><i>contents</i></p>
<dd> Shows a complete list of card controls with their contents. </p>
<dt><i>cset</i> &lt;<i>CONTROL</i>&gt; &lt;<i>PARAMETER</i>&gt; &#8230;</p>
<dd> Sets the card control contents. The identifier has these components: iface, name, index, device, subdevice, numid. The next argument specifies the value of control. </p>
<dt><i>cget</i> &lt;<i>CONTROL</i>&gt;</p>
<dd> Shows the card control contents. The identifier has same syntax as for the <i>cset</i> command. </p>
</dl>
<h2>ADVANCED COMMANDS</h2>
<dl>
<dt><i>sevents</i></p>
<dd> Shows the events for the simple mixer controls. </p>
<dt><i>events</i></p>
<dd> Shows the events for the mixer controls. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>-c</i> card</p>
<dd>
<p> Select the card number to control. The device name created from this parameter has syntax &#8216;hw:N&#8217; where N is specified card number. </p>
<dt><i>-D</i> device</p>
<dd>
<p> Select the device name to control. The default control name is &#8216;default&#8217;. </p>
<dt><i>-s</i> | <i>&#8211;stdin</i></p>
<dd>
<p> Read from stdin and execute the command on each line sequentially. When this option is given, the command in command-line arguments is ignored. </p>
<p> Only sset and cset are accepted. Other commands are ignored. The commands to unmatched ids are ignored without errors too. </p>
<dt><i>-h</i></p>
<dd> Help: show syntax. </p>
<dt><i>-q</i></p>
<dd> Quiet mode. Do not show results of changes. </p>
<dt><i>-R</i></p>
<dd> Use the raw value for evaluating the percentage representation. This is the default mode. </p>
<dt><i>-M</i></p>
<dd> Use the mapped volume for evaluating the percentage representation like <code>alsamixer</code>, to be more natural for human ear. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>amixer -c 1 sset Line,0 80%,40% unmute cap</code></p>
<dd> will set the second soundcard&#8217;s left line input volume to 80% and right line input to 40%, unmute it, and select it as a source for capture (recording). </p>
<dt><code>amixer -c 1 &#8212; sset Master playback -20dB</code></p>
<dd> will set the master volume of the second card to -20dB. If the master has multiple channels, all channels are set to the same value. </p>
<dt><code>amixer -c 1 set PCM 2dB+</code></p>
<dd> will increase the PCM volume of the second card with 2dB. When both playback and capture volumes exist, this is applied to both volumes. </p>
<dt><code>amixer -c 2 cset iface=MIXER,name=&#8217;Line Playback Volume&quot;,index=1 40%</code></p>
<dd> will set the third soundcard&#8217;s second line playback volume(s) to 40% </p>
<dt><code>amixer -c 2 cset numid=34 40%</code></p>
<dd> will set the 34th soundcard element to 40% </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1) </code> </p>
<h2>BUGS</h2>
<p> None known. </p>
<h2>AUTHOR</h2>
<p> <code>amixer</code> is by Jaroslav Kysela &lt;perex [at] perex.cz&gt;. This document is by Paul Winkler &lt;zarmzarm [at] erols.com&gt; and Jaroslav Kysela &lt;perex [at] perex.cz&gt;. </p>
<h2>Index</h2>
