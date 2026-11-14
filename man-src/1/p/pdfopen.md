---
title: "pdfopen(1)"
name: "pdfopen"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfopen/"
description: "pdfopen, pdfclose – open or close a PDF file viewer"
---

<h2 class="name">NAME</h2>
<p> pdfopen, pdfclose &#8211; open or close a PDF file viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfopen </code> [ <i>options</i> ]&nbsp; [ <code>&#8211;file </code> ]&nbsp; <i>file.pdf</i><br />
 <code>pdfclose</code> [ <code>&#8211;file </code> ]&nbsp; <i>file.pdf</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help, -?</code></p>
<dd> output help and exit.</p>
<dt><code>-v, &#8211;version, -V</code></p>
<dd> output the version number and exit.</p>
<dt><code>-p &lt;n&gt;, &#8211;page &lt;n&gt;</code></p>
<dd> when starting the viewer, display page &lt;n&gt; of the document (notes: not all viewers support this feature, and even in those cases this option only has effect when the document is initially loaded). This option is over-ridden by <code>-g</code>.</p>
<dt><code>-g &lt;named destination&gt;, &#8211;goto &lt;named destination&gt;</code></p>
<dd> when starting the viewer, display the page of the document containing the named destination (notes: not all viewers support this feature, and even in those cases this option only has effect when the document is initially loaded).</p>
<dt><code>-r, &#8211;reset_focus</code></p>
<dd> after sending commands to the PDF viewer, attempt to reset the input focus to the window which had focus before the commands were sent.</p>
<dt><code>-viewer, &#8211;viewer &lt;</code><i>ar9</i>|<i>ar9-tab</i>|<i>ar8</i>|<i>ar7</i>|<i>ar5</i>|<i>xpdf</i>|<i>evince</i>&gt;</p>
<dd> use (respectively) Adobe Reader 9 (in a new window), Adobe Reader 9 (in a new tab of a running AR9, if any), Adobe Reader 8, Adobe Reader 7, Adobe Reader 5, xpdf or evince as the PDF viewer program. Adobe Reader 9 (in a new window) is the default.</dl>
<h2>RATIONALE</h2>
<p> At certain points of TeX document preparation, many people repeat a &quot;edit-compile-view&quot; cycle. Since PDF viewers such as Adobe&#8217;s Acrobat Reader (&quot;<code>acroread</code>&quot;) do not automatically refresh the display when the PDF file changes, this cycle can be more cumbersome than desired. The <code>pdfopen</code> program provides the ability to automate the reloading of the PDF document when it is changed. </p>
<p> Note: there seems to be little need for <code>pdfclose</code> under GNU/Linux, since (unlike the situation for MS windows) <code>acroread</code> does not lock the PDF file, which would prevent <code>pdftex</code> (or a DVI to PDF converter) from creating a new version of the PDF output file. However, <code>pdfclose</code> is provided in case someone finds it useful.</p>
<h2>DESCRIPTION</h2>
<p> <code>pdfopen</code> searches for an instance of the specified (or default) PDF viewer displaying the specified PDF file. If there is already an instance of the given viewer displaying the given file, the viewer is instructed to reload the file. If no such instance is found, <code>pdfopen</code> attempts to run the specified viewer on the specified document. </p>
<p> The default viewer is &quot;<code>acroread</code>&quot;, which could start any one of a number of versions of Acrobat Reader, depending on what is installed on your system. However, the commands to reload the current document vary from one version of <code>acroread</code> to another; consequently, if you are using a version of <code>acroread</code> other than AR9, you should explicitly specify the viewer program. </p>
<p> This version of <code>pdfopen</code> accepts the following viewer options:<br />
 <i>ar9</i>, <i>ar9-tab</i>, <i>ar8</i>, <i>ar7</i>, <i>ar5</i>, <i>xpdf</i>, and <i>evince</i>.<br />
 The difference between <i>ar9</i> and <i>ar9-tab</i> is significant when there is no instance of AR9 already displaying the requested document. In this situation, while <i>ar9</i> will request <code>acroread</code> to create a new instance of <code>acroread</code> (and thus open a new window) by using the <code>-openInNewInstance</code> argument, <i>ar9-tab</i> starts <code>acroread</code> without this argument; if there is already an instance of <code>acroread</code> running, a new tab will be opened in an existing window. </p>
<p> <code>pdfclose</code> searches for one of the above PDF viewers displaying the given file and instructs the viewer to &quot;close&quot; the window. In most cases, the PDF viewer continues to run, possibly now displaying just a blank window. (This behaviour varies somewhat from one PDF viewer to another.)</p>
<h2>PORTABILITY AND AVAILABILITY</h2>
<p> These programs have been tested on Slackware64 Version 14.1 and a few other versions / distributions of GNU/Linux. The code is reasonably generic and should work out of the box using most recent X11 implementations. (Reports to the contrary are welcome, particularly if they come with robust fixes.) </p>
<p> These programs are designed for X11-based systems. If you somehow find compiled versions of these programs on a system using another window system, they are very unlikely to be of any use to you. </p>
<p> Source and binaries of the programs can be downloaded from <tt>CTAN://support/xpdfopen/</tt> (e.g., <tt><a rel="nofollow" href="http://mirror.ctan.org/support/xpdfopen">http://mirror.ctan.org/support/xpdfopen</a></tt>).</p>
<h2>CAVEATS</h2>
<p> If you use <i>ar9-tab</i> to reload the PDF document and the instance of <code>acroread</code> with the given document is currently displaying some other document, the command causes your document to be displayed, but not reloaded. </p>
<p> <code>pdfopen</code> works by looking for a window with a name (window title) matching that expected for the given viewer and document. If for some reason your viewer&#8217;s window name is not as expected, <code>pdfopen</code> may not work for you. </p>
<p> With at least AR9 and some window managers, using <code>pdfopen</code> to reload the document gives focus to the <code>acroread</code> window, even though the mouse cursor is not necessarily in that window. This can be annoying. The <code>-reset_focus</code> option can be used to deal with this problem.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Jim Diamond &lt;<tt>Jim.Diamond [at] acadiau.ca</tt>&gt;. I am the current maintainer of the X11 versions of <code>pdfopen</code> and <code>pdfclose</code>. Report any bugs you find to me. Feature enhancement requests are welcome, coded enhancements even more so. </p>
<p> Past authors: Fabrice Popineau wrote the MS-windows versions of <code>pdfopen</code> and <code>pdfclose</code> upon which these programs were originally based. Taco Hoekwater created the GNU/Linux versions, up to Version 0.61 (including some documentation which inspired parts of this man page). Peter Breitenlohner has contributed both code and suggestions to versions later than 0.61. </p>
<h2>Index</h2>
