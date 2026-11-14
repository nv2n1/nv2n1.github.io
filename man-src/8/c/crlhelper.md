---
title: "crlhelper(8)"
name: "crlhelper"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crlhelper/"
description: "crlhelper – Helper program used to store-and-forward CRLs"
---

<p>crlhelper &#8211; Helper program used to store-and-forward CRLs </p>
<h2>Synopsis</h2>
<p>crlhelper &lt;semid&gt; &lt;parentpid&gt; &lt;directory&gt; [prefix] </p>
<h2>Description</h2>
<p>A helper program used by the Apache <code>httpd</code> mod_revocator plug-in to store-and-forward CRLs from upstream to the various Apache processes in the preform MPM. This saves each process from having to fetch the CRL itself. This is not expected to be run by end-users. The mod_revocator plug-in requires the mod_nss plug-in to also be registered with this Apache <code>httpd</code> process. Whenever an Apache <code>httpd</code> process configured to use the mod_revocator plug-in is started, this program will be automatically invoked via reference to the mod_revocator configuration file stored under <code>/etc/httpd/conf.d/revocator.conf</code> which contains the following default entry:</p>
<dl>
<dd># CRL Helper:<br />
 # This helper program does the actual CRL retrieval<br />
 #<br />
 # NOTE: Located at &#8216;/usr/bin/crlhelper&#8217; prior<br />
 # to &#8216;mod_revocator-1.0.3-16&#8217;.<br />
 #<br />
 CRLHelper /usr/libexec/crlhelper </p>
<h2>Options</h2>
<dl>
<dt><code>&lt;semid&gt;</code></p>
<dd>The semaphore which corresponds to the mod_revocator plug-in registered with the Apache <code>httpd</code> process during startup.</p>
<dt><code>&lt;parentpid&gt;</code></p>
<dd>The primary parent pid of the Apache <code>httpd</code> process into which both the mod_nss and mod_revocator plug-ins have been loaded.</p>
<dt><code>&lt;directory&gt;</code></p>
<dd>Since the mod_revocator plug-in depends upon the mod_nss plug-in being configured, this option specifies the destination directory of the NSS databases that will be associated with this executable specified by the following entry in the mod_nss plug-in&#8217;s <code>/etc/httpd/conf.d/nss.conf</code> configuration file:</p>
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
<dd>Optional prefix to attach prior to the names of the NSS certificate and key databases contained in the directory referenced by the previous argument and specified by the following entry in mod_nss plug-in&#8217;s <code>/etc/httpd/conf.d/nss.conf</code> configuration file (must be uncommented in order to be utilized):</p>
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
