---
title: "jack_metro(1)"
name: "jack_metro"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_metro/"
description: "jack_metro – JACK toolkit metronome"
---

<h2>NAME</h2>
<p> jack_metro &#8211; JACK toolkit metronome</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_metro</code> [ <i>-n</i> name ] [ <i>-f</i> hz ] [ <i>-D</i> msecs ] [<i>-a</i> % ] [ <i>-d</i> % ] <i>-b</i> bpm</p>
<h2>DESCRIPTION</h2>
<p> <code>jack_metro</code> is a simple metronome for JACK. It generates a synthetic &quot;tick&quot; sound for every beat. Note that is does <code>not</code> connect its output port by default &#8211; to hear the sound it makes you must connect them using some other tool.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;name</code></p>
<dd>
 Specify a name for this instance of the metronome.</p>
<dt><code>-f</code>, <code>&#8211;frequency</code> Hz</p>
<dd>
 Define the frequency of the &quot;tick&quot; in Hz.</p>
<dt><code>-D</code>, <code>&#8211;duration</code> msecs</p>
<dd>
 Define the duration of the &quot;tick&quot; in milliseconds.</p>
<dt><code>-a</code>, <code>&#8211;attack</code> %-age</p>
<dd>
 Define the duration of the attack phase of the &quot;tick&quot; as a percentage of the duration.</p>
<dt><code>-d</code>, <code>&#8211;decay</code> %-age</p>
<dd>
 Define the duration of the decay phase of the &quot;tick&quot; as a percentage of the duration.</p>
<dt><code>&#8211;b</code>, <code>&#8211;bpm</code> bpm</p>
<dd>
 Define the number of beats per minute.</dl>
<h2>AUTHOR</h2>
<p> Anthony Van Groningen </p>
<h2>Index</h2>
