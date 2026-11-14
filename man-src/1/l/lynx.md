---
title: "lynx(1)"
name: "lynx"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lynx/"
description: "lynx – a general purpose distributed information browser for the World Wide Web"
---

<h2 class="name">NAME</h2>
<p> lynx &#8211; a general purpose distributed information browser for the World Wide Web </p>
<h2>SYNOPSIS</h2>
<p> <code>lynx </code><i>[options] [optional paths or URLs]</i> </p>
<p> <code>lynx </code><i>[options] [path or URL]</i> <code>-get_data</code><br />
 <i>data</i><br />
 <code>&#8212;</code> </p>
<p> <code>lynx </code><i>[options] [path or URL]</i> <code>-post_data</code><br />
 <i>data</i><br />
 <code>&#8212;</code> </p>
<p> Use &#8220;lynx -help&#8221; to display a complete list of current options.</p>
<h2>DESCRIPTION</h2>
<p> <i>Lynx</i> is a fully-featured World Wide Web (WWW) client for users running cursor-addressable, character-cell display devices (e.g., vt100 terminals, vt100 emulators running on Windows 95/NT/XP/7/8 or any POSIX platform, or any other &#8220;curses-oriented&#8221; display). It will display hypertext markup language (HTML) documents containing links to files residing on the local system, as well as files residing on remote systems running Gopher, HTTP, FTP, WAIS, and NNTP servers. Current versions of <i>Lynx</i> run on Unix, VMS, Windows 95/NT/XP/7/8, DOS DJGPP and OS/2. </p>
<p> <i>Lynx</i> can be used to access information on the World Wide Web, or to build information systems intended primarily for local access. For example, <i>Lynx</i> has been used to build several Campus Wide Information Systems (CWIS). In addition, <i>Lynx</i> can be used to build systems isolated within a single LAN.</p>
<h2>OPTIONS</h2>
<p> At start up, <i>Lynx</i> will load any local file or remote URL specified at the command line. For help with URLs, press &#8220;<code>?</code>&#8221; or &#8220;<code>H</code>&#8221; while running <i>Lynx</i>. Then follow the link titled, &#8220;Help on URLs.&#8221; </p>
<p> If more than one local file or remote URL is listed on the command line, <i>Lynx</i> will open only the last interactively. All of the names (local files and remote URLs) are added to the <code>G)oto</code> history. </p>
<p> <i>Lynx</i> uses only long option names. Option names can begin with double dash &#8220;&#8211;&#8221; as well, underscores and dashes can be intermixed in option names (in the reference below, options are shown with one dash &#8220;-&#8221; before them, and with underscores &#8220;_&#8221;). </p>
<p> <i>Lynx</i> provides many command-line options. Some options require a value (string, number or keyword). These are noted in the reference below. The other options set boolean values in the program. There are three types of boolean options: set, unset and toggle. If no option value is given, these have the obvious meaning: set (to true), unset (to false), or toggle (between true/false). For any of these, an explicit value can be given in different forms to allow for operating system constraints, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
<code>-center:off</code>
<code>-center=off</code>
<code>-center-</code>
</pre>
<p>&nbsp;.in -4 </p>
<p> <i>Lynx</i> recognizes &#8220;1&#8221;, &#8220;+&#8221;, &#8220;on&#8221; and &#8220;true&#8221; for true values, and &#8220;0&#8221;, &#8220;-&#8221;, &#8220;off&#8221; and &#8220;false&#8221; for false values. Other option-values are ignored. </p>
<p> The default boolean, number and string option values that are compiled into <i>Lynx</i> are displayed in the help-message provided by <code>lynx -help</code>. Some of those may differ according to how <i>Lynx</i> was built; see the help message itself for these values. The <code>-help</code> option is processed in the third pass of options-processing, so any option which sets a value, as well as runtime configuration values are reflected in the help-message.</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> If the argument is only &#8220;-&#8221;, then <i>Lynx</i> expects to receive the arguments from the standard input. This is to allow for the potentially very long command line that can be associated with the <code>-get_data</code> or <code>-post_data</code> arguments (see below). It can also be used to avoid having sensitive information in the invoking command line (which would be visible to other processes on most systems), especially when the <code>-auth</code> or <code>-pauth</code> options are used.</p>
<dt><code>-accept_all_cookies</code></p>
<dd> accept all cookies.</p>
<dt><code>-anonymous</code></p>
<dd> apply restrictions for anonymous account, see also <code>-restrictions</code>.</p>
<dt><code>-assume_charset</code>=<i>MIMEname</i></p>
<dd> charset for documents that do not specify it.</p>
<dt><code>-assume_local_charset</code>=<i>MIMEname</i></p>
<dd> charset assumed for local files, i.e., files which <i>Lynx</i> creates such as internal pages for the options menu.</p>
<dt><code>-assume_unrec_charset</code>=<i>MIMEname</i></p>
<dd> use this instead of unrecognized charsets.</p>
<dt><code>-auth</code>=<i>ID</i>:<i>PASSWD</i></p>
<dd> set authorization ID and password for protected documents at startup. Be sure to protect any script files which use this switch.</p>
<dt><code>-base</code></p>
<dd> prepend a request URL comment and BASE tag to text/html outputs for <code>-source</code> dumps.</p>
<dt><code>-bibhost</code>=<i>URL</i></p>
<dd> specify a local bibp server (default <a rel="nofollow" href="http://bibhost/">http://bibhost/</a>).</p>
<dt><code>-blink</code></p>
<dd> forces high intensity background colors for color mode, if available and supported by the terminal. This applies to the <code>slang</code> library (for a few terminal emulators), or to OS/2 EMX with <code>ncurses</code>.</p>
<dt><code>-book</code></p>
<dd> use the bookmark page as the startfile. The default or command line startfile is still set for the Main screen command, and will be used if the bookmark page is unavailable or blank.</p>
<dt><code>-buried_news</code></p>
<dd> toggles scanning of news articles for buried references, and converts them to news links. Not recommended because email addresses enclosed in angle brackets will be converted to false news links, and uuencoded messages can be trashed.</p>
<dt><code>-cache</code>=<i>NUMBER</i></p>
<dd> set the NUMBER of documents cached in memory. The default is 10.</p>
<dt><code>-case</code></p>
<dd> enable case-sensitive string searching.</p>
<dt><code>-center</code></p>
<dd> Toggle center alignment in HTML TABLE.</p>
<dt><code>-cfg</code>=<i>FILENAME</i></p>
<dd> specifies a <i>Lynx</i> configuration file other than the default lynx.cfg.</p>
<dt><code>-child</code></p>
<dd> exit on left-arrow in startfile, and disable save to disk and associated print/mail options.</p>
<dt><code>-child_relaxed</code></p>
<dd> exit on left-arrow in startfile, but allow save to disk and associated print/mail options.</p>
<dt><code>-cmd_log</code>=<i>FILENAME</i></p>
<dd> write keystroke commands and related information to the specified file.</p>
<dt><code>-cmd_script</code>=<i>FILENAME</i></p>
<dd> read keystroke commands from the specified file. You can use the data written using the <code>-cmd_log</code> option. <i>Lynx</i> will ignore other information which the command-logging may have written to the logfile. Each line of the command script contains either a comment beginning with &#8220;#&#8221;, or a keyword:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>exit</code></p>
<dd> causes the script to stop, and forces <i>Lynx</i> to exit immediately.</p>
<dt><code>key</code></p>
<dd> the character value, in printable form. Cursor and other special keys are given as names, e.g., &#8220;Down Arrow&#8221;. Printable 7-bit ASCII codes are given as-is, and hexadecimal values represent other 8-bit codes.</p>
<dt><code>set</code></p>
<dd> followed by a &#8220;name=value&#8221; allows one to override values set in the lynx.cfg or .lynxrc files. <i>Lynx</i> tries the cfg-file setting first.</dl>
</dl>
<dt><code>-collapse_br_tags</code></p>
<dd> toggles collapsing of BR tags.</p>
<dt><code>-color</code></p>
<dd> forces color mode on, if available. Default color control sequences which work for many terminal types are assumed if the terminal capability description does not specify how to handle color. <i>Lynx</i> needs to be compiled with the <code>slang</code> library for this flag, it is equivalent to setting the <code>COLORTERM</code> environment variable. (If color support is instead provided by a color-capable curses library like <code>ncurses</code>, <i>Lynx</i> relies completely on the terminal description to determine whether color mode is possible, and this flag is not needed and thus unavailable.) A saved show_color=always setting found in a .lynxrc file at startup has the same effect. A saved show_color=never found in .lynxrc on startup is overridden by this flag.</p>
<dt><code>-connect_timeout</code>=<i>N</i></p>
<dd> Sets the connection timeout, where N is given in seconds.</p>
<dt><code>-cookie_file</code>=<i>FILENAME</i></p>
<dd> specifies a file to use to read cookies. If none is specified, the default value is ~/.lynx_cookies for most systems, but ~/cookies for MS-DOS.</p>
<dt><code>-cookie_save_file</code>=<i>FILENAME</i></p>
<dd> specifies a file to use to store cookies. If none is specified, the value given by <code>-cookie_file</code> is used.</p>
<dt><code>-cookies</code></p>
<dd> toggles handling of Set-Cookie headers.</p>
<dt><code>-core</code></p>
<dd> toggles forced core dumps on fatal errors. Turn this option off to ask <i>Lynx</i> to force a core dump if a fatal error occurs.</p>
<dt><code>-crawl</code></p>
<dd> with <code>-traversal,</code> output each page to a file. with <code>-dump</code>, format output as with <code>-traversal</code>, but to the standard output.</p>
<dt><code>-curses_pads</code></p>
<dd> toggles the use of curses &#8220;pad&#8221; feature which supports left/right scrolling of the display. The feature is normally available for curses configurations, but inactive. To activate it, use the &#8220;|&#8221; character or the LINEWRAP_TOGGLE command. Toggling this option makes the feature altogether unavailable.</p>
<dt><code>-debug_partial</code></p>
<dd> separate incremental display stages with MessageSecs delay</p>
<dt><code>-default_colors</code></p>
<dd> toggles the default-colors feature which is normally set in the lynx.cfg file.</p>
<dt><code>-delay</code></p>
<dd> add DebugSecs delay after each progress-message</p>
<dt><code>-display</code>=<i>DISPLAY</i></p>
<dd> set the display variable for X rexec-ed programs.</p>
<dt><code>-display_charset</code>=<i>MIMEname</i></p>
<dd> set the charset for the terminal output.</p>
<dt><code>-dont_wrap_pre</code></p>
<dd> inhibit wrapping of text when <code>-dump</code>&#8216;ing and <code>-crawl</code>&#8216;ing, mark wrapped lines of &lt;pre&gt; in interactive session.</p>
<dt><code>-dump</code></p>
<dd> dumps the formatted output of the default document or those specified on the command line to standard output. Unlike interactive mode, all documents are processed. This can be used in the following way:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
lynx <code>-dump</code> <a rel="nofollow" href="http://www.subir.com/lynx.html">http://www.subir.com/lynx.html</a>
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> Files specified on the command line are formatted as HTML if their names end with one of the standard web suffixes such as &#8220;.htm&#8221; or &#8220;.html&#8221;. Use the <code>-force_html</code> option to format files whose names do not follow this convention.</p>
<dt><code>-editor</code>=<i>EDITOR</i></p>
<dd> enable external editing, using the specified EDITOR. (vi, ed, emacs, etc.)</p>
<dt><code>-emacskeys</code></p>
<dd> enable emacs-like key movement.</p>
<dt><code>-enable_scrollback</code></p>
<dd> toggles compatibility with communication programs&#8217; scrollback keys (may be incompatible with some curses packages).</p>
<dt><code>-error_file</code>=<i>FILE</i></p>
<dd> define a file where <i>Lynx</i> will report HTTP access codes.</p>
<dt><code>-exec</code></p>
<dd> enable local program execution (normally not configured).</p>
<dt><code>-fileversions</code></p>
<dd> include all versions of files in local VMS directory listings.</p>
<dt><code>-find_leaks</code></p>
<dd> toggle memory leak-checking. Normally this is not compiled-into your executable, but when it is, it can be disabled for a session.</p>
<dt><code>-force_empty_hrefless_a</code></p>
<dd> force href-less &#8220;A&#8221; elements to be empty (close them as soon as they are seen).</p>
<dt><code>-force_html</code></p>
<dd> forces the first document to be interpreted as HTML.</p>
<dt>
<dd> This is most useful when processing files specified on the command line which have an unrecognized suffix (or the suffix is associated with a non-HTML type, such as &#8220;.txt&#8221; for plain text files).</p>
<dt>
<dd> <i>Lynx</i> recognizes these file suffixes as HTML:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
``.ht3'',
``.htm'',
``.html3'',
``.html'',
``.htmlx'',
``.php3'',
``.php'',
``.phtml'',
``.sht'', and
``.shtml''.
</pre>
<p>&nbsp;.in -4</p>
<dt><code>-force_secure</code></p>
<dd> toggles forcing of the secure flag for SSL cookies.</p>
<dt><code>-forms_options</code></p>
<dd> toggles whether the Options Menu is key-based or form-based.</p>
<dt><code>-from</code></p>
<dd> toggles transmissions of From headers.</p>
<dt><code>-ftp</code></p>
<dd> disable ftp access.</p>
<dt><code>-get_data</code></p>
<dd> properly formatted data for a <i>get</i> form are read in from the standard input and passed to the form. Input is terminated by a line that starts with &#8220;&#8212;&#8221;.</p>
<dt>
<dd> <i>Lynx</i> issues an HTTP <code>GET</code>, sending the form to the path or URL given on the command-line and prints the response of the server. If no path or URL is given, <i>Lynx</i> sends the form to the start-page.</p>
<dt><code>-head</code></p>
<dd> send a HEAD request for the mime headers.</p>
<dt><code>-help</code></p>
<dd> print the <i>Lynx</i> command syntax usage message, and exit.</p>
<dt><code>-hiddenlinks=[option]</code></p>
<dd> control the display of hidden links.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>merge</code></p>
<dd> hidden links show up as bracketed numbers and are numbered together with other links in the sequence of their occurrence in the document.</p>
<dt><code>listonly</code></p>
<dd> hidden links are shown only on <code>L)ist</code> screens and listings generated by <code>-dump</code> or from the <code>P)rint</code> menu, but appear separately at the end of those lists. This is the default behavior.</p>
<dt><code>ignore</code></p>
<dd> hidden links do not appear even in listings.</dl>
</dl>
<dt><code>-historical</code></p>
<dd> toggles use of &#8220;&gt;&#8221; or &#8220;&#8211;&gt;&#8221; as a terminator for comments.</p>
<dt><code>-homepage</code>=<i>URL</i></p>
<dd> set homepage separate from start page.</p>
<dt><code>-image_links</code></p>
<dd> toggles inclusion of links for all images.</p>
<dt><code>-index</code>=<i>URL</i></p>
<dd> set the default index file to the specified URL.</p>
<dt><code>-ismap</code></p>
<dd> toggles inclusion of ISMAP links when client-side MAPs are present.</p>
<dt><code>-justify</code></p>
<dd> do justification of text.</p>
<dt><code>-link</code>=<i>NUMBER</i></p>
<dd> starting count for lnk#.dat files produced by <code>-crawl</code>.</p>
<dt><code>-list_decoded</code></p>
<dd> for <code>-dump</code>, show URL-encoded links decoded.</p>
<dt><code>-list_inline</code></p>
<dd> for <code>-dump</code>, show the links inline with the text.</p>
<dt><code>-listonly</code></p>
<dd> for <code>-dump</code>, show only the list of links.</p>
<dt><code>-localhost</code></p>
<dd> disable URLs that point to remote hosts.</p>
<dt><code>-locexec</code></p>
<dd> enable local program execution from local files only (if <i>Lynx</i> was compiled with local execution enabled).</p>
<dt><code>-lss</code>=<i>FILENAME</i></p>
<dd> specify filename containing color-style information. The default is lynx.lss. If you give an empty filename, <i>Lynx</i> uses a built-in monochrome scheme which imitates the non-color-style configuration.</p>
<dt><code>-mime_header</code></p>
<dd> prints the MIME header of a fetched document along with its source.</p>
<dt><code>-minimal</code></p>
<dd> toggles minimal versus valid comment parsing.</p>
<dt><code>-nested_tables</code></p>
<dd> toggles nested-tables logic (for debugging).</p>
<dt><code>-newschunksize</code>=<i>NUMBER</i></p>
<dd> number of articles in chunked news listings.</p>
<dt><code>-newsmaxchunk</code>=<i>NUMBER</i></p>
<dd> maximum news articles in listings before chunking.</p>
<dt><code>-nobold</code></p>
<dd> disable bold video-attribute.</p>
<dt><code>-nobrowse</code></p>
<dd> disable directory browsing.</p>
<dt><code>-nocc</code></p>
<dd> disable Cc: prompts for self copies of mailings. Note that this does not disable any CCs which are incorporated within a mailto URL or form ACTION.</p>
<dt><code>-nocolor</code></p>
<dd> force color mode off, overriding terminal capabilities and any -color flags, COLORTERM variable, and saved .lynxrc settings.</p>
<dt><code>-noexec</code></p>
<dd> disable local program execution. (DEFAULT)</p>
<dt><code>-nofilereferer</code></p>
<dd> disable transmissions of Referer headers for file URLs.</p>
<dt><code>-nolist</code></p>
<dd> disable the link list feature in dumps.</p>
<dt><code>-nolog</code></p>
<dd> disable mailing of error messages to document owners.</p>
<dt><code>-nomargins</code></p>
<dd> disable left/right margins in the default style sheet.</p>
<dt><code>-nomore</code></p>
<dd> disable -more- string in statusline messages.</p>
<dt><code>-nonrestarting_sigwinch</code></p>
<dd> This flag is not available on all systems, <i>Lynx</i> needs to be compiled with HAVE_SIGACTION defined. If available, this flag <i>may</i> cause <i>Lynx</i> to react more immediately to window changes when run within an <code>xterm</code>.</p>
<dt><code>-nonumbers</code></p>
<dd> disable link- and field-numbering. This overrides <code>-number_fields</code> and <code>-number_links</code>.</p>
<dt><code>-nopause</code></p>
<dd> disable forced pauses for statusline messages.</p>
<dt><code>-noprint</code></p>
<dd> disable most print functions.</p>
<dt><code>-noredir</code></p>
<dd> prevents automatic redirection and prints a message with a link to the new URL.</p>
<dt><code>-noreferer</code></p>
<dd> disable transmissions of Referer headers.</p>
<dt><code>-noreverse</code></p>
<dd> disable reverse video-attribute.</p>
<dt><code>-nosocks</code></p>
<dd> disable SOCKS proxy usage by a SOCKSified <i>Lynx</i>.</p>
<dt><code>-nostatus</code></p>
<dd> disable the retrieval status messages.</p>
<dt><code>-notitle</code></p>
<dd> disable title and blank line from top of page.</p>
<dt><code>-nounderline</code></p>
<dd> disable underline video-attribute.</p>
<dt><code>-number_fields</code></p>
<dd> force numbering of links as well as form input fields</p>
<dt><code>-number_links</code></p>
<dd> force numbering of links.</p>
<dt><code>-partial</code></p>
<dd> toggles display partial pages while loading.</p>
<dt><code>-partial_thres</code>=<i>NUMBER</i></p>
<dd> number of lines to render before repainting display with partial-display logic</p>
<dt><code>-passive_ftp</code></p>
<dd> toggles passive ftp connections.</p>
<dt><code>-pauth</code>=<i>ID</i>:<i>PASSWD</i></p>
<dd> set authorization ID and password for a protected proxy server at startup. Be sure to protect any script files which use this switch.</p>
<dt><code>-popup</code></p>
<dd> toggles handling of single-choice SELECT options via popup windows or as lists of radio buttons.</p>
<dt><code>-post_data</code></p>
<dd> properly formatted data for a <i>post</i> form are read in from the standard input and passed to the form. Input is terminated by a line that starts with &#8220;&#8212;&#8221;.</p>
<dt>
<dd> <i>Lynx</i> issues an HTTP <code>POST</code>, sending the form to the path or URL given on the command-line and prints the response of the server. If no path or URL is given, <i>Lynx</i> sends the form to the start-page.</p>
<dt><code>-preparsed</code></p>
<dd> show HTML source preparsed and reformatted when used with <code>-source</code> or in source view.</p>
<dt><code>-prettysrc</code></p>
<dd> show HTML source view with lexical elements and tags in color.</p>
<dt><code>-print</code></p>
<dd> enable print functions. (default)</p>
<dt><code>-pseudo_inlines</code></p>
<dd> toggles pseudo-ALTs for inline images with no ALT string.</p>
<dt><code>-raw</code></p>
<dd> toggles default setting of 8-bit character translations or CJK mode for the startup character set.</p>
<dt><code>-realm</code></p>
<dd> restricts access to URLs in the starting realm.</p>
<dt><code>-read_timeout</code>=<i>N</i></p>
<dd> Sets the read-timeout, where N is given in seconds.</p>
<dt><code>-reload</code></p>
<dd> flushes the cache on a proxy server (only the first document given on the command-line is affected).</p>
<dt><code>-restrictions</code>=<i>[option][,option][,option]&#8230;</i></p>
<dd> allows a list of services to be disabled selectively. Dashes and underscores in option names can be intermixed. The following list is printed if no options are specified.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>all</code></p>
<dd> restricts all options listed below.</p>
<dt><code>bookmark</code></p>
<dd> disallow changing the location of the bookmark file.</p>
<dt><code>bookmark_exec</code></p>
<dd> disallow execution links via the bookmark file.</p>
<dt><code>change_exec_perms</code></p>
<dd> disallow changing the eXecute permission on files (but still allow it for directories) when local file management is enabled.</p>
<dt><code>default</code></p>
<dd> same as command line option <code>-anonymous</code>. Disables default services for anonymous users. Set to all restricted, except for: inside_telnet, outside_telnet, inside_ftp, outside_ftp, inside_rlogin, outside_rlogin, inside_news, outside_news, telnet_port, jump, mail, print, exec, and goto. The settings for these, as well as additional goto restrictions for specific URL schemes that are also applied, are derived from definitions within userdefs.h.</p>
<dt><code>dired_support</code></p>
<dd> disallow local file management.</p>
<dt><code>disk_save</code></p>
<dd> disallow saving to disk in the download and print menus.</p>
<dt><code>dotfiles</code></p>
<dd> disallow access to, or creation of, hidden (dot) files.</p>
<dt><code>download</code></p>
<dd> disallow some downloaders in the download menu (does not imply disk_save restriction).</p>
<dt><code>editor</code></p>
<dd> disallow external editing.</p>
<dt><code>exec</code></p>
<dd> disable execution scripts.</p>
<dt><code>exec_frozen</code></p>
<dd> disallow the user from changing the local execution option.</p>
<dt><code>externals</code></p>
<dd> disallow some &#8220;EXTERNAL&#8221; configuration lines if support for passing URLs to external applications (with the EXTERN command) is compiled in.</p>
<dt><code>file_url</code></p>
<dd> disallow using <code>G)oto</code>, served links or bookmarks for file: URLs.</p>
<dt><code>goto</code></p>
<dd> disable the &#8220;g&#8221; (goto) command.</p>
<dt><code>inside_ftp</code></p>
<dd> disallow ftps for people coming from inside your domain (utmp required for selectivity).</p>
<dt><code>inside_news</code></p>
<dd> disallow USENET news posting for people coming from inside your domain (utmp required for selectivity).</p>
<dt><code>inside_rlogin</code></p>
<dd> disallow rlogins for people coming from inside your domain (utmp required for selectivity).</p>
<dt><code>inside_telnet</code></p>
<dd> disallow telnets for people coming from inside your domain (utmp required for selectivity).</p>
<dt><code>jump</code></p>
<dd> disable the &#8220;j&#8221; (jump) command.</p>
<dt><code>multibook</code></p>
<dd> disallow multiple bookmarks.</p>
<dt><code>mail</code></p>
<dd> disallow mail.</p>
<dt><code>news_post</code></p>
<dd> disallow USENET News posting.</p>
<dt><code>options_save</code></p>
<dd> disallow saving options in .lynxrc.</p>
<dt><code>outside_ftp</code></p>
<dd> disallow ftps for people coming from outside your domain (utmp required for selectivity).</p>
<dt><code>outside_news</code></p>
<dd> disallow USENET news reading and posting for people coming from outside your domain (utmp required for selectivity). This restriction applies to &#8220;news&#8221;, &#8220;nntp&#8221;, &#8220;newspost&#8221;, and &#8220;newsreply&#8221; URLs, but not to &#8220;snews&#8221;, &#8220;snewspost&#8221;, or &#8220;snewsreply&#8221; in case they are supported.</p>
<dt><code>outside_rlogin</code></p>
<dd> disallow rlogins for people coming from outside your domain (utmp required for selectivity).</p>
<dt><code>outside_telnet</code></p>
<dd> disallow telnets for people coming from outside your domain (utmp required for selectivity).</p>
<dt><code>print</code></p>
<dd> disallow most print options.</p>
<dt><code>shell</code></p>
<dd> disallow shell escapes and lynxexec or lynxprog <code>G)oto</code>&#8216;s.</p>
<dt><code>suspend</code></p>
<dd> disallow Unix Control-Z suspends with escape to shell.</p>
<dt><code>telnet_port</code></p>
<dd> disallow specifying a port in telnet <code>G)oto</code>&#8216;s.</p>
<dt><code>useragent</code></p>
<dd> disallow modifications of the User-Agent header.</dl>
</dl>
<dt><code>-resubmit_posts</code></p>
<dd> toggles forced resubmissions (no-cache) of forms with method POST when the documents they returned are sought with the PREV_DOC command or from the History List.</p>
<dt><code>-rlogin</code></p>
<dd> disable recognition of rlogin commands.</p>
<dt><code>-scrollbar</code></p>
<dd> toggles showing scrollbar.</p>
<dt><code>-scrollbar_arrow</code></p>
<dd> toggles showing arrows at ends of the scrollbar.</p>
<dt><code>-selective</code></p>
<dd> require .www_browsable files to browse directories.</p>
<dt><code>-session</code>=<i>FILENAME</i></p>
<dd> resumes from specified file on startup and saves session to that file on exit.</p>
<dt><code>-sessionin</code>=<i>FILENAME</i></p>
<dd> resumes session from specified file.</p>
<dt><code>-sessionout</code>=<i>FILENAME</i></p>
<dd> saves session to specified file.</p>
<dt><code>-short_url</code></p>
<dd> show very long URLs in the status line with &#8220;&#8230;&#8221; to represent the portion which cannot be displayed. The beginning and end of the URL are displayed, rather than suppressing the end.</p>
<dt><code>-show_cfg</code></p>
<dd> Print the configuration settings, e.g., as read from &#8220;lynx.cfg&#8221;, and exit.</p>
<dt><code>-show_cursor</code></p>
<dd> If enabled the cursor will not be hidden in the right hand corner but will instead be positioned at the start of the currently selected link. Show cursor is the default for systems without FANCY_CURSES capabilities. The default configuration can be changed in userdefs.h or lynx.cfg. The command line switch toggles the default.</p>
<dt><code>-show_rate</code></p>
<dd> If enabled the transfer rate is shown in bytes/second. If disabled, no transfer rate is shown. Use lynx.cfg or the options menu to select KB/second and/or ETA.</p>
<dt><code>-socks5-proxy=URL</code></p>
<dd> (Via which) SOCKS5 proxy to connect. This controls the builtin SOCKS5 support, and is therefore unrelated to the option <code>-nosocks</code>.</p>
<dt><code>-soft_dquotes</code></p>
<dd> toggles emulation of the old Netscape and Mosaic bug which treated &#8220;&gt;&#8221; as a co-terminator for double-quotes and tags.</p>
<dt><code>-source</code></p>
<dd> works the same as dump but outputs HTML source instead of formatted text. For example<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
lynx -source .&nbsp;&gt;foo.html
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> generates HTML source listing the files in the current directory. Each file is marked by an href relative to the parent directory. Add a trailing slash to make the href&#8217;s relative to the current directory:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
lynx -source ./ &gt;foo.html
</pre>
<p>&nbsp;.in -4</p>
<dt><code>-stack_dump</code></p>
<dd> disable SIGINT cleanup handler</p>
<dt><code>-startfile_ok</code></p>
<dd> allow non-http startfile and homepage with <code>-validate</code>.</p>
<dt><code>-stderr</code></p>
<dd> When dumping a document using <code>-dump</code> or <code>-source</code>, <i>Lynx</i> normally does not display alert (error) messages that you see on the screen in the status line. Use the <code>-stderr</code> option to tell <i>Lynx</i> to write these messages to the standard error.</p>
<dt><code>-stdin</code></p>
<dd> read the startfile from standard input (UNIX only).</p>
<dt><code>-syslog</code>=<i>text</i></p>
<dd> information for syslog call.</p>
<dt><code>-syslog_urls</code></p>
<dd> log requested URLs with syslog.</p>
<dt><code>-tagsoup</code></p>
<dd> initialize parser, using Tag Soup DTD rather than SortaSGML.</p>
<dt><code>-telnet</code></p>
<dd> disable recognition of telnet commands.</p>
<dt><code>-term</code>=<i>TERM</i></p>
<dd> tell <i>Lynx</i> what terminal type to assume it is talking to. (This may be useful for remote execution, when, for example, <i>Lynx</i> connects to a remote TCP/IP port that starts a script that, in turn, starts another <i>Lynx</i> process.)</p>
<dt><code>-timeout</code>=<i>N</i></p>
<dd> For win32, sets the network read-timeout, where N is given in seconds.</p>
<dt><code>-tlog</code></p>
<dd> toggles between using a <i>Lynx</i> Trace Log and stderr for trace output from the session.</p>
<dt><code>-tna</code></p>
<dd> turns on &#8220;Textfields Need Activation&#8221; mode.</p>
<dt><code>-trace</code></p>
<dd> turns on <i>Lynx</i> trace mode. Destination of trace output depends on -tlog.</p>
<dt><code>-trace_mask</code>=<i>value</i></p>
<dd> turn on optional traces, which may result in very large trace files. Logically OR the values to combine options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1</code></p>
<dd> SGML character parsing states</p>
<dt><code>2</code></p>
<dd> color-style</p>
<dt><code>4</code></p>
<dd> TRST (table layout)</p>
<dt><code>8</code></p>
<dd> configuration (lynx.cfg, .lynxrc, .lynx-keymaps, mime.types and mailcap contents)</p>
<dt><code>16</code></p>
<dd> binary string copy/append, used in form data construction.</p>
<dt><code>32</code></p>
<dd> cookies</p>
<dt><code>64</code></p>
<dd> character sets</p>
<dt><code>128</code></p>
<dd> GridText parsing</p>
<dt><code>256</code></p>
<dd> timing</p>
<dt><code>512</code></p>
<dd> detailed URL parsing</dl>
</dl>
<dt><code>-traversal</code></p>
<dd> traverse all http links derived from startfile. When used with <code>-crawl</code>, each link that begins with the same string as startfile is output to a file, intended for indexing.</p>
<dt>
<dd> See CRAWL.announce for more information.</p>
<dt><code>-trim_blank_lines</code></p>
<dd> toggles trimming of trailing blank lines as well as the related trimming of blank lines while collapsing BR tags.</p>
<dt><code>-trim_input_fields</code></p>
<dd> trim input text/textarea fields in forms.</p>
<dt><code>-underline_links</code></p>
<dd> toggles use of underline/bold attribute for links.</p>
<dt><code>-underscore</code></p>
<dd> toggles use of _underline_ format in dumps.</p>
<dt><code>-unique_urls</code></p>
<dd> check for duplicate link numbers in each page and corresponding lists, and reuse the original link number.</p>
<dt><code>-update_term_title</code></p>
<dd> enables updating the title in terminal emulators. Use only if your terminal emulator supports that escape code. Has no effect when used with <code>-notitle</code>.</p>
<dt><code>-use_mouse</code></p>
<dd> turn on mouse support, if available. Clicking the left mouse button on a link traverses it. Clicking the right mouse button pops back. Click on the top line to scroll up. Click on the bottom line to scroll down. The first few positions in the top and bottom line may invoke additional functions. <i>Lynx</i> must be compiled with <code>ncurses</code> or <code>slang</code> to support this feature. If <code>ncurses</code> is used, clicking the middle mouse button pops up a simple menu. Mouse clicks may only work reliably while <i>Lynx</i> is idle waiting for input.</p>
<dt><code>-useragent=Name</code></p>
<dd> set alternate <i>Lynx</i> User-Agent header.</p>
<dt><code>-validate</code></p>
<dd> accept only http URLs (for validation). Complete security restrictions also are implemented.</p>
<dt><code>-verbose</code></p>
<dd> toggle [LINK], [IMAGE] and [INLINE] comments with filenames of these images.</p>
<dt><code>-version</code></p>
<dd> print version information, and exit.</p>
<dt><code>-vikeys</code></p>
<dd> enable vi-like key movement.</p>
<dt><code>-wdebug</code></p>
<dd> enable Waterloo tcp/ip packet debug (print to watt debugfile). This applies only to DOS versions compiled with WATTCP or WATT-32.</p>
<dt><code>-width</code>=<i>NUMBER</i></p>
<dd> number of columns for formatting of dumps, default is 80. This is limited by the number of columns that <i>Lynx</i> could display, typically 1024 (the <i>MAX_LINE</i> symbol).</p>
<dt><code>-with_backspaces</code></p>
<dd> emit backspaces in output if <code>-dump</code>&#8216;ing or <code>-crawl</code>&#8216;ing (like <code>man</code> does)</p>
<dt><code>-xhtml_parsing</code></p>
<dd> tells <i>Lynx</i> that it can ignore certain tags which have no content in an XHTML 1.0 document. For example &#8220;&lt;p/&gt;&#8221; will be discarded.</dl>
<h2>COMMANDS</h2>
<p> More than one key can be mapped to a given command. Here are some of the most useful:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Use <code>Up arrow</code> and <code>Down arrow</code> to scroll through hypertext links.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>Right arrow</code> or <code>Return</code> will follow a highlighted hypertext link.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>Left Arrow</code> or &#8220;<code>u</code>&#8221; will retreat from a link.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Type &#8220;<code>H</code>&#8221;, &#8220;<code>?</code>&#8221;, or <code>F1</code> for online help and descriptions of key-stroke commands.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Type &#8220;<code>k</code>&#8221; or &#8220;<code>K</code>&#8221; for a list of the current key-stroke command mappings.</p>
<dl>
<dt>
<dd> If the same command is mapped to the same letter differing only by upper/lowercase only the lowercase mapping is shown.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Type <code>Delete</code> to view history list.</dl>
<h2>ENVIRONMENT</h2>
<p> In addition to various &#8220;standard&#8221; environment variables such as <code>HOME</code>, <code>PATH</code>, <code>USER</code>, <code>DISPLAY</code>, <code>TMPDIR</code>, <code>etc</code>, <i>Lynx</i> utilizes several <i>Lynx</i>-specific environment variables, if they exist. </p>
<p> Others may be created or modified by <i>Lynx</i> to pass data to an external program, or for other reasons. These are listed separately below. </p>
<p> See also the sections on <code>SIMULATED CGI SUPPORT</code> and <code>NATIVE LANGUAGE SUPPORT</code>, below. </p>
<p> Note: Not all environment variables apply to all types of platforms supported by <i>Lynx</i>, though most do. Feedback on platform dependencies is solicited. </p>
<p> Environment Variables Used By <i>Lynx</i>:</p>
<dl>
<dt><code>COLORTERM</code></p>
<dd> If set, color capability for the terminal is forced on at startup time. The actual value assigned to the variable is ignored. This variable is only meaningful if <i>Lynx</i> was built using the <code>slang</code> screen-handling library.</p>
<dt><code>LYNX_CFG</code></p>
<dd> This variable, if set, will override the default location and name of the global configuration file (normally, <code>lynx.cfg</code>) that was defined by the LYNX_CFG_FILE constant in the userdefs.h file, during installation.</p>
<dt>
<dd> See the userdefs.h file for more information.</p>
<dt><code>LYNX_CFG_PATH</code></p>
<dd> If set, this variable overrides the compiled-in search-list of directories used to find the configuration files, e.g., <code>lynx.cfg</code> and <code>lynx.lss</code>. The list is delimited with &quot;:&quot; (or &quot;;&quot; for Windows) like the <code>PATH</code> environment variable.</p>
<dt><code>LYNX_HELPFILE</code></p>
<dd> If set, this variable overrides the compiled-in URL and configuration file URL for the <i>Lynx</i> help file.</p>
<dt><code>LYNX_LOCALEDIR</code></p>
<dd> If set, this variable overrides the compiled-in location of the locale directory which contains native language (NLS) message text.</p>
<dt><code>LYNX_LSS</code></p>
<dd> This variable, if set, specifies the location of the default <i>Lynx</i> character style sheet file. [Currently only meaningful if <i>Lynx</i> was built using curses color style support.]</p>
<dt><code>LYNX_SAVE_SPACE</code></p>
<dd> This variable, if set, will override the default path prefix for files saved to disk that is defined in the <code>lynx.cfg SAVE_SPACE:</code> statement.</p>
<dt>
<dd> See the <code>lynx.cfg</code> file for more information.</p>
<dt><code>LYNX_TEMP_SPACE</code></p>
<dd> This variable, if set, will override the default path prefix for temporary files that was defined during installation, as well as any value that may be assigned to the <code>TMPDIR</code> variable.</p>
<dt><code>MAIL</code></p>
<dd> This variable specifies the default inbox <i>Lynx</i> will check for new mail, if such checking is enabled in the <code>lynx.cfg</code> file.</p>
<dt><code>NEWS_ORGANIZATION</code></p>
<dd> This variable, if set, provides the string used in the <code>Organization:</code> header of <code>USENET</code> news postings. It will override the setting of the ORGANIZATION environment variable, if it is also set (and, on <code>UNIX</code>, the contents of an /etc/organization file, if present).</p>
<dt><code>NNTPSERVER</code></p>
<dd> If set, this variable specifies the default NNTP server that will be used for <code>USENET</code> news reading and posting with <i>Lynx</i>, via news: URL&#8217;s.</p>
<dt><code>ORGANIZATION</code></p>
<dd> This variable, if set, provides the string used in the <code>Organization:</code> header of <code>USENET</code> news postings. On <code>UNIX</code>, it will override the contents of an /etc/organization file, if present.</p>
<dt><i>PROTOCOL</i><code>_proxy</code></p>
<dd> <i>Lynx</i> supports the use of proxy servers that can act as firewall gateways and caching servers. They are preferable to the older gateway servers (see WWW_access_GATEWAY, below).</p>
<dt>
<dd> Each protocol used by <i>Lynx</i>, (http, ftp, gopher, etc), can be mapped separately by setting environment variables of the form <i>PROTOCOL</i>_proxy. Protocols are indicated in a URI by the name before &#8220;:&#8221;, e.g., &#8220;http&#8221; in &#8220;<a rel="nofollow" href="http://some.server.dom:port/''">http://some.server.dom:port/&#8221;</a> for HTML.</p>
<dt>
<dd> Depending on your system configuration and supported protocols, the environment variables recognized by <i>lynx</i> may include<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
cso_proxy
finger_proxy
ftp_proxy
gopher_proxy
https_proxy
http_proxy
newspost_proxy
newsreply_proxy
news_proxy
nntp_proxy
no_proxy
snewspost_proxy
snewsreply_proxy
snews_proxy
wais_proxy
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> See <code>Lynx Users Guide</code> for additional details and examples.</p>
<dt><code>SSL_CERT_DIR</code></p>
<dd> Set to the directory containing trusted certificates.</p>
<dt><code>SSL_CERT_FILE</code></p>
<dd> Set to the full path and filename for your file of trusted certificates.</p>
<dt><code>WWW_</code><i>access</i><code>_GATEWAY</code></p>
<dd> <i>Lynx</i> still supports use of gateway servers, with the servers specified via &#8220;WWW_<i>access</i>_GATEWAY&#8221; variables (where &#8220;<i>access</i>&#8221; is lower case and can be &#8220;http&#8221;, &#8220;ftp&#8221;, &#8220;gopher&#8221; or &#8220;wais&#8221;). However most gateway servers have been discontinued. Note that you do not include a terminal &#8220;/&#8221; for gateways, but do for proxies specified by <i>PROTOCOL</i>_proxy environment variables.</p>
<dt>
<dd> See <code>Lynx Users Guide</code> for details.</p>
<dt><code>WWW_HOME</code></p>
<dd> This variable, if set, will override the default startup URL specified in any of the <i>Lynx</i> configuration files.</dl>
<p> Environment Variables <code>Set</code> or <code>Modified</code> By <i>Lynx</i>:</p>
<dl>
<dt><code>LYNX_PRINT_DATE</code></p>
<dd> This variable is set by the <i>Lynx</i> p(rint) function, to the <code>Date:</code> string seen in the document&#8217;s &#8220;<code>Information about</code>&#8221; page (= cmd), if any. It is created for use by an external program, as defined in a <code>lynx.cfg PRINTER:</code> definition statement. If the field does not exist for the document, the variable is set to a null string under <code>UNIX</code>, or &#8220;No Date&#8221; under <code>VMS</code>.</p>
<dt><code>LYNX_PRINT_LASTMOD</code></p>
<dd> This variable is set by the <i>Lynx</i> p(rint) function, to the <code>Last Mod:</code> string seen in the document&#8217;s &#8220;<code>Information about</code>&#8221; page (= cmd), if any. It is created for use by an external program, as defined in a <code>lynx.cfg PRINTER:</code> definition statement. If the field does not exist for the document, the variable is set to a null string under <code>UNIX</code>, or &#8220;No LastMod&#8221; under <code>VMS</code>.</p>
<dt><code>LYNX_PRINT_TITLE</code></p>
<dd> This variable is set by the <i>Lynx</i> p(rint) function, to the <code>Linkname:</code> string seen in the document&#8217;s &#8220;<code>Information about</code>&#8221; page (= cmd), if any. It is created for use by an external program, as defined in a <code>lynx.cfg PRINTER:</code> definition statement. If the field does not exist for the document, the variable is set to a null string under <code>UNIX</code>, or &#8220;No Title&#8221; under <code>VMS</code>.</p>
<dt><code>LYNX_PRINT_URL</code></p>
<dd> This variable is set by the <i>Lynx</i> p(rint) function, to the <code>URL:</code> string seen in the document&#8217;s &#8220;<code>Information about</code>&#8221; page (= cmd), if any. It is created for use by an external program, as defined in a <code>lynx.cfg PRINTER:</code> definition statement. If the field does not exist for the document, the variable is set to a null string under <code>UNIX</code>, or &#8220;No URL&#8221; under <code>VMS</code>.</p>
<dt><code>LYNX_TRACE</code></p>
<dd> If set, causes <i>Lynx</i> to write a trace file as if the <code>-trace</code> option were supplied.</p>
<dt><code>LYNX_TRACE_FILE</code></p>
<dd> If set, overrides the compiled-in name of the trace file, which is either <code>Lynx.trace</code> or <code>LY-TRACE.LOG</code> (the latter on the DOS/Windows platforms). The trace file is in either case relative to the home directory.</p>
<dt><code>LYNX_VERSION</code></p>
<dd> This variable is always set by <i>Lynx</i>, and may be used by an external program to determine if it was invoked by <i>Lynx</i>.</p>
<dt>
<dd> See also the comments in the distribution&#8217;s sample <code>mailcap</code> file, for notes on usage in such a file.</p>
<dt><code>TERM</code></p>
<dd> Normally, this variable is used by <i>Lynx</i> to determine the terminal type being used to invoke <i>Lynx</i>. If, however, it is unset at startup time (or has the value &#8220;unknown&#8221;), or if the <code>-term</code> command-line option is used (see <code>OPTIONS</code> section above), <i>Lynx</i> will set or modify its value to the user specified terminal type (for the <i>Lynx</i> execution environment). Note: If set/modified by <i>Lynx</i>, the values of the <code>LINES</code> and/or <code>COLUMNS</code> environment variables may also be changed.</dl>
<h2>SIMULATED CGI SUPPORT</h2>
<p> If built with the <code>cgi-links</code> option enabled, <i>Lynx</i> allows access to a cgi script directly without the need for an http daemon. </p>
<p> When executing such &#8220;lynxcgi scripts&#8221; (if enabled), the following variables may be set for simulating a CGI environment: </p>
<p> <code>CONTENT_LENGTH</code> </p>
<p> <code>CONTENT_TYPE</code> </p>
<p> <code>DOCUMENT_ROOT</code> </p>
<p> <code>HTTP_ACCEPT_CHARSET</code> </p>
<p> <code>HTTP_ACCEPT_LANGUAGE</code> </p>
<p> <code>HTTP_USER_AGENT</code> </p>
<p> <code>PATH_INFO</code> </p>
<p> <code>PATH_TRANSLATED</code> </p>
<p> <code>QUERY_STRING</code> </p>
<p> <code>REMOTE_ADDR</code> </p>
<p> <code>REMOTE_HOST</code> </p>
<p> <code>REQUEST_METHOD</code> </p>
<p> <code>SERVER_SOFTWARE</code> </p>
<p> Other environment variables are not inherited by the script, unless they are provided via a LYNXCGI_ENVIRONMENT statement in the configuration file. See the <code>lynx.cfg</code> file, and the (draft) CGI 1.1 Specification &lt;<a rel="nofollow" href="http://Web.Golux.Com/coar/cgi/draft-coar-cgi-v11-00.txt">http://Web.Golux.Com/coar/cgi/draft-coar-cgi-v11-00.txt</a>&gt; for the definition and usage of these variables. </p>
<p> The CGI Specification, and other associated documentation, should be consulted for general information on CGI script programming.</p>
<h2>NATIVE LANGUAGE SUPPORT</h2>
<p> If configured and installed with <code>Native Language Support</code>, <i>Lynx</i> will display status and other messages in your local language. See the file <code>ABOUT_NLS</code> in the source distribution, or at your local <code>GNU</code> site, for more information about internationalization. </p>
<p> The following environment variables may be used to alter default settings:</p>
<dl>
<dt><code>LANG</code></p>
<dd> This variable, if set, will override the default message language. It is an <code>ISO 639</code> two-letter code identifying the language. Language codes are <code>NOT</code> the same as the country codes given in <code>ISO 3166</code>.</p>
<dt><code>LANGUAGE</code></p>
<dd> This variable, if set, will override the default message language. This is a <code>GNU</code> extension that has higher priority for setting the message catalog than <code>LANG</code> or <code>LC_ALL</code>.</p>
<dt><code>LC_ALL</code></p>
<dd> and</p>
<dt><code>LC_MESSAGES</code></p>
<dd> These variables, if set, specify the notion of native language formatting style. They are <code>POSIXly</code> correct.</p>
<dt><code>LINGUAS</code></p>
<dd> This variable, if set prior to configuration, limits the installed languages to specific values. It is a space-separated list of two-letter codes. Currently, it is hard-coded to a wish list.</p>
<dt><code>NLSPATH</code></p>
<dd> This variable, if set, is used as the path prefix for message catalogs.</dl>
<h2>NOTES</h2>
<p> This is the manual for <i>Lynx</i> v2.9.0dev.5; development is in progress for 2.9.0. </p>
<p> If you wish to contribute to the further development of <i>Lynx</i>, subscribe to our mailing list. Send email to &lt;lynx-dev-request [at] nongnu.org&gt; with &#8220;subscribe lynx-dev&#8221; as the only line in the body of your message. </p>
<p> Send bug reports, comments, suggestions to &lt;lynx-dev [at] nongnu.org&gt; after subscribing. </p>
<p> Unsubscribe by sending email to &lt;lynx-dev-request [at] nongnu.org&gt; with &#8220;unsubscribe lynx-dev&#8221; as the only line in the body of your message. Do not send the unsubscribe message to the lynx-dev list, itself.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-catgets/">catgets</a></code>(3), <code><a href="/docs/linux/man/3-curses/">curses</a></code>(3), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1), <code>gettext</code>(GNU), <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), <code><a href="/docs/linux/man/3-ncurses/">ncurses</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code>slang</code>(?), <code><a href="/docs/linux/man/5-termcap/">termcap</a></code>(5), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5), <code>wget</code>(GNU) </p>
<p> Note that man page availability and section numbering is somewhat platform dependent, and may vary from the above references. </p>
<p> A section shown as (GNU), is intended to denote that the topic may be available via an info page, instead of a man page (i.e., try &#8220;info subject&#8221;, rather than &#8220;man subject&#8221;). </p>
<p> A section shown as <code>(?)</code> denotes that documentation on the topic exists, but is not part of an established documentation retrieval system (see the distribution files associated with the topic, or contact your System Administrator for further information).</p>
<h2>ACKNOWLEDGMENTS</h2>
<p> <i>Lynx</i> has incorporated code from a variety of sources along the way. The earliest versions of <i>Lynx</i> included code from Earl Fogel of Computing Services at the University of Saskatchewan, who implemented HYPERREZ in the Unix environment. HYPERREZ was developed by Niel Larson of Think.com and served as the model for the early versions of <i>Lynx</i>. Those versions also incorporated libraries from the Unix Gopher clients developed at the University of Minnesota, and the later versions of <i>Lynx</i> rely on the WWW client library code developed by Tim Berners-Lee and the WWW community. Also a special thanks to Foteos Macrides who ported much of <i>Lynx</i> to VMS and did or organized most of its development since the departures of Lou Montulli and Garrett Blythe from the University of Kansas in the summer of 1994 through the release of v2.7.2, and to everyone on the net who has contributed to <i>Lynx</i>&#8216;s development either directly (through patches, comments or bug reports) or indirectly (through inspiration and development of other systems).</p>
<h2>AUTHORS</h2>
<p> Lou Montulli, Garrett Blythe, Craig Lavender, Michael Grobe, Charles Rezac<br />
 Academic Computing Services<br />
 University of Kansas<br />
 Lawrence, Kansas 66047 </p>
<p> Foteos Macrides<br />
 Worcester Foundation for Biomedical Research<br />
 Shrewsbury, Massachusetts 01545 </p>
<p> Thomas E. Dickey<br />
 &lt;dickey [at] invisible-island.net&gt; </p>
<h2>Index</h2>
