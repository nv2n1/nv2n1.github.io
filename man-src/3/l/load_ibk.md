---
title: "load_ibk(3)"
name: "load_ibk"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_ibk/"
description: "load_ibk – Reads in a .IBK patch definition file for the Adlib driver. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_ibk &#8211; Reads in a .IBK patch definition file for the Adlib driver. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int load_ibk(char *filename, int drums);</code></p>
<h2>DESCRIPTION</h2>
<p> Reads in a .IBK patch definition file for use by the Adlib driver. If drums is set, it will load it as a percussion patch set, otherwise it will use it as a replacement set of General MIDI instruments. You may call this before or after initialising the sound code, or can simply set the ibk_file and ibk_drum_file variables in the configuration file to have the data loaded automatically. Note that this function has no effect on any drivers other than the Adlib one!</p>
<h2>RETURN VALUE</h2>
<p> Returns non-zero on error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3) </p>
<h2>Index</h2>
