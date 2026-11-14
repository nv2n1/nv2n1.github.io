---
title: "globus_net_manager_attr_init(3)"
name: "globus_net_manager_attr_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_attr_init/"
description: "Attributes –"
---

<h2 class="name">NAME</h2>
<p> Attributes &#8211; </p>
<p> Net Manager Attribute Management Functions.</p>
<h3>Data Structures</h3>
<p> struct <code>globus_net_manager_attr_s</code><br />
 <i>Net Manager Attributes. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_NET_MANAGER_NULL_ATTR</code><br />
 <i>End of attribute array static initializer. </i></p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 <code>globus_net_manager_attr_s</code> <code>globus_net_manager_attr_t</code>&quot;<br />
 <i>Net Manager Attributes. </i></p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_net_manager_attr_array_copy</code> (<code>globus_net_manager_attr_t</code> **dest_array, const <code>globus_net_manager_attr_t</code> *src_array)<br />
 <i>Copy an array of Network Manager attributes. </i><br />
 void <code>globus_net_manager_attr_array_delete</code> (<code>globus_net_manager_attr_t</code> *attrs)<br />
 <i>Destroy an array of Network Manager attributes. </i><br />
 globus_result_t <code>globus_net_manager_attr_array_from_string</code> (<code>globus_net_manager_attr_t</code> **attr, const char *scope, const char *attr_string)<br />
 <i>Parse an array of Network Manager attributes from a string. </i><br />
 void <code>globus_net_manager_attr_destroy</code> (<code>globus_net_manager_attr_t</code> *attr)<br />
 <i>Destroy the contents of an attribute. </i><br />
 globus_result_t <code>globus_net_manager_attr_init</code> (<code>globus_net_manager_attr_t</code> *attr, const char *scope, const char *name, const char *value)<br />
 <i>Initialize the contents of an attribute. </i></p>
<h3>Variables</h3>
<p> const <code>globus_net_manager_attr_t</code> <code>globus_net_manager_null_attr</code> = <code>GLOBUS_NET_MANAGER_NULL_ATTR</code><br />
 <i>End of array value. </i></p>
<h2>Detailed Description</h2>
<p> Net Manager Attribute Management Functions. </p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>globus_net_manager_attr_s</code></h3>
<p>&nbsp;<wbr><code>globus_net_manager_attr_t</code>&quot; </p>
<p> Net Manager Attributes. The globus_net_manager_attr_t structure defines a scoped (attribute, value) tuple. The scope in most cases is either the name of the transport driver or the &#8216;globus_net_manager&#8217; scope, for attributes specific to the network manager implementation.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_net_manager_attr_array_copy (<code>globus_net_manager_attr_t</code> **dest_array, const <code>globus_net_manager_attr_t</code> *src_array)</h3>
<p> Copy an array of Network Manager attributes. This function performs a deep copy of array of net_manager attributes. The new array will be stored in the pointer passed to by the dest_array parameter. It will contain all entries in the array passed as the src_array, ending with the value <code>GLOBUS_NET_MANAGER_NULL_ATTR</code>. </p>
<p> The caller must free the array stored in *dest_array by calling globus_net_manager_attr_array_destroy(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>dest_array</i> A pointer to an array of attributes to be allocated and initialized.<br />
 <i>src_array</i> An array of attributes to copy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On error, the dest_array is set to NULL and this function returns an error object. Otherwise, this function returns GLOBUS_SUCCESS.</dl>
<h3>void globus_net_manager_attr_array_delete (<code>globus_net_manager_attr_t</code> *attrs)</h3>
<p> Destroy an array of Network Manager attributes. This function deletes an array of Network Manager attributes and all values contained within them. The array must be terminated by the value <code>GLOBUS_NET_MANAGER_NULL_ATTR</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attrs</i> A pointer to an array of attributes to be freed.</dl>
<h3>globus_result_t globus_net_manager_attr_array_from_string (<code>globus_net_manager_attr_t</code> **attr, const char *scope, const char *attr_string)</h3>
<p> Parse an array of Network Manager attributes from a string. This function parses a string containing a list of attributes and creates a new array of Network Manager attribute values from it. The array is terminated by globus_net_manager_null_attr. </p>
<p> Attribute strings are formed by the regular expression </p>
<pre>
    NAME=VALUE(;NAME=VALUE)*
</pre>
<p>&nbsp;<wbr>The NAME and VALUE strings may contain any character except&nbsp;<wbr>;&nbsp;<wbr>=, and the carriage return and newline characters. </p>
<p> The caller must free the array stored in *attr by calling globus_net_manager_attr_array_destroy(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A pointer to an array of attributes to be allocated and initialized.<br />
 <i>scope</i> The string to be added as the scope value of the attributes.<br />
 <i>attr_string</i> The string to be parsed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, this function returns GLOBUS_SUCCESS. Otherwise, an error result is returned to the caller.</dl>
<h3>void globus_net_manager_attr_destroy (<code>globus_net_manager_attr_t</code> *attr)</h3>
<p> Destroy the contents of an attribute. This function frees the values contained in <code>attr</code> and reinitializes them to NULL. It <i>does not</i> free attr itself. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Pointer to the attribute to destroy.</dl>
<h3>globus_result_t globus_net_manager_attr_init (<code>globus_net_manager_attr_t</code> *attr, const char *scope, const char *name, const char *value)</h3>
<p> Initialize the contents of an attribute. This function initializes <code>attr</code> and with copies of the values passed as the <code>scope</code>, <code>name</code>, and <code>value</code> parameters. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Pointer to the attribute to initialize.<br />
 <i>scope</i> Attribute scope<br />
 <i>name</i> Attribute name<br />
 <i>value</i> Attribute value</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On error, &#8216;attr&#8217; is set to NULL and this function returns an error object. Otherwise this function returns &#8216;GLOBUS_SUCCESS&#8217;</dl>
<h2>Variable Documentation</h2>
<h3>const <code>globus_net_manager_attr_t</code> globus_net_manager_null_attr = <code>GLOBUS_NET_MANAGER_NULL_ATTR</code></h3>
<p> End of array value. This value may be assigned to an element in an array of Network Manager attributes to terminate the array.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_net_manager from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Function Documentation</a></p>
<dd>
<dt><a href="#lbAQ">Variable Documentation</a></p>
<dd>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
