---
title: "globus_gsi_cred_error_reading_cred(3)"
name: "globus_gsi_cred_error_reading_cred"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cred_error_reading_cred/"
description: "Credential Constants –"
---

<p>Credential Constants &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gsi_cred_error_t</code> { <code>GLOBUS_GSI_CRED_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_CRED_ERROR_READING_PROXY_CRED</code> = 1, <code>GLOBUS_GSI_CRED_ERROR_READING_HOST_CRED</code> = 2, <code>GLOBUS_GSI_CRED_ERROR_READING_SERVICE_CRED</code> = 3, <code>GLOBUS_GSI_CRED_ERROR_READING_CRED</code> = 4, <code>GLOBUS_GSI_CRED_ERROR_WRITING_CRED</code> = 5, <code>GLOBUS_GSI_CRED_ERROR_WRITING_PROXY_CRED</code> = 6, <code>GLOBUS_GSI_CRED_ERROR_CHECKING_PROXY</code> = 7, <code>GLOBUS_GSI_CRED_ERROR_VERIFYING_CRED</code> = 8, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED</code> = 9, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT</code> = 10, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_PRIVATE_KEY</code> = 11, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_CHAIN</code> = 12, <code>GLOBUS_GSI_CRED_ERROR_ERRNO</code> = 13, <code>GLOBUS_GSI_CRED_ERROR_SYSTEM_CONFIG</code> = 14, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_HANDLE_ATTRS</code> = 15, <code>GLOBUS_GSI_CRED_ERROR_WITH_SSL_CTX</code> = 16, <code>GLOBUS_GSI_CRED_ERROR_WITH_CALLBACK_DATA</code> = 17, <code>GLOBUS_GSI_CRED_ERROR_CREATING_ERROR_OBJ</code> = 18, <code>GLOBUS_GSI_CRED_ERROR_KEY_IS_PASS_PROTECTED</code> = 19, <code>GLOBUS_GSI_CRED_ERROR_NO_CRED_FOUND</code> = 20, <code>GLOBUS_GSI_CRED_ERROR_SUBJECT_CMP</code> = 21, <code>GLOBUS_GSI_CRED_ERROR_GETTING_SERVICE_NAME</code> = 22, <code>GLOBUS_GSI_CRED_ERROR_BAD_PARAMETER</code> = 23, <code>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_NAME</code> = 24, <code>GLOBUS_GSI_CRED_ERROR_LAST</code> = 25 } </p>
<p> enum <code>globus_gsi_cred_type_t</code> </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gsi_cred_error_t</code></h3>
<p>Credential Error codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GSI_CRED_ERROR_SUCCESS </i></p>
<dd>Success &#8211; never used</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_PROXY_CRED </i></p>
<dd>Failed to read proxy credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_HOST_CRED </i></p>
<dd>Failed to read host credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_SERVICE_CRED </i></p>
<dd>Failed to read service credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_READING_CRED </i></p>
<dd>Failed to read user credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WRITING_CRED </i></p>
<dd>Failed to write credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WRITING_PROXY_CRED </i></p>
<dd>Failed to write proxy credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_CHECKING_PROXY </i></p>
<dd>Error checking for proxy credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_VERIFYING_CRED </i></p>
<dd>Failed to verify credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED </i></p>
<dd>Invalid credential</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT </i></p>
<dd>Invalid certificate</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_PRIVATE_KEY </i></p>
<dd>Invalid private key</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_CHAIN </i></p>
<dd>Invalid certificate chain</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_ERRNO </i></p>
<dd>System error</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_SYSTEM_CONFIG </i></p>
<dd>A Globus GSI System Configuration call failed</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_HANDLE_ATTRS </i></p>
<dd>Invalid credential handle attributes</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_SSL_CTX </i></p>
<dd>Faulty SSL context</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CALLBACK_DATA </i></p>
<dd>Faulty callback data</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_CREATING_ERROR_OBJ </i></p>
<dd>Failed to aggregate errors</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_KEY_IS_PASS_PROTECTED </i></p>
<dd>Error reading private key &#8211; the key is password protected</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_NO_CRED_FOUND </i></p>
<dd>Couldn&#8217;t find credential to read</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_SUBJECT_CMP </i></p>
<dd>Credential subjects do not compare</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_GETTING_SERVICE_NAME </i></p>
<dd>Unable to obtain service name from CN entry</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_BAD_PARAMETER </i></p>
<dd>Invalid function parameter</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_WITH_CRED_CERT_NAME </i></p>
<dd>Failed to process certificate subject</p>
<dt><i>GLOBUS_GSI_CRED_ERROR_LAST </i></p>
<dd>End marker &#8211; never used</dl>
<h3>enum <code>globus_gsi_cred_type_t</code></h3>
<p>Credential Type </p>
<p> An enum representing a GSI Credential Type which holds info about the type of a particular credential. The three types of credential can be: GLOBUS_PROXY, GLOBUS_USER, or GLOBUS_HOST. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Credential Handle Management</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_credential from the source code.</p>
