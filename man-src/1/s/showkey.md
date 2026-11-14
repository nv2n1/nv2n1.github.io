---
title: "showkey(1)"
name: "showkey"
section: "1"
letter: "s"
url: "/docs/linux/man/1-showkey/"
description: "showkey – examine the codes sent by the keyboard"
---

<h2 class="name">NAME</h2>
<p> showkey &#8211; examine the codes sent by the keyboard </p>
<h2>SYNOPSIS</h2>
<p> showkey [-h|&#8211;help] [-a|&#8211;ascii] [-s|&#8211;scancodes] [-k|&#8211;keycodes] [-V|&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <code>showkey</code> prints to standard output either the scan codes or the keycode or the `ascii&#8217; code of each key pressed. In the first two modes the program runs until 10 seconds have elapsed since the last key press or release event, or until it receives a suitable signal, like SIGTERM, from another process. In `ascii&#8217; mode the program terminates when the user types ^D. </p>
<p> When in scancode dump mode, <code>showkey</code> prints in hexadecimal format each byte received from the keyboard to the standard output. A new line is printed when an interval of about 0.1 seconds occurs between the bytes received, or when the internal receive buffer fills up. This can be used to determine roughly, what byte sequences the keyboard sends at once on a given key press. The scan code dumping mode is primarily intended for debugging the keyboard driver or other low level interfaces. As such it shouldn&#8217;t be of much interest to the regular end-user. However, some modern keyboards have keys or buttons that produce scancodes to which the kernel does not associate a keycode, and, after finding out what these are, the user can assign keycodes with <code><a href="/docs/linux/man/8-setkeycodes/">setkeycodes</a></code>(8). </p>
<p> When in the default keycode dump mode, <code>showkey</code> prints to the standard output the keycode number or each key pressed or released. The kind of the event, press or release, is also reported. Keycodes are numbers assigned by the kernel to each individual physical key. Every key has always only one associated keycode number, whether the keyboard sends single or multiple scan codes when pressing it. Using <code>showkey</code> in this mode, you can find out what numbers to use in your personalized keymap files. </p>
<p> When in `ascii&#8217; dump mode, <code>showkey</code> prints to the standard output the decimal, octal, and hexadecimal value(s) of the key pressed, according to he present keymap.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h &#8211;help</p>
<dd> <code>showkey</code> prints to the standard error output its version number, a compile option and a short usage message, then exits.</p>
<dt>-s &#8211;scancodes</p>
<dd> Starts <code>showkey</code> in scan code dump mode.</p>
<dt>-k &#8211;keycodes</p>
<dd> Starts <code>showkey</code> in keycode dump mode. This is the default, when no command line options are present.</p>
<dt>-a &#8211;ascii</p>
<dd> Starts <code>showkey</code> in `ascii&#8217; dump mode.</p>
<dt>-V &#8211;version</p>
<dd> <code>showkey</code> prints version number and exits.</dl>
<h2>2.6 KERNELS</h2>
<p> In 2.6 kernels key codes lie in the range 1-255, instead of 1-127. Key codes larger than 127 are returned as three bytes of which the low order 7 bits are: zero, bits 13-7, and bits 6-0 of the key code. The high order bits are: 0/1 for make/break, 1, 1. </p>
<p> In 2.6 kernels raw mode, or scancode mode, is not very raw at all. Scan codes are first translated to key codes, and when scancodes are desired, the key codes are translated back. Various transformations are involved, and there is no guarantee at all that the final result corresponds to what the keyboard hardware did send. So, if you want to know the scan codes sent by various keys it is better to boot a 2.4 kernel. Since 2.6.9 there also is the boot option atkbd.softraw=0 that tells the 2.6 kernel to return the actual scan codes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1), <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5), <code><a href="/docs/linux/man/8-setkeycodes/">setkeycodes</a></code>(8) </p>
<h2>Index</h2>
