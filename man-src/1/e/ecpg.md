---
title: "ecpg(1)"
name: "ecpg"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecpg/"
description: "ecpg – embedded SQL C preprocessor"
---

<h2 class="name">NAME</h2>
<p> ecpg &#8211; embedded SQL C preprocessor </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ecpg</code> [<i>option</i>&#8230;] <i>file</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<p> <code>ecpg</code></p>
<dd>is the embedded SQL preprocessor for C programs. It converts C programs with embedded SQL statements to normal C code by replacing the SQL invocations with special function calls. The output files can then be processed with any C compiler tool chain. </p>
<p> <code>ecpg</code> will convert each input file given on the command line to the corresponding C output file. Input files preferably have the extension .pgc, in which case the extension will be replaced by .c to determine the output file name. If the extension of the input file is not .pgc, then the output file name is computed by appending .c to the full file name. The output file name can also be overridden using the <code>-o</code> option. </p>
<p> This reference page does not describe the embedded SQL language. See Chapter 33, ECPG &#8211; Embedded SQL in C, in the documentation for more information on that topic.</p>
<h2>OPTIONS</h2>
<p> <code>ecpg</code> accepts the following command-line arguments: </p>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Automatically generate certain C code from SQL code. Currently, this works for EXEC SQL TYPE.</dl>
<p> <code>-C </code><i>mode</i></p>
<dl>
<dt>
<dd> Set a compatibility mode. <i>mode</i> can be INFORMIX or INFORMIX_SE.</dl>
<p> <code>-D </code><i>symbol</i></p>
<dl>
<dt>
<dd> Define a C preprocessor symbol.</dl>
<p> <code>-h </code></p>
<dl>
<dt>
<dd> Parse a header file, this option includes otion <code>-c</code>.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Parse system include files as well.</dl>
<p> <code>-I </code><i>directory</i></p>
<dl>
<dt>
<dd> Specify an additional include path, used to find files included via EXEC SQL INCLUDE. Defaults are . (current directory), /usr/local/include, the PostgreSQL include directory which is defined at compile time (default: /usr/local/pgsql/include), and /usr/include, in that order.</dl>
<p> <code>-o </code><i>filename</i></p>
<dl>
<dt>
<dd> Specifies that <code>ecpg</code> should write all its output to the given <i>filename</i>.</dl>
<p> <code>-r </code><i>option</i></p>
<dl>
<dt>
<dd> Selects run-time behavior. <i>Option</i> can be one of the following: </p>
<p> <code>no_indicator</code></p>
<dl>
<dt>
<dd> Do not use indicators but instead use special values to represent null values. Historically there have been databases using this approach.</dl>
<p> <code>prepare</code></p>
<dl>
<dt>
<dd> Prepare all statements before using them. Libecpg will keep a cache of prepared statements and reuse a statement if it gets executed again. If the cache runs full, libecpg will free the least used statement.</dl>
<p> <code>questionmarks</code></p>
<dl>
<dt>
<dd> Allow question mark as placeholder for compatibility reasons. This used to be the default long ago.</dl>
</dl>
<p> <code>&#8211;regression</code></p>
<dl>
<dt>
<dd> Run in regression testing mode.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Turn on autocommit of transactions. In this mode, each SQL command is automatically committed unless it is inside an explicit transaction block. In the default mode, commands are committed only when <code>EXEC SQL COMMIT</code> is issued.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Print additional information including the version and the &quot;include&quot; path.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the ecpg version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about ecpg command line arguments, and exit.</dl>
<h2>NOTES</h2>
<p> When compiling the preprocessed C code files, the compiler needs to be able to find the ECPG header files in the PostgreSQL include directory. Therefore, you might have to use the <code>-I</code> option when invoking the compiler (e.g., -I/usr/local/pgsql/include). </p>
<p> Programs using C code with embedded SQL have to be linked against the libecpg library, for example using the linker options -L/usr/local/pgsql/lib -lecpg. </p>
<p> The value of either of these directories that is appropriate for the installation can be found out using <code><a href="/docs/linux/man/1-pg_config/">pg_config</a></code>(1).</p>
<h2>EXAMPLES</h2>
<p> If you have an embedded SQL C source file named prog1.pgc, you can create an executable program using the following sequence of commands: </p>
<dl>
<dt>
<dd>
<pre>
ecpg prog1.pgc
cc -I/usr/local/pgsql/include -c prog1.c
cc -o prog1 prog1.o -L/usr/local/pgsql/lib -lecpg
</pre>
</dl>
<h2>Index</h2>
