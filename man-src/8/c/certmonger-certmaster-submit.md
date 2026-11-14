---
title: "certmonger-certmaster-submit(8)"
name: "certmonger-certmaster-submit"
section: "8"
letter: "c"
url: "/docs/linux/man/8-certmonger-certmaster-submit/"
description: "certmaster-submit"
---

<p>certmaster-submit</p>
<h2>Synopsis</h2>
<p>certmaster-submit [-h serverHost] [-c cafile] [-C capath] [csrfile] </p>
<h2>Description</h2>
<p><i>certmaster-submit</i> is the helper which <i>certmonger</i> uses to make requests to certmaster-based CAs. It is not normally run interactively, but it can be for troubleshooting purposes. The signing request which is to be submitted should either be in a file whose name is given as an argument, or fed into <i>certmaster-submit</i> via stdin. There is no standard authenticated method for obtaining the root certificate from certmaster CAs, so <code>certmonger</code> does not support retrieving trust information from them. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> serverHost</p>
<dd>Submit the request to the certmaster instance running on the named host. The default is <i>localhost:51235</i> if a file named <code>/var/run/certmaster.pid</code> is found on the local system, and is read from <code>/etc/certmaster/minion.conf</code> if that file is not found.</p>
<dt><code>-c</code> cafile</p>
<dd>Submit the request over HTTPS instead of HTTP, and only trust the server if its certificate was issued by the CA whose certificate is in the named file.</p>
<dt><code>-C</code> capath</p>
<dd>Submit the request over HTTPS instead of HTTP, and only trust the server if its certificate was issued by a CA whose certificate is in a file in the named directory. </p>
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
<dd>if critical configuration information is missing. An error message may be printed. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/run/certmaster.pid</i></p>
<dd>the certmaster service&#8217;s PID file. Its presence is taken to indicate that this system is a CA, and that requests should be submitted to a certmaster server running on the local system.</p>
<dt><i>/etc/certmaster/minion.conf</i></p>
<dd>the certmaster minion configuration file. If there is no indication that the local system is a certmaster server, then this file is consulted to determine the location of the certmaster server. </p>
</dl>
<h2>Known Bugs</h2>
<p>Checking for the existence of certmaster&#8217;s PID file is a terrible way to figure out whether we&#8217;re a minion or not.</p>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
