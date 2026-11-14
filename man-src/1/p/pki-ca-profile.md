---
title: "pki-ca-profile(1)"
name: "pki-ca-profile"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-ca-profile/"
description: "pki-profile – Command-Line Interface for managing Certificate System CA profiles."
---

<h2 class="name">NAME</h2>
<p> pki-profile &#8211; Command-Line Interface for managing Certificate System CA profiles.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] ca - profile pki[CLI options] ca - profile - find[command options] pki[CLI options] ca - profile - show&lt;profile ID&gt;[command options] pki[CLI options] ca - profile - add&lt;input file path&gt;[command options] pki[CLI options] ca - profile - mod&lt;input file path&gt;[command options] pki[CLI options] ca - profile - del&lt;profile ID&gt;[command options] pki[CLI options] ca - profile - enable&lt;profile ID&gt;[command options] pki[CLI options] ca - profile - disable&lt;profile ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki ca-profile</code> commands provide command-line interfaces to manage profiles on the CA. </p>
<p> <code>pki</code> [CLI options] <code>ca-profile-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list the profiles.</dl>
<p> <code>pki</code> [CLI options] <code>ca-profile-show &lt;profile ID&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to view the details of a profile.</dl>
<p> <code>pki</code> [CLI options] <code>ca-profile-add &lt;input file path&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to create a new profile.</dl>
<p> <code>pki</code> [CLI options] <code>ca-profile-mod &lt;input file path&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to modify an existing profile.</dl>
<p> <code>pki</code> [CLI options] <code>ca-profile-del &lt;profile ID&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to delete a profile.</dl>
<p> <code>pki</code> [CLI options] <code>ca-profile-enable &lt;profile ID&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to enable a profile.</dl>
<p> <code>pki</code> [CLI options] <code>ca-profile-disable &lt;profile ID&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to disable a profile.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available profile commands, type <code>pki ca-profile</code>. To view each command&#8217;s usage, type <code> pki ca-profile-&lt;command&gt; &#8211;help</code>. </p>
<p> All the ca-profile commands require CA agent authentication. </p>
<h3>Viewing the profiles</h3>
<p> <code>pki &lt;CA agent authentication&gt; ca-profile-find</code> </p>
<p> The results can be paged using the <code>&#8211;start</code> and <code>&#8211;size</code> options described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<p> To view the contents of a profile: </p>
<p> A set of profile inputs, profile outputs, authenticators, policies and constraints are defined in a profile. These contents can be viewed using the following command: </p>
<p> <code>pki &lt;CA agent authentication&gt; ca-profile-show &lt;profile ID&gt;</code> </p>
<p> To store the output of the above operation, the output option must be specified. </p>
<p> <code>pki &lt;CA agent authentication&gt; ca-profile-show &lt;profile ID&gt; &#8211;output &lt;file path&gt;</code> </p>
<p> This output file can be used for modifying the profile. It can be used as a template for certificate enrollment as well but, a more suitable template can be fetched using the <code>pki cert-request-profile-show</code> command. The <code>pki cert-request-profile-show</code> command does not require an agent/administrator level authentication and contains only the profile inputs section (which is required for certificate enrollment). </p>
<h3>Add/Modify/Delete a profile</h3>
<p> <code>pki &lt;CA admin authentication&gt; ca-profile-add &lt;input file path&gt;</code> </p>
<p> The contents of the input file must be in an XML format returned by the ca-profile-show command. This data will be marshaled by the CLI client to create a new profile in the CA. The profile must be disabled before it is modified. It must be enabled after modification to be used for certificate enrollment. </p>
<p> To modify an existing profile: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-profile-mod &lt;input file path&gt;</code> </p>
<p> The profile data can be retrieved using the ca-profile-show command and after editing the file, it can be provided to the profile-mod command to modify an existing profile. </p>
<p> To delete a profile in the CA: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-profile-del &lt;profile ID&gt;</code> </p>
<h3>Enabling/Disabling a profile in the CA</h3>
<p> To enable a profile in the CA: </p>
<p> <code>pki &lt;CA agent authenticaton&gt; ca-profile-enable &lt;profile ID&gt;</code> </p>
<p> A profile must be enabled before it can be used. </p>
<p> To disable a profile in the CA: </p>
<p> <code>pki &lt;CA agent authentication&gt; ca-profile-disable &lt;profile ID&gt;</code> </p>
<p> A profile must be disabled before it can be modified. </p>
<p> <code>Note:</code> Modifying or deleting a profile requires user(s) that have two roles (admin and agent). The same user may be in both roles. An agent is needed to first disable the profile. Once the profile is disabled, it can be modified/deleted by an admin user. Then, an agent is needed to enable the profile for use by the CA. </p>
<h2>AUTHORS</h2>
<p> Abhishek Koneru &lt;akoneru [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki/">pki</a>(1)</code> </p>
<h2>Index</h2>
