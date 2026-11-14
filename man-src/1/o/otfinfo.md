---
title: "otfinfo(1)"
name: "otfinfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otfinfo/"
description: "otfinfo – report information about OpenType fonts"
---

<h2 class="name">NAME</h2>
<p> otfinfo &#8211; report information about OpenType fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>otfinfo</code> [<code>-sfzpvag</code>] [<i>FILE&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Otfinfo</code> reports information about the named OpenType font <i>FILE</i>s (or standard input, if no <i>FILE</i>s are given). Results are printed to standard output. Each line is prefaced with the relevant <i>FILE</i> if more than one <i>FILE</i> was supplied.</p>
<h2>OPTIONS</h2>
<p> With long options, you need type only as many characters as will make the option unique.</p>
<h3>Query options</h3>
<dl>
<dt><code>-s</code>, <code>&#8211;scripts</code></p>
<dd> Print supported scripts and language systems. The scripts are printed one per line, with human-readable descriptions; for example: </p>
<pre>
  cyrl            Cyrillic
  grek            Greek
  latn            Latin
  latn.TUR        Latin/Turkish
</pre>
<dt><code>-f</code>, <code>&#8211;features</code></p>
<dd> Print GSUB and GPOS features supported by the selected script (see the <code>&#8211;script</code> option below). The scripts are printed one per line, with human-readable descriptions; for example: </p>
<pre>
  aalt    Access All Alternates
  c2sc    Small Capitals From Capitals
  case    Case-Sensitive Forms
  cpsp    Capital Spacing
  ...
  zero    Slashed Zero
</pre>
<dt><code>-z</code>, <code>&#8211;optical-size</code></p>
<dd> Print optical size information. For example: </p>
<pre>
  design size 11 pt, size range (8.4 pt, 13 pt], subfamily ID 11, subfamily name Semibold Italic
</pre>
<dt><code>-p</code>, <code>&#8211;postscript-name</code></p>
<dd> Print each font&#8217;s PostScript name. For example: </p>
<pre>
  MinionPro-SemiboldItCapt
</pre>
<dt><code>-a</code>, <code>&#8211;family</code></p>
<dd> Print each font&#8217;s family name. For example: </p>
<pre>
  Minion Pro
</pre>
<dt><code>-v</code>, <code>&#8211;font-version</code></p>
<dd> Print font version information, if available. For example: </p>
<pre>
  OTF 1.013;PS 001.000;Core 1.0.27;makeotf.lib(1.11)
</pre>
<dt><code>-i</code>, <code>&#8211;info</code></p>
<dd> Print each font&#8217;s name, version, designer, vendor, copyright, and license information. For example: </p>
<pre><code>
Family : Minion Pro
             Subfamily : Regular
                             Full name : Minion Pro
                                             PostScript name : MinionPro -
                                                               Regular
                                                                   Version : OTF 1.011;
PS 001.000;
Core 1.0.27;
makeotf.lib1 .3.1 Unique ID : 1.011;
ADBE;
MinionPro - Regular
                Designer : Robert Slimbach
                               Vendor URL : http : // www.adobe.com/type/
                                                   Trademark : Minion is either a registered trademark or
    a trademark of Adobe Systems Incorporated in the United States and / or other countries.Copyright : &amp;#169;
2000 Adobe Systems Incorporated.All Rights Reserved.U.S.Patent Des.337, 604. Other patents pending.License URL : http: // www.adobe.com/type/legal.html
</code></pre>
<dt><code>-g</code>, <code>&#8211;glyphs</code></p>
<dd> Print the name of every glyph in each font, one per line. For example: </p>
<pre>
  .notdef
  space
  exclam
  ...
  ncommaaccent.end
  lje.alt
</pre>
<dt><code>-u</code>, <code>&#8211;unicode</code></p>
<dd> Print each Unicode code point supported by the font, followed by the glyph number representing that code point (and, if present, the name of the corresponding glyph). </p>
<dt><code>-t</code>, <code>&#8211;tables</code></p>
<dd> Print the size and name of every OpenType table in the font. For example: </p>
<pre>
       52 BASE
    87723 CFF
     4940 DSIG
    21366 GPOS
  ...
</pre>
<dt><code>-T</code> <i>table</i>, <code>&#8211;dump-table=</code><i>table</i></p>
<dd> Print the contents of the font&#8217;s OpenType table <i>table</i>.</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt><code>&#8211;script=</code><i>script</i>[.<i>lang</i>]</p>
<dd> Select the script system <i>script</i> and language system <i>lang</i> used to look up features by <code>&#8211;features</code>. Examples include &quot;latn&quot; (Latin script), &quot;grek&quot; (Greek script), and &quot;yi.YIC&quot; (Yi script with classic characters). If <i>lang</i> is not specified, otfinfo will use the default language system for that script. Defaults to &quot;latn&quot;. </p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Write progress messages to standard error. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not generate any error messages. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <i>OpenType Specification</i>, Version 1.4</p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
