---
title: "sispmctl(1)"
name: "sispmctl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sispmctl/"
description: "sispmctl – Gembird Silver Shield PM ConTroL program"
---

<h2 class="name">NAME</h2>
<p> sispmctl &#8211; Gembird Silver Shield PM ConTroL program</p>
<h2>SYNOPSIS</h2>
<p> <code>sispmctl</code> <i>-s</i> </p>
<p> <code>sispmctl [</code> <i>-q</i> <code>] [</code> <i>-n</i> <code>] [</code> <i>-d</i> <code>0&#8230; ]</code> <code>[</code> <i>-D</i> <code>&#8230; ]</code> <i>-b</i> <code>&lt;on|off&gt;</code> </p>
<p> <code>sispmctl [</code> <i>-q</i> <code>] [</code> <i>-n</i> <code>] [</code> <i>-d</i> <code>0&#8230; ]</code> <code>[</code> <i>-D</i> <code>&#8230; ] &lt;</code> <i>-o</i> <code>|</code> <i>-f</i> <code>|</code> <i>-t</i> <code>|</code> <i>-g</i> <code>|</code> <i>-m</i> <code>&gt; &lt;1..4|all&gt;</code> </p>
<p> <code>sispmctl [</code> <i>-q</i> <code>] [</code> <i>-n</i> <code>] [</code> <i>-d</i> <code>0&#8230; ]</code> <code>[</code> <i>-D</i> <code>&#8230; ] &lt;</code> <i>-a</i> <code>|</code> <i>-A</i> <code>&gt; &lt;1..4|all&gt;</code> <code>[</code> <i>&#8211;Aat</i> <code>&#8216;&#8230;&#8217; ] [</code> <i>&#8211;Aafter</i> <code>&#8230; ] [</code> <i>&#8211;Ado</i> <code>&lt;on|off&gt; ] &#8230; [</code> <i>&#8211;Aloop</i> <code>&#8230; ]</code> </p>
<p> <code>sispmctl [</code> <i>-d</i> <code>0&#8230; ]</code> <code>[</code> <i>-D</i> <code>&#8230; ] [</code> <i>-i &lt;ip&gt;</i> <code>] [</code> <i>-p &lt;#port&gt;</i> <code>] [</code> <i>-u &lt;path&gt;</i> <code>]</code> <i>-l</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>sispmctl</code> is a tool to switch the USB controlled outlets of Gembird Silver Shield PM. It is known by many names, e.g. Revolt Power Switch. </p>
<p> It is coded in C and uses the usb specific library (LibUSB). This allows you a portable and fast solution. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</p>
<dd> print usage information</p>
<dt>-s</p>
<dd> scan for supported GEMBIRD devices</p>
<dt>-l</p>
<dd> daemonize and start to listening as a simple http webserver (default port: 2638)</p>
<dt>-p</p>
<dd> IP network port (default: 2638) for listener. There is no authentication implemented yet.</p>
<dt>-u</p>
<dd> give the directory path where pages lay, that are served (default: /usr/local/httpd/sispmctl). The Web path component is completely ignored for security reasons.</p>
<dt>-b</p>
<dd> switch the buzzer on and off</p>
<dt>-o</p>
<dd> switch the given outlet(s) to &quot;ON&quot;</p>
<dt>-f</p>
<dd> switch the given outlet(s) to &quot;OFF&quot;</p>
<dt>-t</p>
<dd> toggle the state of the given outlet(s)</p>
<dt>-g</p>
<dd> show the status of the given outlet(s)</p>
<dt>-m</p>
<dd> get power supply status for the given outlet(s)</p>
<dt>-d</p>
<dd> Use not the first but the given device in the sequence of detected devices, starting with &quot;0&quot; for the first device (see scan option)</p>
<dt>-D</p>
<dd> Same as -d, but choose by serial number (see scan option)</p>
<dt>-n</p>
<dd> do not print &quot;ON&quot; and &quot;OFF&quot;, but &quot;1&quot; and &quot;0&quot; instead</p>
<dt>-q</p>
<dd> do neither print explanations nor disclaimers except it is requested</p>
<dt>-a</p>
<dd> get plannification for given outlet</p>
<dt>-A</p>
<dd> set plannification for given outlet<br />
&nbsp;<wbr>&#8211;Aat&nbsp;<wbr>&quot;date&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; sets an event time as a date&nbsp;<wbr>&#8216;%Y-%m-%d&nbsp;<wbr>%H:%M&#8217;<br />
&nbsp;<wbr>&#8211;Aafter N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; sets an event time as N minutes after the previous one<br />
&nbsp;<wbr>&#8211;Ado&nbsp;<wbr>&lt;on|off&gt;&nbsp;<wbr>&#8211; sets the current event&#8217;s action<br />
&nbsp;<wbr>&#8211;Aloop N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; loops to 1st event&#8217;s action after N minutes</p>
<dt>-v</p>
<dd> print version &amp; copyright </p>
</dl>
<h2>WEB INTERFACE</h2>
<p> The sispmctl program provides a web interface when started with the <i>-l</i> option. No additional http server is needed. Each selected usb device is blocked by sispmctl while running. </p>
<p> After installation, the first of two web-interfaces is selected. The default location of the HTML files is /usr/local/httpd/sispmctl/doc which is a symbolic link to /usr/local/httpd/sispmctl/skin1. </p>
<p> The http capabilities of sispmctl are limited. Technically speaking, only the first line of each http request is parsed. The terminating path component, i.e. file name, is looked up in the repository directory. If present the file is parsed and in absence of control sequences sent as is. The files must include the http header portion. </p>
<p> Control sequences start and end with double dollar `$$&#8217;. They consist of a command portion separated by a question mark `?&#8217; from alternative outputs which are separated by the first colon `:&#8217;. The command portion is a token followed by an embraced number that references the outlet, e.g. <i>$$<a href="/docs/linux/man/1-command/">command</a>(1)?positive:negative$$</i> while command is one of <code>status,</code> <code>toggle,</code> <code>on</code> or <code>off.</code> I strongly recommend to avoid the on/off/toggle commands in pages that may be reloaded. Best is to redirect to other pages that only include status requests. </p>
<h2>PLANNIFICATIONS</h2>
<p> The sispmctl program provides plannifications, plannifications can be used to turn given outlets of the device &quot;ON&quot; or &quot;OFF&quot; at or after a given time. Plannifications can also be set to loop after a given number of minutes. </p>
<p> To show the planned plannification for a given outlet use the option <i>-a</i> and specify the wanted outlet(s). The option <i>-A</i> plus any of the options <i>&#8211;Aat</i> , <i>&#8211;Aafter</i> , <i>&#8211;Ado</i> and <i>&#8211;Aloop</i> will create a new plannification for the given output. If only <i>-A</i> plus an outlet is called, the plannification for the outlet will be deleted. </p>
<h2>EXAMPLES</h2>
<p> Switch off the first outlet of the first SiS-PM and the third outlet of the second SiS-PM: </p>
<p> <code>sispmctl -f 1 -d 1 -f 3</code> </p>
<p> Print the status of the forth outlet as zero or one: </p>
<p> <code>sispmctl -nqg 4</code> </p>
<p> Set a planification so outlet 2 on the first device gets turned &quot;ON&quot; on the given date and time: </p>
<p> <code>sispmctl -A 2 &#8211;Aat &#8216;2011-07-27 20:45&#8217; &#8211;Ado on</code> </p>
<p> Set a planification so outlet 3 on the second device gets turned &quot;ON&quot; after 2 minutes and &quot;OFF&quot; after another 10 minutes. The planification will loop after 1 hour: </p>
<p> <code>sispmctl -d 1 -A 3 &#8211;Aafter 2 &#8211;Ado on &#8211;Aafter 10 &#8211;Ado off &#8211;Aloop 60</code> </p>
<p> Run sispmctl on the second device as a web-server: </p>
<p> <code>sispmctl -d 1 -l</code> </p>
<p> You can connect to it from the same machine by pointing to <a rel="nofollow" href="http://localhost:2638">http://localhost:2638</a> with your webbrowser </p>
<h2>AUTHOR</h2>
<p> First version by Mondrian Nuessle, nuessle [at] uni-mannheim.de </p>
<p> Web integration and man page by Andreas Neuper, ANeuper-at-web-dot-de </p>
<p> Plannifications by Olivier Matheret </p>
<h2>Index</h2>
