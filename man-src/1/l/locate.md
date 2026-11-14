---
title: "locate(1)"
name: "locate"
section: "1"
letter: "l"
url: "/docs/linux/man/1-locate/"
description: "locate – find files by name"
---

<h2 class="name">NAME</h2>
<p> locate &#8211; find files by name</p>
<h2>SYNOPSIS</h2>
<p> <code>locate</code> [<i>OPTION</i>]&#8230; <i>PATTERN</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>locate</code> reads one or more databases prepared by <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8) and writes file names matching at least one of the <i>PATTERN</i>s to standard output, one per line. </p>
<p> If <code>&#8211;regex</code> is not specified, <i>PATTERN</i>s can contain globbing characters. If any <i>PATTERN</i> contains no globbing characters, <code>locate</code> behaves as if the pattern were <code>*</code><i>PATTERN</i><code>*</code>. </p>
<p> By default, <code>locate</code> does not check whether files found in database still exist (but it does require all parent directories to exist if the database was built with <code>&#8211;require-visibility no</code>). <code>locate</code> can never report files created after the most recent update of the relevant database. </p>
<h2>EXIT STATUS</h2>
<p> <code>locate</code> exits with status 0 if any match was found or if <code>locate</code> was invoked with one of the <code>&#8211;limit 0</code>, <code>&#8211;help</code>, <code>&#8211;statistics</code> or <code>&#8211;version</code> options. If no match was found or a fatal error was encountered, <code>locate</code> exits with status 1. </p>
<p> Errors encountered while reading a database are not fatal, search continues in other specified databases, if any. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Print only entries that match all <i>PATTERN</i>s instead of requiring only one of them to match. </p>
<dt><code>-b</code>, <code>&#8211;basename</code></p>
<dd> Match only the base name against the specified patterns. This is the opposite of <code>&#8211;wholename</code>. </p>
<dt><code>-c</code>, <code>&#8211;count</code></p>
<dd> Instead of writing file names on standard output, write the number of matching entries only. </p>
<dt><code>-d, &#8211;database</code> <i>DBPATH</i></p>
<dd> Replace the default database with <i>DBPATH</i>. <i>DBPATH</i> is a <code>:</code>-separated list of database file names. If more than one <code>&#8211;database</code> option is specified, the resulting path is a concatenation of the separate paths. </p>
<p> An empty database file name is replaced by the default database. A database file name <code>&#8211;</code> refers to the standard input. Note that a database can be read from the standard input only once. </p>
<dt><code>-e</code>, <code>&#8211;existing</code></p>
<dd> Print only entries that refer to files existing at the time <code>locate</code> is run. </p>
<dt><code>-L</code>, <code>&#8211;follow</code></p>
<dd> When checking whether files exist (if the <code>&#8211;existing</code> option is specified), follow trailing symbolic links. This causes broken symbolic links to be omitted from the output. </p>
<p> This is the default behavior. The opposite can be specified using <code>&#8211;nofollow</code>. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Write a summary of the available options to standard output and exit successfully. </p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> Ignore case distinctions when matching patterns. </p>
<dt><code>-p</code>, <code>&#8211;ignore-spaces</code></p>
<dd> Ignore punctuation and spaces when matching patterns. </p>
<dt><code>-t</code>, <code>&#8211;transliterate</code></p>
<dd> Ignore accents using iconv transliteration when matching patterns. </p>
<dt><code>-l</code>, <code>&#8211;limit</code>, <code>-n</code> <i>LIMIT</i></p>
<dd> Exit successfully after finding <i>LIMIT</i> entries. If the <code>&#8211;count</code> option is specified, the resulting count is also limited to <i>LIMIT</i>. </p>
<dt><code>-m</code>, <code>&#8211;mmap</code></p>
<dd> Ignored, for compatibility with <font SIZE="-1">BSD</font> and <font SIZE="-1">GNU</font> <code>locate</code>. </p>
<dt><code>-P</code>, <code>&#8211;nofollow</code>, <code>-H</code></p>
<dd> When checking whether files exist (if the <code>&#8211;existing</code> option is specified), do not follow trailing symbolic links. This causes broken symbolic links to be reported like other files. </p>
<p> This is the opposite of <code>&#8211;follow</code>. </p>
<dt><code>-0</code>, <code>&#8211;null</code></p>
<dd> Separate the entries on output using the <font SIZE="-1">ASCII NUL</font> character instead of writing each entry on a separate line. This option is designed for interoperability with the <code>&#8211;null</code> option of <font SIZE="-1">GNU</font> <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1). </p>
<dt><code>-S</code>, <code>&#8211;statistics</code></p>
<dd> Write statistics about each read database to standard output instead of searching for files and exit successfully. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Write no messages about errors encountered while reading and processing databases. </p>
<dt><code>-r</code>, <code>&#8211;regexp</code> <i>REGEXP</i></p>
<dd> Search for a basic regexp <i>REGEXP</i>. No <i>PATTERN</i>s are allowed if this option is used, but this option can be specified multiple times. </p>
<dt><code>&#8211;regex</code></p>
<dd> Interpret all <i>PATTERN</i>s as extended regexps. </p>
<dt><code>-s</code>, <code>&#8211;stdio</code></p>
<dd> Ignored, for compatibility with <font SIZE="-1">BSD</font> and <font SIZE="-1">GNU</font> <code>locate</code>. </p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Write information about the version and license of <code>locate</code> on standard output and exit successfully. </p>
<dt><code>-w</code>, <code>&#8211;wholename</code></p>
<dd> Match only the whole path name against the specified patterns. </p>
<p> This is the default behavior. The opposite can be specified using <code>&#8211;basename</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To search for a file named exactly <i>NAME</i> (not <code>*</code><i>NAME</i><code>*</code>), use</p>
<dl>
<dt>
<dd> <code>locate -b</code> <code>&#8216;\</code><i>NAME</i><code>&#8216;</code></dl>
<p> Because <code>\</code> is a globbing character, this disables the implicit replacement of <i>NAME</i> by <code>*</code><i>NAME</i><code>*</code>. </p>
<h2>FILES</h2>
<dl>
<dt><code>/var/lib/mlocate/mlocate.db</code></p>
<dd> The database searched by default. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LOCATE_PATH</code></p>
<dd> Path to additional databases, added after the default database or the databases specified using the <code>&#8211;database</code> option. </p>
</dl>
<h2>NOTES</h2>
<p> The order in which the requested databases are processed is unspecified, which allows <code>locate</code> to reorder the database path for security reasons. </p>
<p> <code>locate</code> attempts to be compatible to <code>slocate</code> (without the options used for creating databases) and <font SIZE="-1">GNU</font> <code>locate</code>, in that order. This is the reason for the impractical default <code>&#8211;follow</code> option and for the confusing set of <code>&#8211;regex</code> and <code>&#8211;regexp</code> options. </p>
<p> The short spelling of the <code>-r</code> option is incompatible to <font SIZE="-1">GNU</font> <code>locate</code>, where it corresponds to the <code>&#8211;regex</code> option. Use the long option names to avoid confusion. </p>
<p> The <code>LOCATE_PATH</code> environment variable replaces the default database in <font SIZE="-1">BSD</font> and <font SIZE="-1">GNU</font> <code>locate</code>, but it is added to other databases in this implementation and <code>slocate</code>. </p>
<h2>AUTHOR</h2>
<p> Miloslav Trmac &lt;mitr [at] redhat.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8), <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), </p>
<h2>Index</h2>
