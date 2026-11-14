---
title: "webquiz(1)"
name: "webquiz"
section: "1"
letter: "w"
url: "/docs/linux/man/1-webquiz/"
description: "WebQuiz: a LaTeX package for writing online quizzes –"
---

<h2 class="name">NAME</h2>
<p> WebQuiz: a LaTeX package for writing online quizzes &#8211; </p>
<p> <i>WebQuiz</i> makes it possible to use <i>LaTeX</i> to write interactive online quizzes. The quizzes are first written in <i>LaTeX</i> and then converted into HTML using <i>WebQuiz</i>, which is written in python. The conversion from <i>LaTeX</i> to HTML is done behind the scenes using <i>TeX4ht</i>. The idea is that you should be able to produce nice online quizzes using <i>WebQuiz</i> and basic knowledge of <i>LaTeX</i>. </p>
<p> <i>WebQuiz</i> is designed to be used from the command-line. For example, if <i>quiz1.tex</i> is a LaTeX file for a quiz then:</p>
<dl>
<dt><i>latex quiz1</i></p>
<dd> produces a &quot;readable&quot; DVI file for the quiz</p>
<dt><i>pdflatex quiz1</i></p>
<dd> produces a &quot;readable&quot; PDF file for the quiz</p>
<dt><i>webquiz quiz1</i></p>
<dd> creates the web page <i>quiz1.html</i> </p>
<p> If you prefer to use <i>LaTeX</i> from a GUI for <i>LaTeX</i> then it should be possible to configure it to use <i>WebQuiz</i> directly. As an example, the manual provides some details about how to do this for TeXShop.</dl>
<h2>USAGE</h2>
<dl>
<dt><code>usage: webquiz [-h] [-q] [-d] [-s] [&#8211;latex | -l | -x] [-r RCFILE]</code></p>
<dd> [-i | -e | &#8211;settings [SETTINGS]] [quiz_file [quiz_file &#8230;]] </p>
<p> A LaTeX package for writing online quizzes</p>
<dt><code>positional arguments:</code></p>
<dd> quiz_file latex quiz files</p>
<dt><code>optional arguments:</code></p>
<dd>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-q</code>,<code> &#8211;quiet</code></p>
<dd> Suppress tex4ht messages (also -qq etc)</p>
<dt><code>-d</code>,<code> &#8211;draft</code></p>
<dd> Use make4ht draft mode</p>
<dt><code>-s</code>,<code> &#8211;shell-escape</code></p>
<dd> Shell escape for tex4ht/make4ht</p>
<dt><code>&#8211;latex</code></p>
<dd> Use latex to compile document with make4ht (default)</p>
<dt><code>-l</code>,<code> &#8211;lua</code></p>
<dd> Use lualatex to compile the quiz</p>
<dt><code>-x</code>,<code> &#8211;xelatex</code></p>
<dd> Use xelatex to compile the quiz</p>
<dt><code>-r</code><i>&nbsp;RCFILE</i>,<code>&nbsp;&#8211;rcfile</code><i>&nbsp;RCFILE</i></p>
<dd> Specify location of the webquiz rc-file</p>
<dt><code>-i</code>,<code> &#8211;initialise</code>,<code> &#8211;initialize</code></p>
<dd> Install web components of webquiz</p>
<dt><code>-e</code>,<code> &#8211;edit-settings</code></p>
<dd> Edit default settings for webquiz</p>
<dt><code>&#8211;settings</code><i>&nbsp;&lt;SETTINGS&gt;</i></p>
<dd> List default settings for webquiz</dl>
<h2>INSTALLATION</h2>
<p> To use <i>WebQuiz</i> you need to have a standard <i>LaTeX</i> distribution installed, such as <i>TeXLive</i>, that includes <i>TeX4ht</i>. In addition, you need to have <i>Python3</i> installed. As <i>WebQuiz</i> uses scalable vector graphics (SVG) you should check that all of the dependencies of <i>dvisvgm</i> are installed on your system, especially if you plan on using graphics or images. </p>
<p> Once the TeX components of <i>WebQuiz</i> package have been installed you can install the web components of <i>WebQuiz</i> using the following command, which needs to be run from the command line: </p>
<p> &gt; webquiz &#8211;initialise </p>
<p> If you want to install the web components of <i>WebQuiz</i> into a system directory then you need to run this command from an administrators account, so using <i>sudo</i> on a unix-like system. For more details about the installation and configuration of <i>WebQuiz</i> please see Section 3.2 of the <i>WebQuiz</i> manual. </p>
<p> Please see the manual for more details about initialising and using <i>WebQuiz</i>.</p>
<h2>INSTALLATION FROM THE CTAN ZIPFILE</h2>
<p> On both unix-like systems (including macosx), and windows systems (using either TeXLive or MiKTeX), you can install WebQuiz by downloading the WebQuiz zip file from: <i><a rel="nofollow" href="http://mirrors.ctan.org/macros/latex/contrib/webquiz.zip">http://mirrors.ctan.org/macros/latex/contrib/webquiz.zip</a></i> </p>
<p> To install the package, unzip this file and change directory to the webquiz/scripts subdirectory run: </p>
<p> &gt; webquiz &#8211;tex-install </p>
<p> (or webquiz.bat &#8211;text-install on windows). This commands unpacks the webquiz files into their standard locations in the TeX install tree to it should be run from an administrators account, or using sudo on a unix-like system. Roughly what this command does is the following:</p>
<dl>
<dt>&bull;</p>
<dd> It creates a symbolic link, or equivalent, to the main WebQuiz executable, which is the file webquiz.py in the scripts directory</p>
<dt>&bull;</p>
<dd> Copies the latex directory to somewhere in the TeX search path and then runs <i>mktexlsr</i> so that LaTeX and WebQuiz can find these files.</p>
<dt>&bull;</p>
<dd> Copies the python code into the TeX scripts subdirectory</p>
<dt>&bull;</p>
<dd> Copies the WebQuiz doc subdirectory into the TeX doc/latex subdirectory. </p>
<p> If you are using MiKTeX you may need to open the MiKTeX console, go to the Tasks menu and then rebuild the TeX filename database. </p>
<p> Once the files above are in place initialise WebQuiz by following the installation instructions above. </p>
<p> Mainly for development purposes, there is another undocumented command-line option for removing these files from TEXMFMAIN: </p>
<p> &gt; sudo webquiz/scripts/webquiz &#8211;tex-uninstall</dl>
<h2>SYSTEM REQUIREMENTS</h2>
<p> In order to work WebQuiz needs the following programs to be installed on your system:</p>
<dl>
<dt>&bull;</p>
<dd> An up-to-date <i>LaTeX</i> distribution, such as that provided by <i>TeXLive</i>. In particular, you need to have <i>TeX4ht</i> and <i>make4ht</i> installed. Unfortunately, since TeXLive 2018 was released there have been a significat bunber of updates to a number of packahges that <i>WebQuiz</i> uses, including updates to <i>TeX4ht</i>, <i>make4ht</i>, <i>tikz</i> and <i>pstricks</i>. For this reason, <i>it is strongly recommended that you all packages from ctan_ before using WebQuiz_</i>.</p>
<dt>&bull;</p>
<dd> <i>python3</i> As of writing python 3.7.2 is available.</p>
<dt>&bull;</p>
<dd> <i>Javascript</i></p>
<dt>&bull;</p>
<dd> If you plan to use <i>pstricks</i> with <i>WebQuiz</i>, or if you want to compile the online manual for WebQuiz, then you need to ensure that <i>ghostscript</i> and <i>dvisvgm</i> are installed and properly configured on your system. See the <i>WebQuiz</i> manual and the <i>dvisvgm</i> documentation for more details</p>
<dt>&bull;</p>
<dd> A web server. To view online quizzes you of course need a web server. As described in the <code>Installation</code> section you will also need to copy of the <i>WebQuiz</i> components onto your web server using the command: </p>
<p> &gt; webquiz &#8211;initialise</dl>
<h2>AUTHORS</h2>
<p> The LaTeX component of <i>WebQuiz</i> was written by Andrew Mathas and the python, css and javascript code was written by Andrew Mathas (and Don Taylor), based on an initial protype of Don Taylor&#8217;s from 2001. Since 2004 the program has been maintained and developed by Andrew Mathas. Although the program has changed substantially since 2004 Don&#8217;s idea of using <i>TeX4ht</i>, and some of his code, is still very much in use. </p>
<p> Copyright (C) 2004-2019</p>
<h2>LICENSE</h2>
<p> GNU General Public License, Version 3, 29 June 2007 </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU_General Public License (<i>GPL</i>) as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
