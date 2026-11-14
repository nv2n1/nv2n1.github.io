---
title: "mpif90(1)"
name: "mpif90"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpif90/"
---

<h2 class="name">NAME</h2>
 

 mpif77, mpif90 -- Deprecated Open MPI Fortran wrapper compilers 

<h2>SYNTAX</h2>

 mpif90 ...

<h2>DESCRIPTION</h2>

 

 The <i>mpif77</i> and <i>mpif90</i> wrapper compiler names are deprecated, and will disappear in a future version of Open MPI. You should use the <i>mpifort</i> wrapper compiler, instead. While they are deprecated, <i>mpif77</i> and <i>mpif90</i> accept all the same parameters as <i>mpifort</i>, and behaves the same as <i>mpifort</i>. 

 With <i>mpifort</i>, you can compile any Fortran program that uses the &quot;mpif.h&quot;, &quot;use mpi&quot;, and/or &quot;use mpi_f08&quot; MPI Fortran interfaces. 

 See <a HREF="/docs/linux/man/1-mpifort/">mpifort</a>(1) for more details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-mpifort/">mpifort</a>(1) 

<h2>Index</h2>


