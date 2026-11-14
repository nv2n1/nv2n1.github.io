---
title: "pam(3)"
name: "pam"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam/"
description: "pam – Pluggable Authentication Modules Library"
---

<p>pam &#8211; Pluggable Authentication Modules Library</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;
#include &lt;security/pam_modules.h&gt;
#include &lt;security/pam_ext.h&gt;</code></pre>
<h2>Description</h2>
<p><code>PAM</code> is a system of libraries that handle the authentication tasks of applications (services) on the system. The library provides a stable general interface (Application Programming Interface &#8211; API) that privilege granting programs (such as <code><a href="/docs/linux/man/1-login/">login</a></code>(1) and <code><a href="/docs/linux/man/1-su/">su</a></code>(1)) defer to to perform standard authentication tasks.</p>
<h3>Initialization and Cleanup</h3>
<p>The <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3) function creates the PAM context and initiates the PAM transaction. It is the first of the PAM functions that needs to be called by an application. The transaction state is contained entirely within the structure identified by this handle, so it is possible to have multiple transactions in parallel. But it is not possible to use the same handle for different transactions, a new one is needed for every new context. </p>
<p> The <code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3) function terminates the PAM transaction and is the last function an application should call in the PAM context. Upon return the handle pamh is no longer valid and all memory associated with it will be invalid. It can be called at any time to terminate a PAM transaction.</p>
<h3>Authentication</h3>
<p>The <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3) function is used to authenticate the user. The user is required to provide an authentication token depending upon the authentication service, usually this is a password, but could also be a finger print. </p>
<p> The <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) function manages the userscredentials.</p>
<h3>Account Management</h3>
<p>The <code><a href="/docs/linux/man/3-pam_acct_mgmt/">pam_acct_mgmt</a></code>(3) function is used to determine if the users account is valid. It checks for authentication token and account expiration and verifies access restrictions. It is typically called after the user has been authenticated.</p>
<h3>Password Management</h3>
<p>The <code><a href="/docs/linux/man/3-pam_chauthtok/">pam_chauthtok</a></code>(3) function is used to change the authentication token for a given user on request or because the token has expired.</p>
<h3>Session Management</h3>
<p>The <code><a href="/docs/linux/man/3-pam_open_session/">pam_open_session</a></code>(3) function sets up a user session for a previously successful authenticated user. The session should later be terminated with a call to <code><a href="/docs/linux/man/3-pam_close_session/">pam_close_session</a></code>(3).</p>
<h3>Conversation</h3>
<p>The PAM library uses an application-defined callback to allow a direct communication between a loaded module and the application. This callback is specified by the <i>struct pam_conv</i> passed to <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3) at the start of the transaction. See <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3) for details.</p>
<h3>Data Objects</h3>
<p>The <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3) and <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3) functions allows applications and PAM service modules to set and retrieve PAM informations. </p>
<p> The <code><a href="/docs/linux/man/3-pam_get_user/">pam_get_user</a></code>(3) function is the preferred method to obtain the username. </p>
<p> The <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3) and <code><a href="/docs/linux/man/3-pam_get_data/">pam_get_data</a></code>(3) functions allows PAM service modules to set and retrieve free-form data from one invocation to another.</p>
<h3>Environment and Error Management</h3>
<p>The <code><a href="/docs/linux/man/3-pam_putenv/">pam_putenv</a></code>(3), <code><a href="/docs/linux/man/3-pam_getenv/">pam_getenv</a></code>(3) and <code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3) functions are for maintaining a set of private environment variables. </p>
<p> The <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) function returns a pointer to a string describing the given PAM error code.</p>
<h2>Return Values</h2>
<p>The following return codes are known by PAM: </p>
<p> PAM_ABORT</p>
<dl>
<dd>Critical error, immediate abort.</dl>
<p> PAM_ACCT_EXPIRED</p>
<dl>
<dd>User account has expired.</dl>
<p> PAM_AUTHINFO_UNAVAIL</p>
<dl>
<dd>Authentication service cannot retrieve authentication info.</dl>
<p> PAM_AUTHTOK_DISABLE_AGING</p>
<dl>
<dd>Authentication token aging disabled.</dl>
<p> PAM_AUTHTOK_ERR</p>
<dl>
<dd>Authentication token manipulation error.</dl>
<p> PAM_AUTHTOK_EXPIRED</p>
<dl>
<dd>Authentication token expired.</dl>
<p> PAM_AUTHTOK_LOCK_BUSY</p>
<dl>
<dd>Authentication token lock busy.</dl>
<p> PAM_AUTHTOK_RECOVERY_ERR</p>
<dl>
<dd>Authentication information cannot be recovered.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>Conversation failure.</dl>
<p> PAM_CRED_ERR</p>
<dl>
<dd>Failure setting user credentials.</dl>
<p> PAM_CRED_EXPIRED</p>
<dl>
<dd>User credentials expired.</dl>
<p> PAM_CRED_INSUFFICIENT</p>
<dl>
<dd>Insufficient credentials to access authentication data.</dl>
<p> PAM_CRED_UNAVAIL</p>
<dl>
<dd>Authentication service cannot retrieve user credentials.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>The return value should be ignored by PAM dispatch.</dl>
<p> PAM_MAXTRIES</p>
<dl>
<dd>Have exhausted maximum number of retries for service.</dl>
<p> PAM_MODULE_UNKNOWN</p>
<dl>
<dd>Module is unknown.</dl>
<p> PAM_NEW_AUTHTOK_REQD</p>
<dl>
<dd>Authentication token is no longer valid; new one required.</dl>
<p> PAM_NO_MODULE_DATA</p>
<dl>
<dd>No module specific data is present.</dl>
<p> PAM_OPEN_ERR</p>
<dl>
<dd>Failed to load module.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Permission denied.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Error in service module.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Cannot make/remove an entry for the specified session.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<p> PAM_SYMBOL_ERR</p>
<dl>
<dd>Symbol not found.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>System error.</dl>
<p> PAM_TRY_AGAIN</p>
<dl>
<dd>Failed preliminary check by password service.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known to the underlying authentication module.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_acct_mgmt/">pam_acct_mgmt</a></code>(3), <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_chauthtok/">pam_chauthtok</a></code>(3), <code><a href="/docs/linux/man/3-pam_close_session/">pam_close_session</a></code>(3), <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3), <code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_data/">pam_get_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_getenv/">pam_getenv</a></code>(3), <code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_user/">pam_get_user</a></code>(3), <code><a href="/docs/linux/man/3-pam_open_session/">pam_open_session</a></code>(3), <code><a href="/docs/linux/man/3-pam_putenv/">pam_putenv</a></code>(3), <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3), <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3)</p>
<h2>Notes</h2>
<p>The <i>libpam</i> interfaces are only thread-safe if each thread within the multithreaded application uses its own PAM handle. </p>
