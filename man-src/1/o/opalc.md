---
title: "opalc(1)"
name: "opalc"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opalc/"
description: "opal_wrapper – Back-end Open MPI wrapper command"
---

<p>opal_wrapper &#8211; Back-end Open MPI wrapper command </p>
<h2>Synopsis</h2>
<p><code>opal_wrapper [options]</code></p>
<h2>Description</h2>
<p><code>opal_wrapper</code> is not meant to be called directly by end users. It is automatically invoked as the back-end by the Open MPI wrapper commands such as: <code>mpicc</code>, <code>mpiCC</code>, <code>mpic++</code>, and <code>mpifort</code> (and its legacy/deprecated names <code>mpif77</code> and <code>mpif90</code>). </p>
<p> Some Open MPI installations may have additional wrapper commands, and/or have renamed the wrapper compilers listed above to avoid executable name conflicts with other MPI implementations. Hence, you may also have wrapper compilers installed including the following names: <code>mpifort.openmpi</code> (and the legacy/deprecated names <code>mpif90.openmpi</code> and <code>mpif77.openmpi</code>), <code>mpicxx.openmpi</code>, <code>mpiCC.openmpi</code>, <code>mpicc.openmpi</code>, <code>mpic++.openmpi</code>, <code>opalcc</code>, <code>opalc++</code>, <code>ortecc</code>, and <code>ortec++</code>,</p>
<h2>See Also</h2>
<p>The following may exist depending on your particular Open MPI installation: <code><a href="/docs/linux/man/1-mpicc/">mpicc</a></code>(1), <code><a href="/docs/linux/man/1-mpicc/">mpiCC</a></code>(1), <code>mpic++</code>(1), <code><a href="/docs/linux/man/1-mpifort/">mpifort</a></code>(1), <code><a href="/docs/linux/man/1-mpifort-openmpi/">mpifort.openmpi</a></code>(1), <code><a href="/docs/linux/man/1-mpicxx-openmpi/">mpicxx.openmpi</a></code>(1), <code><a href="/docs/linux/man/1-mpicc-openmpi/">mpiCC.openmpi</a></code>(1), <code><a href="/docs/linux/man/1-mpicc-openmpi/">mpicc.openmpi</a></code>(1), <code>mpic++<a href="/docs/linux/man/1--openmpi/">.openmpi</a></code>(1), <code><a href="/docs/linux/man/1-ortecc/">ortecc</a></code>(1), <code>ortec++</code>(1), <code><a href="/docs/linux/man/1-opalccc/">opalccc</a></code>(1), and the website at <i><a rel="nofollow" href="http://www.openmpi.org/">http://www.openmpi.org/</a></i>.</p>
<h2>Authors</h2>
<p>The Open MPI maintainers &#8212; see <i><a rel="nofollow" href="http://www.openmpi.org/">http://www.openmpi.org/</a></i> or the file <i>AUTHORS</i>. </p>
<p> This manual page was originally contributed by Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, one of the Debian GNU/Linux maintainers for Open MPI, and may be used by others.</p>
