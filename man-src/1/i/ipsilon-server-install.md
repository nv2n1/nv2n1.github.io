---
title: "ipsilon-server-install(1)"
name: "ipsilon-server-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipsilon-server-install/"
description: "ipsilon-server-install – Configure an Ipsilon Identity Provider instance"
---

<h2>NAME</h2>
<p> ipsilon-server-install &#8211; Configure an Ipsilon Identity Provider instance</p>
<h2>SYNOPSIS</h2>
<p> ipsilon-server-install [OPTION]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Configure an Ipsilon instance to provide identity services using any of the supported and enabled protocols. </p>
<p> Ipsilon uses a plugable framework so some options may not be available, depending on what plugins have been installed. </p>
<p> Ipsilon supports three types of plugins: </p>
<p> 1. Authentication provider plugins &#8211; implements an authentication protocol such as SAML 2, OpenID or Persona. At least one needs to be enabled.<br />
 2. Login plugins &#8211; mechanisms for authenticating including GSSAPI, LDAP, PAM, etc. At least one should be enabled.<br />
 3. Info plugins &#8211; sources where additional attributes of the user may be obtained. </p>
<p> There are also environment helper options which aid in configuring the Identity Provider for a particular environment, such as a FreeIPA domain. </p>
<p> The installation details are logged to /var/log/ipsilon-install.log.</p>
<h2>DATABASES</h2>
<p> Ipsilon stores configuration and session information in database tables. By default, a set of sqlite databases are used. If a full RDBMS is desired then the <code>&#8211;database-url</code> and/or <code>*-dburi</code> options can be used to provide the database URIs. This should probably be used in load-balanced situations so all servers can use the same database. </p>
<p> An example of a specific URI is<br />
 &#8211;users_dburi=postgresql://@dbserver.example.com:45432/users </p>
<p> The templatized version would be<br />
 &#8211;database-url=postgresql://@dbserver.example.com:45432/%(dbname)s</p>
<h2>OPTIONS</h2>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit</p>
<dt><code>-o</code> <i>LM_ORDER</i>, <code>&#8211;login-managers-order</code> <i>LM_ORDER</i></p>
<dd> Comma separated list of login managers</p>
<dt><code>&#8211;hostname</code> <i>HOSTNAME</i></p>
<dd> The hostname used by clients to reach this instance. This is used to determine the URLs provided in SAML metadata</p>
<dt><code>&#8211;instance</code> <i>INSTANCE</i></p>
<dd> Ipsilon instance name</p>
<dt><code>&#8211;system-user</code> <i>SYSTEM_USER</p>
<dd> User account used to run the server</p>
<dt></i><code>&#8211;admin-user</code> <i>ADMIN_USER</i></p>
<dd> User account that is assigned Ipsilon admin privileges</p>
<dt><code>&#8211;database-url</code> <i>DATABASE_URL</i></p>
<dd> The (templatized) database URL to use</p>
<dt><code>&#8211;secure</code></p>
<dd> Boolean to turn on all security checks</p>
<dt><code>&#8211;server-debugging</code></p>
<dd> Enable debugging</p>
<dt><code>&#8211;uninstall</code></p>
<dd> Uninstall the server and all data</p>
<dt><code>&#8211;yes</code></p>
<dd> Always answer yes</p>
<dt><code>&#8211;admin-dburi</code> <i>ADMIN_DBURI</i></p>
<dd> Configuration database URI (override template)</p>
<dt><code>&#8211;users-dburi </code><i>USERS_DBURI</i></p>
<dd> User configuration database URI (override template)</p>
<dt><code>&#8211;transaction-dburi</code> <i>TRANSACTION_DBURI</i></p>
<dd> Transaction database URI (override template)</dl>
<h3>AUTHENTICATION PROVIDER OPTIONS</h3>
<dl>
<dt><code>&#8211;openid</code></p>
<dd> Configure OpenID Provider</p>
<dt><code>&#8211;openid-dburi</code> <i>OPENID_DBURI</i></p>
<dd> OpenID database URI (override template)</p>
<dt><code>&#8211;persona</code></p>
<dd> Configure Persona Provider</p>
<dt><code>&#8211;saml2</code></p>
<dd> Configure SAML2 Provider</p>
<dt><code>&#8211;saml2-metadata-validity</code> <i>SAML2_METADATA_VALIDITY</i></p>
<dd> Metadata validity period in days (default &#8211; 1825) </p>
</dl>
<h3>LOGIN MANAGER OPTIONS</h3>
<dl>
<dt><code>&#8211;form</code></p>
<dd> Configure External Form authentication</p>
<dt><code>&#8211;form-service</code> <i>FORM_SERVICE</i></p>
<dd> PAM service name to use for authentication</p>
<dt><code>&#8211;fas</code></p>
<dd> Configure FAS (Fedora Authentication System) authentication</p>
<dt><code>&#8211;ldap</code></p>
<dd> Configure LDAP authentication</p>
<dt><code>&#8211;ldap-server-url</code> <i>LDAP_SERVER_URL</i></p>
<dd> LDAP Server Url</p>
<dt><code>&#8211;ldap-bind-dn-template</code> <i>LDAP_BIND_DN_TEMPLATE</i></p>
<dd> LDAP Bind DN Template</p>
<dt><code>&#8211;ldap-tls-level</code> <i>LDAP_TLS_LEVEL</i></p>
<dd> LDAP TLS level</p>
<dt><code>&#8211;ldap-base-dn</code> <i>LDAP_BASE_DN</i></p>
<dd> LDAP Base DN</p>
<dt><code>&#8211;krb</code></p>
<dd> Configure Kerberos authentication</p>
<dt><code>&#8211;krb-httpd-keytab</code> <i>KRB_HTTPD_KEYTAB</i></p>
<dd> Kerberos keytab location for HTTPD</p>
<dt><code>&#8211;pam</code></p>
<dd> Configure PAM authentication</p>
<dt><code>&#8211;pam-service</code> <i>PAM_SERVICE</i></p>
<dd> PAM service name to use for authentication</p>
<dt><code>&#8211;testauth</code></p>
<dd> Configure testing environment authentication </p>
</dl>
<h3>INFO PROVIDER OPTIONS</h3>
<p> <code>&#8211;info-ldap</code> Use LDAP to populate user attrs</p>
<dl>
<dt><code>&#8211;info-ldap-server-url</code> <i>INFO_LDAP_SERVER_URL</i></p>
<dd> LDAP Server Url</p>
<dt><code>&#8211;info-ldap-bind-dn</code> <i>INFO_LDAP_BIND_DN</i></p>
<dd> LDAP Bind DN</p>
<dt><code>&#8211;info-ldap-bind-pwd</code> <i>INFO_LDAP_BIND_PWD</i></p>
<dd> LDAP Bind Password</p>
<dt><code>&#8211;info-ldap-user-dn-template</code> <i>INFO_LDAP_USER_DN_TEMPLATE</i></p>
<dd> LDAP User DN Template</p>
<dt><code>&#8211;info-ldap-base-dn</code> <i>INFO_LDAP_BASE_DN</i></p>
<dd> LDAP Base DN</p>
<dt><code>&#8211;info-nss</code></p>
<dd> Use passwd data to populate user attrs</p>
<dt><code>&#8211;info-sssd</code> <i></p>
<dd> Use mod_lookup_identity and SSSD to populate user attrs. SSSD must be pre-configured for at least one domain.</p>
<dt></i><code>&#8211;info-sssd-domain</code> <i>INFO_SSSD_DOMAIN</i></p>
<dd> SSSD domain to enable mod_lookup_identity for (default is all) </p>
</dl>
<h3>ENVIRONMENT HELPER OPTIONS</h3>
<p> <code>&#8211;ipa</code> Helper for IPA joined machines. This configures Ipsilon for Kerberos authentication.</p>
<h2>EXIT STATUS</h2>
<p> 0 if the installation was successful </p>
<p> 1 if an error occurred</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ipsilon/">ipsilon</a>(7),</code> <code><a href="/docs/linux/man/1-ipsilon-client-install/">ipsilon-client-install</a>(1)</code> </p>
<h2>Index</h2>
