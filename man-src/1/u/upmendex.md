---

title: "upmendex(1)"
name: "upmendex"
section: "1"
letter: "u"
url: "/docs/linux/man/1-upmendex/"
description: "upmendex – Multilingual index processor"
---

<p> <code>upmendex</code> [-ilqrcgf] [<code>-s</code><i> sty</i>] [<code>-d</code><i> dic</i>] [<code>-o</code><i> ind</i>] [<code>-t</code><i> log</i>] [<code>-p</code><i> no</i>] [<code>--</code>] [<i> idx0 idx1 idx2 ...</i>] <br />
 <code>upmendex</code> <code>--help</code>  </p>
<p> The program <i>upmendex</i> is a general purpose multilingual hierarchical index generator working with upLaTeX, XeLaTeX and LuaLaTeX; it accepts one or more input files (<i>.idx</i>; often produced by a text formatter such as LaTeX families), sorts the entries, and produces an output file which can be formatted. It supports Latin (including non-English), Greek, Cyrillic, Korean Hangul and Han (Hanzi ideographs) scripts, as well as Japanese Kana. It is almost compatible with <i>makeindex</i> and <i>mendex</i>, and additional feature for handling readings of kanji words is also available. The formats of the input and output files are specified in a style file. The readings of kanji words can be specified in a dictionary file. The index can have up to three levels (0, 1, and 2) of subitem nesting.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></dt>
<dd> <p> Take input from stdin, even when index files are specified. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Set &#8216;sort by character order&#8217;. By default, &#8216;sort by word order&#8217; is used. Details are described below. </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Quiet mode; send no message to <i>stderr</i>, except error messages and warnings. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Disable implicit page range formation. By default, three or more successive pages are automatically abbreviated as a range (e.g. 1-5). </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Compress sequence of intermediate blanks (space(s) and/or tab(s)) into a space and ignore leading and trailing blank(s). By default, blanks in the index key are retained. </p>
 </dd>
<dt><code>-g</code></dt>
<dd> <p> Make Japanese index head <i>A</i>-line (<i>A, Ka, Sa, ...</i>; 10 characters) of the <i>gojuon</i> table (Japanese syllabary). By default, all 48 characters in the <i>gojuon</i> table are used. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Force to output characters even if the scripts are not supported by <i>upmendex</i>. </p>
 </dd>
<dt><code>-s</code><i> sty</i></dt>
<dd> <p> Employ <i>sty</i> as the style file. </p>
 </dd>
<dt><code>-d</code><i> dic</i></dt>
<dd> <p> Employ <i>dic</i> as the dictionary file. The dictionary file is composed of lists of &lt;<i>index_word</i>&nbsp;<i>reading</i>&gt;. </p>
 </dd>
<dt><code>-o</code><i> ind</i></dt>
<dd> <p> Employ <i>ind</i> as the output index file. By default, the file name is created by appending the extension <i>ind</i> to the base name of the first input file. </p>
 </dd>
<dt><code>-t</code><i> log</i></dt>
<dd> <p> Employ <i>log</i> as the transcript file. By default, the file name is created by appending the extension <i>ilg</i> to the base name of the first input file. </p>
 </dd>
<dt><code>-p</code><i> no</i></dt>
<dd> <p> Set the starting page number of the output index list to be <i>no</i>. The argument <i>no</i> may be numerical or one of the following: <i>any</i> (the next page to the end of contents), <i>odd</i> (the next odd page to the end of contents), <i>even</i> (the next even page to the end of contents). </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Show summary of options. </p>
 </dd>
<dt><code>--</code></dt>
<dd> <p> Arguments after <code>--</code> are not taken as options. This is useful when the input file name starts with &#8216;-&#8216;. </p>
 </dd></dl>
<h2>STYLE FILE</h2>
<p> The style file informs <i>upmendex</i> about the format of the <i>idx</i> input files and the intended format of the final output file. The format is upper compatible with the one for <i>makeindex</i> and <i>mendex</i>. The style file contains a list of &lt;<i>specifier</i>&nbsp;<i>attribute</i>&gt; pairs. There are two types of specifiers: input and output. Pairs do not have to appear in any particular order. A line begun by &#8216;%&#8216; is a comment. </p>
<p> <code>Input file style parameter</code> </p>
<dl>
<dt><code>keyword</code> &lt;string&gt;</dt>
<dd> <p> &quot;\\indexentry&quot; </p>
 </dd>
<dl>
<dd> <p> Command with an argument of index entry which is going to be processed. </p>
 </dd></dl>
<dt><code>arg_open</code> &lt;char&gt;</dt>
<dd> <p> &#8216;{&#8216; </p>
 </dd>
<dl>
<dd> <p> Opening delimiter which shows the beginning of index entry. </p>
 </dd></dl>
<dt><code>arg_close</code> &lt;char&gt;</dt>
<dd> <p> &#8216;}&#8216; </p>
 </dd>
<dl>
<dd> <p> Closing delimiter which shows the end of index entry. </p>
 </dd></dl>
<dt><code>range_open</code> &lt;char&gt;</dt>
<dd> <p> &#8216;(&#8216; </p>
 </dd>
<dl>
<dd> <p> Opening delimiter which shows the beginning of page range. </p>
 </dd></dl>
<dt><code>range_close</code> &lt;char&gt;</dt>
<dd> <p> &#8216;)&#8216; </p>
 </dd>
<dl>
<dd> <p> Closing delimiter which shows the end of page range. </p>
 </dd></dl>
<dt><code>level</code> &lt;char&gt;</dt>
<dd> <p> &#8216;!&#8216; </p>
 </dd>
<dl>
<dd> <p> Delimiter which shows lower level. </p>
 </dd></dl>
<dt><code>actual</code> &lt;char&gt;</dt>
<dd> <p> &#8216;@&#8216; </p>
 </dd>
<dl>
<dd> <p> Symbol which shows the next sequence is to appear as index strings in the output file. </p>
 </dd></dl>
<dt><code>encap</code> &lt;char&gt;</dt>
<dd> <p> &#8216;|&#8216; </p>
 </dd>
<dl>
<dd> <p> Symbol which shows the next sequence is to be used as command name attached to the page number. </p>
 </dd></dl>
<dt><code>page_compositor</code> &lt;string&gt;</dt>
<dd> <p> &quot;-&quot; </p>
 </dd>
<dl>
<dd> <p> Separator between page levels for a style with multi-levels of page numbers. </p>
 </dd></dl>
<dt><code>page_precedence</code> &lt;string&gt;</dt>
<dd> <p> &quot;rnaRA&quot; </p>
 </dd>
<dl>
<dd> <p> Priority of expression for page number. &#8216;R&#8217; and &#8216;r&#8217; correspond to Roman. &#8216;n&#8217; corresponds to arabic numeral. &#8216;A&#8217; and &#8216;a&#8217; correspond to Latin alphabet. </p>
 </dd></dl>
<dt><code>quote</code> &lt;char&gt;</dt>
<dd> <p> &#8216;&quot;&#8216; </p>
 </dd>
<dl>
<dd> <p> Escape character for <i>upmendex</i> parameters. </p>
 </dd></dl>
<dt><code>escape</code> &lt;char&gt;</dt>
<dd> <p> &#8216;\\&#8216; </p>
 </dd>
<dl>
<dd> <p> Escape character for general scripts. </p>
 </dd></dl>
<p> <code>Output file style parameter</code> </p>
<dt><code>preamble</code> &lt;string&gt;</dt>
<dd> <p> &quot;\\begin{theindex}\n&quot; </p>
 </dd>
<dl>
<dd> <p> Preamble of output file. </p>
 </dd></dl>
<dt><code>postamble</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n\n\\end{theindex}\n&quot; </p>
 </dd>
<dl>
<dd> <p> Postamble of output file. </p>
 </dd></dl>
<dt><code>setpage_prefix</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\setcounter{page}{&quot; </p>
 </dd>
<dl>
<dd> <p> Prefix of page number if start page is designated. </p>
 </dd></dl>
<dt><code>setpage_suffix</code> &lt;string&gt;</dt>
<dd> <p> &quot;}\n&quot; </p>
 </dd>
<dl>
<dd> <p> Suffix of page number if start page is designated. </p>
 </dd></dl>
<dt><code>group_skip</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n\n \\indexspace\n&quot; </p>
 </dd>
<dl>
<dd> <p> Strings to insert vertical space before new section of index. </p>
 </dd></dl>
<dt><code>lethead_prefix</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Prefix of heading for newly appeared heading letter. </p>
 </dd></dl>
<dt><code>heading_prefix</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Same as <code>lethead_prefix</code>. (compatible with makeindex) </p>
 </dd></dl>
<dt><code>lethead_suffix</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Suffix of heading for newly appeared heading letter. </p>
 </dd></dl>
<dt><code>heading_suffix</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Same as <code>lethead_suffix</code>. (compatible with makeindex) </p>
 </dd></dl>
<dt><code>lethead_flag</code> &lt;number&gt;</dt>
<dd> <p> 0 </p>
 </dd>
<dl>
<dd> <p> Flag to control output of heading letters in Latin, Greek and Cyrillic scripts. &#8216;0&#8217;, &#8216;1&#8217;, &#8216;-1&#8217; and &#8216;2&#8217; respectively denotes no output, uppercase, lowercase and titlecase. </p>
 </dd></dl>
<dt><code>heading_flag</code> &lt;number&gt;</dt>
<dd> <p> 0 </p>
 </dd>
<dl>
<dd> <p> Same as <code>lethead_flag</code>. (Note: makeindex uses a different name <code>headings_flag</code>) </p>
 </dd></dl>
<dt><code>headings_flag</code> &lt;number&gt;</dt>
<dd> <p> 0 </p>
 </dd>
<dl>
<dd> <p> Same as <code>lethead_flag</code>. (compatible with makeindex) </p>
 </dd></dl>
<dt><code>kana_head</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Heading characters of Kana specified by a string. By default, it is controlled by <code>letter_head</code> and command line option <code>-g</code>. (Extended by upmendex) </p>
 </dd></dl>
<dt><code>hangul_head</code> &lt;string&gt;</dt>
<dd> <p> &quot;ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ&quot; </p>
 </dd>
<dl>
<dd> <p> Heading characters of Hangul specified by a string. (Extended by upmendex) </p>
 </dd></dl>
<dt><code>tumunja</code> &lt;string&gt;</dt>
<dd> <p> &quot;ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ&quot; </p>
 </dd>
<dl>
<dd> <p> Heading characters of Hangul specified by a string. (Deprecated, Extended by upmendex) </p>
 </dd></dl>
<dt><code>hanzi_head</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Heading strings of hanzi (Kanji, Hanja) specified by a string, which is concatenated of items with a separator &#8216;;&#8216;. (Extended by upmendex) </p>
 </dd></dl>
<dt><code>devanagari_head</code> &lt;string&gt;</dt>
<dd> <p> &quot;ऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसह&quot; </p>
 </dd>
<dl>
<dd> <p> Heading characters of Devanagari specified by a string. (Experimental, Extended by upmendex) </p>
 </dd></dl>
<dt><code>thai_head</code> &lt;string&gt;</dt>
<dd>  </dd>
<dl>
<dd> <p> Heading characters of Thai script specified by a string. (Experimental, Extended by upmendex) </p>
 </dd></dl>
<dt><code>item_0</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\item &quot; </p>
 </dd>
<dl>
<dd> <p> Command sequence inserted between primary level entries. </p>
 </dd></dl>
<dt><code>item_1</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\subitem &quot; </p>
 </dd>
<dl>
<dd> <p> Command sequence inserted between sub level entries. </p>
 </dd></dl>
<dt><code>item_2</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\subsubitem &quot; </p>
 </dd>
<dl>
<dd> <p> Command sequence inserted between subsub level entries. </p>
 </dd></dl>
<dt><code>item_01</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\subitem &quot; </p>
 </dd>
<dl>
<dd> <p> Command sequence inserted between primaly and sub level entries. </p>
 </dd></dl>
<dt><code>item_x1</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\subitem &quot; </p>
 </dd>
<dl>
<dd> <p> Command sequence inserted between primary and sub level entries when main entry does not have page number. </p>
 </dd></dl>
<dt><code>item_12</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\subsubitem &quot; </p>
 </dd>
<dl>
<dd> <p> Command sequence inserted between sub and subsub level entries. </p>
 </dd></dl>
<dt><code>item_x2</code> &lt;string&gt;</dt>
<dd> <p> &quot;\n \\subsubitem &quot; </p>
 </dd>
<dl>
<dd> <p> Command sequence inserted between sub and subsub level entries when sub level entry does not have page number. </p>
 </dd></dl>
<dt><code>delim_0</code> &lt;string&gt;</dt>
<dd> <p> &quot;, &quot; </p>
 </dd>
<dl>
<dd> <p> Delimiter string between primary level entry and first page number. </p>
 </dd></dl>
<dt><code>delim_1</code> &lt;string&gt;</dt>
<dd> <p> &quot;, &quot; </p>
 </dd>
<dl>
<dd> <p> Delimiter string between sub level entry and first page number. </p>
 </dd></dl>
<dt><code>delim_2</code> &lt;string&gt;</dt>
<dd> <p> &quot;, &quot; </p>
 </dd>
<dl>
<dd> <p> Delimiter string between subsub level entry and first page number. </p>
 </dd></dl>
<dt><code>delim_n</code> &lt;string&gt;</dt>
<dd> <p> &quot;, &quot; </p>
 </dd>
<dl>
<dd> <p> Delimiter string between page numbers commonly used for any entry level. </p>
 </dd></dl>
<dt><code>delim_r</code> &lt;string&gt;</dt>
<dd> <p> &quot;--&quot; </p>
 </dd>
<dl>
<dd> <p> Delimiter string between pages to show page range. </p>
 </dd></dl>
<dt><code>delim_t</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Delimiter string output at the end of page number list. </p>
 </dd></dl>
<dt><code>suffix_2p</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> String to be inserted in place of <code>delim_n</code> and the next page number when the two pages are contiguous. </p>
 </dd></dl>
<p> It works only when the parameter is defined. </p>
<dt><code>suffix_3p</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> String to be inserted in place of <code>delim_r</code> and the third page number when the three pages are contiguous. The parameter is prior to <code>suffix_mp</code>. </p>
 </dd></dl>
<p> It works only when the parameter is defined. </p>
<dt><code>suffix_mp</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> String to be inserted in place of <code>delim_r</code> and the last page number when the three or more pages are contiguous. </p>
 </dd></dl>
<p> It works only when the parameter is defined. </p>
<dt><code>encap_prefix</code> &lt;string&gt;</dt>
<dd> <p> &quot;\\&quot; </p>
 </dd>
<dl>
<dd> <p> Prefix for an encapsulating command when the encapsulating command is added to the page number. </p>
 </dd></dl>
<dt><code>encap_infix</code> &lt;string&gt;</dt>
<dd> <p> &quot;{&quot; </p>
 </dd>
<dl>
<dd> <p> Prefix just before the page number when the encapsulating command is added to the page number. </p>
 </dd></dl>
<dt><code>encap_suffix</code> &lt;string&gt;</dt>
<dd> <p> &quot;}&quot;. </p>
 </dd>
<dl>
<dd> <p> Suffix after the page number when the encapsulating command is added to the page number. </p>
 </dd></dl>
<dt><code>line_max</code> &lt;number&gt;</dt>
<dd> <p> 72 </p>
 </dd>
<dl>
<dd> <p> Maximum number of one line. If exceed the number, lines are folded. </p>
 </dd></dl>
<dt><code>indent_space</code> &lt;string&gt;</dt>
<dd> <p> &quot; &quot; </p>
 </dd>
<dl>
<dd> <p> Space for indent which inserted to top of folded line. </p>
 </dd></dl>
<dt><code>indent_length</code> &lt;number&gt;</dt>
<dd> <p> 16 </p>
 </dd>
<dl>
<dd> <p> Length of space for indent which inserted to top of folded line. </p>
 </dd></dl>
<dt><code>symhead_positive</code> &lt;string&gt;</dt>
<dd> <p> &quot;Symbols&quot; </p>
 </dd>
<dl>
<dd> <p> Strings to output as heading letter for symbols when lethead_flag or heading_flag or headings_flag is positive number. </p>
 </dd></dl>
<dt><code>symhead_negative</code> &lt;string&gt;</dt>
<dd> <p> &quot;symbols&quot; </p>
 </dd>
<dl>
<dd> <p> Strings to output as heading letter for symbols when lethead_flag or heading_flag or headings_flag is negative number. </p>
 </dd></dl>
<dt><code>symbol</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Strings to output as heading letter for symbols when symbol_flag is non zero. </p>
 </dd></dl>
<p> If specified, the option is prior to symhead_positive and symhead_negative. (Extended by (up)mendex) </p>
<dt><code>numhead_positive</code> &lt;string&gt;</dt>
<dd> <p> &quot;Numbers&quot; </p>
 </dd>
<dl>
<dd> <p> Strings to output as heading letter for numbers when lethead_flag or heading_flag or headings_flag is positive number and symbol_flag is 2. </p>
 </dd></dl>
<dt><code>numhead_negative</code> &lt;string&gt;</dt>
<dd> <p> &quot;numbers&quot; </p>
 </dd>
<dl>
<dd> <p> Strings to output as heading letter for numbers when lethead_flag or heading_flag or headings_flag is negative number and symbol_flag is 2. </p>
 </dd></dl>
<dt><code>symbol_flag</code> &lt;number&gt;</dt>
<dd> <p> 1 </p>
 </dd>
<dl>
<dd> <p> Flag to output of symbol. If &#8216;0&#8217;, do not output headings for symbols and numbers. If &#8216;1&#8217;, output symbols and numbers as a group of symbols. If &#8216;2&#8217;, output symbols and numbers separately. (Extended by (up)mendex) </p>
 </dd></dl>
<dt><code>letter_head</code> &lt;number&gt;</dt>
<dd> <p> 1 </p>
 </dd>
<dl>
<dd> <p> Flag of heading letter for Japanese Kana. If &#8216;1&#8217; and &#8216;2&#8217;, Katakana and Hiragana is used, respectively. (Extended by (up)mendex) </p>
 </dd></dl>
<dt><code>priority</code> &lt;number&gt;</dt>
<dd> <p> 0 </p>
 </dd>
<dl>
<dd> <p> Flag of sorting method for index words composed of Japanese and non-Japanese (ex. Latin scripts). If non zero, one space (U+20) is inserted between Japanese sequence and non-Japanese sequence in sorting procedure. (Extended by (up)mendex) </p>
 </dd></dl>
<dt><code>character_order</code> &lt;string&gt;</dt>
<dd> <p> &quot;SNLGCJKHDTah&quot; </p>
 </dd>
<dl>
<dd> <p> Order of scripts and symbols. &#8216;S&#8217;, &#8216;N&#8217;, &#8216;L&#8217;, &#8216;G&#8217;, &#8216;C&#8217;, &#8216;J&#8217;, &#8216;K&#8217;, &#8216;H&#8217;, &#8216;D&#8217;, &#8216;T&#8217;, &#8216;a&#8217; and &#8216;h&#8217; respectively denotes symbol, number, Latin, Greek, Cyrillic, Japanese Kana, Korean Hangul, Hanja, Devanagari, Thai, Arabic and Hebrew script. Please make sure that &#8216;S&#8217; and &#8216;N&#8217; are next to each other if symbol_flag=1, since numbers are classified as a part of symbol. (Extended by upmendex) </p>
 </dd></dl>
<dt><code>script_preamble</code> &lt;string 1&gt; &lt;string 2&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Preamble of script block in output file, specified by string 2. One of script names must be specified in the string 1: &#8216;latin&#8217;, &#8216;cyrillic&#8217;, &#8216;greek&#8217;, &#8216;kana&#8217;, &#8216;hangul&#8217;, &#8216;hanzi&#8217;, &#8216;devanagari&#8217;, &#8216;thai&#8217;, &#8216;arabic&#8217;, or &#8216;hebrew&#8217;. (Extended by upmendex) </p>
 </dd></dl>
<dt><code>script_postamble</code> &lt;string 1&gt; &lt;string 2&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Postamble of script block in output file, specified by string 2. One of script names must be specified in the string 1: &#8216;latin&#8217;, &#8216;cyrillic&#8217;, &#8216;greek&#8217;, &#8216;kana&#8217;, &#8216;hangul&#8217;, &#8216;hanzi&#8217;, &#8216;devanagari&#8217;, &#8216;thai&#8217;, &#8216;arabic&#8217;, or &#8216;hebrew&#8217;. (Extended by upmendex) </p>
 </dd></dl>
<dt><code>icu_locale</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Locale in ICU collator. By default, &quot;root sort order&quot; is set. (Extended by upmendex) </p>
 </dd></dl>
<dt><code>icu_rules</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Customized collation rules in ICU collator. Unicode characters in UTF-8 encoding and following escape sequences are accepted: <code>\Uhhhhhhhh</code> (8-digit hexadecimal [0-9A-Fa-f]), <code>\uhhhh</code> (4-digit hexadecimal), <code>\xhh</code> (2-digit hexadecimal), <code>\x{h...}</code> (1..8-digit hexadecimal), and <code>\ooo</code> (3-digit octal [0-7]). If icu_rules and icu_locale are simultaneously specified, collation rules specified by icu_rules are added on collation rules specified by icu_locale. By default, locale is used. (Extended by upmendex) </p>
 </dd></dl>
<p> Ref. &lt;<a rel="nofollow" href="https://unicode-org.github.io/icu/userguide/collation/customization/">https://unicode-org.github.io/icu/userguide/collation/customization/</a>&gt;, &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr35/tr35-collation.html#Rules">http://www.unicode.org/reports/tr35/tr35-collation.html#Rules</a>&gt; </p>
<dt><code>icu_attributes</code> &lt;string&gt;</dt>
<dd> <p> &quot;&quot; </p>
 </dd>
<dl>
<dd> <p> Attributes in ICU collator. Followings are available: &quot;alternate:shifted&quot;, &quot;alternate:non-ignorable&quot;, &quot;strength:primary&quot;, &quot;strength:secondary&quot;, &quot;strength:tertiary&quot;, &quot;strength:quaternary&quot;, &quot;strength:identical&quot;, &quot;french-collation:on&quot;, &quot;french-collation:off&quot;, &quot;case-first:off&quot;, &quot;case-first:upper-first&quot;, &quot;case-first:lower-first&quot;, &quot;case-level:on&quot;, &quot;case-level:off&quot;, &quot;normalization-mode:on&quot;, &quot;normalization-mode:off&quot;, &quot;numeric-ordering:on&quot;, &quot;numeric-ordering:off&quot; (Extended by upmendex) </p>
 </dd></dl>
<p> Ref. &lt;<a rel="nofollow" href="https://unicode-org.github.io/icu/userguide/collation/customization/#default-options">https://unicode-org.github.io/icu/userguide/collation/customization/#default-options</a>&gt;, &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr35/tr35-collation.html#Setting_Options">http://www.unicode.org/reports/tr35/tr35-collation.html#Setting_Options</a>&gt; </dl>
 </p>
<h2>ABOUT JAPANESE PROCESSING</h2>
<p> <i>upmendex</i> has an additional feature to simplify the procedure of handling Japanese indexes, compared to <i>makeindex</i>. Users can save the effort of manually specifying a reading for every kanji word. Japanese kanji words are usually sorted by the syllables of their readings (<i>&#8216;Yomi&#8217;</i>), which can be represented by kana (Hiragana, Katakana) scripts. <i>upmendex</i> accepts index words specified in kana expression directly on an input file, and also accepts conversion from index words in Kanji or symbols to phonogram scripts by referring to Japanese dictionaries. </p>
<p> Examples of internal simplification of syllables are shown below. </p>
<dl>
<dd> <p> <br />
 かぶしきがいしゃ <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>かふしきかいしや<br />
 <br />
 マッキントッシュ <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>まつきんとつしゆ<br />
 <br />
 ワープロ <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>わあふろ<br />
 </p>
 </dd></dl>
<p> The dictionary file consists of list with &lt;&#8216;index_word&#8217; &#8216;reading&#8217;&gt;. The index word can be written in any scripts (kanji, kana, etc), and the reading can be in any phonograms such as Hiragana or Katakana scripts. The delimiter between the index word and its reading is one or more tab(s) or space(s). An example of a Japanese dictionary is shown below. </p>
<dl>
<dd> <p> <br />
 漢字 <code>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>かんじ<br />
 <br />
 読み <code>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>よみ<br />
 <br />
 環境 <code>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>かんきょう<br />
 <br />
 ＄<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>ドル<br />
 </p>
 </dd></dl>
<p> Here, each index word is allowed to have only one Yomi. Though some kanji words (ex. 「表」) may have more than one Yomi&#8217;s (ex. 「ひょう」 and 「おもて」), only one of them can be registered in the dictionary. When some different Yomi&#8217;s are needed, they should be specified explicitly in kana expression (ex. \index{ひょう@表} or \index{おもて@表}) on the input file. Moreover, a dictionary file is automatically referred by setting the file name at an environment variable <i>INDEXDEFAULTDICTIONARY</i>. The dictionary set by the environment variable can be used together with file(s) specified by <i>-d</i> option. </p>
<h2>ABOUT SORTING PROCEDURE</h2>
<p> <i>upmendex</i> sorts indexes as is (&#8216;sort by word order&#8217;) by default. Setting <i>-l</i> option, spaces between words in an index are truncated prior to sorting procedure (&#8216;sort by character order&#8217;). Even when sort by character order, the index at output remains the original sequence without the truncation. Follows show an example. </p>
<dl>
<dd> <p> <i>sort by word order <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>sort by character order</i><br />
 <br />
 X Window <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>Xlib<br />
 <br />
 Xlib <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>XView<br />
 <br />
 XView <code>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>X Window<br />
 </p>
 </dd></dl>
<p> In addition, two sorting methods can be applied for indexes which contains both Japanese kana and other scripts (e.g. Latin script). By setting <i>priority</i> 0 (default) and 1 at a style file, a space between Japanese Kana and other scripts is inserted and not inserted respectively, prior to the sorting procedure. Follows show an example. </p>
<dl>
<dd> <p> <i>priority=0 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>priority=1</i><br />
 <br />
 index sort <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>indファイル<br />
 <br />
 indファイル <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>index sort<br />
 </p>
 </dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <i>upmendex</i> refers environment variables as follows. </p>
<dl>
<dt><i>INDEXSTYLE</i></dt>
<dd> <p> Directory where index style files exist. </p>
 </dd>
<dt><i>INDEXDEFAULTSTYLE</i></dt>
<dd> <p> Index style file to be referred to as default. </p>
 </dd>
<dt><i>INDEXDICTIONARY</i></dt>
<dd> <p> Directory where dictionary files exist. </p>
 </dd>
<dt><i>INDEXDEFAULTDICTIONARY</i></dt>
<dd> <p> Dictionary file which is automatically read. </p>
 </dd></dl>
<h2>DETAIL</h2>
<p> Detailed specification is compatible with <i>makeindex</i>. </p>
<h2>KNOWN ISSUES</h2>
<p> When plural page number expression is used, <i>.idx</i> files should be specified along with the order of page numbers. Otherwise, wrong page numbers might be output. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a>(1),</code> <code><a href="/docs/linux/man/1-latex/">latex</a>(1),</code> <code><a href="/docs/linux/man/1-makeindex/">makeindex</a>(1),</code> <code><a href="/docs/linux/man/1-mendex/">mendex</a>(1).</code> <br />
 International Components for Unicode (ICU): &lt;<a rel="nofollow" href="http://icu.unicode.org/">http://icu.unicode.org/</a>&gt;, &lt;<a rel="nofollow" href="https://unicode-org.github.io/icu/">https://unicode-org.github.io/icu/</a>&gt;  </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Takuji Tanaka based on the mendex manual page written by Japanese TeX Development Community. </p>
