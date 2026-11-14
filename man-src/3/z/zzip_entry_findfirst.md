---
title: "zzip_entry_findfirst(3)"
name: "zzip_entry_findfirst"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_entry_findfirst/"
description: "zzip_entry_findfile, zzip_entry_findfirst, zzip_entry_findnext, zzip_entry_free, zzip_entry_findmatch – search for files in the (fseeko) zip central directory"
---

<p>zzip_entry_findfile, zzip_entry_findfirst, zzip_entry_findnext, zzip_entry_free, zzip_entry_findmatch &#8211; search for files in the (fseeko) zip central directory</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/fseeko.h&gt;

zzip__new__ ZZIP_ENTRY *zzip_entry_findfile((FILE * disk, char *filename, ZZIP_ENTRY *_zzip_restrict entry, zzip_strcmp_fn_t compare));

zzip__new__ ZZIP_ENTRY *zzip_entry_findfirst((FILE * disk));

zzip__new__ ZZIP_ENTRY *zzip_entry_findnext((ZZIP_ENTRY * _zzip_restrict entry));

int zzip_entry_free((ZZIP_ENTRY * entry));

zzip__new__ ZZIP_ENTRY *zzip_entry_findmatch((FILE * disk, char *filespec, ZZIP_ENTRY *_zzip_restrict entry, zzip_fnmatch_fn_t compare, int flags));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_entry_findfile</code> function is given a filename as an additional argument, to find the disk_entry matching a given filename. The compare-function is usually strcmp or strcasecmp or perhaps strcoll, if null then strcmp is used. &#8211; use null as argument for &quot;old&quot;-entry when searching the first matching entry, otherwise the last returned value if you look for other entries with a special &quot;compare&quot; function (if null then a doubled search is rather useless with this variant of _findfile). If no further entry is found then null is returned and any &quot;old&quot;-entry gets already free()d. The <code>zzip_entry_findfirst</code> function is the first call of all the zip access functions here. It contains the code to find the first entry of the zip central directory. Here we require the stdio handle to represent a real zip file where the disk_trailer is _last_ in the file area, so that its position would be at a fixed offset from the end of the file area if not for the comment field allowed to be of variable length (which needs us to do a little search for the disk_tailer). However, in this simple implementation we disregard any disk_trailer info telling about multidisk archives, so we just return a pointer to the first entry in the zip central directory of that file. For an actual means, we are going to search backwards from the end of the mmaped block looking for the PK-magic signature of a disk_trailer. If we see one then we check the rootseek value to find the first disk_entry of the root central directory. If we find the correct PK-magic signature of a disk_entry over there then we assume we are done and we are going to return a pointer to that label. The return value is a pointer to the first zzip_disk_entry being checked to be within the bounds of the file area specified by the arguments. If no disk_trailer was found then null is returned, and likewise we only accept a disk_trailer with a seekvalue that points to a disk_entry and both parts have valid PK-magic parts. Beyond some sanity check we try to catch a common brokeness with zip archives that still allows us to find the start of the zip central directory. The <code>zzip_entry_findnext</code> function takes an existing &quot;entry&quot; in the central root directory (e.g. from zzip_entry_findfirst) and moves it to point to the next entry. On error it returns 0, otherwise the old entry. If no further match is found then null is returned and the entry already free()d. If you want to stop searching for matches before that case then please call <code>zzip_entry_free</code> on the cursor struct ZZIP_ENTRY. </p>
<pre><code>the
zzip_entry_free
function releases the malloc()ed areas needed for zzip_entry, the pointer is invalid afterwards. The
zzip_entry_free
function has #define synonyms of zzip_entry_findlast(), zzip_entry_findlastfile(), zzip_entry_findlastmatch()</code></pre>
<p> The <code>zzip_entry_findmatch</code> function uses a compare-function with an additional argument and it is called just like <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) from POSIX.2 AD:1993), i.e. the argument filespec first and the ziplocal filename second with the integer-flags put in as third to the indirect call. If the platform has fnmatch available then null-compare will use that one and otherwise we fall back to mere strcmp, so if you need fnmatch searching then please provide an implementation somewhere else. &#8211; use null as argument for &quot;after&quot;-entry when searching the first matching entry, or the last disk_entry return-value to find the next entry matching the given filespec. If no further entry is found then null is returned and any &quot;old&quot;-entry gets already free()d.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2003,2004 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
