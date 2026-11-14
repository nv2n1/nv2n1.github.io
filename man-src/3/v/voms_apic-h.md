---
title: "voms_apic-h(3)"
name: "voms_apic-h"
section: "3"
letter: "v"
url: "/docs/linux/man/3-voms_apic-h/"
description: "voms_apic.h –"
---

<p>voms_apic.h &#8211;</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;openssl/x509.h&gt;

#include &lt;time.h&gt;

#include 'newformat.h'</code></pre>
<h3>Data Structures</h3>
<p>struct data</p>
<p>User&#8217;s characteristics: can be repeated.</p>
<p>struct attribute</p>
<p>struct contactdata</p>
<p>The type of data returned.</p>
<p>struct voms</p>
<p>struct vomsdata</p>
<p>Macros<br />
#define NOGLOBUS</p>
<p>#define TYPE_NODATA   0</p>
<p>#define TYPE_STD   1</p>
<p>#define TYPE_CUSTOM   2</p>
<p>#define RECURSE_CHAIN   0</p>
<p>#define RECURSE_NONE   1</p>
<p>#define VERIFY_FULL   0xffffffff</p>
<p>#define VERIFY_NONE   0x00000000</p>
<p>#define VERIFY_DATE   0x00000001</p>
<p>#define VERIFY_NOTARGET   0x00000002</p>
<p>#define VERIFY_KEY   0x00000004</p>
<p>#define VERIFY_SIGN   0x00000008</p>
<p>#define VERIFY_ORDER   0x00000010</p>
<p>#define VERIFY_ID   0x00000020</p>
<p>#define VERIFY_CERTLIST   0x00000040</p>
<p>#define VERR_NONE   0</p>
<p>Error codes.</p>
<p>#define VERR_NOSOCKET   1</p>
<p>#define VERR_NOIDENT   2</p>
<p>#define VERR_COMM   3</p>
<p>#define VERR_PARAM   4</p>
<p>#define VERR_NOEXT   5</p>
<p>#define VERR_NOINIT   6</p>
<p>#define VERR_TIME   7</p>
<p>#define VERR_IDCHECK   8</p>
<p>#define VERR_EXTRAINFO   9</p>
<p>#define VERR_FORMAT   10</p>
<p>#define VERR_NODATA   11</p>
<p>#define VERR_PARSE   12</p>
<p>#define VERR_DIR   13</p>
<p>#define VERR_SIGN   14</p>
<p>#define VERR_SERVER   15</p>
<p>#define VERR_MEM   16</p>
<p>#define VERR_VERIFY   17</p>
<p>#define VERR_TYPE   18</p>
<p>#define VERR_ORDER   19</p>
<p>#define VERR_SERVERCODE   20</p>
<p>#define VERR_NOTAVAIL   21</p>
<p>Typedefs<br />
 typedef void * <code>gss_cred_id_t</code> </p>
<p> typedef void * <code>gss_ctx_id_t</code></p>
<h3>Functions</h3>
<pre><code>struct contactdata ** VOMS_FindByAlias (struct vomsdata *vd, char *alias, char *system, char *user, int *error)



struct contactdata ** VOMS_FindByVO (struct vomsdata *vd, char *vo, char *system, char *user, int *error)



void VOMS_DeleteContacts (struct contactdata **list)



struct vomsdata * VOMS_Init (char *voms, char *cert)



struct voms * VOMS_Copy (struct voms *v, int *error)



struct vomsdata * VOMS_CopyAll (struct vomsdata *vd, int *error)



void VOMS_Delete (struct voms *v)



int VOMS_AddTarget (struct vomsdata *vd, char *target, int *error)



void VOMS_FreeTargets (struct vomsdata *vd, int *error)



char * VOMS_ListTargets (struct vomsdata *vd, int *error)



int VOMS_SetVerificationType (int type, struct vomsdata *vd, int *error)



int VOMS_SetLifetime (int length, struct vomsdata *vd, int *error)



void VOMS_Destroy (struct vomsdata *vd)



int VOMS_ResetOrder (struct vomsdata *vd, int *error)



int VOMS_Ordering (char *order, struct vomsdata *vd, int *error)



int VOMS_Contact (char *hostname, int port, char *servsubject, char *command, struct vomsdata *vd, int *error)



int VOMS_ContactRaw (char *hostname, int port, char *servsubject, char *command, void **data, int *datalen, int *version, struct vomsdata *vd, int *error)



int VOMS_Retrieve (X509 *cert, STACK_OF(X509)*chain, int how, struct vomsdata *vd, int *error)



int VOMS_Import (char *buffer, int buflen, struct vomsdata *vd, int *error)



int VOMS_Export (char **buffer, int *buflen, struct vomsdata *vd, int *error)



struct voms * VOMS_DefaultData (struct vomsdata *vd, int *error)



char * VOMS_ErrorMessage (struct vomsdata *vd, int error, char *buffer, int len)



int VOMS_RetrieveEXT (X509_EXTENSION *ext, struct vomsdata *vd, int *error)



int VOMS_RetrieveFromCred (gss_cred_id_t cred, int how, struct vomsdata *vd, int *error)



int VOMS_RetrieveFromFile (FILE *file, int how, struct vomsdata *vd, int *error)



int VOMS_RetrieveFromCtx (gss_ctx_id_t ctx, int how, struct vomsdata *vd, int *error)



int VOMS_RetrieveFromProxy (int how, struct vomsdata *vd, int *error)



int VOMS_RetrieveFromAC (AC *ac, struct vomsdata *vd, int *error)



int VOMS_GetAttributeSourcesNumber (struct voms *v, struct vomsdata *vd, int *error)



int VOMS_GetAttributeSourceHandle (struct voms *v, int num, struct vomsdata *vd, int *error)



const char * VOMS_GetAttributeGrantor (struct voms *v, int handle, struct vomsdata *vd, int *error)



int VOMS_GetAttributesNumber (struct voms *v, int handle, struct vomsdata *vd, int *error)



int VOMS_GetAttribute (struct voms *v, int handle, int num, struct attribute *at, struct vomsdata *vd, int *error)



struct vomsdata * VOMS_Duplicate (struct vomsdata *vd)



AC * VOMS_GetAC (struct voms *v)



int getMajorVersionNumber (void)



int getMinorVersionNumber (void)



int getPatchVersionNumber (void)



int VOMS_SetVerificationTime (time_t verificationtime, struct vomsdata *vd, int *error)



char ** VOMS_GetTargetsList (struct voms *v, struct vomsdata *vd, int *error)



void VOMS_FreeTargetsList (char **)



int VOMS_SetTimeout (int t, struct vomsdata *vd, int *error)



int VOMS_LoadCredentials (X509 *cert, EVP_PKEY *pkey, STACK_OF(X509)*chain, struct vomsdata *vd, int *error)</code></pre>
<h2>Macro Definition Documentation</h2>
<h3>#define NOGLOBUS</h3>
<p>Definition at line 33 of file voms_apic.h.</p>
<h3>#define RECURSE_CHAIN 0</h3>
<p>Definition at line 113 of file voms_apic.h.</p>
<h3>#define RECURSE_NONE 1</h3>
<p>Definition at line 114 of file voms_apic.h.</p>
<h3>#define TYPE_CUSTOM 2</h3>
<p>result of an S command </p>
<p> Definition at line 85 of file voms_apic.h.</p>
<h3>#define TYPE_NODATA 0</h3>
<p>no data </p>
<p> Definition at line 83 of file voms_apic.h.</p>
<h3>#define TYPE_STD 1</h3>
<p>group, role, capability triplet </p>
<p> Definition at line 84 of file voms_apic.h.</p>
<h3>#define VERIFY_CERTLIST 0x00000040</h3>
<p>Definition at line 124 of file voms_apic.h.</p>
<h3>#define VERIFY_DATE 0x00000001</h3>
<p>Definition at line 118 of file voms_apic.h.</p>
<h3>#define VERIFY_FULL 0xffffffff</h3>
<p>Definition at line 116 of file voms_apic.h.</p>
<h3>#define VERIFY_ID 0x00000020</h3>
<p>Definition at line 123 of file voms_apic.h.</p>
<h3>#define VERIFY_KEY 0x00000004</h3>
<p>Definition at line 120 of file voms_apic.h.</p>
<h3>#define VERIFY_NONE 0x00000000</h3>
<p>Definition at line 117 of file voms_apic.h.</p>
<h3>#define VERIFY_NOTARGET 0x00000002</h3>
<p>Definition at line 119 of file voms_apic.h.</p>
<h3>#define VERIFY_ORDER 0x00000010</h3>
<p>Definition at line 122 of file voms_apic.h.</p>
<h3>#define VERIFY_SIGN 0x00000008</h3>
<p>Definition at line 121 of file voms_apic.h.</p>
<h3>#define VERR_COMM 3</h3>
<p>Server problem </p>
<p> Definition at line 131 of file voms_apic.h.</p>
<h3>#define VERR_DIR 13</h3>
<p>Directory error </p>
<p> Definition at line 143 of file voms_apic.h.</p>
<h3>#define VERR_EXTRAINFO 9</h3>
<p>VO name and URI missing </p>
<p> Definition at line 139 of file voms_apic.h.</p>
<h3>#define VERR_FORMAT 10</h3>
<p>Wrong data format </p>
<p> Definition at line 140 of file voms_apic.h.</p>
<h3>#define VERR_IDCHECK 8</h3>
<p>User data in extension different from the real ones </p>
<p> Definition at line 136 of file voms_apic.h.</p>
<h3>#define VERR_MEM 16</h3>
<p>Memory problems </p>
<p> Definition at line 146 of file voms_apic.h.</p>
<h3>#define VERR_NODATA 11</h3>
<p>Empty extension </p>
<p> Definition at line 141 of file voms_apic.h.</p>
<h3>#define VERR_NOEXT 5</h3>
<p>VOMS extension missing </p>
<p> Definition at line 133 of file voms_apic.h.</p>
<h3>#define VERR_NOIDENT 2</h3>
<p>Cannot identify itself (certificate problem) </p>
<p> Definition at line 130 of file voms_apic.h.</p>
<h3>#define VERR_NOINIT 6</h3>
<p>Initialization error </p>
<p> Definition at line 134 of file voms_apic.h.</p>
<h3>#define VERR_NONE 0</h3>
<p>Error codes. </p>
<p> Definition at line 128 of file voms_apic.h.</p>
<h3>#define VERR_NOSOCKET 1</h3>
<p>Socket problem </p>
<p> Definition at line 129 of file voms_apic.h.</p>
<h3>#define VERR_NOTAVAIL 21</h3>
<p>Method not available </p>
<p> Definition at line 151 of file voms_apic.h.</p>
<h3>#define VERR_ORDER 19</h3>
<p>Ordering different than required </p>
<p> Definition at line 149 of file voms_apic.h.</p>
<h3>#define VERR_PARAM 4</h3>
<p>Wrong parameters </p>
<p> Definition at line 132 of file voms_apic.h.</p>
<h3>#define VERR_PARSE 12</h3>
<p>Parse error </p>
<p> Definition at line 142 of file voms_apic.h.</p>
<h3>#define VERR_SERVER 15</h3>
<p>Unidentifiable VOMS server </p>
<p> Definition at line 145 of file voms_apic.h.</p>
<h3>#define VERR_SERVERCODE 20</h3>
<p>Error from the server </p>
<p> Definition at line 150 of file voms_apic.h.</p>
<h3>#define VERR_SIGN 14</h3>
<p>Signature error </p>
<p> Definition at line 144 of file voms_apic.h.</p>
<h3>#define VERR_TIME 7</h3>
<p>Error in time checking </p>
<p> Definition at line 135 of file voms_apic.h.</p>
<h3>#define VERR_TYPE 18</h3>
<p>Returned data of unknown type </p>
<p> Definition at line 148 of file voms_apic.h.</p>
<h3>#define VERR_VERIFY 17</h3>
<p>Generic verification error </p>
<p> Definition at line 147 of file voms_apic.h.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void* <code>gss_cred_id_t</code></h3>
<p>Definition at line 42 of file voms_apic.h.</p>
<h3>typedef void* <code>gss_ctx_id_t</code></h3>
<p>Definition at line 43 of file voms_apic.h.</p>
<h2>Function Documentation</h2>
<h3>int getMajorVersionNumber (void)</h3>
<h3>int getMinorVersionNumber (void)</h3>
<h3>int getPatchVersionNumber (void)</h3>
<h3>int VOMS_AddTarget (struct <code>vomsdata</code> *vd, char *target, int *error)</h3>
<p>Adds a target to the AC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> The vomsdata structure.<br />
 <i>target</i> The target to add. It should be a FQDN.<br />
 <i>error</i> RETURN PARAMETER: qualifies the error message.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_Contact (char *hostname, intport, char *servsubject, char *command, struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Contacts a VOMS server to get a certificate </p>
<p> It is the equivalent of the voms_proxy_init command, but without the &#8211;include functionality. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hostname</i> FQDN of the VOMS server<br />
 <i>port</i> the port on which the VOMS server is listening<br />
 <i>servsubject</i> the subject of the server&#8217;s certificate<br />
 <i>command</i> Command<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_ContactRaw (char *hostname, intport, char *servsubject, char *command, void **data, int *datalen, int *version, struct <code>vomsdata</code> *vd, int *error)</h3>
<p>The same as VOMS_Contact, except that instead of starting the verification process, the data is returned as is in the </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>data</i> and<br />
 <i>datalen</i> fields.<br />
 <i>hostname</i> FQDN of the VOMS server<br />
 <i>port</i> the port on which the VOMS server is listening<br />
 <i>servsubject</i> the subject of the server&#8217;s certificate<br />
 <i>command</i> the command sent to the server<br />
 <i>version</i> is the version number of the data.<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>struct <code>voms</code>* VOMS_Copy (struct <code>voms</code> *v, int *error)</h3>
<pre> Copies a voms structure.
 N.B: This is the ONLY way to correctly initialize a voms structure as a</pre>
<p>&nbsp;<wbr>copy of another voms structure.&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>v</i> The structure to copy.<br />
 <i>error</i> RETURN PARAMETER: qualifies the error message.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL (error) or the new voms structure.</dl>
<h3>struct <code>vomsdata</code>* VOMS_CopyAll (struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Copies a vomsdata structure.
 N.B: This is the ONLY way to correctly initialize a vomsdata structure as a</pre>
<p>&nbsp;<wbr>copy of another vomsdata structure.&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> The structure to copy.<br />
 <i>error</i> RETURN PARAMETER: qualifies the error message.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL (error) or the new vomsdata structure.</dl>
<h3>struct <code>voms</code>* VOMS_DefaultData (struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Gets the default attributes from a vomsdata structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> the vomsdata structure to analyze<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a pointer to the relevant voms structure. DO NOT modify the fields.</dl>
<h3>void VOMS_Delete (struct <code>voms</code> *v)</h3>
<p>Deletes a voms structure </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>v</i> Pointer to the structure to delete.</dl>
<h3>void VOMS_DeleteContacts (struct <code>contactdata</code> **list)</h3>
<p>Frees a contactdata vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>list</i> The vector to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>NONE</dl>
<h3>void VOMS_Destroy (struct <code>vomsdata</code> *vd)</h3>
<p>Destroys a proper vomsdata structure /param vd The structure to deallocate.</p>
<h3>struct <code>vomsdata</code>* VOMS_Duplicate (struct <code>vomsdata</code> *vd)</h3>
<h3>char* VOMS_ErrorMessage (struct <code>vomsdata</code> *vd, interror, char *buffer, intlen)</h3>
<pre> Gets a textual description of the error.</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> The vomsdata structure to analyze<br />
 <i>error</i> The error returned by the last function<br />
 <i>buffer</i> A pointer to a buffer where the error message will be written. If NULL, then memory is allocated by the function, and will have to be free()ed by the caller.<br />
 <i>len</i> The length of the memory pointed to by the buffer parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A pointer to the error message.</dl>
<h3>int VOMS_Export (char **buffer, int *buflen, struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Converts data into a test format</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buffer</i> OUTPUT PARAMETER contains the converted data<br />
 <i>buflen</i> OUTPUT PARAMETER contains the length of buffer<br />
 <i>vd</i> contains the data to convert<br />
 <i>error</i> RETURN PARAMETER Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>struct <code>contactdata</code>** VOMS_FindByAlias (struct <code>vomsdata</code> *vd, char *alias, char *system, char *user, int *error)</h3>
<p>Gets a list of VOMS servers which share an alias. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> The correctly initialized vomsdata structured.<br />
 <i>alias</i> The alias to look for.<br />
 <i>system</i> The directory in which to look for the system configuration files. If NULL, defaults to /opt/edc/etc/vomses<br />
 <i>user</i> The directory in which to look for the user configuration files. Defaults to $VOMS_USERCONF if NULL. Again defaults to $HOME/.edg/vomses if the latter is NULL, or to ~/.edg/vomses as a last resort.<br />
 <i>error</i> RETURN PARAMETER: qualifies the error message.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL, or a NULL-terminated vector of contactdata structures. The only supported way to free this array is via the VOMS_DeleteContacts function. Note also that the order in which the servers are returned is unspecified.</dl>
<h3>struct <code>contactdata</code>** VOMS_FindByVO (struct <code>vomsdata</code> *vd, char *vo, char *system, char *user, int *error)</h3>
<p>Gets a list of VOMS servers which serve the same VO. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> The correctly initialized vomsdata structured.<br />
 <i>vo</i> The VO to look for.<br />
 <i>system</i> The directory in which to look for the system configuration files. If NULL, defaults to /opt/edc/etc/vomses<br />
 <i>user</i> The directory in which to look for the user configuration files. Defaults to $VOMS_USERCONF if NULL. Again defaults to $HOME/.edg/vomses if the latter is NULL, or to ~/.edg/vomses as a last resort.<br />
 <i>error</i> RETURN PARAMETER: qualifies the error message.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL, or a NULL-terminated vector of contactdata structures. The only supported way to free this array is via the VOMS_DeleteContacts function. Note also that the order in which the servers are returned is unspecified.</dl>
<h3>void VOMS_FreeTargets (struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Delete the targets from the AC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> The vomsdata structure.<br />
 <i>error</i> RETURN PARAMETER: qualifies the error message.</dl>
<h3>void VOMS_FreeTargetsList (char **)</h3>
<h3>AC* VOMS_GetAC (struct <code>voms</code> *v)</h3>
<h3>int VOMS_GetAttribute (struct <code>voms</code> *v, inthandle, intnum, struct <code>attribute</code> *at, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>const char* VOMS_GetAttributeGrantor (struct <code>voms</code> *v, inthandle, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_GetAttributesNumber (struct <code>voms</code> *v, inthandle, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_GetAttributeSourceHandle (struct <code>voms</code> *v, intnum, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_GetAttributeSourcesNumber (struct <code>voms</code> *v, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>char** VOMS_GetTargetsList (struct <code>voms</code> *v, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_Import (char *buffer, intbuflen, struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Converts data from the format used for inclusion into a certificate to the internal format </p>
<p> The function does verify the data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buffer</i> contains the data to be converted<br />
 <i>buflen</i> contains the length of buffer<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>struct <code>vomsdata</code>* VOMS_Init (char *voms, char *cert)</h3>
<p>Initializes a vomsdata structure for use by the other functions. N.B: This is the ONLY way to correctly initialize a vomsdata structure. It is also forbidden to directly take the sizeof() of this structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>voms</i> The directory which contains the certificates of the VOMS servers<br />
 <i>cert</i> The directory which contains the CA certificates</dl>
<p> If voms_dir is empty, the value of the environment variable X509_VOMS_DIR is taken </p>
<p> If cert_dir is empty, the value of the environment variable X509_CERT_DIR is taken </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL for failure, or a pointer to a properly initialized structure.</dl>
<h3>char* VOMS_ListTargets (struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_LoadCredentials (X509 *cert, EVP_PKEY *pkey, STACK_OF(X509)*chain, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_Ordering (char *order, struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Further specified the order of the returned attributes. Please do note that calls are cumulative unless <code>VOMS_ResetOrder()</code> is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>order</i> the group:role attribute.<br />
 <i>vd</i> RETURN PARAMETER: contains the modified data.<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_ResetOrder (struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Unsets the return order of the attributes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>vd</i> RETURN PARAMETER: contains the modified data.<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_Retrieve (X509 *cert, STACK_OF(X509)*chain, inthow, struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Extracts the VOMS extension from an X.509 certificate. </p>
<pre> The function doesn't check the validity of the certificates, 
 but it does check the content of the user data.
 <br>
aram cert The certificate with the VOMS extensions
 <br>
aram chain The chain of the validation certificates 
 (only the intermediate ones)
 <br>
aram how Recursion type
 <br>
aram vd RETURN PARAMETER: contains the data returned by the connection
 <br>
aram error RETURN PARAMETER: Qualifies the error message
 eturn failure (0) or success (&lt;&gt;0)</pre>
<p>&nbsp;<wbr></p>
<h3>int VOMS_RetrieveEXT (X509_EXTENSION *ext, struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Gets VOMS information from the given extension</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ext</i> The extension to parse.<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_RetrieveFromAC (AC *ac, struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Gets VOMS information from an existing globus proxy</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ac</i> AC from which to get the credentials<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_RetrieveFromCred (<code>gss_cred_id_t</code>cred, inthow, struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Gets VOMS information from the given globus credential</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>cred</i> The credential from which to retrieve the certificate.<br />
 <i>how</i> Recursion type<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_RetrieveFromCtx (<code>gss_ctx_id_t</code>ctx, inthow, struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Gets VOMS information from the given globus context</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ctx</i> The context from which to retrieve the certificate.<br />
 <i>how</i> Recursion type<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_RetrieveFromFile (FILE *file, inthow, struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Gets VOMS information from the given globus credential</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>file</i> The file from which to retrieve the certificate.<br />
 <i>how</i> Recursion type<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_RetrieveFromProxy (inthow, struct <code>vomsdata</code> *vd, int *error)</h3>
<pre> Gets VOMS information from an existing globus proxy</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>how</i> Recursion type<br />
 <i>vd</i> RETURN PARAMETER: contains the data returned by the connection<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_SetLifetime (intlength, struct <code>vomsdata</code> *vd, int *error)</h3>
<p>Set requested lifetime for <code>VOMS_Contact()</code> calls. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>length</i> Lifetime requested.<br />
 <i>vd</i> RETURN PARAMETER: contains the modified data.<br />
 <i>error</i> RETURN PARAMETER: Qualifies the error message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>failure (0) or success (&lt;&gt;0)</dl>
<h3>int VOMS_SetTimeout (intt, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_SetVerificationTime (time_tverificationtime, struct <code>vomsdata</code> *vd, int *error)</h3>
<h3>int VOMS_SetVerificationType (inttype, struct <code>vomsdata</code> *vd, int *error)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for VOMS C API from the source code.</p>
