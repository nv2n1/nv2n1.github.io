---
title: "h2root(1)"
name: "h2root"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h2root/"
description: "h2root – convert PAW HBOOK files to ROOT files"
---

<h2 class="name">NAME</h2>
<p> h2root &#8211; convert PAW HBOOK files to ROOT files </p>
<h2>SYNOPSIS</h2>
<p> <code>h2root</code> <i>file.hbook file.root [compress] [tolower] [lrecl]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>h2root</code> you can use to convert your <code>HBOOK/PAW</code> histograms or ntuples files into <code>ROOT</code> files. To use this program, you type the shell script command: </p>
<dl>
<dt>
<dd> <code>h2root</code> <i>hbookfile</i> <i>rootfile</i></dl>
<p> If you do not specify the second parameter, a file name is automatically generated for you. If <i>hbookfile</i> is of the form <i>file.hbook</i>, then the <code>ROOT</code> file will be called <i>file.root</i>. </p>
<p> This program converts <code>HBOOK</code> histograms into <code>ROOT</code> objects of the class <i>TH1F</i>. <code>HBOOK</code> profile histograms are converted into <code>ROOT</code> profile histograms (see class <i>TProfile</i>). <code>HBOOK</code> row-wise and column-wise ntuples are automatically converted to <code>ROOT</code> Trees(see <i>TTree</i>). Some <code>HBOOK</code> column-wise ntuples may not be fully converted in case one of the columns is an array with fix dimensions (eg. `var[6]&#8217;) or is a multi-dimensional array. </p>
<p> <code>HBOOK</code> integer identifiers are converted into <code>ROOT</code> named objects by prefixing the integer identifier with the letter `h&#8217; if the identifier is a positive integer and by `h_&#8217; if it is a negative integer identifier. </p>
<p> In case of row-wise or column-wise ntuples, each column is converted to a branch of a Tree. <code>Note that</code> <code>h2root</code> is able to convert <code>HBOOK</code> files containing several levels of sub-directories. <code>Once you have converted your file, you can look at it and draw</code> histograms or process ntuples using the <code>ROOT</code> interactive module. You can also use the <code>ROOT</code> browser (see <i>TBrowser</i>) to inspect this file. </p>
<p> The chapter <i>How to read a Tree</i> explains two ways to read a Tree. ROOT includes the function <i>TTree::MakeCode</i> to automatically generate the code for a skeleton analysis function. With</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>compress</code></p>
<dd> = 1 by default (use 0 for no compression)</p>
<dt><code>tolower</code></p>
<dd> = 1 by default (use 0 to keep case of column names)</p>
<dt><code>lrecl</code></p>
<dd> = 0 by default (must be specified if &gt;8092)</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <i><a href="/docs/linux/man/1-root/">root</a>(1)</i>, <i><a href="/docs/linux/man/1-g2root/">g2root</a>(1)</i></dl>
<p> and</p>
<dl>
<dt>
<dd> <i>The ROOT Users Guide</i></dl>
<p> available from the main <code>ROOT</code> website:</p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></dl>
<p> <code>h2root</code> is documented fully on</p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://root.cern.ch/root/HowtoConvert.html">http://root.cern.ch/root/HowtoConvert.html</a></i></dl>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
