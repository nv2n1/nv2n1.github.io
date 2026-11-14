---
title: "lmms(1)"
name: "lmms"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lmms/"
description: "lmms – software for easy music production"
---

<h2 class="name">NAME</h2>
<p> lmms &#8211; software for easy music production </p>
<h2>SYNOPSIS</h2>
<p> <code>lmms</code> [ &#8212;<code>render</code> <i>file</i> ] [options]<br />
 <code>lmms</code> [ &#8212;<code>upgrade</code> <i>in</i> <i>out</i> ]<br />
 <code>lmms</code> [ &#8212;<code>dump</code> <i>in</i> ]<br />
 <code>lmms</code> [ file ]</p>
<h2>DESCRIPTION</h2>
<p> <code>LMMS</code> LMMS is a free cross-platform alternative to commercial programs like FL Studio®, which allow you to produce music with your computer. This includes the creation of melodies and beats, the synthesis and mixing of sounds, and arranging of samples. You can have fun with your MIDI-keyboard and much more; all in a user-friendly and modern interface. </p>
<p> LMMS features components such as a Song Editor, a Beat+Bassline Editor, a Piano Roll, an FX Mixer as well as many powerful instruments and effects. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r, &#8211;render</code> <i>project-file</i></p>
<dd> Render given file to either a wav- or ogg-file. See <code>-f</code> for details</p>
<dt><code>-o, &#8211;output</code> <i>file</i></p>
<dd> render into <i>file</i></p>
<dt><code>-f, &#8211;output-format</code> <i>format</i></p>
<dd> Specify format of render-output where <i>format</i> is either &#8216;wav&#8217; or &#8216;ogg&#8217;</p>
<dt><code>-s, &#8211;samplerate</code> <i>samplerate</i></p>
<dd> Specify output samplerate in Hz &#8211; range is 44100 (default) to 192000</p>
<dt><code>-b, &#8211;bitrate</code> <i>bitrate</i></p>
<dd> Specify output bitrate in kHz (for OGG encoding only), default is 160</p>
<dt><code>-i, &#8211;interpolation</code> <i>method</i></p>
<dd> Specify interpolation method &#8211; possible values are <i>linear</i>, <i>sincfastest</i> (default), <i>sincmedium</i>, <i>sincbest</i></p>
<dt><code>-x, &#8211;oversampling</code> <i>value</i></p>
<dd> Specify oversampling, possible values: 1, 2 (default), 4, 8</p>
<dt><code>-u, &#8211;upgrade</code> <i>in</i> <i>out</i></p>
<dd> Upgrade file <i>in</i> and save as <i>out</i></p>
<dt><code>-d, &#8211;dump</code> <i>in</i></p>
<dd> Dump XML of compressed file <i>in</i> (i.e. MMPZ-file)</p>
<dt><code>-v, &#8211;version</p>
<dd> Show version information and exit.</p>
<dt>-h, &#8211;help</p>
<dd> Show usage information and exit.</dl>
<p> </code></p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://lmms.sf.net/">http://lmms.sf.net/</a></code> <code><a rel="nofollow" href="http://lmms.sf.net/wiki/">http://lmms.sf.net/wiki/</a></code></p>
<h2>AUTHORS</h2>
<p> <code>Tobias</code>Doerffel<code>&lt;tobydox/at/users.sourceforge.net&gt;,</code>Paul<code>Giblock</code>and<code>others.</code>See<code>AUTHORS</code>for<code>details.</code> </p>
<h2>Index</h2>
