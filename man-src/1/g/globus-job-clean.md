---

title: "globus-job-clean(1)"
name: "globus-job-clean"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-job-clean/"
description: "globus-job-clean – Cancel and clean up a GRAM batch job"
---

<p> globus-job-clean &#8211; Cancel and clean up a GRAM batch job </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-job-clean</code> [OPTIONS] <i>JOBID</i> </p>
<p> <code>globus-job-clean</code> [ -help | -usage | -version | -versions ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>globus-job-clean</code> program cancels the job named by <i>JOBID</i> if it is still running, and then removes any cached files on the GRAM service node related to that job. In order to do the file clean up, it submits a job which removes the cache files. By default this cleanup job is submitted to the default GRAM resource running on the same host as the job. This behavior can be controlled by specifying a resource manager contact string as the parameter to the <i>-r</i> or <i>-resource</i> option. </p>
<p> By default, <code>globus-job-clean</code> prompts the user prior to canceling the job. This behavior can be overridden by specifying the <i>-f</i> or <i>-force</i> command-line options.</p>
<h2>OPTIONS</h2>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
</dt><dd> Display a help message to standard error and exit.</dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
</dt><dd> Display the software version of the <code>globus-job-clean</code> program to standard output.</dd></dl>
<p> <code>-versions</code></p>
<dl>
<dt>
</dt><dd> Display the software version of the <code>globus-job-clean</code> program including DiRT information to standard output.</dd></dl>
<p> <code>-resource </code><i>RESOURCE</i><code>, -resource </code><i>RESOURCE</i></p>
<dl>
<dt>
</dt><dd> Submit the clean-up job to the resource named by <i>RESOURCE</i> instead of the default GRAM service on the same host as the job contact.</dd></dl>
<p> <code>-force, -f</code></p>
<dl>
<dt>
</dt><dd> Do not prompt to confirm job cancel and clean-up.</dd></dl>
<p> <code>-quiet, -q</code></p>
<dl>
<dt>
</dt><dd> Do not print diagnostics for successful clean-up. Implies <i>-f</i>.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> The following variables affect the execution of <code>globus-job-clean</code>. </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
</dt><dd> Path to proxy credential.</dd></dl>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
</dt><dd> Path to trusted certificate directory.</dd></dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
