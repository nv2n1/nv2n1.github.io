---
title: "klist(1)"
name: "klist"
section: "1"
letter: "k"
url: "/docs/linux/man/1-klist/"
description: "klist – list cached Kerberos tickets"
---

<h2>NAME</h2>
<p> klist &#8211; list cached Kerberos tickets</p>
<h2>SYNOPSIS</h2>
<p> <code>klist</code> [<code>-e</code>] [[<code>-c</code>] [<code>-l</code>] [<code>-A</code>] [<code>-f</code>] [<code>-s</code>] [<code>-a</code> [<code>-n</code>]]] [<code>-C</code>] [<code>-k</code> [<code>-t</code>] [<code>-K</code>]] [<code>-V</code>] [<i>cache_name</i>|<i>keytab_name</i>]</p>
<h2>DESCRIPTION</h2>
<p> klist lists the Kerberos principal and Kerberos tickets held in a credentials cache, or the keys held in a keytab file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code></p>
<dd> Displays the encryption types of the session key and the ticket for each credential in the credential cache, or each key in the keytab file.</p>
<dt><code>-l</code></p>
<dd> If a cache collection is available, displays a table summarizing the caches present in the collection.</p>
<dt><code>-A</code></p>
<dd> If a cache collection is available, displays the contents of all of the caches in the collection.</p>
<dt><code>-c</code></p>
<dd> List tickets held in a credentials cache. This is the default if neither <code>-c</code> nor <code>-k</code> is specified.</p>
<dt><code>-f</code></p>
<dd> Shows the flags present in the credentials, using the following abbreviations: </p>
<pre>
F    Forwardable
f    forwarded
P    Proxiable
p    proxy
D    postDateable
d    postdated
R    Renewable
I    Initial
i    invalid
H    Hardware authenticated
A    preAuthenticated
T    Transit policy checked
O    Okay as delegate
a    anonymous
</pre>
<dt><code>-s</code></p>
<dd> Causes klist to run silently (produce no output). klist will exit with status 1 if the credentials cache cannot be read or is expired, and with status 0 otherwise.</p>
<dt><code>-a</code></p>
<dd> Display list of addresses in credentials.</p>
<dt><code>-n</code></p>
<dd> Show numeric addresses instead of reverse-resolving addresses.</p>
<dt><code>-C</code></p>
<dd> List configuration data that has been stored in the credentials cache when klist encounters it. By default, configuration data is not listed.</p>
<dt><code>-k</code></p>
<dd> List keys held in a keytab file.</p>
<dt><code>-i</code></p>
<dd> In combination with <code>-k</code>, defaults to using the default client keytab instead of the default acceptor keytab, if no name is given.</p>
<dt><code>-t</code></p>
<dd> Display the time entry timestamps for each keytab entry in the keytab file.</p>
<dt><code>-K</code></p>
<dd> Display the value of the encryption key in each keytab entry in the keytab file.</p>
<dt><code>-V</code></p>
<dd> Display the Kerberos version number and exit. </p>
<p> If <i>cache_name</i> or <i>keytab_name</i> is not specified, klist will display the credentials in the default credentials cache or keytab file as appropriate. If the <code>KRB5CCNAME</code> environment variable is set, its value is used to locate the default ticket cache.</dl>
<h2>ENVIRONMENT</h2>
<p> klist uses the following environment variable:</p>
<dl>
<dt><code>KRB5CCNAME</code></p>
<dd> Location of the default Kerberos 5 credentials (ticket) cache, in the form <i>type</i>:<i>residual</i>. If no <i>type</i> prefix is present, the <code>FILE</code> type is assumed. The type of the default cache may determine the availability of a cache collection; for instance, a default cache of type <code>DIR</code> causes caches within the directory to be present in the collection.</dl>
<h2>FILES</h2>
<dl>
<dt><code>FILE:/tmp/krb5cc_%{uid}</code></p>
<dd> Default location of Kerberos 5 credentials cache</p>
<dt><code>FILE:/etc/krb5.keytab</code></p>
<dd> Default location for the local host&#8217;s keytab file.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i>, <i><a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
