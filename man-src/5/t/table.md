---
title: "table(5)"
name: "table"
section: "5"
letter: "t"
url: "/docs/linux/man/5-table/"
description: "table – format description for smtpd tables"
---

<p><code>table</code> &#8211; format description for smtpd tables</p>
<h2>Description</h2>
<p>This manual page documents the file format for the various tables used in the <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) mail daemon. </p>
<p> The format described here applies to tables as defined in <code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5).</p>
<h2>Table Types</h2>
<p>There are two types of tables: lists and mappings. A list consists of a series of values, while a mapping consists of a series of keys and their associated values. The following illustrates how to declare them as static tables:</p>
<dl>
<dd>
<pre>table mylist { value1, value2, value3 }
table mymapping { key1 = value1, key2 = value2, key3 = value3 }
</dl>
When using a
Ql file
table, a list will be written with each value on a line by itself:
<dl><dt><dd>value1
value2
value3
</dl>
A mapping will be written with each key and value on a line,
whitespaces separating both columns:
<dl><dt><dd>key1 value1
key2 value2
key3 value3
</dl>
A file table can be converted to a Berkeley database using the
<code><a href="//www.systutorials.com/docs/linux/man/8-makemap/">makemap</a></code>(8)
utility with no syntax change.
Tables using a
Ql file
or Berkeley DB backend will be referenced as follows:
<dl><dt><dd>table name file:/path/to/file
table name db:/path/to/file.db
</dl></pre>
<h3>Aliasing tables</h3>
<p>Aliasing tables are mappings that associate a recipient to one or many destinations. They can be used in two contexts: primary domain aliases and virtual domain mapping.</p>
<dl>
<dd>
<pre>accept for domain example.org alias &lt;myaliases&gt; deliver to mbox
accept for domain example.org virtual &lt;myaliases&gt; deliver to mbox
</dl>
In a primary domain context, the key is the user part of the recipient address,
whilst the value is one or many recipients as described in
<code><a href="//www.systutorials.com/docs/linux/man/5-aliases/">aliases</a></code>(5):
<dl><dt><dd>user1 otheruser
user2 otheruser1,otheruser2
user3 otheruser [at] example.com
</dl>
In a virtual domain context, the key is either a user part, a full email
address or a catch all, following selection rules described in
<code><a href="//www.systutorials.com/docs/linux/man/5-smtpd.conf/">smtpd.conf</a></code>(5),
and the value is one or many recipients as described in
<code><a href="//www.systutorials.com/docs/linux/man/5-aliases/">aliases</a></code>(5):
<dl><dt><dd>user1 otheruser
user2 [at] example.org otheruser1,otheruser2
@example.org otheruser [at] example.com
@ catchall [at] example.com
</dl></pre>
<h3>Domain tables</h3>
<p>Domain tables are simple lists of domains. They can only be used in one context:</p>
<dl>
<dd>
<pre>accept for domain &lt;mydomains&gt; deliver to mbox
</dl>
In that context, the list of domains will be matched against the recipient
domain.
For
Ql static,
Ql file
and
<code><a href="//www.systutorials.com/docs/linux/man/3-dbopen/">dbopen</a></code>(3)
backends, a wildcard may be used so the domain table may contain:
<dl><dt><dd>example.org
*.example.org
</dl></pre>
<h3>Credentials tables</h3>
<p>Credentials tables are mappings of credentials. They can be used in two contexts:</p>
<dl>
<dd>
<pre>listen on tls [...] auth &lt;credentials&gt;
accept for any relay tls+<a href="auth://label@host">auth://label@host</a> auth &lt;credentials&gt;
</dl>
In a listener context, the credentials are a mapping of username and encrypted
passwords:
<dl><dt><dd>user1 $2a$06$hIJ4QfMcp.90nJwKqGbKM.MybArjHOTpEtoTV.DgLYAiThuoYmTSe
user2 $2a$06$bwSmUOBGcZGamIfRuXGTvuTo3VLbPG9k5yeKNMBtULBhksV5KdGsK
</dl>
The passwords are to be encrypted using the
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8)
encrypt subcommand.
In a relay context, the credentials are a mapping of labels and
username:password pairs,
where the username may be omitted if identical to the label:
<dl><dt><dd>label1 user:password
label2 password
</dl>
The label must be unique and is used as a selector for the proper credentials
when multiple credentials are valid for a single destination.
The password is not encrypted as it must be provided to the remote host.</pre>
<h3>Netaddr tables</h3>
<p>Netaddr tables are lists of IPv4 and IPv6 network addresses. They can only be used in the following context:</p>
<dl>
<dd>
<pre>accept from source &lt;netaddr&gt; for domain example.org deliver to mbox
</dl>
When used as a &quot;from source&quot;, the address of a client is compared to the list
of addresses in the table until a match is found.
A netaddr table can contain exact addresses or netmasks, and looks as follow:
<dl><dt><dd>192.168.1.1
::1
ipv6:::1
192.168.1.0/24
</dl></pre>
<h3>Userinfo tables</h3>
<p>User info tables are used to described virtual system users. They are used in rule context to specify an alternate user base, mapping virtual users to local system UID, GID and home directory.</p>
<dl>
<dd>
<pre>accept for domain example.org userbase &lt;userinfo&gt; deliver to maildir
</dl>
The userinfo table is a mapping from virtual user names to a set of system user
ID, group ID and path to home directory.
A userinfo table looks as follows:
<dl><dt><dd>joe 1000:100:/home/virtual/joe
jack 1000:100:/home/virtual/jack
</dl>
In this example, both joe and jack are virtual users mapped to the local
system user with UID 1000 and GID 100, but different home directories.
These directories may contain a
<code><a href="//www.systutorials.com/docs/linux/man/5-forward/">forward</a></code>(5)
file.</pre>
<h3>Source tables</h3>
<p>Source tables are lists of IPv4 and IPv6 addresses. They can only be used in the following context:</p>
<dl>
<dd>
<pre>accept for domain example.org relay source &lt;addresses&gt;
</dl>
Successive queries to the source table will return the elements one by one.
A source table looks as follow:
<dl><dt><dd>192.168.1.2
192.168.1.3
::1
::2
ipv6:::3
ipv6:::4
</dl></pre>
<h3>Mailaddr tables</h3>
<p>Mailaddr tables are lists of email addresses. They can be used in the following contexts:</p>
<dl>
<dd>
<pre>accept sender &lt;senders&gt; for domain example.org deliver to mbox
accept for domain example.org recipient &lt;recipients&gt; deliver to mbox
</dl>
A mailaddr entry is used to match an email address against a username,
a domain or a full email address.
A &quot;*&quot; wildcard may be used in part of the domain name.
A mailaddr table looks as follow:
<dl><dt><dd>user
@domain
user [at] domain
user@*.domain
</dl></pre>
<h3>Addrname tables</h3>
<p>Addrname tables are used to map IP addresses to hostnames. They can be used in both listen context and relay context:</p>
<dl>
<dd>
<pre>listen on 0.0.0.0 hostnames &lt;addrname&gt;
accept for any relay hostnames &lt;addrname&gt;
</dl>
In listen context, the table is used to look up the server name to advertise
depending on the local address of the socket on which a connection is accepted.
In relay context, the table is used to determine the hostname for the HELO
sequence of the SMTP protocol, depending on the local address used for the
outgoing connection.
The format is a mapping from inet4 or inet6 addresses to hostnames:
<dl><dt><dd>::1 localhost
127.0.0.1 localhost
88.190.23.165 <a rel="nofollow" href="http://www.opensmtpd.org">www.opensmtpd.org</a>
</dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5), <code><a href="/docs/linux/man/8-makemap/">makemap</a></code>(8), <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) </p>
