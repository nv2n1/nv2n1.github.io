---
title: "aliases-opensmtpd(5)"
name: "aliases-opensmtpd"
section: "5"
letter: "a"
url: "/docs/linux/man/5-aliases-opensmtpd/"
description: "aliases – aliases file for smtpd"
---

<p><code>aliases</code> &#8211; aliases file for smtpd</p>
<h2>Description</h2>
<p>This manual page describes the format of the <code>aliases</code> file, as used by <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8). An alias in its simplest form is used to assign an arbitrary name to an email address, or a group of email addresses. This provides a convenient way to send mail. For example an alias could refer to all users of a group: email to that alias would be sent to all members of the group. Much more complex aliases can be defined however: an alias can refer to other aliases, be used to send mail to a file instead of another person, or to execute various commands. </p>
<p> Within the file, Ql # is a comment delimiter; anything placed after it is discarded. The file consists of key/value mappings of the form: -filled -offset indent key: value1, value2, value3, &#8230; </p>
<p> <i>key</i> is always folded to lowercase before alias lookups to ensure that there can be no ambiguity. The key is expanded to the corresponding values, which consist of one or more of the following:</p>
<dl>
<dd>
<dl>
<dt><i>user</i></p>
<dd>A user on the host machine. The user must have a valid entry in the <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) database file.</p>
<dt><i>/path/to/file</i></p>
<dd>Append messages to <i>file</i>, specified by its absolute pathname.</p>
<dt>| <i>command</i></p>
<dd>Pipe the message to <i>command</i> on its standard input. The command is run under the privileges of the daemon&#8217;s unprivileged account.</p>
<dt>: <i>include</i>: <i>/path/to/file</i></p>
<dd>Include any definitions in <i>file</i> as alias entries. The format of the file is identical to this one.</p>
<dt><i>user-part [at] domain-part</i></p>
<dd>An email address in RFC 5322 format (see <code><a href="/docs/linux/man/7-mailaddr/">mailaddr</a></code>(7)). If an address extension is appended to the user-part, it is first compared for an exact match. It is then stripped so that an address such as user+ext [at] example.com will only use the part that precedes Sq + as a <i>key.</i></p>
<dt><i>error</i>: <i>code</i> <i>message</i></p>
<dd>A status code and message to return. The code must be 3 digits, starting 4XX (TempFail) or 5XX (PermFail). The message must be present and can be freely chosen.</p>
<dt><i>maildir</i>: <i>/path</i></p>
<dd>Deliver messages to Maildir at the <i>path</i>.</dl>
</dl>
<h2>Files</h2>
<dl>
<dd>
<dl>
<dt><code>/etc/opensmtpd/aliases</code></p>
<dd>Default <code>aliases</code> file.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5), <code><a href="/docs/linux/man/8-makemap/">makemap</a></code>(8), <code><a href="/docs/linux/man/8-newaliases/">newaliases</a></code>(8), <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8)</p>
<h2>History</h2>
<p>The <code>aliases</code> file format appeared in Bx 4.0.</p>
