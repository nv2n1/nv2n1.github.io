---
title: "globus_gsi_sysconfig_set_key_permissions(3)"
name: "globus_gsi_sysconfig_set_key_permissions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig_set_key_permissions/"
description: "Defines –"
---

<p>Defines &#8211; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_SYSCONFIG_SET_KEY_PERMISSIONS</code> </p>
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
<h2>Detailed Description</h2>
<p>These preprocessor defines allow for a platform (ie Win32 vs UNIX) independent API.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GSI_SYSCONFIG_CHECK_CERTFILE</h3>
<p>Check for the correct file permissions on a certificate. </p>
<p> See <code>globus_gsi_sysconfig_check_certfile_unix()</code> and globus_gsi_sysconfig_check_certfile_win32()</p>
<h3>#define GLOBUS_GSI_SYSCONFIG_CHECK_KEYFILE</h3>
<p>Check for the correct file permissions on a private key. </p>
<p> See <code>globus_gsi_sysconfig_check_keyfile_unix()</code> and globus_gsi_sysconfig_check_keyfile_win32()</p>
<h3>#define GLOBUS_GSI_SYSCONFIG_DIR_EXISTS</h3>
<p>Check whether a given directory exists </p>
<p> See <code>globus_gsi_sysconfig_dir_exists_unix()</code> and <code>globus_gsi_sysconfig_dir_exists_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_FILE_EXISTS</h3>
<p>Check whether a given file exists </p>
<p> See <code>globus_gsi_sysconfig_file_exists_unix()</code> and <code>globus_gsi_sysconfig_file_exists_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_AUTHZ_CONF_FILENAME</h3>
<p>Determine the location of the authorization callout config file. </p>
<p> See <code>globus_gsi_sysconfig_get_authz_conf_filename_unix()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_CA_CERT_FILES</h3>
<p>Get a list of of trusted CA certificate filenames in a trusted CA certificate directory. </p>
<p> See <code>globus_gsi_sysconfig_get_ca_cert_files_unix()</code> and <code>globus_gsi_sysconfig_get_ca_cert_files_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_CERT_DIR</h3>
<p>Determine the location of the trusted certificates directory </p>
<p> See <code>globus_gsi_sysconfig_get_cert_dir_unix()</code> and <code>globus_gsi_sysconfig_get_cert_dir_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_CURRENT_WORKING_DIR</h3>
<p>Get the current working directory </p>
<p> See <code>globus_gsi_sysconfig_get_current_working_dir_unix()</code> and <code>globus_gsi_sysconfig_get_current_working_dir_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_GAA_CONF_FILENAME</h3>
<p>Determine the location of the GAA callout config file. </p>
<p> See <code>globus_gsi_sysconfig_get_gaa_conf_filename_unix()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_GRIDMAP_FILENAME</h3>
<p>Determine the location of the grid map file. </p>
<p> See <code>globus_gsi_sysconfig_get_gridmap_filename_unix()</code> and <code>globus_gsi_sysconfig_get_gridmap_filename_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_HOME_DIR</h3>
<p>Get the current users home directory </p>
<p> See <code>globus_gsi_sysconfig_get_home_dir_unix()</code> and globus_gsi_sysconfig_get_home_dir_win32()</p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_HOST_CERT_FILENAME</h3>
<p>Determine the location of the host certificate and private key </p>
<p> See <code>globus_gsi_sysconfig_get_host_cert_filename_unix()</code> and <code>globus_gsi_sysconfig_get_host_cert_filename_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_PROC_ID_STRING</h3>
<p>Get the current PID in string form </p>
<p> See <code>globus_gsi_sysconfig_get_proc_id_string_unix()</code> and globus_gsi_sysconfig_get_proc_id_string_win32()</p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_PROXY_FILENAME</h3>
<p>Determine the location of a proxy certificate and private key </p>
<p> See <code>globus_gsi_sysconfig_get_proxy_filename_unix()</code> and <code>globus_gsi_sysconfig_get_proxy_filename_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_SERVICE_CERT_FILENAME</h3>
<p>Determine the location of a service certificate and private key </p>
<p> See <code>globus_gsi_sysconfig_get_service_cert_filename_unix()</code> and <code>globus_gsi_sysconfig_get_service_cert_filename_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_SIGNING_POLICY_FILENAME</h3>
<p>Determine the name of the signing policy file for a given CA </p>
<p> See <code>globus_gsi_sysconfig_get_signing_policy_filename_unix()</code> and <code>globus_gsi_sysconfig_get_signing_policy_filename_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_UNIQUE_PROXY_FILENAME</h3>
<p>Generate a unqiue proxy file name </p>
<p> See <code>globus_gsi_sysconfig_get_unique_proxy_filename()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_USER_CERT_FILENAME</h3>
<p>Determine the location of the users certificate and private key </p>
<p> See <code>globus_gsi_sysconfig_get_user_cert_filename_unix()</code> and <code>globus_gsi_sysconfig_get_user_cert_filename_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_USER_ID_STRING</h3>
<p>Get the current UID in string form </p>
<p> See <code>globus_gsi_sysconfig_get_user_id_string_unix()</code> and globus_gsi_sysconfig_get_user_id_string_win32()</p>
<h3>#define GLOBUS_GSI_SYSCONFIG_GET_USERNAME</h3>
<p>Get the current user name </p>
<p> See <code>globus_gsi_sysconfig_get_username_unix()</code> and globus_gsi_sysconfig_get_username_win32()</p>
<h3>#define GLOBUS_GSI_SYSCONFIG_IS_SUPERUSER</h3>
<p>Determine whether the current user is the super user </p>
<p> See <code>globus_gsi_sysconfig_is_superuser_unix()</code> and <code>globus_gsi_sysconfig_is_superuser_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_MAKE_ABSOLUTE_PATH_FOR_FILENAME</h3>
<p>Prepend the current working directory to the give filename </p>
<p> See <code>globus_gsi_sysconfig_make_absolute_path_for_filename_unix()</code> and <code>globus_gsi_sysconfig_make_absolute_path_for_filename_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_REMOVE_ALL_OWNED_FILES</h3>
<p>Remove all proxies owned by current uid </p>
<p> See <code>globus_gsi_sysconfig_remove_all_owned_files_unix()</code> and <code>globus_gsi_sysconfig_remove_all_owned_files_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_SET_KEY_PERMISSIONS</h3>
<p>Set the correct file permissions on a private key. </p>
<p> See <code>globus_gsi_sysconfig_set_key_permissions_unix()</code> and <code>globus_gsi_sysconfig_set_key_permissions_win32()</code></p>
<h3>#define GLOBUS_GSI_SYSCONFIG_SPLIT_DIR_AND_FILENAME</h3>
<p>Split directory component of path from filename. </p>
<p> See <code>globus_gsi_sysconfig_split_dir_and_filename_unix()</code> and <code>globus_gsi_sysconfig_split_dir_and_filename_win32()</code></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_sysconfig from the source code.</p>
