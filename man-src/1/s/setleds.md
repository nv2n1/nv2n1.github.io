---
title: "setleds(1)"
name: "setleds"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setleds/"
description: "setleds – set the keyboard leds"
---

<h2 class="name">NAME</h2>
<p> setleds &#8211; set the keyboard leds </p>
<h2>SYNOPSIS</h2>
<p> <code>setleds</code> [<i>-v</i>] [<i>-L</i>] [<i>-D</i>] [<i>-F</i>] [<i>{+|-}num</i>] [<i>{+|-}caps</i>] [<i>{+|-}scroll</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Setleds</code> reports and changes the led flag settings of a VT (namely NumLock, CapsLock and ScrollLock). Without arguments, <code>setleds</code> prints the current settings. With arguments, it sets or clears the indicated flags (and leaves the others unchanged). The settings before and after the change are reported if the -v flag is given. </p>
<p> The led flag settings are specific for each VT (and the VT corresponding to stdin is used). </p>
<p> By default (or with option -F), <code>setleds</code> will only change the VT flags (and their setting may be reflected by the keyboard leds). </p>
<p> With option -D, <code>setleds</code> will change both the VT flags and their default settings (so that a subsequent reset will not undo the change). This might be useful for people who always want to have numlock set. </p>
<p> With option -L, <code>setleds</code> will not touch the VT flags, but only change the leds. From this moment on, the leds will no longer reflect the VT flags (but display whatever is put into them). The command <code>setleds -L</code> (without further arguments) will restore the situation in which the leds reflect the VT flags. </p>
<p> One might use <code>setleds</code> in /etc/rc to define the initial and default state of NumLock, e.g. by<br />
 INITTY=/dev/tty[1-8]<br />
 for tty in $INITTY; do<br />
 setleds -D +num &lt; $tty<br />
 done</p>
<h2>OPTIONS</h2>
<dl>
<dt>-num +num</p>
<dd> Clear or set NumLock. (At present, the NumLock setting influences the interpretation of keypad keys. Pressing the NumLock key complements the NumLock setting.)</p>
<dt>-caps +caps</p>
<dd> Clear or set CapsLock. (At present, the CapsLock setting complements the Shift key when applied to letters. Pressing the CapsLock key complements the CapsLock setting.)</p>
<dt>-scroll +scroll</p>
<dd> Clear or set ScrollLock. (At present, pressing the ScrollLock key (or ^S/^Q) stops/starts console output.)</dl>
<h2>BUGS</h2>
<p> In keyboard application mode the NumLock key does not influence the NumLock flag setting.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) </p>
<h2>Index</h2>
