---
title: "papi_multiplex_cost(1)"
name: "papi_multiplex_cost"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_multiplex_cost/"
---

<h2 class="name">NAME</h2>
 

 papi_multiplex_cost - papi_multiplex_cost utility. 

 file multiplex.c 

<h2 class="name">NAME</h2>
 

 

 papi_multiplex_cost - computes execution time costs for basic PAPI operations on multiplexed EventSets. 

<h2>Synopsis</h2>

 

 papi_cost [-m, --min &lt; min &gt;] [-x, --max &lt; max &gt;] [-k,-s]

<h2>Description</h2>

 

 papi_multiplex_cost is a PAPI utility program that computes the min / max / mean / std. deviation of execution times for PAPI start/stop pairs and for PAPI reads on multiplexed eventsets. This information provides the basic operating cost to a user's program for collecting hardware counter data. Command line options control display capabilities.

<h2>Options</h2>

 

<dl>
<dt>&bull;
<dd> -m &lt; Min number of events to test &gt;
<dt>&bull;
<dd> -x &lt; Max number of events to test &gt;
<dt>&bull;
<dd> -k, Do not time kernel multiplexing
<dt>&bull;
<dd> -s, Do not ime software multiplexed EventSets
<dt>&bull;
<dd> -t THREASHOLD, Test with THRESHOLD iterations of counting loop.</dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org. 

<h2>Index</h2>


