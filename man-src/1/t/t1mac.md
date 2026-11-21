---

title: "t1mac(1)"
name: "t1mac"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1mac/"
description: "t1mac – translate a PFA or PFB PostScript Type 1 font into Macintosh format"
---

<p> <code>t1mac</code> [<code>&#8211;macbinary</code> | <code>&#8211;applesingle</code> | <code>&#8211;appledouble</code> | <code>&#8211;binhex</code> | <code>&#8211;raw</code>] [<code>&#8211;filename</code> <i>name</i>] [<i>input</i> [<i>output</i>]]</p>
<p> <code>t1mac</code> reads a PFA (hexadecimal) or PFB (binary) PostScript Type 1 font file and generates an equivalent Macintosh Type 1 font file. The output file can be in MacBinary II, AppleSingle, AppleDouble, or BinHex format, or it can be a raw resource fork. The default is MacBinary II; use an option to choose a different format. If the <i>output</i> file is not specified output goes to the standard output. </p>
<p> WARNING: The output of <code>t1mac</code> is not sufficient to use the font, since Macintoshes can&#8217;t read raw Type 1 fonts. You will need to create a font suitcase containing bitmap fonts if you do not have such a suitcase for the font already. <code>t1mac</code> cannot help you do this.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;raw</code>, <code>-r</code></dt>
<dd> Indicates that output should be a raw resource fork.</dd>
<dt><code>&#8211;macbinary</code></dt>
<dd> Indicates that output should be in MacBinary I or II format. This is the default.</dd>
<dt><code>&#8211;applesingle</code></dt>
<dd> Indicates that output should be in AppleSingle format.</dd>
<dt><code>&#8211;appledouble</code></dt>
<dd> Indicates that output should be in AppleDouble format.</dd>
<dt><code>&#8211;binhex</code></dt>
<dd> Indicates that output should be in BinHex 4.0 format.</dd>
<dt><code>&#8211;filename</code>=<i>name</i>, <code>-n</code> <i>name</i></dt>
<dd> Sets the Macintosh filename of the output font to <i>name</i>. The default is to construct the filename from the font&#8217;s name using established Macintosh conventions. This option is not useful when output is a raw resource fork.</dd></dl>
<h2>SEE ALSO</h2>
<h2>AUTHORS</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
