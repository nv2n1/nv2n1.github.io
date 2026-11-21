---
title: "latex2rtf(1)"
name: "latex2rtf"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex2rtf/"
description: "latex2rtf – Convert a LaTeX file to an RTF file"
---
<h2>NAME</h2>
<p> latex2rtf - Convert a LaTeX file to an RTF file  </p>
<h2>SYNTAX</h2>
<p> latex2rtf [-hlpFSVW] [ -d# ] [ -D# ] [ -M# ] [ -se#] [ -sf#] [ -t# ] [ -Z# ] [ -a <i>auxfile</i> ] [ -b <i>bblfile</i> ] [ -C <i>codepage</i> ] [ -i <i>language</i> ] [ -o <i>outputfile</i> ] [ -P <i>/path/to/cfg</i> ] [ -T <i>/path/to/tmp</i> ] [ <i>inputfile</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The <i>latex2rtf</i> command converts a LaTeX file into RTF text format. The text and much of the formatting information is translated to RTF. </p>
<dl>
<dt><code>-a auxfile</code></dt>
<dd> <p> Used to specify a particular cross-referencing file. When this option is omitted, the <i>auxfile </i> is assumed to be the same as <i>inputfile</i> with the .tex suffix replaced by .aux. </p>
 </dd>
<dt><code>-b bblfile</code></dt>
<dd> <p> Used to specify a particular bibliography file When this option is omitted, the <i>bblfile </i> is assumed to be the same as <i>inputfile</i> with the .tex suffix replaced by .bbl. </p>
 </dd>
<dt><code>-C codepage</code></dt>
<dd> <p> used to specify the character set (code page) used in the LaTeX document for non-ansi characters. <i>codepage</i> may be one of the following: ansinew, applemac, cp437, cp437de, cp850, cp852, cp855, cp865, cp866, decmulti, cp1250, cp1252, koi8-r, koi8-u, latin1, latin2, latin3, latin4, latin5, latin9, maccyr, macukr, next, raw, raw437, raw852, raw1250, raw1251, and raw1253. The default behavior is to use ansinew (same as cp1252). For convenience, just the numbers 437, 437de, 850, 852, 855, 866, 1250 or 1252 may be specified. </p>
<p> The raw character set encoding prevents any 8-bit character translation. The RTF file is marked to use the same encoding as the default encoding for the program interpreting the RTF file. This is particularly useful when translating a file written in a language (e.g., czech) that maps poorly into the ansinew (western european) character set. </p>
 </dd>
<dt><code>-d#</code></dt>
<dd> <p> Write extra debugging output to stderr. Higher numbers cause more debugging output and range from 0 (only errors) to 6 (absurdly many messages). The default is 1 (Warnings and Errors only). </p>
 </dd>
<dt><code>-D dots_per_inch</code></dt>
<dd> <p> Used to specify the number of dots per inch in equations that are converted to bitmaps and for graphics that must be converted. Default is 300 dpi. </p>
 </dd>
<dt><code>-E# </code></dt>
<dd> <p> where # selects the type of figure handling desired. RTF does not support insertion of PS, PDF, or EPS file types. These figures must be converted to a bitmap format and then inserted. One trick is to insert the filenames into the RTF file and then in post-processing, insert the file. These options can be added together. <br />
 -E3 insert all figures (DEFAULT) <br />
 -E0 no figures in the RTF <br />
 -E1 insert figures having RTF-supported formats <br />
 -E2 convert and insert unsupported figure formats <br />
 -E4 insert only filenames for supported file formats <br />
 -E8 insert only filenames for unsupported file formats </p>
 </dd>
<dt><code>-f use fields</code></dt>
<dd> <p> -f0 do not use fields in RTF. This is handy when primitive RTF editors are being used to view the RTF output. <br />
 -f1 use fields for equations but not \ref and \cite. <br />
 -f2 use fields for \ref and \cite but not equations. <br />
 -f3 use fields when possible. This is the default and is most useful when the RTF file is being exported to be used in Word. This retains the most information from the original LaTeX file. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> use LaTeX to create bitmaps for all figures. This may help when figures are not translated properly. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Print a short usage note </p>
 </dd>
<dt><code>-i language</code></dt>
<dd> <p> used to set the idiom or language used in the LaTeX document <i>language</i> may be one of the following afrikaans, bahasa, basque, brazil, breton, catalan, croatian, czech, danish, dutch, english, esperanto, estonian, finnish, french, galician, german, icelandic, irish,italian, latin, lsorbian, magyar, norsk, nynorsk, polish, portuges, romanian, russian, samin, scottish, serbian, slovak, slovene, spanish, swedish, turkish, usorbian, welsh. The default is english. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Assume LaTeX source uses ISO 8859-1 (Latin-1) special characters (default behavior). </p>
 </dd>
<dt><code>-o outputfile</code></dt>
<dd> <p> Redirect output to <i>outputfile</i> Unless an <i>outputfile</i> is specified with the -o option, the resulting RTF is produced in a file with .tex replaced by .rtf. </p>
 </dd>
<dt><code>-M#</code></dt>
<dd> <p> where # selects the type of equation conversion. <br />
 -M1 displayed equations to RTF <br />
 -M2 inline equations to RTF <br />
 -M4 displayed equations to bitmap <br />
 -M8 inline equations to bitmap <br />
 -M16 insert Word comment field containing the raw LaTeX equation <br />
 -M32 insert raw LaTeX equation delimited by $...$ and \[...\] <br />
 -M64 displayed equations to EPS files with filenames in RTF <br />
 -M128 inline equations to EPS files with filenames in RTF <br />
 </p>
 </dd>
<dt>These options may be added together to get different results</dt>
<dd> <p> <br />
 -M0 no equations fields in the RTF. <br />
 -M3 converts both inline and displayed equations to RTF (DEFAULT). <br />
 -M12 converts inline and displayed equations to bitmaps. <br />
 -M192 converts inline and displayed equations to eps files and inserts a tag in RTF. <br />
 Bitmap conversion requires a working latex2png script. Producing bitmaps is slow. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Escape printed parentheses in mathematical formulas, as some versions of Word (e.g Word 2000) have deep psychological problems with EQ fields using quoted parentheses. If Word displays some formulas with parentheses as &#8216;Error!&#8216;, try this option. See also the -S option. </p>
 </dd>
<dt><code>-P /path/to/cfg</code></dt>
<dd> <p> used to specify the directory that contains the @code{.cfg} files </p>
 </dd>
<dt><code>-se#</code></dt>
<dd> <p> selects the scale for equation conversion, where # is the scale factor (default 1.00). </p>
 </dd>
<dt><code>-sf#</code></dt>
<dd> <p> selects the scale for figure conversion, where # is the scale factor (default 1.00). </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Use semicolons to separate arguments in RTF fields. This is needed when the machine opening the RTF file has a version of Word that uses commas for decimal points. This also can fix displaying some formulas as &#8216;Error!&#8216; You may also need to try the -p option. </p>
 </dd>
<dt><code>-t#</code></dt>
<dd> <p> selects the type of table conversion. <br />
 -t1 convert tables to RTF (default) <br />
 -t2 convert tables to bitmaps </p>
 </dd>
<dt><code>-T /path/to/tmp</code></dt>
<dd> <p> used to specify the folder where to put temporary files. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> Prints version on standard output and exits. </p>
 </dd>
<dt><code>-W </code></dt>
<dd> <p> Emit warnings directly in RTF file. Handy for catching things that do not get translated correctly. </p>
 </dd>
<dt><code>-Z# </code></dt>
<dd> <p> Add # close braces to end of RTF file. (Handy when file is not converted correctly and will not open in another word processor.) </p>
 </dd></dl>
<h2>CONFIGURATION FILES</h2>
<p> The configuration files are searched first in any directory specified by -P, then in the location specified by the environment variable RTFPATH, and finally in the location CFGDIR specified when <i>latex2rtf</i> was compiled. If the configuration files are not found then <i>latex2rtf </i> aborts. The configuration files allow additional fonts to be recognized, additional simple commands to be translation, and additional commands to be ignored.  </p>
<h2>CAUTION</h2>
<p> The input file must be a valid LaTeX file. Use LaTeX to find and fix errors before converting with <i>latex2rtf.</i> </p>
<p> The configuration files <code>direct.cfg</code> and <code>fonts.cfg</code> are in the correct directory. You may have to change <code>fonts.cfg</code> or <code>direct.cfg</code> to suit your needs.  </p>
<h2>BUGS</h2>
<p> Some might consider RTF to be a bug. </p>
<p> Some environments are currently ignored. </p>
<p> Translation without a LaTeX generated .aux file is poor.  </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to to the bug tracking system at <a rel="nofollow" href="http://sourceforge.net/projects/latex2rtf/.">http://sourceforge.net/projects/latex2rtf/.</a> Only report bugs for the latest version of <i>latex2rtf</i> that is available. Please identify your operating system. </p>
<p> If the program produces wrong output or does not work for you, INCLUDE A SHORT LATEX FILE that demonstrates the problem. The shorter the LaTeX file, the quicker your bug will get addressed. Bug reports with non-existent LaTeX files are not welcomed by the developers. Do not bother to send RTF files, since these are usually unhelpful.  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-latex/">latex</a>(1), rtf2LaTeX2e(1), LaTeX User&#8217;s Guide &amp; Reference Manual by Leslie Lamport </p>
<p> For complete, current documentation, refer to the Info file <code>latex2rtf.info,</code> the PDF file <code>latex2rtf.pdf</code> or the HTML file <code>latex2rtf.html</code> which are made from the TeXInfo source file <code>latex2rtf.texi.</code> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNTAX</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">CONFIGURATION FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">CAUTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">REPORTING BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">SEE ALSO</a></dt>
<dd>  </dd></dl>
