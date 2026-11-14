---
title: "globus_uuid_create(3)"
name: "globus_uuid_create"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_uuid_create/"
description: "globus_uuid.h –"
---

<h2 class="name">NAME</h2>
<p> globus_uuid.h &#8211; </p>
<p> Globus UUID Generator.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_libc.h&#8217; </p>
<h3>Functions</h3>
<p> int <code>globus_uuid_create</code> (globus_uuid_t *uuid)<br />
 <i>Create UUID</i> </p>
<p> Creates a time based, Leach-Salz variant uuid, using the mac address when available. &quot;<br />
 int <code>globus_uuid_import</code> (globus_uuid_t *uuid, const char *str)<br />
 <i>Import a UUID</i> </p>
<p> Import a string in the text UUID format into a globus_uuid_t value. &quot;<br />
 int <code>globus_uuid_fields</code> (globus_uuid_t *uuid, globus_uuid_fields_t *uuid_fields)<br />
 <i>Extract fields from UUID</i> </p>
<p> Copy the fields from uuid to uuid_fields in host byte order. &quot;</p>
<h2>Detailed Description</h2>
<p> Globus UUID Generator. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
