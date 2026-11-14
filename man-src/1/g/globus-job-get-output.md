---
title: "globus-job-get-output(1)"
name: "globus-job-get-output"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-job-get-output/"
description: "globus-job-get-output – Retrieve the output and error streams from a GRAM job"
---

<h2 class="name">NAME</h2>
<p> globus-job-get-output &#8211; Retrieve the output and error streams from a GRAM job </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-job-get-output</code> [ -r <i>RESOURCE</i> | -resource <i>RESOURCE</i> ] [OPTIONS] <i>JOBID</i> </p>
<p> <code>globus-job-get-output</code> [-help | -usage | -version | -versions ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>globus-job-get-output</code> program retrieves the output and error streams of the job named by <i>JOBID</i>. By default, <code>globus-job-get-output</code> will retrieve all output and error data from the job and display them to its own output and error streams. Other behavior can be controlled by using command-line options. The data retrieval is implemented by submitting another job which simply displays the contents of the first job&#8217;s output and error streams. By default this retrieval job is submitted to the default GRAM resource running on the same host as the job. This behavior can be controlled by specifying a particular resource manager contact string as the <i>RESOURCE</i> parameter to the <i>-r</i> or <i>-resource</i> option.</p>
<h2>OPTIONS</h2>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display a help message to standard error and exit.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the software version of the <code>globus-job-get-output</code> program to standard output.</dl>
<p> <code>-versions</code></p>
<dl>
<dt>
<dd> Display the software version of the <code>globus-job-get-output</code> program including DiRT information to standard output.</dl>
<p> <code>-resource </code><i>RESOURCE</i><code>, -r </code><i>RESOURCE</i></p>
<dl>
<dt>
<dd> Submit the retrieval job to the resource named by <i>RESOURCE</i> instead of the default GRAM service on the same host as the job contact.</dl>
<p> <code>-out</code></p>
<dl>
<dt>
<dd> Retrieve only the standard output stream of the job. The default is to retrieve both standard output and standard error.</dl>
<p> <code>-err</code></p>
<dl>
<dt>
<dd> Retrieve only the standard error stream of the job. The default is to retrieve both standard output and standard error.</dl>
<p> <code>-tail </code><i>LINES</i><code>, -t </code><i>LINES</i></p>
<dl>
<dt>
<dd> Print only the last <i>LINES</i> count lines of output from the data streams being retrieved. By default, the entire output and error file data is retrieved. This option can not be used along with the <i>-f</i> or <i>-follow</i> options.</dl>
<p> <code>-follow </code><i>LINES</i><code>, -f </code><i>LINES</i></p>
<dl>
<dt>
<dd> Print the last <i>LINES</i> count lines of output from the data streams being retrieved and then wait until canceled, printing any subsequent job output that occurs. By default, the entire output and error file data is retrieved. This option can not be used along with the <i>-t</i> or <i>-tail</i> options.</dl>
<h2>ENVIRONMENT</h2>
<p> The following variables affect the execution of <code>globus-job-get-output</code>. </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
<dd> Path to proxy credential.</dl>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
<dd> Path to trusted certificate directory.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
