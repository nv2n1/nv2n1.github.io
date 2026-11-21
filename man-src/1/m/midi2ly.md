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
<p> <code>midi2ly</code> [<i>OPTION</i>]&#8230; <i>FILE</i></p>
<p> Convert MIDI to LilyPond input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;absolute-pitches</code></dt>
<dd> print absolute pitches</dd>
<dt><code>-d</code>, <code>&#8211;duration-quant</code>=<i>DUR</i></dt>
<dd> quantise note durations on DUR</dd>
<dt><code>-e</code>, <code>&#8211;explicit-durations</code></dt>
<dd> print explicit durations</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help and exit</dd>
<dt><code>-k</code>, <code>&#8211;key</code>=<i>ALT[</i>:MINOR]</dt>
<dd> set key: ALT=+sharps|-flats; MINOR=1</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></dt>
<dd> write output to FILE</dd>
<dt><code>-s</code>, <code>&#8211;start-quant</code>=<i>DUR</i></dt>
<dd> quantise note starts on DUR</dd>
<dt><code>-t</code>, <code>&#8211;allow-tuplet</code>=<i>DUR</i>*NUM/DEN</dt>
<dd> allow tuplet durations DUR*NUM/DEN</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose</dd>
<dt><code>&#8211;version</code></dt>
<dd> show version number and exit</dd>
<dt><code>-w</code>, <code>&#8211;warranty</code></dt>
<dd> show warranty and copyright</dd>
<dt><code>-x</code>, <code>&#8211;text-lyrics</code></dt>
<dd> treat every text as a lyric</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> <tt>$ midi2ly --key=-2:1 --duration-quant=32 --allow-tuplet=4*2/3 --allow-tuplet=2*4/3 foo.midi</tt></dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs via <a rel="nofollow" href="http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs">http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs</a></p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>midi2ly</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>midi2ly</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info midi2ly</code></dd></dl>
<p> should give you access to the complete manual. </p>
