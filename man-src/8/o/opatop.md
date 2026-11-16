---
title: "opatop(8)"
name: "opatop"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opatop/"
---

opatop 

 

 

 Starts the opatop Text User Interface (TUI) menu to display performance, congestion, and error information about a fabric. Refer to <i>Intel(R) Omni-Path Fabric Suite FastFabric User Guide</i> 

 for additional details.

<h2>Syntax</h2>

opatop [-v] [-q] [-h <i>hfi</i>] [-p <i>port</i>] [-i <i>seconds</i>]

<h2>Options</h2>

<h2>Options</h2>

<dl><dt>--help
</dt><dd>Produces full help text. 
</dd><dt>-v/--verbose level
</dt><dd>Verbose output level. Value is additive and includes:
</dd><dl><dd></dd><dl><dd>1 Screen</dd></dl></dl><dl><dd></dd><dl><dd>4 STDERR opatop</dd></dl></dl><dl><dd></dd><dl><dd>16 STDERR PaClient</dd></dl></dl><dt>-q/--quiet
</dt><dd>Disables progress reports.
</dd><dt>-h/--hfi <i>hfi</i>
</dt><dd>HFI, numbered 1..n. Using 0 specifies that the -p <i>port</i> is a system-wide port number. Default is 0. 

</dd><dt>-p/--port <i>port</i>
</dt><dd>List of local HFI ports used to access fabrics for counter clear. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. 

</dd><dd>Uses the format hfi:port, for example:
</dd><dl><dd></dd><dl><dd>0:0 First active port in system. 
</dd></dl></dl><dl><dd></dd><dl><dd>0:y Port <i>y</i> within system. 
</dd></dl></dl><dl><dd></dd><dl><dd>x:0 First active port on HFI <i>x</i>. 
</dd></dl></dl><dl><dd></dd><dl><dd>x:y HFI <i>x</i>, port <i>y</i>. 
</dd></dl></dl><dt>-i/--interval <i>seconds</i>
</dt><dd>Interval in <i>seconds</i> at which PA queries are performed to refresh to the latest PA image. Default = 10 seconds. 

 

</dd></dl>

<h2>-h and -p options permit a variety of selections:</h2>

<dl><dt>-h 0
</dt><dd>First active port in system (default). 
</dd><dt>-h 0 -p 0
</dt><dd>First active port in system. 
</dd><dt>-h <i>x</i>
</dt><dd>First active port on HFI <i>x</i>. 
</dd><dt>-h <i>x</i>#8217#160;-p 0
</dt><dd>First active port on HFI <i>x</i>. 
</dd><dt>-h 0 -p <i>y</i>
</dt><dd>Port <i>y#8217#160;</i> within system (no matter which ports are active). 
</dd><dt>-h <i>x</i>#8217#160;-p <i>y</i>
</dt><dd>HFI <i>x</i>, port <i>y</i>. 
</dd></dl>
