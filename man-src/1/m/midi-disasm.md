---
title: "midi-disasm(1)"
name: "midi-disasm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-midi-disasm/"
description: "midi-disasm – disassemble midi files"
---

<h2>NAME</h2>
<p> midi-disasm &#8211; disassemble midi files</p>
<h2>SYNOPSIS</h2>
<p> <code>midi-disasm</code> [ <code>-d</code> ] [ <code>-s</code> ] [ <code>-q</code> ] [ file ]</p>
<h2>DESCRIPTION</h2>
<p> <i>midi-disasm</i> disassembles a standard <code>midi</code> file into readable/editable text. <i>midi-disasm</i> prefers the file suffix &quot;.mid&quot; &#8212; it will supply it if a file by the name given on the command line cannot be found. Its output is to <i>stdout</i>. </p>
<p> There are the following options for <i>midi-disasm</i>:</p>
<dl>
<dt><code>-d</code></p>
<dd> displays times as deltas from the time of the last midi event. A keyword &quot;DELTA&quot; is placed in the header line in the disassembly.</p>
<dt><code>-s</code></p>
<dd> displays times in seconds and factions instead of midi ticks; the format is &quot;&lt;seconds&gt;.&lt;centiseconds&gt;.&lt;16nths of a centisecond&gt;&quot;.</p>
<dt><code>-q</code></p>
<dd> suppresses note-on and note-off output lines.</dl>
<h2>AUTHORS</h2>
<p> The code for <i>midi-disasm</i> is an elaboration of the program <i>mftext</i> by Tim Thompson, &#8230;twitch!glimmer!tjt, who also wrote the first version of the library functions in midifile.c, which were elaborated for midi file output by M. Czeiszperger.<br />
 The rest is by Greg Lee, lee [at] Hawaii.edu. </p>
<h2>Index</h2>
