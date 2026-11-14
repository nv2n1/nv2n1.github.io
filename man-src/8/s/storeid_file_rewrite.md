---
title: "storeid_file_rewrite(8)"
name: "storeid_file_rewrite"
section: "8"
letter: "s"
url: "/docs/linux/man/8-storeid_file_rewrite/"
---

<pre> storeid_file_rewrite - File based Store-ID helper for Squid</pre>

<h2>Synopsis</h2>

<pre> storeid_file_rewrite filepath</pre>

<h2>Description</h2>

This program acts as a store_id helper program, rewriting URLs passed by Squid into storage-ids that can be used to achieve better caching for websites that use different URLs for the same content. 

 It takes a text file with two tab separated columns. Column 1: Regular expression to match against the <font SIZE="-1">URL</font> Column 2: Rewrite rule to generate a Store-ID Eg: ^http:\/\/[^\.]+\.dl\.sourceforge\.net\/(.*)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" HREF="http://dl.sourceforge.net.squid.internal/$1">http://dl.sourceforge.net.squid.internal/$1</a>
 

 Rewrite rules are matched in the same order as they appear in the rules file. So for best performance, sort it in order of frequency of occurrence. 

 This program will automatically detect the existence of a concurrecy channel-ID and adjust appropriately. It may be used with any value 0 or above for the store_id_children concurrency= parameter.

<h2>Options</h2>

The only command line parameter this helper takes is the regex rules file name.

<h2>Author</h2>

This program and documentation was written by <i>Alan Mizrahi &lt;alan [at] mizrahi.com.ve</i>&gt; 

 Based on prior work by <i>Eliezer Croitoru &lt;eliezer [at] ngtech.co.il</i>&gt;

<h2>Copyright</h2>

<pre> * Copyright (C) 1996-2016 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.
 Copyright (C) 2013 Alan Mizrahi &lt;alan [at] mizrahi.com.ve&gt;
 Based on code from Eliezer Croitoru &lt;eliezer [at] ngtech.co.il&gt;
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.</pre>

<h2>Questions</h2>

Questions on the usage of this program can be sent to the <i>Squid Users mailing list &lt;squid-users [at] squid-cache.org</i>&gt;

<h2>Reporting Bugs</h2>

Bug reports need to be made in English. See <a rel="nofollow" HREF="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. 

 Report bugs or bug fixes using <a rel="nofollow" HREF="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> 

 Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org</i>&gt; 

 Report ideas for new improvements to the <i>Squid Developers mailing list &lt;squid-dev [at] squid-cache.org</i>&gt;

<h2>See Also</h2>

squid (8), <font SIZE="-1">GPL \<a HREF="/docs/linux/man/7-fis0/">fIs0</a>(7), The Squid wiki <a rel="nofollow" HREF="http://wiki.squid-cache.org/Features/StoreID">http://wiki.squid-cache.org/Features/StoreID</a> The Squid Configuration Manual <a rel="nofollow" HREF="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> 
