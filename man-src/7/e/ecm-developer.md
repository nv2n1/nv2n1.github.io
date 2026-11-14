---
title: "ecm-developer(7)"
name: "ecm-developer"
section: "7"
letter: "e"
url: "/docs/linux/man/7-ecm-developer/"
description: "ecm-developer – ECM Developer Reference"
---

<p>ecm-developer &#8211; ECM Developer Reference</p>
<h2>Writing Modules</h2>
<p>The CMake 3 documentation (and <i><a href="/docs/linux/man/7-cmake-developer/">cmake-developer</a>(7)</i> in particular) has a lot of useful information about writing CMake modules, including a large section devoted to find modules. This guide will only highlight things that are particular to the Extra CMake Modules project. </p>
<p> Most of these are stylistic points. For example, the license header for a module in ECM should look like: </p>
<pre>#=============================================================================
# Copyright 20XX Your Name &lt;your.email [at] example.com&gt;
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the copyright
# notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</pre>
<p>Functions should be used instead of macros unless there is a good reason not to (and that reason should be noted in a comment), and lowercase should be used for macros, functions and commands. </p>
<p> 4 spaces is the generally-recommended indent, although there are several files that use 2 spaces; consistency within a file is more important than consistency across files. </p>
<p> If in doubt, look at how other modules in Extra CMake Modules are written, and follow the same pattern.</p>
<h3>Find Modules</h3>
<p>A good template for find module documentation is: </p>
<pre>#.rst:
# FindFoo
# -------
#
# Finds the Foo library.
#
# This will define the following variables:
#
# ``Foo_FOUND``
# True if (the requested version of) Foo is available
# ``Foo_VERSION``
# The version of Foo, if it is found
# ``Foo_LIBRARIES``
# This can be passed to target_link_libraries() instead of the ``Foo::Foo``
# target
# ``Foo_INCLUDE_DIRS``
# This should be passed to target_include_directories() if the target is not
# used for linking
# ``Foo_DEFINITIONS``
# This should be passed to target_compile_options() if the target is not
# used for linking
#
# If ``Foo_FOUND`` is TRUE, it will also define the following imported target:
#
# ``Foo::Foo``
# The Foo library
#
# In general we recommend using the imported target, as it is easier to use.
# Bear in mind, however, that if the target is in the link interface of an
# exported library, it must be made available by the package config file.</pre>
<p>Note the use of definition lists for the variables. </p>
<p> Because of the <code>ECMUseFindModules</code> module, projects may easily make local copies of find modules, and may install those copies with their own CMake project config files. For this reason, find modules should include the full BSD 3-clause license: </p>
<pre>#=============================================================================
# Copyright 20XX Your Name &lt;your.email [at] example.com&gt;
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the copyright
# notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#=============================================================================</pre>
<p>Find modules should always provide imported targets in addition to the traditional variables (like <code>Foo_LIBRARIES</code>, etc). </p>
<p> Unlike find modules shipped with CMake, if the module requires a specific CMake version it is not enough to warn when the minimum required version is not high enough: you should also produce an error when the actual CMake version being used is not high enough. This can be done with: </p>
<pre>if(CMAKE_VERSION VERSION_LESS 2.8.12)
 message(FATAL_ERROR &quot;CMake 2.8.12 is required by FindFoo.cmake&quot;)
endif()
if(CMAKE_MINIMUM_REQUIRED_VERSION VERSION_LESS 2.8.12)
 message(AUTHOR_WARNING &quot;Your project should require at least CMake 2.8.12 to use FindFoo.cmake&quot;)
endif()</pre>
<p>The <code>ECMFindModuleHelpers</code> module has several useful functions and macros. For example, it allows you to replace the above version check with: </p>
<pre>ecm_find_package_version_check(Foo)</pre>
<h3>Components</h3>
<p>Using <code>ECMFindModuleHelpers</code>, creating a find module for a library with several inter-dependent components is reasonably straightforward. After the documentation, you need to include the module and do the usual version check: </p>
<pre>include(ECMFindModuleHelpers)
ecm_find_package_version_check(Foo)</pre>
<p>The important macros are <code>ecm_find_package_parse_components</code> and <code>ecm_find_package_handle_library_components</code>. These take a list of components, and query other variables you provide to find out the information they require. The documentation for <code>ECMFindModuleHelpers</code> provides more information, but a simple setup might look like: </p>
<pre>set(Foo_known_components Bar Baz)
set(Foo_Bar_pkg_config &quot;foo-bar&quot;)
set(Foo_Bar_lib &quot;bar&quot;)
set(Foo_Bar_header &quot;foo/bar.h&quot;)
set(Foo_Bar_pkg_config &quot;foo-baz&quot;)
set(Foo_Baz_lib &quot;baz&quot;)
set(Foo_Baz_header &quot;foo/baz.h&quot;)</pre>
<p>If <code>Baz</code> depends on <code>Bar</code>, for example, you can specify this with </p>
<pre>set(Foo_Baz_component_deps &quot;Bar&quot;)</pre>
<p>Then call the macros: </p>
<pre>ecm_find_package_parse_components(Foo
 RESULT_VAR Foo_components
 KNOWN_COMPONENTS ${Foo_known_components}
)
ecm_find_package_handle_library_components(Foo
 COMPONENTS ${Foo_components}
)</pre>
<p>Of course, if your components need unusual handling, you may want to replace <code>ecm_find_package_handle_library_components</code> with, for example, a <code>foreach</code> loop over the components (the body of which should implement most of what a normal find module does, including setting <code>Foo_&lt;component&gt;_FOUND</code>). </p>
<p> At this point, you should set <code>Foo_VERSION</code> using whatever information you have available (such as from parsing header files). Note that <code>ecm_find_package_handle_library_components</code> will set it to the version reported by pkg-config of the first component found, but this depends on the presence of pkg-config files, and the version of a component may not be the same as the version of the whole package. After that, finish off with </p>
<pre>include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Foo
 FOUND_VAR
 Foo_FOUND
 REQUIRED_VARS
 Foo_LIBRARIES
 VERSION_VAR
 Foo_VERSION
 HANDLE_COMPONENTS
)
include(FeatureSummary)
set_package_properties(Foo PROPERTIES
 URL &quot;<a rel="nofollow" href="http://www.foo.example.com/">http://www.foo.example.com/</a>&quot;
 DESCRIPTION &quot;A library for doing useful things&quot;)</pre>
<h2>Submitting Modules</h2>
<p>Proposed new modules should be submitted using the <i>KDE Review Board instance</i>, and be assigned to the <code>buildsystem</code> and <code>extracmakemodules</code> groups. You should be able to point to two separate projects that will make use of the module. </p>
<p> The mailing list can be found at <i><a rel="nofollow" href="https://mail.kde.org/mailman/listinfo/kde-buildsystem">https://mail.kde.org/mailman/listinfo/kde-buildsystem</a></i>.</p>
<h2>Copyright</h2>
<p>KDE Developers</p>
