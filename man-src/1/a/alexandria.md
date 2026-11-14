---
title: "alexandria(1)"
name: "alexandria"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alexandria/"
description: "alexandria – a book collection manager"
---

<h2>NAME</h2>
<p> alexandria &#8211; a book collection manager </p>
<h2>SYNOPSIS</h2>
<p> <code>alexandria</code> <i>[OPTIONS]</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>Alexandria</i> is a GNOME desktop application for managing book collections. It has a simple user interface which makes it easy to enter the details of your library, generally using Internet sources to find catalogue information for your books. It also enables you to create filtered views of your book collection based on details such as author, publisher etc. </p>
<p> When launched without any options the <i>Alexandria</i> main window opens and presents a view of your libraries, or if run for the first time creates a new library ready for you to add books either manually or with the help of providers of book information on the Internet. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;debug</code><br />
&nbsp;<wbr>Print verbose debug information describing the operation of the<br />
&nbsp;<wbr>program. Useful for determining behaviour when a problem is<br />
&nbsp;<wbr>encountered. This also sets the logger level to DEBUG. </p>
<p> <code>&#8211;version</code><br />
&nbsp;<wbr>Show program version information and exit. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>Show summary of options and exit. This also shows a great many<br />
&nbsp;<wbr>predefined options common to all GTK programs which are not<br />
&nbsp;<wbr>defined in this manual page. </p>
<h2>FILES</h2>
<p> <code>$HOME/.alexandria</code><br />
&nbsp;<wbr>The per-user configuration of&nbsp;<wbr> <i>Alexandria </i><br />
&nbsp;<wbr>is stored in this directory. Each the books in each library are<br />
&nbsp;<wbr>stored in a sub-directory with the library&#8217;s name e.g.&nbsp;<wbr>`My<br />
&nbsp;<wbr>Library&#8217;. Book files are stored in YAML format&nbsp;<wbr>(a text-based data<br />
&nbsp;<wbr>format). They are named after the book&#8217;s ISBN<br />
&nbsp;<wbr>e.g. 9780755322800.yaml The cover images are also named after with<br />
&nbsp;<wbr>book&#8217;s ISBN, with the file extension .cover, although they are<br />
&nbsp;<wbr>usually JPEG format files. If a book has no ISBN, it&#8217;s ID will be<br />
&nbsp;<wbr>a number generated from the book title. </p>
<p> <code>$HOME/.alexandria/.smart_libraries</code><br />
&nbsp;<wbr>Smart Libraries are a filtered view of your book collection, and<br />
&nbsp;<wbr>are saved as YAML format files in this directory. </p>
<h2>ENVIRONMENT</h2>
<p> <code>LOGLEVEL</code><br />
&nbsp;<wbr>Setting this environment variable affects the level at which<br />
&nbsp;<wbr>messages will be logged. The log levels are cumulative, setting<br />
&nbsp;<wbr>the level to log information messages means it will also include<br />
&nbsp;<wbr>all warnings and error messages. Possible values are:</p>
<dl>
<dt>
<dd>
<p> <code>FATAL</code> Only log messages for fatal errors. </p>
<p> <code>ERROR</code> Log messages for all errors. </p>
<p> <code>WARN</code> Log warnings and errors. </p>
<p> <code>INFO</code> Also include information messages. </p>
<p> <code>DEBUG</code> Log everything, including debug messages.</dl>
<p>&nbsp;<wbr>The default level is&nbsp;<wbr> <code>WARN</code> </p>
<h2>BUGS</h2>
<p> Please report any bugs you find on the <a rel="nofollow" href="http://rubyforge.org/tracker/?group_id=205">http://rubyforge.org/tracker/?group_id=205</a> laURL: L raTracker Please check for any similar reports before reporting a new bug. </p>
<p> You can also discuss any problems you encounter with the <i>Alexandria</i> developers and other users by joining the <a rel="nofollow" href="http://rubyforge.org/mailman/listinfo/alexandria-list">http://rubyforge.org/mailman/listinfo/alexandria-list</a> laURL: L raalexandria-list </p>
<h2>WEB SITE</h2>
<p> News, details of the development team and further documentation may be found on the <a rel="nofollow" href="http://alexandria.rubyforge.org/">http://alexandria.rubyforge.org/</a> laURL: L raAlexandria web site </p>
<h2>AUTHOR</h2>
<p> Alexandria was originally written by Laurent Sansonetti. The current maintainer is Joseph Method &lt;tristil [at] gmail.com&gt;. For a full list of contributors, see the file AUTHORS in Alexandria&#8217;s documentation. </p>
<p> This manual page was written by Cathal Mc Ginley &lt;cathal.alexandria [at] gnostai.org&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2004-2006 Laurent Sansonetti </p>
<p> Copyright (C) 2007-2010 Alexandria Contributors </p>
<h2>LICENSE</h2>
<p> <i>Alexandria</i> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
