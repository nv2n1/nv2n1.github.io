---
title: "nss_pcache(8)"
name: "nss_pcache"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nss_pcache/"
description: "nss_pcache – Helper program used to store token password pins"
---

<p>nss_pcache &#8211; Helper program used to store token password pins </p>
<h2>Synopsis</h2>
<p>nss_pcache &lt;semid&gt; &lt;fips on/off&gt; &lt;directory&gt; [prefix] </p>
<h2>Description</h2>
<p>A helper program used by the Apache <code>httpd</code> mod_nss plug-in to store the NSS PKCS #11 token password pins between restarts of Apache. Whenever an Apache <code>httpd</code> process configured to use the mod_nss plug-in is started, this program will be automatically invoked via reference to the mod_nss configuration file stored under <code>/etc/httpd/conf.d/nss.conf</code> which contains the following default entry:</p>
<dl>
<dd># Pass Phrase Helper:<br />
 # This helper program stores the token password pins between<br />
 # restarts of Apache.<br />
 #<br />
 # NOTE: Located at &#8216;/usr/sbin/nss_pcache&#8217; prior<br />
 # to &#8216;mod_nss-1.0.8-22&#8217;.<br />
 #<br />
 NSSPassPhraseHelper /usr/libexec/nss_pcache </p>
<h2>Options</h2>
<dl>
<dt><code>&lt;semid&gt;</code></p>
<dd>The semaphore which corresponds to the mod_nss plug-in registered with the Apache <code>httpd</code> process during startup.</p>
<dt><code>&lt;fips on/off&gt;</code></p>
<dd>Specifies whether FIPS mode should be enabled, <code>on</code>, or disabled, <code>off</code>. By default, FIPS mode is disabled, and no variable is specified in <code>/etc/httpd/conf.d/nss.conf</code>. To enable FIPS mode, establish password access for the specified NSS security databases, and specify the following variable in <code>/etc/httpd/conf.d/nss.conf</code>:</p>
<dd>
<table>
<tr VALIGN=top>
<td></td>
<td>NSSFIPS on
</td>
</tr>
</table>
<dt><code>&lt;directory&gt;</code></p>
<dd>Specifies the destination directory of the NSS databases that will be associated with this executable specified by the following entry in <code>/etc/httpd/conf.d/nss.conf</code>:</p>
<dd>
<table>
<tr VALIGN=top>
<td></td>
<td># Server Certificate Database:
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># The NSS security database directory that holds the
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># certificates and keys. The database consists
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># of 3 files: cert8.db, key3.db and secmod.db.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># Provide the directory that these files exist.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>NSSCertificateDatabase /etc/httpd/alias
</td>
</tr>
</table>
<dt><code>[prefix]</code></p>
<dd>Optional prefix to attach prior to the names of the NSS certificate and key databases contained in the directory referenced by the previous argument and specified by the following entry in <code>/etc/httpd/conf.d/nss.conf</code> (must be uncommented in order to be utilized):</p>
<dd>
<table>
<tr VALIGN=top>
<td></td>
<td># Database Prefix:
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># In order to be able to store multiple NSS databases
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># in one directory they need unique names. This option
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># sets the database prefix used for cert8.db and key3.db.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>#NSSDBPrefix my-prefix-
</td>
</tr>
</table>
</dl>
<h2>Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a> </p>
<h2>Authors</h2>
<p>Rob Crittenden &lt;rcritten [at] redhat.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2013 Red Hat, Inc. This is licensed under the Apache License, Version 2.0 (the &quot;License&quot;); no one may use this file except in compliance with the License. A copy of this license is available at <a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0.">http://www.apache.org/licenses/LICENSE-2.0.</a> </p>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
