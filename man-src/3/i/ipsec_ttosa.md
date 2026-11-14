---
title: "ipsec_ttosa(3)"
name: "ipsec_ttosa"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_ttosa/"
description: "ipsec_ttosa, ipsec_satot, ipsec_initsaid – convert IPsec Security Association IDs to and from text, initialize an SA ID"
---

<h2>NAME</h2>
<p> ipsec_ttosa, ipsec_satot, ipsec_initsaid &#8211; convert IPsec Security Association IDs to and from text, initialize an SA ID</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>typedef struct {</code><br />
 &nbsp;<wbr> <code>ip_address dst;</code><br />
 &nbsp;<wbr> <code>ipsec_spi_t spi;</code><br />
 &nbsp;<wbr> <code>int proto;</code><br />
 <code>} ip_said;</code> </p>
<p> <code>const char *ttosa(const char *src, size_t srclen,</code><br />
 &nbsp;<wbr> <code>ip_said *sa);</code><br />
 <code>size_t satot(const ip_said *sa, int format,</code><br />
 &nbsp;<wbr> <code>char *dst, size_t dstlen);</code><br />
 <code>void initsaid(const ip_address *addr, ipsec_spi_t spi,</code><br />
 &nbsp;<wbr> <code>int proto, ip_said *dst);</code></p>
<h2>DESCRIPTION</h2>
<p> <i>Ttosa</i> converts an ASCII Security Association (SA) specifier into an <code>ip_said</code> structure (containing a destination-host address in network byte order, an SPI number in network byte order, and a protocol code). <i>Satot</i> does the reverse conversion, back to a text SA specifier. <i>Initsaid</i> initializes an <code>ip_said</code> from separate items of information. </p>
<p> An SA is specified in text with a mail-like syntax, e.g. <code>esp.5a7 [at] 1.2.3.4</code>. An SA specifier contains a protocol prefix (currently <code>ah</code>, <code>esp</code>, <code>tun</code>, <code>comp</code>, or <code>int</code>), a single character indicating the address family (<code>.</code> for IPv4, <code>:</code> for IPv6), an unsigned integer SPI number in hexadecimal (with no <code>0x</code> prefix), and an IP address. The IP address can be any form accepted by <i><a href="/docs/linux/man/3-ipsec_ttoaddr/">ipsec_ttoaddr</a></i>(3), e.g. dotted-decimal IPv4 address, colon-hex IPv6 address, or DNS name. </p>
<p> As a special case, the SA specifier <code>%passthrough4</code> or <code>%passthrough6</code> signifies the special SA used to indicate that packets should be passed through unaltered. (At present, these are synonyms for <code>tun.0 [at] 0.0.0.0</code> and <code>tun:0@::</code> respectively, but that is subject to change without notice.) <code>%passthrough</code> is a historical synonym for <code>%passthrough4</code>. These forms are known to both <i>ttosa</i> and <i>satot</i>, so the internal representation is never visible. </p>
<p> Similarly, the SA specifiers <code>%pass</code>, <code>%drop</code>, <code>%reject</code>, <code>%hold</code>, <code>%trap</code>, and <code>%trapsubnet</code> signify special &#8220;magic&#8221; SAs used to indicate that packets should be passed, dropped, rejected (dropped with ICMP notification), held, and trapped (sent up to <i><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></i>(8), with either of two forms of <code>%hold</code> automatically installed) respectively. These forms too are known to both routines, so the internal representation of the magic SAs should never be visible. </p>
<p> The <code>&lt;libreswan.h&gt;</code> header file supplies the <code>ip_said</code> structure, as well as a data type <code>ipsec_spi_t</code> which is an unsigned 32-bit integer. (There is no consistency between kernel and user on what such a type is called, hence the header hides the differences.) </p>
<p> The protocol code uses the same numbers that IP does. For user convenience, given the difficulty in acquiring the exact set of protocol names used by the kernel, <code>&lt;libreswan.h&gt;</code> defines the names <code>SA_ESP</code>, <code>SA_AH</code>, <code>SA_IPIP</code>, and <code>SA_COMP</code> to have the same values as the kernel names <code>IPPROTO_ESP</code>, <code>IPPROTO_AH</code>, <code>IPPROTO_IPIP</code>, and <code>IPPROTO_COMP</code>. </p>
<p> <code>&lt;libreswan.h&gt;</code> also defines <code>SA_INT</code> to have the value <code>61</code> (reserved by IANA for &#8220;any host internal protocol&#8221;) and <code>SPI_PASS</code>, <code>SPI_DROP</code>, <code>SPI_REJECT</code>, <code>SPI_HOLD</code>, and <code>SPI_TRAP</code> to have the values 256-260 (in <i>host</i> byte order) respectively. These are used in constructing the magic SAs (which always have address <code>0.0.0.0</code>). </p>
<p> If <i>satot</i> encounters an unknown protocol code, e.g. 77, it yields output using a prefix showing the code numerically, e.g. &#8220;unk77&#8221;. This form is <i>not</i> recognized by <i>ttosa</i>. </p>
<p> The <i>srclen</i> parameter of <i>ttosa</i> specifies the length of the string pointed to by <i>src</i>; it is an error for there to be anything else (e.g., a terminating NUL) within that length. As a convenience for cases where an entire NUL-terminated string is to be converted, a <i>srclen</i> value of <code>0</code> is taken to mean <code>strlen(src)</code>. </p>
<p> The <i>dstlen</i> parameter of <i>satot</i> specifies the size of the <i>dst</i> parameter; under no circumstances are more than <i>dstlen</i> bytes written to <i>dst</i>. A result which will not fit is truncated. <i>Dstlen</i> can be zero, in which case <i>dst</i> need not be valid and no result is written, but the return value is unaffected; in all other cases, the (possibly truncated) result is NUL-terminated. The <code>&lt;libreswan.h&gt;</code> header file defines a constant, <code>SATOT_BUF</code>, which is the size of a buffer just large enough for worst-case results. </p>
<p> The <i>format</i> parameter of <i>satot</i> specifies what format is to be used for the conversion. The value <code>0</code> (not the ASCII character <code>&#8216;0&#8217;</code>, but a zero value) specifies a reasonable default (currently lowercase protocol prefix, lowercase hexadecimal SPI, dotted-decimal or colon-hex address). The value <code>&#8216;f&#8217;</code> is similar except that the SPI is padded with <code>0</code>s to a fixed 32-bit width, to ease aligning displayed tables. </p>
<p> <i>Ttosa</i> returns <code>NULL</code> for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS. <i>Satot</i> returns <code>0</code> for a failure, and otherwise always returns the size of buffer which would be needed to accommodate the full conversion result, including terminating NUL; it is the caller&#8217;s responsibility to check this against the size of the provided buffer to determine whether truncation has occurred. </p>
<p> There is also, temporarily, support for some obsolete forms of SA specifier which lack the address-family indicator.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ipsec_ttoul/">ipsec_ttoul</a>(3), <a href="/docs/linux/man/3-ipsec_ttoaddr/">ipsec_ttoaddr</a>(3), <a href="/docs/linux/man/3-ipsec_samesaid/">ipsec_samesaid</a>(3), <a href="/docs/linux/man/3-inet/">inet</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in <i>ttosa</i> are: empty input; input too small to be a legal SA specifier; no <code>@</code> in input; unknown protocol prefix; conversion error in <i>ttoul</i> or <i>ttoaddr</i>. </p>
<p> Fatal errors in <i>satot</i> are: unknown format.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> The restriction of text-to-binary error reports to literal strings (so that callers don&#8217;t need to worry about freeing them or copying them) does limit the precision of error reporting. </p>
<p> The text-to-binary error-reporting convention lends itself to slightly obscure code, because many readers will not think of NULL as signifying success. A good way to make it clearer is to write something like: </p>
<dl>
<dt>
<dd>
<pre><code>
const char *error;
error = ttosa(/* ... */);
if (error != NULL) {
/* something went wrong */
</code></pre>
</dl>
<h2>Index</h2>
