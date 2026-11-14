---
title: "beakerlib-performance(1)"
name: "beakerlib-performance"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-performance/"
---

<h2 class="name">NAME</h2>
 

 BeakerLib - performance - Performance measuring routines 

<h2>DESCRIPTION</h2>

 This is a library of helpers and shortcut for performance monitoring of applications. It provides various means of measuring time and memory performance of programs.

<h2>FUNCTIONS</h2>

<h3>Time Performance</h3>

 <i>rlPerfTime_RunsInTime</i> 

 Measures, how many runs of some commands can be done in specified time. This approach is suitable for short-time running tasks (up to few seconds), where averaging few runs is not precise. This is done several times, and the final result is the average of all runs. It prints the number on stdout, so it has to be captured. 

 <pre><code>
rlPerfTime_RunsInTime command[time][runs]
</code></pre>
<dl>
<dt>command
<dd> Command to run.
<dt>time
<dd> Time in seconds (optional, default=30).
<dt>runs
<dd> Number of averaged runs (optional, default=3).</dl>
 

 <i>rlPerfTime_AvgFromRuns</i> 

 Measures the average time of running some task. This approach is suitable for long-time running tasks (tens of seconds and more), where it is precise enough. Measured runs can be preceded by dry run, which is not measured and it's purpose is to warm up various caches. It prints the number on stdout, so it has to be captured. Or, result is then stored in special rl_retval variable. 

 <pre><code>
rlPerfTime_AvgFromRuns command[count][warmup]
</code></pre>
<dl>
<dt>command
<dd> Command to run.
<dt>count
<dd> Times to run (optional, default=3).
<dt>warmup
<dd> Warm-up run, run if this option is not ``warmup'' (optional, default=``warmup'')</dl>

<h2>AUTHORS</h2>

<dl>
<dt>&bull;
<dd> Petr Muller &lt;pmuller [at] redhat.com&gt; 

</dl>

<h2>Index</h2>


