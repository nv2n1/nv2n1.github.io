---
title: "tcl_zlibstreamchecksum(3)"
name: "tcl_zlibstreamchecksum"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_zlibstreamchecksum/"
description: "Tcl_ZlibAdler32, Tcl_ZlibCRC32, Tcl_ZlibDeflate, Tcl_ZlibInflate, Tcl_ZlibStreamChecksum, Tcl_ZlibStreamClose, Tcl_ZlibStreamEof, Tcl_ZlibStreamGet, Tcl_ZlibStreamGetCommandName, Tcl_ZlibStreamInit..."
---

<p>Tcl_ZlibAdler32, Tcl_ZlibCRC32, Tcl_ZlibDeflate, Tcl_ZlibInflate, Tcl_ZlibStreamChecksum, Tcl_ZlibStreamClose, Tcl_ZlibStreamEof, Tcl_ZlibStreamGet, Tcl_ZlibStreamGetCommandName, Tcl_ZlibStreamInit, Tcl_ZlibStreamPut &#8211; compression and decompression functions </p>
<h2>Synopsis</h2>
<pre>#include &lt;tcl.h&gt;
int
<code>Tcl_ZlibDeflate</code>(<i>interp, format, dataObj, level, dictObj</i>)
int
<code>Tcl_ZlibInflate</code>(<i>interp, format, dataObj, dictObj</i>)
unsigned int
<code>Tcl_ZlibCRC32</code>(<i>initValue, bytes, length</i>)
unsigned int
<code>Tcl_ZlibAdler32</code>(<i>initValue, bytes, length</i>)
int
<code>Tcl_ZlibStreamInit</code>(<i>interp, mode, format, level, dictObj, zshandlePtr</i>)
Tcl_Obj *
<code>Tcl_ZlibStreamGetCommandName</code>(<i>zshandle</i>)
int
<code>Tcl_ZlibStreamEof</code>(<i>zshandle</i>)
int
<code>Tcl_ZlibStreamClose</code>(<i>zshandle</i>)
int
<code>Tcl_ZlibStreamReset</code>(<i>zshandle</i>)
int
<code>Tcl_ZlibStreamChecksum</code>(<i>zshandle</i>)
int
<code>Tcl_ZlibStreamPut</code>(<i>zshandle, dataObj, flush</i>)
int
<code>Tcl_ZlibStreamGet</code>(<i>zshandle, dataObj, count</i>)
<code>Tcl_ZlibStreamSetCompressionDictionary</code>(<i>zshandle, compDict</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) The interpreter to store resulting compressed or uncompressed data in. Also where any error messages are written. For <code>Tcl_ZlibStreamInit</code>, this can be NULL to create a stream that is not bound to a command.</p>
<dd>int <i>format</i> (in) What format of compressed data to work with. Must be one of <code>TCL_ZLIB_FORMAT_ZLIB</code> for zlib-format data, <code>TCL_ZLIB_FORMAT_GZIP</code> for gzip-format data, or <code>TCL_ZLIB_FORMAT_RAW</code> for raw compressed data. In addition, for decompression only, <code>TCL_ZLIB_FORMAT_AUTO</code> may also be chosen which can automatically detect whether the compressed data was in zlib or gzip format.</p>
<dd>Tcl_Obj <i>*dataObj</i> (in/out) A byte-array value containing the data to be compressed or decompressed, or to which the data extracted from the stream is appended when passed to <code>Tcl_ZlibStreamGet</code>.</p>
<dd>int <i>level</i> (in) What level of compression to use. Should be a number from 0 to 9 or one of the following: <code>TCL_ZLIB_COMPRESS_NONE</code> for no compression, <code>TCL_ZLIB_COMPRESS_FAST</code> for fast but inefficient compression, <code>TCL_ZLIB_COMPRESS_BEST</code> for slow but maximal compression, or <code>TCL_ZLIB_COMPRESS_DEFAULT</code> for the level recommended by the zlib library.</p>
<dd>Tcl_Obj <i>*dictObj</i> (in/out) A dictionary that contains, or which will be updated to contain, a description of the gzip header associated with the compressed data. Only useful when the <i>format</i> is <code>TCL_ZLIB_FORMAT_GZIP</code> or <code>TCL_ZLIB_FORMAT_AUTO</code>. If a NULL is passed, a default header will be used on compression and the header will be ignored (apart from integrity checks) on decompression. See the section <code>GZIP OPTIONS DICTIONARY</code> for details about the contents of this dictionary.</p>
<dd>unsigned int <i>initValue</i> (in) The initial value for the checksum algorithm.</p>
<dd>unsigned char <i>*bytes</i> (in) An array of bytes to run the checksum algorithm over, or NULL to get the recommended initial value for the checksum algorithm.</p>
<dd>int <i>length</i> (in) The number of bytes in the array.</p>
<dd>int <i>mode</i> (in) What mode to operate the stream in. Should be either <code>TCL_ZLIB_STREAM_DEFLATE</code> for a compressing stream or <code>TCL_ZLIB_STREAM_INFLATE</code> for a decompressing stream.</p>
<dd>Tcl_ZlibStream <i>*zshandlePtr</i> (out) A pointer to a variable in which to write the abstract token for the stream upon successful creation.</p>
<dd>Tcl_ZlibStream <i>zshandle</i> (in) The abstract token for the stream to operate on.</p>
<dd>int <i>flush</i> (in) Whether and how to flush the stream after writing the data to it. Must be one of: <code>TCL_ZLIB_NO_FLUSH</code> if no flushing is to be done, <code>TCL_ZLIB_FLUSH</code> if the currently compressed data must be made available for access using <code>Tcl_ZlibStreamGet</code>, <code>TCL_ZLIB_FULLFLUSH</code> if the stream must be put into a state where the decompressor can recover from on corruption, or <code>TCL_ZLIB_FINALIZE</code> to ensure that the stream is finished and that any trailer demanded by the format is written.</p>
<dd>int <i>count</i> (in) The maximum number of bytes to get from the stream, or -1 to get all remaining bytes from the stream&#8217;s buffers.</p>
<dd>Tcl_Obj <i>*compDict</i> (in) A byte array value that is the compression dictionary to use with the stream. Note that this is <i>not a Tcl dictionary</i>, and it is recommended that this only ever be used with streams that were created with their <i>format</i> set to <code>TCL_ZLIB_FORMAT_ZLIB</code> because the other formats have no mechanism to indicate whether a compression dictionary was present other than to fail on decompression.
</dl>
<h2>Description</h2>
<p>These functions form the interface from the Tcl library to the Zlib library by Jean-loup Gailly and Mark Adler. </p>
<p> <code>Tcl_ZlibDeflate</code> and <code>Tcl_ZlibInflate</code> respectively compress and decompress the data contained in the <i>dataObj</i> argument, according to the <i>format</i> and, for compression, <i>level</i> arguments. The dictionary in the <i>dictObj</i> parameter is used to convey additional header information about the compressed data when the compression format supports it; currently, the dictionary is only used when the <i>format</i> parameter is <code>TCL_ZLIB_FORMAT_GZIP</code> or <code>TCL_ZLIB_FORMAT_AUTO</code>. For details of the contents of the dictionary, see the <code>GZIP OPTIONS DICTIONARY</code> section below. Upon success, both functions leave the resulting compressed or decompressed data in a byte-array value that is the Tcl interpreter&#8217;s result; the returned value is a standard Tcl result code. </p>
<p> <code>Tcl_ZlibAdler32</code> and <code>Tcl_ZlibCRC32</code> compute checksums on arrays of bytes, returning the computed checksum. Checksums are computed incrementally, allowing data to be processed one block at a time, but this requires the caller to maintain the current checksum and pass it in as the <i>initValue</i> parameter; the initial value to use for this can be obtained by using NULL for the <i>bytes</i> parameter instead of a pointer to the array of bytes to compute the checksum over. Thus, typical usage in the single data block case is like this: </p>
<dl COMPACT>
<dd>
<pre>checksum = <code>Tcl_ZlibCRC32</code>(<code>Tcl_ZlibCRC32</code>(0,NULL,0), data, length);</pre>
</dl>
<p> Note that the Adler-32 algorithm is not a real checksum, but instead is a related type of hash that works best on longer data.</p>
<h3>Zlib Streams</h3>
<p><code>Tcl_ZlibStreamInit</code> creates a compressing or decompressing stream that is linked to a Tcl command, according to its arguments, and provides an abstract token for the stream and returns a normal Tcl result code; <code>Tcl_ZlibStreamGetCommandName</code> returns the name of that command given the stream token, or NULL if the stream has no command. Streams are not designed to be thread-safe; each stream should only ever be used from the thread that created it. When working with gzip streams, a dictionary (fields as given in the <code>GZIP OPTIONS DICTIONARY</code> section below) can be given via the <i>dictObj</i> parameter that on compression allows control over the generated headers, and on decompression allows discovery of the existing headers. Note that the dictionary will be written to on decompression once sufficient data has been read to have a complete header. This means that the dictionary must be an unshared value in that case; a blank value created with <code>Tcl_NewObj</code> is suggested. </p>
<p> Once a stream has been constructed, <code>Tcl_ZlibStreamPut</code> is used to add data to the stream and <code>Tcl_ZlibStreamGet</code> is used to retrieve data from the stream after processing. Both return normal Tcl result codes and leave an error message in the result of the interpreter that the stream is registered with in the error case (if such a registration has been performed). With <code>Tcl_ZlibStreamPut</code>, the data buffer value passed to it should not be modified afterwards. With <code>Tcl_ZlibStreamGet</code>, the data buffer value passed to it will have the data bytes appended to it. Internally to the stream, data is kept compressed so as to minimize the cost of buffer space. </p>
<p> <code>Tcl_ZlibStreamChecksum</code> returns the checksum computed over the uncompressed data according to the format, and <code>Tcl_ZlibStreamEof</code> returns a boolean value indicating whether the end of the uncompressed data has been reached. </p>
<p> <code>Tcl_ZlibStreamSetCompressionDictionary</code> is used to control the compression dictionary used with the stream, a compression dictionary being an array of bytes (such as might be created with <code>Tcl_NewByteArrayObj</code>) that is used to initialize the compression engine rather than leaving it to create it on the fly from the data being compressed. Setting a compression dictionary allows for more efficient compression in the case where the start of the data is highly regular, but it does require both the compressor and the decompressor to agreee on the value to use. Compression dictionaries are only fully supported for zlib-format data; on compression, they must be set before any data is sent in with <code>Tcl_ZlibStreamPut</code>, and on decompression they should be set when <code>Tcl_ZlibStreamGet</code> produces an <code>error</code> with its <code>-errorcode</code> set to &#8220;<code>ZLIB NEED_DICT</code><i> code</i>&#8221;; the <i>code</i> will be the Adler-32 checksum (see <code>Tcl_ZlibAdler32</code>) of the compression dictionary sought. (Note that this is only true for zlib-format streams; gzip streams ignore compression dictionaries as the format specification doesn&#8217;t permit them, and raw streams just produce a data error if the compression dictionary is missing or incorrect.) </p>
<p> If you wish to clear a stream and reuse it for a new compression or decompression action, <code>Tcl_ZlibStreamReset</code> will do this and return a normal Tcl result code to indicate whether it was successful; if the stream is registered with an interpreter, an error message will be left in the interpreter result when this function returns TCL_ERROR. Finally, <code>Tcl_ZlibStreamClose</code> will clean up the stream and delete the associated command: using <code>Tcl_DeleteCommand</code> on the stream&#8217;s command is equivalent (when such a command exists).</p>
<h2>Gzip Options Dictionary</h2>
<p>The <i>dictObj</i> parameter to <code>Tcl_ZlibDeflate</code>, <code>Tcl_ZlibInflate</code> and <code>Tcl_ZlibStreamInit</code> is used to pass a dictionary of options about that is used to describe the gzip header in the compressed data. When creating compressed data, the dictionary is read and when unpacking compressed data the dictionary is written (in which case the <i>dictObj</i> parameter must refer to an unshared dictionary value). </p>
<p> The following fields in the dictionary value are understood. All other fields are ignored. No field is required when creating a gzip-format stream.</p>
<dl COMPACT>
<dt><code>comment</code></p>
<dd>This holds the comment field of the header, if present. If absent, no comment was supplied (on decompression) or will be created (on compression).</p>
<dt><code>crc</code></p>
<dd>A boolean value describing whether a CRC of the header is computed. Note that the <code>gzip</code> program does <i>not</i> use or allow a CRC on the header.</p>
<dt><code>filename</code></p>
<dd>The name of the file that held the uncompressed data. This should not contain any directory separators, and should be sanitized before use on decompression with <code>file tail</code>.</p>
<dt><code>os</code></p>
<dd>The operating system type code field from the header (if not the &#8220;unknown&#8221; value). See RFC 1952 for the meaning of these codes. On compression, if this is absent then the field will be set to the &#8220;unknown&#8221; value.</p>
<dt><code>size</code></p>
<dd>The size of the uncompressed data. This is ignored on compression; the size of the data compressed depends on how much data is supplied to the compression engine.</p>
<dt><code>time</code></p>
<dd>The time field from the header if non-zero, expected to be the time that the file named by the <code>filename</code> field was modified. Suitable for use with <code>clock format</code>. On creation, the right value to use is that from <code>clock seconds</code> or <code>file mtime</code>.</p>
<dt><code>type</code></p>
<dd>The type of the uncompressed data (either <code>binary</code> or <code>text</code>) if known.</dl>
<h2>Portability Notes</h2>
<p>These functions will fail gracefully if Tcl is not linked with the zlib library.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_newbytearrayobj/">Tcl_NewByteArrayObj</a>(3), <a href="/docs/linux/man/n-zlib/">zlib</a>(n)</p>
<h2>Keywords</h2>
<p>compress, decompress, deflate, gzip, inflate</p>
