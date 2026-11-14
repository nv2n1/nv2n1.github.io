---
title: "pcre2_serialize_decode(3)"
name: "pcre2_serialize_decode"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_serialize_decode/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>int32_t pcre2_serialize_decode(pcre2_code **</code><i>codes</i>,
<code> int32_t </code><i>number_of_codes</i>, const uint8_t *<i>bytes</i>,
<code> pcre2_general_context *</code><i>gcontext</i>);</pre>
<h2>Description</h2>
<p>This function decodes a serialized set of compiled patterns back into a list of individual patterns. This is possible only on a host that is running the same version of PCRE2, with the same code unit width, and the host must also have the same endianness, pointer width and PCRE2_SIZE type. The arguments for <code>pcre2_serialize_decode()</code> are:<br />
&nbsp;<wbr>&nbsp;<i>codes</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to a vector in which to build the list<br />
&nbsp;<wbr>&nbsp;<i>number_of_codes</i>&nbsp;<wbr>&nbsp;number of slots in the vector<br />
&nbsp;<wbr>&nbsp;<i>bytes</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the serialized byte stream<br />
&nbsp;<wbr>&nbsp;<i>gcontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to a general context or NULL The <i>bytes</i> argument must point to a block of data that was originally created by <code>pcre2_serialize_encode()</code>, though it may have been saved on disc or elsewhere in the meantime. If there are more codes in the serialized data than slots in the list, only those compiled patterns that will fit are decoded. The yield of the function is the number of decoded patterns, or one of the following negative error codes:<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADDATA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>number_of_codes</i>&nbsp;is zero or less<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;mismatch of id bytes in&nbsp;<i>bytes</i><br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMODE&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch of variable unit size or PCRE version<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_MEMORY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory allocation failed<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>codes</i>&nbsp;or&nbsp;<i>bytes</i>&nbsp;is NULL PCRE2_ERROR_BADMAGIC may mean that the data is corrupt, or that it was compiled on a system with different endianness. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the serialization functions in the <code>pcre2serialize</code> page. </p>
