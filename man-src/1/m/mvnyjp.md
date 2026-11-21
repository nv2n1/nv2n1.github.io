---

title: "mvnyjp(1)"
name: "mvnyjp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mvnyjp/"
description: "mvn – software project management and comprehension tool"
---

<h2>NAME</h2>
<p> mvn &#8211; software project management and comprehension tool</p>
<p> usage: mvn [options] [&lt;goal(s)&gt;] [&lt;phase(s)&gt;] usage: mvnDebug [options] [&lt;goal(s)&gt;] [&lt;phase(s)&gt;] usage: mvnyjp [options] [&lt;goal(s)&gt;] [&lt;phase(s)&gt;]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-am</code>,&#8211;also-make</dt>
<dd> If project list is specified, also build projects required by the list</dd>
<dt><code>-amd</code>,&#8211;also-make-dependents</dt>
<dd> If project list is specified, also build projects that depend on projects on the list</dd>
<dt><code>-B</code>,&#8211;batch-mode</dt>
<dd> Run in non-interactive (batch) mode</dd>
<dt><code>-b</code>,&#8211;builder &lt;arg&gt;</dt>
<dd> The id of the build strategy to use.</dd>
<dt><code>-C</code>,&#8211;strict-checksums</dt>
<dd> Fail the build if checksums don&#8217;t match</dd>
<dt><code>-c</code>,&#8211;lax-checksums</dt>
<dd> Warn if checksums don&#8217;t match</dd>
<dt><code>-cpu</code>,&#8211;check-plugin-updates</dt>
<dd> Ineffective, only kept for backward compatibility</dd>
<dt><code>-D</code>,&#8211;define &lt;arg&gt;</dt>
<dd> Define a system property</dd>
<dt><code>-e</code>,&#8211;errors</dt>
<dd> Produce execution error messages</dd>
<dt><code>-emp</code>,&#8211;encrypt-master-password &lt;arg&gt;</dt>
<dd> Encrypt master security password</dd>
<dt><code>-ep</code>,&#8211;encrypt-password &lt;arg&gt;</dt>
<dd> Encrypt server password</dd>
<dt><code>-f</code>,&#8211;file &lt;arg&gt;</dt>
<dd> Force the use of an alternate POM file (or directory with pom.xml).</dd>
<dt><code>-fae</code>,&#8211;fail-at-end</dt>
<dd> Only fail the build afterwards; allow all non-impacted builds to continue</dd>
<dt><code>-ff</code>,&#8211;fail-fast</dt>
<dd> Stop at first failure in reactorized builds</dd>
<dt><code>-fn</code>,&#8211;fail-never</dt>
<dd> NEVER fail the build, regardless of project result</dd>
<dt><code>-gs</code>,&#8211;global-settings &lt;arg&gt;</dt>
<dd> Alternate path for the global settings file</dd>
<dt><code>-gt</code>,&#8211;global-toolchains &lt;arg&gt;</dt>
<dd> Alternate path for the global toolchains file</dd>
<dt><code>-h</code>,&#8211;help</dt>
<dd> Display help information</dd>
<dt><code>-l</code>,&#8211;log-file &lt;arg&gt;</dt>
<dd> Log file to where all build output will go.</dd>
<dt><code>-llr</code>,&#8211;legacy-local-repository</dt>
<dd> Use Maven 2 Legacy Local Repository behaviour, ie no use of _remote.repositories. Can also be activated by using <code>-Dmaven</code>.legacyLocalRepo=true</dd>
<dt><code>-N</code>,&#8211;non-recursive</dt>
<dd> Do not recurse into sub-projects</dd>
<dt><code>-npr</code>,&#8211;no-plugin-registry</dt>
<dd> Ineffective, only kept for backward compatibility</dd>
<dt><code>-npu</code>,&#8211;no-plugin-updates</dt>
<dd> Ineffective, only kept for backward compatibility</dd>
<dt><code>-nsu</code>,&#8211;no-snapshot-updates</dt>
<dd> Suppress SNAPSHOT updates</dd>
<dt><code>-o</code>,&#8211;offline</dt>
<dd> Work offline</dd>
<dt><code>-P</code>,&#8211;activate-profiles &lt;arg&gt;</dt>
<dd> Comma-delimited list of profiles to activate</dd>
<dt><code>-pl</code>,&#8211;projects &lt;arg&gt;</dt>
<dd> Comma-delimited list of specified reactor projects to build instead of all projects. A project can be specified by [groupId]:artifactId or by its relative path.</dd>
<dt><code>-q</code>,&#8211;quiet</dt>
<dd> Quiet output &#8211; only show errors</dd>
<dt><code>-rf</code>,&#8211;resume-from &lt;arg&gt;</dt>
<dd> Resume reactor from specified project</dd>
<dt><code>-s</code>,&#8211;settings &lt;arg&gt;</dt>
<dd> Alternate path for the user settings file</dd>
<dt><code>-T</code>,&#8211;threads &lt;arg&gt;</dt>
<dd> Thread count, for instance 2.0C where C is core multiplied</dd>
<dt><code>-t</code>,&#8211;toolchains &lt;arg&gt;</dt>
<dd> Alternate path for the user toolchains file</dd>
<dt><code>-U</code>,&#8211;update-snapshots</dt>
<dd> Forces a check for missing releases and updated snapshots on remote repositories</dd>
<dt><code>-up</code>,&#8211;update-plugins</dt>
<dd> Ineffective, only kept for backward compatibility</dd>
<dt><code>-V</code>,&#8211;show-version</dt>
<dd> Display version information WITHOUT stopping build</dd>
<dt><code>-v</code>,&#8211;version</dt>
<dd> Display version information</dd>
<dt><code>-X</code>,&#8211;debug</dt>
<dd> Produce execution debug output </dd>
</dl>
