---

title: "rrdcreate(1)"
name: "rrdcreate"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdcreate/"
description: "rrdcreate – Set up a new Round Robin Database"
---

<p> rrdcreate &#8211; Set up a new Round Robin Database </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>create</code> <i>filename</i> [<code>&#8211;start</code>|<code>-b</code>&nbsp;<wbr><i>start time</i>] [<code>&#8211;step</code>|<code>-s</code>&nbsp;<wbr><i>step</i>] [<code>&#8211;no-overwrite</code>] [<code>DS:</code><i>ds-name</i><code>:</code><i></i><i>DST</i><i></i><code>:</code><i>dst arguments</i>] [<code>RRA:</code><i></i><i>CF</i><i></i><code>:</code><i>cf arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> The create function of RRDtool lets you set up new Round Robin Database (<code>RRD</code>) files. The file is created at its final, full size and filled with <i>*UNKNOWN*</i> data.</p>
<h3><i>filename</i></h3>
<p> The name of the <code>RRD</code> you want to create. <code>RRD</code> files should end with the extension <i>.rrd</i>. However, <code>RRDtool</code> will accept any filename.</p>
<h3><code>&#8211;start</code>|<code>-b</code> <i>start time</i> (default: now &#8211; 10s)</h3>
<p> Specifies the time in seconds since 1970-01-01 UTC when the first value should be added to the <code>RRD</code>. <code>RRDtool</code> will not accept any data timed before or at the time specified. </p>
<p> See also AT-STYLE TIME SPECIFICATION section in the <i>rrdfetch</i> documentation for other ways to specify time.</p>
<h3><code>&#8211;step</code>|<code>-s</code> <i>step</i> (default: 300 seconds)</h3>
<p> Specifies the base interval in seconds with which data will be fed into the <code>RRD</code>.</p>
<h3><code>&#8211;no-overwrite</code></h3>
<p> Do not clobber an existing file of the same name.</p>
<h3><code>DS:</code><i>ds-name</i><code>:</code><i></i><i>DST</i><i></i><code>:</code><i>dst arguments</i></h3>
<p> A single <code>RRD</code> can accept input from several data sources (<code>DS</code>), for example incoming and outgoing traffic on a specific communication line. With the <code>DS</code> configuration option you must define some basic properties of each data source you want to store in the <code>RRD</code>. </p>
<p> <i>ds-name</i> is the name you will use to reference this particular data source from an <code>RRD</code>. A <i>ds-name</i> must be 1 to 19 characters long in the characters [a-zA-Z0-9_]. </p>
<p> <i></i><i>DST</i><i></i> defines the Data Source Type. The remaining arguments of a data source entry depend on the data source type. For GAUGE, COUNTER, DERIVE, and ABSOLUTE the format for a data source entry is: </p>
<p> <code>DS:</code><i>ds-name</i><code>:</code><i></i><i>GAUGE</i><i> | </i><i>COUNTER</i><i> | </i><i>DERIVE</i><i> | </i><i>ABSOLUTE</i><i></i><code>:</code><i>heartbeat</i><code>:</code><i>min</i><code>:</code><i>max</i> </p>
<p> For COMPUTE data sources, the format is: </p>
<p> <code>DS:</code><i>ds-name</i><code>:</code><i></i><i>COMPUTE</i><i></i><code>:</code><i>rpn-expression</i> </p>
<p> In order to decide which data source type to use, review the definitions that follow. Also consult the section on &#8220;HOW TO MEASURE&#8221; for further insight.</p>
<dl>
<dt><code>GAUGE</code></dt>
<dd> is for things like temperatures or number of people in a room or the value of a RedHat share.</dd>
<dt><code>COUNTER</code></dt>
<dd> is for continuous incrementing counters like the ifInOctets counter in a router. The <code>COUNTER</code> data source assumes that the counter never decreases, except when a counter overflows. The update function takes the overflow into account. The counter is stored as a per-second rate. When the counter overflows, RRDtool checks if the overflow happened at the 32bit or 64bit border and acts accordingly by adding an appropriate value to the result.</dd>
<dt><code>DERIVE</code></dt>
<dd> will store the derivative of the line going from the last to the current value of the data source. This can be useful for gauges, for example, to measure the rate of people entering or leaving a room. Internally, derive works exactly like COUNTER but without overflow checks. So if your counter does not reset at 32 or 64 bit you might want to use DERIVE and combine it with a MIN value of 0. </dd>
<p> <code>NOTE</code><code> on </code><code>COUNTER</code><code> vs </code><code>DERIVE</code> </p>
<p> by Don Baarda &lt;don.baarda [at] baesystems.com&gt; </p>
<p> If you cannot tolerate ever mistaking the occasional counter reset for a legitimate counter wrap, and would prefer &#8220;Unknowns&#8221; for all legitimate counter wraps and resets, always use DERIVE with min=0. Otherwise, using COUNTER with a suitable max will return correct values for all legitimate counter wraps, mark some counter resets as &#8220;Unknown&#8221;, but can mistake some counter resets for a legitimate counter wrap. </p>
<p> For a 5 minute step and 32-bit counter, the probability of mistaking a counter reset for a legitimate wrap is arguably about 0.8% per 1Mbps of maximum bandwidth. Note that this equates to 80% for 100Mbps interfaces, so for high bandwidth interfaces and a 32bit counter, DERIVE with min=0 is probably preferable. If you are using a 64bit counter, just about any max setting will eliminate the possibility of mistaking a reset for a counter wrap.</p>
<dt><code>ABSOLUTE</code></dt>
<dd> is for counters which get reset upon reading. This is used for fast counters which tend to overflow. So instead of reading them normally you reset them after every read to make sure you have a maximum time available before the next overflow. Another usage is for things you count like number of messages since the last update.</dd>
<dt><code>COMPUTE</code></dt>
<dd> is for storing the result of a formula applied to other data sources in the <code>RRD</code>. This data source is not supplied a value on update, but rather its Primary Data Points (PDPs) are computed from the PDPs of the data sources according to the rpn-expression that defines the formula. Consolidation functions are then applied normally to the PDPs of the COMPUTE data source (that is the rpn-expression is only applied to generate PDPs). In database software, such data sets are referred to as &#8220;virtual&#8221; or &#8220;computed&#8221; columns.</dd></dl>
<p> <i>heartbeat</i> defines the maximum number of seconds that may pass between two updates of this data source before the value of the data source is assumed to be <i>*UNKNOWN*</i>. </p>
<p> <i>min</i> and <i>max</i> define the expected range values for data supplied by a data source. If <i>min</i> and/or <i>max</i> are specified any value outside the defined range will be regarded as <i>*UNKNOWN*</i>. If you do not know or care about min and max, set them to U for unknown. Note that min and max always refer to the processed values of the DS. For a traffic-<code>COUNTER</code> type DS this would be the maximum and minimum data-rate expected from the device. </p>
<p> <i>If information on minimal/maximal expected values is available, always set the min and/or max properties. This will help RRDtool in doing a simple sanity check on the data supplied when running update.</i> </p>
<p> <i>rpn-expression</i> defines the formula used to compute the PDPs of a COMPUTE data source from other data sources in the same &lt;RRD&gt;. It is similar to defining a <code>CDEF</code> argument for the graph command. Please refer to that manual page for a list and description of RPN operations supported. For COMPUTE data sources, the following RPN operations are not supported: COUNT, PREV, TIME, and LTIME. In addition, in defining the RPN expression, the COMPUTE data source may only refer to the names of data source listed previously in the create command. This is similar to the restriction that <code>CDEF</code>s must refer only to <code>DEF</code>s and <code>CDEF</code>s previously defined in the same graph command.</p>
<h3><code>RRA:</code><i></i><i>CF</i><i></i><code>:</code><i>cf arguments</i></h3>
<p> The purpose of an <code>RRD</code> is to store data in the round robin archives (<code>RRA</code>). An archive consists of a number of data values or statistics for each of the defined data-sources (<code>DS</code>) and is defined with an <code>RRA</code> line. </p>
<p> When data is entered into an <code>RRD</code>, it is first fit into time slots of the length defined with the <code>-s</code> option, thus becoming a <i>primary data point</i>. </p>
<p> The data is also processed with the consolidation function (<i></i><i>CF</i><i></i>) of the archive. There are several consolidation functions that consolidate primary data points via an aggregate function: <code>AVERAGE</code>, <code>MIN</code>, <code>MAX</code>, <code>LAST</code>.</p>
<dl>
<dt>AVERAGE</dt>
<dd> the average of the data points is stored.</dd>
<dt>MIN</dt>
<dd> the smallest of the data points is stored.</dd>
<dt>MAX</dt>
<dd> the largest of the data points is stored.</dd>
<dt>LAST</dt>
<dd> the last data points is used.</dd></dl>
<p> Note that data aggregation inevitably leads to loss of precision and information. The trick is to pick the aggregate function such that the <i>interesting</i> properties of your data is kept across the aggregation process. </p>
<p> The format of <code>RRA</code> line for these consolidation functions is: </p>
<p> <code>RRA:</code><i></i><i>AVERAGE</i><i> | </i><i>MIN</i><i> | </i><i>MAX</i><i> | </i><i>LAST</i><i></i><code>:</code><i>xff</i><code>:</code><i>steps</i><code>:</code><i>rows</i> </p>
<p> <i>xff</i> The xfiles factor defines what part of a consolidation interval may be made up from <i>*UNKNOWN*</i> data while the consolidated value is still regarded as known. It is given as the ratio of allowed <i>*UNKNOWN*</i> PDPs to the number of PDPs in the interval. Thus, it ranges from 0 to 1 (exclusive). </p>
<p> <i>steps</i> defines how many of these <i>primary data points</i> are used to build a <i>consolidated data point</i> which then goes into the archive. </p>
<p> <i>rows</i> defines how many generations of data values are kept in an <code>RRA</code>. Obviously, this has to be greater than zero.</p>
<h2>Aberrant Behavior Detection with Holt-Winters Forecasting</h2>
<p> In addition to the aggregate functions, there are a set of specialized functions that enable <code>RRDtool</code> to provide data smoothing (via the Holt-Winters forecasting algorithm), confidence bands, and the flagging aberrant behavior in the data source time series:</p>
<dl>
<dt>&bull;</dt>
<dd> <code>RRA:</code><i></i><i>HWPREDICT</i><i></i><code>:</code><i>rows</i><code>:</code><i>alpha</i><code>:</code><i>beta</i><code>:</code><i>seasonal period</i>[<code>:</code><i>rra-num</i>]</dd>
<dt>&bull;</dt>
<dd> <code>RRA:</code><i></i><i>MHWPREDICT</i><i></i><code>:</code><i>rows</i><code>:</code><i>alpha</i><code>:</code><i>beta</i><code>:</code><i>seasonal period</i>[<code>:</code><i>rra-num</i>]</dd>
<dt>&bull;</dt>
<dd> <code>RRA:</code><i></i><i>SEASONAL</i><i></i><code>:</code><i>seasonal period</i><code>:</code><i>gamma</i><code>:</code><i>rra-num</i>[<code>:smoothing-window=</code><i>fraction</i>]</dd>
<dt>&bull;</dt>
<dd> <code>RRA:</code><i></i><i>DEVSEASONAL</i><i></i><code>:</code><i>seasonal period</i><code>:</code><i>gamma</i><code>:</code><i>rra-num</i>[<code>:smoothing-window=</code><i>fraction</i>]</dd>
<dt>&bull;</dt>
<dd> <code>RRA:</code><i></i><i>DEVPREDICT</i><i></i><code>:</code><i>rows</i><code>:</code><i>rra-num</i></dd>
<dt>&bull;</dt>
<dd> <code>RRA:</code><i></i><i>FAILURES</i><i></i><code>:</code><i>rows</i><code>:</code><i>threshold</i><code>:</code><i>window length</i><code>:</code><i>rra-num</i></dd></dl>
<p> These <code>RRAs</code> differ from the true consolidation functions in several ways. First, each of the <code>RRA</code>s is updated once for every primary data point. Second, these <code>RRAs</code> are interdependent. To generate real-time confidence bounds, a matched set of SEASONAL, DEVSEASONAL, DEVPREDICT, and either HWPREDICT or MHWPREDICT must exist. Generating smoothed values of the primary data points requires a SEASONAL <code>RRA</code> and either an HWPREDICT or MHWPREDICT <code>RRA</code>. Aberrant behavior detection requires FAILURES, DEVSEASONAL, SEASONAL, and either HWPREDICT or MHWPREDICT. </p>
<p> The predicted, or smoothed, values are stored in the HWPREDICT or MHWPREDICT <code>RRA</code>. HWPREDICT and MHWPREDICT are actually two variations on the Holt-Winters method. They are interchangeable. Both attempt to decompose data into three components: a baseline, a trend, and a seasonal coefficient. HWPREDICT adds its seasonal coefficient to the baseline to form a prediction, whereas MHWPREDICT multiplies its seasonal coefficient by the baseline to form a prediction. The difference is noticeable when the baseline changes significantly in the course of a season; HWPREDICT will predict the seasonality to stay constant as the baseline changes, but MHWPREDICT will predict the seasonality to grow or shrink in proportion to the baseline. The proper choice of method depends on the thing being modeled. For simplicity, the rest of this discussion will refer to HWPREDICT, but MHWPREDICT may be substituted in its place. </p>
<p> The predicted deviations are stored in DEVPREDICT (think a standard deviation which can be scaled to yield a confidence band). The FAILURES <code>RRA</code> stores binary indicators. A 1 marks the indexed observation as failure; that is, the number of confidence bounds violations in the preceding window of observations met or exceeded a specified threshold. An example of using these <code>RRAs</code> to graph confidence bounds and failures appears in rrdgraph. </p>
<p> The SEASONAL and DEVSEASONAL <code>RRAs</code> store the seasonal coefficients for the Holt-Winters forecasting algorithm and the seasonal deviations, respectively. There is one entry per observation time point in the seasonal cycle. For example, if primary data points are generated every five minutes and the seasonal cycle is 1 day, both SEASONAL and DEVSEASONAL will have 288 rows. </p>
<p> In order to simplify the creation for the novice user, in addition to supporting explicit creation of the HWPREDICT, SEASONAL, DEVPREDICT, DEVSEASONAL, and FAILURES <code>RRAs</code>, the <code>RRDtool</code> create command supports implicit creation of the other four when HWPREDICT is specified alone and the final argument <i>rra-num</i> is omitted. </p>
<p> <i>rows</i> specifies the length of the <code>RRA</code> prior to wrap around. Remember that there is a one-to-one correspondence between primary data points and entries in these RRAs. For the HWPREDICT CF, <i>rows</i> should be larger than the <i>seasonal period</i>. If the DEVPREDICT <code>RRA</code> is implicitly created, the default number of rows is the same as the HWPREDICT <i>rows</i> argument. If the FAILURES <code>RRA</code> is implicitly created, <i>rows</i> will be set to the <i>seasonal period</i> argument of the HWPREDICT <code>RRA</code>. Of course, the <code>RRDtool</code> <i>resize</i> command is available if these defaults are not sufficient and the creator wishes to avoid explicit creations of the other specialized function <code>RRAs</code>. </p>
<p> <i>seasonal period</i> specifies the number of primary data points in a seasonal cycle. If SEASONAL and DEVSEASONAL are implicitly created, this argument for those <code>RRAs</code> is set automatically to the value specified by HWPREDICT. If they are explicitly created, the creator should verify that all three <i>seasonal period</i> arguments agree. </p>
<p> <i>alpha</i> is the adaption parameter of the intercept (or baseline) coefficient in the Holt-Winters forecasting algorithm. See rrdtool for a description of this algorithm. <i>alpha</i> must lie between 0 and 1. A value closer to 1 means that more recent observations carry greater weight in predicting the baseline component of the forecast. A value closer to 0 means that past history carries greater weight in predicting the baseline component. </p>
<p> <i>beta</i> is the adaption parameter of the slope (or linear trend) coefficient in the Holt-Winters forecasting algorithm. <i>beta</i> must lie between 0 and 1 and plays the same role as <i>alpha</i> with respect to the predicted linear trend. </p>
<p> <i>gamma</i> is the adaption parameter of the seasonal coefficients in the Holt-Winters forecasting algorithm (HWPREDICT) or the adaption parameter in the exponential smoothing update of the seasonal deviations. It must lie between 0 and 1. If the SEASONAL and DEVSEASONAL <code>RRAs</code> are created implicitly, they will both have the same value for <i>gamma</i>: the value specified for the HWPREDICT <i>alpha</i> argument. Note that because there is one seasonal coefficient (or deviation) for each time point during the seasonal cycle, the adaptation rate is much slower than the baseline. Each seasonal coefficient is only updated (or adapts) when the observed value occurs at the offset in the seasonal cycle corresponding to that coefficient. </p>
<p> If SEASONAL and DEVSEASONAL <code>RRAs</code> are created explicitly, <i>gamma</i> need not be the same for both. Note that <i>gamma</i> can also be changed via the <code>RRDtool</code> <i>tune</i> command. </p>
<p> <i>smoothing-window</i> specifies the fraction of a season that should be averaged around each point. By default, the value of <i>smoothing-window</i> is 0.05, which means each value in SEASONAL and DEVSEASONAL will be occasionally replaced by averaging it with its (<i>seasonal period</i>*0.05) nearest neighbors. Setting <i>smoothing-window</i> to zero will disable the running-average smoother altogether. </p>
<p> <i>rra-num</i> provides the links between related <code>RRAs</code>. If HWPREDICT is specified alone and the other <code>RRAs</code> are created implicitly, then there is no need to worry about this argument. If <code>RRAs</code> are created explicitly, then carefully pay attention to this argument. For each <code>RRA</code> which includes this argument, there is a dependency between that <code>RRA</code> and another <code>RRA</code>. The <i>rra-num</i> argument is the 1-based index in the order of <code>RRA</code> creation (that is, the order they appear in the <i>create</i> command). The dependent <code>RRA</code> for each <code>RRA</code> requiring the <i>rra-num</i> argument is listed here:</p>
<dl>
<dt>&bull;</dt>
<dd> HWPREDICT <i>rra-num</i> is the index of the SEASONAL <code>RRA</code>.</dd>
<dt>&bull;</dt>
<dd> SEASONAL <i>rra-num</i> is the index of the HWPREDICT <code>RRA</code>.</dd>
<dt>&bull;</dt>
<dd> DEVPREDICT <i>rra-num</i> is the index of the DEVSEASONAL <code>RRA</code>.</dd>
<dt>&bull;</dt>
<dd> DEVSEASONAL <i>rra-num</i> is the index of the HWPREDICT <code>RRA</code>.</dd>
<dt>&bull;</dt>
<dd> FAILURES <i>rra-num</i> is the index of the DEVSEASONAL <code>RRA</code>.</dd></dl>
<p> <i>threshold</i> is the minimum number of violations (observed values outside the confidence bounds) within a window that constitutes a failure. If the FAILURES <code>RRA</code> is implicitly created, the default value is 7. </p>
<p> <i>window length</i> is the number of time points in the window. Specify an integer greater than or equal to the threshold and less than or equal to 28. The time interval this window represents depends on the interval between primary data points. If the FAILURES <code>RRA</code> is implicitly created, the default value is 9.</p>
<h2>The HEARTBEAT and the STEP</h2>
<p> Here is an explanation by Don Baarda on the inner workings of RRDtool. It may help you to sort out why all this *UNKNOWN* data is popping up in your databases: </p>
<p> RRDtool gets fed samples/updates at arbitrary times. From these it builds Primary Data Points (PDPs) on every &#8220;step&#8221; interval. The PDPs are then accumulated into the RRAs. </p>
<p> The &#8220;heartbeat&#8221; defines the maximum acceptable interval between samples/updates. If the interval between samples is less than &#8220;heartbeat&#8221;, then an average rate is calculated and applied for that interval. If the interval between samples is longer than &#8220;heartbeat&#8221;, then that entire interval is considered &#8220;unknown&#8221;. Note that there are other things that can make a sample interval &#8220;unknown&#8221;, such as the rate exceeding limits, or a sample that was explicitly marked as unknown. </p>
<p> The known rates during a PDP&#8216;s &#8220;step&#8221; interval are used to calculate an average rate for that PDP. If the total &#8220;unknown&#8221; time accounts for more than <code>half</code> the &#8220;step&#8221;, the entire PDP is marked as &#8220;unknown&#8221;. This means that a mixture of known and &#8220;unknown&#8221; sample times in a single PDP &#8220;step&#8221; may or may not add up to enough &#8220;known&#8221; time to warrant a known PDP. </p>
<p> The &#8220;heartbeat&#8221; can be short (unusual) or long (typical) relative to the &#8220;step&#8221; interval between PDPs. A short &#8220;heartbeat&#8221; means you require multiple samples per PDP, and if you don&#8217;t get them mark the PDP unknown. A long heartbeat can span multiple &#8220;steps&#8221;, which means it is acceptable to have multiple PDPs calculated from a single sample. An extreme example of this might be a &#8220;step&#8221; of 5 minutes and a &#8220;heartbeat&#8221; of one day, in which case a single sample every day will result in all the PDPs for that entire day period being set to the same average rate. <i>&#8212; Don Baarda &lt;don.baarda [at] baesystems.com&gt;</i> </p>
<pre><code>
       time|
       axis|
 begin__|00|
        |01|
       u|02|----* sample1, restart "hb"-timer
       u|03|   /
       u|04|  /
       u|05| /
       u|06|/     "hbt" expired
       u|07|
        |08|----* sample2, restart "hb" 
        |09|   / 
        |10|  /
       u|11|----* sample3, restart "hb"
       u|12|   /
       u|13|  /
 step1_u|14| /
       u|15|/     "swt" expired
       u|16|
        |17|----* sample4, restart "hb", create "pdp" for step1 = 
        |18|   /  = unknown due to 10 "u" labled secs &gt; 0.5 * step
        |19|  /
        |20| /
        |21|----* sample5, restart "hb"
        |22|   /
        |23|  /
        |24|----* sample6, restart "hb"
        |25|   /
        |26|  /
        |27|----* sample7, restart "hb"
 step2__|28|   /
        |22|  /
        |23|----* sample8, restart "hb", create "pdp" for step1, create "cdp" 
        |24|   /
        |25|  /
</code></pre>
<p> graphics by <i>vladimir.lavrov [at] desy.de</i>.</p>
<h2>HOW TO MEASURE</h2>
<p> Here are a few hints on how to measure:</p>
<dl>
<dt>Temperature</dt>
<dd> Usually you have some type of meter you can read to get the temperature. The temperature is not really connected with a time. The only connection is that the temperature reading happened at a certain time. You can use the <code>GAUGE</code> data source type for this. RRDtool will then record your reading together with the time.</dd>
<dt>Mail Messages</dt>
<dd> Assume you have a method to count the number of messages transported by your mail server in a certain amount of time, giving you data like &#8216;5 messages in the last 65 seconds&#8217;. If you look at the count of 5 like an <code>ABSOLUTE</code> data type you can simply update the RRD with the number 5 and the end time of your monitoring period. RRDtool will then record the number of messages per second. If at some later stage you want to know the number of messages transported in a day, you can get the average messages per second from RRDtool for the day in question and multiply this number with the number of seconds in a day. Because all math is run with Doubles, the precision should be acceptable.</dd>
<dt>It&#8217;s always a Rate</dt>
<dd> RRDtool stores rates in amount/second for COUNTER, DERIVE and ABSOLUTE data. When you plot the data, you will get on the y axis amount/second which you might be tempted to convert to an absolute amount by multiplying by the delta-time between the points. RRDtool plots continuous data, and as such is not appropriate for plotting absolute amounts as for example &#8220;total bytes&#8221; sent and received in a router. What you probably want is plot rates that you can scale to bytes/hour, for example, or plot absolute amounts with another tool that draws bar-plots, where the delta-time is clear on the plot for each point (such that when you read the graph you see for example GB on the y axis, days on the x axis and one bar for each day).</dd></dl>
<h2>EXAMPLE</h2>
<pre>
 rrdtool create temperature.rrd --step 300 \
  DS:temp:GAUGE:600:-273:5000 \
  RRA:AVERAGE:0.5:1:1200 \
  RRA:MIN:0.5:12:2400 \
  RRA:MAX:0.5:12:2400 \
  RRA:AVERAGE:0.5:12:2400
</pre>
<p> This sets up an <code>RRD</code> called <i>temperature.rrd</i> which accepts one temperature value every 300 seconds. If no new data is supplied for more than 600 seconds, the temperature becomes <i>*UNKNOWN*</i>. The minimum acceptable value is -273 and the maximum is 5&#8217;000. </p>
<p> A few archive areas are also defined. The first stores the temperatures supplied for 100 hours (1&#8217;200 * 300 seconds = 100 hours). The second RRA stores the minimum temperature recorded over every hour (12 * 300 seconds = 1 hour), for 100 days (2&#8217;400 hours). The third and the fourth RRA&#8216;s do the same for the maximum and average temperature, respectively.</p>
<h2>EXAMPLE 2</h2>
<pre>
 rrdtool create monitor.rrd --step 300        \
   DS:ifOutOctets:COUNTER:1800:0:4294967295   \
   RRA:AVERAGE:0.5:1:2016                     \
   RRA:HWPREDICT:1440:0.1:0.0035:288
</pre>
<p> This example is a monitor of a router interface. The first <code>RRA</code> tracks the traffic flow in octets; the second <code>RRA</code> generates the specialized functions <code>RRAs</code> for aberrant behavior detection. Note that the <i>rra-num</i> argument of HWPREDICT is missing, so the other <code>RRAs</code> will implicitly be created with default parameter values. In this example, the forecasting algorithm baseline adapts quickly; in fact the most recent one hour of observations (each at 5 minute intervals) accounts for 75% of the baseline prediction. The linear trend forecast adapts much more slowly. Observations made during the last day (at 288 observations per day) account for only 65% of the predicted linear trend. Note: these computations rely on an exponential smoothing formula described in the LISA 2000 paper. </p>
<p> The seasonal cycle is one day (288 data points at 300 second intervals), and the seasonal adaption parameter will be set to 0.1. The RRD file will store 5 days (1&#8217;440 data points) of forecasts and deviation predictions before wrap around. The file will store 1 day (a seasonal cycle) of 0-1 indicators in the FAILURES <code>RRA</code>. </p>
<p> The same RRD file and <code>RRAs</code> are created with the following command, which explicitly creates all specialized function <code>RRAs</code>. </p>
<pre>
 rrdtool create monitor.rrd --step 300 \
   DS:ifOutOctets:COUNTER:1800:0:4294967295 \
   RRA:AVERAGE:0.5:1:2016 \
   RRA:HWPREDICT:1440:0.1:0.0035:288:3 \
   RRA:SEASONAL:288:0.1:2 \
   RRA:DEVPREDICT:1440:5 \
   RRA:DEVSEASONAL:288:0.1:2 \
   RRA:FAILURES:288:7:9:5
</pre>
<p> Of course, explicit creation need not replicate implicit create, a number of arguments could be changed.</p>
<h2>EXAMPLE 3</h2>
<pre>
 rrdtool create proxy.rrd --step 300 \
   DS:Total:DERIVE:1800:0:U  \
   DS:Duration:DERIVE:1800:0:U  \
   DS:AvgReqDur:COMPUTE:Duration,Requests,0,EQ,1,Requests,IF,/ \
   RRA:AVERAGE:0.5:1:2016
</pre>
<p> This example is monitoring the average request duration during each 300 sec interval for requests processed by a web proxy during the interval. In this case, the proxy exposes two counters, the number of requests processed since boot and the total cumulative duration of all processed requests. Clearly these counters both have some rollover point, but using the DERIVE data source also handles the reset that occurs when the web proxy is stopped and restarted. </p>
<p> In the <code>RRD</code>, the first data source stores the requests per second rate during the interval. The second data source stores the total duration of all requests processed during the interval divided by 300. The COMPUTE data source divides each PDP of the AccumDuration by the corresponding PDP of TotalRequests and stores the average request duration. The remainder of the RPN expression handles the divide by zero case.</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
