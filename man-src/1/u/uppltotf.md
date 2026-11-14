---
title: "uppltotf(1)"
name: "uppltotf"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uppltotf/"
description: "ppltotf, uppltotf – Create Japanese pTeX font metric (JFM)"
---

<h2 class="name">NAME</h2>
<p> ppltotf, uppltotf &#8211; Create Japanese pTeX font metric (JFM) </p>
<h2>SYNOPSIS</h2>
<p> <code>ppltotf</code> [<i>options</i>] <i>pl_file_name</i>[<i></i><code>.pl</code>] [<i>tfm_file_name</i>[<i></i><code>.tfm</code>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>ppltotf</code> program translates a Japanese property list (JPL) file to a Japanese pTeX font metric (JFM) file. The resulting JFM file can be used with pTeX and e-pTeX. </p>
<p> The <code>uppltotf</code> program is a Unicode-enabled version of ppltotf. The resulting JFM file can be used with upTeX and e-upTeX. </p>
<p> In the following sections, we refer to these programs as <code>(u)ppltotf</code>. </p>
<p> <code>(u)ppltotf</code> is upper compatible with <code>pltotf</code>; if the input PL file is for roman fonts, it is translated into an ordinary TeX font metric (TFM) file. The difference between <code>ppltotf</code> and <code>uppltotf</code> lies in the output encoding: <code>ppltotf</code> always outputs JIS-encoded JFM; on the other hand, <code>uppltotf</code> outputs Unicode-encoded JFM by default.</p>
<h2>OPTIONS</h2>
<p> Compared to pltotf, the following option is added to <code>(u)ppltotf</code>.</p>
<dl>
<dt><code>-kanji</code><i>&nbsp;string</i></p>
<dd> Sets the input Japanese <i>Kanji</i> code. The <i>string</i> can be one of the followings: <i>euc</i>&nbsp;(EUC-JP), <i>jis</i>&nbsp;(ISO-2022-JP), <i>sjis</i>&nbsp;(Shift_JIS), <i>utf8</i>&nbsp;(UTF-8), <i>uptex</i>&nbsp;(UTF-8; <code>uppltotf</code> only).</dl>
<p> When one of <i>euc</i>, <i>jis</i>, <i>sjis</i> or <i>utf8</i> is specified, both <code>ppltotf</code> and <code>uppltotf</code> output a JIS-encoded JFM. When <i>uptex</i> is specified with <code>uppltotf</code>, it outputs a Unicode-encoded JFM.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ptex/">ptex</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> <code>(u)ppltotf</code> is maintained by Japanese TeX Development Community &lt;<a rel="nofollow" href="https://texjp.org">https://texjp.org</a>&gt;. For bug reports, open an issue at GitHub repository &lt;<a rel="nofollow" href="https://github.com/texjporg/tex-jp-build">https://github.com/texjporg/tex-jp-build</a>&gt;, or send an e-mail to &lt;issue [at] texjp.org&gt;. </p>
<p> This manual page was written by Hironobu Yamashita. </p>
<h2>Index</h2>
