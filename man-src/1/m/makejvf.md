---
title: "makejvf(1)"
name: "makejvf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makejvf/"
description: "makejvf – Make Japanese VF file from Japanese TeX TFM file"
---

<h2 class="name">NAME</h2>
<p> makejvf &#8211; Make Japanese VF file from Japanese TeX TFM file </p>
<h2>SYNOPSIS</h2>
<p> <code>makejvf</code> [&lt;<i>options</i>&gt;] &lt;<i>TeX TFM file</i>&gt; &lt;<i>PS font TFM</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>makejvf</code> is a tool to generate Japanese VF file from Japanese TeX TFM (JFM) file for use with dvips.</p>
<dl>
<dt>When processing Japanese texts, pTeX refers to JFM (min10.tfm, jis.tfm etc.), which includes definitions of some different character widths and metric glue/kerns. For most punctuations and quotation marks, the character widths are truncated to less than 1 zw (zenkaku-width; the width of ordinary Kanji characters), and metric glue/kerns are inserted as a substitute.</p>
<dd>
<dt>On the other hand, in Japanese PS fonts, all punctuations and quotation marks have the same character widths as ordinary Kanji characters. For this reason, when dvips processes the resulting DVI, these characters have to be shifted to the left by the amount of glue/kerns inserted.</p>
<dd>
<dt>To achieve this, Virtual fonts (VF) and PS TFM files are required; When VF contains the commands of shifting characters, PS font TFM can have the exact character widths of PS fonts.</p>
<dd>
<dt>The program <code>makejvf</code> can be used for this purpose. It inputs a pTeX JFM file (refered to as &lt;<i>TeX TFM file</i>&gt; in <code>SYNOPSIS</code> above), and outputs a corresponding VF file (with the same basename as &lt;<i>TeX TFM file</i>&gt;) and a JFM file for a PS font JFM file (&lt;<i>PS font TFM</i>&gt; above).</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Condensed (&quot;Cho-tai&quot;) mode.</p>
<dt><code>-K</code> &lt;<i>PS-TFM</i>&gt;</p>
<dd> Map Kana (more exactly, non-Kanji) characters to another PS font JFM named &lt;<i>PS-TFM</i>&gt;.</p>
<dt><code>-b</code> &lt;<i>integer</i>&gt;</p>
<dd> Base line shift amount; the <i>integer</i> represents a relative value, using the character height as a base of 1000. When a positive integer is specified, the characters are lowered. When a negative integer is specified, the characters are raised.</p>
<dt><code>-m</code></p>
<dd> Replace single/double quotation marks (&#8216;, &#8221;) with single/double prime quotation marks (so-called &quot;minute&quot;) in vertical writing. The replacement is realized by manipulating glyphs of prime and double prime (JIS 0x216C and 0x216D; Unicode U+2032 and U+2033), <i>not</i> by putting actual glyphs designed for quotation marks (Unicode U+301D and U+301E/U+301F).</p>
<dt><code>-a</code> &lt;<i>AFMfile</i>&gt;</p>
<dd> Name of the input AFM file used for Kana-tsume mode. This option is unsupported.</p>
<dt><code>-k</code> &lt;<i>integer</i>&gt;</p>
<dd> Kana-tsume (narrower spaces between Kana characters) margin amount; the <i>integer</i> represents a relative value, using the character width as a base of 1000. This option should be accompanied with <code>-a</code> option. This option is unsupported.</p>
<dt><code>-i</code></p>
<dd> Start mapped font ID from No. 0 in output VF (by default, makejvf defaults to No. 1).</p>
<dt><code>-e</code></p>
<dd> Enhanced mode; the horizontal shift amount is determined from the glue/kern table of input JFM file.</p>
<dt>By default, <code>makejvf</code> uses the hard-coded value as the horizontal shift amount, which is (mostly) optimized for Japanese fonts. When enhanced mode (option <code>-e</code>) is enabled, the shift amount is determined from the input pTeX TFM (JFM) file, which is likely to output most suitable VF for the JFM.</p>
<dd>
<dt>For most standard Japanese JFM (like jis.tfm and its derivatives), the output VFs from both modes will have no significant difference. For simplified/traditional Chinese JFM (like upschrm-h.tfm and uptchrm-h.tfm), the output VF from enhanced mode will be better. For min10.tfm and its derivatives, enhanced mode should <i>never</i> be enabled, since the characterization in min10.tfm is non-standard.</p>
<dd>
<dt><code>-t</code> &lt;<i>CNFfile</i>&gt;</p>
<dd> Use &lt;<i>CNFfile</i>&gt; as a configuration file.</p>
<dt><code>-u</code> &lt;<i>Charset</i>&gt;</p>
<dd> UCS mode. Available charsets are: gb (GB = Simplified Chinese), cns (CNS = Traditional Chinese), ks (KS = Korean), jis (JIS = Japanese), jisq (JIS quote only), custom (user-defined CHARSET from &lt;CNFfile&gt;; see <code>CONFIGURATION FILE FORMAT</code> section).</p>
<dt>Options below are effective only in UCS mode:</p>
<dd>
<dt><code>-J</code> &lt;<i>PS-TFM</i>&gt;</p>
<dd> Map single/double quote to another JIS-encoded PSfont TFM.</p>
<dt><code>-U</code> &lt;<i>PS-TFM</i>&gt;</p>
<dd> Map single/double quote to another UCS-encoded PSfont TFM.</p>
<dt><code>-3</code></p>
<dd> Use set3, that is, enable non-BMP characters support (with UCS mode). By default <code>makejvf</code> does not output &gt;=U+10000, to reduce file size and to avoid problems with old DVI drivers. Recent versions of dvipdfmx and others can handle VF with &gt;=U+10000 (= set3 in DVI language), therefore <code>-3</code> might be helpful.</p>
<dt><code>-H</code></p>
<dd> Use half-width Katakana.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>If you want to use min10 as Ryumin-Light-H, run</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;makejvf min10.tfm rml</p>
<dt>This generates min10.vf and rml.tfm. Put these files in an appropriate directory under TEXMF tree, and add the following line to psfonts.map.</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rml Ryumin-Light-H</dl>
<h2>CONFIGURATION FILE FORMAT</h2>
<dl>
<dt>With <code>-t</code> option, you can give <code>makejvf</code> a custom settings for generating VF. The syntax is:</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;comment line<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MOVE<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&lt;code&gt;<tt>&nbsp;<wbr>&nbsp;</tt>&lt;right&gt;<tt>&nbsp;</tt>&lt;down&gt;</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REPLACE<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&lt;code&gt;<tt>&nbsp;<wbr>&nbsp;</tt>&lt;new code&gt;</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CHARSET<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&lt;code&gt;,&lt;code&gt;,&lt;code&gt;..&lt;code&gt;,&lt;code&gt;,</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+<tt>&nbsp;<wbr>&nbsp;</tt>&lt;code&gt;,&lt;code&gt;..&lt;code&gt;</p>
<dt>Each line should begin with a command, and should be TAB-separated. Line starting with % is a comment, and empty lines are ignored.</p>
<dd>
<dt>The <code>MOVE</code> command specifies horizontal/vertical shift amount for the individual character &lt;<i>code</i>&gt;. The <code>REPLACE</code> command replaces the character &lt;<i>code</i>&gt; with &lt;<i>new code</i>&gt;. The <code>CHARSET</code> command sets the custom character set of output VF; the + character continues from the previous line.</p>
<dd>
<dt>An example usage can be found in uptex-fonts project. See GitHub repository</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;<a rel="nofollow" href="https://github.com/texjporg/uptex-fonts">https://github.com/texjporg/uptex-fonts</a>&gt;.</dl>
<h2>SEE ALSO</h2>
<p> More detailed description of <code>makejvf</code> in Japanese is available at<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$TEXMFDIST/doc/fonts/ptex-fonts/README_makejvf</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Japanese TeX Development Community &lt;<a rel="nofollow" href="https://texjp.org">https://texjp.org</a>&gt;. For more information, see GitHub repository &lt;<a rel="nofollow" href="https://github.com/texjporg/ptex-fonts">https://github.com/texjporg/ptex-fonts</a>&gt;.</p>
<dl>
<dt>Many thanks to Atsuhito KOHDA &lt;kohda [at] debian.org&gt;, for providing another manpage in Debian GNU/Linux system.</p>
<dd>
</dl>
<h2>Index</h2>
