---
title: "globus_gsi_sysconfig_get_home_dir_unix(3)"
name: "globus_gsi_sysconfig_get_home_dir_unix"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig_get_home_dir_unix/"
description: "Functions for UNIX platforms –"
---

<h2 class="name">NAME</h2>
<p> Functions for UNIX platforms &#8211; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_sysconfig_set_key_permissions_unix</code> (char *filename)<br />
 <i>UNIX &#8211; Set Key Permissions. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_user_id_string_unix</code> (char **user_id_string)<br />
 <i>UNIX &#8211; Get User ID. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_username_unix</code> (char **username)<br />
 <i>UNIX &#8211; Get Username. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_proc_id_string_unix</code> (char **proc_id_string)<br />
 <i>UNIX &#8211; Get Process ID. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_make_absolute_path_for_filename_unix</code> (char *filename, char **absolute_path)<br />
 <i>UNIX &#8211; Make Absolute Path. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_split_dir_and_filename_unix</code> (char *full_filename, char **dir_string, char **filename_string)<br />
 <i>UNIX &#8211; Split Directory and Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_current_working_dir_unix</code> (char **working_dir)<br />
 <i>UNIX &#8211; Get Current Working Directory. </i><br />
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
 globus_result_t <code>globus_gsi_sysconfig_get_user_cert_filename_unix</code> (char **user_cert, char **user_key)<br />
 <i>UNIX &#8211; Get User Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_host_cert_filename_unix</code> (char **host_cert, char **host_key)<br />
 <i>UNIX &#8211; Get Host Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_service_cert_filename_unix</code> (char *service_name, char **service_cert, char **service_key)<br />
 <i>UNIX &#8211; Get Service Certificate and Key Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_proxy_filename_unix</code> (char **user_proxy, <code>globus_gsi_proxy_file_type_t</code> proxy_file_type)<br />
 <i>UNIX &#8211; Get Proxy Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_signing_policy_filename_unix</code> (X509_NAME *ca_name, char *cert_dir, char **signing_policy_filename)<br />
 <i>UNIX &#8211; Get Signing Policy Filename. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_ca_cert_files_unix</code> (char *ca_cert_dir, globus_fifo_t *ca_cert_list)<br />
 <i>UNIX &#8211; Get CA Cert Filenames. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_remove_all_owned_files_unix</code> (char *default_filename)<br />
 <i>UNIX &#8211; Remove all proxies owned by current uid. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_is_superuser_unix</code> (int *is_superuser)<br />
 <i>UNIX &#8211; Check if the current user is root. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_gridmap_filename_unix</code> (char **filename)<br />
 <i>UNIX &#8211; Get the path and file name of the grid map file. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_authz_conf_filename_unix</code> (char **filename)<br />
 <i>UNIX &#8211; Get the path of authorization callback configuration. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_authz_lib_conf_filename_unix</code> (char **filename)<br />
 <i>UNIX &#8211; Get the path and file name of the authorization callback configuration file. </i><br />
 globus_result_t <code>globus_gsi_sysconfig_get_gaa_conf_filename_unix</code> (char **filename)<br />
 <i>UNIX &#8211; Get the path and file name of the gaa configuration file. </i></p>
<h2>Detailed Description</h2>
<p> These functions implement the UNIX version of the Globus GSI System Configuration API. <code>They should never be called directly, please use the provided platform independent defines.</code></p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_sysconfig_check_certfile_unix (const char *filename)</h3>
<p> UNIX &#8211; Check File Status for Cert. This is a convenience function used to check the status of a certificate file. The desired status is the current user has ownership and read/write permissions, while group and others only have read permissions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> The name of the file to check the status of</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the status of the file was able to be determined. Otherwise, an error object identifier</dl>
<h3>globus_result_t globus_gsi_sysconfig_check_keyfile_unix (const char *filename)</h3>
<p> UNIX &#8211; Check File Status for Key. This is a convenience function used to check the status of a private key file. The desired status is only the current user has ownership and read permissions, everyone else should not be able to access it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> The name of the file to check the status of</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the status of the file was able to be determined. Otherwise, an error object identifier</dl>
<h3>globus_result_t globus_gsi_sysconfig_dir_exists_unix (const char *filename)</h3>
<p> UNIX &#8211; Directory Exists. Check if the directory exists </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> The filename of the directory to check for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the directory exists, otherwise an error object identifier.</dl>
<h3>globus_result_t globus_gsi_sysconfig_file_exists_unix (const char *filename)</h3>
<p> UNIX &#8211; File Exists. Check if the file exists </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> The filename of the file to check for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the file exists and is readable, otherwise an error object identifier</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_authz_conf_filename_unix (char **filename)</h3>
<p> UNIX &#8211; Get the path of authorization callback configuration. Get the path and file name of the authorization callback configuration file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> Contains the location of the authorization callback configuration file upon successful return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_authz_lib_conf_filename_unix (char **filename)</h3>
<p> UNIX &#8211; Get the path and file name of the authorization callback configuration file. Get the path and file name of the authorization callback configuration file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> Contains the location of the authorization callback configuration file upon successful return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_ca_cert_files_unix (char *ca_cert_dir, globus_fifo_t *ca_cert_list)</h3>
<p> UNIX &#8211; Get CA Cert Filenames. Gets a list of trusted CA certificate filenames in a trusted CA certificate directory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ca_cert_dir</i> The trusted CA certificate directory to get the filenames from<br />
 <i>ca_cert_list</i> The resulting list of CA certificate filenames. This is a a globus list structure.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_fifo_t</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_cert_dir_unix (char **cert_dir)</h3>
<p> UNIX &#8211; Get Trusted CA Cert Dir. Get the Trusted Certificate Directory containing the trusted Certificate Authority certificates. This directory is determined in the order shown below. Failure in one method results in attempting the next. </p>
<dl>
<dt>1.</p>
<dd> <code>X509_CERT_DIR environment variable</code> &#8211; if this is set, the trusted certificates will be searched for in that directory. This variable allows the end user to specify the location of trusted certificates.</p>
<dt>2.</p>
<dd> <code>$HOME/.globus/certificates</code> &#8211; If this directory exists, and the previous methods of determining the trusted certs directory failed, this directory will be used.</p>
<dt>3.</p>
<dd> <code>/etc/grid-security/certificates</code> &#8211; This location is intended to be independent of the globus installation ($GLOBUS_LOCATION), and is generally only writeable by the host system administrator.</p>
<dt>4.</p>
<dd> <code>$GLOBUS_LOCATION/share/certificates</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cert_dir</i> The trusted certificates directory</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, and a sufficient trusted certificates directory was found. Otherwise, an error object identifier returned.</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_current_working_dir_unix (char **working_dir)</h3>
<p> UNIX &#8211; Get Current Working Directory. Get the current working directory on the system. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>working_dir</i> The current working directory</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_gaa_conf_filename_unix (char **filename)</h3>
<p> UNIX &#8211; Get the path and file name of the gaa configuration file. Get the path and file name of the GAA configuration file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> Contains the location of the GAA callback configuration file upon successful return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_gridmap_filename_unix (char **filename)</h3>
<p> UNIX &#8211; Get the path and file name of the grid map file. Get the path and file name of the grid map file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> Contains the location of the grid map file upon successful return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_home_dir_unix (char **home_dir)</h3>
<p> UNIX &#8211; Get HOME Directory </p>
<p> Get the HOME Directory of the current user. Should be the $HOME environment variable. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>home_dir</i> The home directory of the current user</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occured, otherwise an error object is returned.</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_host_cert_filename_unix (char **host_cert, char **host_key)</h3>
<p> UNIX &#8211; Get Host Certificate and Key Filenames. Get the Host Certificate and Key Filenames based on the current user&#8217;s environment. The host cert and key are searched for in the following locations (in order): </p>
<dl>
<dt>1.</p>
<dd> X509_USER_CERT and X509_USER_KEY environment variables</p>
<dt>2.</p>
<dd> <i>$GLOBUS_LOCATION</i>/etc/host[cert|key].pem</p>
<dt>3.</p>
<dd> <i>$HOME</i>/.globus/host[cert|key].pem</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>host_cert</i> pointer to the host certificate filename<br />
 <i>host_key</i> pointer to the host key filename</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the host cert and key were found, otherwise an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_proc_id_string_unix (char **proc_id_string)</h3>
<p> UNIX &#8211; Get Process ID. Get a unique string representing the current process. This is just the pid converted to a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proc_id_string</i> A unique string representing the process</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_proxy_filename_unix (char **user_proxy, <code>globus_gsi_proxy_file_type_t</code>proxy_file_type)</h3>
<p> UNIX &#8211; Get Proxy Filename. Get the proxy cert filename based on the following search order: </p>
<dl>
<dt>1.</p>
<dd> X509_USER_PROXY environment variable &#8211; This environment variable is set by the at run time for the specific application. If the proxy_file_type variable is set to GLOBUS_PROXY_OUTPUT (a proxy filename for writing is requested), and the X509_USER_PROXY is set, this will be the resulting value of the user_proxy filename string passed in. If the proxy_file_type is set to GLOBUS_PROXY_INPUT and X509_USER_PROXY is set, but the file it points to does not exist, or has some other readability issues, the function will continue checking using the other methods available.</dl>
<dl>
<dt>2.</p>
<dd> Check the default location for the proxy file of \/tmp\/x509_u\&lt;user_id\&gt; where \&lt;user id\&gt; is some unique string for that user on the host</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_proxy</i> the proxy filename of the user<br />
 <i>proxy_file_type</i> Switch for determining whether to return a existing proxy filename or if a filename suitable for creating a proxy should be returned</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_service_cert_filename_unix (char *service_name, char **service_cert, char **service_key)</h3>
<p> UNIX &#8211; Get Service Certificate and Key Filenames. Get the Service Certificate Filename based on the current user&#8217;s environment. The host cert and key are searched for in the following locations (in order): </p>
<dl>
<dt>1.</p>
<dd> X509_USER_CERT and X509_USER_KEY environment variables</p>
<dt>2.</p>
<dd> \/etc\/grid-security\/{service_name}\/{service_name}[cert|key].pem</p>
<dt>3.</p>
<dd> GLOBUS_LOCATION\/etc\/{service_name}\/{service_name}[cert|key].pem So for example, if my service was named: myservice, the location of the certificate would be: GLOBUS_LOCATION\/etc\/myservice\/myservicecert.pem</p>
<dt>4.</p>
<dd> \&lt;users home\&gt;\/.globus\/{service_name}\/{service_name}[cert|key].pem</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>service_name</i> The name of the service which allows us to determine the locations of cert and key files to look for<br />
 <i>service_cert</i> pointer to the host certificate filename<br />
 <i>service_key</i> pointer to the host key filename</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the service cert and key were found, otherwise an error object identifier</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_signing_policy_filename_unix (X509_NAME *ca_name, char *cert_dir, char **signing_policy_filename)</h3>
<p> UNIX &#8211; Get Signing Policy Filename. Get the Signing Policy Filename on the current system, based on the CA&#8217;s subject name, and the trusted certificates directory </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ca_name</i> The X509 subject name of the CA to get the signing policy of. The hash of the CA is generated from this<br />
 <i>cert_dir</i> The trusted CA certificates directory, containing the singing_policy files of the trusted CA&#8217;s.<br />
 <i>signing_policy_filename</i> The resulting singing_policy filename</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_user_cert_filename_unix (char **user_cert, char **user_key)</h3>
<p> UNIX &#8211; Get User Certificate and Key Filenames. Get the User Certificate Filename based on the current user&#8217;s environment. The following locations are searched for cert and key files in order: </p>
<dl>
<dt>1.</p>
<dd> environment variables X509_USER_CERT and X509_USER_KEY</p>
<dt>2.</p>
<dd> $HOME/.globus/usercert.pem and $HOME/.globus/userkey.pem</p>
<dt>3.</p>
<dd> $HOME/.globus/usercred.p12 &#8211; this is a PKCS12 credential</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_cert</i> pointer the filename of the user certificate<br />
 <i>user_key</i> pointer to the filename of the user key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the cert and key files were found in one of the possible locations, otherwise an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_user_id_string_unix (char **user_id_string)</h3>
<p> UNIX &#8211; Get User ID. Get a unique string representing the current user. This is just the uid converted to a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_id_string</i> A unique string representing the user</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred</dl>
<h3>globus_result_t globus_gsi_sysconfig_get_username_unix (char **username)</h3>
<p> UNIX &#8211; Get Username. Get the username of the current user. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>username</i> This parameter will contain the current user name upon a successful return. It is the users responsibility to free memory allocated for this return value.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred</dl>
<h3>globus_result_t globus_gsi_sysconfig_is_superuser_unix (int *is_superuser)</h3>
<p> UNIX &#8211; Check if the current user is root. Checks whether the current user is root. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>is_superuser</i> 1 if the user is the superuser 0 if not</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_make_absolute_path_for_filename_unix (char *filename, char **absolute_path)</h3>
<p> UNIX &#8211; Make Absolute Path. Make the filename into an absolute path string based on the current working directory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i> the filename to get the absolute path of.<br />
 <i>absolute_path</i> The resulting absolute path. This needs to be freed when no longer needed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_remove_all_owned_files_unix (char *default_filename)</h3>
<p> UNIX &#8211; Remove all proxies owned by current uid. Removes all proxies (ie. all delegated and grid-proxy-init generated proxies) found in the secure tmp directory that are owned by the current user. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>default_filename</i> The filename of the default proxy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned</dl>
<h3>globus_result_t globus_gsi_sysconfig_set_key_permissions_unix (char *filename)</h3>
<p> UNIX &#8211; Set Key Permissions. Set the file permissions of a file to read-write only by the user which are the permissions that should be set for all private keys. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filename</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object id</dl>
<h3>globus_result_t globus_gsi_sysconfig_split_dir_and_filename_unix (char *full_filename, char **dir_string, char **filename_string)</h3>
<p> UNIX &#8211; Split Directory and Filename. Split the directory and filename portions of a filename string into two separate strings </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>full_filename</i> The filename to split. Splits on the last occurrence of &#8216;/&#8217; where the directory is everything before the last &#8216;/&#8217;, and the filename is everything after.<br />
 <i>dir_string</i> The directory portion of the filename string. If no &#8216;/&#8217; is found throughout the string, this variable points to NULL. This needs to be freed when no longer needed.<br />
 <i>filename_string</i> The filename portion of the filename string. If no &#8216;/&#8217; is found throughout, this variable is a duplicate of the full_filename parameter. This needs to be freed when no longer needed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error occurred. Otherwise an error object ID is returned.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_sysconfig from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBE">Author</a></p>
<dd></dl>
