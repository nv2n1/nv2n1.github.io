---
title: "globus_gsi_sysconfig_make_absolute_path_for_filename_win32(3)"
name: "globus_gsi_sysconfig_make_absolute_path_for_filename_win32"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig_make_absolute_path_for_filename_win32/"
description: "Functions for Win32 platforms –"
---

<h2 class="name">NAME</h2>
<p> Functions for Win32 platforms &#8211; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_sysconfig_set_key_permissions_win32</code> (char *filename)<br />
 <i>Win32 &#8211; Set Key Permissions. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_file_exists_win32</code> (const char *filename)<br />
 <i>Win32 &#8211; File Exists. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_dir_exists_win32</code> (const char *filename)<br />
 <i>Win32 &#8211; Directory Exists. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_current_working_dir_win32</code> (char **working_dir)<br />
 <i>Win32 &#8211; Get Current Working Directory. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_make_absolute_path_for_filename_win32</code> (char *filename, char **absolute_path)<br />
 <i>Win32 &#8211; Make Absolute Path. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_split_dir_and_filename_win32</code> (char *full_filename, char **dir_string, char **filename_string)<br />
 <i>Win32 &#8211; Split Directory and Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_cert_dir_win32</code> (char **cert_dir)<br />
 <i>Win32 &#8211; Get Trusted CA Cert Dir. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_user_cert_filename_win32</code> (char **user_cert, char **user_key)<br />
 <i>Win32 &#8211; Get User Certificate Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_host_cert_filename_win32</code> (char **host_cert, char **host_key)<br />
 <i>Win32 &#8211; Get Host Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_service_cert_filename_win32</code> (char *service_name, char **service_cert, char **service_key)<br />
 <i>Win32 &#8211; Get Service Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_proxy_filename_win32</code> (char **user_proxy, <code>globus_gsi_proxy_file_type_t</code> proxy_file_type)<br />
 <i>Win32 &#8211; Get Proxy Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_ca_cert_files_win32</code> (char *ca_cert_dir, globus_fifo_t *ca_cert_list)<br />
 <i>Win32 &#8211; Get CA Cert Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_remove_all_owned_files_win32</code> (char *default_filename)<br />
 <i>Win32 &#8211; Remove all proxies owned by current uid. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_gridmap_filename_win32</code> (char **filename)<br />
 <i>Win32 &#8211; Get the path and file name of the grid map file. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_authz_conf_filename_win32</code> (char **filename)<br />
 <i>Win32 &#8211; Get the path and file name of the grid map file. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_authz_lib_conf_filename_win32</code> (char **filename)<br />
 <i>Win32 &#8211; Get authorization configuration filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_gaa_conf_filename_win32</code> (char **filename)<br />
 <i>Win32 &#8211; Get the path and file name of the gaa config file. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_is_superuser_win32</code> (int *is_superuser)<br />
 <i>Win32 &#8211; Check if the current user is root. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_signing_policy_filename_win32</code> (X509_NAME *ca_name, char *cert_dir, char **signing_policy_filename)<br />
 <i>Win32 &#8211; Get Signing Policy Filename. </i></p>
<h2>Detailed Description</h2>
<p> These functions implement the Win32 version of the Globus GSI System Configuration API. <code>They should never be called directly, please use the provided platform independent defines.</code></p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_sysconfig_dir_exists_win32 (const char *filename)</h3>
<p> Win32 &#8211; Directory Exists. Check that the directory exists </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> the file to check</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the directory exists, otherwise an error object identifier.</dl>
<h3>globus_result_t globus_gsi_sysconfig_file_exists_win32 (const char *filename)</h3>
<p> Win32 &#8211; File Exists. Check that the file exists </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> the file to check</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS (even if the file doesn&#8217;t exist) &#8211; in some abortive cases an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_authz_conf_filename_win32 (char **filename)</h3>
<p> Win32 &#8211; Get the path and file name of the grid map file. Get the path and file name of the authorization callback configuration file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> Contains the location of the authorization callback configuration file upon successful return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_authz_lib_conf_filename_win32 (char **filename)</h3>
<p> Win32 &#8211; Get authorization configuration filename. Get the path and file name of the authorization callback library configuration file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> Contains the location of the authorization callback library configuration file upon successful return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_ca_cert_files_win32 (char *ca_cert_dir, globus_fifo_t *ca_cert_list)</h3>
<p> Win32 &#8211; Get CA Cert Filenames. Gets a list of trusted CA certificate filenames in a trusted CA certificate directory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ca_cert_dir</i> The trusted CA certificate directory to get the filenames from<br />
 <i>ca_cert_list</i> The resulting list of CA certificate filenames. This is a globus list structure.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_fifo_t</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_cert_dir_win32 (char **cert_dir)</h3>
<p> Win32 &#8211; Get Trusted CA Cert Dir. Get the Trusted Certificate Directory containing the trusted Certificate Authority certificates. This directory is determined in the order shown below. Failure in one method results in attempting the next. </p>
<dl>
<dt>1.</p>
<dd> <code>X509_CERT_DIR environment variable</code> &#8211; if this is set, the trusted certificates will be searched for in that directory. This variable allows the end user to specify the location of trusted certificates.</p>
<dt>2.</p>
<dd> <code>x509_cert_dir registry key</code> &#8211; If this registry key is set on windows, the directory it points to should contain the trusted certificates. The path to the registry key is software\Globus\GSI</p>
<dt>3.</p>
<dd> <code>\&lt;user home directory&gt;\</code><code>.globus
