---
title: "midicopy(1)"
name: "midicopy"
section: "1"
letter: "m"
url: "/docs/linux/man/1-midicopy/"
description: "midicopy – Copy selected track, channel, time interval of a MIDI file to another MIDI file"
---

<h2>NAME</h2>
<p> midicopy &#8211; Copy selected track, channel, time interval of a MIDI file to another MIDI file</p>
<h2>SYNOPSIS</h2>
<p> <code>midicopy</code> [<code>-ver</code>] [<code>-trks</code> <i>n1,n2,..</i>] [<code>-chans</code> <i>n1,n2,&#8230;</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-from</code>&nbsp;<wbr><i>n&nbsp;<wbr>(in midi ticks)</i>]&nbsp;<wbr>[<code>-to</code>&nbsp;<wbr><i>n&nbsp;<wbr>(in midi ticks)</i>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-fromsec&nbsp;<wbr>%f</code>&nbsp;<wbr><i>n&nbsp;<wbr>(in seconds)</i>]&nbsp;<wbr>[<code>-tosec</code>&nbsp;<wbr><i>n&nbsp;<wbr>(in seconds)</i>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-frombeat&nbsp;<wbr>%f</code>&nbsp;<wbr><i>n&nbsp;<wbr>(in beats)</i>]&nbsp;<wbr>[<code>-tosec</code>&nbsp;<wbr><i>n&nbsp;<wbr>(in beats)</i>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-replace</code>&nbsp;<wbr><i>trk,loc,val</i>]&nbsp;<wbr><i>input.mid output.mid</i></p>
<h2>DESCRIPTION</h2>
<p> <code>midicopy</code> is used to copy part of a MIDI file to another MIDI file. You can select a particular time interval, particular channels, and particular tracks or any combinations. If one or both of the run time parameters -from or -to are included, the program returns the playing time in seconds of the output file. Midicopy was developed by Seymour Shlien from the midifilelib distribution available from <i><a rel="nofollow" href="http://www.harmony-central.com/MIDI/midifilelib.tar.gz">http://www.harmony-central.com/MIDI/midifilelib.tar.gz</a></i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ver</code></p>
<dd> prints version number and then exits</p>
<dt><code>-trks n</code></p>
<dd> Selects the tracks to be copied where the track numbers start from 1. If more than one track is specified, they should be separated by commas. You should always copy track 1 since by convention it contains information pertinent to all the other tracks. By default all tracks are copied unless you specify particular tracks using this run time parameter.</p>
<dt><code>-chns n</code></p>
<dd> Like above, it specifies the MIDI channels to be copied. By default all channels are copied. Channel numbers also start from 1.</p>
<dt><code>-from n</code></p>
<dd> The program will copy all MIDI commands starting from midi pulse number n. By default it will start from time zero or the beginning of the MIDI file.</p>
<dt><code>-to n</code></p>
<dd> Stops copying all events after midi pulse number n. By default the file is copied to the end.</p>
<dt><code>-frombeat n</code></p>
<dd> The program will copy all MIDI commands starting from quarter beat number n. By default it will start from time zero or the beginning of the MIDI file.</p>
<dt><code>-tobeat n</code></p>
<dd> Stops copying all events after quarter beat number n. By default the file is copied to the end.</p>
<dt><code>-fromsec n</code></p>
<dd> The program will copy all MIDI commands starting from time n in seconds.</p>
<dt><code>-tosec n</code></p>
<dd> Stops copying all events after time n in seconds. These two options (-fromsec and -tosec) do not work accurately if the MIDI file has more than one tempo command. Only the first one is used for converting seconds into MIDI pulse units. It is therefore preferable to use the -from and -to options.</p>
<dt><code>-replace trk,loc,val</code></p>
<dd> This option should be used alone. Midicopy will copy the entire file verbatim except it will replace a byte by val, where the byte is located in the specified track (trk) and specified position (loc). Commonly this function is used for changing a particular MIDI program number (instrument) associated with a channel. You need to know the byte count in the track of that parameter in order to use this function,</dl>
<h2>EXAMPLE</h2>
<p> <code>midicopy.exe -trks 1,5 -from 2669 -to 8634 uzicko.mid fragment.mid</code> Midicopy will copy tracks 1 and 5 starting from midi pulse position 2669 and ending at MIDI pulse position 8634. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-abcmtex/">abcmtex</a></i>(1), <i><a href="/docs/linux/man/1-abc2abc/">abc2abc</a></i>(1), <i><a href="/docs/linux/man/1-abc2midi/">abc2midi</a></i>(1), <i><a href="/docs/linux/man/1-midi2abc/">midi2abc</a></i>(1) ,<i><a href="/docs/linux/man/1-yaps/">yaps</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Seymour Shlien.</p>
<h2>VERSION</h2>
<p> This man page describes midicopy version 1.04 from September 19 2005. </p>
<h2>Index</h2>
