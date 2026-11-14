---
title: "lout(1)"
name: "lout"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lout/"
description: "lout – prepare Lout document for printing"
---

<h2>NAME</h2>
<p> lout &#8211; prepare Lout document for printing</p>
<h2>SYNOPSIS</h2>
<p> <code>lout</code> [ <i>options</i> ] <i>file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Invoke the Basser Lout interpreter on the concatenation of the named files, producing a PostScript file on standard output suitable for printing on PostScript printers using <i><a href="/docs/linux/man/1-lpr/">lpr</a></i>(1). If no files are named, stdin is used instead. The special file name `<code>&#8211;</code>&#8216; may be used to denote standard input. White space between flags and their associated option values is optional. </p>
<p> An optional <code>.lt</code> suffix may be used for Lout source and include files. When invoking files ending in this suffix the suffix may be omitted.</p>
<h2>OPTIONS</h2>
<h3>Output</h3>
<dl>
<dt><code>-o</code><i> filename</i></p>
<dd> Direct output to <i>filename</i> instead of to stdout.</p>
<dt><code>-e</code><i> filename</i></p>
<dd> Direct error messages to <i>filename</i> instead of to stderr.</p>
<dt><code>-a</code></p>
<dd> Use &quot;<i>filename</i>:<i>linenum</i>:<i>colnum</i>:<i>message</i>&quot; alternative error message format (useful with Emacs compilation mode and other tools).</dl>
<h3>Output format</h3>
<dl>
<dt><code>-EPS</code></p>
<dd> Produce output in the form of an EPS (Encapsulated PostScript) file, suitable for inclusion in another document. Useful with stand-alone illustrations.</p>
<dt><code>-p</code></p>
<dd> Produce plain text output instead of PostScript.</p>
<dt><code>-P</code></p>
<dd> Like <code>-p</code>, but with a form-feed character between pages.</p>
<dt><code>-Z</code></p>
<dd> Produce Adobe Portable Document Format (PDF) output. This includes links, but the more advanced graphics packages of Lout are not supported.</p>
<dt><code>-PDF</code></p>
<dd> Synonym for <code>-Z.</code></p>
<dt><code>-t</code></p>
<dd> Ignore texture-changing options; everything that would otherwise have been printed using a texture will be printed in solid colour.</dl>
<h3>Cross-reference database</h3>
<dl>
<dt><code>-s</code></p>
<dd> Suppress all reading and writing of the cross reference database; other databases are not affected. Useful when many simple documents that don&#8217;t do any cross referencing are stored in one directory.</p>
<dt><code>-l</code></p>
<dd> Use ASCII order when sorting index entries etc.; the default depends on the COLLATE compilation option (use <code>-V</code> option to find out your default value).</p>
<dt><code>-L</code></p>
<dd> Use your locale&#8217;s order when sorting index entries etc.; the default depends on the COLLATE compilation option (use <code>-V</code> option to find out your default value).</dl>
<h3>Execution of filters</h3>
<dl>
<dt><code>-S</code></p>
<dd> Safe execution: disable all calls to <i><a href="/docs/linux/man/3-system/">system</a></i>(3), instead echoing the commands that would have been executed. Although this makes the Lout run certainly safe, the PostScript output file may not be.</p>
<dt><code>-U</code></p>
<dd> Unsafe execution: allow calls to <i><a href="/docs/linux/man/3-system/">system</a></i>(3). This is usually the default behavior, but it is possible to make safe execution the default during installation (use <code>-V</code> option to find out whether this was done or not), hence the need for this flag.</dl>
<h3>Changing document setup options</h3>
<dl>
<dt><code>&#8212;</code><i>option</i><code>{</code><i>value</i><code>}</code></p>
<dd> Set setup file <i>option</i> to <i>value</i>, overriding any value assigned to <i>option</i> in the setup file. For example, <code>&#8212; [at] PageType{Letter}</code> will set the <code>@PageType</code> setup file option to <code>Letter</code>. The value may be a sequence of words but not an arbitrary Lout object. If there are spaces you must ensure that it is passed to Lout as a single option; the usual way to do this is to enclose it in quotes.</dl>
<h3>Searching for files</h3>
<dl>
<dt><code>-i</code><i> filename</i></p>
<dd> Search the directories of the include file path (see below) for <i>filename</i> or <i>filename</i>.lt and include it. There may be multiple <code>-i</code> options.</p>
<dt><code>-I</code><i> dirname</i></p>
<dd> Add <i>dirname</i> to the list of directories searched for <code>@Include</code> files and <code>-i</code> option files. There may be multiple <code>-I</code> options. <code>@Include</code> first searches the current directory, then searches the <code>-I</code> directories in the order given, and finally searches the default include file directory (see below). <code>@SysInclude</code> and the <code>-i</code> option omit the search of the current directory.</p>
<dt><code>-C</code><i> dirname</i></p>
<dd> Add <i>dirname</i> to the list of directories searched for Lout character mapping (<code>.LCM</code>) files. There may be multiple <code>-C</code> options; the directories are searched in the order given, and finally the default character mappings directory is searched (see below).</p>
<dt><code>-F</code><i> dirname</i></p>
<dd> Add <i>dirname</i> to the list of directories searched for font metrics (formerly <code>.AFM</code>) files. There may be multiple <code>-F</code> options; the directories are searched in the order given, and finally the default font metrics directory is searched (see below).</p>
<dt><code>-H</code><i> dirname</i></p>
<dd> Add <i>dirname</i> to the list of directories searched for hyphenation patterns files, both unpacked (<code>.lh</code>) and packed (<code>.lp</code>). There may be multiple <code>-H</code> options; the directories are searched in the order given, and finally the default hyphenation directory is searched (see below).</p>
<dt><code>-D</code><i> dirname</i></p>
<dd> Add <i>dirname</i> to the list of directories searched for Lout database files. There may be multiple <code>-D</code> options. <code>@Database</code> searches the current directory, then the <code>-D</code> directories in the order given, and finally searches the default databases directory (see below). <code>@SysDatabase</code> omits the search of the current directory.</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt><code>-r num</code></p>
<dd> Run Lout num times, producing output only on the last run. Useful for bringing cross references up to date quickly.</p>
<dt><code>-x</code></p>
<dd> Initializing run, not for ordinary use: read and check all font files mentioned in font definitions, read and check all hyphenation files mentioned in language definitions and build compressed versions, read and check all database files mentioned in database clauses and build index files.</p>
<dt><code>-u</code></p>
<dd> Print usage information on stderr and exit.</p>
<dt><code>-V</code></p>
<dd> Print version information on stderr and exit.</p>
<dt><code>-M</code></p>
<dd> Use less memory and run more slowly (the cross reference database index will be kept in a file rather than in memory).</p>
<dt><code>-w</code></p>
<dd> Show the total number of non-empty words printed in the output file. This includes words and numbers in page headers and footers; section numbers and other numbers; every punctuation character in a font different from its adjacent word; and every little fragment of every equation; so it will always somewhat overestimate the true number.</dl>
<h2>FILES AND ENVIRONMENT VARIABLE</h2>
<pre>
Default include file directory:   <i>LOUTLIB</i>/include
Default databases directory:      <i>LOUTLIB</i>/data
Default font metrics directory:   <i>LOUTLIB</i>/font
Default hyphenation directory:    <i>LOUTLIB</i>/hyph
Default character mappings dir.:  <i>LOUTLIB</i>/maps
Default locales directory:        <i>LOUTLIB</i>/locale
</pre>
<p> The default library directory, usually <code>/usr/local/lib/lout</code>, can be changed by setting environment variable <font SIZE="-1"><code>LOUTLIB</code></font> to an alternative directory name.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-prg2lout/">prg2lout</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-ghostview/">ghostview</a></code>(1)</p>
<h2>REFERENCES</h2>
<p> Jeffrey H. Kingston, <i>&#8220;A User&#8217;s Guide to the Lout Document Formatting System&#8221;</i>, and <i>&#8220;An Expert&#8217;s Guide to the Lout Document Formatting System&#8221;</i>.</p>
<h2>AUTHOR</h2>
<p> Jeffrey H. Kingston </p>
<h2>Index</h2>
