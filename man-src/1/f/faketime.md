---
title: "faketime(1)"
name: "faketime"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faketime/"
description: "faketime – manipulate the system time for a given command"
---

<h2>NAME</h2>
<p> faketime &#8211; manipulate the system time for a given command</p>
<h2>SYNOPSIS</h2>
<p> <code>faketime</code> <i>[options] timestamp program [arguments&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> The given command will be tricked into believing that the current system time is the one specified in the timestamp. The wall clock will continue to run from this date and time unless specified otherwise (see advanced options). Actually, faketime is a simple wrapper for libfaketime, which uses the LD_PRELOAD mechanism to load a small library which intercepts system calls to functions such as <i><a href="/docs/linux/man/2-time/">time</a>(2)</i> and <i><a href="/docs/linux/man/2-fstat/">fstat</a>(2)</i>. This wrapper exposes only a subset of libfaketime&#8217;s functionality; please refer to the README file that came with faketime for more details and advanced options, or have a look at <a rel="nofollow" href="http://github.com/wolfcw/libfaketime">http://github.com/wolfcw/libfaketime</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> show usage information and quit.</p>
<dt><code>&#8211;version</code></p>
<dd> show version information and quit.</p>
<dt><code>-m</code></p>
<dd> use the multi-threading variant of libfaketime.</p>
<dt><code>-f</code></p>
<dd> use the advanced timestamp specification format. </p>
</dl>
<h2>EXAMPLES</h2>
<pre><code>
faketime 'last Friday 5 pm' /bin/date
faketime '2008-12-24 08:15:42' /bin/date
faketime -f '+2,5y x10,0' /bin/bash -c 'date; while true; do echo $SECONDS ; sleep 1 ; done'
faketime -f '+2,5y x0,50' /bin/bash -c 'date; while true; do echo $SECONDS ; sleep 1 ; done'
faketime -f '+2,5y i2,0' /bin/bash -c 'while true; do date ; sleep 1 ; done'
In this single case all spawned processes will use the same global clock without restaring it at the start of each process.
(Please note that it depends on your locale settings whether . or , has to be used for fractional offsets)
</code></pre>
<h2>ADVANCED TIMESTAMP FORMAT</h2>
<p> The simple timestamp format used by default applies the <code>/bin/date -d</code> command to parse user-friendly specifications such as &#8216;last friday&#8217;. When using the faketime option <code>-f</code>, the timestamp specified on the command line is directly passed to libfaketime, which enables a couple of additional features such as speeding the clock up or slowing it down for the target program. It is strongly recommended that you have a look at the libfaketime documentation. Summary:</p>
<dl>
<dt>Freeze clock at absolute timestamp: <code>&quot;YYYY-MM-DD hh:mm:ss&quot;</code></p>
<dd> If you want to specify an absolute point in time, exactly this format must be used. Please note that freezing the clock is usually not what you want and may break the application. Only use if you know what you&#8217;re doing!</p>
<dt>Relative time offset: <code>&quot;[+/-]123[m/h/d/y]</code>, e.g. &quot;+60m&quot;, &quot;+2y&quot;</p>
<dd> This is the most often used format and specifies the faked time relatively to the current real time. The first character of the format string <code>must</code> be a + or a -. The numeric value by default represents seconds, but the modifiers m, h, d, and y can be used to specify minutes, hours, days, or years, respectively. For example, &quot;-2y&quot; means &quot;two years ago&quot;. Fractional time offsets can be used, e.g. &quot;+2,5y&quot;, which means &quot;two and a half years in the future&quot;. Please note that the fraction delimiter depends on your locale settings, so if &quot;+2,5y&quot; does not work, you might want to try &quot;+2.5y&quot;.</p>
<dt>Start-at timestamps: <code>&quot;@YYYY-MM-DD hh:mm:ss&quot;</code></p>
<dd> The wall clock will start counting at the given timestamp for the program. This can be used for specifying absolute timestamps without freezing the clock.</dl>
<h2>ADVANCED USAGE</h2>
<p> When using relative time offsets or start-at timestamps (see ADVANCED TIMESTAMP FORMAT above and option <code>-f</code>), the clock speed can be adjusted, i.e. time may run faster or slower for the executed program. For example, <code>&quot;+5y x10&quot;</code> will set the faked time 5 years into the future and make the time pass 10 times as fast (one real second equals 10 seconds measured by the program). Similarly, the flow of time can be slowed, e.g. using <code>&quot;-7d x0,2&quot;</code>, which will set the faked time 7 days in the past and set the clock speed to 20 percent, i.e. it takes five real world seconds for one second measured by the program. Again, depending on your locale, either &quot;x2.0&quot; or &quot;x2,0&quot; may be required regarding the delimiter. You can also make faketime to advance the reported time by a preset interval upon each time() call independently from the system&#8217;s time using <code>&quot;-7d i2,0&quot;</code>, where <code>&quot;i&quot;</code> is followed by the increase interval in seconds. </p>
<p> Faking times for multiple programs or even system-wide can be simplified by using ~/.faketimerc files and /etc/faketimerc. Please refer to the README that came with faketime for warnings and details.</p>
<h2>AUTHOR</h2>
<p> Please see the README and NEWS files for contributers.</p>
<h2>BUGS</h2>
<p> Due to limitations of the LD_PRELOAD mechanism, faketime will not work with suidroot and statically linked programs. While timestamps and time offsets will work for child processes, speeding the clock up or slowing it down might not work for child processes spawned by the executed program as expected; a new instance of libfaketime is used for each child process, which means that the libfaketime start time, which is used in speed adjustments, will also be re-initialized. Some programs may dynamically load system libraries, such as librt, at run-time and therefore bypass libfaketime. You may report programs that do not work with libfaketime, but only if they are available as open source.</p>
<h2>REPORTING BUGS</h2>
<p> Please use <a rel="nofollow" href="https://github.com/wolfcw/libfaketime/issues">https://github.com/wolfcw/libfaketime/issues</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2013 by the libfaketime authors. </p>
<p> There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. You may redistribute copies of faketime under the terms of the GNU General Public License.<br />
 For more information about these matters, see the file named COPYING.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ld-so/">ld.so</a>(1), <a href="/docs/linux/man/2-time/">time</a>(2), <a href="/docs/linux/man/2-fstat/">fstat</a>(2) </p>
<h2>Index</h2>
