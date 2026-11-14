---
title: "twinwave(1)"
name: "twinwave"
section: "1"
letter: "t"
url: "/docs/linux/man/1-twinwave/"
---

<h2>NAME</h2>

 

 twinwave - Wraps multiple GTKWave sessions in one window or two synchronized windows

<h2>SYNTAX</h2>

 

 twinwave &lt;<i>arglist1</i>&gt; &lt;<i>separator</i>&gt; &lt;<i>arglist2</i>&gt;

<h2>DESCRIPTION</h2>

 

 Wraps multiple GTKWave sessions with synchronized markers, horizontal scrolling, and zooming.

<h2>EXAMPLES</h2>

 

 To run this program the standard way type:
<dl>
<dt>twinwave filename1.vcd filename1.sav + filename2.vcd filename2.sav
<dd> Two synchronized viewers are then opened in one window.
<dt>twinwave filename1.vcd filename1.sav ++ filename2.vcd filename2.sav
<dd> Two synchronized viewers are then opened in two windows.</dl>

<h2>LIMITATIONS</h2>

 <i>twinwave</i> uses the GtkSocket/GtkPlug mechanism to embed two <i><a HREF="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) sessions into one window. The amount of coupling is currently limited to communication of temporal information. Other than that, the two gtkwave processes are isolated from each other as if the viewers were spawned separately. Keep in mind that using the same save file for each session may cause unintended behavior problems if the save file is written back to disk: only the session written last will be saved. (i.e., the save file isn't cloned and made unique to each session.) Note that <i>twinwave</i> compiled against Quartz (not X11) on OSX as well as MinGW does not place both sessions in a single window. 

<h2>AUTHORS</h2>

 

 Anthony Bybell &lt;bybell [at] rocketmail.com&gt;

<h2>SEE ALSO</h2>

 

 <i><a HREF="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) 

<h2>Index</h2>


