---
title: "jack_freewheel(1)"
name: "jack_freewheel"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_freewheel/"
description: "jack_freewheel – JACK toolkit client to control freewheeling mode"
---

<h2>NAME</h2>
<p> jack_freewheel &#8211; JACK toolkit client to control freewheeling mode</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_freewheel [y|n]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>jack_freewheel</code> Turns freewheeling mode on (y) or off (n). While in freewheeling mode, the JACK server does not wait in between process() calls, and does not read or write data from/to any audio interface. That results in the JACK graph processing data as fast as possible. Freewheeling makes fast exports to files possible. </p>
<p> There is no useful reason to use this tool other than testing. JACK clients that use freewheeling will turn it on and off themselves. </p>
<h2>Index</h2>
