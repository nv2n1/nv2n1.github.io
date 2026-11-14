---
title: "mongoc_ssl_opt_t(3)"
name: "mongoc_ssl_opt_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_ssl_opt_t/"
description: "mongoc_ssl_opt_t – typedef struct { const char *pem_file; const char *pem_pwd; const char *ca_file; const char *ca_dir; const char *crl_file; bool weak_cert_validation; void *padding [8]; } mongoc_..."
---

<p>mongoc_ssl_opt_t &#8211; typedef struct {<br />
const char&nbsp;<wbr>*pem_file;<br />
const char&nbsp;<wbr>*pem_pwd;<br />
const char&nbsp;<wbr>*ca_file;<br />
const char&nbsp;<wbr>*ca_dir;<br />
const char&nbsp;<wbr>*crl_file;<br />
bool&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>weak_cert_validation;<br />
void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*padding&nbsp;<wbr>[8]; } mongoc_ssl_opt_t;</p>
<h2>Synopsis</h2>
<pre>typedef struct
{
 const char *pem_file;
 const char *pem_pwd;
 const char *ca_file;
 const char *ca_dir;
 const char *crl_file;
 bool weak_cert_validation;
 void *padding [8];
} mongoc_ssl_opt_t;</pre>
<h2>Description</h2>
<p>This structure is used to set the SSL options for a <code>mongoc_client_t</code> or <code>mongoc_client_pool_t</code> \&amp;. </p>
<p> Beginning in version 1.2.0, once a pool or client has any SSL options set, all connections use SSL, even if &quot;ssl=true&quot; is omitted from the MongoDB URI. Before, SSL options were ignored unless &quot;ssl=true&quot; was included in the URI. </p>
<h2>See Also</h2>
<dl COMPACT>
<dt>\[bu]</p>
<dd>
<dt>\[bu]</p>
<dd><code></dl>
<p> </code></p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
