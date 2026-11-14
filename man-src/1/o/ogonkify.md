---
title: "ogonkify(1)"
name: "ogonkify"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogonkify/"
description: "ogonkify – international support for PostScript"
---

<h2 class="name">NAME</h2>
<p> ogonkify &#8211; international support for PostScript</p>
<h2>SYNOPSIS</h2>
<p> <code>ogonkify</code> [<code>-p</code> <i>procset</i>] [<code>-e</code> <i>encoding</i>] [<code>-r</code> <i>Old=New</i>] [<code>-a</code>] [<code>-c</code>] [<code>-h</code>] [<code>-t</code>] [<code>-A</code>] [<code>-C</code>] [<code>-H</code>] [<code>-T</code>] [<code>-AT</code>] [<code>-CT</code>] [<code>-ATH</code>] [<code>-CTH</code>] [<code>-E</code>] [<code>-N</code>] [<code>-M</code>] [<code>-mp</code>] [<code>-SO</code>] [<code>-AX</code>] [<code>-F</code>] [<code>-RS</code>] [<code>&#8212;</code>] <i>file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ogonkify</code> does various munging of PostScript files related to printing in different languages. Its main use is to filter the output of Netscape, Mosaic and other programs in order to print in languages that don&#8217;t use the standard Western-European encoding (ISO 8859-1). </p>
<h2>SUMMARY USAGE</h2>
<p> Installation instructions are provided in the file INSTALL. Assuming the installation has been correctly completed, save the PostScript output of Netscape or Mosaic to a file, say <code>output.ps</code>. Then print it using</p>
<dl>
<dt>
<dd> % ogonkify -AT -N output.ps | lpr</p>
<dt>in the case of Netscape, or</p>
<dd>
<dt>
<dd> % ogonkify -AT -M output.ps | lpr</p>
<dt>in the case of Mosaic.</p>
<dd></dl>
<p> You may want to change the <code>-AT</code> option to <code>-CT</code> in order to use a high quality Courier font from IBM (at the price of slower printing). </p>
<p> An alternative way to print from Netscape is to set the printing command in the printing dialog box to:</p>
<dl>
<dt>
<dd> ogonkify -AT -N | lpr</p>
<dt>For more details, see the USAGE section below.</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code></p>
<dd> Includes the specified procset in the output file. </p>
<dt><code>-e</code></p>
<dd> Set the encoding of the output. Defaults to <code>L2</code> (ISO 8859-2, a.k.a. ISO Latin-2). Other possible values are <code>L1</code> (ISO 8859-1, a.k.a. ISO Latin-1), <code>L3</code> (ISO 8859-3, a.k.a. ISO Latin-3), <code>L4</code> (ISO 8859-4, a.k.a. ISO Latin-4), <code>L5</code> (ISO 8859-9, a.k.a. ISO Latin-5), <code>L6</code> (ISO 8859-10, a.k.a. ISO Latin-6), <code>L7</code> (ISO 8859-13, a.k.a. ISO Latin-7), <code>L9</code> (ISO 8859-15, a.k.a. ISO Latin-9), <code>CP1250</code> (Microsoft Code Page 1250, a.k.a. CeP), <code>ibmpc</code> (Original IBM-PC encoding), <code>mac</code> (Apple Macintosh encoding) and <code>hp</code> (HP Roman Encoding). </p>
<dt><code>-r</code></p>
<dd> Use the font <i>New</i> in place of <i>Old</i>. Will lead to ugly or unreadable output when the metrics mismatch. </p>
<dt><code>-a</code></p>
<dd> Do the right font remappings for using Courier-Ogonki in place of Courier (the <code>a</code> stands for Adobe Courier). This avoids downloading any fonts to the printer. </p>
<dt><code>-c</code></p>
<dd> Do the right font remappings for using IBM Courier in place of Adobe Courier. </p>
<dt><code>-t</code></p>
<dd> Do the right font remappings for using Times-Roman-Ogonki in place of Times-Roman. </p>
<dt><code>-h</code></p>
<dd> Do the right font remappings for using Helvetica-Ogonki in place of Helvetica. </p>
<dt><code>-A</code></p>
<dd> Like <code>-a</code> but also downloads the Courier-Ogonki fonts. </p>
<dt><code>-C</code></p>
<dd> Like <code>-c</code>, but also downloads the IBM Courier fonts. </p>
<dt><code>-H</code></p>
<dd> Like <code>-h</code>, but also downloads the Helvetica-xxx-Ogonki fonts. </p>
<dt><code>-T</code></p>
<dd> Like <code>-t</code>, but also downloads the Times-xxx-Ogonki fonts. </p>
<dt><code>-CT</code></p>
<dd> Equivalent to <code>-C</code> <code>-T</code>. </p>
<dt><code>-CTH</code></p>
<dd> Equivalent to <code>-C</code> <code>-T </code> <code>-H</code>. </p>
<dt><code>-E</code></p>
<dd> Add the <code>Euro</code> currency sign to all standard fonts (use with <code>-e</code> <code>L9</code>). </p>
<dt><code>-N</code></p>
<dd> Do <code>Netscape </code> processing. </p>
<dt><code>-M</code></p>
<dd> Do <code>Mosaic </code> processing. </p>
<dt><code>-mp</code></p>
<dd> Do <code>mp </code> processing. Will not work with the <code>-A</code> option (use <code>-C</code> instead). </p>
<dt><code>-SO</code></p>
<dd> Do <code>StarOffice</code> processing. </p>
<dt><code>-AX</code></p>
<dd> Do <code>ApplixWare</code> processing. </p>
<dt><code>-F</code></p>
<dd> Do <code>XFig</code> processing. </p>
<dt><code>-RS</code></p>
<dd> Recode standard fonts. This is likely to work with applications that leave fonts in <code>AdobeStandardEncoding</code>, typically applications that do not even support printing even of characters. </p>
<dt><code>&#8212;</code></p>
<dd> End options. </p>
</dl>
<h2>USAGE</h2>
<p> Let us assume that you want to print a WWW page encoded in ISO Latin-2. Netscape stubbornly insists on printing it as ISO Latin-1. By using the File-&gt;Print command, have Netscape send the output to a file, say alamakota.ps. </p>
<p> As <code>ogonkify</code> is configured for ISO Latin-2 by default, passing it the PostScript generated by Netscape will correct the encoding of the fonts. It is enough to do:</p>
<dl>
<dt>
<dd> % ogonkify -N &lt;alamakota.ps | lpr</dl>
<p> However, most printers do not have fonts with the needed characters installed; synthesized fonts will be downloaded and used instead of Courier and Times-Roman with <code>-AT</code>, and a very good Courier font from IBM will be used with: <code>-CT</code>. The command will therefore typically be:</p>
<dl>
<dt>
<dd> % ogonkify -N -AT &lt;alamakota.ps | lpr</dl>
<p> or eventually</p>
<dl>
<dt>
<dd> % ogonkify -N -CT &lt;alamakota.ps | lpr</dl>
<p> Typical usage with other programs is:</p>
<dl>
<dt>
<dd>
<pre>
% ogonkify -M -AT &lt;alamakota.ps | lpr
% ogonkify -mp -AT &lt;alamakota.ps | lpr
% ogonkify -SO -AT &lt;alamakota.ps | lpr
% ogonkify -AX -ATH &lt;alamakota.ps | lpr
% ogonkify -XF -ATH &lt;alamakota.ps | lpr
</pre>
</dl>
<h2>BUGS</h2>
<p> Characters with an `ogonek&#8217; should be constructed differently (for instance, the `ogonek&#8217; used with an `a&#8217; should be differently shaped than the one used with an `e&#8217;.) </p>
<p> It would be better to patch the programs we have the sources to than to post-process the produced PostScript. </p>
<p> The program is written in Perl. </p>
<h2>NOTES</h2>
<p> In order to view the output PostScript with Ghostscript, you might need to run <code>gs</code> with the flag <code>-dNOPLATFONTS</code>, and <code>ghostview</code> with the flag <code>-arguments </code> <code>-dNOPLATFONTS</code>. </p>
<p> Netscape, IBM, Adobe, PostScript, StarOffice, ApplixWare and possibly others are registered trademarks. </p>
<h2>THANKS</h2>
<p> Much of the composite character data have been provided by Primoz Peterlin, H. Turgut Uyar, Ricardas Cepas, Kristof Petrovay and Jan Prikryl. </p>
<p> Jacek Pliszka provided the support for <code>StarOffice</code>. Andrzej Baginski provided the support for <code>ApplixWare</code>. </p>
<p> Markku Rossi wrote <code>genscript</code> and provided many useful encoding vectors with the distribution. </p>
<p> Throughout writing the Postscript code, I used the <code>ghostscript</code> interpreter, by Peter Deutsch. </p>
<p> Larry Wall wrote <code>perl</code>, the syntax and semantics of which are a never ending source of puzzlement. </p>
<h2>AUTHOR</h2>
<p> Juliusz Chroboczek &lt;jec [at] dcs.ed.ac.uk&gt;, with help from loads of people. </p>
<h2>Index</h2>
