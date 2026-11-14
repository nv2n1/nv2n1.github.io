---
title: "ipsec_atoasr(3)"
name: "ipsec_atoasr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_atoasr/"
description: "ipsec_atoasr, ipsec_rangetoa – convert ASCII to Internet address, subnet, or range, convert Internet address range to ASCII"
---

<h2>NAME</h2>
<p> ipsec_atoasr, ipsec_rangetoa &#8211; convert ASCII to Internet address, subnet, or range, convert Internet address range to ASCII</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>const char *atoasr(const char *src, size_t srclen,</code><br />
 &nbsp;<wbr> <code>char *type, struct in_addr *addrs);</code><br />
 <code>size_t rangetoa(struct in_addr *addrs, int format,</code><br />
 &nbsp;<wbr> <code>char *dst, size_t dstlen);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions are obsolete; there is no current equivalent, because so far they have not proved useful. </p>
<p> <i>Atoasr</i> converts an ASCII address, subnet, or address range into a suitable combination of binary addresses (in network byte order). <i>Rangetoa</i> converts an address range back into ASCII, using dotted-decimal form for the addresses (the other reverse conversions are handled by <i><a href="/docs/linux/man/3-ipsec_addrtoa/">ipsec_addrtoa</a></i>(3) and <i><a href="/docs/linux/man/3-ipsec_subnettoa/">ipsec_subnettoa</a></i>(3)). </p>
<p> A single address can be any form acceptable to <i><a href="/docs/linux/man/3-ipsec_atoaddr/">ipsec_atoaddr</a></i>(3): dotted decimal, DNS name, or hexadecimal number. A subnet specification uses the form <i>network</i><code>/</code><i>mask</i> interpreted by <i><a href="/docs/linux/man/3-ipsec_atosubnet/">ipsec_atosubnet</a></i>(3). </p>
<p> An address range is two <i><a href="/docs/linux/man/3-ipsec_atoaddr/">ipsec_atoaddr</a></i>(3) addresses separated by a <code>&#8230;</code> delimiter. If there are four dots rather than three, the first is taken as part of the begin address, e.g. for a complete DNS name which ends with <code>.</code> to suppress completion attempts. The begin address of a range must be less than or equal to the end address. </p>
<p> The <i>srclen</i> parameter of <i>atoasr</i> specifies the length of the ASCII string pointed to by <i>src</i>; it is an error for there to be anything else (e.g., a terminating NUL) within that length. As a convenience for cases where an entire NUL-terminated string is to be converted, a <i>srclen</i> value of <code>0</code> is taken to mean <code>strlen(src)</code>. </p>
<p> The <i>type</i> parameter of <i>atoasr</i> must point to a <code>char</code> variable used to record which form was found. The <i>addrs</i> parameter must point to a two-element array of <code>struct in_addr</code> which receives the results. The values stored into <code>*type</code>, and the corresponding values in the array, are: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*typeaddrs[0]addrs[1]</p>
<p> address<code>&#8216;a&#8217;</code>address-</p>
<p> subnet<tt>&nbsp;<wbr></tt><code>&#8216;s&#8217;</code>networkmask</p>
<p> range<tt>&nbsp;<wbr>&nbsp;<wbr></tt><code>&#8216;r&#8217;</code>beginend</p>
<p> The <i>dstlen</i> parameter of <i>rangetoa</i> specifies the size of the <i>dst</i> parameter; under no circumstances are more than <i>dstlen</i> bytes written to <i>dst</i>. A result which will not fit is truncated. <i>Dstlen</i> can be zero, in which case <i>dst</i> need not be valid and no result is written, but the return value is unaffected; in all other cases, the (possibly truncated) result is NUL-terminated. The <i>libreswan.h</i> header file defines a constant, <code>RANGETOA_BUF</code>, which is the size of a buffer just large enough for worst-case results. </p>
<p> The <i>format</i> parameter of <i>rangetoa</i> specifies what format is to be used for the conversion. The value <code>0</code> (not the ASCII character <code>&#8216;0&#8217;</code>, but a zero value) specifies a reasonable default, and is in fact the only format currently available. This parameter is a hedge against future needs. </p>
<p> <i>Atoasr</i> returns NULL for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS. <i>Rangetoa</i> returns <code>0</code> for a failure, and otherwise always returns the size of buffer which would be needed to accommodate the full conversion result, including terminating NUL; it is the caller&#8217;s responsibility to check this against the size of the provided buffer to determine whether truncation has occurred.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ipsec_atoaddr/">ipsec_atoaddr</a>(3), <a href="/docs/linux/man/3-ipsec_atosubnet/">ipsec_atosubnet</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in <i>atoasr</i> are: empty input; error in <i><a href="/docs/linux/man/3-ipsec_atoaddr/">ipsec_atoaddr</a></i>(3) or <i><a href="/docs/linux/man/3-ipsec_atosubnet/">ipsec_atosubnet</a></i>(3) during conversion; begin address of range exceeds end address. </p>
<p> Fatal errors in <i>rangetoa</i> are: unknown format.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> The restriction of error reports to literal strings (so that callers don&#8217;t need to worry about freeing them or copying them) does limit the precision of error reporting. </p>
<p> The error-reporting convention lends itself to slightly obscure code, because many readers will not think of NULL as signifying success. A good way to make it clearer is to write something like: </p>
<dl>
<dt>
<dd>
<pre><code>
const char *error;
error = atoasr(/* ... */);
if (error != NULL) {
/* something went wrong */
</code></pre>
</dl>
<h2>Index</h2>
