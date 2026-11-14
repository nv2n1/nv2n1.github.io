---
title: "git-mergetool(1)"
name: "git-mergetool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-mergetool/"
description: "git-mergetool – Run merge conflict resolution tools to resolve merge conflicts"
---

<h2 class="name">NAME</h2>
<p> git-mergetool &#8211; Run merge conflict resolution tools to resolve merge conflicts </p>
<h2>SYNOPSIS</h2>
<pre><code>
git mergetool[--tool = &lt;tool&gt;][-y | --[no - ] prompt][&lt;file&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Use <code>git mergetool</code> to run one of several merge utilities to resolve merge conflicts. It is typically run after <i>git merge</i>. </p>
<p> If one or more &lt;file&gt; parameters are given, the merge tool program will be run to resolve differences on each file (skipping those without conflicts). Specifying a directory will include all unresolved files in that path. If no &lt;file&gt; names are specified, <i>git mergetool</i> will run the merge tool program on every file with merge conflicts.</p>
<h2>OPTIONS</h2>
<p> -t &lt;tool&gt;, &#8211;tool=&lt;tool&gt;</p>
<dl>
<dt>
<dd> Use the merge resolution program specified by &lt;tool&gt;. Valid values include emerge, gvimdiff, kdiff3, meld, vimdiff, and tortoisemerge. Run <code>git mergetool &#8211;tool-help</code> for the list of valid &lt;tool&gt; settings. </p>
<p> If a merge resolution program is not specified, <i>git mergetool</i> will use the configuration variable <code>merge.tool</code>. If the configuration variable <code>merge.tool</code> is not set, <i>git mergetool</i> will pick a suitable default. </p>
<p> You can explicitly provide a full path to the tool by setting the configuration variable <code>mergetool.&lt;tool&gt;.path</code>. For example, you can configure the absolute path to kdiff3 by setting <code>mergetool.kdiff3.path</code>. Otherwise, <i>git mergetool</i> assumes the tool is available in PATH. </p>
<p> Instead of running one of the known merge tool programs, <i>git mergetool</i> can be customized to run an alternative program by specifying the command line to invoke in a configuration variable <code>mergetool.&lt;tool&gt;.cmd</code>. </p>
<p> When <i>git mergetool</i> is invoked with this tool (either through the <code>-t</code> or <code>&#8211;tool</code> option or the <code>merge.tool</code> configuration variable) the configured command line will be invoked with <code>$BASE</code> set to the name of a temporary file containing the common base for the merge, if available; <code>$LOCAL</code> set to the name of a temporary file containing the contents of the file on the current branch; <code>$REMOTE</code> set to the name of a temporary file containing the contents of the file to be merged, and <code>$MERGED</code> set to the name of the file to which the merge tool should write the result of the merge resolution. </p>
<p> If the custom merge tool correctly indicates the success of a merge resolution with its exit code, then the configuration variable <code>mergetool.&lt;tool&gt;.trustExitCode</code> can be set to <code>true</code>. Otherwise, <i>git mergetool</i> will prompt the user to indicate the success of the resolution after the custom tool has exited.</dl>
<p> &#8211;tool-help</p>
<dl>
<dt>
<dd> Print a list of merge tools that may be used with <code>&#8211;tool</code>.</dl>
<p> -y, &#8211;no-prompt</p>
<dl>
<dt>
<dd> Don&#8217;t prompt before each invocation of the merge resolution program. This is the default if the merge resolution program is explicitly specified with the <code>&#8211;tool</code> option or with the <code>merge.tool</code> configuration variable.</dl>
<p> &#8211;prompt</p>
<dl>
<dt>
<dd> Prompt before each invocation of the merge resolution program to give the user a chance to skip the path.</dl>
<p> -g, &#8211;gui</p>
<dl>
<dt>
<dd> When <i>git-mergetool</i> is invoked with the <code>-g</code> or <code>&#8211;gui</code> option the default merge tool will be read from the configured <code>merge.guitool</code> variable instead of <code>merge.tool</code>. If <code>merge.guitool</code> is not set, we will fallback to the tool configured under <code>merge.tool</code>.</dl>
<p> &#8211;no-gui</p>
<dl>
<dt>
<dd> This overrides a previous <code>-g</code> or <code>&#8211;gui</code> setting and reads the default merge tool will be read from the configured <code>merge.tool</code> variable.</dl>
<p> -O&lt;orderfile&gt;</p>
<dl>
<dt>
<dd> Process files in the order specified in the &lt;orderfile&gt;, which has one shell glob pattern per line. This overrides the <code>diff.orderFile</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). To cancel <code>diff.orderFile</code>, use <code>-O/dev/null</code>.</dl>
<h2>CONFIGURATION</h2>
<p> mergetool.&lt;tool&gt;.path</p>
<dl>
<dt>
<dd> Override the path for the given tool. This is useful in case your tool is not in the PATH.</dl>
<p> mergetool.&lt;tool&gt;.cmd</p>
<dl>
<dt>
<dd> Specify the command to invoke the specified merge tool. The specified command is evaluated in shell with the following variables available: <i>BASE</i> is the name of a temporary file containing the common base of the files to be merged, if available; <i>LOCAL</i> is the name of a temporary file containing the contents of the file on the current branch; <i>REMOTE</i> is the name of a temporary file containing the contents of the file from the branch being merged; <i>MERGED</i> contains the name of the file to which the merge tool should write the results of a successful merge.</dl>
<p> mergetool.&lt;tool&gt;.hideResolved</p>
<dl>
<dt>
<dd> Allows the user to override the global <code>mergetool.hideResolved</code> value for a specific tool. See <code>mergetool.hideResolved</code> for the full description.</dl>
<p> mergetool.&lt;tool&gt;.trustExitCode</p>
<dl>
<dt>
<dd> For a custom merge command, specify whether the exit code of the merge command can be used to determine whether the merge was successful. If this is not set to true then the merge target file timestamp is checked and the merge assumed to have been successful if the file has been updated, otherwise the user is prompted to indicate the success of the merge.</dl>
<p> mergetool.meld.hasOutput</p>
<dl>
<dt>
<dd> Older versions of <code>meld</code> do not support the <code>&#8211;output</code> option. Git will attempt to detect whether <code>meld</code> supports <code>&#8211;output</code> by inspecting the output of <code>meld &#8211;help</code>. Configuring <code>mergetool.meld.hasOutput</code> will make Git skip these checks and use the configured value instead. Setting <code>mergetool.meld.hasOutput</code> to <code>true</code> tells Git to unconditionally use the <code>&#8211;output</code> option, and <code>false</code> avoids using <code>&#8211;output</code>.</dl>
<p> mergetool.meld.useAutoMerge</p>
<dl>
<dt>
<dd> When the <code>&#8211;auto-merge</code> is given, meld will merge all non-conflicting parts automatically, highlight the conflicting parts and wait for user decision. Setting <code>mergetool.meld.useAutoMerge</code> to <code>true</code> tells Git to unconditionally use the <code>&#8211;auto-merge</code> option with <code>meld</code>. Setting this value to <code>auto</code> makes git detect whether <code>&#8211;auto-merge</code> is supported and will only use <code>&#8211;auto-merge</code> when available. A value of <code>false</code> avoids using <code>&#8211;auto-merge</code> altogether, and is the default value.</dl>
<p> mergetool.hideResolved</p>
<dl>
<dt>
<dd> During a merge Git will automatically resolve as many conflicts as possible and write the <i>MERGED</i> file containing conflict markers around any conflicts that it cannot resolve; <i>LOCAL</i> and <i>REMOTE</i> normally represent the versions of the file from before Git&#8217;s conflict resolution. This flag causes <i>LOCAL</i> and <i>REMOTE</i> to be overwriten so that only the unresolved conflicts are presented to the merge tool. Can be configured per-tool via the <code>mergetool.&lt;tool&gt;.hideResolved</code> configuration variable. Defaults to <code>false</code>.</dl>
<p> mergetool.keepBackup</p>
<dl>
<dt>
<dd> After performing a merge, the original file with conflict markers can be saved as a file with a <code>.orig</code> extension. If this variable is set to <code>false</code> then this file is not preserved. Defaults to <code>true</code> (i.e. keep the backup files).</dl>
<p> mergetool.keepTemporaries</p>
<dl>
<dt>
<dd> When invoking a custom merge tool, Git uses a set of temporary files to pass to the tool. If the tool returns an error and this variable is set to <code>true</code>, then these temporary files will be preserved, otherwise they will be removed after the tool has exited. Defaults to <code>false</code>.</dl>
<p> mergetool.writeToTemp</p>
<dl>
<dt>
<dd> Git writes temporary <i>BASE</i>, <i>LOCAL</i>, and <i>REMOTE</i> versions of conflicting files in the worktree by default. Git will attempt to use a temporary directory for these files when set <code>true</code>. Defaults to <code>false</code>.</dl>
<p> mergetool.prompt</p>
<dl>
<dt>
<dd> Prompt before each invocation of the merge resolution program.</dl>
<h2>TEMPORARY FILES</h2>
<p> <code>git mergetool</code> creates <code>*.orig</code> backup files while resolving merges. These are safe to remove once a file has been merged and its <code>git mergetool</code> session has completed. </p>
<p> Setting the <code>mergetool.keepBackup</code> configuration variable to <code>false</code> causes <code>git mergetool</code> to automatically remove the backup as files are successfully merged.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
