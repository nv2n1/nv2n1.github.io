---
title: "gemfile2-7(5)"
name: "gemfile2-7"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gemfile2-7/"
description: "Gemfile – A format for describing gem dependencies for Ruby programs"
---

<p><code>Gemfile</code> &#8211; A format for describing gem dependencies for Ruby programs</p>
<h2>Synopsis</h2>
<p>A <code>Gemfile</code> describes the gem dependencies required to execute associated Ruby code. </p>
<p> Place the <code>Gemfile</code> in the root of the directory containing the associated code. For instance, in a Rails application, place the <code>Gemfile</code> in the same directory as the <code>Rakefile</code>.</p>
<h2>Syntax</h2>
<p>A <code>Gemfile</code> is evaluated as Ruby code, in a context which makes available a number of methods used to describe the gem requirements.</p>
<h2>Global Sources</h2>
<p>At the top of the <code>Gemfile</code>, add a line for the <code>Rubygems</code> source that contains the gems listed in the <code>Gemfile</code>.</p>
<dl>
<dd>
<pre>source &quot;<a rel="nofollow" href="https://rubygems.org">https://rubygems.org</a>&quot;</pre>
<dd></dl>
<p> It is possible, but not recommended as of Bundler 1.7, to add multiple global <code>source</code> lines. Each of these <code>source</code>s <code>MUST</code> be a valid Rubygems repository. </p>
<p> Sources are checked for gems following the heuristics described in <i>SOURCE PRIORITY</i>. If a gem is found in more than one global source, Bundler will print a warning after installing the gem indicating which source was used, and listing the other sources where the gem is available. A specific source can be selected for gems that need to use a non-standard repository, suppressing this warning, by using the <i></i><code>:source</code> option or a <i></i><code>source</code> block.</p>
<h3>Credentials</h3>
<p>Some gem sources require a username and password. Use bundle <a href="/docs/linux/man/1-config/">config</a>(1) <i>bundle-config.1.html</i> to set the username and password for any of the sources that need it. The command must be run once on each computer that will install the Gemfile, but this keeps the credentials from being stored in plain text in version control.</p>
<dl>
<dd>
<pre>bundle config gems.example.com user:password</pre>
<dd></dl>
<p> For some sources, like a company Gemfury account, it may be easier to include the credentials in the Gemfile as part of the source URL.</p>
<dl>
<dd>
<pre>source &quot;<a rel="nofollow" href="https://user:password@gems.example.com">https://user:password@gems.example.com</a>&quot;</pre>
<dd></dl>
<p> Credentials in the source URL will take precedence over credentials set using <code>config</code>.</p>
<h2>Ruby</h2>
<p>If your application requires a specific Ruby version or engine, specify your requirements using the <code>ruby</code> method, with the following arguments. All parameters are <code>OPTIONAL</code> unless otherwise specified.</p>
<h3>VERSION (required)</h3>
<p>The version of Ruby that your application requires. If your application requires an alternate Ruby engine, such as JRuby, Rubinius or TruffleRuby, this should be the Ruby version that the engine is compatible with.</p>
<dl>
<dd>
<pre>ruby &quot;1.9.3&quot;</pre>
<dd></dl>
<h3>Engine</h3>
<p>Each application <i>may</i> specify a Ruby engine. If an engine is specified, an engine version <i>must</i> also be specified. </p>
<p> What exactly is an Engine? &#8211; A Ruby engine is an implementation of the Ruby language.</p>
<dl>
<dt>&bull;</p>
<dd>For background: the reference or original implementation of the Ruby programming language is called Matz&#8217;s Ruby Interpreter <i><a rel="nofollow" href="https://en.wikipedia.org/wiki/Ruby_MRI">https://en.wikipedia.org/wiki/Ruby_MRI</a></i>, or MRI for short. This is named after Ruby creator Yukihiro Matsumoto, also known as Matz. MRI is also known as CRuby, because it is written in C. MRI is the most widely used Ruby engine.</p>
<dt>&bull;</p>
<dd>Other implementations <i><a rel="nofollow" href="https://www.ruby-lang.org/en/about/">https://www.ruby-lang.org/en/about/</a></i> of Ruby exist. Some of the more well-known implementations include Rubinius <i><a rel="nofollow" href="https://rubinius.com/">https://rubinius.com/</a></i>, and JRuby <i><a rel="nofollow" href="http://jruby.org/">http://jruby.org/</a></i>. Rubinius is an alternative implementation of Ruby written in Ruby. JRuby is an implementation of Ruby on the JVM, short for Java Virtual Machine.</p>
<dd></dl>
<h3>Engine Version</h3>
<p>Each application <i>may</i> specify a Ruby engine version. If an engine version is specified, an engine <i>must</i> also be specified. If the engine is &quot;ruby&quot; the engine version specified <i>must</i> match the Ruby version.</p>
<dl>
<dd>
<pre>ruby &quot;1.8.7&quot;, :engine =&gt; &quot;jruby&quot;, :engine_version =&gt; &quot;1.6.7&quot;</pre>
<dd></dl>
<h3>Patchlevel</h3>
<p>Each application <i>may</i> specify a Ruby patchlevel.</p>
<dl>
<dd>
<pre>ruby &quot;2.0.0&quot;, :patchlevel =&gt; &quot;247&quot;</pre>
<dd></dl>
<h2>Gems</h2>
<p>Specify gem requirements using the <code>gem</code> method, with the following arguments. All parameters are <code>OPTIONAL</code> unless otherwise specified.</p>
<h3>NAME (required)</h3>
<p>For each gem requirement, list a single <i>gem</i> line.</p>
<dl>
<dd>
<pre>gem &quot;nokogiri&quot;</pre>
<dd></dl>
<h3>Version</h3>
<p>Each <i>gem</i> <code>MAY</code> have one or more version specifiers.</p>
<dl>
<dd>
<pre>gem &quot;nokogiri&quot;, &quot;&gt;= 1.4.2&quot;
gem &quot;RedCloth&quot;, &quot;&gt;= 4.1.0&quot;, &quot;&lt; 4.2.0&quot;</pre>
<dd></dl>
<h3>Require As</h3>
<p>Each <i>gem</i> <code>MAY</code> specify files that should be used when autorequiring via <code>Bundler.require</code>. You may pass an array with multiple files or <code>true</code> if file you want <code>required</code> has same name as <i>gem</i> or <code>false</code> to prevent any file from being autorequired.</p>
<dl>
<dd>
<pre>gem &quot;redis&quot;, :require =&gt; [&quot;redis/connection/hiredis&quot;, &quot;redis&quot;]
gem &quot;webmock&quot;, :require =&gt; false
gem &quot;byebug&quot;, :require =&gt; true</pre>
<dd></dl>
<p> The argument defaults to the name of the gem. For example, these are identical:</p>
<dl>
<dd>
<pre>gem &quot;nokogiri&quot;
gem &quot;nokogiri&quot;, :require =&gt; &quot;nokogiri&quot;
gem &quot;nokogiri&quot;, :require =&gt; true</pre>
<dd></dl>
<h3>Groups</h3>
<p>Each <i>gem</i> <code>MAY</code> specify membership in one or more groups. Any <i>gem</i> that does not specify membership in any group is placed in the <code>default</code> group.</p>
<dl>
<dd>
<pre>gem &quot;rspec&quot;, :group =&gt; :test
gem &quot;wirble&quot;, :groups =&gt; [:development, :test]</pre>
<dd></dl>
<p> The Bundler runtime allows its two main methods, <code>Bundler.setup</code> and <code>Bundler.require</code>, to limit their impact to particular groups.</p>
<dl>
<dd>
<pre># setup adds gems to Ruby's load path
Bundler.setup # defaults to all groups
require &quot;bundler/setup&quot; # same as Bundler.setup
Bundler.setup(:default) # only set up the _default_ group
Bundler.setup(:test) # only set up the _test_ group (but `not` _default_)
Bundler.setup(:default, :test) # set up the _default_ and _test_ groups, but no others
# require requires all of the gems in the specified groups
Bundler.require # defaults to the _default_ group
Bundler.require(:default) # identical
Bundler.require(:default, :test) # requires the _default_ and _test_ groups
Bundler.require(:test) # requires the _test_ group</pre>
<dd></dl>
<p> The Bundler CLI allows you to specify a list of groups whose gems <code>bundle install</code> should not install with the <code>without</code> configuration. </p>
<p> To specify multiple groups to ignore, specify a list of groups separated by spaces.</p>
<dl>
<dd>
<pre>bundle config set without test
bundle config set without development test</pre>
<dd></dl>
<p> Also, calling <code>Bundler.setup</code> with no parameters, or calling <code>require &quot;bundler/setup&quot;</code> will setup all groups except for the ones you excluded via <code>&#8211;without</code> (since they are not available). </p>
<p> Note that on <code>bundle install</code>, bundler downloads and evaluates all gems, in order to create a single canonical list of all of the required gems and their dependencies. This means that you cannot list different versions of the same gems in different groups. For more details, see Understanding Bundler <i><a rel="nofollow" href="https://bundler.io/rationale.html">https://bundler.io/rationale.html</a></i>.</p>
<h3>Platforms</h3>
<p>If a gem should only be used in a particular platform or set of platforms, you can specify them. Platforms are essentially identical to groups, except that you do not need to use the <code>&#8211;without</code> install-time flag to exclude groups of gems for other platforms. </p>
<p> There are a number of <code>Gemfile</code> platforms:</p>
<dl>
<dt><code>ruby</code></p>
<dd>C Ruby (MRI), Rubinius or TruffleRuby, but <code>NOT</code> Windows</p>
<dt><code>mri</code></p>
<dd>Same as <i>ruby</i>, but only C Ruby (MRI)</p>
<dt><code>mingw</code></p>
<dd>Windows 32 bit &#8216;mingw32&#8217; platform (aka RubyInstaller)</p>
<dt><code>x64_mingw</code></p>
<dd>Windows 64 bit &#8216;mingw32&#8217; platform (aka RubyInstaller x64)</p>
<dt><code>rbx</code></p>
<dd>Rubinius</p>
<dt><code>jruby</code></p>
<dd>JRuby</p>
<dt><code>truffleruby</code></p>
<dd>TruffleRuby</p>
<dt><code>mswin</code></p>
<dd>Windows</dl>
<p> You can restrict further by platform and version for all platforms <i>except</i> for <code>rbx</code>, <code>jruby</code>, <code>truffleruby</code> and <code>mswin</code>. </p>
<p> To specify a version in addition to a platform, append the version number without the delimiter to the platform. For example, to specify that a gem should only be used on platforms with Ruby 2.3, use:</p>
<dl>
<dd>
<pre>ruby_23</pre>
<dd></dl>
<p> The full list of platforms and supported versions includes:</p>
<dl>
<dt><code>ruby</code></p>
<dd>1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6</p>
<dt><code>mri</code></p>
<dd>1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6</p>
<dt><code>mingw</code></p>
<dd>1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6</p>
<dt><code>x64_mingw</code></p>
<dd>2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6</dl>
<p> As with groups, you can specify one or more platforms:</p>
<dl>
<dd>
<pre>gem &quot;weakling&quot;, :platforms =&gt; :jruby
gem &quot;ruby-debug&quot;, :platforms =&gt; :mri_18
gem &quot;nokogiri&quot;, :platforms =&gt; [:mri_18, :jruby]</pre>
<dd></dl>
<p> All operations involving groups (<code>bundle install</code> <i>bundle-install.1.html</i>, <code>Bundler.setup</code>, <code>Bundler.require</code>) behave exactly the same as if any groups not matching the current platform were explicitly excluded.</p>
<h3>Source</h3>
<p>You can select an alternate Rubygems repository for a gem using the &#8216;:source&#8217; option.</p>
<dl>
<dd>
<pre>gem &quot;some_internal_gem&quot;, :source =&gt; &quot;<a rel="nofollow" href="https://gems.example.com">https://gems.example.com</a>&quot;</pre>
<dd></dl>
<p> This forces the gem to be loaded from this source and ignores any global sources declared at the top level of the file. If the gem does not exist in this source, it will not be installed. </p>
<p> Bundler will search for child dependencies of this gem by first looking in the source selected for the parent, but if they are not found there, it will fall back on global sources using the ordering described in <i>SOURCE PRIORITY</i>. </p>
<p> Selecting a specific source repository this way also suppresses the ambiguous gem warning described above in <i>GLOBAL SOURCES (#source)</i>. </p>
<p> Using the <code>:source</code> option for an individual gem will also make that source available as a possible global source for any other gems which do not specify explicit sources. Thus, when adding gems with explicit sources, it is recommended that you also ensure all other gems in the Gemfile are using explicit sources.</p>
<h3>Git</h3>
<p>If necessary, you can specify that a gem is located at a particular git repository using the <code>:git</code> parameter. The repository can be accessed via several protocols:</p>
<dl>
<dt><code>HTTP(S)</code></p>
<dd>gem &quot;rails&quot;, :git =&gt; &quot;<a rel="nofollow" href="https://github.com/rails/rails.git">https://github.com/rails/rails.git</a>&quot;</p>
<dt><code>SSH</code></p>
<dd>gem &quot;rails&quot;, :git =&gt; &quot;git [at] github.com:rails/rails.git&quot;</p>
<dt><code>git</code></p>
<dd>gem &quot;rails&quot;, :git =&gt; &quot;<a href="git://github.com/rails/rails.git">git://github.com/rails/rails.git</a>&quot;</dl>
<p> If using SSH, the user that you use to run <code>bundle install</code> <code>MUST</code> have the appropriate keys available in their <code>$HOME/.ssh</code>. </p>
<p> <code>NOTE</code>: <code>http://</code> and <code>git://</code> URLs should be avoided if at all possible. These protocols are unauthenticated, so a man-in-the-middle attacker can deliver malicious code and compromise your system. HTTPS and SSH are strongly preferred. </p>
<p> The <code>group</code>, <code>platforms</code>, and <code>require</code> options are available and behave exactly the same as they would for a normal gem. </p>
<p> A git repository <code>SHOULD</code> have at least one file, at the root of the directory containing the gem, with the extension <code>.gemspec</code>. This file <code>MUST</code> contain a valid gem specification, as expected by the <code>gem build</code> command. </p>
<p> If a git repository does not have a <code>.gemspec</code>, bundler will attempt to create one, but it will not contain any dependencies, executables, or C extension compilation instructions. As a result, it may fail to properly integrate into your application. </p>
<p> If a git repository does have a <code>.gemspec</code> for the gem you attached it to, a version specifier, if provided, means that the git repository is only valid if the <code>.gemspec</code> specifies a version matching the version specifier. If not, bundler will print a warning.</p>
<dl>
<dd>
<pre>gem &quot;rails&quot;, &quot;2.3.8&quot;, :git =&gt; &quot;<a rel="nofollow" href="https://github.com/rails/rails.git">https://github.com/rails/rails.git</a>&quot;
# bundle install will fail, because the .gemspec in the rails
# repository's master branch specifies version 3.0.0</pre>
<dd></dl>
<p> If a git repository does <code>not</code> have a <code>.gemspec</code> for the gem you attached it to, a version specifier <code>MUST</code> be provided. Bundler will use this version in the simple <code>.gemspec</code> it creates. </p>
<p> Git repositories support a number of additional options.</p>
<dl>
<dt><code>branch</code>, <code>tag</code>, and <code>ref</code></p>
<dd>You <code>MUST</code> only specify at most one of these options. The default is <code>:branch =&gt; &quot;master&quot;</code>. For example:</p>
<dd>gem &quot;rails&quot;, :git =&gt; &quot;<a rel="nofollow" href="https://github.com/rails/rails.git">https://github.com/rails/rails.git</a>&quot;, :branch =&gt; &quot;5-0-stable&quot;</p>
<dd>gem &quot;rails&quot;, :git =&gt; &quot;<a rel="nofollow" href="https://github.com/rails/rails.git">https://github.com/rails/rails.git</a>&quot;, :tag =&gt; &quot;v5.0.0&quot;</p>
<dd>gem &quot;rails&quot;, :git =&gt; &quot;<a rel="nofollow" href="https://github.com/rails/rails.git">https://github.com/rails/rails.git</a>&quot;, :ref =&gt; &quot;4aded&quot;</p>
<dt><code>submodules</code></p>
<dd>For reference, a git submodule <i><a rel="nofollow" href="https://git-scm.com/book/en/v2/Git-Tools-Submodules">https://git-scm.com/book/en/v2/Git-Tools-Submodules</a></i> lets you have another git repository within a subfolder of your repository. Specify <code>:submodules =&gt; true</code> to cause bundler to expand any submodules included in the git repository</dl>
<p> If a git repository contains multiple <code>.gemspecs</code>, each <code>.gemspec</code> represents a gem located at the same place in the file system as the <code>.gemspec</code>.</p>
<dl>
<dd>
<pre>|~rails [git root]
| |-rails.gemspec [rails gem located here]
|~actionpack
| |-actionpack.gemspec [actionpack gem located here]
|~activesupport
| |-activesupport.gemspec [activesupport gem located here]
|...</pre>
<dd></dl>
<p> To install a gem located in a git repository, bundler changes to the directory containing the gemspec, runs <code>gem build name.gemspec</code> and then installs the resulting gem. The <code>gem build</code> command, which comes standard with Rubygems, evaluates the <code>.gemspec</code> in the context of the directory in which it is located.</p>
<h3>Git Source</h3>
<p>A custom git source can be defined via the <code>git_source</code> method. Provide the source&#8217;s name as an argument, and a block which receives a single argument and interpolates it into a string to return the full repo address:</p>
<dl>
<dd>
<pre>git_source(:stash){ |repo_name| &quot;<a rel="nofollow" href="https://stash.corp.acme.pl/#{repo_name}.git">https://stash.corp.acme.pl/#{repo_name}.git</a>&quot; }
gem 'rails', :stash =&gt; 'forks/rails'</pre>
<dd></dl>
<p> In addition, if you wish to choose a specific branch:</p>
<dl>
<dd>
<pre>gem &quot;rails&quot;, :stash =&gt; &quot;forks/rails&quot;, :branch =&gt; &quot;branch_name&quot;</pre>
<dd></dl>
<h3>Github</h3>
<p><code>NOTE</code>: This shorthand should be avoided until Bundler 2.0, since it currently expands to an insecure <code>git://</code> URL. This allows a man-in-the-middle attacker to compromise your system. </p>
<p> If the git repository you want to use is hosted on GitHub and is public, you can use the :github shorthand to specify the github username and repository name (without the trailing &quot;.git&quot;), separated by a slash. If both the username and repository name are the same, you can omit one.</p>
<dl>
<dd>
<pre>gem &quot;rails&quot;, :github =&gt; &quot;rails/rails&quot;
gem &quot;rails&quot;, :github =&gt; &quot;rails&quot;</pre>
<dd></dl>
<p> Are both equivalent to</p>
<dl>
<dd>
<pre>gem &quot;rails&quot;, :git =&gt; &quot;<a href="git://github.com/rails/rails.git">git://github.com/rails/rails.git</a>&quot;</pre>
<dd></dl>
<p> Since the <code>github</code> method is a specialization of <code>git_source</code>, it accepts a <code>:branch</code> named argument.</p>
<h3>Gist</h3>
<p>If the git repository you want to use is hosted as a Github Gist and is public, you can use the :gist shorthand to specify the gist identifier (without the trailing &quot;.git&quot;).</p>
<dl>
<dd>
<pre>gem &quot;the_hatch&quot;, :gist =&gt; &quot;4815162342&quot;</pre>
<dd></dl>
<p> Is equivalent to:</p>
<dl>
<dd>
<pre>gem &quot;the_hatch&quot;, :git =&gt; &quot;<a rel="nofollow" href="https://gist.github.com/4815162342.git">https://gist.github.com/4815162342.git</a>&quot;</pre>
<dd></dl>
<p> Since the <code>gist</code> method is a specialization of <code>git_source</code>, it accepts a <code>:branch</code> named argument.</p>
<h3>Bitbucket</h3>
<p>If the git repository you want to use is hosted on Bitbucket and is public, you can use the :bitbucket shorthand to specify the bitbucket username and repository name (without the trailing &quot;.git&quot;), separated by a slash. If both the username and repository name are the same, you can omit one.</p>
<dl>
<dd>
<pre>gem &quot;rails&quot;, :bitbucket =&gt; &quot;rails/rails&quot;
gem &quot;rails&quot;, :bitbucket =&gt; &quot;rails&quot;</pre>
<dd></dl>
<p> Are both equivalent to</p>
<dl>
<dd>
<pre>gem &quot;rails&quot;, :git =&gt; &quot;<a rel="nofollow" href="https://rails@bitbucket.org/rails/rails.git">https://rails@bitbucket.org/rails/rails.git</a>&quot;</pre>
<dd></dl>
<p> Since the <code>bitbucket</code> method is a specialization of <code>git_source</code>, it accepts a <code>:branch</code> named argument.</p>
<h3>Path</h3>
<p>You can specify that a gem is located in a particular location on the file system. Relative paths are resolved relative to the directory containing the <code>Gemfile</code>. </p>
<p> Similar to the semantics of the <code>:git</code> option, the <code>:path</code> option requires that the directory in question either contains a <code>.gemspec</code> for the gem, or that you specify an explicit version that bundler should use. </p>
<p> Unlike <code>:git</code>, bundler does not compile C extensions for gems specified as paths.</p>
<dl>
<dd>
<pre>gem &quot;rails&quot;, :path =&gt; &quot;vendor/rails&quot;</pre>
<dd></dl>
<p> If you would like to use multiple local gems directly from the filesystem, you can set a global <code>path</code> option to the path containing the gem&#8217;s files. This will automatically load gemspec files from subdirectories.</p>
<dl>
<dd>
<pre>path 'components' do
 gem 'admin_ui'
 gem 'public_ui'
end</pre>
<dd></dl>
<h2>BLOCK FORM OF SOURCE, GIT, PATH, GROUP and PLATFORMS</h2>
<p>The <code>:source</code>, <code>:git</code>, <code>:path</code>, <code>:group</code>, and <code>:platforms</code> options may be applied to a group of gems by using block form.</p>
<dl>
<dd>
<pre>source &quot;<a rel="nofollow" href="https://gems.example.com">https://gems.example.com</a>&quot; do
 gem &quot;some_internal_gem&quot;
 gem &quot;another_internal_gem&quot;
end
git &quot;<a rel="nofollow" href="https://github.com/rails/rails.git">https://github.com/rails/rails.git</a>&quot; do
 gem &quot;activesupport&quot;
 gem &quot;actionpack&quot;
end
platforms :ruby do
 gem &quot;ruby-debug&quot;
 gem &quot;sqlite3&quot;
end
group :development, :optional =&gt; true do
 gem &quot;wirble&quot;
 gem &quot;faker&quot;
end</pre>
<dd></dl>
<p> In the case of the group block form the :optional option can be given to prevent a group from being installed unless listed in the <code>&#8211;with</code> option given to the <code>bundle install</code> command. </p>
<p> In the case of the <code>git</code> block form, the <code>:ref</code>, <code>:branch</code>, <code>:tag</code>, and <code>:submodules</code> options may be passed to the <code>git</code> method, and all gems in the block will inherit those options. </p>
<p> The presence of a <code>source</code> block in a Gemfile also makes that source available as a possible global source for any other gems which do not specify explicit sources. Thus, when defining source blocks, it is recommended that you also ensure all other gems in the Gemfile are using explicit sources, either via source blocks or <code>:source</code> directives on individual gems.</p>
<h2>Install_If</h2>
<p>The <code>install_if</code> method allows gems to be installed based on a proc or lambda. This is especially useful for optional gems that can only be used if certain software is installed or some other conditions are met.</p>
<dl>
<dd>
<pre>install_if -&gt; { RUBY_PLATFORM =~ /darwin/ } do
 gem &quot;pasteboard&quot;
end</pre>
<dd></dl>
<h2>Gemspec</h2>
<p>The <code>.gemspec</code> <i><a rel="nofollow" href="http://guides.rubygems.org/specification-reference/">http://guides.rubygems.org/specification-reference/</a></i> file is where you provide metadata about your gem to Rubygems. Some required Gemspec attributes include the name, description, and homepage of your gem. This is also where you specify the dependencies your gem needs to run. </p>
<p> If you wish to use Bundler to help install dependencies for a gem while it is being developed, use the <code>gemspec</code> method to pull in the dependencies listed in the <code>.gemspec</code> file. </p>
<p> The <code>gemspec</code> method adds any runtime dependencies as gem requirements in the default group. It also adds development dependencies as gem requirements in the <code>development</code> group. Finally, it adds a gem requirement on your project (<code>:path =&gt; &#8216;.&#8217;</code>). In conjunction with <code>Bundler.setup</code>, this allows you to require project files in your test code as you would if the project were installed as a gem; you need not manipulate the load path manually or require project files via relative paths. </p>
<p> The <code>gemspec</code> method supports optional <code>:path</code>, <code>:glob</code>, <code>:name</code>, and <code>:development_group</code> options, which control where bundler looks for the <code>.gemspec</code>, the glob it uses to look for the gemspec (defaults to: &quot;{,<i>,</i>/*}.gemspec&quot;), what named <code>.gemspec</code> it uses (if more than one is present), and which group development dependencies are included in. </p>
<p> When a <code>gemspec</code> dependency encounters version conflicts during resolution, the local version under development will always be selected &#8212; even if there are remote versions that better match other requirements for the <code>gemspec</code> gem.</p>
<h2>Source Priority</h2>
<p>When attempting to locate a gem to satisfy a gem requirement, bundler uses the following priority order:</p>
<dl>
<dt>1.</p>
<dd>The source explicitly attached to the gem (using <code>:source</code>, <code>:path</code>, or <code>:git</code>)</p>
<dt>2.</p>
<dd>For implicit gems (dependencies of explicit gems), any source, git, or path repository declared on the parent. This results in bundler prioritizing the ActiveSupport gem from the Rails git repository over ones from <code>rubygems.org</code></p>
<dt>3.</p>
<dd>The sources specified via global <code>source</code> lines, searching each source in your <code>Gemfile</code> from last added to first added.</p>
<dd></dl>
