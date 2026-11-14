---
title: "midi2ly(1)"
name: "midi2ly"
section: "1"
letter: "m"
url: "/docs/linux/man/1-midi2ly/"
description: "midi2ly – manual page for midi2ly (LilyPond) 2.12.2"
---

<h2>NAME</h2>
<p> midi2ly &#8211; manual page for midi2ly (LilyPond) 2.12.2</p>
<h2>SYNOPSIS</h2>
<p> <code>midi2ly</code> [<i>OPTION</i>]&#8230; <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> Convert MIDI to LilyPond input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;absolute-pitches</code></p>
<dd> print absolute pitches</p>
<dt><code>-d</code>, <code>&#8211;duration-quant</code>=<i>DUR</i></p>
<dd> quantise note durations on DUR</p>
<dt><code>-e</code>, <code>&#8211;explicit-durations</code></p>
<dd> print explicit durations</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help and exit</p>
<dt><code>-k</code>, <code>&#8211;key</code>=<i>ALT[</i>:MINOR]</p>
<dd> set key: ALT=+sharps|-flats; MINOR=1</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> write output to FILE</p>
<dt><code>-s</code>, <code>&#8211;start-quant</code>=<i>DUR</i></p>
<dd> quantise note starts on DUR</p>
<dt><code>-t</code>, <code>&#8211;allow-tuplet</code>=<i>DUR</i>*NUM/DEN</p>
<dd> allow tuplet durations DUR*NUM/DEN</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> be verbose</p>
<dt><code>&#8211;version</code></p>
<dd> show version number and exit</p>
<dt><code>-w</code>, <code>&#8211;warranty</code></p>
<dd> show warranty and copyright</p>
<dt><code>-x</code>, <code>&#8211;text-lyrics</code></p>
<dd> treat every text as a lyric</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> <tt>$ midi2ly --key=-2:1 --duration-quant=32 --allow-tuplet=4*2/3 --allow-tuplet=2*4/3 foo.midi</tt></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs via <a rel="nofollow" href="http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs">http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs</a></p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>midi2ly</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>midi2ly</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info midi2ly</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
