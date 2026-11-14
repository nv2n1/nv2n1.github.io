---
title: "gdal_calc(1)"
name: "gdal_calc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_calc/"
---

<h2 class="name">NAME</h2>
 

 gdal_calc - gdal_calc.py Command line raster calculator with numpy syntax 

<h2>SYNOPSIS</h2>

 

 

 <pre><code>
gdal_calc.py[-A&lt;filename&gt;][--A_band][-B... - Z filename][other_options] Options : -h, --help show this help message and exit-- calc = CALC calculation in gdalnumeric syntax using + -/* or any
                        numpy array functions (i.e. logical_and())
  -A A                  input gdal raster file, note you can use any letter
                        A-Z
  --A_band=A_BAND       number of raster band for file A (default 0)
  --outfile=OUTF        output file to generate or fill
  --NoDataValue=NODATAVALUE
                        set output nodata value (Defaults to datatype specific
                        value)
  --type=TYPE           output datatype, must be one of ['Int32', 'Int16',
                        'Float64', 'UInt16', 'Byte', 'UInt32', 'Float32']
  --format=FORMAT       GDAL format for output file (default 'GTiff')
  --creation-option=CREATION_OPTIONS, --co=CREATION_OPTIONS
                        Passes a creation option to the output format driver.
                        Multiple options may be listed. See format specific
                        documentation for legal creation options for each
                        format.
  --allBands=ALLBANDS   process all bands of given raster (A-Z)
  --overwrite           overwrite output file if it already exists
  --debug               print debugging information
</code></pre> 

<h2>DESCRIPTION</h2>

 

 Command line raster calculator with numpy syntax. Use any basic arithmetic supported by numpy arrays such as +-*\ along with logical operators such as &gt;. Note that all files must have the same dimensions, but no projection checking is performed.

<h2>EXAMPLE</h2>

 

 add two files together 

 <pre>
gdal_calc.py -A input1.tif -B input2.tif --outfile=result.tif --calc=&quot;A+B&quot;
</pre> 

 

 average of two layers 

 <pre>
gdal_calc.py -A input.tif -B input2.tif --outfile=result.tif --calc=&quot;(A+B)/2&quot;
</pre> 

 

 set values of zero and below to null 

 <pre>
gdal_calc.py -A input.tif --outfile=result.tif --calc=&quot;A*(A&gt;0)&quot; --NoDataValue=0
</pre> 

<h2>AUTHORS</h2>

 

 Chris Yesson &lt;chris dot='' yesson='' at='' ioz='' dot='' ac='' dot='' uk&gt;=''&gt; Etienne Tourigny &lt;etourigny dot='' dev='' at='' gmail='' dot='' com&gt;=''&gt; 

<h2>Index</h2>


