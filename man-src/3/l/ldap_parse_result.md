---
title: "ldap_parse_result(3)"
name: "ldap_parse_result"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_parse_result/"
description: "ldap_parse_result – Parsing results"
---

<h2 class="name">NAME</h2>
<p> ldap_parse_result &#8211; Parsing results </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_parse_result(LDAP *ld, LDAPMessage *result,
                      int *errcodep, char **matcheddnp, char **errmsgp,
                      char ***referralsp, LDAPControl ***serverctrlsp,
                      int freeit) int ldap_parse_sasl_bind_result(LDAP *ld, LDAPMessage *result,
                                                                  struct berval **servercredp, int freeit) int ldap_parse_extended_result(LDAP *ld, LDAPMessage *result,
                                                                                                                                          char **retoidp, struct berval **retdatap, int freeit)
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to extract information from a result message. They will operate on the first result message in a chain of search results (skipping past other message types). They take the <i>result</i> as returned by a call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search_s/">ldap_search_s</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_search_st/">ldap_search_st</a></code>(3). In addition to <code>ldap_parse_result()</code>, the routines <code>ldap_parse_sasl_bind_result()</code> and <code>ldap_parse_extended_result()</code> are used to get all the result information from SASL bind and extended operations. </p>
<p> The <i>errcodep</i> parameter will be filled in with the result code from the result message. </p>
<p> The server might supply a matched DN string in the message indicating how much of a name in a request was recognized. The <i>matcheddnp</i> parameter will be filled in with this string if supplied, else it will be NULL. If a string is returned, it should be freed using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). </p>
<p> The <i>errmsgp</i> parameter will be filled in with the error message field from the parsed message. This string should be freed using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). </p>
<p> The <i>referralsp</i> parameter will be filled in with an allocated array of referral strings from the parsed message. This array should be freed using <code><a href="/docs/linux/man/3-ldap_memvfree/">ldap_memvfree</a></code>(3). If no referrals were returned, <i>*referralsp</i> is set to NULL. </p>
<p> The <i>serverctrlsp</i> parameter will be filled in with an allocated array of controls copied from the parsed message. The array should be freed using <code><a href="/docs/linux/man/3-ldap_controls_free/">ldap_controls_free</a></code>(3). If no controls were returned, <i>*serverctrlsp</i> is set to NULL. </p>
<p> The <i>freeit</i> parameter determines whether the parsed message is freed or not after the extraction. Any non-zero value will make it free the message. The <code><a href="/docs/linux/man/3-ldap_msgfree/">ldap_msgfree</a></code>(3) routine can also be used to free the message later. </p>
<p> For SASL bind results, the <i>servercredp</i> parameter will be filled in with an allocated berval structure containing the credentials from the server if present. The structure should be freed using <code><a href="/docs/linux/man/3-ber_bvfree/">ber_bvfree</a></code>(3). </p>
<p> For extended results, the <i>retoidp</i> parameter will be filled in with the dotted-OID text representation of the name of the extended operation response. The string should be freed using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). If no OID was returned, <i>*retoidp</i> is set to NULL. </p>
<p> For extended results, the <i>retdatap</i> parameter will be filled in with a pointer to a berval structure containing the data from the extended operation response. The structure should be freed using <code><a href="/docs/linux/man/3-ber_bvfree/">ber_bvfree</a></code>(3). If no data were returned, <i>*retdatap</i> is set to NULL. </p>
<p> For all the above result parameters, NULL values can be used in calls in order to ignore certain fields.</p>
<h2>ERRORS</h2>
<p> Upon success LDAP_SUCCESS is returned. Otherwise the values of the result parameters are undefined.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search/">ldap_search</a></code>(3), <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), <code><a href="/docs/linux/man/3-ldap_memvfree/">ldap_memvfree</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_values/">ldap_get_values</a></code>(3), <code><a href="/docs/linux/man/3-ldap_controls_free/">ldap_controls_free</a></code>(3), <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
