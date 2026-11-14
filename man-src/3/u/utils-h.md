---
title: "utils-h(3)"
name: "utils-h"
section: "3"
letter: "u"
url: "/docs/linux/man/3-utils-h/"
description: "utils.h –"
---

<p>utils.h &#8211; </p>
<p> C wrapper for DMLite utils.</p>
<h2>Synopsis</h2>
<pre><code>
#include 'any.h'

#include 'dmlite/common/config.h'

#include &lt;limits.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<h3>Data Structures</h3>
<pre><code>struct dmlite_url


Handles URL.


struct dmlite_aclentry


Handles ACL entries.



Macros
#define ACL_ENTRIES_MAX   300



#define ACL_SIZE   13



#define CSUMTYPE_MAX   3



#define CSUMVALUE_MAX   33



#define GUID_MAX   36



#define HOST_NAME_MAX   _POSIX_HOST_NAME_MAX



#define QUERY_MAX   1024



#define SCHEME_MAX   7



#define URL_MAX   8192



#define ACL_USER_OBJ   1



#define ACL_USER   2



#define ACL_GROUP_OBJ   3



#define ACL_GROUP   4



#define ACL_MASK   5



#define ACL_OTHER   6



#define ACL_DEFAULT   0x20



Typedefs</code></pre>
<p> typedef struct <code>dmlite_url</code> <code>dmlite_url</code><br />
 <i>Handles URL. </i><br />
 typedef struct <code>dmlite_aclentry</code> <code>dmlite_aclentry</code><br />
 <i>Handles ACL entries. </i></p>
<h3>Functions</h3>
<p><code>dmlite_url</code> * <code>dmlite_url_new</code> (void)<br />
 <i>Creates a new </i><code>dmlite_url</code>.<br />
 <code>dmlite_url</code> * <code>dmlite_parse_url</code> (const char *source)<br />
 <i>Parses a URL. </i><br />
 void <code>dmlite_url_free</code> (<code>dmlite_url</code> *url)<br />
 <i>Frees the given url. </i><br />
 char * <code>dmlite_url_serialize</code> (<code>dmlite_url</code> *url, char *buffer, size_t bsize)<br />
 <i>Serializes a URL. </i><br />
 void <code>dmlite_serialize_acls</code> (unsigned nEntries, <code>dmlite_aclentry</code> *acl, char *buffer, size_t bsize)<br />
 <i>Serializes into a string a set of ACL entries. </i><br />
 void <code>dmlite_deserialize_acl</code> (const char *buffer, unsigned *nEntries, <code>dmlite_aclentry</code> **acl)<br />
 <i>Deserializes a string into an array of ACL entries. </i><br />
 void <code>dmlite_acl_free</code> (unsigned nEntries, <code>dmlite_aclentry</code> *acl)<br />
 <i>Frees an array of ACL entries as returned by dm_deserialize_acls. </i></p>
<h2>Detailed Description</h2>
<p>C wrapper for DMLite utils. </p>
<p> <code>Author:</code></p>
<dl>
<dd>Alejandro Álvarez Ayllon aalvarez [at] cern.ch</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define ACL_DEFAULT 0x20</h3>
<h3>#define ACL_ENTRIES_MAX 300</h3>
<h3>#define ACL_GROUP 4</h3>
<h3>#define ACL_GROUP_OBJ 3</h3>
<h3>#define ACL_MASK 5</h3>
<h3>#define ACL_OTHER 6</h3>
<h3>#define ACL_SIZE 13</h3>
<h3>#define ACL_USER 2</h3>
<h3>#define ACL_USER_OBJ 1</h3>
<h3>#define CSUMTYPE_MAX 3</h3>
<h3>#define CSUMVALUE_MAX 33</h3>
<h3>#define GUID_MAX 36</h3>
<h3>#define HOST_NAME_MAX _POSIX_HOST_NAME_MAX</h3>
<h3>#define QUERY_MAX 1024</h3>
<h3>#define SCHEME_MAX 7</h3>
<h3>#define URL_MAX 8192</h3>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>dmlite_aclentry</code> <code>dmlite_aclentry</code></h3>
<p>Handles ACL entries.</p>
<h3>typedef struct <code>dmlite_url</code> <code>dmlite_url</code></h3>
<p>Handles URL.</p>
<h2>Function Documentation</h2>
<h3>void dmlite_acl_free (unsignednEntries, <code>dmlite_aclentry</code> *acl)</h3>
<p>Frees an array of ACL entries as returned by dm_deserialize_acls. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>nEntries</i> The number of entries in the array.<br />
 <i>acl</i> The ACL.</dl>
<h3>void dmlite_deserialize_acl (const char *buffer, unsigned *nEntries, <code>dmlite_aclentry</code> **acl)</h3>
<p>Deserializes a string into an array of ACL entries. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buffer</i> The string.<br />
 <i>nEntries</i> The resulting number of ACL entries.<br />
 <i>acl</i> The resulting ACL.</dl>
<h3><code>dmlite_url</code>* dmlite_parse_url (const char *source)</h3>
<p>Parses a URL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>source</i> Original URL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Parsed URL.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>dest-&gt;query must be NULL for the first call, so it is internally allocated.</dl>
<h3>void dmlite_serialize_acls (unsignednEntries, <code>dmlite_aclentry</code> *acl, char *buffer, size_tbsize)</h3>
<p>Serializes into a string a set of ACL entries. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>nEntries</i> The number of ACL entries in the array.<br />
 <i>acl</i> The ACL.<br />
 <i>buffer</i> Where to put the resulting string.<br />
 <i>bsize</i> The buffer size.</dl>
<h3>void dmlite_url_free (<code>dmlite_url</code> *url)</h3>
<p>Frees the given url. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>url</i> The url to free.</dl>
<h3><code>dmlite_url</code>* dmlite_url_new (void)</h3>
<p>Creates a new <code>dmlite_url</code>.</p>
<h3>char* dmlite_url_serialize (<code>dmlite_url</code> *url, char *buffer, size_tbsize)</h3>
<p>Serializes a URL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>url</i> The url to serialize.<br />
 <i>buffer</i> Where to put the serialized version.<br />
 <i>bsize</i> The buffer size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Buffer, NULL on error.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for dmlite from the source code.</p>
