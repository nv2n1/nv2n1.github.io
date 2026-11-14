---
title: "cgitrc(5)"
name: "cgitrc"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cgitrc/"
---

cgitrc - runtime configuration for cgit

<h2>Synopsis</h2>

Cgitrc contains all runtime settings for cgit, including the list of git repositories, formatted as a line-separated list of NAME=VALUE pairs. Blank lines, and lines starting with <i>#</i>, are ignored.

<h2>Location</h2>

The default location of cgitrc, defined at compile time, is /etc/cgitrc. At runtime, cgit will consult the environment variable CGIT_CONFIG and, if defined, use its value instead.

<h2>Global Settings</h2>

about-filter
<dl><dd>Specifies a command which will be invoked to format the content of about pages (both top-level and for each repository). The command will get the content of the about-file on its STDIN, the name of the file as the first argument, and the STDOUT from the command will be included verbatim on the about page. Default value: none. See also: &quot;FILTER API&quot;.</dl>
 

 agefile
<dl><dd>Specifies a path, relative to each repository path, which can be used to specify the date and time of the youngest commit in the repository. The first line in the file is used as input to the &quot;parse_date&quot; function in libgit. Recommended timestamp-format is &quot;yyyy-mm-dd hh:mm:ss&quot;. You may want to generate this file from a post-receive hook. Default value: &quot;info/web/last-modified&quot;.</dl>
 

 auth-filter
<dl><dd>Specifies a command that will be invoked for authenticating repository access. Receives quite a few arguments, and data on both stdin and stdout for authentication processing. Details follow later in this document. If no auth-filter is specified, no authentication is performed. Default value: none. See also: &quot;FILTER API&quot;.</dl>
 

 branch-sort
<dl><dd>Flag which, when set to &quot;age&quot;, enables date ordering in the branch ref list, and when set to &quot;name&quot; enables ordering by branch name. Default value: &quot;name&quot;.</dl>
 

 cache-root
<dl><dd>Path used to store the cgit cache entries. Default value: &quot;/var/cache/cgit&quot;. See also: &quot;MACRO EXPANSION&quot;.</dl>
 

 cache-static-ttl
<dl><dd>Number which specifies the time-to-live, in minutes, for the cached version of repository pages accessed with a fixed SHA1. See also: &quot;CACHE&quot;. Default value: -1&quot;.</dl>
 

 cache-dynamic-ttl
<dl><dd>Number which specifies the time-to-live, in minutes, for the cached version of repository pages accessed without a fixed SHA1. See also: &quot;CACHE&quot;. Default value: &quot;5&quot;.</dl>
 

 cache-repo-ttl
<dl><dd>Number which specifies the time-to-live, in minutes, for the cached version of the repository summary page. See also: &quot;CACHE&quot;. Default value: &quot;5&quot;.</dl>
 

 cache-root-ttl
<dl><dd>Number which specifies the time-to-live, in minutes, for the cached version of the repository index page. See also: &quot;CACHE&quot;. Default value: &quot;5&quot;.</dl>
 

 cache-scanrc-ttl
<dl><dd>Number which specifies the time-to-live, in minutes, for the result of scanning a path for git repositories. See also: &quot;CACHE&quot;. Default value: &quot;15&quot;.</dl>
 

 cache-about-ttl
<dl><dd>Number which specifies the time-to-live, in minutes, for the cached version of the repository about page. See also: &quot;CACHE&quot;. Default value: &quot;15&quot;.</dl>
 

 cache-snapshot-ttl
<dl><dd>Number which specifies the time-to-live, in minutes, for the cached version of snapshots. See also: &quot;CACHE&quot;. Default value: &quot;5&quot;.</dl>
 

 cache-size
<dl><dd>The maximum number of entries in the cgit cache. When set to &quot;0&quot;, caching is disabled. See also: &quot;CACHE&quot;. Default value: &quot;0&quot;</dl>
 

 case-sensitive-sort
<dl><dd>Sort items in the repo list case sensitively. Default value: &quot;1&quot;. See also: repository-sort, section-sort.</dl>
 

 clone-prefix
<dl><dd>Space-separated list of common prefixes which, when combined with a repository url, generates valid clone urls for the repository. This setting is only used if repo.clone-url is unspecified. Default value: none.</dl>
 

 clone-url
<dl><dd>Space-separated list of clone-url templates. This setting is only used if repo.clone-url is unspecified. Default value: none. See also: &quot;MACRO EXPANSION&quot;, &quot;FILTER API&quot;.</dl>
 

 commit-filter
<dl><dd>Specifies a command which will be invoked to format commit messages. The command will get the message on its STDIN, and the STDOUT from the command will be included verbatim as the commit message, i.e. this can be used to implement bugtracker integration. Default value: none. See also: &quot;FILTER API&quot;.</dl>
 

 commit-sort
<dl><dd>Flag which, when set to &quot;date&quot;, enables strict date ordering in the commit log, and when set to &quot;topo&quot; enables strict topological ordering. If unset, the default ordering of &quot;git log&quot; is used. Default value: unset.</dl>
 

 css
<dl><dd>Url which specifies the css document to include in all cgit pages. Default value: &quot;/cgit.css&quot;.</dl>
 

 email-filter
<dl><dd>Specifies a command which will be invoked to format names and email address of committers, authors, and taggers, as represented in various places throughout the cgit interface. This command will receive an email address and an origin page string as its command line arguments, and the text to format on STDIN. It is to write the formatted text back out onto STDOUT. Default value: none. See also: &quot;FILTER API&quot;.</dl>
 

 embedded
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit generate a html fragment suitable for embedding in other html pages. Default value: none. See also: &quot;noheader&quot;.</dl>
 

 enable-commit-graph
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit print an ASCII-art commit history graph to the left of the commit messages in the repository log page. Default value: &quot;0&quot;.</dl>
 

 enable-filter-overrides
<dl><dd>Flag which, when set to &quot;1&quot;, allows all filter settings to be overridden in repository-specific cgitrc files. Default value: none.</dl>
 

 enable-follow-links
<dl><dd>Flag which, when set to &quot;1&quot;, allows users to follow a file in the log view. Default value: &quot;0&quot;.</dl>
 

 enable-http-clone
<dl><dd>If set to &quot;1&quot;, cgit will act as an dumb HTTP endpoint for git clones. You can add &quot;<a rel="nofollow" HREF="http://$HTTP_HOST$SCRIPT_NAME/$CGIT_REPO_URL">http://$HTTP_HOST$SCRIPT_NAME/$CGIT_REPO_URL</a>&quot; to clone-url to expose this feature. If you use an alternate way of serving git repositories, you may wish to disable this. Default value: &quot;1&quot;.</dl>
 

 enable-index-links
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit generate extra links for each repo in the repository index (specifically, to the &quot;summary&quot;, &quot;commit&quot; and &quot;tree&quot; pages). Default value: &quot;0&quot;.</dl>
 

 enable-index-owner
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit display the owner of each repo in the repository index. Default value: &quot;1&quot;.</dl>
 

 enable-log-filecount
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit print the number of modified files for each commit on the repository log page. Default value: &quot;0&quot;.</dl>
 

 enable-log-linecount
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit print the number of added and removed lines for each commit on the repository log page. Default value: &quot;0&quot;.</dl>
 

 enable-remote-branches
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit display remote branches in the summary and refs views. Default value: &quot;0&quot;. See also: &quot;repo.enable-remote-branches&quot;.</dl>
 

 enable-subject-links
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit use the subject of the parent commit as link text when generating links to parent commits in commit view. Default value: &quot;0&quot;. See also: &quot;repo.enable-subject-links&quot;.</dl>
 

 enable-html-serving
<dl><dd>Flag which, when set to &quot;1&quot;, will allow the /plain handler to serve mimetype headers that result in the file being treated as HTML by the browser. When set to &quot;0&quot;, such file types are returned instead as text/plain or application/octet-stream. Default value: &quot;0&quot;. See also: &quot;repo.enable-html-serving&quot;.</dl>
 

 enable-tree-linenumbers
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit generate linenumber links for plaintext blobs printed in the tree view. Default value: &quot;1&quot;.</dl>
 

 enable-git-config
<dl><dd>Flag which, when set to &quot;1&quot;, will allow cgit to use git config to set any repo specific settings. This option is used in conjunction with &quot;scan-path&quot;, and must be defined prior, to augment repo-specific settings. The keys gitweb.owner, gitweb.category, gitweb.description, and gitweb.homepage will map to the cgit keys repo.owner, repo.section, repo.desc, and repo.homepage respectively. All git config keys that begin with &quot;cgit.&quot; will be mapped to the corresponding &quot;repo.&quot; key in cgit. Default value: &quot;0&quot;. See also: scan-path, section-from-path.</dl>
 

 favicon
<dl><dd>Url used as link to a shortcut icon for cgit. It is suggested to use the value &quot;/favicon.ico&quot; since certain browsers will ignore other values. Default value: &quot;/favicon.ico&quot;.</dl>
 

 footer
<dl><dd>The content of the file specified with this option will be included verbatim at the bottom of all pages (i.e. it replaces the standard &quot;generated by...&quot; message. Default value: none.</dl>
 

 head-include
<dl><dd>The content of the file specified with this option will be included verbatim in the html HEAD section on all pages. Default value: none.</dl>
 

 header
<dl><dd>The content of the file specified with this option will be included verbatim at the top of all pages. Default value: none.</dl>
 

 include
<dl><dd>Name of a configfile to include before the rest of the current config- file is parsed. Default value: none. See also: &quot;MACRO EXPANSION&quot;.</dl>
 

 index-header
<dl><dd>The content of the file specified with this option will be included verbatim above the repository index. This setting is deprecated, and will not be supported by cgit-1.0 (use root-readme instead). Default value: none.</dl>
 

 index-info
<dl><dd>The content of the file specified with this option will be included verbatim below the heading on the repository index page. This setting is deprecated, and will not be supported by cgit-1.0 (use root-desc instead). Default value: none.</dl>
 

 local-time
<dl><dd>Flag which, if set to &quot;1&quot;, makes cgit print commit and tag times in the servers timezone. Default value: &quot;0&quot;.</dl>
 

 logo
<dl><dd>Url which specifies the source of an image which will be used as a logo on all cgit pages. Default value: &quot;/cgit.png&quot;.</dl>
 

 logo-link
<dl><dd>Url loaded when clicking on the cgit logo image. If unspecified the calculated url of the repository index page will be used. Default value: none.</dl>
 

 owner-filter
<dl><dd>Specifies a command which will be invoked to format the Owner column of the main page. The command will get the owner on STDIN, and the STDOUT from the command will be included verbatim in the table. This can be used to link to additional context such as an owners home page. When active this filter is used instead of the default owner query url. Default value: none. See also: &quot;FILTER API&quot;.</dl>
 

 max-atom-items
<dl><dd>Specifies the number of items to display in atom feeds view. Default value: &quot;10&quot;.</dl>
 

 max-commit-count
<dl><dd>Specifies the number of entries to list per page in &quot;log&quot; view. Default value: &quot;50&quot;.</dl>
 

 max-message-length
<dl><dd>Specifies the maximum number of commit message characters to display in &quot;log&quot; view. Default value: &quot;80&quot;.</dl>
 

 max-repo-count
<dl><dd>Specifies the number of entries to list per page on the repository index page. Default value: &quot;50&quot;.</dl>
 

 max-repodesc-length
<dl><dd>Specifies the maximum number of repo description characters to display on the repository index page. Default value: &quot;80&quot;.</dl>
 

 max-blob-size
<dl><dd>Specifies the maximum size of a blob to display HTML for in KBytes. Default value: &quot;0&quot; (limit disabled).</dl>
 

 max-stats
<dl><dd>Set the default maximum statistics period. Valid values are &quot;week&quot;, &quot;month&quot;, &quot;quarter&quot; and &quot;year&quot;. If unspecified, statistics are disabled. Default value: none. See also: &quot;repo.max-stats&quot;.</dl>
 

 mimetype.&lt;ext&gt;
<dl><dd>Set the mimetype for the specified filename extension. This is used by the plain command when returning blob content.</dl>
 

 mimetype-file
<dl><dd>Specifies the file to use for automatic mimetype lookup. If specified then this field is used as a fallback when no &quot;mimetype.&lt;ext&gt;&quot; match is found. If unspecified then no such lookup is performed. The typical file to use on a Linux system is /etc/mime.types. The format of the file must comply to: 

<dl><dd>&bull; a comment line is an empty line or a line starting with a hash (#), optionally preceded by whitespace</dl><dl><dd>&bull; a non-comment line starts with the mimetype (like image/png), followed by one or more file extensions (like jpg), all separated by whitespace Default value: none. See also: &quot;mimetype.&lt;ext&gt;&quot;.</dl></dl>
 

 module-link
<dl><dd>Text which will be used as the formatstring for a hyperlink when a submodule is printed in a directory listing. The arguments for the formatstring are the path and SHA1 of the submodule commit. Default value: none.</dl>
 

 nocache
<dl><dd>If set to the value &quot;1&quot; caching will be disabled. This settings is deprecated, and will not be honored starting with cgit-1.0. Default value: &quot;0&quot;.</dl>
 

 noplainemail
<dl><dd>If set to &quot;1&quot; showing full author email addresses will be disabled. Default value: &quot;0&quot;.</dl>
 

 noheader
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit omit the standard header on all pages. Default value: none. See also: &quot;embedded&quot;.</dl>
 

 project-list
<dl><dd>A list of subdirectories inside of scan-path, relative to it, that should loaded as git repositories. This must be defined prior to scan-path. Default value: none. See also: scan-path, &quot;MACRO EXPANSION&quot;.</dl>
 

 readme
<dl><dd>Text which will be used as default value for &quot;repo.readme&quot;. Multiple config keys may be specified, and cgit will use the first found file in this list. This is useful in conjunction with scan-path. Default value: none. See also: scan-path, repo.readme.</dl>
 

 remove-suffix
<dl><dd>If set to &quot;1&quot; and scan-path is enabled, if any repositories are found with a suffix of &quot;.git&quot;, this suffix will be removed for the url and name. This must be defined prior to scan-path. Default value: &quot;0&quot;. See also: scan-path.</dl>
 

 renamelimit
<dl><dd>Maximum number of files to consider when detecting renames. The value &quot;-1&quot; uses the compiletime value in git (for further info, look at man git-diff). Default value: &quot;-1&quot;.</dl>
 

 repo.group
<dl><dd>Legacy alias for &quot;section&quot;. This option is deprecated and will not be supported in cgit-1.0.</dl>
 

 repository-sort
<dl><dd>The way in which repositories in each section are sorted. Valid values are &quot;name&quot; for sorting by the repo name or &quot;age&quot; for sorting by the most recently updated repository. Default value: &quot;name&quot;. See also: section, case-sensitive-sort, section-sort.</dl>
 

 robots
<dl><dd>Text used as content for the &quot;robots&quot; meta-tag. Default value: &quot;index, nofollow&quot;.</dl>
 

 root-desc
<dl><dd>Text printed below the heading on the repository index page. Default value: &quot;a fast webinterface for the git dscm&quot;.</dl>
 

 root-readme
<dl><dd>The content of the file specified with this option will be included verbatim below the &quot;about&quot; link on the repository index page. Default value: none.</dl>
 

 root-title
<dl><dd>Text printed as heading on the repository index page. Default value: &quot;Git Repository Browser&quot;.</dl>
 

 scan-hidden-path
<dl><dd>If set to &quot;1&quot; and scan-path is enabled, scan-path will recurse into directories whose name starts with a period (<i>.</i>). Otherwise, scan-path will stay away from such directories (considered as &quot;hidden&quot;). Note that this does not apply to the &quot;.git&quot; directory in non-bare repos. This must be defined prior to scan-path. Default value: 0. See also: scan-path.</dl>
 

 scan-path
<dl><dd>A path which will be scanned for repositories. If caching is enabled, the result will be cached as a cgitrc include-file in the cache directory. If project-list has been defined prior to scan-path, scan-path loads only the directories listed in the file pointed to by project-list. Be advised that only the global settings taken before the scan-path directive will be applied to each repository. Default value: none. See also: cache-scanrc-ttl, project-list, &quot;MACRO EXPANSION&quot;.</dl>
 

 section
<dl><dd>The name of the current repository section - all repositories defined after this option will inherit the current section name. Default value: none.</dl>
 

 section-sort
<dl><dd>Flag which, when set to &quot;1&quot;, will sort the sections on the repository listing by name. Set this flag to &quot;0&quot; if the order in the cgitrc file should be preserved. Default value: &quot;1&quot;. See also: section, case-sensitive-sort, repository-sort.</dl>
 

 section-from-path
<dl><dd>A number which, if defined prior to scan-path, specifies how many path elements from each repo path to use as a default section name. If negative, cgit will discard the specified number of path elements above the repo directory. Default value: &quot;0&quot;.</dl>
 

 side-by-side-diffs
<dl><dd>If set to &quot;1&quot; shows side-by-side diffs instead of unidiffs per default. Default value: &quot;0&quot;.</dl>
 

 snapshots
<dl><dd>Text which specifies the default set of snapshot formats that cgit generates links for. The value is a space-separated list of zero or more of the values &quot;tar&quot;, &quot;tar.gz&quot;, &quot;tar.bz2&quot;, &quot;tar.xz&quot; and &quot;zip&quot;. Default value: none.</dl>
 

 source-filter
<dl><dd>Specifies a command which will be invoked to format plaintext blobs in the tree view. The command will get the blob content on its STDIN and the name of the blob as its only command line argument. The STDOUT from the command will be included verbatim as the blob contents, i.e. this can be used to implement e.g. syntax highlighting. Default value: none. See also: &quot;FILTER API&quot;.</dl>
 

 summary-branches
<dl><dd>Specifies the number of branches to display in the repository &quot;summary&quot; view. Default value: &quot;10&quot;.</dl>
 

 summary-log
<dl><dd>Specifies the number of log entries to display in the repository &quot;summary&quot; view. Default value: &quot;10&quot;.</dl>
 

 summary-tags
<dl><dd>Specifies the number of tags to display in the repository &quot;summary&quot; view. Default value: &quot;10&quot;.</dl>
 

 strict-export
<dl><dd>Filename which, if specified, needs to be present within the repository for cgit to allow access to that repository. This can be used to emulate gitweb's EXPORT_OK and STRICT_EXPORT functionality and limit cgit's repositories to match those exported by git-daemon. This option must be defined prior to scan-path.</dl>
 

 virtual-root
<dl><dd>Url which, if specified, will be used as root for all cgit links. It will also cause cgit to generate <i>virtual urls</i>, i.e. urls like <i>/cgit/tree/README</i> as opposed to <i>?r=cgit&amp;p=tree&amp;path=README</i>. Default value: none. NOTE: cgit has recently learned how to use PATH_INFO to achieve the same kind of virtual urls, so this option will probably be deprecated.</dl>

<h2>Repository Settings</h2>

repo.about-filter
<dl><dd>Override the default about-filter. Default value: none. See also: &quot;enable-filter-overrides&quot;. See also: &quot;FILTER API&quot;.</dl>
 

 repo.branch-sort
<dl><dd>Flag which, when set to &quot;age&quot;, enables date ordering in the branch ref list, and when set to &quot;name&quot; enables ordering by branch name. Default value: &quot;name&quot;.</dl>
 

 repo.clone-url
<dl><dd>A list of space-separated urls which can be used to clone this repo. Default value: none. See also: &quot;MACRO EXPANSION&quot;.</dl>
 

 repo.commit-filter
<dl><dd>Override the default commit-filter. Default value: none. See also: &quot;enable-filter-overrides&quot;. See also: &quot;FILTER API&quot;.</dl>
 

 repo.commit-sort
<dl><dd>Flag which, when set to &quot;date&quot;, enables strict date ordering in the commit log, and when set to &quot;topo&quot; enables strict topological ordering. If unset, the default ordering of &quot;git log&quot; is used. Default value: unset.</dl>
 

 repo.defbranch
<dl><dd>The name of the default branch for this repository. If no such branch exists in the repository, the first branch name (when sorted) is used as default instead. Default value: branch pointed to by HEAD, or &quot;master&quot; if there is no suitable HEAD.</dl>
 

 repo.desc
<dl><dd>The value to show as repository description. Default value: none.</dl>
 

 repo.homepage
<dl><dd>The value to show as repository homepage. Default value: none.</dl>
 

 repo.email-filter
<dl><dd>Override the default email-filter. Default value: none. See also: &quot;enable-filter-overrides&quot;. See also: &quot;FILTER API&quot;.</dl>
 

 repo.enable-commit-graph
<dl><dd>A flag which can be used to disable the global setting 'enable-commit-graph'. Default value: none.</dl>
 

 repo.enable-log-filecount
<dl><dd>A flag which can be used to disable the global setting 'enable-log-filecount'. Default value: none.</dl>
 

 repo.enable-log-linecount
<dl><dd>A flag which can be used to disable the global setting 'enable-log-linecount'. Default value: none.</dl>
 

 repo.enable-remote-branches
<dl><dd>Flag which, when set to &quot;1&quot;, will make cgit display remote branches in the summary and refs views. Default value: &lt;enable-remote-branches&gt;.</dl>
 

 repo.enable-subject-links
<dl><dd>A flag which can be used to override the global setting 'enable-subject-links'. Default value: none.</dl>
 

 repo.enable-html-serving
<dl><dd>A flag which can be used to override the global setting enable-html-serving. Default value: none.</dl>
 

 repo.hide
<dl><dd>Flag which, when set to &quot;1&quot;, hides the repository from the repository index. The repository can still be accessed by providing a direct path. Default value: &quot;0&quot;. See also: &quot;repo.ignore&quot;.</dl>
 

 repo.ignore
<dl><dd>Flag which, when set to &quot;1&quot;, ignores the repository. The repository is not shown in the index and cannot be accessed by providing a direct path. Default value: &quot;0&quot;. See also: &quot;repo.hide&quot;.</dl>
 

 repo.logo
<dl><dd>Url which specifies the source of an image which will be used as a logo on this repo's pages. Default value: global logo.</dl>
 

 repo.logo-link
<dl><dd>Url loaded when clicking on the cgit logo image. If unspecified the calculated url of the repository index page will be used. Default value: global logo-link.</dl>
 

 repo.owner-filter
<dl><dd>Override the default owner-filter. Default value: none. See also: &quot;enable-filter-overrides&quot;. See also: &quot;FILTER API&quot;.</dl>
 

 repo.module-link
<dl><dd>Text which will be used as the formatstring for a hyperlink when a submodule is printed in a directory listing. The arguments for the formatstring are the path and SHA1 of the submodule commit. Default value: &lt;module-link&gt;</dl>
 

 repo.module-link.&lt;path&gt;
<dl><dd>Text which will be used as the formatstring for a hyperlink when a submodule with the specified subdirectory path is printed in a directory listing. The only argument for the formatstring is the SHA1 of the submodule commit. Default value: none.</dl>
 

 repo.max-stats
<dl><dd>Override the default maximum statistics period. Valid values are equal to the values specified for the global &quot;max-stats&quot; setting. Default value: none.</dl>
 

 repo.name
<dl><dd>The value to show as repository name. Default value: &lt;repo.url&gt;.</dl>
 

 repo.owner
<dl><dd>A value used to identify the owner of the repository. Default value: none.</dl>
 

 repo.path
<dl><dd>An absolute path to the repository directory. For non-bare repositories this is the .git-directory. Default value: none.</dl>
 

 repo.readme
<dl><dd>A path (relative to &lt;repo.path&gt;) which specifies a file to include verbatim as the &quot;About&quot; page for this repo. You may also specify a git refspec by head or by hash by prepending the refspec followed by a colon. For example, &quot;master:docs/readme.mkd&quot;. If the value begins with a colon, i.e. &quot;:docs/readme.rst&quot;, the default branch of the repository will be used. Sharing any file will expose that entire directory tree to the &quot;/about/PATH&quot; endpoints, so be sure that there are no non-public files located in the same directory as the readme file. Default value: &lt;readme&gt;.</dl>
 

 repo.snapshots
<dl><dd>A mask of snapshot formats for this repo that cgit generates links for, restricted by the global &quot;snapshots&quot; setting. Default value: &lt;snapshots&gt;.</dl>
 

 repo.section
<dl><dd>Override the current section name for this repository. Default value: none.</dl>
 

 repo.source-filter
<dl><dd>Override the default source-filter. Default value: none. See also: &quot;enable-filter-overrides&quot;. See also: &quot;FILTER API&quot;.</dl>
 

 repo.url
<dl><dd>The relative url used to access the repository. This must be the first setting specified for each repo. Default value: none.</dl>

<h2>Repository-Specific Cgitrc File</h2>

When the option &quot;scan-path&quot; is used to auto-discover git repositories, cgit will try to parse the file &quot;cgitrc&quot; within any found repository. Such a repo-specific config file may contain any of the repo-specific options described above, except &quot;repo.url&quot; and &quot;repo.path&quot;. Additionally, the &quot;filter&quot; options are only acknowledged in repo-specific config files when &quot;enable-filter-overrides&quot; is set to &quot;1&quot;. 

 Note: the &quot;repo.&quot; prefix is dropped from the option names in repo-specific config files, e.g. &quot;repo.desc&quot; becomes &quot;desc&quot;.

<h2>Filter Api</h2>

By default, filters are separate processes that are executed each time they are needed. Alternative technologies may be used by prefixing the filter specification with the relevant string; available values are: 

 <i>exec:</i>
<dl><dd>The default &quot;one process per filter&quot; mode.</dl>
 

 <i>lua:</i>
<dl><dd>Executes the script using a built-in Lua interpreter. The script is loaded once per execution of cgit, and may be called multiple times during cgit's lifetime, making it a good choice for repeated filters such as the <i>email filter</i>. It responds to three functions:</dl>
 

 <i>filter_open(argument1, argument2, argument3, ...)</i>
<dl><dd>This is called upon activation of the filter for a particular set of data.</dl>
 

 <i>filter_write(buffer)</i>
<dl><dd>This is called whenever cgit writes data to the webpage.</dl>
 

 <i>filter_close()</i>
<dl><dd>This is called when the current filtering operation is completed. It must return an integer value. Usually 0 indicates success. 

<dl><dd><pre>Additionally, cgit exposes to the Lua the following built-in functions:</pre></dl></dl>
 

 <i>html(str)</i>
<dl><dd>Writes <i>str</i> to the webpage.</dl>
 

 <i>html_txt(str)</i>
<dl><dd>HTML escapes and writes <i>str</i> to the webpage.</dl>
 

 <i>html_attr(str)</i>
<dl><dd>HTML escapes for an attribute and writes &quot;str' to the webpage.</dl>
 

 <i>html_url_path(str)</i>
<dl><dd>URL escapes for a path and writes <i>str</i> to the webpage.</dl>
 

 <i>html_url_arg(str)</i>
<dl><dd>URL escapes for an argument and writes <i>str</i> to the webpage.</dl>
 

 <i>html_include(file)</i>
<dl><dd>Includes <i>file</i> in webpage.</dl>
 

 Parameters are provided to filters as follows. 

 about filter
<dl><dd>This filter is given a single parameter: the filename of the source file to filter. The filter can use the filename to determine (for example) the type of syntax to follow when formatting the readme file. The about text that is to be filtered is available on standard input and the filtered text is expected on standard output.</dl>
 

 commit filter
<dl><dd>This filter is given no arguments. The commit message text that is to be filtered is available on standard input and the filtered text is expected on standard output.</dl>
 

 email filter
<dl><dd>This filter is given two parameters: the email address of the relevant author and a string indicating the originating page. The filter will then receive the text string to format on standard input and is expected to write to standard output the formatted text to be included in the page.</dl>
 

 owner filter
<dl><dd>This filter is given no arguments. The owner text is available on standard input and the filter is expected to write to standard output. The output is included in the Owner column.</dl>
 

 source filter
<dl><dd>This filter is given a single parameter: the filename of the source file to filter. The filter can use the filename to determine (for example) the syntax highlighting mode. The contents of the source file that is to be filtered is available on standard input and the filtered contents is expected on standard output.</dl>
 

 auth filter
<dl><dd>The authentication filter receives 12 parameters: 

<dl><dd>&bull; filter action, explained below, which specifies which action the filter is called for</dl><dl><dd>&bull; http cookie</dl><dl><dd>&bull; http method</dl><dl><dd>&bull; http referer</dl><dl><dd>&bull; http path</dl><dl><dd>&bull; http https flag</dl><dl><dd>&bull; cgit repo</dl><dl><dd>&bull; cgit page</dl><dl><dd>&bull; cgit url</dl><dl><dd>&bull; cgit login url When the filter action is &quot;body&quot;, this filter must write to output the HTML for displaying the login form, which POSTs to the login url. When the filter action is &quot;authenticate-cookie&quot;, this filter must validate the http cookie and return a 0 if it is invalid or 1 if it is invalid, in the exit code / close function. If the filter action is &quot;authenticate-post&quot;, this filter receives POST'd parameters on standard input, and should write a complete CGI response, preferably with a 302 redirect, and write to output one or more &quot;Set-Cookie&quot; HTTP headers, each followed by a newline. 

<dl><dd><pre>Please see `filters/simple-authentication.lua` for a clear example
script that may be modified.</pre></dl></dl>
</dl>
 

 All filters are handed the following environment variables: 

<dl><dd>&bull; CGIT_REPO_URL (from repo.url)</dl><dl><dd>&bull; CGIT_REPO_NAME (from repo.name)</dl><dl><dd>&bull; CGIT_REPO_PATH (from repo.path)</dl><dl><dd>&bull; CGIT_REPO_OWNER (from repo.owner)</dl><dl><dd>&bull; CGIT_REPO_DEFBRANCH (from repo.defbranch)</dl><dl><dd>&bull; CGIT_REPO_SECTION (from repo.section)</dl><dl><dd>&bull; CGIT_REPO_CLONE_URL (from repo.clone-url)</dl>
 

 If a setting is not defined for a repository and the corresponding global setting is also not defined (if applicable), then the corresponding environment variable will be unset.

<h2>Macro Expansion</h2>

The following cgitrc options support a simple macro expansion feature, where tokens prefixed with &quot;$&quot; are replaced with the value of a similarly named environment variable: 

<dl><dd>&bull; cache-root</dl><dl><dd>&bull; include</dl><dl><dd>&bull; project-list</dl><dl><dd>&bull; scan-path</dl>
 

 Macro expansion will also happen on the content of $CGIT_CONFIG, if defined. 

 One usage of this feature is virtual hosting, which in its simplest form can be accomplished by adding the following line to /etc/cgitrc: 

<dl><dd><pre>include=/etc/cgitrc.d/$HTTP_HOST</pre></dl>
 

 The following options are expanded during request processing, and support the environment variables defined in &quot;FILTER API&quot;: 

<dl><dd>&bull; clone-url</dl><dl><dd>&bull; repo.clone-url</dl>

<h2>Cache</h2>

All cache ttl values are in minutes. Negative ttl values indicate that a page type will never expire, and thus the first time a URL is accessed, the result will be cached indefinitely, even if the underlying git repository changes. Conversely, when a ttl value is zero, the cache is disabled for that particular page type, and the page type is never cached.

<h2>Example Cgitrc File</h2>

<dl><dd><pre># Enable caching of up to 1000 output entries
cache-size=1000
# Specify some default clone urls using macro expansion
clone-url=<a HREF="git://foo.org/$CGIT_REPO_URL">git://foo.org/$CGIT_REPO_URL</a> git [at] foo.org:$CGIT_REPO_URL
# Specify the css url
css=/css/cgit.css
# Show owner on index page
enable-index-owner=1
# Allow http transport git clone
enable-http-clone=1
# Show extra links for each repository on the index page
enable-index-links=1
# Enable ASCII art commit history graph on the log pages
enable-commit-graph=1
# Show number of affected files per commit on the log pages
enable-log-filecount=1
# Show number of added/removed lines per commit on the log pages
enable-log-linecount=1
# Sort branches by date
branch-sort=age
# Add a cgit favicon
favicon=/favicon.ico
# Use a custom logo
logo=/img/mylogo.png
# Enable statistics per week, month and quarter
max-stats=quarter
# Set the title and heading of the repository index page
root-title=example.com git repositories
# Set a subheading for the repository index page
root-desc=tracking the foobar development
# Include some more info about example.com on the index page
root-readme=/var/www/htdocs/about.html
# Allow download of tar.gz, tar.bz2 and zip-files
snapshots=tar.gz tar.bz2 zip
##
## List of common mimetypes
##
mimetype.gif=image/gif
mimetype.html=text/html
mimetype.jpg=image/jpeg
mimetype.jpeg=image/jpeg
mimetype.pdf=application/pdf
mimetype.png=image/png
mimetype.svg=image/svg+xml
# Highlight source code with python pygments-based highlighter
source-filter=/var/www/cgit/filters/syntax-highlighting.py
# Format markdown, restructuredtext, manpages, text files, and html files
# through the right converters
about-filter=/var/www/cgit/filters/about-formatting.sh
##
## Search for these files in the root of the default branch of repositories
## for coming up with the about page:
##
readme=:README.md
readme=:readme.md
readme=:README.mkd
readme=:readme.mkd
readme=:README.rst
readme=:readme.rst
readme=:README.html
readme=:readme.html
readme=:README.htm
readme=:readme.htm
readme=:README.txt
readme=:readme.txt
readme=:README
readme=:readme
readme=:INSTALL.md
readme=:install.md
readme=:INSTALL.mkd
readme=:install.mkd
readme=:INSTALL.rst
readme=:install.rst
readme=:INSTALL.html
readme=:install.html
readme=:INSTALL.htm
readme=:install.htm
readme=:INSTALL.txt
readme=:install.txt
readme=:INSTALL
readme=:install
##
## List of repositories.
## PS: Any repositories listed when section is unset will not be
## displayed under a section heading
## PPS: This list could be kept in a different file (e.g. '/etc/cgitrepos')
## and included like this:
## include=/etc/cgitrepos
##
repo.url=foo
repo.path=/pub/git/foo.git
repo.desc=the master foo repository
repo.owner=fooman [at] example.com
repo.readme=info/web/about.html
repo.url=bar
repo.path=/pub/git/bar.git
repo.desc=the bars for your foo
repo.owner=barman [at] example.com
repo.readme=info/web/about.html
# The next repositories will be displayed under the 'extras' heading
section=extras
repo.url=baz
repo.path=/pub/git/baz.git
repo.desc=a set of extensions for bar users
repo.url=wiz
repo.path=/pub/git/wiz.git
repo.desc=the wizard of foo
# Add some mirrored repositories
section=mirrors
repo.url=git
repo.path=/pub/git/git.git
repo.desc=the dscm
repo.url=linux
repo.path=/pub/git/linux.git
repo.desc=the kernel
# Disable adhoc downloads of this repo
repo.snapshots=0
# Disable line-counts for this repo
repo.enable-log-linecount=0
# Restrict the max statistics period for this repo
repo.max-stats=month</pre></dl>

<h2>Bugs</h2>

Comments currently cannot appear on the same line as a setting; the comment will be included as part of the value. E.g. this line:
<dl><dd><pre>robots=index # allow indexing</pre></dl>
 will generate the following html element: <pre><code>&lt;meta name='robots' content='index  # allow indexing'/&gt;</code></pre>

<h2>Author</h2>

Lars Hjemli &lt;hjemli [at] gmail.com&gt; Jason A. Donenfeld &lt;Jason [at] zx2c4.com&gt;
