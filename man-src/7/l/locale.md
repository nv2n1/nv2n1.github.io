---
title: "locale(7)"
name: "locale"
section: "7"
letter: "l"
url: "/docs/linux/man/7-locale/"
description: "locale – description of multilanguage support"
---

<p>locale &#8211; description of multilanguage support</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;locale.h&gt;</code></pre>
<h2>Description</h2>
<p>A locale is a set of language and cultural rules. These cover aspects such as language for messages, different character sets, lexicographic conventions, and so on. A program needs to be able to determine its locale and act accordingly to be portable to different cultures. The header <i>&lt;locale.h&gt;</i> declares data types, functions and macros which are useful in this task. The functions it declares are <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) to set the current locale, and <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3) to get information about number formatting. There are different categories for locale information a program might need; they are declared as macros. Using them as the first argument to the <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) function, it is possible to set one of these to the desired locale:</p>
<dl>
<dt><code>LC_ADDRESS</code> (GNU extension, since glibc 2.2)</p>
<dd>Change settings that describe the formats (e.g., postal addresses) used to describe locations and geography-related items. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_ADDRESS_COUNTRY_NAME</code> (country name, in the language of the locale) and <code>_NL_ADDRESS_LANG_NAME</code> (language name, in the language of the locale), which return strings such as &quot;Deutschland&quot; and &quot;Deutsch&quot; (for German-language locales). (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.)</p>
<dt><code>LC_COLLATE</code></p>
<dd>This category governs the collation rules used for sorting and regular expressions, including character equivalence classes and multicharacter collating elements. This locale category changes the behavior of the functions <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3) and <code><a href="/docs/linux/man/3-strxfrm/">strxfrm</a></code>(3), which are used to compare strings in the local alphabet. For example, the German sharp s is sorted as &quot;ss&quot;.</p>
<dt><code>LC_CTYPE</code></p>
<dd>This category determines the interpretation of byte sequences as characters (e.g., single versus multibyte characters), character classifications (e.g., alphabetic or digit), and the behavior of character classes. On glibc systems, this category also determines the character transliteration rules for <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) and <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3). It changes the behavior of the character handling and classification functions, such as <code><a href="/docs/linux/man/3-isupper/">isupper</a></code>(3) and <code><a href="/docs/linux/man/3-toupper/">toupper</a></code>(3), and the multibyte character functions such as <code><a href="/docs/linux/man/3-mblen/">mblen</a></code>(3) or <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3).</p>
<dt><code>LC_IDENTIFICATION</code> (GNU extension, since glibc 2.2)</p>
<dd>Change settings that relate to the metadata for the locale. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_IDENTIFICATION_TITLE</code> (title of this locale document) and <code>_NL_IDENTIFICATION_TERRITORY</code> (geographical territory to which this locale document applies), which might return strings such as &quot;English locale for the USA&quot; and &quot;USA&quot;. (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.)</p>
<dt><code>LC_MONETARY</code></p>
<dd>This category determines the formatting used for monetary-related numeric values. This changes the information returned by <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), which describes the way numbers are usually printed, with details such as decimal point versus decimal comma. This information is internally used by the function <code><a href="/docs/linux/man/3-strfmon/">strfmon</a></code>(3).</p>
<dt><code>LC_MESSAGES</code></p>
<dd>This category affects the language in which messages are displayed and what an affirmative or negative answer looks like. The GNU C library contains the <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), <code><a href="/docs/linux/man/3-ngettext/">ngettext</a></code>(3), and <code><a href="/docs/linux/man/3-rpmatch/">rpmatch</a></code>(3) functions to ease the use of this information. The GNU gettext family of functions also obey the environment variable <code>LANGUAGE</code> (containing a colon-separated list of locales) if the category is set to a valid locale other than <code>&quot;C&quot;</code>. This category also affects the behavior of <code><a href="/docs/linux/man/3-catopen/">catopen</a></code>(3).</p>
<dt><code>LC_MEASUREMENT</code> (GNU extension, since glibc 2.2)</p>
<dd>Change the settings relating to the measurement system in the locale (i.e., metric versus US customary units). Applications can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve the nonstandard <code>_NL_MEASUREMENT_MEASUREMENT</code> element, which returns a pointer to a character that has the value 1 (metric) or 2 (US customary units).</p>
<dt><code>LC_NAME</code> (GNU extension, since glibc 2.2)</p>
<dd>Change settings that describe the formats used to address persons. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_NAME_NAME_MR</code> (general salutation for men) and <code>_NL_NAME_NAME_MS</code> (general salutation for women) elements, which return strings such as &quot;Herr&quot; and &quot;Frau&quot; (for German-language locales). (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.)</p>
<dt><code>LC_NUMERIC</code></p>
<dd>This category determines the formatting rules used for nonmonetary numeric values&#8212;for example, the thousands separator and the radix character (a period in most English-speaking countries, but a comma in many other regions). It affects functions such as <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3), and <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3). This information can also be read with the <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3) function.</p>
<dt><code>LC_PAPER</code> (GNU extension, since glibc 2.2)</p>
<dd>Change the settings relating to the dimensions of the standard paper size (e.g., US letter versus A4). Applications that need the dimensions can obtain them by using <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve the nonstandard <code>_NL_PAPER_WIDTH</code> and <code>_NL_PAPER_HEIGHT</code> elements, which return <i>int</i> values specifying the dimensions in millimeters.</p>
<dt><code>LC_TELEPHONE</code> (GNU extension, since glibc 2.2)</p>
<dd>Change settings that describe the formats to be used with telephone services. Applications that need this information can use <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) to retrieve nonstandard elements, such as <code>_NL_TELEPHONE_INT_PREFIX</code> (international prefix used to call numbers in this locale), which returns a string such as &quot;49&quot; (for Germany). (Other element names are listed in <i>&lt;langinfo.h&gt;</i>.)</p>
<dt><code>LC_TIME</code></p>
<dd>This category governs the formatting used for date and time values. For example, most of Europe uses a 24-hour clock versus the 12-hour clock used in the United States. The setting of this category affects the behavior of functions such as <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) and <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3).</p>
<dt><code>LC_ALL</code></p>
<dd>All of the above.</dl>
<p> If the second argument to <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) is an empty string, <i>&quot;&quot;</i>, for the default locale, it is determined using the following steps:</p>
<dl>
<dt>1.</p>
<dd>If there is a non-null environment variable <code>LC_ALL</code>, the value of <code>LC_ALL</code> is used.</p>
<dt>2.</p>
<dd>If an environment variable with the same name as one of the categories above exists and is non-null, its value is used for that category.</p>
<dt>3.</p>
<dd>If there is a non-null environment variable <code>LANG</code>, the value of <code>LANG</code> is used.</dl>
<p> Values about local numeric formatting is made available in a <i>struct lconv</i> returned by the <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3) function, which has the following declaration: </p>
<pre><code>struct lconv {
    /* Numeric (nonmonetary) information */
    char *decimal_point; /* Radix character */
    char *thousands_sep; /* Separator for digit groups to left
                            of radix character */
    char *grouping;      /* Each element is the number of digits in
                            a group; elements with higher indices
                            are further left.  An element with value
                            CHAR_MAX means that no further grouping
                            is done.  An element with value 0 means
                            that the previous element is used for
                            all groups further left. */
    /* Remaining fields are for monetary information */
    char *int_curr_symbol;   /* First three chars are a currency
                                    symbol from ISO 4217.  Fourth char
                                    is the separator.  Fifth char
                                    is '
