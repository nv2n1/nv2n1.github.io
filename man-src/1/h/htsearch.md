---
title: "htsearch(1)"
name: "htsearch"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htsearch/"
description: "htsearch – create document index and word database for the ht://Dig search engine"
---

<h2 class="name">NAME</h2>
<p> htsearch &#8211; create document index and word database for the ht://Dig search engine </p>
<h2>SYNOPSIS</h2>
<p> <code>htsearch</code> <i>[options] [query_string]</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Htsearch</i> is used to search in de databases created by <i>htdig</i> for content. is the actual search engine of the <i>htdig</i> search system. It is a CGI program that is expected to be invoked by an HTML form. It will accept both the GET and POST methods of passing data to the CGI program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>query_string</code></p>
<dd> A CGI-style query string can be given as a single argument, and is only used if the REQUEST_METHOD environment variable is not set. If no query_string is given, and REQUEST_METHOD is not set, htsearch will prompt for the query.</p>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the specified <i>configfile</i> instead of the default (for security reasons this option is only available when htsearch is used on the commandline).</p>
<dt><code>-v -d</code></p>
<dd> Run in verbose mode. This increases the verbosity of the program. Using more than 2 is probably only useful for debugging purposes. The default verbose mode gives a progress on what it is doing and where it is.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file.</p>
<dt><code>/var/www/html/htdig/header.html</code></p>
<dd> The default search results header file</p>
<dt><code>/var/www/html/htdig/footer.html</code></p>
<dd> The default search results footer file</p>
<dt><code>/var/www/html/htdig/wrapper.html</code></p>
<dd> The default search results wrapper file, that contains the header and footer together in one file</p>
<dt><code>/var/www/html/htdig/nomatch.html</code></p>
<dd> The default &#8216;no matches found&#8217; HTML file</p>
<dt><code>/var/www/html/htdig/syntax.html</code></p>
<dd> The default file that explains boolean expression syntax errors</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/1-htdig/">htdig</a>(1)</i> and <i><a href="/docs/linux/man/1-htmerge/">htmerge</a>(1)</i> for a detailed description of ht://Dig and its commands.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Stijn de Bekker, based on the HTML documentation of ht://Dig. </p>
<h2>Index</h2>
