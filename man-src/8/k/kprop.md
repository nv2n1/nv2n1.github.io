---
title: "kprop(8)"
name: "kprop"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kprop/"
description: "kprop – propagate a Kerberos V5 principal database to a slave server"
---

<p>kprop &#8211; propagate a Kerberos V5 principal database to a slave server</p>
<h2>Synopsis</h2>
<p><code>kprop</code> [<code>-r</code> <i>realm</i>] [<code>-f</code> <i>file</i>] [<code>-d</code>] [<code>-P</code> <i>port</i>] [<code>-s</code> <i>keytab</i>] <i>slave_host</i></p>
<h2>Description</h2>
<p>kprop is used to securely propagate a Kerberos V5 database dump file from the master Kerberos server to a slave Kerberos server, which is specified by <i>slave_host</i>. The dump file must be created by <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>-r</code> <i>realm</i></dt>
<dd>Specifies the realm of the master server.</dd>
<dt><code>-f</code> <i>file</i></dt>
<dd>Specifies the filename where the dumped principal database file is to be found; by default the dumped database file is normally <code>/var/kerberos</code><code>/krb5kdc</code><code>/slave_datatrans</code>.</dd>
<dt><code>-P</code> <i>port</i></dt>
<dd>Specifies the port to use to contact the <i><a href="/docs/linux/man/8-kpropd/">kpropd</a>(8)</i> server on the remote host.</dd>
<dt><code>-d</code></dt>
<dd>Prints debugging information.</dd>
<dt><code>-s</code> <i>keytab</i></dt>
<dd>Specifies the location of the keytab file.</dd></dl>
<h2>Environment</h2>
<p><i>kprop</i> uses the following environment variable:</p>
<dl>
<dt>&bull;</dt>
<dd><code>KRB5_CONFIG</code></dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-kpropd/">kpropd</a>(8)</i>, <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i>, <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
