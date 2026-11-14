---
title: "calf(7)"
name: "calf"
section: "7"
letter: "c"
url: "/docs/linux/man/7-calf/"
description: "calf – a audio plugin library"
---

<p>calf &#8211; a audio plugin library</p>
<h2>Synopsis</h2>
<p>calfjackhost plugin <code>!</code> <i>[</i>&nbsp;<wbr>plugin <code>!</code> <i>]</i> [<i>&#8230;</i>]</p>
<h2>Description</h2>
<p>&nbsp;<wbr>The Calf project aims at providing a set of high quality open source audio plugins for musicians, possibly in many different plugin formats, so that they can be used in as many hosts as possible and in standalone mode. Currently available plugins: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>Flanger with linear interpolation. In case&nbsp;<wbr>&quot;zipper noise&quot;&nbsp;<wbr>of basic flanger effects was driving you mad, use this one!<br />
&nbsp;<wbr>*&nbsp;<wbr>Simple reverb with basic controls and relatively neutral sound. No dreaded metal barrel sound, at expense of higher CPU use and less time density.<br />
&nbsp;<wbr>*&nbsp;<wbr>Multimode filter&nbsp;<wbr>(selectable 12dB/24dB/36dB rolloff, lowpass or highpass)&nbsp;<wbr>with inertia/smoothing for cutoff for more&nbsp;<wbr>&quot;analog&quot;&nbsp;<wbr>sound when tweaking.<br />
&nbsp;<wbr>*&nbsp;<wbr>Vintage delay &#8211; in other words, a very simple simulation of tape echo, with a filter in a feedback loop.<br />
&nbsp;<wbr>*&nbsp;<wbr>Simple monophonic synthesizer with 2 oscillators, multimode filter and an envelope.<br />
&nbsp;<wbr>*&nbsp;<wbr>Optional: electric organ synthesizer and rotary speaker emulation, best used together&nbsp;<wbr>(use&nbsp;<wbr>&quot;configure &#8211;enable-experimental&quot;&nbsp;<wbr>to enable them) The plugins are available in following formats: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>LADSPA&nbsp;<wbr>(all effect plugins)<br />
&nbsp;<wbr>*&nbsp;<wbr>DSSI&nbsp;<wbr>(both synthesizers and effects), including DSSI GUI<br />
&nbsp;<wbr>*&nbsp;<wbr>Standalone JACK client application with GTK+-based GUI&nbsp;<wbr>(new: it is possible to run several plugins simultaneously in one JACK client, and connect them in chains using standard JACK facilities)<br />
&nbsp;<wbr>*&nbsp;<wbr>LV2&nbsp;<wbr>(experimental, SVN only, some features may not work, host support for several features may vary)</p>
<h2>Options</h2>
<dl>
<dt><code>&nbsp;<wbr>How to use Calf plugins:</code></p>
<dd>
<dt><code>&nbsp;<wbr>* LADSPA plugins</code></p>
<dd>Calf is installed as calf.so library in your LADSPA directory (typically /usr/lib/ladspa). It means that typical LADSPA host should be able to find Calf&#8217;s plugins. </p>
<dt><code>&nbsp;<wbr>* DSSI plugins</code></p>
<dd>The calf.so module is also installed in your DSSI plugin directory, which means your DSSI host (like jack-dssi-host or rosegarden) should find it and include its plugins in the plugin list. </p>
<dt><code>&nbsp;<wbr>* JACK client application</code></p>
<dd>You can also use Calf plugins as one or more separate applications, connecting to other applications using JACK Audio Connection Kit (version 0.103 or newer is required). To run the client, type: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>calfjackhost monosynth&nbsp;<wbr>! </p>
<p> (! means &quot;connect&quot;, last &quot;!&quot; means &quot;connect to output&quot;) </p>
<p> Other examples: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>calfjackhost monosynth&nbsp;<wbr>!&nbsp;<wbr>vintagedelay&nbsp;<wbr>!&nbsp;<wbr>flanger&nbsp;<wbr>! </p>
<p> (runs monosynth into vintagedelay and vintagedelay into flanger, then to output) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>calfjackhost&nbsp;<wbr>!&nbsp;<wbr>reverb&nbsp;<wbr>! </p>
<p> (takes signal from system:capture_1 and _2, puts it through reverb, and then sends to system:playback_1 and _2) </p>
</dl>
<h2>Environment</h2>
<p><code>LADSPA_PATH</code> Path to LADSPA plugins.</p>
<h2>Bugs</h2>
<p>LV2 support is in infant stage. Some knobs may still cause clicks/zipper noise. Plugin versions (especially LADSPA) have very poor usability comparing to standalone versions, because of platform limitations. In case of other bugs, please send bug reports to &lt;wdev [at] foltman.com&gt;, they will be fixed in order of importance. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-calfjackhost/">calfjackhost</a>(1) </p>
<h2>Author</h2>
<p>Krzysztof Foltman. Man page by Hermann Meyer, edited by Krzysztof Foltman. </p>
<p> <a rel="nofollow" href="http://calf.sourceforge.net/">http://calf.sourceforge.net/</a></p>
