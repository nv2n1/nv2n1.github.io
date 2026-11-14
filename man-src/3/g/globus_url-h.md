---
title: "globus_url-h(3)"
name: "globus_url-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_url-h/"
description: "globus_url.h –"
---

<p>globus_url.h &#8211; </p>
<p> URL Parsing.</p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>globus_url_t</code><br />
 <i>Parsed URLs.</i> </p>
<p> This structure contains the fields which were parsed from an string representation of an URL. There are no methods to access fields of this structure. &quot;</p>
<h3>Enumerations</h3>
<p>enum <code>globus_url_scheme_t</code> { <code>GLOBUS_URL_SCHEME_FTP</code> =0, <code>GLOBUS_URL_SCHEME_GSIFTP</code>, <code>GLOBUS_URL_SCHEME_HTTP</code>, <code>GLOBUS_URL_SCHEME_HTTPS</code>, <code>GLOBUS_URL_SCHEME_LDAP</code>, <code>GLOBUS_URL_SCHEME_FILE</code>, <code>GLOBUS_URL_SCHEME_X_NEXUS</code>, <code>GLOBUS_URL_SCHEME_X_GASS_CACHE</code>, <code>GLOBUS_URL_SCHEME_UNKNOWN</code>, <code>GLOBUS_URL_NUM_SCHEMES</code> }<br />
 <i>URL Schemes.</i> </p>
<p> The Globus URL library supports a set of URL schemes (protocols). This enumeration can be used to quickly dispatch a parsed URL based on a constant value. &quot;</p>
<h3>Functions</h3>
<p>int <code>globus_url_parse</code> (const char *url_string, <code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_parse_rfc1738</code> (const char *url_string, <code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_parse_loose</code> (const char *url_string, <code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_destroy</code> (<code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_copy</code> (<code>globus_url_t</code> *dest, const <code>globus_url_t</code> *src) </p>
<p> int <code>globus_url_get_scheme</code> (const char *url_string, <code>globus_url_scheme_t</code> *scheme_type) </p>
<h2>Detailed Description</h2>
<p>URL Parsing. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
