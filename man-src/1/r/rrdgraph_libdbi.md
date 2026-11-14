---
title: "rrdgraph_libdbi(1)"
name: "rrdgraph_libdbi"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdgraph_libdbi/"
description: "rrdgraph_libdbi – fetching data for graphing in rrdtool graph via libdbi"
---

<h2 class="name">NAME</h2>
<p> rrdgraph_libdbi &#8211; fetching data for graphing in rrdtool graph via libdbi </p>
<h2>SYNOPSIS</h2>
<p> &lt;rrdfile&gt; = <code>sql//&lt;libdbi driver&gt;/&lt;driver-option-name&gt;=&lt;driver-option-value&gt;/&#8230;[/rrdminstepsize=&lt;stepsize&gt;][/rrdfillmissing=&lt;fill missing n seconds&gt;]//&lt;table&gt;/&lt;unixtimestamp column&gt;/&lt;data value column&gt;[/derive]/&lt;where clause 1&gt;/&#8230;/&lt;where clause n&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> This pseudo-rrd-filename defines a sql datasource:</p>
<dl>
<dt><code>sql//</code></p>
<dd>
<pre>
  magic cookie-prefix for a libdbi type datasource
</pre>
<dt><code>&lt;libdbi driver&gt;</code></p>
<dd>
<pre>
  which libdbi driver to use (e.g: mysql)
</pre>
<dt><code>&lt;driver-option-name&gt;</code>=<code>&lt;driver-option-value&gt;</code></p>
<dd>
<pre>
  defines the parameters that are required to connect to the database with the given libdbi driver
  (These drivers are libdbi dependent - for details please look at the driver documentation of libdbi!)
</pre>
<dt><code>/rrdminstepsize</code>=<code>&lt;minimum step size&gt;</code></p>
<dd>
<pre>
  defines the minimum number of the step-length used for graphing (default: 300 seconds)
</pre>
<dt><code>/rrdfillmissing</code>=<code>&lt;fill missing seconds&gt;</code></p>
<dd>
<pre>
  defines the number of seconds to fill with the last value to avoid NaN boxes due to data-insertation jitter (default: 0 seconds)
</pre>
<dt><code>&lt;table&gt;</code></p>
<dd>
<pre>
  defines the table from which to fetch the resultset.
  If there is a need to fetch data from several tables, these tables can be defined by separating the tablenames with a &quot;+&quot;
  hex-type-encoding via %xx are translated to the actual value, use %% to use %
</pre>
<dt><code>&lt;[*]unixtimestamp column&gt;</code></p>
<dd>
<pre>
  defines the column of E&lt;lt&gt;tableE&lt;gt&gt; which contains the unix-timestamp 
  - if this is a DATETIME field in the database, then prefix with leading '*'
  hex-type-encoding via %xx are translated to the actual value, use %% to use %
</pre>
<dt><code>&lt;data value column&gt;</code></p>
<dd>
<pre>
  defines the column of E&lt;lt&gt;tableE&lt;gt&gt; which contains the value column, which should be graphed
  hex-type-encoding via %xx are translated to the actual value, use %% to use %
</pre>
<dt><code>/derive</code></p>
<dd>
<pre>
  defines that the data value used should be the delta of the 2 consecutive values (to simulate COUNTER or DERIVE type datasources)
</pre>
<dt><code>/&lt;where clause(s)&gt;</code></p>
<dd>
<pre>
  defines one (ore more) where clauses that are joined with AND to filter the entries in the &lt;lt&gt;table&lt;gt&gt;
  hex-type-encoding via %xx are translated to the actual value, use %% to use %
</pre>
</dl>
<p> the returned value column-names, which can be used as ds-names, are:</p>
<dl>
<dt><code>min</code>, <code>avg</code>, <code>max</code>, <code>count</code> and <code>sigma</code></p>
<dd>
<pre>
  are returned to be used as ds-names in your DS definition.
  The reason for using this is that if the consolidation function is used for min/avg and max, then the engine is used several times.
  And this results in the same SQL Statements used several times
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> Here an example of a table in a MySQL database: </p>
<pre><code>
DB connect information
    dbhost = 127.0.0.1 user = rrd
        password = secret
            dbname = rrd
                here the table : CREATE TABLE
                                 RRDValue(
                                     RRDKeyID bigint(20) NOT NULL,
                                     UnixTimeStamp int(11) NOT NULL,
                                     value double default NOT NULL,
                                     PRIMARY KEY(RRDKeyID, UnixTimeStamp));
</code></pre>
<p> and the RRDKeyID we want to graph for is: 1141942900757789274 </p>
<p> The pseudo rrd-filename to access this is: &#8220;sql//mysql/host=127.0.0.1/dbname=rrd/username=rrd/password=secret//RRDValue/UnixTimeStamp/value/RRDKeyID=1141464142203608274&#8221; </p>
<p> To illustrate this here a command to create a graph that contains the actual values. </p>
<pre><code>
DS_BASE = "sql//mysql/host=127.0.0.1/dbname=rrd/username=rrd/password=passwd//RRDValue/UnixTimeStamp/value/RRDKeyID=1141942900757789274" rrdtool graph test.png-- imgformat = PNG-- start = -1day --end = +3hours --width = 1000 --height = 600 "DEF:min=$DS_BASE:min:AVERAGE"
                                                                                                                                                                                                                                                "LINE1:min#FF0000:value"
                                                                                                                                                                                                                                                "DEF:avg=$DS_BASE:avg:AVERAGE"
                                                                                                                                                                                                                                                "LINE1:avg#00FF00:average"
                                                                                                                                                                                                                                                "DEF:max=$DS_BASE:max:AVERAGE"
                                                                                                                                                                                                                                                "LINE1:max#FF0000:max"
                                                                                                                                                                                                                                                "DEF:sigma=$DS_BASE:sigma:AVERAGE"
                                                                                                                                                                                                                                                "CDEF:upper=avg,4,sigma,*,+"
                                                                                                                                                                                                                                                "LINE1:upper#0000FF:+4 sigma"
                                                                                                                                                                                                                                                "CDEF:lower=avg,4,sigma,*,-"
                                                                                                                                                                                                                                                "LINE1:lower#0000FF:-4 sigma"
</code></pre>
<h2>NOTES</h2>
<p> * Naturally you can also use any other kind of driver that libdbi supports &#8211; e.g postgres, &#8230; </p>
<p> * From the way the data source is joined, it should also be possible to do joins over different tables<br />
&nbsp;<wbr>&nbsp;<wbr>(separate tables with&nbsp;<wbr>&#8220;,&#8221;&nbsp;<wbr>in table and add in the&nbsp;<wbr><font SIZE="-1">WHERE</font>&nbsp;<wbr>Clauses the table equal joins.&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This has not been tested!!!) </p>
<p> * It should also be relatively simple to add to the database using the same data source string.<br />
&nbsp;<wbr>&nbsp;<wbr>This has not been implemented&#8230; </p>
<p> * The aggregation functions are ignored and several data columns are used instead<br />
&nbsp;<wbr>&nbsp;<wbr>to avoid querying the same&nbsp;<wbr><font SIZE="-1">SQL</font>&nbsp;<wbr>several times when minimum, average and maximum are needed for graphing&#8230; </p>
<p> * for <font SIZE="-1">DB</font> efficiency you should think of having 2 tables, one containing historic values and the other containing the latest data.<br />
&nbsp;<wbr>&nbsp;<wbr>This second table should be kept small to allow for the least ammount of blocking&nbsp;<wbr><font SIZE="-1">SQL</font>&nbsp;<wbr>statements.<br />
&nbsp;<wbr>&nbsp;<wbr>Whith mysql you can even use myisam table-type for the first and InnoDB for the second.&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This is especially interresting as with tables with&nbsp;<wbr>+100M rows myisam is much smaller then InnoDB. </p>
<p> * To debug the <font SIZE="-1">SQL</font> statements set the environment variable <font SIZE="-1">RRDDEBUGSQL</font> and the actual <font SIZE="-1">SQL</font> statements and the timing is printed to stderr.</p>
<h2>Performance issues with MySQL backend</h2>
<p> LibDBI has a big performance issue when you retrieve data from a MySQL server. Performance impact is exponentially based on the number of values you retrieve from the database. For example, it would take more than 2 seconds to graph 5DS on 150 hours of data with a precision of 5 minutes (against 100ms when data comes from a <font SIZE="-1">RRD</font> file). This bug has been fixed on latest version of LibDBI (not release yet). At that time, you would need to compile libdbi and libdbi-drivers from <font SIZE="-1">CVS</font> repository to fix it. You can find more informations on this libdbi-users mailing list thread : <a rel="nofollow" href="http://sourceforge.net/mailarchive/message.php?msg_id=30320894">http://sourceforge.net/mailarchive/message.php?msg_id=30320894</a></p>
<h2>BUGS</h2>
<p> * at least on Linux please make sure that the libdbi driver is explicitly linked against libdbi.so.0<br />
&nbsp;<wbr>&nbsp;<wbr>check via ldd&nbsp;<wbr>/usr/lib/dbd/libmysql.so, that there is a line with libdbi.so.0.&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>otherwise at least the perl module RRDs will fail because the dynamic linker can not find some symbols from libdbi.so.<br />
&nbsp;<wbr>&nbsp;<wbr>(this only happens when the libdbi driver is actually used the first time!)<br />
&nbsp;<wbr>&nbsp;<wbr>This is&nbsp;<wbr><font SIZE="-1">KNOWN</font>&nbsp;<wbr>to be the case with&nbsp;<wbr><font SIZE="-1">RHEL4</font>&nbsp;<wbr>and&nbsp;<wbr><font SIZE="-1">FC4</font>&nbsp;<wbr>and&nbsp;<wbr><font SIZE="-1">FC5</font>!&nbsp;<wbr>(But actually this is a bug with libdbi make files!) </p>
<p> * at least version 0.8.1 of libdbi exhibits a bug with <font SIZE="-1">BINARY</font> fields<br />
&nbsp;<wbr>&nbsp;<wbr>(shorttext,text,mediumtext,longtext and possibly also&nbsp;<wbr><font SIZE="-1">BINARY</font>&nbsp;<wbr>and&nbsp;<wbr><font SIZE="-1">BLOB</font>&nbsp;<wbr>fields),&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>that can result in coredumps of rrdtool.&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>The tool will tell you on stderr if this occures, so that you know what may be the reason.<br />
&nbsp;<wbr>&nbsp;<wbr>If you are not experiencing these coredumps, then set the environment variable&nbsp;<wbr><font SIZE="-1">RRD_NO_LIBDBI_BUG_WARNING,&nbsp;<wbr><br />
&nbsp;<wbr></font>&nbsp;<wbr>and then the message will not get shown.</p>
<h2>AUTHOR</h2>
<p> Martin Sperl &lt;rrdtool [at] martin.sperl.org&gt; </p>
<h2>Index</h2>
