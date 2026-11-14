---
title: "locale(5)"
name: "locale"
section: "5"
letter: "l"
url: "/docs/linux/man/5-locale/"
description: "locale – describes a locale definition file"
---

<p>locale &#8211; describes a locale definition file</p>
<h2>Description</h2>
<p>The <code>locale</code> definition file contains all the information that the <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1) command needs to convert it into the binary locale database. </p>
<p> The definition files consist of sections which each describe a locale category in detail. See <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7) for additional details for these categories.</p>
<h3>Syntax</h3>
<p>The locale definition file starts with a header that may consist of the following keywords:</p>
<dl>
<dt><i>escape_char</i></p>
<dd>is followed by a character that should be used as the escape-character for the rest of the file to mark characters that should be interpreted in a special way. It defaults to the backslash (\).</p>
<dt><i>comment_char</i></p>
<dd>is followed by a character that will be used as the comment-character for the rest of the file. It defaults to the number sign (#).</dl>
<p> The locale definition has one part for each locale category. Each part can be copied from another existing locale or can be defined from scratch. If the category should be copied, the only valid keyword in the definition is <i>copy</i> followed by the name of the locale in double quotes which should be copied. The exceptions for this rule are <code>LC_COLLATE</code> and <code>LC_CTYPE</code> where a <i>copy</i> statement can be followed by locale-specific rules and selected overrides. </p>
<p> When defining a locale or a category from scratch, an existing system- provided locale definition file should be used as a reference to follow common glibc conventions.</p>
<h3>Locale category sections</h3>
<p>The following category sections are defined by POSIX:</p>
<dl>
<dt>*</p>
<dd><code>LC_CTYPE</code></p>
<dt>*</p>
<dd><code>LC_COLLATE</code></p>
<dt>*</p>
<dd><code>LC_MESSAGES</code></p>
<dt>*</p>
<dd><code>LC_MONETARY</code></p>
<dt>*</p>
<dd><code>LC_NUMERIC</code></p>
<dt>*</p>
<dd><code>LC_TIME</code></dl>
<p> In addition, since version 2.2, the GNU C library supports the following nonstandard categories:</p>
<dl>
<dt>*</p>
<dd><code>LC_ADDRESS</code></p>
<dt>*</p>
<dd><code>LC_IDENTIFICATION</code></p>
<dt>*</p>
<dd><code>LC_MEASUREMENT</code></p>
<dt>*</p>
<dd><code>LC_NAME</code></p>
<dt>*</p>
<dd><code>LC_PAPER</code></p>
<dt>*</p>
<dd><code>LC_TELEPHONE</code></dl>
<p> See <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7) for a more detailed description of each category.</p>
<h3>Lc_Address</h3>
<p>The definition starts with the string <i>LC_ADDRESS</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>postal_fmt</i></p>
<dd>followed by a string containing field descriptors that define the format used for postal addresses in the locale. The following field descriptors are recognized:</p>
<dl>
<dd>
<dl>
<dt>%n</p>
<dd>Person&#8217;s name, possibly constructed with the <code>LC_NAME</code> <i>name_fmt</i> keyword (since glibc 2.24).</p>
<dt>%a</p>
<dd>Care of person, or organization.</p>
<dt>%f</p>
<dd>Firm name.</p>
<dt>%d</p>
<dd>Department name.</p>
<dt>%b</p>
<dd>Building name.</p>
<dt>%s</p>
<dd>Street or block (e.g., Japanese) name.</p>
<dt>%h</p>
<dd>House number or designation.</p>
<dt>%N</p>
<dd>Insert an end-of-line if the previous descriptor&#8217;s value was not an empty string; otherwise ignore.</p>
<dt>%t</p>
<dd>Insert a space if the previous descriptor&#8217;s value was not an empty string; otherwise ignore.</p>
<dt>%r</p>
<dd>Room number, door designation.</p>
<dt>%e</p>
<dd>Floor number.</p>
<dt>%C</p>
<dd>Country designation, from the <i>country_post</i> keyword.</p>
<dt>%l</p>
<dd>Local township within town or city (since glibc 2.24).</p>
<dt>%z</p>
<dd>Zip number, postal code.</p>
<dt>%T</p>
<dd>Town, city.</p>
<dt>%S</p>
<dd>State, province, or prefecture.</p>
<dt>%c</p>
<dd>Country, as taken from data record.</dl>
<p> Each field descriptor may have an &#8216;R&#8217; after the &#8216;%&#8217; to specify that the information is taken from a Romanized version string of the entity.</dl>
<dt><i>country_name</i></p>
<dd>followed by the country name in the language of the current document (e.g., &quot;Deutschland&quot; for the <code>de_DE</code> locale).</p>
<dt><i>country_post</i></p>
<dd>followed by the abbreviation of the country (see CERT_MAILCODES).</p>
<dt><i>country_ab2</i></p>
<dd>followed by the two-letter abbreviation of the country (ISO 3166).</p>
<dt><i>country_ab3</i></p>
<dd>followed by the three-letter abbreviation of the country (ISO 3166).</p>
<dt><i>country_num</i></p>
<dd>followed by the numeric country code (ISO 3166).</p>
<dt><i>country_car</i></p>
<dd>followed by the international license plate country code.</p>
<dt><i>country_isbn</i></p>
<dd>followed by the ISBN code (for books).</p>
<dt><i>lang_name</i></p>
<dd>followed by the language name in the language of the current document.</p>
<dt><i>lang_ab</i></p>
<dd>followed by the two-letter abbreviation of the language (ISO 639).</p>
<dt><i>lang_term</i></p>
<dd>followed by the three-letter abbreviation of the language (ISO 639-2/T).</p>
<dt><i>lang_lib</i></p>
<dd>followed by the three-letter abbreviation of the language for library use (ISO 639-2/B). Applications should in general prefer <i>lang_term</i> over <i>lang_lib</i>.</dl>
<p> The <code>LC_ADDRESS</code> definition ends with the string <i>END LC_ADDRESS</i>.</p>
<h3>Lc_Ctype</h3>
<p>The definition starts with the string <i>LC_CTYPE</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>upper</i></p>
<dd>followed by a list of uppercase letters. The letters <code>A</code> through <code>Z</code> are included automatically. Characters also specified as <code>cntrl</code>, <code>digit</code>, <code>punct</code>, or <code>space</code> are not allowed.</p>
<dt><i>lower</i></p>
<dd>followed by a list of lowercase letters. The letters <code>a</code> through <code>z</code> are included automatically. Characters also specified as <code>cntrl</code>, <code>digit</code>, <code>punct</code>, or <code>space</code> are not allowed.</p>
<dt><i>alpha</i></p>
<dd>followed by a list of letters. All character specified as either <code>upper</code> or <code>lower</code> are automatically included. Characters also specified as <code>cntrl</code>, <code>digit</code>, <code>punct</code>, or <code>space</code> are not allowed.</p>
<dt><i>digit</i></p>
<dd>followed by the characters classified as numeric digits. Only the digits <code>0</code> through <code>9</code> are allowed. They are included by default in this class.</p>
<dt><i>space</i></p>
<dd>followed by a list of characters defined as white-space characters. Characters also specified as <code>upper</code>, <code>lower</code>, <code>alpha</code>, <code>digit</code>, <code>graph</code>, or <code>xdigit</code> are not allowed. The characters <code>&lt;space&gt;</code>, <code>&lt;form-feed&gt;</code>, <code>&lt;newline&gt;</code>, <code>&lt;carriage-return&gt;</code>, <code>&lt;tab&gt;</code>, and <code>&lt;vertical-tab&gt;</code> are automatically included.</p>
<dt><i>cntrl</i></p>
<dd>followed by a list of control characters. Characters also specified as <code>upper</code>, <code>lower</code>, <code>alpha</code>, <code>digit</code>, <code>punct</code>, <code>graph</code>, <code>print</code>, or <code>xdigit</code> are not allowed.</p>
<dt><i>punct</i></p>
<dd>followed by a list of punctuation characters. Characters also specified as <code>upper</code>, <code>lower</code>, <code>alpha</code>, <code>digit</code>, <code>cntrl</code>, <code>xdigit</code>, or the <code>&lt;space&gt;</code> character are not allowed.</p>
<dt><i>graph</i></p>
<dd>followed by a list of printable characters, not including the <code>&lt;space&gt;</code> character. The characters defined as <code>upper</code>, <code>lower</code>, <code>alpha</code>, <code>digit</code>, <code>xdigit</code>, and <code>punct</code> are automatically included. Characters also specified as <code>cntrl</code> are not allowed.</p>
<dt><i>print</i></p>
<dd>followed by a list of printable characters, including the <code>&lt;space&gt;</code> character. The characters defined as <code>upper</code>, <code>lower</code>, <code>alpha</code>, <code>digit</code>, <code>xdigit</code>, <code>punct</code>, and the <code>&lt;space&gt;</code> character are automatically included. Characters also specified as <code>cntrl</code> are not allowed.</p>
<dt><i>xdigit</i></p>
<dd>followed by a list of characters classified as hexadecimal digits. The decimal digits must be included followed by one or more set of six characters in ascending order. The following characters are included by default: <code>0</code> through <code>9</code>, <code>a</code> through <code>f</code>, <code>A</code> through <code>F</code>.</p>
<dt><i>blank</i></p>
<dd>followed by a list of characters classified as <code>blank</code>. The characters <code>&lt;space&gt;</code> and <code>&lt;tab&gt;</code> are automatically included.</p>
<dt><i>charclass</i></p>
<dd>followed by a list of locale-specific character class names which are then to be defined in the locale.</p>
<dt><i>toupper</i></p>
<dd>followed by a list of mappings from lowercase to uppercase letters. Each mapping is a pair of a lowercase and an uppercase letter separated with a <code>,</code> and enclosed in parentheses.</p>
<dt><i>tolower</i></p>
<dd>followed by a list of mappings from uppercase to lowercase letters. If the keyword tolower is not present, the reverse of the toupper list is used.</p>
<dt><i>map totitle</i></p>
<dd>followed by a list of mapping pairs of characters and letters to be used in titles (headings).</p>
<dt><i>class</i></p>
<dd>followed by a locale-specific character class definition, starting with the class name followed by the characters belonging to the class.</p>
<dt><i>charconv</i></p>
<dd>followed by a list of locale-specific character mapping names which are then to be defined in the locale.</p>
<dt><i>outdigit</i></p>
<dd>followed by a list of alternate output digits for the locale.</p>
<dt><i>map to_inpunct</i></p>
<dd>followed by a list of mapping pairs of alternate digits and separators for input digits for the locale.</p>
<dt><i>map to_outpunct</i></p>
<dd>followed by a list of mapping pairs of alternate separators for output for the locale.</p>
<dt><i>translit_start</i></p>
<dd>marks the start of the transliteration rules section. The section can contain the <i>include</i> keyword in the beginning followed by locale-specific rules and overrides. Any rule specified in the locale file will override any rule copied or included from other files. In case of duplicate rule definitions in the locale file, only the first rule is used.</p>
<dd>A transliteration rule consist of a character to be transliterated followed by a list of transliteration targets separated by semicolons. The first target which can be presented in the target character set is used, if none of them can be used the <i>default_missing</i> character will be used instead.</p>
<dt><i>include</i></p>
<dd>in the transliteration rules section includes a transliteration rule file (and optionally a repertoire map file).</p>
<dt><i>default_missing</i></p>
<dd>in the transliteration rules section defines the default character to be used for transliteration where none of the targets cannot be presented in the target character set.</p>
<dt><i>translit_end</i></p>
<dd>marks the end of the transliteration rules.</dl>
<p> The <code>LC_CTYPE</code> definition ends with the string <i>END LC_CTYPE</i>.</p>
<h3>Lc_Collate</h3>
<p>Note that glibc does not support all POSIX-defined options, only the options described below are supported (as of glibc 2.23). </p>
<p> The definition starts with the string <i>LC_COLLATE</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>coll_weight_max</i></p>
<dd>followed by the number representing used collation levels. This keyword is recognized but ignored by glibc.</p>
<dt><i>collating-element</i></p>
<dd>followed by the definition of a collating-element symbol representing a multicharacter collating element.</p>
<dt><i>collating-symbol</i></p>
<dd>followed by the definition of a collating symbol that can be used in collation order statements.</p>
<dt><i>define</i></p>
<dd>followed by <code>string</code> to be evaluated in an <i>ifdef</i> <code>string</code> / <i>else</i> / <i>endif</i> construct.</p>
<dt><i>reorder-after</i></p>
<dd>followed by a redefinition of a collation rule.</p>
<dt><i>reorder-end</i></p>
<dd>marks the end of the redefinition of a collation rule.</p>
<dt><i>reorder-sections-after</i></p>
<dd>followed by a script name to reorder listed scripts after.</p>
<dt><i>reorder-sections-end</i></p>
<dd>marks the end of the reordering of sections.</p>
<dt><i>script</i></p>
<dd>followed by a declaration of a script.</p>
<dt><i>symbol-equivalence</i></p>
<dd>followed by a collating-symbol to be equivalent to another defined collating-symbol.</dl>
<p> The collation rule definition starts with a line:</p>
<dl>
<dt><i>order_start</i></p>
<dd>followed by a list of keywords chosen from <code>forward</code>, <code>backward</code>, or <code>position</code>. The order definition consists of lines that describe the collation order and is terminated with the keyword <i>order_end</i>.</dl>
<p> The <code>LC_COLLATE</code> definition ends with the string <i>END LC_COLLATE</i>.</p>
<h3>Lc_Identification</h3>
<p>The definition starts with the string <i>LC_IDENTIFICATION</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>title</i></p>
<dd>followed by the title of the locale document (e.g., &quot;Maori language locale for New Zealand&quot;).</p>
<dt><i>source</i></p>
<dd>followed by the name of the organization that maintains this document.</p>
<dt><i>address</i></p>
<dd>followed by the address of the organization that maintains this document.</p>
<dt><i>contact</i></p>
<dd>followed by the name of the contact person at the organization that maintains this document.</p>
<dt><i>email</i></p>
<dd>followed by the email address of the person or organization that maintains this document.</p>
<dt><i>tel</i></p>
<dd>followed by the telephone number (in international format) of the organization that maintains this document. As of glibc 2.24, this keyword is deprecated in favor of other contact methods.</p>
<dt><i>fax</i></p>
<dd>followed by the fax number (in international format) of the organization that maintains this document. As of glibc 2.24, this keyword is deprecated in favor of other contact methods.</p>
<dt><i>language</i></p>
<dd>followed by the name of the language to which this document applies.</p>
<dt><i>territory</i></p>
<dd>followed by the name of the country/geographic extent to which this document applies.</p>
<dt><i>audience</i></p>
<dd>followed by a description of the audience for which this document is intended.</p>
<dt><i>application</i></p>
<dd>followed by a description of any special application for which this document is intended.</p>
<dt><i>abbreviation</i></p>
<dd>followed by the short name for provider of the source of this document.</p>
<dt><i>revision</i></p>
<dd>followed by the revision number of this document.</p>
<dt><i>date</i></p>
<dd>followed by the revision date of this document.</dl>
<p> In addition, for each of the categories defined by the document, there should be a line starting with the keyword <i>category</i>, followed by:</p>
<dl>
<dt>*</p>
<dd>a string that identifies this locale category definition,</p>
<dt>*</p>
<dd>a semicolon, and</p>
<dt>*</p>
<dd>one of the <code>LC_*</code> identifiers.</dl>
<p> The <code>LC_IDENTIFICATION</code> definition ends with the string <i>END LC_IDENTIFICATION</i>.</p>
<h3>Lc_Messages</h3>
<p>The definition starts with the string <i>LC_MESSAGES</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>yesexpr</i></p>
<dd>followed by a regular expression that describes possible yes-responses.</p>
<dt><i>noexpr</i></p>
<dd>followed by a regular expression that describes possible no-responses.</p>
<dt><i>yesstr</i></p>
<dd>followed by the output string corresponding to &quot;yes&quot;.</p>
<dt><i>nostr</i></p>
<dd>followed by the output string corresponding to &quot;no&quot;.</dl>
<p> The <code>LC_MESSAGES</code> definition ends with the string <i>END LC_MESSAGES</i>.</p>
<h3>Lc_Measurement</h3>
<p>The definition starts with the string <i>LC_MEASUREMENT</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>measurement</i></p>
<dd>followed by number identifying the standard used for measurement. The following values are recognized:</p>
<dl>
<dd>
<dl>
<dt><code>1</code></p>
<dd>Metric.</p>
<dt><code>2</code></p>
<dd>US customary measurements.</dl>
</dl>
</dl>
<p> The <code>LC_MEASUREMENT</code> definition ends with the string <i>END LC_MEASUREMENT</i>.</p>
<h3>Lc_Monetary</h3>
<p>The definition starts with the string <i>LC_MONETARY</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>int_curr_symbol</i></p>
<dd>followed by the international currency symbol. This must be a 4-character string containing the international currency symbol as defined by the ISO 4217 standard (three characters) followed by a separator.</p>
<dt><i>currency_symbol</i></p>
<dd>followed by the local currency symbol.</p>
<dt><i>mon_decimal_point</i></p>
<dd>followed by the single-character string that will be used as the decimal delimiter when formatting monetary quantities.</p>
<dt><i>mon_thousands_sep</i></p>
<dd>followed by the single-character string that will be used as a group separator when formatting monetary quantities.</p>
<dt><i>mon_grouping</i></p>
<dd>followed by a sequence of integers separated by semicolons that describe the formatting of monetary quantities. See <i>grouping</i> below for details.</p>
<dt><i>positive_sign</i></p>
<dd>followed by a string that is used to indicate a positive sign for monetary quantities.</p>
<dt><i>negative_sign</i></p>
<dd>followed by a string that is used to indicate a negative sign for monetary quantities.</p>
<dt><i>int_frac_digits</i></p>
<dd>followed by the number of fractional digits that should be used when formatting with the <i>int_curr_symbol</i>.</p>
<dt><i>frac_digits</i></p>
<dd>followed by the number of fractional digits that should be used when formatting with the <i>currency_symbol</i>.</p>
<dt><i>p_cs_precedes</i></p>
<dd>followed by an integer that indicates the placement of <i>currency_symbol</i> for a nonnegative formatted monetary quantity:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>the symbol succeeds the value.</p>
<dt><code>1</code></p>
<dd>the symbol precedes the value.</dl>
</dl>
<dt><i>p_sep_by_space</i></p>
<dd>followed by an integer that indicates the separation of <i>currency_symbol</i>, the sign string, and the value for a nonnegative formatted monetary quantity. The following values are recognized:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>No space separates the currency symbol and the value.</p>
<dt><code>1</code></p>
<dd>If the currency symbol and the sign string are adjacent, a space separates them from the value; otherwise a space separates the currency symbol and the value.</p>
<dt><code>2</code></p>
<dd>If the currency symbol and the sign string are adjacent, a space separates them from the value; otherwise a space separates the sign string and the value.</dl>
</dl>
<dt><i>n_cs_precedes</i></p>
<dd>followed by an integer that indicates the placement of <i>currency_symbol</i> for a negative formatted monetary quantity. The same values are recognized as for <i>p_cs_precedes</i>.</p>
<dt><i>n_sep_by_space</i></p>
<dd>followed by an integer that indicates the separation of <i>currency_symbol</i>, the sign string, and the value for a negative formatted monetary quantity. The same values are recognized as for <i>p_sep_by_space</i>.</p>
<dt><i>p_sign_posn</i></p>
<dd>followed by an integer that indicates where the <i>positive_sign</i> should be placed for a nonnegative monetary quantity:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>Parentheses enclose the quantity and the <i>currency_symbol</i> or <i>int_curr_symbol</i>.</p>
<dt><code>1</code></p>
<dd>The sign string precedes the quantity and the <i>currency_symbol</i> or the <i>int_curr_symbol</i>.</p>
<dt><code>2</code></p>
<dd>The sign string succeeds the quantity and the <i>currency_symbol</i> or the <i>int_curr_symbol</i>.</p>
<dt><code>3</code></p>
<dd>The sign string precedes the <i>currency_symbol</i> or the <i>int_curr_symbol</i>.</p>
<dt><code>4</code></p>
<dd>The sign string succeeds the <i>currency_symbol</i> or the <i>int_curr_symbol</i>.</dl>
</dl>
<dt><i>n_sign_posn</i></p>
<dd>followed by an integer that indicates where the <i>negative_sign</i> should be placed for a negative monetary quantity. The same values are recognized as for <i>p_sign_posn</i>.</p>
<dt><i>int_p_cs_precedes</i></p>
<dd>followed by an integer that indicates the placement of <i>int_curr_symbol</i> for a nonnegative internationally formatted monetary quantity. The same values are recognized as for <i>p_cs_precedes</i>.</p>
<dt><i>int_n_cs_precedes</i></p>
<dd>followed by an integer that indicates the placement of <i>int_curr_symbol</i> for a negative internationally formatted monetary quantity. The same values are recognized as for <i>p_cs_precedes</i>.</p>
<dt><i>int_p_sep_by_space</i></p>
<dd>followed by an integer that indicates the separation of <i>int_curr_symbol</i>, the sign string, and the value for a nonnegative internationally formatted monetary quantity. The same values are recognized as for <i>p_sep_by_space</i>.</p>
<dt><i>int_n_sep_by_space</i></p>
<dd>followed by an integer that indicates the separation of <i>int_curr_symbol</i>, the sign string, and the value for a negative internationally formatted monetary quantity. The same values are recognized as for <i>p_sep_by_space</i>.</p>
<dt><i>int_p_sign_posn</i></p>
<dd>followed by an integer that indicates where the <i>positive_sign</i> should be placed for a nonnegative internationally formatted monetary quantity. The same values are recognized as for <i>p_sign_posn</i>.</p>
<dt><i>int_n_sign_posn</i></p>
<dd>followed by an integer that indicates where the <i>negative_sign</i> should be placed for a negative internationally formatted monetary quantity. The same values are recognized as for <i>p_sign_posn</i>.</dl>
<p> The <code>LC_MONETARY</code> definition ends with the string <i>END LC_MONETARY</i>.</p>
<h3>Lc_Name</h3>
<p>The definition starts with the string <i>LC_NAME</i> in the first column. </p>
<p> Various keywords are allowed, but only <i>name_fmt</i> is mandatory. Other keywords are needed only if there is common convention to use the corresponding salutation in this locale. The allowed keywords are as follows:</p>
<dl>
<dt><i>name_fmt</i></p>
<dd>followed by a string containing field descriptors that define the format used for names in the locale. The following field descriptors are recognized:</p>
<dl>
<dd>
<dl>
<dt>%f</p>
<dd>Family name(s).</p>
<dt>%F</p>
<dd>Family names in uppercase.</p>
<dt>%g</p>
<dd>First given name.</p>
<dt>%G</p>
<dd>First given initial.</p>
<dt>%l</p>
<dd>First given name with Latin letters.</p>
<dt>%o</p>
<dd>Other shorter name.</p>
<dt>%m</p>
<dd>Additional given name(s).</p>
<dt>%M</p>
<dd>Initials for additional given name(s).</p>
<dt>%p</p>
<dd>Profession.</p>
<dt>%s</p>
<dd>Salutation, such as &quot;Doctor&quot;.</p>
<dt>%S</p>
<dd>Abbreviated salutation, such as &quot;Mr.&quot; or &quot;Dr.&quot;.</p>
<dt>%d</p>
<dd>Salutation, using the FDCC-sets conventions.</p>
<dt>%t</p>
<dd>If the preceding field descriptor resulted in an empty string, then the empty string, otherwise a space character.</dl>
</dl>
<dt><i>name_gen</i></p>
<dd>followed by the general salutation for any gender.</p>
<dt><i>name_mr</i></p>
<dd>followed by the salutation for men.</p>
<dt><i>name_mrs</i></p>
<dd>followed by the salutation for married women.</p>
<dt><i>name_miss</i></p>
<dd>followed by the salutation for unmarried women.</p>
<dt><i>name_ms</i></p>
<dd>followed by the salutation valid for all women.</dl>
<p> The <code>LC_NAME</code> definition ends with the string <i>END LC_NAME</i>.</p>
<h3>Lc_Numeric</h3>
<p>The definition starts with the string <i>LC_NUMERIC</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>decimal_point</i></p>
<dd>followed by the single-character string that will be used as the decimal delimiter when formatting numeric quantities.</p>
<dt><i>thousands_sep</i></p>
<dd>followed by the single-character string that will be used as a group separator when formatting numeric quantities.</p>
<dt><i>grouping</i></p>
<dd>followed by a sequence of integers separated by semicolons that describe the formatting of numeric quantities.</p>
<dd>Each integer specifies the number of digits in a group. The first integer defines the size of the group immediately to the left of the decimal delimiter. Subsequent integers define succeeding groups to the left of the previous group. If the last integer is not -1, then the size of the previous group (if any) is repeatedly used for the remainder of the digits. If the last integer is -1, then no further grouping is performed.</dl>
<p> The <code>LC_NUMERIC</code> definition ends with the string <i>END LC_NUMERIC</i>.</p>
<h3>Lc_Paper</h3>
<p>The definition starts with the string <i>LC_PAPER</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>height</i></p>
<dd>followed by the height, in millimeters, of the standard paper format.</p>
<dt><i>width</i></p>
<dd>followed by the width, in millimeters, of the standard paper format.</dl>
<p> The <code>LC_PAPER</code> definition ends with the string <i>END LC_PAPER</i>.</p>
<h3>Lc_Telephone</h3>
<p>The definition starts with the string <i>LC_TELEPHONE</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>tel_int_fmt</i></p>
<dd>followed by a string that contains field descriptors that identify the format used to dial international numbers. The following field descriptors are recognized:</p>
<dl>
<dd>
<dl>
<dt>%a</p>
<dd>Area code without nationwide prefix (the prefix is often &quot;00&quot;).</p>
<dt>%A</p>
<dd>Area code including nationwide prefix.</p>
<dt>%l</p>
<dd>Local number (within area code).</p>
<dt>%e</p>
<dd>Extension (to local number).</p>
<dt>%c</p>
<dd>Country code.</p>
<dt>%C</p>
<dd>Alternate carrier service code used for dialing abroad.</p>
<dt>%t</p>
<dd>If the preceding field descriptor resulted in an empty string, then the empty string, otherwise a space character.</dl>
</dl>
<dt><i>tel_dom_fmt</i></p>
<dd>followed by a string that contains field descriptors that identify the format used to dial domestic numbers. The recognized field descriptors are the same as for <i>tel_int_fmt</i>.</p>
<dt><i>int_select</i></p>
<dd>followed by the prefix used to call international phone numbers.</p>
<dt><i>int_prefix</i></p>
<dd>followed by the prefix used from other countries to dial this country.</dl>
<p> The <code>LC_TELEPHONE</code> definition ends with the string <i>END LC_TELEPHONE</i>.</p>
<h3>Lc_Time</h3>
<p>The definition starts with the string <i>LC_TIME</i> in the first column. </p>
<p> The following keywords are allowed:</p>
<dl>
<dt><i>abday</i></p>
<dd>followed by a list of abbreviated names of the days of the week. The list starts with the first day of the week as specified by <i>week</i> (Sunday by default). See NOTES.</p>
<dt><i>day</i></p>
<dd>followed by a list of names of the days of the week. The list starts with the first day of the week as specified by <i>week</i> (Sunday by default). See NOTES.</p>
<dt><i>abmon</i></p>
<dd>followed by a list of abbreviated month names.</p>
<dt><i>mon</i></p>
<dd>followed by a list of month names.</p>
<dt><i>d_t_fmt</i></p>
<dd>followed by the appropriate date and time format (for syntax, see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3)).</p>
<dt><i>d_fmt</i></p>
<dd>followed by the appropriate date format (for syntax, see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3)).</p>
<dt><i>t_fmt</i></p>
<dd>followed by the appropriate time format (for syntax, see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3)).</p>
<dt><i>am_pm</i></p>
<dd>followed by the appropriate representation of the <code>am</code> and <code>pm</code> strings. This should be left empty for locales not using AM/PM convention.</p>
<dt><i>t_fmt_ampm</i></p>
<dd>followed by the appropriate time format (for syntax, see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3)) when using 12h clock format. This should be left empty for locales not using AM/PM convention.</p>
<dt><i>era</i></p>
<dd>followed by semicolon-separated strings that define how years are counted and displayed for each era in the locale. Each string has the following format:</p>
<dl>
<dd><i>direction</i>:<i>offset</i>:<i>start_date</i>:<i>end_date</i>:<i>era_name</i>:<i>era_format</i> </p>
<p> The fields are to be defined as follows:</p>
<dl>
<dt><i>direction</i></p>
<dd>Either <code>+</code> or <code>&#8211;</code>. <code>+</code> means the years closer to <i>start_date</i> have lower numbers than years closer to <i>end_date</i>. <code>&#8211;</code> means the opposite.</p>
<dt><i>offset</i></p>
<dd>The number of the year closest to <i>start_date</i> in the era, corresponding to the <i>%Ey</i> descriptor (see <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)).</p>
<dt><i>start_date</i></p>
<dd>The start of the era in the form of <i>yyyy/mm/dd</i>. Years prior AD 1 are represented as negative numbers.</p>
<dt><i>end_date</i></p>
<dd>The end of the era in the form of <i>yyyy/mm/dd</i>, or one of the two special values of <code>-*</code> or <code>+*</code>. <code>-*</code> means the ending date is the beginning of time. <code>+*</code> means the ending date is the end of time.</p>
<dt><i>era_name</i></p>
<dd>The name of the era corresponding to the <i>%EC</i> descriptor (see <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)).</p>
<dt><i>era_format</i></p>
<dd>The format of the year in the era corresponding to the <i>%EY</i> descriptor (see <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)).</dl>
</dl>
<dt><i>era_d_fmt</i></p>
<dd>followed by the format of the date in alternative era notation, corresponding to the <i>%Ex</i> descriptor (see <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)).</p>
<dt><i>era_t_fmt</i></p>
<dd>followed by the format of the time in alternative era notation, corresponding to the <i>%EX</i> descriptor (see <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)).</p>
<dt><i>era_d_t_fmt</i></p>
<dd>followed by the format of the date and time in alternative era notation, corresponding to the <i>%Ec</i> descriptor (see <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)).</p>
<dt><i>alt_digits</i></p>
<dd>followed by the alternative digits used for date and time in the locale.</p>
<dt><i>week</i></p>
<dd>followed by a list of three values separated by semicolons: The number of days in a week (by default 7), a date of beginning of the week (by default corresponds to Sunday), and the minimal length of the first week in year (by default 4). Regarding the start of the week, <code>19971130</code> shall be used for Sunday and <code>19971201</code> shall be used for Monday. See NOTES.</p>
<dt><i>first_weekday</i> (since glibc 2.2)</p>
<dd>followed by the number of the day from the <i>day</i> list to be shown as the first day of the week in calendar applications. The default value of <code>1</code> corresponds to either Sunday or Monday depending on the value of the second <i>week</i> list item. See NOTES.</p>
<dt><i>first_workday</i> (since glibc 2.2)</p>
<dd>followed by the number of the first working day from the <i>day</i> list. The default value is <code>2</code>. See NOTES.</p>
<dt><i>cal_direction</i></p>
<dd>followed by a number value that indicates the direction for the display of calendar dates, as follows:</p>
<dl>
<dd>
<dl>
<dt><code>1</code></p>
<dd>Left-right from top.</p>
<dt><code>2</code></p>
<dd>Top-down from left.</p>
<dt><code>3</code></p>
<dd>Right-left from top.</dl>
</dl>
<dt><i>date_fmt</i></p>
<dd>followed by the appropriate date representation for <code><a href="/docs/linux/man/1-date/">date</a></code>(1) (for syntax, see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3)).</dl>
<p> The <code>LC_TIME</code> definition ends with the string <i>END LC_TIME</i>.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/locale/locale-archive</i></p>
<dd>Usual default locale archive location.</p>
<dt><i>/usr/share/i18n/locales</i></p>
<dd>Usual default path for locale definition files.</dl>
<h2>Conforming To</h2>
<p>POSIX.2.</p>
<h2>Notes</h2>
<p>The collective GNU C library community wisdom regarding <i>abday</i>, <i>day</i>, <i>week</i>, <i>first_weekday</i>, and <i>first_workday</i> states at <a rel="nofollow" href="https://sourceware.org/glibc/wiki/Locales">https://sourceware.org/glibc/wiki/Locales</a> the following:</p>
<dl>
<dt>*</p>
<dd>The value of the second <i>week</i> list item specifies the base of the <i>abday</i> and <i>day</i> lists.</p>
<dt>*</p>
<dd><i>first_weekday</i> specifies the offset of the first day-of-week in the <i>abday</i> and <i>day</i> lists.</p>
<dt>*</p>
<dd>For compatibility reasons, all glibc locales should set the value of the second <i>week</i> list item to <code>19971130</code> (Sunday) and base the <i>abday</i> and <i>day</i> lists appropriately, and set <i>first_weekday</i> and <i>first_workday</i> to <code>1</code> or <code>2</code>, depending on whether the week and work week actually starts on Sunday or Monday for the locale.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1), <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3), <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3), <code><a href="/docs/linux/man/5-charmap/">charmap</a></code>(5), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), <code><a href="/docs/linux/man/7-unicode/">unicode</a></code>(7), <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
