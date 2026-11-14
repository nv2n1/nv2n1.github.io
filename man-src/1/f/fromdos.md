---
title: "fromdos(1)"
name: "fromdos"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fromdos/"
description: "tofrodos – Converts text files between DOS and Unix formats."
---

<h2>NAME</h2>
<p> tofrodos &#8211; Converts text files between DOS and Unix formats.</p>
<h2>SYNOPSIS</h2>
<p> <code>fromdos</code> [ <i>options</i> ] [file&#8230;]<br />
 <code>todos</code> [ <i>options</i> ] [file&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> DOS text files traditionally have carriage return and line feed pairs as their newline characters while Unix text files have the line feed as their newline character. <i>fromdos</i> converts ASCII and Unicode UTF-8 text files from the DOS format to the Unix format, while <i>todos</i> converts them from the Unix format to the DOS format. </p>
<p> The programs accept multiple filenames and wildcards as their arguments. You may also use them in a pipe. If either program finds its input redirected, it will process stdin and place the output on stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> This option is deprecated. Do not use it unless you know what you&#8217;re doing. By default, Tofrodos does the expected thing for text files. That is, when converting from DOS to Unix, it will remove carriage returns only if they are followed by line feeds. When converting from Unix to DOS, it will add carriage returns only if the linefeeds are not already preceeded by carriage returns. When Tofrodos is run on a normal text file that has already been converted, the resulting file should be identical to the original. However, if you use this option, the program will always remove carriage returns in the DOS to Unix mode and always add carriage returns in the Unix to DOS mode even if it is not appropriate.</p>
<dt><code>-b</code></p>
<dd> Make a backup of original file. The original file with a <i>.bak</i> extension appended to the original filename, silently replacing any existing file of that name. For example, a file called &quot;filename.ext&quot; becomes &quot;filename.ext.bak&quot; replacing any existing file having the name &quot;filename.ext.bak&quot;. Important: the program behaves differently if it is compiled for DOS (as compared to being compiled for Windows, Linux, Mac OS X or other systems). In view of the filename restrictions present on DOS, the DOS executable will strip the original file extension, if any, from the file before appending the <i>.bak</i> extension. For example, &quot;filename.ext&quot; becomes &quot;filename.bak&quot;.</p>
<dt><code>-d</code></p>
<dd> Convert from DOS to Unix. This forces the program to convert the file in a particular direction. By default, if the program is named <i>fromdos</i> or <i>dos2unix,</i> it will assume that the input file is in a DOS format and convert it to a Unix format. If the program is named <i>todos</i> or <i>unix2dos,</i> it will assume that the input file is in a Unix format and convert it to a DOS format. Using the <i>-d</i> option forces the program to convert from a DOS format to a Unix format regardless of how the program is named. Likewise, using the <i>-u</i> option forces the program to convert from a Unix format to a DOS format regardless of the name of the program.</p>
<dt><code>-e</code></p>
<dd> Abort processing on any error in any file. Normally, the program will simply skip to process the next file on the command line when it encounters any errors. This option causes it to abort on errors.</p>
<dt><code>-f</code></p>
<dd> Force: convert even if the file is not writeable (read-only). By default, if the program finds that the file does not have write permission, it will not process that file. This option forces the conversion even if the file is read-only.</p>
<dt><code>-h</code></p>
<dd> Display a short help screen on the program usage and quit.</p>
<dt><code>-l</code><i>&lt;logfile&gt;</i></p>
<dd> Log error messages to &lt;logfile&gt;. Note that if your command line has an error, such as when you specify an unknown option, the error message for the command line option error will be issued to stderr instead and not logged.</p>
<dt><code>-o</code></p>
<dd> Overwrite the original file (no backup). This is the default.</p>
<dt><code>-p</code></p>
<dd> Preserve file ownership and time on Unix-type systems (like Linux). On Windows and MSDOS, it only preserves the file time. Note that on many Unix-type systems, including Linux, the file ownership will only be preserved if the program is run as root, otherwise it will just set the file time and silently fail the change of file ownership. On such systems, if you want a warning message when the file ownership cannot be changed, use -v (the verbose flag) as well.</p>
<dt><code>-u</code></p>
<dd> Convert from Unix to DOS. See the <i>-d</i> option above for more information.</p>
<dt><code>-v</code></p>
<dd> Verbose.</p>
<dt><code>-V</code></p>
<dd> Show version message and quit.</dl>
<h2>EXIT CODE</h2>
<p> Tofrodos terminates with an exit code of 0 on success and 1 on error. </p>
<p> If the program is invoked with multiple files on the command line, the default behaviour is to skip to the next file in the list if an error is encountered with any file. In such a case, the exit code returned will the status of the last file processed (ie, 0 on success, 1 on failure). If this is not desirable, use the -e option, which will force the program to abort immediately with the appropriate exit code on encountering any error.</p>
<h2>AUTHOR</h2>
<p> The program and its documentation are copyrighted (c) 1996-2013 by Christopher Heng. All rights reserved. They are distributed under the terms of the GNU General Public License Version 2. </p>
<p> The latest version of tofrodos can be obtained from<br />
 <a rel="nofollow" href="http://www.thefreecountry.com/tofrodos/index.shtml">http://www.thefreecountry.com/tofrodos/index.shtml</a> </p>
<h2>Index</h2>
