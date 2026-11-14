---
title: "update-crypto-policies(8)"
name: "update-crypto-policies"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-crypto-policies/"
description: "update-crypto-policies – manage the policies available to the various cryptographic back-ends."
---

<p>update-crypto-policies &#8211; manage the policies available to the various cryptographic back-ends.</p>
<h2>Synopsis</h2>
<p><code>update-crypto-policies</code> [<i>COMMAND</i>]</p>
<h2>Description</h2>
<p><a href="/docs/linux/man/8-update-crypto-policies/">update-crypto-policies</a>(8) is used to set the policy applicable for the various cryptographic back-ends, such as SSL/TLS libraries. That will be the default policy used by these back-ends unless the application user configures them otherwise. </p>
<p> The available policies are restricted to the following three profiles. </p>
<dl>
<dd>&bull; LEGACY: ensures maximum compatibility with legacy systems (64-bit security)</dl>
<dl>
<dd>&bull; DEFAULT: A reasonable default for today&#8217;s standards (80-bit security).</dl>
<dl>
<dd>&bull; FUTURE: A level that will provide security on a conservative level that is believed to withstand any near-term future attacks (112-bit security).</dl>
<p> The desired system policy is selected in /etc/crypto-profiles/config and this tool will generate the individual policy requirements for all back-ends that support such configuration. After this tool is called the administrator is assured that any application that utilizes the supported back-ends will policy that adheres to the configured profile. </p>
<p> The generated back-end policies will be placed in /etc/crypto-profiles/back-ends. Currently the supported back-ends are: </p>
<dl>
<dd>&bull; GnuTLS library</dl>
<dl>
<dd>&bull; OpenSSL library</dl>
<dl>
<dd>&bull; BIND</dl>
<h2>Compatibility</h2>
<p>Policies that were present in previously released Fedora systems will be available using the -FXX suffix, where XX is the Fedora version. For example the LEGACY policy in Fedora 21 will also be available as LEGACY-F21.</p>
<h2>Application Support</h2>
<p>Applications shipped by Fedora that provide a default configuration file that includes a cryptographic policy string will be modified gradually to support these policies. </p>
<p> When an application provides a configuration file, the changes needed to utilize the system-wide policy are the following. </p>
<dl>
<dd>&bull; Applications using GnuTLS: The special priority string &quot;@SYSTEM&quot; should replace any other priority string.</dl>
<dl>
<dd>&bull; Applications using OpenSSL: The special cipher string &quot;PROFILE=SYSTEM&quot; should replace any other cipher string.</dl>
<p> In all cases if the application isn&#8217;t using a particular setting, e.g., using gnutls_priority_set_default() in GnuTLS, or no specific cipher string setting in OpenSSL, no other changes are required. The system-wide string will be used automatically.</p>
<h2>Policy Configuration</h2>
<p>One of the supported profiles should be set in /etc/crypto-profiles/config and this script should be run afterwards. </p>
<p> In case of a parsing error no policies will be updated.</p>
<h2>Files</h2>
<p>/etc/crypto-profiles/config</p>
<dl>
<dd>The file contains the current system policy. It should contain a string of one of the profiles listed above (e.g., DEFAULT).</dl>
<p> /etc/crypto-profiles/back-ends</p>
<dl>
<dd>Contains the generated policies in separated files, and in a format readable by the supported back-ends.</dl>
<h2>Author</h2>
<p>Written by Nikos Mavrogiannopoulos.</p>
