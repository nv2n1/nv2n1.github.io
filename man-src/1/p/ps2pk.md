---
title: "ps2pk(1)"
name: "ps2pk"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2pk/"
---

<h2 class="name">NAME</h2>
 

 ps2pk - creates a TeX pkfont from a type1 PostScript font 

<h2>SYNOPSIS</h2>

 ps2pk [ -v ] [ -e<i>enc</i> ] [ -X<i>xres</i> ] [ -E<i>expansion</i> ] [ -S<i>slant</i> ] [ -P<i>pointsize</i> ] [ -R<i>baseres</i> ] [ -r<i>aspectratio</i> ] [ -Y<i>yres</i> ] [ -a<i>AFMfile</i> ] [ -m<i>modename</i> ] type1 [pkfont]

<h2>DESCRIPTION</h2>

 This program renders a given type1 PostScript font at a given pointsize (default 10.0 points) and resolution (default 300dpi) into a TeX pkfont. 

 To generate the pkfont ps2pk needs a valid type1 font file (for example Utopia-Regular, Utopia-Regula.pfb or Utopia-Regula.pfa) and its corresponding AFM-file (Utopia-Regular.afm) with the font metrics. The program accepts both the binary type1 format (Utopia-Regula.pfb) and its ASCII equivalent (Utopia-Regular or Utopia-Regula.pfa). To locate the files, ps2pk uses the kpathsea library (see the info page on kpathsea). Additionally, pfb and pfa files are searched for in the directory specified in the environment variable T1INPUTS, and afm files are searched in AFMFONTS, if they are set (the -v flag will report which filenames are looked for). 

 The program will make a pkfont in which the character codes are derived from their AFM (Adobe Font Metrics) defined values. This can be overruled by specifying an explicit encoding file via the -e option. The encoding file <i>enc</i> should contain a valid PostScript encoding containing PostScript names like /hyphen. Here is an incomplete example (see afm2tfm for complete syntax): 

<dl>
<dt>
<dd> <pre>
% This is the EC encoding.
/ECEncoding [          % now 256 chars follow
% 0x00
  /grave /acute /circumflex /tilde /dieresis /hungarumlaut
  /ring /caron /breve /macron /dotaccent /cedilla
  /ogonek /quotesinglbase /guilsinglleft /guilsinglright
  (Rest of lines omitted.)
% 0xF0
  /eth /ntilde /ograve /oacute /ocircumflex /otilde
  /odieresis /oe /oslash /ugrave /uacute /ucircumflex
  /udieresis /yacute /thorn /germandbls ] def
</pre></dl>
 

 Options and arguments:
<dl>
<dt>-a<i>AFMfile</i>
<dd> Overrules the name that is used to locate the AFM file. 

<dt>-e<i>enc</i>
<dd> Name of a file containing an encoding scheme (default - the encoding named in the AFM-file is used). The actual PostScript name of the encoding scheme is written as a &quot;special&quot; at the end of the pkfont. 

<dt>-E<i>extension</i>
<dd> The extension factor (real value, default 1.0). 

<dt>-m<i>modename</i>
<dd> A modename such as would be used by METAFONT (default &quot;Unknown mode&quot;). 

<dt>-P<i>pointsize</i>
<dd> The desired pointsize (real value, default 10.0 points). 

<dt>-R<i>baseres</i>
<dd> The desired base resolution (integer value, default 300 dpi). If this differs from the value of <i>xres</i>, the appropriate magnification will be shown in the &quot;specials&quot; at the end of the pkfont. If possible, this will be expressed as a magstep, otherwise as a real number. For example, a pkfont with an <i>xres</i> of 329, using the default base resolution of 300, will include the &quot;special&quot; text &quot;mag=magstep(0.5)&quot; at the end of the font. 

<dt>-r<i>aspectratio</i>
<dd> The desired aspect ratio (expression, integerY/integerX, default 300/300). This will be shown in the &quot;specials&quot; at the end of the pkfont. Setting the aspect ratio creates a value for <i>yres</i> but an explicit <i>yres</i> value will take precedence. Argument must be in &quot;&quot; if spaces are left around `/'. 

<dt>-S<i>slant</i>
<dd> The slant (real value, default 0.0). 

<dt>-X<i>xres</i>
<dd> The resolution in the X direction (integer value, default 300 dpi). 

<dt>-Y<i>yres</i>
<dd> The resolution in the Y direction (integer value, default the value of <i>xres</i>). If <i>yres</i> differs from <i>xres</i>, a &quot;special&quot; text giving the aspect ratio will be written at the end of the pkfont. 

<dt>-v
<dd> Verbose flag. (Tells what the program is doing.) 

<dt>type1
<dd> The name of the PostScript type1 font. The name of the AFM-file will be constructed from this name by removing the extension (if suplied) and adding &quot;.afm&quot;. The PostScript &quot;FontName&quot; is extracted from the AFM-file and written into a &quot;special&quot; at the end of the pkfont. 

<dt>[pkfont]
<dd> The name of the resulting pkfont can be overruled with this name. The default name of pkfont is derived from the basename of the type1 font, the pointsize and <i>xres</i>. For example `ps2pk -P17.28 Utopia-Regular' will result in `Utopia-Regular17.300pk'. An explicit value for the name of the pkfont is necessary when the type1 font name already shows the point size, otherwise the <i>pointsize</i> value is catenated on to the pkfont basename which is usually not what is wanted. 

</dl>
 

 The following PK &quot;specials&quot; provide an internal check on the characteristics of the pkfont, in accordance with the recommendations of the TeX Working Group on the TeX Directory Standard (TWG-TDS): 
 &quot;fontid=<i>FontName</i>&quot;, &quot;codingscheme=<i>Encoding</i>&quot;, &quot;fontfacebyte&quot;, &quot;mag&quot;, &quot;mode=(ps2pk)<i>modename</i>&quot;, &quot;pixels-per-inch&quot;, and &quot;aspect-ratio&quot; if it is other than unity. 

<h2>ACKNOWLEDGEMENT</h2>

 This program uses the Type1 hinting and rendering software IBM has donated to the X Consortium. 

<h2>SEE ALSO</h2>

 <pre>
`METAFONT: The Program', Donald Knuth.
`The GFtoPK processor', belonging to the METAFONTware.
`Adobe Font Metric Files', Version 3.0, PostScript Developer
Support Group.
<a HREF="//www.systutorials.com/docs/linux/man/1-afm2tfm/">afm2tfm</a>(1)
<a HREF="//www.systutorials.com/docs/linux/man/1-pk2bm/">pk2bm</a>(1)
<a HREF="//www.systutorials.com/docs/linux/man/1-kpsewhich/">kpsewhich</a>(1)
info kpathsea
</pre>

<h2>VERSION</h2>

 1.4 (January 1994) 

<h2>AUTHOR</h2>

 Piet Tutelaers, modified for ps2pkm by Pierre A. Mackay. This manpage was adapted to teTeX by Frank Kuester. 

 Maintained in TeX Live; please send bug reports or other correspondence to tex-k [at] tug.org (<a rel="nofollow" HREF="http://lists.tug.org/tex-k">http://lists.tug.org/tex-k</a>). 

<h2>Index</h2>


