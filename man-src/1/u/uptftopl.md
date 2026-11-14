---
title: "uptftopl(1)"
name: "uptftopl"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uptftopl/"
description: "ptftopl, uptftopl – Convert Japanese pTeX font metric (JFM) files to propery list"
---

<h2 class="name">NAME</h2>
<p> ptftopl, uptftopl &#8211; Convert Japanese pTeX font metric (JFM) files to propery list </p>
<h2>SYNOPSIS</h2>
<p> <code>ptftopl</code> [<i>OPTIONS</i>] <i>tfm_name</i>[<i></i><code>.tfm</code>] [<i>pl_name</i>[<i></i><code>.pl</code>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>ptftopl</code> program translates a Japanese pTeX font metric (JFM) file to a Japanese property list (JPL) file. It also serves as a TFM/JFM-file validating program. </p>
<p> The <code>uptftopl</code> program is a Unicode-enabled version of ptftopl. </p>
<p> In the following sections, we refer to these programs as <code>(u)ptftopl</code>. </p>
<p> <code>(u)ptftopl</code> is upper compatible with <code>tftopl</code>; if the input TFM file is for roman fonts, it is translated into an ordinary property list file. The difference between <code>ptftopl</code> and <code>uptftopl</code> lies in the internal encoding: when the input is a JFM file, <code>ptftopl</code> always treats it as a JIS-encoded JFM; on the other hand, <code>uptftopl</code> treats it as a Unicode-encoded JFM by default.</p>
<h2>OPTIONS</h2>
<p> Compared to tftopl, the following option is added to <code>(u)ptftopl</code>.</p>
<dl>
<dt><code>-kanji</code><i>&nbsp;string</i></p>
<dd> Sets the output Japanese <i>Kanji</i> code. The <i>string</i> can be one of the followings: <i>euc</i>&nbsp;(EUC-JP), <i>jis</i>&nbsp;(ISO-2022-JP), <i>sjis</i>&nbsp;(Shift_JIS), <i>utf8</i>&nbsp;(UTF-8), <i>uptex</i>&nbsp;(UTF-8; <code>uptftopl</code> only).</dl>
<p> When one of <i>euc</i>, <i>jis</i>, <i>sjis</i> or <i>utf8</i> is specified, both <code>ptftopl</code> and <code>uptftopl</code> treats the input JFM as JIS-encoded. When <i>uptex</i> is specified with <code>uptftopl</code>, it treats the input JFM as Unicode-encoded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ptex/">ptex</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> <code>(u)ptftopl</code> is maintained by Japanese TeX Development Community &lt;<a rel="nofollow" href="https://texjp.org">https://texjp.org</a>&gt;. For bug reports, open an issue at GitHub repository &lt;<a rel="nofollow" href="https://github.com/texjporg/tex-jp-build">https://github.com/texjporg/tex-jp-build</a>&gt;, or send an e-mail to &lt;issue [at] texjp.org&gt;. </p>
<p> This manual page was written by Hironobu Yamashita. </p>
<h2>Index</h2>
