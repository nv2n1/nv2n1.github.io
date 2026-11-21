---

title: "ldap_perror(3)"
name: "ldap_perror"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_perror/"
description: "ldap_perror, ld_errno, ldap_result2error, ldap_errlist, ldap_err2string – LDAP protocol error handling routines"
---

<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<pre><code>
#include &lt;ldap.h&gt;
char *ldap_err2string(int err);
</code></pre>
<p> The <code>ldap_err2string()</code> routine provides short description of the various codes returned by routines in this library. The returned string is a pointer to a static area that should not be modified. </p>
<p> These codes are either negative, indicating an API error code; positive, indicating an LDAP resultCode other than &#8216;success&#8217; (0), or &#8211; zero, indicating both successful use of the API and the LDAP resultCode &#8216;success&#8217; (0). </p>
<p> The code associated with an LDAP session is accessible using <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3) and <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3) with the <code>LDAP_OPT_RESULT_CODE</code> option (previously called <code>LDAP_OPT_ERROR_NUMBER</code>). </p>
<h2>PROTOCOL RESULT CODES</h2>
<p> This section provides a partial list of protocol codes recognized by the library. As LDAP is extensible, additional values may be returned. A complete listing of <i>registered</i> LDAP result codes can be obtained from the <i>Internet Assigned Numbers Authority</i> &lt;<a rel="nofollow" href="http://www.iana.org">http://www.iana.org</a>&gt;. </p>
<dl>
<dt><font SIZE="-1">LDAP_SUCCESS</font></dt>
<dd> The request was successful.</dd>
<dt><font SIZE="-1">LDAP_OPERATIONS_ERROR</font></dt>
<dd> An operations error occurred.</dd>
<dt><font SIZE="-1">LDAP_PROTOCOL_ERROR</font></dt>
<dd> A protocol violation was detected.</dd>
<dt><font SIZE="-1">LDAP_TIMELIMIT_EXCEEDED</font></dt>
<dd> An LDAP time limit was exceeded.</dd>
<dt><font SIZE="-1">LDAP_SIZELIMIT_EXCEEDED</font></dt>
<dd> An LDAP size limit was exceeded.</dd>
<dt><font SIZE="-1">LDAP_COMPARE_FALSE</font></dt>
<dd> A compare operation returned false.</dd>
<dt><font SIZE="-1">LDAP_COMPARE_TRUE</font></dt>
<dd> A compare operation returned true.</dd>
<dt><font SIZE="-1">LDAP_STRONG_AUTH_NOT_SUPPORTED</font></dt>
<dd> The LDAP server does not support strong authentication.</dd>
<dt><font SIZE="-1">LDAP_STRONG_AUTH_REQUIRED</font></dt>
<dd> Strong authentication is required for the operation.</dd>
<dt><font SIZE="-1">LDAP_PARTIAL_RESULTS</font></dt>
<dd> Partial results only returned.</dd>
<dt><font SIZE="-1">LDAP_NO_SUCH_ATTRIBUTE</font></dt>
<dd> The attribute type specified does not exist in the entry.</dd>
<dt><font SIZE="-1">LDAP_UNDEFINED_TYPE</font></dt>
<dd> The attribute type specified is invalid.</dd>
<dt><font SIZE="-1">LDAP_INAPPROPRIATE_MATCHING</font></dt>
<dd> Filter type not supported for the specified attribute.</dd>
<dt><font SIZE="-1">LDAP_CONSTRAINT_VIOLATION</font></dt>
<dd> An attribute value specified violates some constraint (e.g., a postalAddress has too many lines, or a line that is too long).</dd>
<dt><font SIZE="-1">LDAP_TYPE_OR_VALUE_EXISTS</font></dt>
<dd> An attribute type or attribute value specified already exists in the entry.</dd>
<dt><font SIZE="-1">LDAP_INVALID_SYNTAX</font></dt>
<dd> An invalid attribute value was specified.</dd>
<dt><font SIZE="-1">LDAP_NO_SUCH_OBJECT</font></dt>
<dd> The specified object does not exist in The Directory.</dd>
<dt><font SIZE="-1">LDAP_ALIAS_PROBLEM</font></dt>
<dd> An alias in The Directory points to a nonexistent entry.</dd>
<dt><font SIZE="-1">LDAP_INVALID_DN_SYNTAX</font></dt>
<dd> A syntactically invalid DN was specified.</dd>
<dt><font SIZE="-1">LDAP_IS_LEAF</font></dt>
<dd> The object specified is a leaf.</dd>
<dt><font SIZE="-1">LDAP_ALIAS_DEREF_PROBLEM</font></dt>
<dd> A problem was encountered when dereferencing an alias.</dd>
<dt><font SIZE="-1">LDAP_INAPPROPRIATE_AUTH</font></dt>
<dd> Inappropriate authentication was specified (e.g., LDAP_AUTH_SIMPLE was specified and the entry does not have a userPassword attribute).</dd>
<dt><font SIZE="-1">LDAP_INVALID_CREDENTIALS</font></dt>
<dd> Invalid credentials were presented (e.g., the wrong password).</dd>
<dt><font SIZE="-1">LDAP_INSUFFICIENT_ACCESS</font></dt>
<dd> The user has insufficient access to perform the operation.</dd>
<dt><font SIZE="-1">LDAP_BUSY</font></dt>
<dd> The DSA is busy.</dd>
<dt><font SIZE="-1">LDAP_UNAVAILABLE</font></dt>
<dd> The DSA is unavailable.</dd>
<dt><font SIZE="-1">LDAP_UNWILLING_TO_PERFORM</font></dt>
<dd> The DSA is unwilling to perform the operation.</dd>
<dt><font SIZE="-1">LDAP_LOOP_DETECT</font></dt>
<dd> A loop was detected.</dd>
<dt><font SIZE="-1">LDAP_NAMING_VIOLATION</font></dt>
<dd> A naming violation occurred.</dd>
<dt><font SIZE="-1">LDAP_OBJECT_CLASS_VIOLATION</font></dt>
<dd> An object class violation occurred (e.g., a &quot;must&quot; attribute was missing from the entry).</dd>
<dt><font SIZE="-1">LDAP_NOT_ALLOWED_ON_NONLEAF</font></dt>
<dd> The operation is not allowed on a nonleaf object.</dd>
<dt><font SIZE="-1">LDAP_NOT_ALLOWED_ON_RDN</font></dt>
<dd> The operation is not allowed on an RDN.</dd>
<dt><font SIZE="-1">LDAP_ALREADY_EXISTS</font></dt>
<dd> The entry already exists.</dd>
<dt><font SIZE="-1">LDAP_NO_OBJECT_CLASS_MODS</font></dt>
<dd> Object class modifications are not allowed.</dd>
<dt><font SIZE="-1">LDAP_OTHER</font></dt>
<dd> An unknown error occurred. </dd>
</dl>
<h2>API ERROR CODES</h2>
<p> This section provides a complete list of API error codes recognized by the library. Note that LDAP_SUCCESS indicates success of an API call in addition to representing the return of the LDAP &#8216;success&#8217; resultCode. </p>
<dl>
<dt><font SIZE="-1">LDAP_SERVER_DOWN</font></dt>
<dd> The LDAP library can&#8217;t contact the LDAP server.</dd>
<dt><font SIZE="-1">LDAP_LOCAL_ERROR</font></dt>
<dd> Some local error occurred. This is usually a failed dynamic memory allocation.</dd>
<dt><font SIZE="-1">LDAP_ENCODING_ERROR</font></dt>
<dd> An error was encountered encoding parameters to send to the LDAP server.</dd>
<dt><font SIZE="-1">LDAP_DECODING_ERROR</font></dt>
<dd> An error was encountered decoding a result from the LDAP server.</dd>
<dt><font SIZE="-1">LDAP_TIMEOUT</font></dt>
<dd> A timelimit was exceeded while waiting for a result.</dd>
<dt><font SIZE="-1">LDAP_AUTH_UNKNOWN</font></dt>
<dd> The authentication method specified to ldap_bind() is not known.</dd>
<dt><font SIZE="-1">LDAP_FILTER_ERROR</font></dt>
<dd> An invalid filter was supplied to ldap_search() (e.g., unbalanced parentheses).</dd>
<dt><font SIZE="-1">LDAP_PARAM_ERROR</font></dt>
<dd> An ldap routine was called with a bad parameter.</dd>
<dt><font SIZE="-1">LDAP_NO_MEMORY</font></dt>
<dd> An memory allocation (e.g., <a href="/docs/linux/man/3-malloc/">malloc</a>(3) or other dynamic memory allocator) call failed in an ldap library routine.</dd>
<dt><font SIZE="-1">LDAP_USER_CANCELED</font></dt>
<dd> Indicates the user cancelled the operation.</dd>
<dt><font SIZE="-1">LDAP_CONNECT_ERROR</font></dt>
<dd> Indicates a connection problem.</dd>
<dt><font SIZE="-1">LDAP_NOT_SUPPORTED</font></dt>
<dd> Indicates the routine was called in a manner not supported by the library.</dd>
<dt><font SIZE="-1">LDAP_CONTROL_NOT_FOUND</font></dt>
<dd> Indicates the control provided is unknown to the client library.</dd>
<dt><font SIZE="-1">LDAP_NO_RESULTS_RETURNED</font></dt>
<dd> Indicates no results returned.</dd>
<dt><font SIZE="-1">LDAP_MORE_RESULTS_TO_RETURN</font></dt>
<dd> Indicates more results could be returned.</dd>
<dt><font SIZE="-1">LDAP_CLIENT_LOOP</font></dt>
<dd> Indicates the library has detected a loop in its processing.</dd>
<dt><font SIZE="-1">LDAP_REFERRAL_LIMIT_EXCEEDED</font></dt>
<dd> Indicates the referral limit has been exceeded. </dd>
</dl>
<h2>DEPRECATED</h2>
<p> Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3),</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
