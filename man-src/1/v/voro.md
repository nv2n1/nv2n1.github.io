---
title: "voro(1)"
name: "voro"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voro/"
description: "voro++ – a 3D Voronoi cell library"
---

<p>voro++ &#8211; a 3D Voronoi cell library </p>
<h2>Synopsis</h2>
<p><code>voro++</code> [options] &lt;x_min&gt; &lt;x_max&gt; &lt;y_min&gt; &lt;y_max&gt; &lt;z_min&gt; &lt;z_max&gt; &lt;filename&gt; </p>
<h2>Description</h2>
<p>Voro++ is a software library for carrying out three-dimensional computations of the Voronoi tessellation. A distinguishing feature of the Voro++ library is that it carries out cell-based calculations, computing the Voronoi cell for each particle individually, rather than computing the Voronoi tessellation as a global network of vertices and edges. It is particularly well-suited for applications that rely on cell-based statistics, where features of Voronoi cells ( <i>eg.</i> volume, centroid, number of faces) can be used to analyze a system of particles. </p>
<p> Voro++ is written in C++ and can be built as a static library that can be linked to. This man page describes a command-line utility that is provided with the library, which can be used to access most of the library&#8217;s functionality. The utility imports text files of particle positions, computes the Voronoi cells for them, and then saves text files containing various types of information about the Voronoi cells. </p>
<h2>File Input And Output</h2>
<p>The input file should have entries on separate lines with the following format: </p>
<dl COMPACT>
<dd>&lt;Numerical ID label&gt; &lt;x coordinate&gt; &lt;y coordinate&gt; &lt;z coordinate&gt;</dl>
<p> When the command imports the particles, any that lie outside the container geometry are ignored. The program then computes Voronoi cells for all the particles, and generates an output file using the same filename but with a &quot;.vol&quot; suffix, that has the following entries: </p>
<dl COMPACT>
<dd>&lt;Numerical ID label&gt; &lt;x coordinate&gt; &lt;y coordinate&gt; &lt;z coordinate&gt; &lt;Voronoi cell volume&gt;</dl>
<p> To compute different statistics about the Voronoi cells, the -c option can be used to specify a custom output string. By default, the command assumes non-periodic boundary conditions, although this can be modified with the -p option described below. If periodicity is enabled, then particles will be re-mapped into the primary domain when the file is imported. </p>
<p> Under normal operation, the output file should have exactly the same number of lines in as the input file. However, if particles lie outside the container geometry, they will be omitted by the program, and will not appear in the output file. In certain cases, a Voronoi cell for a valid particle may be completely deleted ( <i>eg.</i> by a wall cut) and it will also not appear in the output file. By default, the particles in the output file may be ordered differently to those in the input file, although the original ordering can be preserved with the -o option described below. </p>
<h2>Internal Computational Grid</h2>
<p>To carry out the computation, the code divides the computational box into a grid of equally-sized rectangular blocks. Particles are internally sorted into this grid for computational efficiency, with maximum performance usually being achieved when there is an average of 3 to 8 particles per block. Performance is also improved if the blocks are close to cubes, with similar side lengths in three directions. In general the code is not very sensitive to the block size, and reasonable performance is achieved over a large range of values. </p>
<p> By default, the code estimates the grid size to use by counting the number of particles in the input file and choosing the number of blocks to aim for a 3 to 8 particles per block. However, is also possible to manually configure the grid size using the -l and -n options. </p>
<h2>Options</h2>
<p>The utility accepts the following basic options: </p>
<p> <code></p>
<dl COMPACT>
<dt>-c &lt;string&gt;</p>
<dd></code> This option allows the format of the output file to be customized to hold a variety of statistics about the computed Voronoi cells. The specified string can contain regular characters, plus control sequences beginning with percentage signs that are expanded to contain different Voronoi cell statistics. See below for a full custom output reference. <code></p>
<dt>-g</p>
<dd></code> If this option is specified, then an additional output file is generated with the &quot;.gnu&quot; extension, which contains a description of all the cells in a format that can be viewed using gnuplot using the <i>splot</i> command. Caution: For large input files, the gnuplot output file will be extremely large, so this option is best used on smaller systems. <code></p>
<dt>-h or &#8211;help</p>
<dd></code> This option prints out a summary of the command syntax and the available options. <code></p>
<dt>-hc</p>
<dd></code> This option prints out all the available control sequences for the customized output. <code></p>
<dt>-l &lt;len&gt;</p>
<dd></code> Manually specify a typical length scale between particles, with which to configure the internal grid size. For example, if the particles represent densely-packed hard spheres of diameter d, then d would be an appropriate value to use. The length scale can be used to estimate the optimal grid size. Using this option will result in a small performance boost, since the internal grid can be set up immediately, and it is not necessary to temporarily store the input file contents while estimating the grid size. <code></p>
<dt>-m &lt;mem&gt;</p>
<dd></code> Manually specify the initial number of particles that can be stored in each block. By default a value of 8 is used. For any block where this limit is reached, the code will dynamically allocate more memory as neccessary, so usually it is not necessary to alter this. <code></p>
<dt>-n &lt;nx&gt; &lt;ny&gt; &lt;nz&gt;</p>
<dd></code> Manually specify the internal computational grid to have nx, ny, and nz blocks in the x, y, and z directions respectively, giving nx*ny*nz blocks in total. Manually specifying the size will result in a small performance boost, since the internal grid can be set up immediately, and it is not necessary to temporarily store the input file contents while estimating the size. <code></p>
<dt>-o</p>
<dd></code> Ensure that particles in the output file are in the same order as those in the input file. This may result in a very small increase in memory usage and execution time, and is turned off by default. <code></p>
<dt>-p</p>
<dd></code> Make the container periodic in all three coordinate directions. <code></p>
<dt>-px</p>
<dd></code> Make container periodic in the x direction. <code></p>
<dt>-py</p>
<dd></code> Make container periodic in the y direction. <code></p>
<dt>-pz</p>
<dd></code> Make container periodic in the z direction. <code></p>
<dt>-r</p>
<dd></code> Carry out a Voronoi tessellation for a polydisperse particle arrangement using the radical Voronoi tessellation. For this case, an extra column is required in the input file, that contains the particle radii. The radii are also included in the output file. <code></p>
<dt>-v</p>
<dd></code> Verbose output. After the computation is completed, some statistics are printed about the container geometry, the internal computational grid, the number of particles imported, the number Voronoi cells computed, and the volume of the computed Voronoi cells. <code></p>
<dt>&#8211;version</p>
<dd></code> Print version information. <code></p>
<dt>-y</p>
<dd></code> Save the particles in POV-Ray format to &quot;filename_p.pov&quot; and the Voronoi cells in POV-Ray format to &quot;filename_v.pov&quot;. Caution: For large input files, the POV-Ray Voronoi cell file will be extremely large, so this option is best used on smaller systems. <code></p>
<dt>-yp</p>
<dd></code> Save the particles in POV-Ray format to &quot;filename_p.pov&quot;. <code></p>
<dt>-yv</p>
<dd></code> Save the Voronoi cells in POV-Ray format to &quot;filename_v.pov&quot;. </p>
</dl>
<h2>Options For Walls</h2>
<p>In addition, a number of options can be used to specify wall objects. Walls are implemented by applying extra plane cuts during the cell construction process. At present, four wall types are supported: </p>
<p> <code></p>
<dl COMPACT>
<dt>-wb &lt;x1&gt; &lt;x2&gt; &lt;x3&gt; &lt;x4&gt; &lt;x5&gt; &lt;x6&gt;</p>
<dd></code> Add six plane wall objects to make a box containing the space x1&lt;x&lt;x2, x3&lt;y&lt;x4, and x5&lt;z&lt;z6. This can be useful for embedding a smaller box within a larger container, in cases when the influence of particles outside the smaller box still need to be considered. This option is shorthand to avoid using the -wp option six times. <code></p>
<dt>-wc &lt;x1&gt; &lt;x2&gt; &lt;x3&gt; &lt;x4&gt; &lt;x5&gt; &lt;x6&gt; &lt;x7&gt;</p>
<dd></code> Add a cylindrical wall object, where (x1,x2,x3) is a point on the cylinder axis, (x4,x5,x6) is a vector along the cylinder axis, and x7 is the cylinder radius. <code></p>
<dt>-wo &lt;x1&gt; &lt;x2&gt; &lt;x3&gt; &lt;x4&gt; &lt;x5&gt; &lt;x6&gt; &lt;x7&gt;</p>
<dd></code> Add a conical wall object, with apex at (x1,x2,x3), axis along (x4,x5,x6), and half angle x7 (specified in radians). <code></p>
<dt>-ws &lt;x1&gt; &lt;x2&gt; &lt;x3&gt; &lt;x4&gt;</p>
<dd></code> Add a spherical wall object, centered on (x1,x2,x3), with radius x4. <code></p>
<dt>-wp &lt;x1&gt; &lt;x2&gt; &lt;x3&gt; &lt;x4&gt;</p>
<dd></code> Add a plane wall object, with normal (x1,x2,x3), and displacement x4. </p>
<p> Each wall is accounted for using a single approximating plane; several of the examples on the library website discuss this in more detail. If neighbor information is requested via the custom output string, then the walls are numbered sequentially, starting at -7 and decreasing. </p>
</dl>
<h2>Custom Output Commands</h2>
<p>The output files created by Voro++ can be fully customized to contain a variety of different statistics about the computed Voronoi cells. This is done by specifying a format string that contains text plus additional control sequences that begin with percentage signs. The output file contains a line for each particle, where the control sequences are expanded to different statistics. Several examples on the library website describe the customized output in more detail. </p>
<p> Particle-related entries: </p>
<p> <code></p>
<dl COMPACT>
<dt>%i</p>
<dd></code> The particle ID number.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 <code></p>
<dt>%x</p>
<dd></code> The x coordinate of the particle. <code></p>
<dt>%y</p>
<dd></code> The y coordinate of the particle. <code></p>
<dt>%z</p>
<dd></code> The z coordinate of the particle. <code></p>
<dt>%q</p>
<dd></code> The position vector of the particle, short for &quot;%x %y %z&quot;. <code></p>
<dt>%r</p>
<dd></code> The radius of the particle (only printed if the polydisperse information is available). </p>
</dl>
<p> Vertex-related entries: </p>
<p> <code></p>
<dl COMPACT>
<dt>%w</p>
<dd></code> The number of vertices in the Voronoi cell. <code></p>
<dt>%p</p>
<dd></code> A list of the vertices of the Voronoi cell in the format (x,y,z), relative to the particle center. <code></p>
<dt>%P</p>
<dd></code> A list of the vertices of the Voronoi cell in the format (x,y,z), relative to the global coordinate system. <code></p>
<dt>%o</p>
<dd></code> A list of the orders of each vertex. <code></p>
<dt>%m</p>
<dd></code> The maximum radius squared of a vertex position, relative to the particle center. </p>
</dl>
<p> Edge-related entries: </p>
<p> <code></p>
<dl COMPACT>
<dt>%g</p>
<dd></code> The number of edges of the Voronoi cell. <code></p>
<dt>%E</p>
<dd></code> The total edge distance. <code></p>
<dt>%e</p>
<dd></code> A list of perimeters of each face. </p>
</dl>
<p> Face-related entries: </p>
<p> <code></p>
<dl COMPACT>
<dt>%s</p>
<dd></code> The number of faces of the Voronoi cell. <code></p>
<dt>%F</p>
<dd></code> The total surface area of the Voronoi cell. <code></p>
<dt>%A</p>
<dd></code> A frequency table of the orders of the faces. <code></p>
<dt>%a</p>
<dd></code> A list of the orders of the faces, showing how many edges make up each face. <code></p>
<dt>%f</p>
<dd></code> A list of areas of each face. <code></p>
<dt>%t</p>
<dd></code> A list of bracketed sequences of vertices that make up each face. <code></p>
<dt>%l</p>
<dd></code> A list of normal vectors for each face. <code></p>
<dt>%n</p>
<dd></code> A list of the neighboring particle or wall IDs corresponding to each face. The list can contain negative numbers. For the non-periodic case these correspond to when the particles have faces created by the edges of the computational region. The numbers -1 to -6 correspond to the minimum x, maximum x, minimum y, maximum y, minimum z, and maximum z walls respectively. For periodic boundary conditions, negative numbers correspond to the cases when a face of the Voronoi cell is created by the periodic image of the current particle. </p>
<p> In general, the neighbor information will be symmetric, so that if particle A reports particle B as a neighbor, then particle B will report particle A as a neighbor. However, due to the fact that Voro++ computes each Voronoi cell individually, it does not provide an explicit guarantee that the neighbor information will always be symmetric. Suppose there is a very small Voronoi face connecting A to B &#8211; it may be the case that due to roundoff error, the Voronoi cell computed for particle A has a face connecting it to B, but the cell computed for particle B does not have a face connecting it to A. If the user requires perfectly symmetric neighbor information, this can be achieved by scanning the output for any one-sided connections, and either deleting them or adding in the reverse connections. The face areas output from &quot;%f&quot; can also be used to remove connections between particles that only have a very small face between them. </p>
</dl>
<p> Volume-related entries: <code></p>
<dl COMPACT>
<dt>%v</p>
<dd></code> The volume of the Voronoi cell. <code></p>
<dt>%c</p>
<dd></code> The centroid of the Voronoi cell, relative to the particle center. <code></p>
<dt>%C</p>
<dd></code> The centroid of the Voronoi cell, in the global coordinate system. </p>
</dl>
<h2>Author</h2>
<p>Voro++ is written and maintained by Chris H. Rycroft, a visiting assistant professor in the Department of Mathematics, University of California, Berkeley and Department of Mathematics, Lawrence Berkeley National Laboratory. Feedback about the code is welcome; please email chr [at] alum.mit.edu.</p>
<h2>Bugs</h2>
<p>Contact Chris H. Rycroft (chr [at] alum.mit.edu) to report problems with the code.</p>
<h2>See Also</h2>
<p>See the library website <a rel="nofollow" href="http://math.lbl.gov/voro++/">http://math.lbl.gov/voro++/</a> for complete documentation and examples.</p>
