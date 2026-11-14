---
title: "enca(1)"
name: "enca"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enca/"
description: "enca — detect and convert encoding of text files"
---

<h2>NAME</h2>
<p> enca &#8212; detect and convert encoding of text files</p>
<h2>SYNOPSIS</h2>
<p> <code>enca</code> [<code>-L</code> <i>LANGUAGE</i>] [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;<br />
 <code>enconv</code> [<code>-L</code> <i>LANGUAGE</i>] [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>INTRODUCTION AND EXAMPLES</h2>
<p> If you are lucky enough, the only two things you will ever need to know are: command</p>
<dl>
<dt>
<dd>
<p> enca <i>FILE</i></dl>
<p> will tell you which encoding file <i>FILE</i> uses (without changing it), and</p>
<dl>
<dt>
<dd>
<p> enconv <i>FILE</i></dl>
<p> will convert file <i>FILE</i> to your locale native encoding. To convert the file to some other encoding use the <code>-x</code> option (see <code>-x</code> entry in section <code>OPTIONS</code> and sections <code>CONVERSION</code> and <code>ENCODINGS</code> for details). </p>
<p> Both work with multiple files and standard input (output) too. E.g.</p>
<dl>
<dt>
<dd>
<p> enca -x latin2 &lt;sometext | lpr</dl>
<p> assures file `sometext&#8217; is in ISO Latin~2 when it&#8217;s sent to printer. </p>
<p> The main reason why these command will fail and turn your files into garbage is that Enca needs to know their language to detect the encoding. It tries to determine your language and preferred charset from locale settings, which might not be what you want. </p>
<p> You can (or have to) use <code>-L</code> option to tell it the right language. Suppose, you downloaded some Russian HTML file, `file.htm&#8217;, it claims it&#8217;s windows-1251 but it isn&#8217;t. So you run</p>
<dl>
<dt>
<dd>
<p> enca -L ru file.htm</dl>
<p> and find out it&#8217;s KOI8-R (for example). Be warned, currently there are not many supported languages (see section <code>LANGUAGES</code>). </p>
<p> Another warning concerns the fact several Enca&#8217;s features, namely its charset conversion capabilities, strongly depend on what other tools are installed on your system (see section <code>CONVERSION)</code>&#8211;run</p>
<dl>
<dt>
<dd>
<p> enca &#8211;version</dl>
<p> to get list of features (see section <code>FEATURES</code>). Also try</p>
<dl>
<dt>
<dd>
<p> enca &#8211;help</dl>
<p> to get description of all other Enca options (and to find the rest of this manual page redundant).</p>
<h2>DESCRIPTION</h2>
<p> Enca reads given text files, or standard input when none are given, and uses knowledge about their language (must be supported by you) and a mixture of parsing, statistical analysis, guessing and black magic to determine their encodings, which it then prints to standard output (or it confesses it doesn&#8217;t have any idea what the encoding could be). By default, Enca presents results as a multiline human-readable descriptions, several other formats are available&#8211;see Output type selectors below. </p>
<p> Enca can also convert files to some other encoding <i>ENC</i> when you ask for it&#8211;either using a built-in converter, some conversion library, or by calling an external converter. </p>
<p> Enca&#8217;s primary goal is to be usable unattended, as an automatic conversion tool, though it perhaps have not reached this point yet (please see section <code>SECURITY</code>). </p>
<p> Please note except rare cases Enca really has to know the language of input files to give you a reliable answer. On the other hand, it can then cope quite well with files that are not purely textual or even detect charset of text strings inside some binary file; of course, it depends on the character of the non-text component. </p>
<p> Enca doesn&#8217;t care about structure of input files, it views them as a uniform piece of text/data. In case of multipart files (e.g. mailboxes), you have to use some tool knowing the structure to extract the individual parts first. It&#8217;s the cost of ability to detect encodings of any damaged, incomplete or otherwise incorrect files.</p>
<h2>OPTIONS</h2>
<p> There are several categories of options: operation mode options, output type selectors, guessing parameters, conversion parameters, general options and listings. </p>
<p> All long options can be abbreviated as long as they are unambiguous, mandatory parameters of long options are mandatory for short options too. </p>
<h3>Operation modes</h3>
<p> are following:</p>
<dl>
<dt><code>-c</code>, <code>&#8211;auto-convert</code></p>
<dd> Equivalent to calling Enca as <code>enconv</code>. </p>
<p> If no output type selector is specified, detect file encodings, guess your preferred charset from locales, and convert files to it (only available with +target-charset-auto feature).</p>
<dt><code>-g</code>, <code>&#8211;guess</code></p>
<dd> Equivalent to calling Enca as <code>enca</code>. </p>
<p> If no output type selector is specified, detect file encodings and report them.</dl>
<h3>Output type selectors</h3>
<p> select what action Enca will take when it determines the encoding; most of them just choose between different names, formats and conventions how encodings can be printed, but one of them (<code>-x</code>) is special: it tells Enca to recode files to some other encoding <i>ENC</i>. These options are mutually exclusive; if you specify more than one output type selector the last one takes precedence. </p>
<p> Several output types represent charset name used by some other program, but not all these programs know all the charsets which Enca recognises. Be warned, Enca makes no difference between unrecognised charset and charset having no name in given namespace in such situations.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;details</code></p>
<dd> It used to print a few pages of details about the guessing process, but since Enca is just a program linked against Enca library, this is not possible and this option is roughly equivalent to <code>&#8211;human-readable</code>, except it reports failure reason when Enca doesn&#8217;t recognize the encoding.</p>
<dt><code>-e</code>, <code>&#8211;enca-name</code></p>
<dd> Prints Enca&#8217;s nice name of the charset, i.e., perhaps the most generally accepted and more or less human-readable charset identifier, with surfaces appended. </p>
<p> This name is used when calling an external converter, too.</p>
<dt><code>-f</code>, <code>&#8211;human-readable</code></p>
<dd> Prints verbal description of the detected charset and surfaces&#8211;something a human understands best. This is the default behaviour. </p>
<p> The precise format is following: the first line contains charset name alone, and it&#8217;s followed by zero or more indented lines containing names of detected surfaces. This format is not, however, suitable or intended for further machine-processing, and the verbal charset descriptions are like to change in the future.</p>
<dt><code>-i</code>, <code>&#8211;iconv-name</code></p>
<dd> Prints how <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3) (and/or <i><a href="/docs/linux/man/1-iconv/">iconv</a></i>(1)) calls the detected charset. More precisely, it prints one, more or less arbitrarily chosen, alias accepted by iconv. A charset unknown to iconv counts as unknown. </p>
<p> This output type makes sense only when Enca is compiled with iconv support (feature +iconv-interface).</p>
<dt><code>-r</code>, <code>&#8211;rfc1345-name</code></p>
<dd> Prints RFC~1345 charset name. When such a name doesn&#8217;t exist because RFC~1345 doesn&#8217;t define a given encoding, some other name defined in some other RFC or just the name which author considers `the most canonical&#8217;, is printed. </p>
<p> Since RFC~1345 doesn&#8217;t define surfaces, no surface info is appended.</p>
<dt><code>-m</code>, <code>&#8211;mime-name</code></p>
<dd> Prints preferred MIME name of detected charset. This is the name you should normally use when fixing e-mails or web pages. </p>
<p> A charset not present in <a rel="nofollow" href="http://www.iana.org/assignments/character-sets">http://www.iana.org/assignments/character-sets</a> counts as unknown.</p>
<dt><code>-s</code>, <code>&#8211;cstocs-name</code></p>
<dd> Prints how <i><a href="/docs/linux/man/1-cstocs/">cstocs</a></i>(1) calls the detected charset. A charset unknown to cstocs counts as unknown.</p>
<dt><code>-n</code>, <code>&#8211;name=</code><i>WORD</i></p>
<dd> Prints charset (encoding) name selected by <i>WORD</i> (can be abbreviated as long as is unambiguous). For names listed above, <code>&#8211;name=</code><i>WORD</i> is equivalent to <code>&#8212;</code><i>WORD</i>. </p>
<p> Using <code>aliases</code> as the output type causes Enca to print list of all accepted aliases of detected charset.</p>
<dt><code>-x</code>, <code>&#8211;convert-to=</code>[<code>..</code>]<i>ENC</i></p>
<dd> Converts file to encoding <i>ENC</i>. </p>
<p> The optional `..&#8217; before encoding name has no special meaning, except you can use it to remind yourself that, unlike in <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1), you should specify <i>desired</i> encoding, instead of current. </p>
<p> You can use <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1) recoding chains or any other kind of braindead recoding specification for <i>ENC</i>, provided that you tell Enca to use some tool understanding it for conversion (see section <code>CONVERSION</code>). </p>
<p> When Enca fails to determine the encoding, it prints a warning and leaves the the file as is; when it is run as a filter it tries to do its best to copy standard input to standard output unchanged. Nevertheless, you should not rely on it and do backup.</dl>
<h3>Guessing parameters</h3>
<p> There&#8217;s only one: <code>-L</code> setting language of input files. This option is mandatory (but see below).</p>
<dl>
<dt><code>-L</code>, <code>&#8211;language=</code><i>LANG</i></p>
<dd> Sets language of input files to <i>LANG</i>. </p>
<p> More precisely, <i>LANG</i> can be any valid locale name (or alias with +locale-alias feature) of some supported language. You can also specify `none&#8217; as language name, only multibyte encodings are recognised then. Run </p>
<p> enca &#8211;list languages </p>
<p> to get list of supported languages. When you don&#8217;t specify any language Enca tries to guess your language from locale settings and assumes input files use this language. See section <code>LANGUAGES</code> for details.</dl>
<h3>Conversion parameters</h3>
<p> give you finer control of how charset conversion will be performed. They don&#8217;t affect anything when <code>-x</code> is not specified as output type. Please see section <code>CONVERSION</code> for the gory conversion details.</p>
<dl>
<dt><code>-C</code>, <code>&#8211;try-converters=</code><i>LIST</i></p>
<dd> Appends comma separated <i>LIST</i> to the list of converters that will be tried when you ask for conversion. Their names can be abbreviated as long as they are unambiguous. Run </p>
<p> enca &#8211;list converters </p>
<p> to get list of all valid converter names (and see section <code>CONVERSION</code> for their description). </p>
<p> The default list depends on how Enca has been compiled, run </p>
<p> enca &#8211;help </p>
<p> to find out default converter list. </p>
<p> Note the default list is used only when you don&#8217;t specify <code>-C</code> at all. Otherwise, the list is built as if it were initially empty and every <code>-C</code> adds new converter(s) to it. Moreover, specifying <code>none</code> as converter name causes clearing the converter list.</p>
<dt><code>-E</code>, <code>&#8211;external-converter-program=</code><i>PATH</i></p>
<dd> Sets external converter program name to <i>PATH</i>. Default external converter depends on how enca has been complied, and the possibility to use external converters may not be available at all. Run </p>
<p> enca &#8211;help </p>
<p> to find out default converter program in your enca build.</dl>
<h3>General options</h3>
<p> don&#8217;t fit to other option categories&#8230;</p>
<dl>
<dt><code>-p</code>, <code>&#8211;with-filename</code></p>
<dd> Forces Enca to prefix each result with corresponding file name. By default, Enca prefixes results with filenames when run on multiple files. </p>
<p> Standard input is printed as <code>STDIN</code> and standard output as <code>STDOUT</code> (the latter can be probably seen in error messages only).</p>
<dt><code>-P</code>, <code>&#8211;no-filename</code></p>
<dd> Forces Enca to not prefix results with file names. By default, Enca doesn&#8217;t prefix result with file name when run on a single file (including standard input).</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Increases verbosity level (each use increases it by one). </p>
<p> Currently this option in not very useful because different parts of Enca respond differently to the same verbosity level, mostly not at all.</dl>
<h3>Listings</h3>
<p> are all terminal, i.e. when Enca encounters some of them it prints the required listing and terminates without processing any following options.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Prints brief usage help.</p>
<dt><code>-G</code>, <code>&#8211;license</code></p>
<dd> Prints full Enca license (through a pager, if possible).</p>
<dt><code>-l</code>, <code>&#8211;list=</code><i>WORD</i></p>
<dd> Prints list specified by <i>WORD</i> (can be abbreviated as long as it is unambiguous). Available lists include: </p>
<p> <code>built-in-charsets</code>. All encodings convertible by built-in converter, by group (both input and output encoding must be from this list and belong to the same group for internal conversion). </p>
<p> <code>built-in-encodings</code>. Equivalent to <code>built-in-charsets</code>, but considered obsolete; will be accepted with a warning, for a while. </p>
<p> <code>converters</code>. All valid converter names (to be used with <code>-C</code>). </p>
<p> <code>charsets</code>. All encodings (charsets). You can select what names will be printed with <code>&#8211;name</code> or any name output type selector (of course, only encodings having a name in given namespace will be printed then), the selector must be specified <i>before</i> <code>&#8211;list</code>. </p>
<p> <code>encodings</code>. Equivalent to <code>charsets</code>, but considered obsolete; will be accepted with a warning, for a while. </p>
<p> <code>languages</code>. All supported languages together with charsets belonging to them. Note output type selects language name style, not charset name style here. </p>
<p> <code>names</code>. All possible values of <code>&#8211;name</code> option. </p>
<p> <code>lists</code>. All possible values of this option. (Crazy?) </p>
<p> <code>surfaces</code>. All surfaces Enca recognises.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Prints program version and list of features (see section <code>FEATURES</code>).</dl>
<h2>CONVERSION</h2>
<p> Though Enca has been originally designed as a tool for guessing encoding only, it now features several methods of charset conversion. You can control which of them will be used with <code>-C</code>. </p>
<p> Enca sequentially tries converters from the list specified by <code>-C</code> until it finds some that is able to perform required conversion or until it exhausts the list. You should specify preferred converters first, less preferred later. External converter (<code>extern</code>) should be always specified last, only as last resort, since it&#8217;s usually not possible to recover when it fails. The default list of converters always starts with <code>built-in</code> and then continues with the first one available from: <code>librecode</code>, <code>iconv</code>, nothing. </p>
<p> It should be noted when Enca says it is not able to perform the conversion it only means none of the converters is able to perform it. It can be still possible to perform the required conversion in several steps, using several converters, but to figure out how, human intelligence is probably needed. </p>
<h3>Built-in converter</h3>
<p> is the simplest and far the fastest of all, can perform only a few byte-to-byte conversions and modifies files directly in place (may be considered dangerous, but is pretty efficient). You can get list of all encodings it can convert with</p>
<dl>
<dt>
<dd>
<p> enca &#8211;list built-in</dl>
<p> Beside speed, its main advantage (and also disadvantage) is that it doesn&#8217;t care: it simply converts characters having a representation in target encoding, doesn&#8217;t touch anything else and never prints any error message. </p>
<p> This converter can be specified as <code>built-in</code> with <code>-C</code>. </p>
<h3>Librecode converter</h3>
<p> is an interface to GNU recode library, that does the actual recoding job. It may or may not be compiled in; run</p>
<dl>
<dt>
<dd>
<p> enca &#8211;version</dl>
<p> to find out its availability in your enca build (feature +librecode-interface). </p>
<p> You should be familiar with <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1) before using it, since recode is a quite sophisticated and powerful charset conversion tool. You may run into problems using it together with Enca particularly because Enca&#8217;s support for surfaces not 100% compatible, because recode tries too hard to make the transformation reversible, because it sometimes silently ignores I/O errors, and because it&#8217;s incredibly buggy. Please see GNU recode info pages for details about recode library. </p>
<p> This converter can be specified as <code>librecode</code> with <code>-C</code>. </p>
<h3>Iconv converter</h3>
<p> is an interface to the UNIX98 <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3) conversion functions, that do the actual recoding job. It may or may not be compiled in; run</p>
<dl>
<dt>
<dd>
<p> enca &#8211;version</dl>
<p> to find out its availability in your enca build (feature +iconv-interface). </p>
<p> While iconv is present on most today systems it only rarely offer some useful set of available conversions, the only notable exception being iconv from GNU libc. It is usually quite picky about surfaces, too (while, at the same time, not implementing surface conversion). It however probably represents the only standard(ized) tool able to perform conversion from/to Unicode. Please see iconv documentation about for details about its capabilities on your particular system. </p>
<p> This converter can be specified as <code>iconv</code> with <code>-C</code>. </p>
<h3>External converter</h3>
<p> is an arbitrary external conversion tool that can be specified with <code>-E</code> option (at most one can be defined simultaneously). There are some standard, provided together with enca: <code>cstocs</code>, <code>recode</code>, <code>map</code>, <code>umap</code>, and <code>piconv</code>. All are wrapper scripts: for <i><a href="/docs/linux/man/1-cstocs/">cstocs</a></i>(1), <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1), <i><a href="/docs/linux/man/1-map/">map</a></i>(1), <i><a href="/docs/linux/man/1-umap/">umap</a></i>(1), and <i><a href="/docs/linux/man/1-piconv/">piconv</a></i>(1). </p>
<p> Please note enca has little control what the external converter really does. If you set it to <code>/bin/rm</code> you are fully responsible for the consequences. </p>
<p> If you want to make your own converter to use with enca, you should know it is always called</p>
<dl>
<dt>
<dd>
<p> <i>CONVERTER</i> <i>ENC_CURRENT</i> <i>ENC</i> <i>FILE</i> [<code>&#8211;</code>]</dl>
<p> where <i>CONVERTER</i> is what has been set by <code>-E</code>, <i>ENC_CURRENT</i> is detected encoding, <i>ENC</i> is what has been specified with <code>-x</code>, and <i>FILE</i> is the file to convert, i.e. it is called for each file separately. The optional fourth parameter, <code>&#8211;</code>, should cause (when present) sending result of conversion to standard output instead of overwriting the file <i>FILE</i>. The converter should also take care of not changing file permissions, returning error code~1 when it fails and cleaning its temporary files. Please see the standard external converters for examples. </p>
<p> This converter can be specified as <code>extern</code> with <i>-C</i>. </p>
<h3>Default target charset</h3>
<p> The straightforward way of specifying target charset is the <code>-x</code> option, which overrides any defaults. When Enca is called as <code>enconv</code>, default target charset is selected exactly the same way as <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1) does it. </p>
<p> If the <code>DEFAULT_CHARSET</code> environment variable is set, it&#8217;s used as the target charset. </p>
<p> Otherwise, if you system provides the <i><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></i>(3) function, current locale&#8217;s native charset is used as the target charset. </p>
<p> When both methods fail, Enca complains and terminates. </p>
<h3>Reversibility notes</h3>
<p> If reversibility is crucial for you, you shouldn&#8217;t use enca as converter at all (or maybe you can, with very specifically designed <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1) wrapper). Otherwise you should at least know that there four basic means of handling inconvertible character entities: </p>
<p> fail&#8211;this is a possibility, too, and incidentally it&#8217;s exactly what current GNU libc iconv implementation does (recode can be also told to do it) </p>
<p> don&#8217;t touch them&#8211;this is what enca internal converter always does and recode can do; though it is not reversible, a human being is usually able to reconstruct the original (at least in principle) </p>
<p> approximate them&#8211;this is what cstocs can do, and recode too, though differently; and the best choice if you just want to make the accursed text readable </p>
<p> drop them out&#8211;this is what both recode and cstocs can do (cstocs can also replace these characters by some fixed character instead of mere ignoring); useful when the to-be-omitted characters contain only noise. </p>
<p> Please consult your favourite converter manual for details of this issue. Generally, if you are not lucky enough to have all convertible characters in you file, manual intervention is needed anyway. </p>
<h3>Performance notes</h3>
<p> Poor performance of available converters has been one of main reasons for including built-in converter in enca. Try to use it whenever possible, i.e. when files in consideration are charset-clean enough or charset-messy enough so that its zero built-in intelligence doesn&#8217;t matter. It requires no extra disk space nor extra memory and can outperform <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1) more than 10 times on large files and Perl version (i.e. the faster one) of <i><a href="/docs/linux/man/1-cstocs/">cstocs</a></i>(1) more than 400 times on small files (in fact it&#8217;s almost as fast as mere <i><a href="/docs/linux/man/1-cp/">cp</a></i>(1)). </p>
<p> Try to avoid external converters when it&#8217;s not absolutely necessary since all the forking and moving stuff around is incredibly slow.</p>
<h2>ENCODINGS</h2>
<p> You can get list of recognised character sets with</p>
<dl>
<dt>
<dd>
<p> enca &#8211;list charsets</dl>
<p> and using <code>&#8211;name</code> parameter you can select any name you want to be used in the listing. You can also list all surfaces with</p>
<dl>
<dt>
<dd>
<p> enca &#8211;list surfaces</dl>
<p> Encoding and surface names are case insensitive and non-alphanumeric characters are not taken into account. However, non-alphanumeric characters are mostly not allowed at all. The only allowed are: `-&#8216;, `_&#8217;, `.&#8217;, `:&#8217;, and~`/&#8217; (as charset/surface separator). So `ibm852&#8242; and `IBM-852&#8242; are the same, while `IBM 852&#8242; is not accepted. </p>
<h3>Charsets</h3>
<p> Following list of recognised charsets uses Enca&#8217;s names (<code>-e</code>) and verbal descriptions as reported by Enca (<code>-f</code>): </p>
<table>
<tr VALIGN=top>
<td>ASCII</td>
<td>7bit ASCII characters
</td>
</tr>
<tr VALIGN=top>
<td>ISO-8859-2</td>
<td>ISO 8859-2 standard; ISO Latin 2
</td>
</tr>
<tr VALIGN=top>
<td>ISO-8859-4</td>
<td>ISO 8859-4 standard; Latin 4
</td>
</tr>
<tr VALIGN=top>
<td>ISO-8859-5</td>
<td>ISO 8859-5 standard; ISO Cyrillic
</td>
</tr>
<tr VALIGN=top>
<td>ISO-8859-13</td>
<td>ISO 8859-13 standard; ISO Baltic; Latin 7
</td>
</tr>
<tr VALIGN=top>
<td>ISO-8859-16</td>
<td>ISO 8859-16 standard
</td>
</tr>
<tr VALIGN=top>
<td>CP1125</td>
<td>MS-Windows code page 1125
</td>
</tr>
<tr VALIGN=top>
<td>CP1250</td>
<td>MS-Windows code page 1250
</td>
</tr>
<tr VALIGN=top>
<td>CP1251</td>
<td>MS-Windows code page 1251
</td>
</tr>
<tr VALIGN=top>
<td>CP1257</td>
<td>MS-Windows code page 1257; WinBaltRim
</td>
</tr>
<tr VALIGN=top>
<td>IBM852</td>
<td>IBM/MS code page 852; PC (DOS) Latin 2
</td>
</tr>
<tr VALIGN=top>
<td>IBM855</td>
<td>IBM/MS code page 855
</td>
</tr>
<tr VALIGN=top>
<td>IBM775</td>
<td>IBM/MS code page 775
</td>
</tr>
<tr VALIGN=top>
<td>IBM866</td>
<td>IBM/MS code page 866
</td>
</tr>
<tr VALIGN=top>
<td>baltic</td>
<td>ISO-IR-179; Baltic
</td>
</tr>
<tr VALIGN=top>
<td>KEYBCS2</td>
<td>Kamenicky encoding; KEYBCS2
</td>
</tr>
<tr VALIGN=top>
<td>macce</td>
<td>Macintosh Central European
</td>
</tr>
<tr VALIGN=top>
<td>maccyr</td>
<td>Macintosh Cyrillic
</td>
</tr>
<tr VALIGN=top>
<td>ECMA-113</td>
<td>Ecma Cyrillic; ECMA-113
</td>
</tr>
<tr VALIGN=top>
<td>KOI-8_CS_2</td>
<td>KOI8-CS2 code (`T602&#8242;)
</td>
</tr>
<tr VALIGN=top>
<td>KOI8-R</td>
<td>KOI8-R Cyrillic
</td>
</tr>
<tr VALIGN=top>
<td>KOI8-U</td>
<td>KOI8-U Cyrillic
</td>
</tr>
<tr VALIGN=top>
<td>KOI8-UNI</td>
<td>KOI8-Unified Cyrillic
</td>
</tr>
<tr VALIGN=top>
<td>TeX</td>
<td>(La)TeX control sequences
</td>
</tr>
<tr VALIGN=top>
<td>UCS-2</td>
<td>Universal character set 2 bytes; UCS-2; BMP
</td>
</tr>
<tr VALIGN=top>
<td>UCS-4</td>
<td>Universal character set 4 bytes; UCS-4; ISO-10646
</td>
</tr>
<tr VALIGN=top>
<td>UTF-7</td>
<td>Universal transformation format 7 bits; UTF-7
</td>
</tr>
<tr VALIGN=top>
<td>UTF-8</td>
<td>Universal transformation format 8 bits; UTF-8
</td>
</tr>
<tr VALIGN=top>
<td>CORK</td>
<td>Cork encoding; T1
</td>
</tr>
<tr VALIGN=top>
<td>GBK</td>
<td>Simplified Chinese National Standard; GB2312
</td>
</tr>
<tr VALIGN=top>
<td>BIG5</td>
<td>Traditional Chinese Industrial Standard; Big5
</td>
</tr>
<tr VALIGN=top>
<td>HZ</td>
<td>HZ encoded GB2312
</td>
</tr>
<tr VALIGN=top>
<td>unknown</td>
<td>Unrecognized encoding
</td>
</tr>
</table>
<p> where <code>unknown</code> is not any real encoding, it&#8217;s reported when Enca is not able to give a reliable answer. </p>
<h3>Surfaces</h3>
<p> Enca has some experimental support for so-called surfaces (see below). It detects following surfaces (not all can be applied to all charsets): </p>
<table>
<tr VALIGN=top>
<td>/CR</td>
<td>CR line terminators
</td>
</tr>
<tr VALIGN=top>
<td>/LF</td>
<td>LF line terminators
</td>
</tr>
<tr VALIGN=top>
<td>/CRLF</td>
<td>CRLF line terminators
</td>
</tr>
<tr VALIGN=top>
<td>N.A.</td>
<td>Mixed line terminators
</td>
</tr>
<tr VALIGN=top>
<td>N.A.</td>
<td>Surrounded by/intermixed with non-text data
</td>
</tr>
<tr VALIGN=top>
<td>/21</td>
<td>Byte order reversed in pairs (1,2 -&gt; 2,1)
</td>
</tr>
<tr VALIGN=top>
<td>/4321</td>
<td>Byte order reversed in quadruples (1,2,3,4 -&gt; 4,3,2,1)
</td>
</tr>
<tr VALIGN=top>
<td>N.A.</td>
<td>Both little and big endian chunks, concatenated
</td>
</tr>
<tr VALIGN=top>
<td>/qp</td>
<td>Quoted-printable encoded
</td>
</tr>
</table>
<p> Note some surfaces have N.A. in place of identifier&#8211;they cannot be specified on command line, they can only be reported by Enca. This is intentional because they only inform you why the file cannot be considered surface-consistent instead of representing a real surface. </p>
<p> Each charset has its natural surface (called `implied&#8217; in recode) which is not reported, e.g., for IBM 852 charset it&#8217;s `CRLF line terminators&#8217;. For UCS encodings, big endian is considered as natural surface; unusual byte orders are constructed from 21 and 4321 permutations: 2143 is reported simply as 21, while 3412 is reported as combination of 4321 and 21. </p>
<p> Doubly-encoded UTF-8 is neither charset nor surface, it&#8217;s just reported. </p>
<h3>About charsets, encodings and surfaces</h3>
<p> Charset is a set of character entities while encoding is its representation in the terms of bytes and bits. In Enca, the word <i>encoding</i> means the same as `representation of text&#8217;, i.e. the relation between sequence of character entities constituting the text and sequence of bytes (bits) constituting the file. </p>
<p> So, encoding is both character set and so-called surface (line terminators, byte order, combining, Base64 transformation, etc.). Nevertheless, it proves convenient to work with some {charset,surface} pairs as with genuine charsets. So, as in <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1), all UCS- and UTF- encodings of Universal character set are called charsets. Please see recode documentation for more details of this issue. </p>
<p> The only good thing about surfaces is: when you don&#8217;t start playing with them, neither Enca won&#8217;t start and it will try to behave as much as possible as a surface-unaware program, even when talking to recode. </p>
<h2>LANGUAGES</h2>
<p> Enca needs to know the language of input files to work reliably, at least in case of regular 8bit encoding. Multibyte encodings should be recognised for any Latin, Cyrillic or Greek language. </p>
<p> You can (or have to) use <code>-L</code> option to tell Enca the language. Since people most often work with files in the same language for which they have configured locales, Enca tries tries to guess the language by examining value of <code>LC_CTYPE</code> and other locale categories (please see <i><a href="/docs/linux/man/7-locale/">locale</a></i>(7)) and using it for the language when you don&#8217;t specify any. Of course, it may be completely wrong and will give you nonsense answers and damage your files, so please don&#8217;t forget to use the <code>-L</code> option. You can also use <code>ENCAOPT</code> environment variable to set a default language (see section <code>ENVIRONMENT</code>). </p>
<p> Following languages are supported by Enca (each language is listed together with supported 8bit encodings). </p>
<table>
<tr VALIGN=top>
<td>Belarusian </td>
<td>CP1251 IBM866 ISO-8859-5 KOI8-UNI maccyr IBM855
</td>
</tr>
<tr VALIGN=top>
<td>Bulgarian </td>
<td>CP1251 ISO-8859-5 IBM855 maccyr ECMA-113
</td>
</tr>
<tr VALIGN=top>
<td>Czech </td>
<td>ISO-8859-2 CP1250 IBM852 KEYBCS2 macce KOI-8_CS_2 CORK
</td>
</tr>
<tr VALIGN=top>
<td>Estonian </td>
<td>ISO-8859-4 CP1257 IBM775 ISO-8859-13 macce baltic
</td>
</tr>
<tr VALIGN=top>
<td>Croatian </td>
<td>CP1250 ISO-8859-2 IBM852 macce CORK
</td>
</tr>
<tr VALIGN=top>
<td>Hungarian </td>
<td>ISO-8859-2 CP1250 IBM852 macce CORK
</td>
</tr>
<tr VALIGN=top>
<td>Lithuanian </td>
<td>CP1257 ISO-8859-4 IBM775 ISO-8859-13 macce baltic
</td>
</tr>
<tr VALIGN=top>
<td>Latvian </td>
<td>CP1257 ISO-8859-4 IBM775 ISO-8859-13 macce baltic
</td>
</tr>
<tr VALIGN=top>
<td>Polish </td>
<td>ISO-8859-2 CP1250 IBM852 macce ISO-8859-13 ISO-8859-16 baltic CORK
</td>
</tr>
<tr VALIGN=top>
<td>Russian </td>
<td>KOI8-R CP1251 ISO-8859-5 IBM866 maccyr
</td>
</tr>
<tr VALIGN=top>
<td>Slovak </td>
<td>CP1250 ISO-8859-2 IBM852 KEYBCS2 macce KOI-8_CS_2 CORK
</td>
</tr>
<tr VALIGN=top>
<td>Slovene </td>
<td>ISO-8859-2 CP1250 IBM852 macce CORK
</td>
</tr>
<tr VALIGN=top>
<td>Ukrainian </td>
<td>CP1251 IBM855 ISO-8859-5 CP1125 KOI8-U maccyr
</td>
</tr>
<tr VALIGN=top>
<td>Chinese </td>
<td>GBK BIG5 HZ
</td>
</tr>
<tr VALIGN=top>
<td>none </td>
<td>
</td>
</tr>
</table>
<p> The special language <code>none</code> can be shortened to <code>__</code>, it contains no 8bit encodings, so only multibyte encodings are detected. </p>
<p> You can also use locale names instead of languages: </p>
<table>
<tr VALIGN=top>
<td>Belarusian </td>
<td>be
</td>
</tr>
<tr VALIGN=top>
<td>Bulgarian </td>
<td>bg
</td>
</tr>
<tr VALIGN=top>
<td>Czech </td>
<td>cs
</td>
</tr>
<tr VALIGN=top>
<td>Estonian </td>
<td>et
</td>
</tr>
<tr VALIGN=top>
<td>Croatian </td>
<td>hr
</td>
</tr>
<tr VALIGN=top>
<td>Hungarian </td>
<td>hu
</td>
</tr>
<tr VALIGN=top>
<td>Lithuanian </td>
<td>lt
</td>
</tr>
<tr VALIGN=top>
<td>Latvian </td>
<td>lv
</td>
</tr>
<tr VALIGN=top>
<td>Polish </td>
<td>pl
</td>
</tr>
<tr VALIGN=top>
<td>Russian </td>
<td>ru
</td>
</tr>
<tr VALIGN=top>
<td>Slovak </td>
<td>sk
</td>
</tr>
<tr VALIGN=top>
<td>Slovene </td>
<td>sl
</td>
</tr>
<tr VALIGN=top>
<td>Ukrainian </td>
<td>uk
</td>
</tr>
<tr VALIGN=top>
<td>Chinese </td>
<td>zh
</td>
</tr>
</table>
<h2>FEATURES</h2>
<p> Several Enca&#8217;s features depend on what is available on your system and how it was compiled. You can get their list with</p>
<dl>
<dt>
<dd>
<p> enca &#8211;version</dl>
<p> Plus sign before a feature name means it&#8217;s available, minus sign means this build lacks the particular feature. </p>
<p> <code>librecode-interface</code>. Enca has interface to GNU recode library charset conversion functions. </p>
<p> <code>iconv-interface</code>. Enca has interface to UNIX98 iconv charset conversion functions. </p>
<p> <code>external-converter</code>. Enca can use external conversion programs (if you have some suitable installed). </p>
<p> <code>language-detection</code>. Enca tries to guess language (<code>-L</code>) from locales. You don&#8217;t need the <code>&#8211;language</code> option, at least in principle. </p>
<p> <code>locale-alias</code>. Enca is able to decrypt locale aliases used for language names. </p>
<p> <code>target-charset-auto</code>. Enca tries to detect your preferred charset from locales. Option <code>&#8211;auto-convert</code> and calling Enca as <code>enconv</code> works, at least in principle. </p>
<p> <code>ENCAOPT</code>. Enca is able to correctly parse this environment variable before command line parameters. Simple stuff like <code>ENCAOPT=&quot;-L uk&quot;</code> will work even without this feature. </p>
<h2>ENVIRONMENT</h2>
<p> The variable <code>ENCAOPT</code> can hold set of default Enca options. Its content is interpreted before command line arguments. Unfortunately, this doesn&#8217;t work everywhere (must have +ENCAOPT feature). </p>
<p> <code>LC_CTYPE</code>, <code>LC_COLLATE</code>, <code>LC_MESSAGES</code> (possibly inherited from <code>LC_ALL</code> or <code>LANG</code>) is used for guessing your language (must have +language-detection feature). </p>
<p> The variable <code>DEFAULT_CHARSET</code> can be used by <code>enconv</code> as the default target charset. </p>
<h2>DIAGNOSTICS</h2>
<p> Enca returns exit code~0 when all input files were successfully proceeded (i.e. all encodings were detected and all files were converted to required encoding, if conversion was asked for). Exit code~1 is returned when Enca wasn&#8217;t able to either guess encoding or perform conversion on any input file because it&#8217;s not clever enough. Exit code~2 is returned in case of serious (e.g. I/O) troubles. </p>
<h2>SECURITY</h2>
<p> It should be possible to let Enca work unattended, it&#8217;s its goal. However: </p>
<p> There&#8217;s no warranty the detection works 100%. Don&#8217;t bet on it, you can easily lose valuable data. </p>
<p> Don&#8217;t use enca (the program), link to libenca instead if you want anything resembling security. You have to perform the eventual conversion yourself then. </p>
<p> Don&#8217;t use external converters. Ideally, disable them compile-time. </p>
<p> Be aware of <code>ENCAOPT</code> and all the built-in automagic guessing various things from environment, namely locales. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-autoconvert/">autoconvert</a></i>(1), <i><a href="/docs/linux/man/1-cstocs/">cstocs</a></i>(1), <i><a href="/docs/linux/man/1-file/">file</a></i>(1), <i><a href="/docs/linux/man/1-iconv/">iconv</a></i>(1), <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3), <i><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></i>(3), <i><a href="/docs/linux/man/1-map/">map</a></i>(1), <i><a href="/docs/linux/man/1-piconv/">piconv</a></i>(1), <i><a href="/docs/linux/man/1-recode/">recode</a></i>(1), <i><a href="/docs/linux/man/5-locale/">locale</a></i>(5), <i><a href="/docs/linux/man/7-locale/">locale</a></i>(7), <i><a href="/docs/linux/man/1-ltt/">ltt</a></i>(1), <i><a href="/docs/linux/man/1-umap/">umap</a></i>(1), <i><a href="/docs/linux/man/7-unicode/">unicode</a></i>(7), <i><a href="/docs/linux/man/7-utf-8/">utf-8</a></i>(7), <i><a href="/docs/linux/man/1-xcode/">xcode</a></i>(1) </p>
<h2>KNOWN BUGS</h2>
<p> It has too many <i>unknown</i> bugs. </p>
<p> The idea of using <code>LC_*</code> value for language is certainly braindead. However I like it. </p>
<p> It can&#8217;t backup files before mangling them. </p>
<p> In certain situations, it may behave incorrectly on &gt;31bit file systems and/or over NFS (both untested but shouldn&#8217;t cause problems in practice). </p>
<p> Built-in converter does not convert character `ch&#8217; from <i>KOI8-CS2</i>, and possibly some other characters you&#8217;ve probably never heard about anyway. </p>
<p> EOL type recognition works poorly on Quoted-printable encoded files. This should be fixed someday. </p>
<p> There are no command line options to tune libenca parameters. This is intentional (Enca should DWIM) but sometimes this is a nuisance. </p>
<p> The manual page is too long, especially this section. This doesn&#8217;t matter since nobody does read it. </p>
<p> Send bug reports to &lt;<a rel="nofollow" href="https://github.com/nijel/enca/issues">https://github.com/nijel/enca/issues</a>&gt;.</p>
<h2>TRIVIA</h2>
<p> Enca is Extremely Naive Charset Analyser. Nevertheless, the `enc&#8217; originally comes from `encoding&#8217; so the leading~`e&#8217; should be read as in `encoding&#8217; not as in `extreme&#8217;.</p>
<h2>AUTHORS</h2>
<p> David Necas (Yeti) &lt;yeti [at] physics.muni.cz&gt; </p>
<p> Michal Cihar &lt;michal [at] cihar.com&gt; </p>
<p> Unicode data has been generated from various (free) on-line resources or using GNU recode. Statistical data has been generated from various texts on the Net, I hope character counting doesn&#8217;t break anyone&#8217;s copyright.</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Please see the file THANKS in distribution.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2003 David Necas (Yeti). </p>
<p> Copyright (C) 2009 Michal Cihar &lt;michal [at] cihar.com&gt;. </p>
<p> Enca is free software; you can redistribute it and/or modify it under the terms of version 2 of the GNU General Public License as published by the Free Software Foundation. </p>
<p> Enca is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with Enca; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
