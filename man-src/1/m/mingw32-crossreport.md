---

title: "mingw32-crossreport(1)"
name: "mingw32-crossreport"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mingw32-crossreport/"
---

CrossReport - Analysis tool to help cross-compilation to Windows. 

<h2>SYNOPSIS</h2>

 <pre>
 mingw32-crossreport [options] /path/to/linuxbinary
</pre>

<h2>DESCRIPTION</h2>

 CrossReport is a tool to help you analyze the APIs used by a compiled Linux program, in order to work out the effort required to cross-compile that program for Windows, using the Fedora MinGW cross-compiler. 

 The simplest way to use it is to point it at an existing Linux binary, and then read the generated report. 

 What it does in more detail: It looks at the libraries and API calls used by the Linux binary, and compares them to the libraries and API calls that we currently support under the Fedora MinGW cross-compiler. It then works out what is missing, and produces a report suggesting the amount of work that needs to be done to port the program. For example, whether whole libraries need to be ported first, and/or how to substitute individual calls to work on Windows.

<h2>EXAMPLE</h2>

 Assuming that the excellent vector graphics editor Inkscape (&lt;<a rel="nofollow" HREF="http://www.inkscape.org/">http://www.inkscape.org/</a>&gt;) is installed, you could do: 

 <pre>
 mingw32-crossreport /usr/bin/inkscape &gt; inkscape-report.txt
 less inkscape-report.txt
</pre>

<h2>SHORTCOMINGS</h2>

 The report is only a general guide. CrossReport contains a lot of knowledge about common Linux calls and APIs, but does not know about every possible library.

<h2>DATABASE</h2>

 The program relies on a database of MinGW APIs. The default location for this database is <tt>&quot;/usr/share/crossreport/crossreport.db&quot;</tt> or the same file in the current working directory. If the database cannot be found in either location, the program will fail with an error message. 

 The database is updated regularly and distributed with CrossReport. To get the best quality report, make sure you are running a recent version of the program.

<h2>COPYRIGHT</h2>

 Copyright (C) 2009 Red Hat Inc. Written by Richard W.M. Jones &lt;rjones [at] redhat.com&gt;. 

 This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

 You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
