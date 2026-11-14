---
title: "pm_which(1)"
name: "pm_which"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pm_which/"
---

<h2 class="name">NAME</h2>
 

 pm_which - find installed modules 

<h2>SYNOPSIS</h2>

 <pre>
    pm_which [ options ] module(s)
    Returns the path to the given module(s)
</pre>

<h2><font SIZE="-1">OPTIONS</font></h2>

 <pre><code>
- q, --quiet Just print paths - p, --paths Just convert the module name into a relative path - a, --all Print all paths, not just the first one found - n, --namespace Print all modules in the given namespace - m Only print module names, not paths - V Show module version - I libpath Add a path to search(like perl - I) - d, --dump Dump paths that would be searched(@INC by default) - h, --help Print this message - v, --version Print version information - Read modules from stdin, one per line
</code></pre>

<h2>DESCRIPTION</h2>

 This tool reports the locations of installed perl modules. 

 By default it lists the location of each specified module that would be loaded by require.

<h2>OPTION DETAILS</h2>

<h2>quiet</h2>

 Under quiet mode, module names are suppressed and missing modules are not reported. 

 Normal output: 

 <pre>
    $ pm_which Module::One Module::Two Missing::Module
    Module::One     - /path/to/Module/One.pm
    Module::Two     - /path/to/Module/Two.pm
    Missing::Module - not found
</pre> 

 Under --quiet: 

 <pre>
    $ pm_which -q Module::One Module::Two Missing::Module
    /path/to/Module/One.pm
    /path/to/Module/Two.pm
</pre>

<h2>paths</h2>

 In ``paths'' mode, each module is simply converted into a relative file path. This is possible even when the module is not installed. 

 <pre>
    $ pm_which -p Missing::Module
    Missing/Module.pm
</pre>

<h2>all</h2>

 When the ``all'' switch is specified, all installed modules will be reported, not just the first one. This is useful for determining when there is a module installed in multiple locations. 

 <pre>
    $ pm_which -a MyModule
    /path/to/MyModule.pm
    /home/me/perl/MyModule.pm
</pre>

<h2>namespace</h2>

 Arguments are taken as namespaces to search under. 

 <pre>
    $ pm_which -n MyModule
    MyModule            - /path/to/MyModule.pm
    MyModule::Foo       - /path/to/MyModule/Foo.pm
    MyModule::Foo::Bar  - /path/to/MyModule/Foo/Bar.pm
</pre>

<h2>-m</h2>

 Disables printing of module paths. This is only really useful in conjunction with --namespace. 

 <pre>
    $ pm_which -nm MyModule
    MyModule
    MyModule::Foo
    MyModule::Foo::Bar
</pre>

<h2>-V</h2>

 Prints the version of each module, according to ExtUtils::MakeMaker. 

 <pre><code>
$ pm_which - V MyModule MyModule - / path / to / MyModule.pm[1.00] $ pm_which - Vnm MyModule MyModule[1.00] MyModule::Foo[0.01] MyModule::Foo::Bar[undef]
</code></pre>

<h2>dump</h2>

 Dumps the paths that would be searched and exits. This is <tt>@INC</tt> modified by any -I switches. 

 <pre>
    $ pm_which --dump
    /usr/lib/perl5/site_perl/5.8.6
    /usr/lib/perl5/vendor_perl/5.8.6
    ...
    $ pm_which -I lib --dump -I blib/lib
    lib
    blib/lib
    /usr/lib/perl5/site_perl/5.8.6
    ...
</pre>

<h2>version</h2>

 Prints the version number of the script, plus the version and path of Module::Util that was loaded.

<h2>EXIT CODES</h2>

<dl>
<dt>*
<dd> 0 - Everything was <font SIZE="-1">OK</font>
<dt>*
<dd> 1 - Initialisation failed (bad switches?)
<dt>*
<dd> 2 - Some modules were not installed</dl>

<h2>SEE ALSO</h2>

 This utility comes with Module::Util.

<h2>AUTHOR</h2>

 Matt Lawrence &lt;mattlaw [at] cpan.org&gt; 

<h2>Index</h2>


