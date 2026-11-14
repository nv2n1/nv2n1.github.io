---
title: "globus_gram_job_manager_script_interface(3)"
name: "globus_gram_job_manager_script_interface"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_job_manager_script_interface/"
description: "globus_gram_job_manager_script_interface – Job Manager Scheduler Interface The GRAM Job Manager interfaces with the job filesystems and scheduler through scheduler-specific Perl modules."
---

<h2 class="name">NAME</h2>
<p> globus_gram_job_manager_script_interface &#8211; Job Manager Scheduler Interface The GRAM Job Manager interfaces with the job filesystems and scheduler through scheduler-specific Perl modules. </p>
<p> GRAM provides several Perl modules which can be used to implement scheduler-specific interfaces to the GRAM Job Manager. These are:</p>
<dl>
<dt><code>Globus::GRAM::Error </code></p>
<dd> This module implements the GRAM error results as objects. Methods in this module will construct a GRAM error with the value matching the values in the GRAM Protocol library. A scheduler-specific JobManager module may return one of these objects from its methods to indicate errors to the Job Manager program.</p>
<dt><code>Globus::GRAM::JobState </code></p>
<dd> This module defines the GRAM job state constants. A scheduler-specific JobManager module returns one of these values from its methods to indicate the managed job&#8217;s current state.</p>
<dt><code>Globus::GRAM::JobSignal </code></p>
<dd> This module defines the GRAM job signal constant values. The Job Manager uses these values to communicate which signal is being invoked in the manager&#8217;s signal method.</p>
<dt><code>Globus::GRAM::JobManager </code></p>
<dd> This module defines the actual implementatoin of the Job Manager scheduler interface. One writing a scheduler-specific GRAM interface will create a subclass of this object which overrides the default implementation&#8217;s methods.</p>
<dt><code>Globus::GRAM::JobDescription </code></p>
<dd> This module mimics the RSL job description using perl syntax. The job manager passes an object of this type to the JobManager modules&#8217;s constructor. The job manager stores RSL and some configuration values in that JobDescription object. The manager accesses values stored in the JobDescription by invoking methods containing the RSL attribute&#8217;s name (example: $description-&gt;gram_my_job()). Method names are handled as if they were based on the canonical RSL representation of the attribute name. For example, the <code>gram_my_job</code> may be equivalently referred to as <code>GramMyJob</code>, <code>grammyjob</code>, or <code>GRAM_My_Job</code>.</dl>
<hr>
<h2>Index</h2>
