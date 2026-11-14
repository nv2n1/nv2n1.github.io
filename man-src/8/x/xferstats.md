---
title: "xferstats(8)"
name: "xferstats"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xferstats/"
description: "xferstats – compiles information about file transfers from logfiles"
---

<p>xferstats &#8211; compiles information about file transfers from logfiles</p>
<h2>Synopsis</h2>
<p><code>xferstats</code> [- | + ] [-c &lt;config file&gt;] [-T &lt;number&gt;] [[-+]C] [[-+]H] [[-+]n] [[-+]s] [[-+]r] [[-+]a] [[-+]g] [[-+]i] [[-+]u] [[-+]h] [[-+]m] [[-+]w] [[-+]M] [[-+]f [number]] [[-+]d [number]] [[-+]t [number]] [[-+]O [number]] [[-+]o [number]] [+L &lt;number&gt;] [+A] [-D &lt;number&gt;] [+D &lt;number&gt;] [+P &lt;prefix&gt;] [+B &lt;timestamp&gt;] [+E &lt;timestamp&gt;] [-v] [&#8211;version] [&#8211;help] [&#8211;] [filename(s)] </p>
<h2>Description</h2>
<p><code>xferstats</code> is a utility that parses wu-ftpd, ncftpd, and (special) apache <code>xferlogs</code> (although it&#8217;s not difficult to add support for other log types) and gives various information and totals about the data transferred. </p>
<h2>Options</h2>
<dl>
<dt><code>+</code></p>
<dd>The single plus tells <code>xferstats</code> to get the <code>xferlog</code> from stdin. For example:</p>
<dd>cat xferlog | xferstats +</p>
<dt><code>&#8211;</code></p>
<dd>The single hyphen tells <code>xferstats</code> to get the <code>xferlog</code> from a file. While this is the default behaviour, the configuration file may change the default, and this option allows you to override it. For example:</p>
<dd>xferstats &#8211; /var/log/xferlog</p>
<dt><code>-c</code><i> configuration file</i></p>
<dd>Specify an alternate path and filename for the configuration file. The packaged default is <i>/etc/xferstats.cfg</i> but your administrator may have changed this. A new default can be set by changing the appropriate variable in xferstats.h and recompiling.</p>
<dt><code>-T</code><i> log type</i></p>
<dd>Specify the type of log file to be parsed. Currently, only three types are defined, <code>wu-ftpd</code> for wu-ftpd-style logs, <code>ncftpd</code> for ncftpd-style logs, and <code>apache</code> for special Apache logs. Note: you can also use &quot;wu-ftp&quot;, &quot;wuftp&quot;, &quot;wuftpd&quot;, or &quot;ncftp&quot;. In order for xferstats to parse Apache logfiles, you must use a special LogFile line: LogFormat &quot;%{%a %b %d %X %Y}t %T %h %b %f %u&quot;. <code>xferstats</code> may or may not support regular Apache logfiles in the future. If this is something you want, please let me know.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Display what version of <code>xferstats</code> you&#8217;re running.</p>
<dt><code>&#8211;help</code></p>
<dd>Display a quick summary of the command line options.</p>
<dt><code>&#8212;</code></p>
<dd>Use a &#8212; (double hyphen) to indicate that you are finished giving parameters and will follow with a filename. This is particularly useful when you want to specify a filename that begins with a + or &#8211; </p>
</dl>
<h3>Toggle Options</h3>
<p>The options in this section can be either forced on with +[option] or forced off with -[option]. Options in this section, like all other options, will always override any settings in the xferstats configuration file. Any arguments to toggle options should only be used when enabling an option. Supplying an argument when disabling an option will generate an error. </p>
<dl>
<dt><code>C</code></p>
<dd>When enabled, xferstats will try to weed out corrupt log lines by strictly checking to make sure that the data is valid. If you &#8211;enable-debug_flow at compile time, xferstats will notify you when corrupt lines are detected.</p>
<dt><code>H</code></p>
<dd>When enabled, xferstats will generate HTML tables and graphs instead of text tables. In order to actually generate tables instead of broken graphic icons, you must put the graph JPGs in the directory pointed to by the GRAPH_PATH configuration command. For more information, see the CONFIGURATION FILE section.</p>
<dt><code>n</code></p>
<dd>When enabled, xferstats will refrain from adding &lt;HTML&gt;, &lt;BODY&gt;, and &lt;TITLE&gt; tags, so that the output can be inserted into pages containing custom headers.</p>
<dt><code>s</code></p>
<dd>When enabled, xferstats will output HTML as a single page (filename &quot;xferstats.html&quot;) instead of a page for each section. This option also disables &lt;HTML&gt; and &lt;BODY&gt; tags, although it does produce a &lt;TITLE&gt; tag unless the NO_HTML_HEADERS option is also specified.</p>
<dt><code>r</code></p>
<dd>When enabled, xferstats will generate statistics about real user connections (but not necessarily <code>only</code> real user connections)</p>
<dt><code>a</code></p>
<dd>When enabled, xferstats will generate statistics about anonymous connections (but not necessarily <code>only</code> anonymous connections)</p>
<dt><code>g</code></p>
<dd>When enabled, xferstats will generate statistics about guest connections (but not necessarily <code>only</code> guest connections)</p>
<dt><code>i</code></p>
<dd>When enabled, xferstats will generate statistics about inbound (the product of a PUT) files (but not necessarily <code>only</code> inbound files)</p>
<dt><code>u</code></p>
<dd>When enabled, xferstats will generate statistics about outbound (the product of a GET) files (but not necessarily <code>only</code> outbound files)</p>
<dt><code>h</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by hour</p>
<dt><code>m</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by month (January, February, etc.)</p>
<dt><code>S</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by file size</p>
<dt><code>w</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by day of the week (Monday, Tuesday, etc.)</p>
<dt><code>M</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by day of the month (1st, 2nd, 3rd, etc.)</p>
<dt><code>f&nbsp;<wbr>[number]</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by file. You can supply an optional argument that will determine how many file records xferstats displays (0 (zero) disables the limit)</p>
<dt><code>d&nbsp;<wbr>[number]</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by directory. You can supply an optional argument that will determine how many directory records xferstats displays (0 (zero) disables the limit). See the -D and +D options, as well as the DIR_DEPTH and DIR_FILTER configuration commands for more information.</p>
<dt><code>t&nbsp;<wbr>[number]</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by top-level domain. You can supply an optional argument that will determine how many TLD records xferstats displays (0 (zero) disables the limit)</p>
<dt><code>O&nbsp;<wbr>[number]</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by domain. You can supply an optional argument that will determine how many domain records xferstats displays (0 (zero) disables the limit)</p>
<dt><code>o&nbsp;<wbr>[number]</code></p>
<dd>When enabled, xferstats will generate a report listing traffic by host. You can supply an optional argument that will determine how many host records xferstats displays (0 (zero) disables the limit) </p>
</dl>
<h3>Other Options</h3>
<dl>
<dt><code>+A</code></p>
<dd>Include all users, generate all reports</p>
<dt><code>+L&nbsp;<wbr>&lt;number&gt;</code></p>
<dd>Limit the daily report to the last &lt;number&gt; days</p>
<dt><code>-D&nbsp;<wbr>&lt;number&gt;</code></p>
<dd>Depth of path detail for directories (default 3)</p>
<dt><code>+D&nbsp;<wbr>&lt;directory&gt;</code></p>
<dd>Generate reports on files located only in <i>&lt;directory&gt;</i>. For example:</p>
<dd><code>+D&nbsp;<wbr>/pub</code> will report only on paths under <code>/pub</code>. Specifying multiple +D options will instruct <code>xferstats</code> to include data from all specified directories.</p>
<dt><code>+P&nbsp;<wbr>&lt;path</code><i>prefix&gt;</i></p>
<dd>Strip the <i>&lt;prefix&gt;</i> from any pathnames that begin with it. This is the same as specifying a <i>STRIP_PREFIX</i> configuration file command. Keep in mind that the <i>DIR_FILTER</i> (or <i>+D</i>) is checked before the <i>STRIP_PREFIX</i> (or <i>+P</i>) when using these.</p>
<dt><code>+B&nbsp;<wbr>&lt;timestamp&gt;</code></p>
<dd>Providing a +B argument instructs xferstats to only generate data on transfers occuring after that time. The time stamp format is &quot;Jan DD HH:MM:ss YYYY&quot;. One may combine +B and +E to generate a report about a specific window in time.</p>
<dt><code>+E&nbsp;<wbr>&lt;timestamp&gt;</code></p>
<dd>Providing a +E argument instructs xferstats to only generate data on transfers occuring before that time. The time stamp format is &quot;Jan DD HH:MM:ss YYYY&quot;. One may combine +B and +E to generate a report about a specific window in time.</dl>
<p> The default compile-time setting for the <code>xferlog</code> location is <code>/var/log/xferlog</code> but your administrator may have changed this. If <code>xferstats</code> reports an error, try specifying the filename as the last command line parameter.</p>
<h2>Configuration File</h2>
<p>The default configuration file path is <i>/etc/xferstats.cfg</i> although your administrator may have changed this. </p>
<p> Any text after a &#8216;#&#8217; is ignored, as long as the &#8216;#&#8217; begins a line or is prepended by whitespace. </p>
<p> Commands (LOGFILE, ANON_TRAFFIC, etc) are not case sensitive, although some arguments may be. </p>
<dl>
<dt><code>LOGFILE &lt;filename&gt;</code></p>
<dd>sets the default log file to process. It can be overridden by adding &quot;&lt;filename&gt;&quot; at the end of the command line options. You may specify as many LOGFILE lines as you like; they will be processed in the order specified (although the order processed should not change the output). Example:</p>
<dd>LOGFILE /var/log/xferlog LOGFILE /var/log/xferlog.1 LOGFILE /var/log/xferlog.2</p>
<dt><code>STRICT_CHECK</code></p>
<dd>takes no arguments. When enabled, xferstats will try to weed out corrupt log lines by strictly checking to make sure that the data is valid. If you &#8211;enable-debug_flow at compile time, xferstats will notify you when corrupt lines are detected. It can be enabled with &quot;+C&quot; or disabled with &quot;-C&quot; on the command line.</p>
<dt><code>ANON_TRAFFIC</code></p>
<dd>takes no arguments. When enabled, xferstats will generate statistics about anonymous connections (but not necessarily <code>only</code> anonymous connections). It can be enabled with &quot;+a&quot; or disabled with &quot;-a&quot; on the command line.</p>
<dt><code>GUEST_TRAFFIC</code></p>
<dd>takes no arguments. When enabled, xferstats will generate statistics about guest connections (but not necessarily <code>only</code> guest connections). This option has no effect when parsing non-wuftpd logfiles. It can be enabled with &quot;+g&quot; or disabled with &quot;-g&quot; on the command line.</p>
<dt><code>REAL_TRAFFIC</code></p>
<dd>takes no arguments. When enabled, xferstats will generate statistics about real user connections (but not necessarily <code>only</code> real user connections). It can be enabled with &quot;+r&quot; or disabled with &quot;-r&quot; on the command line.</p>
<dt><code>INBOUND</code></p>
<dd>takes no arguments. When enabled, xferstats will generate statistics about inbound (the product of a PUT) files (but not necessarily <code>only</code> inbound files). It can be enabled with &quot;+i&quot; or disabled with &quot;-i&quot; on the command line.</p>
<dt><code>OUTBOUND</code></p>
<dd>takes no arguments. When enabled, xferstats will generate statistics about outbound (the product of a GET) files (but not necessarily <code>only</code> outbound files). It can be enabled with &quot;+u&quot; or disabled with &quot;-u&quot; on the command line.</p>
<dt><code>HOURLY_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic per hour. It can be enabled with &quot;+h&quot; or disabled with &quot;-h&quot; on the command line.</p>
<dt><code>DOW_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic by day of the week (Monday, Tuesday, etc). It can be enabled with &quot;+w&quot; or disabled with &quot;-w&quot; on the command line.</p>
<dt><code>DOM_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic by day of the month (1st, 2nd, etc). It can be enabled with &quot;+M&quot; or disabled with &quot;-M&quot; on the command line.</p>
<dt><code>TLD_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic by top-level domain (com, edu, net, us, uk, etc). It can be enabled with &quot;+t &lt;number&gt;&quot; or disabled with &quot;-t&quot; on the command line.</p>
<dt><code>DOMAIN_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic by domain (foo.com, blah.edu, etc). It can be enabled with &quot;+O &lt;number&gt;&quot; or disabled with &quot;-O&quot; on the command line.</p>
<dt><code>HOST_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic by host. It can be enabled with &quot;+o&quot; or disabled with &quot;-o&quot; on the command line.</p>
<dt><code>DIR_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic by directory. The directory depth that xferstats will keep track of can be controlled by the DIR_DEPTH configuration command or with the &quot;-l &lt;depth&gt;&quot; command line option. It can be enabled with &quot;+d&quot; or disabled with &quot;-d&quot; on the command line.</p>
<dt><code>FILE_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic by file. It can be enabled with &quot;+f&quot; or disabled with &quot;-f&quot; on the command line.</p>
<dt><code>MONTHLY_REPORT</code></p>
<dd>takes no arguments. When enabled, xferstats will generate a report listing traffic per month (January, February, etc). It can be enabled with &quot;+m&quot; or disabled with &quot;-m&quot; on the command line.</p>
<dt><code>HTML_OUTPUT</code></p>
<dd>takes no arguments. When enabled, xferstats will output all reports into individual HTML files. Future versions will contain a configuration option to set the directory in which to place the HTML files. For now they are placed in the present working# directory. It can be enabled with &quot;+H&quot; or disabled with &quot;-H&quot; on the command line.</p>
<dt><code>USE_STDIN</code></p>
<dd>takes no arguments. When enabled, xferstats will, by default, read the logfile from the standard input instead of from a file on disk. It can be enabled with &quot;+&quot; or disabled with &quot;-&quot; on the command line.</p>
<dt><code>LOG_TYPE</code></p>
<dd>takes one argument, the type of log that will be processed by default. The argument can be either a number or a case insensitive string and are as follows:</p>
<dd>wu-ftpd log: &quot;1&quot; or &quot;wu-ftp&quot; or &quot;wu-ftpd&quot; or &quot;wuftp&quot; or &quot;wuftpd&quot;</p>
<dd>ncftpd log : &quot;2&quot; or &quot;ncftp&quot; or &quot;ncftpd&quot;</p>
<dd>Apache log : &quot;3&quot; or &quot;apache&quot;</p>
<dd>Therefore:</p>
<dd>LOG_TYPE 1</p>
<dd>LOG_TYPE wu-ftp</p>
<dd>LOG_TYPE wu-ftpd</p>
<dd>LOG_TYPE wuftp</p>
<dd>LOG_TYPE wuftpd</p>
<dd>are all equivalent.</p>
<dd>Future versions will contain support for additional logfile types. It can be set on the command line with &quot;-T &lt;number&gt;&quot;</p>
<dt><code>DIR_DEPTH</code></p>
<dd>takes one argument, the number of subdirectories deep that xferstats should go when generating statistics by directory. This configuration command has no effect when DIR_REPORT has not been enabled. DIR_DEPTH has no upper bound. A DIR_DEPTH of &#8216;0&#8217; (zero) tells xferstats to process all subdirectories. The default value is 3. It can be set on the command line with &quot;-D &lt;number&gt;&quot;. Example:</p>
<dd>DIR_DEPTH 3</p>
<dt><code>DIR_FILTER</code></p>
<dd>takes one argument, the directory that xferstats should report on. xferstats will discard any data that does not have a path that begins with the value set by DIR_FILTER. This value <code>is</code> case-sensitive, as it is part of a path name. Specifying multiple statements will instruct <code>xferstats</code> to include data from all specified directories. It can be set on the command line with &quot;+D &lt;path&gt;&quot;. Example:</p>
<dd>DIR_FILTER /pub/foobar</p>
<dt><code>NUMBER_FILE_STATS</code></p>
<dd>takes one argument, the number of files to report on in the file statistics section. It must be a number greater than or equal to zero, with zero denoting no limit. It can be set on the command line with &quot;+f &lt;number&gt;&quot;. The default is 50.</p>
<dd>NUMBER_FILE_STATS 50</p>
<dt><code>NUMBER_DIR_STATS</code></p>
<dd>takes one argument, the number of directories to report on in the directory statistics section. It must be a number greater than or equal to zero, with zero denoting no limit. It can be set on the command line with &quot;+d &lt;number&gt;&quot;. The default is 50.</p>
<dt><code>NUMBER_DAILY_STATS</code></p>
<dd>takes one argument, the number of days to report on in the daily statistics section. It must be a number greater than or equal to zero, with zero denoting no limit. It can be set on the command line with &quot;+L &lt;number&gt;&quot;. The default is 50.</p>
<dd>Note: the daily statistics section will always be displayed.</p>
<dt><code>NUMBER_TLD_STATS</code></p>
<dd>takes one argument, the number of top-level domains to report on in the TLD statistics section. It must be a number greater than or equal to zero, with zero denoting no limit. It can be set on the command line with &quot;+t &lt;number&gt;&quot;. The default is 50.</p>
<dt><code>NUMBER_DOMAIN_STATS</code></p>
<dd>takes one argument, the number of top-level domains to report on in the domain statistics section. It must be a number greater than or equal to zero, with zero denoting no limit. It can be set on the command line with &quot;+O &lt;number&gt;&quot;. The default is 50.</p>
<dt><code>NUMBER_HOST_STATS</code></p>
<dd>takes one argument, the number of hosts to report on in the host statistics section. It must be a number greater than or equal to zero, with zero denoting no limit. It can be set on the command line with &quot;+o &lt;number&gt;&quot;. The default is 50.</p>
<dt><code>MAX_REPORT_SIZE</code></p>
<dd>takes one argument, the maximum size of any one output table. This is particularly useful to keep xferstats from generating gigantic tables that make graphical browsers choke. It will split tables to be no larger than# this value. It must be greater than or equal to ten, or zero, zero denoting no limit. It can be set on the command line with &quot;+R &lt;number&gt;&quot;. The default is 30.</p>
<dt><code>GRAPH_PATH</code></p>
<dd>takes one argument, the location of the JPGs used to draw graphs in the HTML output. It can be an absolute path (ie, <a rel="nofollow" href="http://foo.bar.com/graphs/)">http://foo.bar.com/graphs/)</a> or a relative path (ie, ../graphs/). You must include a trailing &#8216;/&#8217; or it <code>will not work.</code> This option cannot be set on the command line. The default is nothing (which will make the browser look for the graphs in the directory with the HTML). Example:</p>
<dd>GRAPH_PATH ../graphs/</p>
<dt><code>NO_HTML_HEADERS</code></p>
<dd>takes no arguments. When enabled, xferstats will refrain from adding &lt;HTML&gt;, &lt;BODY&gt;, and &lt;TITLE&gt; tags, so that the output can be inserted into pages containing custom headers. It can be enabled with &quot;+n&quot; or disabled with &quot;-n&quot; on the command line.</p>
<dt><code>REFRESH</code></p>
<dd>takes one argument, the number of seconds after being displayed that the browser should refresh it. Unspecified or zero indicates no refresh.</p>
<dt><code>SINGLE_PAGE</code></p>
<dd>takes no arguments. When enabled, xferstats will output HTML as a single page (entitled &quot;xferstats.html&quot;) instead of a page for each section. This option also disables &lt;HTML&gt; and &lt;BODY&gt; tags, although it does produce a &lt;TITLE&gt; tag unless the NO_HTML_HEADERS option is also specified. It can be enabled with &quot;+s&quot; or disabled with &quot;-s&quot; on the command line.</p>
<dt><code>STRIP_PREFIX</code></p>
<dd>takes one argument. When specified, xferstats will strip the given string from the beginning of any paths. Keep in mind when using this option with <code>DIR_FILTER</code> that the <code>DIR_FILTER</code> is applied -before- stripping, so that you must take this into account when specifying the <code>DIR_FILTER</code> string. This option cannot be set on the command line. Example:</p>
<dd>STRIP_PREFIX /home/ftp</dl>
<p> The next 11 entries are all basically the same&#8211;they define how the reports are to be sorted.</p>
<dl>
<dd><code>0</code> &#8212; Sort by the number of bytes downloaded</p>
<dd><code>1</code> &#8212; Sort by the number of files downloaded</p>
<dd><code>2</code> &#8212; Sort by the &quot;name&quot;. This varies by report; for the file, directory, TLD, etc reports, it sorts them alphabetically; for the file size report it lists the file sizes in alphabetical order; for the daily report, it lists the days in order. You get the idea. <code>3</code> &#8212; Sort by average throughput, in K/s</p>
<dd><code>FILE_SORT_PREF</code>, <code>DIR_SORT_PREF</code>, <code>DOMAIN_SORT_PREF</code>, <code>TLD_SORT_PREF</code>, <code>HOST_SORT_PREF</code>, <code>DOM_SORT_PREF</code>, <code>DOW_SORT_PREF</code>, <code>HOURLY_SORT_PREF</code>, <code>DAILY_SORT_PREF</code>, <code>SIZE_SORT_PREF</code>, <code>MONTHLY_SORT_PREF</code></p>
<dt><code>CHUNK_INPUT</code></p>
<dd>takes one argument. When specified, xferstats will parse the logfiles in chunks of the given size (in number of lines), process them, and continue. This will keep it from trying to parse the entire log at once, using up a lot of memory for large logs. Specifying too small a value will cause xferstats to waste a lot of time switching tasks, while too large a value may slow it down as your system swaps. Toy with this value a bit and see what works best for you. If left unspecified, xferstats will continue to parse the logs in one pass. </p>
</dl>
<h2>Files</h2>
<p><code>xferlog</code> (generated by wu-ftpd or ncftpd) </p>
<p> <code>/etc/xferstats.cfg</code> contains all of the default settings and many settings which cannot be set from the command line. </p>
<p> If you installed the RPM version of xferstats, you&#8217;ll find the JPGs for the graphs in /usr/share/xferstats/graphs.</p>
<h2>Bugs</h2>
<p>The JPG graph pieces included are not ideal; sometimes artifacts show up. I will eventually get around to making new GIFs or something. Please send bug reports to phil [at] off.net If the xferlog that you&#8217;re using is smaller than 1 megabyte, please send a gzipped copy, along with the exact parameters you&#8217;re using. </p>
<h2>Acknowledgements</h2>
<p>I greatly appreciate the suggestions and assistance of Nat Friedman &lt;ndf [at] mit.edu&gt;. </p>
<p> Thanks to Mike Shaver &lt;shaver [at] mozilla.org&gt; and Jamie Zawinski &lt;jwz [at] netscape.com&gt; for coughing up gigantic mozilla.org logs to aid my testing. </p>
<p> Thanks to Phil Copeland &lt;bryce [at] zen.ics.uwe.ac.uk&gt; for getting on my back constantly to add new stuff, fix nagging bugs, and speed it up. Oh, and for using it, at least someone does :). </p>
<p> Extreme gratitude to Mark Hagler &lt;hagler [at] hagler.org&gt;, someone whom I&#8217;ve left off of this list for too long. Mark was kind enough to Amazon me a copy of O&#8217;Reillys _Pthreads Programming_ which was the catalyst for the threaded version and really helped get me interested in the project again. While the threaded version doesn&#8217;t exist anymore, the book is still terribly useful for other projects.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ftpd/">ftpd</a></code>(8), <code><a href="/docs/linux/man/8-ncftpd/">ncftpd</a></code>(8), <code><a href="/docs/linux/man/5-xferlog/">xferlog</a></code>(5) </p>
<h2>Location</h2>
<p><code>xferstats</code> is available from the following locations. The old addresses are valid, but are deprecated! Please use the new addresses whenever possible.</p>
<dl>
<dd><a rel="nofollow" href="http://xferstats.off.net/">http://xferstats.off.net/</a></p>
<dd><a href="ftp://xferstats.off.net/pub/xferstats/">ftp://xferstats.off.net/pub/xferstats/</a> </p>
</dl>
<h2>Author</h2>
<p><i>xferstats</i> is Copyright (c) 1997-2000 Phil Schwan &lt;phil [at] off.net&gt; and is released under the terms and provisions of the GNU Public License.</p>
