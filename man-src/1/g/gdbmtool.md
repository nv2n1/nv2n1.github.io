---
title: "gdbmtool(1)"
name: "gdbmtool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdbmtool/"
description: "gdbmtool – examine and modify a GDBM database"
---

<h2>NAME</h2>
<p> gdbmtool &#8211; examine and modify a GDBM database</p>
<h2>SYNOPSIS</h2>
<p> <code>gdbmtool</code> [<code>-lmNnqrs</code>] [<code>-b</code> <i>SIZE</i>] [<code>-c</code> <i>SIZE</i>]<br />
&nbsp;<wbr>[<code>-f</code>&nbsp;<wbr><i>FILE</i>]&nbsp;<wbr>[<code>&#8211;block-size</code>=<i>SIZE</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;cache-size</code>=<i>SIZE</i>]&nbsp;<wbr>[<code>&#8211;file</code>&nbsp;<wbr><i>FILE</i>]&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;newdb</code>]&nbsp;<wbr>[<code>&#8211;no-lock</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;no-mmap</code>]&nbsp;<wbr>[<code>&#8211;norc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;quiet</code>]&nbsp;<wbr>[<code>&#8211;read-only</code>]&nbsp;<wbr>[<code>&#8211;synchronize</code>]&nbsp;<wbr>[<i>DBFILE</i>] </p>
<p> <code>gdbmtool</code> [<code>-Vh</code>] ][<code>&#8211;help</code>] [<code>&#8211;usage</code>] [<code>&#8211;version</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>gdbmtool</code> utility allows you to view and modify an existing GDBM database or to create a new one. </p>
<p> The <i>DBFILE</i> argument supplies the name of the database to open. If not supplied, the default name <code>junk.gdbm</code> is used instead. If the named database does not exist, it will be created. An existing database can be cleared (i.e. all records removed from it) using the <code>&#8211;newdb</code> option (see below). </p>
<p> Unless the <code>-N</code> (<code>&#8211;norc</code>) option is given, after startup <code>gdbmtool</code> looks for file named <code>.gdbmtoolrc</code> first in the current working directory, and, if not found there, in the home directory of the user who started the program. If found, this file is read and interpreted as a list of <code>gdbmtool</code> commands. </p>
<p> Then <code>gdbmtool</code> starts a loop, in which it reads commands from the standard input, executes them and prints the results on the standard output. If the standard input is attached to a console, the program runs in interactive mode. </p>
<p> The program terminates when the <code>quit</code> command is given, or end-of-file is detected on its standard input. </p>
<p> A <code>gdbmtool</code> command consists of a command verb, optionally followed by one or more arguments, separated by any amount of white space. A command verb can be entered either in full or in an abbreviated form, as long as that abbreviation does not match any other verb. </p>
<p> Any sequence of non-whitespace characters appearing after the command verb forms an argument. If the argument contains whitespace or unprintable characters it must be enclosed in double quotes. Within double quotes the usual escape sequences are understood, as shown in the table below: </p>
<pre>
        Escape      Expansion
                  Audible bell character (ASCII 7)
                  Backspace character (ASCII 8)
                  Form-feed character (ASCII 12)
        
          Newline character (ASCII 10)
                  Carriage return character (ASCII 13)
        	          Horizontal tabulation character (ASCII 9)
                  Vertical tabulation character (ASCII 11)
        \          Single slash
        </pre>
<p> In addition, a backslash immediately followed by the end-of-line<br />
 character effectively removes that character, allowing to split long arguments over several input lines.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;block-size</code>=<i>SIZE</i></p>
<dd> Set block size.</p>
<dt><code>-c</code>, <code>&#8211;cache-size</code>=<i>SIZE</i></p>
<dd> Set cache size.</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>FILE</i></p>
<dd> Read commands from <i>FILE</i>, instead of from the standard input.</p>
<dt><code>-l</code>, <code>&#8211;no-lock</code></p>
<dd> Disable file locking.</p>
<dt><code>-m</code>, <code>&#8211;no-mmap</code></p>
<dd> Do not use <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<dt><code>-n</code>, <code>&#8211;newdb</code></p>
<dd> Create the database, truncating it if it already exists.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Don&#8217;t print initial banner.</p>
<dt><code>-r</code>, <code>&#8211;read-only</code></p>
<dd> Open database in read-only mode.</p>
<dt><code>-s</code>, <code>&#8211;synchronize</code></p>
<dd> Synchronize to disk after each write.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a short usage summary.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a list of available options.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print program version</dl>
<h2>SHELL COMMANDS</h2>
<dl>
<dt><code>avail</code></p>
<dd> Print the <code>avail list</code>.</p>
<dt><code>bucket</code> <i>NUM</i></p>
<dd> Print the bucket number <i>NUM</i> and set is as the current one.</p>
<dt><code>cache</code></p>
<dd> Print the bucket cache.</p>
<dt><code>close</code></p>
<dd> Close the currently open database.</p>
<dt><code>count</code></p>
<dd> Print the number of entries in the database.</p>
<dt><code>current</code></p>
<dd> Print the current bucket.</p>
<dt><code>delete</code> <i>KEY</i></p>
<dd> Delete record with the given <i>KEY</i>.</p>
<dt><code>dir</code></p>
<dd> Print hash directory.</p>
<dt><code>export</code>, <code>e</code> <i>FILE-NAME</i> [<code>truncate</code>] [<code>binary</code>|<code>ascii</code>]</p>
<dd> Export the database to the flat file <i>FILE-NAME</i>. This is equivalent to <code><a href="/docs/linux/man/1-gdbm_dump/">gdbm_dump</a></code>(1). </p>
<p> This command will not overwrite an existing file, unless the <code>truncate</code> parameter is also given. Another optional parameter determines the type of the dump (*note Flat files::). By default, ASCII dump will be created.</p>
<dt><code>fetch</code> <i>KEY</i></p>
<dd> Fetch and display the record with the given <i>KEY</i>.</p>
<dt><code>first</code></p>
<dd> Fetch and display the first record in the database. Subsequent records can be fetched using the <code>next</code> command (see below).</p>
<dt><code>hash</code> <i>KEY</i></p>
<dd> Compute and display the hash value for the given <i>KEY</i>.</p>
<dt><code>header</code></p>
<dd> Print file header.</p>
<dt><code>help</code> or <code>?</code></p>
<dd> Print a concise command summary, showing each command letter and verb with its parameters and a short description of what it does. Optional arguments are enclosed in square brackets.</p>
<dt><code>import</code> <i>FILE-NAME</i> [<code>replace</code>] [<code>nometa</code>]</p>
<dd> Import data from a flat dump file <i>FILE-NAME</i>. If the <code>replace</code> argument is given, any records with the same keys as the already existing ones will replace them. The <code>nometa</code> argument turns off restoring meta-information from the dump file.</p>
<dt><code>list</code></p>
<dd> List the contents of the database.</p>
<dt><code>next</code> [<i>KEY</i>]</p>
<dd> Sequential access: fetch and display the next record. If the <i>KEY</i> is given, the record following the one with this key will be fetched.</p>
<dt><code>open</code> <i>FILE</i></p>
<dd> Open the database file <i>FILE</i>. If successful, any previously open database is closed. Otherwise, if the operation fails, the currently opened database remains unchanged. </p>
<p> This command takes additional information from the variables <code>open</code>, <code>lock</code>, <code>mmap</code>, and <code>sync</code>. See the section <code>VARIABLES</code>, for a detailed description of these.</p>
<dt><code>quit</code></p>
<dd> Close the database and quit the utility.</p>
<dt><code>reorganize</code></p>
<dd> Reorganize the database. <code>set</code> [<i>VAR</i>=<i>VALUE</i>&#8230;] Without arguments, lists variables and their values. If arguments are specified, sets variables. Boolean variables can be set by specifying variable name, optionally prefixed with <code>no</code>, to set it to <code>false</code>.</p>
<dt><code>source</code> <i>FILE</i></p>
<dd> Read commands from the given <i>FILE</i>.</p>
<dt><code>status</code></p>
<dd> Print current program status.</p>
<dt><code>store</code> <i>KEY</i> <i>DATA</i></p>
<dd> Store the <i>DATA</i> with the given <i>KEY</i> in the database. If the <i>KEY</i> already exists, its data will be replaced.</p>
<dt><code>unset</code> <i>VARIABLE</i>&#8230;</p>
<dd> Unsets listed variables.</p>
<dt><code>version</code></p>
<dd> Print the version of <code>gdbm</code>.</dl>
<h2>DATA DEFINITIONS</h2>
<p> The <code>define</code> statement provides a mechanism for defining key or content structures. It is similar to the <code>C</code> <code>struct</code> declaration: </p>
<pre>
<code>define</code> <code>key</code>|<code>content</code> <code>{</code> <i>defnlist</i> <code>}</code>
</pre>
<p> The <i>defnlist</i> is a comma-separated list of member declarations. Within <i>defnlist</i> the newline character looses its special meaning as the command terminator, so each declaration can appear on a separate line and arbitrary number of comments can be inserted to document the definition. </p>
<p> Each declaration has one of the following formats </p>
<pre>
<i>type</i> <i>name</i>
<i>type</i> <i>name</i> <code>[</code><i>N</i><code>]</code>
</pre>
<p> where <i>type</i> is a data type and <i>name</i> is the member name. The second format defines the member <i>name</i> as an array of <i>N</i> elements of <i>type</i>. </p>
<p> The supported types are: </p>
<pre><code>
type meaning char single byte(signed) short signed short integer
    ushort unsigned short integer
    int signed integer
    unsigned unsigned integer
    uint ditto
    long signed long integer
    ulong unsigned long integer
    llong signed long long integer
    ullong unsigned long long integer
    float a floating point number
    double double -
    precision floating point number
    string array of characters(see the NOTE below)
        stringz null
    - terminated string of characters
</code></pre>
<p> The following alignment declarations can be used within <i>defnlist</i>:</p>
<dl>
<dt><code>offset</code> <i>N</i></p>
<dd> The next member begins at offset <i>N</i>.</p>
<dt><code>pad</code> <i>N</i></p>
<dd> Add <i>N</i> bytes of padding to the previous member.</dl>
<p> For example: </p>
<pre><code>
define content
{
    int status,
        pad 8,
        char id[3],
        stringz name
}
</code></pre>
<p> To define data consisting of a single data member, the following simplified construct can be used: </p>
<pre>
<code>define</code> <code>key</code>|<code>content</code> <i>type</i>
</pre>
<p> where <i>type</i> is one of the types discussed above. </p>
<p> <code>NOTE</code>: The <code>string</code> type can reasonably be used only if it is the last or the only member of the data structure. That&#8217;s because it provides no information about the number of elements in the array, so it is interpreted to contain all bytes up to the end of the datum.</p>
<h2>VARIABLES</h2>
<dl>
<dt><code>confirm</code>, boolean</p>
<dd> Whether to ask for confirmation before certain destructive operations, such as truncating the existing database. Default is <code>true</code>.</p>
<dt><code>ps1</code>, string</p>
<dd> Primary prompt string. Its value can contain <i>conversion specifiers</i>, consisting of the <code>%</code> character followed by another character. These specifiers are expanded in the resulting prompt as follows: </p>
<pre>
        Sequence    Expansion
        <code>%f</code>          name of the db file
        <code>%p</code>          program name
        <code>%P</code>          package name (<code>gdbm</code>)
        <code>%_</code>          horizontal space (<code>ASCII</code> 32)
        <code>%v</code>          program version
        <code>%%</code>          <code>%</code>
</pre>
<p> The default prompt is <code>%p&gt;%_</code>.</p>
<dt><code>ps2</code>, string</p>
<dd> Secondary prompt. See <code>ps1</code> for a description of its value. This prompt is displayed before reading the second and subsequent lines of a multi-line command. </p>
<p> The default value is <code>%_&gt;%_</code>.</p>
<dt><code>delim1</code>, string</p>
<dd> A string used to delimit fields of a structured datum on output (see the section <code>DATA DEFINITIONS</code>). </p>
<p> Default is <code>,</code> (a comma). This variable cannot be unset.</p>
<dt><code>delim2</code>, string</p>
<dd> A string used to delimit array items when printing a structured datum. </p>
<p> Default is <code>,</code> (a comma). This variable cannot be unset.</p>
<dt><code>pager</code>, string</p>
<dd> The name and command line of the pager program to pipe output to. This program is used in interactive mode when the estimated number of output lines is greater then the number of lines on your screen. </p>
<p> The default value is inherited from the environment variable <code>PAGER</code>. Unsetting this variable disables paging.</p>
<dt><code>quiet</code>, boolean</p>
<dd> Whether to display welcome banner at startup. This variable should be set in a startup script file.</dl>
<p> The following variables control how the database is opened:</p>
<dl>
<dt><code>cachesize</code>, numeric</p>
<dd> Sets the cache size. By default this variable is not set.</p>
<dt><code>blocksize</code>, numeric</p>
<dd> Sets the block size. Unset by default.</p>
<dt><code>open</code>, string</p>
<dd> Open mode. The following values are allowed:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>newdb</code></p>
<dd> Truncate the database if it exists or create a new one. Open it in read-write mode.</p>
<dt><code>wrcreat</code> or <code>rw</code></p>
<dd> Open the database in read-write mode. Create it if it does not exist. This is the default.</p>
<dt><code>reader</code> or <code>readonly</code></p>
<dd> Open the database in read-only mode. Signal an error if it does not exist.</dl>
</dl>
<dt><code>lock</code>, boolean</p>
<dd> Lock the database. This is the default.</p>
<dt><code>mmap</code>, boolean</p>
<dd> Use memory mapping. This is the default. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdbm_dump/">gdbm_dump</a></code>(1), <code><a href="/docs/linux/man/1-gdbm_load/">gdbm_load</a></code>(1), <code><a href="/docs/linux/man/3-gdbm/">gdbm</a></code>(3).</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gdbm [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Free Software Foundation, Inc<br />
 License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
