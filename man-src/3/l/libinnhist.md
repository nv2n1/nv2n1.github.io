---
title: "libinnhist(3)"
name: "libinnhist"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libinnhist/"
description: "his – routines for managing INN history"
---

<h2 class="name">NAME</h2>
<p> his &#8211; routines for managing INN history </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;inn/history.h&gt;
struct history;
struct token;
struct histstats {
    int hitpos;
    int hitneg;
    int misses;
    int dne;
};
#define HIS_RDONLY ...
#define HIS_RDWR ...
#define HIS_CREAT ...
#define HIS_ONDISK ...
#define HIS_INCORE ...
#define HIS_MMAP ...
enum {
    HISCTLG_PATH,
    HISCTLS_PATH,
    HISCTLS_SYNCCOUNT,
    HISCTLS_NPAIRS,
    HISCTLS_IGNOREOLD,
    HISCTLS_STATINTERVAL
};
struct history *HISopen(const char *path, const char *method, int flags);
bool HISclose(struct history *history);
bool HISsync(struct history *history);
void HISsetcache(struct history *history, size_t size);
bool HISlookup(struct history *history, const char *key, time_t *arrived, time_t *posted, time_t *expires, TOKEN *token);
bool HIScheck(struct history *history, const char *key);
bool HISwrite(struct history *history, const char *key, time_t arrived, time_t posted, time_t expires, const TOKEN *token);
bool HISremember(struct history *history, const char *key, time_t arrived, time_t posted);
bool HISreplace(struct history *history, const char *key, time_t arrived, time_t posted, time_t expires, const TOKEN *token);
bool HISexpire(struct history *history, const char *path, const char *reason, bool writing, void *cookie, time_t threshold, bool (*exists)(void *cookie, time_t arrived, time_t posted, time_t expires, const TOKEN *token));
bool HISwalk(struct history *history, const char *reason, void *cookie, bool (*callback)(void *cookie, time_t arrived, time_t posted, time_t expires, const TOKEN *token));
struct histstats HISstats(struct history *history);
const char *HISerror(struct history *history);
bool HISctl(struct history *history, int request, void *val);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions provide access to the <font SIZE="-1">INN</font> history database. They maintain key/value pairs in an opaque database whilst providing for expiry of outdated information. </p>
<p> The history structure is an opaque handle returned from HISopen. </p>
<p> The <code>HISopen</code> function opens the history file designated by <i>path</i> using the mode <i>flags</i> using the specified <i>method</i>. <i>flags</i> may be <font SIZE="-1"><code>HIS_RDONLY</code></font> to indicate that read-only access to the history database is desired, or <font SIZE="-1"><code>HIS_RDWR</code></font> for read/write access. History methods are defined at build time; the history method currently available is &#8220;hisv6&#8221;. On success a newly initialised history handle is returned, or <font SIZE="-1"><code>NULL</code></font> on failure. </p>
<p> <font SIZE="-1"><code>HIS_ONDISK</code></font>, <font SIZE="-1"><code>HIS_INCORE</code></font> and <font SIZE="-1"><code>HIS_MMAP</code></font> may be logically ORed into <i>flags</i> to provide a hint to the underlying history manager as to how it should handle its data files; <font SIZE="-1"><code>HIS_ONDISK</code></font> indicates that the caller would like as much of the data to be kept on disk (and out of memory), <font SIZE="-1"><code>HIS_INCORE</code></font> indicates that the data files should be kept in main memory where possible and <font SIZE="-1"><code>HIS_MMAP</code></font> that the files should be <i>mmap()</i>ed into the processes address space. <font SIZE="-1"><code>HIS_INCORE</code></font> is typically used where a mass rebuild of the history database is being performed; the underlying history manager may assume that the caller will call <code>HISsync</code>() to sync the data files to disk. </p>
<p> The <font SIZE="-1"><code>HIS_CREAT</code></font> flag indicates that the history database should be initialised as new; if any options which affect creation of the database need to be set an anonymous history handle should be created by calling <code>HISopen</code> with <i>path</i> set to <font SIZE="-1"><code>NULL</code></font>, any options set using <code>HISctl</code>, then the database opened by calling <code>HISctl</code> with <font SIZE="-1"><code>HISCTLS_PATH</code></font>. </p>
<p> The <code>HISclose</code> function closes the handle <i>history</i> and deallocates any resources associated with it. It returns <code>false</code> on failure or <code>true</code> on success. </p>
<p> The <code>HISsync</code> function synchronises any outstanding transactions associated with <i>history</i> to disk. </p>
<p> <code>HISsetcache</code> associates a cache used for speeding up HIScheck with <i>history</i>. The cache will occupy approximately <i>size</i> bytes. </p>
<p> <code>HISlookup</code> retrieves a token from <i>history</i> based on the passed <i>key</i> (normally the Message-ID). If no entry with an associated token can be found, <code>HISlookup</code> will return <code>false</code>. If a token is found <i>arrived</i>, <i>expires</i>, and <i>posted</i> are filled in with the message arrival, expiry, and posting times respectively (or zero, if the time component is not available), in addition to <i>token</i> being set to the retrieved token and a function return value of <code>true</code>. Any of arrived, expires, posted, or token may be <font SIZE="-1"><code>NULL</code></font> in which case that component is not returned to the caller, without affecting the return value. </p>
<p> <code>HIScheck</code> checks the database <i>history</i> for <i>key</i> (normally the Message-ID); if <i>key</i> has previously been set via <code>HISwrite</code>, <code>HIScheck</code> returns <code>true</code>, else <code>false</code>. </p>
<p> <code>HISwrite</code> writes a new entry to the database <i>history</i> associated with <i>key</i>. <i>arrived</i>, <i>posted</i>, and <i>expired</i> specify the arrival, posting, and expiry time respectively; <i>posted</i> and <i>expired</i> may be specifed as &lt;= 0 in which case that component shall be treated as absent in the database. <i>token</i> is associated with the specified <i>key</i>. <code>HISwrite</code> returns <code>true</code> on success, or <code>false</code> on failure. The behaviour when <i>key</i> is not unique with respect to the existing entries in <i>history</i> is unspecified. </p>
<p> <code>HISremember</code> writes a new entry to the database <i>history</i> associated with <i>key</i>, merely remembering that this <i>key</i> has been seen, together with its arrival time <i>arrived</i> and also its posting time <i>posted</i>, if known. (Otherwise, its posting time may be specified as &lt;= 0 in case it is absent.) <code>HISremember</code> returns <code>true</code> on success, or <code>false</code> on failure. The behaviour when <i>key</i> is not unique with respect to the existing entries in <i>history</i> is unspecified. </p>
<p> <code>HISreplace</code> replaces an existing entry in the database <i>history</i>, associated with <i>key</i>. <i>arrived</i>, <i>posted</i>, <i>expired</i> specify the arrival, posting and expiry time respectively; <i>posted</i> and <i>expired</i> may be specifed as &lt;= 0 in which case that component shall be treated as absent in the database. <i>token</i> is associated with the specified <i>key</i>; if <font SIZE="-1"><code>NULL</code></font> then the history database merely remembers that this <i>key</i> has been seen, together with its arrival time. <code>HISreplace</code> returns <code>true</code> on success, or <code>false</code> on failure. </p>
<p> <code>HISexpire</code> expires the history database associated with <i>history</i>, creating a new, replacement, database in the same location if <i>path</i> is <font SIZE="-1"><code>NULL</code></font>, or in <i>path</i> if not <font SIZE="-1"><code>NULL</code></font>; if <i>path</i> is not <font SIZE="-1"><code>NULL</code></font> then the replacement of the old history database with the new one is assumed to be performed out of band by the caller. The <i>writing</i> flag is normally passed as <code>true</code>, if you wish to inhibit writing of the new database (and so merely see the callbacks), <i>writing</i> may be set <code>false</code>. </p>
<p> If the underlying history mechanism needs to pause the server, the <i>reason</i> string is used as the argument to the `ctlinnd pause&#8217; command, and as such the server should be reserved by the caller prior to calling <code>HISexpire</code>; if the caller wishes to inhibit pausing of the server, passing <font SIZE="-1"><code>NULL</code></font> will achieve this. If <i>reason</i> is not <font SIZE="-1"><code>NULL</code></font>, then on successful return from <code>HISexpire</code> the server will be left paused and the caller should unpause it. </p>
<p> The history database is scanned and entries with an associated storage token are passed to the discrimination function <i>exists</i>. </p>
<p> If <i>exists</i>() returns <code>false</code> it indicates that stored entity associated with token is no longer available (or no longer required), and therefore the associated history entry may be expired once it meets the <i>threshold</i> constraint. If <i>exists</i>() returns <code>true</code> the entry is kept as-is in the newly expired history database. </p>
<p> The <i>exists</i> function is passed the arrival, posting and expiry times, in addition to the token associated with the entry. Note that posting and/or expiry may be zero, but that the token will never be <font SIZE="-1"><code>NULL</code></font> (such entries are handled solely via the threshold mechanism). The storage token passed to the discrimination function may be updated if required (for example, as might be needed by a hierachical storage management implementation). </p>
<p> Entries in the database with a posting time less than <i>threshold</i> with no token associated with them are deleted from the database. In case the posting time is unknown, the arrival time is used instead. </p>
<p> The parameter <i>cookie</i> is passed to the discrimination function, and may be used for any purpose required by the caller. </p>
<p> If the discrimination function attempts to access the underlying database (for read or write) during the callback, the behaviour is unspecified. </p>
<p> <code>HISwalk</code> provides an iteration function for the specified <i>history</i> database. For every entry in the history database, <i>callback</i> is invoked, passing the <i>cookie</i>, arrival, posting, and expiry times, in addition to the token associated with the entry. If the <i>callback</i>() returns <code>false</code> the iteration is aborted and <code>HISwalk</code> returns <code>false</code> to the caller. </p>
<p> To process the entire database in the presence of a running server, <i>reason</i> may be passed; if this argument is not <font SIZE="-1"><code>NULL</code></font>, it is used as an an argument to the `ctlinnd (reserve|pause|go)&#8217; commands. If <i>reason</i> is <font SIZE="-1"><code>NULL</code></font> and the server is running, the behaviour of <code>HISwalk</code> is undefined. </p>
<p> If the callback function attempts to access the underlying database during the callback, the behaviour is unspecified. </p>
<p> <code>HISstats</code> returns statistics on the history cache mechanism; given a handle <i>history</i>, the return value is a <i>struct histstats</i> detailing:</p>
<dl>
<dt>&quot;hitpos&quot;</p>
<dd> The number of times an item was found directly in the cache and known to exist in the underlying history manager.</p>
<dt>&quot;hitneg&quot;</p>
<dd> The number of times an item was found directly in the cache and known not to exist in the underlying history manager.</p>
<dt>&quot;misses&quot;</p>
<dd> The number of times an item was not found directly in the cache, but on retrieval from the underlying history manager was found to exist.</p>
<dt>&quot;dne&quot;</p>
<dd> The number of times an item was not found directly in the cache, but on retrieval from the underlying history manager was found not to exist.</dl>
<p> Note that the history cache is only checked by <code>HIScheck</code> and only affected by <code>HIScheck</code>, <code>HISwrite</code>, <code>HISremember</code> and <code>HISreplace</code>. Following a call to <code>HISstats</code> the history statistics associated with <i>history</i> are cleared. </p>
<p> <code>HISerror</code> returns a string describing the most recent error associated with <i>history</i>; the format and content of these strings is history manager dependent. Note that on setting an error, the history <font SIZE="-1">API</font> will call the <code>warn</code> function from <i><a href="/docs/linux/man/3-libinn/">libinn</a></i>(3). </p>
<p> <code>HISctl</code> provides a control interface to the underlying history manager. The <i>request</i> argument determines the type of the request and the meaning of the <i>val</i> argument. The values for <i>request</i> are:</p>
<dl>
<dt>&quot;HISCTLG_PATH&quot; (const char **)</p>
<dd> Get the base file path which the history handle represents. <i>val</i> should be a pointer to a location of type <code>const char *</code>. The result must not later be passed to <i><a href="/docs/linux/man/3-free/">free</a></i>(3).</p>
<dt>&quot;HISCTLS_PATH&quot; (const char *)</p>
<dd> Set the base file path which this history handle should use; typically this is used after an anonymous handle has been created using <code>HISopen(</code><font SIZE="-1"><code>NULL</code></font><code>, &#8230;)</code>. <i>val</i> should be a value of type <code>const char *</code> and will be copied before being stored internally.</p>
<dt>&quot;HISCTLS_SYNCCOUNT&quot; (size_t *)</p>
<dd> Set an upper bound on how many history operations may be pending in core before being synced to permanent storage; <code>0</code> indicates unlimited. <i>val</i> should be a pointer to a value of type <code>size_t</code> and will not be modified by the call.</p>
<dt>&quot;HISCTLS_NPAIRS&quot; (size_t *)</p>
<dd> Set a hint to the to the underlying history manager as to how many entries there are expected to be in the history database; <code>0</code> indicates that an automatic or default sizing should be made. <i>val</i> should be a pointer to a value of type <code>size_t</code> and will not be modified by the call.</p>
<dt>&quot;HISCTLS_IGNOREOLD&quot; (bool *)</p>
<dd> Instruct the underlying history manager to ignore existing database when creating new ones; typically this option may be set to <code>true</code> if the administrator believes that the existing history database is corrupt and that ignoring it may help. <i>val</i> should be a pointer to a value of type <code>bool</code> and will not be modified by the call.</p>
<dt>&quot;HISCTLS_STATINTERVAL&quot; (time_t *)</p>
<dd> For the history v6 and tagged hash managers, set the interval, in seconds, between <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2)s of the history files checking for replaced files (as happens during expire); this option is typically used by <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) like applications. <i>val</i> should be a pointer to a value of type <code>time_t</code> and will not be modified by the call.</dl>
<h2>HISTORY</h2>
<p> Written by Alex Kiernan &lt;alexk [at] demon.net&gt; for InterNetNews 2.4.0. </p>
<p> <tt>$Id:</tt> libinnhist.pod 9074 2010-05-31 19:01:32Z iulius $ </p>
<h2>Index</h2>
