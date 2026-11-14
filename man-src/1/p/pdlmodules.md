---
title: "pdlmodules(1)"
name: "pdlmodules"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlmodules/"
---

PDL::Modules - A guide to PDL's module reference. 

<h2>Description</h2>This page serves as a table of contents for <font SIZE="-1">PDL</font>'s module documentation. This page does not list every single <font SIZE="-1">PDL</font> module. It only shows the ones intended for <font SIZE="-1">PDL</font> users, while ommitting those which are deemed ``for internal use only''. If you wish to see a comprehensive list of all documentation, please see the PDL::Index page.
<h2>Looking For A Function?</h2>If you want to search for a function name, you should use the <font SIZE="-1">PDL</font> shell along with the ``help'' or ``apropos'' command (to do a fuzzy search). For example: 

 <pre> pdl&gt; apropos xval
 xlinvals X axis values between endpoints (see xvals).
 xlogvals X axis values logarithmicly spaced...
 xvals Fills a piddle with X index values...
 yvals Fills a piddle with Y index values. See the CAVEAT for xvals.
 zvals Fills a piddle with Z index values. See the CAVEAT for xvals.</pre>To learn more about the <font SIZE="-1">PDL</font> shell, see perldl or pdl2.
<h2>Foundation</h2><dl><dt>perldl or pdl2
<dd>Learn about the <font SIZE="-1">PDL</font> shell.</dl><h3>Functions</h3><dl><dt>PDL::Core
<dd>Core module (e.g. creating piddles).
<dt>PDL::Basic
<dd>Simplified interface to the more general PDL::Primitive.
<dt>PDL::Ops
<dd>Basic operators (e.g. arithmetic, comparisons, etc.).
<dt>PDL::Ufunc
<dd>Functions that accumulate along a dimension (e.g. sum, max).</dl><h3>Other Features</h3><dl><dt>PDL::AutoLoader
<dd>MATLAB-style function autoloader.
<dt>PDL::Slices
<dd>Indexing and slices. How to access a subset of a piddle.
<dt>PDL::NiceSlice
<dd>Nicer syntax for slices.</dl><h2>Miscellaneous</h2><dl><dt>PDL::Primitive
<dd>Fundamental operations on piddles.
<dt>PDL::Complex
<dd>Complex numbers.
<dt>PDL::Bad
<dd>Bad value support.
<dt>PDL::Reduce
<dd>A 'reduce' function for <font SIZE="-1">PDL.</font>
<dt>PDL::Lite
<dd>Minimum <font SIZE="-1">PDL</font> module <font SIZE="-1">OO</font> loader.
<dt>PDL::LiteF
<dd>Minimum <font SIZE="-1">PDL</font> module function loader.
<dt>PDL::Extended
<dd>Extended Mathematical Operators.
<dt>PDL::Func
<dd>Interpolation-related functions.</dl><h2>Graphics</h2><dl><dt>PDL::Graphics::PGPLOT
<dd><font SIZE="-1">PGPLOT</font> library.
<dt>PDL::Graphics::PLplot
<dd>PLplot library.</dl><h3>3D Graphics</h3><dl><dt>PDL::Graphics::TriD
<dd>3D graphics core module.
<dt>PDL::Graphics::TriD::Rout
<dd>Helper routines for 3D graphics.
<dt>PDL::Graphics::TriD::Contours
<dd>3D surface contours.</dl><h3>Helper Modules</h3><dl><dt>PDL::Graphics::LUT
<dd>Look-up tables.
<dt>PDL::Graphics::IIS
<dd>Display images on <font SIZE="-1">IIS</font> devices.
<dt>PDL::Graphics::Limits
<dd>Derive data limits for display purposes.</dl><h2>Image Processing</h2><dl><dt>PDL::Compression
<dd>Compression utilities.
<dt>PDL::Image2D
<dd>2-dimmensional image processing.
<dt>PDL::ImageND
<dd>N-dimmensional image processing.
<dt>PDL::ImageRGB
<dd><font SIZE="-1">RGB</font> image data handling.</dl><h2>Numerical Methods</h2><dl><dt><font SIZE="-1">PDL::FFT</font>
<dd>Fast Fourier Transform (native implementation).
<dt><font SIZE="-1">PDL::FFTW</font>
<dd><font SIZE="-1">PDL</font> interface to the <font SIZE="-1">FFTW</font> library.
<dt>PDL::Filter::LinPred
<dd>Linear predictive filtering.
<dt>PDL::Filter::Linear
<dd>Linear filtering.
<dt>PDL::Opt::Simplex
<dd>Simplex optimization routines.
<dt>PDL::Minuit
<dd><font SIZE="-1">PDL</font> interface to the Minuit library.
<dt>PDL::Slatec
<dd><font SIZE="-1">PDL</font> interface to the Slatec library.</dl><h2>Coordinate Transformations</h2><dl><dt>PDL::Transform
<dd>Coordinate transforms, image warping, and N-D functions.
<dt>PDL::Transform::Cartography
<dd>Cartographic projections.
<dt>PDL::Transform::Proj4
<dd><font SIZE="-1">PDL</font> interface to the Proj4 projection library.</dl><h2>Io Functions</h2><dl><dt><font SIZE="-1">PDL::IO</font>
<dd>Overview of <font SIZE="-1">IO</font> functions.
<dt>PDL::IO::Dumper
<dd>Data dumper.
<dt>PDL::IO::FastRaw
<dd>Fast storage format (outdated).
<dt>PDL::IO::FlexRaw
<dd>Flexible storage format.
<dt>PDL::IO::Rout
<dd>Misc <font SIZE="-1">IO</font> routines.
<dt>PDL::IO::Sortable
<dd>Support for Perl's 'Storable' module.</dl><h3>Image Formats</h3><dl><dt><font SIZE="-1">PDL::IO::FITS</font>
<dd><font SIZE="-1">PDL</font> support for <font SIZE="-1">FITS</font> images.
<dt><font SIZE="-1">PDL::IO::PNM</font>
<dd><font SIZE="-1">PDL</font> support for <font SIZE="-1">PNM</font> images.
<dt><font SIZE="-1">PDL::IO::GD</font>
<dd><font SIZE="-1">PDL</font> interface to the <font SIZE="-1">GD</font> image library.
<dt><font SIZE="-1">PDL::IO::HDF</font>
<dd><font SIZE="-1">PDL</font> interface to the <font SIZE="-1">HDH4</font> image library.
<dt>PDL::IO::NetPBM
<dd><font SIZE="-1">PDL</font> interface to the NetPBM image library.
<dt><font SIZE="-1">PDL::IO::NDF</font>
<dd><font SIZE="-1">PDL</font> interface to the Starlink image library. Available as a separate <font SIZE="-1">CPAN</font> download.</dl><h2>2D Matrices</h2><dl><dt>PDL::Matrix
<dd>Convenience class for 2D matrix work.
<dt>PDL::MatrixOps
<dd>Additional matrix operators.</dl><h2>Gnu Scientific Library</h2><dl><dt><font SIZE="-1">PDL::GSL::DIFF</font>
<dd>Numerical differentiation.
<dt><font SIZE="-1">PDL::GSL::INTEG</font>
<dd>Numerical integration.
<dt><font SIZE="-1">PDL::GSL::INTERP</font>
<dd>Interpolation.
<dt><font SIZE="-1">PDL::GSL::MROOT</font>
<dd>Multidimensional root-finding.
<dt><font SIZE="-1">PDL::GSL::RNG</font>
<dd><font SIZE="-1">RNG</font> and randist.</dl><h3>Special Functions</h3><dl><dt><font SIZE="-1">PDL::GSL::AIRY</font>
<dd><dt><font SIZE="-1">PDL::GSL::BESSEL</font>
<dd><dt><font SIZE="-1">PDL::GSL::CLAUSEN</font>
<dd><dt><font SIZE="-1">PDL::GSL::COULOMB</font>
<dd><dt><font SIZE="-1">PDL::GSL::COUPLING</font>
<dd><dt><font SIZE="-1">PDL::GSL::DAWSON</font>
<dd><dt><font SIZE="-1">PDL::GSL::DEBYE</font>
<dd><dt><font SIZE="-1">PDL::GSL::DILOG</font>
<dd><dt><font SIZE="-1">PDL::GSL::ELEMENTARY</font>
<dd><dt><font SIZE="-1">PDL::GSL::ELLINT</font>
<dd><dt><font SIZE="-1">PDL::GSL::ELLJAC</font>
<dd><dt><font SIZE="-1">PDL::GSL::ERF</font>
<dd><dt><font SIZE="-1">PDL::GSL::EXP</font>
<dd><dt><font SIZE="-1">PDL::GSL::EXPINT</font>
<dd><dt><font SIZE="-1">PDL::GSL::FERMI_DIRAC</font>
<dd><dt><font SIZE="-1">PDL::GSL::GAMMA</font>
<dd><dt><font SIZE="-1">PDL::GSL::GEGENBAUER</font>
<dd><dt><font SIZE="-1">PDL::GSL::HYPERG</font>
<dd><dt><font SIZE="-1">PDL::GSL::LAGUERRE</font>
<dd><dt><font SIZE="-1">PDL::GSL::LEGENDRE</font>
<dd><dt><font SIZE="-1">PDL::GSL::LOG</font>
<dd><dt><font SIZE="-1">PDL::GSL::POLY</font>
<dd><dt><font SIZE="-1">PDL::GSL::POW_INT</font>
<dd><dt><font SIZE="-1">PDL::GSL::PSI</font>
<dd><dt><font SIZE="-1">PDL::GSL::SYNCHROTRON</font>
<dd><dt><font SIZE="-1">PDL::GSL::TRANSPORT</font>
<dd><dt><font SIZE="-1">PDL::GSL::TRIG</font>
<dd><dt><font SIZE="-1">PDL::GSL::ZETA</font>
<dd></dl><h2>Fitting Functions</h2><dl><dt>PDL::Fit::Gaussian
<dd>Fit gaussian curves.
<dt>PDL::Fit::Polynomial
<dd>Fit polynomials.
<dt>PDL::Fit::Linfit
<dd>Fit linear combinations of functions.
<dt>PDL::Fit::LM
<dd>Fit functions using the Levenberg-Marquardt algorithm.</dl><h2>Advanced</h2><dl><dt>PDL::Dbg
<dd><font SIZE="-1">PDL</font> debugger.
<dt>PDL::DiskCache
<dd>Manage many piddles through a disk cache.
<dt>PDL::CallExt
<dd>Call external functions.
<dt>PDL::Objects
<dd>If you want to sub-class from <font SIZE="-1">PDL </font>(note: incomplete).</dl><h2>Copyright</h2>Copyright 2010 Daniel Carrera (dcarrera [at] gmail.com). You can distribute and/or modify this document under the same terms as the current Perl license. 

 See: <a rel="nofollow" HREF="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a>
