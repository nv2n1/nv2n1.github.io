---
title: "globus_gss_assist_map_local_user(3)"
name: "globus_gss_assist_map_local_user"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_map_local_user/"
description: "Gridmap Authorization –"
---

<h2 class="name">NAME</h2>
<p> Gridmap Authorization &#8211; </p>
<p> Gridmap Authorization and Local User Mapping.</p>
<h3>Macros</h3>
<p> #define <code>GlobusGssAssistFreeDNArray</code>(dn_a)<br />
 <i>Free array of distinguished names. </i></p>
<h3>Functions</h3>
<p> int <code>globus_gss_assist_gridmap</code> (char *globusidp, char **useridp)<br />
 <i>Look up the default mapping for a Grid identity in a gridmap file. </i><br />
 int <code>globus_gss_assist_userok</code> (char *globusid, char *userid)<br />
 <i>Gridmap entry existence check. </i><br />
 int <code>globus_gss_assist_map_local_user</code> (char *local_user, char **globusidp)<br />
 <i>Look up the default Grid identity associated with a local user name. </i><br />
 globus_result_t <code>globus_gss_assist_lookup_all_globusid</code> (char *username, char **dns[], int *dn_count)<br />
 <i>Look up all Grid IDs associated with a local user ID. </i><br />
 globus_result_t <code>globus_gss_assist_map_and_authorize</code> (gss_ctx_id_t context, char *service, char *desired_identity, char *identity_buffer, unsigned int identity_buffer_length)<br />
 <i>Authorize the peer of a security context to use a service. </i><br />
 globus_result_t <code>globus_gss_assist_map_and_authorize_sharing</code> (char *shared_user_certificate, gss_ctx_id_t context, char *desired_identity, char *identity_buffer, unsigned int identity_buffer_length)<br />
 <i>Authorize a particular credential for shared access. </i></p>
<h2>Detailed Description</h2>
<p> Gridmap Authorization and Local User Mapping. </p>
<p> Functions in this group are used to authorize a GSSAPI credential to perform some action on the local machine. In addition to checking whether a credential is authorized, it can also be mapped to a local user name.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GlobusGssAssistFreeDNArray(dn_a)</h3>
<p> Free array of distinguished names. Free the contents of a name array created during a successful call to <code>globus_gss_assist_lookup_all_globusid()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dn_a</i> Array of names to free.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>void</i></dl>
<h2>Function Documentation</h2>
<h3>int globus_gss_assist_gridmap (char *globusidp, char **useridp)</h3>
<p> Look up the default mapping for a Grid identity in a gridmap file. The <code>globus_gss_assist_gridmap()</code> function parses the default gridmap file and modifies its <i>useridp</i> parameter to point to a copy of the string containing the default local identity that the grid identity is mapped to. If successful, the caller is responsible for freeing the string pointed to by <i>useridp</i>. </p>
<p> By default, <code>globus_gss_assist_gridmap()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>globusidp</i> The GSSAPI name string of the identity who requested authorization<br />
 <i>useridp</i> A pointer to a string to be set to the default user ID for the local system. No validation is done to check that such a user exists.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_gss_assist_gridmap()</code> returns 0 and modifies the the string pointed to by the <i>useridp</i> parameter. If an error occurs, a non-zero value is returned and the value pointed to by <i>useridp</i> is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>1</i> Error</dl>
<h3>globus_result_t globus_gss_assist_lookup_all_globusid (char *username, char **dns[], int *dn_count)</h3>
<p> Look up all Grid IDs associated with a local user ID. The <code>globus_gss_assist_lookup_all_globusid()</code> function parses a gridmap file and finds all Grid IDs that map to a local user ID. The <i>dns</i> parameter is modified to point to an array of Grid ID strings from the gridmap file, and the <i>dn_count</i> parameter is modified to point to the number of Grid ID strings in the array. The caller is responsible for freeing the array using the macro <i></i><code>GlobusGssAssistFreeDNArray()</code>. </p>
<p> By default, <code>globus_gss_assist_lookup_all_globusid()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>username</i> The local username to look up in the gridmap file.<br />
 <i>dns</i> A pointer to an array of strings. This function modifies this to point to a newly allocated array of strings. The caller must use the macro <i></i><code>GlobusGssAssistFreeDNArray()</code> to free this memory.<br />
 <i>dn_count</i> A pointer to an integer that is modified to contain the number of entries in the array returned via the <i>dns</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_gss_assist_lookup_all_globusid()</code> returns GLOBUS_SUCCESS and modifies its <i>dns</i> and <i>dn_count</i> parameters as described above. If an error occurs, <code>globus_gss_assist_lookup_all_globusid()</code> returns a globus_result_t that can be resolved to an error object and the values pointed to by <i>dns</i> and <i>dn_count</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_ARGUMENTS</i> Error with arguments<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_GRIDMAP</i> Invalid path to gridmap<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_ERRNO</i> System error</dl>
<h3>globus_result_t globus_gss_assist_map_and_authorize (gss_ctx_id_tcontext, char *service, char *desired_identity, char *identity_buffer, unsigned intidentity_buffer_length)</h3>
<p> Authorize the peer of a security context to use a service. The <code>globus_gss_assist_map_and_authorize()</code> function attempts to authorize the peer of a security context to use a particular service. If the <i>desired_identity</i> parameter is non-NULL, the authorization will succeed only if the peer is authorized for that identity. Otherwise, any valid authorized local user name will be used. If authorized, the local user name will be copied to the string pointed to by the <i>identity_buffer</i> parameter, which must be at least as long as the value passed as the <i>identity_buffer_length</i> parameter. </p>
<p> If authorization callouts are defined in the callout configuration file, <code>globus_gss_assist_map_and_authorize()</code> will invoke both the GLOBUS_GENERIC_MAPPING_TYPE callout and the GLOBUS_GENERIC_AUTHZ_TYPE callout; otherwise the default gridmap file will be used for mapping and no service-specific authorization will be done. </p>
<p> If <code>globus_gss_assist_map_and_authorize()</code> uses a gridmap file, it first looks for a file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Security context to inspect for peer identity information.<br />
 <i>service</i> A NULL-terminated string containing the name of the service that an authorization decision is being made for.<br />
 <i>desired_identity</i> Optional. If non-NULL, perform an authorization to act as the local user named by this NULL-terminated string.<br />
 <i>identity_buffer</i> A pointer to a string buffer into which will be copied the local user name that the peer of the context is authorized to act as.<br />
 <i>identity_buffer_length</i> Length of the <i>identity_buffer</i> array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_gss_assist_map_and_authorize()</code> returns GLOBUS_SUCCESS and copies the authorized local identity to the <i>identity_buffer</i> parameter. If an error occurs, <code>globus_gss_assist_map_and_authorize()</code> returns a globus_result_t that can be resolved to an error object.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_CALLOUT_CONFIG</i> Invalid authorization configuration file<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_HASHTABLE</i> Hash table operation failed.<br />
 <i>GLOBUS_CALLOUT_ERROR_CALLOUT_ERROR</i> The callout itself returned a error.<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_DL</i> Dynamic library operation failed.<br />
 <i>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY</i> Out of memory<br />
 <i>GLOBUS_GSI_GSS_ASSIST_GSSAPI_ERROR</i> A GSSAPI function returned an error<br />
 <i>GLOBUS_GSI_GSS_ASSIST_GRIDMAP_LOOKUP_FAILED</i> Gridmap lookup failure<br />
 <i>GLOBUS_GSI_GSS_ASSIST_BUFFER_TOO_SMALL</i> Caller provided insufficient buffer space for local identity</dl>
<h3>globus_result_t globus_gss_assist_map_and_authorize_sharing (char *shared_user_certificate, gss_ctx_id_tcontext, char *desired_identity, char *identity_buffer, unsigned intidentity_buffer_length)</h3>
<p> Authorize a particular credential for shared access. The <code>globus_gss_assist_map_and_authorize_sharing()</code> function attempts to authorize a particular credential for shared access. the <i>desired_identity</i> parameter is non-NULL, the authorization will succeed only if the credential is authorized for that identity. Otherwise, any valid authorized local user name will be used. If authorized, the local user name will be copied to the string pointed to by the <i>identity_buffer</i> parameter, which must be at least as long as the value passed as the <i>identity_buffer_length</i> parameter. </p>
<p> If authorization callouts are defined in the callout configuration file, <code>globus_gss_assist_map_and_authorize_sharing()</code> will invoke both the GLOBUS_GENERIC_MAPPING_TYPE callout and the GLOBUS_GENERIC_AUTHZ_TYPE callout; otherwise the default gridmap file will be used for mapping and no service-specific authorization will be done. </p>
<p> If <code>globus_gss_assist_map_and_authorize_sharing()</code> uses a gridmap file, it first looks for a file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>shared_user_certificate</i> cert and cert chain of user that owns the resources to be shared, in PEM format. This will be parsed to find the identity that should be mapped.<br />
 <i>context</i> Security context of the underlying connection. This should generally be ignored.<br />
 <i>desired_identity</i> Optional. If non-NULL, perform an authorization to act as the local user named by this NULL-terminated string.<br />
 <i>identity_buffer</i> A pointer to a string buffer into which will be copied the local user name that the peer of the context is authorized to act as.<br />
 <i>identity_buffer_length</i> Length of the <i>identity_buffer</i> array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_gss_assist_map_and_authorize_sharing()</code> returns GLOBUS_SUCCESS and copies the authorized local identity to the <i>identity_buffer</i> parameter. If an error occurs, <code>globus_gss_assist_map_and_authorize_sharing()</code> returns a globus_result_t that can be resolved to an error object.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_CALLOUT_CONFIG</i> Invalid authorization configuration file<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_HASHTABLE</i> Hash table operation failed.<br />
 <i>GLOBUS_CALLOUT_ERROR_CALLOUT_ERROR</i> The callout itself returned a error.<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_DL</i> Dynamic library operation failed.<br />
 <i>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY</i> Out of memory<br />
 <i>GLOBUS_GSI_GSS_ASSIST_GSSAPI_ERROR</i> A GSSAPI function returned an error<br />
 <i>GLOBUS_GSI_GSS_ASSIST_GRIDMAP_LOOKUP_FAILED</i> Gridmap lookup failure<br />
 <i>GLOBUS_GSI_GSS_ASSIST_BUFFER_TOO_SMALL</i> Caller provided insufficient buffer space for local identity</dl>
<h3>int globus_gss_assist_map_local_user (char *local_user, char **globusidp)</h3>
<p> Look up the default Grid identity associated with a local user name. The <code>globus_gss_assist_map_local_user()</code> function parses the gridmap file to determine a if the user name passed as the <i>local_user</i> parameter is the default local user for a Grid ID in the gridmap file. If so, it modifies <i>globusidp</i> to point to a copy of that ID. Otherwise, it searches the gridmap file for a Grid ID that has a non-default mapping for <i>local_user</i> and modifies <i>globusidp</i> to point to a copy of that ID. If successful, the caller is responsible for freeing the string pointed to by the <i>globusidp</i> pointer. </p>
<p> By default, <code>globus_gss_assist_map_local_user()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>local_user</i> The local username to find a Grid ID for<br />
 <i>globusidp</i> A Grid ID that maps from the local_user.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_gss_assist_map_local_user()</code> returns 0 and modifies <i>globusidp</i> to point to a Grid ID that maps to <i>local_user</i>; otherwise, <code>globus_gss_assist_map_local_user()</code> returns 1 and the value pointed to by <i>globusidp</i> is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>1</i> Error</dl>
<h3>int globus_gss_assist_userok (char *globusid, char *userid)</h3>
<p> Gridmap entry existence check. The <code>globus_gss_assist_userok()</code> function parses the default gridmap file and checks whether any mapping exists for the grid identity passed as the <i>globusid</i> parameter and the local user identity passed as the @ userid parameter. </p>
<p> By default, <code>globus_gss_assist_userok()</code> looks for the default gridmap file defined by the value of the GRIDMAP environment variable. If that is not set, it falls back to $HOME/.gridmap. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>globusid</i> The GSSAPI name string of the identity who requested authorization<br />
 <i>userid</i> The local account name that access is sought for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> If <code>globus_gss_assist_userok()</code> is able to find a mapping between <i>globusid</i> and <i>userid</i>, it returns 0; otherwise it returns 1.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>1</i> Error</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
