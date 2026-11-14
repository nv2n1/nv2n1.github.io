---
title: "rahisto(1)"
name: "rahisto"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rahisto/"
description: "rahisto – print histogram of metrics from argus(8) data."
---

<h2>NAME</h2>
<p> <code>rahisto</code> &#8211; print histogram of metrics from <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>SYNOPSIS</h2>
<p> <code>rahisto</code> [<code>-M</code> <i>histomode</i>] <code>-H</code> <i>bin[L]:range|size</i> &#8230; [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rahisto</code> reads <code>argus</code> data from an <i>argus-data</i> source, sorts the records based on the criteria specified on the command line, and outputs a valid <i>argus-stream</i>.</p>
<h2>OPTIONS</h2>
<p> Rahisto, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-rahisto/">rahisto</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-M nozero</code></p>
<dd> Don&#8217;t print bins that have zero frequencies.</p>
<dt><code>-M outlayer</code></p>
<dd> Print accumulated stats for outlayer values, i.e. the values that are outside the histogram range.</p>
<dt><code>-H</code><i> metric bin[L]:range | size</i></p>
<dd>
<dt>Supported metrics are:</p>
<dd></dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>dur</code></p>
<dd> record total duration.</p>
<dt><code>avgdur</code></p>
<dd> record average duration.</p>
<dt><code>proto</code></p>
<dd> transaction protocol.</p>
<dt><code>sport</code></p>
<dd> source port number.</p>
<dt><code>dport</code></p>
<dd> destination port number.</p>
<dt><code>stos</code></p>
<dd> source TOS byte value.</p>
<dt><code>dtos</code></p>
<dd> destination TOS byte value.</p>
<dt><code>sttl</code></p>
<dd> src -&gt; dst TTL value.</p>
<dt><code>dttl</code></p>
<dd> dst -&gt; src TTL value.</p>
<dt><code>[s|d]bytes</code></p>
<dd> [src | dst] transaction bytes.</p>
<dt><code>[s|d]appbytes</code></p>
<dd> [src | dst] application bytes.</p>
<dt><code>[s|d]pkts</code></p>
<dd> [src | dst] packet count.</p>
<dt><code>[s|d]meansz</code></p>
<dd> [src | dst] mean packet size.</p>
<dt><code>[s|d]load</code></p>
<dd> packets per second.</p>
<dt><code>[s|d]loss</code></p>
<dd> pkts retransmitted or dropped.</p>
<dt><code>[s|d]ploss</code></p>
<dd> percent pkts retransmitted or dropped.</p>
<dt><code>[s|d]rate</code></p>
<dd> bits per second.</dl>
</dl>
<h2>INVOCATION</h2>
<p> A sample invocation of <code><a href="/docs/linux/man/1-rahisto/">rahisto</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and generates a frequency distribution histogram for the transaction duration for HTTP traffic. </p>
<pre>
<font SIZE="-2">% rahisto -H dur 10 -r ~/argus/data/argus*out.gz - port http
 N = 194     mean = 15.928685  stddev = 23.728876  max = 81.354462  min = 0.008055
           median =  0.079948     95% = 59.208977
 Class     Interval         Freq    Rel.Freq     Cum.Freq    
     1   0.000000e+00        123    63.4021%     63.4021%    
     2   8.200000e+00          7     3.6082%     67.0103%    
     3   1.640000e+01         13     6.7010%     73.7113%    
     4   2.460000e+01          9     4.6392%     78.3505%    
     5   3.280000e+01          0     0.0000%     78.3505%    
     6   4.100000e+01          0     0.0000%     78.3505%    
     7   4.920000e+01          6     3.0928%     81.4433%    
     8   5.740000e+01         35    18.0412%     99.4845%    
     9   6.560000e+01          0     0.0000%     99.4845%    
    10   7.380000e+01          1     0.5155%    100.0000%  
</font>
</pre>
<p> A sample invocation where the call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and generates a frequency distribution histogram for the round-trip time of arp volleys in <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data. </p>
<pre>
<font SIZE="-2">% rahisto -H dur 10:0-75u  -R /Vol*/Data/Archive/split/*68/2012/0[23] - arp and dur gt 0
 N = 360     mean = 0.000028  stddev = 0.000007  max = 0.000066  min = 0.000014
           median = 0.000031     95% = 0.000028
             mode = 0.000026
 Class     Interval         Freq    Rel.Freq     Cum.Freq    
     1   0.000000e+00          0     0.0000%      0.0000%    
     2   7.500000e-06          2     0.5556%      0.5556%    
     3   1.500000e-05         63    17.5000%     18.0556%    
     4   2.250000e-05        188    52.2222%     70.2778%    
     5   3.000000e-05         71    19.7222%     90.0000%    
     6   3.750000e-05         23     6.3889%     96.3889%    
     7   4.500000e-05         10     2.7778%     99.1667%    
     8   5.250000e-05          2     0.5556%     99.7222%    
     9   6.000000e-05          1     0.2778%    100.0000%    
    10   6.750000e-05          0     0.0000%    100.0000% 
</font></pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
