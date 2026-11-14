---
title: "umad_class_str(3)"
name: "umad_class_str"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_class_str/"
description: "umad_*_str – class of functions to return string representations of enums"
---

<p>umad_*_str &#8211; class of functions to return string representations of enums </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad_str.h&gt;

const char * umad_class_str(uint8_t mgmt_class)
const char * umad_method_str(uint8_t mgmt_class, uint8_t method)
const char * umad_attribute_str(uint8_t mgmt_class, be16_t attr_id)

const char * umad_common_mad_status_str(be16_t status)
const char * umad_sa_mad_status_str(be16_t status)</code></pre>
<h2>Description</h2>
<p><code>const char * umad_class_str(uint8_t mgmt_class)</code> Return string value of management class enum <code>const char * umad_method_str(uint8_t mgmt_class, uint8_t method)</code> Return string value of the method for the mgmt_class specified <code>const char * umad_attribute_str(uint8_t mgmt_class, be16_t attr_id)</code> Return string value of attribute specified in attr_id based on mgmt_class specified. <code>const char * umad_common_mad_status_str(be16_t status)</code> Return string value for common MAD status values <code>const char * umad_sa_mad_status_str(be16_t status)</code> Return string value for SA MAD status values <code>NOTE:</code> Not all classes are supported. </p>
<h2>Return Value</h2>
<p>Returns a string representations of the fields specified. </p>
<h2>Author</h2>
<dl>
<dt>Ira Weiny &lt;weiny2 [at] llnl.gov&gt;</p>
<dd></dl>
