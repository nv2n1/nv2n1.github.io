---
title: "cdb(1)"
name: "cdb"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdb/"
description: "cdb – Constant DataBase manipulation tool"
---

<h2>NAME</h2>
<p> cdb &#8211; Constant DataBase manipulation tool</p>
<h2>SYNOPSYS</h2>
<p> <code>cdb</code> -q [-m] [-n <i>num</i>] <i>dbname</i> <i>key</i><br />
 <code>cdb</code> -d [-m] [<i>dbname</i>|-]<br />
 <code>cdb</code> -l [-m] [<i>dbname</i>|-]<br />
 <code>cdb</code> -s [<i>dbname</i>|-]<br />
 <code>cdb</code> -c [-m] [-t <i>tmpname</i>|-] [-p <i>perms</i>] [-weru0] <i>dbname</i> [<i>infile</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>cdb</code> used to query, dump, list, analyze or create CDB (Constant DataBase) files. Format of cdb described in <i><a href="/docs/linux/man/5-cdb/">cdb</a></i>(5) manpage. This manual page corresponds to version <code>0.78</code> of <code>tinycdb</code> package. </p>
<h3>Query</h3>
<p> <code>cdb -q</code> finds given <i>key</i> in a given <i>dbname</i> cdb file, and writes associated value to standard output if found (and exits with zero), or exits with non-zero if not found. <i>dbname</i> must be seekable file, and stdin can not be used as input. By default, <code>cdb</code> will print <i>all</i> records found. Options recognized in query mode: </p>
<dl>
<dt><code>-n</code><i>num</i></p>
<dd> causes <code>cdb</code> to find and write a record with a given number <i>num</i> starting with 1 &#8212; when there are many records with a given key. </p>
<dt><code>-m</code></p>
<dd> newline will be added after every value printed. By default, multiple values will be written without any delimiter. </p>
</dl>
<h3>Dump/List</h3>
<p> <code>cdb -d</code> dumps contents, and <code>cdb -l</code> lists keys of <i>cdbfile</i> (or standard input if not specified) to standard output, in format controlled by presence of <code>-m</code> option. See subsection &quot;Formats&quot; below. Output from <code>cdb -d</code> can be used as an input for <code>cdb -c</code>. </p>
<h3>Create</h3>
<p> Cdb database created in two stages: temporary database is created, and after it is complete, it gets atomically renamed to permanent place. This avoids requirements for locking between readers and writers (or creaters). <code>cdb -c</code> will attempt to create cdb in file <i>tmpname</i> (or <i>dbname</i> with &quot;.tmp&quot; appended if no -t option given) and then rename it to <i>dbname</i>. It will read supplied <i>infile</i>s (or standard input if none specified). Options recognized in create mode: </p>
<dl>
<dt><code>-t </code><i>tmpname</i></p>
<dd> use given <i>tmpname</i> as temporary file. Defaults to <i>dbname</i>.tmp (i.e. with output file with .tmp added). Note <i>tmpname</i> must be in the same filesystem as output file, as <code>cdb</code> uses <i><a href="/docs/linux/man/2-rename/">rename</a></i>(2) to finalize the database creation procedure. If <i>tmpname</i> is a single dash (-), no temp file will be created, database will be built in-place. This mode is useful when the final renaming is done by the caller. </p>
<dt><code>-p </code><i>perms</i></p>
<dd> permissions for the newly created file (usually an octal number, like 0644). By default the permissions are 0666 (with current process umask applied). If this option is specified, current umask value has no effect. </p>
<dt><code>-w</code></p>
<dd> warn about duplicate keys. </p>
<dt><code>-e</code></p>
<dd> abort on duplicate keys (implies -w). </p>
<dt><code>-r</code></p>
<dd> replace existing key with new one in case of duplicate. This may require database file rewrite to remove old records, and can be slow. </p>
<dt><code>-0</code></p>
<dd> zero-fill existing records when duplicate records are added. This is faster than <code>-r</code>, but leaves extra zeros in the database file in case of duplicates. </p>
<dt><code>-u</code></p>
<dd> do not add duplicate records. </p>
<dt><code>-m</code></p>
<dd> interpret input as a sequence of lines, one record per line, with value separated from a key by space or tab characters, instead of native cdb format (see &quot;Input/Output Format&quot; below). </p>
</dl>
<p> Note that using any option that requires duplicate checking will slow creation process <i>significantly</i>, especially for large databases. </p>
<h3>Statistics</h3>
<p> <code>cdb -s</code> will analyze <i>dbfile</i> and print summary to standard output. Statistics include: total number of rows in a file, minimum, average and maximum key and value lengths, hash tables (max 256) and entries used, number of hash collisions (that is, more than one key point to the same hash table entry), minimum, average and maximum hash table size (of non-empty tables), and number of keys that sits at 10 different distances from it&#8217;s calculated hash table index &#8212; keys in distance 0 requires only one hash table lookup, 1 &#8212; two and so on; more keys at greater distance means slower database search. </p>
<h3>Input/Output Format</h3>
<p> By default, <code>cdb</code> expects (for create operation) or writes (for dump/list) native cdb format data. Cdb native format is a sequence of records in a form: </p>
<p>&nbsp;<wbr>+<i>klen</i>,<i>vlen</i>:<i>key</i>-&gt;<i>val</i>
<br />
 where &quot;+&quot;, &quot;,&quot;, &quot;:&quot;, &quot;-&quot;, &quot;&gt;&quot; and &quot;
&quot; (newline) are literal characters, <i>klen</i> and <i>vlen</i> are length of key and value as decimal numbers, and <i>key</i> and <i>val</i> are key and value themselves. Series of records terminated by an empty line. This is the only format where key and value may contain any character including newline, zero (
