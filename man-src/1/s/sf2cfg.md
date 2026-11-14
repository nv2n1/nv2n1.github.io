---
title: "sf2cfg(1)"
name: "sf2cfg"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sf2cfg/"
description: "sf2cfg – construct gt cfg files for SoundFonts"
---

<h2>NAME</h2>
<p> sf2cfg &#8211; construct gt cfg files for SoundFonts </p>
<h2>SYNOPSIS</h2>
<p> <code>sf2cfg</code> sffilename [&gt; cfgname] </p>
<h2>DESCRIPTION</h2>
<p> sf2cfg is a utility program which constructs a gt configure file, with a list of instrument patch names by bank, for an AWE SoundFont file. Just give it the name of the SoundFont file, either an old style .sbk font or a .sf1 or .sf2 font. Capture the output in a file, edit it if you want, then edit gt&#8217;s main configure file (timidity.cfg) to refer to the new cfg file by adding, e.g., lines:<br />
 if 0<br />
 source cfgname </p>
<h2>COPYRIGHT</h2>
<p> (derivatively) Copyright (C) 1998 Takashi Iwai</p>
<h2>AUTHORS</h2>
<p> Greg Lee &lt;lee [at] hawaii.edu&gt;<br />
 adapted from a program by Takashi Iwai. </p>
<h2>Index</h2>
