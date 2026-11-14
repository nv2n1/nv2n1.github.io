---
title: "vomsdata(3)"
name: "vomsdata"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vomsdata/"
description: "vomsdata –"
---

<p>vomsdata &#8211;</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;voms_api.h&gt;

Public Member Functions
vomsdata (std::string voms_dir='', std::string cert_dir='')



bool LoadSystemContacts (std::string dir='')



bool LoadUserContacts (std::string dir='')



std::vector&lt; contactdata &gt; FindByAlias (std::string alias)



std::vector&lt; contactdata &gt; FindByVO (std::string vo)



void Order (std::string att)



void ResetOrder (void)



void AddTarget (std::string target)



std::vector&lt; std::string &gt; ListTargets (void)



void ResetTargets (void)



std::string ServerErrors (void)



bool Retrieve (X509 *cert, STACK_OF(X509)*chain, recurse_type how=RECURSE_CHAIN)



bool Contact (std::string hostname, int port, std::string servsubject, std::string command)



bool Contact (std::string hostname, int port, std::string servsubject, std::string command, int timeout)



bool ContactRaw (std::string hostname, int port, std::string servsubject, std::string command, std::string &amp;raw, int &amp;version)



bool ContactRaw (std::string hostname, int port, std::string servsubject, std::string command, std::string &amp;raw, int &amp;version, int timeout)



void SetVerificationType (verify_type how)



void SetLifetime (int lifetime)



bool Import (std::string buffer)



bool Export (std::string &amp;data)



bool DefaultData (voms &amp;)



std::string ErrorMessage (void)



bool RetrieveFromCtx (gss_ctx_id_t context, recurse_type how)



bool RetrieveFromCred (gss_cred_id_t credential, recurse_type how)



bool Retrieve (X509_EXTENSION *ext)



bool RetrieveFromProxy (recurse_type how)



bool Retrieve (FILE *file, recurse_type how)



bool Retrieve (AC *ac)



~vomsdata ()



vomsdata (const vomsdata &amp;)



void SetRetryCount (int retryCount)



void SetVerificationTime (time_t)



bool LoadCredentials (X509 *, EVP_PKEY *, STACK_OF(X509)*)



bool ContactRESTRaw (const std::string &amp;, int, const std::string &amp;, std::string &amp;, int, int)



Data Fields</code></pre>
<p> <code>verror_type</code> <code>error</code> </p>
<p> std::vector&lt; <code>voms</code> &gt; <code>data</code> </p>
<p> std::string <code>workvo</code> </p>
<p> std::string <code>extra_data</code></p>
<h2>Detailed Description</h2>
<p>Definition at line 194 of file voms_api.h.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>vomsdata::vomsdata (std::stringvoms_dir = &#8221;, std::stringcert_dir = &#8221;)</h3>
<p><code>Parameters:</code></p>
<dl>
<dd><i>voms_dir</i> The directory which contains the certificate of the VOMS server<br />
 <i>cert_dir</i> The directory which contains the certificate of the CA</dl>
<p> If voms_dir is empty, the value of the environment variable X509_VOMS_DIR is taken. </p>
<p> If cert_dir is empty, the value of the environment variable X509_CERT_DIR is taken.</p>
<h3>vomsdata::~vomsdata ()</h3>
<h3>vomsdata::vomsdata (const <code>vomsdata</code> &amp;)</h3>
<h2>Member Function Documentation</h2>
<h3>void vomsdata::AddTarget (std::stringtarget)</h3>
<p>Adds a target to the AC. </p>
<pre> <br>
aram target The target to be added. it should be a FQDN.</pre>
<p>&nbsp;<wbr></p>
<h3>bool vomsdata::Contact (std::stringhostname, intport, std::stringservsubject, std::stringcommand)</h3>
<p>Contacts a VOMS server to get a certificate </p>
<pre> It is the equivalent of the voms_proxy_init command, but 
 without the --include functionality.
 <br>
aram hostname FQDN of the VOMS server
 <br>
aram port the port on which the VOMS server is listening
 <br>
aram servsubject the subject of the server's certificate
 <br>
aram command the command sent to the server
 eturn failure (F) or success (T)</pre>
<p>&nbsp;<wbr></p>
<h3>bool vomsdata::Contact (std::stringhostname, intport, std::stringservsubject, std::stringcommand, inttimeout)</h3>
<p>Contacts a VOMS server to get a certificate </p>
<pre> It is the equivalent of the voms_proxy_init command, but 
 without the --include functionality.
 <br>
aram hostname FQDN of the VOMS server
 <br>
aram port the port on which the VOMS server is listening
 <br>
aram servsubject the subject of the server's certificate
 <br>
aram command the command sent to the server
 <br>
aram timeout Timeout for server connections in seconds
 eturn failure (F) or success (T)</pre>
<p>&nbsp;<wbr></p>
<h3>bool vomsdata::ContactRaw (std::stringhostname, intport, std::stringservsubject, std::stringcommand, std::string &amp;raw, int &amp;version)</h3>
<p>Same as Contact, however it does not start the verification process, and the message receviedfrom the server is not parsed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hostname</i> FQDN of the VOMS server<br />
 <i>port</i> the port on which the VOMS server is listening<br />
 <i>servsubject</i> the subject of the server&#8217;s certificate<br />
 <i>command</i> the command sent to the server<br />
 <i>raw</i> OUTPUT PARAMETER the answer from the server<br />
 <i>version</i> OUTPUT PARAMETER the version of the answer</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>bool vomsdata::ContactRaw (std::stringhostname, intport, std::stringservsubject, std::stringcommand, std::string &amp;raw, int &amp;version, inttimeout)</h3>
<p>Same as Contact, however it does not start the verification process, and the message receviedfrom the server is not parsed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hostname</i> FQDN of the VOMS server<br />
 <i>port</i> the port on which the VOMS server is listening<br />
 <i>servsubject</i> the subject of the server&#8217;s certificate<br />
 <i>command</i> the command sent to the server<br />
 <i>raw</i> OUTPUT PARAMETER the answer from the server<br />
 <i>version</i> OUTPUT PARAMETER the version of the answer<br />
 <i>timeout</i> Timeout for server connections in seconds</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>bool vomsdata::ContactRESTRaw (const std::string &amp;, int, const std::string &amp;, std::string &amp;, int, int)</h3>
<h3>bool vomsdata::DefaultData (<code>voms</code> &amp;)</h3>
<p>Get the default data extension from those present in the pseudo certificate</p>
<h3>std::string vomsdata::ErrorMessage (void)</h3>
<pre> Gets a textual description of the error.</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Returns:</code></p>
<dl>
<dd>A string containg the error message.</dl>
<h3>bool vomsdata::Export (std::string &amp;data)</h3>
<p>Exports data from <code>vomsdata::data</code> to the format used for inclusion into a certificate. </p>
<p> The function doesn&#8217;t verify the data </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>data</i> The certificate extension</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Failure (F) or Success (T)</dl>
<h3>std::vector&lt;<code>contactdata</code>&gt; vomsdata::FindByAlias (std::stringalias)</h3>
<p>Finds servers which share a common alias. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>alias</i> The alias to look for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The servers found. The order in which they are returned is unspecified.</dl>
<h3>std::vector&lt;<code>contactdata</code>&gt; vomsdata::FindByVO (std::stringvo)</h3>
<p>Finds servers which serve a common VO </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vo</i> The VO name to look for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The servers found. The order in which they are returned is unspecified.</dl>
<h3>bool vomsdata::Import (std::stringbuffer)</h3>
<p>Converts data from the format used for inclusion into a certificate to the internal format </p>
<p> The function does verify the data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buffer</i> contains the data to be converted</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Failure (F) or Success (T)</dl>
<h3>std::vector&lt;std::string&gt; vomsdata::ListTargets (void)</h3>
<p>Returns the list of targets.</p>
<h3>bool vomsdata::LoadCredentials (X509 *, EVP_PKEY *, STACK_OF(X509)*)</h3>
<h3>bool vomsdata::LoadSystemContacts (std::stringdir = &#8221;)</h3>
<p>Loads the system wide configuration files. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>dir</i> The directory in which the files are stored.</dl>
<p> If dir is empty, defaults to /opt/edg/etc/vomses. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>True if all went OK, false otherwise.</dl>
<h3>bool vomsdata::LoadUserContacts (std::stringdir = &#8221;)</h3>
<p>Loads the user-specific configuration files. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>dir</i> The directory in which the files are stored.</dl>
<p> If dir is empty, defaults to $VOMS_USERCONF. If this is empty too, defaults to $HOME/.edg/vomses, or to ~/.edg/vomses as a last resort. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>True if all went OK, false otherwise.</dl>
<h3>void vomsdata::Order (std::stringatt)</h3>
<p>Sets up the ordering of the results. </p>
<pre> Defines the ordering of the data returned by Contact(). Results are
 ordered in the same order as the calls to this function.
 <br>
aram att The attribute to be ordered.</pre>
<p>&nbsp;<wbr></p>
<h3>void vomsdata::ResetOrder (void)</h3>
<p>Resets the ordering.</p>
<h3>void vomsdata::ResetTargets (void)</h3>
<p>Resets the target list.</p>
<h3>bool vomsdata::Retrieve (X509 *cert, STACK_OF(X509)*chain, <code>recurse_type</code>how = <code>RECURSE_CHAIN</code>)</h3>
<p>Extracts the VOMS extension from an X.509 certificate. The function doesn&#8217;t check the validity of the certificates, but it does check the content of the user data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>cert</i> The certificate with the VOMS extensions<br />
 <i>chain</i> The chain of the validation certificates (only the intermediate ones)<br />
 <i>how</i> Recursion type</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>bool vomsdata::Retrieve (X509_EXTENSION *ext)</h3>
<pre> Gets VOMS information from the given extension</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ext</i> The extension to parse.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>bool vomsdata::Retrieve (FILE *file, <code>recurse_type</code>how)</h3>
<p>Gets VOMS information from a proxy saved as a file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>file</i> the file name<br />
 <i>how</i> Recursion type</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<p> Note: Does NOT verify that the proxy is valid. Such verification must be obtained through other means.</p>
<h3>bool vomsdata::Retrieve (AC *ac)</h3>
<pre> Gets VOMS information from the AC</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ac</i> The extension to parse.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>bool vomsdata::RetrieveFromCred (<code>gss_cred_id_t</code>credential, <code>recurse_type</code>how)</h3>
<pre> Gets VOMS information from the given globus credential</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>credential</i> The credential from which to retrieve the certificate.<br />
 <i>how</i> Recursion type</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>bool vomsdata::RetrieveFromCtx (<code>gss_ctx_id_t</code>context, <code>recurse_type</code>how)</h3>
<pre> Gets VOMS information from the given globus context</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The context from which to retrieve the certificate.<br />
 <i>how</i> Recursion type</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>bool vomsdata::RetrieveFromProxy (<code>recurse_type</code>how)</h3>
<pre> Gets VOMS information from an existing globus proxy</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>how</i> Recursion type</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (F) or success (T)</dl>
<h3>std::string vomsdata::ServerErrors (void)</h3>
<p>Gets the error message returned by the server</p>
<h3>void vomsdata::SetLifetime (intlifetime)</h3>
<p>Set requested lifetime for the <code>Contact()</code> call. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>lifetime</i> Requested lifetime, in seconds</dl>
<h3>void vomsdata::SetRetryCount (intretryCount)</h3>
<h3>void vomsdata::SetVerificationTime (time_t)</h3>
<h3>void vomsdata::SetVerificationType (<code>verify_type</code>how)</h3>
<p>Sets the type of verification done on the data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>how</i> The type of verification.</dl>
<h2>Field Documentation</h2>
<h3>std::vector&lt;<code>voms</code>&gt; vomsdata::data</h3>
<p>User&#8217;s info, as in the certificate extension. It may contain data gathered from more than one VOMS server, </p>
<p> Definition at line 370 of file voms_api.h.</p>
<h3><code>verror_type</code> vomsdata::error</h3>
<p>Error code </p>
<p> Definition at line 213 of file voms_api.h.</p>
<h3>std::string vomsdata::extra_data</h3>
<pre> The data specified by the user with the --include switch.</pre>
<p>Note that this field doesn&#8217;t contain the result of a request to the VOMS server, but instead data specified by the user. </p>
<p> The reason for the introduction of this extension is to let a user include important data into his proxy certificate, like, for example, a kerberos ticket </p>
<p> Definition at line 374 of file voms_api.h.</p>
<h3>std::string vomsdata::workvo</h3>
<p>The value of the -vo option of the voms-proxy-init command </p>
<p> Definition at line 373 of file voms_api.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for VOMS CC API from the source code.</p>
