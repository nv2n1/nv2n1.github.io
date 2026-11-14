---
title: "smtpd-conf(5)"
name: "smtpd-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-smtpd-conf/"
description: "smtpd.conf – Simple Mail Transfer Protocol daemon configuration file"
---

<p><code>smtpd.conf</code> &#8211; Simple Mail Transfer Protocol daemon configuration file</p>
<h2>Description</h2>
<p><code>smtpd.conf</code> is the configuration file for the mail daemon <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8). </p>
<p> The current line can be extended over multiple lines using a backslash (Sq \.) Comments can be put anywhere in the file using a hash mark (Sq #,) and extend to the end of the current line. Care should be taken when commenting out multi-line text: the comment is effective until the end of the entire block. </p>
<p> Argument names not beginning with a letter, digit, or underscore must be quoted. Arguments containing whitespace should be surrounded by double quotes (&quot;.) </p>
<p> Macros can be defined that will later be expanded in context. Macro names must start with a letter, digit, or underscore, and may contain any of those characters. Macro names may not be reserved words (for example <i>listen</i>, <i>accept</i>, <i>port</i>). Macros are not expanded inside quotes. </p>
<p> For example:</p>
<dl>
<dd>
<pre>lan_addr = &quot;192.168.0.1&quot;
listen on $lan_addr
listen on $lan_addr tls auth
</dl>
Additional configuration files can be included with the
<code> include</code>
keyword, for example:
<dl><dt><dd>include &quot;/etc/opensmtpd/smtpd.conf.local&quot;
</dl>
The syntax of
<code>smtpd.conf</code>
is described below.
<dl><dt><dd><dl><dt><code> accept | reject</code><dd><code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
accepts and rejects messages
based on information gathered during the SMTP session.
</dl>
For each message processed by the daemon,
the rules are evaluated in sequential order,
from first to last.
The first matching rule decides what action is taken.
If no rule matches the message,
the default action is to reject the message.
An exclamation mark may be specified to perform a reverse match.
Following the accept/reject
decision comes the optional tag matching:
<dl><dt><dd><dl><dt><code> tagged</code><dd>[<code> !</code>]
<i>tag</i>
If specified, the rule will only be matched if the client session was tagged with
<i>tag</i>.
</dl></dl>
After that the client's IP address rule is specified:
<dl><dt><dd><dl><dt><code> from any</code><dd>Make the rule match regardless of the IP of connecting client.
<dt><code> from</code><dd>[<code> !</code>]
<code> local</code>
The rule matches only locally originating connections.
This is the default,
and may be omitted.
<dt><code> from</code><dd>[<code> !</code>]
<code> source</code>
Pf &lt; <i>table</i> &gt;
The rule matches if the connection is made from a client whose address
is declared in the table
<i>table</i>.
</dl></dl>
In addition, finer access control may be achieved on the sender if desired:
<dl><dt><dd><dl><dt><code> sender</code><dd>[<code> !</code>]
Pf &lt; <i>senders</i> &gt;
If specified, the rule will only be matched if the sender email address
is found in the table
<i>senders</i>.
The table may contain complete email addresses or apply to an entire
domain if prefixed with
Sq @.
</dl></dl>
Next comes the selection based on the domain the message is sent to:
<dl><dt><dd><dl><dt><code> for any [ alias &lt; </code><i>aliases</i> &gt;]<dd>Make the rule match regardless of the domain it is sent to.
If specified, the table
<i>aliases</i>
is used for looking up alternative destinations for all addresses.
<dt><code> for any virtual &lt; </code><i>vmap</i> &gt;<dd>Make the rule match regardless of the domain it is sent to.
The
<i>vmap</i>
table will be used as the virtual domain mapping.
<dt><code> for</code><dd>[<code> !</code>]
<code> domain</code>
<i>domain</i>
[<code> alias &lt; </code><i>aliases</i> &gt;]
This rule applies to mail destined for the specified
<i>domain</i>.
This parameter supports the
Sq *
wildcard,
so that a single rule for all sub-domains can be used, for example:
<dl><dt><dd>accept for domain &quot;*.example.com&quot; deliver to mbox
</dl></dl>
If specified, the table
<i>aliases</i>
is used for looking up alternative destinations for addresses in this
<i>domain</i>.
<dl><dt><code> for</code><dd>[<code> !</code>]
<code> domain</code>
Pf &lt; <i>domains</i> &gt;
[<code> alias &lt; </code><i>aliases</i> &gt;]
This rule applies to mail destined to domains which are part of the table
<i>domains</i>.
</dl>
If specified, the table
<i>aliases</i>
is used for looking up alternative destinations for addresses in these
<i>domains</i>.
<dl><dt><code> for</code><dd>[<code> !</code>]
<code> domain</code>
<i>domain</i>
<code> virtual &lt; </code><i>users</i> &gt;
This rule applies to mail destined for the specified virtual
<i>domain</i>.
This parameter supports the
Sq *
wildcard,
so that a single rule for all sub-domains can be used, for example:
<dl><dt><dd>accept for domain &quot;*.example.com&quot; \
 virtual &lt;users&gt; deliver to mbox
</dl></dl>
The table
<i>users</i>
holds a key-value mapping of virtual to system users.
For an example of how to configure the
<i>users</i>
table, see
<code><a href="//www.systutorials.com/docs/linux/man/5-table/">table</a></code>(5).
<dl><dt><code> for</code><dd>[<code> !</code>]
<code> domain</code>
Pf &lt; <i>domains</i> &gt;<code> virtual &lt; </code><i>users</i> &gt;
This rule applies to mail destined for the virtual domains specified
in the table
<i>domains</i>.
</dl>
The table
<i>users</i>
holds a key-value mapping of virtual to system users.
For an example of how to configure the
<i>users</i>
table, see
<code><a href="//www.systutorials.com/docs/linux/man/5-table/">table</a></code>(5).
<dl><dt><code> for</code><dd>[<code> !</code>]
<code> local</code>
[<code> alias &lt; </code><i>aliases</i> &gt;]
This rule applies to mail destined to
``localhost''
and to the default server name.
See the
<code>FILES</code>
entry for
<i>/etc/opensmtpd/mailname</i>
below for details of how the server name is determined.
<dt><code> for</code><dd>[<code> !</code>]
<code> local</code>
<code> virtual &lt; </code><i>vmap</i> &gt;
This rule applies to mail destined to
``localhost''
and to the default server name.
The
<i>vmap</i>
table will be used as the virtual domain mapping.
</dl></dl>
Further access control may be achieved on specific recipients if desired:
<dl><dt><dd><dl><dt><code> recipient</code><dd>[<code> !</code>]
Pf &lt; <i>recipients</i> &gt;
If specified, the rule will only be matched if the recipient email address
is found in the table
<i>recipients</i>.
The table may contain complete email addresses or apply to an entire
domain if prefixed with
Sq @.
</dl></dl>
If the method of delivery is local, a user database may be
specified to override the system database:
<dl><dt><dd><dl><dt>[<code> userbase &lt; </code><i>table</i> &gt;]<dd>Look up users in the table
<i>table</i>
instead of performing system lookups using the
<code><a href="//www.systutorials.com/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3)
function.
</dl></dl>
You can also accept mail just to have it forwarded elsewhere:
<dl><dt><dd><dl><dt><code> forward-only</code><dd>Mail is accepted for local recipients ONLY if it is redirected to an
external address via an alias or a ~/.forward file.
</dl>
Example:
<dl><dt><dd>accept for domain opensmtpd.org forward-only
</dl></dl>
Finally, the method of delivery is specified:
<dl><dt><dd><dl><dt><code> deliver to lmtp</code><dd>[<i>host</i>: <i>port</i> | socket]
[<code> rcpt-to</code>]
[<code> as </code><i>user</i>]
Mail is delivered to
<i>host</i>: <i>port</i>,
or to the
Ux
<i>socket</i>
over LMTP with the privileges of the specified
<i>user</i>.
</dl>
Optionally,
<code> rcpt-to</code>
might be specified to use the recipient email address (after expansion) instead
of the local user in the LMTP session as RCPT TO.
<dl><dt><code> deliver to maildir [</code><i>path</i>]<dd>Mail is added to a maildir.
Its location,
<i>path</i>,
may contain format specifiers that are expanded before use
(see .B FORMAT SPECIFIERS .)
If
<i>path</i>
is not provided, then
<i>~/Maildir</i>
is assumed.
<dt><code> deliver to mbox</code><dd>Mail is delivered to the local user's system mailbox in
<i>/var/mail</i>.
<dt><code> deliver to mda </code><i>program</i> [<code> as </code><i>user</i>]<dd>Mail is piped to the specified
<i>program</i>,
which is run with the privileges of the specified
<i>user</i>
or the user the message is destined to.
This parameter may use conversion specifiers that are expanded before use
(see .B FORMAT SPECIFIERS .)
<dt>Bk -words<dd><code> relay</code>
[<code> backup [</code><i>mx</i>]]
[<code> as </code><i>address</i>]
[<code> source &lt; </code><i>source</i> &gt;]
[<code> hostname </code><i>name</i>]
[<code> hostnames &lt; </code><i>names</i> &gt;]
[<code> pki </code><i>pkiname</i>]
[<code> tls [ verify</code>]]
Ek
</dl>
Mail is relayed.
The routing decision is based on the DNS system.
If the
<code> backup</code>
parameter is specified, the current server will act as a backup server
for the target domain.
Accepted mails are only relayed through servers with a lower preference
value in the MX record for the domain than the one specified in
<i>mx</i>.
If
<i>mx</i>
is not specified, the default server name will be assumed.
If the
<code> as</code>
parameter is specified,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will rewrite the sender advertised
in the SMTP session.
<i>address</i>
may be a user, a domain prefixed with
Sq @,
or an email address, causing
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
to rewrite the user-part, the domain-part, or the entire address, respectively.
If the
<code> source</code>
parameter is specified,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will explicitly bind to an address found in the table referenced by
<i>source</i>
when connecting to the relay.
If the table contains more than one address, they are picked in turn each
time a new connection is opened.
By default, when connecting to a remote server,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
advertises its default server name.
A
<code> hostname</code>
parameter may be specified to advertise the alternate hostname
<i>name</i>.
If the
<code> source</code>
parameter is used, the
<code> hostnames</code>
parameter may be specified to advertise a hostname based on
the source address.
Table
<i>names</i>
contains a mapping of IP addresses to hostnames and
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will automatically select the name that matches its source address
when connected to the remote server.
The
<code> hostname</code>
and
<code> hostnames</code>
parameters are mutually exclusive.
When relaying, STARTTLS is always attempted if available on remote host and
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will try to present a certificate matching the outgoing hostname if one is
registered in the pki.
If
<code> pki</code>
is specified, the certificate registered for
<i>pkiname</i>
is used instead.
If
<code> tls</code>
is specified,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will refuse to relay unless the remote host provides STARTTLS.
If
<code> tls verify</code>
is specified,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will refuse to relay unless the remote host provides STARTTLS and the
certificate it presented has been verified.
Note that the
<code> tls</code>
and
<code> tls verify</code>
options should only be used in private networks
as they will prevent proper relaying on the Internet.
<dl><dt><code> relay via</code><dd><i>host</i>
[<code> auth &lt; </code><i>auth</i> &gt;]
[<code> as </code><i>address</i>]
[<code> source &lt; </code><i>source</i> &gt;]
[<code> hostname </code><i>name</i>]
[<code> hostnames &lt; </code><i>names</i> &gt;]
[<code> pki </code><i>pkiname</i>]
[<code> verify</code>]
</dl>
Mail is relayed through the specified
<i>host</i>
expressed as a URL.
For example:
<dl><dt><dd><a href="smtp://mx1.example.org">smtp://mx1.example.org</a> # use SMTP
<a href="smtp://mx1.example.org:4321">smtp://mx1.example.org:4321</a> # use SMTP \
 # with port 4321
<a href="lmtp://localhost:2026">lmtp://localhost:2026</a> # use LMTP \
 # with port 2026
</dl>
The communication channel may be secured using one of the secure
schemas.
For example:
<dl><dt><dd><a href="tls://mx1.example.org">tls://mx1.example.org</a> # use TLS
<a href="smtps://mx1.example.org">smtps://mx1.example.org</a> # use SMTPS
<a href="secure://mx1.example.org">secure://mx1.example.org</a> # try SMTPS and \
 # fallback to TLS
</dl>
In addition, credentials for authenticated relaying may be provided
when using a secure schema.
For example:
<dl><dt><dd>tls+<a href="auth://label@mx.example.org">auth://label@mx.example.org</a> # over TLS
smtps+<a href="auth://label@mx.example.org">auth://label@mx.example.org</a> # over SMTPS
secure+<a href="auth://label@mx.example.org">auth://label@mx.example.org</a> # over either \
 # SMTPS or TLS
</dl>
If a pki entry exists for the outgoing hostname, or one is provided
with
<i>pkiname</i>,
the associated certificate will be sent to the remote server.
If an SMTPAUTH session with
<i>host</i>
is desired, the
<code> auth</code>
parameter is used to specify the
<i>auth</i>
table that holds the credentials.
Credentials will be looked up using the label provided in the URL.
If the
<code> as</code>
parameter is specified,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will rewrite the sender advertised
in the SMTP session.
<i>address</i>
may be a user, a domain prefixed with
Sq @,
or an email address, causing
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
to rewrite the user-part, the domain-part, or the entire address, respectively.
If the
<code> source</code>
parameter is specified,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will explicitly bind to an address found in the table referenced by
Pf &lt; <i>source</i> &gt;
when connecting to the relay.
If the table contains more than one address, they are picked in turn each
time a new connection is opened.
By default, when connecting to a remote server,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
advertises its default server name.
A
<code> hostname</code>
parameter may be specified to advertise the alternate hostname
<i>name</i>.
If the
<code> source</code>
parameter is used, the
<code> hostnames</code>
parameter may be specified to advertise a hostname based on
the source address.
Table
<i>names</i>
contains a mapping of IP addresses to hostnames and
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will automatically select the name that matches its source address
when connected to the remote server.
The
<code> hostname</code>
and
<code> hostnames</code>
parameters are mutually exclusive.
If
<code> verify</code>
is specified,
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will refuse to relay unless the remote host provides STARTTLS and the
certificate it presented has been verified.
The relay URL must specify TLS for this option to be valid.
</dl>
Additional per-rule adjustments are available:
<dl><dt><dd><dl><dt><code> expire</code><dd>Sm off
<i>n</i>
{<code>s</code> | m | h | d}
Sm on
Specify how long a message that matched this rule can stay in the queue.
</dl></dl><dl><dt><code> bounce-warn</code><dd>Sm off
<i>n</i>
{<code>s</code> | m | h | d}
[,
Sm on
<i>...</i>
]
Specify the delays for which temporary failure reports must be generated
when messages are stuck in the queue.
For example:
<dl><dt><dd>bounce-warn 1h, 6h, 2d
</dl></dl>
will generate a failure report when an envelope is in the queue for more
than one hour, six hours and two days.
The default is 4h.
<dl><dt><code> ca </code><i>hostname</i> <code> certificate </code><i>cafile</i><dd>Associate a custom CA certificate located in
<i>cafile</i>
with
<i>hostname</i>.
<dt><code> ciphers </code><i>cipher-list</i><dd>Specify an alternate list of ciphers to use when establishing TLS sessions.
It is highly recommended to avoid making use of this option unless there
is a good understanding of the implications.
</dl>
When not specified, only ciphers considered safe are chosen.
<dl><dt><code> expire</code><dd>Sm off
<i>n</i>
{<code>s</code> | m | h | d}
Sm on
Specify how long a message can stay in the queue.
The default value is 4d.
For example:
<dl><dt><dd>expire 4d # expire after 4 days
expire 10h # expire after 10 hours
</dl><dt><code> filter </code><i>name</i> filter [<i>arguments</i>]<dd>Specify a filter with the given
<i>name</i>
and the program
<i>filter</i>
using the given filter
<i>arguments</i>.
Filters are used to hook into the SMTP dialog and provide additional filtering
options for
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8).
<dt><code> filter </code><i>name</i> <code> chain </code><i>filter</i> <i>...</i><dd>Specify a filter chain with the given
<i>name</i>
and filters.
<dt><code> limit session</code><dd>{<code>max-rcpt</code> | max-mails}
<i>num</i>
Instruct
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
to accept a maximum number of recipients or emails at once
in the receiving queue.
Defaults are 100 for
<code> max-mails</code>
and 1000 for
<code> max-rcpt.</code>
<dt><code> limit mta</code><dd>[<code> for domain </code><i>domain</i>]
<i>family</i>
Instruct
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
to only use the specified address
<i>family</i>
for outgoing connections.
Accepted values are
<code> inet4</code>
and
<code> inet6.</code>
If a
<i>domain</i>
is specified, the restriction only applies when connecting
to MXs for this domain.
<dt><code> limit scheduler max-inflight </code><i>num</i><dd>Suspend the scheduling of envelopes for deliver/relay until the number
of inflight envelopes falls below
<i>num</i>.
Changing the default value might degrade performance.
<dt><code> listen on socket</code><dd>[<code> filter </code><i>name</i>]
[<code> mask-source</code>]
br
Bk -words
<code> listen on </code><i>interface</i>
[<i>family</i>]
[<code> port </code><i>port</i>]
[<code> filter </code><i>name</i>]
[<code> tls | tls-require | tls-require verify | smtps | secure</code>]
[<code> pki </code><i>pkiname</i>]
[<code> ca </code><i>caname</i>]
[<code> auth | auth-optional [&lt; </code><i>authtable</i> &gt;]]
[<code> tag </code><i>tag</i>]
[<code> hostname </code><i>hostname</i>]
[<code> hostnames &lt; </code><i>names</i> &gt;]
[<code> senders &lt; </code><i>users</i> &gt;[masquerade]]
[<code> mask-source</code>]
[<code> received-auth</code>]
[<code> no-dsn</code>]
Ek
</dl>
Specify a
<code> socket</code>
or an
<i>interface</i>
to listen on for incoming connections.
The
<code> listen on socket</code>
directive is used to modify the behavior of the listener handling
messages submitted through the local enqueuer, for example via the
<code><a href="//www.systutorials.com/docs/linux/man/1-mail/">mail</a></code>(1)
utility.
This is an optional directive: if unspecified then
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will simply listen for connections on the
<code> socket</code>
as if it was configured with no option.
Clients connecting through the
<code> socket</code>
will always be tagged with the 'local'
<code> tag.</code>
To listen on a specific network interface, specify an
<i>interface</i>
and an optional
<i>port</i>.
An interface group, an IP address or a domain name may
be used in place of
<i>interface</i>.
The
<i>family</i>
parameter can be used to listen only on specific address family.
Accepted values are
<code> inet4</code>
and
<code> inet6.</code>
A
<code> filter</code>
may be specified to use a filter or filter chain with the given
<i>name</i>
on SMTP transactions.
Secured connections are provided either using STARTTLS
(<code> tls,</code>)
by default on port 25,
or SMTPS
(<code> smtps,</code>)
by default on port 465.
<code> tls-require</code>
may be used to force clients to establish a secure connection
before being allowed to start an SMTP transaction.
If
<code> tls-require verify</code>
is specified, the client must provide a valid certificate to be
able to establish an SMTP session.
<code> secure</code>
may be specified to provide both STARTTLS and SMTPS services.
Host certificates may be used for these connections,
and must be previously declared using the pki directive.
If
<code> pki</code>
is specified,
a certificate matching
<code> name</code>
is searched for.
Moreover, a previously declared
<code> ca</code>
directive may be specified to use a custom CA certificate.
If the
<code> auth</code>
parameter is used,
then a client may only start an SMTP transaction after a
successful authentication.
Any remote sender that passed SMTPAUTH is treated as if
it was the server's local user that was sending the mail.
This means that filter rules using
<code> from local</code>
will be matched.
If
<code> auth-optional</code>
is specified, then SMTPAUTH is not required to establish an
SMTP transaction.
This is only useful to let a listener accept incoming mail from
untrusted senders and outgoing mail from authenticated users in
situations where it is not possible to listen on the submission
port.
Both
<code> auth</code>
and
<code> auth-optional</code>
accept an optional table as a parameter.
When provided, credentials are looked up in this table.
The credentials format is described in
<code><a href="//www.systutorials.com/docs/linux/man/5-table/">table</a></code>(5).
If the
<code> tag</code>
parameter is used, then clients connecting to the listener will be
tagged
<i>tag</i>.
If the
<code> hostname</code>
parameter is used, then it will be used in the greeting banner
instead of the default server name.
The
<code> hostnames</code>
parameter overrides the server name for specific addresses.
Table
<i>names</i>
contains a mapping of IP addresses to hostnames and
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will use the hostname that matches the address on which the connection arrives
if it is found in the mapping.
If the
<code> senders</code>
parameter is used, then
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
will look up a mapping of username to email addresses to see whether
the authenticated user is allowed to submit mail
as the sender that was provided in the SMTP session.
In addition, if the masquerade option is provided,
the From header will be rewritten
to match the sender provided in the SMTP session.
If the
<code> mask-source</code>
parameter is used, then the listener will skip the
<code> from</code>
part when prepending the
``Received''
header.
If the
<code> received-auth</code>
parameter is used, the
``Received''
header will display if the session was authenticated and by which local user.
If the
<code> no-dsn</code>
parameter is used, DSN (Delivery Status Notification) extension will not
be enabled.
<dl><dt><code> max-message-size </code><i>n</i><dd>Specify a maximum message size of
<i>n</i>
bytes.
The argument may contain a multiplier, as documented in
<code><a href="//www.systutorials.com/docs/linux/man/3-scan_scaled/">scan_scaled</a></code>(3).
The default maximum message size is 35MB if none is specified.
<dt><code> pki </code><i>hostname</i> <code> certificate </code><i>certfile</i><dd>Associate the certificate located in
<i>certfile</i>
with
<i>hostname</i>.
</dl>
If a fallback certificate or SNI is wanted, the
Sq *
wildcard may be used as
<i>hostname</i>.
A certificate chain may be created by appending one or many certificates,
including a Certificate Authority certificate,
to
<i>certfile</i>.
Creation of certificates is documented in
<code><a href="//www.systutorials.com/docs/linux/man/8-starttls/">starttls</a></code>(8).
<dl><dt><code> pki </code><i>hostname</i> <code> key </code><i>keyfile</i><dd>Associate the key located in
<i>keyfile</i>
with
<i>hostname</i>.
<dt><code> pki </code><i>hostname</i> <code> dhe </code><i>params</i><dd>Specify the DHE parameters to use for DHE cipher suites with
<i>hostname</i>.
Valid parameter values are none, legacy and auto.
For legacy a fixed key length of 1024 bits is used, whereas for auto the key
length is determined automatically.
The default is none, which disables DHE cipher suites.
<dt><code> queue compression</code><dd>Enable transparent compression of envelopes and messages.
The only supported algorithm at the moment is gzip.
Envelopes and messages may be inspected using the
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8)
or
<code><a href="//www.systutorials.com/docs/linux/man/1-gzcat/">gzcat</a></code>(1)
utilities.
<dt><code> queue encryption [key </code><i>key</i>]<dd>Enable transparent encryption of envelopes and messages.
<i>key</i>
must be a 16-byte random key in hexadecimal representation.
It can be obtained using the
<code><a href="//www.systutorials.com/docs/linux/man/1-openssl/">openssl</a></code>(1)
utility as follow:
<dl><dt><dd>$ openssl rand -hex 16
</dl></dl>
If the
<i>key</i>
parameter is not specified, it is read with
<code><a href="//www.systutorials.com/docs/linux/man/3-getpass/">getpass</a></code>(3)
at startup.
If
<i>key</i>
is
<code> stdin,</code>
then it is read from the standard input at startup.
The only supported algorithm is AES-256 in GCM mode.
Envelopes and messages may be inspected using the
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpctl/">smtpctl</a></code>(8)
utility.
Queue encryption can be used with queue compression and will always
perform compression before encryption.
<dl><dt><code> table </code><i>name</i> [<i>type</i>:] <i>config</i><dd>Tables are used to provide additional configuration information for
<code><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a></code>(8)
in the form of lists or key-value mappings.
The format of the entries depends on what the table is used for.
Refer to
<code><a href="//www.systutorials.com/docs/linux/man/5-table/">table</a></code>(5)
for the exhaustive documentation.
</dl>
The table is identified using table name
<i>name</i>;
the name itself is arbitrarily chosen.
<i>type</i>
specifies the table backend,
and should be one of the following:
<dl><dt><dd><dl><dt>db<dd>Information is stored in a file created using
<code><a href="//www.systutorials.com/docs/linux/man/8-makemap/">makemap</a></code>(8).
<dt>file<dd>Information is stored in a plain text file using the
same format as used to generate
<code><a href="//www.systutorials.com/docs/linux/man/8-makemap/">makemap</a></code>(8)
mappings.
This is the default.
</dl></dl>
<i>config</i>
specifies a configuration file for the table data.
It must be an absolute path to a file for the
``file''
and
``db''
table types.
<dl><dt><code> table </code><i>name</i> {<i>value</i> [, <i>...</i>]}<dd>Tables containing list of static values may be declared
using an inlined notation.
</dl>
The table is identified using table name
<i>name</i>;
the name itself is arbitrarily chosen.
The table must contain at least one value and may declare many values as a
list of comma-separated strings.
<dl><dt><code> table </code><i>name</i> {<i>key</i>=<i>value</i> [, <i>...</i>]}<dd>Tables containing static key-value mappings may be declared
using an inlined notation.
</dl>
The table is identified using table name
<i>name</i>;
the name itself is arbitrarily chosen.
The table must contain at least one key-value mapping and may declare
many mappings as a list of comma-separated
<i>key</i>=<i>value</i>
descriptions.
</dl></pre>
<h3>Format Specifiers</h3>
<p>Some configuration directives support expansion of their parameters at runtime. Such directives (for example <code> deliver to maildir,</code> <code> deliver to mda)</code> may use format specifiers which will be expanded before delivery or relaying. The following formats are currently supported:</p>
<dl>
<dd>
<dl>
<dt>%{sender} Ta sender email address</p>
<dd>
<dt>%{sender.user} Ta user part of the sender email address</p>
<dd>
<dt>%{sender.domain} Ta domain part of the sender email address</p>
<dd>
<dt>%{rcpt} Ta recipient email address</p>
<dd>
<dt>%{rcpt.user} Ta user part of the recipient email address</p>
<dd>
<dt>%{rcpt.domain} Ta domain part of the recipient email address</p>
<dd>
<dt>%{dest} Ta recipient email address after expansion</p>
<dd>
<dt>%{dest.user} Ta user part after expansion</p>
<dd>
<dt>%{dest.domain} Ta domain part after expansion</p>
<dd>
<dt>%{user.username} Ta local user</p>
<dd>
<dt>%{user.directory} Ta home directory of the local user</p>
<dd></dl>
</dl>
<p> Expansion formats also support partial expansion using the optional bracket notations with substring offset. For example, with recipient domain &#8220;example.org :&#8221;</p>
<dl>
<dd>
<dl>
<dt>%{rcpt.domain[0]} Ta expands to &#8220;e&#8221;</p>
<dd>
<dt>%{rcpt.domain[1]} Ta expands to &#8220;x&#8221;</p>
<dd>
<dt>%{rcpt.domain[8:]} Ta expands to &#8220;org&#8221;</p>
<dd>
<dt>%{rcpt.domain[-3:]} Ta expands to &#8220;org&#8221;</p>
<dd>
<dt>%{rcpt.domain[0:6]} Ta expands to &#8220;example&#8221;</p>
<dd>
<dt>%{rcpt.domain[0:-4]} Ta expands to &#8220;example&#8221;</p>
<dd></dl>
</dl>
<p> In addition, modifiers may be applied to the token. For example, with recipient &#8220;User+Tag [at] Example.org :&#8221;</p>
<dl>
<dd>
<dl>
<dt>%{rcpt:lowercase} Ta expands to &#8220;user+tag [at] example.org&#8221;</p>
<dd>
<dt>%{rcpt:uppercase} Ta expands to &#8220;USER+TAG [at] EXAMPLE.ORG&#8221;</p>
<dd>
<dt>%{rcpt:strip} Ta expands to &#8220;User [at] Example.org&#8221;</p>
<dd>
<dt>%{rcpt:lowercase|strip} Ta expands to &#8220;user [at] example.org&#8221;</p>
<dd></dl>
</dl>
<p> For security concerns, expanded values are sanitized and potentially dangerous characters are replaced with Sq :. In situations where they are desirable, the &#8220;raw&#8221; modifier may be applied. For example, with recipient &#8220;user+t?g@example.org :&#8221;</p>
<dl>
<dd>
<dl>
<dt>%{rcpt} Ta expands to &#8220;user+t:g@example.org&#8221;</p>
<dd>
<dt>%{rcpt:raw} Ta expands to &#8220;user+t?g@example.org&#8221;</p>
<dd></dl>
</dl>
<h2>Files</h2>
<dl>
<dd>
<dl>
<dt><code>/etc/opensmtpd/smtpd.conf</code></p>
<dd>Default <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) configuration file.</p>
<dt><code>/etc/opensmtpd/mailname</code></p>
<dd>If this file exists, the first line is used as the server name. Otherwise, the server name is derived from the local hostname returned by <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3), either directly if it is a fully qualified domain name, or by retrieving the associated canonical name through <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3).</p>
<dt><code>/var/spool/smtpd/</code></p>
<dd>Spool directories for mail during processing.</dl>
</dl>
<h2>Examples</h2>
<p>The default <code>smtpd.conf</code> file listens on the loopback network interface (lo0), and allows for mail from users and daemons on the local machine, as well as permitting email to remote servers. Some more complex configurations are given below. </p>
<p> This first example is the same as the default configuration, but all outgoing mail is forwarded to a remote SMTP server. A secrets file is needed to specify a username and password:</p>
<dl>
<dd>
<pre># touch /etc/opensmtpd/secrets
# chmod 640 /etc/opensmtpd/secrets
# chown root:_smtpd /etc/opensmtpd/secrets
# echo &quot;label username:password&quot; &gt; /etc/opensmtpd/secrets
</dl>
<code>smtpd.conf</code>
would look like this:
<dl><dt><dd>table aliases file:/etc/opensmtpd/aliases
table secrets file:/etc/opensmtpd/secrets
listen on lo0
accept for local alias &lt;aliases&gt; deliver to mbox
accept for any relay via tls+<a href="auth://label@smtp.example.com">auth://label@smtp.example.com</a> \
 auth &lt;secrets&gt;
</dl>
In this second example,
the aim is to permit mail relaying for any user that can authenticate
using their normal login credentials.
An RSA certificate must be provided to prove the server's identity.
The mail server listens on all interfaces the default route(s) point to.
Mail with a local destination should be sent to an external mda.
First, the RSA certificate is created:
<dl><dt><dd># openssl genrsa -out /etc/ssl/private/mail.example.com.key 4096
# openssl req -new -x509 -key /etc/ssl/private/mail.example.com.key \
 -out /etc/ssl/mail.example.com.crt -days 365
# chmod 600 /etc/ssl/mail.example.com.crt
# chmod 600 /etc/ssl/private/mail.example.com.key
</dl>
In the example above,
a certificate valid for one year was created.
The configuration file would look like this:
<dl><dt><dd>pki mail.example.com certificate &quot;/etc/ssl/mail.example.com.crt&quot;
pki mail.example.com key &quot;/etc/ssl/private/mail.example.com.key&quot;
table aliases file:/etc/opensmtpd/aliases
listen on lo0
listen on egress tls pki mail.example.com auth
accept for local alias &lt;aliases&gt; deliver to mda &quot;/path/to/mda -f -&quot;
accept from any for domain example.com \
 deliver to mda &quot;/path/to/mda -f -&quot;
accept for any relay
</dl>
For sites that wish to sign messages using DKIM, the
<i>dkimproxy</i>
package may be used as a filter.
The following example is the same as the default configuration,
but all outgoing mail is passed to dkimproxy_out on port 10027
for signing.
The signed messages are received on port 10028 and tagged for relaying.
<dl><dt><dd>table aliases file:/etc/opensmtpd/aliases
listen on lo0
listen on lo0 port 10028 tag DKIM
accept for local alias &lt;aliases&gt; deliver to mbox
accept tagged DKIM for any relay
accept from local for any relay via <a href="smtp://127.0.0.1:10027">smtp://127.0.0.1:10027</a>
</dl>
Sites that accept non-local messages may be able to cut down on the
volume of spam received by rejecting forged messages that claim
to be from the local domain.
The table
<i>other-relays</i>
can be used to specify the IP addresses of relays that may legitimately
originate mail with your domain as the sender.
<dl><dt><dd>table aliases file:/etc/opensmtpd/aliases
table other-relays file:/etc/opensmtpd/other-relays
listen on lo0
listen on egress
accept for local alias &lt;aliases&gt; deliver to mbox
accept from local for any relay
reject from ! source &lt;other-relays&gt; sender &quot;@example.com&quot; for any
accept from any for domain example.com \
 alias &lt;aliases&gt; deliver to mbox
</dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-mailer-conf/">mailer.conf</a></code>(5), <code><a href="/docs/linux/man/5-table/">table</a></code>(5), <code><a href="/docs/linux/man/8-makemap/">makemap</a></code>(8), <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8)</p>
<h2>History</h2>
<p><code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) first appeared in OpenBSD 4.6.</p>
