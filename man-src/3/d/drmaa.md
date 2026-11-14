---
title: "drmaa(3)"
name: "drmaa"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa/"
description: "DRMAA interface. –"
---

<h2 class="name">NAME</h2>
<p> DRMAA interface. &#8211; </p>
<h3>Modules</h3>
<p> <code>Vector iteration functions.</code><br />
 <i>The drmaa_get_next_X</i>() functions SHALL store up to <i>value_len</i> bytes of the next attribute name / attribute value / job identifier from the <i>values</i> opaque string vector in the <i>value</i> buffer.<br />
 <code>Job template operations.</code><br />
 <i>The function drmaa_allocate_job_template() SHALL allocate a new job template, returned in jt</i>.</p>
<h3>Functions</h3>
<p> int <code>drmaa_init</code> (const char *contact, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_init()</code> function SHALL initialize DRMAA library and create a new DRMAA session, using the contact parameter, if provided, to determine to which DRMS to connect.<br />
 int <code>drmaa_exit</code> (char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_exit()</code> function SHALL disengage from DRMAA library and allow the DRMAA library to perform any necessary internal cleanup.<br />
 int <code>drmaa_get_attribute</code> (<code>drmaa_job_template_t</code> *jt, const char *name, char *value, size_t value_len, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_attribute()</code> SHALL fill the <i>value</i> buffer with up to <i>value_len</i> characters of the scalar attribute, <i>name&#8217;s</i>, value in the given job template.<br />
 int <code>drmaa_set_vector_attribute</code> (<code>drmaa_job_template_t</code> *jt, const char *name, const char *value[], char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_set_vector_attribute()</code> SHALL set the vector attribute, <i>name</i>, in the job template, <i>jt</i>, to the value(s), <i>value</i>.<br />
 int <code>drmaa_get_vector_attribute</code> (<code>drmaa_job_template_t</code> *jt, const char *name, <code>drmaa_attr_values_t</code> **values, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_vector_attribute()</code> SHALL store in <i>values</i> an opaque values string vector containing the values of the vector attribute, <i>name&#8217;s</i>, value in the given job template.<br />
 int <code>drmaa_get_attribute_names</code> (<code>drmaa_attr_names_t</code> **values, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_attribute_names()</code> SHALL return the set of supported scalar attribute names in an opaque names string vector stored in <i>values</i>.<br />
 int <code>drmaa_get_vector_attribute_names</code> (<code>drmaa_attr_names_t</code> **values, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_vector_attribute_names()</code> SHALL return the set of supported vector attribute names in an opaque names string vector stored in <i>values</i>.</p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int drmaa_init (const char *contact, char *error_diagnosis, size_terror_diag_len)</h3>
<p> The <code>drmaa_init()</code> function SHALL initialize DRMAA library and create a new DRMAA session, using the contact parameter, if provided, to determine to which DRMS to connect. This function MUST be called before any other DRMAA function, except for <code>drmaa_get_DRM_system()</code>, <code>drmaa_get_DRMAA_implementation()</code>, <code>drmaa_get_contact()</code>, and <code>drmaa_strerror()</code>. If <i>contact</i> is NULL, the default DRM system SHALL be used, provided there is only one DRMAA implementation in the provided binary module. When there is more than one DRMAA implementation in the binary module, <code>drmaa_init()</code> SHALL return the DRMAA_ERRNO_NO_DEFAULT_CONTACT_STRING_SELECTED error code. The <code>drmaa_init()</code> function SHOULD be called by only one of the threads. The main thread is RECOMMENDED. A call by another thread SHALL return the DRMAA_ERRNO_ALREADY_ACTIVE_SESSION error code.</p>
<h3>int drmaa_exit (char *error_diagnosis, size_terror_diag_len)</h3>
<p> The <code>drmaa_exit()</code> function SHALL disengage from DRMAA library and allow the DRMAA library to perform any necessary internal cleanup. This routine SHALL end the current DRMAA session but SHALL NOT affect any jobs (e.g, queued and running jobs SHALL remain queued and running). <code>drmaa_exit()</code> SHOULD be called by only one of the threads. The first call to call <code>drmaa_exit()</code> by a thread will operate normally. All other calls from the same and other threads SHALL fail, returning a DRMAA_ERRNO_NO_ACTIVE_SESSION error code.</p>
<h3>int drmaa_set_vector_attribute (<code>drmaa_job_template_t</code> *jt, const char *name, const char *value[], char *error_diagnosis, size_terror_diag_len)</h3>
<p> The function <code>drmaa_set_vector_attribute()</code> SHALL set the vector attribute, <i>name</i>, in the job template, <i>jt</i>, to the value(s), <i>value</i>. The DRMAA implementation MUST accept value values that are arrays of one or more strings terminated by a NULL entry.</p>
<h3>int drmaa_get_attribute_names (<code>drmaa_attr_names_t</code> **values, char *error_diagnosis, size_terror_diag_len)</h3>
<p> The function <code>drmaa_get_attribute_names()</code> SHALL return the set of supported scalar attribute names in an opaque names string vector stored in <i>values</i>. This vector SHALL include all required scalar attributes, all supported optional scalar attributes, all DRM-specific scalar attributes, and no unsupported optional attributes.</p>
<h3>int drmaa_get_vector_attribute_names (<code>drmaa_attr_names_t</code> **values, char *error_diagnosis, size_terror_diag_len)</h3>
<p> The function <code>drmaa_get_vector_attribute_names()</code> SHALL return the set of supported vector attribute names in an opaque names string vector stored in <i>values</i>. This vector SHALL include all required vector attributes, all supported optional vector attributes, all DRM-specific vector attributes, and no unsupported optional attributes.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for torque from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
