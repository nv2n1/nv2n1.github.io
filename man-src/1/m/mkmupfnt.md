---
title: "mkmupfnt(1)"
name: "mkmupfnt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkmupfnt/"
description: "mkmupfnt – create fontfile for overriding Mup fonts"
---

<h2>NAME</h2>
<p> mkmupfnt &#8211; create fontfile for overriding Mup fonts</p>
<h2>SYNOPSIS</h2>
<p> mkmupfnt <i>PostScript_font_name Mup_font_name outfile [file]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>mkmupfnt</code> program creates an <i>outfile</i> that can be used with the Mup &quot;fontfile&quot; statement to override a Mup font. </p>
<p> The <i>PostScript_font_name</i> is the name of the font you want Mup to use. This would be something that could be given as a name to the PostScript <code>findfont</code> procedure. </p>
<p> The <i>Mup_font_name</i> is the name of the Mup font you want to override, either an abbreviated name, like &quot;PR&quot; or a full name, like &quot;palatino rom&quot;. </p>
<p> The <i>outfile</i> is the file that will be generated, which will contain character size and other information, to use with Mup&#8217;s &quot;fontfile&quot; statement. </p>
<p> The final optional <i>file</i> argument is the name of a file that contains PostScript to be placed at the end of the Mup PostScript prolog. This might be useful if you have a font whose implementation PostScript could not find on its own. For example, if you&#8217;ve written your own font implementation, you could put it in the given <i>file</i>. The actual characters produced by the font need not be similar to those in the font being replaced; they could be in some other alphabet, or hieroglyphics or whatever you wish. However, see the CAVEATS section for limitations. </p>
<p> An an example, suppose you want Mup to use the Helvetica-Narrow font rather than the plain Helvetica font. You could use:<br />
 mkmupfnt Helvetica-Narrow HR helvnarr<br />
 to generate a Mup fontfile, then in your Mup program put:<br />
 fontfile &quot;helvnarr&quot;<br />
 Then anything that would normally be printed in Helvetica will come out in Helvetica-Narrow instead.</p>
<h2>FILE FORMAT</h2>
<p> Mup requires a <i>fontfile</i> to be in a fairly rigid format. This section describes the format of the file that is produced by mkmupfnt. The file can contain comment lines, which have a &#8216;#&#8217; in column 1. Otherwise the format is: </p>
<pre>
<code>Mup font name:</code> <i>Mup_font_name</i>
<code>PostScript font name:</code> <i>PostScript_font_name</i>
<code>Size data:</code>
<code>32</code>   <i>width   height   ascent</i>
<code>33</code>   <i>width   height   ascent</i>
        <i>... similar lines for ASCII codes 34-126.
        Dimension are given in 1/1000ths of an inch for a 12-point character.
        All codes must be specified, and they must be in order.</i>
<code>PostScript:</code>
        <i>Zero or more lines of PostScript that will be copied
        exactly as is to the end of the Mup PostScript prolog.</i>
<br>
</pre>
<h2>FILES</h2>
<p> mkmupfnt.ps PostScript program that extracts font size information</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-mup/">mup</a>(1).<br />
 Mup &#8212; Music Publisher User&#8217;s Guide</p>
<h2>CAVEATS</h2>
<p> You must have ghostscript (gs or gs386.exe) in your PATH and it must be built to include the &quot;bit&quot; device. </p>
<p> Mup uses certain fonts for certain things, such as time signatures, octave marks, endings, tuplet numbers, etc. (The fonts used include all the Times fonts and New Century bold, plus Helvetica roman and Helvetica bold for tablature.) If your override one of the fonts used for those things, they will come out in your new font. On the one hand, if you don&#8217;t like Mup&#8217;s choices, this provides you a way to get your own. On the other hand, if you want to change most, but not all uses of a particular font, it may not be possible to do that. </p>
<p> Only the ASCII characters 32-126 can be overridden. The non-ASCII characters can not be overridden. </p>
<p> Mup only allows width values up to 1/2 inch for a 12-point character. This program does not enforce that limitation. </p>
<p> This program has been tested with various Ghostscript fonts, but may not work on just any arbitrary PostScript font. </p>
<h2>Index</h2>
