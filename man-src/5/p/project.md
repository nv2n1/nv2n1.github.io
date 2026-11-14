---
title: "project(5)"
name: "project"
section: "5"
letter: "p"
url: "/docs/linux/man/5-project/"
description: "project – xxQS_NAMExx project entry file format"
---

<p>project &#8211; xxQS_NAMExx project entry file format</p>
<h2>Description</h2>
<p>Jobs can be submitted to projects, and a project can be assigned with a certain level of importance, via the functional or the override policy. This level of importance is then inherited by the jobs executing under that project. </p>
<p> A list of currently configured projects can be displayed via the <code>-sprjl</code> option. The contents of each listed project definition can be shown via the <code>-sprj</code> switch. The output follows the <i>project</i> format description. New projects can be created, and existing ones can be modified, via the <code>-aprj</code>, <code>-mprj</code> and <code>-dprj</code> options to </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>A project definition contains the following parameters:</p>
<h3><code>name</code></h3>
<p>The project name in the format for <i>project_name</i> in</p>
<h3><code>oticket</code></h3>
<p>The number of override tickets currently assigned to the project.</p>
<h3><code>fshare</code></h3>
<p>The current functional share of the project.</p>
<h3><code>acl</code></h3>
<p>A list of user access lists (ACLs &#8211; see referring to those users allowed to submit jobs to the project. </p>
<p> If the <code>acl</code> parameter is set to NONE, all users are allowed to submit jobs to the project except for those listed in the <code>xacl</code> parameter described below.</p>
<h3><code>xacl</code></h3>
<p>A list of user access lists (ACLs &#8211; see referring to those users not allowed to submit jobs to the project.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
