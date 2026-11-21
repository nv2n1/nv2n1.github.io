---

title: "rrdtool(1)"
name: "rrdtool"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdtool/"
description: "rrdtool – Round Robin Database Tool"
---

<p> <code>rrdtool</code> <code>&#8211;</code> [workdir]| <i>function</i></p>
<h3><font SIZE="-1">OVERVIEW</font></h3>
<p> It is pretty easy to gather status information from all sorts of things, ranging from the temperature in your office to the number of octets which have passed through the <font SIZE="-1">FDDI</font> interface of your router. But it is not so trivial to store this data in an efficient and systematic manner. This is where <code>RRDtool</code> comes in handy. It lets you <i>log and analyze</i> the data you gather from all kinds of data-sources (<font SIZE="-1"><code>DS</code></font>). The data analysis part of RRDtool is based on the ability to quickly generate graphical representations of the data values collected over a definable time period. </p>
<p> In this man page you will find general information on the design and functionality of the Round Robin Database Tool (RRDtool). For a more detailed description of how to use the individual functions of <code>RRDtool</code> check the corresponding man page. </p>
<p> For an introduction to the usage of RRDtool make sure you consult the rrdtutorial.</p>
<h3><font SIZE="-1">FUNCTIONS</font></h3>
<p> While the man pages talk of command line switches you have to set in order to make <code>RRDtool</code> work it is important to note that <code>RRDtool</code> can be remotely controlled through a set of pipes. This saves a considerable amount of startup time when you plan to make <code>RRDtool</code> do a lot of things quickly. Check the section on Remote_Control further down. There is also a number of language bindings for RRDtool which allow you to use it directly from Perl, python, Tcl, <font SIZE="-1">PHP</font>, etc.</p>
<dl>
<dt><code>create</code></dt>
<dd> Set up a new Round Robin Database (<font SIZE="-1">RRD</font>). Check rrdcreate.</dd>
<dt><code>update</code></dt>
<dd> Store new data values into an <font SIZE="-1">RRD</font>. Check rrdupdate.</dd>
<dt><code>updatev</code></dt>
<dd> Operationally equivalent to <code>update</code> except for output. Check rrdupdate.</dd>
<dt><code>graph</code></dt>
<dd> Create a graph from data stored in one or several RRDs. Apart from generating graphs, data can also be extracted to stdout. Check rrdgraph.</dd>
<dt><code>graphv</code></dt>
<dd> Create a graph from data stored in one or several RRDs. Same as graph, but metadata are printed before the graph. Check rrdgraph.</dd>
<dt><code>dump</code></dt>
<dd> Dump the contents of an <font SIZE="-1">RRD</font> in plain <font SIZE="-1">ASCII</font>. In connection with restore you can use this to move an <font SIZE="-1">RRD</font> from one computer architecture to another. Check rrddump.</dd>
<dt><code>restore</code></dt>
<dd> Restore an <font SIZE="-1">RRD</font> in <font SIZE="-1">XML</font> format to a binary <font SIZE="-1">RRD</font>. Check rrdrestore</dd>
<dt><code>fetch</code></dt>
<dd> Get data for a certain time period from a <font SIZE="-1">RRD</font>. The graph function uses fetch to retrieve its data from an <font SIZE="-1">RRD</font>. Check rrdfetch.</dd>
<dt><code>tune</code></dt>
<dd> Alter setup of an <font SIZE="-1">RRD</font>. Check rrdtune.</dd>
<dt><code>first</code></dt>
<dd> Find the first update time of an <font SIZE="-1">RRD</font>. Check rrdfirst.</dd>
<dt><code>last</code></dt>
<dd> Find the last update time of an <font SIZE="-1">RRD</font>. Check rrdlast.</dd>
<dt><code>lastupdate</code></dt>
<dd> Find the last update time of an <font SIZE="-1">RRD</font>. It also returns the value stored for each datum in the most recent update. Check rrdlastupdate.</dd>
<dt><code>info</code></dt>
<dd> Get information about an <font SIZE="-1">RRD</font>. Check rrdinfo.</dd>
<dt><code>resize</code></dt>
<dd> Change the size of individual RRAs. This is dangerous! Check rrdresize.</dd>
<dt><code>xport</code></dt>
<dd> Export data retrieved from one or several RRDs. Check rrdxport.</dd>
<dt><code>flushcached</code></dt>
<dd> Flush the values for a specific <font SIZE="-1">RRD</font> file from memory. Check rrdflushcached.</dd></dl>
<h3><font SIZE="-1">HOW</font> <font SIZE="-1">DOES</font> <font SIZE="-1">RRDTOOL</font> <font SIZE="-1">WORK</font>?</h3>
<dl>
<dt>Data Acquisition</dt>
<dd> When monitoring the state of a system, it is convenient to have the data available at a constant time interval. Unfortunately, you may not always be able to fetch data at exactly the time you want to. Therefore <code>RRDtool</code> lets you update the log file at any time you want. It will automatically interpolate the value of the data-source (<font SIZE="-1"><code>DS</code></font>) at the latest official time-slot (interval) and write this interpolated value to the log. The original value you have supplied is stored as well and is also taken into account when interpolating the next log entry.</dd>
<dt>Consolidation</dt>
<dd> You may log data at a 1 minute interval, but you might also be interested to know the development of the data over the last year. You could do this by simply storing the data in 1 minute intervals for the whole year. While this would take considerable disk space it would also take a lot of time to analyze the data when you wanted to create a graph covering the whole year. <code>RRDtool</code> offers a solution to this problem through its data consolidation feature. When setting up an Round Robin Database (<font SIZE="-1"><code>RRD</code></font>), you can define at which interval this consolidation should occur, and what consolidation function (<font SIZE="-1"><code>CF</code></font>) (average, minimum, maximum, total, last) should be used to build the consolidated values (see rrdcreate). You can define any number of different consolidation setups within one <font SIZE="-1"><code>RRD</code></font>. They will all be maintained on the fly when new data is loaded into the <font SIZE="-1"><code>RRD</code></font>.</dd>
<dt>Round Robin Archives</dt>
<dd> Data values of the same consolidation setup are stored into Round Robin Archives (<font SIZE="-1"><code>RRA</code></font>). This is a very efficient manner to store data for a certain amount of time, while using a known and constant amount of storage space. </dd>
<p> It works like this: If you want to store 1&#8217;000 values in 5 minute interval, <code>RRDtool</code> will allocate space for 1&#8217;000 data values and a header area. In the header it will store a pointer telling which slots (value) in the storage area was last written to. New values are written to the Round Robin Archive in, you guessed it, a round robin manner. This automatically limits the history to the last 1&#8217;000 values (in our example). Because you can define several <font SIZE="-1"><code>RRA</code></font>s within a single <font SIZE="-1"><code>RRD</code></font>, you can setup another one, for storing 750 data values at a 2 hour interval, for example, and thus keep a log for the last two months at a lower resolution. </p>
<p> The use of <font SIZE="-1"><code>RRA</code></font>s guarantees that the <font SIZE="-1"><code>RRD</code></font> does not grow over time and that old data is automatically eliminated. By using the consolidation feature, you can still keep data for a very long time, while gradually reducing the resolution of the data along the time axis. </p>
<p> Using different consolidation functions (<font SIZE="-1"><code>CF</code></font>) allows you to store exactly the type of information that actually interests you: the maximum one minute traffic on the <font SIZE="-1">LAN</font>, the minimum temperature of your wine cellar, the total minutes of down time, etc.</p>
<dt>Unknown Data</dt>
<dd> As mentioned earlier, the <font SIZE="-1"><code>RRD</code></font> stores data at a constant interval. Sometimes it may happen that no new data is available when a value has to be written to the <font SIZE="-1"><code>RRD</code></font>. Data acquisition may not be possible for one reason or other. With <code>RRDtool</code> you can handle these situations by storing an <i>*UNKNOWN*</i> value into the database. The value &#8216;<i>*UNKNOWN*</i>&#8216; is supported through all the functions of the tool. When consolidating a data set, the amount of <i>*UNKNOWN*</i> data values is accounted for and when a new consolidated value is ready to be written to its Round Robin Archive (<font SIZE="-1"><code>RRA</code></font>), a validity check is performed to make sure that the percentage of unknown values in the data point is above a configurable level. If not, an <i>*UNKNOWN*</i> value will be written to the <font SIZE="-1"><code>RRA</code></font>.</dd>
<dt>Graphing</dt>
<dd> <code>RRDtool</code> allows you to generate reports in numerical and graphical form based on the data stored in one or several <font SIZE="-1"><code>RRD</code></font>s. The graphing feature is fully configurable. Size, color and contents of the graph can be defined freely. Check rrdgraph for more information on this.</dd>
<dt>Aberrant Behavior Detection</dt>
<dd> by Jake Brutlag </dd>
<p> <code>RRDtool</code> provides the building blocks for near real-time aberrant behavior detection. These components include:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> An algorithm for predicting the value of a time series one time step into the future.</dd>
<dt>&bull;</dt>
<dd> A measure of deviation between predicted and observed values.</dd>
<dt>&bull;</dt>
<dd> A mechanism to decide if and when an observed value or sequence of observed values is <i>too deviant</i> from the predicted value(s).</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Here is a brief explanation of these components: </p>
<p> The Holt-Winters time series forecasting algorithm is an on-line (or incremental) algorithm that adaptively predicts future observations in a time series. Its forecast is the sum of three components: a baseline (or intercept), a linear trend over time (or slope), and a seasonal coefficient (a periodic effect, such as a daily cycle). There is one seasonal coefficient for each time point in the period (cycle). After a value is observed, each of these components is updated via exponential smoothing. This means that the algorithm &#8220;learns&#8221; from past values and uses them to predict the future. The rate of adaptation is governed by 3 parameters, alpha (intercept), beta (slope), and gamma (seasonal). The prediction can also be viewed as a smoothed value for the time series. </p>
<p> The measure of deviation is a seasonal weighted absolute deviation. The term <i>seasonal</i> means deviation is measured separately for each time point in the seasonal cycle. As with Holt-Winters forecasting, deviation is predicted using the measure computed from past values (but only at that point in the seasonal cycle). After the value is observed, the algorithm learns from the observed value via exponential smoothing. Confidence bands for the observed time series are generated by scaling the sequence of predicted deviation values (we usually think of the sequence as a continuous line rather than a set of discrete points). </p>
<p> Aberrant behavior (a potential failure) is reported whenever the number of times the observed value violates the confidence bands meets or exceeds a specified threshold within a specified temporal window (e.g. 5 violations during the past 45 minutes with a value observed every 5 minutes). </p>
<p> This functionality is embedded in a set of related <code>RRAs</code>. In particular, a <font SIZE="-1">FAILURES</font> <font SIZE="-1"><code>RRA</code></font> logs potential failures. With these data you could, for example, use a front-end application to <code>RRDtool</code> to initiate real-time alerts. </p>
<p> For a detailed description on how to set this up, see rrdcreate.</dd></dl>
</dl>
<h3><font SIZE="-1">REMOTE</font> <font SIZE="-1">CONTROL</font></h3>
<p> When you start <code>RRDtool</code> with the command line option &#8216;<code>&#8211;</code>&#8216; it waits for input via standard input (<font SIZE="-1">STDIN</font>). With this feature you can improve performance by attaching <code>RRDtool</code> to another process (<font SIZE="-1">MRTG</font> is one example) through a set of pipes. Over these pipes <code>RRDtool</code> accepts the same arguments as on the command line and some special commands like <code>quit, cd, mkdir</code> and <code>ls</code>. For detailed help on the server commands type: </p>
<pre>
   rrdtool help cd|mkdir|pwd|ls|quit
</pre>
<p> When a command is completed, RRDtool will print the string &#8216;<tt>&quot;OK&quot;</tt>&#8216;, followed by timing information of the form <code>u:</code><i>usertime</i> <code>s:</code><i>systemtime</i>. Both values are the running totals of seconds since RRDtool was started. If an error occurs, a line of the form &#8216;<tt>&quot;ERROR:&quot;</tt> <i>Description of error</i>&#8216; will be printed instead. <code>RRDtool</code> will not abort, unless something really serious happens. If a <code>workdir</code> is specified and the <font SIZE="-1">UID</font> is 0, RRDtool will do a chroot to that workdir. If the <font SIZE="-1">UID</font> is not 0, RRDtool only changes the current directory to <code>workdir</code>.</p>
<h3><font SIZE="-1">RRD</font> Server</h3>
<p> If you want to create a RRD-Server, you must choose a <font SIZE="-1">TCP/IP</font> Service number and add them to <i>/etc/services</i> like this: </p>
<pre>
 rrdsrv      13900/tcp                       # RRD server
</pre>
<p> Attention: the <font SIZE="-1">TCP</font> port 13900 isn&#8217;t officially registered for rrdsrv. You can use any unused port in your services file, but the server and the client system must use the same port, of course. </p>
<p> With this configuration you can add RRDtool as meta-server to <i>/etc/inetd.conf</i>. For example: </p>
<pre>
 rrdsrv stream tcp nowait root /opt/rrd/bin/rrdtool rrdtool - /var/rrd
</pre>
<p> Don&#8217;t forget to create the database directory /var/rrd and reinitialize your inetd. </p>
<p> If all was setup correctly, you can access the server with Perl sockets, tools like netcat, or in a quick interactive test by using &#8216;telnet localhost rrdsrv&#8217;. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> that there is no authentication with this feature! Do not setup such a port unless you are sure what you are doing.</p>
<h2>RRDCACHED, THE CACHING DAEMON</h2>
<p> For very big setups, updating thousands of <font SIZE="-1">RRD</font> files often becomes a serious <font SIZE="-1">IO</font> problem. If you run into such problems, you might want to take a look at rrdcached, a caching daemon for RRDtool which may help you lessen the stress on your disks.</p>
<h2>SEE ALSO</h2>
<p> rrdcreate, rrdupdate, rrdgraph, rrddump, rrdfetch, rrdtune, rrdlast, rrdxport, rrdflushcached, rrdcached</p>
<h2>BUGS</h2>
<p> Bugs? Features!</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
