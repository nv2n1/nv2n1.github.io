---
title: "nasl(1)"
name: "nasl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nasl/"
description: "nasl – Nessus Attack Scripting Language"
---

<h2>NAME</h2>
<p> nasl &#8211; Nessus Attack Scripting Language</p>
<h2>SYNOPSIS</h2>
<p> <code>nasl</code> <i>&lt;[-vh] [-T tracefile] [-s] [-t target] [-sX] &gt; files&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>nasl</code> executes a set of NASL scripts against a given target host. It can also be used to determine if a NASL script has any syntax errors by running it in parse (<code>-p</code>) or lint (<code>-L</code>) mode. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-T tracefile</code></p>
<dd> Makes nasl write verbosely what the script does in the file <i>tracefile</i> , ala &#8216;set -x&#8217; under sh </p>
<dt><code>-t target</code></p>
<dd> Apply the NASL script to <i>target</i> which may be a single host (127.0.0.1), a whole subnet (192.168.1.0/24) or several subnets (192.168.1.0/24, 192.168.243.0/24) </p>
<dt><code>-s</code></p>
<dd> Sets the return value of safe_checks() to 1. (See the nessusd manual to know what the safe checks are) </p>
<dt><code>-D</code></p>
<dd> Only run the description part of the script.<br />
&nbsp;<wbr></p>
<dt><code>-L</code></p>
<dd> <code>Lint</code> the script (run extended checks). </p>
<dt><code>-X</code></p>
<dd> Run the script in <code>authenticated</code> mode. For more information see the nasl reference manual </p>
<dt><code>-h</code></p>
<dd> Show help</p>
<dt><code>-v</code></p>
<dd> Show the version of NASL.</dl>
<h2>SEE ALSO</h2>
<p> <code>The NASL2 reference manual,</code> <code><a rel="nofollow" href="http://www.nessus.org/nasl2ref.pdf,">http://www.nessus.org/nasl2ref.pdf,</a></code> <code><a href="/docs/linux/man/1-nessus/">nessus</a></code>(1), <code><a href="/docs/linux/man/8-nessusd/">nessusd</a></code>(8).</p>
<h2>HISTORY</h2>
<p> NASL comes from a private project called &#8216;pkt_forge&#8217;, which was written in late 1998 by Renaud Deraison and which was an interactive shell to forge and send raw IP packets (this pre-dates Perl&#8217;s Net::RawIP by a couple of weeks). It was then extended to do a wide range of network-related operations and integrated into Nessus as &#8216;NASL&#8217;. </p>
<p> The parser was completely hand-written and a pain to work with. In Mid-2002, Michel Arboi wrote a bison parser for NASL, and he and Renaud Deraison re-wrote NASL from scratch. Although the &quot;new&quot; NASL was nearly working as early as August 2002, Michel&#8217;s lazyness made us wait for early 2003 to have it working completely. </p>
<h2>AUTHOR</h2>
<p> Most of the engine is (C) 2003 Michel Arboi, most of the built-in functions are (C) 2003 Renaud Deraison </p>
<h2>Index</h2>
