---
title: "tv_grab_na_dd(1)"
name: "tv_grab_na_dd"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_na_dd/"
description: "tv_grab_na_dd – Grab TV listings for North America using Schedules Direct"
---

<h2 class="name">NAME</h2>
<p> tv_grab_na_dd &#8211; Grab TV listings for North America using Schedules Direct </p>
<p><a rel="nofollow" href="http://www.schedulesdirect.org">http://www.schedulesdirect.org</a></p>
<h2>SYNOPSIS</h2>
<pre><code>
tv_grab_na_dd-- help
        tv_grab_na_dd-- version
            tv_grab_na_dd-- capabilities
                tv_grab_na_dd-- configure[--config - file FILE][--dd - data FILE]
                                         [--reprocess][--auto - config add | ignore]
                                         [--gui OPTION] tv_grab_na_dd-- list -
    lineups[--config - file FILE][--dd - data FILE]
           [--reprocess] tv_grab_na_dd[--config - file FILE][--dd - data FILE]
                                      [--reprocess][--auto - config add | ignore]
                                      [--days N][--offset N][--quiet][--notrim]
                                      [--old - chan - id][--low - mem][--output FILE]
                                      [--list - channel][--share SHAREDIR][--list - times]
                                      [--download - only][--padd n][--dropbadchar][--agent NAME]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This script downloads <font SIZE="-1">TV</font> listings using Schedules Direct&#8217;s data service, converts it to <font SIZE="-1">XMLTV</font> format, and outputs the results. </p>
<p> You must first register with Schedules Direct at: &lt;<a rel="nofollow" href="http://www.schedulesdirect.org">http://www.schedulesdirect.org</a>&gt; </p>
<p> Schedules Direct is a non-profit organization whose mission is to provide low-cost television program guide data to end-users of Open Source and Freeware applications. </p>
<p> The raw data source is Tribune Media Service&#8217;s Data Direct Service, which is very similar to the free Zap2IT Labs service Tribune previously offerred. </p>
<p> While the service is not available for free, Schedules Direct strives to keep costs as low as possible. </p>
<p> First you must become a member at the &lt;<a rel="nofollow" href="http://www.schedulesdirect.org">http://www.schedulesdirect.org</a>&gt; site. </p>
<p> Next, you use that website to add lineup(s) to your account. </p>
<p> Next, you execute <tt>&quot;tv_grab_na_dd --configure&quot;</tt> to set up the grabber. </p>
<p> Finally, you execute <code>tv_grab_na_dd</code> with no arguments and it will output listings in <font SIZE="-1">XML</font> format to standard output. See below for other options. </p>
<p> Like many utilities, tv_grab_na_dd tries to exit with a &#8220;0&#8221; on success and something else on error.</p>
<h2>Stand-alone options</h2>
<dl>
<dt>&#8211;help</p>
<dd> Print a help message and exit.</p>
<dt>&#8211;version</p>
<dd> Show the version of the grabber.</p>
<dt>&#8211;capabilities</p>
<dd> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt;</dl>
<h2>Mode selection (default is grab mode)</h2>
<dl>
<dt>&#8211;configure</p>
<dd> Activates configure mode. If a config file already exists the values are used as defaults.</p>
<dt>&#8211;gui <font SIZE="-1">OPTION</font></p>
<dd> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar.</p>
<dt>&#8211;list-lineups</p>
<dd> Lists available lineups. Only requires username in the config file. Used by programs that automate the &#8220;&#8211;configure&#8221; process.</dl>
<h2>General Options</h2>
<dl>
<dt>&#8211;config-file <i>file</i></p>
<dd> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_na_dd.conf</code>. This is the file created during &#8220;&#8211;configure&#8221; mode.</p>
<dt>&#8211;dd-data <i>file</i></p>
<dd> Store raw Data Direct data to this file. (default is a temporary file)</p>
<dt>&#8211;reprocess</p>
<dd> Don&#8217;t get data from Data Direct, but reprocess a file saved with &#8211;dd-data.</p>
<dt>&#8211;auto-config <i>add|ignore</i></p>
<dd> When used in &#8211;configure mode, updates the config file, removing old channels, and adding or ignoring new channels. Prompts are skipped if defaults are available in the current config file. </p>
<p> When used in grab mode, appends new channels to the config file.</dl>
<h2>Grabber Mode options</h2>
<dl>
<dt>&#8211;days <i>n</i></p>
<dd> Grab <i>n</i> days. The default is 7.</p>
<dt>&#8211;offset <i>n</i></p>
<dd> Start N days after the default.</p>
<dt>&#8211;quiet</p>
<dd> Suppress some messages normally written to standard error.</p>
<dt>&#8211;notrim</p>
<dd> Data Direct includes shows in progress at the start time. The default behavior is to filter these shows out so data can be cleanly split between days. This option turns off that filter so you get shows in progress a tthe start time.</p>
<dt>&#8211;old-chan-id</p>
<dd> Use a channel id similar to the one used by the old <code>tv_grab_na</code> grabber.</p>
<dt>&#8211;low-mem</p>
<dd> Omit all but the most basic program information. Reduces memory usage.</p>
<dt>&#8211;output <i>file</i></p>
<dd> Write xml to <i>file</i> rather than standard output.</p>
<dt>&#8211;list-channel</p>
<dd> Same as <code>&#8211;days</code> 0</p>
<dt>&#8211;share <i></i><font SIZE="-1"><i>SHAREDIR</i></font><i></i></p>
<dd> tv_grab_na_icons stores icons in <i></i><font SIZE="-1"><i>SHAREDIR</i></font><i></i>/icons. The share directory is set at install time, but there may be times when it needs to be specified. (for example: no write access to the default share directory)</p>
<dt>&#8211;list-times</p>
<dd> Report to <font SIZE="-1">STDERR</font> the Schedules Direct blockedTime (not currently enforced) and suggestedTime values to assist automated processes with scheduling.</p>
<dt>&#8211;download-only</p>
<dd> Don&#8217;t generate any output, just fetch the data. Personally I don&#8217;t see the point, but it was requested and easy to add.</p>
<dt>&#8211;padd <i>n</i></p>
<dd> Add &lt;n&gt; spaces to the front of the start date. This is normally not needed, but can be helpful in working around a Tribune problem when the request packet spans <font SIZE="-1">TCP</font> packets. Recommended initial value is &#8220;20&#8221;. This is only needed if you get &#8220;invalid start time&#8221; messages. If this helps, please post results to the list.</p>
<dt>&#8211;dropbadchar</p>
<dd> <font SIZE="-1">DD</font> data is supposed to be in <font SIZE="-1">UTF-8</font> format. Sometimes <font SIZE="-1">DD</font> sends bad characters which cause a &#8220;Bad <font SIZE="-1">XML</font> from <font SIZE="-1">DD&#8221;</font> error. This option causes those bad characters to be deleted.</p>
<dt>&#8211;agent <font SIZE="-1">NAME</font></p>
<dd> appends <font SIZE="-1">NAME</font> to the http agent string when fetching data. This is a polite way to tell Schedules Direct which application is being used. It helps developers know how many people are using their application and gives applications credit towards free accounts.</dl>
<h2>Automating configuration</h2>
<p> Sometimes applications want to call <code>tv_grab_na_dd</code> as a standalone application, but automate the configure process. The best way is to hook in to the XMLTV::Ask module, but if that&#8217;s not available, here is a solution. </p>
<dl>
<dt>
<dd> Step1. Application creates config file with username (and optionally password). </p>
<p> Step2. <tt>&quot;tv_grab_na_dd --dd-data lineups.xml --list-lineups&quot;</tt> </p>
<p> Step3. Application adds desired lineup to config file. </p>
<p> Step4. <tt>&quot;tv_grab_na_dd --dd-data lineups.xml --reprocess --auto-config add --list-channels&quot;</tt> </p>
<p> Step5. Application edits config file as needed, and deletes lineups.xml.</dl>
<h2>Grabber Timing</h2>
<p> Data Direct offers a &#8220;suggested download time&#8221; that can be retrieved with the &#8220;&#8211;list-times&#8221; option. Its use is encouraged.</p>
<h2>Handling Multiple Linups</h2>
<p> tv_grab_na_dd only outputs a single lineup. If your Schedules Direct account has multiple lineups, they are all downloaded even though only one is output. </p>
<p> To process multiple lineups, use separate &#8211;config-file. Separate config files are also handy if you need different channel sets for a lineup (common with MythTV). To prevent re-downloading the data on subsequent passes, the &#8220;&#8211;reprocess&#8221; option is recommended. </p>
<p> Here&#8217;s an example: (the = sign is optional, but helps readability) </p>
<pre><code>
tv_grab_na_dd-- config - file = lineup1.dat-- output = lineup1.xml-- dd - data = dd.xml
                                                                                     tv_grab_na_dd-- config -
                                                                                 file = lineup2.dat-- output = lineup2.xml-- dd - data = dd.xml-- reprocess
                                                                                                                                             tv_grab_na_dd-- config -
                                                                                                                                         file = lineup3.dat-- output = lineup3.xml-- dd - data = dd.xml-- reprocess
</code></pre>
<p> Each config file specifies the desired lineup and channel list. </p>
<p> If you want to merge the lineups into a single file, you can use tv_cat </p>
<pre>
 tv_cat lineup1.xml lineup2.xml lineup3.xml &gt;guide.xml
</pre>
<h2>Non-US/Canada listings. fake postal codes.</h2>
<p> <font SIZE="-1">TMS</font>&#8216;s Data direct service proivdes listings for a few non US/Canada locations. These are accessed with &#8220;fake&#8221; postal codes. The following are available: </p>
<pre>
    147BERM Bermuda Cablevision
    366HAMI Hamilton, Bermuda Wow World on Wireless
    101VENE DirecTV Latin America
    904MEXI Mexico #1
    954MEXI Mexico #2
    512TRIN Trinidad Express
    782YOKO Yokota AFB, Japan. Americable International
</pre>
<p> For a more complete list, check the Schedules Direct <font SIZE="-1">FAQ</font></p>
<h2>Adding icon links to listings</h2>
<p> <code>tv_grab_na_dd</code> checks for channel icons in a directory share/<code>icons</code>. The <i>share</i> directory is usually set during the install. For windows exe users, it defaults to the location where <code>xmltv.exe</code> is. <code>tv_grab_na_icons</code> is available to download the icons.</p>
<h2>Notes on channel lists</h2>
<p> Channel lists can be configured both at the Schedules Direct website and through the grabber. This is done to allow multiple config files with different channel lists as Schedules Direct only supports a single channel map per lineup. </p>
<p> Similarly, tv_grab_na_dd only supports a single channel mapping for a station. If multiple mappings are detected, only the first one is used and you are advised to adjust your Schedules Direct lineup.</p>
<h2>Notes on episode numbers</h2>
<p> Three episode-num formats are supplied (when available)</p>
<dl>
<dt>xmltv_ns</p>
<dd> always <tt>&quot;..a/b&quot;</tt> for part <tt>&quot;a&quot;</tt> of <tt>&quot;b&quot;</tt>. First two xmltv_ns fields always blank.</p>
<dt>dd_progid</p>
<dd> <font SIZE="-1">TMS</font> generated <tt>&quot;a.b.c/d&quot;</tt> where <tt>&quot;a&quot;</tt> is a unique program id, <tt>&quot;b&quot;</tt> is a unique episode id, <tt>&quot;c/d&quot;</tt> is part <tt>&quot;c&quot;</tt> of <tt>&quot;d&quot;</tt> similar to xmltv_ns.</p>
<dt>onscreen</p>
<dd> Distributor-designated number corresponding to an episode of a specific show. Varies by distributor.</dl>
<h2>Notes on passwords</h2>
<p> If a password is stored in the config file, the config file should be properly protected. Instead of storing the password in the config file, it can be omitted, and will be prompted for.</p>
<h2>Notes on lineup changes</h2>
<p> Data Direct currently adds a channel to your lineup automatically when it is available. When <code>tv_grab_na_dd</code> sees the new channel in the Schedules Direct lineup, it prints a message (and potentially adds or ignores it based on &#8211;auto-config). </p>
<p> If you are sensitive to bandwidth issues, I would set <code>&#8211;auto-config ignore</code> and periodically check your <code>&#8211;config-file</code> for ignored channels and remove from your Schedules Direct lineup.</p>
<h2>Notes on previously-shown</h2>
<p> Previous releases of tv_grab_na_dd set <font SIZE="-1">XMLTV</font>&#8216;s &#8220;date&#8221; field for <font SIZE="-1">DD </font>&#8220;original-air-date&#8221; field. The correct place for the data is &#8220;previously-shown-&gt;start&#8221; The <font SIZE="-1">OAD</font> is in both places temporarily for compatability reasons. </p>
<p> <font SIZE="-1">DD</font> has dropped the &#8220;repeat&#8221; flag and replaced it with a &#8220;new&#8221; flag. Now we set &quot;previously-shown</p>
<h2>Known issues</h2>
<p> none!</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>Author</h2>
<p> Author/Maintainer: Robert Eden, rmeden [at] yahoo.com</p>
<h3>Contributors:</h3>
<dl>
<dt>
<dd> Ed Avis, ed [at] membled.com </p>
<p> Don Huettl, drh [at] huettl.net </p>
<p> Matti Airas, mairas [at] iki.fi (I used tv_grab_fi as a template) </p>
<p> and of course everyone else I forgot to mention. :)</dl>
<h2>POD ERRORS</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 340:</p>
<dd> =over without closing =back </p>
</dl>
<h2>Index</h2>
