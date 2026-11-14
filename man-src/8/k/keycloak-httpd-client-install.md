---
title: "keycloak-httpd-client-install(8)"
name: "keycloak-httpd-client-install"
section: "8"
letter: "k"
url: "/docs/linux/man/8-keycloak-httpd-client-install/"
description: "keycloak-httpd-client-install – Tools to configure Apache HTTPD as Keycloak client"
---

<p>keycloak-httpd-client-install &#8211; Tools to configure Apache HTTPD as Keycloak client</p>
<h2>Synopsis</h2>
<p><code>keycloak-httpd-client-install</code> [<code>-h</code>] [<code>&#8211;no-root-check</code>] [<code>-v</code>] [<code>-d</code>] [<code>&#8211;show-traceback</code>] [<code>&#8211;log-file</code> <i>LOG_FILE</i>] <code>&#8211;app-name</code> <i>APP_NAME</i> [<code>&#8211;force</code>] [<code>&#8211;permit-insecure-transport</code>] [<code>&#8211;template-dir</code> <i>TEMPLATE_DIR</i>] [<code>&#8211;httpd-dir</code> <i>HTTPD_DIR</i>] -r KEYCLOAK_REALM <code>-s</code> <i>KEYCLOAK_SERVER_URL</i> [<code>-a</code> <i>root-admin|realm-admin|anonymous</i>] [<code>-u</code> <i>KEYCLOAK_ADMIN_USERNAME</i>] <code>-p</code> <i>KEYCLOAK_ADMIN_PASSWORD</i> [<code>&#8211;keycloak-admin-realm</code> <i>KEYCLOAK_ADMIN_REALM</i>] [<code>&#8211;initial-access-token</code> <i>INITIAL_ACCESS_TOKEN</i>] [<code>&#8211;client-originate-method</code> <i>{descriptor|registration}</i>] [<code>&#8211;mellon-key-file</code> <i>MELLON_KEY_FILE</i>] [<code>&#8211;mellon-cert-file</code> <i>MELLON_CERT_FILE</i>] [<code>&#8211;mellon-hostname</code> <i>MELLON_HOSTNAME</i>] [<code>&#8211;mellon-https-port</code> <i>MELLON_HTTPS_PORT</i>] [<code>&#8211;mellon-root</code> <i>MELLON_ROOT</i>] [<code>&#8211;mellon-endpoint</code> <i>MELLON_ENDPOINT</i>] [<code>&#8211;mellon-entity-id</code> <i>MELLON_ENTITY_ID</i>] [<code>&#8211;mellon-idp-attr-name</code> <i>MELLON_IDP_ATTR_NAME</i>] [<code>&#8211;mellon-organization-name</code> <i>MELLON_ORGANIZATION_NAME</i>] [<code>&#8211;mellon-organization-display-name</code> <i>MELLON_ORGANIZATION_DISPLAY_NAME</i>] [<code>&#8211;mellon-organization-url</code> <i>MELLON_ORGANIZATION_URL</i>] [<code>-l</code> <i>MELLON_PROTECTED_LOCATIONS</i>] Configure mod_auth_mellon as Keycloak client </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>&#8211;no-root-check</code></p>
<dd>permit running by non-root (default: False)</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>be chatty (default: False)</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>turn on debug info (default: False)</p>
<dt><code>&#8211;show-traceback</code></p>
<dd>exceptions print traceback in addition to error message (default: False)</p>
<dt><code>&#8211;log-file</code> <i>LOG_FILE</i></p>
<dd>log file pathname (default: /var/log/python-keycloak-httpd-client/keycloak-httpd-client-install.log)</p>
<dt><code>&#8211;app-name</code> <i>APP_NAME</i></p>
<dd>name of the web app being protected by mellon (default: None)</p>
<dt><code>&#8211;force</code></p>
<dd>forcefully override safety checks (default: False)</p>
<dt><code>&#8211;permit-insecure-transport</code></p>
<dd>Normally secure transport such as TLS is required, defeat this check (default: False) </p>
</dl>
<p> Program Configuration: </p>
<dl>
<dt><code>&#8211;template-dir</code> <i>TEMPLATE_DIR</i></p>
<dd>Template location (default: /usr/share/keycloak-httpd-client/templates)</p>
<dt><code>&#8211;httpd-dir</code> <i>HTTPD_DIR</i></p>
<dd>Template location (default: /etc/httpd) </p>
</dl>
<p> Keycloak IdP: </p>
<dl>
<dt><code>-r</code>, <code>&#8211;keycloak-realm</code> <i>KEYCLOAK_REALM</i></p>
<dd>realm name (default: None)</p>
<dt><code>-s</code>, <code>&#8211;keycloak-server-url</code> <i>KEYCLOAK_SERVER_URL</i></p>
<dd>Keycloak server URL (default: None)</p>
<dt><code>-a</code>, <code>&#8211;keycloak-auth-role</code> <i>root-admin|realm-admin|anonymous</i></p>
<dd>authenticating as what type of user (default: root-admin)</p>
<dt><code>-u</code>, <code>&#8211;keycloak-admin-username</code> <i>KEYCLOAK_ADMIN_USERNAME</i></p>
<dd>admin user name (default: admin)</p>
<dt><code>-p</code>, <code>&#8211;keycloak-admin-password</code> <i>KEYCLOAK_ADMIN_PASSWORD</i></p>
<dd>admin password (use &#8211; to read from stdin) (default: None)</p>
<dt><code>&#8211;keycloak-admin-realm</code> <i>KEYCLOAK_ADMIN_REALM</i></p>
<dd>realm admin belongs to (default: master)</p>
<dt><code>&#8211;initial-access-token</code> <i>INITIAL_ACCESS_TOKEN</i></p>
<dd>realm initial access token for client registeration (default: None)</p>
<dt><code>&#8211;client-originate-method</code> <i>descriptor|registration</i></p>
<dd>select Keycloak method for creating SAML client (default: descriptor) </p>
</dl>
<p> Mellon SP: </p>
<dl>
<dt><code>&#8211;mellon-key-file</code> <i>MELLON_KEY_FILE</i></p>
<dd>certficate key file (default: None)</p>
<dt><code>&#8211;mellon-cert-file</code> <i>MELLON_CERT_FILE</i></p>
<dd>certficate file (default: None)</p>
<dt><code>&#8211;mellon-hostname</code> <i>MELLON_HOSTNAME</i></p>
<dd>Machine&#8217;s fully qualified host name</p>
<dt><code>&#8211;mellon-https-port</code> <i>MELLON_HTTPS_PORT</i></p>
<dd>SSL/TLS port on mellon-hostname</p>
<dt><code>&#8211;mellon-root</code> <i>MELLON_ROOT</i></p>
<dd>Common root ancestor for all mellon endpoints</p>
<dt><code>&#8211;mellon-endpoint</code> <i>MELLON_ENDPOINT</i></p>
<dd>Used to form the MellonEndpointPath, e.g. {mellon_root}/{mellon_endpoint} (default: mellon)</p>
<dt><code>&#8211;mellon-entity-id</code> <i>MELLON_ENTITY_ID</i></p>
<dd>SP SAML Entity ID (default: {mellon_http_url}/{mellon_root}/{mellon_endpoint_path}/metadata)</p>
<dt><code>&#8211;mellon-idp-attr-name</code> <i>MELLON_IDP_ATTR_NAME</i></p>
<dd>Name of the attribute Mellon adds which will contain the IdP entity id (default: {mellon_http_url}/{mellon_root}/{mellon_endpoint_path}/metadata)</p>
<dt><code>&#8211;mellon-organization-name</code> <i>MELLON_ORGANIZATION_NAME</i></p>
<dd>Add SAML OrganizationName to SP metadata (default: None)</p>
<dt><code>&#8211;mellon-organization-display-name</code> <i>MELLON_ORGANIZATION_DISPLAY_NAME</i></p>
<dd>Add SAML OrganizationDisplayName to SP metadata (default: None)</p>
<dt><code>&#8211;mellon-organization-url</code> <i>MELLON_ORGANIZATION_URL</i></p>
<dd>Add SAML OrganizationURL to SP metadata (default: None)</p>
<dt><code>-l</code>, <code>&#8211;mellon-protected-locations</code> <i>MELLON_PROTECTED_LOCATIONS</i></p>
<dd>Web location to protect with Mellon. May be specified multiple times (default: []) </p>
</dl>
<h2>Description</h2>
<p><code>keycloak-httpd-client-install</code> will configure a node running Apache with mod_auth_mellon as SAML Service Provider (<code>SP</code>) utilizing a <code>Keycloak</code> server as an Identity Provider(<code>IdP</code>). <code>Authentication Levels and Permissions</code> The tool is capable of range of configuration steps. But the extent of those operations may be circumscribed by the privilege level (authorization) the tool is run with. The privilege level is determined by the <code>&#8211;keycloak-auth-role</code> command line option which may be one of: <code>root-admin</code>: The Keycloak installation has a super realm normally called <i>master</i> which is the container for all realms hosted by the Keycloak instance. A user with administration priviliges in the <i>master</i> realm can perform all operations on all realms hosted by the instance. Think of such a user as a root user or root admin. <code>realm-admin</code>: Each subordinate realm in the Keycloak instance may have it&#8217;s own administrator(s) whose privileges are restricted exclusively to that realm. <code>anonymous</code>: The tool does not authenticate as a user and hence no priviliges are granted. Any privilege is granted by virtue of an <i>initial access token</i> passed in via the <code>-initial-access-token</code> command line option. Think of an initial access token as a one time password scoped to a specific realm. The initial access token must be generated by an administrator with sufficient priviliges on the realm and given to the user of the tool. The priviliges conferred by the initial access token are limited to registering the client in the realm utilizing the Keycloak client registration service. Selecting which authencation role will be used is determined by a combination of the <code>&#8211;keycloak-auth-role</code> option and the <code>&#8211;keycloak-admin-realm</code> option. When the authentication role is one of <i>root-admin</i> or <i>realm-admin</i> the tool will authenticate as a user in a specific realm, the <code>&#8211;keycloak-admin-realm</code> option declares the realm the administrator will authenticate to. For the <i>root-admin</i> role this is typically the <i>master</i> realm. For the <i>realm-admin</i> role this would be realm the tool is registrating the client in. <code>Determining which authentication role to use</code> In general the principle of <i>least privilige</i> should apply. Grant to the tool the least privilige necessary to perform the required action. In oder of least privilige to greatest privilige the following operations are possible under the defined authentication roles: <code>anonymous</code></p>
<dl>
<dd><code>*</code> Can register the client using only the Keycloak client registration service. The tool cannot determine a prori if the client already exists in the realm nor can it adjust any configuration options on the client. <code>*</code> The realm must pre-exist.</dl>
<p> <code>realm-admin</code></p>
<dl>
<dd><code>*</code> Can enumerate the existing clients in the realm to determine if a conflict would occur. <code>*</code> Can delete a pre-existing client and replace it with the new client definition if the <code>&#8211;force</code> option is supplied. <code>*</code> Can modify the clients configuration. <code>*</code> Can use either the client registration service or the REST API to create the client. <code>*</code> The realm must pre-exist and contain the realm admin user.</dl>
<p> <code>root-admin</code></p>
<dl>
<dd><code>*</code> Includes all of the priviliged operation conferred by the <i>realm-admin</i>. <code>*</code> Can enumerate existing realms on the Keycloak instance to verify the existence of the target realm the client is to be installed in. <code>*</code> Can create the target realm if it does not exist.</dl>
<p> <code>Client creation methods</code> Keycloak offers two methods to add a client to a realm</p>
<dl>
<dd><code>*</code> The OpenID Connect client registration service. Note even though we are registering a SAML Service Provider (SP) which is not part of OAuth2 nor OpenID Connect the client registration service is still capable of registering a SAML SP client. Selected with <code>&#8211;client-originate-method register</code>. <code>*</code> Utilizing the Keycloak REST API to create and configure the SAML SP client. The Keycloak REST API utilizes a 2-step process whereby the SP metadata is sent to the the Keycloak instance and it returns a client descriptor which is then used to create the client. Selected with <code>&#8211;client-originate-method descriptor</code>.</dl>
<p> At the time of this writing the client registration service behaves differently than the REST API. Advice on which to use is likely to be dependent upone the Keycloak version. Note, if anonymous authentication is used in conjunction with a initial access token then the client registration service <i>must</i> be used. The client registration service requies the use of an initial access token. For all authentiction roles an initial access token can be provided on the command line via the <code>initial-access-token</code> option. The initial access token will have to have been provided by a Keycloak administrator who pre-creates it. If the authencation role is either <i>root-admin</i> or <i>realm-admin</i> the tool has sufficient privilige to obtain an initial access token on it&#8217;s behalf negating the need for a Keycloak admin to supply one externally. The client registration service may be used by the following authentication roles:</p>
<dl>
<dd><code>*</code> root-admin <code>*</code> realm-admin <code>*</code> anonymous (requires use of <code>&#8211;initial-access-token</code>)</dl>
<p> The REST API may be used by the following authentication roles:</p>
<dl>
<dd><code>*</code> root-admin <code>*</code> realm-admin</dl>
<h2>Operation</h2>
<p><code>keycloak-httpd-client-install</code> performs the following operational steps: </p>
<p> <code>*</code> Connect to Keycloak Server.</p>
<dl>
<dd>A session is established with the Keycloak server. OAuth2 is used to log in as the admin user using the <code>&#8211;keycloak-admin-username</code> and <code>&#8211;keycloak-admin-password</code> options. The Keycloak server is identified by the <code>-keycloak-server-url</code> option. This step is performed first to assure the remaining steps can complete successfully. A session is maintained for efficiency reasons. You may also need to specify <code>&#8211;keycloak-admin-role</code> and <code>&#8211;keycloak-admin-realm</code> to indicate the privilege level you are authenticating with. An anonymous auth role connects to the Keycloak service without any authentication.</dl>
<p> <code>*</code> Create directories.</p>
<dl>
<dd>Files written by <code>keycloak-httpd-client-install</code> need a destination directory (see <code>FILES</code>). If the necessary directories are not present they are created.</dl>
<p> <code>*</code> Set up template environment</p>
<dl>
<dd>Many of the files written by <code>keycloak-httpd-client-install</code> are based on <i>jinga2</i> templates. The default template file location can be overridden with the <code>&#8211;template-dir</code> option.</dl>
<p> <code>*</code> Set up Service Provider X509 Certificiates.</p>
<dl>
<dd>A SAML SP must have a X509 certificate and key used to sign and optionally encrypt it&#8217;s SAML messages sent to the SAML IdP. <code>keycloak-httpd-client-install</code> can generate a self-signed certificate for you or you may supply your own key and certificate via the <code>&#8211;mellon-key-file</code> and <code>&#8211;mellon-cert-file</code> options. The files must be in PEM format.</dl>
<p> <code>*</code> Build Mellon httpd config file.</p>
<dl>
<dd>The Mellon HTTPD configuration file tells <i>mod_auth_mellon</i> where to find things such as certificates and metadata files as well as what web resources to protect. It is generated from the <i>mellon_httpd.conf</i> template file. (see <code>FILES</code>). There is one mellon httpd conf file per application.</dl>
<p> <code>*</code> Build Mellon SP metadata file.</p>
<dl>
<dd>The Mellon SP needs to be registered with the Keycloak IdP. This forms a trust relationship and provides infomation to the IdP about the Mellon SP. Registering an SP with an IdP is done via a SP metadata file. The Mellon SP metadata also instructs <i>mod_auth_mellon</i> how to operate. The Mellon SP is generated from the <i>sp_metadata.tpl</i> template file.</dl>
<p> <code>*</code> Query realms from Keycloak server, optionally create new realm.</p>
<dl>
<dd>Keycloak supports multi-tenancy, it may serve many IdP&#8217;s each one specified by a Keycloak realm. The <code>&#8211;keycloak-realm</code> option identifies which Keycloak realm we will bind to. The Keycloak realm may already exist on the Keycloak server, if it does <code>keycloak-httpd-client-install</code> will use it. If the Keycloak realm does not exist yet it will be created for you. </p>
<p> Requires the <i>root-admin</i> auth role.</dl>
<p> <code>*</code> Query realm clients from Keycloak server, optionally delete existing.</p>
<dl>
<dd>SAML SP&#8217;s are one type of Keycloak client that can be serviced by the Keycloak realm IdP. The Mellon SP is a new Keycloak client which needs to be added to the Keycloak realm. However we must assure the new client does not conflict with an existing client on the Keycloak realm. If the Mellon SP is already registered on the Keycloak realm <code>keycloak-httpd-client-install</code> will stop processing and exit with an error unless the <code>&#8211;force</code> option is used. <code>&#8211;force</code> will cause the existing client on the Keycloak realm to be deleted first so that it can be replaced in the next step. </p>
<p> Requires either the <i>root-admin</i> or <i>realm-admin</i> auth role.</dl>
<p> <code>*</code> Create new SP client in Keycloak realm.</p>
<dl>
<dd>The Mellon SP is registered with the Keycloak realm on the Keycloak server by sending the Keycloak server the Mellon SP metadata to the Keycloak server. </p>
<p> When the client-originate-method is <i>descriptor</i> either the <i>root-admin</i> or <i>realm-admin</i> auth role is required. When the <i>client-originate-method</i> is <i>registration</i> the initial access token is mandatory for the <i>anonymous</i> auth role and optional for the <i>root-admin</i> or <i>realm-admin</i> roles.</dl>
<p> <code>*</code> Adjust client configuration</p>
<dl>
<dd>Override default Keycloak client values. This varies by Keycloak release. </p>
<p> Requires either the <i>root-admin</i> or <i>realm-admin</i> auth role.</dl>
<p> <code>*</code> Add attributes to be returned in assertion</p>
<dl>
<dd>The client is configured to return necessary attributes. The added attributes are:</p>
<dl>
<dd><code>*</code> Groups user is a member of.</dl>
<p> Requires either the <i>root-admin</i> or <i>realm-admin</i> auth role.</dl>
<p> <code>*</code> Retrieve IdP metadata from Keycloak server.</p>
<dl>
<dd>The Mellon SP needs SAML metadata that describes the Keycloak IdP. The metadata for the Keycloak IdP is fetched from the Keycloak server and stored in a location referenced in the Mellon SP httpd configuration file. (see <code>FILES</code>)</dl>
<p> <code>STRUCTURE</code> </p>
<p> The overarching organization is the web application. An independent set of Mellon files are created per application and registered with the Keycloak server. This permits multiple indpendent SAML Service Providers and/or protected web resources to be handled by one Apache instance. When you run <code>keycloak-httpd-client-install</code> you must supply an application name via the <code>&#8211;app-name</code> option. </p>
<p> Within the web application you may protect via SAML multiple independent web resources specified via the <code>&#8211;mellon-protected-locations</code> /xxx option. This will cause a: </p>
<pre><dl><dt><dd>&lt;Location&gt;
 AuthType Mellon
 MellonEnable auth
 Require valid-user
&lt;/Location&gt;
</dl></pre>
<p>directive to be added to the Mellon HTTPD configuration file. The Mellon SP parameters are located at the root of the web application root, each protected location inherits from that.</p>
<h2>Files</h2>
<p>Files created by running <code>keycloak-httpd-client-install</code>:</p>
<dl>
<dt><code>{httpd-dir}/conf.d/{app-name}_mellon_keycloak_{realm}.conf</code></p>
<dd>This is the primary Mellon configuration file for the application. It binds to the Keycloak realm IdP. It is generated from the <i>mellon_httpd.conf</i> template file. </p>
<dt><code>{httpd-dir}/saml2/{app-name}.cert</code></p>
<dd>The Mellon SP X509 certficate file in PEM format. </p>
<dt><code>{httpd-dir}/saml2/{app-name}.key</code></p>
<dd>The Mellon SP X509 key file in PEM format. </p>
<dt><code>{httpd-dir}/saml2/{app-name}_keycloak_{realm}_idp_metadata.xml</code></p>
<dd>The Keycloak SAML2 IdP metadata file. It is fetched from the Keycloak server. </p>
<dt><code>{httpd-dir}/saml2/{app-name}_sp_metadata.xml</code></p>
<dd>The Mellon SAML2 SP metadata file. It is generated from the <i>sp_metadata.xml</i> template file. </p>
</dl>
<p> <code>Files referenced by keycloak-httpd-client-install</code> when it runs: </p>
<dl>
<dt><code>/usr/share/python-keycloak-httpd-client/templates/*</code></p>
<dd>jinja2 templates </p>
</dl>
<p> <code>Log files:</code></p>
<dl>
<dt><code>/var/log/python-keycloak-httpd-client/keycloak-httpd-client-install.log</code></p>
<dd>Installation log file </p>
</dl>
<p> <code>DEBUGGING</code> </p>
<p> The <code>&#8211;verbose</code> and <code>&#8211;debug</code> options can be used to increase the level of detail emitted on the console. However, note the log file logs everything at the <i>DEBUG</i> level so it is usually easier to consult the log file when debugging (see <code>LOGGING</code>) </p>
<p> <code>LOGGING</code> </p>
<p> <code>keycloak-httpd-client-install</code> logs all it&#8217;s operations to a rotated log file. The default log file can be overridden with the <code>&#8211;log-file</code> option. Each run of <code>keycloak-httpd-client-install</code> will create a new log file. Any previous log file will be rotated as a numbered verson keeping a maximum of 3 previous log files. Logging to the log file occurs at the <i>DEBUG</i> level that includes all HTTP requests and responses, this is useful for debugging. </p>
<p> <code>TEMPLATES</code> </p>
<p> Many of the files generated by <code>keycloak-httpd-client-install</code> are produced via jinja2 templates substituting values determined by <code>keycloak-httpd-client-install</code> when it runs. The default template file location can be overridden with the <code>&#8211;template-dir</code> option.</p>
<h2>Exit Status</h2>
<dl>
<dd><code>0</code>: SUCCESS </p>
<p> <code>1</code>: OPERATION_ERROR </p>
<p> <code>2</code>: CONFIGURATION_ERROR </p>
<p> <code>3</code>: INSUFFICIENT_PRIVILEGE </p>
<p> <code>4</code>: COMMUNICATION_ERROR </p>
<p> <code>5</code>: ALREADY_EXISTS_ERROR</dl>
<h2>Author</h2>
<p>John Dennis &lt;jdennis [at] redhat.com&gt;</p>
