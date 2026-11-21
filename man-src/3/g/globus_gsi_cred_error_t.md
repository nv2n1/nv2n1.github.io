---

title: "globus_gsi_cred_error_t(3)"
name: "globus_gsi_cred_error_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cred_error_t/"
description: "Credential Constants –"
---

<p> Credential Constants &#8211; </p>
<h3>Enumerations</h3>
<p> enum <code>globus_gsi_cred_error_t</code> { <code>GLOBUS_GSI_CRED_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_CRED_ERROR_READING_PROXY_CRED</code> = 1, <code>GLOBUS_GSI_CRED_ERROR_READING_HOST_CRED</code> = 2, <code>GLOBUS_GSI_CRED_ERROR_READING_SERVICE_CRED</code> = 3, <code>GLOBUS_GSI_CRED_ERROR_READING_CRED</code> = 4, <code>GLOBUS_GSI_CRED_ERROR_WRITING_CRED</code> = 5, <code>GLOBUS_GSI_CRED_ERROR_WRITING_PROXY_CRED</code> = 6, <code>GLOBUS_GSI_CRED_ERROR_CHECKING_PROXY</code> = 7, <code>GLOBUS_GSI_CRED_ERROR_VERIFYING_CRED</code> = 8, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED</code> = 9, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT</code> = 10, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_PRIVATE_KEY</code> = 11, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_CHAIN</code> = 12, <code>GLOBUS_GSI_CRED_ERROR_ERRNO</code> = 13, <code>GLOBUS_GSI_CRED_ERROR_SYSTEM_CONFIG</code> = 14, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_HANDLE_ATTRS</code> = 15, <code>GLOBUS_GSI_CRED_ERROR_WITH_SSL_CTX</code> = 16, <code>GLOBUS_GSI_CRED_ERROR_WITH_CALLBACK_DATA</code> = 17, <code>GLOBUS_GSI_CRED_ERROR_CREATING_ERROR_OBJ</code> = 18, <code>GLOBUS_GSI_CRED_ERROR_KEY_IS_PASS_PROTECTED</code> = 19, <code>GLOBUS_GSI_CRED_ERROR_NO_CRED_FOUND</code> = 20, <code>GLOBUS_GSI_CRED_ERROR_SUBJECT_CMP</code> = 21, <code>GLOBUS_GSI_CRED_ERROR_GETTING_SERVICE_NAME</code> = 22, <code>GLOBUS_GSI_CRED_ERROR_BAD_PARAMETER</code> = 23, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_NAME</code> = 24, <code>GLOBUS_GSI_CRED_ERROR_LAST</code> = 25 } </p>
<p> enum <code>globus_gsi_cred_type_t</code> </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gsi_cred_error_t</code></h3>
<p> Credential Error codes </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_GSI_CRED_ERROR_SUCCESS </i></dt>
<dd> Success &#8211; never used</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_PROXY_CRED </i></dt>
<dd> Failed to read proxy credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_HOST_CRED </i></dt>
<dd> Failed to read host credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_SERVICE_CRED </i></dt>
<dd> Failed to read service credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_CRED </i></dt>
<dd> Failed to read user credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WRITING_CRED </i></dt>
<dd> Failed to write credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WRITING_PROXY_CRED </i></dt>
<dd> Failed to write proxy credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_CHECKING_PROXY </i></dt>
<dd> Error checking for proxy credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_VERIFYING_CRED </i></dt>
<dd> Failed to verify credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED </i></dt>
<dd> Invalid credential</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT </i></dt>
<dd> Invalid certificate</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_PRIVATE_KEY </i></dt>
<dd> Invalid private key</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_CHAIN </i></dt>
<dd> Invalid certificate chain</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_ERRNO </i></dt>
<dd> System error</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_SYSTEM_CONFIG </i></dt>
<dd> A Globus GSI System Configuration call failed</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_HANDLE_ATTRS </i></dt>
<dd> Invalid credential handle attributes</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_SSL_CTX </i></dt>
<dd> Faulty SSL context</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CALLBACK_DATA </i></dt>
<dd> Faulty callback data</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_CREATING_ERROR_OBJ </i></dt>
<dd> Failed to aggregate errors</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_KEY_IS_PASS_PROTECTED </i></dt>
<dd> Error reading private key &#8211; the key is password protected</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_NO_CRED_FOUND </i></dt>
<dd> Couldn&#8217;t find credential to read</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_SUBJECT_CMP </i></dt>
<dd> Credential subjects do not compare</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_GETTING_SERVICE_NAME </i></dt>
<dd> Unable to obtain service name from CN entry</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_BAD_PARAMETER </i></dt>
<dd> Invalid function parameter</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_NAME </i></dt>
<dd> Failed to process certificate subject</dd>
<dt><i>GLOBUS_GSI_CRED_ERROR_LAST </i></dt>
<dd> End marker &#8211; never used</dd></dl>
<h3>enum <code>globus_gsi_cred_type_t</code></h3>
<p> Credential Type </p>
<p> An enum representing a GSI Credential Type which holds info about the type of a particular credential. The three types of credential can be: GLOBUS_PROXY, GLOBUS_USER, or GLOBUS_HOST. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
</dt><dd> <code>Credential Handle Management</code></dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_credential from the source code. </p>
