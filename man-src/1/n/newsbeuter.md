---
title: "newsbeuter(1)"
name: "newsbeuter"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newsbeuter/"
---

<h2 class="name">NAME</h2>
 

 newsbeuter - an RSS feed reader for text terminals 

<h2>SYNOPSIS</h2>

 <i>newsbeuter</i> [-r] [-e] [-i opmlfile] [-u urlfile] [-c cachefile] [-C configfile] [-X] [-o] [-x &lt;command&gt; ...] [-h] 

<h2>DESCRIPTION</h2>

 <i>newsbeuter</i> is an RSS feed reader for text terminals. RSS is a number of widely-used XML formats to transmit, publish and syndicate articles, for example news or blog articles. Newsbeuter is designed to be used on text terminals on Unix or Unix-like systems such as Linux, BSD or Mac OS X. 

<h2>OPTIONS</h2>

 

 -h
<dl>
<dt>
<dd> Display help</dl>
 

 -r
<dl>
<dt>
<dd> Refresh feeds on start</dl>
 

 -e
<dl>
<dt>
<dd> Export feeds as OPML to stdout</dl>
 

 -X
<dl>
<dt>
<dd> Clean up cache thoroughly (i.e. reduce it in size if possible)</dl>
 

 -v, -V
<dl>
<dt>
<dd> Get version information about newsbeuter and the libraries it uses</dl>
 

 -i opmlfile
<dl>
<dt>
<dd> Import an OPML file</dl>
 

 -u urlfile
<dl>
<dt>
<dd> Use an alternative URL file</dl>
 

 -c cachefile
<dl>
<dt>
<dd> Use an alternative cache file</dl>
 

 -C configfile
<dl>
<dt>
<dd> Use an alternative configuration file</dl>
 

 -x command ...
<dl>
<dt>
<dd> Execute one or more commands to run newsbeuter unattended. Currently available commands are &quot;reload&quot; and &quot;print-unread&quot;.</dl>
 

 -o
<dl>
<dt>
<dd> Active offline reading mode. When bloglines synchronization mode is configured, then the list of feeds will not be loaded from bloglines.com, but instead from the local cache. This makes it possible to read locally cached articles even without internet connection to connect to the bloglines server.</dl>
 

 -l loglevel
<dl>
<dt>
<dd> Generate a loglevel with a certain loglevel. Valid loglevels are 1 to 6. An actual logfile will only be written when you provide a logfile name.</dl>
 

 -d logfile
<dl>
<dt>
<dd> Use this logfile as output when logging debug messages. Please note that this only works when providing a loglevel.</dl>
 

 -E file
<dl>
<dt>
<dd> Export a list of read articles (resp. their GUIDs). This can be used to transfer information about read articles between different computers.</dl>
 

 -I file
<dl>
<dt>
<dd> Import a list of read articles and mark them as read if they are held in the cache. This is to be used in conjunction with the -E commandline parameter.</dl>

<h2>FIRST STEPS</h2>

 After you've installed newsbeuter, you can run it for the first time by typing &quot;newsbeuter&quot; on your command prompt. This will bring you the following message: 

 

<dl>
<dt>
<dd> <pre>
Error: no URLs configured. Please fill the file /home/ak/.newsbeuter/urls with RSS feed URLs or import an OPML file.
</pre></dl>
 

<dl>
<dt>
<dd> <pre><code>
newsbeuter 2.3 usage :./ newsbeuter[-i&lt;file&gt; | -e][-u&lt;urlfile&gt;][-c&lt;cachefile&gt;][-x&lt;command&gt;...][-h] - e export OPML feed to stdout - r refresh feeds on start - i&lt;file&gt; import OPML file - u&lt;urlfile&gt; read RSS feed URLs from&lt;urlfile&gt; - c&lt;cachefile&gt; use&lt;cachefile&gt; as cache file - C&lt;configfile&gt; read configuration from&lt;configfile&gt; - X clean up cache thoroughly - x&lt;command&gt;... execute list of commands - o activate offline mode(only applies to bloglines synchronization mode) - v get version information
    - l&lt;loglevel&gt; write a log with a certain loglevel(valid values : 1 to 6) - d&lt;logfile&gt; use&lt;logfile&gt; as output log file
    - E&lt;file&gt; export list of read articles to&lt;file&gt; - I&lt;file&gt; import list of read articles from&lt;file&gt; - h this help
</code></pre></dl>
 This means that newsbeuter can't start without any configured feeds. To add feeds to newsbeuter, you can either add URLs to the configuration file $HOME/.newsbeuter/urls or you can import an OPML file by running &quot;newsbeuter -i blogroll.opml&quot;. To manually add URLs, open the file with your favorite text editor and add the URLs, one per line: 

 

<dl>
<dt>
<dd> <pre>
<a rel="nofollow" HREF="http://rss.cnn.com/rss/cnn_topstories.rss">http://rss.cnn.com/rss/cnn_topstories.rss</a>
<a rel="nofollow" HREF="http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml">http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml</a>
</pre></dl>
 If you need to add URLs that have restricted access via username/password, simply provide the username/password in the following way: 

 

<dl>
<dt>
<dd> <pre>
<a rel="nofollow" HREF="http://username:password@hostname.domain.tld/feed.rss">http://username:password@hostname.domain.tld/feed.rss</a>
</pre></dl>
 In order to protect username and password, make sure that $HOME/.newsbeuter/urls has the appropriate permissions. Newsbeuter also makes sure that usernames and passwords within URLs aren't displayed in its user interface. In case there is a <i>@</i> in the username, you need to write it as <i>%40</i> instead so that it can be distinguished from the <i>@</i> that separates the username/password part from the hostname part. 

 You can also configure local files as feeds, by prefixing the local path with &quot;file://&quot; and adding it to the $HOME/.newsbeuter/urls file: 

 

<dl>
<dt>
<dd> <pre>
file:///var/log/rss_eventlog.xml
</pre></dl>
 Now you can run newsbeuter again, and it will present you with a controllable list of the URLs that you configured previously. You can now start downloading the feeds, either by pressing &quot;R&quot; to download all feeds, or by pressing &quot;r&quot; to download the currently selected feed. You can then select a feed you want to read, and by pressing &quot;Enter&quot;, you can go to the article list for this feed. This works even while the downloading is still in progress. You can now see the list of available articles by their title. A &quot;N&quot; on the left indicates that an article wasn't read yet. Pressing Enter brings you to the content of the article. You can scroll through this text, and also run a browser (default: lynx) to view the complete article if the content is empty or just an abstract or a short description. Pressing &quot;q&quot; brings you back to the article list, and pressing &quot;q&quot; again brings you back to the feed list. Pressing &quot;q&quot; a third time then closes newsbeuter. 

 Newsbeuter caches the article that it downloads. This means that when you start newsbeuter again and reload a feed, the old articles can still be read even if they aren't in the current RSS feeds anymore. Optionally you can configure how many articles shall be preserved by feed so that the article backlog doesn't grow endlessly (see &quot;max-items&quot; below). 

 Newsbeuter also uses a number of measures to preserve the users' and feed providers' bandwidth, by trying to avoid unnecessary feed downloads through the use of conditional HTTP downloading. It saves every feed's &quot;Last-Modified&quot; and &quot;ETag&quot; response header values (if present) and advises the feed's HTTP server to only send data if the feed has been updated by modification date/time or &quot;ETag&quot; header. This doesn't only make feed downloads for RSS feeds with no new updates faster, it also reduces the amount of transferred data per request. Conditional HTTP downloading can be optionally disabled per feed by using the &quot;always-download&quot; configuration command. 

 Several aspects of newsbeuter's behaviour can be configured via a configuration file, by default $HOME/.newsbeuter/config. This configuration file contains lines in the form &quot;&lt;config-command&gt; &lt;arg1&gt; ...&quot;. The configuration file can also contain comments, which start with the <i>#</i> character and go as far as the end of line. If you need to enter a configuration argument that contains spaces, use quotes (&quot;) around the whole argument. It's even possible to integrate the output of external commands into the configuration. The text between two backticks (&quot;`&quot;) is evaluated as shell command, and its output is put on its place instead. This works like backtick evaluation in Bourne-compatible shells and allows users to use external information from the system within the configuration. 

 Searching for articles is possible in newsbeuter, too. Just press the &quot;/&quot; key, enter your search phrase, and the title and content of all articles are searched for it. When you do a search from the list of feeds, all articles of all feeds will be searched. When you do a search from the article list of a feed, only the articles of the currently viewed feed are searched. When opening an article from a search result dialog, the search phrase is highlighted. 

 The history of all your searches is saved to the filesystem, to ~/.newsbeuter/history.search. By default, the last 100 search phrases are stored, but this limited can be influenced through the &quot;history-limit&quot; configuration variable. To disable search history saving, simply set the history-limit to 0. 

<h2>CONFIGURATION COMMANDS</h2>

 

 <i>always-display-description</i> (parameters: [true/false]; default value: <i>false</i>)
<dl>
<dt>
<dd> If true, then the description will always displayed even if e.g. a content:encoded tag has been found. (example: always-display-description true)</dl>
 

 <i>always-download</i> (parameters: &lt;rssurl&gt; [&lt;rssurl&gt;]; default value: <i>n/a</i>)
<dl>
<dt>
<dd> The parameters of this configuration command are one or more RSS URLs. These URLs will always get downloaded, regardless of their Last-Modified timestamp and ETag header. (example: always-download &quot;<a rel="nofollow" HREF="http://www.n-tv.de/23.rss">http://www.n-tv.de/23.rss</a>&quot;)</dl>
 

 <i>article-sort-order</i> (parameters: &lt;sortfield&gt;[-&lt;direction&gt;]; default value: <i>date</i>)
<dl>
<dt>
<dd> The sortfield specifies which article property shall be used for sorting (currently available: date, title, flags, author, link, guid). The optional direction specifies the sort direction (&quot;asc&quot; specifies ascending sorting, &quot;desc&quot; specifies descending sorting. for date, &quot;desc&quot; is default, for all others, &quot;asc&quot; is default). (example: article-sort-order author-desc)</dl>
 

 <i>articlelist-format</i> (parameters: &lt;format&gt;; default value: <i>&quot;%4i %f %D %6L %?T?;%-17T; ?%t&quot;</i>)
<dl>
<dt>
<dd> This variable defines the format of entries in the article list. See the respective section in the documentation for more information on format strings (note that the semicolon should actually be a vertical bar; this is a limitation in AsciiDoc). (example: articlelist-format &quot;%4i %f %D %?T?;%-17T; ?%t&quot;)</dl>
 

 <i>auto-reload</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If enabled, all feeds will be automatically reloaded at start up and then continuously after a certain time has passed (see reload-time). (example: auto-reload yes)</dl>
 

 <i>bind-key</i> (parameters: &lt;key&gt; &lt;operation&gt; [&lt;dialog&gt;]; default value: <i>n/a</i>)
<dl>
<dt>
<dd> Bind key &lt;key&gt; to &lt;operation&gt;. This means that whenever &lt;key&gt; is pressed, then &lt;operation&gt; is executed (if applicable in the current dialog). A list of available operations can be found below. Optionally, you can specify a dialog. If you specify one, the key binding will only be added to the specified dialog. Available dialogs are &quot;all&quot; (default if none is specified), &quot;feedlist&quot;, &quot;filebrowser&quot;, &quot;help&quot;, &quot;articlelist&quot;, &quot;article&quot;, &quot;tagselection&quot;, &quot;filterselection&quot;, &quot;urlview&quot; and &quot;podbeuter&quot;. (example: bind-key ^R reload-all)</dl>
 

 <i>bloglines-auth</i> (parameters: &lt;login&gt;:&lt;password&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> Set the Bloglines username and password. This is necessary for the Bloglines synchronization mode. (example: bloglines-auth &quot;username [at] emailaddress.com:mypassword&quot;)</dl>
 

 <i>bloglines-mark-read</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If set to yes, it will mark all articles that are downloaded from Bloglines as read. (example: bloglines-mark-read yes)</dl>
 

 <i>bookmark-cmd</i> (parameters: &lt;bookmark-command&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> If set, then &lt;bookmark-command&gt; will be used as bookmarking plugin. See the documentation on bookmarking for further information. (example: bookmark-cmd &quot;~/bin/delicious-bookmark.sh&quot;)</dl>
 

 <i>bookmark-interactive</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If set to yes, then the configured bookmark command is an interactive program. (example: bookmark-interactive yes)</dl>
 

 <i>browser</i> (parameters: &lt;browser-command&gt;; default value: <i>lynx</i>)
<dl>
<dt>
<dd> Set the browser command to use when opening an article in the browser. If &lt;browser-command&gt; contains %u, it will be used as complete commandline and %u will be replaced with the URL that shall be opened. (example: browser &quot;w3m %u&quot;)</dl>
 

 <i>cache-file</i> (parameters: &lt;path&gt;; default value: <i>&quot;~/.newsbeuter/cache.db&quot;</i>)
<dl>
<dt>
<dd> This configuration option sets the cache file. This is especially useful if the filesystem of your home directory doesn't support proper locking (e.g. NFS). (example: cache-file &quot;/tmp/testcache.db&quot;)</dl>
 

 <i>cleanup-on-quit</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If yes, then the cache gets locked and superfluous feeds and items are removed, such as feeds that can't be found in the urls configuration file anymore. (example: cleanup-on-quit no)</dl>
 

 <i>color</i> (parameters: &lt;element&gt; &lt;fgcolor&gt; &lt;bgcolor&gt; [&lt;attr&gt; ...]; default value: <i>n/a</i>)
<dl>
<dt>
<dd> Set the foreground color, background color and optional attributes for a certain element (example: color background white black)</dl>
 

 <i>confirm-exit</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If set to yes, then newsbeuter will ask for confirmation whether the user really wants to quit newsbeuter. (example: confirm-exit yes)</dl>
 

 <i>datetime-format</i> (parameters: &lt;date/time format&gt;; default value: <i>%b %d</i>)
<dl>
<dt>
<dd> This format specifies the date/time format in the article list. For a detailed documentation on the allowed formats, consult the manpage of <a HREF="/docs/linux/man/3-strftime/">strftime</a>(3). (example: datetime-format &quot;%D, %R&quot;)</dl>
 

 <i>define-filter</i> (parameters: &lt;name&gt; &lt;filter&gt;; default value: <i>n/a</i>)
<dl>
<dt>
<dd> With this command, you can predefine filters, which can you later select from a list, and which are then applied after selection. This is especially useful for filters that you need often and you don't want to enter them every time you need them. (example: define-filter &quot;all feeds with <i>fun</i> tag&quot; &quot;tags # \\&quot;fun\\&quot;&quot;)</dl>
 

 <i>display-article-progress</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If set to yes, then a read progress (in percent) is displayed in the article view. Otherwise, no read progress is displayed. (example: display-article-progress no)</dl>
 

 <i>download-retries</i> (parameters: &lt;number retries&gt;; default value: <i>1</i>)
<dl>
<dt>
<dd> How many times newsbeuter shall try to successfully download a feed before giving up. This is an option to improve the success of downloads on slow and shaky connections such as via a TOR proxy. (example: download-retries 4)</dl>
 

 <i>download-timeout</i> (parameters: &lt;seconds&gt;; default value: <i>30</i>)
<dl>
<dt>
<dd> The number of seconds newsbeuter shall wait when downloading a feed before giving up. This is an option to improve the success of downloads on slow and shaky connections such as via a TOR proxy. (example: download-timeout 60)</dl>
 

 <i>error-log</i> (parameters: &lt;path&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> If set, then user errors (e.g. errors regarding defunct RSS feeds) will be logged to this file. (example: error-log &quot;~/.newsbeuter/error.log&quot;)</dl>
 

 <i>feed-sort-order</i> (parameters: &lt;sortorder&gt;; default value: <i>none</i>)
<dl>
<dt>
<dd> If set to &quot;firsttag&quot;, the feeds in the feed list will be sorted by their first tag in the urls file. (example: feed-sort-order firsttag)</dl>
 

 <i>feedlist-format</i> (parameters: &lt;format&gt;; default value: <i>&quot;%4i %n %11u %t&quot;</i>)
<dl>
<dt>
<dd> This variable defines the format of entries in the feed list. See the respective section in the documentation for more information on format strings. (example: feedlist-format &quot; %n %4i - %11u -%&gt; %t&quot;)</dl>
 

 <i>googlereader-flag-share</i> (parameters: &lt;flag&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> If this is set and Google Reader support is used, then all articles that are flagged with the specified flag are being &quot;shared&quot; in Google Reader so that people that follow you can see it. (example: googlereader-flag-share &quot;a&quot;)</dl>
 

 <i>googlereader-flag-star</i> (parameters: &lt;flag&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> If this is set and Google Reader support is used, then all articles that are flagged with the specified flag are being &quot;starred&quot; in Google Reader and appear in the list of &quot;Starred items&quot;. (example: googlereader-flag-star &quot;b&quot;)</dl>
 

 <i>googlereader-login</i> (parameters: &lt;login&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> This variable sets your Google Reader login for the Google Reader support. (example: googlereader-login &quot;your-login&quot;)</dl>
 

 <i>googlereader-password</i> (parameters: &lt;password&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> This variable sets your Google Reader password for the Google Reader support. (example: google-password &quot;your-password&quot;)</dl>
 

 <i>googlereader-show-special-feeds</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If this is set, then &quot;special feeds&quot; like &quot;People you follow&quot; (articles shared by people you follow), &quot;Starred items&quot; (your starred articles), &quot;Shared items&quot; (your shared articles) and &quot;Popular items&quot; (articles considered to be popular by Google's magic algorithms) appear in your subscription list. (example: googlereader-show-special-feeds &quot;no&quot;)</dl>
 

 <i>goto-first-unread</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If set to yes (the default), then the first unread article will be selected whenever a feed is entered. (example: goto-first-unread no)</dl>
 

 <i>goto-next-feed</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If set to yes, then the next-unread and prev-unread keys will search in other feeds for unread articles if all articles in the current feed are read. If set to no, then the next-unread and prev-unread keys will stop in the current feed. (example: goto-next-feed no)</dl>
 

 <i>highlight</i> (parameters: &lt;target&gt; &lt;regex&gt; &lt;fgcolor&gt; [&lt;bgcolor&gt; [&lt;attribute&gt; ...]]; default value: <i>n/a</i>)
<dl>
<dt>
<dd> With this command, you can highlight text parts in the feed list, the article list and the article view. For a detailed documentation, see the chapter on highlighting. (example: highlight all &quot;newsbeuter&quot; red)</dl>
 

 <i>highlight-article</i> (parameters: &lt;filterexpr&gt; &lt;fgcolor&gt; &lt;bgcolor&gt; [&lt;attribute&gt; ...]; default value: <i>n/a</i>)
<dl>
<dt>
<dd> With this command, you can highlight articles in the article list if they match a filter expression. For a detailed documentation, see the chapter on highlighting. (example: highlight-article &quot;author =~ \\&quot;Andreas Krennmair\\&quot;&quot; white red bold)</dl>
 

 <i>history-limit</i> (parameters: &lt;number&gt;; default value: <i>100</i>)
<dl>
<dt>
<dd> Defines the maximum number of entries of commandline resp. search history to be saved. To disable history saving, set history-limit to 0. (example: history-limit 0)</dl>
 

 <i>html-renderer</i> (parameters: &lt;path&gt;; default value: <i>internal</i>)
<dl>
<dt>
<dd> If set to &quot;internal&quot;, then the internal HTML renderer will be used. Otherwise, the specified command will be executed, the HTML to be rendered will be written to the command's stdin, and the program's output will be displayed. This makes it possible to use other, external programs, such as w3m, links or lynx, to render HTML. (example: html-renderer &quot;w3m -dump -T text/html&quot;)</dl>
 

 <i>ignore-article</i> (parameters: &lt;feed&gt; &lt;filterexpr&gt;; default value: <i>n/a</i>)
<dl>
<dt>
<dd> If a downloaded article from &lt;feed&gt; matches &lt;filterexpr&gt;, then it is ignored and not presented to the user. This command is further explained in the &quot;kill file&quot; section below. (example: ignore-article &quot;*&quot; &quot;title =~ \\&quot;Windows\\&quot;&quot;)</dl>
 

 <i>ignore-mode</i> (parameters: [download/display]; default value: <i>download</i>)
<dl>
<dt>
<dd> This configuration option defines in what way an article is ignored (see ignore-article). If set to &quot;download&quot;, then it is ignored in the download/parsing phase (which is the default) and thus never written to the cache, if it set to &quot;display&quot;, it is ignored when displaying articles but is kept in the cache. (example: ignore-mode &quot;display&quot;)</dl>
 

 <i>include</i> (parameters: &lt;path&gt;; default value: <i>n/a</i>)
<dl>
<dt>
<dd> With this command, you can include other files to be interpreted as configuration files. This is especially useful to separate your configuration into several files, e.g. key configuration, color configuration, ... (example: include &quot;~/.newsbeuter/colors&quot;)</dl>
 

 <i>keep-articles-days</i> (parameters: &lt;days&gt;; default value: <i>0</i>)
<dl>
<dt>
<dd> If set the a number greater than 0, only articles that are were published within the last &lt;n&gt; days are kept, and older articles are deleted. If set to 0 (default value), this option is not active. (example: keep-articles-days 30)</dl>
 

 <i>macro</i> (parameters: &lt;macro key&gt; &lt;command list&gt;; default value: <i>n/a</i>)
<dl>
<dt>
<dd> With this command, you can define a macro key and specify a list of commands that shall be executed when the macro prefix and the macro key are pressed. (example: macro k open ; reload ; quit)</dl>
 

 <i>mark-as-read-on-hover</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If set to yes, then all articles that get selected in the article list are marked as read. (example: mark-as-read-on-hover yes)</dl>
 

 <i>max-items</i> (parameters: &lt;number&gt;; default value: <i>0</i>)
<dl>
<dt>
<dd> Set the number of articles to maximally keep per feed. If the number is set to 0, then all articles are kept. (example: max-items 100)</dl>
 

 <i>notify-format</i> (parameters: &lt;string&gt;; default value: <i>&quot;newsbeuter: finished reload, %f unread feeds (%n unread articles total)&quot;</i>)
<dl>
<dt>
<dd> Format string that is used for formatting notifications. See the chapter on format strings for more information. (example: notify-format &quot;%d new articles (%n unread articles, %f unread feeds)&quot;)</dl>
 

 <i>notify-program</i> (parameters: &lt;path&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> If set, then the configured program will be executed if new articles arrived (through a reload) or if notify-always is true. The first parameter of the called program contains the notification message. (example: notify-program &quot;~/bin/my-notifier&quot;)</dl>
 

 <i>notify-always</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If no, notifications will only be made when there are new feeds or articles. If yes, notifications will be made regardless. (example: notify-always yes)</dl>
 

 <i>notify-screen</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then a &quot;privacy message&quot; will be sent to the terminal, containing a notification message about new articles. This is especially useful if you use terminal emulations such as GNU screen which implement privacy messages. (example: notify-screen yes)</dl>
 

 <i>notify-xterm</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then the xterm window title will be set to a notification message about new articles. (example: notify-xterm yes)</dl>
 

 <i>notify-beep</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then the speaker beep on new articles. (example: notify-beep yes)</dl>
 

 <i>opml-url</i> (parameters: &lt;url&gt; ...; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> If the OPML online subscription mode is enabled, then the list of feeds will be taken from the OPML file found on this location. Optionally, you can specify more than one URL. All the listed OPML URLs will then be taken into account when loading the feed list. (example: opml-url &quot;<a rel="nofollow" HREF="http://host.domain.tld/blogroll.opml">http://host.domain.tld/blogroll.opml</a>&quot; &quot;<a HREF="http://example.com/anotheropmlfile.opml">http://example.com/anotheropmlfile.opml</a>&quot;)</dl>
 

 <i>pager</i> (parameters: [&lt;path&gt;/internal]; default value: <i>internal</i>)
<dl>
<dt>
<dd> If set to &quot;internal&quot;, then the internal pager will be used. Otherwise, the article to be displayed will be rendered to be a temporary file and then displayed with the configured pager. If the pager path is set to an empty string, the content of the &quot;PAGER&quot; environment variable will be used. If the pager path contains a placeholder &quot;%f&quot;, it will be replaced with the temporary filename. (example: less %f)</dl>
 

 <i>podcast-auto-enqueue</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then all podcast URLs that are found in articles are added to the podcast download queue. See the respective section in the documentation for more information on podcast support in newsbeuter. (example: podcast-auto-enqueue yes)</dl>
 

 <i>prepopulate-query-feeds</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then all query feeds are prepopulated with articles on startup. (example: prepopulate-query-feeds yes)</dl>
 

 <i>proxy</i> (parameters: &lt;server:port&gt;; default value: <i>n/a</i>)
<dl>
<dt>
<dd> Set the proxy to use for downloading RSS feeds. (example: proxy localhost:3128)</dl>
 

 <i>proxy-auth</i> (parameters: &lt;auth&gt;; default value: <i>n/a</i>)
<dl>
<dt>
<dd> Set the proxy authentication string. (example: proxy-auth user:password)</dl>
 

 <i>proxy-type</i> (parameters: &lt;type&gt;; default value: <i>http</i>)
<dl>
<dt>
<dd> Set proxy type. Allowed values: http, socks4, socks4a, socks5. (example: proxy-type socks5)</dl>
 

 <i>refresh-on-startup</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then all feeds will be reloaded when newsbeuter starts up. This is equivalent to the -r commandline option. (example: refresh-on-startup yes)</dl>
 

 <i>reload-only-visible-feeds</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then manually reloading all feeds will only reload the currently visible feeds, e.g. if a filter or a tag is set. (example: reload-only-visible-feeds yes)</dl>
 

 <i>reload-time</i> (parameters: &lt;number&gt;; default value: <i>60</i>)
<dl>
<dt>
<dd> The number of minutes between automatic reloads. (example: reload-time 120)</dl>
 

 <i>reload-threads</i> (parameters: &lt;number&gt;; default value: <i>1</i>)
<dl>
<dt>
<dd> The number of parallel reload threads that shall be started when all feeds are reloaded. (example: reload-threads 3)</dl>
 

 <i>reset-unread-on-update</i> (parameters: &lt;url&gt; ...; default value: <i>n/a</i>)
<dl>
<dt>
<dd> With this configuration command, you can provide a list of RSS feed URLs for whose articles the unread flag will be reset if an article has been updated, i.e. its content has been changed. This is especially useful for RSS feeds where single articles are updated after publication, and you want to be notified of the updates. (example: reset-unread-on-update &quot;<a rel="nofollow" HREF="http://blog.fefe.de/rss.xml?html">http://blog.fefe.de/rss.xml?html</a>&quot;)</dl>
 

 <i>save-path</i> (parameters: &lt;path&gt;; default value: <i>~/</i>)
<dl>
<dt>
<dd> The default path where articles shall be saved to. If an invalid path is specified, the current directory is used. (example: save-path &quot;~/Saved Articles&quot;)</dl>
 

 <i>search-highlight-colors</i> (parameters: &lt;fgcolor&gt; &lt;bgcolor&gt; [&lt;attribute&gt; ...]; default value: <i>black yellow bold</i>)
<dl>
<dt>
<dd> This configuration command specifies the highlighting colors when searching for text from the article view. (example: search-highlight-colors white black bold)</dl>
 

 <i>show-keymap-hint</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If no, then the keymap hints on the bottom of screen will not be displayed. (example: show-keymap-hint no)</dl>
 

 <i>show-read-feeds</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If yes, then all feeds, including those without unread articles, are listed. If no, then only feeds with one or more unread articles are list. (example: show-read-feeds no)</dl>
 

 <i>show-read-articles</i> (parameters: [yes/no]; default value: <i>yes</i>)
<dl>
<dt>
<dd> If yes, then all articles of a feed are listed in the article list. If no, then only unread articles are listed. (example: show-read-articles no)</dl>
 

 <i>suppress-first-reload</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then the first automatic reload will be suppressed if auto-reload is set to yes. (example: suppress-first-reload yes)</dl>
 

 <i>text-width</i> (parameters: &lt;number&gt;; default value: <i>0</i>)
<dl>
<dt>
<dd> If set to a number greater than 0, then all HTML will be rendered to this maximum line length. If set to 0, the terminal width will be used. (example: text-width 72)</dl>
 

 <i>unbind-key</i> (parameters: &lt;key&gt; [&lt;dialog&gt;]; default value: <i>n/a</i>)
<dl>
<dt>
<dd> Unbind key &lt;key&gt;. This means that no operation is called when &lt;key&gt; is pressed. Optionally, you can specify a dialog (for a list of available dialogs, see &quot;bind-key&quot; above). If you specify one, the key binding will only be unbound for the specified dialog. (example: unbind-key R)</dl>
 

 <i>urls-source</i> (parameters: &lt;source&gt;; default value: <i>&quot;local&quot;</i>)
<dl>
<dt>
<dd> This configuration command sets the source where URLs shall be retrieved from. By default, this is ~/.newsbeuter/urls. Alternatively, you can set it to &quot;bloglines&quot;, which enables newsbeuter's Bloglines synchronization mode, to &quot;opml&quot;, which enables newsbeuter's OPML online subscription mode, or to &quot;googlereader&quot;, which enables newsbeuter's Google Reader support. In order to make Google Reader support work correctly, you also need to set googlereader-login and googlereader-password. (example: urls-source &quot;bloglines&quot;)</dl>
 

 <i>use-proxy</i> (parameters: [yes/no]; default value: <i>no</i>)
<dl>
<dt>
<dd> If yes, then the configured proxy will be used for downloading the RSS feeds. (example: use-proxy yes)</dl>
 

 <i>user-agent</i> (parameters: &lt;user agent string&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> If set to a non-zero-length string, this value will be used as HTTP User-Agent header for all HTTP requests. (example: user-agent &quot;Lynx/2.8.5rel.1 libwww-FM/2.14&quot;)</dl>

<h2>AVAILABLE OPERATIONS</h2>

 

 <i>open</i> (default key: <i>ENTER</i>)
<dl>
<dt>
<dd> Open the currently selected feed or article.</dl>
 

 <i>quit</i> (default key: <i>q</i>)
<dl>
<dt>
<dd> Quit the program or return to the previous dialog (depending on the context).</dl>
 

 <i>reload</i> (default key: <i>r</i>)
<dl>
<dt>
<dd> Reload the currently selected feed.</dl>
 

 <i>reload-all</i> (default key: <i>R</i>)
<dl>
<dt>
<dd> Reload all feeds.</dl>
 

 <i>mark-feed-read</i> (default key: <i>A</i>)
<dl>
<dt>
<dd> Mark all articles in the currently selected feed read.</dl>
 

 <i>mark-all-feeds-read</i> (default key: <i>C</i>)
<dl>
<dt>
<dd> Mark articles in all feeds read.</dl>
 

 <i>save</i> (default key: <i>s</i>)
<dl>
<dt>
<dd> Save the currently selected article to a file.</dl>
 

 <i>next-unread</i> (default key: <i>n</i>)
<dl>
<dt>
<dd> Jump to the next unread article.</dl>
 

 <i>prev-unread</i> (default key: <i>p</i>)
<dl>
<dt>
<dd> Jump to the previous unread article.</dl>
 

 <i>random-unread</i> (default key: <i>^K</i>)
<dl>
<dt>
<dd> Jump to a random unred article.</dl>
 

 <i>open-in-browser</i> (default key: <i>o</i>)
<dl>
<dt>
<dd> Opens the URL associated with the current article.</dl>
 

 <i>open-in-browser-and-mark-read</i> (default key: <i>O</i>)
<dl>
<dt>
<dd> Opens the URL associated with the current article and marks the article as read.</dl>
 

 <i>help</i> (default key: <i>?</i>)
<dl>
<dt>
<dd> Runs the help screen.</dl>
 

 <i>toggle-source-view</i> (default key: <i>^U</i>)
<dl>
<dt>
<dd> Toggles between the HTML view and the source view in the article view.</dl>
 

 <i>toggle-article-read</i> (default key: <i>N</i>)
<dl>
<dt>
<dd> Toggle the read flag for the currently selected article.</dl>
 

 <i>toggle-show-read-feeds</i> (default key: <i>l</i>)
<dl>
<dt>
<dd> Toggle whether read feeds should be shown in the feed list.</dl>
 

 <i>show-urls</i> (default key: <i>u</i>)
<dl>
<dt>
<dd> Show all URLs in the article in a list (similar to urlview).</dl>
 

 <i>clear-tag</i> (default key: <i>^T</i>)
<dl>
<dt>
<dd> Clear current tag.</dl>
 

 <i>set-tag</i> (default key: <i>t</i>)
<dl>
<dt>
<dd> Select tag.</dl>
 

 <i>open-search</i> (default key: <i>/</i>)
<dl>
<dt>
<dd> Opens the search dialog. When a search is done in the article list, then the search operation only applies to the articles of the current feed, otherwise to all articles.</dl>
 

 <i>goto-url</i> (default key: <i>#</i>)
<dl>
<dt>
<dd> Open the URL dialog and then opens specified URL.</dl>
 

 <i>enqueue</i> (default key: <i>e</i>)
<dl>
<dt>
<dd> Add the podcast download URL of the current article (if any is found) to the podcast download queue (see the respective section in the documentation for more information on podcast support).</dl>
 

 <i>edit-urls</i> (default key: <i>E</i>)
<dl>
<dt>
<dd> Edit the list of subscribed URLs. newsbeuter will start the editor configured through the $VISUAL environment variable (if unset, $EDITOR is used; fallback: &quot;vi&quot;). When editing is finished, newsbeuter will reload the URLs file.</dl>
 

 <i>reload-urls</i> (default key: <i>^R</i>)
<dl>
<dt>
<dd> Reload the URLs configuration file.</dl>
 

 <i>redraw</i> (default key: <i>^L</i>)
<dl>
<dt>
<dd> Redraw the screen.</dl>
 

 <i>cmdline</i> (default key: <i>&lt;colon&gt;</i>)
<dl>
<dt>
<dd> Open the command line.</dl>
 

 <i>set-filter</i> (default key: <i>F</i>)
<dl>
<dt>
<dd> Set a filter.</dl>
 

 <i>select-filter</i> (default key: <i>f</i>)
<dl>
<dt>
<dd> Select a predefined filter.</dl>
 

 <i>clear-filter</i> (default key: <i>^F</i>)
<dl>
<dt>
<dd> Clear currently set filter.</dl>
 

 <i>bookmark</i> (default key: <i>^B</i>)
<dl>
<dt>
<dd> Bookmark currently selected article or URL.</dl>
 

 <i>edit-flags</i> (default key: <i>^E</i>)
<dl>
<dt>
<dd> Edit the flags of the currently selected article.</dl>
 

 <i>next-unread-feed</i> (default key: <i>^N</i>)
<dl>
<dt>
<dd> Go to the next feed with unread articles. This only works from the article list.</dl>
 

 <i>prev-unread-feed</i> (default key: <i>^P</i>)
<dl>
<dt>
<dd> Go to the previous feed with unread articles. This only works from the article list.</dl>
 

 <i>delete-article</i> (default key: <i>D</i>)
<dl>
<dt>
<dd> Delete the currently selected article.</dl>
 

 <i>purge-deleted</i> (default key: <i>$</i>)
<dl>
<dt>
<dd> Purge all article that are marked as deleted from the article list.</dl>
 

 <i>view-dialogs</i> (default key: <i>v</i>)
<dl>
<dt>
<dd> View list of open dialogs.</dl>
 

 <i>close-dialog</i> (default key: <i>^X</i>)
<dl>
<dt>
<dd> Close currently selected dialog.</dl>
 

 <i>next-dialog</i> (default key: <i>^V</i>)
<dl>
<dt>
<dd> Go to next dialog.</dl>
 

 <i>prev-dialog</i> (default key: <i>^G</i>)
<dl>
<dt>
<dd> Go to previous dialog.</dl>
 

 <i>pipe-to</i> (default key: <i>|</i>)
<dl>
<dt>
<dd> Pipe article to command.</dl>
 

 <i>sort</i> (default key: <i>g</i>)
<dl>
<dt>
<dd> Sort feeds/articles by interactively choosing the sort method.</dl>
 

 <i>revsort</i> (default key: <i>G</i>)
<dl>
<dt>
<dd> Sort feeds/articles by interactively choosing the sort method (reversed).</dl>
 

 <i>up</i> (default key: <i>UP</i>)
<dl>
<dt>
<dd> Goes up one item in the list.</dl>
 

 <i>down</i> (default key: <i>DOWN</i>)
<dl>
<dt>
<dd> Goes down one item in the list.</dl>
 

 <i>pageup</i> (default key: <i>PPAGE</i>)
<dl>
<dt>
<dd> Goes up one page in the list.</dl>
 

 <i>pagedown</i> (default key: <i>NPAGE</i>)
<dl>
<dt>
<dd> Goes down one page in the list.</dl>

<h2>TAGGING</h2>

 Newsbeuter comes with the possibility to categorize or &quot;tag&quot;, as we call it, RSS feeds. Every RSS feed can be assigned 0 or more tags. Within newsbeuter, you can then select to only show RSS feeds that match a certain tag. That makes it easy to categorize your feeds in a flexible and powerful way. 

 Usually, the ~/.newsbeuter/urls file contains one RSS feed URL per line. To assign a tag to an RSS feed, simply attach it as a single word, separated by blanks such as space or tab. If the tag needs to contain spaces, you must use quotes (&quot;) around the tag (see example below). An example ~/.newsbeuter/urls file may look like this: 

 

<dl>
<dt>
<dd> <pre>
<a rel="nofollow" HREF="http://blog.fefe.de/rss.xml?html">http://blog.fefe.de/rss.xml?html</a> interesting conspiracy news &quot;cool stuff&quot;
<a rel="nofollow" HREF="http://rss.orf.at/news.xml">http://rss.orf.at/news.xml</a> news orf
<a rel="nofollow" HREF="http://www.heise.de/newsticker/heise.rdf">http://www.heise.de/newsticker/heise.rdf</a> news interesting
</pre></dl>
 When you now start newsbeuter with this configuration, you can press &quot;t&quot; to select a tag. When you select the tag &quot;news&quot;, you will see all three RSS feeds. Pressing &quot;t&quot; again and e.g. selecting the &quot;conspiracy&quot; tag, you will only see the <a rel="nofollow" HREF="http://blog.fefe.de/rss.xml?html">http://blog.fefe.de/rss.xml?html</a> RSS feed. Pressing &quot;^T&quot; clears the current tag, and again shows all RSS feeds, regardless of their assigned tags. 

 A special type of tag are tags that start with the tilde character (&quot;~&quot;). When such a tag is found, the feed title is set to the tag name (excluding the ~ character). With this feature, you can give feeds any title you want in your feed list: 

 

<dl>
<dt>
<dd> <pre>
<a rel="nofollow" HREF="http://rss.orf.at/news.xml">http://rss.orf.at/news.xml</a> &quot;~ORF News&quot;
</pre></dl>

<h2>SCRIPTS AND FILTERS</h2>

 From version 0.4 on, newsbeuter contains support for Snownews extensions. The RSS feed readers Snownews and Liferea share a common way of extending the readers with custom scripts. Two mechanisms, namely &quot;execurl&quot; and &quot;filter&quot; type scripts, are available and supported by newsbeuter. 

 An &quot;execurl&quot; script can be any program that gets executed and whose output is interpreted as RSS feed, while &quot;filter&quot; scripts are fed with the content of a configured URL and whose output is interpreted as RSS feed. 

 The configuration is simple and straight-forward. Just add to your ~/.newsbeuter/urls file configuration lines like the following ones: 

 

<dl>
<dt>
<dd> <pre>
exec:~/bin/execurl-script
filter:~/bin/filter-script:<a rel="nofollow" HREF="http://some.test/url">http://some.test/url</a>
</pre></dl>
 The first line shows how to add an execurl script to your configuration: start the line with &quot;exec:&quot; and then immediately append the path of the script that shall be executed. If this script requires additional parameters, simply use quotes: 

 

<dl>
<dt>
<dd> <pre>
&quot;exec:~/bin/execurl-script param1 param2&quot;
</pre></dl>
 The second line shows how to add a filter script to your configuration: start the line with &quot;filter:&quot;, then immediately append the path of the script, then append a colon (&quot;:&quot;), and then append the URL of the file that shall be fed to the script. Again, if the script requires any parameters, simply quote: 

 

<dl>
<dt>
<dd> <pre>
&quot;filter:~/bin/filter-script param1 param2:<a rel="nofollow" HREF="http://url/foobar">http://url/foobar</a>&quot;
</pre></dl>
 In both cases, the tagging feature as described above is still available: 

 

<dl>
<dt>
<dd> <pre>
exec:~/bin/execurl-script tag1 tag2 &quot;quoted tag&quot;
filter:~/bin/filter-script:<a rel="nofollow" HREF="http://some.test/url">http://some.test/url</a> tag3 tag4 tag5
</pre></dl>
 A collection of such extension scripts can be found on this website: <a rel="nofollow" HREF="http://kiza.kcore.de/software/snownews/snowscripts/extensions">http://kiza.kcore.de/software/snownews/snowscripts/extensions</a> 

 If you want to write your own extensions, refer to this website for further instructions: <a rel="nofollow" HREF="http://kiza.kcore.de/software/snownews/snowscripts/writing">http://kiza.kcore.de/software/snownews/snowscripts/writing</a> 

<h2>COMMAND LINE</h2>

 Like other text-oriented software, newsbeuter contains an internal commandline to modify configuration variables ad hoc and to run own commands. It provides a flexible access to the functionality of newsbeuter which is especially useful for advanced users. 

 To start the commandline, type &quot;:&quot;. You will see a &quot;:&quot; prompt at the bottom of the screen, similar to tools like vi(m) or mutt. You can now enter commands. Pressing the return key executes the command (possibly giving feedback to the user) and closes the commandline. You can cancel entering commands by pressing the ESC key. The history of all the commands that you enter will be saved to ~/.newsbeuter/history.cmdline. The backlog is limited to 100 entries by default, but can be influenced by setting the &quot;history-limit&quot; configuration variable. To disable history saving, set the history-limit to 0. 

 Starting with newsbeuter 2.0, the commandline provides you with some help if you can't remember the full names of commandline commands. By pressing the TAB key, newsbeuter will try to automatically complete your command. If there is more than one possible completion, you can subsequently press the TAB key to cycle through all results. If no match is found, no suggestion will be inserted into the commandline. For the &quot;set&quot; command, the completion also works for configuration variable names. 

 In additon, some common key combination such as Ctrl-G (to cancel input), Ctrl-K (to delete text from the cursor position to the end of line), Ctrl-U (to clear the whole line) and Ctrl-W (to delete the word before the current cursor position) were added. 

 Please be aware that the input history of both the command line and the search functions are saved to the filesystems, to the files ~/.newsbeuter/history.cmdline resp. ~/.newsbeuter/history.search. By default, the last 100 entries are saved, but this can be configured (configuratin variable history-limit) and also totally disabled (by setting said variable to 0). 

 Currently, the following command line commands are available: 

 <i>quit</i>
<dl>
<dt>
<dd> Quit newsbeuter</dl>
 

 <i>save</i> &lt;filename&gt;
<dl>
<dt>
<dd> Save current article to &lt;filename&gt;</dl>
 

 <i>set</i> &lt;variable&gt;[=&lt;value&gt;|&amp;|!]
<dl>
<dt>
<dd> Set (or get) configuration variable value. Specifying a <i>!</i> after the name of a boolean configuration variable toggles their values, a <i>&amp;</i> directly after the name of a configuration variable of any type resets its value to the documented default value.</dl>
 

 <i>tag</i> &lt;tagname&gt;
<dl>
<dt>
<dd> Select a certain tag</dl>
 

 <i>goto</i> &lt;case-insensitive substring&gt;
<dl>
<dt>
<dd> Go to the next feed whose name contains the case-insensitive substring.</dl>
 

 <i>source</i> &lt;filename&gt; [...]
<dl>
<dt>
<dd> Load the specified configuration files. This allows it to load alternative configuration files or reload already loaded configuration files on-the-fly from the filesystem.</dl>
 

 <i>dumpconfig</i> &lt;filename&gt;
<dl>
<dt>
<dd> Save current internal state of configuration to file, so that it can be instantly reused as configuration file.</dl>
 

 <i>&lt;number&gt;</i>
<dl>
<dt>
<dd> Jump to the &lt;number&gt;th entry in the current dialog</dl>

<h2>FILES</h2>

 <i>$HOME/.newsbeuter/config</i> 

 <i>$HOME/.newsbeuter/urls</i> 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-podbeuter/">podbeuter</a>(1). The documentation that comes with newsbeuter is a good source about the general use and configuration of newsbeuter. 

<h2>AUTHORS</h2>

 Andreas Krennmair &lt;ak [at] newsbeuter.org&gt;, for contributors see AUTHORS file. 

<h2>NOTES</h2>

<dl>
<dt> 1.
<dd> ak [at] newsbeuter.org
<dl>
<dt>
<dd> mailto:ak [at] newsbeuter.org</dl>
 

</dl>

<h2>Index</h2>


