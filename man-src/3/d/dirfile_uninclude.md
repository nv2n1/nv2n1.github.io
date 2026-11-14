---
title: "dirfile_uninclude(3)"
name: "dirfile_uninclude"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_uninclude/"
description: "dirfile_uninclude — remove a format file fragment from a dirfile"
---

<h2>NAME</h2>
<p> dirfile_uninclude &#8212; remove a format file fragment from a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int *dirfile_uninclude(DIRFILE *</code><i>dirfile</i><code>, int </code><i>fragment_index</i><code>,</code> <code>int </code><i>del</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_uninclude</code>() removes the format file fragment indexed by <i>fragment_index</i> from the specified dirfile, as well as any fragments the specified fragment INCLUDEs. Fields defined in the removed fragments will be removed from the dirfile. </p>
<p> Before removing the specified fragment, all pending writes are flushed to <code>RAW</code> fields defined the the removed fragments. If <i>del</i> is zero, metadata changes will also be written to the removed fragments. If <i>del</i> is non-zero, the format file fragments will be deleted from disk, if possible. Regardless of the value of <i>del</i>, binary data files associated with <code>RAW</code> fields defined in the removed fragments will not be deleted. To delete these binary files, use <code><a href="/docs/linux/man/3-dirfile_delete/">dirfile_delete</a></code>(3) before calling this function. </p>
<p> The primary format file (the fragment indexed by zero) cannot be removed from the dirfile.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_uninclude</code>() returns zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The supplied dirfile was opened in read-only mode.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied fragment index was out of range, or an attempt was made to remove the primary format file.</p>
<dt><code>GD_E_OPEN_INCLUDE</code></p>
<dd> A temporary file could not be opened into which to write the metadata of a modified, removed fragment.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the fragment which included the removed fragment was protected from change.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An error occurred while trying to flush or close a removed field. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). When finished with it, the DIRFILE object may be deallocated with a call to <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3), even if the open failed.</dl>
<h2>NOTES</h2>
<p> This function re-arranges the remaining format file fragments in some unspecified way, except for the primary fragment, which is guaranteed to remain at index zero. Callers which cache format file fragment indices must re-initialise their cache after calling this function. </p>
<p> Unlike <code><a href="/docs/linux/man/3-dirfile_delete/">dirfile_delete</a></code>(3), fields which depend on fields removed by this function are not automatically updated, nor is any check made to ensure that this function does not leave fields with missing input fields. Because of this, a fragment inclusion may be easily moved from one fragment to another with a combination of <code>dirfile_uninclude</code>() and <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3). However, if such checks are required, use <code><a href="/docs/linux/man/3-dirfile_delete/">dirfile_delete</a></code>(3) to delete the fields defined in the removed fragments first.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_delete/">dirfile_delete</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_reference/">dirfile_reference</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_fragmentname/">get_fragmentname</a></code>(3), <code><a href="/docs/linux/man/3-get_nfragments/">get_nfragments</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
