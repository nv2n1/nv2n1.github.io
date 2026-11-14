---
title: "git-difftool(1)"
name: "git-difftool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-difftool/"
description: "git-difftool – Show changes using common diff tools"
---

<h2 class="name">NAME</h2>
<p> git-difftool &#8211; Show changes using common diff tools </p>
<h2>SYNOPSIS</h2>
<pre><code>
git difftool[&lt;options&gt;][&lt;commit&gt;[&lt;commit&gt;]][--][&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>git difftool</i> is a Git command that allows you to compare and edit files between revisions using common diff tools. <i>git difftool</i> is a frontend to <i>git diff</i> and accepts the same options and arguments. See <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> -d, &#8211;dir-diff</p>
<dl>
<dt>
<dd> Copy the modified files to a temporary location and perform a directory diff on them. This mode never prompts before launching the diff tool.</dl>
<p> -y, &#8211;no-prompt</p>
<dl>
<dt>
<dd> Do not prompt before launching a diff tool.</dl>
<p> &#8211;prompt</p>
<dl>
<dt>
<dd> Prompt before each invocation of the diff tool. This is the default behaviour; the option is provided to override any configuration settings.</dl>
<p> &#8211;rotate-to=&lt;file&gt;</p>
<dl>
<dt>
<dd> Start showing the diff for the given path, the paths before it will move to end and output.</dl>
<p> &#8211;skip-to=&lt;file&gt;</p>
<dl>
<dt>
<dd> Start showing the diff for the given path, skipping all the paths before it.</dl>
<p> -t &lt;tool&gt;, &#8211;tool=&lt;tool&gt;</p>
<dl>
<dt>
<dd> Use the diff tool specified by &lt;tool&gt;. Valid values include emerge, kompare, meld, and vimdiff. Run <code>git difftool &#8211;tool-help</code> for the list of valid &lt;tool&gt; settings. </p>
<p> If a diff tool is not specified, <i>git difftool</i> will use the configuration variable <code>diff.tool</code>. If the configuration variable <code>diff.tool</code> is not set, <i>git difftool</i> will pick a suitable default. </p>
<p> You can explicitly provide a full path to the tool by setting the configuration variable <code>difftool.&lt;tool&gt;.path</code>. For example, you can configure the absolute path to kdiff3 by setting <code>difftool.kdiff3.path</code>. Otherwise, <i>git difftool</i> assumes the tool is available in PATH. </p>
<p> Instead of running one of the known diff tools, <i>git difftool</i> can be customized to run an alternative program by specifying the command line to invoke in a configuration variable <code>difftool.&lt;tool&gt;.cmd</code>. </p>
<p> When <i>git difftool</i> is invoked with this tool (either through the <code>-t</code> or <code>&#8211;tool</code> option or the <code>diff.tool</code> configuration variable) the configured command line will be invoked with the following variables available: <code>$LOCAL</code> is set to the name of the temporary file containing the contents of the diff pre-image and <code>$REMOTE</code> is set to the name of the temporary file containing the contents of the diff post-image. <code>$MERGED</code> is the name of the file which is being compared. <code>$BASE</code> is provided for compatibility with custom merge tool commands and has the same value as <code>$MERGED</code>.</dl>
<p> &#8211;tool-help</p>
<dl>
<dt>
<dd> Print a list of diff tools that may be used with <code>&#8211;tool</code>.</dl>
<p> &#8211;[no-]symlinks</p>
<dl>
<dt>
<dd> <i>git difftool</i>&#8216;s default behavior is create symlinks to the working tree when run in <code>&#8211;dir-diff</code> mode and the right-hand side of the comparison yields the same content as the file in the working tree. </p>
<p> Specifying <code>&#8211;no-symlinks</code> instructs <i>git difftool</i> to create copies instead. <code>&#8211;no-symlinks</code> is the default on Windows.</dl>
<p> -x &lt;command&gt;, &#8211;extcmd=&lt;command&gt;</p>
<dl>
<dt>
<dd> Specify a custom command for viewing diffs. <i>git-difftool</i> ignores the configured defaults and runs <code>$command $LOCAL $REMOTE</code> when this option is specified. Additionally, <code>$BASE</code> is set in the environment.</dl>
<p> -g, &#8211;[no-]gui</p>
<dl>
<dt>
<dd> When <i>git-difftool</i> is invoked with the <code>-g</code> or <code>&#8211;gui</code> option the default diff tool will be read from the configured <code>diff.guitool</code> variable instead of <code>diff.tool</code>. The <code>&#8211;no-gui</code> option can be used to override this setting. If <code>diff.guitool</code> is not set, we will fallback in the order of <code>merge.guitool</code>, <code>diff.tool</code>, <code>merge.tool</code> until a tool is found.</dl>
<p> &#8211;[no-]trust-exit-code</p>
<dl>
<dt>
<dd> <i>git-difftool</i> invokes a diff tool individually on each file. Errors reported by the diff tool are ignored by default. Use <code>&#8211;trust-exit-code</code> to make <i>git-difftool</i> exit when an invoked diff tool returns a non-zero exit code. </p>
<p> <i>git-difftool</i> will forward the exit code of the invoked tool when <code>&#8211;trust-exit-code</code> is used.</dl>
<p> See <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) for the full list of supported options.</p>
<h2>CONFIG VARIABLES</h2>
<p> <i>git difftool</i> falls back to <i>git mergetool</i> config variables when the difftool equivalents have not been defined. </p>
<p> diff.tool</p>
<dl>
<dt>
<dd> The default diff tool to use.</dl>
<p> diff.guitool</p>
<dl>
<dt>
<dd> The default diff tool to use when <code>&#8211;gui</code> is specified.</dl>
<p> difftool.&lt;tool&gt;.path</p>
<dl>
<dt>
<dd> Override the path for the given tool. This is useful in case your tool is not in the PATH.</dl>
<p> difftool.&lt;tool&gt;.cmd</p>
<dl>
<dt>
<dd> Specify the command to invoke the specified diff tool. </p>
<p> See the <code>&#8211;tool=&lt;tool&gt;</code> option above for more details.</dl>
<p> difftool.prompt</p>
<dl>
<dt>
<dd> Prompt before each invocation of the diff tool.</dl>
<p> difftool.trustExitCode</p>
<dl>
<dt>
<dd> Exit difftool if the invoked diff tool returns a non-zero exit status. </p>
<p> See the <code>&#8211;trust-exit-code</code> option above for more details.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1)</p>
<dl>
<dt>
<dd> Show changes between commits, commit and working tree, etc</dl>
<p> <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1)</p>
<dl>
<dt>
<dd> Run merge conflict resolution tools to resolve merge conflicts</dl>
<p> <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)</p>
<dl>
<dt>
<dd> Get and set repository or global options</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
