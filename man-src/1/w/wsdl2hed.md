---
title: "wsdl2hed(1)"
name: "wsdl2hed"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsdl2hed/"
description: "wsdl2hed – ARC skeleton generator"
---

<h2 class="name">NAME</h2>
<p> wsdl2hed &#8211; ARC skeleton generator</p>
<h2>DESCRIPTION</h2>
<p> The <code>wsdl2hed</code> command creates the C++ skeleton from a WSDL file. </p>
<h2>SYNOPSIS</h2>
<p> <code>wsdl2hed [-s] WSDL_file service_name</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&nbsp;<wbr>-s </code></p>
<dd> If specified then schema inside WSDL is parsed and corresponding wrapper C++ classes are generated for every declared type. Otherwise C++ skeleton for HED service is generated.</p>
<dt><code>&nbsp;<wbr>WSDL_file </code></p>
<dd> The WSDL file describe a webservice interface by standard way.</p>
<dt><code>&nbsp;<wbr>service_name</code></p>
<dd> ARC1 service name (C++ class and header name come from this)</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>Index</h2>
