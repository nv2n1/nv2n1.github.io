---
title: "man(1)"
name: "man"
section: "1"
letter: "m"
url: "/docs/linux/man/1-man/"
description: "man – an interface to the system reference manuals"
---

<h2 class="name">NAME</h2>
<p> man &#8211; an interface to the system reference manuals </p>
<h2>SYNOPSIS</h2>
<p> <code>man</code> [<i>man options</i>] [[<i>section</i>] <i>page</i>&nbsp;&#8230;]&nbsp;&#8230;<br />
 <code>man</code> <code>-k</code> [<i>apropos options</i>] <i>regexp</i> &#8230;<br />
 <code>man</code> <code>-K</code> [<i>man options</i>] [<i>section</i>] <i>term</i>&nbsp;&#8230;<br />
 <code>man</code> <code>-f</code> [<i>whatis</i> <i>options</i>] <i>page</i> &#8230;<br />
 <code>man</code> <code>-l</code> [<i>man options</i>] <i>file</i> &#8230;<br />
 <code>man</code> <code>-w</code>|<code>-W</code> [<i>man options</i>] <i>page</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>man</code> is the system&#8217;s manual pager. Each <i>page</i> argument given to <code>man</code> is normally the name of a program, utility or function. The <i>manual page</i> associated with each of these arguments is then found and displayed. A <i>section</i>, if provided, will direct <code>man</code> to look only in that <i>section</i> of the manual. The default action is to search in all of the available <i>sections</i> following a pre-defined order (see <code>DEFAULTS</code>), and to show only the first <i>page</i> found, even if <i>page</i> exists in several <i>sections</i>. </p>
<p> The table below shows the <i>section</i> numbers of the manual followed by the types of pages they contain. </p>
<table>
<tr VALIGN=top>
<td>1</td>
<td> Executable programs or shell commands
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> System calls (functions provided by the kernel)
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td> Library calls (functions within program libraries)
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td> Special files (usually found in <i>/dev/</i>)
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td> File formats and conventions, e.g. <i>/etc/passwd</i>
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td> Games
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td> Miscellaneous (including macro packages and conventions), e.g. <code><a href="/docs/linux/man/7-man/">man</a></code>(7), <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7), <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td> System administration commands (usually only for root)
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td> Kernel routines [Non standard]
</td>
</tr>
</table>
<p> A manual <i>page</i> consists of several sections. </p>
<p> Conventional section names include <code>NAME</code>, <code>SYNOPSIS</code>, <code>CONFIGURATION</code>, <code>DESCRIPTION</code>, <code>OPTIONS</code>, <code>EXIT STATUS</code>, <code>RETURN VALUE</code>, <code>ERRORS</code>, <code>ENVIRONMENT</code>, <code>FILES</code>, <code>VERSIONS</code>, <code>CONFORMING TO</code>, <code>NOTES</code>, <code>BUGS</code>, <code>EXAMPLE</code>, <code>AUTHORS</code>, and <code>SEE ALSO</code>. </p>
<p> The following conventions apply to the <code>SYNOPSIS</code> section and can be used as a guide in other sections. </p>
<table>
<tr VALIGN=top>
<td><code>bold text</code></td>
<td> type exactly as shown.
</td>
</tr>
<tr VALIGN=top>
<td><i>italic text</i></td>
<td> replace with appropriate argument.
</td>
</tr>
<tr VALIGN=top>
<td>[<code>-abc</code>]</td>
<td> any or all arguments within [ ] are optional.
</td>
</tr>
<tr VALIGN=top>
<td><code>-a</code>|<code>-b</code></td>
<td> options delimited by | cannot be used together.
</td>
</tr>
<tr VALIGN=top>
<td><i>argument</i> &#8230;</td>
<td> <i>argument</i> is repeatable.
</td>
</tr>
<tr VALIGN=top>
<td>[<i>expression</i>] &#8230;</td>
<td> entire <i>expression</i>&nbsp;within [ ] is repeatable.
</td>
</tr>
</table>
<p> Exact rendering may vary depending on the output device. For instance, man will usually not be able to render italics when running in a terminal, and will typically use underlined or coloured text instead. </p>
<p> The command or function illustration is a pattern that should match all possible invocations. In some cases it is advisable to illustrate several exclusive invocations as is shown in the <code>SYNOPSIS</code> section of this manual page.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>man</code><i>&nbsp;ls</i></p>
<dd> Display the manual page for the <i>item</i> (program) <i>ls</i>.</p>
<dt><code>man</code> <i>man</i>.<i>7</i></p>
<dd> Display the manual page for macro package <i>man</i> from section <i>7</i>. (This is an alternative spelling of &quot;<code>man</code> <i>7 man</i>&quot;.)</p>
<dt><code>man &#8216;</code><i>man</i>(<i>7</i>)&#8217;</p>
<dd> Display the manual page for macro package <i>man</i> from section <i>7</i>. (This is another alternative spelling of &quot;<code>man</code> <i>7 man</i>&quot;. It may be more convenient when copying and pasting cross-references to manual pages. Note that the parentheses must normally be quoted to protect them from the shell.)</p>
<dt><code>man -a</code><i>&nbsp;intro</i></p>
<dd> Display, in succession, all of the available <i>intro</i> manual pages contained within the manual. It is possible to quit between successive displays or skip any of them.</p>
<dt><code>man -t </code><i>bash </i>|<i> lpr -Pps</p>
<dd> Format the manual page for bash</i> into the default <code>troff</code> or <code>groff</code> format and pipe it to the printer named <i>ps</i>. The default output for <code>groff</code> is usually PostScript. <code>man &#8211;help</code> should advise as to which processor is bound to the <code>-t</code> option.</p>
<dt><code>man -l -T</code><i>dvi ./foo.1x.gz</i><code> &gt; </code><i>./foo.1x.dvi</i></p>
<dd> This command will decompress and format the nroff source manual page <i>./foo.1x.gz</i> into a <code>device independent (dvi)</code> file. The redirection is necessary as the <code>-T</code> flag causes output to be directed to <code>stdout</code> with no pager. The output could be viewed with a program such as <code>xdvi</code> or further processed into PostScript using a program such as <code>dvips</code>.</p>
<dt><code>man -k</code><i>&nbsp;printf</i></p>
<dd> Search the short descriptions and manual page names for the keyword <i>printf</i> as regular expression. Print out any matches. Equivalent to <code>apropos</code><i>&nbsp;printf</i><code>.</code></p>
<dt><code>man -f</code><i>&nbsp;smail</i></p>
<dd> Lookup the manual pages referenced by <i>smail</i> and print out the short descriptions of any found. Equivalent to <code>whatis</code><i>&nbsp;smail</i><code>.</code></dl>
<h2>OVERVIEW</h2>
<p> Many options are available to <code>man</code> in order to give as much flexibility as possible to the user. Changes can be made to the search path, section order, output processor, and other behaviours and operations detailed below. </p>
<p> If set, various environment variables are interrogated to determine the operation of <code>man</code>. It is possible to set the &quot;catch-all&quot; variable $<code>MANOPT</code> to any string in command line format, with the exception that any spaces used as part of an option&#8217;s argument must be escaped (preceded by a backslash). <code>man</code> will parse $<code>MANOPT</code> prior to parsing its own command line. Those options requiring an argument will be overridden by the same options found on the command line. To reset all of the options set in $<code>MANOPT</code>, <code>-D</code> can be specified as the initial command line option. This will allow man to &quot;forget&quot; about the options specified in $<code>MANOPT</code>, although they must still have been valid. </p>
<p> Manual pages are normally stored in <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1) format under a directory such as <i>/usr/share/man</i>. In some installations, there may also be preformatted <i>cat pages</i> to improve performance. See <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5) for details of where these files are stored. </p>
<p> This package supports manual pages in multiple languages, controlled by your <i>locale</i>. If your system did not set this up for you automatically, then you may need to set $<code>LC_MESSAGES</code>, $<code>LANG</code>, or another system-dependent environment variable to indicate your preferred locale, usually specified in the <code>POSIX</code> format: </p>
<p> &lt;<i>language</i>&gt;[<code>_</code>&lt;<i>territory</i>&gt;[<code>.</code>&lt;<i>character-set</i>&gt;[<code>,</code>&lt;<i>version</i>&gt;]]] </p>
<p> If the desired page is available in your <i>locale</i>, it will be displayed in lieu of the standard (usually American English) page. </p>
<p> If you find that the translations supplied with this package are not available in your native language and you would like to supply them, please contact the maintainer who will be coordinating such activity. </p>
<p> Individual manual pages are normally written and maintained by the maintainers of the program, function, or other topic that they document, and are not included with this package. If you find that a manual page is missing or inadequate, please report that to the maintainers of the package in question. </p>
<p> For information regarding other features and extensions available with this manual pager, please read the documents supplied with the package.</p>
<h2>DEFAULTS</h2>
<p> The order of sections to search may be overridden by the environment variable $<code>MANSECT</code> or by the <code>SECTION</code> directive in <i>/etc/manpath.config</i>. By default it is as follows: </p>
<dl>
<dt>
<dd> 1 n l 8 3 0 2 3posix 3pm 3perl 3am 5 4 9 6 7</dl>
<p> The formatted manual page is displayed using a <i>pager</i>. This can be specified in a number of ways, or else will fall back to a default (see option <code>-P</code> for details). </p>
<p> The filters are deciphered by a number of means. Firstly, the command line option <code>-p</code> or the environment variable $<code>MANROFFSEQ</code> is interrogated. If <code>-p</code> was not used and the environment variable was not set, the initial line of the nroff file is parsed for a preprocessor string. To contain a valid preprocessor string, the first line must resemble </p>
<p> <code>&#8216;\</code> &lt;<code>string</code>&gt; </p>
<p> where <code>string</code> can be any combination of letters described by option <code>-p</code> below. </p>
<p> If none of the above methods provide any filter information, a default set is used. </p>
<p> A formatting pipeline is formed from the filters and the primary formatter (<code>nroff</code> or [<code>tg</code>]<code>roff</code> with <code>-t</code>) and executed. Alternatively, if an executable program <i>mandb_nfmt</i> (or <i>mandb_tfmt</i> with <code>-t</code>) exists in the man tree root, it is executed instead. It gets passed the manual source file, the preprocessor string, and optionally the device specified with <code>-T</code> or <code>-E</code> as arguments.</p>
<h2>OPTIONS</h2>
<p> Non-argument options that are duplicated either on the command line, in $<code>MANOPT</code>, or both, are not harmful. For options that require an argument, each duplication will override the previous argument value.</p>
<h3>General options</h3>
<dl>
<dt><code>-C&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;config-file=</code><i>file</i></p>
<dd> Use this user configuration file rather than the default of <i>~/.manpath</i>.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information.</p>
<dt><code>-D</code>, <code>&#8211;default</code></p>
<dd> This option is normally issued as the very first option and resets <code>man&#8217;s</code> behaviour to its default. Its use is to reset those options that may have been set in $<code>MANOPT</code>. Any options that follow <code>-D</code> will have their usual effect.</p>
<dt><code>&#8211;warnings</code>[=<i>warnings/</i>]</p>
<dd> Enable warnings from <i>groff</i>. This may be used to perform sanity checks on the source text of manual pages. <i>warnings</i> is a comma-separated list of warning names; if it is not supplied, the default is &quot;mac&quot;. See the &#8220;Warnings&#8221; node in <code>info groff</code> for a list of available warning names.</dl>
<h3>Main modes of operation</h3>
<dl>
<dt><code>-f</code>, <code>&#8211;whatis</code></p>
<dd> Equivalent to <code>whatis</code>. Display a short description from the manual page, if available. See <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1) for details.</p>
<dt><code>-k</code>, <code>&#8211;apropos</code></p>
<dd> Equivalent to <code>apropos</code>. Search the short manual page descriptions for keywords and display any matches. See <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1) for details.</p>
<dt><code>-K</code>, <code>&#8211;global-apropos</code></p>
<dd> Search for text in all manual pages. This is a brute-force search, and is likely to take some time; if you can, you should specify a section to reduce the number of pages that need to be searched. Search terms may be simple strings (the default), or regular expressions if the <code>&#8211;regex</code> option is used.</p>
<dt>
<dd> Note that this searches the <i>sources</i> of the manual pages, not the rendered text, and so may include false positives due to things like comments in source files. Searching the rendered text would be much slower.</p>
<dt><code>-l</code>, <code>&#8211;local-file</code></p>
<dd> Activate &quot;local&quot; mode. Format and display local manual files instead of searching through the system&#8217;s manual collection. Each manual page argument will be interpreted as an nroff source file in the correct format. No cat file is produced. If &#8216;-&#8216; is listed as one of the arguments, input will be taken from stdin. When this option is not used, and man fails to find the page required, before displaying the error message, it attempts to act as if this option was supplied, using the name as a filename and looking for an exact match.</p>
<dt><code>-w</code>, <code>&#8211;where</code>, <code>&#8211;path</code>, <code>&#8211;location</code></p>
<dd> Don&#8217;t actually display the manual page, but do print the location of the source nroff file that would be formatted. If the <code>-a</code> option is also used, then print the locations of all source files that match the search criteria.</p>
<dt><code>-W</code>, <code>&#8211;where-cat</code>, <code>&#8211;location-cat</code></p>
<dd> Don&#8217;t actually display the manual page, but do print the location of the preformatted cat file that would be displayed. If the <code>-a</code> option is also used, then print the locations of all preformatted cat files that match the search criteria.</p>
<dt>
<dd> If <code>-w</code> and <code>-W</code> are both used, then print both source file and cat file separated by a space. If all of <code>-w</code>, <code>-W</code>, and <code>-a</code> are used, then do this for each possible match.</p>
<dt><code>-c</code>, <code>&#8211;catman</code></p>
<dd> This option is not for general use and should only be used by the <code>catman</code> program.</p>
<dt><code>-R&nbsp;</code><i>encoding</i>,&nbsp;<i></i><code>&#8211;recode</code>=<i>encoding</i></p>
<dd> Instead of formatting the manual page in the usual way, output its source converted to the specified <i>encoding</i>. If you already know the encoding of the source file, you can also use <code><a href="/docs/linux/man/1-manconv/">manconv</a></code>(1) directly. However, this option allows you to convert several manual pages to a single encoding without having to explicitly state the encoding of each, provided that they were already installed in a structure similar to a manual page hierarchy.</p>
<dt>
<dd> Consider using <code><a href="/docs/linux/man/1-man-recode/">man-recode</a></code>(1) instead for converting multiple manual pages, since it has an interface designed for bulk conversion and so can be much faster.</dl>
<h3>Finding manual pages</h3>
<dl>
<dt><code>-L&nbsp;</code><i>locale</i>,&nbsp;<code>&#8211;locale=</code><i>locale</i></p>
<dd> <code>man</code> will normally determine your current locale by a call to the C function <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) which interrogates various environment variables, possibly including $<code>LC_MESSAGES</code> and $<code>LANG</code>. To temporarily override the determined value, use this option to supply a <i>locale</i> string directly to <code>man</code>. Note that it will not take effect until the search for pages actually begins. Output such as the help message will always be displayed in the initially determined locale.</p>
<dt><code>-m</code> <i>system</i>[,&#8230;], <code>&#8211;systems=</code><i>system</i>[,&#8230;]</p>
<dd> If this system has access to other operating systems&#8217; manual pages, they can be accessed using this option. To search for a manual page from NewOS&#8217;s manual page collection, use the option <code>-m</code> <code>NewOS</code>. </p>
<p> The <i>system</i> specified can be a combination of comma delimited operating system names. To include a search of the native operating system&#8217;s manual pages, include the system name <code>man</code> in the argument string. This option will override the $<code>SYSTEM</code> environment variable.</p>
<dt><code>-M&nbsp;</code><i>path</i>,&nbsp;<code>&#8211;manpath=</code><i>path</i></p>
<dd> Specify an alternate manpath to use. By default, <code>man</code> uses <code>manpath</code> derived code to determine the path to search. This option overrides the $<code>MANPATH</code> environment variable and causes option <code>-m</code> to be ignored. </p>
<p> A path specified as a manpath must be the root of a manual page hierarchy structured into sections as described in the man-db manual (under &quot;The manual page system&quot;). To view manual pages outside such hierarchies, see the <code>-l</code> option.</p>
<dt><code>-S</code> <i>list/</i>, <code>-s</code> <i>list/</i>, <code>&#8211;sections=</code><i>list/</i></p>
<dd> The given <i>list</i> is a colon- or comma-separated list of sections, used to determine which manual sections to search and in what order. This option overrides the $<code>MANSECT</code> environment variable. (The <code>-s</code> spelling is for compatibility with System V.)</p>
<dt><code>-e&nbsp;</code><i>sub-extension</i>,&nbsp;<code>&#8211;extension=</code><i>sub-extension</i></p>
<dd> Some systems incorporate large packages of manual pages, such as those that accompany the <code>Tcl</code> package, into the main manual page hierarchy. To get around the problem of having two manual pages with the same name such as <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), the <code>Tcl</code> pages were usually all assigned to section <code>l</code>. As this is unfortunate, it is now possible to put the pages in the correct section, and to assign a specific &quot;extension&quot; to them, in this case, <code>exit</code>(3tcl). Under normal operation, <code>man</code> will display <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) in preference to <code>exit</code>(3tcl). To negotiate this situation and to avoid having to know which section the page you require resides in, it is now possible to give <code>man</code> a <i>sub-extension</i> string indicating which package the page must belong to. Using the above example, supplying the option <code>-e tcl</code> to <code>man</code> will restrict the search to pages having an extension of <code>*tcl</code>.</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> Ignore case when searching for manual pages. This is the default.</p>
<dt><code>-I</code>, <code>&#8211;match-case</code></p>
<dd> Search for manual pages case-sensitively.</p>
<dt><code>&#8211;regex</code></p>
<dd> Show all pages with any part of either their names or their descriptions matching each <i>page</i> argument as a regular expression, as with <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1). Since there is usually no reasonable way to pick a &quot;best&quot; page when searching for a regular expression, this option implies <code>-a</code>.</p>
<dt><code>&#8211;wildcard</code></p>
<dd> Show all pages with any part of either their names or their descriptions matching each <i>page</i> argument using shell-style wildcards, as with <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1) <code>&#8211;wildcard</code>. The <i>page</i> argument must match the entire name or description, or match on word boundaries in the description. Since there is usually no reasonable way to pick a &quot;best&quot; page when searching for a wildcard, this option implies <code>-a</code>.</p>
<dt><code>&#8211;names-only</code></p>
<dd> If the <code>&#8211;regex</code> or <code>&#8211;wildcard</code> option is used, match only page names, not page descriptions, as with <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1). Otherwise, no effect.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> By default, <code>man</code> will exit after displaying the most suitable manual page it finds. Using this option forces <code>man</code> to display all the manual pages with names that match the search criteria.</p>
<dt><code>-u</code>, <code>&#8211;update</code></p>
<dd> This option causes <code>man</code> to update its database caches of installed manual pages. This is only needed in rare situations, and it is normally better to run <code><a href="/docs/linux/man/8-mandb/">mandb</a></code>(8) instead.</p>
<dt><code>&#8211;no-subpages</code></p>
<dd> By default, <code>man</code> will try to interpret pairs of manual page names given on the command line as equivalent to a single manual page name containing a hyphen or an underscore. This supports the common pattern of programs that implement a number of subcommands, allowing them to provide manual pages for each that can be accessed using similar syntax as would be used to invoke the subcommands themselves. For example: </p>
<pre>
  $ man -aw git diff
  /usr/share/man/man1/git-diff.1.gz
</pre>
<p> To disable this behaviour, use the <code>&#8211;no-subpages</code> option. </p>
<pre>
  $ man -aw --no-subpages git diff
  /usr/share/man/man1/git.1.gz
  /usr/share/man/man3/Git.3pm.gz
  /usr/share/man/man1/diff.1.gz
</pre>
</dl>
<h3>Controlling formatted output</h3>
<dl>
<dt><code>-P&nbsp;</code><i>pager</i>,&nbsp;<code>&#8211;pager=</code><i>pager</i></p>
<dd> Specify which output pager to use. By default, <code>man</code> uses <code>pager</code>, falling back to <code>cat</code> if <code>pager</code> is not found or is not executable. This option overrides the $<code>MANPAGER</code> environment variable, which in turn overrides the $<code>PAGER</code> environment variable. It is not used in conjunction with <code>-f</code> or <code>-k</code>. </p>
<p> The value may be a simple command name or a command with arguments, and may use shell quoting (backslashes, single quotes, or double quotes). It may not use pipes to connect multiple commands; if you need that, use a wrapper script, which may take the file to display either as an argument or on standard input.</p>
<dt><code>-r&nbsp;</code><i>prompt</i>,&nbsp;<code>&#8211;prompt=</code><i>prompt</i></p>
<dd> If a recent version of <code>less</code> is used as the pager, <code>man</code> will attempt to set its prompt and some sensible options. The default prompt looks like </p>
<p> <code> Manual page</code><i> name</i><code>(</code><i>sec</i><code>) line</code><i> x</i> </p>
<p> where <i>name</i> denotes the manual page name, <i>sec</i> denotes the section it was found under and <i>x</i> the current line number. This is achieved by using the $<code>LESS</code> environment variable. </p>
<p> Supplying <code>-r</code> with a string will override this default. The string may contain the text <code>$MAN_PN</code> which will be expanded to the name of the current manual page and its section name surrounded by &quot;(&quot; and &quot;)&quot;. The string used to produce the default could be expressed as </p>
<p> <code>\&nbsp;Manual\&nbsp;page\&nbsp;\$MAN_PN\&nbsp;?ltline\&nbsp;%lt?L/%L.:</code><br />
 <code>byte\&nbsp;%bB?s/%s..?\&nbsp;(END):?pB\&nbsp;%pB\%..</code><br />
 <code>(press h for help or q to quit)</code> </p>
<p> It is broken into three lines here for the sake of readability only. For its meaning see the <code><a href="/docs/linux/man/1-less/">less</a></code>(1) manual page. The prompt string is first evaluated by the shell. All double quotes, back-quotes and backslashes in the prompt must be escaped by a preceding backslash. The prompt string may end in an escaped $ which may be followed by further options for less. By default <code>man</code> sets the <code>-ix8</code> options. </p>
<p> The $<code>MANLESS</code> environment variable described below may be used to set a default prompt string if none is supplied on the command line.</p>
<dt><code>-7</code>, <code>&#8211;ascii</code></p>
<dd> When viewing a pure <i><a href="/docs/linux/man/7-ascii/">ascii</a></i>(7) manual page on a 7 bit terminal or terminal emulator, some characters may not display correctly when using the <i><a href="/docs/linux/man/7-latin1/">latin1</a></i>(7) device description with <code>GNU</code> <code>nroff</code>. This option allows pure <i>ascii</i> manual pages to be displayed in <i>ascii</i> with the <i>latin1</i> device. It will not translate any <i>latin1</i> text. The following table shows the translations performed: some parts of it may only be displayed properly when using <code>GNU</code> <code>nroff</code>&#8216;s <i><a href="/docs/linux/man/7-latin1/">latin1</a></i>(7) device. </p>
<table>
<tr VALIGN=top>
<td>Description</td>
<td ALIGN=center>Octal</td>
<td ALIGN=center>latin1</td>
<td ALIGN=center>ascii
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> continuation hyphen </td>
<td ALIGN=center>255</td>
<td ALIGN=center></td>
<td ALIGN=center>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td> bullet (middle dot) </td>
<td ALIGN=center>267</td>
<td ALIGN=center>&bull;</td>
<td ALIGN=center>o
</td>
</tr>
<tr VALIGN=top>
<td> acute accent </td>
<td ALIGN=center>264</td>
<td ALIGN=center>&acute;</td>
<td ALIGN=center>&#8216;
</td>
</tr>
<tr VALIGN=top>
<td> multiplication sign </td>
<td ALIGN=center>327</td>
<td ALIGN=center>&#215;</td>
<td ALIGN=center>x
</td>
</tr>
</table>
<p> If the <i>latin1</i> column displays correctly, your terminal may be set up for <i>latin1</i> characters and this option is not necessary. If the <i>latin1</i> and <i>ascii</i> columns are identical, you are reading this page using this option or <code>man</code> did not format this page using the <i>latin1</i> device description. If the <i>latin1</i> column is missing or corrupt, you may need to view manual pages with this option. </p>
<p> This option is ignored when using options <code>-t</code>, <code>-H</code>, <code>-T</code>, or <code>-Z</code> and may be useless for <code>nroff</code> other than <code>GNU&#8217;s</code>.</p>
<dt><code>-E&nbsp;</code><i>encoding</i>,&nbsp;<i></i><code>&#8211;encoding</code>=<i>encoding</i></p>
<dd> Generate output for a character encoding other than the default. For backward compatibility, <i>encoding</i> may be an <code>nroff</code> device such as <code>ascii</code>, <code>latin1</code>, or <code>utf8</code> as well as a true character encoding such as <code>UTF-8</code>.</p>
<dt><code>&#8211;no-hyphenation</code>, <code>&#8211;nh</code></p>
<dd> Normally, <code>nroff</code> will automatically hyphenate text at line breaks even in words that do not contain hyphens, if it is necessary to do so to lay out words on a line without excessive spacing. This option disables automatic hyphenation, so words will only be hyphenated if they already contain hyphens. </p>
<p> If you are writing a manual page and simply want to prevent <code>nroff</code> from hyphenating a word at an inappropriate point, do not use this option, but consult the <code>nroff</code> documentation instead; for instance, you can put &quot;\%&quot; inside a word to indicate that it may be hyphenated at that point, or put &quot;\%&quot; at the start of a word to prevent it from being hyphenated.</p>
<dt><code>&#8211;no-justification</code>, <code>&#8211;nj</code></p>
<dd> Normally, <code>nroff</code> will automatically justify text to both margins. This option disables full justification, leaving justified only to the left margin, sometimes called &quot;ragged-right&quot; text. </p>
<p> If you are writing a manual page and simply want to prevent <code>nroff</code> from justifying certain paragraphs, do not use this option, but consult the <code>nroff</code> documentation instead; for instance, you can use the &quot;.na&quot;, &quot;.nf&quot;, &quot;.fi&quot;, and &quot;.ad&quot; requests to temporarily disable adjusting and filling.</p>
<dt><code>-p&nbsp;</code><i>string</i>,&nbsp;<code>&#8211;preprocessor=</code><i>string</i></p>
<dd> Specify the sequence of preprocessors to run before <code>nroff</code> or <code>troff</code>/<code>groff</code>. Not all installations will have a full set of preprocessors. Some of the preprocessors and the letters used to designate them are: <code>eqn</code> (<code>e</code>), <code>grap</code> (<code>g</code>), <code>pic</code> (<code>p</code>), <code>tbl</code> (<code>t</code>), <code>vgrind</code> (<code>v</code>), <code>refer</code> (<code>r</code>). This option overrides the $<code>MANROFFSEQ</code> environment variable. <code>zsoelim</code> is always run as the very first preprocessor.</p>
<dt><code>-t</code>, <code>&#8211;troff</code></p>
<dd> Use <i>groff -mandoc</i> to format the manual page to stdout. This option is not required in conjunction with <code>-H</code>, <code>-T</code>, or <code>-Z</code>.</p>
<dt><code>-T</code>[<i>device/</i>], <code>&#8211;troff-device</code>[=<i>device/</i>]</p>
<dd> This option is used to change <code>groff</code> (or possibly <code>troff&#8217;s</code>) output to be suitable for a device other than the default. It implies <code>-t</code>. Examples (provided with Groff-1.17) include <code>dvi</code>, <code>latin1</code>, <code>ps</code>, <code>utf8</code>, <code>X75</code> and <code>X100</code>.</p>
<dt><code>-H</code>[<i>browser/</i>], <code>&#8211;html</code>[=<i>browser/</i>]</p>
<dd> This option will cause <code>groff</code> to produce HTML output, and will display that output in a web browser. The choice of browser is determined by the optional <i>browser</i> argument if one is provided, by the $<code>BROWSER</code> environment variable, or by a compile-time default if that is unset (usually <code>lynx</code>). This option implies <code>-t</code>, and will only work with <code>GNU</code> <code>troff</code>.</p>
<dt><code>-X</code>[<i>dpi/</i>], <code>&#8211;gxditview</code>[=<i>dpi/</i>]</p>
<dd> This option displays the output of <code>groff</code> in a graphical window using the <code>gxditview</code> program. The <i>dpi</i> (dots per inch) may be 75, 75-12, 100, or 100-12, defaulting to 75; the -12 variants use a 12-point base font. This option implies <code>-T</code> with the X75, X75-12, X100, or X100-12 device respectively.</p>
<dt><code>-Z</code>, <code>&#8211;ditroff</code></p>
<dd> <code>groff</code> will run <code>troff</code> and then use an appropriate post-processor to produce output suitable for the chosen device. If <i>groff -mandoc</i> is <code>groff</code>, this option is passed to <code>groff</code> and will suppress the use of a post-processor. It implies <code>-t</code>.</dl>
<h3>Getting help</h3>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Successful program execution.</p>
<dt><code>1</code></p>
<dd> Usage, syntax or configuration file error.</p>
<dt><code>2</code></p>
<dd> Operational error.</p>
<dt><code>3</code></p>
<dd> A child process returned a non-zero exit status.</p>
<dt><code>16</code></p>
<dd> At least one of the pages/files/keywords didn&#8217;t exist or wasn&#8217;t matched.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MANPATH</code></p>
<dd> If $<code>MANPATH</code> is set, its value is used as the path to search for manual pages. </p>
<p> See the <code>SEARCH PATH</code> section of <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5) for the default behaviour and details of how this environment variable is handled.</p>
<dt><code>MANROFFOPT</code></p>
<dd> Every time <code>man</code> invokes the formatter (<code>nroff</code>, <code>troff</code>, or <code>groff</code>), it adds the contents of $<code>MANROFFOPT</code> to the formatter&#8217;s command line.</p>
<dt><code>MANROFFSEQ</code></p>
<dd> If $<code>MANROFFSEQ</code> is set, its value is used to determine the set of preprocessors to pass each manual page through. The default preprocessor list is system dependent.</p>
<dt><code>MANSECT</code></p>
<dd> If $<code>MANSECT</code> is set, its value is a colon-delimited list of sections and it is used to determine which manual sections to search and in what order. The default is &quot;1 n l 8 3 0 2 3posix 3pm 3perl 3am 5 4 9 6 7&quot;, unless overridden by the <code>SECTION</code> directive in <i>/etc/manpath.config</i>.</p>
<dt><code>MANPAGER</code>,<code> PAGER</code></p>
<dd> If $<code>MANPAGER</code> or $<code>PAGER</code> is set ($<code>MANPAGER</code> is used in preference), its value is used as the name of the program used to display the manual page. By default, <code>pager</code> is used, falling back to <code>cat</code> if <code>pager</code> is not found or is not executable. </p>
<p> The value may be a simple command name or a command with arguments, and may use shell quoting (backslashes, single quotes, or double quotes). It may not use pipes to connect multiple commands; if you need that, use a wrapper script, which may take the file to display either as an argument or on standard input.</p>
<dt><code>MANLESS</code></p>
<dd> If $<code>MANLESS</code> is set, its value will be used as the default prompt string for the <code>less</code> pager, as if it had been passed using the <code>-r</code> option (so any occurrences of the text <code>$MAN_PN</code> will be expanded in the same way). For example, if you want to set the prompt string unconditionally to &#8220;my prompt string&#8221;, set $<code>MANLESS</code> to &#8216;<code>-Psmy prompt string</code>&#8216;. Using the <code>-r</code> option overrides this environment variable.</p>
<dt><code>BROWSER</code></p>
<dd> If $<code>BROWSER</code> is set, its value is a colon-delimited list of commands, each of which in turn is used to try to start a web browser for <code>man</code> <code>&#8211;html</code>. In each command, <i>%s</i> is replaced by a filename containing the HTML output from <code>groff</code>, <i>%%</i> is replaced by a single percent sign (%), and <i>%c</i> is replaced by a colon (:).</p>
<dt><code>SYSTEM</code></p>
<dd> If $<code>SYSTEM</code> is set, it will have the same effect as if it had been specified as the argument to the <code>-m</code> option.</p>
<dt><code>MANOPT</code></p>
<dd> If $<code>MANOPT</code> is set, it will be parsed prior to <code>man&#8217;s</code> command line and is expected to be in a similar format. As all of the other <code>man</code> specific environment variables can be expressed as command line options, and are thus candidates for being included in $<code>MANOPT</code> it is expected that they will become obsolete. N.B. All spaces that should be interpreted as part of an option&#8217;s argument must be escaped.</p>
<dt><code>MANWIDTH</code></p>
<dd> If $<code>MANWIDTH</code> is set, its value is used as the line length for which manual pages should be formatted. If it is not set, manual pages will be formatted with a line length appropriate to the current terminal (using the value of $<code>COLUMNS</code>, and <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) if available, or falling back to 80 characters if neither is available). Cat pages will only be saved when the default formatting can be used, that is when the terminal line length is between 66 and 80 characters.</p>
<dt><code>MAN_KEEP_FORMATTING</code></p>
<dd> Normally, when output is not being directed to a terminal (such as to a file or a pipe), formatting characters are discarded to make it easier to read the result without special tools. However, if $<code>MAN_KEEP_FORMATTING</code> is set to any non-empty value, these formatting characters are retained. This may be useful for wrappers around <code>man</code> that can interpret formatting characters.</p>
<dt><code>MAN_KEEP_STDERR</code></p>
<dd> Normally, when output is being directed to a terminal (usually to a pager), any error output from the command used to produce formatted versions of manual pages is discarded to avoid interfering with the pager&#8217;s display. Programs such as <code>groff</code> often produce relatively minor error messages about typographical problems such as poor alignment, which are unsightly and generally confusing when displayed along with the manual page. However, some users want to see them anyway, so, if $<code>MAN_KEEP_STDERR</code> is set to any non-empty value, error output will be displayed as usual.</p>
<dt><code>MAN_DISABLE_SECCOMP</code></p>
<dd> On Linux, <code>man</code> normally confines subprocesses that handle untrusted data using a <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) sandbox. This makes it safer to run complex parsing code over arbitrary manual pages. If this goes wrong for some reason unrelated to the content of the page being displayed, you can set $<code>MAN_DISABLE_SECCOMP</code> to any non-empty value to disable the sandbox.</p>
<dt><code>PIPELINE_DEBUG</code></p>
<dd> If the $<code>PIPELINE_DEBUG</code> environment variable is set to &quot;1&quot;, then <code>man</code> will print debugging messages to standard error describing each subprocess it runs.</p>
<dt><code>LANG</code>,<code> LC_MESSAGES</code></p>
<dd> Depending on system and implementation, either or both of $<code>LANG</code> and $<code>LC_MESSAGES</code> will be interrogated for the current message locale. <code>man</code> will display its messages in that locale (if available). See <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) for precise details.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/manpath.config</i></p>
<dd> man-db configuration file.</p>
<dt><i>/usr/share/man</i></p>
<dd> A global manual page hierarchy.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-less/">less</a></code>(1), <code><a href="/docs/linux/man/1-manpath/">manpath</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1), <code><a href="/docs/linux/man/1-zsoelim/">zsoelim</a></code>(1), <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5), <code><a href="/docs/linux/man/7-man/">man</a></code>(7), <code><a href="/docs/linux/man/8-catman/">catman</a></code>(8), <code><a href="/docs/linux/man/8-mandb/">mandb</a></code>(8) </p>
<p> Documentation for some packages may be available in other formats, such as <code><a href="/docs/linux/man/1-info/">info</a></code>(1) or HTML.</p>
<h2>HISTORY</h2>
<p> 1990, 1991 &#8211; Originally written by John W. Eaton (jwe [at] che.utexas.edu). </p>
<p> Dec 23 1992: Rik Faith (faith [at] cs.unc.edu) applied bug fixes supplied by Willem Kasdorp (wkasdo [at] nikhefk.nikef.nl). </p>
<p> 30th April 1994 &#8211; 23rd February 2000: Wilf. (G.Wilford [at] ee.surrey.ac.uk) has been developing and maintaining this package with the help of a few dedicated people. </p>
<p> 30th October 1996 &#8211; 30th March 2001: Fabrizio Polacco &lt;fpolacco [at] debian.org&gt; maintained and enhanced this package for the Debian project, with the help of all the community. </p>
<p> 31st March 2001 &#8211; present day: Colin Watson &lt;cjwatson [at] debian.org&gt; is now developing and maintaining man-db.</p>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
<h2>Index</h2>
