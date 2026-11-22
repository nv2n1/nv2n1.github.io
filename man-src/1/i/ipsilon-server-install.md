---

title: "ipsilon-server-install(1)"
name: "ipsilon-server-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipsilon-server-install/"
description: "ipsilon-server-install – Configure an Ipsilon Identity Provider instance"
---

<p> ipsilon-server-install &#8211; Configure an Ipsilon Identity Provider instance</p>
<h2>SYNOPSIS</h2>
<p> ipsilon-server-install [OPTION]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Configure an Ipsilon instance to provide identity services using any of the supported and enabled protocols. </p>
<p> Ipsilon uses a plugable framework so some options may not be available, depending on what plugins have been installed. </p>
<p> Ipsilon supports three types of plugins: </p>
<p> 1. Authentication provider plugins &#8211; implements an authentication protocol such as SAML 2, OpenID or Persona. At least one needs to be enabled.<br/>
 2. Login plugins &#8211; mechanisms for authenticating including GSSAPI, LDAP, PAM, etc. At least one should be enabled.<br/>
 3. Info plugins &#8211; sources where additional attributes of the user may be obtained. </p>
<p> There are also environment helper options which aid in configuring the Identity Provider for a particular environment, such as a FreeIPA domain. </p>
<p> The installation details are logged to /var/log/ipsilon-install.log.</p>
<h2>DATABASES</h2>
<p> Ipsilon stores configuration and session information in database tables. By default, a set of sqlite databases are used. If a full RDBMS is desired then the <code>&#8211;database-url</code> and/or <code>*-dburi</code> options can be used to provide the database URIs. This should probably be used in load-balanced situations so all servers can use the same database. </p>
<p> An example of a specific URI is<br/>
 &#8211;users_dburi=postgresql://@dbserver.example.com:45432/users </p>
<p> The templatized version would be<br/>
 &#8211;database-url=postgresql://@dbserver.example.com:45432/%(dbname)s</p>
<h2>OPTIONS</h2>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show this help message and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show program&#8217;s version number and exit</dd>
<dt><code>-o</code> <i>LM_ORDER</i>, <code>&#8211;login-managers-order</code> <i>LM_ORDER</i></dt>
<dd> Comma separated list of login managers</dd>
<dt><code>&#8211;hostname</code> <i>HOSTNAME</i></dt>
<dd> The hostname used by clients to reach this instance. This is used to determine the URLs provided in SAML metadata</dd>
<dt><code>&#8211;instance</code> <i>INSTANCE</i></dt>
<dd> Ipsilon instance name</dd>
<dt><code>&#8211;system-user</code> <i>SYSTEM_USER</dt>
<dd> User account used to run the server</dd>
<dt></i><code>&#8211;admin-user</code> <i>ADMIN_USER</i></dt>
<dd> User account that is assigned Ipsilon admin privileges</dd>
<dt><code>&#8211;database-url</code> <i>DATABASE_URL</i></dt>
<dd> The (templatized) database URL to use</dd>
<dt><code>&#8211;secure</code></dt>
<dd> Boolean to turn on all security checks</dd>
<dt><code>&#8211;server-debugging</code></dt>
<dd> Enable debugging</dd>
<dt><code>&#8211;uninstall</code></dt>
<dd> Uninstall the server and all data</dd>
<dt><code>&#8211;yes</code></dt>
<dd> Always answer yes</dd>
<dt><code>&#8211;admin-dburi</code> <i>ADMIN_DBURI</i></dt>
<dd> Configuration database URI (override template)</dd>
<dt><code>&#8211;users-dburi </code><i>USERS_DBURI</i></dt>
<dd> User configuration database URI (override template)</dd>
<dt><code>&#8211;transaction-dburi</code> <i>TRANSACTION_DBURI</i></dt>
<dd> Transaction database URI (override template)</dd></dl>
<h3>AUTHENTICATION PROVIDER OPTIONS</h3>
<dl>
<dt><code>&#8211;openid</code></dt>
<dd> Configure OpenID Provider</dd>
<dt><code>&#8211;openid-dburi</code> <i>OPENID_DBURI</i></dt>
<dd> OpenID database URI (override template)</dd>
<dt><code>&#8211;persona</code></dt>
<dd> Configure Persona Provider</dd>
<dt><code>&#8211;saml2</code></dt>
<dd> Configure SAML2 Provider</dd>
<dt><code>&#8211;saml2-metadata-validity</code> <i>SAML2_METADATA_VALIDITY</i></dt>
<dd> Metadata validity period in days (default &#8211; 1825) </dd>
</dl>
<h3>LOGIN MANAGER OPTIONS</h3>
<dl>
<dt><code>&#8211;form</code></dt>
<dd> Configure External Form authentication</dd>
<dt><code>&#8211;form-service</code> <i>FORM_SERVICE</i></dt>
<dd> PAM service name to use for authentication</dd>
<dt><code>&#8211;fas</code></dt>
<dd> Configure FAS (Fedora Authentication System) authentication</dd>
<dt><code>&#8211;ldap</code></dt>
<dd> Configure LDAP authentication</dd>
<dt><code>&#8211;ldap-server-url</code> <i>LDAP_SERVER_URL</i></dt>
<dd> LDAP Server Url</dd>
<dt><code>&#8211;ldap-bind-dn-template</code> <i>LDAP_BIND_DN_TEMPLATE</i></dt>
<dd> LDAP Bind DN Template</dd>
<dt><code>&#8211;ldap-tls-level</code> <i>LDAP_TLS_LEVEL</i></dt>
<dd> LDAP TLS level</dd>
<dt><code>&#8211;ldap-base-dn</code> <i>LDAP_BASE_DN</i></dt>
<dd> LDAP Base DN</dd>
<dt><code>&#8211;krb</code></dt>
<dd> Configure Kerberos authentication</dd>
<dt><code>&#8211;krb-httpd-keytab</code> <i>KRB_HTTPD_KEYTAB</i></dt>
<dd> Kerberos keytab location for HTTPD</dd>
<dt><code>&#8211;pam</code></dt>
<dd> Configure PAM authentication</dd>
<dt><code>&#8211;pam-service</code> <i>PAM_SERVICE</i></dt>
<dd> PAM service name to use for authentication</dd>
<dt><code>&#8211;testauth</code></dt>
<dd> Configure testing environment authentication </dd>
</dl>
<h3>INFO PROVIDER OPTIONS</h3>
<p> <code>&#8211;info-ldap</code> Use LDAP to populate user attrs</p>
<dl>
<dt><code>&#8211;info-ldap-server-url</code> <i>INFO_LDAP_SERVER_URL</i></dt>
<dd> LDAP Server Url</dd>
<dt><code>&#8211;info-ldap-bind-dn</code> <i>INFO_LDAP_BIND_DN</i></dt>
<dd> LDAP Bind DN</dd>
<dt><code>&#8211;info-ldap-bind-pwd</code> <i>INFO_LDAP_BIND_PWD</i></dt>
<dd> LDAP Bind Password</dd>
<dt><code>&#8211;info-ldap-user-dn-template</code> <i>INFO_LDAP_USER_DN_TEMPLATE</i></dt>
<dd> LDAP User DN Template</dd>
<dt><code>&#8211;info-ldap-base-dn</code> <i>INFO_LDAP_BASE_DN</i></dt>
<dd> LDAP Base DN</dd>
<dt><code>&#8211;info-nss</code></dt>
<dd> Use passwd data to populate user attrs</dd>
<dt><code>&#8211;info-sssd</code> <i></dt>
<dd> Use mod_lookup_identity and SSSD to populate user attrs. SSSD must be pre-configured for at least one domain.</dd>
<dt></i><code>&#8211;info-sssd-domain</code> <i>INFO_SSSD_DOMAIN</i></dt>
<dd> SSSD domain to enable mod_lookup_identity for (default is all) </dd>
</dl>
<h3>ENVIRONMENT HELPER OPTIONS</h3>
<p> <code>&#8211;ipa</code> Helper for IPA joined machines. This configures Ipsilon for Kerberos authentication.</p>
<h2>EXIT STATUS</h2>
<p> 0 if the installation was successful </p>
<p> 1 if an error occurred</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ipsilon/">ipsilon</a>(7),</code> <code><a href="/docs/linux/man/1-ipsilon-client-install/">ipsilon-client-install</a>(1)</code> </p>
