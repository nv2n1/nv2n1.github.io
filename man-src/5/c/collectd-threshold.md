---
title: "collectd-threshold(5)"
name: "collectd-threshold"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-threshold/"
description: "collectd-threshold – Documentation of collectd’s Threshold plugin"
---

<p>collectd-threshold &#8211; Documentation of collectd&#8217;s Threshold plugin</p>
<h2>Synopsis</h2>
<pre> LoadPlugin &quot;threshold&quot;
 &lt;Plugin &quot;threshold&quot;&gt;
 &lt;Type &quot;foo&quot;&gt;
 WarningMin 0.00
 WarningMax 1000.00
 FailureMin 0.00
 FailureMax 1200.00
 Invert false
 Instance &quot;bar&quot;
 &lt;/Type&gt;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>Starting with version <tt>4.3.0</tt> <i>collectd</i> has support for <code>monitoring</code>. By that we mean that the values are not only stored or sent somewhere, but that they are judged and, if a problem is recognized, acted upon. The only action the <i>Threshold plugin</i> takes itself is to generate and dispatch a <i>notification</i>. Other plugins can register to receive notifications and perform appropriate further actions. </p>
<p> Since systems and what you expect them to do differ a lot, you can configure <i>thresholds</i> for your values freely. This gives you a lot of flexibility but also a lot of responsibility. </p>
<p> Every time a value is out of range, a notification is dispatched. This means that the idle percentage of your <font SIZE="-1">CPU</font> needs to be less then the configured threshold only once for a notification to be generated. There&#8217;s no such thing as a moving average or similar &#8211; at least not now. </p>
<p> Also, all values that match a threshold are considered to be relevant or &#8220;interesting&#8221;. As a consequence collectd will issue a notification if they are not received for <code>Timeout</code> iterations. The <code>Timeout</code> configuration option is explained in section &#8220;<font SIZE="-1">GLOBAL OPTIONS&#8221;</font> in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5). If, for example, <code>Timeout</code> is set to &#8220;2&#8221; (the default) and some hosts sends it&#8217;s <font SIZE="-1">CPU</font> statistics to the server every 60 seconds, a notification will be dispatched after about 120 seconds. It may take a little longer because the timeout is checked only once each <code>Interval</code> on the server. </p>
<p> When a value comes within range again or is received after it was missing, an &#8220;OKAY-notification&#8221; is dispatched.</p>
<h2>Configuration</h2>
<p>Here is a configuration example to get you started. Read below for more information. </p>
<pre> LoadPlugin &quot;threshold&quot;
 &lt;Plugin &quot;threshold&quot;&gt;
 &lt;Type &quot;foo&quot;&gt;
 WarningMin 0.00
 WarningMax 1000.00
 FailureMin 0.00
 FailureMax 1200.00
 Invert false
 Instance &quot;bar&quot;
 &lt;/Type&gt;
 
 &lt;Plugin &quot;interface&quot;&gt;
 Instance &quot;eth0&quot;
 &lt;Type &quot;if_octets&quot;&gt;
 FailureMax 10000000
 DataSource &quot;rx&quot;
 &lt;/Type&gt;
 &lt;/Plugin&gt;
 
 &lt;Host &quot;hostname&quot;&gt;
 &lt;Type &quot;cpu&quot;&gt;
 Instance &quot;idle&quot;
 FailureMin 10
 &lt;/Type&gt;
 
 &lt;Plugin &quot;memory&quot;&gt;
 &lt;Type &quot;memory&quot;&gt;
 Instance &quot;cached&quot;
 WarningMin 100000000
 &lt;/Type&gt;
 &lt;/Plugin&gt;
 
 &lt;Type &quot;load&quot;&gt;
 DataSource &quot;midterm&quot;
 FailureMax 4
 Hits 3
 Hysteresis 3
 &lt;/Type&gt;
 &lt;/Host&gt;
 &lt;/Plugin&gt;</pre>
<p>There are basically two types of configuration statements: The <tt>&quot;Host&quot;</tt>, <tt>&quot;Plugin&quot;</tt>, and <tt>&quot;Type&quot;</tt> blocks select the value for which a threshold should be configured. The <tt>&quot;Plugin&quot;</tt> and <tt>&quot;Type&quot;</tt> blocks may be specified further using the <tt>&quot;Instance&quot;</tt> option. You can combine the block by nesting the blocks, though they must be nested in the above order, i.e. <tt>&quot;Host&quot;</tt> may contain either <tt>&quot;Plugin&quot;</tt> and <tt>&quot;Type&quot;</tt> blocks, <tt>&quot;Plugin&quot;</tt> may only contain <tt>&quot;Type&quot;</tt> blocks and <tt>&quot;Type&quot;</tt> may not contain other blocks. If multiple blocks apply to the same value the most specific block is used. </p>
<p> The other statements specify the threshold to configure. They <code>must</code> be included in a <tt>&quot;Type&quot;</tt> block. Currently the following statements are recognized:</p>
<dl>
<dt><code>FailureMax</code> <i>Value</i></p>
<dd>
<dt><code>WarningMax</code> <i>Value</i></p>
<dd>Sets the upper bound of acceptable values. If unset defaults to positive infinity. If a value is greater than <code>FailureMax</code> a <font SIZE="-1"><code>FAILURE</code></font> notification will be created. If the value is greater than <code>WarningMax</code> but less than (or equal to) <code>FailureMax</code> a <font SIZE="-1"><code>WARNING</code></font> notification will be created.</p>
<dt><code>FailureMin</code> <i>Value</i></p>
<dd>
<dt><code>WarningMin</code> <i>Value</i></p>
<dd>Sets the lower bound of acceptable values. If unset defaults to negative infinity. If a value is less than <code>FailureMin</code> a <font SIZE="-1"><code>FAILURE</code></font> notification will be created. If the value is less than <code>WarningMin</code> but greater than (or equal to) <code>FailureMin</code> a <font SIZE="-1"><code>WARNING</code></font> notification will be created.</p>
<dt><code>DataSource</code> <i>DSName</i></p>
<dd>Some data sets have more than one &#8220;data source&#8221;. Interesting examples are the <tt>&quot;if_octets&quot;</tt> data set, which has received (<tt>&quot;rx&quot;</tt>) and sent (<tt>&quot;tx&quot;</tt>) bytes and the <tt>&quot;disk_ops&quot;</tt> data set, which holds <tt>&quot;read&quot;</tt> and <tt>&quot;write&quot;</tt> operations. The system load data set, <tt>&quot;load&quot;</tt>, even has three data sources: <tt>&quot;shortterm&quot;</tt>, <tt>&quot;midterm&quot;</tt>, and <tt>&quot;longterm&quot;</tt>. </p>
<p> Normally, all data sources are checked against a configured threshold. If this is undesirable, or if you want to specify different limits for each data source, you can use the <code>DataSource</code> option to have a threshold apply only to one data source.</p>
<dt><code>Invert</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> the range of acceptable values is inverted, i.e. values between <code>FailureMin</code> and <code>FailureMax</code> (<code>WarningMin</code> and <code>WarningMax</code>) are not okay. Defaults to <code>false</code>.</p>
<dt><code>Persist</code> <code>true</code>|<code>false</code></p>
<dd>Sets how often notifications are generated. If set to <code>true</code> one notification will be generated for each value that is out of the acceptable range. If set to <code>false</code> (the default) then a notification is only generated if a value is out of range but the previous value was okay. </p>
<p> This applies to missing values, too: If set to <code>true</code> a notification about a missing value is generated once every <code>Interval</code> seconds. If set to <code>false</code> only one such notification is generated until the value appears again.</p>
<dt><code>PersistOK</code> <code>true</code>|<code>false</code></p>
<dd>Sets how <font SIZE="-1">OKAY</font> notifications act. If set to <code>true</code> one notification will be generated for each value that is in the acceptable range. If set to <code>false</code> (the default) then a notification is only generated if a value is in range but the previous value was not.</p>
<dt><code>Percentage</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code>, the minimum and maximum values given are interpreted as percentage value, relative to the other data sources. This is helpful for example for the &#8220;df&#8221; type, where you may want to issue a warning when less than 5&nbsp;<wbr>% of the total space is available. Defaults to <code>false</code>.</p>
<dt><code>Hits</code> <i>Value</i></p>
<dd>Sets the number of occurrences which the threshold must be raised before to dispatch any notification or, in other words, the number of <code>Interval</code>s that the threshold must be match before dispatch any notification.</p>
<dt><code>Hysteresis</code> <i>Value</i></p>
<dd>Sets the hysteresis value for threshold. The hysteresis is a method to prevent flapping between states, until a new received value for a previously matched threshold down below the threshold condition (<code>WarningMax</code>, <code>FailureMin</code> or everything else) minus the hysteresis value, the failure (respectively warning) state will be keep.</p>
<dt><code>Interesting</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> (the default), a notification with severity <tt>&quot;FAILURE&quot;</tt> will be created when a matching value list is no longer updated and purged from the internal cache. When this happens depends on the <i>interval</i> of the value list and the global <code>Timeout</code> setting. See the <code>Interval</code> and <code>Timeout</code> settings in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for details. If set to <code>false</code>, this event will be ignored.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5)</p>
<h2>Author</h2>
<p>Florian Forster &lt;octo at collectd.org&gt;</p>
