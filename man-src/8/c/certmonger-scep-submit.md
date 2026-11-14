---
title: "certmonger-scep-submit(8)"
name: "certmonger-scep-submit"
section: "8"
letter: "c"
url: "/docs/linux/man/8-certmonger-scep-submit/"
description: "scep-submit"
---

<p>scep-submit</p>
<h2>Synopsis</h2>
<p>scep-submit -u SERVER-URL [-r ra-cert-file] [-R ca-cert-file] [-I other-certs-file] [-i ca-identifier] [-v] [-n] [-c|-C|-g|-p] [pkimessage-filename] </p>
<h2>Description</h2>
<p><i>scep-submit</i> is the helper which <i>certmonger</i> can use to transmit certificate enrollment and renewal requests to servers using SCEP. It is not normally run interactively, but it can be for troubleshooting purposes. The request which is to be submitted should be a PEM-encoded SCEP pkiMessage either in a file whose name is given as an argument, or fed into <i>scep-submit</i> via stdin. </p>
<h2>Modes</h2>
<dl>
<dt><code>-c</code></p>
<dd><i>scep-submit</i> will issue a <i>GetCACaps</i> request to the server and print the results.</p>
<dt><code>-C</code></p>
<dd><i>scep-submit</i> will issue <i>GetCACert</i> and <i>GetCAChain</i> requests to the server, parse the responses, and then print, in order, the RA certificate, the CA certificate, and any additional certificates.</p>
<dt><code>-p</code></p>
<dd><i>scep-submit</i> will issue a <i>PKIOperation</i> request to the server using the passed-in message as the message content. It will parse the server&#8217;s response, verify the signature, and if the response includes an issued certificate, it will output the <i>pkcsPKIEnvelope</i> in PEM format. If the response indicates an error, it will print the error.</p>
<dt><code>-g</code></p>
<dd><i>scep-submit</i> will issue a <i>PKIOperation</i> request to the server using the passed-in message as the message content. It will parse the server&#8217;s response, verify the signature, and if the response includes an issued certificate, it will output the <i>pkcsPKIEnvelope</i> in PEM format. If the response indicates an error, it will print the error.</dl>
<h2>Options</h2>
<dl>
<dt><code>-u</code> SERVER-URL</p>
<dd>The location of the SCEP interface provided by the CA. This is typically <i>http://</i><code>SERVER</code>/cgi-bin/PKICLIENT.EXE or <i>http://</i><code>SERVER</code>/certsrv/mscep/mscep.dll. This option is always required.</p>
<dt><code>-R</code> CA-certificate-file</p>
<dd>The location of the SCEP server&#8217;s CA certificate, which was used to issue the SCEP server&#8217;s certificate, or the SCEP server&#8217;s own certificate, if it is self-signed, in PEM form. If the URL specified with the <code>-u</code> option is an <i>https</i> URL, then this option is required.</p>
<dt><code>-r</code> RA-certificate-file</p>
<dd>The location of the SCEP server&#8217;s RA certificate, which is expected to be used for signing responses sent by the SCEP server back to the client. This option is required when either the <code>-g</code> flag or the <code>-p</code> flag is specified.</p>
<dt><code>-I</code> other-certificates-file</p>
<dd>The location of a file containing other PEM-formatted certificates which may be needed in order to properly verify signed responses sent by the SCEP server back to the client. This option may be necessary when either the <code>-g</code> flag or the <code>-p</code> flag is specified.</p>
<dt><code>-i</code> ca-identifier</p>
<dd>When called with the <code>-c</code> or <code>-C</code> flag, this option can be used to specify the CA identifier which is passed to the server as part of the client&#8217;s request. The default is &quot;0&quot;.</p>
<dt><code>-v</code></p>
<dd>Increases the logging level. Use twice for more logging. This option is mainly useful for troubleshooting. </p>
</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>if the certificate was issued. The pkcsPKIEnvelope will be printed in PEM-encoded form.</p>
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
<dt>16</p>
<dd>if the helper needs an SCEP pkiMessage, but couldn&#8217;t read one.</p>
<dt>17</p>
<dd>if the CA indicates that the client needs to attempt enrollment using a new key pair. </p>
</dl>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
