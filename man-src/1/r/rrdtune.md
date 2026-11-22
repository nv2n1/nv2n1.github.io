---

title: "rrdtune(1)"
name: "rrdtune"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdtune/"
description: "rrdtune – Modify some basic properties of a Round Robin Database"
---

<p> rrdtune &#8211; Modify some basic properties of a Round Robin Database </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>tune</code> <i>filename</i> [<code>&#8211;heartbeat</code>|<code>-h</code>&nbsp;<wbr><i>ds-name</i>:<i>heartbeat</i>] [<code>&#8211;minimum</code>|<code>-i</code>&nbsp;<wbr><i>ds-name</i>:<i>min</i>] [<code>&#8211;maximum</code>|<code>-a</code>&nbsp;<wbr><i>ds-name</i>:<i>max</i>] [<code>&#8211;data-source-type</code>|<code>-d</code>&nbsp;<wbr><i>ds-name</i>:<i></i><i>DST</i><i></i>] [<code>&#8211;data-source-rename</code>|<code>-r</code>&nbsp;<wbr><i>old-name</i>:<i>new-name</i>] [<code>&#8211;deltapos</code>&nbsp;<wbr><i>scale-value</i>] [<code>&#8211;deltaneg</code>&nbsp;<wbr><i>scale-value</i>] [<code>&#8211;failure-threshold</code>&nbsp;<wbr><i>failure-threshold</i>] [<code>&#8211;window-length</code>&nbsp;<wbr><i>window-length</i>] [<code>&#8211;alpha</code>&nbsp;<wbr><i>adaption-parameter</i>] [<code>&#8211;beta</code>&nbsp;<wbr><i>adaption-parameter</i>] [<code>&#8211;gamma</code>&nbsp;<wbr><i>adaption-parameter</i>] [<code>&#8211;gamma-deviation</code>&nbsp;<wbr><i>adaption-parameter</i>] [<code>&#8211;smoothing-window</code>&nbsp;<wbr><i>fraction-of-season</i>] [<code>&#8211;smoothing-window-deviation</code>&nbsp;<wbr><i>fraction-of-season</i>] [<code>&#8211;aberrant-reset</code>&nbsp;<wbr><i>ds-name</i>]</p>
<h2>DESCRIPTION</h2>
<p> The tune option allows you to alter some of the basic configuration values stored in the header area of a Round Robin Database (<code>RRD</code>). </p>
<p> One application of the <code>tune</code> function is to relax the validation rules on an <code>RRD</code>. This allows to fill a new <code>RRD</code> with data available in larger intervals than what you would normally want to permit. Be very careful with tune operations for COMPUTE data sources. Setting the <i>min</i>, <i>max</i>, and <i>heartbeat</i> for a COMPUTE data source without changing the data source type to a non-COMPUTE <code>DST</code> WILL corrupt the data source header in the <code>RRD</code>. </p>
<p> A second application of the <code>tune</code> function is to set or alter parameters used by the specialized function <code>RRAs</code> for aberrant behavior detection.</p>
<dl>
<dt><i>filename</i></dt>
<dd> The name of the <code>RRD</code> you want to tune.</dd>
<dt><code>&#8211;heartbeat</code>|<code>-h</code>&nbsp;<wbr><i>ds-name</i>:<i>heartbeat</i></dt>
<dd> modify the <i>heartbeat</i> of a data source. By setting this to a high value the RRD will accept things like one value per day.</dd>
<dt><code>&#8211;minimum</code>|<code>-i</code>&nbsp;<wbr><i>ds-name</i>:<i>min</i></dt>
<dd> alter the minimum value acceptable as input from the data source. Setting <i>min</i> to &#8216;U&#8217; will disable this limit.</dd>
<dt><code>&#8211;maximum</code>|<code>-a</code>&nbsp;<wbr><i>ds-name</i>:<i>max</i></dt>
<dd> alter the maximum value acceptable as input from the data source. Setting <i>max</i> to &#8216;U&#8217; will disable this limit.</dd>
<dt><code>&#8211;data-source-type</code>|<code>-d</code>&nbsp;<wbr><i>ds-name</i>:<i></i><i>DST</i><i></i></dt>
<dd> alter the type <code>DST</code> of a data source.</dd>
<dt><code>&#8211;data-source-rename</code>|<code>-r</code>&nbsp;<wbr><i>old-name</i>:<i>new-name</i></dt>
<dd> rename a data source.</dd>
<dt><code>&#8211;deltapos</code>&nbsp;<wbr><i>scale-value</i></dt>
<dd> Alter the deviation scaling factor for the upper bound of the confidence band used internally to calculate violations for the FAILURES <code>RRA</code>. The default value is 2. Note that this parameter is not related to graphing confidence bounds which must be specified as a CDEF argument to generate a graph with confidence bounds. The graph scale factor need not to agree with the value used internally by the FAILURES <code>RRA</code>.</dd>
<dt><code>&#8211;deltaneg</code>&nbsp;<wbr><i>scale-value</i></dt>
<dd> Alter the deviation scaling factor for the lower bound of the confidence band used internally to calculate violations for the FAILURES <code>RRA</code>. The default value is 2. As with <code>&#8211;deltapos</code>, this argument is unrelated to the scale factor chosen when graphing confidence bounds.</dd>
<dt><code>&#8211;failure-threshold</code>&nbsp;<wbr><i>failure-threshold</i></dt>
<dd> Alter the number of confidence bound violations that constitute a failure for purposes of the FAILURES <code>RRA</code>. This must be an integer less than or equal to the window length of the FAILURES <code>RRA</code>. This restriction is not verified by the tune option, so one can reset failure-threshold and window-length simultaneously. Setting this option will reset the count of violations to 0.</dd>
<dt><code>&#8211;window-length</code>&nbsp;<wbr><i>window-length</i></dt>
<dd> Alter the number of time points in the temporal window for determining failures. This must be an integer greater than or equal to the window length of the FAILURES <code>RRA</code> and less than or equal to 28. Setting this option will reset the count of violations to 0.</dd>
<dt><code>&#8211;alpha</code>&nbsp;<wbr><i>adaption-parameter</i></dt>
<dd> Alter the intercept adaptation parameter for the Holt-Winters forecasting algorithm. This parameter must be between 0 and 1.</dd>
<dt><code>&#8211;beta</code>&nbsp;<wbr><i>adaption-parameter</i></dt>
<dd> Alter the slope adaptation parameter for the Holt-Winters forecasting algorithm. This parameter must be between 0 and 1.</dd>
<dt><code>&#8211;gamma</code>&nbsp;<wbr><i>adaption-parameter</i></dt>
<dd> Alter the seasonal coefficient adaptation parameter for the SEASONAL <code>RRA</code>. This parameter must be between 0 and 1.</dd>
<dt><code>&#8211;gamma-deviation</code>&nbsp;<wbr><i>adaption-parameter</i></dt>
<dd> Alter the seasonal deviation adaptation parameter for the DEVSEASONAL <code>RRA</code>. This parameter must be between 0 and 1.</dd>
<dt><code>&#8211;smoothing-window</code>&nbsp;<wbr><i>fraction-of-season</i></dt>
<dd> Alter the size of the smoothing window for the SEASONAL <code>RRA</code>. This must be between 0 and 1.</dd>
<dt><code>&#8211;smoothing-window-deviation</code>&nbsp;<wbr><i>fraction-of-season</i></dt>
<dd> Alter the size of the smoothing window for the DEVSEASONAL <code>RRA</code>. This must be between 0 and 1.</dd>
<dt><code>&#8211;aberrant-reset</code>&nbsp;<wbr><i>ds-name</i></dt>
<dd> This option causes the aberrant behavior detection algorithm to reset for the specified data source; that is, forget all it is has learnt so far. Specifically, for the HWPREDICT or MHWPREDICT <code>RRA</code>, it sets the intercept and slope coefficients to unknown. For the SEASONAL <code>RRA</code>, it sets all seasonal coefficients to unknown. For the DEVSEASONAL <code>RRA</code>, it sets all seasonal deviation coefficients to unknown. For the FAILURES <code>RRA</code>, it erases the violation history. Note that reset does not erase past predictions (the values of the HWPREDICT or MHWPREDICT <code>RRA</code>), predicted deviations (the values of the DEVPREDICT <code>RRA</code>), or failure history (the values of the FAILURES <code>RRA</code>). This option will function even if not all the listed <code>RRAs</code> are present. </dd>
<p> Due to the implementation of this option, there is an indirect impact on other data sources in the RRD. A smoothing algorithm is applied to SEASONAL and DEVSEASONAL values on a periodic basis. During bootstrap initialization this smoothing is deferred. For efficiency, the implementation of smoothing is not data source specific. This means that utilizing reset for one data source will delay running the smoothing algorithm for all data sources in the file. This is unlikely to have serious consequences, unless the data being collected for the non-reset data sources is unusually volatile during the reinitialization period of the reset data source. </p>
<p> Use of this tuning option is advised when the behavior of the data source time series changes in a drastic and permanent manner.</dl>
<h2>EXAMPLE 1</h2>
<p> <tt>&quot;rrdtool tune data.rrd -h in:100000 -h out:100000 -h through:100000&quot;</tt> </p>
<p> Set the minimum required heartbeat for data sources &#8216;in&#8217;, &#8216;out&#8217; and &#8216;through&#8217; to 10&#8217;000 seconds which is a little over one day in data.rrd. This would allow to feed old data from MRTG-2.0 right into RRDtool without generating *UNKNOWN* entries.</p>
<h2>EXAMPLE 2</h2>
<p> <tt>&quot;rrdtool tune monitor.rrd --window-length 5 --failure-threshold 3&quot;</tt> </p>
<p> If the FAILURES <code>RRA</code> is implicitly created, the default window-length is 9 and the default failure-threshold is 7. This command now defines a failure as 3 or more violations in a temporal window of 5 time points.</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
