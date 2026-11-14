---
title: "jack-keyboard(1)"
name: "jack-keyboard"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack-keyboard/"
description: "jack-keyboard – A virtual keyboard for JACK MIDI"
---

<h2 class="name">NAME</h2>
<p> jack-keyboard &#8211; A virtual keyboard for JACK MIDI </p>
<h2>SYNOPSIS</h2>
<p> <code>jack-keyboard</code> [ <code>-C</code> ] [ <code>-G</code> ] [ <code>-K</code> ] [ <code>-T</code> ] [ <code>-V</code> ] [ <code>-a </code><i>input port</i> ] [ <code>-k</code> ] [ <code>-r </code><i>rate</i> ] [ <code>-t</code> ] [ <code>-u</code> ] [ <code>-c </code><i>channel</i> ] [ <code>-b </code><i>bank</i> ] [ <code>-p </code><i>program</i> ] [ <code>-l </code><i>layout</i> ] </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Enable &quot;keyboard cue&quot; &#8211; two horizontal lines over a part of keyboard; keys under the lower line are mapped to the lower row of your PC keyboard; keys under the upper line are mapped to the upper row.</p>
<dt><code>-G</code></p>
<dd> Disable GUI. It makes <code>jack-keyboard</code> look like it did before version 2.0.</p>
<dt><code>-K</code></p>
<dd> Grab the keyboard. This makes <code>jack-keyboard</code> receive keyboard events even when it does not have focus. In other words, you can play while mousing in a different window. </p>
<p> Note: It&#8217;s not reliable yet. It does not work when some other application keeps the keyboard grabbed. It does not work with GNOME. Even when it seems to work, some keyboard events may get lost.</p>
<dt><code>-T</code></p>
<dd> Toggle titlebar, on which channel/bank/program information is shown. With -G option, it disables titlebar; otherwise it enables it.</p>
<dt><code>-V</code></p>
<dd> Print version number to standard output and exit.</p>
<dt><code>-a </code><i>input port</i></p>
<dd> Automatically connect to the named input port. Note that this may cause problems with LASH.</p>
<dt><code>-k</code></p>
<dd> Allow connecting to other instances of jack-keyboard (see PIANOLA MODE below). Without this option, <code>jack-keyboard</code> will refuse to connect to any JACK client whose name starts in &quot;jack-keyboard&quot;; this is to prevent loops. Note that it&#8217;s impossible to connect instance of <code>jack-keyboard</code> to itself, even with this option set.</p>
<dt><code>-r </code><i>rate</i></p>
<dd> Set rate limit to <i>rate</i>, in Kbaud. Limit defined by the MIDI specification is 31.25. By default this parameter is zero, that is, rate limiting is disabled.</p>
<dt><code>-t</code></p>
<dd> Send all MIDI messages with zero time offset, making them play as soon as they reach the synth. This was the default behavior before version 1.6.</p>
<dt><code>-u</code></p>
<dd> By default, <code>jack-keyboard</code> does not send program/bank change messages after reconnecting, so the newly connected instrument remains at previous settings. This option changes that behaviour.</p>
<dt><code>-c </code><i>channel</i></p>
<dd> Set initial MIDI channel to <i>channel</i>; by default it&#8217;s 1.</p>
<dt><code>-b </code><i>bank</i></p>
<dd> Set initial MIDI bank to <i>bank</i>. With this option, <code>jack-keyboard</code> will send the bank/program change once, when it connects.</p>
<dt><code>-p </code><i>program</i></p>
<dd> Set initial MIDI program to <i>program</i>. With this option, <code>jack-keyboard</code> will send the bank/program change once, when it connects.</p>
<dt><code>-l </code><i>layout</i></p>
<dd> Specify the layout of computer keyboard being used. Valid arguments are QWERTY, QWERTZ, AZERTY and DVORAK. Default is QWERTY.</dl>
<h2>DESCRIPTION</h2>
<p> <code>jack-keyboard</code> is a virtual MIDI keyboard &#8211; a program that allows you to send JACK MIDI events (play ;-) using your PC keyboard. It&#8217;s somewhat similar to <code>vkeybd</code>, except it uses JACK MIDI instead of ALSA, and the keyboard mapping is much better &#8211; it uses the same layout as trackers (like Impulse Tracker) did, so you have two and half octaves under your fingers.</p>
<h2>KEY BINDINGS</h2>
<p> Keyboard mapping is the same as in Impulse Tracker. This is your QWERTY keyboard: </p>
<pre><code>
+ -- --+-- --+ +-- --+-- --+-- --+ +-- --+-- --+ | 2 | 3 | | 5 | 6 | 7 | | 9 | 0 |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+ | Q | W | E | R | T | Y | U | I | O | P |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+ | S | D | | G | H | J |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+ | Z | X | C | V | B | N | M |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+
</code></pre>
<p> And this is MIDI mapping: </p>
<pre><code>
+ -- --+-- --+ +-- --+-- --+-- --+ +-- --+-- --+ | C #5 | D #5 | | F #5 | G #5 | A #5 | | C #6 | D #6 |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+ | C5 | D5 | E5 | F5 | G5 | A5 | B5 | C6 | D6 | E6 |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+-- --+ | C #4 | D #4 | | F #4 | G #4 | A #4 |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+ | C4 | D4 | E4 | F4 | G4 | A4 | B4 |
    +-- --+-- --+-- --+-- --+-- --+-- --+-- --+
</code></pre>
<p> Spacebar is a sustain key. Holding it when pressing or releasing key will make that key sustained, i.e. Note Off MIDI event won&#8217;t be sent after releasing the key. To release (stop) all the sustained notes, press and release spacebar. </p>
<p> Holding Shift when pressing note will make it louder (it increases velocity). Holding Ctrl will do the opposite. You can change the default velocity by moving the Velocity slider. You can change the &quot;high&quot; and &quot;low&quot; velocity values by moving the slider while holding Shift or Ctrl keys. </p>
<p> Pressing &quot;-&quot; and &quot;+&quot; keys on numeric keypad changes the octave your keyboard is mapped to. Pressing &quot;*&quot; and &quot;/&quot; on numeric keypad changes MIDI program (instrument). Pressing Insert or Delete keys will connect <code>jack-keyboard</code> to the next/previous MIDI input port (it will cycle between running instances of ghostess, for example). Home and End keys change the MIDI channel. Page Up and Page Down keys switch the MIDI bank. </p>
<p> Esc works as a panic key &#8211; when you press it, all sound stops.</p>
<h2>SETTING CHANNEL/BANK/PROGRAM NUMBER DIRECTLY</h2>
<p> To switch directly to a channel, bank or program, enter its number on the numeric keypad (it won&#8217;t be shown in any way) and press Home or End (to change channel), Page Up or Page Down (to change bank) or &quot;/&quot; or &quot;*&quot; (to change program). For example, to change to program number 123, type, on the numeric keypad, &quot;123/&quot;, without quotes.</p>
<h2>TITLEBAR</h2>
<p> When <code>-G</code> xor <code>-T</code> is given, some informational messages in the title bar appear. They are supposed to be self explanatory. If you see &quot;bank/program change not sent&quot;, it means that the bank/program numbers as seen in the title bar were not sent. In other words, synth the <code>jack-keyboard</code> is connected to may use different values. This happens at startup and after switching between synths (using Insert/Delete keys). To send bank/program change at startup, use <code>-b</code> and <code>-p</code> parameters. To automatically send bank/program change after reconnect, use the <code>-u</code> option.</p>
<h2>PIANOLA MODE</h2>
<p> In addition to the MIDI output port, <code>jack-keyboard</code> also opens MIDI input (listening) port. MIDI events going into this port will be passed to the output port unmodified, except for channel number, which will be set to the one <code>jack-keyboard</code> is configured to use. Note On and Note Off MIDI events will cause visible effect (pressing and releasing) on keys, just like if they were being pressed using keyboard or mouse. </p>
<p> <code>jack-keyboard</code> will never connect to it&#8217;s own MIDI input port. It will also refuse to connect to any other client whose name begins in &quot;jack-keyboard&quot;, unless the &quot;-k&quot; option is given. It is, however, possible to connect these ports manually, using <code>jack_connect</code> or <code>qjackctl</code>; this may create feedback loop.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jackd/">jackd</a></code>(1), <code><a href="/docs/linux/man/1-ghostess/">ghostess</a></code>(1), <code><a href="/docs/linux/man/1-qjackctl/">qjackctl</a></code>(1)</p>
<h2>BUGS</h2>
<p> Key grabbing is unreliable. </p>
<p> Many PC keyboards have problems with polyphony. For example, with the one I&#8217;m using right now, it&#8217;s impossible to press &quot;c&quot;, &quot;v&quot; and &quot;b&quot; at the same time. It&#8217;s a hardware problem, not the software one. </p>
<p> The spin widgets used to set channel/bank/program number don&#8217;t take focus, so the value cannot be entered into them in the usual way. It&#8217;s because <code>jack-keyboard</code> already uses numeric keys for different purposes. You can still directly enter channel/bank/program in a way described above. </p>
<h2>Index</h2>
