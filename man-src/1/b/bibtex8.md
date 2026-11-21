---
title: "bibtex8(1)"
name: "bibtex8"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibtex8/"
description: "bibtex8 – 8-bit Big BibTeX"
---
<h2 class="name">NAME</h2>
<p> bibtex8 - 8-bit Big BibTeX </p>
<h2>SYNOPSIS</h2>
<p> <code>bibtex8</code> [<i>options</i>] <i>aux-file</i>  </p>
<h2>DESCRIPTION</h2>
<p> <code>BibTeX8</code> is an 8-bit implementation of BibTeX written in C. It has been enhanced by adding the following features: </p>
<p> - &quot;big&quot; (32-bit) and customisable capacity </p>
<p> - flexible support for non-English languages using 8-bit character sets </p>
<p> <code>BibTeX8</code> accepts 8-bit characters in its input files, and writes 8-bit characters to its output files. The character set is defined by an external configuration file --- the Codepage and Sort order (&quot;CS&quot;) file. By default, it reads a specific CS file &quot;88591lat.csf&quot;, which defines ISO 8859-1 character set and its alphabetical sorting order including accented characters.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code><code>--help</code></dt>
<dd> <p> display some brief help text. </p>
 </dd>
<dt><code>-7</code><code>--traditional</code></dt>
<dd> <p> operate in the original 7-bit mode, no CS file used. Only 7-bit ASCII characters are supported, and they are sorted by ASCII code value. </p>
 </dd>
<dt><code>-8</code><code>--8bit</code></dt>
<dd> <p> force 8-bit mode, no CS file used. All 8-bit characters (code &gt; 127) are treated as letters, and they are sorted by their code value. </p>
 </dd>
<dt><code>-c</code><code>--csfile</code> FILE</dt>
<dd> <p> read FILE as the BibTeX character set and sort definition file. Note that options <code>-7</code>, <code>-8</code> and <code>-c</code> are exclusive. </p>
 </dd>
<dt><code>-d</code><code>--debug</code> TYPE</dt>
<dd> <p> report debugging information. TYPE is one or more of all, csf, io, mem, misc, search. </p>
 </dd>
<dt><code>-s</code><code>--statistics</code></dt>
<dd> <p> report internal statistics. </p>
 </dd>
<dt><code>-t</code><code>--trace</code></dt>
<dd> <p> report execution tracing. </p>
 </dd>
<dt><code>-v</code><code>--version</code></dt>
<dd> <p> report BibTeX version. </p>
 </dd>
<dt><code>-B</code><code>--big</code></dt>
<dd> <p> set large BibTeX capacity. </p>
 </dd>
<dt><code>-H</code><code>--huge</code></dt>
<dd> <p> set huge BibTeX capacity. </p>
 </dd>
<dt><code>-W</code><code>--wolfgang</code></dt>
<dd> <p> set really huge BibTeX capacity for Wolfgang. </p>
 </dd>
<dt><code>-M</code><code>--min_crossrefs</code> ##</dt>
<dd> <p> set min_crossrefs to ##. </p>
 </dd>
<dt><code>--mcites</code> ##</dt>
<dd> <p> allow ## \cites in the .aux files (deprecated). </p>
 </dd>
<dt><code>--mentints</code> ##</dt>
<dd> <p> allow ## integer entries in the .bib databases (deprecated). </p>
 </dd>
<dt><code>--mentstrs</code> ##</dt>
<dd> <p> allow ## string entries in the .bib databases (deprecated). </p>
 </dd>
<dt><code>--mfields</code> ##</dt>
<dd> <p> allow ## fields in the .bib databases (deprecated). </p>
 </dd>
<dt><code>--mpool</code> ##</dt>
<dd> <p> set the string pool to ## bytes (deprecated). </p>
 </dd>
<dt><code>--mstrings</code> ##</dt>
<dd> <p> allow ## unique strings. </p>
 </dd>
<dt><code>--mwizfuns</code> ##</dt>
<dd> <p> allow ## wizard functions (deprecated). </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> More detailed description of <code>BibTeX8</code> is available at $TEXMFDIST/doc/bibtex8/00readme.txt. The syntax of Codepage and Sort order (CS) File can be found at $TEXMFDIST/doc/bibtex8/csfile.txt.  </p>
<h2>AUTHORS</h2>
<p> <code>BibTeX8</code> was written by Niel Kempson &lt;kempson [at] snowyowl.co.uk&gt; and Alejandro Aguilar-Sierra &lt;asierra [at] servidor.unam.mx&gt;. This manpage was written for TeX Live, based on the work by Norbert Preining for Debian/GNU Linux. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">AUTHORS</a></dt>
<dd>  </dd></dl>
