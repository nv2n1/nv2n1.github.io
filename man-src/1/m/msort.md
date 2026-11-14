---
title: "msort(1)"
name: "msort"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msort/"
description: "msort – sort records in complex ways"
---

<h2>NAME</h2>
<p> msort &#8211; sort records in complex ways</p>
<h2>SYNOPSIS</h2>
<p> <code>msort</code> &lt;options&gt; [&lt;input file&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <i>msort</i> is a program for sorting text files in sophisticated ways. It was developed initially for alphabetizing dictionaries of languages in which the ordering may be quite different from English but has many other uses. </p>
<p> <i>msort</i> allows you to sort blocks of text delimited in a number of ways rather than just lines and to specify particular fields of a record as sort keys using either their position, counted from either end, or by matching regular expressions to their tags. </p>
<p> <i>msort </i> is capable of sorting on multiple keys, so that when two records tie on one key, the tie may be broken on another. Any or all keys may be optional. How absent optional keys are ordered with respect to present keys may be set separately for each key. </p>
<p> <i>msort</i> allows you to specify arbitrary sort orders and to define virtually unlimited numbers of multigraphs of effectively unlimited length. The sort order and multigraphs are defined separately for each key. If your system has locale support, you can also use locale collation rules instead of specify your own sort order. </p>
<p> <i>msort</i> provides twelve types of key comparison: lexicographic, numeric, numeric string, hybrid, by string length, by angle, by date, by domain name, by time, by ISO8601 date/time stamp, by month name, and random. </p>
<p> What month names are used is a bit complicated. If the <i>-s</i> flag is used on the same key and its argument is the name of a file, the month names are read from the file, which should be in the same format as a sort order definition file. If the <i>-s</i> flag is used and its argument is a locale name, the month names recognized will be the month names and abbreviations associated with the specified locale. If the <i>-s</i> flag is not used the month names recognized will be the month names and abbreviations associated with the current locale. If your system does not have locale support and you do not use the <i>-s</i> flag to read the month names from a file, the month names recognized will be the English month names and abbreviations. </p>
<p> <i>msort</i> can reverse the characters in a key, allowing it to be used to generate reverse dictionaries. </p>
<p> A choice of sorting algorithms is provided. </p>
<p> <i>msort</i> fully supports Unicode. The text to be sorted, and all specifications, should be in UTF-8 Unicode. (If you have plain ASCII text, this is not a problem as ASCII is a subset of Unicode.) Full Unicode case-folding is available, in Turkic and non-Turkic variants. Unicode normalization is performed before sorting. </p>
<p> For usage information, execute <i>msort</i> with no arguments. </p>
<p> Full information about <code>msort</code> is currently to be found in the reference manual, which is distributed as a PDF (Portable Document Format) file. If a copy is not available locally, you can download it from msort&#8217;s home page:<br />
 <a rel="nofollow" href="http://billposer.org/Software/msort.html">http://billposer.org/Software/msort.html</a> </p>
<h2>OPTIONS</h2>
<h3>Informational options</h3>
<dl>
<dt><code>-h,&#8211;help</code></p>
<dd> Print usage message</p>
<dt><code>-v,&#8211;version</code></p>
<dd> Print version message</p>
<dt><code>-D,&#8211;defaults</code></p>
<dd> List defaults</p>
<dt><code>-F,&#8211;general-options</code></p>
<dd> List general command line options</p>
<dt><code>-G,&#8211;gnu-equivalences</code></p>
<dd> List equivalents for GNU sort command line options.</p>
<dt><code>-H,&#8211;informational-options</code></p>
<dd> List informational command line options</p>
<dt><code>-K,&#8211;key-specific-options</code></p>
<dd> List key-specific command line options</p>
<dt><code>-L,&#8211;limits</code></p>
<dd> List limits</p>
<dt><code>-N,&#8211;number-systems</code></p>
<dd> List the supported number systems.</dl>
<h3>General options</h3>
<dl>
<dt><code>-b,&#8211;block</code></p>
<dd> A record is terminated by two or more newlines</p>
<dt><code>-l,&#8211;line</code></p>
<dd> A record consists of a single line</p>
<dt><code>-r,&#8211;record-separator</code> &lt;separator&gt;</p>
<dd> A record is terminated by separator character</p>
<dt><code>-O,&#8211;fixed-size-record</code> &lt;bytes&gt;</p>
<dd> A record consists of the specified number of bytes.</p>
<dt><code>-d,&#8211;field-separators</code> &lt;character&gt;+</p>
<dd> Fields are delimited by the named character(s)</p>
<dt><code>-w,&#8211;whole</code></p>
<dd> Sort on the entire text of the record</p>
<dt><code>-a,&#8211;algorithm</code> &lt;algorithm&gt;</p>
<dd> Use the specified sort algorithm. The choices are: I(nsertionSort), M(ergeSort), Q(uickSort), and S(hellSort). Note that InsertionSort and MergeSort are stable, while QuickSort and ShellSort are unstable. The default is QuickSort.</p>
<dt><code>-M,-initial-maximum-records</code> &lt;records&gt;</p>
<dd> Set initial maximum number of records</p>
<dt><code>-m,&#8211;line-end-carriage-return</code></p>
<dd> End-of-line in the input data is marked by Carriage Return (0x0D) as on the Macintosh rather than by Line Feed (0x0A) as on Unix systems.</p>
<dt><code>-I,&#8211;invert-globally</code></p>
<dd> Invert sense of comparisons globally</p>
<dt><code>-B,&#8211;BMP</code></p>
<dd> No characters fall outside the Basic Multingual Plane (that is, have values greater than 0xFFFF).</p>
<dt><code>-p,&#8211;reserve-private-use-area</code></p>
<dd> Do not make internal use of the Private Use areas. By default, multigraphs are assigned internally to codepoints in the Supplementary Private Use areas if full Unicode is in use or to codepoints in the Private Use area if input is restricted to the Basic Multilingual Plane by means of the <i>-B</i> option. If your input makes use of the Private Use areas, this option prevents interference with your input. In this case, multigraphs will be assigned to the Low and High Surrogate areas (0xD800-0xDFFF). Note that this limits the number of multigraphs to 2,048.</p>
<dt><code>-Q,&#8211;check-only</code></p>
<dd> Check whether the input is already sorted. Do not generate any output. Exit status is 0 if input is already sorted, non-zero if not sorted.</p>
<dt><code>-1,&#8211;in</code> &lt;input file name&gt;</p>
<dd>
<dt><code>-2,&#8211;out</code> &lt;output file name&gt;</p>
<dd> If the output file is the same as the input file, the input file will be overwritten. The input file will not be overwritten if the run is unsuccessful.</p>
<dt><code>-j,&#8211;suppress-log</code></p>
<dd> Suppress output to the log. If this flag is given before there is any output to the log from a command line flag, nothing will be written to the log and the log file will not be created. If a command line flag generates a log message before this flag is processed, the log file will be created but no log messages will be written to it once this flag is processed. To guarantee that no attempt will be made to open a log file, give this flag first.</p>
<dt><code>-q,&#8211;quiet</code></p>
<dd> Be quiet &#8211; do not chat while working</p>
<dt><code>-u,&#8211;unicode-normalization</code> &lt;mode&gt;</p>
<dd> Select Unicode normalization mode. The choices of mode are: <i>c</i> for normalization form C (NFC), <i>d</i> for normalization form D (NFD), and <i>n</i> for no normalization. The default is NFC.</dl>
<h3>Key specific options</h3>
<dl>
<dt><code>-e,&#8211;character-range</code> &lt;m,n&gt;</p>
<dd> Sort on characters m through n. Positive indices start from one. Negative indices indicate position with respect to the end of the record. For example, the range <i>3,-2</i> consists of the third character through the next-to-last character.</p>
<dt><code>-n,&#8211;position</code> &lt;POS&gt;(,&lt;POS&gt;)</p>
<dd> Sort on the specified POS or contiguous range of POSs, where a POS is of the form &lt;field number&gt;(.&lt;character number&gt;). Both counts begin at one. Field numbers but not character numbers may be negative, in which case they are counted from the right. Thus, 1.2 is the second character of the first field; -2.1 is the first character of the next to last field.</p>
<dt><code>-t,&#8211;tag</code> &lt;tag regexp&gt;</p>
<dd> Sort on the field with the specified tag</p>
<dt><code>-o,&#8211;optional</code> &lt;comparison&gt;</p>
<dd> Optional: compare as (&lt;,=,&gt;) to present key if absent</p>
<dt><code>-C,&#8211;fold-case</code></p>
<dd> Fold case</p>
<dt><code>-z,&#8211;fold-case-turkic</code></p>
<dd> Fold case with additional Turkic conversions.</p>
<dt><code>-c,&#8211;comparison-type</code> &lt;comparison type&gt;</p>
<dd> a(ngle),l(exicographic), i(so8601 date/time), t(ime), D(omain name/email address), d(ate), m(onth name), n(umeric), N(umeric string),s(ize), h(hybrid), r(andom)</p>
<dt><code>-y,&#8211;number-system</code> &lt;number system&gt;</p>
<dd> Specifies the number system expected for this key. This affects only numeric and numeric string keys. There are two special values. If the number system is &quot;all&quot;, records may contain any number system that msort can interpret. Different records may contain different number systems. If the number system is &quot;any&quot;, records may contain any writing system that msort can interpret, but all records must make use of the same number system. <i>msort</i> sets the number system on the basis of the first record.</p>
<dt><code>-f,&#8211;date-format</code> &lt;date format&gt;</p>
<dd> Permutation of ymd with separators, e.g. y-m-d for international date format, m/d/y for American date format, or a permutation of yd with separators, e.g. y-d, for day-of-year dates. All three components may be numbers in any available number system. The month field may also be a month name, determined by the same devices as independent month name fields.</p>
<dt><code>-W,&#8211;sort-order-file-separators</code> &lt;file name&gt;</p>
<dd> Read the list of characters to be treated as separators in the sort order definition file.</p>
<dt><code>-S,&#8211;substitutions</code> &lt;file name&gt;</p>
<dd> Read substitutions from named file</p>
<dt><code>-s,&#8211;sort-order</code> &lt;file name&gt;|&lt;locale name&gt;|&quot;locale&quot;</p>
<dd> If the argument is a file name, it is taken to be a sort order file and the sort order for the key is read from the file. If the argument is a locale name, the collation rules for that locale are used. If the argument is &quot;locale&quot;, the collation rules for the current locale are used.</p>
<dt><code>-T,&#8211;transformations</code> &lt;(d)(e)(s)&gt;</p>
<dd> Apply the specified transformations. <i>d</i> specifies that diacritics are to be stripped. Separately encoded combining diacritics are removed. Characters with diacritics represented by<tt>&nbsp;<wbr>&nbsp;<wbr></tt>single codepoints are<br />
 replaced with the corresponding ASCII character without the diacritics, if there is one. <i>e</i> specifies that enclosed characters, that is, characters within circles or parentheses, are to be replaced with the corresponding plain ASCII character if there is one. <i>s</i> specifies that characters in special styles are to be replaced with the corresponding plain ASCII character if there is one. Stylistic equivalents include: small capitals (e.g. U+1D04), script forms (e.g. U+212C), black letter forms (e.g. U+212D), Arabic presentation forms (e.g. U+FE81), Hebrew presentation forms (e.g. U+FB1D), fullwidth forms (e.g. U+FF01), halfwidth forms (e.g. U+FF7B), and the mathematical alphanumeric symbols (e.g. U+1D400).</p>
<dt><code>-x,&#8211;exclusion-file</code> &lt;file name&gt;</p>
<dd> Read exclusions from named file</p>
<dt><code>-X,&#8211;exclude-characters</code> &lt;exclusions&gt;</p>
<dd> Exclude specified characters</p>
<dt><code>-i,&#8211;invert-locally</code></p>
<dd> Invert sense of comparisons</p>
<dt><code>-R,&#8211;reverse-key</code></p>
<dd> Reverse characters of key</dl>
<p> Note: long options may not be available on your system.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sort/">sort</a>(1), <a href="/docs/linux/man/3-uninum/">uninum</a>(3) </p>
<h2>AUTHOR</h2>
<p> Bill Poser (billposer [at] alum.mit.edu)</p>
<h2>LICENSE</h2>
<p> GNU General Public License (<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>), version 3. </p>
<h2>Index</h2>
