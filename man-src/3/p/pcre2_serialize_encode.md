---
title: "pcre2_serialize_encode(3)"
name: "pcre2_serialize_encode"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_serialize_encode/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>int32_t pcre2_serialize_encode(const pcre2_code **</code><i>codes</i>,
<code> int32_t </code><i>number_of_codes</i>, uint8_t **<i>serialized_bytes</i>,
<code> PCRE2_SIZE *</code><i>serialized_size</i>, pcre2_general_context *<i>gcontext</i>);</pre>
<h2>Description</h2>
<p>This function encodes a list of compiled patterns into a byte stream that can be saved on disc or elsewhere. Note that this is not an abstract format like Java or .NET. Conversion of the byte stream back into usable compiled patterns can only happen on a host that is running the same version of PCRE2, with the same code unit width, and the host must also have the same endianness, pointer width and PCRE2_SIZE type. The arguments for <code>pcre2_serialize_encode()</code> are:<br />
&nbsp;<wbr>&nbsp;<i>codes</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to a vector containing the list<br />
&nbsp;<wbr>&nbsp;<i>number_of_codes</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;number of slots in the vector<br />
&nbsp;<wbr>&nbsp;<i>serialized_bytes</i>&nbsp;<wbr>&nbsp;set to point to the serialized byte stream<br />
&nbsp;<wbr>&nbsp;<i>serialized_size</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set to the number of bytes in the byte stream<br />
&nbsp;<wbr>&nbsp;<i>gcontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to a general context or NULL The context argument is used to obtain memory for the byte stream. When the serialized data is no longer needed, it must be freed by calling <code>pcre2_serialize_free()</code>. The yield of the function is the number of serialized patterns, or one of the following negative error codes:<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADDATA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>number_of_codes</i>&nbsp;is zero or less<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch of id bytes in one of the patterns<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_MEMORY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory allocation failed<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_MIXEDTABLES&nbsp;<wbr>&nbsp;the patterns do not all use the same tables<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;an argument other than&nbsp;<i>gcontext</i>&nbsp;is NULL PCRE2_ERROR_BADMAGIC means either that a pattern&#8217;s code has been corrupted, or that a slot in the vector does not point to a compiled pattern. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the serialization functions in the <code>pcre2serialize</code> page. </p>
