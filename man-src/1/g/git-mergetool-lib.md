---
title: "git-mergetool-lib(1)"
name: "git-mergetool-lib"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-mergetool-lib/"
description: "git-mergetool–lib – Common Git merge tool shell scriptlets"
---

<p>git-mergetool&#8211;lib &#8211; Common Git merge tool shell scriptlets </p>
<h2>Synopsis</h2>
<pre><i>TOOL_MODE=(diff|merge) . &quot;$(git --exec-path)/git-mergetool--lib&quot;</i></pre>
<h2>Description</h2>
<p>This is not a command the end user would want to run. Ever. This documentation is meant for people who are studying the Porcelain-ish scripts and/or are writing new ones. </p>
<p> The <i>git-mergetool&#8211;lib</i> scriptlet is designed to be sourced (using <code>.</code>) by other shell scripts to set up functions for working with Git merge tools. </p>
<p> Before sourcing <i>git-mergetool&#8211;lib</i>, your script must set <code>TOOL_MODE</code> to define the operation mode for the functions listed below. <i>diff</i> and <i>merge</i> are valid values.</p>
<h2>Functions</h2>
<p>get_merge_tool</p>
<dl>
<dd>returns a merge tool. the return code is 1 if we returned a guessed merge tool, else 0. <i>$GIT_MERGETOOL_GUI</i> may be set to <i>true</i> to search for the appropriate guitool.</dl>
<p> get_merge_tool_cmd</p>
<dl>
<dd>returns the custom command for a merge tool.</dl>
<p> get_merge_tool_path</p>
<dl>
<dd>returns the custom path for a merge tool.</dl>
<p> initialize_merge_tool</p>
<dl>
<dd>bring merge tool specific functions into scope so they can be used or overridden.</dl>
<p> run_merge_tool</p>
<dl>
<dd>launches a merge tool given the tool name and a true/false flag to indicate whether a merge base is present. <i>$MERGED</i>, <i>$LOCAL</i>, <i>$REMOTE</i>, and <i>$BASE</i> must be defined for use by the merge tool.</dl>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
