---
title: "midi2abc(1)"
name: "midi2abc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-midi2abc/"
description: "midi2abc – program to convert MIDI format files to abc notation"
---

<h2>NAME</h2>
<p> <code>midi2abc</code> &#8211; program to convert MIDI format files to abc notation</p>
<h2>SYNOPSIS</h2>
<p> midi2abc -f <i>infile</i> [-xa] [-ga] [-a <i>acbeats</i>] [-m <i>time signature</i>] [-ppu parts per unit] [-aul denominator of unit length] [-gu] [-b <i>bars</i>] [-Q <i>tempo</i>] [-u pulses] [-k <i>key</i>] [-c <i>channel</i>] [-obpl] [-bpl bars] [-bps bars] [-o <i>filename</i>] [-s] [-sr units] [-sum] [-nt] [-splitbars] [-splitvoices] [-midigram] [-mftext] [-nogr] [-title string] [-origin string]</p>
<h2>DESCRIPTION</h2>
<p> <i>midi2abc</i> takes a MIDI format file and converts it to something as close as possible to abc text format. The user then has to add text fields not present in the MIDI header and possibly tidy up the abc note output. </p>
<p> The output of midi2abc is printed to the screen. To save it to a file, use the redirection operator, (e.g. <i>midi2abc -f file.mid &gt; file.abc</i>) or specify the output file using the -o option. </p>
<p> Use only one or none of the options -u -gu, -b and -Q. Midi2abc normally converts the MIDI time units into quantum units normally corresponding to the abc 1/16th note or 1/32nd note. If none of these is present, the program will use the PPQN information in the MIDI header to compute the suitable conversion factor. For most MIDI files on the web, it is recommended to rely on the MIDI header information and not use any of the options other than the formatting options. </p>
<p> The program will extract the time signature infromation from the MIDI file if it is present. Otherwise it will assume 4/4 or you could specify it with -m. option. </p>
<p> If the tune has an anacrusis, you can use either the -ga or -xa option to estimate the its length. Alternatively, you can specify its value using the -a option. The anacrusis is specified in half unit lengths, where the unit length is defined by the L: field. For example if L: 1/8, then a quarter note would be indicated by the value 4, (4 1/16 units).</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-a </code><i>acbeats</i></p>
<dd> where acbeats specifies the anacrusis in half unit lengths.</p>
<dt><code>-xa</code></p>
<dd> extract the anacrusis from file by finding the first strong note</p>
<dt><code>-ga</code></p>
<dd> guess the anacrusis by minimizing the number of ties across bars</p>
<dt><code>-m </code><i>time signature</i></p>
<dd> time signature</p>
<dt><code>-b </code><i>bars</i></p>
<dd> number of bars wanted in output</p>
<dt><code>-Q </code><i>tempo</i></p>
<dd> tempo in quarter-notes per minute</p>
<dt><code>-u </code>pulses</p>
<dd> Allows you to specify directly the number of midi pulses per abc time unit.</p>
<dt><code>-ppu </code>parts per abc unit length</p>
<dd> Normally, the smallest note unit that midi2abc can extract is half the L: unit length.This is called the quantum unit. Thus for L: 1/8, midi2abc can extract 1/16 notes but not 1/32 notes. You can change this by specifying -ppu 4 for example. The number of parts should be a power of 2.</p>
<dt><code>-aul </code>denominator of abc unit length</p>
<dd> Normally midi2abc chooses a unit length of 1/8 or 1/16 depending upon the time signature. For time signatures smaller than 3/4 the L: 1/16 is used and for larger time signatures L: 1/8 is used. You can specify the unit length to be used using this parameter. Thus -aul 32 will cause midi2abc to use a unit length of 1/32 nd note.</p>
<dt><code>-gu</code></p>
<dd> Tells midi2abc to estimate the number of midi pulses per abc time unit from the note duration or spacing in the MIDI file.</p>
<dt><code>-gk</code></p>
<dd> Tells midi2abc to guess the key signature by minimizing the number of accidentals even if the key signature is already specified in the MIDI file. By default the key signature is the one specified in the MIDI file. If it is not specified, then the program guesses the key signature by minimizing accidentals.</p>
<dt><code>-k </code><i>key</i></p>
<dd> key signature: -6 to 6 sharps.</p>
<dt><code>-c </code><i>channel</i></p>
<dd> select only this midi channel.</p>
<dt><code>-f </code><i>infile</i></p>
<dd> input file in midi format</p>
<dt><code>-o </code><i>output file</i></p>
<dd> specifies the output abc file name.</p>
<dt><code>-s</code></p>
<dd> do not discard very short notes.</p>
<dt><code>-sr </code><i>quantum units</i></p>
<dd> do not notate a short rest smaller than the specified size after a note. If the size (in quantum units) is zero, nothing is done. For larger values, the rest is absorbed into the preceding note. In other words, the preceding note is lengthened to include that rest.</p>
<dt><code>-sum</code></p>
<dd> print a short summary of the input midi file.</p>
<dt><code>-nt</code></p>
<dd> do not look for triplets or broken rhythm</p>
<dt><code>-obpl</code></p>
<dd> Print only one bar per line instead of 4. For complex music this improves the readability and avoids some problems with some abc to postscript converters. This option is deprecated.</p>
<dt><code>-nogr</code></p>
<dd> (No note grouping.) Inserts a space between all notes. It makes a less pretty postscript file but it is easier to edit.</p>
<dt><code>-bpl </code>nbars</p>
<dd> Print nbars of music on every line followed by a backslash.</p>
<dt><code>-bps </code>nbars</p>
<dd> When nbars have been printed (including those lines joined by a backslash continuation) go to a new line (with no backslash).</p>
<dt><code>-splitbars</code></p>
<dd> This parameter changes the way midi2abc prints chords composed of notes of unequal length (polyphonic chords). Normally, midi2abc joins the longer notes to the notes in the following chord using ties. A more readable output, can be obtained if the measure is split into separate parts using the &#8216;&amp;&#8217; feature in abc notation. The algorithm for dividing the notes in a polyphonic chord to separate voices (label_splits in midi2abc.c) needs some improvement. I welcome any assistance.</p>
<dt><code>-splitvoices</code></p>
<dd> This parameter like above handles polyphonic chords by splitting an entire voice into multi voices.</p>
<dt><code>-midigram</code></p>
<dd> When this option appears, all other options are ignored and no abc file is produced. Instead a list of all notes in the MIDI file are printed in a fixed format. Each line represents a pair of MIDI note on/off event. The line contains the on/off time of the note, its track number, channel number, midi pitch and midi velocity. The last record indicates the duration of the MIDI file in MIDI pulse units. The output is designed to go into a graphical user interface which will produce a graphical representation (piano roll).</p>
<dt><code>-mftext</code></p>
<dd> When this option appears, all other options are ignored and no abc file is produced. Instead a list of all the MIDI commands are printed. The output is designed to go into a graphical user interface provided by runabc.tcl.</p>
<dt><code>-title </code>string</p>
<dd> Replaces the default title field following T: with the given string.</p>
<dt><code>-origin </code>string</p>
<dd> Adds an O: field with the given string.</dl>
<h3>FEATURES</h3>
<p> * The key is chosen so as to minimize the number of accidentals. Alternatively, the user can specify the key numerically (a positive number is the number of sharps, a negative number is minus the number of flats). </p>
<p> * Note length can be set by specifiying the total number of bars or the tempo of the piece. Alternatively the note length can be read from the file. However, by default it is deduced in a heuristic manner from the inter-note distances. This means that you do not have to use the MIDI clock as a metronome when playing in a tune from a keyboard. </p>
<p> * Barlines are automatically inserted. The user specifies the number of measures in the anacrusis before the first barline and the time signature. </p>
<p> * The program can guess how the length of the anacrusis, either by looking for the first strong note or minimizing the number of notes split by a tie across a barline. </p>
<p> * Where a note extends beyond a bar break, it is split into two tied notes. </p>
<p> * The output has 4 bars per line. </p>
<p> * Enough accidental signs are put in the music to ensure that no pitch errors occur if a barline is added or deleted. </p>
<p> * The program attempts to group notes sensibly in each bar. </p>
<p> * Triplets and broken rhythm (a&gt;b) are supported. </p>
<p> * Chords are identified. </p>
<p> * Text information from the original MIDI file is included as comments. </p>
<p> * The -c option can be used to select only 1 MIDI channel. Events on other channels are ignored.</p>
<h3>LIMITATIONS</h3>
<p> midi2abc does not &#8230; </p>
<p> * Supply tune title, composer or any other field apart from X: , K:, Q:, M: and L: &#8211; these must be added by hand afterwards, though they may have been included in the text of the MIDI file. </p>
<p> * Support duplets, quadruplets, other esoteric features. </p>
<p> * Support mid-tune key or time signature changes. </p>
<p> * Deduce repeats. The output is just the notes in the input file. </p>
<p> * Recover an abc tune as supplied to abc2midi. However, if you want to do this, &quot;midi2abc -xa -f file.mid&quot; comes close.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-abc2ps/">abc2ps</a>(1), <a href="/docs/linux/man/1-abc2midi/">abc2midi</a>(1), <a href="/docs/linux/man/1-abc2abc/">abc2abc</a>(1)</p>
<h2>AUTHOR</h2>
<p> James Allwright &lt;J.R.Allwright [at] westminster.ac.uk&gt;</p>
<h2>SUPPORTED</h2>
<p> Seymour Shlien &lt;seymour.shlien [at] crc.ca&gt;</p>
<h2>VERSION</h2>
<p> This man page describes midi2abc version 2.91 from March 09 2008.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1999 James Allwright </p>
<p> midi2abc is supplied &quot;as is&quot; without any warranty. It is free software and can be used, copied, modified and distributed without fee under the terms of the GNU General Public License. </p>
<h2>Index</h2>
