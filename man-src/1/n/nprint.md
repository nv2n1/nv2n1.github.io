---
title: "nprint(1)"
name: "nprint"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nprint/"
description: "nprint – NetWare print client"
---

<h2>NAME</h2>
<p> nprint &#8211; NetWare print client</p>
<h2>SYNOPSIS</h2>
<p> <code>nprint</code> [ <code>-S</code> <i>server</i> ] [ <code>-h</code> ] [ <code>-U</code> <i>username</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-q</code> <i>queuename</i> ] [ <code>-d</code> <i>job-description</i> ] [ <code>-p</code> <i>pathname-in-banner</i> ] [ <code>-B</code> <i>username-in-banner</i> ] [ <code>-s</code> ] [ <code>-f</code> <i>filename-in-banner</i> ] [ <code>-l</code> <i>lines</i> ] [ <code>-r</code> <i>rows</i> ] [ <code>-c</code> <i>copies</i> ] [ <code>-t</code> <i>tab size</i> ] [ <code>-T</code> ] [ <code>-N</code> ] [ <code>-F</code> <i>form-number</i> ] <i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> With <code>nprint</code>, you can print files on print queues of a NetWare file server. </p>
<p> There are a lot of options, so you should probably wrap some default configurations into some shell scripts. </p>
<p> <code>nprint</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of <code>.nwclient</code> MUST be 600, for security reasons. </p>
<h2>OPTIONS</h2>
<p> <code>filename</code></p>
<dl>
<dt>
<dd> <i>filename</i> is the name of the file you want to print. If file is &#8216;<code>&#8211;</code>&#8216;, or no filename is given, standard input is used.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> <code>-h</code> is used to print out a short help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> <i>server</i> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>username</i></p>
<dl>
<dt>
<dd> <i>username</i> is the user name to use for the print request at the server.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dt>
<dd> <i>password</i> is the password to use for the print request at the server. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, <code>nprint</code> prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given if no password is required for the print request.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C</code>.</dl>
<p> <code>-q</code> <i>queuename</i></p>
<dl>
<dt>
<dd> <i>queuename</i> is the name of the print queue to use at the print server. At present, you must specify it in upper case characters.</dl>
<p> <code>-d</code> <i>job-description</i></p>
<dl>
<dt>
<dd> <i>job-description</i> is the string that appears in pconsole when you list the jobs for the print queue. It will also appear in the &quot;Description&quot; field on the banner page.</dl>
<p> <code>-p</code> <i>pathname-in-banner</i></p>
<dl>
<dt>
<dd> <i>pathname-in-banner</i> is the string (up to 79 characters) you want to be printed in the &quot;Directory&quot; field on the banner page.</dl>
<p> <code>-B</code> <i>username-in-banner</i></p>
<dl>
<dt>
<dd> <i>username-in-banner</i> is the string (up to 12 characters) you want to appear on the lower part of the banner page. It will also appear in the &quot;User name&quot; field.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Supress printing of banner page</dl>
<p> <code>-f</code> <i>filename-in-banner</i></p>
<dl>
<dt>
<dd> <i>filename-in-banner</i> is the string (up to 12 characters) you want to appear in large letters on the lower part of the banner page. Default: the name of the file that is printed, or &#8216;<code>stdin</code>&#8216;.</dl>
<p> <code>-l</code> <i>lines</i></p>
<dl>
<dt>
<dd> <i>lines</i> is the number of lines to put on one page. Default: 66.</dl>
<p> <code>-r</code> <i>rows</i></p>
<dl>
<dt>
<dd> <i>rows</i> is the number of rows to put on one page. Default: 80.</dl>
<p> <code>-c</code> <i>copies</i></p>
<dl>
<dt>
<dd> <i>copies</i> tells the print server to the specified number of copies. Default: 1.</dl>
<p> <code>-t</code> <i>tabs</i></p>
<dl>
<dt>
<dd> <i>tabs</i> is the number of spaces to print for a Tab-Character. Default: 8.</dl>
<p> <code>-T</code></p>
<dl>
<dt>
<dd> tells the print server to expand Tab-Character and use 8 spaces</dl>
<p> <code>-N</code></p>
<dl>
<dt>
<dd> tells the print server <code>not</code> to use Form Feeds</dl>
<p> <code>-F</code> <i>form-number</i></p>
<dl>
<dt>
<dd> <i>form-number</i> is the the number of the form to be put into the printer. If it&#8217;s different from the one currently in the printer, your job is only printed if a printer operator has put in the correct form.</dl>
<h2>NOTES</h2>
<p> The &#8216;<code>-B</code>&#8216; option was formerly &#8216;<code>-b</code>&#8216;. But it conflicted with &#8216;<i>bindery only</i>&#8216; login option. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/1-pqlist/">pqlist</a>(1), <a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8)</code> </p>
<h2>CREDITS</h2>
<p> nprint was written by Volker Lendecke (lendecke [at] math.uni-goettingen.de) </p>
<h2>Index</h2>
