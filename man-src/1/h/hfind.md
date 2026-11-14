---
title: "hfind(1)"
name: "hfind"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hfind/"
description: "hfind – Lookup a hash value in a hash database"
---

<h2 class="name">NAME</h2>
<p> hfind &#8211; Lookup a hash value in a hash database </p>
<h2>SYNOPSIS</h2>
<p> <code>hfind [-i</code> <i>db_type</i> <code>] [-f</code> <i>lookup_file</i> <code>] [-eq] </code> <i>db_file [hashes]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>hfind</code> looks up hash values in a database using a binary search algorithm. This allows one to easily create a hash database and identify if a file is known or not. It works with the NIST National Software Reference Library (NSRL) and the output of &#8216;md5sum&#8217;. </p>
<p> Before the database can be used by &#8216;hfind&#8217;, an index file must be created with the &#8216;-i&#8217; option. </p>
<p> This tool is needed for efficiency. Most text-based databases do not have fixed length entries and are sometimes not sorted. The hfind tool will create an index file that is sorted and has fixed-length entries. This allows for fast lookups using a binary search algorithm instead of a linear search such as &#8216;grep&#8217;. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-i db_type</p>
<dd> Create an index file for the database. This step must be done before a lookup can be performed. The &#8216;db_type&#8217; argument specifies the database type (i.e. nsrl-md5 or md5sum). See section below.</p>
<dt>-f lookup_file</p>
<dd> Specify the location of a file that contains one hash value per line. These hashes will be looked up in the database.</p>
<dt>-e</p>
<dd> Extended mode. Additional information besides just the name is printed. (Does not apply for all hash database types).</p>
<dt>-q</p>
<dd> Quick mode. Instead of displaying the corresponding information with the hash, just display 0 if the hash was not found and 1 if it was. If this flag is used, then only one hash can be given at a time.</p>
<dt>-V</p>
<dd> Display version</p>
<dt>db_file</p>
<dd> The location of the hash database file.</p>
<dt>[hashes]</p>
<dd> The hashes to lookup. If they are not supplied on the command line, STDIN is used. If index files exist for both SHA-1 and MD5 hashes, then both types of hashes can be given at runtime. </p>
</dl>
<h2>INDEX FILE</h2>
<p> <code>hfind </code> uses an index file to perform a binary search for a hash value. This is much faster than using &#8216;grep&#8217;, which will do a linear search. Before a hash database is used, a corresponding index file must be created. This is done with the &#8216;-i&#8217; option to hfind. </p>
<p> The resulting index file will be named based on the database file name. The name will have the original name following by the hash type (sha1 or md5) followed by &#8216;.idx&#8217;. For example, creating an MD5 hash index of the NIST NSRL results in &#8216;NSRLFile.txt-md5.idx&#8217; and the SHA-1 index results in &#8216;NSRLFile.txt-sha1.idx&#8217;. </p>
<p> The file has two columns. Each entry is sorted by the first column, which is the hash value. The second column has the byte offset of the corresponding entry in the original file. So, when a hash is found in the index, the offset is recorded and then &#8216;hfind&#8217; seeks to the entry in the original database. </p>
<p> The following input types are valid. For NSRL, &#8216;nsrl-md5&#8217; and &#8216;nsrl-sha1&#8217; can be used. The difference is which hash value the index is sorted by. The &#8216;md5sum&#8217; value can also be used to sort and index &quot;home made&quot; databases. &#8216;hfind&#8217; can take data in both common formats: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MD5&nbsp;(test.txt)&nbsp;=&nbsp;76b1f4de1522c20b67acc132937cf82e </p>
<p> and </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;76b1f4de1522c20b67acc132937cf82e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;test.txt </p>
<h2>EXAMPLES</h2>
<p> To create an MD5 index file for NIST NSRL: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;hfind -i nsrl-md5&nbsp;/usr/local/hash/nsrl/NSRLFile.txt </p>
<p> To lookup a value in the NSRL: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;hfind&nbsp;/usr/local/hash/nsrl/NSRLFile.txt 76b1f4de1522c20b67acc132937cf82e </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;76b1f4de1522c20b67acc132937cf82e&nbsp;<wbr>&nbsp;Hash Not Found </p>
<p> You can even do both SHA-1 and MD5 if you want: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;hfind -i nsrl-sha1&nbsp;/usr/local/hash/nsrl/NSRLFile.txt </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;hfind&nbsp;/usr/local/hash/nsrl/NSRLFile.txt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;76b1f4de1522c20b67acc132937cf82e<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;80001A80B3F1B80076B297CEE8805AAA04E1B5BA </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;76b1f4de1522c20b67acc132937cf82e&nbsp;<wbr>&nbsp;Hash Not Found </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;80001A80B3F1B80076B297CEE8805AAA04E1B5BA&nbsp;<wbr>&nbsp;thrdcore.cpp </p>
<p> To make a database of critical binaries of a trusted system, use &#8216;md5sum&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;md5sum&nbsp;/bin/*&nbsp;/sbin/*&nbsp;/usr/bin/*&nbsp;/usr/bin/*&nbsp;/usr/local/bin/*&nbsp;/usr/local/sbin/*&nbsp;&gt;&nbsp;system.md5 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;hfind -i md5sum system.md5 </p>
<p> To look entries up, the following will work: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;hfind system.md5 76b1f4de1522c20b67acc132937cf82e </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;76b1f4de1522c20b67acc132937cf82e&nbsp;<wbr>&nbsp;Hash Not Found </p>
<p> or </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;md5sum -q&nbsp;/bin/*&nbsp;| hfind system.md5 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;928682269cd3edb1acdf9a7f7e606ff2&nbsp;<wbr>&nbsp;/bin/bash </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&#8230;&gt; </p>
<p> or </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;md5sum -q&nbsp;/bin/*&nbsp;&gt;&nbsp;bin.md5 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;hfind -f bin.md5 system.md5 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;928682269cd3edb1acdf9a7f7e606ff2&nbsp;<wbr>&nbsp;/bin/bash </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&#8230;&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sorter/">sorter</a></code>(1) </p>
<p> The NIST National Software Reference Library (NSRL) can be found at <a rel="nofollow" href="http://www.nsrl.nist.gov">www.nsrl.nist.gov</a>. </p>
<h2>LICENSE</h2>
<p> Distributed under the Common Public License, found in the <i>cpl1.0.txt</i> file in the The Sleuth Kit licenses directory. </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
