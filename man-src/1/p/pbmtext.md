---
title: "pbmtext(1)"
name: "pbmtext"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtext/"
description: "pbmtext – render text into a bitmap"
---

<h2 class="name">NAME</h2>
<p> pbmtext &#8211; render text into a bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtext</code> [<code>-font</code> <i>fontfile</i>] [<code>-builtin</code> <i>fontname</i>] [<code>-space</code> <i>pixels</i>] [<code>-lspace</code> <i>pixels</i>] [<i>text</i>] </p>
<h2>DESCRIPTION</h2>
<p> Takes the specified text, either a single line from the command line or multiple lines from standard input, and renders it into a bitmap. </p>
<p> In the bitmap, each line of input is a line of output. Formatting characters such as newline have no effect on the formatting; like any unprintable character, they turn into spaces. </p>
<p> The bitmap is just wide enough for the longest line of text, plus margins, and just high enough to contain the lines of text, plus margins. The left and right margins are twice the width of the widest character in the font; the top and bottom margins are the height of the tallest character in the font. But if the text is only one line, all the margins are half of this. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-font</code>,<code>-builtin</code></p>
<dd> By default, pbmtext uses a built-in font called bdf (about a 10 point Times-Roman font). You can use a fixed width font by specifying <code>-builtin fixed</code>. </p>
<p> You can also specify your own font with the <code>-font</code> flag. The <i>fontfile</i> is either a BDF file from the X window system or a PBM file. </p>
<p> If the <i>fontfile</i> is a PBM file, it is created in a very specific way. In your window system of choice, display the following text in the desired (fixed-width) font: </p>
<pre><code>
M ",/^_[`jpqy| M
        / !"#$%&amp;'()*+ /
    &lt;
    , -./ 01234567 &lt;
          &gt; 89:;
&lt;=&gt; ? @ABC &gt;
          @DEFGHIJKLMNO @_ PQRSTUVWXYZ[_ { \]^_`abcdefg {
    } hijklmnopqrs } ~tuvwxyz { | } ~~M ",/^_[`jpqy| M
</code></pre>
<p> Do a screen grab or window dump of that text, using for instance <code>xwd</code>, <code>xgrabsc</code>, or <code>screendump</code>. Convert the result into a pbm file. If necessary, use <code>pnmcut</code> to remove everything except the text. Finally, run it through <code>pnmcrop</code> to make sure the edges are right up against the text. <code>pbmtext</code> can figure out the sizes and spacings from that. </p>
<dt><code>-space </code><i>pixels</i></p>
<dd> Add <i>pixels</i> pixels of space between characters. This is in addition to whatever space surrounding characters is built into the font, which is usually enough to produce a reasonable string of text. </p>
<p> <i>pixels</i> may be negative to crowd text together, but the author has not put much thought or testing into how this works in every possible case, so it might cause disastrous results. </p>
<dt>-B -lspace <i>pixels</p>
<dd> Add pixels</i> pixels of space between lines. This is in addition to whatever space above and below characters is built into the font, which is usually enough to produce a reasonable line spacing. </p>
<p> <i>pixels</i> must be a whole number. </p>
<p> <i>pixels</i> may be negative to crowd lines together, but the author has not put much thought or testing into how this works in every possible case, so it might cause disastrous results. </p>
</dl>
<h2>USAGE</h2>
<p> Often, you want to place text over another image. One way to do this is with <code>ppmlabel</code>. <code>ppmlabel</code> does not give you the font options that <code>pbmtext </code> does, though. </p>
<p> Another way is to use <code>pbmtext</code> to create an image containing the text, then use <code>pnmcomp</code> to overlay the text image onto your base image. To make only the text (and not the entire rectangle containing it) cover the base image, you will need to give <code>pnmcomp</code> a mask, via its <code>-alpha</code> option. You can just use the text image itself as the mask, as long as you also specify the <code>-invert</code> option to <code>pnmcomp</code>. </p>
<p> If you want to overlay colored text instead of black, just use <code>ppmchange</code> to change all black pixels to the color of your choice before overlaying the text image. But still use the original black and white image for the alpha mask. </p>
<p> If you want the text at an angle, use <code>pnmrotate</code> on the text image (and alpha mask) before overlaying. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1), <code><a href="/docs/linux/man/1-pnmcrop/">pnmcrop</a></code>(1), <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/1-ppmchange/">ppmchange</a></code>(1), <code><a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a></code>(1), <code><a href="/docs/linux/man/1-pbmtextps/">pbmtextps</a></code>(1), <code><a href="/docs/linux/man/1-ppmlabel/">ppmlabel</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1993 by Jef Poskanzer and George Phillips </p>
<h2>Index</h2>
