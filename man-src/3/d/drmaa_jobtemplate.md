---
title: "drmaa_jobtemplate(3)"
name: "drmaa_jobtemplate"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_jobtemplate/"
description: "drmaa_allocate_job_template, drmaa_delete_job_template, drmaa_set_attribute, drmaa_get_attribute, drmaa_set_vector_attribute, drmaa_get_vector_attribute, drmaa_get_next_attr_value, drmaa_get_num_at..."
---

<h2 class="name">NAME</h2>
<p> drmaa_allocate_job_template, drmaa_delete_job_template, drmaa_set_attribute, drmaa_get_attribute, drmaa_set_vector_attribute, drmaa_get_vector_attribute, drmaa_get_next_attr_value, drmaa_get_num_attr_values, drmaa_release_attr_values &#8211; xxQS_NAMExx DRMAA job template handling</p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre>
<code>int drmaa_allocate_job_template(
<dl><dt><dd>drmaa_job_template_t **jt,
char *error_diagnosis,
size_t error_diag_len
</dl>
</code></pre>
<p> <code>); </p>
<p> </code></p>
<pre>
<code>int drmaa_delete_job_template(
<dl><dt><dd>drmaa_job_template_t *jt,
char *error_diagnosis,
size_t error_diag_len
</dl>
</code></pre>
<p> <code>); </p>
<p> </code></p>
<pre><code>
int drmaa_set_attribute(
drmaa_job_template_t *jt,
const char *name,
const char *value,
char *error_diagnosis,
size_t error_diag_len
</code></pre>
<p> <code>); </p>
<p> </code><br />
int drmaa_get_attribute(<br />
drmaa_job_template_t *jt,<br />
const char *name,<br />
char *value,<br />
size_t value_len,<br />
char *error_diagnosis,<br />
size_t error_diag_len<br />
 <code>); </p>
<p> </code><br />
int drmaa_set_vector_attribute(<br />
drmaa_job_template_t *jt,<br />
const char *name,<br />
const char *value[],<br />
char *error_diagnosis,<br />
size_t error_diag_len<br />
 <code>); </p>
<p> </code></p>
<pre><code>
int drmaa_get_vector_attribute(
drmaa_job_template_t *jt,
const char *name,
drmaa_attr_values_t **values,
char *error_diagnosis,
size_t error_diag_len
</code></pre>
<p> <code>); </p>
<p> </code></p>
<pre>
<code>int drmaa_get_next_attr_value(
<dl><dt><dd>drmaa_attr_values_t* values,
char *value,
int value_len
</dl>
</code></pre>
<p> <code>); </p>
<p> </code></p>
<pre>
<code>int drmaa_get_num_attr_values(
<dl><dt><dd>drmaa_attr_values_t* values,
int *size
</dl>
</code></pre>
<p> );<code> </p>
<p> </code></p>
<pre>
<code>void drmaa_release_attr_values(
<dl><dt><dd>drmaa_attr_values_t* values
</dl>
</code></pre>
<p> <code>); </p>
<p> </code></p>
<h2>DESCRIPTION</h2>
<p> The drmaa_allocate_job_template() function allocates a new DRMAA job template into <i>jt</i>. DRMAA job templates describe specifics of jobs that are submitted using and</p>
<h3>drmaa_delete_job_template()</h3>
<p> The drmaa_delete_job_template() function releases all resources associated with the DRMAA job template <i>jt</i>. Jobs that were submitted using the job template are not affected. </p>
<h3>drmaa_set_attribute()</h3>
<p> The drmaa_set_attribute() function stores the <i>value</i> under <i>name</i> for the given DRMAA job template, <i>jt</i>. Only non-vector attributes may be passed. </p>
<h3>drmaa_get_attribute()</h3>
<p> The drmaa_get_attribute() function returns into <i>value</i> up to <i>value_len</i> bytes from the string stored for the non-vector attribute, <i>name</i>, in the DRMAA job template, <i>jt</i>. </p>
<h3>drmaa_set_vector_attribute()</h3>
<p> The drmaa_set_vector_attribute() function stores the strings in <i>value</i> under <i>name</i> in the list of vector attributes for the given DRMAA job template, <i>jt</i>. Only vector attributes may be passed. The <i>value</i> pointer array must be <i>NULL</i> terminated. </p>
<h3>drmaa_get_vector_attribute()</h3>
<p> The drmaa_get_vector_attribute() function returns into <i>values</i> a DRMAA attribute string vector containing all string values stored in the vector attribute, <i>name</i>. The values in the DRMAA values string vector can be extracted using The caller is responsible for releasing the DRMAA values string vector returned into <i>values</i> using </p>
<h3>drmaa_get_next_attr_value()</h3>
<p> Each time drmaa_get_next_attr_value() is called it returns into <i>value</i> up to <i>value_len</i> bytes of the next entry stored in the DRMAA values string vector, <i>values</i>. Once the values list has been exhausted, DRMAA_ERRNO_NO_MORE_ELEMENTS is returned. </p>
<h3>drmaa_get_num_attr_values()</h3>
<p> The drmaa_get_num_attr_values() returns into <i>size</i> the number of entries in the DRMAA values string vector. This function is only available in the 1.0 implementation. </p>
<h3>drmaa_release_attr_values()</h3>
<p> The drmaa_release_attr_values() function releases all resources associated with the DRMAA values string vector, <i>values</i>. </p>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell to be used. To address a xxQS_NAMExx cell xxQS_NAMExx uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</dl>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, drmaa_allocate_job_template(), drmaa_delete_job_template(), drmaa_set_attribute(), drmaa_get_attribute(), drmaa_set_vector_attribute(), drmaa_get_vector_attribute(), and drmaa_get_next_attr_value() return DRMAA_ERRNO_SUCCESS. Other values indicate an error. Up to <i>error_diag_len</i> characters of error related diagnosis information is then provided in the buffer <i>error_diagnosis</i>. </p>
<h2>ERRORS</h2>
<p> The drmaa_allocate_job_template(), drmaa_delete_job_template(), drmaa_set_attribute(), drmaa_get_attribute(), drmaa_set_vector_attribute(), drmaa_get_vector_attribute(), and drmaa_get_next_attr_value() functions will fail if:</p>
<h3>DRMAA_ERRNO_INTERNAL_ERROR</h3>
<p> Unexpected or internal DRMAA error, like system call failure, etc.</p>
<h3>DRMAA_ERRNO_DRM_COMMUNICATION_FAILURE</h3>
<p> Could not contact DRM system for this request.</p>
<h3>DRMAA_ERRNO_AUTH_FAILURE</h3>
<p> The specified request is not processed successfully due to authorization failure.</p>
<h3>DRMAA_ERRNO_INVALID_ARGUMENT</h3>
<p> The input value for an argument is invalid.</p>
<h3>DRMAA_ERRNO_NO_ACTIVE_SESSION</h3>
<p> Failed because there is no active session.</p>
<h3>DRMAA_ERRNO_NO_MEMORY</h3>
<p> Failed allocating memory. </p>
<p> The drmaa_set_attribute() and drmaa_set_vector_attribute() will fail if:</p>
<h3>DRMAA_ERRNO_INVALID_ATTRIBUTE_FORMAT</h3>
<p> The format for the attribute value is invalid.</p>
<h3>DRMAA_ERRNO_INVALID_ATTRIBUTE_VALUE</h3>
<p> The value for the attribute is invalid.</p>
<h3>DRMAA_ERRNO_CONFLICTING_ATTRIBUTE_VALUES</h3>
<p> The value of this attribute is conflicting with a previously set attributes. </p>
<p> The drmaa_get_attribute() and drmaa_get_vector_attribute() will fail if:</p>
<h3>DRMAA_ERRNO_INVALID_ATTRIBUTE_VALUE</h3>
<p> The specified attribute is not set in the DRMAA job template. </p>
<p> The drmaa_get_next_attr_value() will fail if:</p>
<h3>DRMAA_ERRNO_INVALID_ATTRIBUTE_VALUE</h3>
<p> When there are no more entries in the vector. </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
