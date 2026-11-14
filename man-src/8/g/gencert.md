---
title: "gencert(8)"
name: "gencert"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gencert/"
description: "gencert – Generate a test NSS database for mod_nss"
---

<p>gencert &#8211; Generate a test NSS database for mod_nss </p>
<h2>Synopsis</h2>
<p>gencert &lt;destdir&gt; </p>
<h2>Description</h2>
<p>A tool used to generate a self-signed CA as well as server and user certificates for mod_nss testing. This is used to generate a default NSS database for the mod_nss Apache module. It does not test to see if an existing database already exists, so use with care. <code>gencert</code> will generate a new NSS database with the password &quot;httptest&quot;. It generates a self-signed CA with the subject &quot;CN=Certificate Shack, O=example.com, C=US&quot; It also generates a certificate suitable for servers with the subject &quot;CN=&lt;FQDN&gt;, O=example.com, C=US&quot;, and a user certificate with the subject &quot;E=alpha@&lt;FQDN&gt;, CN=Frank Alpha, UID=alpha, OU=People, O=example.com, C=US&quot;. The nicknames it uses are:</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>CA:</td>
<td>cacert
</td>
</tr>
<tr VALIGN=top>
<td>Server certificate:</td>
<td>Server-Cert
</td>
</tr>
<tr VALIGN=top>
<td>User cert:</td>
<td>alpha
</td>
</tr>
</table>
<h2>Options</h2>
<dl>
<dt><code>&lt;destdir&gt;</code></p>
<dd>Specifies the destination directory where the NSS databases will be created. </p>
</dl>
<h2>Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a> </p>
<h2>Authors</h2>
<p>Rob Crittenden &lt;rcritten [at] redhat.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2011 Red Hat, Inc. This is licensed under the Apache License, Version 2.0 (the &quot;License&quot;); no one may use this file except in compliance with the License. A copy of this license is available at <a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0.">http://www.apache.org/licenses/LICENSE-2.0.</a> </p>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
