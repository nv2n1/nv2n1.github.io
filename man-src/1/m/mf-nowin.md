---
title: "mf-nowin(1)"
name: "mf-nowin"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mf-nowin/"
description: "mf, inimf, mf-nowin – Metafont, a language for font and logo design"
---

<h2>SYNOPSIS</h2>
<p> <code>mf</code> [<i>options</i>] [<i>commands</i>]</p>
<h2>DESCRIPTION</h2>
<p> Metafont reads the program in the specified files and outputs font rasters (in <i>gf</i> format) and font metrics (in <i>tfm</i> format). The Metafont language is described in <i>The Metafontbook</i>. </p>
<p> Like TeX, Metafont is normally used with a large body of precompiled macros, and font generation in particular requires the support of several macro files. This version of Metafont looks at its command line to see what name it was called under. Both <code>inimf</code> and <code>virmf</code> are symlinks to the <code>mf</code> executable. When called as <code>inimf</code> (or when the <code>-ini</code> option is given) it can be used to precompile macros into a <i>.base</i> file. When called as <code>virmf</code> it will use the <i>plain</i> base. When called under any other name, Metafont will use that name as the name of the base to use. For example, when called as <code>mf</code> the <i>mf</i> base is used, which is identical to the <i>plain</i> base. Other bases than <i>plain</i> are rarely used. </p>
<p> The <i>commands</i> given on the command line to the Metafont program are passed to it as the first input line. (But it is often easier to type extended arguments as the first input line, since UNIX shells tend to gobble up or misinterpret Metafont&#8217;s favorite symbols, like semicolons, unless you quote them.) As described in <i>The Metafontbook</i>, that first line should begin with a filename, a \<i>controlsequence</i>, or a <i>&amp;basename</i>. </p>
<p> The normal usage is to say</p>
<dl>
<dt>
</dt><dd> <code>mf&nbsp;</code> &#8216;\mode=&lt;printengine&gt;; [mag=magstep(<i>n</i>);]&#8217; input&nbsp;<i> font </i></dd></dl>
<p> to start processing <i>font.mf</i>. The single quotes are the best way of keeping the Unix shell from misinterpreting the semicolons and from removing the \ character, which is needed here to keep Metafont from thinking that you want to produce a font called <i>mode</i>. (Or you can just say <i>mf</i> and give the other stuff on the next line, without quotes.) Other control sequences, such as <i>batchmode</i> (for silent operation) can also appear. The name <i>font</i> will be the &#8220;jobname&#8221;, and is used in forming output file names. If Metafont doesn&#8217;t get a file name in the first line, the jobname is <i>mfput</i>. The default extension, <i>.mf</i>, can be overridden by specifying an extension explicitly. </p>
<p> A log of error messages goes into the file <i>jobname</i><code>.</code><i>log</i>. The output files are <i>jobname</i><code>.</code><i>tfm</i> and <i>jobname</i><code>.</code><i>&lt;</i>number<i>&gt;gf</i>, where &lt;number&gt; depends on the resolution and magnification of the font. The <i>mode</i> in this example is shown generically as &lt;printengine&gt;, a symbolic term for which the name of an actual device or, most commonly, the name <i>localfont</i> (see below) must be substituted. If the mode is not specified or is not valid for your site, Metafont will default to <i>proof</i> mode which produces large character images for use in font design and refinement. Proof mode can be recognized by the suffix <i>.2602gf</i> after the jobname. Examples of proof mode output can be found in <i>Computer Modern Typefaces</i> (Volume E of <i>Computers and Typesetting</i>). The system of <i>magsteps</i> is identical to the system used by TeX, with values generally in the range 0.5, 1.0, 2.0, 3.0, 4.0 and 5.0. A listing of <i>gf</i> numbers for 118-dpi, 240-dpi and 300-dpi fonts is shown below. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center>MAGSTEP</td>
<td ALIGN=center>118 dpi</td>
<td ALIGN=center>240 dpi</td>
<td ALIGN=center>300 dpi
</td>
</tr>
<tr VALIGN=top>
<td>mag=magstep(0)</td>
<td>118</td>
<td>240</td>
<td>300
</td>
</tr>
<tr VALIGN=top>
<td>mag=magstep(0.5)</td>
<td>129</td>
<td>263</td>
<td>329
</td>
</tr>
<tr VALIGN=top>
<td>mag=magstep(1)</td>
<td>142</td>
<td>288</td>
<td>360
</td>
</tr>
<tr VALIGN=top>
<td>mag=magstep(2)</td>
<td>170</td>
<td>346</td>
<td>432
</td>
</tr>
<tr VALIGN=top>
<td>mag=magstep(3)</td>
<td>204</td>
<td>415</td>
<td>518
</td>
</tr>
<tr VALIGN=top>
<td>mag=magstep(4)</td>
<td>245</td>
<td>498</td>
<td>622
</td>
</tr>
<tr VALIGN=top>
<td>mag=magstep(5)</td>
<td>294</td>
<td>597</td>
<td>746
</td>
</tr>
</table>
<p> Magnification can also be specified not as a magstep but as an arbitrary value, such as 1.315, to create special character sizes. </p>
<p> Before font production can begin, it is necessary to set up the appropriate base files. The minimum set of components for font production for a given print-engine is the <i>plain.mf</i> macro file and the local <i>mode_def</i> file. The macros in <i>plain.mf</i> can be studied in an appendix to the <i>Metafontbook</i>; they were developed by Donald E. Knuth, and this file should never be altered except when it is officially upgraded. Each <i>mode_def</i> specification helps adapt fonts to a particular print-engine. There is a regular discussion of <i>mode_def</i>s in <i>TUGboat</i>, the journal of the TeX Users Group. The local ones in use on this computer should be in <i>modes.mf</i>. </p>
<p> The <i>e</i> response to Metafont&#8217;s error-recovery mode invokes the system default editor at the erroneous line of the source file. There is an environment variable, MFEDIT, that overrides the default editor. It should contain a string with &quot;%s&quot; indicating where the filename goes and &quot;%d&quot; indicating where the decimal linenumber (if any) goes. For example, an MFEDIT string for the <code>vi</code> editor can be set with the <code>csh</code> command</p>
<dl>
<dt>
</dt><dd> <i>setenv MFEDIT &quot;vi +%d %s&quot;</i></dd></dl>
<p> A convenient file in the library is <i>null.mf</i>, containing nothing. When <code>mf</code> can&#8217;t find the file it thinks you want to input, it keeps asking you for another file name; responding `null&#8217; gets you out of the loop if you don&#8217;t want to input anything.</p>
<h2>ONLINE GRAPHICS OUTPUT</h2>
<p> Metafont can use most modern displays, so you can see its output without printing. Chapter 23 of <i>The Metafontbook</i> describes what you can do. This implementation of Metafont uses environment variables to determine which display device you want to use. First it looks for a variable MFTERM, and then for TERM. If it can&#8217;t find either, you get no online output. Otherwise, the value of the variable determines the device to use: <code>hp2627</code>, <code>sun</code> (for old SunView), <code>tek</code>, <code>uniterm</code> (for an Atari ST Tek 4014 emulator), <code>xterm</code> (for either X10 or X11). Some of these devices may not be supported in all Metafont executables; the choice is made at compilation time. </p>
<p> On some systems, there are two Metafont binaries, <code>mf</code> and <code>mf-nowin</code>. On those systems the <code>mf</code> binary supports graphics, while the <code>mf-nowin</code> binary does not. The <code>mf-nowin</code> binary is used by scripts like <code>mktexpk</code> where graphics support is a nuisance rather than something helpful.</p>
<h2>OPTIONS</h2>
<p> This version of Metafont understands the following command line options.</p>
<dl>
<dt><code>-base</code><i>&nbsp;base</i></dt>
<dd> Use <i>base</i> as the name of the base to be used, instead of the name by which Metafont was called or a <i>%&amp;</i> line.</dd>
<dt><code>-cnf-line</code><i>&nbsp;string</i></dt>
<dd> Parse <i>string</i> as a <i>texmf.cnf</i> configuration line. See the Kpathsea manual.</dd>
<dt><code>-file-line-error</code></dt>
<dd> Print error messages in the form <i>file:line:error</i> which is similar to the way many compilers format them.</dd>
<dt><code>-no-file-line-error</code></dt>
<dd> Disable printing error messages in the <i>file:line:error</i> style.</dd>
<dt><code>-file-line-error-style</code></dt>
<dd> This is the old name of the <code>-file-line-error</code> option.</dd>
<dt><code>-halt-on-error</code></dt>
<dd> Exit with an error code when an error is encountered during processing.</dd>
<dt><code>-help</code></dt>
<dd> Print help message and exit.</dd>
<dt><code>-ini</code></dt>
<dd> Be <code>inimf</code>, for dumping bases; this is implicitly true if the program is called as <code>inimf</code>.</dd>
<dt><code>-interaction</code><i>&nbsp;mode</i></dt>
<dd> Sets the interaction mode. The mode can be one of <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding commands.</dd>
<dt><code>-jobname</code><i>&nbsp;name</i></dt>
<dd> Use <i>name</i> for the job name, instead of deriving it from the name of the input file.</dd>
<dt><code>-kpathsea-debug</code><i>&nbsp;bitmask</i></dt>
<dd> Sets path searching debugging flags according to the bitmask. See the <i>Kpathsea</i> manual for details.</dd>
<dt><code>-maketex</code><i>&nbsp;fmt</i></dt>
<dd> Enable mktex<i>fmt</i>, where <i>fmt</i> must be <i>mf</i>.</dd>
<dt><code>-no-maketex</code><i>&nbsp;fmt</i></dt>
<dd> Disable mktex<i>fmt</i>, where <i>fmt</i> must be <i>mf</i>.</dd>
<dt><code>-output-directory</code><i>&nbsp;directory</i></dt>
<dd> Write output files in <i>directory</i> instead of the current directory. Look up input files in <i>directory</i> first, the along the normal search path.</dd>
<dt><code>-parse-first-line</code></dt>
<dd> If the first line of the main input file begins with <i>%&amp;</i> parse it to look for a dump name or a <code>-translate-file</code> option.</dd>
<dt><code>-no-parse-first-line</code></dt>
<dd> Disable parsing of the first line of the main input file.</dd>
<dt><code>-progname</code><i>&nbsp;name</i></dt>
<dd> Pretend to be program <i>name</i>. This affects both the format used and the search paths.</dd>
<dt><code>-recorder</code></dt>
<dd> Enable the filename recorder. This leaves a trace of the files opened for input and output in a file with extension <i>.fls</i>.</dd>
<dt><code>-translate-file</code><i>&nbsp;tcxname</i></dt>
<dd> Use the <i>tcxname</i> translation table.</dd>
<dt><code>-version</code></dt>
<dd> Print version information and exit.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> See the Kpathsearch library documentation (the `Path specifications&#8217; node) for the details of how the environment variables are use when searching. The <code>kpsewhich</code> utility can be used to query the values of the variables. </p>
<p> If the environment variable <code>TEXMFOUTPUT</code> is set, Metafont attempts to put its output files in it, if they cannot be put in the current directory. Again, see <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1).</p>
<dl>
<dt><code>MFINPUTS</code></dt>
<dd> Search path for <i>input</i> files.</dd>
<dt><code>MFEDIT</code></dt>
<dd> Command template for switching to editor.</dd>
<dt><code>MFTERM</code></dt>
<dd> Determines the online graphics display. If MFTERM is not set, and DISPLAY is set, the Metafont window support for X is used. (DISPLAY must be set to a valid X server specification, as usual.) If neither MFTERM nor DISPLAY is set, TERM is used to guess the window support to use.</dd></dl>
<h2>FONT UTILITIES</h2>
<p> A number of utility programs are available. The following is a partial list of available utilities and their purpose. Consult your local Metafont guru for details. </p>
<dl>
<dt><code>gftopk</code></dt>
<dd> Takes a <i>gf</i> file and produces a more tightly packed <i>pk</i> font file.</dd>
<dt><code>gftodvi</code></dt>
<dd> Produces proof sheets for fonts.</dd>
<dt><code>gftype</code></dt>
<dd> Displays the contents of a <i>gf</i> file in mnemonics and/or images.</dd>
<dt><code>pktype</code></dt>
<dd> Mnemonically displays the contents of a <i>pk</i> file.</dd>
<dt><code>mft</code></dt>
<dd> Formats a source file as shown in <i>Computer Modern Typefaces</i>.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>mf.pool</i></dt>
<dd> Encoded text of Metafont&#8217;s messages.</dd>
<dt><i>*.base</i></dt>
<dd> Predigested Metafont base files.</dd>
<dt><i>$TEXMFMAIN/metafont/base/plain.mf</i></dt>
<dd> The standard base.</dd>
<dt><i>$TEXMFMAIN/metafont/misc/modes.mf</i></dt>
<dd> The file of <i>mode_def</i>s for your site&#8217;s various printers</dd></dl>
<h2>NOTES</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of Metafont can be found in the info manual <i>Web2C: A TeX implementation</i>.</p>
<h2>BUGS</h2>
<p> On January 4, 1986 the &#8220;final&#8221; bug in Metafont was discovered and removed. If an error still lurks in the code, Donald E. Knuth promises to pay a finder&#8217;s fee which doubles every year to the first person who finds it. Happy hunting.</p>
<h2>SUGGESTED READING</h2>
<p> Donald E. Knuth, <i>The Metafontbook</i> (Volume C of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13445-4.<br />
 Donald E. Knuth, <i>Metafont: The Program</i> (Volume D of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13438-1.<br />
 Donald E. Knuth, <i>Computer Modern Typefaces</i> (Volume E of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13446-2.<br />
 <i>TUGboat</i> (the journal of the TeX Users Group).</p>
<h2>COMMENTS</h2>
<p> Warning: &#8220;Type design can be hazardous to your other interests. Once you get hooked, you will develop intense feelings about letterforms; the medium will intrude on the messages that you read. And you will perpetually be thinking of improvements to the fonts that you see everywhere, especially those of your own design.&#8221;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gftopk/">gftopk</a></code>(1), <code><a href="/docs/linux/man/1-gftodvi/">gftodvi</a></code>(1), <code><a href="/docs/linux/man/1-gftype/">gftype</a></code>(1), <code><a href="/docs/linux/man/1-mft/">mft</a></code>(1), <code><a href="/docs/linux/man/1-mpost/">mpost</a></code>(1), <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1), <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Metafont was designed by Donald E. Knuth, who implemented it using his Web system for Pascal programs. It was originally ported to Unix by Paul Richards at the University of Illinois at Urbana-Champaign. This page was mostly written by Pierre MacKay. </p>
