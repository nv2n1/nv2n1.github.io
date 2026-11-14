---
title: "gsdj500(1)"
name: "gsdj500"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsdj500/"
description: "gslp – Format and print text using ghostscript gsbj – Format and print text for BubbleJet printer using ghostscript gsdj – Format and print text for DeskJet printer using ghostscript gsdj500 – Form..."
---

<h2 class="name">NAME</h2>
<p> gslp &#8211; Format and print text using ghostscript<br />
 gsbj &#8211; Format and print text for BubbleJet printer using ghostscript<br />
 gsdj &#8211; Format and print text for DeskJet printer using ghostscript<br />
 gsdj500 &#8211; Format and print text for DeskJet 500 BubbleJet using ghostscript<br />
 gslj &#8211; Format and print text for LaserJet printer using ghostscript </p>
<h2>SYNOPSIS</h2>
<p> <code>gslp -12BclqRr -b&lt;header&gt; -f&lt;font&gt; -F&lt;hfont&gt; -L&lt;lines&gt; -p&lt;outfile&gt; -T&lt;n&gt; &#8211;add-to-space&nbsp;&lt;units&gt; &#8211;add-to-width&nbsp;&lt;units&gt; &#8211;columns&nbsp;&lt;n&gt; &#8211;detect &#8211;first-page&nbsp;&lt;n&gt; &#8211;kern&nbsp;&lt;file.afm&gt; &#8211;last-page&nbsp;&lt;n&gt; &#8211;(heading|footing)-(left|center|right)&nbsp;&lt;string&gt; &#8211;margin-(top|bottom|left|right)&nbsp;&lt;inches&gt; &#8211;no-eject-(file|formfeed) &#8211;spacing&nbsp;&lt;n&gt; [gs options] [files]<br />
 gsbj</code> [options] [files]<br />
 <code>gsdj</code> [options] [files]<br />
 <code>gsdj500</code> [options] [files]<br />
 <code>gslj</code> [options] [files]</p>
<h2>DESCRIPTION</h2>
<p> This utility provides functionality approximately equivalent to the Unix <code><a href="/docs/linux/man/1-enscript/">enscript</a></code>(1) program. It prints plain text files using a single font. It currently handles tabs and formfeeds, but not backspaces. It will line-wrap when using fixed-pitch fonts. It will also do kerning and width adjustment. </p>
<p> The default device (-sDEVICE=) and resolution (-r) are as follows: </p>
<pre>
      gslp      epson      180
      gsbj      bj10e      180
      gsdj      deskjet    300
      gsdj500   djet500    300
      gslj      laserjet   300
</pre>
<p> By default the current date is formatted as the center header.</p>
<h2>OPTIONS</h2>
<dl>
<dt>Standard switches implemented:</p>
<dd> -12BclqRr -b&lt;header&gt; -f&lt;font&gt; -F&lt;hfont&gt; -L&lt;lines&gt; -p&lt;outfile&gt;</p>
<dt>Sun switches implemented:</p>
<dd> -T&lt;n&gt;<tt>&nbsp;<wbr>&nbsp;</tt>set tab width</p>
<dt>Switches ignored:</p>
<dd> -GghKkmow -# -C -d -J -n -P -S -s -t -v</p>
<dt>Switches added:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;add-to-space &lt;units&gt;</p>
<dd> add the given number of 1/72&quot; units to the width of each space (may be negative)</p>
<dt>&#8211;add-to-width &lt;units&gt;</p>
<dd> add the given number of 1/72&quot; units to the width of each character (may be negative)</p>
<dt>&#8211;columns &lt;n&gt;</p>
<dd> print in &lt;n&gt; columns</p>
<dt>&#8211;detect</p>
<dd> treat the file as PostScript if it starts with %!</p>
<dt>&#8211;first-page &lt;n&gt;</p>
<dd> start printing at page &lt;n&gt;</p>
<dt>&#8211;kern &lt;file.afm&gt;</p>
<dd> kern using information from the given .AFM file</p>
<dt>&#8211;last-page &lt;n&gt;</p>
<dd> stop printing after page &lt;n&gt;</p>
<dt>&#8211;(heading|footing)-(left|center|right) &lt;string&gt;</p>
<dd> set the heading/footing fields; use -B first to clear</p>
<dt>&#8211;margin-(top|bottom|left|right) &lt;inches&gt;</p>
<dd> set a margin</p>
<dt>&#8211;no-eject-(file|formfeed)</p>
<dd> end-of-file/FF only starts a new column, not a new sheet</p>
<dt>&#8211;spacing &lt;n&gt;</p>
<dd> use double (n=2), triple (n=3), etc. spacing</dl>
</dl>
<p> Also, the string %# in a heading or footing is replaced with the page #.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1)</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. This manpage by George Ferguson. </p>
<h2>Index</h2>
