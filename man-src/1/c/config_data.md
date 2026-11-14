---
title: "config_data(1)"
name: "config_data"
section: "1"
letter: "c"
url: "/docs/linux/man/1-config_data/"
---

<h2 class="name">NAME</h2>
 

 config_data - Query or change configuration of Perl modules 

<h2>SYNOPSIS</h2>

 <pre><code>
#Get config / feature values
config_data-- module Foo::Bar-- feature bazzable
    config_data-- module Foo::Bar-- config magic_number
#Set config / feature values
        config_data-- module Foo::Bar-- set_feature bazzable = 1 config_data-- module Foo::Bar-- set_config magic_number = 42
#Print a usage message
    config_data-- help
</code></pre>

<h2>DESCRIPTION</h2>

 The <tt>&quot;config_data&quot;</tt> tool provides a command-line interface to the configuration of Perl modules. By ``configuration'', we mean something akin to ``user preferences'' or ``local settings''. This is a formalization and abstraction of the systems that people like Andreas Koenig (<tt>&quot;CPAN::Config&quot;</tt>), Jon Swartz (<tt>&quot;HTML::Mason::Config&quot;</tt>), Andy Wardley (<tt>&quot;Template::Config&quot;</tt>), and Larry Wall (perl's own Config.pm) have developed independently. 

 The configuration system employed here was developed in the context of <tt>&quot;Module::Build&quot;</tt>. Under this system, configuration information for a module <tt>&quot;Foo&quot;</tt>, for example, is stored in a module called <tt>&quot;Foo::ConfigData&quot;</tt>) (I would have called it <tt>&quot;Foo::Config&quot;</tt>, but that was taken by all those other systems mentioned in the previous paragraph...). These <tt>&quot;...::ConfigData&quot;</tt> modules contain the configuration data, as well as publicly accessible methods for querying and setting (yes, actually re-writing) the configuration data. The <tt>&quot;config_data&quot;</tt> script (whose docs you are currently reading) is merely a front-end for those methods. If you wish, you may create alternate front-ends. 

 The two types of data that may be stored are called <tt>&quot;config&quot;</tt> values and <tt>&quot;feature&quot;</tt> values. A <tt>&quot;config&quot;</tt> value may be any perl scalar, including references to complex data structures. It must, however, be serializable using <tt>&quot;Data::Dumper&quot;</tt>. A <tt>&quot;feature&quot;</tt> is a boolean (1 or 0) value.

<h2>USAGE</h2>

 This script functions as a basic getter/setter wrapper around the configuration of a single module. On the command line, specify which module's configuration you're interested in, and pass options to get or set <tt>&quot;config&quot;</tt> or <tt>&quot;feature&quot;</tt> values. The following options are supported:
<dl>
<dt>module
<dd> Specifies the name of the module to configure (required).
<dt>feature
<dd> When passed the name of a <tt>&quot;feature&quot;</tt>, shows its value. The value will be 1 if the feature is enabled, 0 if the feature is not enabled, or empty if the feature is unknown. When no feature name is supplied, the names and values of all known features will be shown.
<dt>config
<dd> When passed the name of a <tt>&quot;config&quot;</tt> entry, shows its value. The value will be displayed using <tt>&quot;Data::Dumper&quot;</tt> (or similar) as perl code. When no config name is supplied, the names and values of all known config entries will be shown.
<dt>set_feature
<dd> Sets the given <tt>&quot;feature&quot;</tt> to the given boolean value. Specify the value as either 1 or 0.
<dt>set_config
<dd> Sets the given <tt>&quot;config&quot;</tt> entry to the given value.
<dt>eval
<dd> If the <tt>&quot;--eval&quot;</tt> option is used, the values in <tt>&quot;set_config&quot;</tt> will be evaluated as perl code before being stored. This allows moderately complicated data structures to be stored. For really complicated structures, you probably shouldn't use this command-line interface, just use the Perl <font SIZE="-1">API</font> instead.
<dt>help
<dd> Prints a help message, including a few examples, and exits.</dl>

<h2>AUTHOR</h2>

 Ken Williams, kwilliams [at] cpan.org

<h2>COPYRIGHT</h2>

 Copyright (c) 1999, Ken Williams. All rights reserved. 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/3-module--build/">Module::Build</a></i>(3), <i><a HREF="/docs/linux/man/1-perl/">perl</a></i>(1). 

<h2>Index</h2>


