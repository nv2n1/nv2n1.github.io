---
title: "globus_gsi_sysconfig_error_removing_owned_files(3)"
name: "globus_gsi_sysconfig_error_removing_owned_files"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig_error_removing_owned_files/"
description: "Data Types –"
---

<p>Data Types &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gsi_sysconfig_error_t</code> { <code>GLOBUS_GSI_SYSCONFIG_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CERT_DIR</code> = 1, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CERT_STRING</code> = 2, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_KEY_STRING</code> = 3, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_HOME_DIR</code> = 4, <code>GLOBUS_GSI_SYSCONFIG_ERROR_ERRNO</code> = 5, <code>GLOBUS_GSI_SYSCONFIG_ERROR_CHECKING_FILE_EXISTS</code> = 6, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CERT_FILENAME</code> = 7, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_PROXY_FILENAME</code> = 8, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_DELEG_FILENAME</code> = 9, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CA_CERT_FILENAMES</code> = 10, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CWD</code> = 11, <code>GLOBUS_GSI_SYSCONFIG_ERROR_REMOVING_OWNED_FILES</code> = 12, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_GRIDMAP_FILENAME</code> = 13, <code>GLOBUS_GSI_SYSCONFIG_ERROR_CHECKING_SUPERUSER</code> = 14, <code>GLOBUS_GSI_SYSCONFIG_ERROR_SETTING_PERMS</code> = 15, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_SIGNING_POLICY</code> = 16, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_PW_ENTRY</code> = 17, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_AUTHZ_FILENAME</code> = 18, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_NOT_REGULAR</code> = 19, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_DOES_NOT_EXIST</code> = 20, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_BAD_PERMISSIONS</code> = 21, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_NOT_OWNED</code> = 22, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_IS_DIR</code> = 23, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_ZERO_LENGTH</code> = 24, <code>GLOBUS_GSI_SYSCONFIG_INVALID_ARG</code> = 25, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_HAS_LINKS</code> = 26, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_HAS_CHANGED</code> = 27, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_AUTHZ_LIB_FILENAME</code> = 28, <code>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_GAA_FILENAME</code> = 29, <code>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_NOT_DIR</code> = 30, <code>GLOBUS_GSI_SYSCONFIG_ERROR_LAST</code> = 31 } </p>
<p> enum <code>globus_gsi_proxy_file_type_t</code> { <code>GLOBUS_PROXY_FILE_INPUT</code>, <code>GLOBUS_PROXY_FILE_OUTPUT</code> } </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gsi_proxy_file_type_t</code></h3>
<p>Enumerator used to keep track of input/output types of filenames </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_PROXY_FILE_INPUT </i></p>
<dd>The proxy filename is intended for reading (it should already exist)</p>
<dt><i>GLOBUS_PROXY_FILE_OUTPUT </i></p>
<dd>The proxy filename is intended for writing (it does not need to exist)</dl>
<h3>enum <code>globus_gsi_sysconfig_error_t</code></h3>
<p>GSI System Config Error codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_SUCCESS </i></p>
<dd>Success &#8211; never used</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CERT_DIR </i></p>
<dd>Unable to determine trusted certificates directory</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CERT_STRING </i></p>
<dd>Error while generating certificate filename</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_KEY_STRING </i></p>
<dd>Error while generating private key filename</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_HOME_DIR </i></p>
<dd>Unable to determine user&#8217;s home directory</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_ERRNO </i></p>
<dd>System Error &#8212; see underlying error for details</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_CHECKING_FILE_EXISTS </i></p>
<dd>Unable to determine whether file exists</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CERT_FILENAME </i></p>
<dd>Unable to determine the location of the certificate file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_PROXY_FILENAME </i></p>
<dd>Unable to determine the location of the proxy file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_DELEG_FILENAME </i></p>
<dd>Unable to determine the location of the delegated proxy file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CA_CERT_FILENAMES </i></p>
<dd>Unable to generate a list of CA certificate filenames</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_CWD </i></p>
<dd>Error while discovering the current working directory</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_REMOVING_OWNED_FILES </i></p>
<dd>Failed to remove all proxy files</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_GRIDMAP_FILENAME </i></p>
<dd>Unable to determine the location of the grid map file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_CHECKING_SUPERUSER </i></p>
<dd>Failure while checking whether the current user is the super user</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_SETTING_PERMS </i></p>
<dd>Error while trying to set file permissions</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_SIGNING_POLICY </i></p>
<dd>Unable to determine the location of a signing policy file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_PW_ENTRY </i></p>
<dd>Could not find password entry for user</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_AUTHZ_FILENAME </i></p>
<dd>Failed to locate the authorization callout configuration file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_NOT_REGULAR </i></p>
<dd>File is not a regular file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_DOES_NOT_EXIST </i></p>
<dd>File does not exist</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_BAD_PERMISSIONS </i></p>
<dd>File has incorrect permissions for operation</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_NOT_OWNED </i></p>
<dd>File is not owned by current user</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_IS_DIR </i></p>
<dd>File is a directory</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_ZERO_LENGTH </i></p>
<dd>File has zero length</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_INVALID_ARG </i></p>
<dd>Invalid argument</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_HAS_LINKS </i></p>
<dd>File has more than one link</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_HAS_CHANGED </i></p>
<dd>File has changed in the meantime</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_AUTHZ_LIB_FILENAME </i></p>
<dd>Failed to locate the authorization callout library configuration file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_GETTING_GAA_FILENAME </i></p>
<dd>Failed to locate the GAA configuration file</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_FILE_NOT_DIR </i></p>
<dd>File is not a directory</p>
<dt><i>GLOBUS_GSI_SYSCONFIG_ERROR_LAST </i></p>
<dd>Last marker &#8211; never used</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_sysconfig from the source code.</p>
