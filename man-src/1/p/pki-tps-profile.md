---
title: "pki-tps-profile(1)"
name: "pki-tps-profile"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-tps-profile/"
description: "pki-tps-profile – Command-Line Interface for managing Certificate System TPS profiles."
---

<h2 class="name">NAME</h2>
<p> pki-tps-profile &#8211; Command-Line Interface for managing Certificate System TPS profiles.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] tps - profile pki[CLI options] tps - profile - find[command options] pki[CLI options] tps - profile - show&lt;profile ID&gt;[command options] pki[CLI options] tps - profile - add-- input&lt;file path&gt;[command options] pki[CLI options] tps - profile - mod&lt;profile ID&gt; &amp;nbsp;
--action&lt;action&gt;[command options] pki[CLI options] tps - profile - mod&lt;profile ID&gt; &amp;nbsp;
--input&lt;file path&gt;[command options] pki[CLI options] tps - profile - del&lt;profile ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki tps-profile</code> commands provide command-line interfaces to manage profiles on the TPS. </p>
<p> <code>pki</code> [CLI options] <code>tps-profile-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list the profiles.</dl>
<p> <code>pki</code> [CLI options] <code>tps-profile-show &lt;profile ID&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to view the details of a profile.</dl>
<p> <code>pki</code> [CLI options] <code>tps-profile-add &#8211;input &lt;file path&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to create a new profile.</dl>
<p> <code>pki</code> [CLI options] <code>tps-profile-mod &lt;profile ID&gt;&nbsp;<wbr>&#8211;action &lt;action&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to change the status of a profile.</dl>
<p> <code>pki</code> [CLI options] <code>tps-profile-mod &lt;profile ID&gt;&nbsp;<wbr>&#8211;input &lt;file path&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to modify an existing profile.</dl>
<p> <code>pki</code> [CLI options] <code>tps-profile-del &lt;profile ID&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to delete a profile.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available profile commands, type <code>pki tps-profile</code>. To view each command&#8217;s usage, type <code> pki tps-profile-&lt;command&gt; &#8211;help</code>. </p>
<p> All the tps-profile commands require TPS admin or agent authentication. </p>
<h3>Listing profiles</h3>
<p> To list all profile: </p>
<p> <code>pki &lt;TPS admin/agent authentication&gt; tps-profile-find</code> </p>
<p> The results can be paged using the <code>&#8211;start</code> and <code>&#8211;size</code> options described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h3>Viewing a profile</h3>
<p> To view the status and properties of a profile: </p>
<p> <code>pki &lt;TPS admin/agent authentication&gt; tps-profile-show &lt;profile ID&gt;</code> </p>
<p> To store the output of the above operation into a file: </p>
<p> <code>pki &lt;TPS admin/agent authentication&gt; tps-profile-show &lt;profile ID&gt; &#8211;output &lt;file path&gt;</code> </p>
<h3>Adding a profile</h3>
<p> To add a new profile, prepare an input file specifying the profile properties in the following format: </p>
<dl>
<dt>
<dd>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;yes&quot;?&gt;
&lt;Profile id=&quot;...&quot; xmlns:ns2=&quot;<a rel="nofollow" href="http://www.w3.org/2005/Atom">http://www.w3.org/2005/Atom</a>&quot;&gt;
    &lt;Properties&gt;
        &lt;Property name=&quot;...&quot;&gt;...&lt;/Property&gt;
        ...
    &lt;/Properties&gt;
&lt;/Profile&gt;
</pre>
</dl>
<p> The profile properties are described in <code><a href="/docs/linux/man/5-pki-tps-profile/">pki-tps-profile</a></code>(5). Then execute the following command: </p>
<p> <code>pki &lt;TPS admin authentication&gt; tps-profile-add &#8211;input &lt;file path&gt;</code> </p>
<h3>Changing profile status</h3>
<p> To change the profile status execute the following command: </p>
<p> <code>pki &lt;TPS admin/agent authentication&gt; tps-profile-mod &lt;profile ID&gt; &#8211;action &lt;action&gt;</code> </p>
<p> Available actions for admins: submit, cancel. Available actions for agents: approve, reject. Available actions for users with both admin and agent rights: enable, disable. </p>
<h3>Modifying a profile</h3>
<p> To modify a profile, first disable the profile using the <code>tps-profile-mod &#8211;action disable</code> command. Then download the current profile properties using the <code>tps-profile-show &#8211;output</code> command. Make the modifications in the file, then upload the updated file using the following command: </p>
<p> <code>pki &lt;TPS admin authentication&gt; tps-profile-mod &lt;profile ID&gt; &#8211;input &lt;file path&gt;</code> </p>
<p> Finally, the profile should be re-enabled using the <code>tps-profile-mod &#8211;action enable</code> command. </p>
<h3>Deleting a profile</h3>
<p> To delete a profile, first disable the profile using the <code>tps-profile-mod &#8211;action disable</code> command, then execute: </p>
<p> <code>pki &lt;TPS admin authentication&gt; tps-profile-del &lt;profile ID&gt;</code> </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki/">pki</a>(1),</code> <code><a href="/docs/linux/man/5-pki-tps-profile/">pki-tps-profile</a>(5)</code> </p>
<h2>Index</h2>
