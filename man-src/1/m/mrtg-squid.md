---
title: "mrtg-squid(1)"
name: "mrtg-squid"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-squid/"
---

<h2 class="name">NAME</h2>
 

 mrtg-squid - using mrtg to monitor Squid 

<h2>DESCRIPTION</h2>

 Squid 2.3 knows <font SIZE="-1">SNMP</font> and you can therefore use mrtg to monitor it quite easily. 

 I have made some modifications to mrtg which simplify this. My work is based on earlier modification made by: matija.grabnar [at] arnes.si and kostas [at] nlanr.net.

<h2>MODIFICATIONS</h2>

 I added new code for displaying correct units to the previous patches ``perminute'' and ``perhour'' (``option'' tokens), which allows other measurement in addition to ``persecond''. 

 Then I created a new option token ``dorelpercent'' which allows the calculation of the percentage of IN-stream / OUT-stream on the fly and then displays it on a fixed scale from 0% to 100%. For my requirements, this does good work. Maybe someone wants a floating scale. It should not be a problem to implement it, too (but give me an option to keep my fixed scale). If IN-stream is always less than OUT-stream both lines (OUT-stream and relative percent) are always displayed on top of IN-stream bulk. Otherwise this option makes no sense. With this option you can display hitrates, errorrates (for router monitoring: rel. droprates) easily now. 

 If you use this options please consider that you need a 5th colourname/value pair in your Colours statements! 

 Due to some discussion on this list, I have implemented two tokens too: 

 ``kilo'' and ``kMG'' 

 ``kilo'' should contain the value of k (1000 or 1024), where 1000 is the default. 

 ``kMG'' is a comma separated list of multiplier prefixes, used instead of &quot;``, ''k``, ''M``, ''G``, ''T&quot; on the <font SIZE="-1">MRTG</font> display. Leave the place free, if you want no prefix. 

 Also an incomplete list of OIDs for the new <font SIZE="-1">SQUID</font> release is added. 

 You may need to turn on snmp_port in squid.conf to as it is disabled by default. 

 I hope you enjoy it.

<h2>CONFIG EXAMPLE</h2>

 First load the squid mib 

 <pre>
 LoadMIBs: /usr/share/squid/mib.txt
</pre> 

 You can measure responsetimes in ms and display it with <font SIZE="-1">MRTG</font> correctly with: 

 <pre><code>
kMG[measure - ms] : m, , k, M, G, T short[measure - ms] : s
</code></pre> 

 You can display now MB/s as 1024*1024 B/s with: 

 <pre>
 kilo[volume]: 1024
</pre> 

 Assuming you're not running squid's <font SIZE="-1">SNMP</font> on the default snmp port, you need to include a port number in your target line: 

 
Target[proxy - hit] : cacheHttpHits &amp;cacheProtoClientHttpRequests : public[at] localhost : 3401
 

 A sample config for squid: 

 <pre><code>
Target[proxy - hit] : cacheHttpHits &amp;cacheProtoClientHttpRequests : public[at] proxy
                                                                        Title[proxy - hit] : HTTP Hits
                                                                                                 PageTop[proxy - hit] : &lt;H2&gt;
                                                                                                                            proxy Cache Statistics : HTTP Hits /
                                                                                                                                                     Requests&lt;/ H2&gt;
                                                                                                                                                         Suppress[proxy - hit] : y
                                                                                                                                                                                     LegendI[proxy - hit] : HTTP hits
                                                                                                                                                                                                                LegendO[proxy - hit] : HTTP requests
                                                                                                                                                                                                                                           Legend1[proxy - hit] : HTTP hits
                                                                                                                                                                                                                                                                      Legend2[proxy - hit] : HTTP requests
                                                                                                                                                                                                                                                                                                 YLegend[proxy - hit] : perminute
                                                                                                                                                                                                                                                                                                                            ShortLegend[proxy - hit] : req /
                                                                                                                                                                                                                                                                                                                                                       min
                                                                                                                                                                                                                                                                                                                                                           Options[proxy - hit] : nopercent,
    perminute, dorelpercent Target[proxy - srvkbinout] : cacheServerInKb &amp;cacheServerOutKb : public[at] proxy Title[proxy - srvkbinout] : Cache Server Traffic In / Out PageTop[proxy - srvkbinout] : &lt;H2&gt; Cache Statistics : Server traffic volume(In / Out)&lt;/ H2&gt; Suppress[proxy - srvkbinout] : y LegendI[proxy - srvkbinout] : Traffic In LegendO[proxy - srvkbinout] : Traffic Out Legend1[proxy - srvkbinout] : Traffic In Legend2[proxy - srvkbinout] : Traffic Out YLegend[proxy - srvkbinout] : per minute ShortLegend[proxy - srvkbinout] : b / min kMG[proxy - srvkbinout] : k, M, G, T kilo[proxy - srvkbinout] : 1024 Options[proxy - srvkbinout] : nopercent, perminute
</code></pre>

<h2>AUTHOR</h2>

 Andreas Papst &lt;andreas.papst [at] univie.ac.at&gt; Dirk-Lu.der Kreie &lt;deelkar [at] gmx.de&gt; Chris Chiappa &lt;chris+debian [at] chiappa.net&gt; 

<h2>Index</h2>


