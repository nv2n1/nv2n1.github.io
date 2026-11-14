---
title: "mendex(1)"
name: "mendex"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mendex/"
description: "mendex – Japanese index processor"
---

<h2 class="name">NAME</h2>
<p> mendex &#8211; Japanese index processor </p>
<h2>SYNOPSIS</h2>
<p> <code>mendex</code> [-ilqrcgfEJSU] [<code>-s</code><i> sty</i>] [<code>-d</code><i> dic</i>] [<code>-o</code><i> ind</i>] [<code>-t</code><i> log</i>] [<code>-p</code><i> no</i>] [<code>-I</code><i> enc</i>] [<code>&#8211;help</code>] [<code>&#8212;</code>] [<i> idx0 idx1 idx2 &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> The program <i>mendex</i> is a general purpose hierarchical index generator; it accepts one or more input files (<i>.idx</i>; often produced by a text formatter such as LaTeX), sorts the entries, and produces an output file which can be formatted. It is almost compatible with <i>makeindex</i>, and additional feature for handling readings of kanji words is also available. The formats of the input and output files are specified in a style file. The readings of kanji words can be specified in a dictionary file. The index can have up to three levels (0, 1, and 2) of subitem nesting.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> Take input from stdin, even when index files are specified.</p>
<dt><code>-l</code></p>
<dd> Set &#8216;sort by character order&#8217;. By default, &#8216;sort by word order&#8217; is used. Details are described below.</p>
<dt><code>-q</code></p>
<dd> Quiet mode; send no message to <i>stderr</i>, except error messages and warnings.</p>
<dt><code>-r</code></p>
<dd> Disable implicit page range formation. By default, three or more successive pages are automatically abbreviated as a range (e.g. 1-5).</p>
<dt><code>-c</code></p>
<dd> Compress sequence of intermediate blanks (space(s) and/or tab(s)) into a space and ignore leading and trailing blank(s). By default, blanks in the index key are retained.</p>
<dt><code>-g</code></p>
<dd> Make Japanese index head <i>A</i>-line (<i>A, Ka, Sa, &#8230;</i>; 10 characters) of the <i>gojuon</i> table (Japanese syllabary). By default, all 48 characters in the <i>gojuon</i> table are used.</p>
<dt><code>-f</code></p>
<dd> Force to output Kanji characters even non-existent in dictionaries.</p>
<dt><code>-s</code><i> sty</i></p>
<dd> Employ <i>sty</i> as the style file.</p>
<dt><code>-d</code><i> dic</i></p>
<dd> Employ <i>dic</i> as the dictionary file. The dictionary file is composed of lists of &lt;<i>index_word</i>&nbsp;<i>reading</i>&gt;.</p>
<dt><code>-o</code><i> ind</i></p>
<dd> Employ <i>ind</i> as the output index file. By default, the file name is created by appending the extension <i>ind</i> to the base name of the first input file.</p>
<dt><code>-t</code><i> log</i></p>
<dd> Employ <i>log</i> as the transcript file. By default, the file name is created by appending the extension <i>ilg</i> to the base name of the first input file.</p>
<dt><code>-p</code><i> no</i></p>
<dd> Set the starting page number of the output index list to be <i>no</i>. The argument <i>no</i> may be numerical or one of the following: <i>any</i> (the next page to the end of contents), <i>odd</i> (the next odd page to the end of contents), <i>even</i> (the next even page to the end of contents).</p>
<dt><code>-E</code></p>
<dd> Set input/output character encoding to EUC-JP.</p>
<dt><code>-J</code></p>
<dd> Set input/output character encoding to JIS (ISO-2022-JP).</p>
<dt><code>-S</code></p>
<dd> Set input/output character encoding to Shift_JIS.</p>
<dt><code>-U</code></p>
<dd> Set input/output character encoding to UTF-8.</p>
<dt><code>-I</code><i> enc</i></p>
<dd> Set internal character encoding to <i>enc</i>. The argument <i>enc</i> may be <i>euc</i> (EUC-JP) or <i>utf8</i> (UTF-8). The default is set to <i>utf8</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8212;</code></p>
<dd> Arguments after <code>&#8212;</code> are not taken as options. This is useful when the input file name starts with &#8216;-&#8216;. </p>
</dl>
<h2>STYLE FILE</h2>
<p> The style file informs <i>mendex</i> about the format of the <i>idx</i> input files and the intended format of the final output file. The format is upper compatible with the one for <i>makeindex</i>. The style file contains a list of &lt;<i>specifier</i>&nbsp;<i>attribute</i>&gt; pairs. There are two types of specifiers: input and output. Pairs do not have to appear in any particular order. A line begun by &#8216;%&#8217; is a comment. </p>
<p> <code>Input file style parameter</code></p>
<dl>
<dt><code>keyword</code> &lt;string&gt;</p>
<dd> &quot;\indexentry&quot;</p>
<dl>
<dt>
<dd> Command with an argument of index entry which is going to be processed.</dl>
<dt><code>arg_open</code> &lt;char&gt;</p>
<dd> &#8216;{&#8216;</p>
<dl>
<dt>
<dd> Opening delimiter which shows the beginning of index entry.</dl>
<dt><code>arg_close</code> &lt;char&gt;</p>
<dd> &#8216;}&#8217;</p>
<dl>
<dt>
<dd> Closing delimiter which shows the end of index entry.</dl>
<dt><code>range_open</code> &lt;char&gt;</p>
<dd> &#8216;(&#8216;</p>
<dl>
<dt>
<dd> Opening delimiter which shows the beginning of page range.</dl>
<dt><code>range_close</code> &lt;char&gt;</p>
<dd> &#8216;)&#8217;</p>
<dl>
<dt>
<dd> Closing delimiter which shows the end of page range.</dl>
<dt><code>level</code> &lt;char&gt;</p>
<dd> &#8216;!&#8217;</p>
<dl>
<dt>
<dd> Delimiter which shows lower level.</dl>
<dt><code>actual</code> &lt;char&gt;</p>
<dd> &#8216;@&#8217;</p>
<dl>
<dt>
<dd> Symbol which shows the next sequence is to appear as index strings in the output file.</dl>
<dt><code>encap</code> &lt;char&gt;</p>
<dd> &#8216;|&#8217;</p>
<dl>
<dt>
<dd> Symbol which shows the next sequence is to be used as command name attached to the page number.</dl>
<dt><code>page_compositor</code> &lt;string&gt;</p>
<dd> &quot;-&quot;</p>
<dl>
<dt>
<dd> Separator between page levels for a style with multi-levels of page numbers.</dl>
<dt><code>page_precedence</code> &lt;string&gt;</p>
<dd> &quot;rnaRA&quot;</p>
<dl>
<dt>
<dd> Priority of expression for page number. &#8216;R&#8217; and &#8216;r&#8217; correspond to Roman. &#8216;n&#8217; corresponds to arabic numeral. &#8216;A&#8217; and &#8216;a&#8217; correspond to Latin alphabet.</dl>
<dt><code>quote</code> &lt;char&gt;</p>
<dd> &#8216;&quot;&#8217;</p>
<dl>
<dt>
<dd> Escape character for <i>mendex</i> parameters.</dl>
<dt><code>escape</code> &lt;char&gt;</p>
<dd> &#8216;\&#8217;</p>
<dl>
<dt>
<dd> Escape character for general scripts.</dl>
<p> <code>Output file style parameter</code></p>
<dt><code>preamble</code> &lt;string&gt;</p>
<dd> &quot;\begin{theindex}
&quot;</p>
<dl>
<dt>
<dd> Preamble of output file.</dl>
<dt><code>postamble</code> &lt;string&gt;</p>
<dd> &quot;

\end{theindex}
&quot;</p>
<dl>
<dt>
<dd> Postamble of output file.</dl>
<dt><code>setpage_prefix</code> &lt;string&gt;</p>
<dd> &quot;
 \setcounter{page}{&quot;</p>
<dl>
<dt>
<dd> Prefix of page number if start page is designated.</dl>
<dt><code>setpage_suffix</code> &lt;string&gt;</p>
<dd> &quot;}
&quot;</p>
<dl>
<dt>
<dd> Suffix of page number if start page is designated.</dl>
<dt><code>group_skip</code> &lt;string&gt;</p>
<dd> &quot;

 \indexspace
&quot;</p>
<dl>
<dt>
<dd> Strings to insert vertical space before new section of index.</dl>
<dt><code>lethead_prefix</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> Prefix of heading for newly appeared heading letter.</dl>
<dt><code>heading_prefix</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> Same as <code>lethead_prefix</code>. (compatible with makeindex)</dl>
<dt><code>lethead_suffix</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> Suffix of heading for newly appeared heading letter.</dl>
<dt><code>heading_suffix</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> Same as <code>lethead_suffix</code>. (compatible with makeindex)</dl>
<dt><code>lethead_flag</code> &lt;number&gt;</p>
<dd> 0</p>
<dl>
<dt>
<dd> Flag to control output of heading letters. &#8216;0&#8217;, &#8216;1&#8217; and &#8216;-1&#8217; respectively denotes no output, uppercase and lowercase.</dl>
<dt><code>heading_flag</code> &lt;number&gt;</p>
<dd> 0</p>
<dl>
<dt>
<dd> Same as <code>lethead_flag</code>. (Note: makeindex uses a different name <code>headings_flag</code>)</dl>
<dt><code>item_0</code> &lt;string&gt;</p>
<dd> &quot;
 \item &quot;</p>
<dl>
<dt>
<dd> Command sequence inserted between primary level entries.</dl>
<dt><code>item_1</code> &lt;string&gt;</p>
<dd> &quot;
 \subitem &quot;</p>
<dl>
<dt>
<dd> Command sequence inserted between sub level entries.</dl>
<dt><code>item_2</code> &lt;string&gt;</p>
<dd> &quot;
 \subsubitem &quot;</p>
<dl>
<dt>
<dd> Command sequence inserted between subsub level entries.</dl>
<dt><code>item_01</code> &lt;string&gt;</p>
<dd> &quot;
 \subitem &quot;</p>
<dl>
<dt>
<dd> Command sequence inserted between primaly and sub level entries.</dl>
<dt><code>item_x1</code> &lt;string&gt;</p>
<dd> &quot;
 \subitem &quot;</p>
<dl>
<dt>
<dd> Command sequence inserted between primary and sub level entries when main entry does not have page number.</dl>
<dt><code>item_12</code> &lt;string&gt;</p>
<dd> &quot;
 \subsubitem &quot;</p>
<dl>
<dt>
<dd> Command sequence inserted between sub and subsub level entries.</dl>
<dt><code>item_x2</code> &lt;string&gt;</p>
<dd> &quot;
 \subsubitem &quot;</p>
<dl>
<dt>
<dd> Command sequence inserted between sub and subsub level entries when sub level entry does not have page number.</dl>
<dt><code>delim_0</code> &lt;string&gt;</p>
<dd> &quot;, &quot;</p>
<dl>
<dt>
<dd> Delimiter string between primary level entry and first page number.</dl>
<dt><code>delim_1</code> &lt;string&gt;</p>
<dd> &quot;, &quot;</p>
<dl>
<dt>
<dd> Delimiter string between sub level entry and first page number.</dl>
<dt><code>delim_2</code> &lt;string&gt;</p>
<dd> &quot;, &quot;</p>
<dl>
<dt>
<dd> Delimiter string between subsub level entry and first page number.</dl>
<dt><code>delim_n</code> &lt;string&gt;</p>
<dd> &quot;, &quot;</p>
<dl>
<dt>
<dd> Delimiter string between page numbers commonly used for any entry level.</dl>
<dt><code>delim_r</code> &lt;string&gt;</p>
<dd> &quot;&#8211;&quot;</p>
<dl>
<dt>
<dd> Delimiter string between pages to show page range.</dl>
<dt><code>delim_t</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> Delimiter string output at the end of page number list.</dl>
<dt><code>suffix_2p</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> String to be inserted in place of <code>delim_n</code> and the next page number when the two pages are contiguous.</dl>
<p> It works only when the parameter is defined.</p>
<dt><code>suffix_3p</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> String to be inserted in place of <code>delim_r</code> and the third page number when the three pages are contiguous. The parameter is prior to <code>suffix_mp</code>.</dl>
<p> It works only when the parameter is defined.</p>
<dt><code>suffix_mp</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> String to be inserted in place of <code>delim_r</code> and the last page number when the three or more pages are contiguous.</dl>
<p> It works only when the parameter is defined.</p>
<dt><code>encap_prefix</code> &lt;string&gt;</p>
<dd> &quot;\&quot;</p>
<dl>
<dt>
<dd> Prefix for an encapsulating command when the encapsulating command is added to the page number.</dl>
<dt><code>encap_infix</code> &lt;string&gt;</p>
<dd> &quot;{&quot;</p>
<dl>
<dt>
<dd> Prefix just before the page number when the encapsulating command is added to the page number.</dl>
<dt><code>encap_suffix</code> &lt;string&gt;</p>
<dd> &quot;}&quot;.</p>
<dl>
<dt>
<dd> Suffix after the page number when the encapsulating command is added to the page number.</dl>
<dt><code>line_max</code> &lt;number&gt;</p>
<dd> 72</p>
<dl>
<dt>
<dd> Maximum number of one line. If exceed the number, lines are folded.</dl>
<dt><code>indent_space</code> &lt;string&gt;</p>
<dd> &quot; &quot;</p>
<dl>
<dt>
<dd> Space for indent which inserted to top of folded line.</dl>
<dt><code>indent_length</code> &lt;number&gt;</p>
<dd> 16</p>
<dl>
<dt>
<dd> Length of space for indent which inserted to top of folded line.</dl>
<dt><code>symhead_positive</code> &lt;string&gt;</p>
<dd> &quot;Symbols&quot;</p>
<dl>
<dt>
<dd> Strings to output as heading letter for numbers and symbols when lethead_flag or heading_flag is positive number.</dl>
<dt><code>symhead_negative</code> &lt;string&gt;</p>
<dd> &quot;symbols&quot;</p>
<dl>
<dt>
<dd> Strings to output as heading letter for numbers and symbols when lethead_flag or heading_flag is negative number.</dl>
<dt><code>symbol</code> &lt;string&gt;</p>
<dd> &quot;&quot;</p>
<dl>
<dt>
<dd> Strings to output as heading letter for numbers and symbols when symbol_flag is non zero.</dl>
<p> If specified, the option is prior to symhead_positive and symhead_negative. (Extended by mendex)</p>
<dt><code>symbol_flag</code> &lt;number&gt;</p>
<dd> 1</p>
<dl>
<dt>
<dd> Flag to output of symbol. If &#8216;0&#8217;, do not output. (Extended by mendex)</dl>
<dt><code>letter_head</code> &lt;number&gt;</p>
<dd> 1</p>
<dl>
<dt>
<dd> Flag of heading letter for Japanese Kana. If &#8216;1&#8217; and &#8216;2&#8217;, Katakana and Hiragana is used, respectively. (Extended by mendex)</dl>
<dt><code>priority</code> &lt;number&gt;</p>
<dd> 0</p>
<dl>
<dt>
<dd> Flag of sorting method for index words composed of Japanese and non-Japanese (ex. Latin scripts). If non zero, one space (U+20) is inserted between Japanese sequence and non-Japanese sequence in sorting procedure. (Extended by mendex)</dl>
<dt><code>character_order</code> &lt;string&gt;</p>
<dd> &quot;SNEJ&quot;</p>
<dl>
<dt>
<dd> Order of scripts and symbols. &#8216;S&#8217;, &#8216;N&#8217;, &#8216;E&#8217; and &#8216;J&#8217; respectively denotes symbol, numbers, English and Japanese. (Extended by mendex) Please make sure that &#8216;S&#8217; and &#8216;N&#8217; are next to each other, since <code>mendex</code> considers numbers as part of symbol.</dl>
</dl>
<h2>ABOUT JAPANESE PROCESSING</h2>
<p> <i>mendex</i> has an additional feature to simplify the procedure of handling Japanese indexes, compared to <i>makeindex</i>. Users can save the effort of manually specifying a reading for every kanji word. Japanese kanji words are usually sorted by the syllables of their readings (<i>&#8216;Yomi&#8217;</i>), which can be represented by kana (Hiragana, Katakana) scripts. <i>mendex</i> accepts index words specified in kana expression directly on an input file, and also accepts conversion from index words to kana scripts by referring to Japanese dictionaries. </p>
<p> Examples of internal simplification of syllables are shown below. </p>
<dl>
<dt>
<dd>
 かぶしきがいしゃ<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>かふしきかいしや</p>
<p> マッキントッシュ<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>まつきんとつしゆ</p>
<p> ワープロ<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>わあふろ
</dl>
<p> The dictionary file consists of list with &lt;&#8216;index_word&#8217; &#8216;reading&#8217;&gt;. The index word can be written in any scripts (kanji, kana, etc), and the reading must be in Hiragana or Katakana scripts. The delimiter between the index word and its reading is one or more tab(s) or space(s). An example of a Japanese dictionary is shown below. </p>
<dl>
<dt>
<dd>
 漢字<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>かんじ</p>
<p> 読み<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>よみ</p>
<p> 環境<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>かんきょう</p>
<p> α<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>アルファ
</dl>
<p> Here, each index word is allowed to have only one Yomi. Though some kanji words (ex. 「表」) may have more than one Yomi&#8217;s (ex. 「ひょう」 and 「おもて」), only one of them can be registered in the dictionary. When some different Yomi&#8217;s are needed, they should be specified explicitly in kana expression (ex. \index{ひょう@表} or \index{おもて@表}) on the input file. Moreover, a dictionary file is automatically referred by setting the file name at an environment variable <i>INDEXDEFAULTDICTIONARY</i>. The dictionary set by the environment variable can be used together with file(s) specified by <i>-d</i> option. </p>
<h2>ABOUT SORTING PROCEDURE</h2>
<p> <i>mendex</i> sorts indexes as is (&#8216;sort by word order&#8217;) by default. Setting <i>-l</i> option, spaces between words in an index are truncated prior to sorting procedure (&#8216;sort by character order&#8217;). Even when sort by character order, the index at output remains the original sequence without the truncation. Follows show an example. </p>
<dl>
<dt>
<dd> <i>sort by word order<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>sort by character order</i></p>
<p> X Window<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Xlib</p>
<p> Xlib<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>XView</p>
<p> XView<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>X Window
</dl>
<p> In addition, two sorting methods can be applied for indexes which contains both Japanese kana and other scripts (e.g. Latin script). By setting <i>priority</i> 0 (default) and 1 at a style file, a space between Japanese Kana and other scripts is inserted and not inserted respectively, prior to the sorting procedure. Follows show an example. </p>
<dl>
<dt>
<dd> <i>priority=0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>priority=1</i></p>
<p> index sort<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>indファイル</p>
<p> indファイル<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>index sort
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <i>mendex</i> refers environment variables as follows. </p>
<dl>
<dt><i>INDEXSTYLE</i></p>
<dd> Directory where index style files exist.</p>
<dt><i>INDEXDEFAULTSTYLE</i></p>
<dd> Index style file to be referred to as default.</p>
<dt><i>INDEXDICTIONARY</i></p>
<dd> Directory where dictionary files exist.</p>
<dt><i>INDEXDEFAULTDICTIONARY</i></p>
<dd> Dictionary file which is automatically read.</dl>
<h2>DETAIL</h2>
<p> Detailed specification is compatible with <i>makeindex</i>. </p>
<h2>KNOWN ISSUES</h2>
<p> When plural page number expression is used, <i>.idx</i> files should be specified along with the order of page numbers. Otherwise, wrong page numbers might be output. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tex/">tex</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1), <a href="/docs/linux/man/1-makeindex/">makeindex</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Japanese TeX Development Community. </p>
<h2>Index</h2>
