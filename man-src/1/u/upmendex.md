---
title: "upmendex(1)"
name: "upmendex"
section: "1"
letter: "u"
url: "/docs/linux/man/1-upmendex/"
description: "upmendex – Multilingual index processor"
---

<h2 class="name">NAME</h2>
<p> upmendex &#8211; Multilingual index processor </p>
<h2>SYNOPSIS</h2>
<p> <code>upmendex</code> [-ilqrcgf] [<code>-s</code><i> sty</i>] [<code>-d</code><i> dic</i>] [<code>-o</code><i> ind</i>] [<code>-t</code><i> log</i>] [<code>-p</code><i> no</i>] [<code>&#8212;</code>] [<i> idx0 idx1 idx2 &#8230;</i>]<br />
 <code>upmendex</code> <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> The program <i>upmendex</i> is a general purpose multilingual hierarchical index generator working with upLaTeX, XeLaTeX and LuaLaTeX; it accepts one or more input files (<i>.idx</i>; often produced by a text formatter such as LaTeX families), sorts the entries, and produces an output file which can be formatted. It supports Latin (including non-English), Greek, Cyrillic, Korean Hangul and Han (Hanzi ideographs) scripts, as well as Japanese Kana. It is almost compatible with <i>makeindex</i> and <i>mendex</i>, and additional feature for handling readings of kanji words is also available. The formats of the input and output files are specified in a style file. The readings of kanji words can be specified in a dictionary file. The index can have up to three levels (0, 1, and 2) of subitem nesting.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></dt>
<dd> Take input from stdin, even when index files are specified.</dd>
<dt><code>-l</code></dt>
<dd> Set &#8216;sort by character order&#8217;. By default, &#8216;sort by word order&#8217; is used. Details are described below.</dd>
<dt><code>-q</code></dt>
<dd> Quiet mode; send no message to <i>stderr</i>, except error messages and warnings.</dd>
<dt><code>-r</code></dt>
<dd> Disable implicit page range formation. By default, three or more successive pages are automatically abbreviated as a range (e.g. 1-5).</dd>
<dt><code>-c</code></dt>
<dd> Compress sequence of intermediate blanks (space(s) and/or tab(s)) into a space and ignore leading and trailing blank(s). By default, blanks in the index key are retained.</dd>
<dt><code>-g</code></dt>
<dd> Make Japanese index head <i>A</i>-line (<i>A, Ka, Sa, &#8230;</i>; 10 characters) of the <i>gojuon</i> table (Japanese syllabary). By default, all 48 characters in the <i>gojuon</i> table are used.</dd>
<dt><code>-f</code></dt>
<dd> Force to output characters even if the scripts are not supported by <i>upmendex</i>.</dd>
<dt><code>-s</code><i> sty</i></dt>
<dd> Employ <i>sty</i> as the style file.</dd>
<dt><code>-d</code><i> dic</i></dt>
<dd> Employ <i>dic</i> as the dictionary file. The dictionary file is composed of lists of &lt;<i>index_word</i>&nbsp;<i>reading</i>&gt;.</dd>
<dt><code>-o</code><i> ind</i></dt>
<dd> Employ <i>ind</i> as the output index file. By default, the file name is created by appending the extension <i>ind</i> to the base name of the first input file.</dd>
<dt><code>-t</code><i> log</i></dt>
<dd> Employ <i>log</i> as the transcript file. By default, the file name is created by appending the extension <i>ilg</i> to the base name of the first input file.</dd>
<dt><code>-p</code><i> no</i></dt>
<dd> Set the starting page number of the output index list to be <i>no</i>. The argument <i>no</i> may be numerical or one of the following: <i>any</i> (the next page to the end of contents), <i>odd</i> (the next odd page to the end of contents), <i>even</i> (the next even page to the end of contents).</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8212;</code></dt>
<dd> Arguments after <code>&#8212;</code> are not taken as options. This is useful when the input file name starts with &#8216;-&#8216;. </dd>
</dl>
<h2>STYLE FILE</h2>
<p> The style file informs <i>upmendex</i> about the format of the <i>idx</i> input files and the intended format of the final output file. The format is upper compatible with the one for <i>makeindex</i> and <i>mendex</i>. The style file contains a list of &lt;<i>specifier</i>&nbsp;<i>attribute</i>&gt; pairs. There are two types of specifiers: input and output. Pairs do not have to appear in any particular order. A line begun by &#8216;%&#8217; is a comment. </p>
<p> <code>Input file style parameter</code></p>
<dl>
<dt><code>keyword</code> &lt;string&gt;</dt>
<dd> &quot;\indexentry&quot;</dd>
<dl>
<dt>
</dt><dd> Command with an argument of index entry which is going to be processed.</dd></dl>
<dt><code>arg_open</code> &lt;char&gt;</dt>
<dd> &#8216;{&#8216;</dd>
<dl>
<dt>
</dt><dd> Opening delimiter which shows the beginning of index entry.</dd></dl>
<dt><code>arg_close</code> &lt;char&gt;</dt>
<dd> &#8216;}&#8217;</dd>
<dl>
<dt>
</dt><dd> Closing delimiter which shows the end of index entry.</dd></dl>
<dt><code>range_open</code> &lt;char&gt;</dt>
<dd> &#8216;(&#8216;</dd>
<dl>
<dt>
</dt><dd> Opening delimiter which shows the beginning of page range.</dd></dl>
<dt><code>range_close</code> &lt;char&gt;</dt>
<dd> &#8216;)&#8217;</dd>
<dl>
<dt>
</dt><dd> Closing delimiter which shows the end of page range.</dd></dl>
<dt><code>level</code> &lt;char&gt;</dt>
<dd> &#8216;!&#8217;</dd>
<dl>
<dt>
</dt><dd> Delimiter which shows lower level.</dd></dl>
<dt><code>actual</code> &lt;char&gt;</dt>
<dd> &#8216;@&#8217;</dd>
<dl>
<dt>
</dt><dd> Symbol which shows the next sequence is to appear as index strings in the output file.</dd></dl>
<dt><code>encap</code> &lt;char&gt;</dt>
<dd> &#8216;|&#8217;</dd>
<dl>
<dt>
</dt><dd> Symbol which shows the next sequence is to be used as command name attached to the page number.</dd></dl>
<dt><code>page_compositor</code> &lt;string&gt;</dt>
<dd> &quot;-&quot;</dd>
<dl>
<dt>
</dt><dd> Separator between page levels for a style with multi-levels of page numbers.</dd></dl>
<dt><code>page_precedence</code> &lt;string&gt;</dt>
<dd> &quot;rnaRA&quot;</dd>
<dl>
<dt>
</dt><dd> Priority of expression for page number. &#8216;R&#8217; and &#8216;r&#8217; correspond to Roman. &#8216;n&#8217; corresponds to arabic numeral. &#8216;A&#8217; and &#8216;a&#8217; correspond to Latin alphabet.</dd></dl>
<dt><code>quote</code> &lt;char&gt;</dt>
<dd> &#8216;&quot;&#8217;</dd>
<dl>
<dt>
</dt><dd> Escape character for <i>upmendex</i> parameters.</dd></dl>
<dt><code>escape</code> &lt;char&gt;</dt>
<dd> &#8216;\&#8217;</dd>
<dl>
<dt>
</dt><dd> Escape character for general scripts.</dd></dl>
<p> <code>Output file style parameter</code></p>
<dt><code>preamble</code> &lt;string&gt;</dt>
<dd> &quot;\begin{theindex}
&quot;</dd>
<dl>
<dt>
</dt><dd> Preamble of output file.</dd></dl>
<dt><code>postamble</code> &lt;string&gt;</dt>
<dd> &quot;

\end{theindex}
&quot;</dd>
<dl>
<dt>
</dt><dd> Postamble of output file.</dd></dl>
<dt><code>setpage_prefix</code> &lt;string&gt;</dt>
<dd> &quot;
 \setcounter{page}{&quot;</dd>
<dl>
<dt>
</dt><dd> Prefix of page number if start page is designated.</dd></dl>
<dt><code>setpage_suffix</code> &lt;string&gt;</dt>
<dd> &quot;}
&quot;</dd>
<dl>
<dt>
</dt><dd> Suffix of page number if start page is designated.</dd></dl>
<dt><code>group_skip</code> &lt;string&gt;</dt>
<dd> &quot;

 \indexspace
&quot;</dd>
<dl>
<dt>
</dt><dd> Strings to insert vertical space before new section of index.</dd></dl>
<dt><code>lethead_prefix</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Prefix of heading for newly appeared heading letter.</dd></dl>
<dt><code>heading_prefix</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Same as <code>lethead_prefix</code>. (compatible with makeindex)</dd></dl>
<dt><code>lethead_suffix</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Suffix of heading for newly appeared heading letter.</dd></dl>
<dt><code>heading_suffix</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Same as <code>lethead_suffix</code>. (compatible with makeindex)</dd></dl>
<dt><code>lethead_flag</code> &lt;number&gt;</dt>
<dd> 0</dd>
<dl>
<dt>
</dt><dd> Flag to control output of heading letters in Latin, Greek and Cyrillic scripts. &#8216;0&#8217;, &#8216;1&#8217;, &#8216;-1&#8217; and &#8216;2&#8217; respectively denotes no output, uppercase, lowercase and titlecase.</dd></dl>
<dt><code>heading_flag</code> &lt;number&gt;</dt>
<dd> 0</dd>
<dl>
<dt>
</dt><dd> Same as <code>lethead_flag</code>. (Note: makeindex uses a different name <code>headings_flag</code>)</dd></dl>
<dt><code>headings_flag</code> &lt;number&gt;</dt>
<dd> 0</dd>
<dl>
<dt>
</dt><dd> Same as <code>lethead_flag</code>. (compatible with makeindex)</dd></dl>
<dt><code>kana_head</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Heading characters of Kana specified by a string. By default, it is controlled by <code>letter_head</code> and command line option <code>-g</code>. (Extended by upmendex)</dd></dl>
<dt><code>hangul_head</code> &lt;string&gt;</dt>
<dd> &quot;ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ&quot;</dd>
<dl>
<dt>
</dt><dd> Heading characters of Hangul specified by a string. (Extended by upmendex)</dd></dl>
<dt><code>tumunja</code> &lt;string&gt;</dt>
<dd> &quot;ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ&quot;</dd>
<dl>
<dt>
</dt><dd> Heading characters of Hangul specified by a string. (Deprecated, Extended by upmendex)</dd></dl>
<dt><code>hanzi_head</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Heading strings of hanzi (Kanji, Hanja) specified by a string, which is concatenated of items with a separator &#8216;;&#8217;. (Extended by upmendex)</dd></dl>
<dt><code>devanagari_head</code> &lt;string&gt;</dt>
<dd> &quot;ऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसह&quot;</dd>
<dl>
<dt>
</dt><dd> Heading characters of Devanagari specified by a string. (Experimental, Extended by upmendex)</dd></dl>
<dt><code>thai_head</code> &lt;string&gt;</dt>
<dd>
</dd><dl>
<dt>
</dt><dd> Heading characters of Thai script specified by a string. (Experimental, Extended by upmendex)</dd></dl>
<dt><code>item_0</code> &lt;string&gt;</dt>
<dd> &quot;
 \item &quot;</dd>
<dl>
<dt>
</dt><dd> Command sequence inserted between primary level entries.</dd></dl>
<dt><code>item_1</code> &lt;string&gt;</dt>
<dd> &quot;
 \subitem &quot;</dd>
<dl>
<dt>
</dt><dd> Command sequence inserted between sub level entries.</dd></dl>
<dt><code>item_2</code> &lt;string&gt;</dt>
<dd> &quot;
 \subsubitem &quot;</dd>
<dl>
<dt>
</dt><dd> Command sequence inserted between subsub level entries.</dd></dl>
<dt><code>item_01</code> &lt;string&gt;</dt>
<dd> &quot;
 \subitem &quot;</dd>
<dl>
<dt>
</dt><dd> Command sequence inserted between primaly and sub level entries.</dd></dl>
<dt><code>item_x1</code> &lt;string&gt;</dt>
<dd> &quot;
 \subitem &quot;</dd>
<dl>
<dt>
</dt><dd> Command sequence inserted between primary and sub level entries when main entry does not have page number.</dd></dl>
<dt><code>item_12</code> &lt;string&gt;</dt>
<dd> &quot;
 \subsubitem &quot;</dd>
<dl>
<dt>
</dt><dd> Command sequence inserted between sub and subsub level entries.</dd></dl>
<dt><code>item_x2</code> &lt;string&gt;</dt>
<dd> &quot;
 \subsubitem &quot;</dd>
<dl>
<dt>
</dt><dd> Command sequence inserted between sub and subsub level entries when sub level entry does not have page number.</dd></dl>
<dt><code>delim_0</code> &lt;string&gt;</dt>
<dd> &quot;, &quot;</dd>
<dl>
<dt>
</dt><dd> Delimiter string between primary level entry and first page number.</dd></dl>
<dt><code>delim_1</code> &lt;string&gt;</dt>
<dd> &quot;, &quot;</dd>
<dl>
<dt>
</dt><dd> Delimiter string between sub level entry and first page number.</dd></dl>
<dt><code>delim_2</code> &lt;string&gt;</dt>
<dd> &quot;, &quot;</dd>
<dl>
<dt>
</dt><dd> Delimiter string between subsub level entry and first page number.</dd></dl>
<dt><code>delim_n</code> &lt;string&gt;</dt>
<dd> &quot;, &quot;</dd>
<dl>
<dt>
</dt><dd> Delimiter string between page numbers commonly used for any entry level.</dd></dl>
<dt><code>delim_r</code> &lt;string&gt;</dt>
<dd> &quot;&#8211;&quot;</dd>
<dl>
<dt>
</dt><dd> Delimiter string between pages to show page range.</dd></dl>
<dt><code>delim_t</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Delimiter string output at the end of page number list.</dd></dl>
<dt><code>suffix_2p</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> String to be inserted in place of <code>delim_n</code> and the next page number when the two pages are contiguous.</dd></dl>
<p> It works only when the parameter is defined.</p>
<dt><code>suffix_3p</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> String to be inserted in place of <code>delim_r</code> and the third page number when the three pages are contiguous. The parameter is prior to <code>suffix_mp</code>.</dd></dl>
<p> It works only when the parameter is defined.</p>
<dt><code>suffix_mp</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> String to be inserted in place of <code>delim_r</code> and the last page number when the three or more pages are contiguous.</dd></dl>
<p> It works only when the parameter is defined.</p>
<dt><code>encap_prefix</code> &lt;string&gt;</dt>
<dd> &quot;\&quot;</dd>
<dl>
<dt>
</dt><dd> Prefix for an encapsulating command when the encapsulating command is added to the page number.</dd></dl>
<dt><code>encap_infix</code> &lt;string&gt;</dt>
<dd> &quot;{&quot;</dd>
<dl>
<dt>
</dt><dd> Prefix just before the page number when the encapsulating command is added to the page number.</dd></dl>
<dt><code>encap_suffix</code> &lt;string&gt;</dt>
<dd> &quot;}&quot;.</dd>
<dl>
<dt>
</dt><dd> Suffix after the page number when the encapsulating command is added to the page number.</dd></dl>
<dt><code>line_max</code> &lt;number&gt;</dt>
<dd> 72</dd>
<dl>
<dt>
</dt><dd> Maximum number of one line. If exceed the number, lines are folded.</dd></dl>
<dt><code>indent_space</code> &lt;string&gt;</dt>
<dd> &quot; &quot;</dd>
<dl>
<dt>
</dt><dd> Space for indent which inserted to top of folded line.</dd></dl>
<dt><code>indent_length</code> &lt;number&gt;</dt>
<dd> 16</dd>
<dl>
<dt>
</dt><dd> Length of space for indent which inserted to top of folded line.</dd></dl>
<dt><code>symhead_positive</code> &lt;string&gt;</dt>
<dd> &quot;Symbols&quot;</dd>
<dl>
<dt>
</dt><dd> Strings to output as heading letter for symbols when lethead_flag or heading_flag or headings_flag is positive number.</dd></dl>
<dt><code>symhead_negative</code> &lt;string&gt;</dt>
<dd> &quot;symbols&quot;</dd>
<dl>
<dt>
</dt><dd> Strings to output as heading letter for symbols when lethead_flag or heading_flag or headings_flag is negative number.</dd></dl>
<dt><code>symbol</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Strings to output as heading letter for symbols when symbol_flag is non zero.</dd></dl>
<p> If specified, the option is prior to symhead_positive and symhead_negative. (Extended by (up)mendex)</p>
<dt><code>numhead_positive</code> &lt;string&gt;</dt>
<dd> &quot;Numbers&quot;</dd>
<dl>
<dt>
</dt><dd> Strings to output as heading letter for numbers when lethead_flag or heading_flag or headings_flag is positive number and symbol_flag is 2.</dd></dl>
<dt><code>numhead_negative</code> &lt;string&gt;</dt>
<dd> &quot;numbers&quot;</dd>
<dl>
<dt>
</dt><dd> Strings to output as heading letter for numbers when lethead_flag or heading_flag or headings_flag is negative number and symbol_flag is 2.</dd></dl>
<dt><code>symbol_flag</code> &lt;number&gt;</dt>
<dd> 1</dd>
<dl>
<dt>
</dt><dd> Flag to output of symbol. If &#8216;0&#8217;, do not output headings for symbols and numbers. If &#8216;1&#8217;, output symbols and numbers as a group of symbols. If &#8216;2&#8217;, output symbols and numbers separately. (Extended by (up)mendex)</dd></dl>
<dt><code>letter_head</code> &lt;number&gt;</dt>
<dd> 1</dd>
<dl>
<dt>
</dt><dd> Flag of heading letter for Japanese Kana. If &#8216;1&#8217; and &#8216;2&#8217;, Katakana and Hiragana is used, respectively. (Extended by (up)mendex)</dd></dl>
<dt><code>priority</code> &lt;number&gt;</dt>
<dd> 0</dd>
<dl>
<dt>
</dt><dd> Flag of sorting method for index words composed of Japanese and non-Japanese (ex. Latin scripts). If non zero, one space (U+20) is inserted between Japanese sequence and non-Japanese sequence in sorting procedure. (Extended by (up)mendex)</dd></dl>
<dt><code>character_order</code> &lt;string&gt;</dt>
<dd> &quot;SNLGCJKHDTah&quot;</dd>
<dl>
<dt>
</dt><dd> Order of scripts and symbols. &#8216;S&#8217;, &#8216;N&#8217;, &#8216;L&#8217;, &#8216;G&#8217;, &#8216;C&#8217;, &#8216;J&#8217;, &#8216;K&#8217;, &#8216;H&#8217;, &#8216;D&#8217;, &#8216;T&#8217;, &#8216;a&#8217; and &#8216;h&#8217; respectively denotes symbol, number, Latin, Greek, Cyrillic, Japanese Kana, Korean Hangul, Hanja, Devanagari, Thai, Arabic and Hebrew script. Please make sure that &#8216;S&#8217; and &#8216;N&#8217; are next to each other if symbol_flag=1, since numbers are classified as a part of symbol. (Extended by upmendex)</dd></dl>
<dt><code>script_preamble</code> &lt;string 1&gt; &lt;string 2&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Preamble of script block in output file, specified by string 2. One of script names must be specified in the string 1: &#8216;latin&#8217;, &#8216;cyrillic&#8217;, &#8216;greek&#8217;, &#8216;kana&#8217;, &#8216;hangul&#8217;, &#8216;hanzi&#8217;, &#8216;devanagari&#8217;, &#8216;thai&#8217;, &#8216;arabic&#8217;, or &#8216;hebrew&#8217;. (Extended by upmendex)</dd></dl>
<dt><code>script_postamble</code> &lt;string 1&gt; &lt;string 2&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Postamble of script block in output file, specified by string 2. One of script names must be specified in the string 1: &#8216;latin&#8217;, &#8216;cyrillic&#8217;, &#8216;greek&#8217;, &#8216;kana&#8217;, &#8216;hangul&#8217;, &#8216;hanzi&#8217;, &#8216;devanagari&#8217;, &#8216;thai&#8217;, &#8216;arabic&#8217;, or &#8216;hebrew&#8217;. (Extended by upmendex)</dd></dl>
<dt><code>icu_locale</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Locale in ICU collator. By default, &quot;root sort order&quot; is set. (Extended by upmendex)</dd></dl>
<dt><code>icu_rules</code> &lt;string&gt;</dt>
<dd> &quot;&quot;</dd>
<dl>
<dt>
</dt><dd> Customized collation rules in ICU collator. Unicode characters in UTF-8 encoding and following escape sequences are accepted: <code>
</dd></dl></dl>
</code>
