---
title: "string_driver_pgm(3)"
name: "string_driver_pgm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-string_driver_pgm/"
description: "Driver Programming: String options –"
---

<p>Driver Programming: String options &#8211; </p>
<p> The set of interface functions that the driver author must implement to create a driver and the functions to assist in the creation.</p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_string_cntl_bouncer</code> (<code>globus_xio_driver_attr_cntl_t</code> cntl_func, void *attr, int cmd,&#8230;) </p>
<p> globus_result_t <code>globus_xio_string_cntl_bool</code> (void *attr, const char *key, const char *val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func) </p>
<p> globus_result_t <code>globus_xio_string_cntl_float</code> (void *attr, const char *key, const char *val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func) </p>
<p> globus_result_t <code>globus_xio_string_cntl_int</code> (void *attr, const char *key, const char *val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func) </p>
<p> globus_result_t <code>globus_xio_string_cntl_string</code> (void *attr, const char *key, const char *val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func) </p>
<p> globus_result_t <code>globus_xio_string_cntl_int_int</code> (void *attr, const char *key, const char *val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func)</p>
<h2>Detailed Description</h2>
<p>The set of interface functions that the driver author must implement to create a driver and the functions to assist in the creation. </p>
<p> Driver attribute functions </p>
<p> If the driver wishes to provide driver specific attributes to the user it must implement the following functions: </p>
<p> globus_xio_driver_attr_init_t globus_xio_driver_attr_copy_t globus_xio_driver_attr_cntl_t globus_xio_driver_attr_destroy_t </p>
<p> A driver can choose to expose parameters as in a string form. Providing this feature makes dynamicly setting driver specific options much easier. a user can then load the driverby name and set specific options by name all at runtime with no object module references. For example, a TCP driver can be loaded with the string: tcp, and the options can be set with: </p>
<p> port=50668keepalive=yesnodelay=N </p>
<p> this would set the port to 50668, keepalive to true and nodelay to false. The particular string definition is defined by the tcp driver by properly creating a globus_i_xio_attr_parse_table_t array. Each element of the array is 1 options. There are 3 members of each array entry: key, cmd, and parse function. The key is a string that defines what option is to be set. In the above example string &#8216;port&#8217; would be 1 key. cmd tells the driver what cntl is associated with the key. In otherwords, once the string is parsed out what driver specific control must be called to set the requested option. For more information on controls see <code>globus_xio_attr_cntl</code>. The final value in the array entry is the parsing function. The pasing function takes the value of the &lt;key&gt;= </p>
<p> portion of the string and parses it into data types. once parsed globus_xio_attr_cntl is called and thus the option is set. There are many available parsing functions but the developer is free to right their own if the provided ones are not sufficient. Sample parsing functions follow: </p>
<dl>
<dt>*</p>
<dd><code>globus_xio_string_cntl_bool</code></p>
<dt>*</p>
<dd><code>globus_xio_string_cntl_float</code></p>
<dt>*</p>
<dd><code>globus_xio_string_cntl_int</code></p>
<dt>*</p>
<dd><code>globus_xio_string_cntl_string</code></p>
<dt>*</p>
<dd><code>globus_xio_string_cntl_int_int</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_string_cntl_bouncer (<code>globus_xio_driver_attr_cntl_t</code> cntl_func, void * attr, int cmd, &#8230;)</h3>
<p>New type functions call this one.</p>
<h3>globus_result_t globus_xio_string_cntl_bool (void * attr, const char * key, const char * val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func)</h3>
<p>String option parsing function. </p>
<p> References globus_xio_string_cntl_bool(), and globus_xio_string_cntl_bouncer().</p>
<h3>globus_result_t globus_xio_string_cntl_float (void * attr, const char * key, const char * val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func)</h3>
<p>String option parsing function. </p>
<p> References globus_xio_string_cntl_bouncer(), and globus_xio_string_cntl_float().</p>
<h3>globus_result_t globus_xio_string_cntl_int (void * attr, const char * key, const char * val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func)</h3>
<p>String option parsing function. </p>
<p> References globus_xio_string_cntl_bouncer(), and globus_xio_string_cntl_int().</p>
<h3>globus_result_t globus_xio_string_cntl_string (void * attr, const char * key, const char * val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func)</h3>
<p>String option parsing function. </p>
<p> References globus_xio_string_cntl_bouncer(), and globus_xio_string_cntl_string().</p>
<h3>globus_result_t globus_xio_string_cntl_int_int (void * attr, const char * key, const char * val, int cmd, <code>globus_xio_driver_attr_cntl_t</code> cntl_func)</h3>
<p>String option parsing function. </p>
<p> References globus_xio_string_cntl_bouncer(), and globus_xio_string_cntl_int_int().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus xio from the source code.</p>
