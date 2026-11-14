---
title: "pip3(1)"
name: "pip3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pip3/"
description: "pip – A tool for installing and managing Python packages"
---

<h2 class="name">NAME</h2>
<p> pip &#8211; A tool for installing and managing Python packages </p>
<h2>SYNOPSIS</h2>
<p> pip &lt;command&gt; [options] </p>
<p> pip3 &lt;command&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>pip</code> is a Python package installer, recommended for installing Python packages which are not available in the Debian archive. It can work with version control repositories (currently only Git, Mercurial, and Bazaar repositories), logs output extensively, and prevents partial installs by downloading all requirements before starting installation. </p>
<p> On Debian, <code>pip</code> is the command to use when installing packages for Python 2, while <code>pip3</code> is the command to use when installing packages for Python 3.</p>
<h2>COMMANDS</h2>
<p> The command comes before any options. The following commands are recognized:</p>
<dl>
<dt><code>help</code></p>
<dd> Show help for commands.</p>
<dt><code>install</code></p>
<dd> Install packages.</p>
<dt><code>uninstall</code></p>
<dd> Uninstall packages.</p>
<dt><code>freeze</code></p>
<dd> Output installed packages in requirements format.</p>
<dt><code>list</code></p>
<dd> List installed packages.</p>
<dt><code>show</code></p>
<dd> Show information about installed packages.</p>
<dt><code>search</code></p>
<dd> Search PyPI for packages.</p>
<dt><code>wheel</code></p>
<dd> Build wheels from your requirements.</dl>
<h2>GENERAL OPTIONS</h2>
<p> This list is by no means complete, and it only describes options available to all commands. Use <code>pip &lt;command&gt; &#8211;help</code> for more details on command specific options. A few command options are provided below.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Show more detailed command help.</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> Give more output. Option is additive, and can be used up to 3 times.</p>
<dt><code>-V</code>,<code> &#8211;version</code></p>
<dd> Show version and exit.</p>
<dt><code>-q</code>,<code> &#8211;quiet</code></p>
<dd> Give less output.</p>
<dt><code>&#8211;log-file</code><i>&nbsp;&lt;path&gt;</i></p>
<dd> Path to a verbose non-appending log, that only logs failures. This log is active by default at <i>~/.pip/pip.log</i>.</p>
<dt><code>&#8211;log</code><i>&nbsp;&lt;path&gt;</i></p>
<dd> Path to a verbose appending log. This log is inactive by default.</p>
<dt><code>&#8211;proxy</code><i>&nbsp;&lt;proxy&gt;</i></p>
<dd> Specify a proxy in the form <code>[user:passwd@]proxy.server:port</code>.</p>
<dt><code>&#8211;timeout</code><i>&nbsp;&lt;sec&gt;</i></p>
<dd> Set the socket timeout (default 15 seconds).</p>
<dt><code>&#8211;exists-action</code><i>&nbsp;&lt;action&gt;</i></p>
<dd> Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup.</p>
<dt><code>&#8211;cert</code><i>&nbsp;&lt;path&gt;</i></p>
<dd> Path to alternate CA bundle.</dl>
<h2>INSTALL OPTIONS</h2>
<p> <code>pip install</code> installs packages from:</p>
<dl>
<dt>&bull;</p>
<dd> PyPI (a.k.a. The Cheeseshop) and other indexes, using requirements specifiers.</p>
<dt>&bull;</p>
<dd> VCS project urls.</p>
<dt>&bull;</p>
<dd> Local project directories.</p>
<dt>&bull;</p>
<dd> Local or remote source archives</p>
<dt>&bull;</p>
<dd> Local wheel directories (python-pip-whl installs its wheels in /usr/share/ python-wheels and they can be locally installed by pip using &#8211;find-links)</p>
<dt><code>-e</code>,<i>&#8211;editable</i><code>&nbsp;&lt;path/url&gt;</code></p>
<dd> Install a project in editable mode (i.e. setuptools &quot;develop mode&quot;) from a local project path or a VCS url.</p>
<dt><code>-r</code>,<i>&#8211;requirement</i><code>&nbsp;&lt;file&gt;</code></p>
<dd> Install from the given requirements file. This option can be used multiple times.</p>
<dt><code>-b</code>,<i>&#8211;build</i><code>&nbsp;&lt;dir&gt;</code></p>
<dd> Directory to unpack packages into and build in. The default in a virtualenv is &quot;&lt;venv path&gt;/build&quot;. The default for global installs is &quot;&lt;OS temp dir&gt;/pip_build_&lt;username&gt;&quot;.</p>
<dt><code>-t</code>,<i>&#8211;target</i><code>&nbsp;&lt;dir&gt;</code></p>
<dd> Install packages into &lt;dir&gt;.</p>
<dt><code>-d</code>,<i>&#8211;download</i><code>&nbsp;&lt;dir&gt;</code></p>
<dd> Download packages into &lt;dir&gt; instead of installing them, regardless of what&#8217;s already installed.</p>
<dt><code>&#8211;download-cache</code><i>&nbsp;&lt;dir&gt;</i></p>
<dd> Cache downloaded packages in &lt;dir&gt;.</p>
<dt><code>&#8211;src</code><i>&nbsp;&lt;dir&gt;</i></p>
<dd> Directory to check out editable projects into. The default in a virtualenv is &quot;&lt;venv path&gt;/src&quot;. The default for global installs is &quot;&lt;current dir&gt;/src&quot;.</p>
<dt><code>-U</code>,<code> &#8211;upgrade</code></p>
<dd> Upgrade all packages to the newest available version. This process is recursive regardless of whether a dependency is already satisfied.</p>
<dt><code>&#8211;force-reinstall</code></p>
<dd> When upgrading, reinstall all packages even if they are already up-to-date.</p>
<dt><code>-I</code>,<code> &#8211;ignore-installed</code></p>
<dd> Ignore the installed packages (reinstalling instead).</p>
<dt><code>&#8211;no-deps</code></p>
<dd> Don&#8217;t install package dependencies.</p>
<dt><code>&#8211;install-option</code><i>&nbsp;&lt;options&gt;</i></p>
<dd> Extra arguments to be supplied to the setup.py install command (use like &#8211;install-option =&quot;&#8211;install-scripts=/usr/local/bin&quot;). Use multiple &#8211;install-option options to pass multiple options to setup.py install. If you are using an option with a directory path, be sure to use absolute path.</p>
<dt><code>&#8211;global-option</code><i>&nbsp;&lt;options&gt;</i></p>
<dd> Extra global options to be supplied to the setup.py call before the install command.</p>
<dt><code>&#8211;user</code></p>
<dd> Install using the user scheme.</p>
<dt><code>&#8211;egg</code></p>
<dd> Install packages as eggs, not &#8216;flat&#8217;, like pip normally does. This option is not about installing <i>from</i> eggs. (WARNING: Because this option overrides pip&#8217;s normal install logic, requirements files may not behave as expected.)</p>
<dt><code>&#8211;root</code><i>&nbsp;&lt;dir&gt;</i></p>
<dd> Install everything relative to this alternate root directory.</p>
<dt><code>&#8211;compile</code></p>
<dd> Compile py files to pyc.</p>
<dt><code>&#8211;no-compile</code></p>
<dd> Do not compile py files to pyc.</p>
<dt><code>&#8211;no-use-wheel</code></p>
<dd> Do not find and prefer wheel archives when searching indexes and find-links locations.</p>
<dt><code>&#8211;pre</code></p>
<dd> Include pre-release and development versions. By default, pip only finds stable versions.</p>
<dt><code>&#8211;no-clean</code></p>
<dd> Don&#8217;t clean up build directories. </p>
<p> Package Index Options:</p>
<dt><code>-i</code>,<i>&#8211;index-url</i><code>&nbsp;&lt;url&gt;</code></p>
<dd> Base URL of Python Package Index (default <i><a rel="nofollow" href="https://pypi.python.org/simple/">https://pypi.python.org/simple/</a></i>).</p>
<dt><code>&#8211;extra-index-url</code><i>&nbsp;&lt;url&gt;</i></p>
<dd> Extra URLs of package indexes to use in addition to &#8211;index-url.</p>
<dt><code>&#8211;no-index</code></p>
<dd> Ignore package index (only looking at &#8211;find-links URLs instead).</p>
<dt><code>-f</code>,<i>&#8211;find-links</i><code>&nbsp;&lt;url&gt;</code></p>
<dd> If a url or path to an html file, then parse for links to archives. If a local path or <i>file://</i> url that&#8217;s a directory, then look for archives in the directory listing.</p>
<dt><code>&#8211;allow-external</code><i>&nbsp;&lt;package&gt;</i></p>
<dd> Allow the installation of externally hosted files</p>
<dt><code>&#8211;allow-all-external</code></p>
<dd> Allow the installation of all externally hosted files</p>
<dt><code>&#8211;allow-unverified</code><i>&nbsp;&lt;package&gt;</i></p>
<dd> Allow the installation of insecure and unverifiable files</p>
<dt><code>&#8211;process-dependency-links</code></p>
<dd> Enable the processing of dependency links.</dl>
<h2>UNINSTALL OPTIONS</h2>
<p> pip is able to uninstall most installed packages. Known exceptions are:</p>
<dl>
<dt>&bull;</p>
<dd> Pure distutils packages installed with <code>python setup.py install</code>, which leave behind no metadata to determine what files were installed.</p>
<dt>&bull;</p>
<dd> Script wrappers installed by <code>python setup.py develop</code>.</p>
<dt><code>-r</code>,<i>&#8211;requirement</i><code>&nbsp;&lt;file&gt;</code></p>
<dd> Uninstall all the packages listed in the given requirements file. This option can be used multiple times.</p>
<dt><code>-y</code>,<code> &#8211;yes</code></p>
<dd> Don&#8217;t ask for confirmation of uninstall deletions.</dl>
<h2>AUTHORS</h2>
<p> This manual page was originally written by Jeff Licquia &lt;<i>licquia [at] debian.org</i>&gt;, later rewritten by Carl Chenet &lt;<i>chaica [at] debian.org</i>&gt;. It was rewritten again and the source converted to reStructuredText by Barry Warsaw &lt;<i>barry [at] debian.org</i>&gt;. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 3 or any later version published by the Free Software Foundation.</p>
<h2>AUTHOR</h2>
<p> Barry Warsaw &lt;barry [at] debian.org&gt; </p>
<h2>Index</h2>
