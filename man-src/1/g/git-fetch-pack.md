---
title: "git-fetch-pack(1)"
name: "git-fetch-pack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-fetch-pack/"
description: "git-fetch-pack – Receive missing objects from another repository"
---

<h2 class="name">NAME</h2>
<p> git-fetch-pack &#8211; Receive missing objects from another repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git fetch - pack[--all][--quiet | -q][--keep | -k][--thin][--include - tag]
                [--upload - pack = &lt;git - upload - pack&gt;]
                [--depth = &lt;n&gt;][--no - progress]
                [-v]&lt;repository&gt;[&lt;refs&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Usually you would want to use <i>git fetch</i>, which is a higher level wrapper of this command, instead. </p>
<p> Invokes <i>git-upload-pack</i> on a possibly remote repository and asks it to send objects missing from this repository, to update the named heads. The list of commits available locally is found out by scanning the local refs/ hierarchy and sent to <i>git-upload-pack</i> running on the other end. </p>
<p> This command degenerates to download everything to complete the asked refs from the remote side when the local side does not have a common ancestor commit.</p>
<h2>OPTIONS</h2>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Fetch all remote refs.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Take the list of refs from stdin, one per line. If there are refs specified on the command line in addition to this option, then the refs from stdin are processed after those on the command line. </p>
<p> If <code>&#8211;stateless-rpc</code> is specified together with this option then the list of refs must be in packet format (pkt-line). Each ref must be in a separate packet, and the list must end with a flush packet.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Pass <code>-q</code> flag to <i>git unpack-objects</i>; this makes the cloning process less verbose.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Do not invoke <i>git unpack-objects</i> on received data, but create a single packfile out of it instead, and store it in the object database. If provided twice then the pack is locked against repacking.</dl>
<p> &#8211;thin</p>
<dl>
<dt>
<dd> Fetch a &quot;thin&quot; pack, which records objects in deltified form based on objects not included in the pack to reduce network traffic.</dl>
<p> &#8211;include-tag</p>
<dl>
<dt>
<dd> If the remote side supports it, annotated tags objects will be downloaded on the same connection as the other objects if the object the tag references is downloaded. The caller must otherwise determine the tags this option made available.</dl>
<p> &#8211;upload-pack=&lt;git-upload-pack&gt;</p>
<dl>
<dt>
<dd> Use this to specify the path to <i>git-upload-pack</i> on the remote side, if is not found on your $PATH. Installations of sshd ignores the user&#8217;s environment setup scripts for login shells (e.g. .bash_profile) and your privately installed git may not be found on the system default $PATH. Another workaround suggested is to set up your $PATH in &quot;.bashrc&quot;, but this flag is for people who do not want to pay the overhead for non-interactive shells by having a lean .bashrc file (they set most of the things up in .bash_profile).</dl>
<p> &#8211;exec=&lt;git-upload-pack&gt;</p>
<dl>
<dt>
<dd> Same as &#8211;upload-pack=&lt;git-upload-pack&gt;.</dl>
<p> &#8211;depth=&lt;n&gt;</p>
<dl>
<dt>
<dd> Limit fetching to ancestor-chains not longer than n. <i>git-upload-pack</i> treats the special depth 2147483647 as infinite even if there is an ancestor-chain that long.</dl>
<p> &#8211;shallow-since=&lt;date&gt;</p>
<dl>
<dt>
<dd> Deepen or shorten the history of a shallow repository to include all reachable commits after &lt;date&gt;.</dl>
<p> &#8211;shallow-exclude=&lt;revision&gt;</p>
<dl>
<dt>
<dd> Deepen or shorten the history of a shallow repository to exclude commits reachable from a specified remote branch or tag. This option can be specified multiple times.</dl>
<p> &#8211;deepen-relative</p>
<dl>
<dt>
<dd> Argument &#8211;depth specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history.</dl>
<p> &#8211;no-progress</p>
<dl>
<dt>
<dd> Do not show the progress.</dl>
<p> &#8211;check-self-contained-and-connected</p>
<dl>
<dt>
<dd> Output &quot;connectivity-ok&quot; if the received pack is self-contained and connected.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Run verbosely.</dl>
<p> &lt;repository&gt;</p>
<dl>
<dt>
<dd> The URL to the remote repository.</dl>
<p> &lt;refs&gt;&#8230;</p>
<dl>
<dt>
<dd> The remote heads to update from. This is relative to $GIT_DIR (e.g. &quot;HEAD&quot;, &quot;refs/heads/master&quot;). When unspecified, update from all heads the remote side has. </p>
<p> If the remote has enabled the options <code>uploadpack.allowTipSHA1InWant</code>, <code>uploadpack.allowReachableSHA1InWant</code>, or <code>uploadpack.allowAnySHA1InWant</code>, they may alternatively be 40-hex sha1s present on the remote.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
