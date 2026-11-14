---
title: "xrmdestroydatabase(3)"
name: "xrmdestroydatabase"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrmdestroydatabase/"
description: "XrmGetFileDatabase, XrmPutFileDatabase, XrmGetStringDatabase, XrmLocaleOfDatabase, XrmGetDatabase, XrmSetDatabase, XrmDestroyDatabase – retrieve and store resource databases"
---

<p>XrmGetFileDatabase, XrmPutFileDatabase, XrmGetStringDatabase, XrmLocaleOfDatabase, XrmGetDatabase, XrmSetDatabase, XrmDestroyDatabase &#8211; retrieve and store resource databases </p>
<h2>Syntax</h2>
<dl COMPACT>
<dt> #include &lt;X11/Xresource.h&gt;</p>
<dd>XrmDatabase XrmGetFileDatabase(char *<i>filename</i>);</p>
<dd>void XrmPutFileDatabase(XrmDatabase <i>database</i>, char *<i>stored_db</i>);</p>
<dd>XrmDatabase XrmGetStringDatabase(char *<i>data</i>);</p>
<dd>char *XrmLocaleOfDatabase(XrmDatabase <i>database</i>);</p>
<dd>XrmDatabase XrmGetDatabase(Display *<i>display</i>);</p>
<dd>void XrmSetDatabase(Display *<i>display</i>, XrmDatabase <i>database</i>);</p>
<dd>void XrmDestroyDatabase(XrmDatabase <i>database</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>filename</i></p>
<dd>Specifies the resource database file name.</p>
<dt><i>database</i></p>
<dd>Specifies the database that is to be used.</p>
<dt><i>stored_db</i></p>
<dd>Specifies the file name for the stored database.</p>
<dt><i>data</i></p>
<dd>Specifies the database contents using a string.</p>
<dt><i>database</i></p>
<dd>Specifies the resource database.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</dl>
<h2>Description</h2>
<p>The <code>XrmGetFileDatabase</code> function opens the specified file, creates a new resource database, and loads it with the specifications read in from the specified file. The specified file should contain a sequence of entries in valid ResourceLine format (see section 15.1); the database that results from reading a file with incorrect syntax is implementation-dependent. The file is parsed in the current locale, and the database is created in the current locale. If it cannot open the specified file, <code>XrmGetFileDatabase</code> returns NULL. </p>
<p> The <code>XrmPutFileDatabase</code> function stores a copy of the specified database in the specified file. Text is written to the file as a sequence of entries in valid ResourceLine format (see section 15.1). The file is written in the locale of the database. Entries containing resource names that are not in the Host Portable Character Encoding or containing values that are not in the encoding of the database locale, are written in an implementation-dependent manner. The order in which entries are written is implementation-dependent. Entries with representation types other than &#8220;String&#8221; are ignored. </p>
<p> The <code>XrmGetStringDatabase</code> function creates a new database and stores the resources specified in the specified null-terminated string. <code>XrmGetStringDatabase</code> is similar to <code>XrmGetFileDatabase</code> except that it reads the information out of a string instead of out of a file. The string should contain a sequence of entries in valid ResourceLine format (see section 15.1) terminated by a null character; the database that results from using a string with incorrect syntax is implementation-dependent. The string is parsed in the current locale, and the database is created in the current locale. </p>
<p> If database is NULL, <code>XrmDestroyDatabase</code> returns immediately. </p>
<p> The <code>XrmLocaleOfDatabase</code> function returns the name of the locale bound to the specified database, as a null-terminated string. The returned locale name string is owned by Xlib and should not be modified or freed by the client. Xlib is not permitted to free the string until the database is destroyed. Until the string is freed, it will not be modified by Xlib. </p>
<p> The <code>XrmGetDatabase</code> function returns the database associated with the specified display. It returns NULL if a database has not yet been set. </p>
<p> The <code>XrmSetDatabase</code> function associates the specified resource database (or NULL) with the specified display. The database previously associated with the display (if any) is not destroyed. A client or toolkit may find this function convenient for retaining a database once it is constructed.</p>
<h2>File Syntax</h2>
<p>The syntax of a resource file is a sequence of resource lines terminated by newline characters or the end of the file. The syntax of an individual resource line is: </p>
<pre>ResourceLine = Comment | IncludeFile | ResourceSpec | &lt;empty line&gt;
Comment = &quot;!&quot; {&lt;any character except null or newline&gt;}
IncludeFile = &quot;#&quot; WhiteSpace &quot;include&quot; WhiteSpace FileName WhiteSpace
FileName = &lt;valid filename for operating system&gt;
ResourceSpec = WhiteSpace ResourceName WhiteSpace &quot;:&quot; WhiteSpace Value
ResourceName = [Binding] {Component Binding} ComponentName
Binding = &quot;.&quot; | &quot;*&quot;
WhiteSpace = {&lt;space&gt; | &lt;horizontal tab&gt;}
Component = &quot;?&quot; | ComponentName
ComponentName = NameChar {NameChar}
NameChar = &quot;a&quot;-&quot;z&quot; | &quot;A&quot;-&quot;Z&quot; | &quot;0&quot;-&quot;9&quot; | &quot;_&quot; | &quot;-&quot;
Value = {&lt;any character except null or unescaped newline&gt;}</pre>
<p>Elements separated by vertical bar (|) are alternatives. Curly braces ({&#8230;}) indicate zero or more repetitions of the enclosed elements. Square brackets ([&#8230;]) indicate that the enclosed element is optional. Quotes (&quot;&#8230;&quot;) are used around literal characters. </p>
<p> IncludeFile lines are interpreted by replacing the line with the contents of the specified file. The word &#8220;include&#8221; must be in lowercase. The file name is interpreted relative to the directory of the file in which the line occurs (for example, if the file name contains no directory or contains a relative directory specification). </p>
<p> If a ResourceName contains a contiguous sequence of two or more Binding characters, the sequence will be replaced with single &#8220;.&#8221; character if the sequence contains only &#8220;.&#8221; characters; otherwise, the sequence will be replaced with a single &#8220;*&#8221; character. </p>
<p> A resource database never contains more than one entry for a given ResourceName. If a resource file contains multiple lines with the same ResourceName, the last line in the file is used. </p>
<p> Any white space characters before or after the name or colon in a ResourceSpec are ignored. To allow a Value to begin with white space, the two-character sequence &#8220;\<i>space</i>&#8221; (backslash followed by space) is recognized and replaced by a space character, and the two-character sequence &#8220;\<i>tab</i>&#8221; (backslash followed by horizontal tab) is recognized and replaced by a horizontal tab character. To allow a Value to contain embedded newline characters, the two-character sequence &#8220;
&#8221; is recognized and replaced by a newline character. To allow a Value to be broken across multiple lines in a text file, the two-character sequence &#8220;\<i>newline</i>&#8221; (backslash followed by newline) is recognized and removed from the value. To allow a Value to contain arbitrary character codes, the four-character sequence &#8220;\<i>nnn</i>&#8221;, where each <i>n</i> is a digit character in the range of &#8220;0&#8221;-&#8220;7&#8221;, is recognized and replaced with a single byte that contains the octal value specified by the sequence. Finally, the two-character sequence &#8220;\&#8221; is recognized and replaced with a single backslash.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xrmgetresource/">XrmGetResource</a>(3), <a href="/docs/linux/man/3-xrminitialize/">XrmInitialize</a>(3), <a href="/docs/linux/man/3-xrmputresource/">XrmPutResource</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
