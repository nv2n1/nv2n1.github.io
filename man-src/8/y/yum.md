---
title: "yum(8)"
name: "yum"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yum/"
description: "yum – Yellowdog Updater Modified"
---

<p>yum &#8211; Yellowdog Updater Modified</p>
<h2>Synopsis</h2>
<p><code>yum</code> [options] [command] [package &#8230;]</p>
<h2>Description</h2>
<p><code>yum</code> is an interactive, rpm based, package manager. It can automatically perform system updates, including dependency analysis and obsolete processing based on &quot;repository&quot; metadata. It can also perform installation of new packages, removal of old packages and perform queries on the installed and/or available packages among many other commands/services (see below). <code>yum</code> is similar to other high level package managers like apt-get and smart. While there are some graphical interfaces directly to the <code>yum</code> code, more recent graphical interface development is happening with PackageKit and the gnome-packagekit application. <i>command</i> is one of:<br />
 <i></i> * install package1 [package2] [&#8230;]<br />
 <i></i> * update [package1] [package2] [&#8230;]<br />
 <i></i> * update-to [package1] [package2] [&#8230;]<br />
 <i></i> * update-minimal [package1] [package2] [&#8230;]<br />
 <i></i> * check-update<br />
 <i></i> * upgrade [package1] [package2] [&#8230;]<br />
 <i></i> * upgrade-to [package1] [package2] [&#8230;]<br />
 <i></i> * distribution-synchronization [package1] [package2] [&#8230;]<br />
 <i></i> * remove | erase package1 [package2] [&#8230;]<br />
 <i></i> * autoremove [package1] [&#8230;]<br />
 <i></i> * list [&#8230;]<br />
 <i></i> * info [&#8230;]<br />
 <i></i> * provides | whatprovides feature1 [feature2] [&#8230;]<br />
 <i></i> * clean [ packages | metadata | expire-cache | rpmdb | plugins | all ]<br />
 <i></i> * makecache [fast]<br />
 <i></i> * groups [&#8230;]<br />
 <i></i> * search string1 [string2] [&#8230;]<br />
 <i></i> * shell [filename]<br />
 <i></i> * resolvedep dep1 [dep2] [&#8230;]<br />
&nbsp;<wbr>(maintained for legacy reasons only &#8211; use repoquery or yum provides)<br />
 <i></i> * localinstall rpmfile1 [rpmfile2] [&#8230;]<br />
&nbsp;<wbr>(maintained for legacy reasons only &#8211; use install)<br />
 <i></i> * localupdate rpmfile1 [rpmfile2] [&#8230;]<br />
&nbsp;<wbr>(maintained for legacy reasons only &#8211; use update)<br />
 <i></i> * reinstall package1 [package2] [&#8230;]<br />
 <i></i> * downgrade package1 [package2] [&#8230;]<br />
 <i></i> * deplist package1 [package2] [&#8230;]<br />
 <i></i> * repolist [all|enabled|disabled]<br />
 <i></i> * repoinfo [all|enabled|disabled]<br />
 <i></i> * repository-packages &lt;enabled-repoid&gt; &lt;install|remove|remove-or-reinstall|remove-or-distribution-synchronization&gt; [package2] [&#8230;]<br />
 <i></i> * version [ all | installed | available | group-* | nogroups* | grouplist | groupinfo ]<br />
 <i></i> * history [info|list|packages-list|packages-info|summary|addon-info|redo|undo|rollback|new|sync|stats]<br />
 <i></i> * load-transaction [txfile]<br />
 <i></i> * updateinfo [summary | list | info | remove-pkgs-ts | exclude-updates | exclude-all | check-running-kernel]<br />
 <i></i> * fssnapshot [summary | list | have-space | create | delete]<br />
 <i></i> * fs [filters | refilter | refilter-cleanup | du]<br />
 <i></i> * check<br />
 <i></i> * help [command]<br />
 Unless the &#8211;help or -h option is given, one of the above commands must be present. Repository configuration is honored in all operations.</p>
<dl>
<dt><code>install</code></p>
<dd>Is used to install the latest version of a package or group of packages while ensuring that all dependencies are satisfied. (See <code>Specifying package names</code> for more information) If no package matches the given package name(s), they are assumed to be a shell glob and any matches are then installed. If the name starts with @^ then it is treated as an environment group (group install @^foo), an @ character and it&#8217;s treated as a group (plain group install). If the name starts with a &quot;-&quot; character, then a search is done within the transaction and any matches are removed. Note that Yum options use the same syntax and it may be necessary to use &quot;&#8211;&quot; to resolve any possible conflicts. If the name is a file, then install works like localinstall. If the name doesn&#8217;t match a package, then package &quot;provides&quot; are searched (e.g. &quot;_sqlitecache.so()(64bit)&quot;) as are filelists (Eg. &quot;/usr/bin/yum&quot;). Also note that for filelists, wildcards will match multiple packages. Because install does a lot of work to make it as easy as possible to use, there are also a few specific install commands &quot;<code>install-n</code>&quot;, &quot;<code>install-na</code>&quot; and &quot;<code>install-nevra</code>&quot;. These only work on package names, and do not process wildcards etc.</p>
<dd>
<dt><code>update</code></p>
<dd>If run without any packages, update will update every currently installed package. If one or more packages or package globs are specified, Yum will only update the listed packages. While updating packages, <code>yum</code> will ensure that all dependencies are satisfied. (See <code>Specifying package names</code> for more information) If the packages or globs specified match to packages which are not currently installed then update will not install them. update operates on groups, files, provides and filelists just like the &quot;install&quot; command. If the main obsoletes configure option is true (default) or the &#8211;obsoletes flag is present <code>yum</code> will include package obsoletes in its calculations &#8211; this makes it better for distro-version changes, for example: upgrading from somelinux 8.0 to somelinux 9. Note that &quot;<code>update</code>&quot; works on installed packages first, and only if there are no matches does it look for available packages. The difference is most noticeable when you do &quot;<code>update</code> foo-1-2&quot; which will act exactly as &quot;<code>update</code> foo&quot; if foo-1-2 is installed. You can use the &quot;<code>update-to</code>&quot; if you&#8217;d prefer that nothing happen in the above case.</p>
<dd>
<dt><code>update-to</code></p>
<dd>This command works like &quot;<code>update</code>&quot; but always specifies the version of the package we want to update to.</p>
<dd>
<dt><code>update-minimal</code></p>
<dd>This works like the update command, but if you have the package foo-1 installed and have foo-2 (bugfix) and foo-3 (enhancement) available with updateinfo.xml then update-minimal &#8211;bugfix will update you to foo-2.</p>
<dd>
<dt><code>check-update</code></p>
<dd>Implemented so you could know if your machine had any updates that needed to be applied without running it interactively. Returns exit value of 100 if there are packages available for an update. Also returns a list of the packages to be updated in list format. Returns 0 if no packages are available for update. Returns 1 if an error occurred. Running in verbose mode also shows obsoletes.</p>
<dd>
<dt><code>upgrade</code></p>
<dd>Is the same as the update command with the &#8211;obsoletes flag set. See update for more details.</p>
<dd>
<dt><code>upgrade-to</code></p>
<dd>This command works like &quot;<code>upgrade</code>&quot; but always specifies the version of the package we want to update to.</p>
<dd>
<dt><code>distribution-synchronization</code> or <code>distro-sync</code></p>
<dd>Synchronizes the installed package set with the latest packages available, this is done by either obsoleting, upgrading or downgrading as appropriate. This will &quot;normally&quot; do the same thing as the upgrade command however if you have the package FOO installed at version 4, and the latest available is only version 3, then this command will <code>downgrade</code> FOO to version 3. If you give the optional argument &quot;full&quot;, then the command will also reinstall packages where the install checksum and the available checksum do not match. And remove old packages (can be used to sync. rpmdb versions). The optional argument &quot;different&quot; can be used to specify the default operation. This command does not perform operations on groups, local packages or negative selections.</p>
<dd>
<dt><code>remove</code> or <code>erase</code></p>
<dd>Are used to remove the specified packages from the system as well as removing any packages which depend on the package being removed. remove operates on groups, files, provides and filelists just like the &quot;install&quot; command.(See <code>Specifying package names</code> for more information) Note that &quot;yum&quot; is included in the protected_packages configuration, by default. So you can&#8217;t accidentally remove yum itself. The remove_leaf_only configuration changes the behaviour of this command to only remove packages which aren&#8217;t required by something else. The clean_requirements_on_remove configuration changes the behaviour of this command to also remove packages that are only dependencies of this package. Because remove does a lot of work to make it as easy as possible to use, there are also a few specific remove commands &quot;<code>remove-n</code>&quot;, &quot;<code>remove-na</code>&quot; and &quot;<code>remove-nevra</code>&quot;. These only work on package names, and do not process wildcards etc.</p>
<dd>
<dt><code>autoremove</code></p>
<dd>
<dd>With one or more arguments this command works like running the &quot;<code>remove</code>&quot; command with the clean_requirements_on_remove turned on. However you can also specify no arguments, at which point it tries to remove any packages that weren&#8217;t installed explicitly by the user and which aren&#8217;t required by anything (so called leaf packages). Because autoremove does a lot of work to make it as easy as possible to use, there are also a few specific autoremove commands &quot;<code>autoremove-n</code>&quot;, &quot;<code>autoremove-na</code>&quot; and &quot;<code>autoremove-nevra</code>&quot;. These only work on package names, and do not process wildcards etc.</p>
<dt><code>list</code></p>
<dd>Is used to list various information about available packages; more complete details are available in the <i>List Options</i> section below.</p>
<dd>
<dt><code>provides</code> or <code>whatprovides</code></p>
<dd>Is used to find out which package provides some feature or file. Just use a specific name or a file-glob-syntax wildcards to list the packages available or installed that provide that feature or file.</p>
<dd>
<dt><code>search</code></p>
<dd>This is used to find packages when you know something about the package but aren&#8217;t sure of it&#8217;s name. By default search will try searching just package names and summaries, but if that &quot;fails&quot; it will then try descriptions and url. Yum search orders the results so that those packages matching more terms will appear first. You can force searching everything by specifying &quot;all&quot; as the first argument.</p>
<dd>
<dt><code>info</code></p>
<dd>Is used to list a description and summary information about available packages; takes the same arguments as in the <i>List Options</i> section below.</p>
<dd>
<dt><code>clean</code></p>
<dd>Is used to clean up various things which accumulate in the <code>yum</code> cache directory over time. More complete details can be found in the <i>Clean Options</i> section below.</p>
<dd>
<dt><code>makecache</code></p>
<dd>Is used to download and make usable all the metadata for the currently enabled <code>yum</code> repos. If the argument &quot;fast&quot; is passed, then we just try to make sure the repos. are current (much like &quot;yum clean expire-cache&quot;).</p>
<dd>
<dt><code>groups</code></p>
<dd>A command, new in 3.4.2, that collects all the subcommands that act on groups together. Note that recent yum using distributions (Fedora-19+, RHEL-7+) have configured group_command=objects which changes how group commands act in some important ways. &quot;<code>group install</code>&quot; is used to install all of the individual packages in a group, of the specified types (this works as if you&#8217;d taken each of those package names and put them on the command line for a &quot;yum install&quot; command).<br />
&nbsp;<wbr>The group_package_types configuration option specifies which types will be installed.<br />
&nbsp;<wbr>If you wish to&nbsp;<wbr>&quot;reinstall&quot;&nbsp;<wbr>a group so that you get a package that is currently blacklisted the easiest way to do that currently is to install the package manually and then run &quot;groups mark packages-sync mygroup mypackagename&quot; (or use yumdb to set the group_member of the package(s)). &quot;<code>group update</code>&quot; is just an alias for group install, when using group_command=compat. This will install packages in the group not already installed and upgrade existing packages. With group_command=simple it will just upgrade already installed packages. With group_command=objects it will try to upgrade the group object, installing any available packages not blacklisted (marked &#8216;-&#8216; in group info) and will upgrade the installed packages. &quot;<code>group list</code>&quot; is used to list the available groups from all <code>yum</code> repos. When group_command=objects the group is installed if the user explicitly installed it (or used the group mark* commands to mark it installed). It does not need to have any packages installed. When not using group_command=objects groups are shown as &quot;installed&quot; if all mandatory packages are installed, or if a group doesn&#8217;t have any mandatory packages then it is installed if any of the optional or default package are installed (when not in group_command=objects mode). You can pass optional arguments to the list/summary commands: installed, available, environment, language, packages, hidden and ids (or any of those prefixed by &quot;no&quot; to turn them off again). Note that groups that are available but hidden will not be listed unless &#8216;hidden&#8217; keyword is passed to the command. If you pass the -v option, to enable verbose mode, then the groupids are displayed by default (but &quot;yum group list ids&quot; is often easier to read). &quot;<code>group remove</code>&quot; is used to remove all of the packages in a group, unlike &quot;groupinstall&quot; this will remove everything regardless of group_package_types. It is worth pointing out that packages can be in more than one group, so &quot;group install X Y&quot; followed by &quot;group remove Y&quot; does not do give you the same result as &quot;group install X&quot;. The groupremove_leaf_only configuration changes the behaviour of this command to only remove packages which aren&#8217;t required by something else. &quot;<code>group info</code>&quot; is used to give the description and package list of a group (and which type those packages are marked as). Note that you can use the yum-filter-data and yum-list-data plugins to get/use the data the other way around (i.e. what groups own packages need updating). If you pass the -v option, to enable verbose mode, then the package names are matched against installed/available packages similar to the list command. When using group_command=objects, the info command will display markers next to each package saying how that package relates to the group object. The meaning of these markers is: </p>
<pre><code>&quot;-&quot; = Package isn't installed, and won't be installed as part of the group (Eg.  &quot;yum group install foo -pkgA&quot; or &quot;yum group install foo; yum remove pkgA&quot; … this will have pkgA marked as '-')

&quot;+&quot; = Package isn't installed, but will be the next time you run &quot;yum upgrade&quot; or &quot;yum group upgrade foo&quot;

&quot; &quot; = Package is installed, but wasn't installed via the group (so &quot;group remove foo&quot; won't remove it).

&quot;=&quot; = Package is installed, and was installed via the group.</code></pre>
<p> you can move an installed package into an installed group using either &quot;group mark package-sync/package-sync-forced&quot; or &quot;yumdb set group_member&quot;. &quot;<code>group summary</code>&quot; is used to give a quick summary of how many groups are installed and available. &quot;<code>group mark</code>&quot; and &quot;<code>group unmark</code>&quot; are used when groups are configured in group_command=objects mode. These commands then allow you to alter yum&#8217;s idea of which groups are installed, and the packages that belong to them. &quot;<code>group mark install</code>&quot; mark the group as installed. When installed &quot;<code>yum upgrade</code>&quot; and &quot;<code>yum group upgrade</code>&quot; will install new packages for the group (only those packages already installed will be marked as members of the installed group to start with). &quot;<code>group mark remove</code>&quot; the opposite of mark install. &quot;<code>group mark packages</code>&quot; takes a group id (which must be installed) and marks any given installed packages (which aren&#8217;t members of a group) as members of the group. Note that the data from the repositories does not need to specify the packages as a member of the group. &quot;<code>group mark packages-force</code>&quot; works like mark packages, but doesn&#8217;t care if the packages are already members of another group. &quot;<code>group mark blacklist</code>&quot; will blacklist all packages marked to be installed for a group. After this command a &quot;yum group upgrade&quot; will not install any new packages as part of the group. &quot;<code>group mark convert-blacklist</code>&quot; &quot;<code>group mark convert-whitelist</code>&quot; &quot;<code>group mark convert</code>&quot; converts the automatic data you get without using groups as objects into groups as objects data, in other words this will make &quot;yum &#8211;setopt=group_command=objects groups list&quot; look as similar as possible to the current output of &quot;yum &#8211;setopt=group_command=simple groups list&quot;. This makes it much easier to convert to groups as objects without having to reinstall. For groups that are installed the whitelist variant will mark all uninstalled packages for the group as to be installed on the next &quot;yum group upgrade&quot;, the blacklist variant (current default) will mark them all as blacklisted. &quot;<code>group unmark packages</code>&quot; remove a package as a member from any groups.</p>
<dd>
<dt><code>shell</code></p>
<dd>Is used to enter the &#8216;yum shell&#8217;, when a filename is specified the contents of that file is executed in yum shell mode. See <i><a href="/docs/linux/man/8-yum-shell/">yum-shell</a>(8)</i> for more info.</p>
<dd>
<dt><code>resolvedep</code></p>
<dd>Is used to list packages providing the specified dependencies, at most one package is listed per dependency. This command is maintained for legacy reasons only, use repoquery instead.</p>
<dd>
<dt><code>localinstall</code></p>
<dd>Is used to install a set of local rpm files. If required the enabled repositories will be used to resolve dependencies. Note that the install command will do a local install, if given a filename. This command is maintained for legacy reasons only.</p>
<dd>
<dt><code>localupdate</code></p>
<dd>Is used to update the system by specifying local rpm files. Only the specified rpm files of which an older version is already installed will be installed, the remaining specified packages will be ignored. If required the enabled repositories will be used to resolve dependencies. Note that the update command will do a local update, if given a filename. This command is maintained for legacy reasons only.</p>
<dd>
<dt><code>reinstall</code></p>
<dd>Will reinstall the identically versioned package as is currently installed. This does not work for &quot;installonly&quot; packages, like Kernels. reinstall operates on groups, files, provides and filelists just like the &quot;install&quot; command.</p>
<dd>
<dt><code>downgrade</code></p>
<dd>Will try and downgrade a package from the version currently installed to the previously highest version (or the specified version). The depsolver will not necessarily work, but if you specify all the packages it should work (thus, all the simple cases will work). Also this does not work for &quot;installonly&quot; packages, like Kernels. downgrade operates on groups, files, provides, filelists and rpm files just like the &quot;install&quot; command.</p>
<dd>
<dt><code>swap</code></p>
<dd>At it&#8217;s simplest this is just a simpler way to remove one set of package(s) and install another set of package(s) without having to use the &quot;shell&quot; command. However you can specify different commands to call than just remove or install, and you can list multiple packages (it splits using the &quot;&#8211;&quot; marker). Note that option parsing will remove the first &quot;&#8211;&quot; in an argument list on the command line. Examples: </p>
<pre>swap foo bar
swap -- remove foo -- install bar
swap foo group install bar-grp
swap -- group remove foo-grp -- group install bar-grp</pre>
<dd>
<dt><code>deplist</code></p>
<dd>Produces a list of all dependencies and what packages provide those dependencies for the given packages. As of 3.2.30 it now just shows the latest version of each package that matches (this can be changed by using &#8211;showduplicates) and it only shows the newest providers (which can be changed by using &#8211;verbose).</p>
<dd>
<dt><code>repolist</code></p>
<dd>Produces a list of configured repositories. The default is to list all enabled repositories. If you pass -v, for verbose mode, or use repoinfo then more information is listed. If the first argument is &#8216;enabled&#8217;, &#8216;disabled&#8217; or &#8216;all&#8217; then the command will list those types of repos. You can pass repo id or name arguments, or wildcards which to match against both of those. However if the id or name matches exactly then the repo will be listed even if you are listing enabled repos. and it is disabled. In non-verbose mode the first column will start with a &#8216;*&#8217; if the repo. has metalink data and the latest metadata is not local and will start with a &#8216;!&#8217; if the repo. has metadata that is expired. For non-verbose mode the last column will also display the number of packages in the repo. and (if there are any user specified excludes) the number of packages excluded. One last special feature of repolist, is that if you are in non-verbose mode then yum will ignore any repo errors and output the information it can get (Eg. &quot;yum clean all; yum -C repolist&quot; will output something, although the package counts/etc. will be zeroed out).</p>
<dd>
<dt><code>repoinfo</code></p>
<dd>
<dd>This command works exactly like repolist -v.</p>
<dd>
<dt><code>repository-packages</code></p>
<dd>Treat a repo. as a collection of packages (like &quot;yum groups&quot;) allowing the user to install or remove them as a single entity. &quot;repository-packages &lt;repo&gt; list&quot; &#8211; Works like the &quot;yum list&quot; command, but only shows packages from the given repository. &quot;repository-packages &lt;repo&gt; info&quot; &#8211; Works like the &quot;yum info&quot; command, but only shows packages from the given repository. &quot;repository-packages &lt;repo&gt; check-update&quot; &#8211; Works like the &quot;yum check-update&quot; command, but only shows packages from the given repository. &quot;repository-packages &lt;repo&gt; install&quot; &#8211; Install all of the packages in the repository, basically the same as: yum install $(repoquery &#8211;repoid=&lt;repo&gt; -a). Specific packages/wildcards can be specified. &quot;repository-packages &lt;repo&gt; upgrade&quot; &#8211; Update all of the packages in the repository, basically the same as: yum upgrade $(repoquery &#8211;repoid=&lt;repo&gt; -a). Specific packages/wildcards can be specified. &quot;repository-packages &lt;repo&gt; upgrade-to&quot; &#8211; Update all of the packages in the repository, basically the same as: yum upgrade $(repoquery &#8211;repoid=&lt;repo&gt; -a). Without arguments it works the same as upgrade, with arguments it just interprets them as the versions you want to move to. &quot;repository-packages &lt;repo&gt; reinstall-old&quot; &#8211; ReInstall all of the packages that are installed from the repository and available in the repository, similar to: yum reinstall $(yumdb search-quiet from_repo &lt;repo&gt;). &quot;repository-packages &lt;repo&gt; move-to&quot; &#8211; ReInstall all of the packages that are available in the repository, basically the same as: yum reinstall $(repoquery &#8211;repoid=&lt;repo&gt; -a). &quot;repository-packages &lt;repo&gt; reinstall&quot; &#8211; Tries to do reinstall-old, but if that produces no packages then tries move-to. &quot;repo-pkgs &lt;repo&gt; remove&quot; &#8211; Remove all of the packages in the repository, very similar to: yum remove $(repoquery &#8211;repoid=&lt;repo&gt; -a). However the repopkgsremove_leaf_only option is obeyed. &quot;repo-pkgs &lt;repo&gt; remove-or-reinstall&quot; &#8211; Works like remove for any package that doesn&#8217;t have the exact same version in another repository. For any package that does have the exact NEVRA in another repository then that version will be reinstalled. &quot;repo-pkgs &lt;repo&gt; remove-or-distro-sync&quot; &#8211; Works like remove for any package that doesn&#8217;t exist in another repository. For any package that does exist it tries to work as if distro-sync was called (with the repo. disabled).</p>
<dd>
<dt><code>version</code></p>
<dd>Produces a &quot;version&quot; of the rpmdb, and of the enabled repositories if &quot;all&quot; is given as the first argument. You can also specify version groups in the version-groups configuration file. If you pass -v, for verbose mode, more information is listed. The version is calculated by taking an SHA1 hash of the packages (in sorted order), and the checksum_type/checksum_data entries from the yumdb. Note that this rpmdb version is now also used significantly within yum (esp. in yum history). The version command will now show &quot;groups&quot; of packages as a separate version, and so takes sub-commands: &quot;version grouplist&quot; &#8211; List the defined version groups. &quot;version groupinfo&quot; &#8211; Get the complete list of packages within one or more version groups. &quot;version installed&quot; &#8211; This is the default, only show the version information for installed packages. &quot;version available&quot; &#8211; Only show the version information for available packages. &quot;version all&quot; &#8211; Show the version information for installed and available packages. &quot;version nogroups | nogroups-*&quot; &#8211; Just show the main version information. &quot;version group-*&quot; &#8211; Just show the grouped version information, if more arguments are given then only show the data for those groups.</p>
<dd>
<dt><code>history</code></p>
<dd>The history command allows the user to view what has happened in past transactions (assuming the history_record config. option is set). You can use info/list/packages-list/packages-info/summary to view what happened, undo/redo/rollback to act on that information and new to start a new history file. The info/list/summary commands take either a transaction id or a package (with wildcards, as in <code>Specifying package names</code>), all three can also be passed no arguments. list can be passed the keyword &quot;all&quot; to list all the transactions. The info command can also take ranges of transaction ids, of the form start..end, which will then display a merged history as if all the transactions in the range had happened at once.<br />
 Eg. &quot;history info 1..4&quot; will merge the first four transactions and display them as a single transaction. The packages-list/packages-info commands takes a package (with wildcards, as in <code>Specifying package names</code>). And show data from the point of view of that package. The undo/redo/rollback commands take either a single transaction id or the keyword last and an offset from the last transaction (Eg. if you&#8217;ve done 250 transactions, &quot;last&quot; refers to transaction 250, and &quot;last-4&quot; refers to transaction 246). The redo command can also take some optional arguments before you specify the transaction. &quot;force-reinstall&quot; tells it reinstall any packages that were installed in that transaction (via install, upgrade or downgrade). &quot;force-remove&quot; tells it to forcibly remove any packages that were updated or downgraded. The undo/redo commands act on the specified transaction, undo&#8217;ing or repeating the work of that transaction. While the rollback command will undo all transactions up to the point of the specified transaction. For example, if you have 3 transactions, where package A; B and C where installed respectively. Then &quot;undo 1&quot; will try to remove package A, &quot;redo 1&quot; will try to install package A (if it is not still installed), and &quot;rollback 1&quot; will try to remove packages B and C. Note that after a &quot;rollback 1&quot; you will have a fourth transaction, although the ending rpmdb version (see: yum version) should be the same in transactions 1 and 4. The addon-info command takes a transaction ID, and the packages-list command takes a package (with wildcards). The stats command shows some statistics about the current history DB. The sync commands allows you to change the rpmdb/yumdb data stored for any installed packages, to whatever is in the current rpmdb/yumdb (this is mostly useful when this data was not stored when the package went into the history DB). In &quot;history list&quot; you can change the behaviour of the 2nd column via the configuration option history_list_view. In &quot;history list&quot; output the Altered column also gives some extra information if there was something not good with the transaction (this is also shown at the end of the package column in the packages-list command).<br />
 <i></i><code>&gt;</code> &#8211; The rpmdb was changed, outside yum, after the transaction.<br />
 <i></i><code>&lt;</code> &#8211; The rpmdb was changed, outside yum, before the transaction.<br />
 <i></i><code>*</code> &#8211; The transaction aborted before completion.<br />
 <i></i><code>#</code> &#8211; The transaction completed, but with a non-zero status.<br />
 <i></i><code>E</code> &#8211; The transaction completed fine, but had warning/error output during the transaction.<br />
 <i></i><code>P</code> &#8211; The transaction completed fine, but problems already existed in the rpmdb.<br />
 <i></i><code>s</code> &#8211; The transaction completed fine, but &#8211;skip-broken was enabled and had to skip some packages. </p>
<dd>
<dt><code>load-transaction</code></p>
<dd>This command will re-load a saved yum transaction file, this allows you to run a transaction on one machine and then use it on another. The two common ways to get a saved yum transaction file are from &quot;yum -q history addon-info last saved_tx&quot; or via the automatic saves in $TMPDIR/yum_save_tx.* when a transaction is solved but not run. Running the command without an argument, or a directory as an argument will try and list the possible files available to load. Showing if the packages are still available, if the rpmdb matches the current rpmdb, how many transaction install/removes members are in the saved transaction and what the filename is.</p>
<dd>
<dt><code>updateinfo</code></p>
<dd>This command has a bunch of sub-commands to act on the updateinfo in the repositories. The simplest commands are:<br />
 <i></i> yum updateinfo info [all | available | installed | updates]<br />
 <i></i> yum updateinfo list [all | available | installed | updates]<br />
 <i></i> yum updateinfo [summary] [all | available | installed | updates]<br />
 which all display information about the available update information relevant to your machine (including anything installed, if you supply &quot;all&quot;). </p>
<p> <i></i> <code>* updates</code> Is used to display information about advisories for packages that can be updated. This is the default.<br />
 <i></i> <code>* installed</code> Is used to display information only about installed advisories.<br />
 <i></i> <code>* available</code> Is used to display information about advisories for packages available for updating or installation.<br />
 <i></i> <code>* all</code> Is used to display information about both installed and available advisories.<br />
 They all take as arguments: </p>
<p> <i></i> <code>* &lt;advisory&gt; [advisory&#8230;]</code> Is used to display information about one or more advisories.<br />
 <i></i> <code>* &lt;package&gt; [package&#8230;]</code> Is used to display information about one or more packages.<br />
 <i></i> <code>* bugzillas / bzs</code> Is the subset of the updateinfo information, pertaining to the bugzillas.<br />
 <i></i> <code>* cves</code> Is the subset of the updateinfo information, pertaining to the CVEs.<br />
 <i></i> <code>* enhancement</code> Is the subset of the updateinfo information, pertaining to enhancements.<br />
 <i></i> <code>* bugfix</code> Is the subset of the updateinfo information, pertaining to bugfixes.<br />
 <i></i> <code>* security / sec</code> Is the subset of the updateinfo information, pertaining to security.<br />
 <i></i> <code>* severity / sev</code> Include security relevant packages of this severity.<br />
 <i></i> <code>* recommended</code> Is the subset of the updateinfo information, pertaining to recommended updates.<br />
 <i></i> <code>* new-packages</code> Is the subset of the updateinfo information, pertaining to new packages. These are packages which weren&#8217;t available at the initial release of your distribution.<br />
 There are also three sub-commands to remove packages when using &quot;yum shell&quot;, they are:<br />
 <i></i> yum updateinfo remove-pkgs-ts<br />
 <i></i> yum updateinfo exclude-updates<br />
 <i></i> yum updateinfo exclude-all<br />
 they all take the following arguments: </p>
<pre><code>* [bzs=foo] [advisories=foo] [cves=foo] [security-severity=foo] [security] [bugfix]</code></pre>
<p> and finally there is a command to manually check the running kernel against updateinfo data:<br />
 <i></i> yum updateinfo check-running-kernel </p>
<dd>
<dt><code>fssnapshot</code> or <code>fssnap</code></p>
<dd>This command has a few sub-commands to act on the LVM data of the host, to list snapshots and to create and remove them. The simplest commands, to display information about the configured LVM snapshotable devices, are:<br />
 <i></i> yum fssnapshot [summary]<br />
 <i></i> yum fssnapshot list<br />
 <i></i> yum fssnapshot have-space<br />
 then you can create and delete snapshots using:<br />
 <i></i> yum fssnapshot create<br />
 <i></i> yum fssnapshot delete &lt;device(s)&gt; </p>
<p> Configuration Options: <code>fssnap_automatic_pre</code>, <code>fssnap_automatic_post</code>, <code>fssnap_automatic_keep</code>, <code>fssnap_percentage</code>, <code>fssnap_devices</code>, <code>fssnap_abort_on_errors</code></p>
<dd>
<dt><code>fs</code></p>
<dd>This command has a few sub-commands to act on the filesystem data of the host, mainly for removing languages/documentation for minimal installs:<br />
 <i></i> yum fs filters<br />
 <i></i> yum fs filter languages en:es<br />
 <i></i> yum fs filter documentation<br />
 <i></i> yum fs refilter [package(s)]<br />
 <i></i> yum fs refilter-cleanup [package(s)]<br />
 <i></i> yum fs du [path]<br />
 <i></i> yum fs status [path]<br />
 <i></i> yum fs diff [path] the first 3 being a simple interface to change yum.conf altering the tsflags and override_install_langs configurations. The refilter command is an optimized way of calling &quot;yum reinstall&quot; to reinstall the packages with the new filters applied. The refilter-cleanup command is needed because rpm doesn&#8217;t actually remove the files on reinstall, as it should. And the du/status/diff commands are included so you can easily see the space used/saved and any other changes.</p>
<dd>
<dt><code>check</code></p>
<dd>Checks the local rpmdb and produces information on any problems it finds. You can pass the check command the arguments &quot;dependencies&quot;, &quot;duplicates&quot;, &quot;obsoletes&quot; or &quot;provides&quot;, to limit the checking that is performed (the default is &quot;all&quot; which does all).</p>
<dd>
<dt><code>help</code></p>
<dd>Produces help, either for all commands or if given a command name then the help for that particular command.</p>
<dd></dl>
<h2>General Options</h2>
<p>Most command line options can be set using the configuration file as well and the descriptions indicate the necessary configuration option to set. </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Help; display a help message and then quit.</p>
<dt><code>-y, &#8211;assumeyes</code></p>
<dd>Assume yes; assume that the answer to any question which would be asked is yes.<br />
 Configuration Option: <code>assumeyes</code></p>
<dt><code>&#8211;assumeno</code></p>
<dd>Assume no; assume that the answer to any question which would be asked is no. This option overrides assumeyes, but is still subject to alwaysprompt.<br />
 Configuration Option: <code>assumeno</code></p>
<dt><code>-c, &#8211;config=[config file]</code></p>
<dd>Specifies the config file location &#8211; can take HTTP and FTP URLs and local file paths. </p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Run without output. Note that you likely also want to use -y. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Run with a lot of debugging output. </p>
<dt><code>-d, &#8211;debuglevel=[number]</code></p>
<dd>Sets the debugging level to [number] &#8211; turns up or down the amount of things that are printed. Practical range: 0 &#8211; 10<br />
 Configuration Option: <code>debuglevel</code></p>
<dt><code>-e, &#8211;errorlevel=[number]</code></p>
<dd>Sets the error level to [number] Practical range 0 &#8211; 10. 0 means print only critical errors about which you must be told. 1 means print all errors, even ones that are not overly important. 1+ means print more errors (if any) -e 0 is good for cron jobs.<br />
 Configuration Option: <code>errorlevel</code></p>
<dt><code>&#8211;rpmverbosity=[name]</code></p>
<dd>Sets the debug level to [name] for rpm scriptlets. &#8216;info&#8217; is the default, other options are: &#8216;critical&#8217;, &#8217;emergency&#8217;, &#8216;error&#8217;, &#8216;warn&#8217; and &#8216;debug&#8217;.<br />
 Configuration Option: <code>rpmverbosity</code></p>
<dt><code>-R, &#8211;randomwait=[time in minutes]</code></p>
<dd>Sets the maximum amount of time yum will wait before performing a command &#8211; it randomizes over the time.</p>
<dt><code>-C, &#8211;cacheonly</code></p>
<dd>Tells yum to run entirely from system cache &#8211; does not download or update any headers unless it has to to perform the requested action.</p>
<dt><code>&#8211;version</code></p>
<dd>Reports the <code>yum</code> version number and installed package versions for everything in history_record_packages (can be added to by plugins).</p>
<dt><code>&#8211;showduplicates</code></p>
<dd>Doesn&#8217;t limit packages to their latest versions in the info, list and search commands (will also affect plugins which use the doPackageLists() API).</p>
<dt><code>&#8211;installroot=root</code></p>
<dd>Specifies an alternative installroot, relative to which all packages will be installed. Think of this like doing &quot;chroot &lt;root&gt; yum&quot; except using &#8211;installroot allows yum to work before the chroot is created. Note: You may also want to use the option &#8211;releasever=/ when creating the installroot as otherwise the $releasever value is taken from the rpmdb within the installroot (and thus. will be empty, before creation).<br />
 Configuration Option: <code>installroot</code></p>
<dt><code>&#8211;enablerepo=repoidglob</code></p>
<dd>Enables specific repositories by id or glob that have been disabled in the configuration file using the enabled=0 option.<br />
 Configuration Option: <code>enabled</code></p>
<dt><code>&#8211;disablerepo=repoidglob</code></p>
<dd>Disables specific repositories by id or glob.<br />
 Configuration Option: <code>enabled</code></p>
<dt><code>&#8211;obsoletes</code></p>
<dd>This option only has affect for an update, it enables <code>yum</code>&#8216;s obsoletes processing logic. For more information see the <code>update</code> command above.<br />
 Configuration Option: <code>obsoletes</code></p>
<dt><code>-x, &#8211;exclude=package</code></p>
<dd>Exclude a specific package by name or glob from all repositories, so yum works as if that package was never in the repositories. This is commonly used so a package isn&#8217;t upgraded or installed accidentally, but can be used to remove packages in any way that &quot;yum list&quot; will show packages. </p>
<p> Can be disabled using &#8211;disableexcludes. Configuration Option: <code>exclude</code>, <code>includepkgs</code> </p>
<dt><code>&#8211;color=[always|auto|never]</code></p>
<dd>Display colorized output automatically, depending on the output terminal, always (using ANSI codes) or never. Note that some commands (Eg. list and info) will do a little extra work when color is enabled. Configuration Option: <code>color</code> </p>
<dt><code>&#8211;disableexcludes=[all|main|repoid]</code></p>
<dd>Disable the excludes defined in your config files. Takes one of three options:<br />
 all == disable all excludes<br />
 main == disable excludes defined in [main] in yum.conf<br />
 repoid == disable excludes defined for that repo </p>
<dt><code>&#8211;disableincludes=[all|repoid]</code></p>
<dd>Disable the includes defined in your config files. Takes one of two options:<br />
 all == disable all includes<br />
 repoid == disable includes defined for that repo </p>
<dt><code>&#8211;disableplugin=plugin</code></p>
<dd>Run with one or more plugins disabled, the argument is a comma separated list of wildcards to match against plugin names. </p>
<dt><code>&#8211;noplugins</code></p>
<dd>Run with all plugins disabled.<br />
 Configuration Option: <code>plugins</code></p>
<dt><code>&#8211;nogpgcheck</code></p>
<dd>Run with GPG signature checking disabled.<br />
 Configuration Option: <code>gpgcheck</code></p>
<dt><code>&#8211;skip-broken</code></p>
<dd>Resolve depsolve problems by removing packages that are causing problems from the transaction.<br />
 Configuration Option: <code>skip_broken</code> </p>
<dt><code>&#8211;releasever=version</code></p>
<dd>Pretend the current release version is the given string. This is very useful when combined with &#8211;installroot. You can also use &#8211;releasever=/ to take the releasever information from outside the installroot. Note that with the default upstream cachedir, of /var/cache/yum, using this option will corrupt your cache (and you can use $releasever in your cachedir configuration to stop this).</dl>
<dl>
<dt><code>-t, &#8211;tolerant</code></p>
<dd>This option makes yum go slower, checking for things that shouldn&#8217;t be possible making it more tolerant of external errors. </p>
<dt><code>&#8211;downloadonly</code></p>
<dd>Don&#8217;t update, just download. This is done in the background, so the yum lock is released for other operations. This can also be chosen by typing &#8216;d&#8217;ownloadonly at the transaction confirmation prompt. </p>
<dt><code>&#8211;downloaddir=directory</code></p>
<dd>Specifies an alternate directory to store packages. </p>
<dt><code>&#8211;setopt=option=value</code></p>
<dd>Set any config option in yum config or repo files. For options in the global config just use: &#8211;setopt=option=value for repo options use: &#8211;setopt=repoid.option=value</dl>
<dl>
<dt><code>&#8211;security</code></p>
<dd>This option includes packages that say they fix a security issue, in updates. </p>
<dt><code>&#8211;advisory=ADVS, &#8211;advisories=ADVS</code></p>
<dd>This option includes in updates packages corresponding to the advisory ID, Eg. FEDORA-2201-123.</p>
<dt><code>&#8211;bz=BZS</code></p>
<dd>This option includes in updates packages that say they fix a Bugzilla ID, Eg. 123.</p>
<dt><code>&#8211;cve=CVES</code></p>
<dd>This option includes in updates packages that say they fix a CVE &#8211; Common Vulnerabilities and Exposures ID (<a rel="nofollow" href="http://cve.mitre.org/about/">http://cve.mitre.org/about/</a>), Eg. CVE-2201-0123.</p>
<dt><code>&#8211;bugfix</code></p>
<dd>This option includes in updates packages that say they fix a bugfix issue.</p>
<dt><code>&#8211;sec-severity=SEVS, &#8211;secseverity=SEVS</code></p>
<dd>This option includes in updates security relevant packages of the specified severity. </p>
</dl>
<h2>List Options</h2>
<p>The following are the ways which you can invoke <code>yum</code> in list mode. Note that all <code>list</code> commands include information on the version of the package.</p>
<dl>
<dd>
<dt><code>OUTPUT</code></p>
<dd>The format of the output of yum list is: </p>
<p> name.arch [epoch:]version-release repo or @installed-from-repo </p>
<p> Note that if the repo cannot be determined, &quot;installed&quot; is printed instead. </p>
<dt><code>yum list [all | glob_exp1] [glob_exp2] [&#8230;]</code></p>
<dd>List all available and installed packages.</p>
<dt><code>yum list available [glob_exp1] [&#8230;]</code></p>
<dd>List all packages in the yum repositories available to be installed.</p>
<dd>
<dt><code>yum list updates [glob_exp1] [&#8230;]</code></p>
<dd>List all packages with updates available in the yum repositories.</p>
<dd>
<dt><code>yum list installed [glob_exp1] [&#8230;]</code></p>
<dd>List the packages specified by <i>args</i>. If an argument does not match the name of an available package, it is assumed to be a shell-style glob and any matches are printed.</p>
<dd>
<dt><code>yum list extras [glob_exp1] [&#8230;]</code></p>
<dd>List the packages installed on the system that are not available in any yum repository listed in the config file.</p>
<dd>
<dt><code>yum list distro-extras [glob_exp1] [&#8230;]</code></p>
<dd>List the packages installed on the system that are not available, by name, in any yum repository listed in the config file.</p>
<dd>
<dt><code>yum list obsoletes [glob_exp1] [&#8230;]</code></p>
<dd>List the packages installed on the system that are obsoleted by packages in any yum repository listed in the config file.</p>
<dd>
<dt><code>yum list recent</code></p>
<dd>List packages recently added into the repositories. This is often not helpful, but what you may really want to use is &quot;yum list-updateinfo new&quot; from the security yum plugin.</p>
<dd></dl>
<h2>Specifying Package Names</h2>
<p>A package can be referred to for install, update, remove, list, info etc with any of the following as well as globs of any of the following:</p>
<dl>
<dd><code>name</code><br />
 <code>name.arch</code><br />
 <code>name-ver</code><br />
 <code>name-ver-rel</code><br />
 <code>name-ver-rel.arch</code><br />
 <code>name-epoch:ver-rel.arch</code><br />
 <code>epoch:name-ver-rel.arch</code></p>
<dd>For example: <code>yum remove kernel-2.4.1-10.i686</code><br />
&nbsp;<wbr>&nbsp;<wbr>this will remove this specific kernel-ver-rel.arch.</p>
<dd>Or: <code>yum list available &#8216;foo*&#8217;</code><br />
&nbsp;<wbr>&nbsp;<wbr>will list all available packages that match&nbsp;<wbr>&#8216;foo*&#8217;.&nbsp;<wbr>(The single quotes will keep your shell from expanding the globs.)</p>
<dd></dl>
<h2>Clean Options</h2>
<p>The following are the ways which you can invoke <code>yum</code> in clean mode. Note that &quot;all files&quot; in the commands below means &quot;all files in currently enabled repositories&quot;. If you want to also clean any (temporarily) disabled repositories you need to use <code>&#8211;enablerepo=&#8217;*&#8217;</code> option. </p>
<dl>
<dt><code>yum clean expire-cache</code></p>
<dd>Eliminate the local data saying when the metadata and mirrorlists were downloaded for each repo. This means yum will revalidate the cache for each repo. next time it is used. However if the cache is still valid, nothing significant was deleted. </p>
<dt><code>yum clean packages</code></p>
<dd>Eliminate any cached packages from the system. Note that packages are not automatically deleted after they are downloaded. </p>
<dt><code>yum clean headers</code></p>
<dd>Eliminate all of the header files, which old versions of yum used for dependency resolution. </p>
<dt><code>yum clean metadata</code></p>
<dd>Eliminate all of the files which yum uses to determine the remote availability of packages. Using this option will force yum to download all the metadata the next time it is run. </p>
<dt><code>yum clean dbcache</code></p>
<dd>Eliminate the sqlite cache used for faster access to metadata. Using this option will force yum to download the sqlite metadata the next time it is run, or recreate the sqlite metadata if using an older repo. </p>
<dt><code>yum clean rpmdb</code></p>
<dd>Eliminate any cached data from the local rpmdb. </p>
<dt><code>yum clean plugins</code></p>
<dd>Tell any enabled plugins to eliminate their cached data. </p>
<dt><code>yum clean all</code></p>
<dd>Does all of the above. </p>
</dl>
<h2>Examples</h2>
<p>To list all updates that are security relevant, and get a return code on whether there are security updates use:</p>
<dl>
<dd>yum &#8211;security check-update</dl>
<p> To upgrade packages that have security errata (upgrades to the latest available package) use:</p>
<dl>
<dd>yum &#8211;security update</dl>
<p> To upgrade packages that have security errata (upgrades to the last security errata package) use:</p>
<dl>
<dd>yum &#8211;security update-minimal</dl>
<p> To get a list of all BZs that are fixed for packages you have installed use:</p>
<dl>
<dd>yum updateinfo list bugzillas</dl>
<p> To get a list of all security advisories, including the ones you have already installed use:</p>
<dl>
<dd>yum updateinfo list all security</dl>
<p> To get the information on advisory FEDORA-2707-4567 use:</p>
<dl>
<dd>yum updateinfo info FEDORA-2707-4567</dl>
<p> For Red Hat advisories, respin suffixes are also accepted in the ID, although they won&#8217;t have any effect on the actual respin selected by yum, as it will always select the latest one available. For example, if you use:</p>
<dl>
<dd>yum updateinfo info RHSA-2016:1234-2</dl>
<p> while RHSA-2016:1234-3 has been shipped already, yum will select the latter (provided your updateinfo.xml is current). The same would happen if you just specified RHSA-2016:1234. That said, there&#8217;s no need for you to specify or care about the suffix at all. To update packages to the latest version which contain fixes for Bugzillas 123, 456 and 789; and all security updates use:</p>
<dl>
<dd>yum &#8211;bz 123 &#8211;bz 456 &#8211;bz 789 &#8211;security update</dl>
<p> To update to the packages which just update Bugzillas 123, 456 and 789; and all security updates use:</p>
<dl>
<dd>yum &#8211;bz 123 &#8211;bz 456 &#8211;bz 789 &#8211;security update-minimal</dl>
<p> To get an info list of the latest packages which contain fixes for Bugzilla 123; CVEs CVE-2207-0123 and CVE-2207-3210; and Fedora advisories FEDORA-2707-4567 and FEDORA-2707-7654 use:</p>
<dl>
<dd>yum &#8211;bz 123 &#8211;cve CVE-2207-0123 &#8211;cve CVE-2207-3210 &#8211;advisory FEDORA-2707-4567 &#8211;advisory FEDORA-2707-7654 info updates</dl>
<p> To get a list of packages which are &quot;new&quot;.</p>
<dl>
<dd>yum updateinfo list new</dl>
<p> To get a summary of advisories you haven&#8217;t installed yet use:</p>
<dl>
<dd>yum updateinfo summary </p>
<h2>Plugins</h2>
<p>Yum can be extended through the use of plugins. A plugin is a Python &quot;.py&quot; file which is installed in one of the directories specified by the <code>pluginpath</code> option in yum.conf. For a plugin to work, the following conditions must be met: </p>
<p> 1. The plugin module file must be installed in the plugin path as just described. </p>
<p> 2. The global <code>plugins</code> option in /etc/yum.conf must be set to `1&#8242;. </p>
<p> 3. A configuration file for the plugin must exist in /etc/yum/pluginconf.d/&lt;plugin_name&gt;.conf and the <code>enabled</code> setting in this file must set to `1&#8242;. The minimal content for such a configuration file is:</p>
<dl>
<dd>[main]<br />
 enabled = 1</dl>
<p> See the <code><a href="/docs/linux/man/5-yum-conf/">yum.conf</a>(5)</code> man page for more information on plugin related configuration options.</p>
<h2>Files</h2>
<pre>/etc/yum.conf
/etc/yum/version-groups.conf
/etc/yum.repos.d/
/etc/yum/pluginconf.d/
/var/cache/yum/</pre>
<h2>See Also</h2>
<pre><i>pkcon (1)</i>
<i>yum.conf (5)</i>
<i>yum-updatesd (8)</i>
<i>package-cleanup (1)</i>
<i>repoquery (1)</i>
<i>yum-complete-transaction (1)</i>
<i>yumdownloader (1)</i>
<i>yum-utils (1)</i>
<i>yum-langpacks (1)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
<a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a>
yum search yum</pre>
<h2>Authors</h2>
<pre>See the Authors file included with this program.</pre>
<h2>Bugs</h2>
<p>There of course aren&#8217;t any bugs, but if you find any, you should first consult the FAQ mentioned above and then email the mailing list: yum [at] lists.baseurl.org or filed in bugzilla. </p>
