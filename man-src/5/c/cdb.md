---
title: "cdb(5)"
name: "cdb"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cdb/"
description: "cdb – Constant DataBase file format"
---

<p>cdb &#8211; Constant DataBase file format</p>
<h2>Description</h2>
<p>A <code>cdb</code> database is a single file used to map `keys&#8217; to `values&#8217;, having records of (key,value) pairs. File consists of 3 parts: toc (table of contents), data and index (hash tables). Toc has fixed length of 2048 bytes, containing 256 pointers to hash tables inside index sections. Every pointer consists of position of a hash table in bytes from the beginning of a file, and a size of a hash table in entries, both are 4-bytes (32 bits) unsigned integers in little-endian form. Hash table length may have zero length, meaning that corresponding hash table is empty. Right after toc section, data section follows without any alingment. It consists of series of records, each is a key length, value (data) length, key and value. Again, key and value length are 4-byte unsigned integers. Each next record follows previous without any special alignment. After data section, index (hash tables) section follows. It should be looked to in conjunction with toc section, where each of max 256 hash tables are defined. Index section consists of series of hash tables, with starting position and length defined in toc section. Every hash table is a sequence of records each holds two numbers: key&#8217;s hash value and record position inside data section (bytes from the beginning of a file to first byte of key length starting data record). If record position is zero, then this is an empty hash table slot, pointed to nowhere. CDB hash function is </p>
<pre> hv = ((hv &lt;&lt; 5) + hv) ^ <i>c</i></pre>
<p>for every single <i>c</i> byte of a key, starting with hv = <i>5381</i>. Toc section indexed by (hv % 256), i.e. hash value modulo 256 (number of entries in toc section). In order to find a record, one should: first, compute the hash value (hv) of a key. Second, look to hash table number hv modulo 256. If it is empty, then there is no such key exists. If it is not empty, then third, loop by slots inside that hash table, starting from slot with number hv divided by 256 modulo length of that table, or ((hv / 256) % htlen), searching for this hv in hash table. Stop search on empty slot (if record position is zero) or when all slots was probed (note cyclic search, jumping from end to beginning of a table). When hash value in question is found in hash table, look to key of corresponding record, comparing it with key in question. If them of the same length and equals to each other, then record is found, overwise, repeat with next hash table slot. Note that there may be several records with the same key. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cdb/">cdb</a>(1), <a href="/docs/linux/man/3-cdb/">cdb</a>(3). </p>
<h2>Author</h2>
<p>The <code>tinycdb</code> package written by Michael Tokarev &lt;mjt [at] corpit.ru&gt;, based on ideas and shares file format with original cdb library by Dan Bernstein.</p>
<h2>License</h2>
<p>Public domain.</p>
