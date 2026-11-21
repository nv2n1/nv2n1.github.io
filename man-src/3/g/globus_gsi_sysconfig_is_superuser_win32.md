---
title: "globus_gsi_sysconfig_is_superuser_win32(3)"
name: "globus_gsi_sysconfig_is_superuser_win32"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig_is_superuser_win32/"
description: "Functions for Win32 platforms –"
---
<h2 class="name">NAME</h2>
<p> Functions for Win32 platforms - </p>
<h3>Functions</h3>
<p> <br />
 globus_result_t <code>globus_gsi_sysconfig_set_key_permissions_win32</code> (char *filename) <br />
 <i>Win32 - Set Key Permissions. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_file_exists_win32</code> (const char *filename) <br />
 <i>Win32 - File Exists. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_dir_exists_win32</code> (const char *filename) <br />
 <i>Win32 - Directory Exists. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_current_working_dir_win32</code> (char **working_dir) <br />
 <i>Win32 - Get Current Working Directory. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_make_absolute_path_for_filename_win32</code> (char *filename, char **absolute_path) <br />
 <i>Win32 - Make Absolute Path. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_split_dir_and_filename_win32</code> (char *full_filename, char **dir_string, char **filename_string) <br />
 <i>Win32 - Split Directory and Filename. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_cert_dir_win32</code> (char **cert_dir) <br />
 <i>Win32 - Get Trusted CA Cert Dir. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_user_cert_filename_win32</code> (char **user_cert, char **user_key) <br />
 <i>Win32 - Get User Certificate Filename. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_host_cert_filename_win32</code> (char **host_cert, char **host_key) <br />
 <i>Win32 - Get Host Certificate and Key Filenames. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_service_cert_filename_win32</code> (char *service_name, char **service_cert, char **service_key) <br />
 <i>Win32 - Get Service Certificate and Key Filenames. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_proxy_filename_win32</code> (char **user_proxy, <code>globus_gsi_proxy_file_type_t</code> proxy_file_type) <br />
 <i>Win32 - Get Proxy Filename. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_ca_cert_files_win32</code> (char *ca_cert_dir, globus_fifo_t *ca_cert_list) <br />
 <i>Win32 - Get CA Cert Filenames. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_remove_all_owned_files_win32</code> (char *default_filename) <br />
 <i>Win32 - Remove all proxies owned by current uid. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_gridmap_filename_win32</code> (char **filename) <br />
 <i>Win32 - Get the path and file name of the grid map file. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_authz_conf_filename_win32</code> (char **filename) <br />
 <i>Win32 - Get the path and file name of the grid map file. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_authz_lib_conf_filename_win32</code> (char **filename) <br />
 <i>Win32 - Get authorization configuration filename. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_gaa_conf_filename_win32</code> (char **filename) <br />
 <i>Win32 - Get the path and file name of the gaa config file. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_is_superuser_win32</code> (int *is_superuser) <br />
 <i>Win32 - Check if the current user is root. </i> <br />
 globus_result_t <code>globus_gsi_sysconfig_get_signing_policy_filename_win32</code> (X509_NAME *ca_name, char *cert_dir, char **signing_policy_filename) <br />
 <i>Win32 - Get Signing Policy Filename. </i>  </p>
<h2>Detailed Description</h2>
<p> These functions implement the Win32 version of the Globus GSI System Configuration API. <code>They should never be called directly, please use the provided platform independent defines.</code>  </p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_sysconfig_dir_exists_win32 (const char *filename)</h3>
<p> Win32 - Directory Exists. Check that the directory exists </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> the file to check </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if the directory exists, otherwise an error object identifier. </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_file_exists_win32 (const char *filename)</h3>
<p> Win32 - File Exists. Check that the file exists </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> the file to check </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS (even if the file doesn&#8217;t exist) - in some abortive cases an error object identifier is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_authz_conf_filename_win32 (char **filename)</h3>
<p> Win32 - Get the path and file name of the grid map file. Get the path and file name of the authorization callback configuration file </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> Contains the location of the authorization callback configuration file upon successful return </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_authz_lib_conf_filename_win32 (char **filename)</h3>
<p> Win32 - Get authorization configuration filename. Get the path and file name of the authorization callback library configuration file </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> Contains the location of the authorization callback library configuration file upon successful return </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_ca_cert_files_win32 (char *ca_cert_dir, globus_fifo_t *ca_cert_list)</h3>
<p> Win32 - Get CA Cert Filenames. Gets a list of trusted CA certificate filenames in a trusted CA certificate directory. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>ca_cert_dir</i> The trusted CA certificate directory to get the filenames from <br />
 <i>ca_cert_list</i> The resulting list of CA certificate filenames. This is a globus list structure. </p>
 </dd></dl>
<p> <code>See Also:</code> </p>
<dl>
<dd> <p> globus_fifo_t </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_cert_dir_win32 (char **cert_dir)</h3>
<p> Win32 - Get Trusted CA Cert Dir. Get the Trusted Certificate Directory containing the trusted Certificate Authority certificates. This directory is determined in the order shown below. Failure in one method results in attempting the next. </p>
<dl>
<dt>1.</dt>
<dd> <p> <code>X509_CERT_DIR environment variable</code> - if this is set, the trusted certificates will be searched for in that directory. This variable allows the end user to specify the location of trusted certificates. </p>
 </dd>
<dt>2.</dt>
<dd> <p> <code>x509_cert_dir registry key</code> - If this registry key is set on windows, the directory it points to should contain the trusted certificates. The path to the registry key is software\Globus\GSI </p>
 </dd>
<dt>3.</dt>
<dd> <p> <code>\&lt;user home directory&gt;\</code><code>.globus\certificates</code> - If this directory exists, and the previous methods of determining the trusted certs directory failed, this directory will be used. </p>
 </dd>
<dt>4.</dt>
<dd> <p> <code>Host Trusted Cert Dir</code> - This location is intended to be independent of the globus installation ($GLOBUS_LOCATION), and is generally only writeable by the host system administrator. </p>
 </dd>
<dt>5.</dt>
<dd> <p> <code>Globus Install Trusted Cert Dir</code> - this is $GLOBUS_LOCATION\share\certificates. </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>cert_dir</i> The trusted certificates directory </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, and a sufficient trusted certificates directory was found. Otherwise, an error object identifier returned. </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_current_working_dir_win32 (char **working_dir)</h3>
<p> Win32 - Get Current Working Directory. Get the current working directory on a windows system </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>working_dir</i> The working directory to get </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_gaa_conf_filename_win32 (char **filename)</h3>
<p> Win32 - Get the path and file name of the gaa config file. Get the path and file name of the gaa config configuration file . </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> Contains the location of the authorization callback configuration file upon successful return </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_gridmap_filename_win32 (char **filename)</h3>
<p> Win32 - Get the path and file name of the grid map file. Get the path and file name of the grid map file. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> Contains the location of the grid map file upon successful return </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_host_cert_filename_win32 (char **host_cert, char **host_key)</h3>
<p> Win32 - Get Host Certificate and Key Filenames. Get the Host Certificate and Key Filenames based on the current user&#8217;s environment. The host cert and key are searched for in the following locations (in order): </p>
<dl>
<dt>1.</dt>
<dd> <p> X509_USER_CERT and X509_USER_KEY environment variables </p>
 </dd>
<dt>2.</dt>
<dd> <p> registry keys x509_user_cert and x509_user_key in software\Globus\GSI </p>
 </dd>
<dt>3.</dt>
<dd> <p> <code>&lt;GLOBUS_LOCATION&gt;\etc\host[cert|key].pem</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> <code>&lt;users home directory&gt;\</code><code>.globus\host[cert|key].pem</code> </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>host_cert</i> pointer to the host certificate filename <br />
 <i>host_key</i> pointer to the host key filename </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if the host cert and key were found, otherwise an error object identifier is returned </p>
 </dd></dl>
<code></code><h3>globus_result_t globus_gsi_sysconfig_get_proxy_filename_win32 (char **user_proxy, globus_gsi_proxy_file_type_t proxy_file_type)</h3>
<p> Win32 - Get Proxy Filename. Get the proxy cert filename based on the following search order: </p>
<dl>
<dt>1.</dt>
<dd> <p> X509_USER_PROXY environment variable - This environment variable is set by the at run time for the specific application. If the proxy_file_type variable is set to GLOBUS_PROXY_OUTPUT (a proxy filename for writing is requested), and the X509_USER_PROXY is set, this will be the resulting value of the user_proxy filename string passed in. If the proxy_file_type is set to GLOBUS_PROXY_INPUT and X509_USER_PROXY is set, but the file it points to does not exist, or has some other readability issues, the function will continue checking using the other methods available. </p>
 </dd></dl>
<dl>
<dt>2.</dt>
<dd> <p> check the registry key: x509_user_proxy. Just as with the environment variable, if the registry key is set, and proxy_file_type is GLOBUS_PROXY_OUTPUT, the string set to be the proxy filename will be this registry key&#8217;s value. If proxy_file_type is GLOBUS_PROXY_INPUT, and the file doesn&#8217;t exist, the function will check the next method for the proxy&#8217;s filename. </p>
 </dd></dl>
<dl>
<dt>3.</dt>
<dd> <p> Check the default location for the proxy file. The default location should be set to reside in the temp directory on that host, with the filename taking the format: x509_u&lt;user id&gt; where &lt;user id&gt; is some unique string for that user on the host </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>user_proxy</i> the proxy filename of the user <br />
 <i>proxy_file_type</i> Switch for determining whether to return a existing proxy filename or if a filename suitable for creating a proxy should be returned </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS or an error object identifier </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_service_cert_filename_win32 (char *service_name, char **service_cert, char **service_key)</h3>
<p> Win32 - Get Service Certificate and Key Filenames. Get the Service Certificate Filename based on the current user&#8217;s environment. The host cert and key are searched for in the following locations (in order): </p>
<dl>
<dt>1.</dt>
<dd> <p> X509_USER_CERT and X509_USER_KEY environment variables </p>
 </dd>
<dt>2.</dt>
<dd> <p> registry keys x509_user_cert and x509_user_key in software\Globus\GSI </p>
 </dd>
<dt>3.</dt>
<dd> <p> GLOBUS_LOCATION\etc\{service_name}\{service_name}[cert|key].pem So for example, if my service was named: myservice, the location of the certificate would be: <code>&lt;GLOBUS_LOCATION&gt;\etc\myservice\myservicecert.pem</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> <code>&lt;users home&gt;\</code><code>.globus\{service_name}\{service_name}[cert|key].pem</code> </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>service_name</i> The name of the service which allows us to determine the locations of cert and key files to look for <br />
 <i>service_cert</i> pointer to the host certificate filename <br />
 <i>service_key</i> pointer to the host key filename </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if the service cert and key were found, otherwise an error object identifier </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_signing_policy_filename_win32 (X509_NAME *ca_name, char *cert_dir, char **signing_policy_filename)</h3>
<p> Win32 - Get Signing Policy Filename. Get the Signing Policy Filename on the current system, based on the CA&#8217;s subject name, and the trusted certificates directory </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>ca_name</i> The X.509 subject name of the CA to get the signing policy of. The hash of the CA is generated from this <br />
 <i>cert_dir</i> The trusted CA certificates directory, containing the singing_policy files of the trusted CAs. <br />
 <i>signing_policy_filename</i> The resulting singing_policy filename </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_get_user_cert_filename_win32 (char **user_cert, char **user_key)</h3>
<p> Win32 - Get User Certificate Filename. Get the User Certificate Filename based on the current user&#8217;s environment. The following locations are searched for cert and key files in order: </p>
<dl>
<dt>1.</dt>
<dd> <p> environment variables X509_USER_CERT and X509_USER_KEY </p>
 </dd>
<dt>2.</dt>
<dd> <p> registry keys x509_user_cert and x509_user_key in software\Globus\GSI </p>
 </dd>
<dt>3.</dt>
<dd> <p> <code>&lt;users home directory&gt;\</code><code>.globus\usercert.pem</code> and <code>&lt;users home directory&gt;\</code><code>.globus\userkey.pem</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> <code>&lt;users home directory&gt;\</code><code>.globus\usercred.p12</code> - this is a PKCS12 credential </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>user_cert</i> pointer the filename of the user certificate <br />
 <i>user_key</i> pointer to the filename of the user key </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if the cert and key files were found in one of the possible locations, otherwise an error object identifier is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_is_superuser_win32 (int *is_superuser)</h3>
<p> Win32 - Check if the current user is root. Checks whether the current user is root. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>is_superuser</i> 1 if the user is the superuser 0 if not </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_make_absolute_path_for_filename_win32 (char *filename, char **absolute_path)</h3>
<p> Win32 - Make Absolute Path. Make the filename into an absolute path string based on the current working directory. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> the filename to get the absolute path of. <br />
 <i>absolute_path</i> The resulting absolute path </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_remove_all_owned_files_win32 (char *default_filename)</h3>
<p> Win32 - Remove all proxies owned by current uid. Removes all proxies (all delegated and grid-proxy-init generated proxies) found in the secure temp directory that are owned by the current user. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>default_filename</i> The filename of the default proxy </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS if no error occurred, otherwise an error object ID is returned </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_set_key_permissions_win32 (char *filename)</h3>
<p> Win32 - Set Key Permissions. Set the file permissions of a file to read only by the user which are the permissions that should be set for all private keys. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>filename</i> </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> GLOBUS_SUCCESS or an error object id </p>
 </dd></dl>
<h3>globus_result_t globus_gsi_sysconfig_split_dir_and_filename_win32 (char *full_filename, char **dir_string, char **filename_string)</h3>
<p> Win32 - Split Directory and Filename. Split the directory and filename portions of a filename string into two separate strings </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>full_filename</i> <br />
 <i>dir_string</i> <br />
 <i>filename_string</i> </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd>  </dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_sysconfig from the source code. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAC">Functions</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAD">Detailed Description</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">Function Documentation</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAF">globus_result_t globus_gsi_sysconfig_dir_exists_win32 (const char *filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">globus_result_t globus_gsi_sysconfig_file_exists_win32 (const char *filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">globus_result_t globus_gsi_sysconfig_get_authz_conf_filename_win32 (char **filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">globus_result_t globus_gsi_sysconfig_get_authz_lib_conf_filename_win32 (char **filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">globus_result_t globus_gsi_sysconfig_get_ca_cert_files_win32 (char *ca_cert_dir, globus_fifo_t *ca_cert_list)</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">globus_result_t globus_gsi_sysconfig_get_cert_dir_win32 (char **cert_dir)</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">globus_result_t globus_gsi_sysconfig_get_current_working_dir_win32 (char **working_dir)</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">globus_result_t globus_gsi_sysconfig_get_gaa_conf_filename_win32 (char **filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">globus_result_t globus_gsi_sysconfig_get_gridmap_filename_win32 (char **filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">globus_result_t globus_gsi_sysconfig_get_host_cert_filename_win32 (char **host_cert, char **host_key)</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">globus_result_t globus_gsi_sysconfig_get_proxy_filename_win32 (char **user_proxy, <code>globus_gsi_proxy_file_type_t</code>proxy_file_type)</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">globus_result_t globus_gsi_sysconfig_get_service_cert_filename_win32 (char *service_name, char **service_cert, char **service_key)</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">globus_result_t globus_gsi_sysconfig_get_signing_policy_filename_win32 (X509_NAME *ca_name, char *cert_dir, char **signing_policy_filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">globus_result_t globus_gsi_sysconfig_get_user_cert_filename_win32 (char **user_cert, char **user_key)</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">globus_result_t globus_gsi_sysconfig_is_superuser_win32 (int *is_superuser)</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">globus_result_t globus_gsi_sysconfig_make_absolute_path_for_filename_win32 (char *filename, char **absolute_path)</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">globus_result_t globus_gsi_sysconfig_remove_all_owned_files_win32 (char *default_filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAW">globus_result_t globus_gsi_sysconfig_set_key_permissions_win32 (char *filename)</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">globus_result_t globus_gsi_sysconfig_split_dir_and_filename_win32 (char *full_filename, char **dir_string, char **filename_string)</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAY">Author</a></dt>
<dd>  </dd></dl>
