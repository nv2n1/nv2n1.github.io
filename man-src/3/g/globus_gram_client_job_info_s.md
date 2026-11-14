---
title: "globus_gram_client_job_info_s(3)"
name: "globus_gram_client_job_info_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_client_job_info_s/"
description: "globus_gram_client_job_info_s –"
---

<h2 class="name">NAME</h2>
<p> globus_gram_client_job_info_s &#8211; </p>
<p> Extensible job information structure.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_gram_client.h&gt;</p>
<h3>Data Fields</h3>
<p> globus_hashtable_t <code>extensions</code> </p>
<p> char * <code>job_contact</code> </p>
<p> int <code>job_state</code> </p>
<p> int <code>protocol_error_code</code> </p>
<h2>Detailed Description</h2>
<p> Extensible job information structure. </p>
<p> The <code>globus_gram_client_job_info_t</code> data type is used to pass protocol extensions along with the standard job status information included in the GRAM2 protocol. This structure contains the information returned in job state callbacks plus a hash table of extension entries that contain #globus_gram_protocol_extension_t name-value pairs.</p>
<h2>Field Documentation</h2>
<h3>globus_hashtable_t globus_gram_client_job_info_s::extensions</h3>
<p> Table of extension values</p>
<h3>char* globus_gram_client_job_info_s::job_contact</h3>
<p> GRAM Job Contact String</p>
<h3>int globus_gram_client_job_info_s::job_state</h3>
<p> GRAM Job State</p>
<h3>int globus_gram_client_job_info_s::protocol_error_code</h3>
<p> GRAM Error Code </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_client from the source code. </p>
<h2>Index</h2>
