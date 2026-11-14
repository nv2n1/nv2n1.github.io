---
title: "gprocessor(1)"
name: "gprocessor"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gprocessor/"
---

<h2>NAME</h2>

 gprocessor - Gnash SWF Processor

<h2>Synopsis</h2>

 <pre>
gprocessor (options)... (file)...
</pre>

<h2>DESCRIPTION</h2>

 Gprocessor is a debugging tool for SWF files, a companion to Gnash. It is most often used for debugging and running testcases, as it is equivalant to running Gnash with no graphic output. This tool is primarily used by Gnash developers, or anyone who wishes to run the Gnash test cases.
<dl>
<dt>-h
<dd> Print usage info.
<dt>-w
<dd> Write a .gsc file with preprocessed info, for each input file.
<dt>-vp
<dd> Be verbose about movie parsing.
<dt>-va
<dd> Be verbose about ActionScript.
<dt>-d [ms]
<dd> Milliseconds delay between advances (0 by default). If '-1' the delay will be computed from the FPS.
<dt>-f [frames]
<dd> Allow the given number of frame advancements. If 0, keep advancing until some other stop condition is encountered (default).
<dt>-r [times]
<dd> Allow the given number of complete runs. If 0, keep looping indefinitely. Default is 1 (end as soon as the last frame is reached). 

</dl>

<h2>Index</h2>


