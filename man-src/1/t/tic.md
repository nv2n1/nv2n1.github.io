---
title: "tic(1)"
name: "tic"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tic/"
---

<h2 class="name">NAME</h2>
 

 <b>tic</b> - the <i>terminfo</i> entry-description compiler 

<h2>SYNOPSIS</h2>

 <b>tic</b> [<b>-01CDGIKLNTUVWacfgqrstx</b>] [<b>-e</b> <i>names</i>] [<b>-o</b> <i>dir</i>] [<b>-Q</b>[<i>n</i>]] [<b>-R</b> <i>subset</i>] [<b>-v</b>[<i>n</i>]] [<b>-w</b>[<i>n</i>]] <i>file</i> 

<h2>DESCRIPTION</h2>

 The <b>tic</b> command translates a <b>terminfo</b> file from source format into compiled format. The compiled format is necessary for use with the library routines in <b>ncurses</b>(3NCURSES). 

 As described in <b><a HREF="/docs/linux/man/5-term/">term</a></b>(5), the database may be either a directory tree (one file per terminal entry) or a hashed database (one record per entry). The <b>tic</b> command writes only one type of entry, depending on how it was built: 
&nbsp;.IP&nbsp;&bull;&nbsp;4 For directory trees, the top-level directory, e.g., /usr/share/terminfo, specifies the location of the database. 
&nbsp;.IP&nbsp;&bull;&nbsp;4 For hashed databases, a filename is needed. If the given file is not found by that name, but can be found by adding the suffix &quot;.db&quot;, then that is used.
<dl>
<dt>
<dd> The default name for the hashed database is the same as the default directory name (only adding a &quot;.db&quot; suffix).</dl>
 

 In either case (directory or hashed database), <b>tic</b> will create the container if it does not exist. For a directory, this would be the ``terminfo'' leaf, versus a &quot;terminfo.db&quot; file. 

 The results are normally placed in the system terminfo database <b>/etc/terminfo</b>. The compiled terminal description can be placed in a different terminfo database. There are two ways to achieve this: 
&nbsp;.IP&nbsp;&bull;&nbsp;4 First, you may override the system default either by using the <b>-o</b> option, or by setting the variable <b>TERMINFO</b> in your shell environment to a valid database location. 
&nbsp;.IP&nbsp;&bull;&nbsp;4 Secondly, if <b>tic</b> cannot write in <i>/etc/terminfo</i> or the location specified using your TERMINFO variable, it looks for the directory <i>$HOME/.terminfo</i> (or hashed database <i>$HOME/.terminfo.db)</i>; if that location exists, the entry is placed there. 

 Libraries that read terminfo entries are expected to check in succession 
&nbsp;.IP&nbsp;&bull;&nbsp;4 a location specified with the TERMINFO environment variable, 
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>$HOME/.terminfo</i>, 
&nbsp;.IP&nbsp;&bull;&nbsp;4 directories listed in the TERMINFO_DIRS environment variable, 
&nbsp;.IP&nbsp;&bull;&nbsp;4 a compiled-in list of directories (no default value), and 
&nbsp;.IP&nbsp;&bull;&nbsp;4 the system terminfo database (<i>/etc/terminfo</i>).

<h3>ALIASES</h3>

 

 This is the same program as infotocap and captoinfo; usually those are linked to, or copied from this program: 
&nbsp;.IP&nbsp;&bull;&nbsp;4 When invoked as infotocap, tic sets the <b>-I</b> option. 
&nbsp;.IP&nbsp;&bull;&nbsp;4 When invoked as captoinfo, tic sets the <b>-C</b> option.

<h3>OPTIONS</h3>

<dl>
<dt><b>-0</b>
<dd> restricts the output to a single line
<dt><b>-1</b>
<dd> restricts the output to a single column
<dt><b>-a</b>
<dd> tells <b>tic</b> to retain commented-out capabilities rather than discarding them. Capabilities are commented by prefixing them with a period. This sets the <b>-x</b> option, because it treats the commented-out entries as user-defined names. If the source is termcap, accept the 2-character names required by version 6. Otherwise these are ignored.
<dt><b>-C</b>
<dd> Force source translation to termcap format. Note: this differs from the <b>-C</b> option of <b><a HREF="/docs/linux/man/1-infocmp/">infocmp</a></b>(1) in that it does not merely translate capability names, but also translates terminfo strings to termcap format. Capabilities that are not translatable are left in the entry under their terminfo names but commented out with two preceding dots. The actual format used incorporates some improvements for escaped characters from terminfo format. For a stricter BSD-compatible translation, add the <b>-K</b> option.
<dt>
<dd> If this is combined with <b>-c</b>, <b>tic</b> makes additional checks to report cases where the terminfo values do not have an exact equivalent in termcap form. For example:
<dl>
<dt>
<dd> 
&nbsp;.IP&nbsp;&bull;&nbsp;4 <b>sgr</b> usually will not convert, because termcap lacks the ability to work with more than two parameters, and because termcap lacks many of the arithmetic/logical operators used in terminfo. 
&nbsp;.IP&nbsp;&bull;&nbsp;4 capabilities with more than one delay or with delays before the end of the string will not convert completely.</dl>

<dt><b>-c</b>
<dd> tells <b>tic</b> to only check <i>file</i> for errors, including syntax problems and bad use-links. If you specify <b>-C</b> (<b>-I</b>) with this option, the code will print warnings about entries which, after use resolution, are more than 1023 (4096) bytes long. Due to a fixed buffer length in older termcap libraries, as well as buggy checking for the buffer length (and a documented limit in terminfo), these entries may cause core dumps with other implementations.
<dt>
<dd> <b>tic</b> checks string capabilities to ensure that those with parameters will be valid expressions. It does this check only for the predefined string capabilities; those which are defined with the <b>-x</b> option are ignored.
<dt><b>-D</b>
<dd> tells <b>tic</b> to print the database locations that it knows about, and exit. The first location shown is the one to which it would write compiled terminal descriptions. If <b>tic</b> is not able to find a writable database location according to the rules summarized above, it will print a diagnostic and exit with an error rather than printing a list of database locations.
<dt><b>-e </b><i>names</i>
<dd> Limit writes and translations to the following comma-separated list of terminals. If any name or alias of a terminal matches one of the names in the list, the entry will be written or translated as normal. Otherwise no output will be generated for it. The option value is interpreted as a file containing the list if it contains a '/'. (Note: depending on how tic was compiled, this option may require <b>-I</b> or <b>-C</b>.)
<dt><b>-f</b>
<dd> Display complex terminfo strings which contain if/then/else/endif expressions indented for readability.
<dt><b>-G</b>
<dd> Display constant literals in decimal form rather than their character equivalents.
<dt><b>-g</b>
<dd> Display constant character literals in quoted form rather than their decimal equivalents.
<dt><b>-I</b>
<dd> Force source translation to terminfo format.
<dt><b>-K</b>
<dd> Suppress some longstanding ncurses extensions to termcap format, e.g., &quot;\s&quot; for space.
<dt><b>-L</b>
<dd> Force source translation to terminfo format using the long C variable names listed in &lt;<b>term.h</b>&gt;
<dt><b>-N</b>
<dd> Disable smart defaults. Normally, when translating from termcap to terminfo, the compiler makes a number of assumptions about the defaults of string capabilities <b>reset1_string</b>, <b>carriage_return</b>, <b>cursor_left</b>, <b>cursor_down</b>, <b>scroll_forward</b>, <b>tab</b>, <b>newline</b>, <b>key_backspace</b>, <b>key_left</b>, and <b>key_down</b>, then attempts to use obsolete termcap capabilities to deduce correct values. It also normally suppresses output of obsolete termcap capabilities such as <b>bs</b>. This option forces a more literal translation that also preserves the obsolete capabilities.
<dt><b>-o</b><i>dir</i>
<dd> Write compiled entries to given database location. Overrides the TERMINFO environment variable.
<dt><b>-Q</b><i>n</i>
<dd> Rather than show source in terminfo (text) format, print the compiled (binary) format in hexadecimal or base64 form, depending on the option's value:
<dl>
<dt>
<dd>
<dl>
<dt>1
<dd> hexadecimal
<dt>2
<dd> base64
<dt>3
<dd> hexadecimal and base64</dl>
</dl>

<dt><b>-q</b>
<dd> Suppress comments and blank lines when showing translated source.
<dt><b>-R</b><i>subset</i>
<dd> Restrict output to a given subset. This option is for use with archaic versions of terminfo like those on SVr1, Ultrix, or HP-UX that do not support the full set of SVR4/XSI Curses terminfo; and outright broken ports like AIX 3.x that have their own extensions incompatible with SVr4/XSI. Available subsets are ``SVr1'', ``Ultrix'', ``HP'', ``BSD'' and ``AIX''; see <b><a HREF="/docs/linux/man/5-terminfo/">terminfo</a></b>(5) for details.
<dt><b>-r</b>
<dd> Force entry resolution (so there are no remaining tc capabilities) even when doing translation to termcap format. This may be needed if you are preparing a termcap file for a termcap library (such as GNU termcap through version 1.3 or BSD termcap through 4.3BSD) that does not handle multiple tc capabilities per entry.
<dt><b>-s</b>
<dd> Summarize the compile by showing the database location into which entries are written, and the number of entries which are compiled.
<dt><b>-T</b>
<dd> eliminates size-restrictions on the generated text. This is mainly useful for testing and analysis, since the compiled descriptions are limited (e.g., 1023 for termcap, 4096 for terminfo).
<dt><b>-t</b>
<dd> tells <b>tic</b> to discard commented-out capabilities. Normally when translating from terminfo to termcap, untranslatable capabilities are commented-out.
<dt><b>-U</b>
<dd> tells <b>tic</b> to not post-process the data after parsing the source file. Normally, it infers data which is commonly missing in older terminfo data, or in termcaps.
<dt><b>-V</b>
<dd> reports the version of ncurses which was used in this program, and exits.
<dt><b>-v</b><i>n</i>
<dd> specifies that (verbose) output be written to standard error trace information showing <b>tic</b>'s progress.
<dt>
<dd> The optional parameter <i>n</i> is a number from 1 to 10, inclusive, indicating the desired level of detail of information. If ncurses is built without tracing support, the optional parameter is ignored. If <i>n</i> is omitted, the default level is 1. If <i>n</i> is specified and greater than 1, the level of detail is increased.
<dl>
<dt>
<dd> 

 The debug flag levels are as follows:
<dl>
<dt>1
<dd> Names of files created and linked
<dt>2
<dd> Information related to the ``use'' facility
<dt>3
<dd> Statistics from the hashing algorithm
<dt>5
<dd> String-table memory allocations
<dt>7
<dd> Entries into the string-table
<dt>8
<dd> List of tokens encountered by scanner
<dt>9
<dd> All values computed in construction of the hash table</dl>
 

 If the debug level <i>n</i> is not given, it is taken to be one.</dl>

<dt><b>-W</b>
<dd> By itself, the <b>-w</b> option will not force long strings to be wrapped. Use the <b>-W</b> option to do this.
<dt>
<dd> If you specify both <b>-f</b> and <b>-W</b> options, the latter is ignored when <b>-f</b> has already split the line.
<dt><b>-w</b><i>n</i>
<dd> specifies the width of the output. The parameter is optional. If it is omitted, it defaults to 60.
<dt><b>-x</b>
<dd> Treat unknown capabilities as user-defined (see <b><a HREF="/docs/linux/man/5-user_caps/">user_caps</a>(5)</b>). That is, if you supply a capability name which <b>tic</b> does not recognize, it will infer its type (boolean, number or string) from the syntax and make an extended table entry for that. User-defined capability strings whose name begins with ``k'' are treated as function keys.</dl>

<h3>PARAMETERS</h3>

<dl>
<dt><i>file</i>
<dd> contains one or more <b>terminfo</b> terminal descriptions in source format [see <b><a HREF="/docs/linux/man/5-terminfo/">terminfo</a></b>(5)]. Each description in the file describes the capabilities of a particular terminal.
<dt>
<dd> If <i>file</i> is ``-'', then the data is read from the standard input. The <i>file</i> parameter may also be the path of a character-device.</dl>

<h3>PROCESSING</h3>

 

 All but one of the capabilities recognized by <b>tic</b> are documented in <b><a HREF="/docs/linux/man/5-terminfo/">terminfo</a></b>(5). The exception is the <b>use</b> capability. 

 When a <b>use</b>=<i>entry</i>-<i>name</i> field is discovered in a terminal entry currently being compiled, <b>tic</b> reads in the binary from <b>/etc/terminfo</b> to complete the entry. (Entries created from <i>file</i> will be used first. <b>tic</b> duplicates the capabilities in <i>entry</i>-<i>name</i> for the current entry, with the exception of those capabilities that explicitly are defined in the current entry. 

 When an entry, e.g., <b>entry_name_1</b>, contains a <b>use=</b><i>entry</i>_<i>name</i>_<i>2</i> field, any canceled capabilities in <i>entry</i>_<i>name</i>_<i>2</i> must also appear in <b>entry_name_1</b> before <b>use=</b> for these capabilities to be canceled in <b>entry_name_1</b>. 

 Total compiled entries cannot exceed 4096 bytes. The name field cannot exceed 512 bytes. Terminal names exceeding the maximum alias length (32 characters on systems with long filenames, 14 characters otherwise) will be truncated to the maximum alias length and a warning message will be printed.

<h2>HISTORY</h2>

 

 System V Release 2 provided a <b>tic</b> utility. It accepted a single option: <b>-v</b> (optionally followed by a number). According to Ross Ridge's comment in <i>mytinfo</i>, this version of <b>tic</b> was unable to represent cancelled capabilities. 

 System V Release 3 provided a different <b>tic</b> utility, written by Pavel Curtis, (originally named ``compile'' in <i>pcurses</i>). This added an option <b>-c</b> to check the file for errors, with the caveat that errors in ``use='' links would not be reported. System V Release 3 documented a few warning messages which did not appear in <i>pcurses</i>. While the program itself was changed little as development continued with System V Release 4, the table of capabilities grew from 180 (<i>pcurses</i>) to 464 (Solaris). 

 In early development of ncurses (1993), Zeyd Ben-Halim used the table from <i>mytinfo</i> to extend the <i>pcurses</i> table to 469 capabilities (456 matched SVr4, 8 were only in SVr4, 13 were not in SVr4). Of those 13, 11 were ultimately discarded (perhaps to match the draft of X/Open Curses). The exceptions were <b>memory_lock_above</b> and <b>memory_unlock</b> (see <b><a HREF="/docs/linux/man/5-user_caps/">user_caps</a></b>(5)). 

 Eric Raymond incorporated parts of <i>mytinfo</i> into ncurses to implement the termcap-to-terminfo source conversion, and extended that to begin development of the corresponding terminfo-to-termcap source conversion, Thomas Dickey completed that development over the course of several years. 

 In 1999, Thomas Dickey added the <b>-x</b> option to support user-defined capabilities. 

 In 2010, Roy Marples provided a <b>tic</b> program and terminfo library for NetBSD. That implementation adapts several features from ncurses, including <b>tic</b>'s <b>-x</b> option. 

 The <b>-c</b> option tells <b>tic</b> to check for problems in the terminfo source file. Continued development provides additional checks: 
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>pcurses</i> had 8 warnings 
&nbsp;.IP&nbsp;&bull;&nbsp;4 ncurses in 1996 had 16 warnings 
&nbsp;.IP&nbsp;&bull;&nbsp;4 Solaris (SVr4) curses has 28 warnings 
&nbsp;.IP&nbsp;&bull;&nbsp;4 NetBSD tic in 2019 has 19 warnings. 
&nbsp;.IP&nbsp;&bull;&nbsp;4 ncurses in 2019 has 96 warnings 

 The checking done in ncurses' <b>tic</b> helps with the conversion to termcap, as well as pointing out errors and inconsistencies. It is also used to ensure consistency with the user-defined capabilities. There are 527 distinct capabilities in ncurses' terminal database; 128 of those are user-defined.

<h2>PORTABILITY</h2>

 

 X/Open Curses, Issue 7 (2009) provides a brief description of <b>tic</b>. It lists one option: <b>-c</b>. The omission of <b>-v</b> is unexpected. The change history states that the description is derived from True64 UNIX. According to its manual pages, that system also supported the <b>-v</b> option. 

 Shortly after Issue 7 was released, Tru64 was discontinued. As of 2019, the surviving implementations of <b>tic</b> are SVr4 (AIX, HP-UX and Solaris), ncurses and NetBSD curses. The SVr4 <b>tic</b> programs all support the <b>-v</b> option. The NetBSD <b>tic</b> program follows X/Open's documentation, omitting the <b>-v</b> option. 

 The X/Open rationale states that some implementations of <b>tic</b> read terminal descriptions from the standard input if the <i>file</i> parameter is omitted. None of these implementations do that. Further, it comments that some may choose to read from ''./terminfo.src'' but that is obsolescent behavior from SVr2, and is not (for example) a documented feature of SVr3.

<h3>COMPATIBILITY</h3>

 There is some evidence that historic <b>tic</b> implementations treated description fields with no whitespace in them as additional aliases or short names. This <b>tic</b> does not do that, but it does warn when description fields may be treated that way and check them for dangerous characters.

<h3>EXTENSIONS</h3>

 Unlike the SVr4 <b>tic</b> command, this implementation can actually compile termcap sources. In fact, entries in terminfo and termcap syntax can be mixed in a single source file. See <b><a HREF="/docs/linux/man/5-terminfo/">terminfo</a></b>(5) for the list of termcap names taken to be equivalent to terminfo names. 

 The SVr4 manual pages are not clear on the resolution rules for <b>use</b> capabilities. This implementation of <b>tic</b> will find <b>use</b> targets anywhere in the source file, or anywhere in the file tree rooted at <b>TERMINFO</b> (if <b>TERMINFO</b> is defined), or in the user's <i>$HOME/.terminfo</i> database (if it exists), or (finally) anywhere in the system's file tree of compiled entries. 

 The error messages from this <b>tic</b> have the same format as GNU C error messages, and can be parsed by GNU Emacs's compile facility. 

 Aside from <b>-c</b> and <b>-v</b>, options are not portable: 
&nbsp;.IP&nbsp;&bull;&nbsp;4 Most of tic's options are not supported by SVr4 <b>tic</b>: 

<dl>
<dt>
<dd> <b>-0</b> <b>-1</b> <b>-C</b> <b>-G</b> <b>-I</b> <b>-N</b> <b>-R</b> <b>-T</b> <b>-V</b> <b>-a</b> <b>-e</b> <b>-f</b> <b>-g</b> <b>-o</b> <b>-r</b> <b>-s</b> <b>-t</b> <b>-x</b></dl>
 
&nbsp;.IP&nbsp;&bull;&nbsp;4 The NetBSD <b>tic</b> supports a few of the ncurses options 

<dl>
<dt>
<dd> <b>-a</b> <b>-o</b> <b>-x</b></dl>

<dl>
<dt>
<dd> and adds <b>-S</b> (a feature which does the same thing as infocmp's <b>-e</b> and <b>-E</b> options).</dl>
 

 The SVr4 <b>-c</b> mode does not report bad ``use='' links. 

 System V does not compile entries to or read entries from your <i>$HOME/.terminfo</i> database unless TERMINFO is explicitly set to it.

<h2>FILES</h2>

<dl>
<dt><b>/etc/terminfo/?/*</b>
<dd> Compiled terminal description database.</dl>

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/1-captoinfo/">captoinfo</a></b>(1), <b><a HREF="/docs/linux/man/1-infocmp/">infocmp</a></b>(1), <b><a HREF="/docs/linux/man/1-infotocap/">infotocap</a></b>(1), <b><a HREF="/docs/linux/man/1-toe/">toe</a></b>(1), <b>ncurses</b>(3NCURSES), <b><a HREF="/docs/linux/man/5-term/">term</a></b>(5). <b><a HREF="/docs/linux/man/5-terminfo/">terminfo</a></b>(5). <b><a HREF="/docs/linux/man/5-user_caps/">user_caps</a></b>(5). 

 This describes <b>ncurses</b> version 6.3 (patch 20211021).

<h2>AUTHOR</h2>

 Eric S. Raymond &lt;esr [at] snark.thyrsus.com&gt; and 
 Thomas E. Dickey &lt;dickey [at] invisible-island.net&gt; 

<h2>Index</h2>


