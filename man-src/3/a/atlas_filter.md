---
title: "atlas_filter(3)"
name: "atlas_filter"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_filter/"
description: "Atlas::Filter – Atlas stream filter."
---

<p>Atlas::Filter &#8211; <code>Atlas</code> stream filter. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Filter.h">Filter.h</a>&gt; </p>
<p> Inherited by Atlas::Filters::Bzip2, and Atlas::Filters::Gzip. </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>CHECKSUM</code>, <code>COMPRESSION</code>, <code>ENCRYPTION</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Filter</code> (<code>Filter</code> *=0) </p>
<p> virtual void <code>begin</code> ()=0 </p>
<p> virtual void <code>end</code> ()=0 </p>
<p> virtual std::string <code>encode</code> (const std::string &amp;)=0 </p>
<p> virtual std::string <code>decode</code> (const std::string &amp;)=0 </p>
<h3>Protected Attributes</h3>
<p><code>Filter</code> * <code>m_next</code> </p>
<h2>Detailed Description</h2>
<p><code>Atlas</code> stream filter. </p>
<p> Filters are used by <code>Codec</code> to transform the byte stream before transmission. The transform must be invertible; that is to say, encoding a string and then decoding it must result in the original string. Filters can be used for compression, encryption or performing checksums and other forms of transmission error detection. A compound filter can be created that acts like a single filter, allowing various filters to be chained together in useful ways such as compressing and then encrypting. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Codec</code> </p>
<p> <code>Negotiate</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
