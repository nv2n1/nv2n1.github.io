---
title: "xmltvsupplement(3)"
name: "xmltvsupplement"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmltvsupplement/"
---

XMLTV::Supplement - Supplementary file loader for XMLTV grabbers 

<h2>Description</h2>Utility library that loads supplementary files for xmltv-grabbers and other programs in the xmltv-distribution. 

 Supplementary files can be loaded either via http or from a local file, depending on the configuration of the module. The default is to load the files from <a rel="nofollow" HREF="http://supplement.xmltv.org.">http://supplement.xmltv.org.</a> This can be changed by setting the environment variable XMLTV_SUPPLEMENT to the new root-directory or root-url for supplementary files.
<h2>Exported Functions</h2>All these functions are exported on demand.
<dl COMPACT><dt>GetSupplement
</dt><dd>Load a supplement file and return it as a string. Takes two parameters: directory and filename. 
 <pre> my $content = GetSupplement( 'tv_grab_uk_rt', 'channel_ids' );</pre>GetSupplement will always return a string with the content. If it fails to get the content, it prints an error-message and aborts the program.
</dd><dt>GetSupplementLines
</dt><dd>Load a supplement file and return it as an array. Any comments or blank lines will be removed. Takes two parameters: directory and filename. 
 <pre> my $content = GetSupplementLines( 'tv_grab_uk_rt', 'channel_ids' );</pre>GetSupplementLines will always return an array with the content. If it fails to get the content, it prints an error-message and aborts the program.
</dd><dt>GetSupplementFile
</dt><dd>Get the supplement file from the local machine
</dd><dt>GetSupplementUrl
</dt><dd>Get the supplement file from a URL
</dd><dt>GetSupplementDir
</dt><dd>Get the base directory containing supplementary files. 
e.g.&nbsp;<wbr><tt>$ENV</tt>{HOME}/.xmltv/supplement
</dd><dt>SetSupplementRoot
</dt><dd>Set the root directory for loading supplementary files. 
 <pre> SetSupplementRoot( '/usr/share/xmltv' );
 SetSupplementRoot( '<a rel="nofollow" HREF="http://my.server.org/xmltv'">http://my.server.org/xmltv'</a> );</pre></dd><dt>GetSupplementRoot
</dt><dd>Get the root directory for loading supplementary files.</dd></dl><h2>Caching</h2>The module stores all downloaded files in a cache. The cache is stored on disk in ~/.xmltv/supplement on Unix and in CSIDL_LOCAL_APPDATA//xmltv/supplement on Windows. 

 If a file has been downloaded less than 1 hour ago, the file from the cache is used without contacting the server. Otherwise, if the file has been downloaded more than 1 hour ago, then the module checks with the server to see if an updated file is available and downloads it if necessary. 

 If the server does not respond or returns an error-message, a warning is printed to STDERR and the file from the cache is used.
<h2>Environment Variables</h2>The XMLTV_SUPPLEMENT environment variable can be used to tell the module where the supplementary files are found. 

 <pre> XMLTV_SUPPLEMENT=/usr/share/xmltv
 XMLTV_SUPPLEMENT=<a rel="nofollow" HREF="http://supplementary.xmltv.se">http://supplementary.xmltv.se</a></pre>The XMLTV_SUPPLEMENT_VERBOSE environment variable can be used to get more debug output from XMLTV::Supplement. 

 <pre> XMLTV_SUPPLEMENT_VERBOSE=1</pre><h2>Copyright</h2>Copyright (C) 2007 Mattias Holmlund. 

 This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 

 You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
