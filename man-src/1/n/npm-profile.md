---
title: "npm-profile(1)"
name: "npm-profile"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-profile/"
description: "npm-profile – Change settings on your registry profile"
---

<h2 class="name">NAME</h2>
<p> <code>npm-profile</code> &#8211; Change settings on your registry profile </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm profile get[--json | --parseable][&lt;property&gt;] npm profile set[--json | --parseable]&lt;property&gt;&lt;value&gt;
        npm profile set password
            npm profile enable -
    2fa [auth - and-writes | auth - only] npm profile disable - 2fa
</code></pre>
</dl>
<h3>Description</h3>
<p> Change your profile information on the registry. This not be available if you&#8217;re using a non-npmjs registry.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm profile get [&lt;property&gt;]</code>: Display all of the properties of your profile, or one or more specific properties. It looks like: </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<pre><code>
+ -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | name | example |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | email | me[at] example.com(verified) |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | two factor auth | auth - and-writes |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | fullname | Example User |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | homepage | |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | freenode | |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | twitter | |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | github | |
    +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | created | 2015 - 02 -
    26T01:38:35.892Z |
             +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+ | updated | 2017 - 10 -
    02T21:29
         :45.922Z |
          +-- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -- -+
</code></pre>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm profile set &lt;property&gt; &lt;value&gt;</code>: Set the value of a profile property. You can set the following properties this way:<br />
&nbsp;<wbr>&nbsp;email, fullname, homepage, freenode, twitter, github</p>
<dt>&bull;</p>
<dd> <code>npm profile set password</code>: Change your password. This is interactive, you&#8217;ll be prompted for your current password and a new password. You&#8217;ll also be prompted for an OTP if you have two-factor authentication enabled.</p>
<dt>&bull;</p>
<dd> <code>npm profile enable-2fa [auth-and-writes|auth-only]</code>: Enables two-factor authentication. Defaults to <code>auth-and-writes</code> mode. Modes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>auth-only</code>: Require an OTP when logging in or making changes to your account&#8217;s authentication. The OTP will be required on both the website and the command line.</p>
<dt>&bull;</p>
<dd> <code>auth-and-writes</code>: Requires an OTP at all the times <code>auth-only</code> does, and also requires one when publishing a module, setting the <code>latest</code> dist-tag, or changing access via <code>npm access</code> and <code>npm owner</code>. </p>
</dl>
</dl>
<dt>&bull;</p>
<dd> <code>npm profile disable-2fa</code>: Disables two-factor authentication. </p>
</dl>
</dl>
<h3>Details</h3>
<p> All of the <code>npm profile</code> subcommands accept <code>&#8211;json</code> and <code>&#8211;parseable</code> and will tailor their output based on those. Some of these commands may not be available on non npmjs.com registries.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help config </p>
</dl>
</dl>
<h2>Index</h2>
