---
title: "systemd-journal-upload(8)"
name: "systemd-journal-upload"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-journal-upload/"
description: "systemd-journal-upload – Send journal messages over the network"
---

<p>systemd-journal-upload &#8211; Send journal messages over the network</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-journal-upload</code> [OPTIONS&#8230;] [-u/&#8211;url=<i>URL</i>] [SOURCES&#8230;]</dl>
<h2>Description</h2>
<p><code>systemd-journal-upload</code></p>
<dd>will upload journal entries to the URL specified with <code>&#8211;url</code>. Unless limited by one of the options specified below, all journal entries accessible to the user the program is running as will be uploaded, and then the program will wait and send new entries as they become available.</p>
<h2>Options</h2>
<p><code>-u</code>, <code>&#8211;url=</code><code>[<a rel="nofollow" href="https://]">https://]</a></code><i>URL</i>, <code>&#8211;url=</code><code>[<a rel="nofollow" href="http://]">http://]</a></code><i>URL</i></p>
<dl>
<dd>Upload to the specified address. <i>URL</i> may specify either just the hostname or both the protocol and hostname. <code>https</code> is the default.</dl>
<p> <code>&#8211;system</code>, <code>&#8211;user</code></p>
<dl>
<dd>Limit uploaded entries to entries from system services and the kernel, or to entries from services of current user. This has the same meaning as <code>&#8211;system</code> and <code>&#8211;user</code> options for <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1). If neither is specified, all accessible entries are uploaded.</dl>
<p> <code>-m</code>, <code>&#8211;merge</code></p>
<dl>
<dd>Upload entries interleaved from all available journals, including other machines. This has the same meaning as <code>&#8211;merge</code> option for <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1).</dl>
<p> <code>-D</code>, <code>&#8211;directory=</code><i>DIR</i></p>
<dl>
<dd>Takes a directory path as argument. Upload entries from the specified journal directory <i>DIR</i> instead of the default runtime and system journal paths. This has the same meaning as <code>&#8211;directory</code> option for <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1).</dl>
<p> <code>&#8211;file=</code><i>GLOB</i></p>
<dl>
<dd>Takes a file glob as an argument. Upload entries from the specified journal files matching <i>GLOB</i> instead of the default runtime and system journal paths. May be specified multiple times, in which case files will be suitably interleaved. This has the same meaning as <code>&#8211;file</code> option for <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1).</dl>
<p> <code>&#8211;cursor=</code></p>
<dl>
<dd>Upload entries from the location in the journal specified by the passed cursor. This has the same meaning as <code>&#8211;cursor</code> option for <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1).</dl>
<p> <code>&#8211;after-cursor=</code></p>
<dl>
<dd>Upload entries from the location in the journal <i>after</i> the location specified by the this cursor. This has the same meaning as <code>&#8211;after-cursor</code> option for <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1).</dl>
<p> <code>&#8211;save-state</code>[=<i>PATH</i>]</p>
<dl>
<dd>Upload entries from the location in the journal <i>after</i> the location specified by the cursor saved in file at <i>PATH</i> (/var/lib/systemd/journal-upload/state by default). After an entry is successfully uploaded, update this file with the cursor of that entry.</dl>
<p> <code>&#8211;follow</code>[=<i>BOOL</i>]</p>
<dl>
<dd>If set to yes, then <code>systemd-journal-upload</code> waits for input.</dl>
<p> <code>&#8211;key=</code></p>
<dl>
<dd>Takes a path to a SSL key file in PEM format. Defaults to /etc/ssl/private/journal-upload.pem.</dl>
<p> <code>&#8211;cert=</code></p>
<dl>
<dd>Takes a path to a SSL certificate file in PEM format. Defaults to /etc/ssl/certs/journal-upload.pem.</dl>
<p> <code>&#8211;trust=</code></p>
<dl>
<dd>Takes a path to a SSL CA certificate file in PEM format, or <code>all</code>. If <code>all</code> is set, then certificate checking will be disabled. Defaults to /etc/ssl/ca/trusted.pem.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned; otherwise, a non-zero failure code is returned.</p>
<h2>Examples</h2>
<p><code>Example 1. Setting up certificates for authentication</code> </p>
<p> Certificates signed by a trusted authority are used to verify that the server to which messages are uploaded is legitimate, and vice versa, that the client is trusted. </p>
<p> A suitable set of certificates can be generated with <code>openssl</code>: </p>
<dl>
<dd>
<pre>openssl req -newkey rsa:2048 -days 3650 -x509 -nodes \
 -out ca.pem -keyout ca.key -subj '/CN=Certificate authority/'
cat &gt;ca.conf &lt;&lt;EOF
[ ca ]
default_ca = this
[ this ]
new_certs_dir = .
certificate = ca.pem
database = ./index
private_key = ca.key
serial = ./serial
default_days = 3650
default_md = default
policy = policy_anything
[ policy_anything ]
countryName = optional
stateOrProvinceName = optional
localityName = optional
organizationName = optional
organizationalUnitName = optional
commonName = supplied
emailAddress = optional
EOF
touch index
echo 0001 &gt;serial
SERVER=server
CLIENT=client
openssl req -newkey rsa:1024 -nodes -out $SERVER.csr -keyout $SERVER.key -subj &quot;/CN=$SERVER/&quot;
openssl ca -batch -config ca.conf -notext -in $SERVER.csr -out $SERVER.pem
openssl req -newkey rsa:1024 -nodes -out $CLIENT.csr -keyout $CLIENT.key -subj &quot;/CN=$CLIENT/&quot;
openssl ca -batch -config ca.conf -notext -in $CLIENT.csr -out $CLIENT.pem</pre>
</dl>
<p> Generated files ca.pem, server.pem, and server.key should be installed on server, and ca.pem, client.pem, and client.key on the client. The location of those files can be specified using <i>TrustedCertificateFile=</i>, <i>ServerCertificateFile=</i>, <i>ServerKeyFile=</i>, in /etc/systemd/journal-remote.conf and /etc/systemd/journal-upload.conf, respectively. The default locations can be queried by using <code>systemd-journal-remote &#8211;help</code> and <code>systemd-journal-upload &#8211;help</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-journal-remote/">systemd-journal-remote</a></code>(8), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-journal-gatewayd-service/">systemd-journal-gatewayd.service</a></code>(8) </p>
