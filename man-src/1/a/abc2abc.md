---
title: "abc2abc(1)"
name: "abc2abc"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abc2abc/"
description: "abc2abc – a simple abc checker/re-formatter/transposer"
---

<h2>NAME</h2>
<p> abc2abc &#8211; a simple abc checker/re-formatter/transposer</p>
<h2>SYNOPSIS</h2>
<p> <code>abc2abc</code> <i>file</i> [ <code>-s</code> ] [ <code>-n</code> ] [ <code>-b</code> ] [ <code>-r</code> ] [ <code>-e</code> ] [ <code>-t </code><i>semitones</i> ] [ <code>-nda</code> ] [ <code>-u</code> ] [ <code>-d</code> ] [ <code>-v</code> ] [ <code>-v</code>] [<code>-nokeys</code>] [ <code>-nokeyf</code>] [ <code>-usekey</code><i>(sharps/flats)</i>] [ <code>-OCC</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>abc2abc</code> is a simple abc checker/re-formatter/transposer. It will check whether the <i>file</i> given on the command line obeys basic abc syntax. </p>
<p> If you want to check an abc tune, it is recommended that you use <code>abc2midi</code> with the <code>-c</code> option. This performs extra checks that <code>abc2abc</code> does not do. </p>
<p> The output of <code>abc2abc</code> goes to standard output. Use redirection to save it to a file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></dt>
<dd> Rework spacing in the file (which affects how notes are beamed together when the music is printed out). This option does not appear to be working correctly.</dd>
<dt><code>-n</code><i> X</i></dt>
<dd> Reformats the abc file with line breaks every <i>X</i> bars.</dd>
<dt><code>-b</code></dt>
<dd> Don&#8217;t do bar checking.</dd>
<dt><code>-r</code></dt>
<dd> Don&#8217;t do repeat checking.</dd>
<dt><code>-e</code></dt>
<dd> Don&#8217;t report errors.</dd>
<dt><code>-t</code><i> n</i></dt>
<dd> Transpose tune by <i>n</i> semitones. This function will also work with K: none or one of -nokeys or -nokeyf. If a voice is assigned to channel 10 (drum channel) using a %%MIDI channel 10 command, then this voice is never transposed.</dd>
<dt><code>-nda</code></dt>
<dd> Convert double accidentals in guitar chord to another chord though strictly not correct.</dd>
<dt><code>-u</code></dt>
<dd> Update notation; the older notation <code>+ +</code> for chords is replaced by <code>[]</code> and <code>s s</code> for slurs is replaced by <code>()</code>.</dd>
<dt><code>-OCC</code></dt>
<dd> Accept the old notation for chord. Normally this is turned off, since it conflicts with abc draft standard version 2.0 for decorations (eg. +crescendo(+).</dd>
<dt><code>-d</code></dt>
<dd> Re-notate the tune with all note lengths doubled. The unit length specified by the L: field command is halved (e.g. L:1/8 to L:1/16).</dd>
<dt><code>-v</code></dt>
<dd> Re-notate the tune with all note lengths halved. The unit length specified by the L: field command is doubled (e.g. L:1/8 to L:1/4).</dd>
<dt><code>-ver</code></dt>
<dd> Prints version number and exits.</dd>
<dt><code>-V</code><i> X</i></dt>
<dd> For multivoiced abc files (i.e. contains V: field commands), only voice <i>X</i> is copied.</dd>
<dt><code>-X</code><i> n</i></dt>
<dd> For a file containing many tunes, the X: reference numbers are renumbered sequentially starting from number <i>n</i>.</dd>
<dt><code>-nokeys</code></dt>
<dd> No key signature will be assumed. Instead, sharps and naturals will be placed wherever they are needed.</dd>
<dt><code>-nokeyf</code></dt>
<dd> No key signature will be assumed. Instead, flats and naturals will be placed wherever they are needed.</dd>
<dt><code>-usekey sf</code></dt>
<dd> This will force abc2abc to output the notes in the key signature keys[sf] where sf specifies the number of flats (-negative) or sharps (+positive) in the key signature. It is a number between -5 and +5 inclusive.</dd></dl>
<p> * Normally abc2abc will convert the deprecated notation for decorations (eg. !ppp!) to the abc version 2.0 draft standard (eg. +ppp+). If you do not wish to change to this standard include the -OCC flag.</p>
<h2>SEE ALSO</h2>
<p> <i>abcmtex</i>(1), <i><a href="/docs/linux/man/1-abc2midi/">abc2midi</a></i>(1), <i><a href="/docs/linux/man/1-midi2abc/">midi2abc</a></i>(1), <i><a href="/docs/linux/man/1-mftext/">mftext</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Anselm Lingnau &lt;lingnau [at] tm.informatik.uni-frankfurt.de&gt; and is now supported by Seymour Shlien &lt;seymour.shlien [at] crc.ca&gt; for the GNU/Linux system.</p>
<h2>VERSION</h2>
<p> This man page describes abc2abc version 1.44 from August 13 2005. </p>
<h2>Index</h2>
