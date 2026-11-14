---
title: "purifyeps(1)"
name: "purifyeps"
section: "1"
letter: "p"
url: "/docs/linux/man/1-purifyeps/"
description: "purifyeps – make an Encapsulated PostScript file work with both dvips and pdflatex"
---

<h2 class="name">NAME</h2>
<p> purifyeps &#8211; make an Encapsulated PostScript file work with both dvips and pdflatex </p>
<h2>SYNOPSIS</h2>
<p> purifyeps <code>&#8211;help</code> </p>
<p> purifyeps <code>&#8211;version</code> </p>
<p> purifyeps [<code>&#8211;fontmap</code>=<i>.fmp file</i>] [<i>.eps input file</i> [<i>.eps output file</i>]] </p>
<p> purifyeps <code>&#8211;make-man</code>[=<i>filename</i>] [<code>&#8211;section</code>=<i>section</i>] </p>
<p> purifyeps <code>&#8211;make-ps-man</code>[=<i>filename</i>] [<code>&#8211;section</code>=<i>section</i>]</p>
<h2>DESCRIPTION</h2>
<p> While <code>pdflatex</code> has a number of nice features, its primary shortcoming relative to standard <code>latex</code>+<code>dvips</code> is that it is unable to read ordinary Encapsulated PostScript (<font SIZE="-1">EPS</font>) files, the most common graphics format in the LaTeX world. <code>pdflatex</code> can read only the following types of graphics files:</p>
<dl>
<dt><font SIZE="-1">PDF</font></p>
<dd> Most people who use <code>pdflatex</code> convert their documents to <font SIZE="-1">PDF</font> using a utility such as <code>epstopdf</code>. This works well and preserves the vector nature of the original <font SIZE="-1">EPS</font>. Unfortunately, <code>dvips</code> does not read <font SIZE="-1">PDF</font>, so two versions of the graphic must be maintained if the document is to be processed with both <code>latex</code>+<code>dvips</code> and <code>pdflatex</code>.</p>
<dt><font SIZE="-1">PNG</font></p>
<dd> <font SIZE="-1">PNG</font> is a bitmap format and therefore scales poorly. Also, <code>dvips</code> does not read <font SIZE="-1">PNG</font>, so two versions of the graphic must be maintained if the document is to be processed with both <code>latex</code>+<code>dvips</code> and <code>pdflatex</code>.</p>
<dt><font SIZE="-1">JPEG</font></p>
<dd> <font SIZE="-1">JPEG</font> is a bitmap format and therefore scales poorly. Also, <code>dvips</code> does not read <font SIZE="-1">JPEG</font>, so two versions of the graphic must be maintained if the document is to be processed with both <code>latex</code>+<code>dvips</code> and <code>pdflatex</code>.</p>
<dt><font SIZE="-1">MPS</font></p>
<dd> This is probably the least-used <code>pdflatex</code>-compatible graphics format. <font SIZE="-1">MPS</font> is actually a stylized version of <font SIZE="-1">EPS</font> that MetaPost outputs. Like <font SIZE="-1">PDF</font>, <font SIZE="-1">MPS</font> is a vector format and remains as such when imported into a <code>pdflatex</code> document. Also like <font SIZE="-1">PDF</font>, <code>dvips</code> does not read <font SIZE="-1">MPS</font>, so two versions of the graphic must be maintained if the document is to be processed with both <code>latex</code>+<code>dvips</code> and <code>pdflatex</code>.</dl>
<p> The insight behind <code>purifyeps</code> is that there are only a few, small differences between <font SIZE="-1">MPS</font> and <font SIZE="-1">EPS</font> and that a file can be converted into a format that matches both the <font SIZE="-1">MPS</font> and <font SIZE="-1">EPS</font> specifications simultaneously. <code>purifyeps</code> inputs an <font SIZE="-1">EPS</font> file, uses <code>pstoedit</code>&#8216;s <tt>&quot;mpost&quot;</tt> filter to convert the file to MetaPost (<i>.mp</i>), runs <code>mpost</code> on the file to convert it to <font SIZE="-1">MPS</font>, and finally performs some touchups on the result to convert the file back to <font SIZE="-1">EPS</font>, while preserving its ability to be parsed by <code>pdflatex</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display &#8220;Usage&#8221; and &#8220;Options&#8221; from the <code>purifyeps</code> documentation.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the <code>purifyeps</code> version number, copyright, and license.</p>
<dt><code>&#8211;fontmap</code>=<i>.fmp file</i></p>
<dd> Specify the name of a file that tells <code>purifyeps</code> how to map from TeX font names to PostScript font names. [Default: <i>mpost.fmp</i>]</p>
<dt><code>&#8211;make-man</code> [=<i>filename</i>]] [<code>&#8211;section</code>=<i>section</i>]</p>
<dd> Automatically create a Unix man page for <code>purifyeps</code>. <i>section</i> specifies the section [default: <tt>1</tt> (User Commands)]. <i>filename</i> defaults to <i>purifyeps.1</i> or an analogous filename if <i>section</i> is specified.</p>
<dt><code>&#8211;make-ps-man</code> [=<i>filename</i>]] [<code>&#8211;section</code>=<i>section</i>]</p>
<dd> Automatically create a PostScript version of the <code>purifyeps</code> documentation. The documentation is formatted like a Unix man page. <i>section</i> specifies the section [default: <tt>1</tt> (User Commands)]. <i>filename</i> defaults to <i>purifyeps.ps</i>.</dl>
<p> In normal operation (i.e., when not run with <tt>&quot;--help&quot;</tt>, <tt>&quot;--make-man&quot;</tt>, or <tt>&quot;--make-ps-man&quot;</tt>), <code>purifyeps</code> takes the name of an input file and output file. The same filename can safely be used for both files. If the output filename is omitted, output will go to the standard output device. If the input filename is omitted, <code>purifyeps</code> will read from the standard input device.</p>
<h2>EXAMPLES</h2>
<p> Create a PostScript version of the <code>purifyeps</code> documentation, but call it <i>happydoc.ps</i> instead of the default, <i>purifyeps.ps</i>: </p>
<pre>
    purifyeps --make-ps-man=happydoc.ps
</pre>
<p> Create a Unix man page for <code>purifyeps</code> (in the usual roff format), but indicate that it belongs in section <tt>&quot;LOCAL&quot;</tt> instead of the default of section <tt>1</tt>: </p>
<pre>
    purifyeps --make-man --section=LOCAL
</pre>
<p> Purify <i>sample.eps</i> (<i>mpost.fmp</i> is in the current directory): </p>
<pre>
    purifyeps sample.eps sample.eps
</pre>
<p> Purify <i>sample.eps</i> (<i>mpost.fmp</i> is in a different location): </p>
<pre>
    purifyeps --fontmap=/usr/share/pstoedit/mpost.fmp sample.eps sample.eps
</pre>
<p> Rename the purified version while purifying: </p>
<pre>
    purifyeps sample.eps sample-pure.eps
</pre>
<p> Do the same, but in a Unix pipeline: </p>
<pre>
    cat sample.eps | purifyeps &gt; sample-pure.eps
</pre>
<p> When you run <code>purifyeps</code>, you should see the output from both <code>pstoedit</code> and <code>mpost</code>, followed by a success message from <code>purifyeps</code>: </p>
<pre>
    % cat sample.eps | purifyeps &gt; sample-pure.eps
    pstoedit: version 3.30 / DLL interface 107 (build Mar 14 2002) :
    Copyright (C) 1993 - 2001 Wolfgang Glunz
    Interpreter finished. Return status 0
    This is MetaPost, Version 0.641 (Web2C 7.3.1)
    (/tmp/purifyeps-jdeGPkh9.mp [1] )
    1 output file written: purifyeps-jdeGPkh9.1
    Transcript written on purifyeps-jdeGPkh9.log.
    File seems to have been purified successfully.
</pre>
<h2>FILES</h2>
<dl>
<dt><i>mpost.fmp</i></p>
<dd> File containing mappings between TeX and PostScript font names. See &#8220;<font SIZE="-1">NOTES</font>&#8221; for a description of this file&#8217;s contents.</dl>
<h2>BUGS</h2>
<p> Error reporting could definitely stand to be improved. Error messages produced by <code>pstoedit</code> and <code>mpost</code> are sometimes silently ignored. Also, errors sometimes cause <code>purifyeps</code> to leave temporary files (<i>purifyeps-</i><i>#####</i>) lying around. </p>
<p> <code>purifyeps</code> is subject to all of the limitations that affect <code>pstoedit</code> and especially the <tt>&quot;mpost&quot;</tt> backend to <code>pstoedit</code>. As a result, <code>purifyeps</code> ignores certain PostScript constructs, such as nonuniformly scaled text.</p>
<h2>NOTES</h2>
<p> <code>purifyeps</code> needs a file that tells it how to map from TeX font names to PostScript font names. This file must contain two, space-separated columns. The first lists a PostScript font name, and the second lists the TeX equivalent. Blank lines and lines that start with <tt>&quot;%&quot;</tt> are ignored. The following is a sample <i>.fmp</i> file: </p>
<pre>
    % This is a sample font map for purifyeps.
    Times-Bold                           ptmb
    Times-Italic                         ptmri
    Times-Roman                          ptmr
    Helvetica                            phvr
    Helvetica-Bold                       phvb
    Helvetica-Oblique                    phvro
    Courier                              pcrr
    Courier-Bold                         pcrb
    Courier-Oblique                      pcrro
</pre>
<p> Note that this is exactly the same format that <code>pstoedit</code> uses. By default, <code>purifyeps</code> looks in the current directory for a font map called <i>mpost.fmp</i>. The <tt>&quot;--fontmap&quot;</tt> command-line option tells <code>purifyeps</code> to use a different font map, which will typically be the <i>mpost.fmp</i> file that comes with <code>pstoedit</code>. </p>
<p> Once you create purified <font SIZE="-1">EPS</font> files with <code>purifyeps</code>, you need to instruct <code>pdflatex</code> to use them. The pdfLaTeX configuration of the <tt>&quot;graphics&quot;</tt> and <tt>&quot;graphicx&quot;</tt> packages (<i>pdftex.def</i>) normally ignores <i>.eps</i> files. Putting the following LaTeX code in your document&#8217;s preamble tells <code>pdflatex</code> that all <i>.eps</i> files are in <font SIZE="-1">MPS</font> format: </p>
<pre><code>
% Tell pdfLaTeX that all.eps files were produced by MetaPost.
    
