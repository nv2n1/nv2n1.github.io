---
title: "ipropd-slave(8)"
name: "ipropd-slave"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipropd-slave/"
description: "iprop ipropd-master ipropd-slave – propagate changes to a Heimdal Kerberos master KDC to slave KDCs"
---

<p><code>iprop</code> <code>ipropd-master</code> <code>ipropd-slave</code> &#8211; propagate changes to a Heimdal Kerberos master KDC to slave KDCs</p>
<h2>Synopsis</h2>
<p><code>ipropd-master</code> [-<code>c </code><i>string | </i> &#8211;<code>-config-file= </code><i>string</i> ] [-<code>r </code><i>string | </i> &#8211;<code>-realm= </code><i>string</i> ] [-<code>k </code><i>kspec | </i> &#8211;<code>-keytab= </code><i>kspec</i> ] [-<code>d </code><i>file | </i> &#8211;<code>-database= </code><i>file</i> ] [-<code>-slave-stats-file= </code><i>file</i> ] [-<code>-time-missing= </code><i>time</i> ] [-<code>-time-gone= </code><i>time</i> ] [-<code>-detach</code> ] [-<code>-version</code> ] [-<code>-help</code> ]<br />
<code>ipropd-slave</code> [-<code>c </code><i>string | </i> &#8211;<code>-config-file= </code><i>string</i> ] [-<code>r </code><i>string | </i> &#8211;<code>-realm= </code><i>string</i> ] [-<code>k </code><i>kspec | </i> &#8211;<code>-keytab= </code><i>kspec</i> ] [-<code>-time-lost= </code><i>time</i> ] [-<code>-detach</code> ] [-<code>-version</code> ] [-<code>-help</code> ] <i>master</i></p>
<h2>Description</h2>
<p><code>ipropd-master</code> is used to propagate changes to a Heimdal Kerberos database from the master Kerberos server on which it runs to slave Kerberos servers running <code>ipropd-slave</code> </p>
<p> The slaves are specified by the contents of the slaves file in the KDC&#8217;s database directory, e.g. /var/heimdal/slaves This has principals one per-line of the form </p>
<blockquote><p><tt>iprop/ </tt><i>slave </i><code>@ </code><i>REALM</i> </p></blockquote>
<p> where <i>slave</i> is the hostname of the slave server in the given <i>REALM</i> e.g. </p>
<blockquote><p><tt>iprop/kerberos-1.example.com [at] EXAMPLE.COM</tt></p></blockquote>
<p> On a slave, the argument Fa master specifies the hostname of the master server from which to receive updates. </p>
<p> In contrast to <a href="/docs/linux/man/8-hprop/">hprop</a>(8), which sends the whole database to the slaves regularly, <code>ipropd-master</code> normally sends only the changes as they happen on the master. The master keeps track of all the changes by assigning a version number to every change to the database. The slaves know which was the latest version they saw, and in this way it can be determined if they are in sync or not. A log of all the changes is kept on the master. When a slave is at an older version than the oldest one in the log, the whole database has to be sent. </p>
<p> The changes are propagated over a secure channel (on port 2121 by default). This should normally be defined as &#8220;iprop/tcp&#8221; in /etc/services or another source of the services database. The master and slaves must each have access to a keytab with keys for the <code>iprop</code> service principal on the local host. </p>
<p> There is a keep-alive feature logged in the master&#8217;s slave-stats file (e.g. /var/heimdal/slave-stats ) </p>
<p> Supported options for <code>ipropd-master</code></p>
<dl>
<dt><code>-c </code><i>string , &#8211;</i><code>-config-file= </code><i>string</i></p>
<dd>
<dt><code>-r </code><i>string , &#8211;</i><code>-realm= </code><i>string</i></p>
<dd>
<dt><code>-k </code><i>kspec , &#8211;</i><code>-keytab= </code><i>kspec</i></p>
<dd>keytab to get authentication from</p>
<dt><code>-d </code><i>file , &#8211;</i><code>-database= </code><i>file</i></p>
<dd>Database (default per KDC)</p>
<dt><code>&#8211;slave-stats-file= </code><i>file</i></p>
<dd>file for slave status information</p>
<dt><code>&#8211;time-missing= </code><i>time</i></p>
<dd>time before slave is polled for presence (default 2 min)</p>
<dt><code>&#8211;time-gone= </code><i>time</i></p>
<dd>time of inactivity after which a slave is considered gone (default 5 min)</p>
<dt><code>&#8211;detach</code></p>
<dd>detach from console</p>
<dt><code>&#8211;version</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd></dl>
<p> Supported options for <code>ipropd-slave</code></p>
<dl>
<dt><code>-c </code><i>string , &#8211;</i><code>-config-file= </code><i>string</i></p>
<dd>
<dt><code>-r </code><i>string , &#8211;</i><code>-realm= </code><i>string</i></p>
<dd>
<dt><code>-k </code><i>kspec , &#8211;</i><code>-keytab= </code><i>kspec</i></p>
<dd>keytab to get authentication from</p>
<dt><code>&#8211;time-lost= </code><i>time</i></p>
<dd>time before server is considered lost (default 5 min)</p>
<dt><code>&#8211;detach</code></p>
<dd>detach from console</p>
<dt><code>&#8211;version</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd></dl>
<p> Time arguments for the relevant options above may be specified in forms like 5 min, 300 s, or simply a number of seconds.</p>
<h2>Files</h2>
<p>slaves slave-stats in the database directory.</p>
<h2>See Also</h2>
<p>krb5.conf5, <a href="/docs/linux/man/8-hprop/">hprop</a>(8), <a href="/docs/linux/man/8-hpropd/">hpropd</a>(8), iprop-log8, <a href="/docs/linux/man/8-kdc/">kdc</a>(8). </p>
