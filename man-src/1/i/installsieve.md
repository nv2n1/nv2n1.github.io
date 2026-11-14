---
title: "installsieve(1)"
name: "installsieve"
section: "1"
letter: "i"
url: "/docs/linux/man/1-installsieve/"
description: "installsieve – user utility for managing sieve scripts"
---

<p>&nbsp;<wbr>*</p>
<h2 class="name">NAME</h2>
<p> installsieve &#8211; user utility for managing sieve scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>installsieve</code></p>
<h2>DESCRIPTION</h2>
<p> <i>installsieve</i> is a utility that allows users to manage their sieve scripts kept on the server. </p>
<h2>OPTIONS</h2>
<p> <i>-v &lt;name&gt;</i> View script with the given name. The script if retrieved sucessfully is output to standard output. </p>
<p> <i>-l</i> List all of the scripts currently on the server. If one of the scripts is active a arrow is printed indicating that it is the active script. </p>
<p> <i>-p &lt;port&gt;</i> Port to connect to. If left off this defaults to &quot;sieve&quot; as defined in /etc/services. </p>
<p> <i>-i &lt;file&gt;</i> Install a file onto the server. If a script with the same name already exists on the server it is overwritten. Upon sucessfully putting the script on the server the script is set active. If &lt;file&gt; has the extension .script it is chopped when put on the server since sieve names may not contain a &#8216;.&#8217;. </p>
<p> <i>-a &lt;name&gt;</i> Set &lt;name&gt; as the active script. The list of available names can be obtained from the &#8216;-l&#8217; option.. </p>
<p> <i>-d &lt;name&gt;</i> Delete the sieve script on the server with &lt;name&gt;. </p>
<p> <i>-m &lt;mechanism&gt;</i> Force installsieve to use &lt;mechanism&gt; for authentication. If not specified the strongest authentication mechanism is chosen. </p>
<p> <i>-g &lt;name&gt;</i> Get the sieve script with &lt;name&gt; and save it to disk with a &quot;.script&quot; extension. If a file with that name already exists it is overwritten. </p>
<p> <i>-u &lt;user&gt;</i> Userid/Authname to use for authentication; by default, the current user. </p>
<h2>Index</h2>
