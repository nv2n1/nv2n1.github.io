---
title: "globus_url_t(3)"
name: "globus_url_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_url_t/"
description: "globus_url_t –"
---

<h2 class="name">NAME</h2>
<p> globus_url_t &#8211; </p>
<p> Parsed URLs. </p>
<p> This structure contains the fields which were parsed from an string representation of an URL. There are no methods to access fields of this structure.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_url.h&gt;</p>
<h3>Data Fields</h3>
<p> char * <code>scheme</code> </p>
<p> <code>globus_url_scheme_t</code> <code>scheme_type</code> </p>
<p> char * <code>user</code> </p>
<p> char * <code>password</code> </p>
<p> char * <code>host</code> </p>
<p> unsigned short <code>port</code> </p>
<p> char * <code>url_path</code> </p>
<p> char * <code>dn</code> </p>
<p> char * <code>attributes</code> </p>
<p> char * <code>scope</code> </p>
<p> char * <code>filter</code> </p>
<p> char * <code>url_specific_part</code> </p>
<h2>Detailed Description</h2>
<p> Parsed URLs. </p>
<p> This structure contains the fields which were parsed from an string representation of an URL. There are no methods to access fields of this structure.</p>
<h2>Field Documentation</h2>
<h3>char* globus_url_t::attributes</h3>
<pre>
        The list of attributes which should be returned
</pre>
<p>&nbsp;<wbr>from an LDAP search.&nbsp;<wbr>[ldap]&nbsp;<wbr></p>
<h3>char* globus_url_t::dn</h3>
<pre>
    The distinguished name for the base of an LDAP
</pre>
<p>&nbsp;<wbr>search.&nbsp;<wbr>[ldap]&nbsp;<wbr></p>
<h3>char* globus_url_t::filter</h3>
<pre>
    The filter to be applied to an LDAP search
</pre>
<p>&nbsp;<wbr>[ldap]&nbsp;<wbr></p>
<h3>char* globus_url_t::host</h3>
<pre>
    The host name or IP address of the URL.
</pre>
<p>&nbsp;<wbr>[ftp, gsiftp, http, https, ldap, x-nexus&nbsp;<wbr></p>
<h3>char* globus_url_t::password</h3>
<p> The user&#8217;s password from the URL. [ftp, gsiftp]</p>
<h3>unsigned short globus_url_t::port</h3>
<pre>
        The TCP port number of the service providing the
</pre>
<p>&nbsp;<wbr>URL&nbsp;<wbr>[ftp, gsiftp, http, https, ldap, x-nexus]&nbsp;<wbr></p>
<h3>char* globus_url_t::scheme</h3>
<p> A string containing the URL&#8217;s scheme (http, ftp, etc)</p>
<h3><code>globus_url_scheme_t</code> globus_url_t::scheme_type</h3>
<p> An enumerated scheme type. This is derived from the scheme string</p>
<h3>char* globus_url_t::scope</h3>
<p> The scope of an LDAP search. [ldap]</p>
<h3>char* globus_url_t::url_path</h3>
<pre>
    The path name of the resource on the service
</pre>
<p>&nbsp;<wbr>providing the URL.&nbsp;<wbr>[ftp, gsiftp, http, https]&nbsp;<wbr></p>
<h3>char* globus_url_t::url_specific_part</h3>
<p> An unparsed string containing the remaining text after the optional host and port of an unknown URL, or the contents of a x-gass-cache URL [x-gass-cache, unknown]</p>
<h3>char* globus_url_t::user</h3>
<p> The username portion of the URL. [ftp, gsiftp] </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
