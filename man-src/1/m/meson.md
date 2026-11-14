---
title: "meson(1)"
name: "meson"
section: "1"
letter: "m"
url: "/docs/linux/man/1-meson/"
description: "meson – a high productivity build system"
---

<h2 class="name">NAME</h2>
<p> meson &#8211; a high productivity build system </p>
<h2>DESCRIPTION</h2>
<p> Meson is a build system designed to optimize programmer productivity. It aims to do this by providing simple, out-of-the-box support for modern software development tools and practices, such as unit tests, coverage reports, Valgrind, Ccache and the like. </p>
<p> The main Meson executable provides many subcommands to access all the functionality. </p>
<h2>The setup command</h2>
<p> Using Meson is simple and follows the common two-phase process of most build systems. First you run Meson to configure your build: </p>
<p> <code>meson setup [</code> <i>options</i> <code>] [</code> <i>build directory</i> <code>] [</code> <i>source directory</i> <code>]</code> </p>
<p> Note that the build directory must be different from the source directory. Meson does not support building inside the source directory and attempting to do that leads to an error. </p>
<p> After a successful configuration step you can build the source by running the actual build command in the build directory. The default backend of Meson is Ninja, which can be invoked like this. </p>
<p> <code>ninja [</code> <i>target</i> <code>]</code> </p>
<p> You only need to run the Meson command once: when you first configure your build dir. After that you just run the build command. Meson will autodetect changes in your source tree and regenerate all files needed to build the project. </p>
<p> The setup command is the default operation. If no actual command is specified, Meson will assume you meant to do a setup. That means that you can set up a build directory without the setup command like this: </p>
<p> <code>meson [</code> <i>options</i> <code>] [</code> <i>build directory</i> <code>] [</code> <i>source directory</i> <code>]</code> </p>
<h3>options:</h3>
<dl>
<dt><code>&#8211;version</code></p>
<dd> print version number</p>
<dt><code>&#8211;help</code></p>
<dd> print command line help </p>
</dl>
<h2>The configure command</h2>
<p> <code>meson configure</code> provides a way to configure a Meson project from the command line. Its usage is simple: </p>
<p> <code>meson configure [</code> <i>build directory</i> <code>] [</code> <i>options to set</i> <code>]</code> </p>
<p> If build directory is omitted, the current directory is used instead. </p>
<p> If no parameters are set, <code>meson configure</code> will print the value of all build options to the console. </p>
<p> To set values, use the -D command line argument like this. </p>
<p> <code>meson configure -Dopt1=value1 -Dopt2=value2</code> </p>
<h2>The introspect command</h2>
<p> Meson introspect is a command designed to make it simple to integrate with other tools, such as IDEs. The output of this command is in JSON. </p>
<p> <code>meson introspect [</code> <i>build directory</i> <code>] [</code> <i>option</i> <code>]</code> </p>
<p> If build directory is omitted, the current directory is used instead. </p>
<h3>options:</h3>
<dl>
<dt><code>&#8211;targets</code></p>
<dd> print all top level targets (executables, libraries, etc)</p>
<dt><code>&#8211;target-files</code></p>
<dd> print the source files of the given target</p>
<dt><code>&#8211;buildsystem-files</code></p>
<dd> print all files that make up the build system (meson.build, meson_options.txt etc)</p>
<dt><code>&#8211;tests</code></p>
<dd> print all unit tests</p>
<dt><code>&#8211;help</code></p>
<dd> print command line help </p>
</dl>
<h2>The test command</h2>
<p> <code>meson test</code> is a helper tool for running test suites of projects using Meson. The default way of running tests is to invoke the default build command: </p>
<p> <code>ninja [</code> <i>test</i> <code>]</code> </p>
<p> <code>meson test</code> provides a richer set of tools for invoking tests. </p>
<p> <code>meson test</code> automatically rebuilds the necessary targets to run tests when used with the Ninja backend. Upon build failure, <code>meson test</code> will return an exit code of 125. This return code tells <code>git bisect run</code> to skip the current commit. Thus bisecting using git can be done conveniently like this. </p>
<p> <code>git bisect run meson test -C build_dir</code> </p>
<h3>options:</h3>
<dl>
<dt><code>&#8211;repeat</code></p>
<dd> run tests as many times as specified</p>
<dt><code>&#8211;gdb</code></p>
<dd> run tests under gdb</p>
<dt><code>&#8211;list</code></p>
<dd> list all available tests</p>
<dt><code>&#8211;wrapper</code></p>
<dd> invoke all tests via the given wrapper (e.g. valgrind)</p>
<dt><code>-C</code></p>
<dd> Change into the given directory before running tests (must be root of build directory).</p>
<dt><code>&#8211;suite</code></p>
<dd> run tests in this suite</p>
<dt><code>&#8211;no-suite</code></p>
<dd> do not run tests in this suite</p>
<dt><code>&#8211;no-stdsplit</code></p>
<dd> do not split stderr and stdout in test logs</p>
<dt><code>&#8211;benchmark</code></p>
<dd> run benchmarks instead of tests</p>
<dt><code>&#8211;logbase</code></p>
<dd> base of file name to use for writing test logs</p>
<dt><code>&#8211;num-processes</code></p>
<dd> how many parallel processes to use to run tests</p>
<dt><code>&#8211;verbose</code></p>
<dd> do not redirect stdout and stderr</p>
<dt><code>-t</code></p>
<dd> a multiplier to use for test timeout values (usually something like 100 for Valgrind)</p>
<dt><code>&#8211;setup</code></p>
<dd> use the specified test setup </p>
</dl>
<h2>The wrap command</h2>
<p> Wraptool is a helper utility to manage source dependencies using the online wrapdb service. </p>
<p> <code>meson wrap &lt;</code> <i>command</i> <code>&gt; [</code> <i>options</i> <code>]</code> </p>
<p> You should run this command in the top level source directory of your project. </p>
<h3>Commands:</h3>
<dl>
<dt><code>list</code></p>
<dd> list all available projects</p>
<dt><code>search</code></p>
<dd> search projects by name</p>
<dt><code>install</code></p>
<dd> install a project with the given name</p>
<dt><code>update</code></p>
<dd> update the specified project to latest available version</p>
<dt><code>info</code></p>
<dd> show available versions of the specified project</p>
<dt><code>status</code></p>
<dd> show installed and available versions of currently used subprojects </p>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Successful.</p>
<dt><code>1</code></p>
<dd> Usage error, or an error parsing or executing meson.build.</p>
<dt><code>2</code></p>
<dd> Internal error.</p>
<dt><code>125</code></p>
<dd> <code>meson test</code> could not rebuild the required targets.</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://mesonbuild.com/">http://mesonbuild.com/</a> </p>
<p> <a rel="nofollow" href="https://wrapdb.mesonbuild.com/">https://wrapdb.mesonbuild.com/</a> </p>
<h2>Index</h2>
