---

title: "locale(7)"
name: "locale"
section: "7"
letter: "l"
url: "/docs/linux/man/7-locale/"
description: "locale – description of multilanguage support"
---

<p>locale &#8211; description of multilanguage support </p>
<pre><code>
 #include &lt;locale.h&gt; 
</code></pre>
<p> A locale is a set of language and cultural rules. These cover aspects such as language for messages, different character sets, lexicographic conventions, and so on. A program needs to be able to determine its locale and act accordingly to be portable to different cultures. </p>
<p>The header <i>&lt;locale.h&gt;</i> declares data types, functions and macros which are useful in this task. </p>
<p>The functions it declares are <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) to set the current locale, and <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3) to get information about number formatting. </p>
<p>There are different categories for locale information a program might need; they are declared as macros. Using them as the first argument to the <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) function, it is possible to set one of these to the desired locale: </p>
<dl>
<dt><code>LC_ADDRESS</code> (GNU extension, since glibc 2.2) </dt>
<dd> <p> Change settings that describe the formats (e.g., postal addresses) used to describe locations and geography-related items. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_ADDRESS_COUNTRY_NAME</code> (country name, in the language of the locale) and <code>_NL_ADDRESS_LANG_NAME</code> (language name, in the language of the locale), which return strings such as &quot;Deutschland&quot; and &quot;Deutsch&quot; (for German-language locales). (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.) </p>
 </dd>
<dt><code>LC_COLLATE</code></dt>
<dd> <p> This category governs the collation rules used for sorting and regular expressions, including character equivalence classes and multicharacter collating elements. This locale category changes the behavior of the functions <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3) and <code><a href="/docs/linux/man/3-strxfrm/">strxfrm</a></code>(3), which are used to compare strings in the local alphabet. For example, the German sharp s is sorted as &quot;ss&quot;. </p>
 </dd>
<dt><code>LC_CTYPE</code></dt>
<dd> <p> This category determines the interpretation of byte sequences as characters (e.g., single versus multibyte characters), character classifications (e.g., alphabetic or digit), and the behavior of character classes. On glibc systems, this category also determines the character transliteration rules for <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) and <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3). It changes the behavior of the character handling and classification functions, such as <code><a href="/docs/linux/man/3-isupper/">isupper</a></code>(3) and <code><a href="/docs/linux/man/3-toupper/">toupper</a></code>(3), and the multibyte character functions such as <code><a href="/docs/linux/man/3-mblen/">mblen</a></code>(3) or <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3). </p>
 </dd>
<dt><code>LC_IDENTIFICATION</code> (GNU extension, since glibc 2.2) </dt>
<dd> <p> Change settings that relate to the metadata for the locale. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_IDENTIFICATION_TITLE</code> (title of this locale document) and <code>_NL_IDENTIFICATION_TERRITORY</code> (geographical territory to which this locale document applies), which might return strings such as &quot;English locale for the USA&quot; and &quot;USA&quot;. (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.) </p>
 </dd>
<dt><code>LC_MONETARY</code></dt>
<dd> <p> This category determines the formatting used for monetary-related numeric values. This changes the information returned by <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), which describes the way numbers are usually printed, with details such as decimal point versus decimal comma. This information is internally used by the function <code><a href="/docs/linux/man/3-strfmon/">strfmon</a></code>(3). </p>
 </dd>
<dt><code>LC_MESSAGES</code></dt>
<dd> <p> This category affects the language in which messages are displayed and what an affirmative or negative answer looks like. The GNU C library contains the <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), <code><a href="/docs/linux/man/3-ngettext/">ngettext</a></code>(3), and <code><a href="/docs/linux/man/3-rpmatch/">rpmatch</a></code>(3) functions to ease the use of this information. The GNU gettext family of functions also obey the environment variable <code>LANGUAGE</code> (containing a colon-separated list of locales) if the category is set to a valid locale other than <code>&quot;C&quot;</code>. This category also affects the behavior of <code><a href="/docs/linux/man/3-catopen/">catopen</a></code>(3). </p>
 </dd>
<dt><code>LC_MEASUREMENT</code> (GNU extension, since glibc 2.2) </dt>
<dd> <p> Change the settings relating to the measurement system in the locale (i.e., metric versus US customary units). Applications can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve the nonstandard <code>_NL_MEASUREMENT_MEASUREMENT</code> element, which returns a pointer to a character that has the value 1 (metric) or 2 (US customary units). </p>
 </dd>
<dt><code>LC_NAME</code> (GNU extension, since glibc 2.2) </dt>
<dd> <p> Change settings that describe the formats used to address persons. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_NAME_NAME_MR</code> (general salutation for men) and <code>_NL_NAME_NAME_MS</code> (general salutation for women) elements, which return strings such as &quot;Herr&quot; and &quot;Frau&quot; (for German-language locales). (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.) </p>
 </dd>
<dt><code>LC_NUMERIC</code></dt>
<dd> <p> This category determines the formatting rules used for nonmonetary numeric values---for example, the thousands separator and the radix character (a period in most English-speaking countries, but a comma in many other regions). It affects functions such as <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3), and <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3). This information can also be read with the <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3) function. </p>
 </dd>
<dt><code>LC_PAPER</code> (GNU extension, since glibc 2.2) </dt>
<dd> <p> Change the settings relating to the dimensions of the standard paper size (e.g., US letter versus A4). Applications that need the dimensions can obtain them by using <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve the nonstandard <code>_NL_PAPER_WIDTH</code> and <code>_NL_PAPER_HEIGHT</code> elements, which return <i>int</i> values specifying the dimensions in millimeters. </p>
 </dd>
<dt><code>LC_TELEPHONE</code> (GNU extension, since glibc 2.2) </dt>
<dd> <p> Change settings that describe the formats to be used with telephone services. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_TELEPHONE_INT_PREFIX</code> (international prefix used to call numbers in this locale), which returns a string such as &quot;49&quot; (for Germany). (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.) </p>
 </dd>
<dt><code>LC_TIME</code></dt>
<dd> <p> This category governs the formatting used for date and time values. For example, most of Europe uses a 24-hour clock versus the 12-hour clock used in the United States. The setting of this category affects the behavior of functions such as <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) and <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3). </p>
 </dd>
<dt><code>LC_ALL</code></dt>
<dd> <p> All of the above. </p>
 </dd></dl>
<p>If the second argument to <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) is an empty string, <i>&quot;&quot;</i>, for the default locale, it is determined using the following steps: </p>
<dl>
<dt>1.</dt>
<dd> <p> If there is a non-null environment variable <code>LC_ALL</code>, the value of <code>LC_ALL</code> is used. </p>
 </dd>
<dt>2.</dt>
<dd> <p> If an environment variable with the same name as one of the categories above exists and is non-null, its value is used for that category. </p>
 </dd>
<dt>3.</dt>
<dd> <p> If there is a non-null environment variable <code>LANG</code>, the value of <code>LANG</code> is used. </p>
 </dd></dl>
<p>Values about local numeric formatting is made available in a <i>struct lconv</i> returned by the <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3) function, which has the following declaration: </p>
<p>struct lconv { </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Numeric&nbsp;(nonmonetary)&nbsp;information&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*decimal_point;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Radix character&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*thousands_sep;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Separator for digit groups to left <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of radix character&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*grouping;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Each element is the number of digits in <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a group;&nbsp;elements with higher indices <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;are further left.&nbsp;<wbr>&nbsp;An element with value <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CHAR_MAX means that no further grouping <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is done.&nbsp;<wbr>&nbsp;An element with value 0 means <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;that the previous element is used for <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;all groups further left.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Remaining fields are for monetary information&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*int_curr_symbol;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;First three chars are a currency <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;symbol from ISO 4217.&nbsp;<wbr>&nbsp;Fourth char <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is the separator.&nbsp;<wbr>&nbsp;Fifth char <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is&nbsp;&#8216;\0&#8217;.&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*currency_symbol;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Local currency symbol&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*mon_decimal_point;&nbsp;/*&nbsp;Radix character&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*mon_thousands_sep;&nbsp;/*&nbsp;Like&nbsp;<i>thousands_sep</i>&nbsp;above&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*mon_grouping;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Like&nbsp;<i>grouping</i>&nbsp;above&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*positive_sign;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sign for positive values&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*negative_sign;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sign for negative values&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;int_frac_digits;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;International fractional digits&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;frac_digits;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Local fractional digits&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;p_cs_precedes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;1 if currency_symbol precedes a <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;positive value, 0 if succeeds&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;p_sep_by_space;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;1 if a space separates <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;currency_symbol from a positive <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;n_cs_precedes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;1 if currency_symbol precedes a <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;negative value, 0 if succeeds&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;n_sep_by_space;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;1 if a space separates <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;currency_symbol from a negative <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Positive and negative sign positions: <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 Parentheses surround the quantity and currency_symbol. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 The sign string precedes the quantity and currency_symbol. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 The sign string succeeds the quantity and currency_symbol. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 The sign string immediately precedes the currency_symbol. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 The sign string immediately succeeds the currency_symbol.&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;p_sign_posn; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;n_sign_posn; };  </p>
<h3>POSIX.1-2008 extensions to the locale API</h3>
<p> POSIX.1-2008 standardized a number of extensions to the locale API, based on implementations that first appeared in version 2.3 of the GNU C library. These extensions are designed to address the problem that the traditional locale APIs do not mix well with multithreaded applications and with applications that must deal with multiple locales. </p>
<p>The extensions take the form of new functions for creating and manipulating locale objects (<code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3), <code><a href="/docs/linux/man/3-freelocale/">freelocale</a></code>(3), <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3), and <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3)) and various new library functions with the suffix &quot;_l&quot; (e.g., <code><a href="/docs/linux/man/3-toupper_l/">toupper_l</a></code>(3)) that extend the traditional locale-dependent APIs (e.g., <code><a href="/docs/linux/man/3-toupper/">toupper</a></code>(3)) to allow the specification of a locale object that should apply when executing the function.  </p>
<h2>ENVIRONMENT</h2>
<p> The following environment variable is used by <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3) and <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), and thus affects all unprivileged localized programs: </p>
<dl>
<dt><code>LOCPATH</code></dt>
<dd> <p> A list of pathnames, separated by colons (&#8216;:&#8216;), that should be used to find locale data. If this variable is set, only the individual compiled locale data files from <code>LOCPATH</code> and the system default locale data path are used; any available locale archives are not used (see <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1)). The individual compiled locale data files are searched for under subdirectories which depend on the currently used locale. For example, when <i>en_GB.UTF-8</i> is used for a category, the following subdirectories are searched for, in this order: <i>en_GB.UTF-8</i>, <i>en_GB.utf8</i>, <i>en_GB</i>, <i>en.UTF-8</i>, <i>en.utf8</i>, and <i>en</i>. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/lib/locale/locale-archive</i></dt>
<dd> <p> Usual default locale archive location. </p>
 </dd>
<dt><i>/usr/lib/locale</i></dt>
<dd> <p> Usual default path for compiled individual locale files. </p>
 </dd></dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1), <code><a href="/docs/linux/man/3-catopen/">catopen</a></code>(3), <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), <code><a href="/docs/linux/man/3-mbstowcs/">mbstowcs</a></code>(3), <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3), <code><a href="/docs/linux/man/3-ngettext/">ngettext</a></code>(3), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/3-rpmatch/">rpmatch</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-strfmon/">strfmon</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/3-strxfrm/">strxfrm</a></code>(3), <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3), <code><a href="/docs/linux/man/3-wcstombs/">wcstombs</a></code>(3), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/7-unicode/">unicode</a></code>(7), <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
