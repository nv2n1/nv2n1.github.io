---
title: "page_name(3)"
name: "page_name"
section: "3"
letter: "p"
url: "/docs/linux/man/3-page_name/"
---

<p>page_name &#8211; PKIX/X.509 Names There are several names in PKIX/X.509, GeneralName and Name. A Name consists of an ordered list of Relative Distinguished Names (RDN). Each RDN consists of an unordered list of typed strings. The types are defined by OID and have long and short description. For example id-at-commonName (2.5.4.3) have the long name CommonName and short name CN. The string itself can be of several encoding, UTF8, UTF16, Teltex string, etc. The type limit what encoding should be used. GeneralName is a broader nametype that can contains al kind of stuff like Name, IP addresses, partial Name, etc. Name is mapped into a hx509_name object. Parse and string name into a hx509_name object with <code>hx509_parse_name()</code>, make it back into string representation with <code>hx509_name_to_string()</code>. Name string are defined rfc2253, rfc1779 and X.501. See the library functions here: <code>hx509 name functions</code> </p>
