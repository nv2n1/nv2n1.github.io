---
title: "package-lock-json(5)"
name: "package-lock-json"
section: "5"
letter: "p"
url: "/docs/linux/man/5-package-lock-json/"
description: "package-lock.json – A manifestation of the manifest"
---

<p><code>package-lock.json</code> &#8211; A manifestation of the manifest</p>
<h3>Description</h3>
<p><code>package-lock.json</code> is automatically generated for any operations where npm modifies either the <code>node_modules</code> tree, or <code>package.json</code>. It describes the exact tree that was generated, such that subsequent installs are able to generate identical trees, regardless of intermediate dependency updates. This file is intended to be committed into source repositories, and serves various purposes:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Describe a single representation of a dependency tree such that teammates, deployments, and continuous integration are guaranteed to install exactly the same dependencies.</p>
<dt>&bull;</p>
<dd>Provide a facility for users to &quot;time-travel&quot; to previous states of <code>node_modules</code> without having to commit the directory itself.</p>
<dt>&bull;</p>
<dd>To facilitate greater visibility of tree changes through readable source control diffs.</p>
<dt>&bull;</p>
<dd>And optimize the installation process by allowing npm to skip repeated metadata resolutions for previously-installed packages.  One key detail about <code>package-lock.json</code> is that it cannot be published, and it will be ignored if found in any place other than the toplevel package. It shares a format with npm help npm-shrinkwrap.json, which is essentially the same file, but allows publication. This is not recommended unless deploying a CLI tool or otherwise using the publication process for producing production packages. If both <code>package-lock.json</code> and <code>npm-shrinkwrap.json</code> are present in the root of a package, <code>package-lock.json</code> will be completely ignored.</p>
<h3>File Format</h3>
<h3>name</h3>
<p>The name of the package this is a package-lock for. This must match what&#8217;s in <code>package.json</code>.</p>
<h3>version</h3>
<p>The version of the package this is a package-lock for. This must match what&#8217;s in <code>package.json</code>.</p>
<h3>lockfileVersion</h3>
<p>An integer version, starting at <code>1</code> with the version number of this document whose semantics were used when generating this <code>package-lock.json</code>.</p>
<h3>packageIntegrity</h3>
<p>This is a subresource integrity <i><a rel="nofollow" href="https://w3c.github.io/webappsec/specs/subresourceintegrity/">https://w3c.github.io/webappsec/specs/subresourceintegrity/</a></i> value created from the <code>package.json</code>. No preprocessing of the <code>package.json</code> should be done. Subresource integrity strings can be produced by modules like <code>ssri</code> <i><a rel="nofollow" href="https://www.npmjs.com/package/ssri">https://www.npmjs.com/package/ssri</a></i>.</p>
<h3>preserveSymlinks</h3>
<p>Indicates that the install was done with the environment variable <code>NODE_PRESERVE_SYMLINKS</code> enabled. The installer should insist that the value of this property match that environment variable.</p>
<h3>dependencies</h3>
<p>A mapping of package name to dependency object. Dependency objects have the following properties:</p>
<h3>version</h3>
<p>This is a specifier that uniquely identifies this package and should be usable in fetching a new copy of it.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>bundled dependencies: Regardless of source, this is a version number that is purely for informational purposes.</p>
<dt>&bull;</p>
<dd>registry sources: This is a version number. (eg, <code>1.2.3</code>)</p>
<dt>&bull;</p>
<dd>git sources: This is a git specifier with resolved committish. (eg, <code>git+<a rel="nofollow" href="https://example.com/foo/bar#115311855adb0789a0466714ed48a1499ffea97e">https://example.com/foo/bar#115311855adb0789a0466714ed48a1499ffea97e</a></code>)</p>
<dt>&bull;</p>
<dd>http tarball sources: This is the URL of the tarball. (eg, <code><a rel="nofollow" href="https://example.com/example-1.3.0.tgz">https://example.com/example-1.3.0.tgz</a></code>)</p>
<dt>&bull;</p>
<dd>local tarball sources: This is the file URL of the tarball. (eg <code>file:///opt/storage/example-1.3.0.tgz</code>)</p>
<dt>&bull;</p>
<dd>local link sources: This is the file URL of the link. (eg <code>file:libs/our-module</code>)</dl>
</dl>
<h3>integrity</h3>
<p>This is a Standard Subresource Integrity <i><a rel="nofollow" href="https://w3c.github.io/webappsec/specs/subresourceintegrity/">https://w3c.github.io/webappsec/specs/subresourceintegrity/</a></i> for this resource.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>For bundled dependencies this is not included, regardless of source.</p>
<dt>&bull;</p>
<dd>For registry sources, this is the <code>integrity</code> that the registry provided, or if one wasn&#8217;t provided the SHA1 in <code>shasum</code>.</p>
<dt>&bull;</p>
<dd>For git sources this is the specific commit hash we cloned from.</p>
<dt>&bull;</p>
<dd>For remote tarball sources this is an integrity based on a SHA512 of the file.</p>
<dt>&bull;</p>
<dd>For local tarball sources: This is an integrity field based on the SHA512 of the file.</dl>
</dl>
<h3>resolved</h3>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>For bundled dependencies this is not included, regardless of source.</p>
<dt>&bull;</p>
<dd>For registry sources this is path of the tarball relative to the registry URL. If the tarball URL isn&#8217;t on the same server as the registry URL then this is a complete URL.</dl>
</dl>
<h3>bundled</h3>
<p>If true, this is the bundled dependency and will be installed by the parent module. When installing, this module will be extracted from the parent module during the extract phase, not installed as a separate dependency.</p>
<h3>dev</h3>
<p>If true then this dependency is either a development dependency ONLY of the top level module or a transitive dependency of one. This is false for dependencies that are both a development dependency of the top level and a transitive dependency of a non-development dependency of the top level.</p>
<h3>optional</h3>
<p>If true then this dependency is either an optional dependency ONLY of the top level module or a transitive dependency of one. This is false for dependencies that are both an optional dependency of the top level and a transitive dependency of a non-optional dependency of the top level. All optional dependencies should be included even if they&#8217;re uninstallable on the current platform.</p>
<h3>requires</h3>
<p>This is a mapping of module name to version. This is a list of everything this module requires, regardless of where it will be installed. The version should match via normal matching rules a dependency either in our <code>dependencies</code> or in a level higher than us.</p>
<h3>dependencies</h3>
<p>The dependencies of this dependency, exactly as at the top level.</p>
<h3>See also</h3>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>npm help shrinkwrap</p>
<dt>&bull;</p>
<dd>npm help shrinkwrap.json</p>
<dt>&bull;</p>
<dd>npm help package-locks</p>
<dt>&bull;</p>
<dd>npm help package.json</p>
<dt>&bull;</p>
<dd>npm help install </p>
