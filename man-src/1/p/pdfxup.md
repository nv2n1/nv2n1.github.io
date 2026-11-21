---
title: "pdfxup(1)"
name: "pdfxup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfxup/"
description: "pdfxup – n-up tool with reduced margins"
---

<h2>SYNOPSIS</h2>
<p> pdfxup [OPTIONS] [FILE]</p>
<h2>DESCRIPTION</h2>
<p> pdfxup creates a PDF document where each page is obtained by combining several pages of a PDF file given as output. The important feature of pdfxup, compared to similar programs, is that it tries to compute the (global) bounding box of the input PDF file, in order to remove the margins and to keep the text only. Instead of having the font size divided by 2 (for the case of 2-up output), in some case you may end up with almost the same font size as in the original document (as is the case for a default &#8216;article&#8217; document produced by LaTeX). </p>
<p> pdfxup uses ghostscript for computing the maximal bounding box of (some of) the pages of the document, and then uses pdflatex (with graphicx package) in order to produce the new document.</p>
<h2>OPTIONS</h2>
<p> pdfxup accepts numerous options. The most important ones are:</p>
<dl>
<dt><code>-x</code> m, <code>&#8211;columns</code> m</dt>
<dd> sets the number of columns of the output file (default 2);</dd>
<dt><code>-y</code> n, <code>&#8211;rows</code> n</dt>
<dd> sets the number of lines of the output file (default 1);</dd>
<dt><code>-nup</code> m<code>x</code>n, <code>&#8211;nup</code> m<code>x</code>n</dt>
<dd> sets the number of rows and columns of the output file (default 2&#215;1);</dd>
<dt><code>-l</code> (0|1), <code>&#8211;landscape</code>, <code>&#8211;portrait</code></dt>
<dd> sets orientation of paper (of final document);</dd>
<dt><code>-cf</code> file, <code>&#8211;config </code> file, <code>&#8211;mode </code> file</dt>
<dd> reads file (with extension <code>.xup</code>) and uses options defined in that file (see below for details about <code>.xup</code> files). All options are processed in the order the appear on the command-line, so that it is possible to modify the options set in the configuration file (and it is even possible to include several configuration files, the later one overwriting the options set by the previous ones). Files are looked-up using kpsewhich (if available).</dd>
<dt><code>-b</code> (le|se), <code>&#8211;booklet</code> (le|se)</dt>
<dd> configure for printing as a booklet. Value &#8216;le&#8217; (which is the default value when <code>-b</code> is used with no argument) means that two-sided printing is in &#8216;long-edge&#8217; mode (you turn from one page to the next along the long edge of the paper). &#8216;se&#8217; is the &#8216;short-edge&#8217; option.</dd>
<dt><code>-c</code>, <code>&#8211;clip</code>, <code>-nc</code>, <code>&#8211;no-clip</code></dt>
<dd> clip (or don&#8217;t clip) pages to the computed bounding box. By default, content is clipped, to avoid overlap between neighbouring pages. With <code>&#8211;no-clip</code>, anything outside the bounding box will be displayed.</dd>
<dt><code>-o</code> file, <code>&#8211;output</code> file</dt>
<dd> name of output file.</dd>
<dt><code>-i</code></dt>
<dd> ask before overwriting output file.</dd>
<dt><code>-ow</code></dt>
<dd> overwrite output file without asking.</dd>
<dt><code>-ps</code> s, <code>&#8211;paper</code> s</dt>
<dd> sets paper size (default a4). The name must be known by package geometry (more precisely, &quot;&lt;s&gt;paper&quot; should be defined in that package).</dd>
<dt><code>-fw</code> d, <code>&#8211;framewidth</code> d</dt>
<dd> width of the frame around each page (default 0.4pt). Set to 0pt to have no frame at all.</dd>
<dt><code>-tf</code> [0|1], <code>&#8211;tight-frame</code> [0|1]</dt>
<dd> whether the frame should be tight around the page, leaving horizontal white space outside the frame, or should be wide and span the whole available width.</dd>
<dt><code>-im</code> d, <code>&#8211;innermargins</code> d</dt>
<dd> inner margin between frame and page (default 5pt).</dd>
<dt><code>-m</code> d, <code>&#8211;margins</code> d</dt>
<dd> margin of pages of the new document (default 5pt).</dd>
<dt><code>-is</code> d, <code>&#8211;intspaces</code> d</dt>
<dd> space between different pages (default 1pt).</dd>
<dt><code>-p</code> list, <code>&#8211;pages</code> list</dt>
<dd> only consider sublist of pages of input document. List is a comma-separated list of pages or ranges pages of the form a-b; a can be omitted to start from first page, and b can be omitted to end at the last page. Therefore, &quot;<code>-p</code> -&quot; (which is the default) includes all pages. Also allows modulo, so that &quot;<code>-p</code> 0%2&quot; would include only even-numbered pages.</dd>
<dt><code>-bb</code> list, <code>&#8211;bb</code> list</dt>
<dd> only consider sublist of pages of input document for computing bounding box.</dd>
<dt><code>-nobb</code> list, <code>&#8211;no-bb</code> list</dt>
<dd> omit list of pages of input document from computation of bounding box.</dd>
<dt><code>-g</code>, <code>&#8211;get-bb</code></dt>
<dd> only compute (and output) bounding box. Will not produce any output file.</dd>
<dt><code>-kbb</code>, <code>&#8211;keep-bb</code></dt>
<dd> do not compute bounding box, preserve current margins.</dd>
<dt><code>-s</code> x y W H, <code>&#8211;set-bb</code> x y W H</dt>
<dd> set the bounding box to the given values. Values are in pt; the first two elements correspond to the lower left corner, while the last two represent the width and height of the part to be displayed.</dd>
<dt><code>-w</code> file, <code>&#8211;watermark</code> file</dt>
<dd> use file as background watermark. file can be any format accepted by pdflatex (e.g. png or pdf). If file is a multipage PDF file, page n of the watermark file is used with page n of the input file, and the last page of the watermark file is repeated if the input file has more pages.</dd>
<dt><code>-wp</code> p, <code>&#8211;watermark-period</code> p</dt>
<dd> repeat the last p pages of the watermark file instead of only the last one.</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> debug mode: keep intermediary files.</dd>
<dt><code>-col</code>, <code>&#8211;column-mode</code>, <code>&#8211;vertical</code></dt>
<dd> fill in pages top-down first (instead of the default left-to-right mode). By default, pages are inserted from left to right, until the line is full; with this option, pages are inserted from top to bottom, until the column is full. See option <code>-bal</code> below for examples of both options.</dd>
<dt><code>-row</code>, <code>&#8211;row-mode</code>, <code>&#8211;horizontal</code></dt>
<dd> fill in pages left to right (which is the default mode).</dd>
<dt><code>-bal</code>, <code>&#8211;balance-last</code></dt>
<dd> balance last page: when using column mode, the pages are filled in from top to bottom, and the last page is no exception. Still, it may be prefered that the columns in the last page remains &quot;balanced&quot;, which is what this option achieves. Symmetrically, in row mode, this option would balance the rows. </dd>
<pre><code>
-- -- -- -- - -- -- -- -- -row, no - balance | 1 2 3 | column, no - balance | 1 4 7 | (default mode) | 4 5 6 | | 2 5 8 | | 7 8 9 | | 3 6 9 | -- -- -- -- - -- -- -- -- - -- -- -- -- - -- -- -- -- - | 10 11 12 | | 10 13 | | 13 14 | | 11 14 | | | | 12 | -- -- -- -- - -- -- -- -- - -- -- -- -- - -- -- -- -- -row, balance | 1 2 3 | column, balance | 1 4 7 | | 4 5 6 | | 2 5 8 | | 7 8 9 | | 3 6 9 | -- -- -- -- - -- -- -- -- - -- -- -- -- - -- -- -- -- - | 10 11 | | 10 12 14 | | 12 13 | | 11 13 | | 14 | | | -- -- -- -- - -- -- -- -- -
</code></pre>
<dt><code>-V [0-3]</code>, <code>&#8211;verbose</code> [0-3]</dt>
<dd> select verbosity (default: 1).</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> run quietly (equiv. &#8216;-V 0&#8217;).</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> print version number and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> print help message and exit.</dd></dl>
<h2>CONFIGURATION FILES</h2>
<p> Configuration files (extension <code>.xup</code>) are bash scripts used to set some variables. If option &quot;<code>&#8211;config-file</code> &lt;file&gt;&quot; (or equivalent) is used, &lt;file&gt; is looked up with kpsewhich first, if it contains no &#8216;/&#8217;. If kpsewhich does not find it, then pdfxup checks if the file exists (using &#8216;test -e&#8217;) before sourcing it (the <code>PATH</code> variable will not be used to find it). </p>
<p> The script should only set some internal variables of pdfxup, such as <code>NB_ROWS</code>, <code>NB_COLUMNS</code>, <code>LANDSCAPE</code> (to set up a predefined layout). It can be used to set the bounding box, but it is often better to compute it on the first few pages of the document. Here are some examples of lines that can be put in a <code>.xup</code> file:</p>
<dl>
<dt><code>NB_COLUMNS=1</code></dt>
<dd> set the number of columns to 1</dd>
<dt><code>NB_ROWS=2</code></dt>
<dd> set the number of rows to 2</dd>
<dt><code>LANDSCAPE=0</code></dt>
<dd> set portrait mode</dd>
<dt><code>KEEP_ORIG_BBOX=1</code></dt>
<dd> do not crop margins</dd>
<dt><code>SET_BBOX=&quot;75 47 540 755&quot;</dt>
<dd> set bounding box: lower left=(75,47); upper right=(540,755)</dd>
<dt>TIGHT_FRAME=1</code></dt>
<dd> set tight frames around pages</dd>
<dt><code>INNER_MARGINS=10pt</code></dt>
<dd> set margin around each page (inside the frame) to 10pt</dd>
<dt><code>INTERM_SPACES=10pt</code></dt>
<dd> set space between pages to 10pt</dd>
<dt><code>FRAME_WIDTH=2mm</code></dt>
<dd> set frame width to 2mm </dd>
</dl>
<p> Other available variables can be found in the <code>setdefaultvalues</code> function. </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code># pdfxup file.pdf</code></dt>
<dd> produces 2-up pdf file from file.pdf.</dd>
<dt><code># pdfxup -bb 1-4 file.pdf</code></dt>
<dd> same behaviour, but computes the bounding box only using the first 4 pages (this saves time when processing long documents).</dd>
<dt><code># pdfxup -b -o booklet.pdf file.pdf</code></dt>
<dd> same behaviour, but creates a booklet (as booklet.pdf).</dd>
<dt><code># pdfxup -kbb -x1 -y2 -l0 beamer-frames.pdf</code></dt>
<dd> arranges 2 beamer frames per page (not reducing margins).</dd>
<dt><code># pdfxup &#8211;mode beamer2 beamer-frames.pdf</code></dt>
<dd> arranges PDF pages according to beamer2.xup configuration file.</dd>
<dt><code># pdfxup -kbb -x2 -y2 -l beamer-frames.pdf:1-12,15-19</code></dt>
<dd> arranges 4 beamer frames per page (not reducing margins), including only frames 1 to 12 and 15 to 19.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-pdflatex/">pdflatex</a>(1)</p>
<h2>AUTHOR</h2>
<p> Nicolas Markey (pdfxup [at] markey.fr) </p>
