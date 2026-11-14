---
title: "mod_gridsite(8)"
name: "mod_gridsite"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mod_gridsite/"
description: "mod_gridsite – Grid extensions to Apache httpd"
---

<p><code>mod_gridsite</code> &#8211; Grid extensions to Apache httpd</p>
<h2>Synopsis</h2>
<p><code>LoadModule gridsite_module mod_gridsite.so </code></p>
<h2>Description</h2>
<p><code>mod_gridsite</code> is an Apache 2.0 module which enforces access control via Grid Access Control Lists, and X.509, GSI or VOMS credentials. mod_gridsite also gives Apache built-in support for the HTTP PUT and DELETE methods, and formatting of HTML pages with standard headers and footers. Since mod_gridsite access control within Apache itself, Grid authorization and the associated verified credentials are available to all technologies supported by Apache, including static file serving, SSI, CGI, PHP, mod_perl and Java servlets via a connector to Tomcat. Operation of mod_gridsite can be configured using runtime directives in Apache&#8217;s standard httpd.conf configuration file. The module must first be loaded with a LoadModule directive: LoadModule gridsite_module /PATH/TO/MODULES/mod_gridsite.so The module&#8217;s behaviour is then controlled by GridSite&#8230; directives within Apache &lt;Directory &#8230;&gt; sections, allowing different directories to use GridSite features in different ways. </p>
<h2>Directives</h2>
<dl>
<dt>GridSiteIndexes on|off</p>
<dd>Determines whether GridSite generates HTML directory listings. These have some advantages over standard Apache directory listings (eg the displayed filenames are never truncated) and will include standard headers and footers if GridSiteHtmlFormat is on. (Default: GridSiteIndexes off) </p>
<dt>GridSiteIndexHeader file</p>
<dd>If the named file is found in the directory being listed, the file is included verbatim at the top of the listing and excluded from the file-by-file listing. The file can either be HTML or plain text (in which case browsers will be treat it as one HTML paragraph.) (Default: none) </p>
<dt>GridSiteHtmlFormat on|off</p>
<dd>Determines where HTML pages receive additional formatting before being sent to the client. This includes the &quot;Last modified&quot;, &quot;View page history&quot;, &quot;Switch to HTTP(S)&quot;, &quot;Print View&quot; and &quot;Built with GridSite&quot; footer elements. If header and footer files are found, they will be used too. (Default: GridSiteHtmlFormat off) </p>
<dt>GridSiteHeadFile file</p>
<dd>
<dt>GridSiteFootFile file</p>
<dd>Set the filenames to be used for as standard headers and footers for HTML pages. If the file name begins with &quot;/&quot; then this is used as the absolute path to that file to be used. Otherwise, for each HTML page, the directory of that page is tried first, and then parent directories in ascending order until a header / footer file is found. Header files are inserted in place of HTML &lt;body[ &#8230;]&gt; tags; footer files in place of &lt;/body&gt;. (These standard files should each include the appropriate body tag as a replacement.) (Defaults: GridSiteHeadFile gridsitehead.txt, GridSiteFootFile gridsitefoot.txt) </p>
<dt>GridSiteAuth on|off</p>
<dd>Enables GridSite access control features, using GACL files. The files are named .gacl and are per-directory. The current directory is tried and then parent directories in ascending order until a .gacl file is found. (Default: GridSiteAuth off) </p>
<dt>GridSiteAutoPasscode on|off</p>
<dd>Whether to automatically issue passcodes in response to HTTPS requests made using a full X.509 certificate (not a GSI proxy.) (Default: GridSiteAutoPasscode on) </p>
<dt>GridSiteRequirePasscode on|off</p>
<dd>Whether to require passcode cookies when processing HTTPS requests made using a full X.509 certificate (not a GSI proxy.) (Default: GridSiteRequirePasscode off) </p>
<dt>GridSiteZoneSlashes number</p>
<dd>How many slashes to include in passcode paths. The path is the prefix of REQUEST_URI that includes that number of slashes. Path matching is checked by mod_gridsite in addition to any selection of cookies by path made by the browser. (Default: GridSiteZoneSlashes 1) </p>
<dt>GridSiteAdminList uri</p>
<dd>All members of the DN List with name &quot;uri&quot; receive the full set of permissions, irrespective of per-directory .gacl files. People in this group have full control over the whole site. (Default: none) </p>
<dt>GridSiteGSIProxyLimit limit</p>
<dd>When using GSI Proxy credentials, proxies with delegation depth greater than &quot;limit&quot; will be ignored by mod_gridsite authorization decisions. A limit of zero implies only full X.509 certificates (and no proxies) will be accepted. A limit of 1 implies that only the initial proxy, usually created on the user&#8217;s own machine, is acceptable. Higher levels lead to proxies on remote machines, eg used by running jobs, being accepted. (Default: GridSiteGSIProxyLimit 1) </p>
<dt>GridSiteMethods [GET] [PUT] [DELETE] [MOVE]</p>
<dd>Specifies which HTTP methods are supported by GridSite. GET (and HEAD) are always supported. PUT and DELETE support is turned on by this directive, subject to a positive statement that write permission is allowed for the directory in question, by a GACL file. (Default: GridSite GET) </p>
<dt>GridSiteDNlists directory1[:directory2[:directory3]&#8230;]</p>
<dd>Sets up the DN List path used by GACL for evaluating &lt;dn-list&gt; credentials. If this directive is not used, then GACL will use the GRST_DN_LISTS variable from Apache&#8217;s own environment. If that is not set either, then /etc/grid-security/dn-lists is searched. (Default: none) </p>
<dt>GridSiteDNlistsURI uri</p>
<dd>If GridSiteDNlistsURI is used, then the URI given appears to be populated with all the DN lists on the current DN lists path which match the current server. That is, for server <a rel="nofollow" href="https://example.org/">https://example.org/</a> with DN lists URI /dn-lists/, all DN lists with URLs starting <a rel="nofollow" href="https://example.org/dn-lists/">https://example.org/dn-lists/</a> will appear to be present in /dn-lists/, irrespective of where in the path they are stored. (Default: none) &lt;p&gt; </p>
<dt>GridSiteAdminURI uri</p>
<dd>GridSiteAdminURI gives the absolute URI on the server of the GridSite Admin CGI program, which is used for file management, HTML and GACL editing. This should be used in conjunction with the standard Apache directive ScriptAlias to map that URI to the real-gridsite-admin.cgi executable. For example: </p>
<p> ScriptAlias /real-gridsite-admin.cgi /PATH/TO/real-gridsite-admin.cgi </p>
<p> This URI is always reached by an internal redirection from the value set by GridSiteAdminFile, and is never visible to users. (Default: none) </p>
<dt>GridSiteAdminFile cgifilename</p>
<dd>If GridSiteAdminURI is set, then the cgifilename of GridSiteAdminFile appears to be present in all directories when explicitly requested (it does not appear in directory listings.) Requests for these ghost CGI URIs are internally redirected to the value set by GridSiteAdminURI. (Default: GridSiteAdminFile gridsite-admin.cgi) </p>
<dt>GridSiteEnvs on|off</p>
<dd>This makes mod_gridsite export several variables into the environment of CGI programs and other dynamic content systems. The variable names are listed below. For gridsite-admin.cgi mechanism to work, this switch must be left in its default state of on. (Default: GridSiteEnvs on) </p>
<dt>GridSiteEditable [ext1 [ext2 [ext3] &#8230;]]]</p>
<dd>A space-separated list of file extensions which can safely be edited by the GridSite Text/HTML editor. The extensions are given without the initial dot. This directive must apply to the gridsite-admin.cgi executable, rather than just to the files it manages. This is most easily achieved by placing GridSiteEditable in the main section of the virtual host, outside any Directory or Location containers. (Default: GridSiteEditable txt shtml html htm css js php jsp) </p>
<dt>GridSiteHelpURI uri</p>
<dd>If set, gives the URI to use for &quot;Website Help&quot; links in HTML page footers. (Default: none) </p>
<dt>GridSiteLoginURI uri</p>
<dd>If set, gives the URI prefix to use for login/logout links in page footers. The text &quot;Login/Logout&quot; will be a link to the prefix followed by the value of REQUEST_URI for the page in question. (Default: none) </p>
<dt>GridSiteLink on|off</p>
<dd>Turns off the link in the HTML page footers which gives credit to GridSite. (Default: GridSiteLink on) </p>
<dt>GridSiteUnzip path</p>
<dd>If &quot;path&quot; is set by this directive, then real-gridsite-admin.cgi will offer to list the contents of .zip archives on the server. Users with write access are able to unpack the contents into the same directory as the .zip file. The value of &amp;quot;path&amp;quot; must point to the location of the unzip binary. (Default: none) </p>
<dt>GridSiteGridHTTP on|off</p>
<dd>Enable GridHTTP for this server, virtual server or directory: HTTPS requests made with the header <code>Upgrade: GridHTTP/1.0</code> will be redirected to an HTTP version of the file. (Default: off) </p>
<dt>GridSiteGridHTTPport port</p>
<dd>Sets the port to use for the unencrypted HTTP component of GridHTTP HTTPS-&gt;HTTP transfers. The same setting will be used for all virtual hosts which support GridHTTP. (Default: 777) </p>
<dt>GridSiteSessionsDir path</p>
<dd>Location of authentication cookies and SSL session credentials directory, relative to ServerRoot. Used by GridHTTP to record the credentials obtained via HTTPS, and available to the corresponding HTTP request or subsequent HTTPS requests following a session restart. (Default: /var/www/sessions) </p>
<dt>GridSiteACLFormat GACL|XACML</p>
<dd>Format to use when writing .gacl files. (Both formats are automatically recognised when reading.) (Default: GACL) </p>
<dt>GridSiteACLPath path</p>
<dd>Specify the absolute or relative (to ServerRoot) path of the ACL file governing this section of the server&#8217;s URL space. This can be applied to virtual URL spaces provided by other modules, such as DAV or SVN, using the Apache &lt;Location&gt; container. If the path contains %0, it is replaced by this virtual server&#8217;s hostname. If it contains %1, %2, &#8230; it is replaced with the 1st, 2nd, &#8230; component of the request&#8217;s URI, separated by slashes and counting from immediately after the initial slash. </p>
<dt>GridSiteExecMethod nosetuid|suexec|X509DN|directory</p>
<dd>Execution strategy for CGI scripts and executables. For options other than nosetuid, suexec (or gsexec renamed suexec) must installed. For X509DN and directory, gsexec must be installed, as suexec. See <code><a href="/docs/linux/man/8-gsexec/">gsexec</a>(8)</code> for an explanation of the different execution strategies. (Default: nosetuid) </p>
<dt>GridSiteUserGroup user group</p>
<dd>Unix user and group when using suexec (or gsexec as suexec.) This is equivalent to the suexec SuexecUserGroup directive, but can be specified on a per-directory basis. (Default: none) </p>
<dt>GridSiteDiskMode GroupNone|GroupRead|GroupWrite WorldNone|WorldRead</p>
<dd>The file creation permissions mode, taking two arguments to specify the group and other permissions. The mode always includes read and write permission for the CGI user itself. (Default: GroupNone WorldNone) </p>
<dt>GridSiteCastUniPort port</p>
<dd>The <code>UDP</code> unicast port to listen on for HTCP queries, and from which to send replies to HTCP unicast and multicast queries. Ideally, this should be a privileged port below 1024. This directive may not appear within a virtual server. (Default: 777) </p>
<dt>GridSiteCastGroup group[:port]</p>
<dd>A UDP multicast group on which to listen for HTCP queries, plus an optional port. If no port is given, then 777 is used. Multiple GridSiteCastGroup directives can be given to cause the UDP responder to listen to more than one multicast group. This directive may not appear within a virtual server. </p>
<dt>GridSiteCastAlias URL-prefix path-prefix</p>
<dd>Maps SiteCast generic URLs to the local filesystem. When processing HTCP queries, matching SiteCast URLs will have URL-prefix stripped off and the remaining portion of the URL added to path-prefix to construct a local path and filename. If a file is found with that name, a SiteCast HTCP response will be returned to the querying host. Otherwise the queries are ignored. This directive may appear within virtual servers, and the virtual server&#8217;s servername and first port will determine the host and port name used to construct the transfer URL. </p>
</dl>
<h2>Environment</h2>
<p>The following variables are present in the environment of CGI programs and other dynamic content systems if the <code>GridSiteEnvs on</code> directive is in effect. </p>
<dl>
<dt>GRST_PERM</p>
<dd>Numerical value of the permission bit-map obtained by comparing the user with the GACL in force. (These should be tested using the GRSTgaclPermHasXXXX functions from GACL.) </p>
<dt>GRST_PASSCODE_COOKIE</p>
<dd>Value of GRIDHTTP_PASSCODE cookie that should be returned when using a double-submit cookie procedure to guard against Cross Site Request Forgery (CSRF) attacks. This is only set if a valid passcode file was found in the server&#8217;s sessions directory. </p>
<dt>GRST_ADMIN_LIST</p>
<dd>URI of the DN List, listing people with full admin and write access to the whole site. </p>
<dt>GRST_GSIPROXY_LIMIT</p>
<dd>Maximum valid delegation level for GSI Proxies. </p>
<dt>GRST_DIR_PATH</p>
<dd>Absolute path in the local filesystem to the directory holding the file being requested. </p>
<dt>GRST_DESTINATION_TRANSLATED</p>
<dd>Present if a WebDAV <code>Destination:</code> header was given in the request with a local URL. Contains the translation of the URL given into an absolute path in the local filesystem. </p>
<dt>GRST_HELP_URI</p>
<dd>URI of website help pages set by GridSiteHelpURI directive. </p>
<dt>GRST_ADMIN_FILE</p>
<dd>Filename of per-directory ghost gridsite-admin.cgi program. (This is used by real-gridsite-admin.cgi to construct links in its pages.) </p>
<dt>GRST_EDITABLE</p>
<dd>Space-separated list of extensions which can safely be edited with a Text/HTML editor. </p>
<dt>GRST_HEAD_FILE and GRST_FOOT_FILE</p>
<dd>Filenames of standard header and footer files. </p>
<dt>GRST_DN_LISTS</p>
<dd>DN lists search path. </p>
<dt>GRST_DN_LISTS_URI</p>
<dd>Directory of virtual URIs used to publish this site&#8217;s DN Lists. </p>
<dt>GRST_UNZIP</p>
<dd>Full path to the <code><a href="/docs/linux/man/1-unzip/">unzip</a>(1)</code> binary, used to list and unpack .zip files. </p>
<dt>GRST_NO_LINK</p>
<dd>If set, do not include credit links to GridSite in page footers. </p>
<dt>GRST_ACL_FORMAT</p>
<dd>Format to use when writing .gacl files: either GACL or XACML. </p>
<dt>GRST_EXEC_METHOD</p>
<dd>Specified by <code>GridSiteExecMethod</code> either suexec, X509DN or directory. </p>
<dt>GRST_EXEC_DIRECTORY</p>
<dd>The directory containing the CGI script or executable (used by gsexec to determine which pool account to use in directory mapping mode.) </p>
<dt>GRST_DISK_MODE</p>
<dd>The <code>Apache</code> disk permission modes bit pattern, in hexadecimal, starting with 0x. (Similar to the Unix bit pattern, except with hexadecimal rather than octal values: eg 0x600 [Apache] vs 0600 [Unix] are both read/write for user only.) </p>
</dl>
<h2>Author</h2>
<p>Andrew McNab &lt;Andrew.McNab [at] manchester.ac.uk&gt; </p>
<p> mod_gridsite is part of GridSite: <a rel="nofollow" href="http://www.gridsite.org/">http://www.gridsite.org/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-htcp/">htcp</a>(1),</code> <code><a href="/docs/linux/man/8-httpd/">httpd</a>(8),</code> <code><a href="/docs/linux/man/8-gsexec/">gsexec</a>(8)</code> </p>
