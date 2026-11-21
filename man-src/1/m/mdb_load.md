---

title: "mdb_load(1)"
name: "mdb_load"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb_load/"
description: "mdb_load – LMDB environment import tool"
---

<p> mdb_load &#8211; LMDB environment import tool </p>
<h2>SYNOPSIS</h2>
<p> <code>mdb_load</code> [<code>-V</code>] [<code>-f</code><i>&nbsp;<wbr>file</i>] [<code>-n</code>] [<code>-s</code><i>&nbsp;<wbr>subdb</i>] [<code>-N</code>] [<code>-T</code>] <code>&nbsp;<wbr>envpath</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mdb_load</code> utility reads from the standard input and loads it into the LMDB environment <code>envpath</code>. </p>
<p> The input to <code>mdb_load</code> must be in the output format specified by the <code><a href="/docs/linux/man/1-mdb_dump/">mdb_dump</a></code>(1) utility or as specified by the <code>-T</code> option below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></dt>
<dd> Write the library version number to the standard output, and exit.</dd>
<dt><code>-f</code>&nbsp;<wbr>file</dt>
<dd> Read from the specified file instead of from the standard input.</dd>
<dt><code>-n</code></dt>
<dd> Load an LMDB database which does not use subdirectories.</dd>
<dt><code>-s</code>&nbsp;<wbr>subdb</dt>
<dd> Load a specific subdatabase. If no database is specified, data is loaded into the main database.</dd>
<dt><code>-N</code></dt>
<dd> Don&#8217;t overwrite existing records when loading into an already existing database; just skip them.</dd>
<dt><code>-T</code></dt>
<dd> Load data from simple text files. The input must be paired lines of text, where the first line of the pair is the key item, and the second line of the pair is its corresponding data item. </dd>
<p> A simple escape mechanism, where newline and backslash (\) characters are special, is applied to the text input. Newline characters are interpreted as record separators. Backslash characters in the text will be interpreted in one of two ways: If the backslash character precedes another backslash character, the pair will be interpreted as a literal backslash. If the backslash character precedes any other character, the two characters following the backslash will be interpreted as a hexadecimal specification of a single character; for example, \0a is a newline character in the ASCII character set. </p>
<p> For this reason, any backslash or newline characters that naturally occur in the text input must be escaped to avoid misinterpretation by <code>mdb_load</code>. </p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mdb_dump/">mdb_dump</a></code>(1)  </p>
<h2>AUTHOR</h2>
<p> Howard Chu of Symas Corporation &lt;<a rel="nofollow" href="http://www.symas.com">http://www.symas.com</a>&gt; </p>
