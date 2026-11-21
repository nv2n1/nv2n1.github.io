---

title: "mdtool(1)"
name: "mdtool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdtool/"
description: "mdtool – MonoDevelop Application Runner"
---

<h2>NAME</h2>
<p> mdtool &#8211; MonoDevelop Application Runner</p>
<p> <code>mdtool</code> &lt;applicationId&gt; &#8230; </p>
<p> <code>mdtool</code> setup &#8230; </p>
<p> <code>mdtool</code> -q</p>
<p> <code>mdtool</code> is a tool that can execute head-less MonoDevelop applications, this can be used for example to do batch compilations without starting up the MonoDevelop GUI.</p>
<h2>USAGE</h2>
<dl>
<dt><code>applicationId &#8230;</code></dt>
<dd> Runs the specified application.</dd>
<dt><code>/-q</code></dt>
<dd> Lists available applications.</dd></dl>
<h2>Available Applications</h2>
<p> The list of applications returned by the option -q might be different depending on which add-ins are installed.</p>
<dl>
<dt><code>gsetup</code></dt>
<dd> Graphical add-in setup utility.</dd>
<dt><code>build [options] [project-file]</code></dt>
<dd> Project build tool. Use this tool to build any solution supported by MonoDevelop (eg. .mds, .sln). If no solution/project is specified then it will pull the first solution it can find in the current directory. You can use this option to build packages in a head-less or batch fashion.</dd>
<dl>
<dt>
</dt><dd>
<p> <code>Options</code></p>
</dd><dl>
<dt>
</dt><dd> <code>-c , &#8211;configuration:CONFIGURATION</code> Name of the solution configuration to build. </dd>
<p> <code>-t , &#8211;target:TARGET</code> Name of the target: Clean or Build </p>
<p> <code>-p , &#8211;project:PROJECT</code> Name of the project to build.</dl>
</dl>
<dt><code>dbgen</code></dt>
<dd> Parser database generation tool.</dd>
<dt><code>project-export</code></dt>
<dd> Project conversion tool. </dd>
<dt><code>IDE</code></dt>
<dd> The MonoDevelop IDE. </dd>
<dt><code>generate-makefiles &lt;solution-file&gt; [&#8211;simple-makefiles] [-d:default-config]</code></dt>
<dd> Makefile generator tool. This can be used to generate makefiles from any solution supported by MonoDevelop. </dd>
<dl>
<dt>
</dt><dd> <code>Options</code></dd>
<dl>
<dt>
</dt><dd> <code>&#8211;simple-makefiles , -s</code> Generates set of Makefiles with the most common targets, and a configuration script that does a basic check of package dependencies. Default is to generate Makefile structure based on Autotools with the standard targets and configuration scripts. </dd>
<p> <code>-d:default-config</code> Configuration that the Makefile will build by default. Other configurations can be selected via the &#8216;&#8211;config&#8217; or &#8216;&#8211;enable-*&#8217; option of the generated configure script.</dl>
</dl>
<dt><code>setup command [arg1, .., argn2]</code></dt>
<dd> Runs the MonoDevelop add-in setup command. You must specify a command to execute. If none is provided a list of commands is displayed</dd>
<dl>
<dt>
</dt><dd> <code>Add-in Commands</code></dd>
<dl>
<dt>
</dt><dd> <code>install (i) [package-name|package-file]</code> Installs an add-in or set of addins. The command argument is a list of files and/or package names. If a package name is provided the package will be looked out in the registered repositories. A specific add-in version can be specified by appending it to. the package name using MonoDevelop.SourceEditor/0.9.1</dd>
<dl>
<dt><code>uninstall (u) [package-name]</code></dt>
<dd> Uninstalls an add-in. The command argument is the name of the add-in to uninstall.</dd>
<dt><code>check-install (ci)</code></dt>
<dd> Checks if a package is installed. If it is not, it looks for the package in the registered repositories, and if found the package is downloaded and installed, including all needed dependencies.</dd>
<dt><code>update (up) </code></dt>
<dd> Downloads and installs available updates for installed add-ins.</dd>
<dt><code>list (l) </code></dt>
<dd> Prints a list of all installed add-ins.</dd>
<dt><code>list-av (la) </code></dt>
<dd> Prints a list of add-ins available to install in the registered repositories.</dd>
<dt><code>list-update (lu) </code></dt>
<dd> Prints a list of available add-in updates in the registered repositories.</dd></dl>
</dl>
<p> <code>Repository Commands</code></p>
<dl>
<dl>
<dt><code>rep-add (ra) url1 [url2 [url2]]</code></dt>
<dd> Registers an add-in repository. Several URLs can be provided.</dd>
<dt><code>rep-remove (rr) url1 [url2 [url2]]</code></dt>
<dd> Unregisters an add-in repository. Several URLs can be provided.</dd>
<dt><code>rep-update (ru) </code></dt>
<dd> Updates the lists of addins available in all registered repositories.</dd>
<dt><code>rep-list (rl) </code></dt>
<dd> Shows a list of all registered repositories.</dd></dl>
</dl>
<p> <code>Add-in Registry Commands:</code></p>
<dl>
<dl>
<dt><code>reg-update (rgu) </code></dt>
<dd> Looks for changes in add-in directories and updates the registry. New add-ins will be added and deleted add-ins will be removed.</dd>
<dt><code>reg-build (rgu) </code></dt>
<dd>
</dd><dt><code>info [filename|package-name]</code></dt>
<dd> Prints information about an add-in.</dd></dl>
</dl>
<p> <code>Packaging Commands</code></p>
<dl>
<dl>
<dt><code>rep-build (rb) path</code></dt>
<dd> Scans the provided directory and generates a set of index files with entries for all add-in packages found in the directory tree. The resulting file structure is an add-in repository that can be published in a web site or a shared directory.</dd>
<dt><code>pack (p) file-path</code></dt>
<dd> Creates an add-in package (.mpack file) which includes all files needed to deploy an add-in. The command parameter is the path to the add-in&#8217;s configuration file.</dd>
<dt><code>help (h) [command]</code></dt>
<dd> Shows help for the given command</dd></dl>
</dl>
<p> <code>Debug Commands:</code></p>
<dl>
<dl>
<dt><code>dump-file </code></dt>
<dd> Prints the contents of a registry file for debugging.</dd></dl>
</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-monodevelop/">monodevelop</a>(1), <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1) <code>.SH</code>COPYRIGHT Copyright (C) 2007 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/monodevelop-list">http://lists.ximian.com/mailman/listinfo/monodevelop-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.monodevelop.com">http://www.monodevelop.com</a> for details </p>
