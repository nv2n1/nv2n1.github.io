---
title: "jaxodraw(1)"
name: "jaxodraw"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jaxodraw/"
description: "JaxoDraw – A Program for the Interactive Generation of Feynman Diagrams"
---

<h2>NAME</h2>
<p> <code>JaxoDraw</code> &#8211; A Program for the Interactive Generation of Feynman Diagrams</p>
<h2>SYNTAX</h2>
<p> jaxodraw [<i>options</i>] [&lt;<i>file</i>&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <code>JaxoDraw</code> is a Feynman graph plotting tool written in Java. It has a complete graphical user interface that allows all actions to be carried out via mouse click-and-drag operations in a WYSIWYG fashion. Graphs may be exported to postscript / EPS format and can be saved in XML files to be used for later sessions. With JaxoDraw it becomes possible to draw even complicated Feynman diagrams with just a few mouse clicks, without the knowledge of any programming language. </p>
<p> <code>Note</code>: You need an installed and configured Java Runtime Environment (version 1.4.1 or greater) in order to run <code>JaxoDraw</code>. This may be downloaded free of charge from Sun&#8217;s web pages: <i><a rel="nofollow" href="http://java.sun.com/downloads/">http://java.sun.com/downloads/</a></i> </p>
<p> <code>Note</code>: You need to install the axodraw4j.sty LaTeX style file in order to use the LaTeX features of <code>JaxoDraw</code>. You may download it from <i><a rel="nofollow" href="http://jaxodraw.sourceforge.net/download/">http://jaxodraw.sourceforge.net/download/</a></i>. Please refer to the <code>JaxoDraw</code> User Guide for information on how to install axodraw4j. </p>
<p> <i>options</i> are a set of command line options specified below and <i>file</i> specifies the name of a file to be edited. The objects in the file will be read at the start of <code>JaxoDraw</code>. </p>
<p> Most of the documentation for <code>JaxoDraw</code> is in an HTML-based reference guide that is available via the Help menu in <code>JaxoDraw</code> or at our Web page <i><a rel="nofollow" href="http://jaxodraw.sourceforge.net/">http://jaxodraw.sourceforge.net/</a></i>.</p>
<h2>FILES</h2>
<dl>
<dt><i>~/.jaxodraw/</i></p>
<dd> Per user configuration directory where plugins and User Guide are installed, and log records are written. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To run <code>JaxoDraw</code> the standard way, just type: </p>
<p> jaxodraw </p>
<p> To read in the file <i>epscatter.xml</i> at start-up, type: </p>
<p> jaxodraw epscatter.xml</p>
<h2>BUGS</h2>
<p> See the file <i>BUGS</i> in the source distribution.</p>
<h2>OPTIONS</h2>
<p> Currently, the following command line options are supported: </p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>
 Print all command-line options for <code>JaxoDraw</code>.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints out the version number of <code>JaxoDraw</code>.</p>
<dt><code>&#8211;info</code></p>
<dd>
 Prints out some information about your system.</p>
<dt><code>&#8211;convert</code></p>
<dd>
 Used to convert a number of <code>JaxoDraw</code> xml files (given as parameters on the command line) to axodraw4j tex files (and vice versa) without the need of bringing up the user interface. Use like eg:</p>
<dt>
<dd> jaxodraw &#8211;convert test1.xml test2.tex</p>
<dt>
<dd> This converts test1.xml to test1.tex and test2.tex to test2.xml.</p>
<dt><code>-verbose</code></p>
<dd> Turns on verbose error messaging.</p>
<dt><code>-quiet</code></p>
<dd>
 Turns off verbose error messaging.</p>
<dt><code>-nosplash</code></p>
<dd>
 Do not show the splash window at start up (default is to show it).</dl>
<p> By default, all parameters starting with &#8212; do not pop up the graphical user interface of <code>JaxoDraw</code>.</p>
<h2>AUTHORS</h2>
<p> Daniele Binosi &lt;binosi [at] ect.it&gt;, Christian Kaufhold &lt;jaxodraw [at] chka.de&gt; and Lukas Theussl &lt;theussl [at] nbi.dk&gt;.</p>
<h2>ACKNOWLEDGEMENT</h2>
<p> We are grateful to Prof. Arcadi Santamaria for numerous helpful remarks and moral support during the development of <code>JaxoDraw</code>. We also acknowledge Prof. Jos Vermaseren for his kind permission to use and distribute a modified version of his axodraw style file. John Collins has pushed the development of <code>JaxoDraw</code> a huge step forward by writing the new axodraw4j style file. We would finally like to thank all the people on the <code>JaxoDraw</code> mailing list for their help and feedback during the testing phase.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2006 Daniele Binosi and Lukas Theussl.<br />
 Copyright (C) 2007-2008 Daniele Binosi, Lukas Theussl and Christian Kaufhold </p>
<p> <code>JaxoDraw</code> is published under the terms of the Gnu General Public License. Other Copyrights may be found in various files, see the file <i>LICENSE</i> in the source distribution for detailed information.</p>
<h2>SEE ALSO</h2>
<p> latex (1), tex (1), java (1), javac (1) </p>
<h2>Index</h2>
