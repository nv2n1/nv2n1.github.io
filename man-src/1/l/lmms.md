---

title: "lmms(1)"
name: "lmms"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lmms/"
description: "lmms – software for easy music production"
---

<p> <code>lmms</code> [ &#8212;<code>render</code> <i>file</i> ] [options]<br />
 <code>lmms</code> [ &#8212;<code>upgrade</code> <i>in</i> <i>out</i> ]<br />
 <code>lmms</code> [ &#8212;<code>dump</code> <i>in</i> ]<br />
 <code>lmms</code> [ file ]</p>
<p> <code>LMMS</code> LMMS is a free cross-platform alternative to commercial programs like FL Studio®, which allow you to produce music with your computer. This includes the creation of melodies and beats, the synthesis and mixing of sounds, and arranging of samples. You can have fun with your MIDI-keyboard and much more; all in a user-friendly and modern interface. </p>
<p> LMMS features components such as a Song Editor, a Beat+Bassline Editor, a Piano Roll, an FX Mixer as well as many powerful instruments and effects. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r, &#8211;render</code> <i>project-file</i></dt>
<dd> Render given file to either a wav- or ogg-file. See <code>-f</code> for details</dd>
<dt><code>-o, &#8211;output</code> <i>file</i></dt>
<dd> render into <i>file</i></dd>
<dt><code>-f, &#8211;output-format</code> <i>format</i></dt>
<dd> Specify format of render-output where <i>format</i> is either &#8216;wav&#8217; or &#8216;ogg&#8217;</dd>
<dt><code>-s, &#8211;samplerate</code> <i>samplerate</i></dt>
<dd> Specify output samplerate in Hz &#8211; range is 44100 (default) to 192000</dd>
<dt><code>-b, &#8211;bitrate</code> <i>bitrate</i></dt>
<dd> Specify output bitrate in kHz (for OGG encoding only), default is 160</dd>
<dt><code>-i, &#8211;interpolation</code> <i>method</i></dt>
<dd> Specify interpolation method &#8211; possible values are <i>linear</i>, <i>sincfastest</i> (default), <i>sincmedium</i>, <i>sincbest</i></dd>
<dt><code>-x, &#8211;oversampling</code> <i>value</i></dt>
<dd> Specify oversampling, possible values: 1, 2 (default), 4, 8</dd>
<dt><code>-u, &#8211;upgrade</code> <i>in</i> <i>out</i></dt>
<dd> Upgrade file <i>in</i> and save as <i>out</i></dd>
<dt><code>-d, &#8211;dump</code> <i>in</i></dt>
<dd> Dump XML of compressed file <i>in</i> (i.e. MMPZ-file)</dd>
<dt><code>-v, &#8211;version</dt>
<dd> Show version information and exit.</dd>
<dt>-h, &#8211;help</dt>
<dd> Show usage information and exit.</dd></dl>
<p> </code></p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://lmms.sf.net/">http://lmms.sf.net/</a></code> <code><a rel="nofollow" href="http://lmms.sf.net/wiki/">http://lmms.sf.net/wiki/</a></code></p>
<h2>AUTHORS</h2>
<p> <code>Tobias</code>Doerffel<code>&lt;tobydox/at/users.sourceforge.net&gt;,</code>Paul<code>Giblock</code>and<code>others.</code>See<code>AUTHORS</code>for<code>details.</code> </p>
