---
title: "chkdvifont(1)"
name: "chkdvifont"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chkdvifont/"
description: "chkdvifont – CHecK DVI/tfm/font file and tell informations of FONTs"
---

<h2 class="name">NAME</h2>
<p> chkdvifont &#8211; CHecK DVI/tfm/font file and tell informations of FONTs </p>
<h2>SYNOPSIS</h2>
<p> <code>chkdvifont</code> [<code>-s</code>] [<code>-c</code>] [<code>-{f|F}</code><i>&lt;font_data_file&gt;</i>] [<code>-d</code>] <i>dvi_file_name</i> </p>
<p> <code>chkdvifont</code> [<code>-s</code>] [<code>-c</code>] [<code>-{f|F}</code><i>&lt;font_data_file&gt;</i>] [<code>-t</code>] <i>tfm_file_name</i> </p>
<p> <code>chkdvifont</code> [<code>-s</code>] [<code>-c</code>] [<code>-{f|F}</code><i>&lt;font_data_file&gt;</i>] [<code>-p</code>] <i>font_file_name</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Chkdvifont</code> is a utility to check DVI and other TeX font-related formats (such as TFM, VF, GF and PK) and print information of those fonts. There are 3 modes; </p>
<p> Option <code>-d</code>: force DVI mode </p>
<p> Option <code>-t</code>: force TFM/OFM mode </p>
<p> Option <code>-p</code>: force other FONT mode </p>
<p> By default, the mode is guessed from the file extension.</p>
<h2>EXAMPLE</h2>
<dl>
<dt>(1) If you want to know what font is used in sample.dvi,</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;chkdvifont sample.dvi<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dvi file name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;sample.dvi<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comment&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;TeX output 2007.11.24:0632<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;factor converting to 10^{-5}m&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;25400000/473628672<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;magnification&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;1000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maximum width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;26083328 scaled points&nbsp;=&nbsp;398 points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maximum height+depth&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;11099063 scaled points&nbsp;=&nbsp;169 points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maximum stack depth&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;number of pages&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;13<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;page size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;14.0 cm x&nbsp;<wbr>&nbsp;6.0 cm<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;page size magnificated&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;14.0 cm x&nbsp;<wbr>&nbsp;6.0 cm </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Font 14<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checksum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;44D3ED74<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;design size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;1132462 scaled points&nbsp;=&nbsp;17 points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;space size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;1630536 scaled points&nbsp;=&nbsp;24 points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;magnification&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;+magstep2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;font name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;cmr17 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Font 7<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checksum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;4BF16079<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;design size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;655360 scaled points&nbsp;=&nbsp;10 points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;space size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;655360 scaled points&nbsp;=&nbsp;10 points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;font name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;cmr10 </p>
<dt>(2) If you want to know the brief summary of jis.tfm,</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;chkdvifont jis.tfm<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;jis&quot;&nbsp;is a jfm file :&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;-&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;5<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checksum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;00000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;design size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;10485760 2^{-20}&nbsp;points&nbsp;=&nbsp;10 points </p>
<dt>(3) If you want to know what font is referred to by jis.vf,</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;chkdvifont jis.vf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;jis.vf&quot;&nbsp;is in VF format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checksum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;00000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;design size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;10485760 2^{-20}&nbsp;points&nbsp;=&nbsp;10 points </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mapped Font 1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;font dsize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;10485760 2^{-20}&nbsp;points&nbsp;=&nbsp;10 points<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;font at&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;0.962216<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;font name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;rml </p>
</dl>
<p> Listing the fonts used in a DVI file (as shown in the first example) is almost equivalent to <code>dvifontlist</code> in TeX-Guy package &lt;<a rel="nofollow" href="http://www-masu.ist.osaka-u.ac.jp/%7Ekakugawa/TeX-Guy/">http://www-masu.ist.osaka-u.ac.jp/%7Ekakugawa/TeX-Guy/</a>&gt; and a script <code>dviinfox</code> &lt;<a rel="nofollow" href="https://ctan.org/pkg/dviinfox">https://ctan.org/pkg/dviinfox</a>&gt;. I don&#8217;t know any alternatives for obtaining information about TFM, OFM, VF and other font formats.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pltotf/">pltotf</a>(1), <a href="/docs/linux/man/1-tftopl/">tftopl</a>(1), <a href="/docs/linux/man/1-vptovf/">vptovf</a>(1), <a href="/docs/linux/man/1-vftovp/">vftovp</a>(1)</p>
<h2>AUTHOR</h2>
<p> The program <code>chkdvifont</code> (original name &quot;chkfont&quot;) is derived from the DVIOUT package (DVI previewer for Windows) by Toshio OSHIMA (&quot;SHIMA&quot;), Yoshiki OTOBE, and Kazunori ASAYAMA. Current version is maintained by Japanese TeX Development Community &lt;<a rel="nofollow" href="https://texjp.org">https://texjp.org</a>&gt;.<br />
 For more information, please refer to chkdvifont-ja.txt (in Japanese) on our GitHub repository, &lt;<a rel="nofollow" href="https://github.com/texjporg/tex-jp-build">https://github.com/texjporg/tex-jp-build</a>&gt; (under source/texk/dviout-util directory). </p>
<h2>Index</h2>
