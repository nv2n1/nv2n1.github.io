---
title: "rubber-info(1)"
name: "rubber-info"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rubber-info/"
description: "rubber-info – extract information from LaTeX documents"
---

<h2>NAME</h2>
<p> rubber-info &#8211; extract information from LaTeX documents </p>
<h2>SYNOPSIS</h2>
<p> <code>rubber-info</code> [<i>options</i>] [<i>action</i>] <i>source</i> </p>
<h2>DESCRIPTION</h2>
<p> Rubber-info is a utility for extracting various kinds of information from a LaTeX document. Information can be extracted from the source (for instance when calculating dependencies) or from the compilation log files (to extract errors and warnings). This program is a complement for the compilation system <code><a href="/docs/linux/man/1-rubber/">rubber</a></code>(1). </p>
<p> The command-line options are those used by <code><a href="/docs/linux/man/1-rubber/">rubber</a></code>(1) plus one of the actions described below. </p>
<h2>ACTIONS</h2>
<p> One of the following command-line options must be specified, to decide which information to extract. Of course, for actions that read a log file, a compilation must have been done before. If none of these actions is specified, <i>&#8211;check</i> is assumed.</p>
<dl>
<dt><code>&#8211;boxes</code></p>
<dd> Extracts from the log file the places in the source where bad boxes appeared (these are the famous overfull and underfull \hbox and box)</p>
<dt><code>&#8211;check</code></p>
<dd> Report errors if there are any, otherwise report undefined references if there are any, otherwise list warnings and bad boxes. This is the default action.</p>
<dt><code>&#8211;deps</code></p>
<dd> Analyse the source files and produce a space-separated list of all the files that the document depends on and that Rubber cannot rebuild.</p>
<dt><code>&#8211;errors</code></p>
<dd> Extract from the log file the list of errors that occured during the last compilation.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display the list of all available options and exit nicely.</p>
<dt><code>&#8211;refs</code></p>
<dd> Report the list of undefined or multiply defined references (i.e. the ef&#8217;s that are not defined by one \label).</p>
<dt><code>&#8211;rules</code></p>
<dd> Analyse the source files and produce a list of dependency rules. One rule is produced for each intermediate target that would be made when running <code>rubber</code>. Rules are formatted in the style of Makefiles.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit nicely.</p>
<dt><code>&#8211;warnings</code></p>
<dd> Stupidly enumerate all LaTeX warnings, i.e. all the lines in the log file that contain the string &quot;Warning&quot;.</dl>
<h2>BUGS</h2>
<p> There are surely a some&#8230; </p>
<p> This page documents Rubber version 1.1. The program and this man-page are maintained by Emmanuel Beffara &lt;manu [at] beffara.org&gt;. The homepage for Rubber can be found at <a rel="nofollow" href="http://www.pps.jussieu.fr/~beffara/soft/rubber/.">http://www.pps.jussieu.fr/~beffara/soft/rubber/.</a> </p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>rubber</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>rubber</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info rubber</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
