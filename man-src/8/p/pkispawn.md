---
title: "pkispawn(8)"
name: "pkispawn"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkispawn/"
description: "pkispawn – Sets up an instance of Certificate Server."
---

<p>pkispawn &#8211; Sets up an instance of Certificate Server.</p>
<h2>Synopsis</h2>
<p>pkispawn -s &lt;subsystem&gt; -f &lt;config_file&gt; [-h] [-v] [-p &lt;prefix&gt;] </p>
<h2>Description</h2>
<p>Sets up a Certificate Server subsystem (CA, KRA, OCSP, TKS, or TPS) in a Tomcat instance.</p>
<dl>
<dt><code>Note:</code></p>
<dd>A 389 Directory Server instance must be configured and running before this script can be run. Certificate Server requires an internal directory database. The default configuration assumes a Directory Server instance running on the same machine on port 389. For more information on creating a Directory Server instance, see <code><a href="/docs/linux/man/8-setup-ds-pl/">setup-ds.pl</a>(8).</code></dl>
<p> An instance can contain multiple subsystems, although it may contain at most one of each type of subsystem on a single machine. So, for example, an instance could contain CA and KRA subsystems, but not two CA subsystems. To create an instance with a CA and a KRA, simply run pkispawn twice, with values <i>-s CA </i> and <i>-s KRA </i> respectively. </p>
<p> The instances are created based on values for configuration parameters in the default configuration (/etc/pki/default.cfg) and the user-provided configuration file. The user-provided configuration file is read after the default configuration file, so any parameters defined in that file will override parameters in the default configuration file. In general, most users will store only those parameters which are different from the default configuration in their user-provided configuration file. </p>
<p> This configuration file contains parameters that are grouped into sections. These sections are stacked, so that parameters defined in earlier sections can be overwritten by parameters defined in later sections. The sections are read in the following order: [DEFAULT], [Tomcat], and the subsystem section ([CA], [KRA], [OCSP], [TKS], or [TPS]). This allows the ability to specify parameters to be shared by all subsystems in [DEFAULT] or [Tomcat], and system-specific customization. </p>
<dl>
<dt><code>Note:</code></p>
<dd>Any non-password related parameter values in the configuration file that needs to contain a <code>%</code> character must be properly escaped. For example, a value of <code>foo%bar</code> would be specified as <code>foo%%bar</code> in the configuration file.</dl>
<p> At a minimum, the user-defined configuration file must provide some passwords needed for the install. An example configuration file is provided in the <code>EXAMPLES</code> section below. For more information on the default configuration file and the parameters it contains (and can be customized), see <code><a href="/docs/linux/man/5-pki_default-cfg/">pki_default.cfg</a>(5).</code> </p>
<p> The <code>pkispawn</code> run creates several different installation files that can be referenced later, if need be:</p>
<dl>
<dd>* For Tomcat-based instances, a Tomcat instance is created at /var/lib/pki/&lt;pki_instance_name&gt;, where pki_instance_name is defined in the configuration file.</p>
<dd>* A log file of <code>pkispawn</code> operations is written to <i>/var/log/pki/pki-&lt;subsystem&gt;-spawn.&lt;timestamp&gt;.log</i>.</p>
<dd>* A .p12 (PKCS #12) file containing a certificate for a subsystem administrator is stored in pki_client_dir.</dl>
<p> When the utility is done running, the CA can be accessed by pointing a browser to https://&lt;hostname&gt;:&lt;pki_https_port&gt;/. The agent pages can be accessed by importing the CA certificate and administrator certificate into the browser. </p>
<p> The Certificate Server instance can also be accessed using the <code>pki</code> command line interface. See <code><a href="/docs/linux/man/1-pki/">pki</a>(1)</code>. For more extensive documentation on how to use Certificate Server features, see the Red Hat Certificate System Documentation at <a rel="nofollow" href="https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/.">https://access.redhat.com/knowledge/docs/Red_Hat_Certificate_System/.</a> </p>
<p> Instances created using <code>pkispawn</code> can be removed using <code>pkidestroy</code>. See <code><a href="/docs/linux/man/8-pkidestroy/">pkidestroy</a>(8).</code> </p>
<p> <code>pkispawn</code> supersedes and combines the functionality of <code>pkicreate</code> and <code>pkisilent</code>, which were available in earlier releases of Certificate Server. It is now possible to completely create and configure the Certificate Server subsystem in a single step using <code>pkispawn</code>.</p>
<dl>
<dt><code>Note:</code></p>
<dd>Previously, as an alternative to using <code>pkisilent</code> to perform a non-interactive batch configuration, a PKI instance could be interactively configured by a GUI-based configuration wizard via a Firefox browser. GUI-based configuration of a PKI instance is unavailable in this version of the product.</dl>
<h2>Options</h2>
<dl>
<dt><code>-s &lt;subsystem&gt;</code></p>
<dd>Specifies the subsystem to be installed and configured, where &lt;subsystem&gt; is CA, KRA, OCSP, TKS, or TPS.</p>
<dt><code>-f &lt;config_file&gt;</code></p>
<dd>Specifies the path to the user-defined configuration file. This file contains differences between the default configuration and the custom configuration.</p>
<dt><code>&#8211;precheck</code></p>
<dd>Execute pre-checks and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints additional help information.</p>
<dt><code>-v</code></p>
<dd>Displays verbose information about the installation. This flag can be provided multiple times to increase verbosity. See <code>pkispawn -h </code> for details. </p>
</dl>
<h2>Separate Versus Shared Instances</h2>
<dl>
<dd></dl>
<h3>Separate PKI instances:</h3>
<p>As described above, this version of Certificate System continues to support separate PKI instances for all subsystems. </p>
<p> Separate PKI instances run as a single Java-based Apache Tomcat instance, contain a single PKI subsystem (CA, KRA, OCSP, TKS, or TPS), and must utilize unique ports if co-located on the same physical machine or virtual machine (VM).</p>
<h3>Shared PKI instances:</h3>
<p>Additionally, this version of Certificate System introduces the notion of a shared PKI instance. </p>
<p> Shared PKI instances also run as a single Java-based Apache Tomcat instance, but may contain any combination of up to one of each type of PKI subsystem:</p>
<dl>
<dd>
<pre>CA
TKS
CA, KRA
CA, OCSP
TKS, TPS
CA, KRA, TKS, TPS
CA, KRA, OCSP, TKS, TPS
etc.</pre>
</dl>
<p> Shared PKI instances allow all of their subsystems contained within that instance to share the same ports, and must utilize unique ports if more than one shared PKI instance is co-located on the same physical machine or VM. </p>
<p> Semantically, a shared PKI instance that contains a single PKI subsystem is identical to a separate PKI instance.</p>
<h2>Interactive Mode</h2>
<p>If no options are specified, pkispawn will provide an interactive menu to collect the parameters needed to install the Certificate Server instance. Note that only the most basic installation options are provided. This includes root CA, KRA, OCSP, TKS, and TPS connecting to an existing directory server. More advanced setups such as cloned subsystems, subordinate or externally signed CA, subsystems that connect to the directory server using LDAPS, and subsystems that are customized beyond the options described below require the use of a configuration file with the -f option. </p>
<p> The interactive option is most useful for those users getting familiar with Certificate Server. The parameters collected are written to the installation file of the subsystem, which can be found at <code>/etc/sysconfig/pki/tomcat/&lt;instance name&gt;/&lt;subsystem&gt;/deployment.cfg.</code> </p>
<p> The following parameters are queried interactively during the installation process: </p>
<p> <code>Subsystem Type</code></p>
<dl>
<dt><i>Subsystem (CA/KRA/OCSP/TKS/TPS):</i></p>
<dd>the type of subsystem to be installed. Prompted when the -s option is not specified. The default value chosen is CA.</dl>
<p> <code>Instance Specific Parameters</code></p>
<dl>
<dt><i>Instance name:</i></p>
<dd>the name of the tomcat instance in which the subsystem is to be installed. The default value is pki-tomcat.<br />
 <code>Note:</code> Only one subsystem of a given type (CA, KRA, OCSP, TKS, TPS) can exist within a given instance.</p>
<dt><i>HTTP port:</i></p>
<dd>the HTTP port of the Tomcat instance. The default value is 8080.</p>
<dt><i>Secure HTTP port:</i></p>
<dd>the HTTPS port of the Tomcat instance. The default value is 8443.</p>
<dt><i>AJP port:</i></p>
<dd>the AJP port of the Tomcat instance. The default value is 8009.</p>
<dt><i>Management port:</i></p>
<dd>the management port of the Tomcat instance. The default value is 8005.</p>
<dt><code>Note:</code> When deploying a new subsystem into an existing instance, pkispawn will attempt to read the ports from <code>deployment.cfg</code> files stored for previously installed subsystems for this instance. If successful, the installer will not prompt for these ports.</p>
<dd></dl>
<p> <code>Administrative User Parameters</code></p>
<dl>
<dt><i>Username:</i></p>
<dd>the username of the administrator of this subsystem. The default value is &lt;ca/kra/ocsp/tks/tps&gt;admin.</p>
<dt><i>Password:</i></p>
<dd>password for the administrator user.</p>
<dt><i>Import certificate:</i></p>
<dd>An optional parameter that can be used to import an already available CA admin certificate into this instance.</p>
<dt><i>Export certificate:</i></p>
<dd>setup the path where the admin certificate of this &lt;subsystem&gt; should be stored. The default value is $HOME/.dogtag/pki-tomcat/&lt;ca/kra/ocsp/tks/tps&gt;_admin.cert.</dl>
<p> <code>Directory Server Parameters</code></p>
<dl>
<dt><i>Hostname:</i></p>
<dd>Hostname of the directory server instance. The default value is the hostname of the system.</p>
<dt><i>Use a secure LDAPS connection?</i></p>
<dd>Answering yes to this question will cause prompts for <i>Secure LDAPS Port:</i> and <i>Directory Server CA certificate pem file:</i>. Answering no to this question will cause a prompt for <i>LDAP Port</i>. The initial default value for this question is no.</p>
<dt><i>Secure LDAPS Port:</i></p>
<dd>Secure LDAPS port for the directory server instance. The default value is 636.</p>
<dt><i>Directory Server CA certificate pem file:</i></p>
<dd>The fully-qualified path including the filename of the file which contains an exported copy of the Directory Server&#8217;s CA certificate (e. g. &#8211; $HOME/dscacert.pem). This file must exist prior to <code>pkispawn</code> being able to utilize it. For details on creation of this file see the <code>EXAMPLES</code> section below entitled <code>Installing a CA connecting securely to a Directory Server via LDAPS.</code></p>
<dt><i>LDAP Port:</i></p>
<dd>LDAP port for the directory server instance. The default value is 389.</p>
<dt><i>Base DN:</i></p>
<dd>the Base DN to be used for the internal database for this subsystem. The default value is o=pki-tomcat-&lt;subsystem&gt;.</p>
<dt><i>Bind DN:</i></p>
<dd>the bind DN required to connect for the directory server. This user must have sufficient permissions to install the required schema and database. The default value is cn=Directory Manager.</p>
<dt><i>Password:</i></p>
<dd>password for the bind DN.</dl>
<p> <code>Security Domain Parameters</code></p>
<dl>
<dt><i>Name:</i></p>
<dd>the name of the security domain. Required only if installing a root CA. Default value: &lt;DNS domain name&gt; Security Domain.</p>
<dt><i>Hostname:</i></p>
<dd>the hostname for the security domain CA. Required only for non-CA subsystems. The default value is the hostname of this system.</p>
<dt><i>Secure HTTP port:</i></p>
<dd>the https port for the security domain. Required only for non-CA subsystems. The default value is 8443.</p>
<dt><i>Username:</i></p>
<dd>the username of the security domain administrator of the CA. Required only for non-CA subsystems. The default value is caadmin.</p>
<dt><i>Password:</i></p>
<dd>password for the security domain administrator. Required for all subsystems that are not root CAs. </p>
</dl>
<h2>Pre-Check Mode</h2>
<p>This option is only available when pkispawn is invoked in a non-interactive mode. When the <code>&#8211;precheck</code> option is provided, a set of basic tests are performed to ensure that the parameters provided to pkispawn are valid and consistent. </p>
<p> pkispawn will then exit with an exit code of 0 on success, or 1 on failure. This mode can be used to perform basic tests prior to doing any actual installation of the Certificate Server instance. </p>
<p> Flags are available to disable specific tests. For instance, one might want to disable validation of the credentials for the internal database user if the directory server instance has not yet been created. </p>
<p> See <code> <a href="/docs/linux/man/5-pki_default-cfg/">pki_default.cfg</a>(5) </code> for more details about available flags.</p>
<h2>Examples</h2>
<h3>Installing a root CA</h3>
<p>To install a root CA in a new instance execute the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code>  where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i></pre>
<p> Prior to running this command, a Directory Server instance should be created and running. This command assumes that the Directory Server instance is using its default configuration:</p>
<dl>
<dd>* Installed on the local machine</p>
<dd>* Listening on port 389</p>
<dd>* The user is cn=Directory Manager, with the password specified in pki_ds_password  This invocation of <code>pkispawn</code> creates a Tomcat instance containing a CA running on the local machine with secure port 8443 and unsecure port 8080. To access this CA, simply point a browser to https://&lt;hostname&gt;:8443. The instance name (defined by pki_instance_name) is pki-tomcat, and it is located at <i>/var/lib/pki/pki-tomcat</i>. Logs for the instance are located at <i>/var/log/pki/pki-tomcat</i>, and an installation log is written to <i>/var/log/pki/pki-&lt;subsystem&gt;-spawn.&lt;timestamp&gt;.log</i>. A PKCS #12 file containing the administrator certificate is created in <i>$HOME/.dogtag/pki-tomcat</i>. This PKCS #12 file uses the password designated by pki_client_pkcs12_password in the configuration file. To access the agent pages, first import the CA certificate by accessing the CA End Entity Pages and clicking on the Retrieval Tab. Be sure to trust the CA certificate. Then, import the administrator certificate in the PKCS #12 file.</p>
<h3>Installing a root CA using ECC</h3>
<p>To install a root CA in a new instance using ECC execute the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code>  where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_admin_keysize=nistp256
pki_admin_key_type=ecc
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_ssl_server_key_algorithm=SHA256withEC
pki_ssl_server_key_size=nistp256
pki_ssl_server_key_type=ecc
pki_subsystem_key_algorithm=SHA256withEC
pki_subsystem_key_size=nistp256
pki_subsystem_key_type=ecc
[CA]
pki_ca_signing_key_algorithm=SHA256withEC
pki_ca_signing_key_size=nistp256
pki_ca_signing_key_type=ecc
pki_ca_signing_signing_algorithm=SHA256withEC
pki_ocsp_signing_key_algorithm=SHA256withEC
pki_ocsp_signing_key_size=nistp256
pki_ocsp_signing_key_type=ecc
pki_ocsp_signing_signing_algorithm=SHA256withEC</pre>
<p> In order to utilize ECC, the SSL Server and Subsystem key algorithm, key size, and key type should be changed from SHA256withRSA &#8211;&gt; SHA256withEC, 2048 &#8211;&gt; nistp256, and rsa &#8211;&gt; ecc, respectively. To use an ECC admin key size and key type, the values should also be changed from 2048 &#8211;&gt; nistp256, and rsa &#8211;&gt; ecc. Additionally, for a CA subsystem, both the CA and OCSP Signing key algorithm, key size, key type, and signing algorithm should be changed from SHA256withRSA &#8211;&gt; SHA256withEC, 2048 &#8211;&gt; nistp256, rsa &#8211;&gt; ecc, and SHA256withRSA &#8211;&gt; SHA256withEC,respectively.</p>
<dl>
<dt><code>Note:</code></p>
<dd>For all PKI subsystems including the CA, ECC is not supported for the corresponding Audit Signing parameters. Similarly, for KRA subsystems, ECC is not supported for either of the corresponding Storage or Transport parameters.</dl>
<h3>Installing a KRA, OCSP, TKS, or TPS in a shared instance</h3>
<p>For this example, assume that a new CA instance has been installed by executing the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code></dl>
<p> where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
# Optionally keep client databases
pki_client_database_purge=False
the following command:
<dl><dt><dd><code>pkispawn -s KRA -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
the following command:
<dl><dt><dd><code>pkispawn -s OCSP -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
the following command:
<dl><dt><dd><code>pkispawn -s TKS -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
the following command:
<dl><dt><dd><code>pkispawn -s TPS -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
[TPS]
# Shared TPS instances optionally utilize their shared KRA
# for server-side keygen
pki_enable_server_side_keygen=True
pki_authdb_basedn=<i>dc=example,dc=com</i>
For this particular example, the computed default values for a
PKI instance name including its ports, URLs, machine names, etc.
were utilized as defined in <i>/etc/pki/default.cfg</i>. Each
subsystem in this example will reside under the
<i>/var/lib/pki/pki-tomcat</i> instance housed within their own
<i>ca</i>, <i>kra</i>, <i>ocsp</i>, <i>tks</i>, and <i>tps</i>
subdirectories, utilizing the same default port values of
8080 (http), 8443 (https), 8009 (ajp), 8005 (tomcat), using the
same computed hostname and URL information, and sharing a single
common PKI Administrator Certificate.
</dl>
The <code>pki_security_domain_password</code> is the admin password of the
CA installed in the same instance. This command should be run after
a CA is installed. This installs another subsystem within the same
instance using the certificate generated for the CA administrator
for the subsystem's administrator. This allows a user to access
both subsystems on the browser with a single administrator
certificate. To access the new subsystem's functionality, simply
point the browser to https://&lt;hostname&gt;:8443 and click the
relevant top-level links.
To install TPS in a shared instance the following section must be
added to <i>myconfig.txt</i>:
<dl><dt><dd>[TPS]
pki_authdb_basedn=<i>dc=example,dc=com</i></pre>
<p> TPS requires an authentication database. The <code>pki_authdb_basedn</code> specifies the base DN of the authentication database. TPS also requires that a CA and a TKS subsystems are already installed in the same instance. Since they are in the same instance, a shared secret key will automatically be generated in TKS and imported into TPS. Optionally, server-side key generation can be enabled in TPS by adding the following parameter in [TPS]:</p>
<dl>
<dd>
<pre>pki_enable_server_side_keygen=<i>True</i></pre>
<p> Enabling server-side key generation requires that a KRA subsystem is already installed in the same instance.</p>
<h3>Installing a KRA, OCSP, TKS, or TPS in a separate instance</h3>
<p>For this example, assume that a new CA instance has been installed by executing the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code></dl>
<p> where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
# Optionally keep client databases
pki_client_database_purge=False
# Separated CA instance name and ports
pki_instance_name=<i>pki-ca</i>
pki_http_port=<i>18080</i>
pki_https_port=<i>18443</i>
# This Separated CA instance will be its own security domain
pki_security_domain_https_port=<i>18443</i>
[Tomcat]
# Separated CA Tomcat ports
pki_ajp_port=<i>18009</i>
pki_tomcat_server_port=<i>18005</i>
the following command:
<dl><dt><dd><code>pkispawn -s KRA -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Optionally keep client databases
pki_client_database_purge=False
# Separated KRA instance name and ports
pki_instance_name=<i>pki-kra</i>
pki_http_port=<i>28080</i>
pki_https_port=<i>28443</i>
# Separated KRA instance security domain references
pki_issuing_ca=<i><a rel="nofollow" href="https://pki.example.com:18443">https://pki.example.com:18443</a></i>
pki_security_domain_hostname=<i>pki.example.com</i>
pki_security_domain_https_port=<i>18443</i>
pki_security_domain_user=caadmin
[Tomcat]
# Separated KRA Tomcat ports
pki_ajp_port=<i>28009</i>
pki_tomcat_server_port=<i>28005</i>
[KRA]
# A Separated KRA instance requires its own
# PKI Administrator Certificate
pki_import_admin_cert=False
the following command:
<dl><dt><dd><code>pkispawn -s OCSP -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Optionally keep client databases
pki_client_database_purge=False
# Separated OCSP instance name and ports
pki_instance_name=<i>pki-ocsp</i>
pki_http_port=<i>29080</i>
pki_https_port=<i>29443</i>
# Separated OCSP instance security domain references
pki_issuing_ca=<i><a rel="nofollow" href="https://pki.example.com:18443">https://pki.example.com:18443</a></i>
pki_security_domain_hostname=<i>pki.example.com</i>
pki_security_domain_https_port=<i>18443</i>
pki_security_domain_user=caadmin
[Tomcat]
# Separated OCSP Tomcat ports
pki_ajp_port=<i>29009</i>
pki_tomcat_server_port=<i>29005</i>
[OCSP]
# A Separated OCSP instance requires its own
# PKI Administrator Certificate
pki_import_admin_cert=False
the following command:
<dl><dt><dd><code>pkispawn -s TKS -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Optionally keep client databases
pki_client_database_purge=False
# Separated TKS instance name and ports
pki_instance_name=<i>pki-tks</i>
pki_http_port=<i>30080</i>
pki_https_port=<i>30443</i>
# Separated TKS instance security domain references
pki_issuing_ca=<i><a rel="nofollow" href="https://pki.example.com:18443">https://pki.example.com:18443</a></i>
pki_security_domain_hostname=<i>pki.example.com</i>
pki_security_domain_https_port=<i>18443</i>
pki_security_domain_user=caadmin
[Tomcat]
# Separated TKS Tomcat ports
pki_ajp_port=<i>30009</i>
pki_tomcat_server_port=<i>30005</i>
[TKS]
# A Separated TKS instance requires its own
# PKI Administrator Certificate
pki_import_admin_cert=False
the following command:
<dl><dt><dd><code>pkispawn -s TPS -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Optionally keep client databases
pki_client_database_purge=False
# Separated TPS instance name and ports
pki_instance_name=<i>pki-tps</i>
pki_http_port=<i>31080</i>
pki_https_port=<i>31443</i>
# Separated TPS instance security domain references
pki_issuing_ca=<i><a rel="nofollow" href="https://pki.example.com:18443">https://pki.example.com:18443</a></i>
pki_security_domain_hostname=<i>pki.example.com</i>
pki_security_domain_https_port=<i>18443</i>
pki_security_domain_user=caadmin
[Tomcat]
# Separated TPS Tomcat ports
pki_ajp_port=<i>31009</i>
pki_tomcat_server_port=<i>31005</i>
[TPS]
# Separated TPS instances require specifying a remote CA
pki_ca_uri=<i><a rel="nofollow" href="https://pki.example.com:18443">https://pki.example.com:18443</a></i>
# Separated TPS instances optionally utilize a remote KRA
# for server-side keygen
pki_kra_uri=<i><a rel="nofollow" href="https://pki.example.com:28443">https://pki.example.com:28443</a></i>
pki_enable_server_side_keygen=True
pki_authdb_basedn=<i>dc=example,dc=com</i>
# Separated TPS instances require specifying a remote TKS
pki_tks_uri=<i><a rel="nofollow" href="https://pki.example.com:30443">https://pki.example.com:30443</a></i>
pki_import_shared_secret=True
# A Separated TPS instance requires its own
# PKI Administrator Certificate
pki_import_admin_cert=False
For this particular example, besides passwords, sample
values were also utilized for PKI instance names, ports,
URLs, machine names, etc. Under no circumstances should
these demonstrative values be construed to be required
literal values.
</dl>
A remote CA is one where the CA resides in another
Certificate Server instance, either on the local machine
or a remote machine. In this case, <i>myconfig.txt</i> must
specify the connection information for the remote CA and the
information about the security domain (the trusted collection
of subsystems within an instance).
The subsystem section is [KRA], [OCSP], [TKS], or [TPS].
This example assumes that the specified CA hosts the security
domain. The CA must be running and accessible.
A new administrator certificate is generated for the new
subsystem and stored in a PKCS #12 file
in <i>$HOME/.dogtag/&lt;pki_instance_name&gt;</i>.
As in a shared instance, to install TPS in a separate instance
the authentication database must be specified in the [TPS] section,
and optionally the server-side key generation can be enabled.
If the CA, KRA, or TKS subsystems required by TPS are running
on a remote instance the following parameters must be added into
the [TPS] section to specify their locations:
<dl><dt><dd>pki_ca_uri=<i>https://&lt;ca_hostname&gt;:&lt;ca_https_port&gt;</i>
pki_kra_uri=<i>https://&lt;kra_hostname&gt;:&lt;kra_https_port&gt;</i>
pki_tks_uri=<i>https://&lt;tks_hostname&gt;:&lt;tks_https_port&gt;</i></pre>
<p> If TPS and TKS are installed on separate instances the shared secret key should be imported over the wire between the TKS and TPS automatically. If the automated procedure fails for any unlikely reason the following manual procedure will serve as a fallback. The key needs to be created on the TKS side and imported into the TPS side in this case. Generate the shared secret key (if needed) in TKS with the following command:</p>
<dl>
<dd>tkstool -T -d /var/lib/pki/pki-tomcat/alias -n sharedSecret  Verify the shared secret key in TKS with the following command:</p>
<dl>
<dd>tkstool -L -d /var/lib/pki/pki-tomcat/alias  Once TPS is installed, shutdown TPS instance, then import the shared secret key into TPS with the following command:</p>
<dl>
<dd>tkstool -I -d /var/lib/pki/pki-tomcat/alias -n sharedSecret  Verify the shared secret key in TPS with the following command:</p>
<dl>
<dd>tkstool -L -d /var/lib/pki/pki-tomcat/alias  The shared secret key nickname should be stored in the following property in the TPS&#8217;s CS.cfg:</p>
<dl>
<dd>conn.tks1.tksSharedSymKeyName=sharedSecret  Finally, restart the TPS instance.</p>
<h3>Installing a CA, KRA, OCSP, TKS, or TPS using a Hardware Security Module (HSM)</h3>
<p>This section provides sample <code>myconfig.txt</code> files when an HSM is being utilized in a shared PKI instance. For this example, assume that a new CA instance has been installed by executing the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code></dl>
<p> where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
# Optionally keep client databases
pki_client_database_purge=False
# Provide HSM parameters
pki_hsm_enable=True
pki_hsm_libfile=&lt;hsm_libfile&gt;
pki_hsm_modulename=&lt;hsm_modulename&gt;
pki_token_name=&lt;hsm_token_name&gt;
pki_token_password=&lt;pki_token_password&gt;
# Provide PKI-specific HSM token names
pki_audit_signing_token=&lt;hsm_token_name&gt;
pki_ssl_server_token=&lt;hsm_token_name&gt;
pki_subsystem_token=&lt;hsm_token_name&gt;
[CA]
# Provide CA-specific HSM token names
pki_ca_signing_token=&lt;hsm_token_name&gt;
pki_ocsp_signing_token=&lt;hsm_token_name&gt;
the following command:
<dl><dt><dd><code>pkispawn -s KRA -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Provide HSM parameters
pki_hsm_enable=True
pki_hsm_libfile=&lt;hsm_libfile&gt;
pki_hsm_modulename=&lt;hsm_modulename&gt;
pki_token_name=&lt;hsm_token_name&gt;
pki_token_password=&lt;pki_token_password&gt;
# Provide PKI-specific HSM token names
pki_audit_signing_token=&lt;hsm_token_name&gt;
pki_ssl_server_token=&lt;hsm_token_name&gt;
pki_subsystem_token=&lt;hsm_token_name&gt;
[KRA]
# Provide KRA-specific HSM token names
pki_storage_token=&lt;hsm_token_name&gt;
pki_transport_token=&lt;hsm_token_name&gt;
the following command:
<dl><dt><dd><code>pkispawn -s OCSP -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Provide HSM parameters
pki_hsm_enable=True
pki_hsm_libfile=&lt;hsm_libfile&gt;
pki_hsm_modulename=&lt;hsm_modulename&gt;
pki_token_name=&lt;hsm_token_name&gt;
pki_token_password=&lt;pki_token_password&gt;
# Provide PKI-specific HSM token names
pki_audit_signing_token=&lt;hsm_token_name&gt;
pki_ssl_server_token=&lt;hsm_token_name&gt;
pki_subsystem_token=&lt;hsm_token_name&gt;
[OCSP]
# Provide OCSP-specific HSM token names
pki_ocsp_signing_token=&lt;hsm_token_name&gt;
the following command:
<dl><dt><dd><code>pkispawn -s TKS -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Provide HSM parameters
pki_hsm_enable=True
pki_hsm_libfile=&lt;hsm_libfile&gt;
pki_hsm_modulename=&lt;hsm_modulename&gt;
pki_token_name=&lt;hsm_token_name&gt;
pki_token_password=&lt;pki_token_password&gt;
# Provide PKI-specific HSM token names
pki_audit_signing_token=&lt;hsm_token_name&gt;
pki_ssl_server_token=&lt;hsm_token_name&gt;
pki_subsystem_token=&lt;hsm_token_name&gt;
the following command:
<dl><dt><dd><code>pkispawn -s TPS -f myconfig.txt</code>
</dl>
where <i>myconfig.txt</i> contains the following text:
<dl><dt><dd>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
# Provide HSM parameters
pki_hsm_enable=True
pki_hsm_libfile=&lt;hsm_libfile&gt;
pki_hsm_modulename=&lt;hsm_modulename&gt;
pki_token_name=&lt;hsm_token_name&gt;
pki_token_password=&lt;pki_token_password&gt;
# Provide PKI-specific HSM token names
pki_audit_signing_token=&lt;hsm_token_name&gt;
pki_ssl_server_token=&lt;hsm_token_name&gt;
pki_subsystem_token=&lt;hsm_token_name&gt;
[TPS]
# Shared TPS instances optionally utilize their shared KRA
# for server-side keygen
pki_enable_server_side_keygen=True
pki_authdb_basedn=<i>dc=example,dc=com</i>
Since HSM keys are stored in the HSM (hardware), they cannot be
backed up, moved, or copied to a PKCS #12 file (software).
For example, if <code>pki_hsm_enable</code> is set to True,
<code>pki_backup_keys</code> should be set to False and
<code>pki_backup_password</code> should be left unset (the default
values in <code>/etc/pki/default.cfg</code>). Similarly, for the case
of clones using an HSM, this means that the HSM keys must be
shared between the master and its clones. Therefore, if
<code>pki_hsm_enable</code> is set to True, both
<code>pki_clone_pkcs12_path</code> and <code>pki_clone_pkcs12_password</code>
should be left unset (the default values in
<code>/etc/pki/default.cfg</code>). Failure to comply with these rules
will result in <code>pkispawn</code> reporting an appropriate error and
exiting.
</dl></pre>
<h3>Installing a CA clone</h3>
<p>To install a CA clone execute the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code>  where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
pki_security_domain_hostname=&lt;master_ca_hostname&gt;
pki_security_domain_https_port=&lt;master_ca_https_port&gt;
pki_security_domain_user=caadmin
[Tomcat]
pki_clone=True
pki_clone_pkcs12_password=<i>Secret123</i>
pki_clone_pkcs12_path=&lt;path_to_pkcs12_file&gt;
pki_clone_replicate_schema=True
pki_clone_uri=https://&lt;master_ca_hostname&gt;:&lt;master_ca_https_port&gt;</pre>
<p> A cloned CA is a CA which uses the same signing, OCSP signing, and audit signing certificates as the master CA, but issues certificates within a different serial number range. It has its own internal database &#8212; separate from the master CA database &#8212; but using the same base DN, that keeps in sync with the master CA through replication agreements between the databases. This is very useful for load sharing and disaster recovery. To create a clone, the <i>myconfig.txt</i> uses pki_clone-* parameters in its [Tomcat] section which identify the original CA to use as a master template. Additionally, it connects to the master CA as a remote CA and uses its security domain. Before the clone can be generated, the Directory Server must be created that is separate from the master CA&#8217;s Directory Server. The example assumes that the master CA and cloned CA are on different machines, and that their Directory Servers are on port 389. In addition, since this example does not utilize an HSM, the master&#8217;s system certs and keys have been stored in a PKCS #12 file that is copied over to the clone subsystem in the location specified in &lt;path_to_pkcs12_file&gt;. This file needs to be readable by the user the Certificate Server runs as (by default, pkiuser) and be given the SELinux context pki_tomcat_cert_t. The master&#8217;s system certificates can be exported to a PKCS#12 file when the master is installed if the parameter <code>pki_backup_keys</code> is set to <code>True</code> and the <code>pki_backup_password</code> is set. The PKCS#12 file is then found under <code>/var/lib/pki/&lt;instance_name&gt;/alias</code>. Alternatively, the PKCS#12 file can be generated at any time post-installation using <code>PKCS12Export</code>. An example invocation showing the export of the system certificates and keys, copying the keys to the replica subsystem, and setting the relevant SELinux and file permissions is shown below. <code>pwfile</code> is a text file containing the password for the master NSS DB (found in <code>/etc/pki/&lt;instance_name&gt;/password.conf</code>). <code> pkcs12_password_file</code> is a text file containing the password selected for the generated PKCS12 file.</p>
<dl>
<dd>
<pre><code>master# PKCS12Export -d /etc/pki/pki-tomcat/alias -p pwfile \
 -w pkcs12_password_file -o backup_keys.p12
master# scp backup_keys.p12 clone:/backup_keys.p12
clone# chown pkiuser: /backup_keys.p12
clone# semanage -a -t pki_tomcat_cert_t /backup_keys.p12</code></pre>
<p> <code>Note:</code> From Dogtag 10.3, a slightly different mechanism has been provided to create and specify the required PKCS#12 file to the clone subsystem. This new method is provided in addition to the method above, but will become the preferred method in future releases. This method can be used if both master and clone are 10.3 or above. To export the required keys from the master, use the <code>pki-server</code> command line tool.</p>
<dl>
<dd>
<pre><code>master# pki-server ca-clone-prepare -i pki-tomcat \
 --pkcs12-file backup_keys.p12 \
 --pkcs12-password Secret123
master# scp backup_keys.p12 clone:/backup_keys.p12
master# scp /etc/pki/pki-tomcat/external_certs.conf \
 clone:/external_certs.conf
</code></pre>
<p> The <code>external_certs.conf</code> file contains information about third party certificates that were added to the master&#8217;s certificate database using the <code>pki-server</code> command. The certificates themselves are stored in the backup_keys.p12 file. If there are no third-party certifcates that have been added, then the <code>external_certs.conf</code> file may not exist and should be ignored. The two files (<code>backup_keys.p12</code> and <code>external_certs.conf</code>) are specified to pkispawn as below.</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
pki_security_domain_hostname=&lt;master_ca_hostname&gt;
pki_security_domain_https_port=&lt;master_ca_https_port&gt;
pki_security_domain_user=caadmin
[Tomcat]
pki_server_pkcs12_path=&lt;path to pkcs12 file&gt;
pki_server_pkcs12_password=<i>Secret123</i>
pki_server_external_certs_path=&lt;path to external_certs.conf file&gt;
pki_clone=True
pki_clone_replicate_schema=True
pki_clone_uri=https://&lt;master_ca_hostname&gt;:&lt;master_ca_https_port&gt;</pre>
<p> Note that the previous p12 parameters (pki_clone_pkcs12_*) are no longer needed, and will be ignored. </p>
<pre>Note: One current cloning anomaly to mention is the following scenario:
1. Create a clone of a CA or of any other subsystem.
2. Remove that just created clone.
3. Immediately attempt the exact same clone again, in place of
 the recently destroyed instance. Before recreating this clone,
 make sure the &quot;pki_ds_remove_data=True&quot; is used in the clone's
 deployment config file. This will remove the old data from the previous
 clone.
Here the Director Server instance may have worked itself in into a state
where it no longer accepts connections, aborting the clone configuration quickly.
The fix to this is to simply restart the Directory Server instance before
creating the clone for the second time. After restarting the Directory Server
it should be possible to create the mentioned clone instance.</pre>
<h3>Installing a KRA or TKS clone</h3>
<p>To install a KRA or TKS (OCSP and TPS unsupported as of now) execute the following command:</p>
<dl>
<dd><code>pkispawn -s &lt;subsystem&gt; -f myconfig.txt</code>  where subsystem is KRA or TKS and <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
pki_security_domain_hostname=&lt;master_ca_hostname&gt;
pki_security_domain_https_port=&lt;master_ca_https_port&gt;
pki_security_domain_user=caadmin
[Tomcat]
pki_clone=True
pki_clone_pkcs12_password=<i>Secret123</i>
pki_clone_pkcs12_path=&lt;path_to_pkcs12_file&gt;
pki_clone_replicate_schema=True
pki_clone_uri=https://&lt;master_subsystem_host&gt;:&lt;master_subsystem_https_port&gt;
pki_issuing_ca=https://&lt;ca_hostname&gt;:&lt;ca_https_port&gt;</pre>
<p> As with a CA clone, a KRA or TKS clone uses the same certificates and basic configuration as the original subsystem. The configuration points to the original subsystem to copy its configuration. This example also assumes that the CA is on a remote machine and specifies the CA and security domain information. The parameter <code>pki_clone_uri</code> should be modified to point to the required master (KRA or TKS). As of 10.3, a slightly different mechanism has been introduced to generate and specify the PKCS#12 file and any third-party certificates. See the <code>Installing a CA clone</code> section for details.</p>
<h3>Installing a CA clone on the same host</h3>
<p>For testing purposes, it is useful to configure cloned CAs which exist (with their internal databases) on the same host as the master CA. To configure the cloned CA execute the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code>  where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=Secret123
pki_client_database_password=Secret123
pki_client_pkcs12_password=Secret123
pki_ds_password=Secret123
pki_ds_ldap_port=&lt;unique port different from master&gt;
pki_ds_ldaps_port=&lt;unique port different from master&gt;
pki_http_port=&lt;unique port different from master&gt;
pki_https_port=&lt;unique port different from master&gt;
pki_instance_name=&lt;unique name different from master&gt;
pki_security_domain_hostname=&lt;master_ca_hostname&gt;
pki_security_domain_https_port=&lt;master_ca_https_port&gt;
pki_security_domain_password=Secret123
[Tomcat]
pki_ajp_port=&lt;unique port different from master&gt;
pki_clone=True
pki_clone_pkcs12_password=Secret123
pki_clone_pkcs12_path=&lt;path_to_pkcs12_file&gt;
pki_clone_uri=https://&lt;master_ca_hostname&gt;:&lt;master_ca_https_port&gt;
pki_tomcat_server_port=&lt;unique port different from master&gt;
[CA]
pki_ds_base_dn=&lt;identical value as master&gt;
pki_ds_database=&lt;identical value as master&gt;</pre>
<p> In this case, because both CA Tomcat instances are on the same host, they must have distinct ports. Similarly, each CA must use a distinct directory server instance for its internal database. Like the Tomcat instances, these are distinguished by distinct ports. The suffix being replicated (<code>pki_ds_base</code>), however, must be the same for both master and clone.</p>
<h3>Installing a subordinate CA in existing security domain</h3>
<p>To install a subordinate CA in an existing security domain execute the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code>  where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
pki_security_domain_hostname=&lt;security_domain_ca_hostname&gt;
pki_security_domain_https_port=&lt;security_domain_ca_https_port&gt;
pki_security_domain_user=caadmin
[CA]
pki_subordinate=True
pki_issuing_ca=https://&lt;master_ca_hostname&gt;:&lt;master_ca_https_port&gt;
pki_ca_signing_subject_dn=cn=CA Subordinate Signing,o=example.com</pre>
<p> A sub-CA derives its certificate configuration &#8212; such as allowed extensions and validity periods &#8212; from a superior or root CA. Otherwise, the configuration of the CA is independent of the root CA, so it is its own instance rather than a clone. A sub-CA is configured using the pki_subordinate parameter and a pointer to the CA which issues the sub-CA&#8217;s certificates. <code>Note:</code> The value of <code>pki_ca_signing_subject_dn</code> of a subordinate CA should be different from the root CA&#8217;s signing subject DN.</p>
<h3>Installing a subordinate CA in new security domain</h3>
<p>To install a subordinate CA in a new security domain execute the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code>  where <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
pki_security_domain_hostname=&lt;master CA security domain hostname&gt;
pki_security_domain_https_port=&lt;master CA security domain https port&gt;
pki_security_domain_user=caadmin
[CA]
pki_subordinate=True
pki_issuing_ca=https://&lt;master_ca_hostname&gt;:&lt;master_ca_https_port&gt;
pki_ca_signing_subject_dn=<i>cn=CA Subordinate Signing,o=example.com</i>
pki_subordinate_create_new_security_domain=True
pki_subordinate_security_domain_name=<i>Subordinate CA Security Domain</i></pre>
<p> In this section, the subordinate CA logs onto and registers with the security domain CA (using parameters <code>pki_security_domain_hostname</code>, <code>pki_security_domain_user</code> and <code>pki_security_domain_password</code>) as in the previous section, but also creates and hosts a new security domain. To do this, <code>pki_subordinate_create_new_security_domain</code> must be set to <code>True</code>. The subordinate CA security domain name can also be specified by specifying a value for <code>pki_subordinate_security_domain_name</code>. <code>Note:</code> The value of <code>pki_ca_signing_subject_dn</code> of a subordinate CA should be different from the root CA&#8217;s signing subject DN.</p>
<h3>Installing an externally signed CA</h3>
<p>To install an externally signed CA execute the following command:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code>  This is a two step process. In the first step, a certificate signing request (CSR) is generated for the signing certificate and <i>myconfig.txt</i> contains the following text:</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
[CA]
pki_external=True
pki_external_csr_path=<i>/tmp/ca_signing.csr</i>
pki_ca_signing_subject_dn=<i>cn=CA Signing,ou=External,o=example.com</i></pre>
<p> The CSR is written to pki_external_csr_path. The pki_ca_signing_subject_dn should be different from the subject DN of the external CA that is signing the request. The pki_ca_signing_subject_dn parameter can be used to specify the signing certificate&#8217;s subject DN. The CSR is then submitted to the external CA, and the resulting certificate and certificate chain are saved to files on the system. In the second step, the configuration file has been modified to install the issued certificates. In place of the original CSR, the configuration file now points to the issued CA certificate and certificate chain. There is also a flag to indicate that this completes the installation process (pki_external_step_two).</p>
<dl>
<dd>
<pre>[DEFAULT]
pki_admin_password=<i>Secret123</i>
pki_client_database_password=<i>Secret123</i>
pki_client_pkcs12_password=<i>Secret123</i>
pki_ds_password=<i>Secret123</i>
pki_security_domain_password=<i>Secret123</i>
[CA]
pki_external=True
pki_external_ca_cert_chain_path=<i>/tmp/ca_cert_chain.cert</i>
pki_external_ca_cert_path=<i>/tmp/ca_signing.cert</i>
pki_external_step_two=True
pki_ca_signing_subject_dn=<i>cn=CA Signing Certificate,ou=External,o=example.com</i></pre>
<p> Then, the <code>pkispawn</code> command is run again:</p>
<dl>
<dd><code>pkispawn -s CA -f myconfig.txt</code></dl>
<h3>Installing a PKI subsystem with a secure LDAP connection</h3>
<p>There are three scenarios in which a PKI subsystem (e.g. a CA) needs to communicate securely via LDAPS with a directory server:</p>
<dl>
<dd>* A directory server exists which is already running LDAPS using a CA certificate that has been issued by some other CA. For this scenario, the CA certificate must be made available via a PEM file (e.g. $HOME/dscacert.pem) prior to running <code>pkispawn</code> such that the new CA may be installed and configured to communicate with this directory server using LDAPS.</p>
<dd>* A directory server exists which is currently running LDAP. Once a CA has been created, there is a desire to use its CA certificate to issue an SSL certificate for this directory server so that this CA and this directory server can communicate via LDAPS. For this scenario, since there is no need to communicate securely during the <code>pkispawn</code> installation/configuration, simply use <code>pkispawn</code> to install and configure the CA using the LDAP port of the directory server, issue an SSL certificate from this CA for the directory server, and then reconfigure the CA and directory server to communicate with each other via LDAPS.</p>
<dd>* Similar to the previous scenario, a directory server exists which is currently running LDAP, and the desire is to create a CA and use it to establish LDAPS communications between this CA and this directory server. However, for this scenario, there is a need for the CA and the directory server to communicate securely during <code>pkispawn</code> installation and configuration. For this to succeed, the directory server must generate a temporary self-signed certificate which then must be made available via a PEM file (e.g. $HOME/dscacert.pem) prior to running <code>pkispawn</code>. Once the CA has been created, swap things out to reconfigure the CA and directory server to utilize LDAPS through the desired certificates.  The following example demonstrates the steps to generate a temporary self-signed certificate in the Directory Server which requires an Admin Server. Directory Server and Admin Server instances can be created with the following command:</p>
<dl>
<dd><code>setup-ds-admin.pl</code>  Enable LDAPS in the Directory Server with the following command:</p>
<dl>
<dd><code>/usr/sbin/setupssl2.sh /etc/dirsrv/</code><i>slapd-pki</i> 389 636 <i>Secret123</i>  <code>Note:</code> The <code>setupssl2.sh</code> script may be downloaded from <code><a rel="nofollow" href="https://raw.githubusercontent.com/richm/scripts/master/setupssl2.sh">https://raw.githubusercontent.com/richm/scripts/master/setupssl2.sh</a></code>. Restart the Directory Server with the following command:</p>
<dl>
<dd><code>systemctl restart dirsrv.target</code>  Verify that a client can connect securely over LDAPS with the following command:  <code>Note:</code> The <code>mozldap ldapsearch</code> utility is available from the <code>mozldap-tools</code> package. Export the self-signed CA certificate with the following command:</p>
<dl>
<dd><code>certutil -L -d /etc/dirsrv/</code><i>slapd-pki</i> -n &quot;CA certificate&quot; -a &gt; <i>$HOME/dscacert.pem</i>  Once the self-signed CA certificate is obtained, add the following parameters into the [DEFAULT] section in <i>myconfig.txt</i>:</p>
<dl>
<dd>
<pre>pki_ds_secure_connection=True
pki_ds_secure_connection_ca_pem_file=<i>$HOME/dscacert.pem</i></pre>
<p> Then execute <code>pkispawn</code> to create the CA subsystem.</p>
<h3>Managing PKI instance</h3>
<p>To start all 389 instances (local PKI databases):</p>
<dl>
<dd>
<pre><code>systemctl start dirsrv.target</code></pre>
</dl>
<p> To stop all 389 instances (local PKI databases):</p>
<dl>
<dd>
<pre><code>systemctl stop dirsrv.target</code></pre>
</dl>
<p> To restart all 389 instances (local PKI databases):</p>
<dl>
<dd>
<pre><code>systemctl restart dirsrv.target</code></pre>
</dl>
<p> To obtain the status of all 389 instances (local PKI databases):</p>
<dl>
<dd>
<pre><code>systemctl status dirsrv.target</code></pre>
</dl>
<p> To start a PKI instance named &lt;pki_instance_name&gt;:</p>
<dl>
<dd>
<pre><code>systemctl start pki-tomcatd@&lt;pki_instance_name&gt;.service</code></pre>
</dl>
<p> To stop a PKI instance named &lt;pki_instance_name&gt;:</p>
<dl>
<dd>
<pre><code>systemctl stop pki-tomcatd@&lt;pki_instance_name&gt;.service</code></pre>
</dl>
<p> To restart a PKI instance named &lt;pki_instance_name&gt;:</p>
<dl>
<dd>
<pre><code>systemctl restart pki-tomcatd@&lt;pki_instance_name&gt;.service</code></pre>
</dl>
<p> To obtain the status of a PKI instance named &lt;pki_instance_name&gt;:</p>
<dl>
<dd>
<pre><code>systemctl status pki-tomcatd@&lt;pki_instance_name&gt;.service</code></pre>
</dl>
<p> To obtain a detailed status of a Tomcat PKI instance named &lt;pki_instance_name&gt;:</p>
<dl>
<dd>
<pre><code>pkidaemon status tomcat &lt;pki_instance_name&gt;</code></pre>
</dl>
<p> To obtain a detailed status of all Tomcat PKI instances:</p>
<dl>
<dd>
<pre><code>pkidaemon status tomcat</code></pre>
<h2>Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a> </p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;. <code>pkispawn</code> was written by the Certificate Server project.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pkidestroy/">pkidestroy</a>(8),</code> <code><a href="/docs/linux/man/5-pki_default-cfg/">pki_default.cfg</a>(5),</code> <code><a href="/docs/linux/man/1-pki/">pki</a>(1),</code> <code><a href="/docs/linux/man/8-setup-ds-pl/">setup-ds.pl</a>(8)</code> </p>
