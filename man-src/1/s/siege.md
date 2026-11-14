---
title: "siege(1)"
name: "siege"
section: "1"
letter: "s"
url: "/docs/linux/man/1-siege/"
description: "siege is a HTTP/FTP load tester and benchmarking utility."
---

<h2 class="name">NAME</h2>
<p> siege is a HTTP/FTP load tester and benchmarking utility. </p>
<h2>SYNOPSIS</h2>
<pre><code>
siege[options] siege[options]&lt;URL&gt;
        siege[options] - g&lt;URL&gt; siege[options] - f urls.txt
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>siege</tt> is a multi-threaded <font SIZE="-1">HTTP/FTP</font> load tester and benchmarking utility. It supports most of the features detailed in RFCs 2616 (<font SIZE="-1">HTTP</font>) and 959 (<font SIZE="-1">FTP</font>). Properties can be set at both from the command line and in a configuration file. When the same propertie is set in both locations, the command line takes precedent. </p>
<p> The default configuration file is <tt>$HOME</tt>/.siege/siege.conf If you don&#8217;t have a <tt>$HOME</tt>/.siege directory and a siege.conf and cookies.txt file, siege will generate a new config directory when it runs. You can generate your configu directory with the following command: siege.config</p>
<h2>OPTIONS</h2>
<h3>Option Syntax</h3>
<p> <tt>siege</tt> supports long and short options. Short options look like this:<br />
&nbsp;<wbr>-c 25<br />
&nbsp;<wbr>-c25 </p>
<p> Long options look like this:<br />
&nbsp;<wbr>&#8211;concurrent=25</p>
<h3>Option Values</h3>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Displays the <tt>siege</tt> release version and copyright information.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Prints a help message describing <tt>siege</tt>&#8216;s command-line options.</p>
<dt><code>-C</code>, <code>&#8211;config</code></p>
<dd> Prints a detailed summary of all the currently configured options, most of which are sent in <tt>$HOME</tt>/.siege/siege.conf</p>
<dt><code>-v</code>, <code>&#8211;vebose</code></p>
<dd> This directive puts <tt>siege</tt> into verbose mode which is actually a default setting. This command-line option is useful when the config file is set to &#8216;verbose = false&#8217; since it will allow you to override that. </p>
<p> By default <tt>siege</tt>&#8216;s verbose output is displayed in a color-coded style.<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr><font SIZE="-1">HTTP</font>&nbsp;<wbr>2xx is coded blue<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr><font SIZE="-1">HTTP</font>&nbsp;<wbr>3xx is coded cyan<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr><font SIZE="-1">HTTP</font>&nbsp;<wbr>4xx is coded magenta<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr><font SIZE="-1">HTTP</font>&nbsp;<wbr>5xx is coded red<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr><font SIZE="-1">HTTP</font>&nbsp;<wbr>cached is coded black </p>
<p> <font SIZE="-1">NOTE:</font> You can turn off color in siege.conf like this: &#8216;color = off&#8217;</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> This directive silences <tt>siege</tt>. It is mostly used for scripting and is often used in conjunction with -g/&#8211;get. You can detect the success or failure of the run with its exit code. </p>
<p>  siege &#8211;quiet -g www.joedog.org<br />
  if [ $? -eq 0 ] ;<br />
  then<br />
      echo &#8220;Success&#8221; else echo &#8220;Failure&#8221; fi</p>
<dt><code>-g </code><font SIZE="-1"><code>URL</code></font>, <code>&#8211;get=URL</code></p>
<dd> This option allows you to request a <font SIZE="-1">URL</font> and watch the header transaction. There is a corresponding config file directive that allows you to set the request method for these requests: gmethod = HEAD|GET </p>
<pre>
  $ siege -g &quot;<a rel="nofollow" href="https://www.joedog.org/">https://www.joedog.org/</a>&quot;
  HEAD / HTTP/1.0
  Host: <a rel="nofollow" href="http://www.joedog.org">www.joedog.org</a>
  Accept: */*
  User-Agent: Mozilla/5.0 (unknown-x86_64-linux-gnu) Siege/4.0.0-beta5
  Connection: close
  HTTP/1.1 200 OK
  Server: cloudflare-nginx
  Date: Tue, 09 Feb 2016 18:18:41 GMT
  Content-Type: text/html; charset=UTF-8
  Connection: close
  Last-Modified: Wed, 25 Nov 2015 18:46:08 GMT
  Cache-Control: max-age=3, must-revalidate
  Expires: Tue, 09 Feb 2016 18:18:44 GMT
  Vary: Accept-Encoding,Cookie
  CF-RAY: 27219407eeff084a-IAD
</pre>
<p> <font SIZE="-1">NOTE:</font> It&#8217;s best practice to quote the <font SIZE="-1">URL</font> when it&#8217;s passed to <tt>siege</tt> from the the command-line.</p>
<dt><code>-c </code><font SIZE="-1"><code>NUM</code></font>, <code>&#8211;concurrent=NUM</code></p>
<dd> This option allows you to set the concurrent number of users. The total number of users is technically limited to your computer&#8217;s resources. </p>
<p> You should not configure more users than your web server is configured to handle. For example, the default apache configuration is capped at 255 threads. If you run siege with -c 1024, then 769 siege users are left waiting for an apache handler. </p>
<p> For this reason, the default siege configuration is capped at 255 users. You can increase that number inside siege.conf but if you make a mess, then please don&#8217;t complain to us.</p>
<dt><code>-r </code><font SIZE="-1"><code>NUM</code></font>, <code>&#8211;reps=NUM|once</code></p>
<dd> This option tells each siege user how times it should run. The value should generally be a number greater than zero but it may be the keyword &#8216;once&#8217;. </p>
<p> If &#8211;reps=3 then each siege user will run three times before it exits. However, if &#8211;reps=once, then each user will run through the urls.txt file exactly one time. </p>
<p> For more information about the urls.txt file, see option -f &lt;file&gt;, &#8211;file=&lt;file&gt;</p>
<dt><code>-t NUMm</code>, <code>&#8211;time=NUMm</code></p>
<dd> This option is similar to &#8211;reps but instead of specifying the number of times each user should run, it specifies the amount of time each should run. </p>
<p> The value format is &#8220;NUMm&#8221;, where &#8220;<font SIZE="-1">NUM</font>&#8221; is an amount of time and the &#8220;m&#8221; modifier is either S, M, or H for seconds, minutes and hours. To run <tt>siege</tt> for an hour, you could select any one of the following combinations: -t3600S, -t60M, -t1H. The modifier is not case sensitive, but it does require no space between the number and itself.</p>
<dt><code>-d </code><font SIZE="-1"><code>NUM</code></font>, <code>&#8211;delay=NUM</code></p>
<dd> This option instructs <tt>siege</tt> how long to delay between each page request. The value <font SIZE="-1">NUM</font> represents the number of seconds between each one. This number can be a decimal value. In fact the default is half a second (&#8211;delay=0.5). </p>
<p> The time between delay requests is <font SIZE="-1">NOT</font> applied toward the transaction time. If two 0.1 second transactions have a 2 second delay between them, their average transaction time is run is 0.1 seconds. It is applied toward the total elapsed time. In this scenario, the elapsed time would be 2.2 seconds. </p>
<p> <font SIZE="-1">NOTE:</font> when the parser is enabled (see: -p/&#8211;parser), there is no delay between the page and its elements, i.e., style sheets, javascripts, etc. The delay is only between page requests.</p>
<dt><code>-b</code>, <code>&#8211;benchmark</code></p>
<dd> This directive tells siege to go into benchmark mode. This means there is no delay between iterations.</p>
<dt><code>-i</code>, <code>&#8211;internet</code></p>
<dd> This option sets siege into what we call internet mode. It makes requests from the urls.txt file (see: -f &lt;file&gt; / &#8211;file=&lt;file&gt;) in random order.</p>
<dt><code>-f </code><font SIZE="-1"><code>FILE</code></font>, <code>&#8211;file=FILE</code></p>
<dd> This option tells siege to work with a list of urls inside a text file. The URLs are listed one per line. Unlike URLs that are passed as a command-line argument, the URLs in this file should not be quoted. </p>
<p> <tt>siege</tt>&#8216;s urls.txt parser supports comments and variables.</p>
<dt><code>-R </code><font SIZE="-1"><code>FILE</code></font>, <code>&#8211;rc=FILE</code></p>
<dd> This directive allows you to set an alternative resource file. By default, the siegerc file is <tt>$HOME</tt>/.siege/siege.conf With this directive, you can override the default and use an alternative file.</p>
<dt><code>-L </code><font SIZE="-1"><code>FILE</code></font>, <code>&#8211;log=FILE</code></p>
<dd> The default log file is <tt>$prefix</tt>/var/log/siege.log. This directive allows you to specify and alternative file for logging.</p>
<dt><code>-m &quot;string&quot;</code>, <code>&#8211;mark=&quot;string&quot;</code></p>
<dd> This option allows you to log a message to the log file before your stats are written there. It is generally used to identify the proceding run. You could, for example, mark the file with your command-line parameters so it&#8217;s understood what configuration generated the following data.</p>
<dt><code>-H &quot;header: value&quot;</code>, <code>&#8211;header=&quot;Header: value&quot;</code></p>
<dd> This options allows you to set a custom header in the request. Generally speaking, this request will override an existing header. The Cookie header is a special case. If you set -H &#8220;Cookie: value&#8221; then siege will send that cookie in addition to the other ones.</p>
<dt><code>-A &quot;string&quot;</code>, <code>&#8211;agent=&quot;string&quot;</code></p>
<dd> This option allows you to override the default user-agent with a custom one. </p>
<pre>
  siege --agent=&quot;JoeDog Jr. in da hizzle&quot;
</pre>
<p> Will set this header: </p>
<pre>
  User-agent: JoeDog Jr. in da hizzle
</pre>
<p> Alternatively, you could set the User-agent with the -H/&#8211;header option above.</p>
<dt><code>-T &quot;text&quot;</code>, <code>&#8211;content-type=&quot;text&quot;</code></p>
<dd> This is another set header shortcut. You use this option to override the default Content-type request header.</dl>
<h2>URL FORMAT</h2>
<p> <tt>siege</tt> supports <font SIZE="-1">RFC</font> 1738 <font SIZE="-1">URL</font> formats but it takes pains to implement commonly used shortcuts for your convenience. In addition to <font SIZE="-1">RFC</font> 1738 formats, siege introduces its own <font SIZE="-1">URL</font> format to indicate protocol method. </p>
<p> An <font SIZE="-1">RFC</font> 1738 <font SIZE="-1">URL</font> looks like this:<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;scheme&gt;://&lt;username&gt;:&lt;password&gt;@&lt;hostname&gt;:&lt;port&gt;/&lt;path&gt;;&lt;params&gt;?&lt;query&gt;#&lt;frag&gt; </p>
<p> A <tt>siege</tt> <font SIZE="-1">URL</font> with a method idicator looks like this:<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;scheme&gt;://&lt;username&gt;:&lt;password&gt;@&lt;hostname&gt;:&lt;port&gt;/&lt;path&gt;&nbsp;<wbr><font SIZE="-1">POST</font>&nbsp;<wbr>&lt;query&gt; </p>
<p> You can also post the contents of a file using the redirect character like this:<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;scheme&gt;://&lt;username&gt;:&lt;password&gt;@&lt;hostname&gt;:&lt;port&gt;/&lt;path&gt;&nbsp;<wbr><font SIZE="-1">POST</font>&nbsp;<wbr>&lt;/home/jeff/haha.txt </p>
<p> Here&#8217;s two examples with the <tt>siege</tt> method indicator:<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.joedog.org/">http://www.joedog.org/</a>&nbsp;<wbr><font SIZE="-1">POST</font>&nbsp;<wbr>haha=papa&amp;dada=mama<br />
&nbsp;<wbr>&nbsp;<wbr><a href="ftp://ftp.armstrong.com/">ftp://ftp.armstrong.com/</a>&nbsp;<wbr><font SIZE="-1">PUT</font>&nbsp;<wbr>&lt;/home/jdfulmer/etc/tests/bbc.jpg </p>
<p> <font SIZE="-1">NOTE:</font> If you set URLs with method indicators at the command-line, then you <font SIZE="-1">MUST</font> quote the thing or your shell will treat it like three separate arguments. If the <font SIZE="-1">URL</font> is in a urls.txt file, then you shouldn&#8217;t quote it. </p>
<p> As mentioned above, <tt>siege</tt> goes to great lengths to allow commonly used shortcuts that you&#8217;re used to from most browser implementations. It treats many parts of the 1738 <font SIZE="-1">URL</font> as optional. In this example, the parts in brackets are optional:<br />
&nbsp;<wbr>&nbsp;<wbr>[<a href="scheme://]">scheme://]</a>&nbsp;<wbr>host.domain.xxx&nbsp;<wbr>[:port]&nbsp;<wbr>[/path/file] </p>
<p> When <tt>siege</tt> receives a host name it builds the <font SIZE="-1">URL</font> with default assumptions. <a rel="nofollow" href="http://www.joedog.org">www.joedog.org</a> becomes <a href="http://www.joedog.org:80/">http://www.joedog.org:80/</a></p>
<h2>URLS.txt FILE</h2>
<p> From the section called Option Syntax above we learn that <tt>siege</tt> can take a <font SIZE="-1">URL</font> as an argument. <tt>siege</tt> -c -r2 <a rel="nofollow" href="http://www.joedog.org">www.joedog.org</a> will request the JoeDog index page twice. But what if you want to hit large portions of the site? <tt>siege</tt> will allow you to fill a file with URLs so that it can run through list. </p>
<p> The format for the file is one <font SIZE="-1">URL</font> per line:<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://www.joedog.org/">https://www.joedog.org/</a><br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://www.joedog.org/haha/">https://www.joedog.org/haha/</a><br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://www.joedog.org/haha/">https://www.joedog.org/haha/</a>&nbsp;<wbr><font SIZE="-1">POST</font>&nbsp;<wbr>homer=simpson&amp;marge=doestoo </p>
<p> The file also supports UNIX-style commenting:<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Comment looks like this<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://www.joedog.org/">https://www.joedog.org/</a><br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://www.joedog.org/haha/">https://www.joedog.org/haha/</a><br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://www.joedog.org/haha/">https://www.joedog.org/haha/</a>&nbsp;<wbr><font SIZE="-1">POST</font>&nbsp;<wbr>homer=simpson&amp;marge=doestoo </p>
<p> It supports shell-style variable declaration and references. This is convenient if you want to run the same test on two different tiers or two different shemes: </p>
<pre>
  SCHEME=https
  HOST=bart.joedog.org
  $(SCHEME)://$(HOST)/
  $(SCHEME)://$(HOST)/haha/
  $(SCHEME)://$(HOST)/haha/ POST homer=simpson&amp;marge=doestoo
</pre>
<p> You can tell siege about this file with the -f/&#8211;file option:<br />
&nbsp;<wbr>&nbsp;<wbr>siege -c1 -r50 -f&nbsp;<wbr>/home/jeff/urls.txt</p>
<h2>PERFORMANCE STATISTICS</h2>
<p> When its run is complete, siege will gather performance data from all its clients and summarize them after the run. (You can also choose to log these numbers). The command-line output is modeled after Lincoln Stein&#8217;s torture.pl script: </p>
<pre><code>
Transactions : 2000 hits
        Availability : 100.00 %
    Elapsed time : 58.57 secs
        Data transferred : 5.75 MB
            Response time : 0.25 secs
                Transaction rate : 34.15 trans /
    sec
        Throughput : 0.10 MB /
    sec
        Concurrency : 8.45 Successful transactions : 2000 Failed transactions : 0 Longest transaction : 4.62 Shortest transaction : 0.00 Transactions
            This number represents the total number of HTTP requests.In this example,
    we ran 25 simulated users[-c25] and each ran ten times
                                                [-r10]
                                                    .Twenty -
                                            five times ten equals 250 so why is the transaction
                                                total 2000
    ? That's because siege counts every request. This run  included a META redirect,
    a 301 redirect and the page it requested
            contained several elements that were also downloaded.Availability
                This is the percentage of socket connections successfully handled
                    by the server.It is the result of socket
                    failures(including
                                 timeouts) divided by the sum of all connection attempts.This
        number does not include 400 and
        500 level server errors which are
        recorded in "Failed transactions" described below.Elapsed time
        The duration of the entire siege test.This is measured from the
        time the user invokes siege until the last simulated user
        completes its transactions.Shown above,
    the test took 14.67 seconds to complete.Data transferred
    The sum of data transferred to every siege simulated user.It
    includes the header information as well as content.Because it
    includes header information,
    the number reported by siege will
    be larger then the number reported by the server.In internet
    mode,
    which hits random URLs in a configuration file, this number is expected to vary from run to run.Response time The average time it took to respond to each simulated user's requests. Transaction rate The average number of transactions the server was able to handle per second, in a nutshell : it is the count of all transactions divided by elapsed time.Throughput The average number of bytes transferred every second from the server to all the simulated users.Concurrency This is the average number of simultaneous connections.The metric is calculated like this : the sum of all transaction times divided by elapsed time(how long siege ran) Successful transactions The number of times the server responded with a return code &lt; 400. Failed transactions The number of times the socket transactions failed which includes socket timeouts.Longest transaction The greatest amount of time that any single transaction took, out of all transactions.Shortest transaction The smallest amount of time that any single transaction took, out of all transactions.
</code></pre>
<h2>AUTHOR</h2>
<p> <tt>Jeffrey Fulmer, et al.</tt> &lt;jeff [at] joedog.org&gt; is the primary author of <tt>siege</tt>. Numerous people throughout the globe also contributed to this program. Their contributions are noted in the source code ChangeLog</p>
<h2>COPYRIGHT</h2>
<p> Copyright <tt></tt> by <tt>Jeffrey Fulmer, et al.</tt> &lt;jeff [at] joedog.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.</p>
<h2>AVAILABILITY</h2>
<p> The most recent released version of <tt>siege</tt> is available by <font SIZE="-1">HTTP</font> download:<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://download.joedog.org/pub/siege">http://download.joedog.org/pub/siege</a></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-siege-config/">siege.config</a></i>(1) <i><a href="/docs/linux/man/1-bombardment/">bombardment</a></i>(1) <i><a href="/docs/linux/man/1-siege2csv/">siege2csv</a></i>(1) </p>
<h2>Index</h2>
