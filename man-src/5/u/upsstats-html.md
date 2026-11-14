---
title: "upsstats-html(5)"
name: "upsstats-html"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upsstats-html/"
description: "upsstats.html – HTML template for Network UPS Tools upsstats"
---

<p>upsstats.html &#8211; HTML template for Network UPS Tools upsstats</p>
<h2>Description</h2>
<p>This file is used by <code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8) to generate status pages. Certain commands are recognized, and will be replaced with various status elements on the fly.</p>
<h2>Formatting</h2>
<p>Commands can be placed anywhere on a line, but must start and end with @. Any extra characters before or after the commands will be passed through unchanged. It is allowed to use more than one command on a single line, as long as each command has its own start and end character. If you need to use the @ sign, use @ to prevent it from being treated as a start character.</p>
<h2>Block Control</h2>
<p>Some commands begin blocks &#8211; sections of the template that will be included, excluded, or repeated depending on certain parameters.</p>
<h3>Block Control &#8211; Iteration</h3>
<p><code>@FOREACHUPS@</code></p>
<dl>
<dd>Starts a block that will be repeated for each MONITOR directive in the <code><a href="/docs/linux/man/5-hosts-conf/">hosts.conf</a></code>(5). This is how you can generate pages that monitor all of your systems simultaneously.</dl>
<p> <code>@ENDFOR@</code></p>
<dl>
<dd>Ends a FOREACHUPS block.</dl>
<h3>Block Control &#8211; Matching Specific Cases</h3>
<p><code>@IFSUPP </code><i>var</i>@*</p>
<dl>
<dd>Starts a block that will only be printed if the variable var is supported by the current UPS. This is generally used to suppress &quot;not supported&quot; messages by avoiding the label and variable call entirely.</dl>
<p> <code>@IFEQ</code> <i>var</i> <i>value</i><code>@</code></p>
<dl>
<dd>Starts a block if the value returned from the variable <i>var</i> matches <i>value</i>.</dl>
<p> <code>@IFBETWEEN</code> <i>varlow</i> <i>varhigh</i> <i>varvalue</i><code>@</code></p>
<dl>
<dd>Starts a block if the value returned by the variable <i>varvalue</i> is between the values returned by the variables <i>varlow</i> and <i>varhigh</i>.</dl>
<p> <code>@ELSE@</code></p>
<dl>
<dd>If the previous IF-command did not match, perform this instead.</dl>
<p> <code>@ENDIF@</code></p>
<dl>
<dd>Ends an IF/ELSE-block.</dl>
<h3>Block Control &#8211; Advanced Expressions</h3>
<p>Even though the parser is pretty limited, it&#8217;s still possible to create rather advanced expressions. The key to this is the fact that multiple block control commands are AND:ed. This is illustrated with an example (more examples are available in upsstats.html). </p>
<dl>
<dd>
<pre>@IFSUPP ambient.humidity@
@IFSUPP ambient.temperature@
This UPS knows both ambient temperature and humidity.
@ELSE@
@IFSUPP ambient.humidity@
This UPS only knows ambient humidity.
@ELSE@
@IFSUPP ambient.temperature@
This UPS only knows ambient temperature.
@ELSE@
This UPS knows nothing, how annoying.
@ENDIF@</pre>
</dl>
<h2>Other Commands</h2>
<p><code>@AMBTEMP@</code></p>
<dl>
<dd>Insert the ambient temperature in the current temperature scale.</dl>
<p> <code>@DATE</code> <i>format</i><code>@</code></p>
<dl>
<dd>Insert the current date and time. The format string is passed to strftime, so almost anything is possible. See <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for possible values.</dl>
<p> <code>@DEGREES@</code></p>
<dl>
<dd>Insert the entity for degrees (&#176;) and either C or F depending on the current temperature scale.</dl>
<p> <code>@HOST@</code></p>
<dl>
<dd>Insert the designation of the host being monitored, like myups [at] localhost.</dl>
<p> <code>@HOSTDESC@</code></p>
<dl>
<dd>Insert the hout&#8217;s description from <code><a href="/docs/linux/man/5-hosts-conf/">hosts.conf</a></code>(5).</dl>
<p> <code>@HOSTLINK@</code></p>
<dl>
<dd>Insert a link to upsstats.cgi with the &quot;host&quot; variable set to the current UPS. This is only useful within a FOREACHUPS block.</dl>
<p> <code>@IMG</code> <i>varname</i> <code>@</code></p>
<dl>
<dd>Insert an IMG SRC to <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8) for one of these status variables: </p>
<p> battery.charge</p>
<dl>
<dd>Battery charge &#8211; a percentage</dl>
<p> battery.voltage</p>
<dl>
<dd>The charge on the battery in volts</dl>
<p> input.frequency</p>
<dl>
<dd>Incoming utility frequency (Hz)</dl>
<p> input.voltage</p>
<dl>
<dd>Incoming utility voltage</dl>
<p> input.L1-L2.voltage</p>
<dl>
<dd>Incoming voltage, L1-L2 (3phase)</dl>
<p> input.L2-L3.voltage</p>
<dl>
<dd>Incoming voltage, L2-L3 (3phase)</dl>
<p> input.L3-L1.voltage</p>
<dl>
<dd>Incoming voltage, L3-L1 (3phase)</dl>
<p> output.frequency</p>
<dl>
<dd>Outgoing utility frequency (Hz)</dl>
<p> output.voltage</p>
<dl>
<dd>Outgoing voltage (from the UPS)</dl>
<p> output.L1-L2.voltage</p>
<dl>
<dd>Outgoing voltage, L1-L2 (3phase)</dl>
<p> output.L2-L3.voltage</p>
<dl>
<dd>Outgoing voltage, L2-L3 (3phase)</dl>
<p> output.L3-L1.voltage</p>
<dl>
<dd>Outgoing voltage, L3-L1 (3phase)</dl>
<p> output.L1.power.percent</p>
<dl>
<dd>UPS load, L1 (3phase)</dl>
<p> output.L2.power.percent</p>
<dl>
<dd>UPS load, L2 (3phase)</dl>
<p> output.L3.power.percent</p>
<dl>
<dd>UPS load, L3 (3phase)</dl>
<p> ups.load</p>
<dl>
<dd>UPS load &#8211; percentage</dl>
<p> ups.temperature</p>
<dl>
<dd>UPS temperature</dl>
</dl>
<p> <i>extra</i> is where you can put additional definitions. Right now the valid definitions are colors for various parts of the bars drawn by upsimage.cgi. Possible color names are: </p>
<p> back_col</p>
<dl>
<dd>background color</dl>
<p> scale_num_col</p>
<dl>
<dd>scale number color</dl>
<p> summary_col</p>
<dl>
<dd>summary color (number at the bottom)</dl>
<p> ok_zone_maj_col</p>
<dl>
<dd>major scale color for the normal (&quot;ok&quot;) zone</dl>
<p> ok_zone_min_col</p>
<dl>
<dd>minor scale color for the normal (&quot;ok&quot;) zone</dl>
<p> neutral_zone_maj_col</p>
<dl>
<dd>major scale color for the neutral zone</dl>
<p> neutral_zone_min_col</p>
<dl>
<dd>minor scale color for the neutral zone</dl>
<p> warn_zone_maj_col</p>
<dl>
<dd>major scale color for the warning zone</dl>
<p> warn_zone_min_col</p>
<dl>
<dd>minor scale color for the warning zone</dl>
<p> bar_col</p>
<dl>
<dd>the color of the bar in the middle</dl>
<p> All colors are hex triplets &#8211; 0xff0000 is red, 0x00ff00 is green, and 0x0000ff is blue. </p>
<p> Examples: </p>
<dl>
<dd>
<pre>@IMG battery.charge@
@IMG battery.charge back_col=0xff00ff bar_col=0xaabbcc@
@IMG input.voltage ok_zone_maj_col=0x123456@</pre>
</dl>
<p> <code>@REFRESH@</code></p>
<dl>
<dd>Insert the META header magic for refreshing the page if that variable has been set by the browser. This needs to be in the HEAD section of the page.</dl>
<p> <code>@STATUS@</code></p>
<dl>
<dd>Expand the abbreviations in the ups.status variable &#8211; OL becomes &quot;On line&quot;, OB becomes &quot;On battery&quot;, and so on.</dl>
<p> <code>@STATUSCOLOR@</code></p>
<dl>
<dd>Insert red, green, or yellow color triplets depending on the severity of the current UPS status. Normal operations are green, warnings like voltage trim/boost or &quot;off&quot; are yellow, and other events like being on battery or having a low battery are red.</dl>
<p> <code>@VAR</code> <i>varname</i><code>@</code></p>
<dl>
<dd>Insert the current value of the status variable varname on the host being monitored, or &quot;Not supported&quot;.</dl>
<p> <code>@RUNTIME@</code></p>
<dl>
<dd>Inserts the current runtime, in hh:mm:ss format.</dl>
<p> <code>@TEMPC@</code></p>
<dl>
<dd>Use the Celsius scale for temperature data (default).</dl>
<p> <code>@TEMPF@</code></p>
<dl>
<dd>Use the Fahrenheit scale for temperature data.</dl>
<p> <code>@UPSTEMP@</code></p>
<dl>
<dd>Insert the UPS temperature in the current scale.</dl>
<p> <code>@BATTTEMP@</code></p>
<dl>
<dd>Insert the battery temperature in the current scale.</dl>
<p> <code>@UTILITYCOLOR@</code></p>
<dl>
<dd>Obsoleted. Use IFBETWEEN instead (see example in upsstats.html).</dl>
<p> <code>@VERSION@</code></p>
<dl>
<dd>Insert the version number of the software.</dl>
<h2>Other Templates</h2>
<p><code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8) will also open a file called upsstats-single.html if you call it with &quot;host=&quot; set in the URL. That file uses the same rules and techniques documented here.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
