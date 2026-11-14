---
title: "proofserv(1)"
name: "proofserv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-proofserv/"
description: "proofserv – PROOF (The Parallel ROOT Facility)"
---

<h2 class="name">NAME</h2>
<p> proofserv &#8211; PROOF (The Parallel ROOT Facility) </p>
<h2>DESCRIPTION</h2>
<p> Using <code>PROOF</code><i> (The P</i>arallel <i>ROO</i>T <i>F</i>acility) one can analyze trees in parallel on a cluster of computers. The <code>PROOF</code> system consists of the <i><a href="/docs/linux/man/1-proofd/">proofd</a></i>(1) from-end program which is started via <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8). </p>
<p> <i>proofd</i> takes care of user authentication and overlays itself then with the desired version of the <i><a href="/docs/linux/man/1-proofserv/">proofserv</a></i>(1) executable. </p>
<p> The <i><a href="/docs/linux/man/1-proofserv/">proofserv</a></i>(1) is a basically the same as the <code>ROOT</code> interactive module <i><a href="/docs/linux/man/1-root/">root</a></i>(1), except that it reads its commands from a socket instead of from the terminal. </p>
<p> Since it is a remote server it will not do graphics and therefore is not linked with any graphics libraries (Motif, X11, etc.). </p>
<p> <code>proofserv</code> is started by the daemon <code><a href="/docs/linux/man/1-proofd/">proofd</a></code>(1) on request by the user. It is not a command to be executed by the user directly. </p>
<p> Note, that if <code>proofserv</code> is passed any arguments, it will use the <code>libProofx interface, rather than the standard libProof</code> interface.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-proofd/">proofd</a></i>(1) , <i><a href="/docs/linux/man/1-root/">root</a></i>(1) , <i><a href="/docs/linux/man/1-rootd/">rootd</a></i>(1) </p>
<p> More information can be found at the <code>ROOT</code> website: <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
