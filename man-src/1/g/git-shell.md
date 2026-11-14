---
title: "git-shell(1)"
name: "git-shell"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-shell/"
description: "git-shell – Restricted login shell for Git-only SSH access"
---

<h2 class="name">NAME</h2>
<p> git-shell &#8211; Restricted login shell for Git-only SSH access </p>
<h2>SYNOPSIS</h2>
<pre>
<i>chsh</i> -s $(command -v git-shell) &lt;user&gt;
<i>git clone</i> &lt;user&gt;<code>@localhost:/path/to/repo.git</code>
<i>ssh</i> &lt;user&gt;<code>@localhost</code>
</pre>
<h2>DESCRIPTION</h2>
<p> This is a login shell for SSH accounts to provide restricted Git access. It permits execution only of server-side Git commands implementing the pull/push functionality, plus custom commands present in a subdirectory named <code>git-shell-commands</code> in the user&#8217;s home directory.</p>
<h2>COMMANDS</h2>
<p> <i>git shell</i> accepts the following commands after the <code>-c</code> option: </p>
<p> <i>git receive-pack &lt;argument&gt;</i>, <i>git upload-pack &lt;argument&gt;</i>, <i>git upload-archive &lt;argument&gt;</i></p>
<dl>
<dt>
<dd> Call the corresponding server-side command to support the client&#8217;s <i>git push</i>, <i>git fetch</i>, or <i>git archive &#8211;remote</i> request.</dl>
<p> <i>cvs server</i></p>
<dl>
<dt>
<dd> Imitate a CVS server. See <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1).</dl>
<p> If a <code>~/git-shell-commands</code> directory is present, <i>git shell</i> will also handle other, custom commands by running &quot;<code>git-shell-commands/&lt;command&gt; &lt;arguments&gt;</code>&quot; from the user&#8217;s home directory.</p>
<h2>INTERACTIVE USE</h2>
<p> By default, the commands above can be executed only with the <code>-c</code> option; the shell is not interactive. </p>
<p> If a <code>~/git-shell-commands</code> directory is present, <i>git shell</i> can also be run interactively (with no arguments). If a <code>help</code> command is present in the <code>git-shell-commands</code> directory, it is run to provide the user with an overview of allowed actions. Then a &quot;git&gt; &quot; prompt is presented at which one can enter any of the commands from the <code>git-shell-commands</code> directory, or <code>exit</code> to close the connection. </p>
<p> Generally this mode is used as an administrative interface to allow users to list repositories they have access to, create, delete, or rename repositories, or change repository descriptions and permissions. </p>
<p> If a <code>no-interactive-login</code> command exists, then it is run and the interactive shell is aborted.</p>
<h2>EXAMPLES</h2>
<p> To disable interactive logins, displaying a greeting instead: </p>
<dl>
<dt>
<dd>
<pre>
$ chsh -s /usr/bin/git-shell
$ mkdir $HOME/git-shell-commands
$ cat &gt;$HOME/git-shell-commands/no-interactive-login &lt;&lt;\EOF
#!/bin/sh
printf '%s
' &quot;Hi $USER! You've successfully authenticated, but I do not&quot;
printf '%s
' &quot;provide interactive shell access.&quot;
exit 128
EOF
$ chmod +x $HOME/git-shell-commands/no-interactive-login
</pre>
</dl>
<p> To enable git-cvsserver access (which should generally have the <code>no-interactive-login</code> example above as a prerequisite, as creating the git-shell-commands directory allows interactive logins): </p>
<dl>
<dt>
<dd>
<pre>
$ cat &gt;$HOME/git-shell-commands/cvs &lt;&lt;\EOF
if ! test $# = 1 &amp;&amp; test &quot;$1&quot; = &quot;server&quot;
then
        echo &gt;&amp;2 &quot;git-cvsserver only handles \&quot;server\&quot;&quot;
        exit 1
fi
exec git cvsserver server
EOF
$ chmod +x $HOME/git-shell-commands/cvs
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), <code><a href="/docs/linux/man/1-git-daemon/">git-daemon</a></code>(1), contrib/git-shell-commands/README</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
