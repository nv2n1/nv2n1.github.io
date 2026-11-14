---
title: "certmonger-ipa-submit(8)"
name: "certmonger-ipa-submit"
section: "8"
letter: "c"
url: "/docs/linux/man/8-certmonger-ipa-submit/"
description: "ipa-submit"
---

<p>ipa-submit</p>
<h2>Synopsis</h2>
<p>ipa-submit [-h serverHost] [-H serverURL] [-c cafile] [-C capath] [[-K] | [-t keytab] [-k submitterPrincipal]] [-P principalOfRequest] [-T profile] [csrfile] </p>
<h2>Description</h2>
<p><i>ipa-submit</i> is the helper which <i>certmonger</i> uses to make requests to IPA-based CAs. It is not normally run interactively, but it can be for troubleshooting purposes. The signing request which is to be submitted should either be in a file whose name is given as an argument, or fed into <i>ipa-submit</i> via stdin. <code>certmonger</code> supports retrieving trusted certificates from IPA CAs. See <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) and <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) for information about specifying where those certificates should be stored on the local system. Trusted certificates are retrieved from the <code>caCertificate</code> attribute of entries present at and below <i>cn=cacert,cn=ipa,cn=etc,</i>$BASE in the IPA LDAP server&#8217;s directory tree, where $BASE defaults to the value of the <code>basedn</code> setting in <code>/etc/ipa/default.conf</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-P</code> csrPrincipal</p>
<dd>Identifies the principal name of the service for which the certificate is being issued. This setting is required by IPA and must always be specified.</p>
<dt><code>-X</code> issuer</p>
<dd>Requests that the certificate be processed by the specified certificate issuer. By default, if this flag is not specified, and the <code>CERTMONGER_CA_ISSUER</code> variable is set in the environment, then the value of the environment variable will be used. This setting is optional, and if a server returns error 3005, indicating that it does not understand multiple profiles, the request will be re-submitted without specifying an issuer name.</p>
<dt><code>-T</code> profile</p>
<dd>Requests that the certificate be processed using the specified certificate profile. By default, if this flag is not specified, and the <code>CERTMONGER_CA_PROFILE</code> variable is set in the environment, then the value of the environment variable will be used. This setting is optional, and if a server returns error 3005, indicating that it does not understand multiple profiles, the request will be re-submitted without specifying a profile.</p>
<dt><code>-h</code> serverHost</p>
<dd>Submit the request to the IPA server running on the named host. The default is to read the location of the host from <code>/etc/ipa/default.conf</code>.</p>
<dt><code>-H</code> serverURL</p>
<dd>Submit the request to the IPA server at the specified location. The default is to read the location of the host from <code>/etc/ipa/default.conf</code>.</p>
<dt><code>-c</code> cafile</p>
<dd>The server&#8217;s certificate was issued by the CA whose certificate is in the named file. The default value is <i>/etc/ipa/ca.crt</i>.</p>
<dt><code>-C</code> capath</p>
<dd>Trust the server if its certificate was issued by a CA whose certificate is in a file in the named directory. There is no default for this option, and it is not expected to be necessary.</p>
<dt><code>-t</code> keytab</p>
<dd>Authenticate to the IPA server using credentials derived from keys stored in the named keytab. The default value can vary, but it is usually <i>/etc/krb5.keytab</i>. This option conflicts with the <code>-K</code> option.</p>
<dt><code>-k</code> authPrincipal</p>
<dd>Authenticate to the IPA server using credentials derived from keys stored in the named keytab for this principal name. The default value is the <code>host</code> service for the local host in the local realm. This option conflicts with the <code>-K</code> option.</p>
<dt><code>-K</code></p>
<dd>Authenticate to the IPA server using credentials derived from the default credential cache rather than a keytab. This option conflicts with the <code>-k</code> option. </p>
</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>if the certificate was issued. The certificate will be printed.</p>
<dt>1</p>
<dd>if the CA is still thinking. A cookie value will be printed.</p>
<dt>2</p>
<dd>if the CA rejected the request. An error message may be printed.</p>
<dt>3</p>
<dd>if the CA was unreachable. An error message may be printed.</p>
<dt>4</p>
<dd>if critical configuration information is missing. An error message may be printed.</p>
<dt>17</p>
<dd>if the CA indicates that the client needs to attempt enrollment using a new key pair. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/ipa/default.conf</i></p>
<dd>is the IPA client configuration file. This file is consulted to determine the URL for the IPA server&#8217;s XML-RPC interface. </p>
</dl>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
