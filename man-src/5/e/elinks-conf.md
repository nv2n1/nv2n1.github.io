---
title: "elinks-conf(5)"
name: "elinks-conf"
section: "5"
letter: "e"
url: "/docs/linux/man/5-elinks-conf/"
description: "elinks.conf – ELinks configuration file"
---

<p>elinks.conf &#8211; ELinks configuration file</p>
<h2>Synopsis</h2>
<pre><code>set        &lt;option&gt; = &lt;value&gt;
set_domain &lt;domain&gt; &lt;option&gt; = &lt;value&gt;
unset      &lt;option&gt;
bind       &quot;&lt;keymap&gt;&quot; &quot;&lt;key&gt;&quot; = &quot;&lt;action&gt;&quot;
include    &quot;&lt;file&gt;&quot;</code></pre>
<h2>Description</h2>
<p>The elinks.conf file contains configuration information for ELinks. It can be used to configure the behaviour of ELinks in a wide variety of ways: protocol behaviour, keybindings, colors used for rendering and for the user interface. It is read at startup and saved only when requested. All options described in this document can be fully configured from within ELinks so no editing of elinks.conf is needed. Note that MIME-related options used for specifying handlers of various MIME types are NOT described in this document. Documentation for these options can be found at the ELinks homepage. Keybindings can also be specified in elinks.conf. This is described in <code><a href="/docs/linux/man/5-elinkskeys/">elinkskeys</a></code>(5). </p>
<h2>Syntax</h2>
<p>The syntax of the configuration file is very simple. The elinks.conf file is a free-form ASCII text file. The file may contain extra tabs and newlines for formatting purposes. Keywords in the file are case-sensitive. Comments may be placed anywhere within the file (except within quotes). Comments begin with the # character and end at the end of the line.</p>
<h2>Examples</h2>
<p>Some sample settings: </p>
<pre><code># Use asynchronous DNS resolver?
set connection.async_dns = 1
# horizontal text margin.
set document.browse.margin_width = 3
# Default document codepage.
set document.codepage.assume = &quot;ISO-8859-1&quot;
# User defined protocol handlers
set protocol.user.mailto.unix = &quot;mutt %h -s \&quot;%s\&quot;&quot;</code></pre>
<h2>Options</h2>
<p>Generated using output from ELinks version 0.13.GIT.</p>
<h3>bookmarks (Bookmarks)</h3>
<p>Bookmark options. </p>
<p> bookmarks.file_format <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>File format for bookmarks (affects both reading and saving): </p>
<dl>
<dd>&bull;0 is the default native ELinks format</dl>
<dl>
<dd>&bull;1 is XBEL universal XML bookmarks format</dl>
</dl>
<p> bookmarks.folder_state <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When saving bookmarks also store whether folders are expanded or not, so the look of the bookmark dialog is kept across ELinks sessions. If disabled all folders will appear unexpanded next time ELinks is run.</dl>
<h3>config (Configuration system)</h3>
<p>Configuration handling options. </p>
<p> config.comments <code>&lt;num&gt;</code> (default: 3)</p>
<dl>
<dd>Amount of comments automatically written to the config file: </p>
<dl>
<dd>&bull;0 is no comments are written</dl>
<dl>
<dd>&bull;1 is only the &quot;blurb&quot; (name+type) is written</dl>
<dl>
<dd>&bull;2 is only the description is written</dl>
<dl>
<dd>&bull;3 is full comments are written</dl>
</dl>
<p> config.indentation <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>Shift width of one indentation level in the configuration file. Zero means that no indentation is performed at all when saving the configuration.</dl>
<p> config.saving_style <code>&lt;num&gt;</code> (default: 3)</p>
<dl>
<dd>Determines what happens when you tell ELinks to save options: </p>
<dl>
<dd>&bull;0 is only values of current options are altered</dl>
<dl>
<dd>&bull;1 is values of current options are altered and missing options are added at the end of the file</dl>
<dl>
<dd>&bull;2 is the configuration file is rewritten from scratch</dl>
<dl>
<dd>&bull;3 is values of current options are altered and missing options CHANGED during this ELinks session are added at the end of the file</dl>
</dl>
<p> config.i18n <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>If set to 1, comments in the configuration file will be translated to the language used by UI. Note that if you have different language set in different terminals, the language used in the configuration file MAY be the same as on the terminal where you saved the file, but it should be generally considered unpredictable.</dl>
<p> config.saving_style_w <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>This is internal option used when displaying a warning about obsolete config.saving_style. You shouldn&#8217;t touch it.</dl>
<p> config.show_template <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Show template options in autocreated trees in the options manager and save them to the configuration file.</dl>
<h3>connection (Connections)</h3>
<p>Connection options. </p>
<p> connection.async_dns <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to use asynchronous DNS resolving.</dl>
<p> connection.max_connections <code>&lt;num&gt;</code> (default: 10)</p>
<dl>
<dd>Maximum number of concurrent connections.</dl>
<p> connection.max_connections_to_host <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>Maximum number of concurrent connections to a given host.</dl>
<p> connection.receive_timeout <code>&lt;num&gt;</code> (default: 120)</p>
<dl>
<dd>Receive timeout (in seconds).</dl>
<p> connection.retries <code>&lt;num&gt;</code> (default: 3)</p>
<dl>
<dd>Number of tries to establish a connection. Zero means try forever.</dl>
<p> connection.try_ipv4 <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to try to connect to a host over IPv4. Note that if connection.try_ipv6 is enabled too, it takes precedence. And better do not touch this at all unless you are sure what are you doing. </p>
<p> Note that you can also force a given protocol to be used on a per-connection basis by using a URL in the style of e.g. <i>http4://elinks.cz/</i>.</dl>
<p> connection.try_ipv6 <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to try to connect to a host over IPv6. </p>
<p> Note that you can also force a given protocol to be used on a per-connection basis by using a URL in the style of e.g. <i>http6://elinks.cz/</i>.</dl>
<p> connection.unrestartable_receive_timeout <code>&lt;num&gt;</code> (default: 600)</p>
<dl>
<dd>Timeout for non-restartable connections (in seconds).</dl>
<h3>connection.ssl (SSL)</h3>
<p>SSL options. </p>
<p> connection.ssl.cert_verify <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Verify the peer&#8217;s SSL certificate. Note that this needs extensive configuration of OpenSSL by the user.</dl>
<h3>connection.ssl.client_cert (Client Certificates)</h3>
<p>X509 client certificate options. </p>
<p> connection.ssl.client_cert.enable <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Enable or not the sending of X509 client certificates to servers which request them.</dl>
<p> connection.ssl.client_cert.file <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>The location of a file containing the client certificate and unencrypted private key in PEM format. If unset, the file pointed to by the <code>X509_CLIENT_CERT</code> variable is used instead.</dl>
<h3>cookies (Cookies)</h3>
<p>Cookies options. </p>
<p> cookies.accept_policy <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>Cookies accepting policy: </p>
<dl>
<dd>&bull;0 is accept no cookies</dl>
<dl>
<dd>&bull;1 is ask for confirmation before accepting cookie</dl>
<dl>
<dd>&bull;2 is accept all cookies</dl>
</dl>
<p> cookies.max_age <code>&lt;num&gt;</code> (default: -1)</p>
<dl>
<dd>Cookie maximum age (in days): </p>
<dl>
<dd>&bull;-1 is use cookie&#8217;s expiration date if any</dl>
<dl>
<dd>&bull;0 is force expiration at the end of session, ignoring cookie&#8217;s expiration date</dl>
<dl>
<dd>&bull;1+ is use cookie&#8217;s expiration date, but limit age to the given number of days</dl>
</dl>
<p> cookies.paranoid_security <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>When enabled, we&#8217;ll require three dots in cookies domain for all non-international domains (instead of just two dots). Some countries have generic second level domains (eg. .com.pl, .co.uk) and allowing sites to set cookies for these generic domains could potentially be very bad. Note, it is off by default as it breaks a lot of sites.</dl>
<p> cookies.save <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether cookies should be loaded from and saved to disk.</dl>
<p> cookies.resave <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Save cookies after each change in cookies list? No effect when cookie saving (cookies.save) is off.</dl>
<h3>document (Document)</h3>
<p>Document options.</p>
<h3>document.browse (Browsing)</h3>
<p>Document browsing options (mainly interactivity). </p>
<p> document.browse.margin_width <code>&lt;num&gt;</code> (default: 3)</p>
<dl>
<dd>Horizontal text margin.</dl>
<p> document.browse.refresh <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Automatically follow document-specified refresh directives (&#8216;&lt;meta&gt; refresh&#8217; tags). Web-page authors use these to instruct the browser to reload a document at a given interval or to load another page. Regardless of the value the refresh URI is accessible as a link. </p>
<p> Use the document.browse.minimum_refresh_time to control the minimum number of seconds a refresh will wait.</dl>
<p> document.browse.minimum_refresh_time <code>&lt;num&gt;</code> (default: 1000)</p>
<dl>
<dd>The minimum number of milliseconds that should pass before refreshing. If set to zero the document refresh time is used unchanged. It can fix going back in history for some sites that use refreshing with zero values.</dl>
<p> document.browse.table_move_order <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Move by columns in table, instead of rows.</dl>
<h3>document.browse.accesskey (Access keys)</h3>
<p>Options for handling of link access keys. An HTML document can use the ACCESSKEY attribute to assign an access key to an element. When an access key is pressed, the corresponding element will be given focus. </p>
<p> document.browse.accesskey.auto_follow <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Automatically follow a link or submit a form if appropriate accesskey is pressed &#8211; this is the standard behaviour, but it&#8217;s considered dangerous.</dl>
<p> document.browse.accesskey.display <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Display access key in link info.</dl>
<p> document.browse.accesskey.priority <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Priority of &#8216;accesskey&#8217; HTML attribute: </p>
<dl>
<dd>&bull;0 is first try all normal bindings; if it fails, check accesskey</dl>
<dl>
<dd>&bull;1 is first try only frame bindings; if it fails, check accesskey</dl>
<dl>
<dd>&bull;2 is first check accesskey (this can be dangerous)</dl>
</dl>
<h3>document.browse.forms (Forms)</h3>
<p>Options for handling of the forms interaction. </p>
<p> document.browse.forms.auto_submit <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Automagically submit a form when enter is pressed with a text field selected.</dl>
<p> document.browse.forms.confirm_submit <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Ask for confirmation when submitting a form.</dl>
<p> document.browse.forms.input_size <code>&lt;num&gt;</code> (default: 20)</p>
<dl>
<dd>Default form input size if none is specified.</dl>
<p> document.browse.forms.insert_mode <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>The setting for this option affects how key presses are handled when one selects a text-input form-field. When enabled, one must explicitly &#8216;enter&#8217; a selected text-field to edit it; this prevents text fields from capturing key presses, such as presses of a scroll key, when it is inadvertently selected. When disabled, key presses are always inserted into a selected text field.</dl>
<p> document.browse.forms.editor <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Path to the executable that ELinks should launch when the user requests to edit a textarea with an external editor. </p>
<p> If this is blank, ELinks will use the value of the environmental variable <code>$EDITOR</code>. If <code>$EDITOR</code> is empty or not set, ELinks will then default to <code>vi</code>.</dl>
<p> document.browse.forms.show_formhist <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Ask if a login form should be saved to file or not. This option only disables the dialog, already saved login forms are unaffected.</dl>
<h3>document.browse.images (Images)</h3>
<p>Options for handling of images. </p>
<p> document.browse.images.display_style <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>Display style for image tags when displayed: </p>
<dl>
<dd>&bull;0 means always display IMG</dl>
<dl>
<dd>&bull;1 means always display filename</dl>
<dl>
<dd>&bull;2 means display alt/title attribute if possible, IMG if not</dl>
<dl>
<dd>&bull;3 means display alt/title attribute if possible, filename if not</dl>
</dl>
<p> document.browse.images.filename_maxlen <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Maximum length of image filename when displayed: </p>
<dl>
<dd>&bull;0 means always display full filename</dl>
<dl>
<dd>&bull;1-500 means display filename with this maximal length; if it is longer, the middle is substituted by an asterisk</dl>
</dl>
<p> document.browse.images.image_link_tagging <code>&lt;num&gt;</code> (default: 1)</p>
<dl>
<dd>When to enclose image links: </p>
<dl>
<dd>&bull;0 means never</dl>
<dl>
<dd>&bull;1 means never if alt or title are provided (old behavior)</dl>
<dl>
<dd>&bull;2 means always</dl>
</dl>
<p> document.browse.images.image_link_prefix <code>&lt;str&gt;</code> (default: &quot;[&quot;)</p>
<dl>
<dd>Prefix string to use to mark image links.</dl>
<p> document.browse.images.image_link_suffix <code>&lt;str&gt;</code> (default: &quot;]&quot;)</p>
<dl>
<dd>Suffix string to use to mark image links.</dl>
<p> document.browse.images.label_maxlen <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Maximum length of image label (alt/title): </p>
<dl>
<dd>&bull;0 means always display full label</dl>
<dl>
<dd>&bull;1-500 means display label with this maximal length; if it is longer, the middle is substituted by an asterisk</dl>
</dl>
<p> document.browse.images.show_as_links <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Display links to images without an alt attribute. If this option is off, these images are completely invisible.</dl>
<p> document.browse.images.show_any_as_links <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Display links to any images in the document, regardless of them having an alt attribute or not. If this option is off, the alt attribute contents is shown, but as normal text, not selectable as a link.</dl>
<h3>document.browse.links (Links)</h3>
<p>Options for handling of links to other documents. </p>
<p> document.browse.links.color_dirs <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Highlight links to directories in FTP and local directory listing.</dl>
<p> document.browse.links.numbering <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Display numbers next to the links.</dl>
<p> document.browse.links.target_blank <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Define how to handle links having target=_blank set: </p>
<dl>
<dd>&bull;0 means open link in current tab</dl>
<dl>
<dd>&bull;1 means open link in new tab in foreground</dl>
<dl>
<dd>&bull;2 means open link in new tab in background</dl>
<dl>
<dd>&bull;3 means open link in new window</dl>
</dl>
<p> document.browse.links.use_tabindex <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to navigate links using tabindex specified ordering. The TABINDEX attribute in HTML elements specifies the order in which links should receive focus when using the keyboard to navigate the document.</dl>
<p> document.browse.links.missing_fragment <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Open a message box when document has no tag with given id.</dl>
<p> document.browse.links.number_keys_select_link <code>&lt;num&gt;</code> (default: 1)</p>
<dl>
<dd>Number keys select links rather than specify command prefixes. This is a tristate: </p>
<dl>
<dd>&bull;0 means never</dl>
<dl>
<dd>&bull;1 means if document.browse.links.numbering = 1</dl>
<dl>
<dd>&bull;2 means always</dl>
</dl>
<p> document.browse.links.warn_malicious <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When following a link the user ID part of the URI is checked and if a maliciously crafted URI is detected a warning dialog will ask before following the link.</dl>
<p> document.browse.links.wraparound <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>When pressing &#8216;down&#8217; on the last link, jump to the first one, and vice versa.</dl>
<h3>document.browse.links.active_link (Active link)</h3>
<p>Options for the active link. </p>
<p> document.browse.links.active_link.enable_color <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Enable use of the active link background and text color settings instead of the link colors from the document.</dl>
<p> document.browse.links.active_link.bold <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Make the active link text bold.</dl>
<p> document.browse.links.active_link.invert <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Invert the fore- and background color so the link stands out.</dl>
<p> document.browse.links.active_link.underline <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Underline the active link.</dl>
<h3>document.browse.links.active_link.colors (Colors)</h3>
<p>Active link colors. </p>
<p> document.browse.links.active_link.colors.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<p> document.browse.links.active_link.colors.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<h3>document.browse.scrolling (Scrolling)</h3>
<p>Scrolling options. </p>
<p> document.browse.scrolling.horizontal_extended <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to allow horizontal scrolling when the document does not extend off the screen. Useful for copy/paste operations.</dl>
<p> document.browse.scrolling.horizontal_step <code>&lt;num&gt;</code> (default: 8)</p>
<dl>
<dd>Number of columns to scroll when a key bound to scroll-left or scroll-right is pressed and no prefix was given.</dl>
<p> document.browse.scrolling.margin <code>&lt;num&gt;</code> (default: 3)</p>
<dl>
<dd>Size of the virtual margin &#8211; when you click inside of that margin, document scrolls in that direction.</dl>
<p> document.browse.scrolling.vertical_overlap <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Number of overlapping lines between the new page displayed and the previous one when scrolling one page up or down.</dl>
<p> document.browse.scrolling.vertical_step <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>Number of lines to scroll when a key bound to scroll-up or scroll-down is pressed and no prefix was given.</dl>
<h3>document.browse.search (Searching)</h3>
<p>Options for searching. </p>
<p> document.browse.search.case <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether the search should match the document text while maintaining case sensitivity.</dl>
<p> document.browse.search.regex <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Enable searching with regular expressions: </p>
<dl>
<dd>&bull;0 for plain text searching</dl>
<dl>
<dd>&bull;1 for basic regular expression searches</dl>
<dl>
<dd>&bull;2 for extended regular expression searches</dl>
</dl>
<p> document.browse.search.show_hit_top_bottom <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to show a dialog when the search hits the top or bottom of the document.</dl>
<p> document.browse.search.wraparound <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Wrap around when searching. Currently only used for typeahead.</dl>
<p> document.browse.search.show_not_found <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>How to inform the user when nothing is matched: </p>
<dl>
<dd>&bull;0 means do nothing</dl>
<dl>
<dd>&bull;1 means beep the terminal</dl>
<dl>
<dd>&bull;2 means pop up message box</dl>
</dl>
<p> document.browse.search.typeahead <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Start typeahead searching when an unbound key is pressed without any modifiers. Note that most keys have default bindings, so this feature will not be useful unless you unbind them. </p>
<dl>
<dd>&bull;0 disables this feature; typeahead searching will only be used when you press a key bound to search-typeahead or similar</dl>
<dl>
<dd>&bull;1 automatically starts typeahead searching thru link text</dl>
<dl>
<dd>&bull;2 automatically starts typeahead searching thru all document text</dl>
</dl>
<h3>document.cache (Cache)</h3>
<p>Cache options. </p>
<p> document.cache.cache_redirects <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Cache even redirects sent by server (usually thru HTTP by a 302 HTTP code and a Location header). This was the original behaviour for quite some time, but it causes problems in a situation very common to various web login systems &#8211; frequently, when accessing a certain location, they will redirect you to a login page if they don&#8217;t receive an auth cookie, the login page then gives you the cookie and redirects you back to the original page, but there you have already cached redirect back to the login page! If this option has value of 0, this malfunction is fixed, but occasionally you may get superfluous (depends on how you take it ;-) requests to the server. If this option has value of 1, experienced users can still workaround it by clever combination of usage of reload, jumping around in session history and hitting ctrl+enter. </p>
<p> Note that this option is checked when retrieving the information from cache, not when saving it to cache &#8211; thus if you enable it, even previous redirects will be taken from cache instead of asking the server.</dl>
<p> document.cache.ignore_cache_control <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Ignore Cache-Control and Pragma server headers. When set, the document is cached even with &#8216;Cache-Control: no-cache&#8217;.</dl>
<p> document.cache.revalidation_interval <code>&lt;num&gt;</code> (default: -1)</p>
<dl>
<dd>Period in seconds that a cache entry is considered to be up-to-date. When a document is loaded and this interval has elapsed since the document was initially loaded or most recently revalidated with the server, the server will be checked in case there is a more up-to-date version of the document. </p>
<p> A value of -1 disables automatic revalidation.</dl>
<h3>document.cache.format (Formatted documents)</h3>
<p>Format cache options. </p>
<p> document.cache.format.size <code>&lt;num&gt;</code> (default: 5)</p>
<dl>
<dd>Number of cached formatted pages. Do not get too generous here, &#8216;formatted&#8217; means that all the accompanying structures are kept in memory so that you get the cached document immediately, but these structures may take a lot &#8211; 2x the size of the HTML source is probably not unusual, but it can be even more if the document consists of a lot of short lines (padded right, if possible) and links and not much other markup. So if you set this to 256 and then you don&#8217;t like your ELinks eating 90M, don&#8217;t come complaining to us. ;-) </p>
<p> Also note that the format cache itself is not counted to the memory cache size, but the HTML source of the formatted documents is always cached, even if it is over the memory cache size threshold. (Then of course no other documents can be cached.)</dl>
<h3>document.cache.memory (Memory cache)</h3>
<p>Memory cache options. </p>
<p> document.cache.memory.size <code>&lt;num&gt;</code> (default: 1048576)</p>
<dl>
<dd>Memory cache size (in bytes).</dl>
<h3>document.codepage (Charset)</h3>
<p>Charset options. </p>
<p> document.codepage.assume <code>&lt;codepage&gt;</code> (default: System)</p>
<dl>
<dd>Default document codepage. &#8216;System&#8217; stands for a codepage determined by a selected locale.</dl>
<p> document.codepage.force_assumed <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Ignore charset info sent by server.</dl>
<h3>document.colors (Default color settings)</h3>
<p>Default document color settings. </p>
<p> document.colors.text <code>&lt;color|#rrggbb&gt;</code> (default: gray75)</p>
<dl>
<dd>Default text color.</dl>
<p> document.colors.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<p> document.colors.link <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default link color.</dl>
<p> document.colors.vlink <code>&lt;color|#rrggbb&gt;</code> (default: yellow)</p>
<dl>
<dd>Default visited link color.</dl>
<p> document.colors.image <code>&lt;color|#rrggbb&gt;</code> (default: darkolivegreen)</p>
<dl>
<dd>Default image link color.</dl>
<p> document.colors.bookmark <code>&lt;color|#rrggbb&gt;</code> (default: hotpink)</p>
<dl>
<dd>Default bookmarked link color.</dl>
<p> document.colors.dirs <code>&lt;color|#rrggbb&gt;</code> (default: yellow)</p>
<dl>
<dd>Default directory color. </p>
<p> See document.browse.links.color_dirs option.</dl>
<p> document.colors.increase_contrast <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Increase the contrast between the foreground and background colors to ensure readability. For example it disallows dark colors on a black background. Note, this is different from ensuring the contrast with the ensure_contrast option.</dl>
<p> document.colors.ensure_contrast <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Makes sure that the back- and foreground colors are never equal.</dl>
<p> document.colors.use_document_colors <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>Use colors specified in document: </p>
<dl>
<dd>&bull;0 is use always the default settings</dl>
<dl>
<dd>&bull;1 is use document colors if available, except background</dl>
<dl>
<dd>&bull;2 is use document colors, including background. This can mostly look very impressive, but some sites will appear really ugly. Note, that obviously if the background is not black, it will break the behaviour of transparency.</dl>
</dl>
<h3>document.css (Cascading Style Sheets)</h3>
<p>Options concerning how to use CSS for styling documents. </p>
<p> document.css.enable <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Enable adding of CSS style info to documents.</dl>
<p> document.css.ignore_display_none <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When enabled, elements are rendered, even when their display property has the value &quot;none&quot;. Because ELinks&#8217;s CSS support is still very incomplete, this setting can improve the way that some documents are rendered.</dl>
<p> document.css.import <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When enabled any external style sheets that are imported from either CSS itself using the @import keyword or from the HTML using &lt;link&gt; tags in the document header will also be downloaded.</dl>
<p> document.css.media <code>&lt;str&gt;</code> (default: &quot;tty&quot;)</p>
<dl>
<dd>CSS media types that ELinks claims to support, separated with commas. The &quot;all&quot; type is implied. Currently, only ASCII characters work reliably here. See CSS2 section 7: <i><a rel="nofollow" href="http://www.w3.org/TR/1998/REC-CSS2-19980512/media.html">http://www.w3.org/TR/1998/REC-CSS2-19980512/media.html</a></i></dl>
<p> document.css.stylesheet <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>The path to the file containing the default user defined Cascading Style Sheet. It can be used to control the basic layout of HTML documents. The path is assumed to be relative to ELinks&#8217; home directory. </p>
<p> Leave as &quot;&quot; to use built-in document styling.</dl>
<h3>document.download (Downloading)</h3>
<p>Options regarding files downloading and handling. </p>
<p> document.download.directory <code>&lt;str&gt;</code> (default: &quot;./&quot;)</p>
<dl>
<dd>Default download directory.</dl>
<p> document.download.set_original_time <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Set the timestamp of each downloaded file to the timestamp stored on the server.</dl>
<p> document.download.overwrite <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>Prevent overwriting the local files: </p>
<dl>
<dd>&bull;0 is files will silently be overwritten</dl>
<dl>
<dd>&bull;1 is add a suffix .{number} (for example &#8216;.1&#8217;) to the name</dl>
<dl>
<dd>&bull;2 is ask the user</dl>
</dl>
<p> document.download.notify_bell <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Audio notification when download is completed: </p>
<dl>
<dd>&bull;0 is never</dl>
<dl>
<dd>&bull;1 is when background notification is active</dl>
<dl>
<dd>&bull;2 is always</dl>
</dl>
<h3>document.dump (Dump output)</h3>
<p>Dump output options. </p>
<p> document.dump.codepage <code>&lt;codepage&gt;</code> (default: System)</p>
<dl>
<dd>Codepage used in dump output. &#8216;System&#8217; stands for a codepage determined by a selected locale.</dl>
<p> document.dump.color_mode <code>&lt;num&gt;</code> (default: -1)</p>
<dl>
<dd>Color mode for dumps. </p>
<p> Some modes may have been disabled at compile time. The Setup -&gt; Terminal options dialog lists the modes supported by this executable. If you select an unsupported mode, ELinks uses 16 colors. </p>
<p> The color modes are: </p>
<dl>
<dd>&bull;-1 is standard dump mode</dl>
<dl>
<dd>&bull;0 is mono mode</dl>
<dl>
<dd>&bull;1 is 16 color mode</dl>
<dl>
<dd>&bull;2 is 88 color mode</dl>
<dl>
<dd>&bull;3 is 256 color mode</dl>
<dl>
<dd>&bull;4 is true color mode</dl>
</dl>
<p> document.dump.footer <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Footer string used in dumps. %u is substituted by URL.</dl>
<p> document.dump.header <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Header string used in dumps. %u is substituted by URL.</dl>
<p> document.dump.numbering <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to print link numbers in dump output.</dl>
<p> document.dump.references <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Whether to print references (URIs) of document links in dump output.</dl>
<p> document.dump.separator <code>&lt;str&gt;</code> (default: &quot; &quot;)</p>
<dl>
<dd>String which separates two dumps.</dl>
<p> document.dump.width <code>&lt;num&gt;</code> (default: 80)</p>
<dl>
<dd>Width of screen in characters when dumping documents.</dl>
<h3>document.history (History)</h3>
<p>History options. </p>
<p> document.history.keep_unhistory <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Keep unhistory (&quot;forward history&quot;).</dl>
<h3>document.history.global (Global history)</h3>
<p>Global history options. </p>
<p> document.history.global.enable <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Enable global history (&quot;history of all pages visited&quot;).</dl>
<p> document.history.global.max_items <code>&lt;num&gt;</code> (default: 1024)</p>
<dl>
<dd>Maximum number of entries in the global history.</dl>
<p> document.history.global.display_type <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>What to display in global history dialog: </p>
<dl>
<dd>&bull;0 is URLs</dl>
<dl>
<dd>&bull;1 is page titles</dl>
</dl>
<h3>document.html (HTML rendering)</h3>
<p>Options concerning the display of HTML pages. </p>
<p> document.html.display_frames <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Display frames.</dl>
<p> document.html.display_tables <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Display tables.</dl>
<p> document.html.display_subs <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Display subscripts (as [thing]).</dl>
<p> document.html.display_sups <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Display superscripts (as ^thing).</dl>
<p> document.html.link_display <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>How to render &lt;link&gt; tags from the HTML header: </p>
<dl>
<dd>&bull;0 is nothing</dl>
<dl>
<dd>&bull;1 is title</dl>
<dl>
<dd>&bull;2 is name in addition</dl>
<dl>
<dd>&bull;3 is hreflang in addition</dl>
<dl>
<dd>&bull;4 is type in addition</dl>
<dl>
<dd>&bull;5 is everything</dl>
</dl>
<p> document.html.underline_links <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Underline links.</dl>
<p> document.html.wrap_nbsp <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>If set do not honour non breaking space (the nbsp entity) but allows one to wrap the text. This can help keeping the width of documents down so no horizontal scrolling is needed.</dl>
<h3>document.plain (Plain rendering)</h3>
<p>Options concerning the display of plain text pages. </p>
<p> document.plain.display_links <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Display URIs in the document as links.</dl>
<p> document.plain.compress_empty_lines <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Compress successive empty lines to only one in displayed text.</dl>
<h3>document.uri_passing (URI passing)</h3>
<p>Rules for passing URIs to external commands. When one rule is defined the link and tab menu will have a menu item that makes it possible to pass the the link, frame or tab URI to an external command. If several rules are defined the link and tab menu will have a submenu of items for each rule. </p>
<p> Note, this is mostly useful for launching graphical viewers, since there is no support for releasing the terminal while the command runs. The action and submenus are also available by binding keys to the frame-external-command, the link-external-command, and the tab-external-command actions. </p>
<p> document.uri_passing._template_ <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>A rule for passing URI to an external command. The format is: </p>
<dl>
<dd>&bull;%c in the string means the current URL</dl>
<dl>
<dd>&bull;%% in the string means &#8216;%&#8217;</dl>
<dl>
<dd>Do <code>not</code> put single- or double-quotes around %c.</dl>
</dl>
<h3>ecmascript (ECMAScript)</h3>
<p>ECMAScript options. </p>
<p> ecmascript.enable <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to run those scripts inside of documents.</dl>
<p> ecmascript.error_reporting <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Open a message box when a script reports an error.</dl>
<p> ecmascript.ignore_noscript <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to ignore content enclosed by the &lt;noscript&gt; tag when ECMAScript is enabled.</dl>
<p> ecmascript.max_exec_time <code>&lt;num&gt;</code> (default: 5)</p>
<dl>
<dd>Maximum execution time in seconds for a script.</dl>
<p> ecmascript.block_window_opening <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to disallow scripts to open new windows or tabs.</dl>
<h3>infofiles (Information files)</h3>
<p>Options for information files in <i>~/.elinks</i>. </p>
<p> infofiles.save_interval <code>&lt;num&gt;</code> (default: 300)</p>
<dl>
<dd>Interval at which to trigger information files in <i>~/.elinks</i> to be saved to disk if they have changed (seconds; 0 to disable)</dl>
<p> infofiles.secure_save <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>First write data to unique temporary file, then rename this file upon successfully finishing this. Note that this relates only to config files, not downloaded files. You may want to disable it if you are using some exotic permissions for concerned files. Secure file saving is automagically disabled if file is symlink. </p>
<p> Warning: some systems (ie. OS/2, Win32) require that destination file doesn&#8217;t exist when <code><a href="/docs/linux/man/3-rename/">rename</a></code>(3) is called, breaking atomicity, and reducing reliability of this feature.</dl>
<p> infofiles.secure_save_fsync <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When using secure file saving, call <code><a href="/docs/linux/man/3-fsync/">fsync</a></code>(3), if the OS supports it, to force the OS immediately to write the data to permanent storage. This is optional for those who wish to avoid excessive disk I/O.</dl>
<h3>mime (MIME)</h3>
<p>MIME-related options (handlers of various MIME types). </p>
<p> mime.default_type <code>&lt;str&gt;</code> (default: &quot;application/octet-stream&quot;)</p>
<dl>
<dd>Document MIME-type to assume by default (when we are unable to guess it properly from known information about the document).</dl>
<h3>mime.extension (File extension associations)</h3>
<p>Extension &harr; MIME type association. </p>
<p> mime.extension._template_ <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>MIME-type matching this file extension (&#8216;*&#8217; is used here in place of &#8216;.&#8217;).</dl>
<h3>mime.handler (File type handlers)</h3>
<p>A file type handler is a set of information about how to use an external program to view a file. It is possible to refer to it for several MIME types &#8212; e.g., you can define an &#8216;image&#8217; handler to which mime.type.image.png, mime.type.image.jpeg, and so on will refer; or one might define a handler for a more specific type of file &#8212; e.g., PDF files. Note you must define both a MIME handler and a MIME type association for it to work.</p>
<h3>mime.handler._template_ (Template option folder)</h3>
<p>Description of this handler.</p>
<h3>mime.handler._template_._template_ (Template option folder)</h3>
<p>System-specific handler description (ie. unix, unix-xwin, &#8230;). </p>
<p> mime.handler._template_._template_.ask <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Ask before opening.</dl>
<p> mime.handler._template_._template_.block <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Block the terminal when the handler is running.</dl>
<p> mime.handler._template_._template_.program <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>External viewer for this file type. &#8216;%&#8217; in this string will be substituted by a file name. Do <code>not</code> put single- or double-quotes around the % sign.</dl>
<h3>mime.mailcap (Mailcap)</h3>
<p>Options for mailcap support. </p>
<p> mime.mailcap.enable <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Enable mailcap support.</dl>
<p> mime.mailcap.path <code>&lt;str&gt;</code> (default: &quot;~/.mailcap:/etc/mailcap:/usr/etc/mailcap:/usr/local/etc/mailcap:/usr/share/mailcap:/usr/share/misc/mailcap&quot;)</p>
<dl>
<dd>Mailcap search path. Colon-separated list of files. Leave as &quot;&quot; to use <code>MAILCAP</code> environment variable instead.</dl>
<p> mime.mailcap.ask <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Ask before using the handlers defined by mailcap.</dl>
<p> mime.mailcap.description <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Type of description to show in &quot;what to do with this file&quot; query dialog: </p>
<dl>
<dd>&bull;0 is show &quot;mailcap&quot;</dl>
<dl>
<dd>&bull;1 is show program to be run</dl>
<dl>
<dd>&bull;2 is show mailcap description field if any; &quot;mailcap&quot; otherwise</dl>
</dl>
<p> mime.mailcap.prioritize <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Prioritize entries by the order of the files in the mailcap path. This means that wildcard entries (like: image/*) will also be checked before deciding the handler.</dl>
<h3>mime.mimetypes (Mimetypes files)</h3>
<p>Options for the support of <i>mime.types</i> files. These files can be used to find the content type of a URL by looking at the extension of the file name. </p>
<p> mime.mimetypes.enable <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Enable <i>mime.types</i> support.</dl>
<p> mime.mimetypes.path <code>&lt;str&gt;</code> (default: &quot;~/.mime.types:/etc/mime.types:/usr/etc/mime.types:/usr/local/etc/mime.types:/usr/share/mime.types:/usr/share/misc/mime.types&quot;)</p>
<dl>
<dd>The search path for <i>mime.types</i> files. Colon-separated list of files.</dl>
<h3>mime.type (MIME type associations)</h3>
<p>Handler &harr; MIME type association. The first sub-tree is the MIME class while the second sub-tree is the MIME type (ie. image/gif handler will reside at mime.type.image.gif). Each MIME type option should contain (case-sensitive) name of the MIME handler (its properties are stored at mime.handler.&lt;name&gt;).</p>
<h3>mime.type._template_ (Template option folder)</h3>
<p>Handler matching this MIME-type class (&#8216;*&#8217; is used here in place of &#8216;.&#8217;). </p>
<p> mime.type._template_._template_ <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Handler matching this MIME-type name (&#8216;*&#8217; is used here in place of &#8216;.&#8217;).</dl>
<h3>protocol (Protocols)</h3>
<p>Protocol specific options. </p>
<p> protocol.no_proxy <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Comma separated list of domains for which the proxy (HTTP/FTP) should be disabled. Optionally, a port can be specified for some domains as well. If it&#8217;s blank, <code>NO_PROXY</code> environment variable is checked as well.</dl>
<h3>protocol.bittorrent (BitTorrent)</h3>
<p>BitTorrent specific options. </p>
<p> protocol.bittorrent.piece_cache_size <code>&lt;num&gt;</code> (default: 1048576)</p>
<dl>
<dd>The maximum amount of memory used to hold recently downloaded pieces. </p>
<p> Set to 0 to have unlimited size.</dl>
<p> protocol.bittorrent.max_uploads <code>&lt;num&gt;</code> (default: 7)</p>
<dl>
<dd>The maximum number of uploads to allow at once.</dl>
<p> protocol.bittorrent.min_uploads <code>&lt;num&gt;</code> (default: 2)</p>
<dl>
<dd>The minimum number of uploads which should at least be used for new connections.</dl>
<p> protocol.bittorrent.request_queue_size <code>&lt;num&gt;</code> (default: 5)</p>
<dl>
<dd>How many piece requests to continuously keep in queue. Pipelining of requests is essential to saturate connections and get a good connection performance and thus a faster download. However, a very big queue size can lead to wasting bandwidth near the end of the connection since remaining piece blocks will be requested from multiple peers.</dl>
<p> protocol.bittorrent.choke_interval <code>&lt;num&gt;</code> (default: 10)</p>
<dl>
<dd>The number of seconds between updating the connection state and most importantly choke and unchoke peer connections. The choke period should be big enough for newly unchoked connections to get started but small enough to not allow freeriders too much room for stealing bandwidth.</dl>
<p> protocol.bittorrent.rarest_first_cutoff <code>&lt;num&gt;</code> (default: 4)</p>
<dl>
<dd>The number of pieces to obtain before switching piece selection strategy from random to rarest first.</dl>
<p> protocol.bittorrent.allow_blacklist <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Allow blacklisting of buggy peers.</dl>
<h3>protocol.bittorrent.ports (Port range)</h3>
<p>Port range allowed to be used for listening on. </p>
<p> protocol.bittorrent.ports.min <code>&lt;num&gt;</code> (default: 6881)</p>
<dl>
<dd>The minimum port to try and listen on.</dl>
<p> protocol.bittorrent.ports.max <code>&lt;num&gt;</code> (default: 6999)</p>
<dl>
<dd>The maximum port to try and listen on.</dl>
<h3>protocol.bittorrent.tracker (Tracker)</h3>
<p>Tracker options. </p>
<p> protocol.bittorrent.tracker.compact <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to request that the tracker returns peer info in compact format. Note, the compact format only supports IPv4 addresses.</dl>
<p> protocol.bittorrent.tracker.interval <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>The number of seconds to wait between periodically contacting the tracker for announcing progress and requesting more peers. Set to zero to use the interval requested by the tracker.</dl>
<p> protocol.bittorrent.tracker.ip_address <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>What IP address to report to the tracker. If set to &quot;&quot; no IP address will be sent and the tracker will automatically determine an appropriate IP address.</dl>
<p> protocol.bittorrent.tracker.key <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>An additional identification that is not shared with any users. It is intended to allow a client to prove their identity should their IP address change. It is an optional parameter, but some trackers require this parameter. If set to &quot;&quot; no user key will be sent to the tracker.</dl>
<p> protocol.bittorrent.tracker.numwant <code>&lt;num&gt;</code> (default: 50)</p>
<dl>
<dd>The maximum number of peers to request from the tracker. Set to 0 to use the server default.</dl>
<p> protocol.bittorrent.tracker.min_skip_size <code>&lt;num&gt;</code> (default: 20)</p>
<dl>
<dd>The minimum number of peers to have in the current peer info pool before skipping requesting of more peers. I.e. setting numwant to zero. Set to 0 to not have any limit.</dl>
<h3>protocol.bittorrent.peerwire (Peer-wire)</h3>
<p>Lowlevel peer-wire options. </p>
<p> protocol.bittorrent.peerwire.connections <code>&lt;num&gt;</code> (default: 55)</p>
<dl>
<dd>The maximum number of allowed connections to both active and non-active peers. By increasing the number of allowed connections, the chance of finding good peers to download from is increased. However, too many connections can lead to TCP congestion. If the maximum is reached all new incoming connections will be closed.</dl>
<p> protocol.bittorrent.peerwire.max_message_length <code>&lt;num&gt;</code> (default: 8388608)</p>
<dl>
<dd>The maximum length of messages to accept over the wire. Larger values will cause the connection to be dropped.</dl>
<p> protocol.bittorrent.peerwire.max_request_length <code>&lt;num&gt;</code> (default: 8388608)</p>
<dl>
<dd>The maximum length to allow for incoming requests. Larger requests will cause the connection to be dropped.</dl>
<p> protocol.bittorrent.peerwire.request_length <code>&lt;num&gt;</code> (default: 16384)</p>
<dl>
<dd>How many bytes to query for per request. This is complementary to the max_request_length option. If the configured length is bigger than the piece length it will be truncated.</dl>
<p> protocol.bittorrent.peerwire.timeout <code>&lt;num&gt;</code> (default: 300)</p>
<dl>
<dd>The number of seconds to wait before closing a socket on which nothing has been received or sent.</dl>
<p> protocol.bittorrent.peerwire.pool_size <code>&lt;num&gt;</code> (default: 55)</p>
<dl>
<dd>Maximum number of items in the peer pool. The peer pool contains information used for establishing connections to new peers. </p>
<p> Set to 0 to have unlimited size.</dl>
<h3>protocol.file (Local files)</h3>
<p>Options specific to local browsing. </p>
<p> protocol.file.allow_special_files <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to allow reading from non-regular files. Note this can be dangerous; reading <i>/dev/urandom</i> or <i>/dev/zero</i> can ruin your day!</dl>
<p> protocol.file.show_hidden_files <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When set to false, files with name starting with a dot will be hidden in local directory listings.</dl>
<p> protocol.file.try_encoding_extensions <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When set, if we can&#8217;t open a file named &#8216;filename&#8217;, we&#8217;ll try to open &#8216;filename&#8217; with some encoding extension appended (ie. &#8216;filename.gz&#8217;); it depends on the supported encodings.</dl>
<h3>protocol.file.cgi (Local CGI)</h3>
<p>Local CGI specific options. </p>
<p> protocol.file.cgi.path <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Colon separated list of directories, where CGI scripts are stored.</dl>
<p> protocol.file.cgi.policy <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to execute local CGI scripts.</dl>
<h3>protocol.ftp (FTP)</h3>
<p>FTP specific options. </p>
<p> protocol.<a href="ftp://ftp.anon_passwd">ftp.anon_passwd</a> <code>&lt;str&gt;</code> (default: &quot;some [at] host.domain&quot;)</p>
<dl>
<dd>FTP anonymous password to be sent.</dl>
<p> protocol.<a href="ftp://ftp.use_pasv">ftp.use_pasv</a> <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Use PASV instead of PORT (passive vs active mode, IPv4 only).</dl>
<p> protocol.<a href="ftp://ftp.use_epsv">ftp.use_epsv</a> <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Use EPSV instead of EPRT (passive vs active mode, IPv6 only).</dl>
<h3>protocol.<a href="ftp://ftp.proxy">ftp.proxy</a> (Proxy configuration)</h3>
<p>FTP proxy configuration. </p>
<p> protocol.<a href="ftp://ftp.proxy.host">ftp.proxy.host</a> <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Host and port-number (host:port) of the FTP proxy, or blank. If it&#8217;s blank, <code>FTP_PROXY</code> environment variable is checked as well.</dl>
<h3>protocol.http (HTTP)</h3>
<p>HTTP-specific options. </p>
<p> protocol.http.accept_language <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Send Accept-Language header.</dl>
<p> protocol.http.accept_ui_language <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Request localised versions of documents from web-servers (using the Accept-Language header) using the language you have configured for ELinks&#8217; user-interface (this also affects navigator.language ECMAScript value available to scripts). Note that some see this as a potential security risk because it tells web-masters and the FBI sniffers about your language preference.</dl>
<p> protocol.http.compression <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>If enabled, the capability to receive compressed content (gzip and/or bzip2) is announced to the server, which usually sends the reply compressed, thus saving some bandwidth at slight CPU expense. </p>
<p> If ELinks displays a incomplete page or garbage, try disabling this option. If that helps, there may be a bug in the decompression part of ELinks. Please report such bugs. </p>
<p> If ELinks has been compiled without compression support, this option has no effect. To check the supported features, see Help -&gt; About.</dl>
<p> protocol.http.trace <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>If active, all HTTP requests are sent with TRACE as their method rather than GET or POST. This is useful for debugging of both ELinks and various server-side scripts &#8212; the server only returns the client&#8217;s request back to the client verbatim. Note that this type of request may not be enabled on all servers.</dl>
<p> protocol.http.user_agent <code>&lt;str&gt;</code> (default: &quot;ELinks/%v (textmode; %s; %t-%b)&quot;)</p>
<dl>
<dd>Change the User Agent ID. That means identification string, which is sent to HTTP server when a document is requested. The &#8216;textmode&#8217; token in the first field is our silent attempt to establish this as a standard for new textmode user agents, so that the webmasters can have just a single uniform test for these if they are e.g. pushing some lite version to them automagically. </p>
<p> Use &quot; &quot; if you don&#8217;t want any User-Agent header to be sent at all. </p>
<dl>
<dd>&bull;%v in the string means ELinks version,</dl>
<dl>
<dd>&bull;%s in the string means system identification,</dl>
<dl>
<dd>&bull;%t in the string means size of the terminal,</dl>
<dl>
<dd>&bull;%b in the string means number of bars displayed by ELinks.</dl>
</dl>
<h3>protocol.http.bugs (Server bug workarounds)</h3>
<p>Server-side HTTP bugs workarounds. </p>
<p> protocol.http.bugs.accept_charset <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>The Accept-Charset header is quite long and sending it can trigger bugs in some rarely found servers.</dl>
<p> protocol.http.bugs.allow_blacklist <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Allow blacklisting of buggy servers.</dl>
<p> protocol.http.bugs.broken_302_redirect <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Broken 302 redirect (violates RFC but compatible with Netscape). This is a problem for a lot of web discussion boards and the like. If they will do strange things to you, try to play with this.</dl>
<p> protocol.http.bugs.post_no_keepalive <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Disable keepalive connection after POST request.</dl>
<p> protocol.http.bugs.http10 <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Use HTTP/1.0 protocol instead of HTTP/1.1.</dl>
<h3>protocol.http.proxy (Proxy configuration)</h3>
<p>HTTP proxy configuration. </p>
<p> protocol.http.proxy.host <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Host and port-number (host:port) of the HTTP proxy, or blank. If it&#8217;s blank, <code>HTTP_PROXY</code> environment variable is checked as well.</dl>
<p> protocol.http.proxy.user <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Proxy authentication username.</dl>
<p> protocol.http.proxy.passwd <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Proxy authentication password.</dl>
<h3>protocol.http.referer (Referer sending)</h3>
<p>HTTP referer sending options. HTTP referer is a special header sent in the HTTP requests, which is supposed to contain the previous page visited by the browser.This way, the server can know what link did you follow when accessing that page. However, this behaviour can unfortunately considerably affect privacy and can lead even to a security problem on some badly designed web pages. </p>
<p> protocol.http.referer.policy <code>&lt;num&gt;</code> (default: 3)</p>
<dl>
<dd>Mode of sending HTTP referer: </p>
<dl>
<dd>&bull;0 is send no referer</dl>
<dl>
<dd>&bull;1 is send current URL as referer</dl>
<dl>
<dd>&bull;2 is send fixed fake referer</dl>
<dl>
<dd>&bull;3 is send previous URL as referer (correct, but insecure)</dl>
</dl>
<p> protocol.http.referer.fake <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Fake referer to be sent when policy is 2.</dl>
<h3>protocol.https (HTTPS)</h3>
<p>HTTPS-specific options.</p>
<h3>protocol.https.proxy (Proxy configuration)</h3>
<p>HTTPS proxy configuration. </p>
<p> protocol.https.proxy.host <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Host and port-number (host:port) of the HTTPS CONNECT proxy, or blank. If it&#8217;s blank, <code>HTTPS_PROXY</code> environment variable is checked as well.</dl>
<h3>protocol.nntp (NNTP)</h3>
<p>NNTP and news specific options. </p>
<p> protocol.nntp.server <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Used when resolving news: URIs. If set to the empty string the value of the <code>NNTPSERVER</code> environment variable will be used.</dl>
<p> protocol.nntp.header_entries <code>&lt;str&gt;</code> (default: &quot;Subject,From,Date,Message-ID,Newsgroups&quot;)</p>
<dl>
<dd>Comma separated list of which entries in the article header to show. E.g. &#8216;Subject&#8217; and &#8216;From&#8217;. All header entries can be read in the header info dialog.</dl>
<h3>protocol.rewrite (URI rewriting)</h3>
<p>Rules for rewriting URIs entered in the goto dialog. It makes it possible to define a set of prefixes that will be expanded if they match a string entered in the goto dialog. The prefixes can be dumb, meaning that they work only like URI abbreviations, or smart ones, making it possible to pass arguments to them like search engine keywords. </p>
<p> protocol.rewrite.default_template <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Default URI template used when the string entered in the goto dialog does not appear to be a URI or a filename (i.e. contains no &#8216;.&#8217;, &#8216;:&#8217; or &#8216;/&#8217; characters), and does not match any defined prefixes. Set the value to &quot;&quot; to disable use of the default template rewrite rule. </p>
<dl>
<dd>&bull;%c in the template means the current URL,</dl>
<dl>
<dd>&bull;%s in the template means the whole string from the goto dialog,</dl>
<dl>
<dd>&bull;%0,%1,&#8230;,%9 mean the 1st,2nd,&#8230;,10th space-delimited part of %s,</dl>
<dl>
<dd>&bull;%% in the template means &#8216;%&#8217;.</dl>
</dl>
<p> protocol.rewrite.enable-dumb <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Enable dumb prefixes &#8211; simple URI abbreviations which can be written to the Goto URL dialog instead of actual URIs &#8211; i.e. if you write &#8216;elinks&#8217; there, you are directed to <i><a rel="nofollow" href="http://elinks.cz/">http://elinks.cz/</a></i>.</dl>
<p> protocol.rewrite.enable-smart <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Enable smart prefixes &#8211; URI templates triggered by writing given abbreviation to the Goto URL dialog followed by a list of arguments from which the actual URI is composed &#8211; i.e. &#8216;gg:search keywords&#8217; or &#8216;gn search keywords for news&#8217;.</dl>
<h3>protocol.rewrite.dumb (Dumb Prefixes)</h3>
<p>Dumb prefixes, see enable-dumb description for details. </p>
<p> protocol.rewrite.dumb._template_ <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Replacement URI for this dumbprefix: </p>
<dl>
<dd>&bull;%c in the string means the current URL</dl>
<dl>
<dd>&bull;%% in the string means &#8216;%&#8217;</dl>
</dl>
<h3>protocol.rewrite.smart (Smart Prefixes)</h3>
<p>Smart prefixes, see enable-smart description for details. </p>
<p> protocol.rewrite.smart._template_ <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Replacement URI for this smartprefix: </p>
<dl>
<dd>&bull;%c in the string means the current URL</dl>
<dl>
<dd>&bull;%s in the string means the whole argument to smartprefix</dl>
<dl>
<dd>&bull;%0,%1,&#8230;,%9 means argument 0, 1, &#8230;, 9</dl>
<dl>
<dd>&bull;%% in the string means &#8216;%&#8217;</dl>
</dl>
<h3>protocol.user (User protocols)</h3>
<p>User protocols. Options in this tree specify external handlers for the appropriate protocols. Ie. protocol.user.mailto.unix.</p>
<h3>protocol.user._template_ (Template option folder)</h3>
<p>Handler (external program) for this protocol. Name the options in this tree after your system (ie. unix, unix-xwin). </p>
<p> protocol.user._template_._template_ <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Handler (external program) for this protocol and system. </p>
<dl>
<dd>&bull;%f in the string means file name to include form data from</dl>
<dl>
<dd>&bull;%h in the string means hostname (or email address)</dl>
<dl>
<dd>&bull;%p in the string means port</dl>
<dl>
<dd>&bull;%d in the string means path (everything after the port)</dl>
<dl>
<dd>&bull;%s in the string means subject (?subject=&lt;this&gt;)</dl>
<dl>
<dd>&bull;%u in the string means the whole URL</dl>
</dl>
<h3>terminal (Terminals)</h3>
<p>Terminal options.</p>
<h3>terminal._template_ (Template option folder)</h3>
<p>Options specific to this terminal type (according to <code>$TERM</code> value). </p>
<p> terminal._template_.type <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Terminal type; matters mostly only when drawing frames and dialog box borders: </p>
<dl>
<dd>&bull;0 is dumb terminal type, ASCII art</dl>
<dl>
<dd>&bull;1 is VT100, simple but portable</dl>
<dl>
<dd>&bull;2 is Linux, you get double frames and other goodies</dl>
<dl>
<dd>&bull;3 is KOI-8</dl>
<dl>
<dd>&bull;4 is FreeBSD</dl>
<dl>
<dd>&bull;5 is fbterm</dl>
</dl>
<p> terminal._template_.latin1_title <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When updating the window title of <code>xterm</code> or a similar terminal emulator, encode the title in ISO-8859-1 (Latin-1), rather than in the charset used for other text in the window. Cyrillic and other characters get replaced with Latin ones. Xterm requires this unless you explicitly enable UTF-8 titles in it. </p>
<p> If this option does not take effect immediately, try switching to a different page so that ELinks notices it needs to update the title.</dl>
<p> terminal._template_.m11_hack <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Switch fonts when drawing lines, enabling both local characters and lines working at the same time. ELinks uses this option only if UTF-8 I/O is disabled and the terminal type is Linux or FreeBSD.</dl>
<p> terminal._template_.utf_8_io <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Enable I/O in UTF-8 for Unicode terminals. Note that currently, only the subset of UTF-8 according to terminal codepage is used. ELinks ignores this option if the terminal codepage is UTF-8.</dl>
<p> terminal._template_.combine <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Enable combining characters. It works only with the <code>xterm</code> in UTF-8 mode.</dl>
<p> terminal._template_.restrict_852 <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Restrict the characters used when drawing lines. Makes sense only with linux terminals using the cp850/852 character sets.</dl>
<p> terminal._template_.block_cursor <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Move cursor to bottom right corner when done drawing. This is particularly useful when we have a block cursor, so that inversed text is displayed correctly.</dl>
<p> terminal._template_.colors <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>The color mode controls what colors are used and how they are output to the terminal. </p>
<p> Some modes may have been disabled at compile time. The Setup -&gt; Terminal options dialog lists the modes supported by this executable. If you select an unsupported mode, ELinks uses 16 colors. </p>
<p> The color modes are: </p>
<dl>
<dd>&bull;0 is mono mode, only 2 colors are used</dl>
<dl>
<dd>&bull;1 is 16 color mode, uses the common ANSI colors</dl>
<dl>
<dd>&bull;2 is 88 color mode, uses XTerm RGB codes</dl>
<dl>
<dd>&bull;3 is 256 color mode, uses XTerm RGB codes</dl>
<dl>
<dd>&bull;4 is true color mode, uses konsole RGB codes</dl>
</dl>
<p> terminal._template_.transparency <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>If we should not set the background to black. This is particularly useful when we have a terminal (typically in some windowing environment) with a background image or a transparent background &#8211; it will be visible in ELinks as well (but ELinks document color handling will still assume the background is black so if you have a bright background you might experience contrast problems). Note that this option makes sense only when colors are enabled.</dl>
<p> terminal._template_.italic <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>If we should use italics.</dl>
<p> terminal._template_.underline <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>If we should use underline or enhance the color instead.</dl>
<p> terminal._template_.charset <code>&lt;codepage&gt;</code> (default: System)</p>
<dl>
<dd>Codepage of charset used for displaying content on terminal. &#8216;System&#8217; stands for a codepage determined by a selected locale.</dl>
<h3>ui (User interface)</h3>
<p>User interface options. </p>
<p> ui.date_format <code>&lt;str&gt;</code> (default: &quot;%b %e %H:%M&quot;)</p>
<dl>
<dd>Date format to use in dialogs. See <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3).</dl>
<p> ui.language <code>&lt;language&gt;</code> (default: &quot;System&quot;)</p>
<dl>
<dd>Language of user interface. &#8216;System&#8217; means that the language will be extracted from the environment dynamically.</dl>
<p> ui.show_menu_bar_always <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Always show menu bar on the screen.</dl>
<p> ui.show_status_bar <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Show status bar on the screen.</dl>
<p> ui.show_title_bar <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Show title bar on the screen.</dl>
<p> ui.startup_goto_dialog <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Pop up goto dialog in newly created tabs when there&#8217;s no homepage set. This means also showing goto dialog on startup.</dl>
<p> ui.success_msgbox <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When you pressed a Save button in some manager, this option will make sure that a box confirming success of the operation will pop up.</dl>
<p> ui.window_title <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>Set the window title when running in a windowing environment in an <code>xterm</code>-like terminal. This way the document&#8217;s title is shown on the window titlebar.</dl>
<h3>ui.clock (Clock)</h3>
<p>Digital clock in the status bar. </p>
<p> ui.clock.enable <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to display a digital clock in the status bar.</dl>
<p> ui.clock.format <code>&lt;str&gt;</code> (default: &quot;[%H:%M]&quot;)</p>
<dl>
<dd>Format string for the digital clock. See the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) manpage for details.</dl>
<h3>ui.colors (Color settings)</h3>
<p>Default user interface color settings.</p>
<h3>ui.colors.color (Color terminals)</h3>
<p>Color settings for color terminal.</p>
<h3>ui.colors.color.mainmenu (Main menu bar)</h3>
<p>Main menu bar colors.</p>
<h3>ui.colors.color.mainmenu.normal (Unselected main menu bar item)</h3>
<p>Unselected main menu bar item colors. </p>
<p> ui.colors.color.mainmenu.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.mainmenu.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.mainmenu.selected (Selected main menu bar item)</h3>
<p>Selected main menu bar item colors. </p>
<p> ui.colors.color.mainmenu.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.mainmenu.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.mainmenu.hotkey (Hotkey)</h3>
<p>Main menu hotkey colors.</p>
<h3>ui.colors.color.mainmenu.hotkey.normal (Unselected hotkey)</h3>
<p>Main menu unselected hotkey colors. </p>
<p> ui.colors.color.mainmenu.hotkey.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: darkred)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.mainmenu.hotkey.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.mainmenu.hotkey.selected (Selected hotkey)</h3>
<p>Main menu selected hotkey colors. </p>
<p> ui.colors.color.mainmenu.hotkey.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: darkred)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.mainmenu.hotkey.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.menu (Menu bar)</h3>
<p>Menu bar colors.</p>
<h3>ui.colors.color.menu.normal (Unselected menu item)</h3>
<p>Unselected menu item colors. </p>
<p> ui.colors.color.menu.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.menu.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.menu.selected (Selected menu item)</h3>
<p>Selected menu item colors. </p>
<p> ui.colors.color.menu.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.menu.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.menu.marked (Marked menu item)</h3>
<p>Marked menu item colors. </p>
<p> ui.colors.color.menu.marked.text <code>&lt;color|#rrggbb&gt;</code> (default: red)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.menu.marked.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.menu.hotkey (Hotkey)</h3>
<p>Menu item hotkey colors.</p>
<h3>ui.colors.color.menu.hotkey.normal (Unselected hotkey)</h3>
<p>Menu item unselected hotkey colors. </p>
<p> ui.colors.color.menu.hotkey.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: darkred)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.menu.hotkey.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.menu.hotkey.selected (Selected hotkey)</h3>
<p>Menu item selected hotkey colors. </p>
<p> ui.colors.color.menu.hotkey.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: darkred)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.menu.hotkey.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.menu.frame (Menu frame)</h3>
<p>Menu frame colors. </p>
<p> ui.colors.color.menu.frame.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.menu.frame.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog (Dialog)</h3>
<p>Dialog colors.</p>
<h3>ui.colors.color.dialog.generic (Generic)</h3>
<p>Generic dialog colors. </p>
<p> ui.colors.color.dialog.generic.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.generic.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.frame (Frame)</h3>
<p>Dialog frame colors. </p>
<p> ui.colors.color.dialog.frame.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.frame.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.scrollbar (Scrollbar)</h3>
<p>Scrollbar colors. </p>
<p> ui.colors.color.dialog.scrollbar.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.scrollbar.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.scrollbar-selected (Selected scrollbar)</h3>
<p>Scrollbar selected colors. </p>
<p> ui.colors.color.dialog.scrollbar-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.scrollbar-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.title (Title)</h3>
<p>Dialog title colors. </p>
<p> ui.colors.color.dialog.title.text <code>&lt;color|#rrggbb&gt;</code> (default: darkred)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.title.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.text (Text)</h3>
<p>Dialog text colors. </p>
<p> ui.colors.color.dialog.text.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.text.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.checkbox (Checkbox)</h3>
<p>Dialog checkbox colors. </p>
<p> ui.colors.color.dialog.checkbox.text <code>&lt;color|#rrggbb&gt;</code> (default: darkred)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.checkbox.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.checkbox-selected (Selected checkbox)</h3>
<p>Dialog selected checkbox colors. </p>
<p> ui.colors.color.dialog.checkbox-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: yellow)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.checkbox-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.checkbox-label (Checkbox label)</h3>
<p>Dialog checkbox label colors. </p>
<p> ui.colors.color.dialog.checkbox-label.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.checkbox-label.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.button (Button)</h3>
<p>Dialog button colors. </p>
<p> ui.colors.color.dialog.button.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.button.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.button-selected (Selected button)</h3>
<p>Dialog selected button colors. </p>
<p> ui.colors.color.dialog.button-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: yellow)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.button-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.button-shortcut (Button shortcut)</h3>
<p>Dialog button colors. </p>
<p> ui.colors.color.dialog.button-shortcut.text <code>&lt;color|#rrggbb&gt;</code> (default: yellow)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.button-shortcut.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.button-shortcut-selected (Selected button shortcut)</h3>
<p>Dialog selected button colors. </p>
<p> ui.colors.color.dialog.button-shortcut-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.button-shortcut-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.field (Text field)</h3>
<p>Dialog text field colors. </p>
<p> ui.colors.color.dialog.field.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.field.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.field-text (Text field text)</h3>
<p>Dialog field text colors. </p>
<p> ui.colors.color.dialog.field-text.text <code>&lt;color|#rrggbb&gt;</code> (default: yellow)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.field-text.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.meter (Meter)</h3>
<p>Dialog meter colors. </p>
<p> ui.colors.color.dialog.meter.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.meter.background <code>&lt;color|#rrggbb&gt;</code> (default: blue)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.dialog.shadow (Shadow)</h3>
<p>Dialog shadow colors (see ui.shadows option). </p>
<p> ui.colors.color.dialog.shadow.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.dialog.shadow.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.title (Title bar)</h3>
<p>Title bar colors.</p>
<h3>ui.colors.color.title.title-bar (Generic title bar)</h3>
<p>Generic title bar colors. </p>
<p> ui.colors.color.title.title-bar.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.title.title-bar.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.title.title-text (Title bar text)</h3>
<p>Title bar text colors. </p>
<p> ui.colors.color.title.title-text.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.title.title-text.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.status (Status bar)</h3>
<p>Status bar colors.</p>
<h3>ui.colors.color.status.status-bar (Generic status bar)</h3>
<p>Generic status bar colors. </p>
<p> ui.colors.color.status.status-bar.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.status.status-bar.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.status.status-text (Status bar text)</h3>
<p>Status bar text colors. </p>
<p> ui.colors.color.status.status-text.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.status.status-text.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.tabs (Tabs bar)</h3>
<p>Tabs bar colors.</p>
<h3>ui.colors.color.tabs.unvisited (Unvisited tab)</h3>
<p>Tab colors for tabs that have not been selected since they completed loading. </p>
<p> ui.colors.color.tabs.unvisited.text <code>&lt;color|#rrggbb&gt;</code> (default: darkblue)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.tabs.unvisited.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.tabs.normal (Unselected tab)</h3>
<p>Unselected tab colors. </p>
<p> ui.colors.color.tabs.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.tabs.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.tabs.loading (Loading tab)</h3>
<p>Tab colors for tabs that are loading in the background. </p>
<p> ui.colors.color.tabs.loading.text <code>&lt;color|#rrggbb&gt;</code> (default: darkred)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.tabs.loading.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.tabs.selected (Selected tab)</h3>
<p>Selected tab colors. </p>
<p> ui.colors.color.tabs.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.tabs.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: green)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.tabs.separator (Tab separator)</h3>
<p>Tab separator colors. </p>
<p> ui.colors.color.tabs.separator.text <code>&lt;color|#rrggbb&gt;</code> (default: brown)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.tabs.separator.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.color.searched (Searched strings)</h3>
<p>Searched string highlight colors. </p>
<p> ui.colors.color.searched.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.color.searched.background <code>&lt;color|#rrggbb&gt;</code> (default: lime)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono (Non-color terminals)</h3>
<p>Color settings for non-color terminal.</p>
<h3>ui.colors.mono.mainmenu (Main menu bar)</h3>
<p>Main menu bar colors.</p>
<h3>ui.colors.mono.mainmenu.normal (Unselected main menu bar item)</h3>
<p>Unselected main menu bar item colors. </p>
<p> ui.colors.mono.mainmenu.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.mainmenu.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.mainmenu.selected (Selected main menu bar item)</h3>
<p>Selected main menu bar item colors. </p>
<p> ui.colors.mono.mainmenu.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.mainmenu.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.mainmenu.hotkey (Hotkey)</h3>
<p>Main menu hotkey colors.</p>
<h3>ui.colors.mono.mainmenu.hotkey.normal (Unselected hotkey)</h3>
<p>Main menu unselected hotkey colors. </p>
<p> ui.colors.mono.mainmenu.hotkey.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.mainmenu.hotkey.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.mainmenu.hotkey.selected (Selected hotkey)</h3>
<p>Main menu selected hotkey colors. </p>
<p> ui.colors.mono.mainmenu.hotkey.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.mainmenu.hotkey.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.menu (Menu bar)</h3>
<p>Menu bar colors.</p>
<h3>ui.colors.mono.menu.normal (Unselected menu item)</h3>
<p>Unselected menu item colors. </p>
<p> ui.colors.mono.menu.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.menu.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.menu.selected (Selected menu item)</h3>
<p>Selected menu item colors. </p>
<p> ui.colors.mono.menu.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.menu.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.menu.marked (Marked menu item)</h3>
<p>Marked menu item colors. </p>
<p> ui.colors.mono.menu.marked.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.menu.marked.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.menu.hotkey (Hotkey)</h3>
<p>Menu item hotkey colors.</p>
<h3>ui.colors.mono.menu.hotkey.normal (Unselected hotkey)</h3>
<p>Menu item unselected hotkey colors. </p>
<p> ui.colors.mono.menu.hotkey.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.menu.hotkey.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.menu.hotkey.selected (Selected hotkey)</h3>
<p>Menu item selected hotkey colors. </p>
<p> ui.colors.mono.menu.hotkey.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.menu.hotkey.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.menu.frame (Menu frame)</h3>
<p>Menu frame colors. </p>
<p> ui.colors.mono.menu.frame.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.menu.frame.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog (Dialog)</h3>
<p>Dialog colors.</p>
<h3>ui.colors.mono.dialog.generic (Generic)</h3>
<p>Generic dialog colors. </p>
<p> ui.colors.mono.dialog.generic.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.generic.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.frame (Frame)</h3>
<p>Dialog frame colors. </p>
<p> ui.colors.mono.dialog.frame.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.frame.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.scrollbar (Scrollbar)</h3>
<p>Scrollbar colors. </p>
<p> ui.colors.mono.dialog.scrollbar.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.scrollbar.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.scrollbar-selected (Selected scrollbar)</h3>
<p>Scrollbar selected colors. </p>
<p> ui.colors.mono.dialog.scrollbar-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.scrollbar-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.title (Title)</h3>
<p>Dialog title colors. </p>
<p> ui.colors.mono.dialog.title.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.title.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.text (Text)</h3>
<p>Dialog text colors. </p>
<p> ui.colors.mono.dialog.text.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.text.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.checkbox (Checkbox)</h3>
<p>Dialog checkbox colors. </p>
<p> ui.colors.mono.dialog.checkbox.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.checkbox.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.checkbox-selected (Selected checkbox)</h3>
<p>Dialog selected checkbox colors. </p>
<p> ui.colors.mono.dialog.checkbox-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.checkbox-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.checkbox-label (Checkbox label)</h3>
<p>Dialog checkbox label colors. </p>
<p> ui.colors.mono.dialog.checkbox-label.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.checkbox-label.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.button (Button)</h3>
<p>Dialog button colors. </p>
<p> ui.colors.mono.dialog.button.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.button.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.button-selected (Selected button)</h3>
<p>Dialog selected button colors. </p>
<p> ui.colors.mono.dialog.button-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.button-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.button-shortcut (Button shortcut)</h3>
<p>Dialog button colors. </p>
<p> ui.colors.mono.dialog.button-shortcut.text <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.button-shortcut.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.button-shortcut-selected (Selected button shortcut)</h3>
<p>Dialog selected button colors. </p>
<p> ui.colors.mono.dialog.button-shortcut-selected.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.button-shortcut-selected.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.field (Text field)</h3>
<p>Dialog text field colors. </p>
<p> ui.colors.mono.dialog.field.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.field.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.field-text (Text field text)</h3>
<p>Dialog field text colors. </p>
<p> ui.colors.mono.dialog.field-text.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.field-text.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.meter (Meter)</h3>
<p>Dialog meter colors. </p>
<p> ui.colors.mono.dialog.meter.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.meter.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.dialog.shadow (Shadow)</h3>
<p>Dialog shadow colors (see ui.shadows option). </p>
<p> ui.colors.mono.dialog.shadow.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.dialog.shadow.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.title (Title bar)</h3>
<p>Title bar colors.</p>
<h3>ui.colors.mono.title.title-bar (Generic title bar)</h3>
<p>Generic title bar colors. </p>
<p> ui.colors.mono.title.title-bar.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.title.title-bar.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.title.title-text (Title bar text)</h3>
<p>Title bar text colors. </p>
<p> ui.colors.mono.title.title-text.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.title.title-text.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.status (Status bar)</h3>
<p>Status bar colors.</p>
<h3>ui.colors.mono.status.status-bar (Generic status bar)</h3>
<p>Generic status bar colors. </p>
<p> ui.colors.mono.status.status-bar.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.status.status-bar.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.status.status-text (Status bar text)</h3>
<p>Status bar text colors. </p>
<p> ui.colors.mono.status.status-text.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.status.status-text.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.tabs (Tabs bar)</h3>
<p>Tabs bar colors.</p>
<h3>ui.colors.mono.tabs.unvisited (Unvisited tab)</h3>
<p>Tab colors for tabs that have not been selected since they completed loading. </p>
<p> ui.colors.mono.tabs.unvisited.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.tabs.unvisited.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.tabs.normal (Unselected tab)</h3>
<p>Unselected tab colors. </p>
<p> ui.colors.mono.tabs.normal.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.tabs.normal.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.tabs.loading (Loading tab)</h3>
<p>Tab colors for tabs that are loading in the background. </p>
<p> ui.colors.mono.tabs.loading.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.tabs.loading.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.tabs.selected (Selected tab)</h3>
<p>Selected tab colors. </p>
<p> ui.colors.mono.tabs.selected.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.tabs.selected.background <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.tabs.separator (Tab separator)</h3>
<p>Tab separator colors. </p>
<p> ui.colors.mono.tabs.separator.text <code>&lt;color|#rrggbb&gt;</code> (default: gray)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.tabs.separator.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.colors.mono.searched (Searched strings)</h3>
<p>Searched string highlight colors. </p>
<p> ui.colors.mono.searched.text <code>&lt;color|#rrggbb&gt;</code> (default: black)</p>
<dl>
<dd>Default text color.</dl>
<p> ui.colors.mono.searched.background <code>&lt;color|#rrggbb&gt;</code> (default: white)</p>
<dl>
<dd>Default background color.</dl>
<h3>ui.dialogs (Dialog settings)</h3>
<p>Dialogs-specific appearance and behaviour settings. </p>
<p> ui.dialogs.listbox_min_height <code>&lt;num&gt;</code> (default: 10)</p>
<dl>
<dd>Minimal height of the listbox widget (used e.g. for bookmarks or global history).</dl>
<p> ui.dialogs.shadows <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Make dialogs drop shadows (the shadows are solid, you can adjust their color by ui.colors.*.dialog.shadow). You may also want to eliminate the wide borders by adjusting <i>setup.h</i>.</dl>
<p> ui.dialogs.underline_hotkeys <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to underline hotkeys in menus to make them more visible. Requires that underlining is enabled for the terminal.</dl>
<p> ui.dialogs.underline_button_shortcuts <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether to underline button shortcuts to make them more visible. Requires that underlining is enabled for the terminal.</dl>
<h3>ui.leds (LEDs)</h3>
<p>LEDs (visual indicators) options. </p>
<p> ui.leds.enable <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Enable LEDs. These visual indicators will inform you about various states.</dl>
<h3>ui.sessions (Sessions)</h3>
<p>Sessions settings. </p>
<p> ui.sessions.auto_restore <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Automatically restore the session at start. </p>
<p> This feature requires bookmark support.</dl>
<p> ui.sessions.auto_save <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Automatically save the session when quitting. </p>
<p> This feature requires bookmark support.</dl>
<p> ui.sessions.auto_save_foldername <code>&lt;str&gt;</code> (default: &quot;Auto saved session&quot;)</p>
<dl>
<dd>Name of the bookmarks folder used for auto saving and restoring session. The name has to be unique. Any folders with the same name will be deleted. </p>
<p> This only makes sense with bookmark support.</dl>
<p> ui.sessions.homepage <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>The URI to load either at startup time when no URI was given on the command line or when requested by the goto-url-home action. Set to &quot;&quot; if the environment variable <code>WWW_HOME</code> should be used as homepage URI instead.</dl>
<p> ui.sessions.keep_session_active <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Keep the session active even if the last terminal exits.</dl>
<p> ui.sessions.snapshot <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Automatically save a snapshot of all tabs periodically. This will periodically bookmark the tabs of each terminal in a separate folder for recovery after a crash. </p>
<p> This feature requires bookmark support.</dl>
<h3>ui.tabs (Window tabs)</h3>
<p>Window tabs settings. </p>
<p> ui.tabs.show_bar <code>&lt;num&gt;</code> (default: 1)</p>
<dl>
<dd>Show tabs bar on the screen: </p>
<dl>
<dd>&bull;0 means never</dl>
<dl>
<dd>&bull;1 means only if two or more tabs are open</dl>
<dl>
<dd>&bull;2 means always</dl>
</dl>
<p> ui.tabs.top <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>Whether display tab bar at top like other browsers do.</dl>
<p> ui.tabs.wraparound <code>[0|1]</code> (default: 1)</p>
<dl>
<dd>When moving right from the last tab, jump to the first one, and vice versa.</dl>
<p> ui.tabs.confirm_close <code>[0|1]</code> (default: 0)</p>
<dl>
<dd>When closing a tab show confirmation dialog.</dl>
<h3>ui.timer (Timer options)</h3>
<p>Timed action after certain interval of user inactivity. Someone can even find this useful, although you may not believe that. </p>
<p> ui.timer.enable <code>&lt;num&gt;</code> (default: 0)</p>
<dl>
<dd>Whether to enable the timer or not: </p>
<dl>
<dd>&bull;0 is don&#8217;t count down anything</dl>
<dl>
<dd>&bull;1 is count down, but don&#8217;t show the timer</dl>
<dl>
<dd>&bull;2 is count down and show the timer near LEDs</dl>
</dl>
<p> ui.timer.duration <code>&lt;num&gt;</code> (default: 86400)</p>
<dl>
<dd>Inactivity timeout in seconds. The maximum of one day should be enough for just everyone (TM).</dl>
<p> ui.timer.action <code>&lt;str&gt;</code> (default: &quot;&quot;)</p>
<dl>
<dd>Keybinding action to be triggered when timer reaches zero.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-elinks/">elinks</a></code>(1), <code><a href="/docs/linux/man/5-elinkskeys/">elinkskeys</a></code>(5) </p>
