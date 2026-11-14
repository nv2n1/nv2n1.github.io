---
title: "gdbm(3)"
name: "gdbm"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gdbm/"
description: "GDBM – The GNU database manager. Includes dbm and ndbm compatability. (Version 1.9.)"
---

<h2 class="name">NAME</h2>
<p> GDBM &#8211; The GNU database manager. Includes <code>dbm</code> and <code>ndbm</code> compatability. (Version 1.9.) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;gdbm.h&gt;
extern gdbm_error gdbm_errno;

extern char *gdbm_version;

GDBM_FILE gdbm_open(const char *name, int block_size,

                    &amp;nbsp;
                    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; int flags, int mode,

                                                                                                                                                                &amp;nbsp;
                    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; void (*fatal_func)(const char *));

void gdbm_close(GDBM_FILE dbf);

int gdbm_store(GDBM_FILE dbf, datum key, datum content, int flag);

datum gdbm_fetch(GDBM_FILE dbf, datum key);

int gdbm_delete(GDBM_FILE dbf, datum key);

datum gdbm_firstkey(GDBM_FILE dbf);

datum gdbm_nextkey(GDBM_FILE dbf, datum key);

int gdbm_reorganize(GDBM_FILE dbf);

void gdbm_sync(GDBM_FILE dbf);

int gdbm_exists(GDBM_FILE dbf, datum key);

const char *gdbm_strerror(gdbm_error errno);

int gdbm_setopt(GDBM_FILE dbf, int option, int value, int size);

int gdbm_fdesc(GDBM_FILE dbf);
</code></pre>
<h3>DBM Compatability routines:</h3>
<p> <code>#include &lt;dbm.h&gt;</code> </p>
<p> <code>int dbminit (const char *</code><i>name</i><code>);</code><br />
 <code>int store (datum </code><i>key</i><code>, datum </code><i>content</i><code>);</code><br />
 <code>datum fetch (datum </code><i>key</i><code>);</code><br />
 <code>int delete (datum </code><i>key</i><code>);</code><br />
 <code>datum firstkey (void);</code><br />
 <code>datum nextkey (datum </code><i>key</i><code>);</code><br />
 <code>int dbmclose (void);</code> </p>
<h3>NDBM Compatability routines:</h3>
<p> <code>#include &lt;ndbm.h&gt;</code> </p>
<p> <code>DBM *dbm_open (const char *</code><i>name</i><code>, int </code><i>flags</i><code>, int </code><i>mode</i><code>);</code><br />
 <code>void dbm_close (DBM *</code><i>file</i><code>);</code> <code>datum</code><i>dbm_fetch</i><code>(DBM</code><i>* file ,</i><code>datum</code><i> key );</i><br />
 <code>int dbm_store (DBM *</code><i>file</i><code>, datum </code><i>key</i><code>, datum </code><i>content</i><code>, int </code><i>flags</i><code>);</code><br />
 <code>int dbm_delete (DBM *</code><i>file</i><code>, datum </code><i>key</i><code>);</code><br />
 <code>datum dbm_firstkey (DBM *</code><i>file</i><code>);</code><br />
 <code>datum dbm_nextkey (DBM *</code><i>file</i><code>, datum </code><i>key</i><code>);</code><br />
 <code>int dbm_error (DBM *</code><i>file</i><code>);</code><br />
 <code>int dbm_clearerr (DBM *</code><i>file</i><code>);</code><br />
 <code>int dbm_pagfno (DBM *</code><i>file</i><code>);</code><br />
 <code>int dbm_dirfno (DBM *</code><i>file</i><code>);</code><br />
 <code>int dbm_rdonly (DBM *</code><i>file</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>GNU dbm</code> is a library of routines that manages data files that contain key/data pairs. The access provided is that of storing, retrieval, and deletion by key and a non-sorted traversal of all keys. A process is allowed to use multiple data files at the same time. </p>
<p> This manpage is a short description of the <code>GDBM</code> library. For a detailed discussion, including examples of the configuration and usage recommendations, refer to the <code>GDBM Manual</code> available in Texinfo format. To access it, run: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>info gdbm</code> </p>
<p> Should any discrepancies occur between this manpage and the <code>GDBM Manual</code>, the later shall be considered the authoritative source. </p>
<p> A process that opens a gdbm file is designated as a &quot;reader&quot; or a &quot;writer&quot;. Only one writer may open a gdbm file and many readers may open the file. Readers and writers can not open the gdbm file at the same time. The procedure for opening a gdbm file is: </p>
<p> <code>GDBM_FILE gdbm_open (const char *</code><i>name</i><code>, int </code><i>block_size</i><code>, </code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>int </code><i>flags</i><code>, int </code><i>mode</i><code>, </code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>void (*</code><i>fatal_func</i><code>)(const char *));</code> </p>
<p> <i>Name</i> is the name of the file (the complete name, gdbm does not append any characters to this name). <i>Block_size</i> is the size of a single transfer from disk to memory. This parameter is ignored unless the file is a new file. The minimum size is 512. If it is less than 512, dbm will use the stat block size for the file system. <i>Read_write</i> can have one of the following values:</p>
<dl>
<dt><code>GDBM_READER</code></p>
<dd> reader</p>
<dt><code>GDBM_WRITER</code></p>
<dd> writer</p>
<dt><code>GDBM_WRCREAT</code></p>
<dd> writer &#8211; if database does not exist create new one</p>
<dt><code>GDBM_NEWDB</code></p>
<dd> writer &#8211; create new database regardless if one exists</dl>
<p> The <code>GDBM_NOMMAP</code> added to <i>read_write</i> by bitwise or instructs <code>gdbm_open</code> to disable the use of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). </p>
<p> For the last three (writers of the database) the following may be added added to <i>read_write</i> by bitwise or:</p>
<dl>
<dt><code>GDBM_SYNC</code></p>
<dd> Causes all database operations to be synchronized to the disk,</p>
<dt><code>GDBM_NOLOCK</code></p>
<dd> Pevents the library from performing any locking on the database file.</dl>
<p> The option <code>GDBM_FAST</code> is now obsolete, since gdbm defaults to no-sync mode. </p>
<p> <i>Mode</i> is the file mode (see <code><a href="/docs/linux/man/2-chmod/">chmod</a>(2)</code> and <code><a href="/docs/linux/man/2-open/">open</a>(2)</code>) if the file is created. <i>(*Fatal_func) ()</i> is a function for dbm to call if it detects a fatal error. The only parameter of this function is a string. If the value of 0 is provided, <code>gdbm</code> will use a default function. </p>
<p> The return value is the pointer needed by all other routines to access that gdbm file. If the return is the NULL pointer, <code>gdbm_open</code> was not successful. The errors can be found in <i>gdbm_errno</i> for gdbm errors and in <i>errno</i> for system errors. (For error codes, see gdbmerrno.h.) </p>
<p> In all of the following calls, the parameter <i>dbf</i> refers to the pointer returned from <code>gdbm_open</code>. </p>
<p> It is important that every file opened is also closed. This is needed to update the reader/writer count on the file. This is done by: </p>
<p> <code>void gdbm_close (GDBM_FILE </code><i>dbf</i><code>);</code> </p>
<p> The database is used by 3 primary routines. The first stores data in the database. </p>
<p> <code>int gdbm_store (GDBM_FILE </code><i>dbf</i><code>, datum </code><i>key</i><code>, datum </code><i>content</i><code>, int </code><i>flag</i><code>);</code> </p>
<p> <i>Dbf</i> is the pointer returned by <code>gdbm_open</code>. <i>Key</i> is the key data. <i>Content</i> is the data to be associated with the <i>key</i>. <i>Flag</i> can have one of the following values:</p>
<dl>
<dt><code>GDBM_INSERT</code></p>
<dd> Insert only, generate an error if key exists;</p>
<dt><code>GDBM_REPLACE</code></p>
<dd> Replace contents if key exists.</dl>
<p> If a reader calls <code>gdbm_store</code>, the return value will be -1. If called with <code>GDBM_INSERT</code> and <i>key</i> is in the database, the return value will be 1. Otherwise, the return value is 0. </p>
<p> <i>NOTICE: If you store data for a key that is already in the data base, </i><code>gdbm</code><i> replaces the old data with the new data if called with </i><code>GDBM_REPLACE</code><i>. You do not get two data items for the same key and you do not get an error from </i><code>gdbm_store</code><i>. </p>
<p> NOTICE: The size in </i><code>gdbm</code><i> is not restricted like in </i><code>dbm</code><i> or </i><code>ndbm</code><i>. Your data can be as large as you want.</i> </p>
<p> To search for some data, use: </p>
<p> <code>datum gdbm_fetch (GDBM_FILE </code><i>dbf</i><code>, datum </code><i>key</i><code>);</code> </p>
<p> <i>Dbf</i> is the pointer returned by <code>gdbm_open</code>. <i>Key</i> is the key data. </p>
<p> If the <i>dptr</i> element of the return value is NULL, no data was found. Otherwise the return value is a pointer to the found data. The storage space for the <i>dptr</i> element is allocated using <code><a href="/docs/linux/man/3-malloc/">malloc</a>(3)</code>. <code>Gdbm</code><i> does not automatically free this data. It is the programmer&#8217;s responsibility to free this storage when it is no longer needed. </p>
<p> To search for some data, without retrieving it: </p>
<p> </i><code>int gdbm_exists (GDBM_FILE </code><i>dbf</i><code>, datum </code><i>key</i><code>);</code> </p>
<p> <i>Dbf</i> is the pointer returned by <code>gdbm_open</code>. <i>Key</i> is the key data to search for. </p>
<p> If the <i>key</i> is found within the database, the return value will be true. If nothing appropiate is found, false is returned. This routine is useful for checking for the existence of a record, without performing the memory allocation done by <code>gdbm_fetch</code>. </p>
<p> To remove some data from the database: </p>
<p> <code>int gdbm_delete (GDBM_FILE </code><i>dbf</i><code>, datum </code><i>key</i><code>);</code> </p>
<p> <i>Dbf</i> is the pointer returned by <code>gdbm_open</code>. <i>Key</i> is the key data. </p>
<p> The return value is -1 if the item is not present or the requester is a reader. The return value is 0 if there was a successful delete. </p>
<p> The next two routines allow for accessing all items in the database. This access is not key sequential, but it is guaranteed to visit every key in the database once. (The order has to do with the hash values.) </p>
<p> <code>datum gdbm_firstkey (GDBM_FILE </code><i>dbf</i><code>);</code><br />
 <code>datum gdbm_nextkey (GDBM_FILE </code><i>dbf</i><code>, datum </code><i>key</i><code>);</code> </p>
<p> <i>Dbf</i> is the pointer returned by <code>gdbm_open</code>. <i>Key</i> is the key data. </p>
<p> The return values are both of type <code>datum</code>. If the <i>dptr</i> element of the return value is NULL, there is no first key or next key. Again notice that <i>dptr</i> points to data allocated by <code><a href="/docs/linux/man/3-malloc/">malloc</a>(3)</code> and <code>gdbm</code> will not free it for you. </p>
<p> These functions were intended to visit the database in read-only algorithms, for instance, to validate the database or similar operations. </p>
<p> File `visiting&#8217; is based on a `hash table&#8217;. <i>gdbm_delete</i> re-arranges the hash table to make sure that any collisions in the table do not leave some item `un-findable&#8217;. The original key order is NOT guaranteed to remain unchanged in ALL instances. It is possible that some key will not be visited if a loop like the following is executed: </p>
<p>key = gdbm_firstkey(dbf);<br />
while (key.dptr) {<br />
    nextkey = gdbm_nextkey(dbf, key);<br />
    if (some condition)<br />
        gdbm_delete(dbf, key);<br />
    free(key.dptr);<br />
    key = nextkey;<br />
}</p>
<p> The following routine should be used very infrequently.<br />
&nbsp;<wbr>&nbsp;<wbr> <code>int gdbm_reorganize (GDBM_FILE </code><i>dbf</i><code>);</code> </p>
<p> If you have had a lot of deletions and would like to shrink the space used by the <code>gdbm</code> file, this routine will reorganize the database. <code>Gdbm</code> will not shorten the length of a <code>gdbm</code> file except by using this reorganization. (Deleted file space will be reused.) </p>
<p> Unless your database was opened with the <code>GDBM_SYNC</code> flag, <code>gdbm</code> does not wait for writes to be flushed to the disk before continuing. The following routine can be used to guarantee that the database is physically written to the disk file. </p>
<p> <code>void gdbm_sync (GDBM_FILE </code><i>dbf</i><code>);</code> </p>
<p> It will not return until the disk file state is syncronized with the in-memory state of the database. </p>
<p> To convert a <code>gdbm</code> error code into English text, use this routine: </p>
<p> <code>const char *gdbm_strerror (gdbm_error </code><i>errno</i><code>);</code> </p>
<p> <code>Gdbm</code> now supports the ability to set certain options on an already open database. </p>
<p> <code>int gdbm_setopt (GDBM_FILE </code><i>dbf</i><code>, int </code><i>option</i><code>, int </code><i>value</i><code>, int </code><i>size</i><code>);</code> </p>
<p> Where <i>dbf</i> is the return value from a previous call to <code>gdbm_open</code>, and <i>option</i> specifies which option to set. The valid options are currently:</p>
<dl>
<dt><code>GDBM_CACHESIZE</code></p>
<dd> Set the size of the internal bucket cache. This option may only be set once on each <i>GDBM_FILE</i> descriptor, and is set automatically to 100 upon the first access to the database.</p>
<dt><code>GDBM_FASTMODE</code></p>
<dd>
&nbsp;<wbr>Set&nbsp;<wbr><code>fast mode</code>&nbsp;<wbr>to either on or off.&nbsp;<wbr>&nbsp;<wbr>This allows&nbsp;<wbr><code>fast mode</code>&nbsp;<wbr>to be toggled on an already open and active database. <i>value</i> (see below) should be set to either TRUE or FALSE. <i>This option is now obsolete.</i></p>
<dt><code>GDBM_SYNCMODE</code></p>
<dd> Turn on or off file system synchronization operations. This setting defaults to off; <i>value</i> (see below) should be set to either TRUE or FALSE.</p>
<dt><code>GDBM_CENTFREE</code></p>
<dd> Set <code>central free block pool</code> to either on or off. The default is off, which is how previous versions of <code>Gdbm</code> handled free blocks. If set, this option causes all subsequent free blocks to be placed in the <code>global</code> pool, allowing (in thoery) more file space to be reused more quickly. <i>value</i> (see below) should be set to either TRUE or FALSE. <i>NOTICE: This feature is still under study.</i></p>
<dt><code>GDBM_COALESCEBLKS</code></p>
<dd> Set <code>free block merging</code> to either on or off. The default is off, which is how previous versions of <code>Gdbm</code> handled free blocks. If set, this option causes adjacent free blocks to be merged. This can become a CPU expensive process with time, though, especially if used in conjunction with <code>GDBM_CENTFREE</code>. <i>value</i> (see below) should be set to either TRUE or FALSE. <i>NOTICE: This feature is still under study.</i></dl>
<p> <i>value</i> is the value to set <i>option</i> to, specified as an integer pointer. <i>size</i> is the size of the data pointed to by <i>value</i>. The return value will be -1 upon failure, or 0 upon success. The global variable <i>gdbm_errno</i> will be set upon failure. </p>
<p> For instance, to set a database to use a cache of 10, after opening it with <code>gdbm_open</code>, but prior to accessing it in any way, the following code could be used: </p>
<pre><code>
int value = 10;

ret = gdbm_setopt(dbf, GDBM_CACHESIZE, &amp;value, sizeof(int));
</code></pre>
<p> If the database was opened with the <code>GDBM_NOLOCK</code> flag, the user may wish to perform their own file locking on the database file in order to prevent multiple writers operating on the same file simultaneously. </p>
<p> In order to support this, the <i>gdbm_fdesc</i> routine is provided. </p>
<p> <code>int gdbm_fdesc (GDBM_FILE </code><i>dbf</i><code>);</code> </p>
<p> Where <i>dbf</i> is the return value from a previous call to <code>gdbm_open</code>. The return value will be the file descriptor of the database. </p>
<p> The following two external variables may be useful: </p>
<p> <i>gdbm_errno</i> is the variable that contains more information about gdbm errors. (gdbm.h has the definitions of the error values and defines gdbm_errno as an external variable.) </p>
<p> <i>gdbm_version</i> is the string containing the version information. </p>
<p> There are a few more things of interest. First, <code>gdbm</code> files are not &quot;sparse&quot;. You can copy them with the UNIX <code><a href="/docs/linux/man/1-cp/">cp</a>(1)</code> command and they will not expand in the copying process. Also, there is a compatibility mode for use with programs that already use UNIX <code>dbm</code>. In this compatibility mode, no gdbm file pointer is required by the programmer, and only one file may be opened at a time. All users in compatibility mode are assumed to be writers. If the <code>gdbm</code> file is a read only, it will fail as a writer, but will also try to open it as a reader. All returned pointers in datum structures point to data that <code>gdbm</code> WILL free. They should be treated as static pointers (as standard UNIX <code>dbm</code> does).</p>
<h2>LINKING</h2>
<p> This library is accessed by specifying <i>-lgdbm</i> as the last parameter to the compile line, e.g.: </p>
<pre>
gcc -o prog prog.c -lgdbm
</pre>
<p> If you wish to use the <code>dbm</code> or <code>ndbm</code> compatibility routines, you must link in the <i>gdbm_compat</i> library as well. For example: </p>
<pre>
gcc -o prog proc.c -lgdbm -lgdbm_compat
</pre>
<h2>BUG REPORTS</h2>
<p> Send bug reports to &lt;bug-gdbm [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> dbm, ndbm</p>
<h2>AUTHOR</h2>
<p> by Philip A. Nelson, Jason Downs and Sergey Poznyakoff.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1990 &#8211; 2011 Free Software Foundation, Inc. </p>
<p> GDBM is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version. </p>
<p> GDBM is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with GDBM. If not, see &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;</p>
<h2>CONTACTS</h2>
<p> You may contact the original author by: </p>
<p>e-mail:&nbsp;<wbr>&nbsp;<wbr>phil [at] cs.wwu.edu </p>
<p>&nbsp;<wbr>&nbsp;<wbr>us-mail:&nbsp;<wbr>&nbsp;<wbr>Philip A. Nelson<br />
 Computer Science Department<br />
 Western Washington University<br />
 Bellingham, WA 98226 </p>
<p> You may contact the current maintainers by: </p>
<p>e-mail:&nbsp;<wbr>&nbsp;<wbr>downsj [at] downsj.com<br />
 and<br />
e-mail:&nbsp;<wbr>&nbsp;<wbr>gray [at] gnu.org </p>
<h2>Index</h2>
