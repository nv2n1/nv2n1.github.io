---
title: "ldapget(8)"
name: "ldapget"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ldapget/"
description: "ldapget – Tool used to fetch URLs via LDAP/LDAPS"
---

<p>ldapget &#8211; Tool used to fetch URLs via LDAP/LDAPS </p>
<h2>Synopsis</h2>
<p>ldapget [NSS database] &lt;url&gt; </p>
<h2>Description</h2>
<p>A tool supplied with the Apache <code>httpd</code> mod_revocator plug-in used to demonstrate how CRLs can be fetched using LDAP/LDAPS without the use of any direct LDAP/LDAPS URLs. The mod_revocator plug-in requires the mod_nss plug-in to also be registered with this Apache <code>httpd</code> process. Prior to <code>mod_revocator-1.0.3-16</code>, this tool was located at <code>/usr/bin/ldapget</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>[NSS database]</code></p>
<dd>Optionally specifies the destination directory where the NSS databases reside. If this parameter is not provided, the location specified in mod_nss plug-in&#8217;s <code>/etc/httpd/conf.d/nss.conf</code> configuration file will be utilized:</p>
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
<dt><code>&lt;url&gt;</code></p>
<dd>The LDAP/LDAPS URL utilized to fetch the CRL. The following entry in mod_revocator plug-in&#8217;s <code>/etc/httpd/conf.d/revocator.conf</code> configuration file contains a sample utilization of this executable (the line containing <code>ldapget</code> must be uncommented in order to be utilized):</p>
<dd>
<table>
<tr VALIGN=top>
<td></td>
<td># CRL URLs:
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># A space delimited list of URLs to retrieve and install.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td># protocol://urldata;update_interval;max_age
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>#CRLFile &quot;<a href="ldap://ldap.example.com:5000/o=example.net?">ldap://ldap.example.com:5000/o=example.net?</a>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>usercertificate%3binary?sub?(sn=Jensen)??;30;30&quot;
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><code>#CRLFile &quot;<a href="exec:///usr/sbin/ldapget|ldap://ldap.example.com:">exec:///usr/sbin/ldapget|ldap://ldap.example.com:</a></code>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>3389/o=example.com?userCertificate%3bbinary?sub?
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>(uid=crl)??;30;30&quot;
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>#CRLFile &quot;<a rel="nofollow" href="https://ca.example.com:1025/getCRL?op=">https://ca.example.com:1025/getCRL?op=</a>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>getCRL&amp;issuepoint=MasterCRL;30;30&quot;
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
