---
title: "globus_uuid(3)"
name: "globus_uuid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_uuid/"
description: "Globus UUID Generator –"
---

<h2 class="name">NAME</h2>
<p> Globus UUID Generator &#8211; </p>
<p> UUIDs.</p>
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
<p> UUIDs. </p>
<h2>Function Documentation</h2>
<h3>int globus_uuid_fields (globus_uuid_t *uuid, globus_uuid_fields_t *uuid_fields)</h3>
<p> Extract fields from UUID </p>
<p> Copy the fields from uuid to uuid_fields in host byte order. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>uuid</i> Pointer to a uuid.<br />
 <i>uuid_fields</i> Pointer to uuid fields.</dl>
<h3>int globus_uuid_import (globus_uuid_t *uuid, const char *str)</h3>
<p> Import a UUID </p>
<p> Import a string in the text UUID format into a globus_uuid_t value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>uuid</i> UUID to modify<br />
 <i>str</i> A string at least GLOBUS_UUID_TEXTLEN long and be in the format like 1b4e28ba-2fa1-11d2-883f-b9a761bde3fb</dl>
<p> 1b4e28ba-2fa1-11d2-883f-b9a761bde3fb 012345678901234567890123456789012345 0 1 2 3</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
