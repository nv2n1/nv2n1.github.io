---
title: "ipsilon-client-install(1)"
name: "ipsilon-client-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipsilon-client-install/"
description: "ipsilon-client-install – Configure an Ipsilon client"
---

<h2>NAME</h2>
<p> ipsilon-client-install &#8211; Configure an Ipsilon client</p>
<h2>SYNOPSIS</h2>
<p> ipsilon-client-install [OPTION]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Configures a server to be used as a Service Provider (SP) in federation with an Ipsilon instance as its Identity Provider (IdP). </p>
<p> By default, Apache is configured using mod_auth_mellon to handle the SAML 2 Federation.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code> Show help message and exit</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit</p>
<dt><code>&#8211;hostname</code> <i>HOSTNAME</i></p>
<dd> Machine&#8217;s fully qualified host name</p>
<dt><code>&#8211;port</code> PORT</p>
<dd> Port number that SP listens on. The default is to not set a specific listen port. The &#8211;saml-secure-setup option can affect this.</p>
<dt><code>&#8211;admin-user</code> <i>ADMIN_USER</i></p>
<dd> Account allowed to create a Service Provider (SP). The default is admin.</p>
<dt><code>&#8211;admin-password</code> <i>ADMIN_PASSWORD</i></p>
<dd> File containing the password for the account used toc reate a SP (- to read from stdin)</p>
<dt><code>&#8211;httpd-user</code> <i>HTTPD_USER</i></p>
<dd> Web server account used. Some files created by the installation will be <a href="/docs/linux/man/1-chown/">chown</a>(1) to this user. The default is apache.</p>
<dt><code>&#8211;saml</code></p>
<dd> Boolean value whether to install a saml2 SP or not. Default is True.</p>
<dt><code>&#8211;saml-idp-url</code> <i>SAML_IDP_URL</i></p>
<dd> An URL of the Ipsilon instance to register the SP with.</p>
<dt><code>&#8211;saml-idp-metadata</code> <i>SAML_IDP_METADATA</i></p>
<dd> An URL pointing at the IDP Metadata (FILE or HTTP)</p>
<dt><code>&#8211;saml-no-httpd</code></p>
<dd> Do not configure httpd. The default is False.</p>
<dt><code>&#8211;saml-base</code> <i>SAML_BASE</i></p>
<dd> Where saml2 authdata is available (default: /)</p>
<dt><code>&#8211;saml-auth</code> <i>SAML_AUTH</i></p>
<dd> Where saml2 authentication is enforced. The default is /saml2protected. This only applies when configuring Apache.</p>
<dt><code>&#8211;saml-sp</code> <i>SAML_SP</i></p>
<dd> Where saml communication happens. The default is /saml2.</p>
<dt><code>&#8211;saml-sp-logout</code> <i>SAML_SP_LOGOUT</i></p>
<dd> Single Logout URL. The default is /saml2/logout.</p>
<dt><code>&#8211;saml-sp-post</code> <i>SAML_SP_POST</i></p>
<dd> Post response URL. The default is /saml2/postResponse.</p>
<dt><code>&#8211;saml-secure-setup</code></p>
<dd> Turn on all security checks. The default is True.</p>
<dt><code>&#8211;saml-nameid</code></p>
<dd> The saml2 NameID format that this SP will use. Must be one of: x509,transient,persistent,windows,encrypted,kerberos,email,unspecified,entity. The default is unspecified.</p>
<dt><code>&#8211;saml-sp-name</code> <i>SAML_SP_NAME</i></p>
<dd> The SP name to register with the IdP.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn on script debugging</p>
<dt><code>&#8211;uninstall</code></p>
<dd> Uninstall the ipsilon client</dl>
<h2>CERTIFICATES</h2>
<p> Two levels of SSL certificates may be used in an Ipsilon instalation. </p>
<p> An X509 signing certificate is used by Ipsilon to sign SAML 2 messages. The public key of the certificate is passed in the SAML metadata exchanged between the Identity Provider and the Service Provider. This certificate and key are automatically generated. </p>
<p> Any page on the SP that will use the authentication provided by the IdP will need to be protected by SSL in order to access the secure cookie that the IdP provides. Ipsilon does not provide this certificate.</p>
<h2>EXAMPLES</h2>
<p> Install a SAML 2 SP using the IdP instance idp on idp.example.com. </p>
<p>#&nbsp;<wbr>ipsilon-client-install &#8211;saml-idp-metadata&nbsp;<wbr><a rel="nofollow" href="https://idp.example.com/idp/saml2/metadata">https://idp.example.com/idp/saml2/metadata</a>&nbsp;<wbr>&#8211;saml-auth&nbsp;<wbr>/protected </p>
<p> Any unauthenticated request to /protected will trigger a redirect to the IdP for authentication. </p>
<p> Once the SP has been generated it needs to be registered with the IdP.</p>
<h2>EXIT STATUS</h2>
<p> 0 if the installation was successful </p>
<p> 1 if an error occurred</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ipsilon/">ipsilon</a>(7)</code> </p>
<h2>Index</h2>
