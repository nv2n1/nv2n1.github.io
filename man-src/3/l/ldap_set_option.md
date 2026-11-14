---
title: "ldap_set_option(3)"
name: "ldap_set_option"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_set_option/"
description: "ldap_get_option, ldap_set_option – LDAP option handling routines"
---

<h2 class="name">NAME</h2>
<p> ldap_get_option, ldap_set_option &#8211; LDAP option handling routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_get_option(LDAP *ld, int option, void *outvalue);
int ldap_set_option(LDAP *ld, int option, const void *invalue);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines provide access to options stored either in a LDAP handle or as global options, where applicable. They make use of a neutral interface, where the type of the value either retrieved by <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3) or set by <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3) is cast to <code>void *</code>. The actual type is determined based on the value of the <code>option</code> argument. Global options are set/retrieved by passing a NULL LDAP handle. LDAP handles inherit their default settings from the global options in effect at the time the handle is created.</p>
<dl>
<dt><code>LDAP_OPT_API_FEATURE_INFO</code></p>
<dd> Fills-in a <code>LDAPAPIFeatureInfo</code>; <code>outvalue</code> must be a <code>LDAPAPIFeatureInfo *</code>, pointing to an already allocated struct. The <code>ldapaif_info_version</code> field of the struct must be initialized to <code>LDAP_FEATURE_INFO_VERSION</code> before making the call. The <code>ldapaif_name</code> field must be set to the name of a feature to query. This is a read-only option.</p>
<dt><code>LDAP_OPT_API_INFO</code></p>
<dd> Fills-in a <code>LDAPAPIInfo</code>; <code>outvalue</code> must be a <code>LDAPAPIInfo *</code>, pointing to an already allocated struct. The <code>ldapai_info_version</code> field of the struct must be initialized to <code>LDAP_API_INFO_VERSION</code> before making the call. If the version passed in does not match the current library version, the expected version number will be stored in the struct and the call will fail. The caller is responsible for freeing the elements of the <code>ldapai_extensions</code> array and the array itself using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). The caller must also free the <code>ldapi_vendor_name</code>. This is a read-only option.</p>
<dt><code>LDAP_OPT_CLIENT_CONTROLS</code></p>
<dd> Sets/gets the client-side controls to be used for all operations. This is now deprecated as modern LDAP C API provides replacements for all main operations which accepts client-side controls as explicit arguments; see for example <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3), <code><a href="/docs/linux/man/3-ldap_add_ext/">ldap_add_ext</a></code>(3), <code><a href="/docs/linux/man/3-ldap_modify_ext/">ldap_modify_ext</a></code>(3) and so on. <code>outvalue</code> must be <code>LDAPControl ***</code>, and the caller is responsible of freeing the returned controls, if any, by calling <code><a href="/docs/linux/man/3-ldap_controls_free/">ldap_controls_free</a></code>(3), while <code>invalue</code> must be <code>LDAPControl *const *</code>; the library duplicates the controls passed via <code>invalue</code>.</p>
<dt><code>LDAP_OPT_CONNECT_ASYNC</code></p>
<dd> Sets/gets the status of the asynchronous connect flag. <code>invalue</code> should either be <code>LDAP_OPT_OFF</code> or <code>LDAP_OPT_ON</code>; <code>outvalue</code> must be <code>int *</code>. When set, the library will call <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) and return, without waiting for response. This leaves the handle in a connecting state. Subsequent calls to library routines will poll for completion of the connect before performing further operations. As a consequence, library calls that need to establish a connection with a DSA do not block even for the network timeout (option <code>LDAP_OPT_NETWORK_TIMEOUT</code>). This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_CONNECT_CB</code></p>
<dd> This option allows to set a connect callback. <code>invalue</code> must be a <code>const struct ldap_conncb *</code>. Callbacks are executed in last in-first served order. Handle-specific callbacks are executed first, followed by global ones. Right before freeing the callback structure, the <code>lc_del</code> callback handler is passed a <code>NULL</code> <code>Sockbuf</code>. Calling <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3) for this option removes the callback whose pointer matches <code>outvalue</code>. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_DEBUG_LEVEL</code></p>
<dd> Sets/gets the debug level of the client library. <code>invalue</code> must be a <code>const int *</code>; <code>outvalue</code> must be a <code>int *</code>. Valid debug levels are <code>LDAP_DEBUG_ANY</code>, <code>LDAP_DEBUG_ARGS</code>, <code>LDAP_DEBUG_BER</code>, <code>LDAP_DEBUG_CONNS</code>, <code>LDAP_DEBUG_NONE</code>, <code>LDAP_DEBUG_PACKETS</code>, <code>LDAP_DEBUG_PARSE</code>, and <code>LDAP_DEBUG_TRACE</code>. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_DEFBASE</code></p>
<dd> Sets/gets a string containing the DN to be used as default base for search operations. <code>outvalue</code> must be a <code>char **</code>, and the caller is responsible of freeing the returned string by calling <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), while <code>invalue</code> must be a <code>const char *</code>; the library duplicates the corresponding string. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_DEREF</code></p>
<dd> Sets/gets the value that defines when alias dereferencing must occur. <code>invalue</code> must be <code>const int *</code>; <code>outvalue</code> must be <code>int *</code>. They cannot be NULL. The value of <code>*invalue</code> should be one of <code>LDAP_DEREF_NEVER</code> (the default), <code>LDAP_DEREF_SEARCHING</code>, <code>LDAP_DEREF_FINDING</code>, or <code>LDAP_DEREF_ALWAYS</code>. Note that this has ever been the only means to determine alias dereferencing within search operations.</p>
<dt><code>LDAP_OPT_DESC</code></p>
<dd> Returns the file descriptor associated to the socket buffer of the LDAP handle passed in as <code>ld</code>; <code>outvalue</code> must be a <code>int *</code>. This is a read-only, handle-specific option.</p>
<dt><code>LDAP_OPT_DIAGNOSTIC_MESSAGE</code></p>
<dd> Sets/gets a string containing the error string associated to the LDAP handle. This option was formerly known as <code>LDAP_OPT_ERROR_STRING</code>. <code>outvalue</code> must be a <code>char **</code>, and the caller is responsible of freeing the returned string by calling <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), while <code>invalue</code> must be a <code>char *</code>; the library duplicates the corresponding string.</p>
<dt><code>LDAP_OPT_HOST_NAME</code></p>
<dd> Sets/gets a space-separated list of hosts to be contacted by the library when trying to establish a connection. This is now deprecated in favor of <code>LDAP_OPT_URI</code>. <code>outvalue</code> must be a <code>char **</code>, and the caller is responsible of freeing the resulting string by calling <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), while <code>invalue</code> must be a <code>const char *</code>; the library duplicates the corresponding string.</p>
<dt><code>LDAP_OPT_MATCHED_DN</code></p>
<dd> Sets/gets a string containing the matched DN associated to the LDAP handle. <code>outvalue</code> must be a <code>char **</code>, and the caller is responsible of freeing the returned string by calling <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), while <code>invalue</code> must be a <code>const char *</code>; the library duplicates the corresponding string.</p>
<dt><code>LDAP_OPT_NETWORK_TIMEOUT</code></p>
<dd> Sets/gets the network timeout value after which <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)/<code><a href="/docs/linux/man/2-select/">select</a></code>(2) following a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) returns in case of no activity. <code>outvalue</code> must be a <code>struct timeval **</code> (the caller has to free <code>*outvalue</code>)<code>,</code> and <code>invalue</code> must be a <code>const struct timeval *</code>. They cannot be NULL. Using a struct with seconds set to -1 results in an infinite timeout, which is the default. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_PROTOCOL_VERSION</code></p>
<dd> Sets/gets the protocol version. <code>outvalue</code> and <code>invalue</code> must be <code>int *</code>.</p>
<dt><code>LDAP_OPT_REFERRAL_URLS</code></p>
<dd> Sets/gets an array containing the referral URIs associated to the LDAP handle. <code>outvalue</code> must be a <code>char ***</code>, and the caller is responsible of freeing the returned string by calling <code><a href="/docs/linux/man/3-ldap_memvfree/">ldap_memvfree</a></code>(3), while <code>invalue</code> must be a NULL-terminated <code>char *const *</code>; the library duplicates the corresponding string. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_REFERRALS</code></p>
<dd> Determines whether the library should implicitly chase referrals or not. <code>invalue</code> must be <code>const int *</code>; its value should either be <code>LDAP_OPT_OFF</code> or <code>LDAP_OPT_ON</code>. <code>outvalue</code> must be <code>int *</code>.</p>
<dt><code>LDAP_OPT_RESTART</code></p>
<dd> Determines whether the library should implicitly restart connections (FIXME). <code>invalue</code> must be <code>const int *</code>; its value should either be <code>LDAP_OPT_OFF</code> or <code>LDAP_OPT_ON</code>. <code>outvalue</code> must be <code>int *</code>.</p>
<dt><code>LDAP_OPT_RESULT_CODE</code></p>
<dd> Sets/gets the LDAP result code associated to the handle. This option was formerly known as <code>LDAP_OPT_ERROR_NUMBER</code>. <code>invalue</code> must be a <code>const int *</code>. <code>outvalue</code> must be a <code>int *</code>.</p>
<dt><code>LDAP_OPT_SERVER_CONTROLS</code></p>
<dd> Sets/gets the server-side controls to be used for all operations. This is now deprecated as modern LDAP C API provides replacements for all main operations which accepts server-side controls as explicit arguments; see for example <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3), <code><a href="/docs/linux/man/3-ldap_add_ext/">ldap_add_ext</a></code>(3), <code><a href="/docs/linux/man/3-ldap_modify_ext/">ldap_modify_ext</a></code>(3) and so on. <code>outvalue</code> must be <code>LDAPControl ***</code>, and the caller is responsible of freeing the returned controls, if any, by calling <code><a href="/docs/linux/man/3-ldap_controls_free/">ldap_controls_free</a></code>(3), while <code>invalue</code> must be <code>LDAPControl *const *</code>; the library duplicates the controls passed via <code>invalue</code>.</p>
<dt><code>LDAP_OPT_SESSION_REFCNT</code></p>
<dd> Returns the reference count associated with the LDAP handle passed in as <code>ld</code>; <code>outvalue</code> must be a <code>int *</code>. This is a read-only, handle-specific option. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_SIZELIMIT</code></p>
<dd> Sets/gets the value that defines the maximum number of entries to be returned by a search operation. <code>invalue</code> must be <code>const int *</code>, while <code>outvalue</code> must be <code>int *</code>; They cannot be NULL.</p>
<dt><code>LDAP_OPT_SOCKBUF</code></p>
<dd> Returns a pointer to the socket buffer of the LDAP handle passed in as <code>ld</code>; <code>outvalue</code> must be a <code>Sockbuf **</code>. This is a read-only, handle-specific option. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_TIMELIMIT</code></p>
<dd> Sets/gets the value that defines the time limit after which a search operation should be terminated by the server. <code>invalue</code> must be <code>const int *</code>, while <code>outvalue</code> must be <code>int *</code>, and they cannot be NULL.</p>
<dt><code>LDAP_OPT_TIMEOUT</code></p>
<dd> Sets/gets a timeout value for the synchronous API calls. <code>outvalue</code> must be a <code>struct timeval **</code> (the caller has to free <code>*outvalue</code>)<code>,</code> and <code>invalue</code> must be a <code>struct timeval *</code>, and they cannot be NULL. Using a struct with seconds set to -1 results in an infinite timeout, which is the default. This option is OpenLDAP specific.</p>
<dt><code>LDAP_OPT_URI</code></p>
<dd> Sets/gets a comma- or space-separated list of URIs to be contacted by the library when trying to establish a connection. <code>outvalue</code> must be a <code>char **</code>, and the caller is responsible of freeing the resulting string by calling <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), while <code>invalue</code> must be a <code>const char *</code>; the library parses the string into a list of <code>LDAPURLDesc</code> structures, so the invocation of <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3) may fail if URL parsing fails. URIs may only contain the <code>schema</code>, the <code>host</code>, and the <code>port</code> fields. This option is OpenLDAP specific.</dl>
<h2>SASL OPTIONS</h2>
<p> The SASL options are OpenLDAP specific.</p>
<dl>
<dt><code>LDAP_OPT_X_SASL_AUTHCID</code></p>
<dd> Gets the SASL authentication identity; <code>outvalue</code> must be a <code>char **</code>, its content needs to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_SASL_AUTHZID</code></p>
<dd> Gets the SASL authorization identity; <code>outvalue</code> must be a <code>char **</code>, its content needs to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_SASL_MAXBUFSIZE</code></p>
<dd> Gets/sets SASL maximum buffer size; <code>invalue</code> must be <code>const ber_len_t *</code>, while <code>outvalue</code> must be <code>ber_len_t *</code>. See also <code>LDAP_OPT_X_SASL_SECPROPS</code>.</p>
<dt><code>LDAP_OPT_X_SASL_MECH</code></p>
<dd> Gets the SASL mechanism; <code>outvalue</code> must be a <code>char **</code>, its content needs to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_SASL_MECHLIST</code></p>
<dd> Gets the list of the available mechanisms, in form of a NULL-terminated array of strings; <code>outvalue</code> must be <code>char ***</code>. The caller must not free or otherwise muck with it.</p>
<dt><code>LDAP_OPT_X_SASL_NOCANON</code></p>
<dd> Sets/gets the NOCANON flag. When unset, the hostname is canonicalized. <code>invalue</code> must be <code>const int *</code>; its value should either be <code>LDAP_OPT_OFF</code> or <code>LDAP_OPT_ON</code>. <code>outvalue</code> must be <code>int *</code>.</p>
<dt><code>LDAP_OPT_X_SASL_REALM</code></p>
<dd> Gets the SASL realm; <code>outvalue</code> must be a <code>char **</code>, its content needs to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_SASL_SECPROPS</code></p>
<dd> Sets the SASL secprops; <code>invalue</code> must be a <code>char *</code>, containing a comma-separated list of properties. Legal values are: <code>none</code>, <code>nodict</code>, <code>noplain</code>, <code>noactive</code>, <code>passcred</code>, <code>forwardsec</code>, <code>noanonymous</code>, <code>minssf=&lt;minssf&gt;</code>, <code>maxssf=&lt;maxssf&gt;</code>, <code>maxbufsize=&lt;maxbufsize&gt;</code>.</p>
<dt><code>LDAP_OPT_X_SASL_SSF</code></p>
<dd> Gets the SASL SSF; <code>outvalue</code> must be a <code>ber_len_t *</code>.</p>
<dt><code>LDAP_OPT_X_SASL_SSF_EXTERNAL</code></p>
<dd> Sets the SASL SSF value related to an authentication performed using an EXTERNAL mechanism; <code>invalue</code> must be a <code>const ber_len_t *</code>.</p>
<dt><code>LDAP_OPT_X_SASL_SSF_MAX</code></p>
<dd> Gets/sets SASL maximum SSF; <code>invalue</code> must be <code>const ber_len_t *</code>, while <code>outvalue</code> must be <code>ber_len_t *</code>. See also <code>LDAP_OPT_X_SASL_SECPROPS</code>.</p>
<dt><code>LDAP_OPT_X_SASL_SSF_MIN</code></p>
<dd> Gets/sets SASL minimum SSF; <code>invalue</code> must be <code>const ber_len_t *</code>, while <code>outvalue</code> must be <code>ber_len_t *</code>. See also <code>LDAP_OPT_X_SASL_SECPROPS</code>.</p>
<dt><code>LDAP_OPT_X_SASL_USERNAME</code></p>
<dd> Gets the SASL username; <code>outvalue</code> must be a <code>char **</code>. Its content needs to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</dl>
<h2>TCP OPTIONS</h2>
<p> The TCP options are OpenLDAP specific. Mainly intended for use with Linux, they may not be portable.</p>
<dl>
<dt><code>LDAP_OPT_X_KEEPALIVE_IDLE</code></p>
<dd> Sets/gets the number of seconds a connection needs to remain idle before TCP starts sending keepalive probes. <code>invalue</code> must be <code>const int *</code>; <code>outvalue</code> must be <code>int *</code>.</p>
<dt><code>LDAP_OPT_X_KEEPALIVE_PROBES</code></p>
<dd> Sets/gets the maximum number of keepalive probes TCP should send before dropping the connection. <code>invalue</code> must be <code>const int *</code>; <code>outvalue</code> must be <code>int *</code>.</p>
<dt><code>LDAP_OPT_X_KEEPALIVE_INTERVAL</code></p>
<dd> Sets/gets the interval in seconds between individual keepalive probes. <code>invalue</code> must be <code>const int *</code>; <code>outvalue</code> must be <code>int *</code>.</dl>
<h2>TLS OPTIONS</h2>
<p> The TLS options are OpenLDAP specific.</p>
<dl>
<dt><code>LDAP_OPT_X_TLS_CACERTDIR</code></p>
<dd> Sets/gets the path of the directory containing CA certificates. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_TLS_CACERTFILE</code></p>
<dd> Sets/gets the full-path of the CA certificate file. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_TLS_CERTFILE</code></p>
<dd> Sets/gets the full-path of the certificate file. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_TLS_CIPHER_SUITE</code></p>
<dd> Sets/gets the allowed cipher suite. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_TLS_CONNECT_ARG</code></p>
<dd> Sets/gets the connection callback argument. <code>invalue</code> must be <code>const void *</code>; <code>outvalue</code> must be <code>void **</code>.</p>
<dt><code>LDAP_OPT_X_TLS_CONNECT_CB</code></p>
<dd> Sets/gets the connection callback handle. <code>invalue</code> must be <code>const LDAP_TLS_CONNECT_CB *</code>; <code>outvalue</code> must be <code>LDAP_TLS_CONNECT_CB **</code>.</p>
<dt><code>LDAP_OPT_X_TLS_CRLCHECK</code></p>
<dd> Sets/gets the CRL evaluation strategy, one of <code>LDAP_OPT_X_TLS_CRL_NONE</code>, <code>LDAP_OPT_X_TLS_CRL_PEER</code>, or <code>LDAP_OPT_X_TLS_CRL_ALL</code>. <code>invalue</code> must be <code>const int *</code>; <code>outvalue</code> must be <code>int *</code>. Requires OpenSSL.</p>
<dt><code>LDAP_OPT_X_TLS_CRLFILE</code></p>
<dd> Sets/gets the full-path of the CRL file. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). This option is only valid for GnuTLS.</p>
<dt><code>LDAP_OPT_X_TLS_CTX</code></p>
<dd> Sets/gets the TLS library context. New TLS sessions will inherit their default settings from this library context. <code>invalue</code> must be <code>const void *</code>; <code>outvalue</code> must be <code>void **</code>. When using the OpenSSL library this is an SSL_CTX*. When using other crypto libraries this is a pointer to an OpenLDAP private structure. Applications generally should not use this option or attempt to manipulate this structure.</p>
<dt><code>LDAP_OPT_X_TLS_DHFILE</code></p>
<dd> Gets/sets the full-path of the file containing the parameters for Diffie-Hellman ephemeral key exchange. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). Ignored by GnuTLS and Mozilla NSS.</p>
<dt><code>LDAP_OPT_X_TLS_KEYFILE</code></p>
<dd> Sets/gets the full-path of the certificate key file. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<dt><code>LDAP_OPT_X_TLS_NEWCTX</code></p>
<dd> Instructs the library to create a new TLS library context. <code>invalue</code> must be <code>const int *</code>. A non-zero value pointed to by <code>invalue</code> tells the library to create a context for a server.</p>
<dt><code>LDAP_OPT_X_TLS_PROTOCOL_MIN</code></p>
<dd> Sets/gets the minimum protocol version. <code>invalue</code> must be <code>const int *</code>; <code>outvalue</code> must be <code>int *</code>.</p>
<dt><code>LDAP_OPT_X_TLS_RANDOM_FILE</code></p>
<dd> Sets/gets the random file when <code>/dev/random</code> and <code>/dev/urandom</code> are not available. <code>invalue</code> must be <code>const char *</code>; <code>outvalue</code> must be <code>char **</code>, and its contents need to be freed by the caller using <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3). Ignored by GnuTLS older than version 2.2. Ignored by Mozilla NSS.</p>
<dt><code>LDAP_OPT_X_TLS_REQUIRE_CERT</code></p>
<dd> Sets/gets the peer certificate checking strategy, one of <code>LDAP_OPT_X_TLS_NEVER</code>, <code>LDAP_OPT_X_TLS_HARD</code>, <code>LDAP_OPT_X_TLS_DEMAND</code>, <code>LDAP_OPT_X_TLS_ALLOW</code>, <code>LDAP_OPT_X_TLS_TRY</code>.</p>
<dt><code>LDAP_OPT_X_TLS_SSL_CTX</code></p>
<dd> Gets the TLS session context associated with this handle. <code>outvalue</code> must be <code>void **</code>. When using the OpenSSL library this is an SSL*. When using other crypto libraries this is a pointer to an OpenLDAP private structure. Applications generally should not use this option.</dl>
<h2>ERRORS</h2>
<p> On success, the functions return <code>LDAP_OPT_SUCCESS</code>, while they may return <code>LDAP_OPT_ERROR</code> to indicate a generic option handling error. Occasionally, more specific errors can be returned, like <code>LDAP_NO_MEMORY</code> to indicate a failure in memory allocation.</p>
<h2>NOTES</h2>
<p> The LDAP libraries with the <code>LDAP_OPT_REFERRALS </code> option set to <code>LDAP_OPT_ON</code> (default value) automatically follow referrals using an anonymous bind. Application developers are encouraged to either implement consistent referral chasing features, or explicitly disable referral chasing by setting that option to <code>LDAP_OPT_OFF</code>. </p>
<p> The protocol version used by the library defaults to LDAPv2 (now historic), which corresponds to the <code>LDAP_VERSION2</code> macro. Application developers are encouraged to explicitly set <code>LDAP_OPT_PROTOCOL_VERSION</code> to LDAPv3, using the <code>LDAP_VERSION3</code> macro, or to allow users to select the protocol version.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3), <code>RFC 4422</code> (<a rel="nofollow" href="http://www.rfc-editor.org">http://www.rfc-editor.org</a>),</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
