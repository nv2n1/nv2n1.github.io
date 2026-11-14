---
title: "mech(5)"
name: "mech"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mech/"
description: "mech qop – GSS-API Mechanism and QOP files"
---

<p><code>mech</code> <code>qop</code> &#8211; GSS-API Mechanism and QOP files</p>
<h2>Synopsis</h2>
<p>/etc/gss/mech /etc/gss/qop</p>
<h2>Description</h2>
<p>The /etc/gss/mech file contains a list of installed GSS-API security mechanisms. Each line of the file either contains a comment if the first character is &#8216;#&#8217; or it contains five fields with the following meanings:</p>
<dl>
<dt><code>Name</code></p>
<dd>The name of this GSS-API mechanism.</p>
<dt><code>Object identifier</code></p>
<dd>The OID for this mechanism.</p>
<dt><code>Library</code></p>
<dd>A shared library containing the implementation of this mechanism.</p>
<dt><code>Kernel module (optional)</code></p>
<dd>A kernel module containing the implementation of this mechanism (not yet supported in FreeBSD).</p>
<dt><code>Library options (optional)</code></p>
<dd>Optionsal parameters interpreted by the mechanism. Library options must be enclosed in brackets ([ ]) to differentiate them from the optional kernel module entry.</dl>
<p> The /etc/gss/qop file contains a list of Quality of Protection values for use with GSS-API. Each line of the file either contains a comment if the first character is &#8216;#&#8217; or it contains three fields with the following meanings:</p>
<dl>
<dt><code>QOP string</code></p>
<dd>The name of this Quality of Protection algorithm.</p>
<dt><code>QOP value</code></p>
<dd>The numeric value used to select this algorithm for use with GSS-API functions such as gss_get_mic3.</p>
<dt><code>Mechanism name</code></p>
<dd>The GSS-API mechanism name that corresponds to this algorithm.</dl>
<h2>Examples</h2>
<p>This is a typical entry from /etc/gss/mech </p>
<pre>kerberosv5 1.2.840.113554.1.2.2 /usr/lib/libgssapi_krb5.so.8 -</pre>
<p>This is a typical entry from /etc/gss/qop </p>
<pre>GSS_KRB5_CONF_C_QOP_DES 0x0100 kerberosv5</pre>
<h2>History</h2>
<p>The manual page example first appeared in Fx 7.0 .</p>
<h2>Authors</h2>
<p>This manual page was written by An Doug Rabson Aq dfr [at] FreeBSD.org .</p>
