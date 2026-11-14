---
title: "lwp-rget(1)"
name: "lwp-rget"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lwp-rget/"
---

<h2 class="name">NAME</h2>
 

 lwp-rget - Retrieve web documents recursively 

<h2>SYNOPSIS</h2>

 <pre><code>
lwp - rget[--verbose] [--auth = USER:PASS][--depth = N][--hier][--iis][--keepext = mime / type[, mime / type]][--limit = N][--nospace][--prefix = URL][--referer = URL][--sleep = N][--tolower]&lt;URL&gt; lwp - rget-- version
</code></pre>

<h2>DESCRIPTION</h2>

 This program will retrieve a document and store it in a local file. It will follow any links found in the document and store these documents as well, patching links so that they refer to these local copies. This process continues until there are no more unvisited links or the process is stopped by the one or more of the limits which can be controlled by the command line arguments. 

 This program is useful if you want to make a local copy of a collection of documents or want to do web reading off-line. 

 All documents are stored as plain files in the current directory. The file names chosen are derived from the last component of <font SIZE="-1">URL</font> paths. 

 The options are:
<dl>
<dt>--auth=USER:PASn
<dd> Set the authentication credentials to user ``<font SIZE="-1">USER</font>'' and password ``<font SIZE="-1">PASS</font>'' if any restricted parts of the web site are hit. If there are restricted parts of the web site and authentication credentials are not available, those pages will not be downloaded.
<dt>--depth=<i>n</i>
<dd> Limit the recursive level. Embedded images are always loaded, even if they fall outside the <i>--depth</i>. This means that one can use <i>--depth=0</i> in order to fetch a single document together with all inline graphics. 

 The default depth is 5.
<dt>--hier
<dd> Download files into a hierarchy that mimics the web site structure. The default is to put all files in the current directory.
<dt>--referer=<i></i><font SIZE="-1"><i>URI</i></font><i></i>
<dd> Set the value of the Referer header for the initial request. The special value <tt>&quot;NONE&quot;</tt> can be used to suppress the Referer header in any of subsequent requests. The Referer header will always be suppressed in all normal <tt>&quot;http&quot;</tt> requests if the referring page was transmitted over <tt>&quot;https&quot;</tt> as recommended in <font SIZE="-1">RFC</font> 2616.
<dt>--iis
<dd> Sends an ``Accept: */*'' on all <font SIZE="-1">URL</font> requests as a workaround for a bug in <font SIZE="-1">IIS</font> 2.0. If no Accept <font SIZE="-1">MIME</font> header is present, <font SIZE="-1">IIS</font> 2.0 returns with a ``406 No acceptable objects were found'' error. Also converts any back slashes (\\) in URLs to forward slashes (/).
<dt>--keepext=<i>mime/type[,mime/type]</i>
<dd> Keeps the current extension for the list <font SIZE="-1">MIME</font> types. Useful when downloading text/plain documents that shouldn't all be translated to *.txt files.
<dt>--limit=<i>n</i>
<dd> Limit the number of documents to get. The default limit is 50.
<dt>--nospace
<dd> Changes spaces in all URLs to underscore characters (_). Useful when downloading files from sites serving URLs with spaces in them.<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Does not
 remove spaces from fragments, e.g., ``file.html#somewhere in here''.
<dt>--prefix=<i>url_prefix</i>
<dd> Limit the links to follow. Only URLs that start the prefix string are followed. 

 The default prefix is set as the ``directory'' of the initial <font SIZE="-1">URL</font> to follow.<tt>&nbsp;<wbr></tt> For instance if we start lwp-rget with the <font SIZE="-1">URL</font>
 <tt>&quot;<a rel="nofollow" HREF="http://www.sn.no/foo/bar.html">http://www.sn.no/foo/bar.html</a>&quot;</tt>, then prefix will be set to <tt>&quot;<a rel="nofollow" HREF="http://www.sn.no/foo/">http://www.sn.no/foo/</a>&quot;</tt>. 

 Use <tt>&quot;--prefix=''&quot;</tt> if you don't want the fetching to be limited by any prefix.
<dt>--sleep=<i>n</i>
<dd> Sleep <i>n</i> seconds before retrieving each document. This options allows you to go slowly, not loading the server you visiting too much.
<dt>--tolower
<dd> Translates all links to lowercase. Useful when downloading files from <font SIZE="-1">IIS</font> since it does not serve files in a case sensitive manner.
<dt>--verbose
<dd> Make more noise while running.
<dt>--quiet
<dd> Don't make any noise.
<dt>--version
<dd> Print program version number and quit.
<dt>--help
<dd> Print the usage message and quit.</dl>
 

 Before the program exits the name of the file, where the initial <font SIZE="-1">URL</font> is stored, is printed on stdout. All used filenames are also printed on stderr as they are loaded. This printing can be suppressed with the <i>--quiet</i> option.

<h2>SEE ALSO</h2>

 lwp-request, <font SIZE="-1">LWP</font>

<h2>AUTHOR</h2>

 Gisle Aas &lt;aas [at] sn.no&gt; 

<h2>Index</h2>


