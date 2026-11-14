---
title: "sge_project(5)"
name: "sge_project"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_project/"
description: "project – Grid Engine project entry file format"
---

<p>project &#8211; Grid Engine project entry file format</p>
<h2>Description</h2>
<p>Jobs can be submitted to projects, and a project can be assigned with a certain level of importance via the functional or the override policy. This level of importance is then inherited by the jobs executing under that project. </p>
<p> A list of currently configured projects can be displayed via the <code>-sprjl</code> option. The contents of each enlisted project definition can be shown via the <code>-sprj</code> switch. The output follows the <i>project</i> format description. New projects can be created and existing can be modified via the <code>-aprj</code>, <code>-mprj</code> and <code>-dprj</code> options to </p>
<p> Note, Grid Engine allows backslashes (\) be used to escape newline (
ewline) characters. The backslash and the newline are replaced with a space (&quot; &quot;) character before any interpretation.</p>
<h2>Format</h2>
<p>A project definition contains the following parameters:</p>
<h3><code>name</code></h3>
<p>The project name as defined for <i>project_name</i> in</p>
<h3><code>oticket</code></h3>
<p>The amount of override tickets currently assigned to the project.</p>
<h3><code>fshare</code></h3>
<p>The current functional share of the project.</p>
<h3><code>acl</code></h3>
<p>A list of user access lists (ACLs &#8211; see referring to those users being allowed to submit jobs to the project. </p>
<p> If the <code>acl</code> parameter is set to NONE, all users are allowed to submit jobs to the project except for those listed in <code>xacl</code> parameter described below.</p>
<h3><code>xacl</code></h3>
<p>A list of user access lists (ACLs &#8211; see referring to those users being not allowed to submit jobs to the project.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
