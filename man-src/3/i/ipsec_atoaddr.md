---
title: "ipsec_atoaddr(3)"
name: "ipsec_atoaddr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_atoaddr/"
description: "ipsec_atoaddr, ipsec_addrtoa, ipsec_atosubnet, ipsec_subnettoa – convert Internet addresses and Subnet masks to and from ASCII"
---

<h2>NAME</h2>
<p> ipsec_atoaddr, ipsec_addrtoa, ipsec_atosubnet, ipsec_subnettoa &#8211; convert Internet addresses and Subnet masks to and from ASCII</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>const char *atoaddr(const char *src, size_t srclen,</code><br />
 &nbsp;<wbr> <code>struct in_addr *addr);</code><br />
 <code>size_t addrtoa(struct in_addr addr, int format,</code><br />
 &nbsp;<wbr> <code>char *dst, size_t dstlen);</code> </p>
<p> <code>const char *atosubnet(const char *src, size_t srclen,</code><br />
 &nbsp;<wbr> <code>struct in_addr *addr, struct in_addr *mask);</code><br />
 <code>size_t subnettoa(struct in_addr addr, struct in_addr mask,</code><br />
 &nbsp;<wbr> <code>int format, char *dst, size_t dstlen);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions are obsolete; see <i><a href="/docs/linux/man/3-ipsec_ttoaddr/">ipsec_ttoaddr</a></i>(3) for their replacements. </p>
<p> <i>Atoaddr</i> converts an ASCII name or dotted-decimal address into a binary address (in network byte order). <i>Addrtoa</i> does the reverse conversion, back to an ASCII dotted-decimal address. <i>Atosubnet</i> and <i>subnettoa</i> do likewise for the &#8220;address/mask&#8221; ASCII form used to write a specification of a subnet. </p>
<p> An address is specified in ASCII as a dotted-decimal address (e.g. <code>1.2.3.4</code>), an eight-digit network-order hexadecimal number with the usual C prefix (e.g. <code>0x01020304</code>, which is synonymous with <code>1.2.3.4</code>), an eight-digit host-order hexadecimal number with a <code>0h</code> prefix (e.g. <code>0h01020304</code>, which is synonymous with <code>1.2.3.4</code> on a big-endian host and <code>4.3.2.1</code> on a little-endian host), a DNS name to be looked up via <i><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></i>(3), or an old-style network name to be looked up via <i><a href="/docs/linux/man/3-getnetbyname/">getnetbyname</a></i>(3). </p>
<p> A dotted-decimal address may be incomplete, in which case ASCII-to-binary conversion implicitly appends as many instances of <code>.0</code> as necessary to bring it up to four components. The components of a dotted-decimal address are always taken as decimal, and leading zeros are ignored. For example, <code>10</code> is synonymous with <code>10.0.0.0</code>, and <code>128.009.000.032</code> is synonymous with <code>128.9.0.32</code> (the latter example is verbatim from RFC 1166). The result of <i>addrtoa</i> is always complete and does not contain leading zeros. </p>
<p> The letters in a hexadecimal address may be uppercase or lowercase or any mixture thereof. Use of hexadecimal addresses is <code>strongly</code> <code>discouraged</code>; they are included only to save hassles when dealing with the handful of perverted programs which already print network addresses in hexadecimal. </p>
<p> DNS names may be complete (optionally terminated with a &#8220;.&#8221;) or incomplete, and are looked up as specified by local system configuration (see <i><a href="/docs/linux/man/5-resolver/">resolver</a></i>(5)). The <i>h_addr</i> value returned by <i><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></i>(3) is used, so with current DNS implementations, the result when the name corresponds to more than one address is difficult to predict. Name lookup resorts to <i><a href="/docs/linux/man/3-getnetbyname/">getnetbyname</a></i>(3) only if <i><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></i>(3) fails. </p>
<p> A subnet specification is of the form <i>network</i><code>/</code><i>mask</i>. The <i>network</i> and <i>mask</i> can be any form acceptable to <i>atoaddr</i>. In addition, the <i>mask</i> can be a decimal integer (leading zeros ignored) giving a bit count, in which case it stands for a mask with that number of high bits on and all others off (e.g., <code>24</code> means <code>255.255.255.0</code>). In any case, the mask must be contiguous (a sequence of high bits on and all remaining low bits off). As a special case, the subnet specification <code>%default</code> is a synonym for <code>0.0.0.0/0</code>. </p>
<p> <i>Atosubnet</i> ANDs the mask with the address before returning, so that any non-network bits in the address are turned off (e.g., <code>10.1.2.3/24</code> is synonymous with <code>10.1.2.0/24</code>). <i>Subnettoa</i> generates the decimal-integer-bit-count form of the mask, with no leading zeros, unless the mask is non-contiguous. </p>
<p> The <i>srclen</i> parameter of <i>atoaddr</i> and <i>atosubnet</i> specifies the length of the ASCII string pointed to by <i>src</i>; it is an error for there to be anything else (e.g., a terminating NUL) within that length. As a convenience for cases where an entire NUL-terminated string is to be converted, a <i>srclen</i> value of <code>0</code> is taken to mean <code>strlen(src)</code>. </p>
<p> The <i>dstlen</i> parameter of <i>addrtoa</i> and <i>subnettoa</i> specifies the size of the <i>dst</i> parameter; under no circumstances are more than <i>dstlen</i> bytes written to <i>dst</i>. A result which will not fit is truncated. <i>Dstlen</i> can be zero, in which case <i>dst</i> need not be valid and no result is written, but the return value is unaffected; in all other cases, the (possibly truncated) result is NUL-terminated. The <i>libreswan.h</i> header file defines constants, <code>ADDRTOA_BUF</code> and <code>SUBNETTOA_BUF</code>, which are the sizes of buffers just large enough for worst-case results. </p>
<p> The <i>format</i> parameter of <i>addrtoa</i> and <i>subnettoa</i> specifies what format is to be used for the conversion. The value <code>0</code> (not the ASCII character <code>&#8216;0&#8217;</code>, but a zero value) specifies a reasonable default, and is in fact the only format currently available. This parameter is a hedge against future needs. </p>
<p> The ASCII-to-binary functions return NULL for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS. The binary-to-ASCII functions return <code>0</code> for a failure, and otherwise always return the size of buffer which would be needed to accommodate the full conversion result, including terminating NUL; it is the caller&#8217;s responsibility to check this against the size of the provided buffer to determine whether truncation has occurred.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-inet/">inet</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in <i>atoaddr</i> are: empty input; attempt to allocate temporary storage for a very long name failed; name lookup failed; syntax error in dotted-decimal form; dotted-decimal component too large to fit in 8 bits. </p>
<p> Fatal errors in <i>atosubnet</i> are: no <code>/</code> in <i>src</i>; <i>atoaddr</i> error in conversion of <i>network</i> or <i>mask</i>; bit-count mask too big; mask non-contiguous. </p>
<p> Fatal errors in <i>addrtoa</i> and <i>subnettoa</i> are: unknown format.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> The interpretation of incomplete dotted-decimal addresses (e.g. <code>10/24</code> means <code>10.0.0.0/24</code>) differs from that of some older conversion functions, e.g. those of <i><a href="/docs/linux/man/3-inet/">inet</a></i>(3). The behavior of the older functions has never been particularly consistent or particularly useful. </p>
<p> Ignoring leading zeros in dotted-decimal components and bit counts is arguably the most useful behavior in this application, but it might occasionally cause confusion with the historical use of leading zeros to denote octal numbers. </p>
<p> It is barely possible that somebody, somewhere, might have a legitimate use for non-contiguous subnet masks. </p>
<p> <i><a href="/docs/linux/man/3-getnetbyname/">Getnetbyname</a></i>(3) is a historical dreg. </p>
<p> The restriction of ASCII-to-binary error reports to literal strings (so that callers don&#8217;t need to worry about freeing them or copying them) does limit the precision of error reporting. </p>
<p> The ASCII-to-binary error-reporting convention lends itself to slightly obscure code, because many readers will not think of NULL as signifying success. A good way to make it clearer is to write something like: </p>
<dl>
<dt>
<dd>
<pre><code>
const char *error;
error = atoaddr(/* ... */);
if (error != NULL) {
/* something went wrong */
</code></pre>
</dl>
<h2>Index</h2>
