---
title: "perf-kvm(1)"
name: "perf-kvm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-kvm/"
description: "perf-kvm – Tool to trace/measure kvm guest os"
---

<h2 class="name">NAME</h2>
<p> perf-kvm &#8211; Tool to trace/measure kvm guest os </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf kvm[--host][--guest][--guestmount = &lt;path&gt;[--guestkallsyms = &lt;path&gt; --guestmodules = &lt;path&gt; | --guestvmlinux = &lt;path&gt;]]{top | record | report | diff | buildid - list}[&lt;options&gt;] perf kvm[--host][--guest][--guestkallsyms = &lt;path&gt; --guestmodules = &lt;path&gt; | --guestvmlinux = &lt;path&gt;]{top | record | report | diff | buildid - list | stat}[&lt;options&gt;]
'perf kvm stat [record|report|live] [&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> There are a couple of variants of perf kvm: </p>
<dl>
<dt>
<dd>
<pre>
'perf kvm [options] top &lt;command&gt;' to generates and displays
a performance counter profile of guest os in realtime
of an arbitrary workload.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
'perf kvm record &lt;command&gt;' to record the performance counter profile
    of an arbitrary workload and save it into a perf data file.We set the default behavior of perf kvm as-- guest,
    so if neither-- host nor-- guest
        is input,
    the perf data file name is perf.data.guest.If-- host is input,
    the perf data file name is perf.data.kvm.If you want to record data into
        perf.data.host,
    please input-- host-- no - guest.The behaviors are shown as following : Default('')-&gt;perf.data.guest-- host-&gt;perf.data.kvm-- guest-&gt;perf.data.guest-- host-- guest-&gt;perf.data.kvm-- host-- no - guest-&gt;perf.data.host
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'perf kvm report' to display the performance counter profile information
recorded via perf kvm record.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'perf kvm diff' to displays the performance difference amongst two perf.data
files captured via perf record.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'perf kvm buildid-list' to  display the buildids found in a perf data file,
so that other tools can be used to fetch packages with matching symbol tables
for use by perf report. As buildid is read from /sys/kernel/notes in os, then
if you want to list the buildid for guest, please make sure your perf data file
was captured with --guestmount in perf kvm record.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'perf kvm stat &lt;command&gt;' to run a command and gather performance counter
statistics.
Especially, perf 'kvm stat record/report' generates a statistical analysis
of KVM events. Currently, vmexit, mmio (x86 only) and ioport (x86 only)
events are supported. 'perf kvm stat record &lt;command&gt;' records kvm events
and the events between start and end &lt;command&gt;.
And this command produces a file which contains tracing results of kvm
events.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'perf kvm stat report' reports statistical data which includes events
handled time, samples, and so on.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'perf kvm stat live' reports statistical data in a live mode (similar to
record + report but with statistical data updated live at a given display
rate).
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -i, &#8211;input=&lt;path&gt;</p>
<dl>
<dt>
<dd> Input file name.</dl>
<p> -o, &#8211;output=&lt;path&gt;</p>
<dl>
<dt>
<dd> Output file name.</dl>
<p> &#8211;host</p>
<dl>
<dt>
<dd> Collect host side performance profile.</dl>
<p> &#8211;guest</p>
<dl>
<dt>
<dd> Collect guest side performance profile.</dl>
<p> &#8211;guestmount=&lt;path&gt;</p>
<dl>
<dt>
<dd> Guest os root file system mount directory. Users mounts guest os root directories under &lt;path&gt; by a specific filesystem access method, typically, sshfs. For example, start 2 guest os. The one&#8217;s pid is 8888 and the other&#8217;s is 9999. #mkdir /guestmount; cd/guestmount #sshfs -o allow_other,direct_io -p 5551 localhost:/ 8888/ #sshfs -o allow_other,direct_io -p 5552 localhost:/ 9999/ #perf kvm &#8211;host &#8211;guest &#8211;guestmount=~/guestmount top</dl>
<p> &#8211;guestkallsyms=&lt;path&gt;</p>
<dl>
<dt>
<dd> Guest os /proc/kallsyms file copy. <i>perf</i> kvm&#8217; reads it to get guest kernel symbols. Users copy it out from guest os.</dl>
<p> &#8211;guestmodules=&lt;path&gt;</p>
<dl>
<dt>
<dd> Guest os /proc/modules file copy. <i>perf</i> kvm&#8217; reads it to get guest kernel module information. Users copy it out from guest os.</dl>
<p> &#8211;guestvmlinux=&lt;path&gt;</p>
<dl>
<dt>
<dd> Guest os kernel vmlinux.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose (show counter open errors, etc).</dl>
<h2>STAT REPORT OPTIONS</h2>
<p> &#8211;vcpu=&lt;value&gt;</p>
<dl>
<dt>
<dd> analyze events which occur on this vcpu. (default: all vcpus)</dl>
<p> &#8211;event=&lt;value&gt;</p>
<dl>
<dt>
<dd> event to be analyzed. Possible values: vmexit, mmio (x86 only), ioport (x86 only). (default: vmexit)</dl>
<p> -k, &#8211;key=&lt;value&gt;</p>
<dl>
<dt>
<dd> Sorting key. Possible values: sample (default, sort by samples number), time (sort by average time).</dl>
<p> -p, &#8211;pid=</p>
<dl>
<dt>
<dd> Analyze events only for given process ID(s) (comma separated list).</dl>
<h2>STAT LIVE OPTIONS</h2>
<p> -d, &#8211;display</p>
<dl>
<dt>
<dd> Time in seconds between display updates</dl>
<p> -m, &#8211;mmap-pages=</p>
<dl>
<dt>
<dd> Number of mmap data pages (must be a power of two) or size specification with appended unit character &#8211; B/K/M/G. The size is rounded up to have nearest pages power of two value.</dl>
<p> -a, &#8211;all-cpus</p>
<dl>
<dt>
<dd> System-wide collection from all CPUs.</dl>
<p> -p, &#8211;pid=</p>
<dl>
<dt>
<dd> Analyze events only for given process ID(s) (comma separated list).</dl>
<p> &#8211;vcpu=&lt;value&gt;</p>
<dl>
<dt>
<dd> analyze events which occur on this vcpu. (default: all vcpus)</dl>
<p> &#8211;event=&lt;value&gt;</p>
<dl>
<dt>
<dd> event to be analyzed. Possible values: vmexit, mmio (x86 only), ioport (x86 only). (default: vmexit)</dl>
<p> -k, &#8211;key=&lt;value&gt;</p>
<dl>
<dt>
<dd> Sorting key. Possible values: sample (default, sort by samples number), time (sort by average time).</dl>
<p> &#8211;duration=&lt;value&gt;</p>
<dl>
<dt>
<dd> Show events other than HLT (x86 only) or Wait state (s390 only) that take longer than duration usecs.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-top/">perf-top</a></code>(1), <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1), <code><a href="/docs/linux/man/1-perf-diff/">perf-diff</a></code>(1), <code><a href="/docs/linux/man/1-perf-buildid-list/">perf-buildid-list</a></code>(1), <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1) </p>
<h2>Index</h2>
