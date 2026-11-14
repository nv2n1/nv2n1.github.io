---
title: "libssh2_agent_get_identity(3)"
name: "libssh2_agent_get_identity"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_agent_get_identity/"
description: "libssh2_agent_get_identity – get a public key off the collection of public keys managed by ssh-agent"
---

<h2>NAME</h2>
<p> libssh2_agent_get_identity &#8211; get a public key off the collection of public keys managed by ssh-agent</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_agent_get_identity(LIBSSH2_AGENT *agent,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_agent_publickey&nbsp;<wbr>**store,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_agent_publickey&nbsp;<wbr>*prev);</p>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/3-libssh2_agent_get_identity/">libssh2_agent_get_identity</a>(3)</i> allows an application to iterate over all public keys in the collection managed by ssh-agent. </p>
<p> <i>store</i> should point to a pointer that gets filled in to point to the public key data. </p>
<p> <i>prev</i> is a pointer to a previous &#8216;struct libssh2_agent_publickey&#8217; as returned by a previous invoke of this function, or NULL to get the first entry in the internal collection.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if everything is fine and information about a host was stored in the <i>store</i> struct. </p>
<p> Returns 1 if it reached the end of public keys. </p>
<p> Returns negative values for error</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_agent_list_identities/">libssh2_agent_list_identities</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_agent_userauth/">libssh2_agent_userauth</a>(3)</code> </p>
<h2>Index</h2>
