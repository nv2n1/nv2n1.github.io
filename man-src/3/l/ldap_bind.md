---
title: "ldap_bind(3)"
name: "ldap_bind"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_bind/"
description: "ldap_bind, ldap_bind_s, ldap_simple_bind, ldap_simple_bind_s, ldap_sasl_bind, ldap_sasl_bind_s, ldap_sasl_interactive_bind_s, ldap_parse_sasl_bind_result, ldap_unbind, ldap_unbind_s, ldap_unbind_ex..."
---

<h2 class="name">NAME</h2>
<p> ldap_bind, ldap_bind_s, ldap_simple_bind, ldap_simple_bind_s, ldap_sasl_bind, ldap_sasl_bind_s, ldap_sasl_interactive_bind_s, ldap_parse_sasl_bind_result, ldap_unbind, ldap_unbind_s, ldap_unbind_ext, ldap_unbind_ext_s, ldap_set_rebind_proc &#8211; LDAP bind routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_bind(LDAP *ld, const char *who, const char *cred,
              int method);

int ldap_bind_s(LDAP *ld, const char *who, const char *cred,
                int method);

int ldap_simple_bind(LDAP *ld, const char *who, const char *passwd);
int ldap_simple_bind_s(LDAP *ld, const char *who, const char *passwd);
int ldap_sasl_bind(LDAP *ld, const char *dn, const char *mechanism,
                   struct berval *cred, LDAPControl *sctrls[],
                   LDAPControl *cctrls[], int *msgidp);

int ldap_sasl_bind_s(LDAP *ld, const char *dn, const char *mechanism,
                     struct berval *cred, LDAPControl *sctrls[],
                     LDAPControl *cctrls[], struct berval **servercredp);

int ldap_parse_sasl_bind_result(LDAP *ld, LDAPMessage *res,
                                struct berval **servercredp, int freeit);

int ldap_sasl_interactive_bind_s(LDAP *ld, const char *dn,
                                 const char *mechs,
                                 LDAPControl *sctrls[], LDAPControl *cctrls[],
                                 unsigned flags, LDAP_SASL_INTERACT_PROC *interact,
                                 void *defaults);

int ldap_sasl_interactive_bind(LDAP *ld, const char *dn,
                               const char *mechs,
                               LDAPControl *sctrls[], LDAPControl *cctrls[],
                               unsigned flags, LDAP_SASL_INTERACT_PROC *interact,
                               void *defaults, LDAPMessage *result,
                               const char **rmechp, int *msgidp);

int(LDAP_SASL_INTERACT_PROC)(LDAP *ld, unsigned flags, void *defaults, void *sasl_interact);
int ldap_unbind(LDAP *ld);
int ldap_unbind_s(LDAP *ld);
int ldap_unbind_ext(LDAP *ld, LDAPControl *sctrls[],
                    LDAPControl *cctrls[]);

int ldap_unbind_ext_s(LDAP *ld, LDAPControl *sctrls[],
                      LDAPControl *cctrls[]);

int ldap_set_rebind_proc(LDAP *ld, LDAP_REBIND_PROC *ldap_proc, void *params);
int(LDAP_REBIND_PROC)(LDAP *ld, LDAP_CONST char *url, ber_tag_t request, ber_int_t msgid, void *params);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines provide various interfaces to the LDAP bind operation. After an association with an LDAP server is made using <code><a href="/docs/linux/man/3-ldap_init/">ldap_init</a></code>(3), an LDAP bind operation should be performed before other operations are attempted over the connection. An LDAP bind is required when using Version 2 of the LDAP protocol; it is optional for Version 3 but is usually needed due to security considerations. </p>
<p> There are three types of bind calls, ones providing simple authentication, ones providing SASL authentication, and general routines capable of doing either simple or SASL authentication. </p>
<p> <code>SASL</code> (Simple Authentication and Security Layer) can negotiate one of many different kinds of authentication. Both synchronous and asynchronous versions of each variant of the bind call are provided. All routines take <i>ld</i> as their first parameter, as returned from <code><a href="/docs/linux/man/3-ldap_init/">ldap_init</a></code>(3).</p>
<h2>SIMPLE AUTHENTICATION</h2>
<p> The simplest form of the bind call is <code>ldap_simple_bind_s()</code>. It takes the DN to bind as in <i>who</i>, and the userPassword associated with the entry in <i>passwd</i>. It returns an LDAP error indication (see <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)). The <code>ldap_simple_bind()</code> call is asynchronous, taking the same parameters but only initiating the bind operation and returning the message id of the request it sent. The result of the operation can be obtained by a subsequent call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3).</p>
<h2>GENERAL AUTHENTICATION</h2>
<p> The <code>ldap_bind()</code> and <code>ldap_bind_s()</code> routines can be used when the authentication method to use needs to be selected at runtime. They both take an extra <i>method</i> parameter selecting the authentication method to use. It should be set to LDAP_AUTH_SIMPLE to select simple authentication. <code>ldap_bind()</code> returns the message id of the request it initiates. <code>ldap_bind_s()</code> returns an LDAP error indication.</p>
<h2>SASL AUTHENTICATION</h2>
<p> For SASL binds the server always ignores any provided DN, so the <i>dn</i> parameter should always be NULL. <code>ldap_sasl_bind_s</code>() sends a single SASL bind request with the given SASL <i>mechanism</i> and credentials in the <i>cred</i> parameter. The format of the credentials depends on the particular SASL mechanism in use. For mechanisms that provide mutual authentication the server&#8217;s credentials will be returned in the <i>servercredp</i> parameter. The routine returns an LDAP error indication (see <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)). The <code>ldap_sasl_bind</code>() call is asynchronous, taking the same parameters but only sending the request and returning the message id of the request it sent. The result of the operation can be obtained by a subsequent call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3). The result must be additionally parsed by <code>ldap_parse_sasl_bind_result</code>() to obtain any server credentials sent from the server. </p>
<p> Many SASL mechanisms require multiple message exchanges to perform a complete authentication. Applications should generally use <code>ldap_sasl_interactive_bind_s</code>() rather than calling the basic <code>ldap_sasl_bind</code>() functions directly. The <i>mechs</i> parameter should contain a space-separated list of candidate mechanisms to use. If this parameter is NULL or empty the library will query the supportedSASLMechanisms attribute from the server&#8217;s rootDSE for the list of SASL mechanisms the server supports. The <i>flags</i> parameter controls the interaction used to retrieve any necessary SASL authentication parameters and should be one of:</p>
<dl>
<dt>LDAP_SASL_AUTOMATIC</p>
<dd> use defaults if available, prompt otherwise</p>
<dt>LDAP_SASL_INTERACTIVE</p>
<dd> always prompt</p>
<dt>LDAP_SASL_QUIET</p>
<dd> never prompt</dl>
<p> The <i>interact</i> function uses the provided <i>defaults</i> to handle requests from the SASL library for particular authentication parameters. There is no defined format for the <i>defaults</i> information; it is up to the caller to use whatever format is appropriate for the supplied <i>interact</i> function. The <i>sasl_interact</i> parameter comes from the underlying SASL library. When used with Cyrus SASL this is an array of <code>sasl_interact_t</code> structures. The Cyrus SASL library will prompt for a variety of inputs, including:</p>
<dl>
<dt>SASL_CB_GETREALM</p>
<dd> the realm for the authentication attempt</p>
<dt>SASL_CB_AUTHNAME</p>
<dd> the username to authenticate</p>
<dt>SASL_CB_PASS</p>
<dd> the password for the provided username</p>
<dt>SASL_CB_USER</p>
<dd> the username to use for proxy authorization</p>
<dt>SASL_CB_NOECHOPROMPT</p>
<dd> generic prompt for input with input echoing disabled</p>
<dt>SASL_CB_ECHOPROMPT</p>
<dd> generic prompt for input with input echoing enabled</p>
<dt>SASL_CB_LIST_END</p>
<dd> indicates the end of the array of prompts</dl>
<p> See the Cyrus SASL documentation for more details. </p>
<p> Applications which need to manage connections asynchronously may use <code>ldap_sasl_interactive_bind</code>() instead of the synchronous version. A valid mechs parameter must be supplied, otherwise the library will be forced to query the server for a list of supported mechanisms, and this query will be performed synchronously. The other parameters are the same as for the synchronous function, with three additional parameters. The actual SASL mechanism that was used, and the message ID for use with <code>ldap_result</code>() will be returned in rmechp and msgidp, respectively. The value in rmechp must not be modified by the caller and must be passed back on each subsequent call. The message obtained from <code>ldap_result</code>() must be passed in the result parameter. This parameter must be NULL when initiating a new Bind. The caller must free the result message after each call using <code>ldap_msgfree</code>(). The <code>ldap_sasl_interactive_bind</code>() function returns an LDAP result code. If the code is LDAP_SASL_BIND_IN_PROGRESS then the Bind is not complete yet, and this function must be called again with the next result from the server.</p>
<h2>REBINDING</h2>
<p> The <code>ldap_set_rebind_proc</code> function() sets the process to use for binding when an operation returns a referral. This function is used when an application needs to bind to another server in order to follow a referral or search continuation reference. </p>
<p> The function takes <i>ld</i>, the <i>rebind</i> function, and the <i>params</i>, the arbitrary data like state information which the client might need to properly rebind. The LDAP_OPT_REFERRALS option in the <i>ld</i> must be set to ON for the libraries to use the rebind function. Use the <code>ldap_set_option</code> function to set the value. </p>
<p> The rebind function parameters are as follows: </p>
<p> The <i>ld</i> parameter must be used by the application when binding to the referred server if the application wants the libraries to follow the referral. </p>
<p> The <i>url</i> parameter points to the URL referral string received from the LDAP server. The LDAP application can use the <code><a href="/docs/linux/man/3-ldap_url_parse/">ldap_url_parse</a></code>(3) function to parse the string into its components. </p>
<p> The <i>request</i> parameter specifies the type of request that generated the referral. </p>
<p> The <i>msgid</i> parameter specifies the message ID of the request generating the referral. </p>
<p> The <i>params</i> parameter is the same value as passed originally to the <code>ldap_set_rebind_proc</code>() function. </p>
<p> The LDAP libraries set all the parameters when they call the rebind function. The application should not attempt to free either the ld or the url structures in the rebind function. </p>
<p> The application must supply to the rebind function the required authentication information such as, user name, password, and certificates. The rebind function must use a synchronous bind method.</p>
<h2>UNBINDING</h2>
<p> The <code>ldap_unbind()</code> call is used to unbind from the directory, terminate the current association, and free the resources contained in the <i>ld</i> structure. Once it is called, the connection to the LDAP server is closed, and the <i>ld</i> structure is invalid. The <code>ldap_unbind_s()</code> call is just another name for <code>ldap_unbind()</code>; both of these calls are synchronous in nature. </p>
<p> The <code>ldap_unbind_ext()</code> and <code>ldap_unbind_ext_s()</code> allows the operations to specify controls.</p>
<h2>ERRORS</h2>
<p> Asynchronous routines will return -1 in case of error, setting the <i>ld_errno</i> parameter of the <i>ld</i> structure. Synchronous routines return whatever <i>ld_errno</i> is set to. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for more information.</p>
<h2>NOTES</h2>
<p> If an anonymous bind is sufficient for the application, the rebind process need not be provided. The LDAP libraries with the LDAP_OPT_REFERRALS option set to ON (default value) will automatically follow referrals using an anonymous bind. </p>
<p> If the application needs stronger authentication than an anonymous bind, you need to provide a rebind process for that authentication method. The bind method must be synchronous.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3), <code><a href="/docs/linux/man/3-ldap_open/">ldap_open</a></code>(3), <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3), <code><a href="/docs/linux/man/3-ldap_url_parse/">ldap_url_parse</a></code>(3) <code>RFC 4422</code> (<a rel="nofollow" href="http://www.rfc-editor.org">http://www.rfc-editor.org</a>), <code>Cyrus SASL</code> (<a rel="nofollow" href="http://asg.web.cmu.edu/sasl/)">http://asg.web.cmu.edu/sasl/)</a></p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
