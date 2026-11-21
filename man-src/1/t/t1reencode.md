---

title: "t1reencode(1)"
name: "t1reencode"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1reencode/"
description: "t1reencode – re-encode a PostScript Type 1 font"
---

<p> <code>t1reencode</code> -e ENCODING [OPTIONS&#8230;] <i>font</i> [<i>outputfile</i>]</p>
<p> <code>T1reencode</code> changes a PostScript Type~1 font&#8217;s embedded encoding. The re-encoded font is written to the standard output (but see the <code>&#8211;output</code> option). If no input font file is supplied, <code>t1reencode</code> reads a PFA or PFB font from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;encoding</code>=<i>file</i>, <code>-e</code> <i>file</i></dt>
<dd> Read the encoding from <i>file</i>, which must contain an encoding in format. Alternatively, <i>file</i> can be one of the following special names, in which case the corresponding standard encoding is used. </dd>
<dl>
<dl>
<dt><code>Name</code></dt>
<dd> <code>Source</code></dd>
<dt>StandardEncoding</dt>
<dd> Adobe</dd>
<dt>ISOLatin1Encoding</dt>
<dd> Adobe/ISO (synonym: ISO_8859_1_Encoding)</dd>
<dt>ExpertEncoding</dt>
<dd> Adobe</dd>
<dt>ExpertSubsetEncoding</dt>
<dd> Adobe</dd>
<dt>SymbolEncoding</dt>
<dd> Adobe</dd>
<dt>ISOLatin2Encoding</dt>
<dd> ISO (synonym: ISO_8859_2_Encoding)</dd>
<dt>ISOLatin3Encoding</dt>
<dd> ISO (synonym: ISO_8859_3_Encoding)</dd>
<dt>ISOLatin4Encoding</dt>
<dd> ISO (synonym: ISO_8859_4_Encoding)</dd>
<dt>ISOCyrillicEncoding</dt>
<dd> ISO (synonym: ISO_8859_5_Encoding)</dd>
<dt>ISOGreekEncoding</dt>
<dd> ISO (synonym: ISO_8859_7_Encoding)</dd>
<dt>ISOLatin5Encoding</dt>
<dd> ISO (synonym: ISO_8859_9_Encoding)</dd>
<dt>ISOLatin6Encoding</dt>
<dd> ISO (synonym: ISO_8859_10_Encoding)</dd>
<dt>ISOThaiEncoding</dt>
<dd> ISO (synonym: ISO_8859_11_Encoding)</dd>
<dt>ISOLatin7Encoding</dt>
<dd> ISO (synonym: ISO_8859_13_Encoding)</dd>
<dt>ISOLatin8Encoding</dt>
<dd> ISO (synonym: ISO_8859_14_Encoding)</dd>
<dt>ISOLatin9Encoding</dt>
<dd> ISO (synonym: ISO_8859_15_Encoding)</dd>
<dt>KOI8REncoding</dt>
<dd> &#8211;</dd></dl>
</dl>
<dt><code>&#8211;encoding-text</code>=<i>text</i>, <code>-E</code> <i>text</i></dt>
<dd> Use the encoding in the <i>text</i> argument, which must be formatted as a encoding. One of <code>&#8211;encoding</code> and <code>&#8211;encoding-text</code> must be supplied. </dd>
<dt><code>&#8211;name</code>=<i>name</i>, <code>-n</code> <i>name</i></dt>
<dd> Set the output font&#8217;s PostScript name to <i>name</i>. The default is the input font name followed by the encoding&#8217;s name. </dd>
<dt><code>&#8211;full-name</code>=<i>name</i>, <code>-N</code> <i>name</i></dt>
<dd> Set the output font&#8217;s FullName to <i>name</i>. The default is the input FullName followed by the encoding&#8217;s name. </dd>
<dt><code>&#8211;output</code>=<i>file</i>, <code>-o</code> <i>file</i></dt>
<dd> Send output to <i>file</i> instead of standard output. </dd>
<dt><code>&#8211;pfb</code>, <code>-b</code></dt>
<dd> Output a PFB font. This is the default. </dd>
<dt><code>&#8211;pfa</code>, <code>-a</code></dt>
<dd> Output a PFA font. </dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print usage information and exit. </dd>
<dt><code>&#8211;version</code></dt>
<dd> Print the version number and some short non-warranty information and exit.</dd></dl>
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
