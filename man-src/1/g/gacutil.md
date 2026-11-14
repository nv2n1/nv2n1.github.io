---
title: "gacutil(1)"
name: "gacutil"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gacutil/"
description: "gacutil – Global Assembly Cache management utility."
---

<h2 class="name">NAME</h2>
<p> gacutil &#8211; Global Assembly Cache management utility. </p>
<h2>SYNOPSIS</h2>
<p> <code>gacutil [-user] [command] [options] </code></p>
<h2>DESCRIPTION</h2>
<p> <i>gacutil</i> is a tool used by developers to install versioned assemblies into the system Global Assembly Cache (GAC) to become part of the assemblies that are available for all applications at runtime. </p>
<p> Notice that they are not directly available to the compiler. The convention is that assemblies must also be placed in a separate directory to be accessed by the compiler. This is done with the -package directive to gacutil. </p>
<p> The tool allows for installation, removal, and listing of the contents of the assembly cache. </p>
<p> The GAC is relative to the Mono installation prefix: mono_prefix/lib/mono. </p>
<h2>COMMANDS</h2>
<p> <i>-i &lt;assembly_path&gt; [-check_refs] [-package NAME] [-root ROOTDIR] [-gacdir GACDIR]</i> </p>
<p>&nbsp;Installs an assembly into the global assembly cache.&nbsp;&lt;assembly_path&gt; is the name of the file that contains the assembly manifest </p>
<p> The -package option can be used to also create a directory in in prefix/lib/mono with the name NAME, and a symlink is created from NAME/assembly_name to the assembly on the GAC. This is used so developers can reference a set of libraries at once. </p>
<p> The -root option is used to specify the &quot;libdir&quot; value of an installation prefix which differs from the prefix of the system GAC. Typical automake usage is &quot;-root $(DESTDIR)$(prefix)/lib&quot;. To access assemblies installed to a prefix other than the mono prefix, it is necessary to set the MONO_GAC_PREFIX environment variable. </p>
<p> The -gacdir option is included for backward compatibility but is not recommended for new code. Use the -root option instead. </p>
<p> The -check_refs option is used to ensure that the assembly being installed into the GAC does not reference any non strong named assemblies. Assemblies being installed to the GAC should not reference non strong named assemblies, however the is an optional check. </p>
<p> <i>-l [assembly_name] [-root ROOTDIR] [-gacdir GACDIR]</i> </p>
<p> Lists the contents of the global assembly cache. When the &lt;assembly_name&gt; parameter is specified only matching assemblies are listed. </p>
<p> <i>-u &lt;assembly_display_name&gt; [-package NAME] [-root ROOTDIR] [-gacdir GACDIR]</i> </p>
<p> Uninstalls an assembly from the global assembly cache. &lt;assembly_display_name&gt; is the name of the assembly (partial or fully qualified) to remove from the global assembly cache. If a partial name is specified all matching assemblies will be uninstalled. As opposed to the install option that takes a filename, this takes as an argument the assembly name, which looks like this: </p>
<pre>
        MyLibrary.Something, version=1.0.0.0, publicKeyToken=xxxx,culture=neutral
</pre>
<p> Notice that you can have spaces in the command line. There is no need to quote them. </p>
<p> Performs a greedy removal. If you only specify one component like, &quot;MyLibrary.Something&quot;, it will remove all versions of the library. </p>
<p> <i>-us &lt;assembly_path&gt; [-package NAME] [-root ROOTDIR] [-gacdir GACDIR]</i> Uninstalls an assembly using the specified assembly&#8217;s full name. &lt;assembly path&gt; is the path to an assembly. The full assembly name is retrieved from the specified assembly if there is an assembly in the GAC with a matching name, it is removed. Unlike the -u option this option takes a file name, like this: </p>
<pre>
        Example: -us myDll.dll
</pre>
<p> <i>-ul &lt;assembly_list_file&gt; [-package NAME] [-root ROOTDIR] [-gacdir GACDIR]</i> Uninstalls one or more assemblies from the global assembly cache. &lt;assembly_list_file&gt; is the path to a test file containing a list of assembly names on separate lines. </p>
<pre>
Example -ul assembly_list.txt
</pre>
<pre>
assembly_list.txt contents:
    assembly1,Version=1.0.0.0,Culture=en,PublicKeyToken=0123456789abcdef
    assembly2,Version=2.0.0.0,Culture=en,PublicKeyToken=0123456789abcdef
</pre>
<h2>FILES</h2>
<p> On Unix assemblies are loaded from the installation lib directory. If you set `prefix&#8217; to /usr, the assemblies will be located in /usr/lib. On Windows, the assemblies are loaded from the directory where mono and mint live. </p>
<p> /etc/mono/config, ~/.mono/config </p>
<p> Mono runtime configuration file. See the <a href="/docs/linux/man/5-mono-config/">mono-config</a>(5) manual page for more information.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.go-mono.com">http://www.go-mono.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mcs/">mcs</a>(1),</code><a href="/docs/linux/man/1-mono/">mono</a>(1) </p>
<h2>Index</h2>
