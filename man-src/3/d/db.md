---
title: "db(3)"
name: "db"
section: "3"
letter: "d"
url: "/docs/linux/man/3-db/"
description: "dbopen – database access methods"
---

<h2 class="name">NAME</h2>
<p> dbopen &#8211; database access methods </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;db.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;limits.h&gt;
#include &lt;sys/types.h&gt;
DB *dbopen(const char *file, int flags, int mode, DBTYPE type,
           const void *openinfo);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Note well</i>: This page documents interfaces provided in glibc up until version 2.1. Since version 2.2, glibc no longer provides these interfaces. Probably, you are looking for the APIs provided by the <i>libdb</i> library instead. </p>
<p> <code>dbopen</code>() is the library interface to database files. The supported file formats are btree, hashed and UNIX file oriented. The btree format is a representation of a sorted, balanced tree structure. The hashed format is an extensible, dynamic hashing scheme. The flat-file format is a byte stream file with fixed or variable length records. The formats and file-format-specific information are described in detail in their respective manual pages <code><a href="/docs/linux/man/3-btree/">btree</a></code>(3), <code><a href="/docs/linux/man/3-hash/">hash</a></code>(3), and <code><a href="/docs/linux/man/3-recno/">recno</a></code>(3). </p>
<p> <code>dbopen</code>() opens <i>file</i> for reading and/or writing. Files never intended to be preserved on disk may be created by setting the <i>file</i> argument to NULL. </p>
<p> The <i>flags</i> and <i>mode</i> arguments are as specified to the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) routine, however, only the <code>O_CREAT</code>, <code>O_EXCL</code>, <code>O_EXLOCK</code>, <code>O_NONBLOCK</code>, <code>O_RDONLY</code>, <code>O_RDWR</code>, <code>O_SHLOCK</code>, and <code>O_TRUNC</code> flags are meaningful. (Note, opening a database file <code>O_WRONLY</code> is not possible.) </p>
<p> The <i>type</i> argument is of type <i>DBTYPE</i> (as defined in the <i>&lt;db.h&gt;</i> include file) and may be set to <code>DB_BTREE</code>, <code>DB_HASH</code>, or <code>DB_RECNO</code>. </p>
<p> The <i>openinfo</i> argument is a pointer to an access-method-specific structure described in the access method&#8217;s manual page. If <i>openinfo</i> is NULL, each access method will use defaults appropriate for the system and the access method. </p>
<p> <code>dbopen</code>() returns a pointer to a <i>DB</i> structure on success and NULL on error. The <i>DB</i> structure is defined in the <i>&lt;db.h&gt;</i> include file, and contains at least the following fields: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;DBTYPE type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;(*close)(const DB&nbsp;*db);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;(*del)(const DB&nbsp;*db, const DBT&nbsp;*key, unsigned int flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;(*fd)(const DB&nbsp;*db);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;(*get)(const DB&nbsp;*db, DBT&nbsp;*key, DBT&nbsp;*data,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;(*put)(const DB&nbsp;*db, DBT&nbsp;*key, const DBT&nbsp;*data,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;(*sync)(const DB&nbsp;*db, unsigned int flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;(*seq)(const DB&nbsp;*db, DBT&nbsp;*key, DBT&nbsp;*data,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int flags); } DB; </p>
<p> These elements describe a database type and a set of functions performing various actions. These functions take a pointer to a structure as returned by <code>dbopen</code>(), and sometimes one or more pointers to key/data structures and a flag value.</p>
<dl>
<dt><i>type</i></p>
<dd> The type of the underlying access method (and file format).</p>
<dt><i>close</i></p>
<dd> A pointer to a routine to flush any cached information to disk, free any allocated resources, and close the underlying file(s). Since key/data pairs may be cached in memory, failing to sync the file with a <i>close</i> or <i>sync</i> function may result in inconsistent or lost information. <i>close</i> routines return -1 on error (setting <i>errno</i>) and 0 on success.</p>
<dt><i>del</i></p>
<dd> A pointer to a routine to remove key/data pairs from the database.</p>
<dt>
<dd> The argument <i>flag</i> may be set to the following value:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>R_CURSOR</code></p>
<dd> Delete the record referenced by the cursor. The cursor must have previously been initialized.</dl>
</dl>
<dt>
<dd> <i>delete</i> routines return -1 on error (setting <i>errno</i>), 0 on success, and 1 if the specified <i>key</i> was not in the file.</p>
<dt><i>fd</i></p>
<dd> A pointer to a routine which returns a file descriptor representative of the underlying database. A file descriptor referencing the same file will be returned to all processes which call <code>dbopen</code>() with the same <i>file</i> name. This file descriptor may be safely used as an argument to the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) and <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) locking functions. The file descriptor is not necessarily associated with any of the underlying files used by the access method. No file descriptor is available for in memory databases. <i>fd</i> routines return -1 on error (setting <i>errno</i>), and the file descriptor on success.</p>
<dt><i>get</i></p>
<dd> A pointer to a routine which is the interface for keyed retrieval from the database. The address and length of the data associated with the specified <i>key</i> are returned in the structure referenced by <i>data</i>. <i>get</i> routines return -1 on error (setting <i>errno</i>), 0 on success, and 1 if the <i>key</i> was not in the file.</p>
<dt><i>put</i></p>
<dd> A pointer to a routine to store key/data pairs in the database.</p>
<dt>
<dd> The argument <i>flag</i> may be set to one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>R_CURSOR</code></p>
<dd> Replace the key/data pair referenced by the cursor. The cursor must have previously been initialized.</p>
<dt><code>R_IAFTER</code></p>
<dd> Append the data immediately after the data referenced by <i>key</i>, creating a new key/data pair. The record number of the appended key/data pair is returned in the <i>key</i> structure. (Applicable only to the <code>DB_RECNO</code> access method.)</p>
<dt><code>R_IBEFORE</code></p>
<dd> Insert the data immediately before the data referenced by <i>key</i>, creating a new key/data pair. The record number of the inserted key/data pair is returned in the <i>key</i> structure. (Applicable only to the <code>DB_RECNO</code> access method.)</p>
<dt><code>R_NOOVERWRITE</code></p>
<dd> Enter the new key/data pair only if the key does not previously exist.</p>
<dt><code>R_SETCURSOR</code></p>
<dd> Store the key/data pair, setting or initializing the position of the cursor to reference it. (Applicable only to the <code>DB_BTREE</code> and <code>DB_RECNO</code> access methods.)</dl>
</dl>
<dt>
<dd> <code>R_SETCURSOR</code> is available only for the <code>DB_BTREE</code> and <code>DB_RECNO</code> access methods because it implies that the keys have an inherent order which does not change.</p>
<dt>
<dd> <code>R_IAFTER</code> and <code>R_IBEFORE</code> are available only for the <code>DB_RECNO</code> access method because they each imply that the access method is able to create new keys. This is true only if the keys are ordered and independent, record numbers for example.</p>
<dt>
<dd> The default behavior of the <i>put</i> routines is to enter the new key/data pair, replacing any previously existing key.</p>
<dt>
<dd> <i>put</i> routines return -1 on error (setting <i>errno</i>), 0 on success, and 1 if the <code>R_NOOVERWRITE</code> <i>flag</i> was set and the key already exists in the file.</p>
<dt><i>seq</i></p>
<dd> A pointer to a routine which is the interface for sequential retrieval from the database. The address and length of the key are returned in the structure referenced by <i>key</i>, and the address and length of the data are returned in the structure referenced by <i>data</i>.</p>
<dt>
<dd> Sequential key/data pair retrieval may begin at any time, and the position of the &quot;cursor&quot; is not affected by calls to the <i>del</i>, <i>get</i>, <i>put</i>, or <i>sync</i> routines. Modifications to the database during a sequential scan will be reflected in the scan, that is, records inserted behind the cursor will not be returned while records inserted in front of the cursor will be returned.</p>
<dt>
<dd> The flag value <code>must</code> be set to one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>R_CURSOR</code></p>
<dd> The data associated with the specified key is returned. This differs from the <i>get</i> routines in that it sets or initializes the cursor to the location of the key as well. (Note, for the <code>DB_BTREE</code> access method, the returned key is not necessarily an exact match for the specified key. The returned key is the smallest key greater than or equal to the specified key, permitting partial key matches and range searches.)</p>
<dt><code>R_FIRST</code></p>
<dd> The first key/data pair of the database is returned, and the cursor is set or initialized to reference it.</p>
<dt><code>R_LAST</code></p>
<dd> The last key/data pair of the database is returned, and the cursor is set or initialized to reference it. (Applicable only to the <code>DB_BTREE</code> and <code>DB_RECNO</code> access methods.)</p>
<dt><code>R_NEXT</code></p>
<dd> Retrieve the key/data pair immediately after the cursor. If the cursor is not yet set, this is the same as the <code>R_FIRST</code> flag.</p>
<dt><code>R_PREV</code></p>
<dd> Retrieve the key/data pair immediately before the cursor. If the cursor is not yet set, this is the same as the <code>R_LAST</code> flag. (Applicable only to the <code>DB_BTREE</code> and <code>DB_RECNO</code> access methods.)</dl>
</dl>
<dt>
<dd> <code>R_LAST</code> and <code>R_PREV</code> are available only for the <code>DB_BTREE</code> and <code>DB_RECNO</code> access methods because they each imply that the keys have an inherent order which does not change.</p>
<dt>
<dd> <i>seq</i> routines return -1 on error (setting <i>errno</i>), 0 on success and 1 if there are no key/data pairs less than or greater than the specified or current key. If the <code>DB_RECNO</code> access method is being used, and if the database file is a character special file and no complete key/data pairs are currently available, the <i>seq</i> routines return 2.</p>
<dt><i>sync</i></p>
<dd> A pointer to a routine to flush any cached information to disk. If the database is in memory only, the <i>sync</i> routine has no effect and will always succeed.</p>
<dt>
<dd> The flag value may be set to the following value:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>R_RECNOSYNC</code></p>
<dd> If the <code>DB_RECNO</code> access method is being used, this flag causes the sync routine to apply to the btree file which underlies the recno file, not the recno file itself. (See the <i>bfname</i> field of the <code><a href="/docs/linux/man/3-recno/">recno</a></code>(3) manual page for more information.)</dl>
</dl>
<dt>
<dd> <i>sync</i> routines return -1 on error (setting <i>errno</i>) and 0 on success.</dl>
<h3>Key/data pairs</h3>
<p> Access to all file types is based on key/data pairs. Both keys and data are represented by the following data structure: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t size; } DBT; </p>
<p> The elements of the <i>DBT</i> structure are defined as follows:</p>
<dl>
<dt><i>data</i></p>
<dd> A pointer to a byte string.</p>
<dt><i>size</i></p>
<dd> The length of the byte string.</dl>
<p> Key and data byte strings may reference strings of essentially unlimited length although any two of them must fit into available memory at the same time. It should be noted that the access methods provide no guarantees about byte string alignment.</p>
<h2>ERRORS</h2>
<p> The <code>dbopen</code>() routine may fail and set <i>errno</i> for any of the errors specified for the library routines <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) or the following:</p>
<dl>
<dt><code>EFTYPE</code></p>
<dd> A file is incorrectly formatted.</p>
<dt><code>EINVAL</code></p>
<dd> A parameter has been specified (hash function, pad byte, etc.) that is incompatible with the current file specification or which is not meaningful for the function (for example, use of the cursor without prior initialization) or there is a mismatch between the version number of file and the software.</dl>
<p> The <i>close</i> routines may fail and set <i>errno</i> for any of the errors specified for the library routines <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), or <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2). </p>
<p> The <i>del</i>, <i>get</i>, <i>put</i>, and <i>seq</i> routines may fail and set <i>errno</i> for any of the errors specified for the library routines <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-free/">free</a></code>(3) or <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). </p>
<p> The <i>fd</i> routines will fail and set <i>errno</i> to <code>ENOENT</code> for in memory databases. </p>
<p> The <i>sync</i> routines may fail and set <i>errno</i> for any of the errors specified for the library routine <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2).</p>
<h2>BUGS</h2>
<p> The typedef <i>DBT</i> is a mnemonic for &quot;data base thang&quot;, and was used because no one could think of a reasonable name that wasn&#8217;t already used. </p>
<p> The file descriptor interface is a kludge and will be deleted in a future version of the interface. </p>
<p> None of the access methods provide any form of concurrent access, locking, or transactions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-btree/">btree</a></code>(3), <code><a href="/docs/linux/man/3-hash/">hash</a></code>(3), <code><a href="/docs/linux/man/3-mpool/">mpool</a></code>(3), <code><a href="/docs/linux/man/3-recno/">recno</a></code>(3) </p>
<p> <i>LIBTP: Portable, Modular Transactions for UNIX</i>, Margo Seltzer, Michael Olson, USENIX proceedings, Winter 1992.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
