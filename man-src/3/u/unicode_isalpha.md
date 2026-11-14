---
title: "unicode_isalpha(3)"
name: "unicode_isalpha"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_isalpha/"
description: "unicode_category_lookup, unicode_isalnum, unicode_isalpha, unicode_isblank, unicode_isdigit, unicode_isgraph, unicode_islower, unicode_ispunct, unicode_isspace, unicode_isupper – unicode character ..."
---

<p>unicode_category_lookup, unicode_isalnum, unicode_isalpha, unicode_isblank, unicode_isdigit, unicode_isgraph, unicode_islower, unicode_ispunct, unicode_isspace, unicode_isupper &#8211; unicode character categorization</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

uint32_t unicode_category_lookup(unicode_char c);

int unicode_isalnum(unicode_char c);

int unicode_isalpha(unicode_char c);

int unicode_isblank(unicode_char c);

int unicode_isdigit(unicode_char c);

int unicode_isgraph(unicode_char c);

int unicode_islower(unicode_char c);

int unicode_ispunct(unicode_char c);

int unicode_isspace(unicode_char c);

int unicode_isupper(unicode_char c);</code></pre>
<h2>Description</h2>
<p><code>unicode_category_lookup</code>() looks up the m[blue]<code>unicode character&#8217;s categorization</code>m[]<font SIZE="-2">[1]</font>. <code>unicode_category_lookup</code>() returns a 32 bit value. The value&#8217;s</p>
<dd>UNICODE_CATEGORY_1 bits specify the first level of the unicode character&#8217;s category, with UNICODE_CATEGORY_2, UNICODE_CATEGORY_3, and UNICODE_CATEGORY_4 bits specifying the 2nd, 3rd, and 4th level, if given. A value of 0 for each corresponding bit set indicates that no category is specified for this level, for this character; otherwise the possible values are defined in &lt;courier-unicode.h&gt;. </p>
<p> The remaining functions implement comparable equivalents of their non-unicode versions in the standard C library, as follows: </p>
<p> <code>unicode_isalnum</code>()</p>
<dl>
<dd>Returns non-0 for all <code>unicode_isalpha</code>() or <code>unicode_isdigit</code>().</dl>
<p> <code>unicode_isalpha</code>()</p>
<dl>
<dd>Returns non-0 for all UNICODE_CATEGORY_1_LETTER.</dl>
<p> <code>unicode_isblank</code>()</p>
<dl>
<dd>Return non-0 for TAB, and all UNICODE_CATEGORY_2_SPACE.</dl>
<p> <code>unicode_isdigit</code>()</p>
<dl>
<dd>Returns non-0 for all UNICODE_CATEGORY_1_NUMBER | UNICODE_CATEGORY_2_DIGIT, only (no third categories).</dl>
<p> <code>unicode_isgraph</code>()</p>
<dl>
<dd>Returns non-0 for all codepoints above SPACE which are not <code>unicode_isspace</code>().</dl>
<p> <code>unicode_islower</code>()</p>
<dl>
<dd>Returns non-0 for all <code>unicode_isalpha</code>() for which the character is equal to <code><a href="/docs/linux/man/3-unicode_lc/">unicode_lc</a></code>(3) of itself.</dl>
<p> <code>unicode_ispunct</code>()</p>
<dl>
<dd>Returns non-0 for all UNICODE_CATEGORY_1_PUNCTUATION.</dl>
<p> <code>unicode_isspace</code>()</p>
<dl>
<dd>Returns non-0 for unicode_isblank() or for unicode characters with linebreaking properties of BK, CR, LF, NL, and SP.</dl>
<p> <code>unicode_isupper</code>()</p>
<dl>
<dd>Returns non-0 for all <code>unicode_isalpha</code>() for which the character is equal to <code><a href="/docs/linux/man/3-unicode_uc/">unicode_uc</a></code>(3) of itself.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode_convert_tocase/">unicode_convert_tocase</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>unicode character&#8217;s categorization</p>
<dl>
<dd><a rel="nofollow" href="http://unicode.org/notes/tn36/">http://unicode.org/notes/tn36/</a></dl>
