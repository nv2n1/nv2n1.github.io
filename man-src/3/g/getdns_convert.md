---
title: "getdns_convert(3)"
name: "getdns_convert"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_convert/"
description: "getdns_convert, getdns_convert_dns_name_to_fqdn, getdns_convert_fqdn_to_dns_name — convert dname between presentation- and wire-format"
---

<h2>NAME</h2>
<p> <code>getdns_convert, </code> <code>getdns_convert_dns_name_to_fqdn, </code> <code>getdns_convert_fqdn_to_dns_name</code> &#8212; convert dname between presentation- and wire-format </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;getdns.h&gt; </p>
<p> getdns_return_t<br />
 <code>getdns_convert_dns_name_to_fqdn</code> (const getdns_bindata *dns_name_wire_fmt, </p>
<dl>
<dt>
<dd> char **fqdn_as_string)</dl>
<p> getdns_return_t<br />
 <code>getdns_convert_fqdn_to_dns_name</code> (char *fqdn_as_string, </p>
<dl>
<dt>
<dd> const getdns_bindata **dns_name_wire_fmt)</dl>
<h2>DESCRIPTION</h2>
<p> Names in DNS fields are stored in a fashion very different from the normal presentation format normally used in applications. The DNS format is described in the first paragraph in Section 3.1 of RFC 1035; the presentation format here is a null-terminated string with interior dots. These helper functions only work with names in the DNS format that are not compressed. They are useful for converting domain names in the replies_tree to and from the FQDN presentation format. </p>
<p> getdns_convert_dns_name_to_fqdn() converts a domain name in DNS format to the presentation format. For example, the hex sequence 03 77 77 77 07 65 78 61 6d 70 6c 65 03 63 6f 6d 00 would be converted to &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;. getdns_convert_fqdn_to_dns_name() does the reverse: it converts a null-terminated string in FQDN format to bytes in DNS format. </p>
<dl>
<dt> <i>dns_name_wire_fmt</i></p>
<dd>The non-compressed DNS wire format name (per RFC 1035) in a bindata structure that will be converted to/from an fqdn. In getdns_convert_fqdn_to_dns_name storage is allocated using the system allocator (malloc) and must be freed by the caller. </p>
<dt> <i>fqdn_as_string</i></p>
<dd>a null terminated string to be converted to/from non-compressed DNS wire format name (per RFC 1035). In getdns_convert_dns_name_to_fqdn storage is allocated using the system allocator (malloc) and must be freed by the caller. </p>
<dt></dl>
<h2>RETURN VALUES</h2>
<dd>Upon successful completion the function returns <code>GETDNS_RETURN_GOOD</code> </p>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3) </p>
<h2>Index</h2>
