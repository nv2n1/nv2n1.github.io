---
title: "yum(5)"
name: "yum"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yum/"
description: "yum.conf – Configuration file for yum(8)."
---

<p><code>yum.conf</code> &#8211; Configuration file for <code><a href="/docs/linux/man/8-yum/">yum</a>(8)</code>.</p>
<h2>Description</h2>
<p>Yum uses a configuration file at <code>/etc/yum.conf</code>. Additional configuration files are also read from the directories set by the <code>reposdir</code> option (default is `/etc/yum.repos.d&#8217;). See the <code>reposdir</code> option below for further details. </p>
<h2>Parameters</h2>
<p>There are two types of sections in the yum configuration file(s): main and repository. Main defines all global configuration options. There should be only one main section. The repository section(s) define the configuration for each repository/server. There should be one or more repository sections.</p>
<h2>[main] OPTIONS</h2>
<p>The [main] section must exist for yum to do anything. It consists of the following options: </p>
<dl>
<dd><code>cachedir</code> Directory where yum should store its cache and db files. The default is `/var/cache/yum&#8217;. </p>
<dd><code>persistdir</code> Directory where yum should store information that should persist over multiple runs. The default is `/var/lib/yum&#8217;. </p>
<dd><code>keepcache</code> Either `1&#8242; or `0&#8242;. Determines whether or not yum keeps the cache of headers and packages after successful installation. Default is &#8216;1&#8217; (keep files) </p>
<dd><code>reposdir</code> A list of directories where yum should look for .repo files which define repositories to use. Default is `/etc/yum.repos.d&#8217;. Each file in this directory should contain one or more repository sections as documented in <code>[repository] options</code> below. These will be merged with the repositories defined in /etc/yum.conf to form the complete set of repositories that yum will use. </p>
<dd><code>debuglevel</code> Debug message output level. Practical range is 0-10. Default is `2&#8242;. </p>
<dd><code>errorlevel</code> Error message output level. Practical range is 0-10. Default is `2&#8242;. </p>
<dd><code>rpmverbosity</code> Debug scriptlet output level. &#8216;info&#8217; is the default, other options are: &#8216;critical&#8217;, &#8217;emergency&#8217;, &#8216;error&#8217;, &#8216;warn&#8217; and &#8216;debug&#8217;. </p>
<dd><code>protected_packages</code> This is a list of packages that yum should never completely remove. They are protected via. Obsoletes as well as user/plugin removals. </p>
<p> The default is: yum glob:/etc/yum/protected.d/*.conf So any packages which should be protected can do so by including a file in /etc/yum/protected.d with their package name in it. </p>
<p> Also if this configuration is set to anything, then yum will protect the package corresponding to the running version of the kernel. </p>
<dd><code>protected_multilib</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not it should perform a check to make sure that multilib packages are the same version. For example, if this option is off (rpm behaviour) pkgA-1.x86_64 and pkgA-2.i386 can be installed at the same time. However this is very rarely desired. Install only packages, like the kernel, are exempt from this check. The default is `1&#8242;. </p>
<dd><code>logfile</code> Full directory and file name for where yum should write its log file. </p>
<dd><code>gpgcheck</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not it should perform a GPG signature check on packages. When this is set in the [main] section it sets the default for all repositories. The default is `0&#8242;. </p>
<p> <code>localpkg_gpgcheck</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not it should perform a GPG signature check on local packages (packages in a file, not in a repositoy). The default is `0&#8242;. </p>
<dd><code>repo_gpgcheck</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not it should perform a GPG signature check on the repodata. When this is set in the [main] section it sets the default for all repositories. The default is `0&#8242;. </p>
<dd><code>skip_broken</code> Either `1&#8242; or `0&#8242;. Resolve depsolve problems by removing packages that are causing problems from the transaction. </p>
<dd><code>assumeyes</code> Either `1&#8242; or `0&#8242;. Determines whether or not yum prompts for confirmation of critical actions. Default is `0&#8242; (do prompt).<br />
 Command-line option: <code>-y</code> <code>&#8211;assumeyes</code> </p>
<dd><code>assumeno</code> Either `1&#8242; or `0&#8242;. If yum would prompt for confirmation of critical actions, assume the user chose no. This is basically the same as doing &quot;echo | yum &#8230;&quot; but is a bit more usable. This option overrides <code>assumeyes</code>, but is still subject to <code>alwaysprompt</code>. Default is `0&#8242; (do prompt).<br />
 Command-line option: <code>&#8211;assumeno</code> </p>
<dd><code>alwaysprompt</code> Either `1&#8242; or `0&#8242;. Without this option, yum will not prompt for confirmation when the list of packages to be installed exactly matches those given on the command line. Unless <code>assumeyes</code> is enabled, it will still prompt when additional packages need to be installed to fulfill dependencies. Note that older versions of yum would also always prompt for package removal, and that is no longer true. Default is `1&#8242;. </p>
<dd><code>tolerant</code> Either `1&#8242; or `0&#8242;. If enabled, then yum will be tolerant of errors on the command line with regard to packages. For example: if you request to install foo, bar and baz and baz is installed; yum won&#8217;t error out complaining that baz is already installed. Default to `0&#8242; (not tolerant). Note: This option currently does nothing.<br />
 Command-line option: <code>-t</code> </p>
<dd><code>exclude</code> List of packages to exclude from updates or installs. This should be a space separated list. Shell globs using wildcards (eg. * and ?) are allowed. </p>
<dd><code>exactarch</code> Either `1&#8242; or `0&#8242;. Set to `1&#8242; to make yum update only update the architectures of packages that you have installed. ie: with this enabled yum will not install an i686 package to update an i386 package. Default is `1&#8242;. </p>
<dd><code>installonlypkgs </code> List of package provides that should only ever be installed, never updated. Kernels in particular fall into this category. Defaults to kernel, kernel-bigmem, kernel-enterprise, kernel-smp, kernel-modules, kernel-debug, kernel-unsupported, kernel-source, kernel-devel, kernel-PAE, kernel-PAE-debug. </p>
<p> Note that because these are provides, and not just package names, kernel-devel will also apply to kernel-debug-devel, etc. </p>
<dd><code>installonly_limit </code> Number of packages listed in installonlypkgs to keep installed at the same time. Setting to 0 disables this feature. Default is &#8216;0&#8217;. Note that this functionality used to be in the &quot;installonlyn&quot; plugin, where this option was altered via. tokeep. Note that as of version 3.2.24, yum will now look in the yumdb for a installonly attribute on installed packages. If that attribute is &quot;keep&quot;, then they will never be removed. </p>
<dd><code>kernelpkgnames </code> List of package names that are kernels. This is really only here for the updating of kernel packages and should be removed out in the yum 2.1 series. </p>
<dd><code>showdupesfromrepos</code> Either `0&#8242; or `1&#8242;. Set to `1&#8242; if you wish to show any duplicate packages from any repository, from package listings like the info or list commands. Set to `0&#8242; if you want only to see the newest packages from any repository. Default is `0&#8242;. </p>
<dd><code>obsoletes </code> This option only has affect during an <code>update</code>. It enables yum&#8217;s obsoletes processing logic. Useful when doing distribution level upgrades. See also the yum <code>upgrade</code> command documentation for more details (<a href="/docs/linux/man/8-yum/">yum</a>(8)). Default is `true&#8217;.<br />
 Command-line option: <code>&#8211;obsoletes</code> </p>
<dd><code>overwrite_groups </code> Either `0&#8242; or `1&#8242;. Used to determine yum&#8217;s behaviour if two or more repositories offer the package groups with the same name. If <code>overwrite_groups</code> is `1&#8242; then the group packages of the last matching repository will be used. If <code>overwrite_groups</code> is `0&#8242; then the groups from all matching repositories will be merged together as one large group. </p>
<dd><code>groupremove_leaf_only </code> Either `0&#8242; or `1&#8242;. Used to determine yum&#8217;s behaviour when the groupremove command is run. If <code>groupremove_leaf_only</code> is `0&#8242; (default) then all packages in the group will be removed. If <code>groupremove_leaf_only</code> is `1&#8242; then only those packages in the group that aren&#8217;t required by another package will be removed. </p>
<dd><code>enable_group_conditionals</code> Either `0&#8242; or `1&#8242;. Determines whether yum will allow the use of conditionals packages. Default is `1&#8242; (package conditionals are allowed). </p>
<dd><code>group_package_types</code> List of the following: optional, default, mandatory. Tells yum which type of packages in groups will be installed when &#8216;groupinstall&#8217; is called. Default is: default, mandatory </p>
<dd><code>group_command</code> List of the following: simple, compat, objects. Tells yum what to do for group install/upgrade/remove commands. </p>
<p> Simple acts like you did yum group cmd $(repoquery &#8211;group &#8211;list group), so it is vrery easy to reason about what will happen. Alas. this is often not what people want to happen. </p>
<p> Compat. works much like simple, except that when you run &quot;group upgrade&quot; it actually runs &quot;group install&quot; (this means that you get any new packages added to the group, but you also get packages added that were there before and you didn&#8217;t want). </p>
<p> Objects makes groups act like a real object, seperate from the packages they contain. Yum keeps track of the groups you have installed, so &quot;group upgrade&quot; will install new packages for the group but not install old ones. It also knows about group members that are installed but weren&#8217;t installed as part of the group, and won&#8217;t remove those on &quot;group remove&quot;. Running &quot;yum upgrade&quot; will also run &quot;yum group upgrade&quot; (thus. adding new packages for all groups). </p>
<p> Default is: compat </p>
<dd><code>installroot </code> Specifies an alternative installroot, relative to which all packages will be installed.<br />
 Command-line option: <code>&#8211;installroot</code> </p>
<dd><code>distroverpkg</code> The package used by yum to determine the &quot;version&quot; of the distribution. This can be any installed package. Default is `redhat-release&#8217;. You can see what provides this manually by using: &quot;yum whatprovides redhat-release&quot;. </p>
<dd><code>diskspacecheck</code> Either `0&#8242; or `1&#8242;. Set this to `0&#8242; to disable the checking for sufficient diskspace before a RPM transaction is run. Default is `1&#8242; (perform the check). </p>
<dd><code>tsflags</code> Comma or space separated list of transaction flags to pass to the rpm transaction set. These include &#8216;noscripts&#8217;, &#8216;notriggers&#8217;, &#8216;nodocs&#8217;, &#8216;test&#8217;, &#8216;justdb&#8217; and &#8216;nocontexts&#8217;. &#8216;repackage&#8217; is also available but that does nothing with newer rpm versions. You can set all/any of them. However, if you don&#8217;t know what these do in the context of an rpm transaction set you&#8217;re best leaving it alone. Default is an empty list. </p>
<dd><code>recent</code> Number of days back to look for `recent&#8217; packages added to a repository. Used by the <code>list recent</code> command. Default is `7&#8242;. </p>
<dd><code>retries</code> Set the number of times any attempt to retrieve a file should retry before returning an error. Setting this to `0&#8242; makes yum try forever. Default is `10&#8242;. </p>
<dd><code>keepalive </code> Either `0&#8242; or `1&#8242;. Set whether HTTP keepalive should be used for HTTP/1.1 servers that support it. This can improve transfer speeds by using one connection when downloading multiple files from a repository. Default is `1&#8242;. </p>
<dd><code>timeout </code> Number of seconds to wait for a connection before timing out. Defaults to 30 seconds. This may be too short of a time for extremely overloaded sites. </p>
<dd><code>http_caching</code> Determines how upstream HTTP caches are instructed to handle any HTTP downloads that Yum does. This option can take the following values: </p>
<p> `all&#8217; means that all HTTP downloads should be cached. </p>
<p> `packages&#8217; means that only RPM package downloads should be cached (but not repository metadata downloads). </p>
<p> `none&#8217; means that no HTTP downloads should be cached. </p>
<p> The default is `all&#8217;. This is recommended unless you are experiencing caching related issues. Try to at least use `packages&#8217; to minimize load on repository servers. </p>
<dd><code>throttle </code> Enable bandwidth throttling for downloads. This option can be expressed as a absolute data rate in bytes/sec. An SI prefix (k, M or G) may be appended to the bandwidth value (eg. `5.5k&#8217; is 5.5 kilobytes/sec, `2M&#8217; is 2 Megabytes/sec). </p>
<p> Alternatively, this option can specify the percentage of total bandwidth to use (eg. `60%&#8217;). In this case the <code>bandwidth</code> option should be used to specify the maximum available bandwidth. </p>
<p> Set to `0&#8242; to disable bandwidth throttling. This is the default. </p>
<dd><code>bandwidth </code> Use to specify the maximum available network bandwidth in bytes/second. Used with the <code>throttle</code> option (above). If <code>throttle</code> is a percentage and <code>bandwidth</code> is `0&#8242; then bandwidth throttling will be disabled. If <code>throttle</code> is expressed as a data rate (bytes/sec) then this option is ignored. Default is `0&#8242; (no bandwidth throttling). </p>
<dd><code>ip_resolve </code> Determines how yum resolves host names. </p>
<p> `4&#8242; or `IPv4&#8242;: resolve to IPv4 addresses only. </p>
<p> `6&#8242; or `IPv6&#8242;: resolve to IPv6 addresses only. </p>
<dd><code>max_connections </code> </p>
<p> The maximum number of simultaneous connections. This overrides the urlgrabber default of 5 connections. Note that there are also implicit per-mirror limits and the downloader honors these too. </p>
<dd><code>sslcacert </code> Path to the directory containing the databases of the certificate authorities yum should use to verify SSL certificates. Defaults to none &#8211; uses system default </p>
<dd><code>sslverify </code> Boolean &#8211; should yum verify SSL certificates/hosts at all. Defaults to True. </p>
<p> Note that the plugin yum-rhn-plugin will force this value to true, and may alter other ssl settings (like hostname checking), even if it the machine is not registered. </p>
<dd><code>sslclientcert </code> Path to the SSL client certificate yum should use to connect to repos/remote sites Defaults to none. </p>
<p> Note that if you are using curl compiled against NSS (default in Fedora/RHEL), curl treats sslclientcert values with the same basename as _identical_. This version of yum will check that this isn&#8217;t true and output an error when the repositories &quot;foo&quot; and &quot;bar&quot; violate this, like so: </p>
<p> sslclientcert basename shared between foo and bar </p>
<dd><code>sslclientkey </code> Path to the SSL client key yum should use to connect to repos/remote sites Defaults to none. </p>
<dd><code>ssl_check_cert_permissions </code> Boolean &#8211; Whether yum should check the permissions on the paths for the certificates on the repository (both remote and local). If we can&#8217;t read any of the files then yum will force skip_if_unavailable to be true. This is most useful for non-root processes which use yum on repos. that have client cert files which are readable only by root. Defaults to True. </p>
<dd><code>history_record </code> Boolean &#8211; should yum record history entries for transactions. This takes some disk space, and some extra time in the transactions. But it allows how to know a lot of information about what has happened before, and display it to the user with the history info/list/summary commands. yum also provides the history undo/redo commands. Defaults to True. </p>
<p> Note that if history is recorded, yum uses that information to see if any modifications to the rpmdb have been done outside of yum. These are always bad, from yum&#8217;s point of view, and so yum will issue a warning and automatically run some of &quot;yum check&quot; to try and find some of the worst problems altering the rpmdb might have caused.</p>
<dd>This means that turning this option off will stop yum from being able to detect when the rpmdb has changed and thus. it will never warn you or automatically run &quot;yum check&quot;. The problems will likely still be there, and yumdb etc. will still be wrong but yum will not warn you about it. </p>
<dd><code>history_record_packages </code> This is a list of package names that should be recorded as having helped the transaction. yum plugins have an API to add themselves to this, so it should not normally be necessary to add packages here. Not that this is also used for the packages to look for in &#8211;version. Defaults to rpm, yum, yum-metadata-parser. </p>
<dd><code>history_list_view </code> Which column of information to display in the &quot;yum history list&quot; command. There are currently three options: users, cmds (or commands), auto. </p>
<p> Older versions of yum acted like &quot;users&quot;, which always outputs the user who initiated the yum transaction. You can now specify &quot;commands&quot; which will instead always output the command line of the transaction. You can also specify &quot;single-user-commands&quot; which will display the users if there are more than one, otherwise it will display the command line. </p>
<p> You can also specify &quot;default&quot; which currently selects &quot;single-user-commands&quot;. </p>
<dd><code>commands</code> List of functional commands to run if no functional commands are specified on the command line (eg. &quot;update foo bar baz quux&quot;). None of the short options (eg. -y, -e, -d) are accepted for this option. </p>
<dd><code>syslog_ident </code> Identification (program name) for syslog messages. </p>
<dd><code>syslog_facility </code> Facility name for syslog messages, see <a href="/docs/linux/man/3-syslog/">syslog</a>(3). Default is `LOG_USER&#8217;. </p>
<dd><code>syslog_device </code> Where to log syslog messages. Can be a local device (path) or a host:port string to use a remote syslog. If empty or points to a nonexistent device, syslog logging is disabled. Default is `/dev/log&#8217;. </p>
<dd><code>proxy </code> URL to the proxy server that yum should use. </p>
<dd><code>proxy_username </code> username to use for proxy </p>
<dd><code>proxy_password </code> password for this proxy </p>
<dd><code>username </code> username to use for basic authentication to a repo or really any url. </p>
<dd><code>password </code> password to use with the username for basic authentication. </p>
<dd><code>plugins </code> Either `0&#8242; or `1&#8242;. Global switch to enable or disable yum plugins. Default is `0&#8242; (plugins disabled). See the <code>PLUGINS</code> section of the <code><a href="/docs/linux/man/8-yum/">yum</a>(8)</code> man for more information on installing yum plugins. </p>
<dd><code>pluginpath </code> A list of directories where yum should look for plugin modules. Default is `/usr/share/yum-plugins&#8217; and `/usr/lib/yum-plugins&#8217;. </p>
<dd><code>pluginconfpath </code> A list of directories where yum should look for plugin configuration files. Default is `/etc/yum/pluginconf.d&#8217;. </p>
<dd><code>metadata_expire </code> Time (in seconds) after which the metadata will expire. So that if the current metadata downloaded is less than this many seconds old then yum will not update the metadata against the repository. If you find that yum is not downloading information on updates as often as you would like lower the value of this option. You can also change from the default of using seconds to using days, hours or minutes by appending a d, h or m respectively. The default is 6 hours, to compliment yum-updatesd running once an hour. It&#8217;s also possible to use the word &quot;never&quot;, meaning that the metadata will never expire. Note that when using a metalink file the metalink must always be newer than the metadata for the repository, due to the validation, so this timeout also applies to the metalink file. </p>
<dd><code>mirrorlist_expire </code> Time (in seconds) after which the mirrorlist locally cached will expire. If the current mirrorlist is less than this many seconds old then yum will not download another copy of the mirrorlist, it has the same extra format as metadata_expire. If you find that yum is not downloading the mirrorlists as often as you would like lower the value of this option. </p>
<dd><code>mdpolicy </code> You can select from different metadata download policies depending on how much data you want to download with the main repository metadata index. The advantages of downloading more metadata with the index is that you can&#8217;t get into situations where you need to use that metadata later and the versions available aren&#8217;t compatible (or the user lacks privileges) and that if the metadata is corrupt in any way yum will revert to the previous metadata. </p>
<p> `instant&#8217; &#8211; Just download the new metadata index, this is roughly what yum always did, however it now does some checking on the index and reverts if it classifies it as bad. </p>
<p> `group:primary&#8217; &#8211; Download the primary metadata with the index. This contains most of the package information and so is almost always required anyway. This is the default. </p>
<p> `group:small&#8217; &#8211; With the primary also download the updateinfo metadata, this is required for yum-security operations and it also used in the graphical clients. This file also tends to be significantly smaller than most others. </p>
<p> `group:main&#8217; &#8211; With the primary and updateinfo download the filelists metadata and the group metadata. The filelists data is required for operations like &quot;yum install /bin/bash&quot;, and also some dependency resolutions require it. The group data is used in some graphical clients and for group operations like &quot;yum grouplist Base&quot;. </p>
<p> `group:all&#8217; &#8211; Download all metadata listed in the index, currently the only one not listed above is the other metadata, which contains the changelog information which is used by yum-changelog. This is what &quot;yum makecache&quot; uses. </p>
<dd><code>mddownloadpolicy </code> You can select which kinds of repodata you would prefer yum to download: </p>
<p> `sqlite&#8217; &#8211; Download the .sqlite files, if available. This is currently slightly faster, once they are downloaded. However these files tend to be bigger, and thus. take longer to download. </p>
<p> `sqlite&#8217; &#8211; Download the .XML files, which yum will do anyway as a fallback on the other options. These files tend to be smaller, but they require parsing/converting locally after download and some aditional checks are performed on them each time they are used. </p>
<dd><code>multilib_policy </code> Can be set to &#8216;all&#8217; or &#8216;best&#8217;. All means install all possible arches for any package you want to install. Therefore yum install foo will install foo.i386 and foo.x86_64 on x86_64, if it is available. Best means install the best arch for this platform, only. </p>
<dd><code>bugtracker_url </code> URL where bugs should be filed for yum. Configurable for local versions or distro-specific bugtrackers. </p>
<dd><code>color </code> Whether to display colorized output automatically, depending on the output terminal, can be changed to always (using ANSI codes) or never. Default is `auto&#8217;. Possible values are: auto, never, always. Command-line option: <code>&#8211;color</code> </p>
<dd><code>color_list_installed_older </code> The colorization/highlighting for packages in list/info installed which are older than the latest available package with the same name and arch. Default is `bold&#8217;. Possible values are a comma separated list containing: bold, blink, dim, reverse, underline, fg:black, fg:red, fg:green, fg:yellow, fg:blue, fg:magenta, fg:cyan, fg:white, bg:black, bg:red, bg:green, bg:yellow, bg:blue, bg:magenta, bg:cyan, bg:white. </p>
<dd><code>color_list_installed_newer </code> The colorization/highlighting for packages in list/info installed which are newer than the latest available package with the same name and arch. Default is `bold,yellow&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_list_installed_reinstall </code> The colorization/highlighting for packages in list/info installed which is the same version as the latest available package with the same name and arch. Default is `normal&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_list_installed_extra </code> The colorization/highlighting for packages in list/info installed which has no available package with the same name and arch. Default is `bold,red&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_list_available_upgrade </code> The colorization/highlighting for packages in list/info available which is an upgrade for the latest installed package with the same name and arch. Default is `bold,blue&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_list_available_downgrade </code> The colorization/highlighting for packages in list/info available which is a downgrade for the latest installed package with the same name and arch. Default is `dim,cyan&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_list_available_install </code> The colorization/highlighting for packages in list/info available which has no installed package with the same name and arch. Default is `normal&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_list_available_reinstall </code> The colorization/highlighting for packages in list/info available which is the same version as the installed package with the same name and arch. Default is `bold,underline,green. See color_list_installed_older for possible values. </p>
<dd><code>color_search_match </code> The colorization/highlighting for text matches in search. Default is `bold&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_update_installed </code> The colorization/highlighting for packages in the &quot;updates list&quot; which are installed. The updates list is what is printed when you run &quot;yum update&quot;, &quot;yum list updates&quot;, &quot;yum list obsoletes&quot; and &quot;yum check-update&quot;. Default is `normal&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_update_local </code> The colorization/highlighting for packages in the &quot;updates list&quot; which are already downloaded. The updates list is what is printed when you run &quot;yum update&quot;, &quot;yum list updates&quot;, &quot;yum list obsoletes&quot; and &quot;yum check-update&quot;. Default is `bold&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>color_update_remote </code> The colorization/highlighting for packages in the &quot;updates list&quot; which need to be downloaded. The updates list is what is printed when you run &quot;yum update&quot;, &quot;yum list updates&quot;, &quot;yum list obsoletes&quot; and &quot;yum check-update&quot;. Default is `normal&#8217;. See color_list_installed_older for possible values. </p>
<dd><code>clean_requirements_on_remove </code> When removing packages (by removal, update or obsoletion) go through each package&#8217;s dependencies. If any of them are no longer required by any other package then also mark them to be removed. Boolean (1, 0, True, False, yes, no) Defaults to False </p>
<dd><code>upgrade_requirements_on_install </code> When installing/reinstalling/upgrading packages go through each package&#8217;s installed dependencies and check for an update. Boolean (1, 0, True, False, yes,no) Defaults to False </p>
<dd><code>recheck_installed_requires </code> When upgrading a package do we recheck any requirements that existed in the old package. Turning this on shouldn&#8217;t do anything but slow yum depsolving down, however using rpm &#8211;nodeps etc. can break the rpmdb and then this will help. Boolean (1, 0, True, False, yes,no) Defaults to False </p>
<dd><code>reset_nice </code> If set to true then yum will try to reset the nice value to zero, before running an rpm transaction. Defaults to True. </p>
<p> <code>exit_on_lock</code> Should the yum client exit immediately when something else has the lock. Boolean (1, 0, True, False, yes, no) Defaults to False </p>
<dd><code>loadts_ignoremissing</code> Should the load-ts command ignore packages that are missing. This includes packages in the TS to be removed, which aren&#8217;t installed, and packages in the TS to be added, which aren&#8217;t available. If this is set to true, and an rpm is missing then loadts_ignorenewrpm is automatically set to true. Boolean (1, 0, True, False, yes, no) Defaults to False </p>
<dd><code>loadts_ignorerpm</code> Should the load-ts command ignore the rpmdb version (yum version nogroups) or abort if there is a mismatch between the TS file and the current machine. If this is set to true, then loadts_ignorenewrpm is automatically set to true. Boolean (1, 0, True, False, yes, no) Defaults to False </p>
<dd><code>loadts_ignorenewrpm</code> Should the load-ts command ignore the future rpmdb version or abort if there is a mismatch between the TS file and what will happen on the current machine. Note that if loadts_ignorerpm is True, this option does nothing. Boolean (1, 0, True, False, yes, no) Defaults to False </p>
</dl>
<h2>[repository] OPTIONS</h2>
<p>The repository section(s) take the following form:</p>
<dl>
<dd><code>Example</code>: [repositoryid]<br />
 name=Some name for this repository<br />
 baseurl=<a href="url://path/to/repository/">url://path/to/repository/</a> </p>
<dd><code>repositoryid</code> Must be a unique name for each repository, one word. </p>
<dd><code>name</code> A human readable string describing the repository. </p>
<dd><code>baseurl</code> Must be a URL to the directory where the yum repository&#8217;s `repodata&#8217; directory lives. Can be an <a rel="nofollow" href="http://,">http://,</a> ftp:// or file:// URL. You can specify multiple URLs in one baseurl statement. The best way to do this is like this:<br />
 [repositoryid]<br />
 name=Some name for this repository<br />
 baseurl=<a href="url://server1/path/to/repository/">url://server1/path/to/repository/</a> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a href="url://server2/path/to/repository/">url://server2/path/to/repository/</a> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a href="url://server3/path/to/repository/">url://server3/path/to/repository/</a> </p>
<p> If you list more than one baseurl= statement in a repository you will find yum will ignore the earlier ones and probably act bizarrely. Don&#8217;t do this, you&#8217;ve been warned. </p>
<p> You can use HTTP basic auth by prepending &quot;user:password@&quot; to the server name in the baseurl line. For example: &quot;baseurl=<a rel="nofollow" href="http://user:passwd@example.com/">http://user:passwd@example.com/</a>&quot;. </p>
<dd><code>metalink</code> Specifies a URL to a metalink file for the repomd.xml, a list of mirrors for the entire repository are generated by converting the mirrors for the repomd.xml file to a baseurl. The metalink file also contains the latest timestamp from the data in the repomd.xml, the length of the repomd.xml and checksum data. This data is checked against any downloaded repomd.xml file and all of the information from the metalink file must match. This can be used instead of or with the <code>baseurl</code> option. Substitution variables, described below, can be used with this option. This option disables the mirrorlist option. As a special hack is the mirrorlist URL contains the word &quot;metalink&quot; then the value of mirrorlist is copied to metalink (if metalink is not set). </p>
<dd><code>mirrorlist</code> Specifies a URL to a file containing a list of baseurls. This can be used instead of or with the <code>baseurl</code> option. Substitution variables, described below, can be used with this option. As a special hack is the mirrorlist URL contains the word &quot;metalink&quot; then the value of mirrorlist is copied to metalink (if metalink is not set). </p>
<dd><code>enabled</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not use this repository. </p>
<dd><code>gpgcheck</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not it should perform a GPG signature check on the packages gotten from this repository. </p>
<dd><code>repo_gpgcheck</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not it should perform a GPG signature check on the repodata from this repository. </p>
<dd><code>gpgkey</code> A URL pointing to the ASCII-armored GPG key file for the repository. This option is used if yum needs a public key to verify a package and the required key hasn&#8217;t been imported into the RPM database. If this option is set, yum will automatically import the key from the specified URL. You will be prompted before the key is installed unless the <code>assumeyes</code> option is set. </p>
<p> Multiple URLs may be specified here in the same manner as the <code>baseurl</code> option (above). If a GPG key is required to install a package from a repository, all keys specified for that repository will be installed. </p>
<dd><code>gpgcakey</code> A URL pointing to the ASCII-armored CA key file for the repository. This is a normal gpg public key &#8211; but this key will be used to validate detached signatures of all other keys. The idea is you are asked to confirm import for this key. After that any other gpg key needed for package or repository verification, if it has a detached signature which matches this key will be automatically imported without user confirmation. </p>
<dd><code>exclude</code> Same as the [main] <code>exclude</code> option but only for this repository. Substitution variables, described below, are honored here. </p>
<dd><code>includepkgs</code> Inverse of exclude. This is a list of packages you want to use from a repository. If this option lists only one package then that is all yum will ever see from the repository. Defaults to an empty list. Substitution variables, described below, are honored here. </p>
<dd><code>enablegroups</code> Either `0&#8242; or `1&#8242;. Determines whether yum will allow the use of package groups for this repository. Default is `1&#8242; (package groups are allowed). </p>
<dd><code>failovermethod</code> Either `roundrobin&#8217; or `priority&#8217;. </p>
<p> `roundrobin&#8217; randomly selects a URL out of the list of URLs to start with and proceeds through each of them as it encounters a failure contacting the host. </p>
<p> `priority&#8217; starts from the first baseurl listed and reads through them sequentially. </p>
<p> <code>failovermethod</code> defaults to `roundrobin&#8217; if not specified. </p>
<dd><code>keepalive</code> Either `1&#8242; or `0&#8242;. This tells yum whether or not HTTP/1.1 keepalive should be used with this repository. See the global option in the [main] section above for more information. </p>
<dd><code>timeout</code> Overrides the <code>timeout</code> option from the [main] section for this repository. </p>
<dd><code>http_caching</code> Overrides the <code>http_caching</code> option from the [main] section for this repository. </p>
<dd><code>retries</code> Overrides the <code>retries</code> option from the [main] section for this repository. </p>
<dd><code>throttle</code> Overrides the <code>throttle</code> option from the [main] section for this repository. </p>
<dd><code>bandwidth</code> Overrides the <code>bandwidth</code> option from the [main] section for this repository. </p>
<dd><code>ip_resolve </code> Overrides the <code>ip_resolve</code> option from the [main] section for this repository. </p>
<dd><code>sslcacert </code> Overrides the <code>sslcacert</code> option from the [main] section for this repository. </p>
<dd><code>sslverify </code> Overrides the <code>sslverify</code> option from the [main] section for this repository. </p>
<dd><code>sslclientcert </code> Overrides the <code>sslclientcert</code> option from the [main] section for this repository. </p>
<dd><code>sslclientkey </code> Overrides the <code>sslclientkey</code> option from the [main] section for this repository. </p>
<dd><code>ssl_check_cert_permissions </code> Overrides the <code>ssl_check_cert_permissions</code> option from the [main] section for this repository. </p>
<dd><code>metadata_expire </code> Overrides the <code>metadata_expire</code> option from the [main] section for this repository. </p>
<dd><code>mirrorlist_expire </code> Overrides the <code>mirrorlist_expire</code> option from the [main] section for this repository. </p>
<dd><code>proxy </code> URL to the proxy server for this repository. Set to &#8216;_none_&#8217; to disable the global proxy setting for this repository. If this is unset it inherits it from the global setting </p>
<dd><code>proxy_username </code> username to use for proxy. If this is unset it inherits it from the global setting </p>
<dd><code>proxy_password </code> password for this proxy. If this is unset it inherits it from the global setting </p>
<dd><code>username </code> username to use for basic authentication to a repo or really any url. If this is unset it inherits it from the global setting </p>
<dd><code>password </code> password to use with the username for basic authentication. If this is unset it inherits it from the global setting </p>
<dd><code>cost </code> relative cost of accessing this repository. Useful for weighing one repo&#8217;s packages as greater/less than any other. defaults to 1000 </p>
<dd><code>skip_if_unavailable </code> If set to True yum will continue running if this repository cannot be contacted for any reason. This should be set carefully as all repos are consulted for any given command. Defaults to False. </p>
<dd><code>async </code> If set to True Yum will download packages and metadata from this repo in parallel, if possible. Defaults to True. </p>
</dl>
<h2>Url Include Syntax</h2>
<p>The inclusion of external configuration files is supported for /etc/yum.conf and the .repo files in the /etc/yum.repos.d directory. To include a URL, use a line of the following format: </p>
<p> include=<a href="url://to/some/location">url://to/some/location</a> </p>
<p> The configuration file will be inserted at the position of the &quot;include=&quot; line. Included files may contain further include lines. Yum will abort with an error if an inclusion loop is detected.</p>
<h2>Glob: For List Options</h2>
<p>Any of the configurations options which are a list of items can be specfied using the glob syntax: <code>glob:/etc/path/somewhere.d/*.conf</code>. This will read in all files matching that glob and include all lines in each file (excluding comments and blank lines) as items in the list.</p>
<h2>Variables</h2>
<p>There are a number of variables you can use to ease maintenance of yum&#8217;s configuration files. They are available in the values of several options including <code>name</code>, <code>baseurl</code> and <code>commands. </p>
<dl>
<dd>$releasever</code> This will be replaced with the value of the version of the package listed in <code>distroverpkg</code>. This defaults to the version of `redhat-release&#8217; package. </p>
<dd><code>$arch</code> This will be replaced with your architecture as listed by os.uname()[4] in Python. </p>
<dd><code>$basearch</code> This will be replaced with your base architecture in yum. For example, if your $arch is i686 your $basearch will be i386. </p>
<dd><code>$uuid</code> This will be replaced with a unique but persistent uuid for this machine. The value that is first generated will be stored in /var/lib/yum/uuid and reused until this file is deleted. </p>
<dd><code>$YUM0-$YUM9</code> These will be replaced with the value of the shell environment variable of the same name. If the shell environment variable does not exist then the configuration file variable will not be replaced. </p>
</dl>
<p> As of 3.2.28, any file in /etc/yum/vars is turned into a variable named after the filename (or overrides any of the above variables). </p>
<p> Note that no warnings/errors are given if the files are unreadable, so creating files that only root can read may be confusing for users. </p>
<p> Also note that only the first line will be read and all new line characters are removed, as a convenience. However, no other checking is performed on the data. This means it is possible to have bad character data in any value.</p>
<h2>Files</h2>
<pre>/etc/yum.conf
/etc/yum.repos.d/
/etc/yum/pluginconf.d/
/etc/yum/protected.d
/etc/yum/vars</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-yum/">yum</a>(8) </p>
