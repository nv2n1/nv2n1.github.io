---
title: "bundle-gem2-7(1)"
name: "bundle-gem2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-gem2-7/"
description: "bundle-gem – Generate a project skeleton for creating a rubygem"
---

<p><code>bundle-gem</code> &#8211; Generate a project skeleton for creating a rubygem </p>
<h2>Synopsis</h2>
<p><code>bundle gem</code> <i>GEM_NAME</i> <i>OPTIONS</i></p>
<h2>Description</h2>
<p>Generates a directory named <code>GEM_NAME</code> with a <code>Rakefile</code>, <code>GEM_NAME.gemspec</code>, and other supporting files and directories that can be used to develop a rubygem with that name. </p>
<p> Run <code>rake -T</code> in the resulting project for a list of Rake tasks that can be used to test and publish the gem to rubygems.org. </p>
<p> The generated project skeleton can be customized with OPTIONS, as explained below. Note that these options can also be specified via Bundler&#8217;s global configuration file using the following names:</p>
<dl>
<dt>&bull;</p>
<dd><code>gem.coc</code></p>
<dt>&bull;</p>
<dd><code>gem.mit</code></p>
<dt>&bull;</p>
<dd><code>gem.test</code></p>
<dd></dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;exe</code> or <code>-b</code> or <code>&#8211;bin</code></p>
<dd>Specify that Bundler should create a binary executable (as <code>exe/GEM_NAME</code>) in the generated rubygem project. This binary will also be added to the <code>GEM_NAME.gemspec</code> manifest. This behavior is disabled by default.</p>
<dt><code>&#8211;no-exe</code></p>
<dd>Do not create a binary (overrides <code>&#8211;exe</code> specified in the global config).</p>
<dt><code>&#8211;coc</code></p>
<dd>Add a <code>CODE_OF_CONDUCT.md</code> file to the root of the generated project. If this option is unspecified, an interactive prompt will be displayed and the answer will be saved in Bundler&#8217;s global config for future <code>bundle gem</code> use.</p>
<dt><code>&#8211;no-coc</code></p>
<dd>Do not create a <code>CODE_OF_CONDUCT.md</code> (overrides <code>&#8211;coc</code> specified in the global config).</p>
<dt><code>&#8211;ext</code></p>
<dd>Add boilerplate for C extension code to the generated project. This behavior is disabled by default.</p>
<dt><code>&#8211;no-ext</code></p>
<dd>Do not add C extension code (overrides <code>&#8211;ext</code> specified in the global config).</p>
<dt><code>&#8211;mit</code></p>
<dd>Add an MIT license to a <code>LICENSE.txt</code> file in the root of the generated project. Your name from the global git config is used for the copyright statement. If this option is unspecified, an interactive prompt will be displayed and the answer will be saved in Bundler&#8217;s global config for future <code>bundle gem</code> use.</p>
<dt><code>&#8211;no-mit</code></p>
<dd>Do not create a <code>LICENSE.txt</code> (overrides <code>&#8211;mit</code> specified in the global config).</p>
<dt><code>-t</code>, <code>&#8211;test=minitest</code>, <code>&#8211;test=rspec</code></p>
<dd>Specify the test framework that Bundler should use when generating the project. Acceptable values are <code>minitest</code> and <code>rspec</code>. The <code>GEM_NAME.gemspec</code> will be configured and a skeleton test/spec directory will be created based on this option. If this option is unspecified, an interactive prompt will be displayed and the answer will be saved in Bundler&#8217;s global config for future <code>bundle gem</code> use. If no option is specified, the default testing framework is RSpec.</p>
<dt><code>-e</code>, <code>&#8211;edit[=EDITOR]</code></p>
<dd>Open the resulting GEM_NAME.gemspec in EDITOR, or the default editor if not specified. The default is <code>$BUNDLER_EDITOR</code>, <code>$VISUAL</code>, or <code>$EDITOR</code>.</dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>bundle <a href="/docs/linux/man/1-config/">config</a>(1) <i>bundle-config.1.html</i></p>
<dd></dl>
