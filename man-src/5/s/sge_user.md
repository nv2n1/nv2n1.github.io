---
title: "sge_user(5)"
name: "sge_user"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_user/"
description: "user – Grid Engine user entry file format"
---

<p>user &#8211; Grid Engine user entry file format</p>
<h2>Description</h2>
<p>A user entry is used to store ticket and usage information on a per user basis. Maintaining user entries for all users participating in a Grid Engine system is required if Grid Engine is operated under a user share tree policy. </p>
<p> If the <code>enforce_user</code> cluster configuration parameter is set to <i>auto</i>, a user object for the submitting user will be created automatically during job submission, if one does not already exist. The <code>auto_user_oticket</code>, <code>auto_user_fshare</code>, <code>auto_user_default_project</code>, and <code>auto_user_delete_time</code> cluster configuration parameters will be used as default attributes of the new user object. </p>
<p> A list of currently configured user entries can be displayed via the <code>-suserl</code> option. The contents of each enlisted user entry can be shown via the <code>-suser</code> switch. The output follows the <i>user</i> format description. New user entries can be created and existing can be modified via the <code>-auser</code>, <code>-muser</code> and <code>-duser</code> options to </p>
<p> Note, Grid Engine allows backslashes (\) be used to escape newline (
ewline) characters. The backslash and the newline are replaced with a space (&quot; &quot;) character before any interpretation.</p>
<h2>Format</h2>
<p>A user entry contains four parameters:</p>
<h3><code>name</code></h3>
<p>The user name as defined for <i>user_name</i> in</p>
<h3><code>oticket</code></h3>
<p>The amount of override tickets currently assigned to the user.</p>
<h3><code>fshare</code></h3>
<p>The current functional share of the user.</p>
<h3><code>default_project</code></h3>
<p>The default project of the user.</p>
<h3><code>delete_time</code></h3>
<p><code>Note:</code> Deprecated, may be removed in future release.<br />
 The wall-clock time when this user will be deleted, expressed as the number of seconds elapsed since January 1, 1970. If set to zero, the affected user is a permanent user. If set to one, the user currently has active jobs. For additional information about automatically created users, see the <code>enforce_user</code> and <code>auto_user_delete_time</code> parameters in</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
