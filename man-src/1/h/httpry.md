---
title: "httpry(1)"
name: "httpry"
section: "1"
letter: "h"
url: "/docs/linux/man/1-httpry/"
description: "httpry – HTTP logging and information retrieval tool"
---

<h2>NAME</h2>
<p> httpry &#8211; HTTP logging and information retrieval tool</p>
<h2>SYNOPSIS</h2>
<p> <code>httpry [ -dFpq ] [ -b file ] [ -f format ] [ -i device ] [ -m methods ] [ -n count ] [ -o file ] [ -P file ] [ -r file ] [ -S bytes ] [ -u user ] [ &#8216;expression&#8217; ]</code><br />
 <code>httpry -s [ -l threshold ] [ -t seconds ]</code><br />
 <code>httpry -h</code> </p>
<h2>DESCRIPTION</h2>
<p> <i>httpry</i> is a tool designed for displaying and logging HTTP traffic. It is not designed to perform analysis itself, but instead to capture, parse and log the traffic for later analysis. It can be run in real-time displaying the live traffic on the wire, or as a daemon process that logs to an output file.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-b <i>file</i></p>
<dd> Write all processed HTTP packets to a binary pcap dump file. Useful for further analysis of logged data.</p>
<dt>-d</p>
<dd> Run the program as a daemon process. All program status output will be sent to syslog. A pid file is created for the process in /var/run/httpry.pid by default. Requires an output file specified with -o.</p>
<dt>-f <i>format</i></p>
<dd> Provide a comma-delimited string specifying the parsed HTTP data to output. See the doc/format-string file for further information regarding available options and syntax.</p>
<dt>-F</p>
<dd> Disable all output buffering. This may be helpful when piping httpry output into another program.</p>
<dt>-h</p>
<dd> Display a brief description of these options.</p>
<dt>-i <i>device</i></p>
<dd> Specify an ethernet interface for the program to listen on. If not specified, the program will poll the system for a list of interfaces and select the first one found.</p>
<dt>-l <i>threshold</i></p>
<dd> Specify a requests per second rate threshold value when running in rate statistics mode (-s). Only hosts with a rps value greater than or equal to this number will be displayed. Defaults to 1.</p>
<dt>-m <i>methods</i></p>
<dd> Provide a comma-delimited string that specifies the request methods to parse. The program defaults to parsing all of the standard RFC2616 method strings if this option is not set. See the doc/method-string file for more information.</p>
<dt>-n <i>count</i></p>
<dd> Parse this number of HTTP packets and then exit. Defaults to 0, which means loop forever.</p>
<dt>-o <i>file</i></p>
<dd> Specify an output file for writing parsed packet data.</p>
<dt>-p</p>
<dd> Do not put the NIC in promiscuous mode on startup. Note that the NIC could already be in that mode for another reason.</p>
<dt>-P <i>file</i></p>
<dd> Specify a path and filename for creating the PID file in daemon mode.</p>
<dt>-q</p>
<dd> Suppress non-critical output (startup banner, statistics, etc.).</p>
<dt>-r <i>file</i></p>
<dd> Provide an input capture file to read from instead of performing a live capture. This option does not require root privileges.</p>
<dt>-s</p>
<dd> Run httpry in an HTTP request per second display mode. This periodically displays the rate per active host and total rate at a specified interval.</p>
<dt>-S</p>
<dd> Specify a number of bytes to skip in the ethernet header. This allows for custom header offsets to be accounted for.</p>
<dt>-t <i>seconds</i></p>
<dd> Specify the host statistics display interval in seconds when running in rate statistics mode (-s). Defaults to 5 seconds.</p>
<dt>-u <i>user</i></p>
<dd> Specify an alternate user to take ownership of the process and any output files. You will need root privileges to do this; it will switch to the new user after initialization.</p>
<dt>&#8216;expression&#8217;</p>
<dd> Specify a bpf-style capture filter, overriding the default. Here are a few basic examples starting with the default filter: </p>
<p>&nbsp;<wbr>&#8216;tcp port 80 or 8080&#8217;<br />
&nbsp;<wbr>&#8216;tcp dst port 80&#8217;<br />
&nbsp;<wbr>&#8216;tcp dst port 80 and src host 192.168.1.1&#8217; </p>
<p> These filters will capture all web traffic both directions on two common ports, capture only requests made to port 80, and capture requests to port 80 by a particular host, respectively. See &#8216;man tcpdump&#8217; for further information on the syntax and available primitives.</dl>
<h2>AUTHOR</h2>
<p> <i>httpry</i> was written by Jason Bittel &lt;jason.bittel [at] gmail.com&gt;. See included COPYING file for specific licensing information </p>
<h2>Index</h2>
