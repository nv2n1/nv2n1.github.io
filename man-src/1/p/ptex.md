---
title: "ptex(1)"
name: "ptex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptex/"
description: "ptex, uptex, eptex, euptex – Japanese \"Publishing TeX\""
---

<h2 class="name">NAME</h2>
<p> ptex, uptex, eptex, euptex &#8211; Japanese &quot;Publishing TeX&quot; </p>
<h2>SYNOPSIS</h2>
<p> <code>ptex</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]</p>
<h2>DESCRIPTION</h2>
<p> pTeX (<code>ptex</code>) is a TeX engine with extensions for Japanese typesetting, including features related to line breaking rules, inter-character spacing and vertical writing. It was first developed by ASCII Corporation, in the aim of providing a Japanese TeX which can be used for commercial publishing. For pTeX, the character set available is limited to JIS X 0208, namely JIS level-1 and level-2. </p>
<p> upTeX (<code>uptex</code>) is a Unicode-enabled pTeX with extensions for better handling of CJK (Chinese, Japanese and Korean) multilingual documents. It has been developed by Takuji Tanaka since 2007. </p>
<p> e-pTeX (<code>eptex</code>) is a merge of e-TeX and pTeX. </p>
<p> e-upTeX (<code>euptex</code>) is a merge of e-TeX and upTeX. </p>
<p> In the following sections, we refer to these engines as (e-)(u)pTeX. </p>
<p> (e-)(u)pTeX&#8217;s handling of its command-line arguments is similar to that of the other TeX programs in the <i>web2c</i> implementation.</p>
<h2>OPTIONS</h2>
<p> Here we list only additions/deletions of command line options which are specific to (e-)(u)pTeX. For (u)pTeX, other options are similar to TeX. For e-(u)pTeX, other options are similar to e-TeX.</p>
<dl>
<dt>Additions (supported by ptexenc library):</p>
<dd>
<dt><code>-kanji</code><i>&nbsp;string</i></p>
<dd> Sets the input Japanese <i>Kanji</i> code. The <i>string</i> can be either <i>euc</i>&nbsp;(EUC-JP), <i>jis</i>&nbsp;(ISO-2022-JP), <i>sjis</i>&nbsp;(Shift_JIS), and <i>utf8</i>&nbsp;(UTF-8). For (e-)upTeX, <i>uptex</i> is also allowed.</p>
<dt><code>-kanji-internal</code><i>&nbsp;string</i></p>
<dd> Sets the internal <i>Kanji</i> code. The string can be either <i>euc</i>, and <i>sjis</i>. For (e-)upTeX, <i>uptex</i> is also allowed.</p>
<dt>Deletions:</p>
<dd>
<dt><code>-enc</code></p>
<dd> In this version of (e-)(u)pTeX, encTeX extensions are <i>not</i> available.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> This version of (e-)(u)pTeX is maintained by Japanese TeX Development Community &lt;<a rel="nofollow" href="https://texjp.org">https://texjp.org</a>&gt;. For bug reports, open an issue at GitHub repository &lt;<a rel="nofollow" href="https://github.com/texjporg/tex-jp-build">https://github.com/texjporg/tex-jp-build</a>&gt;, or send an e-mail to &lt;issue [at] texjp.org&gt;. </p>
<p> This manual page was written by Hironobu Yamashita. </p>
<h2>Index</h2>
