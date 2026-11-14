---
title: "latex-git-log(1)"
name: "latex-git-log"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex-git-log/"
description: "latex-git-log – Generates the version history of a git project as LaTeX source code."
---

<h2 class="name">NAME</h2>
<p> latex-git-log &#8211; Generates the version history of a git project as LaTeX source code. </p>
<h2>SYNOPSIS</h2>
<p> latex-git-log [options] </p>
<p> Options: </p>
<pre><code>
--author set this if you want the author included-- startcommit set the start value of count commit-- width set the width in cm of the commit message field in the LaTeX table-- git - c - add set an base URL to link to a commit-- user set a github user to derive the base URL-- repo set a github repository to derive the base URL-- lang language of the legend and all strings in the output-- version, -v print version of this script-- help brief help message-- man full documentation
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;width</code></p>
<dd> Set the width in cm of the commit message field in the LaTeX table. If this parameter is not set then the table is not vertically limited. That means that if you have a very long commit message then the table will probably not fit on the page and you will get a &#8220;Overfull&#8221; error message from TeX. </p>
<p> In this case you should specify the width of the column containing the commit messages. I normally use something like &#8211;width=14 for <font SIZE="-1">DIN</font> A4 in landscape.</p>
<dt><code>&#8211;git-c-add</code></p>
<dd> Set an base <font SIZE="-1">URL</font> to link to a commit. This script will automatically try to use the base <font SIZE="-1">URL</font> for github.</p>
<dt><code>&#8211;lang</code></p>
<dd> Set the language of the legend and all strings in the output. Be default the language of your system is used but you can overwrite this with this parameter. </p>
<p> Currently this script only supports English and German. If you need a translation to another language then you can either create a .po file or I can register this project on one of those websites for online translation.</dl>
<h2>Example</h2>
<p> You can use it like this: </p>
<pre>
    latex-git-log --width=6 --lang=en &gt; example-output.tex
</pre>
<h2>DEPENDENCIES</h2>
<h3>Of this script</h3>
<p> This module requires these other modules and libraries: </p>
<pre>
    IPC::System::Simple
    Locale::Maketext::Simple
</pre>
<p> Everything else should already be installed.</p>
<h3>To compile the output</h3>
<p> The table is using the <code>longtable</code> package and the links to a web resource for each commit use the \href macro from <code>hyperref</code>. So these two packages have to be loaded. </p>
<p> Furthermore you need to defined the macro <code>\longtableendfoot</code> which will be expanded on the bottom of every page if the table will be continued on the next page. You can defined it to a localized message to inform the reader that this table is not complete and will be continued.</p>
<h2>DESCRIPTION</h2>
<p> <code>This program</code> will output the entire version history as table written in LaTeX if it is executed within a git repository. </p>
<p> It is intended that you redirect the standard output of this script to a file which can then be included from your main TeX document. </p>
<p> Because the table can be very large you might want to put the thing on a landscape page.</p>
<h2>Version</h2>
<p> 0.9</p>
<h2>AUTHOR</h2>
<p> Robin Schneider &lt;ypid23 [at] aol.de&gt;</p>
<h2>Development</h2>
<p> Source code repository: <a rel="nofollow" href="https://github.com/ypid/typesetting/tree/master/scripts/latex-git-log">https://github.com/ypid/typesetting/tree/master/scripts/latex-git-log</a> </p>
<p> Please report bugs and feature requests at <a rel="nofollow" href="https://github.com/ypid/typesetting/issues">https://github.com/ypid/typesetting/issues</a></p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2012-2013 by Robin Schneider </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<p> Dieses Programm ist Freie Software: Sie kA~Xnnen es unter den Bedingungen der <font SIZE="-1">GNU</font> General Public License, wie von der Free Software Foundation, Version 3 der Lizenz oder (nach Ihrer Option) jeder spA~Xteren verA~Xffentlichten Version, weiterverbreiten und/oder modifizieren. </p>
<p> Dieses Programm wird in der Hoffnung, dass es nA~Xtzlich sein wird, aber <font SIZE="-1">OHNE</font> <font SIZE="-1">JEDE</font> GEWA~XHRLEISTUNG, bereitgestellt; sogar ohne die implizite GewA~Xhrleistung der MARKTFA~XHIGKEIT oder <font SIZE="-1">EIGNUNG</font> FA~XR <font SIZE="-1">EINEN</font> <font SIZE="-1">BESTIMMTEN</font> <font SIZE="-1">ZWECK</font>. Siehe die <font SIZE="-1">GNU</font> General Public License fA~Xr weitere Details. </p>
<p> Sie sollten eine Kopie der <font SIZE="-1">GNU</font> General Public License zusammen mit diesem Programm erhalten haben. Wenn nicht, siehe &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<h2>Index</h2>
