---
title: "git-send-pack(1)"
name: "git-send-pack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-send-pack/"
description: "git-send-pack – Push objects over Git protocol to another repository"
---

<h2 class="name">NAME</h2>
<p> git-send-pack &#8211; Push objects over Git protocol to another repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git send - pack[--dry - run][--force][--receive - pack = &lt;git - receive - pack&gt;]
               [--verbose][--thin][--atomic]
               [--[no - ] signed | --signed = (true | false | if - asked)]
    [&lt;host&gt;:]&lt;directory&gt;(--all | &lt;ref&gt;...)
</code></pre>
<h2>DESCRIPTION</h2>
<p> Usually you would want to use <i>git push</i>, which is a higher-level wrapper of this command, instead. See <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1). </p>
<p> Invokes <i>git-receive-pack</i> on a possibly remote repository, and updates it from the current repository, sending named refs.</p>
<h2>OPTIONS</h2>
<p> &#8211;receive-pack=&lt;git-receive-pack&gt;</p>
<dl>
<dt>
<dd> Path to the <i>git-receive-pack</i> program on the remote end. Sometimes useful when pushing to a remote repository over ssh, and you do not have the program in a directory on the default $PATH.</dl>
<p> &#8211;exec=&lt;git-receive-pack&gt;</p>
<dl>
<dt>
<dd> Same as &#8211;receive-pack=&lt;git-receive-pack&gt;.</dl>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Instead of explicitly specifying which refs to update, update all heads that locally exist.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Take the list of refs from stdin, one per line. If there are refs specified on the command line in addition to this option, then the refs from stdin are processed after those on the command line. </p>
<p> If <code>&#8211;stateless-rpc</code> is specified together with this option then the list of refs must be in packet format (pkt-line). Each ref must be in a separate packet, and the list must end with a flush packet.</dl>
<p> &#8211;dry-run</p>
<dl>
<dt>
<dd> Do everything except actually send the updates.</dl>
<p> &#8211;force</p>
<dl>
<dt>
<dd> Usually, the command refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. This flag disables the check. What this means is that the remote repository can lose commits; use it with care.</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> Run verbosely.</dl>
<p> &#8211;thin</p>
<dl>
<dt>
<dd> Send a &quot;thin&quot; pack, which records objects in deltified form based on objects not included in the pack to reduce network traffic.</dl>
<p> &#8211;atomic</p>
<dl>
<dt>
<dd> Use an atomic transaction for updating the refs. If any of the refs fails to update then the entire push will fail without changing any refs.</dl>
<p> &#8211;[no-]signed, &#8211;signed=(true|false|if-asked)</p>
<dl>
<dt>
<dd> GPG-sign the push request to update refs on the receiving side, to allow it to be checked by the hooks and/or be logged. If <code>false</code> or <code>&#8211;no-signed</code>, no signing will be attempted. If <code>true</code> or <code>&#8211;signed</code>, the push will fail if the server does not support signed pushes. If set to <code>if-asked</code>, sign if and only if the server supports signed pushes. The push will also fail if the actual call to <code>gpg &#8211;sign</code> fails. See <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) for the details on the receiving end.</dl>
<p> &#8211;push-option=&lt;string&gt;</p>
<dl>
<dt>
<dd> Pass the specified string as a push option for consumption by hooks on the server side. If the server doesn&#8217;t support push options, error out. See <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) and <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5) for details.</dl>
<p> &lt;host&gt;</p>
<dl>
<dt>
<dd> A remote host to house the repository. When this part is specified, <i>git-receive-pack</i> is invoked via ssh.</dl>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> The repository to update.</dl>
<p> &lt;ref&gt;&#8230;</p>
<dl>
<dt>
<dd> The remote refs to update.</dl>
<h2>SPECIFYING THE REFS</h2>
<p> There are three ways to specify which refs to update on the remote end. </p>
<p> With <code>&#8211;all</code> flag, all refs that exist locally are transferred to the remote side. You cannot specify any <i>&lt;ref&gt;</i> if you use this flag. </p>
<p> Without <code>&#8211;all</code> and without any <i>&lt;ref&gt;</i>, the heads that exist both on the local side and on the remote side are updated. </p>
<p> When one or more <i>&lt;ref&gt;</i> are specified explicitly (whether on the command line or via <code>&#8211;stdin</code>), it can be either a single pattern, or a pair of such pattern separated by a colon &quot;:&quot; (this means that a ref name cannot have a colon in it). A single pattern <i>&lt;name&gt;</i> is just a shorthand for <i>&lt;name&gt;:&lt;name&gt;</i>. </p>
<p> Each pattern pair consists of the source side (before the colon) and the destination side (after the colon). The ref to be pushed is determined by finding a match that matches the source side, and where it is pushed is determined by using the destination side. The rules used to match a ref are the same rules used by <i>git rev-parse</i> to resolve a symbolic ref name. See <code><a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a></code>(1). </p>
<dl>
<dt>
<dd> &bull; It is an error if &lt;src&gt; does not match exactly one of the local refs.</dl>
<dl>
<dt>
<dd> &bull; It is an error if &lt;dst&gt; matches more than one remote refs.</dl>
<dl>
<dt>
<dd> &bull; If &lt;dst&gt; does not match any remote ref, either </p>
<dl>
<dt>
<dd> &bull; it has to start with &quot;refs/&quot;; &lt;dst&gt; is used as the destination literally in this case.</dl>
<dl>
<dt>
<dd> &bull; &lt;src&gt; == &lt;dst&gt; and the ref that matched the &lt;src&gt; must not exist in the set of remote refs; the ref matched &lt;src&gt; locally is used as the name of the destination.</dl>
</dl>
<p> Without &#8216;&#8211;force`, the &lt;src&gt; ref is stored at the remote only if &lt;dst&gt; does not exist, or &lt;dst&gt; is a proper subset (i.e. an ancestor) of &lt;src&gt;. This check, known as &quot;fast-forward check&quot;, is performed in order to avoid accidentally overwriting the remote ref and lose other peoples&#8217; commits from there. </p>
<p> With <code>&#8211;force</code>, the fast-forward check is disabled for all refs. </p>
<p> Optionally, a &lt;ref&gt; parameter can be prefixed with a plus <i>+</i> sign to disable the fast-forward check only on that ref.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
