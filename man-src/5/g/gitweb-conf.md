---
title: "gitweb-conf(5)"
name: "gitweb-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gitweb-conf/"
description: "gitweb.conf – Gitweb (Git web interface) configuration file"
---

<p>gitweb.conf &#8211; Gitweb (Git web interface) configuration file</p>
<h2>Synopsis</h2>
<p>/etc/gitweb.conf, /etc/gitweb-common.conf, $GITWEBDIR/gitweb_config.perl</p>
<h2>Description</h2>
<p>The gitweb CGI script for viewing Git repositories over the web uses a perl script fragment as its configuration file. You can set variables using &quot;<code>our $variable = value</code>&quot;; text from a &quot;#&quot; character until the end of a line is ignored. See <code><a href="/docs/linux/man/1-perlsyn/">perlsyn</a></code>(1) for details. An example: </p>
<pre><code>#gitweb configuration file for http: // git.example.org
#
our $projectroot = &quot;/srv/git&quot;;
#FHS recommendation
    our $site_name = 'Example.org &gt;&gt; Repos';
</code></pre>
<p> The configuration file is used to override the default settings that were built into gitweb at the time the <i>gitweb.cgi</i> script was generated. While one could just alter the configuration settings in the gitweb CGI itself, those changes would be lost upon upgrade. Configuration settings might also be placed into a file in the same directory as the CGI script with the default name <i>gitweb_config.perl</i> &#8212; allowing one to have multiple gitweb instances with different configurations by the use of symlinks. Note that some configuration can be controlled on per-repository rather than gitweb-wide basis: see &quot;Per-repository gitweb configuration&quot; subsection on <code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1) manpage.</p>
<h2>Discussion</h2>
<p>Gitweb reads configuration data from the following sources in the following order: </p>
<dl>
<dd>&bull; built-in values (some set during build stage),</dl>
<dl>
<dd>&bull; common system-wide configuration file (defaults to <code>/etc/gitweb-common.conf</code>),</dl>
<dl>
<dd>&bull; either per-instance configuration file (defaults to <i>gitweb_config.perl</i> in the same directory as the installed gitweb), or if it does not exists then fallback system-wide configuration file (defaults to <code>/etc/gitweb.conf</code>).</dl>
<p> Values obtained in later configuration files override values obtained earlier in the above sequence. </p>
<p> Locations of the common system-wide configuration file, the fallback system-wide configuration file and the per-instance configuration file are defined at compile time using build-time Makefile configuration variables, respectively <code>GITWEB_CONFIG_COMMON</code>, <code>GITWEB_CONFIG_SYSTEM</code> and <code>GITWEB_CONFIG</code>. </p>
<p> You can also override locations of gitweb configuration files during runtime by setting the following environment variables: <code>GITWEB_CONFIG_COMMON</code>, <code>GITWEB_CONFIG_SYSTEM</code> and <code>GITWEB_CONFIG</code> to a non-empty value. </p>
<p> The syntax of the configuration files is that of Perl, since these files are handled by sourcing them as fragments of Perl code (the language that gitweb itself is written in). Variables are typically set using the <code>our</code> qualifier (as in &quot;<code>our $variable = &lt;value&gt;;</code>&quot;) to avoid syntax errors if a new version of gitweb no longer uses a variable and therefore stops declaring it. </p>
<p> You can include other configuration file using read_config_file() subroutine. For example, one might want to put gitweb configuration related to access control for viewing repositories via Gitolite (one of Git repository management tools) in a separate file, e.g. in <code>/etc/gitweb-gitolite.conf</code>. To include it, put </p>
<dl>
<dd>
<pre>read_config_file(&quot;/etc/gitweb-gitolite.conf&quot;);</pre>
</dl>
<p> somewhere in gitweb configuration file used, e.g. in per-installation gitweb configuration file. Note that read_config_file() checks itself that the file it reads exists, and does nothing if it is not found. It also handles errors in included file. </p>
<p> The default configuration with no configuration file at all may work perfectly well for some installations. Still, a configuration file is useful for customizing or tweaking the behavior of gitweb in many ways, and some optional features will not be present unless explicitly enabled using the configurable <code>%features</code> variable (see also &quot;Configuring gitweb features&quot; section below).</p>
<h2>Configuration Variables</h2>
<p>Some configuration variables have their default values (embedded in the CGI script) set during building gitweb &#8212; if that is the case, this fact is put in their description. See gitweb&#8217;s <i>INSTALL</i> file for instructions on building and installing gitweb.</p>
<h3>Location of repositories</h3>
<p>The configuration variables described below control how gitweb finds Git repositories, and how repositories are displayed and accessed. </p>
<p> See also &quot;Repositories&quot; and later subsections in <code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1) manpage. </p>
<p> $projectroot</p>
<dl>
<dd>Absolute filesystem path which will be prepended to project path; the path to repository is <code>$projectroot/$project</code>. Set to <code>$GITWEB_PROJECTROOT</code> during installation. This variable has to be set correctly for gitweb to find repositories. </p>
<p> For example, if <code>$projectroot</code> is set to &quot;/srv/git&quot; by putting the following in gitweb config file: </p>
<dl>
<dd>
<pre>our $projectroot = &quot;/srv/git&quot;;</pre>
</dl>
<p> then </p>
<dl>
<dd>
<pre><a rel="nofollow" href="http://git.example.com/gitweb.cgi?p=foo/bar.git">http://git.example.com/gitweb.cgi?p=foo/bar.git</a></pre>
</dl>
<p> and its path_info based equivalent </p>
<dl>
<dd>
<pre><a rel="nofollow" href="http://git.example.com/gitweb.cgi/foo/bar.git">http://git.example.com/gitweb.cgi/foo/bar.git</a></pre>
</dl>
<p> will map to the path <code>/srv/git/foo/bar.git</code> on the filesystem.</dl>
<p> $projects_list</p>
<dl>
<dd>Name of a plain text file listing projects, or a name of directory to be scanned for projects. </p>
<p> Project list files should list one project per line, with each line having the following format </p>
<dl>
<dd>
<pre>&lt;URI-encoded filesystem path to repository&gt; SP &lt;URI-encoded repository owner&gt;</pre>
</dl>
<p> The default value of this variable is determined by the <code>GITWEB_LIST</code> makefile variable at installation time. If this variable is empty, gitweb will fall back to scanning the <code>$projectroot</code> directory for repositories.</dl>
<p> $project_maxdepth</p>
<dl>
<dd>If <code>$projects_list</code> variable is unset, gitweb will recursively scan filesystem for Git repositories. The <code>$project_maxdepth</code> is used to limit traversing depth, relative to <code>$projectroot</code> (starting point); it means that directories which are further from <code>$projectroot</code> than <code>$project_maxdepth</code> will be skipped. </p>
<p> It is purely performance optimization, originally intended for MacOS X, where recursive directory traversal is slow. Gitweb follows symbolic links, but it detects cycles, ignoring any duplicate files and directories. </p>
<p> The default value of this variable is determined by the build-time configuration variable <code>GITWEB_PROJECT_MAXDEPTH</code>, which defaults to 2007.</dl>
<p> $export_ok</p>
<dl>
<dd>Show repository only if this file exists (in repository). Only effective if this variable evaluates to true. Can be set when building gitweb by setting <code>GITWEB_EXPORT_OK</code>. This path is relative to <code>GIT_DIR</code>. git-daemon[1] uses <i>git-daemon-export-ok</i>, unless started with <code>&#8211;export-all</code>. By default this variable is not set, which means that this feature is turned off.</dl>
<p> $export_auth_hook</p>
<dl>
<dd>Function used to determine which repositories should be shown. This subroutine should take one parameter, the full path to a project, and if it returns true, that project will be included in the projects list and can be accessed through gitweb as long as it fulfills the other requirements described by $export_ok, $projects_list, and $projects_maxdepth. Example: </p>
<dl>
<dd>
<pre>our $export_auth_hook = sub { return -e &quot;$_[0]/git-daemon-export-ok&quot;; };</pre>
</dl>
<p> though the above might be done by using <code>$export_ok</code> instead </p>
<dl>
<dd>
<pre>our $export_ok = &quot;git-daemon-export-ok&quot;;</pre>
</dl>
<p> If not set (default), it means that this feature is disabled. </p>
<p> See also more involved example in &quot;Controlling access to Git repositories&quot; subsection on <code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1) manpage.</dl>
<p> $strict_export</p>
<dl>
<dd>Only allow viewing of repositories also shown on the overview page. This for example makes <code>$export_ok</code> file decide if repository is available and not only if it is shown. If <code>$projects_list</code> points to file with list of project, only those repositories listed would be available for gitweb. Can be set during building gitweb via <code>GITWEB_STRICT_EXPORT</code>. By default this variable is not set, which means that you can directly access those repositories that are hidden from projects list page (e.g. the are not listed in the $projects_list file).</dl>
<h3>Finding files</h3>
<p>The following configuration variables tell gitweb where to find files. The values of these variables are paths on the filesystem. </p>
<p> $GIT</p>
<dl>
<dd>Core git executable to use. By default set to <code>$GIT_BINDIR/git</code>, which in turn is by default set to <code>$(bindir)/git</code>. If you use Git installed from a binary package, you should usually set this to &quot;/usr/bin/git&quot;. This can just be &quot;git&quot; if your web server has a sensible PATH; from security point of view it is better to use absolute path to git binary. If you have multiple Git versions installed it can be used to choose which one to use. Must be (correctly) set for gitweb to be able to work.</dl>
<p> $mimetypes_file</p>
<dl>
<dd>File to use for (filename extension based) guessing of MIME types before trying <code>/etc/mime.types</code>. <code>NOTE</code> that this path, if relative, is taken as relative to the current Git repository, not to CGI script. If unset, only <code>/etc/mime.types</code> is used (if present on filesystem). If no mimetypes file is found, mimetype guessing based on extension of file is disabled. Unset by default.</dl>
<p> $highlight_bin</p>
<dl>
<dd>Path to the highlight executable to use (it must be the one from m[blue]<code><a rel="nofollow" href="http://www.andre-simon.de">http://www.andre-simon.de</a></code>m[] due to assumptions about parameters and output). By default set to <i>highlight</i>; set it to full path to highlight executable if it is not installed on your web server&#8217;s PATH. Note that <i>highlight</i> feature must be set for gitweb to actually use syntax highlighting. </p>
<p> <code>NOTE</code>: for a file to be highlighted, its syntax type must be detected and that syntax must be supported by &quot;highlight&quot;. The default syntax detection is minimal, and there are many supported syntax types with no detection by default. There are three options for adding syntax detection. The first and second priority are <code>%highlight_basename</code> and <code>%highlight_ext</code>, which detect based on basename (the full filename, for example &quot;Makefile&quot;) and extension (for example &quot;sh&quot;). The keys of these hashes are the basename and extension, respectively, and the value for a given key is the name of the syntax to be passed via <code>&#8211;syntax &lt;syntax&gt;</code> to &quot;highlight&quot;. The last priority is the &quot;highlight&quot; configuration of <code>Shebang</code> regular expressions to detect the language based on the first line in the file, (for example, matching the line &quot;#!/bin/bash&quot;). See the highlight documentation and the default config at /etc/highlight/filetypes.conf for more details. </p>
<p> For example if repositories you are hosting use &quot;phtml&quot; extension for PHP files, and you want to have correct syntax-highlighting for those files, you can add the following to gitweb configuration: </p>
<dl>
<dd>
<pre>our %highlight_ext;
$highlight_ext{'phtml'} = 'php';</pre>
</dl>
</dl>
<h3>Links and their targets</h3>
<p>The configuration variables described below configure some of gitweb links: their target and their look (text or image), and where to find page prerequisites (stylesheet, favicon, images, scripts). Usually they are left at their default values, with the possible exception of <code>@stylesheets</code> variable. </p>
<p> @stylesheets</p>
<dl>
<dd>List of URIs of stylesheets (relative to the base URI of a page). You might specify more than one stylesheet, for example to use &quot;gitweb.css&quot; as base with site specific modifications in a separate stylesheet to make it easier to upgrade gitweb. For example, you can add a <code>site</code> stylesheet by putting </p>
<dl>
<dd>
<pre>push @stylesheets, &quot;gitweb-site.css&quot;;</pre>
</dl>
<p> in the gitweb config file. Those values that are relative paths are relative to base URI of gitweb. </p>
<p> This list should contain the URI of gitweb&#8217;s standard stylesheet. The default URI of gitweb stylesheet can be set at build time using the <code>GITWEB_CSS</code> makefile variable. Its default value is <code>static/gitweb.css</code> (or <code>static/gitweb.min.css</code> if the <code>CSSMIN</code> variable is defined, i.e. if CSS minifier is used during build). </p>
<p> <code>Note</code>: there is also a legacy <code>$stylesheet</code> configuration variable, which was used by older gitweb. If <code>$stylesheet</code> variable is defined, only CSS stylesheet given by this variable is used by gitweb.</dl>
<p> $logo</p>
<dl>
<dd>Points to the location where you put <i>git-logo.png</i> on your web server, or to be more the generic URI of logo, 72&#215;27 size). This image is displayed in the top right corner of each gitweb page and used as a logo for the Atom feed. Relative to the base URI of gitweb (as a path). Can be adjusted when building gitweb using <code>GITWEB_LOGO</code> variable By default set to <code>static/git-logo.png</code>.</dl>
<p> $favicon</p>
<dl>
<dd>Points to the location where you put <i>git-favicon.png</i> on your web server, or to be more the generic URI of favicon, which will be served as &quot;image/png&quot; type. Web browsers that support favicons (website icons) may display them in the browser&#8217;s URL bar and next to the site name in bookmarks. Relative to the base URI of gitweb. Can be adjusted at build time using <code>GITWEB_FAVICON</code> variable. By default set to <code>static/git-favicon.png</code>.</dl>
<p> $javascript</p>
<dl>
<dd>Points to the location where you put <i>gitweb.js</i> on your web server, or to be more generic the URI of JavaScript code used by gitweb. Relative to the base URI of gitweb. Can be set at build time using the <code>GITWEB_JS</code> build-time configuration variable. </p>
<p> The default value is either <code>static/gitweb.js</code>, or <code>static/gitweb.min.js</code> if the <code>JSMIN</code> build variable was defined, i.e. if JavaScript minifier was used at build time. <code>Note</code> that this single file is generated from multiple individual JavaScript &quot;modules&quot;.</dl>
<p> $home_link</p>
<dl>
<dd>Target of the home link on the top of all pages (the first part of view &quot;breadcrumbs&quot;). By default it is set to the absolute URI of a current page (to the value of <code>$my_uri</code> variable, or to &quot;/&quot; if <code>$my_uri</code> is undefined or is an empty string).</dl>
<p> $home_link_str</p>
<dl>
<dd>Label for the &quot;home link&quot; at the top of all pages, leading to <code>$home_link</code> (usually the main gitweb page, which contains the projects list). It is used as the first component of gitweb&#8217;s &quot;breadcrumb trail&quot;: <code>&lt;home link&gt; / &lt;project&gt; / &lt;action&gt;</code>. Can be set at build time using the <code>GITWEB_HOME_LINK_STR</code> variable. By default it is set to &quot;projects&quot;, as this link leads to the list of projects. Another popular choice is to set it to the name of site. Note that it is treated as raw HTML so it should not be set from untrusted sources.</dl>
<p> @extra_breadcrumbs</p>
<dl>
<dd>Additional links to be added to the start of the breadcrumb trail before the home link, to pages that are logically &quot;above&quot; the gitweb projects list, such as the organization and department which host the gitweb server. Each element of the list is a reference to an array, in which element 0 is the link text (equivalent to <code>$home_link_str</code>) and element 1 is the target URL (equivalent to <code>$home_link</code>). </p>
<p> For example, the following setting produces a breadcrumb trail like &quot;home / dev / projects / &#8230;&quot; where &quot;projects&quot; is the home link. </p>
<dl>
<dd>
<pre> our @extra_breadcrumbs = (
 [ 'home' =&gt; '<a rel="nofollow" href="https://www.example.org/'">https://www.example.org/'</a> ],
 [ 'dev' =&gt; '<a rel="nofollow" href="https://dev.example.org/'">https://dev.example.org/'</a> ],
 );</pre>
</dl>
</dl>
<p> $logo_url, $logo_label</p>
<dl>
<dd>URI and label (title) for the Git logo link (or your site logo, if you chose to use different logo image). By default, these both refer to Git homepage, m[blue]<code><a rel="nofollow" href="https://git-scm.com">https://git-scm.com</a></code>m[]; in the past, they pointed to Git documentation at m[blue]<code><a rel="nofollow" href="https://www.kernel.org">https://www.kernel.org</a></code>m[].</dl>
<h3>Changing gitweb&#8217;s look</h3>
<p>You can adjust how pages generated by gitweb look using the variables described below. You can change the site name, add common headers and footers for all pages, and add a description of this gitweb installation on its main page (which is the projects list page), etc. </p>
<p> $site_name</p>
<dl>
<dd>Name of your site or organization, to appear in page titles. Set it to something descriptive for clearer bookmarks etc. If this variable is not set or is, then gitweb uses the value of the <code>SERVER_NAME</code> <code>CGI</code> environment variable, setting site name to &quot;$SERVER_NAME Git&quot;, or &quot;Untitled Git&quot; if this variable is not set (e.g. if running gitweb as standalone script). </p>
<p> Can be set using the <code>GITWEB_SITENAME</code> at build time. Unset by default.</dl>
<p> $site_html_head_string</p>
<dl>
<dd>HTML snippet to be included in the &lt;head&gt; section of each page. Can be set using <code>GITWEB_SITE_HTML_HEAD_STRING</code> at build time. No default value.</dl>
<p> $site_header</p>
<dl>
<dd>Name of a file with HTML to be included at the top of each page. Relative to the directory containing the <i>gitweb.cgi</i> script. Can be set using <code>GITWEB_SITE_HEADER</code> at build time. No default value.</dl>
<p> $site_footer</p>
<dl>
<dd>Name of a file with HTML to be included at the bottom of each page. Relative to the directory containing the <i>gitweb.cgi</i> script. Can be set using <code>GITWEB_SITE_FOOTER</code> at build time. No default value.</dl>
<p> $home_text</p>
<dl>
<dd>Name of a HTML file which, if it exists, is included on the gitweb projects overview page (&quot;projects_list&quot; view). Relative to the directory containing the gitweb.cgi script. Default value can be adjusted during build time using <code>GITWEB_HOMETEXT</code> variable. By default set to <i>indextext.html</i>.</dl>
<p> $projects_list_description_width</p>
<dl>
<dd>The width (in characters) of the &quot;Description&quot; column of the projects list. Longer descriptions will be truncated (trying to cut at word boundary); the full description is available in the <i>title</i> attribute (usually shown on mouseover). The default is 25, which might be too small if you use long project descriptions.</dl>
<p> $default_projects_order</p>
<dl>
<dd>Default value of ordering of projects on projects list page, which means the ordering used if you don&#8217;t explicitly sort projects list (if there is no &quot;o&quot; CGI query parameter in the URL). Valid values are &quot;none&quot; (unsorted), &quot;project&quot; (projects are by project name, i.e. path to repository relative to <code>$projectroot</code>), &quot;descr&quot; (project description), &quot;owner&quot;, and &quot;age&quot; (by date of most current commit). </p>
<p> Default value is &quot;project&quot;. Unknown value means unsorted.</dl>
<h3>Changing gitweb&#8217;s behavior</h3>
<p>These configuration variables control <i>internal</i> gitweb behavior. </p>
<p> $default_blob_plain_mimetype</p>
<dl>
<dd>Default mimetype for the blob_plain (raw) view, if mimetype checking doesn&#8217;t result in some other type; by default &quot;text/plain&quot;. Gitweb guesses mimetype of a file to display based on extension of its filename, using <code>$mimetypes_file</code> (if set and file exists) and <code>/etc/mime.types</code> files (see <code><a href="/docs/linux/man/5-mime-types/">mime.types</a></code>(5) manpage; only filename extension rules are supported by gitweb).</dl>
<p> $default_text_plain_charset</p>
<dl>
<dd>Default charset for text files. If this is not set, the web server configuration will be used. Unset by default.</dl>
<p> $fallback_encoding</p>
<dl>
<dd>Gitweb assumes this charset when a line contains non-UTF-8 characters. The fallback decoding is used without error checking, so it can be even &quot;utf-8&quot;. The value must be a valid encoding; see the <code><a href="//www.systutorials.com/docs/linux/man/3pm-Encoding::Supported/">Encoding::Supported</a></code>(3pm) man page for a list. The default is &quot;latin1&quot;, aka. &quot;iso-8859-1&quot;.</dl>
<p> @diff_opts</p>
<dl>
<dd>Rename detection options for git-diff and git-diff-tree. The default is (&#8216;-M&#8217;); set it to (&#8216;-C&#8217;) or (&#8216;-C&#8217;, &#8216;-C&#8217;) to also detect copies, or set it to () i.e. empty list if you don&#8217;t want to have renames detection. </p>
<p> <code>Note</code> that rename and especially copy detection can be quite CPU-intensive. Note also that non Git tools can have problems with patches generated with options mentioned above, especially when they involve file copies (&#8216;-C&#8217;) or criss-cross renames (&#8216;-B&#8217;).</dl>
<h3>Some optional features and policies</h3>
<p>Most of features are configured via <code>%feature</code> hash; however some of extra gitweb features can be turned on and configured using variables described below. This list beside configuration variables that control how gitweb looks does contain variables configuring administrative side of gitweb (e.g. cross-site scripting prevention; admittedly this as side effect affects how &quot;summary&quot; pages look like, or load limiting). </p>
<p> @git_base_url_list</p>
<dl>
<dd>List of Git base URLs. These URLs are used to generate URLs describing from where to fetch a project, which are shown on project summary page. The full fetch URL is &quot;<code>$git_base_url/$project</code>&quot;, for each element of this list. You can set up multiple base URLs (for example one for <code>git://</code> protocol, and one for <code>http://</code> protocol). </p>
<p> Note that per repository configuration can be set in <code>$GIT_DIR/cloneurl</code> file, or as values of multi-value <code>gitweb.url</code> configuration variable in project config. Per-repository configuration takes precedence over value composed from <code>@git_base_url_list</code> elements and project name. </p>
<p> You can setup one single value (single entry/item in this list) at build time by setting the <code>GITWEB_BASE_URL</code> build-time configuration variable. By default it is set to (), i.e. an empty list. This means that gitweb would not try to create project URL (to fetch) from project name.</dl>
<p> $projects_list_group_categories</p>
<dl>
<dd>Whether to enable the grouping of projects by category on the project list page. The category of a project is determined by the <code>$GIT_DIR/category</code> file or the <code>gitweb.category</code> variable in each repository&#8217;s configuration. Disabled by default (set to 0).</dl>
<p> $project_list_default_category</p>
<dl>
<dd>Default category for projects for which none is specified. If this is set to the empty string, such projects will remain uncategorized and listed at the top, above categorized projects. Used only if project categories are enabled, which means if <code>$projects_list_group_categories</code> is true. By default set to &quot;&quot; (empty string).</dl>
<p> $prevent_xss</p>
<dl>
<dd>If true, some gitweb features are disabled to prevent content in repositories from launching cross-site scripting (XSS) attacks. Set this to true if you don&#8217;t trust the content of your repositories. False by default (set to 0).</dl>
<p> $maxload</p>
<dl>
<dd>Used to set the maximum load that we will still respond to gitweb queries. If the server load exceeds this value then gitweb will return &quot;503 Service Unavailable&quot; error. The server load is taken to be 0 if gitweb cannot determine its value. Currently it works only on Linux, where it uses <code>/proc/loadavg</code>; the load there is the number of active tasks on the system &#8212; processes that are actually running &#8212; averaged over the last minute. </p>
<p> Set <code>$maxload</code> to undefined value (<code>undef</code>) to turn this feature off. The default value is 300.</dl>
<p> $omit_age_column</p>
<dl>
<dd>If true, omit the column with date of the most current commit on the projects list page. It can save a bit of I/O and a fork per repository.</dl>
<p> $omit_owner</p>
<dl>
<dd>If true prevents displaying information about repository owner.</dl>
<p> $per_request_config</p>
<dl>
<dd>If this is set to code reference, it will be run once for each request. You can set parts of configuration that change per session this way. For example, one might use the following code in a gitweb configuration file </p>
<dl>
<dd>
<pre>our $per_request_config = sub {
 $ENV{GL_USER} = $cgi-&gt;remote_user || &quot;gitweb&quot;;
};</pre>
</dl>
<p> If <code>$per_request_config</code> is not a code reference, it is interpreted as boolean value. If it is true gitweb will process config files once per request, and if it is false gitweb will process config files only once, each time it is executed. True by default (set to 1). </p>
<p> <code>NOTE</code>: <code>$my_url</code>, <code>$my_uri</code>, and <code>$base_url</code> are overwritten with their default values before every request, so if you want to change them, be sure to set this variable to true or a code reference effecting the desired changes. </p>
<p> This variable matters only when using persistent web environments that serve multiple requests using single gitweb instance, like mod_perl, FastCGI or Plackup.</dl>
<h3>Other variables</h3>
<p>Usually you should not need to change (adjust) any of configuration variables described below; they should be automatically set by gitweb to correct value. </p>
<p> $version</p>
<dl>
<dd>Gitweb version, set automatically when creating gitweb.cgi from gitweb.perl. You might want to modify it if you are running modified gitweb, for example </p>
<dl>
<dd>
<pre>our $version .= &quot; with caching&quot;;</pre>
</dl>
<p> if you run modified version of gitweb with caching support. This variable is purely informational, used e.g. in the &quot;generator&quot; meta header in HTML header.</dl>
<p> $my_url, $my_uri</p>
<dl>
<dd>Full URL and absolute URL of the gitweb script; in earlier versions of gitweb you might have need to set those variables, but now there should be no need to do it. See <code>$per_request_config</code> if you need to set them still.</dl>
<p> $base_url</p>
<dl>
<dd>Base URL for relative URLs in pages generated by gitweb, (e.g. <code>$logo</code>, <code>$favicon</code>, <code>@stylesheets</code> if they are relative URLs), needed and used <i>&lt;base href=&quot;$base_url&quot;&gt;</i> only for URLs with nonempty PATH_INFO. Usually gitweb sets its value correctly, and there is no need to set this variable, e.g. to $my_uri or &quot;/&quot;. See <code>$per_request_config</code> if you need to override it anyway.</dl>
<h2>Configuring Gitweb Features</h2>
<p>Many gitweb features can be enabled (or disabled) and configured using the <code>%feature</code> hash. Names of gitweb features are keys of this hash. </p>
<p> Each <code>%feature</code> hash element is a hash reference and has the following structure: </p>
<dl>
<dd>
<pre>&quot;&lt;feature_name&gt;&quot; =&gt; {
 &quot;sub&quot; =&gt; &lt;feature-sub (subroutine)&gt;,
 &quot;override&quot; =&gt; &lt;allow-override (boolean)&gt;,
 &quot;default&quot; =&gt; [ &lt;options&gt;... ]
},</pre>
</dl>
<p> Some features cannot be overridden per project. For those features the structure of appropriate <code>%feature</code> hash element has a simpler form: </p>
<dl>
<dd>
<pre>&quot;&lt;feature_name&gt;&quot; =&gt; {
 &quot;override&quot; =&gt; 0,
 &quot;default&quot; =&gt; [ &lt;options&gt;... ]
},</pre>
</dl>
<p> As one can see it lacks the &#8216;sub&#8217; element. </p>
<p> The meaning of each part of feature configuration is described below: </p>
<p> default</p>
<dl>
<dd>List (array reference) of feature parameters (if there are any), used also to toggle (enable or disable) given feature. </p>
<p> Note that it is currently <code>always</code> an array reference, even if feature doesn&#8217;t accept any configuration parameters, and &#8216;default&#8217; is used only to turn it on or off. In such case you turn feature on by setting this element to <code>[1]</code>, and torn it off by setting it to <code>[0]</code>. See also the passage about the &quot;blame&quot; feature in the &quot;Examples&quot; section. </p>
<p> To disable features that accept parameters (are configurable), you need to set this element to empty list i.e. <code>[]</code>.</dl>
<p> override</p>
<dl>
<dd>If this field has a true value then the given feature is overridable, which means that it can be configured (or enabled/disabled) on a per-repository basis. </p>
<p> Usually given &quot;&lt;feature&gt;&quot; is configurable via the <code>gitweb.&lt;feature&gt;</code> config variable in the per-repository Git configuration file. </p>
<p> <code>Note</code> that no feature is overridable by default.</dl>
<p> sub</p>
<dl>
<dd>Internal detail of implementation. What is important is that if this field is not present then per-repository override for given feature is not supported. </p>
<p> You wouldn&#8217;t need to ever change it in gitweb config file.</dl>
<h3>Features in <code>%feature</code></h3>
<p>The gitweb features that are configurable via <code>%feature</code> hash are listed below. This should be a complete list, but ultimately the authoritative and complete list is in gitweb.cgi source code, with features described in the comments. </p>
<p> blame</p>
<dl>
<dd>Enable the &quot;blame&quot; and &quot;blame_incremental&quot; blob views, showing for each line the last commit that modified it; see <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1). This can be very CPU-intensive and is therefore disabled by default. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.blame</code> configuration variable (boolean).</dl>
<p> snapshot</p>
<dl>
<dd>Enable and configure the &quot;snapshot&quot; action, which allows user to download a compressed archive of any tree or commit, as produced by <code><a href="/docs/linux/man/1-git-archive/">git-archive</a></code>(1) and possibly additionally compressed. This can potentially generate high traffic if you have large project. </p>
<p> The value of &#8216;default&#8217; is a list of names of snapshot formats, defined in <code>%known_snapshot_formats</code> hash, that you wish to offer. Supported formats include &quot;tgz&quot;, &quot;tbz2&quot;, &quot;txz&quot; (gzip/bzip2/xz compressed tar archive) and &quot;zip&quot;; please consult gitweb sources for a definitive list. By default only &quot;tgz&quot; is offered. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.snapshot</code> configuration variable, which contains a comma separated list of formats or &quot;none&quot; to disable snapshots. Unknown values are ignored.</dl>
<p> grep</p>
<dl>
<dd>Enable grep search, which lists the files in currently selected tree (directory) containing the given string; see <code><a href="/docs/linux/man/1-git-grep/">git-grep</a></code>(1). This can be potentially CPU-intensive, of course. Enabled by default. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.grep</code> configuration variable (boolean).</dl>
<p> pickaxe</p>
<dl>
<dd>Enable the so called pickaxe search, which will list the commits that introduced or removed a given string in a file. This can be practical and quite faster alternative to &quot;blame&quot; action, but it is still potentially CPU-intensive. Enabled by default. </p>
<p> The pickaxe search is described in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) (the description of <code>-S&lt;string&gt;</code> option, which refers to pickaxe entry in <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7) for more details). </p>
<p> This feature can be configured on a per-repository basis by setting repository&#8217;s <code>gitweb.pickaxe</code> configuration variable (boolean).</dl>
<p> show-sizes</p>
<dl>
<dd>Enable showing size of blobs (ordinary files) in a &quot;tree&quot; view, in a separate column, similar to what <code>ls -l</code> does; see description of <code>-l</code> option in <code><a href="/docs/linux/man/1-git-ls-tree/">git-ls-tree</a></code>(1) manpage. This costs a bit of I/O. Enabled by default. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.showSizes</code> configuration variable (boolean).</dl>
<p> patches</p>
<dl>
<dd>Enable and configure &quot;patches&quot; view, which displays list of commits in email (plain text) output format; see also <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1). The value is the maximum number of patches in a patchset generated in &quot;patches&quot; view. Set the <i>default</i> field to a list containing single item of or to an empty list to disable patch view, or to a list containing a single negative number to remove any limit. Default value is 16. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.patches</code> configuration variable (integer).</dl>
<p> avatar</p>
<dl>
<dd>Avatar support. When this feature is enabled, views such as &quot;shortlog&quot; or &quot;commit&quot; will display an avatar associated with the email of each committer and author. </p>
<p> Currently available providers are <code>&quot;gravatar&quot;</code> and <code>&quot;picon&quot;</code>. Only one provider at a time can be selected (<i>default</i> is one element list). If an unknown provider is specified, the feature is disabled. <code>Note</code> that some providers might require extra Perl packages to be installed; see <code>gitweb/INSTALL</code> for more details. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.avatar</code> configuration variable. </p>
<p> See also <code>%avatar_size</code> with pixel sizes for icons and avatars (&quot;default&quot; is used for one-line like &quot;log&quot; and &quot;shortlog&quot;, &quot;double&quot; is used for two-line like &quot;commit&quot;, &quot;commitdiff&quot; or &quot;tag&quot;). If the default font sizes or lineheights are changed (e.g. via adding extra CSS stylesheet in <code>@stylesheets</code>), it may be appropriate to change these values.</dl>
<p> email-privacy</p>
<dl>
<dd>Redact e-mail addresses from the generated HTML, etc. content. This obscures e-mail addresses retrieved from the author/committer and comment sections of the Git log. It is meant to hinder web crawlers that harvest and abuse addresses. Such crawlers may not respect robots.txt. Note that users and user tools also see the addresses as redacted. If Gitweb is not the final step in a workflow then subsequent steps may misbehave because of the redacted information they receive. Disabled by default.</dl>
<p> highlight</p>
<dl>
<dd>Server-side syntax highlight support in &quot;blob&quot; view. It requires <code>$highlight_bin</code> program to be available (see the description of this variable in the &quot;Configuration variables&quot; section above), and therefore is disabled by default. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.highlight</code> configuration variable (boolean).</dl>
<p> remote_heads</p>
<dl>
<dd>Enable displaying remote heads (remote-tracking branches) in the &quot;heads&quot; list. In most cases the list of remote-tracking branches is an unnecessary internal private detail, and this feature is therefore disabled by default. <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1), which is usually used to browse local repositories, enables and uses this feature. </p>
<p> This feature can be configured on a per-repository basis via repository&#8217;s <code>gitweb.remote_heads</code> configuration variable (boolean).</dl>
<p> The remaining features cannot be overridden on a per project basis. </p>
<p> search</p>
<dl>
<dd>Enable text search, which will list the commits which match author, committer or commit text to a given string; see the description of <code>&#8211;author</code>, <code>&#8211;committer</code> and <code>&#8211;grep</code> options in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) manpage. Enabled by default. </p>
<p> Project specific override is not supported.</dl>
<p> forks</p>
<dl>
<dd>If this feature is enabled, gitweb considers projects in subdirectories of project root (basename) to be forks of existing projects. For each project <code>$projname.git</code>, projects in the <code>$projname/</code> directory and its subdirectories will not be shown in the main projects list. Instead, a &#8216;+&#8217; mark is shown next to <code>$projname</code>, which links to a &quot;forks&quot; view that lists all the forks (all projects in <code>$projname/</code> subdirectory). Additionally a &quot;forks&quot; view for a project is linked from project summary page. </p>
<p> If the project list is taken from a file (<code>$projects_list</code> points to a file), forks are only recognized if they are listed after the main project in that file. </p>
<p> Project specific override is not supported.</dl>
<p> actions</p>
<dl>
<dd>Insert custom links to the action bar of all project pages. This allows you to link to third-party scripts integrating into gitweb. </p>
<p> The &quot;default&quot; value consists of a list of triplets in the form &#8216;(&quot;&lt;label&gt;&quot;, &quot;&lt;link&gt;&quot;, &quot;&lt;position&gt;&quot;)` where &quot;position&quot; is the label after which to insert the link, &quot;link&quot; is a format string where <code>%n</code> expands to the project name, <code>%f</code> to the project path within the filesystem (i.e. &quot;$projectroot/$project&quot;), <code>%h</code> to the current hash (&#8216;h&#8217; gitweb parameter) and &#8216;%b` to the current hash base (&#8216;hb&#8217; gitweb parameter); &#8216;%%` expands to &#8216;%&#8217;. </p>
<p> For example, at the time this page was written, the m[blue]<code><a rel="nofollow" href="http://repo.or.cz">http://repo.or.cz</a></code>m[] Git hosting site set it to the following to enable graphical log (using the third party tool <code>git-browser</code>): </p>
<dl>
<dd>
<pre>$feature{'actions'}{'default'} =
 [ ('graphiclog', '/git-browser/by-commit.html?r=%n', 'summary')];</pre>
</dl>
<p> This adds a link titled &quot;graphiclog&quot; after the &quot;summary&quot; link, leading to <code>git-browser</code> script, passing <code>r=&lt;project&gt;</code> as a query parameter. </p>
<p> Project specific override is not supported.</dl>
<p> timed</p>
<dl>
<dd>Enable displaying how much time and how many Git commands it took to generate and display each page in the page footer (at the bottom of page). For example the footer might contain: &quot;This page took 6.53325 seconds and 13 Git commands to generate.&quot; Disabled by default. </p>
<p> Project specific override is not supported.</dl>
<p> javascript-timezone</p>
<dl>
<dd>Enable and configure the ability to change a common time zone for dates in gitweb output via JavaScript. Dates in gitweb output include authordate and committerdate in &quot;commit&quot;, &quot;commitdiff&quot; and &quot;log&quot; views, and taggerdate in &quot;tag&quot; view. Enabled by default. </p>
<p> The value is a list of three values: a default time zone (for if the client hasn&#8217;t selected some other time zone and saved it in a cookie), a name of cookie where to store selected time zone, and a CSS class used to mark up dates for manipulation. If you want to turn this feature off, set &quot;default&quot; to empty list: <code>[]</code>. </p>
<p> Typical gitweb config files will only change starting (default) time zone, and leave other elements at their default values: </p>
<dl>
<dd>
<pre>$feature{'javascript-timezone'}{'default'}[0] = &quot;utc&quot;;</pre>
</dl>
<p> The example configuration presented here is guaranteed to be backwards and forward compatible. </p>
<p> Time zone values can be &quot;local&quot; (for local time zone that browser uses), &quot;utc&quot; (what gitweb uses when JavaScript or this feature is disabled), or numerical time zones in the form of &quot;+/-HHMM&quot;, such as &quot;+0200&quot;. </p>
<p> Project specific override is not supported.</dl>
<p> extra-branch-refs</p>
<dl>
<dd>List of additional directories under &quot;refs&quot; which are going to be used as branch refs. For example if you have a gerrit setup where all branches under refs/heads/ are official, push-after-review ones and branches under refs/sandbox/, refs/wip and refs/other are user ones where permissions are much wider, then you might want to set this variable as follows: </p>
<dl>
<dd>
<pre>$feature{'extra-branch-refs'}{'default'} =
 ['sandbox', 'wip', 'other'];</pre>
</dl>
<p> This feature can be configured on per-repository basis after setting $feature{<i>extra-branch-refs</i>}{<i>override</i>} to true, via repository&#8217;s <code>gitweb.extraBranchRefs</code> configuration variable, which contains a space separated list of refs. An example: </p>
<dl>
<dd>
<pre>[gitweb]
 extraBranchRefs = sandbox wip other</pre>
</dl>
<p> The gitweb.extraBranchRefs is actually a multi-valued configuration variable, so following example is also correct and the result is the same as of the snippet above: </p>
<dl>
<dd>
<pre>[gitweb]
 extraBranchRefs = sandbox
 extraBranchRefs = wip other</pre>
</dl>
<p> It is an error to specify a ref that does not pass &quot;git check-ref-format&quot; scrutiny. Duplicated values are filtered.</dl>
<h2>Examples</h2>
<p>To enable blame, pickaxe search, and snapshot support (allowing &quot;tar.gz&quot; and &quot;zip&quot; snapshots), while allowing individual projects to turn them off, put the following in your GITWEB_CONFIG file: $known_snapshot_formats{&#8216;zip&#8217;}{&#8216;disabled&#8217;} = 1;<br />
$known_snapshot_formats{&#8216;tgz&#8217;}{&#8216;compressor&#8217;} = [&#8216;gzip&#8217;,&#8217;-6&#8242;]; If you allow overriding for the snapshot feature, you can specify which snapshot formats are globally disabled. You can also add any command-line options you want (such as setting the compression level). For instance, you can disable Zip compressed snapshots and set <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) to run at level 6 by adding the following lines to your gitweb configuration file: </p>
<pre><code>$known_snapshot_formats{'zip'}{'disabled'} = 1;
$known_snapshot_formats{'tgz'}{'compressor'} = ['gzip','-6'];</code></pre>
<h2>Bugs</h2>
<p>Debugging would be easier if the fallback configuration file (<code>/etc/gitweb.conf</code>) and environment variable to override its location (<i>GITWEB_CONFIG_SYSTEM</i>) had names reflecting their &quot;fallback&quot; role. The current names are kept to avoid breaking working setups.</p>
<h2>Environment</h2>
<p>The location of per-instance and system-wide configuration files can be overridden using the following environment variables: </p>
<p> GITWEB_CONFIG</p>
<dl>
<dd>Sets location of per-instance configuration file.</dl>
<p> GITWEB_CONFIG_SYSTEM</p>
<dl>
<dd>Sets location of fallback system-wide configuration file. This file is read only if per-instance one does not exist.</dl>
<p> GITWEB_CONFIG_COMMON</p>
<dl>
<dd>Sets location of common system-wide configuration file.</dl>
<h2>Files</h2>
<p>gitweb_config.perl</p>
<dl>
<dd>This is default name of per-instance configuration file. The format of this file is described above.</dl>
<p> /etc/gitweb.conf</p>
<dl>
<dd>This is default name of fallback system-wide configuration file. This file is used only if per-instance configuration variable is not found.</dl>
<p> /etc/gitweb-common.conf</p>
<dl>
<dd>This is default name of common system-wide configuration file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1), <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1) </p>
<p> <i>gitweb/README</i>, <i>gitweb/INSTALL</i></p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
