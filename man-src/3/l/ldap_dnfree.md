---
title: "ldap_dnfree(3)"
name: "ldap_dnfree"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_dnfree/"
description: "ldap_get_dn, ldap_explode_dn, ldap_explode_rdn, ldap_dn2ufn – LDAP DN handling routines"
---

<h2 class="name">NAME</h2>
<p> ldap_get_dn, ldap_explode_dn, ldap_explode_rdn, ldap_dn2ufn &#8211; LDAP DN handling routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
char *ldap_get_dn(LDAP *ld, LDAPMessage *entry) int ldap_str2dn(const char *str, LDAPDN *dn, unsigned flags) void ldap_dnfree(LDAPDN dn) int ldap_dn2str(LDAPDN dn, char **str, unsigned flags) char **ldap_explode_dn(const char *dn, int notypes) char **ldap_explode_rdn(const char *rdn, int notypes) char *ldap_dn2ufn(const char *dn) char *ldap_dn2dcedn(const char *dn) char *ldap_dcedn2dn(const char *dn) char *ldap_dn2ad_canonical(const char *dn)
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines allow LDAP entry names (Distinguished Names, or DNs) to be obtained, parsed, converted to a user-friendly form, and tested. A DN has the form described in RFC 4414 &quot;Lightweight Directory Access Protocol (LDAP): String Representation of Distinguished Names&quot;. </p>
<p> The <code>ldap_get_dn()</code> routine takes an <i>entry</i> as returned by <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_next_entry/">ldap_next_entry</a></code>(3) and returns a copy of the entry&#8217;s DN. Space for the DN will be obtained dynamically and should be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). </p>
<p> <code>ldap_str2dn()</code> parses a string representation of a distinguished name contained in <code>str</code> into its components, which are stored in <code>dn</code> as <code>ldap_ava </code> structures, arranged in <code>LDAPAVA,</code> <code>LDAPRDN,</code> and <code>LDAPDN</code> terms. Space for <code>dn</code> will be obtained dynamically and should be freed by the caller using <code><a href="/docs/linux/man/3-ldap_dnfree/">ldap_dnfree</a></code>(3). The <code>LDAPDN</code> is defined as: </p>
<pre><code>
typedef struct ldap_ava {
    struct berval la_attr;
    struct berval la_value;
    unsigned la_flags;
} LDAPAVA;
typedef LDAPAVA **LDAPRDN;
typedef LDAPRDN *LDAPDN;
</code></pre>
<p> The attribute types and the attribute values are not normalized. The <code>la_flags</code> can be either <code>LDAP_AVA_STRING</code> or <code>LDAP_AVA_BINARY,</code> the latter meaning that the value is BER/DER encoded and thus must be represented as, quoting from RFC 4514, &quot; &#8230; an octothorpe character (&#8216;#&#8217; ASCII 35) followed by the hexadecimal representation of each of the bytes of the BER encoding of the X.500 AttributeValue.&quot; The <code>flags</code> parameter to <code>ldap_str2dn()</code> can be </p>
<pre>
        LDAP_DN_FORMAT_LDAPV3
        LDAP_DN_FORMAT_LDAPV2
        LDAP_DN_FORMAT_DCE
</pre>
<p> which defines what DN syntax is expected (according to RFC 4514, RFC 1779 and DCE, respectively). The format can be <i>OR</i>ed to the flags </p>
<pre>
        LDAP_DN_P_NO_SPACES
        LDAP_DN_P_NO_SPACE_AFTER_RDN
        ...
        LDAP_DN_PEDANTIC
</pre>
<p> The latter is a shortcut for all the previous limitations. </p>
<p> <code>LDAP_DN_P_NO_SPACES</code> does not allow extra spaces in the dn; the default is to silently eliminate spaces around AVA separators (&#8216;=&#8217;), RDN component separators (&#8216;+&#8217; for LDAPv3/LDAPv2 or &#8216;,&#8217; for DCE) and RDN separators (&#8216;,&#8217; LDAPv3/LDAPv2 or &#8216;/&#8217; for DCE). </p>
<p> <code>LDAP_DN_P_NO_SPACE_AFTER_RDN</code> does not allow a single space after RDN separators. </p>
<p> <code>ldap_dn2str()</code> performs the inverse operation, yielding in <code>str</code> a string representation of <code>dn.</code> It allows the same values for <code>flags </code> as <code>ldap_str2dn(),</code> plus </p>
<pre>
        LDAP_DN_FORMAT_UFN
        LDAP_DN_FORMAT_AD_CANONICAL
</pre>
<p> for user-friendly naming (RFC 1781) and AD canonical. </p>
<p> The following routines are viewed as deprecated in favor of <code>ldap_str2dn()</code> and <code>ldap_dn2str().</code> They are provided to support legacy applications. </p>
<p> The <code>ldap_explode_dn()</code> routine takes a DN as returned by <code>ldap_get_dn()</code> and breaks it up into its component parts. Each part is known as a Relative Distinguished Name, or RDN. <code>ldap_explode_dn()</code> returns a NULL-terminated array, each component of which contains an RDN from the DN. The <i>notypes</i> parameter is used to request that only the RDN values be returned, not their types. For example, the DN &quot;cn=Bob, c=US&quot; would return as either { &quot;cn=Bob&quot;, &quot;c=US&quot;, NULL } or { &quot;Bob&quot;, &quot;US&quot;, NULL }, depending on whether notypes was 0 or 1, respectively. Assertion values in RDN strings may included escaped characters. The result can be freed by calling <code><a href="/docs/linux/man/3-ldap_value_free/">ldap_value_free</a></code>(3). </p>
<p> Similarly, the <code>ldap_explode_rdn()</code> routine takes an RDN as returned by <code>ldap_explode_dn(dn,0)</code> and breaks it up into its &quot;type=value&quot; component parts (or just &quot;value&quot;, if the <i>notypes</i> parameter is set). Note the value is not unescaped. The result can be freed by calling <code><a href="/docs/linux/man/3-ldap_value_free/">ldap_value_free</a></code>(3). </p>
<p> <code>ldap_dn2ufn()</code> is used to turn a DN as returned by <code><a href="/docs/linux/man/3-ldap_get_dn/">ldap_get_dn</a></code>(3) into a more user-friendly form, stripping off all type names. See &quot;Using the Directory to Achieve User Friendly Naming&quot; (RFC 1781) for more details on the UFN format. Due to the ambiguous nature of the format, it is generally only used for display purposes. The space for the UFN returned is obtained dynamically and the user is responsible for freeing it via a call to <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). </p>
<p> <code>ldap_dn2dcedn()</code> is used to turn a DN as returned by <code><a href="/docs/linux/man/3-ldap_get_dn/">ldap_get_dn</a></code>(3) into a DCE-style DN, e.g. a string with most-significant to least significant rdns separated by slashes (&#8216;/&#8217;); rdn components are separated by commas (&#8216;,&#8217;). Only printable chars (e.g. LDAPv2 printable string) are allowed, at least in this implementation. <code>ldap_dcedn2dn()</code> performs the opposite operation. <code>ldap_dn2ad_canonical()</code> turns a DN into a AD canonical name, which is basically a DCE dn with attribute types omitted. The trailing domain, if present, is turned in a DNS-like domain. The space for the returned value is obtained dynamically and the user is responsible for freeing it via a call to <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<h2>ERRORS</h2>
<p> If an error occurs in <code>ldap_get_dn()</code>, NULL is returned and the <code>ld_errno</code> field in the <i>ld</i> parameter is set to indicate the error. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for a description of possible error codes. <code>ldap_explode_dn()</code>, <code>ldap_explode_rdn()</code>, <code>ldap_dn2ufn(),</code> <code>ldap_dn2dcedn(),</code> <code>ldap_dcedn2dn(),</code> and <code>ldap_dn2ad_canonical()</code> will return NULL with <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3) set appropriately in case of trouble.</p>
<h2>NOTES</h2>
<p> These routines dynamically allocate memory that the caller must free.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3), <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), <code><a href="/docs/linux/man/3-ldap_value_free/">ldap_value_free</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
