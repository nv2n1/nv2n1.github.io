---
title: "myproxy-server-config(5)"
name: "myproxy-server-config"
section: "5"
letter: "m"
url: "/docs/linux/man/5-myproxy-server-config/"
description: "myproxy-server.config – myproxy-server configuration file"
---

<p>myproxy-server.config &#8211; myproxy-server configuration file</p>
<h2>Description</h2>
<p>The <code>myproxy-server.config</code> file sets the policy for the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8), specifying what credentials may be stored in the server&#8217;s repository, who is authorized to retrieve credentials, and other configurable server behaviors. By default, the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) looks for this file in <i>/etc/myproxy-server.config</i> and if it is not found there, it looks in <i>$GLOBUS_LOCATION/etc/myproxy-server.config</i>. A template is provided at <i>$GLOBUS_LOCATION/share/myproxy/myproxy-server.config</i>. The <code>myproxy-server -c</code> option can be used to specify an alternative location. The following lines set access control policies according to the client&#8217;s certificate subject distinguished name (DN). Note that MyProxy uses non-standard regular expressions for distinguished name (DN) matching. See the <code>REGULAR EXPRESSIONS</code> section below for details.</p>
<dl>
<dt><code>accepted_credentials</code><i> &#8220;DN regex&#8221;</i></p>
<dd>Each of these lines allows any clients whose DNs match the given limited regex to connect to the myproxy-server and store credentials with it for future retrieval. Any number of these lines may appear. For backwards compatibility, these lines can also start with <code>allowed_clients </code> instead of <code>accepted_credentials</code>. If no <code>accepted_credentials</code> lines are specified, the server will not allow any clients to store credentials.</p>
<dt><code>authorized_retrievers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>Each of these lines allows the server administrator to set server-wide policies for credential retrievers. If the client DN does not match the given limited regex, the client is not allowed to retrieve credentials from the server. In addition to the server-wide policy, myproxy also provides support for per-credential policy. The user can specify the regex DN of the allowed retrievers of the credential when uploading the credential (using <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) or <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1)). The retrieval client DN must also match the user specified regex. In order to retrieve credentials the client also needs to know the name and pass phrase provided by the client when the credentials were stored. Any number of these lines may appear. For backwards compatibility, these lines can also start with <code>allowed_services </code> instead of <code>authorized_retrievers</code>. If no <code>authorized_retrievers</code> lines are specified, the server will not allow any clients to retrieve credentials.</p>
<dt><code>default_retrievers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>Each of these lines allows the server administrator to set server-wide default policies. The regex specifies the clients who can access the credentials. The default retriever policy is enforced if a per-credential policy is not specified on upload (using <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) or <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1)). In other words, the client can override this policy for a credential on upload. The per-credential policy is enforced in addition to the server-wide policy specified by the authorized_retrievers line (which clients can not override). Any number of these lines may be present. For backwards compatibility, if no <code>default_retrievers </code> line is specified, the default policy is &quot;*&quot;, which allows any client to pass the per-credential policy check. (The client must still pass the <code>authorized_retrievers </code> check.)</p>
<dt><code>authorized_renewers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>Each of these lines allows the server administrator to set server-wide policies for authorized renewers. If the client DN does not match the given limited regex the client is not allowed to renew the credentials previously stored by a client. See <code>allow_self_authorization</code> below for a further restriction on this policy. In addition to the server-wide policy, myproxy also provides support for per-credential policy. The user can specify the regex DN of the allowed renewers of the credential on upload (using <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1)). The renewal client DN must match both this regex and the user specified regex. In this case, the client must also already have a credential with a DN matching the DN of the credentials to be retrieved, to be used in a second authorization step (see the <code>-a</code> options for <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1) and <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1)).</p>
<dt><code>default_renewers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>Each of these lines allows the server administrator to set server-wide default renewer policies. The regex specifies the clients who can renew the credentials. The default renewer policy is enforced if a per-credential policy is not specified on upload (using <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1)). This is enforced in addition to the server-wide policy specified by the <code>authorized_renewers </code> line. Any number of these lines may appear. For backwards compatibility, if no default_renewers line is specified, the default policy is &quot;*&quot;, which allows any client to pass the per-credential policy check. (The client must still pass the <code>authorized_renewers</code> check.)</p>
<dt><code>authorized_key_retrievers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>This policy controls who can retrieve credentials (certificates and keys) directly from the repository using <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1). Clients must also match the <code>authorized_retrievers</code> policy. If no <code>authorized_key_retrievers</code> lines are specified, the server will not allow any clients to retrieve keys directly from the repository.</p>
<dt><code>default_key_retrievers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>This policy applies if a per-credential policy is not specified on upload (using <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) or <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1)). In other words, the client can override this policy for a credential on upload. The per-credential policy is enforced in addition to the server-wide policy specified by the authorized_key_retrievers line (which clients can not override). Any number of these lines may be present. If no <code>default_key_retrievers </code> line is specified, the default policy is &quot;*&quot;, which allows any client to pass the per-credential policy check. (The client must still pass the <code>authorized_key_retrievers </code> check.)</p>
<dt><code>trusted_retrievers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>This policy controls who can retrieve credentials without further authentication. By default, clients that match <code>authorized_retrievers </code> must perform additional authentication (such as passphrase, PAM, or SASL) to retrieve credentials. However, authenticated clients that match both <code>authorized_retrievers </code> and <code>trusted_retrievers </code> do not need to perform additional authentication, unless the credentials are protected by a passphrase, in which case the passphrase is still required. Note: The <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) will fail on startup or reconfig with an &quot;unsafe policy&quot; error if a policy of <code>trusted_retrievers</code><i> &#8220;*&#8221;</i> is specified without also specifying a restrictive <code>default_trusted_retrievers</code> policy, to avoid an unsafe policy that would release credentials to all clients without additional authentication. See also <code>allow_self_authorization</code> below for a further restriction on this policy.</p>
<dt><code>default_trusted_retrievers</code><i> &#8220;DN regex&#8221;</i></p>
<dd>If a user doesn&#8217;t set a trusted retrieval policy with the credential on upload (via <code>&#8216;myproxy-init </code> <code>-Z&#8217;</code>), the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) will apply the following policy in addition to the <code>trusted_retrievers </code> policy. If no <code>default_trusted_retrievers </code> policy is set, then only the <code>trusted_retrievers </code> policy is applied.</dl>
<p> The following lines in the configuration file set other server options.</p>
<dl>
<dt><code>passphrase_policy_program</code><i> full-path-to-script</i></p>
<dd>This line specifies a program to run whenever a passphrase is set or changed for implementing a local password policy. The program is passed the new passphrase via stdin and is passed the following arguments: username, distinguished name, credential name (if any), per-credential retriever policy (if any), and per-credential renewal policy (if any). If the passphrase is acceptable, the program should exit with status 0. Otherwise, it should exit with non-zero status, causing the operation in progress (credential load, passphrase change) to fail with the error message provided by the program&#8217;s stdout. Note: You must specify the full path to the external program. $GLOBUS_LOCATION can&#8217;t be used in the myproxy-server.config file. A sample program is installed in <i>$GLOBUS_LOCATION/share/myproxy/myproxy-passphrase-policy</i> but is not enabled by default.</p>
<dl>
<dd><code>Be sure to follow secure coding practices for this call-out:</code> &#8211; Don&#8217;t allow input to overflow fixed-size buffers. &#8211; Don&#8217;t pass unchecked input to a shell command.</dl>
<dt><code>cert_dir</code><i> full-path-to-certificates-directory</i></p>
<dd>Specifies the path to the CA certificates directory to be returned to clients requesting trust roots (such as via the <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1) <code>-T</code> option).</p>
<dt><code>max_proxy_lifetime</code><i> hours</i></p>
<dd>This line specifies a server-wide maximum lifetime for retrieved proxy credentials. By default, no server-wide maximum is enforced. However, if this option is specified, the server will limit the lifetime of any retrieved proxy credentials to the value given.</p>
<dt><code>max_cred_lifetime</code><i> hours</i></p>
<dd>This line specifies a server-wide maximum lifetime for stored credentials. By default, no server-wide maximum is enforced. However, if this option is specified, the server will limit the lifetime of any stored credentials to the value given.</p>
<dt><code>ignore_globus_limited_proxy_flag</code><i> boolean</i></p>
<dd>By default, MyProxy will respect the policy of &quot;limited&quot; proxy certificates as follows. If a client authenticates with a limited proxy, the client should only be able to obtain another limited proxy, not a full proxy or end entity certificate. Thus, the MyProxy CA will not accept limited proxies for authentication. However, if this option is set to true, MyProxy will treat limited proxy certificates as if they were full proxy certificates.</p>
<dt><code>allow_self_authorization</code><i> boolean</i></p>
<dd>By default, MyProxy will disallow <code>trusted_retrievers</code> and <code>authorized_renewers</code> whose DN matches the identity of the stored credential, so a proxy by itself can not be refreshed or renewed. However, if this option is set to true, this restriction is lifted.</p>
<dt><code>syslog_ident</code><i> name</i></p>
<dd>You can optionally specify the string to be prepended to every message written to the syslog. If not specified, the name defaults to the the program name, i.e. myproxy-server.</p>
<dt><code>syslog_facility</code><i> name</i></p>
<dd>By default, the myproxy-server will log to the syslog &quot;daemon&quot; facility. With this option you can specify an alternate syslog facility, such as &quot;auth&quot;, &quot;user&quot;, &quot;security&quot;, or &quot;local0&quot;. The facility can also be specified numerically as with the <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1) command.</p>
<dt><code>request_timeout</code><i> seconds</i></p>
<dd>Specifies the maximum time a <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) child process should spend servicing a client request before aborting. By default, child processes will abort after 120 seconds. A negative value will disable the timeout.</p>
<dt><code>request_size_limit</code><i> bytes</i></p>
<dd>Limits the amount of incoming application-level protocol data the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) will accept from clients, to avoid memory exhaustion under heavy load. Specified in bytes. Defaults to 1MB (1048576 bytes). A zero or negative value disables the limit.</p>
<dt><code>proxy_extfile</code><i> full-path-to-extension-file</i></p>
<dd>Optionally specifies the full path to a file containing an OpenSSL formatted set of certificate extensions to include in all proxy certificates issued from the MyProxy repository (analogous to <code>certificate_extfile</code> for the CA module).</p>
<dt><code>proxy_extapp</code><i> full-path-to-extension-callout-program</i></p>
<dd>This is the call-out version of proxy_extfile. It optionally specifies the full path to a call-out program for specifying proxy certificate extensions. It will be passed the authenticated username and the proxy credential location as the two command arguments. On success, it should write the OpenSSL formatted set of certificate extensions to stdout and exit with zero status. On error, it should write to stderr and exit with nonzero status. Either <code>proxy_extfile</code> or <code>proxy_extapp</code> can be specified but not both.</p>
<dl>
<dd><code>Be sure to follow secure coding practices for this call-out:</code> &#8211; Don&#8217;t allow input to overflow fixed-size buffers. &#8211; Don&#8217;t pass unchecked input to a shell command.</dl>
<dt><code>voms_userconf</code><i> full-path-to-voms-configuration-file</i></p>
<dd>Optionally specifies the full path to the VOMS configuration file containing VOMS server information. It is usually specified in the environmental variable VOMS_USERCONF.</p>
<dt><code>allow_voms_attribute_requests</code><i> boolean</i></p>
<dd>If this parameter is set to true and a GET request includes VONAME and (optionally) VOMSES parameters, call-out to VOMS to add the requested attributes to the issued certificate. Requires linking with VOMS libraries. By default, VONAME and VOMSES parameters in requests will be ignored unless this parameter is set to true.</dl>
<p> The MyProxy server can be optionally configured for authentication based on Pluggable Authentication Modules (PAM) and/or the Simple Authentication and Security Layer (SASL). Kerberos is one of the supported SASL authentication methods. The following options control the use of PAM and SASL.</p>
<dl>
<dt><code>pam</code><i> option</i></p>
<dd>This line governs the use of PAM to check passphrases. MyProxy will attempt to authenticate via PAM, with the supplied username and passphrase. Note that PAM will need to be configured externally for the application &quot;myproxy&quot; (usually in /etc/pam.d/), or for the application named by pam_id, below. Accepted values:</p>
<dl>
<dd>
<dl>
<dt><code>required</code></p>
<dd>PAM password authentication is required under all conditions. If the credential is unencrypted (that is, it has no passphrase), a PAM password check is still required for authentication. If the credential is encrypted, its passphrase must match the PAM password.</p>
<dt><code>sufficient</code></p>
<dd>The user&#8217;s passphrase may match either the credential passphrase or, if the credential is unencrypted, the PAM passphrase. If the credential is encrypted, then the PAM password is not relevant.</p>
<dt><code>disabled</code> (default)</p>
<dd>PAM is not used to check passphrases.</dl>
</dl>
<dt><code>pam_id</code><i> string</i></p>
<dd>The name that myproxy uses to identify itself to PAM. Default is &quot;myproxy&quot;. For example, on most Unix-like systems, if pam_id is set to &quot;login&quot;, MyProxy will authenticate against the system&#8217;s own usernames and passwords.</p>
<dt><code>sasl</code><i> option</i></p>
<dd>This line governs the use of SASL authentication. Accepted values:</p>
<dl>
<dd>
<dl>
<dt><code>required</code></p>
<dd>SASL authentication is required for retrieving credentials.</p>
<dt><code>sufficient</code></p>
<dd>SASL authentication is sufficient for retrieving credentials, but other authentication methods may be used instead.</p>
<dt><code>disabled</code> (default)</p>
<dd>SASL authentication isn&#8217;t used.</dl>
</dl>
<dt><code>sasl_mech</code><i> mechanism</i></p>
<dd>Forces the use of a single SASL mechanism, overriding the SASL configuration file. (Typically not required.)</p>
<dt><code>sasl_serverFQDN</code><i> hostname</i></p>
<dd>Configures the SASL server fully-qualified domain name for multi-homed servers. (Typically not required.)</p>
<dt><code>sasl_user_realm</code><i> realm</i></p>
<dd>Configures the SASL user realm. (Typically not required.)</dl>
<p> The MyProxy server can also be configured to act as a Certificate Authority (CA) to issue credentials to clients. The following parameters enable and configure the CA functionality.</p>
<dl>
<dt><code>certificate_issuer_cert</code><i> full-path-to-certificate</i></p>
<dd>This line specifies the full path to the issuer certificate to optionally configure the myproxy-server to act as an online certificate authority.</p>
<dt><code>certificate_issuer_key</code><i> full-path-to-key</i></p>
<dd>When specifying <code>certificate_issuer_cert </code> above, you must also give the name of the CA private key for signing certificates. This is normally path to a CA private key in PEM format, but if you are using an OpenSSL engine (see <code>certificate_openssl_engine_id</code> ) then it can be the key name.</p>
<dt><code>certificate_issuer_key_passphrase</code><i> &#8220;passphrase&#8221;</i></p>
<dd>If the <code>certificate_issuer_key </code> is encrypted, give the passphrase here.</p>
<dt><code>certificate_issuer_subca_certfile</code><i> full-path-to-subca-certificate-file</i></p>
<dd>If you would like an intermediate/sub-CA certificate chain to be sent along with the EEC (End Entity Certificate) generated using a local intermediate/sub-CA, specify the file that contains those certificates in PEM format. This is meant to aid scenarios where the CA used is an intermediate CA (i.e. not a root CA) and the client may not have the intermediate CA(s) in its trust store. The client will write out the chain into the same file as the EEC, following the EEC.</p>
<dt><code>certificate_issuer_hashalg</code><i> algorithm</i></p>
<dd>Specifies the hash algorithm to use when signing end-entity certificates. Defaults to &quot;sha256&quot;.</p>
<dt><code>certificate_issuer_email_domain</code><i> &#8220;domain&#8221;</i></p>
<dd>If set, specifies the domain part of the X509v3 Subject Alternative Name email address included in issued certificates.</dl>
<p> <code>certificate_openssl_engine_id</code><i> engineId</i> <code>certificate_openssl_engine_pre</code><i> pre-initialization-commands</i></p>
<dl>
<dt><code>certificate_openssl_engine_post</code><i> post-initialization-commands</i></p>
<dd>These commands can be used to allow any OpenSSL engine to be used with MyProxy. This enables the use of hardware tokens and signing modules to sign certificates. Given the parameters of an OpenSSL &quot;engine&quot; command, the first argument, the identity of the engine becomes the argument to <code>certificate_openssl_engine_id </code> and -pre commands are listed in order using <code>certificate_openssl_engine_pre</code> and -post commands are listed in order using <code>certificate_openssl_engine_post.</code> For example the command-line:</p>
<dd>openssl engine dynamic -pre SO_PATH:/usr/lib/engines/engine_pkcs11.so&nbsp;<wbr> -pre ID:pkcs11 -pre LIST_ADD:1 -pre LOAD -pre MODULE_PATH:/usr/lib/opensc-pksc11.so</p>
<dd>becomes:</p>
<dd>certificate_openssl_engine_id&nbsp;<wbr>&quot;dynamic&quot;</p>
<dd>certificate_openssl_engine_pre&nbsp;<wbr> &quot;SO_PATH:/usr/lib/engines/engine_pkcs11.so&quot; &quot;ID:pkcs11&quot; &quot;LIST_ADD:1&quot; &quot;LOAD&quot; &quot;MODULE_PATH:/usr/lib/opensc-pksc11.so&quot;</p>
<dd>Please note that any shared library engines loaded through the &quot;dynamic&quot; engine MUST be compiled againt the correct version of OpenSSL. The Globus toolkit has its own installation and can be found by running $GLOBUS_LOCATION/bin/openssl version.</p>
<dt><code>certificate_openssl_engine_lockfile</code><i> full-path-to-file</i></p>
<dd>If your hardware token or HSM is unable to handle simultaneous operations, provide a path to a lockfile for synchronizing operations to the engine device. The myproxy-server will create the file if it does not already exist.</p>
<dt><code>certificate_issuer_program</code><i> full-path-to-script</i></p>
<dd>This line specifies the path to a program to issue certificates for authenticated clients that don&#8217;t have credentials stored. This optionally configures the myproxy-server to act as an online certificate authority, allowing programmatic control over the certificate issuance process. You can either specify <code>certificate_issuer_cert</code> or <code>certificate_issuer_program</code>.</p>
<dl>
<dd><code>Be sure to follow secure coding practices for this call-out:</code> &#8211; Don&#8217;t allow input to overflow fixed-size buffers. &#8211; Don&#8217;t pass unchecked input to a shell command.</dl>
<dt><code>certificate_serialfile</code><i> full-path-to-serial-file</i></p>
<dd>Specifies the path to a file to store the serial number counter for issued certificates. Defaults to /var/lib/myproxy/serial.</p>
<dt><code>certificate_serial_skip</code><i> increment</i></p>
<dd>Specifies the number to add to the serial number each time a certificate is issued. Use this to stagger serial numbers across multiple CA instances to avoid serial number clashes. Defaults to 1.</p>
<dt><code>certificate_out_dir</code><i> full-path-to-putput-directory</i></p>
<dd>Specifies the path to a directory where new certificates will be archived.</p>
<dt><code>max_cert_lifetime</code><i> hours</i></p>
<dd>Specifies the maximum lifetime (in hours) for certificates issued by the CA module. Defaults to 12 hours.</p>
<dt><code>min_keylen</code><i> bits</i></p>
<dd>Specifies the minimum RSA key length (in bits) for certificates issued by the CA module.</p>
<dt><code>certificate_extfile</code><i> full-path-to-extension-file</i></p>
<dd>Optionally specifies the full path to a file containing an OpenSSL formatted set of certificate extensions to include in all issued certificates. For example:</p>
<dl>
<dd>keyUsage=digitalSignature,keyEncipherment,dataEncipherment </p>
<pre><code>subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid,issuer:always
crlDistributionPoints=URI:http://ca.ncsa.uiuc.edu/4a6cd8b1.r0</code></pre>
<p>basicConstraints=CA:FALSE</dl>
<dl>
<dd>If not set, the MyProxy CA will include a basic set of extensions in issued certificates.</dl>
<dt><code>certificate_extapp</code><i> full-path-to-extension-callout-program</i></p>
<dd>This is the call-out version of certificate_extfile. It optionally specifies the full path to a call-out program for specifying certificate extensions. It will be passed the authenticated username as the single command argument. On success, it should write the OpenSSL formatted set of certificate extensions to stdout and exit with zero status. On error, it should write to stderr and exit with nonzero status. Either <code>certificate_extfile</code> or <code>certificate_extapp</code> can be specified but not both.</p>
<dl>
<dd><code>Be sure to follow secure coding practices for this call-out:</code> &#8211; Don&#8217;t allow input to overflow fixed-size buffers. &#8211; Don&#8217;t pass unchecked input to a shell command.</dl>
<dt><code>certificate_mapfile</code><i> full-path-to-mapfile</i></p>
<dd>When specifying certificate_issuer_cert above, you can map account names to certificate subject distinguished names for the issued certificates using this mapfile, which has the same format as used by other Globus Toolkit services. By default, /etc/grid-security/grid-mapfile is used. The Globus Toolkit <code>grid-mapfile-add-entry</code> and <code>grid-mapfile-delete-entry</code> commands can be used to manage the grid-mapfile.</p>
<dt><code>certificate_mapapp</code><i> full-path-to-mapapp</i></p>
<dd>When specifying certificate_issuer_cert above, you can map account names to certificate subject distinguished names for the issued certificates using this call-out. It will be passed the authenticated username as the single command argument. On success, it should write the distinguished name in OpenSSL one line format (for example, &quot;/C=US/O=National Computational Science Alliance/CN=Jim Basney&quot;) to stdout and exit with zero status. On error, it should write to stderr and exit with nonzero status. If it is not defined, then mapfile lookup will be executed instead (see certificate_mapfile above). An example is installed in <i>$GLOBUS_LOCATION/share/myproxy/myproxy-certificate-mapapp</i>.</p>
<dl>
<dd><code>Be sure to follow secure coding practices for this call-out:</code> &#8211; Don&#8217;t allow input to overflow fixed-size buffers. &#8211; Don&#8217;t pass unchecked input to a shell command.</dl>
<dt><code>certificate_request_checker</code><i> full-path-to-callout-program</i></p>
<dd>This CA call-out can be used to perform checks on incoming certificate requests. It will be passed the certificate request in PEM format on stdin. If it returns a nonzero exit status, the CA will abort without signing the request. When returning a nonzero exit status, the callout should indicate the problem on stderr. An example is installed in <i>$GLOBUS_LOCATION/share/myproxy/myproxy-certreq-checker</i>.</p>
<dt><code>certificate_issuer_checker</code><i> full-path-to-callout-program</i></p>
<dd>This CA call-out can be used to perform checks on issued certificates before the certificate is returned to the client. It will be passed the certificate in PEM format on stdin. If it returns a nonzero exit status, the CA will abort without returning the signed certificate to the client. When returning a nonzero exit status, the callout should indicate the problem on stderr. An example is installed in <i>$GLOBUS_LOCATION/share/myproxy/myproxy-cert-checker</i>.</dl>
<p> If OpenLDAP support is built-in to the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8), the following parameters can be used to configure the CA module to map account names to certificate subject distinguished names via LDAP.</p>
<dl>
<dt><code>ca_ldap_server</code><i> &#8220;<a href="ldap://localhost:389/''">ldap://localhost:389/&#8221;</a></i></p>
<dd>This parameter specifies the URI to the LDAP server to use for username to DN resolution in the CA module. Both ldap:// and ldaps:// protocols are supported. A port number may optionally be specified as well. Defining this directive is the &quot;trigger&quot; that causes the name resolution module to use LDAP querying. If it is not defined, then mapfile lookup will be executed instead (see <code>certificate_mapfile</code> above).</p>
<dt><code>ca_ldap_uid_attribute</code><i> &#8220;uid&#8221;</i></p>
<dd>The name of the record attribute that maps to the MyProxy username. Required for LDAP username to DN resolution.</p>
<dt><code>ca_ldap_searchbase</code><i> &#8220;ou=people,dc=bullwinkle,dc=lbl,dc=gov&#8221;</i></p>
<dd>The DN of the region of the ldap database to be searched. Required for LDAP username to DN resolution.</p>
<dt><code>ca_ldap_dn_attribute</code><i> &#8220;subjectDN&#8221;</i></p>
<dd>If this directive is set, the LDAP resolver will pull the DN from the specified attribute in the returned record. If it is not set, the default is to use the DN of the record itself.</p>
<dt><code>ca_ldap_connect_dn</code><i> &#8220;cn=MyProxy,ou=ldapusers,dc=lbl,dc=gov&#8221;</i></p>
<dd>DN for LDAP basic authentication (optional).</p>
<dt><code>ca_ldap_connect_passphrase</code><i> &#8220;passphrase&#8221;</i></p>
<dd>Passphrase for LDAP basic authentication (optional).</dl>
<p> The following parameters control server replication with the <code><a href="/docs/linux/man/1-myproxy-replicate/">myproxy-replicate</a></code>(1) utility.</p>
<dl>
<dt><code>slave_servers</code><i> server:port;</i></p>
<dd>This value is for use with the <code><a href="/docs/linux/man/1-myproxy-replicate/">myproxy-replicate</a></code>(1) utility. This tag provides a list of servers that will be used as secondary repositories for the MyProxy database. Each server should be seperated by a &quot;;&quot;. Also, a port may be provided if the slave server is using a port other then the default. The server name maybe a recognized DNS or an IP address.</dl>
<p> The following parameters are used primarily when utilizing MyProxy as a delegation service for web portals.</p>
<dl>
<dt><code>accepted_credentials_mapfile</code><i> full-path-to-mapfile</i></p>
<dd>This parameter points to a grid-mapfile, which is possibly different from other mapfiles above. When specified, this mapfile is utilized during puts/stores (e.g. with <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) and <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1)). A credential is authorized to be put/stored only under the username specified in the mapfile. This prevents storing a user&#8217;s credential under a different username. Note that the credential checked for the presence of a SubjectDN/Username entry in the mapfile is the credential utilized to secure the connection between client and server, NOT the actual credential being stored. As the credential which secures the TLS connection is typically the same as the credential being stored, this should not be a major issue. The Globus Toolkit <code>grid-mapfile-add-entry</code> and <code>grid-mapfile-delete-entry</code> commands can be used to manage the grid-mapfile.</p>
<dt><code>accepted_credentials_mapapp</code><i> full-path-to-mapapp</i></p>
<dd>As an alternative to the accepted_credentials_mapfile option above, you can specify a call-out which is passed two parameters: a certificate subject distinguished name and a username (in that order). In essence, the call-out performs a lookup in a &#8216;virtual&#8217; accepted_credentials_mapfile. If the SubjectDN/Username line would appear in such a mapfile, then the call-out should exit with zero status indicating that a credential with the given SubjectDN is allowed to be stored under the given Username. Otherwise, the call-out should exit with nonzero status indicating error. An example is installed in <i>$GLOBUS_LOCATION/share/myproxy/myproxy-accepted-credentials-mapapp</i>.</p>
<dl>
<dd><code>Be sure to follow secure coding practices for this call-out:</code> &#8211; Don&#8217;t allow input to overflow fixed-size buffers. &#8211; Don&#8217;t pass unchecked input to a shell command.</dl>
<dt><code>check_multiple_credentials</code><i> boolean</i></p>
<dd>Typically when a credential is accessed by a client, the server checks only one credential for possible access authorization, even if there are multiple credentials stored under the given username. If this option is set to &quot;true&quot; AND the client does not specify a credential name for a MyProxy GET operation (i.e., from <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1)), then the server will check multiple credentials with the given username. If a credential is found to be authorized for client access, then that one will be used during processing. The default value for this option is &quot;false&quot;.</dl>
<p> The following parameters enable OCSP status checking of stored credentials in the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) repository, to avoid use of expired credentials.</p>
<dl>
<dt><code>ocsp_policy</code><i> policy</i></p>
<dd>Controls the policy for checking certificate validity via OCSP before credentials may be delegated. Currently, only the status of the end entity certificate is checked via OCSP (and not any proxy certificates or CA certificates). OCSP will not be used unless ocsp_responder_url and/or ocsp_policy are set. Supported policies are:<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;aia&quot;&nbsp;<wbr>&#8211; use OCSP responder in certificate AIA extension, if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>present;&nbsp;<wbr>otherwise use ocsp_responder_url, if set</p>
<dt><code>ocsp_responder_url</code><i> URL</i></p>
<dd>Specifies the URL of an OCSP responder to use to check the validity of credentials stored in the myproxy-server repository before they may be delegated, so that revoked credentials can not be retrieved and used where their revocation status may not be checked. Currently, only the status of the end entity certificate is checked via OCSP (and not any proxy certificates or CA certificates). In any case, CRL checks are always performed. Both http and https urls are supported. OCSP will not be used unless ocsp_responder_url and/or ocsp_policy are set.</p>
<dt><code>ocsp_responder_cert</code><i> path</i></p>
<dd>Specifies the path to the certificate of a trusted OCSP responder. This is needed if the OCSP responder must be explicity trusted in cases where standard path validation fails for the OCSP responder&#8217;s certificate.</dl>
<p> The following parameters control Usage Metrics reporting by the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8).</p>
<dl>
<dt><code>disable_usage_stats</code><i> value</i></p>
<dd>By default Usage Metrics reporting is enabled. Specifying &quot;true&quot;, &quot;enabled&quot;, &quot;yes&quot;, &quot;on&quot; or &quot;1&quot; for <i>value</i> will disable Usage Metrics reporting. Setting the GLOBUS_USAGE_OPTOUT environment variable to &quot;1&quot; will also disable the reporting of usage metrics. Disabling reporting of usage metrics will cause the <code>usage_stats_target</code> setting to be ignored.</p>
<dt><code>usage_stats_target</code><i> target_list</i></p>
<dd>This option can be used to specify the target collector hosts to which usage metrics should be reported. This setting will be ignored if <code>disable_usage_stats</code> is enabled. Multiple targets can be specified in <i>target_list</i> separated by comma(s). Each target specification is of the format <i>host:port[!tags]</i>. The <i>tags</i> control what data elements are reported. The following list specifies the tags for the corresponding data elements.</p>
<dl>
<dd>V &#8211; Major Version number of MyProxy server v &#8211; Minor Version number of MyProxy server t &#8211; Task Code (0=Get, 1=Put, 2=Info, 3=Destroy, 4=ChangeCredPassphrase, 5=StoreEndEntCred, 6=RetrEndEntCred, 7=GetTrustRoots) r &#8211; Task Return Code. l &#8211; Requested Lifetime for Credential. L &#8211; Actual Lifetime for Credential. B &#8211; Informational Bit mask to be interpreted left to right as follows:<br />
&nbsp;<wbr>PAM used<br />
&nbsp;<wbr>SASL used<br />
&nbsp;<wbr>Credential passphrase check used<br />
&nbsp;<wbr>Trusted Retriever&nbsp;<wbr>(Certificate-based authentication)<br />
&nbsp;<wbr>Certificate Authorization method used&nbsp;<wbr>(Trusted Renewer)<br />
&nbsp;<wbr>Pubcookie was used<br />
&nbsp;<wbr>Trustroots requested<br />
&nbsp;<wbr>Trustroots delivered I &#8211; Client IP address u &#8211; Username U &#8211; User DN In addition to the above selected information, the following data are reported to ALL the specified/default target collectors. There&#8217;s no way to exclude these from being reported other than by disabling the reporting of usage metrics: Component code &#8211; 11 for MyProxy Component Data Format version &#8211; 0 currently IP Address of Reporting Server Timestamp Hostname If no tags are specified in a host spec, or the special string &quot;default&quot; is specified, the tags VvtrlLB are assumed. A site could choose to allow a different set of data to be reported by specifying a different tag set. The last 3 tags I, u and U above are more meant for a local collector that a site might like to deploy since they could be construed as private information. The special string &quot;all&quot; denotes all tags. By default, Usage Metrics reporting is disabled. This can be made explicit by specifying &quot;default&quot; (all by itself) for the target specification as in: usage_stats_target &quot;default&quot; </p>
<h2>Regular Expressions</h2>
<p>For matching distinguished names (DNs) in access control policies, MyProxy uses POSIX Extended Regular Expressions (see <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7)), with custom processing of &#8216;*&#8217;, &#8216;?&#8217;, and &#8216;.&#8217; metacharacters to simulate Unix shell style wildcard processing (for backward compatibility and other historical reasons). MyProxy&#8217;s custom regular expressions are converted to POSIX EREs according to the following rules: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>MyProxy regex&nbsp;<wbr>]&nbsp;<wbr>=&gt;&nbsp;<wbr>[&nbsp;<wbr>POSIX ERE&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;*&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;.*&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;?&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;.&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;.&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;\.&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;\*&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;*&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;\?&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;?&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;\.&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;.&#8217; </p>
<p> Additionally, MyProxy wraps all regular expressions inside &#8216;^(&#8216; and &#8216;)$&#8217; to require full DN matching. </p>
<p> Be aware that parentheses are metacharacters according to POSIX, so escaping is required for literal matching. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;*/CN=Jim Basney&nbsp;<wbr>\(admin\)&quot; </p>
<p> The following examples illustrate how MyProxy regular expressions are converted to POSIX EREs: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>MyProxy regex&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>POSIX ERE&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;*/CN=Jim Basney&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&quot;^(.*/CN=Jim Basney)$&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;*/CN=Test User&nbsp;<wbr>?&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&quot;^(.*/CN=Test User .)$&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;*/CN=James A. Basney&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&gt;&nbsp;<wbr>&quot;^(.*/CN=James A\. Basney)$&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;/O=Test/CN=[:alnum:]\*&quot;&nbsp;<wbr>=&gt;&nbsp;<wbr>&quot;^(/O=Test/CN=[:alnum:]*)$&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;*/CN=Jim Basney|*/CN=James Basney&quot;&nbsp;<wbr>=&gt;<br />
&quot;^(.*/CN=Jim Basney|.*/CN=James Basney)$&quot;</p>
<h2>Examples</h2>
<p>The following policy enables all credential repository features. </p>
<p> accepted_credentials &quot;*&quot; </p>
<p> authorized_retrievers &quot;*&quot; </p>
<p> default_retrievers &quot;*&quot; </p>
<p> authorized_renewers &quot;*&quot; </p>
<p> default_renewers &quot;none&quot; </p>
<p> authorized_key_retrievers &quot;*&quot; </p>
<p> default_key_retrievers &quot;none&quot; </p>
<p> trusted_retrievers &quot;*&quot; </p>
<p> default_trusted_retrievers &quot;none&quot; </p>
<p> cert_dir /etc/grid-security/certificates </p>
<p> The following enables CA functionality using an existing Globus Simple CA configuration. </p>
<p> authorized_retrievers &quot;*&quot; </p>
<p> pam &quot;sufficient&quot; </p>
<p> sasl &quot;sufficient&quot; </p>
<p> certificate_issuer_cert /home/globus/.globus/simpleCA/cacert.pem </p>
<p> certificate_issuer_key /home/globus/.globus/simpleCA/private/cakey.pem </p>
<p> certificate_issuer_key_passphrase &quot;myproxy&quot; </p>
<p> certificate_serialfile /home/globus/.globus/simpleCA/serial </p>
<p> certificate_mapfile /etc/grid-security/grid-mapfile </p>
<p> cert_dir /etc/grid-security/certificates </p>
<p> The following will cause usage metrics to be reported to the default target (only the default tags) as well as a local collector (including the tags IuU): </p>
<p> usage_stats_target &quot;usage-stats.cilogon.org:4810,localcollector.somedomain:4810!VvtrlLBIuU&quot;</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/myproxy-server.config</i></p>
<dd>Default location for the server configuration file.</p>
<dt><i>$GLOBUS_LOCATION/etc/myproxy-server.config</i></p>
<dd>Alternate location for the server configuration file. A different location can be specified by using the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) <code>-c</code> option.</p>
<dt><i>$GLOBUS_LOCATION/share/myproxy/myproxy-passphrase-policy</i></p>
<dd>A sample program for evaluating passphrase quality for use with the <i>passphrase_policy_program </i> option.</p>
<dt><i>$GLOBUS_LOCATION/share/myproxy/myproxy-certificate-mapapp</i></p>
<dd>A sample <i>certificate_mapapp</i> program for mapping account names to certificate subject distinguished names.</p>
<dt><i>$GLOBUS_LOCATION/share/myproxy/myproxy-accepted-credentials-mapapp</i></p>
<dd>A sample <i>accepted_credentials_mapapp</i> program for authorizing puts/stores (e.g. with <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) and <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1)).</dl>
<h2>Environment</h2>
<dl>
<dt><code>GLOBUS_LOCATION</code></p>
<dd>Specifies the root of the MyProxy installation, used to find the default location of the <i>myproxy-server.config</i> file.</dl>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-get-trustroots/">myproxy-get-trustroots</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-info/">myproxy-info</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/8-myproxy-admin-adduser/">myproxy-admin-adduser</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-query/">myproxy-admin-query</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) </p>
