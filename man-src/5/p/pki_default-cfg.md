---
title: "pki_default-cfg(5)"
name: "pki_default-cfg"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pki_default-cfg/"
description: "pki_default.cfg – Certificate Server instance default config file."
---

<p>pki_default.cfg &#8211; Certificate Server instance default config file.</p>
<h2>Location</h2>
<p>/etc/pki/default.cfg</p>
<h2>Description</h2>
<p>This file contains the default settings for a Certificate Server instance created using <code>pkispawn</code>. This file should not be edited, as it can be modified when the Certificate Server packages are updated. Instead, when setting up a Certificate Server instance, a user should provide <code>pkispawn</code> with a configuration file containing overrides to the defaults in <code>/etc/pki/default.cfg</code>. See <code><a href="/docs/linux/man/8-pkispawn/">pkispawn</a>(8)</code> for details. </p>
<h2>Sections</h2>
<p><i>default.cfg</i> contains parameters that are grouped into sections. These sections are stacked, so that parameters defined in earlier sections can be overwritten by parameters defined in later sections. The sections are read in the following order: [DEFAULT], [Tomcat], and the subsystem section ([CA], [KRA], [OCSP], [TKS], or [TPS]). This allows the ability to specify parameters to be shared by all subsystems in [DEFAULT] or [Tomcat], and subsystem-specific customization. </p>
<p> There are a small number of bootstrap parameters which are passed in the configuration file by <code>pkispawn</code>. Other parameter&#8217;s values can be interpolated tokens rather than explicit values. For example: </p>
<p> <code>pki_ca_signing_nickname=caSigningCert cert-%(pki_instance_name)s CA</code> </p>
<p> This substitutes the value of pki_instance_name into the parameter value. It is possible to interpolate any non-password parameter within a section or in [DEFAULT]. Any parameter used in interpolation can <code>ONLY</code> be overridden within the same section. So, for example, pki_instance_name should only be overridden in [DEFAULT]; otherwise, interpolations can fail.</p>
<dl>
<dt><code>Note:</code></p>
<dd>Any non-password related parameter values in the configuration file that needs to contain a <code>%</code> character must be properly escaped. For example, a value of <code>foo%bar</code> would be specified as <code>foo%%bar</code> in the configuration file. </p>
</dl>
<h2>Pre-Check Parameters</h2>
<p>Once the configuration parameters have been constructed from the above sections and overrides, pkispawn will perform a series of basic tests to determine if the parameters being passed in are valid and consistent, before starting any installation. In pre-check mode, these tests are executed and then pkispawn exits. </p>
<p> It is possible to disable specific tests by setting the directives below. While all these tests should pass to ensure a successful installation, it may be reasonable to skip tests in pre-check mode.</p>
<dl>
<dt><code>pki_skip_ds_verify</code></p>
<dd>
<dd>Skip verification of the Directory Server credentials. In this test, pkispawn attempts to bind to the directory server instance for the internal database using the provided credentials. This could be skipped if the directory server instance does not yet exist or is inaccessible. Defaults to False.</p>
<dt><code>pki_skip_sd_verify</code></p>
<dd>
<dd>Skip verification of the security domain user/password. In this test, pkispawn attempts to log onto the security domain using the provided credentials. This can be skipped if the security domain is unavailable. Defaults to False. </p>
</dl>
<h2>General Instance Parameters</h2>
<p>The parameters described below, as well as the parameters located in the following sections, can be customized as part of a deployment. This list is not exhaustive.</p>
<dl>
<dt><code>pki_instance_name</code></p>
<dd>
<dd>Name of the instance. The instance is located at /var/lib/pki/&lt;instance_name&gt;. For Java subsystems, the default is specified as pki-tomcat.</p>
<dt><code>pki_https_port, pki_http_port</code></p>
<dd>
<dd>Secure and unsecure ports. Defaults to standard Tomcat ports 8443 and 8080, respectively, for Java subsystems.</p>
<dt><code>pki_ajp_port, pki_tomcat_server_port</code></p>
<dd>
<dd>Ports for Tomcat subsystems. Defaults to standard Tomcat ports of 8009 and 8005, respectively.</p>
<dt><code>pki_ajp_host</code></p>
<dd>
<dd>Host on which to listen for AJP requests. Defaults to localhost to listen to local traffic only.</p>
<dt><code>pki_proxy_http_port, pki_proxy_https_port, pki_enable_proxy</code></p>
<dd>
<dd>Ports for an Apache proxy server. Certificate Server instances can be run behind an Apache proxy server, which will communicate with the Tomcat instance through the AJP port. See the Red Hat Certificate System documentation at <a rel="nofollow" href="https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/">https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/</a> for details.</p>
<dt><code>pki_user, pki_group, pki_audit_group</code></p>
<dd>
<dd>Specifies the default administrative user, group, and auditor group identities for PKI instances. The default user and group are both specified as <code>pkiuser</code>, and the default audit group is specified as <code>pkiaudit</code>.</p>
<dt><code>pki_token_name, pki_token_password</code></p>
<dd>
<dd>The token and password where this instance&#8217;s system certificate and keys are stored. Defaults to the NSS internal software token.</p>
<dt><code>pki_hsm_enable, pki_hsm_libfile, pki_hsm_modulename</code></p>
<dd>
<dd>If an optional hardware security module (HSM) is being utilized (rather than the default software security module included in NSS), then the <code>pki_hsm_enable</code> parameter must be set to &#8216;True&#8217; (by default this parameter is &#8216;False&#8217;), and values must be supplied for both the <code>pki_hsm_libfile</code> (e. g. &#8211; <code>pki_hsm_libfile=/opt/nfast/toolkits/pkcs11/libcknfast.so</code>) and pki_hsm_modulename<code> parameters (e. g. &#8211; pki_hsm_modulename=nethsm</code>). </p>
</dl>
<h3>System Certificate Parameters</h3>
<p><code>pkispawn</code> sets up a number of system certificates for each subsystem. The system certificates which are required differ between subsystems. Each system certificate is denoted by a tag, as noted below. The different system certificates are:</p>
<dl>
<dd>* signing certificate (&quot;signing&quot;). Used to sign other certificates. Required for CA.</p>
<dd>* OCSP signing certificate (&quot;ocsp_signing&quot; in CA, &quot;signing&quot; in OCSP). Used to sign CRLs. Required for OCSP and CA.</p>
<dd>* storage certificate (&quot;storage&quot;). Used to encrypt keys for storage in KRA. Required for KRA only.</p>
<dd>* transport certificate (&quot;transport&quot;). Used to encrypt keys in transport to the KRA. Required for KRA only.</p>
<dd>* subsystem certificate (&quot;subsystem&quot;). Used to communicate between subsystems within the security domain. Issued by the security domain CA. Required for all subsystems.</p>
<dd>* server certificate (&quot;sslserver&quot;). Used for communication with the server. One server certificate is required for each Certificate Server instance.</p>
<dd>* audit signing certificate (&quot;audit_signing&quot;). Used to sign audit logs. Required for all subsystems except the RA.</dl>
<p> Each system certificate can be customized using the parameters below:</p>
<dl>
<dt><code>pki_&lt;tag&gt;_key_type, pki_&lt;type&gt;_keysize, pki_&lt;tag&gt;_key_algorithm</code></p>
<dd>
<dd>Characteristics of the private key. See the Red Hat Certificate System documentation at <a rel="nofollow" href="https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/">https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/</a> for possible options. The defaults are RSA for the type, 2048 bits for the key size, and SHA256withRSA for the algorithm.</p>
<dt><code>pki_&lt;tag&gt;_signing_algorithm</code></p>
<dd>
<dd>For signing certificates, the algorithm used for signing. Defaults to SHA256withRSA.</p>
<dt><code>pki_&lt;tag&gt;_token</code></p>
<dd>
<dd>Location where the certificate and private key are stored. Defaults to the internal software NSS token database.</p>
<dt><code>pki_&lt;tag&gt;_nickname</code></p>
<dd>
<dd>Nickname for the certificate in the token database.</p>
<dt><code>pki_&lt;tag&gt;_subject_dn</code></p>
<dd>
<dd>Subject DN for the certificate. The subject DN for the SSL Server certificate must include CN=&lt;hostname&gt;.</dl>
<h3>Admin User Parameters</h3>
<p><code>pkispawn</code> creates a bootstrap administrative user that is a member of all the necessary groups to administer the installed subsystem. On a security domain CA, the CA administrative user is also a member of the groups required to register a new subsystem on the security domain. The certificate and keys for this administrative user are stored in a PKCS #12 file in <code>pki_client_dir</code>, and can be imported into a browser to administer the system.</p>
<dl>
<dt><code>pki_admin_name, pki_admin_uid</code></p>
<dd>
<dd>Name and UID of this administrative user. Defaults to caadmin for CA, kraadmin for KRA, etc.</p>
<dt><code>pki_admin_password</code></p>
<dd>
<dd>Password for the admin user. This password is used to log into the pki-console (unless client authentication is enabled), as well as log into the security domain CA.</p>
<dt><code>pki_admin_email</code></p>
<dd>
<dd>Email address for the admin user.</p>
<dt><code>pki_admin_dualkey, pki_admin_keysize, pki_admin_key_type</code></p>
<dd>
<dd>Settings for the administrator certificate and keys.</p>
<dt><code>pki_admin_subject_dn</code></p>
<dd>
<dd>Subject DN for the administrator certificate. Defaults to <code>cn=PKI Administrator, e=%(pki_admin_email)s, o=%(pki_security_domain_name)s</code>.</p>
<dt><code>pki_admin_nickname</code></p>
<dd>Nickname for the administrator certificate.</p>
<dt><code>pki_import_admin_cert</code></p>
<dd>
<dd>Set to True to import an existing admin certificate for the admin user, rather than generating a new one. A subsystem-specific administrator will still be created within the subsystem&#8217;s LDAP tree. This is useful to allow multiple subsystems within the same instance to be more easily administered from the same browser by using a single certificate. </p>
<p> By default, this is set to False for CA subsystems and true for KRA, OCSP, TKS, and TPS subsystems. In this case, the admin certificate is read from the file ca_admin.cert in <code>pki_client_dir</code>. </p>
<p> Note that cloned subsystems do not create a new administrative user. The administrative user of the master subsystem is used instead, and the details of this master user are replicated during the install.</p>
<dt><code>pki_client_admin_cert_p12</code></p>
<dd>
<dd>Location for the PKCS #12 file containing the administrative user&#8217;s certificate and keys. For a CA, this defaults to <i>ca_admin_cert.p12</i> in the <code>pki_client_dir</code> directory.</dl>
<h3>Backup Parameters</h3>
<dl>
<dt><code>pki_backup_keys, pki_backup_password</code></p>
<dd>
<dd>Set to True to back up the subsystem certificates and keys to a PKCS #12 file. This file will be located in <i>/var/lib/pki/&lt;instance_name&gt;/alias</i>. pki_backup_password is the password of the PKCS#12 file.</p>
<dt><code>Important:</code></p>
<dd>Since HSM keys are stored in the HSM (hardware), they cannot be backed up to a PKCS #12 file (software). Therefore, if <code>pki_hsm_enable</code> is set to True, <code>pki_backup_keys</code> should be set to False and <code>pki_backup_password</code> should be left unset (the default values in <code>/etc/pki/default.cfg</code>). Failure to do so will result in <code>pkispawn</code> reporting this error and exiting. </p>
</dl>
<h3>Client Directory Parameters</h3>
<dl>
<dt><code>pki_client_dir</code></p>
<dd>
<dd>This is the location where all client data used during the installation is stored. At the end of the invocation of <code>pkispawn</code>, the administrative user&#8217;s certificate and keys are stored in a PKCS #12 file in this location.</p>
<dd><code>Note:</code> When using an HSM, it is currently recommended to NOT specify a value for <code>pki_client_dir</code> that is different from the default value.</p>
<dt><code>pki_client_database_dir, pki_client_database_password</code></p>
<dd>
<dd>Location where an NSS token database is created in order to generate a key for the administrative user. Usually, the data in this location is removed at the end of the installation, as the keys and certificates are stored in a PKCS #12 file in <code>pki_client_dir</code>.</p>
<dt><code>pki_client_database_purge</code></p>
<dd>
<dd>Set to True to remove <code>pki_client_database_dir</code> at the end of the installation. Defaults to True.</dl>
<h3>Internal Database Parameters</h3>
<p><code>pki_ds_hostname, pki_ds_ldap_port, pki_ds_ldaps_port</code></p>
<dl>
<dd>Hostname and ports for the internal database. Defaults to localhost, 389, and 636, respectively.</dl>
<p> <code>pki_ds_bind_dn, pki_ds_password</code></p>
<dl>
<dd>Credentials to connect to the database during installation. Directory Manager-level access is required during installation to set up the relevant schema and database. During the installation, a more restricted Certificate Server user is set up to client authentication connections to the database. Some additional configuration is required, including setting up the directory server to use SSL. See the documentation for details.</dl>
<p> <code>pki_ds_secure_connection</code></p>
<dl>
<dd>Sets whether to require connections to the Directory Server using LDAPS. This requires SSL to be set up on the Directory Server first. Defaults to false.</dl>
<p> <code>pki_ds_secure_connection_ca_nickname</code></p>
<dl>
<dd>Once a Directory Server CA certificate has been imported into the PKI security databases (see <code>pki_ds_secure_connection_ca_pem_file</code>), <code>pki_ds_secure_connection_ca_nickname</code> will contain the nickname under which it is stored. The <code>default.cfg</code> file contains a default value for this nickname. This parameter is only utilized when <code>pki_ds_secure_connection</code> has been set to true.</dl>
<p> <code>pki_ds_secure_connection_ca_pem_file</code></p>
<dl>
<dd>The <code>pki_ds_secure_connection_ca_pem_file</code> parameter will consist of the fully-qualified path including the filename of a file which contains an exported copy of a Directory Server&#8217;s CA certificate. While this parameter is only utilized when <code>pki_ds_secure_connection</code> has been set to true, a valid value is required for this parameter whenever this condition exists.</dl>
<p> <code>pki_ds_remove_data</code></p>
<dl>
<dd>Sets whether to remove any data from the base DN before starting the installation. Defaults to True.</dl>
<p> <code>pki_ds_base_dn</code></p>
<dl>
<dd>The base DN for the internal database. It is advised that the Certificate Server have its own base DN for its internal database. If the base DN does not exist, it will be created during the running of <code>pkispawn</code>. For a cloned subsystem, the base DN for the clone subsystem MUST be the same as for the master subsystem.</dl>
<p> <code>pki_ds_database</code></p>
<dl>
<dd>Name of the back-end database. It is advised that the Certificate Server have its own base DN for its internal database. If the back-end does not exist, it will be created during the running of <code>pkispawn</code>.</dl>
<h3>Issuing Ca Parameters</h3>
<p><code>pki_issuing_ca_hostname, pki_issuing_ca_https_port, pki_issuing_ca_uri</code></p>
<dl>
<dd>Hostname and port, or URI of the issuing CA. Required for installations of subordinate CA and non-CA subsystems. This should point to the CA that will issue the relevant system certificates for the subsystem. In a default install, this defaults to the CA subsystem within the same instance. The URI has the format https://&lt;ca_hostname&gt;:&lt;ca_https_port&gt;.</dl>
<h3>Miscellaneous Parameters</h3>
<p><code>pki_restart_configured_instance</code></p>
<dl>
<dd>Sets whether to restart the instance after configuration is complete. Defaults to True.</dl>
<p> <code>pki_enable_access_log</code></p>
<dl>
<dd>Located in the [Tomcat] section, this variable determines whether the instance will enable (True) or disable (False) Tomcat access logging. Defaults to True.</dl>
<p> <code>pki_enable_java_debugger</code></p>
<dl>
<dd>Sets whether to attach a Java debugger such as Eclipse to the instance for troubleshooting. Defaults to False.</dl>
<p> <code>pki_enable_on_system_boot</code></p>
<dl>
<dd>Sets whether or not PKI instances should be started upon system boot.</p>
<dd>Currently, if this PKI subsystem exists within a shared instance, and it has been configured to start upon system boot, then ALL other previously configured PKI subsystems within this shared instance will start upon system boot.</p>
<dd>Similarly, if this PKI subsystem exists within a shared instance, and it has been configured to NOT start upon system boot, then ALL other previously configured PKI subsystems within this shared instance will NOT start upon system boot.</p>
<dd>Additionally, if more than one PKI instance exists, no granularity exists which allows one PKI instance to be enabled while another PKI instance is disabled (i.e. &#8211; PKI instances are either all enabled or all disabled). To provide this capability, the PKI instances must reside on separate machines.</p>
<dd>Defaults to True (see the following note on why this was previously &#8216;False&#8217;).</p>
<dt><code>Note:</code></p>
<dd>Since this parameter did not exist prior to Dogtag 10.2.3, the default behavior of PKI instances in Dogtag 10.2.2 and prior was False. To manually enable this behavior, obtain superuser privileges, and execute &#8216;<code>systemctl enable pki-tomcatd.target</code>&#8216;; to manually disable this behavior, execute &#8216;<code>systemctl disable pki-tomcatd.target</code>&#8216;.</dl>
<p> <code>pki_security_manager</code></p>
<dl>
<dd>Enables the Java security manager policies provided by the JDK to be used with the instance. Defaults to True.</dl>
<h3>Security Domain Parameters</h3>
<p>The security domain is a component that facilitates communication between subsystems. The first CA installed hosts this component and is used to register subsequent subsystems with the security domain. These subsystems can communicate with each other using their subsystem certificate, which is issued by the security domain CA. For more information about the security domain component, see the Red Hat Certificate System documentation at <a rel="nofollow" href="https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/.">https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/.</a></p>
<dl>
<dt><code>pki_security_domain_hostname, pki_security_domain_https_port</code></p>
<dd>
<dd>Location of the security domain. Required for KRA, OCSP, TKS, and TPS subsystems and for CA subsystems joining a security domain. Defaults to the location of the CA subsystem within the same instance.</p>
<dt><code>pki_security_domain_user, pki_security_domain_password</code></p>
<dd>
<dd>Administrative user of the security domain. Required for KRA, OCSP, TKS, and TPS subsystems, and for CA subsystems joining a security domain. Defaults to the administrative user for the CA subsystem within the same instance (caadmin).</p>
<dt><code>pki_security_domain_name</code></p>
<dd>
<dd>The name of the security domain. This is required for the security domain CA. </p>
</dl>
<h3>Clone Parameters</h3>
<dl>
<dt><code>pki_clone</code></p>
<dd>
<dd>Installs a clone, rather than original, subsystem.</p>
<dt><code>pki_clone_pkcs12_password, pki_clone_pkcs12_path</code></p>
<dd>
<dd>Location and password of the PKCS #12 file containing the system certificates for the master subsystem being cloned. This file should be readable by the user that the Certificate Server is running as (default of pkiuser), and have the correct selinux context (pki_tomcat_cert_t). This can be achieved by placing the file in <i>/var/lib/pki/&lt;instance_name&gt;/alias</i>.</p>
<dt><code>Important:</code></p>
<dd>Since HSM keys are stored in the HSM (hardware), they cannot be copied to a PKCS #12 file (software). For the case of clones using an HSM, this means that the HSM keys must be shared between the master and its clones. Therefore, if <code>pki_hsm_enable</code> is set to True, both <code>pki_clone_pkcs12_path</code> and <code>pki_clone_pkcs12_password</code> should be left unset (the default values in <code>/etc/pki/default.cfg</code>). Failure to do so will result in <code>pkispawn</code> reporting this error and exiting.</p>
<dt><code>pki_clone_setup_replication</code></p>
<dd>
<dd>Defaults to True. If set to False, the installer does not set up replication agreements from the master to the clone as part of the subsystem configuration. In this case, it is expected that the top level suffix already exists, and that the data has already been replicated. This option is useful if you want to use other tools to create and manage your replication topology, or if the baseDN is already replicated as part of a top-level suffix.</p>
<dt><code>pki_clone_reindex_data</code></p>
<dd>
<dd>Defaults to False. This parameter is only relevant when <code>pki_clone_setup_replication</code> is set to False. In this case, it is expected that the database has been prepared and replicated as noted above. Part of that preparation could involve adding indexes and indexing the data. If you would like the Dogtag installer to add the indexes and reindex the data instead, set <code>pki_clone_reindex_data</code> to True.</p>
<dt><code>pki_clone_replication_master_port, pki_clone_replication_clone_port</code></p>
<dd>
<dd>Ports on which replication occurs. These are the ports on the master and clone databases respectively. Defaults to the internal database port.</p>
<dt><code>pki_clone_replicate_schema</code></p>
<dd>
<dd>Replicate schema when the replication agreement is set up and the new instance (consumer) is initialized. Otherwise, the schema must be installed in the clone as a separate step beforehand. This does not usually have to be changed. Defaults to True.</p>
<dt><code>pki_clone_replication_security</code></p>
<dd>
<dd>The type of security used for the replication data. This can be set to SSL (using LDAPS), TLS, or None. Defaults to None. For SSL and TLS, SSL must be set up for the database instances beforehand.</p>
<dt><code>pki_master_hostname, pki_master_https_port, pki_clone_uri</code></p>
<dd>
<dd>Hostname and port, or URI of the subsystem being cloned. The URI format is https://&lt;master_hostname&gt;:&lt;master_https_port&gt; where the default master hostname and https port are set to be the security domain&#8217;s hostname and https port. </p>
</dl>
<h3>Ca Serial Number Parameters</h3>
<p><code>pki_serial_number_range_start, pki_serial_number_range_end</code></p>
<dl>
<dd>Sets the range of serial numbers to be used when issuing certificates. Values here are hexadecimal (without the 0x prefix). It is useful to override these values when migrating data from another CA, so that serial number conflicts do not occur. Defaults to 1 and 10000000 respectively.</dl>
<p> <code>pki_request_number_range_start, pki_request_number_range_end</code></p>
<dl>
<dd>Sets the range of request numbers to be used by the CA. Values here are decimal. It is useful to override these values when migrating data from another CA, so that request number conflicts do not occur. Defaults to 1 and 10000000 respectively.</dl>
<p> <code>pki_replica_number_range_start, pki_replica_number_range_end</code></p>
<dl>
<dd>Sets the range of replica numbers to be used by the CA. These numbers are used to identify database replicas in a replication topology. Values here are decimal. Defaults to 1 and 100 respectively. </p>
</dl>
<h3>External Ca Certificate Parameters</h3>
<p><code>pki_external</code></p>
<dl>
<dd>Sets whether the new CA will have a signing certificate that will be issued by an external CA. This is a two step process. In the first step, a CSR to be presented to the external CA is generated. In the second step, the issued signing certificate and certificate chain are provided to the <code>pkispawn</code> utility to complete the installation. Defaults to False.</dl>
<p> <code>pki_external_csr_path</code></p>
<dl>
<dd>Required in the first step of the external CA signing process. The CSR will be printed to the screen and stored in this location.</dl>
<p> <code>pki_external_step_two</code></p>
<dl>
<dd>Specifies that this is the second step of the external CA process. Defaults to False.</dl>
<p> <code>pki_external_ca_cert_path, pki_external_ca_cert_chain_path</code></p>
<dl>
<dd>Required for the second step of the external CA signing process. This is the location of the CA signing cert (as issued by the external CA) and the external CA&#8217;s certificate chain.</dl>
<h3>Subordinate Ca Certificate Parameters</h3>
<p><code>pki_subordinate</code></p>
<dl>
<dd>Specifies whether the new CA which will be a subordinate of another CA. The master CA is specified by <code>pki_issuing_ca</code>. Defaults to False.</p>
<dt><code>pki_subordinate_create_new_security_domain</code></p>
<dd>
<dd>Set to <code>True</code> if the subordinate CA will host its own security domain. Defaults to <code>False</code>.</p>
<dt><code>pki_subordinate_security_domain_name</code></p>
<dd>
<dd>Used when <code>pki_subordinate_create_security_domain</code> is set to <code>True</code>. Specifies the name of the security domain to be hosted on the subordinate CA. </p>
</dl>
<h3>Standalone Pki Parameters</h3>
<p>A stand-alone PKI subsystem is defined as a non-CA PKI subsystem that does not contain a CA as a part of its deployment, and functions as its own security domain. Currently, only stand-alone KRAs are supported.</p>
<dl>
<dt><code>pki_standalone</code></p>
<dd>
<dd>Sets whether or not the new PKI subsystem will be stand-alone. This is a two step process. In the first step, CSRs for each of this stand-alone PKI subsystem&#8217;s certificates will be generated so that they may be presented to the external CA. In the second step, the issued certificates, external CA certificate, and external CA certificate chain are provided to the <code>pkispawn</code> utility to complete the installation. Defaults to False.</dl>
<p> <code>pki_external_admin_csr_path</code></p>
<dl>
<dd>Will be generated by the first step of a stand-alone PKI process. This is the location of the file containing the administrator&#8217;s CSR (which will be presented to the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_admin.csr&#8217;.</dl>
<p> <code>pki_external_audit_signing_csr_path</code></p>
<dl>
<dd>Will be generated by the first step of a stand-alone PKI process. This is the location of the file containing the audit signing CSR (which will be presented to the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_audit_signing.csr&#8217;.</dl>
<p> <code>pki_external_sslserver_csr_path</code></p>
<dl>
<dd>Will be generated by the first step of a stand-alone PKI process. This is the location of the file containing the SSL server CSR (which will be presented to the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_sslserver.csr&#8217;.</dl>
<p> <code>pki_external_storage_csr_path</code></p>
<dl>
<dd>[KRA ONLY] Will be generated by the first step of a stand-alone KRA process. This is the location of the file containing the storage CSR (which will be presented to the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/kra_storage.csr&#8217;.</dl>
<p> <code>pki_external_subsystem_csr_path</code></p>
<dl>
<dd>Will be generated by the first step of a stand-alone PKI process. This is the location of the file containing the subsystem CSR (which will be presented to the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_subsystem.csr&#8217;.</dl>
<p> <code>pki_external_transport_csr_path</code></p>
<dl>
<dd>[KRA ONLY] Will be generated by the first step of a stand-alone KRA process. This is the location of the file containing the transport CSR (which will be presented to the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/kra_transport.csr&#8217;.</dl>
<p> <code>pki_external_step_two</code></p>
<dl>
<dd>Specifies that this is the second step of a standalone PKI process. Defaults to False.</dl>
<p> <code>pki_external_ca_cert_chain_path</code></p>
<dl>
<dd>Required for the second step of a stand-alone PKI process. This is the location of the file containing the external CA signing certificate (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/external_ca.cert&#8217;.</dl>
<p> <code>pki_external_ca_cert_path</code></p>
<dl>
<dd>Required for the second step of a stand-alone PKI process. This is the location of the file containing the external CA&#8217;s certificate chain (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/external_ca_chain.cert&#8217;.</dl>
<p> <code>pki_external_admin_cert_path</code></p>
<dl>
<dd>Required for the second step of a stand-alone PKI process. This is the location of the file containing the administrator&#8217;s certificate (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_admin.cert&#8217;.</dl>
<p> <code>pki_external_audit_signing_cert_path</code></p>
<dl>
<dd>Required for the second step of a stand-alone PKI process. This is the location of the file containing the audit signing certificate (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_audit_signing.cert&#8217;.</dl>
<p> <code>pki_external_sslserver_cert_path</code></p>
<dl>
<dd>Required for the second step of a stand-alone PKI process. This is the location of the file containing the sslserver certificate (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_sslserver.cert&#8217;.</dl>
<p> <code>pki_external_storage_cert_path</code></p>
<dl>
<dd>[KRA ONLY] Required for the second step of a stand-alone KRA process. This is the location of the file containing the storage certificate (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/kra_storage.cert&#8217;.</dl>
<p> <code>pki_external_subsystem_cert_path</code></p>
<dl>
<dd>Required for the second step of a stand-alone PKI process. This is the location of the file containing the subsystem certificate (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/%(pki_subsystem_type)s_subsystem.cert&#8217;.</dl>
<p> <code>pki_external_transport_cert_path</code></p>
<dl>
<dd>[KRA ONLY] Required for the second step of a stand-alone KRA process. This is the location of the file containing the transport certificate (as issued by the external CA). Defaults to &#8216;%(pki_instance_configuration_path)s/kra_transport.cert&#8217;. </p>
</dl>
<h3>Tps Parameters</h3>
<dl>
<dt><code>pki_authdb_basedn</code></p>
<dd>
<dd>Specifies the base DN of TPS authentication database.</p>
<dt><code>pki_authdb_hostname</code></p>
<dd>
<dd>Specifies the hostname of TPS authentication database. Defaults to localhost.</p>
<dt><code>pki_authdb_port</code></p>
<dd>
<dd>Specifies the port number of TPS authentication database. Defaults to 389.</p>
<dt><code>pki_authdb_secure_conn</code></p>
<dd>
<dd>Specifies whether to use a secure connection to TPS authentication database. Defaults to False.</p>
<dt><code>pki_enable_server_side_keygen</code></p>
<dd>
<dd>Specifies whether to enable server-side key generation. Defaults to False. The location of the KRA instance should be specified in the <code>pki_kra_uri</code> parameter.</p>
<dt><code>pki_ca_uri</code></p>
<dd>
<dd>Specifies the URI of the CA instance used by TPS to create and revoke user certificates. Defaults to the instance in which the TPS is running.</p>
<dt><code>pki_kra_uri</code></p>
<dd>
<dd>Specifies the URI of the KRA instance used by TPS to archive and recover keys. Required if server-side key generation is enabled using the <code>pki_enable_server_side_keygen</code> parameter. Defaults to the instance in which the TPS is running.</p>
<dt><code>pki_tks_uri</code></p>
<dd>
<dd>Specifies the URI of the TKS instance used by TPS to generate symmetric keys. Defaults to the instance in which the TPS is running. </p>
</dl>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;. <code>pkispawn</code> was written by the Dogtag project.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pkispawn/">pkispawn</a>(8)</code> </p>
