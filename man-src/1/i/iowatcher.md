---
title: "iowatcher(1)"
name: "iowatcher"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iowatcher/"
description: "iowatcher – Create visualizations from blktrace results"
---

<h2 class="name">NAME</h2>
<p> iowatcher &#8211; Create visualizations from blktrace results</p>
<h2>SYNOPSIS</h2>
<p> <code>iowatcher</code> <i>OPTIONS&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> iowatcher graphs the results of a blktrace run. It can graph the result of an existing blktrace, start a new blktrace, or start a new blktrace and a benchmark run. It can then create an image or movie of the IO from a given trace. iowatcher can produce either SVG files or movies in mp4 format (with ffmpeg) or ogg format (with png2theora). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Print a brief usage summary.</dd>
<dt><code>-d, &#8211;device</code> &lt;device&gt;</dt>
<dd> Controls which device you are tracing. You can only trace one device at a time for now. It is sent directly to blktrace, and only needed when you are making a new trace.</dd>
<dt><code>-D, &#8211;blktrace-destination</code> &lt;destination&gt;</dt>
<dd> Destination for blktrace.</dd>
<dt><code>-p, &#8211;prog</code> &lt;program&gt;</dt>
<dd> Program to run while blktrace is run.</dd>
<dt><code>-K, &#8211;keep-movie-svgs</code></dt>
<dd> Keep the SVG files generated for movie mode.</dd>
<dt><code>-t, &#8211;trace</code> &lt;file|directory&gt;</dt>
<dd> Controls the name of the blktrace file. iowatcher uses a dump from blkparse, so -t tries to guess the name of the corresponding per CPU blktrace data files if the dump file doesn&#8217;t already exist. If you want more than one trace in a given graph, you can specify -t more than once. If a directory is specified, iowatcher will use the name of the directory as the base name of the dump file and all trace files found inside the directory will be processed.</dd>
<dt><code>-l, &#8211;label</code> &lt;label&gt;</dt>
<dd> Sets a label in the graph for a trace file. The labels are added in the same order the trace files are added.</dd>
<dt><code>-m, &#8211;movie</code> [spindle|rect]</dt>
<dd> Create a movie. The file format depends on the extension used in the -o filename.* option. If you specify an .ogv or .ogg extension, the result will be Ogg Theora video, if png2theora is available. If you use an .mp4 extension, the result will be an mp4 video if ffmpeg is available. You can use any other extension, but the end result will be an mp4. You can use &#8211;movie=spindle or &#8211;movie=rect, which changes the style of the IO mapping.</dd>
<dt><code>-T, &#8211;title</code> &lt;title&gt;</dt>
<dd> Set a title to be placed at the top of the graph.</dd>
<dt><code>-o, &#8211;output</code> &lt;file&gt;</dt>
<dd> Output filename (default: trace.svg).</dd>
<dt><code>-r, &#8211;rolling</code> &lt;seconds&gt;</dt>
<dd> Control the duration for the rolling average. iowatcher tries to smooth out bumpy graphs by averaging the current second with seconds from the past. Larger numbers here give you flatter graphs.</dd>
<dt><code>-h, &#8211;height</code> &lt;height&gt;</dt>
<dd> Set the height of each graph</dd>
<dt><code>-w, &#8211;width</code> &lt;width&gt;</dt>
<dd> Set the width of each graph</dd>
<dt><code>-c, &#8211;columns</code> &lt;columns&gt;</dt>
<dd> Numbers of columns in graph output</dd>
<dt><code>-x, &#8211;xzoom</code> &lt;min:max&gt;</dt>
<dd> Limit processed time range to min:max</dd>
<dt><code>-y, &#8211;yzoom</code> &lt;min:max&gt;</dt>
<dd> Limit processed sectors to min:max</dd>
<dt><code>-a, &#8211;io-plot-action</code> &lt;action&gt;</dt>
<dd> Plot given action (one of Q,D,C) in IO graph</dd>
<dt><code>-P, &#8211;per-process-io</code></dt>
<dd> Distinguish between processes in IO graph</dd>
<dt><code>-O, &#8211;only-graph</code> &lt;graph&gt;</dt>
<dd> Add a single graph to the output (see GRAPHS). By default all the graphs are included, but with -O you get only the graphs you ask for. -O may be used more than once.</dd>
<dt><code>-N, &#8211;no-graph</code> &lt;type&gt;</dt>
<dd> Remove a single graph from the output (see GRAPHS). This may also be used more than once.</dd></dl>
<h2>GRAPHS</h2>
<p> Choices for -O and -N are:<br />
io, tput, latency, queue_depth, iops, cpu-sys, cpu-io, cpu-irq, cpu-user, cpu-soft </p>
<h2>EXAMPLES</h2>
<p> Generate graph from the existing trace.dump: </p>
<dl>
<dt>
</dt><dd> iowatcher -t trace.dump -o trace.svg</dd></dl>
<p> Skip the IO graph: </p>
<dl>
<dt>
</dt><dd> iowatcher -t trace.dump -o trace.svg -N io</dd></dl>
<p> Only graph tput and latency: </p>
<dl>
<dt>
</dt><dd> iowatcher -t trace.dump -o trace.svg -O tput -O latency</dd></dl>
<p> Generate a graph from two runs, and label them: </p>
<dl>
<dt>
</dt><dd> iowatcher -t ext4.dump -t xfs.dump -l Ext4 -l XFS -o trace.svg</dd></dl>
<p> Run a fio benchmark and store the trace in trace.dump, add a title to the top, use /dev/sda for blktrace: </p>
<dl>
<dt>
</dt><dd> iowatcher -d /dev/sda -t trace.dump -T &#8216;Fio Benchmark&#8217; -p &#8216;fio some_job_file&#8217;</dd></dl>
<p> Make a movie from an existing trace: </p>
<dl>
<dt>
</dt><dd> iowatcher -t trace &#8211;movie -o trace.mp4</dd></dl>
