---
title: "texexpand(1)"
name: "texexpand"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texexpand/"
description: "texexpand – expand \\input and \\include statements in a TeX file"
---
<h2>DESCRIPTION</h2>
<p> General translation mechanism: </p>
<p> The main program latex2html calls texexpand with the document name in order to expand some of its \input and \include statements, here also called `merging&#8217;, and to write a list of sensitized style, class, input, or include file names. When texexpand has finished, all is contained in one file, TMP_foo. (assumed foo.tex is the name of the document to translate). </p>
<p> In this version, texexpand cares for following environments that may span include files / section boundaries: a) \begin{comment} b) <code>%begin</code>{comment} c) \begin{any} introduced with \excludecomment d) <code>%begin</code>{any} e) \begin{verbatim} f) \begin{latexonly} g) <code>%begin</code>{latexonly} </p>
<p> e) - g) prevent texexpand from expanding input files, but the environment content goes fully into the output file. </p>
<p> Together with each merging of \input etc. there are so-called %%%texexpand markers accompanying the boundary. </p>
<p> When latex2html reads in the output file, it uses these markers to write each part to a separate file, and process them further. <br />
 </p>
<p> <code>Detailed technical notes:</code> </p>
<p> 1. <code>%begin</code>{latexonly} and <code>%end</code>{latexonly} have to be on a separate line. Anything between these tags (including the tags) is discarded. </p>
<p> 2. \begin{latexonly} and \end{latexonly} have to be on a separate line. Anything between these tags (including the tags) is not expanded. </p>
<p> 3. [%\]begin{&quot;to exclude&quot;} and [%\]end{&quot;to exclude&quot;} have to be on a separate line. Anything between these tags (including the tags) is discarded. </p>
<p> 4. \begin{verbatim/verbatim*} and \end{verbatim/verbatim*} have to be on a separate line. Anything between these tags (including the tags) is not expanded. </p>
<p> 5. The scope of any such tags may extend over several files. The opening tag for latexonly may occur on a different include level than the closing tag. The opening tag for verbatim/&quot;to exclude&#8217;&#8216; must occur within the same file than the closing tag. </p>
<p> 6. Warnings are printed when the document has been parsed and open tags remain. </p>
<p> 7. When in a ``to exclude&quot;/verbatim environment, texexpand won&#8217;t recognize <font SIZE="-1">ANY</font> command except the corresponding closing tag. There cannot be any nested constructions. This behaviour is identical to that of LaTeX. </p>
<p> 8. \begin{latexonly},\end{latexonly} may be nested, whereas <code>%begin</code>{latexonly},%end{latexonly} may not be nested. </p>
<p> 9. A ``%&#8216;&#8216; tag cannot close a ``\&#8216;&#8216; tag, and vice versa. </p>
<p> 10. Every \<i>document</i>(class|style), \usepackage, \input and \include command has to be on a separate line. </p>
<p> 11. Everything behind a `%&#8216; that isn&#8217;t preceded by a `\&#8216; is regarded as a comment, i.e. it is printed but not interpreted. </p>
<p> 12. If any command listed in 10. is preceded by an occurrence of `\verb&#8217; or `\latex&#8217; then it is <font SIZE="-1">NOT</font> interpreted. This crashes on lines like this: blah blah \verb+foo foo+ \input{bar} % bar won&#8217;t be loaded! </p>
<p> 13. Packages provided via \usepackage are handled the same way as `options&#8217; in \<i>document</i>(class|style), i.e. they are included when -auto_exclude is off, the package isn&#8217;t in <code>@dont_include</code> *<font SIZE="-1">OR</font>* the package is in <code>@do_include</code> (new). They are added to the style file together with their options if the file itself hasn&#8217;t been merged. \documentclass[options]{class} searches for every option.clo, \documentstyle[options]{style} searches for every option.sty. \usepackage[options]{packages} searches for every package.sty. </p>
<p> 14. Each texinputs directory is searched for input files/styles. If it ends in `//&#8216;, the whole subdirectory tree is searched. </p>
<p> 15. \input / \include merge the given file (if found under the given name or with .tex extension) if its basename is in <code>@do_include</code> or if it isn&#8217;t in <code>@dont_include</code> or if the given filename doesn&#8217;t end in .sty/.clo/.cls when -auto_exclude is set. <br />
 </p>
<p> <code>Notes</code> </p>
<p> Recognizes \documentclass, \documentstyle, \usepackage, \RequirePackage, \begin{verbatim}...\end{verbatim}, <code>%begin</code>{latexonly}...%end{latexonly}, \begin{latexonly}...\end{latexonly}, \input, \include, \verb, \latex \endinput, \end{document} \includecomment, \excludecomment \begin{&quot;to exclude&quot;}, \end{&quot;to exclude&quot;} <code>%begin</code>{&quot;to exclude&quot;}, <code>%end</code>{&quot;to exclude&quot;}  </p>
<h2>The gory Details</h2>
<p> Include and parse a file. This routine is recursive, see also &amp;process_input_include_file, &amp;process_document_header, and &amp;process_package_cmd. </p>
<p> Two global flags control the states of texexpand. <br />
&nbsp;o&nbsp;<code>$active</code>&nbsp;is true if we should interprete the lines to expand files, check for packages, etc. <br />
&nbsp;o&nbsp;<code>$mute</code>&nbsp;is true if we should prevent the lines from going into the out file. </p>
<p> We have three general states of texexpand: <br />
&nbsp;1)&nbsp;interprete the lines and pass them to the out file This is the normal case. Corresponding: <code>$active</code> true, <code>$mute</code> false </p>
<pre><code> 2) interprete minimal and suppress them
This is when parsing inside a comment environment, which
also would retain its body from LaTeX. =&gt; $active false, $mute true
</code></pre>
<pre><code> 3) interprete minimal and pass the lines to the out file
This is inside a verbatim or latexonly environment.
The line of course must be at least interpreted to determine the closing tag.
=&gt; $active false, $mute false
</code></pre>
<p> Any environment may extend over several include files. Any environment except verbatim and latexonly may have its opening or closing tag on different input levels. The comment and verbatim environments cannot be nested, as is with LaTeX. We must at least parse verbatim/comment environments in latexonly environments, to catch fake latexonly tags. </p>
<p> The work scheme: Five functions influence texexpand&#8217;s behavior. o &amp;process_file opens the given file and parses the non-comment part in order to set <code>$active</code> and <code>$mute</code> (see above). It calls &amp;interprete to interprete the non-comment content and either continues with the next line of its file or terminates if &amp;interprete detected the \end{document} or an \endinput. </p>
<p> o &amp;interprete handles some LaTeX tags with respect to the three states controlled by <code>$active</code> and <code>$mute</code>. Regarding to \input|include, \<i>document</i>(class|style), and \(use|Require)package the functions &amp;process_input_include_file, &amp;process_document_header, and &amp;process_package_cmd are called respectively. </p>
<p> o These three functions check if the file name or option files are enabled or disabled for merging (via TEXE_DO_INCLUDE or TEXE_DONT_INCLUDE). Any file that is to include will be `merged&#8217; into the current file, i.e. the function &amp;process_file is called at this place in time (recursively). This will stop interpretation at the current line in file, start with the new file to process and continues with the next line as soon as the new file is interpreted to its end. </p>
<p> The call tree (noweb+xy.sty would be handy here): </p>
<pre><code>    main
      |
      v
 +-&gt;process_file
 | |
 | v
 | interprete (with respect to the current line, one of that three)
 | | | |
 | v v v
 | process_input_include_file process_document_header process_package_cmd
 | | | |
 | v v v
 +----+---------------------------+------------------------+
</code></pre>
<p> Bugs: o Since the latexonly environment is not parsed, its contents might introduce environments which are not recognized. </p>
<p> o The closing tag for latexonly is not found if hidden inside an input file. </p>
<p> o One environment tag per line, yet! </p>
<p> o If I would have to design test cases for this beast I would immediately desintegrate into a logic cloud. </p>
<p> Notes: </p>
<p> o Ok, I designed test cases for it. Please refer to test `expand&#8217; of the regression test suite in the developers&#8217; module of the l2h repository. </p>
<p> o -unsegment feature: In this (rare) case, the user wants to translate a segmented document not in segments but in a whole (for testing, say). We enable this by recognizing the \segment command in &amp;interprete, causing the segment file to be treated like \input but loosing the first lines prior to \startdocument (incl.), as controlled via <code>$segmentfile</code>. On how to segment a document you are best guided by section ``Document Segmentation&#8217;&#8216; of the LaTeX2HTML manual.  </p>
<h2>CAVEATS</h2>
<p> This utility is automatically configured and built to work on the local setup. If this setup changes (e.g. some of the external commands are moved), the script has be be reconfigured.  </p>
<h2>Authors</h2>
<pre><code> Based on texexpand by Robert Thau, MIT AI lab, including modifications by
 Franz Vojik &lt;vojik [at] de.tu-muenchen.informatik&gt;
 Nikos Drakos &lt;nikos [at] cbl.leeds.ac.uk&gt;
 Sebastian Rahtz &lt;spqr [at] uk.ac.tex.ftp&gt;
 Maximilian Ott &lt;max [at] com.nec.nj.ccrl&gt;
 Martin Boyer
 Herbert Swan
 Jens Lippmann
</code></pre>
