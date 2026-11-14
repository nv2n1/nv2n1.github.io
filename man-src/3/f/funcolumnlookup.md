---
title: "funcolumnlookup(3)"
name: "funcolumnlookup"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funcolumnlookup/"
description: "FunColumnLookup – lookup a Funtools column"
---

<h2>NAME</h2>
<p> <code>FunColumnLookup &#8211; lookup a Funtools column</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>int FunColumnLookup(Fun fun, char *s, int which,<br />
                    char **name, int *type, int *mode,<br />
                    int *offset, int *n, int *width)</p>
<h2>DESCRIPTION</h2>
<p> The FunColumnLookup() routine returns information about a named (or indexed) column. The first argument is the Fun handle associated with this set of columns. The second argument is the name of the column to look up. If the name argument is <font SIZE="-1">NULL</font>, the argument that follows is the zero-based index into the column array of the column for which information should be returned. The next argument is a pointer to a char *, which will contain the name of the column. The arguments that follow are the addresses of int values into which the following information will be returned:</p>
<dl>
<dt>*</p>
<dd> <code>type</code>: data type of column:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> A: <font SIZE="-1">ASCII</font> characters</p>
<dt>*</p>
<dd> B: unsigned 8-bit char</p>
<dt>*</p>
<dd> I: signed 16-bit int</p>
<dt>*</p>
<dd> U: unsigned 16-bit int (not standard <font SIZE="-1">FITS</font>)</p>
<dt>*</p>
<dd> J: signed 32-bit int</p>
<dt>*</p>
<dd> V: unsigned 32-bit int (not standard <font SIZE="-1">FITS</font>)</p>
<dt>*</p>
<dd> E: 32-bit float</p>
<dt>*</p>
<dd> D: 64-bit float</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>*</p>
<dd> <code>mode</code>: bit flag status of column, including:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <font SIZE="-1">COL_ACTIVE</font> 1 is column activated?</p>
<dt>*</p>
<dd> <font SIZE="-1">COL_IBUF</font> 2 is column in the raw input data?</p>
<dt>*</p>
<dd> <font SIZE="-1">COL_PTR</font> 4 is column a pointer to an array?</p>
<dt>*</p>
<dd> <font SIZE="-1">COL_READ</font> 010 is read mode selected?</p>
<dt>*</p>
<dd> <font SIZE="-1">COL_WRITE</font> 020 is write mode selected?</p>
<dt>*</p>
<dd> <font SIZE="-1">COL_REPLACEME</font> 040 is this column being replaced by user data?</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>*</p>
<dd> <code>offset</code>: byte offset in struct</p>
<dt>*</p>
<dd> <code>n</code>: number of elements (i.e. size of vector) in this column</p>
<dt>*</p>
<dd> <code>width</code>: size in bytes of this column</dl>
<p> If the named column exists, the routine returns a positive integer, otherwise zero is returned. (The positive integer is the index+1 into the column array where this column was located.) </p>
<p> If <font SIZE="-1">NULL</font> is passed as the return address of one (or more) of these values, no data is passed back for that information. For example: </p>
<pre><code>
if (!FunColumnLookup(fun, "phas", 0, NULL NULL, NULL, NULL, &amp;npha, NULL))
    gerror(stderr, "can't find phas column
");
</code></pre>
<p> only returns information about the size of the phas vector.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
