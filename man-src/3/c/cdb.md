---
title: "cdb(3)"
name: "cdb"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdb/"
description: "cdb – Constant DataBase library"
---

<h2 class="name">NAME</h2>
<p> cdb &#8211; Constant DataBase library</p>
<h2>SYNOPSYS</h2>
<pre><code>
#include &lt;cdb.h&gt;
cc... - lcdb
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>cdb</code> is a library to create and access Constant DataBase files. File stores (key,value) pairs and used to quickly find a value based on a given key. Cdb files are create-once files, that is, once created, file cannot be updated but recreated from scratch &#8212; this is why database is called <i>constant</i>. Cdb file is optimized for quick access. Format of such file described in <i><a href="/docs/linux/man/5-cdb/">cdb</a></i>(5) manpage. This manual page corresponds to version <code>0.78</code> of <code>tinycdb</code> package. </p>
<p> Library defines two non-interlaced interfaces: for querying existing cdb file data (read-only mode) and for creating such a file (almost write-only). Strictly speaking, those modes allows very limited set of opposite operation as well (i.e. in query mode, it is possible to update key&#8217;s value). </p>
<p> All routines in this library are thread-safe as no global data used, except of <i>errno</i> variable for error indication. </p>
<p> <code>cdb</code> datafiles may be moved between systems safely, since format does not depend on architecture. </p>
<h2>QUERY MODE</h2>
<p> There are two query modes available. First uses a structure that represents a cdb database, just like <code>FILE</code> structure in stdio library, and another works with plain filedescriptor. First mode is more sophisticated and flexible, and usually somewhat faster. It uses <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) internally. This mode may look more &quot;natural&quot; or object-oriented compared to second one. </p>
<p> The following routines works with any mode: </p>
<p>unsigned cdb_unpack(buf)<br />
    const unsigned char buf[4];</p>
<dl>
<dt>
<dd> helper routine to convert 32-bit integer from internal representation to machine format. May be used to handle application integers in a portable way. There is no error return.</dl>
<h3>Query Mode 1</h3>
<p> All query operations in first more deals with common data structure, <code>struct cdb</code>, associated with an open file descriptor. This structure is opaque to application. </p>
<p> The following routines exists for accessing <code>cdb</code> database: </p>
<p>int cdb_init(cdbp, fd)<br />
struct cdb *cdbp;<br />
int fd;</p>
<dl>
<dt>
<dd> initializes structure given by <i>cdbp</i> pointer and associates it with opened file descriptor <i>fd</i>. Memory allocation for structure itself if needed and file open operation should be done by application. File <i>fd</i> should be opened at least read-only, and should be seekable. Routine returns 0 on success or negative value on error.</dl>
<pre>
void <code>cdb_free</code>(<i>cdbp</i>)
   struct cdb *<i>cdbp</i>;
</pre>
<dl>
<dt>
<dd> frees internal resources held by structure. Note that this routine does <i>not</i> closes a file.</dl>
<p>int cdb_fileno(cdbp)<br />
    const struct cdb *cdbp;</p>
<dl>
<dt>
<dd> returns filedescriptor associated with cdb (as was passed to <code>cdb_init</code>()).</dl>
<p>int cdb_read(cdbp, buf, len, pos)<br />
int cdb_readdata(cdbp, buf, len, pos)<br />
int cdb_readkey(cdbp, buf, len, pos)<br />
    const struct cdb *cdbp;<br />
void *buf;<br />
unsigned len;<br />
unsigned pos;</p>
<dl>
<dt>
<dd> reads a data from cdb file, starting at position <i>pos</i> of length <i>len</i>, placing result to <i>buf</i>. This routine may be used to get actual value found by <code>cdb_find</code>() or other routines that returns position and length of a data. Returns 0 on success or negative value on error. Routines <code>cdb_readdata</code>() and <code>cdb_readkey</code>() are shorthands to read current (after e.g. <code>cdb_find</code>()) data and key respectively, using <code>cdb_read</code>().</dl>
<p>const void *cdb_get(cdbp, len, pos)<br />
    const void *cdb_getdata(cdbp)<br />
        const void *cdb_getkey(cdbp)<br />
            const struct cdb *cdbp;<br />
unsigned len;<br />
unsigned pos;</p>
<dl>
<dt>
<dd> Internally, cdb library uses memory-mmaped region to access the on-disk database. <code>cdb_get</code>() allows to access internal memory in a way similar to <code>cdb_read</code>() but without extra copying and buffer allocation. Returns pointer to actual data on success or NULL on error (position points to outside of the database). Routines <code>cdb_getdata</code>() and <code>cdb_getkey</code>() are shorthands to access current (after e.g. <code>cdb_find</code>()) data and key respectively, using <code>cdb_get</code>().</dl>
<p>int cdb_find(cdbp, key, klen)<br />
unsigned cdb_datapos(cdbp)<br />
unsigned cdb_datalen(cdbp)<br />
unsigned cdb_keypos(cdbp)<br />
unsigned cdb_keylen(cdbp)<br />
struct cdb *cdbp;<br />
const void *key;<br />
unsigned klen;</p>
<dl>
<dt>
<dd> attempts to find a key given by (<i>key</i>,<i>klen</i>) parameters. If key exists in database, routine returns 1 and places position and length of value associated with this key to internal fields inside <i>cdbp</i> structure, to be accessible by <code>cdb_datapos</code>(<i>cdbp</i>) and <code>cdb_datalen</code>(<i>cdbp</i>) routines. If key is not in database, <code>cdb_find</code>() returns 0. On error, negative value is returned. Data pointers (available via <code>cdb_datapos</code>() and <code>cdb_datalen</code>()) gets updated only in case of successful search. Note that using <code>cdb_find</code>() it is possible to lookup only <i>first</i> record with a given key.</dl>
<p>int cdb_findinit(cdbfp, cdbp, key, klen)<br />
int cdb_findnext(cdbfp)<br />
struct cdb_find *cdbfp;<br />
const struct cdb *cdbp;<br />
const void *key;<br />
unsigned klen;</p>
<dl>
<dt>
<dd> sequential-find routines that used separate structure. It is possible to have more than one record with the same key in a database, and these routines allows to enumerate all them. <code>cdb_findinit</code>() initializes search structure pointed to by <i>cdbfp</i>. It will return negative value on error or non-negative value on success. <code>cdb_findnext</code>() attempts to find next (first when called right after <code>cdb_findinit</code>()) matching key, setting value position and length in <i>cdbfp</i> structure. It will return positive value if given key was found, 0 if there is no more such key(s), or negative value on error. To access value position and length after successful call to <code>cdb_findnext</code>() (when it returned positive result), use <code>cdb_datapos</code>(<i>cdbp</i>) and <code>cdb_datalen</code>(<i>cdbp</i>) routines. It is error to continue using <code>cdb_findnext</code>() after it returned 0 or error condition (<code>cdb_findinit</code>() should be called again). Current data pointers (available via <code>cdb_datapos</code>() and <code>cdb_datalen</code>()) gets updated only on successful search.</dl>
<p>void cdb_seqinit(cptr, cdbp) int cdb_seqnext(cptr, cdbp)<br />
unsigned *cptr;<br />
struct cdb *cdbp;</p>
<dl>
<dt>
<dd> sequential enumeration of all records stored in cdb file. <code>cdb_seqinit</code>() initializes access current data pointer <i>cptr</i> to point before first record in a cdb file. <code>cdb_seqnext</code>() updates data pointers in <i>cdbp</i> to point to the next record and updates <i>cptr</i>, returning positive value on success, 0 on end of data condition and negative value on error. Current record will be available after successful operation using <code>cdb_datapos</code>(<i>cdbp</i>) and <code>cdb_datalen</code>(<i>cdbp</i>) (for the data) and <code>cdb_keypos</code>(<i>cdbp</i>) and <code>cdb_keylen</code>(<i>cdbp</i>) (for the key of the record). Data pointers gets updated only in case of successful operation.</dl>
<h3>Query Mode 2</h3>
<p> In this mode, one need to open a <code>cdb</code> file using one of standard system calls (such as <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) to obtain a filedescriptor, and then pass that filedescriptor to cdb routines. Available methods to query a cdb database using only a filedescriptor include: </p>
<p>int cdb_seek(fd, key, klen, dlenp)<br />
int fd;<br />
const void *key;<br />
unsigned klen;<br />
unsigned *dlenp;</p>
<dl>
<dt>
<dd> searches a cdb database (as pointed to by <i>fd</i> filedescriptor) for a key given by (<i>key</i>, <i>klen</i>), and positions file pointer to start of data associated with that key if found, so that next read operation from this filedescriptor will read that value, and places length of value, in bytes, to variable pointed to by <i>dlenp</i>. Returns positive value if operation was successful, 0 if key was not found, or negative value on error. To read the data from a cdb file, <code>cdb_bread</code>() routine below can be used.</dl>
<p>int cdb_bread(fd, buf, len)<br />
int fd;<br />
void *buf;<br />
int len;</p>
<dl>
<dt>
<dd> reads data from a file (as pointed to by <i>fd</i> filedescriptor) and places <i>len</i> bytes from this file to a buffer pointed to by <i>buf</i>. Returns 0 if exactly <i>len</i> bytes was read, or a negative value in case of error or end-of-file. This routine ignores interrupt errors (EINTR). Sets errno variable to <code>EIO</code> in case of end-of-file condition (when there is less than <i>len</i> bytes available to read).</dl>
<h3>Notes</h3>
<p> Note that <i>value</i> of any given key may be updated in place by another value of the same size, by writing to file at position found by <code>cdb_find</code>() or <code>cdb_seek</code>(). However one should be very careful when doing so, since write operation may not succeed in case of e.g. power failure, thus leaving corrupted data. When database is (re)created, one can guarantee that no incorrect data will be written to database, but not with inplace update. Note also that it is not possible to update any key or to change length of value. </p>
<h3></h3>
<h2>CREATING MODE</h2>
<p> <code>cdb</code> database file should usually be created in two steps: first, temporary file created and written to disk, and second, that temporary file is renamed to permanent place. Unix <a href="/docs/linux/man/2-rename/">rename</a>(2) call is atomic operation, it removes destination file if any AND renaes another file in one step. This way it is guaranteed that readers will not see incomplete database. To prevent multiple simultaneous updates, locking may also be used. </p>
<p> All routines used to create <code>cdb</code> database works with <code>struct cdb_make</code> object that is opaque to application. Application may assume that <code>struct cdb_make</code> has at least the same member(s) as published in <code>struct cdb</code> above. </p>
<p>int cdb_make_start(cdbmp, fd)<br />
struct cdb_make *cdbmp;<br />
int fd;</p>
<dl>
<dt>
<dd> initializes structure to create a database. File <i>fd</i> should be opened read-write and should be seekable. Returns 0 on success or negative value on error.</dl>
<p>int cdb_make_add(cdbmp, key, klen, val, vlen)<br />
struct cdb_make *cdbmp;<br />
const void *key, *val;<br />
unsigned klen, vlen;</p>
<dl>
<dt>
<dd> adds record with key (<i>key</i>,<i>klen</i>) and value (<i>val</i>,<i>vlen</i>) to a database. Returns 0 on success or negative value on error. Note that this routine does not checks if given key already exists, but <code>cdb_find</code>() will not see second record with the same key. It is not possible to continue building a database if <code>cdb_make_add</code>() returned error indicator.</dl>
<pre>
int <code>cdb_make_finish</code>(<i>cdbmp</i>)
   struct cdb_make *<i>cdbmp</i>;
</pre>
<dl>
<dt>
<dd> finalizes database file, constructing all needed indexes, and frees memory structures. It does <i>not</i> closes filedescriptor. Returns 0 on success or negative value on error.</dl>
<p>int cdb_make_exists(cdbmp, key, klen)<br />
struct cdb_make *cdbmp;<br />
const void *key;<br />
unsigned klen;</p>
<dl>
<dt>
<dd> This routine attempts to find given by (<i>key</i>,<i>klen</i>) key in a not-yet-complete database. It may significantly slow down the whole process, and currently it flushes internal buffer to disk on every call with key those hash value already exists in db. Returns 0 if such key doesn&#8217;t exists, 1 if it is, or negative value on error. Note that database file should be opened read-write (not write-only) to use this routine. If <code>cdb_make_exists</code>() returned error, it may be not possible to continue constructing database.</dl>
<p>int cdb_make_find(cdbmp, key, klen, mode)<br />
struct cdb_make *cdbmp;<br />
const void *key;<br />
unsigned klen;<br />
int mode;</p>
<dl>
<dt>
<dd> This routine attempts to find given by (<i>key</i>,<i>klen</i>) key in the database being created. If the given key is already exists, it an action specified by <i>mode</i> will be performed:</p>
<dl>
<dt><code>CDB_FIND</code></p>
<dd> checks whenever the given record is already in the database.</p>
<dt><code>CDB_FIND_REMOVE</code></p>
<dd> removes all matching records by re-writing the database file accordingly.</p>
<dt><code>CDB_FIND_FILL0</code></p>
<dd> fills all matching records with zeros and removes them from index so that the records in question will not be findable with <code>cdb_find</code>(). This is faster than CDB_FIND_REMOVE, but leaves zero &quot;gaps&quot; in the database. Lastly inserted records, if matched, are always removed.</dl>
<p> If no matching keys was found, routine returns 0. In case at least one record has been found/removed, positive value will be returned. On error, negative value will be returned and <code>errno</code> will be set appropriately. When <code>cdb_make_find</code>() returned negative value in case of error, it is not possible to continue constructing the database. </p>
<p> <code>cdb_make_exists</code>() is the same as calling <code>cdb_make_find</code>() with <i>mode</i> set to CDB_FIND.</dl>
<p>int cdb_make_put(cdbmp, key, klen, val, vlen, mode)<br />
struct cdb_make *cdbmp;<br />
const void *key, *val;<br />
unsigned klen, vlen;<br />
int mode;</p>
<dl>
<dt>
<dd> This is a somewhat combined <code>cdb_make_exists</code>() and <code>cdb_make_add</code>() routines. <i>mode</i> argument controls how repeated (already existing) keys will be treated:</p>
<dl>
<dt><code>CDB_PUT_ADD</code></p>
<dd> no duplicate checking will be performed. This mode is the same as <code>cdb_make_add</code>() routine does.</p>
<dt><code>CDB_PUT_REPLACE</code></p>
<dd> If the key already exists, it will be removed from the database before adding new key,value pair. This requires moving data in the file, and can be quite slow if the file is large. All matching old records will be removed this way. This is the same as calling <code>cdb_make_find</code>() with CDB_FIND_REMOVE <i>mode</i> argument followed by calling <code>cdb_make_add</code>().</p>
<dt><code>CDB_PUT_REPLACE0</code></p>
<dd> If the key already exists and it isn&#8217;t the last record in the file, old record will be zeroed out before adding new key,value pair. This is alot faster than CDB_PUT_REPLACE, but some extra data will still be present in the file. The data &#8212; old record &#8212; will not be accessible by normal searches, but will appear in sequential database traversal. This is the same as calling <code>cdb_make_find</code>() with CDB_FIND_FILL0 <i>mode</i> argument followed by <code>cdb_make_add</code>().</p>
<dt><code>CDB_PUT_INSERT</code></p>
<dd> add key,value pair only if such key does not exists in a database. Note that since query (see query mode above) will find first added record, this mode is somewhat useless (but allows to reduce database size in case of repeated keys). This is the same as calling <code>cdb_make_exists</code>(), followed by <code>cdb_make_add</code>() if the key was not found.</p>
<dt><code>CDB_PUT_WARN</code></p>
<dd> add key,value pair unconditionally, but also check if this key already exists. This is equivalent of <code>cdb_make_exists</code>() to check existence of the given key, unconditionally followed by <code>cdb_make_add</code>().</dl>
<p> If any error occurred during operations, the routine will return negative integer and will set global variable <code>errno</code> to indicate reason of failure. In case of successful operation and no duplicates found, routine will return 0. If any duplicates has been found or removed (which, in case of CDB_PUT_INSERT mode, indicates that the new record was not added), routine will return positive value. If an error occurred and <code>cdb_make_put</code>() returned negative error, it is not possible to continue database construction process. </p>
<p> As with <code>cdb_make_exists</code>() and <code>cdb_make_find</code>(), usage of this routine with any but CDB_PUT_ADD mode can significantly slow down database creation process, especially when <i>mode</i> is equal to CDB_PUT_REPLACE0. </p>
</dl>
<p>void cdb_pack(num, buf) unsigned num;<br />
unsigned char buf[4];</p>
<dl>
<dt>
<dd> helper routine that used internally to convert machine integer <i>n</i> to internal form to be stored in datafile. 32-bit integer is stored in 4 bytes in network byte order. May be used to handle application data. There is no error return.</dl>
<p>unsigned cdb_hash(buf, len)<br />
    const void *buf;<br />
unsigned len;</p>
<dl>
<dt>
<dd> helper routine that calculates cdb hash value of given bytes. CDB hash function is </p>
<p>&nbsp;<wbr>&nbsp;<wbr>hash[n]&nbsp;<wbr>=&nbsp;<wbr>(hash[n-1]&nbsp;<wbr>+&nbsp;<wbr>(hash[n-1]&nbsp;<wbr>&lt;&lt;&nbsp;<wbr>5))&nbsp;<wbr>^&nbsp;<wbr>buf[n]<br />
 starting with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>hash[-1]&nbsp;<wbr>=&nbsp;<wbr>5381
</dl>
<h2>ERRORS</h2>
<p> <code>cdb</code> library may set <code>errno</code> to following on error: </p>
<dl>
<dt>EPROTO</p>
<dd> database file is corrupted in some way</p>
<dt>EINVAL</p>
<dd> the same as EPROTO above if system lacks EPROTO constant</p>
<dt>EINVAL</p>
<dd> <i>flag</i> argument for <code>cdb_make_put</code>() is invalid</p>
<dt>EEXIST</p>
<dd> <i>flag</i> argument for <code>cdb_make_put</code>() is CDB_PUT_INSERT, and key already exists</p>
<dt>ENOMEM</p>
<dd> not enough memory to complete operation (<code>cdb_make_finish</code> and <code>cdb_make_add</code>)</p>
<dt>EIO</p>
<dd> set by <code>cdb_bread</code> and <code>cdb_seek</code> if a cdb file is shorter than expected or corrupted in some other way. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Note: in all examples below, error checking is not shown for brewity. </p>
<h3>Query Mode</h3>
<p>int fd;<br />
struct cdb cdb;<br />
char *key, *data;<br />
unsigned keylen, datalen;<br />
/* opening the database */<br />
fd = open(filename, O_RDONLY);<br />
cdb_init(&amp;cdb, fd);<br />
/* initialize key and keylen here */<br />
/* single-record search. */<br />
if (cdb_find(&amp;cdb, key, keylen) &gt; 0) {<br />
    datalen = cdb_datalen(&amp;cdb);<br />
    data = malloc(datalen + 1);<br />
    cdb_read(&amp;cdb, data, datalen, cdb_datapos(&amp;cdb));<br />
    data[datalen] = &#8216;
