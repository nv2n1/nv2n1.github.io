---
title: "dmlite_credentials(3)"
name: "dmlite_credentials"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmlite_credentials/"
description: "dmlite_credentials –"
---

<h2 class="name">NAME</h2>
<p> dmlite_credentials &#8211; </p>
<p> Security credentials.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;dmlite.h&gt;</p>
<h3>Data Fields</h3>
<p> const char * <code>mech</code> </p>
<p> const char * <code>client_name</code> </p>
<p> const char * <code>remote_address</code> </p>
<p> const char * <code>session_id</code> </p>
<p> unsigned <code>nfqans</code> </p>
<p> const char ** <code>fqans</code> </p>
<p> <code>dmlite_any_dict</code> * <code>extra</code> </p>
<h2>Detailed Description</h2>
<p> Security credentials. </p>
<p> It is up to the caller to allocate and free this pointers. DMLite will keep a copy internaly. Non used values MUST be NULL.</p>
<h2>Field Documentation</h2>
<h3>const char* client_name</h3>
<h3><code>dmlite_any_dict</code>* extra</h3>
<h3>const char** fqans</h3>
<h3>const char* mech</h3>
<h3>unsigned nfqans</h3>
<h3>const char* remote_address</h3>
<h3>const char* session_id</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for dmlite from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
