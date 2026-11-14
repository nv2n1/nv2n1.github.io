---
title: "mvndebug(1)"
name: "mvndebug"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mvndebug/"
description: "mvn – software project management and comprehension tool"
---

<p>mvn &#8211; software project management and comprehension tool</p>
<h2>Description</h2>
<p>usage: mvn [options] [&lt;goal(s)&gt;] [&lt;phase(s)&gt;] usage: mvnDebug [options] [&lt;goal(s)&gt;] [&lt;phase(s)&gt;] usage: mvnyjp [options] [&lt;goal(s)&gt;] [&lt;phase(s)&gt;]</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-am</code>,&#8211;also-make</p>
<dd>If project list is specified, also build projects required by the list</p>
<dt><code>-amd</code>,&#8211;also-make-dependents</p>
<dd>If project list is specified, also build projects that depend on projects on the list</p>
<dt><code>-B</code>,&#8211;batch-mode</p>
<dd>Run in non-interactive (batch) mode</p>
<dt><code>-b</code>,&#8211;builder &lt;arg&gt;</p>
<dd>The id of the build strategy to use.</p>
<dt><code>-C</code>,&#8211;strict-checksums</p>
<dd>Fail the build if checksums don&#8217;t match</p>
<dt><code>-c</code>,&#8211;lax-checksums</p>
<dd>Warn if checksums don&#8217;t match</p>
<dt><code>-cpu</code>,&#8211;check-plugin-updates</p>
<dd>Ineffective, only kept for backward compatibility</p>
<dt><code>-D</code>,&#8211;define &lt;arg&gt;</p>
<dd>Define a system property</p>
<dt><code>-e</code>,&#8211;errors</p>
<dd>Produce execution error messages</p>
<dt><code>-emp</code>,&#8211;encrypt-master-password &lt;arg&gt;</p>
<dd>Encrypt master security password</p>
<dt><code>-ep</code>,&#8211;encrypt-password &lt;arg&gt;</p>
<dd>Encrypt server password</p>
<dt><code>-f</code>,&#8211;file &lt;arg&gt;</p>
<dd>Force the use of an alternate POM file (or directory with pom.xml).</p>
<dt><code>-fae</code>,&#8211;fail-at-end</p>
<dd>Only fail the build afterwards; allow all non-impacted builds to continue</p>
<dt><code>-ff</code>,&#8211;fail-fast</p>
<dd>Stop at first failure in reactorized builds</p>
<dt><code>-fn</code>,&#8211;fail-never</p>
<dd>NEVER fail the build, regardless of project result</p>
<dt><code>-gs</code>,&#8211;global-settings &lt;arg&gt;</p>
<dd>Alternate path for the global settings file</p>
<dt><code>-gt</code>,&#8211;global-toolchains &lt;arg&gt;</p>
<dd>Alternate path for the global toolchains file</p>
<dt><code>-h</code>,&#8211;help</p>
<dd>Display help information</p>
<dt><code>-l</code>,&#8211;log-file &lt;arg&gt;</p>
<dd>Log file to where all build output will go.</p>
<dt><code>-llr</code>,&#8211;legacy-local-repository</p>
<dd>Use Maven 2 Legacy Local Repository behaviour, ie no use of _remote.repositories. Can also be activated by using <code>-Dmaven</code>.legacyLocalRepo=true</p>
<dt><code>-N</code>,&#8211;non-recursive</p>
<dd>Do not recurse into sub-projects</p>
<dt><code>-npr</code>,&#8211;no-plugin-registry</p>
<dd>Ineffective, only kept for backward compatibility</p>
<dt><code>-npu</code>,&#8211;no-plugin-updates</p>
<dd>Ineffective, only kept for backward compatibility</p>
<dt><code>-nsu</code>,&#8211;no-snapshot-updates</p>
<dd>Suppress SNAPSHOT updates</p>
<dt><code>-o</code>,&#8211;offline</p>
<dd>Work offline</p>
<dt><code>-P</code>,&#8211;activate-profiles &lt;arg&gt;</p>
<dd>Comma-delimited list of profiles to activate</p>
<dt><code>-pl</code>,&#8211;projects &lt;arg&gt;</p>
<dd>Comma-delimited list of specified reactor projects to build instead of all projects. A project can be specified by [groupId]:artifactId or by its relative path.</p>
<dt><code>-q</code>,&#8211;quiet</p>
<dd>Quiet output &#8211; only show errors</p>
<dt><code>-rf</code>,&#8211;resume-from &lt;arg&gt;</p>
<dd>Resume reactor from specified project</p>
<dt><code>-s</code>,&#8211;settings &lt;arg&gt;</p>
<dd>Alternate path for the user settings file</p>
<dt><code>-T</code>,&#8211;threads &lt;arg&gt;</p>
<dd>Thread count, for instance 2.0C where C is core multiplied</p>
<dt><code>-t</code>,&#8211;toolchains &lt;arg&gt;</p>
<dd>Alternate path for the user toolchains file</p>
<dt><code>-U</code>,&#8211;update-snapshots</p>
<dd>Forces a check for missing releases and updated snapshots on remote repositories</p>
<dt><code>-up</code>,&#8211;update-plugins</p>
<dd>Ineffective, only kept for backward compatibility</p>
<dt><code>-V</code>,&#8211;show-version</p>
<dd>Display version information WITHOUT stopping build</p>
<dt><code>-v</code>,&#8211;version</p>
<dd>Display version information</p>
<dt><code>-X</code>,&#8211;debug</p>
<dd>Produce execution debug output </p>
</dl>
