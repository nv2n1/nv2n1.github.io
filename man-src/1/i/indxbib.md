---
title: "indxbib(1)"
name: "indxbib"
section: "1"
letter: "i"
url: "/docs/linux/man/1-indxbib/"
description: "indxbib – make inverted index for bibliographic databases"
---

<h2 class="name">NAME</h2>
<p> indxbib &#8211; make inverted index for bibliographic databases </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-w</code> ] [ <code>-c </code><i>file</i> ] [ <code>-d </code><i>dir</i> ] [ <code>-f </code><i>file</i> ] [ <code>-h </code><i>n</i> ] [ <code>-i </code><i>string</i> ] [ <code>-k </code><i>n</i> ] [ <code>-l </code><i>n</i> ] [ <code>-n </code><i>n</i> ] [ <code>-o </code><i>file</i> ] [ <code>-t </code><i>n</i> ] [<i>filename</i> &#8230;] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>indxbib</code> makes an inverted index for the bibliographic databases in <i>filename</i>&#8230; for use with <code><a href="/docs/linux/man/1-refer/">refer</a></code>(1), <code><a href="/docs/linux/man/1-lookbib/">lookbib</a></code>(1), and <code><a href="/docs/linux/man/1-lkbib/">lkbib</a></code>(1). The index will be named filename<i>.i</i>; the index is written to a temporary file which is then renamed to this. If no filenames are given on the command line because the <code>-f</code> option has been used, and no <code>-o</code> option is given, the index will be named <i>Ind.i</i>. </p>
<p> Bibliographic databases are divided into records by blank lines. Within a record, each fields starts with a <code>%</code> character at the beginning of a line. Fields have a one letter name which follows the <code>%</code> character. </p>
<p> The values set by the <code>-c</code>, <code>-n</code>, <code>-l</code>, and <code>-t</code> options are stored in the index; when the index is searched, keys will be discarded and truncated in a manner appropriate to these options; the original keys will be used for verifying that any record found using the index actually contains the keys. This means that a user of an index need not know whether these options were used in the creation of the index, provided that not all the keys to be searched for would have been discarded during indexing and that the user supplies at least the part of each key that would have remained after being truncated during indexing. The value set by the <code>-i</code> option is also stored in the index and will be used in verifying records found using the index.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-v</code></p>
<dd> Print the version number.</p>
<dt><code>-w</code></p>
<dd> Index whole files. Each file is a separate record.</p>
<dt><code>-c</code><i>file</i></p>
<dd> Read the list of common words from <i>file</i> instead of <i>/usr/:share/:groff/:1.22.4/:eign</i>.</p>
<dt><code>-d</code><i>dir</i></p>
<dd> Use <i>dir</i> as the pathname of the current working directory to store in the index, instead of the path printed by <code><a href="/docs/linux/man/1-pwd/">pwd</a></code>(1). Usually <i>dir</i> will be a symbolic link that points to the directory printed by <code><a href="/docs/linux/man/1-pwd/">pwd</a></code>(1).</p>
<dt><code>-f</code><i>file</i></p>
<dd> Read the files to be indexed from <i>file</i>. If <i>file</i> is <code>&#8211;</code>, files will be read from the standard input. The <code>-f</code> option can be given at most once.</p>
<dt><code>-i</code><i>string</i></p>
<dd> Don&#8217;t index the contents of fields whose names are in <i>string</i>. Initially <i>string</i> is <code>XYZ</code>.</p>
<dt><code>-h</code><i>n</i></p>
<dd> Use the first prime greater than or equal to <i>n</i> for the size of the hash table. Larger values of <i>n</i> will usually make searching faster, but will make the index larger and <code>indxbib</code> use more memory. Initially <i>n</i> is 997.</p>
<dt><code>-k</code><i>n</i></p>
<dd> Use at most <i>n</i> keys per input record. Initially <i>n</i> is 100.</p>
<dt><code>-l</code><i>n</i></p>
<dd> Discard keys that are shorter than <i>n</i>. Initially <i>n</i> is 3.</p>
<dt><code>-n</code><i>n</i></p>
<dd> Discard the <i>n</i> most common words. Initially <i>n</i> is 100.</p>
<dt><code>-o</code><i>basename</i></p>
<dd> The index should be named basename<i>.i</i>.</p>
<dt><code>-t</code><i>n</i></p>
<dd> Truncate keys to <i>n</i>. Initially <i>n</i> is 6.</dl>
<h2>FILES</h2>
<dl>
<dt>filename<i>.i</i></p>
<dd> Index.</p>
<dt><i>Ind.i</i></p>
<dd> Default index name.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:eign</i></p>
<dd> List of common words.</p>
<dt><i>indxbib</i>XXXXXX</p>
<dd> Temporary file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-refer/">refer</a></code>(1), <code><a href="/docs/linux/man/1-lkbib/">lkbib</a></code>(1), <code><a href="/docs/linux/man/1-lookbib/">lookbib</a></code>(1) </p>
<h2>Index</h2>
