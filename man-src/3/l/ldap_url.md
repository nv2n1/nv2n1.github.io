---
title: "ldap_url(3)"
name: "ldap_url"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_url/"
description: "ldap_is_ldap_url, ldap_url_parse, ldap_free_urldesc – LDAP Uniform Resource Locator routines"
---

<h2 class="name">NAME</h2>
<p> ldap_is_ldap_url, ldap_url_parse, ldap_free_urldesc &#8211; LDAP Uniform Resource Locator routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_is_ldap_url(const char *url) int ldap_url_parse(const char *url, LDAPURLDesc **ludpp) typedef struct ldap_url_desc {
    char *lud_scheme;  /* URI scheme */
    char *lud_host;    /* LDAP host to contact */
    int lud_port;      /* port on host */
    char *lud_dn;      /* base for search */
    char **lud_attrs;  /* list of attributes */
    int lud_scope;     /* a LDAP_SCOPE_... value */
    char *lud_filter;  /* LDAP search filter */
    char **lud_exts;   /* LDAP extensions */
    int lud_crit_exts; /* true if any extension is critical */
    /* may contain additional fields for internal use */
} LDAPURLDesc;
void ldap_free_urldesc(LDAPURLDesc *ludp);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines support the use of LDAP URLs (Uniform Resource Locators) as detailed in RFC 4516. LDAP URLs look like this: </p>
<pre>
  <code>ldap://</code><i>hostport</i><code>/</code><i>dn</i>[<code>?</code><i>attrs</i>[<code>?</code><i>scope</i>[<code>?</code><i>filter</i>[<code>?</code><i>exts</i>]]]]
where:
  <i>hostport</i> is a host name with an optional &quot;:portnumber&quot;
  <i>dn</i> is the search base
  <i>attrs</i> is a comma separated list of attributes to request
  <i>scope</i> is one of these three strings:
    base one sub (default=base)
  <i>filter</i> is filter
  <i>exts</i> are recognized set of LDAP and/or API extensions.
Example:
  <a href="ldap://ldap.example.net/dc=example,dc=net?cn,sn?sub?(cn=*)">ldap://ldap.example.net/dc=example,dc=net?cn,sn?sub?(cn=*)</a>
</pre>
<p> URLs that are wrapped in angle-brackets and/or preceded by &quot;URL:&quot; are also tolerated. Alternative LDAP schemes such as ldaps:// and ldapi:// may be parsed using the below routines as well. </p>
<p> <code>ldap_is_ldap_url()</code> returns a non-zero value if <i>url</i> looks like an LDAP URL (as opposed to some other kind of URL). It can be used as a quick check for an LDAP URL; the <code>ldap_url_parse()</code> routine should be used if a more thorough check is needed. </p>
<p> <code>ldap_url_parse()</code> breaks down an LDAP URL passed in <i>url</i> into its component pieces. If successful, zero is returned, an LDAP URL description is allocated, filled in, and <i>ludpp</i> is set to point to it. If an error occurs, a non-zero URL error code is returned. </p>
<p> <code>ldap_free_urldesc()</code> should be called to free an LDAP URL description that was obtained from a call to <code>ldap_url_parse().</code></p>
<h2>SEE ALSO</h2>
<pre>
<code><a href="//www.systutorials.com/docs/linux/man/3-ldap/">ldap</a></code>(3)
<code>RFC 4516</code> &lt;<a rel="nofollow" href="http://www.rfc-editor.org/rfc/rfc4516.txt">http://www.rfc-editor.org/rfc/rfc4516.txt</a>&gt;
</pre>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
