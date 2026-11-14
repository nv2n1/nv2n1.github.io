---
title: "ikiwiki(1)"
name: "ikiwiki"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ikiwiki/"
---

<h2>NAME</h2>

 ikiwiki - a wiki compiler 

<h2>SYNOPSIS</h2>

 ikiwiki [options] source destination 

 ikiwiki --setup setupfile 

<h2>DESCRIPTION</h2>

 ikiwiki is a wiki compiler. It builds static HTML pages for a wiki, from source in the ikiwiki/Markdown language (or others), and writes it out to destination. 

 Note that most options can be shortened to single letters, and boolean flags such as --verbose can be negated with --no-verbose. 

<h2>MODE OPTIONS</h2>

 These options control the mode that ikiwiki operates in. 

<dl>
<dt>--refresh
<dd> Refresh the wiki, updating any changed pages. This is the default behavior so you don't normally need to specify it.
<dt>
<dd>
<dt>--rebuild
<dd> Force a rebuild of all pages.
<dt>
<dd>
<dt>--setup setupfile
<dd> The default action when --setup is specified is to automatically generate wrappers for a wiki based on data in a setup file, and rebuild the wiki. If you only want to build any changed pages, you can use --refresh with --setup.
<dt>
<dd>
<dt>--changesetup setupfile
<dd> Reads the setup file, adds any configuration changes specified by other options, and writes the new configuration back to the setup file. Also updates any configured wrappers. In this mode, the wiki is not fully rebuilt, unless you also add --rebuild.
<dt>
<dd> Example, to enable some plugins:
<dt>
<dd> ikiwiki --changesetup ~/ikiwiki.setup --plugin goodstuff --plugin calendar
<dt>
<dd>
<dt>--dumpsetup setupfile
<dd> Causes ikiwiki to write to the specified setup file, dumping out its current configuration.
<dt>
<dd>
<dt>--wrappers
<dd> If used with --setup --refresh, this makes it also update any configured wrappers.
<dt>
<dd>
<dt>--clean
<dd> This makes ikiwiki clean up by removing any files it denerated in the destination directory, as well as any configured wrappers, and the .ikiwiki state directory. This is mostly useful if you're running ikiwiki in a Makefile to build documentation and want a corresponding clean target.
<dt>
<dd>
<dt>--cgi
<dd> Enable CGI mode. In cgi mode ikiwiki runs as a cgi script, and supports editing pages, signing in, and registration.
<dt>
<dd> To use ikiwiki as a CGI program you need to use --wrapper or --setup to generate a wrapper. The wrapper will generally need to run suid 6755 to the user who owns the source and destination directories.
<dt>
<dd>
<dt>--wrapper [file]
<dd> Generate a wrapper binary that is hardcoded to do action specified by the other options, using the specified input files and destination directory. The filename to use for the wrapper is optional.
<dt>
<dd> The wrapper is designed to be safely made suid and be run by untrusted users, as a post-commit hook, or as a CGI.
<dt>
<dd> Note that the generated wrapper will ignore all command line parameters.
<dt>
<dd>
<dt>--aggregate
<dd> If the plugins/aggregate plugin is enabled, this makes ikiwiki poll configured feeds and save new posts to the srcdir.
<dt>
<dd> Note that to rebuild previously aggregated posts, use the --rebuild option along with this one. --rebuild will also force feeds to be polled even if they were polled recently.
<dt>
<dd>
<dt>--render file
<dd> Renders a single file, outputting the resulting html. Does not save state, so this cannot be used for building whole wikis, but it is useful for previewing an edited file at the command line. Generally used in conjunction with --setup to load in a wiki's setup:
<dt>
<dd> ikiwiki --setup ~/ikiwiki.setup --render foo.mdwn
<dt>
<dd>
<dt>--post-commit
<dd> Run in post-commit mode, the same as if called by a post-commit hook. This is probably only useful when using ikiwiki with a web server on one host and a repository on another, to allow the repository's real post-commit hook to ssh to the web server host and manually run ikiwiki to update the web site.
<dt>
<dd>
<dt>--version
<dd> Print ikiwiki's version number.
<dt>
<dd></dl>

<h2>CONFIG OPTIONS</h2>

 These options configure the wiki. Note that plugins can add additional configuration options of their own. All of these options and more besides can also be configured using a setup file. 

<dl>
<dt>--wikiname name
<dd> The name of the wiki, default is &quot;wiki&quot;.
<dt>
<dd>
<dt>--templatedir dir
<dd> Specify the directory that templates are stored in. Default is /usr/share/ikiwiki/templates, or another location as configured at build time. If the templatedir is changed, missing templates will still be searched for in the default location as a fallback. Templates can also be placed in the &quot;templates/&quot; subdirectory of the srcdir.
<dt>
<dd> Note that if you choose to copy and modify ikiwiki's templates, you will need to be careful to keep them up to date when upgrading to new versions of ikiwiki. Old versions of templates do not always work with new ikiwiki versions.
<dt>
<dd>
<dt>--underlaydir dir
<dd> Specify the directory that is used to underlay the source directory. Source files will be taken from here unless overridden by a file in the source directory. Default is /usr/share/ikiwiki/basewiki or another location as configured at build time.
<dt>
<dd>
<dt>--wrappermode mode
<dd> Specify a mode to chmod the wrapper to after creating it.
<dt>
<dd>
<dt>--wrappergroup group
<dd> Specify what unix group the wrapper should be owned by. This can be useful if the wrapper needs to be owned by a group other than the default. For example, if a project has a repository with multiple committers with access controlled by a group, it makes sense for the ikiwiki wrappers to run setgid to that group.
<dt>
<dd>
<dt>--rcs=svn|git|.., --no-rcs
<dd> Enable or disable use of a revision_control_system.
<dt>
<dd> The source directory will be assumed to be a working copy, or clone, or whatever the revision control system you select uses.
<dt>
<dd> In CGI mode, with a revision control system enabled, pages edited via the web will be committed.
<dt>
<dd> No revision control is enabled by default.
<dt>
<dd>
<dt>--svnrepo /svn/wiki
<dd> Specify the location of the svn repository for the wiki.
<dt>
<dd>
<dt>--svnpath trunk
<dd> Specify the path inside your svn repository where the wiki is located. This defaults to trunk; change it if your wiki is at some other path inside the repository. If your wiki is rooted at the top of the repository, set svnpath to &quot;&quot;.
<dt>
<dd>
<dt>--rss, --norss
<dd> If rss is set, ikiwiki will default to generating RSS feeds for pages that inline a blog.
<dt>
<dd>
<dt>--allowrss
<dd> If allowrss is set, and rss is not set, ikiwiki will not default to generating RSS feeds, but setting rss=yes in the inline directive can override this default and generate a feed.
<dt>
<dd>
<dt>--atom, --noatom
<dd> If atom is set, ikiwiki will default to generating Atom feeds for pages that inline a blog.
<dt>
<dd>
<dt>--allowatom
<dd> If allowatom is set, and rss is not set, ikiwiki will not default to generating Atom feeds, but setting atom=yes in the inline directive can override this default and generate a feed.
<dt>
<dd>
<dt>--pingurl URL
<dd> Set this to the URL of an XML-RPC service to ping when an RSS feed is updated. For example, to ping Technorati, use the URL <a rel="nofollow" HREF="http://rpc.technorati.com/rpc/ping">http://rpc.technorati.com/rpc/ping</a>
<dt>
<dd> This parameter can be specified multiple times to specify more than one URL to ping.
<dt>
<dd>
<dt>--url URL
<dd> Specifies the URL to the wiki. This is a required parameter in CGI mode.
<dt>
<dd>
<dt>--cgiurl <a rel="nofollow" HREF="http://example.org/ikiwiki.cgi">http://example.org/ikiwiki.cgi</a>
<dd> Specifies the URL to the ikiwiki CGI script wrapper. Required when building the wiki for links to the cgi script to be generated.
<dt>
<dd>
<dt>--historyurl URL
<dd> Specifies the URL to link to for page history browsing. In the URL, &quot;[[file]]&quot; is replaced with the file to browse. It's common to use ViewVC for this.
<dt>
<dd>
<dt>--adminemail you [at] example.org
<dd> Specifies the email address that ikiwiki should use for sending email.
<dt>
<dd>
<dt>--diffurl URL
<dd> Specifies the URL to link to for a diff of changes to a page. In the URL, &quot;[[file]]&quot; is replaced with the file to browse, &quot;[[r1]]&quot; is the old revision of the page, and &quot;[[r2]]&quot; is the new revision. It's common to use ViewVC for this.
<dt>
<dd>
<dt>--exclude regexp
<dd> Specifies a rexexp of source files to exclude from processing. May be specified multiple times to add to exclude list.
<dt>
<dd>
<dt>--include regexp
<dd> Specifies a rexexp of source files, that would normally be excluded, but that you wish to include in processing. May be specified multiple times to add to include list.
<dt>
<dd>
<dt>--adminuser name
<dd> Specifies a username of a user (or, if openid is enabled, an openid) who has the powers of a wiki admin. Currently allows locking of any page, and banning users; other powers may be added later. May be specified multiple times for multiple admins.
<dt>
<dd> For an openid user specify the full URL of the login, including &quot;http://&quot;.
<dt>
<dd>
<dt>--plugin name
<dd> Enables the use of the specified plugin in the wiki. Note that plugin names are case sensitive.
<dt>
<dd>
<dt>--disable-plugin name
<dd> Disables use of a plugin. For example &quot;--disable-plugin htmlscrubber&quot; to do away with HTML sanitization.
<dt>
<dd>
<dt>--libdir directory
<dd> Makes ikiwiki look in the specified directory first, before the regular locations when loading library files and plugins. For example, if you set libdir to &quot;/home/you/.ikiwiki/&quot;, you can install a foo.pm plugin as &quot;/home/you/.ikiwiki/IkiWiki/Plugin/foo.pm&quot;.
<dt>
<dd>
<dt>--discussion, --no-discussion
<dd> Enables or disables &quot;Discussion&quot; links from being added to the header of every page. The links are enabled by default.
<dt>
<dd>
<dt>--numbacklinks n
<dd> Controls how many backlinks should be displayed at the bottom of a page. Excess backlinks will be hidden in a popup. Default is 10. Set to 0 to disable this feature.
<dt>
<dd>
<dt>--userdir subdir
<dd> Optionally, allows links to users of the wiki to link to pages inside a subdirectory of the wiki. The default is to link to pages in the toplevel directory of the wiki.
<dt>
<dd>
<dt>--htmlext html
<dd> Configures the extension used for generated html files. Default is &quot;html&quot;.
<dt>
<dd>
<dt>--timeformat format
<dd> Specify how to display the time or date. The format string is passed to the <a HREF="/docs/linux/man/3-strftime/">strftime</a>(3) function.
<dt>
<dd>
<dt>--verbose, --no-verbose
<dd> Be verbose about what is being done.
<dt>
<dd>
<dt>--syslog, --no-syslog
<dd> Log to <a HREF="/docs/linux/man/3-syslog/">syslog</a>(3).
<dt>
<dd>
<dt>--usedirs, --no-usedirs
<dd> Toggle creating output files named page/index.html (default) instead of page.html.
<dt>
<dd>
<dt>--prefix-directives, --no-prefix-directives
<dd> Toggle new '!'-prefixed syntax for preprocessor directives. ikiwiki currently defaults to --prefix-directives.
<dt>
<dd>
<dt>--w3mmode, --no-w3mmode
<dd> Enable w3mmode, which allows w3m to use ikiwiki as a local CGI script, without a web server.
<dt>
<dd>
<dt>--sslcookie
<dd> Only send cookies over an SSL connection. This should prevent them being intercepted. If you enable this option then you must run at least the CGI portion of ikiwiki over SSL.
<dt>
<dd>
<dt>--gettime, --no-gettime
<dd> Extract creation and modification times for each new page from the the revision control's log. This is done automatically when building a wiki for the first time, so you normally do not need to use this option.
<dt>
<dd>
<dt>--set var=value
<dd> This allows setting an arbitrary configuration variable, the same as if it were set via a setup file. Since most commonly used options can be configured using command-line switches, you will rarely need to use this.
<dt>
<dd>
<dt>--set-yaml var=value
<dd> This is like --set, but it allows setting configuration variables that use complex data structures, by passing in a YAML document.
<dt>
<dd></dl>

<h2>EXAMPLES</h2>

<dl>
<dt>ikiwiki --setup my.setup
<dd>
<dt>
<dd> Completly (re)build the wiki using the specified setup file.
<dt>
<dd>
<dt>ikiwiki --setup my.setup --refresh
<dd> Refresh the wiki, using settings from my.setup, and avoid rebuilding any pages that have not changed. This is faster.
<dt>
<dd>
<dt>ikiwiki --setup my.setup --refresh --wrappers
<dd> Refresh the wiki, including regnerating all wrapper programs, but do not rebuild all pages. Useful if you have changed something in the setup file that does not need a full wiki rebuild to update all pages, but that you want to immediatly take effect.
<dt>
<dd></dl>

<h2>ENVIRONMENT</h2>

<dl>
<dt>CC
<dd>
<dt>
<dd> This controls what C compiler is used to build wrappers. Default is 'cc'.
<dt>
<dd>
<dt>CFLAGS
<dd> This can be used to pass options to the C compiler when building wrappers.
<dt>
<dd></dl>

<h2>SEE ALSO</h2>

<dl>
<dt><a HREF="/docs/linux/man/8-ikiwiki-mass-rebuild/">ikiwiki-mass-rebuild</a>(8)
<dd>
<dt><a HREF="/docs/linux/man/1-ikiwiki-update-wikilist/">ikiwiki-update-wikilist</a>(1)
<dd>
<dt><a HREF="/docs/linux/man/1-ikiwiki-transition/">ikiwiki-transition</a>(1)
<dd>
<dt>
<dd></dl>

<h2>AUTHOR</h2>

 Joey Hess &lt;joey [at] ikiwiki.info&gt; 

 

 

 

<h2>Index</h2>


