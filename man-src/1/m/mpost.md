---
title: "mpost(1)"
name: "mpost"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpost/"
description: "mpost, pmpost, upmpost – MetaPost, a system for creating graphics r-mpost, r-pmpost, r-upmpost – restricted MetaPost"
---

<h2 class="name">NAME</h2>
<p> mpost, pmpost, upmpost &#8211; MetaPost, a system for creating graphics r-mpost, r-pmpost, r-upmpost &#8211; restricted MetaPost </p>
<h2>SYNOPSIS</h2>
<p> <code>mpost</code> [<i>options</i>] [<i>commands</i>] </p>
<p> <code>mpost </code> <code>&#8211;dvitomp</code> <i>dvifile</i>[<code>.dvi</code>] [<i>mpxfile</i>[<code>.mpx</code>]] </p>
<h2>DESCRIPTION</h2>
<p> MetaPost interprets the MetaPost language and produces PostScript (EPS) or Scalable Vector Graphics (SVG) pictures. The MetaPost language is similar to Knuth&#8217;s Metafont with additional features for including <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) or <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) commands and accessing features of PostScript not found in Metafont. </p>
<p> MetaPost is normally used with a set of basic macros, and it will use its executable name as the name of the preload file to use. For example, when called as <code>mpost</code> the <i>mpost.mp</i> file is used, which simply reads <i>plain.mp</i>. When the <code>&#8211;ini</code> option is given, preloading does not happen. </p>
<p> The <i>commands</i> given on the command line to the MetaPost program are passed to it as the first input line. (But it is often easier to type extended arguments as the first input line, since UNIX shells tend to gobble up or misinterpret MetaPost&#8217;s favorite symbols, like semicolons, unless you quote them.) The normal usage is to say <i>mpost figs</i> to process the file <i>figs.mp</i>. The basename of <i>figs</i> becomes the &#8220;jobname&#8221;, and is used in forming output file names. If no file is named, the jobname becomes <i>mpout</i>. The default extension, <i>.mp</i>, can be overridden by specifying an extension explicitly. </p>
<p> When the <code>&#8211;dvitomp</code> option is given, MetaPost acts as DVI-to-MPX converter only. See dvitomp (1) for details. </p>
<p> The <code>pmpost </code> program is a variant with Japanese support, and <code>upmpost</code> has Unicode-enabled Japanese support, analogous to ptex and uptex. </p>
<p> All three variants are also installed with an `r-&#8216; prefix, that is, <code>r-mpost</code>, <code>r-pmpost</code>, <code>r-upmpost</code>, which implicitly specify the <code>&#8211;restricted</code> option to make MetaPost safe to run on unknown input; the tex, makempx, and editor commands are disabled. </p>
<p> This manual page is a mere skeleton. For a list of all command line options, run <code>&#8211;help</code>. </p>
<p> The main documentation for this version of MetaPost can be found in the User Manual that should have been installed along with the program and is also available from <a rel="nofollow" href="https://tug.org/metapost.">https://tug.org/metapost.</a> </p>
<p> The MetaPost language is similar to Metafont, but the manual assumes no knowledge of Metafont. MetaPost does not have bitmap output commands or Metafont&#8217;s online display mechanism.</p>
<h2>FILES</h2>
<dl>
<dt><i>plain.mp</i></p>
<dd> The standard preload file.</p>
<dt><i>mfplain.mp</i></p>
<dd> The Metafont-compatible preload file.</p>
<dt><i>$TEXMFMAIN/metapost/base/*.mp</i></p>
<dd> The standard MetaPost macros included in the original distribution.</p>
<dt><i>$TEXMFMAIN/metapost/support/*</i></p>
<dd> Various tables for handling included <i>tex</i> and <i>troff</i>.</p>
<dt><i>$TEXMFMAIN/metapost/support/trfonts.map</i></p>
<dd> Table of corresponding font names for <i>troff </i> and PostScript.</p>
<dt><i>psfonts.map</i></p>
<dd> Table of corresponding font names for <i>tex</i> and PostScript.</p>
<dt><i>$TEXMFMAIN/doc/metapost/*</i></p>
<dd> The MetaPost manual and tutorial source, also including sample figures</dl>
<h2>SUGGESTED READING</h2>
<p> Donald E. Knuth, <i>The Metafontbook</i> (Volume C of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13445-4.<br />
 <i>TUGboat</i> (the journal of the TeX Users Group).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvitomp/">dvitomp</a></code>(1), <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1), <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), <code><a href="/docs/linux/man/1-mptopdf/">mptopdf</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1),<br />
 MetaPost home page &lt;URL: <a rel="nofollow" href="https://tug.org/metapost/">https://tug.org/metapost/</a> &gt;.</p>
<h2>AUTHORS</h2>
<p> MetaPost was created by John D. Hobby, incorporating algorithms from Metafont by Donald E. Knuth. It was originally implemented on Unix, incorporating system-dependent routines from <code>web2c</code>, while not relying on it except for the actual Web-to-C translator. </p>
<p> Ulrik Vieth adapted MetaPost to take advantage of the advanced path searching features in more recent versions of <code>web2c</code> and worked towards fully integrating MetaPost into the canonical Unix TeX distribution. </p>
<p> The primary author of the current MetaPost was Taco Hoekwater, with assistance from Hans Hagen and many others. It is currently maintained by Luigi Scarso.</p>
<h2>BUGS</h2>
<p> The MetaPost home page is <a rel="nofollow" href="https://tug.org/metapost.">https://tug.org/metapost.</a> </p>
<h2>Index</h2>
