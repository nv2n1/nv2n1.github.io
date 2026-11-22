---

title: "ld_errno(3)"
name: "ld_errno"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ld_errno/"
description: "ldap_perror, ld_errno, ldap_result2error, ldap_errlist, ldap_err2string – LDAP protocol error handling routines"
---

<p> ldap_perror, ld_errno, ldap_result2error, ldap_errlist, ldap_err2string &#8211; LDAP protocol error handling routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
char *ldap_err2string(int err);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_err2string()</code> routine provides short description of the various codes returned by routines in this library. The returned string is a pointer to a static area that should not be modified. </p>
<p> These codes are either negative, indicating an API error code; positive, indicating an LDAP resultCode other than &#8216;success&#8217; (0), or &#8211; zero, indicating both successful use of the API and the LDAP resultCode &#8216;success&#8217; (0). </p>
<p> The code associated with an LDAP session is accessible using <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3) and <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3) with the <code>LDAP_OPT_RESULT_CODE</code> option (previously called <code>LDAP_OPT_ERROR_NUMBER</code>). </p>
<h2>PROTOCOL RESULT CODES</h2>
<p> This section provides a partial list of protocol codes recognized by the library. As LDAP is extensible, additional values may be returned. A complete listing of <i>registered</i> LDAP result codes can be obtained from the <i>Internet Assigned Numbers Authority</i> &lt;<a rel="nofollow" href="http://www.iana.org">http://www.iana.org</a>&gt;. </p>
<dl>
<dt>LDAP_SUCCESS</dt>
<dd> The request was successful.</dd>
<dt>LDAP_OPERATIONS_ERROR</dt>
<dd> An operations error occurred.</dd>
<dt>LDAP_PROTOCOL_ERROR</dt>
<dd> A protocol violation was detected.</dd>
<dt>LDAP_TIMELIMIT_EXCEEDED</dt>
<dd> An LDAP time limit was exceeded.</dd>
<dt>LDAP_SIZELIMIT_EXCEEDED</dt>
<dd> An LDAP size limit was exceeded.</dd>
<dt>LDAP_COMPARE_FALSE</dt>
<dd> A compare operation returned false.</dd>
<dt>LDAP_COMPARE_TRUE</dt>
<dd> A compare operation returned true.</dd>
<dt>LDAP_STRONG_AUTH_NOT_SUPPORTED</dt>
<dd> The LDAP server does not support strong authentication.</dd>
<dt>LDAP_STRONG_AUTH_REQUIRED</dt>
<dd> Strong authentication is required for the operation.</dd>
<dt>LDAP_PARTIAL_RESULTS</dt>
<dd> Partial results only returned.</dd>
<dt>LDAP_NO_SUCH_ATTRIBUTE</dt>
<dd> The attribute type specified does not exist in the entry.</dd>
<dt>LDAP_UNDEFINED_TYPE</dt>
<dd> The attribute type specified is invalid.</dd>
<dt>LDAP_INAPPROPRIATE_MATCHING</dt>
<dd> Filter type not supported for the specified attribute.</dd>
<dt>LDAP_CONSTRAINT_VIOLATION</dt>
<dd> An attribute value specified violates some constraint (e.g., a postalAddress has too many lines, or a line that is too long).</dd>
<dt>LDAP_TYPE_OR_VALUE_EXISTS</dt>
<dd> An attribute type or attribute value specified already exists in the entry.</dd>
<dt>LDAP_INVALID_SYNTAX</dt>
<dd> An invalid attribute value was specified.</dd>
<dt>LDAP_NO_SUCH_OBJECT</dt>
<dd> The specified object does not exist in The Directory.</dd>
<dt>LDAP_ALIAS_PROBLEM</dt>
<dd> An alias in The Directory points to a nonexistent entry.</dd>
<dt>LDAP_INVALID_DN_SYNTAX</dt>
<dd> A syntactically invalid DN was specified.</dd>
<dt>LDAP_IS_LEAF</dt>
<dd> The object specified is a leaf.</dd>
<dt>LDAP_ALIAS_DEREF_PROBLEM</dt>
<dd> A problem was encountered when dereferencing an alias.</dd>
<dt>LDAP_INAPPROPRIATE_AUTH</dt>
<dd> Inappropriate authentication was specified (e.g., LDAP_AUTH_SIMPLE was specified and the entry does not have a userPassword attribute).</dd>
<dt>LDAP_INVALID_CREDENTIALS</dt>
<dd> Invalid credentials were presented (e.g., the wrong password).</dd>
<dt>LDAP_INSUFFICIENT_ACCESS</dt>
<dd> The user has insufficient access to perform the operation.</dd>
<dt>LDAP_BUSY</dt>
<dd> The DSA is busy.</dd>
<dt>LDAP_UNAVAILABLE</dt>
<dd> The DSA is unavailable.</dd>
<dt>LDAP_UNWILLING_TO_PERFORM</dt>
<dd> The DSA is unwilling to perform the operation.</dd>
<dt>LDAP_LOOP_DETECT</dt>
<dd> A loop was detected.</dd>
<dt>LDAP_NAMING_VIOLATION</dt>
<dd> A naming violation occurred.</dd>
<dt>LDAP_OBJECT_CLASS_VIOLATION</dt>
<dd> An object class violation occurred (e.g., a &quot;must&quot; attribute was missing from the entry).</dd>
<dt>LDAP_NOT_ALLOWED_ON_NONLEAF</dt>
<dd> The operation is not allowed on a nonleaf object.</dd>
<dt>LDAP_NOT_ALLOWED_ON_RDN</dt>
<dd> The operation is not allowed on an RDN.</dd>
<dt>LDAP_ALREADY_EXISTS</dt>
<dd> The entry already exists.</dd>
<dt>LDAP_NO_OBJECT_CLASS_MODS</dt>
<dd> Object class modifications are not allowed.</dd>
<dt>LDAP_OTHER</dt>
<dd> An unknown error occurred. </dd>
</dl>
<h2>API ERROR CODES</h2>
<p> This section provides a complete list of API error codes recognized by the library. Note that LDAP_SUCCESS indicates success of an API call in addition to representing the return of the LDAP &#8216;success&#8217; resultCode. </p>
<dl>
<dt>LDAP_SERVER_DOWN</dt>
<dd> The LDAP library can&#8217;t contact the LDAP server.</dd>
<dt>LDAP_LOCAL_ERROR</dt>
<dd> Some local error occurred. This is usually a failed dynamic memory allocation.</dd>
<dt>LDAP_ENCODING_ERROR</dt>
<dd> An error was encountered encoding parameters to send to the LDAP server.</dd>
<dt>LDAP_DECODING_ERROR</dt>
<dd> An error was encountered decoding a result from the LDAP server.</dd>
<dt>LDAP_TIMEOUT</dt>
<dd> A timelimit was exceeded while waiting for a result.</dd>
<dt>LDAP_AUTH_UNKNOWN</dt>
<dd> The authentication method specified to ldap_bind() is not known.</dd>
<dt>LDAP_FILTER_ERROR</dt>
<dd> An invalid filter was supplied to ldap_search() (e.g., unbalanced parentheses).</dd>
<dt>LDAP_PARAM_ERROR</dt>
<dd> An ldap routine was called with a bad parameter.</dd>
<dt>LDAP_NO_MEMORY</dt>
<dd> An memory allocation (e.g., <a href="/docs/linux/man/3-malloc/">malloc</a>(3) or other dynamic memory allocator) call failed in an ldap library routine.</dd>
<dt>LDAP_USER_CANCELED</dt>
<dd> Indicates the user cancelled the operation.</dd>
<dt>LDAP_CONNECT_ERROR</dt>
<dd> Indicates a connection problem.</dd>
<dt>LDAP_NOT_SUPPORTED</dt>
<dd> Indicates the routine was called in a manner not supported by the library.</dd>
<dt>LDAP_CONTROL_NOT_FOUND</dt>
<dd> Indicates the control provided is unknown to the client library.</dd>
<dt>LDAP_NO_RESULTS_RETURNED</dt>
<dd> Indicates no results returned.</dd>
<dt>LDAP_MORE_RESULTS_TO_RETURN</dt>
<dd> Indicates more results could be returned.</dd>
<dt>LDAP_CLIENT_LOOP</dt>
<dd> Indicates the library has detected a loop in its processing.</dd>
<dt>LDAP_REFERRAL_LIMIT_EXCEEDED</dt>
<dd> Indicates the referral limit has been exceeded. </dd>
</dl>
<h2>DEPRECATED</h2>
<p> Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3),</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
