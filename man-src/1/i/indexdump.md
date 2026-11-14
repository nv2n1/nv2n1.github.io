---
title: "indexdump(1)"
name: "indexdump"
section: "1"
letter: "i"
url: "/docs/linux/man/1-indexdump/"
---

<h2 class="name">NAME</h2>
 

 indexdump - Show the content of the index file 

<h2>FORMAT</h2>

 <pre><code>
indexdump[options] file[tag]
</code></pre> 

 where options are 

 <pre><code>
--debug output record separator(default newline)-- type specifies the num / date / char type of the index-- start defines the value to start dump from-- n prints also the total number of records in the file
</code></pre>

<h2>SYNOPSIS</h2>

 <pre>
        indexdump rooms.cdx FACILITY
        indexdump --debug=14 --start=Dub rooms.cdx ROOMNAME
</pre>

<h2>DESCRIPTION</h2>

 Indexdump prints to standard output the content of the index file. The type of the index is one of those supported by the XBase::Index Perl module (cdx, idx, ntx, ndx, mdx). 

 The output contains the index key and the value, which is the record number in the correcponding dbf file. 

 For mulitag index files (like cdx), you need to specify the tag name to get the actual data.

<h2>AVAILABLE FROM</h2>

 <a rel="nofollow" HREF="http://www.adelton.com/perl/DBD-XBase/">http://www.adelton.com/perl/DBD-XBase/</a>

<h2>AUTHOR</h2>

 (c) 1999--2011 Jan Pazdziora.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-perl/">perl</a></i>(1); <i><a HREF="/docs/linux/man/3-xbase--index/">XBase::Index</a></i>(3) 

<h2>Index</h2>


