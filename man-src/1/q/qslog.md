---
title: "qslog(1)"
name: "qslog"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qslog/"
---

<h2 class="name">NAME</h2>
 

 qslog - collects request statistics from access log data. 

<h2>SYNOPSIS</h2>

 qslog -f &lt;format_string&gt; -o &lt;out_file&gt; [-p[c|u[c]] [-v]] [-x [&lt;num&gt;]] [-u &lt;name&gt;] [-m] [-c &lt;path&gt;]

<h2>DESCRIPTION</h2>

 qslog is a real time access log analyzer. It collects the data from stdin. The output is written to the specified file every minute and includes the following entries: 
&nbsp;<wbr>&nbsp;<wbr>- requests per second&nbsp;<wbr>(r/s) 
&nbsp;<wbr>&nbsp;<wbr>- number of requests within measured time&nbsp;<wbr>(req) 
&nbsp;<wbr>&nbsp;<wbr>- bytes sent to the client per second&nbsp;<wbr>(b/s) 
&nbsp;<wbr>&nbsp;<wbr>- bytes received from the client per second&nbsp;<wbr>(ib/s) 
&nbsp;<wbr>&nbsp;<wbr>- repsonse status codes within the last minute&nbsp;<wbr>(1xx,2xx,3xx,4xx,5xx) 
&nbsp;<wbr>&nbsp;<wbr>- average response duration&nbsp;<wbr>(av) 
&nbsp;<wbr>&nbsp;<wbr>- average response duration in milliseconds&nbsp;<wbr>(avms) 
&nbsp;<wbr>&nbsp;<wbr>- distribution of response durations within the last minute (&lt;1s,1s,2s,3s,4s,5s,&gt;5) 
&nbsp;<wbr>&nbsp;<wbr>- number of established&nbsp;<wbr>(new)&nbsp;<wbr>connections within the measured time&nbsp;<wbr>(esco) 
&nbsp;<wbr>&nbsp;<wbr>- average system load&nbsp;<wbr>(sl) 
&nbsp;<wbr>&nbsp;<wbr>- free memory&nbsp;<wbr>(m)&nbsp;<wbr>(not available for all platforms) 
&nbsp;<wbr>&nbsp;<wbr>- number of client ip addresses seen withn the last 600 seconds&nbsp;<wbr>(ip) 
&nbsp;<wbr>&nbsp;<wbr>- number of different users seen withn the last 600 seconds&nbsp;<wbr>(usr) 
&nbsp;<wbr>&nbsp;<wbr>- number of events identified by the&nbsp;<wbr>'E'&nbsp;<wbr>format character 
&nbsp;<wbr>&nbsp;<wbr>- number of mod_qos events within the last minute&nbsp;<wbr>(qV=create session, qS=session pass, qD=access denied, qK=connection closed, qT=dynamic keep-alive, qL=request/response slow down, qs=serialized request)

<h2>OPTIONS</h2>

<dl>
<dt>-f &lt;format_string&gt;
<dd> Defines the log data format and the positions of data elements processed by this utility. See to the 'LogFormat' directive of the httpd.conf file to see the format defintions of the servers access log data. 
&nbsp;<wbr>&nbsp;<wbr>qslog knows the following elements: 
&nbsp;<wbr>&nbsp;<wbr>I defines the client ip address&nbsp;<wbr>(%h) 
&nbsp;<wbr>&nbsp;<wbr>R defines the request line&nbsp;<wbr>(%r) 
&nbsp;<wbr>&nbsp;<wbr>S defines HTTP response status code&nbsp;<wbr>(%s) 
&nbsp;<wbr>&nbsp;<wbr>B defines the transferred bytes&nbsp;<wbr>(%b or&nbsp;<wbr>%O) 
&nbsp;<wbr>&nbsp;<wbr>i defines the received bytes&nbsp;<wbr>(%I) 
&nbsp;<wbr>&nbsp;<wbr>T defines the request duration&nbsp;<wbr>(%T) 
&nbsp;<wbr>&nbsp;<wbr>t defines the request duration in milliseconds&nbsp;<wbr>(may be used instead of T) 
&nbsp;<wbr>&nbsp;<wbr>D defines the request duration in microseconds&nbsp;<wbr>(may be used instead of T)&nbsp;<wbr>(%D) 
&nbsp;<wbr>&nbsp;<wbr>k defines the number of keepalive requests on the connection&nbsp;<wbr>(%k) 
&nbsp;<wbr>&nbsp;<wbr>U defines the user tracking id&nbsp;<wbr>(%{mod_qos_user_id}e) 
&nbsp;<wbr>&nbsp;<wbr>Q defines the mod_qos_ev event message&nbsp;<wbr>(%{mod_qos_ev}e) 
&nbsp;<wbr>&nbsp;<wbr>C defines the element for the detailed log&nbsp;<wbr>(-c option), e.g.&nbsp;<wbr>&quot;%U&quot; 
&nbsp;<wbr>&nbsp;<wbr>s arbitrary counter to add up&nbsp;<wbr>(sum within a minute) 
&nbsp;<wbr>&nbsp;<wbr>a arbitrary counter to build an average from&nbsp;<wbr>(average per request) 
&nbsp;<wbr>&nbsp;<wbr>A arbitrary counter to build an average from&nbsp;<wbr>(average per request) 
&nbsp;<wbr>&nbsp;<wbr>E comma separated list of event strings 
&nbsp;<wbr>&nbsp;<wbr>c content type&nbsp;<wbr>(%{content-type}o), available in -pc mode only 
&nbsp;<wbr>&nbsp;<wbr>m request method&nbsp;<wbr>(GET/POST)&nbsp;<wbr>(%m), available in -pc mode only 
&nbsp;<wbr>&nbsp;<wbr>. defines an element to ignore&nbsp;<wbr>(unknown string) 

<dt>-o &lt;out_file&gt;
<dd> Specifies the file to store the output to. stdout is used if this option is not defined.
<dt>-p
<dd> Used for post processing when reading the log data from a file (cat/pipe). qslog is started using it's offline mode (extracting the time stamps from the log lines) in order to process existing log files. The option &quot;-pc&quot; may be used alternatively if you want to gather request information per client (identified by IP address (I) or user tracking id (U) showing how many request each client has performed within the captured period of time). &quot;-pc&quot; supports the format characters IURSBTtDkEcm. The option &quot;-pu&quot; collects statistics on a per URL level (supports format characters RSTtD). &quot;-puc&quot; is very similar to &quot;-pu&quot; but cuts the end (handler) of each URL.
<dt>-v
<dd> Verbose mode.
<dt>-x [&lt;num&gt;]
<dd> Rotates the output file once a day (move). You may specify the number of rotated files to keep. Default are 14.
<dt>-u &lt;name&gt;
<dd> Becomes another user, e.g. www-data.
<dt>-m
<dd> Calculates free system memory every minute.
<dt>-c &lt;path&gt;
<dd> Enables the collection of log statitics for different request types. 'path' specifies the necessary rule file. Each rule consists of a rule identifier and a regular expression to identify a request seprarated by a colon, e.g., 01:^(/a)|(/c). The regular expressions are matched against the log data element which has been identified by the 'C' format character.</dl>

<h2>EXAMPLE</h2>

 Configuration using pipped logging: 

 
&nbsp;<wbr>&nbsp;<wbr>CustomLog&nbsp;<wbr>&quot;|/bin/qslog -f ISBTQ -x -o&nbsp;<wbr>/var/logs/stat.csv&quot;&nbsp;<wbr>&quot;%h&nbsp;<wbr>%&gt;s&nbsp;<wbr>%b&nbsp;<wbr>%T&nbsp;<wbr>%{mod_qos_ev}e&quot; 

 Post processing: 

 
&nbsp;<wbr>&nbsp;<wbr>LogFormat&nbsp;<wbr>&quot;%t&nbsp;<wbr>%h&nbsp;<wbr>\&quot;%r\&quot;&nbsp;<wbr>%&gt;s&nbsp;<wbr>%b&nbsp;<wbr>\&quot;%{User-Agent}i\&quot;&nbsp;<wbr>%T&quot; 
&nbsp;<wbr>&nbsp;<wbr>cat access_log |&nbsp;<wbr>/bin/qslog -f ..IRSB.T -o&nbsp;<wbr>/var/logs/stat.csv -p 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qsexec/">qsexec</a>(1), <a HREF="/docs/linux/man/1-qsfilter2/">qsfilter2</a>(1), <a HREF="/docs/linux/man/1-qsgeo/">qsgeo</a>(1), <a HREF="/docs/linux/man/1-qsgrep/">qsgrep</a>(1), <a HREF="/docs/linux/man/1-qshead/">qshead</a>(1), <a HREF="/docs/linux/man/1-qslogger/">qslogger</a>(1), <a HREF="/docs/linux/man/1-qspng/">qspng</a>(1), <a HREF="/docs/linux/man/1-qsrotate/">qsrotate</a>(1), <a HREF="/docs/linux/man/1-qssign/">qssign</a>(1), <a HREF="/docs/linux/man/1-qstail/">qstail</a>(1)

<h2>AUTHOR</h2>

 Pascal Buchbinder, <a rel="nofollow" HREF="http://opensource.adnovum.ch/mod_qos/">http://opensource.adnovum.ch/mod_qos/</a> 

<h2>Index</h2>


