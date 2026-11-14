---
title: "localedef(1)"
name: "localedef"
section: "1"
letter: "l"
url: "/docs/linux/man/1-localedef/"
description: "localedef – compile locale definition files"
---

<h2 class="name">NAME</h2>
<p> localedef &#8211; compile locale definition files </p>
<h2>SYNOPSIS</h2>
<p> <code>localedef</code> [<i>options</i>] <i>outputpath</i><br />
 <code>localedef &#8211;add-to-archive</code> [<i>options</i>] <i>compiledpath</i><br />
 <code>localedef &#8211;delete-from-archive</code> [<i>options</i>] <i>localename</i> &#8230;<br />
 <code>localedef &#8211;list-archive</code> [<i>options</i>]<br />
 <code>localedef &#8211;help</code><br />
 <code>localedef &#8211;usage</code><br />
 <code>localedef &#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>localedef</code> program reads the indicated <i>charmap</i> and <i>input</i> files, compiles them to a binary form quickly usable by the locale functions in the C library (<code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), etc.), and places the output in <i>outputpath</i>. </p>
<p> The <i>outputpath</i> argument is interpreted as follows:</p>
<dl>
<dt>*</p>
<dd> If <i>outputpath</i> contains a slash character (&#8216;/&#8217;), it is interpreted as the name of the directory where the output definitions are to be stored. In this case, there is a separate output file for each locale category (<i>LC_TIME</i>, <i>LC_NUMERIC</i>, and so on).</p>
<dt>*</p>
<dd> If the <code>&#8211;no-archive</code> option is used, <i>outputpath</i> is the name of a subdirectory in <i>/usr/lib/locale</i> where per-category compiled files are placed.</p>
<dt>*</p>
<dd> Otherwise, <i>outputpath</i> is the name of a locale and the compiled locale data is added to the archive file <i>/usr/lib/locale/locale-archive</i>. A locale archive is a memory-mapped file which contains all the system-provided locales; it is used by all localized programs when the environment variable <code>LOCPATH</code> is not set.</dl>
<p> In any case, <code>localedef</code> aborts if the directory in which it tries to write locale files has not already been created. </p>
<p> If no <i>charmapfile</i> is given, the value <i>ANSI_X3.4-1968</i> (for ASCII) is used by default. If no <i>inputfile</i> is given, or if it is given as a dash (-), <code>localedef</code> reads from standard input.</p>
<h2>OPTIONS</h2>
<h3>Operation-selection options</h3>
<p> A few options direct <code>localedef</code> to do something other than compile locale definitions. Only one of these options should be used at a time.</p>
<dl>
<dt><code>&#8211;add-to-archive</code></p>
<dd> Add the <i>compiledpath</i> directories to the locale archive file. The directories should have been created by previous runs of <code>localedef</code>, using <code>&#8211;no-archive</code>.</p>
<dt><code>&#8211;delete-from-archive</code></p>
<dd> Delete the named locales from the locale archive file.</p>
<dt><code>&#8211;list-archive</code></p>
<dd> List the locales contained in the locale archive file.</dl>
<h3>Other options</h3>
<p> Some of the following options are sensible only for certain operations; generally, it should be self-evident which ones. Notice that <code>-f</code> and <code>-c</code> are reversed from what you might expect; that is, <code>-f</code> is not the same as <code>&#8211;force</code>.</p>
<dl>
<dt><code>-f</code><i> charmapfile</i>, &#8211;charmap=<i>charmapfile</i></p>
<dd> Specify the file that defines the character set that is used by the input file. If <i>charmapfile</i> contains a slash character (&#8216;/&#8217;), it is interpreted as the name of the character map. Otherwise, the file is sought in the current directory and the default directory for character maps. If the environment variable <code>I18NPATH</code> is set, <i>$I18NPATH/charmaps/</i> and <i>$I18NPATH/</i> are also searched after the current directory. The default directory for character maps is printed by <code>localedef &#8211;help</code>.</p>
<dt><code>-i</code><i> inputfile</i>, &#8211;inputfile=<i>inputfile</i></p>
<dd> Specify the locale definition file to compile. The file is sought in the current directory and the default directory for locale definition files. If the environment variable <code>I18NPATH</code> is set, <i>$I18NPATH/locales/</i> and <i>$I18NPATH</i> are also searched after the current directory. The default directory for locale definition files is printed by <code>localedef &#8211;help</code>.</p>
<dt><code>-u</code><i> repertoirefile</i>, &#8211;repertoire-map=<i>repertoirefile</i></p>
<dd> Read mappings from symbolic names to Unicode code points from <i>repertoirefile</i>. If <i>repertoirefile</i> contains a slash character (&#8216;/&#8217;), it is interpreted as the pathname of the repertoire map. Otherwise, the file is sought in the current directory and the default directory for repertoire maps. If the environment variable <code>I18NPATH</code> is set, <i>$I18NPATH/repertoiremaps/</i> and <i>$I18NPATH</i> are also searched after the current directory. The default directory for repertoire maps is printed by <code>localedef &#8211;help</code>.</p>
<dt><code>-A</code><i> aliasfile</i>, &#8211;alias-file=<i>aliasfile</i></p>
<dd> Use <i>aliasfile</i> to look up aliases for locale names. There is no default aliases file.</p>
<dt><code>-c</code>, <code>&#8211;force</code></p>
<dd> Write the output files even if warnings were generated about the input file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Generate extra warnings about errors that are normally ignored.</p>
<dt><code>&#8211;big-endian</code></p>
<dd> Generate big-endian output.</p>
<dt><code>&#8211;little-endian</code></p>
<dd> Generate little-endian output.</p>
<dt><code>&#8211;no-archive</code></p>
<dd> Do not use the locale archive file, instead create <i>outputpath</i> as a subdirectory in the same directory as the locale archive file, and create separate output files for locale categories in it. This is helpful to prevent system locale archive updates from overwriting custom locales created with <code>localedef</code>.</p>
<dt><code>&#8211;no-hard-links</code></p>
<dd> Do not create hard links between installed locales.</p>
<dt><code>&#8211;no-warnings=</code><i>warnings</i></p>
<dd> Comma-separated list of warnings to disable. Supported warnings are <i>ascii</i> and <i>intcurrsym</i>.</p>
<dt><code>&#8211;posix</code></p>
<dd> Conform strictly to POSIX. Implies <code>&#8211;verbose</code>. This option currently has no other effect. POSIX conformance is assumed if the environment variable <code>POSIXLY_CORRECT</code> is set.</p>
<dt><code>&#8211;prefix=</code><i>pathname</i></p>
<dd> Set the prefix to be prepended to the full archive pathname. By default, the prefix is empty. Setting the prefix to <i>foo</i>, the archive would be placed in <i>foo/usr/lib/locale/locale-archive</i>.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Suppress all notifications and warnings, and report only fatal errors.</p>
<dt><code>&#8211;replace</code></p>
<dd> Replace a locale in the locale archive file. Without this option, if the locale is in the archive file already, an error occurs.</p>
<dt><code>&#8211;warnings=</code><i>warnings</i></p>
<dd> Comma-separated list of warnings to enable. Supported warnings are <i>ascii</i> and <i>intcurrsym</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print a usage summary and exit. Also prints the default paths used by <code>localedef</code>.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage summary and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number, license, and disclaimer of warranty for <code>localedef</code>.</dl>
<h2>EXIT STATUS</h2>
<p> One of the following exit values can be returned by <code>localedef</code>:</p>
<dl>
<dt><code>0</code></p>
<dd> Command completed successfully.</p>
<dt><code>1</code></p>
<dd> Warnings or errors occurred, output files were written.</p>
<dt><code>4</code></p>
<dd> Errors encountered, no output created.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>POSIXLY_CORRECT</code></p>
<dd> The <code>&#8211;posix</code> flag is assumed if this environment variable is set.</p>
<dt><code>I18NPATH</code></p>
<dd> A colon-separated list of search directories for files.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/i18n/charmaps</i></p>
<dd> Usual default character map path.</p>
<dt><i>/usr/share/i18n/locales</i></p>
<dd> Usual default path for locale definition files.</p>
<dt><i>/usr/share/i18n/repertoiremaps</i></p>
<dd> Usual default repertoire map path.</p>
<dt><i>/usr/lib/locale/locale-archive</i></p>
<dd> Usual default locale archive location.</p>
<dt><i>/usr/lib/locale</i></p>
<dd> Usual default path for compiled individual locale data files.</p>
<dt><i>outputpath/LC_ADDRESS</i></p>
<dd> An output file that contains information about formatting of addresses and geography-related items.</p>
<dt><i>outputpath/LC_COLLATE</i></p>
<dd> An output file that contains information about the rules for comparing strings.</p>
<dt><i>outputpath/LC_CTYPE</i></p>
<dd> An output file that contains information about character classes.</p>
<dt><i>outputpath/LC_IDENTIFICATION</i></p>
<dd> An output file that contains metadata about the locale.</p>
<dt><i>outputpath/LC_MEASUREMENT</i></p>
<dd> An output file that contains information about locale measurements (metric versus US customary).</p>
<dt><i>outputpath/LC_MESSAGES/SYS_LC_MESSAGES</i></p>
<dd> An output file that contains information about the language messages should be printed in, and what an affirmative or negative answer looks like.</p>
<dt><i>outputpath/LC_MONETARY</i></p>
<dd> An output file that contains information about formatting of monetary values.</p>
<dt><i>outputpath/LC_NAME</i></p>
<dd> An output file that contains information about salutations for persons.</p>
<dt><i>outputpath/LC_NUMERIC</i></p>
<dd> An output file that contains information about formatting of nonmonetary numeric values.</p>
<dt><i>outputpath/LC_PAPER</i></p>
<dd> An output file that contains information about settings related to standard paper size.</p>
<dt><i>outputpath/LC_TELEPHONE</i></p>
<dd> An output file that contains information about formats to be used with telephone services.</p>
<dt><i>outputpath/LC_TIME</i></p>
<dd> An output file that contains information about formatting of data and time values.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.</p>
<h2>EXAMPLES</h2>
<p> Compile the locale files for Finnish in the UTF-8 character set and add it to the default locale archive with the name <code>fi_FI.UTF-8</code>: </p>
<p> localedef -f UTF-8 -i fi_FI fi_FI.UTF-8 </p>
<p> The next example does the same thing, but generates files into the <i>fi_FI.UTF-8</i> directory which can then be used by programs when the environment variable <code>LOCPATH</code> is set to the current directory (note that the last argument must contain a slash): </p>
<p> localedef -f UTF-8 -i fi_FI ./fi_FI.UTF-8</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/5-charmap/">charmap</a></code>(5), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5), <code><a href="/docs/linux/man/5-repertoiremap/">repertoiremap</a></code>(5), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
