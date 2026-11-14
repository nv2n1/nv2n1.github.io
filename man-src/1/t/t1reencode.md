---
title: "t1reencode(1)"
name: "t1reencode"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1reencode/"
description: "t1reencode – re-encode a PostScript Type 1 font"
---

<h2 class="name">NAME</h2>
<p> t1reencode &#8211; re-encode a PostScript Type 1 font </p>
<h2>SYNOPSIS</h2>
<p> <code>t1reencode</code> -e ENCODING [OPTIONS&#8230;] <i>font</i> [<i>outputfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>T1reencode</code> changes a PostScript Type~1 font&#8217;s embedded encoding. The re-encoded font is written to the standard output (but see the <code>&#8211;output</code> option). If no input font file is supplied, <code>t1reencode</code> reads a PFA or PFB font from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;encoding</code>=<i>file</i>, <code>-e</code> <i>file</i></p>
<dd> Read the encoding from <i>file</i>, which must contain an encoding in format. Alternatively, <i>file</i> can be one of the following special names, in which case the corresponding standard encoding is used. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Name</code></p>
<dd> <code>Source</code></p>
<dt>StandardEncoding</p>
<dd> Adobe</p>
<dt>ISOLatin1Encoding</p>
<dd> Adobe/ISO (synonym: ISO_8859_1_Encoding)</p>
<dt>ExpertEncoding</p>
<dd> Adobe</p>
<dt>ExpertSubsetEncoding</p>
<dd> Adobe</p>
<dt>SymbolEncoding</p>
<dd> Adobe</p>
<dt>ISOLatin2Encoding</p>
<dd> ISO (synonym: ISO_8859_2_Encoding)</p>
<dt>ISOLatin3Encoding</p>
<dd> ISO (synonym: ISO_8859_3_Encoding)</p>
<dt>ISOLatin4Encoding</p>
<dd> ISO (synonym: ISO_8859_4_Encoding)</p>
<dt>ISOCyrillicEncoding</p>
<dd> ISO (synonym: ISO_8859_5_Encoding)</p>
<dt>ISOGreekEncoding</p>
<dd> ISO (synonym: ISO_8859_7_Encoding)</p>
<dt>ISOLatin5Encoding</p>
<dd> ISO (synonym: ISO_8859_9_Encoding)</p>
<dt>ISOLatin6Encoding</p>
<dd> ISO (synonym: ISO_8859_10_Encoding)</p>
<dt>ISOThaiEncoding</p>
<dd> ISO (synonym: ISO_8859_11_Encoding)</p>
<dt>ISOLatin7Encoding</p>
<dd> ISO (synonym: ISO_8859_13_Encoding)</p>
<dt>ISOLatin8Encoding</p>
<dd> ISO (synonym: ISO_8859_14_Encoding)</p>
<dt>ISOLatin9Encoding</p>
<dd> ISO (synonym: ISO_8859_15_Encoding)</p>
<dt>KOI8REncoding</p>
<dd> &#8211;</dl>
</dl>
<dt><code>&#8211;encoding-text</code>=<i>text</i>, <code>-E</code> <i>text</i></p>
<dd> Use the encoding in the <i>text</i> argument, which must be formatted as a encoding. One of <code>&#8211;encoding</code> and <code>&#8211;encoding-text</code> must be supplied. </p>
<dt><code>&#8211;name</code>=<i>name</i>, <code>-n</code> <i>name</i></p>
<dd> Set the output font&#8217;s PostScript name to <i>name</i>. The default is the input font name followed by the encoding&#8217;s name. </p>
<dt><code>&#8211;full-name</code>=<i>name</i>, <code>-N</code> <i>name</i></p>
<dd> Set the output font&#8217;s FullName to <i>name</i>. The default is the input FullName followed by the encoding&#8217;s name. </p>
<dt><code>&#8211;output</code>=<i>file</i>, <code>-o</code> <i>file</i></p>
<dd> Send output to <i>file</i> instead of standard output. </p>
<dt><code>&#8211;pfb</code>, <code>-b</code></p>
<dd> Output a PFB font. This is the default. </p>
<dt><code>&#8211;pfa</code>, <code>-a</code></p>
<dd> Output a PFA font. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and some short non-warranty information and exit.</dl>
<h2>RETURN VALUES</h2>
<p> <code>T1reencode</code> exits with value 0 if a re-encoded font was successfully generated, and 1 otherwise.</p>
<h2>NOTES</h2>
<p> <code>T1reencode</code> should be used only in special situations. It&#8217;s generally much better to use PostScript commands to re-encode a font; for instance, executing the PostScript commands to generate two differently-encoded versions of a single font will take up much less memory than loading two <code>t1reencode</code>d fonts.</p>
<h2>EXAMPLES</h2>
<p> This command re-encodes Frutiger Roman in the ISO Latin~1 encoding. The new font will have the PostScript name Frutiger-RomanISOLatin1Encoding. </p>
<pre>
    <code>t1reencode</code> <code>-e</code> ISOLatin1Encoding FrutiRom.pfb \
            <code>-o</code> FrutiRomISOL1.pfb
</pre>
<p> This series of commands, which use and as well as <code>t1reencode</code> itself, generate a version of Warnock Pro Regular with old-style figures in the slots for numbers (because of <code>otftotfm</code>&#8216;s <code>-f</code>onum option). The new font will be called WarnockPro-RegularOsF. </p>
<pre>
    <code>otftotfm</code> <code>-f</code>onum WarnockPro-Regular.otf \
            <code>--output-encoding</code> /tmp/osf.enc
    <code>cfftot1</code> WarnockPro-Regular.otf | <code>t1reencode</code> <code>-e</code> /tmp/osf.enc \
            <code>-n</code> WarnockPro-RegularOsF <code>-N</code> &quot;Warnock Pro Regular OsF&quot; \
            <code>-o</code> WarnoProRegOsF.pfb
</pre>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i>,</p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
