---
title: "module-starter(1)"
name: "module-starter"
section: "1"
letter: "m"
url: "/docs/linux/man/1-module-starter/"
---

<h2 class="name">NAME</h2>
 

 module-starter - creates a skeleton module distribution 

<h2>SYNOPSIS</h2>

 module-starter [options] 

 Options: 

 <pre><code>
--module = module Module name(required, repeatable)-- distro = name Distribution name(optional)-- dir = dirname Directory name to create new module in(optional)--builder = module Build with 'ExtUtils::MakeMaker' or 'Module::Build' --eumm Same as-- builder = ExtUtils::MakeMaker-- mb Same as-- builder = Module::Build-- mi Same as-- builder = Module::Install-- author = name Author's name (required) --email = email Author's email (required) --license = type License under which the module will be distributed(default is the same license as perl)-- verbose Print progress messages while working-- force Delete pre - existing files if needed-- help Show this message
</code></pre> 

 Available Licenses: 
&nbsp;<wbr>perl, bsd, gpl, lgpl, mit 

 Example: 

 <pre><code>
module - starter-- module = Foo::Bar, Foo::Bat-- author = "Andy Lester" --email = andy[at] petdance.com
</code></pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;module-starter&quot;</tt> is a command-line interface to Module::Starter, which it uses to perform all the work of creating distributions. An alternate backend for <tt>&quot;module-starter&quot;</tt> can be specified with the <tt>&quot;--class&quot;</tt> option. Plugins to the standard Module::Starter module can be specified with one or more <tt>&quot;--plugin&quot;</tt> options. 

 If no directory name is supplied, the distribution name will be used for the directory. If no distribution name is supplied, the first listed module name will be used as the distribution name. 

 Multiple --builder options may be supplied to produce the files for multiple builders.

<h2>CONFIGURATION</h2>

 module-starter will look for a configuration file before reading its command line parameters. The default location is <tt>&quot;$HOME/.module-starter/config&quot;</tt> but if the <font SIZE="-1">MODULE_STARTER_DIR</font> environment variable is set, module-starter will look for <tt>&quot;config&quot;</tt> in that directory. 

 The configuration file is just a list of names and values, separated by colons. Values that take lists are just space separated. A sample configuration file might read: 

 <pre>
 author: Ricardo SIGNES
 email:  rjbs [at] cpan.org
 plugins: Module::Starter::Simple Module::Starter::Plugin::XYZ
 xyz_option: red green blue
</pre> 

 This format may become more elaborate in the future, but a file of this type should remain valid. 

<h2>Index</h2>


