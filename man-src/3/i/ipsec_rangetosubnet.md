---
title: "ipsec_rangetosubnet(3)"
name: "ipsec_rangetosubnet"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_rangetosubnet/"
description: "ipsec_rangetosubnet – convert address range to subnet"
---

<h2 class="name">NAME</h2>
<p> ipsec_rangetosubnet &#8211; convert address range to subnet </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;freeswan.h&gt;
</code></pre>
<dl>
<dt> <code>const char *rangetosubnet(const ip_address&nbsp;<wbr>*&nbsp;<wbr></code><i>start</i><code>, const ip_address&nbsp;<wbr>*&nbsp;<wbr></code><i>stop</i><code>, ip_subnet&nbsp;<wbr>*&nbsp;<wbr></code><i>dst</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <i>Rangetosubnet</i></p>
<dd>accepts two IP addresses which define an address range, from <i>start</i> to <i>stop</i> inclusive, and converts this to a subnet if possible. The addresses must both be IPv4 or both be IPv6, and the address family of the resulting subnet is the same. </p>
<p> <i>Rangetosubnet</i> returns NULL for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ipsec_initsubnet/">ipsec_initsubnet</a></code>(3), <code><a href="/docs/linux/man/3-ipsec_ttosubnet/">ipsec_ttosubnet</a></code>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in <code>rangetosubnet</code> are: mixed address families; unknown address family; <i>start</i> and <i>stop</i> do not define a subnet.</p>
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
error = rangetosubnet(/* ... */);
if (error != NULL) {
/* something went wrong */
</code></pre>
</dl>
<h2>Index</h2>
