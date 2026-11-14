---
title: "amidi(1)"
name: "amidi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amidi/"
description: "amidi – read from and write to ALSA RawMIDI ports"
---

<h2 class="name">NAME</h2>
<p> amidi &#8211; read from and write to ALSA RawMIDI ports</p>
<h2>SYNOPSIS</h2>
<p> <code>amidi</code> [<i>-p port</i>] [<i>-s file</i> | <i>-S data</i>] [<i>-r file</i>] [<i>-d</i>] [<i>-t seconds</i>] [<i>-a</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>amidi</code> is a command-line utility which allows one to receive and send SysEx (system exclusive) data from/to external MIDI devices. It can also send any other MIDI commands. </p>
<p> <code>amidi</code> handles only files containing raw MIDI commands, without timing information. <code>amidi</code> does not support Standard MIDI (.mid) files, but <code><a href="/docs/linux/man/1-aplaymidi/">aplaymidi</a>(1)</code> and <code><a href="/docs/linux/man/1-arecordmidi/">arecordmidi</a>(1)</code> do. </p>
<h2>OPTIONS</h2>
<p> Use the <i>-h,</i> <i>-V,</i> <i>-l,</i> or <i>-L</i> options to display information; or use at least one of the <i>-s,</i> <i>-r,</i> <i>-S,</i> or <i>-d</i> options to specify what data to send or receive. </p>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd> Help: prints a list of options. </p>
<dt><i>-V, &#8211;version</i></p>
<dd> Prints the current version. </p>
<dt><i>-l, &#8211;list-devices</i></p>
<dd> Prints a list of all hardware MIDI ports. </p>
<dt><i>-L, &#8211;list-rawmidis</i></p>
<dd> Prints all RawMIDI definitions. (used when debugging configuration files) </p>
<dt><i>-p, &#8211;port=name</i></p>
<dd> Sets the name of the ALSA RawMIDI port to use. If this is not specified, <code>amidi</code> uses the default port defined in the configuration file (the default for this is port 0 on card 0, which may not exist). </p>
<dt><i>-s, &#8211;send=filename</i></p>
<dd> Sends the contents of the specified file to the MIDI port. The file must contain raw MIDI commands (e.g. a .syx file); for Standard MIDI (.mid) files, use <code><a href="/docs/linux/man/1-aplaymidi/">aplaymidi</a>(1).</code> </p>
<dt><i>-r, &#8211;receive=filename</i></p>
<dd> Writes data received from the MIDI port into the specified file. The file will contain raw MIDI commands (such as in a .syx file); to record a Standard MIDI (.mid) file, use <code><a href="/docs/linux/man/1-arecordmidi/">arecordmidi</a>(1).</code> </p>
<p> <code>amidi</code> will filter out any Active Sensing and Clock bytes (FEh, F8h), unless the <i>-a</i> or <i>-c</i> options have been given. </p>
<dt><i>-S, &#8211;send-hex=&#8230;</i></p>
<dd> Sends the bytes specified as hexadecimal numbers to the MIDI port. </p>
<dt><i>-d, &#8211;dump</i></p>
<dd> Prints data received from the MIDI port as hexadecimal bytes. Active Sensing and Clock bytes (FEh, F8h) will not be shown, unless the <i>-a</i> or <i>-c</i> options have been given. </p>
<p> This option is useful for debugging. </p>
<dt><i>-t, &#8211;timeout=seconds</i></p>
<dd> Stops receiving data when no data has been received for the specified amount of time. </p>
<p> If this option has not been given, you must press Ctrl+C (or kill <code>amidi</code>) to stop receiving data. </p>
<dt><i>-a, &#8211;active-sensing</i></p>
<dd> Does not ignore Active Sensing bytes (FEh) when saving or printing received MIDI commands. </p>
<dt><i>-c, &#8211;clock</i></p>
<dd> Does not ignore Clock bytes (F8h) when saving or printing received MIDI commands. </p>
<dt><i>-i, &#8211;sysex-interval=mseconds</i></p>
<dd> Adds a delay in between each SysEx message sent to a device. It is useful when sending firmware updates via SysEx messages to a remote device. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>amidi -p hw:0 -s my_settings.syx</code></p>
<dd> will send the MIDI commands in <i>my_settings.syx</i> to port <i>hw:0.</i> </p>
<dt><code>amidi -p hw:1,0,0 -s firmware.syx -i 100</code></p>
<dd> will send the MIDI commands in <i>firmware.syx</i> to port <i>hw:1,0,0</i> with 100 milliseconds delay in between each SysEx message. </p>
<dt><code>amidi -S &#8216;F0 43 10 4C 00 00 7E 00 F7&#8217;</code></p>
<dd> sends an XG Reset to the default port. </p>
<dt><code>amidi -p hw:1,2 -S F0411042110C000000000074F7 -r dump.syx -t 1</code></p>
<dd> sends a &#8220;Parameter Dump Request&#8221; to a GS device, saves the received parameter data to the file <i>dump.syx,</i> and stops after the device has finished sending data (when no data has been received for one second). </p>
<dt><code>amidi -p virtual -d</code></p>
<dd> creates a virtual RawMIDI port and prints all data sent to this port. </p>
</dl>
<h2>FILES</h2>
<p> <i>/usr/share/alsa/alsa.conf</i> default rawmidi definitions<br />
 <i>/etc/asound.conf</i> system-wide rawmidi definitions<br />
 <i>~/.asoundrc</i> user specific rawmidi definitions </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-aplaymidi/">aplaymidi</a>(1)<br />
 <a href="/docs/linux/man/1-arecordmidi/">arecordmidi</a>(1) </p>
<h2>AUTHOR</h2>
<p> Clemens Ladisch &lt;clemens [at] ladisch.de&gt; </p>
<h2>Index</h2>
