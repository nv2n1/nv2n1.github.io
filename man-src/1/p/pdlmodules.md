---
title: "pdlmodules(1)"
name: "pdlmodules"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlmodules/"
---

PDL::Modules - A guide to PDL's module reference. 

<h2>Description</h2>This page serves as a table of contents for PDL's module documentation. This page does not list every single PDL module. It only shows the ones intended for PDL users, while ommitting those which are deemed ``for internal use only''. If you wish to see a comprehensive list of all documentation, please see the PDL::Index page.
<h2>Looking For A Function?</h2>If you want to search for a function name, you should use the PDL shell along with the ``help'' or ``apropos'' command (to do a fuzzy search). For example: 

 <pre> pdl&gt; apropos xval
 xlinvals X axis values between endpoints (see xvals).
 xlogvals X axis values logarithmicly spaced...
 xvals Fills a piddle with X index values...
 yvals Fills a piddle with Y index values. See the CAVEAT for xvals.
 zvals Fills a piddle with Z index values. See the CAVEAT for xvals.</pre>To learn more about the PDL shell, see perldl or pdl2.
<h2>Foundation</h2><dl><dt>perldl or pdl2
</dt><dd>Learn about the PDL shell.</dd></dl><h3>Functions</h3><dl><dt>PDL::Core
</dt><dd>Core module (e.g. creating piddles).
</dd><dt>PDL::Basic
</dt><dd>Simplified interface to the more general PDL::Primitive.
</dd><dt>PDL::Ops
</dt><dd>Basic operators (e.g. arithmetic, comparisons, etc.).
</dd><dt>PDL::Ufunc
</dt><dd>Functions that accumulate along a dimension (e.g. sum, max).</dd></dl><h3>Other Features</h3><dl><dt>PDL::AutoLoader
</dt><dd>MATLAB-style function autoloader.
</dd><dt>PDL::Slices
</dt><dd>Indexing and slices. How to access a subset of a piddle.
</dd><dt>PDL::NiceSlice
</dt><dd>Nicer syntax for slices.</dd></dl><h2>Miscellaneous</h2><dl><dt>PDL::Primitive
</dt><dd>Fundamental operations on piddles.
</dd><dt>PDL::Complex
</dt><dd>Complex numbers.
</dd><dt>PDL::Bad
</dt><dd>Bad value support.
</dd><dt>PDL::Reduce
</dt><dd>A 'reduce' function for PDL.
</dd><dt>PDL::Lite
</dt><dd>Minimum PDL module OO loader.
</dd><dt>PDL::LiteF
</dt><dd>Minimum PDL module function loader.
</dd><dt>PDL::Extended
</dt><dd>Extended Mathematical Operators.
</dd><dt>PDL::Func
</dt><dd>Interpolation-related functions.</dd></dl><h2>Graphics</h2><dl><dt>PDL::Graphics::PGPLOT
</dt><dd>PGPLOT library.
</dd><dt>PDL::Graphics::PLplot
</dt><dd>PLplot library.</dd></dl><h3>3D Graphics</h3><dl><dt>PDL::Graphics::TriD
</dt><dd>3D graphics core module.
</dd><dt>PDL::Graphics::TriD::Rout
</dt><dd>Helper routines for 3D graphics.
</dd><dt>PDL::Graphics::TriD::Contours
</dt><dd>3D surface contours.</dd></dl><h3>Helper Modules</h3><dl><dt>PDL::Graphics::LUT
</dt><dd>Look-up tables.
</dd><dt>PDL::Graphics::IIS
</dt><dd>Display images on IIS devices.
</dd><dt>PDL::Graphics::Limits
</dt><dd>Derive data limits for display purposes.</dd></dl><h2>Image Processing</h2><dl><dt>PDL::Compression
</dt><dd>Compression utilities.
</dd><dt>PDL::Image2D
</dt><dd>2-dimmensional image processing.
</dd><dt>PDL::ImageND
</dt><dd>N-dimmensional image processing.
</dd><dt>PDL::ImageRGB
</dt><dd>RGB image data handling.</dd></dl><h2>Numerical Methods</h2><dl><dt>PDL::FFT
</dt><dd>Fast Fourier Transform (native implementation).
</dd><dt>PDL::FFTW
</dt><dd>PDL interface to the FFTW library.
</dd><dt>PDL::Filter::LinPred
</dt><dd>Linear predictive filtering.
</dd><dt>PDL::Filter::Linear
</dt><dd>Linear filtering.
</dd><dt>PDL::Opt::Simplex
</dt><dd>Simplex optimization routines.
</dd><dt>PDL::Minuit
</dt><dd>PDL interface to the Minuit library.
</dd><dt>PDL::Slatec
</dt><dd>PDL interface to the Slatec library.</dd></dl><h2>Coordinate Transformations</h2><dl><dt>PDL::Transform
</dt><dd>Coordinate transforms, image warping, and N-D functions.
</dd><dt>PDL::Transform::Cartography
</dt><dd>Cartographic projections.
</dd><dt>PDL::Transform::Proj4
</dt><dd>PDL interface to the Proj4 projection library.</dd></dl><h2>Io Functions</h2><dl><dt>PDL::IO
</dt><dd>Overview of IO functions.
</dd><dt>PDL::IO::Dumper
</dt><dd>Data dumper.
</dd><dt>PDL::IO::FastRaw
</dt><dd>Fast storage format (outdated).
</dd><dt>PDL::IO::FlexRaw
</dt><dd>Flexible storage format.
</dd><dt>PDL::IO::Rout
</dt><dd>Misc IO routines.
</dd><dt>PDL::IO::Sortable
</dt><dd>Support for Perl's 'Storable' module.</dd></dl><h3>Image Formats</h3><dl><dt>PDL::IO::FITS
</dt><dd>PDL support for FITS images.
</dd><dt>PDL::IO::PNM
</dt><dd>PDL support for PNM images.
</dd><dt>PDL::IO::GD
</dt><dd>PDL interface to the GD image library.
</dd><dt>PDL::IO::HDF
</dt><dd>PDL interface to the HDH4 image library.
</dd><dt>PDL::IO::NetPBM
</dt><dd>PDL interface to the NetPBM image library.
</dd><dt>PDL::IO::NDF
</dt><dd>PDL interface to the Starlink image library. Available as a separate CPAN download.</dd></dl><h2>2D Matrices</h2><dl><dt>PDL::Matrix
</dt><dd>Convenience class for 2D matrix work.
</dd><dt>PDL::MatrixOps
</dt><dd>Additional matrix operators.</dd></dl><h2>Gnu Scientific Library</h2><dl><dt>PDL::GSL::DIFF
</dt><dd>Numerical differentiation.
</dd><dt>PDL::GSL::INTEG
</dt><dd>Numerical integration.
</dd><dt>PDL::GSL::INTERP
</dt><dd>Interpolation.
</dd><dt>PDL::GSL::MROOT
</dt><dd>Multidimensional root-finding.
</dd><dt>PDL::GSL::RNG
</dt><dd>RNG and randist.</dd></dl><h3>Special Functions</h3><dl><dt>PDL::GSL::AIRY
</dt><dd></dd><dt>PDL::GSL::BESSEL
</dt><dd></dd><dt>PDL::GSL::CLAUSEN
</dt><dd></dd><dt>PDL::GSL::COULOMB
</dt><dd></dd><dt>PDL::GSL::COUPLING
</dt><dd></dd><dt>PDL::GSL::DAWSON
</dt><dd></dd><dt>PDL::GSL::DEBYE
</dt><dd></dd><dt>PDL::GSL::DILOG
</dt><dd></dd><dt>PDL::GSL::ELEMENTARY
</dt><dd></dd><dt>PDL::GSL::ELLINT
</dt><dd></dd><dt>PDL::GSL::ELLJAC
</dt><dd></dd><dt>PDL::GSL::ERF
</dt><dd></dd><dt>PDL::GSL::EXP
</dt><dd></dd><dt>PDL::GSL::EXPINT
</dt><dd></dd><dt>PDL::GSL::FERMI_DIRAC
</dt><dd></dd><dt>PDL::GSL::GAMMA
</dt><dd></dd><dt>PDL::GSL::GEGENBAUER
</dt><dd></dd><dt>PDL::GSL::HYPERG
</dt><dd></dd><dt>PDL::GSL::LAGUERRE
</dt><dd></dd><dt>PDL::GSL::LEGENDRE
</dt><dd></dd><dt>PDL::GSL::LOG
</dt><dd></dd><dt>PDL::GSL::POLY
</dt><dd></dd><dt>PDL::GSL::POW_INT
</dt><dd></dd><dt>PDL::GSL::PSI
</dt><dd></dd><dt>PDL::GSL::SYNCHROTRON
</dt><dd></dd><dt>PDL::GSL::TRANSPORT
</dt><dd></dd><dt>PDL::GSL::TRIG
</dt><dd></dd><dt>PDL::GSL::ZETA
</dt><dd></dd></dl><h2>Fitting Functions</h2><dl><dt>PDL::Fit::Gaussian
</dt><dd>Fit gaussian curves.
</dd><dt>PDL::Fit::Polynomial
</dt><dd>Fit polynomials.
</dd><dt>PDL::Fit::Linfit
</dt><dd>Fit linear combinations of functions.
</dd><dt>PDL::Fit::LM
</dt><dd>Fit functions using the Levenberg-Marquardt algorithm.</dd></dl><h2>Advanced</h2><dl><dt>PDL::Dbg
</dt><dd>PDL debugger.
</dd><dt>PDL::DiskCache
</dt><dd>Manage many piddles through a disk cache.
</dd><dt>PDL::CallExt
</dt><dd>Call external functions.
</dd><dt>PDL::Objects
</dt><dd>If you want to sub-class from PDL (note: incomplete).</dd></dl><h2>Copyright</h2>Copyright 2010 Daniel Carrera (dcarrera [at] gmail.com). You can distribute and/or modify this document under the same terms as the current Perl license. 

 See: <a rel="nofollow" HREF="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a>
