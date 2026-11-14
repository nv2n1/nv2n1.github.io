---
title: "git-upload-archive(1)"
name: "git-upload-archive"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-upload-archive/"
description: "git-upload-archive – Send archive back to git-archive"
---

<h2 class="name">NAME</h2>
<p> git-upload-archive &#8211; Send archive back to git-archive </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git upload-archive</i> &lt;directory&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> Invoked by <i>git archive &#8211;remote</i> and sends a generated archive to the other end over the Git protocol. </p>
<p> This command is usually not invoked directly by the end user. The UI for the protocol is on the <i>git archive</i> side, and the program pair is meant to be used to get an archive from a remote repository.</p>
<h2>SECURITY</h2>
<p> In order to protect the privacy of objects that have been removed from history but may not yet have been pruned, <code>git-upload-archive</code> avoids serving archives for commits and trees that are not reachable from the repository&#8217;s refs. However, because calculating object reachability is computationally expensive, <code>git-upload-archive</code> implements a stricter but easier-to-check set of rules: </p>
<dl>
<dt>
<dd> 1. Clients may request a commit or tree that is pointed to directly by a ref. E.g., <code>git archive &#8211;remote=origin v1.0</code>.</dl>
<dl>
<dt>
<dd> 2. Clients may request a sub-tree within a commit or tree using the <code>ref:path</code> syntax. E.g., <code>git archive &#8211;remote=origin v1.0:Documentation</code>.</dl>
<dl>
<dt>
<dd> 3. Clients may <i>not</i> use other sha1 expressions, even if the end result is reachable. E.g., neither a relative commit like <code>master^</code> nor a literal sha1 like <code>abcd1234</code> is allowed, even if the result is reachable from the refs.</dl>
<p> Note that rule 3 disallows many cases that do not have any privacy implications. These rules are subject to change in future versions of git, and the server accessed by <code>git archive &#8211;remote</code> may or may not follow these exact rules. </p>
<p> If the config option <code>uploadArchive.allowUnreachable</code> is true, these rules are ignored, and clients may use arbitrary sha1 expressions. This is useful if you do not care about the privacy of unreachable objects, or if your object database is already publicly available for access via non-smart-http.</p>
<h2>OPTIONS</h2>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> The repository to get a tar archive from.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
