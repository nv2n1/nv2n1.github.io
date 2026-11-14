---
title: "dirfile_include(3)"
name: "dirfile_include"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_include/"
description: "dirfile_include — add a format file fragment to a dirfile"
---

<h2>NAME</h2>
<p> dirfile_include &#8212; add a format file fragment to a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_include(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>include_file</i><code>,</code> <code>int </code><i>parent_fragment</i><code>, unsigned long </code><i>flags</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_include</code>() adds the format file fragment specified by the path <i>include_file</i> to the specified dirfile, possibly creating the fragment. This occurs as if, in the existing fragment indexed by <i>parent_fragment</i>, the following directive were present:</p>
<dl>
<dt>
<dd> <code>/INCLUDE </code><i>&lt;include_file&gt;</i> (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)). If a parser callback function had been specified when the dirfile was opened using <code><a href="/docs/linux/man/3-dirfile_cbopen/">dirfile_cbopen</a></code>(3), or added later with <code><a href="/docs/linux/man/3-dirfile_parser_callback/">dirfile_parser_callback</a></code>(3), this callback function will be called if a syntax error is encountered while parsing the included fragment. </p>
<p> The <i>flags</i> argument should be a bitwise-or&#8217;d collection of the following flags, or zero if no flags are desired:</p>
<dt><code>GD_BIG_ENDIAN</code></p>
<dd> Specifies that raw data on disk is stored as big-endian data (most significant byte first). Specifying this flag along with the contradictory <code>GD_LITTLE_ENDIAN</code> will cause the library to assume that the endianness of the data is opposite to that of the native architecture. </p>
<p> This flag is ignored completely if an <code>ENDIAN</code> directive occurs in the fragment, unless <code>GD_FORCE_ENDIAN</code> is also specified.</p>
<dt><code>GD_CREAT</code></p>
<dd> An empty fragment will be created, if one does not already exist. The fragment will have mode <code>S_IRUSR</code> | <code>S_IWUSR</code> | <code>S_IRGRP</code> | <code>S_IWGRP</code> | <code>S_IROTH</code> | <code>S_IWOTH</code> (0666), modified by the caller&#8217;s umask value (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)).</p>
<dt><code>GD_EXCL</code></p>
<dd> Ensure that this call creates a new fragment: when specified along with <code>GD_CREAT</code>, the call will fail if the file specified by <i>include_file</i> already exists. Behaviour of this flag is undefined if <code>GD_CREAT</code> is not specified. This flag suffers from all the limitations of the <code>O_EXCL</code> flag as indicated in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt><code>GD_FORCE_ENCODING</code></p>
<dd> Specifies that <code>ENCODING</code> directives (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) found in the fragment should be ignored. The encoding scheme specified in <i>flags</i> will be used instead (see below).</p>
<dt><code>GD_FORCE_ENDIAN</code></p>
<dd> Specifies that <code>ENDIAN</code> directives (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) found in the fragment should be ignored. When specified with one of <code>GD_BIG_ENDIAN</code> or <code>GD_LITTLE_ENDIAN</code>, the endianness specified will be assumed. If this flag is specified with neither of those flags, the fragment will be assumed to have the endianness of the native architecture.</p>
<dt><code>GD_IGNORE_DUPS</code></p>
<dd> If the fragment specifies more than one field with the same name, or a field with the same name as an existing field, all but one of them will be ignored by the parser. Without this flag, parsing would fail with the <code>GD_E_FORMAT </code> error, possibly resulting in invocation of the registered callback function. Which of the duplicate fields is kept is not specified, nor whether an existing field takes precedence over a new one or not. As a result, this flag is typically only useful in the case where identical copies of a field specification line are present. </p>
<p> No indication is provided to indicate whether a duplicate field has been discarded. If finer grained control is required, the caller should handle <code>GD_E_FORMAT_DUPLICATE</code> suberrors itself with an appropriate callback function.</p>
<dt><code>GD_IGNORE_REFS</code></p>
<dd> If the dirfile currently has a reference field (either because one was specified explicitly, or else because the first <code>RAW</code> field was used), <code>/REFERENCE</code> directives in the included fragment will be ignored. Otherwise, a <code>/REFERENCE</code> directive in the included fragment will replace the current reference field in the dirfile.</p>
<dt><code>GD_LITTLE_ENDIAN</code></p>
<dd> Specifies that raw data on disk is stored as little-endian data (least significant byte first). Specifying this flag along with the contradictory <code>GD_BIG_ENDIAN</code> will cause the library to assume that the endianness of the data is opposite to that of the native architecture. </p>
<p> This flag is ignored completely if an <code>ENDIAN</code> directive occurs in the fragment, unless <code>GD_FORCE_ENDIAN</code> is also specified.</p>
<dt><code>GD_PEDANTIC</code></p>
<dd> Specifies that unrecognised lines found during the parsing of the fragment should always cause a fatal error. Without this flag, if a <code>VERSION</code> directive (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) indicates that the fragment being opened conforms Standards Version newer than the version understood by the library, unrecognised lines will be silently ignored.</p>
<dt><code>GD_TRUNC</code></p>
<dd> If <i>include_file</i> already exists, it will be truncated before opening. If the file does not exist, this flag is ignored. </p>
<p> The <i>flags</i> argument may also be bitwise or&#8217;d with one of the following symbols indicating the default encoding scheme of the fragment. Like the endianness flags, the choice of encoding here is ignored if the encoding is specified in the fragment itself, unless <code>GD_FORCE_ENCODED</code> is also specified. If none of these symbols is present, <code>GD_AUTO_ENCODED</code> is assumed, unless the <code>dirfile_include</code>() call results in creation or truncation of the fragment. In that case, <code>GD_UNENCODED</code> is assumed. See <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5) for details on dirfile encoding schemes.</p>
<dt><code>GD_AUTO_ENCODED</code></p>
<dd> Specifies that the encoding type is not known in advance, but should be detected by the GetData library. Detection is accomplished by searching for raw data files with extensions appropriate to the encoding scheme. This method will notably fail if the the library is called via <code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3) to create a previously non-existent raw field unless a read is first successfully performed on the dirfile. Once the library has determined the encoding scheme for the first time, it remembers it for subsequent calls.</p>
<dt><code>GD_BZIP2_ENDODED</code></p>
<dd> Specifies that raw data files are compressed using the Burrows-Wheeler block sorting text compression algorithm and Huffman coding, as implemented in the bzip2 format.</p>
<dt><code>GD_GZIP_ENDODED</code></p>
<dd> Specifies that raw data files are compressed using Lempel-Ziv coding (LZ77) as implemented in the gzip format.</p>
<dt><code>GD_LZMA_ENDODED</code></p>
<dd> Specifies that raw data files are compressed using the Lempel-Ziv Markov Chain Algorithm (LZMA) as implemented in the xz container format.</p>
<dt><code>GD_SLIM_ENCODED</code></p>
<dd> Specifies that raw data files are compressed using the slimlib library.</p>
<dt><code>GD_TEXT_ENCODED</code></p>
<dd> Specifies that raw data files are encoded as text files containing one data sample per line.</p>
<dt><code>GD_UNENCODED</code></p>
<dd> Specifies that raw data files are not encoded, but written verbatim to disk. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_include</code>() returns the format file index of the newly added fragment. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The supplied dirfile was opened in read-only mode.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied parent fragment index was out of range.</p>
<dt><code>GD_E_BAD_REFERENCE</code></p>
<dd> The reference field specified by a <code>/REFERENCE</code> directive in the fragment (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) was not found, or was not a <code>RAW</code> field.</p>
<dt><code>GD_E_CALLBACK</code></p>
<dd> The registered callback function returned an unrecognised response.</p>
<dt><code>GD_E_FORMAT</code></p>
<dd> A syntax error occurred in the fragment.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_OPEN_INCLUDE</code></p>
<dd> The fragment could not be opened or created.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the parent fragment was protected from change.</p>
<dt><code>GD_E_REFERENCE</code></p>
<dd> The included fragment contained a <code>/REFERENCE</code> directive which referred to a non-existent field, or a field that was not of type <code>RAW</code>. In this case, the included fragment will still be added to the dirfile, but the <code>/REFERENCE</code> directive will be ignored. See also the <code>BUGS</code> section below. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). When finished with it, the DIRFILE object may be deallocated with a call to <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3), even if the open failed.</dl>
<h2>BUGS</h2>
<p> If this function fails with the error <code>GD_E_REFERENCE</code>, it typically results in no reference field being defined for the dirfile, even if the dirfile contains <code>RAW</code> fields. As a result, functions which rely on the reference field, such as <code><a href="/docs/linux/man/3-get_nframes/">get_nframes</a></code>(3), will operate incorrectly. Callers should explicitly set the reference field with <code><a href="/docs/linux/man/3-dirfile_reference/">dirfile_reference</a></code>(3) in this case.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_parser_callback/">dirfile_parser_callback</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_reference/">dirfile_reference</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_uninclude/">dirfile_uninclude</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_fragmentname/">get_fragmentname</a></code>(3), <code><a href="/docs/linux/man/3-get_nfragments/">get_nfragments</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
