---
title: "fedora-create-review(1)"
name: "fedora-create-review"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fedora-create-review/"
description: "fedora-create-review – Automatically create RPM review request for Fedora."
---

<h2>NAME</h2>
<p> fedora-create-review &#8211; Automatically create RPM review request for Fedora. </p>
<h2>SYNOPSIS</h2>
<p> <code>fedora-create-review</code> &lt;specfile&gt; &lt;srpmfile&gt; </p>
<h2>DESCRIPTION</h2>
<p> This tool create review request for rpm packages for Fedora. It starts a scratch build on koji, upload your file onto fedorapeople, create the review request and add a comment that the scratch-build on koji was successful. </p>
<h2>USAGE</h2>
<p> This program creates RPM review request for Fedora.</p>
<dl>
<dt>
<dd>fedora-create-review &lt;specfile&gt; &lt;srpmfile&gt; </p>
<p> This will start a build on koji using the given srpmfile. If the build is successful, both file will be uploaded onto fedorapeople. Finally, the review request is generated and a comment is added on the bug about the successful scratch-build. </p>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;user</code><br />
&nbsp;<wbr>FAS user name. </p>
<p> <code>&#8211;rename-request</code><br />
&nbsp;<wbr>To create a rename request instead of a review request. </p>
<p> <code>&#8211;koji-target</code><br />
&nbsp;<wbr>Specify the target for the scratch build. Defaults to rawhide.&nbsp;<wbr><br />
&nbsp;<wbr>The list of targets can be obtained using&nbsp;<wbr>`koji list-targets`. </p>
<p> <code>&#8211;no-scratch-build</code><br />
&nbsp;<wbr>To skip the scratch build but still create the review. </p>
<p> <code>&#8211;debug</code><br />
&nbsp;<wbr>Provides a more detailed output of what&#8217;s going on. </p>
<p> <code>&#8211;test</code><br />
&nbsp;<wbr>Create the review on a test bugzilla instance instead of the official one. </p>
<h2>FILES</h2>
<p> <i>$HOME/.config/fedora-create-review</i></p>
<dl>
<dt>
<dd> User configuration files for fedora-create-review</dl>
<h2>AUTHORS</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>Original author: Pierre-Yves Chibon&nbsp;<wbr>&lt;pingou [at] pingoured.fr&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Developers:<br />
Pierre-Yves Chibon&nbsp;<wbr>&lt;pingou [at] pingoured.fr&gt;<br />
Stanislav Ochotnicky&nbsp;<wbr>&lt;sochotnicky [at] redhat.com&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>For a list of all contributors see AUTHORS file </p>
<p> No known bugs at this time </p>
<h2>Index</h2>
