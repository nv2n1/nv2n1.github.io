---
title: "dirfile_cbopen(3)"
name: "dirfile_cbopen"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_cbopen/"
description: "dirfile_cbopen, dirfile_open — open or create a dirfile"
---

<h2>NAME</h2>
<p> dirfile_cbopen, dirfile_open &#8212; open or create a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>DIRFILE* dirfile_cbopen(const char *</code><i>dirfilename</i><code>, unsigned long</code> <i>flags</i><code>, gd_parser_callback_t </code><i>sehandler</i><code>, void *</code><i>extra</i><code>);</code></p>
<dt> <code>DIRFILE* dirfile_open(const char *</code><i>dirfilename</i><code>, unsigned long </code><i>flags</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_cbopen</code>() function opens or creates the dirfile specified by <i>dirfilename</i>, returning a DIRFILE object associated with it. Opening a dirfile will cause the library to read and parse the dirfile&#8217;s format file (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)). </p>
<p> If not NULL, <i>sehandler</i> should be a pointer to a function which will be called whenever a syntax error is encountered during parsing the format file. Specify NULL for this parameter if no callback function is to be used. The caller may use this function to correct the error or modify the error handling of the format file parser. See <code>The Callback Function</code> section below for details on this function. The <i>extra</i> argument allows the caller to pass data to the callback function. The pointer will be passed to the callback function verbatim. </p>
<p> The <code>dirfile_open</code>() function is equivalent to <code>dirfile_cbopen</code>(), with <i>sehandler</i> and <i>extra</i> set to NULL. </p>
<p> The <i>flags</i> argument should include one of the <i>access modes</i>: <code>GD_RDONLY</code> (read-only) or <code>GD_RDWR</code> (read-write), and may also contain zero or more of the following flags, bitwise-or&#8217;d together:</p>
<dl>
<dt><code>GD_BIG_ENDIAN</code></p>
<dd> Specifies that raw data on disk is stored as big-endian data (most significant byte first). Specifying this flag along with the contradictory <code>GD_LITTLE_ENDIAN</code> will cause the library to assume that the endianness of the data is opposite to that of the native architecture. </p>
<p> This flag is ignored completely if an <code>ENDIAN</code> directive occurs in the dirfile format file, unless <code>GD_FORCE_ENDIAN</code> is also specified.</p>
<dt><code>GD_CREAT</code></p>
<dd> An empty dirfile will be created, if one does not already exist. This will create both the dirfile directory and an empty format file. The directory will have have mode <code>S_IRWXU</code> | <code>S_IRWXG</code> | <code>S_IRWXO</code> (0777), modified by the caller&#8217;s umask value (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)). The format file will have mode <code>S_IRUSR</code> | <code>S_IWUSR</code> | <code>S_IRGRP</code> | <code>S_IWGRP</code> | <code>S_IROTH</code> | <code>S_IWOTH</code> (0666), also modified by the caller&#8217;s umask. </p>
<p> The owner of the dirfile directory and format file will be the effective user ID of the caller. Group ownership follows the rules outlined in <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2).</p>
<dt><code>GD_EXCL</code></p>
<dd> Ensure that this call creates a dirfile: when specified along with <code>GD_CREAT</code>, the call will fail if the dirfile specified by <i>dirfilename</i> already exists. Behaviour of this flag is undefined if <code>GD_CREAT</code> is not specified. This flag suffers from all the limitations of the <code>O_EXCL</code> flag as indicated in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt><code>GD_FORCE_ENCODING</code></p>
<dd> Specifies that <code>ENCODING</code> directives (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) found in the dirfile format file should be ignored. The encoding scheme specified in <i>flags</i> will be used instead (see below).</p>
<dt><code>GD_FORCE_ENDIAN</code></p>
<dd> Specifies that <code>ENDIAN</code> directives (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) found in the dirfile format file should be ignored. When specified with one of <code>GD_BIG_ENDIAN</code> or <code>GD_LITTLE_ENDIAN</code>, the endianness specified will be assumed. If this flag is specified with neither of those flags, the dirfile will be assumed to have the endianness of the native architecture.</p>
<dt><code>GD_IGNORE_DUPS</code></p>
<dd> If the dirfile format metadata specifies more than one field with the same name, all but one of them will be ignored by the parser. Without this flag, parsing would fail with the <code>GD_E_FORMAT </code> error, possibly resulting in invocation of the registered callback function. Which of the duplicate fields is kept is not specified. As a result, this flag is typically only useful in the case where identical copies of a field specification line are present. </p>
<p> No indication is provided to indicate whether a duplicate field has been discarded. If finer grained control is required, the caller should handle <code>GD_E_FORMAT_DUPLICATE</code> suberrors itself with an appropriate callback function.</p>
<dt><code>GD_LITTLE_ENDIAN</code></p>
<dd> Specifies that raw data on disk is stored as little-endian data (least significant byte first). Specifying this flag along with the contradictory <code>GD_BIG_ENDIAN</code> will cause the library to assume that the endianness of the data is opposite to that of the native architecture. </p>
<p> This flag is ignored completely if an <code>ENDIAN</code> directive occurs in the dirfile format file, unless <code>GD_FORCE_ENDIAN</code> is also specified.</p>
<dt><code>GD_PEDANTIC</code></p>
<dd> Specifies that unrecognised lines found during the parsing of the format file should always cause a fatal error. Without this flag, if a <code>VERSION</code> directive (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) indicates that the dirfile being opened conforms Standards Version newer than the version understood by the library, unrecognised lines will be silently ignored.</p>
<dt><code>GD_PRETTY_PRINT</code></p>
<dd> When dirfile metadata is flushed to disc (either explicitly via <code>dirfile_metaflush()</code> or <code>dirfile_flush()</code> or implicitly by closing the dirfile), an attempt will be made to create a nicer looking format file (from a human-readable standpoint). What this explicitly means is not part of the API, and any particular behaviour should not be relied on. If the dirfile is opened read-only, this flag is ignored.</p>
<dt><code>GD_TRUNC</code></p>
<dd> If <i>dirfilename</i> specifies an already existing dirfile, it will be truncated before opening. Since <code>dirfile_cbopen</code>() decides whether <i>dirfilename</i> specifies an existing dirfile before attempting to parse the dirfile, <i>dirfilename</i> is considered to specify an existing dirfile if it refers to a directory containing a regular file called <code>format</code>, regardless of the content or form of that file. </p>
<p> Truncation occurs by deleting every regular file in the specified directory, whether the files were referred to by the dirfile before truncation or not. Accordingly, this flag should be used with caution. Subdirectories are left untouched. Notably, this operation does not consider the presence of subdirfiles declared by <code>INCLUDE</code> directives. If the dirfile does not exist, this flag is ignored.</p>
<dt><code>GD_VERBOSE</code></p>
<dd> Specifies that whenever an error is triggered by the library when working on this dirfile, the corresponding error string, which can be retrieved by calling <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), should be written on standard error by the library. Without this flag, GetData writes nothing to standard error. (GetData never writes to standard output.) </p>
<p> The <i>flags</i> argument may also be bitwise or&#8217;d with one of the following symbols indicating the default encoding scheme of the dirfile. Like the endianness flags, the choice of encoding here is ignored if the encoding is specified in the dirfile itself, unless <code>GD_FORCE_ENCODED</code> is also specified. If none of these symbols is present, <code>GD_AUTO_ENCODED</code> is assumed, unless the <code>dirfile_cbopen</code>() call results in creation or truncation of the dirfile. In that case, <code>GD_UNENCODED</code> is assumed. See <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5) for details on dirfile encoding schemes.</p>
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
<h3>The Callback Function</h3>
<p> The caller-supplied <i>sehandler</i> function is called whenever the format file parser encounters a syntax error (<i>i.e.</i> whenever it would return the <code>GD_E_FORMAT</code> error). This callback may be used to correct the error, or to tell the parser how to recover from it. </p>
<p> This function should take two pointers as arguments, and return an int:</p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>int </code><i>sehandler</i><code>(gd_parser_data_t *</code><i>pdata</i><code>, void *</code><i>extra</i><code>);</code></dl>
</dl>
<dd>The <i>extra</i> parameter is the pointer supplied to <code>dirfile_cbopen</code>(), passed verbatim to this function. It can be used to pass caller data to the callback. GetData does not inspect this pointer, not even to check its validity. If the caller needs to pass no data to the callback, it may be NULL. </p>
<p> The <code>gd_parser_data_t</code> type is a structure with at least the following members: </p>
<pre><code>
typedef struct {
    const DIRFILE *dirfile;
    int suberror;
    int linenum;
    const char *filename;
    char *line;
    ...
} gd_parser_data_t;
</code></pre>
<p> The <i>pdata</i>-&gt;<i>dirfile</i> member will be a pointer to a DIRFILE object suitable only for passing to <code>get_error_string</code>(). Notably, the caller should not assume this pointer will be the same as the pointer eventually returned by <code>dirfile_cbopen</code>(), nor that it will be valid after the callback function returns. </p>
<p> The <i>pdata</i>-&gt;<i>suberror</i> parameter will be one of the following symbols indicating the type of syntax error encountered:</p>
<dl>
<dt><code>GD_E_FORMAT_BAD_LINE</code></p>
<dd> The line was indecipherable. Typically this means that the line contained neither a reserved word, nor a field type.</p>
<dt><code>GD_E_FORMAT_BAD_NAME</code></p>
<dd> The specified field name was invalid.</p>
<dt><code>GD_E_FORMAT_BAD_SPF</code></p>
<dd> The samples-per-frame of a RAW field was out-of-range.</p>
<dt><code>GD_E_FORMAT_BAD_TYPE</code></p>
<dd> The data type of a RAW field was unrecognised.</p>
<dt><code>GD_E_FORMAT_BITNUM</code></p>
<dd> The first bit of a BIT field was out-of-range.</p>
<dt><code>GD_E_FORMAT_BITSIZE</code></p>
<dd> The last bit of a BIT field was out-of-range.</p>
<dt><code>GD_E_FORMAT_CHARACTER</code></p>
<dd> An invalid character was found in the line, or a character escape sequence was malformed.</p>
<dt><code>GD_E_FORMAT_DUPLICATE</code></p>
<dd> The specified field name already exists.</p>
<dt><code>GD_E_FORMAT_ENDIAN</code></p>
<dd> The byte sex specified by an <code>ENDIAN</code> directive was unrecognised.</p>
<dt><code>GD_E_FORMAT_LITTERAL</code></p>
<dd> An unexpected character was encountered in a complex literal.</p>
<dt><code>GD_E_FORMAT_LOCATION</code></p>
<dd> The parent of a metafield was defined in another fragment.</p>
<dt><code>GD_E_FORMAT_METARAW</code></p>
<dd> An attempt was made to add a RAW metafield.</p>
<dt><code>GD_E_FORMAT_N_FIELDS</code></p>
<dd> The number of fields of a LINCOM field was out-of-range.</p>
<dt><code>GD_E_FORMAT_N_TOK</code></p>
<dd> An insufficient number of tokens was found on the line.</p>
<dt><code>GD_E_FORMAT_NO_PARENT</code></p>
<dd> The parent of a metafield was not found.</p>
<dt><code>GD_E_FORMAT_NUMBITS</code></p>
<dd> The number of bits of a BIT field was out-of-range.</p>
<dt><code>GD_E_FORMAT_PROTECT</code></p>
<dd> The protection level specified by a <code>PROTECT</code> directive was unrecognised.</p>
<dt><code>GD_E_FORMAT_RES_NAME</code></p>
<dd> A field was specified with the reserved name <i>INDEX</i>.</p>
<dt><code>GD_E_FORMAT_UNTERM</code></p>
<dd> The last token of the line was unterminated.</dl>
<p> <i>pdata</i>-&gt;<i>filename</i> and <i>pdata</i>-&gt;<i>linenum</i> members contains the name of the fragment and line number where the syntax error was encountered. The first line in a fragment is line one. </p>
<p> The <i>pdata</i>-&gt;<i>line</i> member contains a copy of the line containing the syntax error. This line may be freely modified by the callback function. It will then be reparsed if the callback function returns the symbol <code>GD_SYNTAX_RESCAN</code> (see below). Space is available for at least GD_MAX_LINE_LENGTH characters, including the terminating NUL. </p>
<p> The callback function should return one of the following symbols, which tells the parser how to subsequently handle the error:</p>
<dl>
<dt><code>GD_SYNTAX_ABORT</code></p>
<dd> The parser should immediately abort parsing the format file and fail with the error <code>GD_E_FORMAT</code>. This is the default behaviour, if no callback function is provided (or if the parser is invoked by calling <code>dirfile_open</code>()).</p>
<dt><code>GD_SYNTAX_CONTINUE</code></p>
<dd> The parser should continue parsing the format file. However, once parsing has finished, the parser will fail with the error <code>GD_E_FORMAT</code>, even if no further syntax errors are encountered. This behaviour may be used by the caller to identify all lines containing syntax errors in the format file, instead of just the first one.</p>
<dt><code>GD_SYNTAX_IGNORE</code></p>
<dd> The parser should ignore the line containing the syntax error completely, and carry on parsing the format file. If no further errors are encountered, the dirfile will be successfully opened.</p>
<dt><code>GD_SYNTAX_RESCAN</code></p>
<dd> The parser should rescan the <i>line</i> argument, which replaces the line which originally contained the syntax error. The line is assumed to have been corrected by the callback function. If the line still contains a syntax error, the callback function will be called again. The callback function handles only syntax errors. The parser may still abort early, if a different kind of library error is encountered. Furthermore, although a line may contain more than one syntax error, the parser will only ever report one syntax error per line, even if the callback function returns <code>GD_SYNTAX_CONTINUE</code>. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> A call to <code>dirfile_cbopen</code>() or <code>dirfile_open</code>() always returns a pointer to a newly allocated DIRFILE object. The DIRFILE object is an opaque structure containing the parsed dirfile metadata. If an error occurred, the dirfile error will be set to a non-zero error value. The DIRFILE object will also be internally flagged as invalid. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The library was asked to create or truncate a dirfile opened read-only (i.e. <code>GD_CREAT</code> or <code>GD_TRUNC</code> was specified in <i>flags</i> along with <code>GD_RDONLY</code>).</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_REFERENCE</code></p>
<dd> The reference field specified by a <code>/REFERENCE</code> directive in the format file (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)) was not found, or was not a <code>RAW</code> field.</p>
<dt><code>GD_E_CALLBACK</code></p>
<dd> The registered callback function, <i>sehandler</i>, returned an unrecognised response.</p>
<dt><code>GD_E_CREAT</code></p>
<dd> The library was unable to create the dirfile, or the dirfile exists and both <code>GD_CREAT</code> and <code>GD_EXCL</code> were specified.</p>
<dt><code>GD_E_FORMAT</code></p>
<dd> A syntax error occurred in the format file. See also <code>The Callback Function</code> section above.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the GetData developers.</p>
<dt><code>GD_E_OPEN</code></p>
<dd> The dirfile format file could not be opened, or <i>dirfilename</i> does not specify a valid dirfile.</p>
<dt><code>GD_E_OPEN_INCLUDE</code></p>
<dd> A file specified in an <code>/INCLUDE</code> directive could not be opened.</p>
<dt><code>GD_E_TRUNC</code></p>
<dd> The library was unable to truncate the dirfile. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). When finished with it, the DIRFILE object should be deallocated with a call to <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3), even if the open failed.</dl>
<h2>BUGS</h2>
<p> GetData&#8217;s parser assumes it is running on an ASCII-compatible platform. Format file parsing will fail gloriously on an EBCDIC platform.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_parser_callback/">dirfile_parser_callback</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
