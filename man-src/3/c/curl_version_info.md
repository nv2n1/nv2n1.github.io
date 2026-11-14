---
title: "curl_version_info(3)"
name: "curl_version_info"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_version_info/"
description: "curl_version_info – returns run-time libcurl version info"
---

<h2>NAME</h2>
<p> curl_version_info &#8211; returns run-time libcurl version info</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>curl_version_info_data *curl_version_info( CURLversion type</code><i>);</i></p>
<h2>DESCRIPTION</h2>
<p> Returns a pointer to a filled in struct with information about various run-time features in libcurl. <i>type</i> should be set to the version of this functionality by the time you write your program. This way, libcurl will always return a proper struct that your program understands, while programs in the future might get a different struct. CURLVERSION_NOW will be the most recent one for the library you have installed: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>data&nbsp;<wbr>=&nbsp;<wbr>curl_version_info(CURLVERSION_NOW); </p>
<p> Applications should use this information to judge if things are possible to do or not, instead of using compile-time checks, as dynamic/DLL libraries can be changed independent of applications. </p>
<p> The curl_version_info_data struct looks like this </p>
<pre><code>
typedef struct {
    CURLversion age; /* see description below */
    /* when 'age' is 0 or higher, the members below also exist: */
    const char *version;      /* human readable string */
    unsigned int version_num; /* numeric representation */
    const char *host;         /* human readable string */
    int features;             /* bitmask, see below */
    char *ssl_version;        /* human readable string */
    long ssl_version_num;     /* not used, always zero */
    const char *libz_version; /* human readable string */
    const char **protocols;   /* list of protocols */
    /* when 'age' is 1 or higher, the members below also exist: */
    const char *ares; /* human readable string */
    int ares_num;     /* number */
    /* when 'age' is 2 or higher, the member below also exists: */
    const char *libidn; /* human readable string */
    /* when 'age' is 3 or higher, the members below also exist: */
    int iconv_ver_num;          /* '_libiconv_version' if iconv support enabled */
    const char *libssh_version; /* human readable string */
} curl_version_info_data;
</code></pre>
<p> <i>age</i> describes what the age of this struct is. The number depends on how new the libcurl you&#8217;re using is. You are however guaranteed to get a struct that you have a matching struct for in the header, as you tell libcurl your &quot;age&quot; with the input argument. </p>
<p> <i>version</i> is just an ascii string for the libcurl version. </p>
<p> <i>version_num</i> is a 24 bit number created like this: &lt;8 bits major number&gt; | &lt;8 bits minor number&gt; | &lt;8 bits patch number&gt;. Version 7.9.8 is therefore returned as 0x070908. </p>
<p> <i>host</i> is an ascii string showing what host information that this libcurl was built for. As discovered by a configure script or set by the build environment. </p>
<p> <i>features</i> can have none, one or more bits set, and the currently defined bits are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CURL_VERSION_IPV6</p>
<dd> supports IPv6</p>
<dt>CURL_VERSION_KERBEROS4</p>
<dd> supports kerberos4 (when using FTP)</p>
<dt>CURL_VERSION_SSL</p>
<dd> supports SSL (HTTPS/FTPS) (Added in 7.10)</p>
<dt>CURL_VERSION_LIBZ</p>
<dd> supports HTTP deflate using libz (Added in 7.10)</p>
<dt>CURL_VERSION_NTLM</p>
<dd> supports HTTP NTLM (added in 7.10.6)</p>
<dt>CURL_VERSION_GSSNEGOTIATE</p>
<dd> supports HTTP GSS-Negotiate (added in 7.10.6)</p>
<dt>CURL_VERSION_DEBUG</p>
<dd> libcurl was built with debug capabilities (added in 7.10.6)</p>
<dt>CURL_VERSION_CURLDEBUG</p>
<dd> libcurl was built with memory tracking debug capabilities. This is mainly of interest for libcurl hackers. (added in 7.19.6)</p>
<dt>CURL_VERSION_ASYNCHDNS</p>
<dd> libcurl was built with support for asynchronous name lookups, which allows more exact timeouts (even on Windows) and less blocking when using the multi interface. (added in 7.10.7)</p>
<dt>CURL_VERSION_SPNEGO</p>
<dd> libcurl was built with support for SPNEGO authentication (Simple and Protected GSS-API Negotiation Mechanism, defined in RFC 2478.) (added in 7.10.8)</p>
<dt>CURL_VERSION_LARGEFILE</p>
<dd> libcurl was built with support for large files. (Added in 7.11.1)</p>
<dt>CURL_VERSION_IDN</p>
<dd> libcurl was built with support for IDNA, domain names with international letters. (Added in 7.12.0)</p>
<dt>CURL_VERSION_SSPI</p>
<dd> libcurl was built with support for SSPI. This is only available on Windows and makes libcurl use Windows-provided functions for NTLM authentication. It also allows libcurl to use the current user and the current user&#8217;s password without the app having to pass them on. (Added in 7.13.2)</p>
<dt>CURL_VERSION_CONV</p>
<dd> libcurl was built with support for character conversions, as provided by the CURLOPT_CONV_* callbacks. (Added in 7.15.4)</p>
<dt>CURL_VERSION_TLSAUTH_SRP</p>
<dd> libcurl was built with support for TLS-SRP. (Added in 7.21.4)</p>
<dt>CURL_VERSION_NTLM_WB</p>
<dd> libcurl was built with support for NTLM delegation to a winbind helper. (Added in 7.22.0)</p>
<dt>CURL_VERSION_UNIX_SOCKETS</p>
<dd> libcurl was built with support for UNIX domain sockets.</dl>
</dl>
<p> <i>ssl_version</i> is an ASCII string for the OpenSSL version used. If libcurl has no SSL support, this is NULL. </p>
<p> <i>ssl_version_num</i> is the numerical OpenSSL version value as defined by the OpenSSL project. If libcurl has no SSL support, this is 0. </p>
<p> <i>libz_version</i> is an ASCII string (there is no numerical version). If libcurl has no libz support, this is NULL. </p>
<p> <i>protocols</i> is a pointer to an array of char * pointers, containing the names protocols that libcurl supports (using lowercase letters). The protocol names are the same as would be used in URLs. The array is terminated by a NULL entry.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a curl_version_info_data struct.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-curl_version/">curl_version</a>(3)</i> </p>
<h2>Index</h2>
