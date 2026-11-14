---
title: "yaps(1)"
name: "yaps"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yaps/"
description: "YAPS – converts an abc file to a PostScript file"
---

<h2>NAME</h2>
<p> <code>YAPS</code> &#8211; converts an abc file to a PostScript file</p>
<h2>SYNOPSIS</h2>
<p> yaps abc file [-d] [-e&nbsp;<wbr>&lt;list&gt;] [-E] [-l] [-M XXXxYYY] [-N] [-k nn] [-o file name] [-P -ss] [-s XX] [-V][-ver] [-x] [-OCC] </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> For debugging only. Displays the internal data structures used in the program.</p>
<dt><code>-e </code>&lt;list&gt;</p>
<dd> Draws tunes with reference numbers in a comma separated list. Spaces are not allowed but a range of reference numbers can be specified. For example, 1,3,7-10.</p>
<dt><code>-E</code></p>
<dd> Generates Encapsulated Postscript output.</p>
<dt><code>-M </code>XXXxYYY</p>
<dd> Set margin sizes in points where 28.3 points = 1cm and 72 points = 1 inch.</p>
<dt><code>-N</code></p>
<dd> Adds page numbering.</p>
<dt><code>-k [nn]</code></p>
<dd> Adds bar numbering. If number nn is included, then every nn&#8217;th bar is numbered. Otherwise all bars are numbered.</p>
<dt><code>-o </code>filename</p>
<dd> Specifies the output postscript file name.</p>
<dt><code>-P </code>ss</p>
<dd> Specifies the paper size where 0 is A4 and 1 is US Letter or XXXxYYY sets the paper size in point units.<br />
&nbsp;<wbr>units.</p>
<dt><code>-s </code>XX</p>
<dd> Specifies the scaling factor (default is 0.7)</p>
<dt><code>-V</code></p>
<dd> Voices are printed out seperately for a multi-voice tune. Otherwise they are interleaved.</p>
<dt><code>-ver</code></p>
<dd> Prints version number and exits.</p>
<dt><code>-x</code></p>
<dd> Print tune number in X: field</p>
<dt><code>-OCC</code></p>
<dd> Required if the tune uses the old convention for chords delineated with +..+ instead of [&#8230;]. </p>
</dl>
<h2>FEATURES</h2>
<p> * Uses the abc2midi parsing code, so hopefully compatibility with abc2midi will be good. </p>
<p> * Measures the width of lyric text for lyric typesetting. </p>
<p> * Uses dynamically extensible data structures in most places, so you should not be restricted by compiled-in limits. </p>
<p> * Multiple voices drawn with notes played at the same time aligned. </p>
<p> * Supports special characters using ISO latin 1 font. Special characters are created with a TeX-like code e.g. &#8216;E or a 3 digit octal code e.g. 315 . </p>
<p> * Supports the following clefs : baritone, tenor, alto, mezzo, soprano, treble, bass. Recommended use is </p>
<p> * Invisible rests (x) are displayed like normal rests. </p>
<p> * Nonnumeric voice id&#8217;s, eg. V: soprano are accepted. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>I:clef=bass </p>
<p> To make it easier to enter tunes in clefs othan than treble clef, yaps supports I:octave=-1 to indicate that a C in the tune represents the note one octave below the pitch defined in the abc standard. These may be combined in one I: statement e.g. </p>
<p> I:clef=bass octave=-2 </p>
<p> You can also use clefs that are one, two or three octaves higher or lower than normal using e.g. treble-8, treble+15, treble-22. The clef is drawn with a small 8, 15 or 22 above or below the clef symbol. The clef= and octave= commands may also go in the K: field e.g. </p>
<p> K:G clef=bass-8 octave=-3 </p>
<p> Note that there is an incompatibility between the behaviour of yaps and the behaviour of abc2ps 1.3.3. abc2ps 1.3.3 does not support the I:octave=N command, but selecting certain clefs causes it to automatically transpose by several octaves. You can produce abc that works for both by following the clef change with an I:octave=N command to do the transpose that abc2ps does automatically. </p>
<p> * Produces boxed part labels. </p>
<p> * Supports the segno symbol with !segno! and coda with !coda! . Other musical instructions such as !fine! and !D.C.! come out as text. * Supports the U: field for abbreviating symbols to single characters. e.g. </p>
<p> U:S = !segno! </p>
<p> allows S to be used to produce the segno symbol. Currently this only allows new symbols to be defined and does not allow the existing pre-defined symbols M,L,R,H and T to be altered. </p>
<p> * Supports the !red! and !black! instructions for switching from black to red or vice-versa. </p>
<p> * Supports the following abc2ps extensions to abc : </p>
<p>%%newpage&nbsp;<wbr>&nbsp;<wbr>&#8211; start a new page, </p>
<p>%%vskip N&nbsp;<wbr>&nbsp;<wbr>&#8211; adds vertical space of N points. If N is followed by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;cm&#8217;&nbsp;<wbr>or&nbsp;<wbr>&#8216;in&#8217;&nbsp;<wbr>the units are taken as centimetres or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>inches instead of points e.g. 4cm. </p>
<p>%%text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; print text </p>
<p>%%centre&nbsp;<wbr>(or&nbsp;<wbr>%%center for Americans)&nbsp;<wbr>&#8211; print centred text. </p>
<p>If&nbsp;<wbr>%%text or&nbsp;<wbr>%%centre appear in the header, the text appears above<br />
the tune. </p>
<p>%%staffsep SIZE &#8211; set the vertical blank space between 2 consecutive<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>music staves. </p>
<p>%%titleleft N &#8211; select title placed to the left or centred. N&nbsp;<wbr>=&nbsp;<wbr>1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>places the title on the left while N&nbsp;<wbr>=&nbsp;<wbr>0 centres it. </p>
<p>%%titlecaps &#8211; title is displayed in upper case&nbsp;<wbr>(capital)&nbsp;<wbr>letters. </p>
<p>%%textfont NAME SIZE &#8211; select font called NAME and point size SIZE<br />
for text produced by&nbsp;<wbr>%%text or&nbsp;<wbr>%%centre. If only NAME is given, the<br />
font stays the same size. Likewise, if&nbsp;<wbr>&#8216;-&#8216;&nbsp;<wbr>is given as the NAME,<br />
only the font size changes. </p>
<p>%%titlefont NAME SIZE &#8211; select font for title. </p>
<p>%%subtitlefont NAME SIZE &#8211; select font for titles after the first<br />
title. </p>
<p>%%composerfont NAME SIZE &#8211; select font for words in C: and O: fields<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and part specifier&nbsp;<wbr>(P: in header). </p>
<p>%%wordsfont NAME SIZE &#8211; select font for words in W: fields. </p>
<p>%%partsfont NAME SIZE &#8211; select font for boxed parts and<br />
!instruction!&nbsp;<wbr>. </p>
<p>%%vocalfont NAME SIZE &#8211; select font for words in w: fields. </p>
<p>%%gchordfont NAME SIZE &#8211; select font for guitar chords in the music.<br />
(It is advisable not to change the font name for the last two, since<br />
&nbsp;<wbr>the program calculates the width of strings using default fonts) </p>
<p>%%titlespace,&nbsp;<wbr>%%subtitlespace,&nbsp;<wbr>%%textspace,&nbsp;<wbr>%%composerspace,<br />
%%wordsspace,&nbsp;<wbr>%%partsspace,&nbsp;<wbr>%%vocalspace and&nbsp;<wbr>%%gchordspace<br />
determine the amount of space left above the relevant type&nbsp;<wbr><br />
of text. Each of these should be followed by a size in points<br />
or value in centrimetres or inches. </p>
<p>e.g.&nbsp;<wbr>%%composerfont 3<br />
&nbsp;<wbr>&nbsp;<wbr>%%titlefont 2cm </p>
<p> * Supports placing of accompaniment chords either above or below the<br />
&nbsp;<wbr>&nbsp;<wbr>stave. </p>
<p>%%chordsabove &#8211; places accompaniment chords above the stave<br />
(default). </p>
<p>%%chordsbelow &#8211; places accompaniment chords below the stave. </p>
<p> * Supports optional text enclosed in quotes before and after the<br />
&nbsp;<wbr>&nbsp;<wbr>tempo specification in the Q: field. This extension comes from<br />
&nbsp;<wbr>&nbsp;<wbr>abc2ps. </p>
<h2>AUTHOR</h2>
<p> James Allwright &lt;J.R.Allwright [at] westminster.ac.uk&gt;</p>
<h2>SUPPORTED</h2>
<p> Seymour Shlien &lt;seymour.shlien [at] crc.ca&gt; </p>
<p> More complete documentation can be found in abcguide.txt which comes with the abcMIDI distribution package.</p>
<h2>VERSION</h2>
<p> This man page describes version 1.39 August 13 2005. </p>
<h2>Index</h2>
