---
title: "proxycertinfo_st(3)"
name: "proxycertinfo_st"
section: "3"
letter: "p"
url: "/docs/linux/man/3-proxycertinfo_st/"
description: "PROXYCERTINFO_st –"
---

<p>PROXYCERTINFO_st &#8211; </p>
<p> This typedef maintains information about a proxy certificate.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p>This typedef maintains information about a proxy certificate. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>NOTE: The API provides functions to manipulate the fields of a PROXYCERTINFO. Accessing the fields directly is not a good idea.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path_length</i> an optional field in the ANS.1 DER encoding, it specifies the maximum depth of the path of Proxy Certificates that can be signed by this End Entity Certificate or Proxy Certificate.<br />
 <i>policy</i> a non-optional field in the ANS.1 DER encoding, specifies policies on the use of this certificate.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus gsi proxy ssl from the source code.</p>
