---
title: "papi_cost(1)"
name: "papi_cost"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_cost/"
---

<h2 class="name">NAME</h2>
 

 papi_cost - papi_cost utility. 

 file cost.c 

<h2 class="name">NAME</h2>
 

 

 papi_cost - computes execution time costs for basic PAPI operations. 

<h2>Synopsis</h2>

 

 papi_cost [-dhs] [-b bins] [-t threshold]

<h2>Description</h2>

 

 papi_cost is a PAPI utility program that computes the min / max / mean / std. deviation of execution times for PAPI start/stop pairs and for PAPI reads. This information provides the basic operating cost to a user's program for collecting hardware counter data. Command line options control display capabilities.

<h2>Options</h2>

 

<dl>
<dt>&bull;
<dd> -b &lt; bins &gt; Define the number of bins into which the results are partitioned for display. The default is 100.
<dt>&bull;
<dd> -d Display a graphical distribution of costs in a vertical histogram.
<dt>&bull;
<dd> -h Display help information about this utility.
<dt>&bull;
<dd> -s Show the number of iterations in each of the first 10 standard deviations above the mean.
<dt>&bull;
<dd> -t &lt; threshold &gt; Set the threshold for the number of iterations to measure costs. The default is 100,000.</dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org. 

<h2>Index</h2>


