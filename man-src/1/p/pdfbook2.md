---
title: "pdfbook2(1)"
name: "pdfbook2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfbook2/"
description: "pdfbook2 – transform pdf files into booklets for double-sided printing"
---

<h2 class="name">NAME</h2>
<p> pdfbook2 &#8211; transform pdf files into booklets for double-sided printing</p>
<h2>SYNOPSIS</h2>
<p> <code>pdfbook2</code> [ <i>options</i> ] <i>INPUT</i> [ <i>INPUT</i>, &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Create print-ready PDF files from some <i>INPUT</i> PDF files for booklet printing. The resulting files need to be printed in landscape/long edge double sided printing. The default paper format depends on the locale and is choosen by pdfjam. It can be set with the &#8211;paper option. </p>
<p> Before the pdf is composed the <i>INPUT</i> file is cropped to the relevant area in order to discard unnecessary white spaces. In this process, all pages are cropped to the same dimensions. Extra margins can be defined at the edges of the booklet and in the middle where the binding occurs. </p>
<p> The <i>OUTPUT</i> is written to <i>INPUT</i>-book.pdf. Existing files will be overwritten. All input files are processed seperatly. </p>
<h2>EXAMPLE</h2>
<p> To simply <code>create a booklet</code> from input.pdf you can use </p>
<pre>
<dl><dt><dd>pdfbook2 input.pdf
</dl>
</pre>
<p> to create input-book.pdf. To select a special <code>type of paper</code> you can do </p>
<pre>
<dl><dt><dd>pdfbook2 --paper=letter input.pdf
</dl>
</pre>
<p> for letter or </p>
<pre>
<dl><dt><dd>pdfbook2 --paper=a4paper input.pdf
</dl>
</pre>
<p> for standard A4. To increase the <code>inner margin for binding</code> use </p>
<pre>
<dl><dt><dd>pdfbook2 --inner-margin=200 input.pdf
</dl>
</pre>
<p> to increase the default value of 150. You can submit <code>multiple files</code> to the script for processing like </p>
<pre>
<dl><dt><dd>pdfbook2 input1.pdf input2.pdf
</dl>
</pre>
<p> which will result in input1-book.pdf and input2-book.pdf. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show help message and exit </p>
</dl>
<h3>GENERAL</h3>
<dl>
<dt><code>-p</code>, <code>&#8211;paper</code>=<i>STR</i></p>
<dd> Format of the output paper dimensions as latex keyword (e.g. a4paper, letterpaper, legalpaper, &#8230;)</p>
<dt><code>-s</code>, <code>&#8211;short-edge</code></p>
<dd> Format the booklet for short-edge double-sided printing</p>
<dt><code>-n</code>, <code>&#8211;no-crop</code></p>
<dd> Prevent the cropping to the content area </p>
</dl>
<h3>MARGINS</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;outer-margin</code>=<i>INT</i></p>
<dd> Defines the outer margin in the booklet (default: 40)</p>
<dt><code>-i</code>, <code>&#8211;inner-margin</code>=<i>INT</i></p>
<dd> Defines the inner margin between the pages in the booklet (default: 150)</p>
<dt><code>-t</code>, <code>&#8211;top-margin</code>=<i>INT</i></p>
<dd> Defines the top margin in the booklet (default: 30)</p>
<dt><code>-b</code>, <code>&#8211;bottom-margin</code>=<i>INT</i></p>
<dd> Defines the bottom margin in the booklet (default: 30) </p>
</dl>
<h3>ADVANCED</h3>
<dl>
<dt><code>&#8211;signature</code>=<i>INT</i></p>
<dd> Define the signature for the booklet handed to pdfjam, needs to be multiple of 4 (default: 4)</p>
<dt><code>&#8211;signature*</code>=<i>INT</i></p>
<dd> Same as &#8211;signature</p>
<dt><code>&#8211;resolution</code>=<i>INT</i></p>
<dd> Resolution used by ghostscript in bp (default: 72) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfbook/">pdfbook</a></code>(1), <code><a href="/docs/linux/man/1-pdfjam/">pdfjam</a></code>(1), <code><a href="/docs/linux/man/1-pdfcrop/">pdfcrop</a></code>(1) </p>
<h2>ABOUT</h2>
<p> pdfbook2 v1.4 (<a rel="nofollow" href="https://github.com/jenom/pdfbook2)">https://github.com/jenom/pdfbook2)</a><br />
 (c) 2015 &#8211; 2020 Johannes Neumann (<a rel="nofollow" href="http://www.neumannjo.de)">http://www.neumannjo.de)</a><br />
 licensed under GPLv3 (<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0)">http://www.gnu.org/licenses/gpl-3.0)</a><br />
 based on pdfbook by David Firth with help from Marco Pessotto </p>
<h2>LICENSE</h2>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<h2>Index</h2>
