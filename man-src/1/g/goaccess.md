---
title: "goaccess(1)"
name: "goaccess"
section: "1"
letter: "g"
url: "/docs/linux/man/1-goaccess/"
description: "goaccess – fast web log analyzer and interactive viewer."
---

<h2>NAME</h2>
<p> goaccess &#8211; fast web log analyzer and interactive viewer.</p>
<h2>SYNOPSIS</h2>
<p> <code>goaccess [-f input-file][-c][-r][-d][-m][-q][-o][-h][&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>goaccess</code> GoAccess is an open source real-time web log analyzer and interactive viewer that runs in a <i>terminal</i> in *nix systems or through your <i>browser.</i> </p>
<p> It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly. </p>
<p> GoAccess parses the specified web log file and outputs the data to the X terminal. Features include: </p>
<dl>
<dt>General Statistics:</p>
<dd> This panel gives a summary of several metrics, some of them are: number of valid and invalid requests, time taken to analyze the data set, unique visitors, requested files, static files (CSS, ICO, JPG, etc) HTTP referrers, 404s, size of the parsed log file and bandwidth consumption.</p>
<dt>Unique visitors</p>
<dd> This panel shows metrics such as hits, unique visitors and cumulative bandwidth per date. HTTP requests containing the same IP, the same date, and the same user agent are considered a unique visitor. By default, it includes web crawlers/spiders.</p>
<dt>
<dd> Optionally, date specificity can be set to the hour level using <i>&#8211;date-spec=hr</i> which will display dates such as 05/Jun/2016:16. This is great if you want to track your daily traffic at the hour level.</p>
<dt>Requested files</p>
<dd> This panel displays the most highly requested files on your web server. It shows hits, unique visitors, and percentage, along with the cumulative bandwidth, protocol, and the request method used.</p>
<dt>Requested static files</p>
<dd> Lists the most frequently static files such as: JPG, CSS, SWF, JS, GIF, and PNG file types, along with the same metrics as the last panel. Additional static files can be added to the configuration file.</p>
<dt>404 or Not Found</p>
<dd> Displays the same metrics as the previous request panels, however, its data contains all pages that were not found on the server, or commonly known as 404 status code.</p>
<dt>Hosts</p>
<dd> This panel has detailed information on the hosts themselves. This is great for spotting aggressive crawlers and identifying who&#8217;s eating your bandwidth. </p>
<p> Expanding the panel can display more information such as host&#8217;s reverse DNS lookup result, country of origin and city. If the <i>-a</i> argument is enabled, a list of user agents can be displayed by selecting the desired IP address, and then pressing ENTER.</p>
<dt>Operating Systems</p>
<dd> This panel will report which operating system the host used when it hit the server. It attempts to provide the most specific version of each operating system.</p>
<dt>Browsers</p>
<dd> This panel will report which browser the host used when it hit the server. It attempts to provide the most specific version of each browser.</p>
<dt>Visit Times</p>
<dd> This panel will display an hourly report. This option displays 24 data points, one for each hour of the day.</p>
<dt>
<dd> Optionally, hour specificity can be set to the tenth of a minute level using <i>&#8211;hour-spec=min</i> which will display hours as 16:4 This is great if you want to spot peaks of traffic on your server.</p>
<dt>Virtual Hosts</p>
<dd> This panel will display all the different virtual hosts parsed from the access log. This panel is displayed if <i>%v</i> is used within the log-format string.</p>
<dt>Referrers URLs</p>
<dd> If the host in question accessed the site via another resource, or was linked/diverted to you from another host, the URL they were referred from will be provided in this panel. See `&#8211;ignore-panel` in your configuration file to enable it. <i>disabled</i> by default.</p>
<dt>Referring Sites</p>
<dd> This panel will display only the host part but not the whole URL. The URL where the request came from.</p>
<dt>Keyphrases</p>
<dd> It reports keyphrases used on Google search, Google cache, and Google translate that have lead to your web server. At present, it only supports Google search queries via HTTP. See `&#8211;ignore-panel` in your configuration file to enable it. <i>disabled</i> by default.</p>
<dt>Geo Location</p>
<dd> Determines where an IP address is geographically located. Statistics are broken down by continent and country. It needs to be compiled with GeoLocation support.</p>
<dt>HTTP Status Codes</p>
<dd> The values of the numeric status code to HTTP requests. </p>
</dl>
<p> <i>NOTE:</i> Optionally and if configured, all panels can display the average time taken to serve the request. </p>
<h2>STORAGE</h2>
<p> There are three storage options that can be used with GoAccess. Choosing one will depend on your environment and needs.</p>
<dl>
<dt>Default Hash Tables</p>
<dd> In-memory storage provides better performance at the cost of limiting the dataset size to the amount of available physical memory. By default GoAccess uses in-memory hash tables. If your dataset can fit in memory, then this will perform fine. It has very good memory usage and pretty good performance.</p>
<dt>Tokyo Cabinet On-Disk B+ Tree</p>
<dd> Use this storage method for large datasets where it is not possible to fit everything in memory. The B+ tree database is slower than any of the hash databases since data has to be committed to disk. However, using an SSD greatly increases the performance. You may also use this storage method if you need data persistence to quickly load statistics at a later date.</p>
<dt>Tokyo Cabinet In-memory Hash Database</p>
<dd> An alternative to the default hash tables. It uses generic typing and thus it&#8217;s performance in terms of memory and speed is average.</dl>
<h2>CONFIGURATION</h2>
<p> Multiple options can be used to configure GoAccess. For a complete up-to-date list of configure options, run <i>./configure &#8211;help</i></p>
<dl>
<dt><code>&#8211;enable-debug</p>
<dd> Compile with debugging symbols and turn off compiler optimizations.</p>
<dt>&#8211;enable-utf8</p>
<dd> Compile with wide character support. Ncursesw is required.</p>
<dt>&#8211;enable-geoip</p>
<dd> Compile with GeoLocation support. MaxMind&#8217;s GeoIP is required.</p>
<dt>&#8211;enable-tcb=&lt;memhash|btree&gt;</p>
<dd> Compile with Tokyo Cabinet storage support. </code><i>memhash</i> will utilize Tokyo Cabinet&#8217;s on-memory hash database. <i>btree</i> will utilize Tokyo Cabinet&#8217;s on-disk B+ Tree database.</p>
<dt><code>&#8211;disable-zlib</p>
<dd> Disable zlib compression on B+ Tree database.</p>
<dt>&#8211;disable-bzip</p>
<dd> Disable bzip2 compression on B+ Tree database.</p>
<dt>&#8211;with-getline</p>
<dd> Use GNU getline() to parse full line requests instead of a fixed size buffer of 4096.</dl>
<p> </code></p>
<h2>OPTIONS</h2>
<p> The following options can be supplied to the command or specified in the configuration file. If specified in the configuration file, long options need to be used without prepending &#8211;.</p>
<dl>
<dt><code>&#8211;time-format=&lt;timeformat&gt;</p>
<dd> The time-format variable followed by a space, specifies the log format time containing either a name of a predefined format (see options below) or any combination of regular characters and special format specifiers.</p>
<dt>
<dd> They all begin with a percentage (%) sign. See `man strftime`. </code><i>%T or %H:%M:%S.</i></p>
<dt>
<dd> Note that if a timestamp is given in microseconds, <i>%f</i> must be used as time-format</p>
<dt><code>&#8211;date-format=&lt;dateformat&gt;</p>
<dd> The date-format variable followed by a space, specifies the log format time containing either a name of a predefined format (see options below) or any combination of regular characters and special format specifiers.</p>
<dt>
<dd> They all begin with a percentage (%) sign. See `man strftime`. </code><i>%Y-%m-%d.</i></p>
<dt>
<dd> Note that if a timestamp is given in microseconds, <i>%f</i> must be used as date-format</p>
<dt><code>&#8211;log-format=&lt;logformat&gt;</p>
<dd> The log-format variable followed by a space or </code><i>\t</i> for tab-delimited, specifies the log format string. </p>
<p> Note that if there are spaces within the format, the string needs to be enclosed in single/double quotes. Inner quotes need to be escaped.</p>
<dt>
<dd> In addition to specifying the raw log/date/time formats, for simplicity, any of the following predefined log format names can be supplied to the log/date/time-format variables. GoAccess can also handle one predefined name in one variable and another predefined name in another variable.</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>COMBINED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Combined Log Format,<br />
&nbsp;<wbr>&nbsp;<wbr>VCOMBINED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Combined Log Format with Virtual Host,<br />
&nbsp;<wbr>&nbsp;<wbr>COMMON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Common Log Format,<br />
&nbsp;<wbr>&nbsp;<wbr>VCOMMON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Common Log Format with Virtual Host,<br />
&nbsp;<wbr>&nbsp;<wbr>W3C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; W3C Extended Log File Format,<br />
&nbsp;<wbr>&nbsp;<wbr>SQUID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Native Squid Log Format,<br />
&nbsp;<wbr>&nbsp;<wbr>CLOUDFRONT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Amazon CloudFront Web Distribution,<br />
&nbsp;<wbr>&nbsp;<wbr>CLOUDSTORAGE &#8211; Google Cloud Storage,<br />
&nbsp;<wbr>&nbsp;<wbr>AWSELB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Amazon Elastic Load Balancing,</p>
<dt><code>-a &#8211;agent-list</p>
<dd> Enable a list of user-agents by host. For faster parsing, do not enable this flag.</p>
<dt>-c &#8211;config-dialog</p>
<dd> Prompt log/date configuration window on program start.</p>
<dt>-p &#8211;config-file=&lt;configfile&gt;</p>
<dd> Specify a custom configuration file to use. If set, it will take priority over the global configuration file (if any).</p>
<dt>&#8211;debug-file=&lt;debugfile&gt;</p>
<dd> Send all debug messages to the specified file.</p>
<dt>-e &#8211;exclude-ip=&lt;IP|IP-range&gt;</p>
<dd> Exclude an IPv4 or IPv6 from being counted. Ranges can be included as well using a dash in between the IPs (start-end).</p>
<dt>
<dd> </code><i>Examples:</i><br />
&nbsp;<wbr>&nbsp;<wbr>exclude-ip 127.0.0.1<br />
&nbsp;<wbr>&nbsp;<wbr>exclude-ip 192.168.0.1-192.168.0.100<br />
&nbsp;<wbr>&nbsp;<wbr>exclude-ip ::1<br />
&nbsp;<wbr>&nbsp;<wbr>exclude-ip 0:0:0:0:0:ffff:808:804-0:0:0:0:0:ffff:808:808</p>
<dt><code>-g &#8211;std-geoip</p>
<dd> Standard GeoIP database for less memory usage.</p>
<dt>-h &#8211;help</p>
<dd> The help.</p>
<dt>-i &#8211;hl-header</p>
<dd> Color highlight active panel.</p>
<dt>-M &#8211;http-method=&lt;yes|no&gt;</p>
<dd> Set/unset HTTP request method. This will create a request key containing the request method + the actual request.</p>
<dt>-H &#8211;http-protocol=&lt;yes|no&gt;</p>
<dd> Set/unset HTTP request protocol. This will create a request key containing the request protocol + the actual request.</p>
<dt>-f &#8211;log-file=&lt;logfile&gt;</p>
<dd> Specify the path to the input log file. If set in the config file, it will take priority over -f from the command line.</p>
<dt>-q &#8211;no-query-string</p>
<dd> Ignore request&#8217;s query string. i.e., <a rel="nofollow" href="http://www.google.com">www.google.com</a>/page.htm?query =&gt; <a rel="nofollow" href="http://www.google.com">www.google.com</a>/page.htm.</p>
<dt>
<dd> </code><i>Note:</i> Removing the query string can greatly decrease memory consumption, especially on timestamped requests.</p>
<dt><code>-r &#8211;no-term-resolver</p>
<dd> Disable IP resolver on terminal output.</p>
<dt>-o &#8211;output=&lt;path/file.[json|csv|html]&gt;</p>
<dd> Write output to stdout given one of the following files and the corresponding extension for the output format:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>/path/file.csv&nbsp;<wbr>&nbsp;<wbr>&#8211; Comma-separated values&nbsp;<wbr>(CSV)<br />
&nbsp;<wbr>&nbsp;<wbr>/path/file.json &#8211; JSON&nbsp;<wbr>(JavaScript Object Notation)<br />
&nbsp;<wbr>&nbsp;<wbr>/path/file.html &#8211; HTML</p>
<dt>-s &#8211;storage</p>
<dd> Display current storage method. i.e., B+ Tree, Hash.</p>
<dt>-V &#8211;version</p>
<dd> Display version information and exit.</p>
<dt>-m &#8211;with-mouse</p>
<dd> Enable mouse support on main dashboard.</p>
<dt>-d &#8211;with-output-resolver</p>
<dd> Enable IP resolver on HTML|JSON output.</p>
<dt>&#8211;444-as-404</p>
<dd> Treat non-standard status code 444 as 404.</p>
<dt>&#8211;4xx-to-unique-count</p>
<dd> Add 4xx client errors to the unique visitors count.</p>
<dt>&#8211;addr</p>
<dd> Specify IP address to bind the server to. Otherwise it binds to 0.0.0.0.</p>
<dt>
<dd> Usually there is no need to specify the address, unless you intentionally would like to bind the server to a different address within your server.</p>
<dt>&#8211;all-static-files</p>
<dd> Include static files that contain a query string.</p>
<dt>&#8212;color=&lt;fg:bg[attrs, PANEL]&gt;</p>
<dd> Specify custom colors for the terminal output. </p>
<p> </code><i>Color Syntax</i><br />
&nbsp;<wbr>&nbsp;<wbr>DEFINITION space/tab colorFG#:colorBG#&nbsp;<wbr>[attributes,PANEL] </p>
<p>&nbsp;<wbr>FG#&nbsp;<wbr>=&nbsp;<wbr>foreground color&nbsp;<wbr>[-1&#8230;255]&nbsp;<wbr>(-1&nbsp;<wbr>=&nbsp;<wbr>default term color)<br />
&nbsp;<wbr>BG#&nbsp;<wbr>=&nbsp;<wbr>background color&nbsp;<wbr>[-1&#8230;255]&nbsp;<wbr>(-1&nbsp;<wbr>=&nbsp;<wbr>default term color) </p>
<p> Optionally, it is possible to apply color attributes (multiple attributes are comma separated), such as: <i>bold,</i> <i>underline,</i> <i>normal,</i> <i>reverse,</i> <i>blink</i> </p>
<p> If desired, it is possible to apply custom colors per panel, that is, a metric in the REQUESTS panel can be of color A, while the same metric in the BROWSERS panel can be of color B. </p>
<p> <i>Available color definitions:</i><br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_HITS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_VISITORS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_DATA<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_BW<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_AVGTS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_CUMTS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_MAXTS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_PROT<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_MTHD<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_PERC<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_MTRC_PERC_MAX<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_PANEL_COLS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_BARS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_ERROR<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_SELECTED<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_PANEL_ACTIVE<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_PANEL_HEADER<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_PANEL_DESC<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_OVERALL_LBLS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_OVERALL_VALS<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_OVERALL_PATH<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_ACTIVE_LABEL<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_BG<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_DEFAULT<br />
&nbsp;<wbr>&nbsp;<wbr>COLOR_PROGRESS </p>
<p> See configuration file for a sample color scheme.</p>
<dt><code>&#8211;color-scheme=&lt;1|2|3&gt;</p>
<dd> Choose among color schemes. </code><i>1</i> for the default grey scheme. <i>2</i> for the green scheme.</p>
<dt><code>&#8211;date-spec=&lt;date|hr&gt;</p>
<dd> Set the date specificity to either date (default) or hr to display hours appended to the date.</p>
<dt>
<dd> This is used in the visitors panel. It&#8217;s useful for tracking visitors at the hour level. For instance, an hour specificity would yield to display traffic as 18/Dec/2010:19</p>
<dt>&#8211;dcf</p>
<dd> Display the path of the default config file when `-p` is not used.</p>
<dt>&#8211;double-decode</p>
<dd> Decode double-encoded values. This includes, user-agent, request, and referer.</p>
<dt>&#8211;enable-panel=&lt;PANEL&gt;</p>
<dd> Enable parsing and displaying the given panel.</p>
<dt>
<dd> </code><i>Available panels:</i><br />
&nbsp;<wbr>&nbsp;<wbr>VISITORS<br />
&nbsp;<wbr>&nbsp;<wbr>REQUESTS<br />
&nbsp;<wbr>&nbsp;<wbr>REQUESTS_STATIC<br />
&nbsp;<wbr>&nbsp;<wbr>NOT_FOUND<br />
&nbsp;<wbr>&nbsp;<wbr>HOSTS<br />
&nbsp;<wbr>&nbsp;<wbr>OS<br />
&nbsp;<wbr>&nbsp;<wbr>BROWSERS<br />
&nbsp;<wbr>&nbsp;<wbr>VISIT_TIMES<br />
&nbsp;<wbr>&nbsp;<wbr>VIRTUAL_HOSTS<br />
&nbsp;<wbr>&nbsp;<wbr>REFERRERS<br />
&nbsp;<wbr>&nbsp;<wbr>REFERRING_SITES<br />
&nbsp;<wbr>&nbsp;<wbr>KEYPHRASES<br />
&nbsp;<wbr>&nbsp;<wbr>GEO_LOCATION<br />
&nbsp;<wbr>&nbsp;<wbr>STATUS_CODES</p>
<dt><code>&#8211;hour-spec=&lt;hr|min&gt;</p>
<dd> Set the time specificity to either hour (default) or min to display the tenth of a minute appended to the hour.</p>
<dt>
<dd> This is used in the time distribution panel. It&#8217;s useful for tracking peaks of traffic on your server at specific times.</p>
<dt>&#8211;html-custom-css=&lt;path.css&gt;</p>
<dd> Specifies a custom CSS file path to load in the HTML report.</p>
<dt>&#8211;html-custom-js=&lt;path.js&gt;</p>
<dd> Specifies a custom JS file path to load in the HTML report.</p>
<dt>&#8211;html-report-title=&lt;title&gt;</p>
<dd> Set HTML report page title and header.</p>
<dt>&#8211;ignore-crawlers</p>
<dd> Ignore crawlers from being counted.</p>
<dt>&#8211;ignore-panel=&lt;PANEL&gt;</p>
<dd> Ignore parsing and displaying the given panel.</p>
<dt>
<dd> </code><i>Available panels:</i><br />
&nbsp;<wbr>&nbsp;<wbr>VISITORS<br />
&nbsp;<wbr>&nbsp;<wbr>REQUESTS<br />
&nbsp;<wbr>&nbsp;<wbr>REQUESTS_STATIC<br />
&nbsp;<wbr>&nbsp;<wbr>NOT_FOUND<br />
&nbsp;<wbr>&nbsp;<wbr>HOSTS<br />
&nbsp;<wbr>&nbsp;<wbr>OS<br />
&nbsp;<wbr>&nbsp;<wbr>BROWSERS<br />
&nbsp;<wbr>&nbsp;<wbr>VISIT_TIMES<br />
&nbsp;<wbr>&nbsp;<wbr>VIRTUAL_HOSTS<br />
&nbsp;<wbr>&nbsp;<wbr>REFERRERS<br />
&nbsp;<wbr>&nbsp;<wbr>REFERRING_SITES<br />
&nbsp;<wbr>&nbsp;<wbr>KEYPHRASES<br />
&nbsp;<wbr>&nbsp;<wbr>GEO_LOCATION<br />
&nbsp;<wbr>&nbsp;<wbr>STATUS_CODES</p>
<dt><code>&#8211;ignore-referer=&lt;referer&gt;</p>
<dd> Ignore referers from being counted. Wildcards allowed. e.g., </code><i>*.domain.com</i> <i>ww?.domain.*</i></p>
<dt><code>&#8211;ignore-status=&lt;CODE&gt;</p>
<dd> Ignore parsing and displaying one or multiple status code(s). For multiple status codes, use this option multiple times.</p>
<dt>&#8211;invalid-requests=&lt;filename&gt;</p>
<dd> Log invalid requests to the specified file.</p>
<dt>&#8211;json-pretty-print</p>
<dd> Format JSON output using tabs and newlines.</p>
<dt>
<dd> </code><i>Note:</i> This is not recommended when outputting a real-time HTML report since the WebSocket payload will much much larger.</p>
<dt><code>&#8211;max-items=&lt;number&gt;</p>
<dd> The maximum number of items to display per panel. The maximum can be a number between 1 and n.</p>
<dt>
<dd> </code><i>Note:</i> Only the CSV and JSON output allow a maximum number greater than the default value of 366 (or 50 in the real-time HTML output) items per panel.</p>
<dt><code>&#8211;no-color</p>
<dd> Turn off colored output. This is the default output on terminals that do not support colors.</p>
<dt>&#8211;no-column-names</p>
<dd> Don&#8217;t write column names in the terminal output. By default, it displays column names for each available metric in every panel.</p>
<dt>&#8211;no-csv-summary</p>
<dd> Disable summary metrics on the CSV output.</p>
<dt>&#8211;no-global-config</p>
<dd> Do not load the global configuration file. This directory should normally be /usr/local/etc, unless specified with </code><i>&#8211;sysconfdir=/dir.</i></p>
<dt><code>&#8211;no-progress</p>
<dd> Disable progress metrics [total requests/requests per second].</p>
<dt>&#8211;no-tab-scroll</p>
<dd> Disable scrolling through panels when TAB is pressed or when a panel is selected using a numeric key.</p>
<dt>&#8211;origin=&lt;url&gt;</p>
<dd> Ensure clients send the specified origin header upon the WebSocket handshake.</p>
<dt>&#8211;port=&lt;port&gt;</p>
<dd> Specify the port to use. By default GoAccess listens on port 7890 for the WebSocket server.</p>
<dt>&#8211;real-os</p>
<dd> Display real OS names. e.g, Windows XP, Snow Leopard.</p>
<dt>&#8211;real-time-html</p>
<dd> Enable real-time HTML output.</p>
<dt>
<dd> GoAccess uses its own WebSocket server to push the data from the server to the client. See <a rel="nofollow" href="http://gwsocket.io">http://gwsocket.io</a> for more details how the WebSocket server works.</p>
<dt>&#8211;sort-panel=&lt;PANEL,FIELD,ORDER&gt;</p>
<dd> Sort panel on initial load. Sort options are separated by comma. Options are in the form: PANEL,METRIC,ORDER</p>
<dt>
<dd> </code><i>Available metrics:</i><br />
&nbsp;<wbr>&nbsp;<wbr>BY_HITS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by hits<br />
&nbsp;<wbr>&nbsp;<wbr>BY_VISITORS &#8211; Sort by unique visitors<br />
&nbsp;<wbr>&nbsp;<wbr>BY_DATA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by data<br />
&nbsp;<wbr>&nbsp;<wbr>BY_BW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by bandwidth<br />
&nbsp;<wbr>&nbsp;<wbr>BY_AVGTS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by average time served<br />
&nbsp;<wbr>&nbsp;<wbr>BY_CUMTS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by cumulative time served<br />
&nbsp;<wbr>&nbsp;<wbr>BY_MAXTS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by maximum time served<br />
&nbsp;<wbr>&nbsp;<wbr>BY_PROT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by http protocol<br />
&nbsp;<wbr>&nbsp;<wbr>BY_MTHD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Sort by http method</p>
<dt>
<dd> <i>Available orders:</i><br />
&nbsp;<wbr>&nbsp;<wbr>ASC<br />
&nbsp;<wbr>&nbsp;<wbr>DESC</p>
<dt><code>&#8211;ws-url=&lt;url[:port]&gt;</p>
<dd> URL to which the WebSocket server responds. This is the URL supplied to the WebSocket constructor on the client side.</p>
<dt>
<dd> If GoAccess is running behind a proxy, you could set the client side to connect to a different port by specifying the host followed by a colon and the port. e.g., </code><i>goaccess.io:9999</i></p>
<dt>
<dd> By default, it will attempt to connect to localhost. If GoAccess is running on a remote server, the host of the remote server should be specified here. Also, make sure it is a valid host and NOT an http address.</p>
<dt><code>&#8211;static-file=&lt;extension&gt;</p>
<dd> Add static file extension. e.g.: </code><i>.mp3</i> Extensions are case sensitive.</p>
<dt><code>&#8211;geoip-database=&lt;geofile&gt;</p>
<dd> Specify path to GeoIP database file. i.e., GeoLiteCity.dat. File needs to be downloaded from maxmind.com. IPv4 and IPv6 files are supported as well. </code><i>Note:</i> `&#8211;geoip-city-data` is an alias of `&#8211;geoip-database`.</p>
<dt><code>&#8211;keep-db-files</p>
<dd> Persist parsed data into disk. If database files exist, files will be overwritten. This should be set to the first dataset. Setting it to false will delete all database files when exiting the program. See examples below. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt>&#8211;load-from-disk</p>
<dd> Load previously stored data from disk. If reading persisted data only, the database files need to exist. See </code><i>keep-db-files</i> and examples below. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt><code>&#8211;db-path=&lt;dir&gt;</p>
<dd> Path where the on-disk database files are stored. The default value is the </code><i>/tmp</i> directory. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt><code>&#8211;xmmap=&lt;num&gt;</p>
<dd> Set the size in bytes of the extra mapped memory. The default value is 0. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt>&#8211;cache-lcnum=&lt;num&gt;</p>
<dd> Specifies the maximum number of leaf nodes to be cached. If it is not more than 0, the default value is specified. The default value is 1024. Setting a larger value will increase speed performance, however, memory consumption will increase. Lower value will decrease memory consumption. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt>&#8211;cache-ncnum=&lt;num&gt;</p>
<dd> Specifies the maximum number of non-leaf nodes to be cached. If it is not more than 0, the default value is specified. The default value is 512. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt>&#8211;tune-lmemb=&lt;num&gt;</p>
<dd> Specifies the number of members in each leaf page. If it is not more than 0, the default value is specified. The default value is 128. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt>&#8211;tune-nmemb=&lt;num&gt;</p>
<dd> Specifies the number of members in each non-leaf page. If it is not more than 0, the default value is specified. The default value is 256. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt>&#8211;tune-bnum=&lt;num&gt;</p>
<dd> Specifies the number of elements of the bucket array. If it is not more than 0, the default value is specified. The default value is 32749. Suggested size of the bucket array is about from 1 to 4 times of the number of all pages to be stored. </p>
<p> Only if configured with &#8211;enable-tcb=btree</p>
<dt>&#8211;compression=&lt;zlib|bz2&gt;</p>
<dd> Specifies that each page is compressed with ZLIB|BZ2 encoding. </p>
<p> Only if configured with &#8211;enable-tcb=btree </p>
</dl>
<p> </code></p>
<h2>CUSTOM LOG/DATE FORMAT</h2>
<p> GoAccess can parse virtually any web log format. </p>
<p> Predefined options include, Common Log Format (CLF), Combined Log Format (XLF/ELF), including virtual host, Amazon CloudFront (Download Distribution), Google Cloud Storage and W3C format (IIS). </p>
<p> GoAccess allows any custom format string as well. </p>
<p> There are two ways to configure the log format. The easiest is to run GoAccess with <i>-c</i> to prompt a configuration window. Otherwise, it can be configured under ~/.goaccessrc or the %sysconfdir%.</p>
<dl>
<dt>time-format</p>
<dd> The <i>time-format</i> variable followed by a space, specifies the log format time containing any combination of regular characters and special format specifiers. They all begin with a percentage (%) sign. See `man strftime`. <i>%T or %H:%M:%S.</i></p>
<dt>
<dd> <i>Note:</i> If a timestamp is given in microseconds, <i>%f</i> must be used as <i>time-format</i></p>
<dt>date-format</p>
<dd> The <i>date-format</i> variable followed by a space, specifies the log format date containing any combination of regular characters and special format specifiers. They all begin with a percentage (%) sign. See `man strftime`. e.g., <i>%Y-%m-%d.</i></p>
<dt>
<dd> <i>Note:</i> If a timestamp is given in microseconds, <i>%f</i> must be used as <i>date-format</i></p>
<dt>log-format</p>
<dd> The <i>log-format</i> variable followed by a space or <i>\t</i> , specifies the log format string.</p>
<dt>%x</p>
<dd> A date and time field matching the <i>time-format</i> and <i>date-format</i> variables. This is used when a timestamp is given instead of the date and time being in two separated variables.</p>
<dt>%t</p>
<dd> time field matching the <i>time-format</i> variable.</p>
<dt>%d</p>
<dd> date field matching the <i>date-format</i> variable.</p>
<dt>%v</p>
<dd> The canonical Server Name of the server serving the request (Virtual Host).</p>
<dt>%h</p>
<dd> host (the client IP address, either IPv4 or IPv6)</p>
<dt>%r</p>
<dd> The request line from the client. This requires specific delimiters around the request (as single quotes, double quotes, or anything else) to be parsable. If not, we have to use a combination of special format specifiers as %m %U %H.</p>
<dt>%q</p>
<dd> The query string.</p>
<dt>%m</p>
<dd> The request method.</p>
<dt>%U</p>
<dd> The URL path requested. </p>
<p> <i>Note:</i> If the query string is in %U, there is no need to use <i>%q.</i> However, if the URL path, does not include any query string, you may use <i>%q</i> and the query string will be appended to the request.</p>
<dt>%H</p>
<dd> The request protocol.</p>
<dt>%s</p>
<dd> The status code that the server sends back to the client.</p>
<dt>%b</p>
<dd> The size of the object returned to the client.</p>
<dt>%R</p>
<dd> The &quot;Referrer&quot; HTTP request header.</p>
<dt>%u</p>
<dd> The user-agent HTTP request header.</p>
<dt>%D</p>
<dd> The time taken to serve the request, in microseconds as a decimal number.</p>
<dt>%T</p>
<dd> The time taken to serve the request, in seconds with milliseconds resolution.</p>
<dt>%L</p>
<dd> The time taken to serve the request, in milliseconds as a decimal number.</p>
<dt>
<dd> <i>Note:</i> If multiple time served specifiers are used at the same time, the first option specified in the format string will take priority over the other specifiers.</p>
<dt>%^</p>
<dd> Ignore this field.</p>
<dt>%~</p>
<dd> Move forward through the log string until a non-space (!isspace) char is found.</dl>
<p> GoAccess <i>requires</i> the following fields:</p>
<dl>
<dt>
<dd> <i>%h</i> a valid IPv4/6</p>
<dt>
<dd> <i>%d</i> a valid date</p>
<dt>
<dd> <i>%r</i> the request</dl>
<h2>INTERACTIVE MENU</h2>
<dl>
<dt>F1 or h</p>
<dd> Main help.</p>
<dt>F5</p>
<dd> Redraw main window.</p>
<dt>q</p>
<dd> Quit the program, current window or collapse active module</p>
<dt>o or ENTER</p>
<dd> Expand selected module or open window</p>
<dt>0-9 and Shift + 0</p>
<dd> Set selected module to active</p>
<dt>j</p>
<dd> Scroll down within expanded module</p>
<dt>k</p>
<dd> Scroll up within expanded module</p>
<dt>c</p>
<dd> Set or change scheme color.</p>
<dt>TAB</p>
<dd> Forward iteration of modules. Starts from current active module.</p>
<dt>SHIFT + TAB</p>
<dd> Backward iteration of modules. Starts from current active module.</p>
<dt>^f</p>
<dd> Scroll forward one screen within an active module.</p>
<dt>^b</p>
<dd> Scroll backward one screen within an active module.</p>
<dt>s</p>
<dd> Sort options for active module</p>
<dt>/</p>
<dd> Search across all modules (regex allowed)</p>
<dt>n</p>
<dd> Find the position of the next occurrence across all modules.</p>
<dt>g</p>
<dd> Move to the first item or top of screen.</p>
<dt>G</p>
<dd> Move to the last item or bottom of screen.</dl>
<h2>EXAMPLES</h2>
<h3>DIFFERENT OUTPUTS</h3>
<p> To output to a terminal and generate an interactive report:</p>
<dl>
<dt>
<dd> # goaccess -f access.log</dl>
<p> To generate an HTML report:</p>
<dl>
<dt>
<dd> # goaccess -f access.log -a -o report.html</dl>
<p> To generate a JSON report:</p>
<dl>
<dt>
<dd> # goaccess -f access.log -a -d -o report.json</dl>
<p> To generate a CSV file:</p>
<dl>
<dt>
<dd> # goaccess -f access.log &#8211;no-csv-summary -o report.csv</p>
<dt>&bull;</p>
<dd> <i>-a</i> flag indicates that we want to process an agent-list for every host parsed.</p>
<dt>&bull;</p>
<dd> <i>-d</i> flag indicates that we want to enable the IP resolver on the HTML|JSON output. (It will take longer time to output since it has to resolve all queries)</p>
<dt>&bull;</p>
<dd> <i>-c</i> flag will prompt the date and log format configuration window. Only when curses is initialized.</dl>
<h3>REAL TIME HTML OUTPUT</h3>
<p> GoAccess has the ability the output real-time data in the HTML report. You can even email the HTML file since it is composed of a single file with no external file dependencies, how neat is that! </p>
<p> To output an HTML report and set the WebSocket server to listen on port 7890 and localhost.</p>
<dl>
<dt>
<dd> # goaccess -f access.log -o report.html &#8211;real-time-html</dl>
<p> If GoAccess is running and parsing logs on a specific host, you can specify the URL to which the client&#8217;s browser will connect to.</p>
<dl>
<dt>
<dd> # goaccess -f access.log -o report.html &#8211;real-time-html &#8211;ws-url=goaccess.io</dl>
<p> To use a different port other than 7890, you can specify it as:</p>
<dl>
<dt>
<dd> # goaccess -f access.log -o report.html &#8211;real-time-html &#8211;ws-url=goaccess.io &#8211;port=9870</dl>
<p> And to bind the WebSocket server to a different address other than 0.0.0.0, you can specify it as:</p>
<dl>
<dt>
<dd> # goaccess -f access.log -o report.html &#8211;real-time-html &#8211;ws-url=goaccess.io &#8211;addr=127.0.0.1</dl>
<h3>MULTIPLE LOG FILES</h3>
<p> Now if we want to add more flexibility to GoAccess, we can do a series of pipes. For instance: </p>
<p> If we would like to process all <i>access.log.*.gz</i> we can do one of the following:</p>
<dl>
<dt>
<dd> # zcat -f access.log* | goaccess</p>
<dt>
<dd> # zcat access.log.*.gz | goaccess</dl>
<p> <i>Note:</i> On Mac OS X, use gunzip -c instead of zcat.</p>
<h3>WORKING WITH DATES</h3>
<p> Another useful pipe would be filtering dates out of the web log </p>
<p> The following will get all HTTP requests starting on 05/Dec/2010 until the end of the file.</p>
<dl>
<dt>
<dd> # sed -n &#8216;/05/Dec/2010/,$ p&#8217; access.log | goaccess -a</dl>
<p> or using relative dates such as yesterdays or tomorrows day:</p>
<dl>
<dt>
<dd> # sed -n &#8216;/&#8217;$(date &#8216;+%d/%b/%Y&#8217; -d &#8216;1 week ago&#8217;)&#8217;/,$ p&#8217; access.log | goaccess -a</dl>
<p> If we want to parse only a certain time-frame from DATE a to DATE b, we can do:</p>
<dl>
<dt>
<dd> # sed -n &#8216;/5/Nov/2010/,/5/Dec/2010/ p&#8217; access.log | goaccess -a</dl>
<h3>VIRTUAL HOSTS</h3>
<p> Assuming your log contains the virtual host field. For instance:</p>
<dl>
<dt>
<dd> vhost.com:80 10.131.40.139 &#8211; &#8211; [02/Mar/2016:08:14:04 -0600] &quot;GET /shop/bag-p-20 HTTP/1.1&quot; 200 6715 &quot;-&quot; &quot;Apache (internal dummy connection)&quot;</dl>
<p> And you would like to append the virtual host to the request in order to see which virtual host the top urls belong to</p>
<dl>
<dt>
<dd> awk &#8216;$8=$1$8&#8217; access.log | goaccess -a</dl>
<p> To exclude a list of virtual hosts you can do the following:</p>
<dl>
<dt>
<dd> # grep -v &quot;`cat exclude_vhost_list_file`&quot; vhost_access.log | goaccess</dl>
<h3>FILES &amp; STATUS CODES</h3>
<p> To parse specific pages, e.g., page views, html, htm, php, etc. within a request:</p>
<dl>
<dt>
<dd> # awk &#8216;$7~/.html|.htm|.php/&#8217; access.log | goaccess</dl>
<p> Note, <i>$7</i> is the request field for the common and combined log format, (without Virtual Host), if your log includes Virtual Host, then you probably want to use <i>$8</i> instead. It&#8217;s best to check which field you are shooting for, e.g.:</p>
<dl>
<dt>
<dd> # tail -10 access.log | awk &#8216;{print $8}&#8217;</dl>
<p> Or to parse a specific status code, e.g., 500 (Internal Server Error):</p>
<dl>
<dt>
<dd> # awk &#8216;$9~/500/&#8217; access.log | goaccess</dl>
<h3>SERVER</h3>
<p> Also, it is worth pointing out that if we want to run GoAccess at lower priority, we can run it as:</p>
<dl>
<dt>
<dd> # nice -n 19 goaccess -f access.log -a</dl>
<p> and if you don&#8217;t want to install it on your server, you can still run it from your local machine:</p>
<dl>
<dt>
<dd> # ssh root [at] server &#8216;cat /var/log/apache2/access.log&#8217; | goaccess -a</dl>
<h3>INCREMENTAL LOG PROCESSING</h3>
<p> GoAccess has the ability to process logs incrementally through the on-disk B+Tree database. It works in the following way: </p>
<dl>
<dt>step]</p>
<dd> A data set must be persisted first with <i>&#8211;keep-db-files,</i> then the same data set can be loaded with <i>&#8211;load-from-disk.</i></p>
<dt>step]</p>
<dd> If new data is passed (piped or through a log file), it will append it to the original data set.</p>
<dt>step]</p>
<dd> To preserve the data at all times, <i>&#8211;keep-db-files</i> must be used.</p>
<dt>step]</p>
<dd> If <i>&#8211;load-from-disk</i> is used without <i>&#8211;keep-db-files,</i> database files will be deleted upon closing the program.</dl>
<p> For instance:</p>
<dl>
<dt>
<dd> // last month access log<br />
 goaccess -f access.log.1 &#8211;keep-db-files</dl>
<p> then, load it with</p>
<dl>
<dt>
<dd> // append this month access log, and preserve new data<br />
 goaccess -f access.log &#8211;load-from-disk &#8211;keep-db-files</dl>
<p> To read persisted data only (without parsing new data)</p>
<dl>
<dt>
<dd> goaccess &#8211;load-from-disk &#8211;keep-db-files</dl>
<h2>NOTES</h2>
<p> Each active panel has a total of 366 items or 50 in the real-time HTML report. The number of items is customizable using <i>max-items</i> However, only the CSV and JSON output allow a maximum number greater than the default value of 366 items per panel. </p>
<p> Piping a log to GoAccess will disable the real-time functionality. This is due to the portability issue on determining the actual size of STDIN. However, a future release *might* include this feature. </p>
<p> A hit is a request (line in the access log), e.g., 10 requests = 10 hits. HTTP requests with the same IP, date, and user agent are considered a unique visit.</p>
<h2>BUGS</h2>
<p> If you think you have found a bug, please send me an email to <i>goaccess [at] prosoftcorp.com</i> or use the issue tracker in <a rel="nofollow" href="https://github.com/allinurl/goaccess/issues">https://github.com/allinurl/goaccess/issues</a></p>
<h2>AUTHOR</h2>
<p> Gerardo Orellana &lt;goaccess [at] prosoftcorp.com&gt; For more details about it, or new releases, please visit <a rel="nofollow" href="http://goaccess.io">http://goaccess.io</a> </p>
<h2>Index</h2>
