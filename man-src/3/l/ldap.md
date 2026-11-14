---
title: "ldap(3)"
name: "ldap"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap/"
description: "ldap – OpenLDAP Lightweight Directory Access Protocol API"
---

<h2 class="name">NAME</h2>
<p> ldap &#8211; OpenLDAP Lightweight Directory Access Protocol API </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The Lightweight Directory Access Protocol (LDAP) (RFC 4510) provides access to X.500 directory services. These services may be stand-alone or part of a distributed directory service. This client API supports LDAP over TCP (RFC 4511), LDAP over TLS/SSL, and LDAP over IPC (UNIX domain sockets). This API supports SASL (RFC 4513) and Start TLS (RFC 4513) as well as a number of protocol extensions. This API is loosely based upon IETF/LDAPEXT C LDAP API draft specification, a (orphaned) work in progress. </p>
<p> The OpenLDAP Software package includes a stand-alone server in <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), various LDAP clients, and an LDAP client library used to provide programmatic access to the LDAP protocol. This man page gives an overview of the LDAP library routines. </p>
<p> Both synchronous and asynchronous APIs are provided. Also included are various routines to parse the results returned from these routines. These routines are found in the -lldap library. </p>
<p> The basic interaction is as follows. A session handle is created using <code><a href="/docs/linux/man/3-ldap_initialize/">ldap_initialize</a></code>(3) and set the protocol version to 3 by calling <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3). The underlying session is established first operation is issued. This would generally be a Start TLS or Bind operation, or a Search operation to read attributes of the Root DSE. A Start TLS operation is performed by calling <code><a href="/docs/linux/man/3-ldap_start_tls_s/">ldap_start_tls_s</a></code>(3). A LDAP bind operation is performed by calling <code><a href="/docs/linux/man/3-ldap_sasl_bind/">ldap_sasl_bind</a></code>(3) or one of its friends. A Search operation is performed by calling <a href="/docs/linux/man/3-ldap_search_ext_s/">ldap_search_ext_s</a>(3) or one of its friends. </p>
<p> Subsequently, additional operations are performed by calling one of the synchronous or asynchronous routines (e.g., <code><a href="/docs/linux/man/3-ldap_compare_ext_s/">ldap_compare_ext_s</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_compare_ext/">ldap_compare_ext</a></code>(3) followed by <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3)). Results returned from these routines are interpreted by calling the LDAP parsing routines such as <code><a href="/docs/linux/man/3-ldap_parse_result/">ldap_parse_result</a></code>(3). The LDAP association and underlying connection is terminated by calling <code><a href="/docs/linux/man/3-ldap_unbind_ext/">ldap_unbind_ext</a></code>(3). Errors can be interpreted by calling <code><a href="/docs/linux/man/3-ldap_err2string/">ldap_err2string</a></code>(3).</p>
<h2>LDAP versions</h2>
<p> This library supports version 3 of the Lightweight Directory Access Protocol (LDAPv3) as defined in RFC 4510. It also supports a variant of version 2 of LDAP as defined by U-Mich LDAP and, to some degree, RFC 1777. Version 2 (all variants) are considered obsolete. Version 3 should be used instead. </p>
<p> For backwards compatibility reasons, the library defaults to version 2. Hence, all new applications (and all actively maintained applications) should use <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3) to select version 3. The library manual pages assume version 3 has been selected.</p>
<h2>INPUT and OUTPUT PARAMETERS</h2>
<p> All character string input/output is expected to be/is UTF-8 encoded Unicode (version 3.2). </p>
<p> Distinguished names (DN) (and relative distinguished names (RDN) to be passed to the LDAP routines should conform to RFC 4514 UTF-8 string representation. </p>
<p> Search filters to be passed to the search routines are to be constructed by hand and should conform to RFC 4515 UTF-8 string representation. </p>
<p> LDAP URLs to be passed to routines are expected to conform to RFC 4516 format. The <code><a href="/docs/linux/man/3-ldap_url/">ldap_url</a></code>(3) routines can be used to work with LDAP URLs. </p>
<p> LDAP controls to be passed to routines can be manipulated using the <code><a href="/docs/linux/man/3-ldap_controls/">ldap_controls</a></code>(3) routines.</p>
<h2>DISPLAYING RESULTS</h2>
<p> Results obtained from the search routines can be output by hand, by calling <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3) and <code><a href="/docs/linux/man/3-ldap_next_entry/">ldap_next_entry</a></code>(3) to step through the entries returned, <code><a href="/docs/linux/man/3-ldap_first_attribute/">ldap_first_attribute</a></code>(3) and <code><a href="/docs/linux/man/3-ldap_next_attribute/">ldap_next_attribute</a></code>(3) to step through an entry&#8217;s attributes, and <code><a href="/docs/linux/man/3-ldap_get_values/">ldap_get_values</a></code>(3) to retrieve a given attribute&#8217;s values. Attribute values may or may not be displayable.</p>
<h2>UTILITY ROUTINES</h2>
<p> Also provided are various utility routines. The <code><a href="/docs/linux/man/3-ldap_sort/">ldap_sort</a></code>(3) routines are used to sort the entries and values returned via the ldap search routines.</p>
<h2>DEPRECATED INTERFACES</h2>
<p> A number of interfaces are now considered deprecated. For instance, <a href="/docs/linux/man/3-ldap_add/">ldap_add</a>(3) is deprecated in favor of <a href="/docs/linux/man/3-ldap_add_ext/">ldap_add_ext</a>(3). Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated.</p>
<h2>BER LIBRARY</h2>
<p> Also included in the distribution is a set of lightweight Basic Encoding Rules routines. These routines are used by the LDAP library routines to encode and decode LDAP protocol elements using the (slightly simplified) Basic Encoding Rules defined by LDAP. They are not normally used directly by an LDAP application program except in the handling of controls and extended operations. The routines provide a printf and scanf-like interface, as well as lower-level access. These routines are discussed in <code><a href="/docs/linux/man/3-lber-decode/">lber-decode</a></code>(3), <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3), <code><a href="/docs/linux/man/3-lber-memory/">lber-memory</a></code>(3), and <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3).</p>
<h2>INDEX</h2>
<dl>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_initialize/">ldap_initialize</a>(3)</font></p>
<dd> initialize the LDAP library without opening a connection to a server</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_result/">ldap_result</a>(3)</font></p>
<dd> wait for the result from an asynchronous operation</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_abandon_ext/">ldap_abandon_ext</a>(3)</font></p>
<dd> abandon (abort) an asynchronous operation</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_add_ext/">ldap_add_ext</a>(3)</font></p>
<dd> asynchronously add an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_add_ext_s/">ldap_add_ext_s</a>(3)</font></p>
<dd> synchronously add an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_sasl_bind/">ldap_sasl_bind</a>(3)</font></p>
<dd> asynchronously bind to the directory</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_sasl_bind_s/">ldap_sasl_bind_s</a>(3)</font></p>
<dd> synchronously bind to the directory</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_unbind_ext/">ldap_unbind_ext</a>(3)</font></p>
<dd> synchronously unbind from the LDAP server and close the connection</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_unbind/">ldap_unbind</a>(3) and <a href="/docs/linux/man/3-ldap_unbind_s/">ldap_unbind_s</a>(3) are</font></p>
<dd> equivalent to <code><a href="/docs/linux/man/3-ldap_unbind_ext/">ldap_unbind_ext</a></code>(3)</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a>(3)</font></p>
<dd> dispose of memory allocated by LDAP routines.</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_compare_ext/">ldap_compare_ext</a>(3)</font></p>
<dd> asynchronously compare to a directory entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_compare_ext_s/">ldap_compare_ext_s</a>(3)</font></p>
<dd> synchronously compare to a directory entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_delete_ext/">ldap_delete_ext</a>(3)</font></p>
<dd> asynchronously delete an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_delete_ext_s/">ldap_delete_ext_s</a>(3)</font></p>
<dd> synchronously delete an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ld_errno/">ld_errno</a>(3)</font></p>
<dd> LDAP error indication</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_errlist/">ldap_errlist</a>(3)</font></p>
<dd> list of LDAP errors and their meanings</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_err2string/">ldap_err2string</a>(3)</font></p>
<dd> convert LDAP error indication to a string</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_extended_operation/">ldap_extended_operation</a>(3)</font></p>
<dd> asynchronously perform an arbitrary extended operation</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_extended_operation_s/">ldap_extended_operation_s</a>(3)</font></p>
<dd> synchronously perform an arbitrary extended operation</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_first_attribute/">ldap_first_attribute</a>(3)</font></p>
<dd> return first attribute name in an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_next_attribute/">ldap_next_attribute</a>(3)</font></p>
<dd> return next attribute name in an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a>(3)</font></p>
<dd> return first entry in a chain of search results</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_next_entry/">ldap_next_entry</a>(3)</font></p>
<dd> return next entry in a chain of search results</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_count_entries/">ldap_count_entries</a>(3)</font></p>
<dd> return number of entries in a search result</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_get_dn/">ldap_get_dn</a>(3)</font></p>
<dd> extract the DN from an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_get_values_len/">ldap_get_values_len</a>(3)</font></p>
<dd> return an attribute&#8217;s values with lengths</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_value_free_len/">ldap_value_free_len</a>(3)</font></p>
<dd> free memory allocated by <a href="/docs/linux/man/3-ldap_get_values_len/">ldap_get_values_len</a>(3)</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_count_values_len/">ldap_count_values_len</a>(3)</font></p>
<dd> return number of values</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_modify_ext/">ldap_modify_ext</a>(3)</font></p>
<dd> asynchronously modify an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_modify_ext_s/">ldap_modify_ext_s</a>(3)</font></p>
<dd> synchronously modify an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_mods_free/">ldap_mods_free</a>(3)</font></p>
<dd> free array of pointers to mod structures used by <a href="/docs/linux/man/3-ldap_modify_ext/">ldap_modify_ext</a>(3)</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_rename/">ldap_rename</a>(3)</font></p>
<dd> asynchronously rename an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_rename_s/">ldap_rename_s</a>(3)</font></p>
<dd> synchronously rename an entry</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_msgfree/">ldap_msgfree</a>(3)</font></p>
<dd> free results allocated by <a href="/docs/linux/man/3-ldap_result/">ldap_result</a>(3)</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_msgtype/">ldap_msgtype</a>(3)</font></p>
<dd> return the message type of a message from <a href="/docs/linux/man/3-ldap_result/">ldap_result</a>(3)</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_msgid/">ldap_msgid</a>(3)</font></p>
<dd> return the message id of a message from <a href="/docs/linux/man/3-ldap_result/">ldap_result</a>(3)</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a>(3)</font></p>
<dd> asynchronously search the directory</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_search_ext_s/">ldap_search_ext_s</a>(3)</font></p>
<dd> synchronously search the directory</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_is_ldap_url/">ldap_is_ldap_url</a>(3)</font></p>
<dd> check a URL string to see if it is an LDAP URL</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_url_parse/">ldap_url_parse</a>(3)</font></p>
<dd> break up an LDAP URL string into its components</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_sort_entries/">ldap_sort_entries</a>(3)</font></p>
<dd> sort a list of search results</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_sort_values/">ldap_sort_values</a>(3)</font></p>
<dd> sort a list of attribute values</p>
<dt><font SIZE="-1"><a href="/docs/linux/man/3-ldap_sort_strcasecmp/">ldap_sort_strcasecmp</a>(3)</font></p>
<dd> case insensitive string comparison</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code>draft-ietf-ldapext-ldap-c-api-xx.txt</code>&nbsp;<wbr>&lt;<a rel="nofollow" href="http://www.ietf.org">http://www.ietf.org</a>&gt;</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<p> These API manual pages are loosely based upon descriptions provided in the IETF/LDAPEXT C LDAP API Internet Draft, a (orphaned) work in progress. </p>
<h2>Index</h2>
