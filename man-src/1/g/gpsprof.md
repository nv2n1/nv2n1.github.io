---
title: "gpsprof(1)"
name: "gpsprof"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsprof/"
description: "gpsprof – profile a GPS and gpsd, plotting latency information"
---

<h2 class="name">NAME</h2>
<p> gpsprof &#8211; profile a GPS and gpsd, plotting latency information </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpsprof</code> [-f&nbsp;<wbr><i>plot_type</i>] [-m&nbsp;<wbr><i>threshold</i>] [-n&nbsp;<wbr><i>packetcount</i>] [-t&nbsp;<wbr><i>title</i>] [-T&nbsp;<wbr><i>terminal</i>] [-d&nbsp;<wbr><i>dumpfile</i>] [-l&nbsp;<wbr><i>logfile</i>] [-r] [-D&nbsp;<wbr><i>debuglevel</i>] [-h] [[server[:port[:device]]]]</dl>
<h2>DESCRIPTION</h2>
<dd>gpsprof performs accuracy, latency, and time drift profiling on a GPS. It emits to standard output a GNUPLOT program that draws one of several illustrative graphs. It can also be told to emit the raw profile data. </p>
<p> Information from the default spatial plot it provides can be useful for establishing an upper bound on latency, and thus on position accuracy of a GPS in motion. </p>
<p> gpsprof uses instrumentation built into gpsd. </p>
<p> To display the graph, use <code><a href="/docs/linux/man/1-gnuplot/">gnuplot</a></code>(1). Thus, for example, to display the default spatial scatter plot, do this: </p>
<dl>
<dt>
<dd>
<pre>
gpsprof | gnuplot -persist
</pre>
</dl>
<p> To generate an image file: </p>
<dl>
<dt>
<dd>
<pre>
gpsprof -T png | gnuplot &gt;image.png
</pre>
</dl>
<h2>OPTIONS</h2>
<p> The -f option sets the plot type. The X axis is samples (either sentences with timestamps or PPS time drift messages). The Y axis is normally latency in seconds, except for the spatial plot. Currently the following plot types are defined: </p>
<p> space</p>
<dl>
<dt>
<dd> Generate a scattergram of fixes and plot a probable-error circle. This data is only meaningful if the GPS is held stationary while gpsprof is running. This is the default.</dl>
<p> time</p>
<dl>
<dt>
<dd> Plot delta of system clock (NTP corrected time) against GPS time as reported in PPS messages.</dl>
<p> uninstrumented</p>
<dl>
<dt>
<dd> Plot total latency without instrumentation. Useful mainly as a check that the instrumentation is not producing significant distortion. It only plots times for reports that contain fixes; staircase-like artifacts in the plot are created when elapsed time from reports without fixes is lumped in.</dl>
<p> instrumented</p>
<dl>
<dt>
<dd> Plot instrumented profile. Plots various components of the total latency between the GPS&#8217;s fix time fix and when the client receives the fix.</dl>
<p> For purposes of the description, below, start-of-reporting-cycle (SORC) is when a device&#8217;s reporting cycle begins. This time is detected by watching to see when data availability follows a long enough amount of quiet time that we can be sure we&#8217;ve seen the gap at the end of the sensor&#8217;s previous report-transmission cycle. Detecting this gap requires a device running at 9600bps or faster. </p>
<p> Similarly, EORC is end-of-reporting-cycle; when the daemon has seen the last sentence it needs in the reporting cycle and ready to ship a fix to the client. </p>
<p> The components of the instrumented plot are as follows: </p>
<p> Fix latency</p>
<dl>
<dt>
<dd> Delta between GPS time and SORC.</dl>
<p> RS232 time</p>
<dl>
<dt>
<dd> RS232 transmission time for data shipped during the cycle (computed from character volume and baud rate).</dl>
<p> Analysis time</p>
<dl>
<dt>
<dd> EORC, minus SORC, minus RS232 time. The amount of real time the daemon spent on computation rather than I/O.</dl>
<p> Reception time</p>
<dl>
<dt>
<dd> Shipping time from the daemon to when it was received by gpsprof.</dl>
<p> Because of RS232 buffering effects, the profiler sometimes generates reports of ridiculously high latencies right at the beginning of a session. The -m option lets you set a latency threshold, in multiples of the cycle time, above which reports are discarded. </p>
<p> The -n option sets the number of packets to sample. The default is 100. </p>
<p> The -t option sets a text string to be included in the plot title. </p>
<p> The -T option generates a terminal type setting into the gnuplot code. Typical usage is &quot;-T png&quot; telling gnuplot to write a PNG file. Without this option gnuplot will call its X11 display code. </p>
<p> The -d option dumps the plot data, without attached gnuplot code, to a specified file for post-analysis. </p>
<p> The -l option dumps the raw JSON reports collected from the device to a specified file. </p>
<p> The -r option replots from a JSON logfile (such as -l produces) on standard input. Both -n and -l options are ignored when this one is selected. </p>
<p> The -h option makes gpsprof print a usage message and exit. </p>
<p> The -D sets debug level. </p>
<p> Sending SIGUSR1 to a running instance causes it to write a completion message to standard error and resume processing. The first number in the startup message is the process ID to signal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gpscat/">gpscat</a></code>(1), <code><a href="/docs/linux/man/1-gnuplot/">gnuplot</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. </p>
<h2>Index</h2>
