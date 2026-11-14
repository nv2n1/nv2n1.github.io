---
title: "cmake3-developer(7)"
name: "cmake3-developer"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-developer/"
description: "cmake-developer – CMake Developer Reference"
---

<p>cmake-developer &#8211; CMake Developer Reference</p>
<h2>Introduction</h2>
<p>This manual is intended for reference by developers modifying the CMake source tree itself.</p>
<h2>Permitted C++ Subset</h2>
<p>CMake is required to build with ancient C++ compilers and standard library implementations. Some common C++ constructs may not be used in CMake in order to build with such toolchains.</p>
<h3>std::auto_ptr</h3>
<p>Some implementations have a <code>std::auto_ptr</code> which can not be used as a return value from a function. <code>std::auto_ptr</code> may not be used. Use <code>cmsys::auto_ptr</code> instead.</p>
<h3>size_t</h3>
<p>Various implementations have differing implementation of <code>size_t</code>. When assigning the result of <code>.size()</code> on a container for example, the result should be assigned to <code>size_t</code> not to <code>std::size_t</code>, <code>unsigned int</code> or similar types.</p>
<h2>Adding Compile Features</h2>
<p>CMake reports an error if a compiler whose features are known does not report support for a particular requested feature. A compiler is considered to have known features if it reports support for at least one feature. </p>
<p> When adding a new compile feature to CMake, it is therefore necessary to list support for the feature for all CompilerIds which already have one or more feature supported, if the new feature is available for any version of the compiler. </p>
<p> When adding the first supported feature to a particular CompilerId, it is necessary to list support for all features known to cmake (See <code>CMAKE_C_COMPILE_FEATURES</code> and <code>CMAKE_CXX_COMPILE_FEATURES</code> as appropriate), where available for the compiler. Ensure that the <code>CMAKE_&lt;LANG&gt;_STANDARD_DEFAULT</code> is set to the computed internal variable <code>CMAKE_&lt;LANG&gt;_STANDARD_COMPUTED_DEFAULT</code> for compiler versions which should be supported. </p>
<p> It is sensible to record the features for the most recent version of a particular CompilerId first, and then work backwards. It is sensible to try to create a continuous range of versions of feature releases of the compiler. Gaps in the range indicate incorrect features recorded for intermediate releases. </p>
<p> Generally, features are made available for a particular version if the compiler vendor documents availability of the feature with that version. Note that sometimes partially implemented features appear to be functional in previous releases (such as <code>cxx_constexpr</code> in GNU 4.6, though availability is documented in GNU 4.7), and sometimes compiler vendors document availability of features, though supporting infrastructure is not available (such as <code>__has_feature(cxx_generic_lambdas)</code> indicating non-availability in Clang 3.4, though it is documented as available, and fixed in Clang 3.5). Similar cases for other compilers and versions need to be investigated when extending CMake to support them. </p>
<p> When a vendor releases a new version of a known compiler which supports a previously unsupported feature, and there are already known features for that compiler, the feature should be listed as supported in CMake for that version of the compiler as soon as reasonably possible. </p>
<p> Standard-specific/compiler-specific variables such <code>CMAKE_CXX98_COMPILE_FEATURES</code> are deliberately not documented. They only exist for the compiler-specific implementation of adding the <code>-std</code> compile flag for compilers which need that.</p>
<h2>Help</h2>
<p>The <code>Help</code> directory contains CMake help manual source files. They are written using the <i>reStructuredText</i> markup syntax and processed by <i>Sphinx</i> to generate the CMake help manuals.</p>
<h3>Markup Constructs</h3>
<p>In addition to using Sphinx to generate the CMake help manuals, we also use a C++-implemented document processor to print documents for the <code>&#8211;help-*</code> command-line help options. It supports a subset of reStructuredText markup. When authoring or modifying documents, please verify that the command-line help looks good in addition to the Sphinx-generated html and man pages. </p>
<p> The command-line help processor supports the following constructs defined by reStructuredText, Sphinx, and a CMake extension to Sphinx.</p>
<dl>
<dt><code>CMake Domain directives</code></p>
<dd>Directives defined in the <i>CMake Domain</i> for defining CMake documentation objects are printed in command-line help output as if the lines were normal paragraph text with interpretation.</p>
<dt><code>CMake Domain interpreted text roles</code></p>
<dd>Interpreted text roles defined in the <i>CMake Domain</i> for cross-referencing CMake documentation objects are replaced by their link text in command-line help output. Other roles are printed literally and not processed.</p>
<dt><code>code-block</code> directive</p>
<dd>Add a literal code block without interpretation. The command-line help processor prints the block content without the leading directive line and with common indentation replaced by one space.</p>
<dt><code>include</code> directive</p>
<dd>Include another document source file. The command-line help processor prints the included document inline with the referencing document.</p>
<dt><code>literal block after ::</code></p>
<dd>A paragraph ending in <code>::</code> followed by a blank line treats the following indented block as literal text without interpretation. The command-line help processor prints the <code>::</code> literally and prints the block content with common indentation replaced by one space.</p>
<dt><code>note</code> directive</p>
<dd>Call out a side note. The command-line help processor prints the block content as if the lines were normal paragraph text with interpretation.</p>
<dt><code>parsed-literal</code> directive</p>
<dd>Add a literal block with markup interpretation. The command-line help processor prints the block content without the leading directive line and with common indentation replaced by one space.</p>
<dt><code>productionlist</code> directive</p>
<dd>Render context-free grammar productions. The command-line help processor prints the block content as if the lines were normal paragraph text with interpretation.</p>
<dt><code>replace</code> directive</p>
<dd>Define a <code>|substitution|</code> replacement. The command-line help processor requires a substitution replacement to be defined before it is referenced.</p>
<dt><code>|substitution|</code> reference</p>
<dd>Reference a substitution replacement previously defined by the <code>replace</code> directive. The command-line help processor performs the substitution and replaces all newlines in the replacement text with spaces.</p>
<dt><code>toctree</code> directive</p>
<dd>Include other document sources in the Table-of-Contents document tree. The command-line help processor prints the referenced documents inline as part of the referencing document. </p>
<p> Inline markup constructs not listed above are printed literally in the command-line help output. We prefer to use inline markup constructs that look correct in source form, so avoid use of \-escapes in favor of inline literals when possible. </p>
<p> Explicit markup blocks not matching directives listed above are removed from command-line help output. Do not use them, except for plain <code>..</code> comments that are removed by Sphinx too. </p>
<p> Note that nested indentation of blocks is not recognized by the command-line help processor. Therefore:</p>
<dt>&bull;</p>
<dd>Explicit markup blocks are recognized only when not indented inside other blocks.</p>
<dt>&bull;</p>
<dd>Literal blocks after paragraphs ending in <code>::</code> but not at the top indentation level may consume all indented lines following them. </p>
<p> Try to avoid these cases in practice.</dl>
<h3>CMake Domain</h3>
<p>CMake adds a <i>Sphinx Domain</i> called <code>cmake</code>, also called the &quot;CMake Domain&quot;. It defines several &quot;object&quot; types for CMake documentation:</p>
<dl>
<dt><code>command</code></p>
<dd>A CMake language command.</p>
<dt><code>generator</code></p>
<dd>A CMake native build system generator. See the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> command-line tool&#8217;s <code>-G</code> option.</p>
<dt><code>manual</code></p>
<dd>A CMake manual page, like this <i><a href="/docs/linux/man/7-cmake3-developer/">cmake3-developer</a>(7)</i> manual.</p>
<dt><code>module</code></p>
<dd>A CMake module. See the <code><a href="/docs/linux/man/7-cmake3-modules/">cmake3-modules</a>(7)</code> manual and the <code>include()</code> command.</p>
<dt><code>policy</code></p>
<dd>A CMake policy. See the <code><a href="/docs/linux/man/7-cmake3-policies/">cmake3-policies</a>(7)</code> manual and the <code>cmake_policy()</code> command.</p>
<dt><code>prop_cache, prop_dir, prop_gbl, prop_sf, prop_inst, prop_test, prop_tgt</code></p>
<dd>A CMake cache, directory, global, source file, installed file, test, or target property, respectively. See the <code><a href="/docs/linux/man/7-cmake3-properties/">cmake3-properties</a>(7)</code> manual and the <code>set_property()</code> command.</p>
<dt><code>variable</code></p>
<dd>A CMake language variable. See the <code><a href="/docs/linux/man/7-cmake3-variables/">cmake3-variables</a>(7)</code> manual and the <code>set()</code> command. </p>
<p> Documentation objects in the CMake Domain come from two sources. First, the CMake extension to Sphinx transforms every document named with the form <code>Help/&lt;type&gt;/&lt;file-name&gt;.rst</code> to a domain object with type <code>&lt;type&gt;</code>. The object name is extracted from the document title, which is expected to be of the form: </p>
<pre>&lt;object-name&gt;
-------------</pre>
<p>and to appear at or near the top of the <code>.rst</code> file before any other lines starting in a letter, digit, or <code>&lt;</code>. If no such title appears literally in the <code>.rst</code> file, the object name is the <code>&lt;file-name&gt;</code>. If a title does appear, it is expected that <code>&lt;file-name&gt;</code> is equal to <code>&lt;object-name&gt;</code> with any <code>&lt;</code> and <code>&gt;</code> characters removed. </p>
<p> Second, the CMake Domain provides directives to define objects inside other documents: </p>
<pre>.. command:: &lt;command-name&gt;
 This indented block documents &lt;command-name&gt;.
.. variable:: &lt;variable-name&gt;
 This indented block documents &lt;variable-name&gt;.</pre>
<p>Object types for which no directive is available must be defined using the first approach above.</dl>
<h3>Cross-References</h3>
<p>Sphinx uses reStructuredText interpreted text roles to provide cross-reference syntax. The <i>CMake Domain</i> provides for each domain object type a role of the same name to cross-reference it. CMake Domain roles are inline markup of the forms: </p>
<pre>:type:`name`
:type:`text &lt;name&gt;`</pre>
<p>where <code>type</code> is the domain object type and <code>name</code> is the domain object name. In the first form the link text will be <code>name</code> (or <code>name()</code> if the type is <code>command</code>) and in the second form the link text will be the explicit <code>text</code>. For example, the code: </p>
<pre>* The :command:`list` command.
* The :command:`list(APPEND)` sub-command.
* The :command:`list() command &lt;list&gt;`.
* The :command:`list(APPEND) sub-command &lt;list&gt;`.
* The :variable:`CMAKE_VERSION` variable.
* The :prop_tgt:`OUTPUT_NAME_&lt;CONFIG&gt;` target property.</pre>
<p>produces:</p>
<dl>
<dt>&bull;</p>
<dd>The <code>list()</code> command.</p>
<dt>&bull;</p>
<dd>The <code>list(APPEND)</code> sub-command.</p>
<dt>&bull;</p>
<dd>The <code>list() command</code>.</p>
<dt>&bull;</p>
<dd>The <code>list(APPEND) sub-command</code>.</p>
<dt>&bull;</p>
<dd>The <code>CMAKE_VERSION</code> variable.</p>
<dt>&bull;</p>
<dd>The <code>OUTPUT_NAME_&lt;CONFIG&gt;</code> target property. </p>
<p> Note that CMake Domain roles differ from Sphinx and reStructuredText convention in that the form <code>a&lt;b&gt;</code>, without a space preceding <code>&lt;</code>, is interpreted as a name instead of link text with an explicit target. This is necessary because we use <code>&lt;placeholders&gt;</code> frequently in object names like <code>OUTPUT_NAME_&lt;CONFIG&gt;</code>. The form <code>a &lt;b&gt;</code>, with a space preceding <code>&lt;</code>, is still interpreted as a link text with an explicit target.</dl>
<h3>Style</h3>
<h3>Style: Section Headers</h3>
<p>When marking section titles, make the section decoration line as long as the title text. Use only a line below the title, not above. For example: </p>
<pre>Title Text
----------</pre>
<p>Capitalize the first letter of each non-minor word in the title. </p>
<p> The section header underline character hierarchy is</p>
<dl>
<dt>&bull;</p>
<dd><code>#</code>: Manual group (part) in the master document</p>
<dt>&bull;</p>
<dd><code>*</code>: Manual (chapter) title</p>
<dt>&bull;</p>
<dd><code>=</code>: Section within a manual</p>
<dt>&bull;</p>
<dd><code>&#8211;</code>: Subsection or <i>CMake Domain</i> object document title</p>
<dt>&bull;</p>
<dd><code>^</code>: Subsubsection or <i>CMake Domain</i> object document section</p>
<dt>&bull;</p>
<dd><code>&quot;</code>: Paragraph or <i>CMake Domain</i> object document subsection</dl>
<h3>Style: Whitespace</h3>
<p>Use two spaces for indentation. Use two spaces between sentences in prose.</p>
<h3>Style: Line Length</h3>
<p>Prefer to restrict the width of lines to 75-80 columns. This is not a hard restriction, but writing new paragraphs wrapped at 75 columns allows space for adding minor content without significant re-wrapping of content.</p>
<h3>Style: Prose</h3>
<p>Use American English spellings in prose.</p>
<h3>Style: Starting Literal Blocks</h3>
<p>Prefer to mark the start of literal blocks with <code>::</code> at the end of the preceding paragraph. In cases where the following block gets a <code>code-block</code> marker, put a single <code>:</code> at the end of the preceding paragraph.</p>
<h3>Style: CMake Command Signatures</h3>
<p>Command signatures should be marked up as plain literal blocks, not as cmake <code>code-blocks</code>. </p>
<p> Signatures are separated from preceding content by a section header. That is, use: </p>
<pre>... preceding paragraph.
Normal Libraries
^^^^^^^^^^^^^^^^
::
 add_library(&lt;lib&gt; ...)
This signature is used for ...</pre>
<p>Signatures of commands should wrap optional parts with square brackets, and should mark list of optional arguments with an ellipsis (<code>&#8230;</code>). Elements of the signature which are specified by the user should be specified with angle brackets, and may be referred to in prose using <code>inline-literal</code> syntax.</p>
<h3>Style: Boolean Constants</h3>
<p>Use &quot;<code>OFF</code>&quot; and &quot;<code>ON</code>&quot; for boolean values which can be modified by the user, such as <code>POSITION_INDEPENDENT_CODE</code>. Such properties may be &quot;enabled&quot; and &quot;disabled&quot;. Use &quot;<code>True</code>&quot; and &quot;<code>False</code>&quot; for inherent values which can&#8217;t be modified after being set, such as the <code>IMPORTED</code> property of a build target.</p>
<h3>Style: Inline Literals</h3>
<p>Mark up references to keywords in signatures, file names, and other technical terms with <code>inline-literal</code> syntax, for example: </p>
<pre>If ``WIN32`` is used with :command:`add_executable`, the
:prop_tgt:`WIN32_EXECUTABLE` target property is enabled. That command
creates the file ``&lt;name&gt;.exe`` on Windows.</pre>
<h3>Style: Cross-References</h3>
<p>Mark up linkable references as links, including repeats. An alternative, which is used by wikipedia (<i><a rel="nofollow" href="http://en.wikipedia.org/wiki/WP:REPEATLINK">http://en.wikipedia.org/wiki/WP:REPEATLINK</a></i>), is to link to a reference only once per article. That style is not used in CMake documentation.</p>
<h3>Style: Referencing CMake Concepts</h3>
<p>If referring to a concept which corresponds to a property, and that concept is described in a high-level manual, prefer to link to the manual section instead of the property. For example: </p>
<pre>This command creates an :ref:`Imported Target &lt;Imported Targets&gt;`.</pre>
<p>instead of: </p>
<pre>This command creates an :prop_tgt:`IMPORTED` target.</pre>
<p>The latter should be used only when referring specifically to the property. </p>
<p> References to manual sections are not automatically created by creating a section, but code such as: </p>
<pre>.. _`Imported Targets`:</pre>
<p>creates a suitable anchor. Use an anchor name which matches the name of the corresponding section. Refer to the anchor using a cross-reference with specified text. </p>
<p> Imported Targets need the <code>IMPORTED</code> term marked up with care in particular because the term may refer to a command keyword (<code>IMPORTED</code>), a target property (<code>IMPORTED</code>), or a concept (<i>Imported Targets</i>). </p>
<p> Where a property, command or variable is related conceptually to others, by for example, being related to the buildsystem description, generator expressions or Qt, each relevant property, command or variable should link to the primary manual, which provides high-level information. Only particular information relating to the command should be in the documentation of the command.</p>
<h3>Style: Referencing CMake Domain Objects</h3>
<p>When referring to <i>CMake Domain</i> objects such as properties, variables, commands etc, prefer to link to the target object and follow that with the type of object it is. For example: </p>
<pre>Set the :prop_tgt:`AUTOMOC` target property to ``ON``.</pre>
<p>Instead of </p>
<pre>Set the target property :prop_tgt:`AUTOMOC` to ``ON``.</pre>
<p>The <code>policy</code> directive is an exception, and the type us usually referred to before the link: </p>
<pre>If policy :prop_tgt:`CMP0022` is set to ``NEW`` the behavior is ...</pre>
<p>However, markup self-references with <code>inline-literal</code> syntax. For example, within the <code>add_executable()</code> command documentation, use </p>
<pre>``add_executable``</pre>
<p>not </p>
<pre>:command:`add_executable`</pre>
<p>which is used elsewhere.</p>
<h2>Modules</h2>
<p>The <code>Modules</code> directory contains CMake-language <code>.cmake</code> module files.</p>
<h3>Module Documentation</h3>
<p>To document CMake module <code>Modules/&lt;module-name&gt;.cmake</code>, modify <code>Help/manual/cmake-modules.7.rst</code> to reference the module in the <code>toctree</code> directive, in sorted order, as: </p>
<pre>/module/&lt;module-name&gt;</pre>
<p>Then add the module document file <code>Help/module/&lt;module-name&gt;.rst</code> containing just the line: </p>
<pre>.. cmake-module:: ../../Modules/&lt;module-name&gt;.cmake</pre>
<p>The <code>cmake-module</code> directive will scan the module file to extract reStructuredText markup from comment blocks that start in <code>.rst:</code>. Add to the top of <code>Modules/&lt;module-name&gt;.cmake</code> a <i>Line Comment</i> block of the form: </p>
<pre>#.rst:
# &lt;module-name&gt;
# -------------
#
# &lt;reStructuredText documentation of module&gt;</pre>
<p>or a <i>Bracket Comment</i> of the form: </p>
<pre>#[[.rst:
&lt;module-name&gt;
-------------
&lt;reStructuredText documentation of module&gt;
#]]</pre>
<p>Any number of <code>=</code> may be used in the opening and closing brackets as long as they match. Content on the line containing the closing bracket is excluded if and only if the line starts in <code>#</code>. </p>
<p> Additional such <code>.rst:</code> comments may appear anywhere in the module file. All such comments must start with <code>#</code> in the first column. </p>
<p> For example, a <code>Modules/Findxxx.cmake</code> module may contain: </p>
<pre>#.rst:
# FindXxx
# -------
#
# This is a cool module.
# This module does really cool stuff.
# It can do even more than you think.
#
# It even needs two paragraphs to tell you about it.
# And it defines the following variables:
#
# * VAR_COOL: this is great isn't it?
# * VAR_REALLY_COOL: cool right?
&lt;code&gt;
#[========================================[.rst:
.. command:: xxx_do_something
 This command does something for Xxx::
 xxx_do_something(some arguments)
#]========================================]
macro(xxx_do_something)
 &lt;code&gt;
endmacro()</pre>
<p>After the top documentation block, leave a <i>BLANK</i> line, and then add a copyright and licence notice block like this one (change only the year range and name) </p>
<pre>#=============================================================================
# Copyright 2009-2011 Your Name
#
# Distributed under the OSI-approved BSD License (the &quot;License&quot;);
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distribute this file outside of CMake, substitute the full
# License text for the above reference.)</pre>
<p>Test the documentation formatting by running <code>cmake3 &#8211;help-module &lt;module-name&gt;</code>, and also by enabling the <code>SPHINX_HTML</code> and <code>SPHINX_MAN</code> options to build the documentation. Edit the comments until generated documentation looks satisfactory. To have a .cmake file in this directory NOT show up in the modules documentation, simply leave out the <code>Help/module/&lt;module-name&gt;.rst</code> file and the <code>Help/manual/cmake-modules.7.rst</code> toctree entry.</p>
<h3>Find Modules</h3>
<p>A &quot;find module&quot; is a <code>Modules/Find&lt;package&gt;.cmake</code> file to be loaded by the <code>find_package()</code> command when invoked for <code>&lt;package&gt;</code>. </p>
<p> The primary task of a find module is to determine whether a package exists on the system, set the <code>&lt;package&gt;_FOUND</code> variable to reflect this and provide any variables, macros and imported targets required to use the package. A find module is useful in cases where an upstream library does not provide a <i>config file package</i>. </p>
<p> The traditional approach is to use variables for everything, including libraries and executables: see the <i>Standard Variable Names</i> section below. This is what most of the existing find modules provided by CMake do. </p>
<p> The more modern approach is to behave as much like <i>config file packages</i> files as possible, by providing <i>imported target</i>. This has the advantage of propagating <i>Target Usage Requirements</i> to consumers. </p>
<p> In either case (or even when providing both variables and imported targets), find modules should provide backwards compatibility with old versions that had the same name. </p>
<p> A FindFoo.cmake module will typically be loaded by the command: </p>
<pre>find_package(Foo [major[.minor[.patch[.tweak]]]]
 [EXACT] [QUIET] [REQUIRED]
 [[COMPONENTS] [components...]]
 [OPTIONAL_COMPONENTS components...]
 [NO_POLICY_SCOPE])</pre>
<p>See the <code>find_package()</code> documentation for details on what variables are set for the find module. Most of these are dealt with by using <code>FindPackageHandleStandardArgs</code>. </p>
<p> Briefly, the module should only locate versions of the package compatible with the requested version, as described by the <code>Foo_FIND_VERSION</code> family of variables. If <code>Foo_FIND_QUIETLY</code> is set to true, it should avoid printing messages, including anything complaining about the package not being found. If <code>Foo_FIND_REQUIRED</code> is set to true, the module should issue a <code>FATAL_ERROR</code> if the package cannot be found. If neither are set to true, it should print a non-fatal message if it cannot find the package. </p>
<p> Packages that find multiple semi-independent parts (like bundles of libraries) should search for the components listed in <code>Foo_FIND_COMPONENTS</code> if it is set , and only set <code>Foo_FOUND</code> to true if for each searched-for component <code>&lt;c&gt;</code> that was not found, <code>Foo_FIND_REQUIRED_&lt;c&gt;</code> is not set to true. The <code>HANDLE_COMPONENTS</code> argument of <code>find_package_handle_standard_args()</code> can be used to implement this. </p>
<p> If <code>Foo_FIND_COMPONENTS</code> is not set, which modules are searched for and required is up to the find module, but should be documented. </p>
<p> For internal implementation, it is a generally accepted convention that variables starting with underscore are for temporary use only. </p>
<p> Like all modules, find modules should be properly documented. To add a module to the CMake documentation, follow the steps in the <i>Module Documentation</i> section above.</p>
<h3>Standard Variable Names</h3>
<p>For a <code>FindXxx.cmake</code> module that takes the approach of setting variables (either instead of or in addition to creating imported targets), the following variable names should be used to keep things consistent between find modules. Note that all variables start with <code>Xxx_</code> to make sure they do not interfere with other find modules; the same consideration applies to macros, functions and imported targets.</p>
<dl>
<dt><code>Xxx_INCLUDE_DIRS</code></p>
<dd>The final set of include directories listed in one variable for use by client code. This should not be a cache entry.</p>
<dt><code>Xxx_LIBRARIES</code></p>
<dd>The libraries to link against to use Xxx. These should include full paths. This should not be a cache entry.</p>
<dt><code>Xxx_DEFINITIONS</code></p>
<dd>Definitions to use when compiling code that uses Xxx. This really shouldn&#8217;t include options such as <code>-DHAS_JPEG</code> that a client source-code file uses to decide whether to <code>#include &lt;jpeg.h&gt;</code></p>
<dt><code>Xxx_EXECUTABLE</code></p>
<dd>Where to find the Xxx tool.</p>
<dt><code>Xxx_Yyy_EXECUTABLE</code></p>
<dd>Where to find the Yyy tool that comes with Xxx.</p>
<dt><code>Xxx_LIBRARY_DIRS</code></p>
<dd>Optionally, the final set of library directories listed in one variable for use by client code. This should not be a cache entry.</p>
<dt><code>Xxx_ROOT_DIR</code></p>
<dd>Where to find the base directory of Xxx.</p>
<dt><code>Xxx_VERSION_Yy</code></p>
<dd>Expect Version Yy if true. Make sure at most one of these is ever true.</p>
<dt><code>Xxx_WRAP_Yy</code></p>
<dd>If False, do not try to use the relevant CMake wrapping command.</p>
<dt><code>Xxx_Yy_FOUND</code></p>
<dd>If False, optional Yy part of Xxx system is not available.</p>
<dt><code>Xxx_FOUND</code></p>
<dd>Set to false, or undefined, if we haven&#8217;t found, or don&#8217;t want to use Xxx.</p>
<dt><code>Xxx_NOT_FOUND_MESSAGE</code></p>
<dd>Should be set by config-files in the case that it has set <code>Xxx_FOUND</code> to FALSE. The contained message will be printed by the <code>find_package()</code> command and by <code>find_package_handle_standard_args()</code> to inform the user about the problem.</p>
<dt><code>Xxx_RUNTIME_LIBRARY_DIRS</code></p>
<dd>Optionally, the runtime library search path for use when running an executable linked to shared libraries. The list should be used by user code to create the <code>PATH</code> on windows or <code>LD_LIBRARY_PATH</code> on UNIX. This should not be a cache entry.</p>
<dt><code>Xxx_VERSION</code></p>
<dd>The full version string of the package found, if any. Note that many existing modules provide <code>Xxx_VERSION_STRING</code> instead.</p>
<dt><code>Xxx_VERSION_MAJOR</code></p>
<dd>The major version of the package found, if any.</p>
<dt><code>Xxx_VERSION_MINOR</code></p>
<dd>The minor version of the package found, if any.</p>
<dt><code>Xxx_VERSION_PATCH</code></p>
<dd>The patch version of the package found, if any. </p>
<p> The following names should not usually be used in CMakeLists.txt files, but are typically cache variables for users to edit and control the behaviour of find modules (like entering the path to a library manually)</p>
<dt><code>Xxx_LIBRARY</code></p>
<dd>The path of the Xxx library (as used with <code>find_library()</code>, for example).</p>
<dt><code>Xxx_Yy_LIBRARY</code></p>
<dd>The path of the Yy library that is part of the Xxx system. It may or may not be required to use Xxx.</p>
<dt><code>Xxx_INCLUDE_DIR</code></p>
<dd>Where to find headers for using the Xxx library.</p>
<dt><code>Xxx_Yy_INCLUDE_DIR</code></p>
<dd>Where to find headers for using the Yy library of the Xxx system. </p>
<p> To prevent users being overwhelmed with settings to configure, try to keep as many options as possible out of the cache, leaving at least one option which can be used to disable use of the module, or locate a not-found library (e.g. <code>Xxx_ROOT_DIR</code>). For the same reason, mark most cache options as advanced. For packages which provide both debug and release binaries, it is common to create cache variables with a <code>_LIBRARY_&lt;CONFIG&gt;</code> suffix, such as <code>Foo_LIBRARY_RELEASE</code> and <code>Foo_LIBRARY_DEBUG</code>. </p>
<p> While these are the standard variable names, you should provide backwards compatibility for any old names that were actually in use. Make sure you comment them as deprecated, so that no-one starts using them.</dl>
<h3>A Sample Find Module</h3>
<p>We will describe how to create a simple find module for a library <code>Foo</code>. </p>
<p> The first thing that is needed is documentation. CMake&#8217;s documentation system requires you to start the file with a documentation marker and the name of the module. You should follow this with a simple statement of what the module does. </p>
<pre>#.rst:
# FindFoo
# -------
#
# Finds the Foo library
#</pre>
<p>More description may be required for some packages. If there are caveats or other details users of the module should be aware of, you can add further paragraphs below this. Then you need to document what variables and imported targets are set by the module, such as </p>
<pre># This will define the following variables::
#
# Foo_FOUND - True if the system has the Foo library
# Foo_VERSION - The version of the Foo library which was found
#
# and the following imported targets::
#
# Foo::Foo - The Foo library</pre>
<p>If the package provides any macros, they should be listed here, but can be documented where they are defined. See the <i>Module Documentation</i> section above for more details. </p>
<p> After the documentation, leave a blank line, and then add a copyright and licence notice block </p>
<pre>#=============================================================================
# Copyright 2009-2011 Your Name
#
# Distributed under the OSI-approved BSD License (the &quot;License&quot;);
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distribute this file outside of CMake, substitute the full
# License text for the above reference.)</pre>
<p>Now the actual libraries and so on have to be found. The code here will obviously vary from module to module (dealing with that, after all, is the point of find modules), but there tends to be a common pattern for libraries. </p>
<p> First, we try to use <code>pkg-config</code> to find the library. Note that we cannot rely on this, as it may not be available, but it provides a good starting point. </p>
<pre>find_package(PkgConfig)
pkg_check_modules(PC_Foo QUIET Foo)</pre>
<p>This should define some variables starting <code>PC_Foo_</code> that contain the information from the <code>Foo.pc</code> file. </p>
<p> Now we need to find the libraries and include files; we use the information from <code>pkg-config</code> to provide hints to CMake about where to look. </p>
<pre>find_path(Foo_INCLUDE_DIR
 NAMES foo.h
 PATHS ${PC_Foo_INCLUDE_DIRS}
 PATH_SUFFIXES Foo
)
find_library(Foo_LIBRARY
 NAMES foo
 PATHS ${PC_Foo_LIBRARY_DIRS}
)</pre>
<p>If you have a good way of getting the version (from a header file, for example), you can use that information to set <code>Foo_VERSION</code> (although note that find modules have traditionally used <code>Foo_VERSION_STRING</code>, so you may want to set both). Otherwise, attempt to use the information from <code>pkg-config</code> </p>
<pre>set(Foo_VERSION ${PC_Foo_VERSION})</pre>
<p>Now we can use <code>FindPackageHandleStandardArgs</code> to do most of the rest of the work for us </p>
<pre>include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Foo
 FOUND_VAR Foo_FOUND
 REQUIRED_VARS
 Foo_LIBRARY
 Foo_INCLUDE_DIR
 VERSION_VAR Foo_VERSION
)</pre>
<p>This will check that the <code>REQUIRED_VARS</code> contain values (that do not end in <code>-NOTFOUND</code>) and set <code>Foo_FOUND</code> appropriately. It will also cache those values. If <code>Foo_VERSION</code> is set, and a required version was passed to <code>find_package()</code>, it will check the requested version against the one in <code>Foo_VERSION</code>. It will also print messages as appropriate; note that if the package was found, it will print the contents of the first required variable to indicate where it was found. </p>
<p> At this point, we have to provide a way for users of the find module to link to the library or libraries that were found. There are two approaches, as discussed in the <i>Find Modules</i> section above. The traditional variable approach looks like </p>
<pre>if(Foo_FOUND)
 set(Foo_LIBRARIES ${Foo_LIBRARY})
 set(Foo_INCLUDE_DIRS ${Foo_INCLUDE_DIR})
 set(Foo_DEFINITIONS ${PC_Foo_CFLAGS_OTHER})
endif()</pre>
<p>If more than one library was found, all of them should be included in these variables (see the <i>Standard Variable Names</i> section for more information). </p>
<p> When providing imported targets, these should be namespaced (hence the <code>Foo::</code> prefix); CMake will recognize that values passed to <code>target_link_libraries()</code> that contain <code>::</code> in their name are supposed to be imported targets (rather than just library names), and will produce appropriate diagnostic messages if that target does not exist (see policy <code>CMP0028</code>). </p>
<pre>if(Foo_FOUND AND NOT TARGET Foo::Foo)
 add_library(Foo::Foo UNKNOWN IMPORTED)
 set_target_properties(Foo::Foo PROPERTIES
 IMPORTED_LOCATION &quot;${Foo_LIBRARY}&quot;
 INTERFACE_COMPILE_OPTIONS &quot;${PC_Foo_CFLAGS_OTHER}&quot;
 INTERFACE_INCLUDE_DIRECTORIES &quot;${Foo_INCLUDE_DIR}&quot;
 )
endif()</pre>
<p>One thing to note about this is that the <code>INTERFACE_INCLUDE_DIRECTORIES</code> and similar properties should only contain information about the target itself, and not any of its dependencies. Instead, those dependencies should also be targets, and CMake should be told that they are dependencies of this target. CMake will then combine all the necessary information automatically. </p>
<p> The type of the <code>IMPORTED</code> target created in the <code>add_library()</code> command can always be specified as <code>UNKNOWN</code> type. This simplifies the code in cases where static or shared variants may be found, and CMake will determine the type by inspecting the files. </p>
<p> If the library is available with multiple configurations, the <code>IMPORTED_CONFIGURATIONS</code> target property should also be populated: </p>
<pre>if(Foo_FOUND)
 if (NOT TARGET Foo::Foo)
 add_library(Foo::Foo UNKNOWN IMPORTED)
 endif()
 if (Foo_LIBRARY_RELEASE)
 set_property(TARGET Foo::Foo APPEND PROPERTY
 IMPORTED_CONFIGURATIONS RELEASE
 )
 set_target_properties(Foo::Foo PROPERTIES
 IMPORTED_LOCATION_RELEASE &quot;${Foo_LIBRARY_RELEASE}&quot;
 )
 endif()
 if (Foo_LIBRARY_DEBUG)
 set_property(TARGET Foo::Foo APPEND PROPERTY
 IMPORTED_CONFIGURATIONS DEBUG
 )
 set_target_properties(Foo::Foo PROPERTIES
 IMPORTED_LOCATION_DEBUG &quot;${Foo_LIBRARY_DEBUG}&quot;
 )
 endif()
 set_target_properties(Foo::Foo PROPERTIES
 INTERFACE_COMPILE_OPTIONS &quot;${PC_Foo_CFLAGS_OTHER}&quot;
 INTERFACE_INCLUDE_DIRECTORIES &quot;${Foo_INCLUDE_DIR}&quot;
 )
endif()</pre>
<p>The <code>RELEASE</code> variant should be listed first in the property so that that variant is chosen if the user uses a configuration which is not an exact match for any listed <code>IMPORTED_CONFIGURATIONS</code>. </p>
<p> Most of the cache variables should be hidden in the <code>ccmake3</code> interface unless the user explicitly asks to edit them. </p>
<pre>mark_as_advanced(
 Foo_INCLUDE_DIR
 Foo_LIBRARY
)</pre>
<p>If this module replaces an older version, you should set compatibility variables to cause the least disruption possible. </p>
<pre># compatibility variables
set(Foo_VERSION_STRING ${Foo_VERSION})</pre>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
