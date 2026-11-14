---
title: "globus_gsi_system_config-h(3)"
name: "globus_gsi_system_config-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_system_config-h/"
description: "globus_gsi_system_config.h – Globus GSI System Config Library."
---

<p>globus_gsi_system_config.h &#8211; Globus GSI System Config Library.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_gsi_system_config_constants.h&#8217;<br />
 #include &#8216;openssl/x509.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_SYSCONFIG_MODULE</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_SET_KEY_PERMISSIONS</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_HOME_DIR</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_CHECK_KEYFILE</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_CHECK_CERTFILE</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_FILE_EXISTS</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_DIR_EXISTS</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_CERT_DIR</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_USER_CERT_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_HOST_CERT_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_SERVICE_CERT_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_PROXY_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_SIGNING_POLICY_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_CA_CERT_FILES</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_CURRENT_WORKING_DIR</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_MAKE_ABSOLUTE_PATH_FOR_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_SPLIT_DIR_AND_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_REMOVE_ALL_OWNED_FILES</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_GRIDMAP_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_AUTHZ_CONF_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_GAA_CONF_FILENAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_IS_SUPERUSER</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_USER_ID_STRING</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_PROC_ID_STRING</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_USERNAME</code> </p>
<p> #define <code>GLOBUS_GSI_SYSCONFIG_GET_UNIQUE_PROXY_FILENAME</code> </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_gsi_sysconfig_set_key_permissions_unix</code> (char *filename)<br />
 <i>UNIX &#8211; Set Key Permissions. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_home_dir_unix</code> (char **home_dir)<br />
 <i>UNIX &#8211; Get HOME Directory</i> </p>
<p> Get the HOME Directory of the current user. Should be the $HOME environment variable. &quot;<br />
 globus_result_t <code>globus_gsi_sysconfig_file_exists_unix</code> (const char *filename)<br />
 <i>UNIX &#8211; File Exists. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_dir_exists_unix</code> (const char *filename)<br />
 <i>UNIX &#8211; Directory Exists. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_check_keyfile_unix</code> (const char *filename)<br />
 <i>UNIX &#8211; Check File Status for Key. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_check_certfile_unix</code> (const char *filename)<br />
 <i>UNIX &#8211; Check File Status for Cert. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_cert_dir_unix</code> (char **cert_dir)<br />
 <i>UNIX &#8211; Get Trusted CA Cert Dir. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_user_cert_filename_unix</code> (char **user_cert_filename, char **user_key_filename)<br />
 <i>UNIX &#8211; Get User Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_host_cert_filename_unix</code> (char **host_cert_filename, char **host_key_filename)<br />
 <i>UNIX &#8211; Get Host Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_service_cert_filename_unix</code> (char *service_name, char **service_cert_filename, char **service_key_filename)<br />
 <i>UNIX &#8211; Get Service Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_proxy_filename_unix</code> (char **user_proxy, <code>globus_gsi_proxy_file_type_t</code> proxy_file_type)<br />
 <i>UNIX &#8211; Get Proxy Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_signing_policy_filename_unix</code> (X509_NAME *ca_name, char *cert_dir, char **signing_policy_filename)<br />
 <i>UNIX &#8211; Get Signing Policy Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_ca_cert_files_unix</code> (char *ca_cert_dir, globus_fifo_t *ca_cert_list)<br />
 <i>UNIX &#8211; Get CA Cert Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_current_working_dir_unix</code> (char **working_dir)<br />
 <i>UNIX &#8211; Get Current Working Directory. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_make_absolute_path_for_filename_unix</code> (char *filename, char **absolute_path)<br />
 <i>UNIX &#8211; Make Absolute Path. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_split_dir_and_filename_unix</code> (char *full_filename, char **dir_string, char **filename_string)<br />
 <i>UNIX &#8211; Split Directory and Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_remove_all_owned_files_unix</code> (char *default_filename)<br />
 <i>UNIX &#8211; Remove all proxies owned by current uid. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_is_superuser_unix</code> (int *is_superuser)<br />
 <i>UNIX &#8211; Check if the current user is root. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_user_id_string_unix</code> (char **user_id_string)<br />
 <i>UNIX &#8211; Get User ID. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_username_unix</code> (char **username)<br />
 <i>UNIX &#8211; Get Username. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_proc_id_string_unix</code> (char **proc_id_string)<br />
 <i>UNIX &#8211; Get Process ID. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_gridmap_filename_unix</code> (char **filename)<br />
 <i>UNIX &#8211; Get the path and file name of the grid map file. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_authz_conf_filename_unix</code> (char **filename)<br />
 <i>UNIX &#8211; Get the path of authorization callback configuration. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_gaa_conf_filename_unix</code> (char **filename)<br />
 <i>UNIX &#8211; Get the path and file name of the gaa configuration file. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_unique_proxy_filename</code> (char **unique_filename)<br />
 <i>Get Unique Proxy Filename. </i></p>
<h2>Detailed Description</h2>
<p>Globus GSI System Config Library. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Sam Lang, Sam Meder</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_sysconfig from the source code.</p>
