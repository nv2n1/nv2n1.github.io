---
title: "dvispc(1)"
name: "dvispc"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvispc/"
description: "dvispc – Modify a DVI file to be page-independent in specials"
---

<h2 class="name">NAME</h2>
<p> dvispc &#8211; Modify a DVI file to be page-independent in specials </p>
<h2>SYNOPSIS</h2>
<p> <code>dvispc</code> [<code>-c</code>] [<code>-bvz</code>] <i>input_dvi_file</i> [<i>output_dvi_file</i>] </p>
<p> <code>dvispc -d</code> <i>input_dvi_file</i> </p>
<p> <code>dvispc -s</code> [<code>-p..</code>] <i>input_dvi_file</i> [<i>output_text_file</i>] </p>
<p> <code>dvispc -a</code> [<code>-ltv</code>] [<code>-J..</code>] [<code>-p..</code>] [<code>-r..</code>] <i>input_dvi_file</i> [<i>output_text_file</i>] </p>
<p> <code>dvispc -x[..]</code> [<code>-ltv</code>] [<code>-r..</code>] [<i>input_text_file</i>] <i>output_dvi_file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Dvispc</code> is a utility to modify/edit TeX DVI file with the following features: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mode option&nbsp;<code>-c</code>&nbsp;(default):<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;correct an input DVI to be page-independent in specials&nbsp;(default) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mode option&nbsp;<code>-d</code>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dry run to check if an input DVI is page-independent in specials </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mode option&nbsp;<code>-s</code>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;show all specials in the input DVI </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mode option&nbsp;<code>-a</code>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;translate DVI into a Text&nbsp;(like&nbsp;<code>dv2dt</code>&nbsp;in dtl) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mode option&nbsp;<code>-x</code>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;translate Text into a DVI&nbsp;(like&nbsp;<code>dt2dv</code>&nbsp;in dtl) </p>
<p> (1) The <i>main</i> feature of <code>dvispc</code> is the first one, to make a page-independent DVI file. </p>
<p> A &quot;pure&quot; DVI file must be actually page-independent. However in recent years, DVI files with lots of \special&#8217;s (color, annotation etc.) are commonly used, and they are not always page-independent. In such case, for example, <code>dviselect</code> or <code>dvidvi</code> fails to preserve \special&#8217;s (e.g. page color might be lost). </p>
<p> The program <code>dvispc</code> corrects such page-&quot;dependent&quot; DVI files to be page-independent, which can be safely processed by <code>dviselect</code> or <code>dvidvi</code> and then properly converted to other formats such as PostScript and PDF. </p>
<p> (2) To know whether such a correction is needed or not, <code>dvispc -d</code> will suffice. </p>
<p> (3) The mode <code>-s</code> lists all specials found in the input DVI as-is, with a preceding number which denotes the page where it appears. For example, </p>
<dl>
<dt>
<dd> [1]<br />
 {color push Black}<br />
 {color pop}<br />
 {color push rgb 1 0 0}<br />
 {color pop}<br />
 [2]<br />
 {color push Black}<br />
 {color pop}</dl>
<p> This feature is equivalent to a program <code>dvispecials</code> in TeX-Guy package &lt;<a rel="nofollow" href="http://www-masu.ist.osaka-u.ac.jp/%7Ekakugawa/TeX-Guy/">http://www-masu.ist.osaka-u.ac.jp/%7Ekakugawa/TeX-Guy/</a>&gt; and <code>dvii -s</code> &lt;<a rel="nofollow" href="https://ctan.org/pkg/dvii">https://ctan.org/pkg/dvii</a>&gt;. </p>
<p> (4) The mode <code>-a</code> and <code>-x</code> correspond to <code>dv2dt</code> and <code>dt2dv</code> in the dtl (= DVI Text Language) package respectively. By default <code>dvispc -a</code> formats the output text in its own style, but DTL-compatible format is available with <code>-t</code> option. Also, <code>dvispc -x</code> can accept DTL-compatible text input.</p>
<h2>SUPPORTED SPECIALS</h2>
<p> Currently <code>dvispc</code> supports the followings: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dvips-compatible specials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;color push, color pop, background<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dvipdfm(x)&nbsp;specials<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pdf:bcolor, pdf:ecolor, pdf:bgcolor, pdf:bann, pdf:eann<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tpic specials:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pn </p>
<p> Other specials might be supported in the future if needed.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dviselect/">dviselect</a>(1), <a href="/docs/linux/man/1-dvidvi/">dvidvi</a>(1), <a href="/docs/linux/man/1-dvips/">dvips</a>(1), <a href="/docs/linux/man/1-dvipdfmx/">dvipdfmx</a>(1)</p>
<h2>AUTHOR</h2>
<p> The program <code>dvispc</code> is derived from the DVIOUT package (DVI previewer for Windows) by Toshio OSHIMA (&quot;SHIMA&quot;), Yoshiki OTOBE, and Kazunori ASAYAMA. Current version is maintained by Japanese TeX Development Community &lt;<a rel="nofollow" href="https://texjp.org">https://texjp.org</a>&gt;.<br />
 For more information, please refer to dvispc-en.txt (in English) and dvispc-ja.txt (in Japanese) on our GitHub repository, &lt;<a rel="nofollow" href="https://github.com/texjporg/tex-jp-build">https://github.com/texjporg/tex-jp-build</a>&gt; (under source/texk/dviout-util directory). </p>
<h2>Index</h2>
