---
title: "texexpand(1)"
name: "texexpand"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texexpand/"
description: "texexpand – expand \\input and \\include statements in a TeX file"
---

<h2 class="name">NAME</h2>
<p> texexpand &#8211; expand \input and \include statements in a TeX file </p>
<h2>DESCRIPTION</h2>
<p> General translation mechanism: </p>
<p> The main program latex2html calls texexpand with the document name in order to expand some of its \input and \include statements, here also called `merging&#8217;, and to write a list of sensitized style, class, input, or include file names. When texexpand has finished, all is contained in one file, TMP_foo. (assumed foo.tex is the name of the document to translate). </p>
<p> In this version, texexpand cares for following environments that may span include files / section boundaries: a) egin{comment} b) <tt>%begin</tt>{comment} c) egin{any} introduced with xcludecomment d) <tt>%begin</tt>{any} e) egin{verbatim} f) egin{latexonly} g) <tt>%begin</tt>{latexonly} </p>
<p> e) &#8211; g) prevent texexpand from expanding input files, but the environment content goes fully into the output file. </p>
<p> Together with each merging of \input etc. there are so-called %%%texexpand markers accompanying the boundary. </p>
<p> When latex2html reads in the output file, it uses these markers to write each part to a separate file, and process them further. </p>
<p> <code>Detailed technical notes:</code> </p>
<p> 1. <tt>%begin</tt>{latexonly} and <tt>%end</tt>{latexonly} have to be on a separate line. Anything between these tags (including the tags) is discarded. </p>
<p> 2. egin{latexonly} and nd{latexonly} have to be on a separate line. Anything between these tags (including the tags) is not expanded. </p>
<p> 3. [%\]begin{&quot;to exclude&quot;} and [%\]end{&quot;to exclude&quot;} have to be on a separate line. Anything between these tags (including the tags) is discarded. </p>
<p> 4. egin{verbatim/verbatim*} and nd{verbatim/verbatim*} have to be on a separate line. Anything between these tags (including the tags) is not expanded. </p>
<p> 5. The scope of any such tags may extend over several files. The opening tag for latexonly may occur on a different include level than the closing tag. The opening tag for verbatim/&quot;to exclude&#8221; must occur within the same file than the closing tag. </p>
<p> 6. Warnings are printed when the document has been parsed and open tags remain. </p>
<p> 7. When in a &#8220;to exclude&quot;/verbatim environment, texexpand won&#8217;t recognize <font SIZE="-1">ANY</font> command except the corresponding closing tag. There cannot be any nested constructions. This behaviour is identical to that of LaTeX. </p>
<p> 8. egin{latexonly},nd{latexonly} may be nested, whereas <tt>%begin</tt>{latexonly},%end{latexonly} may not be nested. </p>
<p> 9. A &#8220;%&#8221; tag cannot close a &#8220;\&#8221; tag, and vice versa. </p>
<p> 10. Every \<i>document</i>(class|style), 
