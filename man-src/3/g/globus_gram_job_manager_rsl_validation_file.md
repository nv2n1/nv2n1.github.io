---
title: "globus_gram_job_manager_rsl_validation_file(3)"
name: "globus_gram_job_manager_rsl_validation_file"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_job_manager_rsl_validation_file/"
description: "globus_gram_job_manager_rsl_validation_file – RSL Validation File Format The idea behind the RSL Validation file is to provide a mechanism for job manager scheduler interfaces to implement RSL exte..."
---

<h2 class="name">NAME</h2>
<p> globus_gram_job_manager_rsl_validation_file &#8211; RSL Validation File Format The idea behind the RSL Validation file is to provide a mechanism for job manager scheduler interfaces to implement RSL extensions, while having the job manager still be able to decide whether a job request contains a valid RSL string. </p>
<p> In addition to indicating what RSL attributes are valid, the RSL validation file contains information about when the RSL attribute may be used, it&#8217;s default value, and the format of the attribute&#8217;s value. </p>
<h2>File Format</h2>
<h3>Comments</h3>
<p> The RSL validation file may contain comments. Comments are indicated in the file by a line beginning with the <i>#</i> character. Comments continue until end-of-line. Comments are discarded by the RSL Validation File parser. </p>
<p> Example: </p>
<pre>
# I am a comment. Ignore me.
</pre>
<h3>ValidationRecords</h3>
<p> The RSL validition file consists of a set of <i>ValidationRecords</i>. Each <i>ValidationRecord</i> consists of a number of <i>ValidationProperties</i> associated with a single RSL attribute. <i>ValidationRecord</i>s are separated by a blank line in the RSL validation file.</p>
<h3>Validation Properties</h3>
<p> A <i>ValidationProperty</i> is defined in the RSL validation file by a <i>PropertyName</i> and a <i>PropertyValue</i>. The syntax of a validation property is simply the <i>PropertyName</i> followed by a colon character, followed by a <i>PropertyValue</i>. </p>
<p> If a <i>PropertyValue</i> begins with a double-quote, then it may span multiple lines. Double-quote characters within a multiline <i>PropertyValue</i> must be escaped by a preceding backslash character. An unquoted <i>PropertyValue</i> ends at the first newline character. </p>
<p> Example: </p>
<pre>
Attribute: directory
Description: 'Specifies the path of the directory the jobmanager will
              use as the default directory for the requested job.'
</pre>
<h3>Defined PropertyNames</h3>
<p> The following <i>PropertyName</i>s are understood by this version of the RSL validation file parser. Any unknown <i>PropertyName</i> will cause the <i>ValidationProprty</i> to be ignored by the parser. </p>
<p> <code>Attribute</code></p>
<dl>
<dt>
<dd> The name of the RSL parameter to which this record refers.</dl>
<p> <code>Description</code></p>
<dl>
<dt>
<dd> A textual description of what the RSL parameter means.</dl>
<p> <code>Default</code></p>
<dl>
<dt>
<dd> The default value of the RSL parameter if it is not found in the RSL. The default value is only used if the DefaultWhen value matches the current validation mode.</dl>
<p> <code>Values</code></p>
<dl>
<dt>
<dd> A string containing whitespace-separated list of enumerated values which are valid for this RSL attribute. For example, for the &#8216;dryrun&#8217; parameter, this may be <code>&#8216;yes no&#8217;</code>.</dl>
<p> <code>RequiredWhen</code></p>
<dl>
<dt>
<dd> Some subset of the &#8216;when strings&#8217; (<code>see below</code>), indicating when the RSL parameter is required for the RSL to be valid.</dl>
<p> <code>DefaultWhen</code></p>
<dl>
<dt>
<dd> Some subset of the &#8216;when strings&#8217; (<code>see below</code>) indicating when then RSL&#8217;s default value will be used if the RSL attribute is not present in the RSL.</dl>
<p> <code>ValidWhen</code></p>
<dl>
<dt>
<dd> Some subset of the &#8216;when strings&#8217; (<code>see below</code>) indicating when then RSL attribute may be used.</dl>
<h3>&#8216;When&#8217; Strings</h3>
<p> The set of when strings understood by the RSL validation file parser are </p>
<p> <code>GLOBUS_GRAM_JOB_SUBMIT</code></p>
<dl>
<dt>
<dd> The RSL attribute pertains to job submission.</dl>
<p> <code>GLOBUS_GRAM_JOB_MANAGER_RESTART</code></p>
<dl>
<dt>
<dd> The RSL attribute pertains to job manager restart.</dl>
<p> <code>GLOBUS_GRAM_JOB_MANAGER_STDIO_UPDATE</code></p>
<dl>
<dt>
<dd> The RSL attribute pertains to the STDIO_UPDATE signal.</dl>
<h2>Index</h2>
