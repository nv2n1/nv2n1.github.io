---
title: "nf(1)"
name: "nf"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nf/"
description: "fmt-ptrn – A simple template system"
---

<h2>NAME</h2>
<p> fmt-ptrn &#8211; A simple template system</p>
<h2>SYNOPSIS</h2>
<p> <code>fmt-ptrn [options] filename [template]</code></p>
<h2>OVERVIEW</h2>
<p> New is a template system, especially useful in conjunction with a simple text editor such as vi. The user maintains templates which may contain format strings. At run time, nf replaces the format strings in a template with appropriate values to create a new file. </p>
<p> For example, given the following template: </p>
<dl>
<dt>
<dd>
<pre>
//   FILE: %%(FILE)
// AUTHOR: %%(FULLNAME)
//   DATE: %%(DATE)
// Copyright (C) 1999 %%(FULLNAME) %%(EMAIL)
// All rights reserved.
</pre>
</dl>
<p> nf will create: </p>
<dl>
<dt>
<dd>
<pre>
//   FILE: foo.cpp
// AUTHOR: W. Michael Petullo
//   DATE: 11 September 1999
// Copyright (C) 1999 W. Michael Petullo new [at] flyn.org
// All rights reserved.
</pre>
</dl>
<p> on my computer. </p>
<p> The program understands plaintext or gziped template files. </p>
<p> The fmt-ptrn system also provides a shared library which allows a programmer access to nf&#8217;s functionality. The system was developed to be light and fast. Its only external dependencies are the C library, glib2 and zlib. </p>
<h2>NASTY DETAILS</h2>
<p> Nf first looks for templates in ~/.fmt-ptrn/templates. Second, nf looks for templates in &lt;datadir&gt;/fmt-ptrn/template, where datadir is defined by autoconf. This directory is usually /usr/local/share or /usr/share. </p>
<p> The templates directory contains several subdirectories matching filename extensions. This may include directories such as html, cpp, c, and tex. Within each subdirectory are the actual template files. The template file named default is the default template used for the filename extension. Other templates can be used by specifying their filename to nf on the command line (see <a href="/docs/linux/man/1-nf/">NF</a>(1)). </p>
<p> Certain types of files generally don&#8217;t have extensions. In this case, nf looks for a template directory with the same name as the file being created. This is useful when using templates to create files with names such as Makefile and README. </p>
<p> When filling a format pattern, nf knows the value for the following format patterns: </p>
<dl>
<dt>DATE</p>
<dd> Today&#8217;s date.</p>
<dt>FILE</p>
<dd> The name of the file being created.</p>
<dt>FULLNAME</p>
<dd> The user&#8217;s full name (from GECOS field).</p>
<dt>FIRSTNAME</p>
<dd> The user&#8217;s first name (from GECOS field).</p>
<dt>MIDDLENAME</p>
<dd> The user&#8217;s middle name (from GECOS field).</p>
<dt>LASTNAME</p>
<dd> The user&#8217;s last name (from GECOS field).</p>
<dt>EMPTY_STR</p>
<dd> The empty string.</dl>
<p> In addition, any environment variable can be used as a format pattern. An alternate string to be used in the case of an environment variable being undefined can be specified as follows: </p>
<p> %(UNDEFINED:foo) </p>
<p> This will be replaced with &#8220;foo&#8221; in the created file if UNDEFINED is not a part of one&#8217;s environment. </p>
<p> The alternative may be a format pattern, too. If FIRSTNAME is defined a Mike, the following: </p>
<p> %(UNDEFINED:%(before=&quot;My name is &quot; FIRSTNAME)) </p>
<p> will print &#8220;My name is Mike.&#8221; </p>
<p> A format pattern can also be acted on by a modifier. The following will print the value of FOO in capital letters: </p>
<p> %(upper FOO) </p>
<p> It makes sense to use some modifiers with a literal, instead of a key which will be replaced by a value. For example: </p>
<p> %(file FOO) </p>
<p> will insert the text contained in a the file whose path is the value of the key FOO. But: </p>
<p> %(file &quot;foo&quot;) </p>
<p> will insert the contents of the file named foo. </p>
<p> The following modifiers are currently available: </p>
<dl>
<dt>upper</p>
<dd> Convert to upper case.</p>
<dt>lower</p>
<dd> Convert to lower case.</p>
<dt>basename</p>
<dd> Convert to the basename of a filename.</p>
<dt>before=&quot;str&quot;</p>
<dd> Append the string str before.</p>
<dt>after=&quot;str&quot;</p>
<dd> Append the string str after.</p>
<dt>fn</p>
<dd> Tag a &quot; ()&quot; on the end.</p>
<dt>c_delim</p>
<dd> Print enveloped in a C style deliminator, ie: /* == foo == */.</p>
<dt>cpp_delim</p>
<dd> Print enveloped in a C++ style deliminator, ie: // == foo.</p>
<dt>sh_delim</p>
<dd> Print enveloped in a shell script style deliminator, ie: # == foo.</p>
<dt>tex_delim</p>
<dd> Print eveloped in a LaTeX style deliminator, ie: % == foo.</p>
<dt>newlines</p>
<dd> Replaces occurrences of &quot; &quot; in the string with new lines</p>
<dt>no_newlines</p>
<dd> Replaces occurrences of &quot; in the string with &#8216; &#8216;</p>
<dt>remove_underscore</p>
<dd> Replaces occurrences of &#8216;_&#8217; in the string with &#8216;-&#8216;</p>
<dt>file</p>
<dd> Treats the key as the path to a file, which is included</p>
<dt>template</p>
<dd> Treats the key as the path to a template, which is filled and included</p>
<dt>#</p>
<dd> A comment, this will not appear in destination file %(# Comment.)</dl>
<p> Several modifiers can act within one format string as illustrated: </p>
<p> %(basename upper FOO) </p>
<p> Modifiers use a stack to be applied. The first modifier to be applied is the one farthest to the right. The last to be applied it the one farthest to the left. </p>
<h2>AUTHORS</h2>
<p> W. Michael Petullo &lt;mike [at] flyn.org&gt;</p>
<h2>Index</h2>
