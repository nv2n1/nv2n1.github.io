---
title: "npm-team(1)"
name: "npm-team"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-team/"
description: "npm-team – Manage organization teams and team memberships"
---

<h2 class="name">NAME</h2>
<p> <code>npm-team</code> &#8211; Manage organization teams and team memberships </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm team create &lt;scope:team&gt;
npm team destroy &lt;scope:team&gt;
npm team add &lt;scope:team&gt; &lt;user&gt;
npm team rm &lt;scope:team&gt; &lt;user&gt;
npm team ls &lt;scope&gt;|&lt;scope:team&gt;
npm team edit &lt;scope:team&gt;
</pre>
</dl>
<h3>Description</h3>
<p> Used to manage teams in organizations, and change team memberships. Does not handle permissions for packages. </p>
<p> Teams must always be fully qualified with the organization/scope they belong to when operating on them, separated by a colon (<code>:</code>). That is, if you have a <code>wombats</code> team in a <code>wisdom</code> organization, you must always refer to that team as <code>wisdom:wombats</code> in these commands. </p>
<p> If you have two-factor authentication enabled in <code>auth-and-writes</code> mode, then you can provide a code from your authenticator with <code>[&#8211;otp &lt;otpcode&gt;]</code>. If you don&#8217;t include this then you will be prompted.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> create / destroy: Create a new team, or destroy an existing one. Note: You cannot remove the <code>developers</code> team, &lt;a href=&quot;<a rel="nofollow" href="https://docs.npmjs.com/about-developers-team">https://docs.npmjs.com/about-developers-team</a>&quot; target=&quot;_blank&quot;&gt;learn more.&lt;/a&gt;</p>
<dt>&bull;</p>
<dd> add / rm: Add a user to an existing team, or remove a user from a team they belong to.</p>
<dt>&bull;</p>
<dd> ls: If performed on an organization name, will return a list of existing teams under that organization. If performed on a team, it will instead return a list of all users belonging to that particular team.</p>
<dt>&bull;</p>
<dd> edit: Edit a current team. </p>
</dl>
</dl>
<h3>Details</h3>
<p> <code>npm team</code> always operates directly on the current registry, configurable from the command line using <code>&#8211;registry=&lt;registry url&gt;</code>. </p>
<p> In order to create teams and manage team membership, you must be a <i>team admin</i> under the given organization. Listing teams and team memberships may be done by any member of the organizations. </p>
<p> Organization creation and management of team admins and <i>organization</i> members is done through the website, not the npm CLI. </p>
<p> To use teams to manage permissions on packages belonging to your organization, use the <code>npm access</code> command to grant or revoke the appropriate permissions.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help access</p>
<dt>&bull;</p>
<dd> npm help registry </p>
</dl>
</dl>
<h2>Index</h2>
