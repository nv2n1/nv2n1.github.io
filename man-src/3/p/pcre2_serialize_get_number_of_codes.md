---
title: "pcre2_serialize_get_number_of_codes(3)"
name: "pcre2_serialize_get_number_of_codes"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_serialize_get_number_of_codes/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>int32_t pcre2_serialize_get_number_of_codes(const uint8_t *</code><i>bytes</i>);</pre>
<h2>Description</h2>
<p>The <i>bytes</i> argument must point to a serialized byte stream that was originally created by <code>pcre2_serialize_encode()</code> (though it may have been saved on disc or elsewhere in the meantime). The function returns the number of serialized patterns in the byte stream, or one of the following negative error codes:<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;mismatch of id bytes in&nbsp;<i>bytes</i><br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMODE&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch of variable unit size or PCRE version<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the argument is NULL PCRE2_ERROR_BADMAGIC may mean that the data is corrupt, or that it was compiled on a system with different endianness. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the serialization functions in the <code>pcre2serialize</code> page. </p>
