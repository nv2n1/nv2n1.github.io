---
title: "certmonger-local-submit(8)"
name: "certmonger-local-submit"
section: "8"
letter: "c"
url: "/docs/linux/man/8-certmonger-local-submit/"
description: "local-submit"
---

<p>local-submit</p>
<h2>Synopsis</h2>
<p>local-submit [-d state-directory] [-v] [csrfile] </p>
<h2>Description</h2>
<p><i>local-submit</i> is the helper which <i>certmonger</i> uses to implement its local signer. It is not normally run interactively, but it can be for troubleshooting purposes. The signing request which is to be submitted should either be in a file whose name is given as an argument, or fed into <i>local-submit</i> via stdin. The local signer is currently hard-coded to generate and use a 2048-bit RSA key and a name and initial serial number based on a UUID, replacing that key and certificate at roughly the midpoint of their useful lifetime. <code>certmonger</code> supports retrieving the list of current and previously-used local CA certificates. See <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) and <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) for information about specifying where those certificates should be stored. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code> state-directory</p>
<dd>Identifies the directory which contains the local signer&#8217;s private key, certificates, and other data used by the local signer.</p>
<dt><code>-v</code></p>
<dd>Increases the verbosity of the tool&#8217;s diagnostic logging. </p>
</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>if the certificate was issued. The new certificate will be printed.</p>
<dt>3</p>
<dd>if the helper needs to be called again. An error message may be printed.</p>
<dt>4</p>
<dd>if critical configuration information is missing. An error message may be printed. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>creds</i></p>
<dd>is currently a PKCS#12 bundle containing the local signer&#8217;s current signing key and current and previously-used signer certificates. It should not be modified except by the local signer. A new key is currently generated when ever a new signer certificate is needed.</p>
<dt><i>serial</i></p>
<dd>currently contains the serial number which will be used for the next issued certificate. It should not be modified except by the local signer. </p>
</dl>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
