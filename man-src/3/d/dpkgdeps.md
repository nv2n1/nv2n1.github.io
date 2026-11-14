---
title: "dpkgdeps(3)"
name: "dpkgdeps"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgdeps/"
---

Dpkg::Deps - parse and manipulate dependencies of Debian packages 

<h2>Description</h2>The Dpkg::Deps module provides objects implementing various types of dependencies. 

 The most important function is <i>deps_parse()</i>, it turns a dependency line in a set of Dpkg::Deps::{Simple,AND,OR,Union} objects depending on the case.
<h2>Functions</h2>All the deps_* functions are exported by default.
<dl COMPACT><dt>deps_eval_implication($rel_p, $v_p, $rel_q, $v_q)
<dd>($rel_p, <tt>$v_p</tt>) and ($rel_q, <tt>$v_q</tt>) express two dependencies as (relation, version). The relation variable can have the following values that are exported by Dpkg::Version: <font SIZE="-1">REL_EQ, REL_LT, REL_LE, REL_GT, REL_GT.</font> 

 This functions returns 1 if the ``p'' dependency implies the ``q'' dependency. It returns 0 if the ``p'' dependency implies that ``q'' is not satisfied. It returns undef when there's no implication. 

 The <tt>$v_p</tt> and <tt>$v_q</tt> parameter should be Dpkg::Version objects.
<dt>my $dep = deps_concat(@dep_list)
<dd>This function concatenates multiple dependency lines into a single line, joining them with ``, '' if appropriate, and always returning a valid string.
<dt>my $dep = deps_parse($line, %options)
<dd>This function parses the dependency line and returns an object, either a Dpkg::Deps::AND or a Dpkg::Deps::Union. Various options can alter the behaviour of that function.
<dl COMPACT><dd><dl COMPACT><dt>use_arch (defaults to 1)
<dd>Take into account the architecture restriction part of the dependencies. Set to 0 to completely ignore that information.
<dt>host_arch (defaults to the current architecture)
<dd>Define the host architecture. By default it uses <i>Dpkg::Arch::get_host_arch()</i> to identify the proper architecture.
<dt>build_arch (defaults to the current architecture)
<dd>Define the build architecture. By default it uses <i>Dpkg::Arch::get_build_arch()</i> to identify the proper architecture.
<dt>reduce_arch (defaults to 0)
<dd>If set to 1, ignore dependencies that do not concern the current host architecture. This implicitely strips off the architecture restriction list so that the resulting dependencies are directly applicable to the current architecture.
<dt>use_profiles (defaults to 1)
<dd>Take into account the profile restriction part of the dependencies. Set to 0 to completely ignore that information.
<dt>build_profiles (defaults to no profile)
<dd>Define the active build profiles. By default no profile is defined.
<dt>reduce_profiles (defaults to 0)
<dd>If set to 1, ignore dependencies that do not concern the current build profile. This implicitly strips off the profile restriction formula so that the resulting dependencies are directly applicable to the current profiles.
<dt>reduce_restrictions (defaults to 0)
<dd>If set to 1, ignore dependencies that do not concern the current set of restrictions. This implicitly strips off any architecture restriction list or restriction formula so that the resulting dependencies are directly applicable to the current restriction. This currently implies <tt>&quot;reduce_arch&quot;</tt> and <tt>&quot;reduce_profiles&quot;</tt>, and overrides them if set.
<dt>union (defaults to 0)
<dd>If set to 1, returns a Dpkg::Deps::Union instead of a Dpkg::Deps::AND. Use this when parsing non-dependency fields like Conflicts.
<dt>build_dep (defaults to 0)
<dd>If set to 1, allow build-dep only arch qualifiers, that is “:native”. This should be set whenever working with build-deps.</dl></dl><dl COMPACT><dd></dl><dt>my $bool = deps_iterate($deps, $callback_func)
<dd>This function visits all elements of the dependency object, calling the callback function for each element. 

 The callback function is expected to return true when everything is fine, or false if something went wrong, in which case the iteration will stop. 

 Return the same value as the callback function.
<dt>deps_compare($a, $b)
<dd>Implements a comparison operator between two dependency objects. This function is mainly used to implement the <i>sort()</i> method.</dl><h2>OBJECTS - Dpkg::Deps::*</h2>There are several kind of dependencies. A Dpkg::Deps::Simple dependency represents a single dependency statement (it relates to one package only). Dpkg::Deps::Multiple dependencies are built on top of this object and combine several dependencies in a different manners. Dpkg::Deps::AND represents the logical ``<font SIZE="-1">AND''</font> between dependencies while Dpkg::Deps::OR represents the logical ``<font SIZE="-1">OR''.</font> Dpkg::Deps::Multiple objects can contain Dpkg::Deps::Simple object as well as other Dpkg::Deps::Multiple objects. 

 In practice, the code is only meant to handle the realistic cases which, given Debian's dependencies structure, imply those restrictions: <font SIZE="-1">AND</font> can contain Simple or <font SIZE="-1">OR</font> objects, <font SIZE="-1">OR</font> can only contain Simple objects. 

 Dpkg::Deps::KnownFacts is a special object that is used while evaluating dependencies and while trying to simplify them. It represents a set of installed packages along with the virtual packages that they might provide.
<h3><font SIZE="-1">COMMON FUNCTIONS</font></h3><dl COMPACT><dt>$dep-&gt;<i>is_empty()</i>
<dd>Returns true if the dependency is empty and doesn't contain any useful information. This is true when a Dpkg::Deps::Simple object has not yet been initialized or when a (descendant of) Dpkg::Deps::Multiple contains an empty list of dependencies.
<dt>$dep-&gt;<i>get_deps()</i>
<dd>Returns a list of sub-dependencies. For Dpkg::Deps::Simple it returns itself.
<dt>$dep-&gt;output([$fh])
<dd><dt>&quot;$dep&quot;
<dd>Returns a string representing the dependency. If <tt>$fh</tt> is set, it prints the string to the filehandle.
<dt>$dep-&gt;implies($other_dep)
<dd>Returns 1 when <tt>$dep</tt> implies <tt>$other_dep</tt>. Returns 0 when <tt>$dep</tt> implies <font SIZE="-1">NOT</font>($other_dep). Returns undef when there's no implication. <tt>$dep</tt> and <tt>$other_dep</tt> do not need to be of the same type.
<dt>$dep-&gt;<i>sort()</i>
<dd>Sorts alphabetically the internal list of dependencies. It's a no-op for Dpkg::Deps::Simple objects.
<dt>$dep-&gt;arch_is_concerned($arch)
<dd>Returns true if the dependency applies to the indicated architecture. For multiple dependencies, it returns true if at least one of the sub-dependencies apply to this architecture.
<dt>$dep-&gt;reduce_arch($arch)
<dd>Simplifies the dependency to contain only information relevant to the given architecture. A Dpkg::Deps::Simple object can be left empty after this operation. For Dpkg::Deps::Multiple objects, the non-relevant sub-dependencies are simply removed. 

 This trims off the architecture restriction list of Dpkg::Deps::Simple objects.
<dt>$dep-&gt;get_evaluation($facts)
<dd>Evaluates the dependency given a list of installed packages and a list of virtual packages provided. Those lists are part of the Dpkg::Deps::KnownFacts object given as parameters. 

 Returns 1 when it's true, 0 when it's false, undef when some information is lacking to conclude.
<dt>$dep-&gt;simplify_deps($facts, @assumed_deps)
<dd>Simplifies the dependency as much as possible given the list of facts (see object Dpkg::Deps::KnownFacts) and a list of other dependencies that are known to be true.
<dt>$dep-&gt;<i>has_arch_restriction()</i>
<dd>For a simple dependency, returns the package name if the dependency applies only to a subset of architectures. For multiple dependencies, it returns the list of package names that have such a restriction.
<dt>$dep-&gt;<i>reset()</i>
<dd>Clears any dependency information stored in <tt>$dep</tt> so that <tt>$dep</tt>-&gt;<i>is_empty()</i> returns true.</dl><h3>Dpkg::Deps::Simple</h3>Such an object has four interesting properties:
<dl COMPACT><dt>package
<dd>The package name (can be undef if the dependency has not been initialized or if the simplification of the dependency lead to its removal).
<dt>relation
<dd>The relational operator: ``='', ``&lt;&lt;'', ``&lt;='', ``&gt;='' or ``&gt;&gt;''. It can be undefined if the dependency had no version restriction. In that case the following field is also undefined.
<dt>version
<dd>The version.
<dt>arches
<dd>The list of architectures where this dependency is applicable. It's undefined when there's no restriction, otherwise it's an array ref. It can contain an exclusion list, in that case each architecture is prefixed with an exclamation mark.
<dt>archqual
<dd>The arch qualifier of the dependency (can be undef if there's none). In the dependency ``python:any (&gt;= 2.6)'', the arch qualifier is ``any''.</dl>
 

 <i></i><font SIZE="-1"><i>METHODS</i></font><i></i>
<dl COMPACT><dt>$simple_dep-&gt;parse_string('dpkg-dev (&gt;= 1.14.8) [!hurd-i386]')
<dd>Parses the dependency and modifies internal properties to match the parsed dependency.
<dt>$simple_dep-&gt;merge_union($other_dep)
<dd>Returns true if <tt>$simple_dep</tt> could be modified to represent the union of both dependencies. Otherwise returns false.</dl><h3>Dpkg::Deps::Multiple</h3>This is the base class for Dpkg::Deps::{<font SIZE="-1">AND,OR</font>,Union}. It implements the following methods:
<dl COMPACT><dt>$mul-&gt;add($dep)
<dd>Adds a new dependency object at the end of the list.</dl><h3>Dpkg::Deps::AND</h3>This object represents a list of dependencies who must be met at the same time.
<dl COMPACT><dt>$and-&gt;output([$fh])
<dd>The output method uses ``, '' to join the list of sub-dependencies.</dl><h3>Dpkg::Deps::OR</h3>This object represents a list of dependencies of which only one must be met for the dependency to be true.
<dl COMPACT><dt>$or-&gt;output([$fh])
<dd>The output method uses `` | '' to join the list of sub-dependencies.</dl><h3>Dpkg::Deps::Union</h3>This object represents a list of relationships.
<dl COMPACT><dt>$union-&gt;output([$fh])
<dd>The output method uses ``, '' to join the list of relationships.
<dt>$union-&gt;implies($other_dep)
<dd><dt>$union-&gt;get_evaluation($other_dep)
<dd>Those methods are not meaningful for this object and always return undef.
<dt>$union-&gt;simplify_deps($facts)
<dd>The simplication is done to generate an union of all the relationships. It uses <tt>$simple_dep</tt>-&gt;merge_union($other_dep) to get its job done.</dl><h3>Dpkg::Deps::KnownFacts</h3>This object represents a list of installed packages and a list of virtual packages provided (by the set of installed packages).
<dl COMPACT><dt>my $facts = Dpkg::Deps::KnownFacts-&gt;<i>new()</i>;
<dd>Creates a new object.
<dt>$facts-&gt;add_installed_package($package, $version, $arch, $multiarch)
<dd>Records that the given version of the package is installed. If <tt>$version</tt>/$arch is undefined we know that the package is installed but we don't know which version/architecture it is. <tt>$multiarch</tt> is the Multi-Arch field of the package. If <tt>$multiarch</tt> is undef, it will be equivalent to ``Multi-Arch: no''. 

 Note that <tt>$multiarch</tt> is only used if <tt>$arch</tt> is provided.
<dt>$facts-&gt;add_provided_package($virtual, $relation, $version, $by)
<dd>Records that the ``$by'' package provides the <tt>$virtual</tt> package. <tt>$relation</tt> and <tt>$version</tt> correspond to the associated relation given in the Provides field (if present).
<dt>my ($check, $param) = $facts-&gt;check_package($package)
<dd><tt>$check</tt> is one when the package is found. For a real package, <tt>$param</tt> contains the version. For a virtual package, <tt>$param</tt> contains an array reference containing the list of packages that provide it (each package is listed as [ <tt>$provider</tt>, <tt>$relation</tt>, <tt>$version</tt> ]). 

 This function is obsolete and should not be used. Dpkg::Deps::KnownFacts is only meant to be filled with data and then passed to Dpkg::Deps methods where appropriate, but it should not be directly queried.</dl><h2>Changes</h2><h3>Version 1.05</h3>New function: <i>Dpkg::Deps::deps_iterate()</i>.
<h3>Version 1.04</h3>New options: Add use_profiles, build_profiles, reduce_profiles and reduce_restrictions to <i>Dpkg::Deps::deps_parse()</i>. 

 New methods: Add <tt>$dep</tt>-&gt;<i>profile_is_concerned()</i> and <tt>$dep</tt>-&gt;<i>reduce_profiles()</i> for all dependency objects.
<h3>Version 1.03</h3>New option: Add build_arch option to <i>Dpkg::Deps::deps_parse()</i>.
<h3>Version 1.02</h3>New function: <i>Dpkg::Deps::deps_concat()</i>
<h3>Version 1.01</h3>New method: Add <tt>$dep</tt>-&gt;<i>reset()</i> for all dependency objects. 

 New property: Dpkg::Deps::Simple now recognizes the arch qualifier ``any'' and stores it in the ``archqual'' property when present. 

 New option: Dpkg::Deps::KnownFacts-&gt;<i>add_installed_package()</i> now accepts 2 supplementary parameters ($arch and <tt>$multiarch</tt>). 

 Deprecated method: Dpkg::Deps::KnownFacts-&gt;<i>check_package()</i> is obsolete, it should not have been part of the public <font SIZE="-1">API.</font>
<h3>Version 1.00</h3>Mark the module as public.
