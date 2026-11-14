---
title: "calfjackhost(1)"
name: "calfjackhost"
section: "1"
letter: "c"
url: "/docs/linux/man/1-calfjackhost/"
description: "calfjackhost – JACK wrapper for Calf plugins"
---

<h2>NAME</h2>
<p> calfjackhost &#8211; JACK wrapper for Calf plugins</p>
<h2>SYNOPSIS</h2>
<p> <code>calfjackhost [</code><i>options</i>] <i>plugin[:preset]</i> [<code>!</code>] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Calf JACK host application provides a way to use Calf plugins directly, without need for any external host application. It also offers best GUI functionality (using GTK+ 2 widget set), as there is no restrictive plugin standard getting in a way between GUI and audio processing code. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;client</code> <i>name</i></p>
<dd> sets JACK client name (the name calfjackhost uses when registering in JACK)</p>
<dt><code>&#8211;input</code> <i>name</i></p>
<dd> name prefix for audio inputs</p>
<dt><code>&#8211;output</code> <i>name</i></p>
<dd> name prefix for audio outputs</p>
<dt><code>&#8211;midi</code> <i>name</i></p>
<dd> name prefix for MIDI inputs</p>
<dt><code>&#8211;connect-midi</code> <i>client:port</i></p>
<dd> automatically connect all MIDI ports to <i>client:port</i></p>
<dt><code>&#8211;connect-midi</code> <code>!</code><i>n</i></p>
<dd> automatically connect all MIDI ports to <code>system:midi_capture_</code><i>n</i></p>
<dt><code>&#8211;version</code></p>
<dd> prints a version string (calf some.version.number)</p>
<dt><code>&#8211;help</code></p>
<dd> prints a help text</dl>
<p> An exclamation mark (!) in place of plugin name means automatic connection. If &quot;!&quot; is placed before the first plugin name, the first plugin has its inputs connected to <code>system:capture_1</code> and <code>system:capture_2</code>. If it&#8217;s placed between plugin names, those plugins are connected together (first plugin&#8217;s output is connected to second plugin&#8217;s input). If it&#8217;s placed after last plugin name, that plugin&#8217;s audio outputs are connected to <code>system:playback_1</code> and <code>system:playback_2</code> (first output pair). </p>
<p> Plugin names (should be self-explanatory):<br />
&nbsp;<wbr>*&nbsp;<wbr>flanger<br />
&nbsp;<wbr>*&nbsp;<wbr>filter<br />
&nbsp;<wbr>*&nbsp;<wbr>reverb<br />
&nbsp;<wbr>*&nbsp;<wbr>vintagedelay<br />
&nbsp;<wbr>*&nbsp;<wbr>monosynth<br />
&nbsp;<wbr>*&nbsp;<wbr>multichorus&nbsp;<wbr>(chorus effect with multiple voices)<br />
&nbsp;<wbr>*&nbsp;<wbr>compressor&nbsp;<wbr>(Thor Harald Johansen&#8217;s dynamic compressor)<br />
&nbsp;<wbr>*&nbsp;<wbr>organ&nbsp;<wbr>(polyphonic synthesizer emulating tonewheel or solid state organs)<br />
&nbsp;<wbr>*&nbsp;<wbr>rotaryspeaker&nbsp;<wbr>(not a faithful emulation, not even close) </p>
<h2>BUGS</h2>
<p> Please send bug reports to &lt;wdev [at] foltman.com&gt;. </p>
<h2>EXAMPLES</h2>
<p> To start monosynth with automatic connection to first system audio output, and no automatic MIDI connection, use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>calfjackhost monosynth&nbsp;<wbr>! </p>
<p> (! means &quot;connect&quot;, last &quot;!&quot; means &quot;connect to output&quot;) </p>
<p> Other examples: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>calfjackhost monosynth&nbsp;<wbr>!&nbsp;<wbr>vintagedelay&nbsp;<wbr>!&nbsp;<wbr>flanger&nbsp;<wbr>!&nbsp;<wbr>-M 2 </p>
<p> (runs monosynth into vintagedelay and vintagedelay into flanger, then to output; connects monosynth&#8217;s MIDI input to JACK&#8217;s system:midi_capture_2) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>calfjackhost&nbsp;<wbr>&quot;monosynth:Fat Bass&quot; </p>
<p> (runs monosynth with a Fat Bass preset into monosynth, does not autoconnect) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>calfjackhost&nbsp;<wbr>!&nbsp;<wbr>reverb&nbsp;<wbr>! </p>
<p> (takes signal from system:capture_1 and _2, puts it through reverb, and then sends to system:playback_1 and _2) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-calf/">calf</a>(7) </p>
<h2>Index</h2>
