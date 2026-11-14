---
title: "upsstats(5)"
name: "upsstats"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upsstats/"
description: "upsstats.html – HTML template for Network UPS Tools upsstats"
---

<p>upsstats.html &#8211; HTML template for Network UPS Tools upsstats </p>
<h2>Description</h2>
<p>This file is used by <code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8) to generate status pages. Certain commands are recognized, and will be replaced with various status elements on the fly. </p>
<h2>Formatting</h2>
<p>Commands can be placed anywhere on a line, but must start and end with @. Any extra characters before or after the commands will be passed through unchanged. It is allowed to use more than one command on a single line, as long as each command has its own start and end character. If you need to use the @ sign, use &amp;#64; to prevent it from being treated as a start character.</p>
<h2>Block Control</h2>
<p>Some commands begin blocks &#8211; sections of the template that will be included, excluded, or repeated depending on certain parameters.</p>
<h2>Block Control &#8211; Iteration</h2>
<dl>
<dt>@FOREACHUPS@</p>
<dd>Starts a block that will be repeated for each MONITOR directive in the <code><a href="/docs/linux/man/5-hosts-conf/">hosts.conf</a></code>(5). This is how you can generate pages that monitor all of your systems simultaneously. </p>
<dt>@ENDFOR@</p>
<dd>Ends a FOREACHUPS block. </p>
</dl>
<h2>Block Control &#8211; Matching Specific Cases</h2>
<dl>
<dt>@IFSUPP var@</p>
<dd>Starts a block that will only be printed if the variable var is supported by the current UPS. This is generally used to suppress &quot;not supported&quot; messages by avoiding the label and variable call entirely. </p>
<dt>@IFEQ var value@</p>
<dd>Starts a block if the value returned from the variable var matches value. </p>
<dt>@IFBETWEEN varlow varhigh varvalue@</p>
<dd>Starts a block if the value returned by the variable varvalue is between the values returned by the variables varlow and varhigh. </p>
<dt>@ELSE@</p>
<dd>If the previous IF-command did not match, perform this instead. </p>
<dt>@ENDIF@</p>
<dd>Ends an IF/ELSE-block. </p>
</dl>
<h2>Block Control &#8211; Advanced Expressions</h2>
<p>Even though the parser is pretty limited, it&#8217;s still possible to create rather advanced expressions. The key to this is the fact that multiple block control commands are AND:ed. This is illustrated with an example (more examples are available in upsstats.html). </p>
<p> @IFSUPP ambient.humidity@ </p>
<p> @IFSUPP ambient.temperature@ </p>
<p> This UPS knows both ambient temperature and humidity. </p>
<p> @ELSE@ </p>
<p> @IFSUPP ambient.humidity@ </p>
<p> This UPS only knows ambient humidity. </p>
<p> @ELSE@ </p>
<p> @IFSUPP ambient.temperature@ </p>
<p> This UPS only knows ambient temperature. </p>
<p> @ELSE </p>
<p> This UPS knows nothing, how annoying. </p>
<p> @ENDIF@</p>
<h2>Other Commands</h2>
<dl>
<dt>@AMBTEMP@</p>
<dd>Insert the ambient temperature in the current temperature scale. </p>
<dt>@DATE format@</p>
<dd>Insert the current date and time. The format string is passed to strftime, so almost anything is possible. See <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for possible values. </p>
<dt>@DEGREES@</p>
<dd>Insert the entity for degrees (&amp;deg;) and either C or F depending on the current temperature scale. </p>
<dt>@HOST@</p>
<dd>Insert the designation of the host being monitored, like myups [at] localhost. </p>
<dt>@HOSTDESC@</p>
<dd>Insert the host&#8217;s description from <code><a href="/docs/linux/man/5-hosts-conf/">hosts.conf</a></code>(5). </p>
<dt>@HOSTLINK@</p>
<dd>Insert a link to upsstats.cgi with the &quot;host&quot; variable set to the current UPS. This is only useful within a FOREACHUPS block. </p>
<dt>@IMG varname [<i>extra</i>]@</p>
<dd>Insert an IMG SRC to <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8) for one of these status variables: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>battery.charge &#8211; Battery charge &#8211; a percentage</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>battery.voltage &#8211; The charge on the battery in volts</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>input.frequency &#8211; Incoming utility frequency (Hz)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>input.voltage &#8211; Incoming utility voltage</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>input.L1-L2.voltage &#8211; Incoming voltage, L1-L2 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>input.L2-L3.voltage &#8211; Incoming voltage, L2-L3 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>input.L3-L1.voltage &#8211; Incoming voltage, L3-L1 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.frequency &#8211; Outgoing utility frequency (Hz)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.voltage &#8211; Outgoing voltage (from the UPS)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.L1-L2.voltage &#8211; Outgoing voltage, L1-L2 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.L2-L3.voltage &#8211; Outgoing voltage, L2-L3 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.L3-L1.voltage &#8211; Outgoing voltage, L3-L1 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.L1.power.percent &#8211; UPS load, L1 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.L2.power.percent &#8211; UPS load, L2 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>output.L3.power.percent &#8211; UPS load, L3 (3phase)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ups.load &#8211; UPS load &#8211; percentage</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ups.temperature &#8211; UPS temperature </p>
<p> <i>extra</i> is where you can put additional definitions. Right now the valid definitions are colors for various parts of the bars drawn by upsimage.cgi. Possible color names are: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>back_col &#8211; background color</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>scale_num_col &#8211; scale number color</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>summary_col &#8211; summary color (number at the bottom)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ok_zone_maj_col<tt>&nbsp;<wbr></tt>&#8211; major scale color for the normal (&quot;ok&quot;) zone</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ok_zone_min_col<tt>&nbsp;<wbr></tt>&#8211; minor scale color for the normal (&quot;ok&quot;) zone</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>neutral_zone_maj_col &#8211; major scale color for the neutral zone</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>neutral_zone_min_col &#8211; minor scale color for the neutral zone</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>warn_zone_maj_col &#8211; major scale color for the warning zone</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>warn_zone_min_col &#8211; minor scale color for the warning zone</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bar_col &#8211; the color of the bar in the middle</p>
<p> All colors are hex triplets &#8211; 0xff0000 is red, 0x00ff00 is green, and 0x0000ff is blue. </p>
<p> Examples: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>@IMG battery.charge@</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>@IMG battery.charge back_col=0xff00ff bar_col=0xaabbcc@</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>@IMG input.voltage ok_zone_maj_col=0x123456@</p>
<dt>@REFRESH@</p>
<dd>Insert the META header magic for refreshing the page if that variable has been set by the browser. This needs to be in the HEAD section of the page. </p>
<dt>@STATUS@</p>
<dd>Expand the abbreviations in the ups.status variable &#8211; OL becomes &quot;On line&quot;, OB becomes &quot;On battery&quot;, and so on. </p>
<dt>@STATUSCOLOR@</p>
<dd>Insert red, green, or yellow color triplets depending on the severity of the current UPS status. Normal operations are green, warnings like voltage trim/boost or &quot;off&quot; are yellow, and other events like being on battery or having a low battery are red. </p>
<dt>@VAR varname@</p>
<dd>Insert the current value of the status variable varname on the host being monitored, or &quot;Not supported&quot;. </p>
<dt>@RUNTIME@</p>
<dd>Inserts the current runtime, in hh:mm:ss format. </p>
<dt>@TEMPC@</p>
<dd>Use the Celsius scale for temperature data (default). </p>
<dt>@TEMPF@</p>
<dd>Use the Fahrenheit scale for temperature data. </p>
<dt>@UPSTEMP@</p>
<dd>Insert the UPS temperature in the current scale. </p>
<dt>@BATTTEMP@</p>
<dd>Insert the battery temperature in the current scale. </p>
<dt>@UTILITYCOLOR@</p>
<dd>Obsoleted. Use IFBETWEEN instead (see example in upsstats.html). </p>
<dt>@VERSION@</p>
<dd>Insert the version number of the software. </p>
</dl>
<h2>Other Templates</h2>
<p><code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8) will also open a file called upsstats-single.html if you call it with &quot;host=&quot; set in the URL. That file uses the same rules and techniques documented here.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
