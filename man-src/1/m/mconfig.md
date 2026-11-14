---
title: "mconfig(1)"
name: "mconfig"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mconfig/"
description: "mconfig, – Utility for modifying .NET configuration files"
---

<h2>NAME</h2>
<p> mconfig, &#8211; Utility for modifying .NET configuration files</p>
<h2>SYNOPSIS</h2>
<p> <code>mconfig [options] command [command_parameters]</code></p>
<h2>DESCRIPTION</h2>
<p> mconfig can be used to edit .NET configuration files, by adding &quot;features&quot; (that is sets of xml statements) defined in one of the config files read by mconfig. The config file can also define layouts of default configuration files, which may be useful for bootstrapping your .NET projects. </p>
<p> To see the list of recognized commands, default configuration files and features, run mconfig without passing any parameters.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c &lt;config_file&gt;, &#8211;config=&lt;config_file&gt;</code></p>
<dd> Read the specified config file after reading the other, preconfigured, config files for the utility. Settings in the specified file override those found in the other configuration locations.</p>
<dt><code>-t {any | web | application}, &#8211;target={any | web | application}</code></p>
<dd> Features and default configuration files defined in the mconfig config file(s) can be assigned to one of the three targets &#8211; <i>web</i> (for ASP.NET features/config files), <i>application</i> &#8211; for .NET applications, <i>any</i> &#8211; applicable in both of the previous targets. Defaults to <i>any</i>.</p>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Show a summary usage screen.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show the mconfig version</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>{addfeature, af} &lt;feature_name&gt; [config_file_path]</code></p>
<dd> Adds the feature named <i>&lt;feature_name&gt;</i> to the specified config file. If <i>[config_file_path]</i> is omitted, the name of the output configuration file will be chosen based on the selected target (see the <i>-t</i> option). The <i>web</i> target outputs configuration to file named <i>Web.config</i>, and the <i>application</i> target outputs to file named <i>application.exe.config</i>. The <i>any</i> target does not have a default output file. </p>
<p> If the specified config file exists, the feature will be injected into it at the locations specified by mconfig configuration. If the target config file does not exist, it will be created and will contain only the specified feature and all its dependencies.</p>
<dt><code>{defaultconfig, dc} [config_name [target_directory]]</code></p>
<dd> Generates a default config file using the configuration entry named <i>[config_name]</i> and outputs the resulting configuration file to the directory given by the <i>[target_directory]</i> option. If <i>[config_name]</i> is omitted, it defaults to <i>Web.config</i> for the <i>web</i> target and <i>application</i> target. The <i>any</i> target does not specify any default output configuration name. If the <i>[target_directory]</i> parameter is omitted, it defaults to the current directory. </p>
<p> Name of the output config file created in <i>[target_directory]</i> is given in the config file layout definition.</dl>
<h2>FILES</h2>
<p> Config files are read in the order given below. Each subsequent file may override settings found in the files read before it.</p>
<dl>
<dt><code>$prefix/etc/mono/mconfig/config.xml</code></p>
<dd> The default configuration file, distributed with mconfig. <i>$prefix</i> is the mconfig installation prefix specified on the compilation time.</p>
<dt><code>$config_dir/mconfig/config.xml</code></p>
<dd> $config_dir is the directory specified in the <i>XDG_CONFIG_HOME</i> environment variable or,<br />
&nbsp;<wbr>if it is empty, in the&nbsp;<wbr><i>.config</i>&nbsp;<wbr>directory located in the user&#8217;s home directory. This file is not distributed with Mono.</p>
<dt><code>./mconfig.xml</code></p>
<dd> Local configuration file which can contain per-application settings.</dl>
<h2>SEE ALSO</h2>
<p> mconfig.config (5)</p>
<h2>AUTHOR</h2>
<p> Written by Marek Habersack</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
