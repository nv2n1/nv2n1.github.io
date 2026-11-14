---
title: "hunspell(4)"
name: "hunspell"
section: "4"
letter: "h"
url: "/docs/linux/man/4-hunspell/"
description: "hunspell – format of Hunspell dictionaries and affix files"
---

<p>hunspell &#8211; format of Hunspell dictionaries and affix files</p>
<h2>Description</h2>
<p><i><a href="/docs/linux/man/1-hunspell/">Hunspell</a></i>(1) Hunspell requires two files to define the way a language is being spell checked: a dictionary file containing words and applicable flags, and an affix file that specifies how these flags wil controll spell checking. An optional file is the personal dictionary file. </p>
<h2>Dictionary file</h2>
<p>A dictionary file (*.dic) contains a list of words, one per line. The first line of the dictionaries (except personal dictionaries) contains the approximate word count (for optimal hash memory size). Each word may optionally be followed by a slash (&quot;/&quot;) and one or more flags, which represents the word attributes, for example affixes. </p>
<p> Note: Dictionary words can contain also slashes when escaped like &quot;/&quot; syntax.</p>
<h2>Personal dictionary file</h2>
<p>Personal dictionaries are simple word lists. Asterisk at the first character position signs prohibition. A second word separated by a slash sets the affixation. </p>
<dl>
<dd>
<pre>foo
Foo/Simpson
*bar</pre>
</dl>
<p> In this example, &quot;foo&quot; and &quot;Foo&quot; are personal words, plus Foo will be recognized with affixes of Simpson (Foo&#8217;s etc.) and bar is a forbidden word.</p>
<h2>Short example</h2>
<p>Dictionary file: </p>
<dl>
<dd>
<pre>3
hello
try/B
work/AB</pre>
</dl>
<p> The flags B and A specify attributes of these words. </p>
<p> Affix file: </p>
<dl>
<dd>
<pre>SET UTF-8
TRY esianrtolcdugmphbyfvkwzESIANRTOLCDUGMPHBYFVKWZ'
REP 2
REP f ph
REP ph f
PFX A Y 1
PFX A 0 re .
SFX B Y 2
SFX B 0 ed [^y]
SFX B y ied y</pre>
</dl>
<p> In the affix file, prefix A and suffix B have been defined. Flag A defines a `re-&#8216; prefix. Class B defines two `-ed&#8217; suffixes. First B suffix can be added to a word if the last character of the word isn&#8217;t `y&#8217;. Second suffix can be added to the words terminated with an `y&#8217;. </p>
<p> All accepted words with this dictionary and affix combination are: &quot;hello&quot;, &quot;try&quot;, &quot;tried&quot;, &quot;work&quot;, &quot;worked&quot;, &quot;rework&quot;, &quot;reworked&quot;.</p>
<h2>Affix File General Options</h2>
<p>Hunspell source distribution contains more than 80 examples for option usage. </p>
<dl>
<dt>SET encoding</p>
<dd>Set character encoding of words and morphemes in affix and dictionary files. Possible values: UTF-8, ISO8859-1 &#8211; ISO8859-10, ISO8859-13 &#8211; ISO8859-15, KOI8-R, KOI8-U, microsoft-cp1251, ISCII-DEVANAGARI.</dl>
<dl>
<dd>
<pre>SET UTF-8</pre>
</dl>
<dl>
<dt>FLAG value</p>
<dd>Set flag type. Default type is the extended ASCII (8-bit) character. `UTF-8&#8242; parameter sets UTF-8 encoded Unicode character flags. The `long&#8217; value sets the double extended ASCII character flag type, the `num&#8217; sets the decimal number flag type. Decimal flags numbered from 1 to 65000, and in flag fields are separated by comma. BUG: UTF-8 flag type doesn&#8217;t work on ARM platform.</dl>
<dl>
<dd>
<pre>FLAG long</pre>
</dl>
<dl>
<dt>COMPLEXPREFIXES</p>
<dd>Set twofold prefix stripping (but single suffix stripping) eg. for morphologically complex languages with right-to-left writing system. </p>
<dt>LANG langcode</p>
<dd>Set language code for language specific functions of Hunspell. Use it to activate special casing of Azeri (LANG az) and Turkish (LANG tr).</p>
<dt>IGNORE characters</p>
<dd>Sets characters to ignore dictionary words, affixes and input words. Useful for optional characters, as Arabic (harakat) or Hebrew (niqqud) diacritical marks (see tests/ignore.* test dictionary in Hunspell distribution). </p>
<dt>AF number_of_flag_vector_aliases</p>
<dd>
<dt>AF flag_vector</p>
<dd>Hunspell can substitute affix flag sets with ordinal numbers in affix rules (alias compression, see makealias tool). First example with alias compression:</dl>
<dl>
<dd>
<pre>3
hello
try/1
work/2</pre>
</dl>
<p> AF definitions in the affix file: </p>
<dl>
<dd>
<pre>AF 2
AF A
AF AB</pre>
</dl>
<p> It is equivalent of the following dic file: </p>
<dl>
<dd>
<pre>3
hello
try/A
work/AB</pre>
</dl>
<p> See also tests/alias* examples of the source distribution. </p>
<p> Note I: If affix file contains the FLAG parameter, define it before the AF definitions. </p>
<p> Note II: Use makealias utility in Hunspell distribution to compress aff and dic files.</p>
<dl>
<dt>AM number_of_morphological_aliases</p>
<dd>
<dt>AM morphological_fields</p>
<dd>Hunspell can substitute also morphological data with ordinal numbers in affix rules (alias compression). See tests/alias* examples.</dl>
<h2>Affix File Options For Suggestion</h2>
<p>Suggestion parameters can optimize the default n-gram (similarity search in the dictionary words based on the common 1, 2, 3, 4-character length common character-sequences), character swap and deletion suggestions of Hunspell. REP is suggested to fix the typical and especially bad language specific bugs, because the REP suggestions have the highest priority in the suggestion list. PHONE is for languages with not pronunciation based orthography.</p>
<dl>
<dt>KEY characters_separated_by_vertical_line_optionally</p>
<dd>Hunspell searches and suggests words with one different character replaced by a neighbor KEY character. Not neighbor characters in KEY string separated by vertical line characters. Suggested KEY parameters for QWERTY and Dvorak keyboard layouts:</dl>
<dl>
<dd>
<pre>KEY qwertyuiop|asdfghjkl|zxcvbnm
KEY pyfgcrl|aeouidhtns|qjkxbmwvz</pre>
</dl>
<p> Using the first QWERTY layout, Hunspell suggests &quot;nude&quot; and &quot;node&quot; for &quot;*nide&quot;. A character may have more neighbors, too: </p>
<dl>
<dd>
<pre>KEY qwertzuop|yxcvbnm|qaw|say|wse|dsx|sy|edr|fdc|dx|rft|gfv|fc|tgz|hgb|gv|zhu|jhn|hb|uji|kjm|jn|iko|lkm</pre>
</dl>
<dl>
<dt>TRY characters</p>
<dd>Hunspell can suggest right word forms, when they differ from the bad input word by one TRY character. The parameter of TRY is case sensitive.</p>
<dt>NOSUGGEST flag</p>
<dd>Words signed with NOSUGGEST flag are not suggested (but still accepted when typed correctly). Proposed flag for vulgar and obscene words (see also SUBSTANDARD).</p>
<dt>MAXCPDSUGS num</p>
<dd>Set max. number of suggested compound words generated by compound rules. The number of the suggested compound words may be greater from the same 1-character distance type.</p>
<dt>MAXNGRAMSUGS num</p>
<dd>Set max. number of n-gram suggestions. Value 0 switches off the n-gram suggestions (see also MAXDIFF).</p>
<dt>MAXDIFF [0-10]</p>
<dd>Set the similarity factor for the n-gram based suggestions (5 = default value; 0 = fewer n-gram suggestions, but min. 1; 10 = MAXNGRAMSUGS n-gram suggestions).</p>
<dt>ONLYMAXDIFF</p>
<dd>Remove all bad n-gram suggestions (default mode keeps one, see MAXDIFF).</p>
<dt>NOSPLITSUGS</p>
<dd>Disable word suggestions with spaces.</p>
<dt>SUGSWITHDOTS</p>
<dd>Add dot(s) to suggestions, if input word terminates in dot(s). (Not for OpenOffice.org dictionaries, because OpenOffice.org has an automatic dot expansion mechanism.)</p>
<dt>REP number_of_replacement_definitions</p>
<dd>
<dt>REP what replacement</p>
<dd>This table specifies modifications to try first. First REP is the header of this table and one or more REP data line are following it. With this table, Hunspell can suggest the right forms for the typical spelling mistakes when the incorrect form differs by more than 1 letter from the right form. The search string supports the regex boundary signs (^ and $). For example a possible English replacement table definition to handle misspelled consonants:</dl>
<dl>
<dd>
<pre>REP 5
REP f ph
REP ph f
REP tion$ shun
REP ^cooccurr co-occurr
REP ^alot$ a_lot</pre>
</dl>
<p> Note I: It&#8217;s very useful to define replacements for the most typical one-character mistakes, too: with REP you can add higher priority to a subset of the TRY suggestions (suggestion list begins with the REP suggestions). </p>
<p> Note II: Suggesting separated words, specify spaces with underlines: </p>
<dl>
<dd>
<pre>REP 1
REP onetwothree one_two_three</pre>
</dl>
<p> Note III: Replacement table can be used for a stricter compound word checking with the option CHECKCOMPOUNDREP. </p>
<dl>
<dt>MAP number_of_map_definitions</p>
<dd>
<dt>MAP string_of_related_chars_or_parenthesized_character_sequences</p>
<dd>We can define language-dependent information on characters and character sequences that should be considered related (i.e. nearer than other chars not in the set) in the affix file (.aff) by a map table. With this table, Hunspell can suggest the right forms for words, which incorrectly choose the wrong letter or letter groups from a related set more than once in a word (see REP). </p>
<p> For example a possible mapping could be for the German umlauted ü versus the regular u; the word Frühstück really should be written with umlauted u&#8217;s and not regular ones</dl>
<dl>
<dd>
<pre>MAP 1
MAP uü</pre>
</dl>
<p> Use parenthesized groups for character sequences (eg. for composed Unicode characters): </p>
<dl>
<dd>
<pre>MAP 3
MAP ß(ss) (character sequence)
MAP ﬁ(fi) (&quot;fi&quot; compatibility characters for Unicode fi ligature)
MAP (ọ́)o (composed Unicode character: ó with bottom dot)</pre>
</dl>
<dl>
<dt>PHONE number_of_phone_definitions</p>
<dd>
<dt>PHONE what replacement</p>
<dd>PHONE uses a table-driven phonetic transcription algorithm borrowed from Aspell. It is useful for languages with not pronunciation based orthography. You can add a full alphabet conversion and other rules for conversion of special letter sequences. For detailed documentation see <a rel="nofollow" href="http://aspell.net/man-html/Phonetic-Code.html.">http://aspell.net/man-html/Phonetic-Code.html.</a> Note: Multibyte UTF-8 characters have not worked with bracket expression yet. Dash expression has signed bytes and not UTF-8 characters yet.</p>
<dt>WARN flag</p>
<dd>This flag is for rare words, wich are also often spelling mistakes, see option -r of command line Hunspell and FORBIDWARN.</p>
<dt>FORBIDWARN</p>
<dd>Words with flag WARN aren&#8217;t accepted by the spell checker using this parameter.</dl>
<h2>Options For Compounding</h2>
<dl>
<dt>BREAK number_of_break_definitions</p>
<dd>
<dt>BREAK character_or_character_sequence</p>
<dd>Define new break points for breaking words and checking word parts separately. Use ^ and $ to delete characters at end and start of the word. Rationale: useful for compounding with joining character or strings (for example, hyphen in English and German or hyphen and n-dash in Hungarian). Dashes are often bad break points for tokenization, because compounds with dashes may contain not valid parts, too.) With BREAK, Hunspell can check both side of these compounds, breaking the words at dashes and n-dashes:</dl>
<dl>
<dd>
<pre>BREAK 2
BREAK -
BREAK <code>--</code> # n-dash</pre>
</dl>
<p> Breaking are recursive, so foo-bar, bar-foo and foo-foo<code>&#8212;</code>bar-bar would be valid compounds. Note: The default word break of Hunspell is equivalent of the following BREAK definition: </p>
<dl>
<dd>
<pre>BREAK 3
BREAK -
BREAK ^-
BREAK -$</pre>
</dl>
<p> Hunspell doesn&#8217;t accept the &quot;-word&quot; and &quot;word-&quot; forms by this BREAK definition: </p>
<dl>
<dd>
<pre>BREAK 1
BREAK -</pre>
</dl>
<p> Switching off the default values: </p>
<dl>
<dd>
<pre>BREAK 0</pre>
</dl>
<p> Note II: COMPOUNDRULE is better for handling dashes and other compound joining characters or character strings. Use BREAK, if you want to check words with dashes or other joining characters and there is no time or possibility to describe precise compound rules with COMPOUNDRULE (COMPOUNDRULE handles only the suffixation of the last word part of a compound word). </p>
<p> Note III: For command line spell checking of words with extra characters, set WORDCHARS parameters: WORDCHARS &#8211;<code>&#8212;</code> (see tests/break.*) example</p>
<dl>
<dt>COMPOUNDRULE number_of_compound_definitions</p>
<dd>
<dt>COMPOUNDRULE compound_pattern</p>
<dd>Define custom compound patterns with a regex-like syntax. The first COMPOUNDRULE is a header with the number of the following COMPOUNDRULE definitions. Compound patterns consist compound flags, parentheses, star and question mark meta characters. A flag followed by a `*&#8217; matches a word sequence of 0 or more matches of words signed with this compound flag. A flag followed by a `?&#8217; matches a word sequence of 0 or 1 matches of a word signed with this compound flag. See tests/compound*.* examples. </p>
<p> Note: en_US dictionary of OpenOffice.org uses COMPOUNDRULE for ordinal number recognition (1st, 2nd, 11th, 12th, 22nd, 112th, 1000122nd etc.). </p>
<p> Note II: In the case of long and numerical flag types use only parenthesized flags: (1500)*(2000)? </p>
<p> Note III: COMPOUNDRULE flags work completely separately from the compounding mechanisme using COMPOUNDFLAG, COMPOUNDBEGIN, etc. compound flags. (Use these flags on different enhtries for words). </p>
<dt>COMPOUNDMIN num</p>
<dd>Minimum length of words used for compounding. Default value is 3 letters.</p>
<dt>COMPOUNDFLAG flag</p>
<dd>Words signed with COMPOUNDFLAG may be in compound words (except when word shorter than COMPOUNDMIN). Affixes with COMPOUNDFLAG also permits compounding of affixed words.</p>
<dt>COMPOUNDBEGIN flag</p>
<dd>Words signed with COMPOUNDBEGIN (or with a signed affix) may be first elements in compound words.</p>
<dt>COMPOUNDLAST flag</p>
<dd>Words signed with COMPOUNDLAST (or with a signed affix) may be last elements in compound words.</p>
<dt>COMPOUNDMIDDLE flag</p>
<dd>Words signed with COMPOUNDMIDDLE (or with a signed affix) may be middle elements in compound words.</p>
<dt>ONLYINCOMPOUND flag</p>
<dd>Suffixes signed with ONLYINCOMPOUND flag may be only inside of compounds (Fuge-elements in German, fogemorphemes in Swedish). ONLYINCOMPOUND flag works also with words (see tests/onlyincompound.*). Note: also valuable to flag compounding parts which are not correct as a word by itself.</p>
<dt>COMPOUNDPERMITFLAG flag</p>
<dd>Prefixes are allowed at the beginning of compounds, suffixes are allowed at the end of compounds by default. Affixes with COMPOUNDPERMITFLAG may be inside of compounds.</p>
<dt>COMPOUNDFORBIDFLAG flag</p>
<dd>Suffixes with this flag forbid compounding of the affixed word.</p>
<dt>COMPOUNDROOT flag</p>
<dd>COMPOUNDROOT flag signs the compounds in the dictionary (Now it is used only in the Hungarian language specific code).</p>
<dt>COMPOUNDWORDMAX number</p>
<dd>Set maximum word count in a compound word. (Default is unlimited.)</p>
<dt>CHECKCOMPOUNDDUP</p>
<dd>Forbid word duplication in compounds (e.g. foofoo).</p>
<dt>CHECKCOMPOUNDREP</p>
<dd>Forbid compounding, if the (usually bad) compound word may be a non compound word with a REP fault. Useful for languages with `compound friendly&#8217; orthography.</p>
<dt>CHECKCOMPOUNDCASE</p>
<dd>Forbid upper case characters at word boundaries in compounds.</p>
<dt>CHECKCOMPOUNDTRIPLE</p>
<dd>Forbid compounding, if compound word contains triple repeating letters (e.g. foo|ox or xo|oof). Bug: missing multi-byte character support in UTF-8 encoding (works only for 7-bit ASCII characters).</p>
<dt>SIMPLIFIEDTRIPLE</p>
<dd>Allow simplified 2-letter forms of the compounds forbidden by CHECKCOMPOUNDTRIPLE. It&#8217;s useful for Swedish and Norwegian (and for the old German orthography: Schiff|fahrt -&gt; Schiffahrt).</p>
<dt>CHECKCOMPOUNDPATTERN number_of_checkcompoundpattern_definitions</p>
<dd>
<dt>CHECKCOMPOUNDPATTERN endchars[/flag] beginchars[/flag] [replacement]</p>
<dd>Forbid compounding, if the first word in the compound ends with endchars, and next word begins with beginchars and (optionally) they have the requested flags. The optional replacement parameter allows simplified compound form. </p>
<p> The special &quot;endchars&quot; pattern 0 (zero) limits the rule to the unmodified stems (stems and stems with zero affixes):</dl>
<dl>
<dd>
<pre>CHECKCOMPOUNDPATTERN 0/x /y</pre>
</dl>
<p> Note: COMPOUNDMIN doesn&#8217;t work correctly with the compound word alternation, so it may need to set COMPOUNDMIN to lower value.</p>
<dl>
<dt>FORCEUCASE flag</p>
<dd>Last word part of a compound with flag FORCEUCASE forces capitalization of the whole compound word. Eg. Dutch word &quot;straat&quot; (street) with FORCEUCASE flags will allowed only in capitalized compound forms, according to the Dutch spelling rules for proper names.</p>
<dt>COMPOUNDSYLLABLE max_syllable vowels</p>
<dd>Need for special compounding rules in Hungarian. First parameter is the maximum syllable number, that may be in a compound, if words in compounds are more than COMPOUNDWORDMAX. Second parameter is the list of vowels (for calculating syllables).</p>
<dt>SYLLABLENUM flags</p>
<dd>Need for special compounding rules in Hungarian.</dl>
<h2>Affix File Options For Affix Creation</h2>
<dl>
<dt>PFX flag cross_product number</p>
<dd>
<dt>PFX flag stripping prefix [condition [morphological_fields&#8230;]]</p>
<dd>
<dt>SFX flag cross_product number</p>
<dd>
<dt>SFX flag stripping suffix [condition [morphological_fields&#8230;]]</p>
<dd>An affix is either a prefix or a suffix attached to root words to make other words. We can define affix classes with arbitrary number affix rules. Affix classes are signed with affix flags. The first line of an affix class definition is the header. The fields of an affix class header: </p>
<p> (0) Option name (PFX or SFX) </p>
<p> (1) Flag (name of the affix class) </p>
<p> (2) Cross product (permission to combine prefixes and suffixes). Possible values: Y (yes) or N (no) </p>
<p> (3) Line count of the following rules. </p>
<p> Fields of an affix rules: </p>
<p> (0) Option name </p>
<p> (1) Flag </p>
<p> (2) stripping characters from beginning (at prefix rules) or end (at suffix rules) of the word </p>
<p> (3) affix (optionally with flags of continuation classes, separated by a slash) </p>
<p> (4) condition. </p>
<p> Zero stripping or affix are indicated by zero. Zero condition is indicated by dot. Condition is a simplified, regular expression-like pattern, which must be met before the affix can be applied. (Dot signs an arbitrary character. Characters in braces sign an arbitrary character from the character subset. Dash hasn&#8217;t got special meaning, but circumflex (^) next the first brace sets the complementer character set.) </p>
<p> (5) Optional morphological fields separated by spaces or tabulators. </p>
</dl>
<h2>Affix File Other Options</h2>
<dl>
<dt>CIRCUMFIX flag</p>
<dd>Affixes signed with CIRCUMFIX flag may be on a word when this word also has a prefix with CIRCUMFIX flag and vice versa (see circumfix.* test files in the source distribution).</p>
<dt>FORBIDDENWORD flag</p>
<dd>This flag signs forbidden word form. Because affixed forms are also forbidden, we can subtract a subset from set of the accepted affixed and compound words. Note: usefull to forbid erroneous words, generated by the compounding mechanism.</p>
<dt>FULLSTRIP</p>
<dd>With FULLSTRIP, affix rules can strip full words, not only one less characters, before adding the affixes, see fullstrip.* test files in the source distribution). Note: conditions may be word length without FULLSTRIP, too.</p>
<dt>KEEPCASE flag</p>
<dd>Forbid uppercased and capitalized forms of words signed with KEEPCASE flags. Useful for special orthographies (measurements and currency often keep their case in uppercased texts) and writing systems (e.g. keeping lower case of IPA characters). Also valuable for words erroneously written in the wrong case. </p>
<p> Note: With CHECKSHARPS declaration, words with sharp s and KEEPCASE flag may be capitalized and uppercased, but uppercased forms of these words may not contain sharp s, only SS. See germancompounding example in the tests directory of the Hunspell distribution. </p>
<dt>ICONV number_of_ICONV_definitions</p>
<dd>
<dt>ICONV pattern pattern2</p>
<dd>Define input conversion table. Note: useful to convert one type of quote to another one, or change ligature.</p>
<dt>OCONV number_of_OCONV_definitions</p>
<dd>
<dt>OCONV pattern pattern2</p>
<dd>Define output conversion table.</p>
<dt>LEMMA_PRESENT flag</p>
<dd>Deprecated. Use &quot;st:&quot; field instead of LEMMA_PRESENT.</p>
<dt>NEEDAFFIX flag</p>
<dd>This flag signs virtual stems in the dictionary, words only valid when affixed. Except, if the dictionary word has a homonym or a zero affix. NEEDAFFIX works also with prefixes and prefix + suffix combinations (see tests/pseudoroot5.*).</p>
<dt>PSEUDOROOT flag</p>
<dd>Deprecated. (Former name of the NEEDAFFIX option.)</p>
<dt>SUBSTANDARD flag</p>
<dd>SUBSTANDARD flag signs affix rules and dictionary words (allomorphs) not used in morphological generation (and in suggestion in the future versions). See also NOSUGGEST.</p>
<dt>WORDCHARS characters</p>
<dd>WORDCHARS extends tokenizer of Hunspell command line interface with additional word character. For example, dot, dash, n-dash, numbers, percent sign are word character in Hungarian.</p>
<dt>CHECKSHARPS</p>
<dd>SS letter pair in uppercased (German) words may be upper case sharp s (ß). Hunspell can handle this special casing with the CHECKSHARPS declaration (see also KEEPCASE flag and tests/germancompounding example) in both spelling and suggestion. </p>
</dl>
<h2>Morphological analysis</h2>
<p>Hunspell&#8217;s dictionary items and affix rules may have optional space or tabulator separated morphological description fields, started with 3-character (two letters and a colon) field IDs: </p>
<dl>
<dd>
<pre> word/flags po:noun is:nom</pre>
</dl>
<p> Example: We define a simple resource with morphological informations, a derivative suffix (ds:) and a part of speech category (po:): </p>
<p> Affix file: </p>
<dl>
<dd>
<pre> SFX X Y 1
 SFX X 0 able . ds:able</pre>
</dl>
<p> Dictionary file: </p>
<dl>
<dd>
<pre> drink/X po:verb</pre>
</dl>
<p> Test file: </p>
<dl>
<dd>
<pre> drink
 drinkable</pre>
</dl>
<p> Test: </p>
<dl>
<dd>
<pre> $ analyze test.aff test.dic test.txt
 &gt; drink
 analyze(drink) = po:verb
 stem(drink) = po:verb
 &gt; drinkable
 analyze(drinkable) = po:verb ds:able
 stem(drinkable) = drinkable</pre>
</dl>
<p> You can see in the example, that the analyzer concatenates the morphological fields in <i>item and arrangement</i> style.</p>
<h2>Optional data fields</h2>
<p>Default morphological and other IDs (used in suggestion, stemming and morphological generation):</p>
<dl>
<dt>ph:</p>
<dd>Alternative transliteration for better suggestion. It&#8217;s useful for words with foreign pronunciation. (Dictionary based phonetic suggestion.) For example: </p>
</dl>
<dl>
<dd>
<pre>Marseille ph:maarsayl</pre>
</dl>
<dl>
<dt>st:</p>
<dd>Stem. Optional: default stem is the dictionary item in morphological analysis. Stem field is useful for virtual stems (dictionary words with NEEDAFFIX flag) and morphological exceptions instead of new, single used morphological rules.</dl>
<dl>
<dd>
<pre>feet st:foot is:plural
mice st:mouse is:plural
teeth st:tooth is:plural</pre>
</dl>
<p> Word forms with multiple stems need multiple dictionary items: </p>
<dl>
<dd>
<pre>lay po:verb st:lie is:past_2
lay po:verb is:present
lay po:noun</pre>
</dl>
<dl>
<dt>al:</p>
<dd>Allomorph(s). A dictionary item is the stem of its allomorphs. Morphological generation needs stem, allomorph and affix fields.</dl>
<dl>
<dd>
<pre>sing al:sang al:sung
sang st:sing
sung st:sing</pre>
</dl>
<dl>
<dt>po:</p>
<dd>Part of speech category.</p>
<dt>ds:</p>
<dd>Derivational suffix(es). Stemming doesn&#8217;t remove derivational suffixes. Morphological generation depends on the order of the suffix fields. </p>
<p> In affix rules: </p>
</dl>
<dl>
<dd>
<pre>SFX Y Y 1
SFX Y 0 ly . ds:ly_adj</pre>
</dl>
<p> In the dictionary: </p>
<dl>
<dd>
<pre>ably st:able ds:ly_adj
able al:ably</pre>
</dl>
<dl>
<dt>is:</p>
<dd>Inflectional suffix(es). All inflectional suffixes are removed by stemming. Morphological generation depends on the order of the suffix fields. </p>
</dl>
<dl>
<dd>
<pre>feet st:foot is:plural</pre>
</dl>
<dl>
<dt>ts:</p>
<dd>Terminal suffix(es). Terminal suffix fields are inflectional suffix fields &quot;removed&quot; by additional (not terminal) suffixes. </p>
<p> Useful for zero morphemes and affixes removed by splitting rules. </p>
</dl>
<dl>
<dd>
<pre>work/D ts:present</pre>
</dl>
<dl>
<dd>
<pre>SFX D Y 2
SFX D 0 ed . is:past_1
SFX D 0 ed . is:past_2</pre>
</dl>
<p> Typical example of the terminal suffix is the zero morpheme of the nominative case. </p>
<dl>
<dt>sp:</p>
<dd>Surface prefix. Temporary solution for adding prefixes to the stems and generated word forms. See tests/morph.* example. </p>
<dt>pa:</p>
<dd>Parts of the compound words. Output fields of morphological analysis for stemming.</p>
<dt>dp:</p>
<dd>Planned: derivational prefix.</p>
<dt>ip:</p>
<dd>Planned: inflectional prefix.</p>
<dt>tp:</p>
<dd>Planned: terminal prefix. </p>
</dl>
<h2>Twofold suffix stripping</h2>
<p>Ispell&#8217;s original algorithm strips only one suffix. Hunspell can strip another one yet (or a plus prefix in COMPLEXPREFIXES mode). </p>
<p> The twofold suffix stripping is a significant improvement in handling of immense number of suffixes, that characterize agglutinative languages. </p>
<p> A second `s&#8217; suffix (affix class Y) will be the continuation class of the suffix `able&#8217; in the following example: </p>
<dl>
<dd>
<pre> SFX Y Y 1
 SFX Y 0 s .
 SFX X Y 1
 SFX X 0 able/Y .</pre>
</dl>
<p> Dictionary file: </p>
<dl>
<dd>
<pre> drink/X</pre>
</dl>
<p> Test file: </p>
<dl>
<dd>
<pre> drink
 drinkable
 drinkables</pre>
</dl>
<p> Test: </p>
<dl>
<dd>
<pre> $ hunspell -m -d test &lt;test.txt
 drink st:drink
 drinkable st:drink fl:X
 drinkables st:drink fl:X fl:Y</pre>
</dl>
<p> Theoretically with the twofold suffix stripping needs only the square root of the number of suffix rules, compared with a Hunspell implementation. In our practice, we could have elaborated the Hungarian inflectional morphology with twofold suffix stripping.</p>
<h2>Extended affix classes</h2>
<p>Hunspell can handle more than 65000 affix classes. There are three new syntax for giving flags in affix and dictionary files. </p>
<p> <i>FLAG long</i> command sets 2-character flags: </p>
<dl>
<dd>
<pre> FLAG long
 SFX Y1 Y 1
 SFX Y1 0 s 1</pre>
</dl>
<p> Dictionary record with the Y1, Z3, F? flags: </p>
<dl>
<dd>
<pre> foo/Y1Z3F?</pre>
</dl>
<p> <i>FLAG num</i> command sets numerical flags separated by comma: </p>
<dl>
<dd>
<pre> FLAG num
 SFX 65000 Y 1
 SFX 65000 0 s 1</pre>
</dl>
<p> Dictionary example: </p>
<dl>
<dd>
<pre> foo/65000,12,2756</pre>
</dl>
<p> The third one is the Unicode character flags.</p>
<h2>Homonyms</h2>
<p>Hunspell&#8217;s dictionary can contain repeating elements that are homonyms: </p>
<dl>
<dd>
<pre> work/A po:verb
 work/B po:noun</pre>
</dl>
<p> An affix file: </p>
<dl>
<dd>
<pre> SFX A Y 1
 SFX A 0 s . sf:sg3
 SFX B Y 1
 SFX B 0 s . is:plur</pre>
</dl>
<p> Test file: </p>
<dl>
<dd>
<pre> works</pre>
</dl>
<p> Test: </p>
<dl>
<dd>
<pre> $ hunspell -d test -m &lt;testwords
 work st:work po:verb is:sg3
 work st:work po:noun is:plur</pre>
</dl>
<p> This feature also gives a way to forbid illegal prefix/suffix combinations.</p>
<h2>Prefix&#8211;suffix dependencies</h2>
<p>An interesting side-effect of multi-step stripping is, that the appropriate treatment of circumfixes now comes for free. For instance, in Hungarian, superlatives are formed by simultaneous prefixation of <i>leg-</i> and suffixation of <i>-bb</i> to the adjective base. A problem with the one-level architecture is that there is no way to render lexical licensing of particular prefixes and suffixes interdependent, and therefore incorrect forms are recognized as valid, i.e. *<i>legvén</i> = <i>leg</i> + <i>vén</i> `old&#8217;. Until the introduction of clusters, a special treatment of the superlative had to be hardwired in the earlier <code>HunSpell</code> code. This may have been legitimate for a single case, but in fact prefix&#8211;suffix dependences are ubiquitous in category-changing derivational patterns (cf. English <i>payable</i>, <i>non-payable</i> but <i>*non-pay</i> or <i>drinkable</i>, <i>undrinkable</i> but <i>*undrink</i>). In simple words, here, the prefix <i>un-</i> is legitimate only if the base <i>drink</i> is suffixed with <i>-able</i>. If both these patters are handled by on-line affix rules and affix rules are checked against the base only, there is no way to express this dependency and the system will necessarily over- or undergenerate. </p>
<p> In next example, suffix class R have got a prefix `continuation&#8217; class (class P). </p>
<dl>
<dd>
<pre>PFX P Y 1
PFX P 0 un . [prefix_un]+
SFX S Y 1
SFX S 0 s . +PL
SFX Q Y 1
SFX Q 0 s . +3SGV
SFX R Y 1
SFX R 0 able/PS . +DER_V_ADJ_ABLE</pre>
</dl>
<p> Dictionary: </p>
<dl>
<dd>
<pre>2
drink/RQ [verb]
drink/S [noun]</pre>
</dl>
<p> Morphological analysis: </p>
<dl>
<dd>
<pre>&gt; drink
drink[verb]
drink[noun]
&gt; drinks
drink[verb]+3SGV
drink[noun]+PL
&gt; drinkable
drink[verb]+DER_V_ADJ_ABLE
&gt; drinkables
drink[verb]+DER_V_ADJ_ABLE+PL
&gt; undrinkable
[prefix_un]+drink[verb]+DER_V_ADJ_ABLE
&gt; undrinkables
[prefix_un]+drink[verb]+DER_V_ADJ_ABLE+PL
&gt; undrink
Unknown word.
&gt; undrinks
Unknown word.</pre>
</dl>
<h2>Circumfix</h2>
<p>Conditional affixes implemented by a continuation class are not enough for circumfixes, because a circumfix is one affix in morphology. We also need CIRCUMFIX option for correct morphological analysis. </p>
<dl>
<dd>
<pre># circumfixes: ~ obligate prefix/suffix combinations
# superlative in Hungarian: leg- (prefix) AND -bb (suffix)
# nagy, nagyobb, legnagyobb, legeslegnagyobb
# (great, greater, greatest, most greatest)
CIRCUMFIX X
PFX A Y 1
PFX A 0 leg/X .
PFX B Y 1
PFX B 0 legesleg/X .
SFX C Y 3
SFX C 0 obb . +COMPARATIVE
SFX C 0 obb/AX . +SUPERLATIVE
SFX C 0 obb/BX . +SUPERSUPERLATIVE</pre>
</dl>
<p> Dictionary: </p>
<dl>
<dd>
<pre>1
nagy/C [MN]</pre>
</dl>
<p> Analysis: </p>
<dl>
<dd>
<pre>&gt; nagy
nagy[MN]
&gt; nagyobb
nagy[MN]+COMPARATIVE
&gt; legnagyobb
nagy[MN]+SUPERLATIVE
&gt; legeslegnagyobb
nagy[MN]+SUPERSUPERLATIVE</pre>
</dl>
<h2>Compounds</h2>
<p>Allowing free compounding yields decrease in precision of recognition, not to mention stemming and morphological analysis. Although lexical switches are introduced to license compounding of bases by <code>Ispell</code>, this proves not to be restrictive enough. For example: </p>
<dl>
<dd>
<pre># affix file
COMPOUNDFLAG X</pre>
</dl>
<dl>
<dd>
<pre>2
foo/X
bar/X</pre>
</dl>
<p> With this resource, <i>foobar</i> and <i>barfoo</i> also are accepted words. </p>
<p> This has been improved upon with the introduction of direction-sensitive compounding, i.e., lexical features can specify separately whether a base can occur as leftmost or rightmost constituent in compounds. This, however, is still insufficient to handle the intricate patterns of compounding, not to mention idiosyncratic (and language specific) norms of hyphenation. </p>
<p> The <code>Hunspell</code> algorithm currently allows any affixed form of words, which are lexically marked as potential members of compounds. <code>Hunspell</code> improved this, and its recursive compound checking rules makes it possible to implement the intricate spelling conventions of Hungarian compounds. For example, using COMPOUNDWORDMAX, COMPOUNDSYLLABLE, COMPOUNDROOT, SYLLABLENUM options can be set the noteworthy Hungarian `6-3&#8242; rule. Further example in Hungarian, derivate suffixes often modify compounding properties. Hunspell allows the compounding flags on the affixes, and there are two special flags (COMPOUNDPERMITFLAG and (COMPOUNDFORBIDFLAG) to permit or prohibit compounding of the derivations. </p>
<p> Suffixes with this flag forbid compounding of the affixed word. </p>
<p> We also need several Hunspell features for handling German compounding: </p>
<dl>
<dd>
<pre># German compounding
# set language to handle special casing of German sharp s
LANG de_DE
# compound flags
COMPOUNDBEGIN U
COMPOUNDMIDDLE V
COMPOUNDEND W
# Prefixes are allowed at the beginning of compounds,
# suffixes are allowed at the end of compounds by default:
# (prefix)?(root)+(affix)?
# Affixes with COMPOUNDPERMITFLAG may be inside of compounds.
COMPOUNDPERMITFLAG P
# for German fogemorphemes (Fuge-element)
# Hint: ONLYINCOMPOUND is not required everywhere, but the
# checking will be a little faster with it.
ONLYINCOMPOUND X
# forbid uppercase characters at compound word bounds
CHECKCOMPOUNDCASE
# for handling Fuge-elements with dashes (Arbeits-) 
# dash will be a special word
COMPOUNDMIN 1
WORDCHARS -
# compound settings and fogemorpheme for `Arbeit'
SFX A Y 3
SFX A 0 s/UPX .
SFX A 0 s/VPDX .
SFX A 0 0/WXD .
SFX B Y 2
SFX B 0 0/UPX .
SFX B 0 0/VWXDP .
# a suffix for `Computer'
SFX C Y 1
SFX C 0 n/WD .
# for forbid exceptions (*Arbeitsnehmer)
FORBIDDENWORD Z
# dash prefix for compounds with dash (Arbeits-Computer)
PFX - Y 1
PFX - 0 -/P .
# decapitalizing prefix
# circumfix for positioning in compounds
PFX D Y 29
PFX D A a/PX A
PFX D Ä ä/PX Ä
 .
 .
PFX D Y y/PX Y
PFX D Z z/PX Z</pre>
</dl>
<p> Example dictionary: </p>
<dl>
<dd>
<pre>4
Arbeit/A-
Computer/BC-
-/W
Arbeitsnehmer/Z</pre>
</dl>
<p> Accepted compound compound words with the previous resource: </p>
<dl>
<dd>
<pre>Computer
Computern
Arbeit
Arbeits-
Computerarbeit
Computerarbeits-
Arbeitscomputer
Arbeitscomputern
Computerarbeitscomputer
Computerarbeitscomputern
Arbeitscomputerarbeit
Computerarbeits-Computer
Computerarbeits-Computern</pre>
</dl>
<p> Not accepted compoundings: </p>
<dl>
<dd>
<pre>computer
arbeit
Arbeits
arbeits
ComputerArbeit
ComputerArbeits
Arbeitcomputer
ArbeitsComputer
Computerarbeitcomputer
ComputerArbeitcomputer
ComputerArbeitscomputer
Arbeitscomputerarbeits
Computerarbeits-computer
Arbeitsnehmer</pre>
</dl>
<p> This solution is still not ideal, however, and will be replaced by a pattern-based compound-checking algorithm which is closely integrated with input buffer tokenization. Patterns describing compounds come as a separate input resource that can refer to high-level properties of constituent parts (e.g. the number of syllables, affix flags, and containment of hyphens). The patterns are matched against potential segmentations of compounds to assess wellformedness.</p>
<h2>Unicode character encoding</h2>
<p>Both <code>Ispell</code> and <code>Myspell</code> use 8-bit ASCII character encoding, which is a major deficiency when it comes to scalability. Although a language like Hungarian has a standard ASCII character set (ISO 8859-2), it fails to allow a full implementation of Hungarian orthographic conventions. For instance, the &#8216;&#8211;&#8216; symbol (n-dash) is missing from this character set contrary to the fact that it is not only the official symbol to delimit parenthetic clauses in the language, but it can be in compound words as a special &#8216;big&#8217; hyphen. </p>
<p> MySpell has got some 8-bit encoding tables, but there are languages without standard 8-bit encoding, too. For example, a lot of African languages have non-latin or extended latin characters. </p>
<p> Similarly, using the original spelling of certain foreign names like <i>Ångström</i> or <i>Molière</i> is encouraged by the Hungarian spelling norm, and, since characters &#8216;Å&#8217; and &#8216;è&#8217; are not part of ISO 8859-2, when they combine with inflections containing characters only in ISO 8859-2 (like elative <i>-ből</i>, allative <i>-től</i> or delative <i>-ről</i> with double acute), these result in words (like <i>Ångströmről</i> or <i>Molière-től.</i>) that can not be encoded using any single ASCII encoding scheme. </p>
<p> The problems raised in relation to 8-bit ASCII encoding have long been recognized by proponents of Unicode. It is clear that trading efficiency for encoding-independence has its advantages when it comes a truly multi-lingual application. There is implemented a memory and time efficient Unicode handling in Hunspell. In non-UTF-8 character encodings Hunspell works with the original 8-bit strings. In UTF-8 encoding, affixes and words are stored in UTF-8, during the analysis are handled in mostly UTF-8, under condition checking and suggestion are converted to UTF-16. Unicode text analysis and spell checking have a minimal (0-20%) time overhead and minimal or reasonable memory overhead depends from the language (its UTF-8 encoding and affixation).</p>
<h2>Conversion of aspell dictionaries</h2>
<p>Aspell dictionaries can be easily converted into hunspell. Conversion steps: </p>
<p> <code>dictionary (xx.cwl -&gt; xx.wl):</code> </p>
<pre>preunzip xx.cwl
wc -l &lt; xx.wl &gt; xx.dic
cat xx.wl &gt;&gt; xx.dic</pre>
<p><code>affix file</code> </p>
<p> If the affix file exists, copy it: </p>
<pre>cp xx_affix.dat xx.aff</pre>
<p>If not, create it with the suitable character encoding (see xx.dat) </p>
<pre>echo &quot;SET ISO8859-x&quot; &gt; xx.aff</pre>
<p>or </p>
<pre>echo &quot;SET UTF-8&quot; &gt; xx.aff</pre>
<p>It&#8217;s useful to add a TRY option with the characters of the dictionary with frequency order to set edit distance suggestions: </p>
<pre>echo &quot;TRY qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM&quot; &gt;&gt;xx.aff</pre>
<h2>See Also</h2>
<p><code>hunspell (1),</code> <code>ispell (1),</code> <code>ispell (4)</code> </p>
