---
title: "ompi-ps(1)"
name: "ompi-ps"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ompi-ps/"
description: "ompi-ps, orte-ps – Displays information about the active jobs and processes in Open MPI."
---

<h2 class="name">NAME</h2>
<p> ompi-ps, orte-ps &#8211; Displays information about the active jobs and processes in Open MPI. </p>
<p> <code>NOTE:</code> <i>ompi-ps</i>, and <i>orte-ps</i> are exact synonyms for each other. Using any of the names will result in exactly identical behavior. </p>
<h2>SYNOPSIS</h2>
<p> <code>ompi-ps</code> <code>[ options ]</code></p>
<h2>Options</h2>
<p> <i>ompi-ps</i> will display information about running job(s) in the current universe.</p>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Display help for this command</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Enable verbose output for debugging</p>
<dt><code>&#8211;daemons</code></p>
<dd> Display daemon job information.</p>
<dt><code>-j | &#8211;jobid</code></p>
<dd> Display the state of a specific job in the universe. By default all jobs will be displayed.</p>
<dt><code>-p | &#8211;vpid</code></p>
<dd> Display the state of a specific vpid (process) in the universe. By default all vpids cooresponding to processes will be displayed. Must be used in conjunction with the <code>&#8211;jobid</code> option.</p>
<dt><code>-n | &#8211;nodes</code></p>
<dd> Display all of the allocated nodes, and their cooresponding states. By default this is disabled.</p>
<dt><code>-gmca | &#8211;gmca </code>&lt;key&gt; &lt;value&gt;</p>
<dd> Pass global MCA parameters that are applicable to all contexts. <i>&lt;key&gt;</i> is the parameter name; <i>&lt;value&gt;</i> is the parameter value.</p>
<dt><code>-mca | &#8211;mca &lt;key&gt; &lt;value&gt;</code></p>
<dd> Send arguments to various MCA modules.</dl>
<h2>DESCRIPTION</h2>
<p> <i>ompi-ps</i> displays the state of jobs running inside an Open RTE universe.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-orterun/">orterun</a>(1), <a href="/docs/linux/man/1-orte-clean/">orte-clean</a>(1) </p>
<h2>Index</h2>
