---
title: "globus_url_get_scheme(3)"
name: "globus_url_get_scheme"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_url_get_scheme/"
description: "URL String Parser –"
---

<h2 class="name">NAME</h2>
<p> URL String Parser &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_url_t</code><br />
 <i>Parsed URLs.</i> </p>
<p> This structure contains the fields which were parsed from an string representation of an URL. There are no methods to access fields of this structure. &quot;</p>
<h3>Enumerations</h3>
<p> enum <code>globus_url_scheme_t</code> { <code>GLOBUS_URL_SCHEME_FTP</code> =0, <code>GLOBUS_URL_SCHEME_GSIFTP</code>, <code>GLOBUS_URL_SCHEME_HTTP</code>, <code>GLOBUS_URL_SCHEME_HTTPS</code>, <code>GLOBUS_URL_SCHEME_LDAP</code>, <code>GLOBUS_URL_SCHEME_FILE</code>, <code>GLOBUS_URL_SCHEME_X_NEXUS</code>, <code>GLOBUS_URL_SCHEME_X_GASS_CACHE</code>, <code>GLOBUS_URL_SCHEME_UNKNOWN</code>, <code>GLOBUS_URL_NUM_SCHEMES</code> }<br />
 <i>URL Schemes.</i> </p>
<p> The Globus URL library supports a set of URL schemes (protocols). This enumeration can be used to quickly dispatch a parsed URL based on a constant value. &quot;</p>
<h3>Functions</h3>
<p> int <code>globus_url_parse</code> (const char *url_string, <code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_parse_rfc1738</code> (const char *url_string, <code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_parse_loose</code> (const char *url_string, <code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_destroy</code> (<code>globus_url_t</code> *url) </p>
<p> int <code>globus_url_get_scheme</code> (const char *url_string, <code>globus_url_scheme_t</code> *scheme_type) </p>
<p> int <code>globus_url_copy</code> (<code>globus_url_t</code> *dst, const <code>globus_url_t</code> *src) </p>
<h2>Detailed Description</h2>
<p> The Globus URL functions provide a simple mechanism for parsing a URL string into a data structure, and for determining the scheme of an URL string.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_url_scheme_t</code></h3>
<p> URL Schemes. </p>
<p> The Globus URL library supports a set of URL schemes (protocols). This enumeration can be used to quickly dispatch a parsed URL based on a constant value. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_url_t::scheme_type</code></dl>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_URL_SCHEME_FTP </i></p>
<dd> File Transfer Protocol</p>
<dt><i>GLOBUS_URL_SCHEME_GSIFTP </i></p>
<dd> GSI-enhanced File Transfer Protocol</p>
<dt><i>GLOBUS_URL_SCHEME_HTTP </i></p>
<dd> HyperText Transfer Protocol</p>
<dt><i>GLOBUS_URL_SCHEME_HTTPS </i></p>
<dd> Secure HyperText Transfer Protocol</p>
<dt><i>GLOBUS_URL_SCHEME_LDAP </i></p>
<dd> Lightweight Directory Access Protocol</p>
<dt><i>GLOBUS_URL_SCHEME_FILE </i></p>
<dd> File Location</p>
<dt><i>GLOBUS_URL_SCHEME_X_NEXUS </i></p>
<dd> Nexus endpoint</p>
<dt><i>GLOBUS_URL_SCHEME_X_GASS_CACHE </i></p>
<dd> GASS Cache Entry</p>
<dt><i>GLOBUS_URL_SCHEME_UNKNOWN </i></p>
<dd> Any other URL of the form <code>scheme</code>://<code>something</code></p>
<dt><i>GLOBUS_URL_NUM_SCHEMES </i></p>
<dd> Total number of URL schemes supported</dl>
<h2>Function Documentation</h2>
<h3>int globus_url_copy (<code>globus_url_t</code> *dst, const <code>globus_url_t</code> *src)</h3>
<p> Create a copy of an URL structure. </p>
<p> This function copies the contents of a url structure into another. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dst</i> The URL structure to be populated with a copy of the contents of src.<br />
 <i>src</i> The original URL.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The URL was successfully copied.<br />
 <i>GLOBUS_URL_ERROR_NULL_URL</i> One of the URLs was GLOBUS_NULL.<br />
 <i>GLOBUS_URL_ERROR_OUT_OF_MEMORY;</i> The library was unable to allocate memory to create the the <code>globus_url_t</code> contents.</dl>
<h3>int globus_url_destroy (<code>globus_url_t</code> *url)</h3>
<p> Destroy a <code>globus_url_t</code> structure. </p>
<p> This function frees all memory associated with a <code>globus_url_t</code> structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> The url structure to destroy</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The URL was successfully destroyed.</dl>
<h3>int globus_url_get_scheme (const char *url_string, <code>globus_url_scheme_t</code> *scheme_type)</h3>
<p> Get the scheme of an URL. </p>
<p> This function determines the scheme type of the url string, and populates the variable pointed to by second parameter with that value. This performs a less expensive parsing than <code>globus_url_parse()</code> and is suitable for applications which need only to choose a handler based on the URL scheme. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url_string</i> The string containing the URL.<br />
 <i>scheme_type</i> A pointer to a globus_url_scheme_t which will be set to the scheme.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The URL scheme was recogized, and scheme_type has been updated.<br />
 <i>GLOBUS_URL_ERROR_BAD_SCHEME</i> The URL scheme was not recogized.</dl>
<h3>int globus_url_parse (const char *url_string, <code>globus_url_t</code> *url)</h3>
<p> Parse a string containing a URL into a <code>globus_url_t</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url_string</i> String to parse<br />
 <i>url</i> Pointer to <code>globus_url_t</code> to be filled with the fields of the url</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The string was successfully parsed.<br />
 <i>GLOBUS_URL_ERROR_NULL_STRING</i> The url_string was GLOBUS_NULL.<br />
 <i>GLOBUS_URL_ERROR_NULL_URL</i> The URL pointer was GLOBUS_NULL.<br />
 <i>GLOBUS_URL_ERROR_BAD_SCHEME</i> The URL scheme (protocol) contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_USER</i> The user part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PASSWORD</i> The password part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_HOST</i> The host part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PORT</i> The port part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PATH</i> The path part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_DN</i> -9 The DN part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_ATTRIBUTES</i> -10 The attributes part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_SCOPE</i> -11 The scope part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_FILTER</i> -12 The filter part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_OUT_OF_MEMORY</i> -13 The library was unable to allocate memory to create the the <code>globus_url_t</code> contents.<br />
 <i>GLOBUS_URL_ERROR_INTERNAL_ERROR</i> -14 Some unexpected error occurred parsing the URL.</dl>
<h3>int globus_url_parse_loose (const char *url_string, <code>globus_url_t</code> *url)</h3>
<p> Parse a string containing a URL into a <code>globus_url_t</code> Looser restrictions on characters allowed in the path part of the URL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url_string</i> String to parse<br />
 <i>url</i> Pointer to <code>globus_url_t</code> to be filled with the fields of the url</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The string was successfully parsed.<br />
 <i>GLOBUS_URL_ERROR_NULL_STRING</i> The url_string was GLOBUS_NULL.<br />
 <i>GLOBUS_URL_ERROR_NULL_URL</i> The URL pointer was GLOBUS_NULL.<br />
 <i>GLOBUS_URL_ERROR_BAD_SCHEME</i> The URL scheme (protocol) contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_USER</i> The user part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PASSWORD</i> The password part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_HOST</i> The host part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PORT</i> The port part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PATH</i> The path part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_DN</i> -9 The DN part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_ATTRIBUTES</i> -10 The attributes part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_SCOPE</i> -11 The scope part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_FILTER</i> -12 The filter part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_OUT_OF_MEMORY</i> -13 The library was unable to allocate memory to create the the <code>globus_url_t</code> contents.<br />
 <i>GLOBUS_URL_ERROR_INTERNAL_ERROR</i> -14 Some unexpected error occurred parsing the URL.</dl>
<h3>int globus_url_parse_rfc1738 (const char *url_string, <code>globus_url_t</code> *url)</h3>
<p> Parse a string containing a URL into a <code>globus_url_t</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url_string</i> String to parse<br />
 <i>url</i> Pointer to <code>globus_url_t</code> to be filled with the fields of the url</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The string was successfully parsed.<br />
 <i>GLOBUS_URL_ERROR_NULL_STRING</i> The url_string was GLOBUS_NULL.<br />
 <i>GLOBUS_URL_ERROR_NULL_URL</i> The URL pointer was GLOBUS_NULL.<br />
 <i>GLOBUS_URL_ERROR_BAD_SCHEME</i> The URL scheme (protocol) contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_USER</i> The user part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PASSWORD</i> The password part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_HOST</i> The host part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PORT</i> The port part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_PATH</i> The path part of the URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_DN</i> -9 The DN part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_ATTRIBUTES</i> -10 The attributes part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_SCOPE</i> -11 The scope part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_BAD_FILTER</i> -12 The filter part of an LDAP URL contained invalid characters.<br />
 <i>GLOBUS_URL_ERROR_OUT_OF_MEMORY</i> -13 The library was unable to allocate memory to create the the <code>globus_url_t</code> contents.<br />
 <i>GLOBUS_URL_ERROR_INTERNAL_ERROR</i> -14 Some unexpected error occurred parsing the URL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Function Documentation</a></p>
<dd>
<dt><a href="#lbAP">Author</a></p>
<dd></dl>
