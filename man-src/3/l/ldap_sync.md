---
title: "ldap_sync(3)"
name: "ldap_sync"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_sync/"
description: "ldap_sync_init, ldap_sync_init_refresh_only, ldap_sync_init_refresh_and_persist, ldap_sync_poll – LDAP sync routines"
---

<h2 class="name">NAME</h2>
<p> ldap_sync_init, ldap_sync_init_refresh_only, ldap_sync_init_refresh_and_persist, ldap_sync_poll &#8211; LDAP sync routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_sync_init(ldap_sync_t *ls, int mode);
int ldap_sync_init_refresh_only(ldap_sync_t *ls);
int ldap_sync_init_refresh_and_persist(ldap_sync_t *ls);
int ldap_sync_poll(ldap_sync_t *ls);
ldap_sync_t *ldap_sync_initialize(ldap_sync_t *ls);
void ldap_sync_destroy(ldap_sync_t *ls, int freeit);
typedef int (*ldap_sync_search_entry_f)(ldap_sync_t *ls,
                                        LDAPMessage *msg, struct berval *entryUUID,
                                        ldap_sync_refresh_t phase);

typedef int (*ldap_sync_search_reference_f)(ldap_sync_t *ls,
                                            LDAPMessage *msg);

typedef int (*ldap_sync_intermediate_f)(ldap_sync_t *ls,
                                        LDAPMessage *msg, BerVarray syncUUIDs,
                                        ldap_sync_refresh_t phase);

typedef int (*ldap_sync_search_result_f)(ldap_sync_t *ls,
                                         LDAPMessage *msg, int refreshDeletes);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines provide an interface to the LDAP Content Synchronization operation (RFC 4533). They require an <code>ldap_sync_t</code> structure to be set up with parameters required for various phases of the operation; this includes setting some handlers for special events. All handlers take a pointer to the <code>ldap_sync_t</code> structure as the first argument, and a pointer to the <code>LDAPMessage</code> structure as received from the server by the client library, plus, occasionally, other specific arguments. </p>
<p> The members of the <code>ldap_sync_t</code> structure are:</p>
<dl>
<dt><code>char *</code><i>ls_base</i></p>
<dd> The search base; by default, the <code>BASE</code> option in <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5).</p>
<dt><code>int </code><i>ls_scope</i></p>
<dd> The search scope (one of <code>LDAP_SCOPE_BASE</code>, <code>LDAP_SCOPE_ONELEVEL</code>, <code>LDAP_SCOPE_SUBORDINATE</code> or <code>LDAP_SCOPE_SUBTREE</code>; see <code>ldap.h</code> for details).</p>
<dt><code>char *</code><i>ls_filter</i></p>
<dd> The filter (RFC 4515); by default, <code>(objectClass=*)</code>.</p>
<dt><code>char **</code><i>ls_attrs</i></p>
<dd> The requested attributes; by default <code>NULL</code>, indicating all user attributes.</p>
<dt><code>int </code><i>ls_timelimit</i></p>
<dd> The requested time limit (in seconds); by default <code>0</code>, to indicate no limit.</p>
<dt><code>int </code><i>ls_sizelimit</i></p>
<dd> The requested size limit (in entries); by default <code>0</code>, to indicate no limit.</p>
<dt><code>int </code><i>ls_timeout</i></p>
<dd> The desired timeout during polling with <code><a href="/docs/linux/man/3-ldap_sync_poll/">ldap_sync_poll</a></code>(3). A value of <code>-1</code> means that polling is blocking, so <code><a href="/docs/linux/man/3-ldap_sync_poll/">ldap_sync_poll</a></code>(3) will not return until a message is received; a value of <code>0</code> means that polling returns immediately, no matter if any response is available or not; a positive value represents the timeout the <code><a href="/docs/linux/man/3-ldap_sync_poll/">ldap_sync_poll</a></code>(3) function will wait for response before returning, unless a message is received; in that case, <code><a href="/docs/linux/man/3-ldap_sync_poll/">ldap_sync_poll</a></code>(3) returns as soon as the message is available.</p>
<dt><code>ldap_sync_search_entry_f </code><i>ls_search_entry</i></p>
<dd> A function that is called whenever an entry is returned. The <code>msg</code> argument is the <code>LDAPMessage</code> that contains the searchResultEntry; it can be parsed using the regular client API routines, like <code><a href="/docs/linux/man/3-ldap_get_dn/">ldap_get_dn</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_attribute/">ldap_first_attribute</a></code>(3), and so on. The <code>entryUUID</code> argument contains the entryUUID of the entry. The <code>phase</code> argument indicates the type of operation: one of <code>LDAP_SYNC_CAPI_PRESENT</code>, <code>LDAP_SYNC_CAPI_ADD</code>, <code>LDAP_SYNC_CAPI_MODIFY</code>, <code>LDAP_SYNC_CAPI_DELETE</code>; in case of <code>LDAP_SYNC_CAPI_PRESENT</code> or <code>LDAP_SYNC_CAPI_DELETE</code>, only the DN is contained in the <i>LDAPMessage</i>; in case of <code>LDAP_SYNC_CAPI_MODIFY</code>, the whole entry is contained in the <i>LDAPMessage</i>, and the application is responsible of determining the differences between the new view of the entry provided by the caller and the data already known.</p>
<dt><code>ldap_sync_search_reference_f </code><i>ls_search_reference</i></p>
<dd> A function that is called whenever a search reference is returned. The <code>msg</code> argument is the <code>LDAPMessage</code> that contains the searchResultReference; it can be parsed using the regular client API routines, like <code><a href="/docs/linux/man/3-ldap_parse_reference/">ldap_parse_reference</a></code>(3).</p>
<dt><code>ldap_sync_intermediate_f </code><i>ls_intermediate</i></p>
<dd> A function that is called whenever something relevant occurs during the refresh phase of the search, which is marked by an <i>intermediateResponse</i> message type. The <code>msg</code> argument is the <code>LDAPMessage</code> that contains the intermediate response; it can be parsed using the regular client API routines, like <code><a href="/docs/linux/man/3-ldap_parse_intermediate/">ldap_parse_intermediate</a></code>(3). The <code>syncUUIDs</code> argument contains an array of UUIDs of the entries that depends on the value of the <code>phase</code> argument. In case of <code>LDAP_SYNC_CAPI_PRESENTS</code>, the &quot;present&quot; phase is being entered; this means that the following sequence of results will consist in entries in &quot;present&quot; sync state. In case of <code>LDAP_SYNC_CAPI_DELETES</code>, the &quot;deletes&quot; phase is being entered; this means that the following sequence of results will consist in entries in &quot;delete&quot; sync state. In case of <code>LDAP_SYNC_CAPI_PRESENTS_IDSET</code>, the message contains a set of UUIDs of entries that are present; it replaces a &quot;presents&quot; phase. In case of <code>LDAP_SYNC_CAPI_DELETES_IDSET</code>, the message contains a set of UUIDs of entries that have been deleted; it replaces a &quot;deletes&quot; phase. In case of <code>LDAP_SYNC_CAPI_DONE,</code> a &quot;presents&quot; phase with &quot;refreshDone&quot; set to &quot;TRUE&quot; has been returned to indicate that the refresh phase of refreshAndPersist is over, and the client should start polling. Except for the <code>LDAP_SYNC_CAPI_PRESENTS_IDSET</code> and <code>LDAP_SYNC_CAPI_DELETES_IDSET</code> cases, <code>syncUUIDs</code> is NULL.</p>
<dt><code>ldap_sync_search_result_f </code><i>ls_search_result</i></p>
<dd> A function that is called whenever a searchResultDone is returned. In refreshAndPersist this can only occur when the server decides that the search must be interrupted. The <code>msg</code> argument is the <code>LDAPMessage</code> that contains the response; it can be parsed using the regular client API routines, like <code><a href="/docs/linux/man/3-ldap_parse_result/">ldap_parse_result</a></code>(3). The <code>refreshDeletes</code> argument is not relevant in this case; it should always be -1.</p>
<dt><code>void *</code><i>ls_private</i></p>
<dd> A pointer to private data. The client may register here a pointer to data the handlers above may need.</p>
<dt><code>LDAP *</code><i>ls_ld</i></p>
<dd> A pointer to a LDAP structure that is used to connect to the server. It is the responsibility of the client to initialize the structure and to provide appropriate authentication and security in place. </p>
</dl>
<h2>GENERAL USE</h2>
<p> A <code>ldap_sync_t</code> structure is initialized by calling <code><a href="/docs/linux/man/3-ldap_sync_initialize/">ldap_sync_initialize</a>(3).</code> This simply clears out the contents of an already existing <code>ldap_sync_t</code> structure, and sets appropriate values for some members. After that, the caller is responsible for setting up the connection (member <code>ls_ld</code>), eventually setting up transport security (TLS), for binding and any other initialization. The caller must also fill all the documented search-related fields of the <code>ldap_sync_t</code> structure. </p>
<p> At the end of a session, the structure can be cleaned up by calling <code><a href="/docs/linux/man/3-ldap_sync_destroy/">ldap_sync_destroy</a></code>(3), which takes care of freeing all data assuming it was allocated by <code>ldap_mem*</code>(3) routines. Otherwise, the caller should take care of destroying and zeroing out the documented search-related fields, and call <code><a href="/docs/linux/man/3-ldap_sync_destroy/">ldap_sync_destroy</a></code>(3) to free undocumented members set by the API. </p>
<h2>REFRESH ONLY</h2>
<p> The <code>refreshOnly</code> functionality is obtained by periodically calling <code><a href="/docs/linux/man/3-ldap_sync_init/">ldap_sync_init</a></code>(3) with mode set to <code>LDAP_SYNC_REFRESH_ONLY</code>, or, which is equivalent, by directly calling <code><a href="/docs/linux/man/3-ldap_sync_init_refresh_only/">ldap_sync_init_refresh_only</a></code>(3). The state of the search, and the consistency of the search parameters, is preserved across calls by passing the <code>ldap_sync_t</code> structure as left by the previous call. </p>
<h2>REFRESH AND PERSIST</h2>
<p> The <code>refreshAndPersist</code> functionality is obtained by calling <code><a href="/docs/linux/man/3-ldap_sync_init/">ldap_sync_init</a></code>(3) with mode set to <code>LDAP_SYNC_REFRESH_AND_PERSIST</code>, or, which is equivalent, by directly calling <code><a href="/docs/linux/man/3-ldap_sync_init_refresh_and_persist/">ldap_sync_init_refresh_and_persist</a></code>(3) and, after a successful return, by repeatedly polling with <code><a href="/docs/linux/man/3-ldap_sync_poll/">ldap_sync_poll</a></code>(3) according to the desired pattern. </p>
<p> A client may insert a call to <code><a href="/docs/linux/man/3-ldap_sync_poll/">ldap_sync_poll</a></code>(3) into an external loop to check if any modification was returned; in this case, it might be appropriate to set <code>ls_timeout</code> to 0, or to set it to a finite, small value. Otherwise, if the client&#8217;s main purpose consists in waiting for responses, a timeout of -1 is most suitable, so that the function only returns after some data has been received and handled. </p>
<h2>ERRORS</h2>
<p> All routines return any LDAP error resulting from a lower-level error in the API calls they are based on, or LDAP_SUCCESS in case of success. <code><a href="/docs/linux/man/3-ldap_sync_poll/">ldap_sync_poll</a></code>(3) may return <code>LDAP_SYNC_REFRESH_REQUIRED</code> if a full refresh is requested by the server. In this case, it is appropriate to call <code><a href="/docs/linux/man/3-ldap_sync_init/">ldap_sync_init</a></code>(3) again, passing the same <code>ldap_sync_t</code> structure as resulted from any previous call.</p>
<h2>NOTES</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3)<code>;</code> <code>RFC 4533</code> (<a rel="nofollow" href="http://www.rfc-editor.org">http://www.rfc-editor.org</a>),</p>
<h2>AUTHOR</h2>
<p> Designed and implemented by Pierangelo Masarati, based on RFC 4533 and loosely inspired by syncrepl code in <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8).</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Initially developed by <code>SysNet s.n.c.</code> <code>OpenLDAP</code> is developed and maintained by The OpenLDAP Project (<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>). <code>OpenLDAP</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
