---
title: "npm-audit(1)"
name: "npm-audit"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-audit/"
description: "npm-audit – Run a security audit"
---

<h2 class="name">NAME</h2>
<p> <code>npm-audit</code> &#8211; Run a security audit </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre><code>
npm audit[--json | --parseable | --audit - level = (low | moderate | high | critical)] npm audit fix[--force | --package - lock - only | --dry - run] common options : [--production][--only = (dev | prod)]
</code></pre>
</dd></dl>
<h3>Examples</h3>
<p> Scan your project for vulnerabilities and automatically install any compatible updates to vulnerable dependencies: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit fix
</pre>
</dd></dl>
<p> Run <code>audit fix</code> without modifying <code>node_modules</code>, but still updating the pkglock: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit fix --package-lock-only
</pre>
</dd></dl>
<p> Skip updating <code>devDependencies</code>: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit fix --only=prod
</pre>
</dd></dl>
<p> Have <code>audit fix</code> install semver-major updates to toplevel dependencies, not just semver-compatible ones: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit fix --force
</pre>
</dd></dl>
<p> Do a dry run to get an idea of what <code>audit fix</code> will do, and <i>also</i> output install information in JSON format: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit fix --dry-run --json
</pre>
</dd></dl>
<p> Scan your project for vulnerabilities and just show the details, without fixing anything: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit
</pre>
</dd></dl>
<p> Get the detailed audit report in JSON format: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit --json
</pre>
</dd></dl>
<p> Get the detailed audit report in plain text result, separated by tab characters, allowing for future reuse in scripting or command line post processing, like for example, selecting some of the columns printed: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit --parseable
</pre>
</dd></dl>
<p> To parse columns, you can use for example <code>awk</code>, and just print some of them: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit --parseable | awk -F $'	' '{print $1,$4}'
</pre>
</dd></dl>
<p> Fail an audit only if the results include a vulnerability with a level of moderate or higher: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ npm audit --audit-level=moderate
</pre>
</dd></dl>
<h3>Description</h3>
<p> The audit command submits a description of the dependencies configured in your project to your default registry and asks for a report of known vulnerabilities. The report returned includes instructions on how to act on this information. The command will exit with a 0 exit code if no vulnerabilities were found. </p>
<p> You can also have npm automatically fix the vulnerabilities by running <code>npm audit fix</code>. Note that some vulnerabilities cannot be fixed automatically and will require manual intervention or review. Also note that since <code>npm audit fix</code> runs a full-fledged <code>npm install</code> under the hood, all configs that apply to the installer will also apply to <code>npm install</code> &#8212; so things like <code>npm audit fix &#8211;package-lock-only</code> will work as expected. </p>
<p> By default, the audit command will exit with a non-zero code if any vulnerability is found. It may be useful in CI environments to include the <code>&#8211;audit-level</code> parameter to specify the minimum vulnerability level that will cause the command to fail. This option does not filter the report output, it simply changes the command&#8217;s failure threshold.</p>
<h3>Content Submitted</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm_version</dd>
<dt>&bull;</dt>
<dd> node_version</dd>
<dt>&bull;</dt>
<dd> platform</dd>
<dt>&bull;</dt>
<dd> node_env</dd>
<dt>&bull;</dt>
<dd> A scrubbed version of your package-lock.json or npm-shrinkwrap.json </dd>
</dl>
</dl>
<h3>Scrubbing</h3>
<p> In order to ensure that potentially sensitive information is not included in the audit data bundle, some dependencies may have their names (and sometimes versions) replaced with opaque non-reversible identifiers. It is done for the following dependency types:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Any module referencing a scope that is configured for a non-default registry has its name scrubbed. (That is, a scope you did a <code>npm login &#8211;scope=@ourscope</code> for.)</dd>
<dt>&bull;</dt>
<dd> All git dependencies have their names and specifiers scrubbed.</dd>
<dt>&bull;</dt>
<dd> All remote tarball dependencies have their names and specifiers scrubbed.</dd>
<dt>&bull;</dt>
<dd> All local directory and tarball dependencies have their names and specifiers scrubbed. </dd>
</dl>
</dl>
<p> The non-reversible identifiers are a sha256 of a session-specific UUID and the value being replaced, ensuring a consistent value within the payload that is different between runs.</p>
<h3>Exit Code</h3>
<p> The <code>npm audit</code> command will exit with a 0 exit code if no vulnerabilities were found. </p>
<p> If vulnerabilities were found the exit code will depend on the <code>audit-level</code> configuration setting.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help install</dd>
<dt>&bull;</dt>
<dd> npm help package-locks</dd>
<dt>&bull;</dt>
<dd> npm help config </dd>
</dl>
</dl>
<h2>Index</h2>
