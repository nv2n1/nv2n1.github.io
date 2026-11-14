---
title: "certmonger-dogtag-submit(8)"
name: "certmonger-dogtag-submit"
section: "8"
letter: "c"
url: "/docs/linux/man/8-certmonger-dogtag-submit/"
description: "dogtag-submit"
---

<p>dogtag-submit</p>
<h2>Synopsis</h2>
<p>dogtag-submit -E EE-URL -A AGENT-URL [-d dbdir] [-n nickname] [-i cainfo] [-C capath] [-c certfile] [-k keyfile] [-p pinfile] [-P pin] [-s serial (hex)] [-D serial (decimal)] [-S state] [-T profile] [-O param=value] [-N | -R] [-o option=value] [-a ] [-u username] [-U userdn] [-W userpassword] [-w userpasswordfile] [-Y userpin] [-y userpinfile] [-v] [csrfile] </p>
<h2>Description</h2>
<p><i>dogtag-submit</i> is the helper which <i>certmonger</i> can use to make certificate enrollment and renewal requests to Dogtag servers. It is not normally run interactively, but it can be for troubleshooting purposes. The preferred option is to request a renewal of an already-issued certificate, using its serial number, which can be read from a PEM-formatted certificate provided in the <i>CERTMONGER_CERTIFICATE</i> environment variable, or via the <code>-s</code> or <code>-D</code> option on the command line. If no serial number is provided, then the client will attempt to obtain a new certificate by submitting a signing request to the CA. The signing request which is to be submitted should either be in a file whose name is given as an argument, or fed into <i>dogtag-submit</i> via stdin. <code>certmonger</code> does not yet support retrieving trust information from Dogtag CAs. </p>
<h2>Options</h2>
<dl>
<dt><code>-E</code> EE-URL</p>
<dd>The top-level URL for the end-entity interface provided by the CA, through which the initial enrollment request will be submitted. This is typically <i>http://</i><code>SERVER</code>:<code>EEPORT</code>/ca/ee/ca.</p>
<dt><code>-A</code> AGENT-URL</p>
<dd>The top-level URL for the agent interface provided by the CA, through which the request can be approved using agent credentials. This is typically <i>https://</i><code>SERVER</code>:<code>AGENTPORT</code>/ca/agent/ca.</p>
<dt><code>-d</code> dbdir <code>-n</code> nickname <code>-c</code> certfile <code>-k</code> keyfile</p>
<dd>The location of the key and certificate which the client should use to authenticate to the CA&#8217;s agent interface. Exactly which values are meaningful depend on which cryptography library your copy of libcurl was linked with.</p>
<dt><code>-p</code> pinfile</p>
<dd>The name of a file which contains a PIN/password which will be needed in order to make use of the agent credentials.</p>
<dt><code>-i</code> cainfo <code>-C</code> capath</p>
<dd>The location of a file containing a copy of the CA&#8217;s certificate, against which the CA server&#8217;s certificate will be verified, or a directory containing, among other things, such a file.</p>
<dt><code>-s</code> serial</p>
<dd>The serial number of an already-issued certificate for which the client should attempt to obtain a new certificate, in hexadecimal form, if one can not be read from the <i>CERTMONGER_CERTIFICATE</i> environment variable.</p>
<dt><code>-D</code> serial</p>
<dd>The serial number of an already-issued certificate for which the client should attempt to obtain a new certificate, in decimal form, if one can not be read from the <i>CERTMONGER_CERTIFICATE</i> environment variable.</p>
<dt><code>-S</code> state</p>
<dd>A cookie value provided by a previous instance of this helper, if the helper is being asked to continue a multi-step enrollment process. If the <i>CERTMONGER_COOKIE</i> environment variable is set, its value is used.</p>
<dt><code>-T</code> profile</p>
<dd>The name of the type of certificate which the client should request from the CA if it is not renewing a certificate (per the <code>-s</code> option above). If the <i>CERTMONGER_CA_PROFILE</i> environment variable is set, its value is used. Otherwise, the default value is <code>caServerCert</code>.</p>
<dt><code>-O</code> param=value</p>
<dd>An additional parameter to pass to the server when approving the signing request using agent credentials. By default, any server-supplied default settings are applied. This option can be used either to override a server-supplied default setting, or to supply one which would otherwise have not been used. Requires the <code>-A</code> option.</p>
<dt><code>-N</code></p>
<dd>Even if an already-issued certificate is available in the <i>CERTMONGER_CERTIFICATE</i> environment variable, or a serial number has been provided, don&#8217;t attempt to renew a certificate using its serial number. Instead, attempt to obtain a new certificate using the signing request.</p>
<dt><code>-R</code></p>
<dd>Negates the effect of the <code>-N</code> flag.</p>
<dt><code>-t</code></p>
<dd>Instead of attempting to obtain a new certificate, query the server for a list of the enabled enrollment profiles.</p>
<dt><code>-o</code> param=value</p>
<dd>When initially submitting a request to the CA, add the specified parameter and value along with any request parameters which would otherwise be sent.</p>
<dt><code>-a</code></p>
<dd>Use agent credentials, specified using some combination of the <code>-d</code>, <code>-n</code>, <code>-c</code>, and <code>-k</code> flags, to authenticate to the CA when initially submitting a request to the CA or retrieving the list of enabled enrollment profiles. This is typically required when the enrollment profile being used uses <i>AgentCertAuth</i>-based authentication, and requires that the URL specified using the <code>-E</code> flag be an HTTPS URL, or when the URL specified using the <code>-E</code> flag is an HTTPS URL.</p>
<dt><code>-u username</code></p>
<dd>When initially submitting a request to the CA, supply the specified value as a user name. This is typically required when the enrollment profile being used uses <i>UidPwdDirAuth</i>-based or <i>NISAuth</i>-based authentication.</p>
<dt><code>-U userdn</code></p>
<dd>When initially submitting a request to the CA, supply the specified value as the DN (distinguished name) of the user&#8217;s entry in a directory server which the CA is configured to use for checking the user&#8217;s password. This is typically required when the enrollment profile being used uses <i>UdnPwdDirAuth</i>-based authentication.</p>
<dt><code>-W userpassword</code></p>
<dd>When initially submitting a request to the CA, supply the specified value as the password for the user whose name is specified with the <code>-u</code> option, or whose DN is specified with the <code>-U</code> option. This is typically only required when the enrollment profile being used uses <i>UidPwdDirAuth</i>-based, <i>UserPwdDirAuth</i>-based, or <i>NISAuth</i>-based authentication. If the URL specified using the <code>-E</code> flag is not an HTTPS URL, this value will not be encrypted.</p>
<dt><code>-w userpasswordfile</code></p>
<dd>When initially submitting a request to the CA, read from the specified file a password to supply for the user whose name is specified with the <code>-u</code> option, or whose DN is specified with the <code>-U</code> option. This is typically only required when the enrollment profile being used uses <i>UidPwdDirAuth</i>-based, <i>UserPwdDirAuth</i>-based, or <i>NISAuth</i>-based authentication. If the URL specified using the <code>-E</code> flag is not an HTTPS URL, this value will not be encrypted.</p>
<dt><code>-Y userpin</code></p>
<dd>When initially submitting a request to the CA, supply the specified value as the PIN for the user whose name is specified with the <code>-u</code> option, or whose DN is specified with the <code>-U</code> option. This is typically only required when the enrollment profile being used uses <i>UidPwdPinDirAuth</i>-based authentication. If the URL specified using the <code>-E</code> flag is not an HTTPS URL, this value will not be encrypted.</p>
<dt><code>-y userpinfile</code></p>
<dd>When initially submitting a request to the CA, read from the specified file a PIN to supply for the user whose name is specified with the <code>-u</code> option, or whose DN is specified with the <code>-U</code> option. This is typically only required when the enrollment profile being used uses <i>UidPwdPinDirAuth</i>-based authentication. If the URL specified using the <code>-E</code> flag is not an HTTPS URL, this value will not be encrypted.</p>
<dt><code>-v</code></p>
<dd>Increases the logging level. Use twice for more logging. This option is mainly useful for troubleshooting. </p>
</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>if the certificate was issued. The certificate will be printed.</p>
<dt>1</p>
<dd>if the CA is still thinking. A cookie (state) value will be printed.</p>
<dt>2</p>
<dd>if the CA rejected the request. An error message may be printed.</p>
<dt>3</p>
<dd>if the CA was unreachable. An error message may be printed.</p>
<dt>4</p>
<dd>if critical configuration information is missing. An error message may be printed.</p>
<dt>5</p>
<dd>if the CA is still thinking. A suggested poll delay (specified in seconds) and a cookie (state) value will be printed.</p>
<dt>17</p>
<dd>if the CA indicates that the client needs to attempt enrollment using a new key pair. </p>
</dl>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
