---
title: "certmonger-dogtag-ipa-renew-agent-submit(8)"
name: "certmonger-dogtag-ipa-renew-agent-submit"
section: "8"
letter: "c"
url: "/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/"
description: "dogtag-ipa-renew-agent-submit"
---

<p>dogtag-ipa-renew-agent-submit</p>
<h2>Synopsis</h2>
<p>dogtag-ipa-renew-agent-submit -E EE-URL -A AGENT-URL [-d dbdir] [-n nickname] [-i cainfo] [-C capath] [-c certfile] [-k keyfile] [-p pinfile] [-P pin] [-s serial (hex)] [-D serial (decimal)] [-S state] [-T profile] [-O param=value] [-v] [csrfile] </p>
<h2>Description</h2>
<p><i>dogtag-ipa-renew-agent-submit</i> is the helper which <i>certmonger</i> uses to make certificate renewal requests to Dogtag instances running on IPA servers. It is not normally run interactively, but it can be for troubleshooting purposes. The preferred option is to request a renewal of an already-issued certificate, using its serial number, which can be read from a PEM-formatted certificate provided in the <i>CERTMONGER_CERTIFICATE</i> environment variable, or via the <code>-s</code> or <code>-D</code> option on the command line. If no serial number is provided, then the client will attempt to obtain a new certificate by submitting a signing request to the CA. The signing request which is to be submitted should either be in a file whose name is given as an argument, or fed into <i>dogtag-ipa-renew-agent-submit</i> via stdin. <code>certmonger</code> does not yet support retrieving trust information from Dogtag CAs. </p>
<h2>Options</h2>
<dl>
<dt><code>-E</code> EE-URL</p>
<dd>The top-level URL for the end-entity interface provided by the CA. In IPA installations, this is typically <i>http://</i><code>SERVER</code>:<code>EEPORT</code>/ca/ee/ca. If no URL is specified, the <i>host</i> named in the <i>[global]</i> section in the <i>/etc/ipa/default.conf</i> file is used as the value of <code>SERVER</code>, and the value of <code>EEPORT</code> will be inferred based on the value of the <i>dogtag_version</i> in the <i>[global]</i> section in the <i>/etc/ipa/default.conf</i> file: if <i>dogtag_version</i> is set to <i>10</i> or more, <code>EEPORT</code> will be set to 8080. Otherwise it will be 9180.</p>
<dt><code>-A</code> AGENT-URL</p>
<dd>The top-level URL for the agent interface provided by the CA. In IPA installations, this is typically <i>https://</i><code>SERVER</code>:<code>AGENTPORT</code>/ca/agent/ca. If no URL is specified, the <i>host</i> named in the <i>[global]</i> section in the <i>/etc/ipa/default.conf</i> file is used as the value of <code>SERVER</code>, and the value of <code>AGENTPORT</code> will be inferred based on the value of the <i>dogtag_version</i> in the <i>[global]</i> section in the <i>/etc/ipa/default.conf</i> file: if <i>dogtag_version</i> is set to <i>10</i> or more, <code>AGENTPORT</code> will be set to 8443. Otherwise it will be 9443.</p>
<dt><code>-d</code> dbdir <code>-n</code> nickname <code>-c</code> certfile <code>-k</code> keyfile</p>
<dd>The location of the key and certificate which the client should use to authenticate to the CA&#8217;s agent interface. Exactly which values are meaningful depend on which cryptography library your copy of libcurl was linked with. </p>
<p> If none of these options are specified, and none of the <code>-p</code>, <code>-P</code>, <code>-i</code>, nor <code>-C</code> options are specified, then this set of defaults is used:<br />
&nbsp;<wbr><code>-i</code>&nbsp;<wbr><i>/etc/ipa/ca.crt</i><br />
&nbsp;<wbr><code>-d</code>&nbsp;<wbr><i>/etc/httpd/alias</i><br />
&nbsp;<wbr><code>-n</code>&nbsp;<wbr><i>ipaCert</i><br />
&nbsp;<wbr><code>-p</code>&nbsp;<wbr><i>/etc/httpd/alias/pwdfile.txt</i></p>
<dt><code>-p</code> pinfile</p>
<dd>The name of a file which contains a PIN/password which will be needed in order to make use of the agent credentials. </p>
<p> If this option is not specified, and none of the <code>-d</code>, <code>-n</code>, <code>-c</code>, <code>-k</code>, <code>-P</code>, <code>-i</code>, nor <code>-C</code> options are specified, then this set of defaults is used:<br />
&nbsp;<wbr><code>-i</code>&nbsp;<wbr><i>/etc/ipa/ca.crt</i><br />
&nbsp;<wbr><code>-d</code>&nbsp;<wbr><i>/etc/httpd/alias</i><br />
&nbsp;<wbr><code>-n</code>&nbsp;<wbr><i>ipaCert</i><br />
&nbsp;<wbr><code>-p</code>&nbsp;<wbr><i>/etc/httpd/alias/pwdfile.txt</i></p>
<dt><code>-i</code> cainfo <code>-C</code> capath</p>
<dd>The location of a file containing a copy of the CA&#8217;s certificate, against which the CA server&#8217;s certificate will be verified, or a directory containing, among other things, such a file. </p>
<p> If these options are not specified, and none of the <code>-d</code>, <code>-n</code>, <code>-c</code>, <code>-k</code>, <code>-p</code>, nor <code>-P</code> options are specified, then this set of defaults is used:<br />
&nbsp;<wbr><code>-i</code>&nbsp;<wbr><i>/etc/ipa/ca.crt</i><br />
&nbsp;<wbr><code>-d</code>&nbsp;<wbr><i>/etc/httpd/alias</i><br />
&nbsp;<wbr><code>-n</code>&nbsp;<wbr><i>ipaCert</i><br />
&nbsp;<wbr><code>-p</code>&nbsp;<wbr><i>/etc/httpd/alias/pwdfile.txt</i></p>
<dt><code>-s</code> serial</p>
<dd>The serial number of an already-issued certificate for which the client should attempt to obtain a new certificate, in hexadecimal form, if one can not be read from the <i>CERTMONGER_CERTIFICATE</i> environment variable.</p>
<dt><code>-D</code> serial</p>
<dd>The serial number of an already-issued certificate for which the client should attempt to obtain a new certificate, in decimal form, if one can not be read from the <i>CERTMONGER_CERTIFICATE</i> environment variable.</p>
<dt><code>-S</code> state</p>
<dd>A cookie value provided by a previous instance of this helper, if the helper is being asked to continue a multi-step enrollment process. If the <i>CERTMONGER_COOKIE</i> environment variable is set, its value is used.</p>
<dt><code>-T</code> profile/template</p>
<dd>The name of the type of certificate which the client should request from the CA if it is not renewing a certificate (per the <code>-s</code> option above). If the <i>CERTMONGER_CA_PROFILE</i> environment variable is set, its value is used. Otherwise, the default value is <code>caServerCert</code>.</p>
<dt><code>-O</code> param=value</p>
<dd>An additional parameter to pass to the server when approving the signing request using the agent&#8217;s credentials. By default, any server-supplied default settings are applied. This option can be used either to override a server-supplied default setting, or to supply one which would otherwise have not been used.</p>
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
<h2>Files</h2>
<dl>
<dt><i>/etc/ipa/default.conf</i></p>
<dd>is the IPA client configuration file. This file is consulted to determine the URL for the Dogtag server&#8217;s end-entity and agent interfaces if they are not supplied as arguments. </p>
</dl>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
