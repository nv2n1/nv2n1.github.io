---
title: "kvno(1)"
name: "kvno"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kvno/"
description: "kvno – print key version numbers of Kerberos principals"
---

<h2>NAME</h2>
<p> kvno &#8211; print key version numbers of Kerberos principals</p>
<h2>SYNOPSIS</h2>
<p> <code>kvno</code> [<code>-c</code> <i>ccache</i>] [<code>-e</code> <i>etype</i>] [<code>-q</code>] [<code>-h</code>] [<code>-P</code>] [<code>-S</code> <i>sname</i>] [<code>-U</code> <i>for_user</i>] <i>service1 service2</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> kvno acquires a service ticket for the specified Kerberos principals and prints out the key version numbers of each.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>ccache</i></dt>
<dd> Specifies the name of a credentials cache to use (if not the default)</dd>
<dt><code>-e</code> <i>etype</i></dt>
<dd> Specifies the enctype which will be requested for the session key of all the services named on the command line. This is useful in certain backward compatibility situations.</dd>
<dt><code>-q</code></dt>
<dd> Suppress printing output when successful. If a service ticket cannot be obtained, an error message will still be printed and kvno will exit with nonzero status.</dd>
<dt><code>-h</code></dt>
<dd> Prints a usage statement and exits.</dd>
<dt><code>-P</code></dt>
<dd> Specifies that the <i>service1 service2</i> &#8230; arguments are to be treated as services for which credentials should be acquired using constrained delegation. This option is only valid when used in conjunction with protocol transition.</dd>
<dt><code>-S</code> <i>sname</i></dt>
<dd> Specifies that the <i>service1 service2</i> &#8230; arguments are interpreted as hostnames, and the service principals are to be constructed from those hostnames and the service name <i>sname</i>. The service hostnames will be canonicalized according to the usual rules for constructing service principals.</dd>
<dt><code>-U</code> <i>for_user</i></dt>
<dd> Specifies that protocol transition (S4U2Self) is to be used to acquire a ticket on behalf of <i>for_user</i>. If constrained delegation is not requested, the service name must match the credentials cache client principal.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> kvno uses the following environment variable:</p>
<dl>
<dt><code>KRB5CCNAME</code></dt>
<dd> Location of the credentials (ticket) cache.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>FILE:/tmp/krb5cc_%{uid}</code></dt>
<dd> Default location of the credentials cache</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i>, <i><a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
