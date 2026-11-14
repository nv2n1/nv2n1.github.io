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
<dt><code>&#8211;help</code></p>
<dd> Print a brief usage summary.</p>
<dt><code>-d, &#8211;device</code> &lt;device&gt;</p>
<dd> Controls which device you are tracing. You can only trace one device at a time for now. It is sent directly to blktrace, and only needed when you are making a new trace.</p>
<dt><code>-D, &#8211;blktrace-destination</code> &lt;destination&gt;</p>
<dd> Destination for blktrace.</p>
<dt><code>-p, &#8211;prog</code> &lt;program&gt;</p>
<dd> Program to run while blktrace is run.</p>
<dt><code>-K, &#8211;keep-movie-svgs</code></p>
<dd> Keep the SVG files generated for movie mode.</p>
<dt><code>-t, &#8211;trace</code> &lt;file|directory&gt;</p>
<dd> Controls the name of the blktrace file. iowatcher uses a dump from blkparse, so -t tries to guess the name of the corresponding per CPU blktrace data files if the dump file doesn&#8217;t already exist. If you want more than one trace in a given graph, you can specify -t more than once. If a directory is specified, iowatcher will use the name of the directory as the base name of the dump file and all trace files found inside the directory will be processed.</p>
<dt><code>-l, &#8211;label</code> &lt;label&gt;</p>
<dd> Sets a label in the graph for a trace file. The labels are added in the same order the trace files are added.</p>
<dt><code>-m, &#8211;movie</code> [spindle|rect]</p>
<dd> Create a movie. The file format depends on the extension used in the -o filename.* option. If you specify an .ogv or .ogg extension, the result will be Ogg Theora video, if png2theora is available. If you use an .mp4 extension, the result will be an mp4 video if ffmpeg is available. You can use any other extension, but the end result will be an mp4. You can use &#8211;movie=spindle or &#8211;movie=rect, which changes the style of the IO mapping.</p>
<dt><code>-T, &#8211;title</code> &lt;title&gt;</p>
<dd> Set a title to be placed at the top of the graph.</p>
<dt><code>-o, &#8211;output</code> &lt;file&gt;</p>
<dd> Output filename (default: trace.svg).</p>
<dt><code>-r, &#8211;rolling</code> &lt;seconds&gt;</p>
<dd> Control the duration for the rolling average. iowatcher tries to smooth out bumpy graphs by averaging the current second with seconds from the past. Larger numbers here give you flatter graphs.</p>
<dt><code>-h, &#8211;height</code> &lt;height&gt;</p>
<dd> Set the height of each graph</p>
<dt><code>-w, &#8211;width</code> &lt;width&gt;</p>
<dd> Set the width of each graph</p>
<dt><code>-c, &#8211;columns</code> &lt;columns&gt;</p>
<dd> Numbers of columns in graph output</p>
<dt><code>-x, &#8211;xzoom</code> &lt;min:max&gt;</p>
<dd> Limit processed time range to min:max</p>
<dt><code>-y, &#8211;yzoom</code> &lt;min:max&gt;</p>
<dd> Limit processed sectors to min:max</p>
<dt><code>-a, &#8211;io-plot-action</code> &lt;action&gt;</p>
<dd> Plot given action (one of Q,D,C) in IO graph</p>
<dt><code>-P, &#8211;per-process-io</code></p>
<dd> Distinguish between processes in IO graph</p>
<dt><code>-O, &#8211;only-graph</code> &lt;graph&gt;</p>
<dd> Add a single graph to the output (see GRAPHS). By default all the graphs are included, but with -O you get only the graphs you ask for. -O may be used more than once.</p>
<dt><code>-N, &#8211;no-graph</code> &lt;type&gt;</p>
<dd> Remove a single graph from the output (see GRAPHS). This may also be used more than once.</dl>
<h2>GRAPHS</h2>
<p> Choices for -O and -N are:<br />
io, tput, latency, queue_depth, iops, cpu-sys, cpu-io, cpu-irq, cpu-user, cpu-soft </p>
<h2>EXAMPLES</h2>
<p> Generate graph from the existing trace.dump: </p>
<dl>
<dt>
<dd> iowatcher -t trace.dump -o trace.svg</dl>
<p> Skip the IO graph: </p>
<dl>
<dt>
<dd> iowatcher -t trace.dump -o trace.svg -N io</dl>
<p> Only graph tput and latency: </p>
<dl>
<dt>
<dd> iowatcher -t trace.dump -o trace.svg -O tput -O latency</dl>
<p> Generate a graph from two runs, and label them: </p>
<dl>
<dt>
<dd> iowatcher -t ext4.dump -t xfs.dump -l Ext4 -l XFS -o trace.svg</dl>
<p> Run a fio benchmark and store the trace in trace.dump, add a title to the top, use /dev/sda for blktrace: </p>
<dl>
<dt>
<dd> iowatcher -d /dev/sda -t trace.dump -T &#8216;Fio Benchmark&#8217; -p &#8216;fio some_job_file&#8217;</dl>
<p> Make a movie from an existing trace: </p>
<dl>
<dt>
<dd> iowatcher -t trace &#8211;movie -o trace.mp4</dl>
<h2>Index</h2>
