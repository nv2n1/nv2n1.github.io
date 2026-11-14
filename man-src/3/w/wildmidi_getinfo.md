---
title: "wildmidi_getinfo(3)"
name: "wildmidi_getinfo"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wildmidi_getinfo/"
description: "WildMidi_GetInfo – get information on a midi"
---

<p>WildMidi_GetInfo &#8211; get information on a midi</p>
<h2>Library</h2>
<p><code>libWildMidi</code></p>
<h2>Synopsis</h2>
<p><code>#include &lt;wildmidi_lib.h&gt;</code> </p>
<p> <code>struct _WM_Info *WildMidi_GetInfo (midi *</code><i>handle</i>); </p>
<h2>Description</h2>
<p>Obtains information allowing you to determine song position, current options, and any copyright information. </p>
<dl COMPACT>
<dt><i>handle</i></p>
<dd>The identifier obtained from opening a midi file with <code><a href="/docs/linux/man/3-wildmidi_open/">WildMidi_Open</a></code>(3) or <code><a href="/docs/linux/man/3-wildmidi_openbuffer/">WildMidi_OpenBuffer</a></code>(3)</dl>
<h2>Return Value</h2>
<p>On error returns NULL with an error message displayed to stderr. </p>
<p> Otherwise returns a pointer to a struct containing the information. </p>
<pre>struct _WM_Info {
 char *<i>copyright</i>;
 unsigned long int <i>current_sample</i>;
 unsigned long int <i>approx_total_samples</i>;
 unsigned long int <i>total_midi_time</i>;
 unsigned short int <i>mixer_options</i>;
 unsigned long int <i>total_midi_time</i>;
};</pre>
<dl COMPACT>
<dt><i>copyright</i></p>
<dd>A pointer to a 
