---

title: "euwatch-put-data(1)"
name: "euwatch-put-data"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-put-data/"
description: "euwatch-put-data – add data points to a CloudWatch metric"
---

<p> <code>euwatch-put-data</code> &#8211; add data points to a CloudWatch metric </p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>n</code> <i>NAMESPACE</i> [-<code>v </code><i>FLOAT</i> ] <i>&#8230;</i><br/>
 &#8211;<code>n</code> <i>NAMESPACE</i> [-<code>s </code><i>KEY1=VALUE1,KEY2-VALUE2,&#8230;</i> ] <i>&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The utility adds data to a CloudWatch metric. A metric datum consists of a metric name, any of several attributes, and either a simple, numeric value (-<code>v</code> ) or a set of statistical values (-<code>s</code> ) </p>
<p> All of the data in a given invocation of must belong to one namespace, whose name is specified with &#8211;<code>n</code> </p>
<p> Metric data consist of one or more of the attributes below. These attributes may be specified using dedicated options that apply to all data in a given invocation of <code>,</code> or for individual data as part of an input to &#8211;<code>s</code> A metric name is required for all metric data.</p>
<dl>
<dt><code>Name Ta </code><code>Option Ta </code><code>Aliases</code></dt>
<dd>
</dd><dt><code>MetricName Ta </code>&#8211;<code>m Ta </code>metric</dt>
<dd>
</dd><dt><code>Dimensions Ta </code>&#8211;<code>d Ta </code>dim</dt>
<dd>
</dd><dt><code>Timestamp Ta </code>&#8211;<code>t Ta </code>ts</dt>
<dd>
</dd><dt><code>Unit Ta </code>&#8211;<code>u Ta </code>unit</dt>
<dd></dd></dl>
<p> Simple metric data have one additional attribute for their values.</p>
<dl>
<dt><code>Name Ta </code><code>Option Ta </code><code>Aliases</code></dt>
<dd>
</dd><dt><code>Value Ta </code>&#8211;<code>v Ta </code>val</dt>
<dd></dd></dl>
<p> Statistical metric data have four additional attributes. These attributes cannot be specified using separate command line options.</p>
<dl>
<dt><code>Name Ta </code><code>Aliases</code></dt>
<dd>
</dd><dt><code>Maximum Ta </code>max</dt>
<dd>
</dd><dt><code>Minimum Ta </code>min</dt>
<dd>
</dd><dt><code>SampleCount Ta </code>count</dt>
<dd>
</dd><dt><code>Sum Ta </code>sum</dt>
<dd></dd></dl>
<h3>Optional arguments:</h3>
<dl>
<dt><code>-n </code><i>NAMESPACE, &#8211;</i><code>-namespace </code><i>NAMESPACE</i></dt>
<dd> The namespace for all the data points in the current invocation of <code>.</code> This option is required.</dd>
<dt><code>-v </code><i>FLOAT, &#8211;</i><code>-value </code><i>FLOAT</i></dt>
<dd> Each use of the &#8211;<code>v</code> option specifies a new simple metric datum. A value for a simple metric datum. To specify other attributes for simple data points specifed using this option, use the corresponding options for those attributes from the tables above. In particular, &#8211;<code>m</code> is required when &#8211;<code>v</code> is used.</dd>
<dt><code>-s </code><i>KEY=VALUE,&#8230;, &#8211;</i><code>-metric-datum </code><i>KEY=VALUE,&#8230;</i></dt>
<dd> The &#8211;<code>s</code> option allows for full control of the attributes of each metric datum. This mode of entry is required for specifying statistical data points. To specify a datum using this option, join each attribute&#8217;s name or alias from the tables above with its value using the &#8220;=&#8221; character, and join each of those pairs with &#8220;,&#8221; characters. If a value contains a &#8220;,&#8221; character, surround the entire attribute with double-quotes, as in the following example. </dd>
<blockquote><p><tt>Qq </tt>Dimensions=ImageId=ami-98765432,InstanceId:i-12345678 </p></blockquote>
<p> Note that most shell environments require double-quotes to be escaped. </p>
<p> &#8220;Dimensions&#8221; attributes are specified as a comma-separated list of dimension names and values that are themselves separated by &#8220;:&#8221; characters. </p>
<p> Attributes specified via &#8211;<code>s</code> take precedence over those specified with attribute-specific options, such as &#8211;<code>d</code> </p>
<p> See the Sx EXAMPLES section for some illustrative examples.</p>
<dt><code>-m </code><i>METRIC, &#8211;</i><code>-metric-name </code><i>METRIC</i></dt>
<dd> The name of the metric to add data to. This is required unless all metric data specify metric names themselves.</dd>
<dt><code>-d </code><i>KEY=VALUE,&#8230;, &#8211;</i><code>-dimensions </code><i>KEY=VALUE,&#8230;</i></dt>
<dd> A list of dimensions to associate with the new metric data.</dd>
<dt><code>-t </code><i>YYYY-MM-DDThh:mm:ssZ, &#8211;</i><code>-timestamp </code><i>YYYY-MM-DDThh:mm:ssZ</i></dt>
<dd> A timestamp for the new metric data, in a format specified by ISO 8601. Note that the CloudWatch service does not accept data with timestamps more than two weeks in the past.</dd>
<dt><code>-u </code><i>UNIT, &#8211;</i><code>-unit </code><i>UNIT</i></dt>
<dd> The unit, such as &#8220;Bytes&#8221; in which to report the new metric data. Examples of valid units include the following: </dd>
<dl>
<dt><code>Seconds</code></dt>
<dd>
</dd><dt><code>Microseconds</code></dt>
<dd>
</dd><dt><code>Milliseconds</code></dt>
<dd>
</dd><dt><code>Bytes</code></dt>
<dd>
</dd><dt><code>Kilobytes</code></dt>
<dd>
</dd><dt><code>Megabytes</code></dt>
<dd>
</dd><dt><code>Gigabytes</code></dt>
<dd>
</dd><dt><code>Terabytes</code></dt>
<dd>
</dd><dt><code>Bits</code></dt>
<dd>
</dd><dt><code>Kilobits</code></dt>
<dd>
</dd><dt><code>Megabits</code></dt>
<dd>
</dd><dt><code>Gigabits</code></dt>
<dd>
</dd><dt><code>Terabits</code></dt>
<dd>
</dd><dt><code>Percent</code></dt>
<dd>
</dd><dt><code>Count</code></dt>
<dd>
</dd><dt><code>Bytes/Second</code></dt>
<dd>
</dd><dt><code>Kilobytes/Second</code></dt>
<dd>
</dd><dt><code>Megabytes/Second</code></dt>
<dd>
</dd><dt><code>Gigabytes/Second</code></dt>
<dd>
</dd><dt><code>Terabytes/Second</code></dt>
<dd>
</dd><dt><code>Bits/Second</code></dt>
<dd>
</dd><dt><code>Kilobits/Second</code></dt>
<dd>
</dd><dt><code>Megabits/Second</code></dt>
<dd>
</dd><dt><code>Gigabits/Second</code></dt>
<dd>
</dd><dt><code>Terabits/Second</code></dt>
<dd>
</dd><dt><code>Count/Second</code></dt>
<dd>
</dd><dt><code>None</code></dt>
<dd></dd></dl>
<dt><code>-h , &#8211;help</code></dt>
<dd> Show a help message and exit without doing anything.</dd>
<dt><code>-U </code><i>URL , &#8211;</i><code>-url </code><i>URL</i></dt>
<dd> The URL of the service to contact.</dd>
<dt><code>-I </code><i>KEY_ID , &#8211;</i><code>-access-key-id </code><i>KEY_ID</i></dt>
<dd> The access key ID to use to authenticate requests.</dd>
<dt><code>-S </code><i>KEY . &#8211;</i><code>-secret-key </code><i>KEY</i></dt>
<dd> The secret key to use to authenticate requests.</dd>
<dt><code>&#8211;security-token </code><i>TOKEN</i></dt>
<dd> The STS security token to use to authenticate requests.</dd>
<dt><code>&#8211;region </code><i>USER [at] REGION</i></dt>
<dd> The user and/or region name to use when looking up configuration file data.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Show debugging output when running.</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> Launch an interactive epdb or pdb debugger after encountering an error.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the program&#8217;s version and exit.</dd></dl>
<h2>EXAMPLES</h2>
<p> Report that instance i-12345678 is using 747 megabytes of memory using metric &#8220;MemoryUtilization&#8221; in namespace &#8220;MyNamespace&#8221; </p>
<blockquote><p><tt></tt><code>-n </code><i>MyNamespace &#8211;</i><code>m </code><i>MemoryUtilization &#8211;</i><code>u </code><i>Megabytes &#8211;</i><code>d </code><i>InstanceId=i-12345678 &#8211;</i><code>v </code><i>747</i> </p></blockquote>
<p> Same as above, but using the &#8211;<code>s</code> option. </p>
<blockquote><p><tt></tt><code>-n </code><i>MyNamespace &#8211;</i><code>m </code><i>MemoryUtilization &#8211;</i><code>u </code><i>Megabytes &#8211;</i><code>d </code><i>InstanceId=i-12345678 &#8211;</i><code>s </code><i>Value=747</i> </p></blockquote>
<p> Same as above, but specifying as much as possible using the &#8211;<code>s</code> option. </p>
<blockquote><p><tt></tt><code>-n </code><i>MyNamespace &#8211;</i><code>s </code><i>MetricName=MemoryUtilization,Unit=Megabytes,Dimensions=InstanceId:i-12345678,Value=747</i> </p></blockquote>
<p> Report statistics for 50 samples from instance i-12345678 that have a minimum value of 20, a maximum value of 80, and a sum of 2500 using metric &#8220;QueriesPerSecond&#8221; in namespace &#8220;MyNamespace&#8221; </p>
<blockquote><p><tt></tt><code>-n </code><i>MyNamespace &#8211;</i><code>m </code><i>QueriesPerSecond &#8211;</i><code>u </code><i>Count/Second &#8211;</i><code>d </code><i>InstanceId=i-12345678 &#8211;</i><code>s </code><i>Minimum=20,Maximum=80,Sum=2500,SampleCount=50</i> </p></blockquote>
<p> Same as above, but using aliases for attribute names. </p>
<blockquote><p><tt></tt><code>-n </code><i>MyNamespace &#8211;</i><code>m </code><i>QueriesPerSecond &#8211;</i><code>u </code><i>Count/Second &#8211;</i><code>d </code><i>InstanceId=i-12345678 &#8211;</i><code>s </code><i>min=20,max=80,sum=2500,count=50</i> </p></blockquote>
<p> Report both of the metric data above at once. The second datum uses &#8211;<code>s</code> to override the metric name and unit attributes specified by &#8211;<code>m</code> and &#8211;<code>u</code> but not the dimension specified by &#8211;<code>d</code> </p>
<blockquote><p><tt></tt><code>-n </code><i>MyNamespace &#8211;</i><code>m </code><i>MemoryUtilization &#8211;</i><code>u </code><i>Megabytes &#8211;</i><code>d </code><i>InstanceId=i-12345678 &#8211;</i><code>v </code><i>747 &#8211;</i><code>s </code><i>metric=QueriesPerSecond,unit=Count/Second,min=20,max=80,sum=2500,count=50</i> </p></blockquote>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>AWS_ACCESS_KEY_ID</code></dt>
<dd> The access key ID to use when authenticating web service requests. This takes precedence over &#8211;<code>-region</code> and euca2ools.ini5, but not &#8211;<code>I</code></dd>
<dt><code>AWS_SECRET_ACCESS_KEY</code></dt>
<dd> The secret key to use when authenticating web service requests. This takes precedence over &#8211;<code>-region</code> and euca2ools.ini5, but not &#8211;<code>S</code></dd>
<dt><code>AWS_CLOUDWATCH_URL</code></dt>
<dd> The URL of the service to contact. This takes precedence over &#8211;<code>-region</code> and euca2ools.ini5, but not &#8211;<code>U</code></dd></dl>
<h2>SEE ALSO</h2>
<p> euca2ools.ini5, <a href="/docs/linux/man/7-euca2ools/">euca2ools</a>(7)</p>
<h2>HISTORY</h2>
<p> The command first appeared in euca2ools 3.0. </p>
<p> The ability to report multiple metric data in a single request and the generic &#8211;<code>s</code> syntax that allows one to specify all attributes of a metric datum first appeared in euca2ools 3.4.</p>
<h2>NOTES</h2>
<p> requires access keys and knowledge of where to locate the web services it needs to contact. It can obtain these from several locations. See <a href="/docs/linux/man/7-euca2ools/">euca2ools</a>(7) for more information. </p>
