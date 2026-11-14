---
title: "pcre2serialize(3)"
name: "pcre2serialize"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2serialize/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Saving And Re-Using Precompiled Pcre2 Patterns</h2>
<pre><code>int32_t pcre2_serialize_decode(pcre2_code **</code><i>codes</i>,
<code> int32_t </code><i>number_of_codes</i>, const uint32_t *<i>bytes</i>,
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>int32_t pcre2_serialize_encode(pcre2_code **</code><i>codes</i>,
<code> int32_t </code><i>number_of_codes</i>, uint32_t **<i>serialized_bytes</i>,
<code> PCRE2_SIZE *</code><i>serialized_size</i>, pcre2_general_context *<i>gcontext</i>);
<code>void pcre2_serialize_free(uint8_t *</code><i>bytes</i>);
<code>int32_t pcre2_serialize_get_number_of_codes(const uint8_t *</code><i>bytes</i>);</pre>
<p>If you are running an application that uses a large number of regular expression patterns, it may be useful to store them in a precompiled form instead of having to compile them every time the application is run. However, if you are using the just-in-time optimization feature, it is not possible to save and reload the JIT data, because it is position-dependent. The host on which the patterns are reloaded must be running the same version of PCRE2, with the same code unit width, and must also have the same endianness, pointer width and PCRE2_SIZE type. For example, patterns compiled on a 32-bit system using PCRE2&#8217;s 16-bit library cannot be reloaded on a 64-bit system, nor can they be reloaded using the 8-bit library. </p>
<p> Note that &quot;serialization&quot; in PCRE2 does not convert compiled patterns to an abstract format like Java or .NET serialization. The serialized output is really just a bytecode dump, which is why it can only be reloaded in the same environment as the one that created it. Hence the restrictions mentioned above. Applications that are not statically linked with a fixed version of PCRE2 must be prepared to recompile patterns from their sources, in order to be immune to PCRE2 upgrades.</p>
<h2>Security Concerns</h2>
<p>The facility for saving and restoring compiled patterns is intended for use within individual applications. As such, the data supplied to <code>pcre2_serialize_decode()</code> is expected to be trusted data, not data from arbitrary external sources. There is only some simple consistency checking, not complete validation of what is being re-loaded. Corrupted data may cause undefined results. For example, if the length field of a pattern in the serialized data is corrupted, the deserializing code may read beyond the end of the byte stream that is passed to it.</p>
<h2>Saving Compiled Patterns</h2>
<p>Before compiled patterns can be saved they must be serialized, which in PCRE2 means converting the pattern to a stream of bytes. A single byte stream may contain any number of compiled patterns, but they must all use the same character tables. A single copy of the tables is included in the byte stream (its size is 1088 bytes). For more details of character tables, see the section on locale support in the <code>pcre2api</code> documentation. </p>
<p> The function <code>pcre2_serialize_encode()</code> creates a serialized byte stream from a list of compiled patterns. Its first two arguments specify the list, being a pointer to a vector of pointers to compiled patterns, and the length of the vector. The third and fourth arguments point to variables which are set to point to the created byte stream and its length, respectively. The final argument is a pointer to a general context, which can be used to specify custom memory mangagement functions. If this argument is NULL, <code>malloc()</code> is used to obtain memory for the byte stream. The yield of the function is the number of serialized patterns, or one of the following negative error codes: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADDATA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the number of patterns is zero or less<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch of id bytes in one of the patterns<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_MEMORY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory allocation failed<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_MIXEDTABLES&nbsp;<wbr>&nbsp;the patterns do not all use the same tables<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the 1st, 3rd, or 4th argument is NULL </p>
<p> PCRE2_ERROR_BADMAGIC means either that a pattern&#8217;s code has been corrupted, or that a slot in the vector does not point to a compiled pattern. </p>
<p> Once a set of patterns has been serialized you can save the data in any appropriate manner. Here is sample code that compiles two patterns and writes them to a file. It assumes that the variable <i>fd</i> refers to a file that is open for output. The error checking that should be present in a real application has been omitted for simplicity. </p>
<p>&nbsp;<wbr>&nbsp;int errorcode;<br />
&nbsp;<wbr>&nbsp;uint8_t&nbsp;*bytes;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE erroroffset;<br />
&nbsp;<wbr>&nbsp;PCRE2_SIZE bytescount;<br />
&nbsp;<wbr>&nbsp;pcre2_code&nbsp;*list_of_codes[2];<br />
&nbsp;<wbr>&nbsp;list_of_codes[0]&nbsp;=&nbsp;pcre2_compile(&quot;first pattern&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_ZERO_TERMINATED, 0,&nbsp;&amp;errorcode,&nbsp;&amp;erroroffset, NULL);<br />
&nbsp;<wbr>&nbsp;list_of_codes[1]&nbsp;=&nbsp;pcre2_compile(&quot;second pattern&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_ZERO_TERMINATED, 0,&nbsp;&amp;errorcode,&nbsp;&amp;erroroffset, NULL);<br />
&nbsp;<wbr>&nbsp;errorcode&nbsp;=&nbsp;pcre2_serialize_encode(list_of_codes, 2,&nbsp;&amp;bytes,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;bytescount, NULL);<br />
&nbsp;<wbr>&nbsp;errorcode&nbsp;=&nbsp;fwrite(bytes, 1, bytescount, fd); </p>
<p> Note that the serialized data is binary data that may contain any of the 256 possible byte values. On systems that make a distinction between binary and non-binary data, be sure that the file is opened for binary output. </p>
<p> Serializing a set of patterns leaves the original data untouched, so they can still be used for matching. Their memory must eventually be freed in the usual way by calling <code>pcre2_code_free()</code>. When you have finished with the byte stream, it too must be freed by calling <code>pcre2_serialize_free()</code>. If this function is called with a NULL argument, it returns immediately without doing anything.</p>
<h2>Re-Using Precompiled Patterns</h2>
<p>In order to re-use a set of saved patterns you must first make the serialized byte stream available in main memory (for example, by reading from a file). The management of this memory block is up to the application. You can use the <code>pcre2_serialize_get_number_of_codes()</code> function to find out how many compiled patterns are in the serialized data without actually decoding the patterns: </p>
<p>&nbsp;<wbr>&nbsp;uint8_t&nbsp;*bytes&nbsp;=&nbsp;&lt;serialized data&gt;;<br />
&nbsp;<wbr>&nbsp;int32_t number_of_codes&nbsp;=&nbsp;pcre2_serialize_get_number_of_codes(bytes); </p>
<p> The <code>pcre2_serialize_decode()</code> function reads a byte stream and recreates the compiled patterns in new memory blocks, setting pointers to them in a vector. The first two arguments are a pointer to a suitable vector and its length, and the third argument points to a byte stream. The final argument is a pointer to a general context, which can be used to specify custom memory mangagement functions for the decoded patterns. If this argument is NULL, <code>malloc()</code> and <code>free()</code> are used. After deserialization, the byte stream is no longer needed and can be discarded. </p>
<p>&nbsp;<wbr>&nbsp;int32_t number_of_codes;<br />
&nbsp;<wbr>&nbsp;pcre2_code&nbsp;*list_of_codes[2];<br />
&nbsp;<wbr>&nbsp;uint8_t&nbsp;*bytes&nbsp;=&nbsp;&lt;serialized data&gt;;<br />
&nbsp;<wbr>&nbsp;int32_t number_of_codes&nbsp;=<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcre2_serialize_decode(list_of_codes, 2, bytes, NULL); </p>
<p> If the vector is not large enough for all the patterns in the byte stream, it is filled with those that fit, and the remainder are ignored. The yield of the function is the number of decoded patterns, or one of the following negative error codes: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADDATA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;second argument is zero or less<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch of id bytes in the data<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMODE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch of code unit size or PCRE2 version<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADSERIALIZEDDATA&nbsp;<wbr>&nbsp;other sanity check failure<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_MEMORY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory allocation failed<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first or third argument is NULL </p>
<p> PCRE2_ERROR_BADMAGIC may mean that the data is corrupt, or that it was compiled on a system with different endianness. </p>
<p> Decoded patterns can be used for matching in the usual way, and must be freed by calling <code>pcre2_code_free()</code>. However, be aware that there is a potential race issue if you are using multiple patterns that were decoded from a single byte stream in a multithreaded application. A single copy of the character tables is used by all the decoded patterns and a reference count is used to arrange for its memory to be automatically freed when the last pattern is freed, but there is no locking on this reference count. Therefore, if you want to call <code>pcre2_code_free()</code> for these patterns in different threads, you must arrange your own locking, and ensure that <code>pcre2_code_free()</code> cannot be called by two threads at the same time. </p>
<p> If a pattern was processed by <code>pcre2_jit_compile()</code> before being serialized, the JIT data is discarded and so is no longer available after a save/restore cycle. You can, however, process a restored pattern with <code>pcre2_jit_compile()</code> if you wish.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 27 June 2018
Copyright (c) 1997-2018 University of Cambridge.</pre>
